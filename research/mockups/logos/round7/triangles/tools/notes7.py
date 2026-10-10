"""Notes for the round-seven triangles board: rationale, originality, 16px verdict, masthead test, and
the three closest existing logos with the one difference that keeps ours distinct.

Closest logos come from an image check: about 150 logo files and public symbols were downloaded,
rendered on one sheet, then each concept was rendered beside its three nearest neighbors and compared
by eye. Names only on the board; no reference artwork is kept in the project.
"""

TITLE = 'Logo concepts, round seven: triangles'

INTRO_HTML = '''<p>Eighteen marks drawn from the owner's three triangle sketches: two outlined triangles stacked with a
filled triangle in the overlap, a cluster of outlined triangles holding small filled ones, and a dark diamond made of a
triangular tessellation. Every concept is abstract and secular, uses one owned color (plus ink) on white or cream, and
sits beside the one word "userandproduct" set as outlines in Instrument Sans Bold or Fraunces SemiBold. One will be
picked from this round.</p>
<p>Each concept is shown at 560px on its paper and on near-black, in a 1280px site header strip on white and on near-black,
then the mark, the heavier favicon drawing with its 32px and 16px renders, one color, a 400px avatar and a profile tile.
Below that, the three closest existing logos from the image check with the one difference that keeps ours apart, the
notes, and one line for the masthead test: would this sit on a serious journal, or on a startup pitch deck? Pin any
lockup to compare.</p>
<div class="method"><p><b>How originality was checked.</b> About 150 logo files and public symbols were downloaded and
rendered side by side, then each concept was rendered beside its three nearest neighbors and looked at: the Zelda
Triforce, the Sierpinski triangle, Google Drive, Delta Air Lines, Adobe, Mitsubishi, Fitbit, Deliveroo, Rocket Mortgage (whose 2025 mark is a circular halo with no triangle),
Avalanche, Tron, Ethereum, Sketch, Renault, Unity, Snowflake, Solidity, Nuxt, Alpine Linux, Arch Linux, Vercel, Prisma,
AdonisJS, Codeberg, Pluralsight, Google Play, Material Design, Atlassian, Citroën and others, plus the eye-in-triangle,
the valknut, alchemical triangle signs, the recycling sign, the warning triangle, the eject and sort icons, the Alcoholics
Anonymous circle and triangle, and a Sri Yantra for the sacred-geometry test. Searches: overlapping triangle logos,
triangle tessellation logos, triangle in a circle, and triangle marks in publishing, finance and software.</p>
<p><b>What the check changed or dropped.</b> Three triangles stacked vertically read as a fir tree, so "three stacked" became
the horizontal run (T4). The plain triangle of three solid cells with a hollow center is the Triforce, and every
one-step change (recolor one cell, fill the center, round the corners) still read as it; it survives only as T11, with
every cell slid along the edge so the hollow closes, and as T10, turned over with the roles of solid and outline
swapped. A single white triangle in a solid disc sat one cut away from Avalanche, so T12 keeps a solid core inside the
cut. The owner's cluster with small filled triangles inside each outline carried a yantra feel and was reduced to one
cell (T12) or to three outlines with one solid (T10); no concept keeps nested concentric triangles, an eye, rays or a
radial count of nine. A triangle over a bar of equal width with a gap is the eject key, so the plinth (T16) touches a
bar far wider than itself. Two solid triangles point to point with a gap are the sort icon, so the reflection (T17)
touches and its lower half is an outline. A square with a four-pane triangle window read as the Triforce in a frame, so
T15 became nine panes with one closed.</p></div>
<div class="intro"><p><b>Stacked:</b> T1 stack, T2 shallow stack, T3 keel, T4 run (three), T5 solid stack.</p>
<p><b>Tessellated:</b> T6 diamond of eight, T7 hexagon of six, T8 triangle of nine, T9 quarter.</p>
<p><b>Cluster:</b> T10 inverted pyramid, T11 slid triad.</p>
<p><b>Carved:</b> T12 kept core, T13 carved stack, T14 carved quarter (discs), T15 nine-pane window (square).</p>
<p><b>Own derivatives:</b> T16 plinth, T17 reflection, T18 carved plinth.</p></div>'''

