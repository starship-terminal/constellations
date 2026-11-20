# Airbnb components

The discovery list of every page and view captured, then one entry per component with crops of the real product and the Gaps. Captured from www.airbnb.com — which geo-redirected to www.airbnb.com.sg from this network, the same design system on a regional mirror — on 2026-11-10, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, searched, booked or sent.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (44 components, 105 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Airbnb Cereal VF 14/18 500, #222222`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (103 files, named `{component}-{state}.png`). Most are at 2x; a crop over about 1.2 megapixels is saved at 1x — each state's `cropScale` in [raw/components-computed.json](raw/components-computed.json) says which. Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png` (airbnb.com paints one light theme). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home. The header with the category tabs, the search pill, gallery rails of home cards and the footer. The load-time modal, the search panel open and a card hovered are separate captures. | `/` | [card-hover](screenshots/home-light-card-hover.png), [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [modal](screenshots/home-light-modal.png), [search-open](screenshots/home-light-search-open.png) |
| Experiences landing. Same shell with the experiences gallery. | `/experiences` | [default](screenshots/experiences-light-default.png), [full](screenshots/experiences-light-full.png) |
| Services landing (chefs, photography, spa). | `/services` | [default](screenshots/services-light-default.png), [full](screenshots/services-light-full.png) |
| Search results for Tokyo. The mini search pill, filter chips, result cards and the fees tag; the load-time modal is a separate capture. | `/s/Tokyo--Japan/homes` | [default](screenshots/search-light-default.png), [full](screenshots/search-light-full.png), [modal](screenshots/search-light-modal.png) |
| A Tokyo listing's page: title, photo grid, reserve card, host row, reviews and the footer. | `/rooms/<id> (a public listing the results page linked)` | [default](screenshots/room-light-default.png), [full](screenshots/room-light-full.png), [modal](screenshots/room-light-modal.png) |
| Help Centre. The headline, the search field and the topic grid. | `/help` | [default](screenshots/help-light-default.png), [full](screenshots/help-light-full.png) |
| Host landing. The earnings headline, Get started and the estimator card. | `/host/homes` | [default](screenshots/host-light-default.png), [full](screenshots/host-light-full.png) |
| Home at 390: the compact search pill and the listing rail. | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| Search results at 390: the pill and the card column. | `/s/Tokyo--Japan/homes` | [default](screenshots/mobile-search-light-default.png), [full](screenshots/mobile-search-light-full.png), [modal](screenshots/mobile-search-light-modal.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Load-time modal (a sign-up/coachmark card) | home, search, room, on load | at rest; then hidden by the overlay sweep for every other capture — never clicked | [home-light-modal](screenshots/home-light-modal.png), [search-light-modal](screenshots/search-light-modal.png), [room-light-modal](screenshots/room-light-modal.png), [mobile-search-light-modal](screenshots/mobile-search-light-modal.png) |
| Search panel, open | home | the Where segment clicked — a local UI toggle; nothing was searched | [home-light-search-open](screenshots/home-light-search-open.png), [search-panel-open](#search-panel-open) |
| Listing card, hovered | home | a real pointer hover over the first rail card | [home-light-card-hover](screenshots/home-light-card-hover.png), [listing-card](#listing-card) |
| Wishlist heart states | home and search | hovered, focused and a forced press; a real tap opens the sign-up sheet signed out, so pressed is forced | [card-heart](#card-heart), [result-heart](#result-heart) |
| Reserve card fields | room | the date and guest fields hovered only; a real click opens pickers the kit leaves shut | [reserve-field](#reserve-field) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 17 components were given a real keyboard focus. 3 draw an outline ring (`tab-active` (2px solid #222222 `grey.1000`, offset 4px), `tab` (2px solid #222222 `grey.1000`, offset 4px), `help-tile` (1px auto #005fcc, offset 1px)), the category tabs' being the 2px `#222` outline 4px out. The other buttons draw it as a box-shadow instead: a white 2px halo plus a `#222` ring hugging the shape (`header-host-link`, `header-menu`, `search-submit`, `card-heart`, `filters-button`, `filter-chip`, `result-heart`, `room-share`, `room-save`, `show-photos`, `host-cta`). `search-segment`, `footer-link`, `help-search` show neither on the measured element. `rail-arrow` could not be given a real keyboard focus at all, so its focus state is unmeasured rather than reported.

**Pressed.** Airbnb's controls shrink rather than change colour when pressed: buttons scale to about 0.96 (the header links, the search submit, the filter chips), the wishlist heart to 0.92, and the footer link stays put. Hovering greys the background behind the target (`#f7f7f7`); the search bar deepens its shadow.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `cubic-bezier(0.2, 0, 0, 1)` | transform | filter-chip, filters-button, host-cta, room-save, room-share, section-title |
| 0.2s | `cubic-bezier(0.2, 0, 0, 1)` | box-shadow | filter-chip, filters-button, header-host-link, host-cta, room-save, room-share, section-title, show-photos |
| 0.25s | `cubic-bezier(0.2, 0, 0, 1)` | transform | card-heart, header-host-link, header-menu, rail-arrow, result-heart, show-photos |
| 0.3s | `cubic-bezier(0.2, 0, 0, 1)` | background-color, border-color, color | filter-chip, filters-button, header-host-link, show-photos |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Listing card](#listing-card) | 181.7 x 214.61 | - | 20px | transparent | none | 0 |
| [Result card](#result-card) | 307.19 x 377.39 | - | 20px | transparent | none | 0 |
| [Search bar](#search-bar) | 850 x 66 | - | 32px | transparent | none | 0 |
| [Search panel (open)](#search-panel-open) | 393 x 1532 | - | - | transparent | none | 0 |
| [Help tile](#help-tile) | 344 x 48 | - | - | transparent | none | 0 |
| [Earnings estimator](#estimator-card) | 640 x 376 | - | - | transparent | none | 0 |
| [Reservation card](#reserve-card) | 372.33 x 312 | - | - | transparent | none | 0 |
| [Mobile listing card](#m-listing-card) | 165 x 198.75 | - | 20px | transparent | none | 0 |

## Components

### Header and navigation

The fixed top bar every page shares: the Bélo logo, the Homes / Experiences / Services category tabs with their icons, "Become a host", the language globe and the profile menu. The bar is 96px tall, white, with the search pill centred under it.

#### Header <a id="header"></a>
The fixed top bar: the Bélo logo, the category tabs (All, Homes, Experiences, Services) with their icons, "Become a host", the language globe and the profile menu. The search pill sits under it. Read as `header` on the home page.

**Values (default).** size 1440 x 96; padding 0px 48px; background transparent; text Airbnb Cereal VF 14/18 500, #222222 `grey.1000`; icon 102 x 32, #ff385c `rausch.default`.

Child layers that carry the look: span 3x3 background #222222 `grey.1000` radius 1.5px 0px 0px 1.5px; span 60x3 background #222222 `grey.1000`; span 3x3 background #222222 `grey.1000` radius 0px 1.5px 1.5px 0px.

![Header default](components/crops/header-default.png)

#### Become a host link <a id="header-host-link"></a>
The host entry point in the header. Measured and focused, never followed. Read as `header-host-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 121.27 x 40; padding 11px 12px; radius 20px; background transparent; text Airbnb Cereal VF 14/18 500, #222222 `grey.1000`; transition box-shadow 0.2s cubic-bezier(0.2, 0, 0, 1), transform 0.25s cubic-bezier(0.2, 0, 0, 1), background-color 0.3s cubic-bezier(0.2, 0, 0, 1), border-color 0.3s cubic-bezier(0.2, 0, 0, 1), color 0.3s cubic-bezier(0.2, 0, 0, 1) |
| hover | background #f7f7f7 `faint.default`; layers button (bg #f7f7f7 `faint.default`) |
| focus-visible | shadow #222222 0px 0px 0px 2px; transition box-shadow 0.2s cubic-bezier(0.2, 0, 0, 1); layers button (shadow #222222 `grey.1000` 0px 0px 0px 2px) |
| pressed | size 118.84 x 38.4; background #f7f7f7 `faint.default`; transform matrix(0.98, 0, 0, 0.96, 0, 0); layers button (bg #f7f7f7 `faint.default`) |

![Become a host link default](components/crops/header-host-link-default.png) ![Become a host link hover](components/crops/header-host-link-hover.png) ![Become a host link focus-visible](components/crops/header-host-link-focus-visible.png) ![Become a host link pressed](components/crops/header-host-link-pressed.png)

#### Language button <a id="header-globe"></a>
The globe icon button that opens the language/region sheet. Hovered and focused only. Read as `header-globe` on the home page.

Not on the page when it was captured. Not found on the captured page: the header has no language/region-labelled control. An earlier run's readings under this key measured the Search submit and were removed.

#### Profile menu button <a id="header-menu"></a>
The account buttons rightmost in the header (navigation menu and Log in or sign up). Pressed state is forced, not clicked: the menu leads to sign-up. Read as `header-menu` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 40; radius 50%; background #f2f2f2 `grey.200`; text Airbnb Cereal VF 14/normal 400, #222222 `grey.1000`; transition transform 0.25s cubic-bezier(0.2, 0, 0, 1); icon 20 x 20, #222222 `grey.1000`; before background #f2f2f2 `grey.200`, radius 50% |
| hover | before background #ebebeb `bebe.default`, radius 50% |
| focus-visible | transition box-shadow 0.2s cubic-bezier(0.2, 0, 0, 1); before background #f2f2f2 `grey.200`, shadow #ffffff 0px 0px 0px 2px, #222222 0px 0px 0px 4px, radius 50% |
| pressed | size 38 x 38; transform scale(0.95); icon 19 x 19, #222222 `grey.1000`; before background #ebebeb `bebe.default`, radius 50% |

![Profile menu button default](components/crops/header-menu-default.png) ![Profile menu button hover](components/crops/header-menu-hover.png) ![Profile menu button focus-visible](components/crops/header-menu-focus-visible.png) ![Profile menu button pressed](components/crops/header-menu-pressed.png)

#### Category tab (active) <a id="tab-active"></a>
A category tab in the header (Homes / Experiences / Services), the current one underlined. Read as `tab-active` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 103.55 x 36; padding 0px 0px 0px 5px; background transparent; text Airbnb Cereal VF 14/18 500, #6c6c6c `grey.700` |
| focus-visible | radius 8px; outline 2px solid #222222 `grey.1000`, offset 4px; layers a (outline 2px solid #222222 `grey.1000` offset 4px) |

![Category tab (active) default](components/crops/tab-active-default.png) ![Category tab (active) hover](components/crops/tab-active-hover.png) ![Category tab (active) focus-visible](components/crops/tab-active-focus-visible.png) ![Category tab (active) pressed](components/crops/tab-active-pressed.png)

#### Category tab <a id="tab"></a>
A resting category tab. Pressed is forced: a real click would navigate. Read as `tab` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 124.66 x 36; background transparent; text Airbnb Cereal VF 14/18 500, #6c6c6c `grey.700` |
| hover | text Airbnb Cereal VF 14/18 500, #222222 `grey.1000` |
| focus-visible | radius 8px; outline 2px solid #222222 `grey.1000`, offset 4px; layers a (outline 2px solid #222222 `grey.1000` offset 4px) |

![Category tab default](components/crops/tab-default.png) ![Category tab hover](components/crops/tab-hover.png) ![Category tab focus-visible](components/crops/tab-focus-visible.png) ![Category tab pressed](components/crops/tab-pressed.png)

### Search bar

The booking search: a white pill of Where / When / Who segments with hairline dividers and the pink gradient submit button. Clicking a segment expands the bar into the suggestion panel — a local toggle, never submitted.

#### Search bar <a id="search-bar"></a>
The big white pill: Where, When and Who segments with hairline dividers and the pink gradient submit button. Hovering a segment greys it. Read as `search-bar` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 850 x 66; radius 32px; background transparent; text Airbnb Cereal VF 12/16 500, #222222 `grey.1000` |
| hover | layers div (bg #ebebeb `bebe.default`) |

Child layers that carry the look: div 1x32 background #dddddd `deco.default`; div 1x32 background #dddddd `deco.default`.

![Search bar default](components/crops/search-bar-default.png) ![Search bar hover](components/crops/search-bar-hover.png)

#### Search segment <a id="search-segment"></a>
One labelled segment of the search pill (Where / When / Who): a label line over a placeholder line. Pressed is forced, never submitted. Read as `search-segment` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 278.33 x 66; radius 32px; background transparent; text Airbnb Cereal VF 12/16 500, #222222 `grey.1000`; after radius 32px |
| hover | background #ebebeb `bebe.default`; before background #ffffff `always.white`; layers div (bg #ebebeb `bebe.default`) |
| focus-visible | layers div (bg #ffffff `always.white`; shadow rgba(0, 0, 0, 0.1) 0px 3px 12px 0px, rgba(0, 0, 0, 0.08) `shadow.100` 0px 1px 2px 0px; border T:1px solid #dddddd `deco.default` / R:1px solid #dddddd `deco.default` / B:1px solid #dddddd `deco.default` / L:1px solid #dddddd `deco.default`) |
| pressed | background #dddddd `deco.default`; before background #ebebeb `bebe.default`; layers div (bg #dddddd `deco.default`); div (bg #ffffff `always.white`; shadow rgba(0, 0, 0, 0.1) 0px 3px 12px 0px, rgba(0, 0, 0, 0.08) `shadow.100` 0px 1px 2px 0px; border T:1px solid #dddddd `deco.default` / R:1px solid #dddddd `deco.default` / B:1px solid #dddddd `deco.default` / L:1px solid #dddddd `deco.default`) |

![Search segment default](components/crops/search-segment-default.png) ![Search segment hover](components/crops/search-segment-hover.png) ![Search segment focus-visible](components/crops/search-segment-focus-visible.png) ![Search segment pressed](components/crops/search-segment-pressed.png)

#### Search submit button <a id="search-submit"></a>
The pink gradient round button with the magnifier (icon only at rest, icon + "Search" when the bar is expanded). Pressed is forced: a real press runs the search. Read as `search-submit` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 99.67 x 48; radius 24px; background transparent; text Airbnb Cereal VF 16/20 500, #ffffff `always.white`; icon 16 x 16, #ffffff `always.white` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #222222 0px 0px 0px 4px; layers button (shadow #ffffff `always.white` 0px 0px 0px 2px, #222222 `grey.1000` 0px 0px 0px 4px) |

Child layers that carry the look: div 99.7x48 image linear-gradient(to right, #e61e4d 0%, #e31c5f 50%, #d70466 100%) radius 24px.

![Search submit button default](components/crops/search-submit-default.png) ![Search submit button hover](components/crops/search-submit-hover.png) ![Search submit button focus-visible](components/crops/search-submit-focus-visible.png) ![Search submit button pressed](components/crops/search-submit-pressed.png)

#### Search panel (open) <a id="search-panel-open"></a>
The suggestion panel the Where segment opens ("Suggested destinations": Nearby and city rows with pictograms). Opened by clicking the segment, a local UI toggle; nothing was searched. Read as `search-panel-open` on the home page.

**Values (open).** size 393 x 1532; background transparent; text Airbnb Cereal VF 12/16 400, #222222 `grey.1000`.

Child layers that carry the look: div 361x72 background #ffffff `always.white` radius 12px; div 56x56 background #f4f4f4 radius 12px; div 361x72 background #ffffff `always.white` radius 12px.

![Search panel (open) open](components/crops/search-panel-open-open.png)

#### Mini search pill <a id="mini-search"></a>
The collapsed search pill the results page shows: three segments and the small pink submit. Measured, never opened. Read as `mini-search` on the search results page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 381.36 x 46; background transparent; text Airbnb Cereal VF 14/22 500, #222222 `grey.1000` |

Child layers that carry the look: button 177.9x48 border 1px solid transparent radius 40px 4px 4px 40px; span 1x24 background #dddddd `deco.default`; button 98.4x48 border 1px solid transparent radius 4px.

![Mini search pill default](components/crops/mini-search-default.png) ![Mini search pill hover](components/crops/mini-search-hover.png)

### Home galleries

The home page's recommendation rails: a section title with a chevron, then cards that scroll sideways behind rail arrows. Each card is a 12px-radius photo with a Guest favourite badge and a wishlist heart, then title, price and star rating.

#### Section title <a id="section-title"></a>
A gallery section head ("Places to stay in Busan") with a chevron that follows to the search page. Read as `section-title` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 243.52 x 28; radius 8px; background transparent; text Airbnb Cereal VF 20/24 600, #222222 `grey.1000`; transition box-shadow 0.2s cubic-bezier(0.2, 0, 0, 1), transform 0.1s cubic-bezier(0.2, 0, 0, 1); icon 12 x 12, #222222 `grey.1000` |
| hover | icon 12.92 x 12.92, #222222 `grey.1000`; layers span (bg #ebebeb `bebe.default`) |

Child layers that carry the look: span 28x28 background #f2f2f2 `grey.200` radius 14px.

![Section title default](components/crops/section-title-default.png) ![Section title hover](components/crops/section-title-hover.png)

#### Listing card <a id="listing-card"></a>
A home card in a rail: a 12px-radius photo with the Guest favourite badge and wishlist heart over it, then the title, price and star rating rows. Read as `listing-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 181.7 x 214.61; radius 20px; background transparent; text Airbnb Cereal VF 11/13 600, #222222 `grey.1000`; icon 24 x 24, #222222 `grey.1000` |

Child layers that carry the look: div 181.7x172.6 background #dddddd `deco.default` radius 20px; div 103.6x26 background rgba(255, 255, 255, 0.8) border 1px solid rgba(255, 255, 255, 0.5) radius 14px shadow rgba(0, 0, 0, 0.02) 0px 0px 0px 1px, rgba(0, 0, 0, 0.04) `shadow.50` 0px 2px 6px 0px, rgba(0, 0, 0, 0.1) 0px 4px 8px 0px.

![Listing card default](components/crops/listing-card-default.png) ![Listing card hover](components/crops/listing-card-hover.png)

#### Carousel arrow <a id="rail-arrow"></a>
The small white round button that pages a card rail. Hovered and focused only; pressing pages the rail. Read as `rail-arrow` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 28 x 28; radius 50%; background #f2f2f2 `grey.200`; text Airbnb Cereal VF 14/normal 400, #c1c1c1 `grey.500`; transition transform 0.25s cubic-bezier(0.2, 0, 0, 1); opacity 0.5; icon 12 x 12, #c1c1c1 `grey.500`; before background #f2f2f2 `grey.200`, radius 50% |
| hover | icon 11.2 x 11.2, #c1c1c1 `grey.500` |
| pressed | icon 12.92 x 12.92, #c1c1c1 `grey.500` |

![Carousel arrow default](components/crops/rail-arrow-default.png) ![Carousel arrow hover](components/crops/rail-arrow-hover.png) ![Carousel arrow pressed](components/crops/rail-arrow-pressed.png)

#### Wishlist heart <a id="card-heart"></a>
The heart toggle over the card photo. Pressed is forced: a real tap opens the sign-up sheet signed out. Read as `card-heart` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; padding 2px 0px 0px 0px; radius 50%; background transparent; text Airbnb Cereal VF 16/20 500, #222222 `grey.1000`; transition transform 0.25s cubic-bezier(0.2, 0, 0, 1); icon 24 x 24, #222222 `grey.1000` |
| hover | size 34.56 x 34.56; transform scale(1.08); icon 25.92 x 25.92, #222222 `grey.1000` |
| focus-visible | size 34.56 x 34.56; shadow #ffffff 0px 0px 0px 2px, #222222 0px 0px 0px 4px; transition box-shadow 0.2s cubic-bezier(0.2, 0, 0, 1); transform scale(1.08); icon 25.92 x 25.92, #222222 `grey.1000`; layers button (shadow #ffffff `always.white` 0px 0px 0px 2px, #222222 `grey.1000` 0px 0px 0px 4px) |
| pressed | size 29.44 x 29.44; transform scale(0.92); icon 22.08 x 22.08, #222222 `grey.1000` |

![Wishlist heart default](components/crops/card-heart-default.png) ![Wishlist heart hover](components/crops/card-heart-hover.png) ![Wishlist heart focus-visible](components/crops/card-heart-focus-visible.png) ![Wishlist heart pressed](components/crops/card-heart-pressed.png)

#### Rating row <a id="card-rating"></a>
The star and average under the card title. Read as `card-rating` on the home page.

**Values (default).** size 23.92 x 16; background transparent; text Airbnb Cereal VF 12/16 400, #6c6c6c `grey.700`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Guest favourite badge <a id="card-badge"></a>
The white pill over the card photo (Guest favourite / Superhost). Read as `card-badge` on the home page.

**Values (default).** size 157.7 x 53.53; background transparent; text Airbnb Cereal VF 11/13 600, #222222 `grey.1000`; icon 24 x 24, #222222 `grey.1000`.

Child layers that carry the look: div 103.6x26 background rgba(255, 255, 255, 0.8) border 1px solid rgba(255, 255, 255, 0.5) radius 14px shadow rgba(0, 0, 0, 0.02) 0px 0px 0px 1px, rgba(0, 0, 0, 0.04) `shadow.50` 0px 2px 6px 0px, rgba(0, 0, 0, 0.1) 0px 4px 8px 0px.

![Guest favourite badge default](components/crops/card-badge-default.png)

### Search results

The results page: the mini search pill, the Filters button and filter chips, then full-width result cards with the fees-included tag.

#### Filters button <a id="filters-button"></a>
The sliders-icon button that opens the filters sheet. Pressed is forced; opening the sheet is a toggle but the row also navigates. Read as `filters-button` on the search results page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 83.64 x 34; padding 8px 12px; border 1px solid #dddddd `deco.default`; radius 24px; background #ffffff `always.white`; text Airbnb Cereal VF 12/16 400, #222222 `grey.1000`; transition box-shadow 0.2s cubic-bezier(0.2, 0, 0, 1), transform 0.1s cubic-bezier(0.2, 0, 0, 1), border-color 0.3s cubic-bezier(0.2, 0, 0, 1), background-color 0.3s cubic-bezier(0.2, 0, 0, 1); icon 16 x 16, #222222 `grey.1000` |
| hover | border 1px solid #c1c1c1 `grey.500`; layers button (bg #ffffff `always.white`; border T:1px solid #c1c1c1 `grey.500` / R:1px solid #c1c1c1 `grey.500` / B:1px solid #c1c1c1 `grey.500` / L:1px solid #c1c1c1 `grey.500`) |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #222222 0px 0px 0px 4px; layers button (bg #ffffff `always.white`; shadow #ffffff `always.white` 0px 0px 0px 2px, #222222 `grey.1000` 0px 0px 0px 4px; border T:1px solid #dddddd `deco.default` / R:1px solid #dddddd `deco.default` / B:1px solid #dddddd `deco.default` / L:1px solid #dddddd `deco.default`) |
| pressed | size 81.64 x 32; border 1px solid #c1c1c1 `grey.500`; transform matrix(0.976088, 0, 0, 0.941176, 0, 0); icon 15.62 x 15.06, #222222 `grey.1000`; layers button (bg #ffffff `always.white`; border T:1px solid #c1c1c1 `grey.500` / R:1px solid #c1c1c1 `grey.500` / B:1px solid #c1c1c1 `grey.500` / L:1px solid #c1c1c1 `grey.500`) |

![Filters button default](components/crops/filters-button-default.png) ![Filters button hover](components/crops/filters-button-hover.png) ![Filters button focus-visible](components/crops/filters-button-focus-visible.png) ![Filters button pressed](components/crops/filters-button-pressed.png)

#### Filter chip <a id="filter-chip"></a>
One pill in the quick-filter row (Type of place, Price, Kitchen …). Pressed is forced. Read as `filter-chip` on the search results page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 54 x 34; padding 8px 12px; border 1px solid #dddddd `deco.default`; radius 24px; background #ffffff `always.white`; text Airbnb Cereal VF 12/16 400, #222222 `grey.1000`; transition box-shadow 0.2s cubic-bezier(0.2, 0, 0, 1), transform 0.1s cubic-bezier(0.2, 0, 0, 1), border-color 0.3s cubic-bezier(0.2, 0, 0, 1), background-color 0.3s cubic-bezier(0.2, 0, 0, 1) |
| hover | border 1px solid #c1c1c1 `grey.500`; layers button (bg #ffffff `always.white`; border T:1px solid #c1c1c1 `grey.500` / R:1px solid #c1c1c1 `grey.500` / B:1px solid #c1c1c1 `grey.500` / L:1px solid #c1c1c1 `grey.500`) |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #222222 0px 0px 0px 4px; layers button (bg #ffffff `always.white`; shadow #ffffff `always.white` 0px 0px 0px 2px, #222222 `grey.1000` 0px 0px 0px 4px; border T:1px solid #dddddd `deco.default` / R:1px solid #dddddd `deco.default` / B:1px solid #dddddd `deco.default` / L:1px solid #dddddd `deco.default`) |
| pressed | size 52 x 32; border 1px solid #c1c1c1 `grey.500`; transform matrix(0.962963, 0, 0, 0.941176, 0, 0); layers button (bg #ffffff `always.white`; border T:1px solid #c1c1c1 `grey.500` / R:1px solid #c1c1c1 `grey.500` / B:1px solid #c1c1c1 `grey.500` / L:1px solid #c1c1c1 `grey.500`) |

![Filter chip default](components/crops/filter-chip-default.png) ![Filter chip hover](components/crops/filter-chip-hover.png) ![Filter chip focus-visible](components/crops/filter-chip-focus-visible.png) ![Filter chip pressed](components/crops/filter-chip-pressed.png)

#### Result card <a id="result-card"></a>
A listing card in the results grid: photo with badge and heart, then title, distance line, bed rows, dates, price and Free cancellation. Read as `result-card` on the search results page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 307.19 x 377.39; radius 20px; background transparent; text Airbnb Cereal VF 14/18 500, #ffffff `always.white`; icon 24 x 24, #222222 `grey.1000` |

Child layers that carry the look: div 307.2x230.4 background #dddddd `deco.default` radius 20px; div 307.2x230.4 image linear-gradient(transparent 80%, rgba(0, 0, 0, 0.25)); div 89.8x28 background rgba(96, 96, 96, 0.6) border 1px solid rgba(255, 255, 255, 0.16) radius 40px.

![Result card default](components/crops/result-card-default.png) ![Result card hover](components/crops/result-card-hover.png)

#### Listing badge <a id="result-badge"></a>
The white pill over the photo (Guest favourite / Superhost). Read as `result-badge` on the search results page.

**Values (default).** size 67.84 x 18; background transparent; text Airbnb Cereal VF 14/18 500, #ffffff `always.white`.

![Listing badge default](components/crops/result-badge-default.png)

#### Wishlist heart <a id="result-heart"></a>
The heart over the photo. Pressed is forced: signed out it opens the sign-up sheet. Read as `result-heart` on the search results page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; padding 2px 0px 0px 0px; radius 50%; background transparent; text Airbnb Cereal VF 16/20 500, #222222 `grey.1000`; transition transform 0.25s cubic-bezier(0.2, 0, 0, 1); icon 24 x 24, #222222 `grey.1000` |
| hover | size 34.56 x 34.56; transform scale(1.08); icon 25.92 x 25.92, #222222 `grey.1000` |
| focus-visible | size 34.56 x 34.56; shadow #222222 0px 0px 0px 2px, rgba(255, 255, 255, 0.8) 0px 0px 0px 4px; transition box-shadow 0.2s cubic-bezier(0.2, 0, 0, 1); transform scale(1.08); icon 25.92 x 25.92, #222222 `grey.1000`; layers button (shadow #222222 `grey.1000` 0px 0px 0px 2px, rgba(255, 255, 255, 0.8) 0px 0px 0px 4px) |
| pressed | size 29.44 x 29.44; transform scale(0.92); icon 22.08 x 22.08, #222222 `grey.1000` |

![Wishlist heart default](components/crops/result-heart-default.png) ![Wishlist heart hover](components/crops/result-heart-hover.png) ![Wishlist heart focus-visible](components/crops/result-heart-focus-visible.png) ![Wishlist heart pressed](components/crops/result-heart-pressed.png)

#### All-fees tag <a id="fees-tag"></a>
The inline tag over the results grid explaining the total price display. Read as `fees-tag` on the search results page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 179.69 x 28; padding 10px 0px 0px 40px; background transparent; text Airbnb Cereal VF 14/18 500, #222222 `grey.1000` |

![All-fees tag default](components/crops/fees-tag-default.png) ![All-fees tag hover](components/crops/fees-tag-hover.png)

### Room page

A listing's own page: the photo mosaic, the reserve card in the right column, the guest plaque and the promo strip. Nothing was booked or saved.

#### Room title <a id="room-title"></a>
The listing headline under the header. Read as `room-title` on the room page.

**Values (default).** size 973.89 x 64; background transparent; text Airbnb Cereal VF 26/30 500, #222222 `grey.1000`.

![Room title default](components/crops/room-title-default.png)

#### Share button <a id="room-share"></a>
The underlined Share action beside Save. Pressed is forced. Read as `room-share` on the room page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 77.14 x 34; padding 8px; radius 8px; background transparent; text Airbnb Cereal VF 14/18 500, #222222 `grey.1000`; transition box-shadow 0.2s cubic-bezier(0.2, 0, 0, 1), transform 0.1s cubic-bezier(0.2, 0, 0, 1); icon 16 x 16, #222222 `grey.1000` |
| hover | background #f7f7f7 `faint.default`; text Airbnb Cereal VF 14/18 500, #000000 `always.black`; icon 16 x 16, #000000 `always.black`; layers button (bg #f7f7f7 `faint.default`) |
| focus-visible | background #f7f7f7 `faint.default`; shadow #222222 0px 0px 0px 2px, rgba(255, 255, 255, 0.8) 0px 0px 0px 4px; transition box-shadow 0.2s cubic-bezier(0.2, 0, 0, 1); layers button (bg #f7f7f7 `faint.default`; shadow #222222 `grey.1000` 0px 0px 0px 2px, rgba(255, 255, 255, 0.8) 0px 0px 0px 4px) |
| pressed | size 74.05 x 32.64; background #f7f7f7 `faint.default`; text Airbnb Cereal VF 14/18 500, #000000 `always.black`; transform scale(0.96); icon 15.36 x 15.36, #000000 `always.black`; layers button (bg #f7f7f7 `faint.default`) |

![Share button default](components/crops/room-share-default.png) ![Share button hover](components/crops/room-share-hover.png) ![Share button focus-visible](components/crops/room-share-focus-visible.png) ![Share button pressed](components/crops/room-share-pressed.png)

#### Save button <a id="room-save"></a>
The heart+Save action. Pressed is forced: signed out, a real press opens the sign-up sheet. Read as `room-save` on the room page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 71 x 34; padding 8px; radius 8px; background transparent; text Airbnb Cereal VF 14/18 500, #222222 `grey.1000`; transition box-shadow 0.2s cubic-bezier(0.2, 0, 0, 1), transform 0.1s cubic-bezier(0.2, 0, 0, 1); icon 16 x 16, #222222 `grey.1000` |
| hover | background #f7f7f7 `faint.default`; text Airbnb Cereal VF 14/18 500, #000000 `always.black`; icon 16 x 16, #000000 `always.black`; layers button (bg #f7f7f7 `faint.default`) |
| focus-visible | background #f7f7f7 `faint.default`; shadow #222222 0px 0px 0px 2px, rgba(255, 255, 255, 0.8) 0px 0px 0px 4px; transition box-shadow 0.2s cubic-bezier(0.2, 0, 0, 1); layers button (bg #f7f7f7 `faint.default`; shadow #222222 `grey.1000` 0px 0px 0px 2px, rgba(255, 255, 255, 0.8) 0px 0px 0px 4px) |
| pressed | size 68.16 x 32.64; background #f7f7f7 `faint.default`; text Airbnb Cereal VF 14/18 500, #000000 `always.black`; transform scale(0.96); icon 15.36 x 15.36, #000000 `always.black`; layers button (bg #f7f7f7 `faint.default`) |

![Save button default](components/crops/room-save-default.png) ![Save button hover](components/crops/room-save-hover.png) ![Save button focus-visible](components/crops/room-save-focus-visible.png) ![Save button pressed](components/crops/room-save-pressed.png)

#### Photo collage <a id="photo-grid"></a>
The 5-photo mosaic: one large tile left, a 2x2 grid right, 12px radius. Read as `photo-grid` on the room page.

**Values (default).** size 1120 x 476; background transparent; text Airbnb Cereal VF 12/16 500, #222222 `grey.1000`; icon 16 x 16, #222222 `grey.1000`.

Child layers that carry the look: div 560x476 background rgba(34, 34, 34, 0.1); div::after 560pxx476px background #3f3f3f `grey.900`; div 272x238 background rgba(34, 34, 34, 0.1).

![Photo collage default](components/crops/photo-grid-default.png)

#### Show all photos button <a id="show-photos"></a>
The white pill bottom-right of the collage. Pressed is forced: it opens the photo viewer. Read as `show-photos` on the room page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 140.28 x 32; padding 8px 16px; radius 8px; background #f2f2f2 `grey.200`; text Airbnb Cereal VF 12/16 500, #222222 `grey.1000`; transition box-shadow 0.2s cubic-bezier(0.2, 0, 0, 1), transform 0.25s cubic-bezier(0.2, 0, 0, 1), background-color 0.3s cubic-bezier(0.2, 0, 0, 1), border-color 0.3s cubic-bezier(0.2, 0, 0, 1), color 0.3s cubic-bezier(0.2, 0, 0, 1); icon 16 x 16, #222222 `grey.1000` |
| hover | background #ebebeb `bebe.default`; layers button (bg #ebebeb `bebe.default`) |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #222222 0px 0px 0px 4px; transition box-shadow 0.2s cubic-bezier(0.2, 0, 0, 1); layers button (bg #f2f2f2 `grey.200`; shadow #ffffff `always.white` 0px 0px 0px 2px, #222222 `grey.1000` 0px 0px 0px 4px) |
| pressed | size 138.28 x 30; background #ebebeb `bebe.default`; transform matrix(0.985743, 0, 0, 0.9375, 0, 0); icon 15.77 x 15, #222222 `grey.1000`; layers button (bg #ebebeb `bebe.default`) |

![Show all photos button default](components/crops/show-photos-default.png) ![Show all photos button hover](components/crops/show-photos-hover.png) ![Show all photos button focus-visible](components/crops/show-photos-focus-visible.png) ![Show all photos button pressed](components/crops/show-photos-pressed.png)

#### Listing subtitle <a id="room-subtitle"></a>
The "Entire rental unit in …" line and the guests/bedrooms/beds row. Read as `room-subtitle` on the room page.

**Values (default).** size 653.33 x 26; background transparent; text Airbnb Cereal VF 22/26 500, #222222 `grey.1000`.

![Listing subtitle default](components/crops/room-subtitle-default.png)

#### Guest favourite plaque <a id="guest-plaque"></a>
The laurel-bordered strip: "Guest favourite / One of the most loved homes on Airbnb" with the rating and review count. Read as `guest-plaque` on the room page.

**Values (default).** size 1120 x 242; background transparent; text Airbnb Cereal VF 100/100 500, #222222 `grey.1000`.

![Guest favourite plaque default](components/crops/guest-plaque-default.png)

#### Reservation card <a id="reserve-card"></a>
The booking card pinned right: "Add dates for prices", the CHECK-IN/CHECK-OUT/GUESTS field grid. Nothing was booked. Read as `reserve-card` on the room page.

**Values (default).** size 372.33 x 312; background transparent; text Airbnb Cereal VF 22/26 500, #222222 `grey.1000`; icon 16 x 16, #222222 `grey.1000`.

Child layers that carry the look: aside 372.3x280 border 1px solid #dddddd `deco.default` radius 12px shadow rgba(0, 0, 0, 0.12) `shadow.150` 0px 6px 16px 0px; div 322.3x116 background #ffffff `always.white` radius 12px; button 322.3x56 background #ffffff `always.white`.

![Reservation card default](components/crops/reserve-card-default.png)

#### Date field <a id="reserve-field"></a>
A labelled field cell in the booking grid (CHECK-IN / CHECKOUT / GUESTS). Read as `reserve-field` on the room page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 160.67 x 56; background transparent; text Airbnb Cereal VF 10/12 700, #222222 `grey.1000` |

![Date field default](components/crops/reserve-field-default.png) ![Date field hover](components/crops/reserve-field-hover.png)

#### Promo strip <a id="promo-strip"></a>
The discount banner ("Get $25 SGD off your getaway") with the outlined Claim button. Measured, never pressed. Read as `promo-strip` on the room page.

Not on the page when it was captured.

#### Claim button <a id="promo-claim"></a>
The outlined Claim action on the promo strip. Pressed is forced: claiming needs an account. Read as `promo-claim` on the room page.

Not on the page when it was captured.

#### Host row <a id="host-row"></a>
The "Hosted by" row with the circular avatar. Read as `host-row` on the room page.

**Values (default).** size 177.28 x 20; background transparent; text Airbnb Cereal VF 16/20 500, #222222 `grey.1000`.

![Host row default](components/crops/host-row-default.png)

### Help Centre

The Help Centre home: the headline, the search field and topic tiles.

#### Footer link <a id="footer-link"></a>
A quick link in the footer grid. Pressed is forced: a real click navigates. Read as `footer-link` on the Help Centre page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 437.33 x 20.02; background transparent; text Airbnb Cereal VF 14/18 400, #222222 `grey.1000` |
| focus-visible | text Airbnb Cereal VF 14/18 400, #ffffff `always.white`; layers a (bg #3f3f3f `grey.900`; shadow #3f3f3f `grey.900` 0px 0px 0px 2px) |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Help title <a id="help-title"></a>
"Hi, how can we help?" — the Help Centre headline. Read as `help-title` on the Help Centre page.

**Values (default).** size 1064 x 56; background transparent; text Airbnb Cereal VF 40/56 500, #222222 `grey.1000`.

![Help title default](components/crops/help-title-default.png)

#### Help search field <a id="help-search"></a>
The search field under the headline (the icon + placeholder). Focused only; nothing was searched. Read as `help-search` on the Help Centre page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 342 x 68; padding 24px 0px 24px 32px; background transparent; text Airbnb Cereal VF 16/20 500, #222222 `grey.1000`; placeholder #222222 `grey.1000` |

![Help search field default](components/crops/help-search-default.png) ![Help search field focus-visible](components/crops/help-search-focus-visible.png)

#### Help tile <a id="help-tile"></a>
A topic card in the help grid. Pressed is forced: a real click navigates. Read as `help-tile` on the Help Centre page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 344 x 48; background transparent; text Airbnb Cereal VF 18/24 500, #222222 `grey.1000` |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a (outline 1px auto #005fcc offset 1px) |

![Help tile default](components/crops/help-tile-default.png) ![Help tile hover](components/crops/help-tile-hover.png) ![Help tile focus-visible](components/crops/help-tile-focus-visible.png) ![Help tile pressed](components/crops/help-tile-pressed.png)

### Host landing

The host recruiting page: the earnings headline, the Get started CTA and the earnings estimator card, measured at rest.

#### Host headline <a id="host-hero"></a>
"Your home could make money on Airbnb". Read as `host-hero` on the host landing page.

**Values (default).** size 556 x 192; background transparent; text Airbnb Cereal VF 60/64 700, #222222 `grey.1000`.

![Host headline default](components/crops/host-hero-default.png)

#### Get started button <a id="host-cta"></a>
The rausch CTA in the nav and on the page. Pressed is forced: it starts the host sign-up flow. Read as `host-cta` on the host landing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 143.92 x 48; padding 14px 28px; radius 40px; background transparent; image linear-gradient(to right, #e61e4d 0%, #e31c5f 50%, #d70466 100%); text Airbnb Cereal VF 16/20 500, #ffffff `always.white`; transition box-shadow 0.2s cubic-bezier(0.2, 0, 0, 1), transform 0.1s cubic-bezier(0.2, 0, 0, 1) |
| focus-visible | shadow rgba(255, 255, 255, 0.8) 0px 0px 0px 2px, #222222 0px 0px 0px 4px; transition box-shadow 0.2s cubic-bezier(0.2, 0, 0, 1); layers a (bgImage linear-gradient(to right, #e61e4d 0%, #e31c5f 50%, #d70466 100%); shadow rgba(255, 255, 255, 0.8) 0px 0px 0px 2px, #222222 `grey.1000` 0px 0px 0px 4px) |
| pressed | size 138.17 x 46.08; background #ff385c `rausch.default`; image none; transform scale(0.96); layers a (bg #ff385c `rausch.default`) |

![Get started button default](components/crops/host-cta-default.png) ![Get started button hover](components/crops/host-cta-hover.png) ![Get started button focus-visible](components/crops/host-cta-focus-visible.png) ![Get started button pressed](components/crops/host-cta-pressed.png)

#### Earnings estimator <a id="estimator-card"></a>
The interactive earnings card (location field, guest slider, monthly total). Measured at rest; nothing was submitted. Read as `estimator-card` on the host landing page.

**Values (default).** size 640 x 376; background transparent; text Airbnb Cereal VF 60/64 700, #222222 `grey.1000`; icon 16 x 16, #222222 `grey.1000`.

Child layers that carry the look: button 418x64 background #ffffff `always.white` border 1px solid #dddddd `deco.default` radius 40px.

![Earnings estimator default](components/crops/estimator-card-default.png)

### Mobile (390 wide)

A few components as a phone draws them, at 390 x 844 with an iPhone user agent.

#### Mobile search pill <a id="m-search-pill"></a>
The compact search bar at the top of the mobile home. Read as `m-search-pill` on the home page at 390 wide.

**Values (default).** size 390 x 68; background #ffffff `always.white`; text Airbnb Cereal VF 14/18 500, #222222 `grey.1000`; icon 12 x 12, #222222 `grey.1000`.

![Mobile search pill default](components/crops/m-search-pill-default.png)

#### Mobile listing card <a id="m-listing-card"></a>
A home card in the mobile rail: full-bleed photo, badge, heart, title, price. Read as `m-listing-card` on the home page at 390 wide.

**Values (default).** size 165 x 198.75; radius 20px; background transparent; text Airbnb Cereal VF 13/16 500, #222222 `grey.1000`; icon 24 x 24, #222222 `grey.1000`.

Child layers that carry the look: div 165x156.8 background #dddddd `deco.default` radius 20px shadow rgba(0, 0, 0, 0.02) 0px 0px 0px 1px, rgba(0, 0, 0, 0.1) 0px 8px 24px 0px.

![Mobile listing card default](components/crops/m-listing-card-default.png)
## Gaps

### Pages

- **Signed-in pages.** Nothing behind sign-in was captured: trips, wishlists, the host dashboard, account settings, checkout and messages. The kit never signs in.
- **Anything that sends or creates.** No search was submitted (the Where segment was clicked into its panel and left there), no booking was made, no listing was saved, no help question was sent, no host sign-up was started, no filter was applied.
- **The map.** The results page's interactive map and its price pills load late and sit in canvases; the `fees-tag` entry is the pill chrome, not the map itself.
- **The app and other locales.** airbnb.com redirects by geography (this capture landed on the .sg mirror); the native apps and logged-out variants in other regions can draw different coachmarks and promos.
- **The wishlist sheet.** Tapping a heart signed out opens a sign-up sheet; the heart's own states are measured but the sheet is not opened.

### States

- **Pressed** was forced with DevTools (`CSS.forcePseudoState`) on every control, so a state a script adds on mousedown (if any) is missing.
- **The reserve card's pickers** (date calendar, guest stepper) were hovered but never opened — a click opens UI the kit leaves shut; nothing was booked.
- **Search suggestions** come from the locale and the account; the panel's rows are a snapshot, not an exhaustive list.
- **Disabled states** were not seen on any public control.

### Themes

airbnb.com paints one light theme: every page sets `data-color-scheme="light"` on its roots and `prefersDarkChangesPage` is false on every capture (`themeChecks` in [raw/css-vars.json](raw/css-vars.json)). The stylesheets do declare a full dark palette — the always-dark `.c12bynq4` theme class, and `.c1r7ywgw` rebinding every `--palette-*` name to `--x-dark` under `prefers-color-scheme: dark` — so the token file ships those declared values as a `dark` set, clearly marked never-applied. There is no theme switch in the header, the menus or the footer.

### Fonts

- **Airbnb Cereal VF** is Airbnb's variable face (203 `@font-face` declarations capture its weights); it is served from a0.muscache.com and is not on Google Fonts; the style guide falls back to the system font.

### Screenshots

- Listing photos, avatars and editorial images are Airbnb/host content and appear only inside screenshots and crops. The rails lazy-load, so a second capture of the same page can draw different listings.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Reviews, listing copy and help articles were not transcribed; only the frames around them were measured.
- No personal data was captured: the pages were read signed out, and no location was searched for.
