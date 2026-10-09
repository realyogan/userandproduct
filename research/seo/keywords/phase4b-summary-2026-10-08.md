# Phase 4b summary: v1.1 re-cluster and re-score (8 Oct 2026)

What ran: the manual review's rule patch applied to `tools/cluster_v2.py`, the Phase 1 review rows and a new AI
harvest added to the combined set, the Phase 4 unit builder re-run, page-one SERPs and Google Trends for the new
units only, and the same score. The tree is `research/seo/topic-tree-v1.1.md`.

## Spend (DataForSEO, US)

| Step | Calls | Cost |
|---|---|---|
| Phase 1c AI harvest: keyword suggestions, 16 seeds, 150 rows max, volume >= 100 (probe 1 seed $0.0137, then 15) | 16 | $0.2017 |
| Page-one SERPs for the six new head terms, standard queue (task_post, tasks_ready, task_get/advanced) | 6 tasks | $0.0036 |
| Google Trends explore live: 2 groups of 3 new head terms, 1 regroup of the 2 that came out too small | 3 | $0.0330 |
| Google Ads volumes | none (the new units use the Labs volume) | $0 |
| **Total** | | **$0.2383** |

Balance $20.42 before, $20.19 after. Cache: every head-term SERP and Trends row of the 84 v1 units was reused;
the only SERP that already existed for a new unit's head term 2 ("ai tools for product managers", Phase 0) was
reused too. Index rows: 16 harvest rows (note "phase1c ai"), 1 SERP batch row, 6 SERP rows (ids 261008-P4B-001
to 006), 3 Trends rows. Spend rows appended to `keywords/phase4-spend-2026-10-08.csv`.

## Counts

| | v2 / v1 | v1.1 |
|---|---|---|
| Keywords clustered (unflagged, volume >= 100) | 3,017 | 3,270 |
| Topics | 25 | 30 |
| Sub-topics | 45 | 47 |
| Assigned | 2,641 | 2,884 |
| Unassigned (of which noise) | 376 | 386 (275) |
| Scoring units | 84 | 91 |
| Head-term SERPs | 68 | 74 |

Added rows: 172 from the Phase 1 review (source "1a-review"), 79 from the AI harvest (source "1c-ai"; 62
unflagged), and 19 "jobs to be done" rows of the old combined set that were unflagged after v2. All 142 "existing
topic" verdicts of the review now land in the named topic.

**AI harvest.** Rows per seed: ai design tools 35, ai product manager 14, ai for product managers 10, ai ux
design 6, ai roadmap 5, ai in design 4, ai prototyping 3, ai product development 2, ai agents product 1, chatgpt
for product managers 1 (brand-flagged), and 0 for ai in product management, ai product strategy, ai for ux
designers, ai ux research, ai user research and generative ai product. 79 distinct keywords; flags: 5 jobs, 8
course, 4 brand; 44 of the 62 unflagged rows are on topic, 18 went to the new consumer and off-field AI noise rule
(interior, home, room, landscape, logo, game and engineering design, AI engineer roadmaps). The AI topic has 51
keywords (the 44 plus "ai design assistant", "ai governance framework", "ai for product management", "agent ui",
"agent chat ui" and two AI PRD phrases from the earlier sets).

**New units** (ids continue from u84; every v1 unit kept its id and head terms):

| Unit | Topic or sub-topic | Head terms | Keywords | Adjusted | KD | Score | Rank |
|---|---|---|---|---|---|---|---|
| u91 | ux writing and content design | ux writing / content strategy | 11 | 6,650 | 0 | 65.7 | 9 |
| u86 | ai in product and design work (topic total) | ai for product managers / ai tools for product managers | 51 | 49,530 | 15 | 53.8 | 28 |
| u87 | ai prototyping and design tools | ai powered design tools / ai prototyping tools | 27 | 37,510 | 24 | 50.5 | 40 |
| u85 | visual design principles | principles of design / elements of design | 11 | 65,400 | 20 | 46.6 | 48 |
| u88 | ai in product and ux work (general) | ai for product managers / ai tools for product managers | 24 | 12,020 | 9 | 45.2 | 57 |
| u90 | customer experience (cx) | customer experience / voice of the customer | 12 | 18,820 | 6.5 | 43.1 | 65 |
| u89 | market research and competitor analysis | marketing research / online market research platforms | 20 | 24,760 | 23 | 35.9 | 82 |

No AI unit is in the top 15. "ai tools for product managers" (11 keywords) was a planned AI sub-topic but stays
under the 15-keyword sub-topic floor and sits in the general AI sub-topic. UX writing's median KD of 0 comes from
seven phrases of 110 to 170 searches with no difficulty figure; its head term is KD 18.

## Top 15 by score (v1.1)

