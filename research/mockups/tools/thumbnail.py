"""Article thumbnails and hero images for userandproduct.com: ten code-drawn styles and one photo style.

Rules and the per-article workflow: the project's thumbnail-images skill (kept with the project skills).
Colour: each image gets one bold background, chosen freely per image ("contrast and curiosity, not
clickbait"), and a colour scheme: mono (background and ink; the default), duo (one accent near the complement),
trio (two accents, split-complementary or triadic; rare) or analogous (a neighbouring hue). Accents mark only
the thing that matters and are computed to pass 3:1 against the background (4.5:1 if they carry text); a wheel
position that fails is rotated until it passes, else the image falls back to mono. BACKGROUNDS below are
suggestions; any background whose ink passes 4.5:1 is allowed. The generator records backgrounds and schemes in
research/mockups/thumbnail-history.json and avoids repeating a recent one.
Brand: the full lockup, mark and wordmark (research/mockups/final-logo-2/svg/lockup-white.svg or lockup-black.svg,
by contrast), on both sizes, sized so the wordmark reads where the image is shown (LOCKUP_PX below), in a corner
clear of the subject.
Icons: research/mockups/vendor/pixelarticons (24 px pixel set) and research/mockups/vendor/phosphor (regular, fill).
Gallery of all eleven styles: research/mockups/references/blog-thumbnails/gallery.html

Styles (STYLES below has the one-line spec of each):
  1 flat vector, hard shadows, square grid + grain      7 dark glow diagram, glow in colour
  2 flat vector, hard shadows, dot grid + grain         8 light grid diagram, one accent
  3 pixel-art icon and panel, dot grid                  9 particle field on near-black
  4 icon sequence on a grained grid, numbered           10 bright particle field on a saturated ground
  5 typographic cover, pixel or set type + one object   11 halftone or dithered photo (only with a photo)
  6 dark line diagram, one accent

A spec is a small dict:
  {"slug": "prd-engineers-read",           # required: rotation, palette pick and grain seed come from it
   "subject": "prd",                       # a key of SUBJECTS, or "icon:<phosphor-name>"
   "index": None,                          # publish order, if known (rotation by index, else by slug hash)
   "title": "How to Write a PRD ...",      # the article title: its kind is classified from it (or give "kind")
   "kind": "howto",                        # optional: one of KINDS_OF_ARTICLE
   "cover_title": "PRDs engineers read",   # style 5's short line of type (else the title, if short)
   "steps": ["note", "flask", ...],        # style 4: 3 to 5 Phosphor names (else the subject's own steps)
   "focus": 1,                             # style 4: the step to highlight (0-based), optional
   "photo": "path/to/photo.jpg",           # style 11: the owner's photo; its presence selects style 11
   "photo_method": "screen" | "bayer",     # style 11: dot screen (default) or ordered dither
   "palette": "red-orange",                # a BACKGROUNDS name; or give "bg" as hex instead
   "bg": "#FF5A36",                        # any background whose ink passes 4.5:1; the ink follows by contrast
   "scheme": "duo",                        # mono | duo | trio | analogous (default: mono, or duo after a mono)
   "accent": "#0E6B3A",                    # optional explicit accent (checked 3:1, 4.5:1 for text)
   "style": 7, "reason": "..."}            # override the rotation; a reason is required

Usage:
    python thumbnail.py --slug prd-engineers-read --subject prd [--palette NAME | --bg HEX] [--scheme duo]
                        [--title "..."] [--photo p.jpg] [--style N --reason "..."]
    python thumbnail.py --rotation 12          # print the style for indexes 0 to 11
    python thumbnail.py --palettes             # print the suggested backgrounds with their duo accent

Python:
    from thumbnail import make, pick_style
    result = make({"slug": "prd-engineers-read", "subject": "prd"}, out_dir="...")
    # writes <slug>-hero.png (1200 x 675) and <slug>-thumb.png (600 x 338), both with the lockup, <slug>.svg
    # and <slug>-check-300.png; result has the style and colours used, any fallback note and the checks.
"""
import argparse
import colorsys
import re
import hashlib
import io
import json
import math
import sys
from pathlib import Path
from xml.sax.saxutils import escape

import numpy as np
import resvg_py
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps
from PIL.PngImagePlugin import PngInfo

HERE = Path(__file__).resolve().parent
MOCKUPS = HERE.parent

VENDOR = MOCKUPS / "vendor"
FONTS = MOCKUPS / "fonts"
TYPE_FONT = FONTS / "space-grotesk" / "SpaceGrotesk-Bold.ttf"     # cover titles and step numbers
TYPE_FAMILY = "Space Grotesk"
FONT_FILES = [str(TYPE_FONT)]

W, H = 1200, 675
HERO, THUMB, CHECK_W = (1200, 675), (600, 338), 300
INK = "#1D1B16"                        # outlines, shadows, dark ink
CARD = "#FDFCF8"                       # the pale fill of flat shapes
WHITE = "#FFFFFF"
LOGO = MOCKUPS / "final-logo-2" / "svg"
HISTORY = MOCKUPS / "thumbnail-history.json"
# The full lockup (mark + wordmark) on both output sizes, at the same share of the width (about a fifth), so the
# thumb is the hero at half size and the logo looks the same wherever the image is shown.
#   hero 1200 px: 220 px wide (18%). This is the legibility anchor: shown about 720 px wide on the article page,
#     the wordmark's lowercase x-height (5.9% of the lockup's width) is about 7.8 px.
#   thumb 600 px: 120 px wide (20%, a touch above the hero's share).
LOCKUP_PX = {"hero": 220, "thumb": 120}               # lockup width in output pixels, per output size
LOCKUP_MARGIN_PX = {"hero": 40, "thumb": 20}          # in from the edges, in output pixels
LOCKUP_O = .92                                        # quiet but readable; never below .9
OUT_W = {"hero": HERO[0], "thumb": THUMB[0]}


# ---------------------------------------------------------------- colour
def _rgb01(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def lum(h):
    v = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in _rgb01(h)]
    return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2]


def contrast(a, b):
    x, y = sorted([lum(a), lum(b)], reverse=True)
    return (x + 0.05) / (y + 0.05)


def mix(a, b, t):
    ra, rb = _rgb01(a), _rgb01(b)
    return "#" + "".join(f"{round((ra[i] + (rb[i] - ra[i]) * t) * 255):02X}" for i in range(3))


def ink_for(bg):
    """Dark ink or white, whichever contrasts more with the background."""
    return INK if contrast(INK, bg) >= contrast(WHITE, bg) else WHITE


def _dist(a, b):
    return math.dist([c * 255 for c in _rgb01(a)], [c * 255 for c in _rgb01(b)])


# Suggested backgrounds (suggestions only: any background whose ink passes 4.5:1 may be used).
# kind: bright (dark ink), deep (white ink, saturated), dark (near-black or midnight), paper (pale).
BACKGROUNDS = {
    "red-orange":    ("#FF5A36", "bright"),
    "acid-yellow":   ("#E9FF3B", "bright"),
    "tangerine":     ("#FF8A1F", "bright"),
    "teal":          ("#14B8A6", "bright"),
    "hot-pink":      ("#FF5CA8", "bright"),
    "mint":          ("#3DDC84", "bright"),
    "violet":        ("#6B4CFF", "deep"),
    "electric-blue": ("#2F5BFF", "deep"),
    "night":         ("#16151A", "dark"),
    "night-plum":    ("#1C1426", "dark"),
    "midnight":      ("#121A3A", "dark"),
    "paper":         ("#F4F1E8", "paper"),
}
SCHEMES = ("mono", "duo", "trio", "analogous")
SCHEME_OFFSETS = {"duo": (180,), "trio": (120, 240), "triad": (150, 210), "analogous": (35,)}


# ---- a small HSL helper
def to_hls(h):
    return colorsys.rgb_to_hls(*_rgb01(h))


def from_hls(hh, ll, ss):
    return "#" + "".join(f"{max(0, min(255, round(c * 255))):02X}" for c in colorsys.hls_to_rgb(hh % 1, ll, ss))


def rotate(h, deg):
    hh, ll, ss = to_hls(h)
    return from_hls(hh + deg / 360, ll, ss)


def complement(h):
    return rotate(h, 180)


def split(h):
    return rotate(h, 150), rotate(h, 210)


def triad(h):
    return rotate(h, 120), rotate(h, 240)


def analogous(h, deg=35):
    return rotate(h, deg)


def nudge_for_contrast(color, bg, need=3.0):
    """Keep the hue; raise saturation and move lightness away from the background until the colour reaches
    `need`:1 against it. Returns None when no lightness at this hue gets there."""
    hh, _, ss = to_hls(color)
    ss = max(ss, .65)
    toward_light = lum(bg) < .18
    steps = [i / 100 for i in range(50, 98)] if toward_light else [i / 100 for i in range(50, 3, -1)]
    for ll in steps:
        c = from_hls(hh, ll, ss)
        if contrast(c, bg) >= need:
            return c
    return None


def accent_at(bg, offset, need=3.0, max_turn=90):
    """An accent at `offset` degrees round the wheel from the background's hue, nudged until it passes `need`:1;
    if that hue cannot pass, turn it in 10-degree steps (both ways, up to `max_turn`). None if nothing passes."""
    hh, ll, ss = to_hls(bg)
    base = from_hls(hh, .5, max(ss, .7))
    for turn in [0] + [t * sgn for t in range(10, max_turn + 1, 10) for sgn in (1, -1)]:
        c = nudge_for_contrast(rotate(base, offset + turn), bg, need)
        if c:
            return c
    return None


HUE_NAMES = [(15, "red"), (40, "orange"), (65, "yellow"), (90, "lime"), (165, "green"), (185, "teal"), (200, "cyan"),
             (235, "blue"), (260, "indigo"), (290, "violet"), (330, "magenta"), (350, "pink"), (361, "red")]


def colour_name(h):
    hh, ll, ss = to_hls(h)
    if ss < .15:
        return "white" if ll > .8 else "grey" if ll > .25 else "black"
    deg = hh * 360
    name = next(n for top, n in HUE_NAMES if deg < top)
    return ("deep " if ll < .32 else "pale " if ll > .78 else "") + name


def scheme_accents(bg, scheme, need=3.0):
    """The accents for a scheme on this background: [] for mono, one for duo and analogous, two for trio.
    Falls back to mono ([]) when a wheel position cannot pass the check."""
    if scheme == "mono":
        return []
    offs = SCHEME_OFFSETS["trio" if scheme == "trio" else scheme]
    out = [accent_at(bg, o, need) for o in offs]
    if any(c is None for c in out):
        return []
    if scheme == "trio" and contrast(out[0], out[1]) < 1.3 and _dist(out[0], out[1]) < 120:
        alt = [accent_at(bg, o, need) for o in SCHEME_OFFSETS["triad"]]
        out = alt if all(alt) else out[:1]
    return out


