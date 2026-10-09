# Tiger Data: design reference for our single-article layout

Captured 2026-10-09 from two pages only:
- Home: https://www.tigerdata.com/
- Article (the model): https://www.tigerdata.com/blog/meshtastic-metrics-exporter-case-study-tiger-data

Sources used, and how each value below is marked:
- **[computed]**: read from the live page with `getComputedStyle` in headless Edge at 1280px (and 375px where stated).
- **[css]**: read from the site's stylesheets under `/_next/static/css/` (Tailwind utility classes such as `.text-black-500{color:rgb(161 161 170)}`).
- **[class]**: read from the element's Tailwind class list in the page source (for example `lg:text-[60px]`).
- **[shot]**: observed in the screenshots in this folder only; not measured.

robots.txt allows these pages (it only disallows `/blog/tag/` and `/blog/author/`).

## Files in this folder

| File | What |
|---|---|
| home-1280.png | Home, full page, 1280px wide |
| home-375.png | Home, first screen, 375 x 812 |
| article-1280.png | Article, full page, 1280px wide |
| article-375.png | Article, first screen, 375 x 812 |
| logo.svg | Header logo, downloaded from `https://assets.tigerdata.com/timescale-web/brand/tiger-data/flat-logos/logo-horizontal-black.svg` (the `<img>` inside the header's home link, rendered at 160 x 35) |

No dark variants: the site has no dark mode. With `prefers-color-scheme: dark` the home page rendered pixel-identical and every computed colour was unchanged [computed]; the stylesheets contain no site dark theme (only the Tailwind Typography `--tw-prose-invert-*` defaults, unused). The 375px shots show the site's cookie banner over the lower part of the screen.

## Logo

Mark plus wordmark, horizontal, single colour (black on white; the file is `fill="black"`), viewBox 1314 x 290.
- **Mark** (left, 290 x 290): a solid black circle containing a tiger's head in profile, cut out in negative space, facing right; the lower-left of the circle is sliced by diagonal parallel cuts that read as tiger stripes (and also as data lines). Built as one circular mask plus three paths.
- **Wordmark** (right): "Tiger Data", title case (capital T and capital D), two words, a geometric grotesque sans with a single-storey "g" and tight spacing, in a bold weight. Outlined paths, not live text. Set close to the cap height of the mark, vertically centred on it.
- The footer uses the mark alone (about 52px) and a huge ghosted "Tiger Data" wordmark in pale yellow across the bottom [shot].

## Typefaces

Loaded as self-hosted `@font-face` woff2 files (Next.js font optimisation), no Google Fonts link [computed, from `document.styleSheets`]:

| Family | Role | Weights | Notes |
|---|---|---|---|
| **GeistSans** (Geist) | Everything: headings, body, buttons, nav | variable 100-900 | Stack: `GeistSans, "GeistSans Fallback"`; the fallback is `local("Arial")` with metric overrides |
| **GeistMono** (Geist Mono) | Small uppercase labels: "TABLE OF CONTENTS", "SHARE", "6 MIN", "// RELATED POSTS", tag chips, eyebrow badges, stat labels | variable 100-900 | Stack: `GeistMono, ui-monospace, SFMono-Regular, "Roboto Mono", Menlo, ...` |
| GeistPixel Square / Grid / Circle / Triangle / Line | Decorative pixel display faces (home page graphics, the yellow quote marks) | 500 | Loaded on both pages |
| Cygnito Mono | Loaded from `/fonts/Cygnito-Mono.otf`; not seen in use on these two pages | 400 | |
| KaTeX_* | Maths rendering in posts | | Not used in this article |

Geist and Geist Mono are free (SIL Open Font License) and also on Google Fonts, so they are usable for us.

The `<body>` itself falls back to the system UI stack; every text element sets `font-Geist` explicitly [class]. Pull quotes and figure captions do not set it and so render in the system UI font (Segoe UI on Windows) [computed]; this looks like an oversight, not a choice.

## Type scale (article page)

All Geist Sans unless noted. Desktop is at 1280px, mobile at 375px [computed]; class names [class].

| Element | Desktop size / line height | Weight | Letter spacing | Mobile | Colour |
|---|---|---|---|---|---|
| H1 (headline) | 60px / 72px (1.2) | 600 | -0.03em (-1.8px) | 28px / 1.2 (`text-[28px] lg:text-[60px]`) | #0A0A0C |
| H2 (section) | 32px / 38.4px (1.2) | 600 | -0.03em (-0.96px) | 26px / 36.4px (1.4) | #0A0A0C |
| H3 (subsection) | 26px / 36.4px (1.4) | 600 | -0.03em (-0.78px) | 24px / 1.4, weight 400 | #0A0A0C |
| Body paragraph | 16px / 27.2px (1.7) | 400 | normal | same | #0A0A0C |
| Intro / deck paragraphs | 16px / 27.2px, italic (via `<em>`) [shot] | 400 | normal | same | #0A0A0C |
| Pull quote | 20px / 28px, italic | 400 | normal | | #0A0A0C |
| Figure caption | 14px / 20px, italic (`prose-figcaption:italic text-sm`) | 400 | normal | | #A1A1AA |
| Byline name, date | 16px / 24px | 400 | normal | | name #0A0A0C, date #27272A |
| Read time "6 MIN", TOC label | Geist Mono 15px / 21px, uppercase | 500 | 0.02em (0.3px) | 14px | #0A0A0C |
| "SHARE" label | Geist Mono 14px / 21px, uppercase | 400 | normal | | #0A0A0C |
| TOC items | 16px / 22px (`leading-snug`), numbered "01", "02" | 400; active 500 | normal | | inactive #A1A1AA, active #0A0A0C |
| Related-post title (H3) | 22px / 26.4px (1.2) | 600 | -0.01em | 18px | #0A0A0C |
| Related-post excerpt | 16px / 24px, clamped to 3 lines | 400 | normal | | #27272A |
| Newsletter heading | 80px / 88px (1.1) | 700 | -0.03em (-2.4px) | 44px / 52.8px | #0A0A0C |

Home page for comparison [computed]: H1 80px / 88px, 700, -0.03em (44px on mobile); section H2 52px / 57.2px, 600, -0.03em (28-32px on mobile); body 16px / 24px.

Pattern: one family, strong negative tracking (-0.03em) on every heading, semibold for article headings and bold only for the giant marketing headings; body stays at 16px but gets a generous 1.7 line height; Geist Mono uppercase is the "metadata voice".

## Colour tokens

The site is Tailwind with a custom palette; there are no brand CSS custom properties on `:root` (only cookie-banner `--osano-*` variables and the Next.js starter `--foreground-rgb`). Hex values below are from the utility classes in `81b93873a3013f72.css` [css] and confirmed on elements where noted [computed].

**Neutrals ("black" scale, a cool zinc grey):**

| Token | Hex | Used for |
|---|---|---|
| black (default) | #0A0A0C | All text, headings, primary buttons, rules [computed] |
| black-950 | #101013 | Home section headings |
| black-900 | #1A1A1D | |
| black-800 | #27272A | Date, related-post excerpts [computed] |
| black-700 | #3F3F46 | |
| black-600 | #71717A | |
| black-500 | #A1A1AA | Inactive TOC items, figure captions [computed] |
| black-400 | #CCCCD5 | Secondary button border, input borders [computed] |
| black-300 | #E4E4E7 | Light borders |
| black-200 | #F4F4F5 | Light panels |
| black-100 | #FAFAFA | |
| page background | #FFFFFF | `bg-white` on the page wrapper and header [computed] |

**Brand accents:**

| Token | Hex | Used for |
|---|---|---|
| electricYellow (400) | #F4FF7D | The brand highlight |
| electricYellow-500 | #F1FF5C | Eyebrow badge ("CREATORS OF TIMESCALEDB"), footer gradient, hero art backgrounds |
| electricYellow-300 | #F7FF9D | Footer gradient mid stop |
| electricYellow-100 | #FCFFDE | Tint |
| eyeOfTheTiger (500) | #4B7BFF | Pull-quote left border [computed], inline code colour (`prose-code:text-eyeOfTheTiger-500`) [class], blue post art |
| eyeOfTheTiger-200 / -300 | #DBE5FF / #B7CAFF | Tints |
| tigerBlood-500 | #FF5843 | Red post art, diagram labels |
| tigerBlood-600 | #CC4636 | |
| orange | #FF5B29 | |
| crispBlue | #A8DFF5 | |

**Roles:**
- Background: #FFFFFF. Dark bands on the home page are near-black [shot].
- Text: #0A0A0C (near-black, slightly blue), never pure #000 in content.
- Accent: electric yellow #F1FF5C / #F4FF7D for highlights; tiger blue #4B7BFF for in-content accents.
- Links: no inline links in this article's body. Elsewhere links are the same near-black, underlined (the privacy-policy link) [shot]; nav links are plain black with no underline. The Tailwind Typography default `--tw-prose-links` is #111827 [css], but the article does not use the prose class for body text.
- Code: inline code coloured #4B7BFF [class]. **No code block appears in this article**, so a code-block style could not be observed; the only `pre` rules in the CSS reset margins and set `background: transparent` [css].
- Borders: 1px #CCCCD5 on outlined buttons and inputs [computed]; 1px near-black rule under the byline [shot]; 4px #4B7BFF on pull quotes [computed].
- Footer: vertical gradient `linear-gradient(to top, #F1FF5C 0%, #F7FF9D 37.5%, #FFFFFF 67.78%)` [class on `<footer>`].

## Article layout

Measured at 1280px [computed]:

- **Page container:** `max-w-[1440px] mx-auto`, side padding 40px desktop (`md:px-10`), 16px mobile (`px-4`). Inner width 1200px at a 1280 viewport.
- **Header:** 70px tall, white, logo left (160 x 35), nav centre (Product, Industry, Docs, Pricing, Developer Hub, Company), GitHub star count, "Log In", an outlined "Contact us" button and a solid black "Start a free trial" button on the right. Buttons: 16px text, padding 10px 16px, radius 4px.
- **Headline block (full container width):** H1 left-aligned, `max-width: 1014px`, about 3 lines at 60px. Below it one row: 46px round avatar, "By Andrew Stebbins", a small square bullet, "September 16th, 2026", bullet, hourglass icon + "6 MIN" in Geist Mono. Share label and icons (X, LinkedIn, Hacker News) right-aligned on the same row. A 1px black rule spans the container under this row. No deck/standfirst under the headline; the intro is the first italic paragraphs of the body.
- **Two-column body below the rule:** `flex-row` with a 32px gap (`lg:gap-8`):
  - **Left sidebar, 306px wide, sticky** (`lg:sticky lg:top-[88px]`, max height viewport minus 112px, scrolls on overflow). Contains, top to bottom with 40px gaps: a "Copy as markdown" outlined dropdown button; tag chips (Geist Mono uppercase, small, 1px border, small radius: "DEV Q&A", "TIMESCALEDB"); the **table of contents** (mono label "TABLE OF CONTENTS" with an icon, then numbered items "01 About the project" ... "07 Looking ahead", inactive grey #A1A1AA, active black weight 500, scroll-spy highlighting); a solid black CTA button "Get started for free" with a small arrow box (padding 12px 20px, radius 4px).
  - **Content column, max 755px** (`lg:max-w-[755px]`), starting at x = 378. **Reading width = 755px.** On mobile the sidebar stacks above the content and the column is 343px.
  - The space to the right of the content (about 107px at 1280) is left empty.
- **Hero image:** first item in the content column, full 755px, in the house style: a flat brand-colour panel with a dot grid and a centred "card" graphic (here yellow #F1FF5C with a "COMMUNITY SPOTLIGHT" label).
- **Paragraph rhythm:** paragraphs are flex children with a 20px gap (`gap-5`); H2s add 24px margin-top (16px mobile), so about 44px above an H2 and 20px below; H2s have `scroll-mt-36` (144px) for anchor jumps under the sticky header.
- **Images and figures:** full column width (755px), wrapper radius 8px (`rounded-lg`), caption below in 14px italic grey #A1A1AA; images are click-to-zoom (`cursor-pointer`). Diagrams are drawn in the brand style (mono labels, coloured header bars, dot-grid background).
- **Pull quotes:** `<blockquote>` with a 4px left border in #4B7BFF, 40px padding all round, 20px / 28px italic, no background, attribution inline at the end after a hyphen.
- **Lists, tables, code:** none in this article, so not observed.
- **Related posts:** after the article, full container width: a mono label "// RELATED POSTS" over a 1px black rule, then a 3-column grid of cards (about 379px each): 16:9 image with 4px radius, tag chips, 22px semibold title, 3-line clamped excerpt in #27272A, "By Name • Date" in small text. The whole card is one link.
- **Newsletter CTA:** centred block, 80px / 88px bold "Stay updated with new posts and releases.", one-line subhead, a mono "EMAIL *" label, an input (1px #CCCCD5 border, about 50px tall) and a full-width solid black "Submit" button, privacy line below. Section padding 80px 60px.
- **Footer:** yellow-to-white gradient, mark at left, five link columns with Geist Mono uppercase headings (PRODUCTS, INDUSTRY, SUPPORT, LEARN, COMPANY), social icons right, a giant faded "Tiger Data" wordmark across the bottom, copyright and legal links at bottom right.

## Spacing rhythm

Tailwind's 4px base [class]: 8, 12, 16, 20, 32, 40 and 80px are the values in use.
- 20px between paragraphs, 32px between major blocks in the content column, 40px between sidebar groups and as the side gutter, 80px top and bottom padding on big sections.
- Buttons 10-12px vertical by 16-20px horizontal, radius 4px; image radius 4px (cards) and 8px (in-article figures).
- Headline block: about 80px from header to H1, about 30px from H1 to byline row, about 24px to the rule, 60px from the rule to the body [shot].

## Why the article page is pleasant to read

The page is quiet: white background, one near-black text colour, one typeface, and almost no chrome inside the reading column, so the 1.7 line height and generous 20px paragraph gaps do the work. The big, tightly tracked semibold headline gives a confident editorial entrance, while the metadata (read time, labels, TOC heading) switches to small uppercase Geist Mono, so the "data" voice is clearly separate from the reading voice. The sticky left rail keeps orientation (numbered TOC with scroll-spy) and the single CTA in view without interrupting the text, and colour is saved for a few strong moments: the yellow hero art, the blue quote rule, the yellow footer. One caution for our build: the 755px column at 16px Geist gives roughly 95-100 characters per line, longer than the usual 60-75 character comfort range; for a long-form editorial site we should either narrow the column to about 680-720px or set the body at 17-18px.
