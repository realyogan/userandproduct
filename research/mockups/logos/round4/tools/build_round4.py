"""Build the round-four logo concepts (P1 to P10) and the review board.

Brief: an abstract MARK plus the NAME, feeling like an institution or a publication, not software.

Run from this folder:
    python build_round4.py            # all SVGs, PNG renders and index.html
    python build_round4.py P3 P7      # only those concepts (index is rebuilt too)

Wordmarks are set from the OFL fonts in research/mockups/fonts/ with the shaping and outline code
of research/mockups/tools/wordmark.py (HarfBuzz kerning, fontTools outlines, overlaps merged with
skia-pathops). No <text> anywhere. Files go to the parent folder, per concept p<N>:
  p<N>-lockup.svg, -lockup-dark.svg, -lockup-mono.svg
  p<N>-mark.svg,   -mark-dark.svg,   -mark-mono.svg
  p<N>-favicon.svg with p<N>-favicon-16.png and -32.png (render.py)
  p<N>-avatar.svg with p<N>-avatar-400.png (circle crop, transparent corners)
"""
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
sys.path.insert(0, HERE)
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


CONCEPTS = {}


def concept(key, **meta):
    def wrap(fn):
        CONCEPTS[key] = dict(meta, build=fn)
        return fn
    return wrap


# =============================================================== P1 the vermilion block
P1L = {'block': '#C21E1A', 'ink': INK}
P1D = {'block': '#D7372F', 'ink': PAPER}


def p1_block(fav=False):
    """A red square; one white rule cut at the nameplate's baseline, running out of the right edge."""
    if fav:
        return [(minus(rect(0, 0, 100, 100), rect(16, 70, 101, 86)), 'block')]
    return [(minus(rect(0, 0, 100, 100), rect(14, 81, 101, 88.5)), 'block')]


@concept('P1', name='The vermilion block', tradition='Newspaper masthead',
         direction='Masthead: a solid red block beside a tracked serif nameplate',
         palette='Press Red, Ink and White', swatch=['#C21E1A', '#141414', '#FFFFFF'], accent='#C21E1A',
         device='Red square with one white baseline rule', typeface='Fraunces SemiBold capitals, tracked',
         hh=30, avatar_bg='#FFFFFF')
def p1(mode):
    c = colors(mode, P1L, P1D)
    cap = caph('frau-sb')
    wd, wb = word('USERANDPRODUCT', 'frau-sb', 70)
    S = cap * 1.42
    # block placed so its rule (y 81 of 100) lies just under the nameplate baseline
    s = S / 100
    top = -81 * s + 1.0
    gap = cap * 0.42
    body = frags_svg(p1_block(), c, 0, top, s) + P(shift(wd, S + gap, 0), c['ink'])
    lock = svg(fitbox(0, top, S + gap + wb[2], top + S, 4), body, 'userandproduct')
    return lock, mark_svg(p1_block(), c), mark_svg(p1_block(True), P1L, 'userandproduct')


# =============================================================== P2 the salmon band
P2L = {'band': '#F2C9A8', 'ink': '#121212'}
P2D = {'band': '#F2C9A8', 'ink': '#121212'}


def p2_parts(width, cap):
    """The whole nameplate is a salmon band with a black rule inset along its top."""
    px, m, t, g, pb = cap * 0.62, cap * 0.2, cap * 0.16, cap * 0.42, cap * 0.5
    y0 = -cap - g - t - m
    band = rect(-px, y0, width + px, pb)
    rule = rect(-px + m, y0 + m, width + px - m, y0 + m + t)
    return band, rule, (-px, y0, width + px, pb)


@concept('P2', name='The salmon band', tradition='Newspaper masthead',
         direction='Masthead: the nameplate printed on a band of salmon newsprint under a black rule',
         palette='Salmon Paper and Black', swatch=['#F2C9A8', '#121212', '#FFFFFF'], accent='#121212',
         device='Salmon band with an inset black rule', typeface='Fraunces Regular capitals, tracked',
         hh=40, avatar_bg='#F2C9A8')
