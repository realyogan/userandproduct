"""Explainer illustrations on the Printables tints: a pastel background with a dark dot grid, the picture on top in
dark ink, and our full lockup (mark and wordmark) quiet in the bottom-right corner. No card, outline, border or title
inside the image. The same PNG is used on the light and the dark page. Rules: research/mockups/illustration-rules.md.
Source of the palette: research/mockups/references/printables-tints.md.

One colour per article: every explainer in an article uses the article's tint, from tint_for_article().

Canvas: 1200 x 675 (16:9). Export 1200 x 675 for figures and 600 x 338 for thumbnails (thumb=True doubles the type
floors, because a thumbnail shows at about a quarter of the canvas).

Type: Inter from research/mockups/fonts/inter/, drawn as outlines (paths) inside the SVG and shaped with HarfBuzz
through wordmark.FontRef, so every renderer draws the same letters and no font has to be installed. Labels Inter
Medium (weight "semibold" for emphasis), notes Inter Regular. Floors: LABEL 27 and NOTE 24 units (x2 for thumbnails);
a smaller size is raised to the floor with a warning (FIT_LOG). "code": True sets a label in monospace (Consolas, kept
as <text>), for code-like labels only. Every text on a fill is checked for 4.5:1: dark ink or white, whichever
passes; if neither does, the fill is lightened or darkened until one does (CONTRAST_LOG). A label wider than its
shape less 16 units a side raises FitError: enlarge the shape or shorten the label, never shrink the type.

Fills ("tint"): None or "card" (the plain box), "a" (mid highlight), "b" (deep highlight), "ink", "bg" (the tint
itself), "none". The older names "blue"/"yellow" mean "a" and "red" means "b".

Accents ("accent", on box, rrect, circle, polygon, path, glyph, badge, dot and polyline only; never on the ground, the
dots, rules, arrows, text, bands or the lockup). Mono is the default: ink and the tint's two highlights. An accent is
for the one element whose meaning needs a colour of its own, under the thumbnail scheme rule (one accent, two rarely):
  "fire"     warm orange body with a yellow core (glyphs that have a core, such as "flame")
  "warning"  red          "success"  green          "#RRGGBB" or a hue in degrees (0 to 360): derived the same way
The generator moves the accent's lightness until it passes 3:1 on its ground (the tint, or "accent_on": a fill hex)
and 3:1 against the ink outline beside it; a label on an accent fill passes 4.5:1 as on any fill; a core passes 3:1
on its body. More than two distinct accents raise AccentError; accented elements above ACCENT_SHARE (a fifth) of the
drawn elements warn, and so do two accents under 3:1 against each other. Every pair is logged in ACCENT_LOG. A glyph takes the accent on its fill, or on its stroke for
the line glyphs (check, cross, question); "accent_part": "fill" | "stroke" overrides.

Primitives (canvas units):
  {"type": "box", "x", "y", "w", "h", "label", "tint", "size", "anchor", "weight", "dash": bool, "r": 4, "stroke": bool}
  {"type": "rrect", ...as box, "r": 14 by default}
  {"type": "circle", "x", "y", "r", "tint", "label", "size", "weight", "stroke": bool, "dash": bool}
  {"type": "polygon", "points": [(x, y), ...], "tint", "stroke": bool, "dash": bool}
  {"type": "path", "d": "...", "tint": "none", "stroke": bool, "width": STROKE, "dash": bool}
  {"type": "glyph", "name": one of GLYPHS, "x", "y" (top-left), "size": 80, "tint": "none", "width": 3.5}
  {"type": "badge", "x", "y" (centre), "n": "1", "r": 26, "tint": "b"}
  {"type": "band", "x", "y", "w", "h": 56, "text", "tint": "ink", "size", "anchor": "middle"}
  {"type": "rule", "x", "y1", "y2"}  {"type": "hrule", "y", "x1", "x2", "dash": bool}
  {"type": "arrow", "x1", "y1", "x2", "y2", "dash": bool}
  {"type": "polyline", "points": [(x, y), ...], "tint": None | "a" | "b", "on": None | "a" | "b", "width"}
  {"type": "dot", "x", "y", "r", "tint": None | "a" | "b"}
  {"type": "text", "x", "y" (baseline), "text" ("\n" for a second line), "anchor", "size", "muted": bool, "weight",
   "role": "note" (floor 24) | "label" (floor 27), "code": bool}

Usage:
    from illustration import tint_for_article, illustration, write, png
    tint = tint_for_article("how-to-write-a-prd", index=0)     # or by stable hash of the slug when index is None
    svg = illustration(items, tint=tint, uid="fig-x", title="...", desc="...")
    write(svg, "fig-x.svg"); png(svg, "fig-x.png", 1200)
"""
import colorsys
import hashlib
import math
import re
import sys
import warnings
from pathlib import Path
from xml.sax.saxutils import escape

