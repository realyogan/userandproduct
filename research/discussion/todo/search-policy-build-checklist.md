# Search policy: what we have to build and set

The rulebook is `.claude/skills/search-policy/SKILL.md`; the site layer is `SITE.md` beside it. This
is the to-do that makes the rules true. Tick items as they land; each names the step of the build
plan it belongs to.

## Site design (now)

- [ ] Author page design: byline target, verifiable background, the owner's real photo, links to the LinkedIn
      profile and the other places the owner exists online (portfolio if decided), the same links as `sameAs` in the
      ProfilePage markup. (Rule 5, 8)
- [ ] About page design: what the site is, who runs it, a contact route. (Rule 5)
- [ ] Newsletter sign-up as an in-page box; no pop-up, no overlay, anywhere. (Rule 12)
- [ ] Custom 404 with an explanation, search and useful links. (Rule 12)
- [ ] Ad slots labelled, never styled like content or navigation, never sticky over content; at most
      three in view; mobile density under thirty percent. (Rule 12)
- [ ] Category and series pages with their own intro text, ordered by series or importance, no
      sort-by-date. (Rule 10, 11)
- [ ] Article page: one dominant `<h1>`, quiet "Updated <month year>", byline linking to the author
      page, related pieces, no date-sorted lists. (Rule 6, 11)
- [ ] Tools pages designed as real pages: what it is, when to use it, how, around a working calculator or checker
      in plain JavaScript; at least ten tools ship at launch (templates after launch). (Rule 12)
- [ ] Books shelf entry design with room for the owner's take and a visible disclosure line. (Rule 9)
- [ ] Figures: every diagram gets alt text plus a body-text explanation beside it; placement near the
      text it belongs to. Add to `research/mockups/illustration-rules.md`. (Rule 7)
- [ ] Core Web Vitals budget written into the theme brief: LCP 2.5 s, INP 200 ms, CLS 0.1. (Rule 12)

## WordPress install (build step 4)

- [ ] HTTPS with a valid certificate, HTTP to HTTPS redirect, HSTS. (Rule 10)
- [ ] Permalinks in words, lowercase, hyphenated; sections as folders if the hierarchy helps. (Rule 10)
- [ ] Rank Math: self-referential canonical on every page; noindex on tag, date and author archives,
      internal search, attachment pages; attachment pages disabled; filters never indexable. (Rule 10)
- [ ] Rank Math: Article schema with author as Person linked to the author page; dates from the real
      publish and modified dates with timezone; featured image as the article image in three ratios.
      (Rule 8)
- [ ] Rank Math or theme: Organization markup on the home page (name equal to the site name, url, logo
      at least 112 px square readable on white, sameAs). (Rule 8)
- [ ] Theme: WebSite markup with site name and alternateName on the home page only, same markup on
      http/https and www/non-www, nested in one node; `og:site_name` consistent. (Rule 8)
- [ ] Theme: ProfilePage markup on the author page; no placeholder image. (Rule 8)
- [ ] Rank Math: BreadcrumbList on pages below the home page, typical user path. (Rule 8)
- [ ] Remove any FAQPage, HowTo or sitelinks search box markup the plugin offers. (Rule 8)
- [ ] Meta description field required per article; site-level descriptions on home and sections. (Rule 7)
- [ ] Open Graph title and image equal to the page's title and featured image; `og:image` never the
      logo or an image with text. (Rule 7)
- [ ] Images as `<img>` with `src` fallback; descriptive filenames; one URL per image; no CSS-only
      images for content. (Rule 7)
- [ ] Comments off at launch; if ever on, moderation and `rel="ugc nofollow"` on links. (Rule 12)
- [ ] Sitemap on, listing canonical HTTPS URLs only; image sitemap if figures matter. (Rule 10)
- [ ] `X-Robots-Tag` rules for PDF or file downloads that should not index. (Rule 10)
- [ ] Rich Results Test on every template once live; Schema Markup Validator for WebSite; URL
      Inspection on the first pages. (Rule 8)
- [ ] Search Console connected and sitemap submitted on day one; Core Web Vitals, rich result and page
      indexing reports watched. (Rule 10, 12)
- [ ] Check the domain's history before launch (done 10 Oct 2026: no archived snapshots). (Rule 10)

## Newsroom app and data (build step 1)

- [ ] Card field: the one-line reader reason; cards without it cannot be approved. (Rule 1)
- [ ] Card fields: seed or note, kind, sits-beside, YMYL-adjacent mark, source and origin for every
      fact (the brief's source list). (Rule 2, 4)
- [ ] Preview shows the title tag, meta description, every alt text and a structured data summary
      beside the article so the owner's review covers them. (Rule 7, 8)
- [ ] Positions list on the card above the preview, with keep, reword, strike. (Site layer)
- [ ] Principles file: every rule the owner gives, with id, words and the pieces that use it; drafts
      checked against it for consistency. (Site layer)
- [ ] Check report (`checks.md`) template following the twelve-point checklist. (Rule 14)

## Agent rulebooks (build step 2)

- [ ] Checker: paraphrase check against listed sources and books; three-sentence spot-check through
      the paid API; origin check for every specific; filler and answer-first check; YMYL-adjacent
      handling. (Rule 4)
- [ ] Writer: title rules, description, keyword-once, answer-first, link text, sponsored and nofollow
      marking, no first-person or invented specifics. (Rule 6, 7, 9)
- [ ] Illustrator: alt text method, body-text explanation for diagrams, filenames. (Rule 7)
- [ ] SEO reviewer: stuffing, internal links to neighbours, category and series, canonical targets,
      sits-beside conflict check. (Rule 6, 9, 10)
- [ ] Publisher: real dates, `dateModified` only on substantial change, URL Inspection, live checklist,
      refusal without the owner's confirmation. (Rule 8, 11, 14)
- [ ] Campaign manager: authority signals, review dates, title rewrites bound to honest titles, never a
      rank target as purpose; no automated Google queries. (Rule 5, 6, 11, 13)
- [ ] Explorer: reader-reason line on every card; reader questions as input, never a page per question;
      sitemap and feed reading for research only. (Rule 1, 3, 13)

## Editorial decisions already made (for the record)

- Synthesis pieces up to a quarter, fresh takes only, labeled, not in the flagship launch set.
- No "How this site is made" page; no per-article labels; no tool names anywhere a reader sees.
- Books shelf: owner's take per entry, sponsored links with disclosure.
- Launch with about fifty reviewed pieces at once; sitemap and Search Console on day one.
