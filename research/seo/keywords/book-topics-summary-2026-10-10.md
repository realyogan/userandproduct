# Book topics by search demand (10 October 2026)

Question: which ten of the sixteen book topics get a "Books on X" page at launch, and in what order do
the other six follow (one a month)?

Data: one Google Ads volume pull, US, 90 phrases (86 new, 4 reused from 8 October), and page one of
Google for each topic's head phrase (14 new, 4 reused from 8 October). Spend $0.068.
Files: `keywords/book-topics-2026-10-10.csv` (phrases), `serps/book-topics-2026-10-10.csv` (page one).

## How to read the numbers

- **Core volume** is monthly US searches for phrases that name the topic itself ("okr books",
  "ux design books"). **Broad volume** adds wider phrases a page could also aim at ("marketing books",
  "self help books"). The ranking uses core volume.
- **Close variants are counted once.** Google reports one number for a group of near-identical phrases
  ("product management books", "books for product managers" and "product manager books" are one group
  of 590, not 1,770). The `variant_group` column shows the grouping.
- **"startup books" is ranked at 590, not the reported 8,100.** The yearly average carries a spike
  (33,100 at its peak eight months ago); the last few months run 590 to 880.
- **Weak or small slots** are results in the top 10 that a new expert site can stand beside: small
  editorial sites (one author, a small consultancy, a community) plus Reddit, Quora, Medium, YouTube and
  LinkedIn posts. The rest are marketplaces (Amazon, Goodreads, bookstores), SaaS and brand blogs, and
  publishers or institutions (HBR, Harvard, Wikipedia, libraries).
  Winnability: high = 5 or more such slots, medium = 3 to 4, low = 2 or fewer.
- **All 18 pages show an AI overview**, so it does not separate the topics. A book list with the
  owner's own reasons for each pick is the part an AI summary cannot copy.

## Per topic

| Topic | Core vol | Broad vol | Strongest phrase | Head checked | Small editorial + weak slots in top 10 | Verdict |
|---|---:|---:|---|---|---|---|
| Leadership and teams | 24,360 | 24,360 | leadership books 14,800 | management books; leadership books | 0 + 1 (management); 1 + 2 (leadership) | Huge demand, hard page one (HBR, Harvard, CCL, bookstores). Launch, aimed at people who lead product and design teams; "books for new managers" (260) is the winnable corner. |
| Business and entrepreneurship | 9,950 | 9,950 | best business books 3,600 | startup books | 3 + 2 | Big demand and the most open page one of the big topics (founder blogs, Hacker News, Reddit). Launch. |
| Project management | 2,270 | 2,270 | project management books 1,300 | project management books | 0 + 3 | Solid demand; tool-vendor blogs and forums hold page one. Launch. |
| Psychology and behavioral science | 1,890 | 1,890 | behavioral economics books 1,300 | behavioral economics books | 1 + 2 | Good demand, strong fit for design and product. Launch. |
| Personal development | 1,470 | 83,970 | productivity books 880 | productivity books | 0 + 3 | Real demand, but the broad terms (self help, 60,500) are consumer shelves we will not win. Weakest fit. Launch last of the ten, narrowed to productivity for professionals. |
| Product management | 990 | 990 | product management books 590 | product management books (8 Oct) | 1 + 3 | Core fit, steady demand, beatable page one (Reddit, Medium, SaaS lists, Ken Norton). Launch. |
| UX design | 540 | 540 | ux design books 390 (same group as "ux books") | ux books (8 Oct) | 3 + 2 | Core fit and one of the most open pages. Launch. |
| Product metrics (analytics, OKRs) | 480 | 870 | okr books 390 | okr books | 2 + 2 | OKR books carry this topic; OKR software vendors and small blogs rank. Launch. |
| Accessibility | 420 | 420 | accessibility books 390 | accessibility books | 2 + 0 | Mostly digital-accessibility intent, with some disability memoirs and library guides; vendors (Deque, Vispero) and institutions rank. Low winnability, high fit. Launch. |
| UI design | 230 | 440 | ui design books 140 | ui design books | 3 + 3 | Small demand but the most open page one of all sixteen (six weak or small slots). "web design books" (210) adds reach. Launch. |
| Growth and pricing | 170 | 3,070 | pricing books 50 | pricing books; growth books | 1 + 3 (pricing) | "growth books" (2,900) means personal growth and self help, not product growth. "pricing books" is mixed with book pricing for authors. Little clean demand. Follow-on. |
| UX research | 150 | 150 | ux research books 90 | ux research books (8 Oct) | 2 + 2 | Small but clean demand, core fit, open page one. First follow-on. |
| Design systems | 80 | 170 | atomic design book 90 (a title search); design systems books 70 | design systems books | 0 + 4 | Small; page one is Reddit, Medium, dev.to, YouTube and Smashing. Follow-on. |
| Product marketing | 80 | 2,080 | product marketing books 50 | product marketing books | 1 + 2 | The core phrase is small; "marketing books" (1,000) is a general shelf. Follow-on. |
| Product strategy | 40 | 1,110 | product strategy books 20 | product strategy books (8 Oct) | 0 + 2 | Tiny and muddled; Google mixes in marketing and corporate strategy. Broad "strategy books" (590) is not our reader. Follow-on. |
| Product discovery | 20 | 20 | product discovery books 10 | product discovery books | 3 + 2 | Almost no searches; Google answers with general product management book lists. Follow-on, or a section inside the product management page. |

