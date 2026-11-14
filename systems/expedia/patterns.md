# Expedia patterns

How Expedia's components combine to do the recurring jobs on its public pages, written from the capture of 2026-11-13 (signed out, 1440 and 390 wide, headless Chromium; Wayback snapshots of www.expedia.com painted with live travel-assets.com CSS — see the Gaps in [components.md](components.md)). Each pattern says when Expedia uses it, the components it is built from (entries in [components.md](components.md), values in [tokens.json](tokens.json)), the layout, and the screens that show it. These are observations of what the product does, not Expedia's own guidance.

| Pattern | Captured | Example screen |
|---|---|---|
| [The global header](#the-global-header) | yes, sign-in card open | [home-light-signin-open](screenshots/home-light-signin-open.png) |
| [The multi-product search card](#the-multi-product-search-card) | yes, three field panels open | [home-i-light-calendar-open](screenshots/home-i-light-calendar-open.png) |
| [Marketing bands that re-theme](#marketing-bands-that-re-theme) | yes | [home-light-full](screenshots/home-light-full.png) |
| [Deals carousels and save hearts](#deals-carousels-and-save-hearts) | yes | [home-light-default](screenshots/home-light-default.png) |
| [Results page: rail plus cards](#results-page-rail-plus-cards) | yes, statically | [search-light-default](screenshots/search-light-default.png) |
| [The property result card](#the-property-result-card) | yes | [search-light-full](screenshots/search-light-full.png) |
| [Mobile shell](#mobile-shell) | yes | [mobile-home-light-default](screenshots/mobile-home-light-default.png) |
| [Feedback after an action](#feedback-after-an-action) | partial — hover, focus and forced press only | [card-heart crops](components/crops/card-heart-pressed.png) |
| [Empty, loading and error states](#empty-loading-and-error-states) | no | — |

## The global header

**When.** Every page: home and results alike. A 72px white bar with a hairline `outline-variant` #DFE0E4 bottom border — logo left, then the Shop travel menu, USD currency control, List your property, Support, Trips, the notifications bell and Sign in pushed right.

**Components.** [Header](components.md#header), [Logo link](components.md#logo-link), [Shop travel menu button](components.md#shop-travel-menu-button), [Currency button](components.md#currency-button), [Header link](components.md#header-link), [Sign in button](components.md#sign-in-button), [Sign-in card](components.md#sign-in-card).

**Layout.** Text buttons at 14/18 medium, resting transparent and hovering to `primary`-blue text on the same transparent ground inside a pill radius; the menu triggers carry a chevron. Sign in opens a 375 x 279 menu card (8px radius, `0 2px 12px` shadow at 8% ink — the `menu.container` elevation, not `elevation.8`) anchored under the bar through the header's no-JS checkbox mechanism — a headline, the member-benefits line and a full-width 36px primary `egds.primary` button, with "Create a free account" under it. The Shop travel menu opens the same way. Keyboard focus draws a 1px #101010 outline.

**Screens.** [home-light-default](screenshots/home-light-default.png), [home-light-signin-open](screenshots/home-light-signin-open.png), [home-light-shoptravel-open](screenshots/home-light-shoptravel-open.png), [search-light-default](screenshots/search-light-default.png).

## The multi-product search card

**When.** The home page's hero act — the one control every Expedia flow starts from. It repeats, compacted to a single 1016 x 48 row, at the top of the results page.

**Components.** [Search form shell](components.md#search-form-shell), [Product tabs](components.md#product-tabs), [Product tab](components.md#product-tab), [Destination field](components.md#destination-field), [Dates field](components.md#dates-field), [Travelers field](components.md#travelers-field), [Search button](components.md#search-button), [Bundle & Save checkbox](components.md#bundle--save-checkbox), and the opened [Calendar dialog](components.md#calendar-dialog), [Travelers menu](components.md#travelers-menu) and [Destination panel](components.md#destination-panel).

**Layout.** A 1200 x 252 `uitk-card` over the hero photo: a row of product tabs (Stays active, then Flights, Cars, Packages, Things to do, Cruises — the active tab inks `primary` with a 3px underline), then a 4-column grid of three 344 x 48 `uitk-field` triggers and the 83 x 48 Search button. Fields are 8px-radius boxes on white, icon + bold label; the Search button is the `egds.primary` #1668E3 pill. Under the row a Bundle & Save checkbox offers the flight+hotel upsell; on the Flights tab the card swaps to two-leg fields with a one-way/round-trip selector.

**What the fields open.** Measured on the hydrated snapshot: Dates opens a 652 x 559 `uitk-dialog` two-month calendar — a selected day fills `primary`, the range tints `primary-container` #C8DFF9, a flexibility chip sits over the grid, Done closes. Travelers opens a 375 x 318 stepper menu (rooms, adults, children). Where to? opens a 376 x 510 panel with its own "Search by destination, accommodations, or landmark" input — sample text was typed and deleted; nothing was ever submitted.

**Screens.** [home-light-default](screenshots/home-light-default.png), [home-i-light-calendar-open](screenshots/home-i-light-calendar-open.png), [home-i-light-travelers-open](screenshots/home-i-light-travelers-open.png), [home-i-light-whereto-open](screenshots/home-i-light-whereto-open.png), [home-i-light-flights-tab](screenshots/home-i-light-flights-tab.png), [mobile-home-i-light-calendar-open](screenshots/mobile-home-i-light-calendar-open.png).

## Marketing bands that re-theme

**When.** Below the search card: promo strips (partner offers, app promos, campaign cards) that read as a different palette without being a different component set.

**Components.** [Marketing band](components.md#marketing-band), [Tertiary button](components.md#tertiary-button).

**Layout.** A section carries `data-theme-light="marketing-3"` and every `--egds-*` role inside rebinds: `surface` becomes the pale-blue #B7CDDC, `primary` becomes near-black #191E3B, `outline` inverts. The same card and button markup paints in the campaign palette — the theme-attribute mechanism is doing the work, not per-component overrides. The token file holds `marketing3` as a full set plus `dark1`, `dark2`, `bright1` and the eight `loyalty` tiers in `core.color.palette`.

**Screens.** [home-light-full](screenshots/home-light-full.png) (the pale-blue band under the search card).

## Deals carousels and save hearts

**When.** The home page's body: horizontal `uitk-carousel` rails of deal cards ("Member prices in Toronto" and friends), each item ~270 wide.

**Components.** [Deal card](components.md#deal-card), [Save (heart) button](components.md#save-heart-button), [Footer link](components.md#footer-link).

**Layout.** A card is a rounded `uitk-card`: the photo (which may carry the 48px circular save heart top-right and paging arrows), then name, dates/rating and price text. The heart is a 48px white circle that stays a `favorite-button` link for signed-out guests — saving would route to sign-in, so its pressed state was forced with CDP. Footer link columns close the page.

**Screens.** [home-light-default](screenshots/home-light-default.png), [mobile-home-light-full](screenshots/mobile-home-light-full.png).

## Results page: rail plus cards

**When.** A lodging results page — the compact search form under the header, then a two-column split: ~236px filter rail, ~756px card list.

**Components.** [Sticky search form](components.md#sticky-search-form), [Stay type tabs](components.md#stay-type-tabs), [Sort control](components.md#sort-control), [Results count](components.md#results-count), [Map card](components.md#map-card), [Filter column](components.md#filter-column), [Property name field](components.md#property-name-field), [Filter checkbox](components.md#filter-checkbox), [Compare switch](components.md#compare-switch).

**Layout.** The compact form re-runs the three fields plus a round Search icon at 48px high. Under it the "All stays / Hotels / Homes" segmented control (44px, `surface-container-variant` track, selected-and-disabled radios at rest) and the "Sort by recommended for you" `uitk-pill` — a 32px pill ringed by an inset `outline` hairline that blues to `secondary-container-variant` on hover and opens a menu (screenshot only; hydration refetches empty the list). The rail leads with a static Google-map card ("View in a map"), then the Filter by form: a property-name input, Property-class checkboxes, Guest-rating radios and a compare switch — nothing toggled.

**Screens.** [search-light-default](screenshots/search-light-default.png), [search-light-sort-open](screenshots/search-light-sort-open.png), [mobile-search-light-default](screenshots/mobile-search-light-default.png).

## The property result card

**When.** One row of the results list; the same card repeats for all 221 properties.

**Components.** [Property card](components.md#property-card), [Card gallery](components.md#card-gallery), [Carousel arrow](components.md#carousel-arrow), [VIP Access badge](components.md#vip-access-badge), [Amenity line](components.md#amenity-line), [Refund note](components.md#refund-note), [Rating pill](components.md#rating-pill), [Urgency note](components.md#urgency-note), [Price block](components.md#price-block), ["Sign in for extra savings" pill](components.md#sign-in-for-extra-savings-pill), [Save (heart) button](components.md#save-heart-button-1).

**Layout.** 756 x 232 at desktop: a 252-wide 21:9 gallery on the left with prev/next circles and the heart, then name and amenity icons, the green "Fully refundable" / "Reserve now, pay later" lines, a `surface-container-variant` rating pill ("9.2 Wonderful · 1,234 reviews"), the critical-coloured urgency note ("We have 1 left at this price"), and the right-aligned price block — struck list price, the 20px nightly headline, muted total. A dark "VIP Access" chip pins over the photo on partner hotels; "Sign in for extra savings" is a filled `primary`-blue pill button with white text pointing signed-out guests at member pricing (the fill paints on the button's `::after` layer).

**Screens.** [search-light-full](screenshots/search-light-full.png).

## Mobile shell

**When.** The same surfaces at 390 x 844. The header compresses to 56px; the search card keeps its one-row form squeezed to 390 — three ~58px field columns in a row beside the 83 x 48 Search button rather than stacked full-width fields (the product tabs scroll); the calendar opens as a sheet. On the archived results page the cards turn portrait at ~287px wide, centred in the column.

**Components.** The [Mobile (390 wide)](components.md#mobile-390-wide) group: [Header](components.md#header-1), [Hero title](components.md#hero-title-1), [Search form](components.md#search-form), [Search field](components.md#search-field), [Search button](components.md#search-button-1), [Deal card](components.md#deal-card-1).

**Screens.** [mobile-home-light-default](screenshots/mobile-home-light-default.png), [mobile-home-light-full](screenshots/mobile-home-light-full.png), [mobile-home-i-light-calendar-open](screenshots/mobile-home-i-light-calendar-open.png), [mobile-search-light-default](screenshots/mobile-search-light-default.png).

## Feedback after an action

**When.** What a control does on hover, focus and press.

**Captured.** Hover recolours quiet controls more than it fills them: header buttons and links keep their transparent ground and switch label colour from `on-surface` to `primary` blue, and the product tabs read unchanged. The fills that do paint are `secondary-container-variant` #ECF4FD on the outlined "See all deals" button and the sort pill; the filled savings pill reads unchanged on hover. Keyboard focus draws a 1px #101010 outline on links, tabs and pills, a heavier offset ring on the primary Search and savings buttons, a blue border plus inset ring inside the fields, and a 1px outline on the hearts' inner button (measured `measured.focus.*`). Pressed is forced `:active:hover` — Expedia implements press as a scrim overlay stepping `--egds-button-opacity-overlay-*` (64% → 72% → 92%), which computed styles on the root do not always surface.

**Not captured.** Sign-in/save success, saved-heart fill, sort applied, filters applied, calendar range picked — all need actions the kit does not take.

## Empty, loading and error states

**When.** Zero results, sold-out, API failure, offline.

**Captured.** None — the archived pages ship populated results only; hydration's failed API refetches emptied regions but were not kept as evidence (that is a capture artefact, not a designed empty state). Not measured.
