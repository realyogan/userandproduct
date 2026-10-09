#!/usr/bin/env python3
"""Phase 4 pulls: Google Ads volumes, page-one SERPs and Google Trends for the scoring units.

Standard library only. Every paid or task call goes through dataforseo_client.Client (raw file saved,
index row added, budget cap enforced). Reads distilled CSVs; parses raw JSON only to distil it.

Subcommands (run from the project root):
    python research/seo/tools/phase4.py ads-list          # print the keyword list (no call)
    python research/seo/tools/phase4.py ads-post          # one standard-queue task (Google Ads search volume)
    python research/seo/tools/phase4.py ads-collect       # poll tasks_ready, task_get, distil
    python research/seo/tools/phase4.py serp-post         # one task_post with one task per new head_term_1
    python research/seo/tools/phase4.py serp-collect      # poll, task_get/advanced, save per keyword
    python research/seo/tools/phase4.py trends-probe      # one live explore task
    python research/seo/tools/phase4.py trends-run        # the remaining groups
    python research/seo/tools/phase4.py trends-distil     # keywords/trends-<date>.csv

Inputs:  keywords/phase4-units-<date>.csv (from phase4_units.py), the harvest CSVs (Labs volumes).
Outputs: keywords/ads-volumes-<date>.csv, serps/phase4-queries-<date>.csv, serps/phase4-task-ids-<date>.csv,
         cache/raw/serps-<date>/<slug>.json, keywords/trends-<date>.csv, keywords/trends-groups-<date>.csv
"""
import csv
import json
import os
import re
import statistics
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from dataforseo_client import Client, index_row, read_index  # noqa: E402
from phase4_units import load_units, adjusted, HEADS  # noqa: E402
from serp_distill import slugify  # noqa: E402

SEO = os.path.dirname(HERE)
KW = os.path.join(SEO, "keywords")
SERPS = os.path.join(SEO, "serps")
DATE = "2026-10-08"
RAW_SERPS = os.path.join(SEO, "cache", "raw", "serps-" + DATE)
CAP = 0.60
STATE = os.path.join(SEO, "keywords", "phase4-spend-%s.csv" % DATE)

ADS_EP = "keywords_data/google_ads/search_volume"
SERP_EP = "serp/google/organic"
TRENDS_EP = "keywords_data/google_trends/explore/live"
BAD_ADS = re.compile(r"[,!@%^()={};~`<>?\\|*\"]")


# ---------------------------------------------------------------- shared

