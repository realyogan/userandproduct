"""Concept metadata and file writing for the round-seven tiles board (called by build_tiles.py)."""
import os

from build_tiles import PAL, CREAM, WHITE, WORD_DARK, parts
from geom7 import OUT, P, caph, fitbox, rect, render_avatar, resvg_py, shift, svg, word, write, bounds

C = {}

FONT = {'inst': ('inst-b', 'Instrument Sans Bold, lowercase'), 'frau': ('frau-sb', 'Fraunces SemiBold, lowercase')}


def concept(key, name, group, treatment, rotation, pal, paper, font, word_ink=False, accent=None, disc=False):
    pname, lo, hi = PAL[pal]
    ink_l = '#141414' if word_ink else lo
    ink_d = WORD_DARK
    L = {'m': lo, 'a': lo, 'ink': ink_l}
    D = {'m': hi, 'a': hi, 'ink': ink_d}
    sw = [lo, paper, '#141414']
    label = f'{pname} on {"Cream" if paper == CREAM else "White"}'
    if word_ink and pal != 'ink':
        label = f'{pname} and Ink on {"Cream" if paper == CREAM else "White"}'
    if accent:
        an, alo, ahi = PAL[accent]
        L['a'], D['a'] = alo, ahi
        sw = [lo, alo, paper]
        label = f'{pname} with {an} on {"Cream" if paper == CREAM else "White"}'
    C[key] = dict(name=name, group=group, treatment=treatment, rotation=rotation, palette=label, L=L, D=D,
                  swatch=sw, font=FONT[font][0], typeface=FONT[font][1], paper=paper, disc=disc)


concept('S1', 'The turning square', 'Filled', 'Four solid 7:5 tiles, soft corners', 'Pinwheel turned 18 degrees',
        'navy', WHITE, 'inst')
concept('S2', 'The sketch', 'Filled', "Four solid 7:5 tiles, soft corners, as the owner drew them",
        'Turned 40 degrees, each tile spun 4 more by hand', 'ink', CREAM, 'frau')
concept('S3', 'The quilt block', 'Filled', 'Four solid 4:3 tiles, sharp corners, a pinhole center', 'Square-on',
        'bronze', CREAM, 'frau', word_ink=True)
concept('S4', 'The open frame', 'Filled', 'Four 1:2 tiles on the sides of a square, the corners open',
        'Turned 15 degrees; mirror symmetric, so it never spins', 'green', WHITE, 'inst')
concept('S5', 'Two sizes', 'Filled', 'Four square tiles, the diagonal pair large, the other pair small',
        'Diamond grid at 45 degrees, each tile spun 12', 'oxblood', CREAM, 'frau')
concept('S6', 'The user among the product', 'Filled, one accent tile',
        "The sketch's four tiles, the top one in the accent", 'Turned 40 degrees', 'ink', WHITE, 'inst', accent='red')
concept('S7', 'The outlined sketch', 'Outlined', "The sketch's tiles as rings of one heavy weight",
        'Turned 40 degrees', 'blue', WHITE, 'inst', word_ink=True)
concept('S8', 'Four diamonds', 'Outlined', 'Four square rings, soft corners', 'Square tiles at 45 degrees',
        'oxblood', WHITE, 'frau')
concept('S9', 'Mixed weights', 'Outlined', 'Four square rings, the diagonal pair heavy, the other pair light',
        'Diamond grid at 45 degrees, each tile spun 15', 'ink', WHITE, 'inst')
concept('S10', 'The pierced disc', 'Carved disc', 'Four spun square tiles cut through a solid disc, floating',
        'Diamond grid at 45 degrees, each tile spun 15', 'navy', WHITE, 'inst', disc=True)
concept('S11', 'The inlaid disc', 'Carved disc', 'Only the tile outlines are cut; the tiles stand as islands',
        'Turned 40 degrees', 'bronze', CREAM, 'frau', disc=True)
concept('S12', 'One breaks the rim', 'Carved disc', "The sketch cut from the disc, the lowest tile pushed out through the edge",
        'Turned 40 degrees', 'green', CREAM, 'frau', disc=True)
concept('S13', 'The carved block', 'Carved square', "The sketch cut out of a soft square block",
        'Turned 40 degrees inside a square-on block', 'ink', WHITE, 'inst')
