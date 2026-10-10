# Illustration rules

Rules for every explainer illustration on userandproduct. Draft of 9 Oct 2026; written so it can become a skill.
Generator: `research/mockups/tools/illustration.py`. Source of the palette: `references/printables-tints.md` (the
Printables site's tile tints and dot grid). Examples: http://localhost/user-and-product/research/mockups/option-1/build/explainers.html

## The rules in short

1. The palette is the eight Printables tints, nothing else.
2. One tint per article: every explainer in an article uses the article's tint.
3. The tint comes from rotation, so neighbouring articles differ and an article always keeps its colour.
4. Related-card thumbnails use their own article's tint.
5. The same PNG in both themes; a pastel image on the dark page is intended.

## The eight tints

| Tint | Background | Highlight A (dark label) | Highlight B (white label) | Role |
|---|---|---|---|---|
| teal | #D7F0EE | #88DDD6 | #257E77 | rotates (1st) |
| yellow | #FFF3C4 | #FFE066 | #A18517 | rotates (2nd) |
| pink | #FBE0E6 | #EE7792 | #A11736 | rotates (3rd) |
| blue | #DBE8FB | #75A7F0 | #174FA1 | rotates (4th) |
| green | #DCEFD8 | #97DD88 | #388627 | rotates (5th) |
| purple | #E8E0F7 | #A585E0 | #4B2692 | rotates (6th) |
| peach | #FDE3D0 | #F9A86C | #A15117 | reserved |
| slate | #E0E6EE | #88ACDD | #29558E | reserved |

On every tint: ink #1D1B16 (13.5 to 15.5:1), muted #5F5B52 (5.3 to 6.1:1), plain boxes #FDFCF8 with a 2.5-unit
#1D1B16 border, rules and arrows in #1D1B16. Highlights are the saturated cousins of the pastel (same hue): A a mid
shade with the dark label, B a deep shade with a white label; the generator adjusts their lightness until the label
passes 4.5:1. Use at most one or two highlights per image, A first.

## Choosing the tint

- `tint_for_article(slug, index)` returns `["teal", "yellow", "pink", "blue", "green", "purple"][index % 6]`, where
  `index` is the article's publish order (the same rotation as `printables_tint_class` on Printables). Without an
  index it uses a stable hash of the slug. Consecutive articles therefore differ, and an article never changes colour.
- A writer may override with any of the eight, including the reserved peach and slate, but must give a reason
  (`override="peach", reason="..."`).
- Related thumbnails use their own article's tint, so a Related row naturally shows different colours. Never place two
  identical tints side by side; if a Related row would, pick a different related piece or override one with a reason.

## Dot grid

- Ink-coloured dots (#1D1B16) at 13% opacity, radius 1.9 units, every 22 units, over the whole image. That is the
  Printables grid (12 to 14px tile, 1px dot, 12 to 13%) at a 1200-unit canvas shown about 720px wide.

## Canvas, margins, lines, type

- Canvas 1200 x 675 (16:9). Keep the diagram 72 units inside each edge, and the bottom-right 100 x 100 corner free
  for the mark.
- Lines 2.5 units (about 1.5px on screen, the Printables border) for boxes, rules and arrows; dashed 10/8 for targets;
  chart lines 4 units in highlight B. Boxes radius 4. Arrowheads 14 x 14.
- Type: monospace only (Consolas in the export). Box labels 18 to 19 units, 16 units inside the box; notes and axis
  labels 17 to 18 units in the muted colour; thumbnails 24 to 28 units because they show at half size. Keep labels
  short (about 12 characters for a 145-unit box).

## Mark

- Our mark, the owner's disc from the final pack (`final-logo-2/svg/mark-black.svg`, or `mark-white.svg` if a ground
  is ever dark enough to need it; on the eight pastel tints it is always the black one), 34 units square, 32 units in
  from the bottom and right edges, at 35% opacity (about 2.3:1 on the tint: visible, quiet, decorative). Never on the
  diagram, never in the blue, never recoloured. The head and band are true holes in the pack file, so the generator
  backs them with the flat tint: the dot grid never runs through the figure.

## What an illustration is not

- No frame, card outline, border, notches or title inside the image; the point goes in the `<figcaption>`.
- No colour outside the eight tints and their derived colours.

## Export, names, use on the page

- Figures 1200 x 675 PNG, with the SVG next to it as the source. Thumbnails 600 x 338 PNG.
- Names: `fig-<slug>.png` / `.svg` (the slug says the point, for example `fig-where-prds-fail`);
  `<article-slug>-thumb.png` for thumbnails. Lowercase, hyphens, no dates or sizes.
- On the page: `<img>` with `width` and `height` (1200 x 675 or 600 x 338) so the space is reserved, `loading="lazy"`,
  a full `alt` that says what the diagram shows, and a 6px corner radius from the theme CSS (not in the image).
  Number figures in reading order in the figcaption ("Figure 1.").

## Using the generator

```python
import sys; sys.path.insert(0, "research/mockups/tools")
from illustration import tint_for_article, illustration, palette_for, write, png

tint = tint_for_article("how-to-write-a-prd-that-engineers-actually-read", index=0)   # teal
items = [
    {"type": "box", "x": 120, "y": 220, "w": 300, "h": 64, "label": "written for approval"},
    {"type": "box", "x": 450, "y": 220, "w": 300, "h": 64, "label": "decisions missing", "tint": "b"},
    {"type": "arrow", "x1": 422, "y1": 252, "x2": 448, "y2": 252},
    {"type": "hrule", "y": 420, "x1": 120, "x2": 1080, "dash": True},
    {"type": "text", "x": 120, "y": 470, "text": "kickoff"},
]
svg = illustration(items, tint=tint, uid="fig-example", title="Short title", desc="What it shows")
write(svg, "fig-example.svg")
png(svg, "fig-example.png", 1200)   # 600 for a thumbnail
```

`palette_for(tint)` returns the derived colours and raises `TintError` for anything outside the eight. The article's
figures and thumbnails are in `research/mockups/option-1/build/figures.py`; the gallery in `research/mockups/option-1/build/explainers.py`.
