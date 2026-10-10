# Illustration rules

Rules for every explainer illustration on userandproduct. Draft of 9 Oct 2026; written so it can become a skill.
Generator: `research/mockups/tools/illustration.py`. Source of the palette: `references/printables-tints.md` (the
Printables site's tile tints and dot grid). Examples: http://localhost/user-and-product/research/mockups/option-1/build/explainers.html

The picture is whatever the article needs: a scene, an object, a chart, a diagram, anything; the rules below cover
only the ground, the dots, the lockup, the type and the colours.

## The rules in short

1. The ground is one of the eight Printables tints with the dot grid, nothing else is fixed about the picture. Draw
   whatever the article needs, in whatever colours it needs, and make sure it reads on the tint it sits on.
2. One tint per article: every explainer in an article uses the article's tint.
3. The tint comes from rotation, so neighbouring articles differ and an article always keeps its colour.
4. Related-card thumbnails use their own article's tint.
5. The same PNG in both themes; a pastel image on the dark page is intended.
6. Type is Inter, labels at least 27 units and notes at least 24 units, and every text on a fill passes 4.5:1.

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

## Colour

The foundation is the tint. Everything drawn on it is open: use the colours the picture calls for. The one
requirement is that it works with the background it is on: every shape passes 3:1 against the tint and against
what it touches, every label passes 4.5:1 on whatever it sits on. The generator checks these pairs and adjusts
lightness until they pass; `"accent"` on an element takes a named colour (`fire`, `warning`, `success`), a hex or a
hue, and the tint's own ink, muted and highlight colours remain available as the plain palette.

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

## Canvas, margins, lines

- Canvas 1200 x 675 (16:9). Keep the picture 72 units inside each edge, and the bottom-right corner free for the
  lockup: nothing below y 597 to the right of x 912 (the lockup, 928 to 1168 by 613 to 643,
  plus 16 units of clear space).
- Lines 2.5 units (about 1.5px on screen, the Printables border) for boxes, rules and arrows; dashed 10/8 for targets;
  chart lines 4 units in highlight B. Boxes radius 4. Arrowheads 14 x 14.

## Type

- Typeface: the site's Inter, from `research/mockups/fonts/inter/`. Labels in Inter Medium (SemiBold for the one label
  that must stand out); notes and axis labels in Inter Regular. Monospace (Consolas) only for a label that is code,
  such as a field name or a status code. The generator turns Inter into outlines inside the SVG, so the file draws
  the same everywhere and needs no installed font.
- Sizes on the 1200-unit canvas: labels at least 27 units (16 px when the figure shows 720 px wide in the article),
  notes at least 24 units (14 px). Never smaller. The generator raises any smaller size to the floor and warns, so a
  smaller size never reaches a file.
- Thumbnail figures (exported 600 wide, shown at about a quarter of the canvas): double the floors, labels at least
  54 units and notes at least 48 units.
- At most three or four words per label. A label that does not fit its shape is a spec error: enlarge the shape or
  shorten the label, never shrink the type. The generator refuses a box label wider than its box less 16 units a side.
- Text on a coloured fill must pass 4.5:1. The generator checks every label against its fill, picks the dark ink or
  white, whichever passes, and if neither does it lightens or darkens the fill until one does. Notes sit on the tint
  in ink or the muted colour, both above 5:1 on all eight tints.

## Lockup

- Every explainer figure carries the full logo, the lockup (the mark plus the "userandproduct" wordmark), not the
  mark alone (owner, 10 Oct 2026). The same principle as the thumbnails: the solid one-colour lockup from the final
  pack, `final-logo-2/svg/lockup-black.svg` on the eight light Printables tints, `lockup-white.svg` only if a ground
  is ever dark. The generator reads it from the pack and picks the colour by contrast.
- Width one fifth of the figure's width (the thumbnail rule): 240 units on the 1200 canvas, about 30 units tall.
  Bottom-right corner, 32 units in from the bottom and right edges.
- 60% opacity: quiet inside an article, but the wordmark still reads on the lightest tints (yellow and teal) at the
  width the figure appears in the article column (about 720px, the lockup about 144px wide). It renders at about
  4.8 to 5.0:1 on the tints.
- The head and band are true holes in the pack file, so the generator backs them with the flat tint colour at full
  opacity: the dot grid never runs through the figure.
- Never on the picture, never in the blue, never recoloured.

## What an illustration is not

- No frame, card outline, border, notches or title inside the image; the point goes in the `<figcaption>`.

## Export, names, use on the page

- Figures 1200 x 675 PNG, with the SVG next to it as the source. Thumbnails 600 x 338 PNG.
- Names come from the SEO brief, not from the drawing. The researcher or SEO reviewer sets the article's slug from
  its target phrase and names each figure with that slug plus two or three words that say what the figure shows, in
  words a reader would search: `<article-slug>-<what-it-shows>.png` / `.svg` (for example
  `how-to-write-a-prd-twelve-questions.png`), `<article-slug>-thumb.png` for thumbnails. Lowercase, hyphens, no
  dates, sizes or ids, no keyword padding (the search-policy rulebook's image rules apply). The `alt` text is set the
  same way, from the brief, describing the figure in context.
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

Besides box, arrow, rule, hrule, polyline, dot and text, the generator draws filled shapes (`circle`, `rrect`,
`polygon`, `path`), small line glyphs from paths (`glyph`, with `GLYPHS` listing the names), number badges (`badge`)
and a caption band (`band`). Shapes, glyphs, badges, dots and polylines take `accent` (see Colour);
`ACCENT_LOG` holds every accent pair and its ratio. The docstring at the top of `illustration.py` lists every field. Text takes `weight`
(`regular`, `medium`, `semibold`), `code` for monospace, and `
` for a second line.

`palette_for(tint)` returns the derived colours and raises `TintError` for anything outside the eight. The article's
figures and thumbnails are in `research/mockups/option-1/build/figures.py`; the gallery in `research/mockups/option-1/build/explainers.py`.
