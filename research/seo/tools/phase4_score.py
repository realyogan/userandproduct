#!/usr/bin/env python3
"""Phase 4 scoring: one row per unit in keywords/topic-scores-<date>.csv (free, local).

Standard library only. Reads distilled CSVs only:
  keywords/phase4-units-<date>.csv, keywords/ads-volumes-<date>.csv, keywords/trends-<date>.csv,
  serps/features-<date>.csv, serps/page-one-<date>.csv, keywords/topic-candidates-v2-<date>.csv,
  keywords/section-candidates-<date>.csv, competitors/*-competitors.csv, competitors/traffic-<date>.csv
  and the unit keyword sets from phase4_units.load_units().

Usage (from the project root):
    python research/seo/tools/phase4_score.py          # v1: keywords/topic-scores-<date>.csv
    python research/seo/tools/phase4_score.py v1.1     # v1.1: phase4-units-v1.1, topic-candidates-v1.1 ->
                                                       # keywords/topic-scores-v1.1-<date>.csv,
                                                       # keywords/topic-arena-v1.1-<date>.csv and
                                                       # keywords/topic-evidence-v1.1-<date>.csv
    python research/seo/tools/phase4_score.py v1.2     # v1.2: phase4-units-v1.2-2026-10-09 (tools/phase4c.py) ->
                                                       # keywords/topic-scores-v1.2-2026-10-09.csv,
                                                       # topic-arena-v1.2-2026-10-09.csv, topic-evidence-v1.2-2026-10-09.csv
Same formula for v1 and v1.1. Units without a Google Ads row (the v1.1 new units) keep ads_volume_head empty; the
score never used it (demand is the Labs adjusted volume).

v1.2 formula (9 Oct 2026; same units, keywords, SERPs and Trends as v1.1; intent from tools/phase4c.py):
  score (0-100) = 25*demand + 20*difficulty + 15*intent + 10*weak + 10*ai_overview + 10*trend + 10*competitors
  demand     = ranked percentile of adjusted_volume_field: the variant-adjusted volume of the surviving phrases
               (field fit yes at full weight, partial at half; fine intent not career, brand or dictionary; source
               label not navigational). adjusted_volume (v1.1) and adjusted_volume_practitioner stay as columns.
  difficulty = ranked percentile of median_difficulty, inverted; a median KD of 0 means "no difficulty figure"
               (Labs gives KD 0 when it has none) and gets the neutral 0.5 for every unit, as books already did.
               This fixes the v1.1 UX writing artifact (missing KD read as the easiest possible topic).
  intent     = ranked percentile of practitioner_share (learn + compare + template + tool + question) over the
               same surviving phrases; replaces v1.1's decision_template component.
  weak (soft shelf), ai_overview (answer box), trend and competitors: unchanged from v1.1.
"""
import csv
import glob
import os
import re
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cluster_phase1 import DECISION, tokens  # noqa: E402
from cluster_v2 import QUESTION, TEMPLATE  # noqa: E402
from phase4_units import load_units  # noqa: E402
from phase4b import series_for  # noqa: E402

SEO = os.path.dirname(HERE)
DATE = "2026-10-08"

WEIGHTS = [("demand", 25), ("difficulty", 20), ("decision_template", 15), ("weak", 10), ("ai_overview", 10),
           ("trend", 10), ("competitors", 10)]

# Domain kinds that are not "competitors in the arena": forums, platforms, retailers and their kin.
NOT_ARENA = {"forum", "platform", "video", "retailer", "catalog", "encyclopedia", "dictionary", "government",
             "university", "app store", "other"}
# Types for domains not in the competitor CSVs (Phase 4 SERPs brought in many new ones). Anything not listed
# here and not caught by the suffix rules is a commercial or editorial site ("business") and counts.
TYPE_OVERRIDES = {
    "dictionary.cambridge.org": "dictionary", "collinsdictionary.com": "dictionary", "merriam-webster.com": "dictionary",
    "apps.apple.com": "app store", "play.google.com": "app store", "support.google.com": "platform",
    "stackoverflow.com": "forum", "softwareengineering.stackexchange.com": "forum", "graphicdesignforum.com": "forum",
    "dev.to": "platform", "hackernoon.com": "platform", "instagram.com": "platform", "trustpilot.com": "platform",
    "g2.com": "platform", "dribbble.com": "platform", "github.com": "platform", "facebook.com": "platform",
    "x.com": "platform", "twitter.com": "platform", "tiktok.com": "platform", "strandbooks.com": "retailer",
    "barnesandnoble.com": "retailer", "amazon.com": "retailer", "ebay.com": "retailer", "etsy.com": "retailer",
    "investopedia.com": "publication", "forbes.com": "publication", "techrepublic.com": "publication",
    "cio.com": "publication", "usnews.com": "publication", "uxmag.com": "publication", "ixdf.org": "education",
    "w3.org": "other", "wcag.com": "business", "yale-a11y.gitlab.io": "university", "edutechwiki.unige.ch": "university",
    "homepage.univie.ac.at": "university", "pmc.ncbi.nlm.nih.gov": "government",
    "researchmethodsresources.nih.gov": "government", "abs.gov.au": "government",
}
PLATFORM_SUFFIXES = ("medium.com", "pinterest.com", "substack.com", "wikipedia.org", "youtube.com", "reddit.com",
                     "quora.com", "linkedin.com", "github.io")


