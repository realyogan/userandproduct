# Thumbnail tooling research (2026-10-09)

What would let userandproduct.com produce article thumbnails in the styles of the owner's references
(`references/blog-thumbnails/README.md`) reliably and repeatably, from code or a code-driven tool.
Research only; nothing was installed. Prices are list prices found on 9 Oct 2026; several come from
aggregators and conflict, so confirm on the vendor page before paying.

## Recommendation

The honest summary: **code does most of this better than any generator**, because the reference look is
built from a small set of mechanical treatments (flat ground, dot or square grid, grain, dither or
halftone, hard offset shadow, mono type, mark in a corner). Those are deterministic in Python and keep
hundreds of thumbnails identical in finish. A generator is only needed for the *subject drawing* in the
flat-vector group, and for photos when no free photo fits.

Adopt now, in this order:

1. **Extend our own Python pipeline into `thumbnail.py`** (free; Pillow 12.3, numpy 2.5, resvg-py and
   skia-pathops are already installed). Add: Bayer and clustered-dot dithering, an amplitude-modulated
   halftone dot screen, a palette mapper to the article's Printables tint (ground, highlight A, highlight
   B, ink), grain, square grid, hard offset shadow, pixel upscaling, and the mark. About 300 lines; no new
   install. One finding from testing: Pillow's `Dither.ORDERED` and `Dither.RASTERIZE` are accepted but
   silently fall back to Floyd-Steinberg, so ordered and halftone screens must be written in numpy (each
   is about 20 lines). This alone covers four of the five style groups.
2. **Copy two free icon sets into `research/mockups/vendor/`**: Pixelarticons (MIT, 24 px pixel grid,
   for the pixel-icon group) and Phosphor (MIT, six weights including Fill and Duotone, for flat-vector
   subjects and diagrams). Free, no attribution required. Single SVG files, no npm.
3. **Recraft Pro, monthly, only when the first flat-vector thumbnails are due** (about 20 USD a month for
   2,000 credits; a vector costs 2 credits, so roughly 1,000 vectors; paid plans grant ownership and
   commercial rights). Create one custom style from 3 to 5 of our own finished thumbnails and generate
   every vector subject with that `style_id`, so the series stays consistent. Cancel in months with no
   need; images made while subscribed keep their rights. API alternative with no subscription: V4.1
   Vector at about 0.08 USD, V4 Styles Vector at about 0.05 USD.

Skip for now: Claude Code image skills (none add anything our pipeline would not, see section 1), local
generation (the RX 5500 XT 8 GB is unsupported territory for Flux), Ideogram (our type is set in code, so
its text strength is not needed), Stability. Keep **Flux 2 Pro via the BFL API** (about 0.03 USD per
megapixel, outputs licensed for commercial use) or **Imagen 4 Fast** (0.02 USD) as the pay-per-image
fallback for a halftone source photo when no free photo fits.

## 1. Claude Code skills and plugins

