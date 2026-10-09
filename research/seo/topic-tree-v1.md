# Topic tree v1: Articles, plus the section trees with scores (8 Oct 2026)

The data-driven topic tree for userandproduct.com after Phase 4 (scoring). Factual draft; the owner decides, and
the one hand-set column (owner_fit, 1 to 3) is still empty.

## 1. How to read it and where every number comes from

**Units.** 84 scoring units: the 25 topics and 45 sub-topics of
`research/seo/keywords/topic-candidates-v2-2026-10-08.csv` (a split topic appears as its own "topic total" unit
and as its sub-topics), plus 14 section categories from `research/seo/keywords/section-candidates-2026-10-08.csv`
with 10 or more keywords. Six off-scope section categories were dropped: book cover and layout design,
engineering and software design books, interior and architecture design books, fashion and craft design books,
the rice purity test, and Rice University sports and test scores. Bible and literature journeys, irrigation and
building systems, device and physical accessibility and nursing (NCLEX) prioritization were already removed by
the Phase 1b noise rules, so no topic unit had to be dropped. Unit list with head terms:
`research/seo/keywords/phase4-units-2026-10-08.csv`.

**Head terms.** Up to two per unit, hand-picked from the highest-volume unflagged keywords that read as the topic
itself (not a brand, a job or a word-order variant of the other head term). Twelve head terms reuse Phase 0
SERPs. Judgment calls are noted inline ("Note:").

**Per-unit figures** (all in `research/seo/keywords/topic-scores-2026-10-08.csv`):

