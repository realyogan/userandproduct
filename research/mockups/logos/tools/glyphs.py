"""Geometric letter grid for the logo concepts.

Letters are built from rectangles, elliptical bands and quads on one grid:
cap height 100 (y = 0 is the cap line, y = 100 the baseline), x-height 74.
Every piece is wound clockwise, so a whole word is one path with the
default nonzero fill (overlaps simply merge). Output has absolute
coordinates, no transforms.
"""
import math

CAP = 100.0
XH = 74.0
XT = CAP - XH  # y of the x-height line
OS = 1.5       # overshoot for round letters


def f(v):
    s = f"{v:.2f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


class Rect:
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h

    def d(self, sc, tx, ty):
        x, y = tx + self.x * sc, ty + self.y * sc
        w, h = self.w * sc, self.h * sc
        return f"M{f(x)} {f(y)}h{f(w)}v{f(h)}h{f(-w)}Z"

    def bbox(self):
        return (self.x, self.y, self.x + self.w, self.y + self.h)


class Poly:
    def __init__(self, pts, hole=False):
        area = sum(pts[i][0] * pts[(i + 1) % len(pts)][1] - pts[(i + 1) % len(pts)][0] * pts[i][1]
                   for i in range(len(pts)))
        if (area < 0) != hole:
            pts = pts[::-1]
        self.pts = pts

    def d(self, sc, tx, ty):
        p = [(tx + x * sc, ty + y * sc) for x, y in self.pts]
        return "M" + "L".join(f"{f(x)} {f(y)}" for x, y in p) + "Z"

    def bbox(self):
        xs = [p[0] for p in self.pts]
        ys = [p[1] for p in self.pts]
        return (min(xs), min(ys), max(xs), max(ys))


class Band:
    """Elliptical band from angle a0 to a1 (degrees, screen space, a1 > a0).
    Outer radii rx, ry; thickness tx at the sides, ty at top and bottom.
    tx = rx and ty = ry gives a filled sector (a disc when 0..360)."""

    def __init__(self, cx, cy, rx, ry, tx, ty, a0, a1):
        self.c = (cx, cy, rx, ry, tx, ty, a0, a1)

    def d(self, sc, tx_, ty_):
        cx, cy, rx, ry, tx, ty, a0, a1 = self.c
        if a1 - a0 >= 360:
            return (Band(cx, cy, rx, ry, tx, ty, a0, a0 + 180).d(sc, tx_, ty_) +
                    Band(cx, cy, rx, ry, tx, ty, a0 + 180, a0 + 360).d(sc, tx_, ty_))
        X = lambda v: tx_ + v * sc
        Y = lambda v: ty_ + v * sc
        irx, iry = rx - tx, ry - ty
        r0, r1 = math.radians(a0), math.radians(a1)
        large = 1 if a1 - a0 > 180 else 0
        o0 = (cx + rx * math.cos(r0), cy + ry * math.sin(r0))
        o1 = (cx + rx * math.cos(r1), cy + ry * math.sin(r1))
        s = f"M{f(X(o0[0]))} {f(Y(o0[1]))}A{f(rx*sc)} {f(ry*sc)} 0 {large} 1 {f(X(o1[0]))} {f(Y(o1[1]))}"
        if irx <= 0.01 or iry <= 0.01:
            s += f"L{f(X(cx))} {f(Y(cy))}Z"
        else:
            i1 = (cx + irx * math.cos(r1), cy + iry * math.sin(r1))
            i0 = (cx + irx * math.cos(r0), cy + iry * math.sin(r0))
            s += (f"L{f(X(i1[0]))} {f(Y(i1[1]))}A{f(irx*sc)} {f(iry*sc)} 0 {large} 0 "
                  f"{f(X(i0[0]))} {f(Y(i0[1]))}Z")
        return s

    def bbox(self):
        cx, cy, rx, ry = self.c[:4]
        a0, a1 = self.c[6], self.c[7]
        pts = []
        a = a0
        while a <= a1 + 1e-6:
            r = math.radians(a)
            pts.append((cx + rx * math.cos(r), cy + ry * math.sin(r)))
            a += 2
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        return (min(xs), min(ys), max(xs), max(ys))


# ---------------------------------------------------------------- letters
# Each builder takes (s, h): stem width and horizontal thickness, returns
# (pieces, advance width, kind) where kind marks round/straight sides for
# spacing.

