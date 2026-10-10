# Logo 3: the owner's mark, in color

The owner drew this mark in Illustrator (10 Oct 2026): a solid disc with two cut-outs, a rounded diamond
for the head over a wide curved band for the shoulders (the band also reads as a smile or a bowl). This
folder keeps that drawing exactly as drawn and builds everything around it: a clean master, monochrome,
twenty-two color options, fourteen gradient options (numbered C01 to C22 and G01 to G14; numbers are
never reused or changed), lockups, avatars, favicons, a thumbnail tile, previews and
an export folder to try for real.

**Chosen (owner, 10 Oct 2026): C17 Electric blue, flat.** The final pack built from it is
`../final-logo-2/` (brand sheet: http://localhost/user-and-product/research/mockups/final-logo-2/brand-sheet.html).

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
  `lockup`, `lockup-dark`, `stacked`, `stacked-dark`; `svg/signal/` also keeps `lockup-before.svg` and
  `lockup-before-dark.svg`, the first side lockup, only for the before-and-after pair on the board.
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
viewBox, no fixed size, no live text and under 6 KB (339 SVGs, largest about 5.3 KB); every favicon and export exists at
its size; the board answers 200; no horizontal overflow at 375 and 1280 px; no broken images.

## Lockup geometry

Wordmark: "userandproduct" in Inter Display Bold, lowercase, tracking 0, kerned, outlined to one path (to a
thousandth of an em, relative commands, which keeps each lockup under 6 KB).

- Side lockup (changed 10 Oct 2026 after the owner said the mark looked too small): the first pack's
  geometry from `final-logo/build.py`. The disc is 1.4 cap heights across (101.9 units at 100 units per em),
  which is 1.09 of the wordmark's full ink height (ascender top 72.8 above the baseline to descender bottom
  20.4 below, 93.2 units). Its center sits 31.08 units above the baseline, midway between the cap band (72.75)
  and the x-height band (51.56), the same point the first pack's mark is centered on, so the mark and the name
  are centered on each other (the disc runs from 19.8 below the baseline to 82.0 above it). Gap 0.40 of the
  disc (40.7 units). Margin 4 units. The first version (disc 1.12 cap heights, bottom on the baseline) is kept
  only as `svg/signal/lockup-before*.svg`.
- Stacked: the first pack's stacked geometry, checked against it: disc 3 cap heights, gap 0.76 cap heights,
  centered over the name, margin 4 units.
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

### Added 10 Oct 2026: blues and vibrant colors

| No. | Option | Disc | Second tone | Dark-mode disc | On white | On #111 | Needs |
|-----|--------|------|-------------|----------------|----------|---------|-------|
| C13 | Azure | `#0B72D9` | none | `#5BA8FF` (7.6:1) | 4.7:1 | 4.0:1 | Both grounds; the lighter azure lifts it on dark |
| C14 | Royal blue | `#2F45C8` | none | `#A8B8FF` (9.9:1) | 7.5:1 | 2.5:1 | White grounds; light royal on dark |
| C15 | Slate blue | `#475C80` | none | `#B3C0DD` (10.3:1) | 6.8:1 | 2.8:1 | White grounds; light slate on dark |
| C16 | Midnight | `#0F1B3D` | none | `#9AA7F0` (8.2:1) | 16.9:1 | 1.1:1 | White grounds; periwinkle on dark |
| C17 | Electric blue | `#2E5BFF` | none | `#7DB0FF` (8.6:1) | 5.2:1 | 3.6:1 | Both grounds; the lighter blue lifts it on dark |
| C18 | Hot coral | `#E5432F` | none | same | 4.1:1 | 4.7:1 | Both grounds |
| C19 | Emerald | `#0B8F63` | none | same | 4.1:1 | 4.6:1 | Both grounds |
| C20 | Magenta | `#D6247A` | none | same | 4.8:1 | 3.9:1 | Both grounds |
| C21 | Tangerine | `#D9600A` | none | same | 3.7:1 | 5.1:1 | Both grounds |
| C22 | Lime with a dark figure | `#B5E61D` | head and band `#0B0B0C` | same | 1.5:1 | 12.9:1 | Dark grounds or as a field; the ink figure is 13.4:1 on the lime |

On the board: Blues (flat) C13 to C17, then Blue gradients, then Vibrant (flat) C18 to C22, then Vibrant
gradients, all after the first twelve colors and four gradients.

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
| G05 | Azure to signal blue | `#0B72D9` | `#2B46A0` | 4.7:1 to 8.4:1 |
| G06 | Royal blue to midnight | `#2F45C8` | `#0F1B3D` | 7.5:1 to 16.9:1 |
| G07 | Electric blue to cobalt | `#2E5BFF` | `#2450D8` | 5.2:1 to 6.5:1 |
| G08 | Sky to navy | `#348FDD` | `#1B2A55` | 3.4:1 to 13.9:1 |
| G09 | Signal blue to indigo | `#2B46A0` | `#3B2A8C` | 8.4:1 to 11.1:1 |
| G10 | Coral to magenta | `#E5432F` | `#C81E78` | 4.1:1 to 5.4:1 |
| G11 | Emerald to teal | `#0B8F63` | `#0F766E` | 4.1:1 to 5.5:1 |
| G12 | Tangerine to coral | `#D9600A` | `#E5432F` | 3.7:1 to 4.1:1 |
| G13 | Violet to electric blue | `#7B3FE4` | `#2E5BFF` | 5.2:1 to 5.7:1 |
| G14 | Magenta to violet | `#D6247A` | `#6B2FD6` | 4.8:1 to 7.0:1 |

G05 to G09 are the blue gradients, shown on the board after G01 (signal blue to cobalt, the owner's current
favorite) as the reference; G10 to G14 are the vibrant gradients. All are social candidates only.

## Notes

- At 16 px the band's ends turn down, so with the head above it the figure can read as a frowning face,
  most of all on dark, where the cut-outs show the dark ground. The owner's reading is a person, a smile or a
  bowl; worth looking at in the tab previews before choosing.
- The thumbnail tile is the same warm paper (`#F4F1E8`) for every option so only the mark changes. Real
  article thumbnails follow the thumbnail rules (black or white lockup on a bold ground).
