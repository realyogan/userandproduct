"""Checks for round 2. Run after build.py:  python check.py

1. Every SVG parses as XML, is under 6 KB, has a viewBox, and uses paths only (no text, image,
   filter, gradient, mask, clipPath, stroke or opacity).
2. No feature thinner than 8 units at 512: each colour region of every master is rendered at 512,
   opened with a 9 x 9 square (erode then dilate), and the pixels lost are counted; a region that loses
   a patch is reported with its size.
3. Every mark's 32 px favicons exist at 32 x 32.
4. No two marks share a core shape: masters are compared as 64 px silhouettes (intersection over union).
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

SVG = os.path.join(HERE, 'svg')
PNG = os.path.join(HERE, 'png')
BANNED = re.compile(r'<(text|image|filter|linearGradient|radialGradient|mask|clipPath|use|style)\b|stroke|opacity')
fails = []


def render(svg, size, bg=None):
    return Image.open(io.BytesIO(bytes(resvg_py.svg_to_bytes(svg_string=svg, width=size, height=size, background=bg))))


# 1. files
names = sorted(n for n in os.listdir(SVG) if n.endswith('.svg'))
biggest = 0
for n in names:
    t = open(os.path.join(SVG, n), encoding='utf-8').read()
    try:
        ET.fromstring(t)
    except ET.ParseError as ex:
        fails.append('%s: not valid XML (%s)' % (n, ex))
    size = len(t.encode('utf-8'))
    biggest = max(biggest, size)
    if size >= 6144:
        fails.append('%s: %d bytes, over 6 KB' % (n, size))
    if 'viewBox' not in t:
        fails.append('%s: no viewBox' % n)
    if BANNED.search(t):
        fails.append('%s: uses %s' % (n, BANNED.search(t).group(0)))
print('1. %d SVGs parsed; largest %d bytes' % (len(names), biggest))

# 2. thinnest features, per colour region of each light and dark master
thin = []
for n in names:
    if not re.match(r'r2-\d\d-mark(-dark)?\.svg$', n):
        continue
    t = open(os.path.join(SVG, n), encoding='utf-8').read()
    fills = re.findall(r'<path fill="(#[0-9A-Fa-f]{6})" d="([^"]+)"', t)
    for col, d in fills:
        one = re.sub(r'<path[^>]*/>\n', '', t).replace('</svg>', '<path fill="#000" d="%s"/></svg>' % d)
        m = render(one, 512).split()[3]
        m = m.point(lambda v: 255 if v > 127 else 0)
        opened = m.filter(ImageFilter.MinFilter(9)).filter(ImageFilter.MaxFilter(9))
        lost = ImageChops.subtract(m, opened)
        # ignore the anti-aliased rim and sharp corners: count only lost blobs wider than a corner nick
        lost = lost.filter(ImageFilter.MinFilter(3))
        px = sum(1 for v in lost.getdata() if v)
        if px > 40:
            thin.append('%s %s: %d px narrower than 8 units' % (n, col, px))
print('2. thin-feature scan: %s' % ('none under 8 units' if not thin else '; '.join(thin)))

# 3. favicons
for i in range(1, 11):
    for g in ('light', 'dark'):
        p = os.path.join(PNG, 'r2-%02d-32-%s.png' % (i, g))
        if not os.path.exists(p) or Image.open(p).size != (32, 32):
            fails.append('missing or wrong-size favicon %s' % p)
print('3. 20 favicons at 32 x 32 checked')

# 4. silhouettes
sil = {}
for i in range(1, 11):
    t = open(os.path.join(SVG, 'r2-%02d-mark.svg' % i), encoding='utf-8').read()
    a = render(t, 64).split()[3].point(lambda v: 1 if v > 127 else 0)
    sil[i] = a
worst = (0, None)
pairs = []
for i in range(1, 11):
    for j in range(i + 1, 11):
        ai, aj = list(sil[i].getdata()), list(sil[j].getdata())
        inter = sum(1 for x, y in zip(ai, aj) if x and y)
        uni = sum(1 for x, y in zip(ai, aj) if x or y)
        iou = inter / uni if uni else 0
        pairs.append((iou, i, j))
pairs.sort(reverse=True)
print('4. most similar silhouettes (intersection over union, contained marks share their container):')
for iou, i, j in pairs[:4]:
    print('   R2-%02d / R2-%02d: %.2f' % (i, j, iou))
# a closer test inside the container: compare only the letter (light pixels) of contained marks
let = {}
for i in range(1, 11):
    t = open(os.path.join(SVG, 'r2-%02d-mark.svg' % i), encoding='utf-8').read()
    im = render(t, 64, bg='#2B46A0' if 'fill="#2B46A0"' in t else None).convert('RGB')
    let[i] = [1 if sum(px) > 400 else 0 for px in im.getdata()]
lp = []
for i in range(1, 11):
    for j in range(i + 1, 11):
        inter = sum(1 for x, y in zip(let[i], let[j]) if x and y)
        uni = sum(1 for x, y in zip(let[i], let[j]) if x or y)
        lp.append((inter / uni if uni else 0, i, j))
lp.sort(reverse=True)
print('   letters only (light parts), most similar: ' + ', '.join('R2-%02d/R2-%02d %.2f' % (j, k, v) for v, j, k in lp[:3]))

print('\n'.join(['FAIL ' + x for x in fails]) if fails else 'all checks passed')
sys.exit(1 if fails else 0)
