# Phase 4 summary: scoring units, Google Ads check, page-one SERPs, Trends and scores (8 Oct 2026)

Plan: `research/seo/analysis-plan-2026-10-08.md` (Phase 4). US (2840), English. Scripts:
`research/seo/tools/phase4_units.py` (units and head terms), `tools/phase4.py` (pulls and distils),
`tools/phase4_score.py` (scores), `tools/serp_distill.py` (now reads several queries files and writes a `phase`
column). The tree document is `research/seo/topic-tree-v1.md`.

## Spend

| Step | Calls | Cost |
|---|---|---|
| Google Ads search volume, standard queue, 233 keywords in one task (first use on this account, so the task was the probe) | task_post; tasks_ready and task_get free | $0.0600 |
| Google organic SERPs, standard queue, 56 tasks in one task_post (12 head terms reused Phase 0 pulls) | task_post; tasks_ready and task_get/advanced free | $0.0336 |
| Google Trends explore, live: probe 1 task ($0.011, under the $0.02 stop), 13 more, then 4 regroup tasks for terms too small to read | 18 tasks | $0.1980 |
| Total | | $0.2916 (cap $0.60) |
| Balance after (free user_data call) | | $20.42 |

No 50000 errors on any route. Running spend log: `keywords/phase4-spend-2026-10-08.csv`. Raw responses:
`cache/raw/261008-159.json` to `261008-179.json` (Ads post and get, SERP post, 18 Trends tasks) and
`cache/raw/serps-2026-10-08/<slug>.json` (56 new SERPs). Index rows: 1 Ads post, 233 Ads keywords, 1 SERP post,
56 SERP keywords (ids 261008-P4S-NNN), 18 Trends groups.

## Counts

- Units: 84 (25 topic totals, 45 sub-topics, 14 section categories). Dropped as off-scope: 6 section categories
  (book cover and layout design; engineering, interior and fashion design books; rice purity test; Rice University
  scores). No topic unit dropped: the Phase 1b noise rules had already removed Bible journeys, irrigation and
  building systems, device accessibility and nursing prioritization.
- Head terms: 133 distinct (68 distinct head term 1). Google Ads list: 133 head terms plus the top 100 other
  keywords by volume (one per variant series), 233 in all.
- SERPs: 68 head term 1 pages (56 new, 12 from Phase 0). `serps/page-one-2026-10-08.csv` now has 1,103 rows and
  `serps/features-2026-10-08.csv` 134 keywords (78 phase0, 56 phase4). Mapping of head terms to units:
  `serps/phase4-queries-2026-10-08.csv`; task ids: `serps/phase4-task-ids-2026-10-08.csv`.
- Trends: 68 head terms in 18 groups (`keywords/trends-groups-2026-10-08.csv`): rising 45, flat 8, falling 7,
  too small to read 8.

## Google Ads versus Labs

Median ratio (Ads / Labs): **1.00** over 233 keywords. 223 have the same volume and 222 the identical 12-month
series, so the Google Ads check confirms the scale but is not an independent source. Outliers: "product manager"
0.30 (Ads 6,600, Labs 22,200), "data analyst" 0.30, "ui/ux designer" 6.11, "project manager" 4.98.

Is the Phase 1 decline signal real? No. The 12-month slope (Jun-Aug 2026 over Sep-Nov 2025) has a median of 0.62
on both Labs and Ads, but Google Trends over the same weeks has a median of 0.99 on the 57 head terms with a
readable series (Trends is higher for 43 of them). The fall is seasonality in that window. Over five years, 45 of
68 head terms rise on Trends.

## SERP shares (head term 1)

