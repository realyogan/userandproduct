"""Render an SVG to PNG files at one or more sizes with resvg (resvg-py).

Each size is the output width in pixels; the height follows the SVG's aspect ratio,
unless --square is given, in which case the drawing is fitted and centred inside a
size x size canvas. currentColor in the SVG is replaced by --color first, because a
standalone render has no parent text colour to inherit.

Usage:
    python render.py logo.svg --sizes 16,32,180,512
    python render.py logo.svg --sizes 1200 --background "#ffffff" --color "#111111"
    python render.py mark.svg --sizes 16,32 --square --out-dir previews

Writes <out-dir>/<svg stem>-<size>.png (out-dir defaults to the SVG's folder).
"""

import argparse
import io
import re
from pathlib import Path

import resvg_py

try:
    from PIL import Image
except ImportError:  # only needed for --square
    Image = None


def viewbox_ratio(svg):
    """Return width / height from the root viewBox (1.0 if there is none)."""
    m = re.search(r'viewBox="\s*([-\d.e]+)[\s,]+([-\d.e]+)[\s,]+([-\d.e]+)[\s,]+([-\d.e]+)', svg)
    if not m:
        return 1.0
    w, h = float(m.group(3)), float(m.group(4))
    return w / h if h else 1.0


def render_png(svg, width, height=None, background=None):
    """Render SVG text to PNG bytes at the given pixel size."""
    if height is None:
        height = max(1, round(width / viewbox_ratio(svg)))
    data = resvg_py.svg_to_bytes(svg_string=svg, width=int(width), height=int(height),
                                 background=background)
    return bytes(data)


def render_fitted(svg, size, background=None, pad=0):
    """Render into a size x size canvas, fitted inside `pad` pixels and centred.

    Returns a Pillow RGBA image. Needs Pillow.
    """
    if Image is None:
        raise RuntimeError("Pillow is needed for fitted (square) renders")
    ratio = viewbox_ratio(svg)
    box = size - 2 * pad
    w, h = (box, max(1, round(box / ratio))) if ratio >= 1 else (max(1, round(box * ratio)), box)
    art = Image.open(io.BytesIO(render_png(svg, w, h))).convert("RGBA")
    canvas = Image.new("RGBA", (size, size), background or (0, 0, 0, 0))
    canvas.alpha_composite(art, ((size - w) // 2, (size - h) // 2))
    return canvas


def set_color(svg, color):
    """Replace currentColor with a fixed colour."""
    return svg.replace("currentColor", color) if color else svg


def main(argv=None):
    """Command-line entry point."""
    ap = argparse.ArgumentParser(description="Render an SVG to PNG with resvg.")
    ap.add_argument("svg", help="SVG file")
    ap.add_argument("--sizes", default="16,32,180,512", help="comma list of widths in px")
    ap.add_argument("--out-dir", default="", help="folder for the PNGs")
    ap.add_argument("--color", default="#111111", help="colour used for currentColor")
    ap.add_argument("--background", default=None, help="canvas colour (default transparent)")
    ap.add_argument("--square", action="store_true", help="fit into a square canvas")
    ap.add_argument("--pad", type=int, default=0, help="padding in px for --square")
    args = ap.parse_args(argv)

    src = Path(args.svg)
    svg = set_color(src.read_text(encoding="utf-8"), args.color)
    out_dir = Path(args.out_dir) if args.out_dir else src.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    for size in [int(s) for s in args.sizes.split(",") if s.strip()]:
        out = out_dir / f"{src.stem}-{size}.png"
        if args.square:
            render_fitted(svg, size, args.background, args.pad).save(out)
        else:
            out.write_bytes(render_png(svg, size, background=args.background))
        print(f"wrote {out}")


if __name__ == "__main__":
    main()
