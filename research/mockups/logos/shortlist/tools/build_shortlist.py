"""Build the logo shortlist: seven concepts reset on the final wordmark, plus two new marks.

THE WORDMARK IS FINAL, taken from P8 in round4/tools/build_round4.py: Inter Display Bold, lowercase
"userandproduct" as one word, tracking -25, one ink color (the concept's own), set beside the mark
with P8's side_lockup proportions (mark height 1.4 cap heights, centered on half the cap height, gap
0.38 cap heights).

The seven existing marks are read from their own files (paths and fills exactly as built) and only
the lockup is rebuilt. Marks, favicons and avatars are copied unchanged. The two new marks (NEW1 the
profile, NEW2 the sphere) are drawn in newmarks.py.

Run from anywhere:
    python build_shortlist.py           # every SVG, PNG and index.html
    python build_shortlist.py --sheet   # scratch contact sheet of the new marks (sheet.png here)
Files land in the parent folder, per concept id:
  <id>-lockup.svg, -lockup-dark.svg, -lockup-mono.svg, <id>-mark.svg, -mark-dark.svg, -mark-mono.svg,
  <id>-favicon.svg with -favicon-16.png and -32.png, <id>-avatar.svg with -avatar-400.png
  NEW1 also has <id>-lockup-alt.svg, -lockup-alt-dark.svg and -mark-alt.svg (oxblood).
"""
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from geom import (OUT, P, bounds, caph, fitbox, rect, render_avatar, resvg_py, shift, svg, word,  # noqa: E402
                  write)
import newmarks as N  # noqa: E402

LOGOS = os.path.normpath(os.path.join(OUT, '..'))
WHITE, CREAM, WORD_DARK = '#FFFFFF', '#F4EFE3', '#EEE9DF'

# ---------------------------------------------------------------- the final wordmark (P8)
FONT, TRACK = 'inter-b', -25
H_CAP, GAP_CAP = 1.4, 0.38
_word = None


def final_word():
    global _word
    if _word is None:
        _word = word('userandproduct', FONT, TRACK)
    return _word


def lockup(frags, ink, label='userandproduct'):
    """frags: [(d, fill)]. P8's side_lockup: mark scaled to 1.4 cap heights, centered on -cap/2."""
    wd, wb = final_word()
    cap = caph(FONT)
    H, yc, gap = cap * H_CAP, -cap / 2, cap * GAP_CAP
    bs = [bounds(d) for d, _ in frags]
    x0, y0 = min(b[0] for b in bs), min(b[1] for b in bs)
    x1, y1 = max(b[2] for b in bs), max(b[3] for b in bs)
    s = H / (y1 - y0)
    dx, dy = -x0 * s, yc - H / 2 - y0 * s
    mw = (x1 - x0) * s
    body = ''.join(P(shift(d, dx, dy, s), f) for d, f in frags) + P(shift(wd, mw + gap, 0), ink)
    top, bot = min(yc - H / 2, wb[1]), max(yc + H / 2, wb[3])
    return svg(fitbox(0, top, mw + gap + wb[2], bot, 4), body, label)


# ---------------------------------------------------------------- concepts
C = {}


def concept(key, **meta):
    C[key] = meta


concept('P8', src='round4', board='Round 4', name='The sliced disc', ref=True,
        reading='A black disc sliced once, upright, right of center; both pieces kept',
        palette='Black and White', swatch=['#0B0B0C', '#FFFFFF', '#F3F1EC'], paper=WHITE)
concept('P3', src='round4', board='Round 4', name='The serif monogram',
        reading='A heavy serif "up" reversed out of a deep navy square (the monogram keeps its Fraunces letters; only the name changed)',
        palette='Deep Navy and White', swatch=['#14284B', '#141414', '#FFFFFF'], paper=WHITE)
concept('P5', src='round4', board='Round 4', name='Square and disc',
        reading='A black square and a blue disc of one height, side by side, not touching',
        palette='Ink, Signal Blue and White', swatch=['#111111', '#1F3FBF', '#FFFFFF'], paper=WHITE)
