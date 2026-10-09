#!/usr/bin/env python3
"""Phase 1 keyword harvest for Articles (userandproduct.com).

Standard library only. Uses dataforseo_client.py (cache check, budget guard, raw save).

Usage (from the project root):
    python research/seo/tools/harvest.py fetch --probe          # first seed only, prints cost and rows
    python research/seo/tools/harvest.py fetch                  # remaining seeds (cached ones skipped)
    python research/seo/tools/harvest.py distil                 # raw -> keywords/harvest-articles-<date>.csv
    python research/seo/tools/harvest.py fetch --dry-run        # print requests only

    Phase 1b (keyword suggestions, phrase match):
    python research/seo/tools/harvest.py fetch --endpoint suggestions --tag 1b --cap 1.10 --probe
    python research/seo/tools/harvest.py fetch --endpoint suggestions --tag 1b --cap 1.10
    python research/seo/tools/harvest.py distil --endpoint suggestions --tag 1b

    Phase 1c (AI in product and design work, phrase match; note "phase1c ai"):
    python research/seo/tools/harvest.py fetch --endpoint suggestions --tag ai --cap 0.45 --probe
    python research/seo/tools/harvest.py distil --endpoint suggestions --tag ai

    Phase 3 (section seeds, keywords/seeds-sections-<date>.csv with seed,section; note "phase3 <section>"):
    python research/seo/tools/harvest.py fetch --endpoint suggestions --tag sections --cap 0.50 --probe
    python research/seo/tools/harvest.py distil --endpoint suggestions --tag sections   # + section column
    python research/seo/tools/harvest.py reflag --file research/seo/keywords/<harvest>.csv  # flags only, in place
    python research/seo/tools/harvest.py reflag --rules v1.1 --file ...   # the v1.1 jobs list (before 9 Oct 2026)
    python research/seo/tools/harvest.py reintent --file research/seo/keywords/<harvest>.csv  # fine_intent, in place

v1.2 (9 Oct 2026): fine_intent(kw) gives one finer intent per keyword by wording, first match wins: career, brand,
dictionary, tool, template, compare, learn, define, question, other (rules next to the function; "remote usability
testing" is not career and "agile software development" is not tool). The jobs flag now uses the
same career list (position, vacancy, remote, intern, ...; "jobs to be done" excepted). reflag with the v1.2 rules
keeps the previous flags in a flag_v1_1 column; v1.1 code paths read it through old_flag(row).
reintent also writes field_fit (yes, partial, no) and field_rule from field_fit_rule(kw) (rules next to it).

Options: --date YYYY-MM-DD (file date, default 2026-10-08), --cap 2.00 (dollars per run),
         --endpoint ideas|suggestions (default ideas = Phase 1 behaviour),
         --limit N (rows per seed; default 250 for ideas, 150 for suggestions),
         --tag T (file and note tag: seeds-articles-T-<date>.csv, harvest-articles-T-<date>.csv,
                  note "phaseT articles"; default none = Phase 1 files and note "phase1 articles").
Ideas are category-wide, so the volume sort pulls category noise; suggestions are phrase match (every
result contains the seed), so the volume sort is safe there.

Inputs:  keywords/seeds-articles[-T]-<date>.csv (seed,domain)
Outputs: cache/raw/<id>.json + one cache/index.csv row per seed (note "phase1 articles; N rows; $cost")
         keywords/harvest-articles[-T]-<date>.csv
         (keyword,seeds,domains,volume,cpc,competition,difficulty,intent,monthly_12,slope_12m,seasonal,flag)
"""
import argparse
import csv
import json
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dataforseo_client as dfs  # noqa: E402

SEO = dfs.SEO
ENDPOINTS = {"ideas": "dataforseo_labs/google/keyword_ideas/live",
             "suggestions": "dataforseo_labs/google/keyword_suggestions/live"}
DEFAULT_LIMIT = {"ideas": 250, "suggestions": 150}

