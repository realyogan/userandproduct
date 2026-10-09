#!/usr/bin/env python3
"""Phase 3 clustering of the section harvest (Links, Books, Tools, Templates) into candidate categories (free, local).

Standard library only. Reads distilled CSVs, never raw JSON.

Usage (from the project root):
    python research/seo/tools/cluster_sections.py [--date 2026-10-08] [--show SECTION]

Input:   keywords/harvest-sections-<date>.csv (unflagged rows with volume >= 100)
Output:  keywords/section-candidates-<date>.csv
         (section,category,keyword_count,total_volume,adjusted_volume,median_difficulty,template_share,
          question_share,top_keywords)

Method: the cluster_v2.py method with section thresholds. Ordered pattern rules per section, first match wins.
A first-level category needs 10 or more keywords (MIN_KW); smaller rule groups go to the section's
"(below threshold)" row, which lists them. A second-level category ("parent > child") is written when the
parent qualifies and the child has 5 or more keywords (MIN_SUB). Categories whose name ends in "(off-scope)"
are other meanings of the seed phrase (interior design books, rice purity test) kept visible, not proposed.
adjusted_volume: each distinct (volume, monthly_12) pair counted once (word-order variants share one series).
template_share and question_share: same definitions as cluster_v2.py, except that "sample size" does not count
as a template word.
"""
import argparse
import collections
import csv
import os
import re
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cluster_phase1 import tokens  # noqa: E402
from cluster_v2 import QUESTION, TEMPLATE  # noqa: E402

SEO = os.path.dirname(HERE)
MIN_KW, MIN_SUB = 10, 5

# section -> [(category, pattern, [(child, pattern), ...]), ...]; order matters, first match wins
RULES = {
    "links": [
        ("design resources (off-scope)", r"power design|resources inc|resources group|human resources|interior design|"
                                         r"trade resources|apple design", []),
        ("product management software (off-scope)", r"product lifecycle management|product information management", []),
        ("prototyping tools", r"prototyp", [("rapid prototyping tools", r"rapid|fast|quick")]),
        ("ux research and testing tools", r"research|testing|test tools|test\b", []),
        ("product management tools", r"product management|roadmap|product analytics", []),
        ("ux and ui design tools", r"\bux\b|\bui\b|ui/ux|user experience", []),
        ("design resources", r"design resources|resources for|resources graphic", []),
    ],
    "books": [
        ("book cover and layout design (off-scope)", r"cover|layout|book design|on book design|photo books|recipe books|"
                                                     r"comic books design|design your", []),
        ("interior, home and architecture design books (off-scope)",
         r"interior|house|home|furniture|landscap|architecture|flower", []),
        ("fashion and craft design books (off-scope)", r"fashion|clothing|apparel|pattern ?making|nail|tattoo|jewelry|"
                                                       r"human design", []),
        ("engineering and software design books (off-scope)", r"system|mechanical|vlsi|domain.driven|design patterns|"
                                                               r"pattern design", []),
        ("game and character design books", r"game|character", []),
        ("product management books", r"product management", []),
        ("ux design books", r"\bux\b|user experience", []),
        ("design thinking books", r"design thinking", []),
        ("graphic and visual design books", r"graphic|visual", []),
        ("design books (general)", r"design", []),
    ],
    "templates": [
        ("user story templates", r"user story",
         [("agile and scrum user story templates", r"agile|scrum|safe"),
          ("user story templates with acceptance criteria", r"acceptance"),
          ("user story template formats (word, doc, card)", r"word|doc|card")]),
        ("product roadmap templates", r"roadmap", [("roadmap templates for powerpoint", r"powerpoint|ppt")]),
        ("prd templates", r"\bprd\b|requirements", []),
        ("persona templates", r"persona", []),
    ],
    "tools": [
        ("rice purity test (off-scope)", r"purity", []),
        ("rice university and sports scores (off-scope)", r"football|basketball|baseball|\bsat\b|\bact\b|jerry rice|"
                                                           r"rice university|owls", []),
        ("a/b test calculators", r"\bab\b|a/b|a b test|split test", []),
        ("sample size calculators", r"sample size|size sample",
         [("power analysis sample size calculators", r"power"),
          ("statistical significance sample size calculators", r"significan|statistic|relevant"),
          ("survey sample size calculators", r"survey|raosoft|qualtrics|surveymonkey")]),
        ("prioritization scores (rice)", r"\brice score\b", []),
    ],
}


