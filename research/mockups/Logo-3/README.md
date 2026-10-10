# Logo 3: the owner's mark, in color

The owner drew this mark in Illustrator (10 Oct 2026): a solid disc with two cut-outs, a rounded diamond
for the head over a wide curved band for the shoulders (the band also reads as a smile or a bowl). This
folder keeps that drawing exactly as drawn and builds everything around it: a clean master, monochrome,
twelve color options, four gradient options, lockups, avatars, favicons, a thumbnail tile, previews and
an export folder to try for real.

Board: http://localhost/user-and-product/research/mockups/Logo-3/

## What is here

- `Logo.svg`: the owner's file. Never edited; `check.py` confirms it matches `source/Logo-owner.svg`.
- `source/Logo-owner.svg`: the copy every build reads its geometry from (`geo.py` takes the circle and both
  paths verbatim).
- `svg/mark.svg`: the clean master. The owner's geometry exactly, one compound path with `fill-rule="evenodd"`,
  so the cut-outs are true holes and show whatever is behind the mark. The circle is written as four
  quarter arcs (two half arcs render a gray level off along the top edge; four match the owner's file
  pixel for pixel). No comment, no classes, explicit fill.
- `svg/mark-solid.svg`: the same with the cut-outs filled white, for photos. On white it renders the same as
  the master (within one gray level of 255 along the cut-out edges, from anti-aliasing) and pixel for pixel the
  same as the owner's file.
- `svg/mark-black.svg`, `mark-white.svg`, `mark-currentcolor.svg`, `lockup-black.svg`, `lockup-white.svg`,
  `stacked-black.svg`, `stacked-white.svg`: monochrome masters.
- `svg/<option>/`: per option `mark`, `mark-dark`, `single` (only C11 and C12, where the cut-outs are filled),
  `avatar-circle` (the disc edge to edge), `avatar-rounded`, `avatar-square` (LinkedIn, Apple touch icon),
  `lockup`, `lockup-dark`, `stacked`, `stacked-dark`.
- `png/<option>/`: favicons at 16 and 32 px on white and on near-black (`#111111`), transparent 16 px tab icons,
  the 600 x 338 thumbnail tile (at 2x); for the gradients also the avatars as 440 px PNGs. `png/mono/`: the
  monochrome favicons.
- `export/`: the signal blue option ready to use: `favicon.svg` (switches to `#8EA2FF` in dark themes),
  `favicon.ico` (16, 32, 48), `favicon-16.png`, `favicon-32.png`, `favicon-48.png` (figure filled white, so they
  hold in light and dark tabs), `apple-touch-icon-180.png`, `social-square-400.png` and `-1080.png`,
  `social-circle-400.png` and `-1080.png` (transparent corners), `head-snippet.html`, and `gradient/` (each
  gradient as a 1080 square and circle, dithered; social only).
- `index.html`: the board (light and dark, theme toggle).
- `geo.py` (geometry, options, writers), `build.py` (writes everything), `board.py` (the board), `check.py`
  (checks), `status.py` (progress page updates).

## Rebuild

```
python build.py
python check.py
```

Needs Python 3 with fontTools, uharfbuzz, skia-pathops, resvg-py, Pillow and numpy, plus
`research/mockups/tools/wordmark.py` and `research/mockups/fonts/inter/`. `check.py` also needs Playwright
with Chrome and XAMPP serving (for the 200 and overflow checks). It checks: the owner file is unchanged; the
master and mark-solid render the same as the owner's file at 512 and 1920 px; every SVG is valid XML with a
viewBox, no fixed size, no live text and under 6 KB (largest about 5.3 KB); every favicon and export exists at
its size; the board answers 200; no horizontal overflow at 375 and 1280 px; no broken images.

## Lockup geometry

Wordmark: "userandproduct" in Inter Display Bold, lowercase, tracking 0, kerned, outlined to one path (to a
thousandth of an em, relative commands, which keeps each lockup under 6 KB).

- Side lockup: the disc is 1.12 cap heights across, a little taller than the capitals; its bottom sits on the
  baseline with the 1.2 percent overshoot a round letter has. Gap 0.40 of the disc, the first pack's gap.
