# Phase 4c summary: meaning and field fit per phrase and per topic, re-score v1.2 (9 Oct 2026)

What ran (free, local, no API calls): a fine intent per phrase including a dictionary intent (`tools/harvest.py`,
`fine_intent`, command `reintent`), a field fit per phrase by rules (`field_fit_rule`) and by a manual review of
each unit's 30 highest-volume phrases (`keywords/field-fit-review-2026-10-09.csv`), the jobs flag widened to the
career list (`reflag`), intent, field share and article capacity per unit (`tools/phase4c.py`) and the v1.2 score
(`tools/phase4_score.py v1.2`). Same 91 units, keyword sets, head terms, SERPs and Trends as v1.1. The tree is
`research/seo/topic-tree-v1.2.md`. Spend: $0 (the whole pass is still $3.55 of $5; balance $20.19).

The rule behind it: a topic is on the tree because of what people mean when they search, and only then because
of how many search. Dictionary lookups, job hunters, brand lookups, site lookups and readers from another world
are taken out before anything is counted.

v1.1 stays reproducible: `reflag` keeps the old flags in a `flag_v1_1` column that every v1.1 code path reads.
Re-running the v1.1 chain after all changes reproduced `topic-candidates-v1.1`, `keyword-to-topic-v1.1`,
`phase4-units-v1.1`, `topic-scores-v1.1`, `topic-arena-v1.1` and `topic-evidence-v1.1` byte for byte.

## Rules

**Fine intent** (one per phrase, by wording, first match wins): career (job, salary, hire, resume, cv, interview
questions, certification, pmp, csm, cspo, position, vacancy, opening, recruit, remote, near me, intern, entry
level, apprenticeship; "jobs to be done" and remote research methods excepted), brand, **dictionary** (another
word for, synonym, antonym, pronunciation, spelling, thesaurus, abbreviation, acronym, translations, "in a
sentence", the meaning or definition of a single everyday word, or an everyday word on its own: prioritization,
analytics, metrics, retention, accessibility, agile, design and similar), tool, template, compare, learn, define,
question, other. "software" in "agile software development" names a field, not a tool.

**Field fit** (is the searcher our reader?): no for another world (personal tasks and time, health care and
nursing, HR and employees, school, money and property, home and food, devices and settings, maps and travel,
religion, history and literature, personality, generic small business, engineering software); yes when the
phrase names a method, artifact, role, metric, tool category or activity of product, design or business work;
partial otherwise (generic but plausible, such as "prioritization matrix" or "retention rate"). The manual
review read 1,816 distinct phrases (2,359 unit rows) and changed the rule result for 385 of them, for example:
"one ui" and "ui benefits" (phone software, unemployment insurance), "user interviews legit" and other User
Interviews brand searches (paid-study participants), "keysight advanced design system" (electronics software),
"texas accessibility standards" (buildings), hotel pricing strategies, "data analyst" (the job); and the other
way, agile and SAFe word-order variants, A/B testing written "a b testing", and website accessibility checks.

**Surviving phrase**: field fit yes (full weight) or partial (half weight), fine intent not career, brand or
dictionary, source label not navigational.

## Flag changes

The jobs flag now uses the career list. `reflag` changed **37 rows** of the combined harvest (all from
unflagged to jobs), **0** of the AI harvest and **0** of the section harvest. By topic: product owner and product manager roles 11, product management (discipline) 8, ux research 5, unassigned 3, ux and ui design (discipline) 3, analytics 2, retention, churn and engagement 2, project management 1, web design 1, product strategy, discovery and launch 1.

