"""Set a word in an open-licence font and write it as a clean SVG made of paths.

The text is shaped with HarfBuzz (uharfbuzz) when it is installed, so the font's own
kerning and ligatures apply; otherwise glyphs are placed by advance width only (no
kerning). Outlines come from fontTools. The result has no <text> element, no width or
height, a viewBox fitted to the ink bounds plus a small margin, and fill="currentColor".

Usage:
    python wordmark.py --font Geist-Bold.ttf --text "userandproduct" --out wm.svg
    python wordmark.py --font Geist-Bold.ttf --split "user|and|product" --out wm.svg
    python wordmark.py --font Geist-Bold.ttf --split "user|and|product" \\
        --highlight and --alt-font Geist-Regular.ttf --accent "#B3141C" --out wm.svg

Options:
    --size N          font size in output units (default 100; one em = N units)
    --tracking U      extra space after each glyph, in thousandths of an em (scaled for
                      2048- or 2000-unit fonts, so the number means the same everywhere)
    --split "a|b|c"   write one <path> per part, each with an id and a class, so a
                      page or a build can colour one part differently
    --highlight a,b   parts that use --alt-font and/or --accent
    --alt-font FILE   font for the highlighted parts (for example a lighter weight)
    --fill COLOR      fill for the whole mark (default currentColor)
    --accent COLOR    fill for the highlighted parts
    --id-prefix P     prefix for part ids (default "wm-"), to keep ids unique on a page
    --margin M        margin around the ink, as a fraction of --size (default 0.04)
    --merge           remove overlapping contours with skia-pathops (if installed)
    --weight-note     add a comment naming the font, weight class and version

Prints the ink bounds and the viewBox in output units.
"""

import argparse
import re
import sys
from pathlib import Path

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

try:
    import uharfbuzz as hb
except ImportError:  # shaping falls back to advance widths
    hb = None

try:
    import pathops
except ImportError:
    pathops = None


def fmt(n):
    """Format a coordinate with at most two decimals and no trailing zeros."""
    s = f"{n:.2f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


def esc(s):
    """Escape a string for an XML attribute or text node."""
    return s.replace("&", "&amp;").replace("<", "&lt;").replace('"', "&quot;")


