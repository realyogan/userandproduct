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
- [publishing-system-proposal-2026-10-09.html](http://localhost/user-and-product/research/explainers/publishing-system-proposal-2026-10-09.html):
  the proposal for the publishing system, told as a magazine newsroom: a one-screen summary, then 11 numbered sections
  with one picture each (the desks around the backlog board, the backlog bucket with its 20 and 12 water marks and the
  learning-sentence gate, the explorer's three circles and six sources, the owner's Sunday, one article's stations with
  two stop signs, publishing and the live-page check, LinkedIn and reels, the learning loop, the 10 to 12 agents with
  what each reads, writes and loads, the build order) and six questions for the owner, remembered in the browser.
- [publishing-system-proposal-2-2026-10-09.html](http://localhost/user-and-product/research/explainers/publishing-system-proposal-2-2026-10-09.html):
  proposal 2, which replaces proposal 1 (kept as it was for comparison). Same newsroom and 11 sections, plus a fifth desk,
  Performance: a campaign manager that, once the site is live, reads Search Console, analytics, page speed, the keyword
  store and rival sitemaps every week, scores the site, each category and each article against its one-line expectation,
  writes nudges with evidence, and keeps old pages current with review dates and refresh jobs that run through the
  making desk. It proposes and never edits the site. Adds the expectation and review-date backlog fields, 12 agents
  with the campaign manager after launch, and a seventh question (when the weekly scorecard reaches the owner).
- [publishing-system-proposal-3-2026-10-09.html](http://localhost/user-and-product/research/explainers/publishing-system-proposal-3-2026-10-09.html):
  proposal 3, built on proposal 2 with every agent and desk kept (12 agents, five desks, the campaign manager, refresh
  jobs, expectation and review date). What changed is the owner's rhythm: a monthly pitch meeting started by one command
  (`/whatsup`, a placeholder name) that gives the status and about ten pitch cards with outlines and a story slot; a two-
  or three-day build window where the desks make the whole ready set and the publisher creates scheduled drafts in local
  WordPress; a review week (30 to 40 minutes per draft); scheduled publishing at about two a week; and the arithmetic
  (8 to 10 pieces a window, the first window 3 or 4). 12 sections, with a new pitch-meeting section and a build-window
  section, and 14 questions (proposal 2's seven plus seven on the rhythm).
