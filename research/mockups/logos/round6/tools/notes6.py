"""Notes for the round-six board: rationale, originality, 16px verdict, masthead test, closest logos.

Closest logos come from an image check: about ninety logo files and public symbols were downloaded,
rendered side by side and looked at (Tiger Data, Oyster HR, Carraro, the IEC power symbol, Neo4j,
Asana, Atari, Maserati, Mercedes-Benz, Mitsubishi, Target, Lucid, Mastercard, the peace symbol,
the radiation and biohazard signs, the Deathly Hallows sign, CircleCI, Umbraco, Coursera, Vodafone,
Opera, CodePen, Chase, Hashnode, GraphQL, HubSpot, Linear, Raycast, Udemy, Fig, Pocket and others
from HR tech, consulting, fintech, publishing and developer tools). Names only on the board.
"""

# per concept: rationale, originality, 16px verdict, masthead test, [(name, category, difference) x 3]
NOTES = {
    'R1': (
        "Round five's braced tripod, the owner's pick, turned into a cut. The disc is the solid thing; the "
        "tripod is the light coming through it: an apex, a spine, two struts, the two braces and three round "
        "feet, all one hole. The braces leave three small solid triangles standing inside the figure, which "
        "is what makes it read as built rather than drawn. Heavy strokes, so the cut stays open small.",
        "No cross and nothing above the apex; the feet are solid round holes, not open rings; the source's "
        "tall triangle is now wide and low, braced at the feet and enclosed in a disc. Unlike Tiger Data it "
        "has no animal and no parallel slicing: one symmetric frame floating in the middle.",
        "Reads at 16px as a pale diamond with three dots; the inner triangles close up below 20px, so the "
        "favicon thickens the frame. Good.",
        "Masthead, just. It is the most engineered of the ten and could pass for a standards body; the risk is "
        "that a network diagram in a disc tips toward a data product.",
        [("Neo4j", "graph database", "theirs is open nodes on lines with no container; ours is one hole cut from a solid disc, braced into triangles"),
         ("GraphQL", "developer tools", "a triangle inside a hexagon with six nodes; ours is a tripod with a spine, three feet and no outer frame line"),
         ("Tiger Data", "database software", "an animal head and diagonal slices; ours is symmetric pure geometry centered in the disc")]),
    'R2': (
        "Round five's tree of three, hung from the top of the disc. Three lines fan from a point on the rim "
        "to three round holes, and a solid disc stands inside each hole, so every terminal is a disc held in "
        "a disc. The middle terminal sits higher, nearer the root: the reader closest to the source. The only "
        "concept where the figure touches the rim at its root.",
        "Changed from the source: no cross and no braces; the root sits on the rim instead of under a "
        "cross; the middle terminal is higher than the outer two (the source's is lowest); the terminals "
        "are holes with standing discs, not drawn rings. Of the ten, this keeps the most of the source's "
        "layout (three lines to three round ends), so it is the one to watch.",
        "Weakest at 16px: the standing discs turn to noise, so the favicon drops them and keeps three round "
        "holes on three lines. Fair.",
        "Borderline. Fraunces and deep green make it feel like a learned society, but three round terminals "
        "on threads still read as a pendant or a mobile at header size.",
        [("Target", "retail", "one ring around one dot, concentric; ours has three small hole-and-dot terminals hung on lines from the rim"),
         ("HubSpot", "marketing software", "a sprocket: one ring with three spokes ending in dots; ours fans three lines downward from the rim with no hub ring"),
         ("CircleCI", "developer tools", "one slot from the rim into one ring around a dot; ours has three lines and three terminals")]),
    'R3': (
        "The tripod with everything removed but its legs: a spine and two struts, no rings, no braces. The "
        "apex is cut flat so it never comes to a point (a point makes it an arrow), the struts splay wide, "
        "and all three feet are cut flat on one horizontal line inside the disc. It stands; it does not point.",
        "Checked against the peace symbol (a full vertical with legs from the center, inside a ring), the "
        "UK broad arrow and an up-arrow icon (three lines meeting at a point), Atari (three separate prongs "
        "that flare at the base) and the Deathly Hallows sign (triangle, circle and line). Ours has a flat "
        "head, nothing above it, splayed legs of equal weight, a flat baseline and no outer ring. A pointed "
        "draft read as an up arrow and was dropped.",
        "Strong at 16px: a pale flat-topped stand on a dark disc, still legible as three legs. Good.",
        "Masthead. Flat cuts and one baseline give it the plainness of a survey mark or a museum sign; in "
        "oxblood with Fraunces it is the most publication-like of the tripods.",
        [("Atari", "video games", "three separate prongs that flare at the base, unjoined at the top; ours are joined under a flat head and splay downward"),
         ("Peace symbol", "public symbol", "a vertical through the whole ring with two legs from its center; ours has no line above the head, no ring and flat feet"),
         ("Deathly Hallows sign", "fan symbol", "a closed triangle with a circle and a line inside; ours has no base line and no inner circle")]),
    'R4': (
        "The tripod's three feet alone. Three ring cuts in one low row, the middle one dropped, each leaving "
        "a solid disc standing in its hole; no struts at all. The broad solid dome above them stands in for "
        "the frame they carry. The most reduced of the four tripod readings.",
        "Arrangements of three rings were tried and dropped: a two-over-one cluster read as a face, and "
        "rings biting into the rim read as wheels. A low row with the middle one dropped is what survived. "
        "Nothing of the source's struts or cross remains.",
        "Reads at 16px as three small rings low in a disc; the inner dots hold as single pixels. Fair.",
        "Borderline. Ink on white is as settled as a mark can be, but three rings in a row can read as a "
        "status light or as decoration; it needs the wordmark to carry it.",
        [("Asana", "work management", "three solid dots in a triangle, no container; ours is three ring cuts in a low row inside a solid disc"),
         ("Target", "retail", "one large ring around a dot; ours is three small ones, set low and off the disc's center"),
         ("Olympic rings", "sport", "five interlaced open rings; ours are three separate cuts that never touch")]),
    'R5': (
        "A line of reading enters from the left edge of the disc and stops square, then a full point. A "
        "sentence, finished: the smallest possible picture of writing that is not a letter. The line breaks "
        "the rim, so the disc reads as a page the line runs onto.",
        "The bar ends square, not round, so it does not read as a slider or a toggle switch. Searches for "
        "line-and-dot marks in a disc found no close match; Konica Minolta's disc has horizontal stripes "
        "but no point, and Linear's has diagonal cuts. Distinct from Tiger Data: one horizontal cut, no "
        "picture.",
        "Strong at 16px: a white dash and a dot on red, the clearest of the ten. Good.",
        "Masthead. A full stop is the most editorial device there is, and press red with Instrument Sans "
        "carries the newspaper flag of The Economist without copying its block.",
        [("Konica Minolta", "imaging", "a disc with several horizontal stripes and no point; ours is one line from the edge, then a point"),
         ("Linear", "work management", "a disc cut by parallel diagonals from one edge; ours is one horizontal line that stops, then a point"),
         ("Hashnode", "developer publishing", "a rounded square with one round hole; ours is a disc with a line and a point")]),
    'R6': (
        "One straight cut from rim to rim, off center at the golden section, so the disc becomes a narrow "
        "part and a broad part: the margin and the text block of a page, or user and product, unequal and "
        "together. The plainest figure on the board; it leaves almost everything out.",
        "A centered split is everywhere; the off-center cut and the single straight rule are what keep this "
        "apart. Checked against Linear (several diagonal cuts), Tiger Data (diagonal slices and a head) and "
        "Fig (a slot inside a rounded square). It is close to generic, which is both the point and the risk: "
        "it would need years of use to become ours.",
        "Strong at 16px: a disc with one light line, always legible. Good.",
        "Masthead. Bronze, cream and Fraunces make it look like a university press colophon. Weakness: it may "
        "be too plain to own or register.",
        [("Linear", "work management", "a disc cut by several parallel diagonals; ours is one vertical cut, off center"),
         ("Tiger Data", "database software", "diagonal slices plus an animal head; ours is one straight rule and nothing else"),
         ("Fig", "developer tools", "a vertical slot inside a rounded square; ours is a full rim-to-rim cut through a disc")]),
    'R7': (
        "A spine with one terminal: a slot drops from the top rim and opens into one round hole below the "
        "center, a plumb line and its bob. It is the single-leg reduction of the tripod, so it sits in the "
        "same family as R1 to R4 without showing the source.",
        "A first draft with a ring and a standing dot was one rotation away from CircleCI's mark (a slot from "
        "the rim into a ring around a dot), so the dot was removed. Checked against the power symbol (a line "
        "into the gap of an open ring) and a keyhole (round hole above, flared slot below): ours is a closed "
        "hole with the slot entering from above, no ring.",
        "Strong at 16px: a light drop on a dark disc. Good.",
        "Masthead in ink on cream, but the closeness to a power button at a glance is "
        "a real cost.",
        [("IEC power symbol", "public symbol", "an open ring with a line in its gap; ours is a solid disc with a closed round hole the slot runs into"),
         ("CircleCI", "developer tools", "a slot from the left rim into a ring around a dot; ours drops from the top into a plain round hole"),
         ("Keyhole", "public symbol", "round part above a flared slot; ours is a straight slot from the rim down to a round hole")]),
    'R8': (
        "Two shapes meeting across an empty center: two right-angle brackets, like a printer's crop marks, "
        "one cut clean through and one cut as a lighter tone. The empty middle is the subject: the place "
        "where user and product meet. The one two-tone concept.",
        "Checked against CodePen (an outline cube cut into a disc), Chase (four pieces around a square hole) "
        "and Lucid (stacked L blocks). Two brackets on one diagonal, one in a second tone, inside a disc, "
        "matched none of them. In one color the lighter bracket becomes a full cut.",
        "Fair at 16px: both brackets read; the tint softens to a pale blue patch. Good on dark.",
        "Borderline, toward pitch deck: crop marks are honest editorial tools, but corner brackets also mean "
        "'full screen' in every interface, and blue pushes it toward software.",
        [("Chase", "banking", "four rotated pieces around a square hole in an octagon; ours is two brackets on a diagonal in a disc"),
         ("CodePen", "developer tools", "an isometric cube outline cut into a disc; ours is two flat corner brackets, one tinted"),
         ("Lucid", "software", "an L built from blocks with no container; ours is a pair of brackets framing an empty center")]),
    'R9': (
        "The passing: one slot drops from the top rim, another rises from the bottom rim, offset, and they "
        "pass each other through the middle without meeting. Two halves of one disc that hold each other: "
        "the two sides of the name, each reaching past the center toward the other.",
        "A stepped draft that joined the two slots read as a lightning bolt or a crack and was dropped. "
        "Checked against Hotjar (two S strokes), Fig (one slot) and the pause symbol (two equal bars side by "
        "side, floating): ours are offset vertically, each tied to the rim.",
        "Fair at 16px: two light bars that read as offset; at very small sizes it can look like a broken "
        "line. Fair.",
        "Masthead. Pure and calm in deep green with Instrument Sans; it suggests exchange without a picture "
        "of anything.",
        [("Hotjar", "product analytics", "two curved S strokes with no container; ours are two straight cuts from opposite rims"),
         ("Pause symbol", "public symbol", "two equal bars side by side, floating; ours are offset, each running out through the rim"),
         ("Fig", "developer tools", "one slot in a rounded square; ours is two offset slots through a disc")]),
    'R10': (
        "A square channel cut into the round, open at one corner: the made thing inside the human one, not "
        "quite closed. The square inside stays solid; the gap at the lower right lets it breathe and gives "
        "the mark a direction.",
        "Checked against CodePen (a cube outline in a disc), Chase (a square hole made of four pieces) and the "
        "'stop' symbol (a solid square in a circle): ours is an outline channel, open at one corner, with "
        "the square left standing.",
        "Good at 16px: a light square outline with its corner open; reads clearly.",
        "Borderline. Navy and Fraunces keep it formal, but a square in a circle is close to an interface "
        "icon; it is the least distinctive of the imagination set.",
        [("CodePen", "developer tools", "an isometric cube outline in a disc; ours is a flat square channel, open at one corner"),
         ("Chase", "banking", "four pieces around a square hole; ours is one channel with the square standing inside"),
         ("Stop symbol", "public symbol", "a solid square in a circle; ours is an outline cut with an open corner")]),
}
