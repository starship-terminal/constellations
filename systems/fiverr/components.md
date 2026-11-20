# Fiverr components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from fiverr.com on 2026-11-15, signed out, in Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; the join, login, search and every other field was typed into then cleared and never sent; every link and CTA was measured, never followed. PerimeterX's press&hold was driven automatically, never answered by hand; the UserWay widget and consent layers were hidden, never answered.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (77 components, 158 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Macan 56/61.6 700, #ffffff`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (138 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png` where `{theme}` is the mode the page painted at capture: `light` for every public page — fiverr.com's sheets declare ~1,290 custom properties on `:root`, all named by content hash (a token-free layer with no semantic names to alias), and no page ships a theme switch, so light is the only painted theme (the hero search form's `dark` class is a component skin, not a site theme). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages bounded at eight chunks — a page that reports an unbounded scrollHeight is truncated with the boundary recorded in the shot's `.capture.json` sidecar; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

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
| Become a Seller | `/start_selling` | [default](screenshots/selling-light-default.png), [full](screenshots/selling-light-full.png) |
| How Fiverr works | `/cp/how-fiverr-works` | [default](screenshots/how-it-works-light-default.png), [full](screenshots/how-it-works-light-full.png) |
| Legal portal | `/legal-portal` | [default](screenshots/legal-light-default.png), [full](screenshots/legal-light-full.png) |
| Sign in | `/login` | [default](screenshots/login-light-default.png), [full](screenshots/login-light-full.png) |
| Join | `/join` | [default](screenshots/join-light-default.png), [full](screenshots/join-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [drawer](screenshots/mobile-home-light-drawer.png), [full](screenshots/mobile-home-light-full.png) |
| Search, phone | `/search/gigs?query=logo%20design` | [default](screenshots/mobile-search-light-default.png), [full](screenshots/mobile-search-light-full.png) |
| Gig page, phone | `the same gig at 390 wide` | [default](screenshots/mobile-gig-light-default.png), [full](screenshots/mobile-gig-light-full.png) |
| Join, phone | `/join` | [default](screenshots/mobile-join-light-default.png), [full](screenshots/mobile-join-light-full.png) |


### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| PerimeterX challenge | entry pages | the scripted press&hold solver drives the 'PRESS & HOLD' control automatically and the clearance cookie is kept; it was never answered by hand | solved, not shown |
| UserWay + consent layers | every page | the accessibility widget and any consent layer are hidden before every shot and reading — never clicked, never answered | hidden, never answered |
| Categories drawer | every page header | clicked the 'Sidebar menu' hamburger (a local UI toggle; keyboard Enter is the fallback) | [drawer](#categories-drawer), [home-light-drawer](screenshots/home-light-drawer.png) |
| Filter dropdowns | /search/gigs | clicked a filter trigger (Category, Service Options, Seller Details, Budget, Delivery Time) — a local UI toggle | [filter-btn](#filter-button), [search-light-default](screenshots/search-light-default.png) |
| Package tabs | a gig page | measured at rest — switching a tab re-prices the card, so they were never switched | [pkg-tablist](#package-tabs), [pkg-tab](#package-tab), [gig-light-default](screenshots/gig-light-default.png) |
| FAQ accordions | a gig page, /cp/how-fiverr-works | clicked the question row — a local UI toggle | [faq-acc](#faq-accordion), [hiw-faq](#hiw-faq-accordion), [gig-light-default](screenshots/gig-light-default.png), [how-it-works-light-default](screenshots/how-it-works-light-default.png) |
| Hero search | home | typed into then cleared — the form was never submitted, nothing was searched | [hero-search-input](#hero-search-field), [home-light-default](screenshots/home-light-default.png) |
| Join/login fields | /join and /login | typed into then cleared — nothing sent; Continue-with-* was never pressed | [login-email](#emailusername-field), [login-password](#password-field), [join-field](#join-field), [join-light-default](screenshots/join-light-default.png), [login-light-default](screenshots/login-light-default.png) |
| Signed-in product | a Fiverr account | buyer/seller dashboards, inbox, checkout and every post-login surface needs an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 17 components were given a real keyboard focus. 13 draw an outline ring: `filter-btn` (2px solid #222325 `light.text.primary`, offset 1px), `gig-contact` (2px solid #222325 `light.text.primary`, offset 1px), `tag-chip` (2px solid #222325 `light.text.primary`, offset 4px), `seller-contact` (2px solid #222325 `light.text.primary`, offset 1px), `join-google` (2px solid #222325 `light.text.primary`, offset 1px), `join-apple` (2px solid #222325 `light.text.primary`, offset 1px), `join-email-btn` (3px solid #222325 `light.text.primary`, offset 0px), `login-google` (2px solid #222325 `light.text.primary`, offset 1px), `login-submit` (2px solid #222325 `light.text.primary`, offset 1px), `about-cta` (2px solid #74767e `light.text.faint`, offset 1px), `sell-cta` (2px solid #222325 `light.text.primary`, offset 1px), `sell-cat` (2px solid #000000 `light.action.primary.default`, offset -2px), `m-menu-btn` (2px solid #222325 `light.text.primary`, offset 1px). The other 4 show no measured change: `dir-sub-link`, `related-chip`, `gig-continue`, `lm-cta`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.07s | `cubic-bezier(0.75, 0, 0.25, 1)` | all | about-cta, filter-btn, footer-currency, footer-locale, gig-contact, gig-continue, hero-search-btn, join-apple and more |
| 0.1s | `ease` | background | nav-locale |
| 0.15s | `ease-in-out` | all | hero-search-input, m-search-input |
| 0.2s | `ease` | color | breadcrumb, cat-card, cat-nav, dir-cat-link, dir-sub-link, footer-link, gig-breadcrumb, mkt-logo and more |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Seller card](#seller-card) | 712 x 7475.45 | - | - | transparent | none | 0 |
| [Mobile drawer](#mobile-drawer) | 390 x 5147.25 | - | - | #ffffff `light.surface.card` | none | 0 |
| [Review card](#review-card) | 0 x 0 | - | - | transparent | none | 0px 16px |

## Components

### Site chrome

The sticky header on every public page: the Fiverr wordmark, the Sidebar-menu hamburger that slides in the Browse-categories drawer, Connect to your AI, the EN locale button, Become a Seller, Sign in and the green Join pill; the category strip runs beneath.

#### Site header
The sticky top bar on every public page: the Fiverr wordmark, the Sidebar-menu hamburger, "Connect to your AI", the EN locale button, Become a Seller, Sign in and the green Join pill. Read as `mkt-header` on home.

**Values (default).** size 1425 x 86; background transparent; text Macan 16/24 600, #222325 `light.text.primary`; layers div.search-bar-dim-background 1425.0x0.0 rgb(0, 0, 0); header._188cbt6._bbx8bt 1425.0x86.0 rgb(255, 255, 255) B:1px solid rgb(218, 219, 221); button._arosdn._1xeo152 0.0x0.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 8px; input.long-placeholder 436.2x42.0 rgb(255, 255, 255) T:1px solid rgb(197, 198, 201) / B:1px solid r.

Child layers that carry the look: div 1425x0 background #000000 `light.action.primary.default`; header 1425x86 background #ffffff `light.surface.card` border 1px solid #dadbdd `light.border.hairline`; button 0x0 border 1px solid transparent radius 8px.

![Site header default](components/crops/mkt-header-default.png)

#### Logo
The Fiverr wordmark in the header, linking home. Read as `mkt-logo` on home.

**Values (default).** size 90 x 35; background transparent; text Macan 16/24 400, #222325 `light.text.primary`; transition color 0.2s ease; icon 90 x 28, #222325 `light.text.primary`.

![Logo default](components/crops/mkt-logo-default.png)

#### Sidebar menu button
The header hamburger that opens the Browse-categories drawer — a local UI toggle; the opened state was measured after its own click. Read as `sidebar-btn` on home.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: opened) | size 0 x 0; border 1px solid transparent; radius 8px; background transparent; text Macan 16/24 600, #222325 `light.text.primary`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1) |
| pressed | background #efeff0 `core.color.neutral.press-wash` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Connect to your AI button
The header "Connect to your AI" button (the Fiverr AI-assistant entry); measured, never pressed. Read as `nav-ai` on home.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 242.91 x 42; padding 8px 16px; border 1px solid transparent; radius 8px; background transparent; text Macan 16/24 600, #222325 `light.text.primary`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1); icon 20 x 20, #222325 `light.text.primary` |
| pressed | background #efeff0 `core.color.neutral.press-wash` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Connect to your AI button default](components/crops/nav-ai-default.png) ![Connect to your AI button hover](components/crops/nav-ai-hover.png) ![Connect to your AI button pressed](components/crops/nav-ai-pressed.png)

#### Locale button
The "EN" header button — a local UI toggle for the language list; measured, never toggled. Read as `nav-locale` on home.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 79.91 x 42; padding 8px 16px; border 1px solid transparent; radius 8px; background transparent; text Macan 16/24 600, #222325 `light.text.primary`; transition background 0.1s ease; icon 16 x 16, #222325 `light.text.primary` |
| pressed | background #f5f5f5 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Locale button default](components/crops/nav-locale-default.png) ![Locale button hover](components/crops/nav-locale-hover.png) ![Locale button pressed](components/crops/nav-locale-pressed.png)

#### Become a Seller link
The header "Become a Seller" link to /start_selling; measured, never followed. Read as `nav-seller` on home.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 159 x 42; padding 8px 16px; border 1px solid transparent; radius 8px; background transparent; text Macan 16/24 600, #222325 `light.text.primary`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1) |
| pressed | background #efeff0 `core.color.neutral.press-wash` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Become a Seller link default](components/crops/nav-seller-default.png) ![Become a Seller link hover](components/crops/nav-seller-hover.png) ![Become a Seller link pressed](components/crops/nav-seller-pressed.png)

#### Sign in link
The header "Sign in" link to /login; measured, never followed. Read as `nav-signin` on home.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 85.02 x 42; padding 8px 16px; border 1px solid transparent; radius 8px; background transparent; text Macan 16/24 600, #222325 `light.text.primary`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1) |
| pressed | background #efeff0 `core.color.neutral.press-wash` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Sign in link default](components/crops/nav-signin-default.png) ![Sign in link hover](components/crops/nav-signin-hover.png) ![Sign in link pressed](components/crops/nav-signin-pressed.png)

#### Join CTA
The green "Join" header pill to /join — the primary header action; measured, never followed. Read as `nav-join` on home.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 88 x 42; padding 8px 16px; border 1px solid transparent; radius 8px; background #222325 `light.text.primary`; text Macan 16/24 600, #ffffff `light.surface.card`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1) |
| pressed | background #62646a `light.text.muted` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Join CTA default](components/crops/nav-join-default.png) ![Join CTA hover](components/crops/nav-join-hover.png) ![Join CTA pressed](components/crops/nav-join-pressed.png)

#### Category nav link
A category-strip link under the header (Trending, Graphics & Design, Programming & Tech, …); measured, never followed. Read as `cat-nav` on home.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 142.39 x 0; padding 8px 0px; background transparent; text Macan 16/24 400, #62646a `light.text.muted`; transition color 0.2s ease |
| hover | size 142.39 x 40; text Macan 16/24 400, #74767e `light.text.faint`; layers ::after rgb(29, 191, 115) 0px none 1; a::after 142.391pxx3px rgb(29, 191, 115) |
| pressed | text Macan 16/24 400, #74767e `light.text.faint` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Category nav link default](components/crops/cat-nav-default.png) ![Category nav link hover](components/crops/cat-nav-hover.png) ![Category nav link pressed](components/crops/cat-nav-pressed.png)

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

**Values (default).** size 612.58 x 172.81; background transparent; text Macan 72/86.4 280, #ffffff `light.surface.card`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero search form
The hero search field — the `dark`-skinned pill inside the light page: an input plus its submit button. Read as `hero-search` on home.

**Values (default).** size 1159.94 x 60; background transparent; text Macan 16/24 400, #62646a `light.text.muted`; icon 18 x 18, #ffffff `light.surface.card`; layers input.long-placeholder.vvvkay0 1159.9x60.0 rgb(255, 255, 255) T:1px solid rgb(197, 198, 201) / R:1px solid rgb(197, 198, 201) / B:1px solid rgb(197, 198, 201) / L:1px solid rgb(197, 198, 201) 12px; input.short-placeholder.vvvkay0 0.0x0.0 rgb(255, 255, 255) T:1px solid rgb(197, 198, 201) / R:1px solid rgb(197, 198, 201) / B:1px solid rgb(197, 198, 201) / L:1px solid rgb(197, 198, 201) 12px; button..

Child layers that carry the look: input 1159.9x60 background #ffffff `light.surface.card` border 1px solid #c5c6c9 `light.border.field` radius 12px; input 0x0 background #ffffff `light.surface.card` border 1px solid #c5c6c9 `light.border.field` radius 12px; button 48x48 background #222325 `light.text.primary` border 1px solid transparent radius 8px.

![Hero search form default](components/crops/hero-search-default.png)

#### Hero search field
The "Search for any service" input inside the dark search form; focused and typed into then cleared — never searched. Read as `hero-search-input` on home.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 1159.94 x 60; padding 10px 58px 10px 16px; border 1px solid #c5c6c9 `light.border.field`; radius 12px; background #ffffff `light.surface.card`; text Macan 16/24 400, #62646a `light.text.muted`; transition all 0.15s ease-in-out; placeholder #95979d |

![Hero search field default](components/crops/hero-search-input-default.png) ![Hero search field focused](components/crops/hero-search-input-focused.png) ![Hero search field filled](components/crops/hero-search-input-filled.png)

#### Search submit
The search submit button inside the hero form; its states were measured but it was never clicked — nothing was searched. Read as `hero-search-btn` on home.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 48 x 48; padding 8px 16px; border 1px solid transparent; radius 8px; background #222325 `light.text.primary`; text Macan 14/14 700, #ffffff `light.surface.card`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1); icon 18 x 18, #ffffff `light.surface.card` |
| pressed | background #404145 `light.text.body` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Search submit default](components/crops/hero-search-btn-default.png) ![Search submit hover](components/crops/hero-search-btn-hover.png) ![Search submit pressed](components/crops/hero-search-btn-pressed.png)

#### Popular-service chip
A "Popular services" pill under the hero (Website Development, Logo Design, …); measured, never followed. Read as `popular-chip` on home.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 232.72 x 42; padding 8px 16px; border 1px solid #ffffff `light.surface.card`; radius 8px; background rgba(255, 255, 255, 0.1) `core.color.neutral.on-dark-wash`; text Macan 16/24 400, #ffffff `light.surface.card`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1); icon 13.91 x 16, #ffffff `light.surface.card` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Popular-service chip default](components/crops/popular-chip-default.png) ![Popular-service chip hover](components/crops/popular-chip-hover.png) ![Popular-service chip pressed](components/crops/popular-chip-pressed.png)

#### Category card
A service-category card tile further down the home page; measured, never followed. Read as `cat-card` on home.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 129 x 129; padding 16px 12px; border 1px solid #ffffff `light.surface.card`; radius 16px; background #ffffff `light.surface.card`; shadow rgba(0, 0, 0, 0.027) 0px 0px 0.880517px 0px, rgba(0, 0, 0, 0.03) 0px 0px 2.29197px 0px, rgba(0, 0, 0, 0.055) 0px 0px 5.52px 0px, rgba(0, 0, 0, 0.09) 0px 0px 11px 0px; text Macan 14/22 600, #222325 `light.text.primary`; transition color 0.2s ease; layers ::before rgb(255, 255, 255) 0px none 0 |

![Category card default](components/crops/cat-card-default.png) ![Category card hover](components/crops/cat-card-hover.png)

#### Section heading
A marketing section heading ("Make it all happen with freelancers", …). Read as `section-h2` on home.

**Values (default).** size 720 x 50.41; background transparent; text Macan 48/50.4 400, #404145 `light.text.body`.

![Section heading default](components/crops/section-h2-default.png)

#### Rating badge
A star-rating badge on the page (seller ratings, reviews strip); recorded missing when none renders. Read as `trust-badge` on home.

Not on the page when it was captured.

### Categories and directory

The /categories services directory and the creative-logo-design subcategory hub: mastheads, the category breadcrumb, related-search chips and the directory's category and subcategory links.

#### Directory heading
"Fiverr Gigs® Directory" — the /categories services-directory masthead. Read as `dir-h2` on the categories directory.

**Values (default).** size 988 x 48.41; padding 0px 0px 10px 0px; background transparent; text Macan 32/38.4 700, #404145 `light.text.body`.

![Directory heading default](components/crops/dir-h2-default.png)

#### Directory category link
A top-category link in the services directory; measured, never followed. Read as `dir-cat-link` on the categories directory.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 124.59 x 14; background transparent; text Macan 14/22 400, #222325 `light.text.primary` |
| hover | transition color 0.2s ease |

![Directory category link default](components/crops/dir-cat-link-default.png) ![Directory category link hover](components/crops/dir-cat-link-hover.png)

#### Directory subcategory link
A subcategory link nested under a top category in the directory; measured, never followed. Read as `dir-sub-link` on the categories directory.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 81.72 x 14; background transparent; text Macan 14/28 400, #555555 |
| hover, pressed | text Macan 14/28 400, #1dbf73 `light.action.accent`; transition color 0.2s ease |

![Directory subcategory link default](components/crops/dir-sub-link-default.png) ![Directory subcategory link hover](components/crops/dir-sub-link-hover.png) ![Directory subcategory link focus-visible](components/crops/dir-sub-link-focus-visible.png) ![Directory subcategory link pressed](components/crops/dir-sub-link-pressed.png)

#### Subcategory heading
The subcategory masthead on /categories/graphics-design/creative-logo-design. Read as `sub-h1` on the creative-logo-design subcategory.

**Values (default).** size 1336 x 52; padding 8px 0px; background transparent; text Macan 32/36 700, #222325 `light.text.primary`.

![Subcategory heading default](components/crops/sub-h1-default.png)

#### Breadcrumb link
The category breadcrumb link back up the tree; measured, never followed. Read as `breadcrumb` on the creative-logo-design subcategory.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 142.39 x 40; padding 8px 0px; background transparent; text Macan 16/24 400, #62646a `light.text.muted`; transition color 0.2s ease |
| hover | text Macan 16/24 400, #74767e `light.text.faint`; layers ::after rgb(29, 191, 115) 0px none 1; a::after 142.391pxx3px rgb(29, 191, 115) |

![Breadcrumb link default](components/crops/breadcrumb-default.png) ![Breadcrumb link hover](components/crops/breadcrumb-hover.png)

#### Related-search chip
A related-search/style chip row on the subcategory page; measured, never followed. Read as `related-chip` on the creative-logo-design subcategory.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 185.23 x 80; padding 12px; border 1px solid #e4e5e7; radius 40px; background transparent; text Macan 16/24 600, #222325 `light.text.primary` |
| hover, pressed | border 1px solid #222325 `light.text.primary` |

![Related-search chip default](components/crops/related-chip-default.png) ![Related-search chip hover](components/crops/related-chip-hover.png) ![Related-search chip focus-visible](components/crops/related-chip-focus-visible.png) ![Related-search chip pressed](components/crops/related-chip-pressed.png)

### Search results

/search/gigs results for a public query: the filter dropdown triggers, the sort control, the gig listing cards (thumbnail, seller row, star rating, starting price, collect heart) and the seller-level badges.

#### Results headline
"Results for logo design" — the search-results masthead. Read as `search-h1` on search results.

**Values (default).** size 308.19 x 36; background transparent; text Macan 28/36 400, #222325 `light.text.primary`.

![Results headline default](components/crops/search-h1-default.png)

#### Filter button
A results-filter dropdown trigger (Category, Service Options, Seller Details, Budget, Delivery Time) — a local UI toggle; the opened state was measured after its own click, then closed. Read as `filter-btn` on search results.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 132.86 x 48; padding 10px 20px; border 1px solid #dadbdd `light.border.hairline`; radius 8px; background transparent; text Macan 16/26 600, #222325 `light.text.primary`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1); icon 12 x 12, #222325 `light.text.primary` |
| hover | background #f5f5f5 |
| focus-visible | outline 2px solid #222325 `light.text.primary`, offset 1px |
| pressed | background #efeff0 `core.color.neutral.press-wash` |
| opened | background #f5f5f5 |

![Filter button default](components/crops/filter-btn-default.png) ![Filter button hover](components/crops/filter-btn-hover.png) ![Filter button focus-visible](components/crops/filter-btn-focus-visible.png) ![Filter button pressed](components/crops/filter-btn-pressed.png) ![Filter button opened](components/crops/filter-btn-opened.png)

#### Sort control
The "Sort by" results control; measured at rest, never toggled. Read as `sort-btn` on search results.

Not on the page when it was captured.

#### Gig card
A gig listing card (thumbnail, seller name, rating, starting price, collect heart); measured, never followed. Read as `gig-card` on search results.

Not on the page when it was captured.

#### Collect button
A gig card's heart/collect button; measured, never pressed (a collect would write to an account). Read as `gig-heart` on search results.

Not on the page when it was captured.

#### Card price
The "From S$xx" starting price on a gig card — localized to this client's currency (SGD). Read as `gig-price` on search results.

Not on the page when it was captured.

#### Seller badge
A seller-level badge on a gig card (Top Rated, Level 2, …); recorded at rest. Read as `seller-badge` on search results.

**Values (default).** size 85.66 x 18; background transparent; text Macan 14/18 600, #222325 `light.text.primary`; icon 10 x 10, #222325 `light.text.primary`.

![Seller badge default](components/crops/seller-badge-default.png)

### Gig page

A live gig page (the first card on the results grid): the 'I will …' title, breadcrumb, gallery, the Basic/Standard/Premium package tablist and its price, the Continue and Contact me buttons, the seller card, FAQ accordion rows, reviews and related tags.

#### Gig headline
The gig page's "I will …" title. Read as `gig-h1` on a gig page.

**Values (default).** size 712 x 52; padding 0px 0px 16px 0px; background transparent; text Macan 28/36 700, #222325 `light.text.primary`.

![Gig headline default](components/crops/gig-h1-default.png)

#### Gig breadcrumb
The category breadcrumb on the gig page; measured, never followed. Read as `gig-breadcrumb` on a gig page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 142.39 x 40; padding 8px 0px; background transparent; text Macan 16/24 400, #62646a `light.text.muted`; transition color 0.2s ease |
| hover | text Macan 16/24 400, #74767e `light.text.faint`; layers ::after rgb(29, 191, 115) 0px none 1; a::after 142.391pxx3px rgb(29, 191, 115) |

![Gig breadcrumb default](components/crops/gig-breadcrumb-default.png) ![Gig breadcrumb hover](components/crops/gig-breadcrumb-hover.png)

#### Package tabs
The Basic/Standard/Premium package tablist on the pricing card. Read as `pkg-tablist` on a gig page.

Not on the page when it was captured.

#### Selected package tab
The selected package tab (Basic) in the pricing card. Read as `pkg-tab-on` on a gig page.

**Values (default).** size 137.84 x 59; padding 16px; border R: 1px solid #dadbdd `light.border.hairline`; B: 3px solid #222325 `light.text.primary`; radius 8px 0px 0px 0px; background #ffffff `light.surface.card`; text Macan 16/24 700, #222325 `light.text.primary`.

![Selected package tab default](components/crops/pkg-tab-on-default.png)

#### Package tab
An unselected package tab (Standard/Premium) in the pricing card; measured at rest, never switched (switching re-prices the card). Read as `pkg-tab` on a gig page.

Not on the page when it was captured.

#### Package price
The selected package's price on the pricing card — localized (SGD for this client). Read as `pkg-price` on a gig page.

**Values (default).** size 94.47 x 24; background transparent; text Macan 20/24 400, #222325 `light.text.primary`.

![Package price default](components/crops/pkg-price-default.png)

#### Continue button
The pricing card's green "Continue" button; its states were measured but it was never pressed — it leads to checkout. Read as `gig-continue` on a gig page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 364.55 x 42; padding 12px 24px; border 1px solid transparent; radius 4px; background #000000 `light.action.primary.default`; text Macan 16/16 600, #ffffff `light.surface.card`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1); icon 16 x 16, #ffffff `light.surface.card` |
| hover | background #404145 `light.text.body` |
| pressed | background #222325 `light.text.primary` |

![Continue button default](components/crops/gig-continue-default.png) ![Continue button hover](components/crops/gig-continue-hover.png) ![Continue button focus-visible](components/crops/gig-continue-focus-visible.png) ![Continue button pressed](components/crops/gig-continue-pressed.png)

#### Contact me button
The "Contact me" button beside Continue; measured, never pressed (it fronts a sign-in wall). Read as `gig-contact` on a gig page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 364.55 x 42; padding 8px 16px; border 1px solid #e4e5e7; radius 4px; background transparent; text Macan 16/24 600, #222325 `light.text.primary`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1) |
| hover | background #f5f5f5 |
| focus-visible | outline 2px solid #222325 `light.text.primary`, offset 1px |
| pressed | background #efeff0 `core.color.neutral.press-wash` |

![Contact me button default](components/crops/gig-contact-default.png) ![Contact me button hover](components/crops/gig-contact-hover.png) ![Contact me button focus-visible](components/crops/gig-contact-focus-visible.png) ![Contact me button pressed](components/crops/gig-contact-pressed.png)

#### Seller card
The "Get to know" seller card (avatar, level, rating, location). Read as `seller-card` on a gig page.

**Values (default).** size 712 x 7475.45; background transparent; text Macan 16/24 400, #c5c6c9 `light.border.field`; icon 16 x 16, #222325 `light.text.primary`; layers a._1fe1trbr._1n2vpki5 24.0x24.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 9999px; div.gig-overview 712.0x116.0 rgb(255, 255, 255); figure._1dxiuao1j._1dxiuao14 0.0x0.0 rgb(145, 38, 38) T:1px solid rgb(218, 219, 221) / R:1px solid rgb(218, 219, 221) / B:1px solid rgb(218, 219, 221) / L:1px solid rgb(218, 219, 221) 9999p.

Child layers that carry the look: a 24x24 border 1px solid transparent radius 9999px; div 712x116 background #ffffff `light.surface.card`; figure 0x0 background #912626 border 1px solid #dadbdd `light.border.hairline` radius 9999px.

![Seller card default](components/crops/seller-card-default.png)

#### FAQ accordion
A question row in the gig page's FAQ section; the opened state was measured after clicking it — a local UI toggle. Read as `faq-acc` on a gig page.

Not on the page when it was captured.

#### Review card
A review block in the gig's reviews list (reviewer name, star rating, review text). Read as `review-card` on a gig page.

**Values (default).** size 0 x 0; padding 0px 16px; background transparent; text Macan 16/24 400, #62646a `light.text.muted`; layers div._12d3e3 0.0x0.0 rgb(228, 229, 231) 999px; span._154693.star-progress-shape 0.0x0.0 rgb(34, 35, 37) 999px; div._12d3e3 0.0x0.0 rgb(228, 229, 231) 999px; span._154693.star-progress-shape 0.0x0.0 rgb(34, 35, 37) 999px; div._12d3e3 0.0x0.0 rgb(228, 229, 231) 999px; span._154693.star-progress-shape 0.0x0.0 rgb(34, 35, 37) 999px.

Child layers that carry the look: div 0x0 background #e4e5e7 radius 999px; span 0x0 background #222325 `light.text.primary` radius 999px; div 0x0 background #e4e5e7 radius 999px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Related tag
A related-tag chip under the gig (Related tags); measured, never followed. Read as `tag-chip` on a gig page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 81.72 x 14; background transparent; text Macan 14/24 400, #222325 `light.text.primary`; transition color 0.2s ease |
| focus-visible | outline 2px solid #222325 `light.text.primary`, offset 4px; layers a._1fe1trbk._1fe1trbl 81.7x14.0 2px solid rgb(34, 35, 37) offset 4px |

![Related tag default](components/crops/tag-chip-default.png) ![Related tag hover](components/crops/tag-chip-hover.png) ![Related tag focus-visible](components/crops/tag-chip-focus-visible.png) ![Related tag pressed](components/crops/tag-chip-pressed.png)

### Seller profile

The gig's seller profile: name and headline, Contact me button and the listings grid's gig cards.

#### Seller headline
The seller profile's name/headline. Read as `seller-h1` on a seller profile.

**Values (default).** size 103.19 x 32; background transparent; text Macan 24/32 700, #222325 `light.text.primary`.

![Seller headline default](components/crops/seller-h1-default.png)

#### Profile Contact me
The "Contact me" button on the seller profile; measured, never pressed. Read as `seller-contact` on a seller profile.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 0 x 0; padding 8px 16px; border 1px solid transparent; radius 8px; background #222325 `light.text.primary`; text Macan 16/24 600, #ffffff `light.surface.card`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1) |
| focus-visible | size 149.56 x 42; outline 2px solid #222325 `light.text.primary`, offset 1px; icon 16 x 16, #ffffff `light.surface.card` |
| pressed | size 149.56 x 42; background #62646a `light.text.muted`; icon 16 x 16, #ffffff `light.surface.card` |

![Profile Contact me focus-visible](components/crops/seller-contact-focus-visible.png) ![Profile Contact me pressed](components/crops/seller-contact-pressed.png)

#### Profile gig card
A gig card on the seller profile's listings grid; measured, never followed. Read as `seller-gig-card` on a seller profile.

Not on the page when it was captured.

### Join and sign-in edge

/join and /login — the only account surfaces a signed-out visitor sees: the Continue-with-* SSO buttons and the e-mail/username/password fields, measured as forms and typed into then cleared, never submitted.

#### Join panel
The /join sign-up card — "Create a new account" with the Continue-with-* SSO buttons and the email join path. Read as `join-panel` on join.

Not on the page when it was captured.

#### Google SSO (join)
The "Continue with Google" button on /join; measured, never pressed. Read as `join-google` on join.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 370 x 42; padding 8px 16px; border 1px solid #e4e5e7; radius 8px; background #ffffff `light.surface.card`; text Macan 16/24 600, #222325 `light.text.primary`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1); icon 20 x 20, #222325 `light.text.primary` |
| hover | background #f5f5f5 |
| focus-visible | outline 2px solid #222325 `light.text.primary`, offset 1px |
| pressed | background #efeff0 `core.color.neutral.press-wash` |

![Google SSO (join) default](components/crops/join-google-default.png) ![Google SSO (join) hover](components/crops/join-google-hover.png) ![Google SSO (join) focus-visible](components/crops/join-google-focus-visible.png) ![Google SSO (join) pressed](components/crops/join-google-pressed.png)

#### Apple SSO (join)
The "Continue with Apple" button on /join; measured, never pressed. Read as `join-apple` on join.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 370 x 42; padding 8px 16px; border 1px solid #e4e5e7; radius 8px; background #ffffff `light.surface.card`; text Macan 16/24 600, #222325 `light.text.primary`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1); icon 20 x 20, #222325 `light.text.primary` |
| hover | background #f5f5f5 |
| focus-visible | outline 2px solid #222325 `light.text.primary`, offset 1px |
| pressed | background #efeff0 `core.color.neutral.press-wash` |

![Apple SSO (join) default](components/crops/join-apple-default.png) ![Apple SSO (join) hover](components/crops/join-apple-hover.png) ![Apple SSO (join) focus-visible](components/crops/join-apple-focus-visible.png) ![Apple SSO (join) pressed](components/crops/join-apple-pressed.png)

#### Email join button
The e-mail join button on /join; measured, never pressed. Read as `join-email-btn` on join.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 370 x 42; padding 8px 16px; border 1px solid #e4e5e7; radius 8px; background #ffffff `light.surface.card`; text Macan 16/24 600, #222325 `light.text.primary`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1); icon 20 x 20, #222325 `light.text.primary` |
| hover | background #f5f5f5 |
| focus-visible | outline 3px solid #222325 `light.text.primary`, offset 0px |
| pressed | background #efeff0 `core.color.neutral.press-wash` |

![Email join button default](components/crops/join-email-btn-default.png) ![Email join button hover](components/crops/join-email-btn-hover.png) ![Email join button focus-visible](components/crops/join-email-btn-focus-visible.png) ![Email join button pressed](components/crops/join-email-btn-pressed.png)

#### Join field
A join form field (e-mail/username); focused and typed into then cleared — never submitted. Recorded missing when /join renders SSO-only. Read as `join-field` on join.

Not on the page when it was captured.

#### Login panel
The /login card — "Sign in to your account" with the Continue-with-* SSO buttons and the username/password form. Read as `login-panel` on login.

Not on the page when it was captured.

#### Google SSO (login)
The "Continue with Google" button on /login; measured, never pressed. Read as `login-google` on login.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 370 x 42; padding 8px 16px; border 1px solid #e4e5e7; radius 8px; background #ffffff `light.surface.card`; text Macan 16/24 600, #222325 `light.text.primary`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1); icon 20 x 20, #222325 `light.text.primary` |
| hover | background #f5f5f5 |
| focus-visible | outline 2px solid #222325 `light.text.primary`, offset 1px |
| pressed | background #efeff0 `core.color.neutral.press-wash` |

![Google SSO (login) default](components/crops/login-google-default.png) ![Google SSO (login) hover](components/crops/login-google-hover.png) ![Google SSO (login) focus-visible](components/crops/login-google-focus-visible.png) ![Google SSO (login) pressed](components/crops/login-google-pressed.png)

#### Email/username field
The username-or-e-mail input on the sign-in form; focused and typed into then cleared — never submitted. Read as `login-email` on login.

Not on the page when it was captured.

#### Password field
The password input on the sign-in form; focused and typed into then cleared — never submitted. Read as `login-password` on login.

Not on the page when it was captured.

#### Sign-in submit
The sign-in form's submit button; its states were measured but it was never clicked — nothing was submitted. Read as `login-submit` on login.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 210 x 42; padding 8px 16px; border 1px solid #222325 `light.text.primary`; radius 8px; background transparent; text Macan 16/24 600, #222325 `light.text.primary`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1) |
| focus-visible | outline 2px solid #222325 `light.text.primary`, offset 1px |
| pressed | background #efeff0 `core.color.neutral.press-wash` |

![Sign-in submit default](components/crops/login-submit-default.png) ![Sign-in submit focus-visible](components/crops/login-submit-focus-visible.png) ![Sign-in submit pressed](components/crops/login-submit-pressed.png)

### Logo maker, about and selling

The /logo-maker, /about-us, /start_selling and /cp/how-fiverr-works marketing pages: mastheads, CTAs, steps and FAQ accordions.

#### Logo maker headline
The /logo-maker masthead. Read as `lm-h1` on the logo maker.

**Values (default).** size 499 x 52; padding 0px 0px 20px 0px; background transparent; text Macan 24/32 400, #ffffff `light.surface.card`.

![Logo maker headline default](components/crops/lm-h1-default.png)

#### Logo maker CTA
The logo maker's primary CTA; measured, never followed. Read as `lm-cta` on the logo maker.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 128.34 x 48; padding 15px 24px; border 1px solid transparent; radius 4px; background #ffffff `light.surface.card`; text Macan 16/16 600, #222325 `light.text.primary`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1) |
| hover | text Macan 16/16 600, #404145 `light.text.body` |

![Logo maker CTA default](components/crops/lm-cta-default.png) ![Logo maker CTA hover](components/crops/lm-cta-hover.png) ![Logo maker CTA focus-visible](components/crops/lm-cta-focus-visible.png) ![Logo maker CTA pressed](components/crops/lm-cta-pressed.png)

#### About headline
The /about-us masthead ("ABOUT US" eyebrow, "Making way for breakthroughs"). Read as `about-h1` on about-us.

**Values (default).** size 70.69 x 20; background transparent; text Macan 14/20 600, #ffffff `light.surface.card`.

![About headline default](components/crops/about-h1-default.png)

#### About link
A marketing link on /about-us; measured, never followed. Read as `about-cta` on about-us.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 120.55 x 42; padding 8px 16px; border 1px solid transparent; radius 8px; background #222325 `light.text.primary`; text Macan 16/24 600, #ffffff `light.surface.card`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1) |
| focus-visible | outline 2px solid #74767e `light.text.faint`, offset 1px |

![About link default](components/crops/about-cta-default.png) ![About link hover](components/crops/about-cta-hover.png) ![About link focus-visible](components/crops/about-cta-focus-visible.png) ![About link pressed](components/crops/about-cta-pressed.png)

#### Selling headline
The /start_selling masthead ("Turn your expertise into a global business"). Read as `sell-h1` on start_selling.

**Values (default).** size 572.48 x 160.81; padding 20px 0px 0px 0px; background transparent; text Macan 64/70.4 400, #222325 `light.text.primary`.

![Selling headline default](components/crops/sell-h1-default.png)

#### Seller CTA
The "Create your profile" / "Get started" CTA on /start_selling; measured, never followed. Read as `sell-cta` on start_selling.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 159 x 42; padding 8px 16px; border 1px solid transparent; radius 8px; background transparent; text Macan 16/24 600, #222325 `light.text.primary`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1) |
| hover | background #f5f5f5 |
| focus-visible | outline 2px solid #222325 `light.text.primary`, offset 1px |
| pressed | background #efeff0 `core.color.neutral.press-wash` |

![Seller CTA default](components/crops/sell-cta-default.png) ![Seller CTA hover](components/crops/sell-cta-hover.png) ![Seller CTA focus-visible](components/crops/sell-cta-focus-visible.png) ![Seller CTA pressed](components/crops/sell-cta-pressed.png)

#### Selling category chip
A category chip on the seller landing page; measured, never toggled. Read as `sell-cat` on start_selling.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 206.22 x 41; padding 8px 32px; border B: 1px solid #dadbdd `light.border.hairline`; background transparent; text Macan 16/24 600, #222325 `light.text.primary`; layers button._1gwpigiw._1gwpigik 206.2x41.0 B:1px solid rgb(218, 219, 221) |
| focus-visible | outline 2px solid #000000 `light.action.primary.default`, offset -2px; layers button._1gwpigiw._1gwpigik 206.2x41.0 B:1px solid rgb(218, 219, 221) 2px solid rgb(0, 0, 0) offset -2px |

Child layers that carry the look: button 206.2x41 border 1px solid #dadbdd `light.border.hairline`.

![Selling category chip default](components/crops/sell-cat-default.png) ![Selling category chip hover](components/crops/sell-cat-hover.png) ![Selling category chip focus-visible](components/crops/sell-cat-focus-visible.png) ![Selling category chip pressed](components/crops/sell-cat-pressed.png)

#### How-it-works headline
The /cp/how-fiverr-works masthead. Read as `hiw-h1` on how-fiverr-works.

**Values (default).** size 770 x 64; padding 0px 86px; background transparent; text Macan 18/32 400, #ffffff `light.surface.card`.

![How-it-works headline default](components/crops/hiw-h1-default.png)

#### Steps section
A step block on the how-it-works explainer. Read as `hiw-step` on how-fiverr-works.

**Values (default).** size 1425 x 5583.2; background transparent; text Macan 16/24 600, #222325 `light.text.primary`; layers header._188cbt6._bbx8bt 1425.0x86.0 rgb(255, 255, 255) B:1px solid rgb(218, 219, 221); button._arosdn._1xeo152 0.0x0.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 8px; input.long-placeholder 436.2x42.0 rgb(255, 255, 255) T:1px solid rgb(197, 198, 201) / B:1px solid rgb(197, 198, 201) / L:1px solid rgb(197, 198, 201) 4px .

Child layers that carry the look: header 1425x86 background #ffffff `light.surface.card` border 1px solid #dadbdd `light.border.hairline`; button 0x0 border 1px solid transparent radius 8px; input 436.2x42 background #ffffff `light.surface.card` border 1px solid #c5c6c9 `light.border.field` radius 4px 0px 0px 4px.

![Steps section default](components/crops/hiw-step-default.png)

#### HIW FAQ accordion
A question row in the page's FAQ section; the opened state was measured after clicking it — a local UI toggle. Read as `hiw-faq` on how-fiverr-works.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: opened) | size 1044 x 64; padding 20px 0px; background transparent; text Macan 16/24 400, #404145 `light.text.body`; icon 20 x 20, #74767e `light.text.faint` |

![HIW FAQ accordion default](components/crops/hiw-faq-default.png) ![HIW FAQ accordion opened](components/crops/hiw-faq-opened.png)

### Mobile (390 wide)

The phone surface at 390 wide: the top bar with the hamburger and the categories drawer it opens, the hero and the search field.

#### Mobile top bar
The phone header at 390 wide: the hamburger, the Fiverr wordmark and the Join/sign-in controls. Read as `m-topbar` on home at 390 wide.

**Values (default).** size 390 x 136; background transparent; text Macan 14/19.6 700, #404145 `light.text.body`; icon 50 x 50, #62646a `light.text.muted`; layers div.app-upper-banner.flex 390.0x71.0 rgb(255, 255, 255) B:1px solid rgb(228, 229, 231); button._581729._9de274 104.4x36.0 rgb(29, 191, 115) T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 4px; header._188cbt6._bbx8bt 390.0x65.0 rgb(255, 255, 255) B:1px solid rgb(218, 219, 221); button._arosdn._1xeo152 42.0x42.0 T:1px solid r.

Child layers that carry the look: div 390x71 background #ffffff `light.surface.card` border 1px solid #e4e5e7; button 104.4x36 background #1dbf73 `light.action.accent` border 1px solid transparent radius 4px; header 390x65 background #ffffff `light.surface.card` border 1px solid #dadbdd `light.border.hairline`.

![Mobile top bar default](components/crops/m-topbar-default.png)

#### Mobile menu button
The hamburger that opens the categories drawer — a local UI toggle; the opened state was measured after activating it. Read as `m-menu-btn` on home at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: opened) | size 42 x 42; border 1px solid transparent; radius 8px; background transparent; text Macan 16/24 600, #222325 `light.text.primary`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1); icon 20 x 20, #222325 `light.text.primary` |
| hover | background #f5f5f5 |
| focus-visible | outline 2px solid #222325 `light.text.primary`, offset 1px |
| pressed | background #efeff0 `core.color.neutral.press-wash` |

![Mobile menu button default](components/crops/m-menu-btn-default.png) ![Mobile menu button hover](components/crops/m-menu-btn-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-btn-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-btn-pressed.png) ![Mobile menu button opened](components/crops/m-menu-btn-opened.png)

#### Mobile drawer
The categories drawer open at 390 wide (Browse categories tree plus locale/currency and Join/Sign-in at its foot); its links were never followed. Read as `m-drawer` on home at 390 wide.

**Values (default).** size 390 x 5147.25; background #ffffff `light.surface.card`; text Macan 14/19.6 700, #404145 `light.text.body`; icon 50 x 50, #62646a `light.text.muted`.

![Mobile drawer default](components/crops/m-drawer-default.png)

#### Mobile hero headline
The masthead at 390 wide. Read as `m-hero-h1` on home at 390 wide.

**Values (default).** size 286.34 x 70.41; background transparent; text Macan 32/35.2 280, #ffffff `light.surface.card`.

![Mobile hero headline default](components/crops/m-hero-h1-default.png)

#### Mobile search field
The hero search input at 390 wide (the header search excluded); focused, never searched. Read as `m-search-input` on home at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 293 x 52; padding 10px 48px 10px 16px; border 1px solid #dadbdd `light.border.hairline`; radius 12px; background #ffffff `light.surface.card`; text Macan 16/24 400, #404145 `light.text.body`; transition all 0.15s ease-in-out; placeholder #95979d |
| focused | border 1px solid #95979d |

![Mobile search field default](components/crops/m-search-input-default.png) ![Mobile search field focused](components/crops/m-search-input-focused.png)

### Footer

The page footer: sitemap columns, social icons and the English-language and currency buttons.

#### Footer
The page footer: category sitemap columns, company links, social icons and the language/currency buttons. Read as `footer` on home.

**Values (default).** size 1425 x 751; border 1px solid #dadbdd `light.border.hairline`; background #ffffff `light.surface.card`; text Macan 16/24 600, #222325 `light.text.primary`; icon 90 x 28, #62646a `light.text.muted`.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer sitemap link; measured, never followed. Read as `footer-link` on home.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 53.23 x 14; background transparent; text Macan 14/22 400, #222325 `light.text.primary`; transition color 0.2s ease |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Footer locale button
The "English" button in the footer — a local UI toggle for the locale list; measured, never toggled. Read as `footer-locale` on home.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 97.73 x 36; padding 6px 12px; border 1px solid transparent; radius 8px; background transparent; text Macan 14/22 600, #74767e `light.text.faint`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1); icon 16 x 16, #74767e `light.text.faint` |
| pressed | background #f5f5f5 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Footer locale button default](components/crops/footer-locale-default.png) ![Footer locale button hover](components/crops/footer-locale-hover.png) ![Footer locale button pressed](components/crops/footer-locale-pressed.png)

#### Currency button
The currency button in the footer ("S$ SGD" for this client — prices localize); measured, never toggled. Read as `footer-currency` on home.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 76.91 x 36; padding 6px 12px; border 1px solid transparent; radius 8px; background transparent; text Macan 14/22 600, #74767e `light.text.faint`; transition all 0.07s cubic-bezier(0.75, 0, 0.25, 1) |
| pressed | background #f5f5f5 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Currency button default](components/crops/footer-currency-default.png) ![Currency button hover](components/crops/footer-currency-hover.png) ![Currency button pressed](components/crops/footer-currency-pressed.png)

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

Every public fiverr.com page paints a single light theme: the site's sheets declare ~1,290 custom properties on `:root`, all named by content hash (a token-free layer with no semantic names to alias), and no page carried a dark attribute, class or theme switch while captured. The hero search form's own `dark` class is a component skin inside the light page, measured as a component, not a dark theme.

### Fonts

- **Macan** (self-hosted woff2 under npm-assets.fiverrcdn.com, weights 400/600/700) carries every heading, control and body on the public site, with an Arial-metric fallback; the style guide falls back to system sans.

The capture ran `tools/capture/public/measure.mjs` (component readings), `tools/capture/public/public.mjs` (screenshots), `tools/capture/vars.mjs` (the stylesheet harvest), `tools/capture/public/build-measurements.mjs` (raw/measurements.md) and `tools/build_components_md.py` (this file).

