# Mockups

Plain HTML mockups of the site, settled before any WordPress work. The current design is option 1, one self-contained
folder that serves as the whole site: http://localhost/user-and-product/research/mockups/option-1/ (site map at
http://localhost/user-and-product/research/mockups/option-1/sitemap.html, every page with its link and status).
All pages link to each other so the mockups can be clicked through as one site (owner, 10 Oct 2026). Brought into
one folder on 10 Oct 2026 ("bring everything into one folder and call it option 1"), with no visual or content
changes. A later redesign would be `option-2/` beside it.

## What is here

- `final-logo/`: the final logo pack (theme T08 "Signal", decided 9 Oct 2026). SVG masters, PNG renders,
  favicons and web manifest, social images, and the brand sheet:
  http://localhost/user-and-product/research/mockups/final-logo/brand-sheet.html. Rebuild everything with
  `python build.py` in that folder (it uses only `tools/` and `fonts/inter/`).
- `Logo-3/`: the owner's own mark (drawn in Illustrator, 10 Oct 2026: a disc with a person cut out, a rounded
  diamond head over a curved band), kept exactly as drawn. Clean master with the cut-outs as true holes, monochrome,
  twenty-two color options and fourteen gradient options (social only), side and stacked lockups, avatars, favicons and
  previews (Instagram, LinkedIn page and feed, browser tabs, thumbnail, header), and `export/` with the signal blue
  favicons and social images: http://localhost/user-and-product/research/mockups/Logo-3/. Rebuild with
  `python build.py`, then `python check.py`, in that folder; details in `Logo-3/README.md`.
- `fonts/`: OFL fonts with their licence files (Inter Display is the logo face). Added 9 Oct for the page
  mockups: Inter text cuts (Regular, Italic, Medium, SemiBold, from the same Inter 4.1 release) and Fraunces 9pt
  (Regular, Italic, SemiBold, from the same Fraunces 1.000 release), plus Latin-subset `.woff2` files for the web.
- `tools/`: `wordmark.py` (text to SVG paths), `render.py` (SVG to PNG), `brand_assets.py` (favicons, app icons,
  social and LinkedIn images), `build_typeboard.py` (builder for the archived type board; it writes into
  `logos/typeboard/`, so it only runs against an unpacked archive).
- `mockup.css` and `mockup.js`: shared tokens (light, dark via `prefers-color-scheme`, and a `data-theme`
  override), the type scale, spacing, components, placeholder ad slots, the theme toggle (remembered in
  localStorage), the contents highlight and the copy button. Kept here for the other mockup folders (the brand
  sheet, the thumbnail board); `option-1/` carries its own copy.
- `option-1/`: the site, design option 1: http://localhost/user-and-product/research/mockups/option-1/.
  - `index.html`: the home page (third pass, 10 Oct 2026: one visually hidden h1, the latest twelve under the
    leaderboard, newest large, in-feed ad in slot six, "All articles", then four section tiles, then the footer).
    Hand-written, on `css/mockup.css` and `css/home.css`.
  - `article.html`: the single article page, variant A (Sidebar), the chosen layout, on `css/article.css`.
  - `category/index.html`, `sections/` (articles, books, links, tools, templates) and `pages/` (about, privacy,
    advertising, contact): placeholder pages in the shared shell until each page is built.
  - `sitemap.html`: every page with its status (built or placeholder), read from the files.
  - `css/`, `js/`: the site's own copies of `mockup.css` (font paths pointed at `assets/fonts/`) and `mockup.js`,
    plus `home.css` and `article.css`.
  - `assets/logo/` (the two lockups the header and footer use, from `final-logo/svg/`), `assets/favicon/` (the
    favicons the pages link, from `final-logo/favicon/`), `assets/fonts/` (only the nine `.woff2` files the css
    loads, with their licence files).
  - `img/`: every image the home page and the article use, plus `thumbs/` (article rail and Just published) and
    `explainers/` (the explainer gallery); `img/README.md` records the home thumbnail styles.
  - `shots/`: screenshots and their README (home at 375 and 1280, article A at ten viewports, the variant thumbnails).
  - `build/`: the generators, run from `option-1/build/`. `placeholders.py` is the single source of the header,
    footer and link map; it writes the placeholder pages and `sitemap.html` (never overwriting a built page;
    placeholders carry `data-placeholder` on `<body>`) and copies the shared header and footer into the hand-written
    home page. `build_article.py` writes `article.html` from one copy of the sample article, with the header and footer
    from `placeholders.py`; `--variants` also writes the old variants B (Magazine) and C (Reader) into
    `build/variants/`, kept for reference beside the variants comparison page (`variants/index.html`), not part of
    the site. `build_home.py` draws the home thumbnails, `build_images.py` the article hero and Related thumbnails,
    `figures.py` the article figures and rail thumbnails, `explainers.py` the explainer gallery
    (`build/explainers.html`, a research page, not a site page). `shots_home.py` and `shots_article.py` take the
    screenshots into `shots/` and print the overflow, ads-in-view and ad-density checks (XAMPP must be serving).
    Rebuild: `python placeholders.py`, `python build_article.py`, and the image scripts only when the art changes.
