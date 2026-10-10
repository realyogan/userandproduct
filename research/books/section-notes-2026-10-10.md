# Books section: how respected sites present recommendations (10 Oct 2026)

Notes from reading twelve book pages on 10 Oct 2026: two product newsletters, two product
publications, a product coaching firm, a growth agency, three design publications or tool makers, an expert-interview
book site, an independent-bookshop platform and a magazine's disclosure policy. Everything below is our
own summary; none of their text is copied. The candidate list these notes support is
`research/books/candidates-2026-10-10.md`.

## What we looked at

| Site | Kind | URL |
|---|---|---|
| Lenny's Newsletter, Essential books for product builders (part 1, May 2026) | Product newsletter | https://www.lennysnewsletter.com/p/essential-books-for-product-builderspart |
| The Product Compass, Top 9 product discovery books | Product newsletter | https://www.productcompass.pm/p/at-least-half-of-your-ideas-will |
| Mind the Product, Best PM books to read in 2023 | Product publication | https://www.mindtheproduct.com/the-best-product-management-books-you-should-read-in-2023 |
| SVPG, Recommended reading | Product coaching firm | https://www.svpg.com/recommended-reading/ |
| Giff Constable, 21 books every PM should know | Practitioner's blog | https://giffconstable.com/2019/08/21-books-every-product-manager-should-know/ |
| UX Mastery, UX books | Design publication | https://uxmastery.com/resources/books/ |
| Interaction Design Foundation, UX design books guide | Design education site | https://ixdf.org/literature/article/ux-design-books-guide |
| Maze, UX design books | Design tool maker's guide | https://maze.co/collections/ux-ui-design/ux-design-books/ |
| Growth Method, Growth marketing books | Growth agency blog | https://www.growthmethod.com/growth-marketing-books/ |
| Five Books, Dan Ariely on behavioral economics | Expert-curated book site | https://fivebooks.com/best-books/behavioural-economics-dan-ariely/ |
| Bookshop.org (affiliate program and widgets) | Independent-bookshop platform | https://support.bookshop.org/en/support/solutions/articles/65000191390-can-you-explain-bookshop-org-s-affiliate-program- |
| Behavioral Scientist, Editorial policy on Bookshop.org affiliate links | Magazine disclosure page | https://behavioralscientist.org/?p=26808 |

Bookshop.org's own curated list pages (for example https://bookshop.org/lists/experience-design-content-ux-strategy-books)
blocked automated reading, so the bookshop view comes from its help pages and widget documentation.

## What each site shows per book

- **Lenny's Newsletter.** The thinnest entries of all: title, author and a number, grouped under
  reader goals written as "I want to..." (get better at strategy, become a better manager, and so on),
  three books per goal. The reasoning sits at the group level, in a short intro and links to his
  podcast episodes with the author. Summaries of the piece give his selection rule as only books he has read, with a
  lean toward books more than ten years old. Authority comes from the person, not from the entry.
- **The Product Compass.** A numbered list of nine with a paragraph each, one composite image of the
  covers at the top, no purchase links.
- **Mind the Product.** Three tiers named by the editor (the standards, more must-reads, books for
  leaders), and a short editorial blurb per book. No covers, no ratings, no prices.
- **SVPG.** Their own four books first, then a bare top-ten list (title and author only). A firm's
  shelf reads as an endorsement; nothing more is needed.
- **Giff Constable.** Category headings (strategy, pricing, teams, leadership, design, psychology),
  then title, author and one line on why. Plain text, no images.
- **UX Mastery.** A long list (about 80) with a starred top ten, each with a buy button. The covers are
  blank placeholders on the live page, which makes the shelf look broken rather than designed.
- **Interaction Design Foundation.** Grouped by reader (beginners, professionals, UI, research and
  strategy), each with a cover, a paragraph, a "key takeaway" box and often a pull quote or a short
  video. The richest entries of the set, and the slowest to scan.
- **Maze.** Grouped by theme, each with a cover, a star rating, publication year, reader level,
  description and quotes from reviewers. No purchase links at all; the page exists to teach and to
  bring readers to Maze.
- **Five Books.** Each book is a numbered entry inside an interview with an expert who explains, in
  conversation, why that book. Cover, title, author and a "read" button per book, plus a "buy all
  five" button. The recommendation is the expert's reasoning, which no list format can copy.

