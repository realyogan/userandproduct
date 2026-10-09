# Council 2 responses, anonymised (A to E)


## Response A

Yes, and it is bigger than a Templates sub-feature. This could be the site's signature format, the thing it is known for.

**1. It wins the template page ones the research already found.** "prd template" is the one template query with a weak page one: 2,900 adjusted searches at KD 6. User story templates are 11,150 at KD 13. Notion, Atlassian and ClickUp hold those page ones with static documents. A page that gives the static template plus a skill that interviews you and writes the PRD is a different kind of answer, and no vendor's gallery offers it. Don't build skills as a separate product. Make every template page "template + skill + worked example". The search demand is for the documents, and the skill is how we beat everyone else's version of them.

**2. It carries the owner's method.** A skill file is 15 years of judgment written down: which questions a senior PM asks, in what order, and what a good answer looks like. That is the authority goal in a form people can run themselves. The owner's own BRD (brd-v1) is a ready-made worked example.

**3. Chain the skills.** Discovery plan, then persona, journey map, PRD, user stories, roadmap, with each skill reading the output of the one before. Nobody in the niche has a linked set, and the chain itself becomes the structure of a course later: each question in a skill is a lesson on why that question matters. The BRD already lists "premium professional templates" and "learning paths". This is the route from free to paid: a free set of single skills, then a paid set for teams.

**4. It brings backlinks to a new domain.** Publish the library as a public GitHub repo. The competitor stock already shows GitHub awesome lists with "Sample Product Documentation" (13 entries) and "Templates" (8) headings, and gist.github.com is on template page ones. A well-made skills repo gets listed, starred and forked, which gives a no-backlink domain its first real links. A coding-agent plugin listing would be a second channel.

**5. It makes the site easier for AI answers to cite.** Plain Markdown on a stable URL is exactly what assistants read and quote, and being cited by AI answers is already a stated goal.

**6. It gives the site a hub for its AI search terms.** "ai for product managers" (3,600, KD 9), "ai for product management" (3,600) and "ai tools for product management" (390, KD 7) need a hub page that isn't another listicle. "How I use AI to write product documents, with the skills" is that page.

**7. It fits LinkedIn.** A post saying "I answered 12 questions and got this PRD", with the output and the skill link, is easy to share. Version numbers and a changelog give people a reason to come back without an email gate.

Launch with three skills tied to the three strongest template pages (user story, PRD, persona), each tested properly, and grow from there.


## Response B

Yes, but as one skill attached to the PRD article, not as a library. A "full list of skill templates" is roughly 15 times 6 hours, which is 90 hours, or about 11 weeks of the two-pieces-a-week budget gone before a single copy click shows demand. The research shows 0 searches for "prd generator". It also shows 18,100 searches for "PRD template" at KD 9. So the skill goes on that page and gets no section of its own.

**How it gets built.** One `SKILL.md` with frontmatter (name, description) in the same format as llm-council. It has four blocks:
- 10 to 12 interview questions, asked one at a time, with a rule to push back on vague answers.
- The PRD structure the owner actually uses.
- A self-check before output: no metric means no PRD, and every requirement needs an acceptance line.
- An output rule: produce .docx if the assistant can make files, otherwise clean Markdown that pastes into Word or Google Docs. Never promise Word.

**How it gets tested.** One fixed test brief is run through three hosts:
- Claude Code: the file goes in `.claude/skills/prd/`.
- claude.ai: the text goes into a Project's instructions.
- ChatGPT: it is pasted as the first message.

Run 3 briefs (good, vague, contradictory) on 3 hosts. That is 9 runs at about 20 minutes each, so 3 hours.

**Owner hours.** About 1.5 hours writing the questions, 1 hour on the structure and checks, 3 hours testing, and 0.5 hours on page copy. That makes about 6 hours, which matches the verdict's 6 to 8 hours per piece. So a skill is not a free extra. It either counts as a weekly piece or it gets bundled. Bundle it: the PRD method in the article already is the skill's content, so converting it adds about 3 to 4 hours.