| Figure | Source |
|---|---|
| keywords, adjusted demand | Phase 1b and Phase 3 harvests; adjusted = each distinct volume plus 12-month series counted once (word-order variants share one Google figure) |
| Google Ads check | `keywords/ads-volumes-2026-10-08.csv`: Google Ads search volume (US, standard queue) for head term 1, with the Labs figure beside it |
| KD | median keyword difficulty (0 to 100) of the unit's keywords; book units have no KD data |
| decision, template, question | share of the unit's keywords with a decision word (how, vs, best, examples, template, framework, tools, guide and similar), a template word (template, example, checklist, format, sample) or a leading question word |
| 12-month slope | median over the unit's keywords of (Jun-Aug 2026) / (Sep-Nov 2025) from the Labs series |
| Trends 5-year | `keywords/trends-2026-10-08.csv`: Google Trends web search, US, Oct 2021 to Oct 2026, head term 1; last-year average over first-year average; rising >= 1.2, falling <= 0.8, flat between; "too small" when both yearly averages are under 1 |
| AI Overview, weak page one | `serps/features-2026-10-08.csv` for head term 1; weak = Medium, Reddit, Quora, LinkedIn, YouTube, Pinterest, Scribd, UX Collective and similar, or a SaaS glossary or blog page; weak page one = 3 or more weak results |
| arena | `keywords/topic-arena-2026-10-08.csv`: distinct page-one domains for the unit's head terms (head 2 only where a SERP exists), minus forums, platforms, video, retailers, catalogs, encyclopedias, dictionaries, government and university sites and app stores. Types come from `competitors/*-competitors.csv`; new domains are typed by `tools/phase4_score.py` (anything commercial or editorial that is not on the exclusion list counts as "business"). Tier and monthly organic traffic from `competitors/traffic-2026-10-08.csv` where the domain was sized in Phase 2 |
| competitor articles | the Phase 1b sitemap approximation (content URLs of 62 seed competitors whose slug holds two of the unit's five most distinctive words), with the number of domains |
| score | see below |

**Score (0 to 100).** Built from ranked percentiles over all 84 units (rank minus one over n minus one, ties
share the average rank):

| Component | Weight | Rule |
|---|---|---|
| Demand | 25 | percentile of adjusted demand |
| Difficulty | 20 | percentile of median KD, inverted (book units, no KD: 0.5) |
| Decision and template | 15 | percentile of decision share plus template share |
| Weak page one | 10 | percentile of the weak-result count on head term 1's page one |
| AI Overview | 10 | 1 if head term 1 has no AI Overview or an empty one, else 0 |
| Trend | 10 | 1 rising, 0.5 flat or too small, 0 falling |
| Competitors in the arena | 10 | percentile of the arena count, inverted |

owner_fit is not in the score. Suggested use once filled: drop units at 1, read the rest by score.

**Reading the Trends figures.** Trends values are relative inside one task of up to five terms. The task grouping
is in `keywords/trends-groups-2026-10-08.csv` (14 groups in unit order, then 4 regroups of the 17 terms that were
too small to read next to a large term, grouped by similar Google Ads volume). Compare a term's own first and last
year, never two terms from different groups.

## 2. The Articles tree

**Do three domains still hold?** Yes, on competitor evidence. The arena domains of the design, product and
business units barely overlap (Jaccard 0.02 design-product, 0.03 design-business, 0.04 business-product), so each
domain is a different set of sites to beat. Demand is close to even (adjusted, leaf units: product 1.48M, design
1.20M, business 1.15M) and so are mean leaf scores (49.8, 49.5, 45.6). The borders are soft in three places:
project management and analytics sit between product and business, and growth marketing is generic marketing.

Topics are ordered by the score of the topic total; sub-topics by their own score.

### Product (10 topics, 23 scoring leaves, adjusted demand 1,476,410, mean leaf score 49.8)

#### product owner and product manager roles

- **Topic total** (u59, score **75.2**): heads "product manager" / "product owner vs product manager"; 86 keywords; adjusted demand 46,990; Google Ads check: 6,600 for head 1 (Labs 22,200); KD 8; decision 0.16, template 0.02, question 0.07; 12-month slope 0.71; Trends 5-year 1.63 (rising); AI Overview yes (empty); weak page one no (2 weak results); competitor articles (sitemap approximation) 83 in 19 domains; arena 4 domains: productplan.com (saas, tier C, 20,541/mo); contentsquare.com (business); productschool.com (education, tier D, 7,453/mo); ironhack.com (business). Note: product manager reads as a role query; job listings are flagged and excluded.
  - **product roles (general)** (u61, score **72.4**): heads "product manager" / "technical product manager"; 11 keywords; adjusted demand 32,770; Google Ads check: 6,600 for head 1 (Labs 22,200); KD 7; decision 0.09, template 0.00, question 0.00; 12-month slope 0.75; Trends 5-year 1.63 (rising); AI Overview yes (empty); weak page one no (2 weak results); competitor articles (sitemap approximation) 7 in 5 domains; arena 4 domains: productplan.com (saas, tier C, 20,541/mo); contentsquare.com (business); productschool.com (education, tier D, 7,453/mo); ironhack.com (business).
  - **product owner** (u60, score **53.4**): heads "product owner" / "product owner vs product manager"; 75 keywords; adjusted demand 16,120; Google Ads check: 2,900 for head 1 (Labs 2,900); KD 8; decision 0.17, template 0.03, question 0.08; 12-month slope 0.71; Trends 5-year 2.38 (rising); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 83 in 19 domains; arena 6 domains: simpliaxis.com (business); scrum.org (education, tier C, 17,058/mo); teravisiontech.com (business); hellopm.co (business); michaelpage.com.hk (business); gainmomentum.ai (business).

#### prioritization

- **Topic total** (u34, score **67.9**): heads "prioritization" / "moscow prioritization"; 108 keywords; adjusted demand 171,110; Google Ads check: 74,000 for head 1 (Labs 74,000); KD 5; decision 0.13, template 0.07, question 0.07; 12-month slope 0.54; Trends 5-year 2.35 (rising); AI Overview yes; weak page one no (2 weak results); competitor articles (sitemap approximation) 41 in 8 domains; arena 9 domains: airfocus.com (saas, tier C, 28,441/mo); pdware.com (business); appfluence.com (business); teamwork.com (business); savio.io (business); wrike.com (business); prince2.com (business); xmind.com (business); craft.io (business).
  - **prioritization (general)** (u35, score **74.6**): heads "prioritization" / "prioritization definition"; 62 keywords; adjusted demand 153,570; Google Ads check: 74,000 for head 1 (Labs 74,000); KD 1; decision 0.11, template 0.06, question 0.10; 12-month slope 0.52; Trends 5-year 2.35 (rising); AI Overview yes; weak page one no (2 weak results); competitor articles (sitemap approximation) 0 in 0 domains; arena 4 domains: airfocus.com (saas, tier C, 28,441/mo); pdware.com (business); appfluence.com (business); teamwork.com (business).
  - **prioritization frameworks** (u36, score **47.6**): heads "moscow prioritization" / "prioritization matrix"; 30 keywords; adjusted demand 14,360; Google Ads check: 4,400 for head 1 (Labs 4,400); KD 21; decision 0.23, template 0.13, question 0.03; 12-month slope 0.57; Trends 5-year n/a (too small); AI Overview yes; weak page one no (2 weak results); competitor articles (sitemap approximation) 29 in 8 domains; arena 5 domains: savio.io (business); wrike.com (business); prince2.com (business); xmind.com (business); craft.io (business).
  - **task and time prioritization** (u37, score **42.6**): heads "task prioritization" / "time management prioritization"; 16 keywords; adjusted demand 3,180; Google Ads check: 1,900 for head 1 (Labs 1,900); KD 10; decision 0.00, template 0.00, question 0.06; 12-month slope 0.32; Trends 5-year 52.00 (rising); AI Overview yes; weak page one no (2 weak results); competitor articles (sitemap approximation) 23 in 11 domains; arena 6 domains: activecollab.com (business); lifelabslearning.com (business); larksuite.com (business); bcit.ca (business); accelo.com (business); fluidwave.com (business).

#### project management

- **Topic total** (u13, score **65.4**): heads "project management" / "project management tools"; 74 keywords; adjusted demand 345,140; Google Ads check: 135,000 for head 1 (Labs 135,000); KD 15; decision 0.22, template 0.03, question 0.01; 12-month slope 0.66; Trends 5-year 1.41 (rising); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 28 in 11 domains; arena 6 domains: pmi.org (business); goskills.com (business); projectmanager.com (business); simpliaxis.com (business); slack.com (business); usnews.com (publication).

#### product roadmap

- **Topic total** (u69, score **57.6**): heads "product roadmap" / "product roadmap examples"; 83 keywords; adjusted demand 11,300; Google Ads check: 3,600 for head 1 (Labs 3,600); KD 10; decision 0.31, template 0.34, question 0.11; 12-month slope 0.28; Trends 5-year 5.11 (rising); AI Overview yes; weak page one yes (3 weak results); competitor articles (sitemap approximation) 57 in 12 domains; arena 7 domains: atlassian.com (saas, tier B, 420,717/mo); productplan.com (saas, tier C, 20,541/mo); agilealliance.org (business); pendo.io (saas, tier C, 12,259/mo); productboard.com (saas, tier D, 6,136/mo); amplitude.com (saas, tier C, 25,299/mo); productschool.com (education, tier D, 7,453/mo).

#### product management (discipline)

- **Topic total** (u21, score **56.9**): heads "product management" / "what is product management"; 94 keywords; adjusted demand 132,410; Google Ads check: 6,600 for head 1 (Labs 6,600); KD 8; decision 0.07, template 0.01, question 0.06; 12-month slope 0.71; Trends 5-year 3.84 (rising); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 21 in 9 domains; arena 9 domains: atlassian.com (saas, tier B, 420,717/mo); ibm.com (business); productboard.com (saas, tier D, 6,136/mo); productplan.com (saas, tier C, 20,541/mo); coursera.org (education, tier A, 1,861,038/mo); tryexponent.com (business); youngurbanproject.com (business); calcalistech.com (business); airfocus.com (saas, tier C, 28,441/mo).
  - **product management (general)** (u22, score **60.6**): heads "product management" / "what is product management"; 74 keywords; adjusted demand 102,690; Google Ads check: 6,600 for head 1 (Labs 6,600); KD 3; decision 0.09, template 0.01, question 0.07; 12-month slope 0.71; Trends 5-year 3.84 (rising); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 0 in 0 domains; arena 9 domains: atlassian.com (saas, tier B, 420,717/mo); ibm.com (business); productboard.com (saas, tier D, 6,136/mo); productplan.com (saas, tier C, 20,541/mo); coursera.org (education, tier A, 1,861,038/mo); tryexponent.com (business); youngurbanproject.com (business); calcalistech.com (business); airfocus.com (saas, tier C, 28,441/mo).
  - **product life cycle** (u23, score **31.7**): heads "product life cycle" / "product life cycle stages"; 20 keywords; adjusted demand 29,720; Google Ads check: 9,900 for head 1 (Labs 9,900); KD 36; decision 0.00, template 0.00, question 0.05; 12-month slope 0.67; Trends 5-year 1.05 (flat); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 12 in 6 domains; arena 6 domains: productleadership.com (business); twproject.com (business); myaccountingcourse.com (business); hellopm.co (business); pwskills.com (business); investopedia.com (publication).

#### requirements and prd

- **Topic total** (u53, score **56.9**): heads "product requirements document" / "product requirements document template"; 66 keywords; adjusted demand 78,170; Google Ads check: 18,100 for head 1 (Labs 18,100); KD 9; decision 0.27, template 0.33, question 0.09; 12-month slope 0.94; Trends 5-year 8.40 (rising); AI Overview yes; weak page one no (0 weak results); competitor articles (sitemap approximation) 25 in 11 domains; arena 12 domains: news.aakashg.com (business); prodpad.com (business); slite.com (business); hustlebadger.com (business); monday.com (business); airfocus.com (saas, tier C, 28,441/mo); anotherwrapper.com (business); notion.com (saas, tier B, 320,481/mo); kolekti.com (business); eonlint.com (business); nuclino.com (business); textcortex.com (business).

#### user stories and acceptance criteria

- **Topic total** (u38, score **56.7**): heads "user stories" / "user stories template"; 177 keywords; adjusted demand 61,410; Google Ads check: 3,600 for head 1 (Labs 3,600); KD 14; decision 0.30, template 0.41, question 0.10; 12-month slope 0.58; Trends 5-year 1.42 (rising); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 12 in 10 domains; arena 13 domains: airfocus.com (saas, tier C, 28,441/mo); agilealliance.org (business); justinmind.com (business); ixdf.org (education, tier C, 32,981/mo); jile.io (business); trailhead.salesforce.com (business); startinfinity.com (business); parabol.co (business); atlassian.com (saas, tier B, 420,717/mo); mountaingoatsoftware.com (expert, tier D, 9,692/mo); rebelscrum.site (business); aha.io (saas, tier C, 28,822/mo); monday.com (business).
  - **acceptance criteria** (u41, score **56.4**): heads "acceptance criteria for user stories examples" / "how to write acceptance criteria for user stories"; 26 keywords; adjusted demand 4,330; Google Ads check: 1,600 for head 1 (Labs 1,600); KD 9.5; decision 0.27, template 0.35, question 0.04; 12-month slope 1.04; Trends 5-year n/a (too small); AI Overview yes; weak page one yes (4 weak results); competitor articles (sitemap approximation) 11 in 9 domains; arena 3 domains: geeksforgeeks.org (education, tier A, 2,532,368/mo); scrum.org (education, tier C, 17,058/mo); salesforceben.com (business).
  - **user story examples and templates** (u39, score **53.9**): heads "user stories template" / "user stories examples"; 63 keywords; adjusted demand 11,650; Google Ads check: 2,900 for head 1 (Labs 2,900); KD 13; decision 0.60, template 1.00, question 0.03; 12-month slope 0.54; Trends 5-year n/a (too small); AI Overview yes; weak page one no (2 weak results); competitor articles (sitemap approximation) 25 in 11 domains; arena 6 domains: atlassian.com (saas, tier B, 420,717/mo); agilealliance.org (business); mountaingoatsoftware.com (expert, tier D, 9,692/mo); rebelscrum.site (business); aha.io (saas, tier C, 28,822/mo); monday.com (business).
  - **user stories (general)** (u40, score **44.7**): heads "user stories" / "story points"; 88 keywords; adjusted demand 45,430; Google Ads check: 3,600 for head 1 (Labs 3,600); KD 22.5; decision 0.09, template 0.00, question 0.17; 12-month slope 0.61; Trends 5-year 1.42 (rising); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 35 in 17 domains; arena 8 domains: airfocus.com (saas, tier C, 28,441/mo); agilealliance.org (business); justinmind.com (business); ixdf.org (education, tier C, 32,981/mo); jile.io (business); trailhead.salesforce.com (business); startinfinity.com (business); parabol.co (business).

#### product strategy, discovery and launch

- **Topic total** (u65, score **48.6**): heads "product development" / "product market fit"; 94 keywords; adjusted demand 39,700; Google Ads check: 4,400 for head 1 (Labs 4,400); KD 8; decision 0.06, template 0.13, question 0.03; 12-month slope 0.41; Trends 5-year 3.17 (rising); AI Overview yes; weak page one no (0 weak results); competitor articles (sitemap approximation) 121 in 23 domains; arena 13 domains: monday.com (business); twi-global.com (business); technia.com (business); lumenalta.com (business); qmarkets.net (business); indepthresearch.org (business); producthq.org (business); moxo.com (business); projectmanager.com (business); browsee.io (business); hypernestlabs.com (business); gapscout.com (business); thryv.com (business).
  - **product strategy** (u66, score **60.3**): heads "product market fit" / "product strategy"; 41 keywords; adjusted demand 21,350; Google Ads check: 2,900 for head 1 (Labs 2,900); KD 4; decision 0.15, template 0.29, question 0.07; 12-month slope 0.56; Trends 5-year 2.60 (rising); AI Overview yes; weak page one no (2 weak results); competitor articles (sitemap approximation) 138 in 21 domains; arena 10 domains: projectmanager.com (business); browsee.io (business); hypernestlabs.com (business); gapscout.com (business); thryv.com (business); atlassian.com (saas, tier B, 420,717/mo); productplan.com (saas, tier C, 20,541/mo); svpg.com (expert, tier D, 6,576/mo); aha.io (saas, tier C, 28,822/mo); romanpichler.com (expert, tier D, 320/mo).
  - **product strategy and discovery (general)** (u68, score **41.0**): heads "mvp minimum viable product" / "product discovery"; 7 keywords; adjusted demand 2,250; Google Ads check: 720 for head 1 (Labs 720); KD 5; decision 0.00, template 0.00, question 0.00; 12-month slope 0.31; Trends 5-year 2.29 (rising); AI Overview yes; weak page one no (2 weak results); competitor articles (sitemap approximation) 0 in 0 domains; arena 11 domains: aalpha.net (business); netsolutions.com (business); blog.logrocket.com (business); codelevate.com (business); ducxinh.com (business); sendpulse.com (business); atlassian.com (saas, tier B, 420,717/mo); productboard.com (saas, tier D, 6,136/mo); productschool.com (education, tier D, 7,453/mo); amplitude.com (saas, tier C, 25,299/mo); pendo.io (saas, tier C, 12,259/mo).
  - **new product development and launch** (u67, score **38.5**): heads "product development" / "product development process"; 46 keywords; adjusted demand 16,100; Google Ads check: 4,400 for head 1 (Labs 4,400); KD 10; decision 0.00, template 0.00, question 0.00; 12-month slope 0.32; Trends 5-year 3.17 (rising); AI Overview yes; weak page one no (0 weak results); competitor articles (sitemap approximation) 83 in 20 domains; arena 8 domains: monday.com (business); twi-global.com (business); technia.com (business); lumenalta.com (business); qmarkets.net (business); indepthresearch.org (business); producthq.org (business); moxo.com (business).

#### agile, scrum and kanban

- **Topic total** (u01, score **48.2**): heads "agile methodology" / "agile project management"; 243 keywords; adjusted demand 370,120; Google Ads check: 135,000 for head 1 (Labs 135,000); KD 36; decision 0.14, template 0.05, question 0.05; 12-month slope 0.66; Trends 5-year 2.39 (rising); AI Overview yes; weak page one no (0 weak results); competitor articles (sitemap approximation) 43 in 16 domains; arena 9 domains: atlassian.com (saas, tier B, 420,717/mo); agilealliance.org (business); geeksforgeeks.org (education, tier A, 2,532,368/mo); instituteprojectmanagement.com (business); asana.com (business); wrike.com (business); comptia.org (business); plane.so (business); ibm.com (business).
  - **agile methodology (general)** (u02, score **48.5**): heads "agile methodology" / "agile"; 96 keywords; adjusted demand 296,030; Google Ads check: 135,000 for head 1 (Labs 135,000); KD 39.5; decision 0.09, template 0.00, question 0.08; 12-month slope 0.60; Trends 5-year 2.39 (rising); AI Overview yes; weak page one no (0 weak results); competitor articles (sitemap approximation) 73 in 20 domains; arena 6 domains: atlassian.com (saas, tier B, 420,717/mo); agilealliance.org (business); geeksforgeeks.org (education, tier A, 2,532,368/mo); instituteprojectmanagement.com (business); asana.com (business); wrike.com (business).
  - **scrum, sprints and backlog** (u05, score **46.5**): heads "agile scrum" / "kanban vs scrum"; 65 keywords; adjusted demand 58,460; Google Ads check: 4,400 for head 1 (Labs 4,400); KD 24; decision 0.20, template 0.20, question 0.06; 12-month slope 0.56; Trends 5-year 0.54 (falling); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 36 in 16 domains; arena 4 domains: agilealliance.org (business); nimblework.com (business); atlassian.com (saas, tier B, 420,717/mo); monday.com (business).
  - **agile project management** (u03, score **45.4**): heads "agile project management" / "lean project management"; 42 keywords; adjusted demand 147,930; Google Ads check: 9,900 for head 1 (Labs 9,900); KD 47; decision 0.02, template 0.00, question 0.00; 12-month slope 1.11; Trends 5-year 0.88 (flat); AI Overview yes; weak page one no (2 weak results); competitor articles (sitemap approximation) 61 in 18 domains; arena 5 domains: agilealliance.org (business); comptia.org (business); plane.so (business); ibm.com (business); atlassian.com (saas, tier B, 420,717/mo).
  - **scaled agile (safe)** (u04, score **31.0**): heads "safe agile framework"; 25 keywords; adjusted demand 12,500; Google Ads check: 8,100 for head 1 (Labs 8,100); KD 45; decision 0.44, template 0.00, question 0.00; 12-month slope 0.66; Trends 5-year 0.31 (falling); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 14 in 8 domains; arena 6 domains: framework.scaledagile.com (business); pmi.org (business); scrum.org (education, tier C, 17,058/mo); monday.com (business); simpliaxis.com (business); cio.com (publication).
  - **agile manifesto and principles** (u06, score **25.0**): heads "agile manifesto" / "agile principles"; 15 keywords; adjusted demand 8,200; Google Ads check: 6,600 for head 1 (Labs 6,600); KD 31; decision 0.00, template 0.00, question 0.00; 12-month slope 0.62; Trends 5-year 0.47 (falling); AI Overview yes; weak page one no (2 weak results); competitor articles (sitemap approximation) 38 in 16 domains; arena 6 domains: agile-academy.com (business); nkdagility.com (business); agilealliance.org (business); niftypm.com (business); project.info (business); kanbanzone.com (business).

#### stakeholder and change management

- **Topic total** (u62, score **47.0**): heads "change management" / "stakeholder management"; 63 keywords; adjusted demand 65,160; Google Ads check: 14,800 for head 1 (Labs 14,800); KD 17; decision 0.05, template 0.03, question 0.08; 12-month slope 0.55; Trends 5-year 3.04 (rising); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 16 in 13 domains; arena 14 domains: online.hbs.edu (education, tier C, 68,686/mo); prosci.com (business); asq.org (business); ibm.com (business); nmsconsulting.com (business); apqc.org (business); mindtools.com (business); runn.io (business); geeksforgeeks.org (education, tier A, 2,532,368/mo); withluna.ai (business); planyway.com (business); greenly.earth (business); unito.io (business); gocardless.com (business).
  - **change management and leadership** (u63, score **57.7**): heads "change management" / "leadership vs management"; 21 keywords; adjusted demand 59,040; Google Ads check: 14,800 for head 1 (Labs 14,800); KD 14; decision 0.14, template 0.10, question 0.00; 12-month slope 0.58; Trends 5-year 3.04 (rising); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 4 in 3 domains; arena 6 domains: online.hbs.edu (education, tier C, 68,686/mo); prosci.com (business); asq.org (business); ibm.com (business); nmsconsulting.com (business); apqc.org (business).
  - **stakeholder management** (u64, score **34.2**): heads "stakeholder management" / "stakeholder in project management"; 42 keywords; adjusted demand 6,120; Google Ads check: 2,400 for head 1 (Labs 2,400); KD 18; decision 0.00, template 0.00, question 0.12; 12-month slope 0.53; Trends 5-year 3.35 (rising); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 28 in 15 domains; arena 8 domains: mindtools.com (business); runn.io (business); geeksforgeeks.org (education, tier A, 2,532,368/mo); withluna.ai (business); planyway.com (business); greenly.earth (business); unito.io (business); gocardless.com (business).

### Design (8 topics, 17 scoring leaves, adjusted demand 1,197,730, mean leaf score 49.5)

#### web design

- **Topic total** (u42, score **68.2**): heads "website design" / "responsive design"; 26 keywords; adjusted demand 151,890; Google Ads check: 49,500 for head 1 (Labs 49,500); KD 35.5; decision 0.58, template 0.50, question 0.04; 12-month slope 0.55; Trends 5-year 2.89 (rising); AI Overview yes; weak page one yes (3 weak results); competitor articles (sitemap approximation) 39 in 10 domains; arena 4 domains: liquidweb.com (business); grovention.com (business); expertise.com (business); techrepublic.com (publication).

#### ux and ui design (discipline)

- **Topic total** (u19, score **67.1**): heads "ui ux design" / "ux design"; 110 keywords; adjusted demand 286,140; Google Ads check: 90,500 for head 1 (Labs 90,500); KD 6.5; decision 0.02, template 0.00, question 0.01; 12-month slope 0.90; Trends 5-year 1.81 (rising); AI Overview yes; weak page one no (2 weak results); competitor articles (sitemap approximation) 57 in 13 domains; arena 6 domains: codebyfarhan.com (business); monsoonfish.com (business); freecodecamp.org (business); ccccollege.com (business); letsgroto.com (business); flyingbisons.com (business).

#### ux research

- **Topic total** (u14, score **64.4**): heads "user testing" / "ux research"; 213 keywords; adjusted demand 264,020; Google Ads check: 18,100 for head 1 (Labs 18,100); KD 8; decision 0.12, template 0.11, question 0.05; 12-month slope 0.70; Trends 5-year 1.95 (rising); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 228 in 24 domains; arena 8 domains: usertesting.com (saas, tier C, 25,214/mo); userfeel.com (business); userlytics.com (business); maze.co (saas, tier D, 6,654/mo); coursera.org (education, tier A, 1,861,038/mo); indeed.design (business); ixdf.org (education, tier C, 32,981/mo); uxtweak.com (business). Note: user interviews (49,500) skipped as head 1: mostly the User Interviews brand.
  - **usability testing** (u17, score **58.4**): heads "user testing" / "usability testing"; 81 keywords; adjusted demand 34,700; Google Ads check: 18,100 for head 1 (Labs 18,100); KD 7; decision 0.14, template 0.14, question 0.06; 12-month slope 0.34; Trends 5-year 1.95 (rising); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 387 in 25 domains; arena 7 domains: usertesting.com (saas, tier C, 25,214/mo); userfeel.com (business); userlytics.com (business); nngroup.com (publication, tier C, 63,183/mo); maze.co (saas, tier D, 6,654/mo); figma.com (saas, tier A, 1,436,611/mo); geeksforgeeks.org (education, tier A, 2,532,368/mo).
  - **ux research (general)** (u18, score **58.4**): heads "ux research" / "user research"; 47 keywords; adjusted demand 20,220; Google Ads check: 2,900 for head 1 (Labs 2,900); KD 8; decision 0.13, template 0.09, question 0.04; 12-month slope 0.61; Trends 5-year 1.61 (rising); AI Overview yes; weak page one no (2 weak results); competitor articles (sitemap approximation) 58 in 12 domains; arena 6 domains: maze.co (saas, tier D, 6,654/mo); coursera.org (education, tier A, 1,861,038/mo); usertesting.com (saas, tier C, 25,214/mo); indeed.design (business); ixdf.org (education, tier C, 32,981/mo); uxtweak.com (business).
  - **surveys and questionnaires** (u15, score **55.1**): heads "closed-ended questions in research" / "customer feedback survey"; 61 keywords; adjusted demand 146,280; Google Ads check: 27,100 for head 1 (Labs 27,100); KD 8; decision 0.15, template 0.15, question 0.00; 12-month slope 0.95; Trends 5-year n/a (too small); AI Overview yes; weak page one no (0 weak results); competitor articles (sitemap approximation) 105 in 15 domains; arena 8 domains: methods.sagepub.com (business); nngroup.com (publication, tier C, 63,183/mo); kantar.com (business); proprofssurvey.com (business); questionpro.com (business); pollfish.com (business); usersnap.com (business); surveymonkey.com (business, tier B, 144,123/mo).
  - **interviews and focus groups** (u16, score **54.3**): heads "user interviews" / "semi-structured interviews in qualitative research"; 24 keywords; adjusted demand 62,820; Google Ads check: 49,500 for head 1 (Labs 49,500); KD 16; decision 0.00, template 0.00, question 0.12; 12-month slope 1.52; Trends 5-year 1.01 (flat); AI Overview yes; weak page one yes (4 weak results); competitor articles (sitemap approximation) 6 in 3 domains; arena 2 domains: usertesting.com (saas, tier C, 25,214/mo); centercode.com (business). Note: user interviews is also the User Interviews brand (userinterviews.com); most of this sub-topic is brand queries.

#### design systems and ui components

- **Topic total** (u50, score **60.8**): heads "design system" / "material design"; 96 keywords; adjusted demand 115,000; Google Ads check: 3,600 for head 1 (Labs 3,600); KD 6.5; decision 0.02, template 0.02, question 0.01; 12-month slope 0.93; Trends 5-year 3.44 (rising); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 3 in 3 domains; arena 6 domains: lovable.dev (business); blog.pixelfreestudio.com (business); figma.com (saas, tier A, 1,436,611/mo); magnific.com (business); gov.ie (business); design-system.canada.ca (business). Note: component-based software engineering, shadcn ui and design patterns are larger but software or brand queries.
  - **ui components and patterns** (u51, score **57.5**): heads "breadcrumbs ui" / "search bar ux"; 62 keywords; adjusted demand 68,590; Google Ads check: 880 for head 1 (Labs 880); KD 1; decision 0.02, template 0.00, question 0.00; 12-month slope 0.93; Trends 5-year n/a (too small); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 0 in 0 domains; arena 4 domains: thegood.com (business); wingify.com (business); uxmag.com (publication); sap.com (business). Note: many small UI-component phrases; design patterns and shadcn ui are software or brand queries.
  - **design systems** (u52, score **45.4**): heads "design system" / "material design"; 34 keywords; adjusted demand 46,410; Google Ads check: 3,600 for head 1 (Labs 3,600); KD 26.5; decision 0.03, template 0.06, question 0.03; 12-month slope 0.92; Trends 5-year 3.44 (rising); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 3 in 3 domains; arena 6 domains: lovable.dev (business); blog.pixelfreestudio.com (business); figma.com (saas, tier A, 1,436,611/mo); magnific.com (business); gov.ie (business); design-system.canada.ca (business).

#### information architecture

- **Topic total** (u70, score **53.3**): heads "information architecture" / "what is information architecture"; 37 keywords; adjusted demand 5,500; Google Ads check: 3,600 for head 1 (Labs 3,600); KD 11; decision 0.05, template 0.19, question 0.05; 12-month slope 0.66; Trends 5-year 4.60 (rising); AI Overview yes; weak page one no (2 weak results); competitor articles (sitemap approximation) 105 in 16 domains; arena 5 domains: optimalworkshop.com (business); uizard.io (business); babich.biz (business); ramotion.com (business); wix.com (business).

#### accessibility

- **Topic total** (u07, score **43.2**): heads "accessibility" / "web content accessibility"; 99 keywords; adjusted demand 291,660; Google Ads check: 110,000 for head 1 (Labs 110,000); KD 76; decision 0.07, template 0.01, question 0.01; 12-month slope 0.81; Trends 5-year 2.94 (rising); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 61 in 12 domains; arena 12 domains: nationaldisabilityinstitute.org (business); siteimprove.com (business); browngold.com (business); ixdf.org (education, tier C, 32,981/mo); accessible.org (business); adatile.com (business); deque.com (business); reciteme.com (business); accessibe.com (business); tasb.org (business); boia.org (business); adacompliancepros.com (business).
  - **accessibility definitions (general)** (u08, score **49.9**): heads "accessibility" / "accessibility definition"; 18 keywords; adjusted demand 199,400; Google Ads check: 110,000 for head 1 (Labs 110,000); KD 24.5; decision 0.06, template 0.00, question 0.06; 12-month slope 0.72; Trends 5-year 2.94 (rising); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 0 in 0 domains; arena 7 domains: nationaldisabilityinstitute.org (business); siteimprove.com (business); browngold.com (business); ixdf.org (education, tier C, 32,981/mo); accessible.org (business); adatile.com (business); deque.com (business).
  - **web and digital accessibility** (u10, score **40.4**): heads "web content accessibility" / "accessibility heuristics"; 19 keywords; adjusted demand 47,300; Google Ads check: 5,400 for head 1 (Labs 5,400); KD 94; decision 0.16, template 0.00, question 0.00; 12-month slope 0.75; Trends 5-year 6.50 (rising); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 53 in 14 domains; arena 7 domains: reciteme.com (business); accessibe.com (business); accessible.org (business); siteimprove.com (business); tasb.org (business); boia.org (business); adacompliancepros.com (business).
  - **guidelines and compliance (wcag, ada, 508)** (u09, score **39.1**): heads "accessibility 508" / "accessibility standards"; 25 keywords; adjusted demand 35,500; Google Ads check: 8,100 for head 1 (Labs 8,100); KD 67; decision 0.04, template 0.04, question 0.00; 12-month slope 0.61; Trends 5-year 3.78 (rising); AI Overview yes; weak page one no (0 weak results); competitor articles (sitemap approximation) 82 in 14 domains; arena 3 domains: wcag.com (business); vispero.com (business); levelaccess.com (business).
  - **accessibility testing and checkers** (u11, score **28.7**): heads "accessibility checker" / "accessibility tools"; 37 keywords; adjusted demand 14,860; Google Ads check: 4,400 for head 1 (Labs 4,400); KD 76; decision 0.05, template 0.00, question 0.00; 12-month slope 0.81; Trends 5-year 1.91 (rising); AI Overview yes; weak page one no (0 weak results); competitor articles (sitemap approximation) 16 in 5 domains; arena 6 domains: audioeye.com (business); tabnav.com (business); friendlycaptcha.com (business); accessibilityinsights.io (business); siteimprove.com (business); aaardvarkaccessibility.com (business).

#### design thinking

- **Topic total** (u27, score **41.0**): heads "design thinking" / "design thinking process"; 137 keywords; adjusted demand 33,640; Google Ads check: 18,100 for head 1 (Labs 18,100); KD 41; decision 0.05, template 0.01, question 0.04; 12-month slope 0.47; Trends 5-year 2.20 (rising); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 28 in 8 domains; arena 5 domains: ideou.com (business); designthinking.ideo.com (business); online.hbs.edu (education, tier C, 68,686/mo); nngroup.com (publication, tier C, 63,183/mo); ixdf.org (education, tier C, 32,981/mo).
  - **design thinking (general)** (u28, score **41.3**): heads "design thinking" / "what is design thinking"; 81 keywords; adjusted demand 25,480; Google Ads check: 18,100 for head 1 (Labs 18,100); KD 27; decision 0.01, template 0.02, question 0.04; 12-month slope 0.52; Trends 5-year 2.20 (rising); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 64 in 14 domains; arena 4 domains: ideou.com (business); designthinking.ideo.com (business); online.hbs.edu (education, tier C, 68,686/mo); nngroup.com (publication, tier C, 63,183/mo).
  - **design thinking process and stages** (u29, score **35.5**): heads "design thinking process" / "design thinking framework"; 56 keywords; adjusted demand 8,330; Google Ads check: 4,400 for head 1 (Labs 4,400); KD 52.5; decision 0.11, template 0.00, question 0.04; 12-month slope 0.40; Trends 5-year 7.70 (rising); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 30 in 7 domains; arena 5 domains: ideou.com (business); nngroup.com (publication, tier C, 63,183/mo); designthinking.ideo.com (business); online.hbs.edu (education, tier C, 68,686/mo); ixdf.org (education, tier C, 32,981/mo).

#### personas and journey maps

- **Topic total** (u43, score **40.0**): heads "customer journey map" / "user persona"; 90 keywords; adjusted demand 44,310; Google Ads check: 6,600 for head 1 (Labs 6,600); KD 23; decision 0.22, template 0.36, question 0.09; 12-month slope 0.47; Trends 5-year 0.82 (flat); AI Overview yes; weak page one no (0 weak results); competitor articles (sitemap approximation) 225 in 30 domains; arena 13 domains: contentful.com (business); usertesting.com (saas, tier C, 25,214/mo); triplewhale.com (business); uxpressia.com (business); awebdigital.co (business); cmswire.com (business); salesmate.io (business); weidert.com (business); mockflow.com (business); uxtweak.com (business); wix.com (business); lyssna.com (business); userpilot.com (saas, tier D, 9,854/mo).
  - **personas** (u45, score **45.5**): heads "user persona" / "customer persona"; 29 keywords; adjusted demand 13,180; Google Ads check: 1,900 for head 1 (Labs 1,900); KD 25; decision 0.21, template 0.24, question 0.10; 12-month slope 0.47; Trends 5-year 1.96 (rising); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 25 in 8 domains; arena 6 domains: uxpressia.com (business); mockflow.com (business); uxtweak.com (business); wix.com (business); lyssna.com (business); userpilot.com (saas, tier D, 9,854/mo).
  - **journey maps and user flows** (u44, score **43.0**): heads "customer journey map" / "user journey map"; 61 keywords; adjusted demand 31,130; Google Ads check: 6,600 for head 1 (Labs 6,600); KD 19; decision 0.23, template 0.41, question 0.08; 12-month slope 0.47; Trends 5-year 0.82 (flat); AI Overview yes; weak page one no (0 weak results); competitor articles (sitemap approximation) 231 in 30 domains; arena 8 domains: contentful.com (business); usertesting.com (saas, tier C, 25,214/mo); triplewhale.com (business); uxpressia.com (business); awebdigital.co (business); cmswire.com (business); salesmate.io (business); weidert.com (business).

### Business (7 topics, 14 scoring leaves, adjusted demand 1,148,140, mean leaf score 45.6)

#### analytics

- **Topic total** (u12, score **67.3**): heads "analytics" / "data analytics"; 93 keywords; adjusted demand 377,190; Google Ads check: 60,500 for head 1 (Labs 60,500); KD 18; decision 0.09, template 0.00, question 0.08; 12-month slope 0.71; Trends 5-year 1.55 (rising); AI Overview yes; weak page one no (2 weak results); competitor articles (sitemap approximation) 115 in 19 domains; arena 4 domains: marketingplatform.google.com (business); online.hbs.edu (education, tier C, 68,686/mo); sap.com (business); business.adobe.com (business).

#### pricing strategy

- **Topic total** (u30, score **53.6**): heads "pricing strategy" / "dynamic pricing"; 185 keywords; adjusted demand 126,510; Google Ads check: 6,600 for head 1 (Labs 6,600); KD 13; decision 0.03, template 0.05, question 0.04; 12-month slope 0.32; Trends 5-year 4.89 (rising); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 70 in 20 domains; arena 9 domains: paddle.com (business); bdc.ca (business); forbes.com (publication); salesforce.com (saas, tier B, 971,723/mo); dealhub.io (business); bcg.com (business); zapier.com (business); deliverect.com (business); business.com (business).
  - **pricing strategy types and models** (u32, score **53.6**): heads "dynamic pricing" / "competitive pricing"; 39 keywords; adjusted demand 28,190; Google Ads check: 18,100 for head 1 (Labs 18,100); KD 19; decision 0.13, template 0.21, question 0.00; 12-month slope 0.23; Trends 5-year 10.69 (rising); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 35 in 15 domains; arena 4 domains: salesforce.com (saas, tier B, 971,723/mo); dealhub.io (business); deliverect.com (business); business.com (business).
  - **pricing strategy (general)** (u31, score **47.7**): heads "pricing strategy" / "product pricing"; 95 keywords; adjusted demand 92,020; Google Ads check: 6,600 for head 1 (Labs 6,600); KD 20; decision 0.00, template 0.02, question 0.07; 12-month slope 0.36; Trends 5-year 4.89 (rising); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 110 in 25 domains; arena 7 domains: paddle.com (business); bdc.ca (business); forbes.com (publication); salesforce.com (saas, tier B, 971,723/mo); dealhub.io (business); bcg.com (business); zapier.com (business). Note: originality pricing (33,100) is noise.
  - **company pricing case studies** (u33, score **40.4**): heads "amazon pricing strategy" / "nike pricing strategy"; 51 keywords; adjusted demand 8,980; Google Ads check: 210 for head 1 (Labs 210); KD 0; decision 0.00, template 0.00, question 0.02; 12-month slope 0.42; Trends 5-year 167.50 (rising); AI Overview yes; weak page one no (0 weak results); competitor articles (sitemap approximation) 21 in 11 domains; arena 9 domains: getida.com (business); priceshape.com (business); prisync.com (business); channelkey.com (business); sellerlogic.com (business); catapult-analytics.com (business); perpetua.io (business); godaddy.com (business); salesduo.com (business). Note: what is retail pricing (5,400) is larger but not a case study.

#### growth marketing and funnels

- **Topic total** (u20, score **52.1**): heads "marketing funnel" / "content marketing"; 39 keywords; adjusted demand 289,200; Google Ads check: 9,900 for head 1 (Labs 9,900); KD 22; decision 0.05, template 0.03, question 0.05; 12-month slope 0.53; Trends 5-year 1.54 (rising); AI Overview yes; weak page one no (0 weak results); competitor articles (sitemap approximation) 225 in 30 domains; arena 6 domains: advertising.amazon.com (business); sproutsocial.com (business); semrush.com (business); business.adobe.com (business); skyword.com (business); ahrefs.com (business). Note: content marketing and marketing strategy are larger but generic marketing; marketing funnel is the product-adjacent head.

#### okrs, kpis and metrics

- **Topic total** (u24, score **50.6**): heads "okr" / "kpi examples"; 153 keywords; adjusted demand 197,560; Google Ads check: 33,100 for head 1 (Labs 33,100); KD 22; decision 0.19, template 0.15, question 0.10; 12-month slope 0.62; Trends 5-year 0.83 (flat); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 25 in 11 domains; arena 10 domains: monday.com (business); mailchimp.com (business); lattice.com (business); thestrategyinstitute.org (business); peoplelogic.ai (business); projectmanager.com (business); netsuite.com (business); zapier.com (business); tempo.io (business); ibm.com (business).
  - **metrics (general)** (u26, score **56.0**): heads "kpi examples" / "kpi metrics"; 34 keywords; adjusted demand 113,780; Google Ads check: 14,800 for head 1 (Labs 14,800); KD 19; decision 0.06, template 0.03, question 0.03; 12-month slope 0.64; Trends 5-year 1.29 (rising); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 25 in 17 domains; arena 5 domains: netsuite.com (business); zapier.com (business); tempo.io (business); ibm.com (business); mailchimp.com (business).
  - **okrs** (u25, score **51.0**): heads "okr" / "okr vs kpi"; 119 keywords; adjusted demand 83,780; Google Ads check: 33,100 for head 1 (Labs 33,100); KD 24; decision 0.23, template 0.18, question 0.12; 12-month slope 0.62; Trends 5-year 0.83 (flat); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 18 in 10 domains; arena 6 domains: monday.com (business); mailchimp.com (business); lattice.com (business); thestrategyinstitute.org (business); peoplelogic.ai (business); projectmanager.com (business).

#### go-to-market and product marketing

- **Topic total** (u54, score **49.8**): heads "4 ps of marketing" / "product marketing"; 42 keywords; adjusted demand 81,600; Google Ads check: 12,100 for head 1 (Labs 12,100); KD 18; decision 0.05, template 0.05, question 0.24; 12-month slope 0.35; Trends 5-year 0.84 (flat); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 58 in 15 domains; arena 6 domains: productmarketingalliance.com (business); corporatefinanceinstitute.com (business); study.com (business); professionalacademy.com (business); prisim.com (business); angle180.com (business).

#### retention, churn and engagement

- **Topic total** (u55, score **43.4**): heads "customer retention" / "retention rate"; 120 keywords; adjusted demand 39,340; Google Ads check: 3,600 for head 1 (Labs 3,600); KD 18; decision 0.20, template 0.02, question 0.19; 12-month slope 0.62; Trends 5-year 3.44 (rising); AI Overview yes; weak page one no (0 weak results); competitor articles (sitemap approximation) 86 in 17 domains; arena 15 domains: dealhub.io (business); referralcandy.com (business); propellocloud.com (business); quiq.com (business); customergauge.com (business); customerthermometer.com (business); blog.accessdevelopment.com (business); customersuccesscollective.com (business); moengage.com (business); zendesk.com (business); adp.com (business); stellic.com (business); productplan.com (saas, tier C, 20,541/mo); wallstreetprep.com (education, tier B, 200,075/mo); 15five.com (business).
  - **retention (general)** (u57, score **40.1**): heads "retention rate" / "engagement rate"; 52 keywords; adjusted demand 14,900; Google Ads check: 3,600 for head 1 (Labs 3,600); KD 22; decision 0.04, template 0.02, question 0.12; 12-month slope 0.47; Trends 5-year 3.33 (rising); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 53 in 10 domains; arena 6 domains: zendesk.com (business); adp.com (business); stellic.com (business); productplan.com (saas, tier C, 20,541/mo); wallstreetprep.com (education, tier B, 200,075/mo); 15five.com (business).
  - **retention rate formulas and calculation** (u56, score **39.3**): heads "calculate retention rate" / "customer retention rate formula"; 49 keywords; adjusted demand 4,870; Google Ads check: 1,600 for head 1 (Labs 1,600); KD 16; decision 0.39, template 0.00, question 0.33; 12-month slope 0.69; Trends 5-year 0.81 (flat); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 45 in 9 domains; arena 8 domains: compt.io (business); adp.com (business); wallstreetprep.com (education, tier B, 200,075/mo); vendordirectory.shrm.org (business); hibob.com (business); productive.io (business); churnkey.co (business); adjust.com (business).
  - **customer retention and loyalty** (u58, score **36.1**): heads "customer retention" / "customer retention strategies"; 19 keywords; adjusted demand 19,570; Google Ads check: 3,600 for head 1 (Labs 3,600); KD 26; decision 0.16, template 0.05, question 0.05; 12-month slope 0.51; Trends 5-year 3.44 (rising); AI Overview yes; weak page one no (0 weak results); competitor articles (sitemap approximation) 147 in 18 domains; arena 9 domains: dealhub.io (business); referralcandy.com (business); propellocloud.com (business); quiq.com (business); customergauge.com (business); customerthermometer.com (business); blog.accessdevelopment.com (business); customersuccesscollective.com (business); moengage.com (business).

#### a/b testing and experimentation

- **Topic total** (u46, score **39.3**): heads "a/b testing" / "a/b testing tools"; 113 keywords; adjusted demand 32,160; Google Ads check: 12,100 for head 1 (Labs 12,100); KD 38; decision 0.14, template 0.10, question 0.09; 12-month slope 0.82; Trends 5-year 2.47 (rising); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 64 in 18 domains; arena 12 domains: salesforce.com (saas, tier B, 971,723/mo); geeksforgeeks.org (education, tier A, 2,532,368/mo); kameleoon.com (business); coursera.org (education, tier A, 1,861,038/mo); mastercard.com (business); business.adobe.com (business); convert.com (business); piwik.pro (business); growthbook.io (business); dripagency.de (business); conversionista.com (business); awa-digital.com (business).
  - **a/b testing (general)** (u47, score **45.0**): heads "a/b testing" / "what is a b testing"; 40 keywords; adjusted demand 29,570; Google Ads check: 12,100 for head 1 (Labs 12,100); KD 48; decision 0.20, template 0.28, question 0.15; 12-month slope 0.82; Trends 5-year 2.47 (rising); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 76 in 20 domains; arena 6 domains: salesforce.com (saas, tier B, 971,723/mo); geeksforgeeks.org (education, tier A, 2,532,368/mo); kameleoon.com (business); coursera.org (education, tier A, 1,861,038/mo); mastercard.com (business); business.adobe.com (business).
  - **a/b testing tools and platforms** (u48, score **42.5**): heads "a/b testing tools" / "a/b testing software"; 39 keywords; adjusted demand 3,650; Google Ads check: 260 for head 1 (Labs 260); KD 23; decision 0.21, template 0.00, question 0.08; 12-month slope 0.88; Trends 5-year 33.90 (rising); AI Overview yes; weak page one no (2 weak results); competitor articles (sitemap approximation) 63 in 18 domains; arena 6 domains: convert.com (business); piwik.pro (business); growthbook.io (business); dripagency.de (business); conversionista.com (business); awa-digital.com (business).
  - **a/b testing in marketing (email, landing pages, ads)** (u49, score **17.5**): heads "a/b testing landing pages" / "email a/b testing"; 34 keywords; adjusted demand 840; Google Ads check: 170 for head 1 (Labs 170); KD 38; decision 0.00, template 0.00, question 0.03; 12-month slope 0.82; Trends 5-year n/a (too small); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) 66 in 18 domains; arena 7 domains: unbounce.com (business); knowledge.hubspot.com (business); crazyegg.com (business); contentful.com (business); blog.adobe.com (business); wynter.com (business); landingi.com (business).


