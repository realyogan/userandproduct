"""Build the userandproduct logo pack (theme T08 "Signal", decided 9 Oct 2026).

Run from anywhere:  python build.py
Writes svg/, png/, favicon/, social/, brand-sheet.html and README.md next to this file, then validates
everything. Rerunnable; the output is deterministic.

Needs only research/mockups/tools/ (wordmark.py, render.py, brand_assets.py) and
research/mockups/fonts/inter/. The mark geometry (S5: four tiles of two sizes, rotated 45 degrees) is
embedded below as path data; the wordmark is set from Inter Display Bold at build time.
"""
import io
import json
import os
import re
import sys
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
MOCK = os.path.normpath(os.path.join(HERE, '..'))
sys.path.insert(0, os.path.join(MOCK, 'tools'))

import pathops  # noqa: E402
from fontTools.pens.svgPathPen import SVGPathPen  # noqa: E402
from fontTools.svgLib.path import parse_path  # noqa: E402
from fontTools.ttLib import TTFont  # noqa: E402
from PIL import Image  # noqa: E402

import brand_assets as BA  # noqa: E402
import render as R  # noqa: E402
import wordmark as WM  # noqa: E402

DECIDED = '2026-10-09'
FONT_B = os.path.join(MOCK, 'fonts', 'inter', 'InterDisplay-Bold.ttf')
FONT_R = os.path.join(MOCK, 'fonts', 'inter', 'InterDisplay-Regular.ttf')

# ------------------------------------------------------------------ colour tokens
BLUE_L, BLUE_D = '#2B46A0', '#8EA2FF'      # mark, light and dark mode
INK, OFF = '#0B0B0C', '#F1EEE7'            # wordmark, light and dark mode
WHITE, NEAR = '#FFFFFF', '#0B0B0C'         # page backgrounds
BLACK_MONO, WHITE_MONO = '#0B0B0C', '#FFFFFF'

# ------------------------------------------------------------------ geometry
TRACK = 0            # 1/1000 em; 0 = the typeface as designed (decided 9 Oct 2026; was -25)
H_CAP = 1.4          # mark height in cap heights (side lockup)
GAP_CAP = 0.38       # the original P8 gap, in cap heights (0.27 of the mark height); kept for the record
STACK_H_CAP = 3.0    # mark height in the stacked lockup
STACK_GAP_CAP = 0.76

# S5 mark, 0..100 box: tiles top, bottom (large) and right, left (small)
MARK_D = ('M58.01 2.66 69.42 20.21C71.19 22.94 70.41 26.58 67.68 28.36L50.13 39.76C47.4 41.53 43.76 40.75 41.99 '
          '38.03L30.58 20.47C28.81 17.74 29.59 14.1 32.32 12.33L49.87 0.93C52.6 -0.85 56.24 -0.07 58.01 2.66Z'
          'M41.99 97.34 30.58 79.79C28.81 77.06 29.59 73.42 32.32 71.64L49.87 60.24C52.6 58.47 56.24 59.25 58.01 '
          '61.97L69.42 79.53C71.19 82.26 70.41 85.9 67.68 87.67L50.13 99.07C47.4 100.85 43.76 100.07 41.99 97.34Z'
          'M92.39 55.77 79.75 63.98C77.79 65.25 75.16 64.7 73.89 62.73L65.68 50.09C64.41 48.13 64.96 45.5 66.93 '
          '44.23L79.57 36.02C81.53 34.75 84.15 35.3 85.43 37.27L93.64 49.91C94.91 51.87 94.36 54.5 92.39 55.77Z'
          'M7.61 44.23 20.25 36.02C22.21 34.75 24.84 35.3 26.11 37.27L34.32 49.91C35.59 51.87 35.04 54.5 33.07 '
          '55.77L20.43 63.98C18.47 65.25 15.85 64.7 14.57 62.73L6.36 50.09C5.09 48.13 5.64 45.5 7.61 44.23Z')
# The favicon cut: the same mark with wider gaps so the tiles stay apart at 16 px
FAV_D = ('M57.78 2.64 68.85 19.69C70.57 22.34 69.82 25.88 67.17 27.6L50.13 38.67C47.48 40.39 43.94 39.64 42.22 '
         '36.99L31.15 19.94C29.43 17.29 30.18 13.75 32.83 12.03L49.87 0.96C52.52 -0.76 56.06 0 57.78 2.64Z'
         'M42.22 97.36 31.15 80.31C29.43 77.66 30.18 74.12 32.83 72.4L49.87 61.33C52.52 59.61 56.06 60.36 57.78 '
         '63.01L68.85 80.06C70.57 82.71 69.82 86.25 67.17 87.97L50.13 99.04C47.48 100.76 43.94 100 42.22 97.36Z'
         'M92.55 55.6 80.27 63.57C78.37 64.81 75.82 64.27 74.58 62.36L66.61 50.09C65.37 48.18 65.91 45.63 67.82 '
         '44.4L80.09 36.43C82 35.19 84.55 35.73 85.79 37.64L93.76 49.91C95 51.82 94.45 54.37 92.55 55.6Z'
         'M7.45 44.4 19.73 36.43C21.63 35.19 24.18 35.73 25.42 37.64L33.39 49.91C34.63 51.82 34.09 54.37 32.18 '
         '55.6L19.91 63.57C18 64.81 15.45 64.27 14.21 62.36L6.24 50.09C5 48.18 5.55 45.63 7.45 44.4Z')
SMALL_TILE_D = MARK_D.split('Z')[3] + 'Z'   # the left small tile

fmt = WM.fmt


def to_path(d):
    p = pathops.Path()
    parse_path(d, p.getPen())
    return p


def from_path(p):
    pen = SVGPathPen(None, ntos=fmt)
    p.draw(pen)
    return pen.getCommands()


def shift(d, dx, dy, s=1.0):
    return from_path(to_path(d).transform(s, 0, 0, s, dx, dy))


def bounds(d):
    return to_path(d).bounds


def svg(vb, body, label='userandproduct'):
    x, y, w, h = vb
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{fmt(x)} {fmt(y)} {fmt(w)} {fmt(h)}" '
            f'role="img" aria-label="{label}"><title>{label}</title>{body}</svg>')


def P(d, fill):
    return f'<path fill="{fill}" d="{d}"/>'


def fitbox(x0, y0, x1, y1, m):
    return (x0 - m, y0 - m, x1 - x0 + 2 * m, y1 - y0 + 2 * m)


