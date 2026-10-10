---
name: search-policy
description: Google Search policy rulebook for everything userandproduct.com publishes. Built from Google's spam policies, its guidance on using generative AI content and every page that guidance links to (the Search Quality Rater Guidelines, the helpful-content page, the ranking systems guide, the title link, snippet, structured data, alt text and page experience pages, the AI-content FAQ, the SEO starter guide), all saved in references/ and read in full on 10 October 2026. Load this skill whenever an article, template page, tools page, books page, category page or any indexable page is pitched, briefed, written, checked, SEO-reviewed, edited, published, refreshed or measured, whenever a title, meta description, structured data, alt text, internal link, outbound link, affiliate link, date, URL or redirect is set, whenever the theme or plugin emits metadata or markup, and whenever the owner says "spam policy", "scaled content", "helpful content", "E-E-A-T", "rater guidelines", "thin page", "filler", "AI content", "disclosure", "structured data", "schema", "rich results", "alt text", "affiliate links", "penalty" or "manual action". Every publishing agent (explorer, researcher, writer, illustrator, checker, SEO reviewer, editor, publisher, campaign manager) obeys it; the checker and the publisher run its checklist on every page.
---

# Search policy rulebook for userandproduct.com

Google does not ban content made with software. It bans content made to game search, and it
rewards content made to help the person who reads it. That is the whole rulebook in two sentences.
Everything below says what it means for each station.

The sources are in `references/` (plain-text extracts of the Google pages, with the dates they were
read). When a rule here and the source disagree, the source wins; update this file. Google's own
line on generative tools, from its guidance page: they are "particularly useful when researching a
topic, and to add structure to original content", and "it is critical to manually factcheck and
review all AI-generated content for accuracy and trustworthiness before publishing", metadata
included.

## 1. The one test every page must pass

A page exists because a reader who came straight to the site would be glad it is there. Not
because a search engine might send visits. Google's words: using automation "to produce content for
the primary purpose of manipulating search rankings" is a spam policy violation, and "content
primarily made to attract visits from search engines" is the first warning sign of search-engine-
first content.

So on every pitch card the explorer answers, in one line, **"Why would our own readers want this if
search did not exist?"** If the honest answer is "they wouldn't, but the phrase has volume", the card
dies. Search volume ranks ideas that passed. It never admits one.

## 2. Scaled content abuse: the policy that fits our method

Google's definition: "many pages generated for the primary purpose of manipulating search rankings
and not helping users ... large amounts of unoriginal content that provides little to no value, no
matter how it's created." Its examples: generative tools making many pages without adding value;
scraping or synonymizing; stitching content from different pages; pages that make little sense but
carry keywords; several sites to hide the scale. The rater guidelines (section 4.6.5) add the
defining attribute: "an abundance of content with little effort or originality with no editing or
manual curation", and tell raters to rate a site Lowest on strong suspicion "even if unsure of the
method of creation".

Raters judge **effort, originality, talent or skill, and accuracy** (section 3.2). On effort:
"generative AI to produce large amounts of text without manual oversight or curation represents
little to no effort. Attribution or giving credit to other sources doesn't replace the need for
original effort." Section 4.6.6: the Lowest rating applies when "all or almost all of the main
content is copied, paraphrased, embedded, auto or AI generated, or reposted from other sources with
little to no effort, little to no originality, and little to no added value", and "paraphrased"
means "unoriginal content that exists on other pages, with different wording, organization or
phrasing", by a person or a tool.

Our rules, which are what "oversight", "curation" and "original" mean here:

