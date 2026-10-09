# Phase 1b summary: keyword suggestions re-harvest and v2 topics (8 Oct 2026)

Why: Phase 1 used keyword ideas sorted by volume, which pulled category-wide noise (see
`keywords/phase1-summary-2026-10-08.md`). Phase 1b re-harvests 30 seeds with DataForSEO Labs keyword
suggestions (live), which is phrase match: every result contains the seed phrase, so the volume sort is
safe. US (2840), English, one task per seed, limit 150, volume >= 100, ordered by volume descending.

Files:

- Seeds: `keywords/seeds-articles-1b-2026-10-08.csv` (30 seeds: 10 design, 11 product, 7 business, 2 off-map)
- Harvest: `keywords/harvest-articles-1b-2026-10-08.csv` (same columns and flag rules as the Phase 1 harvest)
- Combined on-topic set: `keywords/harvest-articles-combined-2026-10-08.csv` (harvest columns + `source`: 1a, 1b, both)
- Topics: `keywords/topic-candidates-v2-2026-10-08.csv` (one row per topic with an empty subtopic = the topic
  total, then one row per sub-topic), `keywords/keyword-to-topic-v2-2026-10-08.csv`
- Raw responses: `cache/raw/261008-105.json` to `cache/raw/261008-136.json` (index rows 261008-105 to -136)
- Scripts: `tools/harvest.py` (new `--endpoint ideas|suggestions`, `--limit`, `--tag`; the defaults still
  reproduce Phase 1 exactly), `tools/combine_1b.py`, `tools/cluster_v2.py`. `tools/dataforseo_client.py` now
  ignores index rows whose note records an error status, so a failed call can be retried.

## Spend

| Item | Cost |
|---|---|
| Probe (seed "ux research", 59 rows) | $0.0191 (= $0.012 + 59 x $0.00012, as priced) |
| Remaining 29 seeds | $0.6353 |
| Two calls that returned 50000 Internal Error ("user persona", "product backlog"), retried once each | $0.0000 |
| Total | $0.6544 (cap $1.10) |
| Balance after | $21.28 |

## Rows per seed

Nine seeds hit the 150-row cap: design system, accessibility, journey map, product management, user stories,
agile, product owner, pricing strategy, design thinking. Then okr 138, a/b testing 127, prioritization 118,
product strategy 100, retention rate 91, product roadmap 85, usability testing 80, ux research 59,
information architecture 53.

**Seeds under 50 rows (12):** product backlog 49, stakeholder management 42, product requirements 35, user
interviews 27, user persona 25, jobs to be done 19, ux writing 18, product analytics 18, product discovery 12,
saas metrics 4, ux metrics 2, product metrics 1. Phrase match is narrow by design: "ux metrics", "product
metrics" and "saas metrics" barely exist as US searches at volume 100+ in those exact words; the demand sits
under "kpi", "okr" and "metrics" (see the okrs, kpis and metrics topic).

## Keywords

- 1b: 2,440 distinct keywords (2,202 unflagged; flagged: jobs 147, brand 54, course 37).
- Combined on-topic set: 3,255 distinct keywords = 2,393 from 1b only + 815 from 1a only + 47 in both.
  3,017 are unflagged and were clustered.
- Clustered: 2,641 keywords in 25 topics (16 split into 45 sub-topics); 376 unassigned, of which 264 are
  explicit noise (below).

**Read total volume with care.** Keyword suggestions returns many word-order variants that share one volume
and one 12-month series ("agile methodology", "agile approach", "agile computing" and 14 more all at 135,000;
Google groups close variants). Total volume therefore double-counts heavily for big head terms. The table
adds a variant-adjusted volume (each distinct volume + 12-month series counted once; computed for this
summary only, not a CSV column). Agile drops from 3.88M to 370K, design thinking from 237K to 34K, user
stories from 203K to 61K. Rank by the adjusted figure.

## v2 candidate topics (20 or more keywords), sorted by total volume

Sub-topics are indented under their topic. A topic with 60 or more keywords was split where the phrases
separate; a sub-topic needs 15 or more keywords, smaller ones fold into the topic's "(general)" remainder
(two remainders are under 15: product roles 11, product strategy and discovery 7). Shares: decision = how,
vs, best, examples, template, framework, tools, guide and similar (as Phase 1); question = starts with how,
what, why, when, which, who, is, are, can, should, do, does; template = contains template, example, checklist,
format or sample (singular or plural). Competitor articles: same sitemap approximation as Phase 1.

