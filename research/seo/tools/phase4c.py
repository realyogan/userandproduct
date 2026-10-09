#!/usr/bin/env python3
"""Phase 4c: intent and field fit per scoring unit (v1.2, 9 Oct 2026; free, local).

Standard library only. Reads distilled CSVs only. Same units, keyword sets and head terms as v1.1
(phase4_units.load_units(version="v1.1")). The harvests carry fine_intent, field_fit and field_rule from
`harvest.py reintent` and the v1.2 flags from `harvest.py reflag` (old flags in flag_v1_1).

Usage (from the project root):
    python research/seo/tools/phase4c.py            # writes keywords/phase4-units-v1.2-2026-10-09.csv
    python research/seo/tools/phase4c.py show u59   # prints one unit's keywords with intent, fit and survival

Per keyword:
- fine intent: the fine_intent column, or the review's intent_override (dictionary or career) where the manual
  review set one;
- field fit: keywords/field-fit-review-2026-10-09.csv (manual review of each unit's 30 highest-volume phrases)
  where the phrase was reviewed, else the rule result in the field_fit column; weight yes 1, partial 0.5, no 0;
- survives: field fit yes or partial, fine intent not career, brand or dictionary, source label not navigational.

Per unit (its keywords are the v1.1 clustered set; phrases the widened v1.2 jobs flag catches stay visible as career):
- intent_mix: volume-weighted share of each fine intent over all the unit's keywords ("define 42; learn 18; ...").
- field_share: surviving volume (partial at half weight) over all the unit's volume.
- dictionary_share, career_share, navigational_share, offfield_share: volume-weighted shares over all keywords.
- adjusted_volume_field: the variant-adjusted volume of the surviving keywords (each distinct (volume, monthly_12)
  series counted once, at the highest fit weight among its phrases). This is the demand that is scored.
- adjusted_volume_practitioner: the earlier v1.2 draft figure (career, brand and navigational removed, no field or
  dictionary filter), kept for comparison with adjusted_volume (v1.1).
- practitioner_share: learn + compare + template + tool + question over the surviving keywords (volume times fit).
- article_capacity: distinct phrase groups among the surviving practitioner keywords (all have volume >= 100); a
  group is the set of content words left after removing intent words (how to, vs, template, examples, tools, best,
  ...), with plurals folded. Label: thin under 5, medium 5 to 15, deep above 15.
- articles_estimate: article_capacity plus one explainer or hub when surviving define demand exists (at least 1
  for a node that is not parked). For a split topic the tree sums its sub-topics.
- meaning_loss: the volume share of dictionary, career and brand phrases plus phrases from another world (field fit
  no). parked: yes when meaning_loss is PARKED_AT (half) or more: the node is on the tree because of what people mean,
  and here most of them mean something else. Site lookups (navigational) are removed from demand but do not park a
  node: the source's label marks some core phrases ("customer journey map") as navigational.
- format_suggestion and section_hint: from the surviving keywords. Format: the largest of define and the
  practitioner intents; define = explainer (hub page with 60+ keywords), learn = how-to guide, compare = comparison,
  template = template page, tool = calculator or tool page, question = explainer. Section: Templates when template
  share >= 0.25; Tools when tool share >= 0.25 and most tool volume is calculators, formulas or scores; Links when
  half or more is tool-list phrases; Books for the books section's own categories; else Articles.
- what_this_is: one sentence from the surviving phrases: the biggest one and the largest practical phrase groups.
- median_difficulty_known: median KD over the surviving keywords with a KD figure (KD 0 means none); shown only.
"""
import collections
import csv
import os
import re
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from harvest import FINE_INTENTS, PRACTITIONER, field_fit_rule, fine_intent  # noqa: E402
from phase4_units import KW, UNIT_COLS, adjusted, heads_for, load_units, unit_stats  # noqa: E402

