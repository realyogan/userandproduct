"""Writes article-a.html, article-b.html and article-c.html from one copy of the sample article.

The pages are plain static HTML; this script only keeps the three variants in step.
Run: python build.py
"""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

TITLE = "How to Write a PRD That Engineers Actually Read"
DECK = ("Most product requirement documents get read once, in the kickoff, and never opened again. "
        "After fifteen years of writing them and watching engineers scroll past mine, I now answer twelve "
        "questions before I write a heading, keep the document to a few screens, and end it with lines a "
        "tester can check. Here is the structure, a worked example, and a template you can use today.")
DESC = "The PRD structure I have used for fifteen years: twelve questions, six parts, acceptance lines a tester can check, and a free template."

# ---------------------------------------------------------------- shared bits

ICON_MOON = ('<svg class="i-moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" '
             'd="M20.3 14.6A8.5 8.5 0 0 1 9.4 3.7a8.5 8.5 0 1 0 10.9 10.9Z"/></svg>')
ICON_SUN = ('<svg class="i-sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.5" '
            'fill="currentColor"/><g stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 2v2.5M12 19.5V22M2 12h2.5M19.5 12H22M4.9 4.9l1.8 1.8M17.3 17.3l1.8 1.8M4.9 19.1l1.8-1.8M17.3 6.7l1.8-1.8"/></g></svg>')
TOGGLE = f'<button class="theme-toggle" type="button" data-theme-toggle aria-label="Switch theme">{ICON_MOON}{ICON_SUN}</button>'

def logo(w, h):
    return ('<a class="logo" href="#" aria-label="userandproduct home">'
            f'<img class="l-light" src="../final-logo/svg/lockup-light.svg" alt="userandproduct" width="{w}" height="{h}">'
            f'<img class="l-dark" src="../final-logo/svg/lockup-dark.svg" alt="userandproduct" width="{w}" height="{h}">'
            '</a>')

LOGO = logo(236, 30)       # header: CSS sets 236px from 768px, 168px on phones
LOGO_FOOT = logo(168, 21)  # footer stays at 168px

SECTIONS_NAV = ["Articles", "Topics", "Books", "Links", "Tools", "Templates"]

def nav_items():
    return "".join(f'<li><a href="#">{s}</a></li>' for s in SECTIONS_NAV)

def avatar(size, title="Photo of [Author Name] (placeholder)"):
    return (f'<svg class="avatar" width="{size}" height="{size}" viewBox="0 0 64 64" role="img"><title>{title}</title>'
            '<circle cx="32" cy="25" r="11" fill="currentColor"/>'
            '<path d="M11 56c2.5-11 11-17 21-17s18.5 6 21 17Z" fill="currentColor"/></svg>')

def head(variant, label, preload_serif=False):
    pre = ('<link rel="preload" href="../fonts/inter/Inter-Regular.woff2" as="font" type="font/woff2" crossorigin>\n'
           '<link rel="preload" href="../fonts/inter/InterDisplay-Bold.woff2" as="font" type="font/woff2" crossorigin>\n')
    if preload_serif:
        pre = ('<link rel="preload" href="../fonts/fraunces/Fraunces9pt-Regular.woff2" as="font" type="font/woff2" crossorigin>\n'
               '<link rel="preload" href="../fonts/inter/InterDisplay-Bold.woff2" as="font" type="font/woff2" crossorigin>\n')
    return f"""<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITLE} | userandproduct</title>
<meta name="description" content="{DESC}">
<meta name="robots" content="noindex">
<meta name="theme-color" content="#2B46A0">
<link rel="icon" href="../final-logo/favicon/favicon.ico" sizes="48x48">
<link rel="icon" href="../final-logo/favicon/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="../final-logo/favicon/apple-touch-icon-180.png">
<script>try{{var t=localStorage.getItem("uap-theme");if(t==="dark"||t==="light"){{document.documentElement.setAttribute("data-theme",t)}}}}catch(e){{}}</script>
{pre}<link rel="stylesheet" href="../mockup.css">
<link rel="stylesheet" href="article.css">
<script src="../mockup.js" defer></script>
</head>
<!-- Mockup variant {variant}: {label} -->
"""

def site_header():
    return f"""<header class="site-head">
  <div class="site-head__in">
    {LOGO}
    <nav class="site-nav" aria-label="Sections"><ul>{nav_items()}</ul></nav>
    <details class="menu"><summary>Menu</summary><ul>{nav_items()}</ul></details>
    {TOGGLE}
  </div>
</header>"""

