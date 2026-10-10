"""Geometry for the ten round-1 marks (logo exploration 2).

Every mark is drawn on a 512 x 512 canvas. Shapes are built as SVG path data, combined with
skia-pathops (true booleans, so overlaps are real paths, not transparency), and returned as
ordered layers of (role, path). Roles map to colours through a palette:

  c  container (filled circle or rounded square)
  a  primary form          b  secondary form
  f  fold: where a and b overlap
  o  the part of a form that leaves the container (rocket R1-05 only)
"""

import math
import re

import pathops
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.svgLib.path import parse_path

K = 0.5523  # cubic circle constant


# ---------- path text helpers ----------

def fmt(v):
    s = f"{v:.1f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


def circle(cx, cy, r):
    k = K * r
    return (f"M{fmt(cx)} {fmt(cy - r)}C{fmt(cx + k)} {fmt(cy - r)} {fmt(cx + r)} {fmt(cy - k)} {fmt(cx + r)} {fmt(cy)}"
            f"C{fmt(cx + r)} {fmt(cy + k)} {fmt(cx + k)} {fmt(cy + r)} {fmt(cx)} {fmt(cy + r)}"
            f"C{fmt(cx - k)} {fmt(cy + r)} {fmt(cx - r)} {fmt(cy + k)} {fmt(cx - r)} {fmt(cy)}"
            f"C{fmt(cx - r)} {fmt(cy - k)} {fmt(cx - k)} {fmt(cy - r)} {fmt(cx)} {fmt(cy - r)}Z")


def rrect(x, y, w, h, r, k=K):
    """Rounded rectangle; k > 0.5523 gives a smoother, squircle-like corner."""
    r = min(r, w / 2, h / 2)
    c = r * (1 - k)
    x2, y2 = x + w, y + h
    return (f"M{fmt(x + r)} {fmt(y)}L{fmt(x2 - r)} {fmt(y)}C{fmt(x2 - c)} {fmt(y)} {fmt(x2)} {fmt(y + c)} {fmt(x2)} {fmt(y + r)}"
            f"L{fmt(x2)} {fmt(y2 - r)}C{fmt(x2)} {fmt(y2 - c)} {fmt(x2 - c)} {fmt(y2)} {fmt(x2 - r)} {fmt(y2)}"
            f"L{fmt(x + r)} {fmt(y2)}C{fmt(x + c)} {fmt(y2)} {fmt(x)} {fmt(y2 - c)} {fmt(x)} {fmt(y2 - r)}"
            f"L{fmt(x)} {fmt(y + r)}C{fmt(x)} {fmt(y + c)} {fmt(x + c)} {fmt(y)} {fmt(x + r)} {fmt(y)}Z")


def squircle(x, y, s):
    """The app-tile shape used for every rounded square on this board."""
    return rrect(x, y, s, s, 0.3 * s, k=0.72)


def rpoly(pts, rad, T=None):
    """Polygon with every corner rounded by `rad` (cubic fillets)."""
    T = T or (lambda p: p)
    n = len(pts)
    out = []
    for i in range(n):
        p0, p1, p2 = pts[i - 1], pts[i], pts[(i + 1) % n]
        def toward(a, b, d):
            dx, dy = b[0] - a[0], b[1] - a[1]
            L = math.hypot(dx, dy)
            d = min(d, L / 2)
            return (a[0] + dx * d / L, a[1] + dy * d / L)
        s = toward(p1, p0, rad)
        e = toward(p1, p2, rad)
        c1 = (s[0] + (p1[0] - s[0]) * K, s[1] + (p1[1] - s[1]) * K)
        c2 = (e[0] + (p1[0] - e[0]) * K, e[1] + (p1[1] - e[1]) * K)
        out.append((s, c1, c2, e))
    d = ""
    for i, (s, c1, c2, e) in enumerate(out):
        s, c1, c2, e = T(s), T(c1), T(c2), T(e)
        d += (f"M{fmt(s[0])} {fmt(s[1])}" if i == 0 else f"L{fmt(s[0])} {fmt(s[1])}")
        d += f"C{fmt(c1[0])} {fmt(c1[1])} {fmt(c2[0])} {fmt(c2[1])} {fmt(e[0])} {fmt(e[1])}"
    return d + "Z"


