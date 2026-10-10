"""The ten round 2 marks as geometry on a 512 canvas (y down).

Each mark returns layers [(role, path)], drawn in order. Roles: 'c' container, 'a' first tone,
'b' second tone, 'f' fold (the overlap of a and b, computed with a boolean, never with opacity).
"""
from geo import (rect, circle, poly, U, D, counter_u, counter_d, solid_d, ring, op, union,
                 transform, empty)

SQ = 116  # corner radius of the rounded-square container (22.7 percent of 512)


def squircle():
    return rect(0, 0, 512, 512, SQ)


def disc():
    return circle(256, 256, 256)


def fold(a, b):
    return op(a, b, 'inter')


def m01():
    """U and D share one stem."""
    t = 72
    u = U(66, 111, 204, 290, t)
    d = D(198, 111, 248, 290, t)
    return 'squircle', [('c', squircle()), ('a', u), ('b', d), ('f', fold(u, d))]


def m02():
    """A U turned on its side becomes the bowl of a D."""
    t = 80
    x0, y0, h = 116, 116, 280
    stem = rect(x0, y0, t, h)
    side_u = transform(U(0, 0, h, 250, t), rot=-90, cx=0, cy=0, tx=x0, ty=y0 + h)
    # U(0,0,w=h,250) opens up; rotated -90 it opens left with its round end on the right
    return 'circle', [('c', disc()), ('a', stem), ('b', side_u), ('f', fold(stem, side_u))]


def m03():
    """One ring: its lower half is a u, its upper half and the tail make a p."""
    t = 74
    x, w = 144, 228
    top, bot = 92, 372
    lower = U(x, 182, w, bot - 182, t)
    upper = transform(U(x, 0, w, 242 - top, t), sy=-1, ty=242)  # the same U flipped: an arch
    tail = rect(x, 300, t, 140)
    p_part = union(upper, tail)
    return 'circle', [('c', disc()), ('a', lower), ('b', p_part), ('f', fold(lower, p_part))]


def m04():
    """A solid D whose bowl holds a U in negative space; stem and bowl in two tones."""
    slab = rect(56, 56, 216, 400, (72, 0, 0, 72))
    bowl = circle(256, 256, 200)
    hole = U(164, 128, 196, 248, 62)
    a = op(op(slab, hole, 'diff'), rect(256, 0, 100, 512), 'diff')
    b = op(op(bowl, hole, 'diff'), rect(0, 0, 256, 512), 'diff')
    return None, [('a', a), ('b', b)]


def m05():
    """A U cut out of a filled circle; the circle's middle is the U's counter."""
    w, t = 244, 58
    x = 256 - w / 2
    groove = op(U(x, -40, w, 416, t), disc(), 'inter')
    tongue = op(counter_u(x, -40, w, 416, t), disc(), 'inter')
    rest = op(op(disc(), groove, 'diff'), tongue, 'diff')
    return 'circle', [('c', rest), ('a', groove), ('b', tongue)]


def m06():
    """A U made of two tones only: two hooks, one from each side, folded where they meet."""
    u = U(72, 64, 368, 384, 124)
    left = op(u, rect(0, 0, 292, 512), 'inter')
    right = op(u, rect(220, 0, 292, 512), 'inter')
    return None, [('a', left), ('b', right), ('f', fold(left, right))]


def m07():
    """U stacked on P, the P's bowl tucked into the U: one standing figure."""
    t = 64
    u = U(140, 40, 232, 208, t)
    bowl = D(140, 208, 232, 220, t)
    stem = rect(140, 300, t, 172)
    p = union(bowl, stem)
    return None, [('a', u), ('b', p), ('f', fold(u, p))]


def m08():
    """A reversed D that follows the tile's own corners; its counter is lit."""
    t = 104
    x, y, w, h = 84, 84, 344, 344
    d = D(x, y, w, h, t)
    d = op(d, rect(x - 1, y - 1, 60, h + 2), 'diff')
    d = union(d, rect(x, y, 70, h, (44, 0, 0, 44)))
    cnt = counter_d(x, y, w, h, t)
    return 'squircle', [('c', squircle()), ('a', d), ('b', cnt)]


def m09():
    """An ampersand: a P loop on top, a U bowl below, the P's stem as the tail."""
    t = 62
    loop = ring(220, 164, 86, 28)
    bowl = transform(U(0, 0, 236, 184, t), rot=38, cx=118, cy=100, tx=112, ty=206)
    leg = poly([(140, 190), (204, 190), (424, 430), (360, 430)])
    p = union(loop, leg)
    return 'circle', [('c', disc()), ('a', bowl), ('b', p), ('f', fold(bowl, p))]


FONT = __import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..', 'fonts', 'inter', 'InterDisplay-Bold.ttf')


def inter_u():
    """The u of Inter Display Bold as a pathops Path in font units (y up), plus its advance and stem box."""
    from fontTools.ttLib import TTFont
    import pathops
    font = TTFont(FONT)
    gs = font.getGlyphSet()
    p = pathops.Path()
    gs['u'].draw(p.getPen())
    return p, gs['u'].width, font['head'].unitsPerEm


def dog_ear(u, c):
    """Cut the top-right corner of a u (y down, top at its bounds) and fold it in: returns (body, flap)."""
    x0, y0, x1, y1 = u.bounds
    cut = poly([(x1 - c, y0 - 1), (x1 + 1, y0 - 1), (x1 + 1, y0 + c + 1)])
    body = op(u, cut, 'diff')
    flap = poly([(x1 - c, y0), (x1, y0 + c), (x1 - c, y0 + c)])
    return body, flap


def u_mark(height=384, top=64):
    """The Inter u scaled so its x-height is `height`, centred on 256, y down."""
    g, adv, upm = inter_u()
    gx0, gy0, gx1, gy1 = g.bounds
    s = height / 1118.0 * (1118.0 / (gy1 - 0)) if False else height / (gy1 - gy0)
    p = transform(g, sx=s, sy=-s)
    x0, y0, x1, y1 = p.bounds
    return transform(p, tx=256 - (x0 + x1) / 2, ty=top - y0)


def m10():
    """A custom u for the name: Inter's u with its right stem folded down like a page corner."""
    u = u_mark()
    x0, y0, x1, y1 = u.bounds
    stem = (x1 - x0) * 0.30
    body, flap = dog_ear(u, stem * 0.92)
    return None, [('a', body), ('f', flap)]


MARKS = [m01, m02, m03, m04, m05, m06, m07, m08, m09, m10]
