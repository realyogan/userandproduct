"""Build the typeface board for the "userandproduct" wordmark.

For each candidate font this writes, into research/mockups/logos/typeboard/:
    <slug>.svg          one colour (currentColor), bold, all one path
    <slug>-light.svg    #111111 ink, "and" in the lighter weight and the red accent
    <slug>-dark.svg     #F2F2F2 ink, "and" in the lighter weight and a lighter red
    <slug>-split.svg    currentColor, "and" in the lighter weight, three paths with classes
    <slug>-upper.svg    USERANDPRODUCT, bold, currentColor
    <slug>-tracked.svg  userandproduct, bold, +60/1000 em tracking, currentColor
and then index.html, which inlines them so CSS can colour the "and" part.

Usage (from anywhere):
    python build_typeboard.py
"""

import re
import sys
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import wordmark  # noqa: E402

MOCKUPS = HERE.parent
FONTS = MOCKUPS / "fonts"
OUT = MOCKUPS / "logos" / "typeboard"

RED, BLUE = "#B3141C", "#1F3FBF"
RED_DARK, BLUE_DARK = "#F0676C", "#8EA2FF"  # lifted for contrast on near-black

CANDIDATES = [
    {
        "slug": "geist", "name": "Geist", "bold": "geist/Geist-Bold.ttf",
        "light": "geist/Geist-Regular.ttf", "weights": "Bold 700, and in Regular 400",
        "licence": "OFL 1.1", "licence_file": "geist/OFL.txt",
        "source": "https://github.com/vercel/geist-font/releases/tag/v1.7.2",
        "source_label": "vercel/geist-font v1.7.2",
        "character": "Swiss-style neo-grotesque; cool, exact, technical. Reads as a modern software company.",
    },
    {
        "slug": "inter-display", "name": "Inter Display", "bold": "inter/InterDisplay-Bold.ttf",
        "light": "inter/InterDisplay-Regular.ttf", "weights": "Bold 700, and in Regular 400",
        "licence": "OFL 1.1", "licence_file": "inter/LICENSE.txt",
        "source": "https://github.com/rsms/inter/releases/tag/v4.1",
        "source_label": "rsms/inter v4.1",
        "character": "Neutral workhorse grotesque, tightened for big sizes; calm and familiar, the voice of product UI.",
    },
    {
        "slug": "space-grotesk", "name": "Space Grotesk", "bold": "space-grotesk/SpaceGrotesk-Bold.ttf",
        "light": "space-grotesk/SpaceGrotesk-Regular.ttf", "weights": "Bold 700, and in Regular 400",
        "licence": "OFL 1.1", "licence_file": "space-grotesk/OFL.txt",
        "source": "https://github.com/floriankarsten/space-grotesk/releases/tag/2.0.0",
        "source_label": "floriankarsten/space-grotesk 2.0.0",
        "character": "Quirky geometric grotesque born from a monospace; techy, a little playful, very recognizable.",
    },
    {
        "slug": "instrument-sans", "name": "Instrument Sans", "bold": "instrument-sans/InstrumentSans-Bold.ttf",
        "light": "instrument-sans/InstrumentSans-Regular.ttf", "weights": "Bold 700, and in Regular 400",
        "licence": "OFL 1.1", "licence_file": "instrument-sans/OFL.txt",
        "source": "https://github.com/Instrument/instrument-sans/tree/master/fonts/ttf",
        "source_label": "Instrument/instrument-sans (fonts/ttf)",
        "character": "Compact contemporary grotesque with crisp, slightly narrow letters; editorial and precise.",
    },
    {
        "slug": "fraunces", "name": "Fraunces 72pt", "bold": "fraunces/Fraunces72pt-SemiBold.ttf",
        "light": "fraunces/Fraunces72pt-Regular.ttf", "weights": "SemiBold 600, and in Regular 400",
        "licence": "OFL 1.1", "licence_file": "fraunces/OFL.txt",
        "source": "https://github.com/undercasetype/Fraunces/releases/tag/1.000",
        "source_label": "undercasetype/Fraunces 1.000 (static, 72pt optical size)",
        "character": "Soft old-style display serif with a slight wobble; warm, bookish, literary. The serif for contrast.",
    },
    {
        "slug": "bricolage-grotesque", "name": "Bricolage Grotesque", "bold": "bricolage-grotesque/BricolageGrotesque-Bold.ttf",
        "light": "bricolage-grotesque/BricolageGrotesque-Regular.ttf", "weights": "Bold 700, and in Regular 400",
        "licence": "OFL 1.1", "licence_file": "bricolage-grotesque/OFL.txt",
        "source": "https://github.com/ateliertriay/bricolage/tree/main/fonts/ttf",
        "source_label": "ateliertriay/bricolage (fonts/ttf)",
        "character": "French-flavoured grotesque with ink traps and a big x-height; confident, characterful, opinionated.",
    },
]


