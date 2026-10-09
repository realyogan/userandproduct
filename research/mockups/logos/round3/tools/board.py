"""Write the round-three review board (index.html) with every SVG inlined."""
import os
import html

NOTES = {
    'N1': ("Round one's A, rebuilt in a real face: \"user\" and \"product\" in Instrument Sans Bold, \"and\" "
           "dropped to Instrument Sans Regular in signal blue, so the name reads in three beats and the joining word "
           "is quiet. The mark is the same move on two letters: a bold u and a light blue a in a black tile. "
           "Palette: Ink and Signal Blue.",
           "Two-weight or two-color wordmarks are common (FedEx splits its name by color); this one "
           "differs by lightening the middle word, not a prefix or suffix, and the outlines are not exclusive "
           "until a letter is customized. The \"ua\" tile could recall a language code; it is never shown "
           "without the wordmark at large sizes."),
    'N2': ("A journal nameplate: Fraunces SemiBold capitals tracked wide between a thick and a thin rule above "
           "and below, the way a quarterly or a learned society sets its title. The mark is the U between the "
           "same rules; the favicon drops the rules and sets the U in an oxblood tile. "
           "Palette: Oxblood and Bone.",
           "Ruled serif capitals are a long newspaper and journal tradition (The Economist's old masthead, "
           "Harper's); none sets this name, and the thick-thin double rule pairs are the signature. It is "
           "far from round one's F, which stacked three words in a sans; this is one line in a serif."),
    'N3': ("The name as a ratio: \"user\" over \"product\" in Geist Bold, with a hairline rule between them "
           "and a small graphite \"and\" sitting at the start of the rule, so the stack reads top to bottom and "
           "looks like a fraction, a product manager's way of weighing one thing against another. The mark is "
           "u over p on the same rule. Palette: Newsprint: ink, warm paper and graphite.",
           "Stacked two-line wordmarks are common in magazines; the fraction bar with the joining word on it is "
           "uncommon. A u over p fraction could recall a \"per\" sign or a stock ticker; the rule is wider "
           "than both letters, which keeps it a fraction, not a slash."),
    'N4': ("Round two's M2 u, the part the owner liked, now on its own: two square stems sitting on one solid "
           "half disc, amber bowl and ink stems, with the full name beside it in Inter Display SemiBold. "
           "No p, so nothing fails to gel. In one color a hairline of air keeps the build visible. "
           "Palette: Ink and Amber.",
           "Geometric U marks built from a semicircle are widespread (Uber's old U, many U-initial startups); "
           "this one keeps M2's construction (square stems, a flat-topped half disc, a square slot), which is "
           "rarer, and the two-color split at the bowl line is its signature. No search hit used the same build."),
    'N5': ("A cornerstone. The name is cut into the face of a raised granite tablet in Fraunces SemiBold, "
           "gilded in bronze with the shaded wall of the cut showing, and the founding year MMXXVI between two "
           "rules below it: a building's foundation stone. The mark is the same tablet with an incised u. "
           "Palette: Granite and Bronze.",
           "Engraved and gilded tablets are a heritage look (law firms, banks, universities); the searches found "
           "engraved-style logos but none with this name or this beveled-tablet build. It fixes M9 by putting "
           "the name on the face of the stone, front on, instead of on an isometric box."),
    'N6': ("The name as the monument: \"userandproduct\" in Fraunces SemiBold stands on a solid three-step "
           "podium in royal blue, the stylobate of a temple; the two p descenders are sunk into the stone with a "
           "line of air around them, so the word is set in the base, not floating above it. The mark is the u on "
           "the same steps. Palette: Ink and Royal Blue.",
           "Podium and pedestal icons exist (award and ranking brands); none carries a wordmark with "
           "descenders sunk into the steps. It answers M9 in elevation instead of isometric, so the mark stays "
           "readable at 16px."),
    'N7': ("Three solid steps as one mass, the top step cut in signal red: the reading order the site is built "
           "on, from first principles to the landing, one step at a time. Space Grotesk Bold beside it. "
           "Palette: Signal Red on Black.",
           "Stair marks are common in property and coaching logos, and a stepped silhouette can read as a bar "
           "chart; the steps here are one joined mass with no gaps, and only the landing is colored. The "
           "closest found was STEP Tools (grey steps with red); its steps are separate and its red is lettering."),
    'N8': ("True north: the north arrow from a surveyor's site plan, an arrowhead split down its spine, one half "
           "forest green and the other ink: the bearing a practitioner checks before deciding. Instrument Sans "
           "Bold beside it. Palette: Forest and Cream.",
           "Upward arrowheads recall navigation cursors (map apps tilt theirs 45 degrees) and an earlier two-tone "
           "diamond try was dropped because it read as the Ethereum mark. True North Gear puts an arrow in an "
           "ellipse; this has no ring, stands upright and is split left and right, as on architectural plans."),
    'N9': ("One beam held level on a single pivot: user and business weighed against each other, kept in "
           "balance. The beam in plum sits on an ink fulcrum whose base stands on the baseline of the name, set "
           "in Bricolage Grotesque Bold. Palette: Plum and Parchment.",
           "Lever-and-fulcrum marks are used by firms called Fulcrum and by physics tools; none found pairs a "
           "flat beam with no pans (so it is not the scales of justice). At very small sizes it can read as an "
           "upside-down eject symbol; the beam is always above and wider than the pivot."),
    'N10': ("The lectern: the reading stand one speaks from, drawn in side elevation with a steep brass desk "
            "and a ledge that holds the page, one navy post and a foot that stands on the baseline. One author, "
            "speaking with authority. Inter Display Bold. Palette: Navy and Brass.",
            "Lectern icons exist in stock sets (front-on podiums with a microphone); none found is a side "
            "elevation with a ledge, and none is used as a publication's mark. Without the ledge it could read "
            "as a capital I with a slanted top; the ledge and the wide foot keep it a stand."),
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


EXTRA_CSS = """
.tab .t img,.tab .big img{flex:none;display:block}
.px{image-rendering:pixelated;image-rendering:crisp-edges}
.sw{display:inline-flex;gap:4px;vertical-align:middle;margin-left:6px}
.sw i{display:inline-block;width:14px;height:14px;border-radius:3px;border:1px solid var(--line)}
.panel.w svg.lock-narrow,.panel.k svg.lock-narrow{width:auto;max-height:180px}
.intro{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px 24px;margin-top:18px;font-size:16px;color:var(--muted)}
.intro b{color:var(--fg)}
"""


def swatches(c):
    return ''.join(f'<i style="background:{h}" title="{h}"></i>' for h in c.get('swatch', []))


def write(concepts, out):
    jump = ''.join(f'<a href="#{k.lower()}">{k}</a>' for k in concepts)
    secs = []
    for k, c in concepts.items():
        m = k.lower()
        R = lambda fn: read(out, fn)
        rat, orig = NOTES[k]
        mono = R(f'{m}-mark-mono.svg')
        acc = c['accent']
        lock, lockd = R(f'{m}-lockup.svg'), R(f'{m}-lockup-dark.svg')
        # tall lockups (the two-line stack) are capped in height so they sit at header scale
        vb = [float(v) for v in lock.split('viewBox="')[1].split('"')[0].split()]
        if vb[2] / vb[3] < 2.2:
            lock = lock.replace('<svg ', '<svg class="lock-narrow" ', 1)
            lockd = lockd.replace('<svg ', '<svg class="lock-narrow" ', 1)
        f16 = f'<img src="{m}-favicon-16.png" width="16" height="16" alt="">'
        f32 = f'<img src="{m}-favicon-32.png" width="32" height="32" alt="">'
        zoom = f'<img class="px" src="{m}-favicon-16.png" width="64" height="64" alt="16px favicon enlarged four times">'
        secs.append(f'''
<section class="c" id="{m}" aria-labelledby="{m}-h">
 <div class="head"><h2 id="{m}-h" data-name="{html.escape(c['name'])}">{k} &middot; {html.escape(c['name'])}</h2>
  <span class="dir">{html.escape(c['direction'])} &middot; {html.escape(c['palette'])}<span class="sw">{swatches(c)}</span></span>
  <button class="pin" type="button" data-k="{m}" aria-pressed="false">Pin to compare</button></div>
 <div class="pair">
  <div class="panel w">{lock}</div>
  <div class="panel k">{lockd}</div>
 </div>
 <div class="tiles">
  <div class="tile"><div class="box">{R(f'{m}-mark.svg')}</div><span class="cap">Mark, 128px</span></div>
  <div class="tile"><div class="box k">{R(f'{m}-mark-dark.svg')}</div><span class="cap">Mark on near-black</span></div>
  <div class="tile"><div class="tab"><div class="t">{f16}<span>userandproduct</span></div>
   <div class="big">{f32}<span>32px</span>{f16}<span>16px</span></div></div><span class="cap">Favicon PNG, 32px and 16px</span></div>
  <div class="tile"><div class="box">{zoom}</div><span class="cap">16px PNG, enlarged 4x</span></div>
  <div class="tile"><div class="box" style="color:#111111">{mono}</div><span class="cap">Single color</span></div>
  <div class="tile"><div class="box" style="color:{acc}">{mono}</div><span class="cap">Accent on white</span></div>
  <div class="tile"><div class="box"><div class="avatar">{R(f'{m}-mark.svg')}</div></div><span class="cap">Avatar crop</span></div>
 </div>
 <div class="notes"><p><b>Rationale</b>{html.escape(rat)}</p><p><b>Originality</b>{html.escape(orig)}</p></div>
</section>''')
    page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Logo concepts, round three</title><meta name="color-scheme" content="light dark"><style>{CSS}{EXTRA_CSS}</style></head>
<body>
<header class="top"><div class="wrap"><h1>Logo concepts, round three</h1>
<p>Ten concepts for userandproduct, built on the two things that landed so far: round one's quiet "and" (A) and round two's
monumental weight (M9). Every name is set in a real open-license typeface and outlined, no hand-built letters.
Each lockup is shown at 560px on white and on near-black, then the mark at 128px, the favicon as rendered PNGs at 32px and
16px, one color, the accent alone and an avatar crop. Pin any to compare lockups side by side at 320px.</p>
<div class="intro"><p><b>Wordmarks:</b> N1 Instrument Sans, N2 Fraunces capitals, N3 Geist two-line.</p>
<p><b>Monuments:</b> N5 cornerstone, N6 stylobate. <b>The u:</b> N4.</p>
<p><b>New metaphors:</b> N7 stair, N8 north arrow, N9 fulcrum, N10 lectern.</p></div></div></header>
<nav class="jump" aria-label="Jump to concept"><div class="wrap">{jump}</div></nav>
<main class="wrap">{''.join(secs)}</main>
<footer class="wrap">SVG files sit next to this page as n1-lockup.svg, n1-lockup-dark.svg, n1-lockup-mono.svg, n1-mark*.svg,
n1-favicon.svg and n1-favicon-16.png / -32.png (and so on to n10). Fonts: SIL Open Font License 1.1, which allows logo use
(clause 5 and the preamble: the license "does not apply to any document created using the Font Software").
Rebuild with tools/build_round3.py.</footer>
<aside class="tray" id="tray" aria-label="Pinned lockups"><div class="wrap"><div class="bar"><span id="count">0 pinned</span>
<button type="button" id="clear">Clear</button></div><div class="items"></div></div></aside>
<script>{JS}</script>
</body></html>'''
    with open(os.path.join(out, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(page)
