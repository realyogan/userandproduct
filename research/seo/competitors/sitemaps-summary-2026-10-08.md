# Seed sitemap pulls, 2026-10-08

Phase 0 inventory of every domain in `seeds.csv` (73 unique domains across five sections). Free:
robots.txt and sitemap XML only, no pages fetched. Tool: `tools/sitemaps.py` (fetch, classify, index).

Files:
- Per domain: `competitors/sitemaps/<domain>-sitemap-2026-10-08.csv`
  (domain, url, lastmod, first_segment, slug, slug_tokens, year, content)
- Across domains: `competitors/sitemaps-stats-2026-10-08.csv` and `competitors/slug-tokens-2026-10-08.csv`
- Raw: `cache/raw/sitemaps-2026-10-08/` (one JSON per domain, plus `fetch.log`)
- Index: 62 rows `261008-001` to `261008-062` in `cache/index.csv` (skipped domains are not indexed)

## Outcome

| Status | Domains |
|---|---|
| ok | 51 |
| blocked (403/429/Cloudflare) | 6: uxdatabase.io, bookauthority.org (429), pragmaticinstitute.com (Cloudflare), andrewchen.com, jpattonassociates.com (Cloudflare), scrum.org |
| none (no sitemap found) | 5: evanmiller.org, abtestguide.com, roadmunk.com, juliezhuo.com, uxbooth.com (every path answers 301, not followed; the site may be retired or moved) |
| skipped (platform-scale) | 11: github.com, producthunt.com, goodreads.com, figma.com, notion.so, miro.com, atlassian.com, surveymonkey.com, optimizely.com, intercom.com, statsig.com |

159,038 URLs pulled; 124,367 classified as content. No domain hit the 100,000-URL or 60-sub-sitemap cap.

## Content URLs by seeded section

"Content" excludes home pages, feeds, pagination, author/tag/category archives, search, jobs,
changelogs, product docs and support, non-English locale copies, and slugs with no topic words.
12m = content URLs with a lastmod in the last 12 months.

### Articles

| Domain | Content | 12m | Main sections |
|---|---|---|---|
| uxdesign.cc | 7,475 | 952 | all at root (Medium) |
| smashingmagazine.com | 5,758 | 206 | year folders 2009-2026, newsletter 415 |
| uxplanet.org | 5,672 | 521 | all at root (Medium) |
| productschool.com | 4,646 | 492 | product-leaders 3,538 (people profiles), blog 696 |
| amplitude.com | 3,932 | 3,344 | blog 1,502, track 397, events 346 |
| mindtheproduct.com | 3,668 | 296 | root 3,621 |
| aha.io | 2,980 | 513 | blog 2,106, roadmapping 401 |
| reforge.com | 2,862 | 589 | artifacts 1,736, guides 536, blog 288 |
| pendo.io | 2,836 | 733 | pendo-blog 1,793 |
| nngroup.com | 2,766 | 327 | articles 1,735, videos 946 |
| interaction-design.org | 2,638 | 2,099 | literature 1,835 (10,118 job pages excluded) |
| uxmatters.com | 2,544 | 215 | mt/archives 2,287 |
| lukew.com | 2,184 | 41 | ff (Functioning Form) 2,139 |
| dovetail.com | 1,937 | 416 | contributors 352, research 266 |
| baymard.com | 1,619 | 187 | research-articles 445, ux-benchmark 437 |
| hotjar.com | 1,617 | 0 | root 491, blog 340 |
| productplan.com | 1,408 | 1,408 | learn 596, glossary 309, blog 253 |
| measuringu.com | 1,404 | 100 | root 931 |
| productboard.com | 1,373 | 716 | blog 653, prompts library 157 |
| lennysnewsletter.com | 1,266 | 433 | /p/ 1,264 |
| mixpanel.com | 1,020 | 569 | blog 619 |
| producttalk.org | 777 | 651 | root |
| userpilot.com | 724 | 640 | blog 513 |
| maze.co | 658 | n/a | blog 127, guides 99 (no lastmod) |
| svpg.com | 649 | 51 | root 511 |
| boxesandarrows.com | 618 | 8 | root |
| mountaingoatsoftware.com | 599 | n/a | agile 356, podcasts 191 (no lastmod) |
| cutlefish.substack.com | 473 | 68 | /p/ |
| alistapart.com | 270 | 2 | blog 255 |
| growthunhinged.com | 265 | 265 | /p/ 234 |
| productcoalition.com | 206 | 99 | /p/ 204 |
| romanpichler.com | 171 | 58 | podcast 89 |
| melissaperri.com | 95 | 2 | blog 50 |
| growth.design | 59 | 14 | case-studies 52 |
| departmentofproduct.com | 54 | 5 | blog 49 |
| centercentre.com | 53 | 23 | root |
| lawsofux.com | 42 | 0 | root (most URLs are translations) |
| gibsonbiddle.com | 30 | 6 | root |

