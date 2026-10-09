# Phase 0 SERPs: Books section (2026-10-08)

Google US (2840), desktop, depth 10, standard queue. 12 tasks collected, free (posting cost $0.0006 each,
already logged at post time). Raw JSON: `research/seo/cache/raw/serps-2026-10-08/<slug>.json`.

Files:
- `research/seo/serps/page-one-2026-10-08-books.csv` (102 organic rows; no featured snippets)
- `research/seo/serps/features-2026-10-08-books.csv` (12 rows)
- `research/seo/cache/index-staging-serps-books.csv` (12 rows, ids 261008-SK-001 to 012; to be merged into
  `cache/index.csv` by the main session)

## Collected / pending

All 12 collected, none pending: ux books, best ux design books, product management books, best product
management books, books for product managers, ux research books, design books, business books for product
managers, behavioral psychology books for designers, agile books, product strategy books, leadership books for
product managers.

## Top 20 domains on page one (organic, keywords appearing in, out of 12)

| # | Domain | Count | Type |
|---|---|---|---|
| 1 | reddit.com | 11 | forum |
| 2 | amazon.com | 11 | retailer |
| 3 | productplan.com | 4 | SaaS |
| 4 | quora.com | 4 | forum |
| 5 | goodreads.com | 3 | catalog |
| 6 | youtube.com | 3 | video |
| 7 | bringthedonuts.com | 3 | personal |
| 8 | rysullivan.medium.com | 3 | Medium |
| 9 | userflow.com | 3 | SaaS |
| 10 | johannesippen.com | 2 | personal |
| 11 | uxplanet.org | 2 | Medium |
| 12 | blog.uxfol.io | 2 | SaaS |
| 13 | medium.com | 2 | Medium |
| 14 | nextleap.app | 2 | edtech |
| 15 | linkedin.com | 2 | social |
| 16 | productmanagementexercises.com | 2 | edtech |
| 17 | dontpaniclabs.com | 1 | agency |
| 18 | ixdf.org | 1 | edtech |
| 19 | smart-interface-design-patterns.com | 1 | course |
| 20 | schoolofux.com | 1 | course |

Rows 17 to 20 are an arbitrary pick among about 30 domains seen once (others include simonsovic.com,
audible.com, prodpad.com, mentorcruise.com, gainsight.com, mindtheproduct.com, amplitude.com,
productschool.com, agilealliance.org, pmi.org, mountaingoatsoftware.com, digitaldefynd.com, maze.co).

## Headline numbers

- AI Overview: 12 of 12 keywords. In 4 (best ux design books, behavioral psychology books for designers,
  product strategy books, leadership books for product managers) it is an asynchronous placeholder with no
  content or references, so `ai_overview_ref_domains` is empty there.
- weak_count of 3 or more: 7 of 12 (best ux design books 4, leadership books for product managers 4,
  product management books 3, best product management books 3, books for product managers 3,
  design books 3, behavioral psychology books for designers 3).
- Featured snippet: 0 of 12. Knowledge graph: 0 of 12.

## Who holds these SERPs

- Reddit: on page one for 11 of 12 and in the top 3 organic for all 11. The single strongest pattern.
- Amazon: 11 of 12 (all but ux research books), mostly mid or low page one, usually search/bestseller pages,
  sometimes a single product page.
- Goodreads: 3 (ux books, product management books, agile books). Present but not dominant.
- Medium and Medium-hosted (uxplanet.org, author subdomains): 8 appearances across 7 keywords.
- SaaS blogs: productplan.com (4), userflow.com (3), uxfol.io (2), amplitude.com, maze.co, prodpad.com,
  gainsight.com, uxtweak. Strongest on the PM keywords.
- Publications: almost none (bostonmagazine.com, strategy-business.com once each). No Smashing, NN/g,
  HBR or similar editorial site ranks. Personal practitioner lists (Ken Norton's bringthedonuts.com,
  johannesippen.com, jenson.org, simonsovic.com) rank well, which supports an owner-authored list.
- AI Overview citations repeat the same sources: reddit, bringthedonuts, productplan, userflow, amplitude,
  mindtheproduct, nextleap, ixdf, goodreads.

## Book carousels

- No `shopping` or `knowledge_graph` item type appears. Google shows book carousels as `popular_products`
  ("Popular products" / "More products", 8 books each, sold by Barnes & Noble, Target, Walmart, Books A Million
  and others, never Amazon) on 10 of 12 keywords (not on ux books or best ux design books). The features CSV
  marks `shopping=yes` for these 10, since `popular_products` is the shopping unit here.
- Images pack: design books, product strategy books.

## Anything odd

- The PM cluster is one SERP: product management books, books for product managers and business books for
  product managers share an identical AI Overview, and leadership books for product managers overlaps heavily.
  One strong pillar page can target all four.
- No `video` item type anywhere (video column is "no" for all), but 4 keywords have a YouTube or TikTok
  result as a regular organic row with `is_video` (best ux design books, product management books,
  design books, behavioral psychology books for designers).
- `discussions_and_forums` blocks (Reddit, Quora, LinkedIn) on 5 keywords, on top of the organic Reddit
  results; not counted as organic.
- "design books" and "product strategy books" are off-intent for us: design books leans graphic/interior
  design and coffee-table books (Phaidon, a $1,200 Assouline title); product strategy books ranks marketing
  strategy lists, a $210 academic title and scrum.org. Both look winnable but need careful intent framing.
- behavioral psychology books for designers has the weakest page one (productdesignpsychology.com, a Facebook
  group post, a Google Books page, Pinterest, an old Reddit thread).
- Weak-domain rule applied to subdomains for all listed weak domains (so kr.pinterest.com and
  *.medium.com count); amplitude.com counted weak on leadership books because its URL is under /blog/.
- Some timestamps are synthetic (e.g. "2025-10-08 15:45:41" for TikTok/YouTube), derived from "1 year ago".
