---
name: seo-research
description: Cache-first, cost-aware keyword and competitor research for the User and the Product site. Use before ANY Ubersuggest or DataForSEO call, when the user asks about keyword volume, search demand, difficulty, SERPs, competitor traffic, sitemaps, keyword maps, or "what should we make next", or mentions "Ubersuggest", "DataForSEO", "keyword research", "search volume", "SERP", "competitor", "research budget" or "quota". Enforces checking research/seo/cache/index.csv first, reuse windows, batching, queue-not-live, filters, logging, and the daily spend cap.
---

# SEO research (cache first, spend last)

The store is `research/seo/`. Read `research/seo/README.md` once per session; it holds the
layout, the reuse windows, the price sheet and the file conventions. This skill is the short
version that must be followed every time.

## Before any paid or quota-limited call

1. `grep -i "<subject>" research/seo/cache/index.csv` for every keyword, seed or domain.
2. A hit younger than the reuse window (volumes/SERPs/domains 30 days, ideas and ranked
   keywords 60 days, sitemaps 90 days) means: open the distilled file in the `file` column and
   use it. Do not call.
3. Only subjects with no fresh hit go into the call, batched.

## When calling

- **Unmeasured endpoint = probe first.** If an endpoint has no measured price in the README price sheet, run ONE task, read `appmgmt/user_data` (free), and only then run the rest. (2026-09-28: historical_rank_overview turned out to be ~$0.15/task, not $0.012; 12 tasks blew a $1 cap.)
- Prefer bulk endpoints: DataForSEO Labs ideas/suggestions with filters (minimum volume,
  exclude brands/marketplaces, capped limit); Google Ads volumes up to 1,000 keywords per task on
  the **standard queue**; SERPs only for head terms. Ubersuggest: bulk suggestion tools first,
  single overviews only for a shortlist; it resets to 100 reports daily.
- US (`2840`) first; UK (`2826`) and CA (`2124`) only for a shortlist.
- Never track rankings through paid APIs; Search Console is free.

## After every call, before anything else

1. Save the raw response to `research/seo/cache/raw/<id>.json` (committed to Git) when the call came
   from code; MCP results that only exist in chat are distilled immediately.
2. Append one row per subject to `research/seo/cache/index.csv`
   (`id,date,source,endpoint,subject,location,file,note`).
3. Write or append the distilled CSV (`keywords/`, `serps/`, `competitors/`) in the documented
   columns. Empty volume + note = "no data", never zero.
4. Add a line to `research/seo/ledger.md` with reports used or dollars spent.

## Context hygiene

- Bulk research runs in a subagent that writes the files and reports a short summary.
- The main session reads distilled CSVs, never raw JSON.
- Do not paste large tool outputs into `context.md`; link the CSV.

## Account guardrails (user-side, remind if missing)

- DataForSEO dashboard: daily expense limit about $2 across the account; auto-recharge OFF.
- Pipeline client keeps a monthly ledger and stops at a soft budget.
- Typical cost: about $3.50 per pillar research pass; about $25 per quarter in normal use.
