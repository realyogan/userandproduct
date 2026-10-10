"""Writes index.html, the "Thumbnail styles" board, from the group data below.
Run: python research/mockups/references/blog-thumbnails/build.py
Demonstrations come from demo/make_demos.py (run that first; it writes demo/times.json)."""
import json
from html import escape
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent

VERDICT = {
    "code": ("Code alone", "v-code"),
    "source": ("Code plus a source image", "v-source"),
    "external": ("External image tool", "v-external"),
}

GROUPS = [
    {
        "id": "flat-vector",
        "name": "Flat vector with hard shadows on a grained grid",
        "refs": [10, 17, 18, 19, 20, 21, 22, 23, 29, 30],
        "note": "ref-18 and ref-19 are the same image.",
        "style": "A saturated flat color (red-orange, acid yellow, teal, violet, near-white) under a fine square grid "
                 "or a dot grid, with film-like grain over everything. One to three simple objects (gears, a "
                 "magnifier, a database drum, a line chart, a chat window, a box robot) drawn as flat shapes with a "
                 "thin black outline and a solid black shadow offset down and to the right, so they look like paper "
                 "cut-outs lifted off the page. A few thin lines run in from the edge to suggest flow. Type is rare: a "
                 "short label on a pale box in a bold mono face. The brand mark appears as an object itself (a white "
                 "disc on the drum, or a logo pair for an integration) rather than in a corner.",
        "use": "Friendly, concrete, a little playful. It says \"here is the idea in one picture\" without "
               "pretending to be data. It suits how-to pieces, concepts, announcements and anything where one "
               "everyday object can stand for the topic: a magnifier for research, a chat box for interviews, a "
               "chart for metrics.",
        "verdict": "code",
        "why": "Every object here is a handful of rectangles, circles and paths. The shadow is the same shape drawn "
               "again in black and shifted; the grid is a loop of lines; the grain is random noise added to the "
               "pixels. All of it is SVG written by hand and rendered with Python. Demonstration (a) proves it on "
               "our yellow tint. The only weak spot is an organic object with character (see the elephant in its "
               "own group).",
        "ours": "Our tint as the field (the article's tint from the rotation), a fine ink grid at 10% and light grain, "
                "objects in card white and highlight A with ink outlines and a solid ink shadow, our mark small in "
                "the bottom-right corner. Objects from our world: a browser window, a cursor, a sticky note, a "
                "roadmap card, a research magnifier, a speech bubble.",
        "confidence": "high",
        "demo": ("demo-a-flat-vector.png", "a",
                 "Demonstration (a): flat vector with hard shadows on the yellow tint with a grained grid. "
                 "A browser window, a cursor and a speech bubble with a check, drawn as hand-written SVG; shadows "
                 "are the same shapes in ink shifted 14 units; grain is noise added in Python.",
                 "about 15 minutes to write"),
    },
    {
        "id": "pixel",
        "name": "Pixel-art icons and panels",
        "refs": [5, 12, 14, 15, 16],
        "style": "Icons built from square pixels on a visible grid: a padlock, a factory, a key, database drums, "
                 "a RAM stick spilling squares into a disk. Outlines are one pixel thick and fills use a checker "
                 "dither for mid-tones. Backgrounds are near-black or a flat red-orange; two of them put a dark "
                 "rounded panel on the color, like a game screen. Type, when present, is a pixel font in capitals. "
                 "One accent color (acid yellow) at most. No brand mark.",
        "use": "Technical, nostalgic, systematic. It reads as \"this is about how the machine works\". It suits "
               "short, tactical pieces, tool and calculator pages, checklists and anything process-like where an "
               "arrow between two icons tells the story.",
        "verdict": "code",
        "why": "Pixel art is a grid of squares, which is the easiest thing in the world to write as code: each icon "
               "is a small text map of filled and empty cells. Dithered fills are a checker pattern. Demonstration "
               "(b) is a person, a product window and two arrows (a feedback loop) on our teal tint.",
        "ours": "On our tint with the Printables dot grid (not on black), ink outlines, a checker dither in highlight "
                "A or B for the one area that matters, our mark in the corner. A small library of pixel icons for "
                "our recurring subjects (user, window, note, chart, calendar, book) would make each new thumbnail a "
                "few minutes of layout.",
        "confidence": "high",
        "demo": ("demo-b-pixel-icon.png", "b",
                 "Demonstration (b): pixel icons on the teal tint with the dot grid. Each icon is a text map of "
                 "cells turned into squares; the person and the window hero are filled with a checker dither in "
                 "highlight B and A.",
                 "about 15 minutes to write"),
    },
    {
        "id": "dithered",
        "name": "Dithered and halftone objects on a flat color",
        "refs": [1, 6, 9, 11, 13],
        "style": "A real photograph or 3D render (a robot hand and a database, a power substation, a laptop with a "
                 "clock, server stacks) reduced to a pattern of dots or square pixels, in a single ink, on one flat "
                 "color: red-orange, acid yellow, blue. A loose dot grid or scattered pixel crosses sit behind. "
                 "Ref-09 is the same treatment applied to a vector icon (a cloud over databases). Type is rare and "
                 "plain. The brand mark is big in the corner on ref-09, absent on the rest.",
        "use": "Real-world weight with a printed, newsy feel. The photo says \"this exists\", the dots say \"this is "
               "our publication\". It suits industry pieces, case studies, opinion, event recaps and anything "
               "about a physical place, product or person.",
        "verdict": "source",
        "why": "The dot treatment itself is pure code: a dot screen, Floyd-Steinberg error diffusion or an ordered "
               "Bayer pattern are each a few lines in Pillow, followed by recoloring to two colors and placing on "
               "the tint. What code cannot make is the subject. It needs a photograph with real light and shadow. "
               "Sources: the owner's own photos first (desk, workshops, sketches, devices); open-license photo "
               "sites such as Unsplash and Pexels (free to use, attribution appreciated, no reselling the photo "
               "alone); for ref-09 style, an open icon set. Demonstration (d) runs the pipeline on a screenshot of "
               "the owner's Printables site: the method works, but a flat screenshot has little tone, so it reads "
               "as an outline; a photo with shadows gives the rich result in ref-01 and ref-06.",
        "ours": "A photo cut out from its background, reduced to ink dots, on the article's tint with a faint dot "
                "grid, our mark in the corner. Best with the owner's own photos, which also builds the authority "
                "the site is for.",
        "confidence": "low",
        "confidence_note": "for code alone; high once a good photo is supplied",
        "demo": ("demo-d-halftone.png", "d",
                 "Demonstration (d): a 45-degree dot screen of a source image on the pink tint. The source is a "
                 "screenshot of the owner's Printables site (the Halloween calendar sheet), tilted, given a soft "
                 "shadow, then turned into ink dots whose size follows the darkness.",
                 "about 15 minutes to write, including finding a source"),
    },
    {
        "id": "icon-sequence",
        "name": "Icon sequences on a grained grid",
        "refs": [24, 25, 28],
        "note": "ref-25 and ref-28 are the same image.",
        "style": "Four or five line icons from one consistent set (a table with a bolt, a branching diagram, a "
                 "lightbulb, a document with a magnifier) arranged as a sequence: on white discs riding a conveyor "
                 "belt, or in a numbered ring around a soft orange glow. Grained orange or yellow field with a grid "
                 "or a few edge lines. Numbers in a mono face. No brand mark.",
        "use": "Order and completeness: \"there are five steps\" or \"these four features\". It suits listicles, "
               "frameworks, step-by-step guides and product round-ups, where the count is the hook.",
        "verdict": "source",
        "why": "The layout, discs, conveyor, glow, numbers and grain are code alone. The icons should come from an "
               "open set so they share one stroke weight and look professional: Lucide (ISC license), Phosphor "
               "(MIT), Tabler (MIT). All three allow use without attribution. Drawing twenty good icons by hand "
               "is possible but slower and less consistent than taking them from a set.",
        "ours": "Icons from one open set in ink at our 2.5-unit stroke, on card-white discs with a solid ink shadow, "
                "numbered in Inter, on the article's tint with grain. One highlight-A disc marks the step the "
                "article is about.",
        "confidence": "high",
        "confidence_note": "with an open icon set",
    },
    {
        "id": "type-cover",
        "name": "Typographic covers on dark",
        "refs": [2, 4, 8],
        "style": "A near-black field (dot grid on one) with a title in a heavy mono or pixel face, a short "
                 "subtitle, sometimes a small colored kicker above, and one image: a blue fingerprint drawn in fine "
                 "lines, a dithered factory photo in a framed panel, or a full-bleed dithered event photo. Accent in "
                 "acid yellow or blue. The brand mark sits large in yellow in the corner of the event cover.",
        "use": "Headline-first. The words do the work and the image is supporting texture. It suits series, "
               "reports, event recaps, \"what we heard\" pieces and anything where the title is the hook and must "
               "be readable in a feed.",
        "verdict": "source",
        "why": "The type is easy and exact with our self-hosted fonts. Two of the three use a dithered photograph "
               "(see the dithered group for sources and method) and the fingerprint needs a fingerprint image or "
               "vector from outside. With a code-drawn object instead (a diagram, a pixel icon), the cover is code "
               "alone. Note that a title inside the image doubles the headline on the page and is lost in search "
               "results, so this suits social cards more than on-site thumbnails.",
        "ours": "If used, on a tint rather than black, the title in Inter Display Bold, one object from the "
                "flat-vector or pixel library, our mark in the corner. Best kept for social images and series covers.",
        "confidence": "medium",
    },
    {
        "id": "dark-diagram",
        "name": "Dark line diagrams with one accent",
        "refs": [3, 27, 35],
        "style": "A near-black field, sometimes with a faint dot grid, carrying a real explainer diagram: a bar "
                 "chart with a lookback window, two ranked lists swapped by a search method, a numbered pipeline of "
                 "boxes. Thin white or gray lines, small mono labels, rounded boxes, and one accent color (red, "
                 "blue, lime, teal) for the part that matters. Partner logos inside the diagram on ref-35, no brand "
                 "mark otherwise.",
        "use": "Precise and technical. It promises a mechanism will be explained. It suits deep explainers and "
               "comparisons, where the thumbnail is literally the article's key figure.",
        "verdict": "code",
        "why": "This is boxes, lines, arrows and text, exactly what our explainer generator already draws. "
               "Demonstration (c) is a four-stage product flow with a feedback loop in one accent, on our ink as "
               "the background. Text renders with system mono fonts, so the export should stick to fonts that are "
               "installed or self-hosted.",
        "ours": "Ink #1D1B16 as the field with a faint white dot grid, white lines and labels, one highlight A from "
                "the article's tint as the accent. It breaks our rule of one pastel tint per image, so it suits a "
                "named series (for example data or metrics pieces) rather than the main rotation.",
        "confidence": "high",
        "demo": ("demo-c-dark-diagram.png", "c",
                 "Demonstration (c): a dark line diagram on our ink with yellow highlight A as the one accent. "
                 "Four stages, white outlines, the accent on discovery and a dashed loop back from ship.",
                 "about 10 minutes to write"),
    },
    {
        "id": "dark-glow",
        "name": "Dark glow diagrams",
        "refs": [32, 33, 34],
        "style": "Pure black with large soft shapes in dark gray (a cloud, a half-circle) lit from within, and "
                 "objects drawn in glossy white lines that fade at their ends: a cloud of database drums with one "
                 "lit in yellow, a tangle of cards sorted into a grid, a sync loop to a cloud. One accent at most. "
                 "No type, no mark.",
        "use": "Premium, product-launch, infrastructure. It feels like a keynote slide. It suits architecture, "
               "migration and scale topics; it is cooler and more corporate than the rest of the set.",
        "verdict": "code",
        "why": "Soft shapes are SVG gradients and blur filters, which our renderer supports; fading line ends are "
               "linear gradients on strokes. It can be made here, but getting the glow and depth to look expensive "
               "rather than flat takes tuning per image, so the quality is less predictable than the flat styles.",
        "ours": "Probably not for us: black breaks the tint system and the mood is more enterprise than editorial. "
                "If ever used, the article's highlight A as the single lit element.",
        "confidence": "medium",
    },
    {
        "id": "light-grid",
        "name": "Light grid diagram",
        "refs": [31],
        "style": "Near-white with a faint square grid and fine speckle, a thin rounded inner frame, and an abstract "
                 "diagram: blocks of black stripes (rows of data) with orange lines fading in from the left and two "
                 "arrows splitting one block into two. One accent color. No type, no mark.",
        "use": "Calm, precise, quietly technical. It explains a structural idea (splitting, merging, partitioning) "
               "without words. It suits concept explainers and pairs naturally with figures inside the article.",
        "verdict": "code",
        "why": "Lines, rectangles, a gradient on a stroke, a grid and speckle noise. It is the closest of all the "
               "references to the explainer illustrations we already make on the Printables tints.",
        "ours": "Exactly our explainer style: the article's tint with the dot grid, ink lines, highlight A or B as "
                "the accent, our mark in the corner. A thumbnail can be a simplified version of the article's key "
                "figure.",
        "confidence": "high",
    },
    {
        "id": "particle",
        "name": "Particle field render",
        "refs": [7],
        "style": "A black panel inside a thin rounded frame. Thousands of tiny yellow dots stream from both sides "
                 "into a pinch point, glowing where they are densest, with a pixel table icon at the waist, a small "
                 "mono label on a leader line, and a large pixel-font number (2.8s) to the right.",
        "use": "Speed, volume, a bottleneck. One number is the headline. It suits performance stories and "
               "before-and-after results.",
        "verdict": "code",
        "why": "A particle field is a loop that scatters dots along a curve with some jitter, plus a blur for the "
               "glow; the icon is pixel art and the number is type. All doable in Python. The organic look of the "
               "streams needs a few rounds of tuning to avoid looking mechanical.",
        "ours": "Ink dots streaming on the article's tint (no glow), a pixel icon at the pinch, one number in Inter "
                "Display. Occasional use for a piece built around one result.",
        "confidence": "medium",
    },
    {
        "id": "character",
        "name": "Character drawing on a grained grid",
        "refs": [26],
        "style": "The flat-vector look (grained orange field, square grid, a line chart with dots) but the subject is "
                 "an elephant with real character: hand-drawn contour lines for the legs, ear and trunk, a pale "
                 "yellow fill and a deep red shadow, standing on the chart like a pull toy. No type, no mark.",
        "use": "Warmth and personality. A mascot or a metaphor animal makes a piece memorable. It suits flagship "
               "articles, annual pieces and anything that should be shared.",
        "verdict": "external",
        "why": "The background, chart, grain and shadow are code. The elephant is not: an animal with believable "
               "proportions and expressive line work, written by hand as SVG, comes out stiff and crude. It needs "
               "a human illustrator or an image-generation tool, given a prompt that describes this style (flat "
               "shape, single outline, pale fill, solid offset shadow, no gradients) and our palette. The result "
               "would then be traced or cleaned, recolored to the tint and highlights, given the grain and grid, "
               "and marked, all by code.",
        "ours": "A small set of recurring characters drawn once by an illustrator (for example a researcher, a "
                "product manager, a user), reused across flagship pieces on their article's tint with code adding "
                "the grid, grain, shadow and mark.",
        "confidence": "low",
    },
]


