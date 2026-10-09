# Explainers

Plain-language HTML pages that explain research results to the site owner. Each one takes a
finished piece of research (SERP pulls, competitor passes, keyword data) and tells its story in
short sentences, with simple charts and diagrams.

- One file per topic, named `<topic>-<date>.html` (for example `phase0-serp-findings-2026-10-08.html`).
- Self-contained: no external scripts or fonts; plain CSS and inline SVG only.
- Every number comes from the files under `research/seo/`; each page lists its sources in its footer.
- Open them at `http://localhost/user-and-product/research/explainers/<file>`.

## Pages

- [phase0-serp-findings-2026-10-08.html](http://localhost/user-and-product/research/explainers/phase0-serp-findings-2026-10-08.html):
  what Google's first page showed for 78 questions across the five sections.
- [topic-scores-explained-2026-10-08.html](http://localhost/user-and-product/research/explainers/topic-scores-explained-2026-10-08.html):
  the research report (scores v1.2), summary first: one screen with the three headline numbers, the six Wave 1
  topics to launch first, the tree at a glance (every line badged easy, promising, takes work, hard, parked or no data,
  with a hover or tap card of its numbers; the same badges in the whole tree and the section trees) and the four decisions. Everything else is folded into sections
  that open on click: what we did, how a topic is judged, the whole tree (domain, topic, sub-topic), the scoreboard,
  the evidence for the top 30, the section trees, AI, the launch plan, confidence, spend, the checklist and the data files.
- [tree-simplified-2026-10-09.html](http://localhost/user-and-product/research/explainers/tree-simplified-2026-10-09.html):
  the site tree, simplified for readers: the 77 article nodes of the research tree as 13 categories and 61 article groups (v1.1, 12 of them sized from the harvest scan) in three
  domain cards, each line badged with the same ease icons and colors and a hover or tap card (articles, searches,
  difficulty, score range, formats, wave and everything merged into it); the AI, Careers, Templates and Tools tags, the
  parked list and the two calls for the owner. Data in `research/seo/tree-simplified-v1.1-*.csv` and `tree-simplified-v1.1.md` (v1 files kept).
