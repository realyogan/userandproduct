"""The Books section mockup: the shelf page and the sample topic page (product management).

Both pages are what WordPress would produce on its own: the shelf from the topic pages (a tile each, grouped by
domain, with the count of books on each), and a topic page from its book posts in the order the owner set. Nothing
on the shelf is picked by hand. The header and footer come from placeholders.py, the single source.

Book facts (title, authors, edition, what each is known for, who it is for, where it has aged, who recommends it)
come from research/books/candidates-2026-10-10.csv; the wording is ours. No quotes from the books, no real covers:
each cover is drawn in code. Book counts on the nine topics that are not built yet are mockup samples.

Run: python build_books.py   (from option-1/build/; writes ../sections/books.html and ../books/product-management.html)
Then: python placeholders.py  (writes the shared placeholder topic page and refreshes the site map)
"""
import random
from html import escape
from pathlib import Path

import placeholders as P

ROOT = Path(__file__).resolve().parent.parent   # option-1/
SHELF = "sections/books.html"
TOPIC_PM = "books/product-management.html"
TOPIC_PH = "books/topic.html"                   # shared placeholder for the nine topic pages not built yet

# ---------- topics: name, group, slug of the thumbnail, books on the page, link, alt ----------
TOPICS = [
    ("UX design", "Design", "books-ux-design", 5, TOPIC_PH, "Illustration of a site tree on a mint square grid."),
    ("UI design", "Design", "books-ui-design", 4, TOPIC_PH, "Illustration of a painter's palette on an orange dot grid."),
    ("UX research", "Design", "books-ux-research", 5, TOPIC_PH, "Line drawing of a magnifier over a screen."),
    ("Product management", "Product", "books-product-management", 5, TOPIC_PM, "Diagram of a roadmap timeline on a light grid."),
    ("Product discovery", "Product", "books-product-discovery", 5, TOPIC_PH, "Illustration of a clipboard with interview notes."),
    ("Project management", "Product", "books-project-management", 4, TOPIC_PH, "Pixel drawing of a loop of arrows in a window."),
    ("Product metrics", "Product", "books-product-metrics", 4, TOPIC_PH, "Line chart of a curve that falls, then flattens."),
    ("Psychology for product people", "Business", "books-psychology", 5, TOPIC_PH, "A glowing light bulb drawn in lines."),
    ("Startups and business", "Business", "books-startups-business", 5, TOPIC_PH, "Illustration of a rocket on a red dot grid."),
    ("Leading product teams", "Business", "books-leading-product-teams", 6, TOPIC_PH, "A stream of dots gathering into a group of three people."),
]
GROUPS = [
    ("Design", "How products look, work and hold up with real people."),
    ("Product", "Deciding what to build, shipping it, and knowing if it worked."),
    ("Business", "The minds, money and teams around the product."),
]

ARTICLE_TITLE = "How to Write a PRD That Engineers Actually Read"

# ---------- the five books, in reading order ----------
# id, title, cover lines, authors, edition line, cover colours (bg, ink, spine, rule), fields, owner_read, reason, read_with
BOOKS = [
    {
        "id": "inspired", "title": "Inspired", "lines": ["Inspired"], "authors": "Marty Cagan",
        "edition": "second edition, 2017", "colors": ("#0D6B5C", "#FFFFFF", "#0A4F44", "#9FE3D3"),
        "covers": "How the best product companies decide what to build. Cagan argues that a product team should test "
                  "ideas with real customers before engineers build them, and should be judged by what changes for "
                  "customers rather than by the number of features shipped. He also sets out what a product manager owns.",
        "for": "Every product manager, new or senior. Designers and engineering leads read it to learn what to expect from their PM.",
        "skip": "PMs who already test ideas with customers every week and have read it once. A second read gives less than the next book here.",
        "key": "The chapters on product discovery: testing an idea cheaply, with prototypes and real users, before it reaches the backlog.",
        "aged": "Still current. Get the second edition (2017), not the 2008 first edition.",
        "read": True,
        "read_with": [("article", "the PRD comes after discovery, not before it"), ("empowered", "the same ideas, for the people who lead teams")],
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
        "read_with": [("inspired", "read it first"), ("working-backwards", "one company's habits, written down")],
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
        "read_with": [("article", "the same habit: write it down before you build"), ("inspired", "the discovery work the press release feeds")],
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
        "read_with": [("article", "a document the whole team reads"), ("inspired", "the bigger picture of the role")],
    },
]
DISCLOSURE = ("Affiliate link: if you buy through it, this site earns a small commission at no extra cost to you. "
              "Commissions never decide which books are on the shelf.")


