#!/usr/bin/env python3
"""Competitor sitemap pull and inventory classification for userandproduct.com (Phase 0).

Free: fetches robots.txt and sitemap XML only, never the pages themselves.
Standard library only. Rerun quarterly (sitemap reuse window is 90 days).

Usage (from the project root):
    python research/seo/tools/sitemaps.py fetch    [--date YYYY-MM-DD] [--section NAME] [--domains a.com,b.com]
                                                   [--skip a.com,b.com] [--force]
    python research/seo/tools/sitemaps.py classify [--date YYYY-MM-DD] [--section NAME] [--domains ...]
    python research/seo/tools/sitemaps.py index    [--date YYYY-MM-DD] [--section NAME] [--domains ...]

Domain list: research/seo/competitors/seeds.csv (section,domain,type,source,note). A domain seeded
for several sections is fetched once and remembers all its sections. --section and --domains filter
the list (both may be combined). Domains in SKIP_FETCH (plus --skip) are not fetched and are
reported with status "skipped".

fetch    -> cache/raw/sitemaps-<date>/<domain>.json    (url list + fetch log; committed)
classify -> competitors/sitemaps/<domain>-sitemap-<date>.csv
            (domain,url,lastmod,first_segment,slug,slug_tokens,year,content)
            competitors/sitemaps-stats-<date>.csv     (one row per domain)
            competitors/slug-tokens-<date>.csv        (token,domains,urls; content URLs only)
index    -> appends one row per fetched domain to cache/index.csv (append mode, never rewrites)
"""
import argparse
import csv
import datetime as dt
import gzip
import html
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, OrderedDict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # research/seo
COMP = os.path.join(ROOT, 'competitors')
RAW = os.path.join(ROOT, 'cache', 'raw')
INDEX = os.path.join(ROOT, 'cache', 'index.csv')
SEEDS = os.path.join(COMP, 'seeds.csv')

# Platform-scale sitemaps, not competitor inventories: millions of user pages, repos, products,
# community files or help-center articles that say nothing about what a publication writes about.
# They are recorded in the stats file with status "skipped" and never fetched.
SKIP_FETCH = {'github.com', 'producthunt.com', 'goodreads.com', 'figma.com', 'notion.so', 'miro.com',
              'atlassian.com', 'surveymonkey.com', 'optimizely.com', 'intercom.com', 'statsig.com'}

UA = 'UserAndProduct-research/1.0 (sitemap inventory; contact: site owner)'
TIMEOUT = 20
DELAY = 1.0
MAX_SUBSITEMAPS = 60
MAX_URLS = 100_000
FALLBACK_PATHS = ['/sitemap.xml', '/sitemap_index.xml', '/wp-sitemap.xml', '/sitemap.xml.gz']
# Yoast/Rank Math sites whose index is disabled still serve these; tried only after the four above
FALLBACK_EXTRA = ['/sitemap-index.xml', '/sitemaps.xml', '/sitemap/', '/post-sitemap.xml', '/page-sitemap.xml', '/product-sitemap.xml',
                  '/category-sitemap.xml']
SKIP_SUB = re.compile(r'image|video|author|(^|[^a-z])tags?([^a-z]|$)|post_tag|attachment|media', re.I)

# ---------------------------------------------------------------- fetching

_last = [0.0]
_insecure = ssl.create_default_context()
_insecure.check_hostname = False
_insecure.verify_mode = ssl.CERT_NONE


