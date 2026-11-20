# Components

Controls that were on the public pages. Crops are cut from the 2x screenshots. Values are token names.

## Button

The hero primary is a coral rectangle with no radius.

| State | Evidence |
|---|---|
| Accent, default | [components/crops/button-accent-default.png](components/crops/button-accent-default.png). Fill `light.action.accent`, text `light.text.on-accent`, radius `core.radius.none`, type `core.typography.button-hero`. |
| Ghost, default | [components/crops/button-ghost-default.png](components/crops/button-ghost-default.png). 1px `light.border.default`, transparent fill. |
| Outline, nav | [components/crops/button-outline-default.png](components/crops/button-outline-default.png). 13px, weight 700, uppercase, padding 6.9px 20px. |
| Plan | Fill `light.action.plan`, radius `core.radius.pill-plan`, 2px white border. On the pricing screenshot. |
| Sign-in | Fill `core.color.sign-button`, radius `core.radius.pill`. The login page was measured and not screenshotted. |
| Hover, pressed, disabled, loading | Not captured. The sheet declares `.ts-btn:hover` as `#FEF9F6`. Marketing hover was not forced. |

## Link

Nav links are 13px, weight 700, uppercase, letter-spacing 0.5px. [components/crops/nav-links-default.png](components/crops/nav-links-default.png).

Focus on the marketing Sign up control is a 3px outline, `light.focus.ring`, offset 4px. Hover colour was not forced.

## Text field

Sign-in email and password fields: 24px TildaSans, letter-spacing 1px, height 53px, 1px white underline, white text. Labels are 16px black. The form was not submitted. A validation error was not shown. The error block is declared (black fill, white text) and was `display: none`.

## Tabs

Billing period on pricing. Active is `#222222` at weight 500 with a black underline. Idle is `#777777` at weight 400. [components/crops/tabs-billing-default.png](components/crops/tabs-billing-default.png).

## Card

Plan card: 3px black border, padding 45px 30px, radius 0, transparent fill. [components/crops/card-plan-default.png](components/crops/card-plan-default.png).

## Cookie banner

White panel, 398 by 184. Accept all and Reject all are `#0A0A0A` with white 12px type, radius 0. Dismissed with Reject all before the screenshots. Settings panel was not opened.

## Not on these pages

Text area, select, checkbox, radio, switch, menu, tooltip, dialog, toast, table row, avatar, badge, icon button. The pricing comparison table header was measured (`#333333` with white 20px type) and is below the fold of the viewport shot.
