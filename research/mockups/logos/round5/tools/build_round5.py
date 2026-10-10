"""Build the round-five logo concepts (Q1 to Q10) and the review board.

Brief: six readings of a three-legged structure (a spine, two struts, three terminals; no cross-bar),
three developments of round four's weighted ring (P6), and one fusion of the two.

Run from this folder:
    python build_round5.py            # all SVGs, PNG renders and index.html
    python build_round5.py Q3 Q8      # only those concepts (index is rebuilt too)

Wordmarks are set from the OFL fonts in research/mockups/fonts/ with the shaping and outline code
of research/mockups/tools/wordmark.py. Strokes are built as filled outlines and merged with
skia-pathops, so every file is plain filled paths. No <text> anywhere. Files go to the parent
folder, per concept q<N>:
  q<N>-lockup.svg, -lockup-dark.svg, -lockup-mono.svg
  q<N>-mark.svg,   -mark-dark.svg,   -mark-mono.svg
  q<N>-favicon.svg (the reduced form) with q<N>-favicon-16.png and -32.png
  q<N>-avatar.svg with q<N>-avatar-400.png (circle crop)
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


CONCEPTS = {}


def concept(key, **meta):
    def wrap(fn):
        CONCEPTS[key] = dict(meta, build=fn)
        return fn
    return wrap


# =============================================================== Q1 the plumb line
Q1L = {'m': '#6B1E2A', 'ink': '#6B1E2A'}
Q1D = {'m': '#E5A0A8', 'ink': WORD_DARK}


def q1_mark():
    A = (50, 3)
    sides, centre = [(28, 58), (72, 58)], (50, 84)
    w = 2.2
    parts = [seg(*A, *p, w) for p in sides] + [seg(*A, *centre, w)]
    parts += [circle(*p, 7.5) for p in sides] + [circle(*centre, 13)]
    return union(*parts)


def q1_fav():
    return union(seg(50, 0, 50, 50, 10, 'butt'), circle(50, 70, 27))


@concept('Q1', name='The plumb line', group='Tripod',
         reading='A plumb line with three weights: hairline cords from one point, the heaviest weight lowest',
         palette='Oxblood on Cream', swatch=['#6B1E2A', PAPER_CREAM, '#FFFFFF'],
         treatment='Hairline cords, three solid weights (the center one larger and lower)',
         typeface='Fraunces SemiBold, lowercase', reduction='One weight on a cord: a plumb bob',
         hh=40, avatar_bg=PAPER_CREAM, paper=PAPER_CREAM)
def q1(mode):
    return make(mode, q1_mark(), q1_fav(), 'frau-sb', -10, 1.75, 0.4, Q1L, Q1D)


# =============================================================== Q2 the stand
Q2L = {'m': '#141414', 'ink': '#141414'}
Q2D = {'m': '#F1EEE7', 'ink': '#F1EEE7'}


def q2_mark(w=10, r=10):
    top, base = 2, 94
    a = seg(60, top - 8, 14, base + 8, w, 'butt')
    b = seg(40, top - 8, 86, base + 8, w, 'butt')
    # the legs cross just under the top; the rear leg drops from the crossing to a solid foot
    t = (60 - 50) / (60 - 14)
    yx = top - 8 + t * (base - top + 16)
    spine = seg(50, yx, 50, base - r, w, 'butt')
    d = clip(union(a, b, spine), -10, top, 110, base)
    return union(d, circle(50, base - r, r))


@concept('Q2', name='The stand', group='Tripod',
         reading='An easel or stand reduced to its legs: two struts crossing at the top, a rear leg ending in a weight',
         palette='Ink and White', swatch=['#141414', '#FFFFFF', '#F3F1EC'],
         treatment='Uniformly heavy, ends cut to one baseline; a single solid foot on the spine',
         typeface='Instrument Sans Bold, lowercase', reduction='The same three legs, thickened',
         hh=34, avatar_bg='#FFFFFF')
def q2(mode):
    return make(mode, q2_mark(), q2_mark(15, 13), 'inst-b', -10, 1.45, 0.42, Q2L, Q2D)


# =============================================================== Q3 the tree of three
Q3L = {'m': '#1D4636', 'ink': '#1D4636'}
Q3D = {'m': '#9CC9B0', 'ink': WORD_DARK}


def q3_mark(w=5, r=11, t=5, J=(50, 10), sides=((16, 84), (84, 84)), centre=(50, 58), rc=None):
    rc = rc or r
    lines = [seg(*J, *p, w) for p in sides] + [seg(*J, *centre, w)]
    d = union(*lines, *[circle(*p, r) for p in sides], circle(*centre, rc))
    return minus(d, *[circle(*p, r - t) for p in sides])


@concept('Q3', name='The tree of three', group='Tripod',
         reading='A tree of three terminals from one root: two hollow (user, product), one solid in the middle (the reader)',
         palette='Deep Green on Cream', swatch=['#1D4636', PAPER_CREAM, '#FFFFFF'],
         treatment='Medium line, two hollow rings and one solid disc; the solid one sits higher, nearer the root',
         typeface='Fraunces SemiBold, lowercase', reduction='Three terminals on thick lines, the solid one centered',
         hh=40, avatar_bg=PAPER_CREAM, paper=PAPER_CREAM)
def q3(mode):
    fav = q3_mark(w=11, r=17, t=8, J=(50, 4), sides=((17, 82), (83, 82)), centre=(50, 50), rc=15)
    return make(mode, q3_mark(), fav, 'frau-sb', -10, 1.7, 0.4, Q3L, Q3D)


# =============================================================== Q4 the braced tripod
Q4L = {'m': '#14284B', 'ink': '#14284B'}
Q4D = {'m': '#9DB4E6', 'ink': WORD_DARK}


def q4_mark(w=7, r=9.5, A=(50, 14), Lp=(6, 62), C=(50, 80)):
    Rp = (100 - Lp[0], Lp[1])
    lines = [seg(*A, *Lp, w), seg(*A, *Rp, w), seg(*Lp, *C, w), seg(*Rp, *C, w), seg(*A, *C, w)]
    return union(*lines, circle(*Lp, r), circle(*Rp, r), circle(*C, r))


@concept('Q4', name='The braced tripod', group='Tripod',
         reading="A surveyor's tripod braced at the feet, flattened wide and low so it stands rather than points",
         palette='Deep Navy and White', swatch=['#14284B', '#FFFFFF', '#F3F1EC'],
         treatment='Uniformly heavy line with round joins, three solid feet of one size',
         typeface='Instrument Sans Bold, lowercase', reduction='The same frame, heavier, feet enlarged',
         hh=30, avatar_bg='#FFFFFF')
def q4(mode):
    fav = q4_mark(w=12, r=13, A=(50, 12), Lp=(10, 64), C=(50, 84))
    return make(mode, q4_mark(), fav, 'inst-b', -10, 1.3, 0.42, Q4L, Q4D)


# =============================================================== Q5 the chandelier
Q5L = {'m': '#B3141C', 'ink': '#141414'}
Q5D = {'m': '#F0676C', 'ink': WORD_DARK}


def q5_mark():
    J, top = (50, 60), (50, 2)
    rings = [(14, 46), (86, 46), (50, 84)]
    r, t, w = 10.5, 5.5, 3.2
    lines = [seg(*top, 50, 84, w, 'butt'), seg(*J, 14, 46, w), seg(*J, 86, 46, w)]
    d = union(*lines, *[circle(*p, r) for p in rings])
    return minus(d, *[circle(*p, r - t) for p in rings])


def q5_fav():
    return minus(union(seg(50, 0, 50, 50, 11, 'butt'), circle(50, 68, 29)), circle(50, 68, 16))


@concept('Q5', name='The chandelier', group='Tripod',
         reading='A chandelier or a balance: one cord from above, two arms lifting two rings, a third ring hanging below',
         palette='Press Red and Ink', swatch=['#B3141C', '#141414', '#FFFFFF'],
         treatment='Fine line, three heavy hollow rings of one size',
         typeface='Fraunces SemiBold, lowercase', reduction='One ring on a cord',
         hh=40, avatar_bg='#FFFFFF')
def q5(mode):
    return make(mode, q5_mark(), q5_fav(), 'frau-sb', -10, 1.75, 0.4, Q5L, Q5D)


# =============================================================== Q6 the pure reduction
Q6L = {'m': '#1F3FBF', 'ink': '#141414'}
Q6D = {'m': '#8EA2FF', 'ink': WORD_DARK}


def q6_mark(w=5.5, r=12.5, gap=4.5, A=(50, 4), base=80, xs=(14, 50, 86)):
    feet = [(x, base) for x in xs]
    lines = [seg(*A, *toward(*A, *p, r + gap), w, 'butt') for p in feet]
    d = union(*lines, circle(*A, w / 2))
    return union(d, *[circle(*p, r) for p in feet])


@concept('Q6', name='The pure reduction', group='Tripod',
         reading='Nothing but the parts: one vertical, two diagonals, three equal circles, the lines stopping short of the circles',
         palette='Signal Blue and Ink', swatch=['#1F3FBF', '#141414', '#FFFFFF'],
         treatment='Medium line, three solid circles of one size on one baseline, detached from the lines',
         typeface='Instrument Sans Bold, lowercase', reduction='Three discs and three lines, heavier, smaller gaps',
         hh=32, avatar_bg='#FFFFFF')
def q6(mode):
    fav = q6_mark(w=11, r=15, gap=4, A=(50, 6), base=80, xs=(16, 50, 84))
    return make(mode, q6_mark(), fav, 'inst-b', -10, 1.45, 0.42, Q6L, Q6D)


# =============================================================== Q7 the slotted disc
Q7L = {'m': '#1D4636', 'ink': '#1D4636'}
Q7D = {'m': '#9CC9B0', 'ink': WORD_DARK}


def q7_mark(fav=False):
    """A solid disc with one straight slot cut from the top edge down to the exact center."""
    w = 13 if fav else 9
    slot = union(rect(50 - w / 2, -2, 50 + w / 2, 50), circle(50, 50, w / 2))
    return minus(circle(50, 50, 50), slot)


@concept('Q7', name='The slotted disc', group='Weighted ring',
         reading='P6 rebuilt around a second feature: the opening becomes one slot cut from the rim through to the center, the spine of the tripod drawn as a cut',
         palette='Deep Green on Cream', swatch=['#1D4636', PAPER_CREAM, '#FFFFFF'],
         treatment='Solid disc, one radial slot from the top edge to the center, round at its foot',
         typeface='Instrument Sans Bold, lowercase', reduction='The same disc with a wider slot',
         hh=30, avatar_bg=PAPER_CREAM, paper=PAPER_CREAM)
def q7(mode):
    return make(mode, q7_mark(), q7_mark(True), 'inst-b', -10, 1.36, 0.42, Q7L, Q7D)


# =============================================================== Q8 the weighted foot
Q8L = {'m': '#14284B', 'ink': '#14284B'}
Q8D = {'m': '#9DB4E6', 'ink': WORD_DARK}


def q8_mark(fav=False):
    """The tripod with its center foot replaced by the weighted ring (a disc with its opening set high)."""
    if fav:
        A, sides, rs, w, C, R, op = (50, 2), ((12, 52), (88, 52)), 10, 9, (50, 70), 28, (50, 63, 13)
    else:
        A, sides, rs, w, C, R, op = (50, 2), ((14, 54), (86, 54)), 7, 4, (50, 72), 26, (50, 64, 14)
    lines = [seg(*A, *p, w) for p in sides] + [seg(*A, C[0], C[1] - R + 1, w, 'butt')]
    d = union(*lines, *[circle(*p, rs) for p in sides], circle(*C, R))
    return minus(d, circle(*op))


@concept('Q8', name='The weighted foot', group='Weighted ring',
         reading='The ring holding the structure: three legs from one point, the center leg ending in the weighted ring, the outer two in small weights',
         palette='Deep Navy and White', swatch=['#14284B', '#FFFFFF', '#F3F1EC'],
         treatment='Medium line, two small solid weights, one large ring with a high opening as the center foot',
         typeface='Fraunces SemiBold, lowercase', reduction='The same, lines doubled, outer weights enlarged',
         hh=40, avatar_bg='#FFFFFF')
def q8(mode):
    return make(mode, q8_mark(), q8_mark(True), 'frau-sb', -10, 1.75, 0.4, Q8L, Q8D)


# =============================================================== Q9 the slotted block
Q9L = {'m': '#6B1E2A', 'ink': '#6B1E2A'}
Q9D = {'m': '#E5A0A8', 'ink': WORD_DARK}


def q9_mark(fav=False):
    """The square counterpart of Q7: a solid block with one slot cut from the top edge to the center."""
    w = 14 if fav else 10
    return minus(rect(0, 0, 100, 100), rect(50 - w / 2, -2, 50 + w / 2, 52))


@concept('Q9', name='The slotted block', group='Weighted ring',
         reading='The square counterpart: a solid block with one straight slot from the top edge to the center, flat at its foot, like a mortise',
         palette='Oxblood on Cream', swatch=['#6B1E2A', PAPER_CREAM, '#FFFFFF'],
         treatment='Solid square, one flat-ended slot to the center; the lower half untouched',
         typeface='Fraunces SemiBold, lowercase', reduction='The same, slot wider',
         hh=30, avatar_bg=PAPER_CREAM, paper=PAPER_CREAM)
def q9(mode):
    return make(mode, q9_mark(), q9_mark(True), 'frau-sb', -10, 1.3, 0.45, Q9L, Q9D)


# =============================================================== Q10 the ring on three legs
Q10L = {'m': '#8A6424', 'ink': '#141414'}
Q10D = {'m': '#D6B272', 'ink': WORD_DARK}


def q10_mark(fav=False):
    if fav:
        R, ho, w, spread = 30, (50, 25, 15), 11, 16
    else:
        R, ho, w, spread = 28, (50, 24, 15), 8, 14
    C, base = (50, 32), 98
    legs = [seg(*C, spread, base + 6, w, 'butt'), seg(*C, 100 - spread, base + 6, w, 'butt'),
            seg(*C, 50, base + 6, w, 'butt')]
    d = union(clip(union(*legs), -10, 0, 110, base), circle(*C, R))
    return minus(d, circle(*ho))


@concept('Q10', name='The ring on three legs', group='Fusion',
         reading="The two ideas joined: round four's weighted ring carried as the head of the three-legged stand",
         palette='Bronze and Ink on Cream', swatch=['#8A6424', '#141414', PAPER_CREAM],
         treatment='Heavy ring with a high opening on three heavy legs, cut to one baseline',
         typeface='Instrument Sans Bold, lowercase', reduction='The same, legs and ring thickened',
         hh=36, avatar_bg=PAPER_CREAM, paper=PAPER_CREAM)
def q10(mode):
    return make(mode, q10_mark(), q10_mark(True), 'inst-b', -10, 1.6, 0.42, Q10L, Q10D)


# =============================================================== avatars
def avatar_svg(k, mark_light):
    c = CONCEPTS[k]
    bg = c['avatar_bg']
    inner = mark_light.split('</title>', 1)[1].rsplit('</svg>', 1)[0]
    vb = [float(v) for v in mark_light.split('viewBox="')[1].split('"')[0].split()]
    scale = 56 / max(vb[2], vb[3])
    w, h = vb[2] * scale, vb[3] * scale
    tx, ty = 50 - w / 2 - vb[0] * scale, 50 - h / 2 - vb[1] * scale
    body = (P(rect(0, 0, 100, 100), bg) +
            f'<g transform="translate({fmt(tx)} {fmt(ty)}) scale({round(scale, 4)})">{inner}</g>')
    return svg((0, 0, 100, 100), body, 'userandproduct avatar')


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
    if os.path.exists(os.path.join(HERE, 'board.py')):
        import board
        board.write(CONCEPTS, OUT)
    print('built', ', '.join(keys))