## 3. The launch shortlist

The top eight by score, counting a topic and its sub-topic once when they share head term 1 (product manager:
u59 and u61; prioritization: u35 and u34; user testing: u14 and u17; design system: u50 and u52).

| # | Unit | Score | Why it scores | Head articles (titled in the words people search) |
|---|---|---|---|---|
| 1 | Product owner and product manager roles (u59) | 75.2 | KD 8, small arena (4), empty AI Overview, rising | "What Does a Product Manager Do?"; "Product Owner vs Product Manager: The Real Difference"; "Technical Product Manager: Role and Skills"; "Associate Product Manager: What the Job Is" |
| 2 | Prioritization (general, u35) | 74.6 | 153,570 adjusted at KD 1, rising, 4 arena domains | "Prioritization: What It Means and How Product Teams Do It"; "MoSCoW Prioritization (with Template)"; "Prioritization Matrix: Examples and Template"; "RICE Prioritization: How to Score Features" |
| 3 | Web design (u42) | 68.2 | 151,890 adjusted, decision 0.58 and template 0.50, weak page one (3) | "Website Design Principles That Work"; "Responsive Design: A Practical Guide"; "Portfolio Website Examples" |
| 4 | Analytics (u12) | 67.3 | the largest single demand (377,190), KD 18, rising | "Product Analytics vs Data Analytics"; "What Is Analytics? A Product Team's Guide"; "Business Analytics for Product Managers" |
| 5 | UX and UI design (discipline, u19) | 67.1 | 286,140 adjusted at KD 6.5, rising | "UI vs UX Design: What Is the Difference?"; "What Is UX Design?"; "Product Design vs UX Design" |
| 6 | Project management (u13) | 65.4 | 345,140 adjusted at KD 15 | "Project Management vs Product Management"; "Project Management Tools for Product Teams" |
| 7 | UX research (topic, u14) | 64.4 | 264,020 adjusted at KD 8 | "User Testing: How to Run Your First Session"; "Usability Testing Questions (with Examples)"; "UX Research Methods"; "Closed-Ended Questions in Research: Examples" |
| 8 | Design systems and UI components (u50) | 60.8 | 115,000 adjusted at KD 6.5, rising | "What Is a Design System?"; "Design System Examples (Material Design and Others)"; "UI Components Glossary: Breadcrumbs, Steppers, Chips" |

