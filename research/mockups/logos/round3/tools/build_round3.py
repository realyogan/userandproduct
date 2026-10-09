"""Build the round-three logo concepts (N1 to N10) and the review board.

Run from this folder:
    python build_round3.py            # all SVGs, favicon PNGs and index.html
    python build_round3.py N3 N7      # only those concepts (index is rebuilt too)

Every wordmark is set from the OFL fonts in research/mockups/fonts/ with the shaping and
outline code of research/mockups/tools/wordmark.py (HarfBuzz kerning, fontTools outlines,
overlaps merged with skia-pathops). No <text> anywhere. Files go to the parent folder:
n<N>-lockup[-dark|-mono].svg, n<N>-mark[-dark|-mono].svg, n<N>-favicon.svg and
n<N>-favicon-16.png / -32.png (rendered with research/mockups/tools/render.py).
"""
import os
import subprocess
import sys
import xml.etree.ElementTree as ET

import pathops
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.svgLib.path import parse_path

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, '..'))
MOCK = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
TOOLS = os.path.join(MOCK, 'tools')
FONTDIR = os.path.join(MOCK, 'fonts')
sys.path.insert(0, TOOLS)
sys.path.insert(0, HERE)
import wordmark as WM  # noqa: E402

FONTS = {
    'inst-b': 'instrument-sans/InstrumentSans-Bold.ttf',
    'inst-r': 'instrument-sans/InstrumentSans-Regular.ttf',
    'frau-sb': 'fraunces/Fraunces72pt-SemiBold.ttf',
    'frau-r': 'fraunces/Fraunces72pt-Regular.ttf',
    'geist-b': 'geist/Geist-Bold.ttf',
    'geist-sb': 'geist/Geist-SemiBold.ttf',
    'geist-r': 'geist/Geist-Regular.ttf',
    'inter-b': 'inter/InterDisplay-Bold.ttf',
    'inter-sb': 'inter/InterDisplay-SemiBold.ttf',
    'space-b': 'space-grotesk/SpaceGrotesk-Bold.ttf',
    'bric-b': 'bricolage-grotesque/BricolageGrotesque-Bold.ttf',
}
_cache = {}


def font(key):
    if key not in _cache:
        _cache[key] = WM.FontRef(os.path.join(FONTDIR, FONTS[key]))
    return _cache[key]


def xh(key, size=100):
    """x-height in output units for one em = size."""
    f = font(key)
    return f.tt['OS/2'].sxHeight * size / f.upem


def caph(key, size=100):
    f = font(key)
    return f.tt['OS/2'].sCapHeight * size / f.upem


# ------------------------------------------------------------------ number and path helpers
def fmt(n):
    return WM.fmt(n)


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


def rrect(x0, y0, x1, y1, r):
    w, h = x1 - x0, y1 - y0
    return (f'M{fmt(x0 + r)} {fmt(y0)}h{fmt(w - 2 * r)}a{fmt(r)} {fmt(r)} 0 0 1 {fmt(r)} {fmt(r)}'
            f'v{fmt(h - 2 * r)}a{fmt(r)} {fmt(r)} 0 0 1 {fmt(-r)} {fmt(r)}h{fmt(-(w - 2 * r))}'
            f'a{fmt(r)} {fmt(r)} 0 0 1 {fmt(-r)} {fmt(-r)}v{fmt(-(h - 2 * r))}'
            f'a{fmt(r)} {fmt(r)} 0 0 1 {fmt(r)} {fmt(-r)}Z')


def poly(pts):
    return 'M' + 'L'.join(f'{fmt(x)} {fmt(y)}' for x, y in pts) + 'Z'


def circle(cx, cy, r):
    return (f'M{fmt(cx - r)} {fmt(cy)}a{fmt(r)} {fmt(r)} 0 1 0 {fmt(2 * r)} 0'
            f'a{fmt(r)} {fmt(r)} 0 1 0 {fmt(-2 * r)} 0Z')


def half_disc_down(cx, cy, r):
    """Half disc below the line y = cy (flat side up)."""
    return f'M{fmt(cx - r)} {fmt(cy)}H{fmt(cx + r)}A{fmt(r)} {fmt(r)} 0 0 1 {fmt(cx - r)} {fmt(cy)}Z'


def shift(d, dx, dy, s=1.0):
    return from_path(to_path(d).transform(s, 0, 0, s, dx, dy))


