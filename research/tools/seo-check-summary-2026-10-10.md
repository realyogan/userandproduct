# Tool ideas: the paid search check (2026-10-10)

The paid check the owner approved on October 10, 2026. It measured the 199 tool phrases the keyword store did not cover and rescored the 82 tool ideas on search intent and openness of page one; usefulness, fit and build cost are unchanged. Spend $0.226 against an estimate of about $0.23 and a cap of $0.40; balance after $19.89.

Files: `research/seo/keywords/tools-2026-10-10.csv` (phrase, idea id, US, UK, CA volume, difficulty, CPC, trend, intent), `research/seo/serps/tools-2026-10-10.csv` (19 page ones), `research/tools/opportunities-2026-10-10.csv` and `.md` (rescored and re-ranked), the board at `research/explainers/tools-opportunities-2026-10-10.html`.

## What was measured

- Google Ads search volume, standard queue: US for 198 phrases (prioritization matrix reused from October 8), UK and Canada for the 69 shortlist phrases.
- Keyword difficulty (KD, 0 to 100), US, 198 phrases; 40 came back with no difficulty and 28 with no US volume (too little data; recorded as no data, not zero).
- Google page one, US, top 10, for 19 head phrases (17 new; SUS and churn reused from October 8). Each result is typed as big product, SaaS calculator or content, thin calculator site, editorial, or forum and user posts.

## The short version

- The exact tool phrases are small. Most calculator and generator phrases are 10 to 110 searches a month in the US: SUS score calculator 50, sprint capacity calculator 30, user story generator 30, RICE score calculator 50, type scale generator 110, PRD generator 110. 'OKR checker', 'microcopy checker', 'survey question checker', 'Monte Carlo forecast agile' and the survey margin of error phrases had no data at all.
- The demand sits on template, example and formula phrases instead: PRD template, user story template, OKR examples, positioning statement examples, product survey questions, retention rate formula. A tool page that teaches and builds answers those.
- One real tool head turned up: NPS calculator, 8,100 a month in the US, 5,400 in the UK, 720 in Canada, difficulty 16; plus 'how to calculate nps' 1,900. It moves from the drip into the launch ten.
- The other big tool phrases are out of reach: color palette generator 74,000 (KD 100), color contrast checker 12,100 and contrast checker 8,100 (KD 56 to 59, page one held by WebAIM, Adobe and accessibility vendors).
- An AI Overview sits on 18 of the 19 page ones; only 'color contrast checker' has none. Page one for the generator phrases is AI writing apps (PRD, user story, survey questions); for the calculators it is SaaS lead magnets and thin single-purpose sites.
- Openest page ones: SUS score calculator (NN/g article, forum posts, KD 2), type scale generator (thin sites, Hacker News, a GitHub gist), spacing scale generator (seven thin sites), tint and shade generator (thin sites, Tumblr, Facebook), Monte Carlo forecast (papers and forums). Closest held: RICE (nine vendor calculators), churn (SaaS lead magnets), user story generator (Miro, Atlassian, Figma).

## How the scores changed

- Search intent (1 to 5) is now the measured monthly US demand across the idea's phrases, weighted by what the searcher wants: tool, template and example phrases count in full, how-to phrases half, definitional phrases a fifth (capped at 1,000 per idea), and phrases above difficulty 60 are left out as out of reach. 5 = 5,000 or more, 4 = 1,500, 3 = 500, 2 = 150, 1 = less. The 'when will it be done' volume (2,400) is a song and is left out.
- Openness (1 to 5) comes from the difficulty of the phrase worth targeting (the best mix of volume and ease among tool, template and how-to phrases of 50 searches or more): 5 = KD 10 or less, 4 = 20, 3 = 35, 2 = 50, 1 = above. Where page one was pulled: plus one when five or more of the top ten are thin calculator sites or forum posts, minus one when seven or more are big products or SaaS pages.
- Ideas with no phrase in the check keep their scores. Score = (3 U + 2 I + 2 O + 2 F + C) x 2, as before; ties broken by usefulness.

## The recommended launch ten

Three swaps. In: PRD outline generator, NPS calculator with margin of error, survey question checker. Out: delivery forecast, survey sample size and margin of error calculator (both to the drip), usability test sample size calculator (to later).

