# Review of unassigned keywords (8 Oct 2026)

Question from the owner: did the rule-based clustering miss related keywords?

Files:

- `keywords/review-unassigned-combined-2026-10-08.csv`: every unassigned keyword of the combined on-topic set
  (Phase 1b clustering), with a verdict.
- `keywords/review-unassigned-phase1-2026-10-08.csv`: the kept rows only from the first (Phase 1) harvest's
  unassigned bucket and its seven noise topics.
- `tools/cluster_rules_patch.md`: the rule patterns that would have caught the recovered keywords (not applied).

Columns in both CSVs: keyword, volume, difficulty, verdict (existing | new | off), topic, subtopic, reason.

## Method

Manual review of each phrase, not rules. Every one of the 376 unassigned keywords in the combined set was read
and given a verdict: belongs to an existing v2 topic (named, with sub-topic where clear), belongs to a topic we do
not have yet (a proposed name), or off-field (with a two-word reason). The 6,211 Phase 1 rows (5,288 unassigned
plus the seven noise topics: ai tools 263, design (general) 204, marketing (general) 182, seo and keyword research
107, customer service 62, system and software design 74, graphic and visual design 31) were read in 16 chunks of
400 and only the rows that belong to the site's field were kept. The field: UX and product design, product and
project management where it meets product work, and the business side of products (metrics, growth, pricing,
strategy). Judgment calls leaned strict: generic dictionary words ("requirements", "priority", "methodology"),
tool and vendor searches, job listings and industry-specific small-business plans were left out.

Adjusted volume below = each distinct (volume, 12-month series) pair counted once, as in the Phase 1b summary,
because word-order variants share one Google figure.

## Counts

| | Combined set (Task 1) | Phase 1 harvest (Task 2) |
|---|---|---|
| Rows scanned | 376 | 6,211 |
| Already in a v2 topic (not a miss) | n/a | 4 ("design thinking", "a/b testing" and two variants) |
| In the combined unassigned set (judged in Task 1) | n/a | 11 |
| Recovered to an existing topic | 32 (109,540 raw) | 110 (487,460 raw) |
| New-topic candidates | 32 (63,410 raw) | 62 (366,600 raw) |
| Off-field | 312 (1,060,350 raw) | 6,024 |

Both sets together: 142 keywords recovered into existing topics (597,000 raw, about 564,000 adjusted) and 94
new-topic keywords. For scale, v2 clustered 2,641 keywords, so the recovered rows add about 5% to the assigned
set by count.

## Recovered into existing topics, by topic

Both sets combined, sorted by adjusted volume. KD is the median difficulty of the recovered rows.

| Topic | Keywords | Raw volume | Adjusted | KD | Main recoveries |
|---|---|---|---|---|---|
| project management | 10 | 114,090 | 114,090 | 7.5 | task management (90,500), project coordinator, statement of work, kick off meeting, program management, scope of work examples |
| accessibility | 3 | 78,900 | 78,900 | 27 | electronic accessibility (74,000; sent to noise by the word "electronic"), universal design, assistive technologies examples |
| retention, churn and engagement | 8 | 75,720 | 75,720 | 20.5 | retention (40,500), retention def, customer success, customer loyalty, what is a customer success manager |
| product strategy, discovery and launch | 25 | 56,080 | 53,240 | 17 | value proposition (22,200), beta testing, product line, unique selling proposition meaning, unique value proposition, product failures |
| ux research | 9 | 66,900 | 51,710 | 0 | closed questions in research (27,100), filter question examples (14,800), uat testing, hybrid, contingency and branching questions, importance likert scale |
| growth marketing and funnels | 12 | 50,880 | 49,880 | 38.5 | call to action (18,100), marketing plan, b2b marketing, customer acquisition, conversion rate optimization marketing |
| web design | 14 | 21,790 | 21,790 | 28.5 | portfolio website, landing page examples, about us page examples, faq page examples, website footer examples |
| design thinking | 4 | 19,000 | 19,000 | 31.5 | design process, design process thinking, human centered design, problem statement examples |
| analytics | 2 | 13,700 | 13,700 | 7.5 | data analysis tools, product analyst |
| ux and ui design (discipline) | 2 | 13,200 | 13,200 | 24.5 | digital design, the design of everyday things (a books lead) |
| a/b testing and experimentation | 6 | 12,130 | 12,130 | 29.5 | hypothesis testing (8,100), a b c testing, a b n testing |
| agile, scrum and kanban | 13 | 13,130 | 10,490 | 8 | software development methodologies, sdlc, spiral model, v model, crystal methodologies |
| okrs, kpis and metrics | 3 | 10,400 | 10,400 | 34 | customer acquisition cost, customer lifetime value, arr formula |
| requirements and prd | 1 | 8,100 | 8,100 | 32 | spec driven development |
| personas and journey maps | 4 | 7,780 | 7,780 | 12.5 | flow chart examples, customer profile, flow of a website, patient journey map |
| prioritization | 5 | 6,220 | 6,220 | 36 | urgent important matrix and three variants (Eisenhower), prioritization grid |
| product management (discipline) | 9 | 11,970 | 6,170 | 0 | product service management (five variants), product features, examples of digital products, pragmatic marketing |
| go-to-market and product marketing | 5 | 5,810 | 5,810 | 25 | ideal customer profile, what are customer segments, product promotion strategy |
| design systems and ui components | 5 | 9,840 | 4,480 | 25 | design-system, grid system graphic design (three variants) |
| stakeholder and change management | 1 | 880 | 880 | 0 | expectation management |
| information architecture | 1 | 480 | 480 | 27 | website sitemap examples |