W, H = 1200, 675
# Our lockup: the owner's mark plus the "userandproduct" wordmark, the solid one-colour lockup from the final pack
# (research/mockups/final-logo-2/svg/lockup-black.svg, or lockup-white.svg if a ground is ever dark), read from the
# file so it never drifts from the pack. The mark is one evenodd path inside a positioning group, so its head and
# band are true holes; MARK_FIGURE (the paths filled white in mark-solid.svg, on the same 1920 canvas) backs them.
_PACK = Path(__file__).resolve().parent.parent / "final-logo-2" / "svg"


def _lockup(name):
    t = (_PACK / name).read_text(encoding="utf-8")
    vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', t).group(1).split()]
    inner = re.sub(r"^.*?<svg[^>]*>", "", t, flags=re.S).rsplit("</svg>", 1)[0]
    inner = re.sub(r"<title>.*?</title>", "", inner, flags=re.S)
    fill = re.search(r'fill="(#[0-9A-Fa-f]{6})"', inner).group(1)
    return vb, inner, fill


LOCKUP = {c: _lockup(f"lockup-{c}.svg") for c in ("black", "white")}   # black #0B0B0C, white #FFFFFF
LOCKUP_VB = LOCKUP["black"][0]                                           # -4 -86 885.6 110.4
MARK_FIGURE = re.findall(r'<path fill="#FFFFFF" d="([^"]+)"', (_PACK / "mark-solid.svg").read_text(encoding="utf-8"))
# The mark alone, for the other generators that draw it on their own (build_images.py, make_demos.py): one evenodd
# path on the owner's 1920 canvas; the disc spans 88 to 1832.
MARK = re.search(r'<path[^>]*\sd="([^"]+)"', (_PACK / "mark-black.svg").read_text(encoding="utf-8")).group(1)
MARK_X0, MARK_SPAN = 88, 1744

# The eight Printables tints (main.css lines 72 to 79). Nothing else is allowed.
TINTS = {
    "blue": "#DBE8FB", "green": "#DCEFD8", "pink": "#FBE0E6", "purple": "#E8E0F7",
    "yellow": "#FFF3C4", "teal": "#D7F0EE", "peach": "#FDE3D0", "slate": "#E0E6EE",
}
# printables_tints(): the six that rotate; peach and slate are reserved (overrides, categories).
CYCLE = ["teal", "yellow", "pink", "blue", "green", "purple"]
RESERVED = ["peach", "slate"]

INK = "#1D1B16"        # Printables --ink
MUTED = "#5F5B52"      # Printables --muted
CARD = "#FDFCF8"       # Printables --card, the plain box fill
DOT_STEP, DOT_R, DOT_O = 22, 1.9, 0.13   # about a 13px tile and a 1.1px dot when shown 720px wide (Printables: 12 to 14px, 1px)
LABEL, NOTE, STROKE = 27, 24, 2.5        # type floors: 16 px and 14 px at 720 px wide; 2.5 units is the Printables border
PAD = 16                                 # label inset inside a shape, each side
MONO = "Consolas, 'Cascadia Mono', Menlo, monospace"   # only for code-like labels
# the lockup: a fifth of the figure's width (the thumbnail rule), 32 units in from the bottom and right edges, at
# 60% (the wordmark reads on the lightest tints at the article's 720px column; checked on teal and yellow)
LOCKUP_SHARE, LOCKUP_INSET, LOCKUP_O = 1 / 5, 32, 0.60


class TintError(ValueError):
    pass


class FitError(ValueError):
    pass


# ---------- colour helpers ----------
def _rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def _hex(rgb):
    return "#" + "".join(f"{max(0, min(255, round(c * 255))):02X}" for c in rgb)


def lum(h):
    v = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in _rgb(h)]
    return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2]


def contrast(a, b):
    x, y = sorted([lum(a), lum(b)], reverse=True)
    return (x + 0.05) / (y + 0.05)


def mix(a, b, t):
    ra, rb = _rgb(a), _rgb(b)
    return _hex(tuple(ra[i] + (rb[i] - ra[i]) * t for i in range(3)))


def label_on(fill):
    return max([INK, "#FFFFFF"], key=lambda col: contrast(col, fill))