| # | Tool | Lead phrase (US vol, KD) | Best measured tool phrase | US | UK | CA | KD | Page one (top 10, US) | Score | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | PRD outline generator | prd template (2,900, KD 6) | prd generator | 110 | 20 | 20 | 5 | 6 SaaS calculator or content, 3 forum or UGC; top three brilworks.com, chatprd.ai, telos-ai.org | 84 -> 92 | In. Strongest score after the check. |
| 2 | User story and acceptance criteria builder | user story template (2,900, KD 18) | user story generator | 30 | 10 | 10 | 0 | 3 big product, 5 SaaS calculator or content, 1 forum or UGC; top three kollabe.com, easyretro.io, reddit.com | 90 -> 90 | Stays. Template demand, weekly use. |
| 3 | Type scale generator | type scale generator (110, KD 30) | type scale generator | 110 | 30 | 20 | 30 | 1 SaaS calculator or content, 4 thin calculator site, 1 editorial, 3 forum or UGC; top three illustration.app, news.ycombinator.com, gist.github.com | 82 -> 86 | Stays. Small but beatable. |
| 4 | OKR checker | okr examples (1,300, KD 5) | how to write okrs | 170 | 40 | 10 | 17 | 1 big product, 5 SaaS calculator or content, 2 forum or UGC; top three profit.co, linkedin.com, polly.ai | 82 -> 86 | Stays. Examples page with a checker. |
| 5 | NPS calculator with margin of error | nps calculator (8,100, KD 16) | nps calculator | 8,100 | 5,400 | 720 | 16 | 2 big product, 5 SaaS calculator or content, 1 thin calculator site, 1 forum or UGC; top three npscalculator.com, surveymonkey.com, gainsight.com | 78 -> 86 | In. The surprise: real tool demand in all three countries. |
| 6 | Survey question checker | product survey questions (1,600, KD 8) | how to write survey questions | 480 | 20 | 10 | 37 | 5 SaaS calculator or content, 3 thin calculator site; top three surveymars.com, akiosurvey.com, involve.me | 74 -> 86 | In. Template demand, no rule-based rival. |
| 7 | SUS score calculator | sus score calculator (50, KD 2) | sus score calculator | 50 | 20 | 10 | 2 | 3 SaaS calculator or content, 1 thin calculator site, 1 editorial, 2 forum or UGC; top three nngroup.com, yourcx.io, stackoverflow.com | 92 -> 84 | Stays on usefulness and openness; little traffic. |
| 8 | Backlog prioritization scorer (RICE, ICE, WSJF) | rice score calculator (50, KD 0) | prioritization matrix | 2,400 | 1,300 | 480 | 21 | 8 SaaS calculator or content, 1 thin calculator site; top three productlift.dev, easyretro.io, userpilot.com | 88 -> 84 | Stays. MoSCoW and matrix carry the demand. |
| 9 | Sprint capacity calculator | sprint capacity calculator (30, KD 0) | capacity planning scrum | 140 | 10 | 10 | 0 | 2 big product, 4 SaaS calculator or content, 1 editorial, 2 forum or UGC; top three float.com, atlassian.com, pawelrola.com | 88 -> 84 | Stays on repeat use; little traffic. |
| 10 | Retention and churn calculator | churn rate calculator (260, KD 18) | churn rate calculator | 260 | 70 | 30 | 18 | 7 SaaS calculator or content, 2 thin calculator site; top three mailmodo.com, amplitude.com, saaselevate.com | 84 -> 84 | Stays. Formula demand holds. |

Build effort: about 75 hours of plain JavaScript (was about 76). Spread: Product 4 (user story, PRD, prioritization, sprint capacity), Business 3 (OKR, NPS, retention), Design and research 3 (type scale, SUS, survey questions). No accessibility tool still; the palette contrast checker stays first reserve.

Why each swap:

- **PRD outline generator in (score 84 -> 92).** PRD template is 2,900 a month at difficulty 6; page one for 'prd generator' is AI apps and forum threads. It was held back as template-shaped, but the check makes it the strongest page in the set. Ship it with the PRD template page.
- **NPS calculator in (78 -> 86).** The only tool head with real volume in all three countries and a beatable page one. CSAT and CES fold in as a tab ('csat calculator' 590 at difficulty 0).
- **Survey question checker in (74 -> 86).** Product survey questions 1,600 at difficulty 8; page one is AI survey makers only.
- **Delivery forecast out (84 -> 80).** No search for the tool itself. Still a strong reader tool; it opens the second half of the drip.
- **Survey sample size and margin of error out (82 -> 78).** The head stays at difficulty 39 with SurveyMonkey twice on page one, and the margin of error phrases came back empty.
- **Usability test sample size out (86 -> 74).** The calculator phrases are 10 a month; the answer can be a section on the SUS page.

Kept despite little search: SUS score calculator and sprint capacity calculator (intent dropped to 1, openness 5, usefulness 5). They are the repeat-use tools for researchers and scrum teams and build authority more than traffic. If you want search to weigh more, the next in line are the tint and shade generator, A/B test planner and positioning statement builder (all 84).

## The drip, re-ranked

