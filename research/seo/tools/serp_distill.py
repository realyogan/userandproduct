"""Distill saved Google organic SERP responses into two consolidated CSVs.

Reads every raw SERP response (task_get/advanced, default response shape:
{"id", "status_code", "status_message", "items": [...]}) in a raw folder,
skipping files whose name starts with "_". Each file name is a keyword slug
(keyword lowercased, non-alphanumerics collapsed to single hyphens, trimmed);
the slug is mapped back to keyword and section through one or more queries
CSVs (columns: section,keyword and optionally phase). The first file that
names a slug wins; a row whose phase differs from the file's own phase (a
Phase 4 head term reusing a Phase 0 pull) is skipped there. Default queries:
serps/phase0-queries-<date>.csv (phase0) and serps/phase4-queries-<date>.csv
(phase4, when present).

Rebuilds from scratch:
  page-one CSV:  date,section,keyword,position,type,domain,url,title,timestamp,phase
                 (organic results only; position = rank_group)
  features CSV:  date,section,keyword,task_id,ai_overview,ai_overview_empty,
                 featured_snippet,people_also_ask,video,images,popular_products,
                 knowledge_graph,related_searches,organic_count,weak_count,
                 weak_domains,ai_overview_ref_domains,phase

Rules:
  - domain is stored without a leading "www."
  - weak domains: medium.com and subdomains, uxdesign.cc, uxplanet.org,
    productcoalition.com, bootcamp.uxdesign.cc, quora.com, reddit.com,
    linkedin.com, pinterest.com and subdomains, youtube.com, scribd.com;
    plus any URL containing "/glossary/" or "/blog/" on productplan.com,
    productboard.com, aha.io, userpilot.com, hotjar.com, pendo.io,
    amplitude.com, mixpanel.com, maze.co, dovetail.com
  - ai_overview_empty = yes when the ai_overview item has no text, markdown
    or references (the asynchronous placeholder)
  - popular_products = yes when an item of type popular_products is present
  - video = yes when a video or short_videos item is present

Usage (from the project root):
  python research/seo/tools/serp_distill.py
  python research/seo/tools/serp_distill.py --raw <dir> --queries <csv> [--queries <csv>] \
      --page-one <csv> --features <csv> --date 2026-10-08

Standard library only.
"""

import argparse
import csv
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
DATE = "2026-10-08"
DEFAULTS = {
    "raw": os.path.join(ROOT, "research", "seo", "cache", "raw", "serps-" + DATE),
    "queries": [os.path.join(ROOT, "research", "seo", "serps", "phase0-queries-" + DATE + ".csv"),
                os.path.join(ROOT, "research", "seo", "serps", "phase4-queries-" + DATE + ".csv")],
    "page_one": os.path.join(ROOT, "research", "seo", "serps", "page-one-" + DATE + ".csv"),
    "features": os.path.join(ROOT, "research", "seo", "serps", "features-" + DATE + ".csv"),
}

WEAK_EXACT = {
    "uxdesign.cc", "uxplanet.org", "productcoalition.com", "bootcamp.uxdesign.cc",
    "quora.com", "reddit.com", "linkedin.com", "youtube.com", "scribd.com",
}
WEAK_WITH_SUBDOMAINS = ("medium.com", "pinterest.com")
SAAS_BLOGS = (
    "productplan.com", "productboard.com", "aha.io", "userpilot.com", "hotjar.com",
    "pendo.io", "amplitude.com", "mixpanel.com", "maze.co", "dovetail.com",
)

PAGE_ONE_COLS = ["date", "section", "keyword", "position", "type", "domain", "url", "title", "timestamp", "phase"]
FEATURE_COLS = [
    "date", "section", "keyword", "task_id", "ai_overview", "ai_overview_empty",
    "featured_snippet", "people_also_ask", "video", "images", "popular_products",
    "knowledge_graph", "related_searches", "organic_count", "weak_count",
    "weak_domains", "ai_overview_ref_domains", "phase",
]


def slugify(keyword):
    return re.sub(r"[^a-z0-9]+", "-", keyword.lower()).strip("-")


def strip_www(domain):
    domain = (domain or "").strip().lower()
    return domain[4:] if domain.startswith("www.") else domain


def on_domain(domain, base):
    return domain == base or domain.endswith("." + base)


def is_weak(domain, url):
    if domain in WEAK_EXACT:
        return True
    if any(on_domain(domain, base) for base in WEAK_WITH_SUBDOMAINS):
        return True
    if any(on_domain(domain, base) for base in SAAS_BLOGS):
        path = (url or "").lower()
        if "/glossary/" in path or "/blog/" in path:
            return True
    return False


def yn(flag):
    return "yes" if flag else "no"


