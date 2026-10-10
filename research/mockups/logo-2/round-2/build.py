"""Build round 2 of the second logo exploration: masters, dark variants, avatars, lockups,
32 px favicons, thumb tiles and the board (index.html).

Run from anywhere:  python build.py
Needs Python 3 with fontTools, uharfbuzz, skia-pathops, resvg-py and Pillow, and the Inter Display
Bold font in research/mockups/fonts/inter/.
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import pathops
import resvg_py
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from PIL import Image

import marks as M
from geo import d_of, transform, op, union, f as fmt
from info import INFO

SVG_DIR = os.path.join(HERE, 'svg')
PNG_DIR = os.path.join(HERE, 'png')
FONT = os.path.join(HERE, '..', '..', 'fonts', 'inter', 'InterDisplay-Bold.ttf')
WHITE, BLACK = '#FFFFFF', '#0B0B0C'
INK_LIGHT, INK_DARK = '#0B0B0C', '#F1EEE7'

# Palettes by family. 'c' container, 'a' first tone, 'b' second tone, 'f' fold (the overlap).
PAL = {
    'blue': {
        'contained': {'c': '#2B46A0', 'a': '#FFFFFF', 'b': '#8EA2FF', 'f': '#C9D3FF'},
        'contained-dark': {'c': '#3653C4', 'a': '#FFFFFF', 'b': '#8EA2FF', 'f': '#C9D3FF'},
        'free': {'a': '#2B46A0', 'b': '#4D6CF0', 'f': '#9DB2FF'},
        'free-dark': {'a': '#5B77EE', 'b': '#9AAEFF', 'f': '#DCE2FF'},
    },
    'green': {
        'contained': {'c': '#0E5A49', 'a': '#FFFFFF', 'b': '#5FC7A6', 'f': '#B5E9D7'},
        'contained-dark': {'c': '#137A62', 'a': '#FFFFFF', 'b': '#5FC7A6', 'f': '#B5E9D7'},
        'free': {'a': '#0E5A49', 'b': '#1F9277', 'f': '#7FD6BA'},
        'free-dark': {'a': '#2A9A7E', 'b': '#5FC7A6', 'f': '#C3EFE0'},
    },
    'vermilion': {
        'contained': {'c': '#B8321C', 'a': '#FFFFFF', 'b': '#FF9C84', 'f': '#FFD0C3'},
        'contained-dark': {'c': '#CF3E25', 'a': '#FFFFFF', 'b': '#FF9C84', 'f': '#FFD0C3'},
        'free': {'a': '#B8321C', 'b': '#EE5A3A', 'f': '#FFB39E'},
        'free-dark': {'a': '#E0533A', 'b': '#FF8A6E', 'f': '#FFD5C9'},
    },
}

# Thumb tile colours, from the thumbnail generator's palette, one per mark.
TILES = ['#FF5A36', '#14B8A6', '#6B4CFF', '#E9FF3B', '#121A3A',
         '#FF8A1F', '#3DDC84', '#2F5BFF', '#FF5CA8', '#F4F1E8']


def lum(hexc):
    r, g, b = (int(hexc[i:i + 2], 16) / 255 for i in (1, 3, 5))
    c = lambda v: v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * c(r) + 0.7152 * c(g) + 0.0722 * c(b)


def contrast(x, y):
    a, b = sorted((lum(x), lum(y)), reverse=True)
    return (a + 0.05) / (b + 0.05)


def svg_doc(body, vb='0 0 512 512', label='userandproduct'):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="%s" role="img" aria-label="%s">\n'
            '<title>%s</title>\n%s</svg>\n' % (vb, label, label, body))


def d_c(p):
    return d_of(p, coarse=True)


def paths(layers, pal, coarse=False):
    out = []
    for role, p in layers:
        d = d_of(p, coarse)
        if d:
            out.append('<path fill="%s" d="%s"/>' % (pal[role], d))
    return '\n'.join(out) + '\n'


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(text)


def png(svg, w, h, bg=None):
    data = resvg_py.svg_to_bytes(svg_string=svg, width=int(w), height=int(h), background=bg)
    return Image.open(io.BytesIO(bytes(data))).convert('RGBA')


def ink_bounds(layers):
    return union(*[q for _, q in layers]).bounds


def fit(layers, box, cx=256, cy=256):
    """Scale and centre layers so their ink fits a box x box square around cx, cy."""
    x0, y0, x1, y1 = ink_bounds(layers)
    s = box / max(x1 - x0, y1 - y0)
    return [(r, transform(p, sx=s, tx=cx - (x0 + x1) / 2 * s, ty=cy - (y0 + y1) / 2 * s)) for r, p in layers]


def scale_about(layers, k, cx=256, cy=256):
    return [(r, transform(p, sx=k, tx=cx - cx * k, ty=cy - cy * k)) for r, p in layers]


def clip(layers, shape):
    return [(r, op(p, shape, 'inter')) for r, p in layers]


# ---------------------------------------------------------------- wordmark

_WORD = None


def wordmark_glyphs():
    """'userandproduct' in Inter Display Bold, 100 units per em, y down, baseline 0, kerned by HarfBuzz."""
    global _WORD
    if _WORD:
        return _WORD
    font = TTFont(FONT)
    upm = font['head'].unitsPerEm
    gs = font.getGlyphSet()
    hbf = hb.Font(hb.Face(hb.Blob.from_file_path(FONT)))
    buf = hb.Buffer()
    buf.add_str('userandproduct')
    buf.guess_segment_properties()
    hb.shape(hbf, buf, {})
    order = font.getGlyphOrder()
    s = 100.0 / upm
    x = 0
    out = []
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        p = pathops.Path()
        gs[order[info.codepoint]].draw(p.getPen())
        out.append(transform(p, sx=s, sy=-s, tx=(x + pos.x_offset) * s))
        x += pos.x_advance
    _WORD = (out, x * s)
    return _WORD


CAP = 72.75


def custom_u_word():
    """Wordmark-forward idea: the first u of the name with its right stem folded like a page corner."""
    glyphs, _ = wordmark_glyphs()
    u = glyphs[0]
    x0, y0, x1, y1 = u.bounds
    body, flap = M.dog_ear(u, (x1 - x0) * 0.30 * 0.92)
    return [('a', body), ('f', flap)], union(*glyphs[1:])


def lockup_svg(layers, pal, ink, mono=None, custom=False, keep=()):
    """Mark + wordmark with the final-logo geometry: mark 1.4 cap heights tall, centred 31.08 units
    above the baseline, gap 0.40 of the mark height. mono: one colour (contained marks knocked out)."""
    glyphs, adv = wordmark_glyphs()
    pad = 3
    if custom:
        ul, rest = custom_u_word()
        if mono:
            body = '<path fill="%s" d="%s"/>\n' % (mono, d_c(union(*[p for _, p in ul], rest)))
        else:
            body = paths(ul, pal, True) + '<path fill="%s" d="%s"/>\n' % (ink, d_c(rest))
        x0, y0, x1, y1 = union(*[p for _, p in ul], rest).bounds
        vb = '%s %s %s %s' % (fmt(x0 - pad), fmt(y0 - pad), fmt(x1 - x0 + 2 * pad), fmt(y1 - y0 + 2 * pad))
        return svg_doc(body, vb)
    H = 1.4 * CAP
    cont = any(r == 'c' for r, _ in layers)
    bx0, by0, bx1, by1 = (0, 0, 512, 512) if cont else ink_bounds(layers)
    s = H / (by1 - by0)
    mw = (bx1 - bx0) * s
    cy = -31.08
    placed = [(r, transform(p, sx=s, tx=-bx0 * s, ty=cy - (by0 + by1) / 2 * s)) for r, p in layers]
    gap = 0.40 * H
    word = transform(union(*glyphs), tx=mw + gap)
    if mono:
        if cont:
            # knock the letter out of the container; parts that are counters (keep) stay filled
            solid = union(*[p for r, p in placed if r == 'c' or r in keep])
            mk = op(solid, union(*[p for r, p in placed if r != 'c' and r not in keep]), 'diff')
        else:
            mk = union(*[p for _, p in placed])
        body = '<path fill="%s" d="%s"/>\n<path fill="%s" d="%s"/>\n' % (mono, d_c(mk), mono, d_c(word))
    else:
        body = paths(placed, pal, True) + '<path fill="%s" d="%s"/>\n' % (ink, d_c(word))
    top = cy - H / 2
    vb = '%s %s %s %s' % (fmt(-pad), fmt(top - pad), fmt(mw + gap + adv + 2 * pad), fmt(H + 2 * pad))
    return svg_doc(body, vb)


# ---------------------------------------------------------------- per mark

def build_mark(i, fn):
    n = '%02d' % (i + 1)
    meta = INFO[i]
    fam = meta['colour']
    cont, layers = fn()
    key = 'contained' if cont else 'free'
    light, dark = PAL[fam][key], PAL[fam][key + '-dark']
    stem = 'r2-%s' % n
    files = {'mark': svg_doc(paths(layers, light)), 'mark-dark': svg_doc(paths(layers, dark))}
    # avatars: the container colour fills the avatar, the letter sits in reverse tones
    glyph = [(r, p) for r, p in layers if r != 'c']
    for shape_name, shape in (('circle', M.disc()), ('square', M.squircle())):
        if cont == 'circle':
            g = glyph
        elif cont == 'squircle':
            g = glyph if shape_name == 'square' else scale_about(glyph, 0.86)
        else:
            g = fit(glyph, 296 if shape_name == 'circle' else 316)
        g = clip(g, shape)
        for suffix, pal in (('', PAL[fam]['contained']), ('-dark', PAL[fam]['contained-dark'])):
            body = '<path fill="%s" d="%s"/>\n' % (pal['c'], d_of(shape)) + paths(g, pal)
            files['avatar-%s%s' % (shape_name, suffix)] = svg_doc(body)
    custom = bool(meta.get('wordmark'))
    files['lockup'] = lockup_svg(layers, light, INK_LIGHT, custom=custom)
    files['lockup-dark'] = lockup_svg(layers, dark, INK_DARK, custom=custom)
    files['lockup-white'] = lockup_svg(layers, light, None, mono='#FFFFFF', custom=custom, keep=meta.get('mono_keep', ()))
    files['lockup-black'] = lockup_svg(layers, light, None, mono='#0B0B0C', custom=custom, keep=meta.get('mono_keep', ()))
    for k, v in files.items():
        write(os.path.join(SVG_DIR, '%s-%s.svg' % (stem, k)), v)
    # favicons on their grounds, rendered at size (never a scaled SVG)
    for size in (32, 16):
        for ground, svg in (('light', files['mark']), ('dark', files['mark-dark'])):
            im = Image.new('RGBA', (size, size), WHITE if ground == 'light' else BLACK)
            im.alpha_composite(png(svg, size, size))
            im.convert('RGB').save(os.path.join(PNG_DIR, '%s-%d-%s.png' % (stem, size, ground)))
    # thumb tile: 600 x 338, lockup 120 px wide, 20 px in, bottom-left, black or white at 92 percent
    tile = TILES[i]
    col = 'white' if contrast('#FFFFFF', tile) > contrast('#0B0B0C', tile) else 'black'
    lk = files['lockup-' + col]
    vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', lk).group(1).split()]
    lw = 120.0
    lh = lw * vb[3] / vb[2]
    inner = re.sub(r'^.*?</title>\n', '', lk, flags=re.S).replace('</svg>\n', '')
    thumb = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 338">'
             '<rect width="600" height="338" fill="%s"/>'
             '<g opacity="0.92" transform="translate(20 %s) scale(%.5f) translate(%s %s)">%s</g></svg>' % (
                 tile, fmt(338 - 20 - lh), lw / vb[2], fmt(-vb[0]), fmt(-vb[1]), inner))
    png(thumb, 1200, 676).convert('RGB').save(os.path.join(PNG_DIR, '%s-thumb.png' % stem), optimize=True)
    return {'n': n, 'stem': stem, 'container': cont or 'free', 'tile': tile, 'thumb_ink': col, 'meta': meta}


def main():
    os.makedirs(PNG_DIR, exist_ok=True)
    built = [build_mark(i, fn) for i, fn in enumerate(M.MARKS)]
    from board import board
    write(os.path.join(HERE, 'index.html'), board(built))
    print('built %d marks' % len(built))


if __name__ == '__main__':
    main()
