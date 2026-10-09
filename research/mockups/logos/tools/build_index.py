"""Writes index.html: a review board with one full-width section per concept.
All SVG is inlined and sized by CSS from its viewBox (no width or height attributes)."""
import html
import os


def _svg(markup_fn, art, mode, acc, idp, cls):
    m = markup_fn(art, mode, acc, idp, standalone=False)
    return m.replace("<svg ", f'<svg class="{cls}" focusable="false" ', 1)


CSS = """
:root{--bg:#f6f6f7;--fg:#0a0a0c;--muted:#52525b;--card:#fff;--line:#e4e4e7;--bar:rgba(246,246,247,.92)}
@media (prefers-color-scheme:dark){:root{--bg:#111114;--fg:#f4f4f5;--muted:#a1a1aa;--card:#1a1a1d;--line:#2c2c31;--bar:rgba(17,17,20,.92)}}
*{box-sizing:border-box}
html{scroll-padding-top:72px}
body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;overflow-x:hidden}
.wrap{max-width:1400px;margin:0 auto;padding:0 24px}
.top{position:sticky;top:0;z-index:20;background:var(--bar);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.top .wrap{display:flex;align-items:center;gap:12px 20px;flex-wrap:wrap;min-height:56px;padding-top:8px;padding-bottom:8px}
.top strong{font-size:15px;letter-spacing:-.01em}
.jump{display:flex;flex-wrap:wrap;gap:4px}
.jump a{display:inline-block;min-width:32px;text-align:center;padding:4px 6px;border-radius:4px;text-decoration:none;color:var(--fg);font:600 14px/1.4 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
.jump a:hover,.jump a:focus-visible{background:var(--line)}
.cmp{margin-left:auto;display:flex;gap:8px;align-items:center;font-size:14px;color:var(--muted)}
button{font:inherit;font-size:14px;cursor:pointer;border:1px solid var(--line);background:var(--card);color:var(--fg);border-radius:4px;padding:6px 12px}
button[aria-pressed=true]{background:var(--fg);color:var(--bg);border-color:var(--fg)}
h1{font-size:clamp(30px,4vw,48px);line-height:1.1;letter-spacing:-.03em;margin:40px 0 12px}
.lede{color:var(--muted);max-width:80ch}
.notes{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,420px),1fr));gap:24px;margin:24px 0 8px}
.notes h3,.label{font:600 12px/1.4 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;text-transform:uppercase;letter-spacing:.05em;color:var(--muted);margin:0 0 8px}
.notes ol{margin:0;padding-left:20px}
.sw{display:inline-flex;align-items:center;gap:8px}
.sw i{width:16px;height:16px;border-radius:3px;display:inline-block;flex:none}
section.c{border-top:1px solid var(--line);padding:48px 0}
.head{display:flex;flex-wrap:wrap;gap:8px 16px;align-items:center}
h2{font-size:32px;line-height:1.2;letter-spacing:-.03em;margin:0}
.tag{font:500 12px/1 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;text-transform:uppercase;letter-spacing:.05em;padding:6px 8px;border:1px solid var(--line);border-radius:4px;color:var(--muted)}
.head button{margin-left:auto}
.why{font-size:18px;max-width:75ch;margin:12px 0 4px}
.meta{font-size:15px;color:var(--muted);margin:0 0 24px}
.pair{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px}
.pane{border-radius:8px;padding:48px 40px;display:flex;align-items:center;justify-content:center;min-height:220px}
.pane.w{background:#fff;border:1px solid #e4e4e7}
.pane.k{background:#0a0a0c;border:1px solid #0a0a0c}
.pane .lock{width:100%;max-width:560px;height:auto;display:block}
.pane .lock.st{max-width:420px}
.sub{margin-top:16px}
.tiles{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;margin-top:16px}
.tile{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:16px;display:flex;flex-direction:column;gap:12px;min-width:0}
.tile .stage{flex:1;border-radius:6px;background:#fff;border:1px solid #e4e4e7;display:flex;align-items:center;justify-content:center;gap:16px;padding:20px;min-height:176px;flex-wrap:wrap}
.m128{width:128px;height:auto;display:block}
.m48{width:48px;height:auto;display:block}
.m32{width:32px;height:auto;display:block}
.m16{width:16px;height:auto;display:block;flex:none}
.monolock{width:100%;height:auto;display:block}
.tabs{flex-direction:column;align-items:stretch;justify-content:center;background:#dedee3!important;gap:0!important;padding:16px 12px!important}
.tab{display:flex;align-items:center;gap:8px;background:#fff;border-radius:8px 8px 0 0;padding:8px 12px;font:13px/1 system-ui,sans-serif;color:#0a0a0c;max-width:220px;white-space:nowrap;overflow:hidden}
.tab.k{background:#2a2a2e;color:#f4f4f5;margin-top:12px}
.tab span{overflow:hidden;text-overflow:ellipsis}
.big{display:flex;align-items:center;gap:16px;justify-content:center;margin-top:12px}
.tray{position:fixed;left:0;right:0;bottom:0;z-index:30;background:var(--card);border-top:1px solid var(--line);box-shadow:0 -8px 24px rgba(0,0,0,.12);display:none}
.tray.on{display:block}
.tray .wrap{display:flex;gap:16px;align-items:center;padding-top:12px;padding-bottom:12px}
.tray .row{display:flex;gap:16px;overflow-x:auto;flex:1;padding-bottom:4px}
.pin{flex:none;width:320px;background:#fff;border:1px solid #e4e4e7;border-radius:6px;padding:16px;color:#0a0a0c;position:relative}
.pin .lock{width:100%;height:auto;display:block}
.pin b{display:block;font:600 12px/1 ui-monospace,monospace;color:#71717a;margin-bottom:10px}
body.has-tray{padding-bottom:180px}
@media (max-width:1100px){.tiles{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:720px){.pair{grid-template-columns:minmax(0,1fr)}.tiles{grid-template-columns:minmax(0,1fr)}
.pane{padding:32px 20px;min-height:140px}h2{font-size:26px}.pin{width:240px}
.top strong{display:none}.top .wrap{flex-wrap:nowrap}.jump{flex-wrap:nowrap;overflow-x:auto;min-width:0;flex:1}.cmp span{display:none}}
a{color:inherit}
"""

