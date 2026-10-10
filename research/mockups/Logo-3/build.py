"""Build Logo 3: the owner's mark in a clean master, monochrome, twelve color options and four gradient
options, each with its dark variant, avatars, lockups (side and stacked), favicons, a thumbnail tile, the
board (index.html) and the export folder for the signal blue option.

Run from anywhere:  python build.py      then:  python check.py
Needs Python 3 with fontTools, uharfbuzz, skia-pathops, resvg-py, Pillow and numpy, plus
research/mockups/tools/wordmark.py and research/mockups/fonts/inter/. The owner's Logo.svg is never
touched; the geometry is read from source/Logo-owner.svg (geo.py).
"""
import os
import re
import shutil

import numpy as np
from PIL import Image

import geo as G

HERE = G.HERE
SVG, PNG, EXP = (os.path.join(HERE, d) for d in ('svg', 'png', 'export'))


def write(rel, text):
    p = os.path.join(HERE, *rel.split('/'))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(text)


def save(rel, img, **kw):
    p = os.path.join(HERE, *rel.split('/'))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    img.save(p, optimize=True, **kw)


def dither(img):
    """Add under one gray level of noise to the color channels so a gradient never bands, then
    quantise to 8 bits. Alpha is left alone."""
    a = np.asarray(img.convert('RGBA')).astype(np.float32)
    rng = np.random.default_rng(7)
    a[..., :3] += rng.uniform(-0.5, 0.5, a[..., :3].shape)
    return Image.fromarray(np.clip(np.rint(a), 0, 255).astype(np.uint8), 'RGBA')


