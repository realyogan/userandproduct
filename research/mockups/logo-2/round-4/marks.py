"""The round 4 marks as geometry (round 3 shapes are copied here as the starting point) on a 512 canvas (y down).

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


# ================================================================== round 4

from functools import partial


def rot_all(layers, deg, cx=256, cy=256):
    """Turn layers by deg degrees; negative is anticlockwise on screen (y runs down)."""
    return [(r, transform(p, rot=deg, cx=cx, cy=cy)) for r, p in layers]


def scale_all(layers, k, cx=256, cy=256):
    return [(r, transform(p, sx=k, tx=cx - cx * k, ty=cy - cy * k)) for r, p in layers]


def capsule(x1, y1, x2, y2, w, g=0):
    """A stroke with round ends from (x1, y1) to (x2, y2), w wide, grown by g."""
    length = math.hypot(x2 - x1, y2 - y1)
    ang = math.degrees(math.atan2(y2 - y1, x2 - x1)) - 90
    p = rect(-w / 2 - g, -g, w + 2 * g, length + 2 * g, w / 2 + g)
    return transform(p, rot=ang, cx=0, cy=0, tx=x1, ty=y1)


# ------------------------------------------------------------------ family 1: cup and ball

def cup(turn=0, lift=0, in_disc=False):
    """R3-03 turned `turn` degrees anticlockwise; `lift` raises the ball out of the bowl along its axis."""
    cutp = union(circle(256, 190, 150), rect(106, -20, 300, 210))
    coin = diff(disc(), cutp)
    ball = circle(256, 214 - lift, 104)
    if not in_disc:
        L = rot_all([('h', inter(cutp, disc())), ('c', coin), ('b', ball)], -turn)
        return dict(kind='coin', holder='circle', layers=L, mono=union(L[1][1], L[2][1]))
    L = rot_all(scale_all([('a', coin), ('b', ball)], 0.72), -turn)
    box = disc()
    return dict(kind='circle', layers=[('c', box)] + L, mono=diff(box, union(L[0][1], L[1][1])))


# ------------------------------------------------------------------ family 2: speech mark tails

def speech(head=(300, 218, 186), big=(260, 218, 226), notch=(40, 218, 236), wall=52, floor=218, left=-1):
    """R3-04 with its parts as parameters: the head disc, the circle the tail is cut from, the notch."""
    h = circle(*head)
    tail = inter(diff(circle(*big), circle(*notch)), rect(left, floor, 900, 600))
    shape = union(h, tail)
    lit = inter(diff(circle(notch[0], notch[1], notch[2] + wall), circle(*notch)), shape)
    return fit_shape(dict(kind='shape', layers=[('c', diff(shape, lit)), ('b', lit)], mono=shape))


def fit_shape(m, box=448):
    """Scale and centre a mark so its ink fits a box x box square in the middle of the canvas."""
    x0, y0, x1, y1 = m['mono'].bounds
    k = box / max(x1 - x0, y1 - y0)
    T = lambda p: transform(p, sx=k, tx=256 - (x0 + x1) / 2 * k, ty=256 - (y0 + y1) / 2 * k)
    return dict(m, layers=[(r, T(p)) for r, p in m['layers']], mono=T(m['mono']))


def speech_slit():
    """The tail as a cut through the rim: a curved slit runs in from the rim and stops short, leaving
    the tail joined at the foot; the inner wall of the slit is lit."""
    shape = circle(256, 256, 236)
    cx, cy, r = 36, 236, 238
    slit = inter(diff(circle(cx, cy, r + 22), circle(cx, cy, r)), rect(-1, 236, 514, 214))
    shape = diff(shape, slit)
    lit = inter(inter(diff(circle(cx, cy, r + 22 + 48), circle(cx, cy, r + 22)), shape), rect(-1, 160, 514, 400))
    return dict(kind='shape', layers=[('c', diff(shape, lit)), ('b', lit)], mono=shape)


def speech_wedge():
    """The tail as a solid wedge outside the disc, at the lower left; the wedge is the lit part."""
    h = circle(290, 222, 200)
    wdg = poly([(110, 280), (236, 400), (36, 488)])
    shape = union(h, wdg)
    lit = diff(wdg, h)
    return fit_shape(dict(kind='shape', layers=[('c', diff(shape, lit)), ('b', lit)], mono=shape))


# ------------------------------------------------------------------ family 3: square coin

def square_coin(radius=SQ, t=56, foot=410, width=280):
    """The earlier board's Square coin, with corner radius, channel width and depth as parameters."""
    sq = rect(0, 0, 512, 512, radius)
    x = 256 - width / 2
    channel = inter(U(x, -20, width, foot + 20, t), sq)
    tongue = inter(counter_u(x, -20, width, foot + 20, t, top_extra=10), sq)
    body = diff(sq, channel, tongue)
    return dict(kind='coin', holder='squircle', layers=[('h', channel), ('c', body), ('b', tongue)],
                mono=diff(sq, channel))


