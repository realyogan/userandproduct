# Phase 2 summary: competitor sizing (8 Oct 2026)

Plan: `research/seo/analysis-plan-2026-10-08.md` (Phase 2). Script: `research/seo/tools/phase2.py`
(subcommands domains, traffic, traffic-distil, pick, ranked, ranked-distil, coverage). US (2840), English.

## Spend

| Item | Rows | Cost |
|---|---|---|
| bulk_traffic_estimation, 96 domains, one task (first use on this account, so the single task was the probe) | 96 | $0.0235 (= $0.012 + 96 x $0.00012, as priced) |
| ranked_keywords probe, productplan.com | 500 | $0.0720 |
| ranked_keywords, atlassian.com, coursera.org, amplitude.com | 3 x 500 | $0.2160 |
| Total | | $0.3115 |
| Balance after (free user_data call) | | $20.97 |

No 50000 errors. Raw responses: `cache/raw/261008-137.json` (traffic), `261008-138.json` to `261008-141.json`
(ranked keywords), one index row each (note "phase2; N rows; $cost").

## Domain list

96 domains: every domain in the five `competitors/<section>-competitors.csv` files plus `competitors/seeds.csv`,
deduped, without "www." (109), minus the platform list (reddit, linkedin, youtube, en.wikipedia, quora, medium,
pinterest, scribd, amazon, google, github, facebook, x, twitter, instagram). Also treated as platforms and dropped:
gist.github.com, dhavalthakur.medium.com and rysullivan.medium.com. The list came in under the expected 120 to 160
because Phase 0 kept only domains with two or more page-one results plus the seeds.

## Traffic tiers

File: `competitors/traffic-2026-10-08.csv` (domain, organic_etv, organic_count, paid_etv, sections,
page_one_total, tier). organic_etv is the estimated monthly US organic traffic. Tier A >= 1,000,000; B >= 100,000;
C >= 10,000; D below. Counts: A 5, B 11, C 25, D 55. Each `<section>-competitors.csv` now carries organic_etv and
tier columns (platform rows are empty).

| Tier | Domain | Organic traffic (etv) | Ranked keywords | Sections | Page-one total |
|---|---|---|---|---|---|
| A | omnicalculator.com | 11,060,954 | 1,050,597 | tools | 2 |
| A | goodreads.com | 10,251,469 | 3,759,667 | books | 3 |
| A | geeksforgeeks.org | 2,532,368 | 1,688,847 | articles | 2 |
| A | coursera.org | 1,861,038 | 476,979 | articles | 3 |
| A | figma.com | 1,436,611 | 198,167 | articles, links, templates | 8 |
| B | salesforce.com | 971,723 | 248,025 | articles | 2 |
| B | atlassian.com | 420,717 | 192,758 | articles, links, tools, templates | 12 |
| B | notion.com | 320,481 | 59,235 | templates | 9 |
| B | wallstreetprep.com | 200,075 | 95,222 | tools | 2 |
| B | producthunt.com | 199,284 | 46,074 | links | 0 |
| B | smartsheet.com | 188,985 | 87,639 | templates | 2 |
| B | miro.com | 163,746 | 48,699 | links, templates | 3 |
| B | surveymonkey.com | 144,123 | 43,247 | tools | 0 |
| B | clickup.com | 118,417 | 112,057 | templates | 4 |
| B | fontawesome.com | 111,339 | 25,719 | links | 2 |
| B | w3.org | 109,784 | 294,059 | articles | 2 |

Reading the tiers:

- The A tier is generalists that hold a few of our page-one slots by sheer domain size (calculators, Goodreads,
  GeeksforGeeks, Coursera) plus Figma. None of them is a UX or product publication.
- The publications and experts the site is modeled on are small by this measure: NN/g 63,183, IxDF 32,981,
  UX Collective 18,851, Smashing 16,972, Lenny's 15,099, Mind the Product 1,357, SVPG 6,576, Product Talk 5,301.
- The SaaS blogs with glossaries sit in C and D: Aha! 28,822, Dovetail 27,468, Amplitude 25,299, ProductPlan
  20,541, Pendo 12,259, Userpilot 9,854, Maze 6,654, Productboard 6,136.
- Directories for Links are tiny: bookmarks.design 478, uxtools.co 260, designresourc.es 225, toools.design
  1,080, startupstash.com 6,085; futurepedia.io (AI tools) 30,161 is the exception; producthunt.com 199,284.
- Anomaly: hotjar.com shows 1,015, far below its known size; it likely reflects a domain move. Treat as no data.

All C and D domains (from the same file):