def adjusted(g):
    seen = {}
    for r in g:
        seen.setdefault((r["volume"], r["monthly_12"]), int(r["volume"]))
    return sum(seen.values())


def stats(g):
    kds = [float(r["difficulty"]) for r in g if r["difficulty"] != ""]
    q = sum(1 for r in g if (tokens(r["keyword"]) or [""])[0] in QUESTION)
    tp = sum(1 for r in g if TEMPLATE.search(r["keyword"].replace("sample size", "")))
    top = sorted(g, key=lambda r: (-int(r["volume"]), r["keyword"]))[:8]
    return {"keyword_count": len(g), "total_volume": sum(int(r["volume"]) for r in g), "adjusted_volume": adjusted(g),
            "median_difficulty": ("%g" % statistics.median(kds)) if kds else "",
            "template_share": "%.2f" % (tp / len(g)), "question_share": "%.2f" % (q / len(g)),
            "top_keywords": ";".join(r["keyword"] for r in top)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default="2026-10-08")
    ap.add_argument("--show", default="")
    args = ap.parse_args()
    kd = os.path.join(SEO, "keywords")
    with open(os.path.join(kd, "harvest-sections-%s.csv" % args.date), encoding="utf-8", newline="") as fh:
        rows = [r for r in csv.DictReader(fh) if not r.get("flag_v1_1", r["flag"]) and int(r["volume"] or 0) >= 100]  # v1.1 flags (see harvest.old_flag)
    out = []
    for sec, rules in RULES.items():
        srows = [r for r in rows if sec in r["section"].split(";")]
        groups = collections.OrderedDict((c, []) for c, _, _ in rules)
        rest = []
        for r in srows:
            c = next((c for c, p, _ in rules if re.search(p, r["keyword"])), None)
            (groups[c] if c else rest).append(r)
        below = []
        sec_rows = []
        for c, p, subs in rules:
            g = groups[c]
            if len(g) < MIN_KW:
                if g:
                    below.append((c, g))
                continue
            sec_rows.append(dict(stats(g), section=sec, category=c))
            parts = collections.OrderedDict((s, []) for s, _ in subs)
            for r in g:
                s = next((s for s, sp in subs if re.search(sp, r["keyword"])), None)
                if s:
                    parts[s].append(r)
            for s, pg in parts.items():
                if len(pg) >= MIN_SUB:
                    sec_rows.append(dict(stats(pg), section=sec, category="%s > %s" % (c, s)))
        sec_rows.sort(key=lambda x: (x["category"].endswith("(off-scope)"), -x["adjusted_volume"]) if " > " not in
                      x["category"] else (x["category"].split(" > ")[0].endswith("(off-scope)"), 0))
        # keep children right after their parent
        parents = [x for x in sec_rows if " > " not in x["category"]]
        ordered = []
        for pr in sorted(parents, key=lambda x: (x["category"].endswith("(off-scope)"), -x["adjusted_volume"])):
            ordered.append(pr)
            ordered.extend(sorted((x for x in sec_rows if x["category"].startswith(pr["category"] + " > ")),
                                  key=lambda x: -x["adjusted_volume"]))
        out.extend(ordered)
        leftover = [r for _, g in below for r in g] + rest
        if leftover:
            st = stats(leftover)
            st["top_keywords"] = "; ".join("%s: %d kw" % (c, len(g)) for c, g in below) + \
                                 ("; unmatched: %d kw" % len(rest) if rest else "")
            out.append(dict(st, section=sec, category="(below threshold)"))
        print("== %s: %d keywords" % (sec, len(srows)))
        for x in ordered:
            print("  %-62s n=%3d vol=%6d adj=%6d kd=%s" % (x["category"][:62], x["keyword_count"], x["total_volume"],
                                                          x["adjusted_volume"], x["median_difficulty"]))
        for c, g in below:
            print("  below: %-54s n=%3d adj=%6d" % (c, len(g), adjusted(g)))
        if rest:
            print("  unmatched:", "; ".join(r["keyword"] for r in rest))
        if args.show == sec:
            for c, g in list(groups.items()):
                print("  [%s] %s" % (c, "; ".join(r["keyword"] for r in g)))
    cols = ["section", "category", "keyword_count", "total_volume", "adjusted_volume", "median_difficulty",
            "template_share", "question_share", "top_keywords"]
    path = os.path.join(kd, "section-candidates-%s.csv" % args.date)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(out)
    print("->", path)


if __name__ == "__main__":
    main()