BRANDS = ["figma", "jira", "notion", "miro", "asana", "trello", "monday", "clickup", "productboard", "aha",
          "pendo", "amplitude", "mixpanel", "hotjar", "adobe", "sketch", "invision", "salesforce", "hubspot",
          "google", "microsoft", "atlassian", "confluence", "airtable", "canva", "webflow", "framer", "zeplin",
          "maze", "dovetail", "userpilot", "optimizely", "tableau", "looker", "power bi", "excel", "chatgpt",
          "openai"]
# v1.1 jobs list (kept so the v1.1 flags can be reproduced: flag_for(kw, rules="v1.1")).
JOBS_V11 = ["job", "jobs", "salary", "salaries", "hiring", "career", "resume", "interview question",
            "interview questions", "certification", "certified", "exam", "pmp", "csm"]
# v1.2 (9 Oct 2026): the jobs flag uses the full career list, the same list as fine_intent "career".
CAREER = ["job", "jobs", "salary", "salaries", "hiring", "hire", "career", "careers", "resume", "cv",
          "interview question", "interview questions", "certification", "certified", "exam", "pmp", "csm", "cspo",
          "position", "positions", "vacancy", "vacancies", "opening", "openings", "recruit", "recruiter",
          "recruiters", "remote", "near me", "internship", "internships", "intern", "interns", "entry level",
          "apprenticeship"]
JOBS = CAREER
FLAG_RULES = {"v1.1": JOBS_V11, "v1.2": CAREER}
COURSE = ["course", "courses", "bootcamp", "certificate", "degree", "training", "udemy", "coursera"]


def has_term(kw, terms):
    for t in terms:
        if re.search(r"(?<![a-z0-9])%s(?![a-z0-9])" % re.escape(t), kw):
            return True
    return False


# "jobs to be done" is a product framework, not a job search: the phrase is removed before the JOBS test,
# so "jobs to be done framework" stays unflagged while "jobs to be done salary" is still flagged.
JTBD = re.compile(r"\bjobs?[ -]to[ -]be[ -]done\b")
# v1.2: remote research methods are practice, not a job search ("remote usability testing software" stays unflagged).
REMOTE_METHOD = re.compile(r"\bremote (moderated |unmoderated )?(usability|user|ux) (testing|tests?|research|interviews?)\b")


def not_career_text(k):
    """The keyword with the phrases that only look like career words removed (jobs to be done, remote testing)."""
    return REMOTE_METHOD.sub(" ", JTBD.sub(" ", k))


def flag_for(kw, rules="v1.2"):
    """Flag a keyword: brand, jobs or course (first match wins), else "". rules="v1.1" uses the v1.1 jobs list."""
    k = kw.lower()
    if has_term(k, BRANDS):
        return "brand"
    if has_term(JTBD.sub(" ", k) if rules == "v1.1" else not_career_text(k), FLAG_RULES[rules]):
        return "jobs"
    if has_term(k, COURSE):
        return "course"
    return ""


# Fine intent (v1.2, 9 Oct 2026): what the searcher means, decided by wording, first match wins in the order
# career, brand, dictionary, tool, template, compare, learn, define, question, other. The source label (column "intent":
# informational, navigational, commercial, transactional) is kept as is.
FINE_INTENTS = ["define", "learn", "compare", "template", "tool", "question", "career", "brand", "dictionary",
                "other"]
PRACTITIONER = ["learn", "compare", "template", "tool", "question"]
TOOL_TERMS = ["calculator", "calculators", "generator", "generators", "software", "tool", "tools", "platform",
              "platforms", "app", "apps", "plugin", "plugins", "extension", "extensions"]
TEMPLATE_TERMS = ["template", "templates", "example", "examples", "sample", "samples", "checklist", "checklists",
                  "format", "formats", "worksheet", "worksheets", "canvas", "pdf", "download", "downloads"]
COMPARE_TERMS = ["vs", "versus", "difference between", "differences between", "compared", "comparison", "or",
                 "better than", "alternatives", "alternative"]
