"""Figures for the round-seven triangles family (T1 to T18).

Every figure is drawn in a 100 x 100 box and returns a list of (d, role) fragments:
  'o' structure (outlines, cells, solid shapes) in the owned color or ink,
  'a' the accent (the filled overlap, the one marked cell),
  'm' a carved solid (disc or square) in the owned color.
fav=True returns the heavier 16px drawing (thicker strokes, wider gaps).
All cuts are real booleans (skia-pathops), so every fragment is one compound path.
"""
import math

from geom7 import bounds, circle, fmt, minus, rect, union, to_path, from_path
import pathops

SQ3 = math.sqrt(3)
DISC = circle(50, 50, 50)
SQUARE = rect(0, 0, 100, 100)


def poly(pts):
    return 'M' + 'L'.join(f'{fmt(x)} {fmt(y)}' for x, y in pts) + 'Z'


def inter(a, b):
    return from_path(pathops.op(to_path(a), to_path(b), pathops.PathOp.INTERSECTION))


def tri_up(cx, top, base, t=0.0):
    """Equilateral triangle, apex up at y=top, base at y=base; inset every edge by t."""
    top, base = top + 2 * t, base - t
    hw = (base - top) / SQ3
    return poly([(cx, top), (cx + hw, base), (cx - hw, base)])


def tri_dn(cx, top, bottom, t=0.0):
    """Equilateral triangle, flat edge at y=top, apex down at y=bottom; inset every edge by t."""
    top, bottom = top + t, bottom - 2 * t
    hw = (bottom - top) / SQ3
    return poly([(cx - hw, top), (cx + hw, top), (cx, bottom)])


def outline_up(cx, top, base, w):
    return minus(tri_up(cx, top, base), tri_up(cx, top, base, w))


def outline_dn(cx, top, bottom, w):
    return minus(tri_dn(cx, top, bottom), tri_dn(cx, top, bottom, w))


def inset_region(d, t, up=True):
    """Shrink an equilateral triangular region (given as a path) by t on every edge."""
    x0, y0, x1, y1 = bounds(d)
    return (tri_up if up else tri_dn)((x0 + x1) / 2, y0, y1, t)


def cells_tri(n, cx, top, s, t, down=False):
    """A triangle of side n*s cut into n*n cells, each inset by t. Returns [(row, k, d)]."""
    h = s * SQ3 / 2
    out = []
    for r in range(n):
        for k in range(2 * r + 1):
            x = cx + (k - r) * s / 2
            up = (k % 2 == 0) != down
            if not down:
                y = top + r * h
            else:
                y = top + (n - 1 - r) * h
            out.append((r, k, (tri_up if up else tri_dn)(x, y, y + h, t)))
    return out


# ============================================================== stacked
def t1(fav=False):
    """The stack: two outlined triangles, the lower rising into the upper; the overlap filled solid in
    the accent, touching both frames, as in the owner's sketch."""
    w = 8.5 if fav else 5.8
    s_h = 64          # each triangle's height
    top1, top2 = 2, 22
    up1 = outline_up(50, top1, top1 + s_h, w)
    up2 = outline_up(50, top2, top2 + s_h, w)
    fill = inter(tri_up(50, top2, top2 + s_h, w), tri_up(50, top1, top1 + s_h, w))
    return [(union(up1, up2), 'o'), (fill, 'a')]


def t2(fav=False):
    """The shallow stack: a lighter stroke and a shallow overlap; the filled triangle floats inside the
    small overlap, parted from both frames by a gap of paper."""
    w, g = (7.5, 2.6) if fav else (4.2, 2.2)
    s_h = 62
    top1, top2 = 2, 32
    a = outline_up(50, top1, top1 + s_h, w)
    b = outline_up(50, top2, top2 + s_h, w)
    inner = inter(tri_up(50, top1, top1 + s_h, w), tri_up(50, top2, top2 + s_h, w))
    return [(union(a, b), 'o'), (inset_region(inner, g), 'a')]


def t3(fav=False):
    """The keel: the stacked pair, and the filled triangle turned to point down, hung from the upper
    frame's base into the lower frame, like a keel under a hull."""
    w, g = (8.5, 3.0) if fav else (5.8, 2.4)
    s_h = 62
    top1, top2 = 2, 26
    a = outline_up(50, top1, top1 + s_h, w)
    b = outline_up(50, top2, top2 + s_h, w)
    yb = top1 + s_h            # bottom edge of the upper frame's base
    x0, _, x1, _ = bounds(inter(tri_up(50, top2, top2 + s_h, w), rect(0, yb, 100, yb + 0.01)))
    hgt = (x1 - x0) * SQ3 / 2
    fill = tri_dn(50, yb, yb + hgt, g)
    return [(union(a, b), 'o'), (fill, 'a')]

