# userandproduct.com — project context (working title "User and the Product")

## What this is
userandproduct.com: a Smashing-Magazine-style knowledge site at the intersection of UX, product
management and business, written by the owner (15 years in product design and product management).
Primary goal: authority in both directions (the experience backs the site, the site backs the owner).
Second: organic search traffic. Later: books with affiliate links, a tools and links directory,
calculators and small tools, templates, courses. The owner's BRD is
`research/discussion/brd-v1-2026-10-08.md`.

Phase 1 (now): discussion and SEO research, then articles that rank. Nothing is built yet.
Planned stack, same as the sister project (Printables, c:\xampp\htdocs\Printables): WordPress +
GeneratePress parent + our child theme + our structure plugin (post types, taxonomies) + Rank Math,
served locally by XAMPP at http://localhost/user-and-product/. Everything free, from wordpress.org.

## Discussion log
`research/discussion/context.md` is the running record of everything discussed and decided. Read it and
the newest `research/discussion/todo/next-session-<date>.md` at the start of a session; append to
context.md when a decision is made.

## The system carried over from Printables
Only the method carries over, not the content: the SEO research store (`research/seo/`, cache-first,
spend-last, rules in `.claude/skills/seo-research/`), the pillar method, the competitor pass, the tree
and build-plan app idea, build windows with scheduled posts, and the ops layer. The tools in
`research/seo/tools/` still point at the Printables domain and file names and must be re-pointed
before first use.

## Working rules for Claude
- Planning, thinking, architecture, reviews: the main session (Fable 5.1).
- All code writing and execution: delegate to subagents running Opus 5.5 (`model: "opus"`).
- Chat and plan before building; answer questions first and wait for a "go".
- Save anything the owner shares (lists, screenshots, documents) under `research/` the same session.
- No AI attribution in anything a reader sees: no Co-Authored-By trailers, no model or tool names in
  commits, in research documents, explainers or the site. `CLAUDE.md` and `.claude/` (skills, agents)
  ARE tracked in git (owner, 9 Oct 2026: everything goes to git except secrets); vendored skills may
  name their tools. Secrets live only in `.local/`, which stays ignored.
- Dependency-light: no build step, no frameworks; plain CSS + small vanilla JS; WP-CLI for setup.
- US English and US spelling; US first, then the UK and Canada.
- Give clickable http://localhost/user-and-product/... URLs for any HTML page.

## WordPress development rules
Child theme as light as possible; structure (post types, taxonomies) in the plugin, never the theme;
escaping and sanitising everywhere; i18n-ready; no direct DB queries; one canonical URL per page;
attachment pages disabled; filters never create indexable URLs; semantic HTML; Core Web Vitals in
mind. Load the project skills in `.claude/skills/` when writing or reviewing theme or plugin code.
