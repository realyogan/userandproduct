"""The owner's mark, read from source/Logo-owner.svg, plus the color options, the gradients and the
wordmark. Everything else in this folder is built from what is defined here."""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MOCK = os.path.normpath(os.path.join(HERE, '..'))
sys.path.insert(0, os.path.join(MOCK, 'tools'))

import pathops  # noqa: E402
import resvg_py  # noqa: E402
from fontTools.pens.transformPen import TransformPen  # noqa: E402
from PIL import Image  # noqa: E402

import wordmark as WM  # noqa: E402

SOURCE = os.path.join(HERE, 'source', 'Logo-owner.svg')
FONT = os.path.join(MOCK, 'fonts', 'inter', 'InterDisplay-Bold.ttf')

# ------------------------------------------------------------------ the owner's geometry, read verbatim
_src = open(SOURCE, encoding='utf-8').read()
_c = re.search(r'<circle cx="([\d.]+)" cy="([\d.]+)" r="([\d.]+)"', _src)
CX, CY, R = (float(v) for v in _c.groups())
BAND_D, HEAD_D = re.findall(r'<path[^>]* d="([^"]+)"', _src)   # first the band, then the head
assert BAND_D.startswith('M1595.8') and HEAD_D.startswith('M1176.4'), 'source paths changed order'


def num(v):
    s = ('%.4f' % v).rstrip('0').rstrip('.')
    return '0' if s in ('-0', '') else s


# the circle as a path: four quarter arcs from the top, the same centre and radius as the owner's
# <circle>. (Two half arcs render up to 64 of 255 gray levels off along the edge; four quarter arcs
# match the owner's file pixel for pixel.)
_r = num(R)
DISC_D = 'M%s %sa%s %s 0 0 1 %s %sa%s %s 0 0 1-%s %sa%s %s 0 0 1-%s-%sa%s %s 0 0 1 %s-%sZ' % (
    num(CX), num(CY - R), _r, _r, _r, _r, _r, _r, _r, _r, _r, _r, _r, _r, _r, _r, _r, _r)
VB = '0 0 1920 1920'                                                               # the owner's canvas
VB_BLEED = '%s %s %s %s' % (num(CX - R), num(CY - R), num(2 * R), num(2 * R))      # the disc edge to edge

# ------------------------------------------------------------------ color tokens
WHITE, NEAR, INK, OFF = '#FFFFFF', '#111111', '#0B0B0C', '#F1EEE7'
BLACK_MONO, WHITE_MONO = '#0B0B0C', '#FFFFFF'
TILE = '#F4F1E8'   # the thumbnail tile, the same for every option

# disc: light mode; dark: the disc in dark mode; head, band: fills for the cut-outs (absent: a true hole)
OPTIONS = [
    dict(key='signal', name='Signal blue', disc='#2B46A0', dark='#8EA2FF',
         note='The house blue from the first logo pack; on dark it switches to the house dark-mode blue.'),
    dict(key='navy', name='Deep navy', disc='#1B2A55', dark='#A9B8E8',
         note='Darker and quieter than the signal blue; close to black at 16 px.'),
    dict(key='cobalt', name='Cobalt', disc='#2450D8', dark='#7A96FF',
         note='A brighter blue; the most energy of the three blues.'),
    dict(key='ink', name='Near-black ink', disc='#0B0B0C', dark='#F1EEE7',
         note='The same ink as the wordmark; flips to off-white on dark.'),
    dict(key='charcoal', name='Warm charcoal', disc='#3A3532', dark='#D8D0C8',
         note='Softer than ink, with a warm cast.'),
    dict(key='green', name='Deep green', disc='#0E5A49', dark='#5FC7A6',
         note='Calm and serious, a publisher green.'),
    dict(key='oxblood', name='Oxblood', disc='#6E1F2A', dark='#E48593',
         note='Deep red-brown; bookish and warm.'),
    dict(key='vermilion', name='Vermilion', disc='#D9411E', dark='#D9411E',
         note='The loudest option; the same red passes on white and on near-black.'),
    dict(key='plum', name='Plum', disc='#4B2A7A', dark='#B9A0EC',
         note='Dark purple; rare in the UX and product space.'),
    dict(key='teal', name='Teal', disc='#0F766E', dark='#3DC2B5',
         note='Blue-green; passes on both grounds, with a brighter teal on dark for more lift.'),
    dict(key='mustard', name='Mustard with a dark figure', disc='#E3A72F', dark='#E3A72F',
         head=INK, band=INK,
         note='The cut-outs are filled with ink, so the person is dark on yellow. The disc edge is soft on white.'),
    dict(key='twotone', name='Two-tone blue', disc='#2B46A0', dark='#2B46A0',
         head='#FFFFFF', band='#8EA2FF',
         note='Signal blue disc; the head in white, the band in the light blue, so the head carries the lighter tone.'),
]
for _o in OPTIONS:
    _o['group'] = 'first'