# the palette kinds each style can sit on
KINDS = {1: ("bright",), 2: ("bright",), 3: ("bright",), 4: ("bright",), 5: ("dark", "deep"),
         6: ("dark",), 7: ("dark",), 8: ("paper",), 9: ("dark",), 10: ("bright", "deep"), 11: ("bright",)}
LINE_STYLES = (6, 7, 8)
ACCENT_TEXT_STYLES = (5,)          # styles where the accent colours type, so it needs 4.5:1


def kind_of(bg):
    if lum(bg) > .75 and _dist(bg, "#FFFFFF") < 60:
        return "paper"
    if ink_for(bg) == INK:
        return "bright"
    return "dark" if lum(bg) < .03 else "deep"


def check_colors(bg, accents=(), style=None):
    """Problems with a background and its accents (an empty list means allowed): the ink must reach 4.5:1 on the
    background; each accent 3:1 (shapes) or 4.5:1 (when it colours text); at most two accents."""
    probs = []
    ink = ink_for(bg)
    if contrast(ink, bg) < 4.5:
        probs.append(f"no ink reaches 4.5:1 on {bg} (best {contrast(ink, bg):.1f}:1)")
    need = 4.5 if style in ACCENT_TEXT_STYLES else 3.0
    for a in accents:
        if contrast(a, bg) < need:
            probs.append(f"accent {a} is {contrast(a, bg):.1f}:1 on {bg}; needs {need}:1")
    if len(accents) > 2:
        probs.append("more than two accents")
    return probs


def make_palette(bg, accents, scheme, name="custom"):
    """The colours one image uses. With no accent (mono) the accent role falls back to a neutral: card white on
    bright and paper grounds, white on dark ones, so the subject reads in ink alone."""
    ink = ink_for(bg)
    neutral = CARD if ink == INK else WHITE
    a = accents[0] if accents else neutral
    b = accents[1] if len(accents) > 1 else a
    return dict(name=name, bg=bg, a=a, b=b, ink=ink, kind=kind_of(bg), scheme=scheme if accents else "mono",
                accents=list(accents))


