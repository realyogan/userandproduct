"""Build the round-seven four-tile logo concepts (S1 onward) and the review board.

Brief: the owner's sketch of four rounded rectangles turning around a center, as filled tiles, as
outlines, and as negative space carved out of a disc (or a square), beside a settled lowercase
wordmark in Instrument Sans or Fraunces.

Run from this folder:
    python build_tiles.py            # all SVGs, PNG renders and index.html
    python build_tiles.py S3 S9      # only those concepts (index is rebuilt too)
    python build_tiles.py --sheet    # contact sheet of all marks at 160, 32 and 16px (scratch check)

Geometry. Every concept starts from one layout, the pinwheel tiling: four L x S tiles around a center,
each turned 90 degrees from the last, so the outer edge is a square of side L + S and the center hole
is L - S wide (with square tiles it collapses to a 2 x 2 grid). Each tile is shrunk by the gap, given a
corner radius, optionally spun about its own center, and the whole layout is turned by a global angle.
Outlines are real rings (tile minus inset tile). Carved marks are a disc or square minus the tiles
(skia-pathops DIFFERENCE): one compound path, nothing white painted on top.

Files per concept s<N>, in the parent folder:
  s<N>-lockup.svg, -lockup-dark.svg, -lockup-mono.svg
  s<N>-mark.svg,   -mark-dark.svg,   -mark-mono.svg
  s<N>-favicon.svg (heavier gaps and strokes for 16px) with s<N>-favicon-16.png and -32.png
  s<N>-avatar.svg with s<N>-avatar-400.png
"""
import io
import math
import os
import sys

import pathops

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from geom7 import (OUT, P, caph, circle, fitbox, from_path, minus, rect, render_avatar, resvg_py,  # noqa: E402
                   shift, svg, to_path, union, word, write, bounds, Image, fmt)

WORD_DARK = '#EEE9DF'
NEAR = '#141414'
CREAM = '#F4EFE3'
WHITE = '#FFFFFF'

# ---------------------------------------------------------------------- palettes (light, dark lift)
PAL = {
    'blue': ('Blue, Black and White', '#1F3FBF', '#8EA2FF'),
    'navy': ('Deep Navy', '#14284B', '#9DB4E6'),
    'green': ('Deep Green', '#1D4636', '#9CC9B0'),
    'oxblood': ('Oxblood', '#6B1E2A', '#E5A0A8'),
    'red': ('Press Red', '#B3141C', '#F0676C'),
    'bronze': ('Bronze', '#8A6424', '#D6B272'),
    'ink': ('Ink', '#141414', '#F1EEE7'),
}


# ---------------------------------------------------------------------- tile geometry
def rot(x, y, a):
    c, s = math.cos(math.radians(a)), math.sin(math.radians(a))
    return x * c - y * s, x * s + y * c


def rrect(cx, cy, w, h, r, ang=0.0):
    """A rounded rectangle centerd on (cx, cy), turned by ang degrees, as a closed path."""
    r = max(0.0, min(r, w / 2, h / 2))
    k = 0.5523 * r
    a, b = w / 2, h / 2
    if r < 0.01:
        pts = [(-a, -b), (a, -b), (a, b), (-a, b)]
        q = [rot(x, y, ang) for x, y in pts]
        return 'M' + 'L'.join(f'{fmt(x + cx)} {fmt(y + cy)}' for x, y in q) + 'Z'
    # four sides, each followed by a cubic corner
    seq = [('M', [(-a + r, -b)]), ('L', [(a - r, -b)]), ('C', [(a - r + k, -b), (a, -b + r - k), (a, -b + r)]),
           ('L', [(a, b - r)]), ('C', [(a, b - r + k), (a - r + k, b), (a - r, b)]),
           ('L', [(-a + r, b)]), ('C', [(-a + r - k, b), (-a, b - r + k), (-a, b - r)]),
           ('L', [(-a, -b + r)]), ('C', [(-a, -b + r - k), (-a + r - k, -b), (-a + r, -b)])]
    out = []
    for cmd, pts in seq:
        q = [rot(x, y, ang) for x, y in pts]
        out.append(cmd + ' '.join(f'{fmt(x + cx)} {fmt(y + cy)}' for x, y in q))
    return ''.join(out) + 'Z'


