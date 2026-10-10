"""Build logo exploration 2, round 1: ten marks, their renders, lockups, thumbnail tiles and the board.

Run from this folder:  python build.py
Writes ../svg/, ../png/, ../index.html. Needs fontTools, skia-pathops, resvg-py and Pillow, plus
research/mockups/tools/render.py and the final wordmark in research/mockups/final-logo/svg/.
"""

import io
import math
import re
import sys
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
ROUND = HERE.parent
MOCK = ROUND.parent.parent
sys.path.insert(0, str(MOCK / "tools"))
sys.path.insert(0, str(HERE))

from render import render_png  # noqa: E402
import marks as M  # noqa: E402
from ideas import IDEAS  # noqa: E402

SVG_DIR = ROUND / "svg"
PNG_DIR = ROUND / "png"

PAPER_L, PAPER_D = "#FFFFFF", "#0B0B0C"
INK_L, INK_D = "#0B0B0C", "#F1EEE7"

# Palettes by family. Container marks keep the same colours in light and dark (an app icon is one
# file); free-standing marks lift their tones on near-black, as the brand's signal blue does.
PAL = {
    "blue": {
        "box": {"c": "#2B46A0", "a": "#FFFFFF", "b": "#A9BBFF", "f": "#5A7BF0", "o": "#5A7BF0"},
        "box-dark": {"c": "#2B46A0", "a": "#FFFFFF", "b": "#A9BBFF", "f": "#5A7BF0", "o": "#8EA2FF"},
        "free": {"a": "#2B46A0", "b": "#5A7BF0", "f": "#A9BBFF"},
        "free-dark": {"a": "#8EA2FF", "b": "#4F6FE6", "f": "#D2DBFF"},
    },
    "coral": {
        "box": {"c": "#C23B26", "a": "#FFFFFF", "b": "#FFC4B4", "f": "#EE7A5F", "o": "#C23B26"},
        "box-dark": {"c": "#C23B26", "a": "#FFFFFF", "b": "#FFC4B4", "f": "#EE7A5F", "o": "#FF8A70"},
    },
    "teal": {
        "free": {"a": "#0F6E61", "b": "#2FA38E", "f": "#A8E6D7"},
        "free-dark": {"a": "#4CC9B0", "b": "#1E8A77", "f": "#C9F2E8"},
    },
    "oxblood": {
        "box": {"c": "#7A1F2B", "a": "#FFFFFF", "b": "#F0B9BF", "f": "#B4505E", "o": "#7A1F2B"},
        "box-dark": {"c": "#7A1F2B", "a": "#FFFFFF", "b": "#F0B9BF", "f": "#B4505E", "o": "#E07B88"},
    },
}

# Bold thumbnail grounds (one per idea), from the thumbnail rules' suggestions.
TILES = ["#F2C230", "#E8552E", "#6B4FD8", "#0E8C7A", "#111216", "#1F5BFF", "#F28AB2", "#2B2F3A", "#C9F23A", "#B3141C"]


def hex2rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def lum(h):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(v) for v in hex2rgb(h))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(x, y):
    a, b = sorted((lum(x), lum(y)), reverse=True)
    return (a + 0.05) / (b + 0.05)


def mix(x, y, t):
    a, b = hex2rgb(x), hex2rgb(y)
    return "#" + "".join(f"{round(a[i] + (b[i] - a[i]) * t):02X}" for i in range(3))


# ---------- composing SVG ----------

def container_path(kind):
    if kind == "circle":
        return M.P(M.circle(256, 256, 256))
    return M.P(M.squircle(0, 0, 512))


def mark_layers(spec):
    """Layers of the master mark, container first."""
    kind = spec["container"]
    if kind in ("circle", "squircle"):
        return [("c", container_path(kind))] + spec["layers"]
    return spec["layers"]


def paths_svg(layers, pal, T=None):
    out = []
    for role, p in layers:
        d = M.D(p, T)
        if d:
            out.append(f'<path fill="{pal[role]}" d="{d}"/>')
    return "".join(out)


def svg_doc(body, vb="0 0 512 512", label="userandproduct mark"):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{label}">'
            f"<title>{label}</title>{body}</svg>")