def load_history():
    try:
        return json.loads(HISTORY.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return []


def save_history(entry, keep=24):
    hist = [h for h in load_history() if h.get("slug") != entry["slug"]] + [entry]
    HISTORY.write_text(json.dumps(hist[-keep:], indent=2), encoding="utf-8")


def pick_palette(style, slug, history=None, avoid_last=3):
    """A suggested background that suits the style. An article that already has one keeps it; otherwise the first
    suited background, in a slug-hashed order, not among the last `avoid_last` used."""
    history = history or []
    suited = [n for n, (_, k) in BACKGROUNDS.items() if k in KINDS[style]]
    for h in history:
        if h.get("slug") == slug and h.get("palette") in suited:
            return h["palette"]
    others = [h for h in history if h.get("slug") != slug]
    recent = {h.get("bg") for h in others[-avoid_last:]}
    start = _hash(slug, "palette") % len(suited)
    order = suited[start:] + suited[:start]
    fresh = [n for n in order if BACKGROUNDS[n][0] not in recent] or order
    if others and others[-1].get("bg"):                  # prefer a ground that looks different from the last one
        far = [n for n in fresh if _dist(BACKGROUNDS[n][0], others[-1]["bg"]) >= 80
               and BACKGROUNDS[n][1] != others[-1].get("ground")]
        fresh = far or fresh
    return fresh[0]


def pick_scheme(slug, history=None):
    """Restraint first: mono by default; duo when the previous piece was mono, so neighbours differ. Trio and
    analogous are chosen by the writer, never automatically. An article that already has a scheme keeps it."""
    history = history or []
    for h in history:
        if h.get("slug") == slug and h.get("scheme"):
            return h["scheme"]
    others = [h for h in history if h.get("slug") != slug]
    last = others[-1].get("scheme") if others else None
    return "duo" if last in (None, "mono") else "mono"


def resolve_palette(spec, style, history):
    need = 4.5 if style in ACCENT_TEXT_STYLES else 3.0
    if spec.get("bg"):
        bg, name = spec["bg"].upper(), "custom"
    else:
        name = spec.get("palette") or pick_palette(style, spec["slug"], history)
        if name not in BACKGROUNDS:
            raise SpecError(f"Unknown palette {name!r}; use one of {', '.join(BACKGROUNDS)} or give bg.")
        bg = BACKGROUNDS[name][0]
    if kind_of(bg) not in KINDS[style]:
        raise SpecError(f"a {kind_of(bg)} background ({name}) does not suit style {style}")
    scheme = "mono" if style == PHOTO_STYLE else (spec.get("scheme") or pick_scheme(spec["slug"], history))
    if scheme not in SCHEMES:
        raise ValueError(f"Unknown scheme {scheme!r}; use one of {', '.join(SCHEMES)}.")
    if spec.get("accent"):
        accents = [c.upper() for c in ([spec["accent"]] + ([spec["accent2"]] if spec.get("accent2") else []))]
    else:
        accents = scheme_accents(bg, scheme, need)
    probs = check_colors(bg, accents, style)
    if probs:
        raise ValueError("colours fail: " + "; ".join(probs))
    return make_palette(bg, accents, scheme, name)

# The rotation order: light and dark, busy and quiet alternate, so neighbouring articles differ.
ROTATION = [1, 6, 3, 9, 4, 7, 10, 5, 2, 8]
PHOTO_STYLE = 11

# Kinds of article, and the styles that suit each (the rotation runs only among these).
KINDS_OF_ARTICLE = {
    "howto": "a how-to or procedure",
    "opinion": "a judgment or opinion piece",
    "concept": "a concept explainer",
    "comparison": "a comparison",
    "list": "a list or sequence of things",
    "data": "a data or metrics piece",
    "tool": "a tool or template page",
    "story": "a story or case",
    "series": "a series piece",
}
SUITS = {
    1: {"howto", "opinion", "concept", "comparison", "list", "tool", "story", "series"},  # one nameable object
    2: {"howto", "opinion", "concept", "comparison", "list", "tool", "story", "series"},
    3: {"tool", "howto", "concept"},                     # tools, templates, technical concepts
    4: {"list", "howto", "series"},                      # lists, steps, series; not opinion or one concept
    5: {"opinion", "series", "story"},                   # judgment pieces, announcements, series covers
    6: {"data", "comparison", "concept"},                # data, systems, comparisons
    7: {"concept", "data", "opinion"},                   # one key idea or result
    8: {"data", "comparison", "concept"},                # structure, models, comparisons
    9: {"concept", "data"},                              # flows, scale, abstract concepts
    10: {"concept", "data", "list"},                     # the same, bright
    11: {"story"},                                       # only with the owner's photo
}

_KIND_WORDS = [
    ("series", (r"\bpart \d", r"\bseries\b", r"\bepisode\b", r"#\d")),
    ("story", (r"\bcase stud", r"\bhow we\b", r"\bstory\b", r"\bpostmortem\b", r"\bwhat happened\b",
               r"\blessons from\b", r"\bwe (?:learned|shipped|built)\b")),
    ("comparison", (r"\bvs\.?\b", r"\bversus\b", r"\bcompared\b", r"\bdifference between\b", r"\bor\b.*\?$",
                    r"\bwhich\b")),
    ("tool", (r"\btemplate", r"\bchecklist", r"\btoolkit", r"\bcalculator", r"\bworksheet", r"\bcanvas\b",
              r"\bgenerator\b", r"\bfree tool")),
    ("data", (r"\bretention\b", r"\bchurn\b", r"\bmetric", r"\bkpi", r"\banalytics\b", r"\bcohort",
              r"\bfunnel\b", r"\bdata\b", r"\bnumbers\b", r"\bconversion\b", r"\bnps\b", r"\bbenchmark")),
    ("list", (r"^\d+\s", r"\b\d+ (?:ways|tips|mistakes|lessons|questions|signs|steps|rules|habits|books)\b",
              r"\bmistakes\b", r"\btips\b")),
    ("opinion", (r"^why\b", r"\bstop\b", r"\bshould\b", r"\bmyth", r"\bis dead\b", r"\bthe case (?:for|against)\b",
                 r"\boverrated\b", r"\bwrong\b", r"\bdon't\b", r"\bnobody\b", r"\bin defen[cs]e of\b")),
    ("howto", (r"^how to\b", r"\bguide\b", r"^(?:write|run|build|plan|set up|start|make|use|create|design|"
               r"hire|interview|prioriti[sz]e|measure|test)\b", r"\bstep[- ]by[- ]step\b")),
    ("concept", (r"^what (?:is|are)\b", r"\bexplained\b", r"\bunderstanding\b", r"\bprinciple\b", r"\bmodel\b")),
]


def classify_kind(title, subject=""):
    """The article's kind from its title (first match in a fixed order); concept when nothing matches."""
    t = (title or "").strip().lower()
    for kind, pats in _KIND_WORDS:
        if any(re.search(p, t) for p in pats):
            return kind
    return "concept"


def suitable_styles(kind):
    """The code-drawn styles that suit a kind, in rotation order."""
    return [st for st in ROTATION if kind in SUITS[st]]

STYLES = {
    1: ("Flat vector, square grid", "Bold bright ground, fine ink square grid and grain; the subject in pale card and the "
        "accent with ink outlines and a solid ink shadow offset down-right."),
    2: ("Flat vector, dot grid", "As style 1 on the dot grid: bold ground, ink dot grid and grain, paper-cut subject with "
        "a hard ink shadow."),
    3: ("Pixel icon and panel", "Bold bright ground with the dot grid; a Pixelarticons glyph on whole cells inside a "
        "pixel window, interior checker-dithered in the accent, one-cell ink shadow."),
    4: ("Icon sequence", "Bold bright ground, grain and a grid; three to five Phosphor icons on pale discs with hard "
        "shadows, numbered, on a track; one disc in the accent."),
    5: ("Typographic cover", "Near-black or deep saturated ground; a short title in pixel type cut from Space Grotesk "
        "(or set type when long) in the accent, and one pixel object."),
    6: ("Dark line diagram", "Near-black ground with a faint white dot grid; the subject in thin white lines, one part "
        "in the accent."),
    7: ("Dark glow diagram", "Near-black ground; a soft radial glow in the accent behind the subject (trio: two, one "
        "per accent), white lines with a halo, the accented part glowing in its colour."),
    8: ("Light grid diagram", "Pale paper ground with a fine square grid and specks; thin ink lines and one strong "
        "warm accent."),
    9: ("Particle field", "Near-black ground; a stream of dots in the accent flows in from the left, fading to white, "
        "and gathers into the subject's silhouette in white (trio: in a second accent)."),
    10: ("Bright particle field", "Saturated ground (acid yellow, red-orange, electric blue); the same stream in the "
         "accent fading to the ink, the silhouette in the ink (trio: in a second accent)."),
    11: ("Halftone photo", "The owner's photo as a 45-degree ink dot screen (or an ordered dither) on a bold bright "
         "ground, feathered into it, faint dot grid."),
}


class SpecError(ValueError):
    pass


# ---------------------------------------------------------------- rotation
def _hash(text, salt):
    return int(hashlib.sha1(f"{salt}:{text}".encode("utf-8")).hexdigest(), 16)


def pick_style(slug_or_index, has_photo=False):
    """The article's style. A photo selects style 11. Otherwise the ten rotate: by publish index
    (ROTATION[index % 10]) or, for a slug, by a stable salted hash."""
    if has_photo:
        return PHOTO_STYLE
    if isinstance(slug_or_index, int):
        return ROTATION[slug_or_index % len(ROTATION)]
    return ROTATION[_hash(slug_or_index, "thumbnail-style") % len(ROTATION)]


def pick_for_kind(kind, slug_or_index, history=None, recent_n=3):
    """The style for an article of `kind`: the rotation runs only among the suitable styles, starting at the
    article's place (index or slug hash), skipping the previous article's style and preferring one not used in
    the last `recent_n` pieces. Returns (style, candidates, reason)."""
    cands = suitable_styles(kind)
    history = [h for h in (history or []) if h.get("slug") != (slug_or_index if isinstance(slug_or_index, str) else None)]
    key = slug_or_index if isinstance(slug_or_index, int) else _hash(slug_or_index, "thumbnail-style")
    start = key % len(cands)
    order = cands[start:] + cands[:start]
    last = history[-1]["style"] if history else None
    recent = [h.get("style") for h in history[-recent_n:]]
    fresh = [st for st in order if st not in recent]
    not_last = [st for st in order if st != last]
    last_ground = history[-1].get("ground") if history else None
    if last_ground:                                      # light and dark alternate: prefer a different ground
        fresh = [st for st in fresh if set(KINDS[st]) - {last_ground}] or fresh
    pick = (fresh or not_last or order)[0]
    why = (f"{KINDS_OF_ARTICLE[kind]}; suitable styles {cands}; style {pick} "
           + ("is next in the rotation and unused in the last pieces" if fresh else
              "differs from the previous piece" if not_last else "is the only suitable style"))
    return pick, cands, why


def next_style(style, candidates=None):
    """The style after `style` among the candidates (else the whole rotation): used when a style cannot carry
    the subject."""
    ring = candidates if candidates and style in candidates and len(candidates) > 1 else ROTATION
    if style not in ring:
        return ring[0]
    return ring[(ring.index(style) + 1) % len(ring)]


def seed_for(slug):
    return _hash(slug, "grain") % (2 ** 32)


# ---------------------------------------------------------------- icons
def _svg_paths(svg_text):
    import re
    return re.findall(r'<path[^>]*\sd="([^"]+)"', svg_text)


def phosphor(name, weight="fill"):
    p = VENDOR / "phosphor" / weight / f"{name}.svg"
    if not p.exists():
        raise SpecError(f"No Phosphor icon {name!r} ({weight}) in {p.parent}.")
    return _svg_paths(p.read_text(encoding="utf-8"))


def phosphor_svg(name, x, y, size, color, weight="fill", opacity=1):
    s = size / 256
    paths = "".join(f'<path d="{d}"/>' for d in phosphor(name, weight))
    return (f'<g transform="translate({x:.1f} {y:.1f}) scale({s:.4f})" fill="{color}" fill-opacity="{opacity}">'
            f'{paths}</g>')


def pixel_cells(name):
    """A Pixelarticons glyph as a 24 x 24 boolean array (rendered crisp, thresholded)."""
    p = VENDOR / "pixelarticons" / f"{name}.svg"
    if not p.exists():
        raise SpecError(f"No Pixelarticons glyph {name!r} in {p.parent}.")
    svg = p.read_text(encoding="utf-8").replace('fill="currentColor"', 'fill="#000000"')
    png = resvg_py.svg_to_bytes(svg_string=svg, width=24, height=24, shape_rendering="crisp_edges")
    a = np.asarray(Image.open(io.BytesIO(bytes(png))).convert("RGBA"))[..., 3]
    return a > 127


def interior(cells):
    """Empty cells enclosed by the glyph (flood fill from the border)."""
    h, w = cells.shape
    out = np.zeros_like(cells)
    stack = [(i, j) for i in range(h) for j in (0, w - 1)] + [(i, j) for i in (0, h - 1) for j in range(w)]
    while stack:
        i, j = stack.pop()
        if 0 <= i < h and 0 <= j < w and not out[i, j] and not cells[i, j]:
            out[i, j] = True
            stack += [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    return ~cells & ~out


# ---------------------------------------------------------------- the pen: one subject library, four treatments
class Pen:
    """Draws subject primitives in one of four treatments:
    flat  (styles 1, 2, 4): card-white and highlight-A fills, ink outline, solid ink shadow offset down-right
    dark  (style 6):        no fills, white lines, the accent role in the accent colour
    glow  (style 7):        as dark, with a halo on every line and a strong glow on the accent role
    light (style 8):        no fills, ink lines on paper, the accent role in the accent colour"""

    def __init__(self, mode, accent, accent2=None):
        self.mode, self.acc, self.acc2 = mode, accent, accent2 or accent
        self.two = self.acc2 != self.acc                 # a trio: a second accent exists for a second element
        self.flat = mode == "flat"
        self.sw = {"flat": 4, "dark": 3.6, "glow": 3.4, "light": 3.6}[mode]
        self.line = {"flat": INK, "dark": WHITE, "glow": WHITE, "light": INK}[mode]
        self.line_o = {"flat": 1, "dark": .86, "glow": .9, "light": .9}[mode]
        self.sh = 14

    def _attrs(self, kw):
        return " ".join(f'{k.rstrip("_").replace("_", "-")}="{v}"' for k, v in kw.items())

    def shape(self, tag, role="card", lift=True, **kw):
        """A closed shape. role: card | acc | ink | none."""
        a = self._attrs(kw)
        if self.flat:
            fill = {"card": CARD, "acc": self.acc, "acc2": self.acc2, "ink": INK, "none": "none"}[role]
            out = f'<{tag} {a} fill="{INK}" transform="translate({self.sh} {self.sh})"/>' if lift and role != "none" else ""
            return out + (f'<{tag} {a} fill="{fill}" stroke="{INK}" stroke-width="{self.sw}" '
                          f'stroke-linejoin="round"/>')
        if role in ("acc", "acc2"):
            col = self.acc if role == "acc" else self.acc2
            filt = ' filter="url(#glow-acc)"' if self.mode == "glow" else ""
            return (f'<{tag} {a} fill="{col}" fill-opacity=".16" stroke="{col}" stroke-width="{self.sw + .6}" '
                    f'stroke-linejoin="round"{filt}/>')
        if role == "ink":
            return f'<{tag} {a} fill="{self.line}" fill-opacity="{.75 if self.mode != "light" else .85}"/>'
        return (f'<{tag} {a} fill="none" stroke="{self.line}" stroke-opacity="{self.line_o}" stroke-width="{self.sw}" '
                f'stroke-linejoin="round"/>')

    def bar(self, x, y, w, h=12, strong=False):
        """A text-line bar (stands for words without using words)."""
        if self.flat:
            return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h / 2}" fill="{INK}" fill-opacity="{.85 if strong else .32}"/>'
        o = (.8 if strong else .38) if self.mode != "light" else (.85 if strong else .35)
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h * .8:.1f}" rx="{h * .4:.1f}" fill="{self.line}" fill-opacity="{o}"/>'

    def stroke(self, d, role="line", width=None, lift=False, dash=None, cap="round"):
        """An open path. role: line | acc | acc2."""
        w = width or self.sw
        da = f' stroke-dasharray="{dash}"' if dash else ""
        if self.flat:
            col = INK if role == "line" else self.acc
            out = ""
            if lift:
                out += (f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{w}" stroke-linecap="{cap}" '
                        f'stroke-linejoin="round" transform="translate({self.sh} {self.sh})"/>')
            if role == "acc":       # an accent stroke in flat mode: ink edge, accent core
                out += (f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{w + 7}" stroke-linecap="{cap}" '
                        f'stroke-linejoin="round"{da}/>')
            return out + (f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linecap="{cap}" '
                          f'stroke-linejoin="round"{da}/>')
        col, o = {"acc": (self.acc, 1), "acc2": (self.acc2, 1)}.get(role, (self.line, self.line_o))
        accented = role in ("acc", "acc2")
        filt = ' filter="url(#glow-acc)"' if (self.mode == "glow" and accented) else ""
        w = w if self.flat or accented or w < self.sw * 1.5 else max(self.sw, w * .5)
        return (f'<path d="{d}" fill="none" stroke="{col}" stroke-opacity="{o}" stroke-width="{w}" stroke-linecap="{cap}" '
                f'stroke-linejoin="round"{da}{filt}/>')

    def dot(self, cx, cy, r, role="card", lift=False):
        return self.shape("circle", role, lift, cx=cx, cy=cy, r=r)

    def check(self, cx, cy, s=1.0, role="line"):
        d = f"M{cx - 26 * s:.1f} {cy:.1f} l{18 * s:.1f} {18 * s:.1f} l{36 * s:.1f} {-38 * s:.1f}"
        return self.stroke(d, role, width=max(self.sw, 9 * s) if self.flat else self.sw + 1)

    def icon(self, name, x, y, size, role="line"):
        """A Phosphor icon: fill weight in flat mode, regular weight as lines in the others."""
        if self.flat:
            return phosphor_svg(name, x, y, size, INK if role != "acc" else self.acc, "fill")
        col = self.acc if role == "acc" else self.line
        filt = ' filter="url(#glow-acc)"' if (self.mode == "glow" and role == "acc") else ""
        return f'<g{filt}>' + phosphor_svg(name, x, y, size, col, "regular", self.line_o if role != "acc" else 1) + "</g>"