# added 10 Oct 2026 after the owner's first look; numbering continues (C13 on), nothing is renumbered
OPTIONS += [
    # blues, flat
    dict(key='azure', name='Azure', disc='#0B72D9', dark='#5BA8FF', group='blues',
         note='A clear, bright mid blue; passes on both grounds, with a lighter azure on dark for more lift.'),
    dict(key='royal', name='Royal blue', disc='#2F45C8', dark='#A8B8FF', group='blues',
         note='Between the signal blue and cobalt: deeper than cobalt, brighter than signal.'),
    dict(key='slate', name='Slate blue', disc='#475C80', dark='#B3C0DD', group='blues',
         note='A grayed blue; the quietest of the blues, close to a printed ink.'),
    dict(key='midnight', name='Midnight', disc='#0F1B3D', dark='#9AA7F0', group='blues',
         note='Almost black with a blue cast; reads as black at small sizes.'),
    dict(key='electric', name='Electric blue', disc='#2E5BFF', dark='#7DB0FF', group='blues',
         note='The most saturated blue; passes on both grounds, with a lighter blue on dark for more lift.'),
    # vibrant, flat
    dict(key='coral', name='Hot coral', disc='#E5432F', dark='#E5432F', group='vibrant',
         note='A hot red-orange; warmer than the vermilion and just as loud.'),
    dict(key='emerald', name='Emerald', disc='#0B8F63', dark='#0B8F63', group='vibrant',
         note='A bright, saturated green; one color for both grounds.'),
    dict(key='magenta', name='Magenta', disc='#D6247A', dark='#D6247A', group='vibrant',
         note='A strong pink-red; the most unusual of the vibrant set.'),
    dict(key='tangerine', name='Tangerine', disc='#D9600A', dark='#D9600A', group='vibrant',
         note='A deep orange, dark enough to carry a white figure.'),
    dict(key='lime', name='Lime with a dark figure', disc='#B5E61D', dark='#B5E61D', head=INK, band=INK,
         group='vibrant',
         note='Too light for a white figure, so the cut-outs are filled with ink, like the mustard.'),
]
for _i, _o in enumerate(OPTIONS, 1):
    _o['num'] = 'C%02d' % _i
    _o.setdefault('head', None)
    _o.setdefault('band', None)
    _o['grad'] = False

# gradients: diagonal, top left to bottom right; social backgrounds and avatars only, never on the site
GRADIENTS = [
    dict(key='g-signal-cobalt', name='Signal blue to cobalt', a='#3B63E6', b='#2B46A0',
         note='The smallest step: the house blue, lifted to cobalt in the top left corner.'),
    dict(key='g-navy-teal', name='Navy to teal', a='#0F766E', b='#1B2A55',
         note='Teal in the top left, deep navy in the bottom right.'),
    dict(key='g-plum-vermilion', name='Plum to vermilion', a='#D9411E', b='#4B2A7A',
         note='The warmest and the loudest: vermilion fading into plum.'),
    dict(key='g-charcoal-ink', name='Charcoal to ink', a='#4A4440', b='#0B0B0C',
         note='Almost flat: a warm charcoal glow on near-black.'),
]
for _g in GRADIENTS:
    _g['group'] = 'first'
GRADIENTS += [
    # blue gradients
    dict(key='g-azure-signal', name='Azure to signal blue', a='#0B72D9', b='#2B46A0', group='blues',
         note='A brighter, cleaner blue in the top left, settling into the house blue.'),
    dict(key='g-royal-midnight', name='Royal blue to midnight', a='#2F45C8', b='#0F1B3D', group='blues',
         note='The deepest of the blue gradients: royal fading to near-black.'),
    dict(key='g-electric-cobalt', name='Electric blue to cobalt', a='#2E5BFF', b='#2450D8', group='blues',
         note='Barely a gradient: a glow of electric blue over cobalt.'),
    dict(key='g-sky-navy', name='Sky to navy', a='#348FDD', b='#1B2A55', group='blues',
         note='The widest blue range: a light sky blue down to deep navy.'),
    dict(key='g-signal-indigo', name='Signal blue to indigo', a='#2B46A0', b='#3B2A8C', group='blues',
         note='The house blue turning toward purple in the bottom right.'),
    # vibrant gradients
    dict(key='g-coral-magenta', name='Coral to magenta', a='#E5432F', b='#C81E78', group='vibrant',
         note='Hot coral into a deep magenta.'),
    dict(key='g-emerald-teal', name='Emerald to teal', a='#0B8F63', b='#0F766E', group='vibrant',
         note='Green to blue-green; the calmest of the vibrant set.'),
    dict(key='g-tangerine-coral', name='Tangerine to coral', a='#D9600A', b='#E5432F', group='vibrant',
         note='Orange into red; the warmest gradient.'),
    dict(key='g-violet-electric', name='Violet to electric blue', a='#7B3FE4', b='#2E5BFF', group='vibrant',
         note='Purple to the most saturated blue.'),
    dict(key='g-magenta-violet', name='Magenta to violet', a='#D6247A', b='#6B2FD6', group='vibrant',
         note='Pink-red into a deep violet.'),
]
for _i, _g in enumerate(GRADIENTS, 1):
    _g['num'] = 'G%02d' % _i
    _g.update(disc='url(#%s)' % _g['key'], dark='url(#%s)' % _g['key'], grad=True, head=None, band=None)


