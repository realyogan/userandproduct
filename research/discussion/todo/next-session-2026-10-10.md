# Next session — User and the Product

Session closed 9 Oct 2026, late evening. The owner said: "tomorrow we'll review this and move forward."
Start by opening proposal 3 together and going through its fourteen questions, then the council verdict.

Read `research/discussion/context.md` (9 Oct entries, especially the last three: thumbnail skill finished,
council on the publishing system, proposal 3) before anything else.

## First thing: commit

Nothing from the afternoon and evening is committed. The owner said "say which styles stay in the rotation,
and I'll commit it all" and never said "go" after that. Ask for the go, then `git add -A` and push to
`github-realyogan:realyogan/userandproduct` (no attribution lines). Waiting:
- `.claude/skills/thumbnail-images/` (skill, references, evals), `research/mockups/tools/thumbnail.py`,
  `research/mockups/references/blog-thumbnails/` (gallery.html, gallery/, build_gallery.py, README, board),
  `research/mockups/vendor/` (icon sets)
- `research/explainers/publishing-system-proposal-{,2-,3-}2026-10-09.html` and the explainers README
- `research/discussion/council/publishing-system-2026-10-09/` (question, responses, reviews, verdict)
- `research/discussion/context.md`, this file, `research/progress/status.json`

## Where things stand

**Thumbnails (done, owner confirmed the decisions are in the skill).** Eleven styles, full lockup on every
image (hero 220 px, thumb 120 px, a fifth of the width), free high-contrast colours with twelve suggested pairs,
mono by default, duo and trio with restraint, the particle stream and the glow bloom carry the accent, duo on
mid-bright grounds, fit first then rotation, photo style only with the owner's photo.
Gallery: http://localhost/user-and-product/research/mockups/references/blog-thumbnails/gallery.html

**Publishing system (in discussion).** Three proposal pages, all kept:
- http://localhost/user-and-product/research/explainers/publishing-system-proposal-2026-10-09.html (v1)
- http://localhost/user-and-product/research/explainers/publishing-system-proposal-2-2026-10-09.html (v2, adds
  the Performance desk: campaign manager watches, scores, nudges, schedules refreshes, never edits)
- http://localhost/user-and-product/research/explainers/publishing-system-proposal-3-2026-10-09.html (v3, the
  current one: v2 plus the owner's rhythm. Sunday pitch meeting via a placeholder "/whatsup" command: status,
  then about ten pitch cards with title, learning sentence, TL;DR outline, images planned, evidence,
  expectation, a story slot the owner answers on the spot; monthly build window of two or three days producing
  everything into article folders and local WordPress as scheduled drafts; review week in local WordPress at 30
  to 40 minutes per draft; then scheduled publishing at two a week with the verifier checking each page; the
  first window three or four pieces to measure. Every agent and desk from v2 kept: twelve agents, five desks.)

Three choices in v3 the owner should confirm or overrule: the main session answers the pitch command (not the
editor agent); the explorer drafts outlines and planned images for the top ideas before the meeting (the only
added duty); the pitch meeting runs monthly on the Sunday before a window, other Sundays give status only.

**Council verdict on v2** (`research/discussion/council/publishing-system-2026-10-09/verdict.md`), parked by
the owner until v3 is finalised, then the council runs again on v3. Its main points, for when they come back:
owner's experience is the scarce input and gets ten minutes per article; two a week, not six; build order
upside down (ideas are not the bottleneck); the gate grades itself; 90-day rank expectation is fantasy on a
domain with no links; invented first-person detail cannot be caught by a source check; confidentiality of
stories; stories run out; no newsletter; no real readers; one session routing 40 hand-offs overflows; measure
authority signals; prove the belt on one owner-written baseline plus three plain-prompt pieces before any
agent file. The owner's pitch-meeting rhythm already answers part of this (outline checkpoint, story given at
pitch time, window of eight to ten feeding two a week).

## Tomorrow's agenda

1. Commit (ask for go).
2. Walk proposal 3's fourteen questions with the owner (the page saves answers in the browser; read them back
   from the owner, they are not on disk). Confirm the three v3 choices above.
3. Fold the answers into the page (proposal 3 updated in place, or a proposal 4 if the owner prefers new files,
   which has been the pattern today).
4. Run the council on the finalised proposal (new folder under `research/discussion/council/`).
5. Then build order, per the proposal: editorial folder and backlog seeded from the tree, the pitch command,
   the build-window runner, illustration skill, article-SEO rulebook, the first small window.

## Still open from earlier sessions

- Article A "settled" → Impeccable/Taste polish pass (IMPECCABLE_NO_TELEMETRY=1); home page and series page
  mockups; PRD interview skill (parked); skill library (back burner); illustration rules → skill (owner nod);
  fit ratings for categories; project management / web design / analytics yes or no; launch size; WordPress
  install.
