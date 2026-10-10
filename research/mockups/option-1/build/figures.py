"""Article illustrations (plain style, see research/mockups/illustration-rules.md) and the background comparison.

build_article.py imports fig_questions() and fig_fail() for variant A. Run `python figures.py` (from option-1/build/)
to write the PNG and SVG files into option-1/img/ and to refresh the background comparison row in
variants/index.html (between frames:start and frames:end).
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent   # option-1/build/
sys.path.insert(0, str(HERE.parents[1] / "tools"))   # research/mockups/tools/
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


# Labels without the Q prefix so each fits a 168-unit box at 27 units; the number stays in front.
PARTS = [("problem", ["1 problem", "5 success"]),
         ("users", ["2 who", "3 today", "4 proof"]),
         ("scope", ["6 in scope", "7 not in v1"]),
         ("flows", ["8 flows", "9 edges", "10 limits"]),
         ("accept", ["11 accept"]),
         ("open", ["12 open"])]
KEY = {"7 not in v1", "9 edges", "12 open"}


def questions_items():
    x0, cw = 72, 176
    items = [{"type": "rule", "x": x0 + i * cw, "y1": 72, "y2": 540} for i in range(7)]
    for i, (_, qs) in enumerate(PARTS):
        y = 92 + i * 52
        for q in qs:
            items.append({"type": "box", "x": x0 + i * cw + 4, "y": y, "w": cw - 8, "h": 56, "label": q,
                          "tint": "b" if q in KEY else None})
            y += 68
    for i, (name, _) in enumerate(PARTS):
        items.append({"type": "text", "x": x0 + (i + 0.5) * cw, "y": 584, "text": name, "anchor": "middle",
                      "role": "label", "muted": False})
    return items


def fail_items():
    items = []
    for x, label, note, tint in ((72, "written for approval", "market and strategy first", None),
                                 (440, "wall of text", "every edge case, same weight", None),
                                 (808, "decisions missing", "asked in week-3 tickets", "b")):
        items.append({"type": "box", "x": x, "y": 200, "w": 320, "h": 72, "label": label, "tint": tint})
        items.append({"type": "text", "x": x + 16, "y": 316, "text": note})
    items += [{"type": "arrow", "x1": 394, "y1": 236, "x2": 438, "y2": 236},
              {"type": "arrow", "x1": 762, "y1": 236, "x2": 806, "y2": 236},
              {"type": "hrule", "y": 420, "x1": 72, "x2": 1128},
              {"type": "text", "x": 72, "y": 466, "text": "kickoff"},
              {"type": "text", "x": 600, "y": 466, "text": "sprint 1", "anchor": "middle"},
              {"type": "text", "x": 1128, "y": 466, "text": "sprint 2 and later", "anchor": "end"}]
    return items


ALT_Q = ("Diagram: six columns, one per part of the PRD (problem, users, scope, flows, acceptance, open). Each holds the "
         "questions answered there, stepping down from left to right; question 4 is the proof, and question 7 (not in version 1), "
         "question 9 (edges) and question 12 (open) are highlighted.")
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


# Thumbnails export at 600 wide and show at about a quarter of the canvas, so their type floors are doubled
# (labels 54, notes 48; illustration(..., thumb=True)) and their labels are one or two words.
THUMBS = {
    "user-stories": [
        {"type": "box", "x": 140, "y": 130, "w": 470, "h": 100, "label": "As a user"},
        {"type": "box", "x": 200, "y": 270, "w": 470, "h": 100, "label": "so that"},
        {"type": "box", "x": 260, "y": 410, "w": 470, "h": 100, "label": "done when", "tint": "a"},
        {"type": "arrow", "x1": 744, "y1": 460, "x2": 816, "y2": 460},
        {"type": "box", "x": 830, "y": 410, "w": 260, "h": 100, "label": "sprint", "anchor": "middle"}],
    "discovery-plan": [
        *[{"type": "rule", "x": 120 + i * 240, "y1": 110, "y2": 560} for i in range(5)],
        {"type": "box", "x": 128, "y": 140, "w": 464, "h": 96, "label": "interviews"},
        {"type": "box", "x": 368, "y": 270, "w": 224, "h": 96, "label": "data", "anchor": "middle"},
        {"type": "box", "x": 608, "y": 400, "w": 224, "h": 96, "label": "memo", "anchor": "middle", "tint": "a"},
        {"type": "box", "x": 848, "y": 400, "w": 224, "h": 96, "label": "decide", "anchor": "middle", "tint": "b"}],
    "usability-test": [
        {"type": "hrule", "y": 540, "x1": 120, "x2": 1080},
        *[{"type": "box", "x": 170 + i * 176, "y": 540 - h, "w": 120, "h": h, "label": str(n), "anchor": "middle",
           "tint": "a" if n == 5 else None} for i, (n, h) in enumerate([(1, 100), (2, 180), (3, 250), (4, 300), (5, 340)])]],
}


def write_all():
    img = HERE.parent / "img"
    for name, items, title, desc in (("fig-twelve-questions", questions_items(), "The twelve questions in six parts", ALT_Q),
                                     ("fig-where-prds-fail", fail_items(), "Where PRDs fail", ALT_F)):
        svg = illustration(items, tint=TINT, uid=name, title=title, desc=desc)
        write(svg, img / f"{name}.svg")
        png(svg, img / f"{name}.png", 1200)
    for slug, items in THUMBS.items():
        art = THUMB_ARTICLE[slug]
        png(illustration(items, tint=tint_for_article(art, index=ARTICLES[art]), uid=f"t-{slug}", thumb=True), img / f"{slug}-thumb.png", 600)


def comparison_row():
    return ('<p><a href="../explainers.html">Open the explainer gallery</a>: fourteen figures, from diagrams and charts to an analogy scene and an object, each on a '
            'Printables tint, each shown on the white page and on the near-black page.</p>')


if __name__ == "__main__":
    write_all()
    idx = HERE / "variants" / "index.html"
    s = idx.read_text(encoding="utf-8")
    s = re.sub(r"(<!-- frames:start -->).*?(<!-- frames:end -->)", lambda m: m.group(1) + comparison_row() + m.group(2), s, flags=re.S)
    idx.write_text(s, encoding="utf-8", newline="\n")
    print("wrote figures, thumbnails and backgrounds; refreshed variants/index.html")
