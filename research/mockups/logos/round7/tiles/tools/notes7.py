"""Notes for the round-seven tiles board: rationale, originality, 16px verdict, masthead test, closest logos.

Closest logos come from an image check: logo files were downloaded, rendered on one contact sheet and
looked at (Microsoft, the Windows 11 and Windows 8 flags, Slack, Chase, Google Photos, Dropbox,
Binance, Zoho, Kentico, Trello, Mitsubishi, Columbia, Mastercard, Airtable, Buffer, Tiger Data,
Linear, Craft CMS, Deutsche Bank, Toyota, the sun cross and about seventy others from software,
consulting, finance and publishing). Names only on the board.
"""

# per concept: rationale, originality, 16px verdict, masthead test, [(name, category, difference) x 3]
NOTES = {
    'S1': (
        "The pinwheel tiling at its plainest: four 7:5 tiles, each turned a quarter from the last, so the "
        "four together make one square that seems to turn. Turned 18 degrees off the page so it rests "
        "rather than spins. Soft corners keep it from looking like a floor plan.",
        "The 7:5 tiles alternate direction, so the seams jog at the center instead of running straight "
        "through as in Microsoft. No square hole and no chamfered octagon, which is what Chase is.",
        "Good: four dark blocks in a turned square, the jog still visible at 32px, a solid cluster at 16px.",
        "Masthead, quietly. Navy and a plain grotesque make it read as an institute's seal; the tilt is the "
        "only gesture.",
        [("Chase", "banking", "four chamfered pieces round a large square hole, forming an octagon; ours has no hole, no chamfer, and four separate rounded tiles"),
         ("Microsoft", "software", "four equal squares on a straight grid with a straight cross of space; ours alternates 7:5 tiles and is turned 18 degrees"),
         ("Zoho", "business software", "four tilted letter tiles in a row; ours is a closed square cluster with no letters")]),
    'S2': (
        "The owner's sketch, made exact but not stiff: four 7:5 tiles in the pinwheel tiling, the whole "
        "turned 40 degrees, each tile spun a further 4 so it keeps a little of the hand. Ink on cream with "
        "Fraunces: the bookish version of the idea.",
        "Turned near 45 degrees, four tiles risk reading as Microsoft on its point or the Dropbox diamonds. "
        "The alternating 7:5 tiles and the small spin break the straight seams that both of those have.",
        "Good: reads as a diamond of four blocks; the individual spin is lost below 24px but the cluster holds.",
        "Masthead. In ink with a serif it looks like a printer's ornament on a title page.",
        [("Microsoft, turned", "software", "equal squares and two straight seams; ours has alternating 7:5 tiles and jogged seams"),
         ("Dropbox", "file storage", "two pairs of diamonds that open into a box with a lower flap; ours is one closed cluster of rounded tiles"),
         ("Binance", "crypto exchange", "a center diamond, four diamonds and four chevrons; ours has no center tile and no chevrons")]),
    'S3': (
        "Square-on and sharp: four 4:3 blocks laid like a quilt block or a paving pattern, the seams "
        "jogging around a pinhole center. The most architectural of the set; bronze on cream for weight.",
        "Square-on is where Microsoft and Chase live. 4:3 tiles make the center a pinhole, not Chase's large "
        "square hole, and the outline stays square, not octagonal; the jogged seams are not Microsoft's cross.",
        "Good: a solid square with a pinwheel of hairline seams; the seams close at 16px and it reads as a block.",
        "Masthead, sober. It could be a building society or a standards body; the risk is that it reads as a "
        "layout icon in a software toolbar.",
        [("Chase", "banking", "an octagon round a large square hole; ours is a square with a pinhole and no chamfer"),
         ("Microsoft", "software", "four equal squares, straight cross; ours 4:3 tiles with jogged seams"),
         ("Trello", "project software", "two bars inside a rounded square frame; ours is four tiles and no frame")]),
    'S4': (
        "The four tiles moved to the sides of a square, leaving the middle empty and the corners open: a "
        "frame around the reader's space. Mirror symmetric, so unlike the pinwheels it never turns.",
        "Built in place of a 1:2 pinwheel round a hole, which was Chase. The open frame is close to the "
        "generic focus and crop icons and, at small sizes, to loading spinners.",
        "Fair: four dots in a ring at 16px; the frame is legible from 32px.",
        "Borderline. Green and a grotesque keep it calm, but the open corners read as a camera viewfinder or a "
        "loading spinner more than as a seal.",
        [("Google Photos", "software", "four curved petals turning round a point; ours is four straight tiles, mirror symmetric, with an empty center"),
         ("CodeSandbox", "developer tools", "one closed square outline; ours is broken at the corners into four tiles"),
         ("Focus and crop icons", "generic UI", "corner brackets; ours keeps the sides and opens the corners")]),
    'S5': (
        "Two sizes: the diagonal pair large, the other pair small, on a diamond grid with each tile spun 12 "
        "degrees. The big pair is the user and the product; the small pair is everything between.",
        "Unequal tiles break the even rhythm that Microsoft, Binance and Mitsubishi all rely on.",
        "Good: reads as a diamond with a long axis; the small pair holds at 16px.",
        "Masthead. Oxblood and Fraunces make it feel like a learned society's device.",
        [("Mitsubishi", "industrial", "three equal diamonds meeting at the center; ours is four tiles in two sizes, separated"),
         ("Binance", "crypto exchange", "equal diamonds round a center tile; ours has no center and two sizes"),
         ("Microsoft, turned", "software", "four equal squares; ours pairs large and small, each spun")]),
    'S6': (
        "The sketch in ink with one tile in press red: the user among the product. One color carries the "
        "meaning; the other three stay quiet.",
        "Microsoft and Slack use four colors, one per tile; this uses one ink and one accent, which is how "
        "newspapers use red.",
        "Good: the red tile survives at 16px as a clear spot on the dark cluster.",
        "Masthead. Ink and one red is the newspaper palette; the red tile reads as an editorial mark.",
        [("Microsoft", "software", "four colors on a straight grid; ours is three ink tiles and one red, turned"),
         ("Slack", "software", "four colors in a pinwheel of rounded bars and dots; ours is four tiles, one color plus one accent"),
         ("Windows XP flag", "software", "four colored panes on a waving flag; ours is flat, turned, single accent")]),
    'S7': (
        "The sketch drawn as rings of one heavy weight, as the owner drew it in pen. Blue rings beside an ink "
        "word.",
        "Outlined tile clusters are common as app-grid icons; the alternating 7:5 tiles and the turn keep it "
        "off the straight grid.",
        "Fair: the counters close to slits at 16px; it reads as four dark tiles, not rings.",
        "Pitch deck, leaning. Outlines feel lighter and more like an interface icon than an institution.",
        [("App-grid icons", "generic UI", "four outlined squares square-on; ours alternates 7:5 rings, turned 40 degrees"),
         ("Zoho", "business software", "four tilted tiles in a row with letters; ours is a closed cluster, no letters"),
         ("Microsoft", "software", "solid equal squares; ours is outlined and alternating")]),
    'S8': (
        "Four square rings on their points: a diamond of diamonds. Soft corners and heavy rings give it the "
        "look of a stamped seal.",
        "Square tiles at 45 degrees are Microsoft turned, so the rings and the wide gaps carry the difference; "
        "it is the closest to the edge of the outlined set.",
        "Fair to good: four rings read at 32px; at 16px a grey diamond with four dots.",
        "Borderline. Oxblood and Fraunces help; the shape itself is generic.",
        [("Audi", "automotive", "four overlapping rings in a row; ours is four separate square rings in a diamond"),
         ("Binance", "crypto exchange", "solid diamonds round a center tile; ours outlined, no center"),
         ("Dropbox", "file storage", "solid diamonds in two pairs; ours four rings, one closed cluster")]),
    'S9': (
        "Mixed weights: the same spun squares, the diagonal pair in a heavy ring, the other pair light. Two "
        "voices, one shape.",
        "No four-square mark seen in the check uses two stroke weights.",
        "Fair: the light pair thins to a grey line at 16px; the heavy pair carries it.",
        "Pitch deck. It is clever, and cleverness is what the feeling board says to leave out.",
        [("Microsoft", "software", "solid equal squares; ours outlined in two weights and spun"),
         ("Audi", "automotive", "four equal interlocked rings; ours two weights, separate"),
         ("Binance", "crypto exchange", "solid diamonds round a center; ours rings, no center")]),
    'S10': (
        "The Tiger Data treatment: a solid disc with four spun square tiles cut clean through it, floating "
        "well inside the rim. The disc is the institution; the tiles are the light coming through.",
        "Holes are kept small so the solid reads as a pierced disc, not a ring and a cross. Tiger Data slices "
        "run off the edge on parallel lines; these float and turn.",
        "Good: a navy disc with four light spots at 16px.",
        "Masthead. The most seal-like of the set; it would sit on a report cover without apology.",
        [("Tiger Data", "database software", "an animal head and parallel slices running out of the disc; ours four floating tiles"),
         ("Chase", "banking", "one square hole inside four pieces; ours four holes in one solid disc"),
         ("Four-hole button", "object", "four round holes square-on; ours spun tiles on a diamond grid")]),
    'S11': (
        "The inlaid disc: only the outlines of the tiles are cut, so the tiles stay standing as islands, "
        "like tiles set into a round floor. Bronze on cream, the most crafted of the set.",
        "The thin cuts must stay outlines of whole tiles, never lines across the disc, or it becomes a sun "
        "cross; the islands and the solid between them prevent that.",
        "Weak for the inlay (lines close below 40px); the favicon falls back to clean cuts, which read well.",
        "Masthead, at large sizes only. It is a medal, not a favicon.",
        [("Tiger Data", "database software", "parallel slices; ours four closed outlines with the tiles left standing"),
         ("Sun cross", "public symbol", "a ring with a cross; ours has no lines across, only closed tile outlines"),
         ("Kentico", "content software", "a radial figure cut into a square; ours four tiles inlaid in a disc")]),
    'S12': (
        "The sketch cut from the disc, with the lowest tile pushed out through the edge: one piece leaving "
        "the set. The only asymmetry in the carved family, so it never reads as a symbol.",
        "With all four tiles through the rim the solid became a hooked cross, so only one breaks it. Linear and "
        "Tiger Data cut out through the edge with parallel lines; ours with one tile.",
        "Good: the notch in the rim shows at 16px.",
        "Masthead. Green and Fraunces read as a society or a press; the broken rim adds a sentence, not noise.",
        [("Tiger Data", "database software", "parallel slices through the rim; ours one tile of four"),
         ("Linear", "software", "diagonal lines running off a disc; ours rounded tiles, only one leaving"),
         ("Chase", "banking", "symmetric pieces round a hole; ours asymmetric cuts in a disc")]),
    'S13': (
        "The carved square: a soft square block with the sketch cut out of it. A square holding a turned "
        "pinwheel: the made thing and the human hand in one shape.",
        "Square blocks with figures cut out are common in software (Trello, Kentico); the turned 7:5 pinwheel "
        "is not, and avoids the straight cross of the Windows tile.",
        "Good: a black square with four light tiles at 16px.",
        "Masthead in ink; but it is also the most app-icon shaped, which tips it toward software.",
        [("Trello", "project software", "two upright bars cut in a rounded square; ours four turned tiles"),
         ("Kentico", "content software", "a radial burst in a square; ours four tiles in a pinwheel"),
         ("Deutsche Bank", "banking", "one slash in a square outline; ours a solid block with four cuts")]),
    'S14': (
        "Three tiles cut through the disc; the fourth stays solid, in red. The user is the one piece still "
        "in place. In one color the fourth simply stays uncut, so the mark still works.",
        "Microsoft colors each tile; this colors one, and it is the only tile not cut.",
        "Good: the red tile reads at 16px as a spot on the disc.",
        "Masthead. Navy and one red is a serious journal; the meaning is quiet enough to explain once.",
        [("Tiger Data", "database software", "one color, parallel slices; ours three cuts and one standing accent tile"),
         ("Chase", "banking", "four pieces round a hole; ours three holes and one solid tile in a disc"),
         ("Microsoft", "software", "four colors; ours one accent")]),
    'S15': (
        "Four pages fanned from one corner, like a swatch book opened: the tiles as sheets of a publication. "
        "Each sheet is cut from the one above, so it is one shape in one color.",
        "A first draft fanned from the bottom center was a hand of playing cards; the corner pivot reads as a "
        "swatch book or a stack of pages.",
        "Fair: a dark sheet with stepped edges at 16px.",
        "Borderline. Literal for a publication, and fans are a design-tool cliche.",
        [("Buffer", "social media software", "three stacked layers seen in perspective; ours four flat sheets fanned on a corner"),
         ("Swatch book", "object", "many thin strips; ours four broad sheets"),
         ("Paper stack icons", "generic UI", "sheets offset straight; ours fanned on a pivot")]),
    'S16': (
        "Two tiles only: two neighboring tiles of the sketch, one solid, one outlined. The user and the "
        "product, side by side; the outline is the one still being made.",
        "Two-shape marks are common (Mastercard); turned tiles, one open, are not.",
        "Good: two pieces read at 16px; the outlined one closes to a darker block.",
        "Borderline. It reads as a pair, not as an institution.",
        [("Mastercard", "payments", "two overlapping discs; ours two separate turned tiles, one outlined"),
         ("Trello", "project software", "two bars in a frame; ours two tiles, no frame"),
         ("Make", "automation software", "slanted bars in a row; ours two tiles at right angles")]),
    'S17': (
        "Three solid tiles and the fourth an outline: the empty seat, the place kept for the reader.",
        "Within the family, one open tile is the difference from Microsoft-style clusters.",
        "Fair: the outlined tile closes at 16px and the four look the same.",
        "Masthead in large use, weaker small.",
        [("Microsoft", "software", "four solid equal squares; ours three solid 7:5 tiles and one open"),
         ("Binance", "crypto exchange", "solid diamonds round a center; ours no center, one open"),
         ("Dropbox", "file storage", "solid diamonds in pairs; ours three solid, one open")]),
    'S18': (
        "The square-on version of the carved disc: S3's sharp 4:3 blocks cut small through a red disc, beside "
        "an ink word. The press-red seal.",
        "Square-on tiles in a disc are close to the old Windows start orb; the 4:3 jogged seams and the small, "
        "floating cuts keep it a pierced disc, not a window.",
        "Good: a red disc with a small window of light at 16px, but that is exactly the Windows reading.",
        "Borderline. Red and ink are right; the window reading is hard to shake.",
        [("Windows start orb", "software", "the four-color flag in a glass disc; ours one color, 4:3 tiles with jogged seams"),
         ("Chase", "banking", "octagon round a square hole; ours four sharp cuts in a disc"),
         ("Microsoft", "software", "four squares straight; ours 4:3 pinwheel inside a disc")]),
}
