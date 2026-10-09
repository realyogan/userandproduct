#!/usr/bin/env python3
"""Phase 4b pulls for the v1.1 units that are new (no head-term SERP or Trends row yet).

Standard library only. Every paid or task call goes through dataforseo_client.Client (raw file saved,
index row added, budget cap enforced). Reads distilled CSVs; parses raw JSON only to distil it.

Subcommands (run from the project root):
    python research/seo/tools/phase4b.py plan            # new head terms, cached or not (no call)
    python research/seo/tools/phase4b.py serp-post       # one task_post, one task per uncached head_term_1
    python research/seo/tools/phase4b.py serp-collect    # poll tasks_ready every 20 s, task_get/advanced, save
    python research/seo/tools/phase4b.py trends-run      # Google Trends explore live, groups of up to 5
    python research/seo/tools/phase4b.py trends-distil   # append the new rows to keywords/trends-<date>.csv

Inputs:  keywords/phase4-units-v1.1-<date>.csv, keywords/phase4-units-<date>.csv (v1 units: their pulls are reused)
Outputs: serps/phase4b-task-ids-<date>.csv, rows appended to serps/phase4-queries-<date>.csv,
         cache/raw/serps-<date>/<slug>.json, rows appended to keywords/trends-<date>.csv and
         keywords/trends-groups-<date>.csv, rows appended to keywords/phase4-spend-<date>.csv.
Google Ads volumes are not pulled for the new units; their scores use the Labs volume (ads_volume_head empty).
"""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from dataforseo_client import Client, index_row, read_index  # noqa: E402
from phase4 import (DATE, KW, SERPS, RAW_SERPS, SERP_EP, TRENDS_EP, read, write, log_spend, poll,  # noqa: E402
                    trends_task)
from serp_distill import slugify  # noqa: E402

SEO = os.path.dirname(HERE)
CAP = 0.40          # this step's share of the run cap (the AI harvest used the rest)
TASKS = os.path.join(SERPS, "phase4b-task-ids-%s.csv" % DATE)
QUERIES = os.path.join(SERPS, "phase4-queries-%s.csv" % DATE)
TRENDS = os.path.join(KW, "trends-%s.csv" % DATE)
GROUPS = os.path.join(KW, "trends-groups-%s.csv" % DATE)
# Trends groups for the new head terms, grouped by similar Labs volume so no term flattens the others.
TREND_GROUPS = [["principles of design", "customer experience", "ai for product managers"],
                ["ai powered design tools", "marketing research", "ux writing"],
                # regroup (as in Phase 4): the two terms that came out "too small" in group 20, pulled alone together
                ["ai powered design tools", "ux writing"]]


def new_heads():
    """(head_term_1, [unit_ids]) for v1.1 units whose head_term_1 was not a v1 head term."""
    v1 = {u["head_term_1"] for u in read(os.path.join(KW, "phase4-units-%s.csv" % DATE))}
    plan = {}
    for u in read(os.path.join(KW, "phase4-units-v1.1-%s.csv" % DATE)):
        if u["head_term_1"] not in v1:
            plan.setdefault(u["head_term_1"], []).append(u["unit_id"])
    have = {f[:-5] for f in os.listdir(RAW_SERPS) if f.endswith(".json") and not f.startswith("_")}
    return [(k, ids, slugify(k) in have) for k, ids in plan.items()]


def cmd_plan():
    for k, ids, cached in new_heads():
        print("%-30s %-12s %s" % (k, ";".join(ids), "cached" if cached else "to pull"))


def append_queries(plan):
    rows = read(QUERIES)
    known = {r["keyword"] for r in rows}
    for k, ids, cached in plan:
        if k not in known:
            rows.append({"section": "articles", "keyword": k, "phase": "phase0" if cached else "phase4",
                         "unit_ids": ";".join(ids)})
    write(QUERIES, ["section", "keyword", "phase", "unit_ids"], rows)


