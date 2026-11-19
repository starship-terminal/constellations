# Components

Signed-out Threads chrome, measured on 2026-11-19. Token names point at [tokens.json](tokens.json). Crops are from the headless shots. The login-card crop is under the signup dialog scrim, so its pixels are darker than the computed fill.

## Login card

The home page card reads "Log in or sign up for Threads". Computed box 337 by 289, fill `color.background.login-card` (`#1e1e1e` dark, `#f5f5f5` light), radius `radius.login-card` (24 px), padding 32 px 24 px 28 px, border 0.5 px solid `color.border.line`. Title is `typography.card-title` (20 px / 25 px, weight 700). Body copy is `typography.body` in `color.text.secondary`.

Crop: [components/crops/card-login-default.png](components/crops/card-login-default.png). The scrim darkens this crop. Use the token, not a pixel sample from the crop.

## Continue with Instagram

On the login card the control is 288 by 80, fill `color.background.primary` (`#101010` in dark), radius `radius.instagram-wall` (16 px), padding 28 px, label `typography.button`.

In the signup dialog and on `/login` the same label sits in a wider control: 408 by 94 in the dialog, 370 by 94 on `/login`, radius `radius.instagram-dialog` (20 px), border 0.5 px solid `color.border.line`. A focus ring was observed on the dialog instance: `shadow.focus` (`0 0 0 2px #ffffff, 0 0 0 4px #1877F2`).

Crop: [components/crops/button-instagram-default.png](components/crops/button-instagram-default.png).

This control starts Instagram login. It was not followed.

## Log in button

On `/login`, 370 by 56, radius `radius.login-field` (18 px), padding 16 px, weight 600, label 15 px. Dark face is `color.control.button-background` `#ffffff` with `color.control.button-text` `#101010`. Light inverts that: black face, white text.

Crops: [components/crops/button-primary-default.png](components/crops/button-primary-default.png), [components/crops/button-primary-light.png](components/crops/button-primary-light.png).

The declared Facebook primary (`#2374E1` / `#1B74E4`, radius 6 px) is not this button. The button was not pressed.

## Text field

Username and password fields on `/login` are 370 by 54, fill `color.background.input`, border 0.5 px solid `color.border.line`, radius 18 px, padding 16 px. The font computes to `font.family.default` (Helvetica, Arial, sans-serif) at 15 px. Placeholder colour is `color.text.secondary` (`#777777` in dark), not the declared `#8A8D91` placeholder token, which is stored as `color.text.placeholder`.

Placeholder text is "Username, phone or email" and "Password". Nothing was typed.

Crops: [components/crops/text-field-default.png](components/crops/text-field-default.png), [components/crops/text-field-password.png](components/crops/text-field-password.png).

## Muted link

"Forgot password?" and "Log in with username instead" compute to 15 px in `color.text.secondary`. Footer legal links are 12 px / 16.8 px in the same colour, and they leave threads.com for help.instagram.com.

Crop: [components/crops/link-muted-default.png](components/crops/link-muted-default.png).

## Nav pill

The signed-out home column shows a Home pill. The crop is the selected row from the dark home shot. Declared side-nav widths are `size.nav-expanded` 230 px and `size.nav-collapsed` 68 px. The crop is the row, not a measurement of the collapsed state.

Crop: [components/crops/nav-item-selected.png](components/crops/nav-item-selected.png).

## Signup dialog

"Say more with Threads". Panel fill `color.background.primary`, radius 16 px, padding 48 px 56 px 56 px, about 520 px wide. Headline is `typography.dialog-title` (32 px / 44.8 px, weight 800). The declared `--system-32-line-height` is 40 px. The measured headline is 44.8 px, and the token uses the measured line height.

Crop: [components/crops/dialog-signup-default.png](components/crops/dialog-signup-default.png).

## Shared values

| Role | Token | Dark | Light |
|---|---|---|---|
| Page | `color.background.page` | `#101010` | `#ffffff` |
| Login card | `color.background.login-card` | `#1e1e1e` | `#f5f5f5` |
| Text | `color.text.primary` | `#f3f5f7` | `#000000` |
| Muted text | `color.text.secondary` | `#777777` | `#999999` |
| Login button face | `color.control.button-background` | `#ffffff` | `#000000` |
| Hairline | `color.border.line` | `rgba(243, 245, 247, 0.15)` | `rgba(0, 0, 0, 0.15)` |
| Focus | `shadow.focus` | `0 0 0 2px #ffffff, 0 0 0 4px #1877F2` | same |

## Gaps

- Signup was not completed. No account, no Instagram session, no phone number.
- Pressed, error, disabled, and loading were not provoked. A press submits or starts SSO.
- Hover was not measured as its own state. `color.background.hover` is the declared custom property.
- Toast colours are declared (`--toast-*`) and were not seen painted. They are not tokenised.
- Phone-width light theme was not shot.
- Reduced motion was not emulated. The stylesheet has about 20 `prefers-reduced-motion` rules.
- Icons were not extracted. Meta artwork stays out of this package. See [docs/RIGHTS.md](../../docs/RIGHTS.md).
- The nav crop and the login-card crop are darkened by the dialog scrim. Sizes in this file come from computed style, not from those pixels.
