# Subjects: article topic to one-noun visual

Pick the row closest to the article's title. **Subject** is what goes in the spec's `subject`: a
library key (drawn by hand in `thumbnail.py`, works in every style) or `icon:<phosphor-name>` (a big
Phosphor icon on a disc; works in every style, plainer). **Pixel** is the Pixelarticons glyph for
styles 3 and 5 (pass it as `pixel` when it is not the default). **Steps** are the Phosphor icons for
style 4; a dash means the subject has no real sequence and style 4 falls to the next style.

Icons available offline: `research/mockups/vendor/phosphor/regular/` and `fill/` (same names),
`research/mockups/vendor/pixelarticons/`. To add an icon, fetch it from the same package version (see
`sources.md`) into those folders.

## Library subjects (hand-drawn, strongest)

| Topic | One-noun visual | Subject | Pixel | Steps (style 4) |
|---|---|---|---|---|
| PRD, spec, one-pager, brief | document | `prd` | file-text | note, users, list-checks, check-circle |
| Usability test, UX audit, heuristic review | magnifier | `usability-test` | search | clipboard-text, eye, note, wrench |
| Roadmap, planning, now-next-later | timeline | `roadmap` | flag | lightbulb, flask, rocket-launch, chart-line-up |
| Retention, churn, cohort, any metric chart | curve (falling, then flat) | `retention-chart` | chart-line | - |
| Persona, user profile, JTBD profile | profile card | `persona` | avatar-square | - |
| Research plan, interview guide, discovery | clipboard | `research-plan` | clipboard-note | question, users, chats-circle, lightbulb |
| Prioritization (RICE, MoSCoW, 2 x 2) | matrix | `prioritization-matrix` | grid-2x2-2 | - |
| Design system, components, tokens | component grid | `design-system` | blocks | - |
| Sprint, Scrum, iteration, retro | loop | `sprint` | reload | kanban, code, presentation-chart, chats-circle |
| Hiring, interviewing candidates, career | briefcase | `hiring-guide` | briefcase | file-text, chats-circle, scales, handshake |

## Icon subjects (`icon:<name>`)

| Topic | One-noun visual | Subject | Pixel | Steps (style 4) |
|---|---|---|---|---|
| A/B test, experiment | flask | `icon:flask` | test-tube | lightbulb, flask, chart-bar, check-circle |
| Analytics, dashboards, KPIs | gauge | `icon:gauge` | analytics | - |
| Funnel, conversion, onboarding drop-off | funnel | `icon:funnel` | filter | users, cursor, shopping-cart, check-circle |
| Pricing, monetization, willingness to pay | coins | `icon:coins` | coins | - |
| Business model, unit economics | piggy bank | `icon:piggy-bank` | money | - |
| Stakeholders, alignment, buy-in | handshake | `icon:handshake` | users | - |
| Strategy, vision, positioning | compass | `icon:compass` | directions | - |
| OKRs, goals, north-star metric | target | `icon:target` | target | flag, target, chart-line-up, trophy |
| Launch, go-to-market | rocket | `icon:rocket-launch` | zap | megaphone, rocket-launch, chart-line-up |
| Onboarding, first-run experience | signpost | `icon:signpost` | road-sign | user, cursor, check-circle, star |
| Customer interviews, user feedback | speech bubbles | `icon:chats-circle` | message-text | question, microphone, note, lightbulb |
| Surveys, NPS | clipboard | `icon:clipboard-text` | checkbox-on | - |
| Information architecture, sitemaps | tree | `icon:tree-structure` | git-branch | - |
| Wireframes, prototyping | layout | `icon:layout` | layout | pencil-simple, layout, cursor, check-circle |
| Accessibility | eye | `icon:eye` | eye | - |
| Mobile UX | phone | `icon:device-mobile` | smartphone | - |
| Writing, UX copy, content design | pencil | `icon:pencil-simple` | pencil | - |
| Visual design, colour, type | palette | `icon:palette` | colors-swatch | - |
| Decision-making, trade-offs | scales | `icon:scales` | scale | - |
| Meetings, workshops, facilitation | presentation | `icon:chalkboard-teacher` | teach | - |
| Product sense, ideas, ideation | light bulb | `icon:lightbulb` | lightbulb | - |
| Bugs, quality, incidents | bug | `icon:bug` | bug | - |
| Feature flags, settings, configuration | sliders | `icon:sliders` | sliders | - |
| Data, databases, tracking plans | database | `icon:database` | database | - |
| Email, newsletters, lifecycle messaging | envelope | `icon:envelope` | mail | - |
| Books, reading lists, learning | open book | `icon:book-open` | book-open | - |
| Templates, toolkits | stack | `icon:stack` | notes | - |
| Leadership, managing a team | crown | `icon:crown` | crown | - |
| Customer support, service design | headset | `icon:headset` | message-reply | - |
| Security, privacy, trust | shield | `icon:shield-check` | shield | - |
| AI features, automation | robot | `icon:robot` | robot | - |

## Choosing well

- Name the object, not the idea: "a document with a checklist", not "clarity".
- One subject. If two come to mind (a PRD and an engineer), pick the one a reader would search for.
- When a new topic recurs (three articles or more), draw it as a library subject in `thumbnail.py`
  (a `s_<name>(pen)` function plus a row in `SUBJECTS` and, for flow lines, `FLOWS`) and add it here.
