# FARFETCH components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from farfetch.com on 2026-11-14, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. www.farfetch.com answers Akamai 403 to automation and its CDNs 429, so the DOM is Wayback Machine SSR snapshots served locally and painted by their archived Emotion CSS with scripts removed — nothing was signed into, submitted or bought; hover/focus/pressed states were forced, and the controls hydration owns (size listbox, menus, filter panels, accordions) stay closed rather than faked. Department, product, category and footer links and the account/wishlist/bag icons were measured, never followed; the search and newsletter fields were typed into and cleared, never submitted.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (73 components, 150 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (144 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every page paints `light`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at CSS scale (one CSS pixel per image pixel — mobile fulls are 390 wide); mobile viewport shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home (department chooser) | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Women's listing | `/shopping/women/items.aspx` | [default](screenshots/plp-women-light-default.png), [full](screenshots/plp-women-light-full.png) |
| Men's listing | `/shopping/men/items.aspx` | [default](screenshots/plp-men-light-default.png), [full](screenshots/plp-men-light-full.png) |
| New In edit | `/sets/women/new-in-this-week-eu-women.aspx` | [default](screenshots/set-women-light-default.png), [full](screenshots/set-women-light-full.png) |
| Product detail | `/shopping/women/dolce-gabbana-logo-embossed-cut-out-slides-item-22465526.aspx` | [default](screenshots/pdp-light-default.png), [full](screenshots/pdp-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| Women's listing, phone | `/shopping/women/items.aspx` | [default](screenshots/mobile-plp-women-light-default.png), [full](screenshots/mobile-plp-women-light-full.png) |
| Product detail, phone | `/shopping/women/dolce-gabbana-logo-embossed-cut-out-slides-item-22465526.aspx` | [default](screenshots/mobile-pdp-light-default.png), [full](screenshots/mobile-pdp-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Select size listbox | product detail | hydration-only — the SSR ships the combobox closed and no script runs in the archived copy | resting states only; [size-selector](#size-selector) |
| Department/menu dropdowns | every page | hydration-only — DropdownMenuSelector panels render client-side | triggers measured; [m-dept-menu](#mobile-department-menu) at 390 |
| All Filters panel / sort | new-in edit | hydration-only — its trigger was measured, never toggled | [filter-button](#all-filters-button) |
| Wishlist toggles | cards, product detail | aria-pressed needs hydration; adding to a wishlist needs an account anyway | resting states only; see Gaps |
| Account / wishlist / bag links | the TopBar | measured at rest, never followed — gated | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 19 components were given a real keyboard focus. 19 draw an outline ring: `topbar-dept` (2px solid #101010, offset -2px), `topbar-locale` (2px solid #101010, offset -2px), `topbar-account` (2px solid #101010, offset -2px), `topbar-wishlist` (2px solid #101010, offset -2px), `topbar-bag` (2px solid #101010, offset -2px), `nav-link` (2px solid #101010, offset -2px), `nav-sale` (2px solid #101010, offset -2px), `search-submit` (2px solid #101010, offset -2px), `filter-button` (2px solid #101010, offset -2px), `card-wishlist` (2px solid #101010, offset -2px), `pagination-next` (2px solid #101010, offset -2px), `footer-link` (2px solid #101010, offset -2px), `news-submit` (2px solid #101010, offset 1px), `footer-social` (2px solid #101010, offset -2px), `pdp-brand` (2px solid #101010, offset -2px), `add-to-bag` (2px solid #101010, offset -2px), `pdp-wishlist` (2px solid #101010, offset -2px), `accordion-button` (2px solid #101010, offset -2px), `hero-cta` (2px solid #005fcc, offset -2px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.66, 0, 0.2, 1)` | color, text-decoration, text-decoration-color | footer-link, pdp-brand |
| 0.2s | `ease-in-out` | transform | header, m-header |
| 0.3s | `cubic-bezier(0, 0, 0, 1)` | background-color, border-color, color, opacity | add-to-bag, card-wishlist, carousel-arrow, filter-button, footer-social, hero-cta, m-add-to-bag, news-submit and more |
| 0.3s | `cubic-bezier(0.66, 0, 0.2, 1)` | border-color, box-shadow, opacity | card-sizes, m-search, search-field |
| 0.3s | `ease` | background-color, opacity | topbar-account |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Product card](#product-card) | 321 x 536.98 | - | - | transparent | none | 0 |
| [Editorial card](#editorial-card) | 329.98 x 483.59 | - | - | transparent | none | 0 |
| [Brands module](#brands-module) | 1392 x 722.64 | - | - | transparent | none | 48px 0px 24px 0px |
| [Card skeleton](#card-skeleton) | 288.88 x 501.16 | - | - | transparent | none | 0 |
| [Department tile](#department-tile) | 447.98 x 251.92 | - | - | transparent | none | 0 |
| [Mobile product card](#mobile-product-card) | 173 x 339.64 | - | - | transparent | none | 0 |

## Components

### Header and site chrome

The ~124px top chrome shared by every page: the 44px TopBar row (department links, the 201px FARFETCH wordmark, Language-and-region flag, account, wishlist and bag icons) over the NavBar row (category links, the red Sale link, the 270x44 search field). The TopBar is position:sticky with a 1px #e6e6e6 hairline.

#### Header
The full top chrome: the TopBar (department links, locale flag, account, wishlist, bag) over the NavBar row (wordmark, category links, search field). Read as `header` on the new-in edit page.

**Values (default).** size 1440 x 124; background #ffffff `light.action.ghost-light.active.icon`; text Farfetch Basis 15/19.99 700, #222222 `light.access.private-client.01`; transition transform 0.2s ease-in-out; layers ::after rgba(0, 0, 0, 0) 0px none 0; ancestors div bg #ffffff `light.action.ghost-light.active.icon`.

![Header default](components/crops/header-default.png)

#### Department link
A TopBar department link ("Womenswear" / "Menswear" / "Kidswear"); measured, never followed. Read as `topbar-dept` on the new-in edit page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 121 x 44; padding 10px 12px; border 1px solid rgba(255, 255, 255, 0) `light.action.ghost-dark.active.stroke`; background rgba(255, 255, 255, 0) `light.action.ghost-dark.active.stroke`; text Farfetch Basis 15/19.99 700, #222222 `light.access.private-client.01`; transition background-color 0.3s cubic-bezier(0, 0, 0, 1), border-color 0.3s cubic-bezier(0, 0, 0, 1), opacity 0.3s cubic-bezier(0, 0, 0, 1), color 0.3s cubic-bezier(0, 0, 0, 1) |
| hover | background #f5f5f5 `light.action.ghost-dark.active.surface` |
| focus-visible | outline 2px solid #101010, offset -2px |
| pressed | background #f5f5f5 `light.action.ghost-dark.active.surface`; text Farfetch Basis 15/19.99 700, #727272 `light.action.ghost-dark.active.icon` |

![Department link default](components/crops/topbar-dept-default.png) ![Department link hover](components/crops/topbar-dept-hover.png) ![Department link focus-visible](components/crops/topbar-dept-focus-visible.png) ![Department link pressed](components/crops/topbar-dept-pressed.png)

#### Locale control
The "Language and region" flag IconButtonGhostDark in the TopBar; measured, never toggled (its picker needs hydration). Read as `topbar-locale` on the new-in edit page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 44 x 44; border 1px solid rgba(255, 255, 255, 0) `light.action.ghost-dark.active.stroke`; background rgba(255, 255, 255, 0) `light.action.ghost-dark.active.stroke`; text Farfetch Basis 15/normal 700, #222222 `light.access.private-client.01`; transition background-color 0.3s cubic-bezier(0, 0, 0, 1), border-color 0.3s cubic-bezier(0, 0, 0, 1), opacity 0.3s cubic-bezier(0, 0, 0, 1), color 0.3s cubic-bezier(0, 0, 0, 1); icon 24 x 24, #222222 `light.access.private-client.01` |
| hover | background #f5f5f5 `light.action.ghost-dark.active.surface` |
| focus-visible | outline 2px solid #101010, offset -2px |
| pressed | background #f5f5f5 `light.action.ghost-dark.active.surface`; text Farfetch Basis 15/normal 700, #727272 `light.action.ghost-dark.active.icon`; icon 24 x 24, #727272 `light.action.ghost-dark.active.icon` |

![Locale control default](components/crops/topbar-locale-default.png) ![Locale control hover](components/crops/topbar-locale-hover.png) ![Locale control focus-visible](components/crops/topbar-locale-focus-visible.png) ![Locale control pressed](components/crops/topbar-locale-pressed.png)

#### Account icon
The account/sign-in icon button in the TopBar; measured, never followed. Read as `topbar-account` on the new-in edit page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 44 x 44; border 1px solid rgba(255, 255, 255, 0) `light.action.ghost-dark.active.stroke`; background #f5f5f5 `light.action.ghost-dark.active.surface`; text Farfetch Basis 15/normal 700, transparent; transition background-color 0.3s ease, opacity 0.3s ease; icon 30.86 x 30.86, transparent |
| hover | icon 27.6 x 27.6, transparent |
| focus-visible | outline 2px solid #101010, offset -2px; icon 33.78 x 33.78, transparent |
| pressed | text Farfetch Basis 15/normal 700, #727272 `light.action.ghost-dark.active.icon`; icon 24.99 x 24.99, #727272 `light.action.ghost-dark.active.icon` |

![Account icon default](components/crops/topbar-account-default.png) ![Account icon hover](components/crops/topbar-account-hover.png) ![Account icon focus-visible](components/crops/topbar-account-focus-visible.png) ![Account icon pressed](components/crops/topbar-account-pressed.png)

#### Wishlist icon
The heart icon link to /wishlist (gated); measured, never followed. Read as `topbar-wishlist` on the new-in edit page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 44 x 44; border 1px solid rgba(255, 255, 255, 0) `light.action.ghost-dark.active.stroke`; background rgba(255, 255, 255, 0) `light.action.ghost-dark.active.stroke`; text Farfetch Basis 15/19.99 700, #222222 `light.access.private-client.01`; transition background-color 0.3s cubic-bezier(0, 0, 0, 1), border-color 0.3s cubic-bezier(0, 0, 0, 1), opacity 0.3s cubic-bezier(0, 0, 0, 1), color 0.3s cubic-bezier(0, 0, 0, 1); icon 24 x 24, #222222 `light.access.private-client.01` |
| hover | background #f5f5f5 `light.action.ghost-dark.active.surface` |
| focus-visible | outline 2px solid #101010, offset -2px |
| pressed | background #f5f5f5 `light.action.ghost-dark.active.surface`; text Farfetch Basis 15/19.99 700, #727272 `light.action.ghost-dark.active.icon`; icon 24 x 24, #727272 `light.action.ghost-dark.active.icon` |

![Wishlist icon default](components/crops/topbar-wishlist-default.png) ![Wishlist icon hover](components/crops/topbar-wishlist-hover.png) ![Wishlist icon focus-visible](components/crops/topbar-wishlist-focus-visible.png) ![Wishlist icon pressed](components/crops/topbar-wishlist-pressed.png)

#### Bag icon
The shopping-bag icon link to checkout (gated); measured, never followed. Read as `topbar-bag` on the new-in edit page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 44 x 44; border 1px solid rgba(255, 255, 255, 0) `light.action.ghost-dark.active.stroke`; background rgba(255, 255, 255, 0) `light.action.ghost-dark.active.stroke`; text Farfetch Basis 15/19.99 700, #222222 `light.access.private-client.01`; transition background-color 0.3s cubic-bezier(0, 0, 0, 1), border-color 0.3s cubic-bezier(0, 0, 0, 1), opacity 0.3s cubic-bezier(0, 0, 0, 1), color 0.3s cubic-bezier(0, 0, 0, 1); icon 24 x 24, #222222 `light.access.private-client.01` |
| hover | background #f5f5f5 `light.action.ghost-dark.active.surface` |
| focus-visible | outline 2px solid #101010, offset -2px |
| pressed | background #f5f5f5 `light.action.ghost-dark.active.surface`; text Farfetch Basis 15/19.99 700, #727272 `light.action.ghost-dark.active.icon`; icon 24 x 24, #727272 `light.action.ghost-dark.active.icon` |

![Bag icon default](components/crops/topbar-bag-default.png) ![Bag icon hover](components/crops/topbar-bag-hover.png) ![Bag icon focus-visible](components/crops/topbar-bag-focus-visible.png) ![Bag icon pressed](components/crops/topbar-bag-pressed.png)

#### Wordmark
The FARFETCH wordmark lockup linking home; measured, never followed. Read as `logo` on the new-in edit page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 201 x 24.95; background transparent; text Farfetch Basis 15/19.99 400, #222222 `light.access.private-client.01` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Wordmark default](components/crops/logo-default.png) ![Wordmark hover](components/crops/logo-hover.png) ![Wordmark pressed](components/crops/logo-pressed.png)

#### Category link
A NavBar category link ("Clothing"); measured, never followed. Read as `nav-link` on the new-in edit page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 58 x 19.98; background transparent; text Farfetch Basis 15/19.99 400, #222222 `light.access.private-client.01` |
| focus-visible | outline 2px solid #101010, offset -2px; layers a.ltr-k0ippd.e3owdn51 58.0x20.0 2px solid rgb(16, 16, 16) offset -2px |

![Category link default](components/crops/nav-link-default.png) ![Category link hover](components/crops/nav-link-hover.png) ![Category link focus-visible](components/crops/nav-link-focus-visible.png) ![Category link pressed](components/crops/nav-link-pressed.png)

#### Sale link
The red "Sale" link in the NavBar — the one nav item painted in pos-sales red. Read as `nav-sale` on the new-in edit page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 29 x 19.98; background transparent; text Farfetch Basis 15/19.99 400, #e71d34 `light.content.primary.disabled.sale` |
| focus-visible | outline 2px solid #101010, offset -2px; layers a.ltr-k0ippd.e3owdn51 29.0x20.0 2px solid rgb(16, 16, 16) offset -2px |

![Sale link default](components/crops/nav-sale-default.png) ![Sale link hover](components/crops/nav-sale-hover.png) ![Sale link focus-visible](components/crops/nav-sale-focus-visible.png) ![Sale link pressed](components/crops/nav-sale-pressed.png)

#### Search field
The header "What are you looking for?" search input; focused and typed into then cleared — never submitted. Read as `search-field` on the new-in edit page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 270 x 44; border B: 1px solid #727272 `light.action.ghost-dark.active.icon`; background #ffffff `light.action.ghost-light.active.icon`; text Farfetch Basis 15/19.99 400, #222222 `light.access.private-client.01`; transition box-shadow 0.3s cubic-bezier(0.66, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.66, 0, 0.2, 1); icon 24 x 24, #b6b6b6 `light.action.ghost-dark.disabled.icon` |
| focused, filled | border B: 1px solid #222222 `light.access.private-client.01`; shadow #222222 0px -1px 0px 0px inset |

![Search field default](components/crops/search-field-default.png) ![Search field focused](components/crops/search-field-focused.png) ![Search field filled](components/crops/search-field-filled.png)

#### Search icon button
The search-icon submit inside the header field; measured, never pressed. Read as `search-submit` on the new-in edit page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 32 x 32; border 1px solid rgba(255, 255, 255, 0) `light.action.ghost-dark.active.stroke`; background rgba(255, 255, 255, 0) `light.action.ghost-dark.active.stroke`; text Farfetch Basis 15/normal 700, #b6b6b6 `light.action.ghost-dark.disabled.icon`; transition background-color 0.3s cubic-bezier(0, 0, 0, 1), border-color 0.3s cubic-bezier(0, 0, 0, 1), opacity 0.3s cubic-bezier(0, 0, 0, 1), color 0.3s cubic-bezier(0, 0, 0, 1); icon 24 x 24, #b6b6b6 `light.action.ghost-dark.disabled.icon`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ancestors div.ltr-qfqbf bg #ffffff `light.action.ghost-light.active.icon` shadow transparent 0px -1px 0px 0px inset |
| focus-visible | outline 2px solid #101010, offset -2px; ancestors div.ltr-qfqbf bg #ffffff `light.action.ghost-light.active.icon` shadow #222222 0px -1px 0px 0px inset |

![Search icon button default](components/crops/search-submit-default.png) ![Search icon button hover](components/crops/search-submit-hover.png) ![Search icon button focus-visible](components/crops/search-submit-focus-visible.png) ![Search icon button pressed](components/crops/search-submit-pressed.png)

### Product listing page

The modular women's/men's listing front (/shopping/{women,men}/items.aspx): the 1392px campaign hero modules (DisplayLarge + Editorial dek + Shop Now), the 'Brands of the moment' tile module, the 4-up product-card grid (brand kicker, description, price, wishlist heart) and the editorial-card rail. Breadcrumbs, filters and pagination render after hydration on these pages, so they are gaps here and measured on the edit page instead.

#### Hero module
The content-module hero on the listing front: campaign image, Display title, dek and a "Shop Now" secondary button. Read as `hero-module` on the men's listing page.

**Values (default).** size 1392 x 1007.64; padding 48px 0px; background transparent; text Farfetch Basis 38/48.00 400, #222222 `light.access.private-client.01`; layers a.ltr-i5fx28 106.4x44.0 rgb(255, 255, 255) T:1px solid rgb(34, 34, 34) / R:1px solid rgb(34, 34, 34) / B:1px solid rgb(34, 34, 34) / L:1px solid rgb(34, 34, 34); ancestors div.ltr-wn2fdi bg #ffffff `light.action.ghost-light.active.icon`.

Child layers that carry the look: a 106.4x44 background #ffffff `light.action.ghost-light.active.icon` border 1px solid #222222 `light.access.private-client.01`.

![Hero module default](components/crops/hero-module-default.png)

#### Hero CTA
The "Shop Now" secondary button inside the hero module (white surface, dark stroke); measured, never followed. Read as `hero-cta` on the men's listing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 106.44 x 44; padding 10px 16px; border 1px solid #222222 `light.access.private-client.01`; background #ffffff `light.action.ghost-light.active.icon`; text Farfetch Basis 15/19.99 700, #222222 `light.access.private-client.01`; transition background-color 0.3s cubic-bezier(0, 0, 0, 1), border-color 0.3s cubic-bezier(0, 0, 0, 1), opacity 0.3s cubic-bezier(0, 0, 0, 1), color 0.3s cubic-bezier(0, 0, 0, 1) |
| hover | background #f5f5f5 `light.action.ghost-dark.active.surface` |
| focus-visible | outline 2px solid #005fcc, offset -2px |
| pressed | border 1px solid #727272 `light.action.ghost-dark.active.icon`; background #f5f5f5 `light.action.ghost-dark.active.surface`; text Farfetch Basis 15/19.99 700, #727272 `light.action.ghost-dark.active.icon` |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

### New-in edit page

The 'New In' edit (/sets/women/new-in-this-week-eu-women.aspx) — the classic listing: Breadcrumbs, the PageTitleHeading + collapsible description, the All Filters button, the quick-filter scroller (skeleton until hydration), product cards with size hints and sale pricing, showcase carousels with CarouselArrowSmall controls, and the Pagination row.

#### Breadcrumbs
The category breadcrumb trail (Home > Women > …). Read as `breadcrumb` on the new-in edit page.

**Values (default).** size 1392 x 41; background transparent; text Farfetch Basis 13/17.00 400, #222222 `light.access.private-client.01`; icon 12 x 12, #222222 `light.access.private-client.01`.

![Breadcrumbs default](components/crops/breadcrumb-default.png)

#### Page heading
The listing h1 (PageTitleHeading on the classic listing) or the hero module DisplayLarge title on the modular pages. Read as `page-title` on the new-in edit page.

**Values (default).** size 928 x 38; background transparent; text Farfetch Basis 30/38.00 400, #222222 `light.access.private-client.01`; ancestors div.ltr-1md0mx1 bg rgba(255, 255, 255, 0) `light.action.ghost-dark.active.stroke`.

![Page heading default](components/crops/page-title-default.png)

#### Page description
The collapsible SEO body copy under the page heading. Read as `page-desc` on the new-in edit page.

**Values (default).** size 928 x 39.97; background transparent; text Farfetch Basis 15/19.99 400, #222222 `light.access.private-client.01`.

![Page description default](components/crops/page-desc-default.png)

#### All Filters button
The "All Filters" button in the listing toolbar; measured, never toggled (its panel needs hydration). Read as `filter-button` on the new-in edit page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 129 x 44; padding 10px 44px 10px 16px; border 1px solid #222222 `light.access.private-client.01`; background #ffffff `light.action.ghost-light.active.icon`; text Farfetch Basis 15/19.99 700, #222222 `light.access.private-client.01`; transition background-color 0.3s cubic-bezier(0, 0, 0, 1), border-color 0.3s cubic-bezier(0, 0, 0, 1), opacity 0.3s cubic-bezier(0, 0, 0, 1), color 0.3s cubic-bezier(0, 0, 0, 1); icon 24 x 24, #222222 `light.access.private-client.01`; ancestors div.ltr-1pvugye.e1deumxq0 bg #ffffff `light.action.ghost-light.active.icon` |
| hover | background #f5f5f5 `light.action.ghost-dark.active.surface` |
| focus-visible | outline 2px solid #101010, offset -2px |
| pressed | border 1px solid #727272 `light.action.ghost-dark.active.icon`; background #f5f5f5 `light.action.ghost-dark.active.surface`; text Farfetch Basis 15/19.99 700, #727272 `light.action.ghost-dark.active.icon`; icon 24 x 24, #727272 `light.action.ghost-dark.active.icon` |

![All Filters button default](components/crops/filter-button-default.png) ![All Filters button hover](components/crops/filter-button-hover.png) ![All Filters button focus-visible](components/crops/filter-button-focus-visible.png) ![All Filters button pressed](components/crops/filter-button-pressed.png)

#### Quick filter scroller
The quick-filter chip scroller under the toolbar — the chips are lazy-rendered, so the SSR copy only paints their skeleton bar. Read as `quick-filter` on the new-in edit page.

**Values (default).** size 475 x 44; background transparent; text Farfetch Basis 15/19.99 400, #222222 `light.access.private-client.01`; layers div.ltr-naoiyt 75.0x44.0 rgb(245, 245, 245); div.ltr-naoiyt 80.0x44.0 rgb(245, 245, 245); div.ltr-naoiyt 120.0x44.0 rgb(245, 245, 245); div.ltr-naoiyt 80.0x44.0 rgb(245, 245, 245); div.ltr-naoiyt 90.0x44.0 rgb(245, 245, 245).

Child layers that carry the look: div 75x44 background #f5f5f5 `light.action.ghost-dark.active.surface`; div 80x44 background #f5f5f5 `light.action.ghost-dark.active.surface`; div 120x44 background #f5f5f5 `light.action.ghost-dark.active.surface`.

![Quick filter scroller default](components/crops/quick-filter-default.png)

#### Product card
A listing product card: image, wishlist heart, brand name, description, price. Read as `product-card` on the new-in edit page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 321 x 536.98; background transparent; text Farfetch Basis 13/17.00 400, #727272 `light.action.ghost-dark.active.icon`; icon 24 x 24, #222222 `light.access.private-client.01`; layers div.ltr-mhoyab 321.0x537.0 rgb(255, 255, 255); div::before.ltr-1d9p1fi 281pxx376px rgb(245, 245, 245); div.ltr-1ismw06 321.0x103.0 rgb(255, 255, 255); button.ltr-o7d7sz 44.0x44.0 T:1px solid rgba(255, 255, 255, 0) / R:1px solid rgba(255, 255, 255, 0) / B:1px solid rgba(255, 255, 255, 0) / L:1px solid rgba(255, 255, 255, 0); ancestors ul.ltr-sjsjxu.eoq4d4w0 bg #ffffff `light.action.ghost-light.active.icon` |

Child layers that carry the look: div 321x537 background #ffffff `light.action.ghost-light.active.icon`; div::before 281pxx376px background #f5f5f5 `light.action.ghost-dark.active.surface`; div 321x103 background #ffffff `light.action.ghost-light.active.icon`.

![Product card default](components/crops/product-card-default.png) ![Product card hover](components/crops/product-card-hover.png)

#### Card brand
The brand-name line on a product card. Read as `card-brand` on the new-in edit page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 321 x 19.98; background transparent; text Farfetch Basis 15/19.99 700, #222222 `light.access.private-client.01`; layers ::after rgba(0, 0, 0, 0) 0px none 1 |

![Card brand default](components/crops/card-brand-default.png) ![Card brand hover](components/crops/card-brand-hover.png)

#### Card description
The product description line under the brand. Read as `card-desc` on the new-in edit page.

**Values (default).** size 321 x 17; background transparent; text Farfetch Basis 13/17.00 400, #222222 `light.access.private-client.01`; layers ::after rgba(0, 0, 0, 0) 0px none 1.

![Card description default](components/crops/card-desc-default.png)

#### Card price
The price block on a product card. Read as `card-price` on the new-in edit page.

**Values (default).** size 321 x 25.98; padding 6px 0px 0px 0px; background transparent; text Farfetch Basis 15/19.99 700, #222222 `light.access.private-client.01`.

![Card price default](components/crops/card-price-default.png)

#### Card wishlist heart
The heart icon button floating on the card image (aria-pressed toggle); measured, never toggled — adding to a wishlist needs an account. Read as `card-wishlist` on the new-in edit page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 44 x 44; border 1px solid rgba(255, 255, 255, 0) `light.action.ghost-dark.active.stroke`; background transparent; text Farfetch Basis 15/normal 700, #222222 `light.access.private-client.01`; transition background-color 0.3s cubic-bezier(0, 0, 0, 1), border-color 0.3s cubic-bezier(0, 0, 0, 1), opacity 0.3s cubic-bezier(0, 0, 0, 1), color 0.3s cubic-bezier(0, 0, 0, 1); icon 24 x 24, #222222 `light.access.private-client.01`; ancestors div.ltr-mhoyab bg #ffffff `light.action.ghost-light.active.icon` |
| hover | background #f5f5f5 `light.action.ghost-dark.active.surface` |
| focus-visible | outline 2px solid #101010, offset -2px |
| pressed | background #f5f5f5 `light.action.ghost-dark.active.surface`; text Farfetch Basis 15/normal 700, #727272 `light.action.ghost-dark.active.icon`; icon 24 x 24, #727272 `light.action.ghost-dark.active.icon` |

![Card wishlist heart default](components/crops/card-wishlist-default.png) ![Card wishlist heart hover](components/crops/card-wishlist-hover.png) ![Card wishlist heart focus-visible](components/crops/card-wishlist-focus-visible.png) ![Card wishlist heart pressed](components/crops/card-wishlist-pressed.png)

#### Card size hint
The size-availability hint under a card ("XS S M L" style). Read as `card-sizes` on the new-in edit page.

**Values (default).** size 321 x 102.98; padding 17.0001px 0px 0px 0px; background #ffffff `light.action.ghost-light.active.icon`; text Farfetch Basis 15/19.99 700, #222222 `light.access.private-client.01`; transition opacity 0.3s cubic-bezier(0.66, 0, 0.2, 1); opacity 0.

![Card size hint default](components/crops/card-sizes-default.png)

#### Pagination
The pagination control under the grid ("1 of 3" + next arrow). Read as `pagination` on the new-in edit page.

**Values (default).** size 1392 x 117; padding 48px 0px 0px 0px; background transparent; text Farfetch Basis 15/19.99 400, #222222 `light.access.private-client.01`; icon 24 x 24, #ffffff `light.action.ghost-light.active.icon`; layers hr.ltr-llidud 1392.0x1.0 T:1px solid rgb(230, 230, 230); a.ltr-nlzw0a 93.0x44.0 rgb(34, 34, 34) T:1px solid rgba(255, 255, 255, 0) / R:1px solid rgba(255, 255, 255, 0) / B:1px solid rgba(255, 255, 255, 0) / L:1px solid rgba(255, 255, 255, 0).

Child layers that carry the look: hr 1392x1 border 1px solid #e6e6e6 `light.action.ghost-light.hover.label`; a 93x44 background #222222 `light.access.private-client.01` border 1px solid rgba(255, 255, 255, 0) `light.action.ghost-dark.active.stroke`.

![Pagination default](components/crops/pagination-default.png)

#### Pagination next
The next-page arrow in the pagination control; measured, never followed. Read as `pagination-next` on the new-in edit page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 93 x 44; padding 0px 12px 0px 16px; border 1px solid rgba(255, 255, 255, 0) `light.action.ghost-dark.active.stroke`; background #222222 `light.access.private-client.01`; text Farfetch Basis 15/19.99 700, #ffffff `light.action.ghost-light.active.icon`; transition background-color 0.3s cubic-bezier(0, 0, 0, 1), border-color 0.3s cubic-bezier(0, 0, 0, 1), opacity 0.3s cubic-bezier(0, 0, 0, 1), color 0.3s cubic-bezier(0, 0, 0, 1); icon 24 x 24, #ffffff `light.action.ghost-light.active.icon` |
| hover | background #727272 `light.action.ghost-dark.active.icon` |
| focus-visible | outline 2px solid #101010, offset -2px |
| pressed | background #b6b6b6 `light.action.ghost-dark.disabled.icon` |

![Pagination next default](components/crops/pagination-next-default.png) ![Pagination next hover](components/crops/pagination-next-hover.png) ![Pagination next focus-visible](components/crops/pagination-next-focus-visible.png) ![Pagination next pressed](components/crops/pagination-next-pressed.png)

#### Carousel arrow
A showcase carousel next-arrow (small ghost-dark icon button); measured, never pressed. Read as `carousel-arrow` on the new-in edit page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 32 x 32; border 1px solid #222222 `light.access.private-client.01`; background #ffffff `light.action.ghost-light.active.icon`; text Farfetch Basis 15/normal 700, #222222 `light.access.private-client.01`; transition background-color 0.3s cubic-bezier(0, 0, 0, 1), border-color 0.3s cubic-bezier(0, 0, 0, 1), opacity 0.3s cubic-bezier(0, 0, 0, 1), color 0.3s cubic-bezier(0, 0, 0, 1); icon 24 x 24, #222222 `light.access.private-client.01`; layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| pressed | border 1px solid #727272 `light.action.ghost-dark.active.icon`; background #f5f5f5 `light.action.ghost-dark.active.surface`; text Farfetch Basis 15/normal 700, #727272 `light.action.ghost-dark.active.icon`; icon 24 x 24, #727272 `light.action.ghost-dark.active.icon` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Carousel arrow default](components/crops/carousel-arrow-default.png) ![Carousel arrow hover](components/crops/carousel-arrow-hover.png) ![Carousel arrow pressed](components/crops/carousel-arrow-pressed.png)

#### Brands module
"Brands of the moment" — the premium-brand tile module on the modular listing. Read as `brands-module` on the men's listing page.

**Values (default).** size 1392 x 722.64; padding 48px 0px 24px 0px; background transparent; text Farfetch Basis 22/27.99 400, #222222 `light.access.private-client.01`.

![Brands module default](components/crops/brands-module-default.png)

#### Editorial card
A fashion-feed editorial card on the listing tail. Read as `editorial-card` on the men's listing page.

**Values (default).** size 329.98 x 483.59; background transparent; text Farfetch Basis 15/19.99 400, #222222 `light.access.private-client.01`.

![Editorial card default](components/crops/editorial-card-default.png)

#### Sale price mark
The "-40%" discount footnote on a sale card — content-primary-enabled-sale red (its sibling PriceOriginal strikes through). Read as `sale-price` on the new-in edit page.

**Values (default).** size 33.63 x 17; background transparent; text Farfetch Basis 13/17.00 400, #e71d34 `light.content.primary.disabled.sale`.

![Sale price mark default](components/crops/sale-price-default.png)

#### Original price
The struck-through pre-sale price beside the discount mark on a sale card (grey, line-through). Read as `sale-original` on the new-in edit page.

**Values (default).** size 28.42 x 17; background transparent; text Farfetch Basis 13/17.00 400, #727272 `light.action.ghost-dark.active.icon`; decoration line-through #727272 `light.action.ghost-dark.active.icon`.

![Original price default](components/crops/sale-original-default.png)

### Product detail page

A D&G slides PDP: breadcrumbs, the image carousel with ghost arrows, the ghost-dark brand link, product title, the $345 PriceCallout, the 44px 'Select size' combobox, the square #222 Add To Bag and the Wishlist toggle, then the information accordion and skeletonised related showcases.

#### Breadcrumbs
The PDP breadcrumb trail (Women > Dolce & Gabbana > Shoes > …). Read as `pdp-breadcrumb` on the product detail page.

**Values (default).** size 1392 x 17; background transparent; text Farfetch Basis 13/17.00 400, #222222 `light.access.private-client.01`; icon 12 x 12, #222222 `light.access.private-client.01`.

![Breadcrumbs default](components/crops/pdp-breadcrumb-default.png)

#### Gallery arrow
A gallery next/previous arrow; measured, never pressed. Read as `pdp-arrow` on the product detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 32 x 32; border 1px solid #222222 `light.access.private-client.01`; background #ffffff `light.action.ghost-light.active.icon`; text Farfetch Basis 15/normal 700, #222222 `light.access.private-client.01`; transition background-color 0.3s cubic-bezier(0, 0, 0, 1), border-color 0.3s cubic-bezier(0, 0, 0, 1), opacity 0.3s cubic-bezier(0, 0, 0, 1), color 0.3s cubic-bezier(0, 0, 0, 1); icon 24 x 24, #222222 `light.access.private-client.01`; layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| pressed | border 1px solid #727272 `light.action.ghost-dark.active.icon`; background #f5f5f5 `light.action.ghost-dark.active.surface`; text Farfetch Basis 15/normal 700, #727272 `light.action.ghost-dark.active.icon`; icon 24 x 24, #727272 `light.action.ghost-dark.active.icon` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Gallery arrow default](components/crops/pdp-arrow-default.png) ![Gallery arrow pressed](components/crops/pdp-arrow-pressed.png)

#### Brand link
The "Dolce & Gabbana" ghost-dark brand link over the PDP title; measured, never followed. Read as `pdp-brand` on the product detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 175 x 27.98; background transparent; text Farfetch Basis 22/27.99 400, #222222 `light.access.private-client.01`; transition color 0.15s cubic-bezier(0.66, 0, 0.2, 1), text-decoration 0.15s cubic-bezier(0.66, 0, 0.2, 1) |
| hover | decoration underline #222222 `light.access.private-client.01` |
| focus-visible | outline 2px solid #101010, offset -2px; transition color 0.15s cubic-bezier(0.66, 0, 0.2, 1); layers a.ltr-1rkeqir-Body-Heading.e1h8dali1 175.0x28.0 2px solid rgb(16, 16, 16) offset -2px |
| pressed | decoration underline #222222 `light.access.private-client.01` |

![Brand link default](components/crops/pdp-brand-default.png) ![Brand link hover](components/crops/pdp-brand-hover.png) ![Brand link focus-visible](components/crops/pdp-brand-focus-visible.png) ![Brand link pressed](components/crops/pdp-brand-pressed.png)

#### Product title
The product description heading ("logo-embossed cut-out slides"). Read as `pdp-title` on the product detail page.

**Values (default).** size 452 x 47.97; background transparent; text Farfetch Basis 22/27.99 400, #222222 `light.access.private-client.01`.

![Product title default](components/crops/pdp-title-default.png)

#### Price callout
The "$345" price callout above the size selector. Read as `pdp-price` on the product detail page.

**Values (default).** size 452 x 19.98; background transparent; text Farfetch Basis 15/19.99 400, #222222 `light.access.private-client.01`.

![Price callout default](components/crops/pdp-price-default.png)

#### Size selector
The "Select size" combobox (44px outlined field, chevron). Its listbox is hydration-rendered, so no opened state exists in the static copy. Read as `size-selector` on the product detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 452 x 44; background transparent; text Farfetch Basis 15/19.99 400, #727272 `light.action.ghost-dark.active.icon`; icon 24 x 24, #222222 `light.access.private-client.01`; layers div.ltr-cubnbt 452.0x44.0 rgb(255, 255, 255) T:1px solid rgb(114, 114, 114) / R:1px solid rgb(114, 114, 114) / B:1px solid rgb(114, 114, 114) / L:1px solid rgb(114, 114, 114) |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: div 452x44 background #ffffff `light.action.ghost-light.active.icon` border 1px solid #727272 `light.action.ghost-dark.active.icon`.

![Size selector default](components/crops/size-selector-default.png) ![Size selector hover](components/crops/size-selector-hover.png) ![Size selector pressed](components/crops/size-selector-pressed.png)

#### Add To Bag
The primary "Add To Bag" button — actions-primary dark surface; measured, never pressed. Read as `add-to-bag` on the product detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 322 x 44; padding 10px 16px; border 1px solid rgba(255, 255, 255, 0) `light.action.ghost-dark.active.stroke`; background #222222 `light.access.private-client.01`; text Farfetch Basis 15/19.99 700, #ffffff `light.action.ghost-light.active.icon`; transition background-color 0.3s cubic-bezier(0, 0, 0, 1), border-color 0.3s cubic-bezier(0, 0, 0, 1), opacity 0.3s cubic-bezier(0, 0, 0, 1), color 0.3s cubic-bezier(0, 0, 0, 1) |
| hover | background #727272 `light.action.ghost-dark.active.icon` |
| focus-visible | outline 2px solid #101010, offset -2px |
| pressed | background #959595 |

![Add To Bag default](components/crops/add-to-bag-default.png) ![Add To Bag hover](components/crops/add-to-bag-hover.png) ![Add To Bag focus-visible](components/crops/add-to-bag-focus-visible.png) ![Add To Bag pressed](components/crops/add-to-bag-pressed.png)

#### PDP wishlist
The "Wishlist" secondary action beside Add To Bag (aria-pressed toggle); measured, never toggled. Read as `pdp-wishlist` on the product detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 118 x 44; padding 10px 44px 10px 16px; border 1px solid #222222 `light.access.private-client.01`; background #ffffff `light.action.ghost-light.active.icon`; text Farfetch Basis 15/19.99 700, #222222 `light.access.private-client.01`; transition background-color 0.3s cubic-bezier(0, 0, 0, 1), border-color 0.3s cubic-bezier(0, 0, 0, 1), opacity 0.3s cubic-bezier(0, 0, 0, 1), color 0.3s cubic-bezier(0, 0, 0, 1); icon 24 x 24, #222222 `light.access.private-client.01` |
| focus-visible | outline 2px solid #101010, offset -2px |

![PDP wishlist default](components/crops/pdp-wishlist-default.png) ![PDP wishlist hover](components/crops/pdp-wishlist-hover.png) ![PDP wishlist focus-visible](components/crops/pdp-wishlist-focus-visible.png) ![PDP wishlist pressed](components/crops/pdp-wishlist-pressed.png)

#### Info accordion
"The Details / Composition / FARFETCH ID" accordion under the buy box. Read as `pdp-accordion` on the product detail page.

**Values (default).** size 1392 x 484.78; background transparent; text Farfetch Basis 15/19.99 400, #222222 `light.access.private-client.01`; icon 24 x 24, #222222 `light.access.private-client.01`; layers section.ltr-t80gkb 1392.0x472.8 B:1px solid rgb(230, 230, 230).

Child layers that carry the look: section 1392x472.8 border 1px solid #e6e6e6 `light.action.ghost-light.hover.label`.

![Info accordion default](components/crops/pdp-accordion-default.png)

#### Accordion section
One accordion section (SSR ships the first panel expanded). Read as `accordion-item` on the product detail page.

**Values (default).** size 1392 x 472.78; border B: 1px solid #e6e6e6 `light.action.ghost-light.hover.label`; background transparent; text Farfetch Basis 15/19.99 400, #222222 `light.access.private-client.01`; icon 24 x 24, #222222 `light.access.private-client.01`; layers section.ltr-t80gkb 1392.0x472.8 B:1px solid rgb(230, 230, 230).

Child layers that carry the look: section 1392x472.8 border 1px solid #e6e6e6 `light.action.ghost-light.hover.label`.

![Accordion section default](components/crops/accordion-item-default.png)

#### Accordion toggle
An accordion section toggle; measured, never toggled (panels need hydration). Read as `accordion-button` on the product detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 1392 x 44; background transparent; text Farfetch Basis 15/19.99 400, #222222 `light.access.private-client.01`; icon 24 x 24, #222222 `light.access.private-client.01` |
| focus-visible | outline 2px solid #101010, offset -2px; layers button.ltr-g3vsg 1392.0x44.0 2px solid rgb(16, 16, 16) offset -2px |

![Accordion toggle default](components/crops/accordion-button-default.png) ![Accordion toggle hover](components/crops/accordion-button-hover.png) ![Accordion toggle focus-visible](components/crops/accordion-button-focus-visible.png) ![Accordion toggle pressed](components/crops/accordion-button-pressed.png)

#### Card skeleton
A product-card loading skeleton in the related-products showcase (the showcase grid ships skeletonised in SSR). Read as `skeleton-card` on the product detail page.

**Values (default).** size 288.88 x 501.16; background transparent; text Farfetch Basis 15/19.99 400, #222222 `light.access.private-client.01`; layers div.ltr-q6lfkw 288.9x385.2 rgb(245, 245, 245); div.ltr-7yf7ta 202.2x22.0 rgb(245, 245, 245); div.ltr-7yf7ta 260.0x22.0 rgb(245, 245, 245); div.ltr-7yf7ta 144.4x22.0 rgb(245, 245, 245).

Child layers that carry the look: div 288.9x385.2 background #f5f5f5 `light.action.ghost-dark.active.surface`; div 202.2x22 background #f5f5f5 `light.action.ghost-dark.active.surface`; div 260x22 background #f5f5f5 `light.action.ghost-dark.active.surface`.

![Card skeleton default](components/crops/skeleton-card-default.png)

#### Showcase skeleton
A related-products showcase in its SSR loading state. Read as `skeleton-showcase` on the product detail page.

**Values (default).** size 1392 x 573.14; background transparent; text Farfetch Basis 15/19.99 400, #222222 `light.access.private-client.01`; icon 24 x 24, #222222 `light.access.private-client.01`; layers div.ltr-vqy38v-TitleSkeleton 487.2x28.0 rgb(245, 245, 245) B:2px solid rgb(255, 255, 255); div.ltr-q6lfkw 288.9x385.2 rgb(245, 245, 245); div.ltr-7yf7ta 202.2x22.0 rgb(245, 245, 245); div.ltr-7yf7ta 260.0x22.0 rgb(245, 245, 245); div.ltr-7yf7ta 144.4x22.0 rgb(245, 245, 245); div.ltr-q6lfkw 288.9x385.2 rgb(245, 245, 245).

Child layers that carry the look: div 487.2x28 background #f5f5f5 `light.action.ghost-dark.active.surface` border 2px solid #ffffff `light.action.ghost-light.active.icon`; div 288.9x385.2 background #f5f5f5 `light.action.ghost-dark.active.surface`; div 202.2x22 background #f5f5f5 `light.action.ghost-dark.active.surface`.

![Showcase skeleton default](components/crops/skeleton-showcase-default.png)

#### Image gallery
The PDP product-photo column (the stacked product shots left of the buy box; its arrow controls need hydration). Read as `pdp-gallery` on the product detail page.

**Values (default).** size 904 x 1201.31; background transparent; text Farfetch Basis 15/19.99 400, #222222 `light.access.private-client.01`.

![Image gallery default](components/crops/pdp-gallery-default.png)

#### Variant tabs
Colour/variant tabs in the variant selector. The archived PDP renders only the size combobox there, so none exist to measure. Read as `variant-tabs` on the product detail page.

Not on the page when it was captured.

### Home (department chooser)

The country landing: 'Choose a department' over three full-bleed tiles (WOMENSWEAR/MENSWEAR/KIDSWEAR with Display overlays), per-department rows of Kicker-labelled category cards, then the newsletter and footer (the archived home paints no editorial feed).

#### Chooser heading
"Choose a department" — the Title heading over the three department tiles. Read as `dept-heading` on the home page.

**Values (default).** size 928 x 27.98; background transparent; text Farfetch Basis 22/27.99 400, #222222 `light.access.private-client.01`.

![Chooser heading default](components/crops/dept-heading-default.png)

#### Department tile
A department chooser tile — full-bleed image with the department Display name overlaid; measured, never followed. Read as `dept-tile` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 447.98 x 251.92; background transparent; text Farfetch Basis 30/38.00 400, #ffffff `light.action.ghost-light.active.icon`; layers div::before._eb25ab._f6155d 447.984pxx251.922px |

Child layers that carry the look: div::before 447.984pxx251.922px image linear-gradient(rgba(34, 34, 34, 0), rgba(34, 34, 34, 0.82)).

![Department tile default](components/crops/dept-tile-default.png) ![Department tile hover](components/crops/dept-tile-hover.png)

#### Category kicker
The Kicker heading ("Clothing") over a category card in a department column; the card around it is the link, the heading itself is not interactive. Read as `dept-kicker` on the home page.

**Values (default).** size 329.98 x 19.98; background transparent; text Farfetch Basis 15/19.99 400, #222222 `light.access.private-client.01`.

![Category kicker default](components/crops/dept-kicker-default.png)

#### Category card
A department-column category card (image with a Kicker label, e.g. NEW IN); measured, never followed. Read as `home-category-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 329.98 x 483.59; background transparent; text Farfetch Basis 15/19.99 400, #222222 `light.access.private-client.01` |

![Category card default](components/crops/home-category-card-default.png) ![Category card hover](components/crops/home-category-card-hover.png)

#### Editorial card
A fashion-feed editorial card on the home tail. The archived home paints only department and category cards, so no feed card exists to measure (the listing pages carry the editorial-card component). Read as `home-editorial` on the home page.

Not on the page when it was captured.

### Type specimens

The pulse type roles measured where they paint on the pages (DisplayLarge, Display, Title, Kicker, Body, Footnote, Label, Editorial).

#### Display
A --typography-display / display-large specimen. Read as `type-display` on the women's listing page.

**Values (default).** size 588 x 48; background transparent; text Farfetch Basis 38/48.00 400, #222222 `light.access.private-client.01`.

![Display default](components/crops/type-display-default.png)

#### Kicker
The uppercase --typography-kicker over a heading. Read as `type-kicker` on the women's listing page.

**Values (default).** size 329.98 x 19.98; background transparent; text Farfetch Basis 15/19.99 400, #222222 `light.access.private-client.01`.

![Kicker default](components/crops/type-kicker-default.png)

#### Footnote
The --typography-footnote micro-label. Read as `type-footnote` on the women's listing page.

**Values (default).** size 1392 x 17; background transparent; text Farfetch Basis 13/17.00 400, #222222 `light.access.private-client.01`.

![Footnote default](components/crops/type-footnote-default.png)

#### Label
A small label style (LabelPrimarySmall). Read as `type-label` on the women's listing page.

**Values (default).** size 336 x 17; background transparent; text Farfetch Basis 13/17.00 400, #727272 `light.action.ghost-dark.active.icon`.

![Label default](components/crops/type-label-default.png)

#### Editorial
The Nimbus Roman D --typography-editorial serif. Read as `type-editorial` on the women's listing page.

**Values (default).** size 588 x 48; background transparent; text Nimbus Roman D 20/24 400, #222222 `light.access.private-client.01`.

![Editorial default](components/crops/type-editorial-default.png)

#### Title
A --typography-title specimen. Read as `type-title` on the women's listing page.

**Values (default).** size 928 x 27.98; background transparent; text Farfetch Basis 22/27.99 400, #222222 `light.access.private-client.01`.

![Title default](components/crops/type-title-default.png)

#### Body
A --typography-body specimen. Read as `type-body` on the women's listing page.

**Values (default).** size 684 x 19.98; background transparent; text Farfetch Basis 15/19.99 400, #222222 `light.access.private-client.01`.

![Body default](components/crops/type-body-default.png)

### Footer

The site footer: section-title columns of links, the 'Get updates by Email' field + 90px Sign Up button, the social IconButtonGhostDark row and the legal line.

#### Footer
The site footer: link columns, newsletter sign-up, socials, locale/legal line. Read as `footer` on the new-in edit page.

**Values (default).** size 1440 x 508.97; background #ffffff `light.action.ghost-light.active.icon`; text Farfetch Basis 15/19.99 700, #222222 `light.access.private-client.01`; icon 24 x 24, #222222 `light.access.private-client.01`; ancestors div bg #ffffff `light.action.ghost-light.active.icon`.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer column link; measured, never followed. Read as `footer-link` on the new-in edit page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 330 x 34; padding 6px 0px; background transparent; text Farfetch Basis 15/19.99 400, #222222 `light.access.private-client.01`; decoration underline transparent; transition text-decoration-color 0.15s cubic-bezier(0.66, 0, 0.2, 1) |
| hover | decoration underline #222222 `light.access.private-client.01` |
| focus-visible | outline 2px solid #101010, offset -2px; decoration underline #222222 `light.access.private-client.01`; layers a.ltr-o5fwqn 330.0x34.0 2px solid rgb(16, 16, 16) offset -2px |
| pressed | decoration underline #222222 `light.access.private-client.01` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Footer column heading
A footer column heading (small caps label). Read as `footer-heading` on the new-in edit page.

**Values (default).** size 330 x 19.98; background transparent; text Farfetch Basis 15/19.99 700, #222222 `light.access.private-client.01`.

![Footer column heading default](components/crops/footer-heading-default.png)

#### Newsletter field
The footer "Get updates by Email" field; focused and typed into then cleared — never submitted. Read as `news-field` on the new-in edit page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 300 x 42; padding 0px 0px 0px 16px; background #ffffff `light.action.ghost-light.active.icon`; text Farfetch Basis 15/19.99 400, #222222 `light.access.private-client.01`; placeholder #727272 `light.action.ghost-dark.active.icon`; ancestors div.ltr-6xvdur bg #ffffff `light.action.ghost-light.active.icon` |
| focused, filled | ancestors div.ltr-6xvdur bg #ffffff `light.action.ghost-light.active.icon` outline 2px solid #101010 |

![Newsletter field default](components/crops/news-field-default.png) ![Newsletter field focused](components/crops/news-field-focused.png) ![Newsletter field filled](components/crops/news-field-filled.png)

#### Sign Up button
The "Sign Up" newsletter button; measured, never pressed. Read as `news-submit` on the new-in edit page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 90 x 44; padding 10px 16px; border 1px solid rgba(255, 255, 255, 0) `light.action.ghost-dark.active.stroke`; background #222222 `light.access.private-client.01`; text Farfetch Basis 15/19.99 700, #ffffff `light.action.ghost-light.active.icon`; transition background-color 0.3s cubic-bezier(0, 0, 0, 1), border-color 0.3s cubic-bezier(0, 0, 0, 1), opacity 0.3s cubic-bezier(0, 0, 0, 1), color 0.3s cubic-bezier(0, 0, 0, 1) |
| hover | background #727272 `light.action.ghost-dark.active.icon` |
| focus-visible | outline 2px solid #101010, offset 1px |
| pressed | background #b6b6b6 `light.action.ghost-dark.disabled.icon` |

![Sign Up button default](components/crops/news-submit-default.png) ![Sign Up button hover](components/crops/news-submit-hover.png) ![Sign Up button focus-visible](components/crops/news-submit-focus-visible.png) ![Sign Up button pressed](components/crops/news-submit-pressed.png)

#### Social icon link
A social icon link in the footer; measured, never followed. Read as `footer-social` on the new-in edit page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 44 x 44; border 1px solid rgba(255, 255, 255, 0) `light.action.ghost-dark.active.stroke`; background rgba(255, 255, 255, 0) `light.action.ghost-dark.active.stroke`; text Farfetch Basis 15/19.99 700, #222222 `light.access.private-client.01`; transition background-color 0.3s cubic-bezier(0, 0, 0, 1), border-color 0.3s cubic-bezier(0, 0, 0, 1), opacity 0.3s cubic-bezier(0, 0, 0, 1), color 0.3s cubic-bezier(0, 0, 0, 1); icon 24 x 24, #222222 `light.access.private-client.01` |
| hover | background #f5f5f5 `light.action.ghost-dark.active.surface` |
| focus-visible | outline 2px solid #101010, offset -2px |
| pressed | background #f5f5f5 `light.action.ghost-dark.active.surface`; text Farfetch Basis 15/19.99 700, #727272 `light.action.ghost-dark.active.icon`; icon 24 x 24, #727272 `light.action.ghost-dark.active.icon` |

![Social icon link default](components/crops/footer-social-default.png) ![Social icon link hover](components/crops/footer-social-hover.png) ![Social icon link focus-visible](components/crops/footer-social-focus-visible.png) ![Social icon link pressed](components/crops/footer-social-pressed.png)

### Mobile (390 wide)

The pages at phone width: the TopBar collapses the departments into the DropdownMenuSelector trigger; the NavBar row and buy box re-stack (the archived SSR paints the desktop chrome responsively — the hamburger itself needs hydration).

#### Mobile header
The top chrome at 390: department links, wordmark, locale/account/wishlist/bag icons (the SSR markup paints the desktop chrome responsively; the hamburger needs hydration). Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 100; background #ffffff `light.action.ghost-light.active.icon`; text Farfetch Basis 15/19.99 700, #222222 `light.access.private-client.01`; transition transform 0.2s ease-in-out; icon 24 x 24, #222222 `light.access.private-client.01`; layers ::after rgba(0, 0, 0, 0) 0px none 0; ancestors div bg #ffffff `light.action.ghost-light.active.icon`.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile department menu
The "departments" DropdownMenuSelectorUncontrolled in the TopBar — visible only below 60em; measured, never toggled. Read as `m-dept-menu` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 62 x 44; background transparent; text Farfetch Basis 15/19.99 700, #222222 `light.access.private-client.01`; icon 24 x 24, #222222 `light.access.private-client.01`; layers button.ey6fkr80.ltr-1iz9vsw 215.0x44.0 rgba(255, 255, 255, 0) T:1px solid rgba(255, 255, 255, 0) / R:1px solid rgba(255, 255, 255, 0) / B:1px solid rgba(255, 255, 255, 0) / L:1px solid rgba(255, 255, 255, 0) |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: button 215x44 background rgba(255, 255, 255, 0) `light.action.ghost-dark.active.stroke` border 1px solid rgba(255, 255, 255, 0) `light.action.ghost-dark.active.stroke`.

![Mobile department menu default](components/crops/m-dept-menu-default.png) ![Mobile department menu hover](components/crops/m-dept-menu-hover.png) ![Mobile department menu pressed](components/crops/m-dept-menu-pressed.png)

#### Mobile search field
The search input at phone width. Read as `m-search` on the home page at 390 wide.

**Values (default).** size 270 x 44; border B: 1px solid #727272 `light.action.ghost-dark.active.icon`; background #ffffff `light.action.ghost-light.active.icon`; text Farfetch Basis 15/19.99 400, #222222 `light.access.private-client.01`; transition box-shadow 0.3s cubic-bezier(0.66, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.66, 0, 0.2, 1); icon 24 x 24, #b6b6b6 `light.action.ghost-dark.disabled.icon`.

![Mobile search field default](components/crops/m-search-default.png)

#### Mobile wordmark
The FARFETCH wordmark at phone width. Read as `m-logo` on the home page at 390 wide.

**Values (default).** size 124 x 15.39; background transparent; text Farfetch Basis 15/19.99 400, #222222 `light.access.private-client.01`.

![Mobile wordmark default](components/crops/m-logo-default.png)

#### Mobile Add To Bag
The primary buy button at phone width. Read as `m-add-to-bag` on the product detail page at 390 wide.

**Values (default).** size 84.5 x 61.97; padding 10px 16px; border 1px solid rgba(255, 255, 255, 0) `light.action.ghost-dark.active.stroke`; background #222222 `light.access.private-client.01`; text Farfetch Basis 15/19.99 700, #ffffff `light.action.ghost-light.active.icon`; transition background-color 0.3s cubic-bezier(0, 0, 0, 1), border-color 0.3s cubic-bezier(0, 0, 0, 1), opacity 0.3s cubic-bezier(0, 0, 0, 1), color 0.3s cubic-bezier(0, 0, 0, 1).

![Mobile Add To Bag default](components/crops/m-add-to-bag-default.png)

#### Mobile size selector
The "Select size" combobox at phone width. Read as `m-size-selector` on the product detail page at 390 wide.

**Values (default).** size 142.5 x 44; background transparent; text Farfetch Basis 15/19.99 400, #727272 `light.action.ghost-dark.active.icon`; icon 24 x 24, #222222 `light.access.private-client.01`; layers div.ltr-cubnbt 142.5x44.0 rgb(255, 255, 255) T:1px solid rgb(114, 114, 114) / R:1px solid rgb(114, 114, 114) / B:1px solid rgb(114, 114, 114) / L:1px solid rgb(114, 114, 114).

Child layers that carry the look: div 142.5x44 background #ffffff `light.action.ghost-light.active.icon` border 1px solid #727272 `light.action.ghost-dark.active.icon`.

![Mobile size selector default](components/crops/m-size-selector-default.png)

#### Mobile department tile
A department chooser tile at phone width. Read as `m-dept-tile` on the home page at 390 wide.

**Values (default).** size 260 x 146.25; background transparent; text Farfetch Basis 30/38.00 400, #ffffff `light.action.ghost-light.active.icon`; layers div::before._eb25ab._f6155d 260pxx146.25px.

Child layers that carry the look: div::before 260pxx146.25px image linear-gradient(rgba(34, 34, 34, 0), rgba(34, 34, 34, 0.82)).

![Mobile department tile default](components/crops/m-dept-tile-default.png)

#### Mobile product card
A listing product card at phone width. Read as `m-product-card` on the women's listing page at 390 wide.

**Values (default).** size 173 x 339.64; background transparent; text Farfetch Basis 13/17.00 400, #727272 `light.action.ghost-dark.active.icon`; icon 24 x 24, #222222 `light.access.private-client.01`; layers div.ltr-mhoyab 173.0x339.6 rgb(255, 255, 255); div::before.ltr-1d9p1fi 133pxx178.656px rgb(245, 245, 245); button.ltr-o7d7sz 44.0x44.0 T:1px solid rgba(255, 255, 255, 0) / R:1px solid rgba(255, 255, 255, 0) / B:1px solid rgba(255, 255, 255, 0) / L:1px solid rgba(255, 255, 255, 0).

Child layers that carry the look: div 173x339.6 background #ffffff `light.action.ghost-light.active.icon`; div::before 133pxx178.656px background #f5f5f5 `light.action.ghost-dark.active.surface`; button 44x44 border 1px solid rgba(255, 255, 255, 0) `light.action.ghost-dark.active.stroke`.

![Mobile product card default](components/crops/m-product-card-default.png)

#### Mobile filter button
The All Filters control at phone width (plp modular page renders it post-hydration). Read as `m-filter` on the women's listing page at 390 wide.

Not on the page when it was captured.

## Icons

No standalone SVG icon set was lifted on this pass; the glyphs in the crops and screenshots (the wordmark, the social icons, the #iconLoaded-* sprite symbols the Emotion markup references) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Members and external destinations

FARFETCH has a signed-in product — account, wishlist, bag, checkout, FARFETCH Access loyalty, order tracking and private-client surfaces — that lives behind the Login page link and was never opened. The account, wishlist and bag TopBar icons, every product/brand/category/footer link and the social icons were measured, never followed; nothing was added to a bag or wishlist and no form was submitted.

### Pages

- **Live farfetch.com is unreachable to automation** — Akamai answers 403 on www.farfetch.com and 429 on both farfetch-contents.com CDNs, headless and headed alike. The DOM evidence is Wayback Machine SSR snapshots (home 2026-10-16, listings 2026-08, PDP 2025-12-17) served locally; the CSS, fonts and product images are their own archived assets fetched through web.archive.org and mirrored under scratch. The markup is archived, not current live markup.
- **Scripts were stripped** from the archived pages, so everything hydration owns — the Select size listbox, the department/menu dropdown panels, the All Filters drawer, sort, accordion animation, carousel scrolling, wishlist aria-pressed — stays closed. Those resting controls were measured; their opened states are recorded as a boundary, not faked.
- **The modular PLPs (women/men) render their breadcrumb, filter bar and pagination client-side**, so those components were measured on the classic 'New In' edit page instead and read as missing on the modular pages.
- **Skeletons.** The modular pages ship TopBanner skeleton bars and the PDP ships skeletonised related-product showcases; they are measured as the loading states they are.
- **Checkout, account, wishlist, bag, sign-in** — all gated; the icons and links were measured at rest and the destinations are boundaries.
- **Search, designers, sale, help surfaces** — no usable Wayback snapshot was found for these routes inside this pass; search results, the designers index and Help/FAQ reuse the listing and footer chrome but are not individually captured.

### States

- **Pressed** was forced with DevTools (`CSS.forcePseudoState` :active:hover) on every control, so a state a script adds on mousedown (if any) is missing.
- **Opened, expanded and selected states** that hydration renders (size listbox, menus, filter drawer, accordion toggles, wishlist aria-pressed=true) are absent — the archived copy cannot paint them.
- **Disabled, error and loading action states** were not seen painted on the public surface; their declared values are in the tokens (--colors-actions-*/--colors-forms-* disabled/error/loading).

### Themes

One painted theme, no toggle: white surfaces with the #222222 ink, #727272 secondary text, #e6e6e6 hairlines and the #e71d34 sale red, over the pulse token layer ('Farfetch Basis' UI, 'Nimbus Roman D' editorial). The dark scrims (ui-overlay01 rgba(34,34,34,.4)) and loyalty-tier palettes are declared inside the single theme; tokens.json emits light only.

### Fonts

- **'Farfetch Basis'** (UI) and **'Nimbus Roman D'** (editorial) are proprietary webfonts served from cdn-static.farfetch-contents.com; the woff2 files paint the captures (fetched through the archive) but are not shipped in this package. Samples fall back to Helvetica Neue/Arial and Times New Roman where noted.

### Screenshots

- Product photography, campaign imagery and brand names shown on cards are the product's published content; only frames and components were measured.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Product names, prices, campaign copy and photography are the product's content; only frames and components were measured.
