# Phase 3 summary: section demand and section category trees (8 Oct 2026)

Plan: `research/seo/analysis-plan-2026-10-08.md` (Phase 3). DataForSEO Labs keyword suggestions (live, phrase
match), US (2840), English, one task per seed, limit 150, volume >= 100, ordered by volume descending.

## Spend

| Item | Cost |
|---|---|
| Probe (seed "ux tools", 23 rows) | $0.0148 |
| Remaining 16 seeds | $0.2408 |
| Total | $0.2556 (expected under $0.45) |
| Balance after (free user_data call) | $20.72 |

No 50000 errors. Raw responses `cache/raw/261008-142.json` to `261008-158.json`; one index row per seed (note
"phase3 <section>; N rows; $cost").

## Rows per seed

Seeds: `keywords/seeds-sections-2026-10-08.csv` (seed,section).

| Seed | Section | Rows | Cost |
|---|---|---|---|
| ux tools | links | 23 | $0.0148 |
| ux research tools | links | 2 | $0.0122 |
| product management tools | links | 9 | $0.0131 |
| product analytics tools | links | 1 | $0.0121 |
| roadmap tools | links | 5 | $0.0126 |
| design resources | links | 16 | $0.0139 |
| prototyping tools | links | 18 | $0.0142 |
| ux books | books | 20 | $0.0144 |
| product management books | books | 14 | $0.0137 |
| design books | books | 150 | $0.0300 |
| prd template | templates | 3 | $0.0124 |
| user persona template | templates | 1 | $0.0121 |
| product roadmap template | templates | 14 | $0.0137 |
| user story template | templates | 30 | $0.0156 |
| ab test calculator | tools | 3 | $0.0124 |
| rice score | tools | 45 | $0.0174 |
| sample size calculator | tools | 76 | $0.0211 |

Only "design books" hit the 150-row cap, and most of its rows are other design fields. Phrase match is narrow:
"product analytics tools", "user persona template" (1 row each), "ux research tools" (2), "prd template",
"ab test calculator" (3) barely exist as longer US phrases at volume 100 or more.

## Harvest and the flag fix

- `keywords/harvest-sections-2026-10-08.csv`: 423 distinct keywords, the harvest-articles-1b columns plus
  `section` (the `domains` column is empty for section seeds). Flags: brand 10 (Figma, Jira, Confluence,
  Optimizely), jobs 0, course 0; 413 unflagged.
- Flag function (`tools/harvest.py`, `flag_for`): the phrase "jobs to be done" (also "job to be done" and the
  hyphenated forms) is now removed before the jobs test, so a JTBD keyword is never flagged as jobs, while
  "jobs to be done salary" still would be. Re-run in place over `keywords/harvest-articles-combined-2026-10-08.csv`
  (new `harvest.py reflag --file ...`, no API calls): **19 rows changed** from jobs to unflagged (jobs to be done,
  jobs to be done framework, template(s), example(s), theory, book(s), "what is jobs to be done" and variants).
  The v2 topic files were not re-clustered; with these 19 rows the jobs to be done rule group (under 20 keywords
  in v2) would likely qualify as a topic on the next cluster run.
- `harvest.py` also gained `--tag sections` (seeds file with seed,section; note "phase3 <section>"; output adds
  the section column).

## Section candidates

File: `keywords/section-candidates-2026-10-08.csv`; script `tools/cluster_sections.py` (the cluster_v2 method:
ordered pattern rules per section, first match wins). A first-level category needs 10 or more unflagged keywords
with volume >= 100; a second-level one ("parent > child") 5 or more. Categories marked "(off-scope)" are other
meanings of the seed phrase. "(below threshold)" rows sum the smaller groups and name them. Adjusted volume counts
each distinct volume plus 12-month series once. Template share ignores "sample size" (the word "sample" there is
not a template signal).

