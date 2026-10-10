"""Writes index.html, the round 4 board. Called by build.py."""
from html import escape as e

COLOR_NAME = {'blue': 'Signal blue with a lighter fold', 'green': 'Alternative: deep green',
              'vermilion': 'Alternative: vermilion', 'oxblood': 'Alternative: oxblood',
              'plum': 'Alternative: plum'}

from info import GROUPS

CSS = """
.r4{max-width:1180px;margin:0 auto;padding:24px var(--gutter) 96px}
.r4 a{color:var(--signal)}
.bar{display:flex;justify-content:space-between;align-items:center;gap:16px;margin:0 0 24px}
.bar p{margin:0;font-size:var(--fs-meta)}
.toggle{border:1px solid var(--rule);background:var(--panel);color:var(--ink);border-radius:999px;padding:6px 14px;cursor:pointer;font:500 14px/1 var(--font-ui)}
.r4 h1{font-family:var(--font-display);font-weight:700;font-size:clamp(32px,5vw,52px);line-height:1.05;letter-spacing:-.01em;margin:0 0 20px}
.top{display:grid;gap:24px;grid-template-columns:minmax(0,1fr);margin-bottom:8px}
@media (min-width:900px){.top{grid-template-columns:minmax(0,1.3fr) minmax(0,1fr)}}
.top h2{font-size:15px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;margin:0 0 10px;color:var(--ink-2)}
.top ol,.top ul{margin:0;padding-left:20px;font-size:16px;line-height:1.5;color:var(--ink-2)}
.top li{margin:0 0 6px}
.top li b{color:var(--ink)}
.toc{margin:28px 0 0;display:grid;gap:12px;grid-template-columns:1fr}
@media (min-width:800px){.toc{grid-template-columns:repeat(3,1fr)}}
.toc h3{font-size:14px;margin:0 0 6px}
.toc ol{list-style:none;margin:0;padding:0;font-size:var(--fs-ui)}
.toc a{text-decoration:none;color:var(--ink)}
.toc b{font-family:var(--font-display);color:var(--signal);margin-right:6px}
.grp{margin-top:72px;padding:20px 0 0;border-top:4px solid var(--ink)}
.grp h2{font-family:var(--font-display);font-size:clamp(26px,4vw,36px);margin:0 0 6px}
.grp p{margin:0;color:var(--ink-2);max-width:70ch}
.mk{border-top:2px solid var(--rule-strong);margin-top:48px;padding-top:20px}
.mk__head{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 16px;margin-bottom:18px}
.mk__num{font-family:var(--font-display);font-weight:700;font-size:15px;color:var(--signal);margin:0}
.mk h3.mk__name{font-family:var(--font-display);font-weight:700;font-size:30px;line-height:1.1;margin:0}
.mk__tags{margin:0;font-size:var(--fs-meta);color:var(--ink-2)}
.row{margin:0 0 22px}
.row h4{font-size:12px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;margin:0 0 8px;color:var(--ink-2)}
.pair{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.trio{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.g{min-width:0;border-radius:var(--radius);padding:18px;display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:18px;min-height:100px}
.g--w{background:#FFFFFF;border:1px solid #E3E3E6;color:#55555C}
.g--k{background:#0B0B0C;border:1px solid #26262B;color:#9A9AA2}
.g--pk{background:#000000;border:1px solid #26262B}
.g img{display:block}
.g figcaption{width:100%;text-align:center;font-size:11px}
.g figure{margin:0;display:flex;flex-direction:column;align-items:center;gap:8px}
.av{width:110px;height:110px}
.m160{width:160px;height:160px;max-width:100%;height:auto}
.lk{width:236px;height:auto;max-width:100%}
.fav{display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:12px}
.fav .z{width:96px;height:96px;image-rendering:pixelated;image-rendering:crisp-edges}
.fav small{font-size:11px}
.prev{display:grid;gap:12px;grid-template-columns:minmax(0,1fr)}
@media (min-width:900px){.prev{grid-template-columns:minmax(0,1.1fr) minmax(0,1fr) minmax(0,1fr)}}
.mock{border:1px solid var(--rule);border-radius:var(--radius);background:var(--panel);color:var(--ink);overflow:hidden}
.mock__label{font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-3);padding:8px 12px 0;margin:0}
.ig{display:flex;gap:18px;align-items:center;padding:14px 16px 16px}
.ig__av{width:110px;height:110px;border-radius:50%;flex:none}
.ig__user{font:600 17px/1.2 var(--font-ui);margin:0 0 8px}
.ig__stats{list-style:none;margin:0 0 8px;padding:0;display:flex;flex-wrap:wrap;gap:4px 14px;font-size:13px}
.ig__stats li{white-space:nowrap}
.ig__stats b{font-weight:700}
.ig__name{font:600 13px/1.3 var(--font-ui);margin:0}
.ig__bio{font-size:13px;line-height:1.35;margin:2px 0 0;color:var(--ink-2)}
.li__banner{height:64px;margin-top:8px}
.li__body{padding:0 16px 16px}
.li__logo{width:100px;height:100px;border-radius:4px;border:3px solid var(--panel);margin-top:-44px;display:block;background:#fff}
.li__name{font:700 18px/1.2 var(--font-ui);margin:8px 0 2px}
.li__meta{font-size:13px;color:var(--ink-2);margin:0}
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
.words{display:grid;grid-template-columns:minmax(120px,190px) 1fr;gap:8px 20px;margin:8px 0 0;font-size:var(--fs-ui);line-height:1.5;max-width:900px}
.words dt{font-weight:600}
.words dd{margin:0}
.words dd.means{font-size:17px;line-height:1.5;color:var(--ink)}
.words ul{margin:0;padding-left:18px}
.note{border:1px solid var(--signal);background:var(--signal-wash);border-radius:var(--radius);padding:12px 16px;margin:0 0 24px;font-size:15px;line-height:1.5;color:var(--ink)}
.note p{margin:0}
.foot{margin-top:64px;font-size:var(--fs-meta);color:var(--ink-3)}
@media (max-width:640px){.pair,.trio{grid-template-columns:minmax(0,1fr)}.fav .z{width:64px;height:64px}.words{grid-template-columns:1fr}.words dd{margin-bottom:8px}.ig{flex-wrap:wrap}}
"""


