#!/usr/bin/env python3
"""Phase 1b clustering of the combined on-topic Articles harvest into topics and sub-topics (free, local).

Standard library only. Reads distilled CSVs, never raw JSON.

Usage (from the project root):
    python research/seo/tools/cluster_v2.py [--date 2026-10-08] [--version v1.1] [--show TOPIC]

v1.1 (8 Oct 2026): the rules carry tools/cluster_rules_patch.md (manual review of the unassigned keywords):
narrower noise rules (electronic, patient, grid), recovery patterns for existing topics, new topics
(visual design principles, customer experience, ux writing and content design, vision and mission statements,
AI in product and design work) and consumer-AI noise. --version v1.1 (the default) reads
keywords/harvest-articles-combined-v1.1-<date>.csv (from combine_v11.py) and writes
topic-candidates-v1.1-<date>.csv and keyword-to-topic-v1.1-<date>.csv. --version v2 reads the original
combined harvest and writes the v2 file names, but with the v1.1 rules (the v2 files on disk were made with
the earlier rules). Topics in LOW_FLOOR need 10 keywords instead of 20 (the review's bar: 10+ keywords or
5,000+ adjusted searches); "vision and mission statements" keeps the 20 floor. SPLIT_AT_TOPIC lowers the
split threshold for one topic (AI) whose phrases separate cleanly.

Input:   keywords/harvest-articles-combined[-v1.1]-<date>.csv (unflagged rows with volume >= 100 are clustered)
         competitors/sitemaps/*-sitemap-<date>.csv (content rows only; slug_tokens column)
Outputs: keywords/topic-candidates-v2-<date>.csv
         (topic,subtopic,domain_guess,keyword_count,total_volume,median_volume,median_difficulty,
          decision_share,question_share,template_share,top_keywords,competitor_articles,competitor_domains)
         One row per topic with an empty subtopic (the topic total), followed by one row per sub-topic
         when the topic was split.
         keywords/keyword-to-topic-v2-<date>.csv (keyword,topic,subtopic); "unassigned" for the rest
         prints a summary, small groups, noise counts and the largest unassigned word groups

Method: same as cluster_phase1.py. Ordered pattern rules, first match wins; a topic needs 20 or more
keywords, smaller rule groups fall back to "unassigned". A NOISE rule list runs first and sends clearly
off-topic catch (Bible and literature journeys, building systems, nursing prioritization, PLM software)
to "unassigned", with the reason counted. New in v2: a topic with 60 or more keywords is split by its
ordered sub-topic rules; a sub-topic needs 15 or more keywords, smaller ones fold into the topic's
remainder sub-topic ("<name> (general)"). competitor_articles is the same approximation as Phase 1
(5 most distinctive tokens of the group, content URLs whose slug holds at least two of them).
question_share: keywords starting with how, what, why, when, which, who, is, are, can, should, do, does.
template_share: keywords containing template(s), example(s), checklist(s), format(s) or sample(s).
The printed "dd" figure is a variant-adjusted volume: keyword suggestions return many word-order variants
that share one volume and one 12-month series (Google groups close variants), so each distinct
(volume, monthly_12) pair is counted once. It is printed only, not written to the CSV.
"""
import argparse
import collections
import csv
import glob
import math
import os
import re
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cluster_phase1 import DECISION, GENERIC, STOP, tokens  # noqa: E402

SEO = os.path.dirname(HERE)
MIN_KW, SPLIT_AT, MIN_SUB = 20, 60, 15
LOW_FLOOR, MIN_KW_LOW = {"visual design principles", "customer experience (cx)", "ux writing and content design",
                         "market research and competitor analysis", "ai in product and design work"}, 10
SPLIT_AT_TOPIC = {"ai in product and design work": 30}
QUESTION = {"how", "what", "why", "when", "which", "who", "is", "are", "can", "should", "do", "does"}
TEMPLATE = re.compile(r"\b(templates?|examples?|checklists?|formats?|samples?)\b")