concept('S14', 'Three cut, one kept', 'Carved disc, two tones',
        'Three tiles cut through the disc; the fourth stays solid, in the accent', 'Turned 40 degrees',
        'navy', WHITE, 'inst', accent='red', disc=True)
concept('S15', 'Four pages fanned', 'Derivative', 'Four 3:4 sheets on one corner pivot, each cut from the next',
        'Fanned 0 to 42 degrees in 14-degree steps', 'oxblood', CREAM, 'frau')
concept('S16', 'Two tiles', 'Derivative', 'Two neighboring tiles of the sketch, one solid, one outlined',
        'Turned 40 degrees', 'blue', WHITE, 'inst', word_ink=True)
concept('S17', 'The empty seat', 'Derivative', 'Three solid tiles and the fourth an outline', 'Turned 40 degrees',
        'green', WHITE, 'inst')
concept('S18', 'The window disc', 'Carved disc', 'Four sharp 4:3 tiles cut through the disc, small and floating',
        'Square-on', 'red', WHITE, 'inst', word_ink=True, disc=True)


# ---------------------------------------------------------------------- files
def colors(mode, c):
    if mode == 'mono':
        return {'m': 'currentColor', 'a': 'currentColor', 'ink': 'currentColor'}
    return c['L'] if mode == 'light' else c['D']


def body(ps, col, s=1.0, dx=0.0, dy=0.0):
    return ''.join(P(shift(d, dx, dy, s) if (s != 1 or dx or dy) else d, col[r]) for d, r in ps)


def ink_box(ps):
    bs = [bounds(d) for d, _ in ps]
    return min(b[0] for b in bs), min(b[1] for b in bs), max(b[2] for b in bs), max(b[3] for b in bs)


def mark_svg(key, mode, fav=False, label='userandproduct mark'):
    col = colors(mode, C[key])
    vb = (-1, -1, 102, 102) if not fav else (0, 0, 100, 100)
    return svg(vb, body(parts(key, fav), col), label)


def lockup_svg(key, mode, label='userandproduct'):
    c = C[key]
    col = colors(mode, c)
    cap = caph(c['font'])
    wd, wb = word('userandproduct', c['font'], -10)
    ps = parts(key)
    x0, y0, x1, y1 = ink_box(ps)
    H = cap * (1.62 if c['disc'] else 1.5)      # height of the mark
    s = H / (y1 - y0)
    yc = -cap * 0.42                             # centerd a little below the cap middle
    mw = (x1 - x0) * s
    gap = cap * 0.46
    b = body(ps, col, s, -x0 * s, yc - H / 2 - y0 * s)
    b += P(shift(wd, mw + gap, 0), col['ink'])
    top, bot = min(yc - H / 2, wb[1]), max(yc + H / 2, wb[3])
    return svg(fitbox(0, top, mw + gap + wb[2], bot, 4), b, label)


def avatar_svg(key):
    c = C[key]
    ps = parts(key)
    if c['disc']:
        b = P(rect(0, 0, 100, 100), c['paper']) + body(ps, c['L'])
    else:
        k = 0.6
        b = P(rect(0, 0, 100, 100), c['paper']) + body(ps, c['L'], k, 50 - 50 * k, 50 - 50 * k)
    return svg((0, 0, 100, 100), b, 'userandproduct avatar')


def render_png(svg_text, path, size):
    data = bytes(resvg_py.svg_to_bytes(svg_string=svg_text, width=size, height=size))
    with open(path, 'wb') as f:
        f.write(data)


def build(keys):
    for k in keys:
        m = k.lower()
        for mode in ('light', 'dark', 'mono'):
            sfx = '' if mode == 'light' else '-' + mode
            write(f'{m}-lockup{sfx}.svg', lockup_svg(k, mode))
            write(f'{m}-mark{sfx}.svg', mark_svg(k, mode))
        fav = mark_svg(k, 'light', True, 'userandproduct')
        write(f'{m}-favicon.svg', fav)
        for sz in (16, 32):
            render_png(fav, os.path.join(OUT, f'{m}-favicon-{sz}.png'), sz)
        av = avatar_svg(k)
        write(f'{m}-avatar.svg', av)
        render_avatar(av, os.path.join(OUT, f'{m}-avatar-400.png'))
