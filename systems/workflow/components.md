# Components

Controls measured on the public marketing site on 2026-11-19. Values are token names. The signed-in app was a loading screen, so app controls are gaps except where a marketing demo showed one.

## Button

Quiet actions use [light.button.secondary](tokens.json) (`#f6f6f6`) with [light.text.primary](tokens.json), 8px radius, 8px 16px padding, 40px height, Inter 14px.

![Try now](components/crops/button-secondary-default.png)

Ink actions on the pricing page use [light.button.dark](tokens.json) with [light.text.on-invert](tokens.json), the same radius and padding. One trial button computed 37px tall. Hover, pressed, disabled and loading were not captured.

## Link

Nav links are Inter 14px, [light.text.primary](tokens.json), no underline. The skip link is ink on `#f6f6f6`, 8px radius, 44px tall. `a:focus-visible` declares a 2px outline in [light.border.focus](tokens.json), offset 2px. A live focused element was not measured.

## Tabs

Home page media tabs are 48px tall, Inter 14px. The current tab is [light.text.primary](tokens.json) with an 8px radius. Resting tabs are [light.text.secondary](tokens.json) and a 0 radius.

## Chip

Feature jump links on `/features` are 32px tall, 8px 16px padding, 9999px radius, 1px border in [light.border.default](tokens.json).

## Badge

The marketing demo's Approve control is `#e9f6ee` on `#547e69`, 5px radius, 32px tall. The "approved" label in the same demo is 4px radius and 25px tall. These are demo chrome, not the signed-in app.

## Switch

The marketing demo shows an on switch, 42 by 24px, 24px radius, `#60886f`. The pricing yearly toggle is a separate control: 28 by 16px, 9999px radius, ink track, 13px white dot. Off, disabled and focus were not captured.

## Card

Feature sections sit on white. Comment cards in the demo use `rgba(26, 26, 26, 0.08) 0px 8px 16px`. Card padding was not isolated from the section.

## Gaps

Icon button, text field, text area, select, checkbox, radio, menu, tooltip, dialog, toast, list row, table and avatar were not on the marketing pages that were opened. The app at `app.workflow.design` showed a loading mark and no form. A banner in the marketing DOM says the app is offline for a planned upgrade. No email was entered.
