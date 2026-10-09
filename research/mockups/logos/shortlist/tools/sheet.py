"""Scratch contact sheet: marks at 200px, then 32px and 16px, and 16px enlarged 6x."""
import io, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import resvg_py
from PIL import Image
from geom import svg, P


def png(d, size, fill='#141414', bg=None):
    body = (P('M-1 -1H101V101H-1Z', bg) if bg else '') + P(d, fill)
    t = svg((-1, -1, 102, 102), body, 'x')
    return Image.open(io.BytesIO(bytes(resvg_py.svg_to_bytes(svg_string=t, width=size, height=size)))).convert('RGBA')


def sheet(rows, path):
    W, rh = 200 + 40 + 32 + 30 + 16 + 30 + 96 + 30 + 96 + 30, 230
    img = Image.new('RGB', (W, rh * len(rows)), 'white')
    for i, (d, fd) in enumerate(rows):
        y = i * rh + 15
        b = png(d, 200); img.paste(b, (15, y), b)
        x = 255
        for sz in (32, 16):
            t = png(fd, sz, bg='#ffffff'); img.paste(t, (x, y + 80), t); x += sz + 30
        z = png(fd, 16, bg='#ffffff').resize((96, 96), Image.NEAREST); img.paste(z, (x, y + 50)); x += 126
        z = png(fd, 16, fill='#f1eee7', bg='#141414').resize((96, 96), Image.NEAREST); img.paste(z, (x, y + 50))
    img.save(path)