def footer():
    return f"""<footer class="site-foot">
  <div class="site-foot__in">
    <div class="site-foot__brand">
      {LOGO_FOOT}
      <p>Practical writing on UX, product management and the business decisions between them, from fifteen years of shipping software.</p>
    </div>
    <nav aria-label="Domains">
      <h2>Domains</h2>
      <ul><li><a href="#">Design</a></li><li><a href="#">Product</a></li><li><a href="#">Business</a></li></ul>
    </nav>
    <nav aria-label="Site sections">
      <h2>Sections</h2>
      <ul>{nav_items()}</ul>
    </nav>
    <div class="legal">
      <span>&copy; 2026 userandproduct</span>
      <a href="#">About</a><a href="#">Privacy</a><a href="#">Advertising policy</a><a href="#">Contact</a>
    </div>
  </div>
</footer>"""

def crumbs():
    return """<nav class="crumbs" aria-label="Breadcrumb"><ol>
      <li><a href="#">Home</a></li><li><a href="#">Product</a></li><li><a href="#" aria-current="page">Product discovery</a></li>
    </ol></nav>"""

def byline(size=44):
    return f"""<div class="byline">
      {avatar(size)}
      <div>
        <div>userandproduct, by <a href="#author"><strong>[Author Name]</strong></a></div>
        <div class="when"><span><time datetime="2026-10-09">9 Oct 2026</time></span><span>9 min read</span></div>
      </div>
    </div>"""

# ---------------------------------------------------------------- images

def themed_img(light, dark, alt, w, h, cls="", hero=False):
    """A picture whose dark source follows the system theme; mockup.js re-points it when the reader toggles."""
    load = 'fetchpriority="high"' if hero else 'loading="lazy"'
    return (f'<picture><source srcset="{dark}" media="(prefers-color-scheme: dark)" data-dark>'
            f'<img class="{cls}" src="{light}" width="{w}" height="{h}" alt="{alt}" {load} decoding="async"></picture>')

HERO = f"""<figure class="hero-fig">
      {themed_img("img/hero-prd-light.png", "img/hero-prd-dark.png", "Illustration: a PRD page with twelve question lines, three of them marked in blue, beside four blue tiles", 1200, 675, hero=True)}
      <figcaption>Twelve questions before the first heading. Questions 7, 9 and 12 do most of the work.</figcaption>
    </figure>"""

# ---------------------------------------------------------------- ad slots
# Google allows only "Advertisements" or "Sponsored Links" as the label above an ad unit.
AD_LABEL = "Advertisements"

def ad(kind, name):
    sizes = {
        "leader": ('<span class="sz-0">320 &times; 100</span><span class="sz-1">728 &times; 90</span>'
                   '<span class="sz-2">970 &times; 90</span>'),
        "rect": '<span class="sz-0">336 &times; 280</span>',
        "side": '<span class="sz-0">300 &times; 250</span>',
        "half": '<span class="sz-0">300 &times; 600 half page</span>',
        "sky": '<span class="sz-0">160 &times; 600</span><span class="sz-1">300 &times; 600 half page</span>',
    }[kind]
    return (f'<aside class="ad ad--{kind}" data-ad="{name}" aria-label="Advertisement">'
            f'<span class="ad__label">{AD_LABEL}</span><div class="ad__box">{sizes}</div></aside>')

ANCHOR = f"""<aside class="anchor" data-ad="anchor" data-anchor data-anchor-until=".tpl" aria-label="Advertisement">
  <div class="anchor__bar"><span class="ad__label">{AD_LABEL}</span>
  <button class="anchor__toggle" type="button" data-anchor-toggle aria-expanded="true">Hide ad</button></div>
  <div class="ad__box"><span class="sz-0">320 &times; 50 anchor</span></div>
</aside>"""

# ---------------------------------------------------------------- figures

def fig_structure():
    rows = [("1", "Problem and why", 12, "why"), ("2", "Users and evidence", 10, "why"),
            ("3", "Scope: in and out", 14, "build"), ("4", "Flows and states", 30, "build"),
            ("5", "Acceptance lines", 22, "build"), ("6", "Open questions", 12, "build")]
    out = []
    y = 16
    for n, label, pct, grp in rows:
        w = round(pct / 30 * 180)
        cls = "svg-ink-3" if grp == "why" else "svg-signal"
        out.append(f'<text x="0" y="{y + 16}" class="svg-tb svg-ink">{n}</text>'
                   f'<text x="22" y="{y + 16}" class="svg-t svg-ink">{label}</text>'
                   f'<rect x="172" y="{y + 2}" width="{w}" height="20" rx="3" class="{cls}"/>'
                   f'<text x="{172 + w + 8}" y="{y + 17}" class="svg-ts svg-ink-3">{pct}%</text>')
        y += 42
    ly = y + 14
    legend = (f'<rect x="0" y="{ly}" width="14" height="14" rx="2" class="svg-ink-3"/>'
              f'<text x="22" y="{ly + 12}" class="svg-ts svg-ink-2">Why: fits on one screen</text>'
              f'<rect x="200" y="{ly}" width="14" height="14" rx="2" class="svg-signal"/>'
              f'<text x="220" y="{ly + 12}" class="svg-ts svg-ink-2">What to build</text>')
    h = ly + 22
    return f"""<figure class="fig" id="fig-structure">
  <div class="frame">
  <svg viewBox="0 0 400 {h}" role="img" aria-labelledby="f1t f1d">
    <title id="f1t">The six parts of the PRD</title>
    <desc id="f1d">A bar chart of the six parts in order with the share of a typical four-screen PRD: problem and why 12 percent, users and evidence 10, scope 14, flows and states 30, acceptance lines 22, open questions 12. The first two parts are the why and fit on one screen; the last four describe what to build.</desc>
    {''.join(out)}{legend}
  </svg>
  </div>
  <figcaption><b>Figure 1.</b> The six parts, always in this order, with the share of a typical four-screen PRD each one takes. The why fits on one screen; most of the length goes to flows and acceptance lines.</figcaption>
</figure>"""

