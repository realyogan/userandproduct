"""Writes index.html, the Logo 3 board. Called by build.py."""
from html import escape as e

import geo as G

CSS = """
.l3{max-width:1180px;margin:0 auto;padding:24px var(--gutter) 96px}
.l3 a{color:var(--signal)}
.bar{display:flex;justify-content:space-between;align-items:center;gap:16px;margin:0 0 24px}
.bar p{margin:0;font-size:var(--fs-meta)}
.toggle{border:1px solid var(--rule);background:var(--panel);color:var(--ink);border-radius:999px;padding:6px 14px;cursor:pointer;font:500 14px/1 var(--font-ui)}
.l3 h1{font-family:var(--font-display);font-weight:700;font-size:clamp(32px,5vw,52px);line-height:1.05;letter-spacing:-.01em;margin:0 0 12px}
.lede{font-size:18px;line-height:1.5;color:var(--ink-2);max-width:68ch;margin:0 0 24px}
.hero{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:0 0 12px}
.hero .g{min-height:280px}
.hero img{width:220px;height:220px;max-width:100%;height:auto}
.toc{margin:24px 0 0;padding:0;list-style:none;display:flex;flex-wrap:wrap;gap:8px}
.toc a{display:inline-flex;align-items:center;gap:8px;border:1px solid var(--rule);border-radius:999px;padding:5px 12px 5px 6px;text-decoration:none;color:var(--ink);font-size:14px}
.toc img{width:20px;height:20px}
.tw{overflow-x:auto;margin:16px 0 0;-webkit-overflow-scrolling:touch}
table.opts{border-collapse:collapse;font-size:14px;min-width:760px;width:100%}
.opts th,.opts td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--rule);vertical-align:middle}
.opts th{font-size:12px;letter-spacing:.05em;text-transform:uppercase;color:var(--ink-2);font-weight:600}
.opts td.n{white-space:nowrap;font-variant-numeric:tabular-nums}
.sw{display:inline-block;width:14px;height:14px;border-radius:50%;vertical-align:-2px;margin-right:6px;border:1px solid rgba(128,128,128,.4)}
.pass{color:var(--ink)}.fail{color:var(--ink-3)}
.grp{margin-top:72px;padding:20px 0 0;border-top:4px solid var(--ink)}
.grp h2{font-family:var(--font-display);font-size:clamp(26px,4vw,36px);margin:0 0 6px}
.grp p{margin:0 0 8px;color:var(--ink-2);max-width:72ch}
.mk{border-top:2px solid var(--rule-strong);margin-top:48px;padding-top:20px}
.mk__head{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 16px;margin-bottom:8px}
.mk__num{font-family:var(--font-display);font-weight:700;font-size:15px;color:var(--signal);margin:0}
.mk h3{font-family:var(--font-display);font-weight:700;font-size:30px;line-height:1.1;margin:0}
.mk__note{margin:0 0 6px;color:var(--ink-2);max-width:72ch}
.mk__facts{margin:0 0 18px;font-size:var(--fs-meta);color:var(--ink-2)}
.mk__facts code{font-size:13px}
.row{margin:0 0 22px}
.row h4{font-size:12px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;margin:0 0 8px;color:var(--ink-2)}
.pair{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.trio{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.g{min-width:0;border-radius:var(--radius);padding:18px;display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:18px;min-height:100px;margin:0}
.g--w{background:#FFFFFF;border:1px solid #E3E3E6;color:#55555C}
.g--k{background:#111111;border:1px solid #2A2A2E;color:#9A9AA2}
.g--pk{background:#000000;border:1px solid #2A2A2E;color:#9A9AA2}
.g img{display:block}
.g figcaption{width:100%;text-align:center;font-size:11px}
.av{width:110px;height:110px}
.av--c{border-radius:50%}
.strip{justify-content:flex-start;gap:16px}
.strip figure{margin:0;display:flex;flex-direction:column;align-items:center;gap:6px;width:120px}
.strip a{display:block}
.m160{width:160px;height:160px;max-width:100%;height:auto}
.lk{width:236px;height:auto;max-width:100%}
.st{width:120px;height:auto}
.fav{display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:12px}
.fav .z{width:96px;height:96px;image-rendering:pixelated}
.prev{display:grid;gap:12px;grid-template-columns:minmax(0,1fr)}
@media (min-width:900px){.prev{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}}
.mock{border:1px solid var(--rule);border-radius:var(--radius);background:var(--panel);color:var(--ink);overflow:hidden;min-width:0}
.mock__label{font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-3);padding:8px 12px 0;margin:0}
.ig{display:flex;gap:18px;align-items:center;padding:14px 16px 16px}
.ig__av{width:110px;height:110px;border-radius:50%;flex:none}
.ig__user{font:600 17px/1.2 var(--font-ui);margin:0 0 8px}
.ig__stats{list-style:none;margin:0 0 8px;padding:0;display:flex;flex-wrap:wrap;gap:4px 14px;font-size:13px}
.ig__stats li{white-space:nowrap}
.ig__stats b{font-weight:700}
.ig__name{font:600 13px/1.3 var(--font-ui);margin:0}
.ig__bio{font-size:13px;line-height:1.35;margin:2px 0 0;color:var(--ink-2)}
.li__banner{height:72px;margin-top:8px}
.li__body{padding:0 16px 12px;display:flex;gap:14px;align-items:flex-end;flex-wrap:wrap}
.li__logo{width:100px;height:100px;border-radius:4px;border:3px solid var(--panel);margin-top:-44px;display:block;flex:none}
.li__name{font:700 18px/1.2 var(--font-ui);margin:0 0 2px}
.li__meta{font-size:13px;color:var(--ink-2);margin:0 0 4px}
.li__post{border-top:1px solid var(--rule);margin:0 16px;padding:12px 0 14px;display:flex;gap:10px;align-items:flex-start}
.li__post img{width:48px;height:48px;border-radius:2px;flex:none}
.li__post b{display:block;font:600 14px/1.25 var(--font-ui)}
.li__post small{display:block;font-size:12px;color:var(--ink-3)}
.li__post p{margin:6px 0 0;font-size:13px;line-height:1.4;color:var(--ink-2)}
.tabs{display:flex;align-items:flex-end;gap:2px;padding:10px 10px 0;overflow:hidden}
.tabs--l{background:#DEE1E6}
.tabs--d{background:#202124}
.tab{display:flex;align-items:center;gap:8px;height:34px;padding:0 12px;border-radius:8px 8px 0 0;font:400 12px/1 var(--font-ui);min-width:0}
.tab img{width:16px;height:16px;flex:none}
.tab span{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.tabs--l .tab--on{background:#FFFFFF;color:#202124}
.tabs--d .tab--on{background:#35363A;color:#E8EAED}
.tabs--l .tab--off{color:#5F6368}
.tabs--d .tab--off{color:#9AA0A6}
.tab .x{margin-left:6px;opacity:.6}
.tabs__url{height:10px}
.tabs--l + .tabs__url{background:#FFFFFF}
.tabs--d + .tabs__url{background:#35363A}
.thumb{display:block;width:100%;max-width:600px;height:auto;border-radius:4px}
.note{border:1px solid var(--signal);background:var(--signal-wash);border-radius:var(--radius);padding:12px 16px;margin:12px 0 0;font-size:15px;line-height:1.5;color:var(--ink)}
.note p{margin:0}
.files{font-size:15px;line-height:1.55;color:var(--ink-2);padding-left:20px;max-width:90ch}
.files code{font-size:13px;color:var(--ink);white-space:normal;overflow-wrap:anywhere}
.files li{margin:0 0 6px}
.foot{margin-top:64px;font-size:var(--fs-meta);color:var(--ink-3)}
@media (max-width:640px){.pair,.trio{grid-template-columns:minmax(0,1fr)}.hero{grid-template-columns:minmax(0,1fr)}.hero .g{min-height:220px}.fav .z{width:64px;height:64px}.ig{flex-wrap:wrap}}
"""

