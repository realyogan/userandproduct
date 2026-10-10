"""Explainer gallery: fourteen figures, twelve diagram and chart types plus an analogy scene and an object, drawn by
tools/illustration.py across the eight Printables tints (so some tints repeat). Writes option-1/img/explainers/ex-<slug>.png (1200 x 675) and option-1/build/explainers.html.
Run: python explainers.py
"""
import sys
from pathlib import Path
from xml.sax.saxutils import escape

HERE = Path(__file__).resolve().parent   # option-1/build/
sys.path.insert(0, str(HERE.parents[1] / "tools"))   # research/mockups/tools/
from illustration import illustration, png, palette_for, TINTS, CYCLE, contrast, label_on, INK, check_contrast  # noqa: E402


def timeline():
    names = ["kickoff", "interviews", "prototype", "beta", "launch"]
    weeks = ["week 1", "week 3", "week 6", "week 9", "week 12"]
    it = [{"type": "hrule", "y": 420, "x1": 96, "x2": 1104}]
    for i, (n, w) in enumerate(zip(names, weeks)):
        x = 160 + i * 220
        hi = n == "launch"
        it += [{"type": "rule", "x": x, "y1": 326, "y2": 420},
               {"type": "box", "x": x - 92, "y": 262, "w": 184, "h": 64, "label": n, "anchor": "middle", "tint": "a" if hi else None},
               {"type": "dot", "x": x, "y": 420, "r": 10, "tint": "a" if hi else None},
               {"type": "text", "x": x, "y": 474, "text": w, "anchor": "middle"}]
    return it


def flow():
    labels = ["visit", "sign up", "onboard", "activate"]
    it = []
    for i, n in enumerate(labels):
        x = 96 + i * 260
        it.append({"type": "box", "x": x, "y": 200, "w": 200, "h": 68, "label": n, "anchor": "middle", "tint": "a" if n == "activate" else None})
        if i < 3:
            it.append({"type": "arrow", "x1": x + 202, "y1": 234, "x2": x + 258, "y2": 234})
    it += [{"type": "arrow", "x1": 716, "y1": 270, "x2": 716, "y2": 396},
           {"type": "box", "x": 616, "y": 398, "w": 200, "h": 68, "label": "drop off", "anchor": "middle", "tint": "b"},
           {"type": "text", "x": 840, "y": 442, "text": "38% leave here", "muted": False}]
    return it


def before_after():
    it = [{"type": "text", "x": 110, "y": 120, "text": "before", "role": "label", "muted": False, "weight": "semibold"},
          {"type": "text", "x": 660, "y": 120, "text": "after", "role": "label", "muted": False, "weight": "semibold"}]
    for i, n in enumerate(["market sizing", "persona poster", "competitor grid", "every edge case", "decisions?"]):
        it.append({"type": "box", "x": 110, "y": 148 + i * 80, "w": 400, "h": 64, "label": n, "tint": "b" if n == "decisions?" else None})
    it += [{"type": "box", "x": 660, "y": 148, "w": 400, "h": 64, "label": "decisions", "tint": "a"},
           {"type": "box", "x": 660, "y": 228, "w": 400, "h": 64, "label": "edge states that matter"},
           {"type": "arrow", "x1": 526, "y1": 310, "x2": 644, "y2": 310},
           {"type": "text", "x": 660, "y": 350, "text": "4 screens instead of 11"}]
    return it


def matrix():
    return [{"type": "rule", "x": 600, "y1": 128, "y2": 548}, {"type": "hrule", "y": 338, "x1": 236, "x2": 964},
            {"type": "text", "x": 600, "y": 108, "text": "high impact", "anchor": "middle"},
            {"type": "text", "x": 600, "y": 586, "text": "low impact", "anchor": "middle"},
            {"type": "text", "x": 220, "y": 346, "text": "less effort", "anchor": "end"},
            {"type": "text", "x": 980, "y": 346, "text": "more effort"},
            {"type": "box", "x": 268, "y": 176, "w": 280, "h": 72, "label": "quick wins", "anchor": "middle", "tint": "a"},
            {"type": "box", "x": 652, "y": 176, "w": 280, "h": 72, "label": "big bets", "anchor": "middle"},
            {"type": "box", "x": 268, "y": 428, "w": 280, "h": 72, "label": "fill-ins", "anchor": "middle"},
            {"type": "box", "x": 652, "y": 428, "w": 280, "h": 72, "label": "money pits", "anchor": "middle", "tint": "b"}]


