"""Write the round-1 board, ../index.html, from ideas.py and the files build.py made."""

from html import escape as e

NOT_AGAIN = [
    ("Thin lines and scattered small parts", "hairline cords, rings on legs, dots on stalks (round 5's plumb line, chandelier, ring on three legs)."),
    ("One-colour cut-outs with no depth", "a figure punched through a flat disc or block (round 6's hollowed discs, round 1's imprint, round 4's sliced disc and quarter cut)."),
    ("Abstract geometry with no readable idea", "tiles, triangles, tripods and trees of three (rounds 5 and 7, including the current four-tile mark)."),
    ("Architecture metaphors", "plinths, keystones, stylobates, cornerstones, stairs, lecterns (rounds 1 to 3)."),
    ("Letterforms and monograms", "the UP shared stem, the cradle U, serif and grotesque monograms, the et ampersand: they move to round 2, a letterform round of its own."),
    ("Circle-and-square pairs", "round 1's 'where they meet' and round 4's square and disc; nothing here is a plain circle beside a plain square."),
    ("Rim-breaking tiles and profiles", "round 7's 'one breaks the rim' and the shortlist's profile and sphere; the one breakout here is a rocket, not a tile or a head."),
    ("The stock reference itself", "no cursor, no arrow in a ring; only its qualities are kept: mass, one idea, a lighter fold where two forms overlap."),
]


