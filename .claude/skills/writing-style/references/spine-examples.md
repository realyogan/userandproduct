# The spine, worked twice

Two outlines on the same six-part spine. The first is a judgment piece, the kind most of this site
is. The second is a procedure piece, used only because the reader performs the steps afterward.
Read the headings alone in each: they tell the argument. Where an outline says `[OWNER]`, the case
must come from the author.

---

## A judgment piece: "How long should a PRD be?"

Three to five takeaways, planned first:
1. Length follows how many decisions are still open, not the size of the feature.
2. One page is right for most work; long PRDs are written for approval, not for building.
3. Three signals tell you a PRD needs to be longer.
4. Cut the sections nobody reads: background, market sizing, the persona recap.

**Promise.** "Most PRDs should fit on one page. Here is how to tell when yours should not, and what
to cut either way."

**The problem (heading: Why PRDs keep getting longer).** Teams add a section each time something
goes wrong. Nobody removes one. The document grows for the approval meeting, and engineers stop
reading by page two. `[OWNER: the 14-page PRD and what happened to it]`

**What to skip.** "This is not about PRD templates for regulated industries. If an auditor reads
your PRD, the rules are different."

**The body (judgment).**
- *Length follows open decisions, not feature size.* Reasoning, plus one small and one large
  feature whose PRDs were the same length. Picture: open decisions against pages.
- *One page is the default, and why.* What fits on a page, what does not, what the reader does with
  it. Rule box: "If a section does not change a decision, it does not go in."
- *Three signals you need more than a page.* Several teams build parts of it; the edge cases are
  the product; a decision will be argued again in three months. One short case each.
- *What to cut.* The sections that inflate PRDs, and where that content lives instead.
- *Where I disagree with the usual advice.* The author's opinion with its reason, for example that
  the "goals and non-goals" pair is worth more than the full background section.

**The usable thing.** A one-page PRD outline with a line under each section on what belongs there,
plus the three-signal check as a small table.

**The way on.** "Next: How to write acceptance criteria engineers do not have to ask about. It
covers the part of the PRD that gets read most."

Note what is absent: no numbered steps. The reader leaves with a judgment and a template, not a
procedure.

---

## A procedure piece: "How to run a usability test with five people"

Three to five takeaways, planned first:
1. Five people find most of the problems that block most users.
2. The script is three tasks, written as goals, not instructions.
3. Your job in the room is to stay quiet.
4. Write the findings the same day, as a short ranked list.

**Promise.** "Five people, three tasks, one afternoon. By tonight you will know the problems that
stop most of your users."

**The problem (heading: Why teams skip testing).** Teams wait for a research budget, a lab or 20
recruits. So the test never happens, and the first real test is launch day.
`[OWNER: a launch that a one-afternoon test would have saved]`

**What to skip.** "You do not need a lab, eye tracking or a recruiting agency. A video call and a
calendar link will do."

**The body (procedure).**
1. *Recruit five people who match your users.* Where to find them, what to pay. Check it worked:
   five confirmed slots, 45 minutes each, with 15-minute gaps.
2. *Write three tasks as goals.* Shown: a bad task ("Click Export") and a good one ("Send last
   month's report to your manager"). One line on what to change for your product.
3. *Run each session and stay quiet.* The four sentences you are allowed to say, shown in a box.
4. *Note every place someone stops, guesses or gives up.* Shown: a notes grid, one row per task.
5. *Rank the findings the same day.* Shown: a ranked list of five findings with a count each
   ("4 of 5 missed the Export menu").

**Stop line and reflection.** "That is it. Five sessions, one list." Then *What just happened*:
why five is enough, why goals beat instructions, and when to test again.

**The usable thing.** The session script, the notes grid and the findings template, ready to copy.

**The way on.** "Next: How to turn five findings into a fix list your team will actually ship."

Note why this one gets steps: the reader closes the page and does each of them, in order.

---

## A series explainer: "Technical things for non-technical people, No. N: What a feature flag is"

The series format. One concept, one analogy, one picture per idea, one real-life mapping per
picture. 500 to 800 words. Every number in the series follows this shape, so a reader who has read
one knows how to read the next. The body is the analogy and the mapping (see SKILL.md).

Three takeaways, planned first:
1. A feature flag lets the team put finished code live while keeping it switched off.
2. The switch can be on for some people and off for others, or on for a growing share.
3. If something breaks, one switch turns it off in seconds, with no new release.

**Title and number.** "Technical things for non-technical people, No. 7: What a feature flag is."
The number shows it is a series; the rest is the search phrase.

**Promise.** "Your engineers say the feature is 'shipped but behind a flag'. Here is what that
means, in four pictures and about five minutes."

**The problem (one short paragraph).** Product people hear "it's live" and "customers cannot see
it" in the same meeting and nod. The gap between those two is the whole concept.
`[OWNER: the launch where this confusion cost a week]`

**The analogy, introduced once.** "Think of a theater. The lights are already hanging above the
stage. A lighting board at the back decides which ones come on."

**Section 1: The lights are already up.** Picture: a stage with unlit lamps.
In real life: the lamps are the new code; hanging them is the deploy (putting code on the live
servers). Rule: "Deployed is not the same as switched on."

**Section 2: The lighting board.** Picture: a board with labeled switches.
In real life: the board is the flag dashboard (a settings screen, often a service such as a flag
tool or a simple config file); each switch is one flag, named after the feature.
Rule: "Every unfinished feature gets its own switch."

**Section 3: Some seats, then more seats.** Picture: a spotlight on the front rows, then half the
house. In real life: on for staff first, then 5% of customers, then 50%, then everyone. That
growing share is a percentage rollout. Rule: "Turn it up slowly and watch the numbers."

**Section 4: The house-lights switch.** Picture: one big switch by the door.
In real life: the kill switch. If error rates jump, someone flips the flag off and every customer
is back on the old version in seconds, with no new release. Rule: "Off is always one click away."

**The usable thing.** Five questions to ask your engineers about any flagged feature (who has it
on now, what share, what number makes you turn it off, who can flip it, when the flag gets
removed), plus a four-line glossary: deploy, release, flag, rollout.

**The way on.** "No. 8: What an A/B test is. It uses the same switch, with a stopwatch."

Note the limits that keep the series consistent: one concept per number (A/B testing gets its own
number, even though it uses flags); no section without a picture, an In real life line and a Rule;
the analogy never changes halfway; the technical names appear in every In real life line, so the
engineer reading over the shoulder finds nothing wrong.
