"""Write the round-six review board (index.html) with every SVG inlined.

Per concept: lockup on white (or cream) and near-black, a 1280px site header strip on white and on
near-black, the mark, the favicon art, favicon PNGs, one color, the 400px avatar (the disc fills it) and a
mock profile tile, the closest existing logos (names only), then the notes.
"""
import html
import os

from notes6 import NOTES

CSS = """
:root{--bg:#f7f6f3;--fg:#141414;--muted:#5b5a56;--line:#dddad3;--card:#ffffff;--chip:#ecebe6}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#0f0f0f;--fg:#efede8;--muted:#a19e97;--line:#2c2b29;--card:#1a1a19;--chip:#262624}}
:root[data-theme=dark]{--bg:#0f0f0f;--fg:#efede8;--muted:#a19e97;--line:#2c2b29;--card:#1a1a19;--chip:#262624}
*{box-sizing:border-box}
html{scroll-padding-top:64px}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;overflow-x:hidden}
.wrap{max-width:1400px;margin:0 auto;padding:0 24px}
header.top{padding:40px 0 16px}
header.top h1{font-size:clamp(28px,4vw,44px);line-height:1.1;margin:0 0 10px;letter-spacing:-.02em}
header.top p{margin:0 0 10px;max-width:900px;color:var(--muted);font-size:18px}
nav.jump{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--line)}
nav.jump .wrap{display:flex;flex-wrap:wrap;gap:6px;padding-top:10px;padding-bottom:10px;align-items:center}
nav.jump a{display:inline-block;min-width:44px;text-align:center;padding:6px 10px;border-radius:6px;background:var(--chip);color:var(--fg);text-decoration:none;font-weight:600;font-size:15px}
nav.jump a:hover,nav.jump a:focus-visible{background:var(--fg);color:var(--bg)}
#theme{margin-left:auto;font:inherit;font-size:14px;font-weight:600;padding:6px 12px;border-radius:6px;border:1px solid var(--fg);background:transparent;color:var(--fg);cursor:pointer}
section.c{padding:44px 0;border-bottom:1px solid var(--line)}
.head{display:flex;flex-wrap:wrap;align-items:baseline;gap:8px 16px;margin-bottom:18px}
.head h2{margin:0;font-size:28px;letter-spacing:-.01em}
.head .dir{color:var(--muted);font-size:18px}
.pin{margin-left:auto;font:inherit;font-size:15px;font-weight:600;padding:8px 14px;border-radius:6px;border:1px solid var(--fg);background:transparent;color:var(--fg);cursor:pointer}
.pin[aria-pressed=true]{background:var(--fg);color:var(--bg)}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.panel{display:flex;align-items:center;justify-content:center;padding:44px 24px;border-radius:10px;min-height:240px}
.panel.w{background:#ffffff;border:1px solid var(--line)}
.panel.k{background:#141414;color:#f3f1ec}
.panel svg{display:block;width:560px;max-width:100%;height:auto}
.ctx{margin-top:16px;display:grid;gap:10px}
.ctx .lab{font-size:14px;color:var(--muted)}
.strip-wrap{width:100%;overflow:hidden;border-radius:8px;border:1px solid var(--line)}
.strip{width:1280px;height:72px;display:flex;align-items:center;justify-content:space-between;padding:0 40px;transform-origin:0 0;background:#ffffff;border-bottom:1px solid #e6e4df}
.strip.k{background:#111111;border-bottom-color:#2a2a2a}
.strip .logo svg{display:block;width:auto}
.strip nav{display:flex;gap:32px;font:500 15px/1 system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;color:#6b6b6b}
.strip.k nav{color:#9b9892}
.tiles{display:flex;flex-wrap:wrap;gap:16px;margin-top:16px}
.tile{display:flex;flex-direction:column;align-items:center;gap:8px}
.tile .box{display:flex;align-items:center;justify-content:center;border-radius:8px;width:160px;height:160px;background:#ffffff;border:1px solid var(--line);color:#111111}
.tile .box.k{background:#141414;border-color:#141414;color:#f3f1ec}
.tile .box svg{display:block;width:120px;height:120px}
.tile .cap{font-size:14px;color:var(--muted)}
.tab{width:236px;height:160px;border-radius:8px;border:1px solid var(--line);background:#dfe1e5;display:flex;flex-direction:column;justify-content:center;gap:14px;padding:0 12px}
.tab .t{display:flex;align-items:center;gap:8px;background:#ffffff;border-radius:8px 8px 0 0;padding:8px 10px;color:#202124;font-size:13px;white-space:nowrap;overflow:hidden}
.tab .big{display:flex;align-items:center;gap:10px;font-size:13px;color:#444}
.tab img{flex:none;display:block}
.px{image-rendering:pixelated;image-rendering:crisp-edges}
.prof{width:236px;height:160px;border-radius:8px;border:1px solid var(--line);background:#ffffff;overflow:hidden;position:relative;color:#1d1d1d}
.prof .ban{height:52px;background:#d6dbe0}
.prof img{position:absolute;left:14px;top:20px;width:72px;height:72px;border-radius:50%;border:3px solid #ffffff;background:#ffffff}
.prof .nm{position:absolute;left:14px;top:96px;font-weight:700;font-size:15px}
.prof .meta{position:absolute;left:14px;top:118px;font-size:12px;color:#666}
.prof .fl{position:absolute;right:12px;top:62px;font-size:12px;font-weight:600;color:#0a5aa8;border:1px solid #0a5aa8;border-radius:14px;padding:3px 12px}
.av{width:128px;height:128px;display:block}
.sw{display:inline-flex;gap:4px;vertical-align:middle;margin-left:6px}
.sw i{display:inline-block;width:14px;height:14px;border-radius:3px;border:1px solid var(--line)}
.notes{display:grid;grid-template-columns:1fr 1fr;gap:16px 32px;margin-top:24px;font-size:18px;line-height:1.55}
.notes p{margin:0}
.notes b{display:block;font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin-bottom:4px}
.notes .test{grid-column:1/-1;padding:12px 16px;border-left:4px solid var(--fg);background:var(--card)}
.intro{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px 24px;margin-top:18px;font-size:16px;color:var(--muted)}
.intro b{color:var(--fg)}
.tray{position:fixed;left:0;right:0;bottom:0;z-index:6;background:var(--card);border-top:2px solid var(--fg);box-shadow:0 -6px 24px rgba(0,0,0,.18);max-height:55vh;overflow-y:auto;display:none}
.tray.on{display:block}
.tray .wrap{padding-top:12px;padding-bottom:16px}
.tray .bar{display:flex;align-items:center;gap:12px;margin-bottom:10px;font-weight:600}
.tray .bar button{font:inherit;font-size:14px;padding:6px 12px;border-radius:6px;border:1px solid var(--fg);background:transparent;color:var(--fg);cursor:pointer}
.tray .items{display:flex;flex-wrap:wrap;gap:12px}
.tray .it{width:344px;max-width:100%;background:#ffffff;border:1px solid var(--line);border-radius:8px;padding:12px;color:#111}
.tray .it .lab{display:flex;justify-content:space-between;font-size:13px;margin-bottom:8px;color:#444}
.tray .it .lab button{border:0;background:none;font:inherit;cursor:pointer;color:#a3201b}
.tray .it svg{display:block;width:320px;max-width:100%;height:auto;max-height:90px}
.close{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:20px}
.close .cl{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:12px 14px;font-size:16px;line-height:1.45}
.close .cl b{display:block;font-size:17px}
.close .cl i{display:block;font-style:normal;font-size:13px;letter-spacing:.04em;text-transform:uppercase;color:var(--muted);margin:2px 0 6px}
.close-h{margin:22px 0 0;font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.method{margin-top:18px;padding:14px 18px;border-left:4px solid var(--fg);background:var(--card);font-size:17px;max-width:1100px}
.method p{margin:0 0 8px}
footer{padding:32px 0 60px;color:var(--muted);font-size:15px}
@media (max-width:900px){.close{grid-template-columns:1fr}.pair,.notes{grid-template-columns:1fr}.panel{min-height:0;padding:28px 16px}}
@media (max-width:480px){.wrap{padding:0 16px}.tile .box{width:140px;height:140px}.tile .box svg{width:104px;height:104px}.tab,.prof{width:100%}.tile.wide{width:100%}}
"""

