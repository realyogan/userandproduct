---
name: thumbnail-images
description: House rules and generator for every article thumbnail, cover, hero and social image on userandproduct.com. Use this skill whenever a thumbnail, cover image, hero image, featured image, card image, social or Open Graph (OG) image is requested for an article, guide, template page or any page, even for a single piece or a quick placeholder, and whenever the owner says "thumbnail", "cover image", "hero image", "featured image", "OG image", "social image" or "make the image for this post". Covers the eleven styles (ten code-drawn plus a photo style used only when the owner supplies a photo), choosing a style by the article's kind and then the rotation, bold backgrounds and restrained colour schemes, the lockup, drawing with research/mockups/tools/thumbnail.py, the checks, file names and the banned list. Not for explainer figures inside an article (those follow research/mockups/illustration-rules.md).
---

# Thumbnail images for userandproduct.com

Every article gets one image that works as its thumbnail (cards, Related rows, archives) and its hero
(top of the article, social share). It is drawn by code in one of eleven styles, on one bold background,
with our full lockup, mark and wordmark, in a corner. The same file serves the light and the dark theme.

## Contrast and curiosity, not clickbait

A thumbnail has to stand out next to its neighbours and make a reader curious, and it has to promise
the real content, never a trick. One subject, one bold background, at most one or two accents. The test:
would a reader scanning a list stop on it, and does the article deliver what the image hints at? A PRD
article shows a PRD; it never shows a shocked face, a fake notification or a number the article does
not contain.

## The eleven styles

Full specs, the kind-to-style table and the references each style comes from are in
`references/styles.md`. Read it the first time you draw a style.

| # | Style | Ground | Suits |
|---|---|---|---|
| 1 | Flat vector, hard shadows, **square** grid + grain | bright | almost anything with one nameable object |
| 2 | Flat vector, hard shadows, **dot** grid + grain | bright | same as 1; the grid differs |
| 3 | Pixel icon in a pixel window | bright | tools, templates, technical concepts |
| 4 | Icon sequence: 3 to 5 numbered icons on a track | bright | lists, steps, series (not opinion, not one concept) |
| 5 | Typographic cover: short title in pixel type + one object | near-black or deep | opinion and judgment pieces, announcements, series |
| 6 | Dark line diagram | near-black | data, systems, comparisons |
| 7 | Dark glow diagram, the glow in the accent | near-black | one key idea or result |
| 8 | Light grid diagram | pale paper | data, structure, comparisons |
| 9 | Particle field, the stream in the accent | near-black | flows, scale, abstract concepts |
| 10 | Bright particle field, the stream in the accent | saturated (acid yellow, red-orange, electric blue) | the same, louder |
| 11 | Halftone or dithered photo (**only with the owner's photo**) | bright | stories and cases |

## Choosing the style: fit first, then the rotation

1. **Classify the article's kind** from its title and subject: how-to, opinion, concept, comparison,
   list, data, tool, story or series. The generator does this (`classify_kind`) from the title; pass
   `kind` when you know better.
2. **Keep only the styles that suit that kind** (`suitable_styles(kind)`; table in
   `references/styles.md`).
3. **Run the rotation among those** (`ROTATION = [1, 6, 3, 9, 4, 7, 10, 5, 2, 8]`, by publish index or a
   slug hash), skipping the previous piece's style and preferring one not used in the last three.
4. **Record the kind, the candidates and the pick with a one-line reason.** The generator returns them
   and stores them in `research/mockups/thumbnail-history.json` and in the PNG.

A supplied photo selects style 11. A writer may override the style with a reason
(`{"style": 6, "reason": "series on metrics uses the dark diagram"}`); "I like it better" is not one.

## Colour

**Backgrounds** are chosen freely per image: saturated and high-contrast, in the spirit of the
references (red-orange, acid yellow, violet, electric blue, teal, near-black). Twelve suggestions are
in `references/styles.md`; any background whose ink passes 4.5:1 is allowed. The generator picks a
suggested background suited to the style when none is given, and avoids the last three backgrounds used,
so neighbours differ by colour as well as by style. An article keeps its colours on a re-render.

**Schemes**: restraint first. If in doubt, use fewer colours.

- **mono** (the default): background and ink only.
- **duo**: one accent near the complement of the background, when one element must stand out.
- **trio**: two accents (triadic, else split-complementary), only when two things are compared, and rarely.
- **analogous**: one accent from a neighbouring hue, for a calmer look.

Accents mark only the thing that matters most: the active icon in a sequence, the ticked boxes, the one
point on a chart, the highlighted panel, the glow. The rest stays in ink. An accent covers at most about
a fifth of the subject. Never colour decoration (grid, grain, shadows, flow lines, the lockup), except
the particle stream of styles 9 and 10 (below). Every
accent is computed to pass 3:1 against the background (4.5:1 when it colours type). When a wheel
position fails, the hue is turned until it passes, else the image falls back to mono. Two accents at
most. On mid-bright grounds such as red-orange this makes accents deep (a deep cyan, a deep green);
that is the rule working, not a fault. The generator alternates mono and duo by default; trio and
analogous are chosen by hand.

**Two styles where the colour is the point.** On the dark styles a white-only image reads as unfinished,
so prefer duo there:

- **Style 7 (glow)**: in duo the soft bloom behind the subject and the glowing part are in the accent;
  the other lines stay white with their halo. In trio a second element glows in the second accent (in the
  matrix: the winning dot in accent 1, the axis arrows in accent 2) and the bloom splits into two offset
  glows, one per accent. Use trio only when the second accent does not outshine the first.
- **Styles 9 and 10 (particles)**: the one exception to "never colour decoration". As in ref-07, the
  stream is the colour: in duo it carries the accent, fading from the accent at the shape to white (9) or
  the ink (10) at the far left, and the silhouette is white or ink; in trio the stream is in accent 1 and
  the silhouette in accent 2; mono is all white or ink.

## The brand

Every image, hero and thumb, carries the **full lockup**, mark and wordmark (`lockup-white.svg` or
`lockup-black.svg` from `research/mockups/final-logo-2/svg/`, whichever contrasts with the background), at
92% opacity, in the first corner that is clear of the subject on both sizes. It takes the same share
of the width on both sizes, about a fifth, so the thumb is the hero at half size and the logo looks the
same wherever the image is shown:

- **Hero** (1200 x 675): 220 px wide, 40 px in from the edges. This is the size to judge by: shown
  about 720 px wide on the article, the wordmark's small letters are about 7.8 px tall.
- **Thumb** (600 x 338): 120 px wide, 20 px in from the edges. That is a fifth of its width, a touch
  above the hero's share.

It is never over the subject, and it is always black or white, never an accent. If no corner is clear,
move or shrink the subject, never the lockup.

## The photo style (11)

Only when the owner supplies a photo. Owner's photos first (workshops, whiteboards, sticky notes,
sketches, devices). If the owner asks for stock, use Unsplash or Pexels; check the rights line on
Library of Congress items; avoid Wikimedia CC BY-SA. No recognisable faces without consent, no brand
logos. Before drawing, prepare a copy: crop to the subject, paint out logos, legible text and dates, and
thicken lines thinner than the dot screen's 11-unit cell. Keep the original. Record source, author and
licence for any photo that is not the owner's. Terms in `references/sources.md`.