Read before acting: three of the eight are broad fields where the site would be one voice among many and where
the keyword set is mostly not about products (analytics is largely the data-analyst field; web design is agency and
"website design" commercial searches with YouTube and Dribbble on page one; project management is PMI and course
providers). They score on size and low median KD; owner_fit will decide them. Next in line, all core to the brief:
product management general (u22, 60.6), product strategy and product-market fit (u66, 60.3), UX research general
(u18, 58.4), change management (u63, 57.7), product management tools (u72, 57.7), product roadmap (u69, 57.6),
requirements and PRD (u53, 56.9), user stories (u38, 56.7), acceptance criteria (u41, 56.4).

## 4. What the hypothesis got wrong

- **Metrics topics barely exist as phrases.** "ux metrics" (2 keywords at volume 100+), "product metrics" (1) and
  "saas metrics" (4) are not searched in those words. The metrics demand sits on "kpi examples" (14,800),
  "metrics" (a dictionary query, 60,500) and engineering "dora metrics" (8,100); the metrics (general) unit scores
  56.0 on that borrowed demand, with SaaS vendors (NetSuite, Zapier, IBM, Mailchimp) on page one.
- **Surveys and OKRs stand on their own.** Surveys and questionnaires is the biggest UX research sub-topic
  (146,280 adjusted, KD 8, score 55.1), led by "closed-ended questions in research" (27,100); its page one is
  research publishers and survey vendors (NIH, SAGE, NN/g, Kantar, QuestionPro, SurveyMonkey). OKRs is a
  119-keyword sub-topic (83,780 adjusted, KD 24, score 51.0, flat trend); "okr" page one is HR and work-management
  SaaS (monday.com, Mailchimp, Lattice). Neither was a planned top-level topic.
