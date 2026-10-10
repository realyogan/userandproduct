"""The round 3 marks as geometry on a 512 canvas (y down).

Each mark returns a dict:
  kind   'circle' or 'squircle' (drawn in a container), 'coin' (the container is the mark, cut),
         'shape' (the silhouette is the icon shape), or None (stands free)
  holder for a coin, the avatar shape it fills ('circle' or 'squircle')
  layers [(role, path)] drawn in order. Roles: 'c' container or coin body, 'a' first tone,
         'b' second tone, 'f' fold (the overlap of two forms, a real boolean, never opacity),
         'h' a cut through a coin (never drawn in a master; painted white only in avatars)
  mono   one path: the mark in a single colour, readable without the fold (gaps or silhouette)
"""
import math
from geo import rect, circle, poly, U, counter_u, ring, op, union, transform

SQ = 116   # rounded-square corner radius (22.7 percent of 512)
G = 18     # the gap that separates two forms in the monochrome versions


def squircle():
    return rect(0, 0, 512, 512, SQ)


def disc():
    return circle(256, 256, 256)


def inter(a, b):
    return op(a, b, 'inter')


def diff(a, *bs):
    for b in bs:
        a = op(a, b, 'diff')
    return a


def wedge(cx, cy, a0, a1, r=900, steps=48):
    """A pie wedge from angle a0 to a1 (degrees, y down, 0 = east, 90 = south)."""
    pts = [(cx, cy)]
    for k in range(steps + 1):
        t = math.radians(a0 + (a1 - a0) * k / steps)
        pts.append((cx + r * math.cos(t), cy + r * math.sin(t)))
    return poly(pts)


def sector(cx, cy, ro, ri, a0, a1):
    return inter(ring(cx, cy, ro, ri), wedge(cx, cy, a0, a1))


def on_circle(cx, cy, r, deg):
    t = math.radians(deg)
    return cx + r * math.cos(t), cy + r * math.sin(t)


# ------------------------------------------------------------------ group A: the coin evolved

def m01():
    """Magnet: a deep U slot from the top; the two pole caps are the second tone."""
    slot = union(rect(192, -20, 128, 320), circle(256, 300, 64))
    coin = diff(disc(), slot)
    cap = rect(-1, -1, 514, 151)
    pole = inter(coin, cap)
    body = diff(coin, cap)
    mono = diff(coin, rect(-1, 150 - G / 2, 514, G))
    return dict(kind='coin', holder='circle', layers=[('h', inter(slot, disc())), ('c', body), ('b', pole)], mono=mono)


def rising():
    """Rising: the U groove is cut as before, but the tongue (the user) stands taller than the coin."""
    D = circle(256, 300, 212)
    T = union(rect(196, 84, 120, 256), circle(256, 84, 62), circle(256, 340, 60))
    O = union(rect(146, -20, 220, 360), circle(256, 340, 110))
    coin = diff(D, O)
    return dict(kind='coin', holder='circle', layers=[('h', inter(diff(O, T), D)), ('c', coin), ('b', T)],
                mono=union(coin, T))


def m03():
    """Cup and ball: the top of the coin is carved into a bowl; a ball (the user) rests in it."""
    cut = union(circle(256, 190, 150), rect(106, -20, 300, 210))
    coin = diff(disc(), cut)
    ball = circle(256, 214, 104)
    return dict(kind='coin', holder='circle', layers=[('h', inter(cut, disc())), ('c', coin), ('b', ball)],
                mono=union(coin, ball))


def m04():
    """Speech mark: one notch bitten from the coin leaves a tail; the notch's inner wall is lit."""
    head = circle(300, 218, 186)
    big = circle(260, 218, 226)
    notch = circle(40, 218, 236)
    tail = inter(diff(big, notch), rect(-1, 218, 514, 300))
    shape = union(head, tail)
    wall = inter(diff(circle(40, 218, 236 + 52), notch), shape)
    body = diff(shape, wall)
    return dict(kind='shape', layers=[('c', body), ('b', wall)], mono=shape)


def m05():
    """Square coin: a rounded square with a U channel cut through it; the tongue is the second tone."""
    sq = squircle()
    channel = inter(U(116, -20, 280, 430, 56), sq)
    tongue = inter(counter_u(116, -20, 280, 430, 56, top_extra=10), sq)
    body = diff(sq, channel, tongue)
    return dict(kind='coin', holder='squircle', layers=[('h', channel), ('c', body), ('b', tongue)],
                mono=diff(sq, channel))