- AI Overview: 68 of 68 head-term SERPs (100%), 4 of them empty placeholders ("sample size calculator", "product
  management tools", "product manager", "statistical sample size calculator"). Across units: 84 of 84, 5 empty.
- Weak page one (3 or more weak results): 6 of 68 head terms (9%): product management books, acceptance criteria
  for user stories examples, website design, design books, user interviews, product roadmap. Across units: 6 of 84.
- People also ask on 65 of 68; video on 12; no featured snippets.

## Score

0 to 100 from ranked percentiles over the 84 units: adjusted demand 25, difficulty inverted 20, decision plus
template share 15, weak-result count 10, AI Overview absent or empty 10 (binary), Trends direction 10 (rising 1,
flat or too small 0.5, falling 0), competitors in the arena inverted 10. owner_fit (empty, 1 to 3) is a separate
column for the owner. Formula also in the header of `keywords/topic-scores-2026-10-08.csv`; components in the c_*
columns.

## Top 15 by score

| # | Unit | Kind | Head term 1 | Adjusted demand | Ads (head 1) | KD | Trend | Arena | Score |
|---|---|---|---|---|---|---|---|---|---|
| 1 | product owner and product manager roles (u59) | topic | product manager | 46,990 | 6,600 | 8 | rising | 4 | 75.2 |
| 2 | prioritization > prioritization (general) (u35) | subtopic | prioritization | 153,570 | 74,000 | 1 | rising | 4 | 74.6 |
| 3 | product owner and product manager roles > product roles (general) (u61) | subtopic | product manager | 32,770 | 6,600 | 7 | rising | 4 | 72.4 |
| 4 | web design (u42) | topic | website design | 151,890 | 49,500 | 35.5 | rising | 4 | 68.2 |
| 5 | prioritization (u34) | topic | prioritization | 171,110 | 74,000 | 5 | rising | 9 | 67.9 |
| 6 | analytics (u12) | topic | analytics | 377,190 | 60,500 | 18 | rising | 4 | 67.3 |
| 7 | ux and ui design (discipline) (u19) | topic | ui ux design | 286,140 | 90,500 | 6.5 | rising | 6 | 67.1 |
| 8 | project management (u13) | topic | project management | 345,140 | 135,000 | 15 | rising | 6 | 65.4 |
| 9 | ux research (u14) | topic | user testing | 264,020 | 18,100 | 8 | rising | 8 | 64.4 |
| 10 | design systems and ui components (u50) | topic | design system | 115,000 | 3,600 | 6.5 | rising | 6 | 60.8 |
| 11 | product management (discipline) > product management (general) (u22) | subtopic | product management | 102,690 | 6,600 | 3 | rising | 9 | 60.6 |
| 12 | product strategy, discovery and launch > product strategy (u66) | subtopic | product market fit | 21,350 | 2,900 | 4 | rising | 10 | 60.3 |
| 13 | ux research > usability testing (u17) | subtopic | user testing | 34,700 | 18,100 | 7 | rising | 7 | 58.4 |
| 14 | ux research > ux research (general) (u18) | subtopic | ux research | 20,220 | 2,900 | 8 | rising | 6 | 58.4 |
| 15 | stakeholder and change management > change management and leadership (u63) | subtopic | change management | 59,040 | 14,800 | 14 | rising | 6 | 57.7 |

Topic totals and their sub-topics are both scored, so pairs appear (u59 and u61 share "product manager"; u35 and
u34 "prioritization"; u14 and u17 "user testing").

## Files

- `research/seo/keywords/phase4-units-2026-10-08.csv`
- `research/seo/keywords/ads-volumes-2026-10-08.csv`
- `research/seo/keywords/trends-2026-10-08.csv`, `trends-groups-2026-10-08.csv`, `trends-regroup-2026-10-08.csv`
- `research/seo/keywords/topic-scores-2026-10-08.csv`, `topic-arena-2026-10-08.csv`
- `research/seo/keywords/phase4-spend-2026-10-08.csv`
- `research/seo/serps/page-one-2026-10-08.csv`, `features-2026-10-08.csv` (Phase 0 and Phase 4, `phase` column)
- `research/seo/serps/phase4-queries-2026-10-08.csv`, `phase4-task-ids-2026-10-08.csv`
- `research/seo/topic-tree-v1.md`