| Skill | What it does | Code? | Licence, updated | Adds anything for thumbnails? |
|---|---|---|---|---|
| **canvas-design** (Anthropic, `anthropics/skills`) | Writes a short "design philosophy", then composes a single static poster or artwork as PNG or PDF; bundles a folder of open fonts | Instructions plus bundled fonts; Claude writes the drawing code itself | Apache 2.0 for the skill, fonts under their own licences; repo active in 2026 | Little. It is a composition pep talk for one-off posters; it has no dithering, palette or series discipline. Our `illustration-rules.md` is already stricter |
| **algorithmic-art** (Anthropic) | Seeded generative art in p5.js, viewed in a browser | Instructions plus p5.js template | Apache 2.0 | No. Browser-rendered p5 sketches are the wrong output for a Python PNG pipeline |
| **frontend-design** (installed, user level) | Aesthetic direction for UI | Instructions | Installed copy | No image capability |
| **impeccable** (installed, project) | UI design system; has an `impeccable generate-image` API fallback (flags `--ref`, `--quality high`, `--background transparent`) that embeds the prompt in the PNG | Ships a binary; image generation needs a provider API key | Its LICENSE in `.claude/skills/impeccable/` | Only the prompt-embedding idea (`embed-prompt`) is worth copying: store the recipe inside each thumbnail's metadata for provenance |
| **design-taste-frontend** (installed) | Anti-template UI rules; tells the agent to use any image tool present for hero photos and textures | Instructions | Installed copy | No; and its "always use the image tool" rule would push the wrong way for thumbnails |
| **cc-nano-banana** (kkoppenhaver) | Wraps the Gemini CLI nanobanana extension: `/generate`, `/icon`, variations, seeds | Needs Gemini CLI and API key | Last push Feb 2026, about 290 stars | Convenience only; a direct API call from Python is simpler |
| **nano-banana** (glebis/claude-skills) | Calls Gemini image API directly, mentions thumbnails | Python script, Gemini key | Updated Aug 2026 | Same; a thin wrapper |
| **fal-ai-image** (artwist-polyakov) | Nano Banana Pro or GPT Image 2 via fal.ai, reference images | Script, fal key | 2026 | Thin wrapper over fal; useful only if we choose fal |
| **ai-image-generation** (inference.sh) | Multi-model CLI (Gemini, Flux, GPT Image) | Third-party CLI and account | 2026 | Adds a vendor in the middle; no |
| **pixel-art** (ARIS / Hermes agent) | Draws pixel-art SVG from 7 px rects with a small palette | Instructions | Community | Marginal; Pixelarticons plus our upscaler does this better and repeatably |
| **pixel-art** (omer-metin) | Pixel-art craft: palettes, dithering patterns, tiles | Instructions | Community | Background reading only |

Halftone or dithering skills: none found. Thumbnail or cover skills: only the generator wrappers above.
**Verdict: no skill is worth installing.** The value is in our own `thumbnail.py` plus a short
`thumbnail-rules.md` (the sibling of `illustration-rules.md`), which can later become a project skill.

Sources: https://github.com/anthropics/skills , https://skills.sh/nexu-io/open-design/canvas-design ,
https://claudemarketplaces.com/skills/anthropics/skills/algorithmic-art ,
https://gittrend.io/repo/kkoppenhaver/cc-nano-banana ,
https://skillselion.com/skills/glebis/claude-skills/nano-banana ,
https://claudeskills.info/skill/fal-ai-image/ , https://claudeskills.info/zh/best/image-generation-skills/ ,
https://skillselion.com/skills/nousresearch/hermes-agent/pixel-art ,
https://claudeskills.info/skills/omer-metin/skills-for-antigravity/pixel-art/

## 2. Code-only techniques and libraries (Windows, no build step)

**Dithering.** Pillow does Floyd-Steinberg to any palette (`quantize(palette=..., dither=FLOYDSTEINBERG)`,
tested here with a three-colour tint palette). Ordered (Bayer 4x4 or 8x8) and clustered-dot dithering
are not in Pillow (tested: the enum exists but falls back), so write them in numpy: tile a threshold
matrix, compare, map to palette. Bayer gives the crosshatch "pixel" look of the references; clustered
dot gives the print look. Optional libraries: **hitherdither** (Bayer, cluster-dot, Yliluoma ordered
dithering to arbitrary palettes; install from git, not PyPI; check its LICENSE first) and **didder**
(Go CLI, many algorithms, palettes as hex; check for a Windows release). Neither is needed.

**Halftone dot screen.** Amplitude-modulated: grid of cells (for example 8 to 12 px at 1200 wide), rotate
the grid 45 degrees, sample mean darkness per cell, draw a circle of proportional area in ink or
highlight B. Drawing it as SVG circles and rendering with resvg gives crisp, resolution-free dots and a
vector file for free. Library options: **halftone-converter** (Gray, RGB, CMYK screens, needs Pycairo)
and **halftones** on PyPI; both overkill for one-colour screens.

**Grain and paper.** numpy Gaussian noise (sigma 6 to 10 on 0 to 255), blended in soft light or plain
alpha 6 to 10 percent, monochrome, fixed seed per article slug so a re-render is identical. In SVG,
`feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3"` plus `feColorMatrix` to grey, at
low opacity; resvg supports filter primitives, but Python noise is more predictable across renderers.

**Grids.** Our dot grid already exists in `illustration.py`; add a fine square grid (1 px lines every
24 to 32 units, ink at 8 to 10 percent) as the second option.