def size(n):
    with Image.open(HERE / f"ref-{n:02d}.png") as im:
        return im.size


def badge(key):
    label, cls = VERDICT[key]
    return f'<span class="badge {cls}">{label}</span>'


def main():
    times = json.loads((HERE / "demo" / "times.json").read_text())
    total = sum(len(g["refs"]) for g in GROUPS)
    assert total == 35 and sorted(r for g in GROUPS for r in g["refs"]) == list(range(1, 36))

    rows = ""
    for g in GROUPS:
        conf = g["confidence"] + (f' <span class="muted">({g["confidence_note"]})</span>' if g.get("confidence_note") else "")
        rows += (f'<tr><td><a href="#{g["id"]}">{escape(g["name"])}</a></td><td class="num">{len(g["refs"])}</td>'
                 f'<td>{badge(g["verdict"])}</td><td>{conf}</td></tr>\n')

    sections = ""
    for g in GROUPS:
        thumbs = ""
        for n in g["refs"]:
            w, h = size(n)
            thumbs += (f'<li><a href="ref-{n:02d}.png"><img src="ref-{n:02d}.png" width="{w}" height="{h}" '
                       f'loading="lazy" alt="Reference {n}"><span>ref-{n:02d}</span></a></li>')
        demo = ""
        if g.get("demo"):
            f, k, cap, write_time = g["demo"]
            demo = (f'<figure class="demo"><a href="demo/{f}"><img src="demo/{f}" width="600" height="338" '
                    f'loading="lazy" alt="{escape(cap)}"></a><figcaption>{escape(cap)} '
                    f'<strong>Time:</strong> {write_time}, {times[k]} seconds to render. Made here with code.'
                    f'</figcaption></figure>')
        note = f'<p class="muted small">{escape(g["note"])}</p>' if g.get("note") else ""
        conf = g["confidence"] + (f' ({g["confidence_note"]})' if g.get("confidence_note") else "")
        sections += f"""
<section class="group" id="{g['id']}" aria-labelledby="h-{g['id']}">
  <header class="group-head">
    <h2 id="h-{g['id']}">{escape(g['name'])}</h2>
    <p class="count">{len(g['refs'])} {'reference' if len(g['refs']) == 1 else 'references'}</p>
  </header>
  <ul class="thumbs">{thumbs}</ul>
  {note}
  <div class="group-body{' has-demo' if demo else ''}">
    <div class="prose">
      <h3>The style</h3><p>{escape(g['style'])}</p>
      <h3>What it says and when it fits</h3><p>{escape(g['use'])}</p>
      <div class="verdict {VERDICT[g['verdict']][1]}">
        <p class="verdict-line">{badge(g['verdict'])}</p>
        <p>{escape(g['why'])}</p>
      </div>
      <div class="ours"><h3>What I would make for us</h3><p>{escape(g['ours'])}</p>
      <p class="conf">Quality by code alone: <strong>{escape(conf)}</strong></p></div>
    </div>
    {demo}
  </div>
</section>"""

    html = TEMPLATE.replace("{{ROWS}}", rows).replace("{{SECTIONS}}", sections)
    (HERE / "index.html").write_text(html, encoding="utf-8")
    print("index.html written")