THRESHOLD = 3.0   # WCAG 2 non-text contrast for graphics


def r(a, b):
    return G.ratio(a, b)


def fmt_r(v):
    return '%.1f:1' % v


def facts(o):
    """Contrast numbers and the ground each option needs."""
    if o['grad']:
        lo = [r(c, G.WHITE) for c in (o['a'], o['b'])]
        ld = [r(c, G.NEAR) for c in (o['a'], o['b'])]
        fig = [r(G.WHITE, c) for c in (o['a'], o['b'])]
        need = 'Social backgrounds and avatars only. White figure on the gradient: %s to %s.' % (
            fmt_r(min(fig)), fmt_r(max(fig)))
        return dict(white='%s to %s' % (fmt_r(min(lo)), fmt_r(max(lo))),
                    dark='%s to %s' % (fmt_r(min(ld)), fmt_r(max(ld))),
                    dark_disc='same', need=need, second='none')
    w, d, dd = r(o['disc'], G.WHITE), r(o['disc'], G.NEAR), r(o['dark'], G.NEAR)
    ok_w, ok_d, ok_dd = w >= THRESHOLD, d >= THRESHOLD, dd >= THRESHOLD
    if o['head'] == G.INK and o['band'] == G.INK:
        need = ('Dark grounds, or the color used as a field. On white the disc edge is soft (%s) '
                'but the ink figure carries the mark (%s on the disc).' % (fmt_r(w), fmt_r(r(G.INK, o['disc']))))
    elif o['key'] == 'twotone':
        need = ('White grounds (%s). On near-black the disc edge is soft (%s); the filled white head and '
                'light band still read (head %s, band %s on the disc).' % (
                    fmt_r(w), fmt_r(d), fmt_r(r(o['head'], o['disc'])), fmt_r(r(o['band'], o['disc']))))
    elif ok_w and ok_d:
        need = 'Both grounds: the one color passes on white and on near-black.'
        if o['dark'] != o['disc']:
            need += ' The brighter %s on dark gives more lift (%s).' % (o['dark'], fmt_r(dd))
    elif ok_w and ok_dd:
        need = 'White grounds. On near-black it fails (%s), so dark mode uses %s (%s).' % (
            fmt_r(d), o['dark'], fmt_r(dd))
    elif ok_d:
        need = 'Dark grounds.'
    else:
        need = 'Check by eye.'
    second = []
    if o['head']:
        second.append('head %s' % o['head'])
    if o['band']:
        second.append('band %s' % o['band'])
    return dict(white=fmt_r(w), dark=fmt_r(d), dark_disc='%s (%s)' % (o['dark'], fmt_r(dd)) if o['dark'] != o['disc'] else 'same',
                need=need, second=', '.join(second) if second else 'none (cut-outs show the ground)')


