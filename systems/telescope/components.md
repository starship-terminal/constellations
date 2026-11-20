# Telescope components

Inventory of the signed-out surfaces measured on 2026-11-19. Values are token names. Screenshots of the marketing page are in [screenshots/](screenshots/). The preview browser could not produce frames, so there are no login screenshots and no crops.

| Component | Where | Values | States seen |
|---|---|---|---|
| Sign up button | Home footer, `.ui-button.-yellow` | `light.color.accent` fill, `light.color.ink` text, `core.size.button-height`, `core.typography.label` | Default. Hover and focus-visible are declared: fill becomes `light.color.button-hover`, text becomes `light.color.button-hover-ink`, over 400ms `core.motion.easing.out-swift`. Not hovered in this capture. |
| Login link | Home footer, `.signin-btn.t-mono` | `core.typography.label`, `light.color.ink`, no background, padding 9.5px 0 | Default only. |
| Email field | `/login` | `dark.color.page` fill, `dark.color.ink` text, 16px weight 500, `core.radius.auth`, height `core.size.auth-field-height`, focused border `dark.color.border` 1px | Empty and focused. Not filled. Disabled and error not shown. |
| Continue with Google | `/login` | `dark.color.surface` fill, `dark.color.ink` text, 14px weight 600, height 40px, radius 8px | Default. Not clicked. |
| Continue | `/login` | Same fill as Google, text `dark.color.disabled` while the field is empty | Disabled. Enabled state not shown. |
| Legal links | `/login` | 12px / 16px, `dark.color.muted`, underline | Default. |
| Wordmark | `/login` SVG | 156 by 32 px, color `dark.color.ink` | Default. |
| Product card | Home, `.ui-productCard` | `--ar: 4/3`. Saved state declares `--bg-color: #0671ff`. | Default cards in the public demo. Saved state not triggered. |
| Modal | `.tt-modal` present in the home DOM | Row border `light.color.border` (derived from color-mix). Close size `calc(var(--button-height) - .35rem)`. | Empty. No dialog text. |

## Gaps

- No hover, pressed, loading or error crop. Hover colours are declarations.
- No checkbox, radio, switch, select, textarea, tabs, menu, tooltip, toast, table or avatar component on the signed-out pages. The login panel shows a curator image (`cdn.telescope.fyi/login/avatar3`) but it was not cropped.
- No focus ring on the marketing button was computed. Login focus changes the field border to white and leaves `outline: rgba(0, 0, 0, 0) solid 2px`.
- Phone layout of the marketing page was requested at 390. Login at 390 was not captured.
- The preview browser returned "The browser is not producing screenshot frames", so this package has no element crops.