Two recoveries are single dictionary-style heads ("task management", "retention") and carry most of their topic's
figure; read project management and retention with that in mind.

## Proposed new topics

Only topics with 10 or more keywords or 5,000 or more adjusted monthly searches are proposed.

| Proposed topic | Domain | Keywords | Raw volume | Adjusted | KD | Keywords (top by volume) |
|---|---|---|---|---|---|---|
| business strategy fundamentals | business | 31 | 204,660 | 175,680 | 25 | business plan (27,100), start a business plan, starting a business plan, mission statement (22,200), mission statement examples, small business plan, new business plan, software as a service, business plan examples, sba business plan template, vision statement examples, vision statement, strategic management, what is a business plan, business model meaning, vision statement vs mission statement, creating a mission statement, and company examples (Target, Delta, GE) |
| visual design principles | design | 11 | 74,100 | 65,400 | 20 | principles of design (27,100), elements of design (14,800), design principles, balance in principles of design, design elements, principles of design unity, what are the principles of design, contrast as a principle of design (and two contrast variants) |
| market research and competitor analysis | business | 19 | 53,660 | 23,160 | 24 | market research analyst (5,400), online market research platform(s), market research for starting a business, market research and marketing (11 word-order variants at 2,900), market research for small business, customer insights, competitive benchmarking, competitive edge research |
| customer experience (cx) | business | 12 | 18,820 | 18,820 | 6.5 | customer experience (4,400), customer satisfaction index meaning, customer centric, voice of the customer, customer experience software, customer experience platforms, customer experience questions, customer advocacy, customer focus, customer obsession |
| dashboard and data visualization design | design | 4 | 17,300 | 17,300 | 25.5 | data visualization tools (8,100), dashboard design (5,400), dashboard examples, data visualization examples |
| business analysis | product | 4 | 27,800 | 27,800 | 4 | business analyst (22,200), business systems analyst, it business analyst, senior business analyst |
| ux writing and content design | design | 11 | 7,070 | 6,650 | 0 | ux writing (1,900), what is ux writing, content strategy, ux writing portfolio(s), good ux writing, ux writing sample(s) and example(s), ux writing hub |

Read with care:

- **Business strategy fundamentals** is the largest, but most of it is "how to write a business plan" for a small
  business, not product strategy. Mission and vision statements (about 15 keywords) and business model / SaaS are
  the parts that fit the brief. 26 other business-plan rows (22 industry plans such as cleaning, bakery, salon and
  car dealership, plus plan writers, consultants and books) were judged
  off-field and are not in the count.
- **Business analysis** clears the bar on one head term, and that head is mostly a job search. Treat it as a
  role article inside product owner and product manager roles rather than a topic.
- **Market research** was the Phase 1b near miss (19). It now has 19 keywords, but the adjusted figure (23,160)
  shows how much is one variant set.
- Considered and not proposed: "ai in product and design work" (2 keywords: ai design assistant 22,200, ai
  governance framework 4,400). It clears 5,000 on paper, but two phrases are not a topic.

## Largest off-field groups

Combined set (312 off-field rows):

