#!/usr/bin/env python3
"""Google Search Console pulls for https://userandproduct.com.

Every command is read-only except `sitemaps --submit [URL]`, the single write path
(PUT sitemaps/{feedpath}; default URL https://userandproduct.com/sitemap_index.xml).

Writes into research/seo/cache/gsc/ and logs one row per session to
research/seo/cache/index.csv (source "gsc", free calls).

Usage:
    python research/seo/tools/gsc.py sites
    python research/seo/tools/gsc.py sitemaps
    python research/seo/tools/gsc.py sitemaps --submit [URL]     (WRITE: submit a sitemap)
    python research/seo/tools/gsc.py performance [--days 28] [--dimension page|query|page,query|date]
    python research/seo/tools/gsc.py inspect [--urls FILE | --from-sitemap] [--limit 600]
    python research/seo/tools/gsc.py summary
    python research/seo/tools/gsc.py all

Credentials: service account JSON at .local/gsc-service-account.json (override with env GSC_KEY).
The key file is never printed; only client_email is shown in permission errors.
"""
import argparse
import csv
import datetime as dt
import json
import os
import sys
import time
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from urllib.parse import quote as urlquote

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
KEY_PATH = os.environ.get('GSC_KEY') or os.path.join(ROOT, '.local', 'gsc-service-account.json')
CACHE = os.path.join(ROOT, 'research', 'seo', 'cache')
OUT = os.path.join(CACHE, 'gsc')
INDEX = os.path.join(CACHE, 'index.csv')
INSPECT_CSV = os.path.join(OUT, 'inspect.csv')

SITE_HOST = 'userandproduct.com'
CANDIDATES = ['sc-domain:userandproduct.com', 'https://userandproduct.com/']
SITEMAP_INDEX = 'https://userandproduct.com/sitemap_index.xml'
SCOPES = ['https://www.googleapis.com/auth/webmasters']
WM = 'https://www.googleapis.com/webmasters/v3'
INSPECT_API = 'https://searchconsole.googleapis.com/v1/urlInspection/index:inspect'
BROWSER_UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
              '(KHTML, like Gecko) Chrome/128.0 Safari/537.36')
INSPECT_COLS = ['url', 'verdict', 'coverageState', 'indexingState', 'robotsTxtState',
                'pageFetchState', 'lastCrawlTime', 'googleCanonical', 'userCanonical',
                'crawledAs', 'referringUrls', 'inspected_at']
TODAY = dt.date.today().isoformat()


class PermissionDenied(Exception):
    pass


class Client:
    def __init__(self):
        if not os.path.isfile(KEY_PATH):
            sys.exit('Key file not found: %s (set GSC_KEY to override the path).' % KEY_PATH)
        try:
            from google.oauth2 import service_account
            from google.auth.transport.requests import AuthorizedSession
        except ImportError:
            sys.exit('Missing packages. Run: pip install --user google-auth requests')
        with open(KEY_PATH, encoding='utf-8') as fh:
            info = json.load(fh)
        self.email = info.get('client_email', '(unknown)')
        creds = service_account.Credentials.from_service_account_info(info, scopes=SCOPES)
        del info
        self.session = AuthorizedSession(creds)
        self.calls = 0

    def request(self, method, url, body=None, allow=()):
        """JSON request with 429/5xx backoff. Returns (status, data)."""
        delay = 2.0
        for attempt in range(6):
            self.calls += 1
            resp = self.session.request(method, url, json=body, timeout=60)
            if resp.status_code == 429 or resp.status_code >= 500:
                if attempt == 5:
                    break
                time.sleep(delay)
                delay *= 2
                continue
            try:
                data = resp.json()
            except ValueError:
                data = {'raw': resp.text[:500]}
            if resp.status_code == 403 and 403 not in allow:
                if 'sufficient permission' in json.dumps(data).lower():
                    raise PermissionDenied()
            if resp.status_code >= 400 and resp.status_code not in allow:
                err = data.get('error', {}) if isinstance(data, dict) else {}
                raise RuntimeError('HTTP %s on %s: %s' % (resp.status_code, url,
                                                          err.get('message', str(data)[:300])))
            return resp.status_code, data
        raise RuntimeError('Gave up after repeated 429/5xx on %s' % url)


def quote(site):
    return urlquote(site, safe='')


def rel(path):
    return os.path.relpath(path, CACHE).replace('\\', '/')


