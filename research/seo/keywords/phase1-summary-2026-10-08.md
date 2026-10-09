# Phase 1 summary: keyword harvest for Articles (8 Oct 2026)

Source: DataForSEO Labs keyword ideas (live), US (2840), English, one task per seed, limit 250,
volume >= 100, ordered by volume descending. Files:

- Seeds: `keywords/seeds-articles-2026-10-08.csv` (42 seeds: 13 design, 13 product, 9 business, 7 off-map)
- Harvest: `keywords/harvest-articles-2026-10-08.csv` (one row per distinct keyword)
- Topics: `keywords/topic-candidates-2026-10-08.csv`, `keywords/keyword-to-topic-2026-10-08.csv`
- Raw responses: `cache/raw/261008-063.json` to `cache/raw/261008-104.json` (index rows 261008-063 to -104)
- Scripts: `tools/dataforseo_client.py`, `tools/harvest.py`, `tools/cluster_phase1.py`

## Spend

| Item | Cost |
|---|---|
| Probe (seed "ux research", 250 rows) | $0.0420 (= $0.012 + 250 x $0.00012, as priced) |
| Remaining 41 seeds | $1.6956 |
| Total | $1.7376 (cap $2.00) |
| Balance after | $21.94 |

## Rows per seed

40 of 42 seeds hit the 250-row cap. Exceptions: "retention rate" 245 rows; "okr" 35 rows (the only
seed under 50).

## Keywords

- Distinct keywords: 7,706 (all have volume >= 100).
- Flagged: brand 155, jobs 417, course 61 (633 in all); 7,073 unflagged.
- Clustered: 7,073 unflagged keywords; 1,785 assigned to 26 topics, 5,288 unassigned.

**Main caveat: the harvest is mostly off-topic.** Keyword ideas works by category, and ordering by
volume descending pulls the biggest terms in the whole category to the top of each 250-row page, not the
closest ones. "ai product management" returned consumer AI apps ("character ai", "ai humanizer"),
"go to market strategy" returned stock-market queries, "usability testing" returned medical testing,
"user stories" returned Instagram stories, "web accessibility" returned "thingiverse website". A rough
relevance pass found about 870 keywords that sit in the site's subject area. For Phase 3 and any re-run,
use keyword suggestions (phrase match) or related keywords, or keyword ideas without the volume-desc
order, so the 250 rows are the closest terms rather than the largest.

## Candidate topics (20 or more keywords), sorted by total volume

Topics marked "mostly noise" are rule groups that collect the off-topic catch; they are kept so the
assignment is complete, not as proposals. Decision share counts how, vs, best, examples, template,
framework, tools, guide and similar. Competitor articles is an approximation: content URLs across the
Phase 0 sitemaps whose slug contains at least two of the topic's five most distinctive tokens; noisy
token sets (for example "design systems and ui components", whose tokens are component names) give
near-zero or inflated counts.