def _get(url, log):
    """GET with rate limit, one retry on network/5xx errors. Returns (status, body bytes, note)."""
    for attempt in (1, 2):
        wait = DELAY - (time.time() - _last[0])
        if wait > 0:
            time.sleep(wait)
        _last[0] = time.time()
        req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Encoding': 'gzip'})
        ctx = None
        for ssl_try in (0, 1):
            try:
                with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as r:
                    body = r.read(60_000_000)
                    if r.headers.get('Content-Encoding', '').lower() == 'gzip' or body[:2] == b'\x1f\x8b':
                        try:
                            body = gzip.decompress(body)
                        except OSError:
                            pass
                    log.append([url, r.status, ''])
                    return r.status, body, ''
            except urllib.error.HTTPError as e:
                body = b''
                try:
                    body = e.read(20000)
                except Exception:
                    pass
                cf = ('cloudflare' in (e.headers.get('Server') or '').lower()
                      or b'Just a moment' in body or b'cf-chl' in body or b'challenge-platform' in body)
                note = 'cloudflare' if cf and e.code in (403, 503, 429) else ''
                log.append([url, e.code, note])
                if e.code >= 500 and not cf and attempt == 1:
                    break  # retry once
                return e.code, b'', note
            except (urllib.error.URLError, OSError) as e:
                reason = str(getattr(e, 'reason', e))
                if ssl_try == 0 and 'CERTIFICATE' in reason.upper():
                    ctx = _insecure
                    continue
                log.append([url, 0, reason[:120]])
                if attempt == 1:
                    break
                return 0, b'', reason[:120]
        else:
            continue
    return 0, b'', 'failed'


LOC_BLOCK = {
    'url': re.compile(r'<(?:\w+:)?url>(.*?)</(?:\w+:)?url>', re.S | re.I),
    'sitemap': re.compile(r'<(?:\w+:)?sitemap>(.*?)</(?:\w+:)?sitemap>', re.S | re.I),
}
LOC = re.compile(r'<loc>\s*(.*?)\s*</loc>', re.S | re.I)
LOC_NS = re.compile(r'<\w+:loc>\s*(.*?)\s*</\w+:loc>', re.S | re.I)
LASTMOD = re.compile(r'<(?:\w+:)?lastmod>\s*(.*?)\s*</(?:\w+:)?lastmod>', re.S | re.I)


def _clean(s):
    s = s.strip()
    if s.startswith('<![CDATA['):
        s = s[9:].rstrip(']>').rstrip(']')
    return html.unescape(s).strip()


def parse_sitemap(body):
    """Return ('index'|'urlset'|'text'|'none', [(loc, lastmod)])."""
    text = body.decode('utf-8', 'replace')
    head = text[:3000].lower()
    kind = 'index' if '<sitemapindex' in head or '<sitemapindex' in text[:20000].lower() else None
    if kind is None and '<urlset' in text[:20000].lower():
        kind = 'urlset'
    if kind:
        out = []
        for m in LOC_BLOCK['sitemap' if kind == 'index' else 'url'].finditer(text):
            blk = m.group(1)
            lm = LOC.search(blk) or LOC_NS.search(blk)
            if not lm:
                continue
            mod = LASTMOD.search(blk)
            out.append((_clean(lm.group(1)), _clean(mod.group(1))[:10] if mod else ''))
        return kind, out
    if '<html' in head or '<!doctype' in head:
        return 'none', []
    lines = [l.strip() for l in text.splitlines() if l.strip().startswith('http')]
    return ('text', [(l, '') for l in lines]) if lines else ('none', [])


