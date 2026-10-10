"""Explainer illustrations on the Printables tints: a pastel background with a dark dot grid, the diagram on top in
dark ink, and our mark small and quiet in the bottom-right corner. No card, outline, border or title inside the image.
The same PNG is used on the light and the dark page. Rules: research/mockups/illustration-rules.md.
Source of the palette: research/mockups/references/printables-tints.md.

One colour per article: every explainer in an article uses the article's tint, from tint_for_article().

Canvas: 1200 x 675 (16:9). Export 1200 x 675 for figures and 600 x 338 for thumbnails.

Primitives (canvas units):
  {"type": "box", "x", "y", "w", "h", "label", "tint": None | "a" | "b", "size", "anchor"}
  {"type": "rule", "x", "y1", "y2"}  {"type": "hrule", "y", "x1", "x2", "dash": bool}
  {"type": "arrow", "x1", "y1", "x2", "y2"}
  {"type": "polyline", "points": [(x, y), ...], "tint": None | "a" | "b", "on": None | "a" | "b"}
  {"type": "dot", "x", "y", "r", "tint": None | "a" | "b"}
  {"type": "text", "x", "y", "text", "anchor", "size", "muted": bool}

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
from pathlib import Path
from xml.sax.saxutils import escape

W, H = 1200, 675
# Our mark: the owner's disc from the final pack (research/mockups/final-logo-2/svg/mark-black.svg), read from the
# file so it never drifts from the pack. One evenodd path on the owner's 1920 canvas; the disc spans 88 to 1832.
# Its figure (head and band) are the paths filled white in mark-solid.svg.
_PACK = Path(__file__).resolve().parent.parent / "final-logo-2" / "svg"
_mb = (_PACK / "mark-black.svg").read_text(encoding="utf-8")
MARK = re.search(r'<path[^>]*\sd="([^"]+)"', _mb).group(1)
MARK_BLACK = re.search(r'fill="(#[0-9A-Fa-f]{6})"', _mb).group(1)          # #0B0B0C
MARK_WHITE = re.search(r'fill="(#[0-9A-Fa-f]{6})"', (_PACK / "mark-white.svg").read_text(encoding="utf-8")).group(1)
MARK_FIGURE = re.findall(r'<path fill="#FFFFFF" d="([^"]+)"', (_PACK / "mark-solid.svg").read_text(encoding="utf-8"))
MARK_X0, MARK_SPAN = 88, 1744                                              # the disc's edge and width, pack units

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
MONO = "Consolas, 'Cascadia Mono', Menlo, monospace"
DOT_STEP, DOT_R, DOT_O = 22, 1.9, 0.13   # about a 13px tile and a 1.1px dot when shown 720px wide (Printables: 12 to 14px, 1px)
LABEL, NOTE, STROKE = 19, 17, 2.5        # 2.5 units is about 1.5px at 720px wide, the Printables border
MARK_SIZE, MARK_INSET, MARK_O = 34, 32, 0.35


class TintError(ValueError):
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
               a=a, a_s=INK, b=b, b_s=INK, mark=MARK_BLACK, mark_o=MARK_O)
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


def MARK_INK_ON(p):  # the mark as it renders: the black mark at 35% over the tint
    return mix(p["bg"], p["mark"], MARK_O)


# ---------- drawing ----------
def illustration(items, tint="teal", uid="il", desc=None, title=None, width=W, height=H):
    c = palette_for(tint)
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

    def tint_of(it):
        t = it.get("tint")
        return {"blue": "a", "red": "b", "yellow": "a"}.get(t, t)

    for it in items:
        t = it["type"]
        if t == "box":
            tn = tint_of(it)
            fill = c[tn] if tn else c["box"]
            o.append(f'<rect x="{it["x"]}" y="{it["y"]}" width="{it["w"]}" height="{it["h"]}" rx="4" fill="{fill}" '
                     f'stroke="{c["box_s"]}" stroke-width="{STROKE}"/>')
            if it.get("label"):
                size = it.get("size", LABEL)
                anchor = it.get("anchor", "start")
                x = it["x"] + 16 if anchor == "start" else it["x"] + it["w"] / 2
                o.append(f'<text x="{x}" y="{it["y"] + it["h"] / 2 + size * 0.36:.1f}" font-family="{MONO}" font-size="{size}" '
                         f'text-anchor="{anchor}" fill="{label_on(fill)}">{escape(it["label"])}</text>')
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
            o.append(f'<path d="M{x1} {y1}L{bx:.1f} {by:.1f}" stroke="{c["rule"]}" stroke-width="{STROKE}"/>'
                     f'<path d="M{x2} {y2}L{bx + hw * math.sin(a):.1f} {by - hw * math.cos(a):.1f}'
                     f'L{bx - hw * math.sin(a):.1f} {by + hw * math.cos(a):.1f}Z" fill="{c["rule"]}"/>')
        elif t == "polyline":
            tn = tint_of(it)
            col = c["b"] if tn else c["rule"]
            if it.get("on"):
                col = label_on(c[it["on"]])
            pts = " ".join(f"{x},{y}" for x, y in it["points"])
            o.append(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="{STROKE + 1.5}" stroke-linejoin="round" stroke-linecap="round"/>')
        elif t == "dot":
            tn = tint_of(it)
            o.append(f'<circle cx="{it["x"]}" cy="{it["y"]}" r="{it.get("r", 7)}" fill="{c["b"] if tn else c["box"]}" '
                     f'stroke="{INK}" stroke-width="2"/>')
        elif t == "text":
            col = c["muted"] if it.get("muted", True) else c["ink"]
            o.append(f'<text x="{it["x"]}" y="{it["y"]}" font-family="{MONO}" font-size="{it.get("size", NOTE)}" '
                     f'text-anchor="{it.get("anchor", "start")}" fill="{col}">{escape(it["text"])}</text>')
    # the mark, bottom-right: the head and band backed with the flat tint first, so the dot grid never runs through
    # the figure, then the pack's one-colour mark at 35%
    s = MARK_SIZE / MARK_SPAN
    tr = (f'translate({width - MARK_INSET - MARK_SIZE} {height - MARK_INSET - MARK_SIZE}) scale({s:.6f}) '
          f'translate({-MARK_X0} {-MARK_X0})')
    o.append(f'<g transform="{tr}">' + "".join(f'<path fill="{c["bg"]}" d="{d}"/>' for d in MARK_FIGURE) + '</g>')
    o.append(f'<g transform="{tr}" opacity="{c["mark_o"]}"><path fill="{c["mark"]}" fill-rule="evenodd" d="{MARK}"/></g>')
    o.append("</svg>")
    return "".join(o)


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