def fig_readers():
    cols = [("Engineers", 196), ("Design", 256), ("QA", 310), ("Leads", 364)]
    rows = [("Problem and why", "rfrf"), ("Users and evidence", "rfdf"), ("Scope: in and out", "fffr"),
            ("Flows and states", "fffd"), ("Acceptance lines", "frfd"), ("Open questions", "ffrf")]
    out = [f'<text x="{x}" y="22" text-anchor="middle" class="svg-ts svg-ink-2">{c}</text>' for c, x in cols]
    out.append('<line x1="0" y1="36" x2="400" y2="36" class="svg-line" stroke-width="1"/>')
    y = 64
    for label, marks in rows:
        out.append(f'<text x="0" y="{y + 5}" class="svg-t svg-ink">{label}</text>')
        for (c, x), m in zip(cols, marks):
            if m == "f":
                out.append(f'<circle cx="{x}" cy="{y}" r="8" class="svg-signal"/>')
            elif m == "r":
                out.append(f'<circle cx="{x}" cy="{y}" r="7" fill="none" class="svg-sig-stroke" stroke-width="2"/>')
            else:
                out.append(f'<circle cx="{x}" cy="{y}" r="2.5" class="svg-ink-3"/>')
        out.append(f'<line x1="0" y1="{y + 20}" x2="400" y2="{y + 20}" class="svg-rule" stroke-width="1"/>')
        y += 40
    ly = y + 8
    out.append(f'<circle cx="8" cy="{ly}" r="7" class="svg-signal"/><text x="22" y="{ly + 4}" class="svg-ts svg-ink-2">Reads closely</text>'
               f'<circle cx="122" cy="{ly}" r="6" fill="none" class="svg-sig-stroke" stroke-width="2"/><text x="135" y="{ly + 4}" class="svg-ts svg-ink-2">Skims</text>'
               f'<circle cx="196" cy="{ly}" r="2.5" class="svg-ink-3"/><text x="206" y="{ly + 4}" class="svg-ts svg-ink-2">Usually skips</text>')
    h = ly + 14
    return f"""<figure class="fig" id="fig-readers">
  <div class="frame">
  <svg viewBox="0 0 400 {h}" role="img" aria-labelledby="f2t f2d">
    <title id="f2t">Who reads which part</title>
    <desc id="f2d">A grid of the six PRD parts against four readers. Engineers and QA read scope, flows and acceptance lines closely and the why once. Design reads most parts closely. Leads read the problem, the evidence and the open questions closely, skim scope and usually skip flows and acceptance lines.</desc>
    {''.join(out)}
  </svg>
  </div>
  <figcaption><b>Figure 2.</b> Who reads which part. The fixed order means nobody has to read the whole document to do their job.</figcaption>
</figure>"""

# ---------------------------------------------------------------- the article

QUESTIONS = [
    ("What problem are we solving, in one sentence?", "It is the test for every later trade-off."),
    ("Who has this problem, and how often?", "It tells them which paths are busy and which are rare."),
    ("What do they do today instead?", "The workaround is the real competitor, and often half the spec."),
    ("What evidence do we have?", "It separates a known need from a guess."),
    ("What does success look like, and how will we measure it?", "It decides what has to be logged from day one."),
    ("What is in scope for this release?", "It is the list they will estimate against."),
    ("What is explicitly out of scope?", "It stops quiet scope creep in code review."),
    ("What are the main flows, step by step?", "It is the skeleton for tickets and tests."),
    ("What happens when things go wrong or are empty?", "Error, empty and loading states are where estimates break."),
    ("What are the constraints?", "Deadlines, platforms, legal review and performance budgets."),
    ("What are the acceptance lines?", "It is the definition of done a tester can check."),
    ("What is still open, and who decides?", "It shows them where not to build yet."),
]

