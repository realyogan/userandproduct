# SVG tooling installed (2026-10-09)

Implements the recommendation in [tooling-research-2026-10-09.md](tooling-research-2026-10-09.md).
Python 3.12.10, Node 22.19.0, Windows 11.

## Packages

| Package | Version | State | Location |
|---|---|---|---|
| resvg-py | 0.5.0 | Installed now, user-level | `%APPDATA%\Python\Python312\site-packages` |
| skia-pathops | 0.9.2 | Already present (system site-packages), so pip left it | `...\Programs\Python\Python312\Lib\site-packages` |
| uharfbuzz | 0.56.2 (bundles HarfBuzz 14.5.0) | Already present, as above | as above |
| fontTools | 4.66.0 | Already present | as above |
| Pillow | 12.3.0 | Already present (used for .ico and tiles) | as above |
| SVGO | 4.1.0 | Not installed; runs through npx (cached by npm on first use) | npm cache |

Commands used:

```bash
python -m pip install --user resvg-py skia-pathops uharfbuzz
python -m pip show resvg-py skia-pathops uharfbuzz fonttools pillow
python -c "import resvg_py, pathops, uharfbuzz, fontTools, PIL; print(pathops.__version__, uharfbuzz.__version__, uharfbuzz.version_string(), fontTools.version, PIL.__version__)"
python -c "import resvg_py; print(len(resvg_py.svg_to_bytes(svg_string='<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 10 10\"><rect width=\"10\" height=\"10\"/></svg>', width=16, height=16)))"
npx --yes svgo@4.1.0 --version        # 4.1.0
npx --yes svgo@4.1.0 in.svg -o out.svg  # tested on a type board SVG: 5.6 KB to 3.1 KB, viewBox kept
```

## Fonts

In [fonts/](fonts/), static TTFs with the licence file beside each family. All SIL Open Font License 1.1.
Fetched one request per second from the official sources.

| Family | Files | Licence file | Source |
|---|---|---|---|
| Geist 1.800 | Geist-Bold, -SemiBold, -Regular | `geist/OFL.txt` | https://github.com/vercel/geist-font/releases/download/v1.7.2/geist-font-v1.7.2.zip |
| Inter Display 4.001 | InterDisplay-Bold, -SemiBold, -Regular | `inter/LICENSE.txt` (OFL) | https://github.com/rsms/inter/releases/download/v4.1/Inter-4.1.zip (`extras/ttf/`) |
| Space Grotesk 2.000 | SpaceGrotesk-Bold, -Regular | `space-grotesk/OFL.txt` | https://github.com/floriankarsten/space-grotesk/releases/download/2.0.0/SpaceGrotesk-2.0.0.zip (`ttf/static/`) |
| Instrument Sans 1.000 | InstrumentSans-Bold, -Regular | `instrument-sans/OFL.txt` | https://raw.githubusercontent.com/Instrument/instrument-sans/master/fonts/ttf/ (no GitHub release exists) |
| Fraunces 1.000 (72pt optical size) | Fraunces72pt-SemiBold, -Regular | `fraunces/OFL.txt` (from the repo root; the zip has none) | https://github.com/undercasetype/Fraunces/releases/download/1.000/UnderCaseType_Fraunces_1.000.zip (`Fonts - Desktop/static/ttf/`) |
| Bricolage Grotesque 1.001 | BricolageGrotesque-Bold, -Regular | `bricolage-grotesque/OFL.txt` | https://raw.githubusercontent.com/ateliertriay/bricolage/main/fonts/ttf/ |

The sixth pick is Bricolage Grotesque: a grotesque with ink traps and a big x-height, the most
characterful of the options, and a clear contrast to the cooler Geist and Inter. The default (not the
12pt or 96pt) optical cut is used; the 96pt cut is in the same repo if a more exaggerated display
version is wanted.

## Tools

In [tools/](tools/), standard library plus the packages above:

- `wordmark.py`: text to a single-path (or `--split` three-path) SVG, HarfBuzz kerning, fallback to
  advance widths (tested by hiding uharfbuzz).
- `render.py`: SVG to PNG at given widths, or fitted in a square.
- `brand_assets.py`: master mark to favicon.svg, favicon-16/32.png, favicon.ico (16, 32, 48),
  apple-touch-icon-180.png, icon-512.png, og-1200x630.png, avatar-400.png. Tested end to end.
- `build_typeboard.py`: rebuilds [logos/typeboard/](logos/typeboard/) (36 SVGs plus index.html).