def tile_layers(spec):
    """Full-bleed square composition for the avatar crops: the crop is the container."""
    kind = spec["container"]
    if kind == "squircle-inset":
        # scale the inset tile up to the full canvas; whatever leaves it is cut by the crop
        T = M.affine(scale=512 / 400, dx=-56 * 512 / 400, dy=-56 * 512 / 400)
        lay = [(r, p) for r, p in spec["layers"] if r != "c"]
        lay = [("a" if r == "o" else r, p) for r, p in lay]
        return lay, T, "c"
    if kind in ("circle", "squircle"):
        return spec["layers"], None, "c"
    T = M.affine(scale=0.74, dx=256 * 0.26, dy=256 * 0.26)
    return spec["layers"], T, None


def mono_palette(spec, ink, ground):
    """One-colour version for the thumbnail lockup: ink and its tints over the tile ground."""
    if spec["container"]:
        return {"c": ink, "a": ground, "b": mix(ground, ink, 0.45), "f": mix(ground, ink, 0.25), "o": ink}
    return {"a": ink, "b": mix(ink, ground, 0.4), "f": mix(ink, ground, 0.7)}


# ---------- wordmark and lockup ----------

WM = (MOCK / "final-logo" / "svg" / "wordmark-black.svg").read_text(encoding="utf-8")
WM_D = re.search(r' d="([^"]+)"', WM).group(1)
H = 101.85          # mark height in wordmark units (1.4 cap heights), as in the final pack
CY = -31.08         # mark centre above the baseline
GAP = 40.74
WM_W = 735.01       # wordmark ink width (viewBox width minus the 4-unit margins)


def lockup_svg(spec, pal, ink, label="userandproduct"):
    s = H / 512
    T = M.affine(scale=s, dx=0, dy=CY - H / 2)
    mark = paths_svg(mark_layers(spec), pal, T)
    word = f'<g transform="translate({M.fmt(H + GAP)} 0)"><path fill="{ink}" d="{WM_D}"/></g>'
    top = CY - H / 2 - 4
    bottom = max(24.41, CY + H / 2) + 4
    vb = f"-4 {M.fmt(top)} {M.fmt(H + GAP + WM_W + 8)} {M.fmt(bottom - top)}"
    return svg_doc(mark + word, vb, label)


# ---------- rendering ----------

def png(svg, w, h=None):
    return Image.open(io.BytesIO(render_png(svg, w, h))).convert("RGBA")


def mask_png(shape, size):
    d = M.circle(256, 256, 256) if shape == "circle" else M.squircle(0, 0, 512)
    return png(svg_doc(f'<path fill="#000" d="{d}"/>'), size, size).split()[3]


def avatar(spec, pal, ground, shape, size):
    lay, T, bgrole = tile_layers(spec)
    bg = pal[bgrole] if bgrole else ground
    body = f'<rect width="512" height="512" fill="{bg}"/>' + paths_svg(lay, pal, T)
    art = png(svg_doc(body), size * 4, size * 4).resize((size, size), Image.LANCZOS)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(art, (0, 0), mask_png(shape, size * 4).resize((size, size), Image.LANCZOS))
    return out


def thumb_tile(spec, ground, label):
    ink = "#0B0B0C" if contrast(ground, "#0B0B0C") >= contrast(ground, "#FFFFFF") else "#FFFFFF"
    lock = lockup_svg(spec, mono_palette(spec, ink, ground), ink)
    vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', lock).group(1).split()]
    w = 120
    h = w * vb[3] / vb[2]
    inner = re.sub(r"^<svg[^>]*>", "", lock).replace("</svg>", "")
    inner = re.sub(r"<title>.*?</title>", "", inner)
    # a quiet stand-in subject so the corner placement reads as it would on a real thumb
    subject = (f'<rect x="300" y="84" width="220" height="170" rx="14" fill="{ink}" opacity=".14"/>'
               f'<rect x="324" y="110" width="120" height="16" rx="8" fill="{ink}" opacity=".22"/>'
               f'<rect x="324" y="140" width="172" height="12" rx="6" fill="{ink}" opacity=".16"/>')
    body = (f'<rect width="600" height="338" fill="{ground}"/>{subject}'
            f'<svg x="20" y="20" width="{w}" height="{M.fmt(h)}" viewBox="{" ".join(M.fmt(v) for v in vb)}" opacity=".92">{inner}</svg>')
    return svg_doc(body, "0 0 600 338", label), ink