def qtable():
    rows = "".join(f"<tr><td>{i}</td><td>{q}</td><td>{w}</td></tr>" for i, (q, w) in enumerate(QUESTIONS, 1))
    return f"""<div class="qtable-wrap">
<table class="qtable">
  <caption>The twelve questions. I answer them in a scratch file before I write a single heading.</caption>
  <thead><tr><th scope="col"><span class="vh">Number</span></th><th scope="col">Question</th><th scope="col">Why engineers care</th></tr></thead>
  <tbody>{rows}</tbody>
</table>
</div>"""

EXCERPT = """<div class="excerpt" role="group" aria-label="Excerpt from the saved filters PRD">
  <p class="ex-title">Saved filters, v1 (excerpt)</p>
  <dl>
    <dt>Problem</dt><dd>Analysts rebuild the same five to eight filters every Monday before the weekly review. It is the most common "how do I" ticket in the reporting area.</dd>
    <dt>In scope</dt><dd><ul><li>Save the current filters under a name.</li><li>Apply a saved filter from the filter bar.</li><li>Rename and delete your own saved filters.</li></ul></dd>
    <dt>Out of scope</dt><dd><ul><li>Sharing saved filters with teammates (v2).</li><li>Scheduled reports.</li><li>Filters on dashboards.</li></ul></dd>
    <dt>Empty state</dt><dd>A user with no saved filters sees "Save the filters you use most" and the Save button, nothing else.</dd>
    <dt>Acceptance</dt><dd>Given a user has applied three filters, when they choose Save and enter a name, then the name appears in the saved list, and applying it restores all three filters exactly.</dd>
  </dl>
</div>"""

PULL = """<blockquote class="pull"><p>A PRD is not a record of everything you know. It is the smallest set of decisions an engineer needs to build the right thing without having to ask you.</p></blockquote>"""