def cmd_serp_post():
    plan = new_heads()
    todo = [(k, ids) for k, ids, cached in plan if not cached]
    append_queries(plan)
    if not todo:
        print("nothing to post")
        return
    tasks = [{"keyword": k, "location_code": 2840, "language_code": "en", "depth": 10,
              "tag": "phase4b-" + ids[0]} for k, ids in todo]
    c = Client(cap=CAP)
    res = c.post(SERP_EP + "/task_post", tasks)
    cost = float(res.get("cost") or 0)
    rows = []
    for t in res.get("tasks") or []:
        rows.append({"task_id": t.get("id"), "keyword": (t.get("data") or {}).get("keyword", ""),
                     "tag": (t.get("data") or {}).get("tag", ""),
                     "status": "posted" if t.get("status_code") == 20100 else "error %s" % t.get("status_code")})
    write(TASKS, ["task_id", "keyword", "tag", "status"], rows)
    n_ok = sum(r["status"] == "posted" for r in rows)
    index_row(res["_id"], "dataforseo", SERP_EP + "/task_post", "phase4b serp batch (%d tasks)" % len(tasks), "2840",
              res["_file"], "phase4b serps; %d posted; $%.4f" % (n_ok, cost))
    log_spend("phase4b serps", cost, "task_post %d tasks" % len(tasks))
    print("posted %d, errors %d, cost $%.4f" % (n_ok, len(rows) - n_ok, cost))