| # | Tool | Lead phrase (US vol, KD) | Best measured tool phrase | US | UK | CA | KD | Page one (top 10, US) | Score | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Tint and shade scale generator | tint and shade generator (590, KD 6) | tint and shade generator | 590 | 140 | 90 | 6 | 3 SaaS calculator or content, 2 thin calculator site, 3 forum or UGC; top three toolbox-kit.com, tumblr.com, prototypr.io | 76 -> 84 | Drip. Open niche; palette head out of reach. |
| 2 | A/B test sample size and duration planner | power analysis sample size calculator (880, KD 7) | ab test duration calculator | 20 | 10 | 10 | 46 | not pulled | 72 -> 84 | Drip. Store demand holds; tool phrase small. |
| 3 | Positioning statement builder | positioning statement examples (1,300, KD 5) | positioning statement examples | 1,300 | 210 | 140 | 5 | 1 big product, 4 SaaS calculator or content, 1 editorial, 2 forum or UGC; top three professional.dce.harvard.edu, mailchimp.com, productmarketingalliance.com | 80 -> 84 | Drip. Examples page with a builder. |
| 4 | Palette contrast checker | color contrast checker (12,100, KD 56) | color contrast checker | 12,100 | 2,400 | 1,600 | 56 | 1 big product, 6 SaaS calculator or content, 1 thin calculator site, 1 editorial; top three webaim.org, coolors.co, colourcontrast.cc | 78 -> 82 | Drip, first reserve. Big demand, hard page one. |
| 5 | Delivery forecast (velocity range and Monte Carlo) | sprint velocity calculator (50, KD 0) | sprint velocity calculator | 50 | 10 | 10 | 0 | 1 SaaS calculator or content, 3 editorial, 4 forum or UGC; top three dl.acm.org, reddit.com, 55degrees.se | 84 -> 80 | Out of launch. Strong tool, no search. |
| 6 | Release notes formatter | release notes template (720, KD 2) | release notes template | 720 | - | - | 2 | not pulled | 68 -> 80 | Drip (promoted). Easy template phrase. |
| 7 | Survey sample size and margin of error calculator | sample size calculator (8,100, KD 39) | no measured phrase with data |  | - | - | n/a | 2 big product, 5 SaaS calculator or content, 1 thin calculator site, 1 forum or UGC; top three npscalculator.com, surveymonkey.com, surveysparrow.com | 82 -> 78 | Out of launch. Head crowded, tail empty. |
| 8 | Cycle time and lead time calculator | cycle time calculator (390, KD 0) | lead time vs cycle time | 720 | - | - | 0 | not pulled | 70 -> 78 | Drip (promoted). Pairs with the forecast. |
| 9 | Runway calculator | burn rate calculator (590, KD 3) | burn rate calculator | 590 | - | - | 3 | not pulled | 66 -> 78 | Drip (promoted). Founder page, easy phrase. |
| 10 | Stakeholder map | stakeholder map template (1,300, KD 3) | stakeholder mapping | 4,400 | - | - | 7 | not pulled | 62 -> 78 | Drip (promoted). Big, easy template demand. |

Four later ideas rose into the drip on easy template phrases: release notes formatter, cycle time and lead time calculator, runway calculator, stakeholder map. Four drip ideas fell to later: microcopy length checker, unit economics (LTV, CAC, payback), spacing scale and token export, and the usability test sample size calculator.

## Stronger than guessed

- NPS calculator: 8,100 US, 5,400 UK, 720 CA at KD 16 (guessed 3 for intent, now 5).
- Survey question checker: product survey questions 1,600 at KD 8 (intent 2 -> 4).
- PRD outline generator: page one is AI apps, not templates; openness 3 -> 5.
- Stakeholder map: stakeholder mapping 4,400 at KD 7, stakeholder map template 1,300 at KD 3 (score 62 -> 78).
- Release notes formatter: release notes template 720 at KD 2 (68 -> 80).
- Runway calculator: burn rate calculator 590 at KD 3 (66 -> 78).
- Cycle time calculator: lead time vs cycle time 720 and cycle time calculator 390, both KD 0 (70 -> 78).
- Tint and shade generator: 590 at KD 6, thin page one (openness 3 -> 5).
- Also up but not moved: MoSCoW (moscow method 4,400 at KD 16; stays a mode of the prioritization scorer), CSAT (csat calculator 590 at KD 0; a tab of the NPS calculator), RACI (raci chart template 3,600 at KD 9), Likert scale examples (4,400 at KD 21), CSS grid generator (3,600 at KD 14), px to rem (2,900 at KD 3; a mode of the type scale generator).

## Weaker than guessed

- SUS score calculator: 50 a month (intent 3 -> 1). Page one as open as thought.
- Sprint capacity calculator: 30 a month; capacity planning scrum 140 (intent 2 -> 1).
- Delivery forecast: no data for the Monte Carlo and release forecast phrases; sprint velocity calculator 50.
- Usability test sample size: 10 a month for each calculator phrase (score 86 -> 74).
- Survey sample size and margin of error: margin of error phrases empty; head at KD 39 (openness 2 -> 1).
- Microcopy length checker: no demand; page one is forum threads (80 -> 76).
- Spacing scale and token export: 10 to 20 a month per phrase (78 -> 70).
- Unit economics: customer lifetime value calculator 2,400, but Salesforce and Wall Street Prep hold page one (openness 3 -> 2).
- Palette contrast checker: huge demand, closed page one (openness 2 -> 1); score still up, 78 -> 82, on demand.

## Spend

| Call | What | Cost |
|---|---|---|
| Google Ads search volume, US, standard | 198 phrases, 1 task | $0.060 |
| Google Ads search volume, UK and Canada, standard | 69 phrases each, 2 tasks | $0.120 |
| Labs bulk keyword difficulty, US | 198 phrases | $0.036 |
| Google organic page one, US, standard | 17 phrases (2 reused) | $0.010 |
| **Total** | balance $20.11752 -> $19.89156 | **$0.226** |
