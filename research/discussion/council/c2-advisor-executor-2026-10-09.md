# The Executor (council 2: AI skills)

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
