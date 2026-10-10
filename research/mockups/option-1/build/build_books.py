"""The Books section mockup: the shelf page and the sample topic page (product management).

Both pages are what WordPress would produce on its own: the shelf from the topic pages (a tile each, grouped by
domain, with the count of books on each), and a topic page that lists its book posts. Books are simply listed, with
no reading order, so a page reads the same with four books or fourteen. Nothing on the shelf is picked by hand: a tile shows the covers of its topic's first three books.

Colour: each topic owns one of the eight Printables tints (research/mockups/illustration-rules.md), given in shelf
order so neighbours differ, and keeps it on its own page (masthead and accents). Each book entry on a topic page also
carries a quiet accent taken from its own cover. The header and footer come from placeholders.py, the single source.

Book facts (title, authors, edition, what each is known for, who it is for, where it has aged, who recommends it)
come from research/books/candidates-2026-10-10.csv; the wording is ours. No quotes from the books. Book counts on
the nine topics that are not built yet are mockup samples.

Covers: Open Library (openlibrary.org) is the source for the mockup. Each book with a confirmed Open Library cover
for the named edition shows it from our own copy in img/books/covers/ (medium for 1x, large for 2x screens; fetched
once, listed with ISBN, cover id and source URL in that folder's README.md, and kept out of git because the art is
the publishers' copyright). A book without one falls back to the cover card drawn in code. At launch the covers
switch to the affiliate program's licensed images. The page carries no cover caption; the source is recorded only in
that README.

Run: python build_books.py   (from option-1/build/; writes ../sections/books.html and ../books/product-management.html)
Then: python placeholders.py  (writes the shared placeholder topic page and refreshes the site map)
"""
import colorsys
import csv
import random
from html import escape
from pathlib import Path

from PIL import Image

import placeholders as P

ROOT = Path(__file__).resolve().parent.parent   # option-1/
SHELF = "sections/books.html"
TOPIC_PM = "books/product-management.html"
TOPIC_PH = "books/topic.html"                   # shared placeholder for the nine topic pages not built yet

# ---------- topics: name, group, books on the page, link, category in the candidates CSV ----------
TOPICS = [
    ("UX design", "Design", 5, TOPIC_PH, "UX design"),
    ("UI design", "Design", 4, TOPIC_PH, "UI design"),
    ("UX research", "Design", 5, TOPIC_PH, "UX research"),
    ("Product management", "Product", 5, TOPIC_PM, "Product management"),
    ("Product discovery", "Product", 5, TOPIC_PH, "Product discovery"),
    ("Project management", "Product", 4, TOPIC_PH, "Project management"),
    ("Product metrics", "Product", 4, TOPIC_PH, "Product metrics"),
    ("Psychology for product people", "Business", 5, TOPIC_PH, "Psychology and behavioral science"),
    ("Startups and business", "Business", 5, TOPIC_PH, "Business and entrepreneurship"),
    ("Leading product teams", "Business", 6, TOPIC_PH, "Leadership and teams"),
]
# The eight Printables tints, handed out in shelf order: with eight in the cycle, a tile never shares a colour with the
# tile beside it or (at two, three or four columns) the one above it. A topic keeps its tint on its own page.
TINTS = ["teal", "yellow", "pink", "blue", "green", "purple", "peach", "slate"]


def tint(name):
    return TINTS[[t[0] for t in TOPICS].index(name) % len(TINTS)]


GROUPS = [
    ("Design", "How products look, work and hold up with real people."),
    ("Product", "Deciding what to build, shipping it, and knowing if it worked."),
    ("Business", "The minds, money and teams around the product."),
]

CANDIDATES = ROOT.parent.parent / "books" / "candidates-2026-10-10.csv"
COVERS_CSV = ROOT.parent.parent / "books" / "covers-2026-10-10.csv"   # ISBN, Open Library cover id, file, size per book
COVER_DIR = ROOT / "img" / "books" / "covers"


def load_covers():
    """Title -> cover record, only for books whose cover files are on disk (a confirmed Open Library cover)."""
    out = {}
    if COVERS_CSV.exists():
        for r in csv.DictReader(COVERS_CSV.open(encoding="utf-8")):
            if (r["status"] == "ok" and (COVER_DIR / r["file"]).exists()
                    and (COVER_DIR / r["file"].replace("-cover.jpg", "-cover-2x.jpg")).exists()):
                r["lh"] = Image.open(COVER_DIR / r["file"].replace("-cover.jpg", "-cover-2x.jpg")).size[1]
                out[r["title"]] = r
    return out


