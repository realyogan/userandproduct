"""Build the round-six logo concepts (R1 to R10) and the review board.

Brief: every concept is a solid disc with a figure cut out of it as negative space (the figure is the
hole), set beside a settled lowercase wordmark. R1 to R4 cut the tripod (a spine, two struts, three
feet; no cross) out of the disc; R5 to R10 cut other abstract figures.

Run from this folder:
    python build_round6.py            # all SVGs, PNG renders and index.html
    python build_round6.py R3 R8      # only those concepts (index is rebuilt too)
    python build_round6.py --sheet    # contact sheet of all marks at 160, 32 and 16px (scratch check)

Every cut is a real boolean: the disc path is the circle minus the figure (skia-pathops DIFFERENCE),
so each mark is one compound path (plus one tint path for the two-tone concept). Nothing white is
painted over the disc. Wordmarks are set from the OFL fonts with wordmark.py's shaping code.
Files per concept r<N>, in the parent folder:
  r<N>-lockup.svg, -lockup-dark.svg, -lockup-mono.svg
  r<N>-mark.svg,   -mark-dark.svg,   -mark-mono.svg
  r<N>-favicon.svg (heavier cuts for 16px) with r<N>-favicon-16.png and -32.png
  r<N>-avatar.svg (the disc fills the avatar) with r<N>-avatar-400.png
"""
import io
import math
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from geom6 import (OUT, TOOLS, P, caph, circle, fitbox, fmt, minus, rect, render_avatar, resvg_py,  # noqa: E402
                   seg, shift, svg, union, word, write, clip, bounds, Image)

WORD_DARK = '#EEE9DF'
NEAR = '#141414'
CREAM = '#F4EFE3'
DISC = circle(50, 50, 50)


def from_path_op(a, b, op):
    import pathops
    from geom6 import to_path, from_path
    ops = {'and': pathops.PathOp.INTERSECTION}
    return from_path(pathops.op(to_path(a), to_path(b), ops[op]))


def ring(cx, cy, r_out, r_in):
    """An annulus: a round hole with a solid dot left standing inside it."""
    return minus(circle(cx, cy, r_out), circle(cx, cy, r_in))


# ====================================================================== figures (the holes)
# Each returns (hole, tint) in a 100 x 100 box with the disc centred at (50, 50), radius 50.
# fav=True gives the heavier 16px cut.

def r1(fav=False):
    """The braced tripod (round five Q4) as the hole, floating inside the disc."""
    if fav:
        w, r, A, Lp, C = 11, 11.5, (50, 17), (21, 61), (50, 79)
    else:
        w, r, A, Lp, C = 8, 9.5, (50, 17), (20, 61), (50, 79)
    Rp = (100 - Lp[0], Lp[1])
    lines = [seg(*A, *Lp, w), seg(*A, *Rp, w), seg(*Lp, *C, w), seg(*Rp, *C, w), seg(*A, *C, w)]
    return union(*lines, circle(*Lp, r), circle(*Rp, r), circle(*C, r)), None


def r2(fav=False):
    """The tree of three (Q3): three lines fan from a point on the top rim; each terminal is a round
    hole with a solid disc standing inside it. The middle terminal sits higher, nearer the root."""
    if fav:
        w, R, rd, J, sides, centre = 10.5, 14, 8, (50, -4), ((23, 72), (77, 72)), (50, 52)
    else:
        w, R, rd, J, sides, centre = 7.5, 14, 7, (50, -4), ((23, 72), (77, 72)), (50, 52)
    lines = [seg(*J, *p, w, 'butt') for p in sides] + [seg(*J, *centre, w, 'butt')]
    hole = union(*lines, *[circle(*p, R) for p in sides], circle(*centre, R))
    if fav:  # at 16px the standing discs turn to noise, so the favicon keeps plain round holes
        return hole, None
    dots = [circle(*p, rd) for p in sides] + [circle(*centre, rd)]
    return minus(hole, *dots), None

