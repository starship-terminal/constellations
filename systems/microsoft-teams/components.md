# Components

Public marketing controls on microsoft.com/microsoft-teams, measured signed out on 2026-11-19. Crops are from the live page. The signed-in Teams app was not opened.

## Button

The page action is `a.btn.btn--md`. Fill `#5d5bd4`, label `#ffffff`, 15px / 600 Segoe UI Variable Text, tracking -0.3px, 8px radius, padding 8px 16px, height 44px, 2px transparent border.

| State | What changed |
|---|---|
| default | [button-primary-default.png](components/crops/button-primary-default.png) |
| hover | fill `#5553c1` ([button-primary-hover.png](components/crops/button-primary-hover.png)) |
| focus | 3px dotted white outline, offset -6px ([button-primary-focus.png](components/crops/button-primary-focus.png)) |
| pressed | not captured; no pointer-down reading was taken |
| disabled | not present on the public pages |

The universal header uses a smaller control: 31px tall, 3px radius, 13px Segoe UI, padding 4px 8px. "Try for free" is filled `#5d5bd4`. "Sign in" and "Download Teams" are transparent with a 1px `#000000` border and `#262626` text. See [header-default.png](components/crops/header-default.png).

Pricing "Try for free" as a secondary page button is transparent, 2px `#333275` border, `#333275` text, 8px radius, 36px tall.

## Link

`a.link` "Learn more" is `#333275`, 14px / 600, no underline at rest. See [link-default.png](components/crops/link-default.png).

## Text field

The Ask Microsoft input is 64px tall, 8px radius, padding 20px 60px 20px 16px, 16px Segoe UI Variable Text, colour `#000000`, transparent background. See [field-default.png](components/crops/field-default.png) and [field-focus.png](components/crops/field-focus.png). The crop includes the field's "Ask now" and "No thanks" buttons because the input sits in that bar.

## Heading

Home h1 is Segoe UI Variable Display, 62px / 72px, weight 500, tracking -1.55px, colour `#0e1726`. See [heading-hero.png](components/crops/heading-hero.png). At 390px the same heading is 40px / 48px, tracking -1px.

## Not on the public surface

Text area, select, checkbox, radio, switch, tabs, menu (the header menus were not opened), tooltip, dialog, toast, table, avatar, badge, and list row were not present as product controls. The pricing page shows a pill audience switcher (Business / Individuals / Enterprise) and plan cards; those are marketing patterns, recorded in [patterns.md](patterns.md). The signed-in chat, meeting, and calling UI requires a Microsoft account and was not captured.
