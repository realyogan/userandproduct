"""Contact sheet of every figure at 200px, its favicon drawing at 32 and 16px, and 16px enlarged (scratch check)."""
import io, sys
from PIL import Image, ImageDraw
import resvg_py
from figs7 import FIG
from geom7 import svg, P, bounds

COL = {'o': '#141414', 'a': '#B3141C', 'm': '#14284B'}

def sq(frags, m=2):
    bs = [bounds(d) for d, _ in frags]
    x0 = min(b[0] for b in bs); y0 = min(b[1] for b in bs); x1 = max(b[2] for b in bs); y1 = max(b[3] for b in bs)
    s = max(x1 - x0, y1 - y0) + 2 * m
    return ((x0 + x1) / 2 - s / 2, (y0 + y1) / 2 - s / 2, s, s)

def png(frags, size, col=COL):
    t = svg(sq(frags), ''.join(P(d, col[r]) for d, r in frags), 'x')
    return Image.open(io.BytesIO(bytes(resvg_py.svg_to_bytes(svg_string=t, width=size, height=size)))).convert('RGBA')

keys = sys.argv[2:] or list(FIG)
cols = 3
cw, rh = 200 + 30 + 32 + 20 + 16 + 20 + 96 + 30, 250
rows = (len(keys) + cols - 1) // cols
img = Image.new('RGB', (cw * cols, rh * rows), 'white')
dr = ImageDraw.Draw(img)
for i, k in enumerate(keys):
    x, y = (i % cols) * cw + 10, (i // cols) * rh + 30
    dr.text((x, y - 22), k, fill='black')
    im = png(FIG[k](), 200); img.paste(im, (x, y), im)
    fav = FIG[k](True)
    xx = x + 230
    for s in (32, 16):
        t = png(fav, s); img.paste(t, (xx, y + 80), t)
        if s == 16:
            z = t.resize((96, 96), Image.NEAREST); img.paste(z, (xx + 36, y + 50), z)
        xx += s + 20
img.save(sys.argv[1])
