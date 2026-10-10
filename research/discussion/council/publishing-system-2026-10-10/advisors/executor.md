# The Executor

"Each build step is a session or two." Step 1 isn't. It holds the backlog schema, a five-tab app (Board, Cards, Report, Timeline with snapshot replay, Preview with corrections marked on the paragraph), an explorer with eleven sources, coverage mode, /go and the window runner. That is five or six sessions, and the owner still has zero articles, because the making desk only arrives in step 3.

**Dependencies that bite:**

- **The app can't save.** "Your clicks, notes and corrections go back as data," but a plain HTML and vanilla JS page cannot write files. It needs a PHP save endpoint under XAMPP, plus paragraph IDs that stay stable through redrafts. Neither is mentioned.
- **Coverage mode has nothing to measure.** "Index coverage in Search Console... direct visits." There is no domain, hosting, Search Console or analytics. Before launch, coverage is "count published against the tree": a 30-line script, not an agent.
- **The theme isn't in the build order.** Step 4 says "WordPress locally, the publisher." Nothing builds the child theme, the structure plugin, Rank Math, category and series pages, start-here, the author page, the books shelf or the newsletter sign-up. Those are what make "no empty corners" true. It's a second project of four to six sessions, sitting unscheduled on the critical path.
- **The explorer isn't needed before launch.** The tree already holds about 210 scored ideas, so fifty launch cards can come from tree-simplified-v1.1. Mailbox, Reddit, the books door and rival two-pass reading can wait.
- **Hand-off volume.** Seven stations times ten pieces is seventy runs per window. The window runner must be a script that walks article folders by file state, not a chat conversation.
- **Owner-hours.** Fifty at 35 minutes is about 30 hours, or 1.5 to 2 hours a day over 15 to 20 days. Plan the stock at 30.

**Fastest credible path:**

1. **Monday.** Hand-write three cards as JSON from the tree. Run a three-station belt: research plus writing, figures plus thumbnail, then checking, SEO and editing. Render final.md in mockup A with a static script. The owner marks fixes in a feedback file and times each read. One session gives a real number.
2. **In parallel, from Tuesday.** Local WordPress, child theme, plugin, Rank Math, section pages, then the publisher with WP-CLI scheduled posts. Buy the domain and hosting now, because DNS and mailbox setup take days of waiting.
3. **A second window of six.** Add the Cards tab and the PHP save. Split stations only where the merged ones failed.
4. **The launch stock**, built in windows.
5. **After launch.** Explorer sources, the campaign manager's real modes, Timeline, takes, books, voice.

**Cut or defer:** Timeline snapshots, the kanban, the mailbox, the books door, takes before launch, the ten-agent split, and the campaign manager as an agent before Search Console exists. Make the making desk first and run WordPress alongside it, starting now. Grow the machine out of the first three articles, not the other way round.