LEARN_TERMS = ["how to", "guide", "guides", "tutorial", "tutorials", "steps", "process", "tips", "best practices",
               "ways to", "learn"]
# "software" names the field, not a tool, in these phrases ("agile software development", "software requirements").
SOFTWARE_FIELD = re.compile(r"\b(agile |scrum |for )?software (development|engineering|engineer|requirements?|"
                            r"as a service|project|manifesto)\b|\b(agile|scrum) software\b")
# Dictionary lookups (v1.2, 9 Oct 2026, checked after career and brand, before everything else): word meaning,
# synonyms, spelling, pronunciation, translation, or an everyday word on its own. Never practitioner demand.
EVERYDAY = {"prioritization", "prioritisation", "prioritize", "prioritise", "prioritizing", "priority", "priorities",
            "analytics", "analysis", "analytic", "metrics", "metric", "retention", "retain", "accessibility",
            "accessible", "agile", "agility", "design", "designs", "designing", "management", "manage", "strategy",
            "strategies", "research", "engagement", "experience", "journey", "journeys", "innovation", "leadership",
            "marketing", "development", "discovery", "pricing", "price", "survey", "surveys", "questionnaire",
            "interview", "interviews", "stakeholder", "stakeholders", "testing", "requirements", "requirement",
            "framework", "frameworks", "methodology", "methodologies", "principles", "principle", "elements",
            "loyalty", "change"}
DICT_TERMS = ["another word for", "other word for", "other words for", "synonym", "synonyms", "antonym", "antonyms",
              "pronunciation", "pronounce", "pronounced", "in a sentence", "spelled", "spelling", "spell", "thesaurus",
              "abbreviation", "acronym", "is a word", "a word", "in spanish", "in french", "in german", "in hindi",
              "in tagalog", "in urdu", "in tamil", "in telugu", "in marathi", "in bengali", "in arabic", "in chinese",
              "in korean", "in japanese", "in portuguese", "in italian", "plural", "dictionary", "etymology"]
DEF_WORDS = {"meaning", "meanings", "definition", "definitions", "define", "defined", "mean", "means", "def",
             "meaningful"}
DEF_FILLER = {"what", "is", "the", "of", "a", "an", "does", "do", "in", "for", "to", "by", "word", "term", "simple",
              "words"}


def is_dictionary(k):
    words = k.split()
    if has_term(k, DICT_TERMS):
        return True
    if len(words) == 1 and words[0] in EVERYDAY:
        return True
    if set(words) & DEF_WORDS:
        subject = [w for w in words if w not in DEF_WORDS and w not in DEF_FILLER]
        if len(subject) == 1 and subject[0] in EVERYDAY:
            return True
    m = re.match(r"^([a-z]+) or ([a-z]+)$", k)
    if m and m.group(1).replace("s", "z") == m.group(2).replace("s", "z"):
        return True  # "prioritisation or prioritization": a spelling question
    return False


DEFINE_START = ("what is ", "what are ", "what does ")
DEFINE_TERMS = ["meaning", "definition", "define"]
QUESTION_START = {"why", "when", "which", "who", "should", "can", "do", "does", "is", "are"}


def fine_intent(kw):
    """One fine intent per keyword by wording (see the rule order above)."""
    k = " ".join(kw.lower().split())
    words = k.split()
    if has_term(not_career_text(k), CAREER):
        return "career"
    if has_term(k, BRANDS):
        return "brand"
    if is_dictionary(k):
        return "dictionary"
    if has_term(SOFTWARE_FIELD.sub(" ", k), TOOL_TERMS):
        return "tool"
    if has_term(k, TEMPLATE_TERMS):
        return "template"
    if has_term(k, COMPARE_TERMS):
        return "compare"
    if (words and words[0] == "how") or has_term(k, LEARN_TERMS):
        return "learn"
    if k.startswith(DEFINE_START) or has_term(k, DEFINE_TERMS):
        return "define"
    if words and words[0] in QUESTION_START:
        return "question"
    if 1 <= len(words) <= 3:
        return "define"  # a bare noun phrase of 1 to 3 words reads as "tell me what this is"
    return "other"


