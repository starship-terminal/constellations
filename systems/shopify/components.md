# Shopify components

Public marketing site, signed out, captured 2026-11-21 at 1440 and 390. Crops are the live controls. Values are token names from [tokens.json](tokens.json).

## Button

Primary action is a white pill on the black hero.

| State | Crop | Values |
|---|---|---|
| default | [button-primary-default](components/crops/button-primary-default.png) | fill `light.action.primary`, label `light.text.on-accent`, radius 9999px, padding 8px 20px, type 16px / 550 |
| hover | [button-primary-hover](components/crops/button-primary-hover.png) | fill moves to `light.action.primary-hover` (`#d4d4d8`) |
| focus-visible | Not captured | Keyboard focus ring was not read as a painted outline on this control |
| pressed | Not captured | |
| disabled | Not present | No disabled primary on the public home header |
| loading | Not present | |

On the phone drawer, Log in is an outlined pill and Start for free is the white pill. See [mobile-home-light-menu](screenshots/mobile-home-light-menu.png).

## Link

Header Log in is white, 16px, no underline until hover.

| State | Crop |
|---|---|
| default | [link-login-default](components/crops/link-login-default.png) |
| hover | [link-login-hover](components/crops/link-login-hover.png) |

Nav links (Pricing, Enterprise) sit in the 72px header. [nav-link-default](components/crops/nav-link-default.png).

## Icon button

The region dialog's close control. [icon-button-default](components/crops/icon-button-default.png). The phone drawer uses an X of the same role. [mobile-home-light-menu](screenshots/mobile-home-light-menu.png).

## Menu

Why Shopify opens a mega menu of image cards on hover. [menu-open](components/crops/menu-open.png). Phone uses a full-screen drawer. [mobile-home-light-menu](screenshots/mobile-home-light-menu.png) and [mobile-home-light-products-menu](screenshots/mobile-home-light-products-menu.png).

## Dialog

Region and language. [dialog-open](components/crops/dialog-open.png). Page shot: [home-light-region-dialog](screenshots/home-light-region-dialog.png).

## Switch

Pricing yearly toggle. [switch-default](components/crops/switch-default.png), [switch-selected](components/crops/switch-selected.png). Page: [pricing-light-yearly](screenshots/pricing-light-yearly.png).

## Accordion

Pricing FAQ `summary`. [accordion-default](components/crops/accordion-default.png), [accordion-open](components/crops/accordion-open.png).

## Text field

Help Center search, light surface, not the marketing hero. [help-light-default](screenshots/help-light-default.png). The region dialog has two selects. No text was typed.

## Card

Plan cards on pricing. [pricing-light-default](screenshots/pricing-light-default.png). Theme cards on the theme store. [themes-light-default](screenshots/themes-light-default.png).

## Badge

Fall '26 Edition is a pill link in the header, not a status badge. [home-light-default](screenshots/home-light-default.png).

## Not present on the public marketing surface

Text area, checkbox, radio, tabs (beyond the pricing carousel dots), tooltip, toast, table, avatar, list row as an app row. The admin app that would show those is behind login.

## Gaps

- Focus-visible and pressed were not captured as distinct painted states. The primary hover is the only state change that was measured.
- Login and signup were not entered. `https://accounts.shopify.com/lookup` is the login wall.
- Dark theme is not a switch on the marketing site. Help Center is a separate light product.
- Icons are brand artwork and are not extracted (`docs/RIGHTS.md`).
