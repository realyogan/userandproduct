---
name: writing-style
description: House writing rules for every piece of text on userandproduct.com (articles, explainer pages, category intros, template pages, newsletter notes, About and Start-here pages) and the plain-language research explainers in research/explainers/. Use this skill whenever site copy is drafted, outlined, edited, rewritten, shortened, simplified or reviewed, even for a single paragraph, a heading list or a caption, and whenever the owner says "write the article", "draft", "outline", "edit this", "rewrite", "make it simpler", "tighten this", "does this read like AI", "tone", "voice" or "writing style". Covers the teacher's voice, the spine of a piece, writing for readers who scan, sentence rules, the banned machine-writing phrases and the pre-flight checklist.
---

# Writing style for userandproduct.com

The voice is an experienced teacher explaining calmly, from fifteen years of doing the work. Simple
enough that a bright 10-year-old can follow it, even when the matter is hard; for an experienced
reader it is a breeze. Simple never means shallow: keep the depth, lose the jargon.

This is a guide with guardrails, not a template. The spine below stays; what goes in the middle
depends on the piece. Most pieces on this site are judgment pieces, not tutorials.

## Who we write for: two readers in one

Every piece serves two people at once, and both must leave with the point.

- **The reader** goes top to bottom. They need the reasoning, the examples and the story.
- **The scanner** reads the headings, the pictures, the rule boxes and the first line of each
  section, then decides whether to stay. They should get the whole argument from those alone.

The audience is working product managers, designers and founders in the US first, then the UK and
Canada. Many are experienced. None of them wants to be talked down to, and none wants padding.

**The goal: static, but it feels interactive.** A reader shown our explainers said "this is
interactive, I can learn things like this". Nothing on the page moved. The feeling came from the
reader doing something at every step: looking at the picture first, checking an "In real life"
line against what they already know, stopping on a Rule box, trying the thing at the end. Those
are the devices; use them on purpose. The test: **does the reader do something on every screen,
or only read?**

## Why the author matters more than the format

A tidy, correct explainer from this author reads like one from anybody, and anybody includes the
search results and the AI answer above them. What nobody else has is the author's first-hand
material: the PRD that failed, the review that went wrong, the number from a real project, the call
he would make again and the one he would not. Every piece needs at least one of those, placed where
it does work, not as decoration. If the writer has none for a topic, ask the owner for one before
drafting, or leave a marked gap: `[OWNER: a real case where ...]`. Never invent an anecdote, a
client or a number.

## The voice: ten rules

1. **Promise first.** The first two or three lines say what the reader gets and, where it fits, how
   long it takes. The first paragraph answers the title's question.
   "A PRD engineers read to the end. One page, five sections, about an hour to write."
2. **Why before how.** Tell the problem as a short story: what people do today, where it breaks,
   one line that names the fix.
   "Most teams write the PRD for the approval meeting. Then nobody opens it again."
3. **Permission to skip.** Say what this piece leaves out and that the reader does not need it yet.
   "You do not need a research team for this. Five people and a quiet room will do."
4. **Show, then interpret.** Put the thing on the page (the template, the table, the real sentence,
   the picture), then one line on what to notice. Never describe what the reader can look at.
   "Look at the third row. That is the decision nobody wrote down."
5. **A plain word beside every term.** The first time a term appears, its plain meaning sits in the
   same sentence or the next.
   "Track retention (the share of people who come back) by week, not by month."
6. **Short declaratives.** State it. Hedge only where the evidence is honestly mixed, and say why.
   "The roadmap is a promise. The backlog is a list. Keep them apart."
7. **The teacher's calm.** Confident without selling. Admit the messy parts plainly. No hype, no
   alarm, no cheerleading.
   "It is less elegant than a tool. It works fine."
8. **Experience as specifics.** A real case, a real number, a named failure, never "in my
   experience, many teams".
   "On one checkout project we tested with five people and lost two days to a broken prototype."
9. **First person, opinions as opinions.** Say "I" when it is the author's view, and give the reason
   in the same breath.
   "I would not run OKRs in a team of four. The ritual costs more than the focus it buys."
10. **US English, second person, present tense.** Color, prioritize, program. "You" is the reader.
   "You write the goal first. Everything else hangs off it."

### The named device: the analogy and the mapping

This is the bar: even someone with no technical knowledge can follow it and connect it to the real
thing. The exemplar is the origin-lock explainer
(`C:\xampp\htdocs\Printables\research\discussion\origin-lock-explained.html`); read it once if you
have not. Its method, in five parts:

1. **One everyday analogy carries the whole piece.** The website is a concert venue. Cloudflare is
   the front gate with ticket checkers. The checkers press an invisible-ink stamp on every hand.
   The back door gets a guard who opens only for the stamp. One world, kept to the last line.
2. **Every part of the analogy maps to exactly one real thing,** stated in an **In real life** list
   or line right after each picture, with the real names and numbers. "The stamp is a hidden line,
   X-RPP-Edge, on every request. The guard's no is a 403 Forbidden. The old street sign is a 301
   redirect."
