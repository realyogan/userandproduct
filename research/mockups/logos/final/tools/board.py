"""Write the final colour-theme board (index.html): one full-width section per theme, files linked from
each theme's folder, lockups and marks inlined, a pin-to-compare tray, light and dark board modes."""
import html
import os

from themes import checks

E = html.escape

CSS = """
:root{--bg:#f7f6f3;--fg:#141414;--muted:#5b5a56;--line:#dddad3;--card:#ffffff;--chip:#ecebe6;--flag:#1b2e6e}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#0f0f0f;--fg:#efede8;--muted:#a19e97;--line:#2c2b29;--card:#1a1a19;--chip:#262624;--flag:#a9bbf2}}
:root[data-theme=dark]{--bg:#0f0f0f;--fg:#efede8;--muted:#a19e97;--line:#2c2b29;--card:#1a1a19;--chip:#262624;--flag:#a9bbf2}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;overflow-x:hidden}
a{color:inherit}
.wrap{max-width:1400px;margin:0 auto;padding:0 24px}
header.top{padding:40px 0 20px}
header.top h1{font-size:clamp(28px,4vw,44px);line-height:1.1;margin:0 0 12px;letter-spacing:-.02em}
header.top p{margin:0 0 10px;max-width:880px;color:var(--muted);font-size:18px}
header.top p b{color:var(--fg)}
.hero{margin:24px 0 8px;display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:10px}
.hero a{display:flex;flex-direction:column;gap:8px;align-items:center;padding:16px 8px 12px;border-radius:10px;text-decoration:none;border:1px solid var(--line)}
.hero a svg{width:56px;height:56px;display:block}
.hero a span{font-size:13px;font-weight:600}
nav.jump{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--line)}
nav.jump .wrap{display:flex;flex-wrap:wrap;gap:6px;padding-top:10px;padding-bottom:10px;align-items:center}
nav.jump a{display:inline-flex;align-items:center;gap:6px;min-width:44px;padding:6px 10px;border-radius:6px;background:var(--chip);color:var(--fg);text-decoration:none;font-weight:600;font-size:15px}
nav.jump a i{width:10px;height:10px;border-radius:2px;display:inline-block;transform:rotate(45deg)}
nav.jump a:hover,nav.jump a:focus-visible{background:var(--fg);color:var(--bg)}
#theme{margin-left:auto;font:inherit;font-size:14px;font-weight:600;padding:6px 12px;border-radius:6px;border:1px solid var(--fg);background:transparent;color:var(--fg);cursor:pointer}
section.c{padding:48px 0;border-bottom:1px solid var(--line)}
.head{display:flex;flex-wrap:wrap;align-items:baseline;gap:8px 16px;margin-bottom:18px}
.head h2{margin:0;font-size:30px;letter-spacing:-.015em}
.flag{font-size:14px;font-weight:700;padding:3px 10px;border-radius:4px;background:var(--flag);color:var(--bg)}
.pin{margin-left:auto;font:inherit;font-size:15px;font-weight:600;padding:8px 14px;border-radius:6px;border:1px solid var(--fg);background:transparent;color:var(--fg);cursor:pointer}
.pin[aria-pressed=true]{background:var(--fg);color:var(--bg)}
button:focus-visible,a:focus-visible,input:focus-visible{outline:3px solid #4b7bff;outline-offset:2px}
.sw{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:16px}
.sw .mode{border:1px solid var(--line);border-radius:10px;padding:12px 14px;background:var(--card)}
.sw .mode h3{margin:0 0 8px;font-size:15px}
.sw ul{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:8px 16px}
.sw li{display:flex;align-items:center;gap:10px;font-size:14px;line-height:1.3}
.sw li i{flex:none;width:28px;height:28px;border-radius:6px;border:1px solid rgba(128,128,128,.35)}
.sw li code{font:600 14px/1.3 ui-monospace,Consolas,monospace}
.sw li small{display:block;color:var(--muted);font-size:13px}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.panel{display:flex;align-items:center;justify-content:center;padding:48px 24px;border-radius:10px;min-height:240px;border:1px solid var(--line)}
.panel svg{display:block;width:560px;max-width:100%;height:auto}
.strips{margin-top:16px;display:grid;gap:8px}
.strips img{display:block;width:100%;max-width:1280px;height:auto;border-radius:6px;border:1px solid var(--line)}
.tiles{display:flex;flex-wrap:wrap;gap:16px;margin-top:16px;align-items:flex-start}
.tile{display:flex;flex-direction:column;align-items:center;gap:8px}
.tile .box{display:flex;align-items:center;justify-content:center;border-radius:8px;width:160px;height:160px;border:1px solid var(--line)}
.tile .box svg{display:block;width:128px;height:128px}
.tile .cap{font-size:14px;color:var(--muted);text-align:center;max-width:236px}
.tab{width:236px;height:160px;border-radius:8px;border:1px solid var(--line);background:#dfe1e5;display:flex;flex-direction:column;justify-content:center;gap:14px;padding:0 12px}
.tab.k{background:#202124}
.tab .t{display:flex;align-items:center;gap:8px;background:#ffffff;border-radius:8px 8px 0 0;padding:8px 10px;color:#202124;font-size:13px;white-space:nowrap;overflow:hidden}
.tab.k .t{background:#35363a;color:#e8eaed}
.tab .big{display:flex;align-items:center;gap:10px;font-size:13px;color:#444}
.tab.k .big{color:#bdc1c6}
.tab img{flex:none;display:block}
.ico{width:160px;height:160px;border-radius:8px;border:1px dashed var(--line);display:flex;flex-direction:column;justify-content:center;gap:6px;padding:14px;font-size:14px;line-height:1.35;background:var(--card)}
.ico b{font-size:15px}
.apple{width:120px;height:120px;border-radius:27px;display:block;box-shadow:0 1px 4px rgba(0,0,0,.2)}
.appbox{width:160px;height:160px;border-radius:8px;display:flex;align-items:center;justify-content:center;background:linear-gradient(160deg,#5b6b82,#2d3646)}
.av{width:128px;height:128px;border-radius:50%;display:block;border:1px solid var(--line)}
.og{width:400px;max-width:100%;height:auto;display:block;border-radius:6px;border:1px solid var(--line)}
.tile.og-t{max-width:100%}
.li{display:grid;grid-template-columns:1fr 1fr;gap:16px;align-items:start}
.li figure{margin:0;display:flex;flex-direction:column;gap:8px}
.li img{display:block;max-width:100%;height:auto;border-radius:8px}
.li .ban img{width:560px}
.li .ban img.av{width:128px;height:128px;border-radius:50%;border:1px solid var(--line)}
.li figcaption{font-size:14px;color:var(--muted);margin-bottom:6px}
.mono{display:flex;gap:12px;flex-wrap:wrap}
.mono div{flex:1 1 300px;display:flex;align-items:center;justify-content:center;padding:24px;border-radius:8px;border:1px solid var(--line)}
.mono svg{display:block;width:320px;max-width:100%;height:auto}
.lab{font-size:14px;color:var(--muted);margin:22px 0 8px}
.note{margin:22px 0 0;font-size:18px;max-width:900px}
.rec{margin:12px 0 0;padding:12px 16px;border-left:4px solid var(--flag);background:var(--card);font-size:17px;max-width:900px}
.dl{margin:16px 0 0;font-size:14px;color:var(--muted);line-height:1.8}
.dl a{color:var(--fg);margin-right:10px;white-space:nowrap}
.tray{position:fixed;left:0;right:0;bottom:0;z-index:6;background:var(--card);border-top:2px solid var(--fg);box-shadow:0 -6px 24px rgba(0,0,0,.18);max-height:55vh;overflow-y:auto;display:none}
.tray.on{display:block}
.tray .wrap{padding-top:12px;padding-bottom:16px}
.tray .bar{display:flex;align-items:center;gap:12px;margin-bottom:10px;font-weight:600}
.tray .bar button{font:inherit;font-size:14px;padding:6px 12px;border-radius:6px;border:1px solid var(--fg);background:transparent;color:var(--fg);cursor:pointer}
.tray .items{display:flex;flex-wrap:wrap;gap:12px}
.tray .it{width:344px;max-width:100%;border:1px solid var(--line);border-radius:8px;padding:12px}
.tray .it .lab2{display:flex;justify-content:space-between;font-size:13px;margin-bottom:8px;color:#555}
.tray .it .lab2 button{border:0;background:none;font:inherit;cursor:pointer;color:#a3201b}
.tray .it svg{display:block;width:320px;max-width:100%;height:auto}
footer{padding:32px 0 60px;color:var(--muted);font-size:15px}
@media (max-width:900px){.pair,.sw,.li{grid-template-columns:1fr}.panel{min-height:0;padding:28px 16px}.hero{grid-template-columns:repeat(5,minmax(0,1fr))}.hero a svg{width:40px;height:40px}}
@media (max-width:480px){.wrap{padding:0 16px}.hero{grid-template-columns:repeat(2,minmax(0,1fr))}.tile .box,.ico,.appbox{width:140px;height:140px}.tile .box svg{width:104px;height:104px}.tab{width:100%}.tile.wide{width:100%}.pin{margin-left:0}}
"""