def tile_d(t, inset=0.0):
    return rrect(t['cx'], t['cy'], t['w'] - 2 * inset, t['h'] - 2 * inset, max(t['r'] - inset, 0), t['ang'])


def ring_d(t, sw):
    return minus(tile_d(t), tile_d(t, sw))


def pinwheel(L=4, S=3, gap=0.5, rf=0.2, G=0.0, spin=0.0, spread=1.0, sizes=None, push=None):
    """Four tiles of the pinwheel tiling in raw units, centerd on (0, 0).
    rf: corner radius as a fraction of the short side. spread: scales the centers apart (room for
    spin). sizes: per-tile scale factors. push: per-tile outward shift in raw units."""
    tiles = []
    for i in range(4):
        x, y = rot(-S / 2, -L / 2, 90 * i)
        x, y = x * spread, y * spread
        if push and push[i]:
            n = math.hypot(x, y) or 1
            x, y = x + x / n * push[i], y + y / n * push[i]
        k = sizes[i] if sizes else 1.0
        w, h = (L - gap) * k, (S - gap) * k
        x, y = rot(x, y, G)
        tiles.append({'cx': x, 'cy': y, 'w': w, 'h': h, 'r': rf * min(w, h), 'ang': 90 * i + G + spin})
    return tiles


def corners(t):
    """The four corner-arc centers of a tile and its radius (the farthest points are r beyond them)."""
    a, b = t['w'] / 2 - t['r'], t['h'] / 2 - t['r']
    return [(t['cx'] + rot(x, y, t['ang'])[0], t['cy'] + rot(x, y, t['ang'])[1])
            for x, y in ((a, b), (-a, b), (a, -b), (-a, -b))], t['r']


def extent_box(tiles):
    xs, ys = [], []
    for t in tiles:
        b = bounds(tile_d(t))
        xs += [b[0], b[2]]
        ys += [b[1], b[3]]
    return min(xs), min(ys), max(xs), max(ys)


def extent_radius(tiles, cx=0.0, cy=0.0):
    m = 0.0
    for t in tiles:
        cs, r = corners(t)
        m = max(m, max(math.hypot(x - cx, y - cy) for x, y in cs) + r)
    return m


def place(tiles, s, dx, dy):
    return [dict(t, cx=t['cx'] * s + dx, cy=t['cy'] * s + dy, w=t['w'] * s, h=t['h'] * s, r=t['r'] * s) for t in tiles]


def fit_box(tiles, size=100.0):
    """Scale and center so the tiles' bounding box fits a size x size square centerd on (50, 50)."""
    x0, y0, x1, y1 = extent_box(tiles)
    s = size / max(x1 - x0, y1 - y0)
    return place(tiles, s, 50 - (x0 + x1) / 2 * s, 50 - (y0 + y1) / 2 * s)


def fit_radius(tiles, radius):
    """Scale about the layout center so the farthest tile point sits at radius; center on (50, 50)."""
    s = radius / extent_radius(tiles)
    return place(tiles, s, 50, 50)


def check_gaps(tiles):
    """Raise if any two tiles overlap (the gap must stay open)."""
    ps = [to_path(tile_d(t)) for t in tiles]
    for i in range(4):
        for j in range(i + 1, 4):
            if abs(pathops.op(ps[i], ps[j], pathops.PathOp.INTERSECTION).area) > 1e-3:
                raise ValueError(f'tiles {i} and {j} overlap')


DISC = circle(50, 50, 50)


# ---------------------------------------------------------------------- treatments
def filled(tiles, roles=None):
    check_gaps(tiles)
    roles = roles or ['m'] * 4
    out = {}
    for t, r in zip(tiles, roles):
        out.setdefault(r, []).append(tile_d(t))
    return [(union(*ds), r) for r, ds in out.items()]


def outlined(tiles, sw, roles=None, weights=None):
    check_gaps(tiles)
    roles = roles or ['m'] * 4
    weights = weights or [sw] * 4
    out = {}
    for t, r, w in zip(tiles, roles, weights):
        out.setdefault(r, []).append(ring_d(t, w))
    return [(union(*ds), r) for r, ds in out.items()]