JS = """
(function(){
  var root=document.documentElement,tb=document.getElementById('theme');
  function dark(){var t=root.getAttribute('data-theme');return t?t==='dark':matchMedia('(prefers-color-scheme: dark)').matches}
  function label(){tb.textContent=dark()?'Light board':'Dark board'}
  try{var s=localStorage.getItem('r6-theme');if(s)root.setAttribute('data-theme',s)}catch(e){}
  label();
  tb.addEventListener('click',function(){var t=dark()?'light':'dark';root.setAttribute('data-theme',t);try{localStorage.setItem('r6-theme',t)}catch(e){}label()});
  function fit(){document.querySelectorAll('.strip-wrap').forEach(function(w){var s=w.clientWidth/1280,st=w.firstElementChild;st.style.transform='scale('+s+')';w.style.height=(72*s)+'px'})}
  fit();addEventListener('resize',fit);
  var tray=document.getElementById('tray'),items=tray.querySelector('.items'),pinned=[];
  function render(){
    items.innerHTML='';
    pinned.forEach(function(k){
      var src=document.querySelector('#'+k+' .panel.w svg');
      var it=document.createElement('div');it.className='it';
      var lab=document.createElement('div');lab.className='lab';
      var name=document.createElement('span');name.textContent=k.toUpperCase()+' '+document.querySelector('#'+k+' h2').dataset.name;
      var x=document.createElement('button');x.type='button';x.textContent='Unpin';x.onclick=function(){toggle(k)};
      lab.appendChild(name);lab.appendChild(x);it.appendChild(lab);it.appendChild(src.cloneNode(true));items.appendChild(it);
    });
    tray.classList.toggle('on',pinned.length>0);
    document.getElementById('count').textContent=pinned.length+' pinned';
    document.querySelectorAll('.pin').forEach(function(b){var on=pinned.indexOf(b.dataset.k)>-1;b.setAttribute('aria-pressed',on);b.textContent=on?'Pinned':'Pin to compare'});
    document.body.style.paddingBottom=pinned.length?tray.offsetHeight+'px':'';
  }
  function toggle(k){var i=pinned.indexOf(k);if(i>-1)pinned.splice(i,1);else pinned.push(k);render()}
  document.querySelectorAll('.pin').forEach(function(b){b.addEventListener('click',function(){toggle(b.dataset.k)})});
  document.getElementById('clear').addEventListener('click',function(){pinned=[];render()});
})();
"""

