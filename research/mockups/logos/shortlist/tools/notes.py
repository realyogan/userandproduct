"""Notes for the shortlist board: per concept the source, the wordmark change and a note; for the new
marks also originality, the 16px verdict and the closest existing logos (from the image check)."""

INTRO_METHOD = (
    '<p><b>How the new marks were checked.</b> Logos were downloaded, rendered side by side with the drafts and '
    'looked at, not only searched by description: PBS (2019 and 1984), the Lincoln cent, Tiger Data, Headspace, '
    'Persona, Humaans, Kiehl\'s, AMC Networks, Beats, and for the sphere Avalanche, Ethereum, Polygon, the '
    'Sierpinski triangle and the Triforce. The Alfred Hitchcock silhouette and the Schwarzkopf head were checked '
    'from memory of the published marks, not from a downloaded file.</p>'
    '<p><b>What the check changed.</b> PBS turned out to be the closest mark to the profile by far: a white head in '
    'profile, facing right, cut out of a blue disc. A first draft of the minimal profile had a round cranium and was '
    'two small changes from it (drop the eye, drop the echo heads), so the round skull was replaced by three '
    'straight cuts. All three profiles now differ from PBS in four ways: a skull made of straight cuts, no eye, '
    'one head, and a slanted cameo neck line. The alternative color is oxblood, not navy, to stay away from PBS '
    'blue. For the sphere, Avalanche (white triangles in a red disc) is the closest; ours is seven equal cells in a '
    'lattice whose base is the disc\'s own curve, not two solid triangles on a line.</p>')

P8_WORD = ('Inter Display Bold, lowercase, one word, tracking -25, one ink color. The mark is 1.4 cap heights tall, '
           'centered on half the cap height, with a gap of 0.38 cap heights. This is the setup every lockup on this '
           'page now uses.')


def reset(prev):
    return (f'Reset to the final wordmark: Inter Display Bold, tracking -25, in the concept\'s own ink, with P8\'s '
            f'proportions. Before: {prev}.')


NOTES = {
    'P8': dict(from_='', word=P8_WORD,
               note='Included as the reference: its lockup is rebuilt by the same code as every other concept here '
                    'and matches the round 4 file.'),
    'P3': dict(word=reset('Fraunces SemiBold capitals, widely tracked'),
               note='The "up" inside the square is part of the mark and keeps its Fraunces letterforms; next to the '
                    'grotesque name the serif monogram now reads as a deliberate contrast. The square is set 1.4 cap '
                    'heights tall, much smaller than before, so the name leads.'),
    'P5': dict(word=reset('Geist Bold, tracking -20, the mark one cap height tall'),
               note='At P8\'s proportions the pair grows from one to 1.4 cap heights; it now sits as tall as the '
                    'ascenders and reads as a sign rather than a bullet. The word stays in ink; blue lives only in the disc.'),
    'Q3': dict(word=reset('Fraunces SemiBold, tracking -10, mark 1.7 cap heights'),
               note='The tree is smaller than before (1.4 rather than 1.7 cap heights), so its lines are finer in the '
                    'header strip; the green word on cream keeps the bookish feel without the serif.'),
    'R4': dict(word=reset('Instrument Sans Bold, tracking -10, disc 1.62 cap heights'),
               note='The ink disc with three low rings sits naturally next to Inter: the same black, the same calm '
                    'geometry as P8, with a figure instead of a slice.'),
    'R5': dict(word=reset('Instrument Sans Bold, tracking -10, disc 1.62 cap heights'),
               note='The word stays ink and the red stays in the disc, so the lockup still has one ink color in the '
                    'name. The bar and full stop line up with the word that follows: the mark reads as the start of a '
                    'sentence.'),
    'S5': dict(word=reset('Fraunces SemiBold, tracking -10'),
               note='The tiles keep their oxblood; the word is oxblood too, as before. The diamond is wider than tall, '
                    'so at 1.4 cap heights it reaches further into the gap than the round marks.'),
}

for v in 'ABC':
    NOTES['NEW1' + v] = dict(word=P8_WORD.replace('This is the setup every lockup on this page now uses.',
                                                  'Ink on white; oxblood is shown as the alternative.'))
    NOTES['NEW2' + v] = dict(word=P8_WORD.replace('This is the setup every lockup on this page now uses.',
                                                  'Deep navy, from T8.'))

NOTES['NEW1A'].update(
    orig='Four changes from PBS (straight-cut skull, no eye, one head, slanted neck line) and a human head rather than '
         'Tiger Data\'s striped tiger. No coin portrait is a flat cut with no shoulders or legend.',
    v16='Reads. The nose and chin give a face at 16px; the lips merge into the chin, which is why the favicon art drops them.',
    note='The most expressive of the three: the brow and lips make it a person, not a symbol. It is also the one most '
         'likely to be read as a portrait of the author, which may be a plus for an authority-first site.')
NOTES['NEW1B'].update(
    orig='The round cranium of the first draft was two small changes from PBS and was removed; the skull is now three '
         'straight cuts. Still a single head facing right in a disc, so PBS remains the name to watch.',
    v16='Reads. One long forehead-to-nose line is the clearest feature at 16px; the head reads as a head first.',
    note='The calmest and most institutional of the three: closest to a seal or a coin, fewest details to age.')