# per concept: rationale, originality, 16px verdict, masthead test, [(name, category, difference) x 3]
NOTES = {
    'T1': (
        "The owner's second sketch, kept close: two outlined triangles, the lower rising into the upper, the overlap "
        "filled. Two frames that share ground, and the shared part is the solid thing: the user and the product, and "
        "what the site is about is where they overlap. The fill touches both frames, so in one color the overlap "
        "merges into the outlines exactly as the sketch did.",
        "Two triangles, both upright and stacked on one axis, with no interlacing and no third triangle; the fill is "
        "only the overlap. Nothing is nested concentric, so it does not read as an alchemical or occult sign.",
        "Reads as two stacked triangles with a red point inside. Fair; the overlap is a dot at 16px.",
        "Between the two. The heavy frames hold up at header size, but outlined triangles are a common badge style; "
        "it needs the plain wordmark to stay serious.",
        [("Valknut", "Norse symbol", "three interlaced triangles turned about a center; ours is two, upright, stacked on one axis, not interlaced"),
         ("Alchemical air sign", "public symbol", "one triangle crossed by a bar; ours is two whole triangles and a filled overlap"),
         ("Delta Air Lines", "airline", "one solid triangle split in two tones; ours is two outlines with a filled overlap")]),
    'T2': (
        "The same sketch made quieter: a lighter stroke and a shallow overlap, so the filled triangle is small and "
        "floats inside the crossing with paper around it. One navy throughout, set with the serif, so it reads as a "
        "printer's device rather than a badge.",
        "As T1, and the floating fill separates it further from the solid two-tone Delta triangle. The thin stroke is "
        "the most generic part; the shallow crossing is what is ours.",
        "Weak to fair. The two outlines survive; the floating fill disappears below 24px.",
        "Masthead in tone (navy, serif, light line), but the light stroke is fragile beside The Economist or Stripe.",
        [("Valknut", "Norse symbol", "three interlaced triangles; ours is two stacked triangles, not interlaced, one floating fill"),
         ("Alchemical air sign", "public symbol", "a triangle crossed by a bar; ours is two complete triangles"),
         ("Delta Air Lines", "airline", "solid and two-tone; ours is line work with a small floating fill")]),
    'T3': (
        "The stacked pair with the filled triangle turned over and hung from the upper frame's base into the lower "
        "one, like a keel under a hull. The only stacked concept with a point aimed down: the reader's attention "
        "directed into the work.",
        "No warning sign reads here: the filled triangle is small, points down and sits inside two upright frames; "
        "there is no exclamation, no red border, no single dominant triangle. Not nested concentric.",
        "Fair. The two frames read; the keel becomes a colored speck.",
        "Pitch deck, slightly: the down-pointing accent asks to be decoded, which round four taught us to avoid.",
        [("Valknut", "Norse symbol", "interlaced and rotated; ours is two upright triangles and one hanging fill"),
         ("Alchemical earth sign", "public symbol", "a down triangle crossed by a bar; ours keeps both frames upright and the fill below the bar"),
         ("Warning triangle", "road and safety sign", "one red-bordered triangle with a mark inside; ours is two ink frames and a small inverted fill")]),
    'T4': (
        "The brief asked for three stacked. Stacked vertically they read as a fir tree, so they run in a row instead, "
        "each overlapping the next, and the two overlaps are filled: a sequence of steps that share ground, the way "
        "the site moves from design to product to business.",
        "Three equal outlined triangles on one baseline with filled overlaps; no rounded mountain line and no peak "
        "higher than the others, which is what separates it from Nuxt and Alpine Linux.",
        "Weak. At 16px it is a zigzag; the fills vanish. Needs a different favicon if chosen.",
        "Pitch deck. A wide row of peaks reads as outdoor gear or a software brand, not a journal.",
        [("Nuxt", "web framework", "two rounded mountain peaks of one stroke; ours is three sharp equal frames with filled overlaps"),
         ("Alpine Linux", "operating system", "mountain peaks in a hexagon; ours has no container and equal peaks"),
         ("Valknut", "Norse symbol", "three triangles interlaced around a center; ours is three in a straight row")]),
    'T5': (
        "The stack drawn solid: the two triangles are one ink silhouette and only their overlap changes color, parted "
        "by a hairline of paper. The same idea as T1 with nothing outlined, which is how the feeling board says "
        "authority behaves: one solid shape, one owned color.",
        "Vercel is one plain triangle; Delta splits one triangle in two tones. Ours is two triangles whose overlap is "
        "a third triangle in its own color, and the silhouette is a stacked figure, not a single triangle.",
        "Good. A dark stepped triangle with a colored center at 16px.",
        "Masthead. Solid, quiet, one accent; it sits beside a serif without looking like an app.",
        [("Delta Air Lines", "airline", "one triangle split down a diagonal in two tones; ours is two stacked triangles, the overlap in the accent"),
         ("Vercel", "developer platform", "one plain solid triangle; ours is a stacked silhouette with an inset third triangle"),
         ("Arch Linux", "operating system", "one triangle with a curved notch at the foot; ours is two straight triangles and a hairline")]),
    'T6': (
        "The owner's tessellated diamond reduced to the fewest cells that still read as a tessellation: eight, two "
        "rows up and two rows down. One cell beside the waist in the accent, off center, so the mark has a single "
        "point of attention.",
        "Ethereum and Sketch are faceted gems drawn as solids; ours is a grid of equal cells parted by gaps, with no "
        "gem crown and no chevron. Not Renault's open rhombus.",
        "Weak. The tall diamond is only six pixels wide at 16px and the cells blur; the accent survives as a blue patch.",
        "Pitch deck. A faceted diamond reads as crypto or jewelry before it reads as a journal.",
        [("Ethereum", "cryptocurrency", "a gem of two solid facets meeting at a chevron; ours is eight equal cells with one accent"),
         ("Sketch", "design software", "a cut gem with a crown; ours is a symmetric tall diamond of equal cells"),
         ("Renault", "car maker", "an open outlined rhombus; ours is solid cells")]),
    'T7': (
        "Six cells meeting at one point: the smallest tessellation that closes on itself. One cell in oxblood. Read "
        "as a whole, a hexagon; read as parts, six equal triangles of which one is marked.",
        "No cube shading (Unity), no six-arm star (Snowflake), no curved petals. A hexagon split into six is a "
        "generic pie diagram, and the single colored cell is what keeps it from being only that.",
        "Good. A dark hexagon with one red cell; it reads at 16px.",
        "Between the two. Strong and quiet, but a hexagon of triangles also suggests data and charts.",
        [("Unity", "game engine", "a hexagon drawn as a cube in outline; ours is six flat solid cells, one colored"),
         ("Snowflake", "data platform", "six arms from a center; ours is six closed cells forming a hexagon"),
         ("Hexagon pie chart icon", "generic interface icon", "segments for data; ours has equal cells and one owned color")]),
    'T8': (
        "Three rows of cells, nine in all, with the middle cell of the base row in a lighter navy: the cornerstone. "
        "The structure is the point; the site is built cell by cell, from the ground.",
        "Sierpinski removes the down cells recursively; the Triforce leaves the center hollow. Ours keeps all nine "
        "cells solid and marks one at the base. Solidity is stacked rhombi, not a grid.",
        "Fair. Reads as a navy triangle with a pale patch at the base; the cells blur.",
        "Masthead, in navy with the serif; the grid is calm and the accent is quiet.",
        [("Sierpinski triangle", "public figure", "hollow down cells repeated at every scale; ours keeps every cell solid, one tinted"),
         ("Triforce", "game emblem", "three solid cells around a hollow; ours is nine solid cells with a tinted base cell"),
         ("Solidity", "programming language", "stacked rhombi and triangles in a column; ours is one regular triangle grid")]),
    'T9': (
        "One triangle subdivided once into four cells; the apex cell in press red, the three below in ink. The "
        "lightest of the tessellations, and the plainest statement: one part of the whole is marked.",
        "Changed from the Triforce in two ways at once: the center cell is solid, not hollow, and the apex carries the "
        "color. Seen side by side it reads as a split triangle, not three in a cluster.",
        "Good. A red tip on a dark base reads at 16px.",
        "Masthead. Red and ink with a serif is The Economist's register, and the mark is one shape.",
        [("Triforce", "game emblem", "three gold cells and a hollow center; ours fills the center and colors the apex"),
         ("Sierpinski triangle", "public figure", "recursive hollows; ours is one subdivision, all solid"),
         ("Google Drive", "cloud storage", "three colored bands with a triangular void; ours is four cells and no void")]),
    'T10': (
        "The owner's cluster, reduced and turned over. Three outlined triangles pointing down make one large downward "
        "triangle, and the solid triangle at the center points up. The large shape is the journalist's inverted "
        "pyramid, the structure of a news story: what matters most first, then the detail.",
        "Turned over and with the roles swapped against the Triforce (outlines where it is solid, solid where it is "
        "hollow), so neither the silhouette nor the pattern matches. No eye, no rays, nothing nested concentric.",
        "Good. An inverted triangle with a solid center reads at 16px.",
        "Masthead. It has a meaning a publication can own, the inverted pyramid, and still works when nobody knows that.",
        [("Triforce", "game emblem", "upright, three solid cells, hollow center; ours is inverted, three outlines, solid center"),
         ("Tron", "cryptocurrency", "an inverted triangle cut into facets by lines from one corner; ours is a regular four-cell grid"),
         ("Valknut", "Norse symbol", "three interlaced outlines; ours are separate and do not interlace")]),
    'T11': (
        "The triangle of three with a hollow center, changed until it is no longer the Triforce. Each cell slides a "
        "fifth of a side along the outer edge in one turning direction, so the hollow closes into a small turned gap and "
        "the outline steps. The top cell carries the bronze: one resting on two.",
        "The three cells no longer meet point to point and the outline is no longer a triangle, which were the "
        "Triforce's two defining features. Not Mitsubishi's three rhombi around a point.",
        "Good. Reads as a small pile of triangles, the top one colored.",
        "Pitch deck, slightly. The tilt and pile give it movement that a journal would not choose.",
        [("Triforce", "game emblem", "three cells meeting point to point around a hollow; ours are slid apart and the hollow is closed"),
         ("Mitsubishi", "industrial group", "three rhombi meeting at a center; ours is three triangles resting on each other"),
         ("Google Drive", "cloud storage", "three bands framing a void; ours is three solid cells and no void")]),
    'T12': (
        "One triangle carved from the disc as a channel, with the solid core left standing inside it. Taken from the "
        "owner's cluster (an outlined triangle holding a filled one) and reduced to a single cell, then folded into a "
        "disc the way Tiger Data folds its tiger.",
        "Avalanche is a white triangle split by a cut inside a red disc; Alcoholics Anonymous is a line triangle "
        "touching a line circle. Ours is a solid disc with a triangular channel that touches nothing and leaves its "
        "core solid.",
        "Good. A dark disc with a white triangle ring reads at 16px.",
        "Masthead. One disc, one cut, one color: the closest of the eighteen to the feeling board's devices.",
        [("Avalanche", "cryptocurrency", "a solid white triangle split by a diagonal cut; ours is a triangular channel with the core left standing"),
         ("Alcoholics Anonymous", "fellowship", "line triangle inscribed in a line circle; ours is a solid disc and a floating channel"),
         ("AdonisJS", "web framework", "a rounded triangle in a rounded square; ours is a sharp channel in a disc")]),
    'T13': (
        "The owner's stacked pair cut through the disc as two channels; the overlap and the centers of both triangles "
        "stand as solid islands. The sketch itself, carved.",
        "Two upright triangles, not interlaced, and solid islands where the valknut has crossings. The disc removes "
        "any read as a free-standing occult sign.",
        "Fair. The disc and a white triangle read; the inner lines merge.",
        "Between the two. Faithful to the sketch, but busier than the feeling board allows at small sizes.",
        [("Valknut", "Norse symbol", "three interlaced triangles; ours is two stacked channels cut in a disc"),
         ("AdonisJS", "web framework", "one rounded triangle in a square; ours is two sharp triangles in a disc"),
         ("Avalanche", "cryptocurrency", "one split triangle; ours is two stacked outlines")]),
    'T14': (
        "A triangle of four cells carved from the disc: the three lower cells cut clean through, the apex cell left "
        "standing inside a thin channel. The cut shows the structure; the standing cell is the one that matters.",
        "Unlike the Triforce, the center cell is cut and the apex is kept, so the light pattern is a row of three with a "
        "framed cell above. Unlike Avalanche, the figure is a grid, not a split.",
        "Fair. A disc with a light triangle; the cells close up at 16px.",
        "Masthead. Oxblood disc and serif read as a publisher's colophon.",
        [("Avalanche", "cryptocurrency", "a split triangle in a disc; ours is a four-cell grid with the apex kept"),
         ("Triforce", "game emblem", "three corners solid, center hollow; ours cuts the center and keeps the apex"),
         ("Solidity", "programming language", "a column of facets; ours is one regular grid in a disc")]),
    'T15': (
        "The triangle of nine cut through a solid square as a window of nine panes, the middle pane of the base row left "
        "closed. The one carved from a square: a block, like the Financial Times' monogram block, with the structure "
        "showing through.",
        "No hollow down cells repeated (Sierpinski), no three-cell cluster (Triforce): nine panes on one grid with a "
        "single closed pane.",
        "Weak. The panes merge into a pale triangle at 16px; the closed pane is lost.",
        "Masthead in form, a block in ink, but the fine grid needs size to read.",
        [("Triforce", "game emblem", "three solid cells; ours is a block with eight cut panes and one closed"),
         ("AdonisJS", "web framework", "one rounded triangle in a rounded square; ours is a sharp nine-cell window in a square"),
         ("Sierpinski triangle", "public figure", "recursive hollows; ours is one grid level")]),
    'T16': (
        "A solid triangle standing on a broad bar and touching it: a monument on its plinth. The triangle carries the "
        "press red, the bar the ink. In one color the two become one silhouette, which is the test of a settled shape.",
        "The eject key is a triangle over a bar of the same width with a gap; ours touches, and the bar runs far "
        "wider than the triangle. Not the alchemical air sign, which crosses the triangle with a short bar.",
        "Good. Red triangle on a black bar; reads at 16px.",
        "Masthead. Like a publisher's device on a spine: one object, one base, one color.",
        [("Eject key", "interface symbol", "triangle over an equal bar with a gap; ours touches a bar far wider than itself"),
         ("Alchemical air sign", "public symbol", "a bar crossing the triangle; ours is a base under it"),
         ("Vercel", "developer platform", "one triangle alone; ours stands on a plinth in two colors")]),
    'T17': (
        "An upward triangle and a downward one sharing one base: the upper solid, the lower an outline hanging from "
        "it. The made thing standing on its reflection, the product above and the user's view of it below.",
        "The sort icon is two solid triangles point to point with a gap; ours share a base, touch, and the lower is an "
        "outline. Not Ethereum's chevron facets or Renault's open rhombus.",
        "Good. A blue tip over a dark outline reads at 16px.",
        "Between the two. Clear and memorable, but a diamond with a colored half can read as a map pin or a gem.",
        [("Sort icon", "interface symbol", "two solid triangles with a gap; ours touch at a shared base and the lower is an outline"),
         ("Ethereum", "cryptocurrency", "a gem split at a chevron; ours splits on a straight base, solid over outline"),
         ("Renault", "car maker", "an open rhombus of strokes; ours is half solid, half outline")]),
    'T18': (
        "The plinth carved: a channel cut rim to rim near the foot of the disc and a triangle rising from it. The disc "
        "becomes a dome with a pointed hollow, resting on a low segment.",
        "Codeberg cuts a mountain wedge that runs out to the rim; ours rises from a level channel and stops inside the "
        "disc. Avalanche's triangle floats and is split; ours sits on a base.",
        "Good. A bronze disc with a white tent shape and a line reads at 16px.",
        "Between the two. The cut is clean, but a triangle on a line in a disc can read as a tent or a mountain.",
        [("Codeberg", "code hosting", "a mountain wedge running out to the rim; ours rises from a level channel and stops inside"),
         ("Avalanche", "cryptocurrency", "a split triangle floating in the disc; ours stands on a cut base"),
         ("Arch Linux", "operating system", "one triangle with a curved notch; ours is a hollow in a disc on a level base")]),
}