# ---------------------------------------------------------------- subjects (canvas units, centred near 600, 330)
def s_prd(p):
    o = p.shape("rect", "card", x=440, y=120, width=320, height=410, rx=12)
    o += p.stroke("M440 198 H760")
    o += p.bar(474, 148, 150, 16, True)
    for i, w in enumerate((250, 210, 236, 160)):
        o += p.bar(474, 230 + i * 30, w)
    for i in range(3):                                   # the decisions an engineer needs, as a checklist
        y = 370 + i * 46
        o += p.shape("rect", "acc" if i < 2 else "card", lift=False, x=474, y=y, width=28, height=28, rx=5)
        o += p.bar(520, y + 8, (190, 150, 170)[i])
        if i < 2:
            o += p.stroke(f"M480 {y + 14} l7 7 l14 -16", width=5 if p.flat else p.sw)
    o += p.dot(764, 140, 50, "acc2", lift=True)          # the approval badge
    o += p.check(766, 140, .9)
    return o


def s_usability(p):
    o = p.shape("rect", "card", x=330, y=140, width=470, height=320, rx=12)
    o += p.stroke("M330 192 H800")
    for i in range(3):
        o += p.dot(358 + i * 24, 166, 7, "none")
    o += p.shape("rect", "card", lift=False, x=362, y=222, width=190, height=118, rx=6)
    for i, w in enumerate((190, 150, 170)):
        o += p.bar(578, 230 + i * 30, w, 12, i == 0)
    o += p.shape("rect", "acc2", lift=False, x=362, y=372, width=128, height=46, rx=23)
    # the magnifier over the button the participant is hunting for
    o += p.stroke("M800 470 L888 560", width=34 if p.flat else 10, lift=True, cap="round")
    if p.flat:
        o += p.stroke("M800 470 L888 560", width=20, cap="round").replace(f'stroke="{INK}"', f'stroke="{CARD}"', 1)
    o += p.dot(740, 410, 98, "card", lift=True)
    o += p.dot(740, 410, 74, "acc")
    o += p.shape("path", "card", lift=False, d="M712 368 l0 92 l22 -20 l16 36 l18 -8 l-16 -35 l30 -3 z")
    return o


def s_roadmap(p):
    o = p.stroke("M250 470 H950", width=10 if p.flat else p.sw + 1, lift=True)
    xs = (320, 500, 680, 860)
    tops = (300, 210, 280, 190)
    for i, (x, t) in enumerate(zip(xs, tops)):
        o += p.stroke(f"M{x} {t + 104} V458", width=4 if p.flat else p.sw)
        role = "acc" if i == 2 else "card"
        o += p.shape("rect", role, x=x - 78, y=t, width=156, height=104, rx=10)
        o += p.bar(x - 56, t + 26, 92, 14, True)
        o += p.bar(x - 56, t + 56, 112)
        o += p.bar(x - 56, t + 78, 70)
        o += p.dot(x, 470, 17, "acc" if i == 2 else "card", lift=False)
    o += p.stroke("M950 470 V350", width=5 if p.flat else p.sw)
    o += p.shape("path", "acc2", d="M950 350 h70 l-18 24 l18 24 h-70 z")
    return o


def s_retention(p):
    o = p.shape("rect", "card", x=310, y=130, width=580, height=400, rx=12)
    o += p.stroke("M370 180 V470 H850", width=4 if p.flat else p.sw)
    pts = [(380, 200), (450, 300), (520, 360), (590, 392), (660, 408), (730, 416), (800, 420), (840, 421)]
    d = "M" + " L".join(f"{x} {y}" for x, y in pts)
    o += p.stroke("M370 330 H860", dash="12 10", width=3 if p.flat else p.sw - .6)
    o += p.stroke(d, "line", width=7 if p.flat else p.sw + 1.4)
    for x, y in pts[:-2:2]:
        o += p.dot(x, y, 10, "card" if p.flat else "none")
    o += p.dot(800, 420, 22, "acc", lift=p.flat)         # where retention flattens: the point that matters
    return o


def s_persona(p):
    o = p.shape("rect", "card", x=350, y=170, width=500, height=320, rx=14)
    o += p.dot(470, 290, 76, "acc", lift=False)
    if p.flat:
        o += f'<circle cx="470" cy="270" r="28" fill="{CARD}" stroke="{INK}" stroke-width="{p.sw}"/>'
        o += (f'<path d="M418 345 a52 46 0 0 1 104 0 z" fill="{CARD}" stroke="{INK}" stroke-width="{p.sw}" '
              f'stroke-linejoin="round"/>')
    else:
        o += p.dot(470, 270, 28, "none") + p.shape("path", "none", d="M418 345 a52 46 0 0 1 104 0 z")
    o += p.bar(580, 232, 200, 18, True)
    o += p.bar(580, 274, 230)
    o += p.bar(580, 304, 180)
    o += p.bar(580, 334, 210)
    for i, (x, w) in enumerate(((390, 120), (528, 140), (686, 120))):
        o += p.shape("rect", "acc2" if i == 1 else "card", lift=False, x=x, y=410, width=w, height=44, rx=22)
    return o


def s_research_plan(p):
    o = p.shape("rect", "card", x=430, y=140, width=340, height=400, rx=14)
    o += p.shape("rect", "ink" if p.flat else "none", lift=False, x=530, y=116, width=140, height=50, rx=10)
    for i in range(4):
        y = 214 + i * 74
        if i == 2:                                       # the question still open: the row that matters
            o += p.shape("rect", "acc", lift=False, x=454, y=y - 16, width=292, height=62, rx=8)
        o += p.shape("rect", "acc2" if i < 2 and p.acc2 != p.acc else "card", lift=False, x=470, y=y, width=30,
                     height=30, rx=6)
        o += p.bar(522, y + 9, (180, 150, 196, 130)[i], 12, i < 2)
        if i < 2:
            o += p.stroke(f"M476 {y + 15} l8 8 l14 -17", width=5 if p.flat else p.sw)
    return o


def s_matrix(p):
    o = p.shape("rect", "card", x=400, y=120, width=400, height=400, rx=6)
    o += p.stroke("M600 120 V520") + p.stroke("M400 320 H800")
    axis = "acc2" if (p.two and not p.flat) else "line"  # trio in the line styles: the axes carry accent 2
    aw = 4 if p.flat else p.sw - .4
    o += p.stroke("M370 540 V110", axis, width=aw) + p.stroke("M360 124 l10 -14 l10 14", axis, width=aw)
    o += p.stroke("M380 550 H812", axis, width=aw) + p.stroke("M798 540 l14 10 l-14 10", axis, width=aw)
    for (x, y, r, role) in ((480, 200, 24, "acc"), (540, 260, 14, "card"), (680, 190, 14, "card"), (720, 260, 14, "card"),
                            (470, 420, 14, "card"), (700, 450, 14, "card"), (650, 380, 14, "card")):
        o += p.dot(x, y, r, role if p.flat else ("acc" if role == "acc" else "none"), lift=role == "acc" and p.flat)
    return o