OUT_DATE = "2026-10-09"
REVIEW = os.path.join(KW, "field-fit-review-2026-10-09.csv")
FIT_W = {"yes": 1.0, "partial": 0.5, "no": 0.0}
PARKED_AT = 0.50
FORMAT = {"define": "explainer", "learn": "how-to guide", "compare": "comparison", "template": "template page",
          "tool": "calculator or tool page", "question": "explainer"}
CALC = re.compile(r"calculat|\bformula|\bscores?\b|\bscoring\b")
TOOL_LIST = re.compile(r"\b(tools|software|platforms|apps|tool)\b")
REMOVED_INTENTS = {"career", "brand", "dictionary"}
INTENT_WORDS = {"how", "to", "do", "does", "did", "you", "i", "we", "a", "an", "the", "of", "for", "in", "on", "with",
                "and", "or", "vs", "versus", "difference", "differences", "between", "compared", "comparison",
                "better", "than", "alternative", "alternatives", "template", "templates", "example", "examples",
                "sample", "samples", "checklist", "checklists", "format", "formats", "worksheet", "pdf", "download",
                "free", "best", "top", "good", "great", "tool", "tools", "software", "app", "apps", "platform",
                "platforms", "calculator", "calculators", "generator", "generators", "plugin", "extension", "what",
                "is", "are", "why", "when", "which", "who", "should", "can", "guide", "tutorial", "steps", "step",
                "process", "tips", "ways", "way", "learn", "make", "create", "creating", "write", "writing", "build",
                "develop", "developing", "calculate", "calculating", "compute", "determine", "figure", "find", "use",
                "using", "online", "my", "your", "it", "by", "word", "doc", "ppt", "powerpoint", "excel", "online",
                "simple", "easy", "list", "type", "types", "sheet", "at", "from", "about", "new"}
COLS = UNIT_COLS + ["adjusted_volume_practitioner", "adjusted_volume_field", "median_difficulty_known", "intent_mix",
                    "practitioner_share", "field_share", "dictionary_share", "career_share", "navigational_share",
                    "offfield_share", "meaning_loss", "article_capacity", "capacity_label", "articles_estimate", "parked",
                    "park_reason", "format_suggestion", "section_hint", "what_this_is", "practical_groups",
                    "share_define", "share_learn", "share_compare", "share_template", "share_tool", "share_question",
                    "share_career", "share_brand", "share_dictionary", "share_other"]


def load_review():
    out = {}
    if not os.path.exists(REVIEW):
        return out
    with open(REVIEW, encoding="utf-8", newline="") as fh:
        for r in csv.DictReader(ln for ln in fh if not ln.startswith("#")):
            out[r["keyword"]] = (r["field_fit"], r["intent_override"])
    return out


REV = load_review()


def fi(r):
    ov = REV.get(r["keyword"], ("", ""))[1]
    return ov or r.get("fine_intent") or fine_intent(r["keyword"])


def fit(r):
    if r["keyword"] in REV:
        return REV[r["keyword"]][0]
    return r.get("field_fit") or field_fit_rule(r["keyword"])[0]


def survives(r):
    return FIT_W[fit(r)] > 0 and fi(r) not in REMOVED_INTENTS and r["intent"] != "navigational"


def vol(r):
    return int(r["volume"] or 0)


def weighted_adjusted(rows):
    seen = {}
    for r in rows:
        k = (r["volume"], r["monthly_12"])
        seen[k] = max(seen.get(k, 0.0), FIT_W[fit(r)])
    return int(round(sum(int(v or 0) * w for (v, _), w in seen.items())))


def group_key(kw):
    k = kw.lower().replace("a/b", "ab").replace("a b ", "ab ").replace("a-b", "ab")
    toks = [t for t in re.findall(r"[a-z0-9]+", k) if t not in INTENT_WORDS]
    toks = [t[:-1] if len(t) > 3 and t.endswith("s") and not t.endswith("ss") else t for t in toks]
    return frozenset(toks)