# Field fit (v1.2, 9 Oct 2026): is the searcher one of our readers? "yes" when the phrase is plainly about product,
# design or business work (a method, artifact, role, metric, tool category or activity of that work); "no" when it
# belongs to another world; "partial" when it is generic but a product reader could plausibly type it. Rules first
# (FIELD_NO, then FIELD_YES, else partial); the manual review in keywords/field-fit-review-2026-10-09.csv overrides
# them for each unit's 30 highest-volume phrases (tools/phase4c.py applies it).
FIELD_NO = [
    ("personal tasks and time", r"\b(task|tasks)\b(?! management)(?<!testing tasks)|\bto[ -]?do lists?\b|\btodo\b|\b(time management|personal|"
                                r"work load|workload|homework|chores?)\b|\b(high|top|low|first|main|key|highest|"
                                r"utmost|number one) priorit"),
    ("health care and nursing", r"\b(nurs\w*|nclex|patients?|triage|clinical|medical|hospital|health ?care|doctor|"
                                r"therapy|mental|disabilit\w*|wheelchair)\b"),
    ("HR and employees", r"\b(employees?|staff|workforce|human resources|hr|payroll|teachers?|recruit\w*)\b"),
    ("school and students", r"\b(students?|school|classroom|kids|college|university|homework|essay|grade)\b"),
    ("money and property", r"\b(mortgage|loans?|credit card|real estate|insurance|stocks?|crypto|bank\w*)\b"),
    ("home, food and crafts", r"\b(cooking|recipes?|food|kitchen|interior|home|wedding|fashion|tattoo|garden|"
                              r"landscap\w*|nail|hair|clothing|furniture)\b"),
    ("devices and settings", r"\b(iphone|ipad|android|windows|settings?|xbox|playstation|ps5|nintendo|"
                             r"controller|keyboard|mac|laptop|printer)\b"),
    ("maps, places and travel", r"\b(journey planner|planner map|map my journey|journey time map|travel|trip|flight|"
                                r"soil|weather|geograph\w*|google maps?)\b"),
    ("religion, history and literature", r"\b(bible|missionar\w*|jesus|paul'?s?|god|church|hero'?s|novel|poem|"
                                         r"lewis and clark|odysse\w*|ulysses|frodo|columbus|abraham'?s?|titanic|"
                                         r"hobbit|moses|exodus)\b"),
    ("personality and self-help", r"\b(character strengths|personality|horoscope|zodiac|self[ -]help)\b"),
    ("generic small business", r"\b(business plan|small business|sba|llc|startup ideas)\b"),
    ("engineering and software construction", r"\bsoftware engineering\b|\bmicroservices?\b|\bcad\b|"
                                               r"\bplant design\b|\bcircuit|\bmechanical\b"),
]
FIELD_YES = re.compile(
    r"\b(products?|ux|ui|user|users|usability|prototyp\w*|wireframe\w*|mockups?|personas?|roadmaps?|backlogs?|"
    r"sprints?|scrum|kanban|okrs?|kpis?|mvp|prd|requirements?|acceptance criteria|story points|epics?|moscow|rice|kano|"
    r"stakeholders?|change management|a/?b test\w*|ab test\w*|split test\w*|experiment\w*|conversion|funnels?|"
    r"go[ -]to[ -]market|gtm|positioning|value proposition|selling proposition|market fit|beta test\w*|churn|"
    r"customers?|nps|csat|cac|ltv|arr|mrr|saas|onboarding|features?|design systems?|design thinking|"
    r"information architecture|interaction design|service design|visual design|web ?design|website design|"
    r"landing pages?|call to action|wcag|ada compliance|section 508|vpat|aria|screen readers?|"
    r"web accessibility|digital accessibility|website accessibility|accessibility (testing|checker|audit|"
    r"guidelines|standards|statement|tools?|compliance|design)|"
    r"agile (methodolog\w*|project|framework|manifesto|principles?|team|transformation|scrum|software|process|"
    r"approach|method\w*|development|practices|ceremon\w*|values|coach)|"
    r"prioriti[sz]ation (framework|frameworks|technique|techniques|method|methods|model|models|criteria|scoring)|"
    r"product analytics|web analytics|digital analytics|marketing analytics|business analytics|customer analytics|"
    r"design (principles|patterns?|process|sprint|research|review|critique|language|tokens?|components?|"
    r"elements|strategy|leadership|ops)|"
    r"usability testing|user testing|user research|ux research|survey (design|questions?|tools?|software|"
    r"platforms?|methods?|research)|research methods|qualitative|quantitative|focus groups?|"
    r"pricing (strategy|strategies|models?|page|tiers?)|freemium|subscription|dynamic pricing|competitive pricing|"
    r"value[ -]based pricing|penetration pricing|price skimming|project management|program management|"
    r"product management|growth|retention rate|engagement rate|cohort|market research|competitor analysis|"
    r"competitive analysis|swot|marketing (strategy|plan|funnel|mix)|4 ?ps|content strategy|content design|"
    r"ux writing|microcopy|journey maps?|user flows?|user stor\w*|use cases?)\b")
