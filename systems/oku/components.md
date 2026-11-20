# Oku components

Public signed-out surface, measured on oku.club on 2026-11-21. Crops are from the 256-colour screenshots. Values are token names from [tokens.json](tokens.json).

## Button

The header Join control. 112×40, 8px radius, 14px Inter at weight 500, 24px horizontal padding.

| State | Crop | Values |
|---|---|---|
| default, light | [join-button-default.png](components/crops/join-button-default.png) | `light.component.button.background` #000000, `light.component.button.text` #ffffff, `core.radius.control` 8px, `core.shadow.button` |
| default, dark | [join-button-dark-default.png](components/crops/join-button-dark-default.png) | `dark.component.button.background` #e0e1e4, `dark.component.button.text` #131314 |
| hover | not captured as a colour change | computed background and color matched default |
| focus-visible | not captured as a ring | outline width 0px. Focus moved the button shadow blur from 4px to about 6px. |
| pressed, disabled, loading | not captured | not shown on the public surface |

Hero Join for free is the same fill at 54px tall and 15px type. See [hero-cta-default.png](components/crops/hero-cta-default.png).

## Sign in button

A quiet twin of Join: white fill, ink label, an inset 1px ring at `light.color.border`.

| State | Crop | Values |
|---|---|---|
| default | [sign-in-button-default.png](components/crops/sign-in-button-default.png) | `light.component.sign-in.background` #ffffff, `light.component.sign-in.text` #131314 |

## Link

Nav links are 16px Inter, no underline, no radius. Explore, Blog, Pricing, Twitter, Contact.

| State | Crop | Values |
|---|---|---|
| default | [nav-link-default.png](components/crops/nav-link-default.png) | `light.color.text-secondary` #131314 |
| hover | same colour | computed color stayed #000000 on hover, #e0e1e4 in dark |
| focus-visible | no ring | outline width 0px |

The inline "Sign in." under the hero is an underlined text link. Not a separate token.

## Text field

Shown only inside the signup dialog and on the sign-in wall. 384×46, 8px radius, 16px horizontal padding, 1px solid border.

| State | Crop | Values |
|---|---|---|
| empty | [text-field-default.png](components/crops/text-field-default.png) | `light.color.field-border` #d1d1d3, `core.size.field-height` 46px |
| filled, error | not captured | no field was typed into, no form was submitted |

## Dialog

Join opens a 480px panel, 20px radius, over an `rgba(0, 0, 0, 0.6)` scrim. The panel asks for email, username, and password. It was not filled.

| State | Crop | Values |
|---|---|---|
| open | [dialog-default.png](components/crops/dialog-default.png) | `light.component.dialog.background` #ffffff, `core.radius.dialog` 20px, `light.color.scrim` |

Dark paints the same panel at `dark.component.dialog.background` #131314. Screenshot: [home-dark-join-dialog.png](screenshots/home-dark-join-dialog.png).

## Menu

Phone only. The header button opens a full-screen list: Join, Sign in, Explore, Blog, Pricing, Twitter, Contact. Close is the same button, drawn as an ×.

| State | Crop |
|---|---|
| open | [menu-open-default.png](components/crops/menu-open-default.png) |

## Card, list row, tabs

Book covers, activity rows, and blog posts are lists of links, not a separate card component with its own fill. Book pages have Book Info, Reviews, and Highlights as text tabs. See [book-light-default.png](screenshots/book-light-default.png).

Pricing columns are 297px wide with no card fill or radius. The price figure is FabricSerifWeb at 39px (`core.font.size.price`).

## Display type

| Role | Crop | Values |
|---|---|---|
| hero | [hero-title-default.png](components/crops/hero-title-default.png) | FabricSerifWeb 48px, line-height 62.4px, letter-spacing -0.288px |
| pricing title | [pricing-h1-default.png](components/crops/pricing-h1-default.png) | same 48px display |
| book title | [book-title-default.png](components/crops/book-title-default.png) | FabricSerifWeb 24px, #131314 |

## Header

Fixed, 80px, transparent. [header-default.png](components/crops/header-default.png).

## Not present

Checkbox, radio, switch, select, text area, tooltip, toast, table, avatar as a component, badge, icon button with a name. Toastify CSS is loaded. No toast was shown.

## Gaps

- Signed-in library, collections editor, highlights editor, goals, and checkout were not opened.
- `/signin` is a wall. Screenshot [signin-light-wall.png](screenshots/signin-light-wall.png) shows empty fields. Nothing was typed.
- `/login` is the public 404, not a login form.
- Hover and focus did not paint a new colour. Pressed was not held.
- Section heading size (the 36px h2 below the fold) is not in tokens.json. The viewport readings did not include an h2.
- No icon SVG index. The wordmark is in the header crop.
