# Eval notes, iteration 1 (2026-10-09)

Each prompt in `evals.json` was run once by a separate agent that read SKILL.md and its references
fresh and saved the result to `outputs/`. No baseline run was made. Verdicts are by reading against
the skill's checklist and banned list.

| # | Eval | Output | Verdict |
|---|---|---|---|
| 1 | Intro for "How to run a usability test with five people" | `outputs/eval-1-intro-usability-test.md` | Pass. The promise answers the title in two lines, the problem is a short story, there is a skip section, no banned phrases or em dashes, and an [OWNER] gap instead of an invented launch. Watch: it follows the worked outline in `spine-examples.md` almost line for line, so outlines in the references get copied when the topic matches. |
| 2 | Rewrite of the machine-written personas paragraph | `outputs/eval-2-rewrite-personas.md` | Pass. Every banned phrase and the triad are gone, "persona" gets a plain meaning, the vague benefits become one concrete use, and an [OWNER] gap replaces an invented case. |
| 3 | Outline "When a roadmap is the wrong tool" | `outputs/eval-3-outline-roadmap.md` | Pass. It is a judgment body with no numbered steps, the headings make the argument alone, there are three [OWNER] markers and a Rule box and picture where they do work, and it ends on a decision table. Minor: one of the four signals in the table has no section of its own. |

## What to watch next round

- Copying from references: if the owner wants varied openings, swap the usability-test outline in
  `spine-examples.md` for a topic the site will not publish, or add a note that the outlines show
  shape, not wording.
- Add a baseline (no skill) run and a series-explainer prompt ("Technical things for non-technical
  people: what an API is") to test the analogy-and-mapping device.