- **Template demand lives inside product topics.** Template share: user stories 0.41 (the examples and templates
  sub-topic 1.00), journey maps 0.41, product roadmap 0.34, requirements and PRD 0.33. The Templates section units
  score 52.5 (agile user story templates, product roadmap templates) and 44.9 (user story templates); the article
  and the template are one search intent and should be one page plus a download.
- **Retention leans HR.** "calculate retention rate" page one: Compt, ADP, SHRM's vendor directory, HiBob next to
  Wall Street Prep, Churnkey and Adjust. "retention rate": Wikipedia, Zendesk, a university, ADP, 15Five. The
  retention topic has the most crowded arena of all units (15 domains) and scores 43.4.
- **Agile is the largest topic and one of the hardest.** 370,120 adjusted (the largest), KD 36 at topic level, 47
  for agile project management, 45 for SAFe; Atlassian (tier B) and agilealliance.org hold page one and the arena
  has 9 domains. Score 48.2. Within it, Trends has "agile methodology" rising (2.39) but "agile scrum" (0.54),
  "agile manifesto" (0.47) and "safe agile framework" (0.31) falling.
- **Two smaller corrections.** "user interviews" (49,500) is mostly the User Interviews brand (Trustpilot, Reddit
  and the brand on page one). Prioritization's general demand is largely definitional ("another word for
  prioritization", "prioritization definition"), so the 153,570 is softer than it looks.

