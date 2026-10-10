"""Build the round-two logo concepts (M1 to M10) and the review board.

Run from this folder:
    python build_round2.py            # all SVGs + index.html
    python build_round2.py M3 M7      # only those concepts (index is rebuilt too)

Every SVG is written to the parent folder as m<N>-<kind>[-dark|-mono].svg:
lockup, mark (light, dark, mono) and favicon (light). Mono files use currentColor.
"""
import os
import sys
import math
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from geo import (Path, Shape, rect, poly, disc, ring, line, draw, set_text, text_width,
                 text_on_circle, tf_all, circle_path, fmt, Geo, Caps, Block)

OUT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
INK, PAPER, DARK = '#111111', '#F3F1EC', '#141414'
MODES = ('light', 'dark', 'mono')


def svg(vb, body, label, defs=''):
    x, y, w, h = vb
    d = f'<defs>{defs}</defs>' if defs else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{fmt(x)} {fmt(y)} {fmt(w)} {fmt(h)}" '
            f'role="img" aria-label="{label}"><title>{label}</title>{d}{body}</svg>')


def pal(mode, accent, accent_dark, mid=None, mid_dark=None):
    if mode == 'light':
        return {'ink': INK, 'acc': accent, 'mid': mid or INK}
    if mode == 'dark':
        return {'ink': PAPER, 'acc': accent_dark, 'mid': mid_dark or PAPER}
    return {'ink': 'currentColor', 'acc': 'currentColor', 'mid': 'currentColor'}


def mask(mid, vb, black_shapes, white_shapes=None, base='white'):
    """A user-space mask: base fill over the view box, black shapes cut, white shapes add."""
    x, y, w, h = vb
    body = f'<rect x="{fmt(x)}" y="{fmt(y)}" width="{fmt(w)}" height="{fmt(h)}" fill="{base}"/>'
    if black_shapes:
        body += draw(black_shapes, 'black')
    if white_shapes:
        body += draw(white_shapes, 'white')
    return f'<mask id="{mid}" maskUnits="userSpaceOnUse" x="{fmt(x)}" y="{fmt(y)}" width="{fmt(w)}" height="{fmt(h)}">{body}</mask>'


CONCEPTS = {}


def concept(key, **meta):
    def wrap(fn):
        CONCEPTS[key] = dict(meta, build=fn)
        return fn
    return wrap


# =============================================================== M1 Swiss: the split square
@concept('M1', name='The x-height square', direction='Swiss International style',
         accent='Deep red #A3201B')
def m1(mode):
    p = pal(mode, '#A3201B', '#E2574C')
    font = Geo(19, ex=0.9, track=-3)
    X = 40
    A = font.asc * X / 100
    t, w = set_text(font, 'userandproduct', A + 0.45 * X, 0, X)
    sq = [rect(0, -A, A, -X - 2), rect(0, -X + 2, A, 0)]
    W = A + 0.45 * X + w
    lock = svg((-4, -A - 6, W + 8, A + 6 + font.desc * X / 100 + 6),
               draw(sq, p['acc']) + draw(t, p['ink']), 'userandproduct')
    mk = [rect(8, 8, 92, 30.4), rect(8, 35.4, 92, 92)]
    mark = svg((0, 0, 100, 100), draw(mk, p['acc']), 'userandproduct mark')
    fav = svg((0, 0, 32, 32), draw([rect(2, 2, 30, 8.6), rect(2, 11.6, 30, 30)], p['acc']), 'userandproduct')
    return lock, mark, fav


# =============================================================== M2 Bauhaus: u and p from primaries
def m2_shapes(p):
    stems = [rect(6, 15, 18, 35), rect(34, 15, 46, 35)]
    bowl = Shape('F', Path().M(6, 35).L(46, 35).A(20, 20, 0, 1, 6, 35).Z())
    p_bowl = disc(74, 35, 20)
    wedge = poly([(54, 15), (72, 15), (54, 85)])
    return draw(stems, p['ink']) + draw([bowl], p['acc']) + draw([p_bowl, wedge], p['ink'])


@concept('M2', name='Primary u and p', direction='Bauhaus', accent='Amber #B7791F')
def m2(mode):
    p = pal(mode, '#B7791F', '#E2AE4C')
    mark = svg((0, 0, 100, 100), m2_shapes(p), 'userandproduct mark')
    fav = svg((0, 0, 100, 100), m2_shapes(p), 'userandproduct')
    t, w = set_text(Geo(14), 'userandproduct', 110, 55, 26)
    lock = svg((2, 8, 110 + w + 6, 82), m2_shapes(p) + draw(t, p['ink']), 'userandproduct')
    return lock, mark, fav


