"""Build the round-seven triangles family (T1 to T18) and its review board.

Brief (owner, 9 Oct 2026): derivatives of three triangle sketches (two outlined triangles stacked with a
filled triangle in the overlap; a cluster of outlined triangles with small filled ones inside; a diamond
made of a triangular tessellation), including versions carved into a disc. Abstract and secular; one
owned color per concept; the name "userandproduct" set in Instrument Sans or Fraunces beside the mark.

Run from this folder:
    python build_triangles.py            # all SVGs, PNG renders and index.html
    python build_triangles.py T3 T8      # only those concepts (index is rebuilt too)

Figures live in figs7.py (every cut a real skia-pathops boolean), shared helpers in geom7.py, the
board in board7.py and the notes in notes7.py. Files per concept t<N>, in the parent folder:
  t<N>-lockup.svg, -lockup-dark.svg, -lockup-mono.svg
  t<N>-mark.svg,   -mark-dark.svg,   -mark-mono.svg
  t<N>-favicon.svg (heavier drawing for 16px) with t<N>-favicon-16.png and -32.png
  t<N>-avatar.svg with t<N>-avatar-400.png (circle crop)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from geom7 import OUT, P, bounds, caph, fitbox, rect, render_avatar, resvg_py, shift, svg, word, write  # noqa: E402
from figs7 import FIG  # noqa: E402

WORD_DARK = '#EEE9DF'
INK = '#141414'
CREAM = '#F4EFE3'
WHITE = '#FFFFFF'

# name: (light, dark)
PAL = {
    'blue': ('#1F3FBF', '#8EA2FF'),
    'navy': ('#14284B', '#9DB4E6'),
    'green': ('#1D4636', '#9CC9B0'),
    'oxblood': ('#6B1E2A', '#E5A0A8'),
    'red': ('#B3141C', '#F0676C'),
    'bronze': ('#8A6424', '#D6B272'),
    'ink': (INK, '#F1EEE7'),
}
PAL_NAME = {'blue': 'Blue, Black and White', 'navy': 'Deep Navy', 'green': 'Deep Green', 'oxblood': 'Oxblood',
            'red': 'Press Red', 'bronze': 'Bronze', 'ink': 'Ink'}
TYPE = {'inst-b': 'Instrument Sans Bold, lowercase', 'frau-sb': 'Fraunces SemiBold, lowercase'}

C = {}


def concept(key, name, group, reading, pal, o='ink', a=None, word_col='ink', font='inst-b', paper=WHITE,
            h=1.55, yc=0.5, tint=None, hh=34):
    """o, a, word_col name a palette (or 'ink'); tint gives the accent as a lighter shade of one color."""
    a = a or pal
    L = {'o': PAL[o][0], 'a': PAL[a][0], 'm': PAL[pal][0], 'ink': PAL[word_col][0]}
    D = {'o': WORD_DARK if o == 'ink' else PAL[o][1], 'a': PAL[a][1], 'm': PAL[pal][1],
         'ink': WORD_DARK if word_col == 'ink' else PAL[word_col][1]}
    if tint:
        L['a'], D['a'] = tint
    paper_name = 'Cream' if paper == CREAM else 'White'
    palette = f"{PAL_NAME[pal]} on {paper_name}"
    roles = [r for r in ('o', 'a', 'm') if any(rr == r for _, rr in FIG[key]())]
    swatch = list(dict.fromkeys([L[r] for r in roles] + [L['ink'], paper]))
    C[key] = dict(name=name, group=group, reading=reading, palette=palette, L=L, D=D, font=font,
                  typeface=TYPE[font], paper=paper, h=h, yc=yc, swatch=swatch, hh=hh)


# ---------------------------------------------------------------- stacked
concept('T1', 'The stack', 'Stacked',
        "Two outlined triangles, the lower rising into the upper; the overlap filled solid, touching both frames, as in the owner's sketch",
        'red', o='ink', font='inst-b')
concept('T2', 'The shallow stack', 'Stacked',
        'A lighter stroke and a shallow overlap; the filled triangle floats small inside the crossing, parted from both frames by paper',
        'navy', o='navy', word_col='navy', font='frau-sb', paper=CREAM)
concept('T3', 'The keel', 'Stacked',
        "The stacked pair with the filled triangle turned point-down, hung from the upper frame's base into the lower frame",
        'green', o='ink', font='inst-b')
concept('T4', 'The run', 'Stacked (three)',
        'Three outlined triangles in a row, each overlapping the next; the two overlaps filled. A sequence that shares its ground',
        'bronze', o='ink', font='frau-sb', paper=CREAM, h=1.0, yc=0.42)
concept('T5', 'The solid stack', 'Stacked (solid)',
        'The two triangles of the stack drawn solid; only the overlap changes color, parted from the rest by a hairline of paper',
        'oxblood', o='ink', font='frau-sb')
# ---------------------------------------------------------------- tessellated
concept('T6', 'The diamond of eight', 'Tessellated',
        "The owner's tessellated diamond reduced to eight cells, two rows up and two rows down; one cell beside the waist in the accent",
        'blue', o='ink', font='inst-b', h=2.0, yc=0.5)
concept('T7', 'The hexagon of six', 'Tessellated',
        'Six cells meeting at one point, one of them in the accent: the smallest tessellation that closes on itself',
        'oxblood', o='ink', font='inst-b', paper=CREAM, h=1.5, yc=0.45)
concept('T8', 'The triangle of nine', 'Tessellated',
        'Three rows of cells, nine in all; the middle cell of the base row, the cornerstone, in a lighter shade of the same navy',
        'navy', o='navy', word_col='navy', font='frau-sb', tint=('#7F96C4', '#3D5585'))
concept('T9', 'The quarter', 'Tessellated',
        'One triangle subdivided once into four cells; the apex cell in the accent, the three below it in ink',
        'red', o='ink', font='frau-sb', paper=CREAM)
# ---------------------------------------------------------------- cluster
concept('T10', 'The inverted pyramid', 'Cluster',
        "The cluster reduced and turned over: three outlined triangles pointing down form one large downward triangle, with a solid upward triangle at the center",
        'navy', o='navy', word_col='navy', font='inst-b', h=1.5, yc=0.5)
concept('T11', 'The slid triad', 'Cluster (Triforce changed)',
        'Three solid triangles, each slid a fifth of a side along the outer edge in one turning direction, so the hollow center closes and the outline steps; the top one in the accent',
        'bronze', o='ink', font='inst-b', h=1.45)
# ---------------------------------------------------------------- carved
concept('T12', 'The kept core', 'Carved disc',
        "One triangle carved from the disc as a channel, the solid core left standing inside it; the owner's cluster cell (a frame holding a filled triangle) taken down to one",
        'green', word_col='green', font='frau-sb', paper=CREAM, h=1.62, yc=0.42)
concept('T13', 'The carved stack', 'Carved disc',
        "The owner's stacked pair cut through the disc as two channels; the overlap and the centers of both triangles stand as solid islands",
        'navy', word_col='navy', font='inst-b', h=1.62, yc=0.42)
concept('T14', 'The carved quarter', 'Carved disc',
        'A triangle of four cells carved from the disc: the three lower cells cut clean through, the apex cell left standing inside a thin channel',
        'oxblood', word_col='oxblood', font='frau-sb', paper=CREAM, h=1.62, yc=0.42)
concept('T15', 'The nine-pane window', 'Carved square',
        'The triangle of nine cut through a solid square as a window of nine panes, the middle pane of the base row left closed',
        'ink', word_col='ink', font='inst-b', h=1.5, yc=0.45)
# ---------------------------------------------------------------- own derivatives
concept('T16', 'The plinth', 'Own derivative',
        'A solid triangle standing on a broad bar, touching it; the bar wider than the triangle so it reads as a base, the triangle in the accent',
        'red', o='ink', font='frau-sb', paper=CREAM, h=1.3, yc=0.5)
concept('T17', 'The reflection', 'Own derivative',
        'An upward triangle and a downward one sharing one base: the upper solid, the lower an outline hanging from it',
        'blue', o='ink', font='frau-sb', h=2.0, yc=0.5)
concept('T18', 'The carved plinth', 'Own derivative, carved disc',
        'A channel cut rim to rim near the foot of the disc and a triangle rising from it: a dome with a pointed hollow, resting on a low segment',
        'bronze', word_col='ink', font='inst-b', paper=CREAM, h=1.62, yc=0.42)


# ====================================================================== files
def colors(mode, c):
    if mode == 'mono':
        return {k: 'currentColor' for k in ('o', 'a', 'm', 'ink')}
    return c['L'] if mode == 'light' else c['D']


def box(frags):
    bs = [bounds(d) for d, _ in frags]
    return (min(b[0] for b in bs), min(b[1] for b in bs), max(b[2] for b in bs), max(b[3] for b in bs))


def body(frags, col, s=1.0, dx=0.0, dy=0.0):
    return ''.join(P(shift(d, dx, dy, s) if (s != 1 or dx or dy) else d, col[r]) for d, r in frags)


def sq_box(frags, m):
    x0, y0, x1, y1 = box(frags)
    s = max(x1 - x0, y1 - y0) + 2 * m
    return ((x0 + x1) / 2 - s / 2, (y0 + y1) / 2 - s / 2, s, s)


def mark_svg(key, mode, fav=False, label='userandproduct mark'):
    frags = FIG[key](fav)
    return svg(sq_box(frags, 1.5 if fav else 2), body(frags, colors(mode, C[key])), label)


def lockup_svg(key, mode, label='userandproduct'):
    c = C[key]
    col = colors(mode, c)
    frags = FIG[key]()
    cap = caph(c['font'])
    wd, wb = word('userandproduct', c['font'], -10)
    x0, y0, x1, y1 = box(frags)
    H = cap * c['h']
    s = H / (y1 - y0)
    yc = -cap * c['yc']
    dx, dy = -x0 * s, yc - H / 2 - y0 * s
    mw = (x1 - x0) * s
    gap = cap * 0.48
    b = body(frags, col, s, dx, dy) + P(shift(wd, mw + gap, 0), col['ink'])
    top, bot = min(yc - H / 2, wb[1]), max(yc + H / 2, wb[3])
    return svg(fitbox(0, top, mw + gap + wb[2], bot, 4), b, label)


def avatar_svg(key):
    c = C[key]
    frags = FIG[key]()
    carved = any(r == 'm' for _, r in frags)
    x0, y0, x1, y1 = box(frags)
    if carved:      # the disc or square fills the avatar
        s, fill = 100 / max(x1 - x0, y1 - y0), 100
    else:
        s, fill = 60 / max(x1 - x0, y1 - y0), 60
    dx = 50 - (x0 + x1) / 2 * s
    dy = 50 - (y0 + y1) / 2 * s
    b = P(rect(0, 0, 100, 100), c['paper']) + body(frags, c['L'], s, dx, dy)
    return svg((0, 0, 100, 100), b, 'userandproduct avatar')


def render_png(svg_text, path, size):
    data = bytes(resvg_py.svg_to_bytes(svg_string=svg_text, width=size, height=size))
    with open(path, 'wb') as f:
        f.write(data)


def build(keys):
    for k in keys:
        m = k.lower()
        for mode in ('light', 'dark', 'mono'):
            sfx = '' if mode == 'light' else '-' + mode
            write(f'{m}-lockup{sfx}.svg', lockup_svg(k, mode))
            write(f'{m}-mark{sfx}.svg', mark_svg(k, mode))
        fav = mark_svg(k, 'light', True, 'userandproduct')
        write(f'{m}-favicon.svg', fav)
        for sz in (16, 32):
            render_png(fav, os.path.join(OUT, f'{m}-favicon-{sz}.png'), sz)
        av = avatar_svg(k)
        write(f'{m}-avatar.svg', av)
        render_avatar(av, os.path.join(OUT, f'{m}-avatar-400.png'))


if __name__ == '__main__':
    keys = [a.upper() for a in sys.argv[1:]] or list(C)
    build(keys)
    import board7
    board7.write(C, OUT)
    print('built', ', '.join(keys))