| Section | Category | Keywords | Total volume | Adjusted volume | Median KD | Template share | Question share | Top keywords |
|---|---|---|---|---|---|---|---|---|
| links | ux and ui design tools | 19 | 13,620 | 2,910 | 19 | 0.00 | 0.00 | ux and ui design tools; ux design tools; ux designing tools; tools for ui ux design; tools for ui/ux design |
| links | product management tools | 10 | 4,690 | 2,400 | 8 | 0.00 | 0.00 | product management tools; tools for product management; tools product management; ai tools for product management; product analytics tools |
| links | prototyping tools | 17 | 4,200 | 1,160 | 26 | 0.00 | 0.00 | prototyping software tools; prototyping tools; software prototyping tools; tools for prototyping; tools of prototyping |
| links | (below threshold) | 22 | 7,350 | 5,540 | 19 | 0.00 | 0.00 | design resources (off-scope): 7 kw;  product management software (off-scope): 2 kw;  ux research and testing tools: 4 kw;  design resources: 9 kw |
| books | design books (general) | 16 | 22,130 | 4,090 | 0 | 0.00 | 0.00 | books about design; books design; books for design; books on design; design for books |
| books | graphic and visual design books | 26 | 21,060 | 1,690 | 0 | 0.00 | 0.00 | books about graphic design; books for graphic design; books graphic design; books on graphic design; books on graphics design |
| books | product management books | 14 | 6,460 | 980 | 0 | 0.00 | 0.00 | books about product management; books for product management; books on product management; books product management; product management books |
| books | ux design books | 21 | 5,190 | 530 | 0 | 0.00 | 0.00 | books about ux; books about ux design; books for ux; books for ux design; books on ux |
| books | book cover and layout design (off-scope) | 21 | 78,140 | 15,360 | 24 | 0.05 | 0.00 | book cover design books; books cover design; books design cover; cover design books; cover design for books |
| books | engineering and software design books (off-scope) | 16 | 13,210 | 7,490 | 1 | 0.00 | 0.00 | mechanical engineering design books; domain driven design books; domain-driven design books; system design books; systems design books |
| books | interior, home and architecture design books (off-scope) | 31 | 32,320 | 7,060 | 0 | 0.00 | 0.00 | books about interior design; books for interior design; books in interior design; books interior design; books on interior design |
| books | fashion and craft design books (off-scope) | 22 | 16,880 | 5,440 | 0 | 0.00 | 0.00 | fashion design pattern making books; patternmaking for fashion design books; apparel design books; books about clothing design; books about fashion design |
| books | (below threshold) | 13 | 4,790 | 1,100 | 0 | 0.00 | 0.00 | game and character design books: 9 kw;  design thinking books: 4 kw |
| templates | user story templates | 26 | 34,760 | 11,150 | 13 | 1.00 | 0.00 | template for user story; template user story; user story template; user story template example; acceptance criteria user story template |
| templates | user story templates > agile and scrum user story templates | 12 | 15,380 | 3,180 | 13 | 1.00 | 0.00 | agile development user story template; agile user story template; agile user story template example; user story agile template; user story template agile |
| templates | user story templates > user story template formats (word, doc, card) | 5 | 2,610 | 1,500 | 11 | 1.00 | 0.00 | user story template word; user story word template; user story card template; user story template doc; user story template document |
| templates | product roadmap templates | 14 | 6,170 | 1,250 | 7.5 | 1.00 | 0.00 | product roadmap template; roadmap product template; sample product roadmap template; template for product roadmap; template product roadmap |
| templates | product roadmap templates > roadmap templates for powerpoint | 6 | 840 | 140 | 0 | 1.00 | 0.00 | powerpoint product roadmap template; powerpoint template product roadmap; product roadmap powerpoint template; product roadmap ppt template; product roadmap template powerpoint |
| templates | (below threshold) | 4 | 10,300 | 4,500 | 6 | 1.00 | 0.00 | prd templates: 3 kw;  persona templates: 1 kw |
| tools | sample size calculators | 68 | 126,010 | 14,990 | 37.5 | 0.01 | 0.00 | calculate sample size calculator; calculating sample size calculator; calculator for sample size; calculator sample size; determine sample size calculator |
| tools | sample size calculators > power analysis sample size calculators | 24 | 19,530 | 2,390 | 18 | 0.00 | 0.00 | power sample size calculator online; calculator sample size power; power analysis and sample size calculator; power analysis calculator sample size; power analysis for sample size calculator |
| tools | sample size calculators > survey sample size calculators | 13 | 5,920 | 2,140 | 25 | 0.00 | 0.00 | surveymonkey sample size calculator; raosoft sample size calculator; sample size calculator by raosoft; sample size calculator by raosoft inc; sample size calculator raosoft |
| tools | sample size calculators > statistical significance sample size calculators | 14 | 4,550 | 650 | 43 | 0.00 | 0.00 | determining sample size statistics calculator; sample size statistics calculator; statistical calculator for sample size; statistical calculator sample size; statistical sample size calculator |
| tools | rice purity test (off-scope) | 23 | 79,730 | 74,330 | 3 | 0.00 | 0.30 | rice purity score; rice purity test score meaning; rice purity test score meanings; rice purity test score; average rice purity score |
| tools | rice university and sports scores (off-scope) | 21 | 15,510 | 4,780 | 0 | 0.00 | 0.00 | rice football score; rice owls football score; rice score football; rice u football score; rice university football score |
| tools | (below threshold) | 9 | 3,700 | 2,520 | 43 | 0.00 | 0.00 | a/b test calculators: 8 kw;  prioritization scores (rice): 1 kw |

