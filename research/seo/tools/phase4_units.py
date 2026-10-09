#!/usr/bin/env python3
"""Phase 4 scoring units: load the keyword set behind every topic, sub-topic and section category.

Standard library only. Reads distilled CSVs, never raw JSON.

Units
- kind "topic": every topic row of keywords/topic-candidates-v2-<date>.csv (empty subtopic); its keywords
  are every keyword of keywords/keyword-to-topic-v2-<date>.csv with that topic.
- kind "subtopic": every sub-topic row of the same file; keywords with that topic and sub-topic.
- kind "section": every category of keywords/section-candidates-<date>.csv with keyword_count >= 10,
  except "(below threshold)" rows and categories dropped as off-scope (see DROP). Keywords are rebuilt with
  the rules of cluster_sections.py over keywords/harvest-sections-<date>.csv (unflagged, volume >= 100).
Keyword rows (volume, difficulty, monthly_12, slope_12m, flag) come from
keywords/harvest-articles-combined-<date>.csv (topics) and keywords/harvest-sections-<date>.csv (sections).

Usage (from the project root):
    python research/seo/tools/phase4_units.py candidates     # prints the top keywords per unit
    python research/seo/tools/phase4_units.py write          # writes keywords/phase4-units-<date>.csv
    python research/seo/tools/phase4_units.py candidates v1.1
    python research/seo/tools/phase4_units.py write v1.1     # writes keywords/phase4-units-v1.1-<date>.csv

Version v1.1 reads keywords/topic-candidates-v1.1-<date>.csv, keywords/keyword-to-topic-v1.1-<date>.csv and
keywords/harvest-articles-combined-v1.1-<date>.csv. Unit ids stay stable: a unit whose (topic, sub-topic or
category) already exists in keywords/phase4-units-<date>.csv keeps its id and head terms; new units get ids
from u85 upward in candidate-file order, with head terms from NEW_HEADS (keyed by "topic|subtopic").
"""
import collections
import csv
import os
import re
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cluster_sections import RULES  # noqa: E402

SEO = os.path.dirname(HERE)
KW = os.path.join(SEO, "keywords")
DATE = "2026-10-08"

# Section categories dropped as off-scope noise (other meanings of the seed phrase).
DROP_SECTION = {
    "book cover and layout design (off-scope)": "book-design meanings (covers, layout)",
    "interior, home and architecture design books (off-scope)": "off-scope design field (interior, architecture)",
    "fashion and craft design books (off-scope)": "off-scope design field (fashion, craft)",
    "engineering and software design books (off-scope)": "off-scope design field (engineering, software systems)",
    "rice purity test (off-scope)": "rice purity test",
    "rice university and sports scores (off-scope)": "Rice University sports and test scores",
}
# Topic or sub-topic units dropped as off-scope (none: the Phase 1b noise rules already removed Bible journeys,
# building systems, device accessibility and nursing prioritization before clustering).
DROP_TOPIC = {}

