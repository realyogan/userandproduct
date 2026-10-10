# Eval notes (second version: kinds, bold backgrounds, schemes, lockup; 9 Oct 2026)

Prompts in `evals.json`; outputs in `outputs/eval-N/`. Each run read SKILL.md and its references, then used
the generator. Evals 1 to 3 ran with `--no-history` (in parallel); eval 4 used the history file in order.

| Eval | Result | Verdict |
|---|---|---|
| 1 PRD how-to | howto; candidates 1, 3, 4, 2; style 3 by rotation; hot-pink, duo, accent deep green; lockup bottom-right; checks pass | Pass with a finding: the accent also sat on the pixel window's title-bar button and first text line (decoration) and the checker felt heavy. Fixed: decoration in ink, the checker is now a sparse one-in-four dither. |
| 2 Supplied photo | style 11; hot-pink; photo prepared (cropped, month, dates, logos and the Pinterest button painted out, grid rebuilt thicker); checks pass | Pass with a finding: the recipe said "duo" although the dot screen uses no accent. Fixed: style 11 is always recorded as mono. At 300 px the sheet reads as calendar or calculator; a real photo will read better. |
| 3 Style cannot carry | list; candidates 1, 4, 10, 2; rotation gave 4, a persona has no steps, fell to 10 (violet, duo, lime) and said so; checks pass | Pass: fit, rotation and fallback worked end to end. The avatar silhouette reads, if faintly, as dots. |
| 4 Three neighbours | opinion 7 (midnight, duo yellow), data 9 (night-plum, mono), tool 3 (acid yellow, duo indigo); no shared style or background name | Pass with two findings: 7 and 9 were both near-black and looked alike; the retention silhouette rose instead of falling. Fixed: the pick now prefers a different ground family after the last one (rerun: 7 midnight, 10 mint, 3 acid yellow), and the retention silhouette is a falling chart. |