| Keyword | Volume | v1.1 flag | v1.2 flag |
|---|---|---|---|
| data analyst internship | 9,900 | none | jobs |
| product management vacancy | 9,900 | none | jobs |
| accessibility remote | 8,100 | none | jobs |
| remote accessibility | 8,100 | none | jobs |
| data analyst remote | 6,600 | none | jobs |
| product management remote | 2,900 | none | jobs |
| product owner position | 2,900 | none | jobs |
| product owner positions | 2,900 | none | jobs |
| product owner vacancies | 2,900 | none | jobs |
| product owner vacancy | 2,900 | none | jobs |
| remote product management | 2,900 | none | jobs |
| remote product manager | 2,900 | none | jobs |
| remote project manager | 2,900 | none | jobs |
| internship for product management | 2,400 | none | jobs |
| product management intern | 2,400 | none | jobs |
| product management internship | 2,400 | none | jobs |
| product management internships | 2,400 | none | jobs |
| ux research positions | 1,600 | none | jobs |
| product owner cv example | 1,300 | none | jobs |
| product owner cv examples | 1,300 | none | jobs |
| ui ux internship | 1,300 | none | jobs |
| hire a website designer | 1,000 | none | jobs |
| product management cv | 1,000 | none | jobs |
| ux research intern | 590 | none | jobs |
| ux research internships | 590 | none | jobs |
| ux research internship | 390 | none | jobs |
| jane street strategy and product internship | 320 | none | jobs |
| product owner remote | 320 | none | jobs |
| remote product owner | 320 | none | jobs |
| remote ui | 320 | none | jobs |
| product owner position description | 260 | none | jobs |
| product strategy careers | 260 | none | jobs |
| user interviews careers | 260 | none | jobs |
| product owner cv | 210 | none | jobs |
| ux remote | 210 | none | jobs |
| onboarding plan for new hire | 140 | none | jobs |
| onboarding new hire | 110 | none | jobs |

## Intent and field fit across all article keywords

The 2,884 keywords assigned to a topic (unflagged under the v1.1 rules, volume 100 or more); raw monthly volume.

| Fine intent | Keywords | Share of keywords | Volume | Share of volume |
|---|---|---|---|---|
| define | 1,574 | 54.6% | 6,517,540 | 67.2% |
| learn | 77 | 2.7% | 240,420 | 2.5% |
| compare | 57 | 2.0% | 66,310 | 0.7% |
| template | 315 | 10.9% | 345,580 | 3.6% |
| tool | 167 | 5.8% | 341,140 | 3.5% |
| question | 5 | 0.2% | 2,330 | 0.0% |
| career | 38 | 1.3% | 89,980 | 0.9% |
| brand | 0 | 0.0% | 0 | 0.0% |
| dictionary | 63 | 2.2% | 933,130 | 9.6% |
| other | 588 | 20.4% | 1,168,730 | 12.0% |

| Field fit | Keywords | Volume |
|---|---|---|
| yes | 2,131 | 6,739,050 |
| partial | 547 | 2,359,090 |
| no | 206 | 607,020 |

Removed before counting, as shares of raw volume: dictionary 10%, job hunting 1%, site lookup 5%, another world
5% (brand phrases were flagged out before clustering). The variant-adjusted demand of the assigned keywords goes
from 4,326,060 to 2,450,485 once only surviving phrases count (partial at half weight).

## The v1.2 formula

score = 25 demand + 20 difficulty + 15 intent + 10 soft shelf + 10 answer box + 10 trend + 10 competitors, each
a 0-to-1 component over the 91 units: demand = percentile of `adjusted_volume_field` (variant-adjusted volume
of the surviving phrases); difficulty = percentile of median KD, inverted, with a median of 0 (no figure) at 0.5
for every unit; intent = percentile of `practitioner_share` (learn + compare + template + tool + question) over
the surviving phrases; soft shelf, answer box, trend and competitors unchanged. Per unit also: `field_share`,
`dictionary_share`, `meaning_loss`, `article_capacity` (distinct practical phrase groups; thin under 5, medium 5
to 15, deep above 15), `articles_estimate`, `parked` (half or more of the volume is dictionary, career, brand or
another world) and `what_this_is`. Pillars need 5 or more practical phrase groups; thinner topics are
single-article topics or fold into a parent.

## Prioritization, before and after

