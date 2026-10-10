# Mockups

Plain HTML mockups of the site, settled before any WordPress work. Open at
http://localhost/user-and-product/research/mockups/ (index to come).

## What is here

- `final-logo/`: the final logo pack (theme T08 "Signal", decided 9 Oct 2026). SVG masters, PNG renders,
  favicons and web manifest, social images, and the brand sheet:
  http://localhost/user-and-product/research/mockups/final-logo/brand-sheet.html. Rebuild everything with
  `python build.py` in that folder (it uses only `tools/` and `fonts/inter/`).
- `fonts/`: OFL fonts with their licence files (Inter Display is the logo face). Added 9 Oct for the page
  mockups: Inter text cuts (Regular, Italic, Medium, SemiBold, from the same Inter 4.1 release) and Fraunces 9pt
  (Regular, Italic, SemiBold, from the same Fraunces 1.000 release), plus Latin-subset `.woff2` files for the web.
- `tools/`: `wordmark.py` (text to SVG paths), `render.py` (SVG to PNG), `brand_assets.py` (favicons, app icons,
  social and LinkedIn images), `build_typeboard.py` (builder for the archived type board; it writes into
  `logos/typeboard/`, so it only runs against an unpacked archive).
- `mockup.css` and `mockup.js`: shared tokens (light, dark via `prefers-color-scheme`, and a `data-theme`
  override), the type scale, spacing, components, placeholder ad slots, the theme toggle (remembered in
  localStorage), the contents highlight and the copy button. Every page mockup links these two files.
- `article/`: page 2, the single article page in three variants (A Sidebar, B Magazine, C Reader) with the ad
  rules they follow: http://localhost/user-and-product/research/mockups/article/. `article/build.py` writes the
  three pages from one copy of the sample article; `article/shots/` holds the 375px thumbnails.
- `home/`: page 1, the home page mockup: http://localhost/user-and-product/research/mockups/home/. Hand-written
  `index.html` plus `home.css` (page rules only) on the shared `mockup.css` and `mockup.js`, with article A's header,
  footer, chips, ad slots and newsletter box. Top to bottom: the promise (the one h1), the desk (the featured piece,
  the author's margin note beside it, two more), three shelves (each domain a stack of books, one per category, its
  width set by the planned pieces, with the count in a mono chip and a note that the counts are planned), nine
  pieces ordered by importance with one labelled in-feed ad, a five-lesson Start-here course that ends by handing the
  reader back to the shelves, the author strip, Templates and Books teasers (drawn placeholder covers, never real
  ones), the newsletter box. No dates, no "latest". All titles, decks, reading times, the margin note and the path
  are made-up samples. `home/build.py` draws the twelve thumbnails into `home/img/` (styles and reasons in
  `home/img/README.md`); `home/shots/` holds 375px and 1280px screenshots, light and dark. The `.chip` and `.chips`
  rules moved from `article/article.css` into `mockup.css` so both pages share them.
- `references/tigerdata/`: screenshots and notes on the Tiger Data article page the owner likes for the single
  article layout: [references/tigerdata/notes.md](references/tigerdata/notes.md).
- `references/blog-thumbnails/`: the owner's 35 reference thumbnails and the "Thumbnail styles" board, which
  sorts them into ten styles with a feasibility verdict per style, four demonstrations on our palette and a
  recommendation: http://localhost/user-and-product/research/mockups/references/blog-thumbnails/index.html
  (`build.py` writes the board; `demo/make_demos.py` writes the demonstrations).
- Tooling notes: [tooling-research-2026-10-09.md](tooling-research-2026-10-09.md) (what was considered) and
  [tooling-installed-2026-10-09.md](tooling-installed-2026-10-09.md) (what was installed, versions, font sources).

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

1. Home: masthead, three domains as entry points, pieces worth reading, author strip, Start here path.
   Done 10 Oct 2026: [home/index.html](home/index.html) (http://localhost/user-and-product/research/mockups/home/).
2. Article page: typography, reading width, the template-plus-interview block, author box, related.
   Done 9 Oct 2026, three variants to choose from: [article/index.html](article/index.html)
   (http://localhost/user-and-product/research/mockups/article/).
3. Category page (UX research): reading-order groups as headings.
4. Domain hub (Design).
5. Useful links: directory listing with filters that do not create URLs.
6. Books: the owner-written list.
7. Templates: the PRD page with blank template, worked example and the interview block.
8. Tools: the sample-size calculator page.
9. About and author; Start here.