# ------------------------------------------------------------------ type setting (wordmark.py)
def setw(parts, fonts, size, x=0.0, y=0.0, tracking=0.0):
    """Set parts with wordmark.py's layout; baseline at y, pen starting at x.

    Returns a list of (path data, ink bounds) per part, overlaps merged.
    """
    if isinstance(parts, str):
        parts = [parts]
    if isinstance(fonts, str):
        fonts = [fonts] * len(parts)
    refs = [font(k) for k in fonts]
    placed = WM.layout(parts, refs, size, tracking)
    out = []
    for items in placed:
        moved = [(f, g, (m[0], m[1], m[2], m[3], m[4] + x, m[5] + y)) for f, g, m in items]
        d, b = WM.part_path(moved, True)
        out.append((d, b))
    return out


def ink_box(items):
    bs = [b for _, b in items if b]
    return (min(b[0] for b in bs), min(b[1] for b in bs), max(b[2] for b in bs), max(b[3] for b in bs))


def svg(vb, body, label, defs=''):
    x, y, w, h = vb
    d = f'<defs>{defs}</defs>' if defs else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{fmt(x)} {fmt(y)} {fmt(w)} {fmt(h)}" '
            f'role="img" aria-label="{label}"><title>{label}</title>{d}{body}</svg>')


def P(d, fill):
    return f'<path fill="{fill}" d="{d}"/>'


def fitbox(x0, y0, x1, y1, m):
    return (x0 - m, y0 - m, x1 - x0 + 2 * m, y1 - y0 + 2 * m)


INK, PAPER = '#111111', '#F3F1EC'


def colors(mode, light, dark):
    """light/dark: dicts of role -> color. mono: every role is currentColor."""
    if mode == 'mono':
        return {k: 'currentColor' for k in light}
    return light if mode == 'light' else dark


CONCEPTS = {}


def concept(key, **meta):
    def wrap(fn):
        CONCEPTS[key] = dict(meta, build=fn)
        return fn
    return wrap


# =============================================================== N1 the quiet "and"
N1L = {'ink': INK, 'acc': '#1F3FBF', 'tile': '#111111', 'on': '#FFFFFF'}
N1D = {'ink': PAPER, 'acc': '#8EA2FF', 'tile': '#F3F1EC', 'on': '#111111'}


def n1_word(c, x=0, y=0, size=100):
    items = setw(['user', 'and', 'product'], ['inst-b', 'inst-r', 'inst-b'], size, x, y, -10)
    body = P(items[0][0], c['ink']) + P(items[1][0], c['acc']) + P(items[2][0], c['ink'])
    return body, ink_box(items)


def n1_mark(c):
    # the lightened letter alone: a regular-weight "a" in the accent beside a bold "u",
    # set as the three initials u·a·p would not survive 16px, so the mark is "ua" in a tile
    items = setw(['u', 'a'], ['inst-b', 'inst-r'], 100, 0, 0, -20)
    x0, y0, x1, y1 = ink_box(items)
    w, h = x1 - x0, y1 - y0
    s = 62 / w
    dx, dy = 50 - (x0 + w / 2) * s, 50 - (y0 + h / 2) * s + 2
    u = shift(items[0][0], dx, dy, s)
    a = shift(items[1][0], dx, dy, s)
    return P(rrect(0, 0, 100, 100, 18), c['tile']) + P(u, c['on']) + P(a, c['acc'] if c['tile'] != 'currentColor' else 'currentColor')


@concept('N1', name='The quiet and', direction='Wordmark, Instrument Sans Bold and Regular',
         palette='Ink and Signal Blue', swatch=['#111111','#1F3FBF','#FFFFFF'], accent='#1F3FBF')
def n1(mode):
    c = colors(mode, N1L, N1D)
    body, (x0, y0, x1, y1) = n1_word(c)
    lock = svg(fitbox(x0, y0, x1, y1, 4), body, 'userandproduct')
    if mode == 'mono':
        # one color: the tile becomes an outline frame so the letters stay solid
        items = setw(['u', 'a'], ['inst-b', 'inst-r'], 100, 0, 0, -20)
        bx = ink_box(items)
        s = 62 / (bx[2] - bx[0])
        dx = 50 - (bx[0] + (bx[2] - bx[0]) / 2) * s
        dy = 50 - (bx[1] + (bx[3] - bx[1]) / 2) * s + 2
        ua = union(shift(items[0][0], dx, dy, s), shift(items[1][0], dx, dy, s))
        tile = minus(rrect(0, 0, 100, 100, 18), ua)
        mk = P(tile, 'currentColor')
    else:
        mk = n1_mark(c)
    mark = svg((0, 0, 100, 100), mk, 'userandproduct mark')
    fav = svg((0, 0, 100, 100), n1_mark(N1L), 'userandproduct')
    return lock, mark, fav