def r3(fav=False):
    """The reduced tripod: spine and two struts only, no rings, no braces. The apex is cut flat (no
    point, so it never reads as an arrow), the struts splay wide, and all three feet are cut flat on
    one horizontal baseline: a stand, not a sign."""
    if fav:
        w, top, base, ang = 14, 20, 76, 29
    else:
        w, top, base, ang = 11.5, 20, 77, 30
    A = (50, top - 3)
    t = math.radians(ang)
    L = (base - top) / math.cos(t) + 20
    legs = [seg(*A, A[0] - L * math.sin(t), A[1] + L * math.cos(t), w, 'butt'),
            seg(*A, A[0] + L * math.sin(t), A[1] + L * math.cos(t), w, 'butt'),
            rect(50 - w / 2, top, 50 + w / 2, base + 20)]
    fig = union(*legs)
    return clip(fig, 0, top, 100, base), None

def r4(fav=False):
    """The three feet alone: three ring cuts in one low row, the middle one dropped, as the feet of
    the tripod stand on the ground; struts omitted. The solid dome above is the frame they carry."""
    if fav:
        ro, ri, g, drop = 13.5, 6, 2.5, 6
    else:
        ro, ri, g, drop = 12.5, 6.5, 3, 6
    d = 2 * ro + g
    y = 64
    pts = [(50 - d, y), (50, y + drop), (50 + d, y)]
    return union(*[ring(*p, ro, ri) for p in pts]), None

def r5(fav=False):
    """The reading line: a bar entering from the left rim and stopping square, then a full point."""
    if fav:
        h, x1, pr, px, y = 16, 56, 9.5, 77, 58
    else:
        h, x1, pr, px, y = 13, 58, 8, 76, 58
    return union(rect(-5, y - h / 2, x1, y + h / 2), circle(px, y, pr)), None

def r6(fav=False):
    """The margin: one straight cut from rim to rim, off centre at about the golden section, so the
    disc becomes a narrow part and a broad part, like the margin rule of a page."""
    w = 9 if fav else 6.5
    x = 38.2
    return rect(x - w / 2, -5, x + w / 2, 105), None

def r7(fav=False):
    """A spine with one terminal: a slot drops from the top rim and opens into one round hole below
    the centre, like a plumb line and its bob. No ring, no dot."""
    if fav:
        w, cy, R = 12, 63, 17
    else:
        w, cy, R = 9, 63, 15.5
    slot = rect(50 - w / 2, -5, 50 + w / 2, cy)
    return union(slot, circle(50, cy, R)), None

def r8(fav=False):
    """Two shapes meeting: two right-angle brackets, one cut clean through (top left), one cut as a
    lighter tone (bottom right), framing an empty centre like a printer's crop."""
    w = 13 if fav else 10.5
    a, L = 22, 34
    tl = union(rect(a, a, a + L, a + w), rect(a, a, a + w, a + L))
    b = 100 - a
    br = union(rect(b - L, b - w, b, b), rect(b - w, b - L, b, b))
    return tl, br


def r9(fav=False):
    """The passing: one slot drops from the top rim, another rises from the bottom rim, offset, and
    they pass each other through the middle without meeting."""
    w = 10 if fav else 8
    off = 11
    a = rect(50 - off - w / 2, -5, 50 - off + w / 2, 64)
    b = rect(50 + off - w / 2, 36, 50 + off + w / 2, 105)
    return union(a, b), None

def r10(fav=False):
    """The open square: a square channel cut into the disc, the square inside left standing, the
    channel open at one corner."""
    w = 10.5 if fav else 8
    s0, s1 = 25, 75
    outer = rect(s0 - w / 2, s0 - w / 2, s1 + w / 2, s1 + w / 2)
    inner = rect(s0 + w / 2, s0 + w / 2, s1 - w / 2, s1 - w / 2)
    frame = minus(outer, inner)
    gapc = 16 if fav else 14
    frame = minus(frame, rect(s1 - gapc, s1 - gapc, s1 + w, s1 + w))
    return frame, None


FIG = {f'R{i}': fn for i, fn in enumerate([r1, r2, r3, r4, r5, r6, r7, r8, r9, r10], 1)}


def disc_parts(key, fav=False):
    """[(d, role)] for the mark: the disc minus every cut, then the tint shape (role 't')."""
    hole, tint = FIG[key](fav)
    hole = clip(hole, -1, -1, 101, 101)
    if tint:
        tint = clip(tint, 0, 0, 100, 100)
        return [(minus(DISC, hole, tint), 'm'), (minus(tint, hole), 't')]
    return [(minus(DISC, hole), 'm')]


# ====================================================================== concept metadata
C = {}


def concept(key, **meta):
    C[key] = meta


