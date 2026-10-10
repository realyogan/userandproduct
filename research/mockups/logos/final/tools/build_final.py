"""Build the final logo colour themes: S5 with the fixed wordmark, ten colour schemes, a full asset pack each.

The mark is S5 exactly as on the shortlist (shortlist/s5-mark.svg and s5-favicon.svg; the favicon has
wider gaps for 16px). Its four tiles are split into roles: the top and bottom tiles are the large pair,
the right and left tiles the small pair. The lockup is the shortlist's (P8 geometry: Inter Display
Bold, tracking -25, mark 1.4 cap heights tall centered on half the cap height, gap 0.38 cap heights).

Run from anywhere:  python build_final.py
Writes one folder per theme next to this tools folder, then index.html (board.py).
"""
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, '..'))
LOGOS = os.path.normpath(os.path.join(OUT, '..'))
MOCK = os.path.normpath(os.path.join(LOGOS, '..'))
sys.path.insert(0, os.path.join(LOGOS, 'shortlist', 'tools'))
sys.path.insert(0, os.path.join(MOCK, 'tools'))
sys.path.insert(0, HERE)   # last, so this folder's board.py wins over the shortlist's

import xml.etree.ElementTree as ET  # noqa: E402

from PIL import Image  # noqa: E402

import brand_assets as BA  # noqa: E402
import render as R  # noqa: E402
import geom as G  # noqa: E402
from build_shortlist import lockup  # noqa: E402
from themes import T  # noqa: E402

PATH_RE = re.compile(r'<path fill="[^"]+" d="([^"]+)"/>')
NAV_WORDS = ['Design', 'Product', 'Business', 'Library']
NAV_GREY = {'L': '#6B6B6B', 'D': '#9B9892'}
HEADER_LINE = {'L': '#E6E4DF', 'D': '#2A2A2A'}
G.FONTS['inter-r'] = 'inter/InterDisplay-Regular.ttf'
NAV_FONT = 'inter-r'
LOGO_H = 30            # logo height in the header, as on the earlier boards
FILES = ['lockup-light.svg', 'lockup-dark.svg', 'lockup-mono.svg', 'mark.svg', 'mark-dark.svg', 'favicon.svg',
         'favicon-16.png', 'favicon-32.png', 'favicon.ico', 'apple-touch-icon-180.png', 'icon-512.png',
         'avatar-400.png', 'og-1200x630.png', 'og-dark-1200x630.png', 'header-light.png', 'header-dark.png',
         'linkedin-banner-1128x191.png', 'linkedin-banner-dark-1128x191.png', 'linkedin-avatar-400.png',
         'linkedin-mock-light.png', 'linkedin-mock-dark.png', 'linkedin-post-light.png']
FONT_R = os.path.join(MOCK, 'fonts', 'inter', 'InterDisplay-Regular.ttf')
FONT_B = os.path.join(MOCK, 'fonts', 'inter', 'InterDisplay-Bold.ttf')


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def tiles_of(fn):
    """The four tile subpaths of an S5 file: [top, bottom, right, left]."""
    d = PATH_RE.findall(read(os.path.join(LOGOS, 'shortlist', fn)))[0]
    subs = ['M' + s.strip() for s in d.split('M') if s.strip()]
    assert len(subs) == 4, len(subs)
    return subs


MARK = tiles_of('s5-mark.svg')
FAV = tiles_of('s5-favicon.svg')
ROLES = ['big', 'big', 'small', 'small']


def fills(t, mode):
    """Fill per tile for 'L', 'D' or 'mono'."""
    if mode == 'mono':
        return ['currentColor'] * 4
    c = t[mode]
    out = [c[r] for r in ROLES]
    if t['odd']:
        out[2] = t['odd'][mode]     # the right small tile carries the single colour
    return out


def frags(tiles, cols):
    """Group tiles of one colour into one path each (fewer elements)."""
    groups = {}
    for d, c in zip(tiles, cols):
        groups.setdefault(c, []).append(d)
    return [(''.join(ds), c) for c, ds in groups.items()]


def mark_svg(tiles, cols, label='userandproduct mark', vb=(-1, -1, 102, 102)):
    return G.svg(vb, ''.join(G.P(d, c) for d, c in frags(tiles, cols)), label)


def lock_svg(t, mode):
    ink = 'currentColor' if mode == 'mono' else t[mode]['word']
    return lockup(frags(MARK, fills(t, mode)), ink)


def write_svg(folder, name, text):
    ET.fromstring(text)
    with open(os.path.join(folder, name), 'w', encoding='utf-8') as f:
        f.write(text)


def vbox(svg_text):
    return [float(v) for v in re.search(r'viewBox="([^"]+)"', svg_text).group(1).split()]


def inner(svg_text):
    """The drawing inside an SVG, without its title."""
    body = svg_text[svg_text.index('>') + 1:svg_text.rindex('</svg>')]
    return re.sub(r'<title>.*?</title>', '', body)