| Topic | Domain | Keywords | Total volume | Median vol | Median KD | Decision share | Competitor articles / domains | Top keywords |
|---|---|---|---|---|---|---|---|---|
| ai tools (mostly noise) | other | 263 | 27,402,660 | 27,100 | 38 | 0.08 | 140 / 22 | ai; character ai; ai mode; mode ai; humanize ai; ai humanizer; ai image generator; poly ai |
| design (general) (mostly noise) | design | 204 | 2,486,130 | 5,400 | 14 | 0.01 | 3 / 3 | cricut design space; design; design within reach; e design; interior design; mehndi design; peak design |
| marketing (general) (mostly noise) | other | 182 | 1,586,020 | 2,900 | 21 | 0.04 | 54 / 20 | staples print and marketing services; affiliate marketing; digital marketing; social media marketing; marketing; marketing agency; vector marketing; cardenas marketing network |
| graphic and visual design (mostly noise) | other | 31 | 407,520 | 6,600 | 31 | 0.06 | 5 / 2 | graphic design; graphic designer; t shirt design; graphic design is my passion; tshirt design; business card design; character design; what is graphic design |
| analytics | business | 82 | 381,810 | 1,900 | 17 | 0.07 | 115 / 19 | analytics; data analyst; data analytics; business analytics; free web analytics service; data analyst internship; analytics definition; business intelligence analyst |
| project management | product | 68 | 348,590 | 1,600 | 17.5 | 0.19 | 28 / 11 | project management; project manager; project management tools; project management tool; program manager; project mapping; construction project manager; project board |
| seo and keyword research (mostly noise) | other | 107 | 338,300 | 480 | 66 | 0.70 | 25 / 14 | seo tools; keyword research; seo company; semrush seo tools; seo keyword research; website seo; keyword research tools; local seo company |
| ux and ui design (discipline) | design | 103 | 291,430 | 320 | 6 | 0.02 | 18 / 6 | ui ux design; one ui themes; one ui; ux design; ui/ux designer; ux designer; product design; product designer |
| growth marketing and funnels | business | 33 | 288,610 | 2,400 | 31 | 0.06 | 225 / 30 | content marketing; marketing strategy; marketing funnel; content marketing services; growth and development; content marketing strategy; digital marketing strategies; sales funnel |
| customer service (mostly noise) | other | 62 | 255,240 | 1,300 | 12 | 0.02 | 23 / 17 | target customer service; empower customer service; boost customer service; ppl customer service; linkedin customer service; cloud field service software; customer service representative remote; customer service skills |
| system and software design (mostly noise) | other | 74 | 240,530 | 720 | 15 | 0.04 | 30 / 12 | software architecture; native app development; software development; app development; software development company; system design; system design interview; domain driven design |
| surveys and questionnaires | design | 56 | 181,200 | 1,000 | 5 | 0.16 | 62 / 13 | close-ended questions in research; closed-ended questions in research; online survey platforms; web soil survey; online surveys; customer feedback survey; via character strengths survey; customer satisfaction survey |
| agile, scrum and kanban | product | 56 | 171,680 | 880 | 26 | 0.27 | 55 / 19 | agile; scrum master; agile project management; scaled agile framework; agile manifesto; agile scrum; waterfall methodology; agile development |
| web design and accessibility | design | 30 | 155,450 | 1,450 | 36.5 | 0.57 | 78 / 15 | website design; web designer; web design company; web design agency; responsive design; web design services; portfolio website examples; website examples |
| pricing strategy | business | 35 | 119,600 | 1,900 | 11 | 0.03 | 10 / 9 | originality pricing; dynamic pricing; pricing strategies; questions about pricing; what is retail pricing; with pricing; oil price market; datadog pricing |
| design systems and ui components | design | 71 | 119,470 | 320 | 2 | 0.01 | 0 / 0 | component-based software engineering; cadence design systems; shadcn ui; design patterns; banner design; material design; teal material design; ant design |
| okrs, kpis and metrics | business | 33 | 118,400 | 880 | 22 | 0.06 | 2 / 2 | metrics; kpi examples; dora metrics; synonym metrics; thesaurus metrics; kpi meaning in business; kpi metrics; snf metrics |
| ux research, personas and journeys | design | 31 | 113,260 | 1,000 | 13 | 0.16 | 230 / 27 | user interviews; user testing; customer journey; customer experience; qualitative data examples; action research; user testing questions; ux research |
| product management, strategy and roadmaps | product | 58 | 109,880 | 880 | 9 | 0.05 | 98 / 21 | product manager; product life cycle; product management; product development; product roadmap; product science; associate product manager; positioning statement |
| go-to-market and product marketing | business | 40 | 94,890 | 1,300 | 20.5 | 0.05 | 6 / 4 | 4 ps of marketing; marketing mix; what are the 4 ps of marketing; 4ps of marketing; four ps of marketing; product marketing; customer segmentation; market segmentation meaning |
| prioritization | product | 21 | 71,560 | 1,300 | 4 | 0.19 | 34 / 8 | another word for prioritization; use high priority notification meaning; prioritization synonyms; high priority; prioritization matrix; prioritization meaning; priority matrix; task prioritization |
| stakeholder and change management | product | 20 | 59,380 | 1,750 | 14.5 | 0.15 | 9 / 7 | change management; leadership development program; management styles; leadership development; leadership styles in management; leadership vs management; prosci change management; change management process |
| user stories and acceptance criteria | product | 36 | 59,040 | 655 | 18 | 0.19 | 10 / 8 | epic user web; story points; story maps; user stories; user story format; sample acceptance criteria for user stories; user stories examples; user stories in agile examples |
| market research and competitor analysis | business | 20 | 56,780 | 2,900 | 23 | 0.00 | 81 / 23 | market research analyst; online market research platform; online market research platforms; market research for starting a business; market research and marketing; market research and marketing research; market research for marketing; market research in marketing |
| requirements and prd | product | 39 | 51,350 | 590 | 6 | 0.26 | 4 / 3 | software requirement specification meaning; draft requirements; system requirements; design brief; design spec; requirements document; non functional requirements; application requirements |
| retention, churn and engagement | business | 30 | 23,310 | 490 | 18 | 0.10 | 125 / 17 | customer retention; customer retention strategies; customer loyalty program; customer engagement; what is customer retention; customer retention meaning; engagement rate; customer retention loyalty programs |

