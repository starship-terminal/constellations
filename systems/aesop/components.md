# Aesop components

The discovery list of every page and state captured, then one entry per component with crops of the real site, the shared values and the Gaps. Captured from aesop.com on 2026-11-10 — the US storefront (Sites-aesop-us-Site, prices in US$) — as static pages rendered at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the live DOM. Nothing was submitted, bought or signed into; the only presses were local UI toggles (the Search disclosure, Email sign up modal, My cart drawer, All filters rail, burger menu). The OneTrust consent SDK was blocked at the network layer — its banner was never mounted, and no consent button was ever pressed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (68 components, 149 states).

How to read an entry:

- A colour is its value followed by the token in [tokens.json](tokens.json) whose value is the same, when there is one. Text is written family size/line-height weight, then its colour, for example `SuisseIntl 12/20 400, #000000`, and is read from the first text node inside the component.
- The first state of each entry lists every value; later states list only what changed, pseudo-elements and child paint included — a hover underline or a recoloured icon shows as `before`, `after`, `icon` or `layers` in the row. A state identical to the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component in [components/crops/](components/crops) (149 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`. Desktop shots are 1440 x 900 at 2x; `-full` shots are whole pages; mobile shots are `mobile-{page}-light-{state}.png`, 390 x 844 at 2x. Only light exists — the storefront has no dark theme.

| Surface | URL | Screenshots |
|---|---|---|
| Home. The hero, product rows and footer. Captured at rest, search open, sign-up modal, cart drawer, nav hover, and full-page. | `/` | [cart (light)](screenshots/home-light-cart.png), [default (light)](screenshots/home-light-default.png), [full (light)](screenshots/home-light-full.png), [nav-flyout (light)](screenshots/home-light-nav-flyout.png), [search (light)](screenshots/home-light-search.png), [signup (light)](screenshots/home-light-signup.png) |
| Shop all, the catalogue page. Captured at rest, filters rail open, and full-page. | `/shop-all/` | [default (light)](screenshots/shopall-light-default.png), [full (light)](screenshots/shopall-light-full.png), [sort (light)](screenshots/shopall-light-sort.png) |
| The Skin Care category landing. | `/skin-care/` | [default (light)](screenshots/skincare-light-default.png), [full (light)](screenshots/skincare-light-full.png) |
| A product page (The Aesop Valise, APB399). Captured at rest and full-page; its information accordion only renders at phone widths, so the open shot lives on the mobile capture. | `/gifts/seasonal-gift-kits/the-aesop-valise/APB399.html` | [default (light)](screenshots/pdp-light-default.png), [full (light)](screenshots/pdp-light-full.png) |
| The store locator. | `/stores` | [default (light)](screenshots/stores-light-default.png), [full (light)](screenshots/stores-light-full.png) |
| The cart route, empty. | `/cart` | [default (light)](screenshots/cart-light-default.png), [full (light)](screenshots/cart-light-full.png) |
| The Demandware sign-in page. | `/on/demandware.store/Sites-aesop-us-Site/en_US/Login-Show` | [default (light)](screenshots/login-light-default.png), [full (light)](screenshots/login-light-full.png) |
| The styled 404 / unexpected-error page. | `/account` | [default (light)](screenshots/notfound-light-default.png), [full (light)](screenshots/notfound-light-full.png) |
| Home at 390, at rest, the burger drawer open, and full-page. | `/` | [default (light)](screenshots/mobile-home-light-default.png), [full (light)](screenshots/mobile-home-light-full.png), [menu (light)](screenshots/mobile-home-light-menu.png) |
| The catalogue page at 390. | `/shop-all/` | [default (light)](screenshots/mobile-shopall-light-default.png), [full (light)](screenshots/mobile-shopall-light-full.png) |
| The product page at 390. | `/gifts/seasonal-gift-kits/the-aesop-valise/APB399.html` | [accordion (light)](screenshots/mobile-pdp-light-accordion.png), [default (light)](screenshots/mobile-pdp-light-default.png), [full (light)](screenshots/mobile-pdp-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Search disclosure | home | the Search header button | [home-light-search](screenshots/home-light-search.png), [search-field](#search-field) |
| Email sign up modal | home | the Email sign up button | [home-light-signup](screenshots/home-light-signup.png), [signup-dialog](#signup-dialog) |
| My cart drawer | home | the My cart button | [home-light-cart](screenshots/home-light-cart.png), [cart-panel](#cart-panel) |
| Filter rail | PLP | the All filters button | [shopall-light-sort](screenshots/shopall-light-sort.png), [filter-panel](#filter-panel) |
| PDP information accordion | PDP at 390 | the Description row on the mobile product page — the block carries h-hide-for-large, so desktop never paints it | [mobile-pdp-light-accordion](screenshots/mobile-pdp-light-accordion.png), [accordion](#accordion) |
| Mobile burger drawer | home at 390 | the burger button | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-drawer](#m-menu-drawer) |

## Shared values

Values that apply across entries, tallied from the measurement file.

**Radius.** 4px (6), 2px (4). 4px rounds the category quicklink pills and the floating label tabs of the size selects, 2px the Map/Satellite toggle, and the filter toggle's count dot is a 50% circle — every control edge stays square.

**Hover.** no change on the element (20), #fffef2 `action.outline` to #f6f5e8 `background.inset` (2), text #333333 `text.primary` to #000000 `text.black` (2), weight 400 to 700 (1), transparent to #fffef2 `action.outline` (1), #333333 `action.primary` to #252525 `background.dark` (1), a painted ::before/::after or icon change (1), #393939 `action.secondary` to #252525 `background.dark` (1). A hover stays quiet: the nav link goes bold and grows a 3px ink underline under its label (a `::before` bar), footer links pick up an underline, the ink buttons (ADD TO CART, the sign-in submit) deepen from #333333/#393939 to #252525, the quicklink pills go from a muted border to an ink keyline on a #f6f5e8 `background.inset` fill, the Search disclosure's Close icon dot darkens (#666666 to #343434), and the hero CTA card fills cream with ink text.

**Focus.** Of 25 elements given a real keyboard focus: no ring on the element (25). Aesop paints no focus ring — the computed outlineWidth stays 0 on every measured control; focus is at most the hover's colour shift.

**Motion.** 0.5s ease-out (26), 0.2s ease (24), 0.25s ease-out (12), 0.3s ease (6). Eases are short and gentle: 0.5s ease-out colour fades on the header controls, 0.2s ease on field keylines, 0.25s ease-out on the ink buttons and CTA card, 0.3s on the quicklink pills. The stylesheets add a 0.1s max-height reveal on accordions and navigation groups and a 0.4s padding slide on the sliding content panels.

**Layout.** The header is a two-tier rail — a 30px utility row over a 50.8px nav row (50px at 390) — above a fluid grid. Fields are 40px, buttons and CTA cards 48px, the cart drawer 405px, the filter rail 400px and the sign-up dialog 970px; the hero band runs 720px tall at 1440. Hairline 1px keylines in ink or `color.creamDark` separate everything — several are painted as 1px box-shadows rather than borders.

**Accent.** One accent only: the tannin amber #945c26 (`color.amber`), on tile badges (New addition, Beloved formulation), promos and inline links. Everything else is ink — #333333 for text, keylines and the dark fills, #252525/#393939 for the deep and soft steps — on the cream grounds #fffef2, #ebeade and #f6f5e8.

## Components

### Shell and navigation

The two-tier header every page shares: a thin utility row (Stores, Customer service / Email sign up, Account, My cart), the centred Aēsop wordmark and the main-nav row ending in a Search disclosure trigger. Cream-on-ink, transparent over the hero.

#### Header

<a id="header"></a>`header`, on home. The two-tier top bar every page shares: a thin utility row (Stores, Customer service left; Email sign up, Account, My cart right), the centred Aēsop wordmark, the Search disclosure and the main navigation row. Transparent over the hero, solid elsewhere.

<img src="components/crops/header-default.png" alt="Header, default" height="30"> 

| State | Values |
|---|---|
| default | size 1440 x 30; background rgba(255, 254, 242, 0.69); text SuisseIntl 12/14.4 700, #73736f; transition background 0.5s ease-out |

#### Wordmark

<a id="logo"></a>`logo`, on home. The centred "Aēsop." wordmark linking home.

<img src="components/crops/logo-default.png" alt="Wordmark, default" height="44"> 

| State | Values |
|---|---|
| default | size 140 x 44.09; background transparent; text SuisseIntl 12/18 400, #333333 `text.primary`; decoration underline |

#### Utility link

<a id="topnav-link"></a>`topnav-link`, on home. A utility-nav entry on the left of the top row (Stores); Customer service sits beside it.

<img src="components/crops/topnav-link-default.png" alt="Utility link, default" height="24"> <img src="components/crops/topnav-link-hover.png" alt="Utility link, hover" height="24"> <img src="components/crops/topnav-link-focus-visible.png" alt="Utility link, focus-visible" height="24"> <img src="components/crops/topnav-link-pressed.png" alt="Utility link, pressed" height="24"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed) | size 58.17 x 19; padding 0px 0px 0px 12px; background transparent; text SuisseIntl 12/14.4 700, #333333 `text.primary`; transition color 0.5s ease-out; before 0px x 19px; bg #333333 `action.primary`; after 0px x 20px; bg rgba(51, 51, 51, 0.2) `border.field` |

Child layers: a::before 0pxx19px background #333333 `action.primary`; a::after 0pxx20px background rgba(51, 51, 51, 0.2) `border.field`

#### Utility button

<a id="topnav-button"></a>`topnav-button`, on home. The Customer service utility button.

<img src="components/crops/topnav-button-default.png" alt="Utility button, default" height="24"> <img src="components/crops/topnav-button-hover.png" alt="Utility button, hover" height="24"> <img src="components/crops/topnav-button-focus-visible.png" alt="Utility button, focus-visible" height="24"> <img src="components/crops/topnav-button-pressed.png" alt="Utility button, pressed" height="24"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed) | size 109.53 x 14.39; padding 0px 0px 0px 12px; background transparent; text SuisseIntl 12/14.4 700, #333333 `text.primary`; transition color 0.5s ease-out; after 0px x 20px; bg rgba(51, 51, 51, 0.2) `border.field` |

Child layers: button::after 0pxx20px background rgba(51, 51, 51, 0.2) `border.field`

#### Email sign up button

<a id="signup-link"></a>`signup-link`, on home. The Email sign up trigger; opens the newsletter modal (a local toggle).

<img src="components/crops/signup-link-default.png" alt="Email sign up button, default" height="24"> <img src="components/crops/signup-link-hover.png" alt="Email sign up button, hover" height="24"> <img src="components/crops/signup-link-focus-visible.png" alt="Email sign up button, focus-visible" height="24"> <img src="components/crops/signup-link-pressed.png" alt="Email sign up button, pressed" height="24"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed) | size 73.47 x 14.39; background transparent; text SuisseIntl 12/14.4 700, #333333 `text.primary`; transition color 0.5s ease-out; after 0px x 20px; bg rgba(51, 51, 51, 0.2) `border.field` |

Child layers: button::after 0pxx20px background rgba(51, 51, 51, 0.2) `border.field`; span::before 18pxx18px background #333333 `action.primary`

#### Account entry

<a id="account-link"></a>`account-link`, on home. The Account slot in the utility row; its link lazy-loads once the header hydrates.

<img src="components/crops/account-link-default.png" alt="Account entry, default" height="24"> <img src="components/crops/account-link-hover.png" alt="Account entry, hover" height="24"> 

| State | Values |
|---|---|
| default (same: hover) | size 58.2 x 14.39; padding 0px 0px 0px 12px; background transparent; text SuisseIntl 12/14.4 700, #333333 `text.primary`; after 0px x 20px; bg rgba(51, 51, 51, 0.2) `border.field` |

Child layers: li::after 0pxx20px background rgba(51, 51, 51, 0.2) `border.field`

#### My cart button

<a id="cart-button"></a>`cart-button`, on home. The My cart trigger with its item count ("0 product in cart" empty); opens the right-hand cart drawer.

<img src="components/crops/cart-button-default.png" alt="My cart button, default" height="24"> <img src="components/crops/cart-button-hover.png" alt="My cart button, hover" height="24"> <img src="components/crops/cart-button-focus-visible.png" alt="My cart button, focus-visible" height="24"> <img src="components/crops/cart-button-pressed.png" alt="My cart button, pressed" height="24"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed) | size 56.61 x 20; background transparent; text SuisseIntl 12/14.4 700, #333333 `text.primary`; transition color 0.5s ease-out |

Child layers: i 0x20 background #333333 `action.primary`

#### Nav link

<a id="nav-link"></a>`nav-link`, on home. A main-nav entry (Gifts, Shop all, New & Notable, Skin Care, Hand & Body, Fragrance, Home, Hair, Travel, Library, Experience).

<img src="components/crops/nav-link-default.png" alt="Nav link, default" height="51"> <img src="components/crops/nav-link-hover.png" alt="Nav link, hover" height="51"> <img src="components/crops/nav-link-focus-visible.png" alt="Nav link, focus-visible" height="51"> <img src="components/crops/nav-link-pressed.png" alt="Nav link, pressed" height="51"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 64.89 x 50.8; padding 17px; background transparent; text SuisseIntl-Medium 14/16.8 400, #333333 `text.primary`; after 30.8906px x 0px |
| hover, pressed | text SuisseIntl-Medium 14/16.8 700, #333333 `text.primary`; before 64.8906px x 3px; bg #333333 `action.primary` |

#### Search button

<a id="search-button"></a>`search-button`, on home. The "Search…" trigger opening the search disclosure under the nav.

<img src="components/crops/search-button-default.png" alt="Search button, default" height="51"> <img src="components/crops/search-button-hover.png" alt="Search button, hover" height="51"> <img src="components/crops/search-button-focus-visible.png" alt="Search button, focus-visible" height="51"> <img src="components/crops/search-button-pressed.png" alt="Search button, pressed" height="51"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed) | size 140 x 50.8; padding 16px; border L: 2px solid #ebeade `border.secondary`; background #fffef2 `action.outline`; text SuisseIntl 14/16.8 700, #333333 `text.primary`; transition background 0.5s ease-out, color 0.5s ease-out; before 16px x 16px; bg #333333 `action.primary` |

### Home

The home canvas: a full-bleed campaign band under the transparent header (photography or film, an overlaid line and a bordered CTA card), then product rows and the dark footer.

#### Hero

<a id="hero"></a>`hero`, on home. The full-bleed campaign band under the transparent header: photography or film, an overlaid eyebrow line, a headline and a bordered CTA card.

<img src="components/crops/hero-default.png" alt="Hero, default" height="120"> 

| State | Values |
|---|---|
| default | size 1440 x 720; background transparent; text SuisseIntl-Medium 14/21 400, #fffef2 `text.onDark` |

Child layers: div 1440x720 background #333333 `action.primary`; flowplayer-endscreen-interstitial 0x0 background #030303; div 0x0 image url(…)

#### Hero CTA

<a id="hero-cta"></a>`hero-cta`, on home. A bordered call-to-action card inside the hero (Discover).

<img src="components/crops/hero-cta-default.png" alt="Hero CTA, default" height="48"> <img src="components/crops/hero-cta-hover.png" alt="Hero CTA, hover" height="48"> <img src="components/crops/hero-cta-focus-visible.png" alt="Hero CTA, focus-visible" height="48"> <img src="components/crops/hero-cta-pressed.png" alt="Hero CTA, pressed" height="48"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 390 x 48; padding 13px 24px 12px 24px; border 1px solid #fffef2 `border.light`; background transparent; text SuisseIntl-Medium 14/21 400, #fffef2 `text.onDark`; transition background-color 0.25s ease-out, color 0.25s ease-out; before 0px x 0px; after 16px x 16px; bg #fffef2 `action.outline` |
| hover, pressed | background #fffef2 `action.outline`; text SuisseIntl-Medium 14/21 400, #333333 `text.primary` |

### Footer

The dark page foot (ink #252525): secure-checkout and complimentary-samples lines, the Orders and support / About / Sustainability link columns in cream, and the Online Preferences OneTrust trigger.

#### Footer

<a id="footer"></a>`footer`, on pdp. The page foot: the newsletter block, help and service link columns, social and region links, and the "Online Preferences" OneTrust trigger.

<img src="components/crops/footer-default.png" alt="Footer, default" height="120"> 

| State | Values |
|---|---|
| default | size 1440 x 1027.19; background #252525 `background.dark`; text SuisseIntl-Medium 14/21 400, #fffef2 `text.onDark` |

#### Footer column title

<a id="footer-col-title"></a>`footer-col-title`, on pdp. A footer column heading.

<img src="components/crops/footer-col-title-default.png" alt="Footer column title, default" height="43"> 

| State | Values |
|---|---|
| default | size 176 x 43; padding 0px 0px 15px 0px; border B: 1px solid #fffef2 `border.light`; background transparent; text SuisseIntl 18/27 700, #fffef2 `text.onDark` |

Child layers: h2 176x43 border 1px solid #fffef2 `border.light`

#### Footer link

<a id="footer-link"></a>`footer-link`, on pdp. A footer link (Contact us, FAQs, Shipping, Returns, Track your order).

<img src="components/crops/footer-link-default.png" alt="Footer link, default" height="25"> <img src="components/crops/footer-link-hover.png" alt="Footer link, hover" height="25"> <img src="components/crops/footer-link-focus-visible.png" alt="Footer link, focus-visible" height="25"> <img src="components/crops/footer-link-pressed.png" alt="Footer link, pressed" height="25"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 70 x 24.8; padding 0px 0px 8px 0px; background transparent; text SuisseIntl 14/16.8 400, #fffef2 `text.onDark` |
| hover, pressed | decoration underline |

#### Online Preferences link

<a id="footer-prefs-link"></a>`footer-prefs-link`, on pdp. The OneTrust "Online Preferences" cookie-settings trigger in the footer. Measured, never pressed.

<img src="components/crops/footer-prefs-link-default.png" alt="Online Preferences link, default" height="25"> <img src="components/crops/footer-prefs-link-hover.png" alt="Online Preferences link, hover" height="25"> <img src="components/crops/footer-prefs-link-focus-visible.png" alt="Online Preferences link, focus-visible" height="25"> <img src="components/crops/footer-prefs-link-pressed.png" alt="Online Preferences link, pressed" height="25"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 123.64 x 24.8; padding 0px 0px 8px 0px; background transparent; text SuisseIntl 14/16.8 400, #fffef2 `text.onDark` |
| hover, pressed | decoration underline |

#### Newsletter field

<a id="newsletter-field"></a>`newsletter-field`, on pdp. The footer email field, if the region serves one: typed and deleted, never submitted.

<img src="components/crops/newsletter-field-default.png" alt="Newsletter field, default" height="40"> <img src="components/crops/newsletter-field-focused.png" alt="Newsletter field, focused" height="40"> <img src="components/crops/newsletter-field-filled.png" alt="Newsletter field, filled" height="40"> 

| State | Values |
|---|---|
| default | size 370 x 40; padding 0px 16px; border 1px solid rgba(51, 51, 51, 0.2) `border.field`; background #fffef2 `action.outline`; transition box-shadow 0.2s ease, border-color 0.2s ease-in-out; placeholder transparent |
| focused, filled | border 1px solid #333333 `border.default`; shadow #333333 0px 0px 0px 1px; placeholder #333333 `text.primary` |

### Catalogue page (PLP)

A catalogue page such as Shop all: the category title and product count, an All filters toggle opening a 400px left rail of accordion groups (Price, Skin type, Skin concern, Form, Ingredients, Aroma), a Sort select, then the tile grid — photograph, bold name, descriptor, size select, price, ink add-to-cart.

#### Catalogue title

<a id="plp-title"></a>`plp-title`, on shopall. The "Shop all" heading over the results grid, beside the product count.

<img src="components/crops/plp-title-default.png" alt="Catalogue title, default" height="30"> 

| State | Values |
|---|---|
| default | size 88.3 x 30; background transparent; text SuisseIntl 24/30 400, #333333 `text.primary` |

#### All filters button

<a id="filter-toggle"></a>`filter-toggle`, on shopall. The "All filters" toggle opening the refinement panel.

<img src="components/crops/filter-toggle-default.png" alt="All filters button, default" height="24"> <img src="components/crops/filter-toggle-hover.png" alt="All filters button, hover" height="24"> <img src="components/crops/filter-toggle-focus-visible.png" alt="All filters button, focus-visible" height="24"> <img src="components/crops/filter-toggle-pressed.png" alt="All filters button, pressed" height="24"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed) | size 96.77 x 21; padding 0px 40px 0px 0px; background transparent; text SuisseIntl-Medium 14/21 400, #333333 `text.primary`; after 16px x 16px; bg #333333 `action.primary` |

Child layers: button::after 16pxx16px background #333333 `action.primary`; span 0x0 background #333333 `action.primary` radius 50%

#### Refinement rail

<a id="filter-panel"></a>`filter-panel`, on shopall. The left-hand "Filter by" rail the All filters toggle opens: Price and attribute groups (Skin type, Skin concern, Form, Ingredients, Aroma) as accordion rows, RESET ALL and APPLY at the foot.

<img src="components/crops/filter-panel-default.png" alt="Refinement rail, default" height="120"> 

| State | Values |
|---|---|
| default | size 400 x 900; background #fffef2 `action.outline`; text SuisseIntl 12/18 400, #333333 `text.primary` |

#### Filter option

<a id="filter-option"></a>`filter-option`, on shopall. A refinement row inside the panel.

<img src="components/crops/filter-option-default.png" alt="Filter option, default" height="24"> <img src="components/crops/filter-option-hover.png" alt="Filter option, hover" height="24"> 

| State | Values |
|---|---|
| default (same: hover) | size 30.41 x 24; background transparent; text SuisseIntl 14/24 400, #333333 `text.primary`; transition transform 0.2s ease, font-size 0.2s ease, left 0.2s ease; before 100% x calc(50% + 2px); bg #fffef2 `action.outline` |

Child layers: label::before 100%xcalc(50% + 2px) background #fffef2 `action.outline` radius 4px 4px 0px 0px

#### Product tile

<a id="product-card"></a>`product-card`, on shopall. A product cell in the grid: a "New addition" tag when present, the product photograph, the name and the price.

<img src="components/crops/product-card-default.png" alt="Product tile, default" height="120"> <img src="components/crops/product-card-hover.png" alt="Product tile, hover" height="120"> 

| State | Values |
|---|---|
| default (same: hover) | size 270 x 540; background transparent; text SuisseIntl-Medium 11/normal 400, #945c26 `text.accent` |

Child layers: span::after 16pxx16px background #000000 `text.black`; label::before 33.3438pxx10px background #fffef2 `action.outline` radius 4px 4px 0px 0px; div::after 22pxx22px background #333333 `action.primary`

#### Product tile name

<a id="product-card-name"></a>`product-card-name`, on shopall. The product name under the tile photograph.

<img src="components/crops/product-card-name-default.png" alt="Product tile name, default" height="30"> 

| State | Values |
|---|---|
| default | size 270 x 30.23; background transparent; text SuisseIntl 14/15.12 700, #333333 `text.primary` |

#### Product tile price

<a id="product-card-price"></a>`product-card-price`, on shopall. The price under the name.

<img src="components/crops/product-card-price-default.png" alt="Product tile price, default" height="24"> 

| State | Values |
|---|---|
| default | size 270 x 19.19; background transparent; text SuisseIntl 16/19.2 400, #333333 `text.primary` |

#### Tile badge

<a id="tile-badge"></a>`tile-badge`, on shopall. The "New addition" tag over a tile photograph.

<img src="components/crops/tile-badge-default.png" alt="Tile badge, default" height="24"> 

| State | Values |
|---|---|
| default | size 67.17 x 14; radius 0px 4px 4px 0px; background transparent; text SuisseIntl-Medium 11/normal 400, #945c26 `text.accent` |

#### Category title

<a id="category-title"></a>`category-title`, on skincare. The Skin Care landing title.

<img src="components/crops/category-title-default.png" alt="Category title, default" height="38"> 

| State | Values |
|---|---|
| default | size 1170 x 37.5; background transparent; text SuisseIntl 30/37.5 400, #fffef2 `text.onDark` |

#### Category card

<a id="category-card"></a>`category-card`, on skincare. A subcategory card on the Skin Care landing.

<img src="components/crops/category-card-default.png" alt="Category card, default" height="27"> <img src="components/crops/category-card-hover.png" alt="Category card, hover" height="27"> 

| State | Values |
|---|---|
| default | size 72.8 x 26.8; padding 4px 8px 4px 4px; border 1px solid #bcbbb4 `color.muted`; radius 4px; background #fffef2 `action.outline`; text SuisseIntl 14/16.8 400, #333333 `text.primary`; transition background 0.3s ease, color 0.3s ease, border 0.3s ease |
| hover | border 1px solid #252525 `background.dark`; background #f6f5e8 `background.inset` |

#### Filter group row

<a id="filter-group"></a>`filter-group`, on shopall. A refinement group header row inside the rail (Price, Skin type, Skin concern, Form, Ingredients, Aroma).

<img src="components/crops/filter-group-default.png" alt="Filter group row, default" height="49"> <img src="components/crops/filter-group-hover.png" alt="Filter group row, hover" height="49"> <img src="components/crops/filter-group-focus-visible.png" alt="Filter group row, focus-visible" height="49"> <img src="components/crops/filter-group-pressed.png" alt="Filter group row, pressed" height="49"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed) | size 368 x 48.8; padding 16px; background transparent; text SuisseIntl 16/16.8 400, #333333 `text.primary` |

Child layers: span::after 16pxx16px background #333333 `action.primary`

#### Apply button

<a id="filter-apply"></a>`filter-apply`, on shopall. The black APPLY button at the rail’s foot. Measured, never pressed.

*Not found on the captured pages — an honest miss, kept so the gap is visible.*

#### Sort select

<a id="sort-select"></a>`sort-select`, on shopall. The "Sort: Featured" dropdown beside the product count.

<img src="components/crops/sort-select-default.png" alt="Sort select, default" height="24"> <img src="components/crops/sort-select-hover.png" alt="Sort select, hover" height="24"> <img src="components/crops/sort-select-focus-visible.png" alt="Sort select, focus-visible" height="24"> <img src="components/crops/sort-select-pressed.png" alt="Sort select, pressed" height="24"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed) | size 160 x 24; padding 0px 20px 0px 5px; background transparent; text SuisseIntl 14/24 400, #333333 `text.primary`; transition box-shadow 0.2s ease, border-color 0.2s ease-in-out |

#### Category quicklink

<a id="category-quicklink"></a>`category-quicklink`, on skincare. A quicklink pill on the category landing (Category, Skin type, Skin concern).

<img src="components/crops/category-quicklink-default.png" alt="Category quicklink, default" height="27"> <img src="components/crops/category-quicklink-hover.png" alt="Category quicklink, hover" height="27"> <img src="components/crops/category-quicklink-focus-visible.png" alt="Category quicklink, focus-visible" height="27"> <img src="components/crops/category-quicklink-pressed.png" alt="Category quicklink, pressed" height="27"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 72.8 x 26.8; padding 4px 8px 4px 4px; border 1px solid #bcbbb4 `color.muted`; radius 4px; background #fffef2 `action.outline`; text SuisseIntl 14/16.8 400, #333333 `text.primary`; transition background 0.3s ease, color 0.3s ease, border 0.3s ease |
| hover, pressed | border 1px solid #252525 `background.dark`; background #f6f5e8 `background.inset` |

#### Category product tile

<a id="category-product"></a>`category-product`, on skincare. A product tile on the Skin Care landing.

<img src="components/crops/category-product-default.png" alt="Category product tile, default" height="120"> <img src="components/crops/category-product-hover.png" alt="Category product tile, hover" height="120"> 

| State | Values |
|---|---|
| default (same: hover) | size 270 x 540; background transparent; text SuisseIntl-Medium 11/normal 400, #945c26 `text.accent` |

Child layers: span::after 16pxx16px background #000000 `text.black`; span::before 100%xcalc(50% + 2px) background #fffef2 `action.outline` radius 4px 4px 0px 0px; div 270x40 border 1px solid transparent

### Product page (PDP)

A product detail page: breadcrumbs over a two-column canvas (gallery left, purchase column right) — badge line, product title, price, descriptor, the bordered variant/size box, the ink Add to cart bar, then expandable rows and a suggested-partners rail.

#### Breadcrumbs

<a id="breadcrumbs"></a>`breadcrumbs`, on pdp. The breadcrumb line over the PDP.

<img src="components/crops/breadcrumbs-default.png" alt="Breadcrumbs, default" height="31"> 

| State | Values |
|---|---|
| default | size 1170 x 30.8; background transparent; text SuisseIntl-Medium 12/16.8 400, #333333 `text.primary` |

#### Breadcrumb link

<a id="breadcrumb-link"></a>`breadcrumb-link`, on pdp. A crumb link; the last crumb is the product name.

<img src="components/crops/breadcrumb-link-default.png" alt="Breadcrumb link, default" height="31"> <img src="components/crops/breadcrumb-link-hover.png" alt="Breadcrumb link, hover" height="31"> <img src="components/crops/breadcrumb-link-focus-visible.png" alt="Breadcrumb link, focus-visible" height="31"> <img src="components/crops/breadcrumb-link-pressed.png" alt="Breadcrumb link, pressed" height="31"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed) | size 33.95 x 30.8; padding 7px 0px; background transparent; text SuisseIntl-Medium 12/16.8 400, #333333 `text.primary` |

#### Product title

<a id="pdp-title"></a>`pdp-title`, on pdp. The product name heading the purchase column.

<img src="components/crops/pdp-title-default.png" alt="Product title, default" height="28"> 

| State | Values |
|---|---|
| default | size 185.03 x 28; background transparent; text CircularStd 24/30 400, #333333 `text.primary` |

#### Product price

<a id="pdp-price"></a>`pdp-price`, on pdp. The price beside or under the title.

<img src="components/crops/pdp-price-default.png" alt="Product price, default" height="30"> 

| State | Values |
|---|---|
| default | size 95.8 x 30; background transparent; text SuisseIntl 24/30 400, #333333 `text.primary` |

#### Product descriptor

<a id="pdp-subtitle"></a>`pdp-subtitle`, on pdp. The short descriptor line under the product name.

<img src="components/crops/pdp-subtitle-default.png" alt="Product descriptor, default" height="24"> 

| State | Values |
|---|---|
| default | size 99.53 x 16.8; background transparent; text SuisseIntl-Medium 12/16.8 400, #333333 `text.primary` |

#### Add to cart button

<a id="add-to-cart"></a>`add-to-cart`, on pdp. The primary purchase bar, caught mid-hydration as "Loading …" before its label resolves. Measured and state-forced, never pressed: pressing it adds the item.

<img src="components/crops/add-to-cart-default.png" alt="Add to cart button, default" height="48"> <img src="components/crops/add-to-cart-hover.png" alt="Add to cart button, hover" height="48"> <img src="components/crops/add-to-cart-focus-visible.png" alt="Add to cart button, focus-visible" height="48"> <img src="components/crops/add-to-cart-pressed.png" alt="Add to cart button, pressed" height="48"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 409.5 x 48; padding 13px 24px 12px 24px; border 1px solid transparent; background #333333 `action.primary`; text SuisseIntl-Medium 14/21 400, #fffef2 `text.onDark`; transition background-color 0.25s ease-out, color 0.25s ease-out; before 14px x 14px; bg #fffef2 `action.outline`; after 0px x 0px |
| hover, pressed | background #252525 `background.dark` |

#### Quantity control

<a id="qty-select"></a>`qty-select`, on pdp. The quantity selector beside Add to cart, when the product offers one.

*Not found on the captured pages — an honest miss, kept so the gap is visible.*

#### Product gallery

<a id="pdp-image"></a>`pdp-image`, on pdp. The product photograph column.

<img src="components/crops/pdp-image-default.png" alt="Product gallery, default" height="120"> 

| State | Values |
|---|---|
| default | size 700.5 x 700; background transparent |

Child layers: button::before 15pxx40px background #333333 `action.primary`; button::before 15pxx40px background #333333 `action.primary`

#### Service line

<a id="info-row"></a>`info-row`, on pdp. A service message near the purchase bar (complimentary shipping, samples).

<img src="components/crops/info-row-default.png" alt="Service line, default" height="24"> 

| State | Values |
|---|---|
| default | size 160.13 x 21; background transparent; text SuisseIntl-Medium 14/21 400, #fffef2 `text.onDark` |

#### Variant box

<a id="variant-box"></a>`variant-box`, on pdp. The variant/size selector above the purchase bar (the bordered "Kit $600.00" box on a kit).

<img src="components/crops/variant-box-default.png" alt="Variant box, default" height="46"> <img src="components/crops/variant-box-hover.png" alt="Variant box, hover" height="46"> <img src="components/crops/variant-box-focus-visible.png" alt="Variant box, focus-visible" height="46"> <img src="components/crops/variant-box-pressed.png" alt="Variant box, pressed" height="46"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed) | size 173 x 46.5; background transparent; text SuisseIntl 11/16.5 400, #666666 `text.muted` |

Child layers: a 66.9x25 background #fffef2 `action.outline` border 1px solid #333333 `border.default`; a 97.5x25 background #fffef2 `action.outline` border 1px solid #fffef2 `border.light`; button 0x0 background #fffef2 `action.outline`

#### Accordion row

<a id="accordion"></a>`accordion`, on mobile-pdp. An expandable information row on the PDP (Description). The block carries h-hide-for-large — desktop never paints it — so this is measured on the mobile PDP at 390.

<img src="components/crops/accordion-default.png" alt="Accordion row, default" height="49"> 

| State | Values |
|---|---|
| default | size 360 x 49; padding 14px 60px 14px 0px; background transparent; text SuisseIntl-Medium 14/21 400, #333333 `text.primary` |

### Panels and overlays

The overlays: the search disclosure under the nav, the right-hand My cart drawer (405px), the Email sign up modal shell (its remote fragment did not render in headless), the Filter by rail and the locator's No-result dialog.

#### Search disclosure

<a id="search-panel"></a>`search-panel`, on search. The "I'm looking for…" band the Search button reveals under the nav, with a Close button.

*Not found on the captured pages — an honest miss, kept so the gap is visible.*

#### Search field

<a id="search-field"></a>`search-field`, on search. The search text field; typed and deleted, never submitted.

<img src="components/crops/search-field-default.png" alt="Search field, default" height="40"> <img src="components/crops/search-field-focused.png" alt="Search field, focused" height="40"> <img src="components/crops/search-field-filled.png" alt="Search field, filled" height="40"> 

| State | Values |
|---|---|
| default (same: focused, filled) | size 960.66 x 40; padding 0px 10px; background #fffef2 `action.outline`; transition box-shadow 0.2s ease, border-color 0.2s ease-in-out; placeholder #666666 `text.muted` |

#### Search close button

<a id="search-close"></a>`search-close`, on search. The Close button ending the search disclosure.

<img src="components/crops/search-close-default.png" alt="Search close button, default" height="51"> <img src="components/crops/search-close-hover.png" alt="Search close button, hover" height="51"> <img src="components/crops/search-close-focus-visible.png" alt="Search close button, focus-visible" height="51"> <img src="components/crops/search-close-pressed.png" alt="Search close button, pressed" height="51"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 140 x 50.8; padding 16px; border L: 2px solid #ebeade `border.secondary`; background #fffef2 `action.outline`; text SuisseIntl 14/16.8 700, #333333 `text.primary`; transition background 0.5s ease-out, color 0.5s ease-out; before 12px x 12px; bg #666666 `text.muted`; after 138px x 2px; border 1px solid #fffef2 `border.light` |
| hover | before 12px x 12px; bg #343434 |
| pressed | before 12px x 12px; bg #363636 |

#### Cart drawer

<a id="cart-panel"></a>`cart-panel`, on cart. The right-hand sliding panel the My cart button opens; shows the empty-cart state when nothing was added. Its body logs a JSON parse warning in headless Chromium.

<img src="components/crops/cart-panel-default.png" alt="Cart drawer, default" height="120"> 

| State | Values |
|---|---|
| default | size 405 x 900; background #fffef2 `action.outline`; text SuisseIntl 12/18 400, #333333 `text.primary` |

#### Cart close button

<a id="cart-close"></a>`cart-close`, on cart. The close control at the drawer’s head.

*Not found on the captured pages — an honest miss, kept so the gap is visible.*

#### Email sign up dialog

<a id="signup-dialog"></a>`signup-dialog`, on signup. The newsletter modal the Email sign up button mounts (a remote Demandware content fragment).

<img src="components/crops/signup-dialog-default.png" alt="Email sign up dialog, default" height="120"> 

| State | Values |
|---|---|
| default | size 970 x 450; background #fffef2 `action.outline`; text SuisseIntl 0/normal 400, #000000 `text.black` |

#### Sign up email field

<a id="signup-field"></a>`signup-field`, on signup. The email field inside the dialog; typed and deleted, never submitted.

*Not found on the captured pages — an honest miss, kept so the gap is visible.*

#### Sign up checkbox

<a id="signup-checkbox"></a>`signup-checkbox`, on signup. A consent checkbox row in the dialog.

*Not found on the captured pages — an honest miss, kept so the gap is visible.*

#### Sign up button

<a id="signup-submit"></a>`signup-submit`, on signup. The dialog’s submit button. Measured and state-forced, never pressed: pressing it subscribes an address.

*Not found on the captured pages — an honest miss, kept so the gap is visible.*

### Stores

The store locator: Find a store title, an address field with a floating label, Geolocate me, a Filters select, the Map/Satellite toggle over a Google map, and the 'No result found' dialog.

#### Stores title

<a id="stores-title"></a>`stores-title`, on stores. "Find a store" — the locator heading.

<img src="components/crops/stores-title-default.png" alt="Stores title, default" height="30"> 

| State | Values |
|---|---|
| default | size 399.5 x 30; background transparent; text SuisseIntl 30/30 400, #000000 `text.black` |

#### Store search field

<a id="store-search"></a>`store-search`, on stores. The "Address, city, postal code…" locator field (a floating-label text field): typed and deleted, never submitted.

<img src="components/crops/store-search-default.png" alt="Store search field, default" height="40"> <img src="components/crops/store-search-focused.png" alt="Store search field, focused" height="40"> <img src="components/crops/store-search-filled.png" alt="Store search field, filled" height="40"> 

| State | Values |
|---|---|
| default | size 512 x 40; padding 0px 35px; border 1px solid rgba(51, 51, 51, 0.2) `border.field`; background #fffef2 `action.outline`; transition box-shadow 0.2s ease, border-color 0.2s ease-in-out; placeholder #333333 `text.primary` |
| focused, filled | border 1px solid #333333 `border.default`; shadow #333333 0px 0px 0px 1px |

#### Store card

<a id="store-card"></a>`store-card`, on stores. A boutique listing card on the locator page.

*Not found on the captured pages — an honest miss, kept so the gap is visible.*

#### Geolocate button

<a id="store-geolocate"></a>`store-geolocate`, on stores. The "Geolocate me" option under the search field.

<img src="components/crops/store-geolocate-default.png" alt="Geolocate button, default" height="24"> <img src="components/crops/store-geolocate-hover.png" alt="Geolocate button, hover" height="24"> <img src="components/crops/store-geolocate-focus-visible.png" alt="Geolocate button, focus-visible" height="24"> <img src="components/crops/store-geolocate-pressed.png" alt="Geolocate button, pressed" height="24"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed) | size 116.13 x 21; background transparent; text SuisseIntl-Medium 14/21 400, #000000 `text.black`; before 16px x 16px; bg #333333 `action.primary` |

Child layers: button::before 16pxx16px background #333333 `action.primary`

#### Store filters

<a id="store-filters"></a>`store-filters`, on stores. The Filters select beside the search field.

<img src="components/crops/store-filters-default.png" alt="Store filters, default" height="40"> <img src="components/crops/store-filters-hover.png" alt="Store filters, hover" height="40"> <img src="components/crops/store-filters-focus-visible.png" alt="Store filters, focus-visible" height="40"> <img src="components/crops/store-filters-pressed.png" alt="Store filters, pressed" height="40"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 178.13 x 40; padding 0px 45px 0px 20px; border 1px solid rgba(51, 51, 51, 0.2) `border.field`; background #fffef2 `action.outline`; text SuisseIntl 14/40 400, #333333 `text.primary`; transition box-shadow 0.2s ease, border-color 0.2s ease-in-out; after 22px x 22px; bg #333333 `action.primary` |
| hover, pressed | border 1px solid #333333 `border.default`; shadow #333333 0px 0px 0px 1px inset; text SuisseIntl 14/40 500, #000000 `text.black` |

#### Map/Satellite toggle

<a id="map-toggle"></a>`map-toggle`, on stores. The Map/Satellite segmented toggle over the map.

<img src="components/crops/map-toggle-default.png" alt="Map/Satellite toggle, default" height="40"> <img src="components/crops/map-toggle-hover.png" alt="Map/Satellite toggle, hover" height="40"> <img src="components/crops/map-toggle-focus-visible.png" alt="Map/Satellite toggle, focus-visible" height="40"> <img src="components/crops/map-toggle-pressed.png" alt="Map/Satellite toggle, pressed" height="40"> 

| State | Values |
|---|---|
| default (same: focus-visible, pressed) | size 69.56 x 40; padding 0px 17px; radius 2px 0px 0px 2px; background #ffffff `color.white`; shadow rgba(0, 0, 0, 0.3) 0px 1px 4px -1px; text Roboto 18/normal 500, #000000 `text.black` |
| hover | background #ebebeb |

#### No-result dialog

<a id="no-result-dialog"></a>`no-result-dialog`, on stores. The "No result found / Sorry no stores found" dialog the locator raises for a region with no boutiques; carries an OK dismiss button.

<img src="components/crops/no-result-dialog-default.png" alt="No-result dialog, default" height="120"> 

| State | Values |
|---|---|
| default | size 415 x 210.89; padding 24px; background #fffef2 `action.outline`; text SuisseIntl 30/37.5 400, #333333 `text.primary` |

#### See all locations link

<a id="see-all-link"></a>`see-all-link`, on stores. The "See all locations" link beside the map.

<img src="components/crops/see-all-link-default.png" alt="See all locations link, default" height="24"> <img src="components/crops/see-all-link-hover.png" alt="See all locations link, hover" height="24"> <img src="components/crops/see-all-link-focus-visible.png" alt="See all locations link, focus-visible" height="24"> <img src="components/crops/see-all-link-pressed.png" alt="See all locations link, pressed" height="24"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed) | size 91.94 x 18; background transparent; text SuisseIntl-Medium 12/18 400, #000000 `text.black` |

### Sign in

The Demandware sign-in page (Login-Show): My Account heading, full-width email and password fields, a Submit bar and the Create an Account link. Measured, never submitted.

#### Sign in title

<a id="login-title"></a>`login-title`, on login. The sign-in page heading.

<img src="components/crops/login-title-default.png" alt="Sign in title, default" height="50"> 

| State | Values |
|---|---|
| default | size 1440 x 50.39; background transparent; text SuisseIntl 36/50.4 400, #333333 `text.primary` |

#### Email field

<a id="login-email"></a>`login-email`, on login. The sign-in email field: typed and deleted, never submitted.

<img src="components/crops/login-email-default.png" alt="Email field, default" height="40"> <img src="components/crops/login-email-focused.png" alt="Email field, focused" height="40"> <img src="components/crops/login-email-filled.png" alt="Email field, filled" height="40"> 

| State | Values |
|---|---|
| default | size 1440 x 40; padding 0px 16px; border 1px solid rgba(51, 51, 51, 0.2) `border.field`; background #fffef2 `action.outline`; transition box-shadow 0.2s ease, border-color 0.2s ease-in-out; placeholder #333333 `text.primary` |
| focused, filled | border 1px solid #333333 `border.default`; shadow #333333 0px 0px 0px 1px; placeholder #000000 `text.black` |

#### Password field

<a id="login-password"></a>`login-password`, on login. The password field: focused only, never filled or submitted.

<img src="components/crops/login-password-default.png" alt="Password field, default" height="40"> <img src="components/crops/login-password-focused.png" alt="Password field, focused" height="40"> 

| State | Values |
|---|---|
| default | size 1440 x 40; padding 0px 16px; border 1px solid rgba(51, 51, 51, 0.2) `border.field`; background #fffef2 `action.outline`; transition box-shadow 0.2s ease, border-color 0.2s ease-in-out; placeholder #333333 `text.primary` |
| focused | border 1px solid #333333 `border.default`; shadow #333333 0px 0px 0px 1px; placeholder #000000 `text.black` |

#### Sign in button

<a id="login-submit"></a>`login-submit`, on login. The sign-in submit. Measured, never pressed.

<img src="components/crops/login-submit-default.png" alt="Sign in button, default" height="48"> <img src="components/crops/login-submit-hover.png" alt="Sign in button, hover" height="48"> <img src="components/crops/login-submit-focus-visible.png" alt="Sign in button, focus-visible" height="48"> <img src="components/crops/login-submit-pressed.png" alt="Sign in button, pressed" height="48"> 

| State | Values |
|---|---|
| default | size 96.72 x 48; padding 13px 24px 12px 24px; border 1px solid transparent; background #393939 `action.secondary`; text SuisseIntl-Medium 14/21 400, #fcfbef `color.creamHover`; transition background-color 0.25s ease-out, color 0.25s ease-out |
| hover | background #252525 `background.dark`; text SuisseIntl-Medium 14/21 400, #fffef2 `text.onDark` |
| focus-visible | background #333333 `action.primary`; text SuisseIntl-Medium 14/21 400, #fffef2 `text.onDark` |
| pressed | background #252525 `background.dark`; text SuisseIntl-Medium 14/21 400, #fffef2 `text.onDark` |

#### Register link

<a id="login-register"></a>`login-register`, on login. The create-account link beside the form.

<img src="components/crops/login-register-default.png" alt="Register link, default" height="24"> <img src="components/crops/login-register-hover.png" alt="Register link, hover" height="24"> <img src="components/crops/login-register-focus-visible.png" alt="Register link, focus-visible" height="24"> <img src="components/crops/login-register-pressed.png" alt="Register link, pressed" height="24"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 130.39 x 16; background transparent; text SuisseIntl 12/18 400, #333333 `text.primary`; decoration underline |
| hover, pressed | text SuisseIntl 12/18 400, #000000 `text.black` |

### Mobile (390 wide)

The same storefront at 390: the header collapses to Stores, wordmark and My cart; the burger button opens a flat accordion drawer of 48px rows.

#### Mobile header

<a id="m-header"></a>`m-header`, on home. The bar at 390: the burger button, the wordmark, search and cart.

<img src="components/crops/m-header-default.png" alt="Mobile header, default" height="50"> 

| State | Values |
|---|---|
| default | size 390 x 50; background rgba(255, 254, 242, 0.69); text SuisseIntl 12/18 400, #333333 `text.primary`; transition background 0.5s ease-out |

#### Burger button

<a id="m-menu-button"></a>`m-menu-button`, on home. The menu trigger; opens the navigation drawer.

<img src="components/crops/m-menu-button-default.png" alt="Burger button, default" height="52"> <img src="components/crops/m-menu-button-hover.png" alt="Burger button, hover" height="52"> <img src="components/crops/m-menu-button-focus-visible.png" alt="Burger button, focus-visible" height="52"> <img src="components/crops/m-menu-button-pressed.png" alt="Burger button, pressed" height="52"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed) | size 50 x 52; padding 18px 16px 10px 10px; background transparent; text SuisseIntl 12/normal 400, #000000 `text.black`; before 20px x 20px; bg #333333 `action.primary` |

Child layers: button::before 20pxx20px background #333333 `action.primary`

#### Mobile menu drawer

<a id="m-menu-drawer"></a>`m-menu-drawer`, on home. The navigation accordion the burger button opens.

<img src="components/crops/m-menu-drawer-default.png" alt="Mobile menu drawer, default" height="120"> 

| State | Values |
|---|---|
| default | size 390 x 539.17; background transparent; text SuisseIntl 14/16.8 400, #333333 `text.primary` |

Child layers: ul 390x539.2 background #fffef2 `action.outline`; li 390x49 border 1px solid rgba(51, 51, 51, 0.2) `border.field`; span::after 12pxx12px background #333333 `action.primary`

#### Mobile nav item

<a id="m-nav-item"></a>`m-nav-item`, on home. A level-1 accordion row inside the drawer (Gifts, New & Notable, Skin Care…).

<img src="components/crops/m-nav-item-default.png" alt="Mobile nav item, default" height="48"> <img src="components/crops/m-nav-item-hover.png" alt="Mobile nav item, hover" height="48"> <img src="components/crops/m-nav-item-focus-visible.png" alt="Mobile nav item, focus-visible" height="48"> <img src="components/crops/m-nav-item-pressed.png" alt="Mobile nav item, pressed" height="48"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed) | size 390 x 48.02; background transparent; text SuisseIntl 14/normal 400, #000000 `text.black` |

## Gaps

- The Email sign up modal mounts as a cream shell (970 x 450 measured); its remote Demandware Newsletter-SignUp fragment did not render in headless Chromium, so the dialog's fields, checkboxes and submit were never measurable — `signup-field`, `signup-checkbox` and `signup-submit` are honest misses.
- States that submit were never pressed: ADD TO CART, APPLY, the sign-in Submit, the store OK. Their hover, focus and pressed styles come from CDP-forced pseudo-classes and keyboard focus, not real clicks.
- `search-panel`'s container eluded marking (the disclosure mounts under a different id), but `search-field` and `search-close` inside it are measured, and the open state is in screenshots. `cart-close` has no measurable button: the drawer closes on backdrop/Escape.
- `qty-select` is absent on this PDP (a one-variant kit); the variant/size box is measured instead. `no-result-dialog` was measured at 415 x 211.
- Cloudflare Turnstile gates second document loads per context and some system routes: PDPs are reached as a first load in a fresh context (see tools/capture/public/lib.mjs note), and a still-blocked route would be recorded, not fought.
- Hover/focus on the 390 capture is not meaningful (a phone has neither); mobile entries cover layout and the burger drawer.