# ------------------------------------------------------------------ group B: the orbit evolved

def m06():
    """Bead in the track: a heavy ring with one bead riding inside its stroke, a little wider than it."""
    rg = ring(256, 256, 184, 96)
    bx, by = on_circle(256, 256, 140, -45)
    bead = circle(bx, by, 80)
    layers = [('c', disc()), ('b', diff(rg, bead)), ('a', diff(bead, rg)), ('f', inter(bead, rg))]
    mono = diff(disc(), union(diff(rg, circle(bx, by, 80 + G)), bead))
    return dict(kind='circle', layers=layers, mono=mono)


def m07():
    """Broken ring: the ring ends where the disc begins; its two ends tuck under the disc and light up."""
    rg = ring(256, 276, 190, 104)
    dx, dy = on_circle(256, 276, 147, -90)
    d = circle(dx, dy, 98)
    rc = diff(rg, circle(dx, dy, 76))
    layers = [('a', diff(rc, d)), ('b', diff(d, rc)), ('f', inter(rc, d))]
    mono = union(diff(rc, circle(dx, dy, 98 + G)), d)
    return dict(kind=None, layers=layers, mono=mono)


def m08():
    """Heavy arc: a ring (the product) and a thicker arc over its top (the user), lit where they overlap."""
    cx, cy, rm, h = 256, 256, 150, 66            # ring centre line 150, the arc 132 thick with round ends
    rg = ring(cx, cy, 186, 114)

    def arc_of(e):
        ends = [circle(*on_circle(cx, cy, rm, a), h + e) for a in (238, 338)]
        return union(sector(cx, cy, rm + h + e, rm - h - e, 238, 338), *ends)
    arc = arc_of(0)
    layers = [('a', diff(rg, arc)), ('b', diff(arc, rg)), ('f', inter(rg, arc))]
    mono = union(diff(rg, arc_of(G)), arc)
    return dict(kind=None, layers=layers, mono=mono)


def m09():
    """Linked rings: two heavy rings, interlocked; the crossing on top is lit."""
    A = ring(190, 256, 152, 84)
    B = ring(322, 256, 152, 84)
    top = rect(-1, -1, 514, 257)
    bot = rect(-1, 256, 514, 257)
    layers = [('a', diff(A, B)), ('b', B), ('f', inter(inter(A, B), top))]
    mono = union(diff(A, inter(ring(322, 256, 152 + G, 84 - G), bot)),
                 diff(B, inter(ring(190, 256, 152 + G, 84 - G), top)))
    return dict(kind=None, layers=layers, mono=mono)


def m10():
    """Square orbit: a rounded-square ring with a heavy disc riding its top-right corner."""
    sr = diff(rect(56, 72, 384, 384, 124), rect(156, 172, 184, 184, 34))
    dx, dy = 372, 140
    d = circle(dx, dy, 98)
    layers = [('a', diff(sr, d)), ('b', diff(d, sr)), ('f', inter(sr, d))]
    mono = union(diff(sr, circle(dx, dy, 98 + G)), d)
    return dict(kind=None, layers=layers, mono=mono)


def m11():
    """Eclipse: a smaller disc slides over a bright one; the lit crescent is what is left."""
    sun = circle(240, 272, 166)
    moon = circle(298, 214, 150)
    cres = diff(sun, moon)
    blunt = circle(206, 306, 172)   # trims the crescent's tips so nothing runs under 8 units
    cres = inter(cres, blunt)
    layers = [('c', disc()), ('a', cres), ('b', inter(sun, moon))]
    mono = diff(disc(), cres)
    return dict(kind='circle', layers=layers, mono=mono)


# ------------------------------------------------------------------ group C: fresh

def m12():
    """Reader: a head (the user) set over the top of a page (the product); together, a person reading."""
    page = rect(150, 210, 212, 226, 26)
    head = circle(256, 170, 84)
    layers = [('c', disc()), ('a', diff(page, head)), ('b', diff(head, page)), ('f', inter(head, page))]
    mono = diff(disc(), union(diff(page, circle(256, 170, 84 + G)), head))
    return dict(kind='circle', layers=layers, mono=mono)