def swatch(c):
    return '<span class="sw" style="background:%s" aria-hidden="true"></span>' % c


def table(items):
    rows = ''
    for o in items:
        f = facts(o)
        rows += ('<tr><td class="n">%s</td><td><a href="#%s">%s</a></td><td class="n">%s<code>%s</code></td>'
                 '<td>%s</td><td class="n">%s</td><td class="n">%s</td><td>%s</td><td>%s</td></tr>' % (
                     o['num'], o['key'], e(o['name']), swatch(o['disc']), o['disc'], e(f['second']), f['white'],
                     f['dark'], e(f['dark_disc']), e(f['need'])))
    return ('<div class="tw"><table class="opts"><thead><tr><th>No.</th><th>Option</th><th>Disc</th>'
            '<th>Second tone</th><th>On white</th><th>On #111</th><th>Dark-mode disc</th><th>Needs</th></tr>'
            '</thead><tbody>%s</tbody></table></div>' % rows)


def grad_table(items):
    rows = ''
    for o in items:
        f = facts(o)
        rows += ('<tr><td class="n">%s</td><td><a href="#%s">%s</a></td>'
                 '<td class="n">%s<code>%s</code> to %s<code>%s</code></td><td class="n">%s</td>'
                 '<td class="n">%s</td><td>%s</td></tr>' % (
                     o['num'], o['key'], e(o['name']), swatch(o['a']), o['a'], swatch(o['b']), o['b'],
                     f['white'], f['dark'], e(f['need'])))
    return ('<div class="tw"><table class="opts"><thead><tr><th>No.</th><th>Gradient</th>'
            '<th>Top left to bottom right</th><th>On white</th><th>On #111</th><th>Use</th></tr></thead>'
            '<tbody>%s</tbody></table></div>' % rows)