NOISE = [
    ("bible and literature journeys",
     r"missionar|\bpaul|frodo|odysse|ulysses|bilbo|hobbit|abraham|columbus|jonah|moses|exodus|israelites|"
     r"lewis and clark|lewis clark|hero'?s journey|gulliver|lord of the rings|lotr|\bjesus|apostle|"
     r"\b(1st|2nd|3rd|first|second|third) (missionary )?journey"),
    ("building and engineering systems",
     r"sprinkler|irrigation|solar|hvac|septic|fire (alarm|system|protection)|closet|electrical|plumbing|"
     r"^(?!.*(design|prioriti)).*\bgrid\b|drainage|water system|embedded|cadence|grokking|system design (interview|primer)|"
     r"machine learning system"),
    ("software system design",
     r"(?<!design )system design|design (for|the) system|system and design|instructional system|interview system"),
    ("physical and device accessibility",
     r"accessib.*\b(student|beach|public|wisconsin|indiana|colorado|nintendo|switch|tesla|transport|"
     r"transportation|healthcare|metro|united|controllers?|controls?|remote|ipad|iphone|sky|settings?|"
     r"medical|ramp|handicap|handicapped|wheelchair|doors?|security|card|spanish|lab|foundation|parking|"
     r"housing|bathroom|xbox|android|windows|ios|hotel|services?)\b|"
     r"\b(student|beach|public|wisconsin|indiana|colorado|nintendo|tesla|metro|united|remote|ipad|sky|"
     r"handicap|handicapped|wheelchair|security|ibcces|outlook|at&t|one|open|setting|settings|"
     r"healthcare|medical)\b.*accessib|spell accessibility"),
    ("nursing prioritization", r"nursing|nclex|\bnurse|delegation"),
    ("customer experience survey (government)", r"customer experience in the va"),
    ("consumer ai apps and off-field ai design",
     r"character ai|image generator|art generator|humani[sz]er|chatbot app|ai chat app|girlfriend|"
     r"\bai (interior|home|room|landscape|logo|game|engineering|engineer)\b|"
     r"(interior|home|room|landscape|logo|game|engineering) design ai|"
     r"\bai\b.{0,25}\b(interior|landscape|logo|room|home|game|engineering) design|"
     r"(interior|landscape|logo|room|home|game|engineering) design\b.{0,15}\bai\b|"
     r"ai engineer(ing)? roadmap|roadmap sh"),
    ("plm software", r"\bplm\b|siemens|solidworks|teamcenter|windchill|lifecycle management software"),
]