def carved(tiles, base=DISC, keep=None):
    """base minus every tile; keep: index of a tile left standing in the accent (flush, role 'a')."""
    check_gaps(tiles)
    holes = [tile_d(t) for t in tiles]
    parts = [(minus(base, *holes), 'm')]
    if keep is not None:
        parts.append((from_path(pathops.op(to_path(holes[keep]), to_path(base), pathops.PathOp.INTERSECTION)), 'a'))
    return parts


# ---------------------------------------------------------------------- concepts
# Each returns [(d, role)] in a 100 x 100 box. fav=True: the heavier 16px drawing.
def s1(fav=False):
    """Pinwheel: 7:5 tiles in the pinwheel tiling, turned 18 degrees, soft corners."""
    g = 0.85 if fav else 0.62
    return filled(fit_box(pinwheel(7, 5, g, 0.24, 18, 0)))


def s2(fav=False):
    """The sketch: 7:5 tiles in the pinwheel tiling, turned 40 degrees, a slight hand spin."""
    g = 0.85 if fav else 0.62
    return filled(fit_box(pinwheel(7, 5, g, 0.24, 40, 4, spread=1.03)))


def s3(fav=False):
    """Square-on: 3:4 tiles in the pinwheel tiling, sharp corners, no turn."""
    g = 0.6 if fav else 0.42
    return filled(fit_box(pinwheel(4, 3, g, 0.0, 0, 0)))


def s4(fav=False):
    """The open frame: four 1:2 tiles on the sides of a square, turned 15 degrees, soft corners, the
    center left empty and the corners open. Mirror symmetric, so it never turns."""
    L, S = 2.0, 1.0
    g = 0.36 if fav else 0.26
    tiles = []
    for i in range(4):
        x, y = rot(0, -(L / 2), 90 * i + 15)
        tiles.append({'cx': x, 'cy': y, 'w': L - 0.8 - g, 'h': S * 0.8, 'r': 0.22, 'ang': 90 * i + 15})
    return filled(fit_box(tiles))


def s5(fav=False):
    """Two sizes: the diagonal pair large, the other pair small, spun 12 degrees on a diamond grid."""
    g = 0.5 if fav else 0.38
    return filled(fit_box(pinwheel(3, 3, g, 0.18, 45, 12, spread=1.12, sizes=[1, 0.72, 1, 0.72])))


def s6(fav=False):
    """One tile in the accent: S2's layout, the top tile in press red."""
    g = 0.85 if fav else 0.62
    return filled(fit_box(pinwheel(7, 5, g, 0.24, 40, 4, spread=1.03)), roles=['a', 'm', 'm', 'm'])


def s7(fav=False):
    """Outlined pinwheel: S2's tiles drawn as rings of one heavy weight."""
    g = 1.05 if fav else 0.8
    return outlined(fit_box(pinwheel(7, 5, g, 0.3, 40, 4, spread=1.03)), 12 if fav else 9.5)


def s8(fav=False):
    """Outlined diamonds: square tiles at 45 degrees, rounded, heavy rings."""
    g = 0.7 if fav else 0.55
    return outlined(fit_box(pinwheel(3, 3, g, 0.26, 45, 0, spread=1.0)), (12.5 if fav else 9))


def s9(fav=False):
    """Mixed weights: S1's spun squares, the diagonal pair heavy, the other pair light."""
    g = 0.62 if fav else 0.5
    ts = fit_box(pinwheel(3, 3, g, 0.24, 45, 15, spread=1.16))
    return outlined(ts, 9, weights=[12.5, 8, 12.5, 8] if fav else [11, 5, 11, 5])


def s10(fav=False):
    """Carved disc, tiles floating: S1's spun squares cut from the disc."""
    g = 0.62 if fav else 0.5
    return carved(fit_radius(pinwheel(3, 3, g, 0.2, 45, 15, spread=1.16), 38 if fav else 37))


