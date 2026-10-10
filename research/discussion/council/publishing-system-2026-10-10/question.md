# The question for the council

The owner of userandproduct.com (a solo author with 15 years in product design and product management, building a
Smashing-Magazine-style authority site at the crossing of UX, product management and business) has finalized a proposal
for a "newsroom" of AI agents that plans, writes, illustrates, checks, publishes and monitors the site's articles. A
first council reviewed an earlier version (proposal 2) on 9 October 2026; the owner has since answered every open
question and reshaped the system. The owner asks the council: **what gaps remain in this system, and what should be
improved, with the article pipeline as the first goal?** Suggestions for improvement are wanted as much as gaps.

Read the full proposal before answering (advisors receive a plain-text extract of it):
research/explainers/publishing-system-proposal-5-2026-10-10.html

## The proposal in short (proposal 5, 10 October 2026)

- **The owner's role is direction, not stories.** Each pitch card carries "your note", a text box where the owner says
  how the piece should go (write it this way, lead with that, drop this section). A story from the owner's career is an
  optional extra; many cards will have none. Hard rule: no first-person claim the owner did not give. The content is
  written by the agents.
- **Rhythm: rolling build windows.** Two settings the owner fixes later: block length (ten or fifteen days of publishing)
  and window length (two or three days). Example with ten-day blocks: Dec 28-30 builds Jan 1-10, Jan 7-9 builds Jan
  11-20, Jan 18-20 builds Jan 21-30. At the start of each window one command ("/go", placeholder) opens with the campaign
  manager's report (what happened since the last window), then the planned pieces as cards. Pitches equal the slots in
  the block; a killed card is replaced on the spot from the top of the backlog; "publish later" parks the card. Review in
  publishing order, each piece approved before its own date; the publisher never pushes an unapproved piece.
- **Pace.** Three or four a week for the first couple of weeks, then one a day once the process has gelled, maybe two a
  day later. The ramp is gated by the owner's time (notes at the meeting, review at 30 to 40 minutes a draft: about 5 to
  7 hours a month at two or three a week, 15 to 20 hours at one a day). Backlog water marks scale with pace, about a
  month and a half of output (20 / 50 / 100 approved ideas; refill at about sixty percent).
- **The newsroom app.** Agents write data files only (backlog, cards, report, window plans, decisions). One local page
  (plain HTML and vanilla JS, no build step) reads them: a board by status, the pitch cards with approve, kill, change
  and the note box, the report, a timeline of past windows with snapshots for replay, and a draft preview rendered with
  the article page design where the owner marks corrections on the paragraph. Corrections and decisions are saved as
  data the agents read. Review happens in the app; then the publisher creates the real post in local WordPress, the owner
  confirms once, and that confirmation sends it live on its date.
- **Three ways onto the board.** (1) The explorer's weekly reading. (2) A book the owner names, run on demand: the
  book's ideas turned into reader questions, checked against the keyword store and one paid batch, cards with source
  "book: title"; guards: no summaries, no wholesale frameworks, no invented quotes; the piece teaches the idea in our words
  with the owner's experience and credits the book. (3) The owner's brief: "we should write about X" with the rules the
  owner knows, saved word for word as the seed; the explorer does the legwork and checks each rule against sources; the
  owner's rule stands as "from experience" where sources disagree; it skips the queue, not the card.
- **The explorer's sources.** The paid keyword store; competitor sitemaps and feeds (the campaign manager runs the weekly
  pull and diff, the explorer judges each new page: two-pass reading, title and headings first, full read for
  candidates; each lands on gap, take or nothing, logged so it never resurfaces); cached search questions; the top five
  live pages per idea; the coverage map; a newsroom mailbox subscribed once to newsletters (LinkedIn newsletter editions
  are public articles readable without login, verified); Reddit and Hacker News public feeds; what the owner forwards; a
  book the owner names; the owner's brief. Ordinary LinkedIn posts are not read by script, and no fake profile.
- **Kinds of idea.** Gap, better (a different perspective on a topic rivals cover, valid only when none of the top pages
  cover that perspective), expansion, take (a fact-based response to a rival's claim: only when the owner has lived the
  opposite, has evidence the source lacks, or the source left out a case; takes are rare, two to four in fifty, ride the
  normal window, no fast lane; the checker confirms the rival's claim is quoted accurately), refresh. The gate for any
  idea stays one sentence: "the reader learns X, which the top five pages do not teach." Each card pitches an angle and
  names the existing piece it sits beside. A category opens only as a cluster of at least seven or eight planned pieces.
  Killed cards go to an ideas bin with the owner's reason; nothing is deleted.
- **The campaign manager is a director.** It always holds the site's age, the full publishing history and the keyword
  data. Three modes switched by data, decided by itself: coverage from day one (planned versus published, thin
  categories, orphan pages, index coverage, the sitemap pull, authority signals: links, mentions, direct and returning
  visits); early signal once pages have impressions; performance once a page's numbers mean something (about a hundred
  impressions over 28 days as its rule of thumb). It gives direction forward (which categories and rising terms deserve
  the next windows) through the board. It proposes and never changes the site.