COVERS = load_covers()
CANDS = list(csv.DictReader(CANDIDATES.open(encoding="utf-8")))


def topic_covers(t, n=3):
    """The first n books of a topic that have a sharp cover (large file 400 px tall or more): as listed on a built
    page, else tier A, B, C. Low-resolution covers still show on a book's own entry, never on a tile."""
    if t[3] == TOPIC_PM:
        titles = [b["title"] for b in BOOKS]
    else:
        rows = sorted((r for r in CANDS if r["category"] == t[4]), key=lambda r: (r["tier"], int(r["id"])))
        titles = [r["title"] for r in rows]
    return [COVERS[x] for x in titles if x in COVERS and COVERS[x]["lh"] >= 400][:n]


def _hex(rgb):
    return "#" + "".join(f"{round(c * 255):02X}" for c in rgb)


def _lum(rgb):
    c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in rgb]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]


def _contrast(a, b):
    la, lb = sorted((_lum(a), _lum(b)), reverse=True)
    return (la + .05) / (lb + .05)


def cover_accent(rec):
    """A restrained tone from the cover: its most common colour that is neither near white nor near black, with the
    saturation capped, then made dark (light theme) or light (dark theme) enough to read as a 3:1 line on the page.
    Returns None when the cover is all neutrals; the entry then uses the topic's accent."""
    im = Image.open(COVER_DIR / rec["file"]).convert("RGB").resize((60, 90)).quantize(8)
    pal = im.getpalette()
    best = None
    for count, i in sorted(im.getcolors(), reverse=True):
        r, g, b = (pal[i * 3 + k] / 255 for k in range(3))
        h, l, sat = colorsys.rgb_to_hls(r, g, b)
        if .12 < l < .9 and sat > .28:
            best = (h, sat)
            break
    if not best:
        return None
    h, sat = best[0], min(best[1], .5)

    def fit(bg, step):
        l = .5
        while _contrast(colorsys.hls_to_rgb(h, l, sat), bg) < 3 and 0 < l < 1:
            l += step
        return _hex(colorsys.hls_to_rgb(h, l, sat))
    return fit((1, 1, 1), -.02), fit((11 / 255, 11 / 255, 12 / 255), .02)