- C: online.hbs.edu 68,686; nngroup.com 63,183; creately.com 54,535; fivebooks.com 51,823; mostrecommendedbooks.com 44,594; statsig.com 37,222; ixdf.org 32,981; cufonfonts.com 30,640; futurepedia.io 30,161; aha.io 28,822; airfocus.com 28,441; dovetail.com 27,468; amplitude.com 25,299; usertesting.com 25,214; mural.co 21,293; productplan.com 20,541; uxdesign.cc 18,851; measuringu.com 18,525; optimizely.com 18,092; scrum.org 17,058; smashingmagazine.com 16,972; lennysnewsletter.com 15,099; intercom.com 14,638; uxplanet.org 13,291; pendo.io 12,259
- D: userpilot.com 9,854; mountaingoatsoftware.com 9,692; productschool.com 7,453; prototypr.io 6,809; maze.co 6,654; mixpanel.com 6,616; cxl.com 6,582; svpg.com 6,576; productboard.com 6,136; startupstash.com 6,085; producttalk.org 5,301; ones.com 5,289; nextleap.app 3,947; pragmaticinstitute.com 3,764; freedesignresources.net 3,588; alistapart.com 3,463; baymard.com 3,302; reforge.com 3,236; lawsofux.com 2,531; abtestguide.com 2,077; andrewchen.com 2,036; userflow.com 1,854; evanmiller.org 1,640; uxmatters.com 1,422; mindtheproduct.com 1,357; jpattonassociates.com 1,242; fibery.io 1,220; toools.design 1,080; hotjar.com 1,015; boxesandarrows.com 1,000; cutlefish.substack.com 808; lukew.com 807; blog.uxfol.io 685; productcoalition.com 594; bringthedonuts.com 586; bookauthority.org 583; bookmarks.design 478; growth.design 393; productmanagementexercises.com 332; romanpichler.com 320; uxtools.co 260; melissaperri.com 253; designresourc.es 225; centercentre.com 189; juliezhuo.com 185; departmentofproduct.com 170; okrinstitute.org 168; gibsonbiddle.com 151; growthunhinged.com 151; johannesippen.com 72; roadmunk.com 70; undesign.learn.uno 31; uxdatabase.io 20; behindthecmo.com 3; uxbooth.com 0

## Ranked keywords, four Articles competitors

Pick rule: the four domains in `competitors/articles-competitors.csv` with the highest page_one_count, type
publication, saas, expert or education, platforms excluded; ties broken by organic_etv. Result: productplan.com
(8 page-one results), atlassian.com (5), then a three-way tie at 3 broken by traffic: coursera.org (1,861,038)
and amplitude.com (25,299) over usertesting.com (25,214) and productschool.com (3). Request as specified: limit 500,
volume >= 100, ordered by volume descending. Files: `competitors/ranked-<domain>-2026-10-08.csv` (keyword, volume,
difficulty, position, url, intent).

| Domain | Rows | Lowest volume in the pull | Rows at position 1-10 | Rows mapped to a v2 topic |
|---|---|---|---|---|
| productplan.com | 500 | 3,600 | 95 | 96 |
| atlassian.com | 500 | 27,100 | 136 | 32 |
| coursera.org | 500 | 90,500 | 117 | 28 |
| amplitude.com | 500 | 3,600 | 151 | 65 |