def section(b):
    m, n, s = b['meta'], b['n'], 'svg/' + b['stem']
    p = 'png/' + b['stem']
    num = 'R4-%s' % n
    alt = e('%s %s' % (num, m['name']))
    tags = ' · '.join([m['type'], b['holder'], COLOR_NAME[m['colour']]])
    closest = ''.join('<li>%s</li>' % e(c) for c in m['closest'])
    brand = b['brand']
    return f'''
<section class="mk" id="r4-{n}" aria-labelledby="h-{n}">
  <div class="mk__head"><p class="mk__num">{num}</p><h3 class="mk__name" id="h-{n}">{e(m['name'])}</h3><p class="mk__tags">{e(tags)}</p></div>
  <div class="row"><h4>Avatars: 110 px circle and rounded square</h4>
    <div class="pair">
      <div class="g g--w"><img class="av" src="{s}-avatar-circle.svg" alt="{alt}, circle avatar on white"><img class="av" src="{s}-avatar-square.svg" alt="{alt}, rounded-square avatar on white"></div>
      <div class="g g--k"><img class="av" src="{s}-avatar-circle-dark.svg" alt="{alt}, circle avatar on near-black"><img class="av" src="{s}-avatar-square-dark.svg" alt="{alt}, rounded-square avatar on near-black"></div>
    </div></div>
  <div class="row"><h4>Monochrome at 160 px: white on black, black on white, one color with no fold</h4>
    <div class="trio">
      <figure class="g g--pk"><img class="m160" src="{s}-mono-white.svg" width="160" height="160" alt="{alt}, pure white on black"></figure>
      <figure class="g g--w"><img class="m160" src="{s}-mono-black.svg" width="160" height="160" alt="{alt}, pure black on white"></figure>
      <figure class="g g--w"><img class="m160" src="{s}-single.svg" width="160" height="160" alt="{alt}, one color only"></figure>
    </div></div>
  <div class="row"><h4>Color mark at 160 px</h4>
    <div class="pair">
      <div class="g g--w"><img class="m160" src="{s}-mark.svg" width="160" height="160" alt="{alt}, mark on white"></div>
      <div class="g g--k"><img class="m160" src="{s}-mark-dark.svg" width="160" height="160" alt="{alt}, dark mark on near-black"></div>
    </div></div>
  <div class="row"><h4>Favicons: rendered 32 px and 16 px PNGs in color, 32 px in monochrome; the 32 px enlarged three times</h4>
    <div class="pair">
      <div class="g g--w"><div class="fav"><img src="{p}-32-light.png" width="32" height="32" alt="{alt}, 32 px favicon on white"><img class="z" src="{p}-32-light.png" alt=""><img src="{p}-16-light.png" width="16" height="16" alt="{alt}, 16 px favicon on white"><img src="{p}-32-mono-light.png" width="32" height="32" alt="{alt}, 32 px black favicon on white"><img class="z" src="{p}-32-mono-light.png" alt=""></div></div>
      <div class="g g--k"><div class="fav"><img src="{p}-32-dark.png" width="32" height="32" alt="{alt}, 32 px favicon on near-black"><img class="z" src="{p}-32-dark.png" alt=""><img src="{p}-16-dark.png" width="16" height="16" alt="{alt}, 16 px favicon on near-black"><img src="{p}-32-mono-dark.png" width="32" height="32" alt="{alt}, 32 px white favicon on black"><img class="z" src="{p}-32-mono-dark.png" alt=""></div></div>
    </div></div>
  <div class="row"><h4>Previews: Instagram profile, LinkedIn page, browser tab at 16 px</h4>
    <div class="prev">
      <div class="mock"><p class="mock__label">Instagram profile</p>
        <div class="ig"><img class="ig__av" src="{s}-avatar-circle.svg" width="110" height="110" alt="{alt} as an Instagram profile picture">
          <div><p class="ig__user">userandproduct</p>
            <ul class="ig__stats"><li><b>128</b> posts</li><li><b>4,210</b> followers</li><li><b>180</b> following</li></ul>
            <p class="ig__name">User and Product</p><p class="ig__bio">UX, product and business, from 15 years of practice.</p></div></div></div>
      <div class="mock"><p class="mock__label">LinkedIn company page</p>
        <div class="li__banner" style="background:{brand}"></div>
        <div class="li__body"><img class="li__logo" src="{s}-avatar-linkedin.svg" width="100" height="100" alt="{alt} as a LinkedIn company logo">
          <p class="li__name">userandproduct</p><p class="li__meta">Online publishing · 2,340 followers</p></div></div>
      <div class="mock"><p class="mock__label">Browser tab, light and dark</p>
        <div class="tabs tabs--l"><div class="tab tab--on"><img src="{p}-16-tab-light.png" width="16" height="16" alt="{alt}, 16 px favicon in a light tab"><span>userandproduct</span><span class="x" aria-hidden="true">&times;</span></div><div class="tab tab--off"><span>New tab</span></div></div><div class="tabs__url"></div>
        <div class="tabs tabs--d"><div class="tab tab--on"><img src="{p}-16-tab-dark.png" width="16" height="16" alt="{alt}, 16 px favicon in a dark tab"><span>userandproduct</span><span class="x" aria-hidden="true">&times;</span></div><div class="tab tab--off"><span>New tab</span></div></div><div class="tabs__url"></div>
      </div>
    </div></div>
  <div class="row"><h4>Thumbnail: lockup 120 px wide in the corner of a 600 x 338 tile ({b['thumb_ink']}, 92 percent)</h4>
    <img class="thumb" src="{p}-thumb.png" width="600" height="338" alt="{alt}, lockup on a {b['tile']} thumbnail tile" loading="lazy"></div>
  <div class="row"><h4>Header lockup at 236 px with the Inter Display Bold wordmark</h4>
    <div class="pair">
      <div class="g g--w"><img class="lk" src="{s}-lockup.svg" alt="{alt}, header lockup on white"></div>
      <div class="g g--k"><img class="lk" src="{s}-lockup-dark.svg" alt="{alt}, header lockup on near-black"></div>
    </div></div>
  <dl class="words">
    <dt>The idea</dt><dd>{e(m['idea'])}</dd>
    <dt>Why "oh nice"</dt><dd>{e(m['nice'])}</dd>
    <dt>What it means</dt><dd class="means">{e(m['means'])}</dd>
    <dt>Authority check</dt><dd>{e(m['authority'])}</dd>
    <dt>Construction</dt><dd>{e(m['construction'])}</dd>
    <dt>Nearest existing logos</dt><dd><ul>{closest}</ul></dd>
  </dl>
</section>'''


