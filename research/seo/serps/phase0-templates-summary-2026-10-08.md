# Phase 0 SERPs: Templates section (US, desktop, page one), 2026-10-08

Source: DataForSEO standard queue, task_get/advanced. Distilled files:
`page-one-2026-10-08-templates.csv` (116 organic rows), `features-2026-10-08-templates.csv` (14 rows).
Index rows 261008-SP-001 to 014 are merged into `../cache/index.csv`. The consolidated files for all
sections are `page-one-2026-10-08.csv` and `features-2026-10-08.csv` (rebuilt by `tools/serp_distill.py`).

## Collection status: 14 of 14 collected, none pending

First pass (7): prd template, product requirements document template, user persona template, product
roadmap template, customer journey map template, user interview script template, usability test plan
template.

Second pass, same day (7, re-collected from the finished tasks, free): okr template, sprint retrospective
template, lean canvas template, user story template, competitive analysis template, ux research plan
template, prioritization matrix template. All raw files are in `research/seo/cache/raw/serps-2026-10-08/`
and parse as valid JSON with the expected task ids.

Rule note: the second-pass rows count scribd.com as weak (the agreed weak-domain list includes it). The
first 7 rows of the group features file were left as written and do not count Scribd; the consolidated
`features-2026-10-08.csv` applies the rule to all 14 (prd template weak_count 3, product requirements
document template 2, usability test plan template 1).

## Top page-one domains (organic, 14 keywords, 116 organic results, 80 distinct domains)

| domain | count | keywords | type |
|---|---|---|---|
| notion.com | 9 | 9 | saas (template gallery) |
| figma.com | 4 | 4 | saas (Community files) |
| atlassian.com | 4 | 4 | saas (Confluence templates, Agile Coach) |
| clickup.com | 4 | 4 | saas (template listicles) |
| scribd.com | 4 | 4 | platform (document host) |
| pinterest.com | 4 | 3 | platform |
| youtube.com | 3 | 3 | video |
| creately.com | 3 | 3 | saas |
| miro.com | 2 | 2 | saas |
| mural.co | 2 | 2 | saas |
| smartsheet.com | 2 | 2 | saas |
| nngroup.com | 2 | 1 | publication |
| okrinstitute.org | 2 | 1 | education |
| ones.com | 2 | 1 | saas |
| gist.github.com | 2 | 2 | platform |
| dhavalthakur.medium.com | 2 | 2 | platform |
| reddit.com | 2 | 2 | forum |

Position 1 by keyword: Notion on 5 of 14 (prd, product roadmap, usability test plan, sprint
retrospective, competitive analysis); single first places for Atlassian (user story), NN/g (ux research
plan), Smartsheet (prioritization matrix), Figma (user interview script), okrinstitute.org (okr), and
one-off sites (anotherwrapper.com, andacademy.com, dllgroup.com PDF, meta-group.com PDF).

## Features

- AI Overview: 12 of 14 (not on customer journey map template or sprint retrospective template). 4 of
  the 12 are asynchronous placeholders with no text or references (user interview script, usability
  test plan, lean canvas, ux research plan).
- Images pack: 12 of 14, often position 1 and very large (up to about 40 images). People also ask: 10.
- No featured snippets, no popular_products (shopping) units, no knowledge graph. YouTube appears only as
  organic video results (ux research plan, prioritization matrix, product roadmap).
- AI Overview references (keywords citing them): atlassian.com 8, aha.io 5, miro.com 5, youtube.com 4,
  asana.com 4, notion.com 3, canva.com 3, mural.co 3, then productschool.com, figma.com, reddit.com and
  smartsheet.com 2 each. Miro, Canva, Asana and Aha! are cited much more often than they rank.
- weak_count of 3 or more: 1 of 14 (prd template: Scribd, LinkedIn, Medium). Six more keywords have 2.

## Who holds these SERPs

Template galleries and work-management vendors (Notion, Figma, Atlassian, ClickUp, Creately, Miro, Mural,
Smartsheet, ONES) are the largest group and hold first place on 8 of 14. Below them the field is
fragmented: document hosts (Scribd, PDFs on agency, university and bank sites), Pinterest, GitHub gists,
Medium posts and small SaaS listicles. Authority publishers are rare: NN/g (ux research plan, twice),
Mountain Goat Software and Agile Alliance (user story), Reforge (sprint retrospective), Stratechi
(prioritization matrix). The UX and agile templates (ux research plan, user story) are the only ones where
expert sites lead; the business templates (lean canvas, competitive analysis, okr) are held by thin pages.

## Odd things

- Notion ranks with non-English locale URLs (/pt/, /zh-tw/, /he/, /en-gb/) on US queries, and Todoist with /sv/.
- Scribd PDF pages rank on 4 of 14 keywords; Behance ranks with a ?locale=ru URL.
- lean canvas template: positions 1 and 7 are PDFs (meta-group.com and a squarespace subdomain), plus
  Scribd at 8. Strategyzer and Ash Maurya's own site (leanstack) do not rank organically.
- competitive analysis template: two Pinterest results and an "OpenClaw skill" page on page one; HubSpot,
  Canva and Miro appear only in the AI Overview. The intent is marketing more than product.
- okr template: okrinstitute.org holds two positions with an English and a /fr/ URL.
- customer journey map template: a financial firm's PDF (dllgroup.com) ranks first.
- sprint retrospective template: ones.com holds two positions with posts dated "7 days ago".
