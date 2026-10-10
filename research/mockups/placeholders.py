"""Shared page shell for the mockups, the placeholder pages and the site map.

Every mockup page links to every other, so the mockups can be clicked through as one site. This file holds the
link targets (paths from research/mockups/), the shared header and footer, and one template for placeholder pages.

Run: python placeholders.py
  - writes each placeholder page in PLACEHOLDERS, but only if the file is missing or is still a placeholder
    (a built page never gets overwritten; placeholders carry data-placeholder on <body>)
  - writes index.html, the site map, with each page's status read from the files (built or placeholder)
Reuse: import placeholders; placeholders.header(prefix) / footer(prefix) give the shared markup with links
resolved from a page that is `prefix` away from research/mockups/ ("../" for a page one folder down).
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# link targets, as paths from research/mockups/
NAV = [("Articles", "home/index.html#latest"), ("Topics", "category/index.html"), ("Books", "sections/books.html"),
       ("Links", "sections/links.html"), ("Tools", "sections/tools.html"), ("Templates", "sections/templates.html")]
DOMAINS = [("Design", "category/index.html"), ("Product", "category/index.html"), ("Business", "category/index.html")]
LEGAL = [("About", "pages/about.html"), ("Privacy", "pages/privacy.html"),
         ("Advertising policy", "pages/advertising.html"), ("Contact", "pages/contact.html")]
HOME = "home/index.html"

# placeholder pages: path, title, h1, one line
PLACEHOLDERS = [
    ("category/index.html", "Category", "Category page (coming)", "The category page is the next mockup. It will list one topic's articles, grouped under headings."),
    ("sections/articles.html", "All articles", "All articles (coming)", "Every article, newest first, a page at a time. Until then, the latest twelve are on the home page."),
    ("sections/books.html", "Books", "Books (coming)", "The books I hand to colleagues, with a note on what each one is good for."),
    ("sections/links.html", "Links", "Links (coming)", "Useful sites and apps for design and product work, sorted by topic."),
    ("sections/tools.html", "Tools", "Tools (coming)", "Small calculators and checkers for everyday product work."),
    ("sections/templates.html", "Templates", "Templates (coming)", "Free templates to download, each with a worked example beside it."),
    ("pages/about.html", "About", "About (coming)", "Who writes this site, and the fifteen years of work behind it."),
    ("pages/privacy.html", "Privacy", "Privacy (coming)", "What the site collects, why, and how to have it removed."),
    ("pages/advertising.html", "Advertising policy", "Advertising policy (coming)", "Where ads appear, how they are labelled, and how affiliate links work."),
    ("pages/contact.html", "Contact", "Contact (coming)", "How to reach the author."),
]

# site map: path, name, what it is (status is read from the file)
SITEMAP = [
    ("home/index.html", "Home", "Latest articles, topics, links to the sections."),
    ("article/index.html", "Article page variants", "The three single-article layouts side by side."),
    ("article/article-a.html", "Article A, Sidebar", "The sample PRD article with a right rail."),
    ("article/article-b.html", "Article B, Magazine", "The same article, magazine layout."),
    ("article/article-c.html", "Article C, Reader", "The same article, reading layout."),
    ("article/explainers.html", "Explainer gallery", "The explainer figures drawn for the sample article."),
] + [(p, t, line) for p, t, _, line in PLACEHOLDERS] + [
    ("final-logo/brand-sheet.html", "Brand sheet", "The final logo, its colours and sizes (reference)."),
    ("references/blog-thumbnails/index.html", "Thumbnail styles", "The reference thumbnails sorted into styles (reference)."),
]


def _lis(items, p):
    return "".join(f'<li><a href="{p}{href}">{name}</a></li>' for name, href in items)


def head(p, title, desc):
    return f'''<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | userandproduct</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex"><meta name="theme-color" content="#2B46A0">
<link rel="icon" href="{p}final-logo/favicon/favicon.ico" sizes="48x48"><link rel="icon" href="{p}final-logo/favicon/favicon.svg" type="image/svg+xml">
<script>try{{var t=localStorage.getItem("uap-theme");if(t==="dark"||t==="light"){{document.documentElement.setAttribute("data-theme",t)}}}}catch(e){{}}</script>
<link rel="stylesheet" href="{p}mockup.css"><script src="{p}mockup.js" defer></script>
</head>'''


def header(p):
    nav = _lis(NAV, p)
    return f'''<a class="skip" href="#content">Skip to the main content</a><header class="site-head">
  <div class="site-head__in">
    <a class="logo" href="{p}{HOME}" aria-label="userandproduct home"><img class="l-light" src="{p}final-logo/svg/lockup-light.svg" alt="userandproduct" width="236" height="30"><img class="l-dark" src="{p}final-logo/svg/lockup-dark.svg" alt="userandproduct" width="236" height="30"></a>
    <nav class="site-nav" aria-label="Sections"><ul>{nav}</ul></nav>
    <details class="menu"><summary>Menu</summary><ul>{nav}</ul></details>
    <button class="theme-toggle" type="button" data-theme-toggle aria-label="Switch theme"><svg class="i-moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" d="M20.3 14.6A8.5 8.5 0 0 1 9.4 3.7a8.5 8.5 0 1 0 10.9 10.9Z"/></svg><svg class="i-sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.5" fill="currentColor"/><g stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 2v2.5M12 19.5V22M2 12h2.5M19.5 12H22M4.9 4.9l1.8 1.8M17.3 17.3l1.8 1.8M4.9 19.1l1.8-1.8M17.3 6.7l1.8-1.8"/></g></svg></button>
  </div>
</header>'''


def footer(p):
    legal = "".join(f'<a href="{p}{href}">{name}</a>' for name, href in LEGAL)
    return f'''<footer class="site-foot">
  <div class="site-foot__in">
    <div class="site-foot__brand"><a class="logo" href="{p}{HOME}" aria-label="userandproduct home"><img class="l-light" src="{p}final-logo/svg/lockup-light.svg" alt="userandproduct" width="168" height="21"><img class="l-dark" src="{p}final-logo/svg/lockup-dark.svg" alt="userandproduct" width="168" height="21"></a><p>Practical writing on UX, product management and the business decisions between them, from fifteen years of shipping software.</p></div>
    <nav aria-label="Domains"><h2>Domains</h2><ul>{_lis(DOMAINS, p)}</ul></nav>
    <nav aria-label="Site sections"><h2>Sections</h2><ul>{_lis(NAV, p)}</ul></nav>
    <div class="legal"><span>&copy; 2026 userandproduct</span>{legal}</div>
  </div>
</footer>
</body>
</html>
'''


STYLE = ('<style>.ph{max-width:var(--frame,1280px);margin:0 auto;padding:var(--s8) var(--gutter) 0}'
         '.ph h1{font-size:clamp(32px,calc(16px + 3vw),52px);line-height:1.08;letter-spacing:-.03em}'
         '.ph>p{margin-top:var(--s4);font:400 var(--fs-lead)/1.5 var(--font-ui);color:var(--ink-2);max-width:34em}'
         '.ph .back{font:600 var(--fs-ui)/1.4 var(--font-ui)}</style>')


def placeholder(path, title, h1, line):
    p = "../" * path.count("/")
    return (head(p, title, line).replace("</head>", STYLE + "\n</head>")
            + '\n<!-- Placeholder page, written by research/mockups/placeholders.py. Replace it with the real mockup. -->'
            f'\n<body data-placeholder>\n{header(p)}\n<main id="content" class="ph">\n  <h1>{h1}</h1>\n  <p>{line}</p>'
            f'\n  <p class="back"><a href="{p}{HOME}">Back to the home page</a> &middot; <a href="{p}index.html">All mockup pages</a></p>'
            f'\n</main>\n{footer(p)}')


def status(path):
    f = ROOT / path
    if not f.exists():
        return "missing"
    return "placeholder" if "<body data-placeholder" in f.read_text(encoding="utf-8") else "built"


def sitemap():
    rows = []
    for path, name, what in SITEMAP:
        s = status(path)
        chip = "chip chip--cat" if s == "built" else "chip"
        rows.append(f'    <li><a href="{path}">{name}</a><span class="{chip}">{s}</span>'
                    f'<span class="sm__what">{what}</span><span class="sm__path">{path}</span></li>')
    css = STYLE.replace("</style>", '.sm{list-style:none;margin:var(--s6) 0 0;padding:0;max-width:52em}'
                        '.sm li{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:var(--s1) var(--s4);padding:var(--s4) 0;'
                        'border-bottom:1px solid var(--rule);font:400 var(--fs-ui)/1.5 var(--font-ui)}'
                        '.sm a{font-weight:600}.sm .chip{align-self:start}'
                        '.sm__what{grid-column:1/-1;color:var(--ink-2)}'
                        '.sm__path{grid-column:1/-1;font:500 12px/1.4 var(--font-mono);color:var(--ink-3);overflow-wrap:anywhere}</style>')
    return (head("", "Mockup pages", "Every mockup page for userandproduct.com, with its status.").replace("</head>", css + "\n</head>")
            + '\n<!-- Site map of the mockups, written by research/mockups/placeholders.py from the files on disk. -->'
            f'\n<body>\n{header("")}\n<main id="content" class="ph">\n  <h1>Mockup pages</h1>'
            '\n  <p>Every page in the mockups, linked as one site. Built pages are real mockups; placeholders hold the link until their page is made.</p>'
            '\n  <ul class="sm">\n' + "\n".join(rows) + f'\n  </ul>\n</main>\n{footer("")}')


if __name__ == "__main__":
    for path, title, h1, line in PLACEHOLDERS:
        f = ROOT / path
        if f.exists() and status(path) == "built":
            print("kept (built):", path)
            continue
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(placeholder(path, title, h1, line), encoding="utf-8", newline="\n")
        print("placeholder:", path)
    (ROOT / "index.html").write_text(sitemap(), encoding="utf-8", newline="\n")
    print("site map: index.html")
