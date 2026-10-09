"""Notes for the round-five board: rationale, originality, masthead test and closest existing logos.

Closest logos come from an image check: logo files and site icons were opened and looked at
(Oyster HR, Carraro, Asana, Neo4j, Atari, Mercedes-Benz, Maserati, Mitsubishi, Target, the IEC
power symbol and the peace symbol), plus description searches for the source symbol and for
tripod, node, disc-with-slot and three-circle marks. Names only on the board; no logo images.
"""

# per concept: rationale, originality, masthead test, [(name, category, difference) x 3]
NOTES = {
    'Q1': (
        "The structure read as a plumb line: three cords drop from one bare point, each to a weight. The cords "
        "are hairlines and the weights are solid and heavy, the middle one larger and lowest, so the eye goes "
        "down and the mark settles. Nothing sits above the point. Read it as user, product and the reader held "
        "true by one line, or just as a plumb.",
        "Changed from the source: the cross-bar is gone and nothing rises above the apex; the two short braces "
        "between the feet are gone; the open rings are solid weights of two sizes; the proportion is tall and "
        "narrow (about 0.6:1) instead of the source's broad triangle; strokes are hairline against heavy discs. "
        "Of the source only 'three lines from a point' remains, which is generic geometry.",
        "Masthead. A hairline and three weights has the quiet of a museum or a science press; it needs Fraunces "
        "beside it, and the hairlines drop out below 24px, which is why the favicon is the plumb bob alone.",
        [("Neo4j", "graph database software", "theirs has a node at the junction and dots of one size; ours hangs from a bare point with weights of two sizes"),
         ("Asana", "work management SaaS", "three equal dots in a triangle with no lines; ours is carried on cords, heaviest weight lowest"),
         ("Peace symbol and Yr rune", "public symbols", "a spine with two downward diagonals, the first inside a circle; ours has no circle, no stem above the apex, and weights at every foot")]),
    'Q2': (
        "The stand or easel reduced to its legs: two struts that cross just under the top, as easel legs do, and "
        "a rear leg dropping from the crossing to a single solid foot. Uniformly heavy strokes, all cut flat to "
        "one baseline, so it stands on the line of type. The only circle is the foot of the spine.",
        "Changed from the source: no cross-bar, no rings at the outer feet, no braces; the struts cross and "
        "overshoot at the top instead of meeting; every stroke is heavy and flat-ended. The source's lightness "
        "and its three rings are both gone.",
        "Borderline. Heavy and settled, but the crossed top reads a little like a tent or a tipi at header size; "
        "it would suit a design school more than a journal.",
        [("Atari", "video games", "three prongs that curve and flare; ours are straight legs that cross at the top, with a weighted rear leg"),
         ("Mercedes-Benz", "automotive", "three spokes from a center inside a ring; ours is open, unringed and stands on a baseline"),
         ("Broad arrow", "UK government property mark", "a stem with two barbs from its tip; our legs cross above the apex and the stem ends in a solid foot")]),
    'Q3': (
        "A tree of three terminals from one root. The outer two are hollow rings (user, product), the middle one "
        "a solid disc (the reader), and the solid one sits higher, nearer the root, so the reader is the closest "
        "and the most filled-in. Medium line, Fraunces in the same deep green on cream.",
        "Changed from the source: no cross-bar, no braces; the middle terminal is raised instead of lowest; one "
        "terminal is solid and two hollow; the spread is wider and the spine shorter than the struts. The "
        "source's arrangement (center lowest, three equal rings) is reversed.",
        "Borderline masthead. The ring-and-disc logic is clear at 560px, but in a header strip it starts to look "
        "like a diagram, and at 16px it is a green smudge with two dots.",
        [("Neo4j", "graph database software", "a node sits at their junction and all nodes match; ours has a bare root and mixes hollow and solid"),
         ("Share icon", "standard interface symbol", "three equal dots joined in a chain by two lines; ours is three lines from one point"),
         ("Asana", "work management SaaS", "three equal dots without lines; ours is a drawn structure with one solid terminal")]),
    'Q4': (
        "The structure kept closest to what the owner liked, then flattened: a surveyor's tripod braced at the "
        "feet, so wide and low (about 2:1) that it stands rather than points. Uniformly heavy line with round "
        "joins and three solid feet of one size. Instrument Sans Bold in navy.",
        "Closest to the source of the six, so the changes are larger: no cross-bar, nothing above the apex, the "
        "proportion doubled in width, the center foot raised so the braces form a shallow V, solid feet in place "
        "of open rings, and one heavy stroke for everything. Side by side with the source it reads as a "
        "different, squatter object.",
        "Pitch deck, narrowly. It is honest and heavy, but the nodes-and-edges look belongs to network software; "
        "at 16px it closes into a navy diamond.",
        [("Neo4j", "graph database software", "an open chain of nodes; ours is a closed braced frame with three feet and no node at the apex"),
         ("Mitsubishi", "industrial group", "three solid diamonds around a point; ours is a line frame with round feet"),
         ("Source stroke diagram", "spiritual symbol (owner's reference)", "ours drops the cross, doubles the width, raises the center foot and fills the rings")]),
    'Q5': (
        "A chandelier or a balance: one cord from above, two arms lifting two rings, and a third ring hanging "
        "below. The arms meet the cord low down, so the structure hangs instead of standing. Fine red line and "
        "three heavy hollow rings; the name in Fraunces in ink, the red kept for the mark alone.",
        "Changed from the source: no struts from the top at all (the arms branch low and rise), no cross-bar, no "
        "braces; the cord runs from above the whole mark; the side rings are higher than the joint. Only "
        "'three rings and a vertical' survives.",
        "Masthead, by a margin. Red line and rings beside a serif reads as a press or a museum, but the "
        "branching arms can be read as a trident or a candelabrum, which is an object.",
        [("Maserati", "automotive", "a trident with pointed tines above the joint; ours lifts rings on two short arms and hangs a third"),
         ("Neo4j", "graph database software", "nodes on a chain; ours hangs from a cord with three equal rings"),
         ("Psi and candelabrum marks", "generic symbol family", "arms curve up from the stem; ours are straight, short and end in rings")]),
    'Q6': (
        "The pure reduction the brief asked for: one vertical, two diagonals, three equal circles, nothing else. "
        "The lines stop short of the circles, so the circles are free weights under the structure rather than "
        "beads on it. Signal blue for the mark, black Instrument Sans for the name: the blue, black and white "
        "the owner likes.",
        "Changed from the source: no cross-bar, no braces; the three circles are solid, equal and set on one "
        "baseline instead of a V; the lines are detached from them by a gap. The detachment is the one detail "
        "that is ours.",
        "Pitch deck. Clean and legible, but three blue dots under lines is the shape of an org chart or a "
        "network icon; it reads as software.",
        [("Asana", "work management SaaS", "three dots in a triangle with no lines; ours sets three dots in a row under three detached lines"),
         ("Neo4j", "graph database software", "lines run into the nodes; ours stop short of the circles"),
         ("Org chart and sitemap icons", "standard interface symbol", "boxes on right-angled connectors; ours are diagonals from one point to circles")]),
    'Q7': (
        "Round four's weighted ring rebuilt around a second structural feature, as the owner's feedback asked: "
        "the opening becomes one straight slot cut from the top edge through to the exact center, round at its "
        "foot. The disc stays whole below the center, so the weight still settles at the bottom, and the slot "
        "is the tripod's spine drawn as a cut.",
        "P6 was close to Oyster HR's mark (a black oval with one round opening), so the round opening is gone "
        "entirely; no plain disc-with-gap is shipped. The nearest form is now the standby or power symbol, which "
        "is a stroked broken ring with a free bar; ours is a solid disc with a negative slot and no bar, which is "
        "more than one change away. The searches found no company mark of a disc with a radial slot to the center.",
        "Masthead. A solid green disc with one cut is as plain as a seal; the risk is that a hurried eye reads it "
        "as a power button, so it must never sit next to interface icons.",
        [("Power symbol (IEC standby)", "standard interface symbol", "a stroked ring broken at the top with a free bar; ours is a solid disc with a cut slot and no bar"),
         ("Oyster HR", "HR technology", "a solid oval with one round opening set low; ours has no round opening, only a radial slot from the top"),
         ("Carraro", "engineering", "a red disc with chevron cuts on its right edge; ours has one straight vertical cut to the center")]),
    'Q8': (
        "The ring holding the structure: three legs from one bare point, the outer two ending in small solid "
        "weights, the center leg ending in the weighted ring (heavy, with its opening set high). It is the tripod "
        "with the ring as its heaviest terminal, so the eye drops through the lines into the ring and stops. "
        "Fraunces in navy.",
        "The plain ring-holding-a-point was dropped under the new rule (no disc-with-gap alone). Here the ring "
        "only exists as the foot of the three-legged structure, which neither Oyster nor any disc mark has. "
        "From the source: no cross-bar, no braces, one foot hugely enlarged, outer feet small and solid.",
        "Masthead. It has the gravity of a plumb or a scale weight and stays one color; the hairline legs need "
        "the 16px version's doubled strokes.",
        [("Oyster HR", "HR technology", "a solid oval with a low round opening, alone; ours hangs a ring with a high opening from three lines"),
         ("Target", "retail", "a ring around a centered disc; ours has no inner disc and the ring is a foot of a structure"),
         ("Neo4j", "graph database software", "equal nodes on a chain; ours has two small weights and one heavy ring under a bare apex")]),
    'Q9': (
        "The square counterpart of Q7: a solid oxblood block with one flat-ended slot cut from the top edge to "
        "the center, like a mortise waiting for its tenon. The lower half is untouched, so the block keeps its "
        "weight. Fraunces in the same oxblood on cream.",
        "The round-four square with an offset opening would have been a disc-with-gap in square form, so it was "
        "replaced by a slot. Searches for squares with a single slot found monogram blocks and letter-U marks, "
        "not this; the closest publishing marks are text-in-a-block, which ours avoids.",
        "Borderline. A block in oxblood is bookish, but the slot can read as a letter U or a parking bay; it is "
        "the weakest of the four ring developments.",
        [("The Economist", "publishing", "a red rectangle holding the name; ours holds nothing and carries one cut slot"),
         ("Harvard Business Review", "publishing", "letters in a block; ours is a block with no letters and one slot"),
         ("U monograms in a square", "generic letter marks", "a drawn U with a round bottom; ours is a narrow flat-ended slot that stops at the center")]),
    'Q10': (
        "The two ideas fused, kept as simple as they allow: round four's weighted ring carried as the head of "
        "three heavy legs, all cut to one baseline. The ring is heavy at the bottom where the legs leave it, so "
        "the whole mark reads as one standing instrument. Bronze for the mark, Instrument Sans in ink.",
        "The ring's opening is high and small, unlike Oyster's low opening, and the ring is never shown alone; "
        "the legs are straight and outside the ring, unlike Mercedes-Benz's spokes inside one. From the source "
        "only the three legs remain, now heavy and flat-footed under a ring.",
        "Pitch deck, narrowly. It is heavy and simple, but it reads as a figure or a lander at header size, which "
        "is a picture; the owner may find it charming, the journal test does not.",
        [("Mercedes-Benz", "automotive", "three spokes inside a ring; our three legs stand outside and below the ring"),
         ("Oyster HR", "HR technology", "a solid oval with a low round opening, alone; ours has a high opening and stands on legs"),
         ("Atari", "video games", "three flaring prongs with no head; ours are straight legs under a ring")]),
}