JS = """
(function(){
  var tray=document.getElementById('tray'),row=document.getElementById('trayrow'),count=document.getElementById('count');
  var pinned=[];
  function draw(){
    row.innerHTML='';
    pinned.forEach(function(id){
      var src=document.querySelector('#'+id+' .pane.w .lock');
      var d=document.createElement('div');d.className='pin';
      d.innerHTML='<b>'+id.toUpperCase()+'</b>';
      d.appendChild(src.cloneNode(true));row.appendChild(d);
    });
    count.textContent=pinned.length;
    tray.classList.toggle('on',pinned.length>0);
    document.body.classList.toggle('has-tray',pinned.length>0);
    document.querySelectorAll('[data-pin]').forEach(function(b){
      var on=pinned.indexOf(b.getAttribute('data-pin'))>-1;
      b.setAttribute('aria-pressed',on);b.textContent=on?'Pinned':'Pin to compare';
    });
  }
  document.querySelectorAll('[data-pin]').forEach(function(b){
    b.addEventListener('click',function(){
      var id=b.getAttribute('data-pin'),i=pinned.indexOf(id);
      if(i>-1)pinned.splice(i,1);else pinned.push(id);
      draw();
    });
  });
  document.getElementById('clear').addEventListener('click',function(){pinned=[];draw();});
  draw();
})();
"""


