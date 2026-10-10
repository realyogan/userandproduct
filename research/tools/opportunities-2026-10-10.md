# Tool opportunities for userandproduct.com (2026-10-10)

The owner's goal (10 October 2026): at least ten working tools at launch, plain JavaScript, no dependencies, each a real page that says what it is, when to use it and how. Tools must be useful to the people the site serves, so they come back; the search demand must be real as well. This file is the research behind that choice. Rescored on October 10 after the paid check (US volumes, UK and Canada for the shortlist, difficulty, 19 page ones; $0.226): see `research/tools/seo-check-summary-2026-10-10.md`. Before that check every number came from the keyword store in `research/seo/keywords/`, the October 8 page-one pull for twelve calculator phrases (`research/seo/serps/phase0-tools-summary-2026-10-08.md`) and a free web scan on October 10.

Files: `research/tools/opportunities-2026-10-10.csv` (one row per idea; `idea_id` is the number in the table below, `rank` the order after the check), `research/tools/paid-check-phrases-2026-10-10.csv` (the phrases for the paid volume check), the board at `research/explainers/tools-opportunities-2026-10-10.html`.

## The short version

- 82 tool ideas, scored on usefulness (repeat use), search intent, openness of page one, fit with the site and build cost. 32 of them have a store volume behind their best phrase; 50 have none yet.
- The launch ten, after the paid check: PRD outline generator; user story and acceptance criteria builder; type scale generator; OKR checker; NPS calculator with margin of error; survey question checker; SUS score calculator; backlog prioritization scorer (RICE, ICE, WSJF); sprint capacity calculator; retention and churn calculator. Three swaps from the first list: the PRD outline generator, the NPS calculator and the survey question checker come in; the delivery forecast and the survey sample size calculator move to the drip, the usability test sample size calculator to later.
- Build effort for the launch ten: about 75 hours of plain JavaScript, before page copy.
- The store is thin on tool phrases. It was built for articles, so most calculator and generator phrases have no volume yet. The tool-intent phrases it does hold are in the user story, PRD, OKR, retention, sample size and positioning families.
- The paid check ran on October 10 ($0.226). The exact tool phrases are small (most 10 to 110 searches a month); the demand sits on template, example and formula phrases. One real tool head turned up: NPS calculator, 8,100 a month in the US, 5,400 in the UK, at difficulty 16. Details in `research/tools/seo-check-summary-2026-10-10.md`.
- The October 8 page-one pull already showed the shape: an AI Overview on 12 of 12 calculator searches, offering to do the maths itself; no Google calculator widget; page one fragmented (93 domains in 100 results), mostly SaaS lead magnets and thin new calculator sites. A single-formula calculator loses to the AI Overview. Tools that take a pasted list, draw a chart or export to Jira and Figma do not.

## What a tool page must be

The search-policy rulebook (sections 1, 4 and 12) applies: a tool page counts as main content only when the tool works and the page explains when and how to use it. Each tool page here has the tool at the top, working without sign-up; then what it is, when to use it and when not to, how it works (the formula, shown), a worked example with real numbers, what to do with the result, and links to the articles in its category. The page loads fast (Core Web Vitals in mind), works on a phone, and nothing covers the tool. No tool sends queries to Google.

## 1. Personas and their recurring small jobs

**Product manager.** Owns the why and the what; lives between research, design, engineering and the business.

- Ranking a long list of ideas before quarterly planning
- Writing OKRs and checking they are outcomes, not tasks
- Starting a PRD for a new initiative
- Telling a stakeholder when a feature will ship, with a range
- Reading an A/B test result before the review meeting
- Working out the retention or churn number for a monthly review
- Turning a list of tickets into release notes
- Putting a cost on a recurring meeting to argue it away
- Placing stakeholders on a power and interest grid at kick-off

**Product owner.** Runs the backlog with the team, story by story.

- Writing user stories with acceptance criteria several times a week
- Sorting a release scope into Must, Should, Could and Won't
- Converting a backlog in points into sprints and dates
- Checking a story against INVEST before refinement
- Turning acceptance criteria into a test list for QA
- Preparing capacity for sprint planning with the scrum master

**Product designer.** Designs the flows and screens and tests them with people.

- Deciding how many people to recruit for a usability test
- Scoring a SUS questionnaire after the test
- Building a type scale for a new product
- Checking a palette for contrast before handoff
- Checking tap targets on a mobile design
- Writing a proto-persona for a kick-off workshop
- Listing every component state before handoff
- Laying out a journey map for a workshop

**UI designer.** Owns the visual layer: type, color, spacing, grids.

- Making a 50 to 950 color ramp from a brand color
- Setting fluid type sizes with clamp() for the developers
- Working out column widths and gutters for each breakpoint
- Setting the text column width for 45 to 75 characters per line
- Snapping line heights to a 4px grid
- Picking icon sizes and stroke weights
- Converting px to rem for a hand-off table

**UX researcher.** Plans studies, runs sessions, turns notes into findings.

- Sizing a survey and reporting its margin of error
- Scoring SUS and placing it against the 68 average
- Checking survey questions for leading or double-barreled wording
- Writing an interview guide timed to a 45-minute session
- Reporting task completion rates with honest error bars
- Picking labels for a Likert scale
- Grouping interview notes for synthesis
- Setting a fair participant incentive
- Turning a vague ask into research questions

**UX writer.** Writes the words in the interface: labels, errors, empty states, help.

- Checking button labels and toasts against length limits
- Writing an error message that says what to do next
- Estimating how much a string grows in translation
- Checking help text for reading level
- Deciding what alt text an image needs

**Design system lead.** Keeps the shared components, tokens and rules in shape.

- Exporting a spacing scale as tokens
- Naming tokens in a tiered pattern and finding the odd ones out
- Producing a type scale as CSS variables and JSON
- Checking the whole palette for contrast pairs
- Making color ramps with contrast labels for each step

**Accessibility specialist.** Makes sure the product works for everyone, and can prove it.

- Checking every text and background pair against WCAG
- Testing focus order and keyboard traps with a checklist
- Checking target sizes against WCAG 2.2
- Advising on alt text for charts and screenshots
- Logging issues with severity for a review

**Scrum master or delivery lead.** Runs the team's rhythm and protects its flow.

- Working out sprint capacity with days off and meetings
- Forecasting a release date from past velocity
- Setting a WIP limit and seeing the effect on cycle time
- Pulling cycle-time percentiles from a Jira export
- Picking a retro format for a tired team
- Drawing a burn-down for a team without tooling
- Turning three-point guesses into a range

**Product analyst.** Turns data into answers for the product team.

- Building retention curves from a cohort table
- Checking a finished A/B test for significance and sample-ratio problems
- Sizing an A/B test before it starts
- Writing a metric definition everyone reads the same way
- Computing DAU/MAU stickiness
- Computing cycle-time percentiles for the delivery review

**Growth or pricing lead.** Owns acquisition, conversion, monetization and price.

- Computing LTV, CAC and payback for a channel review
- Finding the biggest drop in a funnel
- Planning test duration from daily traffic
- Reading a Van Westendorp price survey
- Sketching good, better, best tiers
- Modelling free-to-paid conversion for a revenue target
- Checking what volume a discount needs to break even

**Product marketer.** Positions the product and launches it.

- Writing a positioning statement
- Building a launch checklist for the launch tier
- Filling a value proposition canvas
- Computing NPS and whether a change is real
- Laying out a competitive feature matrix
- Checking a pricing page draft

**Founder.** Does all of the above, plus keeps the company alive.

- Checking runway and the zero-cash month
- Computing unit economics for a board deck
- Cutting an MVP to what tests the riskiest assumption
- Sizing the market bottom up for a pitch
- Computing MRR movements and ARR
- Writing a mission and vision
- Ranking the next bets

**Engineering manager who works with product.** Runs the engineers and shares planning with product.

- Working out team capacity for the quarter
- Forecasting delivery with a range, not a date
- Putting a cost on a recurring meeting
- Writing team OKRs
- Turning merged work into release notes
- Building a RACI for a cross-team project

## 2. What the keyword store holds

The store was grepped for calculator, generator, template, checker, converter, estimator, planner, maker, builder, formula, "how to calculate", tool, score, canvas and the metric and method names (RICE, OKR, NPS, retention, churn, LTV, CAC, story points, WIP and more) across every CSV in `research/seo/keywords/`.

- 1,592 distinct phrases matched. Most belong to other worlds: AI image generators, website builders, SEO tools, the Rice purity test, Rice University sports.
- The `tools` section harvest (seeds: ab test calculator, rice score, sample size calculator) holds 123 phrases; the sample size family is the only one with real tool volume (8,100 for the head, 880 for the power-analysis family).
- No store data at all for: SUS, NPS, contrast checker, type scale, color palette, tint and shade, line height, aspect ratio, sprint capacity, velocity, burn-down, cycle time, meeting cost, runway, Kano, WSJF calculator, cost of delay, Van Westendorp, readability, alt text, design tokens, spacing, breakpoints. These go to the paid check.
- Intent labels: the store's fine intent marks `tool` on the sample size, A/B, persona generator, research question generator, prioritization tool and retention calculator phrases; `template` on the user story, PRD, OKR, roadmap and persona template phrases (a builder answers these); `define` or `learn` on the retention formula, story points, positioning statement and the metric names (these want an article with a calculator inside).