concept('Q3', src='round5', board='Round 5', name='The tree of three',
        reading='Three terminals from one root: two hollow rings and a raised solid disc in the middle',
        palette='Deep Green on Cream', swatch=['#1D4636', CREAM, '#FFFFFF'], paper=CREAM)
concept('R4', src='round6', board='Round 6', name='The three feet',
        reading='Three ring cuts in a low row, the middle one dropped, cut from an ink disc',
        palette='Ink on White', swatch=['#141414', '#FFFFFF', '#F3F1EC'], paper=WHITE)
concept('R5', src='round6', board='Round 6', name='The reading line',
        reading='A bar enters from the left rim and stops square, then a full stop: a sentence, finished',
        palette='Press Red and Ink', swatch=['#B3141C', '#FFFFFF', '#141414'], paper=WHITE)
concept('S5', src='round7/tiles', board='Round 7 tiles', name='Two sizes',
        reading='Four filled tiles at 45 degrees, the diagonal pair large, the other pair small, each spun 12 degrees',
        palette='Oxblood on Cream', swatch=['#6B1E2A', CREAM, '#141414'], paper=CREAM)

INK_L, INK_D = {'m': '#141414', 'ink': '#141414'}, {'m': '#F1EEE7', 'ink': '#F1EEE7'}
OX_L, OX_D = {'m': '#6B1E2A', 'ink': '#6B1E2A'}, {'m': '#E5A0A8', 'ink': WORD_DARK}
NAVY_L, NAVY_D = {'m': '#14284B', 'ink': '#14284B'}, {'m': '#9DB4E6', 'ink': WORD_DARK}

for v, nm, rd in [
        ('A', 'The profile, angular',
         'A head in profile cut from an ink disc, facing right: eleven short straight cuts down the face '
         '(forehead, brow, nose, two lips, chin, jaw), a polygon skull and a slanted cameo neck line'),
        ('B', 'The profile, minimal',
         'The same head with the fewest cuts: forehead and nose in one long line, one lip step, chin, jaw; '
         'the skull three straight cuts, no round cranium, no eye'),
        ('C', 'The profile, breaking the rim',
         'Head A set larger and higher, so the crown runs out through the top of the disc: a bust rising '
         'out of a coin; the disc stays one open piece')]:
    concept('NEW1' + v, new='profile', variant=v, board='New', name=nm, reading=rd,
            palette='Ink on White (alternative: Oxblood)', swatch=['#141414', '#FFFFFF', '#6B1E2A'], paper=WHITE,
            L=INK_L, D=INK_D, alt=(OX_L, OX_D))

SPHERES = {'A': (34, 6, 36, 6.25), 'B': (35, 8, 37, 9.4), 'C': (36, 11, 38, 12.5)}   # s, g, favicon s, favicon g
for v, nm, rd in [
        ('A', 'The sphere, close',
         "T8's triangle of nine without its two bottom corner cells: seven cells cut from a navy disc, gaps of "
         "6 units (1px in the 16px favicon), the base cells clipped by the disc's inner edge so the cluster "
         "stands on the disc's own curve"),
        ('B', 'The sphere, open',
         'The same seven cells a little larger, gaps of 8 units (1.5px in the favicon): the lattice reads '
         'first, the cells second'),
        ('C', 'The sphere, wide',
         'Gaps of 11 units (2px in the favicon): the widest the lattice can go before the cells turn into '
         'scattered points at 16px')]:
    concept('NEW2' + v, new='sphere', variant=v, board='New', name=nm, reading=rd,
            palette='Deep Navy on White', swatch=['#14284B', '#FFFFFF', '#9DB4E6'], paper=WHITE,
            L=NAVY_L, D=NAVY_D)