def write(built, markup_fn, accents, ink, out):
    parts, jumps = [], []
    for c, files in built:
        acc = c["accent"]
        A = accents[acc]
        cid = c["id"].lower()
        lock, icon = c["lockup"], c["icon"]
        jumps.append(f'<a href="#{cid}" title="{html.escape(c["name"])}">{c["id"]}</a>')
        pair = (f'<div class="pair"><div class="pane w">{_svg(markup_fn, lock, "light", acc, cid + "lw", "lock")}</div>'
                f'<div class="pane k">{_svg(markup_fn, lock, "dark", acc, cid + "lk", "lock")}</div></div>')
        if "alt" in c:
            st = c["alt"]["art"]
            pair += (f'<p class="label sub">{html.escape(c["alt"]["label"])}</p><div class="pair">'
                     f'<div class="pane w">{_svg(markup_fn, st, "light", acc, cid + "sw", "lock st")}</div>'
                     f'<div class="pane k">{_svg(markup_fn, st, "dark", acc, cid + "sk", "lock st")}</div></div>')
        t1 = (f'<div class="tile"><p class="label">Mark, 128px</p><div class="stage">'
              f'{_svg(markup_fn, icon, "light", acc, cid + "m128", "m128")}</div></div>')
        t2 = (f'<div class="tile"><p class="label">Favicon, 16px and 32px</p><div class="stage tabs">'
              f'<div class="tab">{_svg(markup_fn, icon, "light", acc, cid + "t1", "m16")}<span>userandproduct</span></div>'
              f'<div class="tab k">{_svg(markup_fn, icon, "dark", acc, cid + "t2", "m16")}<span>userandproduct</span></div>'
              f'<div class="big">{_svg(markup_fn, icon, "light", acc, cid + "f32", "m32")}'
              f'{_svg(markup_fn, icon, "light", acc, cid + "f16", "m16")}</div></div></div>')
        t3 = (f'<div class="tile"><p class="label">Single colour</p><div class="stage" style="color:{ink["light"]}">'
              f'{_svg(markup_fn, lock, "mono", acc, cid + "mono", "monolock")}</div></div>')
        t4 = (f'<div class="tile"><p class="label">Mark in the accent</p><div class="stage" style="color:{A["light"]}">'
              f'{_svg(markup_fn, icon, "mono", acc, cid + "acc", "m128")}</div></div>')
        flist = ", ".join(f'<a href="{html.escape(files[k])}">{html.escape(files[k])}</a>'
                          for k in sorted(files) if k[1] == "light")
        parts.append(
            f'<section class="c" id="{cid}"><div class="head"><h2>{c["id"]}. {html.escape(c["name"])}</h2>'
            f'<span class="tag">{html.escape(c["category"])}</span>'
            f'<button type="button" data-pin="{cid}" aria-pressed="false">Pin to compare</button></div>'
            f'<p class="why">{html.escape(c["rationale"])}</p>'
            f'<p class="meta"><span class="sw"><i style="background:{A["light"]}"></i>Accent: {A["name"]} '
            f'{A["light"]} (on near-black {A["dark"]}).</span> {html.escape(c["icon_note"])} Files: {flist}, '
            f'each also as -dark and -mono.</p>'
            f'{pair}<div class="tiles">{t1}{t2}{t3}{t4}</div></section>')

    acc_html = "<br>".join(f'<span class="sw"><i style="background:{a["light"]}"></i>{a["name"]}: '
                           f'{a["light"]} on white, {a["dark"]} on near-black</span>' for a in accents.values())
    page = f"""<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Logo Concepts, Round 1</title>
<meta name="color-scheme" content="light dark">
<style>{CSS}</style>
</head>
<body>
<header class="top"><div class="wrap"><strong>userandproduct logos</strong>
<nav class="jump" aria-label="Concepts">{"".join(jumps)}</nav>
<div class="cmp"><span>Pinned: <b id="count">0</b></span><button type="button" id="clear">Clear</button></div>
</div></header>
<main class="wrap">
<h1>Logo concepts, round 1</h1>
<p class="lede">Twelve directions for userandproduct (one word, as the domain), 9 October 2026. A to G
came first; H to L each start from a different root: typography history, the user's eye, evidence,
architecture and the printed page. Every letter is drawn as a path on one geometric grid; a final
typeface can replace it later. Card view with size ramps: <a href="preview.html">preview.html</a>.</p>
<div class="notes"><div><h3>Accents</h3><p>{acc_html}</p><p>Text is #0A0A0C on white and #F4F4F5 on
near-black. Each concept uses one accent only.</p></div>
<div><h3>How to choose</h3><ol>
<li>Put the header lockup on the article mockup at 32 to 40px tall, in light and dark. It should look like
a publication, not a startup.</li>
<li>Try the mark as a LinkedIn avatar, a 64px circle crop next to your name.</li>
<li>Find the 16px tab among your real open tabs. If it takes more than a second, it fails.</li>
<li>Check the single-colour version: one-colour print, a book spine, a stamp.</li>
</ol></div></div>
{"".join(parts)}
</main>
<div class="tray" id="tray" aria-live="polite"><div class="wrap"><div class="row" id="trayrow"></div></div></div>
<script>{JS}</script>
</body>
</html>
"""
    with open(os.path.join(out, "index.html"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(page)