- **Agents.** First build, ten: explorer, researcher, writer, illustrator, thumbnail maker, checker, SEO reviewer,
  editor, publisher, campaign manager. Later, after the article pipeline is settled, social pipelines one by one: a
  LinkedIn writer (posting from a separate LinkedIn page, not the owner's profile) and a reel maker. The main session is
  the managing editor and runs the meeting. Each agent loads one rulebook (skill); writing style, thumbnails and the SEO
  research store exist; illustrations, article SEO review, WordPress publishing and performance review are to write.
- **Build order.** 1 editorial folder, backlog data, the app, the explorer, the campaign manager's coverage mode, the
  "/go" command and the window runner; 2 the illustration and article-SEO rulebooks; 3 the making desk proven on a first
  small window of three or four pieces; 4 WordPress locally, the publisher, the preview-to-local-to-live flow; 5 the
  launch stock in windows; 6 soft launch with Search Console; 7 announcement and the drip; then social pipelines.
- **Launch plan.** About fifty articles live before the public announcement, in six or seven deep categories (seven or
  eight each), plus a books section page (a shelf with the owner's one-paragraph take on each book, affiliate links
  later) and a templates and tools section with a few templates. Why: when the owner announces the site on LinkedIn,
  visitors judge it in seconds; a handful of posts reads as a hobby, a full site reads as a publication, and those first
  visitors are where a new domain earns its first mentions and links. The owner did the same with a sister site
  (Printables: a few hundred pages at launch, then a daily drip) with no harm from Google. The owner's time is the gate
  (about 30 hours of notes and reviews for fifty), so the stock may go live at thirty to forty with the rest as the first
  drip buffer. No backdated dates; the established feel comes from depth and finish (full category and series pages,
  start-here, author page, books shelf, templates, newsletter sign-up, no empty corners). Soft launch two weeks before
  the announcement with the stock scheduled across those weeks, three or four a day, so dates are real and indexing is
  watched before the audience arrives. In the UI there is no sort-by-date; the article shows a quiet "Updated <month
  year>" only.
- **Still open.** Block and window lengths; launch stock size; voice notes later; the LinkedIn pack and social
  pipelines; how LinkedIn newsletter notices reach the newsroom mailbox without access to the owner's personal email; the
  newsletter follow list.

## What the first council said about proposal 2, and how proposal 5 answers it

The 9 October verdict (research/discussion/council/publishing-system-2026-10-09/verdict.md) said: the owner's
experience is the scarce input and gets ten minutes per article; two a week, not six; the build order is upside down
(ideas are not the bottleneck); the gate grades itself; a 90-day rank expectation is fantasy on a domain with no links;
invented first-person detail cannot be caught by a source check; confidentiality of stories; stories run out; no
newsletter; no real readers; one session routing forty hand-offs overflows; measure authority signals; prove the belt on
one owner-written baseline plus three plain-prompt pieces before any agent file.

Proposal 5 answers some of this directly: the owner's input is now direction on every card rather than a story per
piece, so stories cannot run out and confidentiality is the owner's call per note; the pace starts at three or four a
week and ramps only when the owner's review time per piece has come down; the campaign manager measures authority
signals and does not score pages until numbers mean something; the first window is three or four pieces; a newsletter
sign-up is part of the launch; the app removes the routing load from the chat session. It does not take the
"owner-written baseline before any agent file" advice, and it plans a launch stock of about fifty, which is far above
the first council's "about twelve in six weeks". The owner wants the council to judge the finalized design on its own
terms, not to re-argue the earlier verdict point by point.

## Context the advisors should know

- Goal order, set by the owner: (1) authority in both directions, the owner's experience backs the site and the site
  backs the owner; (2) organic search traffic; later books with affiliate links, a tools and links directory, templates,
  calculators, courses.
- The site does not exist yet. Nothing is live, no hosting, no Search Console, no backlinks. Work so far: a keyword and
  SERP research pass, a topic tree of about 210 possible articles in 13 categories, a logo, page mockups (article page,
  code block, illustration and thumbnail systems), three rulebooks (writing style: an experienced teacher's voice, a guide
  with guardrails, every piece should make the reader feel they did something on every screen; thumbnails; SEO research
  store).
- The owner's words on the gate: value first, "people should learn something and think: I haven't seen this approach,
  this is useful for me." Takes must be fact-based, never disagreement for its own sake.
- Constraints: dependency-light (plain HTML, CSS, vanilla JS, WordPress with WP-CLI), everything free or cheap, a hard
  cap on paid keyword spend, no AI attribution anywhere a reader can see, US English, nothing is built until the owner
  says go.

## What is at stake

The owner is about to spend several sessions building this machine and then about fifteen to twenty days producing the
launch stock. If the design has a gap that is not caught now, the cost is paid in those sessions and in the first
impression the site makes on the day it is announced: articles that do not build authority, a review load the owner
cannot sustain, a launch that looks full but reads thin, or a system that optimizes for the wrong signal. The owner wants
the system to be genuinely good, not just to exist, and asks for both gaps and improvements.