# =============================================================== N2 the nameplate
N2L = {'ink': INK, 'acc': '#6E1F24', 'tile': '#6E1F24', 'on': '#F2EDE4'}
N2D = {'ink': '#F2EDE4', 'acc': '#D27C80', 'tile': '#D27C80', 'on': '#1A1213'}


def n2_plate(c, size=100, track=150):
    items = setw('USERANDPRODUCT', 'frau-sb', size, 0, 0, track)
    x0, y0, x1, y1 = ink_box(items)
    cap = y1 - y0
    g = cap * 0.42           # gap between rules and capitals
    t1, t2 = cap * 0.035, cap * 0.10   # hairline and thick rule
    top = [rect(x0, y0 - g - t2, x1, y0 - g), rect(x0, y0 - g - t2 - t1 * 3 - t1, x1, y0 - g - t2 - t1 * 3)]
    bot = [rect(x0, y1 + g, x1, y1 + g + t2), rect(x0, y1 + g + t2 + t1 * 3, x1, y1 + g + t2 + t1 * 4)]
    body = P(items[0][0], c['ink']) + ''.join(P(d, c['acc']) for d in top + bot)
    return body, (x0, y0 - g - t2 - t1 * 4, x1, y1 + g + t2 + t1 * 4)


def n2_mark(c, fav=False):
    items = setw('U', 'frau-sb', 100)
    x0, y0, x1, y1 = ink_box(items)
    s = 56 / (y1 - y0)
    dx = 50 - (x0 + (x1 - x0) / 2) * s
    dy = 50 - (y0 + (y1 - y0) / 2) * s
    u = shift(items[0][0], dx, dy, s)
    if fav:
        return P(rrect(0, 0, 100, 100, 10), c['tile']) + P(u, c['on'])
    rules = [rect(14, 10, 86, 15), rect(14, 18, 86, 19.6), rect(14, 85, 86, 90), rect(14, 80.4, 86, 82)]
    return P(u, c['ink']) + ''.join(P(d, c['acc']) for d in rules)


@concept('N2', name='The nameplate', direction='Wordmark, Fraunces SemiBold capitals, tracked',
         palette='Oxblood and Bone', swatch=['#111111','#6E1F24','#F2EDE4'], accent='#6E1F24')
def n2(mode):
    c = colors(mode, N2L, N2D)
    body, (x0, y0, x1, y1) = n2_plate(c)
    lock = svg(fitbox(x0, y0, x1, y1, 4), body, 'USERANDPRODUCT')
    mark = svg((0, 0, 100, 100), n2_mark(c), 'userandproduct mark')
    fav = svg((0, 0, 100, 100), n2_mark(N2L, True), 'userandproduct')
    return lock, mark, fav


# =============================================================== N3 the ratio
N3L = {'ink': '#141414', 'acc': '#77736B'}
N3D = {'ink': '#F5F1E8', 'acc': '#A9A49A'}


def n3_stack(c):
    S = 100
    lead = S * 0.92
    user = setw('user', 'geist-b', S, 0, 0, -20)
    prod = setw('product', 'geist-b', S, 0, lead + S * 0.30, -20)
    ub, pb = ink_box(user), ink_box(prod)
    x0 = min(ub[0], pb[0])
    x1 = pb[2]
    rule_y = (ub[3] + (pb[1])) / 2
    andw = setw('and', 'geist-r', S * 0.42, 0, 0, 10)
    ab = ink_box(andw)
    ah = ab[3] - ab[1]
    and_items = setw('and', 'geist-r', S * 0.42, x0 - ab[0], rule_y - ab[1] - ah / 2 - 1, 10)
    ab2 = ink_box(and_items)
    rule = rect(ab2[2] + S * 0.08, rule_y - 0.9, x1, rule_y + 0.9)
    body = (P(user[0][0], c['ink']) + P(and_items[0][0], c['acc']) + P(rule, c['acc'])
            + P(prod[0][0], c['ink']))
    return body, (x0, ub[1], x1, pb[3])


