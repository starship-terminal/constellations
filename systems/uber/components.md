# Components

Measured on the signed-out public pages on 2026-11-19. Token names point at [tokens.json](tokens.json).

## Button

Primary, rest, ride page, 1440 CSS pixels. "See prices" and "Next".

| Property | Value | Token |
| --- | --- | --- |
| Background | `#111111` | `light.component.button.primary.bg` |
| Text | `#fcfcfc` | `light.component.button.primary.text` |
| Radius | `8px` | `light.component.button.primary.radius` |
| Height | `48px` | `light.component.button.primary.height` |
| Font | UberMoveText 16px / 20px, weight 500 | `core.typography.body` is 16/24 regular. The button is medium and tighter |
| Padding | `14px 25px` | Not a spacing token |

Header pill, rest. "Ride", "Log in", "Help".

| Property | Value | Token |
| --- | --- | --- |
| Background | `#111111` | `light.component.button.nav.bg` |
| Text | `#fcfcfc` | `light.component.button.nav.text` |
| Radius | `999px` | `light.component.button.nav.radius` |
| Height | `36px` | `light.component.button.nav.height` |
| Padding | `10px 12px` | |
| Font | UberMoveText 14px / 16px, weight 500 | `core.typography.nav` |

Sign up pill, rest. White on the black header.

| Property | Value | Token |
| --- | --- | --- |
| Background | `#ffffff` | `light.component.button.signup.bg` |
| Text | `#000000` | `light.component.button.signup.text` |
| Radius | `999px` | `light.component.button.signup.radius` |

Drive page "Get started" is the inverse: white fill, dark text, 8px radius, on a black hero. See [screenshots/drive-light-default.png](screenshots/drive-light-default.png).

Hover, pressed, and loading were not held. The empty signup Continue uses `rgba(224, 224, 224, 0.6)`, which matches `--base-background-disabled`.

## Link

"See terms" is `#525252` (`--base-content-secondary`), UberMoveText 16px. "Learn more" on the ride page computed to `rgb(0, 0, 238)`, the browser default, on an unstyled anchor. That blue is not a Base token.

## Text field

Pickup and dropoff, ride page. The box, not the inner input, carries the fill.

| Property | Value | Token |
| --- | --- | --- |
| Background | `#f6f6f6` | `light.component.field.bg` (also `light.background.secondary`) |
| Text | `#111111` | `light.content.primary` |
| Radius | `8px` | `light.component.field.radius` |
| Height | `56px` | `light.component.field.height` |
| Font | UberMoveText 16px | |

The signup wall field is the same fill and radius, 48px tall, and draws a `2px solid rgb(0, 0, 0)` border while focused. No value was entered.

## Header

64px, `#000000`. Wordmark is UberMove 24px, white. See [screenshots/ride-light-default.png](screenshots/ride-light-default.png).

## Gaps

- Text area, select, checkbox, radio, switch, tabs, menu, tooltip, dialog, toast, card, list row, table, avatar, badge: not on the signed-out pages that were measured.
- Hover, focus-visible, pressed, and error states of the ride form: not captured.
- Signup and login past the phone-or-email wall: not entered. No phone, email, card, or ride.
- Phone width: the 390 reload was a reCAPTCHA interstitial and was discarded.
- Dark theme as a rendered page: tokens only.