SECTIONS = [
    ("why-prds-fail", "Why most PRDs fail", f"""
<p>I have written well over two hundred PRDs, and for the first five years most of them were read exactly once: in the kickoff meeting, on a shared screen, while I scrolled. After that the engineers worked from the tickets, the design file and whatever they remembered me saying. The document was out of date by the second sprint, and nobody noticed, because nobody opened it.</p>
<p>That is not an engineering problem. It is a writing problem, and it usually has one of two causes.</p>
<h3 id="written-for-approval">It was written for approval, not for building</h3>
<p>Many PRDs are pitch decks in prose. They open with market size, competitor screenshots and a strategy paragraph, because the first reader the author had in mind was a VP who needed convincing. By the time an engineer reaches the part they need, which is what to build and how they will know it works, they are on page four and have started skimming.</p>
<h3 id="wall-of-text">It answers questions nobody asked and skips the ones they did</h3>
<p>The other failure is the wall of text. Every edge case the PM thought of is in there, in the order they thought of it. What is missing is the short list of decisions: what is in scope, what is not, what happens when the data is empty, who sees the error message. Engineers do not need more words. They need the decisions made, in a place they can find them.</p>
@@FIG_FAIL@@
{PULL}
"""),
    ("twelve-questions", "The twelve questions to answer first", f"""
<p>Before I write a single heading, I answer twelve questions in plain sentences, in a scratch file. If I cannot answer one, that is the first thing I go and find out, not something I paper over in the document. Most of the PRD then writes itself from the answers.</p>
{qtable()}
<p>Questions 7, 9 and 12 do most of the work. They are the ones skipped most often, and they are the ones engineers ask about in the ticket thread three weeks later, when changing course costs real time.</p>
"""),
    ("structure", "The structure that works", f"""
<p>Once the answers exist, the document has six parts, always in the same order. Keeping the order fixed matters more than the headings themselves: an engineer who has read one of my PRDs knows where to look in the next one.</p>
@@FIG_STRUCTURE@@
<h3 id="one-screen">One screen for the why</h3>
<p>Problem, users and evidence fit on one screen, or they are not finished. This is the part leadership reads, and it is also the part engineers need to judge edge cases on their own. If the why takes three pages, the team cannot hold it in their heads, and they stop using it to make the small calls that never reach a meeting.</p>
<h3 id="scope-as-a-list">Scope as a list, not a story</h3>
<p>In scope and out of scope are two short lists, side by side if the tool allows it. Each line is short enough to become a ticket title. Out of scope gets as much care as in scope, because it is the list that protects the estimate.</p>
<p>Flows come next, written as numbered steps with the system's response on each step, then acceptance lines, then open questions. That is the whole document. For a mid-sized feature it runs three to five screens.</p>
"""),
    ("worked-example", "A worked example", f"""
<p>Here is a short excerpt from a real PRD, with the product details changed. The feature let analysts in a B2B reporting tool save a set of filters and reuse it. The first draft was eleven pages. This version is four screens, and it is the one the team built from.</p>
{EXCERPT}
<p>Every PRD I write opens with a few lines of front matter, so the team's tracker can read the status, the owner and the decision date without anyone opening the document:</p>
<pre data-filename="saved-filters.prd.json"><code class="language-json">{{
  "title": "Saved filters, v1",
  "owner": "[Author Name]",
  "status": "In review",
  "version": 3,
  "decisionBy": "2026-10-23",
  "openQuestions": 2,
  "links": {{
    "brief": "https://wiki.example.com/briefs/saved-filters",
    "design": "https://design.example.com/files/saved-filters"
  }}
}}</code></pre>
<p>Notice what is not in the excerpt: no market sizing, no persona poster, no competitor screenshot. Those existed, in a separate one-page brief for leadership, and the PRD links to it in one line.</p>
@@FIG_READERS@@
"""),
    ("acceptance", "Acceptance lines and open questions", """
<h3 id="tester-can-check">Write acceptance lines a tester can check</h3>
<p>An acceptance line describes something a person can observe, in a given state, after an action. "Saved filters should be easy to use" is a wish. "Applying a saved filter restores every filter exactly as saved, including date ranges" is a line someone can test. I use Given, When, Then when the starting state matters and a plain sentence when it does not. I aim for five to twelve lines per feature; more than that usually means the feature should be split.</p>
<p>Success measures get the same treatment. For saved filters the measure was a query the analytics team could run from the first day of the release, written into the PRD next to the acceptance lines:</p>
<pre data-caption="The success measure from the saved filters PRD: the weekly share of active analysts who applied a saved filter."><code class="language-sql">-- weekly share of active analysts who applied a saved filter
SELECT date_trunc('week', e.created_at) AS week,
       COUNT(DISTINCT e.user_id) FILTER (WHERE e.name = 'saved_filter_applied') * 100.0
         / COUNT(DISTINCT e.user_id) AS pct_using_saved_filters
FROM events e
WHERE e.created_at &gt;= '2026-01-01'
  AND e.role = 'analyst'
GROUP BY 1
ORDER BY 1;</code></pre>
<h3 id="open-questions">Keep open questions in the open</h3>
<p>Every PRD I write ends with a short table of open questions, each with an owner and a date. After the scope lists it is the most-read part, because it tells engineers where not to build yet. Hiding an open question in a paragraph does not close it. It moves the discussion to a pull request, where it costs more.</p>
<p>Anything nobody has decided yet is marked <code>TBD</code> in the body, never guessed. Before a review I count what is still open across every PRD in the repository:</p>
<pre><code class="language-bash"># list every TBD left in the PRDs, with file and line, then count them
grep -rn "TBD" docs/prd/ | sort | tee open-items.txt | wc -l</code></pre>

"""),
    ("leave-out", "What to leave out", """
<p>The fastest way to get a PRD read is to make it shorter. These are the things I take out, or move somewhere else and link:</p>
<ul>
  <li><strong>Market research and competitor reviews.</strong> They belong in the brief that got the project approved.</li>
  <li><strong>Screen detail the designer owns.</strong> Link the design file; do not describe the screens in prose.</li>
  <li><strong>Implementation choices.</strong> Say what must be true, not how to build it. The engineers will pick a better approach than the one you would have written.</li>
  <li><strong>History.</strong> How the idea came up, who asked for it, the three earlier attempts. One line, if any.</li>
  <li><strong>Every edge case at the same weight.</strong> Name the ones that change the estimate and leave the rest to the team and the acceptance lines.</li>
</ul>
<p>What remains is short, a little plain, and used every day of the build. That is the only measure of a PRD that matters.</p>
"""),
]

INTERVIEW_TEXT = """PRD interview, v1.0, by [Author Name], userandproduct.com/prd-template (CC BY 4.0)

You are helping me write a product requirements document (PRD). Work in two steps.

Step 1, the interview. Ask me these twelve questions one at a time, in order. Wait for my answer before you ask the next one. If an answer is vague, ask one follow-up that makes it specific. If I paste my company's PRD template, keep its headings and use these questions to fill them.
1. What problem are we solving, in one sentence?
2. Who has this problem, and how often?
3. What do they do today instead?
4. What evidence do we have?
5. What does success look like, and how will we measure it?
6. What is in scope for this release?
7. What is explicitly out of scope?
8. What are the main flows, step by step?
9. What happens when things go wrong or are empty?
10. What are the constraints?
11. What are the acceptance lines?
12. What is still open, and who decides?

Step 2, the draft. Write the PRD in six parts: Problem and why, Users and evidence, Scope (in and out), Flows and states, Acceptance lines, Open questions. Keep the why to one screen. Write acceptance lines a tester can check. Mark anything I did not tell you as TBD. Do not invent facts, numbers or names.

Check my draft mode: if I start by pasting an existing PRD instead, skip the interview. Check the draft against the twelve questions, list what is missing or vague, and suggest specific fixes.

End the PRD with: "Structured with the PRD interview, userandproduct.com/prd-template". I may delete this line."""

