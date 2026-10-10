"""Topic tile thumbnails for the Books shelf page (option-1/img/books/).

One thumbnail per launch topic page, drawn with research/mockups/tools/thumbnail.py in the house styles. The tiles
sit three or four to a shelf, so styles and grounds are set by hand so no two neighbours on a shelf share either.
The slug is the topic page's slug (books-<topic>). History is not written: these are mockup samples.
Run: python build_books_thumbs.py   (from option-1/build/; writes ../img/books/<slug>-thumb.png and -check-300.png)
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools"))
import thumbnail as T  # noqa: E402

# slug, title, subject, style, palette, scheme, reason, extra
TILES = [
    ("books-ux-design", "Best UX design books", "icon:tree-structure", 1, "mint", "mono",
     "structure is the subject of most UX design classics; flat square grid opens the Design shelf", {}),
    ("books-ui-design", "Best UI design books for product teams", "icon:palette", 2, "tangerine", "mono",
     "visual craft drawn as the palette; dot grid on a warm ground beside the mint", {}),
    ("books-ux-research", "Best UX research books", "usability-test", 6, "night", "duo",
     "research drawn as the magnifier; the dark line diagram closes the shelf on a dark ground", {}),
    ("books-product-management", "Best product management books", "roadmap", 8, "paper", "duo",
     "the roadmap is the object every PM book returns to; light grid diagram opens the Product shelf", {}),
    ("books-product-discovery", "Best product discovery books", "research-plan", 1, "teal", "mono",
     "discovery drawn as the interview clipboard; flat style on teal beside the pale paper", {}),
    ("books-project-management", "Best project management books for product teams", "sprint", 3, "acid-yellow", "duo",
     "delivery drawn as the loop; the pixel window on a bright ground between two calmer tiles", {"pixel": "reload"}),
    ("books-product-metrics", "Best product metrics books", "retention-chart", 6, "midnight", "duo",
     "metrics drawn as the curve; dark line diagram closes the Product shelf", {}),
    ("books-psychology", "Best psychology books for designers and product managers", "icon:lightbulb", 7, "night-plum", "duo",
     "one idea at a time is what these books give; the glow diagram opens the Business shelf", {}),
    ("books-startups-business", "Best startup and business books for product people", "icon:rocket-launch", 2, "red-orange", "mono",
     "a launch is the startup object; dot grid flat style on a bright ground beside the dark tile", {}),
    ("books-leading-product-teams", "Best leadership books for product leaders and managers", "icon:users-three", 10, "violet", "duo",
     "a team is the subject; the bright particle field gathers into the group", {}),
]


def main():
    out = HERE.parent / "img" / "books"
    for slug, title, subject, style, palette, scheme, reason, extra in TILES:
        spec = {"slug": slug, "title": title, "subject": subject, "kind": "list", "style": style,
                "palette": palette, "scheme": scheme, "reason": reason}
        spec.update(extra)
        r = T.make(spec, out, history=False)
        print(f'{slug:30} style {r["style"]:>2} {r["palette"]:12} {r["scheme"]:5} pass={r["checks"]["pass"]} {r["notes"]}')
        for suffix in ("-hero.png", ".svg"):
            (out / f"{slug}{suffix}").unlink(missing_ok=True)


if __name__ == "__main__":
    main()
