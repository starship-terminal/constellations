# Components

Public marketing controls on mymind.com, measured 2026-11-21. The signed-in app was not reached. Values are token names. A state that was not on screen is Not captured.

## Button

The filled control. Home "TRY IT OUT" is an ember pill (`.is-content`, radius 120px, height 45px) with white Nunito-SemiBold 15px label. Pricing "SIGN UP" is the same ember at radius 25px and height 50px. The header "Sign up" is this pill: white label on ember, sitting beside a blue "Log in" link.

| State | Evidence |
|---|---|
| default | [button-signup-default.png](components/crops/button-signup-default.png). Fill `light.accent.default`, text `light.text.on-accent`, radius `core.radius.pill` |
| hover | Home CTA fill did not change. Header Sign up link text went from `light.text.link` to black. Fill hover is Not captured as a separate colour |
| focus-visible | Not captured. Log in outline computed as `auto 0px` |
| pressed | Not captured |
| disabled | Not present on the public pages |
| loading | Not present |
| error | Not present |

## Link

Auth and nav links are Louize 20px in `light.text.link` (`#1573dd`), authored as `a { color:#1573dd }` in styles.css. They open a page or the auth wall. See [site-tree.md](site-tree.md).

| State | Evidence |
|---|---|
| default | [link-login-default.png](components/crops/link-login-default.png), [nav-default.png](components/crops/nav-default.png) |
| hover | Sign up text colour computed `rgb(0, 0, 0)` |
| focus-visible | Not captured as a painted ring |

## Menu

Phone only. `a[aria-label="Menu"]` opens an overlay on the same URL. What, Why, How, LOG IN, SIGN UP. Close returns to the page. [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png), crop [menu-button-default.png](components/crops/menu-button-default.png).

## Tabs

Pricing Monthly / Yearly is an in-page toggle. Both labels computed Nunito 20px / 600 in `#7e90a7` before a selection was forced. Selected fill was not read as a separate token. Mobile iOS / Android tabs on `/mobile` share fill `#ebebf1`.

## Card

Feature cards on the home page use flat pastel fills: `core.color.card-sand`, `card-blue`, `card-green`, `card-blush`, `card-peach`. Pricing plan cards are white, radius 22px (`core.radius.card`). No shadow was measured (`box-shadow: none` on the sampled cards).

## Display type

Home h1 is Avenir Book 140px / 119px, tracking -8.4px, ink `#000000`. [display-default.png](components/crops/display-default.png). Pricing h1 is Louize, computed 134.11px, colour `#2c3441`.

## Not present on the public surface

Text field, text area, select, checkbox, radio, switch, tooltip, dialog, toast, list row, table, avatar, badge, icon button. FAQ questions are headings, not accordions (`details` count 0, `button` count 0).

## Gaps

- Signed-in library, search, cards and settings: auth wall at https://access.mymind.com/signin. Headless Chromium received HTTP 403 from CloudFront. Not entered.
- Dark theme: not on the public site.
- Pressed, disabled, loading, error, focus ring width, elevation: Not captured.
- Status colours (success, warning, danger, info): not painted.
- WordPress `--wp--preset--*` colours are in styles.css and were not used by these pages. They are not tokens.
