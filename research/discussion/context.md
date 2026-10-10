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