## 5. The section trees with Phase 4 scores

Carried over from `research/seo/section-trees-v1.md` (tree, stock, open questions unchanged there). The section
units are scored on the same scale as the article units.

| Section | Category | Phase 3 build-order score | Phase 4 score |
|---|---|---|---|
| Links | UX and UI design tools | 2,357 | 44.9 |
| Links | Product management tools | 2,208 | 57.7 |
| Links | Prototyping tools | 858 | 45.8 |
| Books | Product management books | 980 | 42.8 |
| Books | UX design books | 530 | 45.5 |
| Books | Graphic and visual design books | 1,690 | 46.2 |
| Books | Design books (general) | up to 4,090 | 53.1 |
| Templates | User story templates | 9,700 | 44.9 |
| Templates | Agile and scrum user story templates | (child) | 52.5 |
| Templates | Product roadmap templates | 1,156 | 52.5 |
| Tools | Sample size calculators | 9,369 | 41.6 |
| Tools | Power analysis sample size calculators | 1,960 | 33.4 |
| Tools | Survey sample size calculators | 1,605 | 31.1 |
| Tools | Statistical significance sample size calculators | (child) | 36.0 |

What changes: the two orders mostly agree inside each section. The Phase 4 score rewards product management tools
over UX design tools (an empty AI Overview on "product management tools", KD 8), and it marks the calculators down
because sample size calculator demand is falling on Trends (0.41 over five years) and their KD is the highest of
the section units. The section units sit in the middle of the article range; none is a traffic play on its own,
which matches the Phase 3 reading (Links and Books as authority and return-visit sections, Templates paired with
articles).