**Pixel art.** Draw or take icons at 24 x 24, upscale with `Image.NEAREST` by an integer factor
(10x to 240 px, 16x to 384 px); never use smooth resampling. For a dithered photo with visible pixels,
downscale to 160 to 240 px wide, dither, then upscale NEAREST by 5 to 8.

**Hard shadow.** Duplicate the shape, fill ink #1D1B16, offset 8 to 14 units down-right, draw under the
pale shape with a 2.5-unit ink stroke. Trivial in SVG.

**Icon sets (all recolourable, since they are single-path SVGs using `currentColor` or one fill):**

| Set | Licence | Fit |
|---|---|---|
| Pixelarticons | MIT (free set about 800 to 1,000 icons, 24 px grid) | Pixel-icon group |
| HackerNoon Pixel Icon Library | CC BY 4.0 icons (credit needed unless paid) | Second pixel set if Pixelarticons lacks a subject |
| Phosphor | MIT, six weights incl. Fill and Duotone | Flat-vector subjects, diagrams |
| Lucide | ISC | Diagrams (thin stroke) |
| Tabler | MIT | Large stroke set |
| Heroicons | MIT | Small set, fine for diagrams |
| Streamline free | Mixed: some sets CC BY 4.0 with a link to streamlinehq.com, others free but not open | Only with a credit line |

**Illustration libraries:** unDraw (free commercial, recolourable via its colour picker, but no
automated download and the look is the generic SaaS style), Open Doodles and Humaaans (CC0, recolourable,
but playful and over-used), Blush (free tier limited, SVG paid). None match the references' look; none
recommended. Detail in `tooling-research-2026-10-09.md` section 4.

Sources: https://pillow.readthedocs.io/en/stable/reference/Image.html ,
https://en.wikipedia.org/wiki/Ordered_dithering , https://github.com/hbldh/hitherdither ,
https://30fps.net/pages/revisiting-yliluoma-2/ ,
https://dyn.manpages.debian.org/unstable/didder/didder.1.en.html ,
https://github.com/curegit/halftone-converter , https://pypi.org/project/halftones ,
https://cdn.jsdelivr.net/npm/pixelarticons@2.4.1/README.md ,
https://unpkg.com/@hackernoon/pixel-icon-library@1.0.6/README.md ,
https://icon-sets.iconify.design/ph/air-traffic-control-duotone/ , https://lucide.dev/license ,
https://licenseorg.com/guide/design-graphics/heroicons ,
https://help.streamlinehq.com/en/articles/5354376-streamline-free-license , https://undraw.co/license

## 3. Image-generation routes

| Route | Price per image | Outputs, commercial | Python API | Vector | Flat style, series consistency | Text | Halftone / pixel |
|---|---|---|---|---|---|---|---|
| **Recraft** V4.1 / V4 Styles | Pro plan about 20 USD/month for 2,000 credits (vector 2 credits). API: V4.1 35 units, V4.1 Vector 80, V4 Styles Vector 50, style creation 40 (about 0.001 USD per unit) | Paid plan: you own, full commercial rights, private; free plan: Recraft owns, no commercial use. No use of outputs to train models | REST API, also on fal.ai | **Native SVG** | **Best**: custom style from reference images gives a reusable `style_id` | Good | Can be prompted; better done in code |
| **Ideogram** 3.0 / 4.0 | API 0.03 (Turbo), 0.06 (Default), 0.10 (Quality) | Ideogram claims no ownership of outputs; free tier public and reportedly personal use only | REST API | No | Style reference (up to 3 images) and reusable style codes | **Best text** | Fair |
| **Flux 2** via BFL API | Pro: 0.03 first megapixel + 0.015 each extra; Max 0.07; fal and Replicate about 0.045 to 0.07 for 1920x1080 | API outputs: full commercial rights included | BFL REST, fal, Replicate clients | No | Multi-reference editing helps; no seed-level style lock across providers | Good | Good photographic sources to dither |
| **OpenAI** GPT Image 2 | 1024x1024: 0.006 low, 0.053 medium, 0.211 high; Batch half price | Customer owns output under OpenAI terms | `openai` SDK | No | Reference images supported; no persistent style | Very good | Fair |
| **Google** Imagen 4 / Gemini image ("Nano Banana") | Imagen 4 Fast 0.02, Standard 0.04, Ultra 0.06; Gemini 3 Pro Image 0.134 | Paid API commercial use allowed; invisible SynthID watermark | `google-genai` SDK | No | Gemini image takes several reference images, good for keeping a look | Good | Fair |
| **Stability** Stable Image Core / Ultra | 0.03 / 0.08 (credits at 0.01) | API outputs usable commercially; self-hosted models free under 1M USD revenue, then enterprise licence | REST | No | Weaker | Fair | Fair |
| **Local** ComfyUI + Flux or SDXL | Electricity only | Flux dev/klein 9B: non-commercial licence for the model, outputs usable; klein 4B Apache 2.0; SDXL open | Python, ComfyUI API | No | LoRA training gives the strongest lock | Weak | Fair |