def make(font, out, **kw):
    """Run wordmark.build with defaults and write the SVG; return its text."""
    args = SimpleNamespace(font=str(FONTS / font), text="", out=str(out), size=100,
                           tracking=0, split="", highlight="", alt_font="",
                           fill="currentColor", accent="", id_prefix="wm-", margin=0.04,
                           merge=False, weight_note=True)
    for k, v in kw.items():
        setattr(args, k, v)
    svg, _, _ = wordmark.build(args)
    Path(out).write_text(svg, encoding="utf-8")
    return svg


def inline(svg, cls, label=None):
    """Prepare an SVG for inlining: drop the comment, ids and title; add a class."""
    svg = re.sub(r"<!--.*?-->\n?", "", svg, flags=re.S)
    svg = re.sub(r'\sid="[^"]*"', "", svg)
    svg = re.sub(r"<title>.*?</title>\n?", "", svg)
    svg = svg.replace("<svg ", f'<svg class="{cls}" ', 1)
    if label:
        svg = re.sub(r'aria-label="[^"]*"', f'aria-label="{label}"', svg, count=1)
    return svg.strip()


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace('"', "&quot;")


def section(c, svgs):
    """Return the HTML for one font."""
    s = c["slug"]
    split = svgs["split"]
    files = " ".join(
        f'<a href="{s}{suffix}.svg">{s}{suffix}.svg</a>'
        for suffix in ("", "-light", "-dark", "-split", "-upper", "-tracked"))
    return f"""
<section class="font" id="{s}">
  <header class="font-head">
    <h2>{esc(c['name'])}</h2>
    <p class="meta"><span>{esc(c['weights'])}</span> <span><a href="../../fonts/{c['licence_file']}">{c['licence']}</a></span>
      <span>Source: <a href="{c['source']}">{esc(c['source_label'])}</a></span></p>
    <p class="character">{esc(c['character'])}</p>
  </header>
  <div class="pair">
    <figure class="panel on-white">{inline(split, 'wm wm-560 and-light')}<figcaption>On white, 560 px wide; "and" in the lighter weight</figcaption></figure>
    <figure class="panel on-black">{inline(split, 'wm wm-560 and-light')}<figcaption>On near-black, 560 px wide</figcaption></figure>
  </div>
  <div class="accents">
    <figure class="panel on-white small">{inline(split, 'wm wm-260 and-red')}<figcaption>Red accent {RED}</figcaption></figure>
    <figure class="panel on-white small">{inline(split, 'wm wm-260 and-blue')}<figcaption>Blue accent {BLUE}</figcaption></figure>
    <figure class="panel on-black small">{inline(split, 'wm wm-260 and-red')}<figcaption>Red on dark {RED_DARK}</figcaption></figure>
    <figure class="panel on-black small">{inline(split, 'wm wm-260 and-blue')}<figcaption>Blue on dark {BLUE_DARK}</figcaption></figure>
  </div>
  <div class="sizes">
    <figure class="panel on-white small"><div class="ramp">{inline(split, 'wm h32 and-red')}{inline(split, 'wm h16 and-red')}</div><figcaption>Header size: 32 px and 16 px tall</figcaption></figure>
    <figure class="panel on-black small"><div class="ramp">{inline(split, 'wm h32 and-red')}{inline(split, 'wm h16 and-red')}</div><figcaption>32 px and 16 px on dark</figcaption></figure>
    <figure class="panel on-white small">{inline(svgs['upper'], 'wm wm-420')}<figcaption>Uppercase, bold</figcaption></figure>
    <figure class="panel on-white small">{inline(svgs['tracked'], 'wm wm-420')}<figcaption>Tracked +60/1000 em, bold</figcaption></figure>
  </div>
  <p class="files">Files: {files}</p>
</section>"""