### Section units in detail

#### Links

- **product management tools** (u72, score **57.7**): heads "product management tools" / "roadmap tools"; 10 keywords; adjusted demand 2,400; Google Ads check: 880 for head 1 (Labs 880); KD 8; decision 1.00, template 0.00, question 0.00; 12-month slope 0.48; Trends 5-year 11.47 (rising); AI Overview yes (empty); weak page one no (1 weak results); competitor articles (sitemap approximation) n/a; arena 12 domains: blog.ravi-mehta.com (business); tech.co (business); themuse.com (business); designsystemscollective.com (business); omr.com (business); atlassian.com (saas, tier B, 420,717/mo); support.microsoft.com (business); miro.com (saas, tier B, 163,746/mo); canny.io (business); gartner.com (business); productplan.com (saas, tier C, 20,541/mo); thedigitalprojectmanager.com (business).
- **prototyping tools** (u73, score **45.8**): heads "prototyping tools" / "ai prototyping tools"; 17 keywords; adjusted demand 1,160; Google Ads check: 480 for head 1 (Labs 480); KD 26; decision 1.00, template 0.00, question 0.00; 12-month slope 0.36; Trends 5-year 30.50 (rising); AI Overview yes; weak page one no (2 weak results); competitor articles (sitemap approximation) n/a; arena 5 domains: bilt.me (business); testingtime.com (business); blog.logrocket.com (business); sitepoint.com (business); ux.stackexchange.com (business).
- **ux and ui design tools** (u71, score **44.9**): heads "ux design tools" / "ux tools"; 19 keywords; adjusted demand 2,910; Google Ads check: 1,300 for head 1 (Labs 1,300); KD 19; decision 1.00, template 0.00, question 0.00; 12-month slope 1.80; Trends 5-year 14.89 (rising); AI Overview yes; weak page one no (2 weak results); competitor articles (sitemap approximation) n/a; arena 12 domains: hype4.academy (business); figma.com (saas, tier A, 1,436,611/mo); uxpilot.ai (business); uxtools.co (business, tier D, 260/mo); pixso.net (business); maze.co (saas, tier D, 6,654/mo); uxmastery.com (business); looppanel.com (business); uxdesigninstitute.com (business); paulolyslager.com (business); convert.com (business); careerkarma.com (business).

#### Books

- **design books (general)** (u74, score **53.1**): heads "design books" / "best books on design"; 16 keywords; adjusted demand 4,090; Google Ads check: 1,300 for head 1 (Labs 1,300); KD no data; decision 0.31, template 0.00, question 0.00; 12-month slope 0.59; Trends 5-year 3.67 (rising); AI Overview yes; weak page one yes (3 weak results); competitor articles (sitemap approximation) n/a; arena 3 domains: sobrief.com (business); bostonmagazine.com (business); hellolovelystudio.com (business). Note: design books (Phase 0 SERP reused) and books about design are variants of one query.
- **graphic and visual design books** (u75, score **46.2**): heads "graphic design books" / "best graphic design books"; 26 keywords; adjusted demand 1,690; Google Ads check: 1,300 for head 1 (Labs 1,300); KD no data; decision 0.38, template 0.00, question 0.00; 12-month slope 1.43; Trends 5-year 2.68 (rising); AI Overview yes; weak page one no (1 weak results); competitor articles (sitemap approximation) n/a; arena 2 domains: yourcentralvalley.com (business); dragonflyeditorial.com (business).
- **ux design books** (u77, score **45.5**): heads "ux books" / "best ux books"; 21 keywords; adjusted demand 530; Google Ads check: 390 for head 1 (Labs 390); KD no data; decision 0.48, template 0.00, question 0.00; 12-month slope 1.00; Trends 5-year 3.18 (rising); AI Overview yes; weak page one no (2 weak results); competitor articles (sitemap approximation) n/a; arena 6 domains: johannesippen.com (expert, tier D, 72/mo); dontpaniclabs.com (business); ixdf.org (education, tier C, 32,981/mo); uxplanet.org (publication, tier C, 13,291/mo); blog.uxfol.io (saas, tier D, 685/mo); smart-interface-design-patterns.com (business).
- **product management books** (u76, score **42.8**): heads "product management books" / "best product management books"; 14 keywords; adjusted demand 980; Google Ads check: 590 for head 1 (Labs 590); KD no data; decision 0.43, template 0.00, question 0.00; 12-month slope 0.62; Trends 5-year 11.38 (rising); AI Overview yes; weak page one yes (3 weak results); competitor articles (sitemap approximation) n/a; arena 10 domains: bringthedonuts.com (expert, tier D, 586/mo); productplan.com (saas, tier C, 20,541/mo); userflow.com (saas, tier D, 1,854/mo); nextleap.app (education, tier D, 3,947/mo); simonsovic.com (business); audible.com (business); prodpad.com (business); mentorcruise.com (business); productmanagementexercises.com (education, tier D, 332/mo); gainsight.com (business).