def n3_mark(c, fav=False):
    u = setw('u', 'geist-b', 100)[0]
    p = setw('p', 'geist-b', 100)[0]
    ub, pb = u[1], p[1]
    s = 0.66 if not fav else 0.74
    # u on top, rule, p below: a fraction, u over p
    uh = (ub[3] - ub[1]) * s
    ph = (pb[3] - pb[1]) * s
    gap = 7 if not fav else 6
    rh = 4 if not fav else 6
    total = uh + gap + rh + gap + ph
    top = 50 - total / 2
    ud = shift(u[0], 50 - (ub[0] + (ub[2] - ub[0]) / 2) * s, top - ub[1] * s, s)
    ry = top + uh + gap
    pd = shift(p[0], 50 - (pb[0] + (pb[2] - pb[0]) / 2) * s, ry + rh + gap - pb[1] * s, s)
    rl = 22 if not fav else 16
    return P(ud, c['ink']) + P(rect(rl, ry, 100 - rl, ry + rh), c['acc']) + P(pd, c['ink'])


@concept('N3', name='The ratio', direction='Wordmark, Geist Bold over Geist Bold, two lines and a rule',
         palette='Newsprint: ink, warm paper and graphite', swatch=['#141414','#77736B','#F5F1E8'], accent='#77736B')
def n3(mode):
    c = colors(mode, N3L, N3D)
    body, (x0, y0, x1, y1) = n3_stack(c)
    lock = svg(fitbox(x0, y0, x1, y1, 5), body, 'userandproduct')
    mark = svg((0, 0, 100, 100), n3_mark(c), 'userandproduct mark')
    fav = svg((0, 0, 100, 100), n3_mark({'ink': '#141414', 'acc': '#141414'}, True), 'userandproduct')
    return lock, mark, fav


# =============================================================== N4 the bowl (M2's u, alone)
N4L = {'ink': INK, 'acc': '#B7791F'}
N4D = {'ink': PAPER, 'acc': '#E2AE4C'}


def n4_u(c, mono=False, x=0, y=0, s=1.0):
    """M2's u, refined: two square stems sitting on a solid half disc, one primitive each."""
    stems = union(rect(12, 10, 38, 50), rect(62, 10, 88, 50))
    bowl = half_disc_down(50, 50, 38)
    if mono:
        bowl = half_disc_down(50, 53, 38)    # a hairline of air keeps the build visible
        bowl = minus(bowl, rect(0, 0, 100, 53))
    return P(shift(stems, x, y, s), c['ink']) + P(shift(bowl, x, y, s), c['acc'])


@concept('N4', name='The bowl', direction='Letterform mark (M2\'s u, alone) with Inter Display SemiBold',
         palette='Ink and Amber', swatch=['#111111','#B7791F','#F3F1EC'], accent='#B7791F')
def n4(mode):
    c = colors(mode, N4L, N4D)
    mono = mode == 'mono'
    word = setw('userandproduct', 'inter-sb', 100, 0, 0, -15)
    wx = xh('inter-sb')
    # mark height = 1.5 x-height, sits from x-height top to below baseline
    s = wx * 1.62 / 78
    my = -wx * 1.62 + (-10 * s)  # mark top so its ink (10..88) spans x-height top to under baseline
    my = -wx - 0.31 * wx - 10 * s
    mark_body = n4_u(c, mono, 0, my, s)
    gap = 0.42 * wx
    word = setw('userandproduct', 'inter-sb', 100, 100 * s + gap, 0, -15)
    wb = ink_box(word)
    body = mark_body + P(word[0][0], c['ink'])
    top, bot = min(my + 10 * s, wb[1]), max(my + 88 * s, wb[3])
    lock = svg(fitbox(12 * s, top, wb[2], bot, 4), body, 'userandproduct')
    mark = svg((0, 0, 100, 100), n4_u(c, mono, 0, 1), 'userandproduct mark')
    fav = svg((6, 6, 88, 88), n4_u(N4L, False, 0, 1), 'userandproduct')
    return lock, mark, fav


# =============================================================== N5 the cornerstone
N5L = {'stone': '#2B2C30', 'hi': '#45474D', 'lt': '#393A3F', 'lo': '#17181A', 'dk': '#202124',
       'gold': '#B8924F', 'shade': '#6E5630', 'ink': INK}
N5D = {'stone': '#3A3C42', 'hi': '#5A5C63', 'lt': '#4A4C52', 'lo': '#232428', 'dk': '#2D2F33',
       'gold': '#D4AE6A', 'shade': '#7E6438', 'ink': PAPER}


