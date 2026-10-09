"""Article illustrations (plain style, see ../illustration-rules.md) and the background comparison.

build.py imports fig_questions() and fig_fail() for variant A. Run `python figures.py` to write the PNG and SVG files
into img/ and to refresh the background comparison row in index.html (between frames:start and frames:end).
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "tools"))
from illustration import illustration, write, png, tint_for_article  # noqa: E402

# One tint per article: every explainer in an article uses its tint; Related thumbnails use their own article's tint.
# Index = publish order (mirrors printables_tint_class(index)), so neighbours differ.
ARTICLES = {
    "how-to-write-a-prd-that-engineers-actually-read": 0,
    "user-stories-that-survive-sprint-planning": 1,
    "the-discovery-plan-i-run-in-the-first-two-weeks": 2,
    "how-many-users-for-a-usability-test": 3,
}
ARTICLE = "how-to-write-a-prd-that-engineers-actually-read"
TINT = tint_for_article(ARTICLE, index=ARTICLES[ARTICLE])
THUMB_ARTICLE = {"user-stories": "user-stories-that-survive-sprint-planning",
                 "discovery-plan": "the-discovery-plan-i-run-in-the-first-two-weeks",
                 "usability-test": "how-many-users-for-a-usability-test"}


PARTS = [("problem", ["Q1 problem", "Q5 success"]),
         ("users", ["Q2 who", "Q3 today", "Q4 evidence"]),
         ("scope", ["Q6 in scope", "Q7 not in v1"]),
         ("flows", ["Q8 flows", "Q9 edges", "Q10 limits"]),
         ("accept", ["Q11 accept"]),
         ("open", ["Q12 open"])]
KEY = {"Q7 not in v1", "Q9 edges", "Q12 open"}


def questions_items():
    x0, cw = 120, 160
    items = [{"type": "rule", "x": x0 + i * cw, "y1": 72, "y2": 540} for i in range(7)]
    for i, (_, qs) in enumerate(PARTS):
        y = 96 + i * 50
        for q in qs:
            items.append({"type": "box", "x": x0 + i * cw + 8, "y": y, "w": cw - 16, "h": 46, "label": q,
                          "tint": "blue" if q in KEY else None, "size": 18})
            y += 60
    for i, (name, _) in enumerate(PARTS):
        items.append({"type": "text", "x": x0 + (i + 0.5) * cw, "y": 590, "text": name, "anchor": "middle", "size": 18})
    return items


def fail_items():
    items = []
    for x, label, note, tint in ((120, "written for approval", "market and strategy first", None),
                                 (450, "wall of text", "every edge case, same weight", None),
                                 (780, "decisions missing", "asked in week-3 tickets", "red")):
        items.append({"type": "box", "x": x, "y": 220, "w": 300, "h": 64, "label": label, "tint": tint})
        items.append({"type": "text", "x": x + 16, "y": 330, "text": note, "size": 18})
    items += [{"type": "arrow", "x1": 422, "y1": 252, "x2": 448, "y2": 252},
              {"type": "arrow", "x1": 752, "y1": 252, "x2": 778, "y2": 252},
              {"type": "hrule", "y": 420, "x1": 120, "x2": 1080},
              {"type": "text", "x": 120, "y": 470, "text": "kickoff", "size": 18},
              {"type": "text", "x": 600, "y": 470, "text": "sprint 1", "anchor": "middle", "size": 18},
              {"type": "text", "x": 1080, "y": 470, "text": "sprint 2 and later", "anchor": "end", "size": 18}]
    return items


ALT_Q = ("Diagram: six columns, one per part of the PRD (problem, users, scope, flows, acceptance, open). Each holds the "
         "questions answered there, stepping down from left to right; question 7 (not in version 1), question 9 (edges) "
         "and question 12 (open) are highlighted.")
ALT_F = ("Diagram: three boxes joined by arrows: written for approval (market and strategy first), wall of text (every edge "
         "case at the same weight) and, highlighted, decisions missing (asked in tickets in week 3), above a timeline from "
         "kickoff to sprint 2 and later.")


def fig_questions():
    return f"""<figure class="fig fig--plain" id="fig-questions">
  <img src="img/fig-twelve-questions.png" width="1200" height="675" alt="{ALT_Q}" loading="lazy" decoding="async">
  <figcaption><b>Figure 2.</b> The twelve questions sorted into the six parts of the PRD. The three highlighted ones are skipped most often and asked about latest.</figcaption>
