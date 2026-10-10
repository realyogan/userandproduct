# Blog thumbnail references

Shared by the owner on 9 Oct 2026 as references for our article thumbnails and hero images (35 images,
ref-01 to ref-35, from Tiger Data's blog; ref-23 to ref-35 added later the same evening). Internal reference only, never for reuse. The owner will add
more.

What they have in common, noted for the illustration rules:
- One flat, saturated background per image: red-orange, near-black, acid yellow, violet, blue, teal, with
  a dot grid, a fine square grid, or a halftone texture over it.
- One subject, drawn in a halftone or pixel style (dithered photo, pixel icon, flat vector with a hard
  shadow), centred or placed with a lot of breathing room.
- Monospace or pixel type when there is text: a short title, sometimes a label or a number.
- The brand mark in a corner on some, not all.
- 16:9, no frames except an occasional thin inner rule or a dark inset panel.

Second batch (ref-23 to ref-35) adds two more kinds:
- Flat vector illustrations on a grained grid: pale shapes with hard black drop shadows on orange or
  acid yellow (a magnifier over a ledger, icons on a conveyor, an elephant on a chart, a numbered cycle
  of icons, a robot by a chat box). Same palette, softer than the halftone ones.
- Dark diagram thumbnails: near-black with thin white lines and one accent (a cloud of databases, a
  tangle of cards sorted into a grid, a sync loop, a numbered pipeline, a ranked list). These are
  explainer diagrams used as thumbnails, which is how the two styles meet.

Note (owner, 9 Oct): the grained background comes in two variants, a square grid and a dot grid, both over the
grain. Treat them as a choice in the thumbnail rules, not one texture.

## Gallery (decided styles)

`gallery.html` (http://localhost/user-and-product/research/mockups/references/blog-thumbnails/gallery.html) shows
the styles decided on 9 Oct 2026: ten made with code and one used only when the owner supplies a photo (eleven in
all; the character-drawing style is dropped). Each is drawn by `research/mockups/tools/thumbnail.py` on a sample
subject from our field. Rebuild with `python build_gallery.py`; files in `gallery/`.

Decisions recorded with it (owner, 9 Oct):
- The style is chosen by fit first: the article's kind (how-to, opinion, concept, comparison, list, data, tool,
  story, series) limits the choice to the styles that suit it, then the rotation runs among those.
- Colour is free per image, not the explainer palette: one bold, high-contrast background (red-orange, acid yellow,
  violet, electric blue, teal, near-black and others), "contrast and curiosity, not clickbait". Schemes: mono by
  default, duo when one element must stand out, trio rarely, analogous for calm; accents only on the thing that
  matters and checked to 3:1. Neighbours differ by style and by background.
- The brand is the full lockup, mark and wordmark (white or black by contrast), on every image, hero and thumb,
  at the same share of the width on both, about a fifth: 220 px wide on the 1200 hero, 120 px wide on the 600
  thumb. The thumb is the hero at half size, so the logo looks the same wherever the image is shown. The hero's
  size is the legibility anchor (shown about 720 px wide, the wordmark's x-height is about 7.8 px). Owner, 9 Oct:
  "make sure to use full logo, not only the icon"; the hero lockup is "perfect", the earlier 240 px thumb lockup
  was far too large.
- Particles come in two styles: on near-black (9) and on a saturated ground (10). The photo style is 11.
- Styles 7 and 9 are shown in colour (owner, 9 Oct): the glow diagram on midnight with a yellow glow, the
  particle field on night with a lime stream. In 9 and 10 the stream carries the accent, as in ref-07.
