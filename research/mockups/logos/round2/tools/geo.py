"""Small vector kit for the round-two logos: paths, transforms, letter grids.

Letters are drawn on a 100-unit grid (x-height or cap height = 100), as centre-line
strokes (monoline faces) or as filled polygons (diagonals), then set, scaled and
placed by the concept builders in build_round2.py.
"""
import math


def fmt(v):
    s = f"{v:.2f}".rstrip('0').rstrip('.')
    return '0' if s in ('-0', '') else s


class Path:
    def __init__(self):
        self.c = []

    def M(self, x, y):
        self.c.append(['M', x, y]); return self

    def L(self, x, y):
        self.c.append(['L', x, y]); return self

    def A(self, rx, ry, large, sweep, x, y, rot=0.0):
        self.c.append(['A', rx, ry, rot, large, sweep, x, y]); return self

    def Z(self):
        self.c.append(['Z']); return self

    def poly(self, pts):
        self.M(*pts[0])
        for p in pts[1:]:
            self.L(*p)
        return self.Z()

    def tf(self, s=1.0, ang=0.0, tx=0.0, ty=0.0):
        a = math.radians(ang)
        ca, sa = math.cos(a), math.sin(a)

        def pt_(x, y):
            return (x * ca - y * sa) * s + tx, (x * sa + y * ca) * s + ty
        p = Path()
        for c in self.c:
            if c[0] in 'ML':
                p.c.append([c[0], *pt_(c[1], c[2])])
            elif c[0] == 'A':
                x, y = pt_(c[6], c[7])
                p.c.append(['A', c[1] * s, c[2] * s, c[3] + ang, c[4], c[5], x, y])
            else:
                p.c.append(['Z'])
        return p

    def d(self):
        out = []
        for c in self.c:
            if c[0] in 'ML':
                out.append(f"{c[0]}{fmt(c[1])} {fmt(c[2])}")
            elif c[0] == 'A':
                rot = fmt(c[3] % 360) if abs(c[1] - c[2]) > 1e-6 else '0'
                out.append(f"A{fmt(c[1])} {fmt(c[2])} {rot} {c[4]} {c[5]} {fmt(c[6])} {fmt(c[7])}")
            else:
                out.append('Z')
        return ''.join(out)


class Shape:
    """kind: 'S' stroke (w), 'F' fill, 'E' fill even-odd."""

    def __init__(self, kind, path, w=0.0, cap='butt', join='miter'):
        self.kind, self.path, self.w, self.cap, self.join = kind, path, w, cap, join

    def tf(self, s=1.0, ang=0.0, tx=0.0, ty=0.0):
        return Shape(self.kind, self.path.tf(s, ang, tx, ty), self.w * s, self.cap, self.join)


def tf_all(shapes, s=1.0, ang=0.0, tx=0.0, ty=0.0):
    return [sh.tf(s, ang, tx, ty) for sh in shapes]


def rect(x0, y0, x1, y1):
    return Shape('F', Path().poly([(x0, y0), (x1, y0), (x1, y1), (x0, y1)]))


def poly(pts):
    return Shape('F', Path().poly(pts))


def circle_path(cx, cy, r, sweep=1):
    return Path().M(cx + r, cy).A(r, r, 1, sweep, cx - r, cy).A(r, r, 1, sweep, cx + r, cy).Z()


def disc(cx, cy, r):
    return Shape('F', circle_path(cx, cy, r))


def ring(cx, cy, r, w):
    """Stroked circle, centre-line radius r."""
    return Shape('S', circle_path(cx, cy, r), w)


def line(x0, y0, x1, y1, w, cap='butt'):
    return Shape('S', Path().M(x0, y0).L(x1, y1), w, cap)


def draw(shapes, color, attrs=''):
    """Render shapes. Strokes sharing width/cap/join merge into one path."""
    out, groups, order = [], {}, []
    for sh in shapes:
        if sh.kind == 'S':
            key = (round(sh.w, 2), sh.cap, sh.join)
            if key not in groups:
                groups[key] = []
                order.append(('S', key))
            groups[key].append(sh.path.d())
        else:
            order.append(('F', sh))
    for kind, item in order:
        if kind == 'S':
            w, cap, join = item
            out.append(f'<path d="{"".join(groups[item])}" fill="none" stroke="{color}" '
                       f'stroke-width="{fmt(w)}" stroke-linecap="{cap}" stroke-linejoin="{join}"{attrs}/>')
        else:
            rule = ' fill-rule="evenodd"' if item.kind == 'E' else ''
            out.append(f'<path d="{item.path.d()}" fill="{color}"{rule}{attrs}/>')
    return ''.join(out)


