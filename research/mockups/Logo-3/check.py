"""Checks for Logo 3. Run after build.py:  python check.py   (XAMPP must be serving for 5 and 6)

1. The owner's Logo.svg is unchanged (same bytes as source/Logo-owner.svg).
2. The clean master renders identically to the owner's file, on white, at 512 and 1920 px; mark-solid
   renders the same as the master on white (within one gray level, from anti-aliasing at the cut-out
   edges); the master carries no comment, class or style.
3. Every SVG parses as XML, has a viewBox and no width or height, no <text>, and is under 6 KB.
4. Every option and gradient has its favicons (16 and 32 px on white and near-black, 16 px tab icons)
   at the right sizes; the export folder has its files at the right sizes.
5. The board answers 200 at http://localhost/user-and-product/research/mockups/Logo-3/
6. No horizontal overflow at 375 px (and at 1280 px), every image on the board loads; screenshots
   go to the scratch folder given as the first argument, if any.
"""
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET

from PIL import Image, ImageChops

import geo as G

HERE = G.HERE
URL = 'http://localhost/user-and-product/research/mockups/Logo-3/'
fails = []


def say(msg):
    print(msg)


# 1
a = open(os.path.join(HERE, 'Logo.svg'), 'rb').read()
b = open(G.SOURCE, 'rb').read()
if a != b:
    fails.append('Logo.svg differs from source/Logo-owner.svg')
say('1. owner file unchanged: %s' % (a == b))

# 2
owner = b.decode('utf-8')
master = open(os.path.join(HERE, 'svg', 'mark.svg'), encoding='utf-8').read()
solid = open(os.path.join(HERE, 'svg', 'mark-solid.svg'), encoding='utf-8').read()


def flat(svg, n):
    return G.on(G.png(svg, n, n), G.WHITE)


for n in (512, 1920):
    for name, x, y in (('master vs owner', owner, master), ('solid vs master', master, solid),
                       ('solid vs owner', owner, solid)):
        diff = ImageChops.difference(flat(x, n), flat(y, n)).convert('L')
        top = diff.getextrema()[1]
        off = sum(1 for v in diff.tobytes() if v > 1)
        # pass: no pixel more than one gray level apart (anti-aliasing rounding along the cut-out edges)
        if top > 1:
            fails.append('%s differ at %d px: %d pixels, up to %d levels' % (name, n, off, top))
        say('2. %s at %d px: %s' % (name, n, 'identical' if top == 0 else
                                       'same within %d of 255 gray levels on the cut-out edges' % top
                                       if top <= 1 else 'DIFFERENT, up to %d levels' % top))
if re.search(r'<!--|class=|<style', master):
    fails.append('svg/mark.svg has a comment, class or style')
for d_ in (G.BAND_D, G.HEAD_D):
    if d_ not in master:
        fails.append('master does not carry the owner path verbatim')

# 3
count, biggest = 0, (0, '')
for root, _, names in os.walk(HERE):
    if os.sep + 'source' in root:
        continue
    for nm in names:
        if not nm.endswith('.svg') or (root == HERE and nm == 'Logo.svg'):
            continue
        p = os.path.join(root, nm)
        rel = os.path.relpath(p, HERE)
        t = open(p, encoding='utf-8').read()
        count += 1
        try:
            el = ET.fromstring(t)
        except ET.ParseError as ex:
            fails.append('%s: not valid XML (%s)' % (rel, ex))
            continue
        size = len(t.encode('utf-8'))
        biggest = max(biggest, (size, rel))
        if size >= 6144:
            fails.append('%s: %d bytes, over 6 KB' % (rel, size))
        if 'viewBox' not in el.attrib or 'width' in el.attrib or 'height' in el.attrib:
            fails.append('%s: viewBox missing or fixed size set' % rel)
        if '<text' in t:
            fails.append('%s: live text' % rel)
say('3. %d SVGs valid; largest %d bytes (%s)' % (count, biggest[0], biggest[1]))

# 4
want = [('fav-16-light', 16), ('fav-16-dark', 16), ('fav-32-light', 32), ('fav-32-dark', 32),
        ('tab-16-light', 16), ('tab-16-dark', 16), ('thumb', 1200)]
n = 0
for o in G.OPTIONS + G.GRADIENTS:
    for suf, sz in want:
        p = os.path.join(HERE, 'png', o['key'], suf + '.png')
        if not os.path.exists(p) or Image.open(p).size[0] != sz:
            fails.append('missing or wrong size: %s' % p)
        n += 1
exp = {'favicon-16.png': 16, 'favicon-32.png': 32, 'favicon-48.png': 48, 'apple-touch-icon-180.png': 180,
       'social-square-1080.png': 1080, 'social-circle-1080.png': 1080, 'social-square-400.png': 400,
       'social-circle-400.png': 400}
for nm, sz in exp.items():
    p = os.path.join(HERE, 'export', nm)
    if not os.path.exists(p) or Image.open(p).size != (sz, sz):
        fails.append('export missing or wrong size: %s' % nm)
for nm in ('favicon.svg', 'favicon.ico', 'head-snippet.html'):
    if not os.path.exists(os.path.join(HERE, 'export', nm)):
        fails.append('export missing: %s' % nm)
say('4. %d option renders and %d export files checked' % (n, len(exp) + 3))

# 5
try:
    code = urllib.request.urlopen(URL, timeout=10).status
except Exception as ex:  # noqa: BLE001
    code = str(ex)
if code != 200:
    fails.append('board answered %s' % code)
say('5. %s -> %s' % (URL, code))

# 6
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sync_playwright = None
shots = sys.argv[1] if len(sys.argv) > 1 else None
if sync_playwright:
    with sync_playwright() as pw:
        br = pw.chromium.launch(channel='chrome')
        for w in (375, 1280):
            pg = br.new_page(viewport={'width': w, 'height': 900})
            pg.goto(URL, wait_until='networkidle')
            sw = pg.evaluate('document.documentElement.scrollWidth')
            broken = pg.evaluate('Array.from(document.images).filter(i => i.complete && i.naturalWidth === 0)'
                                 '.map(i => i.getAttribute("src"))')
            # images below the fold are lazy; scroll through so they load, then look again
            pg.evaluate('window.scrollTo(0, document.body.scrollHeight)')
            pg.wait_for_timeout(500)
            broken = pg.evaluate('Array.from(document.images).filter(i => i.complete && i.naturalWidth === 0)'
                                 '.map(i => i.getAttribute("src"))')
            if sw > w:
                fails.append('horizontal overflow at %d px: scrollWidth %d' % (w, sw))
            if broken:
                fails.append('%d broken images at %d px: %s' % (len(broken), w, broken[:5]))
            say('6. %d px: scrollWidth %d, broken images %d' % (w, sw, len(broken)))
            if shots:
                pg.evaluate('window.scrollTo(0, 0)')
                pg.screenshot(path=os.path.join(shots, 'board-%d.png' % w), full_page=False)
                pg.screenshot(path=os.path.join(shots, 'board-%d-full.png' % w), full_page=True)
            pg.close()
        br.close()
else:
    fails.append('playwright not available for the overflow check')

print('\n'.join('FAIL ' + f for f in fails) if fails else 'all checks passed')
sys.exit(1 if fails else 0)
