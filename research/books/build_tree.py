"""Builds research/explainers/book-shelf-tree-2026-10-10.html from research/books/candidates-2026-10-10.csv.

Run from anywhere: python research/books/build_tree.py
The page layout is in build_tree_template.html beside this script.
"""
import csv, html, collections, os, urllib.parse
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..')) + os.sep
TEMPLATE = os.path.join(HERE, 'build_tree_template.html')
rows = list(csv.DictReader(open(ROOT+'research/books/candidates-2026-10-10.csv', encoding='utf-8')))
E = lambda s: html.escape(s or '', quote=True)

TREE = [
 ('Design', ['UX research','UX design','UI design','Design systems','Accessibility']),
 ('Product', ['Product management','Product strategy','Product discovery','Project management']),
 ('Business', ['Product metrics','Growth and pricing','Product marketing','Leadership and teams']),
 ('Also on the shelf', ['Psychology and behavioral science','Business and entrepreneurship','Personal and professional development']),
]
SHELVES = TREE[3][1]
ALL_CATS = [c for _, cs in TREE for c in cs]
DOMAIN_NOTE = {
 'Design':'The five Design categories.',
 'Product':'The four Product categories.',
 'Business':'The four Business categories.',
 'Also on the shelf':'The three extra shelves from the brief. They are not site categories; the Books page would list them as shelves of their own.',
}
TIER_LABEL = {'A':'the canon everyone names','B':'widely recommended','C':'good but niche'}

POT = {
 1:"Seeds a piece on how much research a small team needs before it builds, and a starter plan for a team with no researcher.",
 2:"Seeds a user interview guide with a question list, and a piece on turning interview notes into decisions.",
 12:"Seeds plain explainers of affordances and signifiers, using screens from products readers open every day.",
 13:"Seeds a page-scanning checklist and a piece on why people skim, tried out on one real landing page.",
 14:"Seeds an explainer of the five planes, matched to the documents a team writes at each one.",
 16:"Seeds a piece on writing design hypotheses, with a template that fits a two-week sprint.",
 23:"Seeds an information architecture primer and a navigation audit checklist.",
 33:"Seeds a before-and-after series that fixes one screen at a time with spacing, contrast and hierarchy.",
 43:"Seeds a piece on when atomic naming helps a design system and when it gets in the way.",
 55:"Seeds pieces on the four product risks and on running discovery and delivery side by side.",
 56:"Seeds a comparison of feature teams and empowered teams, with the signs that tell you which one you are on.",
 58:"Seeds a piece on spotting the build trap in your own roadmap, with outcome questions to ask in planning.",
 59:"Seeds a press-release-first template and a guide to writing a six-page narrative memo.",
 68:"Seeds a piece on telling a strategy from a list of goals, with the kernel as a one-page template.",
 69:"Seeds a product strategy template built on the five choices, filled in for a sample product.",
 75:"Seeds an opportunity solution tree walkthrough and a weekly interview routine for busy teams.",
 76:"Seeds a list of customer questions that get honest answers, set next to the ones that invite polite lies.",
 77:"Seeds a piece on running a shorter design sprint, and on when a sprint is the wrong tool.",
 78:"Seeds a story mapping guide and template for the User stories group.",
 88:"Seeds a piece on finding the bottleneck in a product team's workflow.",
 97:"Seeds a guide to choosing one metric by business model and stage, with a lookup table.",
 98:"Seeds an OKR guide with good and weak examples written for product teams.",
 105:"Seeds a piece on setting up a growth experiment loop, with an experiment log template.",
 106:"Seeds a channel-picking worksheet based on the Bullseye method, for products that are just starting.",
 107:"Seeds a piece on talking price with customers before you build, with a pricing interview script.",
 112:"Seeds a Business Model Canvas guide with a worked example and a template to fill in.",
 114:"Seeds a positioning worksheet and a piece on repositioning a product that sells poorly.",
 116:"Seeds a short piece on where positioning came from and what still holds for software products.",
 117:"Seeds a piece on picking a beachhead segment, with the positioning statement as a template.",
 127:"Seeds pieces on one-on-ones and on judging a manager by the team's output.",
 128:"Seeds a first-90-days guide for new design and product managers.",
 129:"Seeds a feedback guide with sample lines for design and product reviews.",
 130:"Seeds a team health check built on the five layers, usable in a retrospective.",
 145:"Seeds explainers of the biases that show up in roadmap and research decisions.",
 146:"Seeds a piece on the persuasion principles in onboarding and pricing pages, and the point where they turn manipulative.",
 147:"Seeds a piece on defaults and choice architecture in settings screens and sign-up flows.",
 148:"Seeds a piece on habit loops in products, set against the ethics of building them.",
 157:"Seeds an MVP guide that sorts the kinds of MVP by what each one tests.",
 158:"Seeds an explainer of disruption, with the cases it is often wrongly applied to.",
 159:"Seeds a pre-build checklist from the questions it asks of a new product idea.",
 160:"Seeds pieces on the hard calls in product leadership: layoffs, pivots and killing a product.",
 168:"Seeds a piece on protecting focus time in a meeting-heavy product role.",
 169:"Seeds a piece on small weekly habits for product people, such as a fixed research hour.",
 170:"Seeds a piece on running the flood of requests a product manager gets through one capture system.",
 171:"A loose fit for articles; best as background on a career reading list.",
}
ALSO = {
 8:'Product metrics', 11:'UX design', 16:'Product discovery', 17:'Psychology and behavioral science',
 18:'Psychology and behavioral science', 20:'Psychology and behavioral science', 22:'UX research',
 39:'Accessibility', 40:'Product metrics', 42:'Product metrics', 53:'UX design', 59:'Leadership and teams',
 60:'Business and entrepreneurship', 70:'Business and entrepreneurship', 71:'Product marketing',
 73:'Product metrics', 74:'Product discovery', 77:'UX design', 79:'Business and entrepreneurship',
 80:'Product strategy', 84:'Product marketing', 91:'Product management', 93:'Product metrics',
 98:'Leadership and teams', 99:'Leadership and teams', 103:'UI design', 110:'Product strategy',
 112:'Business and entrepreneurship', 113:'Product strategy', 123:'Growth and pricing', 124:'Growth and pricing',
 126:'Product discovery', 136:'Product marketing', 137:'Project management', 138:'UX design',
 147:'UX design', 148:'Growth and pricing', 151:'UX design', 154:'Leadership and teams', 155:'UX design',
 157:'Product discovery', 158:'Product strategy', 165:'Product discovery',
}
WHY_ALSO = {
 123:'its group in the CSV, Growth and funnels, belongs to Growth and pricing',
 124:'its group in the CSV, Product-led growth, belongs to Growth and pricing',
}

