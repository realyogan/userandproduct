# Council responses, anonymised (A to E)


## Response A

The research is done. The approach fails if the owner keeps refining it, because nothing is built, nothing is committed and no articles exist yet. Two days and $3.55 produced a tree of 210 articles. The next-session plan still puts a re-score, a `topic-tree-v1.3.md`, a retrofit document, a five-post-type content model and a GitHub setup ahead of WordPress. That is weeks of preparation before the first word gets published. More research will not change much now. The owner's writing hours are what limit the launch.

**The arithmetic doesn't work as planned.** Wave 1 is 81 articles. At three a week that is 27 weeks, and the full in-brief tree is about 14 months. One practitioner writing three *substantial* pieces a week won't keep that up. Plan for two and treat three as a bonus, which makes Wave 1 about 40 weeks. Launch with a fixed small set, not "Wave 1":
- 12 articles across three topics only: requirements and PRDs, user stories, and UX research. These are the lowest-difficulty topics (KD 9, 23 and 8) and where 15 years of hands-on experience shows.
- Write the first piece first: "PRD: Template and Examples" (18,100 searches, KD 9). The template download is part of the same page, so Templates gets a launch item at no extra cost.

**Cut the launch sections hard.** The plan opens five sections at once. That means two Links categories of about 45 to 50 entries, about 12 templates, a three-mode sample-size calculator (that is software, with testing) and two book lists. At launch, ship Articles plus the templates that come with them. Links, Books and Tools come after 20 articles are live.

**Make the one irreversible decision safe.** URLs are planned as /category/article/, and "Requirements as its own category" is still undecided. Use flat /article-slug/ permalinks. Categories can then move later without redirects.

**Close the open decisions by default today.** Project management (799,180 searches, KD 39, Atlassian on page one): no for now. Web design and analytics: no. Owner_fit: rate only the three launch topics, which takes ten minutes. Skip the v1.3 re-score.

**Monday morning:**
1. 09:00: the owner answers the four pending decisions in one 30-minute sitting, using the defaults above.
2. 09:30: commit `research/` and create the repo.
3. A subagent runs the WP-CLI setup: GeneratePress child theme, a plugin with one post type plus the categories, Rank Math. That is one day, in parallel.
4. The owner drafts the PRD article in plain text. Claude has the brief ready by 09:00.
5. Friday: three drafts done and WordPress running locally.

Publish the first article as soon as it is ready, not when the whole launch set is. Ranking takes months, so the clock should start now. Any plan that doesn't get an article live within two weeks is still just planning.


## Response B

From outside this world, I see a careful plan for where the owner's articles could rank on Google. I don't see a magazine. Both pages are written for the owner and the search engine. Neither one has a sentence written for me, the visitor.

**Category names.** About half work for an outsider. "Accessibility", "Product metrics" and "Growth and pricing" tell me what I'll find. The rest only mean something if you already know the field. I can't tell "UX design" from "UI design", or "Product management" from "Product strategy" from "Product discovery". Three of the thirteen categories start with "Product", and a fourth, "Project management", differs from "Product management" by one word. "Product discovery" sounds like finding products to buy. Yet it holds user stories and PRDs, which the page itself admits might belong in a category called "Requirements". If the people who built the tree aren't sure where things go, a visitor won't be either.

**Jargon I hit on the pages:** UX, UI, PRD, TPM, APM, PO, OKR, KPI, NPS, CSAT, RICE, ICE, SAFe, VPAT, WCAG, "jobs to be done", "product-market fit". The planning words are worse: "units", "scan groups", "parked", "soft shelf", "wave", "intent mix". The hover card on each category shows a ranking score and a difficulty figure. That's internal data. A reader doesn't care how hard a topic is to rank for.

**Would I know where to go?** Only if I arrived with a word to look up. That's exactly what the data says most people do: 67% of searches are "what is X". So the tree is built for someone who leaves once their question is answered. Nothing on these pages gives that person a reason to come back.