def bevel_block(c, x0, y0, x1, y1, b):
    """A raised tablet in front elevation: face plus four bevels lit from the top left."""
    face = rect(x0 + b, y0 + b, x1 - b, y1 - b)
    top = poly([(x0, y0), (x1, y0), (x1 - b, y0 + b), (x0 + b, y0 + b)])
    left = poly([(x0, y0), (x0 + b, y0 + b), (x0 + b, y1 - b), (x0, y1)])
    bot = poly([(x0, y1), (x0 + b, y1 - b), (x1 - b, y1 - b), (x1, y1)])
    right = poly([(x1, y0), (x1, y1), (x1 - b, y1 - b), (x1 - b, y0 + b)])
    return (P(face, c['stone']) + P(top, c['hi']) + P(left, c['lt']) + P(bot, c['lo'])
            + P(right, c['dk']))


def incised(d, c, depth):
    """Gilded incised letters: the cut's shaded upper wall shows as a thin dark offset."""
    return P(shift(d, 0, -depth), c['shade']) + P(d, c['gold'])


def n5_mono_block(x0, y0, x1, y1, b, cuts):
    outer = rect(x0, y0, x1, y1)
    frame_gap = b * 0.28
    inner_line = minus(rect(x0 + b, y0 + b, x1 - b, y1 - b),
                       rect(x0 + b + frame_gap, y0 + b + frame_gap, x1 - b - frame_gap, y1 - b - frame_gap))
    return P(minus(outer, inner_line, *cuts), 'currentColor')


@concept('N5', name='The cornerstone', direction='Monument: the name incised in a granite tablet',
         palette='Granite and Bronze', swatch=['#2B2C30','#B8924F','#F3F1EC'], accent='#B8924F')
def n5(mode):
    c = colors(mode, N5L, N5D)
    mono = mode == 'mono'
    S = 100
    word = setw('userandproduct', 'frau-sb', S, 0, 0, 10)
    wb = ink_box(word)
    year = setw('MMXXVI', 'frau-r', S * 0.24, 0, 0, 420)
    yb = ink_box(year)
    padx, pady, b = 34, 30, 13
    x0, x1 = wb[0] - padx - b, wb[2] + padx + b
    ygap = 20
    y0 = wb[1] - pady - b
    yl = wb[3] + ygap - yb[1]
    yx = (wb[0] + wb[2]) / 2 - (yb[2] + yb[0]) / 2
    year = setw('MMXXVI', 'frau-r', S * 0.24, yx, yl, 420)
    yb = ink_box(year)
    y1 = yb[3] + pady * 0.8 + b
    rule_y = (wb[3] + yb[1]) / 2
    rules = [rect(x0 + b + 22, rule_y - 0.8, yb[0] - 16, rule_y + 0.8),
             rect(yb[2] + 16, rule_y - 0.8, x1 - b - 22, rule_y + 0.8)]
    if mono:
        body = n5_mono_block(x0, y0, x1, y1, b, [word[0][0], year[0][0]] + rules)
    else:
        body = (bevel_block(c, x0, y0, x1, y1, b) + incised(word[0][0], c, 1.6)
                + incised(year[0][0], c, 0.8) + ''.join(P(r, c['gold']) for r in rules))
    lock = svg(fitbox(x0, y0, x1, y1, 3), body, 'userandproduct')

    def mark_body(cc, monoflag, fav=False):
        u = setw('u', 'frau-sb', 100)[0]
        ub = u[1]
        s = (40 if not fav else 52) / (ub[3] - ub[1])
        ud = shift(u[0], 50 - (ub[0] + (ub[2] - ub[0]) / 2) * s, 52 - (ub[1] + (ub[3] - ub[1]) / 2) * s, s)
        bb = 12 if not fav else 9
        x0m, y0m, x1m, y1m = (8, 8, 92, 92) if not fav else (2, 2, 98, 98)
        if monoflag:
            return n5_mono_block(x0m, y0m, x1m, y1m, bb, [ud])
        return bevel_block(cc, x0m, y0m, x1m, y1m, bb) + incised(ud, cc, 1.2 if not fav else 0)
    mark = svg((0, 0, 100, 100), mark_body(c, mono), 'userandproduct mark')
    fav = svg((0, 0, 100, 100), mark_body(N5L, False, True), 'userandproduct')
    return lock, mark, fav


# =============================================================== N6 the stylobate
N6L = {'ink': INK, 'acc': '#1F3FBF'}
N6D = {'ink': PAPER, 'acc': '#8EA2FF'}