- **Every page carries the owner's judgment.** At least three quarters of pieces carry a seed (the
  owner's answers to the card's practice questions), a brief (the owner's rules as the spine) or a
  note that shapes the piece before it is written. Up to a quarter may be synthesis pieces (owner's
  decision, 10 October 2026): written from understanding as a fresh take, with the owner's feedback
  on the draft and the owner's keep-reword-strike on its positions as the oversight, labeled on the
  board, never among the flagship launch pieces. A synthesis piece is never a summary of the top five
  pages and never a stitch of passages from them. The writer reads to understand, then writes its own
  structure, examples and reasoning.
- **Nothing publishes unreviewed.** The owner reads every piece in the app and confirms it once in
  local WordPress before it goes live. The publisher refuses any post without that confirmation on
  record. This is the "manual oversight" the policy asks for, and it must be true, not nominal. The
  review covers the metadata too (section 6).
- **No stitching, no scraping, no spinning, no close paraphrase.** The writer never assembles a piece
  from passages of other pages, never restates a source in different words, never reproduces a
  book's chapter or framework wholesale. The checker runs the paraphrase check in section 3.
- **No filler.** Raters rate a page Low for "a large amount of low quality and unhelpful filler"
  and for helpful content buried under it (section 5.2.2). The most helpful content sits near the
  top. No throat-clearing introductions, no commonly known facts padded in, no history of the
  topic before the answer. Length is never a target: "there's no magical word count".
- **No page without a reason of its own.** No tag, date, author-archive, filter or search-result-like
  pages in the index. Category and series pages are a browseable hierarchy with their own intro text.
  Attachment pages are off. Filters never make indexable URLs.
- **Volume is not the signal; value is.** A full launch of fifty reviewed pieces is an ordinary
  launch. Fifty pieces that each fail section 3 would be scaled content abuse at any pace.

## 3. Originality, value and accuracy, page by page

From Google's self-assessment questions and the rater guidelines. The checker answers each one for
every page; two "no" answers send the draft back.

- Does it give original information, analysis or a judgment from the owner's experience, beyond
  what the top five pages say? (The learning sentence, delivered.) Raters' words for High: "a
  personal perspective based on first-hand life experience"; for Low: "information summarized from
  other sources with little added value".
- When it draws on other sources, does it add substantial value rather than rewriting them?
- Is it complete for its purpose, so the reader does not need to search again?
- Is it something a reader would bookmark, share or expect in a printed magazine?
- Does it have easily verified factual errors? Any error fails the page. "Mild inaccuracies on
  informational pages are evidence of Low quality"; many, or harmful ones, are Lowest.
- Is it produced with care: no spelling or style slips, nothing that reads hastily made, well
  organized and edited?

**The paraphrase check.** Raters find copied and paraphrased content by searching exact sentences
and by asking whether the page "only contains commonly known information", "has high overlap with
well established sources" or "appears to summarize a specific page without any added value". The
checker does the same on every draft: it compares the draft against every source the brief lists
and every book the piece draws on, and it spot-checks three distinctive sentences through the paid
research API's search endpoint, never by querying Google directly (section 10). A draft that reads
as a restatement of one source, or of several, goes back.

**Accuracy and consensus.** Our topics are mostly not "Your Money or Your Life", but pieces that
touch pay, pricing, contracts, hiring, legal or financial decisions edge toward it. The card marks
those, the researcher cites primary sources for every number, and the piece stays "consistent with
well-established expert consensus" where consensus exists. Generative tools "don't retrieve facts,
but predict a likely sequence of words", so every fact, number, name and quote in a draft is treated
as unverified until the checker has opened its origin.

**Warning signs written as rules.** Do not produce pieces on many topics "in hopes that some might
perform". Do not enter a topic "without any real expertise, mainly because you thought you'd get
search traffic" (the cluster rule and the owner's categories keep us inside what the owner knows).
Do not write about a thing "simply because it seems trending" (a take needs the owner to have lived
the opposite, have evidence the source lacks, or see a case the source left out).

## 4. Who, how and why

**Who.** Every article carries the owner's byline, and the byline links to an author page with real
background. The About page says what the site is and who runs it. Raters start E-E-A-T from "the
About us page ... or profile page of the content creator" and from "what is visible on the page",
so the author page must show the fifteen years in fact, and the main content must show experience,
which is what the seed and the positions list are for. Never fabricate a creator profile: no
made-up names, no invented credentials, no generated headshots. The owner is the author of record
because the owner directs, seeds, reviews and approves every piece, and that must stay true in
fact. **Conflict of interest:** raters discount reviews "from an influencer who is paid to promote
the product". Book takes and tool mentions are honest, disclose any affiliate relationship, and say
what the thing is bad at.

**How.** Google does not require an AI disclosure and says not to give AI a byline. It says
disclosures "are useful for content where someone might think 'How was this created?'". Owner's
decision (10 October 2026): no "How this site is made" page. No per-article label and no tool or
model names appear anywhere a reader can see. Image metadata: Google's generative-AI page asks for
IPTC `DigitalSourceType` of `TrainedAlgorithmicMedia` on AI-generated images (a Merchant Center
requirement, a suggestion for Search). Our thumbnails and illustrations are drawn by our own code
from our own rules, not by a generative image model, so the tag does not apply. If a generative
image tool is ever used for a published image, embed that tag.

**Why.** Each piece is made to help the person reading it. Internally, the expectation line on a
card names reader outcomes and leading signals (indexed, impressions on the target phrase, mentions,
links), never a rank target as the purpose of the piece. "E-E-A-T is not a ranking factor"; it is
what the page has to be.

## 5. Titles, headings and keywords

- **The page title summarizes the page honestly.** Raters treat the title as main content and rate
  "exaggerated or shocking titles" as Low "because of the poor user experience that results when
  users see the actual MC". House rule: contrast and curiosity, not clickbait; the title states the
  point and the first screen pays the promise.
- **Every page has one `<title>`,** descriptive and concise, unique on the site, no boilerplate that
  varies by one word, no vague words like "Home", the site name once at the end after a delimiter,
  the same language as the page, no stale year. One visually dominant main heading, the first `<h1>`,
  so Google does not pick another line as the title link.
- **Use the words readers use,** in the title, the main heading, alt text and link text, once and
  naturally. Never repeat a phrase until it sounds unnatural, never list variants, never add a block
  of keywords; Google's title page calls that spammy and its starter guide says keyword stuffing
  "is against Google's spam policies". The SEO reviewer strikes it. Expect both the expert's word and
  the newcomer's word for a thing, and use each where it belongs; no meta keywords tag, no word
  count target, no keyword-stuffed URLs.
- **Title rewrites by the campaign manager** for a page with impressions and no clicks obey this
  section. A clickier title that overpromises is refused.
- **No hidden text or links.** Accordions, tabs, tooltips and screen-reader-only text that helps
  accessibility are fine. Text hidden to feed search engines is not.

## 6. Metadata is content: descriptions, alt text, structured data

Google's generative-AI page says the fact-check and review "also applies to metadata like `<title>`
elements, meta description elements, structured data, and alternate texts for images, which can
appear in Search results." So the app's preview shows the title tag, the meta description, every
alt text and a summary of the structured data beside the article, and the owner's review covers
them.

- **Meta description:** one or two sentences unique to the page, a true summary that would make a
  reader click for the right reason; never a keyword list, never the same text across pages. The
  home page and section pages get site-level descriptions; every article gets its own.
- **Alt text:** describes the image in the context of the surrounding text, in one or two
  sentences, no "image of", first word capitalized, final period, no all caps, consistent for a
  repeated image. Decorative images get `alt=""`. A diagram or chart gets a short alt text and its
  full meaning explained in the body text next to it, never only in the alt. The illustrator writes
  the alt text with the figure; the writer places the explanation in the body.
- **Structured data:** JSON-LD, emitted by the theme and the SEO plugin, never hand-pasted per post.
  Articles carry `Article` (or `BlogPosting`) with `headline`, `image` (crawlable, representative,
  16:9, 4:3 and 1:1, at least 50,000 pixels), `datePublished` and `dateModified` in ISO 8601 with
  timezone, and `author` as a `Person` whose `name` is only the name and whose `url` is the author
  page; the author page carries `ProfilePage`; section pages carry `BreadcrumbList`; the site carries
  `WebSite` and `Organization` with the logo. Markup describes only what is visible on the page,
  never ratings or reviews that are not there, never a misrepresented author or purpose; it is "a
  true representation of the page content". `dateModified` moves only when the content substantially
  changed (section 8). Every template change is validated with the Rich Results Test before deploy,
  the publisher runs the URL Inspection check on each new page, and the campaign manager watches the
  rich result reports in Search Console. A structured data manual action costs rich results, not
  rank, but it is a trust signal lost for nothing.
- **Open Graph and social images** describe the page honestly, same title, same image as the
  featured image.

## 7. Links

- **Outbound links** go to sources worth reading, with descriptive link text that says what the
  target is. Link when it helps the reader or corroborates a claim. A link to a source we cannot
  vouch for carries `rel="nofollow"`. Links to books, tools or anything that pays us carry
  `rel="sponsored"` and a visible disclosure near them. Nothing we are paid for passes ranking
  credit.
- **Never buy, sell, trade or automate links.** No link exchanges, no "write about us for a link",
  no paid guest posts with optimized anchors, no links in widgets or footers distributed to other
  sites, no directory submissions for ranking. Mentions and links are earned by pieces worth citing
  and by the owner telling people about them. Google's own list of good promotion: social media,
  community engagement, word of mouth, a newsletter people asked for; and "you can overdo promoting
  your site and actually harm it".
- **Internal links** connect each piece to the pieces it sits beside and to its category and series
  pages, in plain words. A linking pass at the end of each window adds links from earlier pieces to
  later ones. Links are crawlable `<a href>` elements, never JavaScript-only.
- **The books shelf is not a thin affiliate page.** Every entry has the owner's own take, what the
  book is good for and for whom, where it is wrong or dated, in the owner's words. Google's reviews
  system rewards "insightful analysis and original research, written by experts or enthusiasts who
  know the topic well"; a page of blurbs with buy links does not ship.

## 8. Dates and refreshes

- A page shows one quiet "Updated <month year>" and it is the real date of the last substantial
  change, matching `dateModified`. Never change a date to look fresh. Never backdate.
- A refresh changes content because the world changed or the page was wrong, and only then does the
  date move. Adding or removing lots of pages "to seem fresh" is not a strategy; Google says plainly
  it does not work. "Check in on previously published content and update it as needed, or even
  delete it if it's not relevant anymore": the campaign manager's review date does this.

## 9. One URL per page, site structure, no doorways, no sneaky anything

- One canonical URL per page, set by the SEO plugin. No near-duplicate pages aimed at similar
  queries; the "sits beside" field on every card exists so two of our pages never compete for one
  question. Google's site diversity system shows at most two pages from one site for a query, so a
  cluster's pieces must each own a different question.
- URLs are short, in words a reader understands, lowercase, hyphenated, no dates or ids; sections as
  folders where the hierarchy helps. Redirects only for real reasons (a moved page, two pages
  merged), and search engines and readers see the same page.
- The site is one domain, served over HTTPS. No subdomains or sister sites made to spread content or
  to continue a practice after a warning.
- The domain userandproduct.com has no prior history (no archived snapshots as of 10 October 2026),
  so expired-domain abuse does not apply. If the site ever moves to a bought domain, check its
  history first.

## 10. What our tools may and may not touch

- **Never send automated queries to Google.** No rank checkers that query google.com, no scraping
  of results pages, not even for the paraphrase check. Google calls this machine-generated traffic
  and it violates both the spam policies and the terms of service. Keyword, SERP and sentence checks
  go through the paid research API; our own performance data comes from Search Console and the
  site's analytics.
- Rival sitemaps and feeds are read for research only. Nothing from them is republished.
- The explorer reads rival pages and books to find what is missing; the writer never works from
  their text.

## 11. Page experience, ads, comments

- Good Core Web Vitals, HTTPS, mobile first, the main content easy to tell from everything else.
- **No intrusive interstitials.** No pop-ups or full-screen overlays for the newsletter, for cookies
  beyond what the law requires, or for anything else. The newsletter sign-up is a box in the page.
- Ad units follow the layout rules already set (labelled, never covering content, at most three in
  view, mobile density under thirty percent). Ads never pass ranking credit and never outweigh the
  content on a page. Raters: "the presence or absence of Ads is not by itself a reason for a High or
  Low rating", but ads that block or interfere with the main content are.
- If comments are ever opened, they are moderated and links in them carry `rel="ugc"` and
  `rel="nofollow"` automatically.
- Nothing on the site tricks a reader: no fake tools, no "download" buttons that lead elsewhere, no
  claims of a feature that does not exist. A template or calculator page is main content only when
  it works and when the page explains when and how to use it.

## 12. The checklist the checker and the publisher run

Before a draft reaches the editor, and again before the publisher pushes it live:

1. Reader reason: the card's "why our readers want this" line is present and honest.
2. Owner's judgment is in the piece: seed, brief, note or approved positions; named on the card.
3. Originality: passes section 3; the paraphrase check against every listed source and book is
   clean; no filler ahead of the answer.
4. Accuracy: every fact, number, name, quote and example has an origin the checker opened; no
   invented specifics; no easily verified errors; YMYL-adjacent pieces cite primary sources.
5. Byline and author page link present; no fabricated authorship anywhere; affiliate relationships
   disclosed where a book or tool is recommended.
6. Title and `<title>` honest, unique, one dominant `<h1>`, no stuffing, no hidden text.
7. Meta description unique and true; every image has context-true alt text or `alt=""`; diagrams
   explained in the body.
8. Structured data present, true to the visible page, dates and author correct, Rich Results Test
   clean on the template, URL Inspection clean on the page.
9. Links: sources descriptive; paid links `rel="sponsored"` with disclosure; untrusted links
   `nofollow`; internal links to neighbours, category and series; all crawlable.
10. One canonical URL; no duplicate target; no indexable filter, tag, date or attachment pages
    created; URL in words.
11. Date is real and matches `dateModified`; refresh date moved only for a substantial change.
12. Owner's confirmation on record before anything goes live.

A page that fails any item does not publish. The publisher writes the failed item in the check
report and the piece goes back to the station that owns it.
