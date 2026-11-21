# Components

Public signed-out Instagram, measured on 2026-11-22. Crops are from the desktop captures at 1440x900. Dark crops use the same boxes on the dark captures. Values are token names from [tokens.json](tokens.json).

## Button

The login form's "Log in" control is a full-width pill. With both fields empty it paints the disabled wash (`light.color.button.primary.background.disabled`, `#b8cdff` in light), not the enabled blue (`light.color.button.primary.background`, `#4a5df9`). The enabled fill was not held, because filling the form was out of scope.

| State | Crop |
|---|---|
| Disabled (empty form) | [button-primary-login-light.png](components/crops/button-primary-login-light.png), [button-primary-login.png](components/crops/button-primary-login.png) |
| Nav pill, enabled | [button-login-pill-light.png](components/crops/button-login-pill-light.png), [button-login-pill.png](components/crops/button-login-pill.png) |
| Outline, "Create new account" | [button-outline-create-light.png](components/crops/button-outline-create-light.png), [button-outline-create.png](components/crops/button-outline-create.png) |
| Secondary, "Log in with Facebook" | [button-secondary-facebook-light.png](components/crops/button-secondary-facebook-light.png), [button-secondary-facebook.png](components/crops/button-secondary-facebook.png) |

Hover and pressed are declared as `--ig-colors-button-primary-background--hover` and `--pressed` and tokenised. They were not captured as screenshots: the enabled button was not pressed, and Facebook was not clicked.

## Text field

Two stacked fields on the login form. Radius `core.radius.input` (12px, from `--ig-input-border-radius`). Border `light.color.stroke`. Placeholder colour is the computed `rgb(104, 106, 110)` on the label, close to `light.color.input.text.and.icon.secondary`.

| State | Crop |
|---|---|
| Username, resting | [text-field-username-light.png](components/crops/text-field-username-light.png), [text-field-username.png](components/crops/text-field-username.png) |
| Password, resting | [text-field-password-light.png](components/crops/text-field-password-light.png), [text-field-password.png](components/crops/text-field-password.png) |

Focus-visible was attempted. The password field received focus and the crop showed no ring change, so that crop was not kept. Focus colour is tokenised as `light.color.focus.stroke` (`#a8a8a8`) from `--ig-focus-stroke`. Error and disabled field states were not shown.

## Link

"Forgot password?" is accent text, computed `rgb(65, 80, 247)` in light, which matches `light.color.colors.link.text` (`#4150f7`).

[link-forgot-light.png](components/crops/link-forgot-light.png), [link-forgot.png](components/crops/link-forgot.png)

## Tabs

The public profile uses icon tabs: Posts (selected, black underline), Reels, Tagged. Selected colour is `light.color.tab.underline.active`.

[tabs-profile-light.png](components/crops/tabs-profile-light.png), [tabs-profile.png](components/crops/tabs-profile.png)

## Not present on the public surface

Checkbox, radio, switch, text area, select (the language control is a native `select` in the footer, not a designed menu), tooltip, toast, table, badge as a component token beyond `--ig-badge`.

## Gaps

- Menu, dialog, and the language list were seen as controls in the site tree. The bio links dialog was opened and then excluded: it contained private handles. No dialog crop is kept.
- Icon button, avatar, card, list row, and chip are visible on the profile, popular, and locations screenshots. Element crops of those were not cut cleanly and are not in `components/crops/`.
- Loading, error (field), pressed, and hover screenshots were not captured. Error page copy is in [missing-light-default.png](screenshots/missing-light-default.png).
