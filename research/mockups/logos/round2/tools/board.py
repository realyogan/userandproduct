"""Write the round-two review board (index.html) with every SVG inlined."""
import os
import html

NOTES = {
    'M1': ("Swiss International style. One line of grotesque lowercase on a strict baseline grid; the only "
           "mark is a deep red square as tall as the ascenders, cut once exactly on the x-height line, so the "
           "mark is the grid the letters stand on. Accent: deep red.",
           "A square with a horizontal cut can read as a flag or a sliced block; the cut sits high (on the "
           "x-height), not in the middle, so it never reads as an equals sign. Round one's two-line wordmark "
           "(A) was the first draft of this concept, so it was changed to a single line."),
    'M2': ("Bauhaus. Primary solids build the letters: two squares and an amber half-disc make the u; a black "
           "circle on a blade-shaped triangle makes the p. Flat colour, no outlines, every piece separate. "
           "Accent: amber.",
           "Any u-and-p pair can recall a monogram; this one is assembled from loose primary pieces with gaps, "
           "has no shared stem, no arrow and no underline, and puts the accent in the u's bowl rather than "
           "the p's (changed from a black u and blue p, which was too close to round one's B)."),
    'M3': ("Brutalist. The mark is one cast block, a squared u with a narrow slot, whose top corner has been "
           "cut off clean and set aside in bronze; the name is cut out of a single chamfered slab. "
           "Accent: bronze.",
           "A heavy squared U can recall a magnet icon; the slot is a narrow cut, not a counter, and the "
           "detached bronze chip is the signature. It replaced a three-block u that read too much like round "
           "one's keystone arch (K)."),
    'M4': ("Art Deco. A symmetrical setback tower in one monoline outline with amber flutes and a spire, "
           "standing on a rule over the name in wide spaced capitals, closed by a double amber rule: a "
           "crest lockup. Accent: amber gold.",
           "Skyscraper silhouettes are common in property logos and can recall the Chrysler or Empire State "
           "buildings; this one has no crown, windows or perspective, only a stepped line and vertical "
           "flutes, and it is always shown on the rule with the name as a crest."),
    'M5': ("Japanese mon. One element, the lowercase u, repeated three times around the centre and knocked "
           "out of a stamped red disc inside a thin rim: three arches meeting in one knot. Accent: deep red.",
           "Two earlier tries were dropped: four arches read as a medical cross, and three separated arches "
           "read as the biohazard sign. Joined, it can still recall a cloverleaf or a trefoil knot; the "
           "arms are straight u stems and the rim keeps it a crest, not a leaf."),
    'M6': ("Blueprint and scientific notation. One heavy element, a solid 45-degree set square with its "
           "right-angle tick, inside thin blue construction lines: a compass arc, extended axes and a "
           "dimension line. The method, drawn. Accent: deep blue.",
           "Alone the triangle and arc could read as a pie chart or a sail; the construction lines, "
           "dimension ticks and the cut right-angle mark make it a measured drawing, and the favicon keeps "
           "the arc so it never becomes a plain triangle."),
    'M7': ("Letterpress seal or notary stamp. A round seal with the name spread around the rim, a single "
           "dot at the foot and a pen nib as the central device: written, signed, certified. Accent: deep green.",
           "Notary and university seals all share this form; the nib (not a star, crest or initials) and the "
           "single unbroken name around three-quarters of the rim keep it ours. It is not a fountain-pen "
           "brand mark: no pen body, no star, no flourish."),
    'M8': ("Optical pattern. A square field of black stripes in which a heavy u appears only because its "
           "stripes are shifted half a step and turn blue; at a distance the u resolves. Accent: deep blue.",
           "Striped type recalls IBM and a striped sphere recalls the old AT&T globe; here the stripes are "
           "the background, not the letter, the field is square, and the letter exists only through the "
           "offset. The favicon fills the u solid so it survives at 16px."),
    'M9': ("Isometric and dimensional. The name is cut through the face of a long plinth with a green top "
           "and a grey end; the mark is a two-tier plinth drawn in true isometric. Solid, monumental. "
           "Accent: deep green.",
           "Isometric cubes are everywhere (wireframe boxes, open boxes); this is a stepped two-tier plinth "
           "with solid faces and no wireframe, and the lockup puts the name on the stone instead of beside it."),
    'M10': ("Minimal mark-and-dot. A single line, the product, with a single point, the user, resting on it "
            "at the golden section; a light, widely spaced wordmark beside it. The quietest mark. "
            "Accent: deep red.",
            "Could be mistaken for a slider control; the dot sits exactly tangent on top, never threaded "
            "through, and the line has square ends. The nearest search result (a dot on a wave) uses a curve. "
            "It stays to the left of the name, never under it, so it is not an underline."),
}