def p2(mode):
    c = colors(mode, P2L, P2D)
    cap = caph('frau-r')
    wd, wb = word('USERANDPRODUCT', 'frau-r', 120)
    band, rule, bx = p2_parts(wb[2], cap)
    if mode == 'mono':
        # in one color the rule sits in a cut of its own, so band, rule and letters stay distinct
        hole = rect(bounds(rule)[0] - cap * 0.07, bounds(rule)[1] - cap * 0.07,
                    bounds(rule)[2] + cap * 0.07, bounds(rule)[3] + cap * 0.07)
        body = P(minus(band, hole, wd), c['band']) + P(rule, c['band'])
    else:
        body = P(band, c['band']) + P(rule, c['ink']) + P(wd, c['ink'])
    lock = svg(fitbox(bx[0], bx[1], bx[2], bx[3], 3), body, 'userandproduct')
    # mark and favicon: a square cut from the band, rule across the top
    mk_band = rect(0, 0, 100, 100)
    mk_rule = rect(12, 14, 88, 30)
    if mode == 'mono':
        mfr = P(minus(mk_band, rect(8, 10, 92, 34)), c['band']) + P(mk_rule, c['band'])
    else:
        mfr = P(mk_band, c['band']) + P(mk_rule, c['ink'])
    mark = svg((0, 0, 100, 100), mfr, 'userandproduct mark')
    fav = svg((0, 0, 100, 100), P(mk_band, P2L['band']) + P(rect(0, 12, 100, 36), P2L['ink']),
              'userandproduct')
    return lock, mark, fav


# =============================================================== P3 the serif monogram block
P3L = {'box': '#14284B', 'ink': INK}
P3D = {'box': '#3F64B5', 'ink': PAPER}


def p3_box():
    up, b = word('up', 'frau-sb', -20, 100)
    w, h = b[2], b[3] - b[1]
    S = 100
    s = 74 / w  # letters fill 74 percent of the box width
    dx = (S - w * s) / 2
    dy = (S - h * s) / 2 - b[1] * s
    letters = shift(up, dx, dy, s)
    return [(minus(rect(0, 0, S, S), letters), 'box')], letters


@concept('P3', name='The serif monogram', tradition='Monogram in a block (the HBR move)',
         direction='Monogram: a heavy serif "up" reversed out of a deep navy square, name small and wide',
         palette='Deep Navy and White', swatch=['#14284B', '#141414', '#FFFFFF'], accent='#14284B',
         device='Navy square with "up" cut out', typeface='Fraunces SemiBold (monogram and name)',
         hh=40, avatar_bg='#14284B')
def p3(mode):
    c = colors(mode, P3L, P3D)
    frags, _ = p3_box()
    cap = caph('frau-sb')
    wd, wb = word('USERANDPRODUCT', 'frau-sb', 230)
    H = cap / 0.27  # box is 3.7 cap heights tall, the name sits on its middle
    lock = side_lockup(frags, c, wd, wb, 'ink', H, -cap / 2, H * 0.3)
    return lock, mark_svg(frags, c), mark_svg(frags, P3L, 'userandproduct')


# =============================================================== P4 the grotesque monogram disc
P4L = {'disc': '#111111', 'ink': '#111111'}
P4D = {'disc': '#F3F1EC', 'ink': '#F3F1EC'}


def p4_disc():
    up, b = word('u&p', 'geist-b', -30, 100)
    w, h = b[2], b[3] - b[1]
    s = 60 / w
    dx = (100 - w * s) / 2
    # centre on the x-height band so the descender hangs, as in a set line
    xh = font('geist-b').tt['OS/2'].sxHeight * 100 / font('geist-b').upem
    dy = 50 + (xh * s) / 2 - 1
    letters = shift(up, dx, dy, s)
    return [(minus(circle(50, 50, 50), letters), 'disc')]


@concept('P4', name='The grotesque monogram', tradition='Monogram in a block (the HBR move)',
         direction='Monogram: "u&p" in a heavy grotesque cut out of a black disc, name small and wide',
         palette='Black and White', swatch=['#111111', '#FFFFFF', '#F3F1EC'], accent='#111111',
         device='Black disc with "u&p" cut out', typeface='Geist Bold monogram, Geist SemiBold name',
         hh=40, avatar_bg='#111111')
