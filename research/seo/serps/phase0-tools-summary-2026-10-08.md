# Phase 0 SERP pass: Tools section (2026-10-08)

Google US, desktop, depth 10, standard queue. 12 keywords posted, 12 collected, 0 pending.

Files:
- `research/seo/serps/page-one-2026-10-08-tools.csv` (100 organic rows; no featured snippets)
- `research/seo/serps/features-2026-10-08-tools.csv` (one row per keyword)
- `research/seo/cache/index-staging-serps-tools.csv` (261008-ST-001 to 012)
- raw: `research/seo/cache/raw/serps-2026-10-08/<slug>.json`

Keywords: rice calculator, sample size calculator ab test, ab test significance calculator, sus score
calculator, nps calculator, churn rate calculator, ltv calculator, cac calculator, sprint velocity
calculator, ice score calculator, retention rate calculator, priority matrix tool.

## Headline numbers

- AI Overview: 12 of 12. Two of them (sprint velocity calculator, priority matrix tool) were
  asynchronous, so the content and references were not captured.
- Weak page one (weak_count of 3 or more): 0 of 12. Highest is 2 (priority matrix tool:
  reddit, youtube). Seven keywords have exactly one weak result.
- Featured snippet: 0. Knowledge graph: 0. Shopping: 0. No Google-native calculator widget appears
  on any of the 12 (the response has no such item type). Instead, the AI Overview ends with an offer
  to do the math itself ("share your numbers and I can calculate..."), on 7 of the 10 overviews
  that loaded. That is the real competitor for a single-formula calculator.
- 93 distinct domains across 100 organic results: page one is extremely fragmented, no domain
  dominates the set.

## Top 20 domains on page one (count, type)

Only five domains appear more than once; positions 6 to 20 are single appearances, listed in the
order they first appear, so treat them as examples rather than a ranking.

| # | Domain | Count | Type |
|---|---|---|---|
| 1 | youtube.com | 4 | publication |
| 2 | behindthecmo.com | 2 | calculator |
| 3 | omnicalculator.com | 2 | calculator |
| 4 | wallstreetprep.com | 2 | publication |
| 5 | reddit.com | 2 | publication |
| 6 | miniwebtool.com | 1 | calculator |
| 7 | chefsbinge.com | 1 | publication |
| 8 | 247sports.com | 1 | publication |
| 9 | collegesimply.com | 1 | publication |
| 10 | shutterstock.com | 1 | template |
| 11 | collegevine.com | 1 | publication |
| 12 | rice.co.nz | 1 | publication |
| 13 | makemysushi.com | 1 | publication |
| 14 | optimizely.com | 1 | SaaS |
| 15 | evanmiller.org | 1 | calculator |
| 16 | statsig.com | 1 | SaaS |
| 17 | abtestguide.com | 1 | calculator |
| 18 | wingify.com | 1 | SaaS |
| 19 | clincalc.com | 1 | calculator |
| 20 | cxl.com | 1 | publication |

Type key: SaaS = SaaS vendor using a free tool as lead magnet; calculator = independent calculator
site; publication = editorial, forum or video; template = template or asset gallery (shutterstock
is a stock-image library, the closest fit).

Beyond the top 20, the pattern in the CSV is clear: most page-one calculators are SaaS lead magnets
(yotpo, mailmodo, amplitude, tremendous, compt, churnkey, easyretro, mountaingoatsoftware,
atlassian, surveymonkey, convertize, formbricks, elementor) plus a long tail of thin, recent
single-purpose calculator sites (mcpcalc, calculatordad, rkcalculator, induwara.lk, upgrowth.in,
tools.hackingdemand.com, parrotnotes.app), several dated 2026. That tail is the beatable layer.

## Anything odd

- Ambiguous head terms. Four of the twelve SERPs are mostly about something else:
  - "rice calculator": rice-to-water ratios, Rice University admissions and sports. The RICE
    prioritization intent shows only in the image pack (easyretro, userpilot, fluentsupport).
  - "ice score calculator": medical (ICANS / CAR-T neurotoxicity). The AI Overview asks the user
    which meaning they want and links one product tool (experimentos.io).
  - "ltv calculator": loan-to-value (mortgages), not lifetime value. Every organic result is finance.
  - "nps calculator": split with India's National Pension System (samco, bajajfinservmarkets,
    svacron, x.com/nps_trust). "cac calculator" also leaks into coronary calcium scoring
    (cac-tools.com at #2).
  Product-intent variants ("rice score calculator", "ice prioritization calculator", "customer
  lifetime value calculator", "net promoter score calculator") should be checked before building.
- "priority matrix tool" is a brand SERP: Priority Matrix (appfluence) owns the Microsoft
  Marketplace listing, webcatalog, its own blog and the video pack.
- "sus score calculator": NN/g ranks #1 with an article, not a calculator; page one has only one or
  two real calculators (usability.uno, uiuxtrend cited in the AI Overview). Looks like the most
  open UX-side tool.
- "sample size calculator ab test" and "ab test significance calculator" are crowded with
  established tools (Optimizely, Evan Miller, Statsig, CXL, ABTestGuide, Convertize).
- The only weak hit from the vendor-blog rule is amplitude.com/blog on "churn rate calculator".
- uk.surveymonkey.com ranks #1 for "nps calculator" with a tracking-parameter URL and no snippet
  (blocked description).