**What an ordinary visitor would expect and can't find:**
- **Who the author is.** The whole plan rests on the owner's credibility, yet the owner doesn't appear on either page. There's no About page and no "who I am, what I built, why trust me".
- **Starting points by person.** For example: "New to product management? Start here", "Designers moving into product", "Leading a team". The audience list in the brief (designers, PMs, founders, career switchers) never shows up as a way in.
- **Anything that feels like a magazine.** I see no newest pieces, no point of view, no opinion and no series. The site is meant to read like Smashing Magazine, but the plan is a glossary with templates attached.
- **A reason to return.** There's no newsletter and no "what's new this week".

**Direct verdict:** the research answers "what can we rank for?" well. It doesn't answer "why would anyone come back?" Rename the categories for what readers are trying to do: "Talking to users", "Deciding what to build", "Writing specs and stories", "Measuring what works". Put the author on the front page. And add a "start here" path for each kind of reader before any URLs go live.


## Response C

The main flaw is that the plan aims at the second goal and calls it the first. The owner ranked authority first, but every number in this approach measures search demand. And the demand that exists is the kind that builds the least authority and is the easiest for AI to absorb:

- 67% of the demand we count as ours is "what is X".
- Every head term has an AI Overview.
- Only 6 of 68 head terms have a soft page one.

Look at the Wave 1 head articles: "Closed-Ended Questions in Research" (27,100), "Story Points Explained", "What Is Product Management?", "Product Life Cycle Stages", "Software Requirements Specification: What Goes In". That is Coursera's and Atlassian's lineup. Someone with 15 years of experience who puts their name on it gets filed with content farms, not next to Smashing. The best-scoring unit, "product owner and product manager roles" (78.6), is people searching job titles. The "user interviews" demand turns out to be mostly a brand.

The single most important input was left out of the score on purpose. The report says it plainly: "owner_fit is empty. The score ranks the data, not the author's authority." A launch of 81 articles was proposed before the author rated a single topic. Six months of writing is being set by percentile ranks across 91 units with weights someone picked (demand 25, difficulty 20...). Those ranks moved a lot in one day: prioritization went from 74.2 to 55.1 and the category count went from 11 to 13. A model that moves that much under hand review is not stable enough to commit URLs to.

The data also contradicts the plan's own premise. The models are small: NN/g gets about 63K visits a month and Smashing about 17K. Reddit holds page one on 13 of 16 links pages, and Reddit and LinkedIn hold page one across the field. That is where this audience actually goes to judge someone's credibility. Yet the plan has no LinkedIn, newsletter or community channel. Nothing in it builds the owner's name except Google, on a brand-new domain. "KD 8, easy" is misleading when the page one for that phrase is Atlassian and Coursera.

The workload doesn't fit one author:
- 81 articles at three a week is 27 weeks with no slack.
- The whole tree is about 14 months.
- On top of that come four more sections at launch: a directory of 25 to 30 product management tools plus about 20 design tools to keep current, about 12 templates, a calculator, and two book lists.

Three substantial pieces a week from one practitioner, with drafting help, is how a site slides into generic text that Google demotes. That puts at risk the credibility the site was meant to build.

The evidence base is thin too. The "Google Ads check" is "the same series as Labs (not an independent check)". Only the top 30 phrases per unit were read by hand, and 12% of the volume is "other".

What I'd ask before any "go":
- Which 10 articles could only this owner write?
- What does month 3 look like if Google sends almost nothing?
- Where is the plan for getting readers that doesn't depend on Google?


## Response D

The plan is sized as a blog with side sections. The data points to something bigger: a toolkit with a magazine wrapped around it. You're treating Templates and Tools as later extras, and that is where the upside is.

**The assets are the moat, not the articles.** Templates and Tools carry the biggest single numbers in the files:

- **Sample size calculator:** 14,990 adjusted searches, with power analysis and survey modes on top.
- **User story templates:** 11,150.
- **VPAT template:** 5,400.
- **PRD templates:** 2,900, the one template query Phase 0 found with a weak page one.