def section(o):
    num = o['num']
    k = o['key']
    s, p = 'svg/' + k, 'png/' + k
    alt = e('%s %s' % (num, o['name']))
    f = facts(o)
    single = '%s/single.svg' % s if (o['head'] or o['band']) else '%s/mark.svg' % s
    if o['grad']:
        av_c, av_r, av_s = ('%s/avatar-%s-440.png' % (p, x) for x in ('circle', 'rounded', 'square'))
        banner = 'linear-gradient(135deg,%s,%s)' % (o['a'], o['b'])
        colors = '<code>%s</code> to <code>%s</code>, diagonal' % (o['a'], o['b'])
        site_note = (' <b>Gradient: a social candidate only.</b> The tab, favicon, thumbnail and header rows are '
                     'shown for comparison; on the site the flat color is used.')
    else:
        av_c, av_r, av_s = ('%s/avatar-%s.svg' % (s, x) for x in ('circle', 'rounded', 'square'))
        banner = o['disc']
        colors = 'disc <code>%s</code>, second tone: %s, dark-mode disc: %s' % (
            o['disc'], e(f['second']), e(f['dark_disc']))
        site_note = ''
    return f'''
<section class="mk" id="{k}" aria-labelledby="h-{k}">
  <div class="mk__head"><p class="mk__num">{num}</p><h3 id="h-{k}">{e(o['name'])}</h3></div>
  <p class="mk__note">{e(o['note'])}{site_note}</p>
  <p class="mk__facts">{colors}. Contrast on white {f['white']}, on near-black {f['dark']}. {e(f['need'])}</p>
  <div class="row"><h4>Avatars: 110 px circle and rounded square, on white and on near-black</h4>
    <div class="pair">
      <div class="g g--w"><img class="av av--c" src="{av_c}" width="110" height="110" alt="{alt}, circle avatar on white"><img class="av" src="{av_r}" width="110" height="110" alt="{alt}, rounded-square avatar on white"></div>
      <div class="g g--k"><img class="av av--c" src="{av_c}" width="110" height="110" alt="{alt}, circle avatar on near-black"><img class="av" src="{av_r}" width="110" height="110" alt="{alt}, rounded-square avatar on near-black"></div>
    </div></div>
  <div class="row"><h4>Monochrome at 160 px: black on white, white on black, the option in one color</h4>
    <div class="trio">
      <figure class="g g--w"><img class="m160" src="svg/mark-black.svg" width="160" height="160" alt="The mark in black on white"></figure>
      <figure class="g g--pk"><img class="m160" src="svg/mark-white.svg" width="160" height="160" alt="The mark in white on black"></figure>
      <figure class="g g--w"><img class="m160" src="{single}" width="160" height="160" alt="{alt}, one color only"></figure>
    </div></div>
  <div class="row"><h4>Color mark at 160 px, the cut-outs empty: on white, and the dark-mode version on near-black</h4>
    <div class="pair">
      <div class="g g--w"><img class="m160" src="{s}/mark.svg" width="160" height="160" alt="{alt}, mark on white"></div>
      <div class="g g--k"><img class="m160" src="{s}/mark-dark.svg" width="160" height="160" alt="{alt}, dark-mode mark on near-black"></div>
    </div></div>
  <div class="row"><h4>Instagram and LinkedIn</h4>
    <div class="prev">
      <div class="mock"><p class="mock__label">Instagram profile</p>
        <div class="ig"><img class="ig__av" src="{av_c}" width="110" height="110" alt="{alt} as an Instagram profile picture">
          <div><p class="ig__user">userandproduct</p>
            <ul class="ig__stats"><li><b>128</b> posts</li><li><b>4,210</b> followers</li><li><b>180</b> following</li></ul>
            <p class="ig__name">User and Product</p><p class="ig__bio">UX, product and business, from 15 years of practice.</p></div></div></div>
      <div class="mock"><p class="mock__label">LinkedIn company page and feed</p>
        <div class="li__banner" style="background:{banner}"></div>
        <div class="li__body"><img class="li__logo" src="{av_s}" width="100" height="100" alt="{alt} as a LinkedIn company logo">
          <div><p class="li__name">userandproduct</p><p class="li__meta">Online publishing · 2,340 followers</p></div></div>
        <div class="li__post"><img src="{av_s}" width="48" height="48" alt="{alt} at 48 px in the LinkedIn feed">
          <div><b>userandproduct</b><small>2,340 followers · 1h</small><p>Why most roadmaps fail before the first sprint, and the one question that fixes it.</p></div></div>
      </div>
    </div></div>
  <div class="row"><h4>Browser tab with the 16 px favicon, light and dark</h4>
    <div class="mock">
      <div class="tabs tabs--l"><div class="tab tab--on"><img src="{p}/tab-16-light.png" width="16" height="16" alt="{alt}, 16 px favicon in a light tab"><span>userandproduct</span><span class="x" aria-hidden="true">&times;</span></div><div class="tab tab--off"><span>New tab</span></div></div><div class="tabs__url"></div>
      <div class="tabs tabs--d"><div class="tab tab--on"><img src="{p}/tab-16-dark.png" width="16" height="16" alt="{alt}, 16 px favicon in a dark tab"><span>userandproduct</span><span class="x" aria-hidden="true">&times;</span></div><div class="tab tab--off"><span>New tab</span></div></div><div class="tabs__url"></div>
    </div></div>
  <div class="row"><h4>Favicon: 32 px and 16 px, rendered at size; the 32 px enlarged three times</h4>
    <div class="pair">
      <div class="g g--w"><div class="fav"><img src="{p}/fav-32-light.png" width="32" height="32" alt="{alt}, 32 px favicon on white"><img class="z" src="{p}/fav-32-light.png" alt=""><img src="{p}/fav-16-light.png" width="16" height="16" alt="{alt}, 16 px favicon on white"></div></div>
      <div class="g g--k"><div class="fav"><img src="{p}/fav-32-dark.png" width="32" height="32" alt="{alt}, 32 px favicon on near-black"><img class="z" src="{p}/fav-32-dark.png" alt=""><img src="{p}/fav-16-dark.png" width="16" height="16" alt="{alt}, 16 px favicon on near-black"></div></div>
    </div></div>
  <div class="row"><h4>Thumbnail: the lockup 120 px wide in the corner of a 600 x 338 tile</h4>
    <img class="thumb" src="{p}/thumb.png" width="600" height="338" alt="{alt}, lockup on a thumbnail tile" loading="lazy"></div>
  <div class="row"><h4>Header lockup at 236 px, Inter Display Bold wordmark</h4>
    <div class="pair">
      <div class="g g--w"><img class="lk" src="{s}/lockup.svg" width="236" alt="{alt}, header lockup on white"></div>
      <div class="g g--k"><img class="lk" src="{s}/lockup-dark.svg" width="236" alt="{alt}, header lockup on near-black"></div>
    </div></div>
  <div class="row"><h4>Stacked lockup at 120 px</h4>
    <div class="pair">
      <div class="g g--w"><img class="st" src="{s}/stacked.svg" width="120" alt="{alt}, stacked lockup on white"></div>
      <div class="g g--k"><img class="st" src="{s}/stacked-dark.svg" width="120" alt="{alt}, stacked lockup on near-black"></div>
    </div></div>
</section>'''