| # | Unit | Topic or sub-topic | Head term 1 | Adjusted | KD | Score | v1 score | v1 rank |
|---|---|---|---|---|---|---|---|---|
| 1 | u35 | prioritization (general) | prioritization | 153,570 | 1 | 74.2 | 74.6 | 2 |
| 2 | u59 | product owner and product manager roles (topic total) | product manager | 46,990 | 8 | 73.8 | 75.2 | 1 |
| 3 | u61 | product roles (general) | product manager | 32,770 | 7 | 70.7 | 72.4 | 3 |
| 4 | u34 | prioritization (topic total) | prioritization | 177,330 | 6 | 68.8 | 67.9 | 5 |
| 5 | u42 | web design | website design | 173,680 | 33.5 | 68.4 | 68.2 | 4 |
| 6 | u12 | analytics | analytics | 390,890 | 17 | 67.2 | 67.3 | 6 |
| 7 | u19 | ux and ui design (discipline) | ui ux design | 298,950 | 7 | 67.0 | 67.1 | 7 |
| 8 | u13 | project management | project management | 459,230 | 14 | 66.2 | 65.4 | 8 |
| 9 | u91 | ux writing and content design | ux writing | 6,650 | 0 | 65.7 | new | new |
| 10 | u14 | ux research (topic total) | user testing | 288,630 | 8 | 64.8 | 64.4 | 9 |
| 11 | u66 | product strategy | product market fit | 58,330 | 5 | 64.0 | 60.3 | 12 |
| 12 | u50 | design systems and ui components (topic total) | design system | 115,710 | 6.5 | 61.0 | 60.8 | 10 |
| 13 | u22 | product management (general) | product management | 101,690 | 1 | 60.6 | 60.6 | 11 |
| 14 | u21 | product management (discipline) (topic total) | product management | 131,580 | 8 | 58.5 | 56.9 | 19 |
| 15 | u15 | surveys and questionnaires | closed-ended questions in research | 166,490 | 7 | 57.4 | 55.1 | 24 |
## Score movements larger than 3 points

Every unit moved a little because the percentiles are now taken over 91 units. These moved more than 3 points:

| Unit | v1 | v1.1 | Change | Why |
|---|---|---|---|---|
| u57 retention (general) | 40.1 | 48.8 | +8.7 | adjusted demand 14,900 to 82,500: the review recovered the bare word "retention" (40,500) and "retention def" |
| u08 accessibility definitions (general) | 49.9 | 55.0 | +5.1 | "universal design" and "assistive technologies examples" lowered the median KD (24.5 to 21) and raised the decision and template share |
| u55 retention, churn and engagement (topic total) | 43.4 | 48.1 | +4.7 | adjusted demand 39,340 to 115,060 ("retention", "customer success", "customer loyalty") |
| u54 go-to-market and product marketing | 49.8 | 45.5 | -4.3 | five recovered keywords (ideal customer profile, customer segments, product promotion) raised the median KD (18 to 21) and lowered the decision and template share |
| u10 web and digital accessibility | 40.4 | 44.4 | +4.0 | adjusted demand 47,300 to 124,900: "electronic accessibility" (74,000) is no longer thrown out as noise |
| u66 product strategy | 60.3 | 64.0 | +3.7 | adjusted demand 21,350 to 58,330: "value proposition" (22,200), "unique selling proposition meaning", "unique value proposition", "product line" |

Just under the line: product strategy, discovery and launch (topic total, u65) +3.0 (48.6 to 51.6), surveys and
questionnaires (u15) +2.3, design thinking process and stages (u29) +2.3.

## Files

- `keywords/harvest-articles-ai-2026-10-08.csv`, `keywords/seeds-articles-ai-2026-10-08.csv`
- `keywords/harvest-articles-combined-v1.1-2026-10-08.csv` (`tools/combine_v11.py`)
- `keywords/topic-candidates-v1.1-2026-10-08.csv`, `keywords/keyword-to-topic-v1.1-2026-10-08.csv` (`tools/cluster_v2.py`)
- `keywords/phase4-units-v1.1-2026-10-08.csv` (`tools/phase4_units.py write v1.1`)
- `serps/phase4b-task-ids-2026-10-08.csv`, `serps/page-one-2026-10-08.csv`, `serps/features-2026-10-08.csv`,
  `keywords/trends-2026-10-08.csv`, `keywords/trends-groups-2026-10-08.csv` (`tools/phase4b.py`, `tools/serp_distill.py`)
- `keywords/topic-scores-v1.1-2026-10-08.csv`, `keywords/topic-arena-v1.1-2026-10-08.csv`,
  `keywords/topic-evidence-v1.1-2026-10-08.csv` (`tools/phase4_score.py v1.1`)
