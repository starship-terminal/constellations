# Components

Public signed-out chrome only. Values are token names. The computed readings are in [raw/measurements.md](raw/measurements.md). No crops: the preview browser did not produce screenshot frames.

## Button

Marketing primary (`a.button-type-primary`). Black face, white label, pill radius, 48px tall.

| State | Evidence |
|---|---|
| Default | Measured on US home Learn More and SG home Sign Up. `light.component.button-primary-bg`, `light.component.button-primary-text`, `core.radius.pill`, `core.spacing.control` |
| Focus | Measured. 2px solid `light.color.focus`, offset 2px |
| Hover, pressed, disabled, loading | Not captured. Nothing was hovered through a painting frame, and no disabled control was on the page |

Login Next (`#btnNext`). Blue face `light.color.login-action`, white label, radius `core.radius.login-pill`, padding 12px 32px. Not submitted.

Login secondary (Passkey, Sign Up). Transparent face, 2px solid black border, same pill radius as Next, 48px tall.

Marketing secondary (`a.button-type-secondary`). Fill `light.color.secondary-fill`, black label, pill radius, 48px tall.

Cookie accept. Font PayPalOpen-Medium, 14px, weight 500, white at 70% opacity, 2px border `light.color.field-border`, pill radius. Not clicked.

## Link

Marketing link on a light plate: `light.color.link`, weight 700, 14px. On the navy plate: `light.color.link-on-navy`. Login link (Forgot email): `light.color.login-link`, pp-open-medium, 16px. Hover and visited were not measured.

## Text field

Login email (`#email`, type email, name `login_email`). White face, radius `core.radius.field`, padding 20px 12px 8px, 64 by 364 px. Label `light.color.login-label`. Focus: 2px solid `light.color.login-focus` plus a white 2px ring, border `light.color.field-border`. Empty. Nothing typed. Error, disabled, and filled states were not produced.

## Text area, select, checkbox, radio, switch, tabs, menu, tooltip, dialog, toast, table, avatar, badge

Not present on the signed-out pages that were opened, or present only as a signup choice that was not activated.

The account-selection page shows two cards (Personal, Business) with radius `core.radius.card` and padding `core.spacing.card`. They are a choice of account type, not a form radio that was activated. Get Started links to `https://www.paypal.com/welcome/signup` and was not followed.

Business and Personal on the SG hero are in-page tabs (`?tab=business`, `?tab=personal`). The active tab's text colour matched body ink. A selected-state fill was not isolated from the hero.

## Icon button

Cookie close: 48px, radius 50%, colour `light.color.muted`. The PayPal wordmark SVG in the hero measured 24 by 24 with `fill="none"` on the root. No icon set was lifted.

## Gaps

- Hover, pressed, disabled, loading, and error states.
- Signup form after Get Started. Recorded as a wall, not entered.
- Password step. The email step was not submitted, so it never appeared.
- Dark theme. `color-scheme` computed to `normal`. No toggle was on these pages.
- Crops. Screenshot frames never arrived.