| Phrase | Volume (US) | KD | Intent (store) | Fine intent | Tool it maps to |
|---|---|---|---|---|---|
| mission statement | 22,200 | 37 | informational | define | Mission and vision builder (parked) |
| kpi examples | 14,800 | 43 | informational | template | Metric definition card (article-led) |
| story points | 9,900 | 21 | informational | define | Delivery forecast (definition search) |
| marketing funnel | 9,900 | 45 | commercial | define | Funnel conversion calculator (article-led) |
| sample size calculator | 8,100 | 39 | informational | tool | Survey sample size calculator |
| dashboard design | 5,400 | 24 | commercial | define | Dashboard chart picker (article-led) |
| wcag accessibility | 5,400 | 62 | navigational | define | Focus order checklist (article-led) |
| moscow prioritization | 4,400 | 24 | informational | define | Prioritization scorer (MoSCoW mode) |
| customer lifetime value | 4,400 | 58 | informational | define | Unit economics |
| customer acquisition cost | 4,400 | 34 | commercial | define | Unit economics |
| accessibility checker | 4,400 | 76 | informational | define | None: a site-wide checker needs a server |
| customer satisfaction survey | 4,400 | 21 | informational | define | NPS calculator (CSAT tab) |
| font size accessibility | 3,600 | 13 | informational | define | Type scale generator |
| user story template | 2,900 | 18 | informational | template | User story builder |
| user story format | 2,900 | 21 | informational | template | User story builder |
| prd template | 2,900 | 6 | informational | template | PRD outline generator |
| product requirements document template | 2,900 | 11 | informational | template | PRD outline generator |
| positioning statement | 2,900 | 12 | informational | define | Positioning statement builder |
| high contrast accessibility | 2,900 | 28 | informational | define | Palette contrast checker |
| usability testing | 2,400 | 35 | informational | define | Usability test sample size (article-led) |
| rice score | 1,900 | 4 | informational | define | Prioritization scorer (mixed with the purity test) |
| user persona template | 1,600 | 22 | navigational | template | Proto-persona worksheet |
| user stories examples with acceptance criteria | 1,600 | 20 | informational | template | User story builder |
| acceptance criteria user story template | 1,600 | 10 | informational | template | User story builder |
| retention rate formula | 1,600 | 18 | informational | define | Retention and churn calculator |
| arr formula | 1,600 | 2 | informational | define | MRR and ARR calculator |
| value proposition example | 1,600 | 26 | commercial | template | Value proposition canvas |
| product survey questions | 1,600 | 8 | informational | define | Survey question checker |
| product launch | 1,600 | 27 | informational | define | Launch checklist builder |
| okr examples | 1,300 | 5 | informational | template | OKR checker |
| how to calculate retention rate | 1,300 | 16 | informational | learn | Retention and churn calculator |
| customer journey map template | 1,000 | 19 | navigational | template | Journey map grid builder |
| product roadmap template | 1,000 | 13 | informational | template | Roadmap builder |
| qualitative survey questions | 1,000 | 7 | informational | define | Survey question checker |
| product positioning | 1,000 | 12 | informational | define | Positioning statement builder |
| power analysis sample size calculator | 880 | 7 | informational | tool | A/B test planner; survey sample size |
| grid system in graphic design | 880 | 4 | informational | other | Breakpoint and layout grid calculator |
| rice prioritization | 880 | 31 | informational | define | Prioritization scorer |
| okr template | 880 | 14 | informational | template | OKR checker |
| go to market plan | 880 | 38 | navigational | other | Launch checklist builder |
| importance likert scale | 720 | 14 | informational | define | Likert scale label builder |
| sales funnel stages | 720 | 33 | informational | define | Funnel conversion calculator |
| usability testing questions | 720 | 7 | informational | define | Interview guide builder |
| mvp minimum viable product | 720 | 37 | informational | other | MVP scope cutter |
| a/b testing calculator | 480 | 28 | informational | tool | A/B test planner |
| ab test calculator | 480 | 55 | informational | tool | A/B test planner (significance tab) |
| sample size calculator for survey | 390 | 26 | informational | tool | Survey sample size calculator |
| survey sample size calculator | 390 | 25 | informational | tool | Survey sample size calculator |
| research question generator | 390 | 0 | informational | tool | Research question generator |
| roadmap tools | 390 | 28 | informational | tool | Roadmap builder (vendors hold it) |
| user persona generator | 320 | 19 | informational | tool | Proto-persona worksheet |
| okr tracker | 320 | 19 | navigational | define | OKR checker |
| user persona maker | 260 | 26 | navigational | define | Proto-persona worksheet |
| prioritization matrix template | 260 | 4 | informational | template | Prioritization scorer |
| wsjf prioritization | 210 | 1 | informational | define | Prioritization scorer |
| okr planner | 210 | 7 | navigational | define | OKR checker |
| work in progress formula | 210 | 0 | informational |  | WIP limit calculator |
| customer retention rate calculator | 210 | 25 | informational | tool | Retention and churn calculator |
| net retention rate formula | 210 | 15 | informational | other | Retention and churn calculator |
| tiered pricing strategy | 210 | 19 | informational | define | Price tier builder |
| how to write okr | 170 | 17 | informational | learn | OKR checker |
| smart goal formula | 170 | 63 | informational |  | OKR checker (KD 63, skip) |
| a/b testing sample size calculator | 140 | 31 | informational | tool | A/B test planner |
| prioritization tool | 140 | 5 | informational | tool | Prioritization scorer |
| retention rate calculator | 140 | 9 | informational | tool | Retention and churn calculator |
| cohort retention | 140 | 12 | informational | define | Retention and churn calculator |
| project management stakeholder map | 110 | 26 | informational | other | Stakeholder map |

## 3. The full idea list

Scores are 1 to 5. U = usefulness and repeat use (weight 3), I = search intent (weight 2; measured on October 10, see the rescoring note in section 5), O = openness of page one (weight 2; measured on October 10), F = fit with the site (weight 2), C = build cost, 5 = cheap (weight 1). Score = weighted sum x 2, out of 100. Tier: launch, drip (the second ten), fold (becomes a mode of another tool), later, park.