def pt(cx, cy, rx, ry, deg):
    a = math.radians(deg)
    return cx + rx * math.cos(a), cy + ry * math.sin(a)


# ---------------------------------------------------------------- geometric lowercase (monoline)
class Geo:
    """Monoline geometric lowercase on a 100-unit x-height. ex < 1 narrows the bowls."""

    def __init__(self, w, ex=1.0, asc=142, desc=44, tall=124, track=0.0, side=None):
        self.w, self.ex, self.asc, self.desc, self.tall, self.track = w, ex, asc, desc, tall, track
        ss = 9 + 0.22 * w if side is None else side
        self.sb = {'s': ss, 'r': ss * 0.55, 'o': ss * 0.25}

    def glyph(self, ch):
        w, X = self.w, 100.0
        r = (X - w) / 2
        rx = r * self.ex
        bw = 2 * rx + w
        cx, cy = rx + w / 2, -X / 2
        S = lambda p: Shape('S', p, w)
        bowl = Path().M(cx + rx, cy).A(rx, r, 1, 1, cx - rx, cy).A(rx, r, 1, 1, cx + rx, cy).Z()
        if ch == 'o':
            return [S(bowl)], bw, 'r', 'r'
        if ch == 'a':
            return [S(bowl), S(Path().M(cx + rx, -X).L(cx + rx, 0))], bw, 'r', 's'
        if ch == 'd':
            return [S(bowl), S(Path().M(cx + rx, -self.asc).L(cx + rx, 0))], bw, 'r', 's'
        if ch == 'p':
            return [S(bowl), S(Path().M(cx - rx, -X).L(cx - rx, self.desc))], bw, 's', 'r'
        x0, x1 = w / 2, w / 2 + 2 * rx
        if ch == 'n':
            return [S(Path().M(x0, 0).L(x0, -X)),
                    S(Path().M(x0, cy).A(rx, r, 0, 1, x1, cy).L(x1, 0))], bw, 's', 's'
        if ch == 'u':
            return [S(Path().M(x0, -X).L(x0, cy).A(rx, r, 0, 0, x1, cy)),
                    S(Path().M(x1, -X).L(x1, 0))], bw, 's', 's'
        if ch == 'r':
            ex_, ey_ = pt(cx, cy, rx, r, -62)
            return [S(Path().M(x0, 0).L(x0, -X)),
                    S(Path().M(x0, cy).A(rx, r, 0, 1, ex_, ey_))], ex_ + w * 0.45, 's', 'o'
        if ch == 'e':
            ex_, ey_ = pt(cx, cy, rx, r, 40)
            return [S(Path().M(cx - rx, cy).L(cx + rx, cy)),
                    S(Path().M(cx + rx, cy).A(rx, r, 1, 0, ex_, ey_))], bw, 'r', 'r'
        if ch == 'c':
            sx, sy = pt(cx, cy, rx, r, -48)
            ex_, ey_ = pt(cx, cy, rx, r, 48)
            return [S(Path().M(sx, sy).A(rx, r, 1, 0, ex_, ey_))], sx + w * 0.5, 'r', 'o'
        if ch == 's':
            ry = (X - w) / 4
            rsx = ry * 1.12 * self.ex
            scx = rsx + w / 2
            y1 = -X + w / 2 + ry
            a = pt(scx, y1, rsx, ry, -26)
            b = pt(scx, y1 + 2 * ry, rsx, ry, 154)
            return [S(Path().M(*a).A(rsx, ry, 1, 0, scx, y1 + ry).A(rsx, ry, 1, 1, *b))], \
                2 * rsx + w, 'r', 'r'
        if ch == 't':
            cb = 20 + w / 2
            return [S(Path().M(cb, -self.tall).L(cb, 0)),
                    S(Path().M(0, -X + w / 2).L(2 * cb, -X + w / 2))], 2 * cb, 'o', 'o'
        raise KeyError(ch)


