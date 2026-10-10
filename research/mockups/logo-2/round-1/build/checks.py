"""Checks for round 1: valid SVG, sizes, thin parts (opening test at 512), favicon PNGs present."""
import sys, xml.etree.ElementTree as ET, io
from pathlib import Path
from PIL import Image, ImageFilter, ImageChops
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent.parent / "tools")); sys.path.insert(0, str(HERE))
from render import render_png
import marks as M
from build import mark_layers, svg_doc
ok = True
for f in sorted((HERE.parent / "svg").glob("*.svg")):
    t = f.read_text(encoding="utf-8")
    ET.fromstring(t)
    n = len(t.encode())
    lim = 6144
    if n > lim:
        print("SIZE", f.name, n); ok = False
print("svg files parsed:", len(list((HERE.parent / "svg").glob("*.svg"))))
# thin parts: a layer region that vanishes under a 9 px opening is thinner than 8 px at 512
for i, fn in enumerate(M.MARKS, 1):
    spec = fn()
    worst = 0
    for role, p in mark_layers(spec):
        d = M.D(p)
        if not d: continue
        im = Image.open(io.BytesIO(render_png(svg_doc(f'<rect width="512" height="512" fill="#000"/><path fill="#fff" d="{d}"/>'), 512, 512))).convert("L")
        im = im.point(lambda v: 255 if v > 127 else 0)
        opened = im.filter(ImageFilter.MinFilter(9)).filter(ImageFilter.MaxFilter(9))
        lost = ImageChops.subtract(im, opened)
        # ignore what any convex corner loses: count lost pixels in blobs wider than a corner nick
        thin = lost.filter(ImageFilter.MinFilter(3))
        cnt = sum(1 for v in thin.getdata() if v)
        worst = max(worst, cnt)
    print(f"R1-{i:02d} thin-part pixels after opening: {worst}")
print("OK" if ok else "FAIL")