# =============================================================== M3 Brutalist: trilithon and slab
def m3_mark(p, s=1.0, tx=0.0, ty=0.0, fav=False):
    u = poly([(10, 10), (40, 10), (40, 64), (60, 64), (60, 10), (76, 10), (90, 24), (90, 90), (10, 90)])
    chip = poly([(81, 5), (95, 5), (95, 19)])
    return draw(tf_all([u], s, 0, tx, ty), p['ink']) + draw(tf_all([chip], s, 0, tx, ty), p['acc'])


@concept('M3', name='Monolith and slab', direction='Brutalist', accent='Bronze #8A5A2B')
def m3(mode, fid='m3'):
    p = pal(mode, '#8A5A2B', '#C99460')
    mark = svg((0, 0, 100, 100), m3_mark(p), 'userandproduct mark')
    fav = svg((0, 0, 100, 100), m3_mark(p), 'userandproduct')
    font = Block(28)
    X = 36
    x0 = 106
    t, w = set_text(font, 'userandproduct', x0 + 13, 67, X)
    x1 = x0 + 13 + w + 13
    slab = poly([(x0, 10), (x1 - 10, 10), (x1, 20), (x1, 90), (x0, 90)])
    vb = (6, 6, x1 + 4 - 6, 88)
    mid = f'{fid}-{mode}-cut'
    defs = mask(mid, vb, t)
    body = m3_mark(p) + draw([slab], p['ink'], f' mask="url(#{mid})"')
    lock = svg(vb, body, 'userandproduct', defs)
    return lock, mark, fav


# =============================================================== M4 Art Deco: setback crest
def m4_emblem(p, s=1.0, tx=0.0, ty=0.0, w=3.0, fav=False):
    outer = Path().M(16, 90).L(16, 58).L(30, 58).L(30, 36).L(42, 36).L(42, 22).L(58, 22).L(58, 36)         .L(70, 36).L(70, 58).L(84, 58).L(84, 90)
    base = Path().M(6, 90).L(94, 90)
    spire = Path().M(50, 90).L(50, 13)
    gem = poly([(50, 2), (54, 8), (50, 14), (46, 8)])
    flutes = [Path().M(36, 90).L(36, 44), Path().M(64, 90).L(64, 44),
              Path().M(23, 90).L(23, 66), Path().M(77, 90).L(77, 66)]
    ink = [Shape('S', outer, w), Shape('S', base, w)]
    acc = [Shape('S', spire, w), gem] + ([] if fav else [Shape('S', f, w) for f in flutes])
    return draw(tf_all(ink, s, 0, tx, ty), p['ink']) + draw(tf_all(acc, s, 0, tx, ty), p['acc'])


@concept('M4', name='Setback crest', direction='Art Deco', accent='Amber gold #A8741A')
def m4(mode):
    p = pal(mode, '#A8741A', '#E2AE4C')
    mark = svg((0, 0, 100, 100), m4_emblem(p), 'userandproduct mark')
    fav = svg((2, 2, 96, 96), m4_emblem(p, w=7, fav=True), 'userandproduct')
    font = Caps(6.5, wf=1.28, track=30)
    C = 20
    tw = text_width(font, 'USERANDPRODUCT', C)
    W = tw + 40
    s = 1.15
    ex = W / 2 - 50 * s
    emb = m4_emblem(p, s, ex, 0, w=3.0)
    by = 90 * s
    rules = [line(0, by, ex + 6 * s, by, 3.0 * s), line(ex + 94 * s, by, W, by, 3.0 * s)]
    t, _ = set_text(font, 'USERANDPRODUCT', 20, by + 16 + C, C)
    low = [line(0, by + 16 + C + 14, W, by + 16 + C + 14, 1.4), line(0, by + 16 + C + 19, W, by + 16 + C + 19, 1.4)]
    body = emb + draw(rules + t, p['ink']) + draw(low, p['acc'])
    lock = svg((-4, 0, W + 8, by + 16 + C + 24), body, 'userandproduct')
    return lock, mark, fav


# =============================================================== M5 Japanese mon: three p
def m5_arches(w, r, d, depth, n=3):
    """n identical u shapes on a wheel: bowl outward at distance d, arms pointing to the centre."""
    u = Shape('S', Path().M(-r, -d + depth).L(-r, -d).A(r, r, 0, 1, r, -d).L(r, -d + depth), w)
    return [u.tf(1.0, k * 360 / n, 50, 50) for k in range(n)]