def steps():
    names = ["frame", "interview", "synthesize", "decide", "ship"]
    notes = ["one question", "eight people", "find patterns", "one memo", "a small slice"]
    it = [{"type": "hrule", "y": 280, "x1": 160, "x2": 1040}]
    for i, (n, note) in enumerate(zip(names, notes)):
        x = 160 + i * 220
        it += [{"type": "badge", "x": x, "y": 280, "n": i + 1, "r": 34, "tint": "b" if i == 4 else "card"},
               {"type": "text", "x": x, "y": 370, "text": n, "anchor": "middle", "role": "label", "muted": False},
               {"type": "text", "x": x, "y": 414, "text": note, "anchor": "middle"}]
    return it


def funnel():
    rows = [("visitors 12,400", 900), ("sign-ups 3,100", 720), ("activated 1,240", 540), ("paying 310", 360)]
    return [{"type": "box", "x": 600 - w / 2, "y": 112 + i * 100, "w": w, "h": 76, "label": n, "anchor": "middle",
             "tint": "a" if i == 3 else None} for i, (n, w) in enumerate(rows)]


def bars():
    data = [("saved filters", 72), ("exports", 48), ("alerts", 35), ("sharing", 22), ("themes", 9)]
    it = []
    for i, (n, v) in enumerate(data):
        y = 116 + i * 90
        it += [{"type": "text", "x": 300, "y": y + 38, "text": n, "anchor": "end", "role": "label", "muted": False},
               {"type": "box", "x": 320, "y": y, "w": v * 9, "h": 56, "tint": "a" if i == 0 else None},
               {"type": "text", "x": 336 + v * 9, "y": y + 37, "text": f"{v}%"}]
    return it


def line_chart():
    vals = [10, 12, 16, 20, 26, 31, 36, 41]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"]
    pts = [(220 + i * 115, 530 - v * 7) for i, v in enumerate(vals)]
    it = [{"type": "rule", "x": 170, "y1": 110, "y2": 530}, {"type": "hrule", "y": 530, "x1": 170, "x2": 1080},
          {"type": "hrule", "y": 250, "x1": 170, "x2": 1080, "dash": True},
          {"type": "text", "x": 190, "y": 232, "text": "target 40%", "role": "label", "muted": False},
          {"type": "polyline", "points": pts, "tint": "a"},
          {"type": "dot", "x": pts[-1][0], "y": pts[-1][1], "r": 10, "tint": "a"}]
    it += [{"type": "text", "x": x, "y": 572, "text": m, "anchor": "middle"} for (x, _), m in zip(pts, months)]
    it += [{"type": "text", "x": 150, "y": 538, "text": "0%", "anchor": "end"},
           {"type": "text", "x": 150, "y": 363, "text": "25%", "anchor": "end"},
           {"type": "text", "x": 150, "y": 188, "text": "50%", "anchor": "end"}]
    return it


def stack():
    rows = [("interface", "changes weekly"), ("API", "the contract"), ("services", "owned by teams"), ("data", "source of truth")]
    it = []
    for i, (n, note) in enumerate(rows):
        y = 112 + i * 104
        it += [{"type": "box", "x": 180, "y": y, "w": 680, "h": 84, "label": n, "anchor": "middle", "tint": "a" if n == "API" else None},
               {"type": "text", "x": 888, "y": y + 51, "text": note}]
    return it


def checklist():
    items = ["problem in one sentence", "out of scope listed", "empty states named", "acceptance lines testable",
             "open questions owned", "design file linked"]
    it = []
    for i, n in enumerate(items):
        y = 104 + i * 78
        done = i < 4
        it.append({"type": "box", "x": 180, "y": y, "w": 46, "h": 46, "tint": "a" if done else None})
        if done:
            it.append({"type": "polyline", "points": [(190, y + 24), (199, y + 34), (216, y + 13)], "on": "a"})
        it.append({"type": "text", "x": 252, "y": y + 33, "text": n, "role": "label", "muted": not done,
                   "weight": "medium"})
    it.append({"type": "text", "x": 820, "y": 137, "text": "4 of 6 ready", "role": "label", "muted": False, "weight": "semibold"})
    return it


def cycle():
    return [{"type": "box", "x": 480, "y": 100, "w": 240, "h": 68, "label": "build", "anchor": "middle"},
            {"type": "box", "x": 840, "y": 302, "w": 240, "h": 68, "label": "measure", "anchor": "middle"},
            {"type": "box", "x": 480, "y": 500, "w": 240, "h": 68, "label": "learn", "anchor": "middle", "tint": "a"},
            {"type": "box", "x": 120, "y": 302, "w": 240, "h": 68, "label": "decide", "anchor": "middle"},
            {"type": "arrow", "x1": 722, "y1": 140, "x2": 900, "y2": 298},
            {"type": "arrow", "x1": 960, "y1": 374, "x2": 724, "y2": 524},
            {"type": "arrow", "x1": 476, "y1": 536, "x2": 240, "y2": 374},
            {"type": "arrow", "x1": 240, "y1": 298, "x2": 476, "y2": 140}]


