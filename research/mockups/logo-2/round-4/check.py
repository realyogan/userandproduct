"""Checks for round 4. Run after build.py:  python check.py

1. Every SVG parses as XML, is under 6 KB, has a viewBox, and uses paths only (no text, image,
   filter, gradient, mask, clipPath, stroke or opacity).
2. No feature thinner than 8 units at 512: each color region of every color master, and each
   monochrome master, is rendered at 512, opened with a 9 x 9 square (erode then dilate), and the
   pixels lost are counted; a region that loses a patch is reported with its size.
3. Every mark has its 32 px favicons (color on white and near-black, monochrome on white and black)
   and its 16 px tab favicons.
4. No two marks share a core shape: the figure of each mark (the monochrome silhouette; for a mark
   in a container, what is knocked out of the container) is compared at 64 px (intersection over union).
"""
import io
import os
import re
import sys
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import resvg_py
from PIL import Image, ImageChops, ImageFilter
import marks as M
from info import INFO

SVG = os.path.join(HERE, 'svg')
PNG = os.path.join(HERE, 'png')
BANNED = re.compile(r'<(text|image|filter|linearGradient|radialGradient|mask|clipPath|use|style)\b|stroke|opacity')
N = len(M.MARKS)
fails = []


def render(svg, size):
    return Image.open(io.BytesIO(bytes(resvg_py.svg_to_bytes(svg_string=svg, width=size, height=size))))


# 1. files
names = sorted(n for n in os.listdir(SVG) if n.endswith('.svg'))
biggest = (0, '')
for n in names:
    t = open(os.path.join(SVG, n), encoding='utf-8').read()
    try:
        ET.fromstring(t)
    except ET.ParseError as ex:
        fails.append('%s: not valid XML (%s)' % (n, ex))
    size = len(t.encode('utf-8'))
    biggest = max(biggest, (size, n))
    if size >= 6144:
        fails.append('%s: %d bytes, over 6 KB' % (n, size))
    if 'viewBox' not in t:
        fails.append('%s: no viewBox' % n)
    if BANNED.search(t):
        fails.append('%s: uses %s' % (n, BANNED.search(t).group(0)))
print('1. %d SVGs parsed; largest %d bytes (%s)' % (len(names), biggest[0], biggest[1]))

# 2. thinnest features
thin = []
for n in names:
    if not re.match(r'r4-\d\d-(mark|mark-dark|mono-black)\.svg$', n):
        continue
    t = open(os.path.join(SVG, n), encoding='utf-8').read()
    for col, d in re.findall(r'<path fill="(#[0-9A-Fa-f]{6})" d="([^"]+)"', t):
        one = re.sub(r'<path[^>]*/>\n', '', t).replace('</svg>', '<path fill="#000" d="%s"/></svg>' % d)
        m = render(one, 512).split()[3].point(lambda v: 255 if v > 127 else 0)
        opened = m.filter(ImageFilter.MinFilter(9)).filter(ImageFilter.MaxFilter(9))
        lost = ImageChops.subtract(m, opened).filter(ImageFilter.MinFilter(3))
        px = sum(1 for v in lost.getdata() if v)
        if px > 40:
            thin.append('%s %s: %d px narrower than 8 units' % (n, col, px))
print('2. thin-feature scan: %s' % ('none under 8 units' if not thin else '; '.join(thin)))
if thin:
    fails.append('thin features: ' + '; '.join(thin))

# 3. favicons
want = [('32-light', 32), ('32-dark', 32), ('32-mono-light', 32), ('32-mono-dark', 32),
        ('16-light', 16), ('16-dark', 16), ('16-tab-light', 16), ('16-tab-dark', 16)]
for i in range(1, N + 1):
    for suf, sz in want:
        p = os.path.join(PNG, 'r4-%02d-%s.png' % (i, suf))
        if not os.path.exists(p) or Image.open(p).size != (sz, sz):
            fails.append('missing or wrong-size favicon %s' % p)
print('3. %d favicons checked' % (N * len(want)))

# 4. core shapes
fig = {}
for i, fn in enumerate(M.MARKS, 1):
    m = fn()
    t = open(os.path.join(SVG, 'r4-%02d-mono-black.svg' % i), encoding='utf-8').read()
    a = [1 if v > 127 else 0 for v in render(t, 64).split()[3].getdata()]
    if m['kind'] in ('circle', 'squircle'):
        box = M.disc() if m['kind'] == 'circle' else M.squircle()
        from geo import d_of
        ct = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path d="%s"/></svg>' % d_of(box)
        c = [1 if v > 127 else 0 for v in render(ct, 64).split()[3].getdata()]
        a = [1 if (x and not y) else 0 for x, y in zip(c, a)]
    fig[i] = a
pairs = []
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        inter = sum(1 for x, y in zip(fig[i], fig[j]) if x and y)
        uni = sum(1 for x, y in zip(fig[i], fig[j]) if x or y)
        pairs.append((inter / uni if uni else 0, i, j))
pairs.sort(reverse=True)
print('4. most similar figures across families (intersection over union):')
for v, i, j in [p for p in pairs if INFO[p[1] - 1]['group'] != INFO[p[2] - 1]['group']][:6]:
    print('   R4-%02d / R4-%02d: %.2f' % (i, j, v))
print('   (variants inside one family are meant to be close; the rule applies across families)')
for v, i, j in pairs:
    if v > 0.80 and INFO[i - 1]['group'] == INFO[j - 1]['group']:
        continue
    if v > 0.80:
        fails.append('R4-%02d and R4-%02d share a core shape (%.2f)' % (i, j, v))

print('\n'.join(['FAIL ' + x for x in fails]) if fails else 'all checks passed')
sys.exit(1 if fails else 0)
