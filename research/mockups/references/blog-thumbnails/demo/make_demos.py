"""Four 600 x 338 demonstrations for the thumbnail-styles board, made here with code on our palette.
Run: python research/mockups/references/blog-thumbnails/demo/make_demos.py
Writes demo-a-flat-vector.png, demo-b-pixel-icon.png, demo-c-dark-diagram.png, demo-d-halftone.png and times.json.
Source for (d): a screenshot of the owner's own Printables site (the Halloween calendar sheet)."""
import io
import json
import math
import sys
import time
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageOps
import resvg_py

HERE = Path(__file__).resolve().parent
MOCKUPS = HERE.parents[2]                      # research/mockups
sys.path.insert(0, str(MOCKUPS / "tools"))
from illustration import TINTS, INK, CARD, MARK, palette_for  # noqa: E402

W, H, OUT = 1200, 675, (600, 338)
SRC = Path(r"C:\xampp\htdocs\Printables\research\mockups\collections-strip\_screens\A1-desktop.png")
MONO = "Consolas"


def render(svg, mode="RGB"):
    png = resvg_py.svg_to_bytes(svg_string=svg, width=W * 2, height=H * 2)
    return Image.open(io.BytesIO(bytes(png))).convert(mode)


def finish(img, name, grain=0.0, seed=7):
    img = img.resize(OUT, Image.LANCZOS)
    if grain:
        rng = np.random.default_rng(seed)
        a = np.asarray(img).astype(np.float32)
        n = rng.normal(0, grain, a.shape[:2])[..., None]
        img = Image.fromarray(np.clip(a + n, 0, 255).astype(np.uint8))
    img.save(HERE / name, optimize=True)


def svg_open(bg=None):
    s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
    if bg:
        s += f'<rect width="{W}" height="{H}" fill="{bg}"/>'
    return s


def dots(color, opacity, step=22, r=1.9):
    return (f'<defs><pattern id="dg" width="{step}" height="{step}" patternUnits="userSpaceOnUse">'
            f'<circle cx="{step / 2}" cy="{step / 2}" r="{r}" fill="{color}" fill-opacity="{opacity}"/></pattern></defs>'
            f'<rect width="{W}" height="{H}" fill="url(#dg)"/>')


def mark(color, opacity=0.35, size=34, inset=32):
    s = size / 102
    x, y = W - inset - size, H - inset - size
    return (f'<g transform="translate({x},{y}) scale({s}) translate(1,1)" fill="{color}" fill-opacity="{opacity}">'
            f'<path d="{MARK}"/></g>')


# ---------- (a) flat vector, hard shadows, grained grid ----------
def demo_a():
    p = palette_for("yellow")
    bg, A = TINTS["yellow"], p["a"]
    sh = 14

    def shape(tag, fill, **kw):
        attrs = " ".join(f'{k.replace("_", "-")}="{v}"' for k, v in kw.items())
        return (f'<{tag} {attrs} fill="{INK}" transform="translate({sh},{sh})"/>'
                f'<{tag} {attrs} fill="{fill}" stroke="{INK}" stroke-width="3.5" stroke-linejoin="round"/>')

    s = svg_open(bg)
    for x in range(0, W + 1, 75):
        s += f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="{INK}" stroke-opacity=".10" stroke-width="2"/>'
    for y in range(0, H + 1, 75):
        s += f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="{INK}" stroke-opacity=".10" stroke-width="2"/>'
    for y in (300, 322, 344):                     # flow lines running in from the left
        s += f'<line x1="0" y1="{y}" x2="330" y2="{y}" stroke="{INK}" stroke-width="3"/>'
    s += shape("rect", CARD, x=330, y=150, width=520, height=360, rx=12)   # browser window
    s += f'<line x1="330" y1="200" x2="850" y2="200" stroke="{INK}" stroke-width="3.5"/>'
    for i in range(3):
        s += f'<circle cx="{362 + i * 26}" cy="175" r="7" fill="none" stroke="{INK}" stroke-width="3"/>'
    s += f'<rect x="366" y="232" width="210" height="140" rx="6" fill="{A}" stroke="{INK}" stroke-width="3"/>'
    for i, w in enumerate((220, 180, 200, 140)):
        s += (f'<rect x="604" y="{240 + i * 34}" width="{w}" height="12" rx="6" fill="{INK}" '
              f'fill-opacity="{.85 if i == 0 else .35}"/>')
    s += f'<rect x="366" y="404" width="130" height="50" rx="25" fill="{INK}"/>'
    s += f'<rect x="512" y="404" width="130" height="50" rx="25" fill="none" stroke="{INK}" stroke-width="3"/>'
    s += shape("path", A, d="M800 92 h210 a14 14 0 0 1 14 14 v110 a14 14 0 0 1 -14 14 h-130 l-40 38 v-38 h-40 "
                              "a14 14 0 0 1 -14 -14 v-110 a14 14 0 0 1 14 -14 z")              # speech bubble
    s += (f'<path d="M862 160 l30 30 l62 -64" fill="none" stroke="{INK}" stroke-width="12" '
          f'stroke-linecap="round" stroke-linejoin="round"/>')
    s += shape("path", CARD, d="M690 360 l0 170 l42 -40 l30 66 l34 -16 l-30 -64 l58 -6 z")  # cursor
    for cx, cy, r in ((235, 170, 16), (1000, 450, 20), (1060, 380, 11)):
        s += f'<path d="M{cx - r} {cy} h{2 * r} M{cx} {cy - r} v{2 * r}" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>'
    s += mark(INK) + "</svg>"
    finish(render(s), "demo-a-flat-vector.png", grain=11)