def template_block(tid="template"):
    return f"""<section class="tpl" aria-labelledby="{tid}">
  <h2 id="{tid}">Get the PRD template</h2>
  <p>Three ways to use this structure. All free, no sign-up.</p>
  <div class="tpl__grid">
    <div class="tpl__part">
      <h3>Blank template</h3>
      <p>The six parts and the twelve questions, ready to fill in. Works in Word and Google Docs.</p>
      <div class="btn-row"><a class="btn" href="#" download>Download .docx</a><a class="btn btn--ghost" href="#">Open in Google Docs</a></div>
      <p class="small">Also as <a href="#">Markdown</a>.</p>
    </div>
    <div class="tpl__part">
      <h3>Worked example</h3>
      <p>The full saved-filters PRD from this article, with the answers to the twelve questions that produced it.</p>
      <div class="btn-row"><a class="btn btn--ghost" href="#">See the worked example</a></div>
    </div>
    <div class="tpl__part tpl__part--wide">
      <h3>PRD interview</h3>
      <p class="lead">Paste this into ChatGPT or Claude. It interviews you for about 10 minutes, then drafts your PRD. You review it.</p>
      <p>It drafts. You decide. Anything you didn't tell it is marked TBD, not made up. Already have a draft? Paste it instead and the same text checks it against the twelve questions.</p>
      <div class="btn-row"><button class="btn" type="button" data-copy="prd-interview-text" data-copy-status="copy-status">Copy the interview</button><a class="btn btn--ghost" href="#" download>Download .txt</a></div>
      <p class="copy-status" id="copy-status" role="status" aria-live="polite"></p>
      <div class="before">
        <h4>Before you paste</h4>
        <ul>
          <li>Use only the assistant your employer approves. If it allows none, use the blank template instead.</li>
          <li>Swap customer names, revenue figures, unreleased product names and personal data for placeholders such as [Customer A] and [$X].</li>
          <li>Turn off chat history or training where your assistant allows it.</li>
        </ul>
      </div>
      <textarea id="prd-interview-text" hidden readonly>{INTERVIEW_TEXT}</textarea>
    </div>
  </div>
</section>"""

AUTHOR = f"""<section class="author" id="author" aria-labelledby="author-h">
  {avatar(64)}
  <div>
    <h2 id="author-h">[Author Name]</h2>
    <p>Fifteen years in product design and product management, shipping B2B and consumer software with teams from five people to five hundred. I write userandproduct to share the methods that held up in real teams, and the ones that did not.</p>
    <div class="links"><a href="#">[Author Name] on LinkedIn</a><a href="#">About the author</a></div>
  </div>
</section>"""

RELATED = f"""<section class="related" aria-labelledby="related-h">
  <h2 id="related-h">Related</h2>
  <ul>
    <li><a class="rel-thumb" href="#" tabindex="-1" aria-hidden="true">{themed_img("img/related-user-stories.png", "img/related-user-stories-dark.png", "Three stacked story cards, the last one marked in blue", 600, 338)}</a><div class="rel-body"><span class="cat">Product discovery</span><h3><a href="#">User stories that survive sprint planning</a></h3><p>Why most stories get rewritten in the room, and the three lines that stop it.</p><p class="rt">8 min read</p></div></li>
    <li><a class="rel-thumb" href="#" tabindex="-1" aria-hidden="true">{themed_img("img/related-discovery-plan.png", "img/related-discovery-plan-dark.png", "A two-week grid with five days filled in blue", 600, 338)}</a><div class="rel-body"><span class="cat">Product discovery</span><h3><a href="#">The discovery plan I run in the first two weeks</a></h3><p>Interviews, data pulls and one decision memo, day by day.</p><p class="rt">11 min read</p></div></li>
    <li><a class="rel-thumb" href="#" tabindex="-1" aria-hidden="true">{themed_img("img/related-usability-test.png", "img/related-usability-test-dark.png", "Five user figures, the fifth in blue", 600, 338)}</a><div class="rel-body"><span class="cat">UX research</span><h3><a href="#">How many users do you need for a usability test?</a></h3><p>Five is a starting point, not a rule. When to test more, and when fewer will do.</p><p class="rt">7 min read</p></div></li>
  </ul>
</section>"""