Median KD 0 on the book rows means no difficulty data, not an easy keyword.

## Tools: product meanings versus other meanings

By inspection of the 121 tools keywords in `keywords/harvest-sections-2026-10-08.csv`:

| Meaning | Keywords | Adjusted volume | Product-related |
|---|---|---|---|
| Sample size calculators (general, power analysis, survey, statistical significance) | 68 | 14,990 | yes |
| A/B test calculators (significance, split test, A/B sample size) | 8 | 620 | yes |
| "rice score" (bare phrase, KD 4) | 1 | 1,900 | ambiguous; needs a SERP check |
| Rice purity test (score meanings, averages, by age) | 23 | 74,330 | no |
| Rice University football, basketball, baseball scores; Brother Rice high school football | 11 | 2,950 | no |
| Rice University SAT and ACT scores | 7 | 1,340 | no |
| Jerry Rice score card | 3 | 490 | no |

Navigational tool names inside the product group: SurveyMonkey, Raosoft, Qualtrics and G*Power sample size
calculators (not flagged; Optimizely is flagged as a brand). No cooking, medical ICE or mortgage meanings surfaced:
"ice score" and mortgage-style calculators were not among the seeds.

## Stock evidence

File: `competitors/stock-by-section-2026-10-08.csv` (463 rows; script `tools/stock_sections.py`): GitHub awesome
list headings with entry counts; first-path-segment counts for bookmarks.design, uxtools.co, toools.design,
designresourc.es, startupstash.com (Links), fivebooks.com, mostrecommendedbooks.com, lennysnewsletter.com (Books),
and template URLs on aha.io, productboard.com, maze.co, dovetail.com, nngroup.com, mural.co (Templates); plus
category page names (no counts in sitemaps) and topic-word counts in list and template URLs.

## Section trees

Draft: `research/seo/section-trees-v1.md` (tree, demand, stock, page-one holders, build order and open questions
per section, every number tagged with its source file).

## The three most useful findings

1. **Templates carry the most section demand, and it is soft.** User story templates: adjusted 11,150, KD 13, with
   agile and scrum variants (3,180) and Word, doc and card formats (1,500) as children. The Articles harvest adds
   template demand the seeds missed: PRD template 2,900 (KD 6 to 11), VPAT template 5,400 (KD 23), customer
   journey map templates 1,980 (KD 19), OKR templates 1,130 (KD 7.5). Page one is held by B-tier vendors (Notion 9
   of 14 queries, Atlassian, ClickUp, Smartsheet) that host templates inside their products.
2. **One calculator has real demand: sample size.** Adjusted 14,990, KD 37.5, with softer children: power analysis
   2,390 (KD 18) and survey 2,140 (KD 25). A/B test calculators are small (620, KD 43). "rice score" (1,900) sits
   next to the rice purity test (74,330) and Rice University sports, so a RICE calculator needs a SERP check and
   should target prioritization phrasing.
3. **Links and Books demand is small once it is on-brand.** Links: UX and UI design tools 2,910 (KD 19), product
   management tools 2,400 (KD 8), prototyping tools 1,160 (KD 26); the adjacent general terms are larger but
   harder (project management tools 40,050 at KD 36 in the Articles harvest). Books: product management books 980
   and UX books 530 adjusted, while "design books" is dominated by other fields (cover, interior, fashion,
   engineering: about 35,350 adjusted). Both sections' page ones are held by Reddit (13 of 16 Links queries, 11 of
   12 Books queries), Amazon and Goodreads, so they look more like authority and return-visit sections than traffic
   sections.

## Files

- `research/seo/keywords/seeds-sections-2026-10-08.csv`
- `research/seo/keywords/harvest-sections-2026-10-08.csv`
- `research/seo/keywords/section-candidates-2026-10-08.csv`
- `research/seo/keywords/harvest-articles-combined-2026-10-08.csv` (re-flagged in place, 19 rows)
- `research/seo/competitors/stock-by-section-2026-10-08.csv`
- `research/seo/section-trees-v1.md`
- `research/seo/tools/harvest.py` (flag fix, `--tag sections`, `reflag`), `tools/cluster_sections.py`,
  `tools/stock_sections.py`
