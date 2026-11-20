# Expedia components

The discovery list of every page and view captured, then one entry per component with crops of the real product and the Gaps. Captured from www.expedia.com on 2026-11-14, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, searched for, booked, created, sent or uploaded.

expedia.com answers automation with a 429 "Bot or Not?" challenge, so the DOM is a Wayback snapshot of the public home and hotel-search pages served locally and painted with Expedia's live travel-assets.com CSS and fonts. Entries on the `home-i` page were read on the same snapshot hydrated with the site's own JavaScript, so the field panels (calendar, travellers, destination) open on click; hydration's API refetches fail on the archived page, so only no-submit UI states were read.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (57 components, 116 states). The page layouts are described in [raw/pages.md](raw/pages.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Centra No2 14/20 400, #191e3b`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the page, in [components/crops/](components/crops) (115 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png` (`home-i` is the hydrated home). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home. Hero photo, the Reckless XPD title, the multi-product search card, marketing bands, deals carousels, footer. The sign-in card and Shop travel menu are shown open. | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [shoptravel-open](screenshots/home-light-shoptravel-open.png), [signin-open](screenshots/home-light-signin-open.png) |
| Home, hydrated. The calendar dialog, travellers menu and Where-to panel opened by clicking the field triggers; the Flights tab variant. | `/ (hydrated)` | [calendar-open](screenshots/home-i-light-calendar-open.png), [flights-tab](screenshots/home-i-light-flights-tab.png), [travelers-open](screenshots/home-i-light-travelers-open.png), [whereto-open](screenshots/home-i-light-whereto-open.png) |
| Hotel search results. Compact search form, stay-type tabs, sort pill open, filter rail and map card, property cards. | `/Hotel-Search` | [default](screenshots/search-light-default.png), [full](screenshots/search-light-full.png), [sort-open](screenshots/search-light-sort-open.png) |
| Home at 390: the hero and search card, the full page. | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| Home at 390, hydrated: the calendar sheet. | `/ (hydrated)` | [calendar-open](screenshots/mobile-home-i-light-calendar-open.png) |
| Hotel results at 390. | `/Hotel-Search` | [default](screenshots/mobile-search-light-default.png), [full](screenshots/mobile-search-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Sign-in card | header, every page | the header's no-JS checkbox menu, forced open; the Sign in button inside was hovered only, never followed | [home-light-signin-open](screenshots/home-light-signin-open.png), [signin-card](#sign-in-card) |
| Shop travel menu | header | the Shop travel control, opened by its trigger | [home-light-shoptravel-open](screenshots/home-light-shoptravel-open.png) |
| Calendar dialog | home search form, hydrated | the Dates field clicked; a selected day and range chip read at rest; Done never pressed to search | [home-i-light-calendar-open](screenshots/home-i-light-calendar-open.png), [calendar-dialog](#calendar-dialog) |
| Travellers menu | home search form, hydrated | the Travelers field clicked; the steppers left untouched | [home-i-light-travelers-open](screenshots/home-i-light-travelers-open.png), [travelers-menu](#travelers-menu) |
| Where-to panel | home search form, hydrated | the Where to? field clicked; sample text typed and deleted, nothing searched | [home-i-light-whereto-open](screenshots/home-i-light-whereto-open.png), [whereto-panel](#destination-panel) |
| Flights tab | home search form, hydrated | the Flights product tab | [home-i-light-flights-tab](screenshots/home-i-light-flights-tab.png) |
| Sort pill, open | hotel results | the Sort by pill clicked; no order applied | [search-light-sort-open](screenshots/search-light-sort-open.png) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 18 components were given a real keyboard focus. 14 draw a ring: `header-shop-travel` (1px auto #101010, offset 0px), `header-signin` (1px auto #101010, offset 0px), `header-link` (1px auto #101010, offset 1px), `tab-active` (1px auto #101010, offset 1px), `tab` (1px auto #101010, offset 1px), `search-submit` (5px auto #101010, offset 2px), `tertiary-button` (1px auto #101010, offset 1px), `card-heart` (on a child layer: 1px auto #101010 offset 0px), `header-signin-search` (1px auto #101010, offset 0px), `sort-control` (1px auto #101010, offset 0px), `savings-pill` (5px auto #101010, offset 2px), `card-heart-search` (on a child layer: 1px auto #101010 offset 0px), `carousel-nav` (1px auto #101010, offset 0px), `m-search-button` (5px auto #e59700, offset 2px). 4 show the change only on a painted child layer: `field-destination` (input: border 1px solid #1668e3 `color.palette.light1.outlineFocus`, ring #1668e3 `color.palette.light1.outlineFocus` 0px 0px 0px 1px inset), `field-dates` (input: border 1px solid #1668e3 `color.palette.light1.outlineFocus`, ring #1668e3 `color.palette.light1.outlineFocus` 0px 0px 0px 1px inset), `field-travelers` (input: border 1px solid #1668e3 `color.palette.light1.outlineFocus`, ring #1668e3 `color.palette.light1.outlineFocus` 0px 0px 0px 1px inset), `m-field` (input: border 1px solid #1668e3 `color.palette.light1.outlineFocus`, ring #1668e3 `color.palette.light1.outlineFocus` 0px 0px 0px 1px inset). The header currency control could not be reached by keyboard in the static capture, so its focus state is unmeasured rather than absent.

**Pressed.** Pressed states are forced with DevTools (`:active:hover`), so no button or link ever fired. Expedia's controls react to press mostly through their scrim layers: buttons keep their fill and the overlay opacity token steps up (`--egds-button-opacity-overlay-*`), which computed styles on the root do not always show.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.2s | `ease` | opacity | carousel-nav |
| 0.275s | `ease` | box-shadow | tab, tab-active |

**Layout grid.** Read on each page at each width ([raw/layout.json](raw/layout.json)).

| Page | 1440 | 1920 | 1024 | 390 |
|---|---|---|---|---|
| home | content x 96, 1248 wide; grid 344.3 344.3 344.3 83 gap 12px | content x 336, 1248 wide; grid 344.3 344.3 344.3 83 gap 12px | content x 0, 1024 wide; grid 269.6 269.6 269.6 83 gap 12px | content x 0, 390 wide; grid 58.3 58.3 58.3 83 gap 12px |
| search | content x 96, 1248 wide; grid 1016 184 gap normal | content x 336, 1248 wide; grid 1016 184 gap normal | content x 0, 1024 wide; grid 297.3 297.3 297.3 48 gap 12px | content x 0, 390 wide; grid 79.5 79.5 79.5 79.5 gap 24px |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Search form shell](#search-form-shell) | 1200 x 252 | - | 16px | #ffffff `color.palette.light1.inverseOnSurface` | none | 0 |
| [Sign-in card](#sign-in-card) | 375 x 279 | - | 8px | #ffffff `color.palette.light1.inverseOnSurface` | rgba(12, 14, 28, 0.08) 0px 2px 12px 0px | 12px 0px |
| [Deal card](#deal-card) | 270 x 409.06 | - | 16px | #ffffff `color.palette.light1.inverseOnSurface` | none | 0 |
| [Property card](#property-card) | 756 x 232 | - | 16px | #ffffff `color.palette.light1.inverseOnSurface` | none | 0 |
| [Map card](#map-card) | 236 x 143.14 | - | 16px | #ffffff `color.palette.light1.inverseOnSurface` | none | 0 |
| [Filter column](#filter-column) | 236 x 4108 | - | 16px | #ffffff `color.palette.light1.inverseOnSurface` | none | 0 |
| [Calendar dialog](#calendar-dialog) | 652 x 558.69 | - | 8px | #ffffff `color.palette.light1.inverseOnSurface` | rgba(12, 14, 28, 0.08) 0px 2px 12px 0px | 0 |
| [Destination panel](#destination-panel) | 376 x 510 | - | 8px | #ffffff `color.palette.light1.inverseOnSurface` | rgba(12, 14, 28, 0.08) 0px 2px 12px 0px | 0 |
| [Travelers menu](#travelers-menu) | 375 x 318 | - | 8px | #ffffff `color.palette.light1.inverseOnSurface` | rgba(12, 14, 28, 0.08) 0px 2px 12px 0px | 12px 0px |
| [Deal card](#deal-card) | 342 x 483.58 | - | 16px | #ffffff `color.palette.light1.inverseOnSurface` | none | 0 |

## Components

### Header and navigation

The 72px global header: the Expedia logo, the Shop travel menu, the USD currency control, List your property, Support, Trips, the notifications bell and Sign in. The sign-in card opens through the header's no-JS checkbox mechanism; nothing navigates to a login.

#### Header
The top bar over the whole page: the Expedia logo, the "Shop travel" menu, the USD currency control, "List your property", "Support", "Trips", the notifications bell and "Sign in". Read as `header` on the home page.

**Values (default).** size 1440 x 72; background #ffffff `color.palette.light1.inverseOnSurface`; shadow rgba(12, 14, 28, 0.08) 0px 2px 12px 0px; text Centra No2 14/18 500, #191e3b `color.palette.light1.onFeatured`; icon 18 x 18, #191e3b `color.palette.light1.onFeatured`.

![Header default](components/crops/header-default.png)

#### Logo link
Read as `header-logo` on the home page.

**Values (default).** size 138 x 44; padding 8px 12px 8px 0px; background transparent; text Centra No2 16/0 400, #1668e3 `color.palette.light1.outlineFocus`.

![Logo link default](components/crops/header-logo-default.png)

#### Shop travel menu button
The nav menu trigger next to the logo: a tertiary uitk-button with a chevron. Pressed is forced; the menu is shot separately on the public page. Read as `header-shop-travel` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 128 x 36; padding 4px 16px; background transparent; text Centra No2 14/18 500, #191e3b `color.palette.light1.onFeatured`; icon 18 x 18, #191e3b `color.palette.light1.onFeatured` |
| hover | background rgba(255, 255, 255, 0) `color.palette.light1.surface_Opacity_None`; text Centra No2 14/18 500, #1668e3 `color.palette.light1.outlineFocus`; icon 18 x 18, #1668e3 `color.palette.light1.outlineFocus` |
| focus-visible | outline 1px auto #101010, offset 0px |
| pressed | background rgba(255, 255, 255, 0) `color.palette.light1.surface_Opacity_None`; text Centra No2 14/18 500, #0d4eaf `color.palette.light1.onPrimaryContainer`; icon 18 x 18, #0d4eaf `color.palette.light1.onPrimaryContainer` |

![Shop travel menu button default](components/crops/header-shop-travel-default.png) ![Shop travel menu button hover](components/crops/header-shop-travel-hover.png) ![Shop travel menu button focus-visible](components/crops/header-shop-travel-focus-visible.png) ![Shop travel menu button pressed](components/crops/header-shop-travel-pressed.png)

#### Sign in button
The account menu trigger rightmost in the header. Pressed is forced: a real click only opens the guest card, measured separately. Read as `header-signin` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 78 x 36; padding 4px 16px; background transparent; text Centra No2 14/18 500, #191e3b `color.palette.light1.onFeatured` |
| hover | background rgba(255, 255, 255, 0) `color.palette.light1.surface_Opacity_None`; text Centra No2 14/18 500, #1668e3 `color.palette.light1.outlineFocus` |
| focus-visible | outline 1px auto #101010, offset 0px |
| pressed | background rgba(255, 255, 255, 0) `color.palette.light1.surface_Opacity_None`; text Centra No2 14/18 500, #0d4eaf `color.palette.light1.onPrimaryContainer` |

![Sign in button default](components/crops/header-signin-default.png) ![Sign in button hover](components/crops/header-signin-hover.png) ![Sign in button focus-visible](components/crops/header-signin-focus-visible.png) ![Sign in button pressed](components/crops/header-signin-pressed.png)

#### Currency button
The locale/currency control in the header ("USD" + flag). Hovered and focused only. Read as `header-currency` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 92 x 36; background transparent; text Centra No2 14/18 500, #191e3b `color.palette.light1.onFeatured` |
| hover | text Centra No2 14/18 500, #1668e3 `color.palette.light1.outlineFocus` |

![Currency button default](components/crops/header-currency-default.png) ![Currency button hover](components/crops/header-currency-hover.png)

#### Header link
A plain header link ("Support"; "Trips" and "List your property" share the style): tertiary as-link buttons. Read as `header-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 88 x 36; padding 4px 16px; background transparent; text Centra No2 14/18 500, #191e3b `color.palette.light1.onFeatured` |
| hover | background rgba(255, 255, 255, 0) `color.palette.light1.surface_Opacity_None`; text Centra No2 14/18 500, #1668e3 `color.palette.light1.outlineFocus` |
| focus-visible | outline 1px auto #101010, offset 1px |

![Header link default](components/crops/header-link-default.png) ![Header link hover](components/crops/header-link-hover.png) ![Header link focus-visible](components/crops/header-link-focus-visible.png)

#### Sign-in card
The 375px guest menu the Sign in button opens: "Unlock instant savings with Member Prices", the primary Sign in button, "Learn more about One Key" and a Feedback link. Opened through the SSR checkbox mechanism; nothing was submitted. Read as `signin-card` on the home page.

**Values (open).** size 375 x 279; padding 12px 0px; radius 8px; background #ffffff `color.palette.light1.inverseOnSurface`; shadow rgba(12, 14, 28, 0.08) 0px 2px 12px 0px; text Centra No2 20/24 500, #191e3b `color.palette.light1.onFeatured`.

![Sign-in card open](components/crops/signin-card-open.png)

#### Sign-in card button
The blue primary "Sign in" button inside the guest card. Hovered only, never pressed. Read as `signin-card-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| open (same: hover) | size 327 x 36; padding 4px 16px; radius 40000px; background transparent; text Centra No2 16/20 500, #ffffff `color.palette.light1.inverseOnSurface` |

Child layers that carry the look: a::before 327pxx36px background #0e3672 `color.palette.light1.primaryVariant` radius 40000px; a::after 327pxx36px background #1668e3 `color.palette.light1.outlineFocus` radius 40000px.

![Sign-in card button open](components/crops/signin-card-button-open.png) ![Sign-in card button hover](components/crops/signin-card-button-hover.png)

### Search form

The multi-product search card under the hero: the product tabs (Stays, Flights, Cars, Packages, Things to do, Cruises), the three uitk-field triggers (Where to?, Dates, Travelers), the blue Search button and the bundle checkbox.

#### Search form shell
The white rounded card under the hero holding the product tabs and the three search fields with the Search button. Read as `search-shell` on the home page.

**Values (default).** size 1200 x 252; background transparent; text Centra No2 14/18 500, #1668e3 `color.palette.light1.outlineFocus`; icon 24 x 24, #191e3b `color.palette.light1.onFeatured`.

Child layers that carry the look: div 1200x252 background #ffffff `color.palette.light1.inverseOnSurface` radius 16px; div::before 1200pxx252px border 1px solid #dfe0e4 `color.palette.light1.outlineVariant` radius 16px; ul 1200x110 background #ffffff `color.palette.light1.inverseOnSurface` radius 16px 16px 0px 0px shadow #dfe0e4 `color.palette.light1.outlineVariant` 0px 1px 0px 0px.

![Search form shell default](components/crops/search-shell-default.png)

#### Product tabs
The tab rail atop the form: Stays, Flights, Cars, Packages, Things to do, Cruises, each an icon over a label. Read as `search-tabs` on the home page.

**Values (default).** size 1200 x 110; radius 16px 16px 0px 0px; background #ffffff `color.palette.light1.inverseOnSurface`; shadow #dfe0e4 0px 1px 0px 0px; text Centra No2 14/18 500, #1668e3 `color.palette.light1.outlineFocus`.

![Product tabs default](components/crops/search-tabs-default.png)

#### Product tab (active)
The current product tab (Stays): label and icon in the primary blue with a 2px underline. Read as `tab-active` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 96 x 110; padding 0px 24px; background transparent; shadow #1668e3 0px -2px 0px 0px inset; text Centra No2 14/18 500, #1668e3 `color.palette.light1.outlineFocus` |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | shadow none; transition box-shadow 0.275s ease |

![Product tab (active) default](components/crops/tab-active-default.png) ![Product tab (active) hover](components/crops/tab-active-hover.png) ![Product tab (active) focus-visible](components/crops/tab-active-focus-visible.png) ![Product tab (active) pressed](components/crops/tab-active-pressed.png)

#### Product tab
A resting product tab (Flights). Pressed is forced: a real click switches the form, shot separately on the hydrated page. Read as `tab` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 96 x 110; padding 0px 24px; background transparent; text Centra No2 14/18 500, #191e3b `color.palette.light1.onFeatured` |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | shadow #191e3b 0px -4px 0px 0px inset; transition box-shadow 0.275s ease |

![Product tab default](components/crops/tab-default.png) ![Product tab hover](components/crops/tab-hover.png) ![Product tab focus-visible](components/crops/tab-focus-visible.png) ![Product tab pressed](components/crops/tab-pressed.png)

#### Destination field
The "Where to?" field: a uitk-field box with floated label, pin icon and empty input; once hydrated its trigger button opens the destination panel. Pressed is forced. Read as `field-destination` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 344.33 x 48; background transparent; text Centra No2 16/20 400, #191e3b `color.palette.light1.onFeatured`; icon 24 x 24, #191e3b `color.palette.light1.onFeatured` |
| focus-visible | text Centra No2 12/16 400, #191e3b `color.palette.light1.onFeatured` |

Child layers that carry the look: input 344.3x48 background #ffffff `color.palette.light1.inverseOnSurface` border 1px solid #818494 `color.palette.light1.outline` radius 8px.

![Destination field default](components/crops/field-destination-default.png) ![Destination field hover](components/crops/field-destination-hover.png) ![Destination field focus-visible](components/crops/field-destination-focus-visible.png) ![Destination field pressed](components/crops/field-destination-pressed.png)

#### Dates field
The "Dates" field with the range value (Fri, Feb 13 - Tue, Feb 17) and a calendar icon. Pressed is forced: a click opens the calendar. Read as `field-dates` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 344.33 x 48; background transparent; text Centra No2 12/16 400, #191e3b `color.palette.light1.onFeatured`; icon 24 x 24, #191e3b `color.palette.light1.onFeatured` |
| focus-visible | child paint input: border 1px solid #1668e3 `color.palette.light1.outlineFocus`, ring #1668e3 `color.palette.light1.outlineFocus` 0px 0px 0px 1px inset |

Child layers that carry the look: input 344.3x48 background #ffffff `color.palette.light1.inverseOnSurface` border 1px solid #818494 `color.palette.light1.outline` radius 8px.

![Dates field default](components/crops/field-dates-default.png) ![Dates field hover](components/crops/field-dates-hover.png) ![Dates field focus-visible](components/crops/field-dates-focus-visible.png) ![Dates field pressed](components/crops/field-dates-pressed.png)

#### Travelers field
The "Travelers" field ("2 travelers, 1 room") with a person icon. Pressed is forced: a click opens the room picker. Read as `field-travelers` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 344.34 x 48; background transparent; text Centra No2 12/16 400, #191e3b `color.palette.light1.onFeatured`; icon 24 x 24, #191e3b `color.palette.light1.onFeatured` |
| focus-visible | child paint input: border 1px solid #1668e3 `color.palette.light1.outlineFocus`, ring #1668e3 `color.palette.light1.outlineFocus` 0px 0px 0px 1px inset |

Child layers that carry the look: input 344.3x48 background #ffffff `color.palette.light1.inverseOnSurface` border 1px solid #818494 `color.palette.light1.outline` radius 8px.

![Travelers field default](components/crops/field-travelers-default.png) ![Travelers field hover](components/crops/field-travelers-hover.png) ![Travelers field focus-visible](components/crops/field-travelers-focus-visible.png) ![Travelers field pressed](components/crops/field-travelers-pressed.png)

#### Search button
The primary Search button at the form's right end (uitk-button-primary-large). Pressed is forced: a real press would run a search. Read as `search-submit` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 83 x 48; padding 4px 16px; radius 40000px; background transparent; text Centra No2 16/20 500, #ffffff `color.palette.light1.inverseOnSurface` |
| focus-visible | outline 5px auto #101010, offset 2px |

Child layers that carry the look: button::before 83pxx48px background #0e3672 `color.palette.light1.primaryVariant` radius 40000px; button::after 83pxx48px background #1668e3 `color.palette.light1.outlineFocus` radius 40000px.

![Search button default](components/crops/search-submit-default.png) ![Search button hover](components/crops/search-submit-hover.png) ![Search button focus-visible](components/crops/search-submit-focus-visible.png) ![Search button pressed](components/crops/search-submit-pressed.png)

#### Bundle & Save checkbox
The "Add a flight to Bundle & Save*" checkbox under the fields: an uitk-checkbox box plus label. Read as `bundle-checkbox` on the home page.

**Values (default).** size 1152 x 34; background transparent; text Centra No2 14/18 400, #191e3b `color.palette.light1.onFeatured`.

Child layers that carry the look: input 18x18 background #ffffff `color.palette.light1.inverseOnSurface`; span 18x18 background #ffffff `color.palette.light1.inverseOnSurface` border 2px solid #818494 `color.palette.light1.outline` radius 4px; span::before 18pxx18px border 1px solid transparent radius 4px.

![Bundle & Save checkbox default](components/crops/bundle-checkbox-default.png)

#### Tertiary button
The "See all deals" button by the deals heading: outlined tertiary uitk-button. Pressed is forced, never followed. Read as `tertiary-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 128 x 36; padding 4px 16px; border 1px solid #818494 `color.palette.light1.outline`; radius 40000px; background #ffffff `color.palette.light1.inverseOnSurface`; text Centra No2 16/20 500, #1668e3 `color.palette.light1.outlineFocus` |
| hover | background #ecf4fd `color.palette.light1.secondaryContainerVariant`; text Centra No2 16/20 500, #0d4eaf `color.palette.light1.onPrimaryContainer` |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | background #ecf4fd `color.palette.light1.secondaryContainerVariant`; text Centra No2 16/20 500, #0d4eaf `color.palette.light1.onPrimaryContainer` |

![Tertiary button default](components/crops/tertiary-button-default.png) ![Tertiary button hover](components/crops/tertiary-button-hover.png) ![Tertiary button focus-visible](components/crops/tertiary-button-focus-visible.png) ![Tertiary button pressed](components/crops/tertiary-button-pressed.png)

### Menus and dialogs

What the search fields open, measured on the same page hydrated with Expedia's own JavaScript: the two-month calendar dialog with its range chips, the travellers stepper menu and the Where-to destination panel.

#### Calendar dialog
The date picker the Dates field opens: Calendar/Flexible dates tabs, the range line, two months, weekday headings, the selected range endpoints as filled blue days, the ±day flexibility chips and the Done button. Opened by clicking the field trigger; Escape closed it, nothing was searched. Read as `calendar-dialog` on the home (hydrated) page.

**Values (open).** size 652 x 558.69; radius 8px; background #ffffff `color.palette.light1.inverseOnSurface`; shadow rgba(12, 14, 28, 0.08) 0px 2px 12px 0px; text Centra No2 14/18 500, #1668e3 `color.palette.light1.outlineFocus`; icon 18 x 18, #191e3b `color.palette.light1.onFeatured`.

![Calendar dialog open](components/crops/calendar-dialog-open.png)

#### Calendar day (selected)
A range endpoint in the calendar: the filled primary circle. Read as `calendar-day-selected` on the home (hydrated) page.

**Values (open).** size 40.84 x 40.94; background transparent; text Centra No2 14/18 700, #ffffff `color.palette.light1.inverseOnSurface`.

Child layers that carry the look: div 40.8x40.9 image linear-gradient(to right, transparent 50%, #ecf4fd `color.palette.light1.secondaryContaine; div 40.8x40.9 background #1668e3 `color.palette.light1.outlineFocus` radius 40000px.

![Calendar day (selected) open](components/crops/calendar-day-selected-open.png)

#### Flexibility chip
The "Exact dates" / "± N days" chips under the calendar: outlined pills, the active one filled. Read as `calendar-chip` on the home (hydrated) page.

**Values (open).** size 69 x 32; padding 0px 12px; radius 40000px; background #ffffff `color.palette.light1.inverseOnSurface`; shadow #818494 0px 0px 0px 1px inset; text Centra No2 12/16 400, #191e3b `color.palette.light1.onFeatured`.

![Flexibility chip open](components/crops/calendar-chip-open.png)

#### Dialog Done button
The primary Done button at the foot of the calendar. Hovered only, never pressed. Read as `dialog-done` on the home (hydrated) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| open (same: hover) | size 72 x 36; padding 4px 16px; radius 40000px; background transparent; text Centra No2 16/20 500, #ffffff `color.palette.light1.inverseOnSurface` |

Child layers that carry the look: button::before 72pxx36px background #0e3672 `color.palette.light1.primaryVariant` radius 40000px; button::after 72pxx36px background #1668e3 `color.palette.light1.outlineFocus` radius 40000px.

![Dialog Done button open](components/crops/dialog-done-open.png) ![Dialog Done button hover](components/crops/dialog-done-hover.png)

#### Travelers menu
The room picker the Travelers field opens: "Room 1", the Adults and Children steppers (−/+), "Add another room", the group-booking line and Done. Opened by clicking the field trigger; Escape closed it. Read as `travelers-menu` on the home (hydrated) page.

**Values (open).** size 375 x 318; padding 12px 0px; radius 8px; background #ffffff `color.palette.light1.inverseOnSurface`; shadow rgba(12, 14, 28, 0.08) 0px 2px 12px 0px; text Centra No2 14/18 500, #191e3b `color.palette.light1.onFeatured`; icon 24 x 16, #000000.

![Travelers menu open](components/crops/travelers-menu-open.png)

#### Destination panel
The panel the Where to? field opens: the prompt, the magnifier and the "Search by destination, accommodations, or landmark" input. Opened by clicking the field trigger. Read as `whereto-panel` on the home (hydrated) page.

**Values (open).** size 376 x 510; radius 8px; background #ffffff `color.palette.light1.inverseOnSurface`; shadow rgba(12, 14, 28, 0.08) 0px 2px 12px 0px; text Centra No2 14/18 400, #191e3b `color.palette.light1.onFeatured`; icon 48 x 48, #191e3b `color.palette.light1.onFeatured`.

![Destination panel open](components/crops/whereto-panel-open.png)

#### Destination input
The free-text destination field inside the panel; text was typed and deleted, nothing searched. Read as `whereto-input` on the home (hydrated) page.

**Values (filled).** size 376 x 72; padding 16px 48px 0px 24px; border B: 1px solid #dfe0e4 `color.palette.light1.outlineVariant`; background transparent; text Centra No2 28/32 700, #191e3b `color.palette.light1.onFeatured`; placeholder #676a7d `color.palette.light1.onSurfaceVariant`.

Child layers that carry the look: input 376x72 border 1px solid #dfe0e4 `color.palette.light1.outlineVariant`.

![Destination input filled](components/crops/whereto-input-filled.png)

### Home content

Below the search shell: the Reckless XPD hero title, the marketing-3 re-themed promo band, the deals carousels of cards with save hearts, and the footer.

#### Hero title
"The one place you go to go places" over the hero photo: the display type style in Reckless XPD, inverse colour. Read as `hero-title` on the home page.

**Values (default).** size 659 x 49; background transparent; text Reckless XPD 44/40 400, #ffffff `color.palette.light1.inverseOnSurface`.

![Hero title default](components/crops/hero-title-default.png)

#### Marketing band
The section re-themed data-theme-light="marketing-3": the pale-blue palette applied to the same components (the promo strip under the search form). Read as `marketing-band` on the home page.

**Values (default).** size 1200 x 72; background transparent; text Centra No2 16/20 500, #191e3b `color.palette.marketing3.inverseSurface`; icon 24 x 24, #191e3b `color.palette.marketing3.inverseSurface`.

Child layers that carry the look: div 1200x72 background #b7cddc `color.palette.marketing3.surface` radius 16px.

![Marketing band default](components/crops/marketing-band-default.png)

#### Deal card
One card in the deals carousels: a uitk-card with rounded corners, the gallery photo, a heart save button, the property name and the price. Read as `deal-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 270 x 409.06; radius 16px; background #ffffff `color.palette.light1.inverseOnSurface`; text Centra No2 16/20 500, #191e3b `color.palette.light1.onFeatured`; icon 18 x 18, #191e3b `color.palette.light1.onFeatured` |

![Deal card default](components/crops/deal-card-default.png) ![Deal card hover](components/crops/deal-card-hover.png)

#### Save (heart) button
The heart save control over a card photo: a round white button, pressed state forced so nothing is saved. Read as `card-heart` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 48 x 48; background transparent; text Centra No2 16/normal 400, #191e3b `color.palette.light1.onFeatured`; icon 24 x 24, #000000 |
| focus-visible | child paint button: outline 1px auto #101010 offset 0px |

Child layers that carry the look: button 32x32 background #ffffff `color.palette.light1.inverseOnSurface` radius 40000px.

![Save (heart) button default](components/crops/card-heart-default.png) ![Save (heart) button hover](components/crops/card-heart-hover.png) ![Save (heart) button focus-visible](components/crops/card-heart-focus-visible.png) ![Save (heart) button pressed](components/crops/card-heart-pressed.png)

#### Footer link
A link in the page footer. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 150 x 21; background transparent; text Centra No2 16/normal 400, #1668e3 `color.palette.light1.outlineFocus` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png)

### Hotel results

The Hotel-Search results page: the compact sticky search form, the stay-type segmented control, the sort pill, the filter rail with its map card, and the result cards with gallery, VIP badge, rating, savings pill and price block.

#### Sticky search form
The compact search bar pinned under the header on the results page: the same three fields plus the round search button. Read as `search-form-sticky` on the hotel results page.

**Values (default).** size 1016 x 48; background transparent; text Centra No2 12/16 400, #191e3b `color.palette.light1.onFeatured`; icon 24 x 24, #191e3b `color.palette.light1.onFeatured`.

Child layers that carry the look: input 310.7x48 background #ffffff `color.palette.light1.inverseOnSurface` border 1px solid #818494 `color.palette.light1.outline` radius 8px; input 310.7x48 background #ffffff `color.palette.light1.inverseOnSurface` border 1px solid #818494 `color.palette.light1.outline` radius 8px; input 310.7x48 background #ffffff `color.palette.light1.inverseOnSurface` border 1px solid #818494 `color.palette.light1.outline` radius 8px.

![Sticky search form default](components/crops/search-form-sticky-default.png)

#### Sign in button (results)
Read as `header-signin-search` on the hotel results page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 78 x 36; padding 4px 16px; background transparent; text Centra No2 14/18 500, #191e3b `color.palette.light1.onFeatured` |
| hover | background rgba(255, 255, 255, 0) `color.palette.light1.surface_Opacity_None`; text Centra No2 14/18 500, #1668e3 `color.palette.light1.outlineFocus` |
| focus-visible | outline 1px auto #101010, offset 0px |

![Sign in button (results) default](components/crops/header-signin-search-default.png) ![Sign in button (results) hover](components/crops/header-signin-search-hover.png) ![Sign in button (results) focus-visible](components/crops/header-signin-search-focus-visible.png)

#### Stay type tabs
The segmented "All stays / Hotels / Homes" control above the results. Read as `stay-type-tabs` on the hotel results page.

**Values (default).** size 756 x 44; padding 4px; radius 40000px; background #eff3f7 `color.palette.light1.surfaceContainerVariant`; text Centra No2 14/18 500, #191e3b `color.palette.light1.onFeatured`; icon 18 x 18, #191e3b `color.palette.light1.onFeatured`.

![Stay type tabs default](components/crops/stay-type-tabs-default.png)

#### Sort control
The "Sort by recommended for you" uitk-pill over the results list. Hovered and focused only, never opened. Read as `sort-control` on the hotel results page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 222 x 32; padding 0px 12px; radius 40000px; background #ffffff `color.palette.light1.inverseOnSurface`; shadow #818494 0px 0px 0px 1px inset; text Centra No2 12/16 400, #191e3b `color.palette.light1.onFeatured`; icon 24 x 16, #191e3b `color.palette.light1.onFeatured` |
| hover | background #ecf4fd `color.palette.light1.secondaryContainerVariant` |
| focus-visible | outline 1px auto #101010, offset 0px |

![Sort control default](components/crops/sort-control-default.png) ![Sort control hover](components/crops/sort-control-hover.png) ![Sort control focus-visible](components/crops/sort-control-focus-visible.png)

#### Results count
The "N properties" line over the results list. Read as `results-summary` on the hotel results page.

**Values (default).** size 81 x 16; background transparent; text Centra No2 12/16 400, #191e3b `color.palette.light1.onFeatured`.

![Results count default](components/crops/results-summary-default.png)

#### Property card
One result card (uitk-card): the 21:9 photo gallery with carousel arrows and the heart, VIP badge, name, amenity icons, refund line, rating pill, nightly and total prices, and the "Sign in for extra savings" pill. Read as `property-card` on the hotel results page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 756 x 232; radius 16px; background #ffffff `color.palette.light1.inverseOnSurface`; text Centra No2 12/18 500, #ffffff `color.palette.light1.inverseOnSurface`; icon 24 x 24, #ffffff `color.palette.light1.inverseOnSurface` |

![Property card default](components/crops/property-card-default.png) ![Property card hover](components/crops/property-card-hover.png)

#### Card gallery
The 21:9 image carousel in a result card with prev/next circle buttons. Read as `card-gallery` on the hotel results page.

**Values (default).** size 252 x 232; background transparent; text Centra No2 14/18 400, #191e3b `color.palette.light1.onFeatured`; icon 24 x 24, #ffffff `color.palette.light1.inverseOnSurface`.

Child layers that carry the look: div 252x232 background #c8dff9 `color.palette.light1.primaryContainer` image url(data:…); div 252x232 background #c8dff9 `color.palette.light1.primaryContainer` image url(data:…); div 252x232 background #c8dff9 `color.palette.light1.primaryContainer` image url(data:…).

![Card gallery default](components/crops/card-gallery-default.png)

#### Price block
The right-aligned price area of a result card: the struck list price, the nightly rate in the headline size, and the total with taxes in muted text. Read as `price-block` on the hotel results page.

**Values (default).** size 183 x 62; background transparent; text Centra No2 16/20 400, #191e3b `color.palette.light1.onFeatured`.

![Price block default](components/crops/price-block-default.png)

#### Rating pill
The guest rating on a card: the score chip (9.4) in positive green beside the word and the review count. Read as `rating-pill` on the hotel results page.

**Values (default).** size 244.19 x 34; background transparent; text Centra No2 14/18 500, #191e3b `color.palette.light1.onFeatured`.

![Rating pill default](components/crops/rating-pill-default.png)

#### "Sign in for extra savings" pill
The filled primary-blue pill button with white text on each card pointing signed-out guests at member prices (the fill paints on its ::after layer). Hovered and focused only, never followed. Read as `savings-pill` on the hotel results page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 183 x 32; padding 4px 12px; radius 40000px; background transparent; text Centra No2 12/16 500, #ffffff `color.palette.light1.inverseOnSurface`; icon 16 x 16, #ffffff `color.palette.light1.inverseOnSurface` |
| focus-visible | outline 5px auto #101010, offset 2px |

Child layers that carry the look: a::before 183pxx32px background #0e3672 `color.palette.light1.primaryVariant` radius 40000px; a::after 183pxx32px background #1668e3 `color.palette.light1.outlineFocus` radius 40000px.

!["Sign in for extra savings" pill default](components/crops/savings-pill-default.png) !["Sign in for extra savings" pill hover](components/crops/savings-pill-hover.png) !["Sign in for extra savings" pill focus-visible](components/crops/savings-pill-focus-visible.png)

#### VIP Access badge
The dark "VIP Access" chip pinned over the card photo. Read as `vip-badge` on the hotel results page.

**Values (default).** size 77 x 24; padding 0px 8px; radius 4px; background #191e3b `color.palette.light1.onFeatured`; text Centra No2 12/18 500, #ffffff `color.palette.light1.inverseOnSurface`.

![VIP Access badge default](components/crops/vip-badge-default.png)

#### Save (heart) button
The heart over the card photo. Pressed is forced; nothing was saved. Read as `card-heart-search` on the hotel results page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 48 x 48; background transparent; text Centra No2 14/18 400, #191e3b `color.palette.light1.onFeatured`; icon 24 x 24, #000000 |
| focus-visible | child paint button: outline 1px auto #101010 offset 0px |

Child layers that carry the look: button 32x32 background #ffffff `color.palette.light1.inverseOnSurface` radius 40000px.

![Save (heart) button default](components/crops/card-heart-search-default.png) ![Save (heart) button hover](components/crops/card-heart-search-hover.png) ![Save (heart) button focus-visible](components/crops/card-heart-search-focus-visible.png) ![Save (heart) button pressed](components/crops/card-heart-search-pressed.png)

#### Carousel arrow
A round prev/next button in the card gallery (uitk-button-paging). Hovered and focused only. Read as `carousel-nav` on the hotel results page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 32 x 32; radius 40000px; background transparent; shadow rgba(12, 14, 28, 0.08) 0px 2px 12px 0px; text Centra No2 16/20 500, #ffffff `color.palette.light1.inverseOnSurface`; transition opacity 0.2s ease; icon 24 x 24, #ffffff `color.palette.light1.inverseOnSurface` |
| focus-visible | outline 1px auto #101010, offset 0px |

![Carousel arrow default](components/crops/carousel-nav-default.png) ![Carousel arrow hover](components/crops/carousel-nav-hover.png) ![Carousel arrow focus-visible](components/crops/carousel-nav-focus-visible.png)

#### Amenity line
One amenity row on a card: a small icon and a muted label. Read as `amenity-item` on the hotel results page.

**Values (default).** size 91 x 22; background transparent; text Centra No2 12/16 400, #191e3b `color.palette.light1.onFeatured`; icon 18 x 18, #191e3b `color.palette.light1.onFeatured`.

![Amenity line default](components/crops/amenity-item-default.png)

#### Filter column
The left filter rail: "Search by property name", "Filter by" groups (Property class checkboxes, Guest rating radios), See more links. Read as `filters` on the hotel results page.

**Values (default).** size 236 x 4108; background transparent; text Centra No2 14/18 400, #191e3b `color.palette.light1.onFeatured`; icon 16 x 16, #191e3b `color.palette.light1.onFeatured`.

Child layers that carry the look: div 236x78 background #ffffff `color.palette.light1.inverseOnSurface` radius 16px; div::before 236pxx78px border 1px solid #dfe0e4 `color.palette.light1.outlineVariant` radius 16px; div 48x24 background #676a7d `color.palette.light1.onSurfaceVariant` border 2px solid #676a7d `color.palette.light1.onSurfaceVariant` radius 12px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Property name field
The "e.g. Marriott" text input in the filter rail. Clicked into only. Read as `name-field` on the hotel results page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 236 x 48; background transparent; text Centra No2 16/20 400, #191e3b `color.palette.light1.onFeatured`; icon 24 x 24, #191e3b `color.palette.light1.onFeatured` |
| focused | text Centra No2 12/16 400, #191e3b `color.palette.light1.onFeatured` |

Child layers that carry the look: input 236x48 background #ffffff `color.palette.light1.inverseOnSurface` border 1px solid #818494 `color.palette.light1.outline` radius 8px.

![Property name field focused](components/crops/name-field-focused.png)

#### Filter checkbox
A "Property class" checkbox in the filter rail: an uitk-checkbox box with its count-bearing label. Hovered only, never toggled. Read as `filter-checkbox` on the hotel results page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 240 x 34; padding 8px 4px; background transparent; text Centra No2 14/18 400, #191e3b `color.palette.light1.onFeatured` |
| hover | child paint span: border 2px solid #1668e3 `color.palette.light1.outlineFocus`, ring #1668e3 `color.palette.light1.outlineFocus` 0px 0px 0px 0px |

Child layers that carry the look: input 18x18 background #ffffff `color.palette.light1.inverseOnSurface`; span 18x18 background #ffffff `color.palette.light1.inverseOnSurface` border 2px solid #818494 `color.palette.light1.outline` radius 4px; span::before 18pxx18px border 1px solid transparent radius 4px.

![Filter checkbox default](components/crops/filter-checkbox-default.png) ![Filter checkbox hover](components/crops/filter-checkbox-hover.png)

#### Compare switch
The "Compare properties" toggle over the filter rail. Hovered only, never switched. Read as `compare-switch` on the hotel results page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 212 x 54; background transparent; text Centra No2 14/18 400, #191e3b `color.palette.light1.onFeatured`; icon 16 x 16, #191e3b `color.palette.light1.onFeatured` |

Child layers that carry the look: div 48x24 background #676a7d `color.palette.light1.onSurfaceVariant` border 2px solid #676a7d `color.palette.light1.onSurfaceVariant` radius 12px; div::before 20pxx20px border 2px solid transparent radius 50%; div 20x20 background #ffffff `color.palette.light1.inverseOnSurface` radius 50%.

![Compare switch default](components/crops/compare-switch-default.png) ![Compare switch hover](components/crops/compare-switch-hover.png)

#### Urgency note
"We have 1 left at this price" under a price: the critical-coloured nudge line. Read as `urgency-note` on the hotel results page.

**Values (default).** size 183 x 16; background transparent; text Centra No2 12/16 400, #a7183c `color.palette.light1.critical`.

![Urgency note default](components/crops/urgency-note-default.png)

#### Refund note
"Fully refundable" / "Reserve now, pay later" in positive green. Read as `refund-note` on the hotel results page.

**Values (default).** size 287.19 x 18; background transparent; text Centra No2 14/18 400, #227950 `color.palette.light1.positive`.

![Refund note default](components/crops/refund-note-default.png)

#### Map card
The static map tile card at the top of the filter rail ("View in a map"). Read as `map-card` on the hotel results page.

**Values (default).** size 236 x 143.14; radius 16px; background #ffffff `color.palette.light1.inverseOnSurface`; text Centra No2 14/18 400, #1668e3 `color.palette.light1.outlineFocus`.

![Map card default](components/crops/map-card-default.png)

### Mobile (390 wide)

A few components as a phone draws them, at 390 x 844 at 2x.

#### Header
The mobile top bar. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 56; background #ffffff `color.palette.light1.inverseOnSurface`; shadow rgba(12, 14, 28, 0.08) 0px 2px 12px 0px; text Centra No2 14/18 500, #191e3b `color.palette.light1.onFeatured`; icon 18 x 18, #191e3b `color.palette.light1.onFeatured`.

![Header default](components/crops/m-header-default.png)

#### Hero title
Read as `m-hero-title` on the home page at 390 wide.

**Values (default).** size 277 x 135; background transparent; text Reckless XPD 44/40 400, #ffffff `color.palette.light1.inverseOnSurface`.

![Hero title default](components/crops/m-hero-title-default.png)

#### Search form
Read as `m-search-shell` on the home page at 390 wide.

**Values (default).** size 342 x 252; background transparent; text Centra No2 14/18 500, #1668e3 `color.palette.light1.outlineFocus`; icon 24 x 24, #191e3b `color.palette.light1.onFeatured`.

Child layers that carry the look: div 342x252 background #ffffff `color.palette.light1.inverseOnSurface` radius 16px; div::before 342pxx252px border 1px solid #dfe0e4 `color.palette.light1.outlineVariant` radius 16px; ul 342x110 background #ffffff `color.palette.light1.inverseOnSurface` radius 16px 16px 0px 0px shadow #dfe0e4 `color.palette.light1.outlineVariant` 0px 1px 0px 0px.

![Search form default](components/crops/m-search-shell-default.png)

#### Search field
The first search field at 390 wide. Read as `m-field` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 58.33 x 48; background transparent; text Centra No2 16/normal 400, #191e3b `color.palette.light1.onFeatured`; icon 24 x 24, #191e3b `color.palette.light1.onFeatured` |
| focus-visible | child paint input: border 1px solid #1668e3 `color.palette.light1.outlineFocus`, ring #1668e3 `color.palette.light1.outlineFocus` 0px 0px 0px 1px inset |

Child layers that carry the look: input 58.3x48 background #ffffff `color.palette.light1.inverseOnSurface` border 1px solid #818494 `color.palette.light1.outline` radius 8px.

![Search field default](components/crops/m-field-default.png) ![Search field hover](components/crops/m-field-hover.png) ![Search field focus-visible](components/crops/m-field-focus-visible.png) ![Search field pressed](components/crops/m-field-pressed.png)

#### Search button
Read as `m-search-button` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 83 x 48; padding 4px 16px; radius 40000px; background transparent; text Centra No2 16/20 500, #ffffff `color.palette.light1.inverseOnSurface` |
| focus-visible | outline 5px auto #e59700, offset 2px |

Child layers that carry the look: button::before 83pxx48px background #0e3672 `color.palette.light1.primaryVariant` radius 40000px; button::after 83pxx48px background #1668e3 `color.palette.light1.outlineFocus` radius 40000px.

![Search button default](components/crops/m-search-button-default.png) ![Search button hover](components/crops/m-search-button-hover.png) ![Search button focus-visible](components/crops/m-search-button-focus-visible.png) ![Search button pressed](components/crops/m-search-button-pressed.png)

#### Deal card
Read as `m-card` on the home page at 390 wide.

**Values (default).** size 342 x 483.58; radius 16px; background #ffffff `color.palette.light1.inverseOnSurface`; text Centra No2 16/20 500, #191e3b `color.palette.light1.onFeatured`; icon 24 x 24, #ffffff `color.palette.light1.inverseOnSurface`.

![Deal card default](components/crops/m-card-default.png)
## Gaps

### Pages

- **The live site.** expedia.com answers every automated request with a 429 "Bot or Not?" challenge (headless and headed, several user agents, regional domains). The DOM evidence is therefore a Wayback snapshot: fresh component styles come from live CDN CSS, but a page that changed after the snapshot or that the archive renders differently is not covered. Flights, cars, packages, things-to-do and cruise results pages were not captured.
- **Signed-in pages.** Nothing behind sign-in: trips, loyalty account, member pricing, checkout and booking, settings. The header sign-in card was measured at rest; its links were never followed.
- **Anything that sends or creates.** No search was submitted (the results page is an archived capture of someone else's public query), no booking started, no sort order applied, no destination typed and kept, no filter toggled.
- **Hydrated results.** On the archived search page the app's own JS refetches its GraphQL and empties regions, so the results page was measured statically; the sort pill's open state is a screenshot only.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **The header currency control** could not be reached by keyboard focus in the static capture; its focus-visible state is unmeasured.
- **The checkbox, switch and radio states** were read resting and hovered only; nothing was toggled.
- **Disabled states** were not seen on any public control except the stay-type segmented options, which render selected-and-disabled at rest.

### Themes

The pages pin `data-theme-light="light-1"` on the body; `prefers-color-scheme: dark` changes nothing (`themeChecks` in [raw/css-vars.json](raw/css-vars.json)). The promo sections re-theme to `marketing-3` via their own `data-theme-light` attribute. The stylesheets also ship `dark-1`, `dark-2`, `bright-1`, `marketing-1`, `marketing-2`, `ai-local-1`, `romie` and eight global-loyalty palettes; tokens.json holds sets for the five themes resolved on the pages (light-1, dark-1, dark-2, marketing-3, bright-1) and every palette literal in `core.color.palette`.

### Fonts

- **Centra No2** (the UI face) and **Reckless XPD** (the display face) are Expedia's proprietary fonts, served from travel-assets.com; they loaded during the capture, so measurements name the real faces. The style guide falls back to the system stack without the font files.

### Screenshots

- Hotel photos, destination imagery and the hero are Expedia's and the properties' content and appear only inside screenshots and crops.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- No personal data was captured: the pages are public signed-out surfaces, and the archived search results carry no account information.
