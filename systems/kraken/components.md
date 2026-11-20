# Kraken components

Measured on kraken.com on 2026-11-18, signed out, at 1440 and 390. Values are computed styles. Crops are in [components/crops/](components/crops).

## Shell

### Top bar

The marketing header is 64px tall and transparent over the page. It holds the wordmark, product links (Kraken, Pro, Wallet, Prime, VIP, Markets, About), a language pill, search, Log in and Sign up. Crop: [header-default.png](components/crops/header-default.png).

### Sign up

Primary button. Fill `#7132f5` (`light.accent.default`), text white, radius 12px, 36px in the nav and 48px on the hero. Hover and pressed both resolve to `#5b1ecf`. Focus-visible is a 2px solid `#7132f5` outline. Crops: [nav-signup-default.png](components/crops/nav-signup-default.png), [nav-signup-hover.png](components/crops/nav-signup-hover.png), [nav-signup-focus-visible.png](components/crops/nav-signup-focus-visible.png), [nav-signup-pressed.png](components/crops/nav-signup-pressed.png), [hero-cta-default.png](components/crops/hero-cta-default.png).

### Log in

Secondary wash. Fill `rgba(133, 91, 251, 0.16)`, text `#7132f5`, radius 12px. Hover doubles the wash to `0.32`. Focus-visible is the same 2px purple outline. Crops: [nav-login-default.png](components/crops/nav-login-default.png), [nav-login-hover.png](components/crops/nav-login-hover.png).

### Search

Icon button labelled Search in the header. Opening it is a local overlay; the trigger was not separately cropped on this pass. The open state is [home-light-search-open.png](screenshots/home-light-search-open.png).

## Type

### Hero title

`h1` on the home page: Kraken-Brand, 48px / 56px, weight 400, colour `#101114`. Crop: [hero-title-default.png](components/crops/hero-title-default.png).

On /pro the same role is white, 58px / 66px, on the magic-dark ground. Crop: [pro-title-default.png](components/crops/pro-title-default.png).

## Pro

### Create free account

On the dark Pro page the high-emphasis control is near-white `#f7f7fa` with near-black text, radius 12px. Hover is `#e5e6ec`. Focus-visible is a 2px `#9d82fe` outline. Crops: [pro-cta-default.png](components/crops/pro-cta-default.png), [pro-cta-hover.png](components/crops/pro-cta-hover.png), [pro-cta-focus-visible.png](components/crops/pro-cta-focus-visible.png).

## Account boundary

These sit on the sign-up and sign-in cards. Nothing was typed and nothing was submitted.

### Email field

528px by 48px on /sign-up, 12px radius, 1px `#e5e7eb` border at rest. Focus was applied; the ring lives on the field wrapper more than on the input's own outline. Crop: [signup-email-default.png](components/crops/signup-email-default.png), [signup-email-focused.png](components/crops/signup-email-focused.png).

The id.kraken.com field is 426px by 48px. Crop: [signin-email-default.png](components/crops/signin-email-default.png).

### Password field

At rest only. Crop: [signin-password-default.png](components/crops/signin-password-default.png).

### Continue

Purple `#7132f5`, 46 to 52px tall, radius 12px, white label. Pressed (forced `:active`) is `#5b1ecf`. Crops: [signup-continue-default.png](components/crops/signup-continue-default.png), [signin-continue-default.png](components/crops/signin-continue-default.png), [signin-continue-hover.png](components/crops/signin-continue-hover.png).

## Prices

### Search field

A text input on /prices, focused and not filled. Crop: [prices-search-default.png](components/crops/prices-search-default.png).

### Price table

The home and /prices pages paint a market table: asset, price, 24h change, market cap. Positive change uses the positive solid green; negative uses `#d11d45`. The row itself was not cropped as its own element on this pass. See [prices-light-default.png](screenshots/prices-light-default.png).

## Mobile

The 390 header is 64px. The hero title wraps to 80px. Crops: [m-header-default.png](components/crops/m-header-default.png), [m-hero-default.png](components/crops/m-hero-default.png). The open nav menu is [mobile-home-light-menu-open.png](screenshots/mobile-home-light-menu-open.png). The Search button opens a trade overlay instead.

## Footer

White band, 1440 by 943 on the desktop home, primary text `#101114`. Crop: [footer-default.png](components/crops/footer-default.png).

## Gaps

- Select, checkbox, radio, switch, tooltip, toast, avatar and badge were not mounted as their own controls on the public pages. Status colour is painted as price-change text, not as a badge component.
- Text area, toast, tooltip, avatar, badge, checkbox, radio, switch and a destructive confirmation do not appear as their own controls signed out. The search overlay is [home-light-search-open.png](screenshots/home-light-search-open.png). The phone nav menu is [mobile-home-light-menu-open.png](screenshots/mobile-home-light-menu-open.png).
- Disabled, loading and error states were not offered. The sign-up form was not submitted, so validation never appeared.
- Pressed states are DevTools-forced (`CSS.forcePseudoState`). A script-applied mousedown style, if any, was not captured.
- The search icon button, market tabs and price row selectors missed on the measurement pass. Those states are in the page screenshots.