def hi_png(svg, w, h=None, grad=False):
    """Render at four times the size and step down, so gradients are smooth; dither gradients."""
    img = G.png(svg, w * 4, None if h is None else h * 4)
    img = img.resize((w, img.size[1] // 4), Image.LANCZOS)
    return dither(img) if grad else img


# ------------------------------------------------------------------ shared masters
def build_masters():
    black = G.mono(G.BLACK_MONO)
    white = G.mono(G.WHITE_MONO)
    out = {
        # the clean master: the owner's geometry, the cut-outs as true holes, black like the owner's file
        'svg/mark.svg': G.doc(G.VB, G.mark_body('#000000'), 'userandproduct mark'),
        # the same with the cut-outs filled white, for photos and busy backgrounds
        'svg/mark-solid.svg': G.doc(G.VB, '<path fill="#000000" d="%s"/><path fill="#FFFFFF" d="%s"/>'
                                    '<path fill="#FFFFFF" d="%s"/>' % (G.DISC_D, G.BAND_D, G.HEAD_D),
                                    'userandproduct mark'),
        'svg/mark-currentcolor.svg': G.doc(G.VB, G.mark_body('currentColor'), 'userandproduct mark'),
        'svg/mark-black.svg': G.mark_svg(black),
        'svg/mark-white.svg': G.mark_svg(white),
        'svg/lockup-black.svg': G.lockup_svg(black, word_fill=G.BLACK_MONO),
        'svg/lockup-white.svg': G.lockup_svg(white, word_fill=G.WHITE_MONO),
        'svg/stacked-black.svg': G.lockup_svg(black, word_fill=G.BLACK_MONO, stacked=True),
        'svg/stacked-white.svg': G.lockup_svg(white, word_fill=G.WHITE_MONO, stacked=True),
    }
    for k, v in out.items():
        write(k, v)
    # monochrome favicons, rendered at size on their grounds
    for size in (16, 32):
        save('png/mono/fav-%d-black.png' % size,
             G.on(G.png(G.mark_svg(black, vb=G.VB_BLEED), size, size), G.WHITE))
        save('png/mono/fav-%d-white.png' % size,
             G.on(G.png(G.mark_svg(white, vb=G.VB_BLEED), size, size), '#000000'))
    # large previews of the master for the top of the board
    return out


# ------------------------------------------------------------------ one option
def thumb_png(o):
    lk = G.lockup_svg(o)
    vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', lk).group(1).split()]
    lw = 120.0
    lh = lw * vb[3] / vb[2]
    inner = re.sub(r'^.*?</title>', '', lk, flags=re.S).replace('</svg>\n', '')
    tile = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 338">'
            '<rect width="600" height="338" fill="%s"/>'
            '<g transform="translate(20 %s) scale(%.5f) translate(%s %s)">%s</g></svg>' % (
                G.TILE, G.f1(338 - 20 - lh), lw / vb[2], G.f1(-vb[0]), G.f1(-vb[1]), inner))
    return hi_png(tile, 1200, 676, o['grad']).convert('RGB')


def build_option(o):
    k = o['key']
    files = {
        'mark': G.mark_svg(o, 'light'),
        'mark-dark': G.mark_svg(o, 'dark'),
        'avatar-circle': G.avatar_svg(o, 'circle'),
        'avatar-rounded': G.avatar_svg(o, 'rounded'),
        'avatar-square': G.avatar_svg(o, 'square'),
        'lockup': G.lockup_svg(o, 'light'),
        'lockup-dark': G.lockup_svg(o, 'dark'),
        'stacked': G.lockup_svg(o, 'light', stacked=True),
        'stacked-dark': G.lockup_svg(o, 'dark', stacked=True),
    }
    if o['head'] or o['band']:
        files['single'] = G.single_svg(o)
    for name, text in files.items():
        write('svg/%s/%s.svg' % (k, name), text)
    bleed_l = G.mark_svg(o, 'light', vb=G.VB_BLEED)
    bleed_d = G.mark_svg(o, 'dark', vb=G.VB_BLEED)
    g = o['grad']
    for size in (16, 32):
        # favicons rendered at their own size (never a scaled-down large PNG), on white and near-black
        save('png/%s/fav-%d-light.png' % (k, size), G.on(G.png(bleed_l, size, size), G.WHITE))
        save('png/%s/fav-%d-dark.png' % (k, size), G.on(G.png(bleed_d, size, size), G.NEAR))
    # the tab icons stay transparent, so the tab color shows through the cut-outs
    save('png/%s/tab-16-light.png' % k, G.png(bleed_l, 16, 16))
    save('png/%s/tab-16-dark.png' % k, G.png(bleed_d, 16, 16))
    save('png/%s/thumb.png' % k, thumb_png(o))
    if g:
        # gradient avatars as PNG at twice the board size, smooth and dithered
        for shape in ('circle', 'rounded', 'square'):
            save('png/%s/avatar-%s-440.png' % (k, shape), hi_png(files['avatar-' + shape], 440, 440, True))
    return files


# ------------------------------------------------------------------ the export folder (signal blue)
FAVICON_SVG = None


def build_export():
    o = G.OPTIONS[0]
    if os.path.isdir(EXP):
        shutil.rmtree(EXP)
    os.makedirs(EXP)
    # favicon.svg: holes empty, the disc switches to the dark-mode blue in dark themes
    fav = G.mark_svg(o, 'light', vb=G.VB_BLEED, label='userandproduct').replace(
        '<title>', '<style>@media (prefers-color-scheme:dark){path{fill:%s}}</style><title>' % o['dark'], 1)
    write('export/favicon.svg', fav)
    # PNG favicons: the figure filled white, so they hold in light and dark tabs alike
    solid = G.avatar_svg(o, 'circle')
    for size in (16, 32, 48):
        save('export/favicon-%d.png' % size, G.png(solid, size, size))
    ico = [G.png(solid, s, s) for s in (16, 32, 48)]
    ico[2].save(os.path.join(EXP, 'favicon.ico'), sizes=[(16, 16), (32, 32), (48, 48)],
                append_images=ico[:2])
    # Apple touch icon: opaque full square; iOS rounds the corners itself
    save('export/apple-touch-icon-180.png', G.png(G.avatar_svg(o, 'square'), 180, 180).convert('RGB'))
    # social: a square (Instagram, LinkedIn, X upload) and a circle with transparent corners
    for size in (400, 1080):
        save('export/social-square-%d.png' % size, hi_png(G.avatar_svg(o, 'square'), size, size).convert('RGB'))
        save('export/social-circle-%d.png' % size, hi_png(G.avatar_svg(o, 'circle'), size, size))
    # the gradients as social uploads, for trying out
    for gopt in G.GRADIENTS:
        save('export/gradient/%s-square-1080.png' % gopt['key'][2:],
             hi_png(G.avatar_svg(gopt, 'square'), 1080, 1080, True).convert('RGB'))
        save('export/gradient/%s-circle-1080.png' % gopt['key'][2:],
             hi_png(G.avatar_svg(gopt, 'circle'), 1080, 1080, True))
    write('export/head-snippet.html', HEAD_SNIPPET)


HEAD_SNIPPET = """<!-- userandproduct icons (Logo 3, signal blue option). Copy the files to the site root, then: -->
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon-180.png">
"""


def main():
    for d in (SVG, PNG):
        if os.path.isdir(d):
            shutil.rmtree(d)
    build_masters()
    built = []
    for o in G.OPTIONS + G.GRADIENTS:
        build_option(o)
        built.append(o)
    build_export()
    from board import board
    write('index.html', board())
    print('built %d options and %d gradients' % (len(G.OPTIONS), len(G.GRADIENTS)))


if __name__ == '__main__':
    main()
