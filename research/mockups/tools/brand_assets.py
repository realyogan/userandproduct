"""Make the site's icon and social files from one master SVG mark.

Writes, into the output folder:
    favicon.svg                vector favicon; currentColor becomes --color, with a
                               prefers-color-scheme rule that switches to --dark-color
    favicon-16.png, -32.png    the mark on a --bg tile (reads in light and dark tabs)
    favicon.ico                16, 32 and 48 px in one file (needs Pillow)
    apple-touch-icon-180.png   solid --bg, about 20 px padding, no transparency
    icon-512.png               for the WordPress Site Icon and the web manifest
    og-1200x630.png            placeholder social image: mark centred on --og-bg
    avatar-400.png             LinkedIn and profile avatar, mark centred with margin

Usage:
    python brand_assets.py mark.svg out/ --bg "#111111" --color "#ffffff"
    python brand_assets.py mark.svg out/ --bg "#ffffff" --color "#111111" --og-bg "#f4f1ea"

The master should be the simplified symbol (or one letter), not the full wordmark; check
favicon-16.png by eye. The OG file is only a placeholder; lay out the real one as its own
SVG (mark plus wordmark) and render it with render.py.
"""

import argparse
import io
import re
import sys
from pathlib import Path

import resvg_py

try:
    from PIL import Image
except ImportError:
    Image = None


def viewbox_ratio(svg):
    """Return width / height from the root viewBox (1.0 if there is none)."""
    m = re.search(r'viewBox="\s*([-\d.e]+)[\s,]+([-\d.e]+)[\s,]+([-\d.e]+)[\s,]+([-\d.e]+)', svg)
    if not m:
        return 1.0
    w, h = float(m.group(3)), float(m.group(4))
    return w / h if h else 1.0


def raw_png(svg, w, h, background=None):
    """Render SVG text to PNG bytes at exactly w x h pixels."""
    return bytes(resvg_py.svg_to_bytes(svg_string=svg, width=int(w), height=int(h),
                                       background=background))