# ---------- the article tint ----------
def tint_for_article(slug, index=None, override=None, reason=None):
    """The article's tint. By publish index (mirrors printables_tint_class(index): CYCLE[index % 6]), else by a stable
    hash of the slug. A writer may override with any of the eight tints, but must give a reason."""
    if override:
        if override not in TINTS:
            raise TintError(f"{override!r} is not one of the eight tints: {', '.join(TINTS)}.")
        if not reason:
            raise TintError("An override needs a reason.")
        return override
    if index is not None:
        return CYCLE[int(index) % len(CYCLE)]
    return CYCLE[int(hashlib.sha1(slug.encode("utf-8")).hexdigest(), 16) % len(CYCLE)]


def palette_for(tint):
    """Derived colours for one of the eight tints, every label checked for 4.5:1."""
    if tint not in TINTS:
        raise TintError(f"{tint!r} is not one of the eight Printables tints: {', '.join(TINTS)}.")
    bg = TINTS[tint]
    h, l, s = colorsys.rgb_to_hls(*_rgb(bg))
    muted = MUTED if contrast(MUTED, bg) >= 4.5 else mix(INK, bg, 0.2)
    sat = max(s, 0.55)
    # A: a mid cousin of the pastel (dark label); B: a deep cousin (white label). Lightness moves until labels pass.
    la, lb = 0.70, 0.36
    a = _hex(colorsys.hls_to_rgb(h, la, min(1.0, sat)))
    while contrast(label_on(a), a) < 4.5 and la < 0.9:
        la += 0.02
        a = _hex(colorsys.hls_to_rgb(h, la, min(1.0, sat)))
    b = _hex(colorsys.hls_to_rgb(h, lb, min(0.75, sat)))
    while contrast(label_on(b), b) < 4.5 and lb > 0.1:
        lb -= 0.02
        b = _hex(colorsys.hls_to_rgb(h, lb, min(0.75, sat)))
    pal = dict(name=tint, bg=bg, ink=INK, muted=muted, dots=INK, dots_o=DOT_O, box=CARD, box_s=INK, rule=INK,
               a=a, a_s=INK, b=b, b_s=INK, mark=lockup_color(bg), mark_o=LOCKUP_O)
    for key in ("ink", "muted"):
        if contrast(pal[key], bg) < 4.5:
            raise TintError(f"{key} fails 4.5:1 on {tint}.")
    for fill in (CARD, a, b):
        if contrast(label_on(fill), fill) < 4.5:
            raise TintError(f"label on {fill} fails 4.5:1 for {tint}.")
    return pal


def report():
    rows = []
    for t in TINTS:
        p = palette_for(t)
        rows.append((t, p["bg"], round(contrast(INK, p["bg"]), 1), p["muted"], round(contrast(p["muted"], p["bg"]), 1),
                     p["a"], round(contrast(label_on(p["a"]), p["a"]), 1), p["b"], round(contrast(label_on(p["b"]), p["b"]), 1),
                     round(contrast(MARK_INK_ON(p), p["bg"]), 2)))
    return rows


def lockup_color(bg):
    """The black or the white lockup, whichever contrasts more with the ground (black on all eight tints)."""
    return "white" if contrast("#FFFFFF", bg) > contrast(LOCKUP["black"][2], bg) else "black"


def MARK_INK_ON(p):  # the lockup as it renders: the one-colour lockup at LOCKUP_O over the tint
    return mix(p["bg"], LOCKUP[p["mark"]][2], LOCKUP_O)


def lockup(bg, width=W, height=H, opacity=LOCKUP_O):
    """The full lockup, bottom-right: a fifth of the width, LOCKUP_INSET in from the edges. The head and band are
    backed with the flat tint at full opacity first, so the dot grid never runs through the figure, then the pack's
    one-colour lockup at `opacity`."""
    vb, inner, _ = LOCKUP[lockup_color(bg)]
    w = width * LOCKUP_SHARE
    h = w * vb[3] / vb[2]
    x, y = width - LOCKUP_INSET - w, height - LOCKUP_INSET - h
    tr = re.search(r'<g transform="([^"]+)"', inner).group(1)
    backing = f'<g transform="{tr}">' + "".join(f'<path fill="{bg}" d="{d}"/>' for d in MARK_FIGURE) + "</g>"
    return (f'<svg x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" viewBox="{" ".join(f"{v:g}" for v in vb)}">'
            f'{backing}<g opacity="{opacity}">{inner}</g></svg>')


# ---------- type: Inter as outlines ----------
_FONTS_DIR = Path(__file__).resolve().parent.parent / "fonts" / "inter"
_WEIGHTS = {"regular": "Inter-Regular.ttf", "medium": "Inter-Medium.ttf", "semibold": "Inter-SemiBold.ttf"}
_FONT_CACHE = {}
CONTRAST_LOG = []    # (uid, original fill, used fill, text colour, ratio) for every fill the generator had to change
FIT_LOG = []         # (uid, kind, requested size, used size) for every size raised to the floor