PARTIAL_HINTS = re.compile(r"\b(prioriti[sz]ation matrix|priority matrix|retention rate|data analytics|"
                           r"data analysis|performance metrics|dora metrics|eisenhower|task management)\b")

STRONG_FIELD = re.compile(r"\b(customers?|users?|products?|saas|churn|client|consumer)\b")


def field_fit_rule(kw):
    """Return (field_fit, rule name) for a keyword by rules: no, yes or partial."""
    k = " ".join(kw.lower().split())
    for name, rx in FIELD_NO:
        if re.search(rx, k):
            return "no", name
    if PARTIAL_HINTS.search(k) and not STRONG_FIELD.search(k):
        return "partial", "generic but plausible for a product reader"
    if FIELD_YES.search(k):
        return "yes", "names a method, artifact, role, metric or tool of the work"
    return "partial", "no field word and no other-world word"


AI_TAG = "ai"  # --tag ai: Phase 1c AI-in-the-field seeds (seed,domain), note "phase1c ai"
SECTIONS_TAG = "sections"  # --tag sections: Phase 3 section seeds (seed,section), note "phase3 <section>"


def stem(tag):
    if tag == SECTIONS_TAG:
        return "sections"
    return "articles-%s" % tag if tag else "articles"


def note_prefix(tag, group=""):
    if tag == AI_TAG:
        return "phase1c ai"
    if tag == SECTIONS_TAG:
        return "phase3 %s" % group if group else "phase3 "
    return "phase%s articles" % (tag or "1")


def seeds_path(date, tag=""):
    return os.path.join(SEO, "keywords", "seeds-%s-%s.csv" % (stem(tag), date))


def load_seeds(date, tag=""):
    with open(seeds_path(date, tag), encoding="utf-8", newline="") as fh:
        return [(r["seed"], r.get("domain") or r.get("section") or "") for r in csv.DictReader(fh)]


def task_for(seed, endpoint="ideas", limit=None):
    limit = limit or DEFAULT_LIMIT[endpoint]
    t = {"location_code": 2840, "language_code": "en", "limit": limit,
         "include_seed_keyword": True, "filters": [["keyword_info.search_volume", ">=", 100]],
         "order_by": ["keyword_info.search_volume,desc"]}
    if endpoint == "suggestions":
        t = dict({"keyword": seed}, **t)
    else:
        t = dict({"keywords": [seed]}, **t)
    return [t]


def items_of(res):
    try:
        t = res["tasks"][0]
        r = t.get("result") or []
        return ((r[0] or {}).get("items") or []) if r else [], t.get("status_code"), t.get("status_message")
    except (KeyError, IndexError, TypeError):
        return [], None, None


