#!/usr/bin/env python3
"""Phase 1 first-pass clustering of the Articles harvest into candidate topics (free, local).

Standard library only. Reads the distilled harvest, never raw JSON.

Usage (from the project root):
    python research/seo/tools/cluster_phase1.py [--date 2026-10-08]

Input:   keywords/harvest-articles-<date>.csv   (unflagged rows with volume >= 100 are clustered)
         competitors/sitemaps/*-sitemap-<date>.csv (content rows only; slug_tokens column)
Outputs: keywords/topic-candidates-<date>.csv
         (topic,domain_guess,keyword_count,total_volume,median_volume,median_difficulty,decision_share,
          top_keywords,competitor_articles,competitor_domains)
         keywords/keyword-to-topic-<date>.csv (keyword,topic); "unassigned" for the rest
         prints a short summary, small topics (under 20 keywords) and the largest unassigned word groups

Method: ordered pattern rules (first match wins), written from the seeds and then split or merged by
the dominant noun phrases seen in the data. A topic needs 20 or more keywords; smaller rule groups
fall back to "unassigned". competitor_articles is an approximation: for each topic, its 5 most
distinctive tokens (topic frequency against corpus frequency, generic words excluded), then content
URLs whose slug tokens contain at least two of them.
"""
import argparse
import collections
import csv
import glob
import math
import os
import re
import statistics

HERE = os.path.dirname(os.path.abspath(__file__))
SEO = os.path.dirname(HERE)