**Delivery on plain WordPress.**
- A core Code block with about 25 lines of vanilla JS for a copy button, and a "Copied" state.
- A download served as `prd-skill.txt`. WordPress blocks `.md` uploads, and a .txt file avoids an `upload_mimes` filter.
- A second, shorter block titled "No skills? Paste this", which is the plain prompt.
- Three "how to install" lines, one per host.
- A GA4 event on copy and download. No email gate.

**Monday morning.** The owner writes the 12 questions he actually asks a team before writing a PRD, in 45 minutes. On Tuesday a subagent turns them into `SKILL.md` and the plain prompt. Wednesday is the 9 test runs. It ships inside the PRD article in week 2 or 3, the piece the verdict already says to write first.

**Stop rule.** At week 6, if copy plus download events are under 50, or no peer mentions it on LinkedIn, there is no second skill. If the numbers clear that bar, the next two are user stories, then acceptance criteria, because those launch articles already exist. That caps it at 3 skills by month 3.

**Positioning.** Label it "the PRD interview I run, as an AI skill". Never call it "AI prompts". The owner's method is the product, and the assistant only delivers it.


## Response C

No, I wouldn't understand "AI skill" from a page that offered one. To me a "skill" is something a person has: "negotiation skills". "AI skill" sounds like a course on getting better at AI. "Skill file", "Markdown" and "coding agent" would lose most designers and half of PMs before the second sentence. The example skill file made it worse. It's 470 lines of instructions written for a machine, full of "sub-agents", "anonymize", "triggers" and a GitHub link. If I opened something like that I'd assume it was meant for engineers and close the tab.

What I would understand straight away is: "Paste this into ChatGPT. It will interview you for 10 minutes, then write your BRD." That's an outcome, a time cost and a tool I already have. Put that on the page and leave "skill" out of the headline. Call it "BRD interview", "PRD builder" or "guided template".

Would I put my name on a BRD it wrote? Not as it comes out, and not without seeing an example first. My worry is that AI documents read like AI. They're fluent and generic, and every section is confidently filled in, even the parts I never gave it. My director would spot it. What would get me to try it:

- **A real before and after.** Show the questions it asked, the answers someone gave, and the finished BRD, start to finish, on one page. That's the whole sale.
- **It must flag gaps rather than invent them.** If I didn't give success metrics, the document should say "[TBD: you didn't specify]", not make some up. Say that on the page in plain words. It's the trust line.
- **The author's method stated.** "This follows the BRD structure I used for 15 years at X" is why I'd pick this over a free listicle prompt.
- **Copy button, one block, works in ChatGPT.** No installing, no folders, no "if your assistant has a tool for files". If Word or PDF only works in some tools, I'll hit the case where it doesn't and blame the site.
- **The plain template sitting next to it.** Some days I just want the blank document.

What would put me off:

- "Prompt library" anywhere on the page.
- More than one setup path on the page.
- Model names I don't recognize.
- Any hint that I paste my company's confidential details into something without guidance. Say what to keep out.

Words that help: "interview", "answers", "draft", "you review it", "works in ChatGPT and Claude", "about 10 minutes".
Words that confuse: "skill", "Markdown", "agent", "Claude Code", "project instruction", ".md file", "install".

Bottom line: the idea makes sense to me once I see it work. The jargon is what would stop me trying it. Sell the interview and the finished document, and keep "skill" out of anything a reader sees.


## Response D

Wrong question. "Should we offer a library of AI skills?" treats the file format as the product. It isn't. Look at what a PM is actually stuck on when they search "prd template" (18,100 a month, 33% of PRD searches asking for a template or example). A blank page isn't the problem. They don't know which questions to answer, in what order, or what a good answer looks like. Whatever has value here is the owner's method: the questions, the order, the quality bar, the 15 years of knowing where PRDs go wrong. The Word doc, the Markdown template, the article and the skill file are just four ways of packaging that one method.

