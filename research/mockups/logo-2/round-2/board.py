"""Writes index.html, the round 2 board. Called by build.py."""
from html import escape as e

COLOUR_NAME = {'blue': 'Signal blue with a light-blue fold', 'green': 'Alternative: deep green',
               'vermilion': 'Alternative: vermilion'}

CSS = """
.r2{max-width:1180px;margin:0 auto;padding:32px var(--gutter) 96px}
.r2 a{color:var(--signal)}
.back{font-size:var(--fs-meta);margin:0 0 28px}
.r2 h1{font-family:var(--font-display);font-weight:700;font-size:clamp(32px,5vw,52px);line-height:1.05;letter-spacing:-.01em;margin:0 0 16px}
.brief{max-width:68ch;font-size:var(--fs-body);line-height:var(--lh-body)}
.brief p{margin:0 0 12px}
.brief ul{margin:0 0 12px;padding-left:20px}
.toc{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:8px 24px;list-style:none;padding:0;margin:28px 0 8px;font-size:var(--fs-ui)}
.toc a{text-decoration:none;color:var(--ink)}
.toc b{font-family:var(--font-display);color:var(--signal);margin-right:6px}
.mk{border-top:2px solid var(--rule-strong);margin-top:56px;padding-top:20px}
.mk__head{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 16px;margin-bottom:18px}
.mk__num{font-family:var(--font-display);font-weight:700;font-size:15px;color:var(--signal);margin:0}
.mk h2{font-family:var(--font-display);font-weight:700;font-size:30px;line-height:1.1;margin:0}
.mk__tags{margin:0;font-size:var(--fs-meta);color:var(--ink);opacity:.75}
.row{margin:0 0 22px}
.row h3{font-size:12px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;margin:0 0 8px;opacity:.7}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.g{border-radius:var(--radius);padding:20px;display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:20px;min-height:100px}
.g--w{background:#FFFFFF;border:1px solid #E3E3E6}
.g--k{background:#0B0B0C;border:1px solid #26262B}
.g img{display:block}
.av{width:110px;height:110px}
.m160{width:160px;height:160px}
.lk{width:236px;height:auto}
.fav{display:flex;align-items:center;gap:16px}
.fav .z{width:96px;height:96px;image-rendering:pixelated;image-rendering:crisp-edges}
.fav small{font-size:11px;color:#8A8A92}
.thumb{display:block;width:100%;max-width:600px;height:auto;border-radius:4px}
.words{display:grid;grid-template-columns:minmax(120px,170px) 1fr;gap:8px 20px;margin:8px 0 0;font-size:var(--fs-ui);line-height:1.5;max-width:900px}
.words dt{font-weight:600}
.words dd{margin:0}
.words ul{margin:0;padding-left:18px}
.foot{margin-top:64px;font-size:var(--fs-meta);opacity:.75}
@media (max-width:640px){.pair{grid-template-columns:1fr}.words{grid-template-columns:1fr}.words dd{margin-bottom:8px}}
"""