CSS = """
:root{--bg:#f6f5f2;--fg:#141414;--muted:#5b5b5b;--rule:#dddad3;--card:#ffffff;--link:#1F3FBF;
--ink:#111111;--paper:#ffffff;--night:#121212;--night-ink:#F2F2F2;color-scheme:light dark}
@media (prefers-color-scheme:dark){:root{--bg:#0d0d0d;--fg:#ececec;--muted:#a3a3a3;--rule:#2a2a2a;--card:#171717;--link:#8EA2FF}}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
a{color:var(--link)}
.wrap{max-width:1400px;margin:0 auto;padding:32px 24px 64px}
h1{font-size:clamp(28px,4vw,44px);line-height:1.1;margin:0 0 12px;letter-spacing:-.01em}
.intro{max-width:72ch;color:var(--muted);margin:0 0 8px}
nav.toc{display:flex;flex-wrap:wrap;gap:8px 16px;margin:20px 0 8px;padding:12px 0;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule)}
.font{border-bottom:1px solid var(--rule);padding:40px 0}
.font-head h2{font-size:26px;margin:0 0 4px}
.meta{display:flex;flex-wrap:wrap;gap:4px 18px;margin:0;color:var(--muted);font-size:14px}
.character{margin:6px 0 18px;max-width:80ch}
figure{margin:0}
.panel{border:1px solid var(--rule);border-radius:6px;padding:40px 24px 14px;display:flex;flex-direction:column;align-items:center;gap:20px;min-width:0}
.panel.small{padding:24px 16px 12px;gap:14px;justify-content:space-between}
.on-white{background:var(--paper);color:var(--ink)}
.on-black{background:var(--night);color:var(--night-ink);border-color:#2a2a2a}
figcaption{font-size:12.5px;color:#6b6b6b;align-self:flex-start}
.on-black figcaption{color:#9a9a9a}
.pair{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
.accents,.sizes{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;margin-top:16px}
.wm{display:block;height:auto;max-width:100%}
.wm-560{width:560px}.wm-420{width:420px}.wm-260{width:260px}
.h32{height:32px;width:auto}.h16{height:16px;width:auto}
.ramp{display:flex;flex-direction:column;align-items:flex-start;gap:14px;width:100%}

.on-white .and-red .wm-and{fill:#B3141C}.on-white .and-blue .wm-and{fill:#1F3FBF}
.on-black .and-red .wm-and{fill:#F0676C}.on-black .and-blue .wm-and{fill:#8EA2FF}
.files{font-size:12.5px;color:var(--muted);margin:14px 0 0;overflow-wrap:anywhere}
.files a{margin-right:10px}
.note{font-size:14px;color:var(--muted);max-width:80ch}
@media (max-width:1100px){.accents,.sizes{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:760px){.pair,.accents,.sizes{grid-template-columns:minmax(0,1fr)}.wrap{padding:24px 16px 48px}.panel{padding:28px 14px 12px}}
"""


def main():
    """Generate all SVGs and index.html."""
    OUT.mkdir(parents=True, exist_ok=True)
    sections = []
    for c in CANDIDATES:
        s, bold, light = c["slug"], c["bold"], c["light"]
        svgs = {
            "mono": make(bold, OUT / f"{s}.svg", text="userandproduct"),
            "light": make(bold, OUT / f"{s}-light.svg", split="user|and|product", highlight="and",
                          alt_font=str(FONTS / light), fill="#111111", accent=RED, id_prefix=f"{s}-"),
            "dark": make(bold, OUT / f"{s}-dark.svg", split="user|and|product", highlight="and",
                         alt_font=str(FONTS / light), fill="#F2F2F2", accent=RED_DARK, id_prefix=f"{s}-"),
            "split": make(bold, OUT / f"{s}-split.svg", split="user|and|product", highlight="and",
                          alt_font=str(FONTS / light), id_prefix=f"{s}-"),
            "upper": make(bold, OUT / f"{s}-upper.svg", text="USERANDPRODUCT"),
            "tracked": make(bold, OUT / f"{s}-tracked.svg", text="userandproduct", tracking=60),
        }
        sections.append(section(c, svgs))
        print(f"{c['name']}: 6 SVGs")

    toc = " ".join(f'<a href="#{c["slug"]}">{esc(c["name"])}</a>' for c in CANDIDATES)
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Wordmark type board</title>
<meta name="robots" content="noindex">
<style>{CSS}</style>
</head>
<body>
<main class="wrap">
  <h1>userandproduct: type board</h1>
  <p class="intro">Six open-licence typefaces setting the one-word name. Every word on this page is a real
  font outline turned into an SVG path by <code>tools/wordmark.py</code> (shaped with HarfBuzz, so the
  font's own kerning applies). The big pair shows "and" in the lighter weight of the same family; the small
  row tries the red and blue accents. Look at the 16 px line first: a wordmark that falls apart there is out.</p>
  <p class="note">All six are under the SIL Open Font License 1.1, which allows logos made from the outlines.
  An outlined font is not exclusive, so the chosen face still needs a few custom touches. Fonts and licence
  files are in <a href="../../fonts/">research/mockups/fonts/</a>. Rebuild with
  <code>python research/mockups/tools/build_typeboard.py</code>. The dark-mode accents are lifted
  ({RED_DARK} and {BLUE_DARK}) because {RED} and {BLUE} are too dark to read on near-black.</p>
  <nav class="toc" aria-label="Typefaces">{toc}</nav>
  {''.join(sections)}
</main>
</body>
</html>
"""
    (OUT / "index.html").write_text(html, encoding="utf-8")
    print(f"wrote {OUT / 'index.html'}")


if __name__ == "__main__":
    main()
