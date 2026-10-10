"""Geometry helpers for the round 2 marks: shapes as SVG path data, booleans with skia-pathops."""
import math
import pathops
from fontTools.svgLib.path import parse_path
from fontTools.pens.svgPathPen import SVGPathPen


def P(d):
    """SVG path data to a pathops Path (arcs become cubics)."""
    p = pathops.Path()
    parse_path(d, p.getPen())
    return p


def f(v):
    return ('%.2f' % v).rstrip('0').rstrip('.')


def rect(x, y, w, h, r=0):
    """Rectangle; r is one radius or (tl, tr, br, bl)."""
    tl, tr, br, bl = (r, r, r, r) if not isinstance(r, (tuple, list)) else r
    d = 'M%s %s' % (f(x + tl), f(y))
    d += ' H%s' % f(x + w - tr)
    if tr: d += ' A%s %s 0 0 1 %s %s' % (f(tr), f(tr), f(x + w), f(y + tr))
    d += ' V%s' % f(y + h - br)
    if br: d += ' A%s %s 0 0 1 %s %s' % (f(br), f(br), f(x + w - br), f(y + h))
    d += ' H%s' % f(x + bl)
    if bl: d += ' A%s %s 0 0 1 %s %s' % (f(bl), f(bl), f(x), f(y + h - bl))
    d += ' V%s' % f(y + tl)
    if tl: d += ' A%s %s 0 0 1 %s %s' % (f(tl), f(tl), f(x + tl), f(y))
    return P(d + ' Z')


def circle(cx, cy, r):
    return P('M%s %s A%s %s 0 1 1 %s %s A%s %s 0 1 1 %s %s Z' % (
        f(cx - r), f(cy), f(r), f(r), f(cx + r), f(cy), f(r), f(r), f(cx - r), f(cy)))


def poly(pts):
    return P('M' + ' L'.join('%s %s' % (f(x), f(y)) for x, y in pts) + ' Z')


def U(x, y, w, h, t):
    """Capital U opening up: box x..x+w, y..y+h, stem t, round bottom of radius w/2."""
    r = w / 2
    outer = P('M%s %s V%s A%s %s 0 0 0 %s %s V%s Z' % (
        f(x), f(y), f(y + h - r), f(r), f(r), f(x + w), f(y + h - r), f(y)))
    return op(outer, counter_u(x, y, w, h, t), 'diff')


def counter_u(x, y, w, h, t, top_extra=0):
    """The counter of U(): the slot inside it (top_extra lifts its open top)."""
    r = w / 2
    ri = r - t
    return P('M%s %s V%s A%s %s 0 0 0 %s %s V%s Z' % (
        f(x + t), f(y - top_extra), f(y + h - r), f(ri), f(ri), f(x + w - t), f(y + h - r), f(y - top_extra)))


def D(x, y, w, h, t):
    """Capital D: stem on the left, bowl of radius h/2 on the right."""
    r = h / 2
    outer = P('M%s %s H%s A%s %s 0 0 1 %s %s H%s Z' % (f(x), f(y), f(x + w - r), f(r), f(r), f(x + w - r), f(y + h), f(x)))
    return op(outer, counter_d(x, y, w, h, t), 'diff')


def counter_d(x, y, w, h, t):
    r = h / 2
    ri = r - t
    return P('M%s %s H%s A%s %s 0 0 1 %s %s H%s Z' % (
        f(x + t), f(y + t), f(x + w - r), f(ri), f(ri), f(x + w - r), f(y + h - t), f(x + t)))


def solid_d(x, y, w, h, rl=0):
    r = h / 2
    d = 'M%s %s H%s A%s %s 0 0 1 %s %s H%s' % (f(x + rl), f(y), f(x + w - r), f(r), f(r), f(x + w - r), f(y + h), f(x + rl))
    if rl:
        d += ' A%s %s 0 0 1 %s %s V%s A%s %s 0 0 1 %s %s' % (f(rl), f(rl), f(x), f(y + h - rl), f(y + rl), f(rl), f(rl), f(x + rl), f(y))
    return P(d + ' Z')


def ring(cx, cy, ro, ri):
    return op(circle(cx, cy, ro), circle(cx, cy, ri), 'diff')


OPS = {'union': pathops.PathOp.UNION, 'diff': pathops.PathOp.DIFFERENCE,
       'inter': pathops.PathOp.INTERSECTION, 'xor': pathops.PathOp.XOR}


def op(a, b, kind):
    return pathops.op(a, b, OPS[kind], fix_winding=True)


def union(*ps):
    out = ps[0]
    for p in ps[1:]:
        out = op(out, p, 'union')
    return out


def transform(p, sx=1, sy=None, tx=0, ty=0, rot=0, cx=0, cy=0):
    """Scale about the origin, then rotate (degrees) about cx, cy, then translate."""
    sy = sx if sy is None else sy
    a = math.radians(rot)
    c, s = math.cos(a), math.sin(a)

    def T(pt):
        x, y = pt[0] * sx, pt[1] * sy
        x, y = x - cx, y - cy
        x, y = x * c - y * s + cx, x * s + y * c + cy
        return (x + tx, y + ty)
    out = pathops.Path()
    pen = out.getPen()
    for verb, pts in p.segments:
        if verb == 'moveTo': pen.moveTo(T(pts[0]))
        elif verb == 'lineTo': pen.lineTo(T(pts[0]))
        elif verb == 'curveTo': pen.curveTo(*[T(q) for q in pts])
        elif verb == 'qCurveTo': pen.qCurveTo(*[T(q) for q in pts])
        elif verb == 'closePath': pen.closePath()
        elif verb == 'endPath': pen.endPath()
    return out


def d_of(p):
    pen = SVGPathPen(None, ntos=f)
    p.draw(pen)
    return pen.getCommands()


def bounds(p):
    return p.bounds  # (xmin, ymin, xmax, ymax)


def empty(p):
    try:
        b = p.bounds
        return b[2] - b[0] < 0.5 or b[3] - b[1] < 0.5
    except Exception:
        return True