def year(r):
    y = r['first_published']; ed = r['latest_edition'].strip()
    return y + (', ' + ed if ed and ed != '-' else '')

def aged_flag(r):
    n = r['aged_note'].lower()
    return r['aged'] == 'Dated in parts' or 'dated' in n or 'supersed' in n

def potential(r):
    if r['tier'] == 'A': return POT.get(int(r['id']), '')
    if r['tier'] == 'B' and r['group']:
        return 'A source to cite in the ' + r['group'] + ' pieces.'
    return ''

def host(u):
    h = urllib.parse.urlparse(u).netloc
    return h[4:] if h.startswith('www.') else h

by_cat = collections.defaultdict(list)
for r in rows: by_cat[r['category']].append(r)
assert not [r for r in rows if r['category'] not in ALL_CATS]
tier_order = {'A':0,'B':1,'C':2}
for c in by_cat: by_cat[c].sort(key=lambda r:(tier_order[r['tier']], r['title'].lower()))

def book_li(r):
    i = r['id']; t = r['tier']; aged = aged_flag(r)
    cid = 'card-' + i
    also = ALSO.get(int(i))
    srcs = ''
    if r['recommended_by_urls'].strip():
        links = ' '.join('<a href="%s" rel="noopener">%s</a>' % (E(u), E(host(u))) for u in r['recommended_by_urls'].split())
        srcs = '<p class="src"><b>Backed by:</b> %s. <span class="links">%s</span></p>' % (E(r['recommended_by'].rstrip('.')), links)
    pot = potential(r)
    o = []
    o.append('<li class="book t%s%s" data-tier="%s">' % (t, ' aged' if aged else '', t))
    o.append('<button type="button" class="bk" aria-expanded="false" aria-controls="%s">' % cid)
    o.append('<span class="tt">%s</span> <span class="meta"><span class="au">%s</span> <span class="yr">%s</span></span>' % (E(r['title']), E(r['authors']), E(year(r))))
    o.append('<span class="tags"><span class="badge b%s">%s</span>' % (t, E(TIER_LABEL[t])))
    if aged: o.append('<span class="agedm">aged</span>')
    if also: o.append('<span class="twom">2 homes</span>')
    o.append('</span></button>')
    o.append('<div class="card" id="%s">' % cid)
    o.append('<p><b>Known for:</b> %s.</p>' % E(r['known_for'].rstrip('.')))
    o.append('<p><b>For whom:</b> %s.</p>' % E(r['for_whom'].rstrip('.')))
    o.append('<p><b>Why it is on the list:</b> %s.</p>' % E(r['why_recommended'].rstrip('.')))
    if srcs: o.append(srcs)
    o.append('<p><b>Has it aged?</b> %s.</p>' % E(r['aged_note'].rstrip('.')))
    if also: o.append('<p><b>Could also sit in:</b> %s.</p>' % E(also))
    if pot: o.append('<p class="pot"><b>Article potential:</b> %s</p>' % E(pot))
    o.append('</div></li>')
    return ''.join(o)