def m5_emblem(p, mid, fav=False):
    if fav:
        cut = m5_arches(11, 12, 18, 12)
    else:
        cut = m5_arches(8, 11.5, 19, 11) + [ring(50, 50, 41.5, 2.6)]
    vb = (0, 0, 100, 100)
    defs = mask(mid, vb, cut)
    return defs, draw([disc(50, 50, 47)], p['acc'], f' mask="url(#{mid})"')


@concept('M5', name='Three arches mon', direction='Japanese mon (family crest)', accent='Deep red #9B1C1C')
def m5(mode, fid='m5'):
    p = pal(mode, '#9B1C1C', '#E06A5E')
    defs, body = m5_emblem(p, f'{fid}-{mode}-m')
    mark = svg((0, 0, 100, 100), body, 'userandproduct mark', defs)
    fdefs, fbody = m5_emblem(p, f'{fid}-fav', fav=True)
    fav = svg((0, 0, 100, 100), fbody, 'userandproduct', fdefs)
    t, w = set_text(Geo(10.5), 'userandproduct', 118, 63, 26)
    ldefs, lbody = m5_emblem(p, f'{fid}-{mode}-l')
    lock = svg((0, 0, 118 + w + 4, 100), lbody + draw(t, p['ink']), 'userandproduct', ldefs)
    return lock, mark, fav


# =============================================================== M6 Blueprint: set square
def m6_mark(p, fav=False):
    if fav:
        tri = poly([(12, 88), (74, 88), (12, 26)])
        arc = Shape('S', Path().M(74, 88).A(62, 62, 0, 0, 12, 26), 8)
        return draw([tri], p['ink']) + draw([arc], p['acc'])
    tri = Shape('E', Path().poly([(16, 84), (74, 84), (16, 26)]).M(16, 73.6).L(26.4, 73.6).L(26.4, 84)
                .L(24.2, 84).L(24.2, 75.8).L(16, 75.8).Z())
    w = 1.8
    arc = Shape('S', Path().M(74, 84).A(58, 58, 0, 0, 16, 26), w)
    ext = [line(6, 84, 94, 84, w), line(16, 94, 16, 6, w)]
    dim = [line(16, 93, 74, 93, w), line(13.5, 95.5, 18.5, 90.5, w), line(71.5, 95.5, 76.5, 90.5, w)]
    q = (16 + 58 * math.cos(math.radians(-45)), 84 + 58 * math.sin(math.radians(-45)))
    tick = [line(q[0] - 4.5, q[1] - 4.5, q[0] + 4.5, q[1] + 4.5, w)]
    return draw([tri], p['ink']) + draw([arc] + ext + dim + tick, p['acc'])


@concept('M6', name='Set square', direction='Blueprint and scientific notation', accent='Deep blue #164E87')
def m6(mode):
    p = pal(mode, '#164E87', '#6AA6E6')
    mark = svg((0, 0, 100, 100), m6_mark(p), 'userandproduct mark')
    fav = svg((0, 0, 100, 100), m6_mark(p, fav=True), 'userandproduct')
    t, w = set_text(Geo(7.5), 'userandproduct', 108, 84, 30)
    lock = svg((2, 2, 106 + w + 4, 96), m6_mark(p) + draw(t, p['ink']), 'userandproduct')
    return lock, mark, fav


# =============================================================== M7 Notary seal
def nib(s=1.0, tx=0.0, ty=0.0):
    pth = Path().poly([(50, 29), (60.5, 45), (59, 63), (41, 63), (39.5, 45)])
    pth.M(49.3, 33).L(50.7, 33).L(50.7, 46.6).L(49.3, 46.6).Z()
    hole = circle_path(50, 49.5, 3)
    pth.c += hole.c
    collar = rect(41, 65.5, 59, 69.5)
    return tf_all([Shape('E', pth), collar], s, 0, tx, ty)


def m7_seal(p, fav=False):
    if fav:
        return draw([ring(50, 50, 44, 9)], p['acc']) + draw(nib(1.25, -12.5, -11.5), p['acc'])
    font = Caps(11)
    text = 'USERANDPRODUCT'
    # spread the name to fill about 300 degrees of the rim
    base = text_width(font, text, 100, 0)
    target = math.radians(298) * 35.5 / (9 / 100)
    tr = (target - base) / (len(text) - 1)
    rim, _ = text_on_circle(font, text, 50, 50, 35.5, 9, -90, tracking=tr)
    star = disc(50, 50 + 40, 2.2)
    rings = [ring(50, 50, 47, 2.2), ring(50, 50, 31.5, 1.2)]
    return draw(rings + rim + [star] + nib(0.82, 9, 7.5), p['acc'])


