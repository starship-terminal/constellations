# Fiverr components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from fiverr.com on 2026-11-15, signed out, in Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; the join, login, search and every other field was typed into then cleared and never sent; every link and CTA was measured, never followed. PerimeterX's press&hold was driven automatically, never answered by hand; the UserWay widget and consent layers were hidden, never answered.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (24 components, 60 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Macan 56/61.6 700, #ffffff`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (55 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png` where `{theme}` is the mode the page painted at capture: `light` for every public page — fiverr.com declares no :root custom properties and ships no theme switch, so light is the only painted theme (the hero search form's `dark` class is a component skin, not a site theme). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages bounded at eight chunks — a page that reports an unbounded scrollHeight is truncated with the boundary recorded in the shot's `.capture.json` sidecar; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [drawer](screenshots/home-light-drawer.png), [full](screenshots/home-light-full.png) |
| Categories directory | `/categories` | [default](screenshots/categories-light-default.png), [full](screenshots/categories-light-full.png) |
| Graphics & Design | `/categories/graphics-design` | [default](screenshots/category-design-light-default.png), [full](screenshots/category-design-light-full.png) |
| Creative Logo Design | `/categories/graphics-design/creative-logo-design` | [default](screenshots/subcategory-logo-light-default.png), [full](screenshots/subcategory-logo-light-full.png) |
| Search results | `/search/gigs?query=logo%20design` | [default](screenshots/search-light-default.png), [full](screenshots/search-light-full.png) |
| Gig page | `the first gig on the results grid` | [default](screenshots/gig-light-default.png), [full](screenshots/gig-light-full.png) |
| Seller profile | `that gig's seller` | [default](screenshots/seller-light-default.png), [full](screenshots/seller-light-full.png) |
| Logo Maker | `/logo-maker` | [default](screenshots/logo-maker-light-default.png), [full](screenshots/logo-maker-light-full.png) |
| About | `/about-us` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Become a Seller | `/start_selling` |  |
| How Fiverr works | `/cp/how-fiverr-works` | [default](screenshots/how-it-works-light-default.png), [full](screenshots/how-it-works-light-full.png) |
| Sign in | `/login` | [default](screenshots/login-light-default.png), [full](screenshots/login-light-full.png) |
| Join | `/join` | [default](screenshots/join-light-default.png), [full](screenshots/join-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [drawer](screenshots/mobile-home-light-drawer.png), [full](screenshots/mobile-home-light-full.png) |
| Categories, phone | `/categories` |  |
| Search, phone | `/search/gigs?query=logo%20design` | [default](screenshots/mobile-search-light-default.png), [full](screenshots/mobile-search-light-full.png) |
| Sign in, phone | `/login` |  |
| Join, phone | `/join` | [default](screenshots/mobile-join-light-default.png), [full](screenshots/mobile-join-light-full.png) |


### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| PerimeterX challenge | entry pages | the scripted press&hold solver drives the 'PRESS & HOLD' control automatically and the clearance cookie is kept; it was never answered by hand | solved, not shown |
| UserWay + consent layers | every page | the accessibility widget and any consent layer are hidden before every shot and reading — never clicked, never answered | hidden, never answered |
| Categories drawer | every page header | clicked the 'Sidebar menu' hamburger (a local UI toggle; keyboard Enter is the fallback) | [home-light-sidebar](screenshots/home-light-sidebar.png), [drawer](#categories-drawer) |
| Filter dropdowns | /search/gigs | clicked a filter trigger (Category, Service Options, Seller Details, Budget, Delivery Time) — a local UI toggle | [filter-btn](#filter-button) |
| Package tabs | a gig page | measured at rest — switching a tab re-prices the card, so they were never switched | [pkg-tablist](#package-tabs), [pkg-tab](#package-tab) |
| FAQ accordions | a gig page, /cp/how-fiverr-works | clicked the question row — a local UI toggle | [faq-acc](#faq-accordion), [hiw-faq](#hiw-faq-accordion) |
| Hero search | home | typed into then cleared — the form was never submitted, nothing was searched | [hero-search-input](#hero-search-field) |
| Join/login fields | /join and /login | typed into then cleared — nothing sent; Continue-with-* was never pressed | [login-email](#email-username-field), [login-password](#password-field), [join-field](#join-field) |
| Signed-in product | a Fiverr account | buyer/seller dashboards, inbox, checkout and every post-login surface needs an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 11 components were given a real keyboard focus. 8 draw an outline ring: `nav-ai` (2px solid #222325 `core.color.neutral.ink`, offset 1px), `nav-seller` (2px solid #222325 `core.color.neutral.ink`, offset 1px), `nav-signin` (2px solid #222325 `core.color.neutral.ink`, offset 1px), `nav-join` (2px solid #222325 `core.color.neutral.ink`, offset 1px), `popular-chip` (2px solid #ffffff `light.text.onAccent`, offset 1px), `footer-link` (2px solid #222325 `core.color.neutral.ink`, offset 1px), `footer-locale` (2px solid #74767e `core.color.neutral.faint`, offset 1px), `footer-currency` (2px solid #74767e `core.color.neutral.faint`, offset 1px). The other 3 show no measured change: `nav-locale`, `cat-nav`, `hero-search-btn`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.07s | `cubic-bezier(0.75, 0, 0.25, 1)` | all | footer-currency, footer-locale, hero-search-btn, nav-ai, nav-join, nav-seller, nav-signin, popular-chip and more |
| 0.1s | `ease` | background | nav-locale |
| 0.15s | `ease-in-out` | all | hero-search-input |
| 0.2s | `ease` | color | cat-card, cat-nav, footer-link, mkt-logo |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|

## Components

### Site chrome

The sticky header on every public page: the Fiverr wordmark, the Sidebar-menu hamburger that slides in the Browse-categories drawer, Connect to your AI, the EN locale button, Become a Seller, Sign in and the green Join pill; the category strip runs beneath.

#### Site header
The sticky top bar on every public page: the Fiverr wordmark, the Sidebar-menu hamburger, "Connect to your AI", the EN locale button, Become a Seller, Sign in and the green Join pill. Read as `mkt-header` on home.

**Values (default).** size 1425 x 86; background transparent; text Macan 16/24 600, #222325 `core.color.neutral.ink`; layers div.search-bar-dim-background 1425.0x0.0 rgb(0, 0, 0); header._188cbt6._bbx8bt 1425.0x86.0 rgb(255, 255, 255) B:1px solid rgb(218, 219, 221); button._arosdn._1xeo152 0.0x0.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 8px; input.long-placeholder 436.2x42.0 rgb(255, 255, 255) T:1px solid rgb(197, 198, 201) / B:1px solid r.

Child layers that carry the look: div 1425x0 background #000000 `core.color.neutral.scrim`; header 1425x86 background #ffffff `light.text.onAccent` border 1px solid #dadbdd `core.color.neutral.line`; button 0x0 border 1px solid transparent radius 8px.

![Site header default](components/crops/mkt-header-default.png)

#### Logo
The Fiverr wordmark in the header, linking home. Read as `mkt-logo` on home.

**Values (default).** size 90 x 35; background transparent; text Macan 16/24 400, #222325 `core.color.neutral.ink`; transition color 0.2s ease; icon 90 x 28, #222325 `core.color.neutral.ink`.

![Logo default](components/crops/mkt-logo-default.png)

#### Sidebar menu button
The header hamburger that opens the Browse-categories drawer — a local UI toggle; the opened state was measured after its own click. Read as `sidebar-btn` on home.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: opened) | size 0 x 0; border 1px solid transparent; radius 8px; background transparent; text Macan 16/24 600, #222325 `core.color.neutral.ink`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1) |
| pressed | background #efeff0 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Connect to your AI button
The header "Connect to your AI" button (the Fiverr AI-assistant entry); measured, never pressed. Read as `nav-ai` on home.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 242.91 x 42; padding 8px 16px; border 1px solid transparent; radius 8px; background transparent; text Macan 16/24 600, #222325 `core.color.neutral.ink`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1); icon 20 x 20, #222325 `core.color.neutral.ink` |
| hover | background #f5f5f5 `core.color.neutral.hover-wash` |
| focus-visible | outline 2px solid #222325 `core.color.neutral.ink`, offset 1px |
| pressed | background #efeff0 |

![Connect to your AI button default](components/crops/nav-ai-default.png) ![Connect to your AI button hover](components/crops/nav-ai-hover.png) ![Connect to your AI button focus-visible](components/crops/nav-ai-focus-visible.png) ![Connect to your AI button pressed](components/crops/nav-ai-pressed.png)

#### Locale button
The "EN" header button — a local UI toggle for the language list; measured, never toggled. Read as `nav-locale` on home.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 79.91 x 42; padding 8px 16px; border 1px solid transparent; radius 8px; background transparent; text Macan 16/24 600, #222325 `core.color.neutral.ink`; transition background 0.1s ease; icon 16 x 16, #222325 `core.color.neutral.ink` |
| hover, pressed | background #f5f5f5 `core.color.neutral.hover-wash` |

![Locale button default](components/crops/nav-locale-default.png) ![Locale button hover](components/crops/nav-locale-hover.png) ![Locale button focus-visible](components/crops/nav-locale-focus-visible.png) ![Locale button pressed](components/crops/nav-locale-pressed.png)

#### Become a Seller link
The header "Become a Seller" link to /start_selling; measured, never followed. Read as `nav-seller` on home.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 159 x 42; padding 8px 16px; border 1px solid transparent; radius 8px; background transparent; text Macan 16/24 600, #222325 `core.color.neutral.ink`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1) |
| hover | background #f5f5f5 `core.color.neutral.hover-wash` |
| focus-visible | outline 2px solid #222325 `core.color.neutral.ink`, offset 1px |
| pressed | background #efeff0 |

![Become a Seller link default](components/crops/nav-seller-default.png) ![Become a Seller link hover](components/crops/nav-seller-hover.png) ![Become a Seller link focus-visible](components/crops/nav-seller-focus-visible.png) ![Become a Seller link pressed](components/crops/nav-seller-pressed.png)

#### Sign in link
The header "Sign in" link to /login; measured, never followed. Read as `nav-signin` on home.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 85.02 x 42; padding 8px 16px; border 1px solid transparent; radius 8px; background transparent; text Macan 16/24 600, #222325 `core.color.neutral.ink`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1) |
| hover | background #f5f5f5 `core.color.neutral.hover-wash` |
| focus-visible | outline 2px solid #222325 `core.color.neutral.ink`, offset 1px |
| pressed | background #efeff0 |

![Sign in link default](components/crops/nav-signin-default.png) ![Sign in link hover](components/crops/nav-signin-hover.png) ![Sign in link focus-visible](components/crops/nav-signin-focus-visible.png) ![Sign in link pressed](components/crops/nav-signin-pressed.png)

#### Join CTA
The green "Join" header pill to /join — the primary header action; measured, never followed. Read as `nav-join` on home.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 88 x 42; padding 8px 16px; border 1px solid transparent; radius 8px; background #222325 `core.color.neutral.ink`; text Macan 16/24 600, #ffffff `light.text.onAccent`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1) |
| hover | background #404145 `core.color.neutral.body` |
| focus-visible | outline 2px solid #222325 `core.color.neutral.ink`, offset 1px |
| pressed | background #62646a `core.color.neutral.muted` |

![Join CTA default](components/crops/nav-join-default.png) ![Join CTA hover](components/crops/nav-join-hover.png) ![Join CTA focus-visible](components/crops/nav-join-focus-visible.png) ![Join CTA pressed](components/crops/nav-join-pressed.png)

#### Category nav link
A category-strip link under the header (Trending, Graphics & Design, Programming & Tech, …); measured, never followed. Read as `cat-nav` on home.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 142.39 x 40; padding 8px 0px; background transparent; text Macan 16/24 400, #62646a `core.color.neutral.muted`; transition color 0.2s ease |
| hover | text Macan 16/24 400, #74767e `core.color.neutral.faint`; layers ::after rgb(29, 191, 115) 0px none 1; a::after 142.391pxx3px rgb(29, 191, 115) |
| pressed | text Macan 16/24 400, #74767e `core.color.neutral.faint` |

![Category nav link default](components/crops/cat-nav-default.png) ![Category nav link hover](components/crops/cat-nav-hover.png) ![Category nav link focus-visible](components/crops/cat-nav-focus-visible.png) ![Category nav link pressed](components/crops/cat-nav-pressed.png)

#### Categories drawer
The "Browse categories" drawer the Sidebar-menu hamburger slides in from the left: category tree links, English/currency buttons, Join Fiverr and Sign in. Its links were never followed. Read as `drawer` on home.

Not on the page when it was captured.

#### Drawer category link
A category link inside the open drawer; measured, never followed. Read as `drawer-item` on home.

Not on the page when it was captured.

#### Drawer Join button
The "Join Fiverr" button at the drawer's foot; measured, never pressed. Read as `drawer-join` on home.

Not on the page when it was captured.

### Home

The home page: the hero headline over the dark band, the dark-skinned hero search form (a component skin, not a theme), the popular-service chips, the category card tiles and the marketing sections.

#### Hero headline
"Our freelancers will take it from here" — the home hero display heading over the dark hero band. Read as `hero-h1` on home.

**Values (default).** size 612.58 x 172.81; background transparent; text Macan 72/86.4 280, #ffffff `light.text.onAccent`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero search form
The hero search field — the `dark`-skinned pill inside the light page: an input plus its green submit button. Read as `hero-search` on home.

**Values (default).** size 486.17 x 42; background transparent; text Macan 16/24 400, #62646a `core.color.neutral.muted`; icon 16 x 16, #ffffff `light.text.onAccent`; layers input.long-placeholder 436.2x42.0 rgb(255, 255, 255) T:1px solid rgb(197, 198, 201) / B:1px solid rgb(197, 198, 201) / L:1px solid rgb(197, 198, 201) 4px 0px 0px 4px; input.short-placeholder 0.0x0.0 rgb(255, 255, 255) T:1px solid rgb(197, 198, 201) / B:1px solid rgb(197, 198, 201) / L:1px solid rgb(197, 198, 201) 4px 0px 0px 4px; button._arosdn._1xeo152 50.0x42.0 rgb(34, 35, 37) T:1px solid rgba(0.

Child layers that carry the look: input 436.2x42 background #ffffff `light.text.onAccent` border 1px solid #c5c6c9 `core.color.neutral.field-line` radius 4px 0px 0px 4px; input 0x0 background #ffffff `light.text.onAccent` border 1px solid #c5c6c9 `core.color.neutral.field-line` radius 4px 0px 0px 4px; button 50x42 background #222325 `core.color.neutral.ink` border 1px solid transparent radius 0px 4px 4px 0px.

![Hero search form default](components/crops/hero-search-default.png)

#### Hero search field
The "Search for any service" input inside the dark search form; focused and typed into then cleared — never searched. Read as `hero-search-input` on home.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 436.17 x 42; padding 10px 2px 10px 16px; border T: 1px solid #c5c6c9 `core.color.neutral.field-line`; B: 1px solid #c5c6c9 `core.color.neutral.field-line`; L: 1px solid #c5c6c9 `core.color.neutral.field-line`; radius 4px 0px 0px 4px; background #ffffff `light.text.onAccent`; text Macan 16/24 400, #62646a `core.color.neutral.muted`; transition all 0.15s ease-in-out; placeholder #95979d |

![Hero search field default](components/crops/hero-search-input-default.png) ![Hero search field focused](components/crops/hero-search-input-focused.png) ![Hero search field filled](components/crops/hero-search-input-filled.png)

#### Search submit
The green search submit button inside the hero form; its states were measured but it was never clicked — nothing was searched. Read as `hero-search-btn` on home.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 48 x 48; padding 8px 16px; border 1px solid transparent; radius 8px; background #222325 `core.color.neutral.ink`; text Macan 14/14 700, #ffffff `light.text.onAccent`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1); icon 18 x 18, #ffffff `light.text.onAccent` |
| hover, pressed | background #404145 `core.color.neutral.body` |

![Search submit default](components/crops/hero-search-btn-default.png) ![Search submit hover](components/crops/hero-search-btn-hover.png) ![Search submit focus-visible](components/crops/hero-search-btn-focus-visible.png) ![Search submit pressed](components/crops/hero-search-btn-pressed.png)

#### Popular-service chip
A "Popular services" pill under the hero (Website Development, Logo Design, …); measured, never followed. Read as `popular-chip` on home.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 232.72 x 42; padding 8px 16px; border 1px solid #ffffff `light.text.onAccent`; radius 8px; background rgba(255, 255, 255, 0.1) `core.color.neutral.on-dark-wash`; text Macan 16/24 400, #ffffff `light.text.onAccent`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1); icon 13.91 x 16, #ffffff `light.text.onAccent` |
| focus-visible | outline 2px solid #ffffff `light.text.onAccent`, offset 1px |

![Popular-service chip default](components/crops/popular-chip-default.png) ![Popular-service chip hover](components/crops/popular-chip-hover.png) ![Popular-service chip focus-visible](components/crops/popular-chip-focus-visible.png) ![Popular-service chip pressed](components/crops/popular-chip-pressed.png)

#### Category card
A service-category card tile further down the home page; measured, never followed. Read as `cat-card` on home.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 138.3 x 14; background transparent; text Macan 14/22 400, #222325 `core.color.neutral.ink`; transition color 0.2s ease |

![Category card default](components/crops/cat-card-default.png) ![Category card hover](components/crops/cat-card-hover.png)

#### Section heading
A marketing section heading ("Make it all happen with freelancers", …). Read as `section-h2` on home.

**Values (default).** size 720 x 50.41; background transparent; text Macan 48/50.4 400, #404145 `core.color.neutral.body`.

![Section heading default](components/crops/section-h2-default.png)

#### Rating badge
A star-rating badge on the page (seller ratings, reviews strip); recorded missing when none renders. Read as `trust-badge` on home.

Not on the page when it was captured.

### Footer

The page footer: sitemap columns, social icons and the English-language and currency buttons.

#### Footer
The page footer: category sitemap columns, company links, social icons and the language/currency buttons. Read as `footer` on home.

**Values (default).** size 480 x 91; padding 24px; border T: 1px solid #dadbdd `core.color.neutral.line`; background transparent; text Macan 16/24 600, #ffffff `light.text.onAccent`.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer sitemap link; measured, never followed. Read as `footer-link` on home.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 53.23 x 14; background transparent; text Macan 14/22 400, #222325 `core.color.neutral.ink`; transition color 0.2s ease |
| focus-visible | outline 2px solid #222325 `core.color.neutral.ink`, offset 1px; layers a._ifhvih._tgicbx 53.2x14.0 2px solid rgb(34, 35, 37) offset 1px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Footer locale button
The "English" button in the footer — a local UI toggle for the locale list; measured, never toggled. Read as `footer-locale` on home.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 97.73 x 36; padding 6px 12px; border 1px solid transparent; radius 8px; background transparent; text Macan 14/22 600, #74767e `core.color.neutral.faint`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1); icon 16 x 16, #74767e `core.color.neutral.faint` |
| hover | background #fafafa |
| focus-visible | outline 2px solid #74767e `core.color.neutral.faint`, offset 1px |
| pressed | background #f5f5f5 `core.color.neutral.hover-wash` |

![Footer locale button default](components/crops/footer-locale-default.png) ![Footer locale button hover](components/crops/footer-locale-hover.png) ![Footer locale button focus-visible](components/crops/footer-locale-focus-visible.png) ![Footer locale button pressed](components/crops/footer-locale-pressed.png)

#### Currency button
The currency button in the footer ("S$ SGD" for this client — prices localize); measured, never toggled. Read as `footer-currency` on home.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 76.91 x 36; padding 6px 12px; border 1px solid transparent; radius 8px; background transparent; text Macan 14/22 600, #74767e `core.color.neutral.faint`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1) |
| hover | background #fafafa |
| focus-visible | outline 2px solid #74767e `core.color.neutral.faint`, offset 1px |
| pressed | background #f5f5f5 `core.color.neutral.hover-wash` |

![Currency button default](components/crops/footer-currency-default.png) ![Currency button hover](components/crops/footer-currency-hover.png) ![Currency button focus-visible](components/crops/footer-currency-focus-visible.png) ![Currency button pressed](components/crops/footer-currency-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Fiverr wordmark, the gig-card collect heart, the category-tile glyphs, social and rating glyphs) are the product's artwork. Declared under layoutGaps in the catalog entry.

## Gaps

### The signed-in marketplace

Fiverr's product is the marketplace behind the account: the buyer dashboard, orders and inbox, checkout and payments, the seller studio and Fiverr Go — every surface after Sign in needs an account and was never reached. /login and /join are the only account surfaces a signed-out visitor sees, and they were measured as forms, never submitted; Continue-with-Google/Apple was never pressed.

### Pages

- **The account.** Buyer and seller dashboards, orders, inbox, checkout and payment, the seller studio and post-login gig management were never reached.
- **Forms.** The hero search, the join and login fields were measured at rest and typed into then cleared — nothing was sent; what a search or submission returns was seen only where the site serves it anonymously (the /search/gigs results grid was captured at its public URL).
- **Checkout.** The gig card's Continue button was measured, never pressed — the order/checkout flow it leads to is uncaptured.
- **Messages.** Contact me was measured, never pressed — the message flow it fronts needs an account.
- **Filter results.** A filter trigger's opened panel was captured; applying a filter re-runs the search, so filtered result states were not exercised.
- **Locale and currency lists.** The EN / currency buttons were measured at rest; the lists they open are local toggles that were not exercised; prices were seen localized to this client's currency (SGD).
- **Deeper marketing pages.** Fiverr Pro, success stories, nonprofits, jobs, press and legal pages linked from the footer are index-linked but were not captured; the same templates, unmeasured.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error, loading and validation states** were not seen on the public surface — the forms were never submitted.
- **Package tabs' alternate panels** were not switched (switching re-prices the card), so the Standard/Premium price and deliverables are uncaptured.

### Themes

Every public fiverr.com page paints a single light theme: the site declares no `:root` custom properties and ships no theme switch — no page carried a dark attribute or class while captured. The hero search form's own `dark` class is a component skin inside the light page, measured as a component, not a dark theme.

### Fonts

- **Macan** (self-hosted woff2 under npm-assets.fiverrcdn.com, weights 400/600/700) carries every heading, control and body on the public site, with an Arial-metric fallback; the style guide falls back to system sans.

The capture ran `tools/capture/public/measure.mjs` (component readings), `tools/capture/public/public.mjs` (screenshots), `tools/capture/vars.mjs` (the stylesheet harvest), `tools/capture/public/build-measurements.mjs` (raw/measurements.md) and `tools/build_components_md.py` (this file).

