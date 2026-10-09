#!/usr/bin/env python3
"""Phase 2 competitor sizing for userandproduct.com (traffic tiers, ranked keywords, topic coverage).

Standard library only. Uses dataforseo_client.py (cache check, budget guard, raw save).

Usage (from the project root):
    python research/seo/tools/phase2.py domains                 # print the deduped domain list
    python research/seo/tools/phase2.py traffic --cap 0.10      # bulk_traffic_estimation, one task
    python research/seo/tools/phase2.py traffic-distil          # -> competitors/traffic-<date>.csv + tier columns
    python research/seo/tools/phase2.py pick                    # the four Articles domains for ranked keywords
    python research/seo/tools/phase2.py ranked --probe --cap .2 # first domain only
    python research/seo/tools/phase2.py ranked --cap 0.40       # the rest (cached ones skipped)
    python research/seo/tools/phase2.py ranked-distil           # -> competitors/ranked-<domain>-<date>.csv
    python research/seo/tools/phase2.py coverage                # -> competitors/coverage-by-topic-<date>.csv

Domain list: every domain in competitors/{articles,links,books,tools,templates}-competitors.csv and
competitors/seeds.csv, lower-cased, without "www.", minus the platform drop list (DROP; *.medium.com and
gist.github.com count as platforms).
Tier: A organic_etv >= 1,000,000; B >= 100,000; C >= 10,000; D below (US, estimated monthly organic visits).
Coverage mapping: exact match against keywords/keyword-to-topic-v2-<date>.csv; otherwise the topic or
sub-topic sharing the most non-stopword tokens (at least two) with its name and top_keywords; else "unmapped".
"""
import argparse
import collections
import csv
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dataforseo_client as dfs  # noqa: E402
from cluster_phase1 import STOP, tokens  # noqa: E402

SEO = dfs.SEO
COMP = os.path.join(SEO, "competitors")
SECTIONS = ["articles", "links", "books", "tools", "templates"]
DROP = set("reddit.com linkedin.com youtube.com en.wikipedia.org quora.com medium.com pinterest.com scribd.com "
           "amazon.com google.com github.com facebook.com x.com twitter.com instagram.com".split())
EP_TRAFFIC = "dataforseo_labs/google/bulk_traffic_estimation/live"
EP_RANKED = "dataforseo_labs/google/ranked_keywords/live"
RANK_TYPES = {"publication", "saas", "expert", "education"}


