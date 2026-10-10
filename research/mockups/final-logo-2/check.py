"""Checks for the logo pack 2. Run after build.py:  python check.py [shots folder]
(XAMPP must be serving for 6 and 7.)

1. The masters carry the owner's geometry verbatim (the same compound path as Logo-3/svg/mark.svg), and,
   drawn in black on white, render the same as the owner's file at 512 and 1920 px; the solid mark too.
2. Every SVG parses as XML, has a viewBox and no width or height, no <text>, and is under 6 KB.
3. Every PNG and ICO is at its size; favicon.ico holds 16, 32 and 48; the manifest parses.
4. The contrast figures: the disc on white, the dark disc on #111111.
5. option-1 carries the new lockups and favicons byte for byte.
6. The brand sheet and the option-1 pages answer 200.
7. In a browser: no broken images and no horizontal overflow on the brand sheet and the option-1 home and
   article pages (375 and 1280, light and dark); the header lockup is 236 px wide and the footer 168 px at 1280.
"""
import json
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET

from PIL import Image, ImageChops

import build as B

G = B.G
HERE = B.HERE
MOCK = os.path.dirname(HERE)
BASE = 'http://localhost/user-and-product/research/mockups/'
fails = []


def say(m):
    print(m)


def read(rel):
    return open(B.path_of(rel), encoding='utf-8').read()


# 1
owner = open(G.SOURCE, encoding='utf-8').read()
for k in ('mark', 'mark-dark', 'mark-black', 'mark-white', 'mark-currentcolor', 'lockup-light', 'lockup-dark',
          'lockup-black', 'lockup-white', 'stacked-light', 'stacked-dark', 'stacked-black', 'stacked-white'):
    if B.MARK_D not in read('svg/%s.svg' % k):
        fails.append('%s.svg does not carry the master path' % k)


def flat(svg, n):
    return G.on(G.png(svg, n, n), G.WHITE)


blackened = re.sub(r'fill="#[0-9A-Fa-f]{6}" fill-rule', 'fill="#000000" fill-rule', read('svg/mark.svg'))
solid_bw = read('svg/mark-solid.svg').replace(B.BLUE, '#000000')
for n in (512, 1920):
    for name, svg in (('mark', blackened), ('mark-solid', solid_bw)):
        top = ImageChops.difference(flat(owner, n), flat(svg, n)).convert('L').getextrema()[1]
        if top > 1:
            fails.append('%s differs from the owner file at %d px by %d levels' % (name, n, top))
        say('1. %s vs owner at %d px: %s' % (name, n, 'identical' if top == 0 else 'within %d gray level' % top))

# 2
biggest = (0, '')
svgs = [os.path.join(r, f) for r, _, fs in os.walk(HERE) for f in fs if f.endswith('.svg')]
for p in svgs:
    t = open(p, encoding='utf-8').read()
    rel = os.path.relpath(p, HERE)
    try:
        el = ET.fromstring(t)
    except ET.ParseError as ex:
        fails.append('%s: invalid XML (%s)' % (rel, ex))
        continue
    size = len(t.encode('utf-8'))
    biggest = max(biggest, (size, rel))
    if size >= 6144:
        fails.append('%s: %d bytes' % (rel, size))
    if 'viewBox' not in el.attrib or 'width' in el.attrib or 'height' in el.attrib:
        fails.append('%s: viewBox missing or fixed size' % rel)
    if '<text' in t:
        fails.append('%s: live text' % rel)
say('2. %d SVGs valid, largest %d bytes (%s)' % (len(svgs), biggest[0], biggest[1]))

# 3
want = {}
for s in (64, 128, 256, 512, 1024):
    want['png/mark-light-%d.png' % s] = (s, s)
    want['png/mark-dark-%d.png' % s] = (s, s)
for w in (236, 472, 944):
    want['png/lockup-light-%d.png' % w] = (w, None)
    want['png/lockup-dark-%d.png' % w] = (w, None)
for w in (400, 800):
    want['png/stacked-light-%d.png' % w] = (w, None)
    want['png/stacked-dark-%d.png' % w] = (w, None)
for s in (16, 32, 48, 96, 192, 512):
    want['favicon/favicon-%d.png' % s] = (s, s)
want.update({
    'favicon/apple-touch-icon-180.png': (180, 180), 'favicon/maskable-512.png': (512, 512),
    'social/instagram-avatar-1080.png': (1080, 1080), 'social/instagram-avatar-1080-dark.png': (1080, 1080),
    'social/linkedin-logo-300.png': (300, 300), 'social/linkedin-logo-400.png': (400, 400),
    'social/linkedin-logo-300-dark.png': (300, 300), 'social/linkedin-logo-400-dark.png': (400, 400),
    'social/linkedin-banner-1128x191.png': (1128, 191), 'social/linkedin-banner-1128x191-dark.png': (1128, 191),
    'social/og-1200x630.png': (1200, 630), 'social/og-1200x630-dark.png': (1200, 630),
    'social/x-avatar-400.png': (400, 400), 'social/x-avatar-400-dark.png': (400, 400),
    'social/x-header-1500x500.png': (1500, 500), 'social/x-header-1500x500-dark.png': (1500, 500),
    'png/lockup-black-on-white-944.png': (944, None), 'png/lockup-white-on-black-944.png': (944, None),
    'png/stacked-black-on-white-800.png': (800, None), 'png/stacked-white-on-black-800.png': (800, None),
    'png/mark-black-on-white-1024.png': (1024, 1024), 'png/mark-white-on-black-1024.png': (1024, 1024)})