def transform_d(d, T):
    """Apply a point function to every coordinate pair of an absolute M/L/C/Q/Z path."""
    toks = re.findall(r"[MLCQZ]|-?[\d.]+", d)
    out, i, cmd = [], 0, None
    while i < len(toks):
        t = toks[i]
        if t in "MLCQZ":
            cmd = t
            out.append(t)
            i += 1
            continue
        x, y = T((float(toks[i]), float(toks[i + 1])))
        out.append(f"{fmt(x)} {fmt(y)}")
        i += 2
    return " ".join(out).replace(" Z", "Z")


def affine(scale=1.0, angle=0.0, dx=0.0, dy=0.0):
    a = math.radians(angle)
    ca, sa = math.cos(a), math.sin(a)
    f = lambda p: (dx + scale * (p[0] * ca - p[1] * sa), dy + scale * (p[0] * sa + p[1] * ca))
    f.m = (scale * ca, scale * sa, -scale * sa, scale * ca, dx, dy)
    return f


# ---------- boolean helpers ----------

def P(d):
    p = pathops.Path()
    parse_path(d, p.getPen())
    return p


def U(*ps):
    out = ps[0]
    for p in ps[1:]:
        out = pathops.op(out, p, pathops.PathOp.UNION)
    return out


def I(a, b):
    return pathops.op(a, b, pathops.PathOp.INTERSECTION)


def S(a, b):
    return pathops.op(a, b, pathops.PathOp.DIFFERENCE)


def D(p, T=None):
    pen = SVGPathPen(None)
    if T is not None:
        from fontTools.pens.transformPen import TransformPen
        p.draw(TransformPen(pen, T.m))
    else:
        p.draw(pen)
    d = pen.getCommands()
    d = re.sub(r"-?\d+\.\d+", lambda m: fmt(float(m.group())), d)
    return d


def xform(p, m):
    from fontTools.pens.transformPen import TransformPen
    out = pathops.Path()
    p.draw(TransformPen(out.getPen(), m))
    return out


def fit_free(spec, box=448):
    """Scale and centre a free-standing mark so its ink fills a box x box square on the canvas."""
    xs0, ys0, xs1, ys1 = 1e9, 1e9, -1e9, -1e9
    for _, p in spec["layers"]:
        b = p.bounds
        xs0, ys0, xs1, ys1 = min(xs0, b[0]), min(ys0, b[1]), max(xs1, b[2]), max(ys1, b[3])
    s = box / max(xs1 - xs0, ys1 - ys0)
    dx = 256 - s * (xs0 + xs1) / 2
    dy = 256 - s * (ys0 + ys1) / 2
    spec["layers"] = [(r, xform(p, (s, 0, 0, s, dx, dy))) for r, p in spec["layers"]]
    return spec


def bbox(p):
    return p.bounds  # (xmin, ymin, xmax, ymax)


# ---------- shared rocket ----------

def rocket_parts(T):
    """Upright rocket at the origin (nose at y=-190, base at y=110), mapped by T."""
    body = ("M0 -190C40 -160 64 -100 64 -40L64 94C64 104 58 110 48 110L-48 110C-58 110 -64 104 -64 94"
            "L-64 -40C-64 -100 -40 -160 0 -190Z")
    finL = rpoly([(-60, 6), (-126, 92), (-126, 156), (-60, 112)], 16, T)
    finR = rpoly([(60, 6), (126, 92), (126, 156), (60, 112)], 16, T)
    window = circle(0, -46, 31)
    flame = "M-44 70C-44 150 -18 200 0 262C18 200 44 150 44 70Z"
    hull = S(U(P(transform_d(body, T)), P(finL), P(finR)), P(transform_d(window, T)))
    return hull, P(transform_d(flame, T))


# ---------- the ten marks ----------

def m01_orbit():
    ring = S(P(circle(236, 276, 168)), P(circle(236, 276, 98)))
    a = 315 * math.pi / 180
    cx, cy = 236 + 133 * math.cos(a), 276 + 133 * math.sin(a)
    moon = P(circle(cx, cy, 84))
    return fit_free({"container": None, "layers": [("a", ring), ("b", moon), ("f", I(ring, moon))]})


