# Components

Public Buy Me a Coffee, signed out, 2026-11-21. Values are token names from [tokens.json](tokens.json). Crops are in [components/crops/](components/crops). States that need a signed-in dashboard are in Gaps.

## Button

Yellow pill. Header Sign up and the homepage Start my page.

| State | Fill | Text | Radius | Height |
|---|---|---|---|---|
| default | `light.color.accent` | `light.color.on-accent` | `core.radius.pill` | `light.component.button.height` |
| hover | `core.color.brand.yellow` at 80% (`hover:bg-yellow/80`) | same | same | same |
| focus-visible | Not captured as a separate crop | | | |
| pressed | Not captured. CDP press was not run on a link that navigates to signup. | | | |
| disabled | Not present on the public header | | | |

## Link

Nav links (FAQ, Wall of love, Log in) use `core.font.family.medium` at 16px, colour `light.color.text`. Hover fills a quiet wash (`core.color.neutral.wash`) via `btn-hover-bg`.

## Text field

Login email field is visible on [screenshots/login-light-auth-wall.png](screenshots/login-light-auth-wall.png). Placeholder "Email". Not typed into. Signup name field placeholder "yourname". Not typed into. Search creators field lives in a modal. Not submitted.

| State | Notes |
|---|---|
| default | Login email, empty |
| focused | Not captured. Focusing would be safe, but the capture stopped at the auth wall without interacting. |
| filled | Not captured. No text was typed. |
| error | Not present without a submit |

## Menu

Apps and Resources are hover menus under `#bmc-header`. Panel is white, `core.radius.md`, `core.shadow.menu`.

| State | Where |
|---|---|
| closed | Header resting |
| open | [screenshots/home-light-apps-menu.png](screenshots/home-light-apps-menu.png), [screenshots/home-light-resources-menu.png](screenshots/home-light-resources-menu.png) |
| phone drawer | [screenshots/mobile-home-light-menu-open.png](screenshots/mobile-home-light-menu-open.png) |

## Dialog

Search creators opens `.bmc-modal` on the homepage. Close icon, no submit. See [screenshots/home-light-search-open.png](screenshots/home-light-search-open.png).

## Card

Homepage creator cards and the support card on a public creator page. Radius `core.radius.card` (36px) on the shop specimen in the bundle. Page background `light.color.page`.

## Radio

Public creator page coffee quantity: 1, 3, 5, 10, plus a number field. Selected state: [screenshots/creator-light-quantity-selected.png](screenshots/creator-light-quantity-selected.png). Not submitted.

## Checkbox

Public creator page: "Make this message private" and "Make this monthly". Default only. Not toggled, because either one changes a payment form.

## Tabs

Creator page: Home, Membership, Wishlist. Three pages, not an in-page tab widget. Blog is a separate shell.

## Avatar

Creator cards and the public page show a round avatar (`rounded-full`, 48px on the card specimen). Published photos. Not extracted as assets.

## Badge

Supporter counts sit on creator cards as plain text, not a separate badge component.

## Not present on the public site

Text area exists on the creator support form ("Say something nice...") and was not filled. Select, switch, tooltip, toast, table, and icon button (except the phone menu and modal close) were not a distinct public component. Loading and error states need a submit, which was not done.

## Gaps

- Signed-in dashboard, payouts, shop admin, messages, settings: behind [https://buymeacoffee.com/login](https://buymeacoffee.com/login). Stopped.
- Signup form fields: behind [https://buymeacoffee.com/signup](https://buymeacoffee.com/signup). Not filled.
- Google, Facebook, Apple, Twitter buttons on login: not clicked.
- Dark theme: not offered.
- Focus-visible and pressed crops: not cut. The states are named here as Not captured.
- Help center (`help.buymeacoffee.com`) is a different shell and was not screenshotted.