_FONT = WM.FontRef(FONT_B)
CAP = _FONT.tt['OS/2'].sCapHeight * 100 / _FONT.upem


def word(track=None):
    """The name as one merged path, baseline 0, ink starting at x = 0, and its ink box."""
    items = WM.layout(['userandproduct'], [_FONT], 100, TRACK if track is None else track)
    d, b = WM.part_path(items[0], True)
    return shift(d, -b[0], 0), (0, b[1], b[2] - b[0], b[3])


WORD_D, WB = word()

# side lockup: mark 1.4 cap heights tall; since 9 Oct 2026 centred midway between the cap band and the
# x-height band, gap 0.40 of the mark height (owner decision; see alignment.html)
_mx0, _my0, _mx1, _my1 = bounds(MARK_D)
S_SIDE = CAP * H_CAP / (_my1 - _my0)
MARK_W_SIDE = (_mx1 - _mx0) * S_SIDE
_t = bounds(SMALL_TILE_D)
SMALL_TILE_FRAC = (_t[3] - _t[1]) / (_my1 - _my0)    # small tile height / mark height


XH = _FONT.tt['OS/2'].sxHeight * 100 / _FONT.upem
ALIGN = 'mid'        # set by --align: mid (decided), cap (the original P8) or xheight


def mark_centre(align=None):
    """The y of the mark's centre in the side lockup (baseline 0, y down)."""
    align = align or ALIGN
    if align == 'cap':
        return -CAP / 2                      # centred on the cap band (the decided lockup)
    if align == 'xheight':
        return -XH / 2                       # centred on the x-height band
    if align == 'mid':
        return -(CAP + XH) / 4               # halfway between the two
    raise ValueError(align)


GAP = 0.40           # set by --gap: gap as a fraction of the mark height (decided 0.40; None: the original 0.38 cap heights)


def gap_units(gap=None):
    gap = GAP if gap is None else gap
    if gap == 'original':
        gap = None
    return CAP * GAP_CAP if gap is None else CAP * H_CAP * gap


def lockup(mark_c, word_c, align=None, gap=None, track=None):
    WORD_D, WB = (globals()['WORD_D'], globals()['WB']) if track is None else word(track)
    H, yc, gap = CAP * H_CAP, mark_centre(align), gap_units(gap)
    dx, dy = -_mx0 * S_SIDE, yc - H / 2 - _my0 * S_SIDE
    body = P(shift(MARK_D, dx, dy, S_SIDE), mark_c) + P(shift(WORD_D, MARK_W_SIDE + gap, 0), word_c)
    top, bot = min(yc - H / 2, WB[1]), max(yc + H / 2, WB[3])
    return svg(fitbox(0, top, MARK_W_SIDE + gap + WB[2], bot, 4), body)


def stacked(mark_c, word_c):
    H, gap = CAP * STACK_H_CAP, CAP * STACK_GAP_CAP
    s = H / (_my1 - _my0)
    mw = (_mx1 - _mx0) * s
    mx = (WB[2] - mw) / 2
    mtop = WB[1] - gap - H
    body = P(shift(MARK_D, mx - _mx0 * s, mtop - _my0 * s, s), mark_c) + P(WORD_D, word_c)
    return svg(fitbox(0, mtop, WB[2], WB[3], 4), body)


def mark(c, d=MARK_D, vb=(-1, -1, 102, 102), label='userandproduct mark'):
    return svg(vb, P(d, c), label)


def wordmark(c):
    return svg(fitbox(0, WB[1], WB[2], WB[3], 4), P(WORD_D, c))


# ------------------------------------------------------------------ contrast (WCAG 2)
def lum(hexc):
    h = hexc.lstrip('#')
    out = []
    for i in (0, 2, 4):
        c = int(h[i:i + 2], 16) / 255
        out.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * out[0] + 0.7152 * out[1] + 0.0722 * out[2]


def ratio(a, b):
    la, lb = lum(a), lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


# ------------------------------------------------------------------ writers
def path_of(rel):
    return os.path.join(HERE, *rel.split('/'))