ORDER = ['cup', 'speech', 'square', 'shelf', 'fig', 'fresh']


def board(built):
    tocs = ''
    body = ''
    for g in ORDER:
        items = [b for b in built if b['meta']['group'] == g]
        tocs += '<div><h3>%s</h3><ol>%s</ol></div>' % (e(GROUPS[g][0]), ''.join(
            '<li><a href="#r4-%s"><b>R4-%s</b>%s</a></li>' % (b['n'], b['n'], e(b['meta']['name'])) for b in items))
        body += '<div class="grp" id="group-%s"><h2>%s</h2><p>%s</p></div>' % (g, e(GROUPS[g][0]), e(GROUPS[g][1]))
        body += ''.join(section(b) for b in items)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Logo Round Four</title>
<meta name="robots" content="noindex">
<link rel="stylesheet" href="../../mockup.css">
<style>{CSS}</style>
</head>
<body>
<main class="r4">
  <div class="bar"><p><a href="../hub.html">&larr; Logo exploration 2, hub</a></p><button class="toggle" type="button" data-theme-toggle>Theme</button></div>
  <h1>Round 4: refining the shortlist, and fresh marks</h1>
  <div class="note" role="note"><p><b>What the round found.</b> Cup and ball: 45 degrees holds the three readings best
  (R4-04: a U on its side, a head with a raised arm, the straight cut edge as the stem of a D); lifting the ball (R4-08)
  makes the person read first at the cost of the D. Speech mark: the long tails fix the cricket ball. The heavier
  tail (R4-12) survives smallest and still reads as a quote mark at 16 px; the longer, finer tail (R4-11) is as clear at
  32 px. The wedge (R4-14) reads at any size, but as a chat bubble.</p></div>
  <div class="top">
    <div><h2>The brief</h2>
      <ol>
        <li><b>Refine the four the owner shortlisted:</b> Cup and ball, Speech mark, Square coin, Shelf.</li>
        <li><b>Cup and ball tilted to the left</b> at 30, 45 and 60 degrees, free and in a disc, and with the ball lifted.</li>
        <li><b>Speech mark: make the tail the drawing,</b> tested at 32 px and 16 px first.</li>
        <li><b>Square coin and Shelf:</b> small variations so the exact proportion can be picked.</li>
        <li><b>New ground:</b> figurative candidates from round 3 and eight fresh marks, at the standard of one clean idea cut from a solid form.</li>
      </ol>
      <p style="margin:12px 0 0;font-size:15px;color:var(--ink-2)">Numbering is fixed once the owner has seen this board: new marks go at the end, dropped marks stay and are marked as dropped.</p></div>
    <div><h2>Still out</h2>
      <ul>
        <li>Rockets, folders, switches, bookmarks, cursors, keys, pens.</li>
        <li>A profile head in a disc, and anything from the old exploration (plumb lines, keystones, lecterns, true north were tried there).</li>
        <li>Letters as the main idea: only the Square coin family is letter-based.</li>
      </ul></div>
  </div>
  <nav class="toc" aria-label="Marks">{tocs}</nav>
  {body}
  <p class="foot">Built by <code>build.py</code> in this folder. Masters in <code>svg/</code> (512 canvas, paths only),
  rendered favicons and thumbs in <code>png/</code>. The Instagram, LinkedIn and tab previews are plain HTML mocks, the same
  for every mark. Rebuild notes in README.md.</p>
</main>
<script src="../../mockup.js"></script>
</body>
</html>
'''