# ------------------------------------------------------------------ family 4: shelf

def books(turn=-24, w=118, h=340, x0=104, base=426):
    up = rect(x0, base - h, w, h, 20)

    def lean(g):
        p = transform(rect(-g, -g, w + 2 * g, h + 2 * g, 20 + g), rot=turn, cx=0, cy=h)
        bx0, by0, bx1, by1 = transform(rect(0, 0, w, h, 20), rot=turn, cx=0, cy=h).bounds
        return transform(p, tx=x0 + w - 18 - bx0, ty=base - by1)
    return up, lean


def shelf(turn=-24, w=118, h=340):
    up, lean = books(turn, w, h)
    lf = lean(0)
    layers = [('a', diff(up, lf)), ('b', diff(lf, up)), ('f', inter(up, lf))]
    mono = union(up, diff(lf, rect(104 - G, 426 - h - G, w + 2 * G, h + 2 * G, 20 + G)))
    return dict(kind=None, layers=layers, mono=mono)


def shelf_disc():
    up, lean = books(-24, 108, 300, x0=122, base=410)
    return cut('circle', up, lean(0), lean(G))


# ------------------------------------------------------------------ fresh marks

def lens():
    """Lens: a magnifying glass cut from a tile; the glass is lit."""
    frame = union(ring(222, 222, 150, 92), capsule(318, 318, 410, 410, 84))
    glass = circle(222, 222, 92)
    box = squircle()
    return dict(kind='squircle', layers=[('c', box), ('a', frame), ('b', glass)], mono=diff(box, frame))


def page_turn():
    """Page turn: an open spread with the right-hand page lifting over; where it crosses, it is lit."""
    spread = union(rect(84, 128, 172, 270, (18, 0, 0, 18)), rect(256, 128, 172, 270, (0, 18, 18, 0)))

    def leaf(g):
        return inter(inter(circle(556, 398, 300 + g), circle(226, 68, 400 + g)), rect(256 - g, -1, 300, 420))
    return cut('circle', spread, leaf(0), leaf(G))


def dividers():
    """Dividers: the drawing compass, two legs from one hinge; where the legs cross under the hinge, lit."""
    head = union(circle(256, 116, 50), rect(240, 52, 32, 40, 8))
    left = union(capsule(256, 120, 150, 440, 60), head)

    def right(g):
        return capsule(256, 120, 362, 440, 60, g)
    return cut('circle', left, right(0), right(G))


def desk_lamp():
    """Desk lamp: a jointed lamp leaning over the work; the bulb shows under the shade and is lit."""
    base = rect(118, 404, 190, 54, 27)
    arms = union(capsule(212, 420, 168, 262, 52), capsule(168, 262, 300, 172, 52), circle(168, 262, 34))
    shade = inter(circle(338, 214, 112), wedge(338, 214, 160, 340))
    bx, by = on_circle(338, 214, 14, 70)
    body = union(base, arms, shade)
    return cut('circle', body, circle(bx, by, 46), circle(bx, by, 46 + G))