Not available: uxbooth.com, juliezhuo.com (none); pragmaticinstitute.com, andrewchen.com,
jpattonassociates.com, scrum.org (blocked); atlassian.com (skipped).

### Links

| Domain | Content | 12m | Main sections |
|---|---|---|---|
| startupstash.com | 4,660 | 656 | root 2,409, tools 2,238 |
| futurepedia.io | 1,944 | 1,533 | tool 1,317, courses 530 |
| bookmarks.design | 689 | 8 | product 688 (one entry per link) |
| designresourc.es | 381 | 109 | resources 338 |
| uxtools.co | 207 | n/a | blog 80, episodes 48 |
| toools.design | 75 | 75 | newsletter 30 |
| prototypr.io | 5 | 5 | sitemap lists almost nothing |
| undesign.learn.uno | 3 | n/a | sitemap lists almost nothing |

Not available: uxdatabase.io (blocked); github.com, producthunt.com (skipped).

### Books

| Domain | Content | 12m | Main sections |
|---|---|---|---|
| mostrecommendedbooks.com | 42,736 | 40,166 | series 39,828, lists 1,343, people 1,120 |
| fivebooks.com | 3,221 | 474 | best-books 2,345, reader-list 426 |
| uxdesign.cc, productschool.com, mindtheproduct.com, nngroup.com, lennysnewsletter.com | see Articles | | |

Not available: bookauthority.org (429), goodreads.com (skipped).

### Tools

| Domain | Content | 12m | Main sections |
|---|---|---|---|
| measuringu.com | 1,404 | 100 | root 931 |
| productboard.com | 1,373 | 716 | blog 653 |
| cxl.com | 1,012 | 180 | blog 911 |
| fibery.io | 745 | n/a | blog 570, templates 92 (no lastmod) |

Not available: evanmiller.org, abtestguide.com, roadmunk.com (none); optimizely.com, statsig.com,
surveymonkey.com, intercom.com (skipped). The calculators themselves are mostly single pages, so
sitemaps say little here; this section needs the SERP pass.

### Templates

| Domain | Content | 12m | Main sections |
|---|---|---|---|
| aha.io | 2,980 | 513 | roadmapping 401 (templates and guides) |
| nngroup.com | 2,766 | 327 | see Articles |
| dovetail.com | 1,937 | 416 | see Articles |
| productboard.com | 1,373 | 716 | see Articles |
| mural.co | 1,341 | 504 | templates 459, blog 628 |
| maze.co | 658 | n/a | collections 70 |

Not available: figma.com, notion.so, miro.com, atlassian.com (skipped).

## 40 most widespread slug tokens

Ranked by the number of domains whose content URLs use the token, then by URL count
(domains/urls). Full table (2,000 rows of 45,987 tokens): `slug-tokens-2026-10-08.csv`.

product (45/9,423), design (45/7,033), tools (42/1,088), user (41/2,429), guide (40/1,147),
strategy (40/996), work (40/719), management (39/1,647), research (39/1,530), building (39/751),
testing (39/696), best (38/2,790), data (38/1,506), customer (38/1,235), team (38/883),
teams (38/776), better (38/759), people (38/399), vision (38/197), development (37/720),
business (37/621), success (37/388), learning (37/327), marketing (36/823), build (36/663),
growth (35/828), top (35/757), google (35/381), market (35/380), principles (35/368),
framework (35/356), sales (35/282), impact (35/272), digital (34/803), app (34/767), case (34/667),
world (34/535), feedback (34/516), future (34/515), process (34/493)

## Odd things

- mostrecommendedbooks.com is a third of all content URLs (39,828 book-series pages) and stamps
  almost every lastmod as recent; read its URL counts with care. The token ranking by domain count
  keeps it from dominating the token table, but the URL counts in that table are inflated by it.
- productplan.com has every lastmod in the last 12 months (bulk regenerated), and amplitude.com and
  interaction-design.org nearly so; "12m" is not a freshness signal for them.
- hotjar.com's newest lastmod is 2025-02-25: the sitemap looks frozen.
- maze.co, mountaingoatsoftware.com, fibery.io and uxtools.co publish no lastmod at all.
- productschool.com's count is mostly people profiles (product-leaders 3,538), not articles.
- Medium publications (uxdesign.cc, uxplanet.org) put every story at the root; their /tagged/ pages
  (4,243 on uxdesign.cc alone) were excluded. Medium's trailing hex ids are dropped from the tokens.
- uxmatters.com keeps all articles under /mt/archives/YYYY/MM/; the date-only archive pages are
  excluded, the articles are kept.
- futurepedia.io and startupstash.com slugs are mostly product names (tool listings), which add
  brand names to the long tail of the token table.
- uxbooth.com answers 301 on every path including robots.txt; worth a manual look to see whether
  the site still exists.