# Hand-picked head terms (unit key -> (head_term_1, head_term_2)). Chosen from the highest-volume unflagged
# keywords that read as the topic itself; filled after reading the "candidates" printout.
HEADS = {
    "u01": ("agile methodology", "agile project management"),
    "u02": ("agile methodology", "agile"),
    "u03": ("agile project management", "lean project management"),
    "u04": ("safe agile framework", ""),
    "u05": ("agile scrum", "kanban vs scrum"),
    "u06": ("agile manifesto", "agile principles"),
    "u07": ("accessibility", "web content accessibility"),
    "u08": ("accessibility", "accessibility definition"),
    "u09": ("accessibility 508", "accessibility standards"),
    "u10": ("web content accessibility", "accessibility heuristics"),
    "u11": ("accessibility checker", "accessibility tools"),
    "u12": ("analytics", "data analytics"),
    "u13": ("project management", "project management tools"),
    "u14": ("user testing", "ux research"),
    "u15": ("closed-ended questions in research", "customer feedback survey"),
    "u16": ("user interviews", "semi-structured interviews in qualitative research"),
    "u17": ("user testing", "usability testing"),
    "u18": ("ux research", "user research"),
    "u19": ("ui ux design", "ux design"),
    "u20": ("marketing funnel", "content marketing"),
    "u21": ("product management", "what is product management"),
    "u22": ("product management", "what is product management"),
    "u23": ("product life cycle", "product life cycle stages"),
    "u24": ("okr", "kpi examples"),
    "u25": ("okr", "okr vs kpi"),
    "u26": ("kpi examples", "kpi metrics"),
    "u27": ("design thinking", "design thinking process"),
    "u28": ("design thinking", "what is design thinking"),
    "u29": ("design thinking process", "design thinking framework"),
    "u30": ("pricing strategy", "dynamic pricing"),
    "u31": ("pricing strategy", "product pricing"),
    "u32": ("dynamic pricing", "competitive pricing"),
    "u33": ("amazon pricing strategy", "nike pricing strategy"),
    "u34": ("prioritization", "moscow prioritization"),
    "u35": ("prioritization", "prioritization definition"),
    "u36": ("moscow prioritization", "prioritization matrix"),
    "u37": ("task prioritization", "time management prioritization"),
    "u38": ("user stories", "user stories template"),
    "u39": ("user stories template", "user stories examples"),
    "u40": ("user stories", "story points"),
    "u41": ("acceptance criteria for user stories examples", "how to write acceptance criteria for user stories"),
    "u42": ("website design", "responsive design"),
    "u43": ("customer journey map", "user persona"),
    "u44": ("customer journey map", "user journey map"),
    "u45": ("user persona", "customer persona"),
    "u46": ("a/b testing", "a/b testing tools"),
    "u47": ("a/b testing", "what is a b testing"),
    "u48": ("a/b testing tools", "a/b testing software"),
    "u49": ("a/b testing landing pages", "email a/b testing"),
    "u50": ("design system", "material design"),
    "u51": ("breadcrumbs ui", "search bar ux"),
    "u52": ("design system", "material design"),
    "u53": ("product requirements document", "product requirements document template"),
    "u54": ("4 ps of marketing", "product marketing"),
    "u55": ("customer retention", "retention rate"),
    "u56": ("calculate retention rate", "customer retention rate formula"),
    "u57": ("retention rate", "engagement rate"),
    "u58": ("customer retention", "customer retention strategies"),
    "u59": ("product manager", "product owner vs product manager"),
    "u60": ("product owner", "product owner vs product manager"),
    "u61": ("product manager", "technical product manager"),
    "u62": ("change management", "stakeholder management"),
    "u63": ("change management", "leadership vs management"),
    "u64": ("stakeholder management", "stakeholder in project management"),
    "u65": ("product development", "product market fit"),
    "u66": ("product market fit", "product strategy"),
    "u67": ("product development", "product development process"),
    "u68": ("mvp minimum viable product", "product discovery"),
    "u69": ("product roadmap", "product roadmap examples"),
    "u70": ("information architecture", "what is information architecture"),
    "u71": ("ux design tools", "ux tools"),
    "u72": ("product management tools", "roadmap tools"),
    "u73": ("prototyping tools", "ai prototyping tools"),
    "u74": ("design books", "best books on design"),
    "u75": ("graphic design books", "best graphic design books"),
    "u76": ("product management books", "best product management books"),
    "u77": ("ux books", "best ux books"),
    "u78": ("user story template", "agile user story template"),
    "u79": ("agile user story template", "scrum user story template"),
    "u80": ("product roadmap template", "product roadmap powerpoint template"),
    "u81": ("sample size calculator", "sample size calculator formula"),
    "u82": ("power analysis sample size calculator", "g power sample size calculator"),
    "u83": ("sample size calculator for survey", ""),
    "u84": ("statistical sample size calculator", "sample size statistical significance calculator"),
}
# v1.1 new units (keyed by "topic|subtopic"; ids are assigned at load time).
NEW_HEADS = {
    "ai in product and design work|": ("ai for product managers", "ai tools for product managers"),
    "ai in product and design work|ai prototyping and design tools": ("ai powered design tools",
                                                                       "ai prototyping tools"),
    "ai in product and design work|ai in product and ux work (general)": ("ai for product managers",
                                                                           "ai tools for product managers"),
    "visual design principles|": ("principles of design", "elements of design"),
    "market research and competitor analysis|": ("marketing research", "online market research platforms"),
    "customer experience (cx)|": ("customer experience", "voice of the customer"),
    "ux writing and content design|": ("ux writing", "content strategy"),
}
# Notes on head-term choices that needed judgment (shown in the tree document).
HEAD_NOTES = {
    "u14": "user interviews (49,500) skipped as head 1: mostly the User Interviews brand",
    "u16": "user interviews is also the User Interviews brand (userinterviews.com); most of this sub-topic is brand queries",
    "u20": "content marketing and marketing strategy are larger but generic marketing; marketing funnel is the product-adjacent head",
    "u31": "originality pricing (33,100) is noise",
    "u33": "what is retail pricing (5,400) is larger but not a case study",
    "u50": "component-based software engineering, shadcn ui and design patterns are larger but software or brand queries",
    "u51": "many small UI-component phrases; design patterns and shadcn ui are software or brand queries",
    "u59": "product manager reads as a role query; job listings are flagged and excluded",
    "u74": "design books (Phase 0 SERP reused) and books about design are variants of one query",
    "u83": "SurveyMonkey, Raosoft and Qualtrics calculators are brand queries",
    "ai in product and design work|": "ai design assistant (22,200) is larger but reads as a general assistant-tool"
                                      " query; ai tools for product managers reuses a Phase 0 SERP",
    "market research and competitor analysis|": "market research analyst (5,400) is a job title; no bare"
                                                " \"market research\" row in the harvest",
    "ux writing and content design|": "content strategy (3,600) is larger but mostly marketing content strategy",
}