Start from that and the real competitor is obvious. It isn't Notion or the GitHub prompt repos. It's the assistant itself. Anyone can type "interview me and write a PRD" into ChatGPT, for free, in 10 seconds. A skill file without a real method in it is worth exactly that, and you'd be putting the owner's name on it. Search says the same: zero phrases for "prd generator" or "brd template with AI". People search for the document, not the machine that writes it.

So, rebuilt from the ground up:

1. **No "AI skills" section and no "full list".** The verdict allows about 12 pieces and two a week. A library of 10+ skills, each tested across 3 assistants and several output formats, adds a product line before the site has one live article.
2. **The skill is a by-product of the PRD article, not a separate project.** Writing the PRD piece forces the owner to set out their questions and quality bar. Turning those into a skill file costs about an hour. Put it on the same page as a third format beside the template and the example. That makes it cost almost nothing, and it ranks on demand that is already proven.
3. **Ship a reviewer, not just a generator.** Generating a PRD is a commodity. Judging one is scarce. A skill that says "paste your draft PRD and I'll check it against these 12 tests" puts the owner's expertise on display in a way an interview-and-fill prompt never can. Most PMs already have a draft anyway.
4. **Ship Markdown output only, and don't promise Word or PDF.** Converting files is the assistant's job. If the owner promises it, every model that does it differently becomes a trust problem with the owner's name on it.
5. **Name the method** (for example "the userandproduct PRD method"). A named method is what AI answers quote, and a citation is authority even without a click.

The test: the PRD page goes live with all three formats. At the week-6 checkpoint, compare skill copies against template downloads and LinkedIn reaction. Add a second skill only if the skill outperforms the template. If it doesn't, you've lost an hour, not a section.


## Response E

The fatal flaw is that this product competes with a blank chat box. Any PM can type "interview me, then write a BRD" into ChatGPT today and get about 80% of the result. The only thing that's really yours is the question set and the method behind it. A Markdown file is the most copyable asset that exists: the moment it's published, it's scraped into GitHub "awesome" repos and vendor blogs without your name on it. You'd be giving away the moat and calling it the product.

The demand is also missing. The harvest shows zero matches for "prd generator", "prompt for product managers" or "brd template with AI". The proven demand is "prd template" (18,100 a month), and those people want a document they can open, not an assignment to paste into an assistant. A skill page is a block of Markdown, which is thin content and won't rank. The first council already warned that template pages are hard to rank even when they're good.

Trust is backwards here. The verdict says the owner's 15 years are the identity. A library of AI skills says "a prompt can do my job," which is the opposite message. Then there's quality control, which you can't actually do. One skill times three assistants (Claude Code, claude.ai, ChatGPT), across consumer modes that may or may not export .docx, times a model update every few months, gives you output you can't predict under your name. The first broken Word export or invented "industry benchmark" in a BRD lands on you, not on OpenAI. And the council skill that impressed the owner ran inside Claude Code, a power-user tool. Most PMs live in ChatGPT's consumer app, where file output is inconsistent.

Capacity is the binding constraint, and the verdict already set the limit: 12 pieces in six weeks, two a week, 3 or 4 templates at launch. "A full list of skill templates" is the 81-article mistake again, the day after it was cut. Each skill needs a method, an interview script, an output spec, testing on several assistants and ongoing upkeep. That's a second product line before the first article is live.

It also doesn't show up in measurement. Copied text leaves no analytics, no return visit, no backlink and no newsletter signup. You can't tell whether it worked.

Recency bias is the question nobody is asking. This idea is 24 hours old and came from one impressive demo. What does it beat that's already on the list?

If anything survives, it's one skill, shipped as an appendix to the PRD article, next to the static template. It shouldn't be a library or a section. Test it on 5 working PMs at week 6, and build a second one only if they use it unprompted.