- **prioritization** (u34): v1.1 score 68.8 (rank 4), v1.2 55.8 (rank 23). Adjusted demand 177,330, of which 16,045 survives (field share 11%, dictionary 67%). Searches about "moscow prioritization"; the practical angles are "important vs urgent", "urgent vs important matrix" and "matrix prioritization template". Parked: 84% of its searches are dictionary lookups, job hunting, brands or another world; the largest part is dictionary lookups (67%).
- **prioritization (general)** (u35): v1.1 score 74.2 (rank 1), v1.2 55.1 (rank 25). Adjusted demand 153,570, of which 2,390 survives (field share 3%, dictionary 81%). Searches about "must have nice to have priority"; the practical angles are "prioritization tool" and "why is prioritization important". Parked: 96% of its searches are dictionary lookups, job hunting, brands or another world; the largest part is dictionary lookups (81%).
- **prioritization frameworks** (u36): v1.1 score 47.2 (rank 46), v1.2 43.9 (rank 63). Adjusted demand 20,580, of which 13,655 survives (field share 65%, dictionary 0%). Searches about "moscow prioritization"; the practical angles are "important vs urgent", "urgent vs important matrix" and "matrix prioritization template".
- **task and time prioritization** (u37): v1.1 score 42.3 (rank 69), v1.2 39.4 (rank 74). Adjusted demand 3,180, of which 0 survives (field share 0%, dictionary 0%). Nothing survives: its searches are dictionary lookups, job hunting, brands or another world. Parked: 100% of its searches are dictionary lookups, job hunting, brands or another world; the largest part is another world (100%).

What the pillar really is: prioritization frameworks for product and project work (MoSCoW, RICE, the
urgent-important matrix), 13,655 surviving searches and 3 practical phrase groups. It is a single-article topic,
folded into product strategy, discovery and launch.

## Top 15 by v1.2 score

| # | Unit | Head term 1 | Field demand | KD | Practitioner | Career | Capacity | Score | v1.1 score | v1.1 rank | Move |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | u59 product owner and product manager roles | product manager | 31,410 | 8 | 23% | 22% | 3 thin | 78.6 | 73.8 | 2 | up 1 |
| 2 | u61 product roles (general) | product manager | 26,580 | 7 | 7% | 9% | 1 thin | 74.1 | 70.7 | 3 | up 1 |
| 3 | u12 analytics (parked) | analytics | 106,535 | 17 | 26% | 4% | 8 medium | 70.5 | 67.2 | 6 | up 3 |
| 4 | u19 ux and ui design (discipline) | ui ux design | 160,700 | 7 | 1% | 1% | 2 thin | 68.1 | 67.0 | 7 | up 3 |
| 5 | u14 ux research | user testing | 171,380 | 8 | 29% | 1% | 17 deep | 68.0 | 64.8 | 10 | up 5 |
| 6 | u13 project management | project management | 322,805 | 14 | 17% | 1% | 11 medium | 66.4 | 66.2 | 8 | up 2 |
| 7 | u66 product strategy | product market fit | 52,160 | 5 | 9% | 0% | 4 thin | 65.1 | 64.0 | 11 | up 4 |
| 8 | u42 web design | website design | 94,835 | 33.5 | 21% | 1% | 13 medium | 63.9 | 68.4 | 5 | down 3 |
| 9 | u17 usability testing | user testing | 39,100 | 7.5 | 19% | 0% | 4 thin | 62.2 | 56.9 | 19 | up 10 |
| 10 | u26 metrics (general) (parked) | kpi examples | 40,985 | 19 | 36% | 0% | 2 thin | 61.8 | 55.5 | 25 | up 15 |
| 11 | u18 ux research (general) | ux research | 12,600 | 8 | 34% | 11% | 3 thin | 61.6 | 57.4 | 16 | up 5 |
| 12 | u15 surveys and questionnaires | closed-ended questions in research | 94,310 | 7 | 38% | 0% | 10 medium | 60.4 | 57.4 | 15 | up 3 |
| 13 | u22 product management (general) | product management | 47,030 | 1 | 5% | 17% | 4 thin | 60.0 | 60.6 | 13 | same |
| 14 | u50 design systems and ui components | design system | 39,045 | 6.5 | 2% | 0% | 2 thin | 59.5 | 61.0 | 12 | down 2 |
| 15 | u72 product management tools | product management tools | 2,400 | 8 | 100% | 0% | 5 medium | 59.2 | 57.4 | 17 | up 2 |

