# Section trees v1: Links, Books, Tools, Templates (draft, 8 Oct 2026)

A first proposal for the category tree of each non-article section, built from Phase 3 demand, the free stock
inventories and the Phase 0 page-one holders. Factual draft; the owner decides.

## How to read the numbers

Sources, abbreviated in brackets after each number:

- [SC] `research/seo/keywords/section-candidates-2026-10-08.csv`: Phase 3 keyword suggestions for 17 section seeds
  (US, volume >= 100), clustered; a first-level category needs 10 or more keywords, a second-level one 5 or more.
- [HS] `research/seo/keywords/harvest-sections-2026-10-08.csv`: the same harvest, keyword level (used for groups
  under the threshold).
- [HA] `research/seo/keywords/harvest-articles-combined-2026-10-08.csv`: the Phase 1/1b Articles harvest; it holds
  some template, tool and book phrases the section seeds missed (phrase match is narrow).
- [ST] `research/seo/competitors/stock-by-section-2026-10-08.csv`: entries listed by competitors (GitHub awesome
  list headings with entry counts; sitemap path counts; category page names, which carry no count).
- [P0] `research/seo/competitors/<section>-competitors.csv`: Phase 0 page-one holders (count of page-one results
  across the section's 12 to 16 head queries; organic_etv and tier from Phase 2).

Demand = adjusted volume (each distinct volume and 12-month series counted once, because word-order variants share
one figure), keyword count, median keyword difficulty (KD, 0 to 100). Score for build order = adjusted volume x
(100 - median KD) / 100 ("demand times softness"). KD 0 on most book keywords means no difficulty data, not an
easy keyword. Off-scope groups (other meanings of the seed phrase) are left out of the trees and listed per section.

---

## Links

### Proposed tree

1. **UX and UI design tools**: adjusted 2,910, 19 keywords, KD 19 [SC]
   - Prototyping tools: adjusted 1,160, 17 keywords, KD 26 [SC] (kept as a separate first-level category in the
     data; proposed here as a child)
   - Wireframing and user flow tools: no Phase 3 demand measured; stock only
   - AI design tools: "ai tools for ux design" 110, "ai prototyping tools" 260 [HS]
2. **Product management tools**: adjusted 2,400, 10 keywords, KD 8 [SC]
   - Roadmap tools: "roadmap tools" 390 (KD 28), "product roadmap tools" 210 (KD 16) [HS]
   - Product analytics tools: "product analytics tools" 390 (KD 17) [HS]; analytics tools in general adjusted 9,890,
     KD 27 [HA]
   - AI tools for product managers: "ai tools for product management" 390 (KD 7) [HS]
   - Adjacent, larger and harder: project management tools adjusted 40,050, KD 36; agile, kanban and lean tools
     3,100, KD 12; requirements management tools 590, KD 8 [HA]
3. **UX research and testing tools**: adjusted 650, 4 keywords, KD 10 (below threshold) [HS]; survey tools adjusted
   5,200 but KD 80 [HA]
4. **Design resources**: adjusted 1,330, 9 keywords, KD 23 (below threshold) [HS]
   - Second level from stock only (no demand pulled): icons, colors, typography and fonts, stock photos and video,
     illustrations, design inspiration, design systems and UI kits, mockups

### Stock (entries listed by competitors) [ST]

| Category | GitHub awesome lists (headings: entries) | Directories (category pages named in sitemaps) |
|---|---|---|
| UX and UI design tools | UI Design Tools 20; Online Design Tools 96; Prototyping Tools 21; Prototyping 18; Wireframing Tools 10; User Flow Tools 15; Mockup Tools 32; Collaboration Tools 33 | bookmarks.design: design-tools, prototyping-tools, wireframing-tools, collaboration-tools; designresourc.es: Design Tools, Prototyping Tools, Wireframing, ai-tools-for-designers; startupstash: ui-ux-designing-software, wireframe-software |
| Product management tools | Product Strategy & Planning 30; Roadmaps, Planning, and Prioritization 22; Analytics 13; Product analytics 6; Product Roadmapping & Feedback 4; Product tours & onboarding 4 | startupstash: product-management-software, analytics, web-and-mobile-analytics-software, product-demo |
| UX research and testing tools | User Research Tools 21; User Testing 19; User Interview 8; In-app surveys 6; Research Synthesis 5; Research Plan 4; Research repository 3; User recruitment 3 | startupstash: user-testing-software, survey-and-feedback-software, ab-testing-software; designresourc.es: research-synthesis |
| Design resources | Design Systems 151; Colors 91; Design Inspiration 78; Icons 71; UI Components & Kits 68; Fonts 46; Stock Photos 40; Typography 32 | bookmarks.design: icons, colors, typography, illustrations, stock-photos, ui-resources, design-systems, inspiration (32 category pages); designresourc.es: Icons, Color, Typography, Illustrations, Stock Photos, Inspiration |

Directory sizes [ST]: bookmarks.design 696 entry URLs under /product/; designresourc.es 342 under /resources/;
startupstash.com 2,259 under /tools/ (200 categories, 29 relevant ones kept); uxtools.co 9 under /tools/;
toools.design about 20 single list pages.

### Page-one holders [P0]

reddit.com 13 (of 16 queries); youtube.com 3; toools.design 2 (D); cufonfonts.com 2 (C, 30,640); figma.com 2 (A);
atlassian.com 2 (B); medium.com 2; freedesignresources.net 2 (D); maze.co 2 (D); fontawesome.com 2 (B, 111,339);
then one each: designresourc.es, uxplanet.org, productschool.com, miro.com, userpilot.com, amplitude.com,
productplan.com, dovetail.com, pendo.io. Reddit owns this section's page one; directories barely appear.

### Suggested build order (score)

1. UX and UI design tools, 2,357
2. Product management tools, 2,208
3. Design resources, 1,024
4. Prototyping tools, 858
5. UX research and testing tools, 585

### Off-scope groups [SC, HS]

Design resources with other meanings (Power Design, Design Resources Inc, Apple design resources, interior and human
resources design): 7 keywords. Product lifecycle and product information management software: 2 keywords.

### Open questions

- Demand per Links category is small (the three qualifying categories total about 6,500 adjusted); is Links a
  traffic section or an authority and return-visit section?
- Include general project management and analytics tools (large, harder demand [HA]) or stay on product and UX tools?
- Design resources (icons, fonts, colors) is where stock is deepest, and where fontawesome.com and cufonfonts.com
  already hold page one; in scope for a UX and product site?
- AI tools: a category now, or a tag across categories?

---

## Books

### Proposed tree

1. **Product management books**: adjusted 980, 14 keywords, KD 0 (no data) [SC]
   - Second level candidates from Phase 0 queries (no Phase 3 volume): business books for product managers,
     leadership books for product managers, product strategy books, agile books [P0]
   - OKR books 390, jobs to be done books 140 [HA]
2. **UX design books**: adjusted 530, 21 keywords, KD 0 [SC]
   - Second level candidates from Phase 0 queries: ux research books, behavioral psychology books for designers [P0]
3. **Design books (general)**: adjusted 4,090, 16 keywords, KD 0 [SC]. Part of this series is the other meaning
   ("design of books", "books on book design" share the 2,400 series with "books about design"), so the real
   figure is lower.
   - Graphic and visual design books: adjusted 1,690, 26 keywords, KD 0 [SC]
   - Design thinking books: 390, 4 keywords [HS]; 8 keywords in [HA], same 390 series
   - Game and character design books: adjusted 710, 9 keywords (below threshold) [HS]

### Stock [ST]

| Source | Relevant entries |
|---|---|
| GitHub awesome lists | Books 34 (4 lists); Book 14 |
| fivebooks.com (2,346 best-books lists) | lists mentioning: design 5, business 10, psychology 15, management 3, product 1, leadership 3, data 4, economics 25 |
| mostrecommendedbooks.com (1,344 lists, 1,121 people) | lists mentioning: design 12, management 12, psychology 12, business 10, marketing 9, data 6, product 3 |
| lennysnewsletter.com (1,269 posts) | posts with "book" in the URL: 16 |
| Directories | bookmarks.design category "books"; designresourc.es "Books"; toools.design "books-for-designers" |

### Page-one holders [P0]

reddit.com 11 (of 12 queries); amazon.com 11; productplan.com 4 (C, 20,541); quora.com 4; bringthedonuts.com 3 (D);
rysullivan.medium.com 3; userflow.com 3 (D); goodreads.com 3 (A, 10,251,469); youtube.com 3; then 2 each:
linkedin.com, johannesippen.com, medium.com, uxplanet.org, blog.uxfol.io, productmanagementexercises.com, nextleap.app.
Phase 0 marked 7 of the 12 book queries as a weak page one (three or more forum, social or Medium results).

### Suggested build order (score; KD is missing, so score = adjusted volume)

1. Product management books, 980 (on-brand, weak page one)
2. UX design books, 530 (on-brand, weak page one)
3. Graphic and visual design books, 1,690 (larger, less on-brand)
4. Design books (general), up to 4,090 (mixed meaning)
5. Design thinking books, 390

### Off-scope groups [SC]

Book cover and layout design: 21 keywords, adjusted 15,360. Engineering and software design (system design,
domain-driven design, mechanical): 16, 7,490. Interior, home and architecture: 31, 7,060. Fashion and craft: 22,
5,440. Together about 35,350 adjusted, far above the on-brand groups.

### Open questions

- "design books" demand is mostly other design fields; does the Books section cover graphic and visual design?
- Book pages per book, per list ("best product management books"), or both? Demand sits on the list phrases.
- Phase 0 sub-themes (leadership, business, strategy, psychology for PMs) had page-one SERPs but no Phase 3 volume
  pull; worth a volume check before they become categories.

---

## Templates

### Proposed tree

1. **Product management templates**
   - User story templates: adjusted 11,150, 26 keywords, KD 13 [SC]
     - Agile and scrum user story templates: adjusted 3,180, 12 keywords, KD 13 [SC]
     - Formats (Word, doc, card): adjusted 1,500, 5 keywords, KD 11 [SC]
   - PRD templates: adjusted 2,900, KD 6 (3 keywords) [HS]; the same 2,900 series in [HA] with 4 keywords, KD 8.5
   - Product roadmap templates: adjusted 1,250, 14 keywords, KD 7.5 [SC]; PowerPoint variants 140 [SC]
   - OKR templates: adjusted 1,130, 4 keywords, KD 7.5 [HA]
2. **UX templates**
   - Accessibility conformance (VPAT) template: "voluntary product accessibility template" 5,400, KD 23 [HA]
   - Customer journey map templates: adjusted 1,980, 6 keywords, KD 19 [HA]
   - User persona templates: 1,600, KD 22 (1 keyword) [HS]
   - Usability testing templates and checklists: 140 [HA]; ux research plan and interview script templates have
     Phase 0 SERPs but no volume pulled [P0]
   - Prioritization templates (MoSCoW, matrix): in [HA] "other" group, small

### Stock [ST]

| Source | Template pages | By topic (URL mentions) |
|---|---|---|
| mural.co | 465 under /templates/ | canvas 18, retro 16, workshop 13, brainstorm 10, sprint 9, prioritization 9, strategy 8, persona 7, journey 7, interview 6, discovery 6, stakeholder 6, roadmap 4, okr 3 |
| aha.io | 163 under /roadmapping/, 40 blog, 36 support | roadmap 194, sprint 8, requirement 7, strategy 7, swot 4, research 4, launch 4, persona 3 |
| maze.co | 68 under /templates/ | survey 8, feedback 7, usability 6 |
| dovetail.com | 12 | research 6 (research report, research plan, persona) |
| productboard.com | 8 | spec, discovery, launch, strategy 1 each |
| nngroup.com | 7 articles and videos | journey map 1, service blueprint 1, free UX templates 1 |
| GitHub awesome lists | | Sample Product Documentation 13; Templates 8; Research Plan 4 |

### Page-one holders [P0]

notion.com 9 (of 14 queries; B, 320,481); figma.com 4 (A); atlassian.com 4 (B); clickup.com 4 (B); scribd.com 4;
pinterest.com 4; youtube.com 3; creately.com 3 (C); then 2 each: miro.com (B), mural.co (C), nngroup.com (C),
smartsheet.com (B), okrinstitute.org, ones.com, dhavalthakur.medium.com, reddit.com, gist.github.com.
Phase 0 marked only "prd template" as a weak page one.

### Suggested build order (score)

1. User story templates, 9,700
2. VPAT template, 4,158
3. PRD templates, 2,726
4. Customer journey map templates, 1,604
5. User persona templates, 1,248
6. Product roadmap templates, 1,156
7. OKR templates, 1,045

### Open questions

- The template SERPs are held by B-tier tool vendors (Notion, Atlassian, ClickUp, Smartsheet) that offer the
  template inside their product; is our format a downloadable file (Docs, Sheets, Figma, Notion duplicate) or an
  article with an embedded template?
- VPAT is a compliance document; in scope?
- Seeds "prd template" and "user persona template" returned 3 and 1 rows (phrase match); journey map, OKR,
  research plan and interview script templates were not seeded. A second small seed batch would size them.

---

## Tools (our calculators and small utilities)

### Proposed tree

1. **Experimentation calculators**
   - Sample size calculator: adjusted 14,990, 68 keywords, KD 37.5 [SC]
     - Power analysis: adjusted 2,390, 24 keywords, KD 18 [SC]
     - Survey sample size: adjusted 2,140, 13 keywords, KD 25 [SC] (several are tool names: SurveyMonkey,
       Raosoft, Qualtrics)
     - Statistical significance: adjusted 650, 14 keywords, KD 43 [SC]
   - A/B test calculator (significance and sample size): adjusted 620, 8 keywords, KD 43 (below threshold) [HS];
     the same series in [HA] at KD 37
2. **Prioritization calculators**
   - RICE: "rice score" 1,900, KD 4 [HS], but the phrase is ambiguous (see below); ICE and priority matrix have
     Phase 0 SERPs, no volume pulled [P0]
3. **Product and SaaS metrics calculators**
   - Retention rate calculator: adjusted 560, 3 keywords, KD 16 [HA]; churn rate and CAC calculators have Phase 0
     SERPs, no volume pulled [P0]
4. **UX metrics and agile calculators**: SUS score and sprint velocity calculators have Phase 0 SERPs, no volume
   pulled [P0]

### Product meanings versus other meanings (by inspection of [HS])

| Meaning | Keywords | Adjusted volume | Product-related |
|---|---|---|---|
| Sample size calculators (general, power, survey, significance) | 68 | 14,990 | yes |
| A/B test calculators | 8 | 620 | yes |
| "rice score" (the bare phrase) | 1 | 1,900 | ambiguous: likely mixed with the purity test and sports; a RICE tool should target "rice prioritization", "rice framework", "rice calculator" |
| Rice purity test (score meanings, averages by age) | 23 | 74,330 | no |
| Rice University football, basketball and baseball scores; Brother Rice high school football | 11 | 2,950 | no |
| Rice University SAT and ACT scores | 7 | 1,340 | no |
| Jerry Rice score card | 3 | 490 | no |

No cooking (rice), medical (ICE) or mortgage meanings surfaced, because the seeds were "rice score", "sample size
calculator" and "ab test calculator"; "ice score" was not seeded.

### Stock

No Tools inventory was pulled in Phase 3c. From [P0], the calculator holders are evanmiller.org (D, 1,640),
abtestguide.com (D, 2,077), optimizely.com (C), statsig.com (C), cxl.com (D), omnicalculator.com (A), behindthecmo.com.

### Page-one holders [P0]

youtube.com 4 (of 12 queries); behindthecmo.com 2 (D); wallstreetprep.com 2 (B, 200,075); reddit.com 2;
omnicalculator.com 2 (A, 11,060,954); then one each: nngroup.com, optimizely.com, amplitude.com, evanmiller.org,
mountaingoatsoftware.com, atlassian.com, statsig.com, abtestguide.com, cxl.com, scrum.org. Phase 0 found no weak
page one in Tools.

### Suggested build order (score)

1. Sample size calculator, 9,369 (with power analysis 1,960 and survey 1,605 as modes or child pages)
2. RICE calculator, up to 1,824 if "rice score" intent is product (unverified)
3. Retention rate calculator, 470
4. A/B test calculator, 353

### Open questions

- One sample size calculator with modes (A/B, survey, power) or separate pages per intent?
- A SERP check for "rice score", "rice calculator" and "ice score" before building a prioritization calculator.
- Volume for churn, CAC, LTV, SUS and sprint velocity calculators was not pulled; a small seed batch would size them.