concept('R1', name='The braced tripod', group='Tripod disc', rim='Floats inside; touches nothing',
        reading="Round five's braced tripod cut clean through the disc: apex, spine, two struts, the braces and three round feet",
        palette='Deep Navy on White', L={'m': '#14284B', 'ink': '#14284B'}, D={'m': '#9DB4E6', 'ink': WORD_DARK},
        swatch=['#14284B', '#FFFFFF', '#141414'], font='inst-b', typeface='Instrument Sans Bold, lowercase',
        paper='#FFFFFF')
concept('R2', name='The tree of three', group='Tripod disc', rim='The root sits on the top rim; the terminals float',
        reading="Round five's tree of three, hung from the top of the disc: three lines fan out to three round holes, each with a solid disc standing inside",
        palette='Deep Green on Cream', L={'m': '#1D4636', 'ink': '#1D4636'}, D={'m': '#9CC9B0', 'ink': WORD_DARK},
        swatch=['#1D4636', CREAM, '#141414'], font='frau-sb', typeface='Fraunces SemiBold, lowercase', paper=CREAM)
concept('R3', name='The reduced tripod', group='Tripod disc', rim='The legs run out through the lower rim',
        reading='Spine and two struts only, no rings: the struts meet high, the spine stands apart under the apex, all three run out through the bottom of the disc',
        palette='Oxblood on Cream', L={'m': '#6B1E2A', 'ink': '#6B1E2A'}, D={'m': '#E5A0A8', 'ink': WORD_DARK},
        swatch=['#6B1E2A', CREAM, '#141414'], font='frau-sb', typeface='Fraunces SemiBold, lowercase', paper=CREAM)
concept('R4', name='The three feet', group='Tripod disc', rim='Floats inside, set low toward the rim',
        reading='The tripod with everything removed but its feet: three ring cuts set low in the disc, the dome above them standing in for the frame',
        palette='Ink on White', L={'m': '#141414', 'ink': '#141414'}, D={'m': '#F1EEE7', 'ink': '#F1EEE7'},
        swatch=['#141414', '#FFFFFF', '#F3F1EC'], font='inst-b', typeface='Instrument Sans Bold, lowercase',
        paper='#FFFFFF')
concept('R5', name='The reading line', group='Imagination', rim='The line breaks the left rim',
        reading='A line of reading enters from the left edge and stops, then a full point: a sentence, finished',
        palette='Press Red and Ink', L={'m': '#B3141C', 'ink': '#141414'}, D={'m': '#F0676C', 'ink': WORD_DARK},
        swatch=['#B3141C', '#FFFFFF', '#141414'], font='inst-b', typeface='Instrument Sans Bold, lowercase',
        paper='#FFFFFF')
concept('R6', name='The margin', group='Imagination', rim='The cut runs rim to rim',
        reading='One straight cut, off centre at the golden section: a narrow part and a broad part, the margin and the text block of a page',
        palette='Bronze on Cream', L={'m': '#8A6424', 'ink': '#141414'}, D={'m': '#D6B272', 'ink': WORD_DARK},
        swatch=['#8A6424', CREAM, '#141414'], font='frau-sb', typeface='Fraunces SemiBold, lowercase', paper=CREAM)
concept('R7', name='The spine and point', group='Imagination', rim='The spine breaks the top rim',
        reading='A spine with one terminal: a slot drops from the top edge into a round hole, and a solid point stands in the hole',
        palette='Ink on Cream', L={'m': '#141414', 'ink': '#141414'}, D={'m': '#F1EEE7', 'ink': '#F1EEE7'},
        swatch=['#141414', CREAM, '#FFFFFF'], font='frau-sb', typeface='Fraunces SemiBold, lowercase', paper=CREAM)
concept('R8', name='The crop', group='Imagination (two cut tones)', rim='Floats inside',
        reading="Two shapes meeting across an empty centre: two right-angle brackets, like a printer's crop marks; one cut clean through, the other cut as a lighter tone",
        palette='Blue, Black and White', L={'m': '#1F3FBF', 't': '#A9B6EC', 'ink': '#141414'},
        D={'m': '#8EA2FF', 't': '#3A4A8C', 'ink': WORD_DARK},
        swatch=['#1F3FBF', '#A9B6EC', '#141414', '#FFFFFF'], font='inst-b',
        typeface='Instrument Sans Bold, lowercase', paper='#FFFFFF')