Article capacity of the top 12: u59 product owner and product manager roles (3); u61 product roles (general) (1); u12 analytics (8); u19 ux and ui design (discipline) (2); u14 ux research (17); u13 project management (11); u66 product strategy (4); u42 web design (13); u17 usability testing (4); u26 metrics (general) (2); u18 ux research (general) (3); u15 surveys and questionnaires (10).

## Units that moved more than 5 points

Component changes in points; "intent" compares v1.2's practitioner component with v1.1's decision-and-template
component.

| Unit | v1.1 | v1.2 | Change | Demand | Difficulty | Intent | Why |
|---|---|---|---|---|---|---|---|
| u35 prioritization (general) | 74.2 | 55.1 | -19.1 | -18.2 | +0.4 | -1.5 | dictionary lookups: "prioritization", "another word for prioritization", synonyms and definitions are 81% of its volume; 2,390 of 153,570 survive |
| u91 ux writing and content design | 65.7 | 51.9 | -13.8 | +0.3 | -9.8 | -4.2 | the difficulty fix: its median KD of 0 came from phrases with no KD figure; now neutral 0.5 |
| u34 prioritization | 68.8 | 55.8 | -13.0 | -11.5 | +0.4 | -2.1 | the same dictionary lookups plus personal task prioritization; 16,045 of 177,330 survive |
| u77 ux design books | 45.7 | 35.6 | -10.1 | +0.5 | +0.0 | -10.6 | book phrases ("best ux books") are not a practitioner intent in the rules |
| u33 company pricing case studies | 40.0 | 30.0 | -10.0 | -0.2 | -9.8 | +0.2 | the difficulty fix (median KD 0, no figures) |
| u57 retention (general) | 48.8 | 38.9 | -9.9 | -10.7 | +0.2 | +0.8 | dictionary lookups ("retention", "retention def", 70%) and employee retention (HR) |
| u76 product management books | 42.8 | 33.3 | -9.5 | +0.3 | +0.0 | -9.7 | same as the other book categories |
| u74 design books (general) | 52.5 | 43.3 | -9.2 | -1.3 | +0.0 | -8.1 | same as the other book categories, and half of its phrases mean book design |
| u75 graphic and visual design books | 45.9 | 37.9 | -8.0 | +0.8 | +0.0 | -9.0 | same as the other book categories |
| u04 scaled agile (safe) | 30.6 | 22.8 | -7.8 | +2.3 | +0.0 | -10.0 | v1.1 counted "framework" as a decision word; by wording these are define |
| u08 accessibility definitions (general) | 55.0 | 47.3 | -7.7 | -14.5 | +0.2 | +6.4 | dictionary lookups (93% of volume); 9,050 of 203,600 survive |
| u51 ui components and patterns | 56.8 | 51.0 | -5.8 | -6.7 | +0.6 | +0.4 | a third of its volume is site lookups and several phrases are other worlds (One UI, game add-ons) |
| u31 pricing strategy (general) | 48.1 | 42.9 | -5.2 | -6.0 | +0.2 | +0.4 | vendor price lists (Originality.ai, Datadog, Zoho) and oil prices are another world |
| u47 a/b testing (general) | 45.8 | 40.7 | -5.1 | +3.0 | +0.0 | -8.2 | v1.1's template share was by keyword count; by volume the practitioner phrases are 2% |
| u17 usability testing | 56.9 | 62.2 | +5.3 | +4.5 | +0.4 | +0.5 | all of its demand survives, so it rises against units that lost theirs |
| u26 metrics (general) | 55.5 | 61.8 | +6.3 | -1.8 | +0.2 | +7.7 | "kpi examples" (14,800) counts as template intent, but the unit is parked (the dictionary word "metrics", crypto and server metrics) |
| u48 a/b testing tools and platforms | 42.1 | 48.4 | +6.3 | +0.8 | +0.2 | +5.2 | a tools list: 61% practitioner |
| u67 new product development and launch | 39.6 | 46.3 | +6.7 | +3.5 | +0.2 | +3.0 | almost all of its demand survives |
| u23 product life cycle | 30.9 | 38.9 | +8.0 | +0.5 | +0.2 | +7.4 | PLM software phrases count as practitioner tool searches |
| u89 market research and competitor analysis | 35.9 | 44.0 | +8.1 | -0.5 | +0.2 | +8.6 | tool phrases ("online market research platforms") count; v1.1 had 0 |
| u90 customer experience (cx) | 43.1 | 52.0 | +8.9 | +2.3 | +0.4 | +6.3 | "customer experience software" and platform phrases now count as practitioner |
| u68 product strategy and discovery (general) | 40.5 | 49.5 | +9.0 | +0.5 | +0.4 | +8.0 | tool and learn phrases count as practitioner; v1.1 had 0 |
| u27 design thinking | 42.6 | 51.9 | +9.3 | +4.5 | +0.2 | +4.6 | the learn phrases of the design thinking process count, and almost all of its demand survives |
| u29 design thinking process and stages | 37.8 | 47.5 | +9.7 | +2.0 | +0.0 | +7.5 | a how-to topic: 72% practitioner among surviving phrases |