# ---------------------------------------------------------------- monoline capitals
class Caps:
    def __init__(self, w, wf=1.0, track=0.0, side=None):
        self.w, self.wf, self.track = w, wf, track
        ss = 10 + 0.2 * w if side is None else side
        self.sb = {'s': ss, 'r': ss * 0.6, 'o': ss * 0.2}

    def thick(self, dx, C=100.0):
        """Horizontal thickness of a diagonal of run dx over height C at stroke weight w."""
        return self.w * math.hypot(dx, C) / C

    def glyph(self, ch):
        w, C, wf = self.w, 100.0, self.wf
        S = lambda p: Shape('S', p, w)
        h = w / 2
        if ch == 'O':
            r = (C - w) / 2
            W = C * wf
            rx = (W - w) / 2
            return [S(Path().M(2 * rx + h, -C / 2).A(rx, r, 1, 1, h, -C / 2)
                      .A(rx, r, 1, 1, 2 * rx + h, -C / 2).Z())], W, 'r', 'r'
        if ch == 'C':
            r = (C - w) / 2
            rx = r * wf
            cx = rx + h
            a, b = pt(cx, -C / 2, rx, r, -45), pt(cx, -C / 2, rx, r, 45)
            return [S(Path().M(*a).A(rx, r, 1, 0, *b))], a[0] + h, 'r', 'o'
        if ch == 'U':
            W = 76 * wf
            xl, xr = h, W - h
            r = (xr - xl) / 2
            cy = -h - r
            return [S(Path().M(xl, -C).L(xl, cy).A(r, r, 0, 0, xr, cy).L(xr, -C))], W, 's', 's'
        if ch == 'S':
            ry = (C - w) / 4
            rsx = ry * 1.25 * wf
            scx = rsx + h
            y1 = -C + h + ry
            a = pt(scx, y1, rsx, ry, -28)
            b = pt(scx, y1 + 2 * ry, rsx, ry, 152)
            return [S(Path().M(*a).A(rsx, ry, 1, 0, scx, y1 + ry).A(rsx, ry, 1, 1, *b))], 2 * rsx + w, 'r', 'r'
        if ch == 'E':
            W = 58 * wf
            return [S(Path().M(W, -C + h).L(h, -C + h).L(h, -h).L(W, -h)),
                    S(Path().M(h, -C / 2).L(W * 0.9, -C / 2))], W, 's', 'o'
        if ch == 'T':
            W = 66 * wf
            return [S(Path().M(0, -C + h).L(W, -C + h)), S(Path().M(W / 2, -C).L(W / 2, 0))], W, 'o', 'o'
        if ch in 'PR':
            W = 62 * wf
            y0, y1 = -C + h, -C * 0.44
            rb = (y1 - y0) / 2
            xb = W - h - rb
            sh = [S(Path().M(h, 0).L(h, y0).L(xb, y0).A(rb, rb, 0, 1, xb, y1).L(h, y1))]
            if ch == 'R':
                W2 = W + 6 * wf
                t = self.thick(W2 - xb, -y1)
                sh.append(poly([(xb - t * 0.5, y1), (xb + t * 0.5, y1), (W2, 0), (W2 - t, 0)]))
                return sh, W2, 's', 'o'
            return sh, W, 's', 'r'
        if ch == 'D':
            W = 76 * wf
            r = (C - w) / 2
            xs = W - h - r
            return [S(Path().M(h, -h).L(h, -C + h).L(xs, -C + h).A(r, r, 0, 1, xs, -h).Z())], W, 's', 'r'
        if ch == 'A':
            W = 80 * wf
            m = W / 2
            t = self.thick(m)
            for _ in range(4):
                t = self.thick(m - t / 2)
            sh = [poly([(m - t, -C), (m, -C), (t, 0), (0, 0)]),
                  poly([(m, -C), (m + t, -C), (W, 0), (W - t, 0)])]
            yb = -C * 0.3
            f = -yb / C
            xa = t + (m - t) * f
            sh.append(S(Path().M(xa - 1, yb).L(W - xa + 1, yb)))
            return sh, W, 'o', 'o'
        if ch == 'N':
            W = 76 * wf
            t = self.thick(W - w)
            return [S(Path().M(h, 0).L(h, -C)), S(Path().M(W - h, 0).L(W - h, -C)),
                    poly([(0, -C), (t, -C), (W, 0), (W - t, 0)])], W, 's', 's'
        raise KeyError(ch)


