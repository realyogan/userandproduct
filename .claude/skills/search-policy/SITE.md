# Site layer: userandproduct.com

The general rulebook is `SKILL.md`. This file records the decisions that bind it to this site and this
newsroom. Decisions are the owner's, dated, and logged in `research/discussion/context.md`.

## The author of record

The owner, fifteen years in product design and product management, is the author of every piece in
fact: the owner directs each piece through a note or a seed, reviews every draft in the newsroom app,
approves the positions it takes, and confirms each post once in local WordPress before it goes live.
No first-person claim the owner did not give. No invented specifics of any kind. The author page
states the owner's background plainly and verifiably and proves a real person: the owner's real photo,
the LinkedIn profile and the other places the owner exists online (a portfolio if the owner decides
to add it), all linked from the page and listed as `sameAs` in its ProfilePage markup; the About page
says what the site is, who runs it, and how to reach it (owner, 10 October 2026).

## How the owner's judgment enters a page

- **Seeded pieces (at least three quarters).** The card carries a seed (the owner's answers to two or
  three practice questions), a brief (the owner's rules as the spine), or a shaping note, before the
  piece is written.
- **Synthesis pieces (about one in twenty at most; owner's decision, 10 October 2026, tightened from a
  quarter).** A piece with nothing from the owner before it is written. Written from understanding as a fresh take,
  never a summary or a stitch, labeled on the board, never among the flagship launch pieces; the owner's feedback on
  the draft and the keep-reword-strike on the positions list are the oversight. The owner's "write about this"
  brief followed by the owner reordering or cutting the outline is NOT synthesis: the order and the cuts are the
  owner's judgment entering first, so it counts as seeded.
- **The positions list.** After a draft is done the editor lists every position the piece takes; the
  owner keeps, rewords or strikes each before reading the prose. Reworded rules go into the principles
  file and become the canon later drafts are checked against.

## Disclosure

No "How this site is made" page (owner, 10 October 2026). No per-article label, no tool or model names
anywhere a reader can see. Nothing anywhere on the site says otherwise, so there is no contradiction.
Thumbnails and illustrations are drawn by the site's own generators from the house rules, not by a
generative image model, so no IPTC source-type tag applies; if a generative image tool is ever used,
the tag goes in.

## Who runs what

| Rule section | Owned by |
|---|---|
| 1 reader reason, site purpose | Explorer writes the line on every card; the main session kills cards without one |
| 3, 4 originality, paraphrase, accuracy, filler | Checker, with the writing-style rulebook |
| 5 byline, author page, disclosure | Theme and plugin (byline, author link); the books shelf by the owner's takes |
| 6, 7 titles, descriptions, alt text, images | Writer (title, description), illustrator (alt text), SEO reviewer (stuffing) |
| 8 structured data | Theme and Rank Math at install; publisher validates each page live |
| 9 links | Writer (sources, sponsored, nofollow), SEO reviewer (internal links), the linking pass per window |
| 10 URLs, noindex, canonical, sitemap | Install session (Rank Math settings); publisher's live check |
| 11 dates | Publisher sets the real dates; campaign manager's review date triggers refreshes |
| 12 page experience, ads, newsletter box, 404 | Theme; the site design mockups |
| 13 tools | SEO research store rules; no tool queries Google |
| 14 checklist | Checker before the editor; publisher before going live; report in the article folder as `checks.md` |

The campaign manager measures authority signals (mentions, links, direct and returning visits) and
never scores a rank target as a page's purpose. Takes are measured on those signals, not rank.

## Indexing and feature decisions

- Index: articles, category pages, series pages, template pages with guidance, the books shelf, author,
  About, Start here. Noindex: tag, date and author archives, internal search, filters, attachments.
- Snippet controls: none set; Google may use snippets and previews by default. Revisit if the owner
  wants to limit AI Overviews input.
- Structured data emitted: Article, ProfilePage, Organization, WebSite with site name, BreadcrumbList.
  Not emitted: FAQPage, HowTo, sitelinks search box (features retired).
- Dates in the UI: a quiet "Updated <month year>" only, equal to `dateModified`; no sort-by-date
  anywhere; lists ordered by series or importance.
- Launch: about fifty reviewed articles live at once, plus the books shelf and at least ten working tools (owner,
  10 October 2026: tools rather than templates at launch; templates come later); sitemap and
  Search Console on day one; the announcement about a week later; then one a day from scheduled
  posts. Volume is not the signal; each page passes the checklist.

## Affiliate and ads

Books shelf entries carry the owner's own take, what the book is good for and for whom, where it is
wrong or dated; links `rel="sponsored"` with a visible disclosure beside them. Display ads follow the
layout rules already set: labelled, never covering content, at most three in view, mobile density under
thirty percent, never styled like content or navigation.

## Licensed API

Keyword, SERP and paraphrase sentence checks go through the paid research API under the research
store's cache-first rules. Search Console and the site's analytics are the only sources for the site's
own performance.

## The build to-do

The list of install and build items that make the technical rules true in WordPress is kept at
`research/discussion/todo/search-policy-build-checklist.md`.