def fetch_domain(domain):
    log, sitemaps_seen, notes = [], [], []
    urls = {}
    status = 'none'
    base = 'https://' + domain
    code, body, note = _get(base + '/robots.txt', log)
    if code == 0 and not domain.startswith('www.'):
        base = 'https://www.' + domain
        code, body, note = _get(base + '/robots.txt', log)
    blocked_hits = 0
    if code in (401, 403, 429) or note == 'cloudflare':
        blocked_hits += 1
    starts = []
    if code == 200:
        for line in body.decode('utf-8', 'replace').splitlines():
            m = re.match(r'\s*sitemap\s*:\s*(\S+)', line, re.I)
            if m and m.group(1) not in starts:
                starts.append(m.group(1))
    source = 'robots' if starts else 'fallback'
    queue = [(u, 0) for u in starts if not SKIP_SUB.search(urllib.parse.urlparse(u).path)]
    fallback_mode = not queue
    if fallback_mode:
        queue = [(base + p, 0) for p in FALLBACK_PATHS]
    fetched = 0
    truncated = False
    extra_done = False
    while True:
        if not queue:
            if not urls and not fallback_mode:
                fallback_mode = True
                notes.append('robots sitemaps failed; tried fallback paths')
                queue = [(base + p, 0) for p in FALLBACK_PATHS]
                continue
            if not urls and not extra_done:
                extra_done = True
                queue = [(base + p, 0) for p in FALLBACK_EXTRA]
                continue
            break
        sm, depth = queue.pop(0)
        if sm in sitemaps_seen:
            continue
        if fetched >= MAX_SUBSITEMAPS:
            truncated = True
            notes.append('sub-sitemap cap %d reached' % MAX_SUBSITEMAPS)
            break
        sitemaps_seen.append(sm)
        fetched += 1
        code, body, note = _get(sm, log)
        if code in (401, 403, 429) or note == 'cloudflare':
            blocked_hits += 1
            continue
        if code != 200:
            if sm.startswith('http://'):
                queue.insert(0, ('https://' + sm[7:], depth))
            continue
        kind, items = parse_sitemap(body)
        if kind == 'index':
            subs = [loc for loc, _ in items]
            keep = [s for s in subs if not SKIP_SUB.search(urllib.parse.urlparse(s).path + '?' + urllib.parse.urlparse(s).query)]
            skipped = len(subs) - len(keep)
            if skipped:
                notes.append('skipped %d image/video/author/tag/attachment sub-sitemaps' % skipped)
            if depth < 4:
                queue.extend((s, depth + 1) for s in keep)
        elif kind in ('urlset', 'text'):
            subname = urllib.parse.urlparse(sm).path.rsplit('/', 1)[-1]
            for loc, mod in items:
                if loc not in urls:
                    urls[loc] = (mod, subname)
                if len(urls) >= MAX_URLS:
                    truncated = True
                    notes.append('url cap %d reached' % MAX_URLS)
                    break
        if len(urls) >= MAX_URLS:
            break
        if (fallback_mode and urls and not any(q[1] > 0 for q in queue)
                and not any(sm.endswith(x) for x in FALLBACK_EXTRA)):
            break  # first working standard fallback path is enough
    if urls:
        status = 'ok'
    elif blocked_hits:
        status = 'blocked'
    net = [l for l in log if l[1] == 0]
    if not urls and net and len(net) == len(log):
        status = 'blocked'
        notes.append('network error: ' + str(net[0][2]))
    return {
        'domain': domain, 'status': status, 'source': source, 'truncated': truncated,
        'sitemaps': sitemaps_seen, 'notes': sorted(set(notes)), 'log': log,
        'urls': [[u, m, s] for u, (m, s) in urls.items()],
    }



# ---------------------------------------------------------------- domain list

def load_seeds():
    """Ordered {domain: [sections]} from seeds.csv, deduped across sections."""
    seeds = OrderedDict()
    with open(SEEDS, newline='', encoding='utf-8') as f:
        for r in csv.DictReader(f):
            d = (r.get('domain') or '').strip().lower()
            s = (r.get('section') or '').strip().lower()
            if not d:
                continue
            seeds.setdefault(d, [])
            if s and s not in seeds[d]:
                seeds[d].append(s)
    return seeds


def load_domains(args):
    """Filtered {domain: [sections]}; --domains not in seeds.csv are kept with no section."""
    seeds = load_seeds()
    if args.domains:
        wanted = [d.strip().lower() for d in args.domains.split(',') if d.strip()]
        seeds = OrderedDict((d, seeds.get(d, [])) for d in wanted)
    if args.section:
        sec = args.section.strip().lower()
        seeds = OrderedDict((d, s) for d, s in seeds.items() if sec in s)
    return seeds


