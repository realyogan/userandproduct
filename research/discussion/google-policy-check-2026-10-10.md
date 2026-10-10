# Our plan against Google's policies

10 October 2026. The owner asked for a rulebook built from Google's spam policies and a check of
everything planned so far against them. Sources read in full: the spam policies, "Creating helpful,
reliable, people-first content", "Google Search's guidance about AI-generated content" (February
2023) and the Search Essentials, saved under `research/discussion/references/google-policies/`.
The rulebook is `.claude/skills/search-policy/SKILL.md`. The owner's screenshot of a summary is
saved beside the sources.

## What the policies actually say about our method

- Software-made content is not banned. "Appropriate use of AI or automation is not against our
  guidelines." What is banned is making pages "primarily to manipulate search rankings and not to
  help users", under the scaled content abuse policy, "no matter how it's created".
- The quality bar is effort, originality, skill and accuracy. "Using generative AI to produce large
  amounts of text without manual oversight or curation represents little to no effort." Oversight
  and original contribution are what separate a publication from scaled content.
- The warning signs Google lists for search-engine-first content include: "extensive automation to
  produce content on many topics", "mainly summarizing what others have to say", "lots of content on
  many topics in hopes that some might perform", "things simply because they seem trending", a
  niche entered "without any real expertise", changing dates to look fresh.
- Authorship must be real. Bylines and author pages are encouraged; fabricated profiles are
  deception and a low-quality signal.
- Disclosure of AI use is not required. Google says to "consider adding" it "when it would be
  reasonably expected" and advises against giving AI a byline.
- Affiliate links are fine when marked `rel="sponsored"` and the page adds its own value. Thin
  affiliate pages (copied blurbs plus links) are not.
- Never send automated queries to Google (rank checking, scraping results).

## Where our plan stands

### Clear, as planned

| Plan element | Policy | Standing |
|---|---|---|
| Launch with about fifty reviewed articles at once | Scaled content abuse | Count and timing are not the test; value and oversight are. An ordinary launch. |
| Rolling windows, one piece a day after launch | Same | Fine. Pace is not a signal. |
| Owner's byline on every piece, author page, About page | Who | Matches what Google asks for, as long as the owner is the author of record in fact. |
| Learning-sentence gate, "sits beside" field, cluster rule | Originality, doorways | Good. Keeps pages distinct and prevents near-duplicates aimed at one query. |
| No backdated dates, one quiet "Updated <month year>" | Dates | Fine, provided the date moves only on substantial change. |
| Books section with the owner's own take per book | Thin affiliation | Fine. Add `rel="sponsored"` and a visible disclosure. |
| Keyword and SERP data from the paid research API | Machine-generated traffic | Fine. Our tools use the API, never Google directly (checked the tools folder). |
| Rival sitemap and feed reading for research | Scraping | Fine. Nothing is republished. |
| Filters never indexable, attachment pages off, one canonical URL | Doorways, duplicates | Already in the development rules. |
| Takes only when fact-based and the owner has lived it | Trending, accuracy | Fine. Keeps takes out of "because it is trending". |
| Domain history | Expired domain abuse | No archived snapshots of userandproduct.com. Clean. |

### Needs a change or a decision

1. **Synthesis pieces are the policy's own example of low effort.** The council allowed cards
   labeled "synthesis" (no owner input) at up to a quarter of output. Google's text says that
   "mainly summarizing what others have to say" is a warning sign and that generated text "without
   manual oversight or curation represents little to no effort". A synthesis piece reviewed by the
   owner has oversight, but no original contribution. Recommendation: every page carries the
   owner's judgment (a seed, a brief, a shaping note or an approved position list). The seed the
   council proposed is the cheapest way to make this true. The rulebook is written that way; the
   owner decides whether synthesis pieces exist at all.

2. **"Extensive automation to produce content on many topics" is us, unless the owner's role is
   real on every piece.** The defense is not a label; it is that the owner directs, seeds, reviews
   and approves each piece, and that this is visible in the pages (judgments, examples, rules from
   practice). The review step in the app and the confirmation in local WordPress must stay a real
   read, never a rubber stamp. The ramp rule already gates on fixes per draft, which supports this.

3. **The "How" question and the no-attribution rule.** Google does not require a disclosure, so the
   site's rule (no AI attribution anywhere a reader can see) does not break a policy. Google does
   say a disclosure is "useful for content where someone might think 'How was this created?'".
   This is the owner's call. The honest middle: a short "How this site is made" page saying the
   owner directs, reviews and approves every piece and that research and drafting use software
   tools, with no per-article labels and no tool names. Record the decision either way.

