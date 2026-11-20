# Components

Public signed-out chrome on pinterest.com, measured 19 November 2026. Values are token names from [tokens.json](tokens.json). Crops in [components/crops/](components/crops/) are reconstructions of the measured controls. The preview browser returned "The browser is not producing screenshot frames".

## Button

Primary. Log in, Join Pinterest for free, and Continue.

| Property | Token |
|---|---|
| Fill | `light.background.action` |
| Label | `light.component.button.text` |
| Radius | `light.component.button.radius` |
| Height | `light.component.button.height` |
| Padding | 8px 16px, from `core.spacing.200` and `core.spacing.400` |

Secondary. Sign up, and I already have an account. Fill `light.component.button-secondary.background`, label `light.component.button-secondary.text`, same radius and height.

The button element computed `color: #000000`. The white primary label is `light.component.button.text`, the Gestalt token, not the button's own computed color.

States. Default was on the page. Hover (`light.background.action-hover`) and pressed (`light.background.action-pressed`) are declared Gestalt tokens. A live pointer hover was not captured. Disabled, loading, and selected were not on these pages.

## Link

Explore is a text button with a transparent fill and `light.text.secondary`. Forgot password? and the footer policy link use `light.text.link` at 14px / 500, with no underline.

## Text field

Email, password, and birthday on the homepage signup wall.

| Property | Token |
|---|---|
| Border | `light.border.stroke`, 1px solid |
| Radius | `light.component.field.radius` |
| Height | `light.component.field.height` (56px on the homepage; 63px on /ideas/) |
| Type | `core.typography.ui` |
| Placeholder | `light.text.placeholder` |

The form was not submitted. Error, disabled, and focus-visible were not shown. Focus colour is the declared token `light.border.focus`.

## Search

The homepage search shell is `light.component.search.background`, radius `light.component.search.radius`, height `light.component.search.height`. At 1440 CSS px it was 619px wide. At 390 CSS px the input width computed to 0.

## Card

Idea-card anchors on the homepage computed radius `light.component.card.radius` (8px). Images inside those cards computed radius 0.

## Header

Height `light.component.header.height` (80px) at 1440 and at 390. At 390 the Explore, About, Log in, and Sign up controls still sat past the viewport edge.

## Footer

Homepage footer computed background `light.background.inverse`.

## Gaps

- Icon button, text area, select, checkbox, radio, switch, tabs, menu, tooltip, dialog, toast, list row, table, avatar, and badge were not shown on the public pages. Gestalt declares tokens for several of these. They were not measured on a control.
- Hover, pressed, focus-visible, disabled, loading, and error states were not forced.
- No crops. The preview browser did not produce screenshot frames.