| Topic / sub-topic | Domain | Keywords | Total volume | Variant-adjusted volume | Median vol | Median KD | Decision | Question | Template | Competitor articles / domains | Top keywords |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **agile, scrum and kanban** | product | 243 | 3,883,210 | 370,120 | 4,400 | 36 | 0.14 | 0.05 | 0.05 | 43 / 16 | agile agile; agile agile software; agile approach; agile approaches; agile computing |
| &nbsp;&nbsp;&nbsp;&nbsp;- agile methodology (general) |  | 96 | 2,969,680 | 296,030 | 4,400 | 39.5 | 0.09 | 0.08 | 0.00 | 73 / 20 | agile agile; agile agile software; agile approach; agile approaches; agile computing |
| &nbsp;&nbsp;&nbsp;&nbsp;- agile project management |  | 42 | 504,330 | 147,930 | 9,900 | 47 | 0.02 | 0.00 | 0.00 | 61 / 18 | agile project development; agile and project management; agile development and project management; agile development project management; agile for project management |
| &nbsp;&nbsp;&nbsp;&nbsp;- scaled agile (safe) |  | 25 | 184,000 | 12,500 | 8,100 | 45 | 0.44 | 0.00 | 0.00 | 14 / 8 | agile safe; agile safe framework; agile scaled framework; agile scaling framework; agile scaling frameworks |
| &nbsp;&nbsp;&nbsp;&nbsp;- scrum, sprints and backlog |  | 65 | 131,200 | 58,460 | 260 | 24 | 0.20 | 0.06 | 0.20 | 36 / 16 | scrum master; agile development scrum; agile for scrum; agile i scrum; agile methodology scrum |
| &nbsp;&nbsp;&nbsp;&nbsp;- agile manifesto and principles |  | 15 | 94,000 | 8,200 | 6,600 | 31 | 0.00 | 0.00 | 0.00 | 38 / 16 | agile development manifesto; agile manifesto; agile methodology manifesto; agile project management manifesto; agile software development manifesto |
| **accessibility** | design | 99 | 780,060 | 291,660 | 3,600 | 76 | 0.07 | 0.01 | 0.01 | 61 / 12 | accessibility; accessibility accessibility; accessibility def; accessibility definition; define accessibility |
| &nbsp;&nbsp;&nbsp;&nbsp;- accessibility definitions (general) |  | 18 | 414,700 | 199,400 | 8,100 | 24.5 | 0.06 | 0.06 | 0.00 | 0 / 0 | accessibility; accessibility accessibility; accessibility def; accessibility definition; define accessibility |
| &nbsp;&nbsp;&nbsp;&nbsp;- guidelines and compliance (wcag, ada, 508) |  | 25 | 136,600 | 35,500 | 5,400 | 67 | 0.04 | 0.00 | 0.04 | 82 / 14 | accessibility 508; accessibility 508 compliance; accessibility standard; accessibility standards; accessibility ada |
| &nbsp;&nbsp;&nbsp;&nbsp;- web and digital accessibility |  | 19 | 118,100 | 47,300 | 3,600 | 94 | 0.16 | 0.00 | 0.00 | 53 / 14 | accessibility heuristic; accessibility heuristics; internet accessibility; web accessibility guide; web content accessibility |
| &nbsp;&nbsp;&nbsp;&nbsp;- accessibility testing and checkers |  | 37 | 110,660 | 14,860 | 2,900 | 76 | 0.05 | 0.00 | 0.00 | 16 / 5 | accessibility widget accessibe; accessibility check; accessibility checker; check for accessibility; accessibility check for website |
| **analytics** | business | 93 | 386,580 | 377,190 | 1,600 | 18 | 0.09 | 0.08 | 0.00 | 115 / 19 | analytics; data analyst; data analytics; business analytics; free web analytics service |
| **project management** | product | 74 | 354,780 | 345,140 | 1,600 | 15 | 0.22 | 0.01 | 0.03 | 28 / 11 | project management; project manager; project management tools; project management tool; program manager |
| **ux research** | design | 213 | 330,250 | 264,020 | 390 | 8 | 0.12 | 0.05 | 0.11 | 228 / 24 | user interviews; close-ended questions in research; closed-ended questions in research; online survey platforms; web soil survey |
| &nbsp;&nbsp;&nbsp;&nbsp;- surveys and questionnaires |  | 61 | 184,030 | 146,280 | 880 | 8 | 0.15 | 0.00 | 0.15 | 105 / 15 | close-ended questions in research; closed-ended questions in research; online survey platforms; web soil survey; online surveys |
| &nbsp;&nbsp;&nbsp;&nbsp;- interviews and focus groups |  | 24 | 66,780 | 62,820 | 480 | 16 | 0.00 | 0.12 | 0.00 | 6 / 3 | user interviews; user interviews platform; user interviews focus group; user interviews focus groups; user interviews com |
| &nbsp;&nbsp;&nbsp;&nbsp;- usability testing |  | 81 | 51,370 | 34,700 | 260 | 7 | 0.14 | 0.06 | 0.14 | 387 / 25 | user testing; user testing questions; testing usability; usability testing; user acceptance testing |
| &nbsp;&nbsp;&nbsp;&nbsp;- ux research (general) |  | 47 | 28,070 | 20,220 | 390 | 8 | 0.13 | 0.04 | 0.09 | 58 / 12 | qualitative data examples; action research; ux research; ux research positions; user research |
| **ux and ui design (discipline)** | design | 110 | 293,240 | 286,140 | 320 | 6.5 | 0.02 | 0.01 | 0.00 | 57 / 13 | ui ux design; one ui themes; one ui; ux design; ui/ux designer |
| **growth marketing and funnels** | business | 39 | 292,150 | 289,200 | 1,600 | 22 | 0.05 | 0.05 | 0.03 | 225 / 30 | content marketing; marketing strategy; marketing funnel; content marketing services; growth and development |
| **product management (discipline)** | product | 94 | 272,980 | 132,410 | 2,400 | 8 | 0.07 | 0.06 | 0.01 | 21 / 9 | associate product management; product life cycle; product management vacancy; product life cycle management software; product management pay |
| &nbsp;&nbsp;&nbsp;&nbsp;- product management (general) |  | 74 | 223,060 | 102,690 | 2,400 | 3 | 0.09 | 0.07 | 0.01 | 0 / 0 | associate product management; product management vacancy; product management pay; management of product; management product |
| &nbsp;&nbsp;&nbsp;&nbsp;- product life cycle |  | 20 | 49,920 | 29,720 | 1,900 | 36 | 0.00 | 0.05 | 0.00 | 12 / 6 | product life cycle; product life cycle management software; product life cycle management system; product life cycle management systems; product lifecycle management system |
| **okrs, kpis and metrics** | business | 153 | 269,480 | 197,560 | 480 | 22 | 0.19 | 0.10 | 0.15 | 25 / 11 | metrics; okr; kpi examples; meaning of okr; okr meaning |
| &nbsp;&nbsp;&nbsp;&nbsp;- okrs |  | 119 | 149,860 | 83,780 | 320 | 24 | 0.23 | 0.12 | 0.18 | 18 / 10 | okr; meaning of okr; okr meaning; okr means; kpi vs okr |
| &nbsp;&nbsp;&nbsp;&nbsp;- metrics (general) |  | 34 | 119,620 | 113,780 | 800 | 19 | 0.06 | 0.03 | 0.03 | 25 / 17 | metrics; kpi examples; dora metrics; synonym metrics; thesaurus metrics |
| **design thinking** | design | 137 | 237,390 | 33,640 | 260 | 41 | 0.05 | 0.04 | 0.01 | 28 / 8 | design & thinking; design and design thinking; design design thinking; design for thinking; design of thinking |
| &nbsp;&nbsp;&nbsp;&nbsp;- design thinking (general) |  | 81 | 194,990 | 25,480 | 390 | 27 | 0.01 | 0.04 | 0.02 | 64 / 14 | design & thinking; design and design thinking; design design thinking; design for thinking; design of thinking |
| &nbsp;&nbsp;&nbsp;&nbsp;- design thinking process and stages |  | 56 | 42,400 | 8,330 | 210 | 52.5 | 0.11 | 0.04 | 0.00 | 30 / 7 | design thinking design process; design thinking process; design thinking processes; process design thinking; process of design thinking |
| **pricing strategy** | business | 185 | 227,850 | 126,510 | 390 | 13 | 0.03 | 0.04 | 0.05 | 70 / 20 | originality pricing; dynamic pricing; price pricing strategy; pricing and pricing strategy; pricing and strategy |
| &nbsp;&nbsp;&nbsp;&nbsp;- pricing strategy (general) |  | 95 | 171,260 | 92,020 | 720 | 20 | 0.00 | 0.07 | 0.02 | 110 / 25 | originality pricing; price pricing strategy; pricing and pricing strategy; pricing and strategy; pricing policy strategy |
| &nbsp;&nbsp;&nbsp;&nbsp;- pricing strategy types and models |  | 39 | 38,960 | 28,190 | 390 | 19 | 0.13 | 0.00 | 0.21 | 35 / 15 | dynamic pricing; competitive pricing; psychological pricing; marketing pricing strategy examples; pricing strategy examples marketing |
| &nbsp;&nbsp;&nbsp;&nbsp;- company pricing case studies |  | 51 | 17,630 | 8,980 | 170 | 0 | 0.00 | 0.02 | 0.00 | 21 / 11 | what is retail pricing; define retail pricing; retail pricing definition; amazon pricing strategy; amazon's pricing strategy |
| **prioritization** | product | 108 | 209,300 | 171,110 | 320 | 5 | 0.13 | 0.07 | 0.07 | 41 / 8 | prioritization; another word for prioritization; use high priority notification meaning; prioritization synonym; prioritization synonyms |
| &nbsp;&nbsp;&nbsp;&nbsp;- prioritization (general) |  | 62 | 177,170 | 153,570 | 435 | 1 | 0.11 | 0.10 | 0.06 | 0 / 0 | prioritization; another word for prioritization; use high priority notification meaning; prioritization synonym; prioritization synonyms |
| &nbsp;&nbsp;&nbsp;&nbsp;- prioritization frameworks |  | 30 | 21,280 | 14,360 | 320 | 21 | 0.23 | 0.03 | 0.13 | 29 / 8 | moscow prioritization; matrix for prioritization; matrix prioritization; prioritization matrix; priority matrix |
| &nbsp;&nbsp;&nbsp;&nbsp;- task and time prioritization |  | 16 | 10,850 | 3,180 | 320 | 10 | 0.00 | 0.06 | 0.00 | 23 / 11 | prioritization of tasks; prioritization task; task prioritization; tasks prioritization; prioritization and time management |
| **user stories and acceptance criteria** | product | 177 | 203,490 | 61,410 | 720 | 14 | 0.30 | 0.10 | 0.41 | 12 / 10 | epic user web; story points; story maps; defining user stories; user stories |
| &nbsp;&nbsp;&nbsp;&nbsp;- user story examples and templates |  | 63 | 94,210 | 11,650 | 1,600 | 13 | 0.60 | 0.03 | 1.00 | 25 / 11 | format for user stories; template for user stories; templates for user stories; user stories format; user stories template |
| &nbsp;&nbsp;&nbsp;&nbsp;- user stories (general) |  | 88 | 89,690 | 45,430 | 590 | 22.5 | 0.09 | 0.17 | 0.00 | 35 / 17 | epic user web; story points; story maps; defining user stories; user stories |
| &nbsp;&nbsp;&nbsp;&nbsp;- acceptance criteria |  | 26 | 19,590 | 4,330 | 390 | 9.5 | 0.27 | 0.04 | 0.35 | 11 / 9 | acceptance criteria for user stories examples; examples of user stories with acceptance criteria; sample acceptance criteria for user stories; sample user stories with acceptance criteria; user stories acceptance criteria examples |
| **web design** | design | 26 | 151,890 | 151,890 | 1,600 | 35.5 | 0.58 | 0.04 | 0.50 | 39 / 10 | website design; web designer; web design company; web design agency; responsive design |
| **personas and journey maps** | design | 90 | 136,410 | 44,310 | 800 | 23 | 0.22 | 0.09 | 0.36 | 225 / 30 | customer journey; consumer journey map; customer experience journey map; customer journey map; customers journey map |
| &nbsp;&nbsp;&nbsp;&nbsp;- journey maps and user flows |  | 61 | 109,710 | 31,130 | 880 | 19 | 0.23 | 0.08 | 0.41 | 231 / 30 | customer journey; consumer journey map; customer experience journey map; customer journey map; customers journey map |
| &nbsp;&nbsp;&nbsp;&nbsp;- personas |  | 29 | 26,700 | 13,180 | 480 | 25 | 0.21 | 0.10 | 0.24 | 25 / 8 | define user persona; user persona definition; persona user; persona user experience; user experience persona |
| **a/b testing and experimentation** | business | 113 | 135,980 | 32,160 | 210 | 38 | 0.14 | 0.09 | 0.10 | 64 / 18 | a & b testing; a / b testing; a b split testing; a b testing; a to b testing |
| &nbsp;&nbsp;&nbsp;&nbsp;- a/b testing (general) |  | 40 | 121,020 | 29,570 | 720 | 48 | 0.20 | 0.15 | 0.28 | 76 / 20 | a & b testing; a / b testing; a b split testing; a b testing; a to b testing |
| &nbsp;&nbsp;&nbsp;&nbsp;- a/b testing tools and platforms |  | 39 | 9,900 | 3,650 | 210 | 23 | 0.21 | 0.08 | 0.00 | 63 / 18 | what is a/b testing software; a / b testing tools; a b split testing tools; a b testing in mailchimp; a b testing mailchimp |
| &nbsp;&nbsp;&nbsp;&nbsp;- a/b testing in marketing (email, landing pages, ads) |  | 34 | 5,060 | 840 | 170 | 38 | 0.00 | 0.03 | 0.00 | 66 / 18 | a b testing for landing pages; a b testing for marketing; a b testing for seo; a b testing in marketing; a b testing in seo |
| **design systems and ui components** | design | 96 | 130,280 | 115,000 | 390 | 6.5 | 0.02 | 0.01 | 0.02 | 3 / 3 | component-based software engineering; shadcn ui; design patterns; plant design management system; banner design |
| &nbsp;&nbsp;&nbsp;&nbsp;- ui components and patterns |  | 62 | 71,790 | 68,590 | 260 | 1 | 0.02 | 0.00 | 0.00 | 0 / 0 | component-based software engineering; shadcn ui; design patterns; banner design; microservices design patterns |
| &nbsp;&nbsp;&nbsp;&nbsp;- design systems |  | 34 | 58,490 | 46,410 | 720 | 26.5 | 0.03 | 0.03 | 0.06 | 3 / 3 | plant design management system; material design; teal material design; ant design; delete icon material design |
| **requirements and prd** | product | 66 | 117,570 | 78,170 | 720 | 9 | 0.27 | 0.09 | 0.33 | 25 / 11 | product requirements document; software requirement specification meaning; what are product requirements; what is a product requirements document; what is product requirements |
| **go-to-market and product marketing** | business | 42 | 98,380 | 81,600 | 1,300 | 18 | 0.05 | 0.24 | 0.05 | 58 / 15 | 4 ps of marketing; marketing mix; what are the 4 ps of marketing; 4ps of marketing; four ps of marketing |
| **retention, churn and engagement** | business | 120 | 91,010 | 39,340 | 480 | 18 | 0.20 | 0.19 | 0.02 | 86 / 17 | customer retention; rate of retention; retention rate; customer retention strategies; customer loyalty program |
| &nbsp;&nbsp;&nbsp;&nbsp;- retention rate formulas and calculation |  | 49 | 39,890 | 4,870 | 320 | 16 | 0.39 | 0.33 | 0.00 | 45 / 9 | calculate retention rate; calculating retention rate; calculation of retention rate; employee retention rate formula; formula for employee retention rate |
| &nbsp;&nbsp;&nbsp;&nbsp;- retention (general) |  | 52 | 28,400 | 14,900 | 355 | 22 | 0.04 | 0.12 | 0.02 | 53 / 10 | rate of retention; retention rate; what is a retention rate; what is retention rate; what is the retention rate |
| &nbsp;&nbsp;&nbsp;&nbsp;- customer retention and loyalty |  | 19 | 22,720 | 19,570 | 720 | 26 | 0.16 | 0.05 | 0.05 | 147 / 18 | customer retention; customer retention strategies; customer loyalty program; verizon pricing strategy customer churn; customer engagement |
| **product owner and product manager roles** | product | 86 | 81,870 | 46,990 | 390 | 8 | 0.16 | 0.07 | 0.02 | 83 / 19 | product manager; associate product manager; product owner; product owner position; product owner positions |
| &nbsp;&nbsp;&nbsp;&nbsp;- product owner |  | 75 | 48,880 | 16,120 | 390 | 8 | 0.17 | 0.08 | 0.03 | 83 / 19 | product owner; product owner position; product owner positions; product owner vacancies; product owner vacancy |
| &nbsp;&nbsp;&nbsp;&nbsp;- product roles (general) |  | 11 | 32,990 | 32,770 | 390 | 7 | 0.09 | 0.00 | 0.00 | 7 / 5 | product manager; associate product manager; remote product manager; product manager vs owner; technical product manager |
| **stakeholder and change management** | product | 63 | 78,390 | 65,160 | 480 | 17 | 0.05 | 0.08 | 0.03 | 16 / 13 | change management; leadership development program; management styles; leadership development; leadership styles in management |
| &nbsp;&nbsp;&nbsp;&nbsp;- change management and leadership |  | 21 | 59,520 | 59,040 | 1,600 | 14 | 0.14 | 0.00 | 0.10 | 4 / 3 | change management; leadership development program; management styles; leadership development; leadership styles in management |
| &nbsp;&nbsp;&nbsp;&nbsp;- stakeholder management |  | 42 | 18,870 | 6,120 | 320 | 18 | 0.00 | 0.12 | 0.00 | 28 / 15 | stakeholder in management; stakeholder management; what is a stakeholder management; what is stakeholder management; define stakeholder management |
| **product strategy, discovery and launch** | product | 94 | 54,650 | 39,700 | 290 | 8 | 0.06 | 0.03 | 0.13 | 121 / 23 | product development; positioning statement; product differentiation; product market fit; product positioning bases |
| &nbsp;&nbsp;&nbsp;&nbsp;- product strategy |  | 41 | 29,080 | 21,350 | 260 | 4 | 0.15 | 0.07 | 0.29 | 138 / 21 | positioning statement; product differentiation; product market fit; product positioning bases; straddle positioning in marketing |
| &nbsp;&nbsp;&nbsp;&nbsp;- new product development and launch |  | 46 | 23,180 | 16,100 | 320 | 10 | 0.00 | 0.00 | 0.00 | 83 / 20 | product development; product development life cycle; product development process; product launch; market research and product development |
| &nbsp;&nbsp;&nbsp;&nbsp;- product strategy and discovery (general) |  | 7 | 2,390 | 2,250 | 210 | 5 | 0.00 | 0.00 | 0.00 | 0 / 0 | mvp minimum viable product; innovation discovery; product discovery; online product discovery platform; product discovery service |
| **product roadmap** | product | 83 | 40,430 | 11,300 | 260 | 10 | 0.31 | 0.11 | 0.34 | 57 / 12 | product roadmap; roadmap for product; roadmap product; example of a product roadmap; example of product roadmap |
| **information architecture** | design | 37 | 26,020 | 5,500 | 260 | 11 | 0.05 | 0.05 | 0.19 | 105 / 16 | information about architecture; information architecture; information architecture ia; information of architecture; information on architecture |