@concept('M7', name='Notary seal', direction='Letterpress seal or notary stamp', accent='Deep green #1E5A3C')
def m7(mode):
    p = pal(mode, '#1E5A3C', '#63BE8E')
    mark = svg((0, 0, 100, 100), m7_seal(p), 'userandproduct mark')
    fav = svg((0, 0, 100, 100), m7_seal(p, fav=True), 'userandproduct')
    font = Caps(12.5, track=6)
    t, w = set_text(font, 'USERANDPRODUCT', 114, 62, 24)
    lock = svg((0, 0, 114 + w + 4, 100), m7_seal(p) + draw(t, p['ink']), 'userandproduct')
    return lock, mark, fav


# =============================================================== M8 Optical: striped u
def m8_mark(p, mid, ox=0.0, oy=0.0, fav=False):
    if fav:
        f0, f1, per, size, ux, base = 4, 96, 18.4, 66, 17, 83
        ufont = Geo(36)
    else:
        f0, f1, per, size, ux, base = 8, 92, 7, 62, 19, 81
        ufont = Geo(30)
    n = int(round((f1 - f0) / per))
    th = per / 2
    out_st = [rect(f0, f0 + k * per, f1, f0 + k * per + th) for k in range(n)]
    in_st = [rect(f0, f0 + k * per + th, f1, f0 + k * per + per) for k in range(n)]
    if fav:
        in_st = [rect(f0, f0, f1, f1)]
    u, _ = set_text(ufont, 'u', ux, base, size)
    out_st, in_st, u = (tf_all(x, 1.0, 0, ox, oy) for x in (out_st, in_st, u))
    vb = (ox, oy, 100, 100)
    defs = mask(mid + 'o', vb, u) + mask(mid + 'i', vb, None, u, base='black')
    body = (draw(out_st, p['ink'], f' mask="url(#{mid}o)"') +
            draw(in_st, p['acc'], f' mask="url(#{mid}i)"'))
    return defs, body


@concept('M8', name='Striped u', direction='Optical pattern', accent='Deep blue #22388C')
def m8(mode, fid='m8'):
    p = pal(mode, '#22388C', '#7F96F2')
    defs, body = m8_mark(p, f'{fid}-{mode}-m')
    mark = svg((0, 0, 100, 100), body, 'userandproduct mark', defs)
    fdefs, fbody = m8_mark(p, f'{fid}-fav', fav=True)
    fav = svg((0, 0, 100, 100), fbody, 'userandproduct', fdefs)
    ldefs, lbody = m8_mark(p, f'{fid}-{mode}-l')
    t, w = set_text(Geo(24), 'userandproduct', 108, 81, 30)
    lock = svg((4, 4, 108 + w, 100), lbody + draw(t, p['ink']), 'userandproduct', ldefs)
    return lock, mark, fav


# =============================================================== M9 Dimensional: plinth
IX, IY = (math.cos(math.radians(30)), math.sin(math.radians(30))), (-math.cos(math.radians(30)), math.sin(math.radians(30)))


def iso(g, x, y, z):
    return (g[0] + x * IX[0] + y * IY[0], g[1] + x * IX[1] + y * IY[1] - z)


def iso_box(g, a, b, z0, h):
    A, B = a / 2, b / 2
    top = [iso(g, -A, -B, z0 + h), iso(g, A, -B, z0 + h), iso(g, A, B, z0 + h), iso(g, -A, B, z0 + h)]
    right = [iso(g, A, -B, z0), iso(g, A, B, z0), iso(g, A, B, z0 + h), iso(g, A, -B, z0 + h)]
    left = [iso(g, -A, B, z0), iso(g, A, B, z0), iso(g, A, B, z0 + h), iso(g, -A, B, z0 + h)]
    return top, left, right


def m9_mark(p, mid, fav=False):
    g = (50, 66)
    t1, l1, r1 = iso_box(g, 64, 64, 0, 17)
    t2, l2, r2 = iso_box(g, 34, 34, 17, 17)
    tops, lefts, rights = [poly(t1), poly(t2)], [poly(l1), poly(l2)], [poly(r1), poly(r2)]
    defs, attr = '', ''
    if p['ink'] == 'currentColor' or fav is None:
        edges = []
        for f in (t1, l1, r1, t2, l2, r2):
            edges.append(Shape('S', Path().poly(f), 2.4, 'round', 'round'))
        defs = mask(mid, (0, 0, 100, 100), edges)
        attr = f' mask="url(#{mid})"'
    body = draw(lefts, p['ink'], attr) + draw(rights, p['mid'], attr) + draw(tops, p['acc'], attr)
    # upper tier drawn last so it sits on the lower top face
    body = (draw([lefts[0]], p['ink'], attr) + draw([rights[0]], p['mid'], attr) + draw([tops[0]], p['acc'], attr) +
            draw([lefts[1]], p['ink'], attr) + draw([rights[1]], p['mid'], attr) + draw([tops[1]], p['acc'], attr))
    return defs, body