4. **Any-category expansion versus "topics in hopes some perform".** The explorer may open any of
   the thirteen planned categories as a cluster. That is fine while every cluster is inside the
   owner's experience. The rulebook adds one line to every card: "why our own readers would want
   this if search did not exist." A card whose only reason is volume dies.

5. **Expectation lines framed as rank targets.** "Top 10 within 90 days" on a card frames the
   piece's purpose as ranking. Not a violation (it is internal), but it pulls the system toward
   search-engine-first thinking. Already changed by the council verdict to leading signals; the
   rulebook makes that the rule.

6. **No close-paraphrase check existed.** The writer works from the top five pages and from books.
   The council found no station tests for close paraphrase. The rulebook puts that check at the
   checker's station against every listed source and book.

7. **Title rewrites by the campaign manager.** "Rewrite a title that gets many impressions and few
   clicks" can drift into clickbait. The rulebook binds rewrites to the honest-title rule.

8. **Templates and tools pages must be real pages.** A template page that is a download button and
   a hundred words is thin. Each needs the owner's guidance on when and how to use it, which is
   what makes it main content. Calculators count as main content when they work and help.

9. **Category and tag archives.** Category and series pages are fine as a browseable hierarchy with
   their own intro text. Tag, date and author archives should not be indexed; set this in Rank Math
   at install.

10. **Affiliate disclosure.** The books section and any paid link need `rel="sponsored"` and a
    visible disclosure line; affiliate programs require the disclosure text anyway.

### Nothing to do

Cloaking, hacked content, hidden text, link spam, malicious practices, misleading functionality,
site reputation, sneaky redirects, user-generated spam, scam and fraud, legal removals: none of our
plans touch these. They are in the rulebook as standing rules so nothing drifts into them later
(no bought links, no guest-post schemes, no hidden text, moderation if comments open).

## Changes made today

- New rulebook: `.claude/skills/search-policy/SKILL.md`, loaded by every publishing agent, with the
  ten-point checklist the checker and the publisher run on every page.
- Sources saved in full under `research/discussion/references/google-policies/` and copied into the
  skill's `references/` folder.

## Decisions for the owner

- Do synthesis pieces exist at all, or does every page carry a seed, brief or note? (Recommendation:
  every page.)
- A "How this site is made" page: yes or no.

## Second pass: the generative-AI guidance page and everything it links to

Read on the owner's request later the same day: Google's guidance on using generative AI content and
every page it links to (the Search Quality Rater Guidelines PDF, the ranking systems guide, the title
link, snippet, structured data, alt text, search gallery, image metadata, helpful-content and AI FAQ
pages), plus the Article structured data page, the SEO starter guide and the page experience page.
The rulebook was rewritten to carry them (sections 3, 5, 6, 9, 11 and the checklist grew).

### What the second pass adds that the first did not say

- **Metadata is reviewed like body text.** Google: the fact-check and review "also applies to
  metadata like title elements, meta description elements, structured data, and alternate texts".
  Our plan reviewed the article only. Change: the app's preview shows the title tag, meta description,
  every alt text and a structured data summary beside the piece, so the owner's one review covers
  them. Checklist items 7 and 8.
- **Structured data was not in the plan at all.** Rank Math and the theme emit it, so it must be
  configured and validated: Article markup with author as a Person linked to the author page, dates
  in ISO 8601 with timezone, representative images in three ratios; ProfilePage on the author page;
  BreadcrumbList, WebSite and Organization; markup only for what is visible; Rich Results Test on
  every template change; URL Inspection by the publisher; rich-result reports watched by the campaign
  manager. Goes into the WordPress build and the publisher's live-page check.
- **Alt text has a method.** In-context, one or two sentences, no "image of", decorative images
  alt="", and a diagram's meaning explained in the body text, not only in the alt. Our explainers are
  diagrams, so this becomes a rule in the illustration rulebook: the illustrator writes the alt, the
  writer places the explanation beside the figure.
- **Filler is a rated fault.** Raters rate a page Low for helpful content buried under filler and want
  the most helpful content near the top. The writing style already says answer first; the rulebook
  makes it a check.
- **Titles are main content.** Exaggerated or shocking titles are a Low rating on their own. The
  house title rule now cites this.
- **The paraphrase check has a method, with one limit.** Raters search exact sentences on Google. We
  may not query Google by machine, so the checker compares against the listed sources and spot-checks
  three sentences through the paid research API's search endpoint.