RELATED_A = """<section class="rel2" aria-labelledby="rel2-h">
  <h2 id="rel2-h" class="rel2__h">// Related</h2>
  <ul>
    <li><a href="#"><img src="img/user-stories-thumb.png" width="600" height="338" alt="" loading="lazy" decoding="async"><span class="chips"><span>Discovery</span><span>User stories</span></span><h3>User stories that survive sprint planning</h3></a></li>
    <li><a href="#"><img src="img/discovery-plan-thumb.png" width="600" height="338" alt="" loading="lazy" decoding="async"><span class="chips"><span>Discovery</span></span><h3>The discovery plan I run in the first two weeks</h3></a></li>
    <li><a href="#"><img src="img/usability-test-thumb.png" width="600" height="338" alt="" loading="lazy" decoding="async"><span class="chips"><span>UX research</span></span><h3>How many users do you need for a usability test?</h3></a></li>
  </ul>
</section>"""

NEWS = """<section class="news" id="newsletter" aria-labelledby="news-h">
  <h2 id="news-h" class="vh">Newsletter</h2>
  <form data-news>
    <label for="news-email"><b>One email a month</b> with new articles and templates. Unsubscribe any time.</label>
    <div class="field"><input id="news-email" type="email" name="email" autocomplete="email" placeholder="you@example.com" required><button class="btn" type="submit">Subscribe</button></div>
    <p class="status" role="status" aria-live="polite"></p>
  </form>
</section>"""

READERS_PARA = "<p>The grid is the reason the order works. Engineers and QA read the bottom half closely and the top half once. Leadership reads the top half and the open questions and skims the rest.</p>"

def figures(kind):
    """kind "inline": the original inline SVG figures (B and C); "frame": the plain illustration PNGs (A)."""
    if kind == "frame":
        import figures as F
        return {"@@FIG_STRUCTURE@@": F.fig_questions(), "@@FIG_READERS@@": "", "@@FIG_FAIL@@": F.fig_fail()}
    return {"@@FIG_STRUCTURE@@": fig_structure(), "@@FIG_READERS@@": fig_readers() + READERS_PARA, "@@FIG_FAIL@@": ""}

def body_sections(ads_after, figs="inline"):
    """ads_after: dict section_index (0-based, after that section) -> ad html"""
    out = []
    reps = figures(figs)
    for i, (sid, h2, html) in enumerate(SECTIONS):
        for k, v in reps.items():
            html = html.replace(k, v)
        out.append(f'<h2 id="{sid}">{h2}</h2>{html}')
        if i in ads_after:
            out.append(ads_after[i])
    return "\n".join(out)

def toc_links():
    items = [(sid, h2) for sid, h2, _ in SECTIONS] + [("template", "Get the PRD template")]
    return "".join(f'<li><a href="#{sid}">{h2}</a></li>' for sid, h2 in items)

def after_article():
    return f"{template_block()}\n{AUTHOR}\n{RELATED}\n{NEWS}"

# ---------------------------------------------------------------- variant A

ICON_CLOCK = ('<svg class="ico" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="10" cy="10" r="7.25" fill="none" '
              'stroke="currentColor" stroke-width="1.5"/><path d="M10 6v4.2l2.8 1.8" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>')
ICON_X = ('<svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path fill="currentColor" d="M11.7 8.6 17.6 2h-1.4l-5.1 5.7L7 2H2.3l6.2 8.8L2.3 18h1.4l5.4-6.1 4.3 6.1h4.7l-6.4-9.4Zm-1.9 2.2-.6-.9-5-7h2.1l4 5.7.6.9 5.3 7.4h-2.1l-4.3-6.1Z"/></svg>')
ICON_IN = ('<svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path fill="currentColor" d="M3.2 2h13.6c.7 0 1.2.5 1.2 1.2v13.6c0 .7-.5 1.2-1.2 1.2H3.2C2.5 18 2 17.5 2 16.8V3.2C2 2.5 2.5 2 3.2 2Zm1.9 5.6v7.5h2.4V7.6H5.1Zm1.2-3.8a1.4 1.4 0 1 0 0 2.8 1.4 1.4 0 0 0 0-2.8Zm2.9 3.8v7.5h2.3v-3.7c0-1 .2-2 1.5-2 1.2 0 1.2 1.2 1.2 2v3.7h2.4v-4.1c0-2-.4-3.6-2.8-3.6-1.1 0-1.9.6-2.2 1.2V7.6H9.2Z"/></svg>')
ICON_LINK = ('<svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M8.5 11.5a3.5 3.5 0 0 0 5 0l2.5-2.5a3.5 3.5 0 0 0-5-5l-1 1M11.5 8.5a3.5 3.5 0 0 0-5 0L4 11a3.5 3.5 0 0 0 5 5l1-1" '
             'fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>')

TAGS = '<ul class="chips" aria-label="Tags"><li><a href="#">PRD</a></li><li><a href="#">Discovery</a></li><li><a href="#">Templates</a></li></ul>'

def toc_numbered():
    items = [(sid, h2) for sid, h2, _ in SECTIONS] + [("template", "Get the PRD template")]
    return "".join(f'<li><a href="#{sid}"><span class="n">{i:02d}</span>{h2}</a></li>' for i, (sid, h2) in enumerate(items, 1))