def crossing():
    """Crossing: three heavy discs, design, product and business, overlap; where all three meet is lit."""
    cs = [(256, 176), (339, 320), (173, 320)]
    ds = [circle(x, y, 150) for x, y in cs]
    allx = union(*ds)
    pairs = union(inter(ds[0], ds[1]), inter(ds[1], ds[2]), inter(ds[0], ds[2]))
    triple = inter(inter(ds[0], ds[1]), ds[2])
    layers = [('a', diff(allx, pairs)), ('b', diff(pairs, triple)), ('f', triple)]
    return dict(kind=None, layers=layers, mono=diff(allx, triple))


def m15():
    """Shelf: one book upright, one leaning on it; the corner where they touch is lit."""
    up = rect(104, 86, 118, 340, 20)
    lean = transform(rect(0, 0, 118, 340, 20), rot=-24, cx=0, cy=340)
    x0, y0, x1, y1 = lean.bounds
    lean = transform(lean, tx=204 - x0, ty=426 - y1)
    layers = [('a', diff(up, lean)), ('b', diff(lean, up)), ('f', inter(up, lean))]
    mono = union(up, diff(lean, rect(104 - G, 86 - G, 118 + 2 * G, 340 + 2 * G, 20 + G)))
    return dict(kind=None, layers=layers, mono=mono)


def m16():
    """Shield: a square (the product) and a disc (the user) of the same width make one form, square
    above and round below; where they overlap is lit."""
    s = rect(80, 52, 352, 228, (64, 64, 0, 0))
    d = circle(256, 280, 176)
    shape = union(s, d)
    # the lit overlap takes the last sliver of the corners too, so no tone runs to a hairline
    q = union(inter(s, d), inter(diff(s, d), rect(-1, 214, 514, 100)))
    return dict(kind='shape', layers=[('c', diff(shape, q)), ('f', q)], mono=shape)


def t_shaped():
    """T-shaped: a broad bar (product and business, the breadth) and a deep stem (design, the depth);
    the practitioner is where they cross, and that is lit."""
    bar = rect(56, 92, 400, 128, 64)
    stem = rect(192, 140, 128, 300, 64)
    layers = [('a', diff(bar, stem)), ('b', diff(stem, bar)), ('f', inter(bar, stem))]
    mono = union(bar, diff(stem, rect(56 - G, 92 - G, 400 + 2 * G, 128 + 2 * G, 64 + G)))
    return dict(kind=None, layers=layers, mono=mono)


def phi():
    """Phi: a disc (the user) on the axis of a bar (the product) makes the letter for the golden mean;
    where the bar crosses the disc is lit."""
    d = circle(256, 256, 156)
    bar = rect(204, 40, 104, 432, 52)
    layers = [('a', diff(bar, d)), ('b', diff(d, bar)), ('f', inter(bar, d))]
    mono = union(bar, diff(d, rect(204 - G, 0, 104 + 2 * G, 512)))
    return dict(kind=None, layers=layers, mono=mono)


def lidded():
    """Two solids: the coin is a cup (the product) and a lid with a tongue (the user); the U-shaped
    space between them is the cut."""
    gap = 24
    tongue = union(rect(170, 120, 172, 180), circle(256, 300, 86))
    outer = union(rect(170 - gap, 120 + gap, 172 + 2 * gap, 180), circle(256, 300, 86 + gap))
    wing = rect(-1, 120, 514, gap)
    cut = diff(union(outer, wing), tongue, rect(-1, -1, 514, 121))
    top = diff(inter(disc(), union(rect(-1, -1, 514, 121), tongue)), cut)
    cup = diff(disc(), cut, top)
    return dict(kind='coin', holder='circle', layers=[('h', inter(cut, disc())), ('c', cup), ('b', top)],
                mono=union(cup, top))


# ------------------------------------------------------------------ group C: figurative cut-outs

def cut(kind, a, b, b_gap):
    """A figure cut from a container: a (white) and b (second tone), lit where they overlap.
    Monochrome knocks both out of the container, with b_gap (b grown by G) keeping them apart."""
    box = disc() if kind == 'circle' else squircle()
    a, b, b_gap = inter(a, box), inter(b, box), inter(b_gap, box)
    layers = [('c', box), ('a', diff(a, b)), ('b', diff(b, a)), ('f', inter(a, b))]
    mono = diff(box, union(diff(a, b_gap), b))
    return dict(kind=kind, layers=layers, mono=mono)


