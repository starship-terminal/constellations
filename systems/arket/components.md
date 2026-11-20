# ARKET components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from arket.com on 2026-11-11, signed out, in headed real Chrome at 1440 x 900 (the Mobile group at 390 x 844) — Akamai serves headless Chromium Access Denied (403), and also blocks every /en-ww/product/<slug>-<id>/ URL and, for this client, the /en-ww/ root: the shell and dialogs were measured on /en-ww/women/ — with computed styles read from the running page. Nothing was bought, sent, submitted or signed into.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (58 components, 133 states).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (128 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: the site paints one light theme. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Women landing | `/en-ww/women/` | [default](screenshots/women-light-default.png), [full](screenshots/women-light-full.png) |
| New arrivals | `/en-ww/women/new-arrivals/` | [default](screenshots/new-arrivals-light-default.png), [full](screenshots/new-arrivals-light-full.png) |
| Clothing listing | `/en-ww/women/clothing/` | [default](screenshots/clothing-light-default.png), [filter](screenshots/clothing-light-filter.png), [full](screenshots/clothing-light-full.png) |
| Men clothing | `/en-ww/men/clothing/` | [default](screenshots/men-clothing-light-default.png), [full](screenshots/men-clothing-light-full.png) |
| Gift shop | `/en-ww/gift-shop/` | [default](screenshots/gift-shop-light-default.png), [full](screenshots/gift-shop-light-full.png) |
| Editorial / About | `/en-ww/editorial/` | [default](screenshots/editorial-light-default.png), [full](screenshots/editorial-light-full.png) |
| Customer service | `/en-ww/customer-service/` | [default](screenshots/customer-service-light-default.png), [full](screenshots/customer-service-light-full.png) |
| Account gate | `/en-ww/account/` | [default](screenshots/account-light-default.png), [full](screenshots/account-light-full.png) |
| Previous collections | `/en-ww/previous-collections/women/` | [default](screenshots/previous-collections-light-default.png), [full](screenshots/previous-collections-light-full.png) |
| Women landing, phone | `/en-ww/women/` |  |
| Clothing listing, phone | `/en-ww/women/clothing/` | [default](screenshots/mobile-clothing-light-default.png), [full](screenshots/mobile-clothing-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Cookie consent, as it arrives | women landing | mounted on first load; measured and hidden, never answered | [consent-card](#cookie-consent-card) |
| Location dialog, as it arrives | women landing | mounted on first load; measured and hidden, never answered | [location-dialog](#location-dialog) |
| Search field, focused | women landing | the header search input clicked into; nothing typed or sent | [search-field](#search-field) |
| Cart drawer, empty | women landing | the cart icon's own press | [cart-drawer](#cart-drawer-empty) |
| Filter panel, open | clothing | the Filter button's own press; nothing applied | [filter-panel](#filter-panel-open) |
| Mobile menu, open | women landing, phone | the menu button's own toggle | [m-menu-open](#mobile-menu-open) |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 22 components were given a real keyboard focus. 22 show a visible focus state: `consent-accept` (1px auto #005fcc, offset 0px), `consent-required` (1px auto #005fcc, offset 0px), `consent-settings-link` (1px auto #005fcc, offset 0px), `location-continue` (1px auto #005fcc, offset 0px), `location-stay` (1px auto #005fcc, offset 0px), `nav-item` (1px auto #005fcc, offset 0px), `account-button` (1px auto #005fcc, offset 1px), `wishlist-link` (1px auto #005fcc, offset 1px), `cart-button` (1px auto #005fcc, offset 0px), `locale-button` (1px auto #005fcc, offset 0px), `cafe-link` (1px auto #005fcc, offset 1px), `service-link` (1px auto #005fcc, offset 1px), `read-more` (1px auto #005fcc, offset 0px), `filter-button` (1px auto #005fcc, offset 0px), `sort-button` (1px auto #005fcc, offset 0px), `view-button` (1px auto #005fcc, offset 0px), `service-accordion` (1px auto #005fcc, offset 0px), `gate-continue` (1px auto #005fcc, offset 0px), `footer-link` (1px auto #005fcc, offset 1px), `footer-social` (1px auto #005fcc, offset 1px), `m-menu-button` (1px auto #005fcc, offset 0px), `m-search` (1px auto #005fcc, offset 0px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover): a state a real press could submit (consent, location, gate) was never pressed. Nothing was bought, sent or signed into.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, all, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | card-add-bag, card-img-next, card-img-prev, card-wishlist, cart-drawer, filter-button, filter-panel, header and more |
| 0.3s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | location-search |
| 0.3s | `ease-in-out` | height, top | consent-card |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Cookie consent card](#cookie-consent-card) | 343 x 447.9 | - | - | #ffffff `color.white` | rgba(0, 0, 0, 0.2) 0px 4px 16px 0px | 0 |
| [Location dialog](#location-dialog) | 538 x 900 | - | - | #ffffff `color.white` | none | 0 |
| [Filter panel, open](#filter-panel-open) | 538 x 900 | - | - | #ffffff `color.white` | none | 0 |
| [Cart drawer, empty](#cart-drawer-empty) | 538 x 900 | - | - | #ffffff `color.white` | none | 0 |
| [Product card](#product-card) | 357 x 109.5 | - | - | transparent | none | 0 |
| [Search field](#search-field) | 680 x 40 | - | 4px | #f9f9f9 `color.grey.light.extra` | none | 0px 48px 0px 44px |
| [Email field](#email-field) | 624 x 60 | 1px solid #767676 `color.grey.dark` | - | #ffffff `color.white` | none | 8px 8px 10px 15px |

## Components

### Consent and location dialogs

The two overlays the storefront mounts before the page is usable: the cookie-consent card and the location picker. Measured as they arrive, never answered.

#### Cookie consent card
"Before you start shopping": the consent card measured as it arrives, never answered. Read as `consent-card` on the women landing page.

**Values (default).** size 343 x 447.9; background #ffffff `color.white`; shadow rgba(0, 0, 0, 0.2) 0px 4px 16px 0px; text Arket Sans 16/24 400, #000000 `color.black`; transition top 0.3s ease-in-out, height 0.3s ease-in-out.

![Cookie consent card default](components/crops/consent-card-default.png)

#### Accept all button
The consent primary. Measured, never pressed. Read as `consent-accept` on the women landing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 295 x 56; padding 4px 32px 6px 32px; border 1px solid #000000 `color.black`; radius 2px; background #000000 `color.black`; text Arket Sans 20/16 400, #ffffff `color.white` |
| hover | background #080808 |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | background #080808 |

![Accept all button default](components/crops/consent-accept-default.png) ![Accept all button hover](components/crops/consent-accept-hover.png) ![Accept all button focus-visible](components/crops/consent-accept-focus-visible.png) ![Accept all button pressed](components/crops/consent-accept-pressed.png)

#### Only required cookies button
The consent secondary. Measured, never pressed. Read as `consent-required` on the women landing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 295 x 56; padding 4px 32px 6px 32px; border 1px solid #000000 `color.black`; radius 2px; background #000000 `color.black`; text Arket Sans 20/16 400, #ffffff `color.white` |
| hover | background #080808 |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | background #080808 |

![Only required cookies button default](components/crops/consent-required-default.png) ![Only required cookies button hover](components/crops/consent-required-hover.png) ![Only required cookies button focus-visible](components/crops/consent-required-focus-visible.png) ![Only required cookies button pressed](components/crops/consent-required-pressed.png)

#### Cookie settings link
The text link to the settings panel. Measured, never pressed. Read as `consent-settings-link` on the women landing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 171.98 x 40; background #ffffff `color.white`; text Arket Sans SC 13/19.5 400, #080808 |
| focus-visible | outline 1px auto #005fcc, offset 0px |

![Cookie settings link default](components/crops/consent-settings-link-default.png) ![Cookie settings link hover](components/crops/consent-settings-link-hover.png) ![Cookie settings link focus-visible](components/crops/consent-settings-link-focus-visible.png) ![Cookie settings link pressed](components/crops/consent-settings-link-pressed.png)

#### Location dialog
"Please confirm your location", the auto-mounted <dialog>. Measured, never answered. Read as `location-dialog` on the women landing page.

**Values (default).** size 538 x 900; background #ffffff `color.white`; text arketSansMono 22/28 400, #000000 `color.black`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #000000 `color.black`.

![Location dialog default](components/crops/location-dialog-default.png)

#### Country search field
The "Search country" input; focused only, nothing typed. Read as `location-search` on the women landing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 490 x 56; padding 16px 56px 16px 16px; border 1px solid #767676 `color.grey.dark`; radius 2px; background #ffffff `color.white`; text arketSansMono 16/22 400, #000000 `color.black`; transition color 0.3s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0.4, 0, 0.2, 1), fill 0.3s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.3s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.3s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.3s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.3s cubic-bezier(0.4, 0, 0.2, 1); placeholder #9ca3af |
| focused | border 1px solid #000000 `color.black`; outline 1px auto #005fcc, offset 0px |

![Country search field default](components/crops/location-search-default.png) ![Country search field focused](components/crops/location-search-focused.png)

#### Continue to country button
The black confirm action. Measured, never pressed. Read as `location-continue` on the women landing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 458 x 32; padding 4px 12px; border 1px solid transparent; radius 2px; background #000000 `color.black`; text arketSansMono 16/22 400, #ffffff `color.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | opacity 0.9 |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | opacity 0.9 |

![Continue to country button default](components/crops/location-continue-default.png) ![Continue to country button hover](components/crops/location-continue-hover.png) ![Continue to country button focus-visible](components/crops/location-continue-focus-visible.png) ![Continue to country button pressed](components/crops/location-continue-pressed.png)

#### Stay in country button
The outlined alternative. Measured, never pressed. Read as `location-stay` on the women landing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 458 x 32; padding 4px 12px; border 1px solid #000000 `color.black`; radius 2px; background transparent; text arketSansMono 16/22 400, #000000 `color.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #000000 `color.black`; text arketSansMono 16/22 400, #ffffff `color.white`; opacity 0.9 |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | background #000000 `color.black`; text arketSansMono 16/22 400, #ffffff `color.white`; opacity 0.9 |

![Stay in country button default](components/crops/location-stay-default.png) ![Stay in country button hover](components/crops/location-stay-hover.png) ![Stay in country button focus-visible](components/crops/location-stay-focus-visible.png) ![Stay in country button pressed](components/crops/location-stay-pressed.png)

#### Country row
A country/currency row in the list. Measured, never pressed. Read as `location-row` on the women landing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 490 x 38; background transparent; text arketSansMono 16/22 400, #000000 `color.black`; icon 12 x 8, #000000 `color.black` |

Child layers that carry the look: details 490x38 radius 6px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 2px 10px 2px; button 458x32 background #000000 `color.black` border 1px solid transparent radius 2px.

![Country row default](components/crops/location-row-default.png) ![Country row hover](components/crops/location-row-hover.png)

### Shell and navigation

The locale notice, the promo strip and the sticky header: wordmark, search field, account, wishlist and cart icons, and the category nav that opens the drawer.

#### Locale notice bar
The top "Location and language: <country>/<lang>" strip with Change and Close. Read as `locale-notice` on the women landing page.

**Values (default).** size 379.06 x 22; background transparent; text arketSansMono 16/22 400, #000000 `color.black`.

![Locale notice bar default](components/crops/locale-notice-default.png)

#### Promo strip
The thin promo line under the notice bar. Read as `promo-strip` on the women landing page.

**Values (default).** size 1440 x 56; border B: 1px solid #f5f5f5 `color.grey.light.default`; background #ffffff `color.white`; text arketSansMono 16/16 400, #000000 `color.black`; icon 16 x 16, #000000 `color.black`.

![Promo strip default](components/crops/promo-strip-default.png)

#### Header
The sticky z-header bar: wordmark, search field, account, wishlist, cart. Read as `header` on the women landing page.

**Values (default).** size 1440 x 120; background #ffffff `color.white`; text arketSansMono 16/30 400, #000000 `color.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1).

![Header default](components/crops/header-default.png)

#### Logo
Read as `logo` on the women landing page.

**Values (default).** size 43.31 x 40; background transparent; text arketSCSansMono 16/16 400, #000000 `color.black`.

![Logo default](components/crops/logo-default.png)

#### Nav item
A top-level shop category button; opens the nav drawer at that section. Read as `nav-item` on the women landing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 71.57 x 30; padding 0px 8px; radius 2px; background transparent; text arketSansMono 16/30 400, #000000 `color.black` |
| hover | background #000000 `color.black`; text arketSansMono 16/30 400, #ffffff `color.white` |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | background #000000 `color.black`; text arketSansMono 16/30 400, #ffffff `color.white` |

![Nav item default](components/crops/nav-item-default.png) ![Nav item hover](components/crops/nav-item-hover.png) ![Nav item focus-visible](components/crops/nav-item-focus-visible.png) ![Nav item pressed](components/crops/nav-item-pressed.png)

#### Account button
The account icon button. Measured, never followed. Read as `account-button` on the women landing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 85.69 x 22; background transparent; text arketSansMono 16/22 400, #000000 `color.black` |
| focus-visible | outline 1px auto #005fcc, offset 1px |

![Account button default](components/crops/account-button-default.png) ![Account button hover](components/crops/account-button-hover.png) ![Account button focus-visible](components/crops/account-button-focus-visible.png) ![Account button pressed](components/crops/account-button-pressed.png)

#### Wishlist link
The wishlist icon link. Measured, never followed. Read as `wishlist-link` on the women landing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 32 x 32; background transparent; text arketSansMono 10/15 400, #000000 `color.black`; icon 32 x 32, #000000 `color.black` |
| focus-visible | outline 1px auto #005fcc, offset 1px |

![Wishlist link default](components/crops/wishlist-link-default.png) ![Wishlist link hover](components/crops/wishlist-link-hover.png) ![Wishlist link focus-visible](components/crops/wishlist-link-focus-visible.png) ![Wishlist link pressed](components/crops/wishlist-link-pressed.png)

#### Cart button
The bag icon button; opens the cart drawer. Read as `cart-button` on the women landing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 32 x 32; background transparent; text arketSansMono 10/15 400, #000000 `color.black`; icon 32 x 32, #000000 `color.black` |
| focus-visible | outline 1px auto #005fcc, offset 0px |

![Cart button default](components/crops/cart-button-default.png) ![Cart button hover](components/crops/cart-button-hover.png) ![Cart button focus-visible](components/crops/cart-button-focus-visible.png) ![Cart button pressed](components/crops/cart-button-pressed.png)

#### Locale button
The "AR | EN" region/language button. Measured, never pressed. Read as `locale-button` on the women landing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 73.23 x 22; background transparent; text arketSansMono 16/22 400, #000000 `color.black`; icon 12 x 12, #000000 `color.black` |
| focus-visible | outline 1px auto #005fcc, offset 0px |

![Locale button default](components/crops/locale-button-default.png) ![Locale button hover](components/crops/locale-button-hover.png) ![Locale button focus-visible](components/crops/locale-button-focus-visible.png) ![Locale button pressed](components/crops/locale-button-pressed.png)

#### ARKET CAFÉ link
The café utility link. Measured, never followed. Read as `cafe-link` on the women landing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 115.63 x 30; padding 0px 8px; background transparent; text arketSansMono 16/30 400, #000000 `color.black` |
| focus-visible | outline 1px auto #005fcc, offset 1px |

![ARKET CAFÉ link default](components/crops/cafe-link-default.png) ![ARKET CAFÉ link hover](components/crops/cafe-link-hover.png) ![ARKET CAFÉ link focus-visible](components/crops/cafe-link-focus-visible.png) ![ARKET CAFÉ link pressed](components/crops/cafe-link-pressed.png)

#### Search field
The header search input; focused only, nothing typed or sent. Read as `search-field` on the women landing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 680 x 40; padding 0px 48px 0px 44px; radius 4px; background #f9f9f9 `color.grey.light.extra`; text arketSansMono 16/22 400, oklab(0 0 0 / 0.6); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder oklab(0 0 0 / 0.6) |

![Search field default](components/crops/search-field-default.png) ![Search field focused](components/crops/search-field-focused.png)

#### Cart drawer, empty
The bag drawer after its own icon press; the signed-out bag is empty. Read as `cart-drawer` on the women landing page.

**Values (default).** size 538 x 900; background #ffffff `color.white`; text arketSansMono 22/28 400, #000000 `color.black`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 24 x 24, #000000 `color.black`.

![Cart drawer, empty default](components/crops/cart-drawer-default.png)

### Home

The /en-ww/women/ landing: campaign tiles and editorial sections.

#### Hero heading
Read as `hero-title` on the women landing page.

**Values (default).** size 208.41 x 34; background transparent; text arketSansMono 28/34 400, #000000 `color.black`.

![Hero heading default](components/crops/hero-title-default.png)

#### Campaign tile
A hero/editorial image tile link (the whole tile is the link). Read as `tile-card` on the women landing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 720 x 960.05; background transparent; text arketSansMono 10/15 400, #000000 `color.black` |

![Campaign tile default](components/crops/tile-card-default.png) ![Campaign tile hover](components/crops/tile-card-hover.png)

#### Section heading
Read as `section-title` on the women landing page.

**Values (default).** size 208.41 x 34; background transparent; text arketSansMono 28/34 400, #000000 `color.black`.

![Section heading default](components/crops/section-title-default.png)

#### Tile label
The text on a campaign tile. Read as `tile-label` on the women landing page.

**Values (default).** size 300 x 56; background transparent; text arketSansMono 22/28 400, #000000 `color.black`.

![Tile label default](components/crops/tile-label-default.png)

### Listing page

The category grid: Filter/Sort/View controls, product cards with image carousels, hover-revealed quick-adds and the colour count chip.

#### Category title
"Women's clothes" h1. Read as `plp-title` on the clothing listing page.

**Values (default).** size 624 x 50; padding 0px 0px 16px 0px; background transparent; text arketSansMono 28/34 400, #000000 `color.black`.

![Category title default](components/crops/plp-title-default.png)

#### Breadcrumb
The ARKET / Women / Clothing trail. Read as `breadcrumb` on the clothing listing page.

**Values (default).** size 443.53 x 30; background transparent; text arketSansMono 16/30 400, #000000 `color.black`.

Child layers that carry the look: div 376.7x724 background #ffffff `color.white`; div 376.7x724 border 1px solid #000000 `color.black`; button 0x0 background #ffffff `color.white`.

![Breadcrumb default](components/crops/breadcrumb-default.png)

#### Read more button
The category intro expander; a local toggle, measured closed. Read as `read-more` on the clothing listing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 93.57 x 22; padding 2px 8px; border 1px solid #000000 `color.black`; radius 99990px; background #ffffff `color.white`; text arketSansMono 12/16 400, #000000 `color.black`; icon 12 x 12, #000000 `color.black` |
| focus-visible | outline 1px auto #005fcc, offset 0px |

![Read more button default](components/crops/read-more-default.png) ![Read more button hover](components/crops/read-more-hover.png) ![Read more button focus-visible](components/crops/read-more-focus-visible.png) ![Read more button pressed](components/crops/read-more-pressed.png)

#### Filter button
Opens the filter panel. Measured, never applied. Read as `filter-button` on the clothing listing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 88.85 x 32; padding 4px 12px; border 1px solid #000000 `color.black`; radius 2px; background transparent; text arketSansMono 16/22 400, #000000 `color.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #000000 `color.black` |
| hover | background #000000 `color.black`; text arketSansMono 16/22 400, #ffffff `color.white`; opacity 0.9; icon 16 x 16, #ffffff `color.white` |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | background #000000 `color.black`; text arketSansMono 16/22 400, #ffffff `color.white`; opacity 0.9; icon 16 x 16, #ffffff `color.white` |

![Filter button default](components/crops/filter-button-default.png) ![Filter button hover](components/crops/filter-button-hover.png) ![Filter button focus-visible](components/crops/filter-button-focus-visible.png) ![Filter button pressed](components/crops/filter-button-pressed.png)

#### Filter panel, open
The filter sheet after the Filter button's own press; nothing inside was applied. Read as `filter-panel` on the clothing listing page.

**Values (default).** size 538 x 900; background #ffffff `color.white`; text arketSansMono 10/15 400, #000000 `color.black`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1).

![Filter panel, open default](components/crops/filter-panel-default.png)

#### Filter option
A filter facet row inside the open panel; measured, never selected. Read as `filter-option` on the clothing listing page.

Not on the page when it was captured.

#### Sort button
The sort control. Measured, never opened. Read as `sort-button` on the clothing listing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 102.2 x 32; padding 4px 12px; border 1px solid #000000 `color.black`; radius 2px; background transparent; text arketSansMono 16/22 400, #000000 `color.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #000000 `color.black` |
| hover | background #000000 `color.black`; text arketSansMono 16/22 400, #ffffff `color.white`; opacity 0.9; icon 16 x 16, #ffffff `color.white` |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | background #000000 `color.black`; text arketSansMono 16/22 400, #ffffff `color.white`; opacity 0.9; icon 16 x 16, #ffffff `color.white` |

![Sort button default](components/crops/sort-button-default.png) ![Sort button hover](components/crops/sort-button-hover.png) ![Sort button focus-visible](components/crops/sort-button-focus-visible.png) ![Sort button pressed](components/crops/sort-button-pressed.png)

#### View button
The grid-density control. Measured, never pressed. Read as `view-button` on the clothing listing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 86.34 x 32; padding 4px 12px; border 1px solid transparent; radius 2px; background #ffffff `color.white`; text arketSansMono 16/22 400, #000000 `color.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #000000 `color.black` |
| hover | opacity 0.9 |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | opacity 0.9 |

![View button default](components/crops/view-button-default.png) ![View button hover](components/crops/view-button-hover.png) ![View button focus-visible](components/crops/view-button-focus-visible.png) ![View button pressed](components/crops/view-button-pressed.png)

#### Product card
A listing card: image, name, price, "+N" colours. Read as `product-card` on the clothing listing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 357 x 109.5; background transparent; text arketSansMono 16/18 400, #000000 `color.black` |

Child layers that carry the look: span 14x16 background #272a3e border 1px solid #eaeae8 `color.grey.mid` radius 2px; span 14x16 background #4c3b3d border 1px solid #eaeae8 `color.grey.mid` radius 2px; span 14x16 background #e32b35 border 1px solid #eaeae8 `color.grey.mid` radius 2px.

![Product card default](components/crops/product-card-default.png) ![Product card hover](components/crops/product-card-hover.png)

#### New badge
The "New" tag on a card image. Read as `card-badge` on the clothing listing page.

**Values (default).** size 357 x 476; background transparent; text arketSCSansMono 12/12 400, #000000 `color.black`.

Child layers that carry the look: span 35.3x18 background #fff3db `color.peach` radius 1px.

![New badge default](components/crops/card-badge-default.png)

#### Product name
The card text block: name, price, colour count. Read as `product-name` on the clothing listing page.

**Values (default).** size 357 x 109.5; background transparent; text arketSansMono 16/18 400, #000000 `color.black`.

Child layers that carry the look: span 14x16 background #272a3e border 1px solid #eaeae8 `color.grey.mid` radius 2px; span 14x16 background #4c3b3d border 1px solid #eaeae8 `color.grey.mid` radius 2px; span 14x16 background #e32b35 border 1px solid #eaeae8 `color.grey.mid` radius 2px.

![Product name default](components/crops/product-name-default.png)

#### Price
The "$ 349" price text inside a card. Read as `price` on the clothing listing page.

**Values (default).** size 46.32 x 18; background transparent; text arketSansMono 16/18 400, #000000 `color.black`.

![Price default](components/crops/price-default.png)

#### More colours chip
The "+2" colour count. Read as `more-colors` on the clothing listing page.

**Values (default).** size 17.05 x 19; background transparent; text arketSCSansMono 16/16 400, #000000 `color.black`.

![More colours chip default](components/crops/more-colors-default.png)

#### Quick add-to-bag
The card's quick-add control, shown only while the card image is hovered. Measured, never pressed. Read as `card-add-bag` on the clothing listing page.

**Values (default).** size 36 x 35; background transparent; text arketSansMono 10/15 400, #000000 `color.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 13 x 35, #000000 `color.black`.

![Quick add-to-bag default](components/crops/card-add-bag-default.png)

#### Card wishlist button
The heart quick-toggle, shown on card hover. Measured, never pressed. Read as `card-wishlist` on the clothing listing page.

**Values (default).** size 36 x 35; background transparent; text arketSansMono 10/15 400, #000000 `color.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 17 x 35, #000000 `color.black`.

![Card wishlist button default](components/crops/card-wishlist-default.png)

#### Card image previous
The card image carousel arrow, shown on card hover. Read as `card-img-prev` on the clothing listing page.

**Values (default).** size 36 x 36; radius 2px; background #ffffff `color.white`; text arketSansMono 10/15 400, #000000 `color.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); opacity 0.3; icon 14 x 36, #000000 `color.black`.

![Card image previous default](components/crops/card-img-prev-default.png)

#### Card image next
The card image carousel arrow, shown on card hover. Read as `card-img-next` on the clothing listing page.

**Values (default).** size 36 x 36; radius 2px; background #ffffff `color.white`; text arketSansMono 10/15 400, #000000 `color.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 14 x 36, #000000 `color.black`.

![Card image next default](components/crops/card-img-next-default.png)

### Customer service

The help page's disclosure rows and links.

#### Service link
Read as `service-link` on the customer-service page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 43.31 x 40; background transparent; text arketSCSansMono 16/16 400, #000000 `color.black` |
| focus-visible | outline 1px auto #005fcc, offset 1px |

![Service link default](components/crops/service-link-default.png) ![Service link hover](components/crops/service-link-hover.png) ![Service link focus-visible](components/crops/service-link-focus-visible.png) ![Service link pressed](components/crops/service-link-pressed.png)

#### Service title
Read as `service-title` on the customer-service page.

**Values (default).** size 688 x 34; background transparent; text arketSansMono 28/34 400, #000000 `color.black`.

![Service title default](components/crops/service-title-default.png)

#### Service accordion
A help-topic disclosure row. Read as `service-accordion` on the customer-service page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 688 x 50; padding 10px 16px; border 1px solid transparent; radius 2px; background #000000 `color.black`; text arketSansMono 22/28 400, #ffffff `color.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | opacity 0.9 |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | opacity 0.9 |

![Service accordion default](components/crops/service-accordion-default.png) ![Service accordion hover](components/crops/service-accordion-hover.png) ![Service accordion focus-visible](components/crops/service-accordion-focus-visible.png) ![Service accordion pressed](components/crops/service-accordion-pressed.png)

#### Service accordion, open
The same row after its own toggle. Read as `service-accordion-open` on the customer-service page.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Account gate

The Login/Signup gate: email field and continue, measured, never submitted.

#### Gate title
The Login/Signup gate heading. Read as `gate-title` on the account gate page.

**Values (default).** size 624 x 30; background transparent; text Arket-Sans-Mono 24/30 400, #000000 `color.black`.

![Gate title default](components/crops/gate-title-default.png)

#### Email field
The sign-in email input; focused only, nothing typed or sent. Read as `gate-field` on the account gate page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 624 x 60; padding 8px 8px 10px 15px; border 1px solid #767676 `color.grey.dark`; background #ffffff `color.white`; text Arket-Sans-Mono 16/22.08 400, #000000 `color.black`; placeholder #808080 |

![Email field default](components/crops/gate-field-default.png) ![Email field focused](components/crops/gate-field-focused.png)

#### Continue button
The gate's primary action. Measured, never pressed — no sign-in was attempted. Read as `gate-continue` on the account gate page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 304 x 48; padding 6px 12px; border 1px solid #000000 `color.black`; background #ffffff `color.white`; text Arket-Sans-Mono 16/22.08 400, #000000 `color.black` |
| hover | opacity 0.9 |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | opacity 0.9 |

![Continue button default](components/crops/gate-continue-default.png) ![Continue button hover](components/crops/gate-continue-hover.png) ![Continue button focus-visible](components/crops/gate-continue-focus-visible.png) ![Continue button pressed](components/crops/gate-continue-pressed.png)

### Footer

The link columns, headings, socials and legal.

#### Footer
Read as `footer` on the women landing page.

**Values (default).** size 1440 x 464; background transparent; text arketSansMono 22/28 400, #000000 `color.black`.

Child layers that carry the look: div 1440x418 background #ffffff `color.white` border 2px solid #000000 `color.black`; div 1440x46 background #000000 `color.black`.

![Footer default](components/crops/footer-default.png)

#### Footer heading
Read as `footer-heading` on the women landing page.

**Values (default).** size 138.65 x 28; background transparent; text arketSansMono 22/28 400, #000000 `color.black`.

![Footer heading default](components/crops/footer-heading-default.png)

#### Footer link
Read as `footer-link` on the women landing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 138.65 x 28; background transparent; text arketSansMono 22/28 400, #000000 `color.black` |
| focus-visible | outline 1px auto #005fcc, offset 1px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Footer social icon
Read as `footer-social` on the women landing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 24 x 24; background transparent; text arketSansMono 10/15 400, #000000 `color.black`; icon 24 x 24, #000000 `color.black` |
| focus-visible | outline 1px auto #005fcc, offset 1px |

![Footer social icon default](components/crops/footer-social-default.png) ![Footer social icon hover](components/crops/footer-social-hover.png) ![Footer social icon focus-visible](components/crops/footer-social-focus-visible.png) ![Footer social icon pressed](components/crops/footer-social-pressed.png)

### Mobile (390 wide)

The same surface at phone width, with the menu open.

#### Mobile header
Read as `m-header` on the women landing page at 390 wide.

**Values (default).** size 390 x 107; background #ffffff `color.white`; text arketSansMono 20/28 400, #000000 `color.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 24 x 24, #000000 `color.black`.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile menu button
Read as `m-menu-button` on the women landing page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 24 x 24; background transparent; text arketSansMono 10/15 400, #000000 `color.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 24 x 24, #000000 `color.black` |
| focus-visible | outline 1px auto #005fcc, offset 0px |

![Mobile menu button default](components/crops/m-menu-button-default.png) ![Mobile menu button hover](components/crops/m-menu-button-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-button-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-button-pressed.png)

#### Mobile menu, open
The bar after its own toggle; the crop is the opened drawer that holds the links and actions. Read as `m-menu-open` on the women landing page at 390 wide.

**Values (opened).** size 24 x 24; background transparent; text arketSansMono 10/15 400, #000000 `color.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 24 x 24, #000000 `color.black`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Mobile nav link
Read inside the open menu. Read as `m-nav-link` on the women landing page at 390 wide.

**Values (default).** size 390 x 52; padding 11px 16px 12px 16px; border T: 1px solid #eaeae8 `color.grey.mid`; background transparent; text arketSansMono 20/28 400, #000000 `color.black`; icon 20 x 20, #000000 `color.black`.

![Mobile nav link default](components/crops/m-nav-link-default.png)

#### Mobile search
The mobile search affordance, header or drawer. Read as `m-search` on the women landing page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 24 x 24; background transparent; text arketSansMono 10/15 400, #000000 `color.black`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 24 x 24, #000000 `color.black` |
| focus-visible | outline 1px auto #005fcc, offset 0px |

![Mobile search default](components/crops/m-search-default.png) ![Mobile search hover](components/crops/m-search-hover.png) ![Mobile search focus-visible](components/crops/m-search-focus-visible.png) ![Mobile search pressed](components/crops/m-search-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots are ARKET's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Pages

- **Product pages (PDP).** Akamai answers every /en-ww/product/<slug>-<id>/ URL with 403 for this client, document and RSC fetch alike, so no PDP was captured; PDP-looking values come from the listing cards instead. **The /en-ww/ root** is blocked the same way at capture time; the women landing /en-ww/women/ stands in for it.
- **The account behind the gate.** /en-ww/account/ stops at the Login/Signup gate; no sign-in was attempted. Checkout, the filled cart and wishlist contents were never reached.
- **Anything that buys, sends, submits or signs in.** Nothing was added to the bag, no consent or location answer was given, no form was submitted. Quick-add buttons were measured under a forced card hover, never pressed.
- **Anything that sends, submits or signs in.** No form was submitted, no prompt was sent, no account was created. Fields clicked into (and, where a `filled` state exists, typed into and cleared), never submitted: `location-search`, `search-field`, `gate-field`.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface. The card quick-add/carousel controls only exist under a card :hover, captured via a CDP-forced hover.

### Themes

The site paints one light theme on every captured route: no dark class or attribute is bound, so the dark set is not emitted. The @theme palette is recorded in [raw/css-vars.json](raw/css-vars.json).

### Fonts

- **The faces** are arketSansMono (everything) and arketSCSansMono (small-caps chips), self-hosted woff with Arial-metric fallbacks; the consent and account surfaces fall back to 'Arket Sans'/'Arket-Sans-Mono'. The style guide renders with system fallbacks.
- Photography, campaign art and the ARKET wordmark in the screenshots are ARKET's property.

### Screenshots

- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.
- The changelog page is 91,833 px tall; its -full shot is the whole page stitched from 7 tiles.

### Content left out

- Product photography, campaign imagery and the wordmark are ARKET's content; only the frames and components were measured.