def tile(svg, width, height, bg, pad):
    """Return an RGBA image: the mark fitted inside `pad` and centred on a bg canvas."""
    ratio = viewbox_ratio(svg)
    bw, bh = width - 2 * pad, height - 2 * pad
    w, h = (bw, round(bw / ratio)) if bw / bh <= ratio else (round(bh * ratio), bh)
    art = Image.open(io.BytesIO(raw_png(svg, max(1, w), max(1, h)))).convert("RGBA")
    canvas = Image.new("RGBA", (width, height), bg)
    canvas.alpha_composite(art, ((width - w) // 2, (height - h) // 2))
    return canvas


def favicon_svg(svg, color, dark_color):
    """Return the master with currentColor fixed and a dark-scheme override.

    A favicon has no parent text colour, so currentColor would be black. The style
    rule swaps every currentColor fill to dark_color when the browser is dark.
    """
    fixed = svg.replace("currentColor", color)
    if "currentColor" not in svg or not dark_color:
        return fixed
    rule = (f"<style>@media (prefers-color-scheme: dark)"
            f"{{[fill=\"{color}\"]{{fill:{dark_color}}}}}</style>")
    return re.sub(r"(<svg\b[^>]*>)", r"\1" + rule.replace("\\", "\\\\"), fixed, count=1)


def favicon_svg_pairs(svg, pairs):
    """Return a multi-colour mark with one dark-scheme rule per fixed fill colour.

    pairs: [(light_hex, dark_hex)]. Every fill="light_hex" in the master switches to
    dark_hex when the browser is dark (for two-tone marks, where currentColor cannot work).
    """
    rules = "".join(f"[fill=\"{lt}\"]{{fill:{dk}}}" for lt, dk in pairs if lt.lower() != dk.lower())
    if not rules:
        return svg
    rule = f"<style>@media (prefers-color-scheme: dark){{{rules}}}</style>"
    return re.sub(r"(<svg\b[^>]*>)", lambda m: m.group(1) + rule, svg, count=1)


def write_pack(master, out, bg, pad_avatar=80):
    """Write the PNG and ICO files for a mark whose colours are already fixed.

    Same sizes and padding as the command line; returns the written file names.
    """
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    plan = {
        "favicon-16.png": (16, 16, 1),
        "favicon-32.png": (32, 32, 2),
        "apple-touch-icon-180.png": (180, 180, 20),
        "icon-512.png": (512, 512, 56),
        "avatar-400.png": (400, 400, pad_avatar),
    }
    names = []
    for name, (w, h, pad) in plan.items():
        img = tile(master, w, h, bg, pad)
        if name.startswith("apple") or name.startswith("avatar") or name.startswith("icon"):
            img = img.convert("RGB")
        img.save(out / name)
        names.append(name)
    ico_src = tile(master, 256, 256, bg, 16)
    ico_src.save(out / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    names.append("favicon.ico")
    return names


# ---------------------------------------------------------------- LinkedIn files and mocks
def text_path(font_path, text, size, x=0.0, y=0.0):
    """Text as one SVG path (advance widths, no kerning), baseline at y. Returns (d, width).

    Needs fontTools. Used for mock labels so a render never depends on system fonts.
    """
    from fontTools.pens.svgPathPen import SVGPathPen
    from fontTools.pens.transformPen import TransformPen
    from fontTools.ttLib import TTFont
    tt = _FONTS.get(font_path)
    if tt is None:
        tt = _FONTS[font_path] = TTFont(font_path)
    gs, cmap, hmtx = tt.getGlyphSet(), tt.getBestCmap(), tt["hmtx"]
    sc = size / tt["head"].unitsPerEm
    pen = SVGPathPen(gs, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
    cx = x
    for ch in text:
        name = cmap.get(ord(ch), ".notdef")
        gs[name].draw(TransformPen(pen, (sc, 0, 0, -sc, cx, y)))
        cx += hmtx[name][0] * sc
    return pen.getCommands(), cx - x


_FONTS = {}


def _b64(path):
    import base64
    return "data:image/png;base64," + base64.b64encode(Path(path).read_bytes()).decode("ascii")


def _vb(svg):
    m = re.search(r'viewBox="([^"]+)"', svg)
    return [float(v) for v in m.group(1).replace(",", " ").split()]


def _nest(svg, x, y, h):
    """Place an SVG's drawing at (x, y) at height h. Returns (markup, width)."""
    vx, vy, vw, vh = _vb(svg)
    w = h * vw / vh
    body = svg[svg.index(">") + 1:svg.rindex("</svg>")]
    body = re.sub(r"<title>.*?</title>", "", body)
    return (f'<svg x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" '
            f'viewBox="{vx} {vy} {vw} {vh}">{body}</svg>'), w


def _doc(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
            f"{body}</svg>")


def _rr(x, y, w, h, r, fill, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"{extra}/>'


def _txt(font, text, size, x, y, fill):
    d, w = text_path(font, text, size, x, y)
    return f'<path fill="{fill}" d="{d}"/>', w


def _png(svg, path):
    Path(path).write_bytes(raw_png(svg, *[int(v) for v in _vb(svg)[2:]]))


def linkedin_pack(out, lockup_light, lockup_dark, avatar_png, og_png, colors, font_regular, font_bold,
                  name="userandproduct", tagline="UX, product and business, from a practitioner",
                  followers="Publishing · 1,204 followers", post="New on the site: how to write a "
                  "product brief people actually read.", site="userandproduct.com"):
    """Write the LinkedIn banners and mocks for one colour scheme.

    lockup_light / lockup_dark: SVG text with fixed colours. avatar_png: the square avatar (mark with a
    safe margin; LinkedIn crops it to a circle). og_png: the 1200 x 630 social image.
    colors: bg_light, bg_dark, accent_light, accent_dark, on_accent_light, on_accent_dark.
    Writes linkedin-banner-1128x191.png, linkedin-banner-dark-1128x191.png, linkedin-avatar-400.png,
    linkedin-mock-light.png, linkedin-mock-dark.png and linkedin-post-light.png; returns the names.
    """
    out = Path(out)
    names = []
    # banners: lockup 52 px tall, centred on 42 percent of the width (LinkedIn's avatar covers the lower left)
    for mode, lock, fn in (("light", lockup_light, "linkedin-banner-1128x191.png"),
                           ("dark", lockup_dark, "linkedin-banner-dark-1128x191.png")):
        h = 52
        vx, vy, vw, vh = _vb(lock)
        w = h * vw / vh
        art, _ = _nest(lock, 1128 * 0.42 - w / 2, (191 - h) / 2, h)
        _png(_doc(1128, 191, _rr(0, 0, 1128, 191, 0, colors["bg_" + mode]) + art), out / fn)
        names.append(fn)
    (out / "linkedin-avatar-400.png").write_bytes(Path(avatar_png).read_bytes())
    names.append("linkedin-avatar-400.png")

    av = _b64(avatar_png)
    ui = {"light": dict(page="#F4F2EE", card="#FFFFFF", text="#191919", sub="#666666", line="#E0DFDC"),
          "dark": dict(page="#000000", card="#1B1F23", text="#E9E9E9", sub="#A3A3A3", line="#38434F")}
    # company page mock, 800 x 360
    for mode in ("light", "dark"):
        u = ui[mode]
        ban = _b64(out / ("linkedin-banner-1128x191.png" if mode == "light" else
                          "linkedin-banner-dark-1128x191.png"))
        bh = 800 * 191 / 1128
        ring = "#FFFFFF" if mode == "light" else u["card"]
        body = [_rr(0, 0, 800, 360, 0, u["page"]), _rr(8, 8, 784, 344, 10, u["card"],
                f' stroke="{u["line"]}"'),
                '<clipPath id="bc"><rect x="8" y="8" width="784" height="344" rx="10"/></clipPath>',
                f'<image clip-path="url(#bc)" x="8" y="8" width="784" height="{bh * 784 / 800:.2f}" '
                f'preserveAspectRatio="none" href="{ban}"/>']
        by = 8 + bh * 784 / 800
        body.append(f'<rect x="8" y="{by - 0.5:.2f}" width="784" height="1" fill="{u["line"]}"/>')
        ay, ar = by - 52, 52
        body.append(f'<circle cx="{32 + ar}" cy="{ay + ar}" r="{ar + 4.5}" fill="{u["line"]}"/>')
        body.append(f'<circle cx="{32 + ar}" cy="{ay + ar}" r="{ar + 4}" fill="{ring}"/>')
        body.append(f'<clipPath id="ac"><circle cx="{32 + ar}" cy="{ay + ar}" r="{ar}"/></clipPath>')
        body.append(f'<image clip-path="url(#ac)" x="32" y="{ay}" width="{2 * ar}" height="{2 * ar}" href="{av}"/>')
        y0 = ay + 2 * ar + 34
        body.append(_txt(font_bold, name, 24, 32, y0, u["text"])[0])
        body.append(_txt(font_regular, tagline, 15, 32, y0 + 26, u["text"])[0])
        body.append(_txt(font_regular, followers, 13, 32, y0 + 48, u["sub"])[0])
        fy = y0 + 64
        label, lw = _txt(font_bold, "+ Follow", 15, 0, 0, colors["on_accent_" + mode])
        bw = lw + 36
        body.append(_rr(32, fy, round(bw, 2), 32, 16, colors["accent_" + mode]))
        body.append(_txt(font_bold, "+ Follow", 15, 32 + 18, fy + 21, colors["on_accent_" + mode])[0])
        fn = f"linkedin-mock-{mode}.png"
        _png(_doc(800, 360, "".join(body)), out / fn)
        names.append(fn)

    # post card with link preview, 560 wide
    u = ui["light"]
    ogh = 560 * 630 / 1200
    top = 112
    H = int(top + ogh + 56)
    body = [_rr(0, 0, 560, H, 10, u["card"], f' stroke="{u["line"]}"'),
            '<clipPath id="pc"><circle cx="40" cy="40" r="24"/></clipPath>',
            f'<image clip-path="url(#pc)" x="16" y="16" width="48" height="48" href="{av}"/>',
            _txt(font_bold, name, 15, 76, 36, u["text"])[0],
            _txt(font_regular, "1,204 followers · 1h", 12, 76, 54, u["sub"])[0],
            _txt(font_regular, post, 14, 16, 94, u["text"])[0],
            f'<clipPath id="cc"><rect x="0" y="0" width="560" height="{H}" rx="10"/></clipPath><g clip-path="url(#cc)">',
            f'<image x="0" y="{top}" width="560" height="{ogh:.2f}" preserveAspectRatio="none" href="{_b64(og_png)}"/>',
            _rr(0, top + ogh, 560, 56, 0, "#EEF3F8"),
            f'<rect x="0" y="{top - 0.5}" width="560" height="1" fill="{u["line"]}"/>',
            f'<rect x="0" y="{top + ogh - 0.5:.2f}" width="560" height="1" fill="{u["line"]}"/></g>',
            _txt(font_bold, "How to write a product brief people actually read", 14, 16, top + ogh + 24, u["text"])[0],
            _txt(font_regular, site, 12, 16, top + ogh + 44, u["sub"])[0]]
    body.append(f'<rect x="0.5" y="0.5" width="559" height="{H - 1}" rx="10" fill="none" stroke="{u["line"]}"/>')
    _png(_doc(560, H, "".join(body)), out / "linkedin-post-light.png")
    names.append("linkedin-post-light.png")
    return names


def main(argv=None):
    """Command-line entry point."""
    ap = argparse.ArgumentParser(description="Make favicons, app icons and social images.")
    ap.add_argument("svg", help="master SVG mark (square works best)")
    ap.add_argument("out", help="output folder")
    ap.add_argument("--bg", default="#111111", help="tile background colour")
    ap.add_argument("--color", default="#ffffff", help="colour for currentColor on the tile")
    ap.add_argument("--svg-color", default="#111111", help="favicon.svg colour, light tabs")
    ap.add_argument("--dark-color", default="#f5f5f5", help="favicon.svg colour, dark tabs")
    ap.add_argument("--og-bg", default=None, help="OG background (default: --bg)")
    args = ap.parse_args(argv)

    src = Path(args.svg)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    master = src.read_text(encoding="utf-8")
    on_tile = master.replace("currentColor", args.color)

    (out / "favicon.svg").write_text(favicon_svg(master, args.svg_color, args.dark_color),
                                     encoding="utf-8")
    print(f"wrote {out / 'favicon.svg'}  (optimize: npx svgo@4.1.0 favicon.svg)")

    if Image is None:
        print("Pillow is not installed: PNG tiles, favicon.ico and padded images skipped. "
              "Install with: python -m pip install --user pillow", file=sys.stderr)
        return

    # name: (width, height, padding)
    plan = {
        "favicon-16.png": (16, 16, 1),
        "favicon-32.png": (32, 32, 2),
        "apple-touch-icon-180.png": (180, 180, 20),
        "icon-512.png": (512, 512, 56),
        "avatar-400.png": (400, 400, 80),
    }
    og_bg = args.og_bg or args.bg
    for name, (w, h, pad) in plan.items():
        img = tile(on_tile, w, h, args.bg, pad)
        if name.startswith("apple"):
            img = img.convert("RGB")  # iOS wants no transparency
        img.save(out / name)
        print(f"wrote {out / name}")

    og = tile(on_tile, 1200, 630, og_bg, 165).convert("RGB")
    og.save(out / "og-1200x630.png")
    print(f"wrote {out / 'og-1200x630.png'}  (placeholder layout)")

    ico_src = tile(on_tile, 256, 256, args.bg, 16)
    ico_src.save(out / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    print(f"wrote {out / 'favicon.ico'}  (16, 32, 48)")


if __name__ == "__main__":
    main()