# ------------------------------------------------------------------ contrast (WCAG 2)
def lum(hexc):
    h = hexc.lstrip('#')
    out = []
    for i in (0, 2, 4):
        c = int(h[i:i + 2], 16) / 255
        out.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * out[0] + 0.7152 * out[1] + 0.0722 * out[2]


def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


# ------------------------------------------------------------------ SVG writers
def doc(vb, body, label='userandproduct', defs=''):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="%s" role="img" aria-label="%s">'
            '<title>%s</title>%s%s</svg>\n' % (vb, label, label, defs, body))


def grad_def(o):
    if not o.get('grad'):
        return ''
    return ('<defs><linearGradient id="%s" x1="0" y1="0" x2="1" y2="1">'
            '<stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient></defs>'
            % (o['key'], o['a'], o['b']))


def mark_body(disc, head=None, band=None):
    """The disc with both cut-outs as true holes (evenodd), then any filled cut-out on top."""
    out = '<path fill="%s" fill-rule="evenodd" d="%s%s%s"/>' % (disc, DISC_D, BAND_D, HEAD_D)
    if band:
        out += '<path fill="%s" d="%s"/>' % (band, BAND_D)
    if head:
        out += '<path fill="%s" d="%s"/>' % (head, HEAD_D)
    return out


def mark_svg(o, mode='light', vb=VB, label='userandproduct mark'):
    disc = o['disc'] if mode == 'light' else o['dark']
    return doc(vb, mark_body(disc, o.get('head'), o.get('band')), label, grad_def(o))


def single_svg(o):
    """One color only: the disc in the option's color, both cut-outs empty."""
    return doc(VB, mark_body(o['disc']), 'userandproduct mark', grad_def(o))


def figure(o):
    """Head and band fills for an avatar: the option's own, else white."""
    return o.get('head') or WHITE, o.get('band') or WHITE


def avatar_svg(o, shape):
    """Social avatars, opaque like an upload. circle: the disc edge to edge; square: the disc color as a
    full square (LinkedIn, Apple touch icon); rounded: a rounded square. The figure keeps its place."""
    head, band = figure(o)
    x0 = CX - R
    if shape == 'circle':
        ground = '<path fill="%s" d="%s"/>' % (o['disc'], DISC_D)
    else:
        rx = ' rx="%s"' % num(2 * R * 0.22) if shape == 'rounded' else ''
        ground = '<rect x="%s" y="%s" width="%s" height="%s"%s fill="%s"/>' % (
            num(x0), num(x0), num(2 * R), num(2 * R), rx, o['disc'])
    body = ground + '<path fill="%s" d="%s"/><path fill="%s" d="%s"/>' % (band, BAND_D, head, HEAD_D)
    return doc(VB_BLEED, body, 'userandproduct', grad_def(o))


# ------------------------------------------------------------------ wordmark and lockups
_FONT = WM.FontRef(FONT)
CAP = _FONT.tt['OS/2'].sCapHeight * 100 / _FONT.upem
XH = _FONT.tt['OS/2'].sxHeight * 100 / _FONT.upem


def f1(v):
    s = ('%.1f' % v).rstrip('0').rstrip('.')
    return '0' if s in ('-0', '') else s


def _word():
    """'userandproduct' in Inter Display Bold, 100 units per em, kerned, tracking 0, one merged path,
    baseline at y 0, ink starting at x 0. Coordinates to 0.1 unit (a thousandth of an em)."""
    items = WM.layout(['userandproduct'], [_FONT], 100, 0)
    p = pathops.Path()
    for font, name, matrix in items[0]:
        font.glyphs[name].draw(TransformPen(p.getPen(), matrix))
    p.simplify()
    x0, y0, x1, y1 = p.bounds
    p = p.transform(1, 0, 0, 1, -x0, 0)
    pen = RelPen()
    p.draw(pen)
    return pen.d(), (0, y0, x1 - x0, y1)