# (topic, domain_guess, pattern, [(subtopic, pattern), ...], remainder subtopic name). Order matters.
RULES = [
    ("ai in product and design work", "product",
     r"\bai\b|artificial intelligence|generative ai|\bgenai\b|\bllms?\b|chatgpt|\bagent (chat )?ui",
     [("ai tools for product managers", r"product manage"),
      ("ai prototyping and design tools", r"tool|prototyp|graphic|web ?site|web design|design assistant")],
     "ai in product and ux work (general)"),
    ("user stories and acceptance criteria", "product",
     r"user stor|acceptance criteria|story points|story mapping|story maps|gherkin|given.when|"
     r"invest user story|use case vs user story|\bepic user|\bas a user\b|user points|\bepics?\b",
     [("acceptance criteria", r"acceptance criteria|gherkin|given.when|given then"),
      ("story points and estimation", r"story points|estimat|points"),
      ("story mapping", r"story map"),
      ("user story examples and templates", TEMPLATE.pattern)],
     "user stories (general)"),
    ("product owner and product manager roles", "product",
     r"product owner|product manager|head of product|vp of product|chief product|product lead\b",
     [("product owner", r"product owner"), ("product manager", r"product manager")],
     "product roles (general)"),
    ("agile, scrum and kanban", "product",
     r"\bagile\b|\bscrum\b|\bkanban\b|\bsprints?\b|waterfall|"
     r"\blean (methodology|software|project|techniques|tools|six sigma)|"
     r"six sigma|scaled agile|\bsafe\b|backlog|"
     r"software development (life ?cycle|cycle|process|methodolog)|sdlc|spiral (life.?cycle|methodology)|"
     r"\bv model\b|rapid application development|crystal methodolog|iterative process",
     [("scaled agile (safe)", r"\bsafe\b|scaled|scaling|scalable|\blarge.scale"),
      ("scrum, sprints and backlog", r"scrum|sprint|backlog|stand.?up|retrospective"),
      ("kanban", r"kanban"),
      ("agile manifesto and principles", r"manifesto|principles|values"),
      ("agile vs waterfall", r"waterfall"),
      ("agile project management", r"project")],
     "agile methodology (general)"),
    ("requirements and prd", "product",
     r"(functional|non functional|nonfunctional|product|software|system|user|technical|business|client|project|"
     r"accessibility|application) requirement|requirements (gathering|analysis|elicitation|management|matrix|"
     r"document|doc|definition|questions|meeting|txt)|requirement specification|requirements vs|\bprd\b|"
     r"define the requirements|requirement document|design spec|design brief|draft requirements|"
     r"spec.driven development",
     [], ""),
    ("stakeholder and change management", "product",
     r"stakeholder|change management|management style|leadership|team management|expectation management",
     [("stakeholder management", r"stakeholder|expectation management")], "change management and leadership"),
    ("prioritization", "product",
     r"prioriti[sz]|priority matrix|priority levels|priority list|priority management|must.?have|moscow|"
     r"\brice\b|ice score|eisenhower|top priority|high priority|priorities examples|examples of priorit|"
     r"urgent.{0,5}important|important.{0,5}urgent|prioritization grid",
     [("prioritization frameworks", r"moscow|\brice\b|eisenhower|matrix|framework|method|technique|model|"
                                    r"urgent.{0,5}important|important.{0,5}urgent|grid|"
                                    r"\bice\b|kano|weighted|scor|\babc\b"),
      ("task and time prioritization", r"task|time|work|daily|personal|goals?|skills?")],
     "prioritization (general)"),
    ("product roadmap", "product", r"roadmap", [], ""),
    ("project management", "product",
     r"project manag|project manager|program manager|project (plan|scope|charter|timeline|milestones?|phases|"
     r"life ?cycle|constraints|controls|portfolio|board|success|mapping|requirements)|\bwbs\b|critical path|"
     r"\bevm\b|deliverables|triple constraint|\bpmi\b|milestone|project management office|"
     r"task management|project coordinator|program management|statement of work|scope of work|kick.?off meeting",
     [], ""),
    ("product strategy, discovery and launch", "product",
     r"product strategy|product vision|product positioning|product differentiation|positioning|"
     r"product.market fit|\bmvp\b|minimum viable|product development|new product|product launch|launch formula|"
     r"formula launch|product discovery|innovation discovery|launch(ing)? (a )?(new )?product|product led|"
     r"product-led|product innovation|"
     r"value proposition|selling proposition|product (line|mix|depth|diversification)|^product and strategy$|"
     r"^strategy for product$|product.?/?.?service strategy|product and service strategy|beta testing|launch strategy|release strategy|"
     r"product failures|research and development of a product|product research and development|"
     r"^discovery product$|mvp software",
     [("new product development and launch", r"new product|launch|product development|develop|beta testing|"
                                             r"release strategy|product failures"),
      ("product strategy", r"strateg|vision|positioning|differentiation|market fit|led\b|value proposition|"
                           r"selling proposition|product (line|mix|depth|diversification)")],
     "product strategy and discovery (general)"),
    ("product management (discipline)", "product",
     r"product manag|product life ?cycle|product lifecycle|product operations|product engineering|"
     r"product architecture|product science|data as a product|product-oriented|management (of )?product|"
     r"product (and|&) (services? )?management|product in marketing management|"
     r"product ?/? ?services? management|product features|digital products|pragmatic marketing|"
     r"product obsolescence",
     [("product life cycle", r"life ?cycle|lifecycle|obsolescence")], "product management (general)"),
    ("design thinking", "design",
     r"design thinking|human centered|human-centered|double diamond|design sprint|\bideo\b|"
     r"design.{0,8}thinking|thinking.{0,10}design|human.centered design|^design process$|"
     r"design process thinking|problem statement",
     [("design thinking process and stages", r"process|steps?|stages?|phases?|\b5\b|five|model|framework|"
                                             r"problem statement|"
                                             r"diamond|method|tools?|workshop")],
     "design thinking (general)"),
    ("jobs to be done", "product", r"jobs to be done|\bjtbd\b|job to be done|jobs theory", [], ""),
    ("personas and journey maps", "design",
     r"\bpersonas?\b|persona-|journey map|customer journey|user journey|user flow|ux flow|journey mapping|"
     r"service blueprint|empathy map|experience map|(?<!ideal )customer profile|patient journey|flow ?chart|"
     r"flow of a website",
     [("personas", r"persona|customer profile"),
      ("journey maps and user flows", r"journey|flow|blueprint|experience map|empathy")], ""),
    ("ux research", "design",
     r"ux research|user research|usability|user testing|user interview|research method|qualitative|"
     r"quantitative|research question|card sort|focus group|user feedback|exploratory research|action research|"
     r"user acceptance testing|ux survey|research methodology|survey|questionnaire|open.ended|closed.ended|"
     r"close.ended|dichotomous|semi.structured|tree test|diary stud|\buat\b|"
     r"(closed|filter|hybrid|contingency|branch(ing)?) questions?|likert",
     [("usability testing", r"usability|user testing|user acceptance|\buat\b|tree test|test"),
      ("surveys and questionnaires", r"survey|questionnaire|open.ended|closed.ended|close.ended|dichotomous|"
                                      r"(closed|filter|hybrid|contingency|branch(ing)?) questions?|likert"),
      ("interviews and focus groups", r"interview|focus group|semi.structured"),
      ("research methods", r"method|qualitative|quantitative|research question|card sort|exploratory|"
                           r"action research|diary|technique")],
     "ux research (general)"),
    ("information architecture", "design",
     r"information (about |of |on )?architecture|\bia\b|card sort|site ?map|navigation (design|ux|menu)|taxonomy|"
     r"sitemap examples", [], ""),
    ("accessibility", "design",
     r"accessib|\bwcag\b|\bada\b|\b508\b|a11y|screen reader|alt text|color contrast|colour contrast|"
     r"universal design|assistive technolog",
     [("guidelines and compliance (wcag, ada, 508)", r"wcag|\bada\b|\b508\b|guideline|standard|complian|law|"
                                                     r"requirement|regulation|act\b|vpat|template"),
      ("accessibility testing and checkers", r"test|check|audit|scan|tool|evaluat|validat|widget|overlay"),
      ("web and digital accessibility", r"web|site|digital|online|content|internet|electronic|design|font|colou?r|"
                                        r"contrast|heuristic|ux|app\b|mobile|document|pdf")],
     "accessibility definitions (general)"),
    ("design systems and ui components", "design",
     r"design system|material.?ui|material design|ant design|fluent ui|shadcn|carbon design|swift ?ui|primer|"
     r"\bui (badge|banner|bootstrap|pills?|profile|sides|steppers|toast|datepicker|kit|components?)|"
     r"(badge|badges|banner|banners|chips?|pagination|stepper|steppers|spinners|popovers|dialogs|carousel|"
     r"filter|form|notification|tabs|tagging|coachmark|breadcrumbs|chat|call|faq|leaderboard|profile|"
     r"star rating|rating slider|drop shadow|footnote|inline help|search bar|search box|search field) "
     r"(ui|ux|design)|design patterns?|component|design-system|grid system.*design|design.*grid system",
     [("design systems", r"design system|design-system|material design|carbon|primer|fluent|ant design"),
      ("ui components and patterns", r".")], ""),
    ("visual design principles", "design",
     r"principles? of design|design principles?|elements of design|design elements", [], ""),
    ("ux writing and content design", "design", r"ux writ|ux copy|microcopy|content design|content strategy",
     [], ""),
    ("web design", "design",
     r"web design|website design|design a website|responsive design|website examples|web designer|"
     r"^(?!.*test).*landing page|portfolio website|about us page|faq page|footer examples|layout examples|"
     r"one page website|parts of a website|what makes a good website", [], ""),
    ("ux and ui design (discipline)", "design",
     r"\bux\b|\bui\b|ui/ux|user experience|user interface|interaction design|product design|^digital design$|"
     r"design of everyday things",
     [], ""),
    ("okrs, kpis and metrics", "business",
     r"\bokrs?\b|\bkpis?\b|\bmetrics?\b|north star|vanity metric|key metric|objectives and key results|"
     r"key results|customer acquisition cost|customer lifetime value|\bcac\b|\bltv\b|\bclv\b|\barr formula",
     [("okrs", r"\bokrs?\b|objectives and key results|key results"),
      ("kpis", r"\bkpis?\b")],
     "metrics (general)"),
    ("customer experience (cx)", "business",
     r"customer experience|customer.centric|voice of (the )?customer|customer (advocacy|focus|obsession)|"
     r"customer satisfaction index", [], ""),
    ("retention, churn and engagement", "business",
     r"retention|\bchurn|cohort|(customer|employee|user) engagement|engagement (rate|strategy|formula)|"
     r"active user|loyalty program|onboarding|customer lifecycle|customer success|customer loyalty",
     [("retention rate formulas and calculation", r"calculat|formula|equation|compute|comput|determine|figure|"
                                                   r"find|calculator|how to"),
      ("employee retention", r"employee|staff|employment|workforce|turnover"),
      ("customer retention and loyalty", r"customer|client|consumer|loyalty|churn|user")],
     "retention (general)"),
    ("a/b testing and experimentation", "business",
     r"\ba/?b test|a b test|ab test|split test|experiment|conversion rate(?! optimization)|\bcro\b|multivariate|"
     r"\ba[ -]?b[ -]?(c|n) testing|a-b-testing|a b website testing|what is a and b testing|hypothesis testing|"
     r"\ba ?/ ?b\b|\bab\b|\ba ?(&|to|-) ?b test",
     [("a/b testing tools and platforms", r"tool|software|platform|mailchimp|shopify|vwo|youtube|app\b|plugin"),
      ("a/b testing in marketing (email, landing pages, ads)", r"email|landing|page|marketing|ads?\b|seo|"
                                                                r"website|campaign")],
     "a/b testing (general)"),
    ("pricing strategy", "business", r"pricing|\bprice\b|\bprices\b",
     [("company pricing case studies", r"nike|walmart|amazon|mcdonald|apple|starbucks|airline|hotel|netflix|"
                                       r"costco|target|coca|tesla|uber|disney|retail|restaurant|consulting"),
      ("pricing strategy types and models", r"value|penetration|skimming|premium|cost|competitive|dynamic|"
                                            r"psychological|bundle|freemium|tier|economy|types?|models?|plus|"
                                            r"based|examples?|captive|decoy")],
     "pricing strategy (general)"),
    ("go-to-market and product marketing", "business",
     r"go to market|go-to-market|\bgtm\b|product marketing|market product|product market|marketing mix|"
     r"4 ?ps|four ps|4 p's|price place promotion|segmentation|target market|distribution channel|"
     r"ideal customer profile|customer segments|target definition|product promotion|strategy marketing product",
     [], ""),
    ("market research and competitor analysis", "business",
     r"market(ing)? research|competitive analysis|competitor analysis|competitive|customer insights", [], ""),
    ("vision and mission statements", "business",
     r"mission statement|vision statement|vision and mission|mission and vision", [], ""),
    ("analytics", "business",
     r"analytics|data analyst|analytic|web analytics|business intelligence|product analyst|data analysis tools",
     [("product analytics", r"product")], "data and business analytics"),
    ("growth marketing and funnels", "business",
     r"growth|funnel|marketing strateg|inbound|outbound|content marketing|performance marketing|"
     r"account based|attribution|marketing automation|marketing channels|marketing objectives|"
     r"call to action|marketing plan|b2b marketing|customer acquisition(?! cost)|word of mouth marketing|"
     r"conversion rate optimization", [], ""),
]


