# SEO analysis plan — User and the Product

Written 8 Oct 2026 for the owner. Status: proposed, awaiting "go".

## Principles

1. The topic tree is an output, not an input. The three domains (design; product and delivery; business
   and growth) are only the seed hypothesis for the harvest. Clusters that the data does not support get
   dropped; clusters the data surfaces that we did not list get added.
2. Every section gets its own competitor set, found from the data (who is on page one for that
   section's queries), not from memory. A hand list is used only to seed the free sitemap pulls.
3. Cache first, spend last, as in `README.md`. Free sources (sitemaps, Search Console, GitHub lists)
   before paid ones. Queue, not live. Everything logged in `ledger.md` and `cache/index.csv`.
4. Every response is stored raw before anything else: code calls write `cache/raw/<id>.json`; connector
   (MCP) results are written to the same folder by the subagent from the tool output, not left in chat.
   One index row per subject in `cache/index.csv`. Within the reuse windows (30 days for volumes, SERPs
   and domains; 60 for ideas and ranked keywords; 90 for sitemaps) nothing is queried twice; the
   distilled CSV is read instead.
5. Budget: the owner's cap for this pass is $5, hard stop. Phases 1 and 2 together under $2.50; the
   whole plan about $4.30. Claude stops and asks before any call that would cross $5.

## Phase 0 — competitor discovery per section (near free)

Goal: `competitors/<section>-competitors.csv` for each of the five sections, with columns domain, type,
how found, estimated traffic (filled in Phase 2), notes.

Method: pull the live Google SERP (US) for 15-20 head queries per section and count which domains
appear on page one. About 90 SERPs at about $0.002 each, under $0.20. The counts are the competitor
list. A hand list seeds the queries and the sitemap pulls:

- Articles. Publications: Smashing, NN/g, UX Collective, UX Planet, UX Matters, A List Apart, Boxes
  and Arrows, UX Booth, Interaction Design Foundation, Mind the Product, Product Coalition, Department
  of Product, Product School, Pragmatic Institute, SVPG, Reforge, Lenny's Newsletter. Individual
  experts: Teresa Torres (producttalk.org), Roman Pichler, John Cutler, Jared Spool, Luke Wroblewski,
  Melissa Perri, Gibson Biddle, Julie Zhuo, Jeff Sauro (MeasuringU), Andrew Chen, Kyle Poyar, Mike Cohn
  (Mountain Goat), Jeff Patton, Pavel Samsonov, Baymard, Laws of UX, Growth.Design. SaaS blogs with
  glossaries: Productboard, ProductPlan, Aha!, Hotjar, Maze, Userpilot, Amplitude, Mixpanel, Pendo,
  Dovetail, Atlassian Agile Coach, Scrum.org. The SERP count decides which of these matter per domain.
- Useful links. bookmarks.design, uxtools.co, toools.design, uxdatabase.io, undesign, prototypr toolbox,
  designresourc.es, startupstash, futurepedia (AI tools), Product Hunt collections, GitHub "awesome"
  lists for product management, UX and design (openly licensed, easiest to mine).
- Books. Lenny's book lists, Mind the Product's and Product School's reading lists, NN/g's reading
  list, bookauthority.org, mostrecommendedbooks.com, fivebooks.com, Goodreads shelves, UX Collective
  and Medium roundups ("best UX books").
- Tools (ours: calculators and small utilities). Evan Miller's A/B calculators, MeasuringU calculators,
  AB Testguide, Optimizely and Statsig sample-size calculators, SurveyMonkey sample size, CXL
  calculators, RICE calculators from Intercom, Productboard, Roadmunk and Fibery.
- Templates. Figma Community, Notion template gallery, Miro Miroverse, FigJam, Atlassian templates,
  Aha! and Productboard templates, Maze and Dovetail templates, NN/g free templates, Mural.

Free sitemap pulls (`tools/sitemaps.py`, re-pointed) for every domain that appears three or more
times on page one: article inventories for Articles competitors; entry inventories for Links, Books
and Templates competitors (directory URL slugs name the entries, so the inventory of "what tools are
listed now" comes from sitemaps without scraping pages). Where a directory has no useful sitemap, read
its public listing pages with robots.txt respected and a one-second delay, keep only names and URLs,
and write our own descriptions. GitHub awesome lists are read directly.

Output: five competitor CSVs; `competitors/sitemaps/` inventories; a first "what is listed now" table
for Links, Books and Templates (`competitors/inventory-<section>.csv`).

## Phase 1 — keyword harvest for Articles (about $1.50)

Goal: the raw material for the topic tree.

- About 30 seed terms spread across the three hypothesised domains plus deliberately off-tree seeds
  (service design, growth marketing, data analytics for PMs, AI product management, product ops,
  no-code, startup) so the data can tell us what we missed.
- DataForSEO Labs keyword ideas, US, filters: volume 100 or more, exclude brand and job-posting
  terms, 300 rows per seed. About 30 tasks, 9,000 rows: around $1.45.
- Add the article slugs from the Phase 0 sitemap inventories as a second source of topic evidence
  (what the strongest publications actually write about, by count).
- Cluster (Claude, free) into candidate topics. A topic exists only if it has 20 or more keywords
  with volume 100 or more, or 15 or more competitor articles, or both.

Output: `keywords/harvest-articles.csv` (keyword, volume, CPC, seed, cluster) and
`keywords/topic-candidates.csv` (cluster, keyword count, total volume, competitor article count).

## Phase 2 — competitor sizing (about $1)

- `bulk_traffic_estimation` for every domain from Phase 0 in one task (up to 1,000 domains): about
  $0.05. Gives estimated traffic to tier the list.
- Ranked keywords for the top 6 Articles competitors by page-one count, 500 rows each, filtered to
  volume 100 or more: about $0.45. Shows which clusters they win and which they do not cover (the gaps).
  More competitors only if the cap allows after Phase 4.
- No historical rank overview (dear, and not needed for this decision).

Output: `competitors/articles-competitors.csv` with traffic; `competitors/ranked-<domain>.csv`;
`competitors/coverage-by-topic.csv` (competitor count per candidate topic).

## Phase 3 — section demand and section category trees (about $0.80)

Each section gets its own category tree, derived the same way as the article topics: from keyword
clusters plus what the section's competitors list. bookmarks.design, for example, has one flat level
of categories; the data decides whether ours splits first by domain (design links, product management
links, business links) and then by job (prototyping, research, analytics, icons and assets, roadmapping,
and so on), or the other way round.

- Keyword ideas, 14 seeds, 300 rows each, about $0.65: "best ux tools", "ux research tools", "product
  management tools", "product analytics tools", "roadmap tools", "design resources", "ux books",
  "product management books", "business books for product managers", "prd template", "user persona
  template", "product roadmap template", "rice calculator", "sample size calculator".
- Competitor inventories from Phase 0 (directory and gallery sitemaps, GitHub awesome lists, book-list
  pages): entry counts per category as the second evidence source, and the starting stock of entries.
- Cluster each section's keywords into categories; a category exists only if it has demand (10 or
  more keywords with volume 100 or more) or stock (15 or more entries across competitors), or both.

Output: `keywords/harvest-sections.csv`; `keywords/section-candidates.csv`; and
`research/seo/section-trees-v1.md`: a category tree for Links, Books, Tools and Templates with the
evidence per category, plus the order to build them in.

## Phase 4 — scoring (about $1.10)

For the top 150 keywords across all candidate topics and sections:

- Google Ads volumes on the standard queue, one task: about $0.06.
- Bulk keyword difficulty and search intent, one task each: about $0.10.
- Live SERP for the 100 head terms (about $0.20): page-one domains, SERP features, whether an AI
  Overview is present, and whether page one is weak (Medium, Quora, Reddit, LinkedIn Pulse, thin SaaS
  glossaries).
- Trend, two sources. The Labs and Google Ads responses already carry twelve months of monthly volumes
  for every keyword at no extra cost; the distilled tables keep a twelve-month slope and a seasonality
  flag from them. On top of that, Google Trends explore for the head term of each candidate topic, five
  terms per task on the standard queue, five-year range: about 8 tasks, under $0.10. Topics that are
  falling over five years score down; rising ones score up.

Scoring columns per topic: total volume; twelve-month slope and five-year trend; median difficulty; share of decision-intent queries (how to,
versus, which, examples, template, calculator) versus definitional; AI Overview share (definitional
queries with an AI Overview score down); weak-page-one share; competitor coverage count (fewer is
better); owner authority fit (1-3, the owner's first-hand experience; this is the one hand-set
column). The score is the ranked list.

Output: `keywords/topic-scores.csv`, `serps/page-one.csv`, and the deliverables below.

## Deliverables

1. `research/seo/topic-tree-v1.md`: the data-driven topic tree for Articles (domains, topics, the
   keyword clusters under each), with the evidence per topic and a note on what the hypothesis got wrong.
   `research/seo/section-trees-v1.md`: the category tree for each of Links, Books, Tools and Templates.
2. The launch shortlist: four to six topics to open at launch, in order, with the head articles each
   needs, and the first categories to build for Links, Books, Tools and Templates.
3. Five competitor CSVs with traffic tiers, and the "what is listed now" inventories for Links, Books
   and Templates as the starting stock for those sections.
4. Ledger lines and index rows for every call.

## Order of work and who does it

| Step | Who | Depends on |
|---|---|---|
| Re-point `sitemaps.py` and `gsc.py` to userandproduct.com, add a domains argument | Opus subagent | go |
| Phase 0 SERPs and sitemap pulls | Opus subagent | re-pointed tools, connector authorised |
| Phase 1 harvest and clustering | subagent pulls, main session clusters | Phase 0 inventories |
| Phase 2 sizing | subagent | Phase 0 list |
| Phase 3 section demand | subagent | none (can run with Phase 1) |
| Phase 4 scoring and the tree | subagent pulls, main session scores and writes | Phases 1-3 |

Estimated total: about $4.30 against a $5 cap, with the probe-first rule on any endpoint not yet priced on this
account. Everything is reusable for 30-90 days, so the pass is not repeated for the launch build.

## What Claude needs from the owner

- "Go". The cap is set: $5, hard stop (owner, 8 Oct 2026).
- The DataForSEO connector authorised in the claude.ai connector settings (it still shows as
  unauthorised in this session). Ubersuggest is optional for this plan.
- Any competitor or directory the owner already knows and wants in the seed list.
