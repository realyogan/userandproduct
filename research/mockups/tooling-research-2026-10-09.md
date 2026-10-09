# Logo and illustration tooling research (2026-10-09)

Question from the owner: are there skills, tools or services, for Claude Code or local, that would help
draw better SVG logos and illustrations for userandproduct.com?

## Recommendation (install now, in this order)

1. **Nothing to install for real typefaces as paths.** fontTools 4.66 is already on this machine. The
   20-line script in section 2 turns any open-licence font into a single SVG `<path>` and was tested
   here with Instrument Sans Bold ("User and Product", 5 KB). This ends the hand-built-letterform era:
   wordmarks can now be set in Geist, Inter, Instrument Sans, Fraunces and so on, then tuned by hand.
2. **`pip install resvg-py skia-pathops uharfbuzz`** (all have Windows wheels, no build step).
   resvg-py renders SVG to PNG so every logo draft can be looked at as a picture at 16, 32, 180 and
   512 px, and it is the engine for the favicon pipeline (section 5). skia-pathops does true boolean
   union, subtract and intersect on paths, so a mark and a wordmark (or overlapping glyphs) merge into
   one clean outline. uharfbuzz adds proper kerning to the font-to-path script.
3. **SVGO through npx** (`npx svgo@4.1.0 in.svg -o out.svg`). Node is already installed, so there is
   nothing global to add; npx downloads it on first use. Final optimization of every shipped SVG.
4. **Optional later: Inkscape 1.4.4** (`winget install Inkscape.Inkscape`). A large desktop app, but
   its command line does text-to-path, booleans and PNG export in one tool, and the owner can open any
   draft and nudge nodes by hand. Worth it once a direction is chosen and needs hand polish.

No Claude Code skill found adds enough over the installed `logo-design` skill to be worth installing.
The gap in that skill is not knowledge, it is tools: it says "convert text to paths" and "use boolean
operations" but gives no way to do either on this machine. Rather than add a skill, add a short
`references/font-outlines.md` to the existing skill pointing at the section 2 script and the
section 3 boolean and render commands.

For illustrations: hand-written SVG via the skill for diagrams and spot art, one icon set (Lucide or
Phosphor) inlined as SVG, and no stock illustration library (they read as startup clip art, which works
against the authority goal). Local image generation is not realistic on this machine.

---

## 1. Claude Code skills and plugins

What is installed: `.claude/skills/logo-design` (SKILL.md, about 1,800 words, plus 8 references:
path-patterns, logo-techniques, icon-design, advanced-techniques, animation, optimization,
accessibility-and-pitfalls, editing-workflow; about 8,300 words in all). It covers process, path
syntax, grids, negative space, compound-path "booleans" via fill rules, SVGO config, animation and
accessibility. It does not cover: getting real font outlines, true path booleans, or rendering drafts
to PNG for review.

| Skill | What it does | Type | Licence / updated | Verdict |
|---|---|---|---|---|
| anthropics/skills `canvas-design` | Writes a "design philosophy", then makes a poster or art piece as PNG/PDF | Instructions + about 80 bundled font files | Apache 2.0 for most skills (see each LICENSE.txt); repo last commit 2026-10-05 | **No** as a skill (PNG/PDF art, not SVG logos). **Yes as a font source**: its `canvas-fonts/` folder holds OFL fonts with licence files (Instrument Sans and Serif, Work Sans, Bricolage Grotesque, Crimson Pro, IBM Plex Serif, Young Serif, Gloock, Lora, Libre Baskerville, Outfit, Geist Mono, JetBrains Mono and more), ready for the section 2 script |
| anthropics/skills `algorithmic-art` | p5.js generative art with seeded randomness | Instructions + HTML/JS templates | Apache 2.0 | **No** for logos. Maybe later for generative article headers, but it needs a JS runtime in the page |
| anthropics/skills `brand-guidelines`, `theme-factory` | Apply Anthropic's own brand, or preset font and color themes | Instructions | Apache 2.0 | **No**: another company's brand, and slide presets. Generic SVG icon and diagram skills on the registries (svg-icon-generator, svg-precision-skill, svg-diagrams) are also **no**: thinner versions of the installed skill |
| anthropics/skills `frontend-design` | Distinctive UI and typography direction | Instructions | Apache 2.0 | Already available here; **yes** for the HTML mockup phase, not for the logo |
| discountry/ritmex-skills `svg-logo-maker` (listed on claudskills.com) | Minimalist SVG logos with svg.js, browser visual checks, SVG export | Instructions, needs svg.js and a browser | Licence not stated on the listing; updated 2026-06-13 | **No**: overlaps the installed skill and adds a JS dependency. Its one good idea, render and look at every draft, is covered by resvg-py |
| `opentype-js` skill (skills.sh, openskillindex) | Read fonts, measure text, convert to SVG paths with opentype.js | Instructions + `npm install` | Per source repo | **Maybe**: same job as the fontTools script, in Node. Python is simpler here because fontTools is already installed |
| oaustegard/claude-skills `image-to-svg` | Traces raster images into SVG via OpenCV color quantization | Instructions + Python scripts | MIT; updated 2026-10-08 | **No**: written for a Linux sandbox (`apt-get`, `/mnt/skills` paths) and for reproducing existing pictures, not making original marks |

