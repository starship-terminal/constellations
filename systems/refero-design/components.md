# Refero components

The discovery list of every page and view captured, then one entry per component with crops of the real products, the icon index and the Gaps. Captured from refero.design and styles.refero.design on 2026-11-02, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running pages. Nothing was signed into, created, sent or uploaded.

The two hosts are one product family with two surfaces: **refero.design** is the design-research app (left rail, research box, screenshot galleries, pricing and MCP marketing); **styles.refero.design** is the public styles gallery (top bar, the video-tile card index, a documentation page per style). They share one token system: the same `--gray-solid`/`--gray-alpha` scales, `--fill-*`/`--stroke-*`/`--text-*`/`--status-*` names and the same inverted dark values, each host adding its own display serif (Title on refero.design, kalice on styles) and UI sans (Base-Variable, neueMontreal).

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (40 components, 75 states). The page layouts are described in [raw/layout.json](raw/layout.json).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Base-Variable 14/20 500, rgba(3, 14, 49, 0.54)`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (71 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x). Both hosts honour prefers-color-scheme: the dark values are in the token file's `dark` set rather than a second screenshot pass.

| Surface | URL | Screenshots |
|---|---|---|
| refero.design home. Serif headline, centred research card, coach box, the Page Types / Flows / UX Patterns sections; the two promos closed, the MCP card open, and the field focused. | `https://refero.design/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [promo](screenshots/home-light-promo.png), [research-focused](screenshots/home-light-research-focused.png) |
| refero.design web-apps search. Mode chips, Screens/Flows toggle, the wide search field and screenshot tiles down to the paywall panel. | `https://refero.design/search` | [default](screenshots/search-light-default.png), [full](screenshots/search-light-full.png) |
| refero.design iOS-apps search. The same chrome with iPhone screenshot tiles. | `https://refero.design/apps/search` | [default](screenshots/apps-light-default.png), [full](screenshots/apps-light-full.png) |
| refero.design pricing. Serif title, plan cards, student discount, enterprise band. | `https://refero.design/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| refero.design MCP. Give your AI agent design taste; install steps, Refero Skill, pricing. | `https://refero.design/mcp` | [default](screenshots/mcp-light-default.png), [full](screenshots/mcp-light-full.png) |
| styles.refero.design index. Kalice headline, search pill, chips, the video-tile card grid; one card's hover video. | `https://styles.refero.design/` | [card-hover](screenshots/styles-light-card-hover.png), [default](screenshots/styles-light-default.png), [full](screenshots/styles-light-full.png) |
| A style page. Media frame with the scroll video, favicon and kalice title, doc tabs and the similar-styles grid. | `https://styles.refero.design/style/a73148b9-449b-42cd-9f38-86ef694f500e` | [default](screenshots/styles-entity-light-default.png), [full](screenshots/styles-entity-light-full.png) |
| refero.design home at 390: top bar, the cycling headline, the research card, the MCP promo. | `https://refero.design/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [promo](screenshots/mobile-home-light-promo.png) |
| refero.design web-apps search at 390. | `https://refero.design/search` | [default](screenshots/mobile-search-light-default.png), [full](screenshots/mobile-search-light-full.png) |
| styles.refero.design index at 390: the same bar and hero over a one-column card list. | `https://styles.refero.design/` | [default](screenshots/mobile-styles-light-default.png), [full](screenshots/mobile-styles-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| MCP promo card | every refero.design page, on load | at rest; then dismissed with its own Close button for the other captures | [home-light-promo](screenshots/home-light-promo.png), [mcp-card](#mcp-card) |
| Coach box ("Tell me what you're designing") | refero.design home, on load | at rest; dismissed with its X (a cursor:pointer svg, not a button) | [coach-box](#coach-box) |
| Search-by-image affordance | the research box, every refero.design page | at rest inside the field | inside [research-box](#research-box) |
| Card hover video | styles.refero.design index | a 3-second real hover so the card's scroll-preview mp4 buffered and faded in over the poster | [styles-light-card-hover](screenshots/styles-light-card-hover.png), [styles-card-video](#styles-card-video) |
| Entity scroll video | a style page | the page loads the mp4 over the poster frame on its own | [styles-entity-light-default](screenshots/styles-entity-light-default.png), [entity-frame](#entity-frame) |
| Paywall panel | the end of each search grid | the last tile scrolls into a Sign up to see more panel | in [search-light-full](screenshots/search-light-full.png) |

## Checklist coverage

The 19 components of the library's checklist ([docs/DESIGN-SYSTEM.md](../../docs/DESIGN-SYSTEM.md)), each with the entries below that show it and the states captured across them. 9 of 19 are captured; the rest do not exist on the public pages.

| Component | Entries | States captured |
|---|---|---|
| Button | [Plan CTA button](#plan-cta-button), [Explore MCP button](#explore-mcp-button), [Copy button](#copy-button) | default, hover, focus-visible, pressed |
| Icon button | [Promo card Close button](#promo-card-close-button), [Coach close X](#coach-close-x) | default, hover, pressed |
| Link | not captured: the rail's nav links and the promo's Explore MCP were measured inside their parents, not as standalone entries | - |
| Text field | [Research box](#research-box), [Research prompt field](#research-prompt-field), [Search field](#search-field), [Search box (results page)](#search-box-results-page) | default, focus-visible, focused, filled |
| Text area | [Research box, field active](#research-box-field-active), [Research box (mobile)](#research-box-mobile) | focused, filled, default |
| Select | not captured: no public page offers one | - |
| Checkbox | not captured: no public form has one | - |
| Radio | [Mode chip](#mode-chip), [Filter chip](#filter-chip) | default, hover, focus-visible, pressed |
| Switch | not captured: the search page's Screens/Flows toggle was not measured as an entry | - |
| Tabs | [Doc tab](#doc-tab), [Doc tab, current](#doc-tab-current) | default, hover, focus-visible, pressed |
| Menu | not captured: no menu is reachable signed out | - |
| Tooltip | not captured: none appeared on hover or focus | - |
| Dialog | not captured: the only dismissible overlay is the MCP promo card, a fixed corner card rather than a modal | - |
| Toast | not captured: no toast appeared after any action the capture took signed out | - |
| Card | [Result card](#result-card), [Search result tile](#search-result-tile), [iOS app tile](#ios-app-tile), [Plan card](#plan-card), [Student discount card](#student-discount-card), [Refero MCP promo card](#refero-mcp-promo-card), [Style card](#style-card), [Similar style card](#similar-style-card), [Style card (mobile)](#style-card-mobile) | default, hover, focus-visible, pressed |
| List row | not captured: the rail's nav items were not measured as rows | - |
| Table | not captured: pricing lays plans out as cards, not a table | - |
| Avatar | [Card footer favicon](#card-footer-favicon), [Style favicon](#style-favicon) | default |
| Badge | [Student discount card](#student-discount-card) | default |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 10 components were given a real keyboard focus. 8 show a change: `research-chip` (ring shadow rgba(1, 17, 88, 0.24) 0px 0px 0px 2px), `plan-cta` (1px auto #005fcc, offset 0px), `mcp-card-cta` (1px auto #005fcc, offset 1px), `styles-card` (ring shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(111, 113, 121, 0.5) 0px 0px 0px 3px, transparent 0px 0px 0px 0px), `entity-tab` (ring shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, rgba(111, 113, 121, 0.4) 0px 0px 0px 2px, transparent 0px 0px 0px 0px), `entity-tab-active` (ring shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, #ffffff 0px 0px 0px 0px, rgba(111, 113, 121, 0.4) 0px 0px 0px 2px, transparent 0px 0px 0px 0px), `entity-copy` (ring shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(111, 113, 121, 0.5) 0px 0px 0px 3px, transparent 0px 0px 0px 0px), `styles-chip` (1px auto rgba(111, 113, 121, 0.5), offset 0px). The other 2 draw nothing new (the research input and the result card among them): `research-input`, `result-card`. Focus could not be captured on 1 more (keyboard focus never landed on them, so their readings are left out): `mcp-card-close`. The two hosts focus differently: on refero.design the browser's own `auto` outline (1px #005fcc) appears on CTAs and links, plus the research chips' custom `rgba(1, 17, 88, 0.24)` ring shadow; on styles.refero.design the controls draw their own 2-3px ring shadow in `rgba(111, 113, 121, 0.4-0.5)` (the --ring colour at half alpha).

**Pressed.** Pressed was forced with DevTools, so it is the :active styles only: the research chips and entity tabs go from muted to ink on press exactly as on hover, the MCP card's Close fills #ddddea, and the promo card's plain link takes the browser's default :active red (an artefact of the forced state, not a design colour).

**Motion.** Transitions measured on the components, by duration. The signature motion is not a transition at all: a styles card's scroll-preview mp4 fades in over the poster after a hover, and the entity page's video does the same on load (opacity 0.5s).

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0, 0, 0.2, 1)` | background-color, border-color, box-shadow, color | entity-tab, entity-tab-active |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | all, background-color, color, filter, opacity, transform | entity-copy, styles-chip |
| 0.2s | `ease` | all, border-width, padding-bottom, padding-left | mcp-card-close, plan-cta, research-chip, research-input, result-card-title |
| 0.4s | `ease` | all | coach-box |
| 0.5s | `cubic-bezier(0.4, 0, 0.2, 1)` | opacity | entity-frame |

**Layout.** Read on each page ([raw/layout.json](raw/layout.json)).

| Page | Frame | Content column | Grids | Fixed |
|---|---|---|---|---|
| home@1440 | sidebar 270px | max-width 1600px | - | New research (sticky), div (sticky), New research (sticky) |
| search@1440 | sidebar 270px | max-width 1600px | 1 grids (3 col gap 16px) | New research (sticky), div (sticky), New research (sticky) |
| apps@1440 | sidebar 270px | max-width 1600px | 1 grids (4 col gap 16px) | New research (sticky), div (sticky), New research (sticky) |
| pricing@1440 | sidebar 270px | max-width 1600px | - | New research (sticky), div (sticky), New research (sticky) |
| mcp@1440 | sidebar 270px | max-width 1600px | - | New research (sticky), div (sticky), New research (sticky) |
| styles@1440 | top bar 81px, sticky, blur(24px) | max-width 1100px | 2 grids (4 col gap 8px; 3 col gap 32px) | / (sticky) |
| entity@1440 | top bar 81px, sticky, blur(24px) | max-width 768px | - | / (sticky), Apple iPhone Duo (fixed) |
| mobile-home@390 | - | max-width 1600px | - | - |
| mobile-styles@390 | top bar 81px, sticky, blur(24px) | max-width 390px | 1 grids (2 col gap 4px) | / (sticky) |

**Card shapes.** Default-state values; the entries hold the states. The two galleries draw different cards: refero.design's tiles are rounded rectangles inside padded cards, styles.refero.design's are the signature 32px-radius padded tile with a favicon and name under it.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Research box](#research-box) | 752 x 102 | - | 24px | #f7f8fb `gray.solid.100` | rgba(12, 41, 126, 0.07) 0px 0px 0px 1px inset | 0 |
| [Result card](#result-card) | 369.98 x 228.52 | - | 8px | #eef0f6 `gray.solid.200` | none | 0px 18px |
| [Search result tile](#search-result-tile) | 347.33 x 235.91 | - | 8px | #eef0f6 `gray.solid.200` | none | 0 |
| [iOS app tile](#ios-app-tile) | 256.5 x 599.05 | - | 19% / 9.2% | #eef0f6 `gray.solid.200` | none | 0 |
| [Plan card](#plan-card) | 349.19 x 413 | - | 28px | #000000 | none | 30px |
| [Student discount card](#student-discount-card) | 1167 x 132 | - | 12px | #eef0f6 `gray.solid.200` | none | 0px 16px |
| [Refero MCP promo card](#refero-mcp-promo-card) | 320 x 445 | - | 16px | #ffffff `gray.solid.0` | rgba(7, 25, 31, 0.1) 0px 20px 40px 0px, rgba(7, 25, 31, 0.1) 0px 10px 30px 0px | 0 |
| [Research-mode coach box](#research-mode-coach-box) | 752 x 93 | T: 1px solid rgba(12, 41, 126, 0.07); R: 1px solid rgba(12, 41, 126, 0.07); L: 1px solid rgba(12, 41, 126, 0.07) | 24px 24px 0px 0px | #ffffff `gray.solid.0` | none | 12px 14px 36px 14px |
| [Style card](#style-card) | 394.66 x 338.66 | - | 32px | #f7f8fb `gray.solid.100` | none | 0 |
| [Similar style card](#similar-style-card) | 308 x 260.5 | - | 16px | #f7f8fb `gray.solid.100` | none | 0 |
| [Style card (mobile)](#style-card-mobile) | 342 x 293.75 | - | 32px | #f7f8fb `gray.solid.100` | none | 0 |

## Components

### Home and research

The home page of refero.design: a cycling serif headline over the centred research card (prompt field, Search by Image, mode chips), the coach box under it, then the Page Types / Flows / UX Patterns / UI Elements / Sites sections of screenshot cards.

#### Research box
The centred search card refero.design opens every page with: a prompt field with a Search by Image upload affordance, mode chips (Research mode, Web apps, iOS apps) and a submit. Read as `research-box` on the refero.design home page.

**Values (default).** size 752 x 102; radius 24px; background #f7f8fb `gray.solid.100`; shadow rgba(12, 41, 126, 0.07) 0px 0px 0px 1px inset; text Base-Variable 14/20 600, #13151b `gray.solid.900`; icon 20 x 20, #13151b `gray.solid.900`.

![Research box default](components/crops/research-box-default.png)

#### Research prompt field
Read as `research-input` on the refero.design home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 720 x 24; background transparent; text Base-Variable 16/24 500, #13151b `gray.solid.900`; transition padding-bottom 0.2s ease, padding-left 0.2s ease, border-width 0.2s ease; placeholder rgba(1, 17, 88, 0.24) |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Research box, field active
The same card with the prompt clicked into and sample text typed, then deleted; nothing was submitted. Read as `research-box-state` on the refero.design home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| focused | size 752 x 102; radius 24px; background #f7f8fb `gray.solid.100`; shadow rgba(12, 41, 126, 0.07) 0px 0px 0px 1px inset; text Base-Variable 14/20 600, #13151b `gray.solid.900`; icon 20 x 20, #13151b `gray.solid.900` |
| filled | text Base-Variable 16/24 500, #13151b `gray.solid.900` |

![Research box, field active focused](components/crops/research-box-state-focused.png) ![Research box, field active filled](components/crops/research-box-state-filled.png)

#### Mode chip
One of the research-box scope chips (Research mode / Web apps / iOS apps). Pressed states are forced, not clicked: a real press switches the corpus. Read as `research-chip` on the refero.design home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 119 x 36; padding 0px 16px 0px 12px; border 1px solid transparent; radius 18px; background transparent; text Base-Variable 14/20 500, rgba(3, 14, 49, 0.54); transition all 0.2s ease; icon 20 x 20, rgba(3, 14, 49, 0.54) |
| hover | text Base-Variable 14/20 500, #13151b `gray.solid.900`; icon 20 x 20, #13151b `gray.solid.900` |
| focus-visible | shadow rgba(1, 17, 88, 0.24) 0px 0px 0px 2px |
| pressed | text Base-Variable 14/20 500, #13151b `gray.solid.900`; icon 20 x 20, #13151b `gray.solid.900` |

![Mode chip default](components/crops/research-chip-default.png) ![Mode chip hover](components/crops/research-chip-hover.png) ![Mode chip focus-visible](components/crops/research-chip-focus-visible.png) ![Mode chip pressed](components/crops/research-chip-pressed.png)

#### Hero title
"Design Research for the AI Era" — the display line the home page opens with. Read as `hero-title` on the refero.design home page.

**Values (default).** size 1074 x 60; background transparent; text Title 50/60 400, transparent.

Child layers that carry the look: span 639.2x76 image linear-gradient(110deg, rgba(255, 255, 255, 0) 5.33%, rgba(255, 255, 255, 0) 32.81%, #00aa; span 1074x64 image linear-gradient(-70deg, rgba(255, 255, 255, 0) 5.33%, rgba(255, 255, 255, 0) 32.81%, #00aa.

![Hero title default](components/crops/hero-title-default.png)

#### Hero subline
Read as `hero-sub` on the refero.design home page.

**Values (default).** size 424 x 48; background transparent; text Base-Variable 16/24 500, rgba(3, 14, 49, 0.54).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Section title
A home section head (Page Types, Flows, UX Patterns, UI Elements, Sites). Read as `section-title` on the refero.design home page.

**Values (default).** size 151.75 x 40; background transparent; text Base-Variable 32/40 500, #000000.

![Section title default](components/crops/section-title-default.png)

#### Result card
A gallery card on the home page: a screenshot tile in a rounded padded card with a title under it. Measured, never followed. Read as `result-card` on the refero.design home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 369.98 x 228.52; padding 0px 18px; background transparent; text Base-Variable 16/24 500, #000000; icon 24 x 24, rgba(2, 18, 73, 0.38) `gray.alpha.500` |

Child layers that carry the look: div 334x184.5 background #eef0f6 `gray.solid.200` radius 8px; div 32x32 background rgba(45, 49, 63, 0.2) radius 50% shadow #f7f8fb `gray.solid.100` 0px 0px 0px 2px inset, rgba(45, 49, 63, 0.2) 0px 0px 0px 2px; div 24x24 background rgba(238, 240, 246, 0.78) radius 6px.

![Result card default](components/crops/result-card-default.png) ![Result card hover](components/crops/result-card-hover.png) ![Result card focus-visible](components/crops/result-card-focus-visible.png) ![Result card pressed](components/crops/result-card-pressed.png)

#### Result card label
Read as `result-card-title` on the refero.design home page.

**Values (default).** size 72.23 x 24; background transparent; text Base-Variable 16/24 500, #000000; transition all 0.2s ease.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Search and galleries

The web-apps search and the iOS-apps search: the mode chips and Screens/Flows toggle, a wider search field, then a grid of screenshot tiles (each a page thumbnail over a favicon and name) ending at a paywall panel.

#### Search box (results page)
The same research card pinned above the results on /search. Read as `search-box` on the refero.design search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1170 x 128; background transparent; text Base-Variable 20/24 500, #777d90 `gray.solid.600`; icon 24 x 24, rgba(3, 14, 49, 0.54) |
| focused | text Base-Variable 20/28 500, #000000; icon 24 x 24, #000000 |

Child layers that carry the look: div 16x16 background #eef0f6 `gray.solid.200` radius 50%; div 36x36 background #f7f8fb `gray.solid.100` radius 50% shadow rgba(12, 41, 126, 0.07) 0px 8px 16px 0px; div 1074x64 background #f7f8fb `gray.solid.100` border 1px solid rgba(12, 41, 126, 0.07) radius 24px.

![Search box (results page) default](components/crops/search-box-default.png) ![Search box (results page) focused](components/crops/search-box-focused.png)

#### Search result tile
A result card in the /search grid: a padded tile with a screen image and a favicon-and-name label. Hovered only. Read as `search-tile` on the refero.design search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 347.33 x 235.91; background transparent; text Base-Variable 16/24 500, #000000; icon 24 x 24, rgba(2, 18, 73, 0.38) `gray.alpha.500` |

Child layers that carry the look: div 347.3x191.9 background #eef0f6 `gray.solid.200` radius 8px; div 32x32 background rgba(45, 49, 63, 0.2) radius 50% shadow #f7f8fb `gray.solid.100` 0px 0px 0px 2px inset, rgba(45, 49, 63, 0.2) 0px 0px 0px 2px; div 88x32 image linear-gradient(to right, rgba(255, 255, 255, 0) 0px, #ffffff `gray.solid.0` 15%).

![Search result tile default](components/crops/search-tile-default.png) ![Search result tile hover](components/crops/search-tile-hover.png)

#### iOS app tile
A phone-shaped app card in the iOS gallery: a tall rounded screenshot tile. Hovered only. Read as `ios-tile` on the refero.design iOS apps search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 256.5 x 599.05; background transparent; text Base-Variable 16/24 500, #000000; icon 24 x 24, rgba(2, 18, 73, 0.38) `gray.alpha.500` |

Child layers that carry the look: div 256.5x555 background #eef0f6 `gray.solid.200` radius 19% / 9.2%; div 32x32 background rgba(45, 49, 63, 0.2) radius 50% shadow #f7f8fb `gray.solid.100` 0px 0px 0px 2px inset, rgba(45, 49, 63, 0.2) 0px 0px 0px 2px; div 88x32 image linear-gradient(to right, rgba(255, 255, 255, 0) 0px, #ffffff `gray.solid.0` 15%).

![iOS app tile default](components/crops/ios-tile-default.png) ![iOS app tile hover](components/crops/ios-tile-hover.png)

### Pricing

refero.design's pricing page: the serif title, plan cards, the student discount card and the enterprise band.

#### Pricing title
Read as `pricing-title` on the refero.design pricing page.

**Values (default).** size 730 x 60; background transparent; text Title 50/60 400, #000000.

![Pricing title default](components/crops/pricing-title-default.png)

#### Plan card
A pricing plan card: name, price, feature list and a call-to-action button. Read as `plan-card` on the refero.design pricing page.

**Values (default).** size 349.19 x 413; padding 30px; radius 16px 16px 0px 0px; background transparent; text Base-Variable 16/24 500, #777d90 `gray.solid.600`; icon 46 x 18, #000000.

Child layers that carry the look: div::before 349.188pxx413px background #f7f8fb `gray.solid.100`; div 289.2x56 image conic-gradient(from 180deg, #ff8475 0deg, #ff8475 5.52deg, #ff5c78 34.14deg, #ff87c6 60.76 radius 28px; div 289.2x56 background #000000 radius 28px.

![Plan card default](components/crops/plan-card-default.png)

#### Plan CTA button
The call-to-action inside a plan card. Pressed state is forced; a real press would start checkout. Read as `plan-cta` on the refero.design pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 289.19 x 56; radius 28px; background transparent; text Base-Variable 16/24 600, #f7f8fb `gray.solid.100`; transition all 0.2s ease |
| focus-visible | outline 1px auto #005fcc, offset 0px |

Child layers that carry the look: div 289.2x56 image conic-gradient(from 180deg, #ff8475 0deg, #ff8475 5.52deg, #ff5c78 34.14deg, #ff87c6 60.76 radius 28px; div 289.2x56 background #000000 radius 28px.

![Plan CTA button default](components/crops/plan-cta-default.png) ![Plan CTA button hover](components/crops/plan-cta-hover.png) ![Plan CTA button focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA button pressed](components/crops/plan-cta-pressed.png)

#### Student discount card
The info card beside the plans (Student discount / Enterprise / Integrate Refero). Read as `discount-card` on the refero.design pricing page.

**Values (default).** size 1167 x 132; padding 0px 16px; background transparent; text Base-Variable 16/24 600, #000000.

Child layers that carry the look: div 71.5x40 background #eef0f6 `gray.solid.200` radius 12px; div 124.7x40 background #eef0f6 `gray.solid.200` radius 12px; div 109.6x40 background #eef0f6 `gray.solid.200` radius 12px.

![Student discount card default](components/crops/discount-card-default.png)

### MCP page

The MCP marketing page (Give your AI agent design taste): install instructions, the Refero Skill section and pricing, plus the fixed promo card that also floats on every page.

#### MCP title
"Give your AI agent design taste" — the /mcp hero. Read as `mcp-title` on the refero.design MCP page.

**Values (default).** size 860 x 60; background transparent; text Title 50/60 400, #000000.

![MCP title default](components/crops/mcp-title-default.png)

### Promos and overlays

The two dismissable layers the home page opens with: the fixed MCP promo card at lower left and the coach box pinned under the research field. Both were closed for every other capture.

#### Refero MCP promo card
The floating card pinned over the content: "Refero MCP connects your agent to a curated library…" with an Explore MCP button and a Close. Read as `mcp-card` on the refero.design home page.

**Values (default).** size 320 x 445; radius 16px; background #ffffff `gray.solid.0`; shadow rgba(7, 25, 31, 0.1) 0px 20px 40px 0px, rgba(7, 25, 31, 0.1) 0px 10px 30px 0px; text Base-Variable 14/20 500, #777d90 `gray.solid.600`.

![Refero MCP promo card default](components/crops/mcp-card-default.png)

#### Explore MCP button
The dark button in the promo card. Measured and focused, never pressed. Read as `mcp-card-cta` on the refero.design home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 178.47 x 48; background transparent; text Base-Variable 16/24 600, #f7f8fb `gray.solid.100` |
| focus-visible | outline 1px auto #005fcc, offset 1px |

Child layers that carry the look: div 178.5x48 background #000000 radius 8px.

![Explore MCP button default](components/crops/mcp-card-cta-default.png) ![Explore MCP button hover](components/crops/mcp-card-cta-hover.png) ![Explore MCP button focus-visible](components/crops/mcp-card-cta-focus-visible.png) ![Explore MCP button pressed](components/crops/mcp-card-cta-pressed.png)

#### Promo card Close button
Dismisses the card (a styled div, not a button). Measured, never pressed: closing happens after the measurements. Read as `mcp-card-close` on the refero.design home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 87.53 x 48; padding 0px 16px; border 1px solid rgba(12, 26, 105, 0.14); radius 8px; background transparent; text Base-Variable 16/24 600, #000000; transition all 0.2s ease |
| hover, pressed | border 1px solid #dddfea `gray.solid.300`; background #dddfea `gray.solid.300` |

![Promo card Close button default](components/crops/mcp-card-close-default.png) ![Promo card Close button hover](components/crops/mcp-card-close-hover.png) ![Promo card Close button pressed](components/crops/mcp-card-close-pressed.png)

#### Research-mode coach box
The "Meet new research mode" coach a fresh profile shows once over the research input. Read as `coach-box` on the refero.design home page.

**Values (default).** size 752 x 93; padding 12px 14px 36px 14px; border T: 1px solid rgba(12, 41, 126, 0.07); R: 1px solid rgba(12, 41, 126, 0.07); L: 1px solid rgba(12, 41, 126, 0.07); radius 24px 24px 0px 0px; background #ffffff `gray.solid.0`; text Base-Variable 16/24 600, #000000; transition all 0.4s ease; icon 24 x 24, #000000.

![Research-mode coach box default](components/crops/coach-box-default.png)

#### Coach close X
The dismissal: a bare 24px svg with cursor:pointer, not a button. Measured and hovered, never clicked. Read as `coach-close` on the refero.design home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 24 x 24; background transparent; text Base-Variable 16/24 500, #000000; icon 24 x 24, #000000 |
| hover | text Base-Variable 16/24 500, rgba(3, 14, 49, 0.54); icon 24 x 24, rgba(3, 14, 49, 0.54) |

![Coach close X default](components/crops/coach-close-default.png) ![Coach close X hover](components/crops/coach-close-hover.png)

### Styles gallery

styles.refero.design's index: the kalice serif headline (Your favorite sites, in DESIGN.md), the search pill, filter chips, and the card grid whose tiles play a scroll-through video on hover.

#### Styles header
The sticky translucent bar: logo, section links and the sign-in on styles.refero.design. Read as `styles-header` on the styles.refero.design index page.

**Values (default).** size 1440 x 81; border B: 1px solid rgba(223, 225, 231, 0.5); background rgba(255, 255, 255, 0.9); text neueMontreal 25/32 530, #0d0f15.

![Styles header default](components/crops/styles-header-default.png)

#### Gallery hero
The serif violet display headline and search the index opens with. Read as `styles-hero` on the styles.refero.design index page.

**Values (default).** size 1100 x 495.22; padding 79px 24px 32px 24px; background transparent; text neueMontreal 12/16 500, #0d0f15; icon 18 x 18, #fcfcfc.

Child layers that carry the look: div 37.7x20 border 1px solid #0d0f15 radius 4px; span 6x6 background #10b981 `accent.green` radius 3.35544e+07px; span 960.3x92 image linear-gradient(110deg, transparent 5.33%, transparent 32.81%, #00aaff 41.22%, #e1e1fe 45..

![Gallery hero default](components/crops/styles-hero-default.png)

#### Gallery headline
The kalice serif display line, set in violet. Read as `styles-hero-title` on the styles.refero.design index page.

**Values (default).** size 1052 x 74.22; background transparent; text kalice 64/69.12 400, transparent.

Child layers that carry the look: span 960.3x92 image linear-gradient(110deg, transparent 5.33%, transparent 32.81%, #00aaff 41.22%, #e1e1fe 45.; span 782.7x92 image linear-gradient(-70deg, transparent 5.33%, transparent 32.81%, #00aaff 41.22%, #e1e1fe 45..

![Gallery headline default](components/crops/styles-hero-title-default.png)

#### Search field
The rounded search pill under the headline. Sample text was typed and deleted. Read as `styles-search` on the styles.refero.design index page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 671 x 46; background transparent; text neueMontreal 16/24 530, #0d0f15; placeholder rgba(111, 113, 121, 0.6) |
| filled | size 631 x 46 |

![Search field default](components/crops/styles-search-default.png) ![Search field focused](components/crops/styles-search-focused.png) ![Search field filled](components/crops/styles-search-filled.png)

#### Style card
A gallery card: a padded rounded tile holding the site screenshot, a footer with the site’s favicon, name and tagline. Read as `styles-card` on the styles.refero.design index page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 394.66 x 338.66; radius 32px; background transparent; text neueMontreal 20/28 600, #0d0f15 |
| focus-visible | shadow rgba(111, 113, 121, 0.5) 0px 0px 0px 3px |

Child layers that carry the look: div 394.7x282.7 background #f7f8fb `gray.solid.100` radius 32px; div 298.7x186.7 border 1px solid #dfe1e7 radius 8px; div 296.7x184.7 background #ffffff `gray.solid.0`.

![Style card default](components/crops/styles-card-default.png) ![Style card focus-visible](components/crops/styles-card-focus-visible.png)

#### Style card, video playing
On hover the tile’s screenshot gives way to a scroll-through video of the site, streamed from images.refero.design. Read as `styles-card-video` on the styles.refero.design index page.

**Values (video).** size 394.66 x 338.66; radius 32px; background transparent; text neueMontreal 20/28 600, #0d0f15.

Child layers that carry the look: div 394.7x282.7 background #edeef3 radius 32px; div 304.6x190.4 border 1px solid #dfe1e7 radius 8px; div 302.6x188.3 background #ffffff `gray.solid.0`.

![Style card, video playing video](components/crops/styles-card-video-video.png)

#### Card footer favicon
The site’s favicon in the card footer, ~32px in a small rounded tile. Read as `styles-card-favicon` on the styles.refero.design index page.

**Values (default).** size 40 x 40; radius 8px; background transparent; text neueMontreal 16/24 530, #0d0f15.

![Card footer favicon default](components/crops/styles-card-favicon-default.png)

#### Filter chip
A prompt/filter chip under the search. Pressed state is forced, not clicked: a real press applies the filter. Read as `styles-chip` on the styles.refero.design index page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 182 x 36; padding 0px 8px; radius 12px; background transparent; text neueMontreal 13/24 500, #6f7179; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 14 x 14, rgba(111, 113, 121, 0.7) |
| hover | background rgba(247, 248, 250, 0.6); text neueMontreal 13/24 500, #0d0f15 |
| focus-visible | outline 1px auto rgba(111, 113, 121, 0.5), offset 0px |
| pressed | background rgba(247, 248, 250, 0.6); text neueMontreal 13/24 500, #0d0f15 |

![Filter chip default](components/crops/styles-chip-default.png) ![Filter chip hover](components/crops/styles-chip-hover.png) ![Filter chip focus-visible](components/crops/styles-chip-focus-visible.png) ![Filter chip pressed](components/crops/styles-chip-pressed.png)

### Style entity page

A style's page on styles.refero.design: media frame (poster with the scroll video fading in over it), circular favicon and kalice title, the DESIGN.md / Tailwind v4 / CSS Variables / Design Tokens documentation tabs, and the similar-styles grid.

#### Media frame
The large rounded frame over the page: the site’s scroll video fades in over the poster still, border and shadow around it. Read as `entity-frame` on the styles.refero.design style page page.

**Values (default).** size 630 x 393.75; background transparent; text neueMontreal 16/24 530, #0d0f15; transition opacity 0.5s cubic-bezier(0.4, 0, 0.2, 1).

![Media frame default](components/crops/entity-frame-default.png)

#### Style name
The site’s name in the kalice display serif, next to its round favicon. Read as `entity-title` on the styles.refero.design style page page.

**Values (default).** size 361.45 x 48; background transparent; text kalice 48/48 530, #0d0f15.

![Style name default](components/crops/entity-title-default.png)

#### Style favicon
The site’s favicon in a bordered circle beside the name. Read as `entity-favicon` on the styles.refero.design style page page.

**Values (default).** size 64 x 64; radius 12px; background transparent; text neueMontreal 16/24 530, #0d0f15.

![Style favicon default](components/crops/entity-favicon-default.png)

#### Doc tab
A tab in the documentation pane (DESIGN.md, Tailwind v4, CSS Variables, Design Tokens). Pressed is forced; a real press switches the document. Read as `entity-tab` on the styles.refero.design style page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 84.41 x 44; padding 0px 10px; background transparent; text neueMontreal 13/24 500, #6f7179; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1) |
| hover | text neueMontreal 13/24 500, #0d0f15 |
| focus-visible | shadow #ffffff 0px 0px 0px 0px, rgba(111, 113, 121, 0.4) 0px 0px 0px 2px |
| pressed | text neueMontreal 13/24 500, #0d0f15 |

Child layers that carry the look: button::after 64.4062pxx1.5px background #0d0f15 radius 3.35544e+07px.

![Doc tab default](components/crops/entity-tab-default.png) ![Doc tab hover](components/crops/entity-tab-hover.png) ![Doc tab focus-visible](components/crops/entity-tab-focus-visible.png) ![Doc tab pressed](components/crops/entity-tab-pressed.png)

#### Doc tab, current
The selected tab (DESIGN.md) is measured at rest: it is the tab the page opens on. Read as `entity-tab-active` on the styles.refero.design style page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 91.39 x 44; padding 0px 10px; background transparent; text neueMontreal 13/24 600, #0d0f15; transition color 0.15s cubic-bezier(0, 0, 0.2, 1), background-color 0.15s cubic-bezier(0, 0, 0.2, 1), border-color 0.15s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0, 0, 0.2, 1) |
| focus-visible | shadow #ffffff 0px 0px 0px 0px, rgba(111, 113, 121, 0.4) 0px 0px 0px 2px |

Child layers that carry the look: button::after 71.3906pxx1.5px background #0d0f15 radius 3.35544e+07px.

![Doc tab, current default](components/crops/entity-tab-active-default.png) ![Doc tab, current focus-visible](components/crops/entity-tab-active-focus-visible.png)

#### Copy button
Copies the open document. Measured, never pressed. Read as `entity-copy` on the styles.refero.design style page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 66.44 x 28; padding 0px 10px 0px 6px; border 1px solid #dfe1e7; radius 6px; background #ffffff `gray.solid.0`; text neueMontreal 12.8/24 500, #0d0f15; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #0d0f15 |
| hover | background #edeef3 |
| focus-visible | border 1px solid #6f7179; shadow rgba(111, 113, 121, 0.5) 0px 0px 0px 3px |
| pressed | background #edeef3 |

![Copy button default](components/crops/entity-copy-default.png) ![Copy button hover](components/crops/entity-copy-hover.png) ![Copy button focus-visible](components/crops/entity-copy-focus-visible.png) ![Copy button pressed](components/crops/entity-copy-pressed.png)

#### Similar style card
A card in the Similar styles row at the foot of the page. Read as `entity-similar` on the styles.refero.design style page page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 308 x 260.5; radius 16px; background transparent; text neueMontreal 20/28 600, #0d0f15 |

Child layers that carry the look: div 308x204.5 background #f7f8fb `gray.solid.100` radius 16px; div 276x172.5 border 1px solid #dfe1e7 radius 8px; div 274x170.5 background #ffffff `gray.solid.0`.

![Similar style card default](components/crops/entity-similar-default.png) ![Similar style card hover](components/crops/entity-similar-hover.png)

### Mobile (390 wide)

The same pages as a phone draws them, at 390 x 844 with an iPhone user agent: the rail becomes a top bar on refero.design; the styles index keeps its top bar and one-column cards.

#### Style card (mobile)
Read as `m-styles-card` on the styles.refero.design index page at 390 wide.

**Values (default).** size 342 x 293.75; radius 32px; background transparent; text neueMontreal 20/28 600, #0d0f15.

Child layers that carry the look: div 342x237.8 background #f7f8fb `gray.solid.100` radius 32px; div 278x173.8 border 1px solid #dfe1e7 radius 8px; div 276x171.8 background #ffffff `gray.solid.0`.

![Style card (mobile) default](components/crops/m-styles-card-default.png)

#### Styles header (mobile)
Read as `m-styles-header` on the styles.refero.design index page at 390 wide.

**Values (default).** size 390 x 81; border B: 1px solid rgba(223, 225, 231, 0.5); background rgba(255, 255, 255, 0.9); text neueMontreal 25/32 530, #0d0f15.

![Styles header (mobile) default](components/crops/m-styles-header-default.png)

#### Research box (mobile)
Read as `m-research-box` on the refero.design home page at 390 wide.

**Values (default).** size 358 x 102; radius 24px; background #f7f8fb `gray.solid.100`; shadow rgba(12, 41, 126, 0.07) 0px 0px 0px 1px inset; text Base-Variable 14/20 600, #13151b `gray.solid.900`; icon 18 x 20, #13151b `gray.solid.900`.

![Research box (mobile) default](components/crops/m-research-box-default.png)

## Icons

51 SVGs were lifted from the pages into [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. Product artwork, favicons, brand marks and site screenshots were left out; these are the interface icons. The SVGs are Refero's property, kept for reference only.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|
| [icon-090ba326](icons/icon-090ba326.svg) | 20x20 24x24 | 0 0 24 24 | stroke | home; search; apps; pricing; mcp |  |
| [pricing](icons/pricing.svg) | 24x24 | 0 0 24 24 | stroke | home; search; apps; pricing; mcp | Pricing |
| [log-in-sign-up](icons/log-in-sign-up.svg) | 24x24 | 0 0 24 24 | stroke | home; search; apps; pricing; mcp | Log In/Sign Up |
| [styles-beta](icons/styles-beta-5205d1e5.svg) | 16x16 | 0 0 16 16 | stroke | home; search; apps; pricing; mcp | Styles Beta |
| [icon-ac10bc90](icons/icon-ac10bc90.svg) | 48x48 | 0 0 84 84 | fill | home; search; apps; pricing; mcp |  |
| [styles-beta](icons/styles-beta-bd16025d.svg) | 24x24 | 0 0 24 24 | stroke | home; search; apps; pricing; mcp | Styles Beta |
| [figma-plugin](icons/figma-plugin.svg) | 24x24 | 0 0 24 24 | stroke | home; search; apps; pricing; mcp | Figma Plugin |
| [web-apps](icons/web-apps.svg) | 20x20 24x24 | 0 0 24 24 | stroke | home; search; apps; pricing; mcp | Web apps |
| [connect-mcp](icons/connect-mcp.svg) | 24x24 | 0 0 24 24 | fill | home; search; apps; pricing; mcp | Connect MCP |
| [ios-apps](icons/ios-apps.svg) | 20x20 24x24 | 0 0 24 24 | stroke | home; search; apps; pricing; mcp | iOS apps |
| [new-research](icons/new-research.svg) | 24x16 | 0 0 16 16 | fill | home; search; apps; pricing; mcp | New research |
| [research-mode](icons/research-mode.svg) | 20x20 24x24 | 0 0 20 20 | stroke | home; search; apps; pricing; mcp | Research mode |
| [continue-with-google](icons/continue-with-google.svg) | 26x32 | 0 0 32 32 | fill | home; search; apps | Continue with Google |
| [sites](icons/sites.svg) | 24x24 40x40 | 0 0 32 32 | fill | home; pricing; mcp | Sites / Web designs: 76,000+ screens from shippe |
| [screens](icons/screens.svg) | 24x24 | 0 0 20 20 | stroke | search; apps | Screens |
| [flows](icons/flows.svg) | 24x24 | 0 0 20 20 | stroke | search; apps | Flows |
| [76-912-more-pages-hidden](icons/76-912-more-pages-hidden.svg) | 24x24 | 0 0 24 24 | stroke | search; apps | 76,912 more pages hidden / 68,643 more screens hidden |
| [connect-to-your-ai](icons/connect-to-your-ai-73c93c1e.svg) | 16x16 | 0 0 24 24 | stroke | styles; style page | Connect to your AI / Connect to your AI (opens in a new tab) |
| [g3-n](icons/g3-n.svg) | 20x20 | 0 0 20 20 | stroke | home | Paywalls with plan selection / SaaS landing pages with produ |
| [icon-a679b3d0](icons/icon-a679b3d0.svg) | 20x20 | 0 0 24 24 | stroke | home |  |
| [icon-ba4f26d8](icons/icon-ba4f26d8.svg) | 24x24 | 0 0 24 24 | fill | pricing; mcp | Figma plugin: All references directly in |
| [icon-fa18580d](icons/icon-fa18580d.svg) | 24x24 | 0 0 24 24 | fill | pricing; mcp | Refero Skill: A design methodology that  |
| [icon-0cc69986](icons/icon-0cc69986.svg) | 12x12 | 0 0 24 24 | stroke | style page | Copy Apple Blue #0066cc Inline links, se / Copy Pricing Blue |
| [icon-109b6a19](icons/icon-109b6a19.svg) | 26x26 | 0 0 17 16 | stroke | pricing |  |
| [icon-13c516ba](icons/icon-13c516ba.svg) | 62x17 | 0 0 62 17 | fill | pricing |  |
| [icon-196b0ea5](icons/icon-196b0ea5.svg) | 20x20 | 0 0 20 20 | fill | mcp | Connect your tool ChatGPT / Codex Claude |
| [icon-29c1a4f1](icons/icon-29c1a4f1.svg) | 24x24 46x18 | 0 0 46 18 | fill | pricing |  |
| [icon-2aadde8c](icons/icon-2aadde8c.svg) | 24x24 | 0 0 24 24 | fill | mcp | iOS designs: 68,000+ app screens, growin |
| [icon-35ffb877](icons/icon-35ffb877.svg) | 57x17 | 0 0 57 17 | fill | pricing |  |
| [icon-36f29fe9](icons/icon-36f29fe9.svg) | 24x24 | 0 0 24 24 | stroke | mcp |  |
| [icon-4b25f63e](icons/icon-4b25f63e.svg) | 24x24 | 0 0 60 60 | fill | mcp | Connect your tool ChatGPT / Codex Claude |
| [icon-4e34fdea](icons/icon-4e34fdea.svg) | 16x16 | 0 0 24 24 | stroke | style page | Use #ffffff as the default product-story / Set display hero  |
| [icon-4f71ed80](icons/icon-4f71ed80.svg) | 20x20 | 0 0 20 20 | fill | mcp | Connect your tool ChatGPT / Codex Claude |
| [search-styles](icons/search-styles.svg) | 18x18 | 0 0 24 24 | stroke | styles | Search styles |
| [icon-56a981a8](icons/icon-56a981a8.svg) | 14x14 | 0 0 24 24 | stroke | style page | https://www.apple.com/iphone-duo |
| [icon-66f0541a](icons/icon-66f0541a.svg) | 24x24 | 0 0 24 24 | fill | pricing |  |
| [save-60best-value](icons/save-60best-value.svg) | 20x20 | 0 0 20 20 | fill | pricing | Save $60Best Value! |
| [icon-84943d6e](icons/icon-84943d6e.svg) | 24x24 | 0 0 24 24 | stroke | pricing |  |
| [icon-8ab1b205](icons/icon-8ab1b205.svg) | 20x20 | 0 0 20 20 | fill | mcp | Connect your tool ChatGPT / Codex Claude |
| [icon-93fb15cb](icons/icon-93fb15cb.svg) | 16x16 |  | stroke | pricing | Love the filter functionality the most — / 💙 Reco du mardi:  |
| [download-design-md](icons/download-design-md.svg) | 16x16 | 0 0 24 24 | stroke | style page | Download DESIGN.md |
| [icon-9e7b1389](icons/icon-9e7b1389.svg) | 24x24 | 0 0 24 24 | stroke | home | Meet new research mode Describe your tas |
| [refero-mcp-for-ai-agents](icons/refero-mcp-for-ai-agents.svg) | 20x20 | 0 0 20 20 | fill | mcp | Refero MCP for AI agents / Refero MCP: Give your AI agent ac |
| [icon-b1fe8cbf](icons/icon-b1fe8cbf.svg) | 20x18 | 0 0 20 20 | fill | mcp | Connect your tool ChatGPT / Codex Claude |
| [icon-bc990c54](icons/icon-bc990c54.svg) | 16x16 | 0 0 16 16 | fill | pricing |  |
| [connect-to-your-ai](icons/connect-to-your-ai-c6672cf9.svg) | 14x14 | 0 0 24 24 | stroke | style page | Connect to your AI |
| [icon-dc2bc024](icons/icon-dc2bc024.svg) | 20x20 | 0 0 20 20 | fill | mcp | Connect your tool ChatGPT / Codex Claude |
| [copy](icons/copy.svg) | 16x16 | 0 0 24 24 | stroke | style page | Copy |
| [chalk-charcoal](icons/chalk-charcoal.svg) | 14x14 | 0 0 24 24 | stroke | styles | Chalk & charcoal / Brutalist portfolio / Linear-style SaaS |
| [icon-ed3455c0](icons/icon-ed3455c0.svg) | 10x16 | 0 0 10 16 | fill | pricing |  |
| [icon-f6adc5e0](icons/icon-f6adc5e0.svg) | 16x16 | 0 0 24 24 | stroke | style page | Do not add gradients; product imagery su / Do not use shadow |

## Gaps

### Pages

- **Signed-in pages.** Nothing behind Log In / Sign Up was captured: saved research, the account page, and whatever the New research button's submit does past its empty state. The kit never signs in.
- **Paywalled results.** Both search pages end their grids at a Sign-up-to-see-more panel; the full libraries (web apps, iOS apps, flows and the site pages a card links to) were not entered.
- **The Figma plugin and the checkout.** The Figma Plugin link and the plan CTAs lead off the measured scope; no purchase was made and no card field was filled.
- **New research as a flow.** The mode chips were measured, but submitting a prompt creates a research job, so the result page and its streaming UI are missing.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing; the promo card's plain link paints the browser's default :active red under the forced state.
- **The home h1 cycles** its second line through colourways (the --reveal-* gradient vars on the shell, driven by the same-name keyframe animation); a capture pins whichever pass was running.
- **The Page Types cards rotate** their product links on a timer and are rebuilt by the page's hydration; the measured card is whichever the timer had dealt.
- **Disabled and loading** were not seen on any public control, and **error** exists only as declared status colours.

### Themes

Both hosts ship a light and a dark theme. refero.design applies `body#dark-theme` manually or `body:not(#light-theme)` under prefers-color-scheme: dark; styles.refero.design holds its dark values on `:root` under the same media query. Every page painted dark under prefers-color-scheme: dark (`themeChecks` in [raw/css-vars.json](raw/css-vars.json)). The token file carries a `dark` set built from those declarations; the screenshots stayed in light, so dark component appearance is unverified beyond the variable values.

### Fonts

- **Base-Variable** (refero.design UI, 200-800) and **Title** (its serif display) are self-hosted faces; neither is on a public font CDN.
- **neueMontreal** (styles.refero.design UI, drawn at weight 530), **kalice** (its serif display) and **JetBrains Mono** (the documentation panes) are served by the Next app; kalice and neueMontreal are commercial faces.
- The README's guidance on these fonts applies: substitute close free faces (Instrument Serif for the display serifs, Inter/Public Sans for the UI, JetBrains Mono is freely available) when reproducing the style.

### Screenshots

- Site thumbnails, favicons, app screenshots and the scroll-preview videos inside cards are Refero's content and appear only inside screenshots and crops.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- The text a style's documentation tabs render was not transcribed into the package; the tab controls and the pane around them were measured.
- No personal data was captured: the pages were read signed out.
