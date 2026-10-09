# SEO research store — User and the Product

Every keyword, SERP, domain and sitemap result we ever pull lives here, so nothing is paid for
twice and nothing is re-read at full size. Carried over from the Printables store on 8 Oct 2026
(rules, layout, price sheet); the data folders start empty. Companion rules for Claude are in
`.claude/skills/seo-research/SKILL.md`, which points back to this file.

Access: DataForSEO has two routes: the claude.ai connector (results land in chat; fine for small pulls) and the REST API with the credentials in `.local/dataforseo.env` (git-ignored; used by `tools/dataforseo_client.py` for bulk pulls, which saves raw responses itself). Ubersuggest is a claude.ai connector only.
They must be authorised in the claude.ai connector settings before use. Search Console uses the
service account key in `.local/gsc-service-account.json` (see `tools/README-gsc.md`).

## Layout

```
research/seo/
  README.md                 this file: rules, layout, retention windows, price sheet
  ledger.md                 spend log: one line per research session (tool, reports/cost, what for)
  cache/
    index.csv               ONE ROW PER QUERY. Claude greps this before any call.
    raw/                    full API/MCP responses as JSON, named by the index row id (committed, owner rule)
    gsc/                    Search Console pulls (gsc.py)
  keywords/                 distilled keyword tables (CSV): volume, difficulty, CPC, intent, AI Overview present
  serps/                    distilled page-one tables (CSV): keyword -> positions, domains, DA, SERP features
  competitors/              domain overviews (CSV) and parsed sitemaps (one file per domain, in sitemaps/)
  tools/                    sitemaps.py (competitor sitemap pull), gsc.py (Search Console). Both still point
                            at the Printables domain and file names; re-point before first use.
```

## The cache-first rule

Before any Ubersuggest or DataForSEO call, grep `cache/index.csv` for the subject (keyword,
domain or seed). If a row exists and is younger than the window below, use the distilled file it
points to. Do not call again.

| Data | Reuse window | Why |
|---|---|---|
| Keyword volume / difficulty / CPC | 30 days | monthly data; volumes change slowly |
| Keyword ideas / suggestions for a seed | 60 days | the set barely changes |
| SERP page one | 30 days | rankings move, but not weekly for our terms |
| Domain overview (DA, traffic) | 30 days | monthly estimates |
| Competitor ranked keywords | 60 days | |
| Sitemap pull | 90 days | inventory, not rankings |

After the window, re-query only if the answer would change a decision. A number that is 45 days
old is still good enough to rank a candidate list.

## Frugal rules (both bills: DataForSEO dollars and Claude context)

1. **Batch.** Google Ads volumes take up to 1,000 keywords per task; never one keyword per call.
2. **Queue, not live**, for volumes and anything run overnight (about a third cheaper).
3. **Filter in the request**: minimum volume, exclude brands and marketplaces, cap result count.
4. **Cache every response** to `cache/raw/` and add an index row before doing anything else with it.
5. **Distil, then read the distilled file.** Claude reads CSVs in `keywords/`, `serps/`,
   `competitors/`, never the raw JSON, except to debug a parser.
6. **Bulk research runs in a subagent** that writes files and reports a summary; the main
   session reads the summary and the CSVs.
7. **No rank tracking through paid APIs.** Search Console does that for free.
8. **DataForSEO account settings:** daily expense limit about $2 across the account; auto-recharge
   OFF. The research client keeps its own monthly ledger and refuses calls past a soft budget.
9. **Ubersuggest** (100 reports/day, resets daily): use for conversational exploration and domain
   snapshots; prefer the bulk suggestion tools (dozens of keywords per report) over single
   overviews; log every report in `cache/index.csv` the same way.
10. **Unmeasured endpoint = probe first.** Run one task, read `appmgmt/user_data` (free), then the rest.

## Price sheet (DataForSEO, after the July 2026 increase; measured on the Printables account)

| Call | Price | Note |
|---|---|---|
| Labs: keyword ideas, suggestions, related, overview, bulk difficulty, intent, ranked keywords, competitors domain, domain rank overview | $0.012 per task + $0.00012 per returned row | filters reduce rows |
| Labs: serp_competitors, bulk_traffic_estimation | $0.012 per task + $0.00012 per returned row | bulk_traffic takes up to 1,000 domains per task: the cheap way to size competitors |
| Labs: historical rank overview (monthly domain history) | about $0.15 per domain task | much dearer than other Labs calls; use sparingly |
| Google Ads search volume, up to 1,000 keywords | $0.09 live · $0.06 standard queue | one task per pillar per country |
| Google organic SERP, live advanced | about $0.002 per SERP | head terms only; the response carries the `ai_overview` item |
| Google Trends explore, live | $0.011 per task (up to 5 keywords per task, any time range) | relative demand; standard queue is cheaper for batches |
| Minimum top-up | $50, does not expire | |

Typical costs (Printables experience): a full research pass for one pillar about $3.50; four pillars
about $14; three months of normal use about $25.

## Differences from the Printables store

- Locations: US (`2840`) first; the UK (`2826`) and Canada (`2124`) only for a shortlist.
- Articles, not assets: the keyword tables carry an intent column and an "AI Overview present"
  column (from the SERP `ai_overview` item); definitional queries with an AI Overview are scored down.
- "Weak page one" here means Medium, Quora, Reddit, LinkedIn Pulse or thin SaaS glossary entries,
  not PDFs and Pinterest.
- Competitor set: publications (Smashing, NN/g, UX Collective, Mind the Product, SVPG, Lenny's,
  Reforge) and SaaS blogs with glossaries (Productboard, ProductPlan, Hotjar, Maze, Userpilot,
  Amplitude, Pendo, Dovetail). Sitemap pulls size their article inventories per pillar.