Install method for any of them, if ever wanted: copy the skill folder (SKILL.md plus its files) to
`.claude/skills/<name>/` in this project. No marketplace step is needed.

Sources: https://github.com/anthropics/skills ,
https://claudskills.com/skills/svg-logo-maker/ ,
https://www.skills.sh/terminalskills/skills/opentype-js ,
https://vibeindex.ai/skills/oaustegard/claude-skills/image-to-svg ,
https://mcp.directory/blog/claude-svg-precision-skill-guide

## 2. Real typefaces as paths

**Recommended: fontTools (Python), already installed (4.66.0).** No app, no network, exact outlines,
scriptable, so drafts can be regenerated in seconds with a different font, weight or tracking.

Get a font: download the static TTF from Google Fonts (fonts.google.com, "Get font", unzip, use the
`static/` file for the weight you want) or from the project's GitHub (Geist: github.com/vercel/geist-font).
Keep the OFL.txt next to it in `research/mockups/fonts/`.

Tested script (`wordmark.py`), output verified on this machine:

```python
# Usage: python wordmark.py Font.ttf "User and Product" out.svg [tracking_units]
import sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

font_path, text, out = sys.argv[1], sys.argv[2], sys.argv[3]
tracking = int(sys.argv[4]) if len(sys.argv) > 4 else 0
font = TTFont(font_path)
glyphs, cmap = font.getGlyphSet(), font.getBestCmap()
pen, bounds, x = SVGPathPen(glyphs), BoundsPen(glyphs), 0
for ch in text:
    name = cmap[ord(ch)]
    # font units are y-up, SVG is y-down: flip y and move to the pen position
    glyphs[name].draw(TransformPen(pen, (1, 0, 0, -1, x, 0)))
    glyphs[name].draw(TransformPen(bounds, (1, 0, 0, -1, x, 0)))
    x += glyphs[name].width + tracking
x0, y0, x1, y1 = bounds.bounds
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0:.0f} {y0:.0f} {x1-x0:.0f} {y1-y0:.0f}" '
       f'role="img" aria-label="{text}"><path fill="currentColor" d="{pen.getCommands()}"/></svg>')
open(out, "w", encoding="utf-8").write(svg)
```

Notes:
- Coordinates come out in font units (usually 1,000 per em), so the viewBox for the full name is
  about 8000 x 730. That is fine; SVGO can round and shrink it afterwards.
- This places glyphs by advance width only, so **no kerning**. For a logo that is often what you want
  (you will hand-tune pairs anyway, by adding per-letter offsets). For automatic kerning and
  ligatures, shape the text first with uharfbuzz (`pip install uharfbuzz`): `hb.shape(font, buf)`
  returns glyph ids and x advances and offsets, which replace the simple `x += width` loop.
- Variable fonts (Fraunces, Inter, Geist): use the static instance files, or pin an instance with
  `fonttools varLib.instancer Font.ttf wght=650 opsz=48 -o Font-650.ttf`. That also allows
  in-between weights, such as 650, which is useful for logo tuning.
- Overlapping contours (common in variable fonts) render fine but look messy when edited. Merge them
  with skia-pathops (section 3) before hand editing.

Alternatives:
- **Inkscape CLI** (after `winget install Inkscape.Inkscape`): write an SVG with a `<text>` element
  using an installed font, then
  `inkscape in.svg --export-text-to-path --export-plain-svg --export-filename=out.svg`.
  Good, but the font must be installed in Windows, and it is a large app for one job.
- **opentype.js** (Node): `font.getPath(text, x, y, size).toPathData()`. Same result as fontTools;
  needs `npm install opentype.js`.

**Licence for logo use.** Geist, Inter, Space Grotesk, Instrument Sans and Fraunces are all under the
SIL Open Font License 1.1, as is almost everything on Google Fonts. The OFL FAQ (question 1.1)
explicitly says yes to creating logos and objects from the outlines. The artwork is yours, credit is
not required, and the licence only applies conditions if you redistribute or modify the font file
itself. One caution: an outlined wordmark is not exclusive. Anyone can set the same words in the same
font, so for a trademarkable logo, customize a few letters (a cut terminal, a joined pair, a
distinctive "&"). A few Google Fonts use the Apache or Ubuntu licence; check the licence file of the
font you pick.

