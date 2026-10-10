"""Explainer gallery: twelve diagram types a product or UX article needs, drawn by tools/illustration.py across the eight
Printables tints (so some tints repeat). Writes option-1/img/explainers/ex-<slug>.png (1200 x 675) and option-1/build/explainers.html.
Run: python explainers.py
"""
import sys
from pathlib import Path
from xml.sax.saxutils import escape

HERE = Path(__file__).resolve().parent   # option-1/build/
sys.path.insert(0, str(HERE.parents[1] / "tools"))   # research/mockups/tools/
from illustration import illustration, png, palette_for, TINTS, CYCLE, contrast, label_on, INK  # noqa: E402


def timeline():
    names = ["kickoff", "interviews", "prototype", "beta", "launch"]
    weeks = ["week 1", "week 3", "week 6", "week 9", "week 12"]
    it = [{"type": "hrule", "y": 400, "x1": 120, "x2": 1080}]
    for i, (n, w) in enumerate(zip(names, weeks)):
        x = 160 + i * 220
        it += [{"type": "rule", "x": x, "y1": 316, "y2": 400},
               {"type": "box", "x": x - 90, "y": 260, "w": 180, "h": 56, "label": n, "anchor": "middle", "tint": "a" if n == "launch" else None},
               {"type": "dot", "x": x, "y": 400, "r": 9, "tint": "a" if n == "launch" else None},
               {"type": "text", "x": x, "y": 450, "text": w, "anchor": "middle"}]
    return it


def flow():
    labels = ["visit", "sign up", "onboard", "activate"]
    it = []
    for i, n in enumerate(labels):
        x = 110 + i * 240
        it.append({"type": "box", "x": x, "y": 220, "w": 190, "h": 60, "label": n, "tint": "a" if n == "activate" else None})
        if i < 3:
            it.append({"type": "arrow", "x1": x + 192, "y1": 250, "x2": x + 238, "y2": 250})
    it += [{"type": "arrow", "x1": 685, "y1": 282, "x2": 685, "y2": 408},
           {"type": "box", "x": 590, "y": 410, "w": 190, "h": 60, "label": "drop off", "tint": "b"},
           {"type": "text", "x": 800, "y": 446, "text": "38% leave here"}]
    return it


def before_after():
    it = [{"type": "text", "x": 150, "y": 130, "text": "before", "size": 20, "muted": False},
          {"type": "text", "x": 690, "y": 130, "text": "after", "size": 20, "muted": False}]
    for i, n in enumerate(["market sizing", "persona poster", "competitor grid", "every edge case", "decisions?"]):
        it.append({"type": "box", "x": 150, "y": 160 + i * 68, "w": 380, "h": 54, "label": n, "tint": "b" if n == "decisions?" else None})
    it += [{"type": "box", "x": 690, "y": 160, "w": 380, "h": 54, "label": "decisions", "tint": "a"},
           {"type": "box", "x": 690, "y": 228, "w": 380, "h": 54, "label": "edge states that matter"},
           {"type": "arrow", "x1": 548, "y1": 300, "x2": 672, "y2": 300},
           {"type": "text", "x": 690, "y": 330, "text": "4 screens instead of 11"}]
    return it


def matrix():
    return [{"type": "rule", "x": 600, "y1": 120, "y2": 550}, {"type": "hrule", "y": 335, "x1": 200, "x2": 1000},
            {"type": "text", "x": 600, "y": 100, "text": "high impact", "anchor": "middle"},
            {"type": "text", "x": 600, "y": 585, "text": "low impact", "anchor": "middle"},
            {"type": "text", "x": 185, "y": 341, "text": "less effort", "anchor": "end"},
            {"type": "text", "x": 1015, "y": 341, "text": "more effort"},
            {"type": "box", "x": 260, "y": 180, "w": 260, "h": 58, "label": "quick wins", "tint": "a"},
            {"type": "box", "x": 680, "y": 180, "w": 260, "h": 58, "label": "big bets"},
            {"type": "box", "x": 260, "y": 430, "w": 260, "h": 58, "label": "fill-ins"},
            {"type": "box", "x": 680, "y": 430, "w": 260, "h": 58, "label": "money pits", "tint": "b"}]


def steps():
    it = []
    names = ["1 frame", "2 interview", "3 synthesize", "4 decide", "5 ship"]
    for i, n in enumerate(names):
        x, y = 110 + i * 200, 130 + i * 82
        it.append({"type": "box", "x": x, "y": y, "w": 180, "h": 56, "label": n, "tint": "a" if i == 4 else None})
        if i < 4:
            it.append({"type": "arrow", "x1": x + 182, "y1": y + 30, "x2": x + 210, "y2": y + 80})
    return it