def _font(weight):
    if weight not in _WEIGHTS:
        raise ValueError(f"weight {weight!r}: use one of {', '.join(_WEIGHTS)}")
    if weight not in _FONT_CACHE:
        here = str(Path(__file__).resolve().parent)
        if here not in sys.path:
            sys.path.insert(0, here)
        from wordmark import FontRef
        _FONT_CACHE[weight] = FontRef(_FONTS_DIR / _WEIGHTS[weight])
    return _FONT_CACHE[weight]


def text_width(s, size, weight="medium", code=False):
    """Advance width of one line in canvas units."""
    if code:
        return len(s) * size * 0.55       # Consolas advance is 0.55 em
    f = _font(weight)
    return sum(g[1] for g in f.shape(s)) * size / f.upem


def _num(n):
    s = f"{n:.2f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


def _text_paths(s, x, y, size, anchor, weight, color):
    """One line of Inter as a single <path>, baseline at y."""
    from fontTools.pens.svgPathPen import SVGPathPen
    from fontTools.pens.transformPen import TransformPen
    f = _font(weight)
    sc = size / f.upem
    w = text_width(s, size, weight)
    x0 = x - (w / 2 if anchor == "middle" else w if anchor == "end" else 0)
    pen = SVGPathPen(f.glyphs, ntos=_num)
    pos = 0.0
    for name, adv, xo, yo, _ in f.shape(s):
        f.glyphs[name].draw(TransformPen(pen, (sc, 0, 0, -sc, x0 + (pos + xo) * sc, y - yo * sc)))
        pos += adv
    d = pen.getCommands()
    return f'<path fill="{color}" d="{d}"/>' if d else ""


def _floor(size, kind, k, uid):
    floor = (LABEL if kind == "label" else NOTE) * k
    if size is None:
        return floor
    if size < floor:
        warnings.warn(f"{uid}: {kind} size {size} is below the floor {floor}; raised to {floor}.")
        FIT_LOG.append((uid, kind, size, floor))
        return floor
    return size


def text_svg(s, x, y, size, anchor="start", weight="regular", color=INK, code=False, lh=1.3):
    """Text in Inter outlines (or monospace <text> when code=True); '\n' starts a new line."""
    out = []
    for i, line in enumerate(str(s).split("\n")):
        yy = y + i * size * lh
        if code:
            out.append(f'<text x="{x}" y="{yy:.1f}" font-family="{escape(MONO)}" font-size="{size}" '
                       f'text-anchor="{anchor}" fill="{color}">{escape(line)}</text>')
        else:
            out.append(_text_paths(line, x, yy, size, anchor, weight, color))
    return "".join(out)


# ---------- contrast on fills ----------
def readable_on(fill, uid="", minimum=4.5):
    """(text colour, fill) with the text passing `minimum` on the fill: dark ink or white, whichever passes; if
    neither does, the fill moves lighter (for the dark ink) or darker (for white) until one passes. Logged."""
    best = label_on(fill)
    if contrast(best, fill) >= minimum:
        return best, fill
    h, l, s = colorsys.rgb_to_hls(*_rgb(fill))
    step = 0.01 if best == INK else -0.01
    new = fill
    while contrast(best, new) < minimum and 0.01 < l < 0.99:
        l += step
        new = _hex(colorsys.hls_to_rgb(h, l, s))
    CONTRAST_LOG.append((uid, fill, new, best, round(contrast(best, new), 2)))
    return best, new


# ---------- accents: a colour of its own where meaning needs it ----------
class AccentError(ValueError):
    pass


ACCENT_SHARE = 1 / 5     # accented elements over drawn elements; above this the figure warns (the thumbnail rule)
ACCENT_MAX = 2           # distinct accents per figure: one by default, two rarely
SHAPE_MIN = 3.0          # shapes against their ground and against each other
# name: (hue in degrees, saturation, starting lightness). The lightness moves until the pair passes.
ACCENTS = {"fire": (24, 0.95, 0.50), "warning": (2, 0.72, 0.46), "success": (128, 0.55, 0.40)}
FIRE_CORE = (46, 1.0, 0.62)   # the yellow core inside a fire accent, checked on the fire body
ACCENT_LOG = []   # (uid, element, accent, colour, against, ratio)


def _hls_hex(h, l, s):
    return _hex(colorsys.hls_to_rgb(h / 360, max(0.0, min(1.0, l)), s))