- Stacked: the first pack's proportions, disc 3 cap heights, gap 0.76 cap heights, centered over the name.
- Header size 236 px wide, thumbnail size 120 px wide. Wordmark ink `#0B0B0C` on light, `#F1EEE7` on dark.

## Color options

Contrast is WCAG 2, disc against the ground; 3:1 is the bar for a graphic. Near-black is `#111111`.

| No. | Option | Disc | Second tone | Dark-mode disc | On white | On #111 | Needs |
|-----|--------|------|-------------|----------------|----------|---------|-------|
| C01 | Signal blue | `#2B46A0` | none | `#8EA2FF` (7.9:1) | 8.4:1 | 2.2:1 | White grounds; dark mode uses the light blue |
| C02 | Deep navy | `#1B2A55` | none | `#A9B8E8` (9.6:1) | 13.9:1 | 1.4:1 | White grounds; dark mode uses the light navy |
| C03 | Cobalt | `#2450D8` | none | `#7A96FF` (6.9:1) | 6.5:1 | 2.9:1 | White grounds; dark mode uses the light cobalt |
| C04 | Near-black ink | `#0B0B0C` | none | `#F1EEE7` (16.3:1) | 19.7:1 | 1.0:1 | White grounds; flips to off-white on dark |
| C05 | Warm charcoal | `#3A3532` | none | `#D8D0C8` (12.4:1) | 12.1:1 | 1.6:1 | White grounds; warm light gray on dark |
| C06 | Deep green | `#0E5A49` | none | `#5FC7A6` (9.2:1) | 8.1:1 | 2.3:1 | White grounds; mint on dark |
| C07 | Oxblood | `#6E1F2A` | none | `#E48593` (7.3:1) | 11.1:1 | 1.7:1 | White grounds; rose on dark |
| C08 | Vermilion | `#D9411E` | none | same | 4.4:1 | 4.2:1 | Both grounds, one color |
| C09 | Plum | `#4B2A7A` | none | `#B9A0EC` (8.4:1) | 11.0:1 | 1.7:1 | White grounds; lilac on dark |
| C10 | Teal | `#0F766E` | none | `#3DC2B5` (8.6:1) | 5.5:1 | 3.5:1 | Both grounds; the brighter teal on dark lifts it |
| C11 | Mustard with a dark figure | `#E3A72F` | head and band `#0B0B0C` | same | 2.1:1 | 8.8:1 | Dark grounds or as a yellow field; on white the edge is soft, the ink figure (9.2:1 on the yellow) carries it |
| C12 | Two-tone blue | `#2B46A0` | head `#FFFFFF`, band `#8EA2FF` | same | 8.4:1 | 2.2:1 | White grounds; on dark the edge is soft but the filled head (8.4:1) and band (3.5:1) read |

In C01 to C10 the cut-outs are empty and show the ground. Avatars are opaque, like an upload, so their
figure is white (ink in C11).

## Gradient options (social only)

House rule from the first logo pack: gradients are for social backgrounds only, never on the site. These are
social candidates unless the owner says otherwise. Diagonal, two stops, top left to bottom right; PNGs are
rendered at four times the size, stepped down and dithered by under one gray level, so they do not band.

| No. | Gradient | Top left | Bottom right | White figure on it |
|-----|----------|----------|--------------|--------------------|
| G01 | Signal blue to cobalt | `#3B63E6` | `#2B46A0` | 5.1:1 to 8.4:1 |
| G02 | Navy to teal | `#0F766E` | `#1B2A55` | 5.5:1 to 13.9:1 |
| G03 | Plum to vermilion | `#D9411E` | `#4B2A7A` | 4.4:1 to 11.0:1 |
| G04 | Charcoal to ink | `#4A4440` | `#0B0B0C` | 9.6:1 to 19.7:1 |

## Notes

- At 16 px the band's ends turn down, so with the head above it the figure can read as a frowning face,
  most of all on dark, where the cut-outs show the dark ground. The owner's reading is a person, a smile or a
  bowl; worth looking at in the tab previews before choosing.
- The thumbnail tile is the same warm paper (`#F4F1E8`) for every option so only the mark changes. Real
  article thumbnails follow the thumbnail rules (black or white lockup on a bold ground).