@concept('M9', name='Plinth', direction='Isometric and dimensional', accent='Deep green #23573F')
def m9(mode, fid='m9'):
    p = pal(mode, '#23573F', '#6FBF95', '#55524C', '#8E8A82')
    defs, body = m9_mark(p, f'{fid}-{mode}-m')
    mark = svg((0, 0, 100, 100), body, 'userandproduct mark', defs)
    fdefs, fbody = m9_mark(pal('light', '#23573F', '', '#55524C'), f'{fid}-fav', fav=True)
    fav = svg((0, 0, 100, 100), fbody, 'userandproduct', fdefs)
    font = Geo(17, track=2)
    X = 30
    pad = 16
    t, w = set_text(font, 'userandproduct', pad, 30 + 12 + 1.42 * X, X)
    W = w + 2 * pad
    y0, y1 = 30, 30 + 12 + 1.42 * X + 0.44 * X + 12
    dx, dy = 22, 16
    front = rect(0, y0, W, y1)
    top = poly([(0, y0), (W, y0), (W + dx, y0 - dy), (dx, y0 - dy)])
    side = poly([(W, y0), (W + dx, y0 - dy), (W + dx, y1 - dy), (W, y1)])
    vb = (-4, y0 - dy - 4, W + dx + 8, y1 - y0 + dy + 8)
    mid = f'{fid}-{mode}-l'
    cut = list(t)
    if mode == 'mono':
        cut += [Shape('S', Path().M(0, y0).L(W, y0).L(W, y1), 2.4)]
    defs2 = mask(mid, vb, cut)
    body2 = (draw([front], p['ink'], f' mask="url(#{mid})"') + draw([top], p['acc'], f' mask="url(#{mid})"') +
             draw([side], p['mid'], f' mask="url(#{mid})"'))
    lock = svg(vb, body2, 'userandproduct', defs2)
    return lock, mark, fav


# =============================================================== M10 Line and point
def m10_mark(p, fav=False):
    if fav:
        return draw([rect(3, 19.5, 29, 24)], p['ink']) + draw([disc(19, 14, 5.5)], p['acc'])
    return draw([rect(12, 57.5, 88, 64.5)], p['ink']) + draw([disc(59, 46.5, 11)], p['acc'])


@concept('M10', name='Line and point', direction='Minimal mark-and-dot', accent='Deep red #A3201B')
def m10(mode):
    p = pal(mode, '#A3201B', '#E2574C')
    mark = svg((0, 0, 100, 100), m10_mark(p), 'userandproduct mark')
    fav = svg((0, 0, 32, 32), m10_mark(p, fav=True), 'userandproduct')
    t, w = set_text(Geo(9.5, track=5), 'userandproduct', 104, 64.5, 27)
    lock = svg((8, 18, 104 + w + 2 - 8, 70), m10_mark(p) + draw(t, p['ink']), 'userandproduct')
    return lock, mark, fav


# =============================================================== write files
def build(keys):
    written = []
    for key in keys:
        c = CONCEPTS[key]
        k = key.lower()
        for mode in MODES:
            lock, mark, fav = c['build'](mode)
            suf = '' if mode == 'light' else '-' + mode
            for kind, data in (('lockup', lock), ('mark', mark)):
                fn = os.path.join(OUT, f'{k}-{kind}{suf}.svg')
                with open(fn, 'w', encoding='utf-8') as f:
                    f.write(data)
                written.append(fn)
            if mode == 'light':
                fn = os.path.join(OUT, f'{k}-favicon.svg')
                with open(fn, 'w', encoding='utf-8') as f:
                    f.write(fav)
                written.append(fn)
    for fn in written:
        ET.parse(fn)
    return written


if __name__ == '__main__':
    args = [a.upper() for a in sys.argv[1:]] or list(CONCEPTS)
    keys = [a for a in args if a in CONCEPTS] or list(CONCEPTS)
    files = build(keys)
    print(f'{len(files)} SVG files written and parsed')
    if 'NOINDEX' not in args:
        import board
        board.write(CONCEPTS, OUT)
        print('index.html written')
