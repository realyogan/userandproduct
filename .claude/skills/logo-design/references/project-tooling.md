# Project Tooling (userandproduct.com)

The tools on this machine that turn the skill's advice ("convert text to paths", "use boolean operations", "check it at 16 px") into commands. Paths are relative to the project root `C:\xampp\htdocs\user-and-product`.

## Installed Tools

| Tool | Version | Job | How to call |
|------|---------|-----|-------------|
| fontTools | 4.66.0 | Read font outlines, write them as SVG path data | `from fontTools.ttLib import TTFont` |
| uharfbuzz | 0.56.2 (HarfBuzz 14.5.0) | Shape text: kerning, ligatures, glyph positions | `import uharfbuzz as hb` |
| skia-pathops | 0.9.2 | True path booleans and overlap removal (Chrome's engine) | `import pathops` |
| resvg-py | 0.5.0 | Render SVG to PNG, very accurate | `import resvg_py` |
| Pillow | 12.3.0 | Compose PNG tiles, write `.ico` | `from PIL import Image` |
| SVGO | 4.1.0 | Final optimization of shipped SVGs | `npx svgo@4.1.0 in.svg -o out.svg` (no global install) |

Full install record: `research/mockups/tooling-installed-2026-10-09.md`.

## Fonts

Static TTFs in `research/mockups/fonts/<family>/`, each with its licence file beside it. All SIL Open Font License 1.1.

| Folder | Files | Character |
|--------|-------|-----------|
| `geist/` | Bold, SemiBold, Regular | Swiss neo-grotesque; cool, exact, technical |
| `inter/` | Inter Display Bold, SemiBold, Regular | Neutral grotesque tuned for large sizes |
| `space-grotesk/` | Bold, Regular | Quirky geometric grotesque from a monospace |
| `instrument-sans/` | Bold, Regular | Compact contemporary grotesque; editorial |
| `fraunces/` | 72pt SemiBold, 72pt Regular | Soft old-style display serif; warm, bookish |
| `bricolage-grotesque/` | Bold, Regular | Grotesque with ink traps; characterful |

**OFL and logos.** The OFL FAQ (question 1.1) allows logos made from the outlines. The outlined artwork is yours; no credit is required; conditions apply only when the font file itself is redistributed or modified. An outlined font is **not exclusive**: anyone can set the same word in the same face. For a mark worth registering, customize a few letters (a cut terminal, a joined pair, a distinctive "a") after outlining.

To add a font: take the static file from the family's official GitHub release or the `google/fonts` repo, and copy its `OFL.txt` next to it. For a variable font, pin an instance first:

```bash
fonttools varLib.instancer Font[wght].ttf wght=650 -o Font-650.ttf
```

## wordmark.py: Text to Paths

`research/mockups/tools/wordmark.py`. Shapes with HarfBuzz (falls back to advance widths, no kerning, if uharfbuzz is missing), writes a clean SVG: one `<path>` per part, viewBox fitted to the ink plus a margin, no `width`/`height`, `fill="currentColor"`, no `<text>`. Prints the ink bounds.

```bash
# one path
python research/mockups/tools/wordmark.py --font research/mockups/fonts/geist/Geist-Bold.ttf \
  --text "userandproduct" --out wm.svg

# three paths (ids wm-user, wm-and, wm-product; classes wm-user ...), "and" lighter and red
python research/mockups/tools/wordmark.py --font research/mockups/fonts/geist/Geist-Bold.ttf \
  --split "user|and|product" --highlight and \
  --alt-font research/mockups/fonts/geist/Geist-Regular.ttf --accent "#B3141C" --out wm.svg
```

| Option | Effect |
|--------|--------|
| `--size 100` | One em = 100 output units (keeps coordinates small) |
| `--tracking 60` | Extra spacing in 1/1000 em, the same for 1000- and 2048-unit fonts |
| `--split "a\|b\|c"` | One path per part, with `id` and `class`, so CSS can colour one part |
| `--highlight and` | Parts that take `--alt-font` and/or `--accent` |
| `--fill` / `--accent` | Fixed colours instead of `currentColor` (for light and dark files) |
| `--id-prefix` | Keep ids unique when several SVGs are inlined on one page |
| `--merge` | Union overlapping contours with skia-pathops before hand editing |
| `--weight-note` | Adds a comment with font name, weight class and version |

**Hand tuning.** Kern a pair by nudging later parts: shape once, read the printed bounds, then edit the path or re-run with a different `--tracking`. For booleans between a mark and the wordmark, see the skia-pathops snippet below.

## Booleans with skia-pathops

```python
import pathops
from fontTools.svgLib.path import parse_path
from fontTools.pens.svgPathPen import SVGPathPen
a, b = pathops.Path(), pathops.Path()
parse_path(d_mark, a.getPen()); parse_path(d_word, b.getPen())
merged = pathops.op(a, b, pathops.PathOp.UNION)   # DIFFERENCE, INTERSECTION, XOR
pen = SVGPathPen(None); merged.draw(pen); print(pen.getCommands())
```

## render.py: Look at Every Draft

`research/mockups/tools/render.py` renders with resvg. `currentColor` becomes `--color` first (a standalone render has no parent colour).

```bash
python research/mockups/tools/render.py wm.svg --sizes 16,32,180,512           # widths, aspect kept
python research/mockups/tools/render.py mark.svg --sizes 16,32 --square --pad 1  # fitted in a square
python research/mockups/tools/render.py wm.svg --sizes 1200 --background "#ffffff" --color "#111111"
```

Writes `<stem>-<size>.png` beside the SVG (or in `--out-dir`). Read the 16 px PNG before showing a favicon.

## brand_assets.py: Icon and Social Files

`research/mockups/tools/brand_assets.py` takes the master mark (the simplified symbol or one letter, not the full wordmark) and writes eight files:

| File | Notes |
|------|-------|
| `favicon.svg` | `currentColor` fixed to `--svg-color`, with a `prefers-color-scheme: dark` rule to `--dark-color` |
| `favicon-16.png`, `favicon-32.png` | Mark on a `--bg` tile, so it reads in light and dark tabs |
| `favicon.ico` | 16, 32, 48 in one file (Pillow) |
| `apple-touch-icon-180.png` | Solid background, 20 px padding, no transparency |
| `icon-512.png` | WordPress Site Icon and web manifest |
| `og-1200x630.png` | Placeholder only: mark centred on `--og-bg`. Lay out the real one as an SVG and use render.py |
| `avatar-400.png` | LinkedIn and profile avatar, 80 px margin |

```bash
python research/mockups/tools/brand_assets.py mark.svg out/ --bg "#111111" --color "#ffffff"
```

## Type Board

`research/mockups/logos/typeboard/index.html` (http://localhost/user-and-product/research/mockups/logos/typeboard/) sets the name in all six fonts: 560 px on white and near-black, red and blue accents on "and", 32 px and 16 px, uppercase and tracked. Rebuild with `python research/mockups/tools/build_typeboard.py`. Add a font by adding an entry to `CANDIDATES` in that script.

## SVGO Before Shipping

SVGO 4 keeps `viewBox` by default. Keep ids when CSS targets them (`cleanupIds: false`, see [optimization.md](optimization.md)), and check that `role="img"` and `<title>` survive. Shipped coordinates at `--size 100` are already two decimals; SVGO's path compaction roughly halves the file.

## Pitfalls

| Don't | Do instead |
|-------|-----------|
| Ship a wordmark made with `<text>` and a web font | Run wordmark.py; the logo must not depend on a font loading |
| Use the accent hex as-is on near-black | Lift it for dark (`#B3141C` to about `#F0676C`, `#1F3FBF` to about `#8EA2FF`) |
| Judge a favicon from the SVG in the editor | Render 16 and 32 px with render.py and look at the PNG |
| Inline several split SVGs with the same ids | Use `--id-prefix`, or strip ids and style the classes |
| Take fonts from mirror sites | Official GitHub release or `google/fonts`, licence file beside the font |