# ---------- the five books, as listed on the page ----------
# id, title, cover lines, authors, edition line, cover colours (bg, ink, spine, rule), fields, owner_read, reason, read_with
BOOKS = [
    {
        "id": "inspired", "title": "Inspired", "lines": ["Inspired"], "authors": "Marty Cagan",
        "edition": "second edition, 2017", "colors": ("#0D6B5C", "#FFFFFF", "#0A4F44", "#9FE3D3"),
        "covers": "How the best product companies decide what to build. Cagan argues that a product team should test "
                  "ideas with real customers before engineers build them, and should be judged by what changes for "
                  "customers rather than by the number of features shipped. He also sets out what a product manager owns.",
        "for": "Every product manager, new or senior. Designers and engineering leads read it to learn what to expect from their PM.",
        "skip": "PMs who already test ideas with customers every week and have read it once. A second read gives less than a book you have not read yet.",
        "key": "The chapters on product discovery: testing an idea cheaply, with prototypes and real users, before it reaches the backlog.",
        "aged": "Still current. Get the second edition (2017), not the 2008 first edition.",
        "read": True,
        "read_with": [("empowered", "the same ideas, for the people who lead teams"), ("working-backwards", "one company's way of testing an idea on paper first")],
    },
    {
        "id": "build-trap", "title": "Escaping the Build Trap", "lines": ["Escaping", "the Build", "Trap"], "authors": "Melissa Perri",
        "edition": "2018", "colors": ("#E6F0EB", "#0B1F1A", "#0D6B5C", "#0D6B5C"),
        "covers": "The build trap is a company that measures itself by what it ships instead of what changes for customers. "
                  "Perri shows how teams fall into it and how they climb out: set outcomes, give product managers room to "
                  "decide, and connect the company's strategy to the work of each team.",
        "for": "PMs and leaders in a feature factory: a company where the roadmap is a list of promised features and nobody checks what they did.",
        "skip": "Teams that already plan around outcomes and review them every quarter. You will recognize most of it.",
        "key": "The chapters on strategy: how one company goal becomes goals that each team can act on.",
        "aged": "Still current.",
        "read": False, "reason": "Lenny's Newsletter, Mind the Product and Giff Constable all recommend it.",
        "read_with": [("inspired", "what a strong team looks like"), ("empowered", "what its leaders do differently")],
    },
    {
        "id": "empowered", "title": "Empowered", "lines": ["Empowered"], "authors": "Marty Cagan and Chris Jones",
        "edition": "2020", "colors": ("#17191A", "#F1EEE7", "#0D6B5C", "#5CCFB8"),
        "covers": "The companion to Inspired, written for the people who lead product teams. It sets feature teams, which "
                  "are handed a list of things to build, against empowered teams, which are handed a problem and trusted "
                  "to solve it. Most of the book is the leader's side: coaching, hiring, and a vision and strategy the teams can act on.",
        "for": "Heads of product, directors, and anyone who manages product managers.",
        "skip": "A PM in the first year with nobody reporting to them. Read Inspired now and come back to this when you lead people.",
        "key": "The chapters on coaching product managers, a part of the job most leaders were never taught.",
        "aged": "Still current.",
        "read": False, "reason": "Lenny's Newsletter, Mind the Product and Productboard all recommend it.",
        "read_with": [("inspired", "the ideas it builds on"), ("working-backwards", "one company's habits, written down")],
    },
    {
        "id": "working-backwards", "title": "Working Backwards", "lines": ["Working", "Backwards"], "authors": "Colin Bryar and Bill Carr",
        "edition": "2021", "colors": ("#BFE3D7", "#0B1F1A", "#0A4F44", "#0A4F44"),
        "covers": "Two former Amazon executives describe the habits Amazon runs on. The best known is writing the press "
                  "release, and the questions a customer would ask, before anything gets built. The book also covers "
                  "six-page memos in place of slide decks, leaders who own one thing full time, and the numbers that move before revenue does.",
        "for": "PMs and leaders who want working habits they can copy, with the reason behind each one.",
        "skip": "Readers looking for a theory of product management. These are one company's practices, and a few depend on Amazon's size.",
        "key": "The chapters on the press release and the six-page memo. They change how a team writes before it builds.",
        "aged": "Still current.",
        "read": False, "reason": "it is in SVPG's top ten product books and on Lenny's Newsletter's essential list.",
        "read_with": [("inspired", "the discovery work the press release feeds"), ("build-trap", "why the habit matters: judging work by outcomes")],
    },
    {
        "id": "in-practice", "title": "Product Management in Practice", "lines": ["Product", "Management", "in Practice"],
        "authors": "Matt LeMay", "edition": "second edition, 2022", "colors": ("#0A4F44", "#EAF6F2", "#062F29", "#9FE3D3"),
        "covers": "The day-to-day job as people live it, not as job ads describe it. LeMay puts communication first: most "
                  "of a PM's work is getting the right people to understand the same thing. He groups the rest under "
                  "organization, research and execution.",
        "for": "New and aspiring PMs, and anyone moving into the role from design, engineering or support.",
        "skip": "Senior PMs who already run the job well. The book names good habits; you will have most of them.",
        "key": "The chapters on communication, with plain advice for the meetings and messages that go wrong.",
        "aged": "Still current. Get the second edition (2022).",
        "read": False, "reason": "Mind the Product and Productboard both recommend it.",
        "read_with": [("inspired", "the bigger picture of the role"), ("build-trap", "what goes wrong when the job shrinks to shipping")],
    },
]
DISCLOSURE = ("Affiliate link: if you buy through it, this site earns a small commission at no extra cost to you. "
              "Commissions never decide which books are on the shelf.")


# ---------- drawn pieces ----------
def spines(seed, w=1440, h=88):
    """A row of book spines standing on the shelf board, drawn once per page from a fixed seed. Decorative. The six
    fills come from the band's spine palette (--sp1 to --sp6 in books.css), so each tint gets its own set."""
    rnd = random.Random(seed)
    x, out = 6, []
    while x < w:
        if rnd.random() < .05:                      # a gap on the shelf
            x += rnd.randint(28, 70)
            continue
        sw, sh = rnd.randint(10, 24), rnd.randint(int(h * .52), h - 2)
        cls = rnd.choice("1122334455666")
        top = h - sh
        parts = [f'<rect class="sp-{cls}" x="0" y="{top}" width="{sw}" height="{sh}" rx="1.5"/>']
        if rnd.random() < .45:                      # two bands near the head of the spine
            parts.append(f'<rect class="sp-band" x="2" y="{top + 7}" width="{sw - 4}" height="2"/>'
                         f'<rect class="sp-band" x="2" y="{top + 12}" width="{sw - 4}" height="1"/>')
        if rnd.random() < .05 and sh < h - 10:      # one book leaning on its neighbour
            out.append(f'<g transform="translate({x} 0) rotate(9 0 {h})">{"".join(parts)}</g>')
            x += sw + int(sh * .16) + 3
        else:
            out.append(f'<g transform="translate({x} 0)">{"".join(parts)}</g>')
            x += sw + 2
    return (f'<svg class="spines" viewBox="0 0 {w} {h}" preserveAspectRatio="xMinYMax slice" aria-hidden="true" focusable="false">'
            + "".join(out) + "</svg>")


