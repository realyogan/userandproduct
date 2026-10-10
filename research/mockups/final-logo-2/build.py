"""Build the userandproduct logo pack 2: the owner's mark (Logo-3) in option C17, electric blue, flat.
Decided by the owner on 10 Oct 2026.

Run from anywhere:  python build.py      then:  python check.py
Writes svg/, png/, favicon/, social/, brand-sheet.html next to this file. Rerunnable; the output is
deterministic. The mark is read from ../Logo-3/svg/mark.svg (the clean evenodd master of the owner's
drawing); the wordmark and the lockup geometry come from ../Logo-3/geo.py, so this pack and the Logo-3
board can never drift apart.

Needs Python 3 with fontTools, uharfbuzz, skia-pathops, resvg-py and Pillow, plus
research/mockups/tools/wordmark.py and research/mockups/fonts/inter/.
"""
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LOGO3 = os.path.normpath(os.path.join(HERE, '..', 'Logo-3'))
sys.path.insert(0, LOGO3)

import pathops  # noqa: E402
from fontTools.svgLib.path import parse_path  # noqa: E402
from PIL import Image  # noqa: E402

import geo as G  # noqa: E402

DECIDED = '2026-10-10'

# ------------------------------------------------------------------ the mark, read from the Logo-3 master
MASTER = os.path.join(LOGO3, 'svg', 'mark.svg')
_master = open(MASTER, encoding='utf-8').read()
MARK_D = re.search(r' d="([^"]+)"', _master).group(1)
assert MARK_D == G.DISC_D + G.BAND_D + G.HEAD_D, 'Logo-3/svg/mark.svg no longer matches geo.py'
assert G.VB in _master

# ------------------------------------------------------------------ colour tokens (C17 Electric blue)
BLUE, BLUE_D = '#2E5BFF', '#7DB0FF'        # the disc: light backgrounds, dark mode
INK, OFF = G.INK, G.OFF                    # wordmark: #0B0B0C on light, #F1EEE7 on dark
WHITE = '#FFFFFF'
NEAR = '#111111'                           # near-black for the dark social set and the contrast figure
SITE_DARK = '#0B0B0C'                      # the site's dark-mode page (option-1 tokens)
MONO_BLACK, MONO_WHITE = '#0B0B0C', '#FFFFFF'

E = dict(key='electric', disc=BLUE, dark=BLUE_D, head=None, band=None, grad=False)


def bounds(d):
    p = pathops.Path()
    parse_path(d, p.getPen())
    return p.bounds


HEAD_B = bounds(G.HEAD_D)
BAND_B = bounds(G.BAND_D)
HEAD_H = HEAD_B[3] - HEAD_B[1]              # the head cut-out's height, in the owner's units
HEAD_FRAC = HEAD_H / (2 * G.R)              # ... as a share of the disc's diameter


# ------------------------------------------------------------------ writers
def path_of(rel):
    return os.path.join(HERE, *rel.split('/'))


