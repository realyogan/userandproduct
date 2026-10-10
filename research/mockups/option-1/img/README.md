# Images for option 1

The home page and the article share this folder. The article's images (hero, figures, Related and rail thumbnails
in `thumbs/`, the explainer gallery's `explainers/`) come from `../build/build_images.py`, `../build/figures.py` and
`../build/explainers.py`. The rest of this note is about the home page thumbnails.

## Home page thumbnails

Made with `research/mockups/tools/thumbnail.py` by `../build/build_home.py` (run `python build_home.py` in `option-1/build/`). The titles are
made-up samples for the mockup, so the history file was not written. Thumb size, 600 x 338, with the 120 px lockup;
the featured piece also has its 1200 x 675 hero. The same PNGs serve the light and the dark page. Every check passed.

Styles were chosen fit-first (only the styles that suit the piece's kind), then rotated by hand across the page so no
two neighbours share a style or a colour family: the featured card and its two secondary cards, and the 3 x 3 grid
row by row and column by column. Mono by default; duo only where one part must stand out or a dark style needs it.

| Place | File | Kind | Suitable styles | Style | Ground and scheme | Why |
|---|---|---|---|---|---|---|
| featured | `prd-engineers-read-thumb.png` | howto | 1, 3, 4, 2 | 1 Flat vector, square grid | red-orange (#FF5A36), mono | a how-to with one nameable object, the document; the flat cut-out reads largest at hero size |
| secondary 1 | `usability-test-size-thumb.png` | concept | 1, 6, 3, 9, 7, 10, 2, 8 | 6 Dark line diagram | night (#16151A), mono | a concept about sample size; the dark line diagram sets it apart from the bright featured card |
| secondary 2 | `retention-truth-thumb.png` | data | 6, 9, 7, 10, 8 | 8 Light grid diagram | paper (#F4F1E8), duo blue | a data piece; the light grid diagram with one accent on the flat part of the curve, unlike the dark card above it |
| grid 1 | `price-before-customers-thumb.png` | howto | 1, 3, 4, 2 | 3 Pixel icon and panel | acid-yellow (#E9FF3B), duo indigo | a how-to; the pixel icon suits a practical method and opens the grid on a bright ground |
| grid 2 | `roadmap-sales-call-thumb.png` | opinion | 1, 7, 5, 2 | 5 Typographic cover | violet (#6B4CFF), mono | an opinion piece; the typographic cover carries a judgment, deep violet beside the yellow |
| grid 3 | `dashboard-one-question-thumb.png` | opinion | 1, 7, 5, 2 | 1 Flat vector, square grid | tangerine (#FF8A1F), mono | an opinion piece about one object, the gauge; the flat square-grid style on a warm ground |
| grid 4 | `information-architecture-growth-thumb.png` | concept | 1, 6, 3, 9, 7, 10, 2, 8 | 9 Particle field | midnight (#121A3A), duo yellow | an abstract concept about scale; the particle field, the stream in the accent |
| grid 5 | `kanban-or-scrum-thumb.png` | comparison | 1, 6, 2, 8 | 2 Flat vector, dot grid | teal (#14B8A6), mono | a comparison drawn as the sprint loop; the dot-grid flat style, cool bright between two deep grounds |
| grid 6 | `product-manager-week-thumb.png` | concept | 1, 6, 3, 9, 7, 10, 2, 8 | 7 Dark glow diagram | night (#16151A), duo lime | a concept with one key idea; the glow diagram, the bulb glowing in the accent |
| grid 7 | `accessibility-afternoon-thumb.png` | list | 1, 4, 10, 2 | 4 Icon sequence | hot-pink (#FF5CA8), mono | a list of four real checks; the icon sequence numbers them |
| grid 8 | `design-tokens-thumb.png` | concept | 1, 6, 3, 9, 7, 10, 2, 8 | 10 Bright particle field | electric-blue (#2F5BFF), duo yellow | an abstract concept, many small values becoming one system; the bright particle field |
| grid 9 | `first-product-designer-thumb.png` | howto | 1, 3, 4, 2 | 1 Flat vector, square grid | mint (#3DDC84), mono | a how-to with one object, the briefcase; flat square grid on mint, apart from the dark and blue neighbours |

Notes:

- Grid 1 uses the Pixelarticons `money` glyph: the default `coins` glyph read as a blob at 300 px.
- Grid 2 (style 5) carries the short cover line "The roadmap meets sales", the only image with words in it.
- `recipes.json` holds the same table as data; each PNG also carries its recipe in a text chunk.