| # | Tool | Category | Personas | Job | In | Out | Why they come back | Search phrases (store volume) | Hours | Pasteable to | Nearest tool online | Our angle | U | I | O | F | C | Score | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | SUS score calculator | UX research | UX researcher; product designer | Score a System Usability Scale study and say what the number means | Paste the 10 answers per person from a spreadsheet (one row each) | SUS score, grade and percentile against the 68 average, a confidence interval, per-item averages, flags for straight-lined rows | Every usability round ends with a SUS score; teams re-run it each release to compare | sus score calculator; system usability scale calculator; how to calculate sus score (no store data) | 6 | Spreadsheet (paste in, CSV out) | Trymata free SUS calculator; Lyssna Google Sheets template | Paste a whole sheet instead of typing 10 boxes per person; confidence interval and straight-lining check that the free ones skip | 5 | 1 | 5 | 5 | 5 | 84 | launch 7 |
| 2 | User story and acceptance criteria builder | Product discovery | Product owner; product manager; business analyst | Write a user story and its acceptance criteria in a clean, testable format | Who, what, why; then rules and edge cases as short lines | 'As a / I want / so that' story, Given-When-Then criteria, INVEST warnings, copy as Jira markup or markdown | Several times a week for a product owner | user story template (2,900); user story format (2,900); user stories examples with acceptance criteria (1,600); acceptance criteria user story template (1,600) | 8 | Jira markup; markdown; Gherkin | Figr and Kollabe acceptance criteria generators (AI) | No AI, no sign-up: a structured builder with edge-case prompts and INVEST checks, pasted straight into Jira | 5 | 5 | 3 | 5 | 4 | 90 | launch 2 |
| 3 | Backlog prioritization scorer (RICE, ICE, WSJF) | Product strategy | Product manager; product owner; founder | Score and rank a whole list of ideas with RICE, ICE or WSJF, and see the order change as you tweak | Paste a list from a spreadsheet or a Jira export; pick the method | Ranked table, score breakdown, a flag when one shaky guess decides the order, CSV for Jira or Sheets | Every planning cycle and quarterly review | moscow prioritization (4,400); rice score (1,900, mixed meanings); rice prioritization (880); wsjf prioritization (210); prioritization tool (140) | 10 | CSV for Jira, Sheets, Notion | EasyRetro, ProductLift, Kollabe RICE calculators (one item at a time) | A whole backlog, three methods, and a warning when the order hangs on one guess | 5 | 3 | 4 | 5 | 3 | 84 | launch 8 |
| 4 | Sprint capacity calculator | Project management | Scrum master; delivery lead; engineering manager; product owner | Work out how much the team can take on this sprint | People, days in the sprint, days off, meeting hours, focus factor; optional points-per-day history | Hours and points of capacity, per person and total, with a commitment range; a line for the sprint planning notes | Every sprint, every two weeks | sprint capacity calculator (no data) | 6 | Text for Jira or Confluence; CSV | Vendor articles and spreadsheet templates (ONES, Xebia); no standard free tool | Days off per person and a range, not a single number; remembers the team in the browser | 5 | 1 | 5 | 5 | 5 | 84 | launch 9 |
| 5 | Usability test sample size calculator | UX research | UX researcher; product designer; product manager | Decide how many people to test so you see the problems that matter | How common a problem must be before you care (e.g. 1 in 10 users), the share of those problems you want to see, number of user groups | Number of participants, a curve of problems found per added participant, the plan as rounds (e.g. 3 rounds of 5) | Asked at the start of every study and in every budget conversation | usability testing (2,400); how many users for usability testing (no data) | 5 | Text summary for the research plan | MeasuringU tables and articles (no calculator surfaced in the scan) | Turns the 'five users' debate into a slider: shows what five finds and what it misses for rare problems | 4 | 2 | 3 | 5 | 5 | 74 | later |
| 6 | Delivery forecast (velocity range and Monte Carlo) | Project management | Scrum master; delivery lead; product manager; engineering manager | Answer 'when will it be done' with a range instead of a single date | Backlog size, past sprint velocities or weekly throughput, start date | Dates at 50%, 85% and 95% likelihood, a histogram, and a sentence to share with stakeholders | Every release conversation | story points (9,900, a definition search); release forecast (no data) | 10 | Text and PNG for the stakeholder update | Jira marketplace forecasting apps (Monte Carlo is a paid tier); spreadsheets | Free, in the browser, numbers pasted from Jira; the 85% line explained in plain words | 5 | 1 | 5 | 5 | 3 | 80 | drip 5 |
| 7 | Retention and churn calculator | Product metrics | Product analyst; growth lead; product manager; founder | Turn a cohort table into retention curves, churn and net revenue retention | Paste a cohort table (users or revenue by start month and month since start), or three numbers for a quick rate | Retention per cohort as a heatmap and curves, the average curve, churn rate, gross and net revenue retention, CSV | Monthly metrics review and board decks | retention rate formula (1,600); how to calculate retention rate (1,300); customer retention rate calculator (210); net retention rate formula (210); retention rate calculator (140) | 10 | CSV in and out; PNG chart | Founderpath cohort analysis; MetricGate; Amplitude churn calculator | A quick-rate mode for the 'how to calculate' searcher and a cohort mode for the analyst, on one page | 5 | 4 | 3 | 5 | 3 | 84 | launch 10 |
| 8 | PRD outline generator | Product discovery | Product manager; founder | Start a product requirements document with the right sections for the size of the work | Size of change, audience, open questions | A PRD skeleton (problem, goals, non-goals, users, scope, metrics, risks) with prompts; markdown | Every new initiative | prd template (2,900); product requirements document template (2,900) | 6 | Markdown for Notion, Confluence, Google Docs | Template galleries (Notion, Atlassian, Productboard) | Scales the template to the size of the work: one page for small, full for big | 4 | 5 | 5 | 5 | 4 | 92 | launch 1 |
| 9 | Type scale generator | UI design | UI designer; product designer; design system lead; front-end engineer | Build a consistent set of font sizes and line heights from one base and one ratio | Base size, ratio, steps, optional fluid range (min and max screen width) | Sizes in px and rem, line heights snapped to a 4px grid, CSS variables, clamp() values, a Figma text-style table | Every new product, brand refresh or design system change | type scale generator (no data); font size accessibility (3,600) | 8 | CSS variables; JSON tokens; Figma table | typescale.com (Jeremy Church); Utopia fluid type | Static scale, fluid clamp() and snapped line heights on one page, previewed in real interface text | 5 | 3 | 4 | 5 | 4 | 86 | launch 3 |
| 10 | OKR checker | Product metrics | Product manager; engineering manager; founder; growth lead | Check that objectives are qualitative and key results are measurable outcomes, not tasks | Paste objectives and key results | Flags per line (task not outcome, no number, no baseline, too many KRs), a score, rewrite hints; clean copy for Notion or Sheets | Every quarter's OKR setting and review | okr examples (1,300); okr template (880); okr tracker (320); okr planner (210); how to write okr (170) | 8 | Markdown; spreadsheet | goalsandprogress OKR builder; spreadsheet checklists | Rule-based and explained, with an example library by product role | 4 | 4 | 5 | 5 | 3 | 86 | launch 4 |
| 11 | Survey sample size and margin of error calculator | UX research | UX researcher; product manager; product marketer | Find how many responses a survey needs, or how far to trust the responses you have | Population size, confidence level, margin you can live with; or the responses you got and the percentage you saw | Responses needed; margin of error for your result; the range in plain words ('between 55% and 65%') | Every survey, before sending and when reporting | sample size calculator (8,100); power analysis sample size calculator (880); sample size calculator for survey (390); survey sample size calculator (390) | 5 | Text line for the readout | SurveyMonkey and Qualtrics margin of error calculators; Raosoft | Both directions on one page, the result written as a sentence you can paste into a readout | 4 | 5 | 1 | 5 | 5 | 78 | drip 7 |
| 12 | Microcopy length checker | UX design | UX writer; product designer | Check button labels, errors and toasts against length limits and plain-language rules | Paste strings, pick the element type (button, error, toast, tooltip) | Character and word counts against limits; flags for blame words, jargon, passive voice and a missing next step; a translation expansion estimate | Every copy review and localization prep | ux writing (group 4,740; no tool phrase in the store) | 6 | CSV for string files | Hemingway Editor (general prose) | Built for interface strings, not prose: limits per element and translation expansion | 4 | 1 | 5 | 5 | 4 | 76 | later |
| 13 | Positioning statement builder | Product marketing | Product marketer; founder; product manager | Write a positioning statement from the parts that make it up | Target customer, alternatives, unique attributes, value, category | Statements in two forms (the classic 'For... who...' and a component table), checked for vague words | Launches and repositioning | positioning statement (2,900); product positioning (1,000); examples of market positioning (880) | 5 | Markdown; slide text | Miro positioning template; AI skill listings | No standalone builder surfaced in the scan; ours checks for empty words | 3 | 4 | 5 | 5 | 5 | 84 | drip 3 |
| 14 | Palette contrast checker | Accessibility | UI designer; accessibility specialist; design system lead | Check every text and background pair in a palette against WCAG at once, and get the nearest passing color | Paste a palette (hex list or CSS variables) | A pass/fail grid for AA and AAA, normal and large text, APCA as a reference column, a suggested fix for each failing pair | Every palette change and design review | contrast checker (no data); high contrast accessibility (2,900) | 8 | CSS variables in and out | WebAIM contrast checker (one pair at a time); Coolors | The whole palette as a grid instead of one pair at a time, with a fix | 5 | 5 | 1 | 5 | 4 | 82 | drip 4 |
| 15 | NPS calculator with margin of error | Product metrics | Product manager; product marketer; UX researcher | Compute Net Promoter Score and say whether a change between two surveys is real | Counts of 0 to 10 answers, or the raw scores pasted; an optional second survey | NPS, promoter, passive and detractor shares, margin of error, whether the change is beyond noise | Every NPS survey wave | net promoter score calculator; nps calculator (no data) | 5 | Text line; CSV | Hotjar, QuestionPro, Youform NPS calculators | The margin of error and the 'is this change real' check that vendor calculators skip | 4 | 5 | 3 | 5 | 5 | 86 | launch 5 |
| 16 | Spacing scale and token export | Design systems | Design system lead; UI designer; front-end engineer | Pick a spacing scale and export it as tokens | Base unit (4 or 8), scale type (linear, ratio, t-shirt), names | Spacing tokens with names, CSS variables, JSON in the W3C token format, a visual ruler | Design system setup and audits | spacing scale; design tokens (no data) | 5 | CSS variables; JSON tokens | figr.design spacing generator; bushe.co | Naming advice and the W3C token format built in | 4 | 1 | 3 | 5 | 5 | 70 | later |
| 17 | Unit economics: LTV, CAC and payback | Growth and pricing | Founder; growth lead; product manager | See whether each customer pays back what it cost to win | Revenue per account, gross margin, monthly churn, sales and marketing spend, new customers | LTV, CAC, LTV:CAC ratio, payback months, and a warning when inputs mix monthly and yearly | Board prep, pricing changes, channel reviews | customer lifetime value (4,400); customer acquisition cost (4,400) | 5 | Text; CSV | Founderpath, xgenious, MetricGate calculators | One page for the three numbers, with the unit-mixing trap caught | 4 | 4 | 2 | 4 | 5 | 74 | later |
| 18 | Tint and shade scale generator | UI design | UI designer; design system lead; front-end engineer | Make a 50 to 950 color ramp from one brand color, with contrast labels on each step | One or more hex colors | An 11-step ramp in OKLCH, contrast with white and black on each step, CSS variables, JSON tokens, a Tailwind block | Every new brand color and theme | tint and shade generator; color palette generator (no data) | 6 | CSS variables; JSON; Tailwind | 66colorful; tints.dev; MagicPattern | Contrast labels on every step tie the ramp to accessibility, which most generators leave out | 4 | 3 | 5 | 5 | 4 | 84 | drip 1 |
| 19 | MoSCoW sorter | Product strategy | Product owner; business analyst; product manager | Sort requirements into Must, Should, Could, Won't and check the Must share | List of items | Four columns, a warning above 60% Must, export | Release scoping | moscow prioritization (4,400); prioritization moscow method template (480) | 4 | CSV; markdown | Miro templates; ProductPlan glossary | The 60% Must rule enforced; better as a mode of the prioritization scorer | 3 | 4 | 5 | 5 | 5 | 84 | fold |
| 20 | Survey question checker | UX research | UX researcher; product manager; product marketer | Catch leading, loaded and double-barreled questions before a survey goes out | Paste the questions, one per line | Each question flagged (two questions in one, leading words, absolutes, jargon, no 'none' option) with a rewrite hint | Every survey draft, and every review of a colleague's survey | product survey questions (1,600); qualitative survey questions (1,000) | 8 | Text, ready for Google Forms or Typeform | General grammar checkers; vendor articles on bad survey questions | Rule-based and explained (no AI): each flag names the rule and links the article | 4 | 4 | 5 | 5 | 3 | 86 | launch 6 |
| 21 | A/B test sample size and duration planner | Product metrics | Growth lead; product analyst; product manager | Find how many users and how many days a test needs before you start it | Baseline conversion, smallest lift worth finding, daily traffic, number of variants | Users per variant, days to run, and a warning when the test cannot finish in a sensible time | Every experiment brief | power analysis sample size calculator (880); a/b testing calculator (480); ab test calculator (480); a/b testing sample size calculator (140) | 6 | Text for the experiment brief | Evan Miller sample size calculator; Optimizely | Leads with days to run and the 'not worth testing' warning; plain-language result | 4 | 4 | 5 | 4 | 4 | 84 | drip 2 |
| 22 | Launch checklist builder | Product marketing | Product marketer; product manager | Build a launch checklist sized to the launch tier | Launch tier (big, medium, small), channels, date | A dated checklist by team, CSV for Asana or Jira, markdown | Every launch | product launch (1,600); go to market plan (880); product launch strategy (320) | 6 | CSV; markdown | HubSpot and Asana templates | Tiered and dated backwards from launch day | 4 | 3 | 4 | 4 | 4 | 76 | later |
| 23 | Line length and measure calculator | UI design | UI designer; UX writer; front-end engineer | Set a text column width that gives 45 to 75 characters per line | Font, font size, target characters | Container width in px, rem and ch, with a live sample | Every layout and type change | optimal line length (no data) | 4 | CSS | everycalculators line length calculator | Measures the real font in the browser instead of assuming half an em per character | 3 | 2 | 5 | 5 | 5 | 76 | later |
| 24 | Story points to time estimator | Project management | Product owner; scrum master | Translate a backlog in points into sprints and calendar dates | Points, velocity range, sprint length | Sprint count and date range | Release planning | story points (9,900) | 3 | Text | Spreadsheets | A simple mode of the delivery forecast | 3 | 3 | 3 | 4 | 5 | 68 | fold |
| 25 | Task success and time-on-task calculator | UX research | UX researcher | Report completion rate and task time with honest error bars from a small test | Successes out of attempts; task times | Completion rate with an adjusted-Wald interval, geometric mean time with interval, a one-line summary | Every benchmark study | task completion rate; time on task (no data) | 5 | Spreadsheet in, text out | MeasuringU calculators (paid) | Free, small-sample-correct maths explained in plain words | 3 | 1 | 4 | 5 | 5 | 68 | later |
| 26 | Touch target checker | Accessibility | Product designer; UI designer; accessibility specialist | Check that tap targets meet the size and spacing rules for web, iOS and Android | Target size, spacing to neighbors, platform | Pass or fail against WCAG 2.2 (24px minimum, 44px enhanced), Apple 44pt and Material 48dp; the padding needed | Every mobile design review | touch target size (no data) | 4 | Text note for the review | Guideline pages (Apple HIG, Material, W3C) | All three rulebooks side by side, with unit conversion (pt, dp, px) | 3 | 1 | 2 | 5 | 5 | 60 | later |
| 27 | Cycle time and lead time calculator | Project management | Delivery lead; engineering manager; product analyst | Get cycle-time percentiles from a ticket export | Paste start and end dates from a Jira CSV | 50th, 85th and 95th percentile cycle time, a scatter chart, outliers listed | Monthly flow review | cycle time (no data) | 8 | CSV in; PNG out | Jira apps (paid tiers) | Free paste-in percentiles | 4 | 3 | 5 | 4 | 3 | 78 | drip 8 |
| 28 | Interview guide builder | UX research | UX researcher; product manager; founder | Turn a research goal into an interview script with warm-up, core and wrap-up questions | Research goal, who you talk to, session length | A timed script: intro, consent line, open questions from a vetted bank, probes, wrap-up; markdown | Every new study round | user interviews (49,500, mostly the brand); user interview questions (no data) | 8 | Markdown for Notion or Google Docs | Vendor templates (User Interviews, Dovetail, Maze) | Times each block to the session length and flags leading phrasings; no sign-up | 4 | 3 | 3 | 5 | 3 | 74 | later |
| 29 | Error message builder | UX design | UX writer; product designer; engineer | Write an error message that says what happened, why, and what to do | What failed, whether the user can fix it, the fix | Three drafts in the house pattern, checked for blame and jargon, with length | Every new form or flow | error message examples; how to write error messages (no data) | 5 | Text for Figma and string files | Content style guides (Atlassian, Mailchimp) | A rule-driven builder, not a rewrite engine; shows the rule behind each line | 3 | 1 | 4 | 5 | 4 | 66 | later |
| 30 | MVP scope cutter | Product strategy | Founder; product manager | Cut a feature list to the smallest set that tests the riskiest assumption | Features with value, effort and the assumption each tests | The keep list, the cut list with reasons, a scope summary | Each new bet | mvp minimum viable product (720) | 6 | Markdown | No direct tool; templates | Original framing tied to assumption testing | 3 | 1 | 2 | 5 | 4 | 58 | later |
| 31 | Proto-persona worksheet | UX research | Product designer; product manager; founder | Write an assumption-based persona that is clearly marked as a hypothesis | Role, goals, frustrations, context, what you have evidence for | A one-page persona card with an evidence mark on each line; PNG and markdown | Kick-offs and workshops | user persona template (1,600); user persona generator (320); user persona creator (320); user persona maker (260) | 6 | Markdown; PNG for Figma | HubSpot Make My Persona; Xtensio | Marks each line as evidence or guess, so the persona does not pass as research | 3 | 4 | 3 | 5 | 4 | 74 | later |
| 32 | A/B test significance checker | Product metrics | Growth lead; product analyst; product manager | Check if a finished test's difference is real | Visitors and conversions per variant | Lift, p-value and confidence interval, chance to beat control, a plain verdict, a sample-ratio check | Every test readout | ab test calculator (480); ab split test calculator (480) | 6 | Text for the readout | VWO, Dynamic Yield, ABTestGuide | Sample-ratio mismatch check and a plain verdict; but page one is crowded | 4 | 4 | 3 | 4 | 4 | 76 | fold |
| 33 | Release notes formatter | Product management | Product manager; product marketer; engineering manager | Turn a list of merged changes into readable release notes | Paste ticket titles with a type tag | Grouped notes (new, improved, fixed), plain-language prompts, markdown and HTML | Every release | release notes template (no data) | 5 | Markdown; HTML; Slack | Changelog SaaS (Beamer, LaunchNotes) | A free formatter with a style check (no ticket numbers, user benefit first) | 4 | 3 | 5 | 4 | 4 | 80 | drip 6 |
| 34 | Alt text helper | Accessibility | UX writer; product marketer; accessibility specialist | Decide whether an image needs alt text and what kind | Answers to a short decision tree (decorative? a link? a chart?) | The right treatment (empty alt, short alt, long description), a pattern to fill, a length check | Every content upload | alt text (no data) | 4 | HTML attribute | W3C alt decision tree | The decision tree plus a length check and product examples (charts, screenshots, logos) | 3 | 4 | 3 | 5 | 5 | 76 | later |
| 35 | Component state checklist | Design systems | Product designer; design system lead | List every state a component needs (empty, loading, error, disabled, focus) before handoff | Component type | A state checklist with notes; markdown for the ticket | Every component | ui states (no data) | 4 | Markdown for Jira | Blog checklists | Lists per component, with accessibility states | 3 | 1 | 5 | 5 | 5 | 72 | later |
| 36 | Design token naming helper | Design systems | Design system lead; front-end engineer | Name tokens in a consistent tiered pattern (base, semantic, component) | A list of raw values and where they are used | Suggested names by tier, a lint of inconsistent names, JSON export | Every system change and audit | design token naming (no data) | 8 | JSON tokens; CSS variables | Articles (Nathan Curtis); Tokens Studio (Figma plugin) | A naming linter in the browser; none found free | 3 | 1 | 3 | 5 | 3 | 60 | later |
| 37 | Job story builder | Product discovery | Product manager; UX researcher; product marketer | Write job statements in a consistent form from interview notes | Situation, motivation, outcome | 'When... I want to... so I can...' statements, checked for solution words | Discovery synthesis | jobs to be done (no data) | 4 | Markdown | Articles and templates | Flags solution words inside the job | 3 | 1 | 5 | 5 | 5 | 72 | later |
| 38 | Kano survey analyzer | Product strategy | Product manager; UX researcher | Classify features from Kano survey answers | Paste paired functional and dysfunctional answers | Category per feature (must-be, performance, attractive, indifferent), better and worse coefficients, chart | Each feature survey | kano model (no data) | 8 | CSV in and out | Spreadsheet templates; few calculators | Paste-in analysis that most Kano articles leave to Excel | 3 | 3 | 3 | 5 | 3 | 68 | later |
| 39 | Likert scale label builder | UX research | UX researcher; product marketer | Get balanced labels for a 5- or 7-point scale on agreement, importance, frequency or satisfaction | Scale type and number of points | Balanced labels, the scoring map (1 to 5), a copy block for a form tool | Each new survey; people forget the exact wording | importance likert scale (720) | 3 | Text list for forms; CSV | Lists in survey vendor blogs (SurveyMonkey, Qualtrics) | Copyable sets with the scoring key and a note on when to drop the middle point | 3 | 5 | 3 | 4 | 5 | 76 | later |
| 40 | Roadmap now, next, later builder | Product strategy | Product manager; founder; product marketer | Turn a list of bets into a now, next, later roadmap you can share | Items with horizon, theme, confidence | A clean three-column roadmap image and a markdown version | Monthly roadmap updates | product roadmap template (1,000); product roadmap examples (1,000); roadmap tools (390) | 8 | PNG and SVG for slides; markdown | Roadmap SaaS (ProductPlan, Aha!) and slide templates | Outcome-led, free, no account; the SaaS tools gate exports | 3 | 4 | 4 | 5 | 3 | 76 | later |
| 41 | WIP limit and flow calculator (Little's law) | Project management | Delivery lead; scrum master; engineering manager | Set a WIP limit and see how it changes cycle time | Throughput, current work in progress, target cycle time | Cycle time from Little's law, a suggested WIP limit, a what-if slider | Board reviews | work in progress formula (210) | 4 | Text | Articles (Kanban University) | Rare as a tool | 3 | 3 | 5 | 4 | 5 | 76 | later |
| 42 | Fluid size clamp() calculator | UI design | Front-end engineer; UI designer | Turn a min and max size into a CSS clamp() that scales between two widths | Min size, max size, min and max screen width | clamp() expression, slope and intercept, live preview | Every responsive build | clamp calculator (no data) | 3 | CSS | Utopia; Flavio Copes clamp calculator | Better folded into the type scale generator than a page of its own | 4 | 1 | 5 | 3 | 5 | 70 | fold |
| 43 | Runway calculator | Growth and pricing | Founder | See months of cash left and the month you run out, under growth scenarios | Cash, monthly costs, revenue, revenue growth | Runway months, zero-cash month, breakeven month, three scenarios side by side | Monthly for early founders | runway calculator; burn rate (no data) | 5 | CSV; text | Pilot runway calculator; Kruze | Scenarios side by side, explained without finance jargon | 4 | 3 | 5 | 3 | 5 | 78 | drip 9 |
| 44 | Assumption mapper | Product discovery | Product manager; product designer; founder | Rank assumptions by importance and evidence to choose what to test first | Assumptions with importance and evidence scores | A 2x2 map and a test-first list | Every discovery cycle | assumption mapping (no data) | 5 | PNG; markdown | Miro templates | Turns the board into a ranked test plan | 3 | 1 | 5 | 5 | 4 | 70 | later |
| 45 | Experiment brief builder | Product metrics | Growth lead; product manager | Write a test hypothesis with metric, size and stop rule | Change, expected effect, metric, guardrails | A brief (hypothesis, primary and guardrail metrics, size, duration, decision rule); markdown | Every experiment | hypothesis statement (no data) | 5 | Markdown | Vendor templates | Links into the sample size planner | 3 | 1 | 5 | 5 | 4 | 70 | later |
| 46 | Heuristic evaluation scorer | UX design | Product designer; UX researcher; accessibility specialist | Log issues against the ten usability heuristics and rate severity | Issues with heuristic and severity (0 to 4) | Severity table, counts per heuristic, a ranked fix list as CSV or Jira-ready text | Every expert review | heuristic evaluation (no data) | 6 | CSV; Jira markup | Spreadsheet workbooks (NN/g) | Severity maths and a Jira export in one place | 3 | 1 | 4 | 5 | 4 | 66 | later |
| 47 | North Star metric worksheet | Product metrics | Product manager; founder; growth lead | Pick a North Star metric and its input metrics | Product type, the value moment, candidate metrics | A checked North Star with an input-metric tree; markdown and PNG | Yearly strategy; new teams | north star metric (no data) | 6 | Markdown; PNG | Amplitude North Star playbook | Checks candidates against the usual traps (vanity, lagging) | 3 | 2 | 5 | 5 | 4 | 74 | later |
| 48 | Research question generator | UX research | UX researcher; product manager | Turn a vague ask into research questions and a method | The decision the team must make, what is unknown | Three to five research questions and a suggested method for each | Study kick-offs | research question generator (390) | 6 | Markdown | Academic thesis-question generators (a different reader) | Product decision first, method second; the academic tools answer a student's thesis | 3 | 2 | 5 | 4 | 4 | 70 | later |
| 49 | SaaS MRR and ARR calculator | Growth and pricing | Founder; growth lead; product analyst | Compute MRR movements (new, expansion, contraction, churn) and ARR | Monthly revenue movements | MRR bridge chart, ARR, quick ratio | Monthly board numbers | arr formula (1,600) | 5 | CSV; PNG | Baremetrics and ChartMogul (paid) | A free bridge chart | 3 | 2 | 5 | 4 | 4 | 70 | later |
| 50 | CSAT and CES calculator | Product metrics | Product manager; customer experience lead | Compute CSAT and customer effort scores from raw answers | Paste answers | CSAT %, CES average, distribution | Each survey wave | customer satisfaction survey (4,400); customer satisfaction index meaning (3,600) | 3 | CSV | Vendor calculators | Best as a second tab on the NPS page | 3 | 4 | 5 | 4 | 5 | 80 | fold |
| 51 | Focus order and keyboard checklist | Accessibility | Accessibility specialist; product designer; QA | Walk a page with a checklist for focus order, visible focus and keyboard traps | Ticks as you test | A pass/fail report with the WCAG criterion on each line; markdown | Every release test | wcag accessibility (5,400 KD 62); accessibility checker (4,400 KD 76) | 5 | Markdown for Jira | A11Y Project checklist; WebAIM WCAG checklist | A tickable report rather than a reading list | 3 | 2 | 3 | 4 | 5 | 64 | later |
| 52 | Freemium conversion model | Growth and pricing | Founder; growth lead | Model how many free users you need for a revenue target | Signups per month, activation and conversion rates, price, churn | Paying users and revenue over 24 months; the conversion rate that hits the target | Planning season | freemium conversion rate (no data) | 6 | CSV | Spreadsheet models | Rare as a free web tool | 3 | 1 | 3 | 4 | 3 | 56 | later |
| 53 | Funnel conversion calculator | Growth and pricing | Growth lead; product analyst; product marketer | See step and overall conversion and where the biggest drop is | Counts at each funnel step | Step and cumulative conversion, the biggest drop highlighted, what a 10% lift at each step would add | Weekly growth reviews | marketing funnel (9,900, a definition search); sales funnel stages (720) | 4 | CSV; PNG | SaaS lead magnets | The what-if on each step shows where to work | 3 | 4 | 3 | 4 | 5 | 72 | later |
| 54 | Journey map grid builder | UX research | Product designer; UX researcher; product marketer | Lay out stages, actions, thoughts, feelings and opportunities as a clean grid | Stages and rows as text | A printable journey map with an emotion line; PNG, SVG and CSV | Workshops and discovery | customer journey map template (1,000); journey map template (590) | 10 | SVG for Figma; CSV | Miro, Figma community and Canva templates | Text in, drawing out; no canvas skills needed | 3 | 4 | 4 | 5 | 3 | 76 | later |
| 55 | Line height calculator | UI design | UI designer; front-end engineer | Snap line heights to a 4px grid for every size | Font sizes, base grid | Line heights in px and unitless, snapped to the grid | Type setup | line height calculator (no data) | 3 | CSS; Figma | Small calculator sites | Fold into the type scale generator | 3 | 1 | 4 | 4 | 5 | 64 | fold |
| 56 | Market size (TAM, SAM, SOM) calculator | Product strategy | Founder; product manager | Estimate market size bottom up | Number of customers, price, reachable share | TAM, SAM, SOM with the working shown | Pitch decks and business cases | tam sam som (no data) | 4 | Text; slide numbers | Investor blog calculators | Bottom-up only, working shown | 3 | 1 | 5 | 3 | 5 | 64 | later |
| 57 | Meeting cost calculator | Product management | Engineering manager; product manager; founder; scrum master | Show what a meeting costs per session and per year | People and rough salaries or roles, length, how often | Cost per meeting and per year, cost per minute, a line for the calendar invite | Recurring-meeting audits; easy to share | meeting cost calculator (no data) | 3 | Text for the invite | Omni Calculator; Fellow; Koalendar | Recovery time and a yearly view per recurring meeting; but the field is crowded | 3 | 2 | 5 | 4 | 5 | 72 | later |
| 58 | Metric definition card | Product metrics | Product analyst; product manager | Write a metric definition everyone reads the same way | Name, formula, source, filters, owner | A definition card in markdown with a checklist | Each new KPI | kpi examples (14,800); kpi metrics (2,900) | 4 | Markdown for the wiki | Data catalog tools | A shared format for metrics | 3 | 5 | 2 | 4 | 5 | 72 | later |
| 59 | Price sensitivity analyzer (Van Westendorp) | Growth and pricing | Pricing lead; product marketer; founder | Find an acceptable price range from four survey questions | Paste the four price answers per respondent | The four curves, the optimal and indifference price points, the acceptable range, a chart | Each pricing study | van westendorp (no data) | 8 | CSV in; PNG out | MetricGate; Conjointly Excel template; an R package | A free paste-in chart with a plain explanation and a sample-size warning | 3 | 1 | 5 | 4 | 3 | 64 | later |
| 60 | Price tier builder | Growth and pricing | Founder; pricing lead; product marketer | Sketch good, better, best tiers and check the gaps between them | Features, value metric, price points | Tier table, price ratios between tiers, warnings (too close, too much in the bottom tier); HTML and markdown | Pricing reviews | tiered pricing strategy (210); pricing strategy (6,600, a definition search) | 8 | Markdown; HTML table | Pricing page galleries | Checks, not just a table | 3 | 3 | 3 | 4 | 3 | 64 | later |
| 61 | Retro format picker | Project management | Scrum master; delivery lead | Pick a retrospective format for the team's mood and time box | Team size, time, mood (tired, tense, upbeat), remote or in the room | A format with a timed agenda and prompts; copy for Miro or Confluence | Every sprint | sprint retrospective (no data) | 5 | Markdown | Retromat; EasyRetro templates | Matches the format to mood and time; Retromat picks at random | 3 | 2 | 5 | 4 | 5 | 72 | later |
| 62 | Value proposition canvas | Product marketing | Product manager; product marketer; founder | Fill a value proposition canvas and check the fit | Jobs, pains, gains; products, pain relievers, gain creators | The canvas drawing with fit lines; PNG and markdown | Discovery and launch prep | value proposition (22,200, a definition search); value proposition example (1,600) | 8 | PNG; markdown | Strategyzer (owner of the canvas); Miro templates | Strategyzer owns the name; ours would be the fit check | 3 | 4 | 3 | 5 | 3 | 72 | later |
| 63 | Affinity map sorter | UX research | UX researcher; product designer; product manager | Turn a pile of interview notes into rough groups to start synthesis | Paste notes, one per line, optional tags | Notes grouped by shared words and tags, drag to fix, export as CSV or a markdown outline | Every study's synthesis day | affinity diagram; affinity map (no data; 'affinity designer' pollutes the store) | 12 | CSV and markdown for FigJam or Miro | FigJam and Miro boards; Dovetail (paid) | A fast first pass in the browser with no account and no upload; plain word matching, not AI | 3 | 3 | 3 | 5 | 2 | 66 | later |
| 64 | Breakpoint and layout grid calculator | UI design | UI designer; front-end engineer | Work out column widths, gutters and margins for each breakpoint | Breakpoints, columns, gutter, margin | Column width per breakpoint, CSS grid code, a Figma layout-grid table | New layouts and redesigns | grid system in graphic design (880) | 6 | CSS; Figma grid settings | gridcalculator.dk; Figma layout grids | One table for all breakpoints with the matching Figma settings | 3 | 4 | 4 | 4 | 4 | 74 | later |
| 65 | Competitive feature matrix | Product marketing | Product manager; product marketer | Lay out a feature comparison and see where you lead or trail | Competitors and features with marks | A comparison grid image and a gap summary | Quarterly | competitive analysis template (no data) | 5 | PNG; markdown table | Template galleries | A gap summary | 3 | 3 | 5 | 4 | 4 | 74 | later |
| 66 | Dashboard chart picker | UI design | Product designer; product analyst | Pick the right chart for the comparison you want to show | What you compare (over time, parts of a whole, ranking, distribution), number of series | Recommended chart, what to avoid, a small example | Each dashboard design | dashboard design (5,400); dashboard examples (1,900) | 5 | Text | Chart catalogues (Data Viz Catalogue, FT Visual Vocabulary) | Product-metric examples (funnels, cohorts) instead of general charts | 3 | 4 | 3 | 4 | 4 | 70 | later |
| 67 | Stakeholder map | Leadership and teams | Product manager; delivery lead; founder | Place stakeholders on a power and interest grid and plan how to engage each | Names with power and interest scores | The grid as an image and a contact plan table | Every new initiative | project management stakeholder map (110) | 5 | PNG; markdown | Miro and Lucid templates | A plan table attached to the grid | 3 | 4 | 5 | 4 | 4 | 78 | drip 10 |
| 68 | Three-point estimate (PERT) calculator | Project management | Delivery lead; engineering manager; product manager | Turn optimistic, likely and pessimistic guesses into an estimate with a range | Three estimates per task | PERT mean, spread, total with an 85% range | Project planning | three point estimate (no data) | 3 | CSV | Calculator sites | Totals a task list, not one task | 3 | 3 | 4 | 3 | 5 | 68 | later |
| 69 | Planning poker (local) | Project management | Scrum master; product owner | Run an estimation round with cards | Players, deck (Fibonacci, t-shirt) | Revealed votes, spread, agreed estimate | Every refinement session | planning poker (no data) | 20 | Text | planningpokeronline, Parabol, EasyRetro | Real-time voting needs a server, which breaks the no-dependency rule; park | 4 | 3 | 3 | 4 | 1 | 66 | park |
| 70 | Readability checker for UI and docs | UX design | UX writer; product marketer; product manager | See the reading grade of help text, onboarding or a PRD | Paste text | Grade level, long sentences highlighted, hard words with plain swaps | Every help article and release note | readability checker (no data) | 5 | Text | Hemingway Editor; readable.com | A swap list tuned to product jargon; otherwise a crowded field | 3 | 5 | 3 | 3 | 4 | 70 | later |
| 71 | Research participant incentive calculator | UX research | UX researcher; research ops | Set a fair incentive for a session | Session length, audience (consumer, professional, specialist), remote or in person | Suggested range and a budget for the whole study | Every recruit and budget sign-off | user research incentive calculator (no data) | 4 | Spreadsheet row for the budget | User Interviews incentive calculator (built on its own project data) | Weak: the recruiting vendors own the data; ours would rest on published rates | 3 | 1 | 2 | 4 | 4 | 54 | park |
| 72 | Icon size and stroke calculator | UI design | UI designer; design system lead | Pick icon sizes, padding and stroke weights that stay consistent across sizes | Base icon size, grid, stroke | Size set (16, 20, 24, 32), live area, stroke per size, export table | Icon set work | icon sizes (no data) | 4 | Figma table | Material icon guidelines | A small niche | 2 | 1 | 5 | 4 | 5 | 62 | later |
| 73 | Stickiness calculator (DAU/MAU) | Product metrics | Product analyst; product manager | Compute DAU/MAU from counts and compare with typical ranges | Daily and monthly active users | Stickiness ratio with ranges by product type | Monthly review | dau mau ratio (no data) | 3 | Text | Analytics vendors | Small | 2 | 1 | 4 | 4 | 5 | 58 | later |
| 74 | Aspect ratio calculator | UI design | UI designer; product designer; product marketer | Resize an image or frame keeping the ratio, and name the ratio | Width and height, or a ratio and one side | The other side, the simplified ratio, a CSS aspect-ratio line | Constant small use | aspect ratio calculator (no data); golden ratio number (2,400) | 2 | CSS | calculator.net and many others | A crowded utility; fine as a quiet extra | 3 | 5 | 4 | 2 | 5 | 72 | park |
| 75 | px, rem and em converter | UI design | Front-end engineer; UI designer | Convert between px, rem, em and pt | A value and the root size | All units; a table for a whole scale | Daily for some | px to rem (no data) | 2 | CSS | Many developer sites | Crowded; only as part of the type scale generator | 3 | 3 | 5 | 2 | 5 | 68 | fold |
| 76 | Burn-down chart maker | Project management | Scrum master; product owner | Draw a burn-down or burn-up from daily remaining work | Daily remaining points or tasks | Chart with the ideal line; PNG and SVG | Every sprint for teams without tooling | burndown chart (no data) | 5 | PNG for slides | Jira built-in; spreadsheet templates | Useful only to teams without Jira | 2 | 3 | 5 | 4 | 4 | 68 | later |
| 77 | Opportunity score calculator | Product strategy | Product manager; UX researcher | Score outcomes by importance and satisfaction to find underserved needs | Importance and satisfaction ratings | Opportunity scores, a ranked list, a scatter chart | Each needs survey | opportunity score (no data) | 5 | CSV | Templates | Rare as a free tool | 2 | 1 | 4 | 4 | 4 | 56 | later |
| 78 | Pricing page copy checker | Growth and pricing | Product marketer; founder | Check a pricing page draft for the common mistakes | Paste tier names, prices, feature lines | Flags (no recommended tier, feature names users will not know, no annual price) with fix hints | Each pricing change | pricing page (no data) | 5 | Text | Agency checklists | A rule-based check; low demand | 2 | 1 | 4 | 4 | 4 | 56 | later |
| 79 | Mission and vision statement builder | Leadership and teams | Founder; product leader | Draft a mission and a vision and test them against simple rules | Who you serve, what you do, the change you want | Drafts in standard forms, length and jargon checks | Rare (yearly) | mission statement (22,200); mission statement examples (12,100); vision statement examples (6,600) | 4 | Text | Many AI generators and template sites | High demand but generic, rare use and far from the core reader | 2 | 5 | 5 | 2 | 5 | 70 | park |
| 80 | RACI builder | Leadership and teams | Product manager; delivery lead; engineering manager | Assign who is responsible, accountable, consulted and informed | Tasks and people | RACI table with checks (one A per row), CSV | Project start | raci chart (no data) | 4 | CSV; markdown | Spreadsheet templates | Validation rules | 2 | 4 | 5 | 3 | 5 | 70 | later |
| 81 | Discount break-even calculator | Growth and pricing | Pricing lead; founder | See how much more volume a discount needs to keep profit flat | Price, margin, discount | Break-even volume increase | Promotions | (no data) | 3 | Text | Finance calculator sites | Small and generic | 2 | 1 | 2 | 3 | 5 | 46 | park |
| 82 | Offer comparer for product roles | Leadership and teams | Product manager; product designer | Compare two job offers on total yearly value | Base, bonus, equity, benefits | Side-by-side yearly value | Rare | product management jobs (3,600, a job search) | 5 | Text | Levels.fyi | Weak; Levels.fyi owns it | 2 | 3 | 1 | 2 | 4 | 44 | park |

## 4. Web scan notes (27 ideas scanned, October 10)

Free web searches, standard mode, US. One search per idea; the top existing tool and the shape of page one are noted. This is a reading of the free search results, not a Google page-one pull; the paid check confirms the shape for the head phrases.

| Tool | Top existing tools | Page one | Demand signs |
|---|---|---|---|
| SUS score calculator | Trymata free SUS calculator; Lyssna Google Sheets template | Open: NN/g ranks #1 with an article; only one or two real calculators on page one (Oct 8 SERP) | Several free and paid calculators exist, including a 59 euro Excel calculator: people pay for this job. |
| User story and acceptance criteria builder | Figr and Kollabe acceptance criteria generators (AI) | Template and article pages (Atlassian, Asana); store KD 10 to 21 | AI generators appearing (Figr, Kollabe) and AI skill listings. |
| Backlog prioritization scorer (RICE, ICE, WSJF) | EasyRetro, ProductLift, Kollabe RICE calculators (one item at a time) | 'rice calculator' is food and sports; 'rice score calculator' shows small tool sites | At least eight free RICE calculators, all one item at a time; worked examples in articles that do not add up. |
| Sprint capacity calculator | Vendor articles and spreadsheet templates (ONES, Xebia); no standard free tool | Vendor blogs and docs only; open | Vendor docs describe the same method (focus factor 0.6 to 0.8); no free calculator. |
| Usability test sample size calculator | MeasuringU tables and articles (no calculator surfaced in the scan) | Open: page one is papers and articles; no calculator found | An academic and practitioner debate (Nielsen and Landauer, MeasuringU, ACM); no tool. |
| Delivery forecast (velocity range and Monte Carlo) | Jira marketplace forecasting apps (Monte Carlo is a paid tier); spreadsheets | No free web tool surfaced; apps and Python packages | Python packages, a Jira app with Monte Carlo behind a paid tier, a ProKanban lab. |
| Retention and churn calculator | Founderpath cohort analysis; MetricGate; Amplitude churn calculator | 'churn rate calculator': SaaS lead magnets plus thin calculator sites (Oct 8 SERP), the beatable layer | Founderpath and MetricGate accept pasted cohort tables. |
| Type scale generator | typescale.com (Jeremy Church); Utopia fluid type | Many small tools and plugins; no big product owns it | Many generators and Figma plugins; an npm package. |
| OKR checker | goalsandprogress OKR builder; spreadsheet checklists | No standard tool; template and article pages | Teams build their own spreadsheet checkers; AI skills validate OKRs. |
| Survey sample size and margin of error calculator | SurveyMonkey and Qualtrics margin of error calculators; Raosoft | Crowded at the head (SurveyMonkey, Qualtrics, Raosoft, calculator sites); the survey tail is softer (KD 25) | Every survey vendor offers one as a lead magnet. |
| Microcopy length checker | Hemingway Editor (general prose) | No dedicated tool found; page one is AI skill listings and guides | Only AI skills and guides; no checker. |
| Positioning statement builder | Miro positioning template; AI skill listings | No generator found; templates and guides | Miro templates and AI skill listings; no builder. |
| Palette contrast checker | WebAIM contrast checker (one pair at a time); Coolors | Head term held by WebAIM and big brands; the 'palette' angle is open | Tools adding APCA and auto-fix suggestions; APCA status unsettled. |
| NPS calculator with margin of error | Hotjar, QuestionPro, Youform NPS calculators | 'nps calculator' is split with India's pension scheme; the product variant is held by survey vendors | Survey vendors (Hotjar, QuestionPro, Youform); none shows a margin of error. |
| Spacing scale and token export | figr.design spacing generator; bushe.co | Small tools and AI skill pages; open | AI skill listings and small generators. |
| Unit economics: LTV, CAC and payback | Founderpath, xgenious, MetricGate calculators | 'ltv calculator' is mortgages; 'cac calculator' is mixed; the product variants need a check | Six or more free calculators; one warns about mixing annual revenue with monthly churn. |
| Tint and shade scale generator | 66colorful; tints.dev; MagicPattern | Many small generators; no dominant brand | Many small generators moving to OKLCH. |
| A/B test sample size and duration planner | Evan Miller sample size calculator; Optimizely | Crowded with established tools (Optimizely, Evan Miller, Statsig, CXL) | Established tools (Evan Miller, Optimizely, Statsig). |
| Line length and measure calculator | everycalculators line length calculator | Thin calculator sites; open | Thin calculator sites; a design skill listing. |
| Story points to time estimator | Spreadsheets | Articles | Method described in courses and talks; no tool. |
| Error message builder | Content style guides (Atlassian, Mailchimp) | Unknown | Covered by the microcopy scan: no tool. |
| A/B test significance checker | VWO, Dynamic Yield, ABTestGuide | Fragmented: many thin calculator sites plus vendors (Oct 8 SERP) | Bayesian calculators from VWO, Dynamic Yield, Leadpages. |
| Fluid size clamp() calculator | Utopia; Flavio Copes clamp calculator | Crowded with developer tools | Five or more developer tools. |
| Runway calculator | Pilot runway calculator; Kruze | Finance and accounting firms; small sites appear | Accounting firms (Pilot, Kruze) and calculator sites. |
| Meeting cost calculator | Omni Calculator; Fellow; Koalendar | Many SaaS lead magnets; small sites appear | Ten or more calculators, most SaaS lead magnets. |
| Price sensitivity analyzer (Van Westendorp) | MetricGate; Conjointly Excel template; an R package | A handful of tools and guides; open | MetricGate, a Conjointly Excel template, an R package. |
| Research participant incentive calculator | User Interviews incentive calculator (built on its own project data) | Held by recruiting vendors (User Interviews, Respondent, Rally, Entropik) | Five or more vendor calculators built on their own data. |

Generic searches for 'is there a tool' threads returned tool pages, not forum threads; Reddit did not surface in standard mode. A search inside r/ProductManagement and r/userexperience is a free next step if wanted.

## 5. Ranking, the launch ten and the drip

Rescored on October 10 with the paid check. Search intent is now the measured US demand across each idea's phrases (tool, template and example phrases in full, how-to phrases half, definitional phrases a fifth, capped at 1,000; phrases above difficulty 60 left out). Openness is the difficulty of the phrase worth targeting, plus one when page one is mostly thin sites and forum posts, minus one when big products and SaaS pages hold seven or more of the ten. Usefulness, fit and build cost are unchanged. Full method and per-tool numbers: `research/tools/seo-check-summary-2026-10-10.md`.

### The launch ten

1. **PRD outline generator** (Product discovery; score 92, was 84; about 6 hours). Measured: PRD template 2,900 a month at difficulty 6, the easiest strong phrase in the set. Page one for 'prd generator' is all AI writing apps and forum threads; a structured, no-sign-up outline that scales to the size of the work stands apart. Ships with its own template page.
2. **User story and acceptance criteria builder** (Product discovery; score 90, was 90; about 8 hours). Measured: the demand is template demand (user story template and format, 2,900 each, difficulty 18); 'user story generator' itself is only 30 a month and its page one is AI generators from Miro, Atlassian and Figma. Still the weekly job of every product owner, so it stays: the page answers the template search and the builder does the work.
3. **Type scale generator** (UI design; score 86, was 82; about 8 hours). Measured: type scale generator 110 a month (difficulty 30), plus font size scale 90. Small, but page one is thin single-purpose sites, a Hacker News thread and a GitHub gist: the most beatable design page in the check.
4. **OKR checker** (Product metrics; score 86, was 82; about 8 hours). Measured: OKR examples 1,300 at difficulty 5 and OKR template 880 carry it; 'okr checker' has no volume and its page one is OKR software listings. A checker on an examples page answers both.
5. **NPS calculator with margin of error** (Product metrics; score 86, was 78; about 5 hours). Measured: the surprise of the check. NPS calculator 8,100 a month in the US, 5,400 in the UK, 720 in Canada, difficulty 16; 'how to calculate nps' adds 1,900. Page one is survey vendors' lead magnets plus one thin calculator site. The margin-of-error check and the CSAT and CES tab are what they skip.
6. **Survey question checker** (UX research; score 86, was 74; about 8 hours). Measured: product survey questions 1,600 at difficulty 8; 'how to write survey questions' 480. Page one for 'survey question checker' is AI survey makers only; a rule-based checker that explains each flag is the only one of its kind there.
7. **SUS score calculator** (UX research; score 84, was 92; about 6 hours). Measured: small demand (SUS score calculator 50, SUS calculator 40, how to calculate SUS score 30 a month) but the most open page one in the check, difficulty 2, with NN/g's article on top. Kept for the reader it serves and the authority it earns, not for traffic.
8. **Backlog prioritization scorer (RICE, ICE, WSJF)** (Product strategy; score 84, was 88; about 10 hours). Measured: prioritization matrix 2,400 (UK 1,300) at difficulty 21 and MoSCoW method 4,400 at 16 carry it; 'rice score calculator' is 50 a month and its page one is nine vendor calculators. The whole-backlog ranking and the MoSCoW mode are the angle.
9. **Sprint capacity calculator** (Project management; score 84, was 88; about 6 hours). Measured: tiny demand (capacity planning scrum 140, sprint capacity calculator 30), page one of vendor articles and spreadsheets with no standard tool, difficulty 0. Kept on repeat use: every scrum team, every two weeks.
10. **Retention and churn calculator** (Product metrics; score 84, was 84; about 10 hours). Measured: retention rate formula 1,600 at difficulty 18 holds; churn rate calculator 260 (difficulty 18) with a page one of SaaS lead magnets and thin calculator sites. The cohort paste and the chart are what they lack.

Spread: Product 4 (user story, PRD, prioritization, sprint capacity), Business 3 (OKR, NPS, retention), Design and research 3 (type scale, SUS, survey questions). Accessibility still has no launch tool; the palette contrast checker stays first reserve (big demand, closed page one).

Out of the first list: the delivery forecast (score 84 -> 80; no search for the tool) and the survey sample size and margin of error calculator (82 -> 78; crowded head, empty tail) open the drip's second half; the usability test sample size calculator (86 -> 74; 10 searches a month) moves to later, and its answer can sit on the SUS page as a section.

### The second ten (the drip, one or two a month)

1. **Tint and shade scale generator** (UI design; score 84, was 76). Measured: tint and shade generator 590 a month at difficulty 6, color shade generator 480; page one is thin tool sites and Tumblr and Facebook posts. The 74,000 'color palette generator' is out of reach (difficulty 100).
2. **A/B test sample size and duration planner** (Product metrics; score 84, was 72). Measured from the store: power analysis sample size calculator 880 at difficulty 7; 'ab test duration calculator' only 20 a month. Significance check as a second tab (statistical significance calculator, 2,900 at difficulty 26).
3. **Positioning statement builder** (Product marketing; score 84, was 80). Measured: positioning statement examples 1,300 at difficulty 5 (UK 210, Canada 140); template 390. Page one mixes Harvard, Mailchimp and marketing blogs, no builder.
4. **Palette contrast checker** (Accessibility; score 82, was 78). Measured: the biggest tool demand in the set (color contrast checker 12,100, contrast checker 8,100, WCAG contrast checker 1,300) but difficulty 56 to 59 and a page one held by WebAIM, Adobe and accessibility vendors. First reserve for launch if you want accessibility on day one; the whole-palette check is the angle.
5. **Delivery forecast (velocity range and Monte Carlo)** (Project management; score 80, was 84). Measured: almost no searches for the tool itself (sprint velocity calculator 50; the Monte Carlo and release forecast phrases had no data; 'when will it be done' is 2,400 but a song). Page one for Monte Carlo is papers and forum threads. A strong tool with weak search: build it for readers after launch.
6. **Release notes formatter** (Product management; score 80, was 68). Measured: release notes template 720 a month at difficulty 2; generator 70. Promoted from later: the easiest template-shaped phrase after PRD.
7. **Survey sample size and margin of error calculator** (UX research; score 78, was 82). Measured: the head (sample size calculator, 8,100) stays at difficulty 39 and page one is survey vendors (SurveyMonkey twice); the survey margin of error phrases came back with no data. Drops out of the launch ten.
8. **Cycle time and lead time calculator** (Project management; score 78, was 70). Measured: lead time vs cycle time 720 and cycle time calculator 390, both at difficulty 0. Promoted from later; pairs with the delivery forecast.
9. **Runway calculator** (Growth and pricing; score 78, was 66). Measured: burn rate calculator 590 at difficulty 3. Promoted from later; the founder's page.
10. **Stakeholder map** (Leadership and teams; score 78, was 62). Measured: stakeholder mapping 4,400 at difficulty 7 and stakeholder map template 1,300 at difficulty 3. Promoted from later; a grid builder on a teaching page.

Moved to later by the check: microcopy length checker (80 -> 76), unit economics (78 -> 74), spacing scale and token export (78 -> 70), usability test sample size calculator (86 -> 74).

### Folded into other tools

- MoSCoW sorter: fold into the prioritization scorer.
- Story points to time estimator: fold into the delivery forecast.
- Fluid size clamp() calculator: fold into the type scale generator.
- Line height calculator: fold into the type scale generator.
- px, rem and em converter: fold into the type scale generator.
- CSAT and CES calculator: fold into the NPS calculator.
- A/B test significance checker: fold into the A/B test planner.

### Parked

- Planning poker (local): real-time voting needs a server.
- Offer comparer for product roles: off the core reader, Levels.fyi owns it.
- Mission and vision statement builder: big demand but generic and rare use.
- Research participant incentive calculator: the recruiting vendors own the data.
- Discount break-even calculator: generic finance.
- Aspect ratio calculator: crowded utility.

## 6. The paid check (approved and run October 10; $0.226)

Ran on October 10 as proposed, for $0.226 (balance $19.89). Results: `research/seo/keywords/tools-2026-10-10.csv`, `research/seo/serps/tools-2026-10-10.csv` and `research/tools/seo-check-summary-2026-10-10.md`. The proposal as it stood:

199 phrases with no store data (the full list is in `research/tools/paid-check-phrases-2026-10-10.csv`). Proposed as one batch, standard queue, cache first per the seo-research rules:

| Call | What | Price | Cost |
|---|---|---|---|
| Google Ads search volume, US | all 199 phrases in one task | $0.06 per task (standard) | $0.06 |
| Google Ads search volume, UK and Canada | the 69 phrases of the launch ten and the drip, one task each | $0.06 per task | $0.12 |
| Labs bulk keyword difficulty, US | all 199 phrases | $0.012 + $0.00012 per row | $0.036 |
| Google organic page one, US | the 20 head phrases of the launch ten and the drip | about $0.0006 each (standard, as measured Oct 8) | $0.012 |
| **Total** | | | **about $0.23** |

Phrases:

8pt grid; ab test duration calculator; ab test hypothesis template; ab test significance calculator; acceptance criteria generator; accessibility checklist; accessible color palette; affinity diagram; affinity diagram generator; affinity map; affinity mapping tool; agile release forecast; alt text; alt text examples; aspect ratio calculator; assumption map template; assumption mapping; best line height for body text; burn rate calculator; burn up chart; burndown chart; burndown chart template; button label length; cac payback calculator; capacity planning scrum; characters per line; chart chooser; churn rate calculator; cohort retention analysis; color contrast checker; color palette contrast checker; color palette generator; color shade generator; competitive analysis template; confidence interval for completion rate; contrast checker; conversion rate calculator; csat calculator; css clamp calculator; css grid generator; customer acquisition cost calculator; customer churn calculator; customer interview questions; customer journey map generator; customer lifetime value calculator; cycle time calculator; dau mau ratio; design token naming convention; design tokens; design tokens generator; discount break even calculator; double barreled question checker; empty states; error message examples; error message generator; feature comparison chart; flesch kincaid calculator; fluid typography calculator; font size scale; free to paid conversion rate; freemium conversion rate; funnel conversion rate calculator; grid calculator; heuristic evaluation checklist; heuristic evaluation template; how many participants usability test; how many users for usability testing; how to calculate csat; how to calculate nps; how to calculate sus score; how to write alt text; how to write error messages; how to write okrs; how to write survey questions; hypothesis statement; ice score prioritization; icon grid; icon size guidelines; job story template; jobs to be done statement; journey map maker; kano analysis calculator; kano model; kano survey; keyboard accessibility testing; kpi template; launch plan template; lead time vs cycle time; leading question checker; likert scale 5 point; likert scale examples; likert scale generator; line height calculator; line length calculator; littles law calculator; ltv cac ratio calculator; margin of error calculator; market size calculator; meeting cost calculator; metric definition template; microcopy checker; minimum tap target size; mission statement generator; modular scale calculator; monte carlo forecast agile; moscow method; moscow prioritization template; mrr calculator; mvp feature prioritization; mvp scope; net promoter score calculator; net revenue retention calculator; north star metric; north star metric examples; now next later roadmap; nps calculator; okr checker; okr generator; opportunity score formula; optimal line length; outcome driven innovation; persona generator; persona template; pert calculator; planning poker; positioning statement examples; positioning statement generator; positioning statement template; prd generator; price sensitivity meter; pricing page best practices; pricing tiers; prioritization matrix; product launch checklist; px to rem; raci chart template; raci matrix; readability checker; readability score; release notes generator; release notes template; rem to px; research question generator ux; responsive breakpoints; retro template; retrospective ideas; rice prioritization calculator; rice score calculator; roadmap maker; saas pricing tiers; saas quick ratio; spacing scale generator; sprint capacity calculator; sprint planning capacity; sprint retrospective formats; sprint velocity calculator; stakeholder map template; stakeholder mapping; startup runway calculator; statistical significance calculator; stickiness ratio; story point calculator; story points to hours; survey margin of error calculator; survey question checker; sus calculator; sus score calculator; sus score interpretation; system usability scale calculator; tailwind color generator; tam sam som calculator; task completion rate calculator; team capacity calculator; three point estimate; tiered pricing; tint and shade generator; touch target size; type scale generator; typography scale generator; ui component states; usability test sample size; usability testing sample size calculator; user interview questions; user interview script template; user research incentives; user story generator; ux research incentive calculator; ux research questions; ux writing tool; value proposition canvas; value proposition canvas template; van westendorp calculator; wcag checklist; wcag contrast checker; wcag target size; when will it be done; which chart to use; wip limit; wsjf calculator

## Sources

- The paid check, October 10: `research/seo/keywords/tools-2026-10-10.csv`, `research/seo/serps/tools-2026-10-10.csv`, `research/tools/seo-check-summary-2026-10-10.md`.

- `research/seo/keywords/*.csv` (the store, read October 10; no calls).
- `research/seo/serps/phase0-tools-summary-2026-10-08.md` and `page-one-2026-10-08-tools.csv` (twelve calculator page ones, US, October 8).
- Free web searches on October 10 (standard mode, US).
- `research/discussion/brd-v1-2026-10-08.md` sections 4.2, 4.4, 4.5; the search-policy rulebook, sections 1, 4, 12 and 13, and its site layer (launch with at least ten working tools).