def s11(fav=False):
    """Inlaid disc: only the outlines of the four tiles are cut, so the tiles stay standing as solid
    islands inside the disc, like tiles set into a round floor."""
    if fav:  # at 16px the inlay lines close up, so the favicon cuts the tiles clean through
        return carved(fit_radius(pinwheel(7, 5, 0.85, 0.24, 40, 4, spread=1.03), 38))
    ts = fit_radius(pinwheel(7, 5, 1.0, 0.26, 40, 4, spread=1.03), 39)
    check_gaps(ts)
    sw = 3.6
    return [(minus(DISC, *[ring_d(t, sw) for t in ts]), 'm')]


def s12(fav=False):
    """Carved disc, one tile breaks the rim: the lower tile pushed out through the edge."""
    g = 0.85 if fav else 0.62
    base = pinwheel(7, 5, g, 0.24, 40, 4, spread=1.03)
    s = 38 / extent_radius(base)
    return carved(place(pinwheel(7, 5, g, 0.24, 40, 4, spread=1.03, push=[0, 0, 2.2, 0]), s, 50, 50))


def s13(fav=False):
    """Carved square: a soft square block with S2's turned pinwheel cut out of it."""
    g = 0.85 if fav else 0.62
    block = rrect(50, 50, 100, 100, 16)
    return carved(fit_radius(pinwheel(7, 5, g, 0.24, 40, 4, spread=1.03), 41 if fav else 40), block)


def s14(fav=False):
    """Three cut, the fourth kept: the disc with three tiles cut and the fourth standing in the accent."""
    g = 0.85 if fav else 0.62
    return carved(fit_radius(pinwheel(7, 5, g, 0.24, 40, 4, spread=1.03), 38), keep=0)


def s15(fav=False):
    """Four pages fanned: four 3:4 sheets pivoting on one lower corner, 14 degrees apart, each
    separated from the next by a cut line, like a swatch book opened."""
    ang = [0, -14, -28, -42]
    w, h, r = 44, 60, 4.5
    gap = 4.6 if fav else 3.4
    px, py = 20, 92
    def sheet(a, grow=0.0):
        cx, cy = rot(w / 2 - r, -h / 2 + r, a)
        return rrect(px + cx, py + cy, w + 2 * grow, h + 2 * grow, r + grow, a)
    out = []
    for i, a in enumerate(ang):
        d = sheet(a)
        for b in ang[i + 1:]:
            d = minus(d, sheet(b, gap))
        out.append(d)
    d = union(*out)
    x0, y0, x1, y1 = bounds(d)
    s = 100 / max(x1 - x0, y1 - y0)
    return [(shift(d, 50 - (x0 + x1) / 2 * s, 50 - (y0 + y1) / 2 * s, s), 'm')]


def s16(fav=False):
    """Two tiles only: two neighboring tiles of the pinwheel, one filled, one outlined."""
    g = 0.85 if fav else 0.62
    ts = pinwheel(7, 5, g, 0.24, 40, 4, spread=1.03)
    ts = fit_box([ts[0], ts[1]])
    return [(tile_d(ts[1]), 'm'), (ring_d(ts[0], 13 if fav else 10), 'm')]


def s17(fav=False):
    """The empty seat: three filled tiles and the fourth an outline."""
    g = 0.85 if fav else 0.62
    ts = fit_box(pinwheel(7, 5, g, 0.24, 40, 4, spread=1.03))
    check_gaps(ts)
    solid = union(*[tile_d(t) for t in ts[1:]])
    return [(union(solid, ring_d(ts[0], 10 if fav else 7.5)), 'm')]


def s18(fav=False):
    """Carved disc, square-on: S3's sharp 3:4 pinwheel cut from the disc, small and floating."""
    g = 0.8 if fav else 0.66
    return carved(fit_radius(pinwheel(4, 3, g, 0.06, 0, 0), 35))


FIG = {f'S{i}': fn for i, fn in enumerate([s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14,
                                             s15, s16, s17, s18], 1)}


# ---------------------------------------------------------------------- dropped drafts (shown on the board)
def _cards():
    ang = [-27, -9, 9, 27]
    out = []
    for a in ang:
        cx, cy = rot(0, -39, a)
        out.append(rrect(50 + cx, 98 + cy, 46, 62, 5, a))
    res = []
    for i, d in enumerate(out):
        for j in range(i + 1, 4):
            cx, cy = rot(0, -39, ang[j])
            d = minus(d, rrect(50 + cx, 98 + cy, 52.4, 68.4, 8.2, ang[j]))
        res.append(d)
    d = union(*res)
    x0, y0, x1, y1 = bounds(d)
    s = 100 / max(x1 - x0, y1 - y0)
    return [(shift(d, 50 - (x0 + x1) / 2 * s, 50 - (y0 + y1) / 2 * s, s), 'm')]