def g_U(s, h):
    W = 72
    rx, ry = W / 2, W / 2 + 2
    cy = CAP + OS - ry
    return [Rect(0, 0, s, cy + 0.5), Rect(W - s, 0, s, cy + 0.5),
            Band(W / 2, cy, rx, ry, s, h, 0, 180)], W, "|("


def g_S(s, h, top=0.0, base=CAP, W=68):
    H = base - top
    s, h = s * 0.92, h * 0.84
    ry = (H + 2 * OS + h) / 4
    rx = W / 2
    cyT = top - OS + ry
    cyB = base + OS - ry
    return [Band(rx, cyT, rx, ry, s * 0.98, h, 90, 328),
            Band(rx, cyB, rx, ry, s * 0.98, h, -90, 148)], W, "()"


def g_E(s, h):
    W = 58
    return [Rect(0, 0, s, CAP), Rect(0, 0, W, h), Rect(0, (CAP - h) / 2, W - 5, h),
            Rect(0, CAP - h, W, h)], W, "|/"


def _bowl(s, h, bx, rx, mb):
    return [Rect(0, 0, bx + 0.5, h), Rect(0, mb - h, bx + 0.5, h),
            Band(bx, mb / 2, rx, mb / 2, s, h, -90, 90)]


def g_R(s, h):
    W = 68
    mb = 58
    rx = 28
    bx = W - 2 - rx
    d = s * 1.2
    leg = Poly([(bx - 14, mb - h), (bx - 14 + d, mb - h), (W, CAP), (W - d, CAP)])
    return [Rect(0, 0, s, CAP)] + _bowl(s, h, bx, rx, mb) + [leg], W, "|/"


def g_P(s, h):
    W = 64
    mb = 60
    rx = 30
    return [Rect(0, 0, s, CAP)] + _bowl(s, h, W - rx, rx, mb), W, "|)"


def g_D(s, h):
    W = 80
    r = 50
    bx = W - r
    return [Rect(0, 0, s, CAP), Rect(0, 0, bx + 0.5, h), Rect(0, CAP - h, bx + 0.5, h),
            Band(bx, 50, r, 50, s, h, -90, 90)], W, "|("


def g_A(s, h):
    W = 82
    d = s * 1.22
    ax0 = W / 2 - d * 0.56
    left = Poly([(0, CAP), (ax0, 0), (ax0 + d, 0), (d, CAP)])
    right = Poly([(W - d, CAP), (W - ax0 - d, 0), (W - ax0, 0), (W, CAP)])
    yb = 66
    return [left, right, Rect(12, yb, W - 24, h)], W, "//"


def g_N(s, h):
    W = 78
    d = s * 1.2
    return [Rect(0, 0, s, CAP), Rect(W - s, 0, s, CAP),
            Poly([(0, 0), (d, 0), (W, CAP), (W - d, CAP)])], W, "||"


def g_T(s, h):
    W = 66
    return [Rect(0, 0, W, h), Rect((W - s) / 2, 0, s, CAP)], W, "//"


def g_H(s, h):
    W = 76
    return [Rect(0, 0, s, CAP), Rect(W - s, 0, s, CAP), Rect(0, (CAP - h) / 2, W, h)], W, "||"


def g_O(s, h):
    W = 98
    return [Band(W / 2, 50, W / 2, 50 + OS, s, h, 0, 360)], W, "()"


def g_C(s, h):
    r = 48
    a = 42
    W = r + r * math.cos(math.radians(a))
    return [Band(r, 50, r, 50 + OS, s, h, a, 360 - a)], W, "(/"


# lowercase
def _o(s, h, r=37):
    return Band(r, XT + XH / 2, r, XH / 2 + OS, s, h, 0, 360)


def g_o(s, h):
    return [_o(s, h)], 74, "()"


def g_c(s, h):
    r = 36
    a = 44
    W = r + r * math.cos(math.radians(a))
    return [Band(r, XT + XH / 2, r, XH / 2 + OS, s, h, a, 360 - a)], W, "(/"


def g_e(s, h):
    r = 37
    cy = XT + XH / 2
    return [Band(r, cy, r, XH / 2 + OS, s, h, 38, 360), Rect(0.5, cy - h, 2 * r - 1, h)], 74, "(/"


def g_a(s, h):
    return [_o(s, h), Rect(74 - s, XT, s, XH)], 74, "(|"


