# cluster_v2.py rule patch (proposed, not applied)

Source: `keywords/review-unassigned-summary-2026-10-08.md` (manual review of each unassigned phrase, 8 Oct 2026).
These patterns would have caught the recovered keywords in `keywords/review-unassigned-combined-2026-10-08.csv`
and `keywords/review-unassigned-phase1-2026-10-08.csv`. Apply them in a later session, re-run cluster_v2.py and
diff `keyword-to-topic-v2` against the review CSVs. Patterns are Python regex matched against the lowercased
keyword, in the same shape as `NOISE` and `RULES`.

Note: cluster_v2.py only reads the combined harvest. The Phase 1 recoveries (section 2, most rows) only take
effect if the Phase 1 harvest is re-clustered with these rules or the same phrases come back in a later harvest.

## 1. Noise rules that are too wide (fix first)

| Noise rule | Problem | Change |
|---|---|---|
| physical and device accessibility | `electronic` in the second alternation sends "electronic accessibility" (74,000, KD 27) to noise; it means digital accessibility | remove `electronic` from the list |
| nursing prioritization | `patient` sends "patient journey map" (480) to noise | drop `patient`; the nursing rows already match `nursing\|nclex\|\bnurse\|delegation` |
| building and engineering systems | `\bgrid\b` sends "grid system graphic design" and two variants (880 each) to noise | change to `\bgrid\b(?!.*design)` |

## 2. Extra patterns for existing topics

Add each alternation to the topic's main pattern; the sub-topic column says where it should land (add the same
alternation to that sub-topic's pattern).

| Topic | Sub-topic | Add to pattern | Catches |
|---|---|---|---|
| accessibility | accessibility definitions (general) | `universal design\|assistive technolog` | universal design, assistive technologies examples |
| accessibility | web and digital accessibility | `electronic accessib` (after the noise fix) | electronic accessibility |
| a/b testing and experimentation | a/b testing (general) | `\ba[ -]?b[ -]?(c\|n) testing\|a-b-testing\|a b website testing\|what is a and b testing\|hypothesis testing` | a b c testing, a b n testing, hypothesis testing |
| agile, scrum and kanban | agile methodology (general) | `software development (life ?cycle\|cycle\|process\|methodolog)\|sdlc\|spiral (life.?cycle\|methodology)\|\bv model\b\|rapid application development\|crystal methodolog\|iterative process` | SDLC, spiral model, V model, Crystal |
| analytics | (topic) | `product analyst\|data analysis tools` | product analyst, data analysis tools |
| design systems and ui components | design systems | `design-system\|design system design` | design-system |
| design systems and ui components | ui components and patterns | `grid system.*design\|design.*grid system` | graphic design grid system |
| design thinking | design thinking (general) | `human.centered design` | human centered design |
| design thinking | design thinking process and stages | `^design process$\|design process thinking\|problem statement` | design process, problem statement examples |
| go-to-market and product marketing | (topic) | `ideal customer profile\|customer segments\|target (market\|definition)\|product promotion\|strategy marketing product` | ideal customer profile |
| growth marketing and funnels | (topic) | `call to action\|marketing plan\|b2b marketing\|customer acquisition(?! cost)\|word of mouth marketing\|conversion rate optimization` | call to action, marketing plan, customer acquisition |
| information architecture | (topic) | `sitemap examples` | website sitemap examples |
| okrs, kpis and metrics | metrics (general) | `customer acquisition cost\|customer lifetime value\|\bcac\b\|\bltv\b\|\bclv\b\|\barr formula` | CAC, CLV, ARR |
| personas and journey maps | personas | `customer profile` | customer profile |
| personas and journey maps | journey maps and user flows | `patient journey\|flow ?chart\|flow of a website` | flow chart examples |
| prioritization | prioritization frameworks | `urgent.{0,5}important\|important.{0,5}urgent\|prioritization grid` | urgent important matrix |
| product management (discipline) | product management (general) | `product ?/? ?services? management\|product features\|digital products\|pragmatic marketing` | product service management |
| product management (discipline) | product life cycle | `product obsolescence` | product obsolescence |
| product strategy, discovery and launch | product strategy | `value proposition\|selling proposition\|product (line\|mix\|depth\|diversification)\|^product and strategy$\|^strategy for product$\|product.?/?.?service strategy` | value proposition, unique selling proposition |
| product strategy, discovery and launch | new product development and launch | `beta testing\|launch strategy\|release strategy\|product failures\|research and development of a product\|product research and development` | beta testing |
| product strategy, discovery and launch | product strategy and discovery (general) | `^discovery product$\|mvp software` | discovery product |
| project management | (topic) | `task management\|project coordinator\|program management\|statement of work\|scope of work\|kick.?off meeting` | task management, statement of work |
| requirements and prd | (topic) | `spec.driven development` | spec driven development |
| retention, churn and engagement | retention (general) | `^retention( def)?$\|customer lifecycle` | retention |
| retention, churn and engagement | customer retention and loyalty | `customer success\|customer loyalty` | customer success, customer loyalty |
| stakeholder and change management | stakeholder management | `expectation management` | expectation management |
| ux and ui design (discipline) | (topic) | `^digital design$\|design of everyday things` | digital design |
| ux research | surveys and questionnaires | `(closed\|filter\|hybrid\|contingency\|branch(ing)?) questions?\|likert` | closed questions in research, filter question examples |
| ux research | usability testing | `\buat testing` | uat testing |
| web design | (topic) | `landing page\|portfolio website\|about us page\|faq page\|footer examples\|layout examples\|one page website\|parts of a website\|what makes a good website` | landing page examples |