def fetch(args):
    seeds = load_seeds(args.date, args.tag)
    endpoint = ENDPOINTS[args.endpoint]
    if args.probe:
        seeds = seeds[:1]
    c = dfs.Client(cap=args.cap, dry_run=args.dry_run)
    first = True
    for seed, domain in seeds:
        if not first and not args.dry_run:
            time.sleep(1)
        try:
            res = c.post(endpoint, task_for(seed, args.endpoint, args.limit), subject=seed)
        except dfs.BudgetExceeded:
            break
        first = False
        if res is None:
            continue
        items, code, msg = items_of(res)
        cost = float(res.get("cost") or 0)
        note = "%s; %d rows; $%.4f" % (note_prefix(args.tag, domain), len(items), cost)
        if code != 20000:
            note += "; status %s %s" % (code, msg)
        dfs.index_row(res["_id"], "dataforseo", endpoint, seed, "2840", res["_file"], note)
        print("%-32s %-8s rows %3d  cost $%.4f  status %s" % (seed, domain, len(items), cost, code))
    print("run spent $%.4f over %d requests" % (c.spent, c.requests))


def reflag(args):
    """Re-run flag_for over an existing harvest CSV in place (no API calls); prints how many rows changed.

    With the v1.2 rules (the default) the previous flags are first copied to a "flag_v1_1" column (once; an
    existing flag_v1_1 column is never overwritten), so the v1.1 clustering and scores stay reproducible:
    the v1.1 code paths read it through old_flag(row)."""
    path = args.file
    with open(path, encoding="utf-8", newline="") as fh:
        rd = csv.DictReader(fh)
        cols = list(rd.fieldnames)
        rows = list(rd)
    if args.rules != "v1.1" and "flag_v1_1" not in cols:
        cols.insert(cols.index("flag") + 1, "flag_v1_1")
        for r in rows:
            r["flag_v1_1"] = r["flag"]
    changed = []
    for r in rows:
        f = flag_for(r["keyword"], args.rules)
        if f != r["flag"]:
            changed.append((r["keyword"], r["flag"], f))
            r["flag"] = f
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    print("reflag %s: %d rows, %d changed" % (path, len(rows), len(changed)))
    for c in changed:
        print("  %s: %r -> %r" % c)


def old_flag(row):
    """The v1.1 flag of a harvest row: flag_v1_1 when the file was re-flagged with the v1.2 rules, else flag."""
    return row["flag_v1_1"] if "flag_v1_1" in row else row["flag"]


def reintent(args):
    """Add or rewrite the fine_intent, field_fit and field_rule columns of a harvest CSV in place (no API calls).

    field_fit here is the rule result; the manual review file overrides it in tools/phase4c.py."""
    path = args.file
    with open(path, encoding="utf-8", newline="") as fh:
        rd = csv.DictReader(fh)
        cols = list(rd.fieldnames)
        rows = list(rd)
    if "fine_intent" not in cols:
        cols.insert(cols.index("intent") + 1, "fine_intent")
    for c in ("field_fit", "field_rule"):
        if c not in cols:
            cols.insert(cols.index("fine_intent") + 1 + (c == "field_rule"), c)
    counts = {}
    changed = 0
    for r in rows:
        fi = fine_intent(r["keyword"])
        changed += fi != r.get("fine_intent")
        r["fine_intent"] = fi
        r["field_fit"], r["field_rule"] = field_fit_rule(r["keyword"])
        counts[fi] = counts.get(fi, 0) + 1
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    print("reintent %s: %d rows, %d set or changed; %s" % (path, len(rows), changed,
          ", ".join("%s %d" % (k, counts.get(k, 0)) for k in FINE_INTENTS)))