- **No intrusive interstitials.** The newsletter sign-up is a box in the page, never a pop-up or
  overlay. The owner's no-pop-up rule for ads extends to everything.
- **Site diversity.** Google shows at most two pages from one site per query, so each piece in a
  cluster must own a different question. The sits-beside rule already does this; now it has a reason.
- **YMYL-adjacent pieces.** Pay, pricing, contracts, hiring, legal and financial decisions get a mark
  on the card, primary sources for every number, and consistency with expert consensus.
- **Conflict of interest.** Raters discount paid promotion. Book takes and tool mentions must be
  honest, say what the thing is bad at, and disclose affiliate relationships.
- **URLs and structure.** Words, not ids; lowercase, hyphenated; sections as folders where the
  hierarchy helps; descriptive link text; nofollow on links we cannot vouch for; ugc and nofollow on
  any comment links automatically.
- **Image metadata.** The IPTC tag for AI-generated images does not apply, since our thumbnails and
  illustrations are drawn by our own code, not by a generative model. If a generative image tool is
  ever used, the tag goes in.
- **Promotion.** Google's own list of good promotion is social media, community engagement, word of
  mouth and a newsletter people asked for, with a warning not to overdo it.

### Nothing to do

Ranking systems such as BERT, MUM, passage ranking, neural matching, freshness and deduplication
describe how Google reads pages; they ask nothing of us beyond clear writing and one canonical URL.
The original-content system rewards being the original source, which the paraphrase check protects.
Reviews, local news and crisis systems do not apply. Exact-match domain does not apply.

### Decisions for the owner from the second pass

None new. The additions are rules and build items, not choices.

## Third pass: the whole rater guidelines document and the second ring of links

Owner's instruction later on 10 October: read everything. The first two passes had read about a
quarter of the 182-page rater guidelines; the full document has now been read, and a subagent read and
extracted the second ring (technical requirements, content policies, breadcrumb, organization, profile
page, site names, sitelinks search box, FAQ and HowTo status, image licensing, Merchant Center AI
policy, Rich Results Test, image SEO, canonicalization, sitemaps, robots meta, interstitials, Core Web
Vitals, outbound links, SEO starter, do-you-need-an-SEO). The rulebook was rebuilt as a general guide
(`SKILL.md`) with a site layer (`SITE.md`) and a build to-do
(`research/discussion/todo/search-policy-build-checklist.md`).

### What the full read adds to our rules

- The question-farm pattern is named by raters: collecting "People also ask" questions and answering
  them with paraphrased content. Our cached reader questions stay an input, never a page per question.
- Site purpose must match the About page; a site hosting articles outside its stated focus is rated
  deceptive. All categories stay inside UX, product and business.
- A hidden disclaimer that contradicts the pages is deception (the "AI enthusiasts" terms-of-service
  example). Nothing on the site may say otherwise than what the pages are.
- Overstated author claims are a Low rating; fabricated profiles with generated headshots are Lowest.
  The author page is plain and verifiable.
- Reputation is judged off-site; a small site with none is neutral. Authority signals are the measure.
- Answer up front for specific questions; "incidental and indirect" answers rate down.
- Sites that always show today's date are called out; dates must be real.
- Ads disguised as content or navigation, ads following the scroll, and distracting sidebars rate
  down; comments are main content if opened; custom 404 pages with help rate well.
- Opinion is a beneficial purpose, so takes are legitimate when honest and never mean-spirited.

### What the second ring adds

- Noindex only works on crawlable URLs; robots.txt is not an indexing control. Archives and filters
  are kept out with noindex.
- Affiliate links are "paid placements": `rel="sponsored"` preferred, and the search-features policy
  forbids concealed sponsored content.
- `nosnippet` and `max-snippet` also limit input to AI Overviews and AI Mode; a site decides once.
- FAQPage, HowTo and the sitelinks search box are retired; emit none of them.
- Site name markup lives on the home page only, on all duplicate home pages, nested in one WebSite
  node, not testable in the Rich Results Test; Organization name must match it.
- ProfilePage must not carry a placeholder image; breadcrumbs show on desktop and follow a user path;
  the preferred image is never the logo or an image with text; images are `<img>` elements, not CSS.
- Local pages cannot be validated in the Rich Results Test; validation happens live.
- Keep existing creator, credit and copyright image metadata; stripping it may be illegal.

### Decisions for the owner

None new. Everything in the third pass is a rule or a build item.