def t4(fav=False):
    """The run: three outlined triangles in a row, each overlapping the next; the two overlaps filled
    solid. Read left to right, like a sequence of steps that share ground."""
    w = 7 if fav else 4.6
    h = 46
    hw = h / SQ3
    dx = hw * 0.78
    xs = [50 - dx, 50, 50 + dx]
    top, base = 50 - h / 2, 50 + h / 2
    outs = union(*[outline_up(x, top, base, w) for x in xs])
    fills = [inter(tri_up(x1, top, base, w), tri_up(x2, top, base, w))
             for x1, x2 in ((xs[0], xs[1]), (xs[1], xs[2]))]
    return [(outs, 'o'), (union(*fills), 'a')]


def t5(fav=False):
    """The solid stack: the same two triangles as T1 drawn solid; only the overlap changes color,
    parted from the rest by a hairline of paper."""
    g = 4.5 if fav else 3.2
    s_h = 60
    top1, top2 = 4, 36
    A, B = tri_up(50, top1, top1 + s_h), tri_up(50, top2, top2 + s_h)
    over = inter(A, B)
    grown = inset_region(over, -g)
    return [(minus(union(A, B), grown), 'o'), (over, 'a')]


# ============================================================== tessellated
def t6(fav=False):
    """The diamond of eight: the owner's tessellated diamond reduced to two rows up and two rows down,
    eight cells; one cell, right of the waist, in the accent."""
    g = 3.6 if fav else 2.4
    s = 27
    h = s * SQ3 / 2
    top = 50 - 2 * h
    cells = [d for _, _, d in cells_tri(2, 50, top, s, g / 2)]
    cells += [d for _, _, d in cells_tri(2, 50, top + 2 * h, s, g / 2, down=True)]
    acc_i = 7  # bottom half, first row, right-hand down cell
    acc = cells[acc_i]
    rest = [d for i, d in enumerate(cells) if i != acc_i]
    return [(union(*rest), 'o'), (acc, 'a')]


def t7(fav=False):
    """The hexagon of six: six cells around a point, one in the accent."""
    g = 4.2 if fav else 2.8
    s = 46
    h = s * SQ3 / 2
    cx, cy = 50, 50
    t = g / 2
    cells = [tri_up(cx - s / 2, cy - h, cy, t), tri_dn(cx, cy - h, cy, t), tri_up(cx + s / 2, cy - h, cy, t),
             tri_dn(cx - s / 2, cy, cy + h, t), tri_up(cx, cy, cy + h, t), tri_dn(cx + s / 2, cy, cy + h, t)]
    acc = cells[2]
    return [(union(*[c for i, c in enumerate(cells) if i != 2]), 'o'), (acc, 'a')]


def t8(fav=False):
    """The triangle of nine: three rows of cells, the middle cell of the base row in the accent,
    the cornerstone."""
    g = 4.0 if fav else 2.6
    s = 33
    h = s * SQ3 / 2
    top = 50 - 1.5 * h + 2
    cells = cells_tri(3, 50, top, s, g / 2)
    acc = [d for r, k, d in cells if r == 2 and k == 2][0]
    rest = [d for r, k, d in cells if not (r == 2 and k == 2)]
    return [(union(*rest), 'o'), (acc, 'a')]


def t9(fav=False):
    """The quarter: one triangle subdivided once into four cells; the apex cell in the accent."""
    g = 5.2 if fav else 3.6
    s = 50
    h = s * SQ3 / 2
    top = 50 - h + 4
    cells = cells_tri(2, 50, top, s, g / 2)
    acc = [d for r, k, d in cells if r == 0][0]
    rest = [d for r, k, d in cells if r != 0]
    return [(union(*rest), 'o'), (acc, 'a')]


# ============================================================== cluster
def t10(fav=False):
    """The inverted pyramid: the cluster reduced to three outlined triangles pointing down, arranged
    as one large downward triangle, with a solid upward triangle in the middle. The news writer's
    structure: most important first, narrowing to detail."""
    w, g = (6.4, 4.8) if fav else (4.8, 3.6)
    s = 48
    h = s * SQ3 / 2
    top = 50 - h
    cells = cells_tri(2, 50, top, s, g / 2, down=True)
    outs, solid = [], None
    for r, k, d in cells:
        if r == 1 and k == 1:   # the center cell, which points up in a downward triangle
            solid = d
        else:
            x0, y0, x1, y1 = bounds(d)
            outs.append(outline_dn((x0 + x1) / 2, y0, y1, w))
    return [(union(*outs), 'o'), (solid, 'a')]