NAV = '<nav aria-hidden="true"><span>Design</span><span>Product</span><span>Business</span><span>Library</span></nav>'


def read(out, fn):
    with open(os.path.join(out, fn), encoding='utf-8') as f:
        return f.read()


def sized(svg_text, h):
    return svg_text.replace('<svg ', f'<svg style="height:{h}px" ', 1)


def swatches(c):
    return ''.join(f'<i style="background:{h}" title="{h}"></i>' for h in c.get('swatch', []))


def write(concepts, out):
    jump = ''.join(f'<a href="#{k.lower()}">{k}</a>' for k in concepts)
    secs = []
    for k, c in concepts.items():
        m = k.lower()
        R = lambda fn: read(out, fn)  # noqa: E731
        rat, orig, v16, test, close = NOTES[k]
        paper = c.get('paper', '#ffffff')
        closest = ''.join(f'<div class="cl"><b>{html.escape(n)}</b><i>{html.escape(cat)}</i>{html.escape(diff)}</div>' for n, cat, diff in close)
        lock, lockd, mono = R(f'{m}-lockup.svg'), R(f'{m}-lockup-dark.svg'), R(f'{m}-mark-mono.svg')
        hh = c.get('hh', 34)
        f16 = f'<img src="{m}-favicon-16.png" width="16" height="16" alt="">'
        f32 = f'<img src="{m}-favicon-32.png" width="32" height="32" alt="">'
        zoom = f'<img class="px" src="{m}-favicon-16.png" width="64" height="64" alt="16px favicon enlarged four times">'
        av = f'<img class="av" src="{m}-avatar-400.png" width="128" height="128" alt="400px avatar, circle crop">'
        secs.append(f'''
<section class="c" id="{m}" aria-labelledby="{m}-h">
 <div class="head"><h2 id="{m}-h" data-name="{html.escape(c['name'])}">{k} &middot; {html.escape(c['name'])}</h2>
  <span class="dir">{html.escape(c['group'])} &middot; {html.escape(c['palette'])}<span class="sw">{swatches(c)}</span></span>
  <button class="pin" type="button" data-k="{m}" aria-pressed="false">Pin to compare</button></div>
 <div class="pair">
  <div class="panel w" style="background:{paper}">{lock}</div>
  <div class="panel k">{lockd}</div>
 </div>
 <div class="ctx">
  <span class="lab">In place: a 1280px site header on white, then on near-black (logo {hh}px tall, scaled to fit this column)</span>
  <div class="strip-wrap"><div class="strip"><span class="logo">{sized(lock, hh)}</span>{NAV}</div></div>
  <div class="strip-wrap"><div class="strip k"><span class="logo">{sized(lockd, hh)}</span>{NAV}</div></div>
 </div>
 <div class="tiles">
  <div class="tile"><div class="box" style="background:{paper}">{R(f'{m}-mark.svg')}</div><span class="cap">Mark</span></div>
  <div class="tile"><div class="box" style="background:{paper}">{R(f'{m}-favicon.svg')}</div><span class="cap">Favicon art (heavier cuts)</span></div>
  <div class="tile"><div class="box k">{R(f'{m}-mark-dark.svg')}</div><span class="cap">Mark on near-black</span></div>
  <div class="tile wide"><div class="tab"><div class="t">{f16}<span>userandproduct</span></div>
   <div class="big">{f32}<span>32px</span>{f16}<span>16px</span></div></div><span class="cap">Favicon PNG, 32px and 16px</span></div>
  <div class="tile"><div class="box">{zoom}</div><span class="cap">16px PNG, enlarged 4x</span></div>
  <div class="tile"><div class="box" style="color:#111111">{mono}</div><span class="cap">Single color</span></div>
  <div class="tile"><div class="box k" style="color:#f3f1ec">{mono}</div><span class="cap">Single color, reversed</span></div>
  <div class="tile"><div class="box" style="background:{paper}">{av}</div><span class="cap">Avatar, 400px render</span></div>
  <div class="tile wide"><div class="prof"><div class="ban"></div><img src="{m}-avatar-400.png" alt="">
   <span class="nm">userandproduct</span><span class="meta">Publishing &middot; 1,204 followers</span><span class="fl">Follow</span></div>
   <span class="cap">Profile tile (mock)</span></div>
 </div>
 <p class="close-h">Closest existing logos (image check; names only)</p>
 <div class="close">{closest}</div>
 <div class="notes">
  <p><b>Rationale</b>{html.escape(rat)}</p>
  <p><b>Figure, rim, type, palette</b>{html.escape(c['reading'])}. Rim: {html.escape(c['rim'].lower())}. {html.escape(c['typeface'])}. {html.escape(c['palette'])}.</p>
  <p><b>Originality</b>{html.escape(orig)}</p>
  <p><b>At 16px</b>{html.escape(v16)}</p>
  <p class="test"><b>Masthead or pitch deck?</b>{html.escape(test)}</p>
 </div>
</section>''')
    page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Logo concepts, round six</title><meta name="color-scheme" content="light dark"><style>{CSS}</style></head>