def variant_a():
    return head("A", "Sidebar") + f"""<body class="va has-anchor">
<a class="skip" href="#content">Skip to the article</a>
{site_header()}
{ad("leader", "leaderboard")}
<div class="page">
<main id="content">
<article>
  <header class="top">
    {crumbs()}
    <a class="chip chip--cat" href="#">Product discovery</a>
    <h1>{TITLE}</h1>
    <div class="byrow">
      <div class="by">
        {avatar(48)}
        <span>By <a href="#">[Author Name]</a></span>
        <span class="dot" aria-hidden="true"></span>
        <span class="rt">{ICON_CLOCK}9 min</span>
        <span class="dot dot--2" aria-hidden="true"></span>
        <span class="updated">Updated <time datetime="2026-10">Oct 2026</time></span>
      </div>
      <div class="share">
        <span class="share__label">Share</span>
        <a class="icon-btn" href="#" aria-label="Share on X">{ICON_X}</a>
        <a class="icon-btn" href="#" aria-label="Share on LinkedIn">{ICON_IN}</a>
        <button class="icon-btn" type="button" data-copy-url data-copy-status="share-status" aria-label="Copy link to this article">{ICON_LINK}</button>
        <span class="share-toast" id="share-status" role="status" aria-live="polite"></span>
      </div>
    </div>
  </header>
  <hr class="top-rule">
  <div class="layout">
    <aside class="side" aria-label="Article tools and contents">
      {TAGS}
      <nav class="toc toc--num" data-toc aria-labelledby="toc-h"><h2 id="toc-h">Table of contents</h2><ol>{toc_numbered()}</ol></nav>
    </aside>
    <div class="main">
      {HERO}
      <p class="deck">{DECK}</p>
      <div class="m-only">{TAGS}</div>
      <details class="toc-m"><summary>Table of contents</summary><nav aria-label="Table of contents (compact)"><ol>{toc_links()}</ol></nav></details>
      <div class="prose">
{body_sections({1: ad("rect", "in-article-1"), 2: ad("side", "in-body-300x250"), 3: ad("rect", "in-article-2")}, figs="frame")}
      </div>
    </div>
    <aside class="rail" aria-label="Advertising">
      <div class="rail__sticky">{ad("sky", "rail-unit")}</div>
    </aside>
  </div>
  <!-- The sticky rails live only inside .layout, so they stop where the body ends. -->
  <!-- After the body the page uses the full container: template, related, newsletter. No author box (the byline carries the author). -->
  <div class="after">
    {template_block()}
    {RELATED_A}
    {NEWS}
  </div>
</article>
</main>
</div>
{footer()}
{ANCHOR}
</body>
</html>
"""

# ---------------------------------------------------------------- variant B

def variant_b():
    return head("B", "Magazine", preload_serif=True) + f"""<body class="vb">
<a class="skip" href="#content">Skip to the article</a>
{site_header()}
{ad("leader", "leaderboard")}
<main id="content">
<article>
  <header class="hero">
    {crumbs()}
    <a class="cat-link" href="#">Product discovery</a>
    <h1>{TITLE}</h1>
    <p class="deck">{DECK}</p>
    {byline(48)}
    {HERO}
  </header>
  <div class="col">
    <nav class="intoc" aria-labelledby="intoc-h"><h2 id="intoc-h">In this article</h2><ol>{toc_links()}</ol></nav>
    <div class="prose">
{body_sections({0: ad("rect", "in-article-1"), 2: ad("rect", "in-article-2"), 4: ad("rect", "in-article-3")})}
    </div>
    {after_article()}
  </div>
</article>
</main>
{footer()}
</body>
</html>
"""

# ---------------------------------------------------------------- variant C

def variant_c():
    bar = f"""<header class="site-head">
  <div class="site-head__in">
    {LOGO}
    <div class="bar-right"><a class="sub" href="#newsletter">Subscribe</a>{TOGGLE}</div>
  </div>
</header>"""
    return head("C", "Reader") + f"""<body class="vc">
<a class="skip" href="#content">Skip to the article</a>
{bar}
<main id="content">
<article class="col">
  <header class="hero">
    {crumbs()}
    <h1>{TITLE}</h1>
    <p class="deck">{DECK}</p>
    {byline()}
    {HERO}
  </header>
  {ad("rect", "after-deck")}
  <div class="prose">
{body_sections({2: ad("rect", "in-article-1")})}
  </div>
  {after_article()}
</article>
</main>
{footer()}
</body>
</html>
"""

if __name__ == "__main__":
    for name, fn in (("article-a.html", variant_a), ("article-b.html", variant_b), ("article-c.html", variant_c)):
        (HERE / name).write_text(fn(), encoding="utf-8", newline="\n")
        print("wrote", name)