def m02_frame():
    frame = S(P(rrect(116, 116, 280, 280, 74)), P(rrect(182, 182, 148, 148, 18)))
    frame = S(frame, P(rrect(326, 326, 140, 140, 0.1)))
    dot = P(circle(362, 362, 76))
    return {"container": "squircle", "layers": [("a", frame), ("b", dot), ("f", I(frame, dot))]}


def m03_key():
    bow = S(P(circle(256, 150, 94)), P(circle(256, 150, 36)))
    shaft = P(rrect(222, 236, 68, 232, 18))
    bit1 = P(rrect(270, 382, 74, 36, 9))
    bit2 = P(rrect(270, 432, 56, 36, 9))
    key = U(bow, shaft, bit1, bit2)
    guard = P(rrect(120, 228, 272, 64, 32))
    return {"container": "circle", "layers": [("a", key), ("b", guard), ("f", I(key, guard))]}


def m04_folder():
    back = U(P(circle(256, 168, 66)), P(rrect(134, 216, 244, 190, 34)))
    front = P(rpoly([(94, 292), (418, 266), (404, 420), (108, 420)], 26))
    return {"container": "squircle", "layers": [("a", back), ("b", front), ("f", I(back, front))]}


def m05_breakout():
    T = affine(scale=0.96, angle=45, dx=318, dy=196)
    hull, flame = rocket_parts(T)
    tile = P(squircle(56, 56, 400))
    inside = I(hull, tile)
    outside = S(hull, tile)
    flame_in = I(flame, tile)
    return {"container": "squircle-inset", "tile": tile,
            "layers": [("c", tile), ("b", flame_in), ("a", inside), ("f", I(flame_in, inside)), ("o", outside)]}


def m06_passenger():
    T = affine(scale=1.0, dx=256, dy=222)
    hull, flame = rocket_parts(T)
    return {"container": "circle", "layers": [("a", hull), ("b", flame), ("f", I(hull, flame))]}


def m07_switch():
    track = P(rrect(64, 178, 384, 156, 78))
    knob = P(circle(354, 256, 102))
    return fit_free({"container": None, "layers": [("a", track), ("b", knob), ("f", I(track, knob))]})


def m08_nib():
    nib = P("M140 102L372 102L372 196C372 292 304 352 256 434C208 352 140 292 140 196Z")
    holes = U(P(circle(256, 238, 30)), P(rrect(250, 238, 12, 210, 2)))
    nib = S(nib, holes)
    right = I(nib, P("M256 0L512 0L512 512L256 512Z"))
    left = S(nib, right)
    collar = I(nib, P(rrect(100, 102, 312, 54, 0.1)))
    return {"container": "circle", "layers": [("a", left), ("b", right), ("f", collar)]}


def m09_bookmark():
    body = P(rpoly([(150, 150), (362, 150), (362, 470), (256, 384), (150, 470)], 14))
    cap = P(rrect(150, 52, 212, 136, 46))
    return fit_free({"container": None, "layers": [("a", body), ("b", cap), ("f", I(body, cap))]})


def m10_clasp():
    def hook(cx, side):
        ring = S(P(circle(cx, 256, 122)), P(circle(cx, 256, 56)))
        ang = math.radians(42)
        far = 400
        if side > 0:
            wedge = f"M{cx} 256L{fmt(cx + far * math.cos(ang))} {fmt(256 - far * math.sin(ang))}L{fmt(cx + far * math.cos(ang))} {fmt(256 + far * math.sin(ang))}Z"
        else:
            wedge = f"M{cx} 256L{fmt(cx - far * math.cos(ang))} {fmt(256 - far * math.sin(ang))}L{fmt(cx - far * math.cos(ang))} {fmt(256 + far * math.sin(ang))}Z"
        cut = S(ring, P(wedge))
        # round the cut ends with caps of the ring's half-thickness
        rm, hw = 89, 33
        caps = []
        for s in (1, -1):
            a = ang if side > 0 else math.pi - ang
            caps.append(P(circle(cx + rm * math.cos(a), 256 - s * rm * math.sin(a), hw)))
        return U(cut, *caps)
    left = hook(200, +1)
    right = hook(312, -1)
    return {"container": "circle", "layers": [("a", left), ("b", right), ("f", I(left, right))]}


MARKS = [m01_orbit, m02_frame, m03_key, m04_folder, m05_breakout, m06_passenger, m07_switch, m08_nib,
         m09_bookmark, m10_clasp]
