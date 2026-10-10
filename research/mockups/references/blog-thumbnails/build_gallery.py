"""Render the eleven thumbnail styles on sample subjects from our field and write gallery.html.
Run: python research/mockups/references/blog-thumbnails/build_gallery.py
Writes gallery/<style>-<slug>-hero.png, -thumb.png, .svg, -check-300.png, gallery/checks.json and gallery.html.
The samples do not touch the generator's history file. The photo sample (style 11) is a screenshot of the owner's
own Printables site, saved as gallery/sample-photo-printables-sheet.png; it stands in until the owner supplies a
real photo."""
import json
import sys
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools"))
from thumbnail import (BACKGROUNDS, KINDS_OF_ARTICLE, ROTATION, STYLES, contrast, make,  # noqa: E402
                       suitable_styles)

OUT = HERE / "gallery"
PHOTO = OUT / "sample-photo-printables-sheet.png"

# (style, slug, title, subject, extra spec, the subject in words, reference images that belong to the style)
SAMPLES = [
    (1, "how-to-write-a-prd-engineers-read", "How to Write a PRD That Engineers Actually Read", "prd",
     {"palette": "red-orange", "scheme": "duo"}, "a PRD", "ref-10, 17, 18, 19, 20, 21, 22, 23, 29, 30"),
    (2, "run-a-usability-test-in-a-week", "Run a Usability Test in a Week", "usability-test",
     {"palette": "acid-yellow", "scheme": "mono"}, "a usability test", "ref-10, 17, 18, 19, 20, 21, 22, 23, 29, 30"),
    (3, "roadmap-template", "A Roadmap Template Without Dates", "roadmap",
     {"palette": "teal", "scheme": "duo"}, "a roadmap", "ref-05, 12, 14, 15, 16"),
    (4, "write-a-research-plan", "How to Write a Research Plan", "research-plan",
     {"palette": "tangerine", "scheme": "duo", "focus": 2}, "a research plan", "ref-24, 25, 28"),
    (5, "personas-that-earn-their-keep", "Why Most Personas Fail", "persona",
     {"palette": "violet", "scheme": "duo", "cover_title": "Personas that earn their keep"}, "a persona",
     "ref-02, 04, 07, 08"),
    (6, "read-a-retention-chart", "Reading a Retention Chart", "retention-chart",
     {"palette": "night-plum", "scheme": "duo"}, "a retention chart", "ref-03, 27, 35"),
    (7, "the-prioritization-matrix", "The Prioritization Matrix, Explained", "prioritization-matrix",
     {"palette": "midnight", "scheme": "duo"}, "a prioritization matrix", "ref-32, 33, 34"),
    (8, "design-system-vs-style-guide", "Design System vs Style Guide", "design-system",
     {"palette": "paper", "scheme": "trio"}, "a design system (two things compared)", "ref-31"),
    (9, "a-hiring-guide-for-designers", "What Hiring Looks Like at Scale", "hiring-guide",
     {"palette": "night", "scheme": "duo"}, "a hiring guide", "ref-07"),
    (10, "conversion-funnel-benchmarks", "Conversion Funnel Benchmarks", "icon:funnel",
     {"palette": "electric-blue", "scheme": "duo", "kind": "data"}, "a conversion funnel", "ref-07 (bright)"),
    (11, "plan-a-two-week-sprint", "How We Plan a Two-Week Sprint", "sprint",
     {"palette": "hot-pink", "scheme": "mono", "photo": str(PHOTO)}, "a sprint (the photo: a calendar sheet)",
     "ref-01, 04, 06, 09, 11, 13"),
]