## Ranking of all sixteen

Weighed by demand first, then winnability, then fit with the site's goal (authority in UX, product and
business).

| # | Topic | Core volume | Best phrase | Winnability |
|---:|---|---:|---|---|
| 1 | Leadership and teams | 24,360 | leadership books (14,800) | Low |
| 2 | Business and entrepreneurship | 9,950 | best business books (3,600) | High (startup page) |
| 3 | Project management | 2,270 | project management books (1,300) | Medium |
| 4 | Psychology and behavioral science | 1,890 | behavioral economics books (1,300) | Medium |
| 5 | Product management | 990 | product management books (590) | Medium |
| 6 | UX design | 540 | ux design books (390) | High |
| 7 | Product metrics | 480 | okr books (390) | Medium |
| 8 | Accessibility | 420 | accessibility books (390) | Low |
| 9 | UI design | 230 | ui design books (140) | High |
| 10 | Personal development | 1,470 | productivity books (880) | Medium |
| 11 | UX research | 150 | ux research books (90) | Medium |
| 12 | Growth and pricing | 170 | pricing books (50) | Medium |
| 13 | Design systems | 80 | design systems books (70) | Medium |
| 14 | Product marketing | 80 | product marketing books (50) | Medium |
| 15 | Product strategy | 40 | product strategy books (20) | Low |
| 16 | Product discovery | 20 | product discovery books (10) | High |

Two places in the ranking are judgment, not volume:

- **Personal development sits 10th**, below topics with less demand, because its fit is the weakest of
  the sixteen and none of the top 10 for "productivity books" is a small editorial site. It stays in
  the ten on demand.
- **UX research comes before growth and pricing** although its core volume is a little lower (150
  against 170): its demand is clean, most growth and pricing searches mean something else, and UX
  research is a core fit.

## The ten to launch

Leadership and teams, Business and entrepreneurship, Project management, Psychology and behavioral
science, Product management, UX design, Product metrics, Accessibility, UI design, Personal development.

## The other six, one a month

1. UX research
2. Growth and pricing
3. Design systems
4. Product marketing
5. Product strategy
6. Product discovery

## Notes for the topic pages

- Product discovery and product strategy have so little demand of their own that a section on the
  product management page may serve searchers better than a page each; the pages can still follow later
  to complete the shelf.
- The big generic topics (leadership, business, productivity) win on demand, but each page has to show
  its angle in the title and opening (for example, books for people who lead product teams), or it is
  one more generic list up against HBR and the bookstores.
- "atomic design book" (90) and "web design books" (210) are worth a line on the design systems and UI
  design pages.