def skip_set(args):
    extra = {d.strip().lower() for d in (args.skip or '').split(',') if d.strip()}
    return SKIP_FETCH | extra


def cmd_fetch(args):
    outdir = os.path.join(RAW, 'sitemaps-' + args.date)
    os.makedirs(outdir, exist_ok=True)
    doms = list(load_domains(args))
    skip = skip_set(args)
    tally = Counter()
    for i, d in enumerate(doms, 1):
        if d in skip:
            tally['skipped'] += 1
            print('[%d/%d] %s skipped (platform-scale sitemap)' % (i, len(doms), d), flush=True)
            continue
        path = os.path.join(outdir, d + '.json')
        if os.path.exists(path) and not args.force:
            with open(path, encoding='utf-8') as f:
                tally[json.load(f)['status']] += 1
            continue
        t0 = time.time()
        try:
            res = fetch_domain(d)
        except Exception as e:  # never stop the run for one domain
            res = {'domain': d, 'status': 'none', 'source': '', 'truncated': False, 'sitemaps': [],
                   'notes': ['script error: %r' % e], 'log': [], 'urls': []}
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(res, f)
        tally[res['status']] += 1
        print('[%d/%d] %s %s urls=%d subs=%d %.0fs %s' % (
            i, len(doms), d, res['status'], len(res['urls']), len(res['sitemaps']),
            time.time() - t0, '; '.join(res['notes'])[:120]), flush=True)
        if i % 20 == 0:
            print('PROGRESS %d/%d %s' % (i, len(doms), dict(tally)), flush=True)
    print('DONE', dict(tally), flush=True)


# ---------------------------------------------------------------- classifying

# Slugs (last path segment) that are site furniture, not content.
NONCONTENT = {'about', 'about-us', 'aboutus', 'privacy', 'privacy-policy', 'terms', 'terms-of-use',
              'terms-of-service', 'terms-and-conditions', 'tos', 'contact', 'contact-us', 'cart',
              'basket', 'checkout', 'account', 'my-account', 'login', 'log-in', 'register', 'signup',
              'sign-up', 'sign-in', 'wishlist', 'faq', 'faqs', 'disclaimer', 'cookie-policy', 'cookies',
              'sitemap', 'site-map', 'affiliate', 'affiliates', 'advertise', 'dmca', 'copyright',
              'accessibility', 'search', 'subscribe', 'newsletter', 'members', 'membership',
              'thank-you', 'thanks', 'feed', 'author', 'authors', 'tag', 'tags', 'user', 'users',
              'profile', 'donate', 'press', 'careers', 'legal', 'refund-policy', 'shipping',
              'returns', 'terms-conditions', 'privacy-notice', 'cookie', 'join', 'my-downloads',
              'unsubscribe', 'shop', 'store', 'pricing', 'upgrade', 'lost-password', 'order',
              'orders', 'gdpr', 'ccpa', 'do-not-sell', 'licensing', 'license', 'terms-of-use-2',
              'imprint', 'impressum', 'wp-login-php', 'cgi-bin', 'feedback', 'support', 'help'}

# Platform noise: any path segment in this set makes the URL noncontent (feeds, pagination, REST
# endpoints, author/tag/category archives, search, AMP and attachment duplicates, comment pages).
NOISE_SEGMENTS = {'feed', 'feeds', 'rss', 'atom', 'page', 'wp-json', 'wp-content', 'wp-admin',
                  'wp-includes', 'xmlrpc.php', 'author', 'authors', 'tag', 'tags', 'tagged', 'category',
                  'categories', 'search', 'amp', 'attachment', 'trackback', 'comments', 'embed',
                  'cdn-cgi', 'cart', 'checkout', 'login', 'signup', 'account', 'user', 'users',
                  'profile', 'profiles', 'jobs', 'job', 'careers', 'changelog', 'release-notes', 'releases',
                  'press-releases', 'docs', 'developers', 'support', 'help', 'help-center'}
