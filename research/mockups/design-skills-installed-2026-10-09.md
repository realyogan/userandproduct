# Design skills installed (2026-10-09)

Two third-party design skills, installed by hand (copied, nothing run) into the git-ignored `.claude/` folder for the
second pass on the article-page mockups. Both sit beside the existing `frontend-design` skill, which lives at the user
level (`~/.claude/skills/frontend-design/`), not in this project.

| Skill | Source | Licence | Version | Installed to |
|---|---|---|---|---|
| Impeccable | https://github.com/pbakaus/impeccable (site impeccable.style) | Apache 2.0 | skill 4.5.2, engine 0.1.14 | `.claude/skills/impeccable/` + `.claude/agents/impeccable-*.md` |
| Taste Skill | https://github.com/Leonxlnx/taste-skill (site tasteskill.dev) | MIT | v2 (experimental) | `.claude/skills/design-taste-frontend/`, `minimalist-ui/`, `redesign-existing-projects/` |

Each SKILL.md ends with a `Source: ... (installed 2026-10-09, <licence>)` line, and each folder carries the upstream
LICENSE (Impeccable also its NOTICE.md). The cloned repositories stay in the session scratchpad only.

## How they were installed

**Impeccable.** The official route is `npx impeccable install`. Reading its source (`crates/skills/src/providers.rs`,
`bundle.rs`) and the repository's own `.claude/` folder (the built Claude Code layout) shows that for a project install
it writes three things:

1. `.claude/skills/impeccable/` (SKILL.md, 46 command and reference files under `reference/`, and `scripts/`): copied.
2. `.claude/agents/impeccable-*.md` (four helper agents: asset producer, documenter, finish reviewer, manual-edit
   applier): copied. The skill has fallbacks in `reference/degraded/` if these are absent.
3. A design-detector hook in `.claude/settings.local.json` (SessionStart, after every Edit/Write, and on Stop): **not
   installed**, on purpose. Settings were left untouched. It can be added later with `/impeccable hooks on` if wanted.

No slash-command files: everything runs through the one `/impeccable` skill.

**Taste Skill.** The official route is `npx skills add https://github.com/Leonxlnx/taste-skill`, which simply copies
each `skills/<folder>/SKILL.md` into a folder named after the skill's `name:`. The repository has 13 skills; three were
installed (the main one plus the two that fit an editorial site). The other ten (v1, the stricter variant, soft,
brutalist, output enforcement, Stitch, image-to-code and three image-generation-only skills) are left out to keep the
skills list clean; they can be copied the same way later.

All four SKILL.md files have valid frontmatter (`name`, `description`) and will appear in the skills list in the next
session.

## What each adds beyond frontend-design

`frontend-design` is a single page of principles: ground the design in the subject, pick type deliberately, a list of
five AI-default "looks" to avoid, a plan-review-build-critique loop, and good guidance on UI copy. It has no commands,
no checklist and no tooling.

**Impeccable adds:**

- **A command vocabulary.** Named, repeatable passes (`audit`, `polish`, `critique`, `quieter`...) each with its own
  playbook, scoring and report format, so a review is the same shape every time.
- **Scored reviews.** `audit` scores five areas 0 to 4 (accessibility, performance, theming, responsive,
  implementation integrity) for a /20 total with P0 to P3 issues; `critique` does a heuristic UX review and stores the
  result so a later `polish` can work through its backlog.
- **Surface modes.** It classes each page as Persuade, Operate, Read or Experience. The article page is **Read**:
  "the world owns the frame and serves the column", a calm reading column of 60 to 75 characters at about 16px, with
  the brand living in the masthead, rails, headings and how code and tables are set. That matches our brief closely.
- **A craft floor.** A short, concrete checklist loaded before any edit: contrast, spacing, type measure, one authored
  motion moment, all states, and themed browser surfaces (selection, caret, focus rings, underline offset, tabular
  numerals), plus a refuse list (eyebrows banned outright, section numbers, gradient text, thick colored side borders,
  hard offset shadows, emoji as icons).
