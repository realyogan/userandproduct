"""Shared geometry, type setting and file helpers for the round-six builder (taken from round five)."""
import io
import os
import subprocess
import sys
import xml.etree.ElementTree as ET

import pathops
import resvg_py
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.svgLib.path import parse_path
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, '..'))
MOCK = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
TOOLS = os.path.join(MOCK, 'tools')
FONTDIR = os.path.join(MOCK, 'fonts')
sys.path.insert(0, TOOLS)
import wordmark as WM  # noqa: E402

FONTS = {
    'frau-sb': 'fraunces/Fraunces72pt-SemiBold.ttf',
    'frau-r': 'fraunces/Fraunces72pt-Regular.ttf',
    'geist-b': 'geist/Geist-Bold.ttf',
    'geist-sb': 'geist/Geist-SemiBold.ttf',
    'inst-b': 'instrument-sans/InstrumentSans-Bold.ttf',
    'inter-b': 'inter/InterDisplay-Bold.ttf',
    'inter-sb': 'inter/InterDisplay-SemiBold.ttf',
    'bric-b': 'bricolage-grotesque/BricolageGrotesque-Bold.ttf',
}
_cache = {}


def font(key):
    if key not in _cache:
        _cache[key] = WM.FontRef(os.path.join(FONTDIR, FONTS[key]))
    return _cache[key]


def caph(key, size=100):
    f = font(key)
    return f.tt['OS/2'].sCapHeight * size / f.upem


# ------------------------------------------------------------------ path helpers
fmt = WM.fmt


def to_path(d):
    p = pathops.Path()
    parse_path(d, p.getPen())
    return p


def from_path(p):
    pen = SVGPathPen(None, ntos=fmt)
    p.draw(pen)
    return pen.getCommands()


def union(*ds):
    out = pathops.Path()
    for d in ds:
        if d:
            out = pathops.op(out, to_path(d), pathops.PathOp.UNION)
    return from_path(out)


def minus(a, *bs):
    p = to_path(a)
    for b in bs:
        if b:
            p = pathops.op(p, to_path(b), pathops.PathOp.DIFFERENCE)
    return from_path(p)


def bounds(d):
    return to_path(d).bounds


def rect(x0, y0, x1, y1):
    return f'M{fmt(x0)} {fmt(y0)}H{fmt(x1)}V{fmt(y1)}H{fmt(x0)}Z'


def circle(cx, cy, r):
    return (f'M{fmt(cx - r)} {fmt(cy)}A{fmt(r)} {fmt(r)} 0 1 0 {fmt(cx + r)} {fmt(cy)}'
            f'A{fmt(r)} {fmt(r)} 0 1 0 {fmt(cx - r)} {fmt(cy)}Z')


def half_left(cx, cy, r):
    return f'M{fmt(cx)} {fmt(cy - r)}A{fmt(r)} {fmt(r)} 0 0 0 {fmt(cx)} {fmt(cy + r)}Z'


def half_right(cx, cy, r):
    return f'M{fmt(cx)} {fmt(cy - r)}A{fmt(r)} {fmt(r)} 0 0 1 {fmt(cx)} {fmt(cy + r)}Z'


def shift(d, dx, dy, s=1.0):
    return from_path(to_path(d).transform(s, 0, 0, s, dx, dy))


# ------------------------------------------------------------------ type setting
def setw(parts, fonts, size=100, x=0.0, y=0.0, tracking=0.0):
    """Set text with wordmark.py's layout, baseline at y. Returns [(d, bounds)] per part."""
    if isinstance(parts, str):
        parts = [parts]
    if isinstance(fonts, str):
        fonts = [fonts] * len(parts)
    refs = [font(k) for k in fonts]
    placed = WM.layout(parts, refs, size, tracking)
    out = []
    for items in placed:
        moved = [(f, g, (m[0], m[1], m[2], m[3], m[4] + x, m[5] + y)) for f, g, m in items]
        out.append(WM.part_path(moved, True))
    return out


def word(text, key, tracking=0.0, size=100):
    """One merged path for the text and its ink box, baseline at 0, ink starting at x = 0."""
    items = setw(text, key, size, 0, 0, tracking)
    d, b = items[0]
    return shift(d, -b[0], 0), (0, b[1], b[2] - b[0], b[3])


def svg(vb, body, label):
    x, y, w, h = vb
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{fmt(x)} {fmt(y)} {fmt(w)} {fmt(h)}" '
            f'role="img" aria-label="{label}"><title>{label}</title>{body}</svg>')


def P(d, fill):
    return f'<path fill="{fill}" d="{d}"/>'


def fitbox(x0, y0, x1, y1, m):
    return (x0 - m, y0 - m, x1 - x0 + 2 * m, y1 - y0 + 2 * m)