# (topic, domain_guess, pattern). Order matters: specific before general.
RULES = [
    ("user stories and acceptance criteria", "product",
     r"user stor|acceptance criteria|story points|story mapping|story maps|gherkin|given.when|"
     r"invest user story|use case vs user story|\bepic user|\bas a user\b|user points"),
    ("agile, scrum and kanban", "product",
     r"\bagile\b|\bscrum\b|\bkanban\b|waterfall|\blean (methodology|software|project|techniques|tools|six sigma)|"
     r"six sigma|scaled agile|safe product owner|backlog refinement|product backlog"),
    ("requirements and prd", "product",
     r"(functional|non functional|nonfunctional|product|software|system|user|technical|business|client|project|"
     r"accessibility|application) requirement|requirements (gathering|analysis|elicitation|management|matrix|"
     r"document|doc|definition|questions|meeting|txt)|requirement specification|requirements vs|\bprd\b|"
     r"define the requirements|requirement document|design spec|design brief|draft requirements"),
    ("prioritization", "product",
     r"prioriti[sz]|priority matrix|priority levels|priority list|priority management|must.?have|moscow|"
     r"\brice\b|ice score|eisenhower|top priority|high priority|priorities examples|examples of priorit"),
    ("project management", "product",
     r"project manag|project manager|program manager|project (plan|scope|charter|timeline|milestones?|phases|"
     r"life ?cycle|constraints|controls|portfolio|board|success|mapping|requirements)|\bwbs\b|critical path|"
     r"\bevm\b|deliverables|triple constraint|\bpmi\b|milestone|project management office"),
    ("product management, strategy and roadmaps", "product",
     r"roadmap|product strategy|product vision|product positioning|product differentiation|positioning|"
     r"product.market fit|mvp|minimum viable|product development|product life ?cycle|product lifecycle|"
     r"new product|product launch|launch formula|formula launch|product discovery|innovation discovery|"
     r"product engineering|product architecture|product manag|product owner|product operations|"
     r"product analyst|data as a product|product led|product-oriented|product science"),
    ("okrs, kpis and metrics", "business",
     r"\bokrs?\b|\bkpis?\b|\bmetrics\b|north star|vanity metric|key metric"),
    ("retention, churn and engagement", "business",
     r"customer retention|retention (rate|metrics|strateg|ratio|examples|program|plan)|\bchurn|cohort|"
     r"player retention|long term retention|view retention|acquisition vs retention|user retention|"
     r"(customer|employee) engagement|engagement (rate|strategy|formula)|active user|loyalty program|"
     r"onboarding|retention of employees"),
    ("a/b testing and experimentation", "business",
     r"\ba/?b test|split test|experiment|conversion rate|\bcro\b|hypothes"),
    ("pricing strategy", "business", r"pricing|\bprice\b"),
    ("go-to-market and product marketing", "business",
     r"go to market|go-to-market|\bgtm\b|product marketing|market product|product market|marketing mix|"
     r"4 ?ps|four ps|4 p's|price place promotion|segmentation|target market|distribution channel"),
    ("market research and competitor analysis", "business",
     r"market research|marketing research|competitive analysis|competitor analysis|competitive"),
    ("analytics", "business",
     r"analytics|data analyst|analytic|web analytics|business intelligence"),
    ("growth marketing and funnels", "business",
     r"growth|funnel|marketing strateg|inbound|outbound|content marketing|performance marketing|"
     r"account based|attribution|marketing automation|marketing channels|marketing objectives"),
    ("marketing (general)", "other", r"marketing|marketer"),
    ("surveys and questionnaires", "design",
     r"survey|questionnaire|open.ended|closed.ended|close.ended|dichotomous|semi.structured"),
    ("ux research, personas and journeys", "design",
     r"\bpersonas?\b|persona-|journey map|customer journey|user journey|user flow|ux flow|journey mapping|service blueprint|"
     r"customer experience|cx|ux research|user research|usability|user testing|user interview|"
     r"research method|qualitative|quantitative (research|data|survey)|research question|card sort|focus group|user feedback|"
     r"exploratory research|action research|user acceptance testing|ux survey|research methodology"),
    ("design systems and ui components", "design",
     r"design system|material.?ui|material design|ant design|fluent ui|shadcn|carbon design|swift ?ui|"
     r"\bui (badge|banner|bootstrap|pills?|profile|sides|steppers|toast|datepicker|kit|components?)|"
     r"(badge|badges|banner|banners|chips?|pagination|stepper|steppers|spinners|popovers|dialogs|carousel|"
     r"filter|form|notification|tabs|tagging|coachmark|breadcrumbs|chat|call|faq|leaderboard|profile|"
     r"star rating|rating slider|drop shadow|footnote|inline help|search bar|search box|search field) "
     r"(ui|ux|design)|design patterns?|component"),
    ("ux and ui design (discipline)", "design",
     r"\bux\b|\bui\b|ui/ux|user experience|user interface|interaction design|product design|"
     r"information architecture"),
    ("design thinking and principles", "design",
     r"design thinking|human centered|human-centered|design principles|principles of design|"
     r"elements of design|design elements|design process|universal design|design inspiration|"
     r"design of everyday things"),
    ("web design and accessibility", "design",
     r"web design|website design|design a website|accessib|\bwcag\b|\bada\b|responsive design|"
     r"website design|website examples"),
    ("graphic and visual design", "other",
     r"graphic design|logo|poster|flyer|banner design|brochure|t ?shirt|tshirt|business card|packaging design|"
     r"motion design|layout design|menu design|character design|typography|font"),
    ("system and software design", "other",
     r"system design|software design|software architecture|systems analysis|design patterns|domain driven|"
     r"architecture framework|microservices|software development|app development|application development"),
    ("ai tools", "other", r"\bai\b|chatbot|gpt|gemini|copilot|llm|prompt"),
    ("seo and keyword research", "other", r"\bseo\b|keyword research|keyword"),
    ("customer service", "other", r"customer service|customer support|service management|field service"),
    ("stakeholder and change management", "product",
     r"stakeholder|change management|management style|leadership|team management"),
    ("jobs to be done", "product", r"jobs to be done|\bjtbd\b|job to be done"),
    ("service design", "design", r"service design|service blueprint"),
    ("design (general)", "design", r"\bdesign"),
]

DECISION = ["how", "vs", "versus", "best", "examples", "template", "checklist", "framework", "calculator",
            "tool", "tools", "guide", "which", "should"]
STOP = set("a an and the of to for in on is are what how why which with by vs versus or do does at from as "
           "it its be your you my our i me this that these those can should will".split())
GENERIC = STOP | set("product products design designs user users guide best examples example meaning "
                     "definition free online top tools tool what new management software ux ui one services companies company".split())
MIN_KW = 20


def tokens(s):
    return re.findall(r"[a-z0-9]+", s.lower().replace("a/b", "ab"))