Sources: https://fonttools.readthedocs.io/en/latest/pens/svgPathPen.html ,
https://openfontlicense.org/ofl-faq/ , https://github.com/vercel/geist-font ,
https://github.com/harfbuzz/uharfbuzz

## 3. SVG tools on Windows (no build step)

| Tool | Job | Windows install | Verdict |
|---|---|---|---|
| **SVGO 4.1.0** (Aug 2026, MIT) | Optimize and minify; config already in the logo skill's optimization reference | `npx svgo@4.1.0 in.svg -o out.svg` (Node present) | **Yes** |
| **resvg-py 0.5.0** (Aug 2026) | Render SVG to PNG with the resvg (Rust) renderer, very accurate | `pip install resvg-py` (win_amd64 wheel) | **Yes**: previews, favicons, OG images |
| resvg CLI | Same, as an exe | `resvg-win64.zip` from the v0.47.0 GitHub release (the latest, 0.48.1, ships no Windows zip) | Maybe, if a CLI is preferred |
| **skia-pathops 0.9.2** (BSD-3) | True path booleans (union, difference, intersection, xor) and overlap removal, the same engine Chrome uses | `pip install skia-pathops` | **Yes**: merge mark and wordmark, remove glyph overlaps |
| svgelements 1.9.6 (MIT) | Parse SVG, apply transforms, flatten to absolute paths, bounding boxes | `pip install svgelements` | Maybe: useful when scripting the layout of mark and type |
| picosvg (Google, Apache 2.0) | Flattens any SVG into plain filled paths (no strokes, transforms, clips) | `pip install picosvg` | Maybe: turns stroked drafts into fills before the favicon build |
| Inkscape 1.4.4 (GPL) | Text to path, booleans, PNG export, GUI for hand edits | `winget install Inkscape.Inkscape` | Maybe now, yes later. Union: `inkscape in.svg --actions="select-all;path-union;export-plain-svg;export-filename:out.svg;export-do"`. PNG: `inkscape in.svg --export-type=png --export-width=512 --export-filename=out.png` |
| vtracer 0.6.15 (MIT) | Trace bitmaps (sketches, photos) to color SVG | `pip install vtracer` | Maybe: if the owner sketches a mark on paper and wants a traced starting point |
| cairosvg 2.9.1 | Render SVG to PNG | Needs the Cairo DLL on Windows | **No**: use resvg-py. (Also skipped: potrace, superseded by vtracer; svgpathtools, covered by the two above) |

Boolean union with skia-pathops, the core of it:

```python
import pathops
from fontTools.svgLib.path import parse_path
from fontTools.pens.svgPathPen import SVGPathPen
a, b = pathops.Path(), pathops.Path()
parse_path(d_mark, a.getPen()); parse_path(d_word, b.getPen())   # d strings from the SVGs
merged = pathops.op(a, b, pathops.PathOp.UNION)                  # or DIFFERENCE, INTERSECTION, XOR
pen = SVGPathPen(None); merged.draw(pen); print(pen.getCommands())
# single shape with overlaps: a.simplify()
```

Sources: https://github.com/svg/svgo , https://pypi.org/project/resvg-py/ ,
https://github.com/linebender/resvg/releases , https://pypi.org/project/skia-pathops/ ,
https://github.com/meerk40t/svgelements , https://github.com/googlefonts/picosvg ,
https://pypi.org/project/vtracer/ , https://inkscape.org/doc/inkscape-man.html

## 4. Illustration for the editorial site

| Option | Fit | Why |
|---|---|---|
| **Hand-written SVG via the logo-design skill** | **Yes** | Best for diagrams, frameworks, 2x2s, flows and simple spot illustrations, which is most of what a UX and product article needs. Inline SVG, tiny, themeable with `currentColor`, no dependency. Rule: draw the mechanism, not decoration |
| **Icon set: Lucide** (ISC), **Phosphor** (MIT), **Tabler** (MIT) | **Yes, pick one** | All free for commercial use, no attribution required. Copy individual SVGs into the child theme or inline them; no icon font, no npm. Lucide is the cleanest match for an editorial look; Phosphor has more weights (thin to fill, duotone) if the brand wants a signature style |
| Local image generation (Stable Diffusion, FLUX via ComfyUI) | **No** | This machine has an AMD Radeon RX 5500 XT and 32 GB RAM. Current local models want an NVIDIA card with 12 GB or more of video memory; AMD on Windows is slow and fiddly. Not worth it |
| Hosted generator with real SVG output: **Recraft** (V4/V4.1, 2026) | **Maybe** | Produces editable vector SVG, good for article header art in a consistent style. Free tier has no commercial rights and images are public; paid plans start around 12 USD a month, a vector costs 2 credits. Use for occasional hero images, then clean up with SVGO |
| **unDraw** | No | Free, no attribution, commercial use allowed, but no redistribution in packs and no automated download. The style is the default "SaaS landing page" look; readers will recognize it |
| **Open Doodles** (CC0), **Humaaans** (CC0) | No | Free and public domain, but playful and widely used; wrong register for a practitioner authority site |
| **Streamline free sets** | Maybe | CC BY 4.0 per their free-vectors repo: free commercial use with attribution (a credit line on a colophon page). Large, consistent icon sets; confirm current terms on streamlinehq.com |
| **Blush** | No | Licence page could not be read (blocked); historically the free tier gives small PNGs only and SVG needs a paid plan |