# ---------- drawn pieces ----------
def spines(seed, w=1440, h=88):
    """A row of book spines standing on the shelf board, drawn once per page from a fixed seed. Decorative."""
    rnd = random.Random(seed)
    x, out = 6, []
    while x < w:
        if rnd.random() < .05:                      # a gap on the shelf
            x += rnd.randint(28, 70)
            continue
        sw, sh = rnd.randint(10, 24), rnd.randint(int(h * .52), h - 2)
        cls = rnd.choice("aabbccdde")
        top = h - sh
        parts = [f'<rect class="sp-{cls}" x="0" y="{top}" width="{sw}" height="{sh}" rx="1.5"/>']
        if cls in "abd" and rnd.random() < .6:      # two bands near the head of the spine
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


def cover(b):
    """A drawn cover card: never the publisher's cover. Title in display type, author at the foot, a spine edge."""
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
    """The section mark: the home page's Books glyph, its first spine in the section green."""
    return ('<svg viewBox="0 0 48 48" width="44" height="44" aria-hidden="true" focusable="false"><path class="bk-mark__fill" d="M10 10h7v30h-7z"/>'
            '<path class="bk-mark__ln" d="M10 10h7v30h-7zM17 14h7v26h-7zM27.5 13.4l6.8-1.8 7.8 29-6.8 1.8zM6 40h37"/>'
            '<path class="bk-mark__ln" d="M10 16h7M17 34h7"/></svg>')


def crumbs(items):
    lis = "".join(f'<li><a href="{h}">{escape(n)}</a></li>' if h else f'<li><span aria-current="page">{escape(n)}</span></li>'
                  for n, h in items)
    return f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{lis}</ol></nav>'


def tile(t, p, h="h3"):
    name, _, slug, n, href, alt = t
    return (f'<li><a class="tt" href="{p}{href}"><img src="{p}img/books/{slug}-thumb.png" width="600" height="338" alt="{escape(alt)}" '
            f'loading="lazy" decoding="async"><{h} class="tt__name">{escape(name)}</{h}><span class="tt__count">{n} books</span></a></li>')


def page(path, title, desc, body_cls, main, shelf_page=False):
    p = "../" * path.count("/")
    head = P.head(p, title, desc).replace(
        f'<link rel="stylesheet" href="{p}css/mockup.css">',
        f'<link rel="preload" href="{p}assets/fonts/satoshi/Satoshi-Variable.woff2" as="font" type="font/woff2" crossorigin>'
        f'\n<link rel="stylesheet" href="{p}css/mockup.css">\n<link rel="stylesheet" href="{p}css/books.css">')
    hdr = P.header(p)
    if shelf_page:   # the shelf page is the Books page itself
        hdr = hdr.replace(f'<a href="{p}sections/books.html">', f'<a href="{p}sections/books.html" aria-current="page">')
    return f'{head}\n{main[0]}\n<body class="bk {body_cls}">\n{hdr}\n<main id="content">\n{main[1]}\n</main>\n{P.footer(p)}'


# ---------- the shelf page ----------
def shelf():
    p = "../"
    groups = []
    for g, line in GROUPS:
        ts = [t for t in TOPICS if t[1] == g]
        gid = f"shelf-{g.lower()}"
        groups.append(f'<section class="shelf" aria-labelledby="{gid}"><div class="shelf__head"><h2 id="{gid}">{g}</h2>'
                      f'<p>{escape(line)} {len(ts)} topics.</p></div>'
                      f'<ul class="shelf__row">{"".join(tile(t, p) for t in ts)}</ul></section>')
    main = f'''<header class="bk-mast">
  <div class="bk-in">
    {crumbs([("Home", p + P.HOME), ("Books", None)])}
    <div class="bk-mast__grid">
      <div class="bk-mark">{mark()}<h1>Books</h1></div>
      <div class="bk-intro">
        <p>These are the books I would hand a colleague. The shelf is for product managers, designers and founders who have time for a few books this year and want the right ones.</p>
        <p>It is grouped by the work: design, product and business. Each topic page holds four to six books in the order I would read them, with who each one is for and who can skip it. Where a book has aged, the page says so.</p>
        <p>My own notes appear only on books I have read, under &ldquo;What I took from it&rdquo;. Every other book says plainly why it is on the shelf.</p>
      </div>
    </div>
  </div>
  {spines(11)}
  <div class="bk-board"></div>
</header>
<div class="bk-in">
  <div class="shelves">
    {"\n    ".join(groups)}
  </div>
  <p class="bk-note">The buy links on the topic pages are affiliate links. If you buy a book through one, this site earns a small commission at no extra cost to you. Commissions never decide which books are on the shelf. The <a href="{p}pages/advertising.html">advertising policy</a> has the details.</p>
</div>'''
    comment = ('<!-- Books shelf page mockup (10 Oct 2026), written by build/build_books.py. What WordPress makes on its own: '
               'one tile per published topic page, grouped by domain, with its book count. Only Product management links to '
               'a built page; the other nine go to the shared placeholder topic page. Counts on those nine are samples. -->')
    return page(SHELF, "Books for product managers, designers and founders",
                "The books worth reading on UX, product management and business, grouped into ten topic pages, with who each book is for and where it has aged.",
                "bk--shelf", (comment, main), shelf_page=True)