**The main caveat.** Ordering by volume and stopping at 500 rows returns each domain's 500 biggest keywords,
not its on-topic ones. The pulls stop at volume 3,600 (ProductPlan, Amplitude), 27,100 (Atlassian) and 90,500
(Coursera), and are dominated by off-topic head terms (Coursera: "chatgpt", "fafsa"; Atlassian: "how to screenshot
on mac"; ProductPlan: "jira", "smart goals", "gantt charts"). The domains hold 7,536 (ProductPlan), 70,063
(Atlassian), 199,338 (Coursera) and 6,970 (Amplitude) keywords at volume >= 100 in total. So the coverage table
below measures who holds the head terms of each topic, and a "gap" means none of the four holds five head terms
there; it does not prove they have no pages. ProductPlan showing 0 in "product roadmap" is the clearest example:
it ranks for "roadmap" and "roadmaps" (both mapped to no v2 topic because the single token cannot reach the
two-token rule), and its many mid-volume roadmap pages sit below volume 3,600. A sharper pull, if wanted later:
the same endpoint filtered to on-topic words (for example keyword like "%roadmap%" or position <= 20) costs the
same per task.

## Coverage by topic

File: `competitors/coverage-by-topic-2026-10-08.csv` (topic, subtopic, one column per domain, total, gap).
Mapping: exact match against `keywords/keyword-to-topic-v2-2026-10-08.csv` (67 keywords), else the v2 topic or
sub-topic sharing the most non-stopword tokens with its name and top keywords, at least two (154), else
unmapped (1,779 of 2,000). Split topics are matched through their sub-topics. gap = yes when no competitor has 5
or more ranked keywords in the row. Adjusted volume and median KD come from Phase 1b (variant-adjusted:
each distinct volume and 12-month series counted once).

| Topic | Sub-topic | productplan.com | atlassian.com | coursera.org | amplitude.com | Total | Gap | Adjusted volume (v2) | Median KD (v2) |
|---|---|---|---|---|---|---|---|---|---|
| agile, scrum and kanban | agile methodology (general) | 2 | 7 | 3 | 0 | 12 | no | 296,030 | 39.5 |
| agile, scrum and kanban | agile project management | 1 | 2 | 7 | 0 | 10 | no | 147,930 | 47 |
| agile, scrum and kanban | scaled agile (safe) | 8 | 0 | 0 | 0 | 8 | no | 12,500 | 45 |
| agile, scrum and kanban | scrum, sprints and backlog | 2 | 1 | 0 | 0 | 3 | yes | 58,460 | 24 |
| agile, scrum and kanban | agile manifesto and principles | 8 | 9 | 2 | 0 | 19 | no | 8,200 | 31 |
| accessibility | accessibility definitions (general) | 0 | 0 | 0 | 0 | 0 | yes | 199,400 | 24.5 |
| accessibility | guidelines and compliance (wcag, ada, 508) | 0 | 0 | 0 | 0 | 0 | yes | 35,500 | 67 |
| accessibility | web and digital accessibility | 0 | 0 | 0 | 0 | 0 | yes | 47,300 | 94 |
| accessibility | accessibility testing and checkers | 0 | 0 | 0 | 0 | 0 | yes | 14,860 | 76 |
| analytics |  | 1 | 4 | 0 | 6 | 11 | no | 377,190 | 18 |
| project management |  | 5 | 3 | 4 | 0 | 12 | no | 345,140 | 15 |
| ux research | surveys and questionnaires | 0 | 0 | 0 | 1 | 1 | yes | 146,280 | 8 |
| ux research | interviews and focus groups | 0 | 0 | 0 | 0 | 0 | yes | 62,820 | 16 |
| ux research | usability testing | 0 | 0 | 0 | 0 | 0 | yes | 34,700 | 7 |
| ux research | ux research (general) | 0 | 0 | 0 | 12 | 12 | no | 20,220 | 8 |
| ux and ui design (discipline) |  | 4 | 0 | 0 | 0 | 4 | yes | 286,140 | 6.5 |
| growth marketing and funnels |  | 0 | 0 | 4 | 3 | 7 | yes | 289,200 | 22 |
| product management (discipline) | product management (general) | 9 | 0 | 0 | 0 | 9 | no | 102,690 | 3 |
| product management (discipline) | product life cycle | 8 | 0 | 1 | 0 | 9 | no | 29,720 | 36 |
| okrs, kpis and metrics | okrs | 1 | 2 | 0 | 3 | 6 | yes | 83,780 | 24 |
| okrs, kpis and metrics | metrics (general) | 1 | 0 | 0 | 1 | 2 | yes | 113,780 | 19 |
| design thinking | design thinking (general) | 0 | 0 | 0 | 0 | 0 | yes | 25,480 | 27 |
| design thinking | design thinking process and stages | 0 | 0 | 0 | 0 | 0 | yes | 8,330 | 52.5 |
| pricing strategy | pricing strategy (general) | 0 | 0 | 0 | 0 | 0 | yes | 92,020 | 20 |
| pricing strategy | pricing strategy types and models | 0 | 0 | 0 | 0 | 0 | yes | 28,190 | 19 |
| pricing strategy | company pricing case studies | 0 | 0 | 0 | 0 | 0 | yes | 8,980 | 0 |
| prioritization | prioritization (general) | 4 | 0 | 0 | 0 | 4 | yes | 153,570 | 1 |
| prioritization | prioritization frameworks | 3 | 0 | 0 | 0 | 3 | yes | 14,360 | 21 |
| prioritization | task and time prioritization | 1 | 4 | 3 | 0 | 8 | yes | 3,180 | 10 |
| user stories and acceptance criteria | user story examples and templates | 0 | 0 | 0 | 0 | 0 | yes | 11,650 | 13 |
| user stories and acceptance criteria | user stories (general) | 1 | 0 | 0 | 0 | 1 | yes | 45,430 | 22.5 |
| user stories and acceptance criteria | acceptance criteria | 0 | 0 | 0 | 0 | 0 | yes | 4,330 | 9.5 |
| web design |  | 0 | 0 | 0 | 0 | 0 | yes | 151,890 | 35.5 |
| personas and journey maps | journey maps and user flows | 5 | 0 | 0 | 9 | 14 | no | 31,130 | 19 |
| personas and journey maps | personas | 2 | 0 | 0 | 1 | 3 | yes | 13,180 | 25 |
| a/b testing and experimentation | a/b testing (general) | 0 | 0 | 0 | 5 | 5 | no | 29,570 | 48 |
| a/b testing and experimentation | a/b testing tools and platforms | 0 | 0 | 0 | 3 | 3 | yes | 3,650 | 23 |
| a/b testing and experimentation | a/b testing in marketing (email, landing pages, ads) | 0 | 0 | 2 | 0 | 2 | yes | 840 | 38 |
| design systems and ui components | ui components and patterns | 0 | 0 | 2 | 0 | 2 | yes | 68,590 | 1 |
| design systems and ui components | design systems | 0 | 0 | 0 | 0 | 0 | yes | 46,410 | 26.5 |
| requirements and prd |  | 8 | 0 | 0 | 0 | 8 | no | 78,170 | 9 |
| go-to-market and product marketing |  | 6 | 0 | 0 | 11 | 17 | no | 81,600 | 18 |
| retention, churn and engagement | retention rate formulas and calculation | 0 | 0 | 0 | 1 | 1 | yes | 4,870 | 16 |
| retention, churn and engagement | retention (general) | 4 | 0 | 0 | 1 | 5 | yes | 14,900 | 22 |
| retention, churn and engagement | customer retention and loyalty | 0 | 0 | 0 | 1 | 1 | yes | 19,570 | 26 |
| product owner and product manager roles | product owner | 0 | 0 | 0 | 0 | 0 | yes | 16,120 | 8 |
| product owner and product manager roles | product roles (general) | 1 | 0 | 0 | 0 | 1 | yes | 32,770 | 7 |
| stakeholder and change management | change management and leadership | 1 | 0 | 0 | 0 | 1 | yes | 59,040 | 14 |
| stakeholder and change management | stakeholder management | 0 | 0 | 0 | 0 | 0 | yes | 6,120 | 18 |
| product strategy, discovery and launch | product strategy | 3 | 0 | 0 | 1 | 4 | yes | 21,350 | 4 |
| product strategy, discovery and launch | new product development and launch | 2 | 0 | 0 | 2 | 4 | yes | 16,100 | 10 |
| product strategy, discovery and launch | product strategy and discovery (general) | 4 | 0 | 0 | 4 | 8 | yes | 2,250 | 5 |
| product roadmap |  | 0 | 0 | 0 | 0 | 0 | yes | 11,300 | 10 |
| information architecture |  | 1 | 0 | 0 | 0 | 1 | yes | 5,500 | 11 |
| unmapped |  | 404 | 468 | 472 | 435 | 1779 |  |  |  |

Where the four do hold head terms: ProductPlan in agile (scaled agile 8, manifesto 8), product management
(general 9, life cycle 8), requirements and PRD (8) and go-to-market (6); Atlassian in agile (manifesto 9,
methodology 7); Coursera in agile project management (7); Amplitude in ux research (general 12), go-to-market (11),
journey maps and user flows (9) and analytics (6).

## Gaps: where every competitor is thin

41 of 54 rows are gaps. The largest by Phase 1b adjusted volume:

| # | Topic | Sub-topic | Adjusted volume | Median KD | Ranked keywords across the four |
|---|---|---|---|---|---|
| 1 | growth marketing and funnels |  | 289,200 | 22 | 7 |
| 2 | ux and ui design (discipline) |  | 286,140 | 6.5 | 4 |
| 3 | accessibility | accessibility definitions (general) | 199,400 | 24.5 | 0 |
| 4 | prioritization | prioritization (general) | 153,570 | 1 | 4 |
| 5 | web design |  | 151,890 | 35.5 | 0 |
| 6 | ux research | surveys and questionnaires | 146,280 | 8 | 1 |
| 7 | okrs, kpis and metrics | metrics (general) | 113,780 | 19 | 2 |
| 8 | pricing strategy | pricing strategy (general) | 92,020 | 20 | 0 |
| 9 | okrs, kpis and metrics | okrs | 83,780 | 24 | 6 |
| 10 | design systems and ui components | ui components and patterns | 68,590 | 1 | 2 |
| 11 | ux research | interviews and focus groups | 62,820 | 16 | 0 |
| 12 | stakeholder and change management | change management and leadership | 59,040 | 14 | 1 |

Read with the caveat above: these four domains are product and agile SaaS plus a course catalog, so design-side
topics (accessibility, web design, ux and ui design, design systems, ux research methods) and business-side
topics (pricing, growth, metrics) were never their ground. The design gaps are better tested against NN/g, IxDF
and Smashing in a later pull; their traffic tiers (C) are listed above.

## Files

- `research/seo/competitors/traffic-2026-10-08.csv`
- `research/seo/competitors/{articles,links,books,tools,templates}-competitors.csv` (organic_etv, tier added)
- `research/seo/competitors/ranked-{productplan.com,atlassian.com,coursera.org,amplitude.com}-2026-10-08.csv`
- `research/seo/competitors/coverage-by-topic-2026-10-08.csv`
- `research/seo/tools/phase2.py`