def read(path):
    with open(path, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def write(path, cols, rows):
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def log_spend(step, cost, note):
    """Running spend log for this phase (one row per paid response)."""
    new = not os.path.exists(STATE)
    with open(STATE, "a", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        if new:
            w.writerow(["step", "cost", "note"])
        w.writerow([step, "%.4f" % cost, note])


def spent_so_far():
    if not os.path.exists(STATE):
        return 0.0
    return sum(float(r["cost"]) for r in read(STATE))


def client():
    left = CAP - spent_so_far()
    if left <= 0:
        raise SystemExit("phase cap of $%.2f reached" % CAP)
    return Client(cap=left)


def units():
    return read(os.path.join(KW, "phase4-units-%s.csv" % DATE))


def labs_rows():
    rows = {}
    for name in ("harvest-articles-combined-%s.csv" % DATE, "harvest-sections-%s.csv" % DATE):
        for r in read(os.path.join(KW, name)):
            rows.setdefault(r["keyword"], r)
    return rows


def slope(vols):
    if len(vols) == 12 and all(v is not None for v in vols):
        a, b = sum(vols[:3]) / 3.0, sum(vols[-3:]) / 3.0
        return "%.2f" % (b / a) if a > 0 else ""
    return ""


# ---------------------------------------------------------------- Google Ads volumes

def ads_keywords():
    us = units()
    heads = []
    for u in us:
        for h in (u["head_term_1"], u["head_term_2"]):
            if h and h not in heads:
                heads.append(h)
    full, _ = load_units()
    pool = {}
    for u in full:
        for r in u["rows"]:
            if not r.get("flag_v1_1", r["flag"]):
                pool[r["keyword"]] = r
    seen_groups = {(pool[h]["volume"], pool[h]["monthly_12"]) for h in heads if h in pool}
    extra = []
    for r in sorted(pool.values(), key=lambda r: (-int(r["volume"] or 0), r["keyword"])):
        if r["keyword"] in heads or BAD_ADS.search(r["keyword"]):
            continue
        g = (r["volume"], r["monthly_12"])
        if g in seen_groups:          # a word-order variant of a keyword already in the list
            continue
        seen_groups.add(g)
        extra.append(r["keyword"])
        if len(extra) == 100:
            break
    kws = [k for k in heads + extra if not BAD_ADS.search(k) and len(k) <= 80 and len(k.split()) <= 10]
    return kws, heads, extra


def cmd_ads_list():
    kws, heads, extra = ads_keywords()
    print("head terms %d, extra %d, total %d" % (len(heads), len(extra), len(kws)))
    print("; ".join(extra))


def cmd_ads_post():
    kws, heads, extra = ads_keywords()
    c = client()
    res = c.post(ADS_EP + "/task_post", [{"keywords": kws, "location_code": 2840, "language_code": "en",
                                           "tag": "phase4-ads"}])
    t = res["tasks"][0]
    cost = float(res.get("cost") or 0)
    index_row(res["_id"], "dataforseo", ADS_EP + "/task_post", "phase4 ads batch (%d keywords)" % len(kws), "2840",
              res["_file"], "phase4 ads; task %s; status %s; $%.4f" % (t["id"], t["status_code"], cost)
              if t["status_code"] >= 40000 else "phase4 ads; task %s; posted; $%.4f" % (t["id"], cost))
    log_spend("ads", cost, "task_post %d keywords; task %s; status %s" % (len(kws), t["id"], t["status_code"]))
    print("posted task %s status %s %s cost $%.4f" % (t["id"], t["status_code"], t["status_message"], cost))


def ads_task_id():
    for r in reversed(read_index()):
        if r["endpoint"] == ADS_EP + "/task_post" and "posted" in r["note"]:
            return r["note"].split("task ")[1].split(";")[0]
    raise SystemExit("no posted ads task in the index")


def poll(c, ep, wanted, limit_s=600):
    """Poll <ep>/tasks_ready every 20 s until every id in wanted is listed (or the limit passes)."""
    wanted = set(wanted)
    ready = set()
    start = time.time()
    while True:
        res = c.get(ep + "/tasks_ready", save=False)
        for t in res.get("tasks") or []:
            for r in t.get("result") or []:
                if r.get("id") in wanted:
                    ready.add(r["id"])
        print("ready %d of %d after %ds" % (len(ready), len(wanted), time.time() - start))
        if ready >= wanted or time.time() - start > limit_s:
            return ready
        time.sleep(20)


def cmd_ads_collect():
    tid = ads_task_id()
    c = client()
    poll(c, ADS_EP, [tid])
    res = c.get(ADS_EP + "/task_get/" + tid)
    t = res["tasks"][0]
    print("task_get status %s %s" % (t["status_code"], t["status_message"]))
    items = t.get("result") or []
    labs = labs_rows()
    out, ratios = [], []
    for it in items:
        kw = (it.get("keyword") or "").lower()
        ms = sorted((m for m in (it.get("monthly_searches") or []) if m.get("year")),
                    key=lambda m: (m["year"], m["month"]))[-12:]
        vols = [m.get("search_volume") for m in ms]
        ads = it.get("search_volume")
        lab = labs.get(kw, {}).get("volume", "")
        ratio = ""
        if ads is not None and lab not in ("", None) and int(lab) > 0:
            ratio = "%.2f" % (ads / int(lab))
            ratios.append(ads / int(lab))
        out.append({"keyword": kw, "ads_volume": "" if ads is None else ads,
                    "cpc": "" if it.get("cpc") is None else it.get("cpc"),
                    "competition": it.get("competition") or "",
                    "monthly_12": ";".join("" if v is None else str(v) for v in vols),
                    "slope_12m": slope(vols), "labs_volume": lab, "ratio": ratio})
        index_row(res["_id"], "dataforseo", ADS_EP + "/task_get", kw, "2840",
                  "keywords/ads-volumes-%s.csv" % DATE,
                  "phase4 ads; raw %s; task %s" % (res["_file"], tid) + ("" if ads is not None else "; no data"))
    path = os.path.join(KW, "ads-volumes-%s.csv" % DATE)
    write(path, ["keyword", "ads_volume", "cpc", "competition", "monthly_12", "slope_12m", "labs_volume", "ratio"],
          out)
    print("rows %d -> %s" % (len(out), path))
    if ratios:
        print("median ads/labs ratio %.2f over %d keywords" % (statistics.median(ratios), len(ratios)))


# ---------------------------------------------------------------- SERPs

def serp_plan():
    """(keyword, unit_ids, cached) for every distinct head_term_1."""
    plan = {}
    for u in units():
        plan.setdefault(u["head_term_1"], []).append(u["unit_id"])
    have = {f[:-5] for f in os.listdir(RAW_SERPS) if f.endswith(".json") and not f.startswith("_")}
    return [(k, ids, slugify(k) in have) for k, ids in plan.items()]


def write_phase4_queries():
    rows = []
    for k, ids, cached in serp_plan():
        sec = units_by_id()[ids[0]]["section_or_domain"]
        sec = sec if sec in ("links", "books", "templates", "tools") else "articles"
        rows.append({"section": sec, "keyword": k, "phase": "phase0" if cached else "phase4",
                     "unit_ids": ";".join(ids)})
    write(os.path.join(SERPS, "phase4-queries-%s.csv" % DATE), ["section", "keyword", "phase", "unit_ids"], rows)


def units_by_id():
    return {u["unit_id"]: u for u in units()}


def cmd_serp_post():
    plan = serp_plan()
    todo = [(k, ids) for k, ids, cached in plan if not cached]
    print("head terms %d; cached from Phase 0 %d; to post %d" % (len(plan), len(plan) - len(todo), len(todo)))
    write_phase4_queries()
    tasks = [{"keyword": k, "location_code": 2840, "language_code": "en", "depth": 10,
              "tag": "phase4-" + ids[0]} for k, ids in todo]
    c = client()
    res = c.post(SERP_EP + "/task_post", tasks)
    cost = float(res.get("cost") or 0)
    rows = []
    for t in res.get("tasks") or []:
        kw = t.get("data", {}).get("keyword", "")
        rows.append({"task_id": t.get("id"), "keyword": kw, "tag": t.get("data", {}).get("tag", ""),
                     "status": "posted" if t.get("status_code") == 20100 else "error %s" % t.get("status_code")})
    write(os.path.join(SERPS, "phase4-task-ids-%s.csv" % DATE), ["task_id", "keyword", "tag", "status"], rows)
    index_row(res["_id"], "dataforseo", SERP_EP + "/task_post", "phase4 serp batch (%d tasks)" % len(tasks), "2840",
              res["_file"], "phase4 serps; %d posted; $%.4f" % (sum(r["status"] == "posted" for r in rows), cost))
    log_spend("serps", cost, "task_post %d tasks" % len(tasks))
    print("posted %d, errors %d, cost $%.4f" % (sum(r["status"] == "posted" for r in rows),
                                                 sum(r["status"] != "posted" for r in rows), cost))


def cmd_serp_collect():
    rows = read(os.path.join(SERPS, "phase4-task-ids-%s.csv" % DATE))
    todo = {r["task_id"]: r for r in rows if r["status"] == "posted"}
    c = client()
    ready = poll(c, SERP_EP, list(todo), limit_s=600)
    got = 0
    for tid in sorted(ready):
        r = todo[tid]
        res = None
        for attempt in (1, 2):
            res = c.get(SERP_EP + "/task_get/advanced/" + tid, save=False)
            st = (res.get("tasks") or [{}])[0].get("status_code")
            if st == 20000:
                break
            if attempt == 1 and st == 50000:
                time.sleep(5)
                continue
            break
        t = (res.get("tasks") or [{}])[0]
        if t.get("status_code") != 20000:
            r["status"] = "get error %s" % t.get("status_code")
            continue
        result = (t.get("result") or [{}])[0]
        data = {"id": t["id"], "status_code": t["status_code"], "status_message": t["status_message"],
                "cost": t.get("cost")}
        data.update(result)
        slug = slugify(r["keyword"])
        with open(os.path.join(RAW_SERPS, slug + ".json"), "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=False)
        index_row("261008-P4S-%03d" % (rows.index(r) + 1), "dataforseo",
                  "serp/google/organic/task_post+task_get/advanced (standard)", r["keyword"], "2840",
                  "research/seo/cache/raw/serps-%s/%s.json" % (DATE, slug),
                  "phase4 %s; task %s; $0.0006" % (r["tag"], tid))
        r["status"] = "collected"
        got += 1
    for r in rows:
        if r["status"] == "posted":
            r["status"] = "not ready"
    write(os.path.join(SERPS, "phase4-task-ids-%s.csv" % DATE), ["task_id", "keyword", "tag", "status"], rows)
    print("collected %d of %d" % (got, len(todo)))


# ---------------------------------------------------------------- Trends

def trend_groups():
    kws = []
    for u in units():
        if u["head_term_1"] not in kws:
            kws.append(u["head_term_1"])
    groups = [kws[i:i + 5] for i in range(0, len(kws), 5)]
    if os.path.exists(REGROUP):
        groups += [r["keywords"].split(" | ") for r in read(REGROUP)]
    return groups


REGROUP = os.path.join(KW, "trends-regroup-%s.csv" % DATE)


def cmd_trends_regroup():
    """Re-pull head terms that came out "too small" in their first group, grouped with terms of similar
    Google Ads volume so that no one term flattens the others."""
    if os.path.exists(REGROUP):
        raise SystemExit("regroup file exists; run trends-run to finish it")
    base = len(trend_groups())
    small = [r["keyword"] for r in read(os.path.join(KW, "trends-%s.csv" % DATE)) if r["direction"] == "too small"]
    ads = {r["keyword"]: int(r["ads_volume"] or 0) for r in read(os.path.join(KW, "ads-volumes-%s.csv" % DATE))}
    small.sort(key=lambda k: -ads.get(k, 0))
    rows = [{"group": base + 1 + i // 5, "keywords": " | ".join(small[i:i + 5])} for i in range(0, len(small), 5)]
    write(REGROUP, ["group", "keywords"], rows)
    print("regroup: %d keywords in %d groups" % (len(small), len(rows)))
    cmd_trends_run()


def trends_task(group):
    return [{"keywords": group, "location_code": 2840, "language_code": "en", "date_from": "2021-10-01",
             "date_to": "2026-10-01", "type": "web"}]


def run_trend(c, n, group):
    res = None
    for attempt in (1, 2):
        res = c.post(TRENDS_EP, trends_task(group))
        st = (res.get("tasks") or [{}])[0].get("status_code")
        cost = float(res.get("cost") or 0)
        log_spend("trends", cost, "group %d attempt %d status %s" % (n, attempt, st))
        note = "phase4 trends group %d; %s; $%.4f" % (n, "ok" if st == 20000 else "status %s" % st, cost)
        index_row(res["_id"], "dataforseo", TRENDS_EP, " | ".join(group), "2840", res["_file"], note)
        if st == 50000 and attempt == 1:
            time.sleep(5)
            continue
        print("group %d status %s cost $%.4f" % (n, st, cost))
        return res
    return res


def cmd_trends_probe():
    g = trend_groups()
    c = client()
    run_trend(c, 1, g[0])


def cmd_trends_run():
    groups = trend_groups()
    done = {int(r["note"].split("group ")[1].split(";")[0]) for r in read_index()
            if r["endpoint"] == TRENDS_EP and "; ok;" in r["note"]}
    c = client()
    for n, g in enumerate(groups, 1):
        if n in done:
            continue
        run_trend(c, n, g)


def cmd_trends_distil():
    groups = trend_groups()
    files = {}
    for r in read_index():
        if r["endpoint"] == TRENDS_EP and "; ok;" in r["note"]:
            files[int(r["note"].split("group ")[1].split(";")[0])] = r["file"]
    head_units = {}
    for u in units():
        head_units.setdefault(u["head_term_1"], []).append(u["unit_id"])
    out, grp_rows = [], []
    for n, g in enumerate(groups, 1):
        grp_rows.append({"group": n, "keywords": " | ".join(g), "raw": files.get(n, "")})
        if n not in files:
            for k in g:
                out.append({"keyword": k, "unit_id": ";".join(head_units[k]), "group": n, "note": "no data (task failed)"})
            continue
        with open(os.path.join(SEO, files[n]), encoding="utf-8") as fh:
            res = json.load(fh)
        result = ((res["tasks"][0].get("result") or [{}])[0]) or {}
        graph = next((it for it in (result.get("items") or []) if it.get("type") == "google_trends_graph"), None)
        series = {k: [] for k in g}
        months = []
        if graph:
            kws = [k.lower() for k in (graph.get("keywords") or g)]
            for pt in graph.get("data") or []:
                if pt.get("missing_data"):
                    continue
                months.append(pt.get("date_from", "")[:7])
                for i, v in enumerate(pt.get("values") or []):
                    if i < len(kws) and kws[i] in series:
                        series[kws[i]].append((pt.get("date_from", "")[:7], v if v is not None else 0))
        for k in g:
            pts = series.get(k) or []
            if not pts:
                out.append({"keyword": k, "unit_id": ";".join(head_units[k]), "group": n, "note": "no data"})
                continue
            first = [v for d, v in pts if "2021-10" <= d <= "2022-09"]
            last = [v for d, v in pts if "2025-10" <= d <= "2026-09"]
            a = sum(first) / len(first) if first else 0
            b = sum(last) / len(last) if last else 0
            t5 = "%.2f" % (b / a) if a > 0 else ""
            direction = ""
            note = "group %d (values relative within the group only)" % n
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
            # same window as the Google Ads slope_12m (Jun-Aug 2026 over Sep-Nov 2025)
            w1 = [v for d, v in pts if "2025-09" <= d <= "2025-11"]
            w2 = [v for d, v in pts if "2026-06" <= d <= "2026-08"]
            m1 = sum(w1) / len(w1) if w1 else 0
            m2 = sum(w2) / len(w2) if w2 else 0
            t12 = "%.2f" % (m2 / m1) if m1 >= 1 else ""
            out.append({"keyword": k, "unit_id": ";".join(head_units[k]), "avg_first_year": "%.1f" % a,
                        "avg_last_year": "%.1f" % b, "trend_5y": t5, "direction": direction, "peak_month": peak,
                        "trends_12m": t12, "group": n, "note": note})
    best = {}
    for r in out:
        k = r["keyword"]
        if k not in best or (best[k].get("direction") in ("too small", "", None)
                             and r.get("direction") not in ("too small", "", None)):
            if k in best:
                r["note"] = r["note"] + "; re-pulled (first group %s was too small to read)" % best[k]["group"]
            best[k] = r
    out = [best[k] for k in dict.fromkeys(r["keyword"] for r in out)]
    write(os.path.join(KW, "trends-%s.csv" % DATE),
          ["keyword", "unit_id", "avg_first_year", "avg_last_year", "trend_5y", "direction", "peak_month", "trends_12m",
           "group", "note"], out)
    write(os.path.join(KW, "trends-groups-%s.csv" % DATE), ["group", "keywords", "raw"], grp_rows)
    print("trends rows %d" % len(out))


if __name__ == "__main__":
    cmds = {"ads-list": cmd_ads_list, "ads-post": cmd_ads_post, "ads-collect": cmd_ads_collect,
            "serp-post": cmd_serp_post, "serp-collect": cmd_serp_collect, "trends-probe": cmd_trends_probe,
            "trends-run": cmd_trends_run, "trends-distil": cmd_trends_distil,
            "trends-regroup": cmd_trends_regroup}
    if len(sys.argv) < 2 or sys.argv[1] not in cmds:
        print(__doc__)
        sys.exit(1)
    cmds[sys.argv[1]]()