def grid():
    head = ["feature", "reach", "effort", "score"]
    rows = [["saved filters", "900", "3", "300"], ["exports", "400", "2", "200"], ["alerts", "600", "5", "120"], ["themes", "200", "1", "200"]]
    xs, ws = [130, 450, 650, 850], [300, 180, 180, 220]
    it = [{"type": "box", "x": x, "y": 112, "w": w, "h": 64, "label": h, "tint": "b", "weight": "semibold"} for x, w, h in zip(xs, ws, head)]
    for r, row in enumerate(rows):
        for c, (x, w) in enumerate(zip(xs, ws)):
            it.append({"type": "box", "x": x, "y": 190 + r * 76, "w": w, "h": 64, "label": row[c],
                       "tint": "a" if (r == 0 and c == 3) else None})
    return it


def _ticket(x, y, w, h, tint=None):
    """An order ticket: a paper slip with a torn, zigzag bottom edge and a punched hole."""
    teeth, t = 10, w / 10
    pts = [(x, y), (x + w, y), (x + w, y + h)]
    for i in range(teeth):
        pts += [(x + w - (i + 0.5) * t, y + h - 14), (x + w - (i + 1) * t, y + h)]
    return [{"type": "polygon", "points": pts, "tint": tint},
            {"type": "circle", "x": x + w / 2, "y": y + 26, "r": 8, "tint": "bg"}]


def ticket():
    """Analogy scene: a PRD is like the order ticket a kitchen cooks from."""
    it = []
    # the vague order: the kitchen has nothing to cook from
    it += _ticket(330, 92, 330, 156)
    it += [{"type": "text", "x": 352, "y": 98 + 92, "text": "something nice", "role": "label", "muted": False},
           {"type": "text", "x": 352, "y": 98 + 128, "text": "soon, please"},
           {"type": "arrow", "x1": 684, "y1": 166, "x2": 770, "y2": 166},
           {"type": "glyph", "name": "pan", "x": 790, "y": 96, "size": 150},
           {"type": "glyph", "name": "question", "x": 834, "y": 74, "size": 70},
           {"type": "text", "x": 790, "y": 238, "text": "nothing to cook", "muted": False}]
    # the clear order: three lines, and the pan is on the flame
    y0 = 300
    it += _ticket(330, y0, 330, 250)
    lines = [("2 pasta, no garlic", "what"), ("table 4", "for whom"), ("out by 8:15", "by when")]
    for i, (line, tag) in enumerate(lines):
        yy = y0 + 92 + i * 52
        it += [{"type": "text", "x": 352, "y": yy, "text": line, "role": "label", "muted": False},
               {"type": "path", "d": f"M{230} {yy - 9}H{318}", "width": 2.5},
               {"type": "text", "x": 216, "y": yy, "text": tag, "anchor": "end"}]
    it += [{"type": "arrow", "x1": 684, "y1": 425, "x2": 770, "y2": 425},
           {"type": "glyph", "name": "pan", "x": 790, "y": 350, "size": 150},
           {"type": "glyph", "name": "flame", "x": 818, "y": 452, "size": 56, "tint": "a"},
           {"type": "glyph", "name": "check", "x": 962, "y": 384, "size": 64, "width": 5},
           {"type": "text", "x": 790, "y": 548, "text": "dinner on time", "muted": False}]
    return it


def prd_sheet():
    """Object: a PRD as one page, its five parts named."""
    x, y, w, h = 440, 72, 320, 528
    fold = 40
    it = [{"type": "polygon", "points": [(x, y), (x + w - fold, y), (x + w, y + fold), (x + w, y + h), (x, y + h)]},
          {"type": "path", "d": f"M{x + w - fold} {y}V{y + fold}H{x + w}"}]
    parts = [("the problem", "left", None), ("who it is for", "right", None), ("what is in", "left", None),
             ("what is out", "right", "a"), ("open questions", "left", None)]
    for i, (name, side, tint) in enumerate(parts):
        sy = y + 64 + i * 92
        it += [{"type": "badge", "x": x + 44, "y": sy + 18, "n": i + 1, "r": 22, "tint": "b" if tint else "card"},
               {"type": "rrect", "x": x + 80, "y": sy + 6, "w": 200, "h": 14, "r": 7, "tint": "a" if tint else "bg", "stroke": False},
               {"type": "rrect", "x": x + 80, "y": sy + 30, "w": 150, "h": 10, "r": 5, "tint": "bg", "stroke": False}]
        if side == "left":
            it += [{"type": "path", "d": f"M{x - 16} {sy + 18}H{x - 76}"},
                   {"type": "text", "x": x - 90, "y": sy + 28, "text": name, "anchor": "end", "role": "label", "muted": False}]
        else:
            it += [{"type": "path", "d": f"M{x + w + 16} {sy + 18}H{x + w + 76}"},
                   {"type": "text", "x": x + w + 90, "y": sy + 28, "text": name, "role": "label", "muted": False}]
    return it