**Pattern.** The pages that feel most trustworthy say who is recommending and why in a sentence or two
per book, group by what the reader wants to do, and keep the entry short. The weakest pages are long
lists with buy buttons and no reason per book. That matches our own rule in the search policy layer
(`.claude/skills/search-policy/SITE.md`, Affiliate and ads): every entry carries the owner's take,
what the book is good for, for whom, and where it is wrong or dated.

## Affiliate links and disclosure

- **Most of the respected product pages carry no affiliate links at all.** Lenny's Amazon links have
  no associate tag; several point to the author's or publisher's own site (SVPG, Stripe Press, the
  Build site). The Product Compass and Maze have no purchase links.
- **Several sites use affiliate links without saying so.** UX Mastery's buy buttons carry Amazon and
  Book Depository affiliate IDs with no disclosure on the page. One Mind the Product link carries what
  looks like an associate tag, also undisclosed. Giff Constable's and Growth Method's Amazon links
  carry tracking parameters, with no statement either way. This is the practice to avoid: Google asks
  for `rel="sponsored"` on paid links and a visible disclosure near them, and the US FTC expects the
  same.
- **Five Books does it in the open.** A site-wide statement that it earns from qualifying Amazon
  purchases, an affiliate tag on its buy buttons, and a separate request for donations. It routes buy
  clicks through its own `/buy` page, which makes swapping retailers easy later.
- **Behavioral Scientist shows the cleanest disclosure model.** A dedicated policy page explains that
  its book links go to Bookshop.org, that a small commission funds the magazine, why it chose an
  independent-bookshop platform, and that editors choose every book on its merits.
- **Bookshop.org as an alternative to Amazon.** Its help pages describe a commission for
  non-bookstore affiliates on sales within 48 hours of a click (10 percent per its UK page and
  publisher coverage), an equal share to independent bookshops, last-click attribution, and official
  book, button and list widgets.
- **Amazon Associates.** Third-party summaries of the program policies (not checked against Amazon's
  own agreement yet) say a fixed disclosure sentence must appear where program content is shown, and
  that product images and prices may be shown only through Amazon's own links or its product API,
  with images not stored for more than 24 hours. To confirm against the Operating Agreement before we
  join.

## Cover images

Four approaches seen, with what each means for us:

1. **Publisher or retailer covers hosted on the site.** IxDF hosts covers on its own image server and
   captions them as fair use with the author credited; Five Books hosts covers on its own CDN. Common
   and usually tolerated, but it rests on fair use rather than a license.
2. **Affiliate-program images.** Amazon's images come with the Associates license but only through
   its links or API, with caching limits; Bookshop.org's widget shows a cover and price inside its own
   embed. Both tie the page's look and speed to a third-party script or image host.
3. **Open Library covers.** Free cover images by ISBN at covers.openlibrary.org in three sizes; asks
   for no crawling, a rate limit of 100 ISBN lookups per IP every five minutes, loading from their
   host, and a link back to Open Library as a courtesy. A blank image comes back when no cover exists,
   unless the request asks for a 404 instead. Docs: https://openlibrary.org/dev/docs/api/covers
4. **No covers or drawn placeholders.** Mind the Product, Giff Constable and Growth Method show no
   covers; Lenny uses one banner per group; The Product Compass uses one composite image. UX Mastery's
   blank placeholders show what not to do: an empty box reads as a missing image.

**For our shelf.** The two honest options are a code-drawn spine or card per book (title and author
set in our type on the article's tint, in the same family as our thumbnails, no imitation of the real
jacket) or a real cover from a licensed or freely offered source (Open Library, or the affiliate
program's own images once we join one). Mixing the two on one page would look uneven; pick one.
Hosting scanned publisher jackets ourselves is the option to skip.

## Ideas worth taking, in our own form

- Group by what the reader is trying to do as well as by topic, so a shelf answers "I am a new PM"
  or "I have to set strategy" as well as "UX research".
- One or two sentences of the owner's own reasoning per book, plus a line on who should skip it and
  what has aged. Nobody in the sample says where a book is wrong or dated; that is our gap to fill.
- A short "recommended by" line naming lists the reader already trusts (the tier-A table in the
  candidates file has these), linked to the source.
- Prefer the author's or publisher's own page where it sells direct, and say so.
- One disclosure line beside every buy link and a short policy page in the style of Behavioral
  Scientist's, with `rel="sponsored"` on every affiliate link.