def log_session(command, site, calls, rows, file_rel, extra=''):
    """One row per API session in cache/index.csv (id,date,source,endpoint,subject,location,file,note)."""
    prefix = dt.date.today().strftime('%y%m%d') + '-gsc-'
    n = 0
    if os.path.isfile(INDEX):
        with open(INDEX, encoding='utf-8', newline='') as fh:
            for row in csv.reader(fh):
                if row and row[0].startswith(prefix):
                    n += 1
    with open(INDEX, 'a', encoding='utf-8', newline='') as fh:
        csv.writer(fh).writerow(['%s%02d' % (prefix, n + 1), TODAY, 'gsc', command, site, 'global',
                                 file_rel, 'free; calls %d; rows %d%s'
                                 % (calls, rows, '; ' + extra if extra else '')])


def pick_site(c):
    _, data = c.request('GET', WM + '/sites')
    entries = data.get('siteEntry', [])
    owned = {e['siteUrl']: e.get('permissionLevel') for e in entries}
    for cand in CANDIDATES:
        if cand in owned and owned[cand] != 'siteUnverifiedUser':
            return cand, entries
    for e in entries:
        if SITE_HOST in e['siteUrl'] and e.get('permissionLevel') != 'siteUnverifiedUser':
            return e['siteUrl'], entries
    # Not listed: probe the candidates directly (403/404 means try the next one).
    for cand in CANDIDATES:
        status, _ = c.request('GET', WM + '/sites/' + quote(cand), allow=(403, 404))
        if status == 200:
            return cand, entries
    return None, entries


def cmd_sites(c):
    site, entries = pick_site(c)
    print('## Properties visible to %s\n' % c.email)
    if not entries:
        print('(none)')
    for e in entries:
        print('- %s  (%s)' % (e['siteUrl'], e.get('permissionLevel')))
    print('\nMatched property: %s' % (site or 'NONE'))
    return site


def cmd_sitemaps(c, site):
    _, data = c.request('GET', WM + '/sites/%s/sitemaps' % quote(site))
    maps = data.get('sitemap', [])
    path = os.path.join(OUT, 'sitemaps-%s.json' % TODAY)
    with open(path, 'w', encoding='utf-8') as fh:
        json.dump(maps, fh, indent=2)
    print('\n## Sitemaps (%d)\n' % len(maps))
    for m in maps:
        contents = ', '.join('%s %s submitted / %s indexed' % (x.get('type'), x.get('submitted'),
                                                               x.get('indexed', '-'))
                             for x in m.get('contents', []))
        print('- %s | submitted %s | downloaded %s | errors %s | warnings %s | pending %s | %s'
              % (m.get('path'), m.get('lastSubmitted'), m.get('lastDownloaded'), m.get('errors'),
                 m.get('warnings'), m.get('isPending'), contents))
    return len(maps), rel(path)


def cmd_submit(c, site, feed):
    """The only write call in this script: PUT sites/{site}/sitemaps/{feed}, then re-list."""
    print('## Submitting %s to %s' % (feed, site))
    status, _ = c.request('PUT', WM + '/sites/%s/sitemaps/%s' % (quote(site), quote(feed)))
    print('PUT returned HTTP %s' % status)
    n, f = cmd_sitemaps(c, site)
    entry = None
    try:
        with open(os.path.join(CACHE, f), encoding='utf-8') as fh:
            entry = next((m for m in json.load(fh) if m.get('path') == feed), None)
    except (OSError, ValueError):
        pass
    print('\n## Submitted entry\n')
    if not entry:
        print('(not listed yet; Search Console may take a moment to show it)')
    else:
        for k in ('path', 'lastSubmitted', 'lastDownloaded', 'isPending', 'isSitemapsIndex',
                  'errors', 'warnings'):
            print('- %s: %s' % (k, entry.get(k)))
        for x in entry.get('contents', []):
            print('- contents: %s %s submitted / %s indexed'
                  % (x.get('type'), x.get('submitted'), x.get('indexed', '-')))
    return n, f