def nav_word(text, size):
    """A nav label as one path (advance widths, components decomposed), baseline 0. Returns (d, width)."""
    from fontTools.pens.svgPathPen import SVGPathPen
    from fontTools.pens.transformPen import TransformPen
    f = G.font(NAV_FONT)
    gs, cmap, hmtx = f.tt.getGlyphSet(), f.tt.getBestCmap(), f.tt['hmtx']
    sc = size / f.upem
    pen = SVGPathPen(gs, ntos=G.fmt)
    x = 0.0
    for ch in text:
        name = cmap[ord(ch)]
        gs[name].draw(TransformPen(pen, (sc, 0, 0, -sc, x, 0)))
        x += hmtx[name][0] * sc
    return pen.getCommands(), x


def header_svg(t, mode, lock):
    c = t[mode]
    x, y, w, h = vbox(lock)
    lw = LOGO_H * w / h
    logo = (f'<svg x="40" y="{(72 - LOGO_H) / 2:.2f}" width="{lw:.2f}" height="{LOGO_H}" '
            f'viewBox="{x} {y} {w} {h}">{inner(lock)}</svg>')
    cap = G.caph(NAV_FONT, 15)
    base = 36 + cap / 2
    words, xr = [], 1280 - 40
    for wd in reversed(NAV_WORDS):
        d, width = nav_word(wd, 15)
        words.append(G.P(G.shift(d, xr - width, base), NAV_GREY[mode]))
        xr -= width + 32
    body = (G.P(G.rect(0, 0, 1280, 72), c['bg']) + G.P(G.rect(0, 71, 1280, 72), HEADER_LINE[mode]) +
            logo + ''.join(words))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 72" width="1280" height="72">'
            f'{body}</svg>')


def og_png(lock, bg, path, width=760):
    art = Image.open(io.BytesIO(R.render_png(lock, width))).convert('RGBA')
    canvas = Image.new('RGBA', (1200, 630), bg)
    canvas.alpha_composite(art, ((1200 - art.width) // 2, (630 - art.height) // 2))
    canvas.convert('RGB').save(path)


def build_theme(t):
    folder = os.path.join(OUT, t['slug'])
    os.makedirs(folder, exist_ok=True)
    locks = {m: lock_svg(t, m) for m in ('L', 'D', 'mono')}
    write_svg(folder, 'lockup-light.svg', locks['L'])
    write_svg(folder, 'lockup-dark.svg', locks['D'])
    write_svg(folder, 'lockup-mono.svg', locks['mono'])
    write_svg(folder, 'mark.svg', mark_svg(MARK, fills(t, 'L')))
    write_svg(folder, 'mark-dark.svg', mark_svg(MARK, fills(t, 'D')))
    fav = mark_svg(FAV, fills(t, 'L'), 'userandproduct', (0, 0, 100, 100))
    pairs = list(dict.fromkeys(zip(fills(t, 'L'), fills(t, 'D'))))
    write_svg(folder, 'favicon.svg', BA.favicon_svg_pairs(fav, pairs))
    # PNG and ICO: favicons from the wide-gap favicon geometry, avatar and app icons from the mark
    bg = t['L']['bg']
    BA.write_pack(fav, folder, bg)
    full = mark_svg(MARK, fills(t, 'L'))
    for name, size, pad in (('apple-touch-icon-180.png', 180, 20), ('icon-512.png', 512, 56),
                            ('avatar-400.png', 400, 84)):
        BA.tile(full, size, size, bg, pad).convert('RGB').save(os.path.join(folder, name))
    og_png(locks['L'], bg, os.path.join(folder, 'og-1200x630.png'))
    og_png(locks['D'], t['D']['bg'], os.path.join(folder, 'og-dark-1200x630.png'))
    # LinkedIn: banners, avatar (21 percent margin, inside the 12 percent circle-crop safe zone), mocks
    BA.linkedin_pack(folder, locks['L'], locks['D'], os.path.join(folder, 'avatar-400.png'),
                     os.path.join(folder, 'og-1200x630.png'),
                     dict(bg_light=bg, bg_dark=t['D']['bg'], accent_light=t['L']['link'],
                          accent_dark=t['D']['link'], on_accent_light='#FFFFFF', on_accent_dark='#0F0F10'),
                     FONT_R, FONT_B)
    for mode, name in (('L', 'header-light.png'), ('D', 'header-dark.png')):
        hs = header_svg(t, mode, locks[mode])
        ET.fromstring(hs)
        with open(os.path.join(folder, name), 'wb') as f:
            f.write(R.render_png(hs, 1280, 72))
    return folder


def validate():
    n_svg = n_img = 0
    for t in T:
        folder = os.path.join(OUT, t['slug'])
        for fn in FILES:
            p = os.path.join(folder, fn)
            assert os.path.exists(p), p
            if fn.endswith('.svg'):
                ET.parse(p)
                n_svg += 1
            else:
                with Image.open(p) as im:
                    im.load()
                    if fn == 'favicon.ico':
                        assert {(16, 16), (32, 32), (48, 48)} <= set(im.info.get('sizes', set())), im.info
                n_img += 1
    return n_svg, n_img


if __name__ == '__main__':
    for t in T:
        build_theme(t)
        print('built', t['slug'])
    print('validated %d SVG, %d PNG/ICO' % validate())
    if '--no-board' not in sys.argv:
        import importlib.util
        spec = importlib.util.spec_from_file_location('final_board', os.path.join(HERE, 'board.py'))
        board = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(board)
        board.write(T, OUT)
        print('wrote index.html')