def s_design_system(p):
    o = ""
    tw, th, g = 160, 120, 26
    x0, y0 = 600 - (3 * tw + 2 * g) / 2, 330 - (2 * th + g) / 2 - 10
    for k in range(6):
        x, y = x0 + (k % 3) * (tw + g), y0 + (k // 3) * (th + g)
        role = "acc" if k == 4 else "card"
        o += p.shape("rect", role, x=x, y=y, width=tw, height=th, rx=10)
        cx, cy = x + tw / 2, y + th / 2
        if k == 0:      # button
            o += p.shape("rect", "ink" if p.flat else "acc", lift=False, x=cx - 52, y=cy - 18, width=104, height=36, rx=18)
        elif k == 1:    # toggle
            o += p.shape("rect", "card", lift=False, x=cx - 40, y=cy - 20, width=80, height=40, rx=20)
            o += p.dot(cx + 20, cy, 14, "ink" if p.flat else "none")
        elif k == 2:    # swatches
            for i in range(3):
                o += p.dot(cx - 40 + i * 40, cy, 16, ("ink", "acc2", "card")[i] if p.flat else ("none", "acc2", "none")[i])
        elif k == 3:    # input
            o += p.shape("rect", "card", lift=False, x=cx - 58, y=cy - 18, width=116, height=36, rx=6)
            o += p.bar(cx - 46, cy - 5, 50, 10)
        elif k == 4:    # type scale
            o += p.bar(cx - 56, cy - 30, 100, 18, True) + p.bar(cx - 56, cy + 2, 80) + p.bar(cx - 56, cy + 24, 60)
        else:           # slider
            o += p.stroke(f"M{cx - 56} {cy} H{cx + 56}", width=6 if p.flat else p.sw)
            o += p.dot(cx + 12, cy, 14, "card")
    return o


def s_sprint(p):
    o = ""
    r, cx, cy = 215, 600, 330
    def arc(a0, a1):
        x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
        x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
        return f"M{x0:.1f} {y0:.1f} A{r} {r} 0 0 1 {x1:.1f} {y1:.1f}", (x1, y1), a1
    for a0, a1 in ((200, 330), (20, 150)):
        d, (x1, y1), a = arc(a0, a1)
        o += p.stroke(d, "acc" if a0 == 20 else "line", width=12 if p.flat else p.sw + 1, lift=a0 != 20)
        t = math.radians(a + 90)                          # tangent direction for the arrowhead
        nx, ny = math.cos(t), math.sin(t)
        px, py = -ny, nx
        head = (f"M{x1 + nx * 26:.1f} {y1 + ny * 26:.1f} L{x1 + px * 18:.1f} {y1 + py * 18:.1f} "
                f"L{x1 - px * 18:.1f} {y1 - py * 18:.1f} Z")
        o += p.shape("path", "acc" if a0 == 20 else "ink", lift=False, d=head)
    o += p.shape("rect", "card", x=455, y=240, width=290, height=180, rx=10)
    for i in range(3):
        x = 472 + i * 92
        o += p.bar(x, 256, 70, 10, True)
        for j in range(3 - i):
            o += p.shape("rect", "acc2" if (i == 1 and j == 0) else "card", lift=False, x=x, y=280 + j * 42, width=76, height=32, rx=5)
    return o


def s_hiring(p):
    o = p.shape("rect", "card", x=380, y=230, width=440, height=290, rx=20)
    o += p.shape("path", "none", lift=False, d="M530 230 v-42 a14 14 0 0 1 14 -14 h112 a14 14 0 0 1 14 14 v42")
    if p.flat:
        o += f'<path d="M530 230 v-42 a14 14 0 0 1 14 -14 h112 a14 14 0 0 1 14 14 v42" fill="none" stroke="{INK}" stroke-width="16"/>'
    o += p.stroke("M380 330 H820")
    o += p.shape("rect", "acc", lift=False, x=568, y=310, width=64, height=42, rx=6)
    # the hiring guide's tag: a candidate card with a check
    o += p.stroke("M760 352 C790 380 800 400 806 420", width=4 if p.flat else p.sw - .4)
    o += p.shape("rect", "card", x=760, y=410, width=170, height=120, rx=10)
    o += p.dot(800, 452, 22, "acc2")
    o += p.bar(834, 444, 70, 12, True) + p.bar(834, 468, 54)
    o += p.check(810, 500, .55)
    return o


def s_icon(p, name):
    if p.flat:
        return p.dot(600, 320, 170, "card", lift=True) + p.icon(name, 600 - 120, 320 - 120, 240)
    return p.dot(600, 320, 170, "acc") + p.icon(name, 600 - 120, 320 - 120, 240)


# key: (one-noun visual, draw function, Pixelarticons glyph, Phosphor silhouette, default steps for style 4)
SUBJECTS = {
    "prd": ("document", s_prd, "file-text", "file-text", ["note", "users", "list-checks", "check-circle"]),
    "usability-test": ("magnifier", s_usability, "search", "magnifying-glass",
                       ["clipboard-text", "eye", "note", "wrench"]),
    "roadmap": ("timeline", s_roadmap, "flag", "flag", ["lightbulb", "flask", "rocket-launch", "chart-line-up"]),
    "retention-chart": ("curve", s_retention, "chart-line", "chart-line-down", None),
    "persona": ("profile card", s_persona, "avatar-square", "user-circle", None),
    "research-plan": ("clipboard", s_research_plan, "clipboard-note", "clipboard-text",
                      ["question", "users", "chats-circle", "lightbulb"]),
    "prioritization-matrix": ("matrix", s_matrix, "grid-2x2-2", "squares-four", None),
    "design-system": ("component grid", s_design_system, "blocks", "stack", None),
    "sprint": ("loop", s_sprint, "reload", "arrows-clockwise", ["kanban", "code", "presentation-chart", "chats-circle"]),
    "hiring-guide": ("briefcase", s_hiring, "briefcase", "briefcase", ["file-text", "chats-circle", "scales", "handshake"]),
}


# where the flat styles' flow lines run in from the left edge: (first line's y, x where they meet the subject)
FLOWS = {"prd": (300, 440), "usability-test": (290, 330), "roadmap": (448, 250), "retention-chart": (300, 310),
         "persona": (300, 350), "research-plan": (330, 430), "prioritization-matrix": (190, 370),
         "design-system": (300, 349), "hiring-guide": (400, 380)}


def subject_parts(spec):
    """(noun, draw(pen), pixel glyph, phosphor silhouette, steps) for the spec's subject."""
    sub = spec.get("subject", "")
    if sub.startswith("icon:"):
        name = sub[5:]
        phosphor(name)                                   # raises if missing
        pix = spec.get("pixel") or (name if (VENDOR / "pixelarticons" / f"{name}.svg").exists() else None)
        return name, (lambda p: s_icon(p, name)), pix, name, spec.get("steps")
    if sub not in SUBJECTS:
        raise SpecError(f"Unknown subject {sub!r}. Use one of {', '.join(SUBJECTS)} or icon:<phosphor-name>.")
    noun, fn, pix, sil, steps = SUBJECTS[sub]
    return noun, fn, spec.get("pixel") or pix, spec.get("silhouette") or sil, spec.get("steps") or steps


# ---------------------------------------------------------------- shared helpers
def svg_open(bg, defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
            f'<defs>{defs}</defs><rect width="{W}" height="{H}" fill="{bg}"/>')


def square_grid(color, opacity, step=60, width=2):
    o = "".join(f'<path d="M{x} 0V{H}"/>' for x in range(0, W + 1, step))
    o += "".join(f'<path d="M0 {y}H{W}"/>' for y in range(15, H + 1, step))
    return f'<g stroke="{color}" stroke-opacity="{opacity}" stroke-width="{width}">{o}</g>'


def dot_grid(color, opacity, step=30, r=2.4, uid="dg"):
    return (f'<pattern id="{uid}" width="{step}" height="{step}" patternUnits="userSpaceOnUse">'
            f'<circle cx="{step / 2}" cy="{step / 2}" r="{r}" fill="{color}" fill-opacity="{opacity}"/></pattern>',
            f'<rect width="{W}" height="{H}" fill="url(#{uid})"/>')


def _logo(name):
    t = (LOGO / name).read_text(encoding="utf-8")
    vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', t).group(1).split()]
    # the lockup's own markup, as drawn: the mark is one evenodd path (the figure is a true hole) inside a
    # positioning group, so it is copied whole rather than re-filled path by path
    inner = re.sub(r"^.*?<svg[^>]*>", "", t, flags=re.S).rsplit("</svg>", 1)[0]
    return vb, re.sub(r"<title>.*?</title>", "", inner, flags=re.S)


def brand_color(bg):
    """The white or the black logo, whichever contrasts more with the background."""
    return "white" if contrast(WHITE, bg) > contrast("#0B0B0C", bg) else "black"


def brand_box(size, corner):
    """(x, y, w, h) in canvas units (the 1200 canvas) for the lockup on one output size ("hero" or "thumb")."""
    vb, _ = _logo("lockup-white.svg")
    k = W / OUT_W[size]                                  # output pixels to canvas units
    w = LOCKUP_PX[size] * k
    h, m = w * vb[3] / vb[2], LOCKUP_MARGIN_PX[size] * k
    x = W - m - w if corner in ("br", "tr") else m
    y = H - m - h if corner in ("br", "bl") else m
    return x, y, w, h


def brand(size, bg, corner="br"):
    """The full lockup for one output size ("hero" or "thumb"), white or black by contrast, quiet, in one corner."""
    col = brand_color(bg)
    x, y, w, h = brand_box(size, corner)
    vb, inner = _logo(f"lockup-{col}.svg")       # lockup-white.svg is all #FFFFFF, lockup-black.svg all #0B0B0C
    return (f'<svg x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" viewBox="{" ".join(f"{v:g}" for v in vb)}" '
            f'opacity="{LOCKUP_O}">{inner}</svg>')


def free_corner(img, bg):
    """(corner, clear): the first corner (br, bl, tr, tl) where the lockup of both sizes, with a margin, would not
    touch the subject. The thumb's lockup takes the larger share of the canvas, so both boxes are tested. When no
    corner is clear, ("br", False): the subject has to move or shrink (never the lockup)."""
    a = np.asarray(img.resize((W, H), Image.BOX)).astype(np.float32)
    d = np.sqrt(((a - np.array(hex_rgb(bg), np.float32)) ** 2).sum(-1)) > 70
    pad = 16
    for corner in ("br", "bl", "tr", "tl"):
        ok = True
        for size in ("hero", "thumb"):
            x, y, w, h = brand_box(size, corner)
            box = d[max(0, int(y - pad)):int(y + h + pad), max(0, int(x - pad)):int(x + w + pad)]
            ok = ok and box.mean() < .01
        if ok:
            return corner, True
    return "br", False


def flow_lines(y0, x_end, color, opacity=1, n=3, gap=22, width=3):
    return "".join(f'<path d="M0 {y0 + i * gap}H{x_end}" stroke="{color}" stroke-opacity="{opacity}" '
                   f'stroke-width="{width}"/>' for i in range(n))


def render(svg, width=W * 2):
    png = resvg_py.svg_to_bytes(svg_string=svg, width=width, height=int(width * H / W), font_files=FONT_FILES)
    return Image.open(io.BytesIO(bytes(png))).convert("RGB")


def add_grain(img, sigma, seed):
    if not sigma:
        return img
    rng = np.random.default_rng(seed)
    a = np.asarray(img).astype(np.float32)
    n = rng.normal(0, sigma, a.shape[:2])[..., None]
    return Image.fromarray(np.clip(a + n, 0, 255).astype(np.uint8))


def specks(img, seed, density=.0016, color=(29, 27, 22), alpha=.5):
    """Sparse dark specks, the paper texture of style 8."""
    rng = np.random.default_rng(seed + 1)
    a = np.asarray(img).astype(np.float32)
    m = rng.random(a.shape[:2]) < density
    a[m] = a[m] * (1 - alpha) + np.array(color, np.float32) * alpha
    return Image.fromarray(a.astype(np.uint8))


def pixel_upscale(cells_rgb, factor):
    """Nearest-neighbour upscale of a small RGB array by an integer factor (never smooth)."""
    return Image.fromarray(cells_rgb).resize((cells_rgb.shape[1] * factor, cells_rgb.shape[0] * factor), Image.NEAREST)


BAYER8 = np.array([[0, 32, 8, 40, 2, 34, 10, 42], [48, 16, 56, 24, 50, 18, 58, 26],
                   [12, 44, 4, 36, 14, 46, 6, 38], [60, 28, 52, 20, 62, 30, 54, 22],
                   [3, 35, 11, 43, 1, 33, 9, 41], [51, 19, 59, 27, 49, 17, 57, 25],
                   [15, 47, 7, 39, 13, 45, 5, 37], [63, 31, 55, 23, 61, 29, 53, 21]], np.float32)


def ordered_dither(tone, levels=2):
    """Bayer 8 x 8 ordered dither of a 0..1 darkness array to `levels` steps (0 = ground). Written in numpy
    because Pillow's ORDERED dither silently falls back to Floyd-Steinberg."""
    h, w = tone.shape
    th = (BAYER8 + .5) / 64
    t = np.tile(th, (h // 8 + 1, w // 8 + 1))[:h, :w]
    v = tone * (levels - 1)
    return np.clip(np.floor(v) + (v - np.floor(v) > t), 0, levels - 1).astype(np.int32)


def dot_screen(tone, cell=10.0, angle=45, scale=1.0, min_k=.04, max_r=.74):
    """Amplitude-modulated halftone: a rotated grid of dots whose area follows darkness (0..1). Returns a list of
    (x, y, r) in the tone array's pixel space, multiplied by `scale`."""
    h, w = tone.shape
    blur = np.asarray(Image.fromarray((tone * 255).astype(np.uint8)).filter(
        ImageFilter.BoxBlur(max(1, int(cell / 2))))).astype(np.float32) / 255
    ca, sa = math.cos(math.radians(angle)), math.sin(math.radians(angle))
    R = int(math.hypot(w, h) / cell) + 2
    u, v = np.meshgrid(np.arange(-R, R), np.arange(-R, R))
    x = (u * ca - v * sa) * cell + w / 2
    y = (u * sa + v * ca) * cell + h / 2
    ok = (x >= 0) & (x < w) & (y >= 0) & (y < h)
    x, y = x[ok], y[ok]
    k = blur[y.astype(int), x.astype(int)]
    keep = k > min_k
    r = cell * max_r * np.sqrt(k[keep])
    return list(zip(x[keep] * scale, y[keep] * scale, r * scale))


def to_ink(levels_arr, colors):
    """Palette mapping: level index array to RGB with the given hex colours (ground first)."""
    lut = np.array([[int(c[i:i + 2], 16) for i in (1, 3, 5)] for c in colors], np.uint8)
    return lut[levels_arr]


def hex_rgb(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))


# ---------------------------------------------------------------- styles
def style_flat(spec, pal, grid):
    _, draw, *_ = subject_parts(spec)
    pen = Pen("flat", pal["a"], pal["b"])
    if grid == "square":
        s = svg_open(pal["bg"]) + square_grid(INK, .10)
    else:
        pat, fill = dot_grid(INK, .17)
        s = svg_open(pal["bg"], pat) + fill
    flow = FLOWS.get(spec.get("subject"))
    if spec.get("flows", True) and flow:
        s += flow_lines(flow[0], flow[1], INK, .9)
    s += draw(pen)
    return s + "</svg>", dict(bg=pal["bg"], grain=10, texts=[])


def style_pixel(spec, pal):
    _, _, pix, _, _ = subject_parts(spec)
    if not pix:
        raise SpecError("no Pixelarticons glyph for this subject")
    cells = pixel_cells(pix)
    inside = interior(cells)
    pat, fill = dot_grid(INK, .15, step=24, r=2)
    s = svg_open(pal["bg"], pat) + fill
    c = 14                                                   # canvas units per cell; the glyph shares the grid
    pw, ph = 40, 32                                          # the pixel window, in cells
    x0, y0 = round((W - pw * c) / 2 / c) * c, round((H - ph * c) / 2 / c) * c - c
    rects = []

    def px(i, j, col, n=1, m=1):
        rects.append(f'<rect x="{x0 + i * c}" y="{y0 + j * c}" width="{n * c}" height="{m * c}" fill="{col}"/>')
    px(1, 1, INK, pw, ph)                                    # one-cell hard shadow
    px(0, 0, CARD, pw, ph)
    px(0, 0, INK, pw, 1); px(0, ph - 1, INK, pw, 1); px(0, 3, INK, pw, 1)
    px(0, 0, INK, 1, ph); px(pw - 1, 0, INK, 1, ph)
    for k in range(3):                                       # title-bar buttons
        px(2 + k * 2, 1, INK, 1, 2)                          # decoration stays in ink
    for k, n in enumerate((9, 6, 8, 5, 7)):                  # pixel text lines beside the glyph
        px(28, 8 + k * 4, INK, n, 1)
    gi, gj = 2, 5                                            # glyph origin, in window cells
    for j in range(24):
        for i in range(24):
            if cells[j, i]:
                px(gi + i, gj + j, INK)
            elif inside[j, i]:
                px(gi + i, gj + j, pal["a"] if (i % 2 == 0 and j % 2 == 0) else CARD)   # sparse dither
    s += "".join(rects)
    for (x, y) in ((x0 - 70, y0 + 60), (x0 + pw * c + 60, y0 + ph * c - 80)):   # pixel sparks
        for dx, dy in ((0, 0), (-10, -10), (10, -10), (-10, 10), (10, 10)):
            s += f'<rect x="{x + dx}" y="{y + dy}" width="10" height="10" fill="{INK}"/>'
    s += "</svg>"
    return s, dict(bg=pal["bg"], grain=0, texts=[])


def style_sequence(spec, pal):
    _, _, _, _, steps = subject_parts(spec)
    if not steps or not 3 <= len(steps) <= 5:
        raise SpecError("needs a sequence of 3 to 5 steps (the subject has none)")
    n = len(steps)
    focus = spec.get("focus", 1 if n > 2 else 0)
    grid = spec.get("grid") or ("dot" if _hash(spec["slug"], "grid") % 2 else "square")
    if grid == "square":
        s = svg_open(pal["bg"]) + square_grid(INK, .09)
    else:
        pat, fill = dot_grid(INK, .16)
        s = svg_open(pal["bg"], pat) + fill
    r, gap = (86, 74) if n <= 4 else (74, 52)
    total = n * 2 * r + (n - 1) * gap
    x0, cy = (W - total) / 2 + r, 300
    # the track: a long rounded bar with rivets, like a conveyor
    tx0, tx1, ty = x0 - r - 30, x0 + (n - 1) * (2 * r + gap) + r + 30, cy + r + 30
    s += (f'<rect x="{tx0}" y="{ty - 22}" width="{tx1 - tx0}" height="44" rx="22" fill="none" stroke="{INK}" '
          f'stroke-width="3"/>')
    for k in range(int((tx1 - tx0) // 70)):
        s += f'<circle cx="{tx0 + 40 + k * 70}" cy="{ty}" r="6" fill="none" stroke="{INK}" stroke-width="2.5"/>'
    s += flow_lines(150, 330, INK, .85, n=3, gap=16, width=2.5)
    texts = []
    for i, name in enumerate(steps):
        cx = x0 + i * (2 * r + gap)
        fill = pal["a"] if i == focus else CARD
        s += f'<circle cx="{cx + 12}" cy="{cy + 12}" r="{r}" fill="{INK}"/>'
        s += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{INK}" stroke-width="3.5"/>'
        isz = r * 1.05
        s += phosphor_svg(name, cx - isz / 2, cy - isz / 2, isz, INK, "regular")
        # the step number on a small ink tag
        tx, ty2 = cx - r * .72, cy - r * .72
        s += f'<circle cx="{tx}" cy="{ty2}" r="22" fill="{INK}"/>'
        s += (f'<text x="{tx}" y="{ty2 + 8.5}" text-anchor="middle" font-family="{TYPE_FAMILY}" font-weight="700" '
              f'font-size="24" fill="{CARD}">{i + 1}</text>')
        texts.append((f"step {i + 1}", CARD, INK))
    s += "</svg>"
    return s, dict(bg=pal["bg"], grain=10, texts=texts)


def _title_cells(lines, size):
    """Pixel type: the title set in Space Grotesk at a tiny size and thresholded, one cell per pixel."""
    font = ImageFont.truetype(str(TYPE_FONT), size)
    asc, desc = font.getmetrics()
    lh = int((asc + desc) * 1.02)
    wmax = max(int(font.getlength(t)) for t in lines) + 4
    im = Image.new("L", (wmax, lh * len(lines) + 4), 0)
    d = ImageDraw.Draw(im)
    for k, t in enumerate(lines):
        d.text((2, 2 + k * lh), t, font=font, fill=255)
    a = np.asarray(im) > 110
    rows = np.where(a.any(1))[0]
    cols = np.where(a.any(0))[0]
    return a[rows[0]:rows[-1] + 1, cols[0]:cols[-1] + 1]


def _wrap(words, fits):
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if fits(t) or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w
    return lines + ([cur] if cur else [])


def style_type(spec, pal):
    title = (spec.get("cover_title") or spec.get("title") or "").strip()
    if not title:
        raise SpecError("needs a short title")
    if len(title) > 48:
        raise SpecError(f"title too long for a cover ({len(title)} characters; keep it under 48)")
    _, _, pix, _, _ = subject_parts(spec)
    bg = pal["bg"]
    dark = pal["ink"] == WHITE
    col = pal["a"] if (pal["accents"] and contrast(pal["a"], bg) >= 4.5) else pal["ink"]
    obj_w = 300 if pix else 0
    max_w = W - 96 - 96 - obj_w - (60 if pix else 0)
    best = None
    for cell in (8, 7, 6, 5):                            # pixel type: biggest cell size whose wrap fits 3 lines
        for size in (18, 16, 15):
            font = ImageFont.truetype(str(TYPE_FONT), size)
            lines = _wrap(title.split(), lambda t: font.getlength(t) * cell <= max_w)
            if len(lines) <= 3 and all(font.getlength(t) * cell <= max_w for t in lines):
                best = (cell, size, lines)
                break
        if best:
            break
    if dark:
        pat, fill = dot_grid(WHITE, .07, step=24, r=1.8)
    else:
        pat, fill = dot_grid(INK, .14, step=24, r=1.8)
    s = svg_open(bg, pat) + fill
    texts = []
    if best:
        cell, size, lines = best
        cells = _title_cells(lines, size)
        th, tw = cells.shape[0] * cell, cells.shape[1] * cell
        x0, y0 = 96, (H - th) / 2 - 10
        rects = []
        for j, i in zip(*np.nonzero(cells)):
            rects.append(f'<rect x="{x0 + i * cell}" y="{y0 + j * cell:.0f}" width="{cell}" height="{cell}"/>')
        s += f'<g fill="{col}">{"".join(rects)}</g>'
        texts.append(("title", col, bg))
        tx_end, t_mid = x0 + tw, y0 + th / 2
    else:                                                # set type (long titles): Space Grotesk Bold
        fs = 64
        font = ImageFont.truetype(str(TYPE_FONT), fs)
        lines = _wrap(title.split(), lambda t: font.getlength(t) <= max_w)
        while len(lines) > 3 and fs > 44:
            fs -= 4
            font = ImageFont.truetype(str(TYPE_FONT), fs)
            lines = _wrap(title.split(), lambda t: font.getlength(t) <= max_w)
        lh = fs * 1.08
        y0 = (H - lh * len(lines)) / 2 + fs * .78
        for k, t in enumerate(lines):
            s += (f'<text x="96" y="{y0 + k * lh:.1f}" font-family="{TYPE_FAMILY}" font-weight="700" font-size="{fs}" '
                  f'fill="{col}" letter-spacing="-0.5">{escape(t)}</text>')
        texts.append(("title", col, bg))
        tx_end, t_mid = 96 + max(font.getlength(t) for t in lines), H / 2
    if pix:                                              # the one object: a pixel glyph, card white with ink outline
        cells_o = pixel_cells(pix)
        ins = interior(cells_o)
        g = 12
        ox, oy = W - 96 - 24 * g, t_mid - 12 * g
        ox = max(ox, tx_end + 50)
        o = []
        for j in range(24):
            for i in range(24):
                if cells_o[j, i]:
                    o.append(f'<rect x="{ox + i * g}" y="{oy + j * g:.0f}" width="{g}" height="{g}" fill="{CARD if dark else INK}"/>')
                elif ins[j, i]:
                    o.append(f'<rect x="{ox + i * g}" y="{oy + j * g:.0f}" width="{g}" height="{g}" '
                             f'fill="{pal["a"] if (i + j) % 2 == 0 else (bg if dark else CARD)}"/>')
        s += "".join(o)
    s += "</svg>"
    return s, dict(bg=bg, grain=6 if dark else 8, texts=texts)


def _bloom(uid, col, peak):
    return (f'<radialGradient id="{uid}" cx="50%" cy="50%" r="50%">'
            f'<stop offset="0" stop-color="{col}" stop-opacity="{peak:.2f}"/>'
            f'<stop offset=".55" stop-color="{col}" stop-opacity="{peak * .27:.2f}"/>'
            f'<stop offset="1" stop-color="{col}" stop-opacity="0"/></radialGradient>')


def _glow_defs(acc, acc2=None):
    """The glow filters and the bloom: one radial gradient in the accent (mono: white, duo: the accent); in a trio
    two offset blooms, each in its own accent, which blend in the middle. The only gradient any style uses."""
    peak = .30 if acc == WHITE else .26 if acc2 else .38     # mono: a white bloom, kept faint
    blooms = _bloom("bloom", acc, peak) + (_bloom("bloom2", acc2, .22) if acc2 else "")
    return (f'<filter id="glow-acc" filterUnits="userSpaceOnUse" x="0" y="0" width="{W}" height="{H}">'
            f'<feGaussianBlur stdDeviation="9" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="b"/>'
            f'<feMergeNode in="SourceGraphic"/></feMerge></filter>'
            f'<filter id="halo" x="-20%" y="-20%" width="140%" height="140%">'
            f'<feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/>'
            f'<feMergeNode in="SourceGraphic"/></feMerge></filter>' + blooms)


def style_dark(spec, pal, glow=False):
    _, draw, *_ = subject_parts(spec)
    acc = pal["a"]
    if glow:
        two = pal["b"] != pal["a"]
        s = svg_open(pal["bg"], _glow_defs(acc, pal["b"] if two else None))
        if two:     # two offset blooms: accent 1 up-left, behind the accented part; accent 2 down-right
            s += f'<ellipse cx="500" cy="270" rx="430" ry="290" fill="url(#bloom)"/>'
            s += f'<ellipse cx="720" cy="400" rx="430" ry="290" fill="url(#bloom2)"/>'
        else:
            s += f'<ellipse cx="600" cy="330" rx="520" ry="330" fill="url(#bloom)"/>'
        s += f'<g filter="url(#halo)">{draw(Pen("glow", acc, pal["b"]))}</g>'
    else:
        pat, fill = dot_grid(WHITE, .08, step=26, r=1.7)
        s = svg_open(pal["bg"], pat) + fill
        flow = FLOWS.get(spec.get("subject"))
        if flow:
            s += flow_lines(flow[0], flow[1], WHITE, .4, n=2, gap=18, width=2)
        s += draw(Pen("dark", acc, pal["b"]))
    s += "</svg>"
    return s, dict(bg=pal["bg"], grain=4, texts=[], min_coverage=.02)


def style_light(spec, pal):
    _, draw, *_ = subject_parts(spec)
    paper = pal["bg"]
    s = svg_open(paper) + square_grid(INK, .07, step=50, width=1.5)
    warm = pal["a"]
    # faint warm lines running in from the left, the ref-31 gesture, solid (no gradient)
    s += "".join(f'<path d="M80 {250 + k * 22}H300" stroke="{INK}" stroke-opacity=".25" stroke-width="2"/>'
                 for k in range(6))
    s += draw(Pen("light", warm, pal["b"]))
    s += "</svg>"
    return s, dict(bg=paper, grain=0, specks=True, texts=[], min_coverage=.02)


def _silhouette(name, box):
    """A boolean mask of a Phosphor fill icon rendered into a box (x, y, size) on the canvas, at canvas units."""
    x, y, size = box
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
           + phosphor_svg(name, x, y, size, "#000000") + "</svg>")
    png = resvg_py.svg_to_bytes(svg_string=svg, width=W, height=H)
    return np.asarray(Image.open(io.BytesIO(bytes(png))).convert("RGBA"))[..., 3] > 127


def style_particles(spec, pal):
    """Style 9 on near-black and style 10 on a saturated ground. Here the stream IS the colour (ref-07), the one
    exception to "no accent on decoration":
      mono: stream and silhouette in the ink (white on dark and deep grounds, deep ink on bright ones)
      duo and analogous: the stream in the accent at the shape end, fading to the ink at the far left; the
        silhouette in the ink
      trio: the stream in accent 1 (with the same fade), the silhouette in accent 2
    The particles keep their opacity ramp (faint at the left, solid near the shape)."""
    _, _, _, sil, _ = subject_parts(spec)
    bg = pal["bg"]
    ink = WHITE if pal["ink"] == WHITE else INK
    acc = pal["accents"]
    stream_acc = acc[0] if acc else None
    shape_col = acc[1] if len(acc) > 1 else ink

    def stream_col(t):            # t: 0 at the far left, 1 at the shape
        if not stream_acc:
            return ink
        return mix(ink, stream_acc, min(1.0, .15 + 1.1 * t))
    rng = np.random.default_rng(seed_for(spec["slug"]))
    size = 330
    bx, by = 760, (H - size) / 2 - 10
    mask = _silhouette(sil, (bx, by, size))
    ys, xs = np.nonzero(mask)
    s = svg_open(bg)
    dots = []
    # the shape: dots on a jittered lattice inside the silhouette
    for gy in range(int(by), int(by + size), 7):
        for gx in range(int(bx), int(bx + size), 7):
            jx, jy = gx + rng.normal(0, 1), gy + rng.normal(0, 1)
            if 0 <= int(jy) < H and 0 <= int(jx) < W and mask[int(jy), int(jx)]:
                dots.append((jx, jy, 2.7, shape_col, 1))
    # the stream: curves from the left edge converging on the silhouette's left side, denser near the shape
    tx = xs.min() if len(xs) else bx
    cy0 = (ys.min() + ys.max()) / 2 if len(ys) else H / 2
    for k in range(64):
        y0 = 70 + k * (H - 140) / 63 + rng.normal(0, 3)
        y1 = cy0 + (y0 - H / 2) * .16 + rng.normal(0, 4)
        n = 70
        for t in np.linspace(0, 1, n) ** .8:
            e = t * t * (3 - 2 * t)
            x = 60 + (tx - 70) * t
            y = y0 + (y1 - y0) * e
            if rng.random() < .25 + .65 * t:
                r = 1.4 + 1.5 * t
                dots.append((x + rng.normal(0, 1.5), y + rng.normal(0, 1.2), r, stream_col(t), .3 + .5 * t))
    s += "".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{c}" fill-opacity="{o:.2f}"/>'
                 for x, y, r, c, o in dots)
    s += "</svg>"
    return s, dict(bg=bg, grain=4 if pal["kind"] == "dark" else 7, texts=[])


def style_photo(spec, pal):
    path = spec.get("photo")
    if not path or not Path(path).exists():
        raise SpecError("needs the owner's photo (photo path missing or not found)")
    src = ImageOps.exif_transpose(Image.open(path)).convert("L")
    src = ImageOps.autocontrast(src, cutoff=1)
    # fit the photo into the subject area (about 62 percent of the width), centred
    aw, ah = 760, 540
    scale = min(aw / src.width, ah / src.height)
    pw, ph = int(src.width * scale), int(src.height * scale)
    S = 2                                                     # work at 2400 x 1350
    tone = np.zeros((H * S, W * S), np.float32)
    im = src.resize((pw * S, ph * S), Image.LANCZOS)
    t = 1 - np.asarray(im).astype(np.float32) / 255
    # feather the edges so the photo dissolves into the ground instead of sitting in a frame
    ry = np.abs(np.linspace(-1, 1, ph * S))[:, None]
    rx = np.abs(np.linspace(-1, 1, pw * S))[None, :]
    d = (rx ** 4 + ry ** 4) ** .25                           # a superellipse: square-ish middle, round corners
    feather = np.clip((1 - d) / .38, 0, 1)
    feather = feather * feather * (3 - 2 * feather)          # smoothstep, so there is no visible edge or frame
    t = np.clip((t - .06) * 1.2, 0, 1) * feather
    ox, oy = (W * S - pw * S) // 2, (H * S - ph * S) // 2 - 10 * S
    tone[oy:oy + ph * S, ox:ox + pw * S] = t
    method = spec.get("photo_method", "screen")
    pat, fill = dot_grid(INK, .12, step=24, r=1.8)
    svg = svg_open(pal["bg"], pat) + fill
    if method == "bayer":
        small = Image.fromarray((tone * 255).astype(np.uint8)).resize((W // 5, H // 5), Image.BOX)
        lv = ordered_dither(np.asarray(small).astype(np.float32) / 255, levels=3)
        rgb = to_ink(lv, [pal["bg"], mix(pal["bg"], INK, .55), INK])
        alpha = (lv > 0).astype(np.uint8) * 255
        layer = Image.fromarray(np.dstack([rgb, alpha]), "RGBA").resize((W * S, H * S), Image.NEAREST)
        base = render(svg + "</svg>")
        base.paste(layer, (0, 0), layer)
        return None, dict(bg=pal["bg"], grain=0, texts=[], raster=base)
    dots = dot_screen(tone, cell=11 * S, angle=45, scale=1 / S)
    svg += f'<g fill="{INK}">' + "".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.2f}"/>' for x, y, r in dots) + "</g>"
    svg += "</svg>"
    return svg, dict(bg=pal["bg"], grain=0, texts=[])


def render_mask(fragment):
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">{fragment}</svg>'
    png = resvg_py.svg_to_bytes(svg_string=svg, width=W * 2, height=H * 2)
    return Image.open(io.BytesIO(bytes(png))).convert("RGBA").split()[-1]


# ---------------------------------------------------------------- checks
def _lum255(rgb):
    v = np.asarray(rgb, np.float32) / 255
    v = np.where(v <= .03928, v / 12.92, ((v + .055) / 1.055) ** 2.4)
    return .2126 * v[..., 0] + .7152 * v[..., 1] + .0722 * v[..., 2]


def check_image(img, meta):
    """Label contrast for any text, and whether the subject reads at 300 px wide: coverage of non-ground pixels,
    contrast between the subject's strongest pixels and the ground, and the margin around the subject."""
    out = {"texts": [], "read_300": {}}
    for label, fg, bg in meta.get("texts", []):
        c = contrast(fg, bg)
        out["texts"].append({"label": label, "fg": fg, "bg": bg, "ratio": round(c, 2), "pass": c >= 4.5})
    small = img.resize((CHECK_W, round(CHECK_W * H / W)), Image.LANCZOS)
    a = np.asarray(small).astype(np.float32)
    bg = np.array(hex_rgb(meta["bg"]), np.float32)
    dist = np.sqrt(((a - bg) ** 2).sum(-1))
    mask = dist > 48
    # the lockup is not the subject
    for (bx, by, bw, bh) in meta.get("brand_boxes", []):
        f = CHECK_W / W
        mask[max(0, int(by * f) - 2):int((by + bh) * f) + 2, max(0, int(bx * f) - 2):int((bx + bw) * f) + 2] = False
    cov = float(mask.mean())
    lb = float(_lum255(bg))
    if mask.any():
        ls = _lum255(a[mask])
        ratios = (np.maximum(ls, lb) + .05) / (np.minimum(ls, lb) + .05)
        strong = float(np.percentile(ratios, 90))
        rows = np.where(mask.mean(1) > .03)[0]
        cols = np.where(mask.mean(0) > .03)[0]
        bbox = [int(cols.min()), int(rows.min()), int(cols.max()), int(rows.max())] if len(rows) and len(cols) else None
    else:
        strong, bbox = 1.0, None
    lo = meta.get("min_coverage", .04)                   # line styles carry less ink by design
    ok = lo <= cov <= .6 and strong >= 3.0
    out["read_300"] = {"coverage": round(cov, 3), "subject_contrast_p90": round(strong, 2), "bbox_300": bbox,
                       "pass": ok}
    out["pass"] = ok and all(t["pass"] for t in out["texts"])
    return out, small


# ---------------------------------------------------------------- make
def resolve_style(spec, history=None):
    """(style, reason, kind, candidates). An override needs a reason; a photo selects style 11; otherwise the
    article's kind (given, or classified from the title) limits the rotation to the styles that suit it."""
    kind = spec.get("kind") or classify_kind(spec.get("title", ""), spec.get("subject", ""))
    if kind not in KINDS_OF_ARTICLE:
        raise SpecError(f"Unknown kind {kind!r}; use one of {', '.join(KINDS_OF_ARTICLE)}.")
    cands = suitable_styles(kind)
    if spec.get("style"):
        st = int(spec["style"])
        if st not in STYLES:
            raise SpecError(f"style {st} does not exist (1 to 11)")
        if not spec.get("reason"):
            raise SpecError("A style override needs a reason.")
        return st, f"override: {spec['reason']}", kind, cands
    if spec.get("photo"):
        return PHOTO_STYLE, f"{KINDS_OF_ARTICLE[kind]}; the owner supplied a photo, so style 11", kind, cands
    key = spec["index"] if isinstance(spec.get("index"), int) else spec["slug"]
    st, cands, why = pick_for_kind(kind, key, history)
    return st, why, kind, cands


def draw_style(st, spec, pal):
    if st == 1:
        return style_flat(spec, pal, "square")
    if st == 2:
        return style_flat(spec, pal, "dot")
    if st == 3:
        return style_pixel(spec, pal)
    if st == 4:
        return style_sequence(spec, pal)
    if st == 5:
        return style_type(spec, pal)
    if st == 6:
        return style_dark(spec, pal)
    if st == 7:
        return style_dark(spec, pal, glow=True)
    if st == 8:
        return style_light(spec, pal)
    if st in (9, 10):
        return style_particles(spec, pal)
    return style_photo(spec, pal)


def make(spec, out_dir, name=None, history=True):
    """Draw the spec's thumbnail. When the chosen style cannot carry the subject, fall to the next style in the
    rotation and record why. Colours: spec palette or bg/accent, else a suggested palette that suits the style and
    avoids the last backgrounds in the history file. Writes <name>-hero.png and <name>-thumb.png (both with the
    lockup), <name>.svg (the hero source, when vector) and <name>-check-300.png; returns a dict with
    the style, colours, corner, notes and checks. history=False leaves the history file alone (galleries)."""
    if not spec.get("slug"):
        raise SpecError("A spec needs the article slug.")
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    name = name or spec["slug"]
    hist = load_history() if history else []
    st, why, kind, cands = resolve_style(spec, hist)
    notes, tried = [], []
    while True:
        try:
            pal = resolve_palette(spec, st, hist)
            svg, meta = draw_style(st, spec, pal)
            break
        except SpecError as e:
            if str(e).startswith("Unknown palette"):
                raise
            tried.append(st)
            nxt = next_style(st, cands) if st != PHOTO_STYLE else pick_for_kind(
                kind, spec["index"] if isinstance(spec.get("index"), int) else spec["slug"], hist)[0]
            notes.append(f"style {st} cannot carry it ({e}); fell to style {nxt}")
            st = nxt
            if st in tried:
                raise
    raster = meta.pop("raster", None)
    base = raster or render(svg)
    bg = meta["bg"]
    corner, clear = free_corner(base, bg)
    if raster is None:
        hero_svg = svg[:-len("</svg>")] + brand("hero", bg, corner) + "</svg>"
        thumb_svg = svg[:-len("</svg>")] + brand("thumb", bg, corner) + "</svg>"
        hero_big, thumb_big = render(hero_svg), render(thumb_svg)
    else:
        hero_svg = None
        hero_big, thumb_big = raster.copy(), raster.copy()
        for img, size in ((hero_big, "hero"), (thumb_big, "thumb")):
            frag = brand(size, bg, corner)
            layer = render_mask_rgba(frag)
            img.paste(layer, (0, 0), layer)
    seed = seed_for(spec["slug"])
    hero = hero_big.resize(HERO, Image.LANCZOS)
    thumb = thumb_big.resize(THUMB, Image.LANCZOS)
    if meta.get("grain"):
        hero = add_grain(hero, meta["grain"], seed)
        thumb = add_grain(thumb, meta["grain"] * .8, seed)
    if meta.get("specks"):
        hero = specks(hero, seed)
        thumb = specks(thumb, seed, density=.0012, alpha=.35)
    info = PngInfo()
    recipe = {"slug": spec["slug"], "kind": kind, "candidates": cands, "style": st, "palette": pal["name"],
              "bg": pal["bg"], "scheme": pal["scheme"], "accents": pal["accents"],
              "subject": spec.get("subject"), "seed": seed, "why": why, "notes": notes}
    info.add_text("recipe", json.dumps(recipe))
    hero.save(out_dir / f"{name}-hero.png", optimize=True, pnginfo=info)
    thumb.save(out_dir / f"{name}-thumb.png", optimize=True, pnginfo=info)
    if hero_svg:
        (out_dir / f"{name}.svg").write_text('<?xml version="1.0" encoding="UTF-8"?>\n' + hero_svg, encoding="utf-8")
    col = WHITE if brand_color(bg) == "white" else "#0B0B0C"
    meta.setdefault("texts", []).append(("lockup", mix(bg, col, LOCKUP_O), bg))
    meta["brand_boxes"] = [brand_box("hero", corner)]
    checks, small = check_image(hero, meta)
    tchecks, _ = check_image(thumb.resize(HERO, Image.LANCZOS), dict(meta, brand_boxes=[brand_box("thumb", corner)]))
    checks["thumb_read_300"] = tchecks["read_300"]
    checks["lockup_clear"] = clear                       # the lockup, at both sizes, does not touch the subject
    checks["pass"] = checks["pass"] and tchecks["read_300"]["pass"] and clear
    small.save(out_dir / f"{name}-check-300.png")
    if history:
        save_history({"slug": spec["slug"], "kind": kind, "style": st, "palette": pal["name"], "bg": pal["bg"],
                      "ground": pal["kind"],
                      "scheme": pal["scheme"], "reason": why})
    return {"name": name, "kind": kind, "candidates": cands, "style": st, "style_name": STYLES[st][0], "palette": pal["name"], "bg": pal["bg"],
            "scheme": pal["scheme"], "accents": pal["accents"],
            "accent_names": [colour_name(c) for c in pal["accents"]], "ink": pal["ink"], "corner": corner, "why": why,
            "notes": notes, "checks": checks, "svg": bool(hero_svg)}


def render_mask_rgba(fragment):
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">{fragment}</svg>'
    png = resvg_py.svg_to_bytes(svg_string=svg, width=W * 2, height=H * 2)
    return Image.open(io.BytesIO(bytes(png))).convert("RGBA")


def main():
    ap = argparse.ArgumentParser(description="Draw an article thumbnail and hero image.")
    ap.add_argument("--slug")
    ap.add_argument("--subject", default="")
    ap.add_argument("--title", help="the article title (its kind is classified from it)")
    ap.add_argument("--cover-title", help="style 5's short line of type")
    ap.add_argument("--kind", choices=list(KINDS_OF_ARTICLE))
    ap.add_argument("--index", type=int)
    ap.add_argument("--photo")
    ap.add_argument("--photo-method", choices=["screen", "bayer"])
    ap.add_argument("--steps", help="comma-separated Phosphor names for style 4")
    ap.add_argument("--palette", help="a BACKGROUNDS name")
    ap.add_argument("--bg", help="custom background hex")
    ap.add_argument("--scheme", choices=list(SCHEMES))
    ap.add_argument("--accent", help="explicit accent hex (checked)")
    ap.add_argument("--style", type=int)
    ap.add_argument("--reason")
    ap.add_argument("--out", default=".")
    ap.add_argument("--no-history", action="store_true", help="do not read or write the history file")
    ap.add_argument("--rotation", type=int, help="print the style for the first N indexes")
    ap.add_argument("--palettes", action="store_true", help="print the suggested pairs and their contrast")
    a = ap.parse_args()
    if a.rotation:
        for i in range(a.rotation):
            print(i, pick_style(i), STYLES[pick_style(i)][0])
        for k in KINDS_OF_ARTICLE:
            print(f"{k:11} suits {suitable_styles(k)}")
        return
    if a.palettes:
        for n, (bg, kind) in BACKGROUNDS.items():
            ink = ink_for(bg)
            duo = scheme_accents(bg, "duo")
            d = f"duo {duo[0]} ({colour_name(duo[0])}, {contrast(duo[0], bg):.1f}:1)" if duo else "duo: none passes"
            print(f"{n:14} {bg} ink {ink} {contrast(ink, bg):.1f}:1  {d}  {kind} styles "
                  f"{[k for k, v in KINDS.items() if kind in v]}")
        return
    if not a.slug:
        ap.error("--slug is required")
    spec = {k: v for k, v in dict(slug=a.slug, subject=a.subject, title=a.title, cover_title=a.cover_title, kind=a.kind, index=a.index, photo=a.photo,
                                  photo_method=a.photo_method, palette=a.palette, bg=a.bg, scheme=a.scheme, accent=a.accent,
                                  style=a.style, reason=a.reason).items() if v is not None}
    if a.steps:
        spec["steps"] = [s.strip() for s in a.steps.split(",")]
    print(json.dumps(make(spec, a.out, history=not a.no_history), indent=2))


if __name__ == "__main__":
    main()