def cmd_performance(c, site, days, dimension):
    end = dt.date.today() - dt.timedelta(days=2)
    start = end - dt.timedelta(days=days - 1)
    dims = dimension.split(',')
    rows, start_row = [], 0
    while True:
        body = {'startDate': start.isoformat(), 'endDate': end.isoformat(), 'dimensions': dims,
                'rowLimit': 25000, 'startRow': start_row, 'dataState': 'all'}
        _, data = c.request('POST', WM + '/sites/%s/searchAnalytics/query' % quote(site), body)
        batch = data.get('rows', [])
        rows.extend(batch)
        if len(batch) < 25000:
            break
        start_row += 25000
    name = 'performance-%s-%s.csv' % (dimension.replace(',', '-'), TODAY)
    path = os.path.join(OUT, name)
    with open(path, 'w', encoding='utf-8', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(dims + ['clicks', 'impressions', 'ctr', 'position', 'start', 'end'])
        for r in rows:
            w.writerow(r['keys'] + [r.get('clicks', 0), r.get('impressions', 0),
                                    round(r.get('ctr', 0), 4), round(r.get('position', 0), 2),
                                    start.isoformat(), end.isoformat()])
    print('\n## Performance by %s, %s to %s: %d rows -> %s'
          % (dimension, start, end, len(rows), name))
    return len(rows), rel(path)


def fetch_xml(url):
    import requests
    resp = requests.get(url, headers={'User-Agent': BROWSER_UA,
                                      'Accept': 'application/xml,text/xml,*/*'}, timeout=60)
    resp.raise_for_status()
    return ET.fromstring(resp.content)


def sitemap_urls():
    ns = '{http://www.sitemaps.org/schemas/sitemap/0.9}'
    root = fetch_xml(SITEMAP_INDEX)
    urls = []
    if root.tag.endswith('sitemapindex'):
        for loc in root.iter(ns + 'loc'):
            child = fetch_xml(loc.text.strip())
            urls.extend(x.text.strip() for x in child.iter(ns + 'loc') if x.text)
    else:
        urls.extend(x.text.strip() for x in root.iter(ns + 'loc') if x.text)
    seen, out = set(), []
    for u in urls:
        if u not in seen:
            seen.add(u)
            out.append(u)
    return out


def load_inspect():
    rows = {}
    if os.path.isfile(INSPECT_CSV):
        with open(INSPECT_CSV, encoding='utf-8', newline='') as fh:
            for r in csv.DictReader(fh):
                rows[r['url']] = r
    return rows


def save_inspect(rows):
    tmp = INSPECT_CSV + '.tmp'
    with open(tmp, 'w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=INSPECT_COLS)
        w.writeheader()
        for u in sorted(rows):
            w.writerow({k: rows[u].get(k, '') for k in INSPECT_COLS})
    os.replace(tmp, INSPECT_CSV)


def cmd_inspect(c, site, urls_file, limit):
    if urls_file:
        with open(urls_file, encoding='utf-8') as fh:
            urls = [x.strip() for x in fh if x.strip() and not x.startswith('#')]
    else:
        urls = sitemap_urls()
    cache = load_inspect()
    cutoff = dt.datetime.now() - dt.timedelta(days=7)
    todo = []
    for u in urls:
        prev = cache.get(u, {}).get('inspected_at', '')
        try:
            if prev and dt.datetime.fromisoformat(prev) > cutoff:
                continue
        except ValueError:
            pass
        todo.append(u)
    print('\n## Inspect: %d URLs in source, %d due, limit %d' % (len(urls), len(todo), limit))
    done = errors = 0
    for u in todo[:limit]:
        try:
            _, data = c.request('POST', INSPECT_API, {'inspectionUrl': u, 'siteUrl': site})
        except PermissionDenied:
            raise
        except Exception as exc:  # keep going on single-URL errors
            errors += 1
            print('  error %s: %s' % (u, exc))
            continue
        res = data.get('inspectionResult', {}).get('indexStatusResult', {})
        cache[u] = {
            'url': u, 'verdict': res.get('verdict', ''),
            'coverageState': res.get('coverageState', ''),
            'indexingState': res.get('indexingState', ''),
            'robotsTxtState': res.get('robotsTxtState', ''),
            'pageFetchState': res.get('pageFetchState', ''),
            'lastCrawlTime': res.get('lastCrawlTime', ''),
            'googleCanonical': res.get('googleCanonical', ''),
            'userCanonical': res.get('userCanonical', ''),
            'crawledAs': res.get('crawledAs', ''),
            'referringUrls': len(res.get('referringUrls', []) or []),
            'inspected_at': dt.datetime.now().replace(microsecond=0).isoformat(),
        }
        done += 1
        if done % 25 == 0:
            save_inspect(cache)
            print('  %d inspected' % done)
        time.sleep(0.3)
    save_inspect(cache)
    print('  inspected %d, errors %d, skipped (fresh) %d, left for later %d'
          % (done, errors, len(urls) - len(todo), max(0, len(todo) - limit)))
    return done, rel(INSPECT_CSV)


def latest(prefix):
    if not os.path.isdir(OUT):
        return None
    files = sorted(f for f in os.listdir(OUT) if f.startswith(prefix) and f.endswith('.csv'))
    return os.path.join(OUT, files[-1]) if files else None


def top_rows(path, key, n=20):
    if not path:
        return []
    with open(path, encoding='utf-8', newline='') as fh:
        rows = list(csv.DictReader(fh))
    rows.sort(key=lambda r: (-float(r['clicks']), -float(r['impressions'])))
    return [(r[key], r['clicks'], r['impressions'], r['ctr'], r['position']) for r in rows[:n]]


def cmd_summary():
    lines = ['# Search Console summary, %s' % TODAY, '']
    rows = list(load_inspect().values())
    counts = Counter(r['coverageState'] or '(blank)' for r in rows)
    lines += ['## URL Inspection: coverage states (%d URLs in inspect.csv)' % len(rows), '',
              '| coverageState | URLs |', '|---|---|']
    lines += ['| %s | %d |' % (k, v) for k, v in counts.most_common()]
    groups = defaultdict(list)
    for r in rows:
        if r['coverageState'] != 'Submitted and indexed':
            groups[r['coverageState'] or '(blank)'].append(r['url'])
    lines += ['', '## Not "Submitted and indexed"', '']
    if not groups:
        lines.append('(none)')
    for state in sorted(groups, key=lambda s: -len(groups[s])):
        lines += ['### %s (%d)' % (state, len(groups[state])), '']
        lines += ['- %s' % u for u in sorted(groups[state])]
        lines.append('')
    for label, prefix, key in (('pages', 'performance-page-', 'page'),
                               ('queries', 'performance-query-', 'query')):
        path = latest(prefix)
        top = top_rows(path, key)
        lines += ['', '## Top 20 %s by clicks, then impressions (%s)'
                  % (label, os.path.basename(path) if path else 'no pull yet'), '']
        if not top:
            lines.append('(no rows)')
            continue
        lines += ['| %s | clicks | impressions | ctr | position |' % key, '|---|---|---|---|---|']
        lines += ['| %s | %s | %s | %s | %s |' % t for t in top]
    text = '\n'.join(lines) + '\n'
    path = os.path.join(OUT, 'summary-%s.md' % TODAY)
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(text)
    print('\n' + text)
    return path


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest='cmd', required=True)
    sub.add_parser('sites')
    ps = sub.add_parser('sitemaps')
    ps.add_argument('--submit', nargs='?', const=SITEMAP_INDEX, default=None, metavar='URL',
                    help='WRITE: submit a sitemap (default %s); the only write path' % SITEMAP_INDEX)
    pp = sub.add_parser('performance')
    pp.add_argument('--days', type=int, default=28)
    pp.add_argument('--dimension', default='page', choices=['page', 'query', 'page,query', 'date'])
    pi = sub.add_parser('inspect')
    g = pi.add_mutually_exclusive_group()
    g.add_argument('--urls', help='file with one URL per line')
    g.add_argument('--from-sitemap', action='store_true',
                   help='default: every URL in the live sitemap index')
    pi.add_argument('--limit', type=int, default=600)
    sub.add_parser('summary')
    pa = sub.add_parser('all')
    pa.add_argument('--days', type=int, default=28)
    pa.add_argument('--limit', type=int, default=600)
    args = p.parse_args()
    os.makedirs(OUT, exist_ok=True)

    if args.cmd == 'summary':
        cmd_summary()
        return

    c = Client()
    try:
        if args.cmd == 'sites':
            cmd_sites(c)
            return
        site, _ = pick_site(c)
        if not site:
            print('No Search Console property for %s is visible to %s.' % (SITE_HOST, c.email))
            print('Add that service account email as a user on the property in Search Console.')
            sys.exit(2)
        if args.cmd == 'sitemaps' and args.submit:
            before = c.calls
            n, f = cmd_submit(c, site, args.submit)
            log_session('sitemaps submit ' + args.submit, site, c.calls - before, n, f, 'submit')
        elif args.cmd == 'sitemaps':
            before = c.calls
            n, f = cmd_sitemaps(c, site)
            log_session('sitemaps', site, c.calls - before, n, f)
        elif args.cmd == 'performance':
            before = c.calls
            n, f = cmd_performance(c, site, args.days, args.dimension)
            log_session('searchanalytics/query ' + args.dimension, site, c.calls - before, n, f)
        elif args.cmd == 'inspect':
            before = c.calls
            n, f = cmd_inspect(c, site, args.urls, args.limit)
            log_session('urlInspection/index:inspect', site, c.calls - before, n, f)
        elif args.cmd == 'all':
            print('## Matched property: %s' % site)
            before = c.calls
            n, f = cmd_sitemaps(c, site)
            log_session('sitemaps', site, c.calls - before, n, f)
            for dim in ('page', 'query'):
                before = c.calls
                n, f = cmd_performance(c, site, args.days, dim)
                log_session('searchanalytics/query ' + dim, site, c.calls - before, n, f)
            before = c.calls
            n, f = cmd_inspect(c, site, None, args.limit)
            log_session('urlInspection/index:inspect', site, c.calls - before, n, f)
            cmd_summary()
    except PermissionDenied:
        print('Search Console returned 403 "User does not have sufficient permission".')
        print('Add the service account %s as a user (Restricted or Full) on the property '
              'in Search Console > Settings > Users and permissions, then run again.' % c.email)
        sys.exit(2)
    print('\nAPI calls this session: %d' % c.calls)


if __name__ == '__main__':
    main()
