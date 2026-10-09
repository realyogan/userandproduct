# Next session — User and the Product

Session closed 9 Oct 2026, about 01:30. The owner has the report and the progress page; the research
pass is complete; nothing is committed. Start by asking for the four decisions below.

Read `research/discussion/context.md` (two sections: 8 Oct kick-off, 8 Oct second session) and skim
`research/seo/topic-tree-v1.md` (the data-driven tree) and `research/seo/section-trees-v1.md`.

## Where things stand (end of 8 Oct 2026)

The full SEO research pass is done for $3.55 of the $5 cap (balance $20.19), including the manual keyword review, the v1.1 re-score and the AI harvest. Everything is on disk,
raw and distilled, with index rows and ledger lines. Nothing is committed to git yet.

Explainers for the owner (plain language, pictures):
- http://localhost/user-and-product/research/explainers/phase0-serp-findings-2026-10-08.html
- http://localhost/user-and-product/research/explainers/topic-scores-explained-2026-10-08.html (the main report:
  summary screen with the full tree of all 91 units, then folded sections; rebuilt three times today to the
  owner's taste: summary first, nothing horizontal, no size cap, intent everywhere)
- http://localhost/user-and-product/research/progress/ (live progress page with chime; status.json schema in its README)

Key files: `research/seo/keywords/topic-scores-v1.2-2026-10-09.csv` (91 scored units, intent mix, field share,
article capacity; owner_fit column empty), `topic-evidence-v1.2-2026-10-09.csv`, `topic-tree-v1.2.md` (tree, launch shortlist of eight, what the hypothesis got wrong, caveats),
`section-trees-v1.md` (Links, Books, Tools, Templates), `competitors/traffic-2026-10-08.csv`,
`serps/page-one-2026-10-08.csv` (146 SERPs, Phase 0 and 4).

Tools now in place and working: `tools/dataforseo_client.py` (REST client with raw caching, index
rows, budget guard; credentials in `.local/dataforseo.env`, git-ignored), `harvest.py`,
`serp_distill.py`, `sitemaps.py` and `gsc.py` (re-pointed), `github_lists.py`, phase scripts.

## Waiting on the owner

1. Fill `owner_fit` (1 to 3, first-hand experience) for the launch shortlist and the next-in-line
   units in `topic-scores-2026-10-08.csv`, or say them in chat and Claude writes them in.
2. Yes or no to the three broad-field shortlist entries: analytics, web design, project management.
3. Confirm the first categories for Links, Books, Tools and Templates (section-trees-v1.md).
4. Launch size: how many topics open at launch and how many articles each (the deferred
   "Printables-style launch" discussion).
5. Seed phrases from the owner's own experience, if any; they can be harvested for about $0.03 each.

## Then, in order

- Re-score with owner_fit applied; write `topic-tree-v1.3.md` and the final launch set (the owner cuts
  Wave 1 from 81 articles to the launch size they choose).
- Progress page for long runs: `research/progress/` (status.json schema in its README); use it for every run.
- Write the retrofit document: scoring method (done in practice; write it up), competitor list per
  section (done), content types and formats per section, editorial window process, author and
  authority plan.
- Content model: five post types (articles, links, books, tools, templates) plus the shared Topics
  taxonomy (three domains, topics, subtopics from the tree) and per-section categories.
- Commit the research folder (first commit), create the GitHub repo (owner, realyogan account, SSH
  alias github-realyogan), push.
- Only then: WordPress setup (WP-CLI), child theme, structure plugin.

## Back burner (owner, 9 Oct)

- Skill library: interview and "check my draft" skills across product, UX research and UX/UI design, one per
  template page, growing out of the articles. Parked until the PRD interview passes its blind test and the
  launch set is live. Candidate list in context.md (9 Oct, council 2 entry). Verdict in
  `research/discussion/council/verdict-ai-skills-2026-10-09.md`.

## Lessons recorded this session (so they are not repeated)

- DataForSEO `keyword_ideas` sorted by volume returns category-wide noise; use `keyword_suggestions`
  (phrase match) for topic harvests. Raw Labs volumes are inflated by word-order variants; use the
  variant-adjusted figure.
- The live SERP route failed all day with 50000 errors; the standard queue (task_post + task_get)
  works and costs a quarter as much.
- Google Ads volumes are the same monthly series as Labs volumes here, so they are not an
  independent check; Google Trends over five years is.
- Connector (MCP) results land in chat and have to be re-typed into files; the REST client avoids
  that and is the route for anything bigger than a few dozen rows.
- Every head term in this field has an AI Overview; that score component barely separates topics.
- Rule-based clustering missed 204 of 6,587 unassigned phrases on manual review (the largest miss was
  "electronic accessibility", 74K/month, killed by an over-wide noise word). Patch is applied; keep a
  manual pass over the unassigned bucket as a standard step.
- AI phrased with our field is a small search topic (44 phrases, score 53.8); treat AI as a cross-cutting
  tag, not a pillar.