**Local hardware, honestly.** This machine has an AMD RX 5500 XT with 8 GB. The ZLUDA fork of ComfyUI
lists RDNA1 as supported, but no one has published 5500 XT results; SDXL wants 12 GB, Flux at FP8 took
about 90 seconds per image on a 24 GB RX 7900 XTX, and first runs on ZLUDA can take 10 to 15 minutes to
compile. Practical local use needs an NVIDIA card with 12 to 16 GB (RTX 4070 Ti Super or 5060 Ti 16 GB
class). Not worth it at our volume: 300 hosted images cost 10 to 25 USD.

**What each is good for here.** Vector: Recraft only. Flat illustration in one consistent style: Recraft
custom style, then Ideogram style codes. Typographic covers: Ideogram is best, but we should not
generate type at all; real fonts in SVG are exact, searchable in our files, and free. Halftone and
pixel looks: any photo generator as the *source*, then our code does the screen. Series consistency:
Recraft `style_id` for vectors; for everything else, consistency comes from the code post-processing,
not the generator.

Sources: https://www.recraft.ai/pricing?tab=api , https://www.recraft.ai/docs/plans-and-billing/paid-plans ,
https://www.recraft.ai/docs/plans-and-billing/commercial-rights-and-ownership ,
https://fal.ai/models/recraft/v4/pro/create-style/llms.txt ,
https://developer.puter.com/tutorials/ideogram-api-pricing/ , https://docs.ideogram.ai/using-ideogram/features-and-tools/reference-features ,
https://docs.ideogram.ai/frequently-asked-questions , https://openrouter.ai/black-forest-labs/flux.2-pro/providers ,
https://help.bfl.ai/articles/3670520907-can-i-use-the-api-for-a-commercial-application ,
https://invideo.io/blog/flux-ai-image-generator/ , https://crepal.ai/blog/aiimage/image-gpt-image-2-pricing/ ,
https://magichour.ai/blog/imagen-4-pricing-and-api , https://intuitionlabs.ai/articles/ai-image-generation-pricing-google-openai ,
https://developer.puter.com/tutorials/stability-ai-api-pricing/ , https://stability.ai/license ,
https://github.com/patientx/ComfyUI-Zluda , https://github.com/CS1o/Stable-Diffusion-Info/wiki/Webui-Installation-Guides ,
https://rocm.blogs.amd.com/artificial-intelligence/comfyui-radeon-9000/README.html

## 4. Photo sources for the halftone style

| Source | Terms | Attribution |
|---|---|---|
| **Owner's own photos** | Full rights; strongest for authority (real workshops, whiteboards, sticky notes, devices) | None |
| Unsplash | Free commercial use; no selling unaltered copies, no competing service; no rights to logos or recognisable people beyond the photo | Not required (appreciated) |
| Pexels | Pexels License or CC0; same resale and competing-service limits | Not required |
| Wikimedia Commons | Per file: public domain, CC BY, CC BY-SA | Per file; CC BY-SA would make our derivative share-alike, avoid |
| Library of Congress "Free to Use and Reuse" | Public domain or no known restrictions; check each item's rights line | Credit good practice |
| Openverse | Search engine over CC and public domain; does not verify licences | Per result; verify at source |

