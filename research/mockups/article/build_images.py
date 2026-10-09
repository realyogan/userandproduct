"""Renders the article hero (light and dark, 1200x675) and the three Related thumbnails (600x338)
into img/ from inline SVG compositions, with resvg. No stock imagery, no text in the art.
Run: python build_images.py
"""
from pathlib import Path
import resvg_py

HERE = Path(__file__).resolve().parent
OUT = HERE / "img"

THEMES = {
    "light": dict(bg="#FFFFFF", page="#FFFFFF", page2="#F1F1F3", edge="#D9D9DE", ink="#0B0B0C",
                  line="#D4D4DA", soft="#E9E9ED", sig="#2B46A0", wash="#DCE2F5"),
    "dark": dict(bg="#0B0B0C", page="#141416", page2="#1B1B1F", edge="#2C2C32", ink="#F1EEE7",
                 line="#3A3A42", soft="#26262B", sig="#8EA2FF", wash="#26305A"),
}


def tile(cx, cy, size, fill, rx=None):
    """A square turned 45 degrees: the brand mark's tile."""
    r = rx if rx is not None else size * 0.14
    return (f'<rect x="{cx - size / 2:.1f}" y="{cy - size / 2:.1f}" width="{size}" height="{size}" rx="{r:.1f}" '
            f'fill="{fill}" transform="rotate(45 {cx} {cy})"/>')


def hero(t):
    c = THEMES[t]
    out = [f'<rect width="1200" height="675" fill="{c["bg"]}"/>']
    # second sheet behind, then the PRD page; it runs off the bottom edge
    out.append(f'<rect x="372" y="96" width="520" height="640" rx="14" fill="{c["page2"]}" stroke="{c["edge"]}" stroke-width="2"/>')
    out.append(f'<rect x="340" y="64" width="520" height="660" rx="14" fill="{c["page"]}" stroke="{c["edge"]}" stroke-width="2"/>')
    # title and standfirst
    out.append(f'<rect x="388" y="112" width="290" height="22" rx="5" fill="{c["ink"]}"/>')
    out.append(f'<rect x="388" y="150" width="400" height="10" rx="5" fill="{c["line"]}"/>')
    out.append(f'<rect x="388" y="170" width="330" height="10" rx="5" fill="{c["line"]}"/>')
    out.append(f'<rect x="388" y="204" width="424" height="2" fill="{c["soft"]}"/>')
    # the twelve questions; 7, 9 and 12 carry the weight, so they get the blue
    lengths = [300, 250, 330, 210, 360, 240, 300, 270, 340, 220, 310, 260]
    y = 236
    for i, ln in enumerate(lengths, 1):
        key = i in (7, 9, 12)
        out.append(tile(398, y, 10 if key else 8, c["sig"] if key else c["line"]))
        out.append(f'<rect x="418" y="{y - 5}" width="{ln}" height="10" rx="5" fill="{c["wash"] if key else c["soft"]}"/>')
        if key:
            out.append(f'<rect x="418" y="{y - 5}" width="{round(ln * 0.38)}" height="10" rx="5" fill="{c["sig"]}"/>')
        y += 34
    # the mark's four tiles, large, to the right of the page; one small tile to the left
    out.append(tile(992, 300, 84, c["sig"]))
    out.append(tile(1064, 372, 84, c["sig"]))
    out.append(tile(992, 444, 84, c["sig"]))
    out.append(tile(920, 372, 46, c["sig"]))
    out.append(tile(214, 520, 46, c["sig"]))
    out.append(tile(262, 472, 22, c["line"]))
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 675">{"".join(out)}</svg>'


def thumb_stories(c):
    o = [f'<rect width="600" height="338" fill="{c["bg"]}"/>']
    for i, (x, y) in enumerate([(150, 70), (176, 124), (202, 178)]):
        o.append(f'<rect x="{x}" y="{y}" width="250" height="96" rx="10" fill="{c["page"]}" stroke="{c["edge"]}" stroke-width="2"/>')
        o.append(tile(x + 34, y + 34, 16, c["sig"] if i == 2 else c["line"]))
        o.append(f'<rect x="{x + 58}" y="{y + 28}" width="150" height="12" rx="6" fill="{c["ink"] if i == 2 else c["soft"]}"/>')
        o.append(f'<rect x="{x + 58}" y="{y + 52}" width="110" height="10" rx="5" fill="{c["soft"]}"/>')
    return o


def thumb_plan(c):
    o = [f'<rect width="600" height="338" fill="{c["bg"]}"/>']
    filled = {0, 1, 4, 6, 9}
    for i in range(10):
        col, row = i % 5, i // 5
        x, y = 140 + col * 66, 104 + row * 76
        on = i in filled
        o.append(f'<rect x="{x}" y="{y}" width="52" height="60" rx="8" fill="{c["sig"] if on else c["page"]}" stroke="{c["sig"] if on else c["edge"]}" stroke-width="2"/>')
    o.append(f'<rect x="140" y="74" width="120" height="10" rx="5" fill="{c["ink"]}"/>')
    return o


def thumb_users(c):
    o = [f'<rect width="600" height="338" fill="{c["bg"]}"/>']
    o.append(f'<rect x="110" y="236" width="380" height="2" fill="{c["line"]}"/>')
    for i in range(5):
        x = 150 + i * 75
        col = c["sig"] if i < 5 else c["line"]
        fill = col if i == 4 else c["soft"]
        o.append(f'<circle cx="{x}" cy="148" r="20" fill="{fill}"/>')
        o.append(f'<path d="M{x - 30} 222c4-24 16-34 30-34s26 10 30 34Z" fill="{fill}"/>')
    o.append(tile(150 + 4 * 75, 274, 16, c["sig"]))
    return o


def save(svg, name, w, h):
    data = resvg_py.svg_to_bytes(svg_string=svg, width=w, height=h)
    (OUT / name).write_bytes(bytes(data))
    print("wrote", name)


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for t in THEMES:
        save(hero(t), f"hero-prd-{t}.png", 1200, 675)
    c = THEMES["light"]
    for name, fn in (("related-user-stories.png", thumb_stories), ("related-discovery-plan.png", thumb_plan),
                     ("related-usability-test.png", thumb_users)):
        save(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 338">{"".join(fn(c))}</svg>', name, 600, 338)
    cd = THEMES["dark"]
    for name, fn in (("related-user-stories-dark.png", thumb_stories), ("related-discovery-plan-dark.png", thumb_plan),
                     ("related-usability-test-dark.png", thumb_users)):
        save(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 338">{"".join(fn(cd))}</svg>', name, 600, 338)