def p4(mode):
    c = colors(mode, P4L, P4D)
    frags = p4_disc()
    cap = caph('geist-sb')
    wd, wb = word('USERANDPRODUCT', 'geist-sb', 240)
    H = cap / 0.27
    lock = side_lockup(frags, c, wd, wb, 'ink', H, -cap / 2, H * 0.3)
    return lock, mark_svg(frags, c), mark_svg(frags, P4L, 'userandproduct')


# =============================================================== P5 square and disc
P5L = {'sq': '#111111', 'disc': '#1F3FBF', 'ink': '#111111'}
P5D = {'sq': '#F3F1EC', 'disc': '#7C95FF', 'ink': '#F3F1EC'}


def p5_parts(fav=False):
    g = 8 if fav else 10
    side = (100 - g) / 2
    y0 = (100 - side) / 2
    return [(rect(0, y0, side, y0 + side), 'sq'), (circle(100 - side / 2, 50, side / 2), 'disc')]


@concept('P5', name='Square and disc', tradition='Abstract symbol (the Mastercard and Medium move)',
         direction='Symbol: a black square and a blue disc of one height, side by side, not touching',
         palette='Ink, Signal Blue and White', swatch=['#111111', '#1F3FBF', '#FFFFFF'], accent='#1F3FBF',
         device='Square plus disc', typeface='Geist Bold', hh=30, avatar_bg='#FFFFFF')
def p5(mode):
    c = colors(mode, P5L, P5D)
    frags = p5_parts()
    cap = caph('geist-b')
    wd, wb = word('userandproduct', 'geist-b', -20)
    lock = side_lockup(frags, c, wd, wb, 'ink', cap * 1.0, -cap / 2, cap * 0.5)
    vb = (-2, 24, 104, 52)
    return (lock, mark_svg(frags, c, vb=vb),
            mark_svg(p5_parts(True), P5L, 'userandproduct', vb=(-1, 22, 102, 56)))


# =============================================================== P6 the weighted ring
P6L = {'ring': '#1D4636', 'ink': '#1D4636'}
P6D = {'ring': '#9CC9B0', 'ink': '#EEE8DA'}


def p6_ring(fav=False):
    if fav:
        return [(minus(circle(50, 50, 50), circle(50, 37, 22)), 'ring')]
    return [(minus(circle(50, 50, 50), circle(50, 39, 27)), 'ring')]


@concept('P6', name='The weighted ring', tradition='Abstract symbol (the Mastercard and Medium move)',
         direction='Symbol: a ring whose opening sits high, so the weight settles at the bottom',
         palette='Deep Green on Cream', swatch=['#1D4636', '#F4EFE3', '#FFFFFF'], accent='#1D4636',
         device='Disc with an off-center opening', typeface='Instrument Sans Bold', hh=30,
         avatar_bg='#F4EFE3', paper='#F4EFE3')
def p6(mode):
    c = colors(mode, P6L, P6D)
    frags = p6_ring()
    cap = caph('inst-b')
    wd, wb = word('userandproduct', 'inst-b', -10)
    lock = side_lockup(frags, c, wd, wb, 'ink', cap * 1.36, -cap / 2, cap * 0.42)
    return lock, mark_svg(frags, c), mark_svg(p6_ring(True), P6L, 'userandproduct')


# =============================================================== P7 the shifted halves
P7L = {'a': '#1B2B4D', 'b': '#7A1F2B', 'ink': '#1B2B4D'}
P7D = {'a': '#93A9DB', 'b': '#E58C92', 'ink': '#F1EDE6'}


def p7_parts(fav=False):
    r, off, gap = (44, 6, 3) if fav else (40, 8, 2.5)
    return [(half_left(50 - gap / 2, 50 - off, r), 'a'), (half_right(50 + gap / 2, 50 + off, r), 'b')]


