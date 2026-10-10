"""The words on the round 2 board, one entry per mark, in board order (R2-01 to R2-10)."""

INFO = [
    {
        'name': 'Shared stem', 'letters': 'U and D', 'colour': 'blue', 'holder': 'Rounded square',
        'idea': 'A U and a D standing side by side on one shared stem, in a rounded square.',
        'nice': 'The middle stem is both letters at once, and the light fold shows exactly where they share it.',
        'authority': 'Two upright capitals, heavy and level, with no trick to decode: it reads like a publisher\'s monogram.',
        'construction': 'White U and light-blue D, stems 72 at 512, overlapping by one stem width. The shared stem is the '
                        'fold tone, and the D\'s square foot shows below the U\'s curve. Signal-blue rounded square.',
        'closest': ['LinkedIn (two letters set tight in a rounded tile)', 'Udemy (a U letter mark)',
                    'Dailymotion (a single letter in a tile)'],
    },
    {
        'name': 'Turned U', 'letters': 'U becomes D', 'colour': 'blue', 'holder': 'Circle',
        'idea': 'Turn a U on its side and lay its open ends on a stem: it becomes a D.',
        'nice': 'The two light squares are the U\'s ends folding over the stem; once you see the U, it stays.',
        'authority': 'Read quickly, it is a plain heavy D in a circle, steady and symmetrical, like a seal.',
        'construction': 'White stem 80 wide. A light-blue U, stems 80, turned 90 degrees so its ends sit on the stem; '
                        'the two overlaps are the fold squares. Signal-blue circle.',
        'closest': ['DigitalOcean (a round form with small squares at its base)', 'Discovery (a D monogram)'],
    },
    {
        'name': 'Split ring', 'letters': 'u and p', 'colour': 'blue', 'holder': 'Circle',
        'idea': 'One ring cut across the middle: the lower half is a u, the upper half and a tail make a p.',
        'nice': 'The u and the p share a single counter, so the mark is the word "up".',
        'authority': 'It reads first as a sturdy lowercase p in a disc, a shape people already trust on a home screen.',
        'construction': 'White U, stems 74, overlaps a light-blue arch of the same width by 60; the two side bands where '
                        'they overlap are the fold. The p\'s tail, also light blue, folds over the u\'s left side. '
                        'Signal-blue circle.',
        'closest': ['Pinterest (a p in a circle)', 'Product Hunt (a P in a circle)'],
    },
    {
        'name': 'D holds U', 'letters': 'D with U', 'colour': 'blue', 'holder': 'Shaped as the icon (the D is the tile)',
        'idea': 'A solid D with a U cut out of it, so the letter is the icon\'s own shape.',
        'nice': 'The user sits inside the product: the U is made of nothing but the space the D leaves.',
        'authority': 'One closed, solid silhouette with a clean cut-out, the kind of mark that holds up on a book spine.',
        'construction': 'Solid D: stem half in signal blue, bowl half in bright blue, meeting on the bowl\'s centre line. '
                        'U cut out with stems 62. No overlap here: the two tones meet at a seam, and the cut-out crosses it.',
        'closest': ['Dashlane (a solid D shape with a cut)', 'Deutsche Bahn (letters inside a rounded frame)'],
    },
    {
        'name': 'Cut coin', 'letters': 'U', 'colour': 'blue', 'holder': 'Circle', 'mono_keep': ('b',),
        'idea': 'A U cut out of a filled circle; the middle of the circle is the U\'s counter.',
        'nice': 'The container and the letter are one object: take the circle away and there is no U.',
        'authority': 'A coin with a single clean cut: sober, permanent, nothing added.',
        'construction': 'Signal-blue circle. A white U-shaped groove, 58 wide, runs out through the top edge; the counter '
                        'inside the groove is a light-blue tongue. Three regions of one disc, no outline.',
        'closest': ['Uber (the 2016 app icon, one shape with one cut)', 'Ubuntu (a circle broken by cuts)'],
    },
    {
        'name': 'Two hooks', 'letters': 'U', 'colour': 'green', 'holder': 'Stands free',
        'idea': 'A heavy U made of two hooks, one from each side, folded where they meet at the base.',
        'nice': 'Two halves meeting in the middle, user and product, holding one shape together.',
        'authority': 'Massive, symmetrical and upright: the weight of a university letter without the ornament.',
        'construction': 'Built from two tones only. Left hook deep green, right hook mid green, overlapping by 72 at the '
                        'base; the overlap is the light fold. Stems 124 at 512. Alternative colour: deep green.',
        'closest': ['Udemy (a U letter mark)', 'Upwork (a heavy rounded "up" letter mark)'],
    },
    {
        'name': 'Stack', 'letters': 'U over P', 'colour': 'blue', 'holder': 'Stands free',
        'idea': 'A U standing on a P, the P\'s bowl tucked into the U\'s curve: one upright figure.',
        'nice': 'Top to bottom it reads "UP", and it stands like a person: head and shoulders over a body.',
        'authority': 'An upright column of two capitals, like a masthead stacked into a narrow space.',
        'construction': 'U in signal blue, stems 64, overlaps the top of the P\'s bowl (bright blue) by 40; the lens '
                        'where they meet is the light fold. Stands free; tall rather than wide.',
        'closest': ['Upwork (an "up" letter mark)', 'Uniqlo (stacked letters in a square)'],
    },
    {
        'name': 'Lit D', 'letters': 'D', 'colour': 'blue', 'holder': 'Rounded square', 'mono_keep': ('b',),
        'idea': 'A white D reversed out of a rounded square, drawn on the tile\'s own lines, its counter lit.',
        'nice': 'The D\'s corners echo the tile\'s corners, so letter and icon look cut from one piece.',
        'authority': 'The calmest of the ten: a heavy capital in a tile, the way serious apps and publishers sign an icon.',
        'construction': 'White D, stem 104, inset 84 from a signal-blue rounded square; its left corners follow the '
                        'tile\'s radius. The counter is light blue. No overlap.',
        'closest': ['Dailymotion (a letter in a square tile)', 'Deutsche Bahn (letters inside a rounded frame)'],
    },
    {
        'name': 'Ampersand', 'letters': 'U & P', 'colour': 'vermilion', 'holder': 'Circle',
        'idea': 'An ampersand drawn from a P loop on top and a U bowl below, the P\'s stem running on as the tail.',
        'nice': 'The "and" in the name becomes the mark, and it still carries the U and the P.',
        'authority': 'The ampersand is a printer\'s sign; set in a disc it reads like a publisher\'s imprint.',
        'construction': 'Light P loop and leg; white U bowl tilted 38 degrees; the two cross twice, and both crossings '
                        'are the fold. Alternative colour: vermilion circle.',
        'closest': ['&pizza (an ampersand as the whole mark)', 'Faber & Faber (a printer\'s ff monogram)'],
    },
    {
        'name': 'Folded u', 'letters': 'u in the name', 'colour': 'blue', 'holder': 'Stands free (wordmark-forward)',
        'wordmark': True,
        'idea': 'Keep the name as the logo and change one letter: the first u gets a page corner folded down.',
        'nice': 'A dog-eared page is what a reader does to an article worth coming back to.',
        'authority': 'The name stays in plain Inter Display Bold; one corner of one letter moves, so it reads as a '
                     'publication, not a gimmick.',
        'construction': 'Type change proposed: replace the first u of the wordmark with Inter Display Bold\'s u whose '
                        'right stem is cut on a 45-degree line at the top; the cut corner folds in as a light-blue '
                        'triangle. The u is signal blue, the other letters stay in ink. The same u, scaled up, is the icon.',
        'closest': ['Evernote (the folded corner on the elephant\'s ear)', 'Google Docs (the dog-eared page icon)'],
    },
]
