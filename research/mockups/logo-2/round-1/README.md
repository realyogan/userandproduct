# Logo exploration 2, round 1: ten marks with weight

Board: http://localhost/user-and-product/research/mockups/logo-2/round-1/
Hub (all rounds): http://localhost/user-and-product/research/mockups/logo-2/hub.html

## Brief (owner, 10 October 2026)

The current four-tile mark is "bland": no presence, unattractive as an Instagram icon, "a speck of dust" on its
own. The owner's reference (a stock mark, a thick ring crossed by a cursor, saved in
`research/discussion/references/logo-round-2/`) has what ours lacks, and only its qualities are kept, never its idea:

1. Authority and trust first: a serious publication a professional would cite; never a toy, a game or a consumer app.
2. Mass: thick strokes or solid forms, no thin lines, no scattered small parts.
3. One idea, with a small beat that makes someone say "oh nice".
4. A two-tone fold where two forms overlap.
5. App-icon feel: a filled circle or rounded square that is part of the mark; a few ideas stand free for comparison.
6. Judged first as a 110 px avatar (circle and rounded square) and a 32 px favicon, on white and near-black.
7. Blue by default (signal blue #2B46A0 kept as one tone), three ideas also in another colour.

Letterforms and monograms are not in this round; they are round 2 (`../round-2/`).

## The ten ideas

| # | Name | Container | Colour |
|---|---|---|---|
| R1-01 | The orbit: a thick ring with one heavy moon, the overlap pale | stands free | blue |
| R1-02 | The completed frame: a screen frame whose missing corner is the user's disc | rounded square | blue, also coral |
| R1-03 | The key person: a key whose bow and guard are a head and shoulders | circle | blue |
| R1-04 | The folder bust: an open folder that is also a person behind the flap | rounded square | blue |
| R1-05 | The breakout rocket: the nose leaves the tile and changes tone at the edge | rounded square (inset) | blue |
| R1-06 | The passenger rocket: the porthole is the user, the flame the second tone | circle | blue |
| R1-07 | The switch: a heavy track and a knob wider than it, switched on | stands free | blue, also teal |
| R1-08 | The nib: the author's pen, the slit folds it into a lit and a shaded face | circle | blue, also oxblood |
| R1-09 | The bookmark: a ribbon folded over the top of a page | stands free | blue |
| R1-10 | The clasp: two open hooks that only hold where they overlap | circle | blue |

Each idea's one-line reason, construction note, authority check and nearest existing logos are on the board and in
`build/ideas.py`.

## Files

- `svg/`: per idea `r1-NN-mark-light.svg`, `-mark-dark.svg` (512 master), `-lockup-light.svg`, `-lockup-dark.svg`
  (header lockup with the current Inter Display Bold wordmark, same geometry as the final pack), `-thumb.svg`
  (600 x 338 tile with the one-colour lockup at 120 px), and `-alt-mark-*.svg` for the alternative colours.
- `png/`: the avatar renders at 110 px (circle and rounded square, light and dark), favicons at 32 px, thumbs at 600.
- `build/`: `marks.py` (geometry, booleans with skia-pathops), `ideas.py` (the words), `build.py` (files and
  renders), `board.py` (the page), `checks.py` (valid SVG, under 6 KB, thin-part test), `status.py` (progress page).

## Rebuild

```
cd research/mockups/logo-2/round-1/build
python build.py
python checks.py
```

Needs Python 3 with fontTools, skia-pathops, resvg-py and Pillow, `research/mockups/tools/render.py`, the wordmark
in `research/mockups/final-logo/svg/wordmark-black.svg`, and `npx` for the SVGO 4.1.0 pass (skipped if missing).