@concept('P7', name='The shifted halves', tradition='Abstract symbol, two-tone (the Mastercard move)',
         direction='Symbol: one disc cut in two, the navy half lifted, the oxblood half lowered',
         palette='Navy and Oxblood', swatch=['#1B2B4D', '#7A1F2B', '#FFFFFF'], accent='#7A1F2B',
         device='Two half discs, offset', typeface='Inter Display SemiBold', hh=30, avatar_bg='#FFFFFF')
def p7(mode):
    c = colors(mode, P7L, P7D)
    frags = p7_parts()
    cap = caph('inter-sb')
    wd, wb = word('userandproduct', 'inter-sb', -15)
    lock = side_lockup(frags, c, wd, wb, 'ink', cap * 1.45, -cap / 2, cap * 0.42)
    return lock, mark_svg(frags, c), mark_svg(p7_parts(True), P7L, 'userandproduct')


# =============================================================== P8 the slotted disc
P8L = {'disc': '#0B0B0C', 'ink': '#0B0B0C'}
P8D = {'disc': '#F3F1EC', 'ink': '#F3F1EC'}


def p8_disc(fav=False):
    """A disc cut once by a straight vertical gap right of center; the narrow segment is kept."""
    t = 4.5 if fav else 3.0          # half the gap width
    dist = 26 if fav else 25         # distance of the cut from the center
    # a band perpendicular to the direction (ux, uy): a vertical chord on the right
    import math
    ux, uy = 1.0, 0.0
    vx, vy = -uy, ux
    def band(a, b):
        return ('M' + ' L'.join(f'{fmt(50 + ux * a + vx * l)} {fmt(50 + uy * a + vy * l)}'
                                for l in (-80, 80)) +
                ' L' + ' L'.join(f'{fmt(50 + ux * b + vx * l)} {fmt(50 + uy * b + vy * l)}'
                                 for l in (80, -80)) + 'Z')
    return [(minus(circle(50, 50, 50), band(dist - t, dist + t)), 'disc')]


@concept('P8', name='The sliced disc', tradition='Negative-space mark (the Tiger Data move)',
         direction='Negative space: a black disc sliced once, upright, right of center, both pieces kept',
         palette='Black and White', swatch=['#0B0B0C', '#FFFFFF', '#F3F1EC'], accent='#0B0B0C',
         device='Disc with one upright cut', typeface='Inter Display Bold', hh=30, avatar_bg='#FFFFFF')
def p8(mode):
    c = colors(mode, P8L, P8D)
    frags = p8_disc()
    cap = caph('inter-b')
    wd, wb = word('userandproduct', 'inter-b', -25)
    lock = side_lockup(frags, c, wd, wb, 'ink', cap * 1.4, -cap / 2, cap * 0.38)
    return lock, mark_svg(frags, c), mark_svg(p8_disc(True), P8L, 'userandproduct')


# =============================================================== P9 the quarter cut
P9L = {'sq': '#0E4A57', 'ink': '#0E4A57'}
P9D = {'sq': '#7FC3CF', 'ink': '#EEF0EC'}


def p9_square():
    return [(minus(rect(0, 0, 100, 100), circle(0, 0, 50)), 'sq')]


@concept('P9', name='The quarter cut', tradition='Negative-space mark (the Tiger Data move)',
         direction='Negative space: a deep teal square with a quarter disc taken from its top-left corner',
         palette='Deep Teal and White', swatch=['#0E4A57', '#FFFFFF', '#EEF0EC'], accent='#0E4A57',
         device='Square minus a quarter disc', typeface='Bricolage Grotesque Bold', hh=30,
         avatar_bg='#FFFFFF')
def p9(mode):
    c = colors(mode, P9L, P9D)
    frags = p9_square()
    cap = caph('bric-b')
    wd, wb = word('userandproduct', 'bric-b', -15)
    lock = side_lockup(frags, c, wd, wb, 'ink', cap * 1.32, -cap / 2, cap * 0.45)
    return lock, mark_svg(frags, c), mark_svg(frags, P9L, 'userandproduct')


# =============================================================== P10 the ensign
P10L = {'a': '#14284B', 'b': '#B08A3E', 'ink': '#14284B'}
P10D = {'a': '#E9E4D8', 'b': '#D9B266', 'ink': '#E9E4D8'}


