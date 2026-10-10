# Discussion log — User and the Product

## 8 Oct 2026 — kick-off

Owner shared BRD v1 (see `brd-v1-2026-10-08.md`). Discussion only; no build, no code.
Decisions: none yet. Open questions and Claude's first read are in the chat for this date;
decisions get appended here as they are made.

Owner clarifications (same evening):
- Nothing from Printables carries over except the system: SEO research store, pillar method, competitor
  list, content planning, build windows and scheduled publishing, retrofitted for articles.
- Phase 1 is articles that rank. The site should read like Smashing Magazine, not NN/g; UX plus product
  management plus business metrics, not UX only.
- The owner is the author: 15 years in product design and product management. userandproduct.com is owned.
- Primary goal is authority in both directions: the experience backs the site, the site backs the owner.
  Traffic second, money later.
- Secondary content: tools for PMs and agile teams if useful, a books list with Amazon affiliate links,
  a useful-links directory in the bookmarks.design style but wider (product tools). Downloads are optional.
- Open question raised by the owner: which content types give an edge over competitors (evergreen
  explainers, short-form news, tools, directories).

Claude's first read (same evening, kept here so the reasoning is on disk):
- The research store, cache rules, pillar method, competitor pass, tree and build-plan app, build windows
  with scheduled posts, and the ops layer (Cloudflare, origin lock, IndexNow, deploy) all port.
- What does not: the rate (10 pages a day). A named author sustains 3-5 substantial pieces a week.
  Claude's role shifts to research, briefs, teardowns, outlines, fact-checks and edits; the first-hand
  material comes from the owner. Pillar scoring needs an "AI Overview present" column.
- Edge, in order: decision pieces over definitions; calculators and small tools; a frameworks library as
  the hub layer; the directory and the books list as structured post types; no short-form news (a monthly
  notes column instead).
- Authority loop: a real author page with Person schema and sameAs links, a consistent voice, signature
  pieces with original material; LinkedIn is the distribution channel. Perception in 1-2 months,
  measurable Google traffic in 4-9 months.
- Starting eight pillar candidates: product metrics and analytics; prioritization and roadmapping; product
  discovery and research; UX fundamentals and usability; design systems and accessibility; agile and
  delivery; product strategy and business; careers in product and design.
- Starting competitor list: Smashing, NN/g, UX Collective, UX Planet, Mind the Product, SVPG, Lenny's,
  Reforge, Productboard and ProductPlan glossaries, Hotjar, Maze, Userpilot, Amplitude, Pendo, Dovetail,
  UX Pilot (owner's mention).

Owner (end of evening): move everything to its own folder, c:\xampp\htdocs\user-and-product, with the
SEO system and credentials; start from there next session. Done 8 Oct 2026: discussion moved, SEO store
rules and tools copied (tools still point at the Printables domain), Search Console key copied, review
skills copied, git initialised (no commit yet), fresh CLAUDE.md.

Open for the next session (owner to answer): 1 pillar candidates, cut/add/reorder; 2 competitor list;
3 sustainable writing cadence; 4 authorise the DataForSEO and Ubersuggest connectors in claude.ai.

## 8 Oct 2026 — second session: sections and topics

Owner:
- DataForSEO may be used, but sparingly; the credits are shared with another project. Claude proposed a
  $5 cap for the first pass (three topics, queue not live, no historical rank calls); awaiting confirmation.
- Main "pillars" as the owner sees them: articles; useful links (other products and resources); books.
  Academy or courses later, not now. Tools and templates possible as further sections.
- Under articles, the coverage goal is the whole of product design and UX (including UX metrics), product
  and project management as a professional body of knowledge (the owner mentioned the PMP persona), and
  the business side (product metrics, measurable outcomes, possibly marketing). A visitor from a startup
  should be able to follow the site from top to bottom and get useful information.
- Launch shape to be discussed afterwards, Printables-style.

Claude's proposal (awaiting the owner's answer):
- Two axes: sections (articles, links, books, frameworks, templates; later academy) become post types;
  topics are one shared taxonomy across all sections, and that is what the SEO pass scores. Topic hubs
  list articles in reading order, then books and tools, giving the top-to-bottom path.
- Topic tree, three domains, fifteen topics: Design (UX research and discovery; usability and UX
  fundamentals; UI, design systems and accessibility; UX metrics and measurement; design process and
  collaboration). Product and delivery (strategy, vision and roadmaps; discovery and prioritization;
  requirements, PRDs and backlog; agile, Scrum and project delivery; stakeholders, leadership and teams).
  Business and growth (product metrics and analytics; business models, pricing and unit economics;
  go-to-market and product marketing; experimentation and growth; strategy and finance for product people).
  Cross-cutting tags: AI in product work; careers.
- Open four or five topics at launch based on the research scores; the rest fill in over months.
- Caution: project management as it meets product work, not PMP exam prep (crowded niche).