#### Templates

- **user story templates > agile and scrum user story templates** (u79, score **52.5**): heads "agile user story template" / "scrum user story template"; 12 keywords; adjusted demand 3,180; Google Ads check: 1,600 for head 1 (Labs 1,600); KD 13; decision 1.00, template 1.00, question 0.00; 12-month slope 0.54; Trends 5-year n/a (too small); AI Overview yes; weak page one no (2 weak results); competitor articles (sitemap approximation) n/a; arena 5 domains: wrike.com (business); mockplus.com (business); atlassian.com (saas, tier B, 420,717/mo); agilealliance.org (business); agilemania.com (business).
- **product roadmap templates** (u80, score **52.5**): heads "product roadmap template" / "product roadmap powerpoint template"; 14 keywords; adjusted demand 1,250; Google Ads check: 1,000 for head 1 (Labs 1,000); KD 7.5; decision 1.00, template 1.00, question 0.00; 12-month slope 0.57; Trends 5-year 0.93 (flat); AI Overview yes; weak page one no (2 weak results); competitor articles (sitemap approximation) n/a; arena 6 domains: notion.com (saas, tier B, 320,481/mo); todoist.com (business); super.so (business); clickup.com (saas, tier B, 118,417/mo); digitalmarketinginstitute.com (business); ideascale.com (business).
- **user story templates** (u78, score **44.9**): heads "user story template" / "agile user story template"; 26 keywords; adjusted demand 11,150; Google Ads check: 2,900 for head 1 (Labs 2,900); KD 13; decision 1.00, template 1.00, question 0.00; 12-month slope 0.56; Trends 5-year 0.47 (falling); AI Overview yes; weak page one no (2 weak results); competitor articles (sitemap approximation) n/a; arena 9 domains: atlassian.com (saas, tier B, 420,717/mo); agilealliance.org (business); rebelscrum.site (business); mountaingoatsoftware.com (expert, tier D, 9,692/mo); aha.io (saas, tier C, 28,822/mo); smartsheet.com (saas, tier B, 188,985/mo); wrike.com (business); mockplus.com (business); agilemania.com (business).

#### Tools

- **sample size calculators** (u81, score **41.6**): heads "sample size calculator" / "sample size calculator formula"; 68 keywords; adjusted demand 14,990; Google Ads check: 8,100 for head 1 (Labs 8,100); KD 37.5; decision 1.00, template 0.01, question 0.00; 12-month slope 0.59; Trends 5-year 0.41 (falling); AI Overview yes (empty); weak page one no (0 weak results); competitor articles (sitemap approximation) n/a; arena 7 domains: sawtoothsoftware.com (business); idsurvey.com (business); medcalc.org (business); easymedstat.com (business); numiqo.com (business); tool.yrjournal.org (business); socscistatistics.com (business).
- **sample size calculators > statistical significance sample size calculators** (u84, score **36.0**): heads "statistical sample size calculator" / "sample size statistical significance calculator"; 14 keywords; adjusted demand 650; Google Ads check: 480 for head 1 (Labs 480); KD 43; decision 1.00, template 0.00, question 0.00; 12-month slope 0.27; Trends 5-year 0.43 (falling); AI Overview yes (empty); weak page one no (1 weak results); competitor articles (sitemap approximation) n/a; arena 6 domains: blog.flexmr.net (business); medcalc.org (business); numiqo.com (business); xlstat.com (business); qualitygurus.com (business); geopoll.com (business).
- **sample size calculators > power analysis sample size calculators** (u82, score **33.4**): heads "power analysis sample size calculator" / "g power sample size calculator"; 24 keywords; adjusted demand 2,390; Google Ads check: 880 for head 1 (Labs 880); KD 18; decision 1.00, template 0.00, question 0.00; 12-month slope 0.66; Trends 5-year 0.01 (falling); AI Overview yes; weak page one no (0 weak results); competitor articles (sitemap approximation) n/a; arena 6 domains: clincalc.com (business); statscalculators.com (business); sample-size.net (business); stat.ubc.ca (business); surveymonkey.com (business, tier B, 144,123/mo); numiqo.com (business).
- **sample size calculators > survey sample size calculators** (u83, score **31.1**): heads "sample size calculator for survey"; 13 keywords; adjusted demand 2,140; Google Ads check: 390 for head 1 (Labs 390); KD 25; decision 1.00, template 0.00, question 0.00; 12-month slope 0.76; Trends 5-year n/a (too small); AI Overview yes; weak page one no (0 weak results); competitor articles (sitemap approximation) n/a; arena 7 domains: blog.flexmr.net (business); sogolytics.com (business); omnicalculator.com (calculator, tier A, 11,060,954/mo); surveymars.com (business); socscistatistics.com (business); frac.tl (business); questionpro.com (business). Note: SurveyMonkey, Raosoft and Qualtrics calculators are brand queries.


## 6. Data caveats

- **Variant inflation.** Keyword suggestions return word-order variants that share one Google volume ("agile
  approach", "agile computing" and 15 more at 135,000). Adjusted demand counts each series once, but unrelated
  keywords can still share a series by chance, and some variants are other meanings ("design of books").
- **Four noisy seeds.** Journey map, design system, accessibility and prioritization pulled other meanings; noise
  rules removed most, but some survive inside units ("titanic journey map", "plant design management system",
  "use high priority notification meaning", "component-based software engineering").
- **Ranked-keyword pulls sorted by volume.** The Phase 2 competitor pulls are each domain's 500 biggest keywords,
  not their on-topic ones; the coverage counts say who holds head terms, not who has pages.
- **Google Ads is not an independent check.** The Ads volumes equal the Labs volumes for 223 of 233 keywords
  (median ratio 1.00) and 222 have the identical 12-month series, so it confirms the scale only. The outliers are role
  terms ("product manager" Ads 6,600 versus Labs 22,200; "ui/ux designer" 90,500 versus 14,800).
- **The 12-month decline is a window effect.** The Labs and Ads slope (Jun-Aug 2026 over Sep-Nov 2025) has a median
  of 0.62 on the 57 head terms with a readable Trends series; Google Trends over the same weeks has a median of
  0.99 (Trends is higher for 43 of the 57). The Phase 1 decline signal is seasonality in that window, not falling interest; the score uses the
  five-year Trends direction instead.
- **Trends relativity.** Values are relative inside each group of up to five terms; 8 head terms stayed too small
  to read even after regrouping (long phrases such as "user stories template"). Many terms rise 2 to 5 times over
  five years; read the direction, not the multiple, and do not compare terms across groups.
- **AI Overview everywhere.** All 68 head-term SERPs carry an AI Overview (4 empty placeholders), so that component
  separates almost nothing; it moves only the five units whose head term had an empty one.
- **Weak page one is rare.** 6 of 68 head terms have three or more weak results; the rule counts Medium, Reddit,
  LinkedIn and SaaS glossaries but not app stores, Trustpilot or thin agency pages.
- **Books difficulty missing.** KD is 0 (no data) on the book keywords; those units get the middle value.
- **Arena typing.** 279 of the Phase 4 page-one domains were not in the competitor CSVs and were typed by rule;
  most count as "business" (SaaS vendors, agencies, consultancies, training firms).
- **owner_fit is empty.** The score ranks the data, not the author's authority; it will over-rank broad fields.
- **Topic totals and sub-topics are both scored,** so a topic and its biggest sub-topic often sit next to each
  other in the ranking.

## 7. Next steps

1. Owner fills owner_fit (1 to 3) in `research/seo/keywords/topic-scores-2026-10-08.csv`; drop the 1s and re-read
   the shortlist.
2. Pick four to six launch topics from the shortlist plus the next-in-line core topics; for each, write the head
   article list as titles in the words people search (section 3 is the draft).
3. Pair template articles with downloads (user stories, journey maps, roadmap, PRD) and decide the template format.
4. Sharpen thin arenas with on-topic ranked-keyword pulls (keyword contains the topic word, position 20 or better)
   for nngroup.com, ixdf.org and smashingmagazine.com: about $0.07 each.
5. Re-cluster with the jobs to be done fix (19 rows now unflagged) and check whether it becomes a topic.
6. UK (2826) and Canada (2124) volumes for the chosen launch topics only: one Google Ads task each, about $0.06.
7. Keep Trends for direction only; re-pull in 90 days on the launch head terms.
