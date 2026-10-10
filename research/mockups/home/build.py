"""Thumbnails for the home page mockup (research/mockups/home/img/).

The sample titles are made up for the mockup. Styles are chosen fit-first (the kind's suitable styles), then
rotated by hand across the page layout so no two neighbouring cards share a style or a colour family:
featured beside the two secondary cards, and the 3 x 3 grid row by row and column by column.
History is not written: these are mockup samples, not published articles.
Run: python build.py   (writes img/<slug>-thumb.png and -check-300.png, the featured piece's -hero.png and .svg,
     recipes.json, and prints a summary)
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "tools"))
import thumbnail as T  # noqa: E402

PIECES = [
    # place, slug, title, subject, kind, style, palette, scheme, reason, extra
    ("featured", "prd-engineers-read", "How to Write a PRD That Engineers Actually Read", "prd", "howto", 1,
     "red-orange", "mono", "a how-to with one nameable object, the document; the flat cut-out reads largest at hero size", {}),
    ("secondary 1", "usability-test-size", "How many users do you need for a usability test?", "usability-test", "concept", 6,
     "night", "mono", "a concept about sample size; the dark line diagram sets it apart from the bright featured card", {}),
    ("secondary 2", "retention-truth", "Retention is the number that tells you the truth", "retention-chart", "data", 8,
     "paper", "duo", "a data piece; the light grid diagram with one accent on the flat part of the curve, unlike the dark card above it", {}),
    ("grid 1", "price-before-customers", "How to price a B2B product before your first customer", "icon:coins", "howto", 3,
     "acid-yellow", "duo", "a how-to; the pixel icon suits a practical method and opens the grid on a bright ground", {"pixel": "money"}),
    ("grid 2", "roadmap-sales-call", "Why most roadmaps break on the first sales call", "roadmap", "opinion", 5,
     "violet", "mono", "an opinion piece; the typographic cover carries a judgment, deep violet beside the yellow", {"cover_title": "The roadmap meets sales", "pixel": "flag"}),
    ("grid 3", "dashboard-one-question", "Dashboard design starts with one question", "icon:gauge", "opinion", 1,
     "tangerine", "mono", "an opinion piece about one object, the gauge; the flat square-grid style on a warm ground", {}),
    ("grid 4", "information-architecture-growth", "Information architecture for a product that keeps growing", "icon:tree-structure", "concept", 9,
     "midnight", "duo", "an abstract concept about scale; the particle field, the stream in the accent", {}),
    ("grid 5", "kanban-or-scrum", "Kanban or Scrum for a team of five", "sprint", "comparison", 2,
     "teal", "mono", "a comparison drawn as the sprint loop; the dot-grid flat style, cool bright between two deep grounds", {}),
    ("grid 6", "product-manager-week", "What a product manager does all week", "icon:lightbulb", "concept", 7,
     "night", "duo", "a concept with one key idea; the glow diagram, the bulb glowing in the accent", {}),
    ("grid 7", "accessibility-afternoon", "Four accessibility checks you can run in an afternoon", "icon:eye", "list", 4,
     "hot-pink", "mono", "a list of four real checks; the icon sequence numbers them", {"steps": ["eye", "cursor", "palette", "check-circle"]}),
    ("grid 8", "design-tokens", "What a design token is, and why engineers ask for them", "design-system", "concept", 10,
     "electric-blue", "duo", "an abstract concept, many small values becoming one system; the bright particle field", {}),
    ("grid 9", "first-product-designer", "Hiring your first product designer", "hiring-guide", "howto", 1,
     "mint", "mono", "a how-to with one object, the briefcase; flat square grid on mint, apart from the dark and blue neighbours", {}),
]


def main():
    out = HERE / "img"
    rows = []
    for place, slug, title, subject, kind, style, palette, scheme, reason, extra in PIECES:
        spec = {"slug": slug, "title": title, "subject": subject, "kind": kind, "style": style,
                "reason": reason, "palette": palette, "scheme": scheme}
        spec.update(extra)
        r = T.make(spec, out, history=False)
        rows.append({"place": place, "slug": slug, "title": title, "kind": r["kind"], "candidates": r["candidates"],
                     "style": r["style"], "style_name": r["style_name"], "palette": r["palette"], "bg": r["bg"],
                     "scheme": r["scheme"], "accents": r["accent_names"], "corner": r["corner"], "reason": reason,
                     "notes": r["notes"], "pass": r["checks"]["pass"]})
        print(f'{place:12} {slug:32} style {r["style"]:>2} {r["palette"]:13} {r["scheme"]:5} pass={r["checks"]["pass"]} {r["notes"]}')
    # the page uses every thumb and only the featured hero; drop the rest (python build.py brings them back)
    for row in rows:
        if row["place"] != "featured":
            for suffix in ("-hero.png", ".svg"):
                (out / f'{row["slug"]}{suffix}').unlink(missing_ok=True)
    (out / "recipes.json").write_text(json.dumps(rows, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
