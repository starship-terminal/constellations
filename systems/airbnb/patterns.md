# Airbnb patterns

How Airbnb's components combine to do the recurring jobs on its public pages, written from the captures of 2026-11-09 and 2026-11-10 (signed out, 1440 and 390 wide, headless Chromium, www.airbnb.com → www.airbnb.com.sg). Each pattern says when Airbnb uses it, the components it is built from (entries in [components.md](components.md), values in [tokens.json](tokens.json)), the layout, and the screens that show it. These are observations of what the product does, not Airbnb's own guidance.

| Pattern | Captured | Example screen |
|---|---|---|
| [Header shell and category tabs](#header-shell-and-category-tabs) | yes | [home-light-default](screenshots/home-light-default.png) |
| [The capsule search](#the-capsule-search) | yes, panel open; submit never sent | [home-light-search-open](screenshots/home-light-search-open.png) |
| [Gallery rails and listing cards](#gallery-rails-and-listing-cards) | yes | [home-light-card-hover](screenshots/home-light-card-hover.png) |
| [Filters and the results grid](#filters-and-the-results-grid) | yes; the map was not driven | [search-light-default](screenshots/search-light-default.png) |
| [A listing's page](#a-listings-page) | yes | [room-light-default](screenshots/room-light-default.png) |
| [Load-time coachmarks](#load-time-coachmarks) | yes | [home-light-modal](screenshots/home-light-modal.png) |
| [Help and host surfaces](#help-and-host-surfaces) | yes | [help-light-default](screenshots/help-light-default.png) |
| [Mobile shell](#mobile-shell) | yes | [mobile-home-light-default](screenshots/mobile-home-light-default.png) |
| [Feedback after an action](#feedback-after-an-action) | partial — hover, focus and forced press only | [card-heart crops](components/crops/card-heart-hover.png) |
| [Empty, loading and error states](#empty-loading-and-error-states) | loading only | [search-light-modal](screenshots/search-light-modal.png) |

## Header shell and category tabs

**When.** Every public page: home, search, room, help, host. A fixed 96px white bar padded 48px a side, over the page with a `border` hairline under it — logo left, then the Become a host link, a globe and the menu pushed right.

**Components.** [Header](components.md#header), [Header host link](components.md#header-host-link), [Header globe](components.md#header-globe), [Header menu](components.md#header-menu), [Tab active](components.md#tab-active) and [Tab resting](components.md#tab).

**Layout.** The rausch wordmark at `color.logo.brand` on the left; the second row of the bar on the home page carries the category tabs — Homes / Experiences / Services — as text tabs: the current one draws a 3px `text.primary` underline and sits in `text.primary` #222, the rest in `text.secondary` #6A6A6A that ink-darkens on hover. The host link is a quiet text item that greys to `bg.primary.hover` #F7F7F7 on hover; the globe and menu sit in 40px circles.

**Screens.** [home-light-default](screenshots/home-light-default.png), [search-light-default](screenshots/search-light-default.png) (the bar carries the mini search pill instead).

## The capsule search

**When.** The home page's hero act and the results page's persistent mini pill — the one control every Airbnb flow starts from.

**Components.** [Search bar](components.md#search-bar), [Search segment](components.md#search-segment), [Search submit](components.md#search-submit), [Search panel open](components.md#search-panel-open), [Mini search](components.md#mini-search).

**Layout.** An 850 x 66 capsule at 100px radius on white, ringed by a `border.secondary` #DDDDDD hairline inside a `shadow` drop-shadow — three segments (Where | When | Who) split by hairline dividers, each a stacked bold 12px label over a 14px secondary placeholder, and the 48px gradient circle submit pinned right. Hovering a segment greys it `bg.secondary` #EBEBEB; opening Where drops the suggestion panel under the pill without navigating (measured, then closed with Escape — the query was never submitted). On results and scroll the capsule collapses to the 66px-high mini pill that re-opens it.

**How it reads.** The submit is the only brand-gradient element in the header: `gradient.brand-core` (#E61E4D → #E31C5F → #D70466) — the one place Rausch is not flat. Pressed, segments and button scale to 0.96 over 100ms.

**Screens.** [home-light-default](screenshots/home-light-default.png), [home-light-search-open](screenshots/home-light-search-open.png), [search-light-default](screenshots/search-light-default.png) for the collapsed pill.

## Gallery rails and listing cards

**When.** The home page's body: horizontal rails of destination-titled cards ("Popular homes in Busan" and friends), each with a chevron heading and a scroll arrow.

**Components.** [Section title](components.md#section-title), [Listing card](components.md#listing-card), [Rail arrow](components.md#rail-arrow), [Card badge](components.md#card-badge), [Card heart](components.md#card-heart), [Rating row](components.md#card-rating).

**Layout.** Cards are 182 x 215 photo-led tiles at desktop width (165 x 199 on mobile): a near-square photo at a measured 20px radius with a white "Guest favourite" badge pill top-left and the heart top-right, then under the photo on the page's white: a 500-weight title, a grey dates line, the price line, and a ★-prefixed rating. The rail arrow is a small bordered circle that greys on hover. Cards carry no border and no shadow — the photo is the card.

**The heart.** The wishlist heart is a black-at-50% glyph with a white stroke (`measured.heart-idle`/`measured.heart-stroke`), so it reads over any photo; it has no fill to tint. A real tap opens the sign-up sheet signed out — the capture forces its press with CDP.

**Screens.** [home-light-default](screenshots/home-light-default.png), [home-light-card-hover](screenshots/home-light-card-hover.png), [mobile-home-light-full](screenshots/mobile-home-light-full.png).

## Filters and the results grid

**When.** A destination results page — the mini search pill in the header, a Filters button plus suggestion chips, then the card grid beside (at desktop) the map.

**Components.** [Mini search](components.md#mini-search), [Filters button](components.md#filters-button), [Filter chip](components.md#filter-chip), [Result card](components.md#result-card), [Listing badge](components.md#result-badge), [Result heart](components.md#result-heart), [Fees tag](components.md#fees-tag).

**Layout.** Below the header a row of 34px-high pills: the Filters button (84px, outlined, an icon glyph leading) then text chips — Type of place, Price, … — each a `border.secondary`-ringed 24px-radius pill that darkens its border on hover and draws the halo+ring shadow on focus. Under it the same photo-led cards as home, plus the "prices include all fees" tag. Chips are single-purpose toggles; the grid responds to the map on desktop, which was not driven.

**Screens.** [search-light-default](screenshots/search-light-default.png), [mobile-search-light-default](screenshots/mobile-search-light-default.png).

## A listing's page

**When.** A room's detail page — the book-end of the funnel.

**Components.** [Room title](components.md#room-title), [Share](components.md#room-share), [Save](components.md#room-save), [Photo grid](components.md#photo-grid), [Show all photos](components.md#show-photos), [Listing subtitle](components.md#room-subtitle), [Guest plaque](components.md#guest-plaque), [Reserve card](components.md#reserve-card), [Reserve date field](components.md#reserve-field), [Promo strip](components.md#promo-strip), [Promo claim](components.md#promo-claim), [Host row](components.md#host-row).

**Layout.** A `titles` headline with Share and Save as underlined-quiet text buttons; then the photo collage — one hero image left, a 2x2 grid right, all under a page-wide ~20px round, with the "Show all photos" outline button floating on the last tile. Below, two columns: the listing's copy and host row on the left, and the **reserve card** docked right — a 372px-wide white card at 12px radius with `elevation` shadow, carrying the price line, the stacked Check-in/Guests field box (bordered 8px, uppercase 10px labels), and the full-width gradient Reserve button under a "You won't be charged yet" reassurance.

**The promo strip** (a signed-out "get SGD X off" banner with a Claim button) sits above — its tap requires sign-in and was not performed.

**Screens.** [room-light-default](screenshots/room-light-default.png), [room-light-modal](screenshots/room-light-modal.png).

## Load-time coachmarks

**When.** First load on the home, results and room pages shows a "We're upgrading your search" (or promo) dialog over a dimmer.

**How it reads.** A white card centred on `bg` dim; the capture records it in the `*-modal` shots and hides it (without clicking "Got it") for every default shot and measurement, so the page underneath is what the values describe.

**Screens.** [home-light-modal](screenshots/home-light-modal.png), [search-light-modal](screenshots/search-light-modal.png), [room-light-modal](screenshots/room-light-modal.png).

## Help and host surfaces

**When.** The Help Centre and the Host landing — the quieter, document-led surfaces.

**Components.** [Help title](components.md#help-title), [Help search](components.md#help-search), [Help tile](components.md#help-tile), [Footer link](components.md#footer-link); [Host hero](components.md#host-hero), [Host CTA](components.md#host-cta), [Estimator card](components.md#estimator-card).

**Layout.** Help is a centred column: a `titles` "How can we help?", a full-width 16px-radius search field with a leading glyph, then a grid of topic tiles — icon, bold title, two grey lines — that lift a `border` on hover. The footer is the same on every page: four columns of `text.primary` links that underline on hover, over the `#F7F7F7` ground that separates it from the page. Host opens on a `special.display` hero line with the Get started CTA (the brand gradient, a 40px pill) and an earnings-estimator card.

**Screens.** [help-light-default](screenshots/help-light-default.png), [help-light-full](screenshots/help-light-full.png), [host-light-default](screenshots/host-light-default.png), [host-light-full](screenshots/host-light-full.png).

## Mobile shell

**When.** The same pages at 390 wide.

**Components.** [Mobile search pill](components.md#m-search-pill), [Mobile listing card](components.md#m-listing-card).

**Layout.** The desktop shell collapses: the header keeps only a compact search pill (the tabs become a scrollable strip below), cards go to 165 x 199 two-across, and the reserve pattern is not in the mobile capture's viewport. The tokens are unchanged — mobile is the same system at smaller boxes.

**Screens.** [mobile-home-light-default](screenshots/mobile-home-light-default.png), [mobile-home-light-full](screenshots/mobile-home-light-full.png), [mobile-search-light-default](screenshots/mobile-search-light-default.png).

## Feedback after an action

**What the public site shows.** Hover states are fill or border darkens (`bg.primary.hover` #F7F7F7 on the header links, border darkens on chips); focus is the white-halo + #222-ring box shadow on controls and a 2px outline 4px out on tabs; presses are 100ms 0.96 scale transforms — all measured. Confirmation toasts, error banners and post-action states sit behind the account boundary and were not reached: a blocked tap (wishlist heart, promo claim, menu items) opens a sign-in sheet instead of feedback.

## Empty, loading and error states

**Loading.** Page loads show the coachmark-over-dimmer pattern plus skeleton shimmer on late rails (the `loading` colour names in tokens). **Empty** states on the public surface are limited to the suggestion panel before a query (destinations list, captured with the search panel open). **Error** states exist in the token set (`status`, `invalid` colours, `border.*.invalid`) but no public page surfaced one — a submitted bad query, a failed payment and a missing room all sit behind flows the capture does not perform.
