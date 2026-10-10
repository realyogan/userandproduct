# Book covers (Books mockup)

The cover images on the Books pages (`sections/books.html`, `books/product-management.html`). Source:
[Open Library](https://openlibrary.org/). No caption on the pages credits the covers; this README is where the
source is recorded.

The image files are not in git: cover art is the publishers' copyright and the repository is public. Only this
README is tracked. At launch the covers switch to the images the affiliate program licenses for this use.

## How they were fetched

One request per image with a pause between requests, on 10 October 2026. For each book in
`research/books/candidates-2026-10-10.csv`, an Open Library search by title and first author; the cover is the one
Open Library shows for the matching work (`cover_i`). For the five books on the product management page the
edition the page names was checked by eye (Inspired 2nd edition 2017, Escaping the Build Trap 2018, Empowered
2020, Working Backwards 2021, Product Management in Practice 2nd edition 2022). For the others the cover is the
work's main cover and may show a different edition than the one the page will name; check before a topic page goes
live. The ISBN listed is an English-language ISBN from the same work.

Each book has two files: `<slug>-cover.jpg` is Open Library's medium size (`-M`, about 180 px wide) and
`<slug>-cover-2x.jpg` its large size (`-L`). The pages show the large file at every screen density (the medium one
goes soft once the 3D tilt or a zoom enlarges it), at 250 css px wide or less; the medium file's width and height
give the ratio. The full record, with sizes and the work key, is `research/books/covers-2026-10-10.csv`. To fetch
one again (the build also makes `<slug>-cover-sm.jpg`, a 240 px wide copy of the large file for the shelf tiles
and the masthead, where covers show at about 100 css px; it is remade on the next build if missing):

    curl -sfL -o <slug>-cover.jpg    "https://covers.openlibrary.org/b/id/<cover id>-M.jpg"
    curl -sfL -o <slug>-cover-2x.jpg "https://covers.openlibrary.org/b/id/<cover id>-L.jpg"

## Low resolution (11)

The large file is under 400 px tall, so these covers look soft on the page until the affiliate images replace
them at launch.

- Designing with the Mind in Mind, Jeff Johnson (300 x 300)
- This Is Service Design Doing, Marc Stickdorn, Markus Edgar Hormess, Adam Lawrence, Jakob Schneider (500 x 397)
- How to Make Sense of Any Mess, Abby Covert (296 x 395)
- Content Strategy for the Web, Kristina Halvorson, Melissa Rach (62 x 80)
- Inclusive Design Patterns, Heydon Pickering (342 x 365)
- Value Proposition Design, Alexander Osterwalder, Yves Pigneur, Gregory Bernarda, Alan Smith (500 x 394)
- Testing Business Ideas, David J. Bland, Alexander Osterwalder (500 x 394)
- Business Model Generation, Alexander Osterwalder, Yves Pigneur (500 x 396)
- The Hard Thing About Hard Things, Ben Horowitz (124 x 187)
- The Four Steps to the Epiphany, Steve Blank (128 x 166)
- Essentialism, Greg McKeown (186 x 281)

## Files (169 books, 338 files)

| Slug (`-cover.jpg`, `-cover-2x.jpg`) | Book | ISBN | Cover id | Large size | Source (medium; large is the same with -L) | Fetched |
|---|---|---|---|---|---|---|
| `just-enough-research` | Just Enough Research, Erika Hall | 9781937557102 | 7387007 | 323 x 500 | https://covers.openlibrary.org/b/id/7387007-M.jpg | 2026-10-10 |
| `interviewing-users` | Interviewing Users, Steve Portigal | 9781959029823 | 8778372 | 333 x 500 | https://covers.openlibrary.org/b/id/8778372-M.jpg | 2026-10-10 |
| `rocket-surgery-made-easy` | Rocket Surgery Made Easy, Steve Krug | 9780321702845 | 7440858 | 390 x 499 | https://covers.openlibrary.org/b/id/7440858-M.jpg | 2026-10-10 |
| `observing-the-user-experience` | Observing the User Experience, Elizabeth Goodman, Mike Kuniavsky, Andrea Moed | 9781558609235 | 7273974 | 405 x 500 | https://covers.openlibrary.org/b/id/7273974-M.jpg | 2026-10-10 |
| `handbook-of-usability-testing` | Handbook of Usability Testing, Jeffrey Rubin, Dana Chisnell | 9781281374547 | 305857 | 405 x 500 | https://covers.openlibrary.org/b/id/305857-M.jpg | 2026-10-10 |
| `surveys-that-work` | Surveys That Work, Caroline Jarrett | 9781933820835 | 13985758 | 333 x 500 | https://covers.openlibrary.org/b/id/13985758-M.jpg | 2026-10-10 |
| `practical-empathy` | Practical Empathy, Indi Young | 9781933820644 | 10439633 | 334 x 500 | https://covers.openlibrary.org/b/id/10439633-M.jpg | 2026-10-10 |
| `measuring-the-user-experience` | Measuring the User Experience, Bill Albert, Tom Tullis | 9780123735584 | 10262965 | 405 x 500 | https://covers.openlibrary.org/b/id/10262965-M.jpg | 2026-10-10 |
| `think-like-a-ux-researcher` | Think Like a UX Researcher, David Travis, Philip Hodgson | 9781138365353 | 10522091 | 333 x 500 | https://covers.openlibrary.org/b/id/10522091-M.jpg | 2026-10-10 |
| `the-user-experience-team-of-one` | The User Experience Team of One, Leah Buley; 2nd ed. with Joe Natoli | 9781959029953 | 13221920 | 334 x 500 | https://covers.openlibrary.org/b/id/13221920-M.jpg | 2026-10-10 |
| `mapping-experiences` | Mapping Experiences, Jim Kalbach | 9781492076636 | 7904375 | 500 x 404 | https://covers.openlibrary.org/b/id/7904375-M.jpg | 2026-10-10 |
| `the-design-of-everyday-things` | The Design of Everyday Things, Don Norman | none listed | 7841556 | 400 x 400 | https://covers.openlibrary.org/b/id/7841556-M.jpg | 2026-10-10 |
| `dont-make-me-think` | Don't Make Me Think, Steve Krug | 9780789723109 | 554640 | 372 x 500 | https://covers.openlibrary.org/b/id/554640-M.jpg | 2026-10-10 |
| `the-elements-of-user-experience` | The Elements of User Experience, Jesse James Garrett | 9780735712027 | 461828 | 389 x 500 | https://covers.openlibrary.org/b/id/461828-M.jpg | 2026-10-10 |
| `about-face` | About Face, Alan Cooper, Robert Reimann, David Cronin, Christopher Noessel | 9781568843223 | 812295 | 378 x 475 | https://covers.openlibrary.org/b/id/812295-M.jpg | 2026-10-10 |
| `lean-ux` | Lean UX, Jeff Gothelf, Josh Seiden | 9781491953600 | 7534763 | 266 x 400 | https://covers.openlibrary.org/b/id/7534763-M.jpg | 2026-10-10 |
| `100-things-every-designer-needs-to-know-about-people` | 100 Things Every Designer Needs to Know About People, Susan Weinschenk | 9780321767530 | 8727716 | 389 x 500 | https://covers.openlibrary.org/b/id/8727716-M.jpg | 2026-10-10 |
| `laws-of-ux` | Laws of UX, Jon Yablonski | 9781492055310 | 13131682 | 333 x 500 | https://covers.openlibrary.org/b/id/13131682-M.jpg | 2026-10-10 |
| `change-by-design` | Change by Design, Tim Brown | 9780061937743 | 6305705 | 333 x 500 | https://covers.openlibrary.org/b/id/6305705-M.jpg | 2026-10-10 |
| `designing-with-the-mind-in-mind` | Designing with the Mind in Mind, Jeff Johnson | 9780123750303 | 6969728 | 300 x 300 (low resolution) | https://covers.openlibrary.org/b/id/6969728-M.jpg | 2026-10-10 |
| `articulating-design-decisions` | Articulating Design Decisions, Tom Greever | 9781492079224 | 8253809 | 333 x 499 | https://covers.openlibrary.org/b/id/8253809-M.jpg | 2026-10-10 |
| `this-is-service-design-doing` | This Is Service Design Doing, Marc Stickdorn, Markus Edgar Hormess, Adam Lawrence, Jakob Schneider | 9781491927182 | 12860075 | 500 x 397 (low resolution) | https://covers.openlibrary.org/b/id/12860075-M.jpg | 2026-10-10 |
| `information-architecture-for-the-web-and-beyond` | Information Architecture: For the Web and Beyond, Louis Rosenfeld, Peter Morville, Jorge Arango | 9781491913550 | 8954696 | 333 x 500 | https://covers.openlibrary.org/b/id/8954696-M.jpg | 2026-10-10 |
| `how-to-make-sense-of-any-mess` | How to Make Sense of Any Mess, Abby Covert | 9781500615994 | 7352417 | 296 x 395 (low resolution) | https://covers.openlibrary.org/b/id/7352417-M.jpg | 2026-10-10 |
| `card-sorting` | Card Sorting, Donna Spencer | 9781933820026 | 8626635 | 333 x 500 | https://covers.openlibrary.org/b/id/8626635-M.jpg | 2026-10-10 |
| `everyday-information-architecture` | Everyday Information Architecture, Lisa Maria Marquis | 9781952616655 | 13124023 | 300 x 425 | https://covers.openlibrary.org/b/id/13124023-M.jpg | 2026-10-10 |
| `strategic-writing-for-ux` | Strategic Writing for UX, Torrey Podmajersky | 9781492049395 | 14860599 | 333 x 500 | https://covers.openlibrary.org/b/id/14860599-M.jpg | 2026-10-10 |
| `content-design` | Content Design, Sarah Winters; 2nd ed. with Rachel Edwards | 9781527209183 | 11532650 | 294 x 500 | https://covers.openlibrary.org/b/id/11532650-M.jpg | 2026-10-10 |
| `writing-is-designing` | Writing Is Designing, Michael J. Metts, Andy Welfle | 9781933820668 | 11757386 | 333 x 500 | https://covers.openlibrary.org/b/id/11757386-M.jpg | 2026-10-10 |
| `content-strategy-for-the-web` | Content Strategy for the Web, Kristina Halvorson, Melissa Rach | 9780321648747 | 6645380 | 62 x 80 (low resolution) | https://covers.openlibrary.org/b/id/6645380-M.jpg | 2026-10-10 |
| `nicely-said` | Nicely Said, Nicole Fenton, Kate Kiefer Lee | 9780321988195 | 7284349 | 388 x 500 | https://covers.openlibrary.org/b/id/7284349-M.jpg | 2026-10-10 |
| `refactoring-ui` | Refactoring UI, Adam Wathan, Steve Schoger | none listed | 10527062 | 354 x 500 | https://covers.openlibrary.org/b/id/10527062-M.jpg | 2026-10-10 |
| `the-non-designers-design-book` | The Non-Designer's Design Book, Robin Williams | 9781566091596 | 806074 | 302 x 475 | https://covers.openlibrary.org/b/id/806074-M.jpg | 2026-10-10 |
| `thinking-with-type` | Thinking with Type, Ellen Lupton | 9781856694247 | 812786 | 412 x 500 | https://covers.openlibrary.org/b/id/812786-M.jpg | 2026-10-10 |
| `designing-interfaces` | Designing Interfaces, Jenifer Tidwell, Charles Brewer, Aynne Valencia | 9781600330148 | 389022 | 410 x 500 | https://covers.openlibrary.org/b/id/389022-M.jpg | 2026-10-10 |
| `universal-principles-of-design` | Universal Principles of Design, William Lidwell, Kritina Holden, Jill Butler | 9781592530076 | 868272 | 404 x 475 | https://covers.openlibrary.org/b/id/868272-M.jpg | 2026-10-10 |
| `form-design-patterns` | Form Design Patterns, Adam Silver | none listed | 14625733 | 326 x 500 | https://covers.openlibrary.org/b/id/14625733-M.jpg | 2026-10-10 |
| `information-dashboard-design` | Information Dashboard Design, Stephen Few | 9781938377006 | 389150 | 425 x 500 | https://covers.openlibrary.org/b/id/389150-M.jpg | 2026-10-10 |
| `practical-ui` | Practical UI, Adham Dannaway | none listed | 14625724 | 363 x 500 | https://covers.openlibrary.org/b/id/14625724-M.jpg | 2026-10-10 |
| `the-visual-display-of-quantitative-information` | The Visual Display of Quantitative Information, Edward Tufte | 9781930824133 | 725045 | 387 x 475 | https://covers.openlibrary.org/b/id/725045-M.jpg | 2026-10-10 |
| `atomic-design` | Atomic Design, Brad Frost | 9780998296609 | 12750057 | 323 x 500 | https://covers.openlibrary.org/b/id/12750057-M.jpg | 2026-10-10 |
| `design-systems` | Design Systems, Alla Kholmatova | none listed | 14619754 | 354 x 480 | https://covers.openlibrary.org/b/id/14619754-M.jpg | 2026-10-10 |
| `building-design-systems` | Building Design Systems, Sarrah Vesselov, Taurie Davis | 9781484245132 | 10152408 | 330 x 500 | https://covers.openlibrary.org/b/id/10152408-M.jpg | 2026-10-10 |
| `design-that-scales` | Design That Scales, Dan Mall | 9781959029212 | 14625676 | 333 x 500 | https://covers.openlibrary.org/b/id/14625676-M.jpg | 2026-10-10 |
| `a-web-for-everyone` | A Web for Everyone, Sarah Horton, Whitney Quesenbery | 9781933820972 | 7284646 | 333 x 500 | https://covers.openlibrary.org/b/id/7284646-M.jpg | 2026-10-10 |
| `accessibility-for-everyone` | Accessibility for Everyone, Laura Kalbag | 9781952616716 | 10527251 | 300 x 464 | https://covers.openlibrary.org/b/id/10527251-M.jpg | 2026-10-10 |
| `inclusive-design-patterns` | Inclusive Design Patterns, Heydon Pickering | none listed | 14619750 | 342 x 365 (low resolution) | https://covers.openlibrary.org/b/id/14619750-M.jpg | 2026-10-10 |
| `inclusive-components` | Inclusive Components, Heydon Pickering | none listed | 14442662 | 344 x 500 | https://covers.openlibrary.org/b/id/14442662-M.jpg | 2026-10-10 |
| `mismatch` | Mismatch, Kat Holmes | 9780262539487 | 8835420 | 341 x 500 | https://covers.openlibrary.org/b/id/8835420-M.jpg | 2026-10-10 |
| `practical-web-inclusion-and-accessibility` | Practical Web Inclusion and Accessibility, Ashley Firth | 9781484254516 | 10178803 | 329 x 500 | https://covers.openlibrary.org/b/id/10178803-M.jpg | 2026-10-10 |
| `inspired` | Inspired, Marty Cagan | 9781119387503 | 13348591 | 332 x 494 | https://covers.openlibrary.org/b/id/13348591-M.jpg | 2026-10-10 |
| `empowered` | Empowered, Marty Cagan, Chris Jones | 9781119691297 | 10847862 | 337 x 500 | https://covers.openlibrary.org/b/id/10847862-M.jpg | 2026-10-10 |
| `transformed` | Transformed, Marty Cagan, with Lea Hickman, Christian Idiodi, Chris Jones, Jon Moore | 9781119697336 | 15102388 | 316 x 466 | https://covers.openlibrary.org/b/id/15102388-M.jpg | 2026-10-10 |
| `escaping-the-build-trap` | Escaping the Build Trap, Melissa Perri | 9781491973790 | 10320665 | 333 x 500 | https://covers.openlibrary.org/b/id/10320665-M.jpg | 2026-10-10 |
| `working-backwards` | Working Backwards, Colin Bryar, Bill Carr | 9781250267597 | 10297403 | 329 x 500 | https://covers.openlibrary.org/b/id/10297403-M.jpg | 2026-10-10 |
| `build` | Build, Tony Fadell | 9781787634114 | 12742378 | 327 x 500 | https://covers.openlibrary.org/b/id/12742378-M.jpg | 2026-10-10 |
| `creative-selection` | Creative Selection, Ken Kocienda | 9781529011845 | 10128109 | 312 x 500 | https://covers.openlibrary.org/b/id/10128109-M.jpg | 2026-10-10 |
| `product-management-in-practice` | Product Management in Practice, Matt LeMay | 9781098119737 | 13161220 | 333 x 500 | https://covers.openlibrary.org/b/id/13161220-M.jpg | 2026-10-10 |
| `cracking-the-pm-interview` | Cracking the PM Interview, Gayle Laakmann McDowell, Jackie Bavaro | 9780984782819 | 7793723 | 264 x 400 | https://covers.openlibrary.org/b/id/7793723-M.jpg | 2026-10-10 |
| `cracking-the-pm-career` | Cracking the PM Career, Jackie Bavaro, Gayle Laakmann McDowell | 9781955706988 | 10669886 | 350 x 500 | https://covers.openlibrary.org/b/id/10669886-M.jpg | 2026-10-10 |
| `product-leadership` | Product Leadership, Richard Banfield, Martin Eriksson, Nate Walkingshaw | 9781491960608 | 13161226 | 333 x 500 | https://covers.openlibrary.org/b/id/13161226-M.jpg | 2026-10-10 |
| `good-strategy-bad-strategy` | Good Strategy Bad Strategy, Richard Rumelt | 9781846684814 | 6954850 | 296 x 450 | https://covers.openlibrary.org/b/id/6954850-M.jpg | 2026-10-10 |
| `playing-to-win` | Playing to Win, A.G. Lafley, Roger L. Martin | 9781491528792 | 14507238 | 315 x 500 | https://covers.openlibrary.org/b/id/14507238-M.jpg | 2026-10-10 |
| `7-powers` | 7 Powers, Hamilton Helmer | 9780998116310 | 10208801 | 333 x 500 | https://covers.openlibrary.org/b/id/10208801-M.jpg | 2026-10-10 |
| `blue-ocean-strategy` | Blue Ocean Strategy, W. Chan Kim, Renée Mauborgne | 9781591396192 | 8219313 | 308 x 500 | https://covers.openlibrary.org/b/id/8219313-M.jpg | 2026-10-10 |
| `product-roadmaps-relaunched` | Product Roadmaps Relaunched, C. Todd Lombardo, Bruce McCarthy, Evan Ryan, Michael Connors | 9781491971727 | 8876578 | 500 x 404 | https://covers.openlibrary.org/b/id/8876578-M.jpg | 2026-10-10 |
| `the-lean-product-playbook` | The Lean Product Playbook, Dan Olsen | 9781118960875 | 14816612 | 335 x 500 | https://covers.openlibrary.org/b/id/14816612-M.jpg | 2026-10-10 |
| `continuous-discovery-habits` | Continuous Discovery Habits, Teresa Torres | 9781736633304 | 11136152 | 333 x 500 | https://covers.openlibrary.org/b/id/11136152-M.jpg | 2026-10-10 |
| `the-mom-test` | The Mom Test, Rob Fitzpatrick | 9781492180746 | 10660557 | 324 x 500 | https://covers.openlibrary.org/b/id/10660557-M.jpg | 2026-10-10 |
| `sprint` | Sprint, Jake Knapp, John Zeratsky, Braden Kowitz | 9781501140808 | 7431269 | 331 x 499 | https://covers.openlibrary.org/b/id/7431269-M.jpg | 2026-10-10 |
| `user-story-mapping` | User Story Mapping, Jeff Patton | 9781491904909 | 8206841 | 333 x 499 | https://covers.openlibrary.org/b/id/8206841-M.jpg | 2026-10-10 |
| `running-lean` | Running Lean, Ash Maurya | 9781449331917 | 8122897 | 333 x 500 | https://covers.openlibrary.org/b/id/8122897-M.jpg | 2026-10-10 |
| `competing-against-luck` | Competing Against Luck, Clayton M. Christensen, Taddy Hall, Karen Dillon, David S. Duncan | 9780062435613 | 8138391 | 330 x 499 | https://covers.openlibrary.org/b/id/8138391-M.jpg | 2026-10-10 |
| `the-jobs-to-be-done-playbook` | The Jobs To Be Done Playbook, Jim Kalbach | 9781933820682 | 10085437 | 332 x 500 | https://covers.openlibrary.org/b/id/10085437-M.jpg | 2026-10-10 |
| `jobs-to-be-done-theory-to-practice` | Jobs to Be Done: Theory to Practice, Anthony W. Ulwick | 9780990576747 | 10454444 | 316 x 500 | https://covers.openlibrary.org/b/id/10454444-M.jpg | 2026-10-10 |
| `value-proposition-design` | Value Proposition Design, Alexander Osterwalder, Yves Pigneur, Gregory Bernarda, Alan Smith | 9781322877136 | 10196709 | 500 x 394 (low resolution) | https://covers.openlibrary.org/b/id/10196709-M.jpg | 2026-10-10 |
| `testing-business-ideas` | Testing Business Ideas, David J. Bland, Alexander Osterwalder | 9781119722380 | 9388387 | 500 x 394 (low resolution) | https://covers.openlibrary.org/b/id/9388387-M.jpg | 2026-10-10 |
| `user-stories-applied` | User Stories Applied, Mike Cohn | 9780321205681 | 193014 | 378 x 500 | https://covers.openlibrary.org/b/id/193014-M.jpg | 2026-10-10 |
| `evidence-guided` | Evidence-Guided, Itamar Gilad | 9781601560995 | 1875713 | 323 x 475 | https://covers.openlibrary.org/b/id/1875713-M.jpg | 2026-10-10 |
| `the-goal` | The Goal, Eliyahu M. Goldratt, Jeff Cox | 9781622313945 | 7262320 | 341 x 500 | https://covers.openlibrary.org/b/id/7262320-M.jpg | 2026-10-10 |
| `the-mythical-man-month` | The Mythical Man-Month, Frederick P. Brooks Jr. | 9780201835953 | 6915361 | 340 x 500 | https://covers.openlibrary.org/b/id/6915361-M.jpg | 2026-10-10 |
| `scrum-the-art-of-doing-twice-the-work-in-half-the-time` | Scrum: The Art of Doing Twice the Work in Half the Time, Jeff Sutherland, J.J. Sutherland | 9781847941107 | 8107216 | 329 x 500 | https://covers.openlibrary.org/b/id/8107216-M.jpg | 2026-10-10 |
| `shape-up` | Shape Up, Ryan Singer | none listed | 12600273 | 309 x 475 | https://covers.openlibrary.org/b/id/12600273-M.jpg | 2026-10-10 |
| `the-phoenix-project` | The Phoenix Project, Gene Kim, Kevin Behr, George Spafford | 9781950508969 | 9151976 | 375 x 500 | https://covers.openlibrary.org/b/id/9151976-M.jpg | 2026-10-10 |
| `accelerate` | Accelerate, Nicole Forsgren, Jez Humble, Gene Kim | 9781942788621 | 8509069 | 331 x 500 | https://covers.openlibrary.org/b/id/8509069-M.jpg | 2026-10-10 |
| `the-principles-of-product-development-flow` | The Principles of Product Development Flow, Donald G. Reinertsen | 9781935401001 | 7763174 | 261 x 400 | https://covers.openlibrary.org/b/id/7763174-M.jpg | 2026-10-10 |
| `kanban` | Kanban, David J. Anderson | 9780984521401 | 7273224 | 400 x 500 | https://covers.openlibrary.org/b/id/7273224-M.jpg | 2026-10-10 |
| `a-guide-to-the-project-management-body-of-knowledge-pmbok-guide` | A Guide to the Project Management Body of Knowledge (PMBOK Guide), Project Management Institute | 9781935589679 | 926642 | 368 x 475 | https://covers.openlibrary.org/b/id/926642-M.jpg | 2026-10-10 |
| `lean-analytics` | Lean Analytics, Alistair Croll, Benjamin Yoskovitz | 9781449335724 | 7863278 | 266 x 400 | https://covers.openlibrary.org/b/id/7863278-M.jpg | 2026-10-10 |
| `measure-what-matters` | Measure What Matters, John Doerr | 9780525536222 | 9254540 | 331 x 500 | https://covers.openlibrary.org/b/id/9254540-M.jpg | 2026-10-10 |
| `radical-focus` | Radical Focus, Christina Wodtke | 9780996006088 | 10864735 | 313 x 500 | https://covers.openlibrary.org/b/id/10864735-M.jpg | 2026-10-10 |
| `experimentation-works` | Experimentation Works, Stefan H. Thomke | 9781633697102 | 13837260 | 266 x 400 | https://covers.openlibrary.org/b/id/13837260-M.jpg | 2026-10-10 |
| `how-to-measure-anything` | How to Measure Anything, Douglas W. Hubbard | 9781306473477 | 1239590 | 329 x 500 | https://covers.openlibrary.org/b/id/1239590-M.jpg | 2026-10-10 |
| `storytelling-with-data` | Storytelling with Data, Cole Nussbaumer Knaflic | 9781978614277 | 7932707 | 398 x 500 | https://covers.openlibrary.org/b/id/7932707-M.jpg | 2026-10-10 |
| `the-ultimate-question-2-0` | The Ultimate Question 2.0, Fred Reichheld, Rob Markey | 9781422173350 | 7973519 | 306 x 500 | https://covers.openlibrary.org/b/id/7973519-M.jpg | 2026-10-10 |
| `hacking-growth` | Hacking Growth, Sean Ellis, Morgan Brown | 9781524760007 | 14377164 | 303 x 500 | https://covers.openlibrary.org/b/id/14377164-M.jpg | 2026-10-10 |
| `traction` | Traction, Gabriel Weinberg, Justin Mares | 9781591848363 | 9364675 | 331 x 500 | https://covers.openlibrary.org/b/id/9364675-M.jpg | 2026-10-10 |
| `monetizing-innovation` | Monetizing Innovation, Madhavan Ramanujam, Georg Tacke | 9781119240884 | 13744862 | 331 x 500 | https://covers.openlibrary.org/b/id/13744862-M.jpg | 2026-10-10 |
| `confessions-of-the-pricing-man` | Confessions of the Pricing Man, Hermann Simon | none listed | 10073295 | 330 x 500 | https://covers.openlibrary.org/b/id/10073295-M.jpg | 2026-10-10 |
| `the-strategy-and-tactics-of-pricing` | The Strategy and Tactics of Pricing, Thomas T. Nagle, Georg Müller, Evert Gruyaert (earlier eds. with Reed K. Holden) | 9781315266220 | 91486 | 312 x 475 | https://covers.openlibrary.org/b/id/91486-M.jpg | 2026-10-10 |
| `the-cold-start-problem` | The Cold Start Problem, Andrew Chen | 9781847942791 | 10607120 | 350 x 500 | https://covers.openlibrary.org/b/id/10607120-M.jpg | 2026-10-10 |
| `product-led-growth` | Product-Led Growth, Wes Bush | 9781798434529 | 12445239 | 316 x 500 | https://covers.openlibrary.org/b/id/12445239-M.jpg | 2026-10-10 |
| `business-model-generation` | Business Model Generation, Alexander Osterwalder, Yves Pigneur | 9780470876411 | 6675500 | 500 x 396 (low resolution) | https://covers.openlibrary.org/b/id/6675500-M.jpg | 2026-10-10 |
| `platform-revolution` | Platform Revolution, Geoffrey G. Parker, Marshall W. Van Alstyne, Sangeet Paul Choudary | 9781511366601 | 11390852 | 312 x 500 | https://covers.openlibrary.org/b/id/11390852-M.jpg | 2026-10-10 |
| `obviously-awesome` | Obviously Awesome, April Dunford | 9781999023003 | 10194369 | 324 x 500 | https://covers.openlibrary.org/b/id/10194369-M.jpg | 2026-10-10 |
| `sales-pitch` | Sales Pitch, April Dunford | 9781685834890 | 14784817 | 267 x 400 | https://covers.openlibrary.org/b/id/14784817-M.jpg | 2026-10-10 |
| `positioning-the-battle-for-your-mind` | Positioning: The Battle for Your Mind, Al Ries, Jack Trout | 9781932378252 | 55745 | 314 x 475 | https://covers.openlibrary.org/b/id/55745-M.jpg | 2026-10-10 |
| `crossing-the-chasm` | Crossing the Chasm, Geoffrey A. Moore | 9781841120638 | 684159 | 313 x 475 | https://covers.openlibrary.org/b/id/684159-M.jpg | 2026-10-10 |
| `loved` | Loved, Martina Lauchengco | 9781119704393 | 13688700 | 338 x 500 | https://covers.openlibrary.org/b/id/13688700-M.jpg | 2026-10-10 |
| `made-to-stick` | Made to Stick, Chip Heath, Dan Heath | 9781905211579 | 7004880 | 328 x 500 | https://covers.openlibrary.org/b/id/7004880-M.jpg | 2026-10-10 |
| `building-a-storybrand` | Building a StoryBrand, Donald Miller | 9781536693171 | 8458703 | 335 x 500 | https://covers.openlibrary.org/b/id/8458703-M.jpg | 2026-10-10 |
| `this-is-marketing` | This Is Marketing, Seth Godin | 9780525540830 | 14624926 | 354 x 500 | https://covers.openlibrary.org/b/id/14624926-M.jpg | 2026-10-10 |
| `purple-cow` | Purple Cow, Seth Godin | 9781591845584 | 866008 | 336 x 475 | https://covers.openlibrary.org/b/id/866008-M.jpg | 2026-10-10 |
| `contagious` | Contagious, Jonah Berger | 9781476776682 | 9039370 | 326 x 500 | https://covers.openlibrary.org/b/id/9039370-M.jpg | 2026-10-10 |
| `badass-making-users-awesome` | Badass: Making Users Awesome, Kathy Sierra | 9781491919019 | 8276337 | 333 x 500 | https://covers.openlibrary.org/b/id/8276337-M.jpg | 2026-10-10 |
| `how-brands-grow` | How Brands Grow, Byron Sharp | 9780195596267 | 8947122 | 330 x 500 | https://covers.openlibrary.org/b/id/8947122-M.jpg | 2026-10-10 |
| `demand-side-sales-101` | Demand-Side Sales 101, Bob Moesta, Greg Engle | 9781544509983 | 10455373 | 340 x 500 | https://covers.openlibrary.org/b/id/10455373-M.jpg | 2026-10-10 |
| `high-output-management` | High Output Management, Andrew S. Grove | 9780679772040 | 421244 | 301 x 475 | https://covers.openlibrary.org/b/id/421244-M.jpg | 2026-10-10 |
| `the-making-of-a-manager` | The Making of a Manager, Julie Zhuo | 9780753562451 | 8805106 | 331 x 500 | https://covers.openlibrary.org/b/id/8805106-M.jpg | 2026-10-10 |
| `radical-candor` | Radical Candor, Kim Scott | 9781529038347 | 8088432 | 329 x 500 | https://covers.openlibrary.org/b/id/8088432-M.jpg | 2026-10-10 |
| `the-five-dysfunctions-of-a-team` | The Five Dysfunctions of a Team, Patrick Lencioni | 9780787960759 | 14620714 | 400 x 500 | https://covers.openlibrary.org/b/id/14620714-M.jpg | 2026-10-10 |
| `turn-the-ship-around` | Turn the Ship Around!, L. David Marquet | 9781608323746 | 8142531 | 331 x 499 | https://covers.openlibrary.org/b/id/8142531-M.jpg | 2026-10-10 |
| `multipliers` | Multipliers, Liz Wiseman | 9780062663078 | 9265081 | 330 x 500 | https://covers.openlibrary.org/b/id/9265081-M.jpg | 2026-10-10 |
| `the-managers-path` | The Manager's Path, Camille Fournier | 9781491973899 | 8667291 | 317 x 475 | https://covers.openlibrary.org/b/id/8667291-M.jpg | 2026-10-10 |
| `crucial-conversations` | Crucial Conversations, Joseph Grenny, Kerry Patterson, Ron McMillan, Al Switzler, Emily Gregory | 9781491515624 | 1711809 | 367 x 475 | https://covers.openlibrary.org/b/id/1711809-M.jpg | 2026-10-10 |
| `difficult-conversations` | Difficult Conversations, Douglas Stone, Bruce Patton, Sheila Heen | 9780786511037 | 2555094 | 313 x 475 | https://covers.openlibrary.org/b/id/2555094-M.jpg | 2026-10-10 |
| `start-with-why` | Start with Why, Simon Sinek | 9781984842305 | 6395237 | 375 x 500 | https://covers.openlibrary.org/b/id/6395237-M.jpg | 2026-10-10 |
| `team-topologies` | Team Topologies, Matthew Skelton, Manuel Pais | 9781950508211 | 10354937 | 334 x 500 | https://covers.openlibrary.org/b/id/10354937-M.jpg | 2026-10-10 |
| `influence-without-authority` | Influence Without Authority, Allan R. Cohen, David L. Bradford | 9781282370838 | 305013 | 332 x 500 | https://covers.openlibrary.org/b/id/305013-M.jpg | 2026-10-10 |
| `leading-change` | Leading Change, John P. Kotter | 9781422133415 | 668100 | 329 x 500 | https://covers.openlibrary.org/b/id/668100-M.jpg | 2026-10-10 |
| `switch` | Switch, Chip Heath, Dan Heath | 9781847940322 | 6968365 | 337 x 500 | https://covers.openlibrary.org/b/id/6968365-M.jpg | 2026-10-10 |
| `the-coaching-habit` | The Coaching Habit, Michael Bungay Stanier | 9780978440749 | 12515817 | 341 x 500 | https://covers.openlibrary.org/b/id/12515817-M.jpg | 2026-10-10 |
| `creativity-inc` | Creativity, Inc., Ed Catmull, Amy Wallace | 9781448126286 | 13124793 | 329 x 500 | https://covers.openlibrary.org/b/id/13124793-M.jpg | 2026-10-10 |
| `dare-to-lead` | Dare to Lead, Brené Brown | 9781984854032 | 10304768 | 331 x 500 | https://covers.openlibrary.org/b/id/10304768-M.jpg | 2026-10-10 |
| `thinking-fast-and-slow` | Thinking, Fast and Slow, Daniel Kahneman | 9781846146060 | 13290711 | 386 x 500 | https://covers.openlibrary.org/b/id/13290711-M.jpg | 2026-10-10 |
| `influence` | Influence, Robert B. Cialdini | 9781886746763 | 431011 | 312 x 475 | https://covers.openlibrary.org/b/id/431011-M.jpg | 2026-10-10 |
| `nudge` | Nudge, Richard H. Thaler, Cass R. Sunstein | 9781282352421 | 6402116 | 375 x 500 | https://covers.openlibrary.org/b/id/6402116-M.jpg | 2026-10-10 |
| `hooked` | Hooked, Nir Eyal | 9781591847786 | 12511799 | 320 x 500 | https://covers.openlibrary.org/b/id/12511799-M.jpg | 2026-10-10 |
| `predictably-irrational` | Predictably Irrational, Dan Ariely | 9780062018205 | 2314080 | 329 x 500 | https://covers.openlibrary.org/b/id/2314080-M.jpg | 2026-10-10 |
| `thinking-in-bets` | Thinking in Bets, Annie Duke | 9780735216372 | 8792782 | 333 x 500 | https://covers.openlibrary.org/b/id/8792782-M.jpg | 2026-10-10 |
| `designing-for-behavior-change` | Designing for Behavior Change, Stephen Wendel | 9781492056034 | 13302900 | 381 x 500 | https://covers.openlibrary.org/b/id/13302900-M.jpg | 2026-10-10 |
| `alchemy` | Alchemy, Rory Sutherland | 9781982608088 | 10184444 | 331 x 500 | https://covers.openlibrary.org/b/id/10184444-M.jpg | 2026-10-10 |
| `the-power-of-habit` | The Power of Habit, Charles Duhigg | 9781847946249 | 9078085 | 424 x 500 | https://covers.openlibrary.org/b/id/9078085-M.jpg | 2026-10-10 |
| `drive` | Drive, Daniel H. Pink | 9781847678881 | 6404786 | 375 x 500 | https://covers.openlibrary.org/b/id/6404786-M.jpg | 2026-10-10 |
| `the-paradox-of-choice` | The Paradox of Choice, Barry Schwartz | 9781491514238 | 20382 | 326 x 500 | https://covers.openlibrary.org/b/id/20382-M.jpg | 2026-10-10 |
| `the-lean-startup` | The Lean Startup, Eric Ries | 9781524762407 | 7104760 | 344 x 500 | https://covers.openlibrary.org/b/id/7104760-M.jpg | 2026-10-10 |
| `the-innovators-dilemma` | The Innovator's Dilemma, Clayton M. Christensen | 9781681686905 | 9274687 | 329 x 500 | https://covers.openlibrary.org/b/id/9274687-M.jpg | 2026-10-10 |
| `zero-to-one` | Zero to One, Peter Thiel, Blake Masters | 9780804165259 | 9002334 | 432 x 500 | https://covers.openlibrary.org/b/id/9002334-M.jpg | 2026-10-10 |
| `the-hard-thing-about-hard-things` | The Hard Thing About Hard Things, Ben Horowitz | 9781483002897 | 7279515 | 124 x 187 (low resolution) | https://covers.openlibrary.org/b/id/7279515-M.jpg | 2026-10-10 |
| `good-to-great` | Good to Great, Jim Collins | 9780712676090 | 7431270 | 329 x 499 | https://covers.openlibrary.org/b/id/7431270-M.jpg | 2026-10-10 |
| `rework` | Rework, Jason Fried, David Heinemeier Hansson | 9781785043024 | 6679955 | 265 x 400 | https://covers.openlibrary.org/b/id/6679955-M.jpg | 2026-10-10 |
| `the-e-myth-revisited` | The E-Myth Revisited, Michael E. Gerber | 9780887307287 | 684209 | 328 x 500 | https://covers.openlibrary.org/b/id/684209-M.jpg | 2026-10-10 |
| `shoe-dog` | Shoe Dog, Phil Knight | 9781534415201 | 8858487 | 331 x 500 | https://covers.openlibrary.org/b/id/8858487-M.jpg | 2026-10-10 |
| `the-four-steps-to-the-epiphany` | The Four Steps to the Epiphany, Steve Blank | 9781411601727 | 4985314 | 128 x 166 (low resolution) | https://covers.openlibrary.org/b/id/4985314-M.jpg | 2026-10-10 |
| `venture-deals` | Venture Deals, Brad Feld, Jason Mendelson | 9781283917506 | 8732100 | 336 x 500 | https://covers.openlibrary.org/b/id/8732100-M.jpg | 2026-10-10 |
| `the-personal-mba` | The Personal MBA, Josh Kaufman | 9781591845577 | 6713257 | 327 x 500 | https://covers.openlibrary.org/b/id/6713257-M.jpg | 2026-10-10 |
| `deep-work` | Deep Work, Cal Newport | 9781478936596 | 7988607 | 331 x 500 | https://covers.openlibrary.org/b/id/7988607-M.jpg | 2026-10-10 |
| `atomic-habits` | Atomic Habits, James Clear | 9781847941848 | 12539702 | 369 x 500 | https://covers.openlibrary.org/b/id/12539702-M.jpg | 2026-10-10 |
| `getting-things-done` | Getting Things Done, David Allen | 9781508215530 | 109288 | 320 x 475 | https://covers.openlibrary.org/b/id/109288-M.jpg | 2026-10-10 |
| `the-7-habits-of-highly-effective-people` | The 7 Habits of Highly Effective People, Stephen R. Covey | 9781982143817 | 10079937 | 329 x 500 | https://covers.openlibrary.org/b/id/10079937-M.jpg | 2026-10-10 |
| `essentialism` | Essentialism, Greg McKeown | 9780804165297 | 7285986 | 186 x 281 (low resolution) | https://covers.openlibrary.org/b/id/7285986-M.jpg | 2026-10-10 |
| `so-good-they-cant-ignore-you` | So Good They Can't Ignore You, Cal Newport | 9781478910077 | 9215292 | 284 x 430 | https://covers.openlibrary.org/b/id/9215292-M.jpg | 2026-10-10 |
| `building-a-second-brain` | Building a Second Brain, Tiago Forte | 9781982167400 | 12372866 | 331 x 500 | https://covers.openlibrary.org/b/id/12372866-M.jpg | 2026-10-10 |
| `four-thousand-weeks` | Four Thousand Weeks, Oliver Burkeman | 9781847924025 | 11990973 | 325 x 500 | https://covers.openlibrary.org/b/id/11990973-M.jpg | 2026-10-10 |
| `on-writing-well` | On Writing Well, William Zinsser | 9781559943499 | 20450 | 315 x 475 | https://covers.openlibrary.org/b/id/20450-M.jpg | 2026-10-10 |
| `the-pyramid-principle` | The Pyramid Principle, Barbara Minto | 9781405822145 | 2346771 | 314 x 475 | https://covers.openlibrary.org/b/id/2346771-M.jpg | 2026-10-10 |
| `mindset` | Mindset, Carol S. Dweck | 9781780333939 | 746414 | 329 x 500 | https://covers.openlibrary.org/b/id/746414-M.jpg | 2026-10-10 |
| `how-to-win-friends-and-influence-people` | How to Win Friends and Influence People, Dale Carnegie | 9781982171476 | 13314878 | 328 x 500 | https://covers.openlibrary.org/b/id/13314878-M.jpg | 2026-10-10 |
| `resonate` | Resonate, Nancy Duarte | 9781282914049 | 8715221 | 500 x 500 | https://covers.openlibrary.org/b/id/8715221-M.jpg | 2026-10-10 |

## No cover found (12)

These keep the cover card drawn in code.

- Microcopy: The Complete Guide, Kinneret Yifrah
- Interaction of Color, Josef Albers
- Expressive Design Systems, Yesenia Perez-Cruz
- Laying the Foundations, Andrew Couldwell
- Strong Product People, Petra Wille
- Product Operations, Melissa Perri, Denise Tilles
- Outcomes Over Output, Josh Seiden
- When Coffee and Kale Compete, Alan Klement
- Trustworthy Online Controlled Experiments, Ron Kohavi, Diane Tang, Ya Xu
- Org Design for Design Orgs, Peter Merholz, Kristin Skinner
- Deceptive Patterns, Harry Brignull
- The Effective Executive, Peter F. Drucker