## Per-article workflow

1. **Brief in one line**: who the piece is for and what it promises.
2. **Pick the subject as one noun** from the title, using `references/subjects.md` (library subject or
   `icon:<phosphor-name>`).
3. **Let the generator choose the style** from the kind and the rotation, unless a photo was supplied or
   there is a reason to override.
4. **Draw**:
   ```bash
   python research/mockups/tools/thumbnail.py --slug prd-engineers-read \
     --title "How to Write a PRD That Engineers Actually Read" --subject prd --out <dir>
   # options: --index N  --kind K  --cover-title "..." (style 5)  --steps a,b,c (style 4)  --photo p.jpg
   #          --palette NAME | --bg HEX   --scheme mono|duo|trio|analogous   --style N --reason "..."
   python research/mockups/tools/thumbnail.py --rotation 1    # the kind-to-style table
   python research/mockups/tools/thumbnail.py --palettes      # suggested backgrounds and their duo accent
   ```
5. **Files**: `<slug>-hero.png` (1200 x 675) and `<slug>-thumb.png` (600 x 338), both with the full
   lockup, `<slug>.svg` (the hero's vector source, without grain) and `<slug>-check-300.png`.
6. **Run the checks**: the result's `checks.pass` must be true (subject reads at 300 px on both sizes,
   type and lockup contrast, and `lockup_clear`: the lockup of both sizes is clear of the subject). Then open the 300 px check image and ask: can I name the subject in one
   word? One subject, with room around it? Lockup clear of it? Accent only on the thing that matters?
7. **Same file in both themes.** On the page: `<img>` with `width` and `height`, `loading="lazy"` for
   thumbnails, an `alt` that names the subject.
8. **Report** the kind, the candidates, the style, the background and scheme, and any fall.

## The quality bar

- One subject, with breathing room: about 72 units inside the edges, the lockup corner clear.
- Reads at 300 px. If it does not, simplify; never add detail.
- No frame, border or inner rule. No text except style 5's title and style 4's step numbers.
- The lockup quiet but readable; the colour on the subject, not around it.

## When a style cannot carry the subject

Style 4 needs three to five real steps; style 5 needs a short title; style 3 needs a pixel glyph that
reads; a background must suit the style. Then the generator **falls to the next suitable style** and
returns a note such as `"style 4 cannot carry it (needs a sequence of 3 to 5 steps); fell to style 1"`.
Say so in your reply. Never force a weak picture to keep the rotation tidy.

## Banned

- Clickbait: shocked faces, fake notifications, arrows at nothing, numbers the article lacks.
- The stock-photo look: smiling people at laptops, handshakes, glossy 3D renders.
- Gradients, except style 7's soft glow (one bloom, or two in a trio).
- Clip-art, or mixing icon sets in one image.
- More than one subject; more than two accents; accent on decoration (except the particle stream) or
  on the logo; the logo without its wordmark.
- Text over the subject, or baked-in headlines (except style 5), dates or prices.

## Files and pointers

- Generator: `research/mockups/tools/thumbnail.py` (styles, kinds, colour schemes, lockup, checks).
- Gallery of all eleven styles: http://localhost/user-and-product/research/mockups/references/blog-thumbnails/gallery.html
  (rebuilt by `research/mockups/references/blog-thumbnails/build_gallery.py`).
- Reference board: http://localhost/user-and-product/research/mockups/references/blog-thumbnails/index.html
- Icons: `research/mockups/vendor/` (Pixelarticons and Phosphor, MIT). Font: Space Grotesk Bold in
  `research/mockups/fonts/space-grotesk/`. Logo: `research/mockups/final-logo-2/svg/`.
- `references/styles.md`: the eleven specs, kinds, backgrounds, schemes and the restraint examples.
  `references/subjects.md`: subjects. `references/sources.md`: icon sets, fonts and photo sources.