def read(path):
    with open(path, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def norm(d):
    d = d.strip().lower()
    return d[4:] if d.startswith("www.") else d


def dropped(d):
    return d in DROP or d.endswith(".medium.com") or d == "gist.github.com"


def domain_sections():
    secs = collections.defaultdict(set)
    p1 = collections.Counter()
    for s in SECTIONS:
        for r in read(os.path.join(COMP, "%s-competitors.csv" % s)):
            d = norm(r["domain"])
            secs[d].add(s)
            p1[d] += int(r.get("page_one_count") or 0)
    for r in read(os.path.join(COMP, "seeds.csv")):
        secs[norm(r["domain"])].add(r["section"].strip().lower())
    return secs, p1


def domains():
    secs, _ = domain_sections()
    return sorted(d for d in secs if not dropped(d))


def tier(etv):
    if etv is None:
        return ""
    return "A" if etv >= 1e6 else "B" if etv >= 1e5 else "C" if etv >= 1e4 else "D"


def task_status(res):
    t = (res.get("tasks") or [{}])[0]
    return t.get("status_code"), t.get("status_message"), t.get("result") or []


def post_retry(c, ep, tasks, subject):
    res = c.post(ep, tasks, subject=subject)
    if res is None:
        return None
    code, msg, _ = task_status(res)
    if code == 50000 or res.get("status_code") == 50000:
        dfs.index_row(res["_id"], "dataforseo", ep, subject, "2840", res["_file"],
                      "phase2; 0 rows; $%.4f; status %s %s" % (float(res.get("cost") or 0), code, msg))
        print("50000 on %s; retrying in 5 s" % subject)
        time.sleep(5)
        res = c.post(ep, tasks, subject=subject)
    return res


def cmd_traffic(args):
    ds = domains()
    c = dfs.Client(cap=args.cap, dry_run=args.dry_run)
    subj = "phase2 competitor list (%d domains)" % len(ds)
    res = post_retry(c, EP_TRAFFIC, [{"targets": ds, "location_code": 2840, "language_code": "en"}], subj)
    if res is None:
        return
    code, msg, result = task_status(res)
    items = ((result[0] or {}).get("items") or []) if result else []
    cost = float(res.get("cost") or 0)
    note = "phase2; %d rows; $%.4f" % (len(items), cost)
    if code != 20000:
        note += "; status %s %s" % (code, msg)
    dfs.index_row(res["_id"], "dataforseo", EP_TRAFFIC, subj, "2840", res["_file"], note)
    print("traffic: %d domains sent, %d rows, cost $%.4f, status %s" % (len(ds), len(items), cost, code))


def latest_file(ep, prefix="phase2;", subject=None):
    best = None
    for r in dfs.read_index():
        if r["endpoint"] == ep and r["note"].startswith(prefix) and "; status " not in r["note"]:
            if subject is None or r["subject"] == subject:
                best = r
    return best


def load_etv():
    etv = {}
    tp = os.path.join(COMP, "traffic-2026-10-08.csv")
    if os.path.exists(tp):
        for r in read(tp):
            etv[r["domain"]] = float(r["organic_etv"] or 0)
    return etv


def cmd_traffic_distil(args):
    row = latest_file(EP_TRAFFIC)
    with open(os.path.join(SEO, row["file"]), encoding="utf-8") as fh:
        res = json.load(fh)
    _, _, result = task_status(res)
    items = (result[0] or {}).get("items") or []
    secs, p1 = domain_sections()
    m = {}
    for it in items:
        d = norm(it.get("target") or "")
        met = it.get("metrics") or {}
        org = met.get("organic") or {}
        paid = met.get("paid") or {}
        m[d] = (org.get("etv"), org.get("count"), paid.get("etv"))
    out = []
    for d in domains():
        etv, cnt, petv = m.get(d, (None, None, None))
        out.append({"domain": d, "organic_etv": "" if etv is None else round(etv),
                    "organic_count": "" if cnt is None else cnt,
                    "paid_etv": "" if petv is None else round(petv),
                    "sections": ";".join(s for s in SECTIONS if s in secs[d]),
                    "page_one_total": p1.get(d, 0), "tier": tier(etv)})
    out.sort(key=lambda r: (r["organic_etv"] == "", -(r["organic_etv"] or 0), r["domain"]))
    path = os.path.join(COMP, "traffic-%s.csv" % args.date)
    cols = ["domain", "organic_etv", "organic_count", "paid_etv", "sections", "page_one_total", "tier"]
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(out)
    by = {r["domain"]: r for r in out}
    for s in SECTIONS:
        p = os.path.join(COMP, "%s-competitors.csv" % s)
        rows = read(p)
        cols_s = [c for c in rows[0].keys() if c not in ("organic_etv", "tier")] + ["organic_etv", "tier"]
        for r in rows:
            x = by.get(norm(r["domain"]))
            r["organic_etv"] = x["organic_etv"] if x else ""
            r["tier"] = x["tier"] if x else ""
        with open(p, "w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=cols_s)
            w.writeheader()
            w.writerows(rows)
    tiers = collections.Counter(r["tier"] or "no data" for r in out)
    print("traffic rows %d (api items %d); tiers %s -> %s" % (len(out), len(items), dict(tiers), path))


def pick():
    etv = load_etv()
    rows = [r for r in read(os.path.join(COMP, "articles-competitors.csv"))
            if not dropped(norm(r["domain"])) and r["type"].strip().lower() in RANK_TYPES]
    rows.sort(key=lambda r: (-int(r["page_one_count"]), -etv.get(norm(r["domain"]), 0)))
    return [norm(r["domain"]) for r in rows[:4]], rows[:8]


def cmd_pick(args):
    four, top = pick()
    etv = load_etv()
    for r in top:
        print(r["domain"], r["type"], r["page_one_count"], etv.get(norm(r["domain"]), ""))
    print("picked:", four)


def ranked_task(d):
    return [{"target": d, "location_code": 2840, "language_code": "en", "limit": 500,
             "filters": [["keyword_data.keyword_info.search_volume", ">=", 100]],
             "order_by": ["keyword_data.keyword_info.search_volume,desc"]}]


def cmd_ranked(args):
    four, _ = pick()
    if args.probe:
        four = four[:1]
    c = dfs.Client(cap=args.cap, dry_run=args.dry_run)
    for i, d in enumerate(four):
        if i:
            time.sleep(1)
        try:
            res = post_retry(c, EP_RANKED, ranked_task(d), d)
        except dfs.BudgetExceeded:
            break
        if res is None:
            continue
        code, msg, result = task_status(res)
        items = ((result[0] or {}).get("items") or []) if result else []
        total = (result[0] or {}).get("total_count") if result else None
        cost = float(res.get("cost") or 0)
        note = "phase2; %d rows; $%.4f" % (len(items), cost)
        if code != 20000:
            note += "; status %s %s" % (code, msg)
        dfs.index_row(res["_id"], "dataforseo", EP_RANKED, d, "2840", res["_file"], note)
        print("%-24s rows %3d (total_count %s) cost $%.4f status %s %s" % (d, len(items), total, cost, code,
                                                                            msg if code != 20000 else ""))
    print("run spent $%.4f over %d requests" % (c.spent, c.requests))


def cmd_ranked_distil(args):
    four, _ = pick()
    for d in four:
        row = latest_file(EP_RANKED, subject=d)
        if not row:
            print("no data for", d)
            continue
        with open(os.path.join(SEO, row["file"]), encoding="utf-8") as fh:
            res = json.load(fh)
        _, _, result = task_status(res)
        items = (result[0] or {}).get("items") or []
        out = {}
        for it in items:
            kd = it.get("keyword_data") or {}
            kw = (kd.get("keyword") or "").strip().lower()
            ki = kd.get("keyword_info") or {}
            kp = kd.get("keyword_properties") or {}
            si = kd.get("search_intent_info") or {}
            se = (it.get("ranked_serp_element") or {}).get("serp_item") or {}
            rec = {"keyword": kw, "volume": ki.get("search_volume"), "difficulty": kp.get("keyword_difficulty"),
                   "position": se.get("rank_absolute") or se.get("rank_group"), "url": se.get("url"),
                   "intent": si.get("main_intent")}
            if kw and (kw not in out or (rec["position"] or 999) < (out[kw]["position"] or 999)):
                out[kw] = rec
        cols = ["keyword", "volume", "difficulty", "position", "url", "intent"]
        path = os.path.join(COMP, "ranked-%s-%s.csv" % (d, args.date))
        with open(path, "w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=cols)
            w.writeheader()
            for r in sorted(out.values(), key=lambda r: (-(r["volume"] or 0), r["keyword"])):
                w.writerow({k: ("" if r[k] is None else r[k]) for k in cols})
        print("%-24s %d keywords -> %s" % (d, len(out), path))


def content_tokens(s):
    return set(t for t in tokens(s) if t not in STOP and len(t) > 1)


def cmd_coverage(args):
    four, _ = pick()
    kd = os.path.join(SEO, "keywords")
    exact = {r["keyword"]: (r["topic"], r["subtopic"])
             for r in read(os.path.join(kd, "keyword-to-topic-v2-%s.csv" % args.date)) if r["topic"] != "unassigned"}
    cands = read(os.path.join(kd, "topic-candidates-v2-%s.csv" % args.date))
    split = {r["topic"] for r in cands if r["subtopic"]}
    rows_out = [(r["topic"], r["subtopic"]) for r in cands if not (r["topic"] in split and not r["subtopic"])]
    profiles = []
    for r in cands:
        if r["topic"] in split and not r["subtopic"]:
            continue  # a split topic is matched through its sub-topic rows
        toks = content_tokens(r["topic"] + " " + r["subtopic"] + " " + r["top_keywords"].replace(";", " "))
        profiles.append((r["topic"], r["subtopic"], toks))
    counts = collections.defaultdict(collections.Counter)
    how = collections.Counter()
    for d in four:
        p = os.path.join(COMP, "ranked-%s-%s.csv" % (d, args.date))
        if not os.path.exists(p):
            continue
        for r in read(p):
            kw = r["keyword"]
            if kw in exact:
                key = exact[kw]
                how["exact"] += 1
            else:
                kt = content_tokens(kw)
                best, bs = None, 1
                for t, s, toks in profiles:
                    n = len(kt & toks)
                    if n > bs:
                        best, bs = (t, s), n
                key = best or ("unmapped", "")
                how["tokens" if best else "unmapped"] += 1
            counts[key][d] += 1
    cols = ["topic", "subtopic"] + four + ["total", "gap"]
    path = os.path.join(COMP, "coverage-by-topic-%s.csv" % args.date)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for t, s in rows_out + [("unmapped", "")]:
            c = counts.get((t, s), collections.Counter())
            vals = [c[d] for d in four]
            gap = "" if t == "unmapped" else ("yes" if max(vals) < 5 else "no")
            w.writerow([t, s] + vals + [sum(vals), gap])
            print("%-40s %-45s %s total %d %s" % (t[:40], s[:45], vals, sum(vals), gap))
    print("mapping:", dict(how), "->", path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["domains", "traffic", "traffic-distil", "pick", "ranked", "ranked-distil",
                                    "coverage"])
    ap.add_argument("--probe", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--cap", type=float, default=0.10)
    ap.add_argument("--date", default="2026-10-08")
    args = ap.parse_args()
    if args.cmd == "domains":
        ds = domains()
        print(len(ds), ds)
        return
    {"traffic": cmd_traffic, "traffic-distil": cmd_traffic_distil, "pick": cmd_pick, "ranked": cmd_ranked,
     "ranked-distil": cmd_ranked_distil, "coverage": cmd_coverage}[args.cmd](args)


if __name__ == "__main__":
    main()