DROPPED = [
    ('Plain grid, square-on', 'Four equal squares on a straight grid, sharp or rounded: Microsoft, the Windows 11 flag and every app-grid icon. One change at most.',
     lambda: filled(fit_box(pinwheel(3, 3, 0.3, 0.18, 0, 0)))),
    ('Grid turned 45 degrees', 'The same grid turned on its point: Microsoft turned, and one step from Binance and the Dropbox diamonds.',
     lambda: filled(fit_box(pinwheel(3, 3, 0.3, 0.0, 45, 0)))),
    ('Squares spun in place', 'Four squares square-on, each spun 18 degrees (first S1): at 16px it still read as Microsoft.',
     lambda: filled(fit_box(pinwheel(3, 3, 0.36, 0.24, 0, 18, spread=1.3)))),
    ('1:2 pills round a hole', 'Long tiles in the pinwheel leave a square hole the width of a tile: the Chase octagon, and it spun like a windmill at small sizes.',
     lambda: filled(fit_box(pinwheel(4, 2, 0.55, 0.5, 20, 0)))),
    ('Tiles through the rim', 'All four tiles cut out through the edge of the disc (nine sizes tried): the solid left between them is a hooked cross. Discarded outright.',
     lambda: carved(fit_radius(pinwheel(7, 5, 2.0, 0.24, 40, 4, spread=1.03), 52))),
    ('Tiles filling the disc', 'Large floating cuts leave a thin ring and a thin cross: a sun cross. Every carved disc now keeps its tiles inside 39 percent of the radius.',
     lambda: carved(fit_radius(pinwheel(4, 3, 0.4, 0.06, 0, 0), 45))),
    ('A hand of cards', 'Four sheets fanned from the bottom center (first S15): a poker hand, the wrong register. Now fanned from one corner like a swatch book.',
     _cards),
]


def parts(key, fav=False):
    return FIG[key](fav)


# ---------------------------------------------------------------------- sheet (scratch check)
def mark_plain(key, fav=False):
    col = {'m': '#141414', 'a': '#B3141C', 't': '#999999'}
    return svg((-1, -1, 102, 102), ''.join(P(d, col[r]) for d, r in parts(key, fav)), 'mark')


def sheet(path, keys):
    W, rowh = 4 * 230, 200
    rows = (len(keys) + 3) // 4
    img = Image.new('RGB', (W, rowh * rows), 'white')
    from PIL import ImageDraw
    dr = ImageDraw.Draw(img)
    for i, k in enumerate(keys):
        x0, y = (i % 4) * 230 + 10, (i // 4) * rowh + 10
        big = Image.open(io.BytesIO(bytes(resvg_py.svg_to_bytes(svg_string=mark_plain(k), width=140, height=140)))).convert('RGBA')
        img.paste(big, (x0, y), big)
        fav = mark_plain(k, True)
        for j, sz in enumerate((32, 16)):
            t = Image.open(io.BytesIO(bytes(resvg_py.svg_to_bytes(svg_string=fav, width=sz, height=sz)))).convert('RGBA')
            img.paste(t, (x0 + 150, y + j * 40), t)
        t16 = Image.open(io.BytesIO(bytes(resvg_py.svg_to_bytes(svg_string=fav, width=16, height=16)))).convert('RGBA')
        z = t16.resize((48, 48), Image.NEAREST)
        img.paste(z, (x0 + 150, y + 85), z)
        dr.text((x0, y + 150), k, fill='black')
    img.save(path)


if __name__ == '__main__':
    args = sys.argv[1:]
    if args and args[0] == '--sheet':
        keys = [a.upper() for a in args[2:]] or list(FIG)
        sheet(args[1], keys)
        sys.exit(0)
    import files7
    keys = [a.upper() for a in args] or list(FIG)
    files7.build(keys)
    import board7
    board7.write(files7.C, OUT)
    print('built', ', '.join(keys))