def median(xs):
    return statistics.median(xs) if xs else ""


def stats(g, n_all, df, slugs):
    vols = [int(r["volume"]) for r in g]
    kds = [float(r["difficulty"]) for r in g if r["difficulty"] != ""]
    dec = sum(1 for r in g if set(tokens(r["keyword"])) & set(DECISION) or "versus" in r["keyword"])
    q = sum(1 for r in g if (tokens(r["keyword"]) or [""])[0] in QUESTION)
    tp = sum(1 for r in g if TEMPLATE.search(r["keyword"]))
    top = sorted(g, key=lambda r: (-int(r["volume"]), r["keyword"]))[:8]
    tf = collections.Counter()
    for r in g:
        tf.update(set(tokens(r["keyword"])))
    scored = []
    for tok, c in tf.items():
        if tok in GENERIC or len(tok) < 2 or tok.isdigit() or c < 2:
            continue
        scored.append(((c / len(g)) * math.log(n_all / df[tok]) * math.log(1 + c), tok))
    distinct = [tok for _, tok in sorted(scored, reverse=True)[:5]]
    hits = [d for d, st in slugs if len(st & set(distinct)) >= 2]
    seen = {}
    for r in g:
        seen.setdefault((r["volume"], r["monthly_12"]), int(r["volume"]))
    return {"keyword_count": len(g), "total_volume": sum(vols), "_vol_dedup": sum(seen.values()), "median_volume": int(median(vols)),
            "median_difficulty": ("%g" % median(kds)) if kds else "",
            "decision_share": "%.2f" % (dec / len(g)), "question_share": "%.2f" % (q / len(g)),
            "template_share": "%.2f" % (tp / len(g)),
            "top_keywords": ";".join(r["keyword"] for r in top),
            "competitor_articles": len(hits), "competitor_domains": len(set(hits)), "_tokens": " ".join(distinct)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default="2026-10-08")
    ap.add_argument("--version", default="v1.1", choices=["v1.1", "v2"])
    ap.add_argument("--show", default="", help="print every keyword of this topic (or 'unassigned', 'noise')")
    args = ap.parse_args()
    kwdir = os.path.join(SEO, "keywords")
    src = "harvest-articles-combined-%s.csv" if args.version == "v2" else "harvest-articles-combined-v1.1-%s.csv"
    with open(os.path.join(kwdir, src % args.date), encoding="utf-8", newline="") as fh:
        rows = [r for r in csv.DictReader(fh) if not r.get("flag_v1_1", r["flag"]) and int(r["volume"] or 0) >= 100]  # v1.1 flags (see harvest.old_flag)
    noise = [(n, re.compile(p)) for n, p in NOISE]
    compiled = [(t, re.compile(p)) for t, _, p, _, _ in RULES]
    meta = {t: (d, [(s, re.compile(p)) for s, p in subs], rest) for t, d, _, subs, rest in RULES}
    groups = collections.OrderedDict((t, []) for t, _, _, _, _ in RULES)
    unassigned, noise_hits, noise_kw = [], collections.defaultdict(list), set()
    for r in rows:
        kw = r["keyword"]
        nz = next((n for n, rx in noise if rx.search(kw)), None)
        if nz:
            noise_hits[nz].append(r)
            noise_kw.add(kw)
            unassigned.append(r)
            continue
        for t, rx in compiled:
            if rx.search(kw):
                groups[t].append(r)
                break
        else:
            unassigned.append(r)
    def floor(t):
        return MIN_KW_LOW if t in LOW_FLOOR else MIN_KW
    small = {t: g for t, g in groups.items() if len(g) < floor(t)}
    for g in small.values():
        unassigned.extend(g)
    topics = {t: g for t, g in groups.items() if len(g) >= floor(t)}

    # sub-topics
    sub_of = {}
    subgroups = {}
    for t, g in topics.items():
        _, subs, rest = meta[t]
        if len(g) < SPLIT_AT_TOPIC.get(t, SPLIT_AT) or not subs:
            continue
        rest = rest or (t + " (general)")
        parts = collections.OrderedDict((s, []) for s, _ in subs)
        parts[rest] = []
        for r in g:
            s = next((s for s, rx in subs if rx.search(r["keyword"])), rest)
            parts[s].append(r)
        for s in list(parts):
            if s != rest and len(parts[s]) < MIN_SUB:
                parts[rest].extend(parts.pop(s))
        parts = collections.OrderedDict((s, p) for s, p in parts.items() if p)
        if len(parts) < 2:
            continue
        subgroups[t] = parts
        for s, p in parts.items():
            for r in p:
                sub_of[r["keyword"]] = s

    df = collections.Counter()
    for r in rows:
        df.update(set(tokens(r["keyword"])))
    n_all = len(rows)
    slugs = []
    for f in glob.glob(os.path.join(SEO, "competitors", "sitemaps", "*-sitemap-%s.csv" % args.date)):
        with open(f, encoding="utf-8", newline="") as fh:
            for s in csv.DictReader(fh):
                if s.get("content") == "content":
                    slugs.append((s["domain"], set(tokens(s.get("slug_tokens") or ""))))

    out_rows = []
    for t, g in sorted(topics.items(), key=lambda kv: -sum(int(r["volume"]) for r in kv[1])):
        out_rows.append(dict(stats(g, n_all, df, slugs), topic=t, subtopic="", domain_guess=meta[t][0]))
        if t in subgroups:
            for s, p in sorted(subgroups[t].items(), key=lambda kv: -sum(int(r["volume"]) for r in kv[1])):
                out_rows.append(dict(stats(p, n_all, df, slugs), topic=t, subtopic=s, domain_guess=meta[t][0]))
    cols = ["topic", "subtopic", "domain_guess", "keyword_count", "total_volume", "median_volume",
            "median_difficulty", "decision_share", "question_share", "template_share", "top_keywords",
            "competitor_articles", "competitor_domains"]
    with open(os.path.join(kwdir, "topic-candidates-%s-%s.csv" % (args.version, args.date)), "w", encoding="utf-8",
              newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(out_rows)
    with open(os.path.join(kwdir, "keyword-to-topic-%s-%s.csv" % (args.version, args.date)), "w", encoding="utf-8",
              newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["keyword", "topic", "subtopic"])
        for t, g in topics.items():
            for r in sorted(g, key=lambda r: -int(r["volume"])):
                w.writerow([r["keyword"], t, sub_of.get(r["keyword"], "")])
        for r in sorted(unassigned, key=lambda r: -int(r["volume"])):
            w.writerow([r["keyword"], "unassigned", ""])

    assigned = sum(len(g) for g in topics.values())
    print("clustered %d keywords: %d topics (%d keywords), %d unassigned (noise %d)" % (
        len(rows), len(topics), assigned, len(unassigned), len(noise_kw)))
    for r in out_rows:
        name = r["topic"] if not r["subtopic"] else "    - " + r["subtopic"]
        print("%-52s n=%4d vol=%8d dd=%8d medKD=%-4s dec=%s q=%s tpl=%s comp=%d/%d [%s]" % (
            name[:52], r["keyword_count"], r["total_volume"], r["_vol_dedup"], r["median_difficulty"], r["decision_share"],
            r["question_share"], r["template_share"], r["competitor_articles"], r["competitor_domains"],
            r["_tokens"]))
    print("small rule groups (to unassigned):", {t: len(g) for t, g in small.items()})
    print("noise:", {k: len(v) for k, v in noise_hits.items()})
    grp, gvol = collections.Counter(), collections.Counter()
    for r in unassigned:
        if r["keyword"] in noise_kw:
            continue
        tk = tokens(r["keyword"])
        keys = set(x for x in tk if x not in STOP and len(x) > 1)
        keys |= set(" ".join(b) for b in zip(tk, tk[1:]) if b[0] not in STOP and b[1] not in STOP)
        for k in keys:
            grp[k] += 1
            gvol[k] += int(r["volume"])
    print("unassigned groups (non-noise):", "; ".join("%s (%d kw, %d vol)" % (k, c, gvol[k])
                                                      for k, c in grp.most_common(30)))
    if args.show:
        if args.show == "unassigned":
            sel = [r for r in unassigned if r["keyword"] not in noise_kw]
        elif args.show == "noise":
            sel = [r for v in noise_hits.values() for r in v]
        else:
            sel = groups.get(args.show, [])
        for r in sorted(sel, key=lambda r: -int(r["volume"])):
            print("  %s | %s | %s" % (r["keyword"], r["volume"], sub_of.get(r["keyword"], "")))


if __name__ == "__main__":
    main()