def small_cover(rec):
    """A 240 px wide copy of the large cover for the shelf tiles and the masthead stand, where a cover shows at about
    100 css px: sharp at 2x, about a third of the large file's weight. Made once from the large file, kept beside it
    (git-ignored like the covers)."""
    big = COVER_DIR / rec["file"].replace("-cover.jpg", "-cover-2x.jpg")
    out = COVER_DIR / rec["file"].replace("-cover.jpg", "-cover-sm.jpg")
    if not out.exists() or out.stat().st_mtime < big.stat().st_mtime:
        im = Image.open(big).convert("RGB")
        if im.width > 240:
            im = im.resize((240, round(im.height * 240 / im.width)), Image.LANCZOS)
        im.save(out, "JPEG", quality=84, optimize=True, progressive=True)
    return out.name


def cover_img(rec, p, alt, small=False):
    """Our copy of a book's Open Library cover. The large file serves every screen density: the medium one (180 px)
    goes soft once the tilt or a zoom enlarges it, and covers are shown at 250 css px or less. Width and height carry
    the cover's own ratio so the layout does not jump. Open Library is the source for the mockup; at launch covers
    switch to the affiliate program's licensed images."""
    src = f'{p}img/books/covers/{small_cover(rec) if small else rec["file"][:-4] + "-2x.jpg"}'
    return (f'<img src="{src}" width="{rec["w"]}" height="{rec["h"]}" '
            f'alt="{escape(alt)}" loading="lazy" decoding="async">')


def cover(b, p):
    """The book's cover on its entry: our copy of the Open Library cover, or the drawn card when there is none."""
    rec = COVERS.get(b["title"])
    if rec:
        alt = f'Cover of {b["title"]} by {b["authors"]}'
        # a book in 3D: the cover on the front face, a hinge on the left, page edges on the right (CSS only);
        # books.js lets it settle in when it scrolls into view. No caption: the source is in the covers README.
        return f'<figure class="cover"><span class="b3d">{cover_img(rec, p, alt)}</span></figure>'
    return drawn_cover(b)


def drawn_cover(b):
    """The fallback cover card, drawn in code: title in display type, author at the foot, a spine edge."""
    bg, ink, spine, rule = b["colors"]
    tid = f'cv-{b["id"]}'
    size = 30 if max(len(l) for l in b["lines"]) <= 8 else 24
    lines = "".join(f'<text class="cv-t" x="38" y="{92 + i * (size + 4)}" font-size="{size}" fill="{ink}">{escape(l)}</text>'
                    for i, l in enumerate(b["lines"]))
    names = b["authors"].split(" and ")
    names = [names[0]] + [f"and {x}" for x in names[1:]]          # a second author goes on its own line
    by = "".join(f'<text class="cv-a" x="38" y="{270 - (len(names) - 1 - j) * 16}" font-size="12" fill="{ink}">{escape(a)}</text>'
                 for j, a in enumerate(names))
    return (f'<figure class="cover"><svg viewBox="0 0 200 300" width="200" height="300" role="img" aria-labelledby="{tid}">'
            f'<title id="{tid}">Drawn cover card for {escape(b["title"])} by {escape(b["authors"])}</title>'
            f'<rect width="200" height="300" fill="{bg}"/><rect width="16" height="300" fill="{spine}"/>'
            f'<rect x="16" width="2" height="300" fill="{ink}" opacity=".12"/>'
            f'<rect x="38" y="44" width="40" height="4" fill="{rule}"/>{lines}{by}</svg>'
            '<figcaption>Drawn for this page, not the publisher&rsquo;s cover.</figcaption></figure>')


