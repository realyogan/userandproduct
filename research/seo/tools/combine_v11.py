#!/usr/bin/env python3
"""Build the v1.1 combined Articles harvest (free, local).

Standard library only. Usage (from the project root):
    python research/seo/tools/combine_v11.py [--date 2026-10-08]

Inputs:  keywords/harvest-articles-combined-<date>.csv (the Phase 1b combined set, sources 1a, 1b, both)
         keywords/review-unassigned-phase1-<date>.csv (rows kept by the manual review of the Phase 1 harvest;
         verdict existing or new); their full metrics come from keywords/harvest-articles-<date>.csv
         keywords/harvest-articles-ai-<date>.csv (Phase 1c: AI in product and design work, phrase match)
Output:  keywords/harvest-articles-combined-v1.1-<date>.csv, same columns; the added rows carry source
         "1a-review" or "1c-ai". Deduped on keyword: a keyword already present keeps its row.
         The v1.1 flags are written (an AI row's flag_v1_1 when the AI harvest was re-flagged). A re-run drops
         the v1.2 columns (flag_v1_1, fine_intent): run harvest.py reflag and reintent on the output afterwards.
"""
import argparse
import csv
import os

SEO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read(path):
    with open(path, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default="2026-10-08")
    args = ap.parse_args()
    kd = os.path.join(SEO, "keywords")
    base = read(os.path.join(kd, "harvest-articles-combined-%s.csv" % args.date))
    cols = list(base[0].keys())
    rows = {r["keyword"]: r for r in base}
    p1 = {r["keyword"]: r for r in read(os.path.join(kd, "harvest-articles-%s.csv" % args.date))}
    added = {"1a-review": 0, "1c-ai": 0}
    skipped = {"1a-review": 0, "1c-ai": 0}
    for r in read(os.path.join(kd, "review-unassigned-phase1-%s.csv" % args.date)):
        if r["verdict"] not in ("existing", "new"):
            continue
        if r["keyword"] in rows or r["keyword"] not in p1:
            skipped["1a-review"] += 1
            continue
        rows[r["keyword"]] = dict(p1[r["keyword"]], source="1a-review")
        added["1a-review"] += 1
    for r in read(os.path.join(kd, "harvest-articles-ai-%s.csv" % args.date)):
        if r["keyword"] in rows:
            skipped["1c-ai"] += 1
            continue
        rows[r["keyword"]] = dict(r, source="1c-ai", flag=r.get("flag_v1_1", r["flag"]))  # v1.1 flags
        added["1c-ai"] += 1
    out = sorted(rows.values(), key=lambda r: (-int(r["volume"] or 0), r["keyword"]))
    path = os.path.join(kd, "harvest-articles-combined-v1.1-%s.csv" % args.date)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(out)
    print("base %d; added %s; skipped as duplicates %s; total %d -> %s" % (len(base), added, skipped, len(out), path))


if __name__ == "__main__":
    main()