def funnel():
    rows = [("visitors 12,400", 900), ("sign-ups 3,100", 720), ("activated 1,240", 540), ("paying 310", 360)]
    return [{"type": "box", "x": 600 - w / 2, "y": 120 + i * 98, "w": w, "h": 72, "label": n, "anchor": "middle",
             "tint": "a" if i == 3 else None} for i, (n, w) in enumerate(rows)]


def bars():
    data = [("saved filters", 72), ("exports", 48), ("alerts", 35), ("sharing", 22), ("themes", 9)]
    it = []
    for i, (n, v) in enumerate(data):
        y = 130 + i * 86
        it += [{"type": "text", "x": 300, "y": y + 32, "text": n, "anchor": "end", "size": 19, "muted": False},
               {"type": "box", "x": 320, "y": y, "w": v * 9, "h": 50, "tint": "a" if i == 0 else None},
               {"type": "text", "x": 332 + v * 9, "y": y + 32, "text": f"{v}%"}]
    return it


def line_chart():
    vals = [10, 12, 16, 20, 26, 31, 36, 41]
    months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug"]
    pts = [(200 + i * 120, 540 - v * 7) for i, v in enumerate(vals)]
    it = [{"type": "rule", "x": 160, "y1": 110, "y2": 540}, {"type": "hrule", "y": 540, "x1": 160, "x2": 1080},
          {"type": "hrule", "y": 260, "x1": 160, "x2": 1080, "dash": True},
          {"type": "text", "x": 176, "y": 245, "text": "target 40%", "muted": False},
          {"type": "polyline", "points": pts, "tint": "a"},
          {"type": "dot", "x": pts[-1][0], "y": pts[-1][1], "r": 9, "tint": "a"}]
    it += [{"type": "text", "x": x, "y": 575, "text": m, "anchor": "middle", "size": 16} for (x, _), m in zip(pts, months)]
    it += [{"type": "text", "x": 145, "y": 545, "text": "0%", "anchor": "end", "size": 16},
           {"type": "text", "x": 145, "y": 370, "text": "25%", "anchor": "end", "size": 16},
           {"type": "text", "x": 145, "y": 195, "text": "50%", "anchor": "end", "size": 16}]
    return it


def stack():
    rows = [("interface", "changes weekly"), ("API", "the contract"), ("services", "owned by teams"), ("data", "source of truth")]
    it = []
    for i, (n, note) in enumerate(rows):
        y = 130 + i * 100
        it += [{"type": "box", "x": 220, "y": y, "w": 700, "h": 80, "label": n, "anchor": "middle", "tint": "a" if n == "API" else None},
               {"type": "text", "x": 944, "y": y + 46, "text": note}]
    return it


def checklist():
    items = ["problem in one sentence", "out of scope listed", "empty states named", "acceptance lines testable",
             "open questions owned", "design file linked"]
    it = []
    for i, n in enumerate(items):
        y = 120 + i * 72
        done = i < 4
        it.append({"type": "box", "x": 220, "y": y, "w": 40, "h": 40, "tint": "a" if done else None})
        if done:
            it.append({"type": "polyline", "points": [(229, y + 21), (237, y + 30), (252, y + 11)], "on": "a"})
        it.append({"type": "text", "x": 284, "y": y + 27, "text": n, "size": 20, "muted": not done})
    it.append({"type": "text", "x": 860, "y": 147, "text": "4 of 6 ready", "muted": False})
    return it


def cycle():
    return [{"type": "box", "x": 490, "y": 110, "w": 220, "h": 60, "label": "build", "anchor": "middle"},
            {"type": "box", "x": 850, "y": 310, "w": 220, "h": 60, "label": "measure", "anchor": "middle"},
            {"type": "box", "x": 490, "y": 500, "w": 220, "h": 60, "label": "learn", "anchor": "middle", "tint": "a"},
            {"type": "box", "x": 130, "y": 310, "w": 220, "h": 60, "label": "decide", "anchor": "middle"},
            {"type": "arrow", "x1": 712, "y1": 150, "x2": 900, "y2": 306},
            {"type": "arrow", "x1": 960, "y1": 374, "x2": 714, "y2": 520},
            {"type": "arrow", "x1": 488, "y1": 530, "x2": 240, "y2": 374},
            {"type": "arrow", "x1": 240, "y1": 306, "x2": 488, "y2": 150}]


def grid():
    head = ["feature", "reach", "effort", "score"]
    rows = [["saved filters", "900", "3", "300"], ["exports", "400", "2", "200"], ["alerts", "600", "5", "120"], ["themes", "200", "1", "200"]]
    xs, ws = [150, 450, 640, 830], [290, 180, 180, 220]
    it = [{"type": "box", "x": x, "y": 130, "w": w, "h": 56, "label": h, "tint": "b"} for x, w, h in zip(xs, ws, head)]
    for r, row in enumerate(rows):
        for c, (x, w) in enumerate(zip(xs, ws)):
            it.append({"type": "box", "x": x, "y": 200 + r * 66, "w": w, "h": 56, "label": row[c],
                       "tint": "a" if (r == 0 and c == 3) else None})
    return it