def mark():
    """The section mark: the home page's Books glyph, drawn in ink."""
    return ('<svg viewBox="0 0 48 48" width="44" height="44" aria-hidden="true" focusable="false"><path class="bk-mark__fill" d="M10 10h7v30h-7z"/>'
            '<path class="bk-mark__ln" d="M10 10h7v30h-7zM17 14h7v26h-7zM27.5 13.4l6.8-1.8 7.8 29-6.8 1.8zM6 40h37"/>'
            '<path class="bk-mark__ln" d="M10 16h7M17 34h7"/></svg>')


def crumbs(items):
    lis = "".join(f'<li><a href="{h}">{escape(n)}</a></li>' if h else f'<li><span aria-current="page">{escape(n)}</span></li>'
                  for n, h in items)
    return f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{lis}</ol></nav>'


def plate(t, p, h="h3"):
    """A topic tile: the topic's tint as the ground, its name and count, and the covers of its first three books
    standing in a staggered row along the foot. The covers are decoration inside the link; the name labels it."""
    name, _, n, href, _ = t
    covers = "".join(f'<span class="tp__bk">{cover_img(rec, p, "", small=True)}</span>' for rec in topic_covers(t))
    return (f'<li><a class="tp t-{tint(name)}" href="{p}{href}"><{h} class="tp__name">{escape(name)}</{h}>'
            f'<span class="tp__count">{n} books</span><span class="tp__covers" aria-hidden="true">{covers}</span></a></li>')


def page(path, title, desc, body_cls, main, shelf_page=False):
    p = "../" * path.count("/")
    head = P.head(p, title, desc).replace(
        f'<link rel="stylesheet" href="{p}css/mockup.css">',
        f'<link rel="preload" href="{p}assets/fonts/satoshi/Satoshi-Variable.woff2" as="font" type="font/woff2" crossorigin>'
        f'\n<link rel="stylesheet" href="{p}css/mockup.css">\n<link rel="stylesheet" href="{p}css/books.css">')
    hdr = P.header(p)
    if shelf_page:   # the shelf page is the Books page itself
        hdr = hdr.replace(f'<a href="{p}sections/books.html">', f'<a href="{p}sections/books.html" aria-current="page">')
    if "bk--topic" in body_cls:   # the settle-in motion for the 3D covers; the page reads the same without it
        head = head.replace(f'<script src="{p}js/mockup.js" defer></script>',
                            f'<script src="{p}js/mockup.js" defer></script><script src="{p}js/books.js" defer></script>')
    return f'{head}\n{main[0]}\n<body class="bk {body_cls}">\n{hdr}\n<main id="content">\n{main[1]}\n</main>\n{P.footer(p)}'


# ---------- the shelf page ----------
SHELF_SEED = 54   # a fixed seed: the same row on every build, with few gaps


def shelf():
    p = "../"
    groups = []
    for g, line in GROUPS:
        ts = [t for t in TOPICS if t[1] == g]
        gid = f"shelf-{g.lower()}"
        groups.append(f'<section class="shelf" aria-labelledby="{gid}"><div class="shelf__head"><h2 id="{gid}">{g}</h2>'
                      f'<p>{escape(line)} {len(ts)} topics.</p></div>'
                      f'<ul class="plates">{"".join(plate(t, p) for t in ts)}</ul></section>')
    main = f'''<header class="bk-mast">
  <div class="bk-in">
    {crumbs([("Home", p + P.HOME), ("Recommended books", None)])}
    <div class="bk-mast__grid">
      <div class="bk-mark">{mark()}<h1>Recommended books</h1></div>
      <div class="bk-intro">
        <p>These are the books I would hand a colleague. The shelf is for product managers, designers and founders who have time for a few books this year and want the right ones.</p>
        <p>It is grouped by the work: design, product and business. Each topic page holds a handful of books, with who each one is for and who can skip it. Where a book has aged, the page says so.</p>
      </div>
    </div>
  </div>
  {spines(SHELF_SEED, h=64)}
  <div class="bk-board"></div>
</header>
<div class="bk-in">
  <div class="shelves">
    {"\n    ".join(groups)}
  </div>
  <!-- affiliate links parked (owner, 10 Oct 2026) -->
</div>'''
    comment = ('<!-- Books shelf page mockup (10 Oct 2026), written by build/build_books.py. What WordPress makes on its own: '
               'one tile per published topic page, grouped by domain, with its book count and the covers of its first three '
               'books. Each topic has its own tint. Only Product management links to a built page; the other nine go to '
               'the shared placeholder topic page. Counts on those nine are samples. -->')
    return page(SHELF, "Recommended books on UX, product management and business",
                "The books worth reading on UX, product management and business, grouped by topic, with who each book is for and where it has aged.",
                "bk--shelf", (comment, main), shelf_page=True)


