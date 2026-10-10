# Council verdict: publishing system proposal 5

10 October 2026. Question in `question.md`, the proposal in `research/explainers/publishing-system-proposal-5-2026-10-10.html`,
the five advisor responses in `advisor-responses.md`, the five anonymous peer reviews in `peer-reviews.md`. The owner
asked for gaps and improvements, with the article pipeline as the first goal, and asked that the finalized design be judged
on its own terms.

## Where the council agrees

**1. Nothing in the system is required to supply the X.** Four of five advisors found the same hole from different
directions, and four of five reviewers named it the central finding. The gate for every idea is "the reader learns X,
which the top five pages do not teach." Under proposal 5 the owner gives "direction, not stories", a story is "an extra,
never a requirement", and the content is written by the agents from the top five pages, which by definition lack X. The
proposal's own example card shows the gap: "Keep the example from a real product team, not a made-up one." Nothing on the
belt can get that team except the owner. Without a required place where the owner's judgment enters, the explorer writes
the promise, the writer remixes public sources, and the editor grades the promise the explorer wrote. The result is fifty
fluent syntheses with an expert's byline, which is the opposite of goal one.

The fixes converge on something small. The First Principles Thinker: before each meeting the explorer drafts two or three
questions from practice aimed where the top pages fall short ("They hand out twelve sections. Which five survive on a real
team, and why?"), the owner answers by voice in two or three minutes, and the answers become the spine, stated as rules and
judgments, no first person needed. The Contrarian: a required "where X comes from" field (the owner's answer, a named
source, or "derived" with the reasoning written out). The Outsider: one required "only I know this" line, a number, a
mistake, a decision or a real artifact. These are the same idea at three sizes. It keeps the owner's choice of direction
over stories, and it costs minutes, not the ten minutes of storytelling the first council worried about.

**2. The hard rule is too narrow.** "No first-person claim you did not give" stops faked expertise and nothing else. An
invented third-person case study, team, metric or quote has no source to fail against, so the checker cannot catch it.
Contrarian, First Principles and Outsider all want the rule extended to every invented specific, with the checker listing
each example and number with its origin, and refusing any named example it cannot link to.

**3. The build order puts the expensive part before the risky part.** Step 1 holds the backlog schema, a five-view app, an
explorer with eleven sources, coverage mode, the window command and the window runner. The Executor counts five or six
sessions before a single draft exists; the Contrarian says if drafts come back thin all of it is wasted. Both want the
making desk run first on three cards written by hand, with the drafts read as plain preview pages, and the app built
around what that window turned out to need. Two reviewers checked and agreed.

**4. The build order is missing things that are on the critical path.** The Executor, confirmed by the claim-checking
reviewer: a plain HTML and vanilla JS page cannot save the owner's corrections, so the app needs a small PHP save endpoint
under XAMPP and paragraph ids that stay stable across redrafts; neither is mentioned. The child theme, the structure
plugin, Rank Math, the category and series pages, start-here, the author page, the books shelf and the newsletter sign-up
appear in the launch plan as "no empty corners" but nowhere in the build order, and they are four to six sessions of
work. Domain and hosting are not mentioned anywhere, and DNS and a mailbox take days of waiting.

**5. The review-time math is optimistic and the ramp gate points the wrong way.** The 30 to 40 minutes per draft leaves out
the second read after fixes and the notes written at each meeting. And "review time per piece has come down" rewards
skimming as much as a gelled process; the Outsider and the First Principles Thinker both say the owner's minutes are the
one input that creates authority, so less of them is not progress. Gate the ramp on fixes per draft, not on speed.

**6. The expectation line is precision with nothing behind it.** "Top 10 within 90 days, 50 clicks a month by day 120"
on a domain with no links is a guess the campaign manager would then score pages against. Until performance mode, an
expectation should name leading signals only: indexed, impressions on the target phrase, links or mentions earned.

## Where the council clashes

**Add or subtract.** The Expansionist wants more out of the same machine: a principles file where every rule the owner
gives accumulates with an id and the pieces that use it, a takeaway asset on every card, a quarterly report built from the
explorer's log, more takes, a weekly letter, book shelf entries drafted from the book door, clusters ordered as course
modules. Four reviewers named this the biggest blind spot, because every item adds output and none is weighed against the
owner's hours, which the proposal itself names as the gate. The chairman splits it: the principles file is cheap, it
compounds, and it answers a gap the reviewers found (consistency across pieces, below), so it stays and moves to step 1.
The asset per card, the extra takes and the quarterly report wait until after launch. The newsletter sign-up stays in the
launch; the weekly letter comes later.

**Throughput or judgment in the first window.** The Executor's path proves the belt runs and times the reads; the
Outsider and the First Principles Thinker say it never asks whether the first three drafts carry the author. Two
reviewers called this the Executor's blind spot. They are both right, and the first window can measure both at once:
time every step including re-reads, and have a cold reader with no brief write one sentence on what it learned from each
draft, to be compared with the card's learning sentence.

**Veto or label.** The Contrarian would bar any card whose X is "derived" without an owner note. The First Principles
Thinker would label cards "seeded" or "synthesis", cap synthesis at about a quarter of output, and keep it out of the
launch's flagship pieces. The reviewer who weighed the owner's decisions preferred the label, because the veto would push
the owner back toward a note on every card. The chairman agrees: label and cap, and no synthesis among the ten launch
pieces the owner's network will open first.

**What to defer before launch.** The Executor would cut the explorer's sources, takes and the books door before launch,
since the tree already holds about 210 scored ideas and fifty launch cards can come from it. The owner chose those doors
on purpose, and one reviewer objected. The resolution is to defer the building, not the ideas: launch cards come from the
tree and from the owner's briefs, the sitemap diff stays because it already exists and is cheap, and the mailbox, Reddit,
the book door and two-pass rival reading are built after launch.

## Blind spots the council caught

These came out only in the review round. None of the five advisors raised them.

**Google's scaled-content policy.** Four of five reviewers raised it independently. Fifty agent-written pieces scheduled at
three or four a day on a brand-new domain with no links is the shape Google's scaled content abuse policy describes,
whatever the method of production. Printables is not a precedent: template pages are a different kind of content from
bylined expert articles. The chairman's reading: the policy targets content made at scale primarily to rank, and the
defense is real owner input in every piece, quality a reader can feel, and a pace that does not look like a dump. That
argues for the seed on every card as a floor, a gentler soft launch (one or two a day over three or four weeks rather
than three or four a day over two), and letting the first window's measured numbers set the stock size.

**Consistency across fifty pieces.** Two reviewers. Drafts made in parallel will contradict each other (one PRD piece says
one page, another says three), and nothing checks a draft against the rest of the site. Cards also link only to pieces
already written, so the first pieces in a stock never get links back from the later ones. Fixes: the principles file
becomes the source of truth each draft is checked against; a linking pass at the end of each window adds links from
earlier pieces to the new ones, which the publisher can do as post updates.

**Positions, not facts.** One reviewer, and the chairman thinks it is the sharpest point in the round. The hard rule and
its extension cover claims. But every "do this, never that" under the owner's byline is read as the owner's opinion,
with or without an "I". An agent's recommendation the owner does not hold is a borrowed opinion with his name on it, and
his network will notice. The editor should list every position a draft takes, and the owner approves, rewords or strikes
each one before reading the prose. That list is also the fastest possible review, and it is the natural shape of "your
note" after the draft exists.

**No originality check.** The writer works from the top five pages and from books, and no station tests a draft for close
paraphrase of them. That is a copyright risk and an authority risk. One cheap check at the checker's station.

**The owner misses a window.** Nothing unapproved goes live, so one sick week empties the calendar. Keep a buffer of
approved pieces and write the slipped-date rule down.

**Insider shorthand.** The Outsider tripped over "the tree", "mockup A", "tint", "the store" and "/go", and found the
proposal saying "four kinds of idea" where the card lists five. A short glossary and one metaphor kept throughout.

## The recommendation

Keep proposal 5's shape. The rolling windows, the window command, the app as the owner's surface, the campaign manager as
director, the three doors onto the board, the cluster rule, the ideas bin and the decision to launch full are sound and
were not seriously challenged. Change seven things, most of them small:

1. **A seed on every card.** Two or three practice questions drafted by the explorer where the top pages fall short, answered
   by the owner by voice or in a line, saved word for word, traced on the card as where X comes from. Cards are labeled
   seeded or synthesis; synthesis is capped at about a quarter and kept out of the ten flagship launch pieces. The owner's
   role stays direction, not stories.
2. **Widen the guard.** The hard rule covers every invented specific, not only first-person ones; the checker lists each
   example, number and quote with its origin and refuses named examples it cannot link to; the checker adds a close-paraphrase
   check against the top five and any book used; the editor lists the positions a draft takes for the owner to approve,
   reword or strike before reading the prose.
3. **Reorder the build.** First the making desk, on three cards written by hand from the tree, drafts rendered as static
   preview pages, every step timed including re-reads, a cold reader on each draft. Then the app around what that window
   needed, with the PHP save endpoint and stable paragraph ids. WordPress, the child theme, the structure plugin, Rank Math
   and the section pages run in parallel from the start, and the domain and hosting are bought now. The explorer's extra
   sources, the book door and two-pass rival reading come after launch; the sitemap diff stays.
4. **A principles file from day one.** Every rule the owner gives, in a seed, a note, a brief or a correction, with an id,
   the owner's words and the pieces that use it. Drafts are checked against it for consistency, and it becomes the canon the
   site is known for.
5. **Honest expectations.** Leading signals only until performance mode. The ramp is gated on fixes per draft, not on
   review minutes.
6. **Set the stock from the first window.** Measure the owner's real minutes per piece, re-reads included, and set the launch
   stock from that number. Expect thirty to forty, not fifty. Spread the soft launch over three or four weeks at one or two
   a day, with the ten pieces the owner's network will open first seeded hardest.
7. **Two small rules.** A buffer of approved pieces and a slipped-date rule, and a linking pass at the end of each window so
   earlier pieces link to later ones.

The chairman sides with the majority on the central finding and with the minority on keeping the owner's doors. The
Expansionist's canon is kept against four reviewers' objection because it also solves the consistency gap.

## The one thing to do first

Run the first window now, before any app or explorer is built: three cards written by hand from the tree, each with two or
three seed questions the owner answers by voice, through the making desk, with every step timed including the owner's
re-reads, and a cold reader writing one sentence per draft on what it learned. That one window answers the three questions
everything else depends on: does the belt produce a draft worth reading, do the drafts carry the owner's judgment, and what
is the owner's real cost per piece. The stock size, the pace, the ramp and the shape of the app all follow from those three
numbers.