GALLERY = [
    ("timeline", "Timeline", "teal", timeline, "Milestones on a line from kickoff in week 1 to launch in week 12, launch highlighted."),
    ("flow", "Flow with arrows", "yellow", flow, "Visit, sign up, onboard and activate joined by arrows, with a branch from onboard to drop off: 38% leave here."),
    ("before-after", "Before and after", "pink", before_after, "Before: five sections ending in a question mark over decisions. After: decisions and the edge states that matter, 4 screens instead of 11."),
    ("matrix", "2 x 2 matrix", "blue", matrix, "Impact against effort: quick wins top left, big bets top right, fill-ins bottom left, money pits bottom right."),
    ("steps", "Numbered steps", "green", steps, "Five numbered steps on a line: frame (one question), interview (eight people), synthesize (find patterns), decide (one memo), ship (a small slice)."),
    ("funnel", "Funnel", "purple", funnel, "Visitors 12,400, sign-ups 3,100, activated 1,240, paying 310."),
    ("bars", "Bar comparison", "peach", bars, "Share of users per feature: saved filters 72%, exports 48%, alerts 35%, sharing 22%, themes 9%."),
    ("line", "Line chart with a target", "slate", line_chart, "Monthly share rising from 10% in January to 41% in August, crossing the dashed 40% target."),
    ("stack", "Stack of layers", "teal", stack, "Four layers from interface to data, API highlighted as the contract."),
    ("checklist", "Checklist", "yellow", checklist, "Six PRD checks, four ticked: problem in one sentence, out of scope listed, empty states named, acceptance lines testable."),
    ("cycle", "Cycle", "pink", cycle, "Build, measure, learn, decide in a loop of arrows, learn highlighted."),
    ("grid", "Table grid", "blue", grid, "A scoring table with reach, effort and score for four features; saved filters scores highest at 300."),
    ("ticket", "Analogy scene: the order ticket", "green", ticket, "Two order tickets. One says only 'something nice, soon please', and the pan beside it has a question mark: nothing to cook. The other says '2 pasta, no garlic', 'table 4', 'out by 8:15', tagged what, for whom and by when, and its pan is on the flame with a tick: dinner on time."),
    ("prd-sheet", "Object: the one-page PRD", "purple", prd_sheet, "A single page with a folded corner and five numbered parts, named around it: the problem, who it is for, what is in, what is out (highlighted) and open questions."),
]


def build():
    out = HERE.parent / "img" / "explainers"
    out.mkdir(parents=True, exist_ok=True)
    cards = []
    for slug, name, tint, fn, alt in GALLERY:
        pal = palette_for(tint)
        svg = illustration(fn(), tint=tint, uid=f"ex-{slug}", title=name, desc=alt)
        low = [r for r in check_contrast(svg) if r[2] < 4.5]
        if low:
            raise SystemExit(f"ex-{slug}: text below 4.5:1: {low}")
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
<meta name="description" content="Fourteen explainer figures drawn by the illustration generator, from diagrams and charts to an analogy scene and an object, shown on the white and the near-black page.">
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
    <p>Fourteen explainer figures drawn by <code>tools/illustration.py</code>: twelve diagram and chart types, then an analogy scene (the order ticket a kitchen cooks from) and an object (the one-page PRD with its parts named). The picture is whatever the article needs; these show the range, not a menu. Labels are Inter Medium at 27 units and notes Inter Regular at 24 units, 16 px and 14 px at the article's 720 px column, every label checked for 4.5:1 on its fill. All are drawn on the eight pastel tints from the Printables site, with its dark dot grid and dark ink. In an article every explainer shares the article's tint (by publish order, like the Printables tiles); here the types run across all eight, so some tints repeat. Each image is one PNG, shown on the white page and on the near-black page. The swatches show each tint with its two highlight colours (A and B) and the label contrast. Rules: <a href="../../illustration-rules.md">illustration-rules.md</a>; source: <a href="../../references/printables-tints.md">printables-tints.md</a>.</p>
  </section>
  <h2 class="vh" id="sw-h">The eight tints</h2>
  <ul class="swatches" aria-labelledby="sw-h">
    {swatches}
  </ul>
  <ul class="exs">
{chr(10).join(cards)}
  </ul>
</main>
<footer class="site-foot"><div class="site-foot__in"><div class="legal"><span>userandproduct mockups</span><a href="variants/index.html">Article variants</a><a href="../../final-logo-2/brand-sheet.html">Brand sheet</a></div></div></footer>
</body>
</html>
"""
    (HERE / "explainers.html").write_text(html, encoding="utf-8", newline="\n")
    print("wrote explainers.html")


if __name__ == "__main__":
    build()