EXPORTS = [
    ('export/favicon.svg', 'the signal blue disc with empty cut-outs; switches to #8EA2FF in dark themes.'),
    ('export/favicon.ico, favicon-16.png, favicon-32.png, favicon-48.png',
     'the disc with the figure filled white, so it holds in light and dark tabs.'),
    ('export/apple-touch-icon-180.png', 'opaque full square, signal blue with the white figure; iOS rounds the corners.'),
    ('export/social-square-1080.png, social-square-400.png', 'the square avatar for Instagram, LinkedIn and X uploads.'),
    ('export/social-circle-1080.png, social-circle-400.png', 'the disc edge to edge, transparent corners.'),
    ('export/gradient/', 'each gradient as a 1080 square and circle, dithered against banding; social only.'),
    ('export/head-snippet.html', 'the three tags for the theme head.'),
    ('svg/mark.svg', 'the clean master: the owner\'s geometry exactly, one compound path, the cut-outs true holes.'),
    ('svg/mark-solid.svg', 'the same with the cut-outs filled white, for photos.'),
    ('svg/mark-black.svg, mark-white.svg, mark-currentcolor.svg', 'monochrome and inline masters.'),
    ('svg/lockup-black.svg, lockup-white.svg, stacked-black.svg, stacked-white.svg', 'monochrome lockups.'),
    ('svg/&lt;option&gt;/', 'per option: mark, mark-dark, single (when the cut-outs are filled), avatar-circle, '
     'avatar-rounded, avatar-square, lockup, lockup-dark, stacked, stacked-dark.'),
    ('png/&lt;option&gt;/', 'per option: favicons at 16 and 32 px on white and near-black, transparent tab icons, '
     'the thumbnail tile; for gradients also the avatars as PNG.'),
]


