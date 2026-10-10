import sys, io
sys.path.insert(0, '.')
import resvg_py
from PIL import Image
import marks
from geo import d_of
COL = {'c': '#2B46A0', 'a': '#FFFFFF', 'b': '#8EA2FF', 'f': '#C9D3FF'}
FREE = {'a': '#2B46A0', 'b': '#4D6CF0', 'f': '#9DB2FF'}
ids = sys.argv[2].split(',')
sheet = Image.new('RGB', (len(ids) * 420, 420), 'white')
for i, n in enumerate(ids):
    cont, layers = getattr(marks, 'm' + n)()
    pal = COL if cont else FREE
    body = ''.join('<path fill="%s" d="%s"/>' % (pal[r], d_of(p)) for r, p in layers)
    svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">%s</svg>' % body
    im = Image.open(io.BytesIO(bytes(resvg_py.svg_to_bytes(svg_string=svg, width=400, height=400)))).convert('RGBA')
    sheet.paste(im, (i * 420 + 10, 10), im)
sheet.save(sys.argv[1])