(`\|` in the table is a plain `|` in the regex.)

Order guard: okrs, kpis and metrics must run before growth marketing and funnels, or "customer acquisition cost"
lands in growth marketing (the lookahead above also prevents it). "customer profile" must run before any rule that
matches "customer".

## 3. New topics (only those that met the bar: 10+ keywords or 5,000+ adjusted searches)

Insert before the generic design and marketing rules so they win first match.

```python
("business strategy fundamentals", "business",
 r"business plan|mission statement|vision statement|vision and mission|strategic management|"
 r"business model\b|software as a service",
 [("business plans", r"business plan"),
  ("mission and vision statements", r"mission|vision")],
 "business strategy (general)"),
("visual design principles", "design",
 r"principles? of design|design principles?|elements of design|design elements",
 [], ""),
("market research and competitor analysis", "business",
 r"market(ing)? research|competitive (benchmarking|edge research)|competitor analysis|customer insights",
 [], ""),
("customer experience (cx)", "business",
 r"customer experience|customer.centric|voice of (the )?customer|customer (advocacy|focus|obsession)|"
 r"customer satisfaction index",
 [], ""),
("ux writing and content design", "design",
 r"ux writ|content design|content strategy|microcopy",
 [], ""),
("dashboard and data visualization design", "design",
 r"dashboard (design|examples)|data visuali[sz]ation",
 [], ""),
("business analysis", "product",
 r"business (systems )?analyst|business analysis",
 [], ""),
```

Caveats:

- `business plan` alone also catches industry plans ("cleaning business plan", "bakery business plan"). Add a NOISE
  rule first: `(cleaning|bakery|bar|salon|restaurant|car dealer(ship)?|funeral home|thrift store|vending machine|`
  `construction|clothing line|security company|nonprofit|retail( store)?) business plan|business plan for a`.
- "customer experience in the va is" (government survey) needs a NOISE entry: `customer experience in the va`.
- The 20-keyword topic floor in cluster_v2.py would fold four of these back into unassigned (dashboard and data
  visualization 4, business analysis 4, ux writing 11, customer experience 12 in the combined set alone). Either
  lower the floor for topics with 5,000+ adjusted searches or keep them as near misses on purpose.
- Business analysis is mostly job-title search; the jobs flag may already catch its "remote" and "internship" rows.
