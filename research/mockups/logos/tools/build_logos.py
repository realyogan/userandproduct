"""Builds the round 1 logo concepts: SVG files, variants.js and index.html.

Usage: python build_logos.py [letters]   e.g. "ABC" to build only those.
Writes into the parent folder (research/mockups/logos/).
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from glyphs import word, line, render, bbox, Rect, Band, CAP, DESC, f  # noqa: E402

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME = "userandproduct"

INK = {"light": "#0A0A0C", "dark": "#F4F4F5"}
ACCENTS = {
    "red": {"name": "Masthead red", "light": "#B3141C", "dark": "#F2555C"},
    "blue": {"name": "Ink blue", "light": "#1F3FBF", "dark": "#7D96FF"},
}


# ------------------------------------------------------------ helpers
def P(role, d, rule=None):
    return {"t": "path", "role": role, "d": d, "rule": rule}


def M(role, shape, cut, key):
    return {"t": "masked", "role": role, "d": shape, "cut": cut, "key": key}


def text_line(txt, weight, cap, x, y, track=0.0):
    """Word set at cap height `cap`, top-left at (x, y). Returns (d, width)."""
    pieces, w = word(txt, weight, track=track)
    sc = cap / CAP
    b = bbox(pieces)
    return render(pieces, sc, x - b[0] * sc, y), (b[2] - b[0]) * sc


def name_line(cap, x, y, weight="bold", track=0.0, words=("user", "and", "product")):
    """The one-word name with "and" in the light weight and the accent.
    (x, y) is the ascender top-left. Returns (els, width)."""
    roles = ["ink", "accent", "ink"]
    wts = [weight, "light", weight]
    segs = [(w_, wts[i], roles[i]) for i, w_ in enumerate(words) if w_]
    runs, _ = line(segs, track)
    sc = cap / CAP
    allp = [p for _, ps in runs for p in ps]
    b = bbox(allp)
    d = {"ink": "", "accent": ""}
    for role, ps in runs:
        d[role] += render(ps, sc, x - b[0] * sc, y)
    return [P(r, d[r]) for r in ("ink", "accent") if d[r]], (b[2] - b[0]) * sc


def name_lockup(mark_els, mark_w, cap, weight="bold", track=0.0, gap=34, mark_h=100):
    """Mark at the origin, name to its right with its x-height centred on the mark."""
    sc = cap / CAP
    top = mark_h / 2 - (CAP - 37) * sc
    els, w = name_line(cap, mark_w + gap, top, weight, track)
    y0 = min(-2, top - 2)
    y1 = max(mark_h + 2, top + (CAP + DESC) * sc + 2)
    return {"vb": (-2, f(y0), f(mark_w + gap + w + 4), f(y1 - y0)), "els": mark_els + els}


def line_width(txt, weight, track=0.0):
    pieces, _ = word(txt, weight, track=track)
    b = bbox(pieces)
    return b[2] - b[0]


def rrect(x, y, w, h, r):
    return (f"M{f(x + r)} {f(y)}h{f(w - 2 * r)}a{f(r)} {f(r)} 0 0 1 {f(r)} {f(r)}v{f(h - 2 * r)}"
            f"a{f(r)} {f(r)} 0 0 1 {f(-r)} {f(r)}h{f(-(w - 2 * r))}a{f(r)} {f(r)} 0 0 1 {f(-r)} {f(-r)}"
            f"v{f(-(h - 2 * r))}a{f(r)} {f(r)} 0 0 1 {f(r)} {f(-r)}Z")


def circle(cx, cy, r):
    return (f"M{f(cx - r)} {f(cy)}a{f(r)} {f(r)} 0 1 0 {f(2 * r)} 0a{f(r)} {f(r)} 0 1 0 {f(-2 * r)} 0Z")


def shapes(lst, sc=1.0, tx=0.0, ty=0.0):
    return "".join(s.d(sc, tx, ty) for s in lst)


# ------------------------------------------------------------ concepts
def concept_A():
    acc = "blue"
    # A1: one line, "and" lighter and in the accent
    els, W = name_line(100, 0, 0)
    lockup = {"vb": (-2, -4, f(W + 4), CAP + DESC + 8), "els": els}
    # A2: two lines, "user and" over "product"
    e1, v1 = name_line(100, 0, 0, words=("user", "and", ""))
    e2, v2 = name_line(100, 0, 112, words=("", "", "product"))
    stacked = {"vb": (-2, -4, f(max(v1, v2) + 4), 112 + CAP + DESC + 8), "els": e1 + e2}
    # icon: U P with the accent rule under it
    pieces, _ = word("UP", "black")
    b = bbox(pieces)
    sc = 74 / (b[2] - b[0])
    h = 100 * sc
    top = (100 - (h + 8 + 9)) / 2
    d_up = render(pieces, sc, 13 - b[0] * sc, top)
    icon = {"vb": (0, 0, 100, 100), "els": [P("ink", d_up), P("accent", Rect(13, top + h + 9, 74, 8).d(1, 0, 0))]}
    return {
        "id": "A", "slug": "a-wordmark", "name": "Wordmark", "category": "Pure wordmark", "accent": acc,
        "rationale": "The name is the logo: userandproduct as one heavy lowercase word, with \"and\" in a "
                     "light weight and the accent so it reads user / and / product at a glance.",
        "lockup": lockup, "alt": {"label": "Two lines", "art": stacked}, "icon": icon,
        "icon_note": "Favicon: UP in black weight over an accent rule.",
    }


def concept_B():
    acc = "blue"
    s, h = 27, 23
    W = 84
    ry = W / 2 + 2
    cy = 101.5 - ry
    u = [Rect(0, 0, s, cy + 0.5), Band(W / 2, cy, W / 2, ry, s, h, 0, 180), Rect(W - s, 0, s, 100)]
    mb, rx = 62, 32
    bx = W + 7
    bowl = [Rect(W, 0, bx - W + 0.5, h), Rect(W, mb - h, bx - W + 0.5, h),
            Band(bx, mb / 2, rx, mb / 2, s, h, -90, 90)]
    mark_w = bx + rx

    def mark(tx, ty, sc=1.0):
        return [P("ink", shapes(u, sc, tx, ty)), P("accent", shapes(bowl, sc, tx, ty))]

    sc = 84 / mark_w
    icon = {"vb": (0, 0, 100, 100), "els": mark((100 - mark_w * sc) / 2, (100 - 101.5 * sc) / 2, sc)}
    lockup = name_lockup(mark(0, 0), mark_w, 62, mark_h=101.5)
    return {
        "id": "B", "slug": "b-monogram", "name": "UP monogram", "category": "Monogram", "accent": acc,
        "rationale": "U and P share one stem: the user's right side is the product's spine. It also reads "
                     "\"up\", the direction the site wants to move a career.",
        "lockup": lockup, "icon": icon, "icon_note": "Favicon: the monogram alone, heavy enough for 16px.",
    }


def concept_C():
    acc = "blue"
    cx, cy, r = 35, 50, 22
    sq = (47, 30, 40)
    tile = rrect(0, 0, 100, 100, 16)
    holes = circle(cx, cy, r) + f"M{sq[0]} {sq[1]}h{sq[2]}v{sq[2]}h{-sq[2]}Z"
    dy = math.sqrt(r * r - (sq[0] - cx) ** 2)
    lens = f"M{sq[0]} {f(cy - dy)}A{r} {r} 0 0 1 {sq[0]} {f(cy + dy)}Z"

    def mark(tx=0.0, ty=0.0):
        # the tile is drawn at the origin; lockups shift the text, not the tile
        return [P("ink", tile + holes, "evenodd"), P("accent", lens)]

    icon = {"vb": (0, 0, 100, 100), "els": mark()}
    lockup = name_lockup(mark(), 100, 64, gap=30)
    return {
        "id": "C", "slug": "c-overlap", "name": "Where they meet", "category": "Symbolic mark", "accent": acc,
        "rationale": "A circle (the person) and a square (the thing they use) are cut out of a solid block; "
                     "the only filled part between them is the overlap, which is what the site writes about.",
        "lockup": lockup, "icon": icon, "icon_note": "Favicon: the tile alone.",
    }


def concept_D():
    acc = "red"
    # Solid tile with one P-shaped cut: a round head on a stem that exits the bottom edge.
    cx, cy, r = 57, 40, 21
    sl, sw = cx - r, 15
    sr = sl + sw
    y_join = cy + math.sqrt(r * r - (sr - cx) ** 2)
    k = 5
    tile = (f"M{k} 0h{100 - 2 * k}a{k} {k} 0 0 1 {k} {k}v{100 - 2 * k}a{k} {k} 0 0 1 {-k} {k}"
            f"H{sr}V{f(y_join)}A{r} {r} 0 1 0 {sl} {cy}V100H{k}a{k} {k} 0 0 1 {-k} {-k}V{k}"
            f"a{k} {k} 0 0 1 {k} {-k}Z")
    icon = {"vb": (0, 0, 100, 100), "els": [P("accent", tile)]}
    lockup = name_lockup([P("accent", tile)], 100, 64, gap=30)
    return {
        "id": "D", "slug": "d-imprint", "name": "Imprint", "category": "Abstract geometric", "accent": acc,
        "rationale": "A solid block (the product) with one cut: a head on a body, which is also a P and a "
                     "doorway into the box. Red block like a publisher's imprint or a seal.",
        "lockup": lockup, "icon": icon, "icon_note": "Favicon: the red block alone.",
    }


def concept_E():
    acc = "blue"
    s, h = 24, 22
    u = [Rect(0, 40, s, 10.5), Rect(100 - s, 40, s, 10.5), Band(50, 50, 50, 50, s, h, 0, 180)]
    irx, iry = 50 - s, 50 - h
    gap, half = 6, 20
    yb = 50 + iry * math.sqrt(1 - ((half) / irx) ** 2) - gap
    top = yb - 40

    def mark(sc=1.0, tx=0.0, ty=0.0):
        bx = rrect(tx + 30 * sc, ty + top * sc, 40 * sc, 40 * sc, 6 * sc)
        return [P("ink", shapes(u, sc, tx, ty)), P("accent", bx)]

    hgt = 100 - top
    icon = {"vb": (-8, f(top - (116 - hgt) / 2), 116, 116), "els": mark()}
    sc = 100 / hgt
    lockup = name_lockup(mark(sc, 0, -top * sc), 100 * sc, 64)
    return {
        "id": "E", "slug": "e-cradle", "name": "Cradle", "category": "Letterform and metaphor", "accent": acc,
        "rationale": "A heavy U (the user) holds a rounded square (the product): the product only matters "
                     "in the hands of the person using it.",
        "lockup": lockup, "icon": icon, "icon_note": "Favicon: the U and the box.",
    }


def concept_F():
    acc = "red"
    wP = line_width("PRODUCT", "black")
    wU = line_width("USER", "black")
    capU = 100 * wP / wU
    gap = 16
    l1, _ = text_line("USER", "black", capU, 0, 0)
    y = capU + gap
    # AND: centred between two accent rules
    capA = 40
    l2, wa = text_line("AND", "bold", capA, 0, 0, track=22)
    xa = (wP - wa) / 2
    l2, wa = text_line("AND", "bold", capA, xa, y, track=22)
    rule_h, rgap = 7, 22
    ry = y + (capA - rule_h) / 2
    l2 += Rect(0, ry, xa - rgap, rule_h).d(1, 0, 0) + Rect(xa + wa + rgap, ry, wP - xa - wa - rgap, rule_h).d(1, 0, 0)
    y += capA + gap
    l3, _ = text_line("PRODUCT", "black", 100, 0, y)
    H = y + 100
    lockup = {"vb": (-3, -3, wP + 6, H + 6), "els": [P("ink", l1 + l3), P("accent", l2)]}
    # icon: dark tile with U over P cut out, red rule between
    u_p, _ = word("U", "black")
    p_p, _ = word("P", "black")
    scl = 0.36
    bu, bp = bbox(u_p), bbox(p_p)
    cut = (render(u_p, scl, 50 - (bu[2] - bu[0]) * scl / 2 - bu[0] * scl, 12) +
           render(p_p, scl, 50 - (bp[2] - bp[0]) * scl / 2 - bp[0] * scl, 52.5))
    icon = {"vb": (0, 0, 100, 100), "els": [M("ink", rrect(0, 0, 100, 100, 12), cut, "tile"),
                                             P("accent", Rect(22, 47.5, 56, 6).d(1, 0, 0))]}
    return {
        "id": "F", "slug": "f-masthead", "name": "Masthead", "category": "Editorial masthead", "accent": acc,
        "rationale": "USER / AND / PRODUCT set as one justified block, the way a magazine carries its "
                     "name on the cover: heavy, square, impossible to mistake for a blog.",
        "lockup": lockup, "icon": icon, "icon_note": "Favicon: U over P knocked out of a block, red rule between.",
    }


def _justify(txt, weight, cap, x, y, width):
    """Sets each letter so the line fills `width` exactly, word space doubled."""
    from glyphs import GLYPHS, weights
    s, h = weights(weight)
    sc = cap / CAP
    items = []
    for ch in txt:
        if ch == " ":
            items.append(None)
            continue
        ps, W, _ = GLYPHS[ch](s, h)
        lo = min(p.bbox()[0] for p in ps)
        hi = max(p.bbox()[2] for p in ps)
        items.append((ps, lo, hi))
    letters = [i for i in items if i]
    ink = sum((hi - lo) * sc for _, lo, hi in letters)
    units = 0
    for i in range(1, len(items)):
        if items[i] is None:
            continue
        units += 3 if items[i - 1] is None else 1
    unit = (width - ink) / units
    d, cx, pending = "", x, 0
    first = True
    for it in items:
        if it is None:
            pending = 2
            continue
        ps, lo, hi = it
        if not first:
            cx += unit * (1 + pending)
        pending = 0
        first = False
        d += "".join(p.d(sc, cx - lo * sc, y) for p in ps)
        cx += (hi - lo) * sc
    return d, cx - x


def concept_G():
    acc = "red"
    s, h = 19, 17
    st1 = 44
    st2 = st1 + s + 12
    W = st2 + s
    bowl = [Band(30, 30, 30, 30, 30, 30, 90, 270), Rect(29.5, 0, st1 - 29.5, 60)]
    ink = [Rect(st1, 0, s, 100), Rect(st2, 0, s, 100), Rect(st1, 0, st2 - st1, h)]

    def mark(sc=1.0, tx=0.0, ty=0.0):
        return [P("accent", shapes(bowl, sc, tx, ty)), P("ink", shapes(ink, sc, tx, ty))]

    sc = 0.86
    icon = {"vb": (0, 0, 100, 100), "els": mark(sc, (100 - W * sc) / 2, (100 - 100 * sc) / 2)}
    lockup = name_lockup(mark(), W, 64, weight="semi", track=4, gap=30)
    return {
        "id": "G", "slug": "g-pilcrow", "name": "Pilcrow", "category": "Own idea: the paragraph mark", "accent": acc,
        "rationale": "The pilcrow is the editor's mark for \"a new idea starts here\": two stems (user and "
                     "product) carried by one bowl (the thinking), in editor's red. It is also a P.",
        "lockup": lockup, "icon": icon, "icon_note": "Favicon: the pilcrow alone.",
    }


def concept_H():
    acc = "red"
    # "et" ligature, the ampersand's origin: a heavy e whose bar runs on as the t's crossbar.
    s, h = 22, 16
    cx, cy, r = 44, 54.5, 44
    e = Band(cx, cy, r, r + 1.5, s, h, 38, 360)
    tx = 2 * r + 12
    t_stem = Rect(tx, 0, s, 100.5)
    bar = Rect(s - 0.5, cy - h, tx - s + 1, h)          # e's bar, running on to the t
    arm = Rect(tx + s - 0.5, cy - h, 16.5, h)          # the t's right arm
    W = tx + s + 16

    def mark(sc=1.0, ox=0.0, oy=0.0):
        return [P("ink", e.d(sc, ox, oy) + bar.d(sc, ox, oy)),
                P("accent", t_stem.d(sc, ox, oy) + arm.d(sc, ox, oy))]

    sc = 84 / W
    icon = {"vb": (0, 0, 100, 100), "els": mark(sc, (100 - W * sc) / 2, (100 - 100.5 * sc) / 2)}
    lockup = name_lockup(mark(), W, 64, gap=30)
    return {
        "id": "H", "slug": "h-et", "name": "Et", "category": "Typography history", "accent": acc,
        "rationale": "The ampersand began as a scribe's ligature of \"et\", Latin for \"and\". Here the e's bar "
                     "runs on as the t's crossbar, and the t is in rubric red, the scribe's colour for what matters.",
        "lockup": lockup, "icon": icon, "icon_note": "Favicon: the et ligature alone.",
    }


def concept_I():
    acc = "blue"
    # A geometric eye (two arcs) with a square pupil: the product as the user sees it.
    sag = 32
    R = (50 ** 2 + sag ** 2) / (2 * sag)
    eye = f"M0 50A{f(R)} {f(R)} 0 0 1 100 50A{f(R)} {f(R)} 0 0 1 0 50Z"
    hole = "M33 33h34v34h-34Z"
    pupil = "M41 41h18v18h-18Z"
    els = [P("ink", eye + hole, "evenodd"), P("accent", pupil)]
    icon = {"vb": (0, 0, 100, 100), "els": els}
    lockup = name_lockup(els, 100, 64, gap=30)
    return {
        "id": "I", "slug": "i-view", "name": "Point of view", "category": "The user's eye", "accent": acc,
        "rationale": "An eye drawn from two arcs whose pupil is a square: the product only exists as the "
                     "user sees it. Sight first, object second.",
        "lockup": lockup, "icon": icon, "icon_note": "Favicon: the eye alone.",
    }


def concept_J():
    acc = "blue"
    # A ruler block with notches cut from its top edge and a pointer on the reading.
    top, bot = 36, 82
    depths = [22, 10, 15, 10, 30, 10, 15, 10, 22]
    ticks = [(10 + 10 * i, dp) for i, dp in enumerate(depths)]
    tw = 4.5
    d = f"M0 {top}"
    for x, depth in ticks:
        d += f"H{f(x - tw / 2)}V{top + depth}H{f(x + tw / 2)}V{top}"
    d += f"H100V{bot}H0Z"
    pointer = "M39 8H61L50 28Z"
    els = [P("ink", d), P("accent", pointer)]
    icon = {"vb": (0, -5, 100, 100), "els": els}
    lockup = name_lockup(els, 100, 64, gap=30)
    return {
        "id": "J", "slug": "j-gauge", "name": "Gauge", "category": "Data and evidence", "accent": acc,
        "rationale": "A heavy ruler with notches cut into it and one pointer on the reading: measured, not "
                     "guessed. The site's claim is evidence from 15 years of practice.",
        "lockup": lockup, "icon": icon, "icon_note": "Favicon: the ruler and pointer.",
    }


def concept_K():
    acc = "blue"
    # A round arch: two heavy springers (user, product) held by one keystone (the site).
    cx, cy, R, r = 50, 66, 48, 22
    t = R - r
    j = 2.5  # joint, degrees
    left = Band(cx, cy, R, R, t, t, 180, 254 - j)
    right = Band(cx, cy, R, R, t, t, 286 + j, 360)
    key = Band(cx, cy, R + 6, R + 6, t + 6, t + 6, 254, 286)
    legs = [Rect(2, cy - 0.5, t, 100 - cy + 0.5), Rect(100 - 2 - t, cy - 0.5, t, 100 - cy + 0.5)]
    els = [P("ink", left.d(1, 0, 0) + right.d(1, 0, 0) + shapes(legs)), P("accent", key.d(1, 0, 0))]
    icon = {"vb": (0, 2, 100, 100), "els": els}
    lockup = name_lockup(els, 100, 64, gap=30)
    return {
        "id": "K", "slug": "k-keystone", "name": "Keystone", "category": "Architecture", "accent": acc,
        "rationale": "An arch: two heavy sides, the user and the product, that only stand because one "
                     "keystone at the top locks them together. That keystone is the site.",
        "lockup": lockup, "icon": icon, "icon_note": "Favicon: the arch and keystone.",
    }


def concept_L():
    acc = "red"
    # The magazine as an object: a closed book block with a ribbon marker hanging out of it.
    book = "M10 0H90V84H10ZM21 0H25V84H21Z"  # block with a spine groove
    rx0, rw = 58, 16
    ribbon = f"M{rx0} 0H{rx0 + rw}V100L{rx0 + rw / 2} 92L{rx0} 100Z"
    els = [P("ink", book, "evenodd"), P("accent", ribbon)]
    icon = {"vb": (0, 0, 100, 100), "els": els}
    lockup = name_lockup(els, 100, 64, gap=26)
    return {
        "id": "L", "slug": "l-ribbon", "name": "Ribbon", "category": "The printed page", "accent": acc,
        "rationale": "A heavy book block with a red ribbon marker: the page you keep and return to. The "
                     "site as a reference work, not a feed.",
        "lockup": lockup, "icon": icon, "icon_note": "Favicon: the book and ribbon.",
    }


CONCEPTS = {"A": concept_A, "B": concept_B, "C": concept_C, "D": concept_D, "E": concept_E,
            "F": concept_F, "G": concept_G,
            "H": concept_H, "I": concept_I, "J": concept_J, "K": concept_K, "L": concept_L}


# ------------------------------------------------------------ rendering
def colours(mode, acc):
    if mode == "mono":
        return {"ink": None, "accent": None}
    return {"ink": INK[mode], "accent": ACCENTS[acc][mode]}


def svg_markup(art, mode, acc, idp, standalone=True, title=NAME):
    vb = art["vb"]
    vbs = " ".join(f(float(v)) for v in vb)
    col = colours(mode, acc)
    defs, body = [], []
    for i, e in enumerate(art["els"]):
        fill = col[e["role"]]
        fa = f' fill="{fill}"' if fill else ""
        if e["t"] == "path":
            rule = f' fill-rule="{e["rule"]}"' if e["rule"] else ""
            body.append(f'<path{fa}{rule} d="{e["d"]}"/>')
        else:
            mid = f"{idp}-{e['key']}"
            defs.append(f'<mask id="{mid}" maskUnits="userSpaceOnUse" x="{f(float(vb[0]))}" '
                        f'y="{f(float(vb[1]))}" width="{f(float(vb[2]))}" height="{f(float(vb[3]))}">'
                        f'<rect x="{f(float(vb[0]))}" y="{f(float(vb[1]))}" width="{f(float(vb[2]))}" '
                        f'height="{f(float(vb[3]))}" fill="#fff"/><path fill="#000" d="{e["cut"]}"/></mask>')
            body.append(f'<path{fa} mask="url(#{mid})" d="{e["d"]}"/>')
    root_fill = ' fill="currentColor"' if mode == "mono" else ""
    ns = ' xmlns="http://www.w3.org/2000/svg"' if standalone else ""
    out = [f'<svg{ns} viewBox="{vbs}"{root_fill} role="img" aria-label="{title}">', f"<title>{title}</title>"]
    if defs:
        out.append("<defs>" + "".join(defs) + "</defs>")
    out += body
    out.append("</svg>")
    return "\n".join(out) + "\n"


def write_concept(c):
    files = {}
    arts = [("lockup", c["lockup"]), ("icon", c["icon"])]
    if "alt" in c:
        arts.append(("stacked", c["alt"]["art"]))
    for kind, art in arts:
        for mode in ("light", "dark", "mono"):
            suffix = "" if mode == "light" else f"-{mode}"
            fn = f"{c['slug']}-{kind}{suffix}.svg"
            with open(os.path.join(OUT, fn), "w", encoding="utf-8", newline="\n") as fh:
                fh.write(svg_markup(art, mode, c["accent"], f"{c['id'].lower()}{kind[0]}"))
            files[(kind, mode)] = fn
    return files


def write_variants(built):
    concepts = []
    for c, files in built:
        acc = ACCENTS[c["accent"]]["name"]
        v = [{"id": c["id"], "name": "Mark / favicon (lockups: index.html)",
              "description": f"{c['category']}. {c['rationale']} {c['icon_note']} Accent: {acc}.",
              "light": files[("icon", "light")], "dark": files[("icon", "dark")]}]
        concepts.append({"name": f"{c['id']}. {c['name']} ({c['category']})", "variants": v})
    data = {"projectName": "userandproduct, round 1:", "brandName": NAME, "concepts": concepts}
    with open(os.path.join(OUT, "variants.js"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("// Logo concepts, round 1 (9 Oct 2026). Generated by tools/build_logos.py.\n")
        fh.write("window.VARIANTS = " + json.dumps(data, indent=2) + ";\n")


def main():
    letters = sys.argv[1] if len(sys.argv) > 1 else "ABCDEFGHIJKL"
    built = []
    for k in letters:
        c = CONCEPTS[k]()
        built.append((c, write_concept(c)))
    write_variants(built)
    if len(sys.argv) > 2 and sys.argv[2] == "index":
        import build_index
        build_index.write(built, svg_markup, ACCENTS, INK, OUT)
    print("built", letters)


if __name__ == "__main__":
    main()