def read(path):
    with open(path, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def adjusted(rows):
    seen = {}
    for r in rows:
        seen.setdefault((r["volume"], r["monthly_12"]), int(r["volume"] or 0))
    return sum(seen.values())


def med(xs):
    return statistics.median(xs) if xs else None


def vfile(stem, version, date):
    """keywords/<stem>-<version>-<date>.csv; the v2 harvest has no version in its name."""
    if stem == "harvest-articles-combined":
        return os.path.join(KW, "%s-%s.csv" % (stem, date) if version == "v2" else "%s-%s-%s.csv" % (stem, version, date))
    return os.path.join(KW, "%s-%s-%s.csv" % (stem, version, date))


def load_units(date=DATE, version="v2"):
    """Return (units, dropped). Each unit: dict(unit_id, kind, section_or_domain, topic, subtopic_or_category,
    rows=[keyword rows], src=dict of candidate-file stats)."""
    harvest = {r["keyword"]: r for r in read(vfile("harvest-articles-combined", version, date))}
    k2t = read(vfile("keyword-to-topic", version, date))
    by_topic = collections.defaultdict(list)
    by_sub = collections.defaultdict(list)
    for r in k2t:
        if r["topic"] == "unassigned" or r["keyword"] not in harvest:
            continue
        by_topic[r["topic"]].append(harvest[r["keyword"]])
        by_sub[(r["topic"], r["subtopic"])].append(harvest[r["keyword"]])
    units, dropped = [], []
    n = 0
    for c in read(vfile("topic-candidates", version, date)):
        kind = "subtopic" if c["subtopic"] else "topic"
        rows = by_sub[(c["topic"], c["subtopic"])] if c["subtopic"] else by_topic[c["topic"]]
        key = (c["topic"], c["subtopic"])
        if key in DROP_TOPIC:
            dropped.append((kind, c["topic"], c["subtopic"], DROP_TOPIC[key]))
            continue
        n += 1
        units.append({"unit_id": "u%02d" % n, "kind": kind, "section_or_domain": c["domain_guess"],
                      "topic": c["topic"], "subtopic_or_category": c["subtopic"], "rows": rows, "src": c})
    # sections
    srows = [r for r in read(os.path.join(KW, "harvest-sections-%s.csv" % date))
             if not r.get("flag_v1_1", r["flag"]) and int(r["volume"] or 0) >= 100]  # v1.1 flags (see harvest.old_flag)
    assign = collections.defaultdict(list)
    for sec, rules in RULES.items():
        for r in srows:
            if sec not in r["section"].split(";"):
                continue
            hit = next(((c, subs) for c, p, subs in rules if re.search(p, r["keyword"])), None)
            if not hit:
                continue
            c, subs = hit
            assign[(sec, c)].append(r)
            s = next((s for s, sp in subs if re.search(sp, r["keyword"])), None)
            if s:
                assign[(sec, "%s > %s" % (c, s))].append(r)
    for c in read(os.path.join(KW, "section-candidates-%s.csv" % date)):
        if c["category"] == "(below threshold)" or int(c["keyword_count"]) < 10:
            continue
        if c["category"] in DROP_SECTION:
            dropped.append(("section", c["section"], c["category"], DROP_SECTION[c["category"]]))
            continue
        rows = assign[(c["section"], c["category"])]
        if len(rows) != int(c["keyword_count"]):
            print("warning: %s %s rebuilt %d keywords, file says %s" % (c["section"], c["category"], len(rows),
                                                                         c["keyword_count"]), file=sys.stderr)
        n += 1
        units.append({"unit_id": "u%02d" % n, "kind": "section", "section_or_domain": c["section"],
                      "topic": c["section"], "subtopic_or_category": c["category"], "rows": rows, "src": c})
    if version != "v2":
        old = {"%s|%s" % (r["topic"], r["subtopic_or_category"]): r["unit_id"]
               for r in read(os.path.join(KW, "phase4-units-%s.csv" % date))}
        nxt = max(int(i[1:]) for i in old.values()) + 1
        for u in units:
            k = unit_key(u)
            if k in old:
                u["unit_id"] = old[k]
            else:
                u["unit_id"] = "u%02d" % nxt
                u["new"] = True
                nxt += 1
        gone = set(old) - {unit_key(u) for u in units}
        for k in sorted(gone):
            dropped.append(("v1 unit no longer present", old[k], k, ""))
        units.sort(key=lambda u: int(u["unit_id"][1:]))
    return units, dropped


def heads_for(u):
    if u.get("new"):
        return NEW_HEADS[unit_key(u)]
    return HEADS[u["unit_id"]]


def unit_key(u):
    return "%s|%s" % (u["topic"], u["subtopic_or_category"])


def unit_stats(u):
    rows = u["rows"]
    adj = int(u["src"]["adjusted_volume"]) if u["kind"] == "section" else adjusted(rows)
    return {"keyword_count": int(u["src"]["keyword_count"]), "adjusted_volume": adj,
            "median_difficulty": u["src"]["median_difficulty"]}


UNIT_COLS = ["unit_id", "kind", "section_or_domain", "topic", "subtopic_or_category", "head_term_1", "head_term_2",
             "keyword_count", "adjusted_volume", "median_difficulty"]


def write_units(units, dropped, date=DATE, version="v2"):
    out = []
    for u in units:
        h1, h2 = heads_for(u)
        kws = {r["keyword"] for r in u["rows"]}
        for h in (h1, h2):
            if h and h not in kws:
                raise SystemExit("head term %r is not a keyword of %s" % (h, u["unit_id"]))
        out.append(dict(unit_id=u["unit_id"], kind=u["kind"], section_or_domain=u["section_or_domain"],
                        topic=u["topic"], subtopic_or_category=u["subtopic_or_category"], head_term_1=h1,
                        head_term_2=h2, **unit_stats(u)))
    path = os.path.join(KW, "phase4-units-%s.csv" % date if version == "v2" else
                        "phase4-units-%s-%s.csv" % (version, date))
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=UNIT_COLS)
        w.writeheader()
        w.writerows(out)
    print("units: %d -> %s" % (len(out), path))
    for d in dropped:
        print("dropped:", d)


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "candidates"
    version = sys.argv[2] if len(sys.argv) > 2 else "v2"
    units, dropped = load_units(version=version)
    if cmd == "candidates":
        for u in units:
            rows = sorted((r for r in u["rows"] if not r.get("flag_v1_1", r["flag"])), key=lambda r: -int(r["volume"] or 0))
            print("%s %s | %s | %d kw%s" % (u["unit_id"], u["kind"][0], unit_key(u), len(u["rows"]),
                                            " | NEW" if u.get("new") else ""))
            print("    " + "; ".join("%s %s" % (r["keyword"], r["volume"]) for r in rows[:9]))
        print("dropped:", dropped)
    elif cmd == "write":
        write_units(units, dropped, version=version)


if __name__ == "__main__":
    main()