def practical_groups(rows):
    """[(group id, representative phrase, group volume)] for surviving practitioner phrases, biggest first.

    Phrases join one group when they share a content-word set (group_key) or one Google series (the same volume and
    12-month figures: word-order variants), so variants never count as separate articles."""
    pr = [r for r in sorted(rows, key=lambda r: (-vol(r), r["keyword"])) if survives(r) and fi(r) in PRACTITIONER
          and group_key(r["keyword"])]
    parent = list(range(len(pr)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    first = {}
    for i, r in enumerate(pr):
        for key in (("k", group_key(r["keyword"])), ("s", r["volume"], r["monthly_12"])):
            if key in first:
                parent[find(i)] = find(first[key])
            else:
                first[key] = i
    g = collections.OrderedDict()
    for i, r in enumerate(pr):
        root = find(i)
        if root not in g:
            g[root] = [pr[root]["keyword"], 0]
        g[root][1] = max(g[root][1], vol(r))
    return sorted(((k, v[0], v[1]) for k, v in g.items()), key=lambda x: -x[2])


def intent_stats(u):
    rows = u["rows"]
    tot = sum(vol(r) for r in rows) or 1
    share = {k: sum(vol(r) for r in rows if fi(r) == k) / tot for k in FINE_INTENTS}
    nav = sum(vol(r) for r in rows if r["intent"] == "navigational") / tot
    off = sum(vol(r) for r in rows if fit(r) == "no") / tot
    sv = [r for r in rows if survives(r)]
    sw = {r["keyword"]: vol(r) * FIT_W[fit(r)] for r in sv}
    stot = sum(sw.values())
    field_share = stot / tot
    s_share = {k: (sum(sw[r["keyword"]] for r in sv if fi(r) == k) / stot if stot else 0.0) for k in FINE_INTENTS}
    prac = sum(s_share[k] for k in PRACTITIONER)
    cands = ["define"] + PRACTITIONER
    top = max(cands, key=lambda k: (s_share[k], -cands.index(k)))
    kcount = int(u["src"]["keyword_count"])
    fmt = "hub page" if top == "define" and kcount >= 60 else FORMAT[top]
    tool_rows = [r for r in sv if fi(r) == "tool"]
    tool_vol = sum(sw[r["keyword"]] for r in tool_rows) or 1
    calc = sum(sw[r["keyword"]] for r in tool_rows if CALC.search(r["keyword"])) / tool_vol
    tlist = (sum(sw[r["keyword"]] for r in sv if TOOL_LIST.search(r["keyword"]) and not CALC.search(r["keyword"]))
             / stot) if stot else 0
    if u["kind"] == "section" and u["section_or_domain"] == "books":
        hint = "Books"
    elif s_share["template"] >= 0.25:
        hint = "Templates"
    elif s_share["tool"] >= 0.25 and calc > 0.5:
        hint = "Tools"
    elif tlist >= 0.5:
        hint = "Links"
    else:
        hint = "Articles"
    groups = practical_groups(rows)
    cap = len(groups)
    label = "thin" if cap < 5 else ("medium" if cap <= 15 else "deep")
    removed = {"dictionary lookups": share["dictionary"], "job hunting": share["career"], "brand lookups": share["brand"],
               "another world": sum(vol(r) for r in rows if fit(r) == "no" and fi(r) not in REMOVED_INTENTS) / tot}
    meaning_loss = sum(removed.values())
    parked = meaning_loss >= PARKED_AT
    reason = ""
    if parked:
        big = max(removed, key=lambda k: removed[k])
        reason = "%d%% of its searches are dictionary lookups, job hunting, brands or another world; the largest part" \
                 " is %s (%d%%)" % (round(meaning_loss * 100), big, round(removed[big] * 100))
    has_define = s_share["define"] > 0
    est = 0 if parked else max(1, cap + (1 if has_define else 0))
    kds = [float(r["difficulty"]) for r in sv if r["difficulty"] not in ("", "0")]
    big_sv = sorted(sv, key=lambda r: (-sw[r["keyword"]], r["keyword"]))
    if not big_sv:
        what = "Nothing survives: its searches are dictionary lookups, job hunting, brands or another world."
    else:
        head = big_sv[0]["keyword"]
        if cap:
            angles = [p for _, p, _ in groups[:3]]
            what = 'Searches about "%s"; the practical angles are %s.' % (
                head, ", ".join('"%s"' % p for p in angles[:-1]) + (" and " if len(angles) > 1 else "") +
                '"%s"' % angles[-1])
        else:
            what = 'Searches about "%s", almost all definitions; no practical phrase reaches 100 searches.' % head
    mix = sorted(((k, share[k]) for k in FINE_INTENTS if round(share[k] * 100) > 0), key=lambda x: (-x[1], x[0]))
    out = {"adjusted_volume_practitioner": adjusted([r for r in rows if fi(r) not in ("career", "brand")
                                                     and r["intent"] != "navigational"]),
           "adjusted_volume_field": weighted_adjusted(sv),
           "median_difficulty_known": ("%g" % statistics.median(kds)) if kds else "",
           "intent_mix": "; ".join("%s %d" % (k, round(v * 100)) for k, v in mix),
           "practitioner_share": "%.2f" % prac, "field_share": "%.2f" % field_share,
           "dictionary_share": "%.2f" % share["dictionary"], "career_share": "%.2f" % share["career"],
           "navigational_share": "%.2f" % nav, "offfield_share": "%.2f" % off,
           "article_capacity": cap, "capacity_label": label, "articles_estimate": est,
           "parked": "yes" if parked else "no", "park_reason": reason, "meaning_loss": "%.2f" % meaning_loss,
           "format_suggestion": fmt, "section_hint": hint, "what_this_is": what,
           "practical_groups": " | ".join("%s (%d)" % (p, v) for _, p, v in groups[:12])}
    for k in FINE_INTENTS:
        out["share_" + k] = "%.3f" % share[k]
    return out


def main():
    units, dropped = load_units(version="v1.1")
    if len(sys.argv) > 2 and sys.argv[1] == "show":
        u = next(x for x in units if x["unit_id"] == sys.argv[2])
        for r in sorted(u["rows"], key=lambda r: -vol(r)):
            print("%-58s %7s %-13s %-10s %-7s %s" % (r["keyword"][:58], r["volume"], r["intent"], fi(r), fit(r),
                                                       "survives" if survives(r) else "-"))
        print(intent_stats(u))
        return
    out = []
    for u in units:
        h1, h2 = heads_for(u)
        row = dict(unit_id=u["unit_id"], kind=u["kind"], section_or_domain=u["section_or_domain"], topic=u["topic"],
                   subtopic_or_category=u["subtopic_or_category"], head_term_1=h1, head_term_2=h2, **unit_stats(u))
        row.update(intent_stats(u))
        out.append(row)
    path = os.path.join(KW, "phase4-units-v1.2-%s.csv" % OUT_DATE)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS)
        w.writeheader()
        w.writerows(out)
    print("units: %d -> %s (manual review rows: %d phrases)" % (len(out), path, len(REV)))
    for r in out:
        print("%s %-40s adj %7s field %7s fs %s dict %s cap %2s %-6s prac %s %-22s %-9s %s" % (
            r["unit_id"], (r["subtopic_or_category"] or r["topic"])[:40], r["adjusted_volume"],
            r["adjusted_volume_field"], r["field_share"], r["dictionary_share"], r["article_capacity"],
            r["capacity_label"], r["practitioner_share"], r["format_suggestion"], r["section_hint"],
            "PARKED" if r["parked"] == "yes" else ""))


if __name__ == "__main__":
    main()