def ai_refs(item):
    """Reference domains of an ai_overview item, in order, de-duplicated."""
    seen = []
    refs = list(item.get("references") or [])
    for element in item.get("items") or []:
        refs.extend(element.get("references") or [])
    for ref in refs:
        d = strip_www(ref.get("domain"))
        if d and d not in seen:
            seen.append(d)
    return seen


def ai_is_empty(item):
    if item.get("text") or item.get("markdown") or item.get("references"):
        return False
    for element in item.get("items") or []:
        if element.get("text") or element.get("markdown") or element.get("references"):
            return False
    return True


def load_queries(paths):
    mapping = {}
    for path in paths:
        if not os.path.exists(path):
            continue
        m = re.search(r"(phase\d+)", os.path.basename(path))
        file_phase = m.group(1) if m else ""
        with open(path, encoding="utf-8", newline="") as fh:
            for row in csv.DictReader(fh):
                phase = row.get("phase") or file_phase
                if phase != file_phase:
                    continue  # reuses another phase's pull; that file maps it
                mapping.setdefault(slugify(row["keyword"]), (row["section"], row["keyword"], phase))
    return mapping, list(mapping)


def distill(data, section, keyword, date, phase=""):
    items = data.get("items") or []
    types = {i.get("type") for i in items}
    page_one = []
    weak = []
    for i in items:
        if i.get("type") != "organic":
            continue
        domain = strip_www(i.get("domain"))
        url = i.get("url") or ""
        page_one.append({
            "date": date, "section": section, "keyword": keyword,
            "position": i.get("rank_group"), "type": "organic", "domain": domain,
            "url": url, "title": i.get("title") or "", "timestamp": i.get("timestamp") or "",
            "phase": phase,
        })
        if is_weak(domain, url) and domain not in weak:
            weak.append(domain)
    weak_count = sum(1 for r in page_one if is_weak(r["domain"], r["url"]))
    ao = [i for i in items if i.get("type") == "ai_overview"]
    refs = []
    for item in ao:
        for d in ai_refs(item):
            if d not in refs:
                refs.append(d)
    features = {
        "date": date, "section": section, "keyword": keyword, "task_id": data.get("id", ""),
        "ai_overview": yn(ao),
        "ai_overview_empty": yn(ao and all(ai_is_empty(i) for i in ao)),
        "featured_snippet": yn("featured_snippet" in types),
        "people_also_ask": yn("people_also_ask" in types),
        "video": yn("video" in types or "short_videos" in types),
        "images": yn("images" in types),
        "popular_products": yn("popular_products" in types),
        "knowledge_graph": yn("knowledge_graph" in types),
        "related_searches": yn("related_searches" in types),
        "organic_count": len(page_one),
        "weak_count": weak_count,
        "weak_domains": ";".join(weak),
        "ai_overview_ref_domains": ";".join(refs),
        "phase": phase,
    }
    return page_one, features


def write_csv(path, cols, rows):
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--raw", default=DEFAULTS["raw"])
    p.add_argument("--queries", action="append", help="queries CSV (repeatable); default phase0 + phase4")
    p.add_argument("--page-one", default=DEFAULTS["page_one"])
    p.add_argument("--features", default=DEFAULTS["features"])
    p.add_argument("--date", default=DATE)
    args = p.parse_args(argv)

    mapping, order = load_queries(args.queries or DEFAULTS["queries"])
    files = sorted(f for f in os.listdir(args.raw) if f.endswith(".json") and not f.startswith("_"))
    found = {}
    unknown = []
    for f in files:
        slug = f[:-5]
        if slug in mapping:
            found[slug] = f
        else:
            unknown.append(f)

    all_rows, all_features = [], []
    for slug in order:  # queries-file order: section, then keyword
        if slug not in found:
            continue
        section, keyword, phase = mapping[slug]
        with open(os.path.join(args.raw, found[slug]), encoding="utf-8") as fh:
            data = json.load(fh)
        rows, feats = distill(data, section, keyword, args.date, phase)
        all_rows.extend(rows)
        all_features.append(feats)

    write_csv(args.page_one, PAGE_ONE_COLS, all_rows)
    write_csv(args.features, FEATURE_COLS, all_features)
    missing = [mapping[s][1] for s in order if s not in found]
    print("raw files read: %d" % len(found))
    print("page-one rows: %d -> %s" % (len(all_rows), args.page_one))
    print("features rows: %d -> %s" % (len(all_features), args.features))
    if missing:
        print("queries with no raw file: " + "; ".join(missing))
    if unknown:
        print("raw files not in queries: " + "; ".join(unknown))
    return 0


if __name__ == "__main__":
    sys.exit(main())