def t11(fav=False):
    """The slid triad: three solid triangles, each slid along the outer edge by a fifth of a side in
    the same turning direction, so the hollow center closes into a small turned triangle and the
    outline steps. Two cells ink, one accent."""
    g = 4.2 if fav else 3.0
    s = 44
    h = s * SQ3 / 2
    top = 50 - h + 2
    tt = s * 0.2
    c = cells_tri(2, 50, top, s, g / 2)
    cell = {(r, k): d for r, k, d in c}
    from geom7 import shift
    top_c = shift(cell[(0, 0)], tt * 0.5, tt * SQ3 / 2)
    br = shift(cell[(1, 2)], -tt, 0)
    bl = shift(cell[(1, 0)], tt * 0.5, -tt * SQ3 / 2)
    # recenter
    allb = [bounds(x) for x in (top_c, br, bl)]
    x0 = min(b[0] for b in allb); x1 = max(b[2] for b in allb)
    y0 = min(b[1] for b in allb); y1 = max(b[3] for b in allb)
    dx, dy = 50 - (x0 + x1) / 2, 50 - (y0 + y1) / 2
    top_c, br, bl = (shift(x, dx, dy) for x in (top_c, br, bl))
    return [(union(bl, br), 'o'), (top_c, 'a')]


# ============================================================== carved
def t12(fav=False):
    """The kept core: one triangle carved from the disc, with a smaller solid triangle left standing in
    the middle of the hole, so the cut reads as a frame. Reduced from the owner's cluster image (an
    outlined triangle holding a small filled one), taken down to a single cell."""
    h = 58 if fav else 56
    cy = 56
    top, base = cy - 2 * h / 3, cy + h / 3
    w = 9 if fav else 7.5          # width of the channel
    hole = minus(tri_up(50, top, base), tri_up(50, top, base, w))
    return [(minus(DISC, hole), 'm')]

def t13(fav=False):
    """The stacked pair carved: the two frames of T1 cut as channels through the disc; the overlap
    and the triangle centers stand as solid islands."""
    w = 8 if fav else 5.6
    s_h = 46
    top1, top2 = 16, 40
    a = outline_up(50, top1, top1 + s_h, w)
    b = outline_up(50, top2, top2 + s_h, w)
    return [(minus(DISC, union(a, b)), 'm')]


def t14(fav=False):
    """The subdivided triangle carved: four cells, three cut clean through, the apex cell left
    standing as an island ringed by a thin channel."""
    g = 6 if fav else 4.6
    w = 4.4 if fav else 3.2
    s = 34
    h = s * SQ3 / 2
    top = 51 - h
    cells = cells_tri(2, 50, top, s, g / 2)
    holes = []
    for r, k, d in cells:
        if r == 0:
            x0, y0, x1, y1 = bounds(d)
            holes.append(outline_up((x0 + x1) / 2, y0, y1, w))
        else:
            holes.append(d)
    return [(minus(DISC, union(*holes)), 'm')]


def t15(fav=False):
    """Carved from a square: the triangle of nine cut through a solid square as a window of nine panes,
    with one pane, the middle of the base row, left closed."""
    g = 6.4 if fav else 4.4
    s = 27 if fav else 26
    h = s * SQ3 / 2
    top = 50 - 1.5 * h + 2
    holes = [d for r, k, d in cells_tri(3, 50, top, s, g / 2) if not (r == 2 and k == 2)]
    return [(minus(SQUARE, *holes), 'm')]

def t16(fav=False):
    """The plinth: a solid triangle standing on a broad bar, the bar wider than the triangle so it
    reads as a base, not an eject key; the triangle in the accent, the bar in ink, touching."""
    h = 54
    bar_h = 15 if fav else 12
    base = 70
    tri = tri_up(50, base - h, base)
    bar = rect(4, base, 96, base + bar_h)
    return [(bar, 'o'), (tri, 'a')]


def t17(fav=False):
    """The reflection: an upward triangle and a downward one sharing one base, touching. The upper is
    solid, the lower an outline hanging from it: the made thing standing on its reflection."""
    w = 9 if fav else 6.5
    h = 46
    up = tri_up(50, 50 - h, 50)
    dn = outline_dn(50, 50, 50 + h, w)
    return [(dn, 'o'), (up, 'a')]


def t18(fav=False):
    """The plinth, carved: a disc with a channel cut rim to rim and a triangle rising from it, so the
    disc becomes a dome with a pointed hollow resting on a low segment."""
    w = 9 if fav else 7
    base = 70
    h = 44 if fav else 42
    tri = tri_up(50, base - h, base)
    chan = rect(-5, base, 105, base + w)
    return [(minus(DISC, tri, chan), 'm')]


FIG = {f'T{i}': fn for i, fn in enumerate([t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14,
                                            t15, t16, t17, t18], 1)}