- `references/tigerdata/`: screenshots and notes on the Tiger Data article page the owner likes for the single
  article layout: [references/tigerdata/notes.md](references/tigerdata/notes.md).
- `references/blog-thumbnails/`: the owner's 35 reference thumbnails and the "Thumbnail styles" board, which
  sorts them into ten styles with a feasibility verdict per style, four demonstrations on our palette and a
  recommendation: http://localhost/user-and-product/research/mockups/references/blog-thumbnails/index.html
  (`build.py` writes the board; `demo/make_demos.py` writes the demonstrations).
- Tooling notes: [tooling-research-2026-10-09.md](tooling-research-2026-10-09.md) (what was considered) and
  [tooling-installed-2026-10-09.md](tooling-installed-2026-10-09.md) (what was installed, versions, font sources).

Logo exploration 2 (from 10 Oct 2026, after the owner judged the four-tile mark "bland"): `logo-2/`, with its own hub at
http://localhost/user-and-product/research/mockups/logo-2/hub.html (the brief, the rounds as cards with their status, and
what the first exploration already tried). Round 1, ten pictorial marks with mass and a two-tone fold, judged first as
110 px avatars and 32 px favicons: http://localhost/user-and-product/research/mockups/logo-2/round-1/ (rebuild with
`python build.py` in `logo-2/round-1/build/`). Round 2, letterforms and monograms, is `logo-2/round-2/`.
The first exploration stays at `logos/` (http://localhost/user-and-product/research/mockups/logos/hub.html) for reference only.

The logo exploration (rounds 1 to 7, the type board, the hub, the shortlist, the final colour board with its ten
themes, the feeling board and the reference logos, with every build script) is archived at
`research/archive/logo-exploration-2026-10-09.zip` and shared at https://claude.ai/artifact/SzuFfTLWniQDMSeaXGt5oj.

## Page-mockup plan

One HTML file per page type, a shared `mockup.css`, variants side by side when choosing between looks. Use the
final logo files from `final-logo/svg/` and the header strip in `final-logo/social/` as the starting point for the
masthead.

## Design decisions (owner, 9 Oct 2026)

- Direction: editorial magazine. Bold display type, generous white space, big article pages,
  illustration-friendly; reads as a publication with a point of view.
- Colour: near-black on white, one accent colour for links and marks, automatic dark mode.
- References: Smashing Magazine (editorial layout, type, author presence); Nielsen Norman Group
  (authority, restraint, topic navigation); Lenny's Newsletter / Substack (single-author voice, simple
  reading pages, newsletter-first); bookmarks.design and uxtools.co (directory card grids for Links);
  and, for the single article page specifically, the owner likes
  https://www.tigerdata.com/blog/meshtastic-metrics-exporter-case-study-tiger-data (save a screenshot
  and notes before building the article mockup).

## Page list, in build order

1. Home: masthead, latest articles, topics, links to the sections, newsletter (automatic, nothing hand-picked).
   Done 10 Oct 2026, rebuilt simple the same day: [option-1/index.html](option-1/index.html)
   (http://localhost/user-and-product/research/mockups/option-1/).
2. Article page: typography, reading width, the template-plus-interview block, author box, related.
   Done 9 Oct 2026; variant A chosen: [option-1/article.html](option-1/article.html)
   (http://localhost/user-and-product/research/mockups/option-1/article.html). The three variants side by side are
   kept at [option-1/build/variants/index.html](option-1/build/variants/index.html).
3. Category page (UX research): reading-order groups as headings.
4. Domain hub (Design).
5. Useful links: directory listing with filters that do not create URLs.
6. Books: the owner-written list.
7. Templates: the PRD page with blank template, worked example and the interview block.
8. Tools: the sample-size calculator page.
9. About and author; Start here.
