# Components

Public Pinterest, signed out, 2026-11-21. Crops are from the 1440×900 captures unless the name says mobile. Values are Gestalt tokens from [tokens.json](tokens.json). States that were not painted are Not captured.

| Component | States captured | Crop | Tokens |
|---|---|---|---|
| Button, primary | default | [button-primary-default](components/crops/button-primary-default.png) | `light.background.accent` #e60023, `light.text.on-accent` #fff, radius `core.radius.400` 16px, height 48px measured |
| Button, secondary | default | [button-secondary-default](components/crops/button-secondary-default.png) | `light.background.surface` #e5e5e0, text #000, radius 16px |
| Button, login (header, red) | default | [button-login-default](components/crops/button-login-default.png) | same primary fill |
| Button, signup (header, gray) | default | [button-signup-default](components/crops/button-signup-default.png) | same secondary fill |
| Button, primary, phone | default | [button-primary-mobile-default](components/crops/button-primary-mobile-default.png) | same primary fill, full width on the 390 page |
| Icon button | default (share) | [icon-button-share-default](components/crops/icon-button-share-default.png) | white circle over a pin, `core.elevation.floating` |
| Link | default (Explore) | [link-explore-default](components/crops/link-explore-default.png) | text #211922 measured on the header link, weight 400, 12px in the header |
| Text field | default (search), default (help search), login email in the dialog | [search-field-default](components/crops/search-field-default.png), [text-field-help-default](components/crops/text-field-help-default.png), [dialog-login-default](components/crops/dialog-login-default.png) | search fill is the secondary gray, pill radius. Help search is a white pill with a gray border. Login email shows a blue focus ring (`light.border.focus` #435ee5) because the field was focused when the dialog opened. Nothing was typed. |
| Text area | not present | | No public page showed a multi-line field. |
| Select | not present | | No public select. |
| Checkbox, radio, switch | not present | | None on the signed-out pages that loaded. Gestalt declares `--comp-checkbox-*`, `--comp-radiobutton-*` and `--comp-switch-*` in CSS. Those component values were not measured on an element. |
| Tabs | default, selected (All) | [tabs-default](components/crops/tabs-default.png) | Selected tab is black text with a 2px underline. Unselected is the same black, no underline. |
| Menu | not captured | | The header caret next to Sign up was not opened. Opening it was not required to map the tree, and it may be an account menu. |
| Tooltip | not present | | None surfaced. |
| Dialog | default (login) | [dialog-login-default](components/crops/dialog-login-default.png) | White sheet, radius about 32px (`core.radius.800`), floating shadow. Email and password fields empty. Google and QR were not clicked. |
| Toast | not present | | None surfaced. |
| Card | default (board) | [card-board-default](components/crops/card-board-default.png) | Photo collage, radius about 16px, title 16px/700, meta in gray. |
| List row | not present as a separate component | | Board pages use a pin grid, not a list row. |
| Table | not present | | None on the product pages. Policy pages are legal prose. |
| Avatar | default | [avatar-pinterest-default](components/crops/avatar-pinterest-default.png) | 32px red Pin mark plus the name and a verified check. The name is the product's published account. |
| Badge | observed on the board card | [card-board-default](components/crops/card-board-default.png) | Verified check in `light.background.accent`. No separate badge crop. |

## Shared values

Focus on the login email field is a 2px blue ring, `light.border.focus` #435ee5, with a white inner ring `light.border.focus-inner` #fff. Hover and pressed fills are declared (`light.background.accent-hover` #cc001f, `light.background.accent-pressed` #b2001b) and were not painted: a hover screenshot of Join matched the default frame. Disabled, loading and error were not shown.

Control height on the header and hero buttons measured 48px. Icon size of the share control is about 48px. The focus ring width is Not captured as a length beyond the colour tokens.

## Gaps

- Hover, focus-visible, pressed, disabled, loading and error were not captured as separate crops. The hover and focus screenshots did not differ from default.
- No text was typed into a field, so filled and validation states are Not captured.
- Signed-in components (save button, pin close-up, board create, toast after save) are behind the login wall.