# ---------------------------------------------------------------- squared heavy lowercase
class Block:
    def __init__(self, w, W=80, asc=128, desc=30, track=0.0, side=None):
        self.w, self.W, self.asc, self.desc, self.track = w, W, asc, desc, track
        ss = 7 if side is None else side
        self.sb = {'s': ss, 'r': ss, 'o': ss * 0.5}

    def glyph(self, ch):
        w, X, W = self.w, 100.0, self.W
        h = w / 2
        xl, xr, yt, yb = h, W - h, -X + h, -h
        ym = -X / 2
        S = lambda p: Shape('S', p, w)
        if ch == 'o':
            return [S(Path().poly([(xl, yt), (xr, yt), (xr, yb), (xl, yb)]))], W, 's', 's'
        if ch == 'a':
            return [S(Path().M(xl, yt).L(xr, yt).L(xr, 0)),
                    S(Path().M(xr, ym).L(xl, ym).L(xl, yb).L(xr, yb))], W, 's', 's'
        if ch == 'd':
            return [S(Path().M(xr, -self.asc).L(xr, yb).L(xl, yb).L(xl, yt).L(xr, yt))], W, 's', 's'
        if ch == 'p':
            return [S(Path().M(xl, self.desc).L(xl, yt).L(xr, yt).L(xr, yb).L(xl, yb))], W, 's', 's'
        if ch == 'n':
            return [S(Path().M(xl, 0).L(xl, yt).L(xr, yt).L(xr, 0))], W, 's', 's'
        if ch == 'u':
            return [S(Path().M(xl, -X).L(xl, yb).L(xr, yb).L(xr, -X))], W, 's', 's'
        if ch == 'r':
            Wr = W * 0.66
            return [S(Path().M(xl, 0).L(xl, yt).L(Wr, yt))], Wr, 's', 'o'
        if ch == 'e':
            em = -X * 0.52
            return [S(Path().M(xl, em).L(xr, em).L(xr, yt).L(xl, yt).L(xl, yb).L(W, yb))], W, 's', 's'
        if ch == 'c':
            return [S(Path().M(W, yt).L(xl, yt).L(xl, yb).L(W, yb))], W, 's', 'o'
        if ch == 's':
            return [S(Path().M(W, yt).L(xl, yt).L(xl, ym).L(xr, ym).L(xr, yb).L(0, yb))], W, 's', 's'
        if ch == 't':
            Wt = W * 0.7
            return [S(Path().M(xl, -X * 1.22).L(xl, yb).L(Wt, yb)), S(Path().M(0, yt).L(Wt, yt))], Wt, 's', 'o'
        raise KeyError(ch)


def set_text(font, text, x=0.0, y=0.0, size=100.0, tracking=None):
    """Set text with left edge at x and baseline at y; size is the x-height (or cap height)."""
    s = size / 100.0
    tr = font.track if tracking is None else tracking
    shapes, pen, prev = [], 0.0, None
    for ch in text:
        g, adv, lt, rt = font.glyph(ch)
        if prev is not None:
            pen += font.sb[prev] + font.sb[lt] + tr
        shapes += tf_all(g, 1.0, 0, pen, 0)
        pen += adv
        prev = rt
    return tf_all(shapes, s, 0, x, y), pen * s


def text_width(font, text, size=100.0, tracking=None):
    return set_text(font, text, 0, 0, size, tracking)[1]


def text_on_circle(font, text, cx, cy, rb, size, mid_deg, tracking=None):
    """Set text along a circle (baseline radius rb), centred on mid_deg (screen degrees,
    -90 = top), reading clockwise with the tops of the letters pointing outward."""
    s = size / 100.0
    tr = font.track if tracking is None else tracking
    items, pen, prev = [], 0.0, None
    for ch in text:
        g, adv, lt, rt = font.glyph(ch)
        if prev is not None:
            pen += font.sb[prev] + font.sb[lt] + tr
        items.append((g, pen, adv))
        pen += adv
        prev = rt
    total = pen * s
    span = math.degrees(total / rb)
    out = []
    for g, p0, adv in items:
        mid = (p0 + adv / 2) * s
        ang = mid_deg - span / 2 + math.degrees(mid / rb)
        a = math.radians(ang)
        px, py = cx + rb * math.cos(a), cy + rb * math.sin(a)
        local = tf_all(g, s, 0, -adv / 2 * s, 0)
        out += tf_all(local, 1.0, ang + 90, px, py)
    return out, span