def accent_colour(name, ground, minimum=SHAPE_MIN, also=(INK,)):
    """The accent's colour, its lightness moved until it passes `minimum` on `ground` and against each colour in
    `also` (the ink outline beside it). Darker on a light ground first; if no lightness passes both, AccentError."""
    if isinstance(name, (int, float)):
        h, s, l0 = float(name) % 360, 0.75, 0.45
    elif isinstance(name, str) and name.startswith("#"):
        hh, ll, ss = colorsys.rgb_to_hls(*_rgb(name))
        h, s, l0 = hh * 360, ss, ll
    elif name in ACCENTS:
        h, s, l0 = ACCENTS[name]
    else:
        raise AccentError(f"accent {name!r}: use one of {', '.join(ACCENTS)}, a #hex or a hue in degrees.")
    ok = lambda col: contrast(col, ground) >= minimum and all(contrast(col, a) >= minimum for a in also)
    darker_first = lum(ground) > 0.18
    for step in ((-0.005, 0.005) if darker_first else (0.005, -0.005)):
        l = l0
        while 0.0 < l < 1.0:
            col = _hls_hex(h, l, s)
            if ok(col):
                return col
            l += step
    raise AccentError(f"accent {name!r}: no lightness passes {minimum}:1 on {ground} and against {also}.")


def fire_core(body):
    """The yellow core of a fire accent: lightened until it passes 3:1 on the orange body."""
    h, s, l = FIRE_CORE
    while l < 0.98:
        col = _hls_hex(h, l, s)
        if contrast(col, body) >= SHAPE_MIN:
            return col
        l += 0.01
    raise AccentError(f"fire core: no yellow passes {SHAPE_MIN}:1 on {body}.")


# ---------- glyphs: small line drawings on a 100-unit square ----------
GLYPHS = {
    "person": "M50 12a14 14 0 1 1 0 28a14 14 0 1 1 0-28Z M22 88c0-18 12-30 28-30s28 12 28 30",
    "doc": "M24 8h38l16 16v68H24Z M62 8v16h16 M36 44h28 M36 58h28 M36 72h18",
    "check": "M18 52l20 20 44-44",
    "cross": "M24 24l52 52M76 24L24 76",
    "clock": "M50 10a40 40 0 1 1 0 80a40 40 0 1 1 0-80Z M50 26v24l16 10",
    "bubble": "M14 20h72v46H44l-18 16V66H14Z",
    "flag": "M26 90V10 M26 14h48l-10 16 10 16H26",
    "bulb": "M50 10a28 28 0 0 0-16 51v13h32V61A28 28 0 0 0 50 10Z M38 86h24",
    "pan": "M6 44h62v8a18 18 0 0 1-18 18H24A18 18 0 0 1 6 52Z M68 48h26",
    "flame": "M50 8c10 18 26 26 26 48a26 26 0 0 1-52 0c0-12 8-20 12-28 4 10 8 14 14 14-4-12 0-24 0-34Z",
    "magnifier": "M42 14a28 28 0 1 1 0 56a28 28 0 1 1 0-56Z M62 62l26 26",
    "question": "M34 34a16 16 0 1 1 22 15c-4 2-6 5-6 9v6 M50 78v4",
}
# inner shapes drawn in an accent's second colour (the yellow core of a fire accent), no stroke
GLYPH_CORES = {"flame": "M50 40c6 10 14 15 14 27a14 14 0 0 1-28 0c0-7 4-11 6-15 3 5 5 7 8 7-2-7 0-13 0-19Z"}
LINE_GLYPHS = {"check", "cross", "question"}
ACCENT_TYPES = {"box", "rrect", "circle", "polygon", "path", "glyph", "badge", "dot", "polyline"}   # glyphs drawn as lines: an accent colours the stroke


# ---------- drawing ----------
def _legacy(t):
    return {"blue": "a", "yellow": "a", "red": "b"}.get(t, t)


