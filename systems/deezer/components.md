# Deezer components

Crops are cut from the 2026-11-21 public captures, then quantised. Values are token names from [tokens.json](../tokens.json).

| Component | States captured | Crop | Tokens |
|---|---|---|---|
| Button, marketing primary | default | [button-signup-default.png](crops/button-signup-default.png) | `light.background.accent`, `light.text.onAccent`, `core.radius.marketingButton`, `core.size.controlS` |
| Button, marketing ghost | default | [button-login-default.png](crops/button-login-default.png) | `light.border.login`, `light.text.onHeader` |
| Button, login submit | default | [button-login-submit.png](crops/button-login-submit.png) | `dark.background.accent`, `dark.text.onAccent`, `core.radius.field`, `core.size.loginSubmit` |
| Text field | empty email, empty password | [text-field-email.png](crops/text-field-email.png), [text-field-password.png](crops/text-field-password.png) | `dark.background.raised`, `core.radius.field`, `core.size.field` |
| Search field | default, focused (no text typed) | [search-field-default.png](crops/search-field-default.png), [search-field-focus.png](crops/search-field-focus.png) | `dark.background.raised`, `core.radius.field` |
| Card | channel tile | [card-channel.png](crops/card-channel.png) | `dark.background.surface` |
| Banner | signed-out signup strip | [banner-signup.png](crops/banner-signup.png) | marketing pale purple, observed |
| Player bar | default, paused | [player-bar-default.png](crops/player-bar-default.png) | `dark.background.page`, play uses `dark.background.accent` |
| Dialog | cookie notice | [dialog-cookie.png](crops/dialog-cookie.png) | GDPR banner, light surface |
| Drawer | phone nav open | [drawer-phone-menu.png](crops/drawer-phone-menu.png) | `dark.background.page`, `dark.text.primary` |
| Display | marketing hero | [display-hero.png](crops/display-hero.png) | `core.fontFamily.brand`, `core.fontSize.marketingHero` |

## Gaps

- Hover, pressed, disabled, loading and error states of buttons were not captured. Tempo declares hover and pressed accent fills (`dark.background.accentHover`, `dark.background.accentPressed`) but those states were not held on screen.
- No text area, select (opened), checkbox, radio, switch, tabs, tooltip, toast, table, avatar or badge was measured as a component. The marketing language control is a native `select`; focusing it did not open a styled menu.
- The cookie dialog crop is the visible notice after load. Accept, Refuse and Preferences were not clicked.
- Icon buttons in the player (play, next, shuffle, volume) are in the player-bar crop. Individual icon SVGs were not extracted.