# ---------- (b) pixel icons, flat tint, dot grid ----------
PERSON = """
.....####.....
....######....
...########...
...########...
...########...
...########...
....######....
.....####.....
..............
...########...
..##########..
.############.
.############.
.############.
.############.
.############.
"""
WINDOW = """
####################
#..................#
#.#.#.#............#
####################
#..................#
#.########.........#
#.########..######.#
#.########.........#
#.########..#####..#
#.########.........#
#.########..######.#
#..................#
#.####..####.......#
#..................#
####################
"""


def cells(rows):
    rows = rows.strip("\n").split("\n")
    return {(i, j) for j, r in enumerate(rows) for i, ch in enumerate(r) if ch == "#"}


def demo_b():
    p = palette_for("teal")
    bg, A, B = TINTS["teal"], p["a"], p["b"]
    c = 16

    def px(x, y, color, size=c):
        return f'<rect x="{x}" y="{y}" width="{size}" height="{size}" fill="{color}"/>'

    s = svg_open(bg) + dots(INK, .13)
    # person: ink outline, interior dithered card and highlight B
    filled = cells(PERSON)
    edge = {(i, j) for (i, j) in filled
            if any((i + di, j + dj) not in filled for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)))}
    x0, y0 = 170, 200
    for (i, j) in filled - edge:
        s += px(x0 + i * c, y0 + j * c, B if (i + j) % 2 == 0 else CARD)
    for (i, j) in edge:
        s += px(x0 + i * c, y0 + j * c, INK)
    # window: card fill, ink outline, hero block dithered in highlight A
    wx, wy = 700, 205
    s += f'<rect x="{wx + c}" y="{wy + c}" width="{18 * c}" height="{13 * c}" fill="{CARD}"/>'
    for (i, j) in cells(WINDOW):
        if 5 <= j <= 10 and 2 <= i <= 9:
            s += px(wx + i * c, wy + j * c, A if (i + j) % 2 else INK)
        else:
            s += px(wx + i * c, wy + j * c, INK)
    # arrows: user to product in ink, product back to user in highlight B
    for x in range(450, 640, 2 * c):
        s += px(x, 300, INK)
    for k in range(3):                              # head pointing right at x=650
        for dy in range(-k, k + 1):
            s += px(650 - (k - 2) * c - 2 * c, 300 + dy * c, INK)
    for x in range(498, 690, 2 * c):
        s += px(x, 390, B)
    for k in range(3):                              # head pointing left at x=450
        for dy in range(-k, k + 1):
            s += px(450 + k * c, 390 + dy * c, B)
    for (x, y) in ((560, 170), (1070, 140), (110, 530), (990, 540)):   # pixel sparks
        for dx, dy in ((0, 0), (-8, -8), (8, -8), (-8, 8), (8, 8)):
            s += px(x + dx, y + dy, INK, 8)
    s += mark(INK) + "</svg>"
    finish(render(s), "demo-b-pixel-icon.png")