| Group | Rows | Raw volume |
|---|---|---|
| software engineering system design (interviews, primers, ML and embedded systems, SDLC as an IT subject) | 58 | 123,970 |
| Bible journey maps (Paul, Moses, Abraham, Exodus, Jonah) | 48 | 42,000 |
| building and engineering systems (sprinkler, irrigation, HVAC, solar, septic, closets) | 35 | 39,030 |
| literature journey maps (Odysseus, Frodo, Bilbo) | 24 | 89,210 |
| physical accessibility (student services, beaches, ramps, wheelchairs, healthcare) | 23 | 313,000 |
| device accessibility settings (Outlook, iPad, Nintendo, controllers) | 21 | 184,400 |
| nursing prioritization (NCLEX, delegation) | 19 | 8,720 |
| PLM and PIM software (Siemens, SolidWorks, Windchill) | 18 | 43,280 |
| history journey maps (Lewis and Clark, Columbus) | 7 | 40,220 |
| IT and security architecture, DITA | 11 | 3,160 |
| Jane Street "strategy and product" internship | 6 | 2,120 |
| other (20 small groups: Cadence chip software, spelling, travel planners, hair products, medical tests, labeling rules) | 42 | 171,240 |

Phase 1 harvest (6,024 off-field rows; groups by the dominant word, approximate):

| Group | Rows |
|---|---|
| dictionary and synonym queries ("important meaning", "another word for priority") | 433 |
| metric system and numbers | 321 |
| sales jobs and retail ("sales associate", store sales) | 301 |
| school writing, stories and citations | 300 |
| website builders, domains and hosting | 291 |
| marketing agencies, SEO tools and social media | 272 |
| software development services and companies | 250 |
| consumer AI apps (image generators, chatbots, humanizers) | 237 |
| medical and lab testing | 231 |
| stock market and investing | 152 |
| everything else (brands, place names, managers, products, requirements of unrelated kinds) | 3,236 |

## Judgment

**Did the rules miss much?** Not much, and less than the raw volume suggests. In the combined set, 312 of 376
unassigned rows (83%) are correctly off-field; the noise rules were right about Bible journeys, building systems,
nursing and PLM. The rules missed 32 keywords there, of which one matters: "electronic accessibility" (74,000),
which the accessibility noise rule threw out because it listed the word "electronic". Three noise rules are too
wide (electronic, patient, grid); the patch file fixes them. The rest of the combined misses are small (product
strategy phrasings, a/b/n variants) plus two near-miss groups that were already known (market research 18, ux
writing 10).

The Phase 1 harvest held more: 110 keywords for existing topics and 62 for new ones, out of 6,211 (under 3%).
These were never in the combined set because Phase 1b re-harvested by phrase match, so cluster_v2.py never saw
them. The useful finds are phrases that do not contain a seed word: "closed questions in research", "filter
question examples", "value proposition", "customer acquisition cost", "customer lifetime value", "urgent
important matrix", "beta testing", "statement of work", "landing page examples", "principles of design".

**Does it change the launch shortlist in `research/seo/topic-tree-v1.md`?** Not the top eight. The recoveries
mostly add to topics already on it or next in line, and none is large enough to reorder them without re-scoring:

- Already shortlisted and slightly stronger: project management (+114K, but 90,500 of it is "task management",
  a tool query), UX research (+52K adjusted, surveys again: "closed questions in research", "filter question
  examples"), web design (+22K, landing page and page-pattern examples), analytics (+14K).
- Next in line and stronger: product strategy and product-market fit gains about 53K adjusted at KD 17 ("value
  proposition" 22,200, "beta testing", "unique value proposition"). That roughly doubles its demand (39,700
  adjusted in v2) and is the one recovery that could move a core topic into the shortlist after re-scoring.
- Worth adding to the candidate list: **visual design principles** (65,400 adjusted, KD 20, 11 keywords), a
  natural fit for the design pillar and a classic evergreen article set; and **customer experience** (18,820,
  KD 6.5), small but low difficulty and on-brief. Business strategy fundamentals is large but mostly small-business
  plans, so it should wait for the owner's fit call rather than enter the shortlist on volume.

Next step if the owner agrees: apply `tools/cluster_rules_patch.md`, re-run cluster_v2.py over the combined set
plus the Phase 1 recoveries, and re-score product strategy, visual design principles and customer experience
with the Phase 4 method (head-term SERPs needed for the last two).