<body>
<header class="top"><div class="wrap"><h1>Logo concepts, round six: hollowed discs</h1>
<p>Ten round marks, each a solid disc with a figure cut clean through it, the way Tiger Data folds its tiger into a
disc. The figure is the hole; the disc is one color; nothing is painted on top. R1 to R4 cut the tripod from round five
(a spine, two struts, three feet, no cross) out of the disc. R5 to R10 cut other abstract figures. Each sits beside one
settled lowercase wordmark in Instrument Sans or Fraunces.</p>
<p>Each concept is shown at 560px on its paper and on near-black, then in a 1280px site header strip on white and on
near-black, then the mark, the favicon art with its 32px and 16px renders, one color, the avatar (the disc fills it) and a
profile tile. Below that, the three closest existing logos from the image check, and the notes. Pin any lockup to compare.</p>
<div class="method"><p><b>How originality was checked.</b> About ninety logo files and public symbols were downloaded,
rendered side by side and looked at, not only searched by description: Tiger Data, Oyster HR, Carraro, the power symbol,
Neo4j, Asana, Atari, Maserati, Mercedes-Benz, Mitsubishi, Target, Lucid, Mastercard, the peace symbol, the radiation and
biohazard signs, the Deathly Hallows sign, and disc and cut-out marks from HR tech, consulting, fintech, publishing and
developer tools (CircleCI, Umbraco, Coursera, Vodafone, Opera, CodePen, Chase, Hashnode, GraphQL, HubSpot, Linear,
Raycast, Udemy, Fig, Pocket and others).</p>
<p><b>What the check changed.</b> A ring-and-dot terminal on R7 was one rotation from CircleCI, so it became a plain hole.
A U channel holding a point was one step from Umbraco and Udemy and read as a person with raised arms, so it was dropped
for R6. A pointed R3 read as an up arrow and the broad arrow, so its head is cut flat. A two-over-one ring cluster for R4
read as a face. No cut reads as the power, peace, radiation or biohazard signs, and none of R1 to R4 keeps the source's
cross, its braces at the original proportion or its rings at the feet unchanged.</p></div>
<div class="intro"><p><b>Tripod discs:</b> R1 braced tripod, R2 tree of three, R3 reduced tripod, R4 three feet.</p>
<p><b>Imagination discs:</b> R5 reading line, R6 margin, R7 spine and point, R8 crop (two tones), R9 passing, R10 open square.</p></div></div></header>
<nav class="jump" aria-label="Jump to concept"><div class="wrap">{jump}<button type="button" id="theme">Dark board</button></div></nav>
<main class="wrap">{''.join(secs)}</main>
<footer class="wrap">SVG files sit next to this page as r1-lockup.svg, r1-lockup-dark.svg, r1-lockup-mono.svg, r1-mark*.svg,
r1-favicon.svg with r1-favicon-16.png and -32.png, and r1-avatar.svg with r1-avatar-400.png (and so on to r10). Every cut is a
true compound path. Fonts: SIL Open Font License 1.1, which allows logo use. Rebuild with tools/build_round6.py.</footer>
<aside class="tray" id="tray" aria-label="Pinned lockups"><div class="wrap"><div class="bar"><span id="count">0 pinned</span>
<button type="button" id="clear">Clear</button></div><div class="items"></div></div></aside>
<script>{JS}</script>
</body></html>'''
    with open(os.path.join(out, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(page)
