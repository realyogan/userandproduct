# Search Console pulls (`gsc.py`)

Google Search Console data for https://userandproduct.com, stored in
`research/seo/cache/gsc/`. Free API; no spend cap, but every session is logged.

Every command is read-only except `sitemaps --submit`, which is the only write path: it
submits (or resubmits) one sitemap to the property and changes nothing else.

## Setup

- `pip install --user google-auth requests`
- Service account key at `.local/gsc-service-account.json` (git-ignored; override with env `GSC_KEY`).
  Never print, copy or commit it. The service account email must be a user on the property in
  Search Console (Settings > Users and permissions); otherwise the script exits 2 with that message.
- Property: `sc-domain:userandproduct.com` (falls back to `https://userandproduct.com/`).
  The property does not exist yet (the site is not live); create and verify it before the first run.

## Run

```
python research/seo/tools/gsc.py sites                     # properties and permission levels
python research/seo/tools/gsc.py sitemaps                  # submitted sitemaps, errors, counts
python research/seo/tools/gsc.py sitemaps --submit         # WRITE: submit sitemap_index.xml, then re-list
python research/seo/tools/gsc.py sitemaps --submit https://userandproduct.com/other-sitemap.xml
python research/seo/tools/gsc.py performance --dimension page   # also query | page,query | date; --days 28
python research/seo/tools/gsc.py inspect                   # URL Inspection over the live sitemap
python research/seo/tools/gsc.py inspect --urls list.txt --limit 100
python research/seo/tools/gsc.py summary                   # Markdown from cached files, no API calls
python research/seo/tools/gsc.py all                       # all of the above
```

Performance dates end 2 days ago (Search Console lag).

## Cache files (`research/seo/cache/gsc/`)

| File | Content |
|---|---|
| `sitemaps-YYYY-MM-DD.json` | sitemaps as Search Console reports them |
| `performance-page-YYYY-MM-DD.csv`, `performance-query-YYYY-MM-DD.csv` | clicks, impressions, ctr, position per page / query |
| `inspect.csv` | rolling, one row per URL, latest inspection wins |
| `summary-YYYY-MM-DD.md` | coverage-state counts, URLs not "Submitted and indexed", top 20 pages and queries |

Each API session adds one row to `research/seo/cache/index.csv` (source `gsc`, note
`free; calls N; rows M`; a submit adds `; submit`).

## Quota

URL Inspection allows 2,000 calls per property per day (600 per minute). The script stops at
`--limit` (default 600), skips URLs inspected in the last 7 days, sleeps 0.3 s between calls,
backs off on 429 and keeps going on single-URL errors. Run it again the next day to continue.
Search Analytics and sitemaps calls are cheap (a handful per session).