# ---------- (c) dark line diagram, one accent ----------
def demo_c():
    acc = palette_for("yellow")["a"]
    s = svg_open(INK) + dots("#FFFFFF", .07)
    labels = ["idea", "discovery", "build", "ship"]
    bw, bh, gap, y = 200, 76, 70, 250
    x0 = (W - (4 * bw + 3 * gap)) / 2
    xs = [x0 + i * (bw + gap) for i in range(4)]
    for i, (x, t) in enumerate(zip(xs, labels)):
        accent = i == 1
        col = acc if accent else "#FFFFFF"
        fill = f'fill="{acc}" fill-opacity=".14"' if accent else 'fill="none"'
        s += (f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="10" {fill} stroke="{col}" '
              f'stroke-opacity="{1 if accent else .78}" stroke-width="2.5"/>')
        s += (f'<text x="{x + bw / 2}" y="{y + bh / 2 + 9}" text-anchor="middle" font-family="{MONO}" font-size="27" '
              f'fill="{col}" fill-opacity="{1 if accent else .9}">{t}</text>')
        s += f'<text x="{x}" y="{y - 22}" font-family="{MONO}" font-size="20" fill="#FFFFFF" fill-opacity=".45">0{i + 1}</text>'
        if i < 3:
            ax1, ax2, ay = x + bw + 8, x + bw + gap - 10, y + bh / 2
            s += (f'<line x1="{ax1}" y1="{ay}" x2="{ax2}" y2="{ay}" stroke="#FFFFFF" stroke-opacity=".7" stroke-width="2.5"/>'
                  f'<path d="M{ax2 - 12} {ay - 7} L{ax2} {ay} L{ax2 - 12} {ay + 7}" fill="none" stroke="#FFFFFF" '
                  f'stroke-opacity=".7" stroke-width="2.5"/>')
    lx1, lx2, ly = xs[3] + bw / 2, xs[1] + bw / 2, y + bh       # feedback loop, dashed, in the accent
    s += (f'<path d="M{lx1} {ly + 8} V{ly + 120} H{lx2} V{ly + 18}" fill="none" stroke="{acc}" stroke-width="3" '
          f'stroke-dasharray="12 9"/>'
          f'<path d="M{lx2 - 9} {ly + 31} L{lx2} {ly + 16} L{lx2 + 9} {ly + 31}" fill="none" stroke="{acc}" stroke-width="3"/>'
          f'<text x="{(lx1 + lx2) / 2}" y="{ly + 160}" text-anchor="middle" font-family="{MONO}" font-size="24" '
          f'fill="{acc}">what users did</text>')
    s += mark("#FFFFFF") + "</svg>"
    finish(render(s), "demo-c-dark-diagram.png")


# ---------- (d) halftone of a source image ----------
def demo_d():
    bg = TINTS["pink"]
    sheet = Image.open(SRC).convert("L").crop((200, 1598, 456, 1930))   # the Halloween calendar sheet
    sheet = ImageOps.autocontrast(sheet, cutoff=1)
    S = 2                                                    # work at 2400 x 1350
    cw, ch = W * S, H * S
    sw = 430 * S
    big = sheet.resize((sw, int(sw * sheet.height / sheet.width)), Image.LANCZOS)
    big = ImageOps.expand(big, border=6 * S, fill=30)        # dark edge so the sheet reads
    layer = Image.new("L", (big.width + 200 * S, big.height + 200 * S), 255)
    layer.paste(Image.new("L", big.size, 70), (126 * S, 126 * S))      # soft offset shadow
    layer = layer.filter(ImageFilter.GaussianBlur(10 * S))
    layer.paste(big, (100 * S, 100 * S))
    rot = layer.rotate(-7, resample=Image.BICUBIC, expand=True, fillcolor=255)
    tone = Image.new("L", (cw, ch), 255)
    tone.paste(rot, ((cw - rot.width) // 2 + 40 * S, (ch - rot.height) // 2))
    t = np.clip((1 - np.asarray(tone).astype(np.float32) / 255 - .04) * 1.25, 0, 1)

    img = Image.new("RGB", (cw, ch), bg)
    d = ImageDraw.Draw(img)
    for gy in range(11 * S, ch, 22 * S):                     # faint dot grid
        for gx in range(11 * S, cw, 22 * S):
            d.ellipse((gx - 2, gy - 2, gx + 2, gy + 2), fill=(214, 194, 199))
    cell, ang = 13 * S / 2, math.radians(45)                 # 45-degree dot screen
    ca, sa = math.cos(ang), math.sin(ang)
    tb = np.asarray(Image.fromarray((t * 255).astype(np.uint8)).filter(
        ImageFilter.BoxBlur(int(cell / 2)))).astype(np.float32) / 255
    R = int(math.hypot(cw, ch) / cell) + 2
    for u in range(-R, R):
        for v in range(-R, R):
            x = (u * ca - v * sa) * cell + cw / 2
            y = (u * sa + v * ca) * cell + ch / 2
            if 0 <= x < cw and 0 <= y < ch:
                k = tb[int(y), int(x)]
                if k > .03:
                    r = cell * .72 * math.sqrt(k)
                    d.ellipse((x - r, y - r, x + r, y + r), fill=INK)
    msk = render(svg_open() + mark("#000000", 1) + "</svg>", "RGBA").split()[-1]
    img.paste(Image.new("RGB", img.size, INK), (0, 0), msk.point(lambda a: int(a * .35)))
    finish(img, "demo-d-halftone.png")


if __name__ == "__main__":
    times = {}
    for name, fn in (("a", demo_a), ("b", demo_b), ("c", demo_c), ("d", demo_d)):
        t0 = time.perf_counter()
        fn()
        times[name] = round(time.perf_counter() - t0, 2)
    (HERE / "times.json").write_text(json.dumps(times, indent=2))
    print(times)