def section(b):
    m, n, s = b['meta'], b['n'], 'svg/' + b['stem']
    p = 'png/' + b['stem']
    num = 'R2-%s' % n
    alt = e('%s %s' % (num, m['name']))
    tags = ' · '.join([m['letters'], m['holder'], COLOUR_NAME[m['colour']]])
    closest = ''.join('<li>%s</li>' % e(c) for c in m['closest'])
    lockup_note = ('the name with the custom u, no separate mark' if m.get('wordmark')
                   else 'with the current Inter Display Bold wordmark')
    return f'''
<section class="mk" id="r2-{n}" aria-labelledby="h-{n}">
  <div class="mk__head"><p class="mk__num">{num}</p><h2 id="h-{n}">{e(m['name'])}</h2><p class="mk__tags">{e(tags)}</p></div>
  <div class="row"><h3>Avatar test: 110 px circle and rounded square</h3>
    <div class="pair">
      <div class="g g--w"><img class="av" src="{s}-avatar-circle.svg" alt="{alt}, circle avatar on white"><img class="av" src="{s}-avatar-square.svg" alt="{alt}, rounded-square avatar on white"></div>
      <div class="g g--k"><img class="av" src="{s}-avatar-circle-dark.svg" alt="{alt}, circle avatar on near-black"><img class="av" src="{s}-avatar-square-dark.svg" alt="{alt}, rounded-square avatar on near-black"></div>
    </div></div>
  <div class="row"><h3>Mark at 160 px</h3>
    <div class="pair">
      <div class="g g--w"><img class="m160" src="{s}-mark.svg" alt="{alt}, mark on white"></div>
      <div class="g g--k"><img class="m160" src="{s}-mark-dark.svg" alt="{alt}, dark mark on near-black"></div>
    </div></div>
  <div class="row"><h3>Favicon: rendered 32 px and 16 px PNGs, and the 32 px enlarged three times</h3>
    <div class="pair">
      <div class="g g--w"><div class="fav"><img src="{p}-32-light.png" width="32" height="32" alt="{alt}, 32 px favicon on white"><img src="{p}-16-light.png" width="16" height="16" alt="{alt}, 16 px favicon on white"><img class="z" src="{p}-32-light.png" alt=""><small>32 px x3</small></div></div>
      <div class="g g--k"><div class="fav"><img src="{p}-32-dark.png" width="32" height="32" alt="{alt}, 32 px favicon on near-black"><img src="{p}-16-dark.png" width="16" height="16" alt="{alt}, 16 px favicon on near-black"><img class="z" src="{p}-32-dark.png" alt=""><small>32 px x3</small></div></div>
    </div></div>
  <div class="row"><h3>Thumb: lockup 120 px wide in the corner of a 600 x 338 tile ({b['thumb_ink']}, 92 percent)</h3>
    <img class="thumb" src="{p}-thumb.png" width="600" height="338" alt="{alt}, lockup on a {b['tile']} thumbnail tile"></div>
  <div class="row"><h3>Header lockup at 236 px, {lockup_note}</h3>
    <div class="pair">
      <div class="g g--w"><img class="lk" src="{s}-lockup.svg" alt="{alt}, header lockup on white"></div>
      <div class="g g--k"><img class="lk" src="{s}-lockup-dark.svg" alt="{alt}, header lockup on near-black"></div>
    </div></div>
  <dl class="words">
    <dt>The idea</dt><dd>{e(m['idea'])}</dd>
    <dt>Why "oh nice"</dt><dd>{e(m['nice'])}</dd>
    <dt>Authority check</dt><dd>{e(m['authority'])}</dd>
    <dt>Construction</dt><dd>{e(m['construction'])}</dd>
    <dt>Closest existing logos in this visual family</dt><dd><ul>{closest}</ul></dd>
  </dl>
</section>'''


def board(built):
    toc = ''.join('<li><a href="#r2-%s"><b>R2-%s</b>%s</a></li>' % (b['n'], b['n'], e(b['meta']['name'])) for b in built)
    body = ''.join(section(b) for b in built)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Logo round 2: letterform marks</title>
<meta name="robots" content="noindex">
<link rel="stylesheet" href="../../mockup.css">
<style>{CSS}</style>
</head>
<body>
<main class="r2">
  <p class="back"><a href="../hub.html">&larr; Logo exploration 2, hub</a></p>
  <h1>Round 2: letterform marks</h1>
  <div class="brief">
    <p>Ten marks built from the letters U, D and P (the name is user and product, so U with D and U with P are both in
    scope, and the ampersand may join them). They replace the four-tile Signal mark, which reads as bland and without
    presence.</p>
    <p>In order of priority: authority and trust first (a serious publication a professional would cite), then character,
    then the qualities: mass, one idea per mark, a two-tone fold where forms overlap, an app-icon feel (seven are
    contained in or shaped as a circle or rounded square, three stand free for comparison), and recognisable at 32 px.
    No thin strokes (nothing under 8 at 512), no gradients, no cartoon. Signal blue with a lighter fold tone by default;
    R2-06 and R2-09 are in an alternative colour.</p>
    <p>Each mark is shown first in the test it must pass, a 110 px circle and rounded-square avatar on white and on
    near-black, then at 160 px, as a rendered 32 px favicon, in the corner of a thumbnail, and in the 236 px header
    lockup with the current Inter Display Bold wordmark for a fair comparison.</p>
  </div>
  <ol class="toc">{toc}</ol>
  {body}
  <p class="foot">Built by <code>build.py</code> in this folder. Masters in <code>svg/</code> (512 canvas, paths only),
  rendered favicons and thumbs in <code>png/</code>. Rebuild notes in README.md.</p>
</main>
</body>
</html>
'''
