"""The words on the round 4 board, one entry per mark, in board order (R4-01 onward).

Families share their meaning, authority check and nearest logos; each variant says what changed.
"""


def fam(group, name, colour, typ, means, authority, closest):
    return dict(group=group, family=name, colour=colour, type=typ, means=means, authority=authority, closest=closest)


CUP = fam('cup', 'Cup and ball', 'blue', 'Figurative: an object, tilted to read as a figure',
          'The bowl is the product and the ball is the person. Turn it to the left and the high side of the bowl '
          'becomes a raised arm, the ball a head: someone putting a hand up. It is still a U for user, and the '
          'product is still cut to fit the person.',
          'A heavy coin with one cut. Tilted, it gains movement; it has to stay calm enough to feel steady.',
          ['Target (a dot held by a round form)', 'Ubisoft (a swirl around a dot)'])
SPEECH = fam('speech', 'Speech mark', 'vermilion', 'Symbol: a closing quote mark',
             'It is a closing quote mark. When people cite you, they put your words inside these. The aim of the '
             'site is to be the source people quote.',
             'Editorial, not chat: one heavy quote mark, like a pull-quote in a printed magazine.',
             ['bold comma and closing-quote glyphs in display typefaces', 'Disqus (a speech-bubble letter)'])
SQUARE = fam('square', 'Square coin', 'blue', 'Letter-based: a U cut from a tile',
             'The tile is the product, like an app icon on a phone. The U cut through it is the user. Nothing is '
             'stuck on top; the person is part of the shape of the product.',
             'Square, architectural and level; the steadiest of the shortlist.',
             ['Udemy (a U letter mark)', 'R2-05 the cut coin in round 2 (its ancestor)'])
SHELF = fam('shelf', 'Shelf', 'oxblood', 'Figurative: two books',
            'Two books on a shelf, one leaning on the other. It is a reference shelf, the place you go for an answer '
            'you can trust. Fifteen years of practice, put on the shelf.',
            'Books are the sign of a reference you can cite; a library binding color helps.',
            ['Apple Books (a book form)', 'library icons in interface kits (books on a shelf)'])


def v(base, name, idea, nice, construction, colour=None):
    d = dict(base)
    d.update(name=name, idea=idea, nice=nice, construction=construction)
    if colour:
        d['colour'] = colour
    return d