Look at where template intent sits: 41% of user-story searches, 34% of roadmap searches, 33% of PRD searches. An AI Overview can't hand anyone a working calculator or a filled-in PRD. Every head term has an Overview, so build what an Overview can't replace. Each Wave 1 article (PRDs, user stories, roadmaps) should ship with its template or tool on day one, not in a later wave.

**Every download is an email signup.** The BRD lists "email subscribers" as an objective, and the plan never mentions them. A template library behind a free email gate turns search traffic into an audience you own, whatever Google does next. The list later becomes the launch channel for courses.

**The field's leaders are small, so the ceiling is low.** NN/g gets about 63K visits a month and Smashing about 17K. Being the leading practitioner magazine across UX, product and business together is within reach in a couple of years. Nobody holds the "and business" part.

**Books are the quickest win for the owner's name.** Reddit and Amazon hold 11 of the 12 book page ones, and 7 of the 12 are weak. The files show personal practitioner lists outranking publications, which is exactly what a 15-year practitioner can write. Affiliate links can start in month one.

**The research itself is publishable.** The work mapped 4.33M monthly searches, found 2.45M that are really this field's, and showed that 67% of them are definitions. Publish that as a yearly "what UX and product people search for" report. The niche has nothing like it, it earns links, and it builds authority in both directions on the first day.

**Two things are being undervalued:**

- **Rising terms.** 45 of the 68 head terms have grown over five years: PRD by 8.40x, roadmaps by 5.11x, product management by 3.84x. These are good markets to grow with.
- **The Frameworks library (BRD 4.4).** It dropped out of the five sections. As a hub linking each framework to its article, template, calculator and book, it is what makes all of this a platform rather than a blog.

**Courses are already sitting in Wave 1.** PRDs, user stories, roadmaps and discovery add up to a course on writing product docs that ship. With the templates as the course materials, the first paid product comes out of work already planned.

Plan the launch around 81 articles plus about 8 of these assets, not 81 articles alone.


## Response E

You're asking the wrong question. "Is this the right structure and launch set?" assumes the problem is getting found on Google. The BRD and context.md both put authority first: "the experience backs the site, the site backs the owner." Traffic is second. Two days and $3.55 went into a detailed map of what strangers type into Google, and that map tells you nothing about the owner's main asset, which is 15 years of practice.

Look at what the data actually says. 67% of the 2.45M searches you counted as "ours" are "what is X." Every head term has an AI Overview, and only 6 of 68 have a soft page one. So the demand the tree is built on is the demand Google now answers itself, and the pages still ranking for it are Reddit, Atlassian, ProductPlan and Coursera. A "what is a PRD" explainer from a 15-year practitioner reads exactly like one from a content farm. It doesn't build authority. It makes the owner interchangeable with everyone else.

Then look at the models. Smashing gets about 17K visits a month and NN/g about 63K. Neither became an authority through search volume. They got there by having a point of view that people pass around, and search came later.

The field the whole plan depends on is still empty. `owner_fit` was "left empty for the owner." Wave 1, 81 articles and six months of writing, was picked by score with no input on what the owner knows best, has shipped or strongly believes. That's the most important variable, and it's missing.

Rebuild from the goal:
1. **Which 20 to 30 pieces can only this owner write?** Real decisions, failures, teardowns, how they actually run discovery or write a PRD. That's the authority engine, and LinkedIn is its channel (context.md already says so). Search is not the channel for it.
2. **Use the data to title and format those pieces, not to choose them.** Where the owner's expertise overlaps practitioner demand, the data is gold. Template demand runs through product topics: user stories 41%, roadmaps 34%, PRDs 33%. A strong opinion plus a usable template ranks and also builds credibility. Definitional demand you can't win should come last, if at all.
3. **Don't lock in 13 categories and 210 notional articles.** Twelve months at three a week is about 150 pieces, and the plan splits the writing time across both domains and five sections. Thin categories signal a thin site, and as the brief itself says, live URLs are expensive to unwind. Launch with three or four categories the owner can fill with real experience, and let the rest follow what actually gets written.

The research method is sound and cheap. The mistake is letting it set the site's identity when it should only be a filter. Ask "what does this person know that the internet lacks?" first, and "what does it search for?" second.