DESC = 26  # descender depth below the baseline


def g_p(s, h):
    return [_o(s, h), Rect(0, XT, s, XH + DESC)], 74, "|)"


def g_d(s, h):
    return [_o(s, h), Rect(74 - s, 0, s, CAP)], 74, "(|"


def _arch(s, h, W, top_stem):
    r = W / 2
    cy = XT + r - OS
    return [Rect(0, top_stem, s, CAP - top_stem), Band(r, cy, r, r, s, h, 180, 360),
            Rect(W - s, cy - 0.5, s, CAP - cy + 0.5)]


def g_n(s, h):
    return _arch(s, h, 64, XT), 64, "||"


def g_h(s, h):
    return _arch(s, h, 64, 0), 64, "||"


def g_u(s, h):
    W = 64
    r = W / 2
    cy = CAP - r + OS
    return [Rect(0, XT, s, cy - XT + 0.5), Band(r, cy, r, r, s, h, 0, 180),
            Rect(W - s, XT, s, XH)], W, "||"


def g_r(s, h):
    r = 27
    cy = XT + r - OS
    return [Rect(0, XT, s, XH), Band(r, cy, r, r, s, h, 180, 292)], 40, "|/"


def g_t(s, h):
    W = 42
    return [Rect((W - s) / 2 - 3, 8, s, CAP - 8), Rect(0, XT, W, h)], W, "//"


def g_s(s, h):
    return g_S(s, h, XT, CAP, W=58)


GLYPHS = {"U": g_U, "S": g_S, "E": g_E, "R": g_R, "P": g_P, "D": g_D, "A": g_A, "N": g_N,
          "T": g_T, "H": g_H, "O": g_O, "C": g_C, "o": g_o, "c": g_c, "e": g_e, "a": g_a,
          "d": g_d, "p": g_p, "n": g_n, "h": g_h, "u": g_u, "r": g_r, "t": g_t, "s": g_s}

# side kinds: | straight, ( or ) round, / open or diagonal
GAP = {"|": 1.0, "(": 0.7, ")": 0.7, "/": 0.45}


def weights(name):
    return {"black": (25, 21), "bold": (21, 18), "semi": (17, 15), "light": (10, 9)}[name]


def word(text, weight="bold", track=0.0, space=40.0):
    """Returns (pieces in unit space, width). Spacing is a base gap times
    side factors, plus tracking (in cap units)."""
    s, h = weights(weight)
    base = 9 + s * 0.35
    pieces, x, prev = [], 0.0, None
    for ch in text:
        if ch == " ":
            x += space + track * 1.5
            prev = None
            continue
        ps, W, kind = GLYPHS[ch](s, h)
        if prev is not None:
            g = base * (GAP[prev] + GAP[kind[0]]) / 2 * 2
            x += g * (0.62 if ch.isupper() else 0.5) + track
        for p in ps:
            pieces.append((p, x))
        x += W
        prev = kind[1]
    return pieces, x


def line(segments, track=0.0):
    """segments: list of (text, weight, role). Sets them as one run with
    the same spacing rules as word(), so "user" + "and" + "product" join
    like a single word. Returns (list of (role, pieces), width)."""
    out, x, prev = [], 0.0, None
    for text, weight, role in segments:
        s, h = weights(weight)
        sb, _ = weights("bold")
        base = 9 + sb * 0.35
        pieces = []
        for ch in text:
            if ch == " ":
                x += 40 + track * 1.5
                prev = None
                continue
            ps, W, kind = GLYPHS[ch](s, h)
            if prev is not None:
                g = base * (GAP[prev] + GAP[kind[0]])
                x += g * (0.62 if ch.isupper() else 0.5) + track
            for p in ps:
                pieces.append((p, x))
            x += W
            prev = kind[1]
        out.append((role, pieces))
    return out, x


def render(pieces, sc=1.0, tx=0.0, ty=0.0):
    """pieces: list of (shape, xoffset). Returns path data."""
    return "".join(p.d(sc, tx + xo * sc, ty) for p, xo in pieces)


def bbox(pieces):
    b = [p.bbox() for p, _ in pieces]
    xo = [xo for _, xo in pieces]
    return (min(bb[0] + o for bb, o in zip(b, xo)), min(bb[1] for bb in b),
            max(bb[2] + o for bb, o in zip(b, xo)), max(bb[3] for bb in b))
