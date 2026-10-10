"""Build round 3 of the second logo exploration: masters, dark variants, monochrome and single-colour
versions, avatars (circle, rounded square, LinkedIn square), lockups, favicons (colour and monochrome),
thumb tiles and the board (index.html).

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
from geo import d_of, transform, op, union, f as fmt, rect
from info import INFO

SVG_DIR = os.path.join(HERE, 'svg')
PNG_DIR = os.path.join(HERE, 'png')
FONT = os.path.join(HERE, '..', '..', 'fonts', 'inter', 'InterDisplay-Bold.ttf')
WHITE, NEAR_BLACK = '#FFFFFF', '#0B0B0C'
PURE_BLACK = '#000000'
INK_LIGHT, INK_DARK = '#0B0B0C', '#F1EEE7'

# Palettes by family. 'c' container or coin body, 'a' first tone, 'b' second tone, 'f' fold.
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
    'oxblood': {
        'contained': {'c': '#6E1F2A', 'a': '#FFFFFF', 'b': '#D98A95', 'f': '#F2C9CF'},
        'contained-dark': {'c': '#8E2A38', 'a': '#FFFFFF', 'b': '#D98A95', 'f': '#F2C9CF'},
        'free': {'a': '#6E1F2A', 'b': '#A83A4A', 'f': '#E59AA6'},
        'free-dark': {'a': '#C2505F', 'b': '#E48593', 'f': '#F6D3D8'},
    },
    'plum': {
        'contained': {'c': '#4B2A7A', 'a': '#FFFFFF', 'b': '#A88BE0', 'f': '#D8CBF4'},
        'contained-dark': {'c': '#5E37A0', 'a': '#FFFFFF', 'b': '#A88BE0', 'f': '#D8CBF4'},
        'free': {'a': '#4B2A7A', 'b': '#7A55C0', 'f': '#C2AEEC'},
        'free-dark': {'a': '#9472D8', 'b': '#B9A0EC', 'f': '#E6DDFA'},
    },
}

# Thumb tile colours from the thumbnail generator's palette, one per mark, in rotation.
TILES = ['#FF5A36', '#14B8A6', '#6B4CFF', '#E9FF3B', '#121A3A', '#FF8A1F', '#3DDC84', '#2F5BFF',
         '#FF5CA8', '#F4F1E8', '#16151A', '#1C1426']


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


def paths(layers, pal, coarse=False):
    out = []
    for role, p in layers:
        if role == 'h':
            continue
        d = d_of(p, coarse)
        if d:
            out.append('<path fill="%s" d="%s"/>' % (pal[role], d))
    return '\n'.join(out) + '\n'


def one(p, colour, coarse=False):
    return '<path fill="%s" d="%s"/>\n' % (colour, d_of(p, coarse))


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(text)


def png(svg, w, h):
    data = resvg_py.svg_to_bytes(svg_string=svg, width=int(w), height=int(h))
    return Image.open(io.BytesIO(bytes(data))).convert('RGBA')


def on_ground(svg, size, ground):
    im = Image.new('RGBA', (size, size), ground)
    im.alpha_composite(png(svg, size, size))
    return im.convert('RGB')


def ink_bounds(layers):
    return union(*[q for r, q in layers if r != 'h']).bounds


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


def lockup_svg(m, pal, ink, mono=None):
    """Mark + wordmark with the final-logo geometry: mark 1.4 cap heights tall, centred 31.08 units
    above the baseline, gap 0.40 of the mark height. mono: one colour, using the mark's mono path."""
    glyphs, adv = wordmark_glyphs()
    pad = 3
    H = 1.4 * CAP
    layers = m['layers']
    boxed = m['kind'] in ('circle', 'squircle', 'coin')
    bx0, by0, bx1, by1 = (0, 0, 512, 512) if boxed else ink_bounds(layers)
    s = H / (by1 - by0)
    mw = (bx1 - bx0) * s
    cy = -31.08
    T = lambda p: transform(p, sx=s, tx=-bx0 * s, ty=cy - (by0 + by1) / 2 * s)
    gap = 0.40 * H
    word = transform(union(*glyphs), tx=mw + gap)
    if mono:
        body = one(T(m['mono']), mono, True) + one(word, mono, True)
    else:
        body = paths([(r, T(p)) for r, p in layers], pal, True) + one(word, ink, True)
    top = cy - H / 2
    vb = '%s %s %s %s' % (fmt(-pad), fmt(top - pad), fmt(mw + gap + adv + 2 * pad), fmt(H + 2 * pad))
    return svg_doc(body, vb)


# ---------------------------------------------------------------- per mark