3. **The technical reader loses nothing,** because the mapping is exact. They read the real-life
   lines and skip the story; the beginner reads the story and grows into the real-life lines.
4. **One picture per idea. The words are labels.** "Look at the drawings first; the words are just
   labels."
5. **A one-line Rule box per section,** the thing to remember if nothing else sticks.

An analogy that maps loosely is worse than none: it teaches the wrong thing. If a part of the real
system has no counterpart in the analogy, add one (the mail carrier for certificate renewal, the
janitor for scheduled jobs) or change the analogy.

## The spine of a piece

Six parts, in this order. Each is a job, not a heading; name the headings for what they say.

1. **Promise.** Two or three lines. Always.
2. **The problem.** A short story of how it goes wrong today. Always, even in a procedure piece.
3. **What to skip.** One to three lines on scope. Use it when readers are likely to over-reach or
   feel they need more than they do. Leave it out when nothing needs excluding.
4. **The body.** A judgment body or a procedure body (see below).
5. **The usable thing.** Every piece ends with something to use: a template, a checklist, a
   question list, a decision table, a download. Shown on the page, not only linked.
6. **The way on.** One to three links that name the next piece and say what it holds. No restating
   summary before it. A one-line stop ("That is it. One page.") is fine after a procedure.

### Choosing the body

First: **is the piece explaining a technical or abstract concept** (how a system works, what a
metric means, how a method fits together)? Then the default is an **explainer body**: the analogy
and the mapping. Numbered sections, one idea each; per section one picture, the story in the
analogy, an In real life line or list, a Rule box; a short glossary at the end. This is also the
body of the planned series "technical things for non-technical people".

Otherwise ask: **does the reader perform a sequence of actions right after reading?**

- **Yes: procedure body.** Numbered steps, one action each, the thing itself shown (the file, the
  script, the screen), one line under it on what to change, and a "check it worked" line where
  checking is possible. Then a short "what just happened" reflection.
- **No: judgment body.** Most pieces on this site. How to decide, what fails, what to leave out,
  when a tool is wrong. The middle is reasoning and examples: the options, the signals that point to
  each, cases from real projects, the trade-offs, where the author disagrees with common advice and
  why. Sections are claims or the reader's real questions, not steps.

Do not turn a judgment piece into steps. "7 steps to a better roadmap" for a piece about when a
roadmap is wrong is the most common way a good argument turns generic. A judgment piece may hold a
short procedure (how to run the one meeting it recommends), but that section serves the argument;
it does not become the piece.

Worked outlines of both kinds are in `references/spine-examples.md`.

## Writing for the scanner

- **Plan before you write.** List the three to five things the reader must leave with. Give each a
  heading that states it and, where it helps, a picture. Then fill in the words. If the list runs
  past five, the piece is two pieces.
- **Headings tell the story alone.** Read only the headings in order: they should make the argument.
  Use the words people search for where they fit. "Why PRDs go unread", not "Background".
- **One idea per section.** The first sentence of each section carries that idea.
- **A picture where a picture does the work.** A flow, a comparison, a before and after, a
  structure, a timeline. Not a stock photo, not a picture of the heading. The point goes in the
  caption; the alt text says what the picture shows. Follow `research/mockups/illustration-rules.md`
  for palette, size and file names.
- **Landing spots.** Give the scanner places to stop: a one-line **Rule** box with the takeaway, an
  **In real life** list that maps an analogy to the real thing, a short table, a pulled example.
  About one landing spot per screen of text.
- **Density per screen, not length per piece.** A long piece is fine if every screen has a heading,
  a landing spot or a picture in view. A short wall of text fails.
- **One analogy can carry a whole explainer** (a library, a venue with a front gate, a layer cake).
  Pick one, keep it the whole way, and map it back with an "In real life" list (see the analogy
  and the mapping, above).

## Sentence rules

- Most sentences under 15 words; many under 10. Fragments are fine when they land a point. "Five
  people. One afternoon." Vary the length so it does not tick like a metronome.
- One idea per sentence. One point per paragraph. Paragraphs of one to three sentences.
- Present tense, second person. "You" is the reader; "I" is the author; "we" only for reader and
  author together, never for a faceless company.
- Numbers and nouns over adjectives. "Three of five people missed the button," not "many users
  struggled significantly".
- Concrete over abstract: a file name, a button label, a meeting, a time, a count.
- No exclamation marks. Almost no rhetorical questions; a question heading is fine when it is the
  reader's real question.
- Bold only for labels (a term being defined, a file, a step name, "Rule"). Never for emphasis
  inside a sentence.
- Lists only for parallel items: actions, parts, options, criteria. Reasoning goes in sentences.
- Digits for 10 and up, and for all measurements, money and percentages.
- Spell out an acronym the first time: "objectives and key results (OKRs)".

