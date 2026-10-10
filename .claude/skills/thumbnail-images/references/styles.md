# The eleven thumbnail styles

Canvas units are the 1200 x 675 canvas. Ink is #1D1B16 (or white on dark and deep grounds, whichever
contrasts more), card is #FDFCF8. Reference images are in `research/mockups/references/blog-thumbnails/`
(`ref-NN.png`). Generator: `research/mockups/tools/thumbnail.py`.

Contents: kinds · backgrounds · schemes and restraint · shared finish · styles 1 to 11

## Which styles suit which kind of article

The generator classifies the kind from the title (`classify_kind`), keeps only the suitable styles,
then runs the rotation `[1, 6, 3, 9, 4, 7, 10, 5, 2, 8]` among them, skipping the previous piece's
style and preferring one not used in the last three.

| Kind | Suitable styles (rotation order) | Not suitable, and why |
|---|---|---|
| How-to or procedure | 1, 3, 4, 2 | 5 (a title is not a method), dark diagrams (too abstract) |
| Judgment or opinion | 1, 7, 5, 2 | 4 (a sequence implies steps), 3, 8 (too neutral) |
| Concept explainer | 1, 6, 3, 9, 7, 10, 2, 8 | 4 (one idea, not a list), 5 |
| Comparison | 1, 6, 2, 8 | 4, 9, 10 (no two sides to see) |
| List or sequence | 1, 4, 10, 2 | 5, 7 (one idea, not many) |
| Data or metrics | 6, 9, 7, 10, 8 | 1 to 4 (paper cut-outs undersell data) |
| Tool or template page | 1, 3, 2 | dark diagrams, particles (not concrete enough) |
| Story or case | 1, 5, 2 (11 with the owner's photo) | 4, diagrams (a story is not a system) |
| Series piece | 1, 4, 5, 2 | dark diagrams unless the series is about data |

Each style's own line (what it suits and what it does not) is in its section below; the table is the
union. A writer may override with a reason; the generator records kind, candidates, pick and reason.

## Suggested backgrounds and their duo accent

Suggestions only: **any background whose ink passes 4.5:1 is allowed**, and any accent that passes 3:1
(4.5:1 if it colours type). The duo accent below is what the generator computes at the complement; the
trio and analogous accents are computed the same way (`python thumbnail.py --palettes`).

| Name | Background | Kind (styles) | Ink | Duo accent | Trio accents | Analogous |
|---|---|---|---|---|---|---|
| red-orange | #FF5A36 | bright (1-4, 10, 11) | #1D1B16 5.5:1 | #004B5C deep cyan 3.1:1 | #00520F deep green + #2900E6 indigo | #574200 deep yellow |
| acid-yellow | #E9FF3B | bright | #1D1B16 15.4:1 | #1D00FF indigo 7.5:1 | #009AAD cyan + #FA00DD magenta | #309E00 deep green |
| tangerine | #FF8A1F | bright | #1D1B16 7.3:1 | #0058A8 blue 3.0:1 | #006631 deep green + #7000EB violet | #565C00 deep yellow |
| teal | #14B8A6 | bright | #1D1B16 6.9:1 | #A61222 red 3.1:1 | #8D119C magenta + #5C530A deep yellow | #105493 deep blue |
| hot-pink | #FF5CA8 | bright | #1D1B16 6.0:1 | #00572E deep green 3.1:1 | #265200 deep green + #004799 deep blue | #991200 deep red |
| mint | #3DDC84 | bright | #1D1B16 9.6:1 | #C3227B magenta 3.1:1 | #7626D9 violet + #A1571C orange | #157275 deep teal |
| violet | #6B4CFF | deep (5, 10) | #FFFFFF 5.1:1 | #D3FF00 lime 4.4:1 (turned for type) | #FFB7A8 pale red + #00FF2C green | #ECB2FF pale violet |
| electric-blue | #2F5BFF | deep (5, 10) | #FFFFFF 5.2:1 | #FFC900 yellow 3.4:1 | #FFB2C3 pale pink + #36FF00 green | #D5BDFF pale violet |
| night | #16151A | dark (5, 6, 7, 9) | #FFFFFF 18.2:1 | #B5D926 lime 11.2:1 | #D94A26 red + #26D94A green | #B226D9 violet |
| night-plum | #1C1426 | dark | #FFFFFF 17.8:1 | #89D926 lime 10.2:1 | #D97626 orange + #26D976 green | #D926D4 magenta |
| midnight | #121A3A | dark | #FFFFFF 17.0:1 | #D9B526 yellow 8.6:1 | #D9264A pink + #4AD926 green | #7F44DE violet |
| paper | #F4F1E8 | paper (8) | #1D1B16 15.2:1 | #2653D9 blue 5.6:1 | #1B9C7C teal + #AC26D9 violet | #6F981B lime |

On mid-bright grounds (red-orange, teal, hot-pink, mint) a 3:1 accent has to be deep, because no light
colour can reach 3:1 there. That is intended: the deep accent reads as a confident second ink.

## Schemes and restraint

- **mono** is the default: background and ink. With no accent, the accent role falls back to card
  white (or white on dark grounds), so the subject reads in ink alone.
- **duo** when one element must stand out. **trio** only when two things are compared, and rarely.
  **analogous** for a calmer single accent.
- An accent covers at most about a fifth of the subject's area. Never colour the grid, grain, shadows,
  flow lines or the lockup. If in doubt, fewer colours.
- **The exception: the particle stream (styles 9 and 10).** In ref-07 the stream is the colour, so there
  it carries the accent, fading to white or the ink at the far left. Nowhere else does decoration take an
  accent.
- **On the dark styles prefer duo.** A white-only glow or particle image reads as unfinished; one accent
  makes it. Use trio there only when the second accent does not outshine the first.
- HSL helper in the generator: `complement`, `split`, `triad`, `analogous`, `rotate`, and
  `nudge_for_contrast` (raises saturation and moves lightness away from the background until the
  check passes; turns the hue in 10-degree steps when a position cannot pass; mono if nothing does).

**Too much** (red-orange, duo): the PRD's header band, every checkbox, the badge, the flow lines and the
shadow all in the accent. The eye has nowhere to land, and the accent becomes a second background.

**Right amount** (red-orange, duo): the PRD in card white and ink; only the two ticked boxes and the
approval badge in deep cyan. The accent says "decided", which is what the article is about. The
references do the same: ref-10 (one teal gear among pale ones), ref-20 (one white disc on a black
drum), ref-33 (one blue arrow among white lines), ref-01 (one halftone object, no accent at all).

## Shared finish

- Export 1200 x 675 (hero) and 600 x 338 (thumb), both with the full lockup, both downsampled
  from a 2400-wide render. The SVG source is the hero without grain.
- Grain: monochrome Gaussian noise after the downsample, seed from the slug (sigma 10 on bright flat
  styles, 4 to 7 on others, none on 3, 8 and 11).
- Brand: the full lockup, mark and wordmark (`research/mockups/final-logo-2/svg/lockup-white.svg` or
  `lockup-black.svg`, the owner's disc mark), white or black by contrast at 92%, in the first corner
  (bottom-right, bottom-left, top-right, top-left) clear of the subject on both sizes. Same share of
  the width on both sizes, about a fifth, so the thumb is the hero at half size and the logo looks the
  same wherever the image is shown (`LOCKUP_PX` in the generator):
  - hero: 220 px wide (18%), 40 px in. The legibility anchor: shown about 720 px wide, the wordmark's
    x-height (5.9% of the lockup's width) is about 7.8 px (13 px in the file);
  - thumb: 120 px wide (20%, a touch above the hero's share), 20 px in.
  If no corner is clear, `checks.lockup_clear` is false: move or shrink the subject, never the lockup.
  The mark's head and band are true holes in the pack files, so the lockup is always the solid one-colour
  variant (or `mark-solid.svg` for a lone mark), and the generator fills the holes with the flat background
  colour at full opacity under the lockup: no grid line, dot or particle runs through the figure.
- Subject about 72 units inside the edges.

## 1. Flat vector, square grid

- **Ground**: a bright background (dark ink). **Texture**: square grid every 60 units, ink 2 units at
  10%; grain sigma 10.
- **Subject**: one object from rectangles, circles and paths: card-white fills, 4-unit ink outline,
  round joins; text-line bars stand for words. The accent only on the part that matters.
- **Shadow**: the shape again in solid ink, 14 units down-right. **Flow lines**: three ink lines from
  the left edge meeting the subject.
- **Suits**: almost anything with one nameable object. **Not**: data pieces.
- **References**: ref-10, ref-17, ref-18 (= ref-19), ref-20, ref-21, ref-22, ref-23, ref-29, ref-30.

## 2. Flat vector, dot grid

- As style 1 with a dot grid (every 30 units, radius 2.4, ink at 17%). The owner's note: the grained
  grid comes in two variants, square and dot; they are separate styles so the grid alternates.
- **References**: the same ten as style 1; the board groups both grids together.

## 3. Pixel icon and panel

- **Ground**: bright, with a dot grid (24 units, ink at 15%); no grain.
- **Subject**: a Pixelarticons glyph on whole 14-unit cells inside a pixel window (40 x 32 cells, ink
  outline, title bar with three cell buttons, pixel text lines). Enclosed areas get a checker of the
  accent and card white (mono: card and ink). One-cell ink shadow; two pixel sparks.
- **Suits**: tools, templates, technical concepts, how-tos. **Not**: opinion, data, stories.
- **Cannot carry**: subjects with no glyph that reads at 24 x 24.
- **References**: ref-05, ref-12, ref-14, ref-15, ref-16.

## 4. Icon sequence

- **Ground**: bright, grain, square or dot grid.
- **Subject**: three to five Phosphor regular icons on card-white discs (radius 86, or 74 for five),
  3.5-unit ink outline, 12-unit ink shadow; the active step's disc in the accent. A rounded track with
  rivets underneath.
- **Type**: step numbers in Space Grotesk Bold, card white on small ink discs (16.8:1).
- **Suits**: lists, steps, series. **Not**: opinion pieces or a single concept.
- **Cannot carry**: subjects without 3 to 5 real steps.
- **References**: ref-24, ref-25 (the same image as ref-28).

## 5. Typographic cover

- **Ground**: near-black or a deep saturated background (white ink), with a faint dot grid.
- **Type**: the short title (`cover_title`, else the title when short) in pixel type: Space Grotesk Bold
  set at 15 to 18 px, thresholded and drawn as 5 to 8-unit cells, up to three lines, left-aligned at
  x 96. Colour: the accent if it passes 4.5:1, else the ink. Long titles fall back to set type (44 to
  64 units); over 48 characters the style cannot carry it.
- **Object**: one Pixelarticons glyph on 12-unit cells to the right.
- **Suits**: opinion and judgment pieces, announcements, series covers, stories. **Not**: how-tos, data.
- **References**: ref-02, ref-04, ref-08 (and the pixel numerals of ref-07).

## 6. Dark line diagram

- **Ground**: near-black or midnight, white dot grid at 8%; grain 4.
- **Subject**: line mode: white lines at 86%, 3.6 units, no fills; the part that matters in the accent
  with a 16% fill (mono: white). Two faint flow lines.
- **Suits**: data, systems, comparisons, concepts. **Not**: how-tos, stories.
- **References**: ref-03, ref-27, ref-35.

## 7. Dark glow diagram

- **Ground**: near-black or midnight with one soft radial glow behind the subject, the only gradient
  allowed in any style. Duo: the glow in the accent. Trio: two offset glows, one in each accent, blending
  in the middle. Mono: a faint white glow.
- **Subject**: line mode with a 4-unit halo on every white line; the accented part glows in its colour
  (duo: the one part that matters, such as the matrix's winning dot). Trio adds a second element in the
  second accent (the matrix's axis arrows). Prefer duo; the gallery sample is midnight duo, a yellow dot
  and bloom, because on midnight the trio's red and green outshone the winning dot.
- **Suits**: one key idea or result, concepts, data, opinion. **Not**: lists, procedures.
- **References**: ref-32, ref-33, ref-34.

## 8. Light grid diagram

- **Ground**: pale paper, square grid every 50 units (ink 1.5 units at 7%), sparse dark specks.
- **Subject**: line mode in ink at 90%, 3.6 units; the part that matters in the accent, which must reach
  3:1 on the paper. Faint ink lines run in from the left.
- **Suits**: data, structure, comparisons, concepts. **Not**: opinion, stories.
- **References**: ref-31.

## 9. Particle field

- **Ground**: near-black or midnight; grain 4.
- **Subject**: the subject's Phosphor fill silhouette (330 units) on the right, filled with dots on a
  jittered 7-unit lattice. From the left edge, 64 streams of dots converge on it, denser and more opaque
  near the shape. The stream carries the colour, as in ref-07:
  - duo (and analogous): the stream in the accent at the shape end, fading to white at the far left;
    the silhouette white;
  - trio: the stream in accent 1 (same fade), the silhouette in accent 2;
  - mono: stream and silhouette white.
  Night with a lime stream is the suggested pair (the gallery sample).
- **Suits**: flows, scale, abstract concepts, data. **Not**: how-tos, tools, stories.
- **References**: ref-07.

## 10. Bright particle field

- **Ground**: a saturated bright or deep background: acid yellow, red-orange, electric blue, violet;
  grain 7.
- **Subject**: as style 9, with the ink in place of white (deep ink on bright grounds, white on deep
  ones): duo, the stream in the accent fading to the ink at the far left and the silhouette in the ink;
  trio, the stream in accent 1 and the silhouette in accent 2; mono, all in the ink.
- On mid-bright grounds (red-orange, teal, hot-pink, mint) the accents are deep 3:1 colours, and a trio
  puts both stream and silhouette in them: the dots then fall under 3:1 at 300 px and the check fails.
  Use duo there; trio suits the deep grounds (violet, electric blue) and acid yellow.
- **Suits**: flows, scale, abstract concepts, data, lists of many things. **Not**: stories, tools.
- **References**: ref-07, recoloured onto the bright grounds of the flat-vector set.

## 11. Halftone photo (conditional)

- **Only when the owner supplies a photo.**
- **Ground**: bright, with an ink dot grid at 12%.
- **Subject**: the photo, greyscale and auto-contrasted, fitted into 760 x 540 units, as a 45-degree ink
  dot screen (11-unit cells), or with `photo_method: "bayer"` an 8 x 8 Bayer dither to three levels
  (ground, a mid ink, ink). A superellipse feather dissolves the edges: no frame. Mono by nature.
- **Suits**: stories and cases, real work. **Not**: abstract concepts.
- **References**: ref-01, ref-06, ref-09, ref-11, ref-13 (and the dithered photo panel of ref-04).
