# Printables tints: source for explainer backgrounds

Read on 9 Oct 2026 from the Printables site (https://rockpaperprint.com/), code in `c:\xampp\htdocs\Printables`
(read only). Our explainer illustrations use this inventory exactly.

## The eight tints

`wp-content/themes/printables/assets/css/main.css`, lines 72 to 79 (custom properties on `:root`):

| Token | Hex |
|---|---|
| `--tint-blue` | #dbe8fb |
| `--tint-green` | #dcefd8 |
| `--tint-pink` | #fbe0e6 |
| `--tint-purple` | #e8e0f7 |
| `--tint-yellow` | #fff3c4 |
| `--tint-teal` | #d7f0ee |
| `--tint-peach` | #fde3d0 |
| `--tint-slate` | #e0e6ee |

The classes that apply them: `main.css` lines 170 to 177 (`.tint-blue { --tint: var(--tint-blue); background-color: ... }` and so on).

## Ink and neighbours

`main.css` lines 62 to 67: `--card: #fdfcf8` (62), `--ink: #1d1b16`, `--muted: #5f5b52`, `--rule: #cfc9ba`,
`--border: 1.5px solid var(--ink)` (line 87). We use the ink for labels, lines and dots, the muted colour for notes,
and the card colour for plain boxes with a 1.5px ink border.

## The dot grid

- `main.css` line 1015 (`.dl-stage`): `background-image: radial-gradient(rgba(29, 27, 22, .12) 1px, transparent 1.4px); background-size: 14px 14px;`
- `wp-content/themes/printables/assets/kit/kit.css` line 15 (`.kit-pad`, on `--tint-teal`):
  `background-image: radial-gradient(rgba(29, 27, 22, .13) 1px, transparent 1.5px); background-size: 12px 12px;`

So: ink-coloured dots (rgb 29, 27, 22 is #1d1b16) at 12 to 13% opacity, about 1px across, on a 12 to 14px tile.
In our 1200-unit canvas shown at about 720px that is a 22-unit tile and a 1.9-unit dot at 13%.

## How a tint is assigned

`wp-content/themes/printables/inc/template-tags.php`:

- `printables_tints()` (line 16) returns the six that rotate, in order:
  `tint-teal, tint-yellow, tint-pink, tint-blue, tint-green, tint-purple`.
- `printables_tint_class( $index )` (line 26) returns `printables_tints()[ $index % 6 ]`: the n-th item gets the n-th
  tint, cycling.
- `printables_term_tints()` (line 37) adds the two reserved for categories: `tint-peach, tint-slate`.
- `printables_tint_class_for_post( $post_id )` (line 49) and `printables_tint_class_for_term( $term )` (line 64) use a
  stored tint when one is set, otherwise fall back to the index rotation by ID, so an item keeps its colour everywhere.

We mirror this: an article's tint is `CYCLE[index % 6]` by publish order (or a stable hash of the slug when there is
no index), peach and slate are reserved for overrides, and a writer may override with a reason.