def slug(text):
    """Make a safe id fragment from a part of the text."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "part"


class FontRef:
    """A loaded font: fontTools objects plus an optional HarfBuzz font."""

    def __init__(self, path):
        self.path = str(path)
        self.tt = TTFont(self.path)
        self.glyphs = self.tt.getGlyphSet()
        self.order = self.tt.getGlyphOrder()
        self.cmap = self.tt.getBestCmap()
        self.upem = self.tt["head"].unitsPerEm
        self.hb = None
        if hb is not None:
            face = hb.Face(hb.Blob.from_file_path(self.path))
            self.hb = hb.Font(face)  # scale defaults to units per em

    def describe(self):
        """Return 'Family Style, weight class N, Version x' for a note."""
        name = self.tt["name"]
        weight = self.tt["OS/2"].usWeightClass if "OS/2" in self.tt else "?"
        return f"{name.getDebugName(4)}, weight class {weight}, {name.getDebugName(5)}"

    def shape(self, text):
        """Return a list of (glyph_name, x_advance, x_offset, y_offset, cluster)."""
        if self.hb is not None:
            buf = hb.Buffer()
            buf.add_str(text)
            buf.guess_segment_properties()
            hb.shape(self.hb, buf, {"kern": True, "liga": True})
            return [
                (self.order[i.codepoint], p.x_advance, p.x_offset, p.y_offset, i.cluster)
                for i, p in zip(buf.glyph_infos, buf.glyph_positions)
            ]
        out = []
        for idx, ch in enumerate(text):
            name = self.cmap.get(ord(ch), ".notdef")
            out.append((name, self.glyphs[name].width, 0, 0, idx))
        return out


def layout(parts, fonts, size, tracking):
    """Place every glyph and return, per part, a list of (font, glyph, matrix).

    Consecutive parts that share a font are shaped as one run, so kerning across
    the part boundary is kept. Font units are y-up and SVG is y-down, so each
    glyph is flipped and moved to the pen position.
    """
    placed = [[] for _ in parts]
    x = 0.0  # pen position in output units
    i = 0
    while i < len(parts):
        j = i
        while j + 1 < len(parts) and fonts[j + 1] is fonts[i]:
            j += 1
        font = fonts[i]
        run = "".join(parts[i:j + 1])
        starts, pos = [], 0
        for k in range(i, j + 1):
            starts.append(pos)
            pos += len(parts[k])
        scale = size / font.upem
        track = tracking * font.upem / 1000.0
        for name, adv, xoff, yoff, cluster in font.shape(run):
            part = i + max(n for n, s in enumerate(starts) if s <= cluster)
            matrix = (scale, 0, 0, -scale, x + xoff * scale, -yoff * scale)
            placed[part].append((font, name, matrix))
            x += (adv + track) * scale
        i = j + 1
    return placed


def part_path(items, merge):
    """Draw the glyphs of one part; return (SVG path data, ink bounds)."""
    bounds = BoundsPen(None)
    pen = SVGPathPen(None, ntos=fmt)
    if merge and pathops is not None:
        merged = pathops.Path()
        for font, name, matrix in items:
            font.glyphs[name].draw(TransformPen(merged.getPen(), matrix))
        merged.simplify()
        merged.draw(pen)
        merged.draw(bounds)
    else:
        for font, name, matrix in items:
            font.glyphs[name].draw(TransformPen(pen, matrix))
            font.glyphs[name].draw(TransformPen(bounds, matrix))
    return pen.getCommands(), bounds.bounds


def union_bounds(boxes):
    """Return the box that holds every non-empty box in the list."""
    boxes = [b for b in boxes if b]
    return (min(b[0] for b in boxes), min(b[1] for b in boxes),
            max(b[2] for b in boxes), max(b[3] for b in boxes))


def build(args):
    """Build the SVG and return (svg text, ink bounds, viewBox tuple)."""
    parts = args.split.split("|") if args.split else [args.text]
    text = "".join(parts)
    if args.text and args.split and args.text != text:
        sys.exit(f"--text '{args.text}' does not match --split '{args.split}'")
    highlight = {h.strip() for h in (args.highlight or "").split(",") if h.strip()}
    main_font = FontRef(args.font)
    alt_font = FontRef(args.alt_font) if args.alt_font else main_font
    fonts = [alt_font if p in highlight else main_font for p in parts]

    placed = layout(parts, fonts, args.size, args.tracking)
    paths = [part_path(items, args.merge) for items in placed]
    x0, y0, x1, y1 = union_bounds([b for _, b in paths])
    m = args.margin * args.size
    vb = (x0 - m, y0 - m, (x1 - x0) + 2 * m, (y1 - y0) + 2 * m)

    lines = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{" ".join(fmt(v) for v in vb)}" '
             f'fill="{esc(args.fill)}" role="img" aria-label="{esc(text)}">']
    if args.weight_note:
        note = main_font.describe()
        if alt_font is not main_font:
            note += f"; highlight: {alt_font.describe()}"
        shaping = "harfbuzz" if hb else "advance widths"
        lines.append(f"<!-- {esc(note)}; shaping: {shaping} -->")
    lines.append(f"<title>{esc(text)}</title>")
    if len(parts) == 1:
        lines.append(f'<path d="{paths[0][0]}"/>')
    else:
        for p, (d, _) in zip(parts, paths):
            fill = f' fill="{esc(args.accent)}"' if (p in highlight and args.accent) else ""
            lines.append(f'<path id="{esc(args.id_prefix)}{slug(p)}" class="wm-{slug(p)}"{fill} d="{d}"/>')
    lines.append("</svg>")
    return "\n".join(lines) + "\n", (x0, y0, x1, y1), vb


def main(argv=None):
    """Command-line entry point."""
    ap = argparse.ArgumentParser(description="Set a word in a font and write it as SVG paths.")
    ap.add_argument("--font", required=True, help="TTF or OTF file")
    ap.add_argument("--text", default="", help="text to set (or use --split)")
    ap.add_argument("--out", required=True, help="SVG file to write")
    ap.add_argument("--size", type=float, default=100, help="font size in output units")
    ap.add_argument("--tracking", type=float, default=0, help="extra spacing, 1/1000 em")
    ap.add_argument("--split", default="", help='parts separated by |, e.g. "user|and|product"')
    ap.add_argument("--highlight", default="", help="comma list of parts to highlight")
    ap.add_argument("--alt-font", default="", help="font for highlighted parts")
    ap.add_argument("--fill", default="currentColor", help="fill for the mark")
    ap.add_argument("--accent", default="", help="fill for highlighted parts")
    ap.add_argument("--id-prefix", default="wm-", help="prefix for part ids")
    ap.add_argument("--margin", type=float, default=0.04, help="margin as a fraction of size")
    ap.add_argument("--merge", action="store_true", help="remove overlaps (skia-pathops)")
    ap.add_argument("--weight-note", action="store_true", help="add a font and weight comment")
    args = ap.parse_args(argv)
    if not args.text and not args.split:
        ap.error("give --text or --split")
    if args.merge and pathops is None:
        print("note: skia-pathops not installed, --merge ignored", file=sys.stderr)
    svg, ink, vb = build(args)
    Path(args.out).write_text(svg, encoding="utf-8")
    print(f"ink bounds: x0={ink[0]:.2f} y0={ink[1]:.2f} x1={ink[2]:.2f} y1={ink[3]:.2f} "
          f"(w={ink[2] - ink[0]:.2f} h={ink[3] - ink[1]:.2f})")
    print(f"viewBox: {' '.join(fmt(v) for v in vb)}; "
          f"shaping: {'harfbuzz' if hb else 'advance widths'}; wrote {args.out}")


if __name__ == "__main__":
    main()