def grow(d, r):
    """The shape enlarged by r all round (stroke outline united with the fill)."""
    p = to_path(d)
    q = to_path(d)
    q.stroke(2 * r, pathops.LineCap.ROUND_CAP, pathops.LineJoin.ROUND_JOIN, 4)
    q.convertConicsToQuads()
    return from_path(pathops.op(p, q, pathops.PathOp.UNION))


def steps(x0, x1, ytop, h, out, n=3, gap=0):
    ds = []
    for i in range(n):
        ds.append(rect(x0 - out * i, ytop + (h + gap) * i, x1 + out * i, ytop + (h + gap) * i + h))
    return ds


@concept('N6', name='The stylobate', direction='Monument: the name stands on three temple steps',
         palette='Ink and Royal Blue', swatch=['#111111','#1F3FBF','#FFFFFF'], accent='#1F3FBF')
def n6(mode):
    c = colors(mode, N6L, N6D)
    word = setw('userandproduct', 'frau-sb', 100, 0, 0, -5)
    wb = ink_box(word)
    # the steps start right under the baseline; the two p descenders are sunk into them,
    # cut out with a margin of air, so the name stands on the stone rather than above it
    full = steps(wb[0] + 30, wb[2] - 30, 3, 15, 15, 3, 0)
    hole = grow(word[0][0], 3.2)
    st = [minus(d, hole) for d in full]
    body = P(word[0][0], c['ink']) + ''.join(P(d, c['acc']) for d in st if d)
    sb = bounds(full[-1])
    lock = svg(fitbox(sb[0], wb[1], sb[2], sb[3], 4), body, 'userandproduct')

    def mark_body(cc, fav=False):
        u = setw('u', 'frau-sb', 100)[0]
        ub = u[1]
        s = (50 if not fav else 60) / (ub[2] - ub[0])
        uh = (ub[3] - ub[1]) * s
        n = 3 if not fav else 2
        h, g, o = (9, 0, 9) if not fav else (11, 0, 11)
        stack = n * h + (n - 1) * g
        lift = 3 if not fav else 4
        top = 50 - (uh + lift + stack) / 2
        ud = shift(u[0], 50 - (ub[0] + (ub[2] - ub[0]) / 2) * s, top - ub[1] * s, s)
        half = (ub[2] - ub[0]) * s / 2
        sts = steps(50 - half - 4, 50 + half + 4, top + uh + lift, h, o, n, g)
        return center(P(ud, cc['ink']) + ''.join(P(d, cc['acc']) for d in sts))
    mark = svg((0, 0, 100, 100), mark_body(c), 'userandproduct mark')
    fav = svg((0, 0, 100, 100), mark_body(N6L, True), 'userandproduct')
    return lock, mark, fav


def center(frags):
    """Move a 100-unit mark so its ink is centered in the 100-unit box."""
    ds = [f.split(' d="')[1].split('"')[0] for f in frags.split('<path ')[1:]]
    x0, y0, x1, y1 = bounds(union(*ds))
    return place(frags, 50 - (x0 + x1) / 2, 50 - (y0 + y1) / 2, 1.0)


def place(frags, dx, dy, s):
    """Re-place the <path> elements of a 100-unit mark into lockup coordinates."""
    out = ''
    for frag in frags.split('<path ')[1:]:
        fill = frag.split('fill="')[1].split('"')[0]
        d = frag.split(' d="')[1].split('"')[0]
        out += P(shift(d, dx, dy, s), fill)
    return out


# =============================================================== N7 the stair
N7L = {'ink': '#0E0E0E', 'acc': '#E5372A', 'blk': '#0E0E0E'}
N7D = {'ink': '#F2F0EB', 'acc': '#FF5A47', 'blk': '#F2F0EB'}


def n7_mark(c, mono=False, fav=False):
    """A stair of three solid steps, one mass; the top step is cut in the accent: the
    reading order from first principles to the landing."""
    if fav:
        m, top = 2, 6
    else:
        m, top = 8, 12
    w = (100 - 2 * m) / 3
    h = (100 - top - m) / 3
    y = lambda i: top + h * i
    mass = poly([(m, 100 - m), (m, y(2)), (m + w, y(2)), (m + w, y(1)), (m + 2 * w, y(1)),
                 (m + 2 * w, y(0)), (100 - m, y(0)), (100 - m, 100 - m)])
    land = rect(m + 2 * w, y(0), 100 - m, y(1))
    rest = minus(mass, land)
    if mono:
        air = 3 if not fav else 4
        rest = minus(rest, rect(m + 2 * w - air, y(1) - 0.01, 100, y(1) + air))
        rest = minus(rest, rect(m + 2 * w - air, 0, m + 2 * w, y(1) + air))
        return P(rest, 'currentColor') + P(land, 'currentColor')
    return P(rest, c['blk']) + P(land, c['acc'])


