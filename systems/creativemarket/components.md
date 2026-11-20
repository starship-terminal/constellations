# Creative Market components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from creativemarket.com on 2026-11-12, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought, submitted or added to the cart; the sign-in username field was filled with a placeholder and cleared but Log In was never pressed, and Add to cart, Buy now, FOLLOW and every SSO button were never followed. The CookieYes consent banner and the chat launcher were hidden, never answered. Cloudflare Turnstile greets some routes headless — a still-blocked route is a documented boundary.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (49 components, 119 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (119 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every captured surface paints `light`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Fonts category | `/fonts` | [default](screenshots/category-light-default.png), [full](screenshots/category-light-full.png) |
| Product page | `/SilverStag/7290900-Silver-Garden-Nostalgic-Font-Duo` | [default](screenshots/product-light-default.png), [full](screenshots/product-light-full.png) |
| Search | `/search?query=font` | [default](screenshots/search-light-default.png), [full](screenshots/search-light-full.png) |
| Membership | `/membership` | [default](screenshots/membership-light-default.png), [full](screenshots/membership-light-full.png) |
| Sign in | `/sign-in` | [default](screenshots/signin-light-default.png), [filled](screenshots/signin-light-filled.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Fonts category, phone | `/fonts` | [default](screenshots/mobile-category-light-default.png), [full](screenshots/mobile-category-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu overlay | home, phone width | the 45px hamburger button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open), [m-nav-item](#mobile-menu-row) |
| Sign-in form, filled | /sign-in | the username field filled with a placeholder and cleared — Log In never pressed | [signin-light-filled](screenshots/signin-light-filled.png), [username-field](#username-field) |
| CookieYes consent | every page | hidden via the overlay hider, never answered | not captured |
| Chat launcher | every page | the "Licensing Questions? Let's Chat!" launcher — hidden, never opened | not captured |
| The signed-in account | dashboard, purchases, downloads | Log In leads to the account; purchases and downloads were never used | boundary; see Gaps |
| Cloudflare Turnstile | some routes, headless | fresh contexts and patient waits cleared it most times | intermittent boundary |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 21 components were given a real keyboard focus. 12 draw an outline ring: `join-link` (2px solid #e06868, offset 1px), `save25-button` (2px solid #4e42a1 `color.brand.accent`, offset 2px), `nav-link` (2px solid #e06868, offset 1px), `product-card` (on a child: 2px solid rgb(224, 104, 104) offset 1px), `filter-btn` (2px solid #e06868, offset 0px), `category-card` (on a child: 2px solid rgb(224, 104, 104) offset 1px), `enterprise-cta` (2px solid #088178 `color.brand.teal`, offset 0px), `follow-btn` (2px solid #e06868, offset 0px), `footer-link` (2px solid #e06868, offset 1px), `social-icon` (2px solid #e06868, offset 1px), `m-menu-button` (2px solid #088178 `color.brand.teal`, offset 2px), `m-nav-item` (2px solid #e06868, offset 1px). 3 draw a focus ring as a shadow instead: `login-btn`, `sso-btn`, `search-chip`. 2 change only their border: `add-cart`, `buy-now`. The other 4 show no measured change: `newsletter-field`, `username-field`, `password-field`, `m-search`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `ease` | background-color | enterprise-cta |
| 0.2s | `cubic-bezier(0.32, 0, 0.59, 0.03)` | background-color, border-color, color | add-cart, buy-now, m-menu-button, save25-button |
| 0.2s | `ease` | background, border-color, color, text-shadow | follow-btn, nav-link |
| 0.2s | `ease-in-out` | all | social-icon |
| 0.25s | `ease` | all, color | add-to-cart-btn, footer-link, join-link, login-btn, logo, m-nav-item, search-chip, sso-btn |
| 0.4s | `cubic-bezier(0.25, 1, 0.5, 1)` | all | m-menu-open |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card](#plan-card) | 274 x 323 | - | 16px | #ffffff | none | 30px |

## Components

### Shell and navigation

The 73px site header: the 585x44 search field with its All Categories dropdown, the Creative Market wordmark, Join | Log in, the 92x32 purple Save 25% button and the cart icon; a lower nav row carries FONTS / TEMPLATES / GRAPHICS & ILLUSTRATIONS / BRUSHES & EFFECTS / MORE / SALE / INSPIRATION / ENTERPRISE.

#### Site header
The top bar: All Categories dropdown, the 585px search field, Join | Log in, the amber Save 25% button and the cart icon. Read as `site-header` on the home page.

**Values (default).** size 1440 x 73; background #ffffff; text Averta 14/20 600, #303538.

![Site header default](components/crops/site-header-default.png)

#### Logo
The Creative Market logo anchor. Read as `logo` on the home page.

**Values (default).** size 88 x 36; background transparent; text Averta 16/24 400, #303538; transition color 0.25s ease; icon 87.98 x 34.73, #303538.

![Logo default](components/crops/logo-default.png)

#### Nav search field
The 585x44 header search (All Categories dropdown + field); never submitted. Read as `nav-search` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 585 x 44; background transparent; text Averta 14/20 600, #303538; icon 16 x 16, #899298; layers input.search-field__input 585.0x44.0 rgb(250, 253, 255) T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 100px; div::before.search-field__category 1pxx24px rgb(137, 146, 152); div.multiselect__tags 120.0x32.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, |
| hover | layers input.search-field__input 585.0x44.0 rgb(250, 253, 255) T:1px solid rgb(204, 212, 218) / R:1px solid rgb(204, 212, 218) / B:1px solid rgb(204, 212, 218) / L:1px solid rgb(204, 212, 218) 100px; div::before.search-field__category 1pxx24px rgb(137, 146, 152); div.multiselect__tags 120.0x32.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba( |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: input 585x44 background #fafdff border 1px solid transparent radius 100px; div::before 1pxx24px background #899298; div 120x32 border 1px solid transparent radius 8px shadow transparent 0px 0px 0px 3px.

![Nav search field default](components/crops/nav-search-default.png) ![Nav search field hover](components/crops/nav-search-hover.png) ![Nav search field pressed](components/crops/nav-search-pressed.png)

#### Join link
The "Join" user link; measured, never followed. Read as `join-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 31.34 x 18; background transparent; text Averta 14/14 600, #303538; transition color 0.25s ease |
| hover | size 31.34 x 20; border B: 2px solid #303538; text Averta 14/14 600, #003a37 `color.brand.teal-hover`; layers a.user-link__link 31.3x20.0 B:2px solid rgb(48, 53, 56) |
| focus-visible | outline 2px solid #e06868, offset 1px; layers a.user-link__link 31.3x18.0 2px solid rgb(224, 104, 104) offset 1px |
| pressed | size 31.34 x 20; border B: 2px solid #303538; text Averta 14/14 600, #003a37 `color.brand.teal-hover`; layers a.user-link__link 31.3x20.0 B:2px solid rgb(48, 53, 56) |

![Join link default](components/crops/join-link-default.png) ![Join link hover](components/crops/join-link-hover.png) ![Join link focus-visible](components/crops/join-link-focus-visible.png) ![Join link pressed](components/crops/join-link-pressed.png)

#### Save 25% button
The amber "Save 25%" ui-button--accent (92x32); measured, never followed. Read as `save25-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 92.95 x 32; padding 0px 12px; border 2px solid #4e42a1 `color.brand.accent`; radius 8px; background #4e42a1 `color.brand.accent`; text Averta 14/14 600, #ffffff; transition color 0.2s cubic-bezier(0.32, 0, 0.59, 0.03), background-color 0.2s cubic-bezier(0.32, 0, 0.59, 0.03), border-color 0.2s cubic-bezier(0.32, 0, 0.59, 0.03) |
| hover | border 2px solid #281f6b `color.brand.accent-hover`; background #281f6b `color.brand.accent-hover` |
| focus-visible | outline 2px solid #4e42a1 `color.brand.accent`, offset 2px |
| pressed | border 2px solid #281f6b `color.brand.accent-hover`; background #281f6b `color.brand.accent-hover` |

![Save 25% button default](components/crops/save25-button-default.png) ![Save 25% button hover](components/crops/save25-button-hover.png) ![Save 25% button focus-visible](components/crops/save25-button-focus-visible.png) ![Save 25% button pressed](components/crops/save25-button-pressed.png)

#### Cart icon
The header cart icon with its count badge. Read as `cart-icon` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 20 x 23; background transparent; text Averta 14/14 600, #088178 `color.brand.teal`; icon 20 x 21, #000000 |
| hover | text Averta 14/14 600, #003a37 `color.brand.teal-hover` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Cart icon default](components/crops/cart-icon-default.png) ![Cart icon hover](components/crops/cart-icon-hover.png) ![Cart icon pressed](components/crops/cart-icon-pressed.png)

#### Category nav link
A lower-nav category item (FONTS/TEMPLATES/...); measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 47.94 x 14; background transparent; text Averta 13/14 400, #303538; transition color 0.2s ease, text-shadow 0.2s ease |
| hover | text Averta 13/14 400, #088178 `color.brand.teal` |
| focus-visible | outline 2px solid #e06868, offset 1px; layers a.lower-nav__item-link 47.9x14.0 2px solid rgb(224, 104, 104) offset 1px |
| pressed | text Averta 13/14 400, #003a37 `color.brand.teal-hover` |

![Category nav link default](components/crops/nav-link-default.png) ![Category nav link hover](components/crops/nav-link-hover.png) ![Category nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Category nav link pressed](components/crops/nav-link-pressed.png)

### Home

The illustrated hero ("Bring your creative ideas to life."), the product-card rail of 337px cards with teal price pills and a 44px Add To Cart on hover, the section rows ("Handpicked designs", "Suggested searches") and the 31px footer newsletter field.

#### Accessibility h1
"Bring your creative ideas to life." — a visually-hidden h1; recorded for the type style, not painted. Read as `a11y-h1` on the home page.

Not on the page when it was captured.

#### Hero heading
"Try a new way to search fonts" — the painted headline under the hidden h1. Read as `search-strip-heading` on the home page.

**Values (default).** size 625 x 32; background transparent; text Averta 24/32 600, #303538.

![Hero heading default](components/crops/search-strip-heading-default.png)

#### Section heading
A homepage row heading ("Popular Fonts"). Read as `row-title` on the home page.

**Values (default).** size 1260 x 32; background transparent; text Averta 24/32 600, #303538; icon 7 x 14, #303538.

![Section heading default](components/crops/row-title-default.png)

#### Product card
A product card in a home row (artwork, name, shop, teal price pill); measured, never followed. Read as `product-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 337 x 275.52; padding 4px; background transparent; text Averta 14/14 400, #303538; icon 16 x 16, #303538; layers a 329.0x219.3 rgb(237, 242, 245); div.product-thumbnail-badge 143.4x28.0 rgb(255, 255, 255) T:1px solid rgb(237, 242, 245) / R:1px solid rgb(237, 242, 245) / B:1px solid rgb(237, 242, 245) / L:1px solid rgb(237, 242, 245) 0px 18px 0px 0px; button.like-button.product-thumbnail__like-button 30.0x30.0 rgba(255, 255, 255, 0.9) rgba(0, 0, 0, 0.1) 0px 1px 8px 0px, rgba(0, 0, 0, 0.05) 0px 0px 1px 1px, rg |
| hover | text Averta 14/14 400, #003a37 `color.brand.teal-hover` |
| focus-visible | layers a 329.0x219.3 rgb(237, 242, 245) 2px solid rgb(224, 104, 104) offset 1px; div.product-thumbnail-badge 143.4x28.0 rgb(255, 255, 255) T:1px solid rgb(237, 242, 245) / R:1px solid rgb(237, 242, 245) / B:1px solid rgb(237, 242, 245) / L:1px solid rgb(237, 242, 245) 0px 18px 0px 0px; button.like-button.product-thumbnail__like-button 30.0x30.0 rgba(255, 255, 255, 0.9) rgba(0, 0, 0, 0.1) 0px 1px 8px 0px, |

Child layers that carry the look: a 329x219.3 background #edf2f5; div 143.4x28 background #ffffff border 1px solid #edf2f5 radius 0px 18px 0px 0px; button 30x30 background rgba(255, 255, 255, 0.9) radius 3.35544e+07px shadow rgba(0, 0, 0, 0.1) 0px 1px 8px 0px, rgba(0, 0, 0, 0.05) 0px 0px 1px 1px, #ffffff 0px 1px 1px 0px inset, rgba(255, 255, 255, 0.25) 0px -1px 0px 0px inset.

![Product card default](components/crops/product-card-default.png) ![Product card hover](components/crops/product-card-hover.png) ![Product card focus-visible](components/crops/product-card-focus-visible.png) ![Product card pressed](components/crops/product-card-pressed.png)

#### Card add-to-cart
A product card's sp-button add-to-cart (paints on card hover); measured only — pressing it would change the cart. Read as `add-to-cart-btn` on the home page.

**Values (default).** size 329 x 44; padding 10px 22px; border 2px solid #003a37 `color.brand.teal-hover`; background #003a37 `color.brand.teal-hover`; text Averta 16/normal 600, #ffffff; transition all 0.25s ease.

![Card add-to-cart default](components/crops/add-to-cart-btn-default.png)

#### Newsletter field
The email banner input (368x31); filled with a placeholder, never submitted. Read as `newsletter-field` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, filled) | size 368 x 31; padding 1px 2px; background #ffffff; text Averta 16/normal 400, #303538; placeholder #757575 |

![Newsletter field default](components/crops/newsletter-field-default.png) ![Newsletter field focus-visible](components/crops/newsletter-field-focus-visible.png) ![Newsletter field filled](components/crops/newsletter-field-filled.png)

### Category

The /fonts category surface: the 48px heading, the 44px filter pills, the 480x202 filter groups and the 320px result cards.

#### Category headline
"Fonts" — the category page title. Read as `category-h1` on the category page.

**Values (default).** size 1376 x 70.38; padding 7.2px 0px; background transparent; text Averta 48/56 600, #303538.

![Category headline default](components/crops/category-h1-default.png)

#### Filter button
The "Browse by Category" filter disclosure; toggled locally. Read as `filter-btn` on the category page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 218.95 x 44; padding 0px 24px; border 1px solid #000000; radius 32px; background transparent; text Averta 16/normal 600, #000000; icon 14 x 7, #000000 |
| focus-visible | outline 2px solid #e06868, offset 0px |

![Filter button default](components/crops/filter-btn-default.png) ![Filter button hover](components/crops/filter-btn-hover.png) ![Filter button focus-visible](components/crops/filter-btn-focus-visible.png) ![Filter button pressed](components/crops/filter-btn-pressed.png)

#### Filter groups
The Classification/Style/Aesthetic filter column. Read as `filter-group` on the category page.

**Values (default).** size 480 x 202; padding 12px; background transparent; text Averta 16/24 400, #000000; icon 4 x 4, #303538; layers a.selection-pill 149.5x54.0 T:1px solid rgb(204, 212, 218) / R:1px solid rgb(204, 212, 218) / B:1px solid rgb(204, 212, 218) / L:1px solid rgb(204, 212, 218) 32px; a.selection-pill 86.4x54.0 T:1px solid rgb(204, 212, 218) / R:1px solid rgb(204, 212, 218) / B:1px solid rgb(204, 212, 218) / L:1px solid rgb(204, 212, 218) 32px; a.selection-pill 118.7x54.0 T:1px solid rgb(204, 212, 218) / R:1px solid .

Child layers that carry the look: a 149.5x54 border 1px solid #ccd4da radius 32px; a 86.4x54 border 1px solid #ccd4da radius 32px; a 118.7x54 border 1px solid #ccd4da radius 32px.

![Filter groups default](components/crops/filter-group-default.png)

#### Category product card
A product thumbnail card in the category grid (image, name, shop); measured, never followed. Read as `category-card` on the category page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 320 x 213.33; background transparent; text Averta 14/14 400, #303538; icon 16 x 16, #303538; layers a 320.0x213.3 rgb(237, 242, 245); div.product-thumbnail-badge 143.4x28.0 rgb(255, 255, 255) T:1px solid rgb(237, 242, 245) / R:1px solid rgb(237, 242, 245) / B:1px solid rgb(237, 242, 245) / L:1px solid rgb(237, 242, 245) 0px 18px 0px 0px; button.like-button.product-thumbnail__like-button 30.0x30.0 rgba(255, 255, 255, 0.9) rgba(0, 0, 0, 0.1) 0px 1px 8px 0px, rgba(0, 0, 0, 0.05) 0px 0px 1px 1px, rg |
| hover | text Averta 14/14 400, #003a37 `color.brand.teal-hover`; layers a 320.0x213.3 rgb(237, 242, 245); div.product-thumbnail__font-preview 320.0x213.3 rgb(255, 255, 255); div.product-thumbnail-badge 143.4x28.0 rgb(255, 255, 255) T:1px solid rgb(237, 242, 245) / R:1px solid rgb(237, 242, 245) / B:1px solid rgb(237, 242, 245) / L:1px solid rgb(237, 242, 245) 0px 18px 0px 0px; button.like-button.product-thumbnail__like-button 30.0x30.0 rgba(255, 255, 255, 0.9) rgba(0, |
| focus-visible | layers a 320.0x213.3 rgb(237, 242, 245) 2px solid rgb(224, 104, 104) offset 1px; div.product-thumbnail__font-preview 320.0x213.3 rgb(255, 255, 255); div.product-thumbnail-badge 143.4x28.0 rgb(255, 255, 255) T:1px solid rgb(237, 242, 245) / R:1px solid rgb(237, 242, 245) / B:1px solid rgb(237, 242, 245) / L:1px solid rgb(237, 242, 245) 0px 18px 0px 0px; button.like-button.product-thumbnail__like-button 30 |
| pressed | layers a 320.0x213.3 rgb(237, 242, 245); div.product-thumbnail__font-preview 320.0x213.3 rgb(255, 255, 255); div.product-thumbnail-badge 143.4x28.0 rgb(255, 255, 255) T:1px solid rgb(237, 242, 245) / R:1px solid rgb(237, 242, 245) / B:1px solid rgb(237, 242, 245) / L:1px solid rgb(237, 242, 245) 0px 18px 0px 0px; button.like-button.product-thumbnail__like-button 30.0x30.0 rgba(255, 255, 255, 0.9) rgba(0, |

Child layers that carry the look: a 320x213.3 background #edf2f5; div 143.4x28 background #ffffff border 1px solid #edf2f5 radius 0px 18px 0px 0px; button 30x30 background rgba(255, 255, 255, 0.9) radius 3.35544e+07px shadow rgba(0, 0, 0, 0.1) 0px 1px 8px 0px, rgba(0, 0, 0, 0.05) 0px 0px 1px 1px, #ffffff 0px 1px 1px 0px inset, rgba(255, 255, 255, 0.25) 0px -1px 0px 0px inset.

![Category product card default](components/crops/category-card-default.png) ![Category product card hover](components/crops/category-card-hover.png) ![Category product card focus-visible](components/crops/category-card-focus-visible.png) ![Category product card pressed](components/crops/category-card-pressed.png)

### Product

A product page (/SilverStag/7290900-...): the 24px title and shop byline, the 450px buy box with 24px license radio rows, the 45px teal Add to cart, the 40px outlined Buy now, the 52px enterprise CTA, Product Specs, the Reviews/Comments/FAQs accordions, Suggested-search chips and the Meet-the-shop card.

#### Product title
"Silver Garden - Nostalgic Font Duo" (h1.sp-h4). Read as `product-h1` on the product page.

**Values (default).** size 391.14 x 32; background transparent; text Averta 24/32 600, #303538.

![Product title default](components/crops/product-h1-default.png)

#### Shop byline
"SilverStag Type Foundry | Featured" — the author row. Read as `shop-byline` on the product page.

**Values (default).** size 391.14 x 25.22; background transparent; text Averta 14/14 400, #303538; layers a.header-badge.header-badge--shop 197.3x25.2 rgb(244, 248, 251) 14400px; div::after.header-badge__icon 17.2188pxx17.2188px rgba(0, 0, 0, 0.07) 0px 0px 0px 1px inset 50%; span.header-badge.header-badge--featured-shop 99.1x25.2 rgb(244, 248, 251) 14400px.

Child layers that carry the look: a 197.3x25.2 background #f4f8fb radius 14400px; div::after 17.2188pxx17.2188px radius 50% shadow rgba(0, 0, 0, 0.07) 0px 0px 0px 1px inset; span 99.1x25.2 background #f4f8fb radius 14400px.

![Shop byline default](components/crops/shop-byline-default.png)

#### Price
The buy-box price ($79). Read as `buy-box-price` on the product page.

**Values (default).** size 50.08 x 35; background transparent; text Averta 28/35 600, #303538; layers span.tooltip-text 0.0x0.0 rgb(48, 53, 56) rgba(0, 0, 0, 0.2) 0px 2px 4px 0px 6px.

Child layers that carry the look: span 0x0 background #303538 radius 6px shadow rgba(0, 0, 0, 0.2) 0px 2px 4px 0px.

![Price default](components/crops/buy-box-price-default.png)

#### License row
A license option row in the buy box (label + $79.00 price). Read as `license-row` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 450 x 24; background transparent; text Averta 16/24 600, #303538; icon 16 x 14, #899298; layers input 18.0x18.0 rgb(8, 129, 120) T:2px solid rgb(8, 129, 120) / R:2px solid rgb(8, 129, 120) / B:2px solid rgb(8, 129, 120) / L:2px solid rgb(8, 129, 120) 4px; input::after 12pxx12px; span.tooltip-text 0.0x0.0 rgb(48, 53, 56) rgba(0, 0, 0, 0.2) 0px 2px 4px 0px 6px |

Child layers that carry the look: input 18x18 background #088178 `color.brand.teal` border 2px solid #088178 `color.brand.teal` radius 4px; input::after 12pxx12px image url(data:…); span 0x0 background #303538 radius 6px shadow rgba(0, 0, 0, 0.2) 0px 2px 4px 0px.

![License row default](components/crops/license-row-default.png) ![License row hover](components/crops/license-row-hover.png)

#### Add to cart
The primary buy-box button (450x45); measured only — never pressed. Read as `add-cart` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 450 x 45; padding 0px 12px; border 2px solid #088178 `color.brand.teal`; radius 8px; background #088178 `color.brand.teal`; text Averta 14/32 600, #ffffff; transition color 0.2s cubic-bezier(0.32, 0, 0.59, 0.03), background-color 0.2s cubic-bezier(0.32, 0, 0.59, 0.03), border-color 0.2s cubic-bezier(0.32, 0, 0.59, 0.03); layers ::before rgb(0, 58, 55) 0px none 1 |
| hover, focus-visible, pressed | border 2px solid #003a37 `color.brand.teal-hover`; background #003a37 `color.brand.teal-hover` |

![Add to cart default](components/crops/add-cart-default.png) ![Add to cart hover](components/crops/add-cart-hover.png) ![Add to cart focus-visible](components/crops/add-cart-focus-visible.png) ![Add to cart pressed](components/crops/add-cart-pressed.png)

#### Buy now
The secondary buy-box button (450x40); measured only — never pressed. Read as `buy-now` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 450 x 40; padding 0px 10px; border 1px solid #899298; radius 8px; background #ffffff; text Averta 14/32 600, #088178 `color.brand.teal`; transition color 0.2s cubic-bezier(0.32, 0, 0.59, 0.03), background-color 0.2s cubic-bezier(0.32, 0, 0.59, 0.03), border-color 0.2s cubic-bezier(0.32, 0, 0.59, 0.03); layers ::before rgb(223, 248, 246) 0px none 1 |
| hover, focus-visible, pressed | border 1px solid #088178 `color.brand.teal`; background #dff8f6 `color.brand.teal-soft`; text Averta 14/32 600, #003a37 `color.brand.teal-hover` |

![Buy now default](components/crops/buy-now-default.png) ![Buy now hover](components/crops/buy-now-hover.png) ![Buy now focus-visible](components/crops/buy-now-focus-visible.png) ![Buy now pressed](components/crops/buy-now-pressed.png)

#### Enterprise CTA
"Enterprise or Custom License / Contact sales" row (450x52). Read as `enterprise-cta` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 450 x 52; padding 16px; radius 8px; background #dff8f6 `color.brand.teal-soft`; text Averta 16/normal 600, #303538; transition background-color 0.15s ease; icon 16 x 14, #088178 `color.brand.teal` |
| hover | background #b6e7e4 |
| focus-visible | outline 2px solid #088178 `color.brand.teal`, offset 0px |
| pressed | background #b6e7e4 |

![Enterprise CTA default](components/crops/enterprise-cta-default.png) ![Enterprise CTA hover](components/crops/enterprise-cta-hover.png) ![Enterprise CTA focus-visible](components/crops/enterprise-cta-focus-visible.png) ![Enterprise CTA pressed](components/crops/enterprise-cta-pressed.png)

#### Follow button
The shop FOLLOW button; measured, never pressed. Read as `follow-btn` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 232 x 35; padding 6px 28px; border 1px solid #e2e9ee; radius 24px; background #ffffff; text Averta 14/normal 400, #303538; transition text-shadow 0.2s ease, background 0.2s ease, border-color 0.2s ease; icon 18 x 14, #303538 |
| hover | background #fafdff |
| focus-visible | outline 2px solid #e06868, offset 0px |
| pressed | background #fafdff |

![Follow button default](components/crops/follow-btn-default.png) ![Follow button hover](components/crops/follow-btn-hover.png) ![Follow button focus-visible](components/crops/follow-btn-focus-visible.png) ![Follow button pressed](components/crops/follow-btn-pressed.png)

#### Product Specs
The Product Specs block: File Size, Vector, Web Font, creation date. Read as `specs` on the product page.

**Values (default).** size 450 x 259; background transparent; text Averta 24/24 600, #303538; icon 16 x 16, #4b5258; layers span::before.icon 100%xauto rgb(48, 53, 56); i::before.property-icon.svg-icon-file-size 24pxx24px rgb(75, 82, 88); i::before.property-icon.svg-icon-vector 24pxx24px rgb(75, 82, 88); i::before.property-icon.svg-icon-web-font 24pxx24px rgb(75, 82, 88); i::before.property-icon.svg-icon-calendar 22pxx23px rgb(75, 82, 88); div.report-product 450.0x39.0 T:1px solid rgb(226, 233, 238).

Child layers that carry the look: span::before 100%xauto background #303538; i::before 24pxx24px background #4b5258; i::before 24pxx24px background #4b5258.

![Product Specs default](components/crops/specs-default.png)

#### Accordion row
A details/summary accordion row (Reviews/Comments/FAQs); opened state toggled locally, closed again. Read as `accordion-row` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: opened) | size 878 x 88; padding 32px 0px; background transparent; text Averta 24/24 600, #303538; layers span::before.icon 24pxx24px rgb(48, 53, 56) |

Child layers that carry the look: span::before 24pxx24px background #303538.

![Accordion row default](components/crops/accordion-row-default.png) ![Accordion row opened](components/crops/accordion-row-opened.png)

#### Suggested-search chip
A Suggested Searches pill (Serif, Script, Nostalgic...); measured, never followed. Read as `search-chip` on the product page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 69.95 x 44; padding 10px 20px; radius 20px; background #fee4c3; text Averta 14/14 600, #303538; transition color 0.25s ease |
| hover | background #fcc875 `color.brand.gold` |
| focus-visible | shadow rgba(185, 221, 255, 0.45) 0px 0px 0px 5px |
| pressed | background #fcc875 `color.brand.gold` |

![Suggested-search chip default](components/crops/search-chip-default.png) ![Suggested-search chip hover](components/crops/search-chip-hover.png) ![Suggested-search chip focus-visible](components/crops/search-chip-focus-visible.png) ![Suggested-search chip pressed](components/crops/search-chip-pressed.png)

#### Meet the shop
The shop profile card: avatar, name, bio, FOLLOW/MESSAGE, stats (joined, sales, rating). Read as `shop-card` on the product page.

**Values (default).** size 1376 x 797.33; padding 40px; radius 16px; background #ffffff; text Averta 32/40 600, #303538; icon 16 x 16, #303538.

![Meet the shop default](components/crops/shop-card-default.png)

#### Related product card
A card in "More from this shop"/"Similar Fonts"; measured, never followed. The rails rendered empty on this capture — recorded as a miss if absent. Read as `related-card` on the product page.

Not on the page when it was captured.

### Sign-in

The /sign-in card: "Welcome back to the world's marketplace for design", the 43px username and password fields, the teal Log In button and three SSO buttons — Log In was never pressed.

#### Sign-in headline
"Welcome back to the world's marketplace for design". Read as `signin-h1` on the sign-in page.

**Values (default).** size 673 x 96; background transparent; text Averta 36/48 600, #303538.

![Sign-in headline default](components/crops/signin-h1-default.png)

#### Username field
The username text field; filled with a placeholder, never submitted. Read as `username-field` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, filled) | size 436.66 x 43; padding 0px 16px; background transparent; text Averta 14/20 400, #303538; placeholder #303538 |

![Username field default](components/crops/username-field-default.png) ![Username field focus-visible](components/crops/username-field-focus-visible.png) ![Username field filled](components/crops/username-field-filled.png)

#### Password field
The password field; never filled, never submitted. Read as `password-field` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 392.66 x 43; padding 0px 0px 0px 16px; background transparent; text Averta 14/20 400, #303538; placeholder #303538 |

![Password field default](components/crops/password-field-default.png) ![Password field focus-visible](components/crops/password-field-focus-visible.png)

#### Checkbox
A sign-in checkbox (remember me); never toggled. Read as `remember-check` on the sign-in page.

Not on the page when it was captured.

#### Log In button
The sign-in submit; measured only — pressing it would post credentials. Read as `login-btn` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 438.66 x 51; padding 12px 30px; border 2px solid #088178 `color.brand.teal`; radius 3px; background #088178 `color.brand.teal`; text Averta 18/normal 600, #ffffff; transition all 0.25s ease |
| hover | border 2px solid #003a37 `color.brand.teal-hover`; background #003a37 `color.brand.teal-hover` |
| focus-visible | shadow rgba(182, 231, 228, 0.45) 0px 0px 0px 5px |
| pressed | border 2px solid #003a37 `color.brand.teal-hover`; background #003a37 `color.brand.teal-hover` |

![Log In button default](components/crops/login-btn-default.png) ![Log In button hover](components/crops/login-btn-hover.png) ![Log In button focus-visible](components/crops/login-btn-focus-visible.png) ![Log In button pressed](components/crops/login-btn-pressed.png)

#### Google SSO
"Log In Using Google"; measured, OAuth never followed. Read as `sso-btn` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 438.66 x 51; padding 12px 30px; border 2px solid #303538; radius 3px; background #ffffff; text Averta 18/normal 600, #303538; transition all 0.25s ease |
| hover | background rgba(48, 53, 56, 0.1) |
| focus-visible | shadow rgba(182, 231, 228, 0.45) 0px 0px 0px 5px |
| pressed | background rgba(48, 53, 56, 0.1) |

![Google SSO default](components/crops/sso-btn-default.png) ![Google SSO hover](components/crops/sso-btn-hover.png) ![Google SSO focus-visible](components/crops/sso-btn-focus-visible.png) ![Google SSO pressed](components/crops/sso-btn-pressed.png)

### Search

The /search surface: the 48px heading and the 320px result cards.

#### Search heading
The results heading for ?q=font. Read as `search-h1` on the search page.

**Values (default).** size 1376 x 70.38; padding 7.2px 0px; background transparent; text Averta 48/56 600, #303538.

![Search heading default](components/crops/search-h1-default.png)

#### Result card
A results-grid card; measured, never followed. Read as `result-card` on the search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 320 x 213.33; background transparent; text Averta 14/14 400, #303538; icon 16 x 16, #303538; layers a 320.0x213.3 rgb(237, 242, 245); div.product-thumbnail-badge 143.4x28.0 rgb(255, 255, 255) T:1px solid rgb(237, 242, 245) / R:1px solid rgb(237, 242, 245) / B:1px solid rgb(237, 242, 245) / L:1px solid rgb(237, 242, 245) 0px 18px 0px 0px; button.like-button.product-thumbnail__like-button 30.0x30.0 rgba(255, 255, 255, 0.9) rgba(0, 0, 0, 0.1) 0px 1px 8px 0px, rgba(0, 0, 0, 0.05) 0px 0px 1px 1px, rg |
| hover | text Averta 14/14 400, #003a37 `color.brand.teal-hover`; layers a 320.0x213.3 rgb(237, 242, 245); div.product-thumbnail__font-preview 320.0x213.3 rgb(255, 255, 255); div.product-thumbnail-badge 143.4x28.0 rgb(255, 255, 255) T:1px solid rgb(237, 242, 245) / R:1px solid rgb(237, 242, 245) / B:1px solid rgb(237, 242, 245) / L:1px solid rgb(237, 242, 245) 0px 18px 0px 0px; button.like-button.product-thumbnail__like-button 30.0x30.0 rgba(255, 255, 255, 0.9) rgba(0, |
| pressed | layers a 320.0x213.3 rgb(237, 242, 245); div.product-thumbnail__font-preview 320.0x213.3 rgb(255, 255, 255); div.product-thumbnail-badge 143.4x28.0 rgb(255, 255, 255) T:1px solid rgb(237, 242, 245) / R:1px solid rgb(237, 242, 245) / B:1px solid rgb(237, 242, 245) / L:1px solid rgb(237, 242, 245) 0px 18px 0px 0px; button.like-button.product-thumbnail__like-button 30.0x30.0 rgba(255, 255, 255, 0.9) rgba(0, |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: a 320x213.3 background #edf2f5; div 143.4x28 background #ffffff border 1px solid #edf2f5 radius 0px 18px 0px 0px; button 30x30 background rgba(255, 255, 255, 0.9) radius 3.35544e+07px shadow rgba(0, 0, 0, 0.1) 0px 1px 8px 0px, rgba(0, 0, 0, 0.05) 0px 0px 1px 1px, #ffffff 0px 1px 1px 0px inset, rgba(255, 255, 255, 0.25) 0px -1px 0px 0px inset.

![Result card default](components/crops/result-card-default.png) ![Result card hover](components/crops/result-card-hover.png) ![Result card pressed](components/crops/result-card-pressed.png)

### Membership

The /membership surface: the 72px purple hero and the 274x323 plan cards.

#### Membership headline
The membership page heading. Read as `membership-h1` on the membership page.

**Values (default).** size 730 x 160; background transparent; text Brule 72/80 600, #4e42a1 `color.brand.accent`.

![Membership headline default](components/crops/membership-h1-default.png)

#### Plan card
A membership plan card (name, price, benefits, CTA); measured, never purchased. Read as `plan-card` on the membership page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 274 x 323; padding 30px; radius 16px; background #ffffff; text Averta 16/28 700, #6e777d |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Plan card default](components/crops/plan-card-default.png) ![Plan card hover](components/crops/plan-card-hover.png) ![Plan card pressed](components/crops/plan-card-pressed.png)

### Footer

The 488px footer: category link columns, the socials row and the legal links.

#### Footer
The footer: the logo/about column plus the five link sections (c-site-footer__main, 1376x322). Read as `footer` on the home page.

**Values (default).** size 1440 x 488.5; padding 48px 32px; background transparent; text Averta 14/22 400, #303538; icon 99.98 x 39.47, #303538.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer link; measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 169.16 x 19; background transparent; text Averta 15/37.5 400, #303538; transition color 0.25s ease |
| hover | text Averta 15/37.5 400, #003a37 `color.brand.teal-hover` |
| focus-visible | outline 2px solid #e06868, offset 1px; layers a 169.2x19.0 2px solid rgb(224, 104, 104) offset 1px |
| pressed | text Averta 15/37.5 400, #003a37 `color.brand.teal-hover` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social link
A social icon in the about column. Read as `social-icon` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 20 x 20; background transparent; text Averta 16/24 400, #000000; transition all 0.2s ease-in-out; opacity 0.7; icon 20 x 20, #303538 |
| hover | opacity none |
| focus-visible | outline 2px solid #e06868, offset 1px; layers a 20.0x20.0 2px solid rgb(224, 104, 104) offset 1px |

![Social link default](components/crops/social-icon-default.png) ![Social link hover](components/crops/social-icon-hover.png) ![Social link focus-visible](components/crops/social-icon-focus-visible.png) ![Social link pressed](components/crops/social-icon-pressed.png)

### Mobile (390 wide)



#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 119; background #ffffff; text Averta 10/8 600, #ffffff; icon 18 x 19, #088178 `color.brand.teal`.

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
The header menu button that opens the nav overlay. Read as `m-menu-button` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 45 x 45; border 2px solid transparent; radius 3.35544e+07px; background transparent; text Averta 14/14 600, #088178 `color.brand.teal`; transition color 0.2s cubic-bezier(0.32, 0, 0.59, 0.03), background-color 0.2s cubic-bezier(0.32, 0, 0.59, 0.03), border-color 0.2s cubic-bezier(0.32, 0, 0.59, 0.03); icon 18 x 19, #088178 `color.brand.teal` |
| focus-visible | outline 2px solid #088178 `color.brand.teal`, offset 2px |

![Menu button default](components/crops/m-menu-button-default.png) ![Menu button hover](components/crops/m-menu-button-hover.png) ![Menu button focus-visible](components/crops/m-menu-button-focus-visible.png) ![Menu button pressed](components/crops/m-menu-button-pressed.png)

#### Mobile menu, open
The opened nav overlay (.mobile-menu). Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 295.5 x 844; padding 32px 24px 48px 24px; background #ffffff; text Averta 14/22 600, #303538; transition all 0.4s cubic-bezier(0.25, 1, 0.5, 1); icon 18 x 18, #088178 `color.brand.teal`.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Mobile menu row
A row inside the opened nav overlay. Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40.73 x 18; background transparent; text Averta 14/21 600, #303538; transition color 0.25s ease |
| hover | text Averta 14/21 600, #003a37 `color.brand.teal-hover` |
| focus-visible | outline 2px solid #e06868, offset 1px; layers a 40.7x18.0 2px solid rgb(224, 104, 104) offset 1px |
| pressed | text Averta 14/21 600, #003a37 `color.brand.teal-hover` |

![Mobile menu row default](components/crops/m-nav-item-default.png) ![Mobile menu row hover](components/crops/m-nav-item-hover.png) ![Mobile menu row focus-visible](components/crops/m-nav-item-focus-visible.png) ![Mobile menu row pressed](components/crops/m-nav-item-pressed.png)

#### Mobile heading
Read as `m-heading` on the home page at 390 wide.

**Values (default).** size 283.83 x 26; background transparent; text Averta 20/24 600, #303538.

![Mobile heading default](components/crops/m-heading-default.png)

#### Mobile search
The mobile search bar; never submitted. Read as `m-search` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 358 x 46; background transparent; text Averta 14/20 600, #303538; icon 16 x 16, #899298; layers input.search-field__input 358.0x46.0 rgb(250, 253, 255) T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 100px; div::before.search-field__category 1pxx24px rgb(137, 146, 152); div.multiselect__tags 120.0x32.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, |
| hover, focus-visible | layers input.search-field__input 358.0x46.0 rgb(250, 253, 255) T:1px solid rgb(204, 212, 218) / R:1px solid rgb(204, 212, 218) / B:1px solid rgb(204, 212, 218) / L:1px solid rgb(204, 212, 218) 100px; div::before.search-field__category 1pxx24px rgb(137, 146, 152); div.multiselect__tags 120.0x32.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba( |

Child layers that carry the look: input 358x46 background #fafdff border 1px solid transparent radius 100px; div::before 1pxx24px background #899298; div 120x32 border 1px solid transparent radius 8px shadow transparent 0px 0px 0px 3px.

![Mobile search default](components/crops/m-search-default.png) ![Mobile search hover](components/crops/m-search-hover.png) ![Mobile search focus-visible](components/crops/m-search-focus-visible.png) ![Mobile search pressed](components/crops/m-search-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Creative Market wordmark, the cart glyph, the hamburger glyph, the social glyphs and the product artwork) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

The signed-in account — the dashboard, purchases, downloads, the cart's checkout and the sell/author studio — was never reached. /sign-in is a username/password card whose Log In was never pressed; every purchase CTA (Add to cart, Buy now, the plan CTAs) was measured, never followed. What the product looks like past the public catalogue is not documented here.

### Pages

- **Purchases and CTAs.** Add to cart, Buy now, the enterprise contact CTA, every membership plan CTA and Save 25% were measured or screenshotted, never followed; no purchase was made, nothing was added to the cart and no file was fetched.
- **Sign in.** The username field was filled with a placeholder and cleared; Log In, the SSO buttons and Join were never pressed, so the authenticated step is undocumented.
- **External surfaces** (shop storefronts beyond the captured product page, social profiles, the blog/inspiration hub) are linked from the site but were never opened.
- **The home h1.** "Bring your creative ideas to life." is painted by the hero illustration rather than a text node; the section headings were measured instead.
- **Cloudflare Turnstile** greets some routes headless; fresh contexts and patient waits cleared it this run, but a still-blocked route is a boundary, not a bypass target.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.
- **The nav dropdowns** (FONTS, TEMPLATES, MORE and the All Categories search facet) were never opened — they are flyout menus captured only as nav rows.
- **The license radios** in the buy box were measured at rest; ticking one changes the price but was never clicked.
- **The Reviews/Comments/FAQs accordions** were toggled open and closed locally for the opened-state reading.

### Themes

One theme only: the storefront paints data-theme="legacy" — white page, #303538 ink, #088178 teal actions. The sheets carry no second theme layer; tokens.json's dark set is intentionally empty.

### Fonts

- **Averta** (600 on every heading, 400 UI) is served from CloudFront as a licensed webfont (harvested src list in raw/css-vars.json). The style guide falls back to system sans — the webfont is licensed, not shipped.

### Screenshots

- The product artwork, masthead illustrations and the Creative Market wordmark in the screenshots are the product's published content; only frames and components were measured.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- The kit/template artwork, product previews, plan feature lists and marketing copy are the product's content; only frames and components were measured.