def read(out, fn):
    with open(os.path.join(out, fn), encoding='utf-8') as f:
        return f.read()


CSS = """
:root{--bg:#f7f6f3;--fg:#141414;--muted:#5b5a56;--line:#dddad3;--card:#ffffff;--chip:#ecebe6;--accentui:#a3201b}
@media (prefers-color-scheme:dark){:root{--bg:#0f0f0f;--fg:#efede8;--muted:#a19e97;--line:#2c2b29;--card:#1a1a19;--chip:#262624;--accentui:#e2574c}}
*{box-sizing:border-box}
html{scroll-padding-top:64px}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif}
.wrap{max-width:1400px;margin:0 auto;padding:0 24px}
header.top{padding:40px 0 16px}
header.top h1{font-size:clamp(28px,4vw,44px);line-height:1.1;margin:0 0 10px;letter-spacing:-.02em}
header.top p{margin:0;max-width:820px;color:var(--muted);font-size:18px}
nav.jump{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--line)}
nav.jump .wrap{display:flex;flex-wrap:wrap;gap:6px;padding-top:10px;padding-bottom:10px}
nav.jump a{display:inline-block;min-width:44px;text-align:center;padding:6px 10px;border-radius:6px;background:var(--chip);color:var(--fg);text-decoration:none;font-weight:600;font-size:15px}
nav.jump a:hover,nav.jump a:focus-visible{background:var(--fg);color:var(--bg)}
section.c{padding:40px 0;border-bottom:1px solid var(--line)}
.head{display:flex;flex-wrap:wrap;align-items:baseline;gap:8px 16px;margin-bottom:18px}
.head h2{margin:0;font-size:28px;letter-spacing:-.01em}
.head .dir{color:var(--muted);font-size:18px}
.pin{margin-left:auto;font:inherit;font-size:15px;font-weight:600;padding:8px 14px;border-radius:6px;border:1px solid var(--fg);background:transparent;color:var(--fg);cursor:pointer}
.pin[aria-pressed=true]{background:var(--fg);color:var(--bg)}
.pair{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.panel{display:flex;align-items:center;justify-content:center;padding:44px 24px;border-radius:10px;min-height:260px}
.panel.w{background:#ffffff;border:1px solid var(--line)}
.panel.k{background:#141414;color:#f3f1ec}
.panel svg{display:block;width:560px;max-width:100%;height:auto}
.tiles{display:flex;flex-wrap:wrap;gap:16px;margin-top:16px}
.tile{display:flex;flex-direction:column;align-items:center;gap:8px}
.tile .box{display:flex;align-items:center;justify-content:center;border-radius:8px;width:160px;height:160px;background:#ffffff;border:1px solid var(--line);color:#111111}
.tile .box.k{background:#141414;border-color:#141414;color:#f3f1ec}
.tile .box svg{display:block;width:128px;height:128px}
.tile .cap{font-size:14px;color:var(--muted)}
.tab{width:236px;height:160px;border-radius:8px;border:1px solid var(--line);background:#dfe1e5;display:flex;flex-direction:column;justify-content:center;gap:14px;padding:0 12px}
.tab .t{display:flex;align-items:center;gap:8px;background:#ffffff;border-radius:8px 8px 0 0;padding:8px 10px;color:#202124;font-size:13px;white-space:nowrap;overflow:hidden}
.tab .t svg{flex:none}
.tab .big{display:flex;align-items:center;gap:10px;font-size:13px;color:#444}
.avatar{width:128px;height:128px;border-radius:50%;overflow:hidden;background:#ffffff;display:flex;align-items:center;justify-content:center;border:1px solid var(--line)}
.tile .box .avatar svg{width:86px;height:86px}
.notes{display:grid;grid-template-columns:1fr 1fr;gap:16px 32px;margin-top:22px;font-size:18px;line-height:1.55}
.notes p{margin:0}
.notes b{display:block;font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin-bottom:4px}
.tray{position:fixed;left:0;right:0;bottom:0;z-index:6;background:var(--card);border-top:2px solid var(--fg);box-shadow:0 -6px 24px rgba(0,0,0,.18);max-height:55vh;overflow-y:auto;display:none}
.tray.on{display:block}
.tray .wrap{padding-top:12px;padding-bottom:16px}
.tray .bar{display:flex;align-items:center;gap:12px;margin-bottom:10px;font-weight:600}
.tray .bar button{font:inherit;font-size:14px;padding:6px 12px;border-radius:6px;border:1px solid var(--fg);background:transparent;color:var(--fg);cursor:pointer}
.tray .items{display:flex;flex-wrap:wrap;gap:12px}
.tray .it{width:344px;max-width:100%;background:#ffffff;border:1px solid var(--line);border-radius:8px;padding:12px;color:#111}
.tray .it .lab{display:flex;justify-content:space-between;font-size:13px;margin-bottom:8px;color:#444}
.tray .it .lab button{border:0;background:none;font:inherit;cursor:pointer;color:#a3201b}
.tray .it svg{display:block;width:320px;max-width:100%;height:auto}
body.has-tray{padding-bottom:var(--trayh,0)}
footer{padding:32px 0 60px;color:var(--muted);font-size:15px}
@media (max-width:900px){.pair,.notes{grid-template-columns:1fr}.panel{min-height:0;padding:28px 16px}}
@media (max-width:480px){.wrap{padding:0 16px}.tile .box{width:140px;height:140px}.tile .box svg{width:112px;height:112px}.tab{width:100%}}
"""