def write(rel, text):
    p = path_of(rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(text)


def save(rel, img, **kw):
    p = path_of(rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    img.save(p, optimize=True, **kw)


def vbox(svg):
    return [float(v) for v in re.search(r'viewBox="([^"]+)"', svg).group(1).split()]


def nest(svg, x, y, w):
    """svg placed as a nested <svg> at x, y, w wide (height from its viewBox)."""
    vb = vbox(svg)
    h = w * vb[3] / vb[2]
    inner = re.sub(r'^<svg [^>]*>', '', svg.strip()).replace('</svg>', '')
    inner = re.sub(r'<title>.*?</title>', '', inner)
    return ('<svg x="%s" y="%s" width="%s" height="%s" viewBox="%s">%s</svg>'
            % (G.f1(x), G.f1(y), G.f1(w), G.f1(h), ' '.join(G.f1(v) for v in vb), inner)), h


def canvas(w, h, bg, art=''):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d"><rect width="%d" height="%d" fill="%s"/>%s'
            '</svg>' % (w, h, w, h, bg, art))


def render(svg, w, h=None):
    """Render at twice the size and step down: cleaner edges on the large social images."""
    img = G.png(svg, w * 2, None if h is None else h * 2)
    return img.resize((w, img.size[1] // 2), Image.LANCZOS)


def centred(svg, cw, ch, w, cx=None, cy=None):
    vb = vbox(svg)
    h = w * vb[3] / vb[2]
    cx = cw / 2 if cx is None else cx
    cy = ch / 2 if cy is None else cy
    return nest(svg, cx - w / 2, cy - h / 2, w)[0]


# ------------------------------------------------------------------ 1 masters
SV = {}


def solid_body(disc, figure=WHITE):
    """The disc with the head and band filled: an opaque mark (avatars, app icons, photos)."""
    return ('<path fill="%s" d="%s"/><path fill="%s" d="%s"/><path fill="%s" d="%s"/>'
            % (disc, G.DISC_D, figure, G.BAND_D, figure, G.HEAD_D))


def build_masters():
    black, white = G.mono(MONO_BLACK), G.mono(MONO_WHITE)
    SV['mark'] = G.mark_svg(E, 'light')
    SV['mark-dark'] = G.mark_svg(E, 'dark')
    SV['mark-black'] = G.mark_svg(black)
    SV['mark-white'] = G.mark_svg(white)
    SV['mark-currentcolor'] = G.doc(G.VB, G.mark_body('currentColor'), 'userandproduct mark')
    SV['mark-solid'] = G.doc(G.VB, solid_body(BLUE), 'userandproduct mark')


def build_lockups():
    black, white = G.mono(MONO_BLACK), G.mono(MONO_WHITE)
    SV['lockup-light'] = G.lockup_svg(E, 'light')
    SV['lockup-dark'] = G.lockup_svg(E, 'dark')
    SV['lockup-black'] = G.lockup_svg(black, word_fill=MONO_BLACK)
    SV['lockup-white'] = G.lockup_svg(white, word_fill=MONO_WHITE)
    SV['stacked-light'] = G.lockup_svg(E, 'light', stacked=True)
    SV['stacked-dark'] = G.lockup_svg(E, 'dark', stacked=True)
    SV['stacked-black'] = G.lockup_svg(black, word_fill=MONO_BLACK, stacked=True)
    SV['stacked-white'] = G.lockup_svg(white, word_fill=MONO_WHITE, stacked=True)


def flat(svg, w, bg, pad):
    """svg rendered w - 2 * pad wide, flattened on bg with pad on every side."""
    art = render(svg, w - 2 * pad)
    out = Image.new('RGBA', (w, art.size[1] + 2 * pad), bg)
    out.alpha_composite(art, (pad, pad))
    return out.convert('RGB')


def build_pngs():
    for size in (64, 128, 256, 512, 1024):
        save('png/mark-light-%d.png' % size, render(SV['mark'], size))
        save('png/mark-dark-%d.png' % size, render(SV['mark-dark'], size))
    for w in (236, 472, 944):
        save('png/lockup-light-%d.png' % w, render(SV['lockup-light'], w))
        save('png/lockup-dark-%d.png' % w, render(SV['lockup-dark'], w))
    for w in (400, 800):
        save('png/stacked-light-%d.png' % w, render(SV['stacked-light'], w))
        save('png/stacked-dark-%d.png' % w, render(SV['stacked-dark'], w))
    # one colour, flattened on solid grounds, for tools that cannot take a transparent file
    save('png/lockup-black-on-white-944.png', flat(SV['lockup-black'], 944, WHITE, 48))
    save('png/lockup-white-on-black-944.png', flat(SV['lockup-white'], 944, MONO_BLACK, 48))
    save('png/stacked-black-on-white-800.png', flat(SV['stacked-black'], 800, WHITE, 64))
    save('png/stacked-white-on-black-800.png', flat(SV['stacked-white'], 800, MONO_BLACK, 64))
    save('png/mark-black-on-white-1024.png', G.on(render(SV['mark-black'], 1024), WHITE))
    save('png/mark-white-on-black-1024.png', G.on(render(SV['mark-white'], 1024), MONO_BLACK))


# ------------------------------------------------------------------ 3 favicons and app icons
def avatar(bg_shape='square', ground=BLUE, figure=WHITE, scale=1.0):
    """The disc edge to edge (circle) or the disc colour as a full square, the figure in white.
    scale shrinks the figure about the disc's centre (for the maskable icon's safe zone)."""
    x0 = G.CX - G.R
    if bg_shape == 'circle':
        ground_el = '<path fill="%s" d="%s"/>' % (ground, G.DISC_D)
    else:
        ground_el = '<rect x="%s" y="%s" width="%s" height="%s" fill="%s"/>' % (
            G.num(x0), G.num(x0), G.num(2 * G.R), G.num(2 * G.R), ground)
    fig = '<path fill="%s" d="%s"/><path fill="%s" d="%s"/>' % (figure, G.BAND_D, figure, G.HEAD_D)
    if scale != 1.0:
        t = G.CX * (1 - scale)
        fig = '<g transform="translate(%s %s) scale(%s)">%s</g>' % (G.f1(t), G.f1(t), G.num(scale), fig)
    return G.doc(G.VB_BLEED, ground_el + fig, 'userandproduct')


def figure_reach():
    """How far the figure reaches from the disc's centre, as a share of the radius (corner points of the
    two bounding boxes: an upper bound)."""
    far = 0
    for b in (HEAD_B, BAND_B):
        for x in (b[0], b[2]):
            for y in (b[1], b[3]):
                far = max(far, ((x - G.CX) ** 2 + (y - G.CY) ** 2) ** .5)
    return far / G.R


HEAD_SNIPPET = """<!-- userandproduct icons (logo pack 2, electric blue). Copy the files in favicon/ to the site root,
     then paste these tags into the theme's <head> (wp_head). Do not also set a WordPress Site Icon, or the
     icon tags print twice. -->
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon-180.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#2E5BFF" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0B0B0C" media="(prefers-color-scheme: dark)">
"""


def build_favicons():
    # the SVG favicon keeps the cut-outs as true holes and switches to the dark-mode disc in dark themes
    fav = G.mark_svg(E, 'light', vb=G.VB_BLEED, label='userandproduct').replace(
        '<title>', '<style>@media (prefers-color-scheme:dark){path{fill:%s}}</style><title>' % BLUE_D, 1)
    write('favicon/favicon.svg', fav)
    # PNG favicons: the disc edge to edge with the figure filled white (they hold in light and dark tabs),
    # each rendered at its own size, never scaled down from a large PNG
    circle = avatar('circle')
    ico = {}
    for size in (16, 32, 48, 96, 192, 512):
        ico[size] = G.png(circle, size, size)
        save('favicon/favicon-%d.png' % size, ico[size])
    ico[48].save(path_of('favicon/favicon.ico'), format='ICO', sizes=[(16, 16), (32, 32), (48, 48)],
                 append_images=[ico[16], ico[32]])
    # Apple touch icon: an opaque full square; iOS rounds the corners itself
    save('favicon/apple-touch-icon-180.png', render(avatar('square'), 180).convert('RGB'))
    # maskable: the figure kept inside the 80 percent safe circle
    reach = figure_reach()
    scale = min(1.0, 0.8 / reach)
    save('favicon/maskable-512.png', render(avatar('square', scale=scale), 512).convert('RGB'))
    manifest = {
        'name': 'userandproduct', 'short_name': 'userandproduct', 'start_url': '/', 'display': 'standalone',
        'theme_color': BLUE, 'background_color': WHITE,
        'icons': [
            {'src': '/favicon-192.png', 'sizes': '192x192', 'type': 'image/png'},
            {'src': '/favicon-512.png', 'sizes': '512x512', 'type': 'image/png'},
            {'src': '/maskable-512.png', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'maskable'},
        ]}
    write('favicon/site.webmanifest', json.dumps(manifest, indent=2) + '\n')
    write('favicon/head-snippet.html', HEAD_SNIPPET)
    return reach, scale


# ------------------------------------------------------------------ 4 social
SOCIAL = []   # (file, caption, square?) for the brand sheet


def social(rel, img, caption, square=False):
    save('social/' + rel, img.convert('RGB'))
    SOCIAL.append((rel, caption, square))


def build_social():
    sq = avatar('square')
    # electric blue, white figure: the avatar is the disc colour as a full square, so a circle crop
    # shows exactly the disc; the figure sits well inside it (circle-safe)
    social('instagram-avatar-1080.png', render(sq, 1080), 'Instagram avatar, 1080 (circle-safe)', True)
    social('linkedin-logo-400.png', render(sq, 400), 'LinkedIn company logo, 400', True)
    social('linkedin-logo-300.png', render(sq, 300), 'LinkedIn company logo, 300', True)
    social('x-avatar-400.png', render(sq, 400), 'X avatar, 400', True)
    lw = SV['lockup-white']
    lr = vbox(lw)[2] / vbox(lw)[3]
    # LinkedIn banner: lockup 52 px tall, centred on 42 percent of the width (the logo covers the lower left)
    social('linkedin-banner-1128x191.png',
           render(canvas(1128, 191, BLUE, centred(lw, 1128, 191, 52 * lr, cx=1128 * 0.42)), 1128),
           'LinkedIn banner, 1128 x 191')
    social('og-1200x630.png', render(canvas(1200, 630, BLUE, centred(lw, 1200, 630, 760)), 1200),
           'Open Graph, 1200 x 630')
    # X header: centred, 84 px tall (mobile crops the top and bottom, the avatar covers the lower left)
    social('x-header-1500x500.png', render(canvas(1500, 500, BLUE, centred(lw, 1500, 500, 84 * lr)), 1500),
           'X header, 1500 x 500')
    # the dark set: near-black ground, the dark-mode disc with the cut-outs showing the ground, a 15 percent
    # margin so a circle crop never touches the disc
    dav = lambda s: render(canvas(s, s, NEAR, centred(G.mark_svg(E, 'dark', vb=G.VB_BLEED), s, s, s * .7)), s)  # noqa: E731
    social('instagram-avatar-1080-dark.png', dav(1080), 'Instagram avatar, dark, 1080 (circle-safe)', True)
    social('linkedin-logo-400-dark.png', dav(400), 'LinkedIn company logo, dark, 400', True)
    social('linkedin-logo-300-dark.png', dav(300), 'LinkedIn company logo, dark, 300', True)
    social('x-avatar-400-dark.png', dav(400), 'X avatar, dark, 400', True)
    ld = SV['lockup-dark']
    social('linkedin-banner-1128x191-dark.png',
           render(canvas(1128, 191, NEAR, centred(ld, 1128, 191, 52 * lr, cx=1128 * 0.42)), 1128),
           'LinkedIn banner, dark, 1128 x 191')
    social('og-1200x630-dark.png', render(canvas(1200, 630, NEAR, centred(ld, 1200, 630, 760)), 1200),
           'Open Graph, dark, 1200 x 630')
    social('x-header-1500x500-dark.png', render(canvas(1500, 500, NEAR, centred(ld, 1500, 500, 84 * lr)), 1500),
           'X header, dark, 1500 x 500')


# ------------------------------------------------------------------ 5 brand sheet
def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def inline(svg, cls):
    return svg.strip().replace('<svg ', '<svg class="%s" ' % cls, 1)


def geometry_svg():
    """The side lockup with the cap height, x-height and baseline drawn in, the disc's centre line,
    and the gap between disc and name."""
    lk = SV['lockup-light']
    vx, vy, vw, vh = vbox(lk)
    d = G.SIDE_D
    gap = G.SIDE_GAP * d
    pad = 40
    W, H = vw + 2 * pad + 120, vh + 2 * pad + 30
    ox, oy = vx - pad, vy - pad
    x1 = vx + vw + 6
    lines = []
    for y, name in ((-G.CAP, 'cap height'), (-G.XH, 'x-height'), (0, 'baseline'),
                    (G.SIDE_CY, 'disc centre')):
        dash = ' stroke-dasharray="4 3"' if name == 'disc centre' else ''
        col = '#C2410C' if name == 'disc centre' else '#8A8A92'
        lines.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width=".8"%s/>'
                     '<text x="%s" y="%s" font-size="12" fill="%s" dominant-baseline="middle">%s</text>'
                     % (G.f1(vx), G.f1(y), G.f1(x1), G.f1(y), col, dash, G.f1(x1 + 4), G.f1(y), col, name))
    gy = G.SIDE_CY + d / 2 + 14
    dim = ('<g stroke="#C2410C" stroke-width=".8"><line x1="%s" y1="%s" x2="%s" y2="%s"/>'
           '<line x1="%s" y1="%s" x2="%s" y2="%s"/><line x1="%s" y1="%s" x2="%s" y2="%s"/></g>'
           '<text x="%s" y="%s" font-size="11" fill="#C2410C" text-anchor="middle">gap 0.40 d</text>'
           '<g stroke="#C2410C" stroke-width=".8"><line x1="0" y1="%s" x2="%s" y2="%s"/></g>'
           '<text x="%s" y="%s" font-size="11" fill="#C2410C" text-anchor="middle">d = 1.4 cap</text>'
           % (G.f1(d), G.f1(gy), G.f1(d + gap), G.f1(gy), G.f1(d), G.f1(gy - 4), G.f1(d), G.f1(gy + 4),
              G.f1(d + gap), G.f1(gy - 4), G.f1(d + gap), G.f1(gy + 4), G.f1(d + gap / 2), G.f1(gy + 16),
              G.f1(gy), G.f1(d), G.f1(gy), G.f1(d / 2), G.f1(gy + 16)))
    body = re.sub(r'^<svg [^>]*>(<title>.*?</title>)?', '', lk.strip()).replace('</svg>', '')
    return ('<svg class="diagram" xmlns="http://www.w3.org/2000/svg" viewBox="%s %s %s %s" role="img" '
            'aria-label="Lockup geometry: disc 1.4 cap heights, centred between cap height and x-height, '
            'gap 0.40 of the disc" font-family="Inter, system-ui, sans-serif">%s%s%s</svg>'
            % (G.f1(ox), G.f1(oy), G.f1(W), G.f1(H), body, ''.join(lines), dim))


def clear_space_svg():
    """The mark with its clear space, x = the head cut-out's height, on every side: the dashed edge of the
    clear space, an x square on each side, and the head's height marked beside the head."""
    mk = G.mark_svg(E, 'light', vb=G.VB_BLEED)
    x0 = G.CX - G.R
    c = HEAD_H
    D = 2 * G.R
    ox, size = x0 - 1.25 * c, D + 2.5 * c
    body = re.sub(r'^<svg [^>]*>(<title>.*?</title>)?', '', mk.strip()).replace('</svg>', '')
    sq = ''
    for x, y in ((x0 - c, G.CY - c / 2), (x0 + D, G.CY - c / 2), (G.CX - c / 2, x0 - c), (G.CX - c / 2, x0 + D)):
        sq += '<rect x="%s" y="%s" width="%s" height="%s" fill="#C2410C" fill-opacity=".22"/>' % (
            G.f1(x), G.f1(y), G.f1(c), G.f1(c))
        sq += ('<text x="%s" y="%s" font-size="%s" fill="#C2410C" text-anchor="middle" dominant-baseline="central"'
               ' font-style="italic">x</text>' % (G.f1(x + c / 2), G.f1(y + c / 2), G.f1(c * .5)))
    hx = HEAD_B[2] + 60
    tick = c * .12
    bracket = ('<g stroke="#FFFFFF" stroke-width="16" stroke-linecap="round">'
               '<line x1="%s" y1="%s" x2="%s" y2="%s"/><line x1="%s" y1="%s" x2="%s" y2="%s"/>'
               '<line x1="%s" y1="%s" x2="%s" y2="%s"/></g>'
               '<text x="%s" y="%s" font-size="%s" fill="#FFFFFF" dominant-baseline="central" font-style="italic">x</text>'
               % (G.f1(hx), G.f1(HEAD_B[1]), G.f1(hx), G.f1(HEAD_B[3]),
                  G.f1(hx - tick), G.f1(HEAD_B[1]), G.f1(hx + tick), G.f1(HEAD_B[1]),
                  G.f1(hx - tick), G.f1(HEAD_B[3]), G.f1(hx + tick), G.f1(HEAD_B[3]),
                  G.f1(hx + tick * 1.6), G.f1((HEAD_B[1] + HEAD_B[3]) / 2), G.f1(c * .4)))
    return ('<svg class="diagram sq" xmlns="http://www.w3.org/2000/svg" viewBox="%s %s %s %s" role="img" '
            'aria-label="Clear space: x, the head cut-out&#8217;s height, on every side of the mark" '
            'font-family="Inter, system-ui, sans-serif">'
            '<rect x="%s" y="%s" width="%s" height="%s" fill="none" stroke="#C2410C" stroke-width="10" '
            'stroke-dasharray="40 28"/>%s%s%s</svg>'
            % (G.f1(ox), G.f1(ox), G.f1(size), G.f1(size),
               G.f1(x0 - c), G.f1(x0 - c), G.f1(D + 2 * c), G.f1(D + 2 * c), sq, body, bracket))


CSS = """
.bs{max-width:1120px;margin:0 auto;padding:var(--s6) var(--gutter) var(--s9)}
.bs-top{display:flex;align-items:center;justify-content:space-between;gap:var(--s4);padding:var(--s4) 0 var(--s6);
  border-bottom:1px solid var(--rule)}
.bs-top .logo img{width:236px;max-width:60vw;height:auto}
.bs h1{font-size:clamp(32px,5vw,var(--fs-h1));line-height:1.08;letter-spacing:-.02em;margin:var(--s7) 0 var(--s3)}
.bs h2{font-size:var(--fs-h2);line-height:1.15;letter-spacing:-.01em;margin:var(--s8) 0 var(--s3);padding-top:var(--s5);
  border-top:1px solid var(--rule)}
.bs h3{font:600 var(--fs-ui)/1.3 var(--font-ui);color:var(--ink-3);margin:0 0 var(--s2)}
.bs p{max-width:68ch;margin:0 0 var(--s3);color:var(--ink-2)}
.bs .lede{font-size:var(--fs-lead);color:var(--ink-2)}
.bs code{font:14px/1.4 ui-monospace,Consolas,monospace;overflow-wrap:anywhere}
.grid{display:grid;gap:var(--s4);grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr))}
.grid.two{grid-template-columns:repeat(auto-fit,minmax(min(100%,440px),1fr))}
.grid.four{grid-template-columns:repeat(auto-fit,minmax(min(100%,200px),1fr))}
.panel{border:1px solid var(--rule);border-radius:10px;padding:var(--s6) var(--s5);display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:var(--s3);min-height:180px}
.panel svg,.panel img{display:block;width:100%;height:auto}
.panel .lk{max-width:440px}.panel .mk{width:120px}.panel .st{max-width:300px}
.panel small{font:13px/1.3 var(--font-ui);opacity:.75;text-align:center}
.on-light{background:#FFFFFF;color:#0B0B0C;border-color:#E3E3E6}
.on-dark{background:#0B0B0C;color:#F1EEE7;border-color:#26262B}
.on-near{background:#111111;color:#F1EEE7;border-color:#26262B}
.on-grey{background:#8C8780;color:#FFFFFF;border-color:#8C8780}
.on-blue{background:#2E5BFF;color:#FFFFFF;border-color:#2E5BFF}
.sizes{display:flex;flex-wrap:wrap;align-items:flex-end;gap:var(--s5)}
.sizes figure{margin:0;display:flex;flex-direction:column;align-items:center;gap:6px}
.sizes figcaption{font-size:12px;opacity:.75}
.tabs{display:grid;gap:var(--s4);grid-template-columns:repeat(auto-fit,minmax(min(100%,220px),1fr))}
.tab{background:#DEE1E6;border-radius:10px;padding:8px 8px 0}
.tab.dark{background:#202124}
.tab .t{display:flex;align-items:center;gap:8px;background:#FFFFFF;border-radius:8px 8px 0 0;padding:8px 12px;
  font:13px/1.2 system-ui,sans-serif;color:#202124}
.tab.dark .t{background:#35363A;color:#E8EAED}
.tab img{display:block;flex:none;image-rendering:auto}
.zoom{display:flex;flex-wrap:wrap;gap:var(--s4);margin-top:var(--s4)}
.zoom figure{margin:0}.zoom img{display:block;image-rendering:pixelated;width:128px;height:128px;border:1px solid var(--rule)}
.zoom figcaption{font-size:12px;color:var(--ink-3);margin-top:4px}
.shots{display:grid;gap:var(--s4);grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr))}
.shots figure{margin:0}
.shots figure.sq img{max-width:220px}
.shots img{display:block;width:100%;height:auto;border:1px solid var(--rule);border-radius:6px}
.shots figure.round img{border-radius:50%}
figcaption{font-size:13px;color:var(--ink-3);margin-top:6px;overflow-wrap:anywhere}
.table{overflow-x:auto}
table{border-collapse:collapse;width:100%;font-size:var(--fs-ui)}
th,td{text-align:left;padding:10px 12px;border-bottom:1px solid var(--rule);vertical-align:middle}
th{font-size:13px;color:var(--ink-3);font-weight:600}
@media (max-width:600px){thead{display:none}table,tbody,tr,td{display:block}tr{padding:10px 0;border-bottom:1px solid var(--rule)}
  td{border:0;padding:2px 0}}
.sw{display:inline-block;width:28px;height:28px;border-radius:6px;border:1px solid var(--rule);vertical-align:middle}
.dl{display:grid;grid-template-columns:max-content 1fr;gap:6px 24px;font-size:var(--fs-ui)}
.dl dt{color:var(--ink-3)}.dl dd{margin:0}
@media (max-width:560px){.dl{grid-template-columns:1fr}.dl dd{margin-bottom:8px}}
.figure-box{background:#FFFFFF;border:1px solid #E3E3E6;border-radius:10px;padding:var(--s5);color:#0B0B0C}
.diagram{display:block;width:100%;height:auto;max-width:880px;margin:0 auto}
.diagram.sq{max-width:300px}
.rules{display:grid;gap:var(--s4);grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr))}
.rules ul{margin:0;padding-left:20px;font-size:var(--fs-ui)}.rules li{margin-bottom:6px}
.do h3{color:#1F7A3D}.dont h3{color:#B3141C}
:root[data-theme="dark"] .do h3{color:#6FCF8E}:root[data-theme="dark"] .dont h3{color:#F38A8E}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .do h3{color:#6FCF8E}
  :root:not([data-theme="light"]) .dont h3{color:#F38A8E}}
.files{columns:3 220px;column-gap:var(--s5);padding:0;list-style:none;margin:0}
.files li{break-inside:avoid;font-size:14px;margin-bottom:4px;overflow-wrap:anywhere}
.files .h{font-weight:600;margin-top:12px;color:var(--ink-3)}
.bs-foot{margin-top:var(--s8);color:var(--ink-3);font-size:14px}
"""

TOGGLE = ('<button class="theme-toggle" type="button" data-theme-toggle aria-label="Switch theme">'
          '<svg class="i-moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" '
          'd="M20.3 14.6A8.5 8.5 0 0 1 9.4 3.7a8.5 8.5 0 1 0 10.9 10.9Z"/></svg><svg class="i-sun" viewBox="0 0 24 24" '
          'aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.5" fill="currentColor"/><g stroke="currentColor" '
          'stroke-width="2" stroke-linecap="round"><path d="M12 2v2.5M12 19.5V22M2 12h2.5M19.5 12H22M4.9 4.9l1.8 1.8M17.3 '
          '17.3l1.8 1.8M4.9 19.1l1.8-1.8M17.3 6.7l1.8-1.8"/></g></svg></button>')


def contrasts():
    r = G.ratio
    return dict(blue_white=r(BLUE, WHITE), blued_near=r(BLUE_D, NEAR), blued_site=r(BLUE_D, SITE_DARK),
                blue_near=r(BLUE, NEAR), white_on_blue=r(WHITE, BLUE), ink_white=r(INK, WHITE),
                off_site=r(OFF, SITE_DARK), off_near=r(OFF, NEAR), near_on_blued=r(NEAR, BLUE_D))


def listing():
    out = {}
    for folder in ('svg', 'png', 'favicon', 'social'):
        out[folder] = sorted(os.listdir(path_of(folder)))
    return out


def brand_sheet(rt, reach, scale):
    L = lambda k: inline(SV[k], 'lk')  # noqa: E731
    M = lambda k: inline(SV[k], 'mk')  # noqa: E731
    S = lambda k: inline(SV[k], 'st')  # noqa: E731
    rows = [
        ('Electric blue', 'The disc on light backgrounds; the ground of the social set and app icons',
         BLUE, '%.1f:1 on #FFFFFF' % rt['blue_white']),
        ('Electric blue, dark mode', 'The disc on dark backgrounds',
         BLUE_D, '%.1f:1 on #111111, %.1f:1 on #0B0B0C' % (rt['blued_near'], rt['blued_site'])),
        ('White', 'The figure where the mark is opaque (avatars, app icons); one-colour white',
         WHITE, '%.1f:1 on electric blue' % rt['white_on_blue']),
        ('Ink', 'The wordmark on light; one-colour black', INK, '%.1f:1 on #FFFFFF' % rt['ink_white']),
        ('Off-white', 'The wordmark on dark', OFF, '%.1f:1 on #0B0B0C' % rt['off_site']),
        ('Near-black', 'The ground of the dark social set', NEAR, '(background)'),
    ]
    trs = ''.join('<tr><td><span class="sw" style="background:%s"></span></td><td>%s</td><td><code>%s</code></td>'
                  '<td>%s</td><td>%s</td></tr>' % (h, n, h, c, u) for n, u, h, c in rows)
    bleed = G.mark_svg(E, 'light', vb=G.VB_BLEED).strip()
    sizes = ''.join('<figure>%s<figcaption>%d px</figcaption></figure>'
                    % (bleed.replace('<svg ', '<svg width="%d" height="%d" style="width:%dpx" ' % (s, s, s), 1), s)
                    for s in (24, 32, 48, 64, 96, 128))
    shots = ''.join('<figure%s><img src="social/%s" alt="%s" loading="lazy"><figcaption>%s</figcaption></figure>'
                    % (' class="sq"' if sq else '', f, esc(c), esc(c)) for f, c, sq in SOCIAL if 'dark' not in f)
    shots_d = ''.join('<figure%s><img src="social/%s" alt="%s" loading="lazy"><figcaption>%s</figcaption></figure>'
                      % (' class="sq"' if sq else '', f, esc(c), esc(c)) for f, c, sq in SOCIAL if 'dark' in f)
    circles = ''.join('<figure class="sq round"><img src="social/%s" alt="%s, in a circle crop" loading="lazy">'
                      '<figcaption>%s, circle crop</figcaption></figure>' % (f, esc(c), esc(c.replace(' (circle-safe)', '')))
                      for f, c, sq in SOCIAL if f.startswith('instagram'))
    mono = [('lockup-black-on-white-944.png', 'Lockup, black on white, 944 wide', False),
            ('lockup-white-on-black-944.png', 'Lockup, white on black, 944 wide', False),
            ('stacked-black-on-white-800.png', 'Stacked, black on white, 800 wide', False),
            ('stacked-white-on-black-800.png', 'Stacked, white on black, 800 wide', False),
            ('mark-black-on-white-1024.png', 'Mark, black on white, 1024', True),
            ('mark-white-on-black-1024.png', 'Mark, white on black, 1024', True)]
    monos = ''.join('<figure%s><img src="png/%s" alt="%s" loading="lazy"><figcaption>%s</figcaption></figure>'
                    % (' class="sq"' if sq else '', f, esc(c), esc(c)) for f, c, sq in mono)
    idx = []
    for folder, names in listing().items():
        idx.append('<li class="h">%s/</li>' % folder)
        idx += ['<li><a href="%s/%s">%s</a></li>' % (folder, n, n) for n in names]
    idx += ['<li class="h">source</li>', '<li><a href="build.py">build.py</a></li>',
            '<li><a href="check.py">check.py</a></li>', '<li><a href="README.md">README.md</a></li>']
    head_at_24 = 24 * HEAD_FRAC
    gap_units = G.SIDE_GAP * G.SIDE_D
    return f"""<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>userandproduct brand sheet</title>
<link rel="icon" href="favicon/favicon.ico" sizes="48x48">
<link rel="icon" href="favicon/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../mockup.css">
<style>{CSS}</style>
</head>
<body>
<div class="bs">
<div class="bs-top">
<span class="logo"><img class="l-light" src="svg/lockup-light.svg" alt="userandproduct" width="236" height="29"><img class="l-dark" src="svg/lockup-dark.svg" alt="userandproduct" width="236" height="29"></span>
{TOGGLE}
</div>
<main>
<h1>userandproduct brand sheet</h1>
<p class="lede">The owner's own mark, a solid disc with a person cut out of it (a rounded head over a curved
band), in electric blue, beside the name set in Inter Display Bold. Decided on {DECIDED} (option C17 on the
Logo 3 board). Every file here is built by <code>build.py</code> from the owner's drawing.</p>

<h2>Lockup</h2>
<p>The primary logo: the mark at the left, the name at the right. On a page the cut-outs are true holes, so the
background shows through the figure. Light on white and light greys, dark on near-black.</p>
<div class="grid">
<div class="panel on-light">{L('lockup-light')}<small>lockup-light.svg</small></div>
<div class="panel on-dark">{L('lockup-dark')}<small>lockup-dark.svg</small></div>
</div>

<h2>Stacked</h2>
<p>The mark above the name, for square and centred placements. The disc is three cap heights across here.</p>
<div class="grid">
<div class="panel on-light">{S('stacked-light')}<small>stacked-light.svg</small></div>
<div class="panel on-dark">{S('stacked-dark')}<small>stacked-dark.svg</small></div>
</div>

<h2>Mark</h2>
<p>The mark alone, for avatars, app icons and favicons. Where it sits on a page the figure is empty; where the
mark has to be opaque (an avatar, an app icon, over a photograph) the figure is white.</p>
<div class="grid four">
<div class="panel on-light">{M('mark')}<small>mark.svg</small></div>
<div class="panel on-dark">{M('mark-dark')}<small>mark-dark.svg</small></div>
<div class="panel on-grey">{M('mark-solid')}<small>mark-solid.svg (white figure), on grey</small></div>
<div class="panel on-light" style="color:#2E5BFF">{M('mark-currentcolor')}<small style="color:#0B0B0C">mark-currentcolor.svg (takes the text colour)</small></div>
</div>

<h2 id="one-colour">One colour</h2>
<p>Black and white, for one-ink print, partner pages that ask for one colour, and article thumbnails (black or
white by the background).</p>
<div class="grid two">
<div class="panel on-light">{L('lockup-black')}<small>lockup-black.svg</small></div>
<div class="panel on-blue">{L('lockup-white')}<small>lockup-white.svg, on electric blue</small></div>
<div class="panel on-light">{S('stacked-black')}<small>stacked-black.svg</small></div>
<div class="panel on-dark">{S('stacked-white')}<small>stacked-white.svg</small></div>
</div>
<div class="grid four" style="margin-top:16px">
<div class="panel on-light">{M('mark-black')}<small>mark-black.svg</small></div>
<div class="panel on-dark">{M('mark-white')}<small>mark-white.svg</small></div>
</div>

<h2>Colour</h2>
<p>Two blues, the ink and white, and nothing else. Contrast is the WCAG 2 ratio against the ground the colour is used
on, computed by the build; 3:1 is the bar for a graphic, 4.5:1 for text.</p>
<div class="table"><table>
<thead><tr><th></th><th>Token</th><th>Hex</th><th>Contrast</th><th>Use</th></tr></thead>
<tbody>{trs}</tbody>
</table></div>
<p style="margin-top:12px">The light disc on near-black is only {rt['blue_near']:.1f}:1, which is why dark mode
switches to <code>{BLUE_D}</code>. The near-black figure on the dark disc is {rt['near_on_blued']:.1f}:1.</p>

<h2>Lockup geometry</h2>
<p>Measured in the wordmark's own units (100 per em; cap height {G.CAP:.2f}, x-height {G.XH:.2f}).</p>
<div class="figure-box">{geometry_svg()}</div>
<dl class="dl" style="margin-top:16px">
<dt>Wordmark</dt><dd>userandproduct, Inter Display Bold, lowercase, tracking 0, kerned, outlined to one path</dd>
<dt>Disc, side lockup</dt><dd>1.4 cap heights across ({G.SIDE_D:.1f} units)</dd>
<dt>Disc centre</dt><dd>Midway between the cap height and the x-height, {-G.SIDE_CY:.2f} units above the baseline</dd>
<dt>Gap</dt><dd>0.40 of the disc ({gap_units:.1f} units)</dd>
<dt>Stacked</dt><dd>Disc 3 cap heights across, centred over the name, gap 0.76 cap heights</dd>
<dt>Margin</dt><dd>4 units of empty space inside every viewBox</dd>
<dt>On the site</dt><dd>Header 236 px wide, footer 168 px wide</dd>
</dl>

<h2>Clear space and minimum size</h2>
<p>Clear space is the height of the head cut-out ({HEAD_FRAC * 100:.0f} percent of the disc). Keep at least that
much empty on every side of the mark, and around the lockup measured from the disc.</p>
<div class="figure-box" style="display:flex;justify-content:center">{clear_space_svg()}</div>
<p style="margin-top:16px">Never smaller than 24 px across the disc (the head is then about {head_at_24:.1f} px tall).
The favicon files are the one exception: they are drawn for browser tabs at 16 and 32 px and are used only
there.</p>
<div class="panel on-light" style="align-items:flex-start"><div class="sizes">{sizes}</div></div>

<h2>Favicons and app icons</h2>
<p>The SVG favicon keeps the figure empty and switches to the dark-mode disc in dark browser themes. The PNG and
ICO favicons are the disc edge to edge with the figure filled white, so they read in light and dark tabs alike.
Each size is rendered at its own size.</p>
<div class="tabs">
<div class="tab"><div class="t"><img src="favicon/favicon-16.png" width="16" height="16" alt="">favicon-16.png</div></div>
<div class="tab dark"><div class="t"><img src="favicon/favicon-16.png" width="16" height="16" alt="">favicon-16.png</div></div>
<div class="tab"><div class="t"><img src="favicon/favicon.svg" width="16" height="16" alt="">favicon.svg</div></div>
<div class="tab dark"><div class="t"><img src="favicon/favicon-32.png" width="32" height="32" alt="">favicon-32.png</div></div>
</div>
<div class="zoom">
<figure><img src="favicon/favicon-16.png" alt="16 pixel favicon, enlarged"><figcaption>16 px, enlarged</figcaption></figure>
<figure><img src="favicon/favicon-32.png" alt="32 pixel favicon, enlarged"><figcaption>32 px, enlarged</figcaption></figure>
<figure><img src="favicon/favicon-48.png" alt="48 pixel favicon, enlarged"><figcaption>48 px, enlarged</figcaption></figure>
</div>
<div class="shots" style="margin-top:16px">
<figure class="sq"><img src="favicon/apple-touch-icon-180.png" alt="Apple touch icon" loading="lazy" style="border-radius:22%"><figcaption>apple-touch-icon-180.png (iOS rounds the corners)</figcaption></figure>
<figure class="sq"><img src="favicon/favicon-512.png" alt="512 pixel icon" loading="lazy" style="border:0"><figcaption>favicon-512.png (manifest)</figcaption></figure>
<figure class="sq"><img src="favicon/maskable-512.png" alt="Maskable 512 pixel icon" loading="lazy"><figcaption>maskable-512.png (figure scaled to {scale:.2f} to sit in the safe circle)</figcaption></figure>
</div>

<h2>Social set</h2>
<p>Electric blue with the white figure. The avatars are the disc colour as a full square, so a circle crop shows the
disc exactly and the figure sits well inside it. Banners carry the white lockup.</p>
<div class="shots">{shots}{circles}</div>
<h3 style="margin-top:24px">Dark set, on near-black</h3>
<div class="shots">{shots_d}</div>

<h2>Monochrome on solid</h2>
<p>The one-colour versions flattened on white and black, for tools that cannot take a transparent file.</p>
<div class="shots">{monos}</div>

<h2>Usage rules</h2>
<div class="rules">
<div class="do"><h3>Do</h3><ul>
<li>Use the files as supplied: light, dark, black, white, or the solid mark with the white figure.</li>
<li>Pick light or dark by the background, not by taste.</li>
<li>Keep clear space equal to the head cut-out's height on every side.</li>
<li>Keep the mark at 24 px or larger (favicons excepted).</li>
<li>Scale proportionally.</li>
</ul></div>
<div class="dont"><h3>Don't</h3><ul>
<li>Recolour it outside the two blues, black and white.</li>
<li>Use gradients with it on the site (social backgrounds only, if ever).</li>
<li>Stretch, rotate, outline it, or add shadows or glows.</li>
<li>Fill the head and band in a second colour.</li>
<li>Retype the name in another font or in capitals.</li>
<li>Put the light disc on near-black; use the dark-mode blue there.</li>
</ul></div>
</div>

<h2>Files</h2>
<ul class="files">{''.join(idx)}</ul>

<p class="bs-foot">Rebuild with <code>python build.py</code>, then <code>python check.py</code>, in
research/mockups/final-logo-2/. The previous pack (the four-tile mark) stays in
<a href="../final-logo/brand-sheet.html">final-logo/</a> for reference.</p>
</main>
</div>
<script src="../mockup.js"></script>
</body>
</html>
"""


# ------------------------------------------------------------------ main
def status(n, st, note):
    try:
        import subprocess
        subprocess.run([sys.executable, os.path.join(HERE, 'status.py'), str(n), st, note], check=False)
    except Exception:  # noqa: BLE001
        pass


def main():
    for d in ('svg', 'png', 'favicon', 'social'):
        if os.path.isdir(path_of(d)):
            shutil.rmtree(path_of(d))
    build_masters()
    build_lockups()
    for k, v in SV.items():
        write('svg/%s.svg' % k, v)
    build_pngs()
    status(1, 'done', 'Masters: mark, dark, black, white, currentColor, solid, from Logo-3/svg/mark.svg')
    status(2, 'done', 'Lockups: side and stacked in light, dark, black, white; PNGs at 236/472/944 and 400/800')
    reach, scale = build_favicons()
    status(3, 'done', 'Favicons 16 to 512, favicon.ico, favicon.svg with dark query, Apple touch, manifest')
    build_social()
    status(4, 'done', 'Social set: %d images, electric blue and near-black' % len(SOCIAL))
    rt = contrasts()
    write('brand-sheet.html', brand_sheet(rt, reach, scale))
    status(5, 'done', 'Brand sheet written on the shared tokens, light and dark')
    print('svg %d, png %d, favicon %d, social %d' % tuple(len(v) for v in listing().values()))
    print('contrast: disc on white %.2f, dark disc on #111 %.2f, on #0B0B0C %.2f' % (
        rt['blue_white'], rt['blued_near'], rt['blued_site']))
    print('head cut-out %.1f units, %.3f of the disc; figure reach %.3f of the radius, maskable scale %.3f' % (
        HEAD_H, HEAD_FRAC, reach, scale))


if __name__ == '__main__':
    main()