def rook():
    """Rook: the chess piece that holds its ground; the crown sits on the collar and the seam is lit."""
    lower = union(rect(150, 384, 212, 58, 14), poly([(194, 390), (318, 390), (300, 226), (212, 226)]),
                  rect(176, 200, 160, 40, 10))
    crown = diff(rect(176, 100, 160, 116, 8), rect(208, 92, 32, 46), rect(272, 92, 32, 46))
    return cut('circle', lower, crown, union(crown, rect(150, 200 - G, 212, G + 16)))


def anvil():
    """Anvil: the maker's block; the striking face is lit."""
    face = union(rect(168, 170, 236, 64, (10, 18, 0, 0)),
                 diff(poly([(60, 170), (170, 170), (170, 234), (124, 234)]), circle(60, 300, 118)))
    body = union(poly([(198, 234), (372, 234), (338, 330), (232, 330)]), rect(176, 330, 218, 34, 0),
                 poly([(160, 392), (410, 392), (394, 364), (176, 364)]))
    return cut('circle', body, face, union(face, rect(150, 234, 260, G)))


def signpost():
    """Signpost: one post, two boards pointing opposite ways; where they cross the post, lit."""
    post = rect(228, 64, 56, 470, 0)

    def boards(g):
        return union(poly([(178 - g, 118 - g), (372 + 0.41 * g, 118 - g), (420 + 1.41 * g, 166),
                           (372 + 0.41 * g, 214 + g), (178 - g, 214 + g)]),
                     poly([(334 + g, 244 - g), (140 - 0.41 * g, 244 - g), (92 - 1.41 * g, 292),
                           (140 - 0.41 * g, 340 + g), (334 + g, 340 + g)]))
    return cut('circle', post, boards(0), boards(G))


def funnel():
    """Funnel: many ideas go in at the top, one comes out at the foot; the one is lit."""
    f = poly([(92, 112), (420, 112), (292, 286), (292, 372), (220, 372), (220, 286)])
    return cut('circle', f, circle(256, 418, 46), circle(256, 418, 46 + G))


def cube():
    """One block, three faces: design, product and business as the three visible sides of one solid."""
    top = poly([(256, 72), (415, 164), (256, 256), (97, 164)])
    left = poly([(97, 164), (256, 256), (256, 440), (97, 348)])
    right = poly([(256, 256), (415, 164), (415, 348), (256, 440)])
    k = G / 2
    seam = union(capsule(97, 164, 256, 256, G), capsule(256, 256, 415, 164, G), rect(256 - k, 256, G, 200))
    mono = diff(union(top, left, right), seam)
    return dict(kind=None, layers=[('a', left), ('b', right), ('f', top)], mono=mono)


# ------------------------------------------------------------------ the round, in board order

MARKS = [
    # Cup and ball: the original for reference, then 30, 45, 60 degrees anticlockwise, free and in a disc,
    # then the ball lifted at 45
    partial(cup, 0), partial(cup, 30), partial(cup, 30, in_disc=True), partial(cup, 45),
    partial(cup, 45, in_disc=True), partial(cup, 60), partial(cup, 60, in_disc=True), partial(cup, 45, 60),
    partial(cup, 45, 60, in_disc=True),
    # Speech mark: the original, then a longer, a heavier and a sharper-notched tail, and the tail as a wedge
    partial(speech),
    partial(speech, (286, 200, 170), (176, 200, 280), (0, 170, 250), 52, 200, -300),
    partial(speech, (286, 200, 170), (176, 200, 280), (-48, 150, 252), 56, 200, -300),
    partial(speech, (290, 206, 176), (206, 206, 260), (96, 330, 150), 46, 206, 60),
    speech_wedge,
    # Square coin: the original, softer corners, a wider channel, a shallower channel
    partial(square_coin), partial(square_coin, radius=168), partial(square_coin, t=74), partial(square_coin, foot=356),
    # Shelf: the original, a steeper lean with squatter books, in a disc, in blue
    partial(shelf), partial(shelf, -32, 132, 300), shelf_disc, partial(shelf),
    # New figurative candidates from round 3
    at_screen, door, raised_hand,
    # Fresh marks
    lens, dividers, desk_lamp, rook, anvil, signpost, funnel, cube,
]