# ---------- the topic page ----------
def read_with(b, p):
    by_id = {x["id"]: x for x in BOOKS}
    items = []
    for ref, why in b["read_with"]:
        if ref == "article":
            items.append(f'<li><a href="{p}{P.ARTICLE}">{escape(ARTICLE_TITLE)}</a>: {escape(why)}</li>')
        else:
            items.append(f'<li><a href="#{ref}">{escape(by_id[ref]["title"])}</a>: {escape(why)}</li>')
    return "<ul>" + "".join(items) + "</ul>"


def book(b, i, p):
    hid = f'{b["id"]}-h'
    if b["read"]:
        take = ('<aside class="take" aria-labelledby="' + b["id"] + '-take"><h3 id="' + b["id"] + '-take">What I took from it</h3>'
                '<p class="slot">[Owner writes this after reading]</p></aside>')
    else:
        take = f'<p class="unread">Not yet read by the author; on the shelf because {escape(b["reason"])}</p>'
    q = b["title"].replace(" ", "+") + "+" + b["authors"].split(" and ")[0].replace(" ", "+")
    return f'''<article class="book" id="{b["id"]}" aria-labelledby="{hid}">
  {cover(b)}
  <div class="cat">
    <span class="cat__tab">{i} of {len(BOOKS)} in reading order</span>
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
      <div class="buy"><a class="btn" href="https://www.amazon.com/s?k={q}" rel="sponsored nofollow">Find the book<span class="vh">: {escape(b["title"])}</span></a><p>{DISCLOSURE}</p></div>
    </div>
  </div>
</article>'''


def topic_pm():
    p = "../"
    order = "".join(f'<li><a href="#{b["id"]}" style="--c:{b["colors"][0]}"><span class="n">{i}</span><span class="t">{escape(b["title"])}</span>'
                    f'<span class="a">{escape(b["authors"])}</span></a></li>' for i, b in enumerate(BOOKS, 1))
    neighbours = [t for t in TOPICS if t[0] in ("Product discovery", "Project management")]
    main = f'''<header class="bk-mast bk-mast--topic">
  <div class="bk-in">
    {crumbs([("Home", p + P.HOME), ("Books", p + SHELF), ("Product management", None)])}
    <div class="bk-mast__grid">
      <h1>Books on product management</h1>
      <div class="bk-intro">
        <p>Five books, in the order I would read them. Start with Inspired for how strong product teams work, then Escaping the Build Trap for why most companies drift away from that.</p>
        <p>Empowered is for when you lead other PMs, and Working Backwards gives you one company's habits to copy. Product Management in Practice covers your own week. Each entry says who can skip it, so read only the ones that fit where you are now.</p>
      </div>
    </div>
  </div>
  {spines(23, h=56)}
  <div class="bk-board"></div>
</header>
<div class="bk-in">
  <nav class="order" aria-labelledby="order-h"><h2 id="order-h">The reading order</h2><ol>{order}</ol></nav>
  <div class="books">
{"\n".join(book(b, i, p) for i, b in enumerate(BOOKS, 1))}
  </div>
  <section class="more" aria-labelledby="more-h">
    <h2 id="more-h">More shelves</h2>
    <ul class="shelf__row">{"".join(tile(t, p) for t in neighbours)}</ul>
    <p class="more__all"><a href="{p}{SHELF}">All ten topics on the shelf</a></p>
  </section>
</div>'''
    comment = ('<!-- Books topic page mockup (10 Oct 2026), written by build/build_books.py: the topic page WordPress builds from '
               'its book posts, in the owner\'s order. Every entry has the same parts in the same order. The owner\'s box shows '
               'only on a book he has read (Inspired, as the sample slot). Buy links are affiliate links: rel="sponsored nofollow" '
               'with the disclosure beside each one. Covers are drawn in code, never the publisher\'s. -->')
    return page(TOPIC_PM, "Best product management books: what to read first",
                "Books for product managers, in reading order: the best product management books, who each one is for, what to skip, and where each has aged.",
                "bk--topic", (comment, main))


if __name__ == "__main__":
    for path, html in ((SHELF, shelf()), (TOPIC_PM, topic_pm())):
        f = ROOT / path
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(html, encoding="utf-8", newline="\n")
        print("wrote", path)