- **Project memory.** `init` writes `PRODUCT.md`; `document` writes `DESIGN.md` from the code; working files go in
  `.impeccable/`.
- **A deterministic detector** (59 rules) for anti-patterns and quality issues, run by the engine binary (see run-time
  behavior below).

**Taste Skill adds:**

- **A "design read" first.** One line stating page kind, audience, vibe and foundation before any code.
- **Three dials** that gate layout, motion and density decisions (below).
- **A long pre-flight checklist** (about 60 boxes) with hard, countable rules: at most one eyebrow per three sections,
  no em-dashes or en-dash separators anywhere visible, one accent color locked across the page, one corner-radius
  system, no duplicate CTA intent, quotes at most three lines, hero fits the first viewport, theme never flips
  mid-page, reduced motion honored.
- **Named AI tells** in more detail than frontend-design: fake-precise numbers, "Jane Doe" names, poetic section labels,
  middle-dot overuse, decorative status dots, scroll cues, version stamps.
- **A redesign protocol** (`redesign-existing-projects`, and section 11 of the main skill): audit first, preserve IA,
  slugs, nav labels and SEO.
- `minimalist-ui`: a fixed editorial recipe (warm monochrome, 1px #EAEAEA borders, pastel tags, generous whitespace).

## Commands and how to invoke them

**Impeccable** (always through the one skill: `/impeccable <command> <target>`; `/impeccable` alone shows a menu):

| Group | Commands |
|---|---|
| Build | `shape`, `init` (alias `teach`), `document`, `extract`, `craft` (deprecated alias) |
| Evaluate | `critique`, `audit` |
| Refine | `polish`, `bolder`, `quieter`, `distill`, `harden`, `onboard` |
| Enhance | `animate`, `colorize`, `typeset`, `layout`, `delight`, `overdrive` |
| Fix | `clarify`, `adapt`, `optimize` |
| Iterate | `live`, `generate` |
| Housekeeping | `pin <command>` (makes `/audit` etc. as a shortcut), `hooks <on/off/status...>`, `doctor` |

Example: `/impeccable audit research/mockups/article/variant-b.html`, then
`/impeccable polish research/mockups/article/variant-b.html`.

**Taste Skill** has no commands. Invoke by name (`/design-taste-frontend`, `/minimalist-ui`,
`/redesign-existing-projects`) or let them trigger from their descriptions, and set the dials in the request, for
example "use design-taste-frontend with DESIGN_VARIANCE 3, MOTION_INTENSITY 2, VISUAL_DENSITY 5".

## Settings

**Taste dials** (1 to 10, default 8 / 6 / 4; the skill says to override in conversation, not by editing the file):

- `DESIGN_VARIANCE`: 1 perfect symmetry, 10 artsy chaos. 1-3 symmetric grid; 4-7 offset overlaps; 8-10 asymmetric.
- `MOTION_INTENSITY`: 1 static (hover only), 4-7 CSS transitions and load-in cascades, 8-10 scroll choreography.
- `VISUAL_DENSITY`: 1-3 gallery (huge gaps), 4-7 standard app spacing, 8-10 cockpit.
- Its own presets: Editorial / Blog 6 / 4 / 3; public-sector or trust-first 3 / 2 / 5.

**Impeccable settings** live in `.impeccable/config.json` (created by `init`): `buildPath` (`comp` or `code`), hook
lifecycle and detector ignores. Telemetry can be switched off with the environment variable
`IMPECCABLE_NO_TELEMETRY=1` (or `DO_NOT_TRACK=1`).

## Run-time behavior to know about

**Taste Skill:** plain Markdown, no scripts, nothing runs. Its guidance does point at network resources when it is
followed: placeholder photos from `picsum.photos`, logos from `cdn.simpleicons.org`, and npm packages. Its default
stack is React/Next + Tailwind v4 + Motion + GSAP and an icon library, and it bans hand-drawn SVG icons. That clashes
with our rules (no build step, no frameworks, plain CSS, small vanilla JS), so the stack sections must be overridden in
the request; the design rules themselves are stack-neutral.

**Impeccable:** the skill text is Markdown, but its Setup step runs `scripts/impeccable context` (or
`impeccable.cmd` on Windows) once per session, and several commands call the same launcher (`detect`,
`critique-storage`, `pin`, `live`). The launcher is a readable shell script, but it runs a compiled engine binary that
is **not in the repository**: on first use it downloads it from the project's GitHub releases into
`~/.impeccable/bin/0.1.14/` (outside this project), checks it against a published SHA-256 file and refuses on a
mismatch. After that it runs offline for most verbs. Known network calls from the engine source:

- the one-time engine download (GitHub releases);
- `concept-seed` (used in new-work direction rounds) fetches design "worlds" from `impeccable.style/api` and, after a
  choice, posts a small telemetry ping (chosen concept id, mode, kind) to `impeccable.style/api/chosen`, unless
  `IMPECCABLE_NO_TELEMETRY` or `DO_NOT_TRACK` is set;
- `generate-image` calls the OpenAI images API only if `OPENAI_API_KEY` is set;
- an update check reports `UPDATE_AVAILABLE`;
- `live` mode runs a localhost helper server and can run a project `package.json` script when applying copy edits
  (we have no package.json, so nothing).

The launcher calls go through the normal permission prompt, so each can be refused. If it is refused or fails, the
skill says to announce that and carry on reading `PRODUCT.md` / `DESIGN.md` directly: `audit`, `polish`, `critique`,
`quieter`, `typeset` and `layout` all work as written guidance without the binary; only the deterministic detector and
the stored-critique backlog are lost. Impeccable also writes `PRODUCT.md`, `DESIGN.md` and a `.impeccable/` folder in
the project root when `init` or `document` runs; decide where those belong before running them (the repo `.gitignore`
does not yet cover `.impeccable/`).

Nothing in either repository sends project data anywhere beyond the items above, and nothing modifies files outside
the project except the Impeccable engine cache in the home folder.

## Recommendation for the article-page mockup

1. **Pick the variant first** (A sidebar, B magazine, C reader), then run the skills on that one file rather than on
   all three.
2. **Impeccable, Read mode, refine not redesign.** Run `/impeccable critique` then `/impeccable audit` on the chosen
   variant, then `/impeccable polish` to fix the findings, with `typeset` (measure, scale, the serif/sans pairing) and
   `layout` (rhythm, ad slots versus the column) as needed. Tell it "Read surface, refinement, keep the brand" so it
   preserves the logo, signal blue and the ad rules. Skip `init`, `live`, `generate`, `overdrive`, `delight` and
   `bolder` for now. To avoid the binary download, decline the launcher prompt; the playbooks still apply. If the
   owner wants the detector, allow the one download and set `IMPECCABLE_NO_TELEMETRY=1`.
3. **Taste as a checklist, not a builder.** Use `design-taste-frontend` with **DESIGN_VARIANCE 3, MOTION_INTENSITY 2,
   VISUAL_DENSITY 5** (between its editorial and trust-first presets: a predictable grid, hover-only motion, a
   reading page with sidebar and ad slots), state "plain HTML and CSS, no frameworks, no npm, no picsum", and run its
   pre-flight list against the variant: em-dash count, eyebrow count, one accent, one radius system, quote length,
   theme lock, reduced motion. `minimalist-ui` is optional for variant C only; `redesign-existing-projects` is for the
   WordPress build later, not the mockups.
4. **Known conflicts to override, not follow.** Taste bans Fraunces as a default display serif and discourages
   Inter; `minimalist-ui` bans Inter outright and wants Phosphor icons. Our brand already fixed Inter Display for the
   wordmark, and Fraunces is in the mockup fonts. Both skills say an explicit brand choice wins, so state the fonts as
   the brand in the request. Taste's push for real photos in every section also does not fit a text-led how-to
   article; keep images to what the article needs.
5. **Order of authority** when they disagree: the owner's brief and brand, then frontend-design and Impeccable's Read
   mode for direction, then Taste's pre-flight as the final mechanical check.