GALLERY = [
    ("timeline", "Timeline", "teal", timeline, "Milestones on a line from kickoff in week 1 to launch in week 12, launch highlighted."),
    ("flow", "Flow with arrows", "yellow", flow, "Visit, sign up, onboard and activate joined by arrows, with a branch from onboard to drop off: 38% leave here."),
    ("before-after", "Before and after", "pink", before_after, "Before: five sections ending in a question mark over decisions. After: decisions and the edge states that matter, 4 screens instead of 11."),
    ("matrix", "2 x 2 matrix", "blue", matrix, "Impact against effort: quick wins top left, big bets top right, fill-ins bottom left, money pits bottom right."),
    ("steps", "Numbered steps", "green", steps, "Five steps stepping down to the right: frame, interview, synthesize, decide, ship."),
    ("funnel", "Funnel", "purple", funnel, "Visitors 12,400, sign-ups 3,100, activated 1,240, paying 310."),
    ("bars", "Bar comparison", "peach", bars, "Share of users per feature: saved filters 72%, exports 48%, alerts 35%, sharing 22%, themes 9%."),
    ("line", "Line chart with a target", "slate", line_chart, "Monthly share rising from 10% in January to 41% in August, crossing the dashed 40% target."),
    ("stack", "Stack of layers", "teal", stack, "Four layers from interface to data, API highlighted as the contract."),
    ("checklist", "Checklist", "yellow", checklist, "Six PRD checks, four ticked: problem in one sentence, out of scope listed, empty states named, acceptance lines testable."),
    ("cycle", "Cycle", "pink", cycle, "Build, measure, learn, decide in a loop of arrows, learn highlighted."),
    ("grid", "Table grid", "blue", grid, "A scoring table with reach, effort and score for four features; saved filters scores highest at 300."),
]