## The banned list

These mark text as machine-written or as filler. Rewrite the sentence; do not swap in a synonym.
The full list with plain replacements is in `references/banned.md`. The core:

**Openers and closers:** "In today's fast-paced world", "In the ever-evolving landscape of", "In
the realm of", "Let's dive in", "Let's dive deep", "Let's explore", "Buckle up", "Picture this",
"Imagine a world where", "Have you ever wondered", "In conclusion", "To sum up", "In summary", "At
the end of the day", "Ultimately," (as an opener), "Happy designing!", "I hope this helps".

**Throat-clearing:** "It's important to note that", "It's worth noting", "It's worth mentioning",
"Needless to say", "It goes without saying", "When it comes to", "In order to", "The fact of the
matter is", "Simply put", "That being said", "With that in mind".

**Audience framing:** "Whether you're a seasoned PM or just starting out", "Whether you're a ... or
a ...", "As a product manager, you know", "We've all been there".

**Hype and filler words:** game-changer, game-changing, revolutionary, cutting-edge, seamless,
seamlessly, robust, powerful, leverage (as a verb), unlock, unleash, supercharge, elevate, empower,
harness, transformative, holistic, synergy, best-in-class, world-class, next-level, effortless,
delve, tapestry, navigate (anything but a map), journey (anything but travel), landscape, realm,
paradigm, ecosystem (for a product), crucial, vital, pivotal, essential and key (as filler
adjectives), myriad, plethora, "a testament to".

**Hedges and padding:** "can help you", "may potentially", "arguably", very, really, truly,
incredibly, extremely, basically, actually, "in many ways", various, "a wide range of", "a variety
of".

**Structural tells:**
- A warm-up paragraph that defines the topic before saying anything ("Product management is a
  multifaceted discipline...").
- A closing summary that restates the piece. End on the usable thing and the way on.
- Seven (or ten) generic tips that would fit any company.
- Triads by reflex: three adjectives or three parallel clauses because three sounds finished.
- Mirrored pairs: "It's not about X, it's about Y." "Less X, more Y." "X isn't Y. It's Z."
- Dash chains: more than one em dash in a paragraph. Use a period, a colon or parentheses.
- Every section the same length and shape (claim, three bullets, wrap-up line).
- Bold sprinkled through sentences; emoji in headings; every heading a question.
- Colon titles with a gerund: "Mastering Roadmaps: A Comprehensive Guide".
- Fake balance: "There are pros and cons to both" with no call made.
- A rhetorical question answered by itself: "The result? Chaos."
- "Here's the thing", "Here's why", "The kicker", "Spoiler alert".

## Pre-flight checklist

Run this before a piece ships. Every answer should be yes.

1. Does the first paragraph answer the title's question, with no warm-up?
2. Do the headings, read alone, tell the whole argument?
3. Is there at least one first-hand specific (a case, a number, a failure) the author actually has?
4. Is every opinion marked as the author's, with its reason?
5. Is the body the right kind: steps only if the reader performs steps?
6. Does each section hold one idea, stated in its first sentence?
7. Does the reader do something on every screen (look, check, stop, try), not only read?
8. Does every technical term get its plain meaning the first time?
9. Is every picture doing work, with a caption that states its point and full alt text?
10. Is the banned list clear, structural tells included?
11. Does the piece end on something usable and a named way on, with no restating summary?
12. Is it US English throughout (color, prioritize, center, -ize spellings)?

### The simplicity test

- Read the first paragraph aloud. Where you run out of breath or stumble, cut.
- Could a bright 10-year-old follow it? Not do the job, but follow what is said and why.
- Is the hard part still there? If the simple version dropped the trade-off, the exception or the
  number that makes it true, put it back in plain words. Simple, not shallow.

## How to use this skill

- **Drafting:** plan the three to five takeaways, choose the body type, write the spine headings,
  then fill. Ask the owner for first-hand material where it is missing, or mark the gap.
- **Editing someone's text:** keep the author's facts and stories; change the shape and sentences.
  Flag (do not invent) where a specific is needed.
- **Reviewing ("does this read like AI?"):** go through the banned list and the checklist; quote
  each problem line and give its rewrite.
- **Research explainers in research/explainers/:** same voice, written for the owner; one idea and
  one picture per section, an analogy where it helps, Rule boxes, a short glossary at the end.

## References

- `references/examples.md`: five before-and-after rewrites in the site's field (PRDs, usability
  testing, OKRs, retention, hiring). Read when rewriting or unsure how the voice sounds.
- `references/spine-examples.md`: a judgment piece, a procedure piece and a numbered series
  explainer ("technical things for non-technical people"). Read when outlining or choosing the
  body type.
- `references/banned.md`: the full banned list with plain replacements. Read when reviewing.
- `references/analysis.md`: the approved analysis of the reference pieces this skill comes from.
- `research/mockups/illustration-rules.md`: the rules for every picture.
