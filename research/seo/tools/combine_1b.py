#!/usr/bin/env python3
"""Combine the Phase 1b harvest with the on-topic part of the Phase 1 harvest (free, local).

Standard library only. Usage (from the project root):
    python research/seo/tools/combine_1b.py [--date 2026-10-08]

Inputs:  keywords/harvest-articles-1b-<date>.csv (all rows)
         keywords/harvest-articles-<date>.csv + keywords/keyword-to-topic-<date>.csv (rows whose Phase 1
         topic is on-topic, i.e. not in OFF_TOPIC and not "unassigned")
Output:  keywords/harvest-articles-combined-<date>.csv (harvest columns + source: 1a, 1b or both),
         deduped on keyword; for "both" the 1b metrics are kept and seeds/domains are merged.
"""
import argparse
import csv
import os

SEO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OFF_TOPIC = {"ai tools", "design (general)", "marketing (general)", "graphic and visual design",
             "seo and keyword research", "customer service", "system and software design", "unassigned"}


def read(path):
    with open(path, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def merge(a, b):
    out = a.split(";") if a else []
    for x in (b.split(";") if b else []):
        if x not in out:
            out.append(x)
    return ";".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default="2026-10-08")
    args = ap.parse_args()
    kd = os.path.join(SEO, "keywords")
    b = read(os.path.join(kd, "harvest-articles-1b-%s.csv" % args.date))
    a = read(os.path.join(kd, "harvest-articles-%s.csv" % args.date))
    topic = {r["keyword"]: r["topic"] for r in read(os.path.join(kd, "keyword-to-topic-%s.csv" % args.date))}
    a_on = [r for r in a if r["keyword"] in topic and topic[r["keyword"]] not in OFF_TOPIC]
    cols = list(b[0].keys()) + ["source"]
    rows = {}
    for r in b:
        rows[r["keyword"]] = dict(r, source="1b")
    for r in a_on:
        if r["keyword"] in rows:
            x = rows[r["keyword"]]
            x["source"] = "both"
            x["seeds"] = merge(x["seeds"], r["seeds"])
            x["domains"] = merge(x["domains"], r["domains"])
        else:
            rows[r["keyword"]] = dict(r, source="1a")
    out = sorted(rows.values(), key=lambda r: (-int(r["volume"] or 0), r["keyword"]))
    path = os.path.join(kd, "harvest-articles-combined-%s.csv" % args.date)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(out)
    src = {}
    for r in out:
        src[r["source"]] = src.get(r["source"], 0) + 1
    print("1b rows %d; 1a on-topic rows %d; combined distinct %d; by source %s -> %s"
          % (len(b), len(a_on), len(out), src, path))


if __name__ == "__main__":
    main()