INK, PAPER, NEAR = '#141414', '#F3F1EC', '#141414'


def colors(mode, light, dark):
    if mode == 'mono':
        return {k: 'currentColor' for k in light}
    return light if mode == 'light' else dark


def frags_svg(frags, c, dx=0, dy=0, s=1.0):
    return ''.join(P(shift(d, dx, dy, s) if (dx or dy or s != 1) else d, c[role]) for d, role in frags)


def frags_box(frags):
    bs = [bounds(d) for d, _ in frags]
    return (min(b[0] for b in bs), min(b[1] for b in bs), max(b[2] for b in bs), max(b[3] for b in bs))


def mark_svg(frags, c, label='userandproduct mark', vb=(0, 0, 100, 100)):
    return svg(vb, frags_svg(frags, c), label)


def side_lockup(frags, c, wd, wb, role, H, yc, gap, label='userandproduct'):
    """Mark on the left scaled to height H, vertically centred on yc; word to the right."""
    x0, y0, x1, y1 = frags_box(frags)
    s = H / (y1 - y0)
    dx, dy = -x0 * s, yc - H / 2 - y0 * s
    mw = (x1 - x0) * s
    body = frags_svg(frags, c, dx, dy, s) + P(shift(wd, mw + gap, 0), c[role])
    top, bot = min(yc - H / 2, wb[1]), max(yc + H / 2, wb[3])
    return svg(fitbox(0, top, mw + gap + wb[2], bot, 4), body, label)



#----
def render_avatar(svg_text, path, size=400):
    data = bytes(resvg_py.svg_to_bytes(svg_string=svg_text, width=size, height=size))
    img = Image.open(io.BytesIO(data)).convert('RGBA')
    big = Image.new('L', (size * 4, size * 4), 0)
    ImageDraw.Draw(big).ellipse((0, 0, size * 4 - 1, size * 4 - 1), fill=255)
    mask = big.resize((size, size), Image.LANCZOS)
    img.putalpha(mask)
    img.save(path)


# =============================================================== write, validate, render
def write(name, text):
    ET.fromstring(text)  # raises if the SVG is not well formed
    head = text.split('>')[0]
    assert '<text' not in text and ' width=' not in head and ' height=' not in head and 'viewBox' in head
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        f.write(text)


import math

PAPER_CREAM = '#F4EFE3'
WORD_DARK = '#EEE9DF'


# ------------------------------------------------------------------ stroke geometry
def seg(x1, y1, x2, y2, w, cap='round'):
    """A straight stroke of width w as a filled outline (butt or round ends)."""
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy)
    nx, ny = -dy / L * w / 2, dx / L * w / 2
    pts = [(x1 + nx, y1 + ny), (x2 + nx, y2 + ny), (x2 - nx, y2 - ny), (x1 - nx, y1 - ny)]
    d = 'M' + 'L'.join(f'{fmt(x)} {fmt(y)}' for x, y in pts) + 'Z'
    if cap == 'round':
        d = union(d, circle(x1, y1, w / 2), circle(x2, y2, w / 2))
    return d


def clip(d, x0, y0, x1, y1):
    return from_path(pathops.op(to_path(d), to_path(rect(x0, y0, x1, y1)), pathops.PathOp.INTERSECTION))


def stadium(x0, y0, x1, y1):
    r = (y1 - y0) / 2
    return union(rect(x0 + r, y0, x1 - r, y1), circle(x0 + r, y0 + r, r), circle(x1 - r, y0 + r, r))


def toward(ax, ay, bx, by, dist):
    """The point at distance dist from b, back toward a."""
    L = math.hypot(bx - ax, by - ay)
    return bx - (bx - ax) / L * dist, by - (by - ay) / L * dist


def one(d, role='m'):
    return [(d, role)]


def sq_vb(d, m=3):
    x0, y0, x1, y1 = bounds(d)
    s = max(x1 - x0, y1 - y0) + 2 * m
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    return (cx - s / 2, cy - s / 2, s, s)


def make(mode, mark_d, fav_d, word_key, tracking, H, gap, L, D, word_role='ink', yc_f=0.5):
    """Lockup, mark and favicon for a single-shape mark. L and D map roles to colors."""
    c = colors(mode, L, D)
    frags = one(mark_d)
    cap = caph(word_key)
    wd, wb = word('userandproduct', word_key, tracking)
    lock = side_lockup(frags, c, wd, wb, word_role, cap * H, -cap * yc_f, cap * gap)
    mark = mark_svg(frags, c, vb=sq_vb(mark_d))
    fav = mark_svg(one(fav_d), L, 'userandproduct', vb=sq_vb(fav_d, 1.5))
    return lock, mark, fav