# 'archive' is not noise by itself: some publications keep every article under /archives/YYYY/MM/;
# the date-only archive pages are caught by the empty-slug rule in classify_url().

# Non-English locale prefixes: kept in the CSV but flagged noncontent so the token table stays English.
LOCALES = {'de', 'fr', 'es', 'it', 'pt', 'pt-br', 'br', 'ja', 'jp', 'ko', 'kr', 'zh', 'zh-cn', 'zh-tw',
           'zh-hans', 'zh-hant', 'cn', 'tw', 'nl', 'ru', 'pl', 'tr', 'sv', 'da', 'fi', 'no', 'nb', 'cs',
           'hu', 'ro', 'id', 'th', 'vi', 'uk-ua', 'ua', 'ar', 'he', 'es-es', 'es-la', 'es-mx', 'fr-fr',
           'fr-ca', 'de-de', 'it-it', 'ja-jp', 'ko-kr', 'nl-nl', 'pt-pt', 'sv-se', 'pl-pl', 'tr-tr',
           'fa', 'hi', 'el', 'bg', 'sk', 'sl', 'hr', 'sr', 'lt', 'lv', 'et', 'ms', 'fil', 'ca'}

FILE_EXT = re.compile(r'\.(html?|php|aspx?|jsp)$', re.I)
ASSET_EXT = re.compile(r'\.(xml|json|rss|txt|pdf|jpe?g|png|gif|webp|svg|mp4|mp3|zip|csv|xlsx?|docx?|pptx?)$',
                       re.I)
YEAR = re.compile(r'(?<!\d)(199\d|20[0-2]\d)(?!\d)')

STOPWORDS = set("""
a about above after again against all also am an and any are aren as at be because been before being
below between both but by can cannot could did didn do does doesn doing don down during each few for
from further get gets got had has hasn have haven having he her here hers herself him himself his how
i if in into is isn it its itself just let lets ll me more most my myself no nor not now of off on once
only or other ought our ours ourselves out over own re same she should so some such than that thats
the their theirs them themselves then there these they this those through to too under until up upon
us ve very via was wasn we were weren what when where which while who whom why will with without won
would you your yours yourself yourselves
html htm php aspx asp jsp www http https com org net amp utm ref index default
blog post posts page pages article articles home view
one two three use using need make making made get good first right end real time way ways new like
know things thing much many really every even still back part look take want see think going keep
""".split())

TOKEN_RE = re.compile(r'[a-z0-9]+')


def split_url(url):
    """Return (segments, query) with segments lowercased and percent-decoded."""
    p = urllib.parse.urlparse(url)
    segs = [urllib.parse.unquote(s).lower() for s in p.path.split('/') if s]
    return segs, p.query


def raw_tokens(slug):
    return TOKEN_RE.findall(slug.lower())


def clean_tokens(tokens):
    """Topic tokens: no stopwords, no numbers, no ids or hashes, at least 3 characters."""
    out = []
    for t in tokens:
        if len(t) < 3 or t in STOPWORDS or t.isdigit():
            continue
        digits = sum(c.isdigit() for c in t)
        if digits and (len(t) >= 8 or digits * 2 >= len(t)):
            continue  # ids and hashes such as Medium's trailing 12-character hex
        if len(t) >= 10 and re.fullmatch(r'[0-9a-f]+', t):
            continue
        out.append(t)
    return out