def img(src, w, h, alt, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<img src="{src}" width="{w}" height="{h}" alt="{e(alt)}"{c} loading="lazy" decoding="async">'


def idea_block(i, idea, tile):
    slug = f"r1-{i:02d}"
    num = f"R1-{i:02d}"
    name = idea["name"]
    led = "Stands free" if idea["container"] == "free" else f"Container-led: {idea['container']}"
    fam = idea.get("family")
    colour = "Blue: signal #2B46A0 with a pale fold" + (f"; alternative shown in {fam}" if fam else "")
    av = lambda pre, shape, theme: img(f"png/{slug}{pre}-avatar-{shape}-{theme}-110.png", 110, 110,
                                       f"{name}, {'circle' if shape == 'circle' else 'rounded square'} avatar on {theme}")
    row1 = f"""
      <div class="test">
        <figure class="pan pan--l"><div class="pair">{av('', 'circle', 'light')}{av('', 'square', 'light')}</div><figcaption>110 px circle and rounded square, light</figcaption></figure>
        <figure class="pan pan--d"><div class="pair">{av('', 'circle', 'dark')}{av('', 'square', 'dark')}</div><figcaption>110 px circle and rounded square, dark</figcaption></figure>
        <figure class="pan pan--l pan--fav"><div class="pair">{img(f'png/{slug}-favicon-light-32.png', 32, 32, f'{name} favicon, light')}</div><figcaption>32 px</figcaption></figure>
        <figure class="pan pan--d pan--fav"><div class="pair">{img(f'png/{slug}-favicon-dark-32.png', 32, 32, f'{name} favicon, dark')}</div><figcaption>32 px</figcaption></figure>
      </div>"""
    row2 = f"""
      <div class="row2">
        <figure class="pan pan--l"><div class="big">{img(f'svg/{slug}-mark-light.svg', 160, 160, f'{name} mark on white')}</div><figcaption>Mark, 160 px</figcaption></figure>
        <figure class="pan pan--d"><div class="big">{img(f'svg/{slug}-mark-dark.svg', 160, 160, f'{name} mark on near-black')}</div><figcaption>Mark, 160 px</figcaption></figure>
        <figure class="pan pan--thumb"><div>{img(f'png/{slug}-thumb-600.png', 600, 338, f'{name} lockup, 120 px wide, on a {tile} thumbnail', 'thumb')}</div><figcaption>Thumb lockup, 120 px in a 600 x 338 tile</figcaption></figure>
      </div>
      <div class="heads">
        <figure class="pan pan--l"><div class="head">{img(f'svg/{slug}-lockup-light.svg', 236, 30, f'{name} header lockup on white')}</div><figcaption>Header lockup, 236 px</figcaption></figure>
        <figure class="pan pan--d"><div class="head">{img(f'svg/{slug}-lockup-dark.svg', 236, 30, f'{name} header lockup on near-black')}</div><figcaption>Header lockup, 236 px</figcaption></figure>
      </div>"""
    alt = ""
    if fam:
        alt = f"""
      <div class="alt">
        <p class="alt__h">Alternative colour: {e(fam)}</p>
        <div class="test">
          <figure class="pan pan--l"><div class="pair">{av('-alt', 'circle', 'light')}{av('-alt', 'square', 'light')}</div><figcaption>110 px, light</figcaption></figure>
          <figure class="pan pan--d"><div class="pair">{av('-alt', 'circle', 'dark')}{av('-alt', 'square', 'dark')}</div><figcaption>110 px, dark</figcaption></figure>
          <figure class="pan pan--l pan--fav"><div class="pair">{img(f'png/{slug}-alt-favicon-light-32.png', 32, 32, f'{name} favicon in {fam}, light')}</div><figcaption>32 px</figcaption></figure>
          <figure class="pan pan--d pan--fav"><div class="pair">{img(f'png/{slug}-alt-favicon-dark-32.png', 32, 32, f'{name} favicon in {fam}, dark')}</div><figcaption>32 px</figcaption></figure>
        </div>
      </div>"""
    return f"""
    <article class="idea" id="{slug}">
      <header class="idea__h">
        <p class="idea__n">{num}</p>
        <h2>{e(name)}</h2>
        <p class="idea__k">{e(idea['kind'])} · <span class="tag">{e(led)}</span></p>
      </header>{row1}{row2}{alt}
      <dl class="notes">
        <div><dt>Idea</dt><dd>{e(idea['idea'])}</dd></div>
        <div><dt>Oh nice</dt><dd>{e(idea['nice'])}</dd></div>
        <div><dt>Construction</dt><dd>{e(idea['build'])}</dd></div>
        <div><dt>Authority check</dt><dd>{e(idea['authority'])}</dd></div>
        <div><dt>Colour</dt><dd>{e(colour)}</dd></div>
      </dl>
    </article>"""


CSS = """
.wrap{max-width:1180px;margin:0 auto;padding:0 var(--gutter)}
.top{display:flex;justify-content:space-between;align-items:center;gap:16px;padding:20px 0;border-bottom:1px solid var(--rule)}
.top a{font:600 var(--fs-ui)/1.2 var(--font-ui)}
.toggle{border:1px solid var(--rule);background:var(--panel);border-radius:999px;padding:6px 14px;cursor:pointer;font:500 14px/1 var(--font-ui)}
.intro{padding:48px 0 24px}
.intro h1{font-size:clamp(34px,6vw,56px);line-height:1.02;letter-spacing:-.02em;margin-bottom:16px}
.intro .lede{font-size:var(--fs-lead);color:var(--ink-2);max-width:62ch}
.found{margin:24px 0 0;padding:16px 20px;border-left:4px solid var(--signal);background:var(--signal-wash);max-width:70ch}
.cols{display:grid;gap:32px;grid-template-columns:1fr;padding:24px 0 8px}
@media (min-width:900px){.cols{grid-template-columns:1.2fr 1fr}}
.cols h2{font-size:var(--fs-h3);margin-bottom:10px}
.cols ul{margin:0;padding-left:20px;font-size:16px;color:var(--ink-2)}
.cols li{margin:0 0 6px}
.cols li b{color:var(--ink)}
.jump{display:flex;flex-wrap:wrap;gap:8px;padding:16px 0 8px;margin:0;list-style:none}
.jump a{display:inline-block;padding:6px 10px;border:1px solid var(--rule);border-radius:999px;font:500 14px/1 var(--font-ui);text-decoration:none;color:var(--ink)}
.idea{padding:40px 0;border-top:2px solid var(--rule-strong)}
.idea__h{margin-bottom:18px}
.idea__n{font:600 14px/1 var(--font-ui);color:var(--ink-3);letter-spacing:.06em}
.idea__h h2{font-size:var(--fs-h2);margin:6px 0 4px}
.idea__k{color:var(--ink-3);font-size:15px}
.tag{color:var(--ink);font-weight:600}
figure{margin:0}
figcaption{font:400 13px/1.3 var(--font-ui);color:var(--ink-3);margin-top:8px}
.pan{border:1px solid var(--rule);border-radius:10px;padding:16px}
.pan--l{background:#FFFFFF}
.pan--d{background:#0B0B0C;border-color:#26262B}
.pan--l figcaption{color:#62626A}
.pan--d figcaption{color:#A09E97}
.test{display:flex;flex-wrap:wrap;gap:12px}
.test .pan{flex:1 1 auto}
.pair{display:flex;flex-wrap:wrap;gap:16px;align-items:center;min-height:110px}
.pair img{display:block;flex:none}
.pan--fav .pair{justify-content:center;min-width:64px}
.row2{display:flex;flex-wrap:wrap;gap:12px;margin-top:12px;align-items:flex-start}
.row2 .pan--thumb{flex:1 1 320px;border:0;padding:0;min-width:0}
.big img{display:block;width:160px;height:160px;max-width:none}
.thumb{display:block;width:100%;max-width:600px;height:auto;border-radius:8px}
.heads{display:grid;gap:12px;margin-top:12px;grid-template-columns:1fr}
@media (min-width:700px){.heads{grid-template-columns:1fr 1fr}}
.head img{display:block;width:236px;height:auto}
.alt{margin-top:16px}
.alt__h{font:600 14px/1 var(--font-ui);margin-bottom:8px}
.notes{display:grid;gap:10px 28px;margin:20px 0 0;grid-template-columns:1fr}
@media (min-width:900px){.notes{grid-template-columns:1fr 1fr}}
.notes div{border-top:1px solid var(--rule);padding-top:8px}
.notes dt{font:600 13px/1.2 var(--font-ui);text-transform:uppercase;letter-spacing:.06em;color:var(--ink-3)}
.notes dd{margin:4px 0 0;font-size:16px;line-height:1.5}
.near{padding:40px 0 64px;border-top:2px solid var(--rule-strong)}
.near h2{font-size:var(--fs-h2);margin-bottom:8px}
.near p{color:var(--ink-2);max-width:70ch;margin-bottom:16px}
.near ol{margin:0;padding-left:24px}
.near li{margin:0 0 8px}
"""


def write(round_dir, ideas, tiles):
    freeones = [f"R1-{i:02d}" for i, x in enumerate(ideas, 1) if x["container"] == "free"]
    boxed = [f"R1-{i:02d}" for i, x in enumerate(ideas, 1) if x["container"] != "free"]
    blocks = "".join(idea_block(i, x, tiles[i - 1]) for i, x in enumerate(ideas, 1))
    jump = "".join(f'<li><a href="#r1-{i:02d}">R1-{i:02d} {e(x["name"])}</a></li>' for i, x in enumerate(ideas, 1))
    nota = "".join(f"<li><b>{e(a)}</b>: {e(b)}</li>" for a, b in NOT_AGAIN)
    near = "".join(f'<li><a href="#r1-{i:02d}">R1-{i:02d} {e(x["name"])}</a>: {e(x["near"])}</li>' for i, x in enumerate(ideas, 1))
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Logo Round One</title>
<meta name="description" content="Logo exploration 2, round 1: ten marks with mass, one idea and a two-tone fold, judged first as avatars and favicons.">
<link rel="stylesheet" href="../../mockup.css">
<style>{CSS}</style>
</head>
<body>
<a class="skip" href="#main">Skip to the ideas</a>
<div class="wrap">
  <nav class="top" aria-label="Exploration"><a href="../hub.html">Logo exploration 2: all rounds</a><button class="toggle" type="button" data-theme-toggle>Theme</button></nav>
  <main id="main">
    <header class="intro">
      <h1>Round 1: ten marks with weight</h1>
      <p class="lede">Ten ideas for userandproduct, 10 October 2026. Each one is judged first where the current mark failed: as a 110 px avatar in a circle and in a rounded square, and as a 32 px favicon, on white and on near-black. Then the mark at 160 px, the lockup on a thumbnail and in the header.</p>
      <p class="found"><b>Foundation:</b> authority and trust first. Every mark may have character, mass and an app-icon feel, but it must read as a serious publication a professional would cite: steady geometry, confident weight, two restrained tones, no faces, no squiggles, no splash gradients.</p>
    </header>
    <section class="cols" aria-label="Brief and fresh start">
      <div>
        <h2>What we are not doing again</h2>
        <ul>{nota}</ul>
        <p><a href="../../logos/hub.html">The old exploration, rounds 1 to 7, for reference</a></p>
      </div>
      <div>
        <h2>How to read this board</h2>
        <ul>
          <li><b>Container-led</b> ({len(boxed)}): {", ".join(boxed)}. The filled circle or rounded square is part of the mark; the avatar crop is the container.</li>
          <li><b>Stand free</b> ({len(freeones)}): {", ".join(freeones)}. Kept so you can compare; their avatar is the mark on the page colour.</li>
          <li><b>Colour</b>: signal blue #2B46A0 with a pale fold (#A9BBFF) and a mid fold (#5A7BF0). R1-02 is also shown in coral, R1-07 in teal and R1-08 in oxblood.</li>
          <li><b>Lockups</b> keep the current Inter Display Bold wordmark, so the marks compare fairly. Letterforms and monograms are round 2.</li>
          <li>Avatars and favicons are real PNG renders at the stated size, shown at one to one.</li>
        </ul>
      </div>
    </section>
    <ul class="jump" aria-label="Jump to an idea">{jump}</ul>
    {blocks}
    <section class="near" id="neighbourhood">
      <h2>Closest existing logos in this visual family</h2>
      <p>Named from memory, to show the neighbourhood; the proper check, looking at the logos side by side, happens on the shortlist. Rockets are a crowded field, so both rocket ideas list the nearest rocket marks.</p>
      <ol>{near}</ol>
    </section>
  </main>
</div>
<script src="../../mockup.js"></script>
</body>
</html>
"""
    (round_dir / "index.html").write_text(html, encoding="utf-8")