def median(xs):
    return statistics.median(xs) if xs else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default="2026-10-08")
    args = ap.parse_args()
    kwdir = os.path.join(SEO, "keywords")
    with open(os.path.join(kwdir, "harvest-articles-%s.csv" % args.date), encoding="utf-8", newline="") as fh:
        rows = [r for r in csv.DictReader(fh) if not r.get("flag_v1_1", r["flag"]) and int(r["volume"] or 0) >= 100]  # v1.1 flags (see harvest.old_flag)
    compiled = [(t, d, re.compile(p)) for t, d, p in RULES]
    groups = collections.OrderedDict((t, []) for t, _, _ in RULES)
    dom = {t: d for t, d, _ in RULES}
    unassigned = []
    for r in rows:
        kw = r["keyword"]
        for t, _, rx in compiled:
            if rx.search(kw):
                groups[t].append(r)
                break
        else:
            unassigned.append(r)
    small = {t: g for t, g in groups.items() if len(g) < MIN_KW}
    for t, g in small.items():
        unassigned.extend(g)
    topics = {t: g for t, g in groups.items() if len(g) >= MIN_KW}

    # corpus token document frequency
    df = collections.Counter()
    for r in rows:
        df.update(set(tokens(r["keyword"])))
    n_all = len(rows)

    # sitemap content slugs
    slugs = []
    for f in glob.glob(os.path.join(SEO, "competitors", "sitemaps", "*-sitemap-%s.csv" % args.date)):
        with open(f, encoding="utf-8", newline="") as fh:
            for s in csv.DictReader(fh):
                if s.get("content") == "content":
                    slugs.append((s["domain"], set(tokens(s.get("slug_tokens") or ""))))

    out_rows = []
    for t, g in topics.items():
        vols = [int(r["volume"]) for r in g]
        kds = [float(r["difficulty"]) for r in g if r["difficulty"] != ""]
        dec = sum(1 for r in g if set(tokens(r["keyword"])) & set(DECISION) or "versus" in r["keyword"])
        top = sorted(g, key=lambda r: -int(r["volume"]))[:8]
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
        out_rows.append({
            "topic": t, "domain_guess": dom[t], "keyword_count": len(g), "total_volume": sum(vols),
            "median_volume": int(median(vols)), "median_difficulty": ("%g" % median(kds)) if kds else "",
            "decision_share": "%.2f" % (dec / len(g)),
            "top_keywords": ";".join(r["keyword"] for r in top),
            "competitor_articles": len(hits), "competitor_domains": len(set(hits)),
            "_tokens": " ".join(distinct)})
    out_rows.sort(key=lambda r: -r["total_volume"])
    cols = ["topic", "domain_guess", "keyword_count", "total_volume", "median_volume", "median_difficulty",
            "decision_share", "top_keywords", "competitor_articles", "competitor_domains"]
    with open(os.path.join(kwdir, "topic-candidates-%s.csv" % args.date), "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(out_rows)
    with open(os.path.join(kwdir, "keyword-to-topic-%s.csv" % args.date), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["keyword", "topic"])
        for t, g in topics.items():
            for r in g:
                w.writerow([r["keyword"], t])
        for r in unassigned:
            w.writerow([r["keyword"], "unassigned"])

    print("clustered %d keywords: %d topics, %d unassigned" % (len(rows), len(topics), len(unassigned)))
    for r in out_rows:
        print("%-42s %-8s n=%4d vol=%8d medKD=%s dec=%s comp=%d/%d tokens=[%s]" % (
            r["topic"], r["domain_guess"], r["keyword_count"], r["total_volume"], r["median_difficulty"],
            r["decision_share"], r["competitor_articles"], r["competitor_domains"], r["_tokens"]))
    print("small rule groups (to unassigned):", {t: len(g) for t, g in small.items()})
    # largest unassigned word groups (unigram and bigram, stopwords out)
    grp = collections.Counter()
    gvol = collections.Counter()
    for r in unassigned:
        tk = [x for x in tokens(r["keyword"])]
        keys = set(x for x in tk if x not in STOP and len(x) > 1)
        keys |= set(" ".join(b) for b in zip(tk, tk[1:]) if b[0] not in STOP and b[1] not in STOP)
        for k in keys:
            grp[k] += 1
            gvol[k] += int(r["volume"])
    print("unassigned groups:", "; ".join("%s (%d kw, %d vol)" % (k, c, gvol[k]) for k, c in grp.most_common(40)))


if __name__ == "__main__":
    main()
