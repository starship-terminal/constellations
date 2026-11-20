# Acne Studios components

The discovery list of every page and state captured, then one entry per component with crops of the real site, the shared values and the Gaps. Captured from acnestudios.com on 2026-11-09 — the Singapore storefront the site serves headless Chromium (`/sg/en/`, prices in S$) — as static pages rendered at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the live DOM. Nothing was submitted, bought or signed into; the only presses were local UI toggles (the SEARCH panel, the WOMAN mega-menu, the FILTER rail, the mobile Menu) and one PDP size cell's own toggle. The OneTrust consent SDK was blocked at the network layer — its banner was never mounted, and no consent button was ever pressed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (57 components, 145 states).

How to read an entry:

- A colour is its value followed by the token in [tokens.json](tokens.json) whose value is the same, when there is one. Text is written family size/line-height weight, then its colour, for example `Helvetica Now Text 12/20 400, #000000`, and is read from the first text node inside the component.
- The first state of each entry lists every value; later states list only what changed. A state identical to the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component in [components/crops/](components/crops) (145 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`. Desktop shots are 1440 x 900 at 2x; `-full` shots are whole pages; mobile shots are `mobile-{page}-light-{state}.png`, 390 x 844 at 2x. Only light exists — the storefront has no dark theme.

| Surface | URL | Screenshots |
|---|---|---|
| Home. The hero, gift-guide bars, campaign tiles and footer. Captured at rest, with the search panel open, and full-page. | `/sg/en/home` | [default (light)](screenshots/home-light-default.png), [full (light)](screenshots/home-light-full.png), [search (light)](screenshots/home-light-search.png) |
| WOMEN'S NEW ARRIVALS, the category page. Captured at rest, with the filter rail open, after LOAD MORE, and full-page. | `/sg/en/woman/new-arrivals/` | [default (light)](screenshots/woman-light-default.png), [filter (light)](screenshots/woman-light-filter.png), [full (light)](screenshots/woman-light-full.png), [load-more (light)](screenshots/woman-light-load-more.png) |
| The BAGS category landing. | `/sg/en/bags/` | [default (light)](screenshots/bags-light-default.png), [full (light)](screenshots/bags-light-full.png) |
| A product page (Leather Funnel Neck Jacket). Captured at rest, with a size picked, and full-page. | `/sg/en/rw-wn-leat000073/A70237-ADM.html?g=woman` | [default (light)](screenshots/pdp-light-default.png), [full (light)](screenshots/pdp-light-full.png), [size-picked (light)](screenshots/pdp-light-size-picked.png) |
| The About page. | `/sg/en/about/about.html` | [default (light)](screenshots/about-light-default.png), [full (light)](screenshots/about-light-full.png) |
| The FAQ. | `/sg/en/help/faq.html` | [default (light)](screenshots/faq-light-default.png), [full (light)](screenshots/faq-light-full.png) |
| Contact us. | `/sg/en/help/contact-us.html` | [default (light)](screenshots/contact-light-default.png), [full (light)](screenshots/contact-light-full.png) |
| The store directory. | `/sg/en/stores/stores.html` | [default (light)](screenshots/stores-light-default.png), [full (light)](screenshots/stores-light-full.png) |
| The shopping-bag route, which renders the bag drawer over the home page when empty. | `/sg/en/cart` | [default (light)](screenshots/cart-light-default.png), [full (light)](screenshots/cart-light-full.png) |
| The account sign-in gate. | `/sg/en/account` | [default (light)](screenshots/login-light-default.png), [full (light)](screenshots/login-light-full.png) |
| Home at 390, at rest, the Menu drawer open, and full-page. | `/sg/en/home` | [default (light)](screenshots/mobile-home-light-default.png), [full (light)](screenshots/mobile-home-light-full.png), [menu (light)](screenshots/mobile-home-light-menu.png) |
| The category page at 390. | `/sg/en/woman/new-arrivals/` | [default (light)](screenshots/mobile-woman-light-default.png), [full (light)](screenshots/mobile-woman-light-full.png) |
| The product page at 390. | `/sg/en/rw-wn-leat000073/A70237-ADM.html?g=woman` | [default (light)](screenshots/mobile-pdp-light-default.png), [full (light)](screenshots/mobile-pdp-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Search panel | home | the SEARCH header button | [home-light-search](screenshots/home-light-search.png), [search-panel](#search-panel) |
| Filter rail | PLP | the FILTER button | [woman-light-filter](screenshots/woman-light-filter.png), [filter-rail](#filter-rail) |
| After LOAD MORE | PLP | the LOAD MORE button | [woman-light-load-more](screenshots/woman-light-load-more.png) |
| Size picked | PDP | a size cell's own toggle (a local pick; nothing added) | [pdp-light-size-picked](screenshots/pdp-light-size-picked.png), [size-cell-selected](#size-cell-selected) |
| WOMAN mega-menu | home | the WOMAN nav item | [menu-panel](#menu-panel) |
| Mobile Menu drawer | home at 390 | the Menu button | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-drawer](#m-menu-drawer) |

## Shared values

Values that apply across entries, tallied from the measurement file.

**Radius.** none — every corner on the site is 0px. The single curve is the filter rail's 10px radio dot (`border-radius:100%` on a `::before`).

**Hover.** Acne hovers with colour, never fills or shadows: text #0018a8 `text.link` to #051574 `text.linkHover` (8), text #000000 `text.primary` to #6b6b6b `text.muted` (6), no change on the element (6), #000000 `action.primary` to #0018a8 `action.accent` (3), text #000000 `text.primary` to #051574 `text.linkHover` (2), text #000000 `text.primary` to #5c5c5c `text.secondary` (1), #0018a8 `action.accent` to #051574 `action.accentHover` (1), border #f2f2f2 `border.hairline` to #000000 `border.default` (1). Black fills (LOAD MORE, CONTINUE, SHOW N ITEMS) flip to Acne blue; blue fills (ADD TO BAG) deepen to #051574 `action.accentHover`; blue links deepen the same way; black labels (nav, FILTER, Menu) grey to #6b6b6b `text.muted`.

**Focus.** Of 24 elements given a real keyboard focus: no ring on the element (18), 1px solid #ffffff `text.onDark` offset -3px (3), 1px solid #000000 `border.default` offset -3px (1), 1px solid #051574 `text.linkHover` offset -3px (1), 1px solid #0018a8 `text.link` offset -3px (1). Focus could not be captured on 3 states (not focusable, or focused without matching :focus-visible), left out of the tally: `gift-link`, `geo-selector`, `sort-option`. The ring Acne does draw is a 1px solid keyline 3px inside the control — white on the black/blue buttons, deep blue on the white wishlist button, black on the size cells. Text links show no ring.

**Motion.** 0.15s ease (1). The only transitions the stylesheet carries are the drawers' 150ms padding-bottom safe-area slide, the accordions' 200ms max-height reveal and a 500ms fade on campaign layers, none on the controls themselves.

**Layout.** The header is a 60px rail (45px at 390); every page is a 1440-wide fluid grid of 4-px-base cells (`as-cell`). Primary buttons and the email fields share one 60px height; the small search field, menu links, suggestions and gift-guide bars are 30px rows; size cells are 77 x 45; every right-side drawer is 360 wide with a 45px head. Hairline 1px rules in #f2f2f2 (or black on drawers and the mega-menu's top edge) separate everything — several are painted as 1px background gradients rather than borders.

**Accent.** Acne blue (#0018a8) is the only accent: every text link, the ADD TO BAG fill, the wishlist border, the picked size cell's border and fill, the geo selector, and the hover step of every black button. Its deeper step #051574 is hover-only. Everything else is black, white or one of four warm greys.

## Components

### Shell and navigation

The 60px header every page shares (45px at 390): left the section triggers WOMAN MAN BAGS SCARVES GIFTS, centre the Acne Studios wordmark linking home, right SEARCH HELP ACCOUNT and the BAG count (`00` empty). White ground, 1px hairline rules top and bottom drawn as inset shadows; every item is a header-style 12/20 caps label on a full-height 60px hit row that greys to #6b6b6b on hover.

#### Header

<a id="header"></a>`header`, on home. The fixed top bar: left the section triggers (WOMAN MAN BAGS SCARVES GIFTS on desktop, a Menu button on narrow), centre the Acne Studios wordmark, right SEARCH HELP ACCOUNT and the BAG count, in a two-zone black-on-white layout with hairline rules.

<img src="components/crops/header-default.png" alt="Header, default" height="60"> 

| State | Values |
|---|---|
| default | size 1440 x 60; background #ffffff `action.onAction`; text Helvetica Now Text 12/20 400, #000000 `text.primary` |

#### Nav item

<a id="nav-item"></a>`nav-item`, on home. A section trigger (WOMAN MAN BAGS SCARVES GIFTS): all-caps micro type, opens the section mega-menu on press. Measured, the menu was opened once for its panel.

<img src="components/crops/nav-item-default.png" alt="Nav item, default" height="60"> <img src="components/crops/nav-item-hover.png" alt="Nav item, hover" height="60"> <img src="components/crops/nav-item-focus-visible.png" alt="Nav item, focus-visible" height="60"> <img src="components/crops/nav-item-pressed.png" alt="Nav item, pressed" height="60"> 

| State | Values |
|---|---|
| default | size 70.5 x 60; padding 4px 9px 33px 9px; border 1px solid transparent; background transparent; text Helvetica Now Text 12/20 400, #000000 `text.primary` |
| hover | text Helvetica Now Text 12/20 400, #6b6b6b `text.muted` |
| focus-visible | text Helvetica Now Text 12/20 400, #051574 `text.linkHover` |
| pressed | text Helvetica Now Text 12/20 400, #6b6b6b `text.muted` |

#### Wordmark

<a id="logo"></a>`logo`, on home. The centred Acne Studios logotype image (215px), an img that links home.

<img src="components/crops/logo-default.png" alt="Wordmark, default" height="28"> 

| State | Values |
|---|---|
| default | size 214.86 x 28; background transparent; transform translate(-107.43px, -14px); opacity 0 |

#### Search button

<a id="search-button"></a>`search-button`, on home. The SEARCH trigger opening the right-side search panel.

<img src="components/crops/search-button-default.png" alt="Search button, default" height="60"> <img src="components/crops/search-button-hover.png" alt="Search button, hover" height="60"> <img src="components/crops/search-button-focus-visible.png" alt="Search button, focus-visible" height="60"> <img src="components/crops/search-button-pressed.png" alt="Search button, pressed" height="60"> 

| State | Values |
|---|---|
| default | size 94.55 x 60; padding 4px 9px 33px 9px; border 1px solid transparent; background transparent; text Helvetica Now Text 12/20 400, #000000 `text.primary` |
| hover, focus-visible, pressed | text Helvetica Now Text 12/20 400, #6b6b6b `text.muted` |

#### Help button

<a id="help-button"></a>`help-button`, on home. The HELP trigger in the header.

<img src="components/crops/help-button-default.png" alt="Help button, default" height="60"> <img src="components/crops/help-button-hover.png" alt="Help button, hover" height="60"> <img src="components/crops/help-button-focus-visible.png" alt="Help button, focus-visible" height="60"> <img src="components/crops/help-button-pressed.png" alt="Help button, pressed" height="60"> 

| State | Values |
|---|---|
| default | size 72.89 x 60; padding 4px 9px 33px 9px; background transparent; text Helvetica Now Text 12/20 400, #000000 `text.primary` |
| hover, focus-visible, pressed | text Helvetica Now Text 12/20 400, #6b6b6b `text.muted` |

#### Account link

<a id="account-link"></a>`account-link`, on home. The ACCOUNT entry, an <a> to the sign-in page. Hovered and focused, never followed.

<img src="components/crops/account-link-default.png" alt="Account link, default" height="60"> <img src="components/crops/account-link-hover.png" alt="Account link, hover" height="60"> <img src="components/crops/account-link-focus-visible.png" alt="Account link, focus-visible" height="60"> <img src="components/crops/account-link-pressed.png" alt="Account link, pressed" height="60"> 

| State | Values |
|---|---|
| default | size 101.02 x 60; padding 4px 9px 33px 9px; background transparent; text Helvetica Now Text 12/20 400, #000000 `text.primary` |
| hover, focus-visible, pressed | text Helvetica Now Text 12/20 400, #6b6b6b `text.muted` |

#### Bag button

<a id="bag-button"></a>`bag-button`, on home. The BAG item-count button (shows "00" empty); opens the shopping-bag drawer.

<img src="components/crops/bag-button-default.png" alt="Bag button, default" height="60"> <img src="components/crops/bag-button-hover.png" alt="Bag button, hover" height="60"> <img src="components/crops/bag-button-focus-visible.png" alt="Bag button, focus-visible" height="60"> <img src="components/crops/bag-button-pressed.png" alt="Bag button, pressed" height="60"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed) | size 53.97 x 60; padding 4px 9px 33px 9px; background transparent; text Helvetica Now Text 12/20 400, #6b6b6b `text.muted` |

### Home

The home canvas: a full-bleed black campaign band with the giant white wordmark set over the photo, a GIFT GUIDE eyebrow top-left and WOMEN'S/MEN'S GIFT GUIDE link bars at the foot, then campaign tiles and the footer.

#### Hero

<a id="hero"></a>`hero`, on home. The full-bleed campaign band: black ground, a seasonal photo, the white Acne Studios wordmark set over it, a GIFT GUIDE eyebrow top-left and WOMEN’S/MEN’S GIFT GUIDE bars at the foot.

<img src="components/crops/hero-default.png" alt="Hero, default" height="120"> 

| State | Values |
|---|---|
| default | size 1440 x 810; background transparent; text Helvetica Now Text 12/20 400, #ffffff `text.onDark` |

Child layers: div::after 1440pxx810px shadow #000000 `action.primary` 0px 0px 0px 1px inset; div 1440x30 border 1px solid transparent; div 1440x30 border 1px solid transparent

#### Hero wordmark

<a id="hero-wordmark"></a>`hero-wordmark`, on home. The giant white "Acne Studios" image headline set over the FW26 campaign photo.

<img src="components/crops/hero-wordmark-default.png" alt="Hero wordmark, default" height="120"> 

| State | Values |
|---|---|
| default | size 1080 x 211.19; background transparent |

#### Gift guide bar

<a id="gift-link"></a>`gift-link`, on home. A hero-foot link bar (WOMEN’S GIFT GUIDE / MEN’S GIFT GUIDE).

<img src="components/crops/gift-link-default.png" alt="Gift guide bar, default" height="30"> <img src="components/crops/gift-link-hover.png" alt="Gift guide bar, hover" height="30"> <img src="components/crops/gift-link-pressed.png" alt="Gift guide bar, pressed" height="30"> 

| State | Values |
|---|---|
| default (same: pressed) | size 1440 x 30; padding 4px 9px; border 1px solid transparent; background transparent; text Helvetica Now Text 12/20 400, #ffffff `text.onDark` |
| hover | opacity 0 |

### Footer

The page foot: NEWSLETTER with its email field, contact methods (Live chat, Call, Email), four link columns in blue caps, two-letter social links (IG FB TW YT PT WB), the SHIPPING TO SINGAPORE (ENGLISH) region selector and the cookie-settings link — all under a 1px hairline rule.

#### Footer

<a id="footer"></a>`footer`, on home. The page foot: newsletter signup, contact methods (Live chat / Call / Email), four link columns, social icons, the "SHIPPING TO SINGAPORE (ENGLISH)" region selector and a cookie-settings link.

<img src="components/crops/footer-default.png" alt="Footer, default" height="120"> 

| State | Values |
|---|---|
| default | size 1440 x 572; border T: 1px solid #f2f2f2 `border.hairline`; background transparent; text Helvetica Now Text 12/20 400, #0018a8 `text.link` |

#### Newsletter heading

<a id="newsletter-label"></a>`newsletter-label`, on home. The NEWSLETTER block opening the footer, with the email field under it.

<img src="components/crops/newsletter-label-default.png" alt="Newsletter heading, default" height="24"> 

| State | Values |
|---|---|
| default | size 430 x 20; background transparent; text Helvetica Now Text 12/20 400, #0018a8 `text.link` |

#### Newsletter email field

<a id="newsletter-field"></a>`newsletter-field`, on home. The EMAIL text field in the footer: typed and deleted, never submitted.

<img src="components/crops/newsletter-field-default.png" alt="Newsletter email field, default" height="60"> <img src="components/crops/newsletter-field-focused.png" alt="Newsletter email field, focused" height="60"> <img src="components/crops/newsletter-field-filled.png" alt="Newsletter email field, filled" height="60"> 

| State | Values |
|---|---|
| default | size 430 x 60; padding 19px 10px; border 1px solid #f7f7f7 `border.field`; background #f7f7f7 `background.field`; placeholder #c2c2c2 `border.subtle` |
| focused, filled | padding 30.4px 10px 7.6px 10px; border 1px solid #000000 `border.default`; background #e8f0fe `action.selected` |

#### Footer column title

<a id="footer-col-title"></a>`footer-col-title`, on home. A column heading (HELP, CLIENT SERVICES, COMPANY, CONTACT US) in micro caps.

<img src="components/crops/footer-col-title-default.png" alt="Footer column title, default" height="24"> 

| State | Values |
|---|---|
| default | size 340 x 20; background transparent; text Helvetica Now Text 12/20 400, #000000 `text.primary` |

#### Footer link

<a id="footer-link"></a>`footer-link`, on home. A blue footer link (Contact us, FAQs, Find a store).

<img src="components/crops/footer-link-default.png" alt="Footer link, default" height="24"> <img src="components/crops/footer-link-hover.png" alt="Footer link, hover" height="24"> <img src="components/crops/footer-link-focus-visible.png" alt="Footer link, focus-visible" height="24"> <img src="components/crops/footer-link-pressed.png" alt="Footer link, pressed" height="24"> 

| State | Values |
|---|---|
| default (same: focus-visible, pressed) | size 340 x 24; background transparent; text Helvetica Now Text 12/24 400, #0018a8 `text.link` |
| hover | text Helvetica Now Text 12/24 400, #051574 `text.linkHover` |

#### Social link

<a id="social-link"></a>`social-link`, on home. A two-letter social link (IG FB TW YT PT WB).

<img src="components/crops/social-link-default.png" alt="Social link, default" height="30"> <img src="components/crops/social-link-hover.png" alt="Social link, hover" height="30"> <img src="components/crops/social-link-focus-visible.png" alt="Social link, focus-visible" height="30"> <img src="components/crops/social-link-pressed.png" alt="Social link, pressed" height="30"> 

| State | Values |
|---|---|
| default (same: focus-visible, pressed) | size 33.45 x 30; padding 4px 9px; border 1px solid transparent; background transparent; text Helvetica Now Text 12/20 400, #0018a8 `text.link` |
| hover | text Helvetica Now Text 12/20 400, #051574 `text.linkHover` |

#### Region selector

<a id="geo-selector"></a>`geo-selector`, on home. "SHIPPING TO SINGAPORE (ENGLISH)": the geo prompt serving the SG storefront. Hovered and focused only.

<img src="components/crops/geo-selector-default.png" alt="Region selector, default" height="24"> <img src="components/crops/geo-selector-hover.png" alt="Region selector, hover" height="24"> <img src="components/crops/geo-selector-pressed.png" alt="Region selector, pressed" height="24"> 

| State | Values |
|---|---|
| default (same: pressed) | size 227.52 x 20; background transparent; text Helvetica Now Text 12/20 400, #0018a8 `text.link` |
| hover | text Helvetica Now Text 12/20 400, #051574 `text.linkHover` |

### Category page (PLP)

A category page such as WOMEN'S NEW ARRIVALS: the under-header subnav (New Arrivals, Gifts for Her, Winter Dressing), the FILTER & SORTING rail trigger, then the product grid — 4-span tiles, photo, caps name, price. Prices on the PLP are Helvetica Now Text, not the PDP's monospace.

#### Subnav link

<a id="subnav-link"></a>`subnav-link`, on woman. The under-header section links on a category page (New Arrivals, Gifts for Her, Winter Dressing, Seasonal Denim, Scarf Personalisation): underlined micro caps.

<img src="components/crops/subnav-link-default.png" alt="Subnav link, default" height="30"> <img src="components/crops/subnav-link-hover.png" alt="Subnav link, hover" height="30"> <img src="components/crops/subnav-link-focus-visible.png" alt="Subnav link, focus-visible" height="30"> <img src="components/crops/subnav-link-pressed.png" alt="Subnav link, pressed" height="30"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed) | size 94.59 x 30; padding 4px 9px; border 1px solid transparent; background transparent; text Helvetica Now Text 12/20 400, #5c5c5c `text.secondary` |

#### Category title

<a id="plp-title"></a>`plp-title`, on woman. "WOMEN’S NEW ARRIVALS" with the item count under it.

<img src="components/crops/plp-title-default.png" alt="Category title, default" height="30"> 

| State | Values |
|---|---|
| default | size 1440 x 30; padding 4px 9px; border 1px solid transparent; background transparent; text Helvetica Now Text 12/20 400, #000000 `text.primary` |

#### Filter button

<a id="filter-toggle"></a>`filter-toggle`, on woman. The FILTER button opening the FILTER & SORTING rail: a header-style button in the toolbar.

<img src="components/crops/filter-toggle-default.png" alt="Filter button, default" height="30"> <img src="components/crops/filter-toggle-hover.png" alt="Filter button, hover" height="30"> <img src="components/crops/filter-toggle-focus-visible.png" alt="Filter button, focus-visible" height="30"> <img src="components/crops/filter-toggle-pressed.png" alt="Filter button, pressed" height="30"> 

| State | Values |
|---|---|
| default | size 83.47 x 30; padding 4px 9px; background transparent; text Helvetica Now Text 12/20 400, #000000 `text.primary` |
| hover, focus-visible, pressed | text Helvetica Now Text 12/20 400, #6b6b6b `text.muted` |

#### Product tile

<a id="product-card"></a>`product-card`, on woman. A product cell: a 4-span tile with the product photo(s), the name in caps and the monospace price under it. Hover swaps the photo.

<img src="components/crops/product-card-default.png" alt="Product tile, default" height="120"> <img src="components/crops/product-card-hover.png" alt="Product tile, hover" height="120"> 

| State | Values |
|---|---|
| default (same: hover) | size 360 x 590; background transparent; text Helvetica Now Text 12/20 400, #0018a8 `text.link` |

Child layers: div::after 360pxx590px shadow #000000 `action.primary` 0px 0px 0px 1px inset; picture 360x540 background #f7f7f7 `background.field`; picture 360x540 background #f7f7f7 `background.field`

#### Product tile name

<a id="product-card-name"></a>`product-card-name`, on woman. The product name under the tile photo, caps micro type.

<img src="components/crops/product-card-name-default.png" alt="Product tile name, default" height="24"> 

| State | Values |
|---|---|
| default | size 287.88 x 20; padding 0px 10px 0px 0px; background transparent; text Helvetica Now Text 12/20 400, #0018a8 `text.link` |

#### Product tile price

<a id="product-card-price"></a>`product-card-price`, on woman. The monospace price under the name (S$4,500).

<img src="components/crops/product-card-price-default.png" alt="Product tile price, default" height="24"> 

| State | Values |
|---|---|
| default | size 52.13 x 20; background transparent; text Helvetica Now Text 12/20 400, #000000 `text.primary` |

#### Load more button

<a id="load-more"></a>`load-more`, on woman. The black "LOAD MORE" button under the grid: a full-caps black pill the width of its cell.

<img src="components/crops/load-more-default.png" alt="Load more button, default" height="60"> <img src="components/crops/load-more-hover.png" alt="Load more button, hover" height="60"> <img src="components/crops/load-more-focus-visible.png" alt="Load more button, focus-visible" height="60"> <img src="components/crops/load-more-pressed.png" alt="Load more button, pressed" height="60"> 

| State | Values |
|---|---|
| default | size 320 x 60; padding 19px 9px; border 1px solid transparent; background #000000 `action.primary`; text Helvetica Now Text 12/20 400, #ffffff `text.onDark` |
| hover | background #0018a8 `action.accent` |
| focus-visible, pressed | background #0018a8 `action.accent`; outline 1px solid #ffffff `text.onDark`, offset -3px |

### Product page (PDP)

A product detail page: sticky breadcrumbs over a two-column canvas (gallery left, purchase column right) — caps title, colourway in muted grey, monospace price, the Fit Predictor line, the size grid, the electric-blue ADD TO BAG bar beside the white wishlist button, then expandable service rows and the spec list.

#### Breadcrumbs

<a id="breadcrumbs"></a>`breadcrumbs`, on pdp. The breadcrumb line over the PDP (Clothing / Outerwear / product name), sticky at the page top.

<img src="components/crops/breadcrumbs-default.png" alt="Breadcrumbs, default" height="31"> 

| State | Values |
|---|---|
| default | size 1440 x 31; border B: 1px solid #f2f2f2 `border.hairline`; background #ffffff `action.onAction`; image linear-gradient(#f2f2f2 `border.hairline` 1px, transparent 0px); text Helvetica Now Text 12/20 400, #000000 `text.primary` |

#### Breadcrumb link

<a id="breadcrumb-link"></a>`breadcrumb-link`, on pdp. A crumb link (Clothing, Outerwear); the last crumb is the product name.

<img src="components/crops/breadcrumb-link-default.png" alt="Breadcrumb link, default" height="30"> <img src="components/crops/breadcrumb-link-hover.png" alt="Breadcrumb link, hover" height="30"> <img src="components/crops/breadcrumb-link-focus-visible.png" alt="Breadcrumb link, focus-visible" height="30"> <img src="components/crops/breadcrumb-link-pressed.png" alt="Breadcrumb link, pressed" height="30"> 

| State | Values |
|---|---|
| default (same: focus-visible) | size 85.8 x 30; padding 4px 9px; border 1px solid transparent; background transparent; text Helvetica Now Text 12/20 400, #000000 `text.primary` |
| hover, pressed | text Helvetica Now Text 12/20 400, #5c5c5c `text.secondary` |

#### Product title

<a id="pdp-title"></a>`pdp-title`, on pdp. The product name in caps, right column head.

<img src="components/crops/pdp-title-default.png" alt="Product title, default" height="24"> 

| State | Values |
|---|---|
| default | size 345 x 20; background transparent; text Helvetica Now Text 12/20 400, #000000 `text.primary` |

#### Product price

<a id="pdp-price"></a>`pdp-price`, on pdp. The monospace price (S$4,500) beside the title.

<img src="components/crops/pdp-price-default.png" alt="Product price, default" height="24"> 

| State | Values |
|---|---|
| default | size 115 x 20; background transparent; text Helvetica Monospaced Pro 12/20 400, #000000 `text.primary` |

#### Colour name

<a id="pdp-color"></a>`pdp-color`, on pdp. The colourway under the title (Dark brown).

<img src="components/crops/pdp-color-default.png" alt="Colour name, default" height="24"> 

| State | Values |
|---|---|
| default | size 68 x 17; background transparent; text Helvetica Now Text 12/20 400, #6b6b6b `text.muted` |

#### Fit Predictor button

<a id="fit-predictor"></a>`fit-predictor`, on pdp. The "Fit Predictor - Calculate your size" link-button beside the size grid.

*Not found on the captured pages — an honest miss, kept so the gap is visible.*

#### Size guide link

<a id="size-guide-link"></a>`size-guide-link`, on pdp. The Size guide trigger opening the size drawer.

<img src="components/crops/size-guide-link-default.png" alt="Size guide link, default" height="49"> <img src="components/crops/size-guide-link-hover.png" alt="Size guide link, hover" height="49"> <img src="components/crops/size-guide-link-focus-visible.png" alt="Size guide link, focus-visible" height="49"> <img src="components/crops/size-guide-link-pressed.png" alt="Size guide link, pressed" height="49"> 

| State | Values |
|---|---|
| default | size 106.19 x 49; padding 19px 9px 4px 9px; border 1px solid transparent; background transparent; text Helvetica Now Text 12/24 400, #0018a8 `text.link` |
| hover, focus-visible, pressed | text Helvetica Now Text 12/24 400, #051574 `text.linkHover` |

#### Size cell

<a id="size-cell"></a>`size-cell`, on pdp. A size button in the variations grid (32–42): a bordered cell, caps numeral; the picked size gains a heavy black edge.

<img src="components/crops/size-cell-default.png" alt="Size cell, default" height="45"> <img src="components/crops/size-cell-hover.png" alt="Size cell, hover" height="45"> <img src="components/crops/size-cell-focus-visible.png" alt="Size cell, focus-visible" height="45"> <img src="components/crops/size-cell-pressed.png" alt="Size cell, pressed" height="45"> 

| State | Values |
|---|---|
| default | size 77.34 x 45; padding 4px 9px 19px 9px; border 1px solid #c2c2c2 `border.subtle`; background #ffffff `action.onAction`; text Helvetica Monospaced Pro 12/20 400, #000000 `text.primary` |
| hover | border 1px solid #000000 `border.default`; text Helvetica Monospaced Pro 12/20 400, #051574 `text.linkHover` |
| focus-visible | border 1px solid #000000 `border.default`; outline 1px solid #000000 `border.default`, offset -3px |
| pressed | border 1px solid #000000 `border.default`; text Helvetica Monospaced Pro 12/20 400, #051574 `text.linkHover` |

#### Size cell, picked

<a id="size-cell-selected"></a>`size-cell-selected`, on pdp. The selected size cell, pressed through the page’s own toggle.

<img src="components/crops/size-cell-selected-default.png" alt="Size cell, picked, default" height="45"> 

| State | Values |
|---|---|
| default | size 77.34 x 45; padding 4px 9px 19px 9px; border 1px solid #0018a8 `text.link`; background #e8f0fe `action.selected`; shadow #ffffff 0px 0px 0px 1px inset; text Helvetica Monospaced Pro 12/20 400, #0018a8 `text.link` |

#### Add to bag button

<a id="add-to-bag"></a>`add-to-bag`, on pdp. The electric-blue ADD TO BAG bar; hovered it retitles to "PLEASE SELECT SIZE" until a size is picked. Measured and state-forced, never pressed: pressing it adds the item.

<img src="components/crops/add-to-bag-default.png" alt="Add to bag button, default" height="60"> <img src="components/crops/add-to-bag-hover.png" alt="Add to bag button, hover" height="60"> <img src="components/crops/add-to-bag-focus-visible.png" alt="Add to bag button, focus-visible" height="60"> <img src="components/crops/add-to-bag-pressed.png" alt="Add to bag button, pressed" height="60"> 

| State | Values |
|---|---|
| default | size 400 x 60; padding 19px 9px; border 1px solid transparent; background #0018a8 `action.accent`; text Helvetica Now Text 12/20 400, #ffffff `text.onDark` |
| hover | background #051574 `action.accentHover` |
| focus-visible, pressed | background #051574 `action.accentHover`; outline 1px solid #ffffff `text.onDark`, offset -3px |

#### Wishlist button

<a id="wishlist-button"></a>`wishlist-button`, on pdp. The white heart button beside ADD TO BAG, blue heart outline. Measured, never pressed.

<img src="components/crops/wishlist-button-default.png" alt="Wishlist button, default" height="60"> <img src="components/crops/wishlist-button-hover.png" alt="Wishlist button, hover" height="60"> <img src="components/crops/wishlist-button-focus-visible.png" alt="Wishlist button, focus-visible" height="60"> <img src="components/crops/wishlist-button-pressed.png" alt="Wishlist button, pressed" height="60"> 

| State | Values |
|---|---|
| default | size 60 x 60; padding 19px 9px; border 1px solid #0018a8 `text.link`; background #ffffff `action.onAction`; text Helvetica Now Text 12/20 400, #000000 `text.primary` |
| hover | border 1px solid #051574 `text.linkHover`; text Helvetica Now Text 12/20 400, #051574 `text.linkHover` |
| focus-visible, pressed | border 1px solid #051574 `text.linkHover`; outline 1px solid #051574 `text.linkHover`, offset -3px; text Helvetica Now Text 12/20 400, #051574 `text.linkHover` |

#### Info row

<a id="info-row"></a>`info-row`, on pdp. An expandable service row (FREE DELIVERY & EASY RETURNS, COMPLIMENTARY GIFTWRAPPING, PICK UP IN STORE): caps label with a hairline rule and a chevron.

<img src="components/crops/info-row-default.png" alt="Info row, default" height="50"> <img src="components/crops/info-row-hover.png" alt="Info row, hover" height="50"> 

| State | Values |
|---|---|
| default | size 460 x 50; padding 4px 9px; border 1px solid #f2f2f2 `border.hairline`; background #ffffff `action.onAction`; text Helvetica Now Text 12/20 400, #0018a8 `text.link` |
| hover | border 1px solid #000000 `border.default` |

#### Description block

<a id="description"></a>`description`, on pdp. The product story and bullet spec list under the info rows.

<img src="components/crops/description-default.png" alt="Description block, default" height="40"> 

| State | Values |
|---|---|
| default | size 250 x 40; background transparent; text Helvetica Now Text 12/20 400, #000000 `text.primary` |

#### Show more link

<a id="show-more"></a>`show-more`, on pdp. The "+ SHOW MORE" spec expander.

<img src="components/crops/show-more-default.png" alt="Show more link, default" height="30"> <img src="components/crops/show-more-hover.png" alt="Show more link, hover" height="30"> <img src="components/crops/show-more-focus-visible.png" alt="Show more link, focus-visible" height="30"> <img src="components/crops/show-more-pressed.png" alt="Show more link, pressed" height="30"> 

| State | Values |
|---|---|
| default | size 460 x 30; padding 0px 0px 0px 20px; background transparent; text Helvetica Now Text 12/30 400, #0018a8 `text.link` |
| hover, focus-visible, pressed | text Helvetica Now Text 12/30 400, #051574 `text.linkHover` |

Child layers: button::after 460pxx60px image linear-gradient(transparent 0px, #ffffff `action.onAction` 50%)

### Panels and overlays

The right-side drawers, each 360 wide on opaque white with a 45px head and a black 1px top or bottom keyline: SEARCH (a SEARCH HERE field, SUGGESTIONS in blue caps, SUGGESTED PRODUCTS), FILTER & SORTING (radio rows with 10px dots, the black SHOW N ITEMS apply bar), and the WOMAN mega-menu (a 391 tall panel under the header, alternating 30px white/grey rows).

#### Search panel

<a id="search-panel"></a>`search-panel`, on search. The right-side SEARCH drawer: a SEARCH HERE field, SUGGESTIONS links in blue caps and SUGGESTED PRODUCTS thumbnails.

<img src="components/crops/search-panel-default.png" alt="Search panel, default" height="120"> 

| State | Values |
|---|---|
| default | size 360 x 555; background #ffffff `action.onAction`; text Helvetica Now Text 12/20 400, #000000 `text.primary` |

#### Search field

<a id="search-field"></a>`search-field`, on search. The SEARCH HERE text field; typed and deleted, never submitted.

<img src="components/crops/search-field-default.png" alt="Search field, default" height="30"> <img src="components/crops/search-field-focused.png" alt="Search field, focused" height="30"> <img src="components/crops/search-field-filled.png" alt="Search field, filled" height="30"> 

| State | Values |
|---|---|
| default | size 360 x 30; padding 4px 31px; border 1px solid #000000 `border.default`; background #f7f7f7 `background.field`; text Helvetica Now Text 12/20 400, #000000 `text.primary`; placeholder #c2c2c2 `border.subtle` |
| focused, filled | background #e8f0fe `action.selected` |

#### Search suggestion

<a id="search-suggestion"></a>`search-suggestion`, on search. A suggestion link in the panel (Outerwear, Knitwear, Bags, Scarves, Jeans), blue caps.

<img src="components/crops/search-suggestion-default.png" alt="Search suggestion, default" height="30"> <img src="components/crops/search-suggestion-hover.png" alt="Search suggestion, hover" height="30"> <img src="components/crops/search-suggestion-focus-visible.png" alt="Search suggestion, focus-visible" height="30"> <img src="components/crops/search-suggestion-pressed.png" alt="Search suggestion, pressed" height="30"> 

| State | Values |
|---|---|
| default (same: focus-visible, pressed) | size 360 x 30; padding 4px 9px; border 1px solid transparent; background transparent; text Helvetica Now Text 12/20 400, #0018a8 `text.link` |
| hover | text Helvetica Now Text 12/20 400, #051574 `text.linkHover` |

#### Section menu

<a id="menu-panel"></a>`menu-panel`, on menu. The WOMAN mega-menu: columns of category links under the header.

<img src="components/crops/menu-panel-default.png" alt="Section menu, default" height="120"> 

| State | Values |
|---|---|
| default | size 1440 x 391; border T: 1px solid #000000 `border.default`; background transparent; text Helvetica Now Text 12/20 400, #051574 `text.linkHover` |

#### Menu link

<a id="menu-link"></a>`menu-link`, on menu. A category link inside the mega-menu.

<img src="components/crops/menu-link-default.png" alt="Menu link, default" height="30"> <img src="components/crops/menu-link-hover.png" alt="Menu link, hover" height="30"> <img src="components/crops/menu-link-focus-visible.png" alt="Menu link, focus-visible" height="30"> <img src="components/crops/menu-link-pressed.png" alt="Menu link, pressed" height="30"> 

| State | Values |
|---|---|
| default (same: focus-visible, pressed) | size 360 x 30; padding 4px 9px; border 1px solid transparent; background transparent; text Helvetica Now Text 12/20 400, #0018a8 `text.link` |
| hover | text Helvetica Now Text 12/20 400, #051574 `text.linkHover` |

#### Filter rail

<a id="filter-rail"></a>`filter-rail`, on filter. The FILTER & SORTING drawer on the right: SORT BY radios (Newest, Price High/Low, Popularity) and TYPE OF PRODUCT radios, a bordered row for the picked option, the black SHOW N ITEMS apply button at the foot.

<img src="components/crops/filter-rail-default.png" alt="Filter rail, default" height="120"> 

| State | Values |
|---|---|
| default | size 360 x 901; background #ffffff `action.onAction`; text Helvetica Now Text 12/20 400, #000000 `text.primary` |

#### Sort option

<a id="sort-option"></a>`sort-option`, on filter. A radio row in the filter rail; the picked sort gains a hairline box.

<img src="components/crops/sort-option-default.png" alt="Sort option, default" height="24"> <img src="components/crops/sort-option-hover.png" alt="Sort option, hover" height="24"> <img src="components/crops/sort-option-pressed.png" alt="Sort option, pressed" height="24"> 

| State | Values |
|---|---|
| default (same: hover, pressed) | size 320 x 20; background transparent; text Helvetica Now Text 12/20 400, #000000 `text.primary` |

#### Show items button

<a id="show-items"></a>`show-items`, on filter. The black "SHOW N ITEMS" apply button at the rail’s foot. Measured, never pressed.

<img src="components/crops/show-items-default.png" alt="Show items button, default" height="44"> <img src="components/crops/show-items-hover.png" alt="Show items button, hover" height="44"> <img src="components/crops/show-items-focus-visible.png" alt="Show items button, focus-visible" height="44"> <img src="components/crops/show-items-pressed.png" alt="Show items button, pressed" height="44"> 

| State | Values |
|---|---|
| default | size 165 x 44; padding 4px 9px 18px 9px; border 1px solid #000000 `border.default`; background #000000 `action.primary`; text Helvetica Now Text 12/20 400, #ffffff `text.onDark` |
| hover, focus-visible, pressed | background #0018a8 `action.accent` |

#### Rail close button

<a id="filter-close"></a>`filter-close`, on filter. The X CLOSE at the rail’s head.

<img src="components/crops/filter-close-default.png" alt="Rail close button, default" height="42"> <img src="components/crops/filter-close-hover.png" alt="Rail close button, hover" height="42"> <img src="components/crops/filter-close-focus-visible.png" alt="Rail close button, focus-visible" height="42"> <img src="components/crops/filter-close-pressed.png" alt="Rail close button, pressed" height="42"> 

| State | Values |
|---|---|
| default (same: hover, focus-visible, pressed) | size 77.48 x 42; padding 4px 9px 18px 9px; background transparent; text Helvetica Now Text 12/20 400, #051574 `text.linkHover` |

### Sign in

The account gate: Sign in or register, the member-benefit list, the grey EMAIL field, the black CONTINUE bar and the bordered GOOGLE row, then the Singapore change-location line. Captured, never submitted.

#### Sign in title

<a id="login-title"></a>`login-title`, on login. "Sign in or register" — the gate for the account area.

<img src="components/crops/login-title-default.png" alt="Sign in title, default" height="24"> 

| State | Values |
|---|---|
| default | size 510 x 20; background transparent; text Helvetica Now Text 18/20 400, #000000 `text.primary` |

#### Benefit row

<a id="login-benefit"></a>`login-benefit`, on login. A member-benefit line (Priority access to new collections…) with an en-dash bullet.

<img src="components/crops/login-benefit-default.png" alt="Benefit row, default" height="24"> 

| State | Values |
|---|---|
| default | size 490 x 20; padding 0px 0px 0px 20px; background transparent; text Helvetica Now Text 12/20 400, #000000 `text.primary` |

#### Email field

<a id="login-email"></a>`login-email`, on login. The grey EMAIL field: typed and deleted, never submitted.

<img src="components/crops/login-email-default.png" alt="Email field, default" height="60"> <img src="components/crops/login-email-focused.png" alt="Email field, focused" height="60"> <img src="components/crops/login-email-filled.png" alt="Email field, filled" height="60"> 

| State | Values |
|---|---|
| default | size 520 x 60; padding 19px 10px; border 1px solid #f7f7f7 `border.field`; background #f7f7f7 `background.field`; placeholder #c2c2c2 `border.subtle` |
| focused, filled | padding 30.4px 10px 7.6px 10px; border 1px solid #000000 `border.default`; background #e8f0fe `action.selected` |

#### Continue button

<a id="login-continue"></a>`login-continue`, on login. The black CONTINUE bar. Measured, never pressed.

<img src="components/crops/login-continue-default.png" alt="Continue button, default" height="60"> <img src="components/crops/login-continue-hover.png" alt="Continue button, hover" height="60"> <img src="components/crops/login-continue-focus-visible.png" alt="Continue button, focus-visible" height="60"> <img src="components/crops/login-continue-pressed.png" alt="Continue button, pressed" height="60"> 

| State | Values |
|---|---|
| default | size 520 x 60; padding 19px 9px; border 1px solid transparent; background #000000 `action.primary`; text Helvetica Now Text 12/20 400, #ffffff `text.onDark` |
| hover | background #0018a8 `action.accent` |
| focus-visible, pressed | background #0018a8 `action.accent`; outline 1px solid #ffffff `text.onDark`, offset -3px |

#### Google button

<a id="login-google"></a>`login-google`, on login. The white-bordered GOOGLE oauth row. Measured, never pressed.

<img src="components/crops/login-google-default.png" alt="Google button, default" height="60"> <img src="components/crops/login-google-hover.png" alt="Google button, hover" height="60"> <img src="components/crops/login-google-focus-visible.png" alt="Google button, focus-visible" height="60"> <img src="components/crops/login-google-pressed.png" alt="Google button, pressed" height="60"> 

| State | Values |
|---|---|
| default | size 520 x 60; padding 19px 9px; border 1px solid #000000 `border.default`; background transparent; text Helvetica Now Text 12/20 400, #000000 `text.primary` |
| hover | border 1px solid #0018a8 `text.link`; text Helvetica Now Text 12/20 400, #0018a8 `text.link` |
| focus-visible, pressed | border 1px solid #0018a8 `text.link`; outline 1px solid #0018a8 `text.link`, offset -3px; text Helvetica Now Text 12/20 400, #0018a8 `text.link` |

#### Change location link

<a id="change-location"></a>`change-location`, on login. The "Singapore. Change location" line under the title.

<img src="components/crops/change-location-default.png" alt="Change location link, default" height="24"> <img src="components/crops/change-location-hover.png" alt="Change location link, hover" height="24"> <img src="components/crops/change-location-focus-visible.png" alt="Change location link, focus-visible" height="24"> <img src="components/crops/change-location-pressed.png" alt="Change location link, pressed" height="24"> 

| State | Values |
|---|---|
| default | size 97.16 x 20; background transparent; text Helvetica Now Text 12/20 400, #0018a8 `text.link` |
| hover, focus-visible, pressed | text Helvetica Now Text 12/20 400, #051574 `text.linkHover` |

### Mobile (390 wide)

The same storefront at 390: the header collapses to Menu, wordmark and bag; the Menu button opens a flat drawer of 45px rows (CONTACT US, HELP, CLIENT SERVICES, COMPANY, the social links) each separated by a 1px hairline drawn as a background gradient.

#### Mobile header

<a id="m-header"></a>`m-header`, on home. The bar at 390: a Menu button, the wordmark and the bag count only.

<img src="components/crops/m-header-default.png" alt="Mobile header, default" height="45"> 

| State | Values |
|---|---|
| default | size 390 x 45; background #ffffff `action.onAction`; text Helvetica Now Text 12/20 400, #000000 `text.primary` |

#### Mobile menu button

<a id="m-menu-button"></a>`m-menu-button`, on home. The Menu trigger; opens the drawer.

<img src="components/crops/m-menu-button-default.png" alt="Mobile menu button, default" height="45"> <img src="components/crops/m-menu-button-hover.png" alt="Mobile menu button, hover" height="45"> <img src="components/crops/m-menu-button-focus-visible.png" alt="Mobile menu button, focus-visible" height="45"> <img src="components/crops/m-menu-button-pressed.png" alt="Mobile menu button, pressed" height="45"> 

| State | Values |
|---|---|
| default | size 45 x 45; padding 4px 9px 18px 9px; background transparent; text Helvetica Now Text 12/20 400, #000000 `text.primary` |
| hover, focus-visible, pressed | text Helvetica Now Text 12/20 400, #6b6b6b `text.muted` |

#### Mobile menu drawer

<a id="m-menu-drawer"></a>`m-menu-drawer`, on home. The navigation drawer the Menu button opens.

<img src="components/crops/m-menu-drawer-default.png" alt="Mobile menu drawer, default" height="120"> 

| State | Values |
|---|---|
| default | size 390 x 844; background #ffffff `action.onAction`; text Helvetica Now Text 12/20 400, #000000 `text.primary`; transition padding-bottom 0.15s ease |

#### Mobile main

<a id="m-hero"></a>`m-hero`, on home. The mobile page canvas under the header.

<img src="components/crops/m-hero-default.png" alt="Mobile main, default" height="120"> 

| State | Values |
|---|---|
| default | size 390 x 4251; background transparent; text Helvetica Now Text 12/20 400, #ffffff `text.onDark` |

Child layers: div::after 390pxx585px shadow #000000 `action.primary` 0px 0px 0px 1px inset; div 390x45 border 1px solid transparent; div 390x45 border 1px solid transparent

## Gaps

- The Fit Predictor button (`fit-predictor`) never rendered in headless Chromium — the Fits.me widget did not mount on this product and geo, so it is recorded as an honest miss rather than measured on the wrong element. The PDP still shows its line ("Item runs True to size") in screenshots.
- States that submit were never pressed: ADD TO BAG, WISHLIST, CONTINUE, GOOGLE, SHOW N ITEMS, the newsletter sign-up. Their hover, focus and pressed styles were measured through CDP-forced pseudo-classes and keyboard focus, not real clicks.
- The bag drawer, checkout, account area, store stock check, size-guide drawer and search results were not captured: each either needs a cart item, an account, a purchase or a submitted form — all out of bounds. The cart route renders the home page when the bag is empty, which is what its screenshot shows.
- The OneTrust consent banner never mounted (its SDK was network-blocked), so the banner's own styling is unmeasured — only its selectors are known. The geo/region prompt and the gift-guide overlay bars were handled the same way when they appeared.
- The Fit Predictor, live chat and OneTrust widgets are third-party mounts; their internals are outside this package's palette either way. The few custom properties the site declares (`--safe-area-inset-bottom`, Tailwind framework internals, the Adyen checkout block) are in [raw/css-vars.json](raw/css-vars.json), not tokenised.
- Hover/focus on the 390 capture was not meaningful (a phone has neither); mobile entries cover layout and the drawer only. The PDP's colour variants beyond 'Dark brown' and other products' PDPs were not visited — the capture follows one product.