def illustration(items, tint="teal", uid="il", desc=None, title=None, width=W, height=H, thumb=False):
    c = palette_for(tint)
    k = 2 if thumb else 1
    lab = f' aria-labelledby="{uid}-t{f" {uid}-d" if desc else ""}"' if title else ""
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img"{lab}>']
    if title:
        o.append(f'<title id="{uid}-t">{escape(title)}</title>')
    if desc:
        o.append(f'<desc id="{uid}-d">{escape(desc)}</desc>')
    o.append(f'<defs><pattern id="{uid}-p" width="{DOT_STEP}" height="{DOT_STEP}" patternUnits="userSpaceOnUse">'
             f'<circle cx="{DOT_STEP / 2}" cy="{DOT_STEP / 2}" r="{DOT_R}" fill="{c["dots"]}"/></pattern></defs>')
    o.append(f'<rect width="{width}" height="{height}" fill="{c["bg"]}"/>')
    o.append(f'<rect width="{width}" height="{height}" fill="url(#{uid}-p)" opacity="{c["dots_o"]}"/>')
    lw = width * LOCKUP_SHARE
    zone = (width - LOCKUP_INSET - lw - 16, height - LOCKUP_INSET - lw * LOCKUP_VB[3] / LOCKUP_VB[2] - 16)

    def fill_of(it, default=None):
        t = _legacy(it.get("tint", default))
        return {None: c["box"], "card": c["box"], "a": c["a"], "b": c["b"], "ink": INK, "bg": c["bg"], "none": "none"}[t]

    def stroke_attr(it, default=True):
        if not it.get("stroke", default):
            return ""
        dash = ' stroke-dasharray="10 8"' if it.get("dash") else ""
        return f' stroke="{INK}" stroke-width="{it.get("width", STROKE)}"{dash}'

    def zone_check(x0, y0, x1, y1, what):
        if x1 > zone[0] and y1 > zone[1]:
            warnings.warn(f"{uid}: {what} reaches into the lockup corner (x>{zone[0]:.0f}, y>{zone[1]:.0f}).")

    def label_in(it, x, y, w, h, fill, default_anchor="start"):
        """A label centred vertically in a shape, checked for fit and contrast. Returns (svg, fill used)."""
        if not it.get("label"):
            return "", fill
        size = _floor(it.get("size"), "label", k, uid)
        weight = it.get("weight", "medium")
        col, fill2 = readable_on(fill if fill != "none" else c["bg"], uid)
        if fill != "none":
            fill = fill2
        lines = str(it["label"]).split("\n")
        tw = max(text_width(l, size, weight, it.get("code")) for l in lines)
        if tw > w - 2 * PAD + 0.5:
            raise FitError(f"{uid}: label {it['label']!r} at {size} units is {tw:.0f} wide; the shape allows "
                           f"{w - 2 * PAD:.0f}. Enlarge the shape or shorten the label.")
        anchor = it.get("anchor", default_anchor)
        tx = x + PAD if anchor == "start" else x + w / 2 if anchor == "middle" else x + w - PAD
        lh = 1.25
        ty = y + h / 2 - (len(lines) - 1) * size * lh / 2 + size * 0.36
        on = fill if fill != "none" else c["bg"]
        return (f'<g data-on="{on}">' + text_svg(it["label"], tx, round(ty, 1), size, anchor, weight, col, it.get("code"), lh=lh)
                + "</g>"), fill

    used = {}        # accent name -> colour, for the pairwise check
    n_acc = 0

    def accent_of(it, outline=True, element=""):
        """The accent colour for an element, or None. Checked for SHAPE_MIN on its ground and the ink outline."""
        nonlocal n_acc
        name = it.get("accent")
        if name is None:
            return None
        if it["type"] not in ACCENT_TYPES:
            raise AccentError(f"{uid}: no accent on {it['type']!r} (accents go on shapes, icons and badges only).")
        ground = it.get("accent_on", c["bg"])
        col = accent_colour(name, ground, also=(INK,) if outline else ())
        key = str(name)
        used[key] = col
        n_acc += 1
        what = element or it["type"]
        ACCENT_LOG.append((uid, what, key, col, ground, round(contrast(col, ground), 2)))
        if outline:
            ACCENT_LOG.append((uid, what, key, col, INK, round(contrast(col, INK), 2)))
        return col

    for it in items:
        t = it["type"]
        if t in ("box", "rrect"):
            fill = accent_of(it, it.get("stroke", True), f"{t} {it.get('label', '')!r}") or fill_of(it)
            r = it.get("r", 4 if t == "box" else 14)
            lbl, fill = label_in(it, it["x"], it["y"], it["w"], it["h"], fill)
            o.append(f'<rect x="{it["x"]}" y="{it["y"]}" width="{it["w"]}" height="{it["h"]}" rx="{r}" fill="{fill}"'
                     f'{stroke_attr(it)}/>' + lbl)
            zone_check(it["x"], it["y"], it["x"] + it["w"], it["y"] + it["h"], f"{t} {it.get('label', '')!r}")
        elif t == "circle":
            fill = accent_of(it, it.get("stroke", True), f"circle {it.get('label', '')!r}") or fill_of(it)
            r = it["r"]
            lbl, fill = label_in(it, it["x"] - r, it["y"] - r, 2 * r, 2 * r, fill, "middle")
            o.append(f'<circle cx="{it["x"]}" cy="{it["y"]}" r="{r}" fill="{fill}"{stroke_attr(it)}/>' + lbl)
        elif t == "polygon":
            pts = " ".join(f"{x},{y}" for x, y in it["points"])
            fill = accent_of(it, it.get("stroke", True)) or fill_of(it)
            o.append(f'<polygon points="{pts}" fill="{fill}" stroke-linejoin="round"{stroke_attr(it)}/>')
        elif t == "path":
            fill, sa = fill_of(it, "none"), stroke_attr(it)
            part = it.get("accent_part", "stroke" if fill == "none" else "fill")
            col = accent_of(it, part == "fill" and bool(sa))
            if col and part == "fill":
                fill = col
            elif col:
                sa = sa.replace(f'stroke="{INK}"', f'stroke="{col}"')
            o.append(f'<path d="{it["d"]}" fill="{fill}" stroke-linejoin="round" stroke-linecap="round"{sa}/>')
        elif t == "glyph":
            size = it.get("size", 80)
            sc = size / 100
            sw = it.get("width", 3.5) / sc
            fill, stroke, core = fill_of(it, "none"), INK, ""
            part = it.get("accent_part", "stroke" if it["name"] in LINE_GLYPHS else "fill")
            col = accent_of(it, part == "fill", f"glyph {it['name']}")
            if col and part == "fill":
                fill = col
                if it.get("accent") == "fire" and it["name"] in GLYPH_CORES:
                    cc = fire_core(col)
                    ACCENT_LOG.append((uid, f"glyph {it['name']} core", "fire core", cc, col, round(contrast(cc, col), 2)))
                    core = f'<path d="{GLYPH_CORES[it["name"]]}" fill="{cc}"/>'
            elif col:
                stroke = col
            o.append(f'<g transform="translate({it["x"]} {it["y"]}) scale({sc:g})"><path d="{GLYPHS[it["name"]]}" '
                     f'fill="{fill}" stroke="{stroke}" stroke-width="{sw:.2f}" stroke-linejoin="round" '
                     f'stroke-linecap="round"/>{core}</g>')
        elif t == "badge":
            r = it.get("r", 26) * k
            size = _floor(it.get("size"), "label", k, uid)
            col, fill = readable_on(accent_of(it, True, f"badge {it['n']}") or fill_of(it, "b"), uid)
            if text_width(str(it["n"]), size, "semibold") > 2 * r - 8:
                raise FitError(f"{uid}: badge {it['n']!r} does not fit radius {r}.")
            o.append(f'<circle cx="{it["x"]}" cy="{it["y"]}" r="{r}" fill="{fill}" stroke="{INK}" stroke-width="{STROKE}"/>'
                     + f'<g data-on="{fill}">' + text_svg(str(it["n"]), it["x"], round(it["y"] + size * 0.36, 1), size, "middle",
                                                         "semibold", col) + "</g>")
        elif t == "band":
            h = it.get("h", 56 * k)
            lbl, fill = label_in({"label": it["text"], "size": it.get("size"), "weight": it.get("weight", "semibold"),
                                  "anchor": it.get("anchor", "middle")}, it["x"], it["y"], it["w"], h,
                                 fill_of(it, "ink"), "middle")
            o.append(f'<rect x="{it["x"]}" y="{it["y"]}" width="{it["w"]}" height="{h}" rx="{h / 2:g}" fill="{fill}"/>' + lbl)
            zone_check(it["x"], it["y"], it["x"] + it["w"], it["y"] + h, f"band {it['text']!r}")
        elif t == "rule":
            o.append(f'<path d="M{it["x"]} {it["y1"]}V{it["y2"]}" stroke="{c["rule"]}" stroke-width="{STROKE}"/>')
        elif t == "hrule":
            dash = ' stroke-dasharray="10 8"' if it.get("dash") else ""
            o.append(f'<path d="M{it["x1"]} {it["y"]}H{it["x2"]}" stroke="{c["rule"]}" stroke-width="{STROKE}"{dash}/>')
        elif t == "arrow":
            x1, y1, x2, y2 = it["x1"], it["y1"], it["x2"], it["y2"]
            a = math.atan2(y2 - y1, x2 - x1)
            hl, hw = 14, 7
            bx, by = x2 - hl * math.cos(a), y2 - hl * math.sin(a)
            dash = ' stroke-dasharray="10 8"' if it.get("dash") else ""
            o.append(f'<path d="M{x1} {y1}L{bx:.1f} {by:.1f}" stroke="{c["rule"]}" stroke-width="{STROKE}"{dash}/>'
                     f'<path d="M{x2} {y2}L{bx + hw * math.sin(a):.1f} {by - hw * math.cos(a):.1f}'
                     f'L{bx - hw * math.sin(a):.1f} {by + hw * math.cos(a):.1f}Z" fill="{c["rule"]}"/>')
        elif t == "polyline":
            col = c["b"] if _legacy(it.get("tint")) else c["rule"]
            if it.get("on"):
                col = label_on(c[it["on"]])
            col = accent_of(it, False) or col
            pts = " ".join(f"{x},{y}" for x, y in it["points"])
            o.append(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="{it.get("width", STROKE + 1.5)}" '
                     f'stroke-linejoin="round" stroke-linecap="round"/>')
        elif t == "dot":
            fill = accent_of(it, True) or (c["b"] if _legacy(it.get("tint")) else c["box"])
            o.append(f'<circle cx="{it["x"]}" cy="{it["y"]}" r="{it.get("r", 7)}" fill="{fill}" stroke="{INK}" stroke-width="2"/>')
        elif t == "text":
            if "accent" in it:
                accent_of(it)   # raises: no accent on text
            muted = it.get("muted", True)
            col = c["muted"] if muted else c["ink"]
            if contrast(col, c["bg"]) < 4.5:
                raise TintError(f"{uid}: text colour {col} fails 4.5:1 on {c['bg']}.")
            role = it.get("role", "note")
            size = _floor(it.get("size"), role, k, uid)
            weight = it.get("weight", "regular" if (role == "note" and muted) else "medium")
            an = it.get("anchor", "start")
            o.append(f'<g data-on="{c["bg"]}">' + text_svg(it["text"], it["x"], it["y"], size, an, weight, col, it.get("code")) + "</g>")
            tw = max(text_width(l, size, weight, it.get("code")) for l in str(it["text"]).split("\n"))
            x0 = it["x"] - (tw / 2 if an == "middle" else tw if an == "end" else 0)
            if x0 < 24 or x0 + tw > width - 24:
                warnings.warn(f"{uid}: text {it['text']!r} runs off the canvas.")
            zone_check(x0, it["y"] - size, x0 + tw, it["y"], f"text {it['text']!r}")
        else:
            raise ValueError(f"{uid}: unknown primitive {t!r}")
        if "accent" in it and t not in ACCENT_TYPES:
            accent_of(it)       # raises for rules, arrows, bands and anything else that is not a shape
    # the scheme rule: one accent, two rarely, on at most about a fifth of the drawn elements
    if len(used) > ACCENT_MAX:
        raise AccentError(f"{uid}: {len(used)} accents ({', '.join(used)}); two at most, one by default.")
    names = list(used)
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            a, b = used[names[i]], used[names[j]]
            ACCENT_LOG.append((uid, f"{names[i]} against {names[j]}", "pair", a, b, round(contrast(a, b), 2)))
            if contrast(a, b) < SHAPE_MIN:
                warnings.warn(f"{uid}: accents {names[i]} {a} and {names[j]} {b} are {contrast(a, b):.2f}:1 against "
                              f"each other, under {SHAPE_MIN}:1; drop one (fewer colours).")
    if items and n_acc / len(items) > ACCENT_SHARE:
        warnings.warn(f"{uid}: accents on {n_acc} of {len(items)} drawn elements, above a fifth; use fewer.")
    # the full lockup, bottom-right, quiet (see lockup())
    o.append(lockup(c["bg"], width, height, c["mark_o"]))
    o.append("</svg>")
    return "".join(o)


def check_contrast(svg):
    """Every text colour in a generated SVG paired with the colour it sits on: [(ground, text, ratio)]. The generator
    wraps every text run in <g data-on="ground">, so this reads the file itself, not the spec."""
    out = []
    for on, body in re.findall(r'<g data-on="(#[0-9A-Fa-f]{6})">(.*?)</g>', svg, flags=re.S):
        for col in re.findall(r'<(?:path|text)[^>]*?fill="(#[0-9A-Fa-f]{6})"', body):
            out.append((on, col, round(contrast(on, col), 2)))
    return out


def write(svg, path):
    Path(path).write_text('<?xml version="1.0" encoding="UTF-8"?>\n' + svg, encoding="utf-8")


def png(svg, path, width):
    import resvg_py
    data = resvg_py.svg_to_bytes(svg_string=svg, width=int(width), monospace_family="Consolas")
    Path(path).write_bytes(bytes(data))


if __name__ == "__main__":
    for row in report():
        print(row)
    print([tint_for_article("x", index=i) for i in range(8)])