# ---------------------------------------------------------------- reading the existing marks
PATH_RE = re.compile(r'<path fill="([^"]+)" d="([^"]+)"/>')


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def frags_of(svg_text):
    return [(d, fill) for fill, d in PATH_RE.findall(svg_text)]


def build_existing(k):
    c = C[k]
    m = k.lower()
    src = os.path.join(LOGOS, c['src'])
    for sfx in ('', '-dark', '-mono'):
        mark = read(os.path.join(src, f'{m}-mark{sfx}.svg'))
        old = frags_of(read(os.path.join(src, f'{m}-lockup{sfx}.svg')))
        ink = old[-1][1]            # the old wordmark's color: the concept's own ink in that mode
        write(f'{m}-lockup{sfx}.svg', lockup(frags_of(mark), ink))
        write(f'{m}-mark{sfx}.svg', mark)
    for fn in (f'{m}-favicon.svg', f'{m}-avatar.svg'):
        write(fn, read(os.path.join(src, fn)))
    for fn in (f'{m}-favicon-16.png', f'{m}-favicon-32.png', f'{m}-avatar-400.png'):
        shutil.copyfile(os.path.join(src, fn), os.path.join(OUT, fn))


# ---------------------------------------------------------------- the new marks
def new_disc(k, fav=False):
    c = C[k]
    if c['new'] == 'profile':
        return N.profile_disc(c['variant'], fav)
    s, g, fs, fg = SPHERES[c['variant']]
    return N.sphere_disc(fs, fg) if fav else N.sphere_disc(s, g)


def render_png(svg_text, path, size):
    data = bytes(resvg_py.svg_to_bytes(svg_string=svg_text, width=size, height=size))
    with open(path, 'wb') as f:
        f.write(data)


def build_new(k):
    c = C[k]
    m = k.lower()
    d = new_disc(k)
    for mode, sfx in (('light', ''), ('dark', '-dark'), ('mono', '-mono')):
        col = {'light': c['L'], 'dark': c['D']}.get(mode, {'m': 'currentColor', 'ink': 'currentColor'})
        write(f'{m}-lockup{sfx}.svg', lockup([(d, col['m'])], col['ink']))
        write(f'{m}-mark{sfx}.svg', svg((-1, -1, 102, 102), P(d, col['m']), 'userandproduct mark'))
    if c.get('alt'):
        al, ad = c['alt']
        write(f'{m}-lockup-alt.svg', lockup([(d, al['m'])], al['ink']))
        write(f'{m}-lockup-alt-dark.svg', lockup([(d, ad['m'])], ad['ink']))
        write(f'{m}-mark-alt.svg', svg((-1, -1, 102, 102), P(d, al['m']), 'userandproduct mark'))
    fav = svg((0, 0, 100, 100), P(new_disc(k, True), c['L']['m']), 'userandproduct')
    write(f'{m}-favicon.svg', fav)
    for sz in (16, 32):
        render_png(fav, os.path.join(OUT, f'{m}-favicon-{sz}.png'), sz)
    # avatar: the disc at 84 percent on the paper, so the rim still reads inside the circle crop
    s = 0.84
    av = svg((0, 0, 100, 100), P(rect(0, 0, 100, 100), c['paper']) +
             P(shift(d, 50 - 50 * s, 50 - 50 * s, s), c['L']['m']), 'userandproduct avatar')
    write(f'{m}-avatar.svg', av)
    render_avatar(av, os.path.join(OUT, f'{m}-avatar-400.png'))


def build():
    for k, c in C.items():
        (build_new if c.get('new') else build_existing)(k)


def contact_sheet(path):
    import sheet
    rows = [(new_disc(k), new_disc(k, True)) for k in C if C[k].get('new')]
    sheet.sheet(rows, path)


if __name__ == '__main__':
    if sys.argv[1:2] == ['--sheet']:
        contact_sheet(sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, 'sheet.png'))
        sys.exit(0)
    build()
    import board
    board.write(C, OUT)
    print('built', ', '.join(C))