For a no-build WordPress site: inline SVG in the child theme (icons) and SVG for article diagrams.
WordPress blocks SVG uploads by default, so either paste inline SVG in a Custom HTML block or allow
sanitized SVG uploads for administrators only, through the structure plugin.

Sources: https://lucide.dev/license , https://github.com/phosphor-icons/homepage ,
https://github.com/tabler/tabler-icons , https://undraw.co/license , https://www.opendoodles.com ,
https://www.humaaans.com , https://github.com/webalys/streamline-icons ,
https://www.recraft.ai/pricing , https://invideo.io/blog/recraft-ai-image-generator/

## 5. Favicon and brand asset pipeline

What the site needs (the "six files" approach from Evil Martians, still the consensus in 2026):

| File | Size | Notes |
|---|---|---|
| `favicon.ico` | 32x32 (optionally 16, 32, 48 in one file) | Site root, for old browsers, RSS readers, Google's favicon fetcher |
| `icon.svg` | vector | Modern browsers; can carry a `prefers-color-scheme` dark variant inside |
| `apple-touch-icon.png` | 180x180 | Solid background, about 20 px padding, no transparency |
| `icon-192.png`, `icon-512.png` | 192, 512 | Referenced from `manifest.webmanifest` |
| `og-default.png` | 1200x630 | Default social image; Rank Math sets it site-wide, articles override |
| LinkedIn avatar | 400x400 | Company page logo and personal profile both show as a small square or circle; keep the mark centered with margin |
| LinkedIn company cover | 1128x191 | If a company page is made |

WordPress note: the Customizer "Site Icon" takes one 512x512 PNG and outputs 32, 180, 192 and 270 px
PNGs itself, but no SVG and no .ico. So: set the Site Icon from `icon-512.png`, put `favicon.ico` in the
site root, and add `<link rel="icon" type="image/svg+xml" href=".../icon.svg">` from the child theme on
`wp_head`.

One-command pipeline from a master SVG (Python, needs `pip install resvg-py`; Pillow is already
installed; not yet run here, so test once before relying on it):

```python
# Usage: python brand_assets.py mark.svg out/ "#111111"
import io, sys, pathlib, resvg_py
from PIL import Image
src, out, bg = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), sys.argv[3]
out.mkdir(exist_ok=True); svg = src.read_text(encoding="utf-8")
def png(size):
    data = resvg_py.svg_to_bytes(svg_string=svg, width=size, height=size)
    return Image.open(io.BytesIO(bytes(data))).convert("RGBA")
def on_bg(img, w, h, pad):
    canvas = Image.new("RGBA", (w, h), bg); s = min(w, h) - 2 * pad
    canvas.alpha_composite(img.resize((s, s), Image.LANCZOS), ((w - s) // 2, (h - s) // 2))
    return canvas
png(48).save(out / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
on_bg(png(512), 180, 180, 20).convert("RGB").save(out / "apple-touch-icon.png")
for s in (192, 512): png(s).save(out / f"icon-{s}.png")
on_bg(png(1024), 400, 400, 60).save(out / "linkedin-400.png")
on_bg(png(1024), 1200, 630, 165).save(out / "og-default.png")   # placeholder; design the real one
(out / "icon.svg").write_text(svg, encoding="utf-8")              # then: npx svgo@4.1.0 out/icon.svg
```

Notes: the favicon should use the simplified symbol (or a single letter), not the full wordmark, and
should be checked at 16 px in the rendered PNG. The OG image above is only a placeholder (mark centered
on a color); the real one should be laid out as an SVG with the wordmark and rendered the same way.
Online alternative: realfavicongenerator.net does the same from an upload.

Sources: https://evilmartians.com/chronicles/how-to-favicon-in-six-files-that-fit-most-needs ,
https://developer.wordpress.org/reference/functions/get_site_icon_url/ ,
https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#ico ,
https://resvg-py.readthedocs.io/ , https://realfavicongenerator.net