# ---------- the topic page ----------
def read_with(b, p):
    """Links to other books only (on this page; later also books on other topic pages), never to articles."""
    by_id = {x["id"]: x for x in BOOKS}
    items = [f'<li><a href="#{ref}">{escape(by_id[ref]["title"])}</a>: {escape(why)}</li>' for ref, why in b["read_with"]]
    return "<ul>" + "".join(items) + "</ul>"


def book(b, p):
    hid = f'{b["id"]}-h'
    if b["read"]:
        take = ''
    else:
        take = ''
    q = b["title"].replace(" ", "+") + "+" + b["authors"].split(" and ")[0].replace(" ", "+")
    rec = COVERS.get(b["title"])
    acc = cover_accent(rec) if rec else None
    style = f' style="--ba:{acc[0]};--ba-d:{acc[1]}"' if acc else ""
    return f'''<article class="book" id="{b["id"]}" aria-labelledby="{hid}"{style}>
  {cover(b, p)}
  <div class="cat">
    <div class="cat__card">
      <h2 id="{hid}">{escape(b["title"])}</h2>
      <p class="cat__by">{escape(b["authors"])}<span>, {escape(b["edition"])}</span></p>
      <dl class="fields">
        <div><dt>What it covers</dt><dd>{escape(b["covers"])}</dd></div>
        <div><dt>Who it is for</dt><dd>{escape(b["for"])}</dd></div>
        <div><dt>Who can skip it</dt><dd>{escape(b["skip"])}</dd></div>
        <div class="key"><dt>The part that matters most</dt><dd>{escape(b["key"])}</dd></div>
        <div><dt>Where it has aged</dt><dd>{escape(b["aged"])}</dd></div>
      </dl>
      {take}
      <dl class="fields">
        <div><dt>Read it with</dt><dd>{read_with(b, p)}</dd></div>
      </dl>
    </div>
  </div>
</article>'''


def topic_pm():
    p = "../"
    neighbours = [t for t in TOPICS if t[0] in ("Product discovery", "Project management")]
    main = f'''<header class="bk-mast bk-mast--topic">
  <div class="bk-in">
    {crumbs([("Home", p + P.HOME), ("Recommended books", p + SHELF), ("Product management", None)])}
    <div class="bk-mast__grid">
      <h1>Books on product management</h1>
      <div class="bk-intro">
        <p>These are the product management books I would hand a colleague. Inspired shows how strong product teams work, and Escaping the Build Trap shows why most companies drift away from that.</p>
        <p>Empowered is for when you lead other PMs, Working Backwards gives you one company's habits to copy, and Product Management in Practice covers your own week. Each entry says who the book is for and who can skip it, so read only the ones that fit where you are now.</p>
      </div>
    </div>
  </div>
  {spines(23, h=64)}
  <div class="bk-board"></div>
</header>
<div class="bk-in">
  <div class="books">
{"\n".join(book(b, p) for b in BOOKS)}
  </div>
  <section class="more" aria-labelledby="more-h">
    <h2 id="more-h">More shelves</h2>
    <ul class="plates plates--more">{"".join(plate(t, p) for t in neighbours)}</ul>
    <p class="more__all"><a href="{p}{SHELF}">Back to all recommended books</a></p>
  </section>
</div>'''
    comment = ('<!-- Books topic page mockup (10 Oct 2026), written by build/build_books.py: the topic page WordPress builds from '
               'its book posts, simply listed (no reading order). Every entry has the same parts in the same order. The owner\'s box shows '
               'only on a book he has read (Inspired, as the sample slot). Buy links are affiliate links: rel="sponsored nofollow" '
               'with the disclosure beside each one. The page takes its topic\'s tint; each entry a quiet accent from its cover. -->')
    return page(TOPIC_PM, "Best product management books for product managers",
                "The best product management books for product managers: what each one covers, who it is for, who can skip it, and where each book has aged.",
                f"bk--topic t-{tint('Product management')}", (comment, main))


if __name__ == "__main__":
    for path, html in ((SHELF, shelf()), (TOPIC_PM, topic_pm())):
        f = ROOT / path
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(html, encoding="utf-8", newline="\n")
        print("wrote", path)