**Fell more than 8 points because of dictionary or field fit:** u35 prioritization (general) (74.2 to 55.1); u34 prioritization (68.8 to 55.8); u57 retention (general) (48.8 to 38.9). Just under the line: u08 accessibility definitions (55.0 to 47.3, 93% dictionary). The other falls of more than 8 points come from the difficulty fix (UX writing, company pricing case studies) and from book phrases having no practitioner intent.

## Units with career share above 30%

- u60 product owner: career 31%, site lookup 39%, score 54.9 (rank 26).

## Parked units

- u12 analytics (score 70.5): 55% of its searches are dictionary lookups, job hunting, brands or another world; the largest part is another world (33%).
- u26 metrics (general) (score 61.8): 60% of its searches are dictionary lookups, job hunting, brands or another world; the largest part is dictionary lookups (54%).
- u34 prioritization (score 55.8): 84% of its searches are dictionary lookups, job hunting, brands or another world; the largest part is dictionary lookups (67%).
- u35 prioritization (general) (score 55.1): 96% of its searches are dictionary lookups, job hunting, brands or another world; the largest part is dictionary lookups (81%).
- u08 accessibility definitions (general) (score 47.3): 96% of its searches are dictionary lookups, job hunting, brands or another world; the largest part is dictionary lookups (93%).
- u37 task and time prioritization (score 39.4): 100% of its searches are dictionary lookups, job hunting, brands or another world; the largest part is another world (100%).
- u57 retention (general) (score 38.9): 77% of its searches are dictionary lookups, job hunting, brands or another world; the largest part is dictionary lookups (70%).

## Topics: pillars, single-article topics, parked; the waves

- **Pillars** (12): ux research (17 groups, about 21 articles); project management (11 groups, about 12 articles); product strategy, discovery and launch (6 groups, about 9 articles); web design (13 groups, about 14 articles); product management (discipline) (6 groups, about 8 articles); requirements and prd (8 groups, about 9 articles); user stories and acceptance criteria (10 groups, about 12 articles); ai in product and design work (7 groups, about 9 articles); okrs, kpis and metrics (10 groups, about 11 articles); design thinking (6 groups, about 8 articles); agile, scrum and kanban (16 groups, about 21 articles); personas and journey maps (6 groups, about 8 articles).
- **Single-article topics** (17): product owner and product manager roles (4 groups, about 6 articles); ux and ui design (discipline) (2 groups, about 3 articles); design systems and ui components (2 groups, about 4 articles); product roadmap (2 groups, about 3 articles); stakeholder and change management (3 groups, about 5 articles); pricing strategy (3 groups, about 6 articles); information architecture (2 groups, about 3 articles); customer experience (cx) (1 group, about 2 articles); ux writing and content design (1 group, about 2 articles); growth marketing and funnels (4 groups, about 5 articles); a/b testing and experimentation (3 groups, about 6 articles); accessibility (4 groups, about 7 articles); go-to-market and product marketing (2 groups, about 3 articles); visual design principles (0 groups, about 1 article); retention, churn and engagement (4 groups, about 6 articles); market research and competitor analysis (1 group, about 2 articles); prioritization (3 groups, about 4 articles).
- **Parked** (1): analytics (0 groups, about 0 articles).

Articles possible: product 98, design 71, business 41; about 210 across the tree (the broad fields project management 12 and web design 14 included; analytics is parked).