Rules for our use: prefer the owner's photos, then Unsplash or Pexels; avoid recognisable faces and
brand logos (a halftone does not remove a trademark); record source URL, author and licence in a
`thumbnails/credits.csv` and in the PNG metadata. A heavy dither is a modification, which also keeps us
clear of the "unaltered copy" clauses.

Sources: https://unsplash.com/license , https://help.unsplash.com/en/articles/9251205-can-unsplash-illustrations-be-used-for-commercial-purposes ,
https://help.pexels.com/hc/en-us/articles/360042295174-What-is-the-license-of-the-photos-and-videos-on-Pexels ,
https://pexels.com/terms-of-service , https://lincsproject.ca/docs/terms/wikimedia-commons ,
https://www.openculture.com/2018/11/library-congress-makes-thousands-fabulous-photos-posters-images-free-use-reuse.html ,
https://en.wikipedia.org/wiki/Openverse

## 5. Workflow proposal

**Shared finish (every group, in code):** 1200 x 675 canvas; ground from the article's tint (pastel
background, or highlight B as a saturated ground to match the references' punch, with ink or white
type checked to 4.5:1); dot grid or square grid; grain at a fixed seed from the slug; mono type set in
SVG from a real font; the mark in the bottom-right 100 x 100 zone; export PNG plus a 600 px copy; embed
the recipe (style group, tint, source, seed, prompt if any) in PNG text chunks. One command:
`python thumbnail.py <slug> --style halftone --source photo.jpg`. Consistency comes from this finish
being identical every time.

| Style group | Recommended path | Cost per image | Time per image |
|---|---|---|---|
| **Halftone or dithered photo** | Code plus a source photo: crop to subject, remove background if needed (Recraft or Ideogram background removal 0.01, or a manual mask), map to 2 or 3 tint colours, dot screen at 45 degrees or Bayer dither for the pixel variant | 0 with own or free photo; 0.02 to 0.045 if a source is generated (Imagen 4 Fast or Flux 2 Pro, prompt: "studio photo of a single [object] on plain white, centered, hard side light, high contrast, no text") | 5 to 10 min (finding the photo is most of it) |
| **Pixel icon** | Code alone: Pixelarticons glyph, recoloured, upscaled NEAREST, optional second icon or number; or a hand-drawn 24 x 24 grid in a small text format (`#` and `.`) rendered by the same code | 0 | 2 to 5 min |
| **Flat vector with hard black shadow** | Simple subjects (magnifier, chart, cycle of icons, chat box): code alone from Phosphor Fill shapes, pale fill, ink stroke, offset shadow. Complex subjects (animal, robot, scene): Recraft Vector with our custom style, prompt recipe "flat vector illustration of [subject], pale cream shapes, thick black outline, solid black offset shadow down-right, no gradients, no background, centered"; then code: parse SVG, force fills to the tint palette (pale #FDFCF8, ink #1D1B16, one highlight), add the shadow ourselves if missing, place on the grained grid | 0 (code) or about 0.02 on the Pro plan, 0.05 to 0.08 via API, plus 1 to 3 retries | 5 min (code) to 15 min (generated, including cleanup) |
| **Dark line diagram** | Code alone, from `illustration.py`: near-black ground, 2.5-unit white lines, one accent from the article tint, Lucide or Phosphor regular icons inside boxes. These double as the article's lead explainer | 0 | 10 to 20 min (it is a real diagram) |
| **Typographic cover** | Code alone: mono or pixel font set as SVG (our wordmark tooling already turns fonts into paths), optional big number or label, grid and grain. Never generated | 0 | 2 to 5 min |

**What keeps a consistent look across hundreds of articles:** the code paths. Four groups need no
generator at all, and in the fifth the generator only supplies a shape that the code then recolours and
finishes. The risks are drift in generated subjects (mitigated by one Recraft `style_id` and the palette
remap) and over-using one group; a rotation rule (for example group by category, tint by publish order,
as now) keeps the grid of thumbnails varied but coherent. Expected monthly cost at 20 to 40 articles:
0 to 20 USD.

**Next step if the owner says go:** build `thumbnail.py` and one example per group on the current mock
articles, then write `thumbnail-rules.md` next to `illustration-rules.md`.
