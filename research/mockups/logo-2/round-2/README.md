# Logo exploration 2, round 2: letterform marks

Board: http://localhost/user-and-product/research/mockups/logo-2/round-2/ (back link to the hub at `../hub.html`).

## Brief (owner, 10 Oct 2026)

Ten letterform marks from U, D and P, to replace the four-tile Signal mark (bland, without presence). The owner
said "U and D"; the name is user and product, so U with D and U with P are both in scope, and the ampersand may
join them.

Priority: authority and trust first (a serious publication a professional would cite), then character, then the
qualities from the owner's reference (`research/discussion/references/logo-round-2/`): mass, one idea, a two-tone
fold where forms overlap, an app-icon feel (most contained in or shaped as a filled circle or rounded square, a few
standing free for comparison), recognisable at 32 px. No thin strokes, no gradients, no cartoon. Signal blue as one
tone with a lighter fold tone; two of the ten in an alternative colour.

## The ten

| No. | Name | Letters | Holder | Colour |
|-----|------|---------|--------|--------|
| R2-01 | Shared stem | U and D on one stem | Rounded square | Blue |
| R2-02 | Turned U | a U on its side becomes a D | Circle | Blue |
| R2-03 | Split ring | u below, p above, one counter | Circle | Blue |
| R2-04 | D holds U | solid D, U cut out | Shaped as the icon | Blue |
| R2-05 | Cut coin | U cut from a disc | Circle | Blue |
| R2-06 | Two hooks | U from two tones only | Stands free | Deep green (alternative) |
| R2-07 | Stack | U over P | Stands free | Blue |
| R2-08 | Lit D | reversed-out D | Rounded square | Blue |
| R2-09 | Ampersand | & with a P loop and a U bowl | Circle | Vermilion (alternative) |
| R2-10 | Folded u | the name, first u dog-eared | Stands free (wordmark-forward) | Blue |

The idea, the "oh nice" reason, the authority check, the construction and the closest existing logos for each
are on the board and in `info.py`.

Decided while drawing: a P made of a bar and a disc was dropped (too near Patreon), and so was a solid P made of a
bar and a half-disc (too near Pandora). R2-06 became the two-hook U instead. R2-10 proposes one type change: the
first u of the Inter Display Bold wordmark gets a folded corner on its right stem; nothing else in the name changes.

## Colours

| Role | Light | Dark |
|------|-------|------|
| Container (blue) | `#2B46A0` signal blue | `#3653C4` |
| Letter on a container | `#FFFFFF`, second tone `#8EA2FF`, fold `#C9D3FF` | same |
| Free-standing marks | `#2B46A0`, `#4D6CF0`, fold `#9DB2FF` | `#5B77EE`, `#9AAEFF`, fold `#DCE2FF` |
| Deep green (R2-06) | `#0E5A49`, `#1F9277`, fold `#7FD6BA` | `#2A9A7E`, `#5FC7A6`, fold `#C3EFE0` |
| Vermilion (R2-09) | container `#B8321C`, `#FF9C84`, fold `#FFD0C3` | container `#CF3E25` |

Folds are real shapes (the boolean intersection of the two forms), never opacity or blend modes.

## Files

- `svg/r2-NN-*.svg`, per mark: `mark` and `mark-dark` (512 masters), `avatar-circle`, `avatar-square` and their
  `-dark` versions, `lockup` and `lockup-dark` (with the Inter Display Bold wordmark, final-logo geometry: mark 1.4
  cap heights tall, gap 0.40 of the mark), `lockup-white` and `lockup-black` (one colour, for thumbnails). Paths
  only: no text, raster, filters, gradients, masks or strokes.
- `png/r2-NN-32-light.png`, `-32-dark.png`, `-16-light.png`, `-16-dark.png`: favicons rendered at size on white
  and near-black. `png/r2-NN-thumb.png`: 600 x 338 tile (saved at 2x) with the lockup 120 px wide, 20 px in,
  bottom-left, white or black at 92 percent, as the thumbnail rules say.
- `marks.py` (the geometry), `geo.py` (shapes and booleans), `info.py` (the words), `board.py` (the page),
  `build.py` (writes everything), `check.py` (the checks), `status.py` (the progress page writer for this run).

## Rebuild

```
python build.py
python check.py
```

Needs Python 3 with fontTools, uharfbuzz, skia-pathops, resvg-py and Pillow, and
`research/mockups/fonts/inter/InterDisplay-Bold.ttf`. `check.py` confirms every SVG parses, is under 6 KB and uses
paths only; scans each colour region of every master for any part narrower than 8 units at 512; confirms the 32 px
favicons; and compares the marks' silhouettes and letter shapes so no two share a core shape.

## Check results (10 Oct 2026)

- 100 SVGs, all valid, largest 4,977 bytes (a lockup); masters 0.6 to 1.4 KB.
- Nothing narrower than 8 units at 512.
- All ten read at 32 px. R2-07 Stack is the weakest there (tall and narrow); R2-10's folded corner is only faint at
  32 px, gone at 16 px, and lost in the one-colour thumb lockup at 120 px.
- Letter shapes inside the containers: the most similar pair is R2-01 and R2-08 (0.59 intersection over union),
  then R2-02 and R2-03 (0.58); no pair shares a core shape.
- Old exploration checked by eye (the archived hub, its b-monogram and the type board): nothing repeated. The
  nearest old pieces were the U-and-P-bowl monogram, the stacked "up" tiles and the "u&p" disc; none of the ten
  uses those constructions.
