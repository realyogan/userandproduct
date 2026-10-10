import sys, io
sys.path.insert(0, '.')
import resvg_py
from PIL import Image
from marks import MARKS
from geo import d_of
COL = {'c': '#2B46A0', 'a': '#FFFFFF', 'b': '#8EA2FF', 'f': '#C9D3FF'}
FREE = {'a': '#2B46A0', 'b': '#4D6CF0', 'f': '#9DB2FF'}
sheet = Image.new('RGB', (10 * 200, 400), 'white')
for i, m in enumerate(MARKS):
    cont, layers = m()
    pal = COL if cont else FREE
    body = ''.join('<path fill="%s" d="%s"/>' % (pal[r], d_of(p)) for r, p in layers)
    svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">%s</svg>' % body
    for j, s in enumerate((180, 32)):
        im = Image.open(io.BytesIO(bytes(resvg_py.svg_to_bytes(svg_string=svg, width=s, height=s)))).convert('RGBA')
        sheet.paste(im, (i * 200 + 10, 10 + j * 200), im)
sheet.save(sys.argv[1])