Decision (owner, same session): the content types are called "sections". Launch with five: Articles,
Useful links, Books, Tools, Templates. Academy later. Claude suggested "Articles" as the menu item (the
stream) and "Topics" as the browse-by-subject page (the hubs); and asked whether Tools means things we
build (calculators) as opposed to Links (other people's products). Agreed next steps: owner confirms the
topic tree, the PM scope, the $5 cap and the connector; Claude writes the retrofit document; a subagent
re-points the research tools; first research pass scores the fifteen topics and the structured-section
queries; then the launch-shape discussion.

Owner (later, same session): the topic tree must be evidence-based, from SEO data, not fixed in advance
at three domains and fifteen topics; the three domains are a hypothesis only. Each section needs its own
competitor list: link directories (what they list and what is relevant now), book-recommendation sources,
and for articles both publications and individual experts across the three arenas. Asked for an SEO
analysis plan. Claude wrote research/seo/analysis-plan-2026-10-08.md (five phases, about $4.50, proposed
$6 hard cap); awaiting "go" and the connector authorisation.

Owner: include keyword difficulty and trend in the scoring; store every raw output so nothing is queried
twice. Plan amended: difficulty and intent in Phase 4 (already there); trend from the twelve-month volume
history in the same responses plus Google Trends explore for topic head terms (about $0.10); raw storage
rule for both code and connector results written into the plan principles.

Owner shared https://www.bookmarks.design/ as the known example for the Links section. Saved with the
whole hand seed list in research/seo/competitors/seeds.csv (section, domain, type, source).

Owner: cap for this research pass is $5. Links, Books and the other sections each need their own
category tree from the data (bookmarks.design has one flat level; ours may split by domain, then by job).
Plan amended: Phase 2 trimmed to six competitors, Phase 3 widened to 14 seeds and now delivers
research/seo/section-trees-v1.md; estimated total about $4.30 against the $5 cap.

Owner: "go". Start with DataForSEO. The connector is on the account (Printables used it) but this session
reports it as needing re-authorisation and its tools are not reachable; owner asked to re-authorise in
claude.ai. Meanwhile the free Phase 0 work started: tools re-pointed and seed sitemaps pulled (Opus
subagent), GitHub awesome lists mined for the Links inventory (Opus subagent).

Connector re-authorised by the owner; DataForSEO reachable. Balance check (free): $23.74 left of $51 deposited,
nothing spent today. Phase 0 paid part started: 78 page-one SERPs (US) across the five sections, query set in
research/seo/serps/phase0-queries-2026-10-08.csv, run by three Opus subagents in parallel (cap $0.15 each),
raw responses to research/seo/cache/raw/serps-2026-10-08/. Sitemap and GitHub-list subagents still running.

Phase 0 run (8 Oct, evening): DataForSEO live SERP route returned 50000 on every call (their-side fault, API build
stamped 2026-10-08); switched to the standard queue (task_post + task_get), 78 tasks for $0.047. Collected by six
subagents; the templates group stalled at 7/14 (collector tried to copy results out of its own session log) and is
being re-collected by a cleanup agent that also merges the index, builds research/seo/tools/serp_distill.py and the
per-section competitor tables. Free Phase 0 done: 51/73 seed sitemaps inventoried (124k content URLs), 12 GitHub
awesome lists mined (3,130 unique link entries). Early signals: AI Overview on nearly every head query; Reddit on
page one for 13/16 link queries and 11/12 book queries; Amazon 11/12 book queries; four calculator head terms mean
something else (rice, ice, ltv, nps); templates held by Notion/ClickUp/Figma/Creately galleries plus Scribd.

Phase 0 complete (8 Oct): 78 SERPs collected and distilled (research/seo/serps/page-one-2026-10-08.csv,
features-2026-10-08.csv), per-section competitor tables in research/seo/competitors/<section>-competitors.csv and
phase0-competitors-2026-10-08.md; index 140 rows; spend $0.059 of the $5 cap. Seeds fixed: notion.com, ixdf.org,
source label "hand seed". Findings and the Phase 1 question (API credentials for a code client) in chat and below.

Owner provided DataForSEO API credentials (saved to .local/dataforseo.env, git-ignored, verified: balance $23.68).
Explainer delivered: research/explainers/phase0-serp-findings-2026-10-08.html (folder + README created; the owner
wants this format for every phase). Phase 1 started with a code client (Opus subagent): keyword ideas for about 40
seeds, US, 250 rows each, volume >= 100, soft cap $2 for the phase.

Phase 1 run (8 Oct, late): research/seo/tools/dataforseo_client.py (REST, raw caching, index rows, budget guard) and
harvest.py written; keyword_ideas for 42 seeds, $1.738, 7,706 keywords. Mistake: keyword_ideas sorted by volume returns
category-wide head terms, so about 870 keywords are on topic; 26 candidate topics in keywords/topic-candidates-2026-10-08.csv
(surveys, design systems, requirements and user stories stand out). Spend $1.80 of $5; balance $21.94. Proposed to the
owner: re-run with keyword_suggestions (phrase match), about 30 seeds x 150 rows, about $0.90; awaiting yes/no.
Owner: go for the re-run. Phase 1b started: keyword_suggestions, 30 seeds, 150 rows, cap $1.10; re-cluster into v2 with subtopics.

Phase 1b done: keyword_suggestions, 30 seeds, $0.654; 2,440 keywords; combined on-topic set 3,255; v2 tree in
keywords/topic-candidates-v2-2026-10-08.csv (25 topics, 45 subtopics; summary in keywords/phase1b-summary-2026-10-08.md).
Findings: surveys, OKRs, user stories, requirements and prioritization are standalone topics; "ux/saas/product metrics"
barely exist as phrases; template demand runs through most product topics; retention leans HR. Issues: variant
inflation of raw volume (use adjusted), noise in 4 seeds, jobs-flag bug swallows "jobs to be done". Spend $2.45 of $5,
balance $21.28. Proposed: Phases 2+3 (~$1.50) then Phase 4 (~$1); awaiting go/stop.
Owner: go. Phases 2 and 3 started in one subagent run (cap $1.20): bulk traffic for all competitor domains, ranked keywords
for the four strongest article competitors, section demand via keyword_suggestions (17 seeds), stock evidence from the
free inventories, draft research/seo/section-trees-v1.md; also fixes the jobs-flag bug for "jobs to be done".

Phases 2+3 done ($0.567; total $3.02 of $5; balance $20.72). Traffic tiers: Omni Calculator and Goodreads ~10M/month,
GeeksforGeeks, Coursera, Figma > 1M; NN/g 63K, Smashing 17K (tier C). Ranked keywords for productplan, atlassian,
coursera, amplitude (500 each, but volume-sorted so mostly off-topic; "gap" means head terms unowned). Section demand:
user story templates and sample-size calculators clearest; "rice score" drowned by the Rice Purity Test; books have no
difficulty data. Draft research/seo/section-trees-v1.md. Phase 4 started (cap $0.60): Google Ads volumes on the queue,
SERPs per topic head term on the queue, Google Trends 5-year, scored table, research/seo/topic-tree-v1.md draft.

Phase 4 done ($0.292; whole pass $3.31 of $5; balance $20.42): 84 units scored (25 topics, 45 subtopics, 14 section
categories); research/seo/topic-tree-v1.md with a launch shortlist of eight; Google Ads volumes are the same series as
Labs (not an independent check); Trends over five years shows 45 of 68 head terms rising, so the 12-month dip was
seasonality; every head term has an AI Overview; only 6 of 68 have a weak page one; the three domains hold on competitor
evidence (arena overlap 2-4%). Owner_fit column left empty for the owner. Explainer for Phases 1-4 being built;
next-session note written (research/discussion/todo/next-session-2026-10-09.md).

Owner asked whether the clustering missed related keywords. Manual review of all 6,587 unassigned phrases (free):
204 recovered (largest miss "electronic accessibility", 74K/month, thrown out by an over-wide noise word); four small
new candidates (visual design principles, customer experience, market research, ux writing); shortlist top eight
unchanged, product strategy may climb. Files: keywords/review-unassigned-*.csv, review-unassigned-summary-2026-10-08.md,
tools/cluster_rules_patch.md. Now re-clustering and re-scoring to v1.1 (subagent, cap $0.15). Owner wants a better
explainer afterwards: the score as the main subject, each metric in one line with a picture, worked examples, and the
supporting keywords and SERP evidence shown per topic.
Owner: AI is missing from the tree and must be in it. Cause: the only AI seed noised out in Phase 1 and was dropped
in 1b. Fix in progress: 16 phrase-match AI seeds (ai product manager, ai ux research, ai prototyping, ...) added to
the v1.1 run as an "AI in product and design work" topic with sub-topics; cap raised to $0.60 for that run.

v1.1 done ($0.238; total $3.55 of $5; balance $20.19): 30 topics, 47 subtopics; AI topic in (44 on-topic phrases,
score 53.8, rank 28; conclusion: a cross-cutting tag, not a launch pillar); prioritization and product roles swap
the top two; product strategy first outside the eight; UX writing enters at 7 on missing-difficulty data (formula
weakness: missing KD read as 0 for non-book units; fix next session). Files: research/seo/topic-tree-v1.1.md,
keywords/topic-scores-v1.1-2026-10-08.csv, topic-evidence-v1.1-2026-10-08.csv. Score-first explainer being built to
replace the Phases 1-4 page.

## 9 Oct 2026 (early, same sitting) — intent as a first-class dimension

Owner: intent must be considered everywhere, not only in the score: what people mean when they type a phrase decides
the article format, the section it belongs to and the categories. Trigger: the product roles topic (73.8) carries
job-hunter demand ("product owner position", "vacancies", "remote product manager") and 30 of 86 phrases are
navigational; the jobs filter missed position/vacancy/remote. Decision: (1) per phrase, keep the source intent label
plus our finer reading (define, learn-how, compare, template/example, tool/calculator, career, brand); (2) per topic,
an intent mix and a format suggestion; (3) in the score, career and navigational demand removed before measuring,
practitioner intent weighted; (4) the sections inherit intent (template -> Templates, calculator -> Tools, best-tools
-> Links, books -> Books); (5) each article title and format follow its phrase group dominant intent. v1.2 re-score
running (free); explainer to be refreshed with a "what people mean" section.

Owner (same sitting): intent must be considered deeply per pillar so each makes sense as a body of articles; example
prioritization, whose demand is dictionary lookups ("another word for prioritization") and personal task lists, with
only "prioritization frameworks" being ours. Added to v1.2: a "dictionary" intent, a field_fit value per phrase (yes /
partial / no, rules plus a manual review of each unit top 30 phrases, keywords/field-fit-review-2026-10-09.csv), demand
counted only on field-fit practitioner phrases, and article_capacity per unit (distinct phrase groups that can carry an
article; thin under 5 cannot be a launch pillar). Explainer rebuilt from scratch as one report (no patching), no
horizontal scroll anywhere, ending with the whole tree, the four section trees and launch waves.

v1.2 done (free; spend still $3.55 of $5): dictionary intent, field fit (1,816 phrases hand-reviewed, 385 changed),
wider career flag, article capacity per unit. Surviving demand 2.45M of 4.33M. Prioritization (general) parked (2,390
of 153,570 survive); prioritization frameworks folds into product strategy. Tree: about 210 articles possible (product
98, design 71, business 41). Waves on the page: W1 UX research, product strategy, product management, requirements/PRD,
user stories, AI (81 articles); W2 UX/UI, design systems, stakeholders, pricing, IA, OKRs (32); W3 CX, design thinking,
UX writing, agile, growth, A/B (44); W4 accessibility, GTM, visual design, retention, personas/journeys, market
research (27). Report rebuilt from scratch at the same URL (347 KB, no horizontal scroll). Progress page live at
research/progress/ with chime. Files: seo/topic-tree-v1.2.md, keywords/topic-scores-v1.2-2026-10-09.csv,
topic-evidence-v1.2-2026-10-09.csv, field-fit-review-2026-10-09.csv, phase4c-summary-2026-10-09.md.

Report redesigned (owner: "too much at once"): summary screen first (three tiles, six Wave 1 cards, the complete
tree of all 91 units with subtopics and section categories, the four decisions), everything else in folded sections;
no size cap on local pages; no horizontal scroll. Session closed about 01:30, 9 Oct. Open for next session: the owner
fit ratings, yes/no on analytics, web design and project management, the launch size (Wave 1 is 81 articles as
proposed), the first section categories; then owner_fit re-score, retrofit document, content model, first commit and
GitHub repo.

## 9 Oct 2026 — third session

Owner: colour-code the tree on the report summary by how easy it is for us to rank (score plus difficulty), an icon
before each category name, the name text coloured, and a hover or tap card with the score and a plain-language
meaning (for example what "product owner and product manager roles" really is). Bands defined: easy (green,
KD < 15 and score >= 60), promising (teal), takes work (amber), hard (red, KD >= 35), parked (grey), no data.
Subagent run "tree-badges" in progress; progress page tracking it.

Owner: the research tree is too granular for a site; reader first, SEO second; short names, two levels at most,
merge overlapping topics (personas and journey maps into UX research; visual design principles into UI design;
accessibility with no subcategories; new product launch into product strategy; value proposition, user stories and
acceptance criteria into product discovery; agile into project management); small things like retention become a
group of 3-5 articles, not a category. Decision: simplified tree with 11 categories (Design: UX research, UX design,
UI design, Design systems, Accessibility; Product: Product management, Product strategy, Product discovery, Project
management (your call); Business: Product metrics, Growth and pricing), article groups inside, AI and Careers as
tags. Two judgment calls for the owner: Requirements as its own category or inside discovery; the "your call" trio.
Subagent building research/explainers/tree-simplified-2026-10-09.html plus the mapping CSV and
research/seo/tree-simplified-v1.md; progress page tracking it.

Decision (owner, 9 Oct): the site tree is one navigable level. Three domains (Design, Product, Business) are menu
groupings with one hub page each, not a level articles attach to. Eleven categories hold the articles (Design: UX
research, UX design, UI design, Design systems, Accessibility; Product: Product management, Product strategy, Product
discovery, Project management if the owner says yes; Business: Product metrics, Growth and pricing). No second-level
categories: the 49 groups are headings on the category page and a planning label, never pages. A group that grows
past five or six articles may earn a curated series page later, by hand. URLs: /category/article/, domain hubs at
/design/ etc. Taxonomy: domain terms with category children, article attaches to the category.

Owner: Business needs more than two categories. Scan of all harvests (free) found dashboards, vision/mission, customer
satisfaction (NPS, CSAT), product operations, productivity tools, and almost nothing on business models (never seeded).
Decisions: add Product marketing (go-to-market, product launch, positioning, PLG) and Leadership and teams (hiring guides
by role, interview questions, team structure, stakeholders and change moved from PM, vision and mission, career ladders);
dashboards -> UI design group; satisfaction metrics -> Product metrics; business models and unit economics -> Growth and
pricing; product operations -> Product management; productivity tools -> a Links category. 13 categories; groups stay as
writing cues. New groups carry scan estimates, "not scored yet"; a $0.30 targeted pull can score them later. Tree v1.1
being built by the subagent.

LLM Council run (owner asked to stress-test the whole approach; skill installed from aiwithremy/claude-skills-llm-council
into .claude/skills/llm-council, git-ignored). Five Opus advisors, five peer reviews, chairman verdict; everything saved in
research/discussion/council/ (framed question, advisor responses, anonymised set and key, reviews, verdict-2026-10-09.md).
Verdict in short: keep the research (store, intent labels, SERP and difficulty as a filter, template shares, trends, the
tree as a 210-article backlog); change the launch: owner_fit as a gate, flat /article-slug/ URLs, no category shown until
3 articles, no domain hubs yet, project management / web design / analytics = no, Requirements stays inside discovery;
launch about 12 pieces (4 signature, 6 template-led, 1 search-data report, About + Start here), 3 categories (UX research,
Product discovery, Product strategy), Articles + ungated Templates only, Books month 2, Tools month 3-4, Links after 20
articles; two pieces a week; LinkedIn main channel; checkpoints at day 14, week 3, week 6, month 3, month 6. One thing
first: the owner lists the 20 pieces only they could write. Owner has not yet responded to the verdict.

Council 2 (AI skills as a Templates product): five advisors, five reviews, chairman; verdict in
research/discussion/council/verdict-ai-skills-2026-10-09.md. Verdict: build ONE, on the PRD template page, as a third
format beside the blank template and a worked example; both modes (interview, "check my draft") from one method;
readers never see "skill"; must pass a blind test against a plain "interview me and write a PRD" prompt (5 PMs) before
it ships; credit in the file header and a deletable output footer; CC BY 4.0; "before you paste" confidential-data box;
never promise Word/PDF; cap 6 extra owner hours; stop rules at week 6 (returned outputs + 50 copies or 3 peer mentions);
at most 3 by month 3; the library, repo, chain and paid tier only if the first passes. Fact fix: "prd template" is
2,900/month (KD 6), PRD-template group about 4,500; the 18,100 in the first verdict was wrong and is now corrected.

Owner: the skill library (interview and "check my draft" skills across product, UX research and UX/UI design, one per
template page, growing out of the articles) goes on the back burner. Not refused: parked until the PRD interview passes
the blind test and the launch set is live. Candidate list recorded in this entry for later: PRD, user stories,
acceptance criteria, roadmap, OKR set, competitive analysis, prioritization scoring; research plan, interview script,
survey questions, usability test plan, persona, journey map; heuristic evaluation, design critique, accessibility
checklist, UX writing review (the design ones mostly as reviewers).

Mockups phase started (owner): plain HTML in research/mockups/ before WordPress. Decisions: editorial magazine
direction; one accent, light and dark; references Smashing, NN/g, Lenny/Substack, bookmarks.design/uxtools.co, and
tigerdata.com blog post as the single-article model. Page list in research/mockups/README.md. Owner wants to start
with the logo.

Logo direction (owner, 9 Oct): bold and geometric; the name itself as the mark (wordmark-led); reference Tiger Data,
whose logo reads majestic and authoritative ("if this information is found here, it must be legit"). Target feel:
weight and restraint, heavy geometric wordmark, generous space, one deep accent, nothing playful. Reference capture
(screenshots, logo, type and colour notes) going to research/mockups/references/tigerdata/.

Owner (9 Oct): the brand name is "userandproduct", one word, as in the domain; not "User and the Product". Logo
wordmarks to be rebuilt accordingly (default: lowercase domain-style with a lighter "and"; uppercase variant for the
masthead). Docs that say "User and the Product" are the project working title only.

Logo round 1: twelve concepts (A-L) at research/mockups/logos/index.html, one-word name, review board fixed after a
layout bug. Owner felt the UP-with-underline looked familiar; asked for ten more, each a different art direction and
unique, with originality checks. Round 2 (M1-M10: Swiss grid, Bauhaus, brutalist, art deco, Japanese mon, blueprint,
notary seal, optical pattern, isometric plinth, line-and-dot) building in research/mockups/logos/round2/ by a fresh
subagent that does not see round 1 until done. No illustration skill installed; Figma connector offline this session.

Tooling research (research/mockups/tooling-research-2026-10-09.md): no external skill adds much to the installed
logo-design skill; the gap is tooling. Installing: resvg-py (SVG to PNG), skia-pathops + uharfbuzz (booleans, kerning),
SVGO via npx; fontTools already present turns OFL typefaces into paths (OFL allows logos from outlines). Subagent
installing, fetching six OFL fonts to research/mockups/fonts/, writing tools/wordmark.py, render.py, brand_assets.py,
building a type board at research/mockups/logos/typeboard/, and adding a project-tooling reference to the skill.

Logo round 2 feedback (owner): M9 liked (monumental) but its mark does not land; M1 feels seen before; M2 the u is
good, the p does not gel; M3-M7 no; M8 not legible; M10 does not land. Owner liked the blue/black/white of round one A
but says that is a preference, NOT a constraint: keep experimenting with other colours. Round 3 requested: ten more,
unique, authority; built with the new tooling (real typefaces as paths).

Logo round 3 (N1-N10, real typefaces): owner liked none. Diagnosis from the owner: the repeated miss is the feeling,
they look like software or startups; it should feel like an institution or a publication. References that feel right:
The Economist / FT (masthead), Stripe / Linear (bold wordmark), Harvard Business Review (monogram block), Mastercard /
Medium (abstract symbol), Tiger Data. Final form wanted: an abstract mark plus the name; the symbol must be abstract,
not an object. Round 4 to follow with a reference board first.

Owner feedback on round 4: the weighted ring (P6) is "kind of nice". Owner shared a Reiki symbol diagram (saved to
research/mockups/references/owner/) as inspiration: likes the spine, two struts and three rings; dislikes the cross
at the top. Next round: derivatives of that structure (without the cross, changed enough to be unrecognisable, with
a 16px reduction), plus developments of P6.

Owner on round 4: most marks look like derivatives of other companies; the weighted ring (P6) resembles Oyster HR.
Cause: originality checks were text searches by description. Fix: image-aware checks (look at marks in the same
visual family and industry), a "closest existing logos" row on every board, no plain disc-with-gap variants; applied
to the running round 5 and recorded as a standing rule.

Owner on round 5: likes Q3 (tree of three) and Q4 (braced tripod). Round 6 brief: every option is a solid disc with
the figure hollowed out as negative space, like the Tiger Data mark; three or four carry the tripod from the owner
symbol (Q3 and Q4 as references); the rest from imagination. Image-aware originality checks stay mandatory.

Round 6 feedback pending; owner shared four new sketches (four tilted tiles; stacked triangles; triangle cluster;
triangle diamond), saved under research/mockups/references/owner/. Round 7 brief: derivatives of both families, many
options, including carved-in-disc versions; one to be picked from this round. Two subagents in parallel:
round7/tiles/ and round7/triangles/.

Owner (9 Oct, after rounds 6 and 7 and the hub): wordmark FINALISED as the P8 setup: Inter Display Bold, lowercase
"userandproduct" one word, tracking -25 (tight), single ink colour, beside the mark at about 1.4x cap height. Mark
shortlist: P3, P5, Q3, R4, R5, S5, P8, all to be rebuilt with the P8 wordmark but keeping each own colours. Two new
requests for the same page: (1) a Tiger Data-style disc with a sharp-featured human head in silhouette cut out
instead of the tiger; (2) T8 modified: remove the bottom-left and bottom-right triangles so the rest read as a
sphere, set inside a disc with the sphere bottom merged into the disc bottom, with enough spacing to survive at
favicon size. All on one shortlist page.

LOGO DECISION (owner, 9 Oct 2026): the mark is S5 from round 7 tiles (four filled tiles of two sizes at 45 degrees),
with the final wordmark (Inter Display Bold, lowercase userandproduct, tracking -25). Next: a colour board of ten
themes, each shown as lockup light and dark, header strip, favicon 16 and 32, LinkedIn avatar, OG image, single colour.

Owner on the colour board: no multi-colour marks; press red (T04) stays; the old ink blue and signal blue did not
fully land (signal blue dark shade good, light shade not). Board being rebuilt: ten single-colour themes, red first
then nine blues (midnight, navy, royal, cobalt, Mercedes petrol, steel, Prussian, sapphire, signal) with separately
tuned light and dark shades; wordmark black on light, off-white on dark; the blue is only the mark.

LOGO FINAL (owner, 9 Oct 2026): S5 mark (four tiles of two sizes at 45 degrees) in signal blue, light #2B46A0 / dark
#8EA2FF, wordmark Inter Display Bold lowercase "userandproduct" tracking -25, black on light, off-white on dark.
Asset pack to research/mockups/final-logo/ (SVG masters, monochrome black and white, PNG sizes, favicon set, OG,
LinkedIn, header strips, brand sheet). Exploration (rounds 1-7, shortlist, type board, hub, colour board, feeling
board, owner sketches) archived to one zip under research/archive/ and the working folders removed; kept: fonts,
tools, the Tiger Data reference, tooling notes.

Git: first commit 53f7f7a (everything incl. the archive zip) and the cleanup commit pushed to
git@github-realyogan:realyogan/userandproduct.git (owner created the repo; identity as Printables).

Final lockup refinement (owner, 9 Oct): mark centred midway between the cap band and the x-height (+5.30 SVG units,
alignment C) and the mark-to-word gap widened to 0.40 of the mark height (40.74 units, about 116px at 2400). These are
now the build.py defaults; pack regenerated and committed. research/mockups/final-logo/alignment.html kept as the record.
Wordmark tracking changed to 0 (the typeface as designed) after a comparison of -25, -10, 0 and +10; owner picked 0.
Final spec: Inter Display Bold, lowercase, tracking 0; mark mid-aligned; gap 0.40. Pack regenerated and committed.

## 9 Oct 2026 — mockups: the article page

Owner: start the mockups with the reading (article) page. Building three variants on one sample article (a PRD
how-to): A sidebar (Tiger Data layout, sticky TOC), B magazine (Smashing, serif body), C reader (Substack, narrow).
Owner addition: design ad areas into every layout under Google rules (the fixed three-ads limit was removed in 2019;
now: ads must not exceed content, must be labelled and distinguishable, no covering content; Better Ads Standards:
mobile ad density under 30%, no pop-ups, no large stickies) plus the owner rule of at most three ad units in the
viewport at once; each variant reports its max-in-view and mobile density. Owner also asked to use the Impeccable
and Taste design skills; both are real (pbakaus/impeccable, Apache 2.0; Leonxlnx/taste-skill, MIT) and are being
installed into .claude/skills/ for the second pass.
Owner picked article variant A (sidebar). First fixes: the sticky rail ad overlapped the template block (rail must
stop at the body end); add a featured hero image (16:9, editorial illustration, light and dark) and related-card
thumbnails. Owner will give further changes one by one before the Impeccable and Taste pass.
Owner: variant A follows the Tiger Data structure exactly: title full width, byline row (avatar, name, read time,
share right), rule, then left rail (utility button, tag chips, numbered table of contents), centre (hero then body),
right rail (ads). Date: Claude advised keeping a quiet "Updated <month year>" for search and trust; kept as one
removable element. Header logo 236px wide on desktop (owner tried it in the inspector).
Owner additions to the logo pack: monochrome black-on-white and white-on-black PNGs (flattened), and a gradient
social set (white mark and lockup on a signal-blue gradient) as JPEGs in Instagram, LinkedIn, OG and X sizes; the
gradient is for social backgrounds only, never the site. Building through build.py; commit after.

Owner asks (9 Oct, article mockup): a code block component in the Tiger Data style (dark card, three dots, language
label, copy button, light syntax colours) applied automatically to every code block; built as shared CSS plus a tiny
vanilla highlighter, mapping to the WordPress core code block via the theme. Owner also wants, later, a writing
rules skill: article tone, format and structure; to be briefed by the owner; the skill-creator skill is available
for it and for the PRD interview skill from the council verdict.
Owner (article A): after the body, switch to full container width: the template block, then "// RELATED" with three
large illustration cards (tag chips, bold title), newsletter, footer; remove the author box (byline carries it).
Code block built (dark card, dots, language label, copy, built-in highlighter). Illustration frame generator in
progress with three light/dark treatments to choose from; spec to become a rule once confirmed.
Owner on the illustration frame: illustrations will often be plain PNGs, so the frame cannot rely on CSS theming
inside the SVG; it must be a fixed image design that works on both the white and the near-black page. Candidates to
compare as PNGs on both backgrounds: a dark card always (as Tiger Data thumbnails), a neutral mid card (cool and warm),
the light card as control. Do not copy the Tiger Data frame; keep the dot-grid idea, design our own background and
edge. Rule to be written once the owner picks.
Owner: no illustration frame at all (no card, notches, rules or chrome). An illustration is just the image: a flat
neutral background that sits on both white and near-black (candidates: muted slate, warm stone, cool mid, soft
cool-light), a subtle dot grid, the diagram, a small quiet mark in one corner. Same PNG in both themes. To be
written as research/mockups/illustration-rules.md and later a skill.
Owner: illustration backgrounds are a palette, bright colours allowed, not one grey: six approved backgrounds (signal
blue, cool mid slate, red-orange, mustard, deep green, ink), each with its own ink, muted, dot and tint colours tested
on both page colours; one background per illustration, chosen for meaning or variety; same PNG in both themes.
illustration-rules.md being rewritten with the palette table.
Owner: illustration backgrounds are open, any colour except black-ish and white-ish; the generator derives ink,
muted, dots and tints from the background and checks contrast; the six-colour table and the "ink" preset go; an
explainer gallery of twelve diagram types on twelve hues is being built at research/mockups/article/explainers.html.

Owner (9 Oct, evening): FORGET the earlier illustration palette rules. Foundation is the Printables site
(rockpaperprint.com, code in c:\xampp\htdocs\Printables): eight pastel tile tints with a dark dot grid (main.css
--tint-blue #dbe8fb, green #dcefd8, pink #fbe0e6, purple #e8e0f7, yellow #fff3c4, teal #d7f0ee, peach #fde3d0,
slate #e0e6ee; dots rgba(29,27,22,.13) 1px on a 12-14px tile; assignment by printables_tint_class(index)). Rules:
one tint per article (all its explainers share it), chosen by rotation so articles differ; related thumbnails use
their own article tint; same PNG in both themes. Generator, gallery, article A and illustration-rules.md being
rebuilt on this.

Writing style (owner, 9 Oct): the house voice is an experienced teacher explaining calmly from experience; simple
enough for a 10-year-old without losing the hard part; a guide with guardrails, not a template (judgment pieces stay
judgment pieces; steps only when the reader performs steps); written for both the reader and the scanner (headings
tell the story, one idea per section, pictures where they do the work, landing spots, density per screen). Analysis
of the owner references in research/discussion/references/writing-style/analysis-2026-10-09.md; skill being written
at .claude/skills/writing-style/ with the skill-creator skill.
Owner: the Printables origin-lock explainer is THE bar (analogy that anyone grasps, then an exact "in real life"
mapping, one picture per idea). Added to the skill as a named device. Series idea logged: "technical things for
non-technical people", numbered, one concept, one analogy, one picture, one mapping each, long run (a hundred days).
Owner showed the explainers to a friend: "this is interactive, I can learn things like this". Added to the skill
as the goal: a static piece should feel interactive because the reader does something on every screen. Mockup
backlog: a series page that reads like a course index (numbered, with progress), as in the lesson sidebar the owner
shared.

Thumbnails (owner, 9 Oct evening): 35 reference thumbnails saved under research/mockups/references/blog-thumbnails/.
Two studies running: (1) a style board grouping them by visual style and how they are made, with a feasibility
verdict per group (code alone / code plus a source image / external image tool) proven by four demonstrations
made here in our palette; (2) research into skills, libraries and image-generation services (Recraft, Ideogram,
Flux, local options) that would make thumbnails repeatably, with cost and licence, written to
research/mockups/thumbnail-tooling-research-2026-10-09.md.

Owner (thumbnails): the "grained grid" background is two distinct options, a square grid and a dot grid, both over
the grain; the thumbnail rules must name them as a choice. Style board built at
research/mockups/references/blog-thumbnails/index.html (ten groups, verdicts, four demonstrations); recommendation:
flat vector default, light grid diagrams for explainer-led pieces, pixel icons for tools and templates; dithered
photos and character drawings occasional with outside help; dark styles out of the main rotation.

Thumbnail decision (owner, 9 Oct): nine code-made styles (flat vector on a square grid; flat vector on a dot grid;
pixel icons; icon sequence; typographic cover; dark line diagram; dark glow diagram; light grid diagram; particle
field) plus one conditional style (dithered or halftone photo, only when the owner supplies a photo). Character
drawing dropped. Dark backgrounds allowed for thumbnails (not for explainers). Style rotates per article on its own
cycle, independent of the tint rotation. Skill being written at .claude/skills/thumbnail-images/ with a working
generator (research/mockups/tools/thumbnail.py) and a gallery of all ten.
Owner correction (thumbnails): backgrounds are NOT the Printables tints (those are for explainers only); thumbnail
colours are chosen freely per image, saturated and high-contrast in the spirit of the reference set, "contrast and
curiosity, not clickbait"; the brand on a thumbnail is the full lockup, not the mark alone. Skill, generator and
gallery being regenerated.
Owner: add a bright particle-field variant (particles on a vibrant background) as a tenth code-made style; the
photo style becomes number 11, still conditional.
Owner: the thumbnail style pick is fit first, then rotation: classify the article by kind, keep only the styles
that suit that kind, rotate among those, no two neighbours alike by style or colour, record the reason.
Owner: thumbnails may use more than one colour family per image: colour schemes (mono, duo at the complement,
trio at split-complementary or triadic, analogous), accents only on the highlight that matters, contrast computed
on every pair, at most two accents, lockup stays black or white. Not always, but available; gallery to show it.
Owner: multi-colour must be restrained, as in the references: mono by default, duo when one element must stand out,
trio rarely; an accent on at most about a fifth of the subject; never on decoration; if in doubt, fewer colours.
Thumbnail skill finished (9 Oct): eleven styles (ten code-drawn plus the conditional photo style), gallery at
research/mockups/references/blog-thumbnails/gallery.html, generator research/mockups/tools/thumbnail.py, skill at
.claude/skills/thumbnail-images/ with references and evals. Owner saw the gallery and corrected two things: (1) the
dark glow diagram and the particle fields must be multicolour examples, since the gallery is what the skill draws
from: the glow's bloom and lit part take the accent, and the particle stream carries the colour (the one exception
to "never colour decoration"); the glow sample is duo on midnight because trio came out pink and green; (2) the
full logo on every image, never the mark alone, large enough to read: hero lockup 220 px (18% of the width, the
legibility anchor, "perfect"), thumb 120 px (a fifth of the width, so the thumb is the hero at half size; the first
try at 240 px was far too large). Duo, not trio, on mid-bright grounds, where two deep accents fall under
contrast. Owner confirmed all these decisions are captured in the skill.

Council on the publishing system (9 Oct, evening): the owner asked for proposal 2 to be councilled for gaps and
improvements before discussing its questions tomorrow. Verdict saved at
research/discussion/council/publishing-system-2026-10-09/verdict.md (inputs beside it). Short form: the proposal
spends ten agents on the cheap part and gives the owner's judgment ten minutes per article; rebuild around the
owner as author in fact (agents interview, shape and check); two a week not six; prove the belt on one
owner-written baseline plus three test pieces through plain prompts before any agent file; hard rules against
invented first-person detail and a confidentiality check on every story; four making agents not seven; measure
authority signals not 90-day rank; add a newsletter; park reels, the public newsroom series and the gap-map
dataset until month six. Owner has not yet responded to the verdict.

Session 10 Oct 2026. Yesterday's work committed and pushed (bc46bbf). Owner reviewing proposal 3.
Performance desk (owner, 10 Oct): on a fresh domain there is nothing to score for the first quarter (index
coverage within days, impressions after four to eight weeks, clicks after months), so the campaign manager's
duties switch on by data, not by calendar. Three modes, same agent: coverage mode from day one (planned versus
published per category and pillar; thin pillars, fewer than about five supporting pieces; orphan pages and
missing internal links; Search Console index coverage; rival sitemap diffs as backlog candidates tagged with their
source; authority signals: links, mentions, direct and returning visits); early-signal mode once pages have
impressions (indexed but not showing, impressions without clicks, striking-distance terms at positions eight to
twenty); performance mode once a page has about a hundred impressions over 28 days (the v2 duties: scoring,
nudges, refreshes, pruning). Rival feed guard, owner agreed: the manager flags gaps with evidence, the explorer
judges fit against the tree and the owner's experience, only then a pitch card; the backlog carries a source
field. Early Sunday status is mostly a coverage report. To be folded into the proposal with the fourteen answers.
Explorer (owner, 10 Oct): add a pitch kind, "the take": a response to something notable just published, where the
value is the owner's disagreement, counter-example or the part they missed; links to the source; not me-too. Card:
what they claimed, what experience says instead, the title (states the take, never teases; promise paid in the
first screen). Story slot answered on the spot; no take, no card. Fast lane proposed: a take approved on Sunday is
drafted that week and takes the next scheduled slot, at most one a month. Measured on authority signals (shares,
mentions, links), not rank. Sources: rival sitemap diffs, the owner's reading, what the owner forwards.
Owner: takes must be fact-based, never disagreement for its own sake. Rule: a take earns a slot only when the owner
has lived the opposite, has evidence the source lacks, or the source left out a case that changes the answer.
Mostly agreeing is fine ("they're right, here is the part they skipped") or no card. Verifier adds a check for
takes: the source's claim is quoted accurately and in context, no straw man.
Owner: the competitor sitemap pull is inspiration for the explorer, read together with the tree and the keyword map.
Each new rival URL lands on one of three outcomes: gap (we have nothing and demand exists: ordinary pitch card,
source noted), take (a claim the owner's experience answers: take card), or nothing (covered or no demand: logged
and dropped, never resurfaces). The Performance desk runs the pull and the diff only; the judgment is the explorer's.
Owner: the explorer compares three things, what rivals wrote, what we already published, what the keyword map wants,
and pitches an angle, not just a topic ("we have the how-to on X, nothing on when X fails, two ways to write that").
Each pitch card names the existing piece it sits beside, so no two of ours compete for one query and the new piece
links into the old from day one. "Already covered" is a normal, cheap outcome.
Owner asked to update the proposal with the morning's points so it can be read again. Decision: proposal 4
(new file, pattern of one file per revision), reading the same browser key as proposal 3 so the saved answers carry
over. Edits: the take as a fourth idea kind with its rule and the straw-man check; rival URLs land on gap, take or
nothing; angle not topic, cards name the piece they sit beside; "what you forward" as a seventh explorer source;
campaign manager in three modes switched by data (coverage from day one, early signal, performance), which puts it
in the first build (eleven agents, twelve with reels) and moves only its later modes to build step 7; backlog gains
kind and sits-beside fields; pitch card gains kind, sits-beside and the quoted claim for takes; questions 15 (fast
lane) and 16 (performance-mode threshold) added.
Explorer, two passes (owner question): the sitemap gives only the address, so the explorer opens every new page for
title, description and headings (first pass, cheap triage), then reads the candidates in full (second pass), a take
always in full; blocked or paywalled pages get the RSS title and summary only and the card says so. To be written
into source (b).
Owner: books as a backlog gateway. Eighth explorer source, "a book you name", run on demand: list the book's ideas
(famous books from knowledge; lesser-known ones need the table of contents or the owner's notes), turn each into a
reader question, check the keyword store then one paid batch under the cap, cards with source "book: title", rest
logged so a book is not mined twice. Guards: no summaries or wholesale frameworks, the article teaches the idea in our
words with the owner's experience, credits and links to the book; no invented quotes or page numbers. Series idea:
one book, one idea per piece, tested against practice; feeds the later books directory with affiliate links.
Owner: third backlog gateway, "your brief": the owner says in chat, any day, "we should write about X" with the rules
they know (example: dashboard and table design, numbers right-aligned, text left-aligned). The main session puts it
on the board at once, source "your brief", the owner's rules saved word for word as the seed. The explorer does the
legwork (reader question, keyword fit, top five and what they miss, each rule checked against sources; where sources
disagree the card shows both and the owner's rule stands as "from experience"). It skips the queue, not the card: top
of the next pitch meeting, or straight into the window on "now"; the card still sets outline, expectation and story.
The owner's rules form the spine of the piece, in the owner's order, research fills in the why and the examples.
Proposal answers (owner, 10 Oct). Q1 pace: start smaller, two or three a week, until the process has gelled and the
gaps are found; then ramp toward one a day, possibly two a day later. Noted for the proposal: the ramp is gated by the
owner's own time (stories at the pitch meeting, review week at 30 to 40 minutes a draft: about 5 to 7 hours a month at
two or three a week, 15 to 20 hours at one a day), so the condition for ramping is "process gelled and review time per
piece down", not a date.
Q2 water marks: scale with the pace, about a month and a half of output: 20 at two or three a week (as now), 50 at one
a day, 100 at two a day; bottom mark about sixty percent of the top (12, 30, 60). A formula tied to pace, not fixed.
Q3: a category opens only as a cluster. The explorer may open any planned category when it can put at least seven or
eight planned pieces on the board for it at once, to be scheduled over the coming windows; one idea never opens a
category; no thin categories floating around. The campaign manager's thin-pillar threshold becomes seven or eight.
Q4: the pitch card is enough; no stop at the brief. The writer starts, everything is published to local WordPress
first, the owner gets the list of links, reads, suggests changes, and only the owner's "push" moves a piece live.
(Implies Q11: review in local WordPress.)
Q5: weekly sitemap pull, Saturday night so the diff is ready for Sunday.
Q6: the explorer reads everything that needs no login: rival sites and feeds, newsletters (Substack, Beehiiv, Medium
feeds), Hacker News (public API), Reddit (public subreddit feeds or JSON at low volume, a source of reader questions
in their words). LinkedIn cannot be read by script (login wall, no feed, against its terms); LinkedIn voices come in
through "what you forward" or through their own newsletter feeds. The list of subreddits and newsletters is approved
once by the owner.
Q6 refined (owner wants no routine copy-pasting): a dedicated newsroom mailbox, subscribed once by the owner to the
newsletters worth following, read by the explorer on its weekly pass over a standard mail connection; LinkedIn
newsletters arrive there by email with full text, which is the legal route for that part of LinkedIn. Ordinary
LinkedIn posts: not readable by API, bot accounts or driving the owner's logged-in browser break the terms and risk the
owner's account, advised against. LinkedIn voices followed through their own newsletter, blog or Substack feeds plus
Google Alerts on names delivered to the mailbox. Forwarding stays as the side door for stray posts only.
Correction on LinkedIn newsletters: subscribing needs a LinkedIn account (no email-only box); the notice email carries
title, excerpt and link, not the full text; the newsletter edition itself is a LinkedIn article with a public address,
usually readable without login (short feed posts are the gated ones). Setup: the owner subscribes from their own
account, one mail filter forwards LinkedIn newsletter notices to the newsroom mailbox, the explorer fetches the public
article from the link; a gated edition is marked "excerpt only" on the card.
Verified (10 Oct): a LinkedIn newsletter edition from the owner's notice email was fetched logged-out, with and without
tracking parameters, status 200, full body (about 6,100 characters). Newsletter editions are readable without a login;
the explorer strips the tracking parameters and fetches the public article. Short feed posts remain gated.
Back burner, before launch (owner, 10 Oct): how LinkedIn newsletter notices reach the newsroom mailbox without giving
access to the owner's personal email. No fake or anonymous profile (against LinkedIn's terms). Routes to research: a
mail filter in the owner's mailbox forwarding only LinkedIn newsletter notices to the newsroom mailbox; a secondary
address on the owner's LinkedIn account if notifications can go there. Also: research a follow list of product, UX and
business newsletters (LinkedIn and elsewhere), fifteen to twenty with subscribe links, since LinkedIn has no
newsletter directory (help page: search, My Network trending and recommendations, profile Interests, feed only).
Q7: the scorecard comes at the start of each build window, not weekly; scorecards mean little in the early months. One
command (placeholder "/go") opens with what happened since the last window, then the planned pieces as cards.
Owner: a newsroom app, project-management style, as the front end: agents update data files only (backlog, cards,
scorecard, window plans, decisions), one local app page (plain HTML and vanilla JS on XAMPP, no build step) reads them
with views for the board by status, the pitch cards with approve, kill, change and the story box, the scorecard, and a
timeline of past windows; the owner's clicks and text are saved as a decisions file the agents read; each window keeps
a snapshot for replay. No agent generates HTML for the owner to read. Grows out of the tree and build-plan app idea and
replaces backlog.html; becomes part of build step 1.
Q8: pitches per meeting equal the slots in the block the window feeds; a killed card is replaced on the spot by the
next card from the top of the backlog; "publish later" parks the card with a note for a later meeting; hence the
backlog always holds more than a window needs.
Q9: the window size follows the cadence. Rolling schedule with two settings the owner fixes later (block length, e.g.
ten or fifteen days of publishing; window length, two or three days). Example with ten-day blocks: Dec 28-30 builds
Jan 1-10, Jan 7-9 builds Jan 11-20, Jan 18-20 builds Jan 21-30. Rule added: review in publishing order, each piece
approved before its own date; the publisher never pushes an unapproved piece, a late read slides that slot only.
Q10: three or four a week for the first couple of weeks, then one a day once the process has gelled (ramp conditions
as in Q1).
Q11: review in the app, confirm in local WordPress. The app renders the draft with the article page design (mockup A)
so the owner reads it as it will look; corrections are marked on the paragraph in the app and saved as data the writer
and editor act on; once the owner is happy the publisher creates the real post in local WordPress, the owner confirms
once, and that confirmation sends it live on its date. Folder files are never the owner's reading surface.
Q12: the owner's input is direction, not stories. The card's "story slot" becomes "your note", a plain text box for
how the piece should go (write it this way, lead with that, drop this); a story is an optional extra and many cards
will have none; no first-person claim the owner did not give. Voice through chat when the owner wants, transcribed and
written into the data.
Q13: killed cards go to an ideas bin, their own section of the board, kept with the owner's reason; when the backlog
runs thin the explorer may retry one from a different angle. Nothing deleted.
Q14: deferred. Posting will go from a separate LinkedIn page the owner will create, not the profile. Social pipelines
are decided one by one after the article pipeline is settled; the LinkedIn pack is parked until then.
Q15: no fast lane. The rival feed is inspiration; the usual result is a piece in a different perspective on the same
topic, valid only when none of the top pages cover it (the "better" kind, judged by the learning sentence). Real takes
are rare, two to four in fifty, and ride the normal window.
Q16: the campaign manager is a director, not a switch. It always holds the site's age, the full publishing history and
the keyword data, decides itself when per-page scoring means something (the hundred-impression figure is its rule of
thumb, not an owner setting), and gives direction forward: which categories and rising terms deserve the next windows,
handed to the explorer through the board. Question 16 is withdrawn.
Launch plan (owner, 10 Oct): as with Printables, launch with a full-feeling site, then drip. Target about fifty
articles live before the public announcement, plus a books section and a few templates (scoped separately), then two
or three a week. Agreed shape: fifty pieces in six or seven deep categories (seven or eight each, per Q3), not thirteen
thin ones; the owner's time is the gate (about 30 hours of notes and reviews for fifty), so the stock may launch at
thirty to forty with the rest as the first drip buffer; the first window stays small (three or four pieces) to prove
the belt; no backdated dates, the established feel comes from depth and finish (full category and series pages,
start-here, author page, books shelf with the owner's takes, templates, newsletter, no empty corners); soft launch two
weeks before the announcement with the stock scheduled across those weeks, three or four a day, so dates are real and
spread and indexing is watched before the audience arrives.
Dates in the UI (owner): no sort-by-date anywhere, lists are just lists ordered by series or importance; the article
shows only a quiet "Updated <month year>", present for its own sake and never a focus.
Proposal 5 written (research/explainers/publishing-system-proposal-5-2026-10-10.html): every decision of the day, the
owner's role as direction, rolling windows, the app, three doors, the director, the launch plan, a decisions table.
Council on proposal 5 run (research/discussion/council/publishing-system-2026-10-10/: question, advisor-responses,
peer-reviews, verdict). Verdict in short: keep the shape; the central gap is that nothing is required to supply the X in
the learning sentence once the owner gives direction rather than stories, so add a seed on every card (two or three
practice questions answered by voice in minutes, traced on the card; cards labeled seeded or synthesis, synthesis capped
at about a quarter and kept out of the ten flagship launch pieces); widen the hard rule to every invented specific, add a
close-paraphrase check, and have the editor list the positions a draft takes for the owner to approve or strike; reorder
the build to run the making desk first on three hand-written cards with timing and a cold reader, then the app (needs a
PHP save endpoint and stable paragraph ids), with WordPress, theme, plugin and section pages in parallel and domain and
hosting bought now; a principles file from day one; leading-signal expectations and a ramp gated on fixes per draft; set
the stock from the first window (expect thirty to forty), soft launch spread over three or four weeks at one or two a day
because four reviewers raised Google's scaled-content policy; buffer and slipped-date rule; linking pass per window.
Owner has not yet responded to the verdict.
Owner on the council verdict (first response, 10 Oct): the launch stock stands at fifty as the bar, ten articles in each
of five categories, plus a templates section and a books section, all present on the public launch day; the site is never
announced with a handful of posts. Pages may be indexable from the first one (sitemap and Search Console on day one,
dripped at about two a day, nobody told) while the stock builds; "live to Google" and "launched to people" are different
days. The first window measures the owner's real minutes per piece and sets the date fifty is reached, not the target.
Owner clarifies the launch (10 Oct): "launch" means the site goes live and is indexed with all fifty articles present at
once (not dripped out beforehand), plus the books and templates sections; the LinkedIn page opens about a week later with
the announcement; from then on build windows prepare a block in two or three days and the publisher schedules it to open
one a day. On the scaled-content question: the policy targets pages made to manipulate rankings rather than help readers,
not the count on launch day or the method; a fifty-page launch of substantive, reviewed articles with author and about
pages is an ordinary launch (Printables precedent); the real defense is the owner's judgment visible in each piece and no
invented specifics, which is the council's central finding.
Owner (10 Oct): build a rulebook from Google's spam policies so no agent produces content for publishing's sake, and
check everything planned against it. Four Google pages read in full and saved (research/discussion/references/
google-policies/, owner's screenshot beside them). Rulebook written as a skill: .claude/skills/search-policy/ (one
test per page: why our readers would want it if search did not exist; scaled-content rules: every page carries the
owner's judgment, nothing publishes unreviewed, no stitching or paraphrase, no reason-less pages; originality and
accuracy questions; who/how/why; honest titles and no stuffing; links: sponsored marking, never bought or traded;
one URL, no doorways; real dates; never query Google by machine; a ten-point checklist for checker and publisher).
Check written at research/discussion/google-policy-check-2026-10-10.md: the plan is clear on launch size, pace,
bylines, the gate, dates, the books shelf, tooling (API only, no Google scraping) and the domain (no history);
changes: synthesis pieces conflict with the policy's own low-effort example (recommend every page carries a seed,
brief or note), the owner's oversight must be real per piece, close-paraphrase check added, title rewrites bound to
honest titles, template pages must be real pages, tag/date/author archives noindex, affiliate links sponsored with
disclosure. Two decisions for the owner: synthesis pieces at all; a "How this site is made" page.
Owner on synthesis (10 Oct): up to a quarter of pieces may be synthesis, but synthesis means a fresh take written from
understanding (own structure, examples, reasoning), never a summary and never paragraphs stitched from sources, which
is what Google's scaled-content and scraping policies describe. The owner's feedback on the draft is the oversight for
those pieces; a seed is not required on every card. The other three quarters carry a seed, a brief or the owner's note.
Rulebook updated accordingly.
Owner decisions (10 Oct, afternoon): no "How this site is made" page. Order of work: finalize the design of the whole
website first (every section's mockup, look and feel), then content creation; domain, hosting and WordPress come after
the mockups are final. The council's build order is parked behind that. Committing everything from today.
Owner: yes to the editor's positions list. After a draft is done the editor lists every position the piece takes (eight
to fifteen lines); the owner marks each keep, reword (with the words) or strike before reading the prose; reworded
rules go into the principles file; the list sits on the card in the app above the preview. For synthesis pieces this
is the owner's judgment entering the piece. To be folded into the proposal with the seed, the synthesis rule, the
search-policy rulebook and the parked build order when the publishing system comes back after the site design.
Second policy pass (owner, 10 Oct): Google's guidance on using generative AI content and every page it links to read in
full (rater guidelines PDF sections 2.4, 3.2, 3.4, 4.6, 5.1, 5.2, 7; ranking systems guide; title link, snippet,
structured data intro and general guidelines, Article markup, alt text, search gallery, image metadata, page
experience, SEO starter guide). Rulebook rewritten (.claude/skills/search-policy/SKILL.md, twelve sections, a
twelve-point checklist); sources vendored into the skill. New rules: metadata reviewed like body text (title tag, meta
description, alt text, structured data shown in the app preview); structured data configured and validated (Article
with Person author linked to the author page, ISO dates, three image ratios, ProfilePage, BreadcrumbList, WebSite,
Organization, Rich Results Test per template change, URL Inspection per page); alt text method and diagrams explained
in body text (goes to the illustration rulebook); no filler, answer near the top; titles are main content; paraphrase
spot-check through the paid API, never Google; no interstitials, newsletter as an in-page box; site diversity reason
for sits-beside; YMYL-adjacent pieces marked with primary sources; honest book takes with disclosure; URL and link
rules; IPTC tag not needed for code-drawn images. Check appended to research/discussion/google-policy-check-2026-10-10.md.
Owner: structured data and metadata are basic WordPress plus Rank Math work. Agreed; noted that the install session sets
Rank Math once (author schema to the author page, tag and date archives noindex, organization logo, real modified
dates), alt text and meta descriptions are written per piece and shown in the app preview, and validation (Rich
Results Test per template change, URL Inspection per page) is part of the publisher's live-page check.
Owner (10 Oct, later): read the whole rater guidelines PDF and every article the generative-AI page links to, and make
the rulebook good enough to reuse on other projects; also delegate reading and other simple work to Opus or Sonnet
subagents and keep the thinking in the main session (saved as a standing preference). Correction to the earlier note:
the first pass had read about a quarter of the PDF; the full 182 pages have now been read in the main session, and a
subagent is reading the second ring of linked pages (technical requirements, content policies, breadcrumb,
organization, profile page, site names, sitelinks search box, FAQ and HowTo availability, image licensing, Merchant
Center AI policy, Rich Results Test, image SEO, canonicalization, sitemaps, robots meta, interstitials, Core Web
Vitals, outbound link qualification). Rulebook to be rebuilt as a general guide plus a site-specific layer, with a
build to-do checklist beside it.
Third policy pass done (10 Oct): the whole rater guidelines PDF read in the main session; the second ring of linked
pages read and extracted with quotes by a subagent (research/discussion/references/google-policies/
extract-second-ring.md). Rulebook rebuilt for reuse on other projects: .claude/skills/search-policy/SKILL.md is the
general guide (fifteen sections, twelve-point per-page checklist), SITE.md the userandproduct.com layer (author of
record, seeded and synthesis pieces, no disclosure page, who runs which rule, indexing and feature decisions,
affiliate and ads, licensed API), and research/discussion/todo/search-policy-build-checklist.md the build to-do
(design, WordPress install, app and data, agent rulebooks). New rules from the full read: no question farms from
"people also ask", site purpose must match the About page, no hidden disclaimers, verifiable author claims only,
answer up front, real dates, ads never disguised, comments are main content, custom 404; from the second ring:
noindex not robots.txt for archives, sponsored on affiliate links, snippet controls also govern AI Overviews input,
FAQPage/HowTo/sitelinks box retired, site name markup on the home page only, no placeholder author image, validate
live. Check doc appended. Nothing new for the owner to decide.
Site design phase started (owner, 10 Oct): build the whole site's mockups on article A, one page at a time: home,
category page, About, terms of service, privacy policy and the other pages, bringing everything together. Home page
first, being built at research/mockups/home/ on the shared mockup.css, article A's header and footer, the tree's three
domains and thirteen categories, thumbnails from the generator, copy in the house voice; no dates or "latest" labels;
newsletter as an in-page box; ad slots within the layout rules.
Owner (home page): do not copy Tiger Data or any existing site; references set the feel, the layout and section ideas
must be our own. Passed to the builder mid-run; standing rule for every page from here on.
Owner (article A, 10 Oct): the right rail is not only ads: three stacked blocks, "More in <category>" (three or four
titles from the same category) at the top, the ad unit in the middle, "New on the site" (three pieces, chips and
titles, no dates shown) at the bottom. Being applied through article/build.py in parallel with the home page build.
Home page mockup built (10 Oct): research/mockups/home/ (http://localhost/user-and-product/research/mockups/home/).
Masthead with one h1, the desk (featured piece plus the author's margin note and two secondary cards), three shelves
with thirteen topics drawn as stacked books sized by planned-piece count (original idea), nine pieces numbered by
importance with one in-feed ad, a five-step Start-here rail, author strip, Templates and Books teasers, newsletter box,
shared footer. Twelve generated thumbnails across all ten code-drawn styles. .chip and .chips moved into the shared
mockup.css. Article A's rail rebuilt with "More in <category>", the ad, "New on the site". Owner to review and give
changes one at a time; noted for review: the lone in-feed ad in the middle column, the uneven stacked shelves.
Owner on the home page (10 Oct): too fancy. The home page is just the latest published articles and links to the
other parts of the site; no "pieces I would hand a colleague", no Start-here path, no stacked shelves. Think about how
the functionality works: everything must come from WordPress automatically (latest posts, category lists, section
links), nothing for the owner to curate. Rebuilding in place: masthead line, latest articles (newest larger, then a
grid, no dates), topics as three plain category lists with counts, a row of section links, newsletter, footer.
Standing rule for every page from here on.
Owner (article A, 10 Oct): the rail's "More in <category>" list goes small and compact with small thumbnails; "New on
the site" leaves the rail (rail = compact list plus ad); the bottom "// Related" section becomes the new-articles
section with three large cards, named in one constant ("Just published" for now; alternatives "Fresh from the desk",
"New this week", "Latest"; the owner will pick a name).
Owner: link all the mockup pages together so the site can be navigated as one. Link map set: home at mockups/home/,
article A, category page at mockups/category/ (next to build), sections at mockups/sections/{books,links,tools,
templates}.html, pages at mockups/pages/{about,privacy,advertising,contact}.html; pages not yet built get a minimal
placeholder in the shared shell from mockups/placeholders.py; mockups/index.html becomes the site map with status per page.
Home page rebuilt simple and automatic; article A rail compact with small thumbnails, "// Just published" row at the
bottom in Related's place; all mockup pages linked through mockups/placeholders.py (shared header, footer, link map)
with ten placeholder pages and a site map at research/mockups/index.html (8 built, 10 placeholders). Noted for the
owner: at 1200 to 1439 px the article rail is 160 px wide, so the compact list's titles wrap to several lines; the fix
would be to stack thumbnail above title at that width.
Owner (home, 10 Oct): remove the hero text (h1 kept only visually hidden for search and screen readers), remove the
"Latest articles" heading so the cards start right under the leaderboard, remove the Topics section entirely, and
redesign the section-links block (Books, Templates, Tools, Links) without the "Also on the site" title. Being applied.
Owner: remove the newsletter sign-up from the home page for now (not needed yet). Passed to the builder mid-run.
Owner (article A, 10 Oct): remove the category chip above the title; make the three-column layout flexible for laptop
screens (1366x768, 1440x900 and the like): right rail fixed at 300 px from 1200 px, left rail fluid 200 to 260 px,
reading column within its measure; if the three cannot fit, the left rail folds into the compact table of contents
rather than squeezing. Verification at ten viewports, light and dark, with screenshots and a width table. Being applied.
Article A tuned (10 Oct): chip removed; fluid grid: 1024 to 1199 two columns with the rail block after the body, 1200
to 1279 the left rail folds into the compact contents and the right rail keeps 300 px, from 1280 three columns
(left 200 to 244, reading 560 to 720, right 300); rail ad now 300x600; verified at ten viewports light and dark with
screenshots and a width table in article/shots/README.md.
Owner (10 Oct, evening): the site so far lacks a bit of character, reads like a corporate site; authority yes, but a
slight bit of character would help; changes to come later. No major changes now. Restructure: bring every mockup page
into one self-contained folder, research/mockups/option-1/ (home as index.html, article.html, category, sections,
pages, own css, js, img, assets, build scripts, shots, sitemap), so a later redesign can be option-2 beside it. Move
in progress; links fixed, no visual changes.
Mockups moved into research/mockups/option-1/ (10 Oct): index.html (home), article.html, sitemap.html, category/,
sections/, pages/, css/, js/, assets/ (logo, favicon, fonts), img/, shots/, build/ (placeholders.py as the single
header and footer source, build_article.py, build_home.py, image and shot scripts, variants B and C and the explainer
gallery kept for reference). All links relative within the folder, 791 checked, none broken. Old home/, article/,
category/, sections/, pages/ folders removed. Site: http://localhost/user-and-product/research/mockups/option-1/
Owner (10 Oct, evening): does not like the logo; back to the drawing board. The S5 four-tile mark and Inter Display
wordmark are no longer final. Questions put to the owner before any drawing: what is wrong (mark, wordmark, colour,
feel), what it should feel like (three words or references), mark plus name or name alone, colour open or blue.
Owner on the logo: the mark is bland and has no presence; as an Instagram avatar it is not attractive, and alone (as
in a thumbnail corner) it looks like a speck of dust. Next round to judge every candidate at avatar, favicon and
thumbnail-corner size first, then the header; marks need mass, a recognisable silhouette and character. Proposed: a
direction board of eight to twelve marks at those sizes, light and dark; originality check on the shortlist; one
direction refined. Open: colour (blue or open), wordmark (Inter Display or open). Waiting for go.
Owner: none of the shortlisted marks had the "oh nice" feeling. Proposed method change: the owner sends ten to fifteen
logos from any field that gave that feeling; derive what they share as the brief; then a board of twelve genuinely
different ideas (not variations), each with the reason it could delight; judged at avatar size first. Waiting for the
owner's references or a go.
Owner shared a stock mark (thick blue ring with a chunky cursor crossing it, two-tone with a lighter fold) as the kind
of visual appeal wanted, saved at research/discussion/references/logo-round-2/; not to be used or copied, a derivative
with the same qualities: mass, one clear idea, two-tone fold depth, works as a circle avatar. Owner asked to restore the
deleted exploration folder for inspiration only and to start fresh without repeating it: research/mockups/logos/
restored from the archive (1,472 files, hub at research/mockups/logos/hub.html). Round 2 started at
research/mockups/logo-round-2/: twelve different ideas judged at avatar, favicon, thumbnail corner and header sizes,
blue two-tone by default with three colour alternatives, wordmark kept for fair comparison.
Owner (logo): wants an app-icon feel: not everything inside a circle, but from a distance it should grab attention the
way a round app icon or an Instagram-style rounded square does; a contained, filled, high-contrast form with mass.
Passed to the round 2 builder: most ideas container-led (filled circle or squircle with the two-tone fold), shown at
110 px circle and rounded square as the first test, two or three free-standing for comparison.
Owner: add a couple of rocket-based ideas to round 2 (each with its own twist, not the generic startup rocket). Passed to the builder.
Owner: a new logo hub for the new exploration, round by round, separate from the old one which stays for reference. Set up as research/mockups/logo-2/hub.html with round-1/ as the current board. Passed to the builder.
Owner: the foundation stays authority and trust; character and app-icon feel must still read as a serious publication. Passed to the builder: an authority check line under every idea, the foundation first in the hub brief.
Owner: two rounds at a time. Round 1: ten options from the owner's references (ring-and-cursor appeal, rockets,
app-icon feel) plus original ideas. Round 2: letterform marks on U and D (taken as U with D and U with P, since the
name is user-and-product; owner to correct). Both being built under research/mockups/logo-2/ with the new hub.
Logo exploration 2, round 1 built (10 Oct): research/mockups/logo-2/round-1/ (ten marks: orbit, completed frame, key
person, folder bust, breakout rocket, passenger rocket, switch, nib, bookmark, clasp; seven container-led, three free;
two-tone blue with coral, teal and oxblood alternatives; authority check on each; old-round avoid list) and the new hub
research/mockups/logo-2/hub.html. Main-session read: presence solved; several read as library icons (key, upright
rocket, bookmark, switch, nib); brand ideas in the orbit, the frame, the breakout rocket, the clasp. Round 2
(letterforms) in progress.
Logo exploration 2, round 2 built (10 Oct): research/mockups/logo-2/round-2/ (ten letterform marks on U, D and P:
shared stem, turned U to D, split ring up, D holds U, cut coin, two-hook U in green, stacked UP, lit D in a tile,
ampersand in vermilion, folded-corner u in the wordmark). Main-session read: strongest at avatar size 02, 05, 06, 08;
10 has the nicest idea but fades at 32 px; 01, 03, 04 carry too much; 07 thin. Suggested shortlist across both rounds
for the originality check: R2-02, R2-05, R2-06, R2-08, R1-01, R1-02, R1-05. Waiting for the owner's reaction.
Owner on rounds 1 and 2 (10 Oct): R2-05 the cut coin "kind of okay", R1-01 the orbit okay, "like is a strong word";
round 1 lacked monochrome (white on black, black on white), which is important; no rockets; the folder bust looked like
a stamp; the switch makes no sense; the bookmark is nice but not strong and looks seen before; do not limit a round to
ten. Round 3 started: sixteen to twenty marks in three groups (the coin evolved, the orbit evolved, fresh ideas), every
mark shown in monochrome and single colour as well as two-tone, same first-row avatar test, authority check on each.
Owner: every mark on a board must show its previews in context: monochrome, Instagram profile, LinkedIn company page, browser favicon tab, thumbnail corner, header lockup. Passed to the round 3 builder; standing rule for later rounds.
Owner: each logo on a board gets a short plain 'what it means' paragraph the owner can say to a friend (brand meaning in everyday words). Passed to the round 3 builder; standing rule.
Owner: not everything U and D; the Tiger Data mark's cleanliness and authority (a figurative silhouette cut from a solid disc, one idea) is the bar, as a standard not a shape. Round 3's fresh group becomes mostly figurative negative-space silhouettes; letters a minority. Passed to the builder.
Owner on round 3 (10 Oct): shortlist R3-03 cup and ball (wants it tilted about 45 degrees left so it reads as a
person raising a hand, a U and a hint of a D), R3-04 speech mark (likes it; the bottom tail must be more prominent, at
small sizes it reads as a cricket ball), R3-05 square coin and R3-14 shelf; the rest dropped; the figurative Tiger
Data-standard group still wanted. Round 4 = refinement families of the four plus two or three figurative candidates.
Round 3 was renumbered by the figurative pass after the owner had reviewed it (square coin removed, shelf moved to R3-16). Builder told: restore the square coin for round 4, use names in the hub, add a mapping note on the board; rule: never renumber a board after the owner has seen it.
Owner: round 4 must also bring eight to ten entirely fresh marks, not only refinements of the four. Passed to the builder.
Round 4 built (10 Oct): 33 marks: cup and ball family (45 degrees recommended, reads as raised hand, U and a hint of
D), speech mark tails (still thin lit crescents, not yet solid), square coin and shelf proportion variants, three
figurative carry-overs (at the screen, doorway, raised hand), eight fresh marks (lens, dividers, lamp, rook, anvil,
signpost, funnel, block) that read as library icons. Main-session read: live candidates are the tilted cup, the speech
mark once its tail is solid and breaks the outline, the square coin and the shelf. Round 3 closed with a numbering map
note and the no-renumbering rule. Waiting for the owner.
Owner (10 Oct, later): rounds 1 to 4 all rejected ("all of it"). The owner drew their own mark in Illustrator and put
it at research/mockups/Logo-3/Logo.svg: a solid disc with a rounded diamond (head) and a wide curved band (shoulders,
also a smile) cut out; black mark only. It holds at 32 px. Asked for: the other versions, at least ten colour options,
three or four gradient options, and previews of everything (browser favicon, Instagram, LinkedIn icon and mark). Being
built in Logo-3/ with a clean master (true negative space), monochrome, lockups, exports and a board.
Logo 3 board built and committed (10 Oct): research/mockups/Logo-3/ (clean evenodd master identical to the owner's
drawing, twelve colour options with contrast on white and dark, four gradients labelled social-only under the house
rule, side and stacked lockups, previews for every option, exports for the blue option). Builder flag: with the band's
ends turning down under the head, the figure can read as a frown, more on dark grounds.
Owner on Logo 3 (10 Oct): the header lockup's mark is too small; use the previous final pack's proportion (mark as
tall as the wordmark's full height, vertically centered). Likes G01 signal blue to cobalt for now. Wants twenty more
options: five flat blues, five blue gradients, five vibrant flats, five vibrant gradients, appended with stable
numbering. Being built.
Logo 3 updated and committed: side lockups rebuilt to the previous pack's geometry (disc 1.4 cap heights, centred
between cap height and x-height, gap 0.40 of the disc), before-and-after on the board; twenty options appended
(C13 to C22 flat blues and vibrants, G05 to G14 blue and vibrant gradients) with contrast; gradients still labelled
social-only under the house rule. Owner currently likes G01 signal blue to cobalt.
LOGO DECIDED (owner, 10 Oct 2026): the owner's own mark (solid disc with a head and a curved band cut out) in option C17
Electric blue, flat: #2E5BFF on light, #7DB0FF disc in dark mode, white figure where opaque; Inter Display Bold
wordmark, lockup geometry as the previous pack. Pack being built at research/mockups/final-logo-2/ and wired into
option-1 and the thumbnail generator; final-logo stays as the previous pack. Open question for the owner: whether the
site accent (signal blue #2B46A0 in the tokens) should become electric blue to match the mark.
Final logo pack 2 built and committed (10 Oct): research/mockups/final-logo-2/ (masters, lockups, favicons and app
icons with manifest, social set light and dark, brand sheet at research/mockups/final-logo-2/brand-sheet.html); wired
into option-1 (lockups, favicons, logo aspect ratio in both mockup.css files) and the thumbnail generator (lockup
source now final-logo-2; a bug fixed where the generator dropped the mark's transform and holes). Still old lockup
baked into previously generated thumbnails in option-1; regenerate when the accent is decided. Accent question open.
Owner: update the image generation rules (thumbnails, explainers) to the new logo and regenerate. Rollout running: skills, illustration rules, generators, option-1 images, thumbnail gallery.
Logo rollout committed (10 Oct): thumbnail skill and references, illustration rules, thumbnail, illustration, demo
and hero-art generators all on final-logo-2; the mark's holes are filled with the flat ground colour under a solid
black or white lockup on every image; 54 option-1 images, 12 explainer figures, 44 gallery images and 4 demos
regenerated with identical subjects and colours. Left as history: final-logo/, logos/, logo-2/, Logo-3/, old eval
outputs. Open: the site accent token (#2B46A0) versus the mark's electric blue, and the rotated-square pull-quote marker
that echoes the old tiles.
Owner: explainer figures carry the full lockup, not the mark alone. Being applied: illustration rules and generator, lockup at a fifth of the width bottom-right, quiet strength checked for legibility, all explainer figures regenerated.
Explainer lockup applied and committed (10 Oct): full lockup a fifth of the width, bottom-right, 32 in, 60 percent
(legible at 60 on the lightest tints, about 4.8 to 5:1), holes filled with the tint, clear zone 16 units; rules and
illustration.py updated; 12 gallery explainers, the two article figures and three figure-style related thumbs
regenerated.
Owner on explainer figures (10 Oct): figures are not only flowcharts and boxes; any picture that explains (analogy
scene as in the origin-lock explainer, object, before and after, map, sequence, matrix, chart); and the text is
barely legible even at full size (labels were 18 to 19 units on a 1200 canvas, about 11 px in the 720 px column; the
white text in the matrix's blue box fails). Fix in progress: a "kinds of picture" section in the rules, type floors
of 27 units for labels and 24 for notes in Inter (not monospace), a 4.5:1 check for text on fills, new drawing
primitives for scenes and objects, every figure regenerated, two non-diagram figures added to the gallery.
Owner: no rules on what to draw; the illustration rules cover only the background tint, the dots, the lockup, type floors and the canvas; the picture is whatever the article demands. Passed to the builder.
Figures fixed and committed (10 Oct): illustration rules reduced to the fixed things with one sentence that the picture
is whatever the article needs; type in Inter Medium 27 units for labels (16 px at the 720 px column) and Inter
Regular 24 for notes, floors enforced, labels wider than their box stop the build, text as outlines so no font is
needed; 4.5:1 check on every fill (lowest 4.56); new primitives (shapes, twelve line icons, badges, caption band);
all 17 figures regenerated; two range examples added (restaurant ticket analogy, PRD sheet object).
Owner: explainer figures must not be locked to the tint's family (the ticket figure's flame came out green); apply the thumbnail colour-scheme rule: mono by default, an accent on the part that matters with restraint, contrast checked. Being applied to rules, generator and figures.
Owner: no need to regenerate the figures for the colour change; only make sure the rules and generator do not restrict colour. Passed to the builder.
Explainer colour rule committed (10 Oct): the tint-family lock is gone; mono by default, an accent where meaning needs
it under the thumbnail restraint rule (one accent, two rarely, never on decoration, about a fifth of elements at most),
contrast checked on every pair (3:1 shapes, 4.5:1 labels); generator takes "accent": fire, warning, success, a hex or
a hue, with fire drawn as an orange body and a yellow core because yellow alone fails on pastel tints. Figures not
regenerated, per the owner.
Owner: the illustration rules fix only the foundation (the tint background with the dots) and the lockup bottom-right;
no "mono by default", no accent counting, no "where needed"; the only requirement on the picture is that it matches
the background it is drawn on. Rules rewritten; the generator's accent limits being removed (contrast checks stay).
Owner: image file names (and alt text) follow the SEO brief: the article's SEO slug from the target phrase plus words
that say what the image shows, set by the researcher or SEO reviewer, never generic. Written into illustration-rules.md
and the thumbnail skill.
Committed (10 Oct): illustration generator with no accent caps (any element kind can take a colour; 3:1 shapes and
4.5:1 labels still enforced; adjacency notes only); rules foundation-only; SEO image names in both rule sets.
Owner (10 Oct): use the Satoshi family from Fontshare for the mockups instead of the current type (Inter text and Fraunces). Being self-hosted under research/mockups/fonts/satoshi/ with its licence and switched in both mockup.css files; the logo wordmark (Inter Display Bold) and the figure generator's Inter unchanged for now.
Owner: the Satoshi change is a plain font swap in the CSS only; logo, images and generators untouched; no scale retuning yet.
Satoshi applied and committed (10 Oct): both mockup.css files load Satoshi Variable (roman and italic, 300 to 900) and
map --font-display, --font-ui and --font-body to it; Fraunces and Inter rules left unused; preloads updated. The ITF
Free Font License 2.0 forbids redistributing the files (including via repositories), so the font files are
git-ignored and only the README is tracked; the GitHub repo is public. Builder's tuning notes: Satoshi's x-height is
about 11 percent smaller than Inter's and it sets about 8 percent narrower, so body 18 px reads like 16 px (19 to 20
px body and a 22 px deck would restore the look); small labels at 14 to 15 px look light. Owner to review the swap.
Owner (Satoshi swap): small headings bolder (700 to 800); body paragraphs get a little letter spacing (owner liked about 0.05em in the inspector; to be set within the system). Being applied in the mockup CSS.
Type tweaks committed (10 Oct): tokens --fw-h3 750 (h3, card titles, section names), --fw-label 700 (section labels),
rail titles 600, h1 and h2 stay 700; --tracking-body .03em on paragraphs, lists, decks and captions (.05em read
spaced out), --tracking-ui .01em on 13 to 15 px interface text; chips left at 500.
Owner (article byline): remove the avatar; 'By' plus the author name with no brackets (Yogan for now, one constant); all byline parts in one colour, the name one weight bolder. Being applied.