def read(path, comment=False):
    with open(path, encoding="utf-8", newline="") as fh:
        lines = [ln for ln in fh if not (comment and ln.startswith("#"))]
    return list(csv.DictReader(lines))


def domain_types():
    t = {}
    for f in glob.glob(os.path.join(SEO, "competitors", "*-competitors.csv")):
        for r in read(f):
            t.setdefault(r["domain"], r["type"])
    return t


KNOWN = None


def dtype(d):
    global KNOWN
    if KNOWN is None:
        KNOWN = domain_types()
    if d in KNOWN:
        return KNOWN[d]
    if d in TYPE_OVERRIDES:
        return TYPE_OVERRIDES[d]
    if any(d == s or d.endswith("." + s) for s in PLATFORM_SUFFIXES):
        return "platform"
    if d.endswith(".gov") or ".gov." in d or d.endswith(".mil"):
        return "government"
    if d.endswith(".edu") or ".edu." in d or ".ac." in d:
        return "university"
    return "business"


def pct_rank(values, higher_better=True):
    """Ranked percentile 0..1 (ties share the average rank); None stays None."""
    idx = [i for i, v in enumerate(values) if v is not None]
    order = sorted(idx, key=lambda i: values[i] if higher_better else -values[i])
    out = [None] * len(values)
    n = len(order)
    i = 0
    while i < n:
        j = i
        while j + 1 < n and values[order[j + 1]] == values[order[i]]:
            j += 1
        r = (i + j) / 2.0
        for k in range(i, j + 1):
            out[order[k]] = r / (n - 1) if n > 1 else 0.5
        i = j + 1
    return out