- **Wave 1 (launch)**: ux research; product strategy, discovery and launch + product roadmap, prioritization; product management (discipline) + product owner and product manager roles; requirements and prd; user stories and acceptance criteria; ai in product and design work (about 81 articles).
- **Wave 2 (months 2 to 4)**: ux and ui design (discipline); design systems and ui components; stakeholder and change management; pricing strategy; information architecture; okrs, kpis and metrics (about 32 articles).
- **Wave 3 (months 5 to 8)**: customer experience (cx); design thinking; ux writing and content design; agile, scrum and kanban; growth marketing and funnels; a/b testing and experimentation (about 44 articles).
- **Wave 4 (months 9 to 12)**: accessibility; go-to-market and product marketing; visual design principles; retention, churn and engagement; personas and journey maps; market research and competitor analysis (about 27 articles).

## Format suggestions for the top 20

| # | Unit | Intent mix | Format | Section |
|---|---|---|---|---|
| 1 | u59 product owner and product manager roles | define 50; career 22; compare 14; other 13 | hub page | Articles |
| 2 | u61 product roles (general) | define 85; career 9; compare 6 | explainer | Articles |
| 3 | u12 analytics | define 57; dictionary 18; tool 10; other 9; career 4; compare 1; learn 1 | hub page | Articles |
| 4 | u19 ux and ui design (discipline) | define 95; other 4; career 1 | hub page | Articles |
| 5 | u14 ux research | define 47; other 28; template 13; tool 11; career 1; question 1 | hub page | Articles |
| 6 | u13 project management | define 84; tool 10; other 2; compare 2; template 1; career 1 | hub page | Articles |
| 7 | u66 product strategy | define 81; other 10; template 8 | explainer | Articles |
| 8 | u42 web design | define 78; template 14; tool 3; other 2; learn 1; career 1 | explainer | Articles |
| 9 | u17 usability testing | define 74; tool 14; other 6; template 5 | hub page | Articles |
| 10 | u26 metrics (general) | dictionary 54; define 34; template 11; other 1 | explainer | Templates |
| 11 | u18 ux research (general) | define 56; template 17; career 11; tool 9; other 7 | explainer | Articles |
| 12 | u15 surveys and questionnaires | other 40; define 31; template 17; tool 12 | hub page | Articles |
| 13 | u22 product management (general) | define 57; other 23; career 17; tool 2; compare 1; template 1 | hub page | Articles |
| 14 | u50 design systems and ui components | define 85; other 14; template 1 | hub page | Articles |
| 15 | u72 product management tools | tool 100 | calculator or tool page | Links |
| 16 | u21 product management (discipline) | define 55; other 25; career 14; tool 5; compare 1 | hub page | Articles |
| 17 | u69 product roadmap | template 45; define 44; other 5; learn 4; tool 3 | template page | Templates |
| 18 | u53 requirements and prd | define 69; template 25; dictionary 2; compare 2; other 1; learn 1; tool 1 | hub page | Templates |
| 19 | u63 change management and leadership | define 78; other 10; compare 5; learn 4; template 3 | explainer | Articles |
| 20 | u38 user stories and acceptance criteria | template 52; define 33; other 12; learn 2; compare 1 | template page | Templates |

## Files

- `tools/harvest.py` (`fine_intent`, `field_fit_rule`, `reintent`, `reflag --rules`), `tools/phase4c.py`,
  `tools/phase4_score.py v1.2`
- `keywords/field-fit-review-2026-10-09.csv` (manual review: keyword, unit, field_fit, reason, intent_override)
- `keywords/harvest-articles-combined-v1.1-2026-10-08.csv`, `keywords/harvest-articles-ai-2026-10-08.csv`,
  `keywords/harvest-sections-2026-10-08.csv` (new columns `fine_intent`, `field_fit`, `field_rule`, `flag_v1_1`)
- `keywords/phase4-units-v1.2-2026-10-09.csv`, `keywords/topic-scores-v1.2-2026-10-09.csv`,
  `keywords/topic-arena-v1.2-2026-10-09.csv`, `keywords/topic-evidence-v1.2-2026-10-09.csv`
- `research/seo/topic-tree-v1.2.md`