INFO = [
    # ---------------------------------------------------------------- Cup and ball
    v(CUP, 'Cup and ball, as shortlisted',
      'R3-03 as the owner saw it, for reference: a bowl cut from the top of the coin, a ball resting in it.',
      'Reads as a cup holding a ball, and as a U. No figure yet.',
      'Disc 512; the bowl is a circle of radius 150 at y 190 plus a 300-wide cut to the top; ball radius 104.'),
    v(CUP, 'Cup and ball, 30 degrees',
      'The same coin turned 30 degrees to the left.',
      'The U still reads first; the raised hand is only a hint.',
      'R4-01 turned 30 degrees anticlockwise about its center. The coin is the mark; the cut is real.'),
    v(CUP, 'Cup and ball, 30 degrees, in a disc',
      'The 30-degree cup and ball cut from a filled disc.',
      'In a disc the cup becomes a thick ring around a ball; the figure fades.',
      'R4-02 scaled to 72 percent, cup white and ball in the second tone, in a signal-blue circle.'),
    v(CUP, 'Cup and ball, 45 degrees',
      'The coin turned 45 degrees to the left.',
      'All three readings hold here: a U on its side, a head with one arm raised, and the straight cut edge on '
      'the left as the stem of a D.',
      'R4-01 turned 45 degrees anticlockwise.'),
    v(CUP, 'Cup and ball, 45 degrees, in a disc',
      'The 45-degree cup and ball cut from a filled disc.',
      'The raised arm survives inside the disc, but the D is lost.',
      'R4-04 scaled to 72 percent in a signal-blue circle.'),
    v(CUP, 'Cup and ball, 60 degrees',
      'The coin turned 60 degrees to the left.',
      'The raised arm is strongest, but the U is gone; it starts to look like a shell or a swirl.',
      'R4-01 turned 60 degrees anticlockwise.'),
    v(CUP, 'Cup and ball, 60 degrees, in a disc',
      'The 60-degree cup and ball cut from a filled disc.',
      'Reads as a swirl around a dot; the weakest of the family.',
      'R4-06 scaled to 72 percent in a signal-blue circle.'),
    v(CUP, 'Cup and ball, 45 degrees, ball lifted',
      'At 45 degrees, the ball lifted 60 units out of the bowl along its axis.',
      'With the head clear of the shoulders, the person with a raised hand reads first and the U second.',
      'R4-04 with the ball moved 60 units up the axis of the bowl before the turn; 20 units still sit below the rim.'),
    v(CUP, 'Cup and ball, 45 degrees, ball lifted, in a disc',
      'The lifted version cut from a filled disc.',
      'The figure holds; the coin edge that made the D is gone.',
      'R4-08 scaled to 72 percent in a signal-blue circle.'),
    # ---------------------------------------------------------------- Speech mark
    v(SPEECH, 'Speech mark, as shortlisted',
      'R3-04 as the owner saw it, for reference: one notch bitten from a disc leaves a short tail.',
      'At 32 px the tail almost disappears and the mark reads as a ball with a seam.',
      'Head disc radius 186; the tail is what is left of a 226 circle after a 236 notch. Lit wall 52 wide.'),
    v(SPEECH, 'Speech mark, longer tail',
      'The tail sweeps well past the head and ends in a point at the lower left.',
      'The tail is now the drawing: at 32 px it reads as a quote mark at a glance; at 16 px the tail is thin but still there.',
      'Head radius 170; the tail is cut from a 280 circle that meets the head at its widest point, by a 250 '
      'notch. Lit wall 52 wide along the notch. Fitted to a 448 square.'),
    v(SPEECH, 'Speech mark, heavier tail',
      'The same long tail, made thicker by moving the notch away.',
      'A fuller tail: the one that survives smallest. At 16 px it is still plainly a quote mark, not a ball.',
      'As R4-11 with the notch moved 48 units further out. Lit wall 56 wide.'),
    v(SPEECH, 'Speech mark, sharper notch',
      'A smaller, tighter notch bites deep and leaves a short, hooked tail.',
      'The most typographic of the family: a bold comma. The tail is short again, so it fades at 16 px.',
      'Head radius 176; notch radius 150 set low. Lit wall 46 wide.'),
    v(SPEECH, 'Speech mark, wedge tail',
      'The tail as a solid wedge outside the disc, at the lower left; the wedge is the lit part.',
      'Reads at once at any size, but as a chat bubble rather than a quote mark.',
      'Head radius 200 plus a triangle reaching to the lower left; the part outside the head is the second tone.'),
    # ---------------------------------------------------------------- Square coin
    v(SQUARE, 'Square coin, as shortlisted',
      'R3-05 on the earlier board: a rounded square with a U channel cut through it, the tongue lit.',
      'The tile is the app icon and the letter at once.',
      'Corner radius 116, channel 56 wide, U 280 wide with its foot at y 410.'),
    v(SQUARE, 'Square coin, softer corners',
      'The same cut in a softer tile.',
      'Friendlier, closer to an app-store icon; slightly less architectural.',
      'Corner radius 168; channel 56; foot at y 410.'),
    v(SQUARE, 'Square coin, wider channel',
      'A wider cut, so the U is drawn more boldly and the tongue is narrower.',
      'The U reads first, even at 16 px.',
      'Corner radius 116; channel 74; foot at y 410.'),
    v(SQUARE, 'Square coin, shallower channel',
      'The U stops higher, leaving a heavier floor to the tile.',
      'More weight at the base: the tile feels planted.',
      'Corner radius 116; channel 56; foot at y 356.'),
    # ---------------------------------------------------------------- Shelf
    v(SHELF, 'Shelf, as shortlisted',
      'R3-14 on the earlier board: one book upright, one leaning on it, the corner where they touch lit.',
      'A serious library drawn with two slabs.',
      'Two slabs 118 by 340 (radius 20); the right one turned 24 degrees and set against the first.'),
    v(SHELF, 'Shelf, steeper lean, squatter books',
      'The leaning book tips further, and both books are shorter and wider.',
      'More movement, and the books read as books rather than bars.',
      'Two slabs 132 by 300; the right one turned 32 degrees.'),
    v(SHELF, 'Shelf, in a disc',
      'The two books cut from a filled disc.',
      'Works as an avatar straight away; the books shrink a little to fit.',
      'Two slabs 108 by 300, turned 24 degrees, in an oxblood circle. Monochrome cuts an 18-unit gap where they touch.'),
    v(SHELF, 'Shelf, in blue',
      'R4-19 in the default signal blue.',
      'Shows whether the books need the oxblood to read as a library.',
      'As R4-19, in signal blue.', colour='blue'),
    # ---------------------------------------------------------------- New figurative (from round 3)
    dict(group='fig', name='At the screen', colour='blue', type='Figurative: a cut-out silhouette',
         idea='A person seen from behind, in front of a screen; their head crosses the lower edge of the screen.',
         means='This is someone sitting in front of a product, using it. You see them from behind, the way a '
               'designer watches a test session. The site is about that moment: a real person and the thing on '
               'their screen.',
         nice='You are standing behind the user, which is exactly where a good researcher stands.',
         authority='Two calm solids cut from a disc, no gesture and no expression; it reads like a pictogram on a sign.',
         construction='As R3-12: a screen 352 by 236 and a head (radius 68) with shoulders running out of the disc.',
         closest=['video-call and screen-sharing icons in interface kits', 'Loom (a person on a screen)']),
    dict(group='fig', name='Doorway', colour='blue', type='Figurative: a cut-out silhouette',
         idea='A person (the user) standing in a door frame (the product), shoulders wider than the door.',
         means='The arch is the product, the way in. The person standing in it is a little too wide for the '
               'opening. Good products are built for the people who actually turn up, not for the door you planned.',
         nice='The shoulders overlap the frame: the person does not quite fit, which is the whole job.',
         authority='An arch is the architecture of institutions; one figure in it reads as a welcome.',
         construction='As R3-14: an arched frame 272 wide with a 144 opening, a head radius 50, shoulders radius 118.',
         closest=['emergency exit signs (a figure in a doorway)', 'arched-door marks of museums and libraries']),
    dict(group='fig', name='Raised hand', colour='blue', type='Figurative: a cut-out silhouette',
         idea='A person with one arm raised; the arm crosses the shoulder and is lit there.',
         means='Someone in the room has put their hand up with a question. Most of this site starts there: a real '
               'question from someone doing the work. The answer comes from fifteen years of having asked it too.',
         nice='One raised arm turns a stock figure into a person with something to ask; it echoes the tilted cup.',
         authority='A classroom gesture rather than a wave; calm and level.',
         construction='As R3-18: head radius 64, shoulders radius 156, an arm 76 wide turned 20 degrees.',
         closest=['the raised-hand button in video-call apps', 'classroom and Q&A pictograms']),
    # ---------------------------------------------------------------- Fresh marks
    dict(group='fresh', name='Lens', colour='blue', type='Symbolic: a tool',
         idea='A magnifying glass cut from a tile; the glass is lit.',
         means='A lens is for looking closely. The site takes one question at a time and looks at it properly. '
               'The lit glass is the part you see more clearly after reading.',
         nice='One tool says close reading, research and care at once.',
         authority='Heavy and plain, like an instrument; the risk is that it is also the search icon on every site.',
         construction='In a rounded square: a ring radius 150 to 92 and a handle 84 wide at 45 degrees; the glass '
                      'is the second tone. Monochrome cuts the ring and handle; the glass stays solid.',
         closest=['the search icon in every interface kit', 'magnifier marks of research and audit firms']),
    dict(group='fresh', name='Dividers', colour='blue', type='Symbolic: a tool',
         idea='The drawing compass: two legs from one hinge; where the legs cross under the hinge, lit.',
         means='Dividers are the tool for measuring and drawing true circles. A designer and a builder both use '
               'them. It also looks like a person mid-stride, someone on the move with a plan.',
         nice='A maker\'s tool that is also a walking figure.',
         authority='A drafting instrument: precise, old, trusted by engineers and architects.',
         construction='In a circle: a hinge disc radius 50 with a 32-wide handle, two legs 60 wide from the hinge '
                      'to the foot, spread 212 apart. Monochrome cuts an 18-unit gap around the right leg.',
         closest=['the square and compasses of the Freemasons', 'architecture-school and drafting-tool logos']),
    dict(group='fresh', name='Desk lamp', colour='blue', type='Symbolic: an object',
         idea='A jointed desk lamp leaning over the work; the bulb shows under the shade and is lit.',
         means='The lamp on the author\'s desk, turned onto the work. Late nights, close attention, the one light '
               'in the room. The site is that light pointed at a problem.',
         nice='The lit bulb is the fold: the one place the eye goes.',
         authority='A working lamp, not a cartoon; calm angles, heavy base.',
         construction='In a circle: a base 190 by 54, two arms 52 wide with a 34 joint, a shade (half-disc radius '
                      '112, turned 20 degrees) and a bulb radius 46 under its rim, in the second tone where it shows. '
                      'Monochrome cuts an 18-unit gap around the bulb.',
         closest=['Pixar (the jointed lamp)', 'study and reading-room lamp marks']),
    dict(group='fresh', name='Rook', colour='plum', type='Symbolic: a chess piece',
         idea='The rook, the chess piece that holds its ground; the crown sits on the collar and the seam is lit.',
         means='In chess the rook is the steady piece: straight lines, no tricks. Deciding what to build is a game '
               'of moves, and the site is about making the sound ones.',
         nice='Strategy and solidity in one silhouette, and it reads as a tower too.',
         authority='The most architectural chess piece; it reads as a stronghold, not a game.',
         construction='In a circle: a base 212 by 58, a tapered body, a collar 160 by 40 and a crown 176 by 116 with '
                      'two 32-wide notches. Monochrome cuts an 18-unit gap under the crown.',
         closest=['Chess.com (a pawn)', 'castle and tower marks of banks and schools']),
    dict(group='fresh', name='Anvil', colour='green', type='Symbolic: an object',
         idea='The maker\'s anvil; the striking face is lit.',
         means='An anvil is where things get made, hit by hit. The author is a maker as well as a writer. '
               'What you read here was worked out on real projects first.',
         nice='Heavy enough to be a paperweight; it says "made" without a hammer.',
         authority='Mass itself: the heaviest silhouette in the round.',
         construction='In a circle: a face 236 by 64 with a horn to the left, a waist tapering to 106, a foot 218 '
                      'wide. Face in the second tone; monochrome cuts an 18-unit gap under the face.',
         closest=['blacksmith and forge marks', 'hammer-and-anvil logos of craft brands']),
    dict(group='fresh', name='Signpost', colour='blue', type='Symbolic: an object',
         idea='One post, two boards pointing opposite ways; where the boards cross the post, lit.',
         means='Two boards, two ways to go, one post to stand on. The site is a guide: it tells you which way and '
               'why. A teacher\'s job, drawn as a sign.',
         nice='Every article is a fork in the road; this is the sign at it.',
         authority='Clear and civic, like a trail sign; it points without shouting.',
         construction='In a circle: a post 56 wide running out of the disc, two boards 96 tall with 90-degree '
                      'points. Monochrome cuts an 18-unit gap around the boards.',
         closest=['signpost icons in interface kits', 'national-trail and park signage']),
    dict(group='fresh', name='Funnel', colour='blue', type='Symbolic: an object',
         idea='Many ideas go in at the top of a funnel, one comes out at the foot; the one is lit.',
         means='Product work is choosing. Lots of ideas go in; one is worth building. The site is about how to '
               'find that one.',
         nice='The fold is the decision: the single drop that comes out.',
         authority='Plain and functional; reads as process and judgement.',
         construction='In a circle: a funnel 328 wide at the top, a spout 72 wide, and a drop radius 46 below it. '
                      'Monochrome cuts an 18-unit gap around the drop.',
         closest=['the filter icon in interface kits', 'conversion-funnel diagrams']),
    dict(group='fresh', name='One block', colour='blue', type='Symbolic: one solid with three faces',
         idea='Design, product and business as the three visible faces of one solid block; the top face is lit.',
         means='One block, three faces. Design, product and business are not three subjects, they are sides of '
               'the same thing. You only see the whole if you look from the corner, where this site stands.',
         nice='The crossing of the three fields drawn as one object you could pick up.',
         authority='Solid and geometric, like a building block or a printed specimen.',
         construction='Free-standing: an isometric cube 318 wide; left face main tone, right face second tone, top '
                      'face the fold. Monochrome cuts 18-unit seams between the faces.',
         closest=['package and box icons in interface kits', 'Dropbox (a box made of rhombi)']),
]

# names for the families as board headings
GROUPS = {
    'cup': ('Cup and ball', 'R3-03, tilted to the left so it reads three ways: a person raising a hand, a U, and a '
                            'hint of a D. The original for reference, then 30, 45 and 60 degrees, each as the coin '
                            'itself and cut from a disc, then the ball lifted at 45.'),
    'speech': ('Speech mark', 'R3-04 with the tail made the drawing. The original for reference, then four tails, '
                              'judged at 32 px and 16 px first.'),
    'square': ('Square coin', 'R3-05 of the earlier board, with three small changes so the exact proportion can be picked.'),
    'shelf': ('Shelf', 'R3-14 of the earlier board, with the lean, the proportions, a disc and the color varied.'),
    'fig': ('New figurative', 'From the figurative pass on round 3: the three that passed the authority and 32 px checks.'),
    'fresh': ('Fresh marks', 'New ground, at the standard of a solid form with one clean idea cut from it: tools and '
                             'objects of the reader, the maker and the judge of what to build.'),
}