@concept('N7', name='The stair', direction='Abstract: three solid steps, the top one reached',
         palette='Signal Red on Black', swatch=['#0E0E0E','#E5372A','#F2F0EB'], accent='#E5372A')
def n7(mode):
    c = colors(mode, N7L, N7D)
    mono = mode == 'mono'
    wx = xh('space-b')
    s = (wx * 1.62) / 80
    mtop = -92 * s          # stair foot on the baseline
    mk = n7_mark(c, mono)
    gap = 0.42 * wx
    word = setw('userandproduct', 'space-b', 100, 92 * s + gap, 0, -10)
    wb = ink_box(word)
    body = place(mk, 0, mtop, s) + P(word[0][0], c['ink'])
    lock = svg(fitbox(8 * s, min(mtop + 12 * s, wb[1]), wb[2], max(0, wb[3]), 4), body, 'userandproduct')
    mark = svg((0, 0, 100, 100), mk, 'userandproduct mark')
    fav = svg((0, 0, 100, 100), n7_mark(N7L, False, True), 'userandproduct')
    return lock, mark, fav


# =============================================================== N8 true north
N8L = {'ink': '#141414', 'acc': '#1F4A3A'}
N8D = {'ink': '#F3EEDF', 'acc': '#7FC3A2'}


def n8_arrow(c, mono=False, fav=False):
    """The surveyor's north arrow from a site plan: an arrowhead split down its spine,
    one half solid in the accent, the other in ink."""
    if fav:
        tip, base, notch, w = (50, 2), 98, 76, 34
    else:
        tip, base, notch, w = (50, 6), 94, 72, 26
    left = poly([tip, (50, notch), (50 - w, base)])
    right = poly([tip, (50 + w, base), (50, notch)])
    if mono:
        # one color: the right half becomes an outline
        inner = poly([(50 + 3, tip[1] + 22), (50 + w - 9, base - 7), (50 + 3, notch - 3)])
        return P(left, 'currentColor') + P(minus(right, inner), 'currentColor')
    return P(left, c['acc']) + P(right, c['ink'])


@concept('N8', name='True north', direction="Abstract: the north arrow from a surveyor's site plan",
         palette='Forest and Cream', swatch=['#141414','#1F4A3A','#F3EEDF'], accent='#1F4A3A')
def n8(mode):
    c = colors(mode, N8L, N8D)
    mono = mode == 'mono'
    wx = xh('inst-b')
    s = wx * 1.75 / 88
    mtop = -wx * 1.4 - 6 * s
    frags = n8_arrow(c, mono)
    gap = 0.36 * wx
    shapes = place(frags, -24 * s, mtop, s)
    word = setw('userandproduct', 'inst-b', 100, 52 * s + gap, 0, -10)
    wb = ink_box(word)
    lock = svg(fitbox(0, min(mtop + 6 * s, wb[1]), wb[2], max(mtop + 94 * s, wb[3]), 4),
               shapes + P(word[0][0], c['ink']), 'userandproduct')
    mark = svg((0, 0, 100, 100), frags, 'userandproduct mark')
    fav = svg((0, 0, 100, 100), n8_arrow(N8L, False, True), 'userandproduct')
    return lock, mark, fav


# =============================================================== N9 the fulcrum
N9L = {'ink': '#1C1A1C', 'acc': '#5A2352'}
N9D = {'ink': '#F2ECE4', 'acc': '#D59BCB'}


def n9_mark_d(fav=False):
    if fav:
        beam = rect(2, 26, 98, 44)
        piv = poly([(50, 44), (80, 94), (20, 94)])
    else:
        beam = rect(6, 32, 94, 44)
        piv = poly([(50, 44), (72, 82), (28, 82)])
    return beam, piv


@concept('N9', name='The fulcrum', direction='Abstract: one beam held level on a single pivot',
         palette='Plum and Parchment', swatch=['#1C1A1C','#5A2352','#F2ECE4'], accent='#5A2352')