NOTES['NEW1C'].update(
    orig='None of the checked marks breaks the rim with a head; PBS and coin portraits float inside their disc. The '
         'open crown is the one move that is clearly ours.',
    v16='Fair. At 16px it reads as a cup or a horseshoe with a head inside; the open top costs the disc its outline.',
    note='The most distinctive outline and the most editorial: a head rising out of the frame. The price is the '
         'favicon, where the broken rim weakens the circle.')
NOTES['NEW2A'].update(
    orig='Avalanche is two solid white triangles in a red disc; Sierpinski and the Triforce hollow their centers. Ours '
         'keeps seven equal cells, down cells included, and fuses the base with the disc\'s inner edge.',
    v16='Reads. With 1px gaps the cluster is a pale faceted ball inside the navy disc; the lattice shows as texture.',
    note='The fullest sphere: the cells nearly fill the disc and the base follows the rim, so it reads as one rounded '
         'body. The best of the three at 16px.')
NOTES['NEW2B'].update(
    orig='As A. With wider gaps the triangles read more clearly as separate cells, which moves it slightly toward '
         'Avalanche\'s cut white triangles, still seven against two.',
    v16='Fair. At 1.5px gaps the cells read as seven points arranged in a ball; the outline of the cluster survives.',
    note='The middle step: more air between the cells, a crisper lattice at large sizes.')
NOTES['NEW2C'].update(
    orig='As A; the wider gaps make the lattice the dominant shape, like a cut metal grille.',
    v16='Weak. At 2px gaps the cells shrink to scattered dots and the sphere is lost. Widening the gaps beyond 1.5px '
        'at 16px makes the reading worse, not better.',
    note='Shown as the upper bound: handsome at 560px, but it fails the favicon test.')

for k in NOTES:
    NOTES[k].setdefault('from', '')
    if 'from_' in NOTES[k]:
        NOTES[k]['from'] = NOTES[k].pop('from_')

SRC_TXT = {
    'P8': 'Built on round 4 as the sliced disc; the final wordmark comes from here.',
    'P3': 'Built on round 4; mark copied unchanged.',
    'P5': 'Built on round 4; mark copied unchanged.',
    'Q3': 'Built on round 5; mark copied unchanged.',
    'R4': 'Built on round 6; mark copied unchanged.',
    'R5': 'Built on round 6; mark copied unchanged.',
    'S5': 'Built on round 7 tiles; mark copied unchanged.',
}
for k, t in SRC_TXT.items():
    NOTES[k]['from'] = t
for v in 'ABC':
    NOTES['NEW1' + v]['from'] = 'New on this page: the Tiger Data move with a human head.'
    NOTES['NEW2' + v]['from'] = 'New on this page, from round 7 triangles T8 (the triangle of nine).'

_PROFILE_CLOSE = [
    ('PBS (2019)', 'public broadcaster',
     'A white head in profile facing right, cut from a blue disc, round cranium, an eye dot and two echo heads. Ours: '
     'a skull of straight cuts, no eye, one head, a slanted neck line, ink or oxblood.'),
    ('Lincoln cent', 'coin portrait',
     'A modeled bust facing right with shoulders and a lettered legend round the rim. Ours is one flat cut, no '
     'shoulders, no lettering.'),
    ('Tiger Data', 'database',
     'A tiger head facing right built from stripes on a disc. Ours is a human head, one cut, no stripes.'),
    ('Alfred Hitchcock silhouette', 'television title',
     'A line caricature with a round jowl, no disc. Ours is a solid cut with straight segments inside a disc.'),
    ('Head-in-circle SaaS: Headspace, Humaans, Persona', 'wellness and HR software',
     'Headspace is a plain orange disc, Humaans an H in a coral square, Persona an asterisk over a bar; none uses a '
     'profile. Kiehl\'s is a script wordmark and AMC Networks a wordmark: no profile in either.'),
]
_SPHERE_CLOSE = [
    ('Avalanche', 'blockchain',
     'Two white triangles, one with a slash, cut from a red disc on a common baseline. Ours is seven equal cells '
     'in a lattice whose base follows the disc\'s curve.'),
    ('Ethereum', 'blockchain',
     'A two-tone octahedron, no disc. Ours is a flat lattice of seven triangles in a disc.'),
    ('Sierpinski triangle', 'public figure',
     'A triangle with its down cells hollowed at every scale. Ours keeps the down cells, removes the two bottom '
     'corners and stops at one level.'),
    ('Triforce', 'game emblem',
     'Three solid triangles round a hollow center, no disc. Ours has seven cells, a solid center and a disc.'),
    ('Polygon', 'blockchain',
     'An interlocking hexagonal outline; shares only the faceted feel. Not close in shape.'),
]
CLOSEST = {}
for v in 'ABC':
    CLOSEST['NEW1' + v] = _PROFILE_CLOSE
    CLOSEST['NEW2' + v] = _SPHERE_CLOSE