Near misses (under 20 keywords, left in unassigned): a/b testing and experimentation (16), design
thinking and principles (18). Jobs to be done and service design returned no keyword containing their own phrase at
volume >= 100 (unflagged), so neither formed a group.

## Largest unassigned word groups

Most of the unassigned pile is category noise. The 15 largest groups (keywords, combined volume):

1. examples (374, 1.18M): "personal statement examples", "narrative examples"; a modifier, not a topic
2. management (338, 1.28M): property, construction, inventory, asset management
3. meaning (263, 1.26M): definitional "X meaning" queries across many words
4. testing (222, 2.13M): medical and lab testing (STD, TB, allergy, Prometric)
5. website (215, 2.96M): website builders, "thingiverse website"
6. market (205, 1.86M): stock market, futures, "reading terminal market"
7. number (199, 1.01M): customer service phone numbers
8. sales (192, 1.44M): sales jobs and sales associate (unflagged variants), net sales
9. tech (176, 1.40M): information technology, tech companies
10. product (153, 1.47M): product recalls, product liability, product registration
11. software (142, 0.63M): CRM, ERP, generic business software
12. metric (139, 0.40M): the metric system and unit conversions
13. business (139, 0.57M): business plan, small business
14. tools (120, 0.33M): mostly SEO and generic online tools
15. story (113, 2.19M): short story, story elements, Instagram stories

Worth a second look inside the noise: "requirements" (107; mostly legal and eligibility requirements,
but a few product ones), "priority" (58; priority mail and synonyms, a few prioritization ones),
"research" (56), "performance" (55; performance reviews and metrics), "case" (49; case study).

## What the three-domain hypothesis did not predict

- **Surveys and questionnaires** (56 keywords, 181K) emerged as its own design topic, separate from UX
  research: "close-ended questions in research", "open ended survey examples", "survey introduction".
  Low difficulty (median KD 5), high volume, and closer to research methods than to UX as such.
- **Analytics** (82, 382K) is larger than any product topic, though it leans toward data analytics as a
  field (degrees, platforms) rather than product analytics.
- **UI components** ("pagination ui", "stepper ui", "badge ui", "search bar ux", "material ui"): 71
  keywords with median KD 2, mostly developer-leaning; a possible design-system pattern library angle.
- **Requirements** (39) and **user stories and acceptance criteria** (36) are each bigger than
  "product roadmap", which on its own reached only a handful of keywords at volume 100+.
- **Stakeholder and change management** (20) came through via leadership and Kotter-style change
  queries, not stakeholder mapping.
- **Off-map seeds:** "ai product management" produced only consumer AI tools (no PM angle at volume
  100+); "design thinking" and "service design" collapsed into general design noise; "growth marketing"
  produced a usable growth and funnels topic plus general marketing; "product operations" and "jobs to be
  done" produced almost nothing on-topic. SEO and keyword research (107 keywords, from "user research
  methods") is a real cluster but outside the site's remit.

## Trend observations

Monthly data covers September 2025 to August 2026.

1. **Broad decline.** 3,572 of 7,706 keywords (46%) peak in September 2025, the first month of the
   window, and every on-topic topic has a median slope below 1 (last three months against first three):
   from 0.95 for surveys and 0.93 for UI components down to 0.56 for retention and 0.35 for
   go-to-market. Consistent with answers moving into AI Overviews; worth checking against the Google Ads
   volumes in Phase 4 before treating it as real.
2. **A shared spike in May 2026.** "project management" (135K), "content marketing", "marketing
   strategy" and "ui ux design" all jump to 450K-550K in May 2026 and settle at 135K-200K. The same shape
   across unrelated terms looks like a data artifact or a one-off event, and it makes the seasonal flag
   unreliable: 627 of the 874 on-topic keywords show as "seasonal" (max over twice the min).
3. **Rising on-topic terms** (volume 1,000+): "marketing strategy" (slope 7.4), "scrum project
   management" (5.6), "ui ux design" (5.3), "requirements document" (4.4), "project management" (3.6),
   "website user testing" (3.4). Several of these ride the May spike, so the slope overstates them.
   Falling: "customer journey" (0.04), "responsive design" (0.02), "customer feedback survey" (0.02).