def counts(bs):
    c = collections.Counter(r['tier'] for r in bs)
    return len(bs), c['A'], c['B'], c['C']

def cnt_html(bs):
    n,a,b,c = counts(bs)
    return ('<span class="cnt"><span class="n">%d</span><span class="mix"><span class="m"><i class="dA"></i>%d A</span><span class="m"><i class="dB"></i>%d B</span><span class="m"><i class="dC"></i>%d C</span></span></span>' % (n,a,b,c))

tree = []; placed = []
for dom, cats in TREE:
    dbooks = [r for c in cats for r in by_cat[c]]
    tree.append('<li class="dom"><details open><summary><span class="dn">%s</span>%s</summary><p class="dnote">%s</p><ul class="cats">' % (E(dom), cnt_html(dbooks), E(DOMAIN_NOTE[dom])))
    for c in cats:
        bs = by_cat[c]; placed += bs
        tree.append('<li class="cat"><details><summary><span class="cn">%s</span>%s</summary><ul class="books">' % (E(c), cnt_html(bs)))
        tree += [book_li(r) for r in bs]
        tree.append('</ul></details></li>')
    tree.append('</ul></details></li>')
assert len(placed) == len(rows) and len({r['id'] for r in placed}) == len(rows), 'a book is missing or listed twice'

shelf_map = collections.defaultdict(collections.Counter)
for r in rows:
    if r['category'] not in SHELVES:
        shelf_map[r['brief_shelf']][r['category']] += 1
shelf_lines = []
for s in ['UX and design','Product management','Marketing and growth','Leadership and management']:
    parts = ', '.join('%s (%d)' % (c, n) for c, n in shelf_map[s].most_common())
    shelf_lines.append('<li><b>%s</b> (the brief\'s shelf) went to %s.</li>' % (E(s), E(parts)))
title_of = {int(r['id']): r for r in rows}
two_rows = []
for i in sorted(ALSO, key=lambda k:(ALL_CATS.index(title_of[k]['category']), title_of[k]['title'].lower())):
    r = title_of[i]; why = WHY_ALSO.get(i, '')
    two_rows.append('<tr><td>%s</td><td>%s</td><td>%s%s</td></tr>' % (E(r['title']), E(r['category']), E(ALSO[i]), (' <span class="why">(' + E(why) + ')</span>') if why else ''))
per_cat_rows = ''.join('<tr><td>%s</td><td>%d</td><td>%d</td><td>%d</td><td>%d</td></tr>' % ((E(c),) + counts(by_cat[c])) for c in ALL_CATS)
tot = counts(rows)
n_aged = sum(1 for r in rows if aged_flag(r))

page = open(TEMPLATE, encoding='utf-8').read()
for k, v in {'{{TREE}}':'\n'.join(tree), '{{SHELF}}':'\n'.join(shelf_lines), '{{TWO}}':'\n'.join(two_rows),
             '{{NTWO}}':str(len(ALSO)), '{{PERCAT}}':per_cat_rows, '{{NAGED}}':str(n_aged),
             '{{N}}':str(tot[0]), '{{A}}':str(tot[1]), '{{B}}':str(tot[2]), '{{C}}':str(tot[3])}.items():
    page = page.replace(k, v)
open(ROOT+'research/explainers/book-shelf-tree-2026-10-10.html', 'w', encoding='utf-8', newline='\n').write(page)
for c in ALL_CATS: print(c, counts(by_cat[c]))
print('aged', n_aged, 'two', len(ALSO))