def classify_url(url):
    """Return (segments, first_segment, slug, raw token list, year, content flag)."""
    segs, query = split_url(url)
    first = segs[0] if segs else ''
    slug = FILE_EXT.sub('', segs[-1]) if segs else ''
    toks = raw_tokens(slug)
    m = YEAR.search('/'.join(segs))
    year = m.group(1) if m else ''
    content = 'content'
    if not segs:
        content = 'noncontent'  # home page
    elif any(s in NOISE_SEGMENTS for s in segs) or any(s.startswith('@') for s in segs):
        content = 'noncontent'
    elif slug in NONCONTENT or first in ('wp-login.php', 'cgi-bin'):
        content = 'noncontent'
    elif first in LOCALES:
        content = 'noncontent'
    elif ASSET_EXT.search(segs[-1]):
        content = 'noncontent'
    elif re.search(r'(^|&)(s|q|page|paged|replytocom|share)=', query or ''):
        content = 'noncontent'
    elif not clean_tokens(toks):
        content = 'noncontent'  # numeric, id-only or empty slug carries no topic
    return segs, first, slug, toks, year, content


def read_raw(rawdir, d):
    path = os.path.join(rawdir, d + '.json')
    if not os.path.exists(path):
        return None
    with open(path, encoding='utf-8') as f:
        return json.load(f)


def valid_date(s):
    return s if re.fullmatch(r'\d{4}-\d{2}-\d{2}', s or '') else ''


def cmd_classify(args):
    rawdir = os.path.join(RAW, 'sitemaps-' + args.date)
    outdir = os.path.join(COMP, 'sitemaps')
    os.makedirs(outdir, exist_ok=True)
    doms = load_domains(args)
    skip = skip_set(args)
    run_day = dt.date.fromisoformat(args.date)
    cutoff = (run_day - dt.timedelta(days=365)).isoformat()
    future = (run_day + dt.timedelta(days=1)).isoformat()
    stats = []
    tok_domains = {}
    tok_urls = Counter()
    for d, sections in doms.items():
        row = {'domain': d, 'sections': ' '.join(sections), 'status': '', 'total_urls': 0,
               'content_urls': 0, 'lastmod_12m': 0, 'newest_lastmod': '', 'top_segments': '',
               'notes': ''}
        if d in skip:
            row['status'] = 'skipped'
            row['notes'] = 'platform-scale sitemap, not a competitor inventory; not fetched'
            stats.append(row)
            continue
        res = read_raw(rawdir, d)
        if res is None:
            row['status'] = 'missing'
            row['notes'] = 'no fetch file for this date'
            stats.append(row)
            continue
        notes = list(res.get('notes', []))
        if res.get('truncated'):
            notes.append('capped')
        if res['status'] != 'ok':
            bad = [l for l in res.get('log', []) if l[1] != 200][:1]
            if bad:
                notes.append('first failure %s %s' % (bad[0][1], bad[0][2]))
        seg_counts = Counter()
        newest = ''
        n_future = 0
        rows = []
        for url, mod, _sub in res['urls']:
            segs, first, slug, toks, year, content = classify_url(url)
            mod = valid_date(mod)
            if mod and mod > future:
                n_future += 1
            elif mod and mod > newest:
                newest = mod
            rows.append([d, url, mod, first, slug, ' '.join(toks), year, content])
            if content == 'content':
                row['content_urls'] += 1
                seg_counts[first if len(segs) > 1 else '(root)'] += 1
                if mod and cutoff <= mod <= future:
                    row['lastmod_12m'] += 1
                for t in set(clean_tokens(toks)):
                    tok_urls[t] += 1
                    tok_domains.setdefault(t, set()).add(d)
        if n_future:
            notes.append('%d lastmod dates in the future ignored' % n_future)
        row['status'] = res['status']
        row['total_urls'] = len(rows)
        row['newest_lastmod'] = newest
        row['top_segments'] = '; '.join('%s %d' % kv for kv in seg_counts.most_common(5))
        row['notes'] = '; '.join(notes)
        stats.append(row)
        if rows:
            path = os.path.join(outdir, '%s-sitemap-%s.csv' % (d, args.date))
            with open(path, 'w', encoding='utf-8', newline='') as f:
                w = csv.writer(f)
                w.writerow(['domain', 'url', 'lastmod', 'first_segment', 'slug', 'slug_tokens', 'year',
                            'content'])
                w.writerows(rows)
        print('%-28s %-8s total=%-7d content=%-7d 12m=%-6d %s' % (
            d, row['status'], row['total_urls'], row['content_urls'], row['lastmod_12m'],
            row['top_segments'][:60]), flush=True)

    cols = ['domain', 'sections', 'status', 'total_urls', 'content_urls', 'lastmod_12m',
            'newest_lastmod', 'top_segments', 'notes']
    with open(os.path.join(COMP, 'sitemaps-stats-%s.csv' % args.date), 'w', encoding='utf-8',
              newline='') as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(stats)

    # Ranked by spread first (distinct domains), then volume, so one large site cannot dominate.
    ranked = sorted(tok_urls, key=lambda t: (-len(tok_domains[t]), -tok_urls[t], t))[:2000]
    with open(os.path.join(COMP, 'slug-tokens-%s.csv' % args.date), 'w', encoding='utf-8',
              newline='') as f:
        w = csv.writer(f)
        w.writerow(['token', 'domains', 'urls'])
        for t in ranked:
            w.writerow([t, len(tok_domains[t]), tok_urls[t]])
    print('stats rows %d; tokens written %d of %d' % (len(stats), len(ranked), len(tok_urls)))