def cmd_serp_collect():
    rows = read(TASKS)
    todo = {r["task_id"]: r for r in rows if r["status"] in ("posted", "not ready")}
    c = Client(cap=CAP)
    ready = poll(c, SERP_EP, list(todo), limit_s=900)
    got = 0
    for tid in sorted(ready):
        r = todo[tid]
        res = None
        for attempt in (1, 2):
            res = c.get(SERP_EP + "/task_get/advanced/" + tid, save=False)
            st = (res.get("tasks") or [{}])[0].get("status_code")
            if st == 20000 or attempt == 2:
                break
            time.sleep(5)
        t = (res.get("tasks") or [{}])[0]
        if t.get("status_code") != 20000:
            r["status"] = "get error %s" % t.get("status_code")
            continue
        data = {"id": t["id"], "status_code": t["status_code"], "status_message": t["status_message"],
                "cost": t.get("cost")}
        data.update((t.get("result") or [{}])[0])
        slug = slugify(r["keyword"])
        with open(os.path.join(RAW_SERPS, slug + ".json"), "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=False)
        index_row("261008-P4B-%03d" % (rows.index(r) + 1), "dataforseo",
                  "serp/google/organic/task_post+task_get/advanced (standard)", r["keyword"], "2840",
                  "research/seo/cache/raw/serps-%s/%s.json" % (DATE, slug),
                  "%s; task %s; $0.0006" % (r["tag"], tid))
        r["status"] = "collected"
        got += 1
    for r in rows:
        if r["status"] == "posted":
            r["status"] = "not ready"
    write(TASKS, ["task_id", "keyword", "tag", "status"], rows)
    print("collected %d of %d" % (got, len(todo)))


def group_numbers():
    base = max(int(r["group"]) for r in read(GROUPS))
    done = {r["keywords"]: int(r["group"]) for r in read(GROUPS)}
    out = []
    n = base
    for g in TREND_GROUPS:
        key = " | ".join(g)
        if key in done:
            out.append((done[key], g))
        else:
            n += 1
            out.append((n, g))
    return out


def cmd_trends_run():
    c = Client(cap=CAP)
    done = {r["subject"] for r in read_index() if r["endpoint"] == TRENDS_EP and "; ok;" in r["note"]}
    grows = read(GROUPS)
    for n, g in group_numbers():
        subj = " | ".join(g)
        if subj in done:
            print("group %d already pulled" % n)
            continue
        for attempt in (1, 2):
            res = c.post(TRENDS_EP, trends_task(g))
            st = (res.get("tasks") or [{}])[0].get("status_code")
            cost = float(res.get("cost") or 0)
            log_spend("phase4b trends", cost, "group %d attempt %d status %s" % (n, attempt, st))
            note = "phase4b trends group %d; %s; $%.4f" % (n, "ok" if st == 20000 else "status %s" % st, cost)
            index_row(res["_id"], "dataforseo", TRENDS_EP, subj, "2840", res["_file"], note)
            print("group %d status %s cost $%.4f" % (n, st, cost))
            if st == 20000:
                grows.append({"group": n, "keywords": subj, "raw": res["_file"]})
                break
            time.sleep(5)
    write(GROUPS, ["group", "keywords", "raw"], grows)


def series_for(raw_rel, group):
    """{keyword: [(YYYY-MM, value), ...]} from a saved Trends explore response."""
    with open(os.path.join(SEO, raw_rel), encoding="utf-8") as fh:
        res = json.load(fh)
    result = ((res["tasks"][0].get("result") or [{}])[0]) or {}
    graph = next((it for it in (result.get("items") or []) if it.get("type") == "google_trends_graph"), None)
    series = {k: [] for k in group}
    if graph:
        kws = [k.lower() for k in (graph.get("keywords") or group)]
        for pt in graph.get("data") or []:
            if pt.get("missing_data"):
                continue
            for i, v in enumerate(pt.get("values") or []):
                if i < len(kws) and kws[i] in series:
                    series[kws[i]].append((pt.get("date_from", "")[:7], v if v is not None else 0))
    return series


def trend_row(k, unit_ids, n, pts):
    """Same rules as phase4.cmd_trends_distil."""
    if not pts:
        return {"keyword": k, "unit_id": unit_ids, "group": n, "note": "no data"}
    first = [v for d, v in pts if "2021-10" <= d <= "2022-09"]
    last = [v for d, v in pts if "2025-10" <= d <= "2026-09"]
    a = sum(first) / len(first) if first else 0
    b = sum(last) / len(last) if last else 0
    t5 = "%.2f" % (b / a) if a > 0 else ""
    direction = ""
    note = "group %d (values relative within the group only); phase4b" % n
    if a < 1 and b < 1:
        t5, direction = "", "too small"
        note += "; both yearly averages under 1 (too small a share of the group to read)"
    elif t5:
        x = float(t5)
        direction = "rising" if x >= 1.2 else "falling" if x <= 0.8 else "flat"
        if a < 1:
            note += "; first-year average under 1, ratio exaggerated"
    elif b >= 1:
        direction = "rising"
        note += "; first-year average 0"
    peak = max(pts, key=lambda p: p[1])[0]
    w1 = [v for d, v in pts if "2025-09" <= d <= "2025-11"]
    w2 = [v for d, v in pts if "2026-06" <= d <= "2026-08"]
    m1 = sum(w1) / len(w1) if w1 else 0
    m2 = sum(w2) / len(w2) if w2 else 0
    t12 = "%.2f" % (m2 / m1) if m1 >= 1 else ""
    return {"keyword": k, "unit_id": unit_ids, "avg_first_year": "%.1f" % a, "avg_last_year": "%.1f" % b,
            "trend_5y": t5, "direction": direction, "peak_month": peak, "trends_12m": t12, "group": n, "note": note}


def cmd_trends_distil():
    heads = {}
    for u in read(os.path.join(KW, "phase4-units-v1.1-%s.csv" % DATE)):
        heads.setdefault(u["head_term_1"], []).append(u["unit_id"])
    raw = {int(r["group"]): r["raw"] for r in read(GROUPS)}
    rows = read(TRENDS)
    have = {r["keyword"] for r in rows}
    added = 0
    for n, g in group_numbers():
        if n not in raw:
            print("group %d has no raw file" % n)
            continue
        ser = series_for(raw[n], g)
        for k in g:
            new = trend_row(k, ";".join(heads.get(k, [])), n, ser.get(k))
            if k in have:
                old = next(r for r in rows if r["keyword"] == k)
                if old.get("direction") == "too small" and new.get("direction") not in ("too small", "", None)                         and str(old.get("group")) != str(n):
                    new["note"] += "; re-pulled (first group %s was too small to read)" % old["group"]
                    rows[rows.index(old)] = new
                continue
            rows.append(new)
            have.add(k)
            added += 1
    write(TRENDS, ["keyword", "unit_id", "avg_first_year", "avg_last_year", "trend_5y", "direction", "peak_month",
                   "trends_12m", "group", "note"], rows)
    print("trends rows added %d (total %d)" % (added, len(rows)))


if __name__ == "__main__":
    cmds = {"plan": cmd_plan, "serp-post": cmd_serp_post, "serp-collect": cmd_serp_collect,
            "trends-run": cmd_trends_run, "trends-distil": cmd_trends_distil}
    if len(sys.argv) < 2 or sys.argv[1] not in cmds:
        print(__doc__)
        sys.exit(1)
    cmds[sys.argv[1]]()