</figure>"""


def fig_fail():
    return f"""<figure class="fig fig--plain" id="fig-fail">
  <img src="img/fig-where-prds-fail.png" width="1200" height="675" alt="{ALT_F}" loading="lazy" decoding="async">
  <figcaption><b>Figure 1.</b> Where PRDs fail. The first two are writing problems; the third is the one that costs build time.</figcaption>
</figure>"""


THUMBS = {
    "user-stories": [
        {"type": "box", "x": 200, "y": 190, "w": 440, "h": 70, "label": "As an analyst, I want", "size": 26},
        {"type": "box", "x": 250, "y": 290, "w": 440, "h": 70, "label": "so that Monday is fast", "size": 26},
        {"type": "box", "x": 300, "y": 390, "w": 440, "h": 70, "label": "done when: 3 checks", "tint": "blue", "size": 26},
        {"type": "arrow", "x1": 760, "y1": 425, "x2": 860, "y2": 425},
        {"type": "box", "x": 870, "y": 390, "w": 180, "h": 70, "label": "sprint", "size": 26}],
    "discovery-plan": [
        *[{"type": "rule", "x": 180 + i * 168, "y1": 140, "y2": 540} for i in range(6)],
        {"type": "box", "x": 188, "y": 180, "w": 320, "h": 64, "label": "interviews", "size": 26},
        {"type": "box", "x": 524, "y": 280, "w": 152, "h": 64, "label": "data", "size": 26},
        {"type": "box", "x": 692, "y": 380, "w": 152, "h": 64, "label": "memo", "tint": "blue", "size": 26},
        {"type": "box", "x": 860, "y": 380, "w": 152, "h": 64, "label": "decide", "tint": "yellow", "size": 26}],
    "usability-test": [
        {"type": "hrule", "y": 540, "x1": 160, "x2": 1040},
        *[{"type": "box", "x": 190 + i * 176, "y": 526 - h, "w": 120, "h": h, "label": str(n), "size": 28,
           "tint": "blue" if n == 5 else None} for i, (n, h) in enumerate([(1, 90), (2, 170), (3, 240), (4, 290), (5, 330)])]],
}


def write_all():
    img = HERE / "img"
    for name, items, title, desc in (("fig-twelve-questions", questions_items(), "The twelve questions in six parts", ALT_Q),
                                     ("fig-where-prds-fail", fail_items(), "Where PRDs fail", ALT_F)):
        svg = illustration(items, tint=TINT, uid=name, title=title, desc=desc)
        write(svg, img / f"{name}.svg")
        png(svg, img / f"{name}.png", 1200)
    for slug, items in THUMBS.items():
        art = THUMB_ARTICLE[slug]
        png(illustration(items, tint=tint_for_article(art, index=ARTICLES[art]), uid=f"t-{slug}"), img / f"{slug}-thumb.png", 600)


def comparison_row():
    return ('<p><a href="explainers.html">Open the explainer gallery</a>: twelve diagram types, each on a different '
            'background from the curated twelve, each shown on the white page and on the near-black page.</p>')


if __name__ == "__main__":
    write_all()
    idx = HERE / "index.html"
    s = idx.read_text(encoding="utf-8")
    s = re.sub(r"(<!-- frames:start -->).*?(<!-- frames:end -->)", lambda m: m.group(1) + comparison_row() + m.group(2), s, flags=re.S)
    idx.write_text(s, encoding="utf-8", newline="\n")
    print("wrote figures, thumbnails and backgrounds; refreshed index.html")
