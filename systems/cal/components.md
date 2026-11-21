# Cal.com components

Public marketing and account-entry surfaces, measured signed out on 2026-11-21. Crops are in [components/crops/](components/crops). Values are token names where a token matches the computed colour, otherwise the computed value with its source.

The signed-in product (bookings, event types, availability, settings) was not entered. Login and signup URLs were opened only to photograph the wall. No email was typed. No password was typed. Google, Microsoft and SAML were not clicked.

## Button

The primary action is the ink pill labelled Get started. Measured on the home nav and again on pricing.

| State | Fill | Text | Radius | Height |
|---|---|---|---|---|
| default | `light.accent` #242424 | `light.on-accent` #ffffff | 12px `core.radius.cta` | 36px |
| hover | ink at 90% (computed oklab) | #ffffff | 12px | 36px |
| focus-visible | same fill | #ffffff | 12px | ring colour `light.focus` |
| pressed | forced `:active`, no fill change read | #ffffff | 12px | 36px |

Crops: [nav-cta-default.png](components/crops/nav-cta-default.png), [nav-cta-hover.png](components/crops/nav-cta-hover.png), [nav-cta-focus-visible.png](components/crops/nav-cta-focus-visible.png), [nav-cta-pressed.png](components/crops/nav-cta-pressed.png).

Disabled, loading and error were not present on the public controls that were measured.

## Link

Sign in is a quiet text button: no fill, `light.text` #242424, 14px medium, 10px radius, 36px tall. Hover adds a 4% ink wash. Pricing in the nav uses the same treatment.

Crops: [nav-signin-default.png](components/crops/nav-signin-default.png), [nav-link-default.png](components/crops/nav-link-default.png).

## Menu

Products, Use cases, AI, Features and Resources are buttons with `aria-expanded`. A click opens a dialog panel. The panel's links are 14px Cal Sans. The open Products menu is [screenshots/home-light-menu-products.png](../screenshots/home-light-menu-products.png). The phone drawer is [screenshots/mobile-home-light-menu.png](../screenshots/mobile-home-light-menu.png).

A menu item crop: [menu-link-default.png](components/crops/menu-link-default.png).

## Text field

The login email field on `https://app.cal.com/auth/login` is 364 by 30, 10px radius, fontSans, 14px. It was focused with the keyboard. Nothing was typed. Crop: [login-email-default.png](components/crops/login-email-default.png), [login-email-focus.png](components/crops/login-email-focus.png). The password field was photographed empty: [login-password-default.png](components/crops/login-password-default.png).

Text area, select, checkbox, radio and switch were not present on the measured public pages.

## Card

The login form is a 366 by 208 card. Crop: [login-card-default.png](components/crops/login-card-default.png). Pricing plan prices set 32px bold Cal Sans. Crop: [plan-price-default.png](components/crops/plan-price-default.png).

## Display and body

The home h1 is 80px / 86.4px Cal Sans 700, letter-spacing -0.8px, colour `light.text`. Crop: [display-default.png](components/crops/display-default.png). The first body paragraph is 20px / 28px, weight 500, colour about #6a6e78 (`light.muted` is the declared #676b75).

## OAuth row

The Google control on the login wall is a filled 36px row, 10px radius. It was not clicked. Crop: [oauth-google-default.png](components/crops/oauth-google-default.png).

## Shared values

| | |
|---|---|
| Radius | Nav pills 10px, primary CTA 12px, fields 10px. The Tailwind scale is `core.radius` (xs 2px through 3xl 22px), derived from `--radius` 0.625rem. |
| Focus | Declared `--ring` #9ca3af. Computed focus-visible outline on menu links is 1px of that ring. |
| Motion | Mega-menu class sets `duration-200` and `cubic-bezier(0.22, 1, 0.36, 1)` (`core.motion.ease-hp-fly`). |
| Type | Cal Sans for marketing. The auth card computes `fontSans`. |

## Gaps

| Component | Status |
|---|---|
| Icon button | Not measured as its own crop. The phone menu button is in the mobile menu screenshot. |
| Text area, select, checkbox, radio, switch | Not present on the captured public pages. |
| Tabs | Home has Web app / Cal Desktop / Slack / iMessage tabs. The Cal Desktop tab is [screenshots/home-light-tab-desktop.png](../screenshots/home-light-tab-desktop.png). Per-state values were not read. |
| Tooltip | Not captured. |
| Dialog | The mega-menu is a dialog. A destructive confirmation was not present. |
| Toast | Not present on the public pages. |
| Table, list row, avatar, badge | Marketing cards stand in for list rows. A data table lives behind sign-in. Not captured. |
| Loading, error, disabled, selected | Not present on the measured public controls. |