def avatar_glyph(m, shape_name):
    """The mark's layers placed for an avatar of the given shape; the avatar itself is the container."""
    kind, layers = m['kind'], m['layers']
    if kind == 'coin':
        return [(r, p) for r, p in layers if r != 'c']
    glyph = [(r, p) for r, p in layers if r != 'c']
    if kind == 'circle':
        return glyph
    if kind == 'squircle':
        return glyph if shape_name != 'circle' else scale_about(glyph, 0.86)
    if kind == 'shape':
        glyph = [('a' if r == 'c' else r, p) for r, p in layers]
    return fit(glyph, 300 if shape_name == 'circle' else 316)


def avatar_svg(m, shape, shape_name, pal):
    g = clip(avatar_glyph(m, shape_name), shape)
    body = one(shape, pal['c'])
    for r, p in g:
        if r == 'h':
            body += one(p, '#FFFFFF')
    body += paths(g, pal)
    return svg_doc(body)


def build_mark(i, fn):
    n = '%02d' % (i + 1)
    meta = INFO[i]
    fam = meta['colour']
    m = fn()
    kind = m['kind']
    key = 'free' if kind is None else 'contained'
    light, dark = PAL[fam][key], PAL[fam][key + '-dark']
    main = PAL[fam]['contained']['c']
    stem = 'r3-%s' % n
    files = {
        'mark': svg_doc(paths(m['layers'], light)),
        'mark-dark': svg_doc(paths(m['layers'], dark)),
        'mono-black': svg_doc(one(m['mono'], PURE_BLACK)),
        'mono-white': svg_doc(one(m['mono'], '#FFFFFF')),
        'single': svg_doc(one(m['mono'], main)),
    }
    shapes = {'circle': M.disc(), 'square': M.squircle(), 'linkedin': rect(0, 0, 512, 512)}
    for shape_name, shape in shapes.items():
        for suffix, pal in (('', PAL[fam]['contained']), ('-dark', PAL[fam]['contained-dark'])):
            if shape_name == 'linkedin' and suffix:
                continue
            files['avatar-%s%s' % (shape_name, suffix)] = avatar_svg(m, shape, shape_name, pal)
    files['lockup'] = lockup_svg(m, light, INK_LIGHT)
    files['lockup-dark'] = lockup_svg(m, dark, INK_DARK)
    files['lockup-white'] = lockup_svg(m, light, None, mono='#FFFFFF')
    files['lockup-black'] = lockup_svg(m, light, None, mono='#0B0B0C')
    for k, v in files.items():
        write(os.path.join(SVG_DIR, '%s-%s.svg' % (stem, k)), v)
    # favicons rendered at size on their grounds (never a scaled SVG)
    for size in (32, 16):
        on_ground(files['mark'], size, WHITE).save(os.path.join(PNG_DIR, '%s-%d-light.png' % (stem, size)))
        on_ground(files['mark-dark'], size, NEAR_BLACK).save(os.path.join(PNG_DIR, '%s-%d-dark.png' % (stem, size)))
    png(files['mark'], 16, 16).save(os.path.join(PNG_DIR, '%s-16-tab-light.png' % stem))
    png(files['mark-dark'], 16, 16).save(os.path.join(PNG_DIR, '%s-16-tab-dark.png' % stem))
    on_ground(files['mono-black'], 32, WHITE).save(os.path.join(PNG_DIR, '%s-32-mono-light.png' % stem))
    on_ground(files['mono-white'], 32, PURE_BLACK).save(os.path.join(PNG_DIR, '%s-32-mono-dark.png' % stem))
    # thumb tile: 600 x 338, lockup 120 px wide, 20 px in, bottom-left, black or white at 92 percent
    tile = TILES[i % len(TILES)]
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
    holder = {'circle': 'Circle', 'squircle': 'Rounded square', 'shape': 'Shaped as the icon',
              None: 'Stands free'}[kind] if kind != 'coin' else (
        'Coin (circle)' if m['holder'] == 'circle' else 'Coin (rounded square)')
    return {'n': n, 'stem': stem, 'kind': kind, 'holder': holder, 'tile': tile, 'thumb_ink': col,
            'meta': meta, 'brand': main}


def main():
    os.makedirs(PNG_DIR, exist_ok=True)
    assert len(INFO) == len(M.MARKS)
    # remove files left by marks numbered past the current set (the round was redrawn and renumbered)
    for d in (SVG_DIR, PNG_DIR):
        for name in os.listdir(d):
            mt = re.match(r'r3-(\d\d)-', name)
            if mt and int(mt.group(1)) > len(M.MARKS):
                os.remove(os.path.join(d, name))
    built = [build_mark(i, fn) for i, fn in enumerate(M.MARKS)]
    from board import board
    write(os.path.join(HERE, 'index.html'), board(built))
    print('built %d marks' % len(built))


if __name__ == '__main__':
    main()
