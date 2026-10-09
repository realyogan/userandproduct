# Mockups

Plain HTML mockups of the site, settled before any WordPress work. Open at
http://localhost/user-and-product/research/mockups/ (index to come).

## What is here

- `final-logo/`: the final logo pack (theme T08 "Signal", decided 9 Oct 2026). SVG masters, PNG renders,
  favicons and web manifest, social images, and the brand sheet:
  http://localhost/user-and-product/research/mockups/final-logo/brand-sheet.html. Rebuild everything with
  `python build.py` in that folder (it uses only `tools/` and `fonts/inter/`).
- `fonts/`: OFL fonts with their licence files (Inter Display is the logo face).
- `tools/`: `wordmark.py` (text to SVG paths), `render.py` (SVG to PNG), `brand_assets.py` (favicons, app icons,
  social and LinkedIn images), `build_typeboard.py` (builder for the archived type board; it writes into
  `logos/typeboard/`, so it only runs against an unpacked archive).
- `references/tigerdata/`: screenshots and notes on the Tiger Data article page the owner likes for the single
  article layout: [references/tigerdata/notes.md](references/tigerdata/notes.md).
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

1. Home: masthead, three domains as entry points, latest pieces, author strip, Start here path.
2. Article page: typography, reading width, the template-plus-interview block, author box, related.
3. Category page (UX research): reading-order groups as headings.
4. Domain hub (Design).
5. Useful links: directory listing with filters that do not create URLs.
6. Books: the owner-written list.
7. Templates: the PRD page with blank template, worked example and the interview block.
8. Tools: the sample-size calculator page.
9. About and author; Start here.
