# Components

Public signed-out chrome only. Values are token names. The computed readings are in [raw/measurements.md](raw/measurements.md). No crops: `preview_snapshot` returned "The browser is not producing screenshot frames."

## Button

Toolbar Sign In (`.web-toolbar__signin-button`). Blue face, white label, pill radius, 22 by 70 px.

| State | Evidence |
|---|---|
| Default | Measured on the marketing home and the store. `light.component.button-signin-bg`, `light.component.button-signin-text`, `core.radius.pill`, padding `0px 6px` |
| Hover, focus, pressed, loading | Not captured. No frame was available to hover, and focus was not forced |
| Disabled | Not this control. The sign-in page Next button is the disabled-looking control |

Marketing CTA (`a.cta__primary`, text "Find out more"). Transparent face, radius `core.radius.cta` (28px), padding 2px, height 38px, label 14px / 400, transition `0.1s all`. On a dark hero the label is `light.color.on-dark`. On a light plate the label is `light.color.link`. The fill is not a solid button colour.

Sign-in Next (`#signin-entrance-button`). Grey face `light.component.button-next-bg`, black label, radius `core.radius.pill`, padding `0px 10px`, height 34px, weight 700. The class list included `psw-is-disabled` while the email field was empty. Not clicked.

Create an Account. Fill `light.color.create-fill`, 1px border `light.color.create-border`, white label, radius `core.radius.pill`, height 34px, weight 700. Not clicked. This is the signup wall.

## Link

Light-plate marketing link colour is `light.color.link` (`rgb(0, 104, 189)`), the same blue as a light-plate CTA label. Sign-in links (About Sony Account, Trouble Signing In?) are `light.color.signin-link` at 14px. Hover and visited were not measured.

Nav items (Store, PS5, Games, PS Plus, Accessories, News) are buttons at 11.375px, weight 500, colour `light.color.ink`. Height of the bar is `core.spacing.nav-height`.

## Text field

Sign-in email (`#signin-entrance-input-signinId`, type email). The painted box is the parent: 1px solid `light.border.field`, radius `core.radius.2`, 38 by 422 px. The input itself is transparent, padding `6px 6px 6px 10px`, 16px, white text. Label "Sign-In ID (Email Address)" is white, 14px, weight 400. Empty. Nothing typed. Error, filled, and focus rings were not produced.

A password input was in the DOM at 20px tall and was not the visible step. It was not filled.

## Tabs

Store section tabs (Latest, Collections, Deals, Subscriptions, Browse). Active Latest: fill `light.color.tab-active`, black text, radius `core.radius.4`, padding `core.spacing.tab-y` `core.spacing.tab-x`, height 29px, weight 500, 2px transparent border. Inactive tabs share the radius and padding with a transparent face.

## Badge

Store discount (`-50%`). Face `light.component.badge-bg`, white label, weight 700, 12.25px, padding 4px, radius `core.radius.1`, height 23px.

## Card

Store product tile (`.psw-product-tile`). 313 by 261 px, radius 0, shadow none, text `light.color.store-ink`. Price line 14px / 19.6px. No add-to-bag control was used.

## Icon button

Search (`.shared-nav-icon--search`) is 59 by 21 px, colour `light.color.ink`, weight 500. The PlayStation home mark link is 53 by 50 px. No SVG set was lifted.

## Text area, select, checkbox, radio, switch, menu, tooltip, dialog, toast, table, avatar

Not present on the signed-out pages that were opened, or present only inside the signup flow that was not entered.

The OneTrust cookie banner was on the marketing home (Accept, Decline, Settings). Decline was clicked so the banner computed `display: none`. Its own colours were not measured before that click.

## Gaps

- Hover, focus-visible, pressed, loading, and error states.
- Signup form after Create an Account. Recorded as a wall, not entered. No email, phone, card, or identity field was submitted.
- Password step. Next was not clicked, so the password step was not opened.
- Site-wide dark theme. `color-scheme` computed to `normal`. Dark classes are section banners (hero, footer), not a second theme set.
- Crops and screenshots. Screenshot frames never arrived.
- 1440 and 390 widths. The preview pane was 1169 by 731.
