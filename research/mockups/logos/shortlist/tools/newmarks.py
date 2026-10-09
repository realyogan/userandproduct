"""Geometry for the two new marks on the shortlist.

NEW1, the profile: a solid disc with a head in profile (facing right) cut out as negative space.
NEW2, the sphere: T8's triangle of nine minus its two bottom corner cells, the seven left cut out of a
solid disc, the base cells fused with the inner lower edge of the disc.
Every figure is drawn in a 100 x 100 box, disc centered at (50, 50), radius 50. Each function returns
the disc as one compound path (circle minus figure, skia-pathops DIFFERENCE). fav=True gives the
heavier 16px drawing.
"""
import math

import pathops
from geom import circle, fmt, minus, rect, to_path, from_path, union

SQ3 = math.sqrt(3)
DISC = circle(50, 50, 50)


def poly(pts):
    return 'M' + 'L'.join(f'{fmt(x)} {fmt(y)}' for x, y in pts) + 'Z'


def inter(a, b):
    return from_path(pathops.op(to_path(a), to_path(b), pathops.PathOp.INTERSECTION))


# ====================================================================== NEW1 the profile
# Profile points run clockwise from the crown: forehead, brow, nose, lips, chin, neck front,
# the neck line (the cameo's truncation), nape, back of the skull.

# The face, crown to neck, in head units (crown at y 0, chin at y 52); x grows toward the face.
FACE_FULL = [(10, 0.5), (19, 19), (17.5, 22.5), (27, 34), (18.5, 36.5), (20, 41), (17.5, 42.5),
             (19, 45.5), (15.5, 47.5), (18, 52.5), (8, 55.5), (10, 66)]
FACE_FAV = [(10, 0), (20, 18), (18.5, 21), (31, 34), (19.5, 37.5), (20.5, 46), (17, 48),
            (19, 54), (8, 57.5), (10, 68)]
FACE_MIN = [(11, 1), (27, 34), (18.5, 36.5), (19, 47), (17, 48.5), (18, 52.5), (8, 55.5), (10, 66)]
FACE_MIN_FAV = [(11, 0.5), (31, 35), (19.5, 38.5), (20, 50), (17, 52), (19, 55), (8, 58), (10, 68)]
SKULL_POLY = [(-11, 70), (-12, 48), (-22, 38), (-25, 21), (-19, 7), (-7, 0.5)]
NECK_LINE = 4.5   # the neck line drops this much from back to front (a slanted cameo cut)


def place(pts, x0, y0, k):
    return [(x0 + x * k, y0 + y * k) for x, y in pts]


def head(face, skull, x0, y0, k):
    """Face points, then the neck line (front lower than back), then the skull, all scaled by k."""
    f = place(face, x0, y0, k)
    back = place(skull, x0, y0, k)
    fx, fy = f[-1]
    bx, by = back[0]
    # neck line: from the neck front straight back to the nape column, sloping up
    return f + [(bx, fy - NECK_LINE * k)] + back[1:]


def head_a(fav=False):
    """More angular: the face in eleven short straight cuts (forehead, brow, nose, lips, chin, jaw),
    the skull a polygon of straight cuts too; a slanted cameo neck line well inside the disc."""
    if fav:
        return poly(head(FACE_FAV, SKULL_POLY, 47, 14, 1.06))
    return poly(head(FACE_FULL, SKULL_POLY, 48, 20, 0.92))


SKULL_MIN = [(-11, 70), (-11, 50), (-24, 35), (-22, 11), (-5, 0)]


def head_b(fav=False):
    """More minimal: forehead and nose in one long line, one lip step, chin, jaw; the skull three
    straight cuts. No round cranium and no eye, which keeps it clear of the PBS head."""
    if fav:
        return poly(head(FACE_MIN_FAV, SKULL_MIN, 47, 14, 1.06))
    return poly(head(FACE_MIN, SKULL_MIN, 48, 20, 0.92))


def head_c(fav=False):
    """Breaks the rim: head A set larger and higher, so the crown runs out through the top of the
    disc. The disc stays one piece, open at the top, like a bust rising out of a coin."""
    if fav:
        return poly(head(FACE_FAV, SKULL_POLY, 47, -9, 1.2))
    return poly(head(FACE_FULL, SKULL_POLY, 47, -7, 1.14))


PROFILES = {'A': head_a, 'B': head_b, 'C': head_c}


def profile_disc(v, fav=False):
    return minus(DISC, PROFILES[v](fav))


# ====================================================================== NEW2 the sphere
def tri_up(cx, top, base, t=0.0):
    top, base = top + 2 * t, base - t
    hw = (base - top) / SQ3
    return poly([(cx, top), (cx + hw, base), (cx - hw, base)])


def tri_dn(cx, top, bottom, t=0.0):
    top, bottom = top + t, bottom - 2 * t
    hw = (bottom - top) / SQ3
    return poly([(cx - hw, top), (cx + hw, top), (cx, bottom)])


def cells7(cx, top, s, t):
    """T8's triangle of nine (three rows, side 3s) without the two bottom corner cells."""
    h = s * SQ3 / 2
    out = []
    for r in range(3):
        for k in range(2 * r + 1):
            if r == 2 and k in (0, 4):
                continue
            x = cx + (k - r) * s / 2
            y = top + r * h
            out.append((tri_up if k % 2 == 0 else tri_dn)(x, y, y + h, t))
    return out


def sphere_disc(s, g, rim=None, over=1.5):
    """Cells of side s with gaps g (each edge inset g/2). The cluster is set so its base runs just past
    the disc's inner edge (radius 50 - rim) and every cell is clipped by that edge: the foot of the
    cluster is the disc's own curve, and the band under it is as thick as the lines between cells."""
    rim = g if rim is None else rim
    h = s * SQ3 / 2
    inner = circle(50, 50, 50 - rim)
    base_y = 100 - rim + over + g / 2      # the uninset base line; inset by g/2 it lands at the edge + over
    top = base_y - 3 * h
    fig = union(*[inter(c, inner) for c in cells7(50, top, s, g / 2)])
    return minus(DISC, fig)
