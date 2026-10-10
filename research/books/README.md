# Books

The Books shelf research: `candidates-2026-10-10.csv` (181 candidate books, the data), `candidates-2026-10-10.md`
(the same list by section, with sources) and `section-notes-2026-10-10.md`.

## Rebuilding the tree page

`research/explainers/book-shelf-tree-2026-10-10.html` is generated from the CSV. After any change to the CSV, run
`python research/books/build_tree.py` from the repository root (or anywhere). The page layout is in
`build_tree_template.html`; the article-potential lines and the second homes are in the script itself. The script
stops with an error if a book's category is not one of the 16 categories and shelves, or if any book is missing or listed twice. A new tier-A book has no article-potential line until one is added to `POT` in the script.