def fnum(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


OUT_DATE = {"v1.2": "2026-10-09"}
WEIGHTS_V12 = [("demand", 25), ("difficulty", 20), ("intent", 15), ("weak", 10), ("ai_overview", 10),
               ("trend", 10), ("competitors", 10)]
INTENT_COLS = ["adjusted_volume_practitioner", "adjusted_volume_field", "median_difficulty_known", "intent_mix",
               "practitioner_share", "field_share", "dictionary_share", "career_share", "navigational_share",
               "offfield_share", "meaning_loss", "article_capacity", "capacity_label", "articles_estimate", "parked",
               "park_reason", "format_suggestion", "section_hint", "what_this_is", "practical_groups"]


def vname(stem, version):
    if version == "v1":
        return "%s-%s.csv" % (stem, DATE)
    return "%s-%s-%s.csv" % (stem, version, OUT_DATE.get(version, DATE))


def main():
    version = sys.argv[1] if len(sys.argv) > 1 else "v1"
    kd = os.path.join(SEO, "keywords")
    units = read(os.path.join(kd, vname("phase4-units", version)))
    v12 = version == "v1.2"
    base = "v1.1" if v12 else version  # v1.2 keeps the v1.1 units, keyword sets and candidate files
    weights = WEIGHTS_V12 if v12 else WEIGHTS
    full = {u["unit_id"]: u for u in load_units(version="v2" if version == "v1" else base)[0]}
    ads = {r["keyword"]: r for r in read(os.path.join(kd, "ads-volumes-%s.csv" % DATE))}
    trends = {r["keyword"]: r for r in read(os.path.join(kd, "trends-%s.csv" % DATE))}
    feats = {r["keyword"]: r for r in read(os.path.join(SEO, "serps", "features-%s.csv" % DATE))}
    page_one = {}
    for r in read(os.path.join(SEO, "serps", "page-one-%s.csv" % DATE)):
        page_one.setdefault(r["keyword"], []).append(r)
    v2 = {(r["topic"], r["subtopic"]): r for r in read(os.path.join(
        kd, "topic-candidates-%s-%s.csv" % ("v2" if version == "v1" else base, DATE)))}
    sc = {(r["section"], r["category"]): r for r in read(os.path.join(kd, "section-candidates-%s.csv" % DATE))}

    rows = []
    for u in units:
        fu = full[u["unit_id"]]
        kws = fu["rows"]
        n = len(kws) or 1
        dec = sum(1 for r in kws if set(tokens(r["keyword"])) & set(DECISION) or "versus" in r["keyword"])
        if u["kind"] == "section":
            src = sc[(u["topic"], u["subtopic_or_category"])]
            tshare, qshare = src["template_share"], src["question_share"]
            comp_articles = ""
        else:
            src = v2[(u["topic"], u["subtopic_or_category"])]
            tshare, qshare = src["template_share"], src["question_share"]
            comp_articles = src["competitor_articles"]
        slopes = [float(r["slope_12m"]) for r in kws if r["slope_12m"]]
        h1, h2 = u["head_term_1"], u["head_term_2"]
        f = feats.get(h1, {})
        tr = trends.get(h1, {})
        p1 = sorted(page_one.get(h1, []), key=lambda r: int(r["position"]))
        arena = []
        for h in (h1, h2):
            for r in page_one.get(h, []):
                if dtype(r["domain"]) not in NOT_ARENA and r["domain"] not in arena:
                    arena.append(r["domain"])
        weak = f.get("weak_count", "")
        kd_val = fnum(u["median_difficulty"])
        if (u["section_or_domain"] == "books" or v12) and kd_val == 0:
            kd_val = None  # KD 0 means no data (books only until v1.1; every unit from v1.2)
        rows.append({
            "unit_id": u["unit_id"], "kind": u["kind"], "section_or_domain": u["section_or_domain"],
            "topic": u["topic"], "subtopic_or_category": u["subtopic_or_category"], "head_term_1": h1,
            "keyword_count": u["keyword_count"], "adjusted_volume": u["adjusted_volume"],
            "ads_volume_head": ads.get(h1, {}).get("ads_volume", ""),
            "median_difficulty": "" if kd_val is None else u["median_difficulty"],
            "decision_share": "%.2f" % (dec / n), "template_share": tshare, "question_share": qshare,
            "slope_12m": ("%.2f" % statistics.median(slopes)) if slopes else "",
            "trend_5y": tr.get("trend_5y", ""), "direction": tr.get("direction", ""),
            "ai_overview": f.get("ai_overview", ""), "ai_overview_empty": f.get("ai_overview_empty", ""),
            "weak_count": weak, "weak_page_one": ("yes" if int(weak) >= 3 else "no") if weak != "" else "",
            "page_one_domains": ";".join(r["domain"] for r in p1[:10]),
            "competitor_count_in_arena": len(arena) if p1 else "",
            "competitor_articles": comp_articles, "owner_fit": "",
            "_arena": arena, "_kd": kd_val, "_rows": kws, "_p1": p1, "_src": src,
        })
        if v12:
            rows[-1].update({k: u[k] for k in INTENT_COLS})

    # components (0..1), then weights
    demand = pct_rank([float(r["adjusted_volume_field" if v12 else "adjusted_volume"]) for r in rows])
    intent = pct_rank([float(r["practitioner_share"]) for r in rows]) if v12 else None
    diff = pct_rank([r["_kd"] for r in rows], higher_better=False)
    dt = pct_rank([float(r["decision_share"]) + float(r["template_share"]) for r in rows])
    weak = pct_rank([fnum(r["weak_count"]) for r in rows])
    comp = pct_rank([fnum(r["competitor_count_in_arena"]) for r in rows], higher_better=False)
    for i, r in enumerate(rows):
        ao = 0.5 if r["ai_overview"] == "" else (1.0 if r["ai_overview"] == "no" or r["ai_overview_empty"] == "yes"
                                                 else 0.0)
        trend = {"rising": 1.0, "flat": 0.5, "falling": 0.0}.get(r["direction"], 0.5)
        parts = {"demand": demand[i], "difficulty": diff[i] if diff[i] is not None else 0.5,
                 "decision_template": dt[i], "weak": weak[i] if weak[i] is not None else 0.5, "ai_overview": ao,
                 "trend": trend, "competitors": comp[i] if comp[i] is not None else 0.5}
        if v12:
            parts["intent"] = intent[i]
        r["score"] = "%.1f" % sum(parts[k] * w for k, w in weights)
        for k, _ in weights:
            r["c_" + k] = "%.2f" % parts[k]

    cols = ["unit_id", "kind", "section_or_domain", "topic", "subtopic_or_category", "head_term_1", "keyword_count",
            "adjusted_volume", "ads_volume_head", "median_difficulty", "decision_share", "template_share",
            "question_share", "slope_12m", "trend_5y", "direction", "ai_overview", "ai_overview_empty", "weak_count",
            "weak_page_one", "page_one_domains", "competitor_count_in_arena", "competitor_articles", "owner_fit",
            "score"] + ["c_" + k for k, _ in weights]
    if v12:
        cols[cols.index("adjusted_volume") + 1:cols.index("adjusted_volume") + 1] = [
            "adjusted_volume_practitioner", "adjusted_volume_field"]
        cols[cols.index("median_difficulty") + 1:cols.index("median_difficulty") + 1] = ["median_difficulty_known"]
        cols[cols.index("question_share") + 1:cols.index("question_share") + 1] = [
            "intent_mix", "practitioner_share", "field_share", "dictionary_share", "career_share",
            "navigational_share", "offfield_share", "meaning_loss", "article_capacity", "capacity_label",
            "articles_estimate", "parked", "park_reason", "format_suggestion", "section_hint", "what_this_is",
            "practical_groups"]
    header = [
        "# Phase 4 topic scores%s, 8 Oct 2026. One row per unit (topic, sub-topic or section category)."
        % ("" if version == "v1" else " (%s)" % version),
        "# score (0-100) = 25*demand + 20*difficulty + 15*decision_template + 10*weak + 10*ai_overview + 10*trend"
        " + 10*competitors, each component 0..1:",
        "#   demand = ranked percentile of adjusted_volume (higher is better)",
        "#   difficulty = ranked percentile of median_difficulty, inverted (lower KD is better); book units have no"
        " KD data and get 0.5",
        "#   decision_template = ranked percentile of decision_share + template_share",
        "#   weak = ranked percentile of weak_count on head_term_1's page one (more weak results is better)",
        "#   ai_overview = 1 when head_term_1's SERP has no AI Overview or an empty one, else 0",
        "#   trend = 1 rising, 0.5 flat or too small to read, 0 falling (Google Trends, 5 years, head_term_1)",
        "#   competitors = ranked percentile of competitor_count_in_arena, inverted (fewer is better)",
        "# Ranked percentile: (rank - 1) / (n - 1) over all %d units, ties share the average rank." % len(rows),
        "# owner_fit (1-3) is left empty for the owner and is NOT part of the score. c_* columns are the components.",
        "# competitor_count_in_arena: distinct page-one domains for head_term_1 and head_term_2 (where a SERP exists),"
        " excluding forums, platforms, video, retailers, catalogs, encyclopedias, dictionaries, government,"
        " universities and app stores (types from competitors/*-competitors.csv, else tools/phase4_score.py rules).",
    ]
    if v12:
        header = [
            "# Phase 4c topic scores (v1.2), 9 Oct 2026. One row per unit (topic, sub-topic or section category);"
            " same units, SERPs and Trends as v1.1.",
            "# score (0-100) = 25*demand + 20*difficulty + 15*intent + 10*weak + 10*ai_overview + 10*trend"
            " + 10*competitors, each component 0..1:",
            "#   demand = ranked percentile of adjusted_volume_field: the variant-adjusted volume of the phrases that"
            " survive: field fit yes (full weight) or partial (half weight), fine intent not career, brand or"
            " dictionary, source label not navigational (field fit from keywords/field-fit-review-2026-10-09.csv, else"
            " the rule in tools/harvest.py). adjusted_volume (v1.1) and adjusted_volume_practitioner (career, brand and"
            " navigational removed only) are kept for comparison",
            "#   difficulty = ranked percentile of median_difficulty, inverted (lower KD is better); a median KD of 0"
            " means no difficulty figure and gets 0.5 for every unit (median_difficulty is left empty there)",
            "#   intent = ranked percentile of practitioner_share (learn + compare + template + tool + question) over"
            " the same surviving phrases, weighted by volume times field fit",
            "#   weak = ranked percentile of weak_count on head_term_1's page one (the soft shelf: more weak results"
            " is better)",
            "#   ai_overview = 1 when head_term_1's SERP has no AI Overview or an empty one, else 0 (the answer box)",
            "#   trend = 1 rising, 0.5 flat or too small to read, 0 falling (Google Trends, 5 years, head_term_1)",
            "#   competitors = ranked percentile of competitor_count_in_arena, inverted (fewer is better)",
        ] + header[9:]
    rows.sort(key=lambda r: -float(r["score"]))
    path = os.path.join(kd, vname("topic-scores", version))
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write("\n".join(header) + "\n")
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    # arena detail for the tree document
    tiers = {r["domain"]: r for r in read(os.path.join(SEO, "competitors", "traffic-%s.csv" % DATE))}
    det = []
    for r in rows:
        for d in r["_arena"]:
            t = tiers.get(d, {})
            det.append({"unit_id": r["unit_id"], "domain": d, "type": dtype(d), "tier": t.get("tier", ""),
                        "organic_etv": t.get("organic_etv", "")})
    with open(os.path.join(kd, vname("topic-arena", version)), "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["unit_id", "domain", "type", "tier", "organic_etv"])
        w.writeheader()
        w.writerows(det)
    if version != "v1":
        write_evidence(rows, trends, tiers, os.path.join(kd, vname("topic-evidence", version)), v12)
    print("units scored: %d -> %s" % (len(rows), path))
    for r in rows[:15]:
        print("%s %-6s %-42s %-40s adj %7s kd %4s score %s" % (r["unit_id"], r["kind"][:6],
              (r["subtopic_or_category"] or r["topic"])[:42], r["head_term_1"][:40],
              r.get("adjusted_volume_field", r["adjusted_volume"]), r["median_difficulty"], r["score"]))


QWORDS = {"how", "what", "why", "which", "should"}
TPL = re.compile(r"\b(templates?|examples?|checklists?)\b")


def write_evidence(rows, trends, tiers, path, v12=False):
    """One row per unit with the keyword and page-one evidence behind its score (for the explainer)."""
    groups = {r["group"]: r for r in read(os.path.join(SEO, "keywords", "trends-groups-%s.csv" % DATE))}
    cache = {}
    out = []
    for r in rows:
        kws = sorted((k for k in r["_rows"] if not k.get("flag_v1_1", k["flag"])), key=lambda k: (-int(k["volume"] or 0), k["keyword"]))
        top = ["%s (%s, %s)" % (k["keyword"], k["volume"], k["difficulty"] if k["difficulty"] != "" else "n/a")
               for k in kws[:8]]
        qs = [k["keyword"] for k in kws if (tokens(k["keyword"]) or [""])[0] in QWORDS][:3]
        tp = [k["keyword"] for k in kws if TPL.search(k["keyword"])][:3]
        doms = []
        for p in r["_p1"][:10]:
            t = tiers.get(p["domain"], {}).get("tier", "")
            doms.append("%s (%s)" % (p["domain"], t) if t else p["domain"])
        tr = trends.get(r["head_term_1"], {})
        series = ""
        g = tr.get("group", "")
        if g and g in groups and groups[g].get("raw"):
            key = (g, groups[g]["raw"])
            if key not in cache:
                cache[key] = series_for(groups[g]["raw"], groups[g]["keywords"].split(" | "))
            pts = cache[key].get(r["head_term_1"]) or []
            series = ";".join(str(v) for _, v in pts)
        out.append({"unit_id": r["unit_id"], "topic": r["topic"], "subtopic_or_category": r["subtopic_or_category"],
                    "score": r["score"], "keyword_count": r["keyword_count"],
                    "adjusted_volume": r["adjusted_volume"], "median_difficulty": r["median_difficulty"],
                    "top_keywords_with_volume_kd": "; ".join(top), "question_examples": "; ".join(qs),
                    "template_examples": "; ".join(tp), "page_one_domains_with_tier": "; ".join(doms),
                    "trend_5y": r["trend_5y"], "direction": r["direction"], "trend_series": series,
                    "ai_overview": r["ai_overview"], "ai_overview_empty": r["ai_overview_empty"],
                    "weak_count": r["weak_count"], "competitor_count_in_arena": r["competitor_count_in_arena"],
                    "competitor_articles": r["competitor_articles"],
                    "competitor_domains": r["_src"].get("competitor_domains", "")})
        if v12:
            out[-1].update({k: r[k] for k in INTENT_COLS if k != "median_difficulty_known"})
    cols = ["unit_id", "topic", "subtopic_or_category", "score", "keyword_count", "adjusted_volume",
            "median_difficulty", "top_keywords_with_volume_kd", "question_examples", "template_examples",
            "page_one_domains_with_tier", "trend_5y", "direction", "trend_series", "ai_overview", "ai_overview_empty",
            "weak_count", "competitor_count_in_arena", "competitor_articles", "competitor_domains"]
    if v12:
        cols += [k for k in INTENT_COLS if k != "median_difficulty_known"]
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(out)
    print("evidence rows: %d -> %s" % (len(out), path))


if __name__ == "__main__":
    main()