TEMPLATE = """<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Thumbnail styles</title>
<meta name="description" content="The 35 reference thumbnails grouped by style, with what each can be made with here and a recommendation for our thumbnails.">
<style>
@font-face { font-family: "Inter"; src: url("../../fonts/inter/Inter-Regular.woff2") format("woff2"); font-weight: 400; font-display: swap; }
@font-face { font-family: "Inter"; src: url("../../fonts/inter/Inter-SemiBold.woff2") format("woff2"); font-weight: 600; font-display: swap; }
@font-face { font-family: "Inter Display"; src: url("../../fonts/inter/InterDisplay-Bold.woff2") format("woff2"); font-weight: 700; font-display: swap; }
:root {
  --paper: #FDFCF8; --ink: #1D1B16; --muted: #5F5B52; --rule: #E2DDD1; --panel: #F4F1E8;
  --code-bg: #DCEFD8; --code-fg: #245A18; --code-edge: #97DD88;
  --source-bg: #FFF3C4; --source-fg: #6B5208; --source-edge: #E8C547;
  --ext-bg: #FBE0E6; --ext-fg: #8E1430; --ext-edge: #EE7792;
  --link: #174FA1; --focus: #174FA1;
  color-scheme: light;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --paper: #1D1B16; --ink: #F1EEE6; --muted: #B3AD9F; --rule: #3A372F; --panel: #26241E;
    --code-bg: #1F3A1A; --code-fg: #B8EBAE; --code-edge: #388627;
    --source-bg: #3B3212; --source-fg: #FFE58A; --source-edge: #A18517;
    --ext-bg: #42141F; --ext-fg: #FFB8C7; --ext-edge: #A11736;
    --link: #9EC2F5; --focus: #9EC2F5;
    color-scheme: dark;
  }
}
:root[data-theme="dark"] {
  --paper: #1D1B16; --ink: #F1EEE6; --muted: #B3AD9F; --rule: #3A372F; --panel: #26241E;
  --code-bg: #1F3A1A; --code-fg: #B8EBAE; --code-edge: #388627;
  --source-bg: #3B3212; --source-fg: #FFE58A; --source-edge: #A18517;
  --ext-bg: #42141F; --ext-fg: #FFB8C7; --ext-edge: #A11736;
  --link: #9EC2F5; --focus: #9EC2F5;
  color-scheme: dark;
}
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }
body { margin: 0; background: var(--paper); color: var(--ink); font: 400 17px/1.6 "Inter", system-ui, sans-serif; }
a { color: var(--link); text-underline-offset: 2px; }
a:focus-visible { outline: 3px solid var(--focus); outline-offset: 3px; border-radius: 3px; }
img { max-width: 100%; height: auto; display: block; }
.wrap { max-width: 1400px; margin: 0 auto; padding: 0 16px; }
@media (min-width: 720px) { .wrap { padding: 0 40px; } }
h1, h2 { font-family: "Inter Display", "Inter", system-ui, sans-serif; font-weight: 700; letter-spacing: -0.02em; line-height: 1.08; }
h1 { font-size: clamp(2.6rem, 7vw, 5.2rem); margin: 0 0 .3em; }
h2 { font-size: clamp(1.6rem, 3.2vw, 2.4rem); margin: 0; }
.h-small { font-size: 1.4rem; margin-bottom: 12px; }
h3 { font-size: 1rem; font-weight: 600; margin: 1.4em 0 .3em; }
p { margin: 0 0 .8em; }
.muted { color: var(--muted); }
.small { font-size: .9rem; }
.top { padding: 56px 0 24px; border-bottom: 1px solid var(--rule); }
.intro { max-width: 68ch; font-size: 1.12rem; }
.intro p:last-child { margin-bottom: 0; }
.summary { padding: 32px 0 8px; }
.table-scroll { overflow-x: auto; }
table { border-collapse: collapse; width: 100%; min-width: 560px; font-size: .97rem; }
th, td { text-align: left; padding: 10px 12px 10px 0; border-bottom: 1px solid var(--rule); vertical-align: middle; }
th { font-weight: 600; color: var(--muted); font-size: .9rem; }
td.num, th.num { text-align: right; padding-right: 24px; font-variant-numeric: tabular-nums; }
tfoot td { font-weight: 600; border-bottom: 0; }
.badge { display: inline-block; padding: 3px 10px 4px; border-radius: 999px; font-size: .85rem; font-weight: 600; line-height: 1.3; border: 1.5px solid; white-space: nowrap; }
.v-code .badge, .badge.v-code { background: var(--code-bg); color: var(--code-fg); border-color: var(--code-edge); }
.v-source .badge, .badge.v-source { background: var(--source-bg); color: var(--source-fg); border-color: var(--source-edge); }
.v-external .badge, .badge.v-external { background: var(--ext-bg); color: var(--ext-fg); border-color: var(--ext-edge); }
.group { padding: 56px 0 24px; border-bottom: 1px solid var(--rule); scroll-margin-top: 16px; }
.group-head { display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 20px; margin-bottom: 20px; }
.count { margin: 0; color: var(--muted); }
.thumbs { list-style: none; margin: 0 0 12px; padding: 0; display: grid; gap: 12px; grid-template-columns: repeat(auto-fill, minmax(min(100%, 230px), 1fr)); }
.thumbs a { display: block; text-decoration: none; color: var(--muted); font-size: .82rem; }
.thumbs img { width: 100%; aspect-ratio: 16 / 9; object-fit: contain; background: var(--panel); border-radius: 6px; }
.thumbs span { display: block; padding-top: 4px; }
.group-body { display: grid; gap: 32px; margin-top: 16px; }
@media (min-width: 1000px) { .group-body.has-demo { grid-template-columns: minmax(0, 1fr) minmax(0, 600px); align-items: start; } }
.prose { max-width: 72ch; }
.prose h3:first-child { margin-top: 0; }
.verdict { margin: 1.4em 0; padding: 16px 18px 6px; border-left: 4px solid; border-radius: 0 6px 6px 0; background: var(--panel); }
.verdict.v-code { border-color: var(--code-edge); }
.verdict.v-source { border-color: var(--source-edge); }
.verdict.v-external { border-color: var(--ext-edge); }
.verdict-line { margin-bottom: .6em; }
.ours h3 { margin-top: 0; }
.conf { color: var(--muted); }
.conf strong { color: var(--ink); }
.demo { margin: 0; position: sticky; top: 16px; }
.demo img { border-radius: 6px; width: 100%; }
.demo figcaption { font-size: .9rem; color: var(--muted); margin-top: 10px; }
.demo figcaption strong { color: var(--ink); font-weight: 600; }
.closing { padding: 56px 0 80px; }
.closing .prose { max-width: 76ch; }
.closing ol { padding-left: 1.3em; }
.closing li { margin-bottom: .7em; }
@media (prefers-reduced-motion: reduce) { * { scroll-behavior: auto; } }
@media (max-width: 999px) { .demo { position: static; } }
</style>
</head>
<body>
<main>
<div class="wrap">
  <header class="top">
    <h1>Thumbnail styles</h1>
    <div class="intro">
      <p>The 35 blog thumbnails the owner shared, sorted into ten styles by how they look and how they are made.
      Each style says what it is, what it communicates, and whether we can make it here: with code alone, with code
      plus a photo or icon from outside, or only with an illustrator or an image-generation tool.</p>
      <p class="muted">Four styles have a small demonstration made here on our own palette (the Printables tints and
      our mark), with the time it took. Internal reference only; the references belong to their owner.</p>
      <p><a href="gallery.html">Thumbnail gallery</a>: the eleven styles we decided on (ten made with code, one for the
      owner's photos), each drawn by our generator on a sample subject with a bold background and the lockup.</p>
    </div>
  </header>

  <section class="summary" aria-labelledby="h-summary">
    <h2 id="h-summary" class="h-small">Summary</h2>
    <div class="table-scroll">
    <table>
      <thead><tr><th scope="col">Style</th><th scope="col" class="num">Refs</th><th scope="col">Can we make it?</th><th scope="col">Quality by code alone</th></tr></thead>
      <tbody>
{{ROWS}}      </tbody>
      <tfoot><tr><td>Total</td><td class="num">35</td><td colspan="2"></td></tr></tfoot>
    </table>
    </div>
    <p class="muted small" style="margin-top:12px"><span class="badge v-code">Code alone</span> drawn and rendered here, no outside input.
    <span class="badge v-source">Code plus a source image</span> needs a photo or icon from outside, code does the rest.
    <span class="badge v-external">External image tool</span> needs an illustrator or an image-generation tool, then code finishes it.</p>
  </section>
{{SECTIONS}}

  <section class="closing" aria-labelledby="h-rec">
    <h2 id="h-rec">Recommendation</h2>
    <div class="prose">
      <p>Adopt three styles for our thumbnails, all made here reliably on the article's tint, so a new piece needs
      no outside help:</p>
      <ol>
        <li><strong>Flat vector with hard shadows on a grained grid, as the default.</strong> Warm, editorial,
        readable at small sizes, and every object in our subject area (a window, a cursor, a note, a chart, a
        magnifier) is simple geometry. Demonstration (a).</li>
        <li><strong>The light grid diagram for explainer-led articles.</strong> It is our existing figure style, so
        the thumbnail can be a simplified version of the article's key figure.</li>
        <li><strong>Pixel icons for tools, calculators, templates and short tactical pieces.</strong> A small icon
        library makes each one a few minutes of layout and gives that section of the site its own look.
        Demonstration (b).</li>
      </ol>
      <p>Icon sequences fit inside the first style whenever an open icon set (Lucide, Phosphor or Tabler) is used for
      the icons.</p>
      <p>Reserve for occasional pieces with outside help:</p>
      <ul>
        <li><strong>Dithered photos</strong> for case studies, interviews and event pieces, using the owner's own
        photos first. The dot treatment is code; the photo is the input.</li>
        <li><strong>Character drawings</strong> for flagship articles, from an illustrator or an image-generation
        tool, then finished by code with our grid, grain, shadow and mark.</li>
      </ul>
      <p>Leave out the dark styles (dark diagrams, glow diagrams, dark covers) from the main rotation: they can be
      made here, but black breaks our one-tint-per-article rule. Keep them in mind for a named series or social
      images.</p>
    </div>
  </section>
</div>
</main>
</body>
</html>
"""

if __name__ == "__main__":
    main()
