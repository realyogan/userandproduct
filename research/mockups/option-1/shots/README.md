# Variant A at ten viewports (10 October 2026)

Screenshots of the top 1200 px of `article.html` (variant A), light and dark, named `a-<width>x<height>-<theme>.png`.
Made and measured with `../build/shots_article.py` (run `python shots_article.py` from `research/mockups/option-1/build/`
while XAMPP serves the page). The `article-*-375*.png` files are the thumbnails on the variants page
(`../build/variants/index.html`). The `home-<width>-<theme>.png` files are full-page shots of the home page from
`../build/shots_home.py`.

Widths are rendered pixels. The reading column is the `.main` track; running text inside it is capped at 35 em
(630 px at 18 px, about 70 characters a line). "Rail list" is the longest title in the compact
"More in Product discovery" list, in lines. "Ads in view" is the most ad units in any one screen while scrolling
(the phone anchor counts as always in view).

| Viewport | Left rail px | Reading column px | Right rail px | Result |
|---|---|---|---|---|
| 375 × 812 | none | 343 | none | Pass. No overflow. Contents in the disclosure, rail hidden. Ads in view 2; in-page ad density 5.0% of the page, anchor 10.3% of the screen. |
| 768 × 1024 | none | 688 | none | Pass. No overflow. Text 630 px. Ads in view 1. |
| 1024 × 768 | 240 | 672 | none (block after the body, 672) | Pass. No overflow. Text 630 px. The list (340 px, titles 2 lines) sits beside a 300 × 250 after the body. Left rail stops at the body end. Ads in view 1. |
| 1280 × 720 | 200 | 636 | 300 | Pass. No overflow. Text 630 px. Titles 2 lines. Both sticky blocks stop at the body end. Ads in view 2. |
| 1280 × 800 | 200 | 636 | 300 | Pass. Same as 1280 × 720. |
| 1366 × 768 | 200 | 720 | 300 | Pass. No overflow. Text 630 px. Titles 2 lines. Gap 33 px. Ads in view 2. |
| 1440 × 900 | 244 | 720 | 300 | Pass. No overflow. Gap 48 px. Titles 2 lines. Ads in view 2. |
| 1536 × 864 | 244 | 720 | 300 | Pass. Container capped at 1440, centred. |
| 1680 × 1050 | 244 | 720 | 300 | Pass. Same as 1536. |
| 1920 × 1080 | 244 | 720 | 300 | Pass. Same as 1536. |

Also checked without screenshots: 1100 and 1199 (240 / 720, block after the body), 1200 to 1279
(no left rail, contents in the disclosure, reading column 720, rail 300), 1359 (200 / 636 / 300) and 1360 (200 / 716 / 300).
No horizontal scroll at any of them.

## Why the left rail folds below 1280

The content box is the viewport (capped at 1280 px, 1440 px from 1360) minus two 40 px gutters.
Three columns at their minimums need 200 + 560 + 300 + 2 × 32 = 1124 px.
At 1200 the box is 1120 px, so they cannot fit; at 1280 it is 1200 px, which leaves the reading column 636 px.
From 1204 to 1279 they would just fit, but the reading column would be 560 to 635 px, under the 630 px
text measure for most of that range, so the fold happens at 1280 rather than at the first width where the sum works.
