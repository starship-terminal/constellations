# Outchat components

Measured on the Wayback replay of www.outchat.ai, 2026-11-19, at 1440x900 unless noted. Values are computed styles. Crops are pixels from that replay, not a live session.

## Button

Primary. Sign up, Make your AI chat, Try for free, Get started.

| Property | Value |
|---|---|
| Background | `#000000` `light.background.action` |
| Text | `#ffffff` `light.text.on-action` |
| Font | Aeonik Medium, 16px, weight 400 |
| Radius | 9999px `core.radius.pill` |
| Padding | 10px 20px on the hero button, 8px 16px on nav Sign up |
| Height | 46px hero, 42px nav |
| Hover | opacity 0.8, 100ms `cubic-bezier(0.4, 0, 0.2, 1)` |
| Focus | `outline: rgb(255, 255, 255) solid 3px`. Invisible on the white page |

![Primary](components/crops/button-primary.png)

![Sign up](components/crops/button-signup.png)

![Sign up hover](components/crops/button-signup-hover.png)

Quiet. Login.

| Property | Value |
|---|---|
| Background | `rgba(0, 0, 0, 0.05)` `light.background.quiet` |
| Text | `#000000` |
| Radius | 9999px |
| Padding | 8px 16px |
| Size | 72 x 42 at 1440 |

![Login](components/crops/button-login.png)

Disabled, loading, and pressed were not on the page.

## Link

Nav links are 16px Aeonik Regular, `#000000`, padding 8px 0. Footer legal links are 12px at 50% black.

![Pricing link](components/crops/link-nav.png)

## Text field

The footer email input is in the HTML with placeholder "Email address". It computed while `display: none`: colour `#171717`, background `#ffffff`, padding `10px 12px 10px 0`, border colour `rgba(0, 0, 0, 0.15)`, font 16px Aeonik Regular. It was not shown and not submitted.

## Select

The pricing message picker computed at 298 x 46, radius 12px, fill `rgba(0, 0, 0, 0.05)`, border `1px solid #ffffff`, padding 10px 16px, colour `#171717`, 16px Aeonik Regular.

## Card

The Free plan card is 378 x 411, padding 40px, radius 12px, gap 10px. Border colour `rgba(0, 0, 0, 0.05)`. Border width computed 0. Shadow none.

![Pricing card](components/crops/card-pricing.png)

## Gaps

| Component | Why it is missing |
|---|---|
| Icon button | Not on the public pages |
| Text area, checkbox, radio, switch | Not on the public pages |
| Tabs, tooltip, dialog, toast | Not shown. App CSS names a toaster. It was not rendered |
| Table, list row, avatar, badge | Not on the public pages |
| Login form | Wayback copy of app.outchat.ai/login is a spinner |
| Focus ring that shows | Computed outline is white on white |
| Dark marketing controls | The marketing site has no dark theme |
