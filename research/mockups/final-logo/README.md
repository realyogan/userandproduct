# userandproduct logo pack

The final logo for userandproduct.com, decided 2026-10-09: the Signal mark (four filled tiles of two sizes,
rotated 45 degrees) with the name "userandproduct" in Inter Display Bold, lowercase, tracking 0
(the typeface as designed).

Lockup geometry: the mark is 1.4 cap heights tall, centred midway between the cap band and the x-height
band (mark centre 31.08 units above the baseline at 100 units per em; cap height 72.75, x-height 51.56),
with a gap of 0.40 of the mark height (40.74 units). Both set on 9 Oct 2026 after the comparison in
`alignment.html`; tracking 0 chosen the same day (was -25). `python build.py --align cap|xheight|mid
--gap <fraction> --tracking <n>` rebuilds other variants.

Open the brand sheet: http://localhost/user-and-product/research/mockups/final-logo/brand-sheet.html

## Contents

- `svg/`: masters. Lockup (light, dark, black, white), stacked lockup (light, dark), mark (light, dark,
  black, white), wordmark (black, white), and `mark-currentcolor.svg` for inline use. Clean SVG: viewBox,
  no width or height, no live text, explicit fills.
- `png/`: every master on a transparent background (lockups and wordmarks 1200 and 2400 wide, stacked
  1200 and 2400 square, marks 256, 512 and 1024), plus the lockup on solid white and near-black at 2400.
- `favicon/`: `favicon.svg` (switches to the dark blue in dark themes), 16, 32 and 48 pixel PNGs,
  `favicon.ico` (16, 32, 48), Apple touch icon, 192 and 512 icons, a maskable 512 icon,
  `site.webmanifest` and `head-snippet.html` with the tags for the theme.
- `social/`: Open Graph images (light, dark), LinkedIn banners (light, dark), avatars (light, dark),
  an X header, and the site header strip (light, dark).
- `brand-sheet.html`: usage guide with colour, clear space, minimum sizes and a file index.
- `build.py`: the one source script.

## Rebuild

```
python build.py
```

Needs Python 3 with fontTools, uharfbuzz, skia-pathops, resvg-py and Pillow, plus
`research/mockups/tools/` (wordmark.py, render.py, brand_assets.py) and `research/mockups/fonts/inter/`.
The mark's path data is embedded in build.py. The script validates its own output.

## Colour tokens

| Token | Hex | Contrast |
|-------|-----|----------|
| Signal blue, light (mark) | `#2B46A0` | 8.4:1 on `#FFFFFF` |
| Signal blue, dark (mark) | `#8EA2FF` | 8.2:1 on `#0B0B0C` |
| Ink (wordmark, light) | `#0B0B0C` | 19.7:1 on `#FFFFFF` |
| Off-white (wordmark, dark) | `#F1EEE7` | 17.0:1 on `#0B0B0C` |
| Background, light | `#FFFFFF` | |
| Background, dark | `#0B0B0C` | |

## Licence

The wordmark is drawn from Inter Display Bold, under the SIL Open Font License 1.1 (licence file in
`research/mockups/fonts/inter/`). The OFL allows logos made from the outlines and requires no credit; its
conditions apply only when the font file itself is shared. The outlined name is not exclusive.