concept('R9', name='The joint', group='Imagination', rim='The cut runs rim to rim, top to bottom',
        reading='A split that jogs at the centre: two halves of one disc that lock into each other, neither complete alone',
        palette='Deep Green on White', L={'m': '#1D4636', 'ink': '#1D4636'}, D={'m': '#9CC9B0', 'ink': WORD_DARK},
        swatch=['#1D4636', '#FFFFFF', '#141414'], font='inst-b', typeface='Instrument Sans Bold, lowercase',
        paper='#FFFFFF')
concept('R10', name='The open square', group='Imagination', rim='Floats inside',
        reading='A square channel cut into the round, open at one corner: the made thing inside the human one, not quite closed',
        palette='Deep Navy on Cream', L={'m': '#14284B', 'ink': '#14284B'}, D={'m': '#9DB4E6', 'ink': WORD_DARK},
        swatch=['#14284B', CREAM, '#141414'], font='frau-sb', typeface='Fraunces SemiBold, lowercase', paper=CREAM)


# ====================================================================== files
def colors(mode, c):
    if mode == 'mono':
        return {'m': 'currentColor', 't': 'currentColor', 'ink': 'currentColor'}
    return c['L'] if mode == 'light' else c['D']


def parts_for(key, mode, fav=False):
    """In one colour the tint cannot exist, so the lighter cut becomes a true hole."""
    parts = disc_parts(key, fav)
    if mode == 'mono':
        parts = [(d, r) for d, r in parts if r != 't']
    return parts


def body(parts, col, s=1.0, dx=0.0, dy=0.0):
    return ''.join(P(shift(d, dx, dy, s) if (s != 1 or dx or dy) else d, col[r]) for d, r in parts)


def mark_svg(key, mode, fav=False, label='userandproduct mark'):
    col = colors(mode, C[key])
    return svg((-1, -1, 102, 102) if not fav else (0, 0, 100, 100), body(parts_for(key, mode, fav), col), label)


def lockup_svg(key, mode, label='userandproduct'):
    c = C[key]
    col = colors(mode, c)
    cap = caph(c['font'])
    wd, wb = word('userandproduct', c['font'], -10)
    H = cap * 1.62           # disc diameter
    yc = -cap * 0.42         # centred a little below the cap middle, on the lowercase body
    s = H / 100
    gap = cap * 0.46
    b = body(parts_for(key, mode), col, s, 0, yc - H / 2)
    b += P(shift(wd, H + gap, 0), col['ink'])
    top, bot = min(yc - H / 2, wb[1]), max(yc + H / 2, wb[3])
    return svg(fitbox(0, top, H + gap + wb[2], bot, 4), b, label)


def avatar_svg(key):
    c = C[key]
    b = P(rect(0, 0, 100, 100), c['paper']) + body(parts_for(key, 'light'), c['L'])
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


def sheet(path):
    """All marks at 160px, the favicon art at 32px and 16px, and 16px enlarged 6x, on white."""
    keys = list(C)
    W, rowh = 160 + 40 + 32 + 40 + 16 + 40 + 96 + 40, 200
    img = Image.new('RGB', (W, rowh * len(keys)), 'white')
    for i, k in enumerate(keys):
        y = i * rowh + 20
        big = Image.open(io.BytesIO(bytes(resvg_py.svg_to_bytes(svg_string=mark_svg(k, 'light'), width=160, height=160))))
        img.paste(big, (20, y), big.convert('RGBA'))
        fav = mark_svg(k, 'light', True)
        x = 220
        for sz in (32, 16):
            t = Image.open(io.BytesIO(bytes(resvg_py.svg_to_bytes(svg_string=fav, width=sz, height=sz)))).convert('RGBA')
            img.paste(t, (x, y + 60), t)
            if sz == 16:
                z = t.resize((96, 96), Image.NEAREST)
                img.paste(z, (x + 56, y + 30), z)
            x += sz + 40
    img.save(path)


if __name__ == '__main__':
    args = sys.argv[1:]
    if args and args[0] == '--sheet':
        sheet(args[1] if len(args) > 1 else os.path.join(HERE, 'sheet.png'))
        sys.exit(0)
    keys = [a.upper() for a in args] or list(C)
    build(keys)
    if os.path.exists(os.path.join(HERE, 'board6.py')):
        import board6
        board6.write(C, OUT)
    print('built', ', '.join(keys))
