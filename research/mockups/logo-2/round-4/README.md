# Logo exploration 2, round 4: refining the shortlist, and fresh marks

Board: http://localhost/user-and-product/research/mockups/logo-2/round-4/
Hub (all rounds): http://localhost/user-and-product/research/mockups/logo-2/hub.html

## The owner's brief (10 October 2026)

Round 3 shortlist: Cup and ball, Speech mark, Square coin, Shelf (R3-03, R3-04, R3-05 and R3-14 on the board as
the owner saw it; the round 3 board was renumbered afterwards and carries a note mapping the numbers).

1. Cup and ball, turned to the left so it reads three ways: a person raising a hand, a U, and a hint of a D.
   The original for reference, then 30, 45 and 60 degrees, each as the coin itself and cut from a disc; also the
   ball lifted out of the bowl at 45.
2. Speech mark: the tail was too small and at small sizes the mark looked like a cricket ball. Make the tail the
   drawing, test at 32 px and 16 px, keep the lit notch wall.
3. Square coin: two or three small variations (corner radius, channel width, channel depth).
4. Shelf: two or three variations (lean, proportions, disc versus free, blue versus oxblood).
5. Up to three figurative candidates from round 3 that pass the authority and 32 px checks.
6. Added by the owner: eight to ten fresh marks on new ground, at the standard of one clean idea cut from a solid
   form (a reference for the level, never a shape to copy), numbered after the families.

Rule from now on: a board is never renumbered after the owner has seen it. New marks go at the end; dropped marks
stay on the board, marked as dropped.

## Findings

- **Cup and ball: 45 degrees.** At 45 (R4-04) all three readings hold: a U on its side, a head with one arm
  raised, and the straight cut edge as the stem of a D. At 30 the U dominates and the arm is a hint; at 60 the arm
  is strongest but the U is gone and it starts to look like a shell. Lifting the ball (R4-08) makes the person read
  first, at the cost of the D. Cut from a disc, every angle weakens: the cup becomes a ring around a ball.
- **Speech mark: the heavier long tail (R4-12) survives smallest.** It reads as a quote mark at 16 px; the longer,
  finer tail (R4-11) is as clear at 32 px. The sharper notch (R4-13) is the most typographic but its short tail
  fades at 16 px. The wedge (R4-14) reads at any size but as a chat bubble. Tried and not kept: a curved slit
  through the rim (it read as a crack in a disc, not a tail).

## The marks

| No. | Family | Variant | Holder | Color |
|-----|--------|---------|--------|-------|
| R4-01 | Cup and ball | As shortlisted (0 degrees) | Coin | Blue |
| R4-02 | Cup and ball | 30 degrees | Coin | Blue |
| R4-03 | Cup and ball | 30 degrees, in a disc | Circle | Blue |
| R4-04 | Cup and ball | 45 degrees (recommended) | Coin | Blue |
| R4-05 | Cup and ball | 45 degrees, in a disc | Circle | Blue |
| R4-06 | Cup and ball | 60 degrees | Coin | Blue |
| R4-07 | Cup and ball | 60 degrees, in a disc | Circle | Blue |
| R4-08 | Cup and ball | 45 degrees, ball lifted | Coin | Blue |
| R4-09 | Cup and ball | 45 degrees, ball lifted, in a disc | Circle | Blue |
| R4-10 | Speech mark | As shortlisted | Shape | Vermilion |
| R4-11 | Speech mark | Longer tail | Shape | Vermilion |
| R4-12 | Speech mark | Heavier tail (survives smallest) | Shape | Vermilion |
| R4-13 | Speech mark | Sharper notch | Shape | Vermilion |
| R4-14 | Speech mark | Wedge tail | Shape | Vermilion |
| R4-15 | Square coin | As shortlisted (radius 116, channel 56, foot 410) | Coin (rounded square) | Blue |
| R4-16 | Square coin | Softer corners (radius 168) | Coin (rounded square) | Blue |
| R4-17 | Square coin | Wider channel (74) | Coin (rounded square) | Blue |
| R4-18 | Square coin | Shallower channel (foot 356) | Coin (rounded square) | Blue |
| R4-19 | Shelf | As shortlisted (24 degrees, free) | Stands free | Oxblood |
| R4-20 | Shelf | Steeper lean, squatter books (32 degrees, 132 by 300) | Stands free | Oxblood |
| R4-21 | Shelf | In a disc | Circle | Oxblood |
| R4-22 | Shelf | In blue | Stands free | Blue |
| R4-23 | New figurative | At the screen (R3-12) | Circle | Blue |
| R4-24 | New figurative | Doorway (R3-14) | Rounded square | Blue |
| R4-25 | New figurative | Raised hand (R3-18) | Circle | Blue |
| R4-26 | Fresh | Lens | Rounded square | Blue |
| R4-27 | Fresh | Dividers | Circle | Blue |
| R4-28 | Fresh | Desk lamp | Circle | Blue |
| R4-29 | Fresh | Rook | Circle | Plum |
| R4-30 | Fresh | Anvil | Circle | Deep green |
| R4-31 | Fresh | Signpost | Circle | Blue |
| R4-32 | Fresh | Funnel | Circle | Blue |
| R4-33 | Fresh | One block | Stands free | Blue |

Each mark's idea, "oh nice" reason, what it means, authority check, construction and nearest existing logos are
on the board and in `info.py`.

## Decided while drawing

- Fresh marks kept away from the old exploration: plumb lines, keystones, lecterns and true north were all tried
  there, so none of them is here.
- Page turn (a spread with the right page lifting) did not read and was replaced by Dividers before the board.
- Honest kinships: Lens is the search icon; Desk lamp is in Pixar's family; One block is the package icon; Funnel
  is the filter icon; Dividers sit near the square and compasses. Rook, Anvil and Signpost are the cleanest of the
  fresh marks at 32 px.

## Files, rebuild and checks

Same structure as round 3: `svg/r4-NN-*.svg` (masters, dark, monochrome, single color, avatars, LinkedIn square,
lockups), `png/r4-NN-*.png` (favicons at 32 and 16 px in color, 32 px monochrome, transparent 16 px tab icons,
thumbs). `marks.py` (geometry; the round 3 shapes are copied in as the starting point), `geo.py`, `info.py`,
`board.py`, `build.py`, `check.py`, `status.py`. Rebuild with `python build.py` then `python check.py`.

Check results (10 Oct 2026): 462 SVGs, all valid, paths only, largest 5,017 bytes; nothing under 8 units at 512 in
color or monochrome; 264 favicons present; every 32 px PNG looked at. The shape check compares marks across
families (variants inside a family are meant to be close): the most similar pair across families is R4-13 and
R4-23 at 0.70. The board returns 200.