Near misses (under 20 keywords, left in unassigned): market research and competitor analysis (19), ux writing
(10). Jobs to be done formed no group: all 19 of its rows are flagged "jobs" by the Phase 1 flag rule (the
word "jobs"), including "jobs to be done" (2,400), "jobs to be done framework" (1,600) and "jobs to be done
template" (260); about 7,300 searches in all. The flag rule needs an exception for this phrase before Phase 3.

## Article formats: question and template signals

Highest question_share (topic level): question-led articles, FAQ blocks, definitional intros.

1. go-to-market and product marketing 0.24 ("what are the 4 ps of marketing")
2. retention, churn and engagement 0.19 (sub-topic "retention rate formulas and calculation" 0.33: "how to
   calculate retention rate"; a calculator candidate)
3. product roadmap 0.11
4. okrs, kpis and metrics 0.10 (okrs 0.12: "what is an okr", "what does okr stand for")
5. user stories and acceptance criteria 0.10 (user stories general 0.17)

Question shares are low overall (193 of 3,017 keywords start with a question word), so explicit questions are
a minority format; most demand is a phrase plus a modifier.

Highest template_share (topic level): pointers to the Templates section.

1. web design 0.50 ("website examples", "portfolio website examples"; examples rather than templates)
2. user stories and acceptance criteria 0.41 (sub-topic "user story examples and templates" is 63 keywords,
   all template-type by construction: "user story template", "user story examples", "user story format")
3. personas and journey maps 0.36 (journey maps 0.41: "customer journey map template", "journey map example";
   personas 0.24)
4. product roadmap 0.34 ("product roadmap template", "roadmap powerpoint")
5. requirements and prd 0.33 ("product requirements document template", "prd product requirements document")

These five are the strongest case for downloadable templates paired with an article: user story, journey map,
persona, product roadmap and PRD templates. Acceptance criteria (0.35) and a/b testing general (0.28,
"a b testing sample size calculator") add a checklist and a calculator.

## What the three-domain hypothesis did not predict

- **Surveys and questionnaires** remain the biggest research sub-topic by volume (61 keywords, 184K; 146K
  adjusted), ahead of usability testing (81 keywords but 51K). "close-ended questions", "open ended survey
  examples". Low difficulty (median KD 8).
- **Company pricing case studies**: 51 keywords like "nike pricing strategy", "walmart pricing strategy",
  "airline pricing strategy", median KD 0. Small volumes each, but a ready-made case-study series.
- **Retention leans to HR**: "employee retention rate" and "how to calculate retention rate" outnumber
  customer retention; the calculation sub-topic (49 keywords) is a calculator plus explainer.
- **OKRs** formed a 119-keyword sub-topic on their own (Phase 1 found only 35 "okr" rows), larger than KPIs.
- **Product owner** is mostly a role and certification query set: 74 of its 150 rows were flagged jobs or
  certification; the 75 kept are role definitions and "product owner vs product manager".
- **Change management and leadership** (21 keywords, 60K) again outweighs stakeholder management (42 keywords
  but 19K).
- **UI components** (62 keywords, median KD 1) persist from Phase 1: "search bar ui", "badge ui", "material ui".
- **Analytics** (93) is still mostly data analytics as a field; product analytics as such stayed under 15.

## Seeds that still produced noise

Noise rules in `cluster_v2.py` send 264 keywords to unassigned with a reason:

| Seed | Noise | Example |
|---|---|---|
| journey map | 78 of 145 unflagged: Bible and literature journeys | "paul's missionary journey map", "frodo journey map", "lewis and clark journey map" |
| design system | 96 of 137: building systems (57) and software system design (39) | "sprinkler system design", "irrigation system design", "system design interview" |
| accessibility | 53 of 149: physical and device accessibility | "student accessibility services", "beach accessibility", "outlook accessibility" |
| prioritization | 19 of 118: nursing | "nclex prioritization questions", "prioritization nursing" |
| product management | 12 PLM software, plus 43 rows flagged jobs | "siemens product lifecycle management" |
| product strategy | 17 unassigned | "jane street strategy and product" (a trading firm's internship) |
| a/b testing | 10 unassigned | "testing for influenza a and b", "a b o testing" (blood type) |

Other seeds were clean or nearly so; phrase match fixed the Phase 1 problem for most of the list.

## Largest unassigned word groups

The 15 largest word groups in the unassigned bucket (keywords, combined volume), noise included:

1. design (111, 272,510): system design, cadence design systems, instructional system design
2. system (109, 245,910): the same building and software systems
3. journey (87, 178,740): Bible and literature journeys
4. map (87, 178,740): same
5. system design (64, 153,190): software and building system design
6. accessibility (54, 630,200): student services, beaches, devices, transport
7. product (45, 62,830): PLM software, "product and strategy", product information management
8. journey map (36, 66,950): Paul, Odysseus, Lewis and Clark
9. paul (29, 28,850): Paul's missionary journeys
10. paul s (26, 27,680): same
11. management (23, 52,480): PLM and product information management software
12. prioritization (20, 8,860): nursing and NCLEX
13. missionary (18, 19,090): Bible journeys
14. missionary journey (18, 19,090): same
15. research (17, 52,190): market research (the near-miss topic: "market research analyst", "online market
    research platform")