def person(hx, hy, hr, sx, sy, sr, g=0):
    """Head and shoulders as one solid: a disc and a dome, each grown by g."""
    return union(circle(hx, hy, hr + g), inter(circle(sx, sy, sr + g), rect(-1, -1, 514, sy + g)))


def at_screen():
    """At the screen: a person seen from behind, in front of a screen; their head crosses its lower edge."""
    screen = rect(80, 96, 352, 236, 26)
    p = lambda g: person(256, 330, 68, 256, 520, 132, g)
    return cut('circle', screen, p(0), p(G))


def thumb():
    """Thumb on the phone: a phone (the product) and a thumb (the user) coming in from the edge."""
    phone = rect(176, 52, 196, 380, 40)
    t = lambda g: transform(rect(-g, -g, 112 + 2 * g, 360 + 2 * g, 56 + g), rot=-38, cx=56, cy=56, tx=170, ty=272)
    return cut('squircle', phone, t(0), t(G))


def holding():
    """In hand: an open hand (the user) carrying a block (the product) on its palm, thumb over the side."""
    block = rect(170, 128, 176, 176, 18)

    def hand(g):
        palm = rect(96 - g, 290 - g, 344 + 2 * g, 84 + 2 * g, 42 + g)          # palm and flat fingers
        thumb_ = transform(rect(-g, -g, 64 + 2 * g, 150 + 2 * g, 32 + g), rot=24, cx=32, cy=150, tx=110, ty=176)
        wrist = transform(rect(-g, -g, 110 + 2 * g, 260 + 2 * g, 0), rot=40, cx=0, cy=0, tx=142, ty=322)
        return union(palm, thumb_, wrist)
    return cut('circle', block, hand(0), hand(G))


def door():
    """Doorway: a person (the user) standing in a door frame (the product), shoulders wider than the door."""
    frame = diff(rect(120, 64, 272, 448, (136, 136, 0, 0)), rect(184, 128, 144, 400, (72, 72, 0, 0)))
    p = lambda g: person(256, 236, 50, 256, 470, 118, g)
    return cut('squircle', frame, p(0), p(G))


def eye():
    """Reading eye: an eye whose iris has dropped to the lower lid, looking down at the page."""
    lid = inter(inter(circle(256, 430, 300), circle(256, 82, 300)), rect(56, 0, 400, 512))
    iris = lambda g: circle(256, 346, 78 + g)
    return cut('circle', lid, iris(0), iris(G))


def raised_hand():
    """A question: a person (head and shoulders) with one arm raised; the arm crosses the shoulder, lit there."""
    body = person(206, 196, 64, 206, 476, 156)

    def arm(g):
        return transform(rect(-g, -g, 76 + 2 * g, 300 + 2 * g, 38 + g), rot=20, cx=38, cy=300, tx=264, ty=84)
    return cut('circle', body, arm(0), arm(G))


def glasses():
    """Glasses on a page: reading glasses (the reader) resting across the foot of a page."""
    page = rect(146, 70, 220, 290, 22)

    def specs(g):
        return union(circle(180, 350, 70 + g), circle(332, 350, 70 + g), rect(220 - g, 330 - g, 72 + 2 * g, 28 + 2 * g, 0))
    return cut('circle', page, specs(0), specs(G))


def shelf_cut():
    """Shelf: two books cut from a tile, one upright, one leaning on it; the corner where they touch is lit."""
    up = rect(118, 92, 116, 330, 18)

    def lean(g):
        p = transform(rect(-g, -g, 116 + 2 * g, 330 + 2 * g, 18 + g), rot=-24, cx=0, cy=330)
        x0, y0, x1, y1 = transform(rect(0, 0, 116, 330, 18), rot=-24, cx=0, cy=330).bounds
        return transform(p, tx=212 - x0, ty=422 - y1)
    return cut('squircle', up, lean(0), lean(G))


MARKS = [m01, lidded, m03, m04,
         m06, m07, m08, m09, m10, m11,
         m12, at_screen, holding, door, glasses, shelf_cut, crossing,
         raised_hand]