def avatar_src(o):
    if o['grad']:
        return 'png/%s/avatar-circle-440.png' % o['key']
    return 'svg/%s/avatar-circle.svg' % o['key']


def strip(items):
    """A row of circle avatars, for comparing a family at a glance."""
    cells = ''.join('<figure><a href="#%s"><img class="av av--c" src="%s" width="110" height="110" alt="%s %s"></a>'
                    '<figcaption>%s %s</figcaption></figure>' % (
                        o['key'], avatar_src(o), o['num'], e(o['name']), o['num'], e(o['name'])) for o in items)
    return '<div class="g g--w strip">%s</div>' % cells


LOCKUP_FIX = """
  <div class="grp" id="lockup-fix"><h2>Lockup fix: the mark at the first pack's size</h2>
    <p>The first version set the disc 1.12 cap heights tall with its bottom on the baseline, and it looked small
    beside the name. The side lockups now use the first pack's geometry: the disc is 1.4 cap heights across (1.09 of
    the wordmark's full height, ascender top to descender bottom), and its center sits 31 units above the baseline,
    midway between the cap and x-height bands, so the two are centered on each other. The gap is 0.40 of the disc.
    Every side lockup on this board is rebuilt this way. The stacked lockup already matched the first pack.</p>
    <div class="row"><h4>Signal blue at 236 px: before, after, and the first pack's lockup for comparison</h4>
      <div class="trio">
        <figure class="g g--w"><img class="lk" src="svg/signal/lockup-before.svg" width="236" alt="Before: the smaller disc"><figcaption>Before</figcaption></figure>
        <figure class="g g--w"><img class="lk" src="svg/signal/lockup.svg" width="236" alt="After: the disc at the first pack's size"><figcaption>After</figcaption></figure>
        <figure class="g g--w"><img class="lk" src="../final-logo/svg/lockup-light.svg" width="236" alt="The first pack's lockup"><figcaption>First pack</figcaption></figure>
      </div>
      <div class="trio" style="margin-top:12px">
        <figure class="g g--k"><img class="lk" src="svg/signal/lockup-before-dark.svg" width="236" alt="Before, on near-black"><figcaption>Before</figcaption></figure>
        <figure class="g g--k"><img class="lk" src="svg/signal/lockup-dark.svg" width="236" alt="After, on near-black"><figcaption>After</figcaption></figure>
        <figure class="g g--k"><img class="lk" src="../final-logo/svg/lockup-dark.svg" width="236" alt="The first pack's lockup on near-black"><figcaption>First pack</figcaption></figure>
      </div></div>
    <div class="row"><h4>At the thumbnail size, 120 px: before and after</h4>
      <div class="pair">
        <figure class="g g--w"><img src="svg/signal/lockup-before.svg" width="120" alt="Before, 120 px"><figcaption>Before</figcaption></figure>
        <figure class="g g--w"><img src="svg/signal/lockup.svg" width="120" alt="After, 120 px"><figcaption>After</figcaption></figure>
      </div></div>
  </div>"""


def lockup_fix():
    return LOCKUP_FIX


def board():
    toc = ''.join('<li><a href="#%s"><img src="svg/%s/mark.svg" alt="" width="20" height="20">%s</a></li>' % (
        o['key'], o['key'], e(o['name'])) for o in G.OPTIONS + G.GRADIENTS)
    def grp(kind, group):
        src = G.OPTIONS if kind == 'C' else G.GRADIENTS
        return [o for o in src if o['group'] == group]

    first_c, first_g = grp('C', 'first'), grp('G', 'first')
    blue_c, blue_g = grp('C', 'blues'), grp('G', 'blues')
    vib_c, vib_g = grp('C', 'vibrant'), grp('G', 'vibrant')
    ref = [o for o in G.GRADIENTS if o['key'] == 'g-signal-cobalt']

    def secs(items):
        return ''.join(section(o) for o in items)

    files = ''.join('<li><code>%s</code>: %s</li>' % (a, e(b)) for a, b in EXPORTS)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Logo Three Colors</title>
