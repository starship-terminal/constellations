# Avnier components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from avnier.com on 2026-11-11, signed out, in headless Chrome at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was added to cart, signed into, created, sent or uploaded.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (42 components, 80 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (79 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: the shop paints one light theme. Desktop shots are 1440 x 900 at 1x, including the `-full` whole-page shots; mobile shots are `mobile-{page}-light-{state}.png` at 2x, so a 390-wide viewport — and a 390-wide full page — comes out 780 pixels wide. Read mobile sizes at half the pixels.

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [consent](screenshots/home-light-consent.png), [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Shop grid | `/collections/tous-les-produits` | [default](screenshots/shop-light-default.png), [full](screenshots/shop-light-full.png) |
| Product page | `first product on the shop grid` | [default](screenshots/pdp-light-default.png), [full](screenshots/pdp-light-full.png), [variant-picked](screenshots/pdp-light-variant-picked.png) |
| Cart | `/cart` | [default](screenshots/cart-light-default.png), [full](screenshots/cart-light-full.png) |
| Login gate | `/account/login` | [default](screenshots/login-light-default.png), [full](screenshots/login-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Shop grid, phone | `/collections/tous-les-produits` | [default](screenshots/mobile-shop-light-default.png), [full](screenshots/mobile-shop-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Axeptio consent layer and shipping-country popup | every page, on load | the country popup captured as it arrives, then both hidden (never answered: no Accept/Reject is ever clicked) | [home-light-consent](screenshots/home-light-consent.png) |
| Category mega-menu | category nav, shop grid | the first nav button hovered; the flyout shows in the crop | [nav-flyout](#category-flyout-panel), [nav-mega](#category-flyout-open) |
| PDP size select | product page | a size option picked then restored; never added to bag | [size-select-picked](components/crops/size-select-picked.png), [size-select](#size-select) |
| PDP accordion | product page | a disclosure row's own toggle | [pdp-accordion-open-opened](components/crops/pdp-accordion-open-opened.png), [pdp-accordion](#pdp-accordion) |
| Mobile side-panel menu | home, phone | the menu button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 12 components were given a real keyboard focus. 0 draw an outline ring: . 2 draw a focus ring as a shadow instead: `skip-link`, `cart-cta`. The other 10 show no measured change: `nav-item`, `search-toggle`, `account-link`, `cart-link`, `hero-cta`, `card-name`, `add-to-cart`, `login-button`, `m-menu-button`, `footer-link`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover): controls keep their shape — Avnier answers hover with fill swaps rather than scale or shadow. Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `ease` | box-shadow | add-to-cart, cart-cta, email-input, login-button, password-input, skip-link, sort-select |
| 0.2s | `ease` | all | variant-radio |
| 0.24s | `ease` | background-color | cart-drawer |
| 0.25s | `ease` | all | footer-link, newsletter-input |
| 0.35s | `ease` | all | m-nav-link |
| 0.4s | `ease` | background-color | header, m-header |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Mobile content tile](#mobile-content-tile) | 390 x 390 | - | - | rgba(0, 0, 0, 0.1) | none | 390px 0px 0px 0px |

## Components

### Shell and navigation

The header (wordmark, SHOP/MARQUE/SECONDE MAIN/ARCHIVE SALE, search, CONNEXION, PANIER) and the SHOP mega-menu.

#### Skip link
"IGNORER ET PASSER AU CONTENU" — off-screen until focused. Read as `skip-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 120 x 45; padding 9px 30px 11px 30px; border 1px solid transparent; background #000000 `color.neutral.accent1`; shadow #000000 0px 0px 0px 1px; text Space Mono 15/18 400, #ffffff `color.neutral.background`; transition box-shadow 0.1s ease |
| focus-visible | size 347.05 x 45; shadow #000000 0px 0px 0px 1px, #ffffff 0px 0px 0px 3px, rgba(0, 0, 0, 0.3) 0px 0px 5px 4px |

![Skip link default](components/crops/skip-link-default.png) ![Skip link focus-visible](components/crops/skip-link-focus-visible.png)

#### Header
The white bar: wordmark, SHOP/MARQUE/SECONDE MAIN/ARCHIVE SALE nav, search, CONNEXION and PANIER. Read as `header` on the home page.

**Values (default).** size 1440 x 60; padding 10px 50px; background transparent; text Space Mono 13/normal 400, #ffffff `color.neutral.background`; transition background-color 0.4s ease; layers div.mega-menu__dropdown 0.0x0.0 rgb(117, 117, 117) T:1px solid rgb(255, 255, 255) / R:1px solid rgb(255, 255, 255) / B:1px solid rgb(255, 255, 255) / L:1px solid rgb(255, 255, 255); a::after.dropdown-item__list-item-link 0pxx100% rgb(244, 255, 122); a::after.dropdown-item__list-item-link 0pxx100% rgb(244, 255, 122); a::after.dropdown-item__list-item-link 0pxx100% rgb(244, 255, 122); a::after.dropd.

Child layers that carry the look: div 0x0 background #757575 border 1px solid #ffffff `color.neutral.background`; a::after 0pxx100% background #f4ff7a `measured.action-pressed`; a::after 0pxx100% background #f4ff7a `measured.action-pressed`.

![Header default](components/crops/header-default.png)

#### Logo
The wordmark link (a hidden drawer copy is filtered out). Read as `logo` on the home page.

**Values (default).** size 155 x 38.5; padding 7.5px; background transparent; text avnier-font 14/0 500, #000000 `color.neutral.accent1`.

![Logo default](components/crops/logo-default.png)

#### Nav link
A top-level nav link (SECONDE MAIN). Measured, never followed. Read as `nav-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 95.48 x 20; background transparent; text Space Mono 13/normal 400, #ffffff `color.neutral.background` |

![Nav link default](components/crops/nav-item-default.png) ![Nav link hover](components/crops/nav-item-hover.png) ![Nav link focus-visible](components/crops/nav-item-focus-visible.png) ![Nav link pressed](components/crops/nav-item-pressed.png)

#### SHOP menu item, hover
The SHOP item while its mega-menu dropdown is open. Read as `nav-mega` on the home page.

**Values (hover).** size 85.83 x 64; padding 22px 27px; background transparent; text Space Mono 13/normal 400, #ffffff `color.neutral.background`.

![SHOP menu item, hover hover](components/crops/nav-mega-hover.png)

#### Mega-menu dropdown
The open SHOP dropdown panel. Read as `nav-dropdown` on the page.

Not on the page when it was captured.

#### Search icon
The magnifier that opens the search modal. Measured, never submitted. Read as `search-toggle` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 40 x 40; background transparent; text Space Mono 14/0 400, #ffffff `color.neutral.background`; icon 20 x 20, #ffffff `color.neutral.background` |
| pressed | icon 21.4 x 21.4, #ffffff `color.neutral.background` |

![Search icon default](components/crops/search-toggle-default.png) ![Search icon hover](components/crops/search-toggle-hover.png) ![Search icon focus-visible](components/crops/search-toggle-focus-visible.png) ![Search icon pressed](components/crops/search-toggle-pressed.png)

#### Login link
CONNEXION in the header. Measured, never followed. Read as `account-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 40 x 40; background transparent; text Space Mono 14/normal 400, #ffffff `color.neutral.background`; icon 20 x 20, #ffffff `color.neutral.background` |
| pressed | icon 21.4 x 21.4, #ffffff `color.neutral.background` |

![Login link default](components/crops/account-link-default.png) ![Login link hover](components/crops/account-link-hover.png) ![Login link focus-visible](components/crops/account-link-focus-visible.png) ![Login link pressed](components/crops/account-link-pressed.png)

#### Cart link
PANIER in the header. Measured, never followed. Read as `cart-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 40 x 40; background transparent; text Space Mono 14/normal 400, #ffffff `color.neutral.background`; icon 40 x 40, #ffffff `color.neutral.background` |
| pressed | icon 42.8 x 42.8, #ffffff `color.neutral.background` |

![Cart link default](components/crops/cart-link-default.png) ![Cart link hover](components/crops/cart-link-hover.png) ![Cart link focus-visible](components/crops/cart-link-focus-visible.png) ![Cart link pressed](components/crops/cart-link-pressed.png)

### Home

The collaboration hero and the content tiles below.

#### Hero
The collection announcement block under the header. Read as `hero` on the home page.

**Values (default).** size 799 x 799; padding 799px 0px 0px 0px; background rgba(0, 0, 0, 0.1); text Space Mono 13/normal 400, #000000 `color.neutral.accent1`.

![Hero default](components/crops/hero-default.png)

#### Hero CTA
The first call-to-action on the home page. Measured, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 481 x 30; background transparent; text Space Mono 13/normal 400, #ffffff `color.neutral.background`; icon 30 x 30, #ffffff `color.neutral.background`; layers span::after 0pxx1px rgb(244, 255, 122) |
| pressed | layers span::after 232.859pxx1px rgb(244, 255, 122) |

Child layers that carry the look: span::after 0pxx1px background #f4ff7a `measured.action-pressed`.

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

### Shop grid

The collection grid: count, PRIX/COULEUR/TAILLE facets, sort and product cards.

#### Collection count
The "100 PRODUITS" count / collection heading. Read as `plp-title` on the shop grid page.

**Values (default).** size 59.98 x 17.5; background transparent; text Space Mono 14/17.5 400, #7a7a7a `measured.text-muted`.

![Collection count default](components/crops/plp-title-default.png)

#### Facet filter
A PRIX/COULEUR/TAILLE filter disclosure; opened by its own summary. Read as `facet` on the shop grid page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: opened) | size 74.92 x 36; background transparent; text Space Mono 14/21 400, #000000 `color.neutral.accent1`; layers div.facets__display 350.0x237.0 rgb(255, 255, 255) T:1px solid rgba(0, 0, 0, 0.2) / R:1px solid rgba(0, 0, 0, 0.2) / B:1px solid rgba(0, 0, 0, 0.2) / L:1px solid rgba(0, 0, 0, 0.2); div.facets__header 348.0x52.0 rgb(255, 255, 255) B:1px solid rgba(0, 0, 0, 0.2); span 20.0x20.0 T:1px solid rgb(0, 0, 0) / R:1px solid rgb(0, 0, 0) / B:1px solid rgb(0, 0, 0) / L:1px solid rgb(0, 0, 0) 50%; span 20.0x2 |

Child layers that carry the look: div 350x237 background #ffffff `color.neutral.background` border 1px solid rgba(0, 0, 0, 0.2); div 348x52 background #ffffff `color.neutral.background` border 1px solid rgba(0, 0, 0, 0.2); span 20x20 border 1px solid #000000 `color.neutral.accent1` radius 50%.

![Facet filter default](components/crops/facet-default.png) ![Facet filter opened](components/crops/facet-opened.png)

#### Facet checkbox
A checkbox row inside the open COULEUR facet. Read as `facet-checkbox` on the shop grid page.

**Values (default).** size 16 x 16; background transparent; text Space Mono 13.33/normal 400, #000000 `color.neutral.accent1`; placeholder #000000 `color.neutral.accent1`.

![Facet checkbox default](components/crops/facet-checkbox-default.png)

#### Sort select
The "Recommandés" sort dropdown. Read as `sort-select` on the shop grid page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 166 x 21; padding 0px 20px 0px 0px; background transparent; text Space Mono 14/21 400, rgba(0, 0, 0, 0.75) `measured.text-faded`; transition box-shadow 0.1s ease |

![Sort select default](components/crops/sort-select-default.png) ![Sort select focused](components/crops/sort-select-focused.png)

#### Product card
A grid card: image, name, price. Read as `product-card` on the shop grid page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 450 x 562.5; background transparent; text Space Mono 13/normal 400, #000000 `color.neutral.accent1`; layers a 72.0x36.0 rgb(255, 255, 255) T:1px solid rgb(0, 0, 0) / R:1px solid rgb(0, 0, 0) / B:1px solid rgb(0, 0, 0) / L:1px solid rgb(0, 0, 0); a 72.0x36.0 rgb(255, 255, 255) T:1px solid rgb(0, 0, 0) / R:1px solid rgb(0, 0, 0) / B:1px solid rgb(0, 0, 0) / L:1px solid rgb(0, 0, 0); a 72.0x36.0 rgb(255, 255, 255) T:1px solid rgb(0, 0, 0) / R:1px solid rgb(0, 0, 0) / B:1px solid rgb(0, 0, 0) / L:1px solid  |

Child layers that carry the look: a 72x36 background #ffffff `color.neutral.background` border 1px solid #000000 `color.neutral.accent1`; a 72x36 background #ffffff `color.neutral.background` border 1px solid #000000 `color.neutral.accent1`; a 72x36 background #ffffff `color.neutral.background` border 1px solid #000000 `color.neutral.accent1`.

![Product card default](components/crops/product-card-default.png) ![Product card hover](components/crops/product-card-hover.png)

#### Card link
The product name/link inside a card. Read as `card-name` on the shop grid page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 450 x 562.5; background transparent; text Space Mono 13/normal 400, #000000 `color.neutral.accent1` |

![Card link default](components/crops/card-name-default.png) ![Card link hover](components/crops/card-name-hover.png) ![Card link focus-visible](components/crops/card-name-focus-visible.png) ![Card link pressed](components/crops/card-name-pressed.png)

#### Card price
Read as `card-price` on the shop grid page.

**Values (default).** size 68.42 x 18; background transparent; text Space Mono 12/18 400, #000000 `color.neutral.accent1`.

![Card price default](components/crops/card-price-default.png)

### Product page

Title, price, TAILLE chips and the black AJOUTER AU PANIER button.

#### Product title
Read as `pdp-title` on the product page.

**Values (default).** size 440 x 18; background transparent; text avnier-font 15/18 500, #000000 `color.neutral.accent1`.

![Product title default](components/crops/pdp-title-default.png)

#### Product price
Read as `pdp-price` on the product page.

**Values (default).** size 440 x 27.5; background transparent; text avnier-font 15/22.5 400, #000000 `color.neutral.accent1`.

![Product price default](components/crops/pdp-price-default.png)

#### Variant option
A TAILLE size chip — the visible label of a visually hidden radio input. Read as `variant-radio` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 73.2 x 40; border T: 1px solid #000000 `color.neutral.accent1`; B: 1px solid #000000 `color.neutral.accent1`; L: 1px solid #000000 `color.neutral.accent1`; background #000000 `color.neutral.accent1`; text Space Mono 14/14 400, #ffffff `color.neutral.background`; transition all 0.2s ease; icon 13 x 9.75, #ffffff `color.neutral.background` |
| hover | shadow #000000 0px 0px 0px 1px inset; text Space Mono 14/14 700, #ffffff `color.neutral.background` |

![Variant option default](components/crops/variant-radio-default.png) ![Variant option hover](components/crops/variant-radio-hover.png)

#### Quantity field
Read as `qty-input` on the page.

Not on the page when it was captured.

#### Add to cart
The AJOUTER AU PANIER buy button; measured in every state except a real press. Read as `add-to-cart` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 440 x 48; padding 9px 30px 11px 30px; border 1px solid #000000 `color.neutral.accent1`; background #000000 `color.neutral.accent1`; text Space Mono 15/18 400, #f6f6f6 `measured.action-text`; transition box-shadow 0.1s ease; layers ::after rgb(244, 255, 122) 0px none 1 |
| hover | text Space Mono 15/18 400, #dcdcdc |
| pressed | text Space Mono 15/18 400, #000000 `color.neutral.accent1` |

![Add to cart default](components/crops/add-to-cart-default.png) ![Add to cart hover](components/crops/add-to-cart-hover.png) ![Add to cart focus-visible](components/crops/add-to-cart-focus-visible.png) ![Add to cart pressed](components/crops/add-to-cart-pressed.png)

#### PDP accordion
A disclosure row (Description / Livraison…) — none on the captured product. Read as `accordion` on the product page.

Not on the page when it was captured.

### Cart

The public /cart page, empty signed out.

#### /cart 404 title
The 404 page /cart serves — the cart is the drawer, measured next. Read as `cart-title` on the cart page.

**Values (default).** size 1440 x 188; background transparent; text avnier-font 188/188 500, rgba(10, 10, 10, 0).

![/cart 404 title default](components/crops/cart-title-default.png)

#### Empty cart
LE PANIER EST VIDE in the drawer. Read as `cart-empty` on the cart page.

**Values (default).** size 458 x 20; background transparent; text Space Mono 13/normal 400, #000000 `color.neutral.accent1`.

![Empty cart default](components/crops/cart-empty-default.png)

#### Cart CTA
Measured, never followed. Read as `cart-cta` on the cart page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 265.61 x 45; padding 9px 30px 11px 30px; border 1px solid transparent; background #000000 `color.neutral.accent1`; shadow #000000 0px 0px 0px 1px; text Space Mono 15/18 400, #ffffff `color.neutral.background`; transition box-shadow 0.1s ease |
| focus-visible | shadow #000000 0px 0px 0px 1px, #ffffff 0px 0px 0px 3px, rgba(0, 0, 0, 0.3) 0px 0px 5px 4px |
| pressed | shadow none |

![Cart CTA default](components/crops/cart-cta-default.png) ![Cart CTA hover](components/crops/cart-cta-hover.png) ![Cart CTA focus-visible](components/crops/cart-cta-focus-visible.png) ![Cart CTA pressed](components/crops/cart-cta-pressed.png)

#### Cart drawer
The side-cart opened by PANIER — "MON PANIER - 0 ARTICLE" empty. Read as `cart-drawer` on the cart page.

**Values (default).** size 1440 x 900; background rgba(0, 0, 0, 0.55) `measured.border-field`; text avnier-font 14/20.02 500, #000000 `color.neutral.accent1`; transition background-color 0.24s ease; icon 16 x 16, #000000 `color.neutral.accent1`.

![Cart drawer default](components/crops/cart-drawer-default.png)

### Login gate

The public /account/login form; nothing was submitted.

#### Login title
Read as `login-title` on the login gate page.

**Values (default).** size 448 x 223; background transparent; text avnier-font 220/220 500, rgba(10, 10, 10, 0).

![Login title default](components/crops/login-title-default.png)

#### Email field
Text was typed and deleted; the form was never submitted. Read as `email-input` on the login gate page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 448 x 45; padding 15px; border 1px solid transparent; background transparent; shadow rgba(0, 0, 0, 0.55) 0px 0px 0px 1px; text Space Mono 16/24 400, #000000 `color.neutral.accent1`; transition box-shadow 0.1s ease; placeholder #757575 |

![Email field default](components/crops/email-input-default.png) ![Email field focused](components/crops/email-input-focused.png)

#### Password field
Focused only; nothing typed. Read as `password-input` on the login gate page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 448 x 45; padding 15px; border 1px solid transparent; background transparent; shadow rgba(0, 0, 0, 0.55) 0px 0px 0px 1px; text Space Mono 16/24 400, #000000 `color.neutral.accent1`; transition box-shadow 0.1s ease; placeholder #757575 |
| focused | padding 16px; shadow rgba(0, 0, 0, 0.75) 0px 0px 0px 2px |

![Password field default](components/crops/password-input-default.png) ![Password field focused](components/crops/password-input-focused.png)

#### Login button
The submit; measured except a real press — the form was never submitted. Read as `login-button` on the login gate page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 153.63 x 48; padding 9px 30px 11px 30px; border 1px solid transparent; background #000000 `color.neutral.accent1`; text Space Mono 15/18 400, #ffffff `color.neutral.background`; transition box-shadow 0.1s ease; layers ::after rgb(244, 255, 122) 0px none 1 |

![Login button default](components/crops/login-button-default.png) ![Login button hover](components/crops/login-button-hover.png) ![Login button focus-visible](components/crops/login-button-focus-visible.png)

### Footer

The page footer, social icons and newsletter field.

#### Footer
Read as `footer` on the home page.

**Values (default).** size 1340 x 70; padding 20px 50px; border T: 1px solid rgba(255, 255, 255, 0.22); background transparent; text Space Mono 12/15 400, #ffffff `color.neutral.background`.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 190.86 x 36.8; padding 10px 0px; background transparent; text Space Mono 12/16.8 400, #ffffff `color.neutral.background`; transition all 0.25s ease; opacity 0.75 |
| pressed | opacity none |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Newsletter field
Focused only; never subscribed. Read as `newsletter-input` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 320 x 45; padding 15px; border 1px solid #ffffff `color.neutral.background`; background transparent; shadow rgba(0, 0, 0, 0.55) 0px 0px 0px 1px; text Space Mono 12/15 400, #ffffff `color.neutral.background`; transition all 0.25s ease; opacity 0.75; placeholder #ffffff `color.neutral.background` |
| focused | padding 16px; shadow rgba(0, 0, 0, 0.75) 0px 0px 0px 2px; opacity none |

![Newsletter field default](components/crops/newsletter-input-default.png) ![Newsletter field focused](components/crops/newsletter-input-focused.png)

### Mobile (390 wide)

The same surface at phone width, with the side-panel menu open.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 50.94; padding 10px 15px; background transparent; text Space Mono 10/normal 400, #ffffff `color.neutral.background`; transition background-color 0.4s ease; layers div.mega-menu__dropdown 0.0x0.0 rgb(117, 117, 117) T:1px solid rgb(255, 255, 255) / R:1px solid rgb(255, 255, 255) / B:1px solid rgb(255, 255, 255) / L:1px solid rgb(255, 255, 255); a::after.dropdown-item__list-item-link 0pxx100% rgb(244, 255, 122); a::after.dropdown-item__list-item-link 0pxx100% rgb(244, 255, 122); a::after.dropdown-item__list-item-link 0pxx100% rgb(244, 255, 122); a::after.dropd.

Child layers that carry the look: div 0x0 background #757575 border 1px solid #ffffff `color.neutral.background`; a::after 0pxx100% background #f4ff7a `measured.action-pressed`; a::after 0pxx100% background #f4ff7a `measured.action-pressed`.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile menu button
Read as `m-menu-button` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 35 x 30; background transparent; text Space Mono 10/normal 400, #ffffff `color.neutral.background`; icon 20 x 20, #ffffff `color.neutral.background` |
| hover, pressed | icon 21.4 x 21.4, #ffffff `color.neutral.background` |

![Mobile menu button default](components/crops/m-menu-button-default.png) ![Mobile menu button hover](components/crops/m-menu-button-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-button-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-button-pressed.png)

#### Mobile menu, open
The menu summary after its own toggle; the crop is the open drawer. Read as `m-menu-open` on the home page at 390 wide.

**Values (opened).** size 35 x 30; background transparent; text Space Mono 10/normal 400, #ffffff `color.neutral.background`; icon 16 x 16, #ffffff `color.neutral.background`.

![Mobile menu, open opened](components/crops/m-menu-open-opened.png)

#### Mobile nav link
A row inside the opened drawer. Read as `m-nav-link` on the home page at 390 wide.

**Values (default).** size 388 x 59.11; padding 10px 10px 10px 20px; border T: 1px solid #ffffff `color.neutral.background`; B: 1px solid #ffffff `color.neutral.background`; background transparent; text avnier-font 20/22.8 500, #ffffff `color.neutral.background`; transition all 0.35s ease; icon 35 x 37.11, #000000 `color.neutral.accent1`.

![Mobile nav link default](components/crops/m-nav-link-default.png)

#### Mobile content tile
A content tile under the hero. Read as `m-feature-tile` on the home page at 390 wide.

**Values (default).** size 390 x 390; padding 390px 0px 0px 0px; background rgba(0, 0, 0, 0.1); text Space Mono 12/normal 400, #000000 `color.neutral.accent1`.

![Mobile content tile default](components/crops/m-feature-tile-default.png)

### Other



### Other



## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots are Avnier's artwork (inline SVG). Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Pages

- **Checkout and anything behind sign-in.** No item was added to the cart, so checkout, delivery options, payment and account pages were never reached. The `/account/login` gate itself is public and is measured; it was never submitted. The cart page is public but empty for a signed-out visitor, and is recorded that way.
- **Anything that buys, sends or joins.** No product was added to the bag, no form was submitted (the login email was typed into and cleared), no search was run, no account was created, no consent choice was made.
- **The mega-menu columns, the account dropdown and the filter/sort panels** were opened or hovered but their innards were not measured beyond the first link.
- **The home page's category nav** stays `display:none` on `/` — it is measured on the shop grid, where the row is visible, and the home screenshot records the nav-less layout as served.
- **Headless access.** avnier.com serves headless Chrome (channel `chrome`) a 200, so the whole capture ran headless; a challenge page, had one appeared, was waited out, never bypassed.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Keyboard focus on the header search button** did not land (recorded as an error state on `search-button`, not as evidence). Focus states on flyout links do not exist: the flyout closes the moment focus leaves the nav button.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

The site paints one light theme on every captured route; a `.dark` probe resolves every custom property identically. The vendor custom properties (`--ll-*`, `--swiper-*`, 80 names: Loloyal's loyalty widget, which carries its own `.ll-dark-mode`, and Swiper's carousel) are recorded in [raw/css-vars.json](raw/css-vars.json) and never tokenised. No dark or reduced-contrast mode is offered.

### Fonts

- **avnier-font** is the licensed display face — every page title and product name; **Space Mono** (400) covers all body, nav, field and button text. avnier-font is not distributed; the style guide falls back to a system font.
- Font Awesome and VideoJS faces ship inside widgets only.

### Screenshots

- Product photography, campaign imagery and the AVNIER wordmark in the screenshots are Avnier's content. The PDP captured is whichever product the shop grid listed first at run time (recorded as `pdp_url` in components-computed.json); another run may land on a different product. The site serves French copy (fr-FR); prices are in EUR.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Product photography and campaign imagery are the product's content; only the frames and components were measured.
