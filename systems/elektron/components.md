# Elektron components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from elektron.se on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, submitted or paid for; the magic-login form was measured and its email field given sample text that was deleted again — no code was ever requested; the ADD TO CART, EXPLORE, SUBMIT and CONTINUE SHOPPING actions were never pressed, and checkout was never reached.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (47 components, 106 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Neue Haas Grotesk Text Pro 14/21 400, #eeeef2`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (103 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every captured surface paints `dark` — the site has one theme, a #151515 ground with #eeeef2 text, and no switch. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [account](screenshots/home-dark-account.png), [default](screenshots/home-dark-default.png), [full](screenshots/home-dark-full.png), [search](screenshots/home-dark-search.png) |
| Shop | `/shop` | [default](screenshots/shop-dark-default.png), [full](screenshots/shop-dark-full.png) |
| Digitakt II product page | `/product/digitakt-ii` | [default](screenshots/product-digitakt-dark-default.png), [features](screenshots/product-digitakt-dark-features.png), [full](screenshots/product-digitakt-dark-full.png) |
| PL-2 protective lid product page | `/product/pl-2-protective-lid` | [default](screenshots/product-accessory-dark-default.png) |
| Explore index | `/explore` | [default](screenshots/explore-dark-default.png), [full](screenshots/explore-dark-full.png) |
| Kulture magazine | `/kulture` | [default](screenshots/kulture-dark-default.png), [full](screenshots/kulture-dark-full.png) |
| Support downloads | `/support-downloads` | [default](screenshots/support-dark-default.png), [full](screenshots/support-dark-full.png) |
| Who we are | `/who-we-are` | [default](screenshots/about-dark-default.png), [full](screenshots/about-dark-full.png) |
| Contact | `/contact-us` | [default](screenshots/contact-dark-default.png), [full](screenshots/contact-dark-full.png) |
| Cart (empty drawer) | `/cart` | [default](screenshots/cart-dark-default.png) |
| My account (signed out) | `/my-account` | [default](screenshots/my-account-dark-default.png), [full](screenshots/my-account-dark-full.png) |
| Store locator | `/store-locator` | [default](screenshots/store-locator-dark-default.png), [full](screenshots/store-locator-dark-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-dark-default.png), [full](screenshots/mobile-home-dark-full.png), [menu](screenshots/mobile-home-dark-menu.png) |
| Shop, phone | `/shop` | [default](screenshots/mobile-shop-dark-default.png), [full](screenshots/mobile-shop-dark-full.png) |
| Digitakt II, phone | `/product/digitakt-ii` | [default](screenshots/mobile-product-digitakt-dark-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu overlay | home, phone width | the header menu button's own toggle | [mobile-home-dark-menu](screenshots/mobile-home-dark-menu.png), [m-menu-open](#mobile-menu-open), [m-nav-item](#mobile-nav-item) |
| Search dropdown | the header | the Search action's own toggle | [home-dark-search](screenshots/home-dark-search.png), [search-modal](#search-dropdown), [search-field](#search-field) |
| Account drawer | the header | the Account action's own toggle | [home-dark-account](screenshots/home-dark-account.png), [account-modal](#account-drawer), [magic-email](#magic-login-email-field), [magic-send](#send-me-a-code-button) |
| Key Features accordion | /product/digitakt-ii | the accordion row's own toggle | [product-digitakt-dark-features](screenshots/product-digitakt-dark-features.png), [accordion](#key-features-accordion) |
| Cart drawer | /cart | the page's own empty-cart dialog | [cart-dark-default](screenshots/cart-dark-default.png), [cart-drawer](#mini-cart-drawer), [cart-continue](#continue-shopping-action) |
| Cookie consent banner | every page | hidden, never answered — the thedock consent modal was hidden, not consented | hidden before every shot and reading |
| Magic login | the Account drawer and /my-account | measured at rest; the Email field was focused and given sample text that was deleted — no code was ever requested | [login-panel](#login-panel), [login-email](#login-email-field), [login-send](#send-me-a-code-button-2), [login-create](#create-account-button) |
| The signed-in account and checkout | /my-account, /checkout | behind sign-in; the login card was measured, never used | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 14 components were given a real keyboard focus. 14 draw an outline ring: `nav-link` (2px solid #000000, offset 2px), `nav-icon-link` (2px solid #000000, offset 2px), `magic-send` (2px solid #000000, offset 2px), `pdp-explore` (2px solid #000000, offset 2px), `add-to-cart` (2px solid #000000, offset 2px), `explore-link` (2px solid #000000, offset 2px), `download-row` (2px solid #000000, offset 2px), `submit-button` (2px solid #000000, offset 2px), `cart-continue` (2px solid #000000, offset 2px), `login-send` (2px solid #000000, offset 2px), `login-create` (2px solid #000000, offset 2px), `footer-link` (2px solid #000000, offset 2px), `social-icon` (2px solid #000000, offset 2px), `m-nav-item` (2px solid #000000, offset 2px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.3s | `ease` | background-color, background-position, background-size, border, opacity | accordion, download-row, m-nav-item, nav-icon-link, nav-link |
| 0.4s | `cubic-bezier(0, 1.05, 0.65, 1.01)` | height | m-header |
| 0.4s | `cubic-bezier(0.365, 0.305, 0, 1)` | -webkit-transform, background-color, color, transform | header, m-header |
| 0.4s | `ease` | background-size | add-to-cart, cart-continue, explore-link, footer-link, login-create, login-send, magic-send, pdp-explore and more |
| 0.5s | `ease` | background-image | accordion, download-row, m-nav-item, nav-icon-link, nav-link |
| 0.8s | `cubic-bezier(0.365, 0.305, 0, 1)` | -webkit-box-shadow, box-shadow | m-header |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Product card](#product-card) | 691.31 x 26.97 | - | - | transparent | none | 0 |
| [Account drawer](#account-drawer) | 1440 x 844 | - | - | transparent | none | 0 |
| [Mini-cart drawer](#mini-cart-drawer) | 1440 x 900 | - | - | transparent | none | 0 |
| [Login panel](#login-panel) | 392 x 141.59 | - | - | transparent | none | 0 |

## Components

### Shell and navigation

The 56px transparent header over the #151515 page: Catalog / Shop / Kulture / Search on the left, the Elektron wordmark centre, Support / Account / Cart on the right — 14px Neue Haas Text labels with 28px icons.

#### Header
The 56px transparent top bar over the page: Catalog / Shop / Kulture / Search on the left, the Elektron mark centre, Support / Account / Cart on the right — Neue Haas Grotesk Text 14px labels with small icons. Read as `header` on the home page.

**Values (default).** size 1440 x 56; background transparent; text Neue Haas Grotesk Text Pro 14/21 400, #eeeef2 `color.neutral.paper`; transition color 0.4s cubic-bezier(0.365, 0.305, 0, 1), background-color 0.4s cubic-bezier(0.365, 0.305, 0, 1), transform 0.4s cubic-bezier(0.365, 0.305, 0, 1), -webkit-transform 0.4s cubic-bezier(0.365, 0.305, 0, 1); icon 28 x 28, #eeeef2 `color.neutral.paper`; layers div.element-background.has-center-center-position 1440.0x56.0 rgb(21, 21, 21); span 54.3x21.0; span 35.9x21.0; span 50.1x21.0; span 49.3x21.0; span 55.8x21.0.

Child layers that carry the look: div 1440x56 background #151515 `color.neutral.ink`; span 54.3x21 image linear-gradient(to right, #333333 `color.neutral.sweep` 0%, #333333 `color.neutral.sweep` ; span 35.9x21 image linear-gradient(to right, #333333 `color.neutral.sweep` 0%, #333333 `color.neutral.sweep` .

![Header default](components/crops/header-default.png)

#### Logo
The Elektron wordmark anchor at the centre of the header. Read as `logo` on the home page.

**Values (default).** size 35 x 24.86; background transparent; text Neue Haas Grotesk Text Pro 14/21 400, #eeeef2 `color.neutral.paper`; icon 35 x 24.86, #eeeef2 `color.neutral.paper`.

![Logo default](components/crops/logo-default.png)

#### Nav link
A header destination anchor (Catalog / Shop / Kulture): a .block-button.button-small_text row 28px tall, icon left of a 14px label. Measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 70.92 x 28; background transparent; text Neue Haas Grotesk Text Pro 14/21 400, #eeeef2 `color.neutral.paper`; transition border 0.3s ease, background-color 0.3s ease, background-position 0.3s ease, background-size 0.3s ease, background-image 0.5s ease, opacity 0.3s ease; icon 28 x 28, #eeeef2 `color.neutral.paper`; layers span 35.9x21.0 |
| focus-visible | shadow #ffffff 0px 0px 0px 2px; outline 2px solid #000000, offset 2px; layers a.block-button.button-small_text 70.9x28.0 rgb(255, 255, 255) 0px 0px 0px 2px 2px solid rgb(0, 0, 0) offset 2px; span 35.9x21.0 |

Child layers that carry the look: span 35.9x21 image linear-gradient(to right, #333333 `color.neutral.sweep` 0%, #333333 `color.neutral.sweep` .

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Nav icon link
A right-side header action (Support / Account / Cart): label left of a small icon. Cart opens the mini-cart drawer — measured, never followed to checkout. Read as `nav-icon-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 65.53 x 28; background transparent; text Neue Haas Grotesk Text Pro 14/21 400, #eeeef2 `color.neutral.paper`; transition border 0.3s ease, background-color 0.3s ease, background-position 0.3s ease, background-size 0.3s ease, background-image 0.5s ease, opacity 0.3s ease; icon 28 x 28, #eeeef2 `color.neutral.paper`; layers span 30.5x21.0; span.num-cart-items 0.0x0.0 |
| focus-visible | shadow #ffffff 0px 0px 0px 2px; outline 2px solid #000000, offset 2px; layers a.block-button.button-small_text 65.5x28.0 rgb(255, 255, 255) 0px 0px 0px 2px 2px solid rgb(0, 0, 0) offset 2px; span 30.5x21.0; span.num-cart-items 0.0x0.0 |

Child layers that carry the look: span 30.5x21 image linear-gradient(to right, #333333 `color.neutral.sweep` 0%, #333333 `color.neutral.sweep` ; span 0x0 image linear-gradient(to right, #333333 `color.neutral.sweep` 0%, #333333 `color.neutral.sweep` .

![Nav icon link default](components/crops/nav-icon-link-default.png) ![Nav icon link hover](components/crops/nav-icon-link-hover.png) ![Nav icon link focus-visible](components/crops/nav-icon-link-focus-visible.png) ![Nav icon link pressed](components/crops/nav-icon-link-pressed.png)

### Dialogs and overlays

The header's modal surfaces: the Search dropdown with its full-width field, and the Account drawer (a 420px right panel on #212121) carrying the magic-login form — an Email field and Send me a code, plus Create New Account. Measured, never used.

#### Search dropdown
The header Search dropdown: a large search-field row under the header. Read as `search-modal` on the home page.

**Values (opened).** size 1440 x 6785.33; background transparent; text Neue Haas Grotesk Text Pro 14/21 400, #eeeef2 `color.neutral.paper`; icon 28 x 28, #eeeef2 `color.neutral.paper`; layers div.element-background.has-center-center-position 1440.0x56.0 rgb(21, 21, 21); span 54.3x21.0; span 35.9x21.0; span 50.1x21.0; span 49.3x21.0; span 55.8x21.0.

Child layers that carry the look: div 1440x56 background #151515 `color.neutral.ink`; span 54.3x21 image linear-gradient(to right, #333333 `color.neutral.sweep` 0%, #333333 `color.neutral.sweep` ; span 35.9x21 image linear-gradient(to right, #333333 `color.neutral.sweep` 0%, #333333 `color.neutral.sweep` .

![Search dropdown opened](components/crops/search-modal-opened.png)

#### Search field
The big search input inside the Search dropdown ("Type and press enter to search"). Sample text was typed and deleted; the query was never submitted. Read as `search-field` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1440 x 40.5; padding 10.5px 17.5px; border 1px solid #151515 `color.neutral.ink`; radius 7px; background #151515 `color.neutral.ink`; text Analog One V2. 14/17.5 400, #eeeef2 `color.neutral.paper`; placeholder #757575 `color.neutral.placeholder` |
| focused, filled | shadow #ffffff 0px 0px 0px 2px; outline 2px solid #000000, offset 2px |

![Search field default](components/crops/search-field-default.png) ![Search field focused](components/crops/search-field-focused.png) ![Search field filled](components/crops/search-field-filled.png)

#### Account drawer
The header Account modal (modal-layout-drawer-right): the magic-login panel — a Log in step (Email field, Send me a code) and Create New Account. Measured, never used. Read as `account-modal` on the home page.

**Values (opened).** size 1440 x 844; background transparent; text Neue Haas Grotesk Text Pro 17.99/26.98 400, #eeeef2 `color.neutral.paper`; icon 35 x 35, #eeeef2 `color.neutral.paper`; layers div.element-background.has-center-center-position 1440.0x844.0 rgb(21, 21, 21); div.element-background.has-center-center-position 420.0x844.0 rgb(33, 33, 33); hr.wp-block-separator.thickness-normal 392.0x2.0 rgb(128, 128, 128); input.block-input.button-full_form 0.0x0.0 rgb(238, 238, 242); input.block-input.button-full_form 0.0x0.0 rgb(238, 238, 242); input.block-input.has-undefined-background-col.

Child layers that carry the look: div 1440x844 background #151515 `color.neutral.ink`; div 420x844 background #212121 `color.neutral.raised`; hr 392x2 background #808080 `color.neutral.rule`.

![Account drawer opened](components/crops/account-modal-opened.png)

#### Magic-login email field
The Email input of the magic-login drawer: a 42px block-input field. Sample text was typed and deleted; no code was ever requested. Read as `magic-email` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 392 x 42; padding 10.5px 44px 10.5px 17.5px; background #eeeef2 `color.neutral.paper`; text digi one v2 14/21 400, #151515 `color.neutral.ink`; placeholder #757575 `color.neutral.placeholder` |
| focused, filled | background #151515 `color.neutral.ink`; shadow #ffffff 0px 0px 0px 2px; outline 2px solid #000000, offset 2px; text digi one v2 14/21 400, #eeeef2 `color.neutral.paper` |

![Magic-login email field default](components/crops/magic-email-default.png) ![Magic-login email field focused](components/crops/magic-email-focused.png) ![Magic-login email field filled](components/crops/magic-email-filled.png)

#### Send me a code button
The magic-login submit: a full-width secondary-variant block-button (grey fill, dark label, digi one v2). Measured, never pressed. Read as `magic-send` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 392 x 42; padding 10.5px 17.5px; background #cccccc `color.neutral.grey`; image linear-gradient(to right, #333333 `color.neutral.sweep` 0%, #333333 `color.neutral.sweep` 100%); text digi one v2 14/21 400, #151515 `color.neutral.ink`; transition background-size 0.4s ease |
| hover | background #151515 `color.neutral.ink`; text digi one v2 14/21 400, #cccccc `color.neutral.grey` |
| focus-visible, pressed | background #151515 `color.neutral.ink`; shadow #ffffff 0px 0px 0px 2px; outline 2px solid #000000, offset 2px; text digi one v2 14/21 400, #cccccc `color.neutral.grey` |

![Send me a code button default](components/crops/magic-send-default.png) ![Send me a code button hover](components/crops/magic-send-hover.png) ![Send me a code button focus-visible](components/crops/magic-send-focus-visible.png) ![Send me a code button pressed](components/crops/magic-send-pressed.png)

### About

The page headings: the 31px home hero title, the 64px display that section and page titles take, and the who-we-are heading.

#### Page title
The home page heading. Read as `hero-h1` on the home page.

**Values (default).** size 284.63 x 40.95; background transparent; text Neue Haas Grotesk Display Pro 30.8/40.96 400, #eeeef2 `color.neutral.paper`.

![Page title default](components/crops/hero-h1-default.png)

#### Section heading
A section heading below the fold. Read as `section-h2` on the home page.

**Values (default).** size 749 x 60.84; background transparent; text Neue Haas Grotesk Display Pro 64.05/60.84 500, #eeeef2 `color.neutral.paper`.

![Section heading default](components/crops/section-h2-default.png)

#### About title
Read as `about-title` on the who-we-are page.

**Values (default).** size 128.94 x 31.94; background transparent; text Neue Haas Grotesk Display Pro 24.01/31.93 400, #eeeef2 `color.neutral.paper`.

![About title default](components/crops/about-title-default.png)

### Shop

The /shop product grid: each row is a product name in 18px Neue Haas Text, a one-line descriptor and the $ price.

#### Product card
A shop-grid product block: product name (18px Neue Haas Text), a one-line descriptor and the price in $. Measured, never followed. Read as `product-card` on the shop page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 691.31 x 26.97; background transparent; text Neue Haas Grotesk Text Pro 17.99/26.98 400, #eeeef2 `color.neutral.paper` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Product card default](components/crops/product-card-default.png) ![Product card hover](components/crops/product-card-hover.png) ![Product card pressed](components/crops/product-card-pressed.png)

#### Product card title
Read as `product-card-title` on the shop page.

**Values (default).** size 84.55 x 26.97; background transparent; text Neue Haas Grotesk Text Pro 17.99/26.98 400, #eeeef2 `color.neutral.paper`.

![Product card title default](components/crops/product-card-title-default.png)

#### Product card subtitle
Read as `product-card-sub` on the shop page.

**Values (default).** size 261.42 x 21; background transparent; text Neue Haas Grotesk Text Pro 14/21 400, #eeeef2 `color.neutral.paper`.

![Product card subtitle default](components/crops/product-card-sub-default.png)

#### Price
A product price figure ("349 $"). Read as `price` on the shop page.

**Values (default).** size 57.52 x 26.97; background transparent; text Neue Haas Grotesk Text Pro 17.99/26.98 400, #eeeef2 `color.neutral.paper`.

![Price default](components/crops/price-default.png)

### Product pages

The product detail surface (Digitakt II and the PL-2 protective lid): the 18px name and price, the Key Features accordion, the full-width EXPLORE outline action, and ADD TO CART — a 2px paper-outline 46px block-button. Measured, never pressed.

#### Product title
The product name on the detail page, 18px Neue Haas Text. Read as `pdp-title` on the product page.

**Values (default).** size 86.38 x 26.97; background transparent; text Neue Haas Grotesk Text Pro 17.99/26.98 400, #eeeef2 `color.neutral.paper`.

![Product title default](components/crops/pdp-title-default.png)

#### Product price
The product price figure ("1149 $"). Read as `pdp-price` on the product page.

**Values (default).** size 56.89 x 26.97; background transparent; text Neue Haas Grotesk Text Pro 17.99/26.98 400, #eeeef2 `color.neutral.paper`.

![Product price default](components/crops/pdp-price-default.png)

#### Explore button
The full-width outline action on the product page (EXPLORE DIGITAKT II): a .block-button.button-outline, 2px #eeeef2 border, transparent fill, digi one v2 14px caps at 46px tall. Measured, never followed. Read as `pdp-explore` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 461.33 x 46; padding 10.5px 17.5px; border 2px solid #eeeef2 `color.neutral.paper`; background transparent; image linear-gradient(to right, #333333 `color.neutral.sweep` 0%, #333333 `color.neutral.sweep` 100%); text digi one v2 14/21 400, #eeeef2 `color.neutral.paper`; transition background-size 0.4s ease |
| hover | background #eeeef2 `color.neutral.paper`; text digi one v2 14/21 400, #151515 `color.neutral.ink` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px; outline 2px solid #000000, offset 2px |
| pressed | background #eeeef2 `color.neutral.paper`; text digi one v2 14/21 400, #151515 `color.neutral.ink` |

![Explore button default](components/crops/pdp-explore-default.png) ![Explore button hover](components/crops/pdp-explore-hover.png) ![Explore button focus-visible](components/crops/pdp-explore-focus-visible.png) ![Explore button pressed](components/crops/pdp-explore-pressed.png)

#### Key Features accordion
A 24px Neue Haas Grotesk Display block row with a right icon that expands the feature section — a local UI toggle. Read as `accordion` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, opened) | size 461.33 x 37.81; background transparent; text Neue Haas Grotesk Display Pro 24.01/36.01 450, #eeeef2 `color.neutral.paper`; transition border 0.3s ease, background-color 0.3s ease, background-position 0.3s ease, background-size 0.3s ease, background-image 0.5s ease, opacity 0.3s ease; layers span 146.6x36.0 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: span 146.6x36 image linear-gradient(to right, #333333 `color.neutral.sweep` 0%, #333333 `color.neutral.sweep` .

![Key Features accordion default](components/crops/accordion-default.png) ![Key Features accordion hover](components/crops/accordion-hover.png) ![Key Features accordion pressed](components/crops/accordion-pressed.png) ![Key Features accordion opened](components/crops/accordion-opened.png)

#### Product title (accessory)
Read as `pdp-title-accessory` on the product page.

**Values (default).** size 173.94 x 26.97; background transparent; text Neue Haas Grotesk Text Pro 17.99/26.98 400, #eeeef2 `color.neutral.paper`.

![Product title (accessory) default](components/crops/pdp-title-accessory-default.png)

#### Add to cart button
The in-stock product action: a 2px #eeeef2 outline block-button, digi one v2 14px caps, 46px tall. Measured, never pressed — nothing was added to the cart. Read as `add-to-cart` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 244.67 x 46; padding 10.5px 17.5px; border 2px solid #eeeef2 `color.neutral.paper`; background transparent; image linear-gradient(to right, #333333 `color.neutral.sweep` 0%, #333333 `color.neutral.sweep` 100%); text digi one v2 14/21 400, #eeeef2 `color.neutral.paper`; transition background-size 0.4s ease |
| hover | background #eeeef2 `color.neutral.paper`; text digi one v2 14/21 400, #151515 `color.neutral.ink` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px; outline 2px solid #000000, offset 2px |
| pressed | background #eeeef2 `color.neutral.paper`; text digi one v2 14/21 400, #151515 `color.neutral.ink` |

![Add to cart button default](components/crops/add-to-cart-default.png) ![Add to cart button hover](components/crops/add-to-cart-hover.png) ![Add to cart button focus-visible](components/crops/add-to-cart-focus-visible.png) ![Add to cart button pressed](components/crops/add-to-cart-pressed.png)

### Explore

The /explore index: 44px Neue Haas Display product-name rows with the underline-sweep hover.

#### Explore title
Read as `explore-title` on the explore page.

**Values (default).** size 219.03 x 42.16; background transparent; text Neue Haas Grotesk Display Pro 44.39/42.17 500, #eeeef2 `color.neutral.paper`; layers a 223.5x53.0.

Child layers that carry the look: a 223.5x53 image linear-gradient(to right, #333333 `color.neutral.sweep` 0%, #333333 `color.neutral.sweep` .

![Explore title default](components/crops/explore-title-default.png)

#### Explore product link
A product-name row in the Explore index; measured, never followed. Read as `explore-link` on the explore page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 322.45 x 53; padding 0px 4.43912px; background transparent; image linear-gradient(to right, #333333 `color.neutral.sweep` 0%, #333333 `color.neutral.sweep` 100%); text Neue Haas Grotesk Display Pro 44.39/42.17 500, #eeeef2 `color.neutral.paper`; transition background-size 0.4s ease |
| focus-visible | shadow #ffffff 0px 0px 0px 2px; outline 2px solid #000000, offset 2px |

![Explore product link default](components/crops/explore-link-default.png) ![Explore product link hover](components/crops/explore-link-hover.png) ![Explore product link focus-visible](components/crops/explore-link-focus-visible.png) ![Explore product link pressed](components/crops/explore-link-pressed.png)

### Support and downloads

The /support-downloads page title with its hanging bullet, the action rows, and the /store-locator title.

#### Support title
The 64px Neue Haas Grotesk Display page title. Read as `support-title` on the support page.

**Values (default).** size 400.31 x 121.69; padding 0px 0px 0px 70px; background transparent; text Neue Haas Grotesk Display Pro 64.05/60.84 500, #eeeef2 `color.neutral.paper`; layers ::before rgba(0, 0, 0, 0) 0px none 1.

![Support title default](components/crops/support-title-default.png)

#### Support action link
A support/downloads action row (a .block-button.button-text link with a right icon) in the page content. Measured, never followed. Read as `download-row` on the support page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 28 x 28; background transparent; text Neue Haas Grotesk Text Pro 14/21 400, #eeeef2 `color.neutral.paper`; transition border 0.3s ease, background-color 0.3s ease, background-position 0.3s ease, background-size 0.3s ease, background-image 0.5s ease, opacity 0.3s ease; icon 28 x 28, #eeeef2 `color.neutral.paper` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px; outline 2px solid #000000, offset 2px; layers a.block-button.button-text 28.0x28.0 rgb(255, 255, 255) 0px 0px 0px 2px 2px solid rgb(0, 0, 0) offset 2px |

![Support action link default](components/crops/download-row-default.png) ![Support action link hover](components/crops/download-row-hover.png) ![Support action link focus-visible](components/crops/download-row-focus-visible.png) ![Support action link pressed](components/crops/download-row-pressed.png)

#### Store locator title
Read as `locator-title` on the store-locator page.

**Values (default).** size 400.31 x 121.69; padding 0px 0px 0px 70px; background transparent; text Neue Haas Grotesk Display Pro 64.05/60.84 500, #eeeef2 `color.neutral.paper`; layers ::before rgba(0, 0, 0, 0) 0px none 1.

![Store locator title default](components/crops/locator-title-default.png)

### Contact

The /contact-us form: the 42px light-filled block-inputs (text, select, textarea) and the outline SUBMIT — measured, never sent.

#### Contact title
The 64px Neue Haas Grotesk Display Pro 500 page title. Read as `contact-title` on the contact page.

**Values (default).** size 373.03 x 60.84; padding 0px 0px 0px 70px; background transparent; text Neue Haas Grotesk Display Pro 64.05/60.84 500, #eeeef2 `color.neutral.paper`; layers ::before rgba(0, 0, 0, 0) 0px none 1.

![Contact title default](components/crops/contact-title-default.png)

#### Text field
A 42px block-input: #eeeef2 field, #151515 text, Neue Haas Text 14px, square corners. Sample text was typed and deleted; the form was never submitted. Read as `text-field` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 609 x 42; padding 10.5px 14px; background #eeeef2 `color.neutral.paper`; text Neue Haas Grotesk Text Pro 14/21 400, #151515 `color.neutral.ink`; placeholder #757575 `color.neutral.placeholder` |
| focused, filled | shadow #ffffff 0px 0px 0px 2px; outline 2px solid #000000, offset 2px |

![Text field default](components/crops/text-field-default.png) ![Text field focused](components/crops/text-field-focused.png) ![Text field filled](components/crops/text-field-filled.png)

#### Select field
The Category select: same 42px field treatment; never changed. Read as `select-field` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 609 x 42; padding 10.5px 35px 10.5px 14px; background #eeeef2 `color.neutral.paper`; text Neue Haas Grotesk Text Pro 14/21 400, #151515 `color.neutral.ink` |
| focused | shadow #ffffff 0px 0px 0px 2px; outline 2px solid #000000, offset 2px |

![Select field default](components/crops/select-field-default.png) ![Select field focused](components/crops/select-field-focused.png)

#### Text area
The Message area: a taller #eeeef2 field. Focused only; nothing typed was sent. Read as `textarea-field` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 609 x 126; padding 10.5px 14px; background #eeeef2 `color.neutral.paper`; text Neue Haas Grotesk Text Pro 14/21 400, #151515 `color.neutral.ink`; placeholder #757575 `color.neutral.placeholder` |
| focused | shadow #ffffff 0px 0px 0px 2px; outline 2px solid #000000, offset 2px |

![Text area default](components/crops/textarea-field-default.png) ![Text area focused](components/crops/textarea-field-focused.png)

#### Submit button
The contact form SUBMIT: a 2px #eeeef2 outline block-button, digi one v2 14px caps, 46px tall. Measured, never pressed — the form was never sent. Read as `submit-button` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 104.77 x 46; padding 10.5px 17.5px; border 2px solid #eeeef2 `color.neutral.paper`; background transparent; image linear-gradient(to right, #333333 `color.neutral.sweep` 0%, #333333 `color.neutral.sweep` 100%); text digi one v2 14/21 400, #eeeef2 `color.neutral.paper`; transition background-size 0.4s ease |
| hover | background #eeeef2 `color.neutral.paper`; text digi one v2 14/21 400, #151515 `color.neutral.ink` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px; outline 2px solid #000000, offset 2px |
| pressed | background #eeeef2 `color.neutral.paper`; text digi one v2 14/21 400, #151515 `color.neutral.ink` |

![Submit button default](components/crops/submit-button-default.png) ![Submit button hover](components/crops/submit-button-hover.png) ![Submit button focus-visible](components/crops/submit-button-focus-visible.png) ![Submit button pressed](components/crops/submit-button-pressed.png)

### Account and cart

The empty /cart drawer (a right panel on the page scrim) and the signed-out /my-account magic-login card. Nothing was added, sent or created.

#### Mini-cart drawer
The cart side drawer (a 392px right drawer, dialog.tdc-cart): "Your cart is empty." with a CONTINUE SHOPPING action. Nothing was ever added. Read as `cart-drawer` on the cart page.

**Values (default).** size 1440 x 900; background transparent; text Neue Haas Grotesk Text Pro 14/normal 700, #21759b; icon 28 x 28, #eeeef2 `color.neutral.paper`; layers body.wp-singular.page-template-default 1440.0x4069.1 rgb(21, 21, 21); a.skip-link 156.9x34.4 rgb(241, 241, 241) rgba(0, 0, 0, 0.6) 0px 0px 2px 2px; div.element-background.has-center-center-position 1440.0x56.0 rgb(21, 21, 21); span 54.3x21.0; span 35.9x21.0; span 50.1x21.0.

Child layers that carry the look: body 1440x4069.1 background #151515 `color.neutral.ink`; a 156.9x34.4 background #f1f1f1 image linear-gradient(to right, #333333 `color.neutral.sweep` 0%, #333333 `color.neutral.sweep`  shadow rgba(0, 0, 0, 0.6) 0px 0px 2px 2px; div 1440x56 background #151515 `color.neutral.ink`.

![Mini-cart drawer default](components/crops/cart-drawer-default.png)

#### Continue shopping action
The empty-cart action row; measured, never followed. Read as `cart-continue` on the cart page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 350 x 46; padding 10.5px 17.5px; border 2px solid #eeeef2 `color.neutral.paper`; background transparent; image linear-gradient(to right, #333333 `color.neutral.sweep` 0%, #333333 `color.neutral.sweep` 100%); text digi one v2 14/21 400, #eeeef2 `color.neutral.paper`; transition background-size 0.4s ease |
| hover | background #eeeef2 `color.neutral.paper`; text digi one v2 14/21 400, #151515 `color.neutral.ink` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px; outline 2px solid #000000, offset 2px |
| pressed | background #eeeef2 `color.neutral.paper`; text digi one v2 14/21 400, #151515 `color.neutral.ink` |

![Continue shopping action default](components/crops/cart-continue-default.png) ![Continue shopping action hover](components/crops/cart-continue-hover.png) ![Continue shopping action focus-visible](components/crops/cart-continue-focus-visible.png) ![Continue shopping action pressed](components/crops/cart-continue-pressed.png)

#### Login panel
The /my-account magic-login surface (the same Send me a code form as the header drawer). Captured, never used. Read as `login-panel` on the my-account page.

**Values (default).** size 392 x 141.59; background transparent; text digi one v2 14/21 400, #151515 `color.neutral.ink`; icon 24 x 24, #ffffff `color.neutral.white`; layers input.block-input.button-full_form 392.0x42.0 rgb(238, 238, 242); input.block-input.button-full_form 0.0x0.0 rgb(238, 238, 242); input.block-input.has-undefined-background-color 0.0x0.0 T:2px solid rgb(255, 255, 255) / R:2px solid rgb(255, 255, 255) / B:2px solid rgb(255, 255, 255) / L:2px solid rgb(255, 255, 255); input 0.0x0.0 rgb(21, 21, 21) T:2px solid rgb(238, 238, 242) / R:2px solid rgb(238,.

Child layers that carry the look: input 392x42 background #eeeef2 `color.neutral.paper`; input 0x0 background #eeeef2 `color.neutral.paper`; input 0x0 border 2px solid #ffffff `color.neutral.white`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Login email field
The Email input of the magic-login form. Sample text was typed and deleted; no code was ever requested. Read as `login-email` on the my-account page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 392 x 42; padding 10.5px 44px 10.5px 17.5px; background #eeeef2 `color.neutral.paper`; text digi one v2 14/21 400, #151515 `color.neutral.ink`; placeholder #757575 `color.neutral.placeholder` |
| focused, filled | background #151515 `color.neutral.ink`; shadow #ffffff 0px 0px 0px 2px; outline 2px solid #000000, offset 2px; text digi one v2 14/21 400, #eeeef2 `color.neutral.paper` |

![Login email field default](components/crops/login-email-default.png) ![Login email field focused](components/crops/login-email-focused.png) ![Login email field filled](components/crops/login-email-filled.png)

#### Send me a code button
The full-width secondary-variant block-button (grey #cccccc fill, #151515 digi label). Measured, never pressed. Read as `login-send` on the my-account page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 392 x 42; padding 10.5px 17.5px; background #cccccc `color.neutral.grey`; image linear-gradient(to right, #333333 `color.neutral.sweep` 0%, #333333 `color.neutral.sweep` 100%); text digi one v2 14/21 400, #151515 `color.neutral.ink`; transition background-size 0.4s ease |
| hover | background #151515 `color.neutral.ink`; text digi one v2 14/21 400, #cccccc `color.neutral.grey` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px; outline 2px solid #000000, offset 2px |
| pressed | background #151515 `color.neutral.ink`; text digi one v2 14/21 400, #cccccc `color.neutral.grey` |

![Send me a code button default](components/crops/login-send-default.png) ![Send me a code button hover](components/crops/login-send-hover.png) ![Send me a code button focus-visible](components/crops/login-send-focus-visible.png) ![Send me a code button pressed](components/crops/login-send-pressed.png)

#### Create account button
The secondary account action; measured, never pressed. Read as `login-create` on the my-account page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 392 x 42; padding 10.5px 17.5px; background #cccccc `color.neutral.grey`; image linear-gradient(to right, #333333 `color.neutral.sweep` 0%, #333333 `color.neutral.sweep` 100%); text digi one v2 14/21 400, #151515 `color.neutral.ink`; transition background-size 0.4s ease |
| hover | background #151515 `color.neutral.ink`; text digi one v2 14/21 400, #cccccc `color.neutral.grey` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px; outline 2px solid #000000, offset 2px |
| pressed | background #151515 `color.neutral.ink`; text digi one v2 14/21 400, #cccccc `color.neutral.grey` |

![Create account button default](components/crops/login-create-default.png) ![Create account button hover](components/crops/login-create-hover.png) ![Create account button focus-visible](components/crops/login-create-focus-visible.png) ![Create account button pressed](components/crops/login-create-pressed.png)

### Footer

The footer over the page ground: the Elektron wordmark, Navigation / Shop / Support / Resources columns of 24px display links, the legal row and the social glyphs.

#### Footer
The footer: the Elektron wordmark, the Navigation / Shop / Support / Resources columns of 24px Neue Haas Display links, legal row and the cookie-settings reopen link. Read as `footer` on the home page.

**Values (default).** size 1440 x 656.42; background transparent; text Neue Haas Grotesk Text Pro 14/21 400, #eeeef2 `color.neutral.paper`; layers div.element-background.has-center-center-position 1440.0x656.4 rgba(21, 21, 21, 0.1); a.block-button.button-medium_text 58.0x36.0; a.block-button.button-medium_text 89.6x36.0; a.block-button.button-medium_light_text 63.3x36.0; a.block-button.button-medium_light_text 153.0x36.0; a.block-button.button-medium_light_text 140.8x36.0.

Child layers that carry the look: div 1440x656.4 background rgba(21, 21, 21, 0.1); a 58x36 image linear-gradient(to right, #333333 `color.neutral.sweep` 0%, #333333 `color.neutral.sweep` ; a 89.6x36 image linear-gradient(to right, #333333 `color.neutral.sweep` 0%, #333333 `color.neutral.sweep` .

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer column link: 24px Neue Haas Grotesk Display 450, measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 58.05 x 36.02; background transparent; image linear-gradient(to right, #333333 `color.neutral.sweep` 0%, #333333 `color.neutral.sweep` 100%); text Neue Haas Grotesk Display Pro 24.01/36.01 450, #eeeef2 `color.neutral.paper`; transition background-size 0.4s ease |
| focus-visible | shadow #ffffff 0px 0px 0px 2px; outline 2px solid #000000, offset 2px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Footer wordmark
The Elektron logo link at the foot of the page. Read as `footer-wordmark` on the home page.

**Values (default).** size 213 x 25.55; background transparent; text Neue Haas Grotesk Text Pro 14/21 400, #eeeef2 `color.neutral.paper`.

![Footer wordmark default](components/crops/footer-wordmark-default.png)

#### Social link
A social link in the footer. Read as `social-icon` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 17.97 x 18.38; background transparent; text Neue Haas Grotesk Text Pro 14/21 400, #eeeef2 `color.neutral.paper` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px; outline 2px solid #000000, offset 2px; layers a.block-icon.is-brand 18.0x18.4 rgb(255, 255, 255) 0px 0px 0px 2px 2px solid rgb(0, 0, 0) offset 2px |

![Social link default](components/crops/social-icon-default.png) ![Social link hover](components/crops/social-icon-hover.png) ![Social link focus-visible](components/crops/social-icon-focus-visible.png) ![Social link pressed](components/crops/social-icon-pressed.png)

### Mobile (390 wide)

The same surface at phone width: the 63px header with a burger that expands to a fullscreen menu — a search row and 24px display links.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 63; background transparent; text Neue Haas Grotesk Text Pro 14/21 400, #eeeef2 `color.neutral.paper`; transition box-shadow 0.8s cubic-bezier(0.365, 0.305, 0, 1), height 0.4s cubic-bezier(0, 1.05, 0.65, 1.01), color 0.4s cubic-bezier(0.365, 0.305, 0, 1), background-color 0.4s cubic-bezier(0.365, 0.305, 0, 1), -webkit-box-shadow 0.8s cubic-bezier(0.365, 0.305, 0, 1); icon 35 x 24.86, #eeeef2 `color.neutral.paper`; layers div.element-background.has-center-center-position 390.0x63.0 rgb(21, 21, 21).

Child layers that carry the look: div 390x63 background #151515 `color.neutral.ink`.

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
The burger anchor that toggles the mobile menu panel. Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 35 x 35; background transparent; text Neue Haas Grotesk Text Pro 14/21 400, #eeeef2 `color.neutral.paper`; icon 35 x 35, #eeeef2 `color.neutral.paper`.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The opened mobile navigation panel: the header expands to a fullscreen menu with a search row and Catalog / Shop / Kulture / Support / Account links. Read as `m-menu-open` on the home page at 390 wide.

**Values (opened).** size 390 x 844; background transparent; text Neue Haas Grotesk Display Pro 24.01/36.01 450, #eeeef2 `color.neutral.paper`; icon 35 x 24.86, #eeeef2 `color.neutral.paper`; layers div.element-background.has-center-center-position 390.0x63.0 rgb(21, 21, 21); div.element-background.has-center-center-position 390.0x781.0 rgb(21, 21, 21); input.search-field.has-normal-border 362.0x48.6 rgb(21, 21, 21) T:2px solid rgb(238, 238, 242) / R:2px solid rgb(238, 238, 242) / B:2px solid rgb(238, 238, 242) / L:2px solid rgb(238, 238, 242); span 86.6x36.0; span 58.0x36.0; span 80.3x36.0.

Child layers that carry the look: div 390x63 background #151515 `color.neutral.ink`; div 390x781 background #151515 `color.neutral.ink`; input 362x48.6 background #151515 `color.neutral.ink` border 2px solid #eeeef2 `color.neutral.paper`.

![Mobile menu, open opened](components/crops/m-menu-open-opened.png)

#### Mobile nav item
A row inside the opened mobile menu. Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 138.41 x 36.02; background transparent; text Neue Haas Grotesk Display Pro 24.01/36.01 450, #eeeef2 `color.neutral.paper`; transition border 0.3s ease, background-color 0.3s ease, background-position 0.3s ease, background-size 0.3s ease, background-image 0.5s ease, opacity 0.3s ease; icon 35 x 35, #eeeef2 `color.neutral.paper`; layers span 86.6x36.0 |
| focus-visible, pressed | shadow #ffffff 0px 0px 0px 2px; outline 2px solid #000000, offset 2px; layers a.block-button.button-medium_text 138.4x36.0 rgb(255, 255, 255) 0px 0px 0px 2px 2px solid rgb(0, 0, 0) offset 2px; span 86.6x36.0 |

Child layers that carry the look: span 86.6x36 image linear-gradient(to right, #333333 `color.neutral.sweep` 0%, #333333 `color.neutral.sweep` .

![Mobile nav item default](components/crops/m-nav-item-default.png) ![Mobile nav item hover](components/crops/m-nav-item-hover.png) ![Mobile nav item focus-visible](components/crops/m-nav-item-focus-visible.png) ![Mobile nav item pressed](components/crops/m-nav-item-pressed.png)

#### Mobile heading
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 219.94 x 31.64; background transparent; text Neue Haas Grotesk Display Pro 23.8/31.65 400, #eeeef2 `color.neutral.paper`.

![Mobile heading default](components/crops/m-hero-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Elektron wordmark, the 28px header glyphs, the 35px menu/drawer icons, the social glyphs and the product artwork) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Everything behind the magic-login card — the account dashboard, order history, registered machines, downloads tied to a serial, and checkout — was never reached. /my-account and the header Account drawer show only the passwordless card: an Email field and Send me a code. The field was measured and given sample text that was deleted again; no code was ever requested and Create New Account was never pressed. What the account surfaces look like is not documented here.

### Pages

- **ADD TO CART, EXPLORE and checkout.** The product actions were measured across their states, never pressed; nothing was added to the cart (the drawer read "Your cart is empty.") and no checkout surface was reached.
- **Contact and newsletter forms.** The /contact-us form and footer signup were measured and given sample text that was deleted, never submitted.
- **Kulture articles, product configurators and downloads** are linked from the captured pages but were never opened or started.
- **External surfaces** (elektron.se's other country stores, social profiles, the sister brands) are linked from the site but were never opened.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.
- **product-card's and accordion's focus-visible** could not hold a real keyboard focus (`via: focus failed`) — their focus look is uncaptured, not absent.

### Themes

The public surface paints one dark theme — a #151515 ground with #eeeef2 paper text — on every captured route, with no user-facing switch and no light variant declared. The export emits it as the single `dark` set.

### Fonts

- **Neue Haas Grotesk Text/Display Pro**, **digi one v2** and **Analog One V2.** are licensed faces served from the site's own uploads; the @font-face blocks live in the same-origin theme sheets (src list in raw/css-vars.json). The style guide falls back to system sans — the webfonts are licensed, not shipped.

### Screenshots

- The product photography, Kulture covers and the Elektron wordmark in the screenshots are the product's published content.
- The mobile-home and mobile-shop full-page captures hit the GPU texture cap and were stitched from chunks (the `.partN` PNGs and their sidecars are kept with the unquantized captures, outside the repository).
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Product descriptions, prices beyond the two captured pages, Kulture article text and marketing copy are the product's content; only frames and components were measured.
