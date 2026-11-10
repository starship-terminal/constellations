# Allbirds patterns

How the measured components combine into the storefront's screens. Every value named here is a token in [tokens.json](tokens.json); the component entries are in [components.md](components.md) and the screens in [screenshots/](screenshots).

## Storefront chrome

Every page hangs from the same two-strip chrome: the `component.promo-bar` announcement strip (ink background, white `xs` uppercase text, 32px) over `component.header` — the rounded white nav bar (`elevation.header`) with the serif wordmark, uppercase `tracking-widest` links, the MEN/WOMEN mega-menu buttons, and search + bag at the right. The bar is a floating card over `background.page`, not a full-bleed strip. On mobile it collapses to a 46px ink bar with hamburger and bag.

- Desktop: [home-light-default](screenshots/home-light-default.png), [mega-menu](#mega-menu), [search overlay](#search)
- Mobile: [mobile-home-light-default](screenshots/mobile-home-light-default.png), [menu drawer](#menu-drawer)

## Browse → collection → product

The purchase path: marketing home (rounded photo cards, serif headlines, pill CTAs) → collection grid (serif title, `filter-button`, cards with image + name + price + `more-colors` swatch hints) → PDP (serif title, uppercase price, `swatch` circles, `size-tab`, the `size-button` grid, Fit Guide, `atc-button`, accordions).

- Home: [home-light-full](screenshots/home-light-full.png)
- Collection: [collection-light-default](screenshots/collection-light-default.png), [collection-light-full](screenshots/collection-light-full.png)
- Product: [product-light-default](screenshots/product-light-default.png), [product-light-full](screenshots/product-light-full.png)

## Filtering

The collection's Filter button opens `filter-sheet`, a white `z-takeover` panel over the `elevation.backdrop` dim; Escape or its own close returns to the grid. The same takeover layer carries every overlay in the store.

- [collection-light-filter](screenshots/collection-light-filter.png), [filter-sheet](components/crops/filter-sheet-open.png)

## Selection states on the PDP

Option picking is a two-step grammar: `swatch` circles pick colour (the held one takes the `border.ink` ring), then the `size-button` grid picks size — available chips are `border.stroke` hairlines on white, the held chip washes `action.pressed-fill`, and `size-button-disabled` chips strike through at reduced opacity rather than disappearing. A valid size enables the ink `atc-button`; before that it reads as a disabled primary.

- [product-light-options](screenshots/product-light-options.png), [mobile-product-light-options](screenshots/mobile-product-light-options.png)

## Cart

`atc-button` opens `cart-drawer`, the right-hand `z-takeover` takeover: `CART (n)` heading, free-shipping meter, item rows with a quiet `+` stepper, the `natural-white-60` upsell band with `component.upsell-card` rows, subtotal, the ink checkout pill, then the Shopify-hosted wallet row. The drawer never navigates — it dismisses back to the PDP.

- [product-light-cart-drawer](screenshots/product-light-cart-drawer.png), [mobile-product-light-cart-drawer](screenshots/mobile-product-light-cart-drawer.png), [cart-drawer-open](components/crops/cart-drawer-open.png)
- The empty `/cart` page: [cart-light-default](screenshots/cart-light-default.png)

## Mega-menu

Hovering MEN or WOMEN opens the flyout under the nav bar: category columns with small circular swatch images and uppercase links, over the same `background.surface` white.

- [home-light-menu](screenshots/home-light-menu.png), [mega-menu](components/crops/mega-menu-default.png)

## Search

The Search nav item opens the store's search overlay from the same chrome; the standalone `/search` page holds the same field.

- [home-light-search](screenshots/home-light-search.png), [searchpage-light-default](screenshots/searchpage-light-default.png)

## Menu drawer

On mobile the hamburger opens `m-menu-drawer`, a full-height left takeover listing the same nav tree with the `m-ai-chip` ("Shop with AI") shortcut pinned near it.

- [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-drawer](components/crops/m-menu-drawer-open.png)

## Forms

Fields are pills too: `email-input` (the footer subscribe row) and the search field share the `component.field` shape — `radius.pill`, `border.stroke`, `text.secondary` placeholder. The Shopify-hosted `/account/login` card uses Shop's own faces and a `login-submit` pill; it is the only surface measured off-theme.

- [account-light-default](screenshots/account-light-default.png), [account-light-focus](screenshots/account-light-focus.png), [home-light-full](screenshots/home-light-full.png) (footer)

## Content pages

Our Story, Materials, Help and the Blog index reuse the marketing grammar — serif display over `natural-white` sections, rounded photo cards, pill CTAs — with no commerce components.

- [story-light-full](screenshots/story-light-full.png), [materials-light-full](screenshots/materials-light-full.png), [help-light-full](screenshots/help-light-full.png), [blog-light-full](screenshots/blog-light-full.png)

## Not reached

Checkout (never pressed), anything behind sign-in, and payment-side error/empty states. The geofencing dialog is a first-visit-only takeover and was removed before capture.
