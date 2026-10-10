# userandproduct logo pack 2

The final logo for userandproduct.com, decided by the owner on 10 Oct 2026: the owner's own mark from
`../Logo-3/` (a solid disc with a head and a curved band cut out of it, drawn in Illustrator) in option
C17, Electric blue, flat, with the name "userandproduct" in Inter Display Bold.

Brand sheet: http://localhost/user-and-product/research/mockups/final-logo-2/brand-sheet.html

The previous pack (the four-tile Signal mark, 9 Oct 2026) stays in `../final-logo/` for reference.

## Why

The owner judged the four-tile mark bland and drew a mark of his own: a person (head and shoulders) that also
reads as a smile or a bowl. Logo 3 put it through twenty-two flat colours and fourteen gradients, and the owner
chose C17. What the choice gives: the disc passes on white (5.2:1), its lighter partner passes on near-black, and
the blue carries a white figure on avatars and app icons.

## Colours

| Token | Hex | Use | Contrast (WCAG 2) |
|-------|-----|-----|-------------------|
| Electric blue | `#2E5BFF` | the disc on light backgrounds; the ground of the social set and app icons | 5.2:1 on `#FFFFFF` |
| Electric blue, dark mode | `#7DB0FF` | the disc on dark backgrounds | 8.6:1 on `#111111` (8.9:1 on the site's `#0B0B0C`) |
| White | `#FFFFFF` | the figure where the mark is opaque (avatars, app icons); one-colour white | 5.2:1 on electric blue |
| Ink | `#0B0B0C` | the wordmark on light; one-colour black | 19.7:1 on `#FFFFFF` |
| Off-white | `#F1EEE7` | the wordmark on dark | 17.0:1 on `#0B0B0C` |
| Near-black | `#111111` | the ground of the dark social set | |

3:1 is the bar for a graphic. The light disc on near-black is only 3.6:1, which is why dark mode switches to
`#7DB0FF`. Where the mark sits on a page the head and band are true holes (`fill-rule="evenodd"`), so the
background shows through; where the mark is opaque (avatars, app icons, PNG favicons, `mark-solid.svg`) they are
filled white. The build recomputes every figure.

## Geometry

Wordmark: "userandproduct", Inter Display Bold, lowercase, tracking 0, kerned, outlined to one path. Units are
the wordmark's own, 100 per em: cap height 72.75, x-height 51.56.

- Side lockup: the disc is 1.4 cap heights across (101.9 units), its centre midway between the cap height and the
  x-height (31.08 units above the baseline), the gap 0.40 of the disc (40.7 units), 4 units of margin. viewBox
  `-4 -86 885.6 110.4`.
- Stacked lockup: the disc 3 cap heights across, centred over the name, gap 0.76 cap heights, 4 units of margin.
- On the site: header 236 px wide, footer 168 px wide.
- Clear space: x, the height of the head cut-out (28 percent of the disc), on every side of the mark.
- Minimum size: 24 px across the disc. The favicon files are the one exception (drawn for 16 and 32 px tabs).
- Never recoloured outside the two blues, black and white; never with gradients on the site.

The mark geometry is the owner's, verbatim: `build.py` reads `../Logo-3/svg/mark.svg` (the clean master, one
compound path, the circle as four quarter arcs) and refuses to run if it no longer matches `../Logo-3/geo.py`,
which also supplies the wordmark outline and the lockup placement. The mark SVGs keep the owner's 1920 canvas.

## Contents

- `svg/`: `mark`, `mark-dark`, `mark-black`, `mark-white`, `mark-currentcolor` (takes the text colour),
  `mark-solid` (white figure), `lockup-light`, `lockup-dark`, `lockup-black`, `lockup-white`, `stacked-light`,
  `stacked-dark`, `stacked-black`, `stacked-white`. Clean SVG: viewBox, no width or height, no live text,
  explicit fills, all under 5 KB.
- `png/`: transparent `mark-light` and `mark-dark` at 64, 128, 256, 512 and 1024; `lockup-light` and
  `lockup-dark` at 236, 472 and 944 wide; `stacked-light` and `stacked-dark` at 400 and 800 wide; flattened
  one-colour files: `lockup-black-on-white-944`, `lockup-white-on-black-944`, `stacked-black-on-white-800`,
  `stacked-white-on-black-800`, `mark-black-on-white-1024`, `mark-white-on-black-1024`.
- `favicon/`: `favicon.svg` (the figure empty, a dark-mode media query switches the disc to `#7DB0FF`),
  `favicon.ico` (16, 32, 48), `favicon-16/32/48/96/192/512.png` (the disc edge to edge, the figure white, each
  rendered at its own size), `apple-touch-icon-180.png` (opaque square), `maskable-512.png` (the figure scaled to
  0.83 to sit inside the safe circle), `site.webmanifest`, `head-snippet.html`.
- `social/`: electric blue with the white figure: `instagram-avatar-1080` (circle-safe: the avatar is the disc
  colour as a full square, so the platform's circle crop shows the disc exactly), `linkedin-logo-300` and `-400`,
  `x-avatar-400`, `linkedin-banner-1128x191` (white lockup 52 px tall, centred on 42 percent of the width, clear of
  the logo overlap), `og-1200x630` (white lockup 760 px wide, centred), `x-header-1500x500` (white lockup 84 px
  tall, centred). The dark set, the same names with `-dark`: near-black ground, the dark-mode disc with the figure
  showing the ground, 15 percent margin on the avatars; the banners carry `lockup-dark`.
- `brand-sheet.html`: everything above, light and dark (it follows the system theme and has the theme toggle; it
  is built on the shared tokens in `../mockup.css`).
- `build.py` (writes everything), `check.py` (checks), `status.py` (progress page updates).

## Rebuild

```
python build.py
python check.py
```

Needs Python 3 with fontTools, uharfbuzz, skia-pathops, resvg-py and Pillow, plus `../Logo-3/geo.py`,
`../tools/wordmark.py` and `../fonts/inter/`. `check.py` also needs Playwright with Chrome and XAMPP serving.
It checks: the masters carry the owner's path verbatim and, in black, render the same as the owner's file at 512
and 1920 px (within one gray level along the cut-out edges); every SVG is valid, has a viewBox and no fixed size,
no live text, and is under 6 KB; every PNG and ICO is at its size; the contrast figures; option-1 carries the new
lockups and favicons byte for byte; the brand sheet and the option-1 pages answer 200; no broken images and no
horizontal overflow at 375 and 1280 px in light and dark; the header lockup is 236 px and the footer 168 px.

After a rebuild, copy `svg/lockup-light.svg`, `svg/lockup-dark.svg`, `favicon/favicon.svg`, `favicon/favicon.ico`
and `favicon/apple-touch-icon-180.png` into `../option-1/assets/` (`logo/` and `favicon/`); `check.py` fails until
they match.

## Where it is used

- `../option-1/assets/logo/` and `../option-1/assets/favicon/`: the same file names as before, so every page picks
  them up with no HTML change. The `.logo img` aspect ratio in `option-1/css/mockup.css` and `../mockup.css` is set
  to the new viewBox (885.6 / 110.4).
- `../tools/thumbnail.py` and the thumbnail-images skill: the lockup on article thumbnails comes from `svg/`
  (`lockup-white.svg` or `lockup-black.svg`, by contrast with the background).

## Licence

The wordmark is drawn from Inter Display Bold, under the SIL Open Font License 1.1 (licence file in
`../fonts/inter/`). The OFL allows logos made from the outlines and requires no credit. The mark is the owner's
own drawing.
