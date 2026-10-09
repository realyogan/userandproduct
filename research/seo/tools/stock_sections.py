#!/usr/bin/env python3
"""Phase 3c stock evidence for the Links, Books and Templates sections, from the free inventories (local).

Standard library only. Usage (from the project root):
    python research/seo/tools/stock_sections.py [--date 2026-10-08]

Inputs:  competitors/inventory-links-github-sections.csv (heading,list_count,entry_count)
         competitors/sitemaps/<domain>-sitemap-<date>.csv (domain,url,lastmod,first_segment,slug,slug_tokens,year,content)
Output:  competitors/stock-by-section-<date>.csv (section,source_domain_or_list,category_as_listed,entry_count)

Rows per source:
- "path /<segment>/": URLs in the sitemap under that first path segment (content and non-content);
  segments holding a single URL are summed into one "other segments" row per domain.
- "category page: <slug>" (links directories): a category or list page named in the sitemap; the sitemap
  does not say how many entries it holds, so entry_count is empty. startupstash.com lists 200 categories;
  only those whose slug holds a product, design or research word (STASH_KEEP) are kept.
- "lists mentioning '<word>'" (books): book-list pages whose slug holds the word.
- "template pages, path /<segment>/" and "template pages mentioning '<word>'" (templates): URLs containing
  "template", by first path segment and by topic word in the URL.
"""
import argparse
import collections
import csv
import os
import re
import urllib.parse

SEO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COMP = os.path.join(SEO, "competitors")
LINK_DOMAINS = ["bookmarks.design", "uxtools.co", "toools.design", "designresourc.es", "startupstash.com"]
BOOK_DOMAINS = ["fivebooks.com", "mostrecommendedbooks.com", "lennysnewsletter.com"]
TEMPLATE_DOMAINS = ["aha.io", "productboard.com", "maze.co", "dovetail.com", "nngroup.com", "mural.co"]
CATEGORY_SEGMENTS = {"categories", "category", "list"}
STASH_KEEP = re.compile(r"design|product|ux|ui|prototyp|wirefram|roadmap|research|survey|feedback|analytic|"
                        r"test|user|customer|collaborat|whiteboard|mockup|icon|font|color|stock|no-code|ab-")
BOOK_WORDS = ["design", "ux", "user-experience", "product", "management", "business", "startup", "leadership",
              "psychology", "marketing", "entrepreneur", "innovation", "strategy", "negotiation", "data",
              "statistics", "habit", "behavioral", "economics", "productivity"]
TEMPLATE_WORDS = ["roadmap", "persona", "journey", "user-story", "story-map", "prd", "requirement", "spec-", "okr",
                  "retro", "research", "interview", "usability", "survey", "competitive", "swot", "canvas",
                  "brainstorm", "workshop", "strategy", "sprint", "kanban", "empathy", "flow", "launch",
                  "prioriti", "feedback", "discovery", "go-to-market", "stakeholder"]


def read(path):
    with open(path, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def sitemap(d, date):
    return read(os.path.join(COMP, "sitemaps", "%s-sitemap-%s.csv" % (d, date)))


def seg_rows(section, d, rows, prefix="path"):
    c = collections.Counter(r["first_segment"] or "(home)" for r in rows)
    out = [(section, d, "%s /%s/" % (prefix, s), n) for s, n in c.most_common() if n > 1]
    singles = sum(1 for n in c.values() if n == 1)
    if singles:
        out.append((section, d, "%s: %d other segments with one URL each" % (prefix, singles), singles))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default="2026-10-08")
    args = ap.parse_args()
    out = []
    for r in read(os.path.join(COMP, "inventory-links-github-sections.csv")):
        out.append(("links", "github awesome lists (inventory-links-github-sections.csv)", r["heading"],
                    int(r["entry_count"])))
    for d in LINK_DOMAINS:
        rows = sitemap(d, args.date)
        out.extend(seg_rows("links", d, rows))
        for r in rows:
            parts = [p for p in re.sub(r"^https?://[^/]+", "", r["url"]).split("/") if p]
            if len(parts) >= 2 and parts[0] in CATEGORY_SEGMENTS:
                if d == "startupstash.com" and not STASH_KEEP.search(parts[1]):
                    continue
                out.append(("links", d, "category page: %s" % urllib.parse.unquote(parts[1]), ""))
    for d in BOOK_DOMAINS:
        rows = sitemap(d, args.date)
        out.extend(seg_rows("books", d, rows))
        if d == "lennysnewsletter.com":
            n = sum(1 for r in rows if "book" in r["url"].lower())
            out.append(("books", d, "posts mentioning 'book'", n))
            continue
        lists = [r for r in rows if r["first_segment"] in ("best-books", "lists")]
        for w in BOOK_WORDS:
            n = sum(1 for r in lists if re.search(r"(?<![a-z])%s(?![a-z])" % re.escape(w), r["url"].lower()))
            if n:
                out.append(("books", d, "lists mentioning '%s'" % w, n))
    for d in TEMPLATE_DOMAINS:
        rows = [r for r in sitemap(d, args.date) if "template" in r["url"].lower()]
        out.extend(seg_rows("templates", d, rows, "template pages, path"))
        for w in TEMPLATE_WORDS:
            n = sum(1 for r in rows if w in r["url"].lower())
            if n:
                out.append(("templates", d, "template pages mentioning '%s'" % w, n))
    path = os.path.join(COMP, "stock-by-section-%s.csv" % args.date)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["section", "source_domain_or_list", "category_as_listed", "entry_count"])
        w.writerows(out)
    print("%d rows -> %s" % (len(out), path))


if __name__ == "__main__":
    main()
