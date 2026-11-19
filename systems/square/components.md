# Components

Public signed-out chrome only. Values are token names. Readings are in [raw/measurements.md](raw/measurements.md). No crops: the preview browser did not produce screenshot frames.

## Button

Marketing primary (`a.Action--button`, Contact sales). Face is the `::before` of `.Action__content-wrapper`: `light.color.accent`, label `light.text.on-accent`, radius `core.radius.pill`, height `core.spacing.control`, padding 10px 20px, weight 500.

Marketing alt (`a.Action--button-alt`, Get started). Face `light.background.page`, label `light.color.accent`, same radius and height.

Login Continue (`market-button`). Face `light.text.login`, label white, radius `core.radius.login-pill`, height `core.spacing.login-control`, inner padding 12px 20px, weight 600. Not clicked.

Passkey (`market-button.sign-in-passkeys-button`). Face `light.background.passkey`, label `light.text.login`, same pill and height. Not clicked.

| State | Evidence |
|---|---|
| Default | Measured on home and login |
| Focus | Marketing focus token `light.color.focus` is `--accessibility-focus-outline-color`. Not painted on a focused button in this capture |
| Hover, pressed, disabled, loading | Not captured. Nothing was hovered through a painting frame |

## Link

Nav Sign up and Log in: Cash Sans 15px, white on the home header, padding 18px 10px, radius `core.radius.nav`. Log in points at `https://app.squareup.com/login?lang_code=en-us`.

Text action (`a.Action--text`, Learn more): `light.text.primary`, 16px, weight 400, content padding 0 0 3px.

Login Sign up (`market-link` shadow `a`): underline, weight 600, `light.text.login`, 16px, href `https://app.squareup.com/signup/en-US`. Not followed from the login page. The wall was opened by URL later and not filled.

## Text field

Login email or phone (`#mpui-combo-field-input` inside `market-input-text`). White, radius `core.radius.field`, height `core.spacing.field`, width 534.5px. Rest border is a 1px inset `light.border.field`. After `focus()` and two frames, the inset became 2px `light.text.login`. Value stayed empty. Nothing was typed.

Error border `#CC0023` and error text `#BF0020` are computed custom properties on the host. No error was painted. Disabled background `#f0f0f0` is declared and was not painted.

## Text area, select, checkbox, radio, switch, tabs, menu, tooltip, dialog, toast, table, avatar, badge

Not present on the pages that were measured, or present only inside the signup wall that was not filled. The signup page shows an agreement checkbox in the visible text. It was not activated.

## Icon button

Not isolated. The passkey control contains a 24px svg. No icon set was lifted.

## Gaps

- Hover, pressed, disabled, loading, and error states.
- Signup form. Recorded as a wall, not entered. It asks for email, password, and an agreement checkbox.
- Password step after Continue. Continue was not clicked.
- Dark theme. `color-scheme` computed to `normal`. Dark custom properties exist and were not painted.
- Crops. Screenshot frames never arrived.
