# Douze components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from drinkdouze.com on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. drinkdouze.com is a Shopify storefront in French (the Impact-family theme plus douze-custom.css, Boogy / Robin) painting light only, as boxed sections on a sable field. Nothing was bought, sent or signed into; the login fields were filled once and emptied, a pack-size swatch was toggled (a radio, never an add-to-cart), and no consent or newsletter overlay was ever answered.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (64 components, 136 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Robin Regular 16/19.2 500, #301816`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (134 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every captured surface paints `light` (there is no dark theme; photo sections re-bind the same roles inside light shots). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [cart-drawer](screenshots/home-light-cart-drawer.png), [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Shop (all products) | `/collections/all` | [default](screenshots/shop-light-default.png), [full](screenshots/shop-light-full.png) |
| Orange Sanguine & Piment | `/products/orange-sanguine-piment` | [default](screenshots/product-light-default.png), [full](screenshots/product-light-full.png), [variant](screenshots/product-light-variant.png) |
| Trio Douze (bundle) | `/products/trio-douze` | [default](screenshots/trio-light-default.png), [full](screenshots/trio-light-full.png) |
| Notre histoire | `/pages/notre-histoire` | [default](screenshots/story-light-default.png), [full](screenshots/story-light-full.png) |
| Engagements | `/pages/engagements` | [default](screenshots/engagements-light-default.png), [full](screenshots/engagements-light-full.png) |
| FAQ | `/pages/page-faq` | [default](screenshots/faq-light-default.png), [full](screenshots/faq-light-full.png) |
| Store locator | `/pages/store-locator` | [default](screenshots/locator-light-default.png), [full](screenshots/locator-light-full.png) |
| Abonnement | `/pages/page-dabonnement` | [default](screenshots/abonnement-light-default.png), [full](screenshots/abonnement-light-full.png) |
| Parrainage | `/pages/parrainage` | [default](screenshots/parrainage-light-default.png), [full](screenshots/parrainage-light-full.png) |
| Recipes | `/blogs/recipes` | [default](screenshots/recipes-light-default.png), [full](screenshots/recipes-light-full.png) |
| Recipe (Sirocco) | `/blogs/recipes/sirocco` | [default](screenshots/recipe-light-default.png), [full](screenshots/recipe-light-full.png) |
| Cart | `/cart` | [default](screenshots/cart-light-default.png), [full](screenshots/cart-light-full.png) |
| Account login | `/account/login` | [default](screenshots/login-light-default.png) |
| Search | `/search?q=douze` | [default](screenshots/search-light-default.png), [full](screenshots/search-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Shop, phone | `/collections/all` | [default](screenshots/mobile-shop-light-default.png), [full](screenshots/mobile-shop-light-full.png) |
| Product, phone | `/products/orange-sanguine-piment` | [default](screenshots/mobile-product-light-default.png), [full](screenshots/mobile-product-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu drawer | home, phone width | the hamburger button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open) |
| Mini-cart drawer | home | the bag icon's own toggle (the drawer is empty signed out) | [home-light-cart-drawer](screenshots/home-light-cart-drawer.png) |
| Pack-size swatch | product page | the swatch radio's own click — Ajouter-au-panier was never pressed, nothing was added | [product-light-variant](screenshots/product-light-variant.png), [swatch-selected](#swatch-newly-selected) |
| Quick-add form | home and shop cards | hovering the card — the form is visibility:hidden until the card is hovered, and its submit was never pressed | [quick-add](#quick-add-button), [product-price](#product-price) |
| Klaviyo popup / consent overlays | every page | hidden, never answered (no consent button was ever clicked, no form ever sent) | hidden before every shot and reading |
| Signed-in account and checkout | /account, /checkout | the account area and Shopify checkout need an account and a live cart | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 21 components were given a real keyboard focus. 20 draw an outline ring: `nav-link` (1px auto #005fcc, offset 1px), `nav-shop` (1px auto #005fcc, offset 1px), `account-icon` (1px auto #005fcc, offset 1px), `cart-icon` (1px auto #005fcc, offset 1px), `hero-cta` (1px auto #005fcc, offset 1px), `product-item` (on a child: 1px auto rgb(0, 95, 204) offset 1px), `quick-add` (1px auto #005fcc, offset 0px), `sort-control` (1px auto #005fcc, offset 0px), `add-to-cart` (1px auto #005fcc, offset 0px), `reviews-tab` (on a child: 3px solid rgb(33, 43, 55) offset 1px), `accordion` (1px auto #005fcc, offset 0px), `login-button` (1px auto #005fcc, offset 0px), `recover-link` (1px auto #005fcc, offset 0px), `cart-cta` (1px auto #005fcc, offset 1px), `search-result` (on a child: 1px auto rgb(0, 95, 204) offset 1px), `footer-link` (1px auto #005fcc, offset 1px), `newsletter-button` (2px auto #f6f2e9 `color.brand.sable`, offset 0px), `m-nav-item` (1px auto #005fcc, offset 1px), `register-link` (1px auto #005fcc, offset 1px), `locale-button` (1px auto #005fcc, offset 0px). The other 1 show no measured change: `sort-select`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.2s | `ease` | background, box-shadow, transform | add-to-cart, cart-cta, hero-cta, login-button, m-hero-cta, quick-add, sort-control, swatch-selected and more |
| 0.2s | `ease-in-out` | background, border, box-shadow, color | cart-count, email-field, header, m-header, password-field, search-field |
| 0.6s | `cubic-bezier(0.75, 0, 0.175, 1)` | transform, visibility | m-menu-open |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Login card](#login-card) | 480 x 481.56 | - | 45px | #f6f2e9 `color.brand.sable` | none | 44px 48px |
| [Product card](#product-card) | 398.66 x 498.31 | - | 45px | transparent | none | 0 |
| [Cart, empty](#cart-empty) | 1162.22 x 197.98 | - | - | transparent | none | 0 |
| [Testimonial](#testimonial) | 1390 x 453.31 | - | 45px | transparent | none | 0 |
| [Product media](#product-media) | 695 x 810 | - | - | transparent | none | 0 |

## Components

### Shell and navigation

The storefront chrome: the announcement strip, the 57px transparent header (nav links, the DOUZE wordmark, icons) and the cart bubble.

#### Announcement bar
The top strip ("Livraison gratuite en France métropolitaine à partir de 50€"), sable on the page edge. Read as `announcement-bar` on the home page.

**Values (default).** size 1440 x 36.45; background transparent; text Robin Semibold 12/18.46 500, #301816 `color.brand.dusk`; layers section.section 1390.0x36.5 rgb(246, 242, 233) 45px; announcement-bar.announcement-bar 1390.0x36.5 rgb(246, 242, 233) 45px.

Child layers that carry the look: section 1390x36.5 background #f6f2e9 `color.brand.sable` radius 45px; announcement-bar 1390x36.5 background #f6f2e9 `color.brand.sable` radius 45px.

![Announcement bar default](components/crops/announcement-bar-default.png)

#### Header
The sticky transparent header: nav links left, the DOUZE wordmark centre, links + newsletter/account/cart icons right. Read as `header` on the home page.

**Values (default).** size 1390 x 57; background transparent; text Robin Semibold 12/13.2 500, #301816 `color.brand.dusk`; transition background 0.2s ease-in-out, color 0.2s ease-in-out, box-shadow 0.2s ease-in-out; layers a::after.header__linklist-link.link--animated 38.6406pxx1px rgb(48, 24, 22); a::after.header__linklist-link.link--animated 116.969pxx1px rgb(48, 24, 22); a::after.header__linklist-link.link--animated 139.672pxx1px rgb(48, 24, 22); a::after.header__linklist-link.link--animated 71.8594pxx1px rgb(48, 24, 22); a::after.header__linklist-link.link--animated 109.766pxx1px rgb(48, 24, 22); a::after.header.

Child layers that carry the look: a::after 38.6406pxx1px background #301816 `color.brand.dusk`; a::after 116.969pxx1px background #301816 `color.brand.dusk`; a::after 139.672pxx1px background #301816 `color.brand.dusk`.

![Header default](components/crops/header-default.png)

#### Logo
The DOUZE wordmark SVG anchor. Read as `logo` on the home page.

**Values (default).** size 70 x 23; background transparent; text Robin Regular 16/19.2 500, #301816 `color.brand.dusk`; icon 70 x 23, #301816 `color.brand.dusk`.

![Logo default](components/crops/logo-default.png)

#### Nav link
A plain header nav link (animated-underline style). Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 116.97 x 13.19; background transparent; text Robin Semibold 12/13.2 500, #301816 `color.brand.dusk`; layers ::after rgb(48, 24, 22) 0px none 1; a::after.header__linklist-link.link--animated 116.969pxx1px rgb(48, 24, 22) |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers ::after rgb(48, 24, 22) 0px none 1; a.header__linklist-link.link--animated 117.0x13.2 1px auto rgb(0, 95, 204) offset 1px; a::after.header__linklist-link.link--animated 116.969pxx1px rgb(48, 24, 22) |

Child layers that carry the look: a::after 116.969pxx1px background #301816 `color.brand.dusk`.

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Shop nav link
The Shop link, marked has-dropdown; its panel content is not in the signed-out DOM on hover. Read as `nav-shop` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 38.64 x 13.19; background transparent; text Robin Semibold 12/13.2 500, #301816 `color.brand.dusk`; layers ::after rgb(48, 24, 22) 0px none 1; a::after.header__linklist-link.link--animated 38.6406pxx1px rgb(48, 24, 22) |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers ::after rgb(48, 24, 22) 0px none 1; a.header__linklist-link.link--animated 38.6x13.2 1px auto rgb(0, 95, 204) offset 1px; a::after.header__linklist-link.link--animated 38.6406pxx1px rgb(48, 24, 22) |

Child layers that carry the look: a::after 38.6406pxx1px background #301816 `color.brand.dusk`.

![Shop nav link default](components/crops/nav-shop-default.png) ![Shop nav link hover](components/crops/nav-shop-hover.png) ![Shop nav link focus-visible](components/crops/nav-shop-focus-visible.png) ![Shop nav link pressed](components/crops/nav-shop-pressed.png)

#### Account icon link
The person icon linking to /account/login; measured, never followed. Read as `account-icon` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 25 x 25; background transparent; text Robin Regular 16/19.2 500, #301816 `color.brand.dusk`; icon 25 x 25, #301816 `color.brand.dusk`; layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers ::before rgba(0, 0, 0, 0) 0px none 1; a.header__icon-wrapper.tap-area 25.0x25.0 1px auto rgb(0, 95, 204) offset 1px |

![Account icon link default](components/crops/account-icon-default.png) ![Account icon link hover](components/crops/account-icon-hover.png) ![Account icon link focus-visible](components/crops/account-icon-focus-visible.png) ![Account icon link pressed](components/crops/account-icon-pressed.png)

#### Cart icon
The bag icon with the floating cart-count bubble; toggles the mini-cart drawer. Read as `cart-icon` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 20 x 18; background transparent; text Robin Regular 9/8.55 600, #f6f2e9 `color.brand.sable`; icon 20 x 18, #301816 `color.brand.dusk`; layers ::before rgba(0, 0, 0, 0) 0px none 1; cart-count.header__cart-count.header__cart-count--floating 15.0x15.0 rgb(48, 24, 22) 15px |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers ::before rgba(0, 0, 0, 0) 0px none 1; a.header__icon-wrapper.tap-area 20.0x18.0 1px auto rgb(0, 95, 204) offset 1px; cart-count.header__cart-count.header__cart-count--floating 15.0x15.0 rgb(48, 24, 22) 15px |

Child layers that carry the look: cart-count 15x15 background #301816 `color.brand.dusk` radius 15px.

![Cart icon default](components/crops/cart-icon-default.png) ![Cart icon hover](components/crops/cart-icon-hover.png) ![Cart icon focus-visible](components/crops/cart-icon-focus-visible.png) ![Cart icon pressed](components/crops/cart-icon-pressed.png)

#### Cart count bubble
The numeric bubble on the bag icon (0 signed out). Read as `cart-count` on the home page.

**Values (default).** size 15 x 15; radius 15px; background #301816 `color.brand.dusk`; text Robin Regular 9/8.55 600, #f6f2e9 `color.brand.sable`; transition background 0.2s ease-in-out, color 0.2s ease-in-out.

![Cart count bubble default](components/crops/cart-count-default.png)

### Home hero

The boxed photo hero: a Boogy display line with an italic accent and the square dusk SHOP button over the media.

#### Hero headline
The boxed hero's Boogy display heading (60-72px, italic accent on the flavour name), sable text over the photo. Read as `hero-title` on the home page.

**Values (default).** size 559.8 x 194.39; background transparent; text Boogy Italic 72/64.8 300, #f6f2e9 `color.brand.sable`.

![Hero headline default](components/crops/hero-title-default.png)

#### Hero CTA
The "SHOP" button over the hero media: dusk fill, white label, square 0px corners. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 67.69 x 44; padding 0px 15px; background #301816 `color.brand.dusk`; image linear-gradient(178deg, #301816 `color.brand.dusk`, #301816 `color.brand.dusk` 10%, rgba(0, 0, 0, 0.07) 10%, rgba(0, 0, 0, 0.07) 100%), linear-gradient(#301816 `color.brand.dusk`, #301816 `color.brand; text Robin Semibold 12/14.4 500, #ffffff `color.brand.white`; transition transform 0.2s ease, box-shadow 0.2s ease; layers ::before rgb(48, 24, 22) 0px none 1; ::after rgb(48, 24, 22) 0px none 1 |
| hover | shadow rgba(0, 0, 0, 0.15) 0px 4px 8px 0px; transform translate(0px, -2px) |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | shadow rgba(0, 0, 0, 0.15) 0px 4px 8px 0px; transform translate(0px, -2px) |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

### Home sections

Between the boxed sections: the 50px moving claim banner, Boogy section headings, the product-item cards and the testimonials.

#### Moving banner
The scrolling claim strip ("Sans sucre ajouté · Faible en calories · …") between sections. Read as `marquee` on the home page.

**Values (default).** size 1440 x 50; background transparent; text Robin Semibold 12/14.4 600, #301816 `color.brand.dusk`; layers div::after.moving-banner_divider 9pxx9px rgb(207, 230, 244) T:1px solid rgb(48, 24, 22) / R:1px solid rgb(48, 24, 22) / B:1px solid rgb(48, 24, 22) / L:1px solid rgb(48, 24, 22) 50%; div::after.moving-banner_divider 9pxx9px rgb(207, 230, 244) T:1px solid rgb(48, 24, 22) / R:1px solid rgb(48, 24, 22) / B:1px solid rgb(48, 24, 22) / L:1px solid rgb(48, 24, 22) 50%; div::after.moving-banner_divider 9.

Child layers that carry the look: div::after 9pxx9px background #cfe6f4 border 1px solid #301816 `color.brand.dusk` radius 50%; div::after 9pxx9px background #cfe6f4 border 1px solid #301816 `color.brand.dusk` radius 50%; div::after 9pxx9px background #cfe6f4 border 1px solid #301816 `color.brand.dusk` radius 50%.

![Moving banner default](components/crops/marquee-default.png)

#### Moving banner item
One claim inside the scrolling strip, divided by 9px dots. Read as `marquee-item` on the home page.

**Values (default).** size 96.06 x 28.78; background transparent; text Robin Semibold 12/14.4 600, #301816 `color.brand.dusk`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Section heading
A Boogy section heading inside a boxed section. Read as `section-h2` on the home page.

**Values (default).** size 779 x 104; background transparent; text Boogy 52/52 300, #ffffff `color.brand.white`.

![Section heading default](components/crops/section-h2-default.png)

#### Product card
A product-item card in the featured row: packshot, flavour title, price button; hover swaps to the second image. Read as `product-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 398.66 x 498.31; radius 45px; background transparent; text Robin Semibold 12/14.4 600, #301816 `color.brand.dusk`; layers button.button.button--primary 209.8x44.0 rgb(48, 24, 22); button::before.button.button--primary 20pxx44px rgb(48, 24, 22); button::after.button.button--primary 20pxx44px rgb(48, 24, 22) |
| hover | text Robin Semibold 12/14.4 500, #ffffff `color.brand.white` |
| focus-visible | layers a 0.0x0.0 1px auto rgb(0, 95, 204) offset 1px; button.button.button--primary 209.8x44.0 rgb(48, 24, 22); button::before.button.button--primary 20pxx44px rgb(48, 24, 22); button::after.button.button--primary 20pxx44px rgb(48, 24, 22) |
| pressed | text Robin Regular 16/19.2 500, #301816 `color.brand.dusk` |

Child layers that carry the look: button 209.8x44 background #301816 `color.brand.dusk` image linear-gradient(178deg, #301816 `color.brand.dusk`, #301816 `color.brand.dusk` 10%, rgba(0; button::before 20pxx44px background #301816 `color.brand.dusk`; button::after 20pxx44px background #301816 `color.brand.dusk`.

![Product card default](components/crops/product-item-default.png) ![Product card hover](components/crops/product-item-hover.png) ![Product card focus-visible](components/crops/product-item-focus-visible.png) ![Product card pressed](components/crops/product-item-pressed.png)

#### Product price
The price inside the card's quick-add button — the form reveals on card hover. Read as `product-price` on the home page.

**Values (default).** size 26.3 x 14.39; background transparent; text Robin Semibold 12/14.4 500, #ffffff `color.brand.white`.

![Product price default](components/crops/product-price-default.png)

#### Testimonial
A customer quote in the "Douze & vous" section. Read as `testimonial` on the home page.

**Values (default).** size 1390 x 453.31; radius 45px; background transparent; text Boogy 72/64.8 300, #301816 `color.brand.dusk`; icon 10 x 16, #ffffff `color.brand.white`; layers button.testimonials-2__nav-btn.testimonials-2__nav-btn--prev 35.0x35.0 rgb(186, 190, 197) T:1px solid rgb(255, 255, 255) / R:1px solid rgb(255, 255, 255) / B:1px solid rgb(255, 255, 255) / L:1px solid rgb(255, 255, 255) 50%; div.testimonials-2__item.text--center 450.0x368.5 rgb(48, 24, 22) 45px; div.testimonials-2__item.text--center 450.0x368.5 rgb(48, 24, 22) 45px; div.testimonials-2__item.text--.

Child layers that carry the look: button 35x35 background #babec5 border 1px solid #ffffff `color.brand.white` radius 50%; div 450x368.5 background #301816 `color.brand.dusk` radius 45px; div 450x368.5 background #301816 `color.brand.dusk` radius 45px.

![Testimonial default](components/crops/testimonial-default.png)

### Shop

The /collections/all grid: the image-hero banner, product-item cards whose quick-add form reveals on hover, and the sort control.

#### Shop banner
The collection page's image-hero band — the page leads with media; the heading node is a wordmark image with no live text. Read as `shop-title` on the shop page.

**Values (default).** size 1390 x 550; background transparent; text Robin Regular 16/19.2 500, #ffffff `color.brand.white`.

![Shop banner default](components/crops/shop-title-default.png)

#### Product card
A product-item in the /collections/all grid; its per-flavour --button-background-color rebinds the button fill (#f26554 for Orange Sanguine & Piment). Read as `product-card` on the shop page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 398.66 x 498.31; radius 45px; background transparent; text Robin Semibold 12/14.4 600, #301816 `color.brand.dusk`; layers button.button.button--primary 209.8x44.0 rgb(48, 24, 22); button::before.button.button--primary 20pxx44px rgb(48, 24, 22); button::after.button.button--primary 20pxx44px rgb(48, 24, 22) |
| hover | text Robin Semibold 12/14.4 500, #ffffff `color.brand.white` |
| pressed | text Robin Regular 16/19.2 500, #301816 `color.brand.dusk` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: button 209.8x44 background #301816 `color.brand.dusk` image linear-gradient(178deg, #301816 `color.brand.dusk`, #301816 `color.brand.dusk` 10%, rgba(0; button::before 20pxx44px background #301816 `color.brand.dusk`; button::after 20pxx44px background #301816 `color.brand.dusk`.

![Product card default](components/crops/product-card-default.png) ![Product card hover](components/crops/product-card-hover.png) ![Product card pressed](components/crops/product-card-pressed.png)

#### Product card wordmark
The flavour title on a grid card is a wordmark image (no live text), over a pack-line paragraph. Read as `product-card-title` on the shop page.

**Values (default).** size 378.66 x 65; background transparent; text Boogy 60/39 500, #301816 `color.brand.dusk`.

![Product card wordmark default](components/crops/product-card-title-default.png)

#### Quick-add price
The price span inside the quick-add button. Read as `product-card-price` on the shop page.

**Values (default).** size 26.3 x 14.39; background transparent; text Robin Semibold 12/14.4 500, #ffffff `color.brand.white`.

![Quick-add price default](components/crops/product-card-price-default.png)

#### Quick-add button
The card's Ajouter-au-panier — visibility:hidden until the card is hovered; the press posts to /cart/add so it is measured, never pressed. Read as `quick-add` on the shop page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 209.75 x 44; padding 0px 15px; background #301816 `color.brand.dusk`; image linear-gradient(178deg, #301816 `color.brand.dusk`, #301816 `color.brand.dusk` 10%, rgba(0, 0, 0, 0.07) 10%, rgba(0, 0, 0, 0.07) 100%), linear-gradient(#301816 `color.brand.dusk`, #301816 `color.brand; text Robin Semibold 12/14.4 500, #ffffff `color.brand.white`; transition transform 0.2s ease, box-shadow 0.2s ease; layers ::before rgb(48, 24, 22) 0px none 1; ::after rgb(48, 24, 22) 0px none 1 |
| hover | shadow rgba(0, 0, 0, 0.15) 0px 4px 8px 0px; transform translate(0px, -2px) |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | shadow rgba(0, 0, 0, 0.15) 0px 4px 8px 0px; outline 1px auto #005fcc, offset 0px; transform translate(0px, -2px) |

![Quick-add button default](components/crops/quick-add-default.png) ![Quick-add button hover](components/crops/quick-add-hover.png) ![Quick-add button focus-visible](components/crops/quick-add-focus-visible.png) ![Quick-add button pressed](components/crops/quick-add-pressed.png)

#### Sort control
A sort/filter control on the collection grid, if one paints. Read as `sort-control` on the shop page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 71.2 x 44; padding 8px 16px; border 1px solid #301816 `color.brand.dusk`; radius 999px; background #301816 `color.brand.dusk`; text Robin Semibold 12/14.4 500, #ffffff `color.brand.white`; transition transform 0.2s ease, box-shadow 0.2s ease; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | shadow rgba(0, 0, 0, 0.15) 0px 4px 8px 0px; transform translate(0px, -2px) |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | shadow rgba(0, 0, 0, 0.15) 0px 4px 8px 0px; transform translate(0px, -2px) |

![Sort control default](components/crops/sort-control-default.png) ![Sort control hover](components/crops/sort-control-hover.png) ![Sort control focus-visible](components/crops/sort-control-focus-visible.png) ![Sort control pressed](components/crops/sort-control-pressed.png)

#### Pagination
The grid's pagination, if the catalogue is long enough to need one. Read as `pagination` on the shop page.

Not on the page when it was captured.

#### Card pack line
The "6 canettes 25cl" pack description under the wordmark, h5 style. Read as `product-card-pack` on the shop page.

**Values (default).** size 252.56 x 14.39; background transparent; text Robin Semibold 12/14.4 600, #301816 `color.brand.dusk`.

![Card pack line default](components/crops/product-card-pack-default.png)

### Product page

The buy box on /products/orange-sanguine-piment and /products/trio-douze: the gallery, the 60px Boogy title, pack-size swatches, the Ajouter-au-panier submit (measured, never pressed), the reassurance lines and the Klaviyo reviews widget.

#### Product media
The packshot gallery left of the buy box. Read as `pdp-media` on the product page.

**Values (default).** size 695 x 810; background transparent; text Robin Regular 16/19.2 500, #301816 `color.brand.dusk`; layers div.product__media-image-wrapper 695.0x810.0 rgb(246, 242, 233); div.product__media-image-wrapper 695.0x810.0 rgb(246, 242, 233); div.product__media-image-wrapper 695.0x810.0 rgb(246, 242, 233); button.dots-nav__item.tap-area 0.0x0.0 rgb(48, 24, 22); button.dots-nav__item.tap-area 0.0x0.0 rgb(48, 24, 22); button.dots-nav__item.tap-area 0.0x0.0 rgb(48, 24, 22).

Child layers that carry the look: div 695x810 background #f6f2e9 `color.brand.sable`; div 695x810 background #f6f2e9 `color.brand.sable`; div 695x810 background #f6f2e9 `color.brand.sable`.

![Product media default](components/crops/pdp-media-default.png)

#### Product title
The 60px Boogy flavour title in the buy box. Read as `pdp-title` on the product page.

**Values (default).** size 403.33 x 80; background transparent; text Boogy 60/39 500, #301816 `color.brand.dusk`.

![Product title default](components/crops/pdp-title-default.png)

#### Price
The selling price figure (21.00€ for a 6-pack). Read as `pdp-price` on the product page.

**Values (default).** size 23.48 x 14.39; background transparent; text Robin Semibold 12/14.4 700, #ffffff `color.brand.white`.

![Price default](components/crops/pdp-price-default.png)

#### Pack-size swatch (checked)
The checked "6 Canettes" block-swatch radio label. Read as `variant-swatch` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 106.19 x 36.39; padding 10px; border 1px solid #301816 `color.brand.dusk`; radius 999px; background #f26554 `color.flavor.orange-piment`; text Robin Semibold 12/14.4 600, #301816 `color.brand.dusk`; transition background 0.2s ease |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Pack-size swatch (checked) default](components/crops/variant-swatch-default.png) ![Pack-size swatch (checked) hover](components/crops/variant-swatch-hover.png) ![Pack-size swatch (checked) pressed](components/crops/variant-swatch-pressed.png)

#### Pack-size swatch
An unchecked block-swatch option (12 Canettes), read at rest, on hover, on keyboard focus and forced pressed; the selected look is the separate swatch-selected entry. Never added to the cart. Read as `variant-swatch-2` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 111.83 x 36.39; padding 10px; border 1px solid #301816 `color.brand.dusk`; radius 999px; background #ffffff `color.brand.white`; text Robin Semibold 12/14.4 600, #301816 `color.brand.dusk`; transition background 0.2s ease |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Pack-size swatch default](components/crops/variant-swatch-2-default.png) ![Pack-size swatch hover](components/crops/variant-swatch-2-hover.png) ![Pack-size swatch pressed](components/crops/variant-swatch-2-pressed.png)

#### Swatch, newly selected
The 24-Canettes swatch in its selected state, reached by the swatch's own click. Read as `swatch-selected` on the product page.

**Values (selected).** size 113.8 x 36.39; padding 10px; border 1px solid #301816 `color.brand.dusk`; radius 999px; background #f26554 `color.flavor.orange-piment`; text Robin Semibold 12/14.4 600, #301816 `color.brand.dusk`; transition background 0.2s ease.

![Swatch, newly selected selected](components/crops/swatch-selected-selected.png)

#### Add to cart button
The "Ajouter au panier — 21€" submit; measured, never pressed — a press posts to /cart/add. Read as `add-to-cart` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 380 x 44; padding 0px 20px; background #301816 `color.brand.dusk`; image linear-gradient(178deg, #301816 `color.brand.dusk`, #301816 `color.brand.dusk` 10%, rgba(0, 0, 0, 0.07) 10%, rgba(0, 0, 0, 0.07) 100%), linear-gradient(#301816 `color.brand.dusk`, #301816 `color.brand; text Robin Semibold 12/14.4 500, #ffffff `color.brand.white`; transition transform 0.2s ease, box-shadow 0.2s ease; layers ::before rgb(48, 24, 22) 0px none 1; ::after rgb(48, 24, 22) 0px none 1 |
| hover | shadow rgba(0, 0, 0, 0.15) 0px 4px 8px 0px; transform translate(0px, -2px) |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | shadow rgba(0, 0, 0, 0.15) 0px 4px 8px 0px; transform translate(0px, -2px) |

![Add to cart button default](components/crops/add-to-cart-default.png) ![Add to cart button hover](components/crops/add-to-cart-hover.png) ![Add to cart button focus-visible](components/crops/add-to-cart-focus-visible.png) ![Add to cart button pressed](components/crops/add-to-cart-pressed.png)

#### Reassurance line
A trust line under the buy button ("livraison à J+2…"), dusk text with a flavour-coloured divider. Read as `reassurance` on the product page.

**Values (default).** size 245.11 x 26.38; background transparent; text Robin Semibold 11/13.2 500, #301816 `color.brand.dusk`.

![Reassurance line default](components/crops/reassurance-default.png)

#### Reviews tab
A Klaviyo-reviews tab ("Avis" / "Écrire un avis") — a vendor widget painted in the theme's chrome. Read as `reviews-tab` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 1304.69 x 52; border B: 1px solid #e9e9eb; background transparent; text Robin Regular 12/15 400, #ffffff `color.brand.white`; layers div.kl_reviews__list__tabs 1304.7x52.0 B:1px solid rgb(233, 233, 235); button.kl_reviews__button 89.7x31.0 rgb(48, 24, 22) 8px; button::after.kl_reviews__list__tab.kl_reviews__list__tab--active 71.625pxx5px rgb(33, 43, 55) 5px |
| focus-visible | layers div.kl_reviews__list__tabs 1304.7x52.0 B:1px solid rgb(233, 233, 235); button.kl_reviews__button 89.7x31.0 rgb(48, 24, 22) 3px solid rgb(33, 43, 55) offset 1px 8px; button::after.kl_reviews__list__tab.kl_reviews__list__tab--active 71.625pxx5px rgb(33, 43, 55) 5px |

Child layers that carry the look: div 1304.7x52 border 1px solid #e9e9eb; button 89.7x31 background #301816 `color.brand.dusk` radius 8px; button::after 71.625pxx5px background #212b37 radius 5px.

![Reviews tab default](components/crops/reviews-tab-default.png) ![Reviews tab hover](components/crops/reviews-tab-hover.png) ![Reviews tab focus-visible](components/crops/reviews-tab-focus-visible.png) ![Reviews tab pressed](components/crops/reviews-tab-pressed.png)

#### Review sort select
The Klaviyo reviews sort <select> — the one native select that paints signed out. Read as `sort-select` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 152 x 35.98; padding 8px 36px 8px 16px; radius 24px; background rgba(48, 24, 22, 0.1); text Robin Regular 12.04/19.98 500, #301816 `color.brand.dusk` |
| focus-visible | background rgba(23, 11, 10, 0.19) |

![Review sort select default](components/crops/sort-select-default.png) ![Review sort select hover](components/crops/sort-select-hover.png) ![Review sort select focus-visible](components/crops/sort-select-focus-visible.png) ![Review sort select pressed](components/crops/sort-select-pressed.png)

#### Bundle title
The Trio Douze buy-box title. Read as `trio-title` on the bundle product page.

**Values (default).** size 403.33 x 80; background transparent; text Boogy 60/39 500, #301816 `color.brand.dusk`.

![Bundle title default](components/crops/trio-title-default.png)

#### Purchase-option radio
The one-off vs. subscription radio in the buy box (it renders after the pack-size is settled, seen in the variant shot); never toggled past the default. Read as `subscription-radio` on the bundle product page.

Not on the page when it was captured.

### Content pages

The editorial surface: the story and FAQ pages' headings, prose and disclosure rows.

#### Page title
The "Page FAQ" heading — the page is a stub with no accordion painted signed out. Read as `faq-title` on the FAQ page.

**Values (default).** size 850 x 52; background transparent; text Boogy 52/52 300, #301816 `color.brand.dusk`.

![Page title default](components/crops/faq-title-default.png)

#### Accordion
A disclosure row, where one paints (none on the FAQ stub). Read as `accordion` on the FAQ page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 632.34 x 57; padding 21px 0px; background transparent; text Robin Semibold 12/14.4 600, #301816 `color.brand.dusk`; layers span::before.animated-plus 15pxx1px rgb(48, 24, 22); span::after.animated-plus 1pxx15px rgb(48, 24, 22) |
| focus-visible | outline 1px auto #005fcc, offset 0px; layers button.collapsible-toggle.h5 632.3x57.0 1px auto rgb(0, 95, 204) offset 0px; span::before.animated-plus 15pxx1px rgb(48, 24, 22); span::after.animated-plus 1pxx15px rgb(48, 24, 22) |

Child layers that carry the look: span::before 15pxx1px background #301816 `color.brand.dusk`; span::after 1pxx15px background #301816 `color.brand.dusk`.

![Accordion default](components/crops/accordion-default.png) ![Accordion hover](components/crops/accordion-hover.png) ![Accordion focus-visible](components/crops/accordion-focus-visible.png) ![Accordion pressed](components/crops/accordion-pressed.png)

#### Story title
The Notre-histoire page heading. Read as `story-h1` on the story page.

**Values (default).** size 524.13 x 104; background transparent; text Boogy 52/52 300, #f6f2e9 `color.brand.sable`.

![Story title default](components/crops/story-h1-default.png)

#### Story paragraph
A body paragraph in the story page, Robin Regular. Read as `story-lede` on the story page.

Mismeasured on the first pass and withdrawn: the selector caught the announcement-strip paragraph ("LIVRAISON GRATUITE EN FRANCE METROPOLITAINE A PARTIR DE 50EUR"), not a story body paragraph — no story paragraph was measured. The selector was tightened in tools/capture/public/measure.mjs; a live re-measure is queued.

#### Search title
The search results heading for ?q=douze. Read as `search-title` on the search page.

**Values (default).** size 704 x 52; background transparent; text Boogy 52/52 300, #301816 `color.brand.dusk`.

![Search title default](components/crops/search-title-default.png)

#### Search field
The search page's input, prefilled with "douze"; never re-submitted. Read as `search-field` on the search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 390 x 80; padding 0px 80px 0px 30px; border 1px solid #301816 `color.brand.dusk`; background transparent; text Robin Semibold 16/19.2 500, #301816 `color.brand.dusk`; transition border 0.2s ease-in-out, box-shadow 0.2s ease-in-out; placeholder rgba(48, 24, 22, 0.7) |
| focused | shadow #301816 0px 0px 0px 1px inset |

![Search field default](components/crops/search-field-default.png) ![Search field focused](components/crops/search-field-focused.png)

#### Search result card
A product result in the search grid. Read as `search-result` on the search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 229.25 x 286.56; radius 45px; background transparent; text Robin Semibold 12/14.4 600, #301816 `color.brand.dusk`; layers label.product-item__block-swatch 111.8x32.4 rgb(209, 232, 245) T:1px solid rgb(50, 26, 24) / R:1px solid rgb(50, 26, 24) / B:1px solid rgb(50, 26, 24) / L:1px solid rgb(50, 26, 24) 3.35544e+07px; label.product-item__block-swatch 113.8x32.4 rgb(255, 255, 255) T:1px solid rgb(50, 26, 24) / R:1px solid rgb(50, 26, 24) / B:1px solid rgb(50, 26, 24) / L:1px solid rgb(50, 26, 24) 3.35544e+07px; button.b |
| hover | layers label.product-item__block-swatch 111.8x32.4 rgb(209, 232, 245) T:1px solid rgb(48, 24, 22) / R:1px solid rgb(48, 24, 22) / B:1px solid rgb(48, 24, 22) / L:1px solid rgb(48, 24, 22) 3.35544e+07px; label.product-item__block-swatch 113.8x32.4 rgb(255, 255, 255) T:1px solid rgb(50, 26, 24) / R:1px solid rgb(50, 26, 24) / B:1px solid rgb(50, 26, 24) / L:1px solid rgb(50, 26, 24) 3.35544e+07px; button.b |
| focus-visible | layers a 0.0x0.0 1px auto rgb(0, 95, 204) offset 1px; label.product-item__block-swatch 111.8x32.4 rgb(209, 232, 245) T:1px solid rgb(50, 26, 24) / R:1px solid rgb(50, 26, 24) / B:1px solid rgb(50, 26, 24) / L:1px solid rgb(50, 26, 24) 3.35544e+07px; label.product-item__block-swatch 113.8x32.4 rgb(255, 255, 255) T:1px solid rgb(50, 26, 24) / R:1px solid rgb(50, 26, 24) / B:1px solid rgb(50, 26, 24) / L:1p |
| pressed | text Robin Regular 16/19.2 500, #301816 `color.brand.dusk` |

Child layers that carry the look: label 111.8x32.4 background #d1e8f5 border 1px solid #321a18 `color.brand.border` radius 3.35544e+07px; label 113.8x32.4 background #ffffff `color.brand.white` border 1px solid #321a18 `color.brand.border` radius 3.35544e+07px; button 209.3x44 background #301816 `color.brand.dusk` image linear-gradient(178deg, #301816 `color.brand.dusk`, #301816 `color.brand.dusk` 10%, rgba(0.

![Search result card default](components/crops/search-result-default.png) ![Search result card hover](components/crops/search-result-hover.png) ![Search result card focus-visible](components/crops/search-result-focus-visible.png) ![Search result card pressed](components/crops/search-result-pressed.png)

### Account and cart

The signed-out boundary surfaces: the customer login card (never submitted) and the empty-cart state — the only cart surface reachable without adding an item.

#### Login card
The centred customer-login card; never filled or submitted. Read as `login-card` on the account login page.

**Values (default).** size 480 x 481.56; padding 44px 48px; radius 45px; background #f6f2e9 `color.brand.sable`; text Boogy Italic 72/86.4 300, #301816 `color.brand.dusk`.

![Login card default](components/crops/login-card-default.png)

#### Email field
The E-mail input with its floating label; sample text was typed and deleted, nothing sent. Read as `email-field` on the account login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 384 x 52; padding 0px 18px; border 1px solid #301816 `color.brand.dusk`; radius 16px; background transparent; text Robin Semibold 12/14.4 500, #301816 `color.brand.dusk`; transition border 0.2s ease-in-out, box-shadow 0.2s ease-in-out; placeholder rgba(48, 24, 22, 0.6) |
| focused, filled | shadow #301816 0px 0px 0px 1px inset |

![Email field default](components/crops/email-field-default.png) ![Email field focused](components/crops/email-field-focused.png) ![Email field filled](components/crops/email-field-filled.png)

#### Password field
The Mot-de-passe input; focused only, never filled. Read as `password-field` on the account login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 384 x 52; padding 0px 18px; border 1px solid #301816 `color.brand.dusk`; radius 16px; background transparent; text Robin Semibold 12/14.4 500, #301816 `color.brand.dusk`; transition border 0.2s ease-in-out, box-shadow 0.2s ease-in-out; placeholder rgba(48, 24, 22, 0.6) |
| focused | shadow #301816 0px 0px 0px 1px inset |

![Password field default](components/crops/password-field-default.png) ![Password field focused](components/crops/password-field-focused.png)

#### Login button
The Se-connecter submit; measured, never pressed (a press would submit). Read as `login-button` on the account login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 384 x 44; padding 0px 15px; background #301816 `color.brand.dusk`; image linear-gradient(178deg, #301816 `color.brand.dusk`, #301816 `color.brand.dusk` 10%, rgba(0, 0, 0, 0.07) 10%, rgba(0, 0, 0, 0.07) 100%), linear-gradient(#301816 `color.brand.dusk`, #301816 `color.brand; text Robin Semibold 12/14.4 500, #ffffff `color.brand.white`; transition transform 0.2s ease, box-shadow 0.2s ease; layers ::before rgb(48, 24, 22) 0px none 1; ::after rgb(48, 24, 22) 0px none 1 |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | shadow rgba(0, 0, 0, 0.15) 0px 4px 8px 0px; transform translate(0px, -2px) |

![Login button default](components/crops/login-button-default.png) ![Login button hover](components/crops/login-button-hover.png) ![Login button focus-visible](components/crops/login-button-focus-visible.png) ![Login button pressed](components/crops/login-button-pressed.png)

#### Recover toggle
The "Mot de passe oublié ?" button, which swaps the card to the recover form in place; measured at rest, on hover, on keyboard focus and forced pressed, never clicked, so the swap is not captured. Read as `recover-link` on the account login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 163.78 x 14.39; background transparent; text Robin Regular 12/14.4 500, #301816 `color.brand.dusk` |
| focus-visible | outline 1px auto #005fcc, offset 0px; layers button.customer-form-card__forgot-link 163.8x14.4 1px auto rgb(0, 95, 204) offset 0px |

![Recover toggle default](components/crops/recover-link-default.png) ![Recover toggle hover](components/crops/recover-link-hover.png) ![Recover toggle focus-visible](components/crops/recover-link-focus-visible.png) ![Recover toggle pressed](components/crops/recover-link-pressed.png)

#### Cart, empty
The "Votre panier est vide" empty state — the only cart surface reachable without adding an item. Read as `cart-empty` on the cart page.

**Values (default).** size 1162.22 x 197.98; background transparent; text Boogy 72/64.8 300, #301816 `color.brand.dusk`; layers a.button.button--primary 1162.2x44.0 rgb(48, 24, 22); a::before.button.button--primary 20pxx44px rgb(48, 24, 22); a::after.button.button--primary 20pxx44px rgb(48, 24, 22).

Child layers that carry the look: a 1162.2x44 background #301816 `color.brand.dusk` image linear-gradient(178deg, #301816 `color.brand.dusk`, #301816 `color.brand.dusk` 10%, rgba(0; a::before 20pxx44px background #301816 `color.brand.dusk`; a::after 20pxx44px background #301816 `color.brand.dusk`.

![Cart, empty default](components/crops/cart-empty-default.png)

#### Empty-cart CTA
The "Explorer nos produits" action in the empty state. Read as `cart-cta` on the cart page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1162.22 x 44; padding 0px 15px; background #301816 `color.brand.dusk`; image linear-gradient(178deg, #301816 `color.brand.dusk`, #301816 `color.brand.dusk` 10%, rgba(0, 0, 0, 0.07) 10%, rgba(0, 0, 0, 0.07) 100%), linear-gradient(#301816 `color.brand.dusk`, #301816 `color.brand; text Robin Semibold 12/14.4 500, #ffffff `color.brand.white`; transition transform 0.2s ease, box-shadow 0.2s ease; layers ::before rgb(48, 24, 22) 0px none 1; ::after rgb(48, 24, 22) 0px none 1 |
| hover | shadow rgba(0, 0, 0, 0.15) 0px 4px 8px 0px; transform translate(0px, -2px) |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | shadow rgba(0, 0, 0, 0.15) 0px 4px 8px 0px; transform translate(0px, -2px) |

![Empty-cart CTA default](components/crops/cart-cta-default.png) ![Empty-cart CTA hover](components/crops/cart-cta-hover.png) ![Empty-cart CTA focus-visible](components/crops/cart-cta-focus-visible.png) ![Empty-cart CTA pressed](components/crops/cart-cta-pressed.png)

#### Register link
The "S'inscrire" link to /account/register. Read as `register-link` on the account login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 74.17 x 14.39; background transparent; text Robin Regular 12/14.4 500, #301816 `color.brand.dusk` |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.customer-form-card__footer-link 74.2x14.4 1px auto rgb(0, 95, 204) offset 1px |

![Register link default](components/crops/register-link-default.png) ![Register link hover](components/crops/register-link-hover.png) ![Register link focus-visible](components/crops/register-link-focus-visible.png) ![Register link pressed](components/crops/register-link-pressed.png)

### Footer

The boxed footer over its photo background: link columns, the Klaviyo newsletter embed (never submitted) and the locale selector.

#### Footer
The boxed footer section over its photo background: nav columns, the "La News Douze" Klaviyo signup and the locale selector. Read as `footer` on the home page.

**Values (default).** size 1390 x 903.17; padding 20px 0px; radius 45px; background #f6f2e9 `color.brand.sable`; image url(…); text Robin Semibold 12/14.4 600, #f6f2e9 `color.brand.sable`.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer nav link. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 37.69 x 15; background transparent; text Robin Semibold 12/14.4 600, #f6f2e9 `color.brand.sable` |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.h5 37.7x15.0 1px auto rgb(0, 95, 204) offset 1px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Newsletter field
The email input inside the footer's Klaviyo embed; focused only, never filled or submitted. Read as `newsletter-field` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 450 x 34; border B: 1px solid #f6f2e9 `color.brand.sable`; background rgba(255, 255, 255, 0); text Robin Semibold 12/14.4 400, #f6f2e9 `color.brand.sable`; placeholder #f6f2e9 `color.brand.sable` |
| focused | outline 2px auto #f6f2e9 `color.brand.sable`, offset 0px |

![Newsletter field default](components/crops/newsletter-field-default.png) ![Newsletter field focused](components/crops/newsletter-field-focused.png)

#### Newsletter button
The signup submit inside the Klaviyo embed; measured, never pressed. Read as `newsletter-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 32 x 34; padding 0px 10px; background rgba(38, 133, 59, 0); text Nunito-Sans-Klaviyo-Hosted 20/20 400, #f6f2e9 `color.brand.sable` |
| focus-visible | outline 2px auto #f6f2e9 `color.brand.sable`, offset 0px |

![Newsletter button default](components/crops/newsletter-button-default.png) ![Newsletter button hover](components/crops/newsletter-button-hover.png) ![Newsletter button focus-visible](components/crops/newsletter-button-focus-visible.png) ![Newsletter button pressed](components/crops/newsletter-button-pressed.png)

#### Social icon link
A social link, where the footer paints one (none in the captured DOM). Read as `social-icon` on the home page.

Not on the page when it was captured.

#### Locale button
The FRANÇAIS locale selector in the footer. Read as `locale-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 110.77 x 26.39; padding 6px 12px; background transparent; text Robin Semibold 12/14.4 600, #f6f2e9 `color.brand.sable`; icon 9 x 6, #f6f2e9 `color.brand.sable` |
| focus-visible | outline 1px auto #005fcc, offset 0px; layers button.select.select--small 110.8x26.4 1px auto rgb(0, 95, 204) offset 0px |

![Locale button default](components/crops/locale-button-default.png) ![Locale button hover](components/crops/locale-button-hover.png) ![Locale button focus-visible](components/crops/locale-button-focus-visible.png) ![Locale button pressed](components/crops/locale-button-pressed.png)

### Mobile (390 wide)

The storefront at phone width: the compact header, the from-left navigation drawer and the stacked hero.

#### Mobile header
The compact header at 390: hamburger, wordmark, cart. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 360 x 65; background transparent; text Robin Regular 9/8.55 600, #f6f2e9 `color.brand.sable`; transition background 0.2s ease-in-out, color 0.2s ease-in-out, box-shadow 0.2s ease-in-out; icon 18 x 14, #301816 `color.brand.dusk`; layers a::after.header__linklist-link.link--animated 100%x1px rgb(48, 24, 22); a::after.header__linklist-link.link--animated 100%x1px rgb(48, 24, 22); a::after.header__linklist-link.link--animated 100%x1px rgb(48, 24, 22); a::after.header__linklist-link.link--animated 100%x1px rgb(48, 24, 22); a::after.header__linklist-link.link--animated 100%x1px rgb(48, 24, 22); a::after.header__linklist-link.link--ani.

Child layers that carry the look: a::after 100%x1px background #301816 `color.brand.dusk`; a::after 100%x1px background #301816 `color.brand.dusk`; a::after 100%x1px background #301816 `color.brand.dusk`.

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
The hamburger toggle for the mobile-navigation drawer. Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 18 x 14; background transparent; text Robin Regular 16/19.2 500, #301816 `color.brand.dusk`; icon 18 x 14, #301816 `color.brand.dusk`; layers ::before rgba(0, 0, 0, 0) 0px none 1.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The from-left navigation drawer opened by its own toggle. Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 844; background #ffffff `color.brand.white`; text Robin Semibold 12/13.44 300, #301816 `color.brand.dusk`; transition transform 0.6s cubic-bezier(0.75, 0, 0.175, 1), visibility 0.6s cubic-bezier(0.75, 0, 0.175, 1); icon 14 x 14, #301816 `color.brand.dusk`.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Mobile nav item
A link inside the opened navigation drawer. Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 390 x 45.44; padding 16px 40px; background transparent; text Robin Semibold 12/13.44 300, #301816 `color.brand.dusk` |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.mobile-nav__link.heading 390.0x45.4 1px auto rgb(0, 95, 204) offset 1px |

![Mobile nav item default](components/crops/m-nav-item-default.png) ![Mobile nav item hover](components/crops/m-nav-item-hover.png) ![Mobile nav item focus-visible](components/crops/m-nav-item-focus-visible.png) ![Mobile nav item pressed](components/crops/m-nav-item-pressed.png)

#### Mobile hero title
The Boogy hero heading at 390 (the hidden-tablet-and-up variant). Read as `m-hero-title` on the home page at 390 wide.

Mismeasured on the first pass and withdrawn: the selector caught the hero SHOP button container, not the mobile Boogy heading — the 390px hero heading was not measured. The selector was tightened in tools/capture/public/measure.mjs; a live re-measure is queued.

#### Mobile hero CTA
The SHOP button at 390. Read as `m-hero-cta` on the home page at 390 wide.

**Values (default).** size 77.69 x 38; padding 0px 20px; background #301816 `color.brand.dusk`; text Robin Semibold 12/14.4 500, #ffffff `color.brand.white`; transition transform 0.2s ease, box-shadow 0.2s ease; layers ::before rgb(48, 24, 22) 0px none 1; ::after rgb(48, 24, 22) 0px none 1.

![Mobile hero CTA default](components/crops/m-hero-cta-default.png)

#### Mobile product card
A product-item in the featured row at 390. Read as `m-product-card` on the home page at 390 wide.

**Values (default).** size 316 x 395; radius 22.5px; background transparent; text Robin Semibold 12/14.4 600, #301816 `color.brand.dusk`; transform translate(0px, 5.99359px); opacity 0.828755; layers button.button.button--primary 219.8x38.0 rgb(48, 24, 22); button::before.button.button--primary 20pxx38px rgb(48, 24, 22); button::after.button.button--primary 20pxx38px rgb(48, 24, 22).

Child layers that carry the look: button 219.8x38 background #301816 `color.brand.dusk`; button::before 20pxx38px background #301816 `color.brand.dusk`; button::after 20pxx38px background #301816 `color.brand.dusk`.

![Mobile product card default](components/crops/m-product-card-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the DOUZE wordmark, the bag/person/envelope glyphs, the flavour wordmark images and the packshots) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in and paid product

Douze's commerce — a filled cart, Shopify checkout, payment, the customer account area and subscription management — was never reached: nothing was added to the cart (the quick-add and Ajouter-au-panier submits were measured, never pressed), no form was ever sent, and /account/* beyond the login and register forms needs a customer account. The subscription widget (Appstle) did not render on the captured bundle page signed out.

### Pages

- **Checkout.** Shopify's /checkout was never reached — the one hard boundary of a DTC storefront. The cart was captured only in its empty state; line items, the free-shipping meter and the checkout button inside the filled cart are uncaptured.
- **Account.** /account and /account/register past the forms need a customer session; the login card was measured and its fields filled once and emptied, never submitted.
- **Newsletter drawer and Klaviyo popup.** The header's envelope toggle is display:none at both captured widths and the Klaviyo popup never mounted during the pass, so the newsletter drawer is documented but unmeasured; the footer's embedded Klaviyo form was measured instead.
- **Shop dropdown.** The Shop nav link is marked has-dropdown, but its panel is not in the signed-out DOM on hover — likely mounted by an interaction we did not perform.
- **Store locator.** The page paints its stockist content inside the theme; a map widget, if one exists, is a vendor embed.
- **/en.** The English locale home exists but duplicates the French surface; only the French surface was captured.

### States

- **Pressed** was forced with DevTools (`CSS.forcePseudoState` :active:hover) on the controls, so a state a script adds on mousedown (if any) is missing.
- **Quick-add** was measured under its designed reveal — the form is visibility:hidden until the card is hovered; its own hover/focus states paint with the card already hovered.
- **Selected swatch** was reached by the swatch radio's own click (a local UI state); nothing was added to the cart.
- **Disabled, error and loading states** were not seen on the public surface (the sold-out accent is declared in the sheets but no sold-out product paints it).

### Themes

The site paints light only: no prefers-color-scheme rule, no dark scope. Photo sections — the hero, the footer — re-bind the same roles so type paints sable-on-media; those are kept as light.inverse tokens, not a second theme.

### Fonts

- **Boogy** and **Boogy Italic** (display, weight 300) and **Robin Regular** / **Robin Semibold** (body 500, strong 600) are served as WOFF2 from the Shopify CDN; Jost and Barlow also ship for vendor widgets. The style guide falls back to system serif and sans.

### Screenshots

- Packshots, flavour wordmark images (the card titles are images, not live text), photography, the DOUZE wordmark and testimonial content in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Product copy, recipe text, reviews and the editorial pages' prose are the product's content; only frames and components were measured.
