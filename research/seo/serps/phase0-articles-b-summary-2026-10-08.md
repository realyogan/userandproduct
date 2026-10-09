# Phase 0 SERPs, articles group B (8 Oct 2026)

Google US, desktop, depth 10, standard queue. These are rows 13 to 24 of the "articles" section in
`phase0-task-ids-2026-10-08.csv`. Collecting finished tasks was free; the posting cost was $0.0006 per task.

## Collected (12 of 12, none pending)

north star metric, retention rate, a/b testing, okr examples, jobs to be done, product discovery,
agile vs scrum, customer journey map, product strategy, saas pricing strategy, go to market strategy,
product led growth.

Files:
- `research/seo/serps/page-one-2026-10-08-articles-b.csv` (96 organic rows, no featured snippets)
- `research/seo/serps/features-2026-10-08-articles-b.csv`
- `research/seo/cache/index-staging-serps-articles-b.csv` (ids 261008-SB-001 to 012)
- raw: `research/seo/cache/raw/serps-2026-10-08/<slug>.json`

## Most frequent page-one domains (organic, "www." stripped)

| Domain | Keywords |
|---|---|
| linkedin.com | 3 |
| en.wikipedia.org | 3 |
| productplan.com | 3 |
| reddit.com | 3 |
| coursera.org | 3 |
| quora.com | 3 |
| salesforce.com | 2 |
| medium.com | 2 |
| online.hbs.edu | 2 |
| atlassian.com | 2 |
| amplitude.com | 2 |
| youtube.com | 2 |
| airfocus.com | 1 |
| uxcam.com | 1 |
| subscriptionindex.com | 1 |
| enji.ai | 1 |
| customersuccesscollective.com | 1 |
| kyligence.io | 1 |
| teknicks.com | 1 |
| zendesk.com | 1 |

The top is flat. No domain holds more than 3 of the 12 SERPs, and most domains appear only once.
No single publisher dominates this group.

## SERP features

- AI Overview: 12 of 12.
- Featured snippet: 0 of 12.
- People also ask: 12 of 12.
- Video pack: 1 (agile vs scrum).
- Images: 8. Related searches: 9.

## Weak page one (3 or more weak organic results)

3 of 12 keywords:
- product discovery: 6 weak results (antmurphy.medium.com, productboard.com/blog, amplitude.com/blog,
  reddit.com, youtube.com, pendo.io/glossary). This is the softest SERP in the group.
- product strategy: 3 (productplan.com/glossary, medium.com, reddit.com).
- saas pricing strategy: 3 (linkedin.com twice, quora.com).

okr examples has 2 (quora.com, medium.com). customer journey map has 0.

## Domains cited most often in AI Overviews (number of keywords)

youtube.com 6, en.wikipedia.org 4, salesforce.com 4, atlassian.com 4, reddit.com 4, amplitude.com 3,
coursera.org 3, online.hbs.edu 3, productled.com 2, linkedin.com 2, nngroup.com 2, productplan.com 2,
miro.com 2, paddle.com 2.

## Oddities

- **saas pricing strategy:** the organic results don't match the query. Results include two LinkedIn
  pages (a "top-content" page and a post), a SaaS cost-management page (tropicapp.io) and a "rydoo"
  CFO page. The AI Overview cites strong pricing guides (Stripe, Paddle, Maxio, Chargebee), but those
  pages are not on page one. This looks like a real opening.
- **retention rate:** the intent is mixed. Results cover customer, employee (ADP, 15Five) and student
  retention (UAMS, Stellic, an Australian .gov.au page). The product or SaaS angle gets only
  productplan.com/glossary and Wall Street Prep.
- **jobs to be done:** two of the four People Also Ask questions are about careers ("What 5 jobs will
  remain after 2030?", "What career is Gen Z most interested in?"). Google partly reads the query as
  being about employment.
- **agile vs scrum:** the AI Overview has no top-level reference list; its citations exist only inside
  its sections. The ai_overview_ref_domains column for this keyword is built from those nested
  references. It is the only keyword in the group with a video pack.
- **product strategy:** this SERP carries a paid ad (productside.com) and a short-videos block, which
  the distilled CSVs ignore.
- **customer journey map:** the results are image-heavy. Four of the eight organic results are image
  results, and none are weak domains, so expect strong template and tool competition.
- Several organic items carry "timestamp" values that are only the crawl time (for example
  "2025-10-08 15:45:41"). These are copied as given.
- The raw JSON files were written from the tool's response text, not saved straight from the API.
  All 12 parse as valid JSON and match their task ids.