# ---------------------------------------------------------------- index

def cmd_index(args):
    rawdir = os.path.join(RAW, 'sitemaps-' + args.date)
    yymmdd = args.date[2:].replace('-', '')
    existing = 0
    with open(INDEX, encoding='utf-8') as f:
        for line in f:
            m = re.match(r'%s-(\d{3}),' % yymmdd, line)
            if m:
                existing = max(existing, int(m.group(1)))
    skip = skip_set(args)
    lines = []
    n = existing
    for d, sections in load_domains(args).items():
        if d in skip:
            continue
        res = read_raw(rawdir, d)
        if res is None:
            continue
        n += 1
        note = '%s; %d urls; %d sitemaps; sections %s; free' % (
            res['status'], len(res['urls']), len(res['sitemaps']), ' '.join(sections) or '-')
        if res['truncated']:
            note += '; capped'
        if res['status'] != 'ok':
            bad = [l for l in res['log'] if l[1] != 200][:1]
            if bad:
                note += '; first failure %s %s' % (bad[0][1], bad[0][2])
        if res['urls']:
            fname = 'competitors/sitemaps/%s-sitemap-%s.csv' % (d, args.date)
        else:
            fname = 'cache/raw/sitemaps-%s/%s.json' % (args.date, d)
        buf = []
        csv.writer(_Buf(buf), lineterminator='\n').writerow(
            ['%s-%03d' % (yymmdd, n), args.date, 'sitemap', 'sitemaps.py fetch', d, '', fname, note])
        lines.append(''.join(buf))
    with open(INDEX, 'rb') as f:
        f.seek(-1, os.SEEK_END)
        needs_nl = f.read(1) != b'\n'
    with open(INDEX, 'a', encoding='utf-8', newline='') as f:  # append only, one write
        f.write(('\n' if needs_nl else '') + ''.join(lines))
    print('appended', len(lines), 'rows')


class _Buf:
    def __init__(self, buf):
        self.buf = buf

    def write(self, s):
        self.buf.append(s)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('cmd', choices=['fetch', 'classify', 'index'])
    ap.add_argument('--date', default=dt.date.today().isoformat())
    ap.add_argument('--section', default='', help='only domains seeded for this section')
    ap.add_argument('--domains', default='', help='comma-separated domains (overrides the seeds.csv list)')
    ap.add_argument('--skip', default='', help='extra comma-separated domains to skip (added to SKIP_FETCH)')
    ap.add_argument('--force', action='store_true', help='refetch domains already on disk')
    args = ap.parse_args()
    {'fetch': cmd_fetch, 'classify': cmd_classify, 'index': cmd_index}[args.cmd](args)


if __name__ == '__main__':
    main()