def distil(args):
    seeds = dict(load_seeds(args.date, args.tag))
    endpoint = ENDPOINTS[args.endpoint]
    files = {}
    for row in dfs.read_index():
        if row["subject"] not in seeds or "; status " in row["note"]:
            continue
        prefix = note_prefix(args.tag, seeds[row["subject"]]) + ";"
        if row["endpoint"] == endpoint and row["note"].startswith(prefix):
            files[row["subject"]] = row["file"]  # latest wins
    kws = {}
    for seed, rel in files.items():
        with open(os.path.join(SEO, rel), encoding="utf-8") as fh:
            res = json.load(fh)
        items, _, _ = items_of(res)
        for it in items:
            kw = (it.get("keyword") or "").strip().lower()
            if not kw:
                continue
            ki = it.get("keyword_info") or {}
            rec = kws.get(kw)
            if rec is None:
                months = sorted((m for m in (ki.get("monthly_searches") or [])
                                 if m and m.get("year") and m.get("month")),
                                key=lambda m: (m["year"], m["month"]))[-12:]
                vols = [m.get("search_volume") for m in months]
                slope = ""
                seasonal = ""
                if len(vols) == 12 and all(v is not None for v in vols):
                    a, b = sum(vols[:3]) / 3.0, sum(vols[-3:]) / 3.0
                    slope = "%.2f" % (b / a) if a > 0 else ""
                    mn, mx = min(vols), max(vols)
                    seasonal = "yes" if (mn > 0 and mx > 2 * mn) or (mn == 0 and mx > 0) else "no"
                kp = it.get("keyword_properties") or {}
                si = it.get("search_intent_info") or {}
                rec = {"keyword": kw, "seeds": [], "domains": [],
                       "volume": ki.get("search_volume"), "cpc": ki.get("cpc"),
                       "competition": ki.get("competition"),
                       "difficulty": kp.get("keyword_difficulty"), "intent": si.get("main_intent"),
                       "monthly_12": ";".join("" if v is None else str(v) for v in vols),
                       "slope_12m": slope, "seasonal": seasonal, "flag": flag_for(kw)}
                kws[kw] = rec
            if seed not in rec["seeds"]:
                rec["seeds"].append(seed)
            d = seeds[seed]
            if d not in rec["domains"]:
                rec["domains"].append(d)
    out = os.path.join(SEO, "keywords", "harvest-%s-%s.csv" % (stem(args.tag), args.date))
    cols = ["keyword", "seeds", "domains", "volume", "cpc", "competition", "difficulty", "intent",
            "monthly_12", "slope_12m", "seasonal", "flag"]
    if args.tag == SECTIONS_TAG:
        cols.append("section")  # the seed's section; "domains" stays empty for section seeds
        for r in kws.values():
            r["section"], r["domains"] = r["domains"], []
    rows = sorted(kws.values(), key=lambda r: (-(r["volume"] or 0), r["keyword"]))
    with open(out, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for r in rows:
            vals = []
            for k in cols:
                v = r[k]
                if isinstance(v, list):
                    v = ";".join(v)
                vals.append("" if v is None else v)
            w.writerow(vals)
    flags = {}
    for r in rows:
        flags[r["flag"] or "none"] = flags.get(r["flag"] or "none", 0) + 1
    print("seeds read %d; distinct keywords %d; flags %s -> %s" % (len(files), len(rows), flags, out))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["fetch", "distil", "reflag", "reintent"])
    ap.add_argument("--file", default="", help="reflag, reintent: the harvest CSV to rewrite in place")
    ap.add_argument("--rules", choices=sorted(FLAG_RULES), default="v1.2", help="reflag: flag rules version")
    ap.add_argument("--probe", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--cap", type=float, default=2.00)
    ap.add_argument("--date", default="2026-10-08")
    ap.add_argument("--endpoint", choices=sorted(ENDPOINTS), default="ideas")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--tag", default="")
    args = ap.parse_args()
    {"fetch": fetch, "distil": distil, "reflag": reflag, "reintent": reintent}[args.cmd](args)


if __name__ == "__main__":
    main()