class RelPen:
    """A pen that writes relative path commands to 0.1 unit, rounding the absolute points first so
    the error never adds up along a contour. Keeps the wordmark small enough for the 6 KB limit."""

    def __init__(self):
        self.out, self.cur, self.start = [], (0, 0), (0, 0)

    def _r(self, pt):
        return (round(pt[0] * 10), round(pt[1] * 10))

    def _rel(self, pts):
        s = ''
        for x, y in pts:
            for v in (x - self.cur[0], y - self.cur[1]):
                t = f1(v / 10)
                if s and not t.startswith('-'):
                    s += ' '
                s += t
        return s

    def moveTo(self, pt):
        pt = self._r(pt)
        self.out.append('m' + self._rel([pt]))
        self.cur = self.start = pt

    def lineTo(self, pt):
        pt = self._r(pt)
        self.out.append('l' + self._rel([pt]))
        self.cur = pt

    def curveTo(self, *pts):
        pts = [self._r(p) for p in pts]
        self.out.append('c' + self._rel(pts))
        self.cur = pts[-1]

    def qCurveTo(self, *pts):
        pts = [self._r(p) for p in pts]
        # split a run of off-curve points at their implied on-curve midpoints
        offs, end = pts[:-1], pts[-1]
        for i, c in enumerate(offs):
            if i == len(offs) - 1:
                nxt = end
            else:
                nxt = (round((c[0] + offs[i + 1][0]) / 2), round((c[1] + offs[i + 1][1]) / 2))
            self.out.append('q' + self._rel([c, nxt]))
            self.cur = nxt
    def closePath(self):
        self.out.append('z')
        self.cur = self.start

    endPath = closePath

    def d(self):
        return ''.join(self.out)


WORD_D, WB = _word()

# side lockup, the first pack's geometry (final-logo/build.py, decided 9 Oct 2026, owner feedback on this
# board 10 Oct 2026): the disc 1.4 cap heights across, about the wordmark's full ink height (ascender top
# to descender bottom, 93.2 units, so 1.09 of it); its centre midway between the cap band and the
# x-height band, 31.08 units above the baseline; gap 0.40 of the disc.
SIDE_D = 1.4 * CAP
SIDE_CY = -(CAP + XH) / 4
SIDE_GAP = 0.40
# the first version on this board, kept only for the before-and-after pair: the disc 1.12 cap heights,
# its bottom on the baseline with a 1.2 percent overshoot
BEFORE_D = 1.12 * CAP
BEFORE_CY = 0.012 * BEFORE_D - BEFORE_D / 2
# stacked lockup: the first pack's proportions, disc 3 cap heights, gap 0.76 cap heights
STACK_D, STACK_GAP = 3.0 * CAP, 0.76 * CAP
MARGIN = 4   # the first pack's margin around the ink


def _place(o, mode, x, y, d):
    """The mark at diameter d with its disc's top-left corner at x, y (lockup units)."""
    s = d / (2 * R)
    disc = o['disc'] if mode == 'light' else o['dark']
    return '<g transform="translate(%s %s) scale(%s)">%s</g>' % (
        f1(x - (CX - R) * s), f1(y - (CY - R) * s), num(s), mark_body(disc, o.get('head'), o.get('band')))


def lockup_svg(o, mode='light', word_fill=None, stacked=False, before=False):
    if word_fill is None:
        word_fill = INK if mode == 'light' else OFF
    m = MARGIN
    if stacked:
        d = STACK_D
        top = WB[1] - STACK_GAP - d
        body = _place(o, mode, (WB[2] - d) / 2, top, d) + '<path fill="%s" d="%s"/>' % (word_fill, WORD_D)
        vb = (-m, top - m, WB[2] + 2 * m, WB[3] - top + 2 * m)
    else:
        d, cy = (BEFORE_D, BEFORE_CY) if before else (SIDE_D, SIDE_CY)
        top = cy - d / 2
        gap = SIDE_GAP * d
        body = _place(o, mode, 0, top, d) + '<path fill="%s" transform="translate(%s 0)" d="%s"/>' % (
            word_fill, f1(d + gap), WORD_D)
        top_all, bot = min(top, WB[1]), max(top + d, WB[3])
        vb = (-m, top_all - m, d + gap + WB[2] + 2 * m, bot - top_all + 2 * m)
    return doc(' '.join(f1(v) for v in vb), body, 'userandproduct', grad_def(o))


def mono(color):
    return dict(key='mono', name='Monochrome', disc=color, dark=color, head=None, band=None, grad=False)


# ------------------------------------------------------------------ rendering
def png(svg, w, h=None):
    if h is None:
        m = re.search(r'viewBox="([^"]+)"', svg).group(1).split()
        h = round(w * float(m[3]) / float(m[2]))
    data = resvg_py.svg_to_bytes(svg_string=svg, width=int(w), height=int(h))
    return Image.open(io.BytesIO(bytes(data))).convert('RGBA')


def on(img, color):
    g = Image.new('RGBA', img.size, color)
    g.alpha_composite(img)
    return g.convert('RGB')