JS = """
(function(){
  var root=document.documentElement,tb=document.getElementById('theme');
  function dark(){var t=root.getAttribute('data-theme');return t?t==='dark':matchMedia('(prefers-color-scheme: dark)').matches}
  function label(){tb.textContent=dark()?'Light board':'Dark board'}
  try{var s=localStorage.getItem('final-theme');if(s)root.setAttribute('data-theme',s)}catch(e){}
  label();
  tb.addEventListener('click',function(){var t=dark()?'light':'dark';root.setAttribute('data-theme',t);try{localStorage.setItem('final-theme',t)}catch(e){}label()});
  var tray=document.getElementById('tray'),items=tray.querySelector('.items'),pinned=[];
  function render(){
    items.innerHTML='';
    pinned.forEach(function(k){
      var sec=document.getElementById(k),src=sec.querySelector('.panel.w svg');
      var it=document.createElement('div');it.className='it';it.style.background=sec.dataset.bg;
      var lab=document.createElement('div');lab.className='lab2';
      var name=document.createElement('span');name.textContent=k.toUpperCase()+' '+sec.querySelector('h2').dataset.name;
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

FILES = ['lockup-light.svg', 'lockup-dark.svg', 'lockup-mono.svg', 'mark.svg', 'mark-dark.svg', 'favicon.svg',
         'favicon-16.png', 'favicon-32.png', 'favicon.ico', 'apple-touch-icon-180.png', 'icon-512.png',
         'avatar-400.png', 'og-1200x630.png', 'og-dark-1200x630.png', 'header-light.png', 'header-dark.png',
         'linkedin-banner-1128x191.png', 'linkedin-banner-dark-1128x191.png', 'linkedin-avatar-400.png',
         'linkedin-mock-light.png', 'linkedin-mock-dark.png', 'linkedin-post-light.png']


def read(out, slug, fn):
    with open(os.path.join(out, slug, fn), encoding='utf-8') as f:
        return f.read()


def chip(hexc, role, r=None):
    rr = f'<small>{r:.1f}:1 on the background</small>' if r is not None else '<small>&nbsp;</small>'
    return f'<li><i style="background:{hexc}"></i><span>{E(role)} <code>{hexc}</code>{rr}</span></li>'


def swatch_block(t, mode, title):
    c, r = t[mode], checks(t)[mode]
    two = c['big'] != c['small']
    rows = []
    for hexc, v in r['marks']:
        if t['odd'] and hexc == t['odd'][mode]:
            role = 'Mark, the one coloured tile'
        elif two and hexc == c['big']:
            role = 'Mark, large tiles'
        elif two and hexc == c['small']:
            role = 'Mark, small tiles'
        else:
            role = 'Mark'
        rows.append(chip(hexc, role, v))
    rows.append(chip(c['word'], 'Wordmark', r['word']))
    rows.append(chip(c['link'], 'Link accent', r['link']))
    rows.append(chip(c['bg'], 'Background'))
    return f'<div class="mode"><h3>{title}</h3><ul>{"".join(rows)}</ul></div>'


def section(t, out):
    k, s = t['key'].lower(), t['slug']
    R = lambda fn: read(out, s, fn)  # noqa: E731
    L, D = t['L'], t['D']
    flag = '<span class="flag">Recommended</span>' if t['rec'] else ''
    rec = f'<p class="rec"><b>Recommended.</b> {E(t["rec"])}</p>' if t['rec'] else ''
    f16 = f'<img src="{s}/favicon-16.png" width="16" height="16" alt="">'
    f32 = f'<img src="{s}/favicon-32.png" width="32" height="32" alt="">'
    dl = ' '.join(f'<a href="{s}/{fn}"{" data-lockup" if fn == "lockup-light.svg" else ""}>{fn}</a>' for fn in FILES)
    return f'''
<section class="c" id="{k}" data-bg="{L['bg']}" aria-labelledby="{k}-h">
 <div class="head"><h2 id="{k}-h" data-name="{E(t['name'])}">{t['key']} &middot; {E(t['name'])}</h2>{flag}
  <button class="pin" type="button" data-k="{k}" aria-pressed="false">Pin to compare</button></div>
 <div class="sw">{swatch_block(t, 'L', 'Light')}{swatch_block(t, 'D', 'Dark')}</div>
 <div class="pair">
  <div class="panel w" style="background:{L['bg']}">{R('lockup-light.svg')}</div>
  <div class="panel k" style="background:{D['bg']};border-color:{D['bg']}">{R('lockup-dark.svg')}</div>
 </div>
 <p class="lab">The 1280 &times; 72 site header, light and dark (header-light.png, header-dark.png)</p>
 <div class="strips"><img src="{s}/header-light.png" width="1280" height="72" alt="{E(t['name'])} site header, light" loading="lazy">
  <img src="{s}/header-dark.png" width="1280" height="72" alt="{E(t['name'])} site header, dark" loading="lazy"></div>
 <div class="tiles">
  <div class="tile"><div class="box" style="background:{L['bg']}">{R('mark.svg')}</div><span class="cap">Mark at 128px</span></div>
  <div class="tile"><div class="box" style="background:{D['bg']};border-color:{D['bg']}">{R('mark-dark.svg')}</div><span class="cap">Mark, dark</span></div>
  <div class="tile wide"><div class="tab"><div class="t">{f16}<span>userandproduct</span></div>
   <div class="big">{f32}<span>32px</span>{f16}<span>16px</span></div></div><span class="cap">Favicon in a light tab</span></div>
  <div class="tile wide"><div class="tab k"><div class="t">{f16}<span>userandproduct</span></div>
   <div class="big">{f32}<span>32px</span>{f16}<span>16px</span></div></div><span class="cap">Favicon in a dark tab</span></div>
  <div class="tile"><div class="ico"><b>favicon.ico</b><span>16, 32 and 48px in one file, for old browsers and Windows.</span><a href="{s}/favicon.ico">Download</a></div><span class="cap">ICO</span></div>
  <div class="tile"><div class="appbox"><img class="apple" src="{s}/apple-touch-icon-180.png" width="120" height="120" alt="" loading="lazy"></div><span class="cap">Apple touch icon, 180px</span></div>
  <div class="tile og-t"><img class="og" src="{s}/og-1200x630.png" width="400" height="210" alt="{E(t['name'])} social image, light" loading="lazy"><span class="cap">Social image, 1200 &times; 630</span></div>
  <div class="tile og-t"><img class="og" src="{s}/og-dark-1200x630.png" width="400" height="210" alt="{E(t['name'])} social image, dark" loading="lazy"><span class="cap">Social image, dark</span></div>
 </div>
 <p class="lab">LinkedIn: company page light and dark, a shared article, the cover banner</p>
 <div class="li">
  <figure><img src="{s}/linkedin-mock-light.png" width="800" height="360" alt="{E(t['name'])} LinkedIn company page, light" loading="lazy"><figcaption>Company page, light (linkedin-mock-light.png)</figcaption></figure>
  <figure><img src="{s}/linkedin-mock-dark.png" width="800" height="360" alt="{E(t['name'])} LinkedIn company page, dark" loading="lazy"><figcaption>Company page, dark (linkedin-mock-dark.png)</figcaption></figure>
  <figure class="post"><img src="{s}/linkedin-post-light.png" width="560" height="462" alt="{E(t['name'])} LinkedIn post with link preview" loading="lazy"><figcaption>A shared article with its link preview (linkedin-post-light.png)</figcaption></figure>
  <figure class="ban"><img src="{s}/linkedin-banner-1128x191.png" width="560" height="95" alt="{E(t['name'])} LinkedIn banner, light" loading="lazy"><figcaption>Cover banner at 560px (linkedin-banner-1128x191.png, upload size 1128 &times; 191)</figcaption>
   <img src="{s}/linkedin-banner-dark-1128x191.png" width="560" height="95" alt="{E(t['name'])} LinkedIn banner, dark" loading="lazy"><figcaption>Dark banner (linkedin-banner-dark-1128x191.png)</figcaption>
   <img class="av" src="{s}/linkedin-avatar-400.png" width="128" height="128" alt="" loading="lazy"><figcaption>Avatar as LinkedIn crops it (linkedin-avatar-400.png, 21% margin)</figcaption></figure>
 </div>
 <p class="lab">Single colour (lockup-mono.svg uses currentColor, so it takes any one ink)</p>
 <div class="mono"><div style="background:#ffffff;color:#141414">{R('lockup-mono.svg')}</div><div style="background:#141414;color:#f1eee7;border-color:#141414">{R('lockup-mono.svg')}</div></div>
 <p class="note">{E(t['feel'])}</p>
 {rec}
 <p class="dl"><b>Download pack:</b> {dl}</p>
</section>'''


def write(themes, out):
    jump = ''.join(f'<a href="#{t["key"].lower()}"><i style="background:{t["L"]["big"]}"></i>{t["key"]}</a>' for t in themes)
    hero = ''.join(f'<a href="#{t["key"].lower()}" style="background:{t["L"]["bg"]};color:{t["L"]["word"]}">'
                   f'{read(out, t["slug"], "mark.svg")}<span>{E(t["name"])}</span></a>' for t in themes)
    recs = [t for t in themes if t['rec']]
    secs = ''.join(section(t, out) for t in themes)
    page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Final logo: colour themes</title><meta name="color-scheme" content="light dark"><style>{CSS}</style>
<link rel="stylesheet" href="../hub-menu.css">
</head>
<body>
<header class="top"><div class="wrap"><h1>Final logo: colour themes</h1>
<p>The mark is <b>S5, two sizes</b>, from Round 7 tiles: four filled tiles turned 45 degrees, the top and bottom pair
large, the left and right pair small. The wordmark is fixed: lowercase <b>userandproduct</b> in Inter Display Bold,
tracking &minus;25, set beside the mark as on P8 (mark 1.4 cap heights tall, the same gap and baseline). Only colour
changes below.</p>
<p>Ten single-colour schemes: press red first, then nine blues from darkest to brightest. Each blue has its
light and dark shades tuned separately; the wordmark is black on light and off-white on dark, so the blue lives only
in the mark. Every wordmark clears 7:1 on its background and every mark clears 3:1. Recommended:
<b>{E(recs[0]['key'])} {E(recs[0]['name'])}</b> and <b>{E(recs[1]['key'])} {E(recs[1]['name'])}</b>. Each note
also says how that blue would sit beside press red as a later accent. Pin any theme to compare the lockups side by side.</p>
<div class="hero">{hero}</div></div></header>
<nav class="jump" aria-label="Jump to theme"><div class="wrap">{jump}<button type="button" id="theme">Dark board</button></div></nav>
<main class="wrap">{secs}</main>
<footer class="wrap">Each theme folder holds the same twenty-two files. SVGs are outlined paths (no fonts needed); the
favicon.svg switches to the dark colours in dark browser tabs. Contrast is WCAG 2. Fonts: SIL Open Font License 1.1.
Rebuild with tools/build_final.py.</footer>
<aside class="tray" id="tray" aria-label="Pinned lockups"><div class="wrap"><div class="bar"><span id="count">0 pinned</span>
<button type="button" id="clear">Clear</button></div><div class="items"></div></div></aside>
<script>{JS}</script>
<script src="../hub-menu.js" data-board="final"></script>
</body></html>'''
    with open(os.path.join(out, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(page)