def build():
    OUT.mkdir(exist_ok=True)
    for old in OUT.glob("style-*"):
        old.unlink()
    results = []
    for i, (st, slug, title, subject, extra, words, refs) in enumerate(SAMPLES):
        spec = {"slug": slug, "title": title, "subject": subject, "index": i, **extra}
        if st != 11:
            spec.update(style=st, reason="gallery sample: one of each style")
        r = make(spec, OUT, name=f"style-{st:02d}-{slug}", history=False)
        r.update(words=words, refs=refs, slug=slug, title=title)
        results.append(r)
        print(st, r["style"], r["kind"], r["palette"], r["scheme"], r["accent_names"], r["corner"],
              "pass" if r["checks"]["pass"] else "CHECK", r["checks"]["read_300"], r["notes"])
    (OUT / "checks.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
    return results


CSS = """
@font-face { font-family: "Inter"; src: url("../../fonts/inter/Inter-Regular.woff2") format("woff2"); font-weight: 400; font-display: swap; }
@font-face { font-family: "Inter"; src: url("../../fonts/inter/Inter-SemiBold.woff2") format("woff2"); font-weight: 600; font-display: swap; }
@font-face { font-family: "Space Grotesk"; src: url("../../fonts/space-grotesk/SpaceGrotesk-Bold.ttf") format("truetype"); font-weight: 700; font-display: swap; }
:root {
  --paper: #FDFCF8; --ink: #1D1B16; --muted: #5F5B52; --rule: #E2DDD1; --panel: #F4F1E8;
  --link: #174FA1; --focus: #174FA1; --pass: #245A18; --warn: #8E1430;
  color-scheme: light;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --paper: #1D1B16; --ink: #F1EEE6; --muted: #B3AD9F; --rule: #3A372F; --panel: #26241E;
    --link: #9EC2F5; --focus: #9EC2F5; --pass: #B8EBAE; --warn: #FFB8C7;
    color-scheme: dark;
  }
}
:root[data-theme="dark"] {
  --paper: #1D1B16; --ink: #F1EEE6; --muted: #B3AD9F; --rule: #3A372F; --panel: #26241E;
  --link: #9EC2F5; --focus: #9EC2F5; --pass: #B8EBAE; --warn: #FFB8C7;
  color-scheme: dark;
}
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }
body { margin: 0; background: var(--paper); color: var(--ink); font: 400 17px/1.6 "Inter", system-ui, sans-serif; }
a { color: var(--link); text-underline-offset: 2px; }
a:focus-visible { outline: 3px solid var(--focus); outline-offset: 3px; border-radius: 3px; }
img { max-width: 100%; height: auto; display: block; }
code { font-size: .92em; overflow-wrap: anywhere; }
.wrap { max-width: 1400px; margin: 0 auto; padding: 0 16px; }
@media (min-width: 720px) { .wrap { padding: 0 40px; } }
h1, h2 { font-family: "Space Grotesk", "Inter", system-ui, sans-serif; font-weight: 700; letter-spacing: -0.02em; line-height: 1.05; }
h1 { font-size: clamp(2.4rem, 6.4vw, 4.6rem); margin: 0 0 .35em; }
h2 { font-size: clamp(1.5rem, 3vw, 2.1rem); margin: 0; }
p { margin: 0 0 .8em; }
.muted { color: var(--muted); }
.top { padding: 56px 0 32px; border-bottom: 1px solid var(--rule); }
.intro { max-width: 70ch; font-size: 1.1rem; }
.rotation { padding: 32px 0; border-bottom: 1px solid var(--rule); }
.rotation h2 { font-size: 1.35rem; margin-bottom: .5em; }
.kinds { list-style: none; margin: 16px 0; padding: 0; display: grid; gap: 8px; grid-template-columns: repeat(auto-fill, minmax(min(100%, 250px), 1fr)); }
.kinds li { padding: 10px 12px; border: 1px solid var(--rule); border-radius: 6px; font-size: .9rem; line-height: 1.35; }
.kinds b { display: block; font-weight: 600; }
.swatches { list-style: none; margin: 16px 0 8px; padding: 0; display: flex; flex-wrap: wrap; gap: 8px; }
.swatches li { display: flex; align-items: center; gap: 8px; padding: 6px 10px 6px 6px; border: 1px solid var(--rule); border-radius: 6px; font-size: .85rem; }
.swatches span { width: 26px; height: 26px; border-radius: 4px; border: 1px solid rgba(127, 127, 127, .35); }
.style { padding: 48px 0 40px; border-bottom: 1px solid var(--rule); scroll-margin-top: 16px; }
.style-head { display: grid; grid-template-columns: auto 1fr; gap: 4px 20px; align-items: start; margin-bottom: 20px; max-width: 900px; }
.num { font-family: "Space Grotesk", "Inter", sans-serif; font-weight: 700; font-size: clamp(3rem, 8vw, 5rem); line-height: .9; min-width: 1.1ch; }
.style-head p { margin: .4em 0 0; }
.meta { font-size: .92rem; color: var(--muted); }
.meta strong { color: var(--ink); font-weight: 600; }
.pair { display: grid; gap: 16px; grid-template-columns: 1fr; }
@media (min-width: 1400px) { .pair { grid-template-columns: repeat(2, minmax(0, 640px)); justify-content: start; } }
.pair figure { margin: 0; }
.stage { padding: 20px; border-radius: 8px; }
.stage.white { background: #FFFFFF; border: 1px solid var(--rule); }
.stage.black { background: #0B0B0C; }
.stage img { width: 600px; border-radius: 6px; }
.pair figcaption { font-size: .85rem; color: var(--muted); margin-top: 6px; }
.checks { font-size: .88rem; margin-top: 12px; color: var(--muted); }
.checks .ok { color: var(--pass); font-weight: 600; }
.checks .no { color: var(--warn); font-weight: 600; }
.note { max-width: 76ch; margin-top: 12px; padding: 12px 16px; border-left: 4px solid var(--rule); background: var(--panel); border-radius: 0 6px 6px 0; font-size: .95rem; }
.closing { padding: 48px 0 80px; }
.closing .prose { max-width: 74ch; }
"""


def colour_line(r):
    if r["accents"]:
        acc = ", ".join(f"accent {n}" for n in r["accent_names"])
        return f"{r['palette']}, {r['scheme']}, {acc}"
    return f"{r['palette']}, mono"


def page(results):
    secs = []
    for r in results:
        st = r["style"]
        name, spec_line = STYLES[st]
        base = f"gallery/{r['name']}"
        c = r["checks"]
        rd = c["read_300"]
        ratios = sorted({t["ratio"] for t in c["texts"]})
        verdict = '<span class="ok">passes</span>' if c["pass"] else '<span class="no">needs a look</span>'
        alt = f"Style {st}, {name}: {r['words']} on {r['palette']}, {r['scheme']} scheme."
        note = ""
        if st == 11:
            note = ('<p class="note">The photo here is a screenshot of the owner\'s own Printables site (a calendar '
                    'sheet on a tile), used because there is no free-to-use photograph on this machine. A real '
                    'thumbnail in this style uses the owner\'s photo of the article\'s subject: a whiteboard, sticky '
                    'notes, a workshop table. The same code turns it into ink dots.</p>')
        secs.append(f"""
<section class="style" id="style-{st}" aria-labelledby="h-{st}">
  <div class="style-head">
    <div class="num" aria-hidden="true">{st}</div>
    <div>
      <h2 id="h-{st}">{escape(name)}</h2>
      <p>{escape(spec_line)}</p>
      <p class="meta"><strong>Sample:</strong> {escape(r['words'])}, for "{escape(r['title'])}" ({escape(KINDS_OF_ARTICLE[r['kind']])})
      &nbsp;|&nbsp; <strong>Colour:</strong> {escape(colour_line(r))}
      &nbsp;|&nbsp; <strong>References:</strong> {escape(r['refs'])}</p>
    </div>
  </div>
  <div class="pair">
    <figure><div class="stage white"><img src="{base}-thumb.png" width="600" height="338" loading="lazy" alt="{escape(alt)} On a white page."></div>
      <figcaption>Thumb, 600 px, on the white page (full lockup, 120 px wide)</figcaption></figure>
    <figure><div class="stage black"><img src="{base}-hero.png" width="600" height="338" loading="lazy" alt="{escape(alt)} On a near-black page."></div>
      <figcaption>Hero shown at 600 px on the near-black page (full lockup, 220 px wide in the 1200 file, {r['corner']} corner)</figcaption></figure>
  </div>
  <p class="checks">Checks: {verdict}. At 300 px the subject covers {rd['coverage'] * 100:.0f}% of the image and its
  strongest pixels reach {rd['subject_contrast_p90']}:1 against the ground; type and lockup contrast
  {", ".join(f"{x}:1" for x in ratios)}.
  Files: <a href="{base}-hero.png">hero 1200</a>, <a href="{base}-thumb.png">thumb 600</a>{f', <a href="{base}.svg">SVG</a>' if r['svg'] else ''},
  <a href="{base}-check-300.png">300 px check</a>.</p>
  {note}
</section>""")
    kinds = "".join(f'<li><b>{escape(v[0].upper() + v[1:])}</b>styles {", ".join(str(x) for x in suitable_styles(k))}</li>'
                    for k, v in KINDS_OF_ARTICLE.items())
    sw = "".join(f'<li><span style="background:{bg}"></span>{n} {bg}</li>' for n, (bg, _) in BACKGROUNDS.items())
    counts = {}
    for r in results:
        counts[r["scheme"]] = counts.get(r["scheme"], 0) + 1
    mix_line = ", ".join(f"{v} {k}" for k, v in sorted(counts.items(), key=lambda x: -x[1]))
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Thumbnail gallery</title>
<meta name="robots" content="noindex">
<style>{CSS}</style>
</head>
<body>
<header class="top"><div class="wrap">
  <p class="muted"><a href="index.html">Thumbnail styles board</a></p>
  <h1>Thumbnail gallery</h1>
  <div class="intro">
    <p>Our eleven thumbnail styles, each drawn by <code>research/mockups/tools/thumbnail.py</code> on a sample subject
    from our field. Ten are made with code alone; the eleventh is used only when the owner supplies a photo. Each image
    has one bold background, one subject and at most one or two accents on the thing that matters. Every image, hero
    and thumb, carries the full lockup at the same share of the width, about a fifth: 220 px wide on the 1200 px
    hero, 120 px wide on the 600 px thumb, so the logo looks the same wherever the image is shown.</p>
    <p class="muted">Contrast and curiosity, not clickbait: a reader scanning a list should stop on it, and the article
    should deliver what it hints at. Colour schemes in this set: {mix_line}.</p>
  </div>
</div></header>
<main>
<section class="rotation" aria-labelledby="h-rot"><div class="wrap">
  <h2 id="h-rot">How a style is chosen</h2>
  <p class="intro">Fit first: the article's kind, read from its title, limits the choice to the styles that suit it.
  The rotation ({", ".join(str(s) for s in ROTATION)}) then runs only among those, skipping the previous piece's style
  and preferring one not used lately. A supplied photo selects style 11. A writer may override with a reason.</p>
  <ul class="kinds">{kinds}</ul>
  <h2>Suggested backgrounds</h2>
  <p class="intro">Suggestions only: any background whose ink passes 4.5:1 is allowed. Accents are computed from
  the background's hue (mono, duo, trio or analogous) and must pass 3:1, or 4.5:1 when they colour type.</p>
  <ul class="swatches">{sw}</ul>
</div></section>
<div class="wrap">{"".join(secs)}</div>
<section class="closing"><div class="wrap"><div class="prose">
  <h2>Rebuild</h2>
  <p><code>python research/mockups/references/blog-thumbnails/build_gallery.py</code> redraws every sample and this
  page. Per article: <code>python research/mockups/tools/thumbnail.py --slug &lt;slug&gt; --title "&lt;title&gt;"
  --subject &lt;key&gt;</code>.</p>
</div></div></section>
</main>
</body>
</html>
"""


if __name__ == "__main__":
    res = build()
    (HERE / "gallery.html").write_text(page(res), encoding="utf-8", newline="\n")
    print("wrote gallery.html")