<meta name="robots" content="noindex">
<link rel="icon" href="export/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../mockup.css">
<style>{CSS}</style>
</head>
<body>
<main class="l3">
  <div class="bar"><p>Mockups · Logo 3</p><button class="toggle" type="button" data-theme-toggle>Theme</button></div>
  <h1>Logo 3: the owner's mark, in color</h1>
  <p class="lede">The owner's own drawing: a disc with a person cut out of it, a rounded diamond for the head over a wide
  curved band for the shoulders. The same band also reads as a smile or a bowl. The shapes are exactly as drawn; only the color changes below.</p>
  <div class="hero">
    <div class="g g--w"><img src="svg/mark-black.svg" width="220" height="220" alt="The mark in black on white"></div>
    <div class="g g--pk"><img src="svg/mark-white.svg" width="220" height="220" alt="The mark in white on black"></div>
  </div>
  <ul class="toc" aria-label="Options">{toc}</ul>

  {lockup_fix()}

  <div class="grp" id="colors"><h2>Color options</h2>
    <p>The first twelve. Each disc is checked against white and against near-black (#111111) for the 3:1 a graphic
    needs. Where a disc fails on dark, its dark-mode version is a lighter tone of the same color. The cut-outs are
    true holes, so on any ground they show the ground, except where they are filled (C11, C12, C22).
    Avatars are opaque, like an upload, so the figure in them is white (ink in C11 and C22).</p>
    {table(first_c)}
  </div>
  {secs(first_c)}

  <div class="grp" id="gradients"><h2>Gradient options</h2>
    <p>Four smooth two-stop gradients, diagonal from the top left. The house rule from the first logo pack still
    stands: <b>gradients are for social backgrounds only, never on the site.</b> These and the gradients further
    down are marked as social candidates (avatars, banners, posts) unless the owner says otherwise.</p>
    {grad_table(first_g)}
    <div class="note" role="note"><p>Banding: the board shows the gradient avatars as PNGs rendered at four times
    the size, stepped down and dithered by under one gray level; the exports in <code>export/gradient/</code> are made the same way.</p></div>
  </div>
  {secs(first_g)}

  <div class="grp" id="blues"><h2>Blues (flat)</h2>
    <p>Five more blues across the family, C13 to C17, shown beside the signal blue (C01). Navy (C02) and cobalt
    (C03) are above. Each has its dark-mode lift.</p>
    {strip(G.OPTIONS[:1] + blue_c)}
    {table(blue_c)}
  </div>
  {secs(blue_c)}

  <div class="grp" id="blue-gradients"><h2>Blue gradients</h2>
    <p>Five two-stop diagonals inside the blue family, G05 to G09, with G01 (signal blue to cobalt, the one the
    owner likes) first as the reference. Social candidates only.</p>
    {strip(ref + blue_g)}
    {grad_table(ref + blue_g)}
  </div>
  {secs(blue_g)}

  <div class="grp" id="vibrant"><h2>Vibrant (flat)</h2>
    <p>Five saturated, high-energy colors, C18 to C22. Four carry a white figure at 3:1 or better, so the disc
    still reads as a confident badge; the lime is too light for that and takes an ink figure.</p>
    {strip(vib_c)}
    {table(vib_c)}
  </div>
  {secs(vib_c)}

  <div class="grp" id="vibrant-gradients"><h2>Vibrant gradients</h2>
    <p>Five two-stop diagonals across hues, G10 to G14. Social candidates only, under the house rule, unless the owner lifts it.</p>
    {strip(vib_g)}
    {grad_table(vib_g)}
  </div>
  {secs(vib_g)}

  <div class="grp" id="exports"><h2>What gets exported</h2>
    <p>The export folder holds the signal blue option (C01) ready to try for real. Every other option has its
    masters in <code>svg/</code> and its renders in <code>png/</code>; any of them can be exported the same way
    once one is chosen.</p>
    <ul class="files">{files}</ul>
  </div>
  <p class="foot">Built by <code>build.py</code> in this folder from <code>source/Logo-owner.svg</code> (the owner's
  <code>Logo.svg</code> is never touched). Checks in <code>check.py</code>. The Instagram, LinkedIn and tab previews are plain HTML
  mocks, the same for every option. Rebuild notes in README.md.</p>
</main>
<script src="../mockup.js"></script>
</body>
</html>
'''