def optimise():
    """Compact every SVG with SVGO 4.1.0 (keeps the viewBox), then restore role="img"."""
    import subprocess
    try:
        subprocess.run(f'npx -y svgo@4.1.0 -q -f "{SVG_DIR}" -o "{SVG_DIR}"', shell=True, check=True)
    except Exception as err:  # SVGO is optional; the raw files are valid
        print("svgo skipped:", err)
        return
    for f in SVG_DIR.glob("*.svg"):
        t = f.read_text(encoding="utf-8")
        if 'role="img"' not in t:
            t = t.replace("<svg ", '<svg role="img" ', 1)
            f.write_text(t, encoding="utf-8")


def main():
    SVG_DIR.mkdir(exist_ok=True)
    PNG_DIR.mkdir(exist_ok=True)
    report = []
    for i, (fn, idea) in enumerate(zip(M.MARKS, IDEAS), start=1):
        spec = fn()
        slug = f"r1-{i:02d}"
        free = spec["container"] is None
        fam = idea.get("family", "blue")
        light = PAL["blue"]["free" if free else "box"]
        dark = PAL["blue"]["free-dark" if free else "box-dark"]
        files = {
            f"{slug}-mark-light.svg": svg_doc(paths_svg(mark_layers(spec), light), label=f"{idea['name']} mark"),
            f"{slug}-mark-dark.svg": svg_doc(paths_svg(mark_layers(spec), dark), label=f"{idea['name']} mark"),
            f"{slug}-lockup-light.svg": lockup_svg(spec, light, INK_L),
            f"{slug}-lockup-dark.svg": lockup_svg(spec, dark, INK_D),
        }
        tile_svg, tile_ink = thumb_tile(spec, TILES[i - 1], f"{idea['name']} on a thumbnail")
        files[f"{slug}-thumb.svg"] = tile_svg
        if fam != "blue":
            al = PAL[fam]["free" if free else "box"]
            ad = PAL[fam]["free-dark" if free else "box-dark"]
            files[f"{slug}-alt-mark-light.svg"] = svg_doc(paths_svg(mark_layers(spec), al), label=f"{idea['name']} mark, {fam}")
            files[f"{slug}-alt-mark-dark.svg"] = svg_doc(paths_svg(mark_layers(spec), ad), label=f"{idea['name']} mark, {fam}")
        for name, text in files.items():
            (SVG_DIR / name).write_text(text, encoding="utf-8")
        # PNGs: avatars (110 circle and rounded square, light and dark), favicons 32, thumb 600
        for theme, pal, ground in (("light", light, PAPER_L), ("dark", dark, PAPER_D)):
            for shape in ("circle", "square"):
                avatar(spec, pal, ground, "circle" if shape == "circle" else "squircle", 110).save(
                    PNG_DIR / f"{slug}-avatar-{shape}-{theme}-110.png")
            fav = png(files[f"{slug}-mark-{theme}.svg"], 32, 32)
            fav.save(PNG_DIR / f"{slug}-favicon-{theme}-32.png")
        if fam != "blue":
            al = PAL[fam]["free" if free else "box"]
            ad = PAL[fam]["free-dark" if free else "box-dark"]
            for theme, pal, ground in (("light", al, PAPER_L), ("dark", ad, PAPER_D)):
                for shape in ("circle", "square"):
                    avatar(spec, pal, ground, "circle" if shape == "circle" else "squircle", 110).save(
                        PNG_DIR / f"{slug}-alt-avatar-{shape}-{theme}-110.png")
                png(files[f"{slug}-alt-mark-{theme}.svg"], 32, 32).save(PNG_DIR / f"{slug}-alt-favicon-{theme}-32.png")
        png(tile_svg, 600, 338).convert("RGB").save(PNG_DIR / f"{slug}-thumb-600.png")
        sizes = {n: len(t.encode()) for n, t in files.items()}
        report.append((slug, idea["name"], max(v for n, v in sizes.items() if "-mark-" in n), max(sizes.values()), tile_ink))
    optimise()
    for r in report:
        print(*r)
    import board
    board.write(ROUND, IDEAS, TILES)


if __name__ == "__main__":
    main()