def build():
    out = HERE.parent / "img" / "explainers"
    out.mkdir(parents=True, exist_ok=True)
    cards = []
    for slug, name, tint, fn, alt in GALLERY:
        pal = palette_for(tint)
        svg = illustration(fn(), tint=tint, uid=f"ex-{slug}", title=name, desc=alt)
        png(svg, out / f"ex-{slug}.png", 1200)
        src = f"../img/explainers/ex-{slug}.png"
        cards.append(f"""  <li class="ex" id="ex-{slug}">
    <h2>{escape(name)}</h2>
    <div class="pair">
      <div class="on-white"><img src="{src}" width="600" height="338" alt="{escape(alt)}" loading="lazy" decoding="async"></div>
      <div class="on-black"><img src="{src}" width="600" height="338" alt="{escape(alt)} (on the near-black page)" loading="lazy" decoding="async"></div>
    </div>
    <p class="cap">Tint {tint} {pal["bg"]}, ink {pal["ink"]} ({contrast(pal["ink"], pal["bg"]):.1f}:1), muted {pal["muted"]} ({contrast(pal["muted"], pal["bg"]):.1f}:1). Left on the white page, right on the near-black page; the same file.</p>
  </li>""")
        print("wrote", f"ex-{slug}.png")
    sw = []
    for t, hexv in TINTS.items():
        p = palette_for(t)
        role = "rotates" if t in CYCLE else "reserved"
        sw.append(f'''<li><div class="sw" style="background:{hexv}"><span style="background:{p["a"]};color:{label_on(p["a"])}">A {p["a"]}</span><span style="background:{p["b"]};color:{label_on(p["b"])}">B {p["b"]}</span></div>
      <p><b>{t}</b> {hexv}<br>ink {INK} {contrast(INK, hexv):.1f}:1, muted {p["muted"]} {contrast(p["muted"], hexv):.1f}:1<br>{role}</p></li>''')
    swatches = "\n    ".join(sw)
    html = f"""<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Explainer Gallery | userandproduct</title>
<meta name="description" content="Twelve diagram types drawn by the illustration generator, each on a different background, shown on the white and the near-black page.">
<meta name="robots" content="noindex">
<link rel="icon" href="../assets/favicon/favicon.ico" sizes="48x48">
<link rel="icon" href="../assets/favicon/favicon.svg" type="image/svg+xml">
<script>try{{var t=localStorage.getItem("uap-theme");if(t==="dark"||t==="light"){{document.documentElement.setAttribute("data-theme",t)}}}}catch(e){{}}</script>
<link rel="stylesheet" href="../css/mockup.css">
<script src="../js/mockup.js" defer></script>
<style>
  .wrap{{max-width:calc(1260px + 2 * var(--gutter));margin:0 auto;padding:0 var(--gutter)}}
  .intro{{padding:var(--s7) 0 var(--s5)}}
  .intro h1{{font-size:clamp(34px,5vw,52px);line-height:1.06;letter-spacing:-.03em}}
  .intro p{{margin-top:var(--s4);max-width:68ch;font:400 var(--fs-body)/1.6 var(--font-ui);color:var(--ink-2)}}
  .exs{{list-style:none;margin:0;padding:0;display:grid;gap:var(--s8)}}
  .ex h2{{font-size:24px;letter-spacing:-.015em}}
  .pair{{display:grid;grid-template-columns:1fr;margin-top:var(--s3);border:1px solid var(--rule);border-radius:8px;overflow:hidden}}
  @media (min-width:900px){{.pair{{grid-template-columns:1fr 1fr}}}}
  .pair>div{{padding:24px;display:flex;justify-content:center}}
  .pair img{{display:block;width:100%;max-width:600px;height:auto;border-radius:6px}}
  .on-white{{background:#FFFFFF}} .on-black{{background:#0B0B0C}}
  .cap{{margin-top:var(--s3);font:400 var(--fs-meta)/1.5 var(--font-ui);color:var(--ink-3)}}
  .swatches{{list-style:none;margin:0 0 var(--s8);padding:0;display:grid;gap:var(--s4);grid-template-columns:repeat(auto-fill,minmax(min(100%,260px),1fr))}}
  .sw{{display:flex;flex-direction:column;justify-content:flex-end;gap:6px;height:120px;padding:12px;border-radius:6px;border:1px solid var(--rule);
    background-image:radial-gradient(rgba(29,27,22,.13) 1px,transparent 1.5px)!important;background-size:12px 12px!important}}
  .sw span{{align-self:flex-start;font:500 12px/1 var(--font-mono);padding:6px 8px;border:1.5px solid #1D1B16;border-radius:4px}}
  .swatches p{{margin-top:var(--s2);font:400 var(--fs-meta)/1.5 var(--font-ui);color:var(--ink-2)}}
  .swatches b{{color:var(--ink);font-weight:600}}
</style>
</head>
<body>
<a class="skip" href="#content">Skip to the gallery</a>
<header class="site-head">
  <div class="site-head__in">
    <a class="logo" href="variants/index.html" aria-label="Back to the article variants">
      <img class="l-light" src="../assets/logo/lockup-light.svg" alt="userandproduct" width="236" height="30">
      <img class="l-dark" src="../assets/logo/lockup-dark.svg" alt="userandproduct" width="236" height="30">
    </a>
    <a href="variants/index.html" style="margin-left:auto;font:500 var(--fs-ui)/1 var(--font-ui)">Article variants</a>
    <button class="theme-toggle" type="button" data-theme-toggle aria-label="Switch theme"><svg class="i-moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" d="M20.3 14.6A8.5 8.5 0 0 1 9.4 3.7a8.5 8.5 0 1 0 10.9 10.9Z"/></svg><svg class="i-sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.5" fill="currentColor"/><g stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 2v2.5M12 19.5V22M2 12h2.5M19.5 12H22M4.9 4.9l1.8 1.8M17.3 17.3l1.8 1.8M4.9 19.1l1.8-1.8M17.3 6.7l1.8-1.8"/></g></svg></button>
  </div>
</header>
<main id="content" class="wrap">
  <section class="intro" aria-labelledby="page-h">
    <h1 id="page-h">Explainer gallery</h1>
    <p>Twelve diagram types a product or UX article needs, drawn by <code>tools/illustration.py</code> on the eight pastel tints from the Printables site, with its dark dot grid and dark ink. In an article every explainer shares the article's tint (by publish order, like the Printables tiles); here the types run across all eight, so some tints repeat. Each image is one PNG, shown on the white page and on the near-black page. The swatches show each tint with its two highlight colours (A and B) and the label contrast. Rules: <a href="../../illustration-rules.md">illustration-rules.md</a>; source: <a href="../../references/printables-tints.md">printables-tints.md</a>.</p>
  </section>
  <h2 class="vh" id="sw-h">The eight tints</h2>
  <ul class="swatches" aria-labelledby="sw-h">
    {swatches}
  </ul>
  <ul class="exs">
{chr(10).join(cards)}
  </ul>
</main>
<footer class="site-foot"><div class="site-foot__in"><div class="legal"><span>userandproduct mockups</span><a href="variants/index.html">Article variants</a><a href="../../final-logo/brand-sheet.html">Brand sheet</a></div></div></footer>
</body>
</html>
"""
    (HERE / "explainers.html").write_text(html, encoding="utf-8", newline="\n")
    print("wrote explainers.html")


if __name__ == "__main__":
    build()