JS = """
(function(){
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


def write(concepts, out):
    jump = ''.join(f'<a href="#{k.lower()}">{k}</a>' for k in concepts)
    secs = []
    for k, c in concepts.items():
        m = k.lower()
        R = lambda fn: read(out, fn)
        rat, orig = NOTES[k]
        mono = R(f'{m}-mark-mono.svg')
        accent_hex = c['accent'].split('#')[1][:6]
        fav = R(f'{m}-favicon.svg')
        fav16 = fav.replace('<svg ', '<svg width="16" height="16" ', 1)
        fav32 = fav.replace('<svg ', '<svg width="32" height="32" ', 1)
        secs.append(f'''
<section class="c" id="{m}" aria-labelledby="{m}-h">
 <div class="head"><h2 id="{m}-h" data-name="{html.escape(c['name'])}">{k} &middot; {html.escape(c['name'])}</h2>
  <span class="dir">{html.escape(c['direction'])} &middot; {html.escape(c['accent'])}</span>
  <button class="pin" type="button" data-k="{m}" aria-pressed="false">Pin to compare</button></div>
 <div class="pair">
  <div class="panel w">{R(f'{m}-lockup.svg')}</div>
  <div class="panel k">{R(f'{m}-lockup-dark.svg')}</div>
 </div>
 <div class="tiles">
  <div class="tile"><div class="box">{R(f'{m}-mark.svg')}</div><span class="cap">Mark, 128px</span></div>
  <div class="tile"><div class="box k">{R(f'{m}-mark-dark.svg')}</div><span class="cap">Mark on near-black</span></div>
  <div class="tile"><div class="tab"><div class="t">{fav16}<span>userandproduct</span></div>
   <div class="big">{fav32}<span>32px</span>{fav16}<span>16px</span></div></div><span class="cap">Favicon, 32px and 16px</span></div>
  <div class="tile"><div class="box" style="color:#111111">{mono}</div><span class="cap">Single colour</span></div>
  <div class="tile"><div class="box" style="color:#{accent_hex}">{mono}</div><span class="cap">Accent on white</span></div>
  <div class="tile"><div class="box"><div class="avatar">{R(f'{m}-mark.svg')}</div></div><span class="cap">Avatar crop</span></div>
 </div>
 <div class="notes"><p><b>Rationale</b>{html.escape(rat)}</p><p><b>Originality</b>{html.escape(orig)}</p></div>
</section>''')
    page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Logo concepts, round two</title><meta name="color-scheme" content="light dark"><style>{CSS}</style></head>
<body>
<header class="top"><div class="wrap"><h1>Logo concepts, round two</h1>
<p>Ten concepts for userandproduct, each from its own art direction. Every lockup is shown at 560px on white and on near-black,
then the mark at 128px, the favicon at 32px and 16px, one colour, the accent alone and an avatar crop. Pin any to compare
lockups side by side at 320px.</p></div></header>
<nav class="jump" aria-label="Jump to concept"><div class="wrap">{jump}</div></nav>
<main class="wrap">{''.join(secs)}</main>
<footer class="wrap">SVG files sit next to this page as m1-lockup.svg, m1-lockup-dark.svg, m1-lockup-mono.svg, m1-mark*.svg and
m1-favicon.svg (and so on to m10). Rebuild with tools/build_round2.py.</footer>
<aside class="tray" id="tray" aria-label="Pinned lockups"><div class="wrap"><div class="bar"><span id="count">0 pinned</span>
<button type="button" id="clear">Clear</button></div><div class="items"></div></div></aside>
<script>{JS}</script>
</body></html>'''
    with open(os.path.join(out, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(page)