for rel, (w, h) in want.items():
    p = B.path_of(rel)
    if not os.path.exists(p):
        fails.append('missing %s' % rel)
        continue
    sz = Image.open(p).size
    if sz[0] != w or (h and sz[1] != h):
        fails.append('%s is %s' % (rel, sz))
ico = Image.open(B.path_of('favicon/favicon.ico'))
if not {(16, 16), (32, 32), (48, 48)} <= set(ico.info.get('sizes', set())):
    fails.append('favicon.ico sizes %s' % ico.info.get('sizes'))
json.load(open(B.path_of('favicon/site.webmanifest'), encoding='utf-8'))
fav = read('favicon/favicon.svg')
if 'prefers-color-scheme:dark' not in fav or B.BLUE_D not in fav:
    fails.append('favicon.svg has no dark-mode query')
say('3. %d raster files at their sizes; favicon.ico 16, 32, 48; manifest parses' % len(want))

# 4
rt = B.contrasts()
say('4. disc on white %.2f:1; dark disc on #111111 %.2f:1 (on #0B0B0C %.2f:1)'
    % (rt['blue_white'], rt['blued_near'], rt['blued_site']))
if round(rt['blue_white'], 1) != 5.2:
    fails.append('disc on white is %.2f' % rt['blue_white'])

# 5
pairs = [('svg/lockup-light.svg', 'option-1/assets/logo/lockup-light.svg'),
         ('svg/lockup-dark.svg', 'option-1/assets/logo/lockup-dark.svg'),
         ('favicon/favicon.svg', 'option-1/assets/favicon/favicon.svg'),
         ('favicon/favicon.ico', 'option-1/assets/favicon/favicon.ico'),
         ('favicon/apple-touch-icon-180.png', 'option-1/assets/favicon/apple-touch-icon-180.png')]
for a, b in pairs:
    if open(B.path_of(a), 'rb').read() != open(os.path.join(MOCK, *b.split('/')), 'rb').read():
        fails.append('%s is not the new %s' % (b, a))
say('5. option-1 assets match the pack: %d files' % len(pairs))

# 6
pages = ['final-logo-2/brand-sheet.html', 'option-1/', 'option-1/article.html', 'option-1/sitemap.html',
         'option-1/assets/logo/lockup-light.svg', 'option-1/assets/logo/lockup-dark.svg',
         'option-1/assets/favicon/favicon.svg', 'option-1/assets/favicon/favicon.ico',
         'option-1/assets/favicon/apple-touch-icon-180.png']
bad = 0
for pg in pages:
    try:
        code = urllib.request.urlopen(BASE + pg, timeout=10).status
    except Exception as ex:  # noqa: BLE001
        code = str(ex)
    if code != 200:
        bad += 1
        fails.append('%s answered %s' % (pg, code))
say('6. %d of %d URLs answer 200' % (len(pages) - bad, len(pages)))

# 7
shots = sys.argv[1] if len(sys.argv) > 1 else None
from playwright.sync_api import sync_playwright  # noqa: E402

LOGOS = """() => [...document.querySelectorAll('.logo img')].filter(i => i.offsetParent)
  .map(i => [i.closest('footer') ? 'footer' : 'header', Math.round(i.getBoundingClientRect().width),
             Math.round(i.getBoundingClientRect().height * 10) / 10, i.src.split('/').pop()])"""
with sync_playwright() as pw:
    br = pw.chromium.launch(channel='chrome')
    for url in ('final-logo-2/brand-sheet.html', 'option-1/', 'option-1/article.html'):
        for w in (375, 1280):
            for scheme in ('light', 'dark'):
                pg = br.new_page(viewport={'width': w, 'height': 900}, color_scheme=scheme)
                pg.goto(BASE + url, wait_until='networkidle')
                pg.evaluate("() => document.querySelectorAll('img[loading=lazy]').forEach(i => i.loading = 'eager')")
                pg.wait_for_function('() => [...document.images].every(i => i.complete)')
                broken = pg.evaluate('[...document.images].filter(i => i.naturalWidth === 0).map(i => i.src)')
                over = pg.evaluate('document.documentElement.scrollWidth - innerWidth')
                logos = pg.evaluate(LOGOS)
                if broken:
                    fails.append('%s at %d %s: broken images %s' % (url, w, scheme, broken[:4]))
                if over > 0:
                    fails.append('%s at %d: overflow %d' % (url, w, over))
                if url.startswith('option-1') and w == 1280:
                    for where, lw, lh, src in logos:
                        exp = 236 if where == 'header' else 168
                        if lw != exp:
                            fails.append('%s %s lockup is %d px, expected %d' % (url, where, lw, exp))
                say('7. %s %d %s: broken %d, overflow %d, logos %s' % (url, w, scheme, len(broken), over, logos))
                if shots:
                    os.makedirs(shots, exist_ok=True)
                    name = re.sub(r'[^a-z0-9]+', '-', url).strip('-')
                    pg.screenshot(path=os.path.join(shots, '%s-%d-%s.png' % (name, w, scheme)), full_page=True)
                pg.close()
    br.close()

print('\nFAIL:\n  ' + '\n  '.join(fails) if fails else '\nall checks passed')
sys.exit(1 if fails else 0)