def p10_bars(fav=False):
    if fav:
        return [(rect(0, 8, 100, 54), 'a'), (rect(36, 64, 100, 92), 'b')]
    return [(rect(0, 18, 100, 52), 'a'), (rect(40, 60, 100, 82), 'b')]


@concept('P10', name='The ensign', tradition='Own: an institution\'s flag reduced to two bars',
         direction='Own: a broad navy bar over a shorter gold bar, set flush right, like a college ensign',
         palette='Navy and Old Gold', swatch=['#14284B', '#B08A3E', '#FFFFFF'], accent='#B08A3E',
         device='Two bars, flush right', typeface='Fraunces SemiBold', hh=30, avatar_bg='#FFFFFF')
def p10(mode):
    c = colors(mode, P10L, P10D)
    frags = p10_bars()
    cap = caph('frau-sb')
    wd, wb = word('userandproduct', 'frau-sb', 0)
    lock = side_lockup(frags, c, wd, wb, 'ink', cap * 0.98, -cap * 0.49, cap * 0.45)
    return (lock, mark_svg(frags, c, vb=(-2, 16, 104, 68)),
            mark_svg(p10_bars(True), P10L, 'userandproduct', vb=(0, 0, 100, 100)))


# =============================================================== avatars
def avatar_svg(k, mark_light):
    """400px avatar artwork: the concept's background, the mark centered at a safe size."""
    c = CONCEPTS[k]
    bg = c['avatar_bg']
    inner = mark_light.split('</title>', 1)[1].rsplit('</svg>', 1)[0]
    vb = [float(v) for v in mark_light.split('viewBox="')[1].split('"')[0].split()]
    if k == 'P3':  # the square becomes the field; the letters stay at their size in it
        _, letters = p3_box()
        body = P(rect(0, 0, 100, 100), bg) + P(shift(shift(letters, -50, -50), 50, 50, 0.8), '#FFFFFF')
        return svg((0, 0, 100, 100), body, 'userandproduct avatar')
    if k == 'P4':
        return svg((0, 0, 100, 100), inner, 'userandproduct avatar')
    if k == 'P2':
        return svg((0, 0, 100, 100), P(rect(0, 0, 100, 100), bg) + P(rect(0, 30, 100, 44), '#121212'),
                   'userandproduct avatar')
    scale = 54 / max(vb[2], vb[3])
    w, h = vb[2] * scale, vb[3] * scale
    tx, ty = 50 - w / 2 - vb[0] * scale, 50 - h / 2 - vb[1] * scale
    body = (P(rect(0, 0, 100, 100), bg) +
            f'<g transform="translate({fmt(tx)} {fmt(ty)}) scale({fmt(scale)})">{inner}</g>')
    return svg((0, 0, 100, 100), body, 'userandproduct avatar')


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


def build(keys):
    for k in keys:
        m = k.lower()
        fn = CONCEPTS[k]['build']
        light_mark = None
        for mode in ('light', 'dark', 'mono'):
            lock, mark, fav = fn(mode)
            sfx = '' if mode == 'light' else '-' + mode
            write(f'{m}-lockup{sfx}.svg', lock)
            write(f'{m}-mark{sfx}.svg', mark)
            if mode == 'light':
                write(f'{m}-favicon.svg', fav)
                light_mark = mark
        av = avatar_svg(k, light_mark)
        write(f'{m}-avatar.svg', av)
        render_avatar(av, os.path.join(OUT, f'{m}-avatar-400.png'))
        subprocess.run([sys.executable, os.path.join(TOOLS, 'render.py'),
                        os.path.join(OUT, f'{m}-favicon.svg'), '--sizes', '16,32', '--square', '--pad', '0'],
                       check=True, stdout=subprocess.DEVNULL)


if __name__ == '__main__':
    keys = [a.upper() for a in sys.argv[1:]] or list(CONCEPTS)
    build(keys)
    import board
    board.write(CONCEPTS, OUT)
    print('built', ', '.join(keys))