def write_text(rel, text):
    p = path_of(rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def save_img(rel, img):
    p = path_of(rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    img.save(p)


def png_wide(svg_text, width):
    return Image.open(io.BytesIO(R.render_png(svg_text, width))).convert('RGBA')


def png_square(svg_text, size, pad=0):
    return R.render_fitted(svg_text, size, pad=pad)


def solid(img, bg):
    canvas = Image.new('RGBA', img.size, bg)
    canvas.alpha_composite(img)
    return canvas.convert('RGB')


def vbox(svg_text):
    return [float(v) for v in re.search(r'viewBox="([^"]+)"', svg_text).group(1).split()]


def inner(svg_text):
    body = svg_text[svg_text.index('>') + 1:svg_text.rindex('</svg>')]
    return re.sub(r'<title>.*?</title>', '', body)


def nest(svg_text, x, y, h):
    vx, vy, vw, vh = vbox(svg_text)
    w = h * vw / vh
    return (f'<svg x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" '
            f'viewBox="{fmt(vx)} {fmt(vy)} {fmt(vw)} {fmt(vh)}">{inner(svg_text)}</svg>'), w


def doc(w, h, body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{body}</svg>'


def canvas_png(w, h, bg, art):
    text = doc(w, h, f'<rect width="{w}" height="{h}" fill="{bg}"/>' + art)
    ET.fromstring(text)
    return Image.open(io.BytesIO(R.render_png(text, w, h))).convert('RGB')


# ------------------------------------------------------------------ 1 masters
SV = {}


def build_svgs():
    SV['lockup-light'] = lockup(BLUE_L, INK)
    SV['lockup-dark'] = lockup(BLUE_D, OFF)
    SV['lockup-black'] = lockup(BLACK_MONO, BLACK_MONO)
    SV['lockup-white'] = lockup(WHITE_MONO, WHITE_MONO)
    SV['lockup-stacked-light'] = stacked(BLUE_L, INK)
    SV['lockup-stacked-dark'] = stacked(BLUE_D, OFF)
    SV['mark-light'] = mark(BLUE_L)
    SV['mark-dark'] = mark(BLUE_D)
    SV['mark-black'] = mark(BLACK_MONO)
    SV['mark-white'] = mark(WHITE_MONO)
    SV['wordmark-black'] = wordmark(BLACK_MONO)
    SV['wordmark-white'] = wordmark(WHITE_MONO)
    for k, v in SV.items():
        write_text(f'svg/{k}.svg', v + '\n')
    write_text('svg/mark-currentcolor.svg', mark('currentColor') + '\n')


# ------------------------------------------------------------------ 2 PNG and favicons
FAV_SVG = mark(BLUE_L, FAV_D, (0, 0, 100, 100), 'userandproduct')

HEAD_SNIPPET = """<!-- userandproduct icons. Copy the files in favicon/ to the site root, then paste these tags into
     the theme's <head> (wp_head). Do not also set a WordPress Site Icon, or the icon tags print twice. -->
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon-180.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#2B46A0">
"""


def build_pngs():
    for k, v in SV.items():
        if k.startswith('lockup-stacked'):
            for size in (1200, 2400):
                save_img(f'png/{k}-{size}.png', png_square(v, size, pad=size // 10))
        elif k.startswith('lockup') or k.startswith('wordmark'):
            for w in (1200, 2400):
                save_img(f'png/{k}-{w}.png', png_wide(v, w))
        else:
            for size in (256, 512, 1024):
                save_img(f'png/{k}-{size}.png', png_square(v, size))
    save_img('png/lockup-light-on-white-2400.png', solid(png_wide(SV['lockup-light'], 2400), WHITE))
    save_img('png/lockup-dark-on-black-2400.png', solid(png_wide(SV['lockup-dark'], 2400), NEAR))

    write_text('favicon/favicon.svg', BA.favicon_svg_pairs(FAV_SVG, [(BLUE_L, BLUE_D)]) + '\n')
    fav = {}
    for size, pad in ((16, 1), (32, 2), (48, 3)):
        fav[size] = BA.tile(FAV_SVG, size, size, WHITE, pad)
        save_img(f'favicon/favicon-{size}.png', fav[size])
    fav[48].save(path_of('favicon/favicon.ico'), format='ICO', sizes=[(16, 16), (32, 32), (48, 48)],
                 append_images=[fav[16], fav[32]])
    full = SV['mark-light']
    for name, size, pad in (('apple-touch-icon-180.png', 180, 20), ('icon-192.png', 192, 21),
                            ('icon-512.png', 512, 56), ('maskable-512.png', 512, 112)):
        save_img(f'favicon/{name}', BA.tile(full, size, size, WHITE, pad).convert('RGB'))
    manifest = {
        'name': 'userandproduct', 'short_name': 'userandproduct', 'start_url': '/', 'display': 'standalone',
        'theme_color': BLUE_L, 'background_color': WHITE,
        'icons': [
            {'src': '/icon-192.png', 'sizes': '192x192', 'type': 'image/png'},
            {'src': '/icon-512.png', 'sizes': '512x512', 'type': 'image/png'},
            {'src': '/maskable-512.png', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'maskable'},
        ]}
    write_text('favicon/site.webmanifest', json.dumps(manifest, indent=2) + '\n')
    write_text('favicon/head-snippet.html', HEAD_SNIPPET)


# ------------------------------------------------------------------ 3 social
NAV_WORDS = ['Design', 'Product', 'Business', 'Library']
NAV_GREY = {'light': '#6B6B6B', 'dark': '#9B9892'}
HEADER_LINE = {'light': '#E6E4DF', 'dark': '#2A2A2A'}


def header_png(mode):
    bg = WHITE if mode == 'light' else NEAR
    return canvas_png(1280, 72, bg, header_art(mode, SV['lockup-' + mode]))


def header_art(mode, lock, ref=None):
    """Header drawing. With ref (the cap-aligned lockup), lock is placed at ref's scale and baseline."""
    if ref is None:
        logo, _ = nest(lock, 40, 21, 30)
    else:
        rvb, vb = vbox(ref), vbox(lock)
        sc = 30 / rvb[3]
        logo, _ = nest(lock, 40, 21 + (vb[1] - rvb[1]) * sc, vb[3] * sc)
    tt = TTFont(FONT_R)
    cap = tt['OS/2'].sCapHeight * 15 / tt['head'].unitsPerEm
    base = 36 + cap / 2
    words, xr = [], 1280 - 40
    for wd in reversed(NAV_WORDS):
        _, width = BA.text_path(FONT_R, wd, 15)
        d, _ = BA.text_path(FONT_R, wd, 15, xr - width, base)
        words.append(P(d, NAV_GREY[mode]))
        xr -= width + 32
    return f'<rect y="71" width="1280" height="1" fill="{HEADER_LINE[mode]}"/>' + logo + ''.join(words)


def centred(lock, w, h, lh, cx=None):
    vx, vy, vw, vh = vbox(lock)
    lw = lh * vw / vh
    cx = w / 2 if cx is None else cx
    return nest(lock, cx - lw / 2, h / 2 - lh / 2, lh)[0]


def build_social():
    for mode, bg in (('light', WHITE), ('dark', NEAR)):
        lock = SV['lockup-' + mode]
        vx, vy, vw, vh = vbox(lock)
        save_img(f'social/og-1200x630-{mode}.png', canvas_png(1200, 630, bg, centred(lock, 1200, 630, 760 * vh / vw)))
        # LinkedIn banner: lockup 52 px tall, centred on 42 percent of the width (the avatar covers the lower left)
        save_img(f'social/linkedin-banner-1128x191-{mode}.png',
                 canvas_png(1128, 191, bg, centred(lock, 1128, 191, 52, cx=1128 * 0.42)))
        save_img(f'social/header-strip-{mode}.png', header_png(mode))
    # X header: lockup on the left, 84 px tall, centred vertically (mobile crops the top and bottom)
    save_img('social/twitter-1500x500-light.png',
             canvas_png(1500, 500, WHITE, nest(SV['lockup-light'], 120, 250 - 42, 84)[0]))
    # avatars: 21 percent margin, inside the circle-crop safe zone
    save_img('social/linkedin-avatar-400.png', BA.tile(SV['mark-light'], 400, 400, WHITE, 84).convert('RGB'))
    save_img('social/avatar-400-dark.png', BA.tile(SV['mark-dark'], 400, 400, NEAR, 84).convert('RGB'))


# ------------------------------------------------------------------ 4 brand sheet and README
CSS = """
:root{--bg:#FFFFFF;--fg:#0B0B0C;--sub:#5C5C5F;--line:#E6E4DF;--card:#F7F6F3;--accent:#2B46A0;color-scheme:light dark}
@media (prefers-color-scheme:dark){:root{--bg:#0B0B0C;--fg:#F1EEE7;--sub:#A8A59F;--line:#2A2A2A;--card:#151517;--accent:#8EA2FF}}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
main{max-width:1120px;margin:0 auto;padding:40px 16px 80px}
h1{font-size:clamp(28px,5vw,44px);line-height:1.1;margin:0 0 8px;letter-spacing:-.02em}
h2{font-size:22px;margin:56px 0 6px;letter-spacing:-.01em;padding-top:20px;border-top:1px solid var(--line)}
h3{font-size:15px;margin:0 0 8px;color:var(--sub);font-weight:600}
p{margin:0 0 12px;max-width:68ch}
.lede{color:var(--sub);font-size:18px}
a{color:var(--accent)}
code{font:14px/1.4 ui-monospace,Consolas,monospace;overflow-wrap:anywhere}
.grid{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr))}
.grid.three{grid-template-columns:repeat(auto-fit,minmax(min(100%,220px),1fr))}
.panel{border:1px solid var(--line);border-radius:10px;padding:32px 24px;display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:14px;min-height:180px}
.panel svg{display:block;width:100%;height:auto}
.panel .lk{max-width:420px}.panel .mk{width:112px}.panel .st{max-width:260px}
.panel small{font-size:12px;opacity:.75}
.on-light{background:#FFFFFF;color:#0B0B0C}.on-dark{background:#0B0B0C;color:#F1EEE7;border-color:#2A2A2A}
.on-photo{background:linear-gradient(135deg,#3B4A5C,#1E2733 55%,#4A3B33);color:#FFFFFF;border:0}
.tabs{display:flex;flex-wrap:wrap;gap:16px}
.tab{background:#DEE1E6;border-radius:10px;padding:8px 8px 0;min-width:0;flex:1 1 260px}
.tab.dark{background:#202124}
.tab .t{display:flex;align-items:center;gap:8px;background:#FFFFFF;border-radius:8px 8px 0 0;padding:8px 12px;
  font:13px system-ui,sans-serif;color:#202124;max-width:260px}
.tab.dark .t{background:#35363A;color:#E8EAED}
.tab img{display:block;flex:none}
.shots{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr))}
figure{margin:0}
figure.sq img{max-width:240px}
figure img{display:block;width:100%;height:auto;border:1px solid var(--line);border-radius:6px}
figcaption{font-size:13px;color:var(--sub);margin-top:6px;overflow-wrap:anywhere}
.table{overflow-x:auto}
table{border-collapse:collapse;width:100%;font-size:15px}
th,td{text-align:left;padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:middle}
th{font-size:13px;color:var(--sub);font-weight:600}
@media (max-width:560px){thead{display:none}table,tbody,tr,td{display:block}tr{padding:10px 0;border-bottom:1px solid var(--line)}td{border:0;padding:2px 0}}
.sw{display:inline-block;width:28px;height:28px;border-radius:6px;border:1px solid var(--line);vertical-align:middle}
.dl{display:grid;grid-template-columns:max-content 1fr;gap:6px 20px}
.dl dt{color:var(--sub)}.dl dd{margin:0}
@media (max-width:520px){.dl{grid-template-columns:1fr}.dl dd{margin-bottom:8px}}
.clear{background:#FFFFFF;border-radius:10px;border:1px solid var(--line);padding:24px}
.clear svg{display:block;width:100%;height:auto;max-width:760px;margin:0 auto}
.rules{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr))}
.rules ul{margin:0;padding-left:20px}.rules li{margin-bottom:6px}
.do h3{color:#1F7A3D}.dont h3{color:#B3141C}
@media (prefers-color-scheme:dark){.do h3{color:#6FCF8E}.dont h3{color:#F38A8E}}
.files{columns:3 220px;column-gap:24px;padding:0;list-style:none;margin:0}
.files li{break-inside:avoid;font-size:14px;margin-bottom:4px;overflow-wrap:anywhere}
.files .h{font-weight:600;margin-top:12px;color:var(--sub)}
footer{margin-top:56px;color:var(--sub);font-size:14px}
"""


def _esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def _inline(svg_text, cls):
    """An SVG for inline use: a class, decorative title kept as the accessible name."""
    return svg_text.replace('<svg ', f'<svg class="{cls}" ', 1)


def _clear_space_svg(lock, x_units):
    vx, vy, vw, vh = vbox(lock)
    m = x_units
    W, H = vw + 4 * m, vh + 4 * m
    ox, oy = vx - 2 * m, vy - 2 * m
    tile = (f'<rect x="{fmt(vx - m)}" y="{fmt(vy - m)}" width="{fmt(m)}" height="{fmt(m)}" fill="#2B46A0" '
            f'fill-opacity=".18"/>')
    body = (f'<rect x="{fmt(vx - m)}" y="{fmt(vy - m)}" width="{fmt(vw + 2 * m)}" height="{fmt(vh + 2 * m)}" '
            f'fill="none" stroke="#2B46A0" stroke-width="1.2" stroke-dasharray="6 4"/>'
            f'<rect x="{fmt(vx)}" y="{fmt(vy)}" width="{fmt(vw)}" height="{fmt(vh)}" fill="none" '
            f'stroke="#9B9892" stroke-width=".8"/>' + tile + inner(lock))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{fmt(ox)} {fmt(oy)} {fmt(W)} {fmt(H)}" '
            f'role="img" aria-label="Clear space around the lockup"><title>Clear space around the lockup'
            f'</title>{body}</svg>')


def brand_sheet(sv, tk, rt, geo, files):
    x_units = geo['small_tile_frac'] * geo['mark_h']           # small tile height in lockup units
    lock_h = geo['lock_vb'][3]
    x_at_30 = 30 * x_units / lock_h
    rows = [
        ('Signal blue, light', 'Mark on light backgrounds; links', tk['BLUE_L'], tk['WHITE'], rt['mark_light']),
        ('Signal blue, dark', 'Mark on dark backgrounds; links', tk['BLUE_D'], tk['NEAR'], rt['mark_dark']),
        ('Ink', 'Wordmark on light; one-colour black', tk['INK'], tk['WHITE'], rt['word_light']),
        ('Off-white', 'Wordmark on dark', tk['OFF'], tk['NEAR'], rt['word_dark']),
        ('White', 'Light background; one-colour white', tk['WHITE'], None, None),
        ('Near-black', 'Dark background', tk['NEAR'], None, None),
    ]
    trs = []
    for name, use, hexc, bg, r in rows:
        on = f'{r:.1f}:1 on {bg}' if r else '(background)'
        trs.append(f'<tr><td><span class="sw" style="background:{hexc}"></span></td><td>{name}</td>'
                   f'<td><code>{hexc}</code></td><td>{on}</td><td>{use}</td></tr>')
    social = [('og-1200x630-light.png', 'Open Graph, light, 1200 x 630'),
              ('og-1200x630-dark.png', 'Open Graph, dark, 1200 x 630'),
              ('linkedin-banner-1128x191-light.png', 'LinkedIn banner, light, 1128 x 191'),
              ('linkedin-banner-1128x191-dark.png', 'LinkedIn banner, dark, 1128 x 191'),
              ('twitter-1500x500-light.png', 'X header, 1500 x 500'),
              ('linkedin-avatar-400.png', 'Avatar, light, 400 x 400'),
              ('avatar-400-dark.png', 'Avatar, dark, 400 x 400'),
              ('header-strip-light.png', 'Site header, light, 1280 x 72'),
              ('header-strip-dark.png', 'Site header, dark, 1280 x 72')]
    figs = ''.join(f'<figure{" class=\"sq\"" if "avatar" in f else ""}><img src="social/{f}" alt="{_esc(c)}" loading="lazy"><figcaption>{c}</figcaption>'
                   f'</figure>' for f, c in social)
    idx = []
    for folder, names in files.items():
        idx.append(f'<li class="h">{folder}/</li>')
        idx += [f'<li><a href="{folder}/{n}">{n}</a></li>' for n in names]
    idx += ['<li class="h">source</li>', '<li><a href="build.py">build.py</a></li>',
            '<li><a href="README.md">README.md</a></li>']
    L = lambda k: _inline(sv[k], 'lk')  # noqa: E731
    M = lambda k: _inline(sv[k], 'mk')  # noqa: E731
    S = lambda k: _inline(sv[k], 'st')  # noqa: E731
    return f"""<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>userandproduct brand sheet</title>
<link rel="icon" href="favicon/favicon.svg" type="image/svg+xml">
<style>{CSS}</style>
</head>
<body>
<main>
<header>
<h1>userandproduct brand sheet</h1>
<p class="lede">The logo for userandproduct.com: the Signal mark (four tiles of two sizes, turned 45 degrees) and the
name set in Inter Display Bold. Decided {geo['decided']}. Every file here is built by <code>build.py</code>.</p>
</header>

<h2>Lockup</h2>
<p>The primary logo. Use the light version on white and light greys, the dark version on near-black.</p>
<div class="grid">
<div class="panel on-light">{L('lockup-light')}<small>lockup-light.svg</small></div>
<div class="panel on-dark">{L('lockup-dark')}<small>lockup-dark.svg</small></div>
</div>

<h2>Mark</h2>
<p>The mark alone, for avatars, app icons and favicons. It never takes the name's place in running text.</p>
<div class="grid three">
<div class="panel on-light">{M('mark-light')}<small>mark-light.svg</small></div>
<div class="panel on-dark">{M('mark-dark')}<small>mark-dark.svg</small></div>
<div class="panel on-light">{M('mark-black')}<small>mark-black.svg</small></div>
<div class="panel on-photo">{M('mark-white')}<small>mark-white.svg</small></div>
</div>

<h2>Stacked</h2>
<p>Mark above the name, centred, for square placements (event badges, a square social tile). The mark is three cap
heights tall here.</p>
<div class="grid">
<div class="panel on-light">{S('lockup-stacked-light')}<small>lockup-stacked-light.svg</small></div>
<div class="panel on-dark">{S('lockup-stacked-dark')}<small>lockup-stacked-dark.svg</small></div>
</div>

<h2>One colour</h2>
<p>For print in one ink, embossing, partner pages that ask for one colour, and dark photographs.</p>
<div class="grid">
<div class="panel on-light">{L('lockup-black')}<small>lockup-black.svg</small></div>
<div class="panel on-photo">{L('lockup-white')}<small>lockup-white.svg, on a photograph</small></div>
<div class="panel on-light">{L('wordmark-black')}<small>wordmark-black.svg</small></div>
<div class="panel on-dark">{L('wordmark-white')}<small>wordmark-white.svg</small></div>
</div>

<h2>Favicon</h2>
<p>A wider-gap cut of the mark so the four tiles stay apart at 16 pixels. The SVG favicon switches to the dark
blue in dark browser themes; the PNG and ICO files sit on a white tile so they read in any tab.</p>
<div class="tabs">
<div class="tab"><div class="t"><img src="favicon/favicon-16.png" width="16" height="16" alt="">userandproduct</div></div>
<div class="tab dark"><div class="t"><img src="favicon/favicon.svg" width="16" height="16" alt="">userandproduct</div></div>
<div class="tab"><div class="t"><img src="favicon/favicon-32.png" width="32" height="32" alt="">32 pixels</div></div>
<div class="tab dark"><div class="t"><img src="favicon/favicon.svg" width="32" height="32" alt="">32 pixels, SVG</div></div>
</div>

<h2>Social set</h2>
<div class="shots">{figs}</div>

<h2>Colour</h2>
<p>Four logo colours and two backgrounds. Contrast is the WCAG 2 ratio against the background the colour is used on
(recomputed by the build).</p>
<div class="table"><table>
<thead><tr><th></th><th>Token</th><th>Hex</th><th>Contrast</th><th>Use</th></tr></thead>
<tbody>{''.join(trs)}</tbody>
</table></div>

<h2>Wordmark</h2>
<dl class="dl">
<dt>Typeface</dt><dd>Inter Display (Rasmus Andersson and contributors)</dd>
<dt>Weight</dt><dd>Bold (700)</dd>
<dt>Case</dt><dd>All lowercase, one word: userandproduct</dd>
<dt>Tracking</dt><dd>{geo['track']}, the typeface as designed (the font's own spacing and kerning)</dd>
<dt>Lockup</dt><dd>Mark 1.4 cap heights tall, centred midway between the cap band and the x-height; gap 0.40 of the mark height</dd>
<dt>Files</dt><dd>Outlined as paths; no live text, so nothing depends on a font loading</dd>
<dt>Licence</dt><dd>Inter is under the SIL Open Font License 1.1. The OFL allows logos made from its outlines;
no credit is required. The outlines are not exclusive: anyone can set the same word in the same face.</dd>
</dl>

<h2>Clear space and minimum size</h2>
<p>Clear space, <strong>x</strong>, is the height of one small tile (about {geo['small_tile_frac'] * 100:.0f} percent
of the mark's height). Keep at least x empty on every side. At a 30 pixel tall lockup, x is about
{x_at_30:.1f} pixels.</p>
<div class="clear">{_clear_space_svg(sv['lockup-light'], x_units)}</div>
<dl class="dl" style="margin-top:16px">
<dt>Mark</dt><dd>16 pixels minimum (use the favicon cut at 16 to 48 pixels)</dd>
<dt>Lockup</dt><dd>120 pixels wide minimum; below that, use the mark alone</dd>
</dl>

<h2>Do and don't</h2>
<div class="rules">
<div class="do"><h3>Do</h3><ul>
<li>Use the files as supplied: light, dark, black or white.</li>
<li>Pick light or dark by the background, not by taste.</li>
<li>Scale proportionally and keep the clear space.</li>
<li>Use the white version on photographs, over a calm area.</li>
</ul></div>
<div class="dont"><h3>Don't</h3><ul>
<li>Recolour beyond the four versions.</li>
<li>Stretch, squash, rotate or re-space the logo.</li>
<li>Outline it, or add shadows, glows, gradients or other effects.</li>
<li>Colour the tiles in more than one colour.</li>
<li>Retype the name in another font or in capitals.</li>
</ul></div>
</div>

<h2>Files</h2>
<ul class="files">{''.join(idx)}</ul>

<footer>Rebuild with <code>python build.py</code> in research/mockups/final-logo/.</footer>
</main>
</body>
</html>
"""


def readme(tk, rt, decided):
    return f"""# userandproduct logo pack

The final logo for userandproduct.com, decided {decided}: the Signal mark (four filled tiles of two sizes,
rotated 45 degrees) with the name "userandproduct" in Inter Display Bold, lowercase, tracking 0
(the typeface as designed).

Lockup geometry: the mark is 1.4 cap heights tall, centred midway between the cap band and the x-height
band (mark centre 31.08 units above the baseline at 100 units per em; cap height 72.75, x-height 51.56),
with a gap of 0.40 of the mark height (40.74 units). Both set on 9 Oct 2026 after the comparison in
`alignment.html`; tracking 0 chosen the same day (was -25). `python build.py --align cap|xheight|mid
--gap <fraction> --tracking <n>` rebuilds other variants.

Open the brand sheet: http://localhost/user-and-product/research/mockups/final-logo/brand-sheet.html

## Contents

- `svg/`: masters. Lockup (light, dark, black, white), stacked lockup (light, dark), mark (light, dark,
  black, white), wordmark (black, white), and `mark-currentcolor.svg` for inline use. Clean SVG: viewBox,
  no width or height, no live text, explicit fills.
- `png/`: every master on a transparent background (lockups and wordmarks 1200 and 2400 wide, stacked
  1200 and 2400 square, marks 256, 512 and 1024), plus the lockup on solid white and near-black at 2400.
- `favicon/`: `favicon.svg` (switches to the dark blue in dark themes), 16, 32 and 48 pixel PNGs,
  `favicon.ico` (16, 32, 48), Apple touch icon, 192 and 512 icons, a maskable 512 icon,
  `site.webmanifest` and `head-snippet.html` with the tags for the theme.
- `social/`: Open Graph images (light, dark), LinkedIn banners (light, dark), avatars (light, dark),
  an X header, and the site header strip (light, dark).
- `brand-sheet.html`: usage guide with colour, clear space, minimum sizes and a file index.
- `build.py`: the one source script.

## Rebuild

```
python build.py
```

Needs Python 3 with fontTools, uharfbuzz, skia-pathops, resvg-py and Pillow, plus
`research/mockups/tools/` (wordmark.py, render.py, brand_assets.py) and `research/mockups/fonts/inter/`.
The mark's path data is embedded in build.py. The script validates its own output.

## Colour tokens

| Token | Hex | Contrast |
|-------|-----|----------|
| Signal blue, light (mark) | `{tk['BLUE_L']}` | {rt['mark_light']:.1f}:1 on `{tk['WHITE']}` |
| Signal blue, dark (mark) | `{tk['BLUE_D']}` | {rt['mark_dark']:.1f}:1 on `{tk['NEAR']}` |
| Ink (wordmark, light) | `{tk['INK']}` | {rt['word_light']:.1f}:1 on `{tk['WHITE']}` |
| Off-white (wordmark, dark) | `{tk['OFF']}` | {rt['word_dark']:.1f}:1 on `{tk['NEAR']}` |
| Background, light | `{tk['WHITE']}` | |
| Background, dark | `{tk['NEAR']}` | |

## Licence

The wordmark is drawn from Inter Display Bold, under the SIL Open Font License 1.1 (licence file in
`research/mockups/fonts/inter/`). The OFL allows logos made from the outlines and requires no credit; its
conditions apply only when the font file itself is shared. The outlined name is not exclusive.
"""




def listing():
    out = {}
    for folder in ('svg', 'png', 'favicon', 'social'):
        out[folder] = sorted(os.listdir(path_of(folder)))
    return out


def validate():
    counts = {}
    for folder, names in listing().items():
        counts[folder] = len(names)
        for fn in names:
            p = path_of(f'{folder}/{fn}')
            if fn.endswith('.svg'):
                root = ET.parse(p).getroot()
                assert root.get('viewBox') and root.get('width') is None and root.get('height') is None, fn
                assert '<text' not in open(p, encoding='utf-8').read(), fn
            elif fn.endswith(('.png', '.ico')):
                with Image.open(p) as im:
                    im.load()
                    if fn == 'favicon.ico':
                        sizes = set(im.info.get('sizes', set()))
                        assert {(16, 16), (32, 32), (48, 48)} <= sizes, sizes
            elif fn.endswith('.webmanifest'):
                with open(p, encoding='utf-8') as f:
                    json.load(f)
    for fn in os.listdir(path_of('svg')):
        text = open(path_of(f'svg/{fn}'), encoding='utf-8').read()
        assert ('currentColor' in text) == (fn == 'mark-currentcolor.svg'), fn
    return counts


# ------------------------------------------------------------------ alignment comparison (owner review)
ALIGN_CSS = """
:root{--bg:#FFFFFF;--fg:#0B0B0C;--sub:#5C5C5F;--line:#E6E4DF;color-scheme:light dark}
@media (prefers-color-scheme:dark){:root{--bg:#0B0B0C;--fg:#F1EEE7;--sub:#A8A59F;--line:#2A2A2A}}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
main{max-width:1312px;margin:0 auto;padding:40px 16px 80px}
h1{font-size:clamp(26px,5vw,40px);line-height:1.1;margin:0 0 8px;letter-spacing:-.02em}
h2{font-size:22px;margin:48px 0 6px;padding-top:20px;border-top:1px solid var(--line)}
h3{font-size:15px;margin:24px 0 8px;color:var(--sub);font-weight:600}
p{margin:0 0 12px;max-width:72ch}
.lede{color:var(--sub);font-size:18px}
.key{display:flex;flex-wrap:wrap;gap:8px 24px;font-size:14px;color:var(--sub)}
.key span::before{content:"";display:inline-block;width:28px;height:0;border-top:2px dashed;margin-right:8px;vertical-align:middle}
.key .m::before{border-color:#E0372B}.key .x::before{border-color:#14A37F}
.pair{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(min(100%,600px),1fr))}
.panel{border:1px solid var(--line);border-radius:10px;padding:28px 20px;display:flex;align-items:center;justify-content:center}
.on-light{background:#FFFFFF}.on-dark{background:#0B0B0C;border-color:#2A2A2A}
.big{display:block;width:560px;max-width:100%;height:auto}
.strip{display:block;width:100%;height:auto;border:1px solid var(--line);border-radius:6px}
.mins{display:flex;flex-wrap:wrap;gap:16px}
.mins .panel{padding:20px 24px}
.min{display:block;width:120px;height:auto}
.note{font-size:14px;color:var(--sub);margin-top:8px}
.note code{font:13px ui-monospace,Consolas,monospace}
.cmp{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(min(100%,280px),1fr))}
.cmp .panel{flex-direction:column;gap:10px}
.cmp b{font-size:14px;color:#0B0B0C}.cmp .on-dark b{color:#F1EEE7}
"""

VARIANTS = [('A', 'cap', 'Current: mark centred on the cap band'),
            ('B', 'xheight', 'X-height: mark centred on the x-height band'),
            ('C', 'mid', 'Halfway: mark centred between the cap band and the x-height band')]


def guided(lock, align):
    """The lockup with dashed guides through the mark's centre (red) and the x-height centre (green)."""
    vx, vy, vw, vh = vbox(lock)
    sw = vw / 560 * 1.2
    dash = f'{fmt(vw / 560 * 6)} {fmt(vw / 560 * 4)}'
    lines = ''.join(f'<path d="M{fmt(vx)} {fmt(y)}H{fmt(vx + vw)}" stroke="{c}" stroke-width="{fmt(sw)}" '
                    f'stroke-dasharray="{dash}" fill="none"/>'
                    for y, c in ((mark_centre(align), '#E0372B'), (-XH / 2, '#14A37F')))
    return lock.replace('</svg>', lines + '</svg>')


def cls(svg_text, c):
    return svg_text.replace('<svg ', f'<svg class="{c}" ', 1)


GAPS = [('Current gap', 'original'), ('Gap 0.33', 0.33), ('Gap 0.40', 0.40)]


def gap_section():
    H = CAP * H_CAP
    rows = ['<h2 id="gap">Gap comparison, at alignment C</h2>'
            '<p>The owner chose C (halfway). These three differ only in the space between the mark and the name, '
            'given as a fraction of the mark height.</p>']
    side = []
    for title, g in GAPS:
        L, D = lockup(BLUE_L, INK, 'mid', g, track=-25), lockup(BLUE_D, OFF, 'mid', g, track=-25)
        gu = gap_units(g)
        px = gu * 2400 / vbox(L)[2]
        flag = f'--gap {g:.2f} --tracking -25' if g != 'original' else '--gap 0.2714 --tracking -25'
        note = (f'Gap <code>{gu:.2f}</code> SVG units = {gu / H:.2f} of the mark height ({H:.2f}); about '
                f'{px:.0f} px on the 2400 px render. Build with <code>python build.py --align mid {flag}</code>.')
        side.append(f'<div class="panel on-light"><b>{title}</b>{cls(L, "big")}</div>')
        strips = ''.join(
            f'<svg class="strip" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 72" role="img" '
            f'aria-label="Site header, {m}"><title>Site header, {m}</title>'
            f'<rect width="1280" height="72" fill="{WHITE if m == "light" else NEAR}"/>'
            f'{header_art(m, lk, lockup(BLUE_L if m == "light" else BLUE_D, INK if m == "light" else OFF, "cap", "original", track=-25))}</svg>'
            for m, lk in (('light', L), ('dark', D)))
        rows.append(f"""
<h3>{title}{f' ({gu / H:.2f})' if g == 'original' else ''}</h3>
<p class="note">{note}</p>
<div class="pair">
<div class="panel on-light">{cls(guided(L, 'mid'), 'big')}</div>
<div class="panel on-dark">{cls(guided(D, 'mid'), 'big')}</div>
</div>
<div class="pair" style="margin-top:12px">{strips}</div>
<div class="mins" style="margin-top:12px">
<div class="panel on-light">{cls(L, 'min')}</div>
<div class="panel on-dark">{cls(D, 'min')}</div>
</div>""")
    rows.insert(1, f'<h3>Side by side, no guides</h3><div class="cmp">{"".join(side)}</div>')
    return ''.join(rows)


TRACKS = [(-25, 'the original'), (-10, ''), (0, 'the typeface as designed; chosen'), (10, '')]


def tracking_section():
    H = CAP * H_CAP
    rows = ['<h2 id="tracking">Letter spacing, at alignment C and gap 0.40</h2>'
            '<p>Only the tracking of the name changes (in thousandths of an em, with the font kerning kept). '
            'The mark, its position and the gap (0.40 of the mark height) stay the same.</p>']
    side = []
    ref = {m: lockup(BLUE_L if m == 'light' else BLUE_D, INK if m == 'light' else OFF, 'cap', 'original', -25)
           for m in ('light', 'dark')}
    for t, label in TRACKS:
        L, D = lockup(BLUE_L, INK, 'mid', 0.40, t), lockup(BLUE_D, OFF, 'mid', 0.40, t)
        ww = word(t)[1][2]
        title = f'Tracking {t:+d}'.replace('+0', '0') + (f' ({label})' if label else '')
        note = (f'Tracking <code>{t:+d}</code>; name {ww:.1f} SVG units wide (lockup {vbox(L)[2]:.1f}); gap '
                f'{gap_units(0.40):.2f} units. Build with <code>python build.py --tracking {t}</code>' + (' (the default)' if t == 0 else '') + '.')
        side.append(f'<div class="panel on-light"><b>{t:+d}</b>'.replace('>+0<', '>0<') + f'{cls(L, "big")}</div>')
        strips = ''.join(
            f'<svg class="strip" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 72" role="img" '
            f'aria-label="Site header, {m}"><title>Site header, {m}</title>'
            f'<rect width="1280" height="72" fill="{WHITE if m == "light" else NEAR}"/>'
            f'{header_art(m, lk, ref[m])}</svg>' for m, lk in (('light', L), ('dark', D)))
        rows.append(f"""
<h3>{title}</h3>
<p class="note">{note}</p>
<div class="pair">
<div class="panel on-light">{cls(L, 'big')}</div>
<div class="panel on-dark">{cls(D, 'big')}</div>
</div>
<div class="pair" style="margin-top:12px">{strips}</div>
<div class="mins" style="margin-top:12px">
<div class="panel on-light">{cls(L, 'min')}</div>
<div class="panel on-dark">{cls(D, 'min')}</div>
</div>""")
    rows.insert(1, f'<h3>Side by side</h3><div class="cmp">{"".join(side)}</div>')
    return ''.join(rows)


def alignment_page():
    base = mark_centre('cap')
    out = []
    for key, align, title in VARIANTS:
        off = mark_centre(align) - base
        L, D = lockup(BLUE_L, INK, align, 'original', track=-25), lockup(BLUE_D, OFF, align, 'original', track=-25)
        note = (f'Mark centre at y = <code>{mark_centre(align):.2f}</code> (baseline 0, cap height '
                f'{CAP:.2f}, x-height {XH:.2f}); offset from A: <code>{off:+.2f}</code> SVG units '
                f'(about {off * 2400 / vbox(L)[2]:+.0f} px on the 2400 px render). Build with '
                f'<code>python build.py --align {align} --gap 0.2714 --tracking -25</code> (the gap and tracking at the time).')
        strips = ''.join(
            f'<svg class="strip" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 72" role="img" '
            f'aria-label="Site header, {m}"><title>Site header, {m}</title>'
            f'<rect width="1280" height="72" fill="{WHITE if m == "light" else NEAR}"/>'
            f'{header_art(m, lk, lockup(BLUE_L if m == "light" else BLUE_D, INK if m == "light" else OFF, "cap", "original", track=-25))}</svg>'
            for m, lk in (('light', L), ('dark', D)))
        out.append(f"""
<h2>{key}. {title}</h2>
<p class="note">{note}</p>
<h3>560 px, with guides</h3>
<div class="pair">
<div class="panel on-light">{cls(guided(L, align), 'big')}</div>
<div class="panel on-dark">{cls(guided(D, align), 'big')}</div>
</div>
<h3>Site header, 1280 x 72</h3>
<div class="pair">{strips}</div>
<h3>Minimum size, 120 px wide</h3>
<div class="mins">
<div class="panel on-light">{cls(L, 'min')}</div>
<div class="panel on-dark">{cls(D, 'min')}</div>
</div>""")
    out.append(gap_section())
    out.append(tracking_section())
    side = ''.join(f'<div class="panel on-light"><b>{k}</b>{cls(lockup(BLUE_L, INK, a, "original", track=-25), "big")}</div>'
                   for k, a, _ in VARIANTS)
    side_d = ''.join(f'<div class="panel on-dark"><b>{k}</b>{cls(lockup(BLUE_D, OFF, a, "original", track=-25), "big")}</div>'
                     for k, a, _ in VARIANTS)
    return f"""<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lockup alignment</title>
<style>{ALIGN_CSS}</style>
</head>
<body>
<main>
<h1>Lockup alignment</h1>
<p class="lede">Where the mark should sit next to the name. A is the lockup as decided; B and C move only the mark
down. Nothing else changes: same mark size, gap, colours and wordmark.</p>
<div class="key"><span class="m">Mark centre</span><span class="x">X-height centre</span></div>
<h3>Side by side, no guides</h3>
<div class="cmp">{side}</div>
<div class="cmp" style="margin-top:16px">{side_d}</div>
{''.join(out)}
</main>
</body>
</html>
"""


def main():
    global ALIGN, GAP, TRACK, WORD_D, WB
    args = sys.argv[1:]
    if '--align' in args:
        i = args.index('--align')
        ALIGN = args[i + 1]
        mark_centre(ALIGN)          # raises on an unknown value
        del args[i:i + 2]
    if '--gap' in args:
        i = args.index('--gap')
        GAP = float(args[i + 1])
        del args[i:i + 2]
    if '--tracking' in args:
        i = args.index('--tracking')
        TRACK = float(args[i + 1])
        TRACK = int(TRACK) if TRACK.is_integer() else TRACK
        del args[i:i + 2]
        WORD_D, WB = word()
    if '--alignment-page' in args:  # writes alignment.html only; leaves the pack alone
        write_text('alignment.html', alignment_page())
        print('wrote alignment.html')
        return
    steps = args or ['all']
    build_svgs()
    if 'all' in steps or 'png' in steps:
        build_pngs()
    if 'all' in steps or 'social' in steps:
        build_social()
    if 'all' in steps or 'sheet' in steps:
        tokens = dict(BLUE_L=BLUE_L, BLUE_D=BLUE_D, INK=INK, OFF=OFF, WHITE=WHITE, NEAR=NEAR)
        ratios = {'mark_light': ratio(BLUE_L, WHITE), 'mark_dark': ratio(BLUE_D, NEAR),
                  'word_light': ratio(INK, WHITE), 'word_dark': ratio(OFF, NEAR)}
        geo = dict(cap=CAP, small_tile_frac=SMALL_TILE_FRAC, lock_vb=vbox(SV['lockup-light']),
                   mark_h=CAP * H_CAP, track=TRACK, decided=DECIDED)
        write_text('brand-sheet.html', brand_sheet(SV, tokens, ratios, geo, listing()))
        write_text('README.md', readme(tokens, ratios, DECIDED))
        for k, v in ratios.items():
            print(f'contrast {k}: {v:.2f}:1')
    counts = validate()
    print('validated', ', '.join(f'{k} {v}' for k, v in counts.items()))


if __name__ == '__main__':
    main()