def n9(mode):
    c = colors(mode, N9L, N9D)
    beam, piv = n9_mark_d()
    if mode == 'mono':
        piv = minus(piv, rect(0, 44, 100, 47))
    wx = xh('bric-b')
    s = wx * 1.25 / 50
    dy = -82 * s       # pivot base on the baseline
    dx = -6 * s
    gap = 0.4 * wx
    word = setw('userandproduct', 'bric-b', 100, 88 * s + gap, 0, -5)
    wb = ink_box(word)
    mk = P(beam, c['acc']) + P(piv, c['ink'])
    lk = P(shift(beam, dx, dy, s), c['acc']) + P(shift(piv, dx, dy, s), c['ink'])
    lock = svg(fitbox(0, min(32 * s + dy, wb[1]), wb[2], max(82 * s + dy, wb[3]), 4),
               lk + P(word[0][0], c['ink']), 'userandproduct')
    mark = svg((0, 0, 100, 100), mk, 'userandproduct mark')
    fb, fp = n9_mark_d(True)
    fav = svg((0, 0, 100, 100), P(fb, N9L['acc']) + P(fp, N9L['ink']), 'userandproduct')
    return lock, mark, fav


# =============================================================== N10 the lectern
N10L = {'ink': '#1C2B4B', 'acc': '#A8822E'}
N10D = {'ink': '#EFEBE0', 'acc': '#D9B562'}


def n10_parts(fav=False):
    """Side elevation of a lectern: a steep reading desk with a ledge, one post, a foot."""
    if fav:
        desk = union(poly([(2, 6), (92, 34), (92, 50), (2, 22)]), rect(84, 22, 98, 50))
        post = rect(38, 36, 58, 86)
        foot = rect(14, 82, 86, 98)
    else:
        desk = union(poly([(8, 10), (86, 34), (86, 46), (8, 22)]), rect(82, 26, 92, 46))
        post = rect(42, 36, 54, 82)
        foot = rect(22, 80, 76, 90)
    return desk, union(post, foot)


@concept('N10', name='The lectern', direction='Abstract: the reading stand one speaks from',
         palette='Navy and Brass', swatch=['#1C2B4B','#A8822E','#EFEBE0'], accent='#A8822E')
def n10(mode):
    c = colors(mode, N10L, N10D)
    desk, stand = n10_parts()
    if mode == 'mono':
        stand = minus(stand, grow(desk, 2.5))
    wx = xh('inter-b')
    s = wx * 1.7 / 80
    dy = -90 * s       # foot on the baseline
    dx = -8 * s
    gap = 0.5 * wx
    word = setw('userandproduct', 'inter-b', 100, 84 * s + gap, 0, -18)
    wb = ink_box(word)
    body = P(shift(desk, dx, dy, s), c['acc']) + P(shift(stand, dx, dy, s), c['ink']) + P(word[0][0], c['ink'])
    lock = svg(fitbox(0, min(10 * s + dy, wb[1]), wb[2], max(90 * s + dy, wb[3]), 4), body, 'userandproduct')
    mark = svg((0, 0, 100, 100), P(desk, c['acc']) + P(stand, c['ink']), 'userandproduct mark')
    fd, fs = n10_parts(True)
    fav = svg((0, 0, 100, 100), P(fd, N10L['acc']) + P(fs, N10L['ink']), 'userandproduct')
    return lock, mark, fav


# =============================================================== write, validate, render
def write(name, text):
    ET.fromstring(text)  # raises if the SVG is not well formed
    assert '<text' not in text and ' width=' not in text.split('>')[0]
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        f.write(text)


def build(keys):
    for k in keys:
        m = k.lower()
        fn = CONCEPTS[k]['build']
        for mode in ('light', 'dark', 'mono'):
            lock, mark, fav = fn(mode)
            sfx = '' if mode == 'light' else '-' + mode
            write(f'{m}-lockup{sfx}.svg', lock)
            write(f'{m}-mark{sfx}.svg', mark)
            if mode == 'light':
                write(f'{m}-favicon.svg', fav)
        subprocess.run([sys.executable, os.path.join(TOOLS, 'render.py'),
                        os.path.join(OUT, f'{m}-favicon.svg'), '--sizes', '16,32', '--square', '--pad', '0'],
                       check=True, stdout=subprocess.DEVNULL)


if __name__ == '__main__':
    keys = [a.upper() for a in sys.argv[1:]] or list(CONCEPTS)
    build(keys)
    import board
    board.write(CONCEPTS, OUT)
    print('built', ', '.join(keys))
