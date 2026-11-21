# ClassPass components

Public site only, measured on 2026-11-21. Crops are in [components/crops](components/crops) where a locator screenshot succeeded. Several header controls timed out while scrolling into view, so those states are in the readings and the page screenshots, not as crops.

## What was measured

| Component | States | Where |
|---|---|---|
| Header | default | Home. White bar, 64px, shadow `rgba(0, 0, 0, 0.08) 0px 2px 10px 0px`. |
| Nav link | default, hover | Log in. 14px medium. Hover fills `#f7f7f7`. |
| Primary button | default | Log in submit on `/login`. Pill, 48px, `#0055ff` fill, white text, weight 500. |
| SSO button | default | Sign in with Apple. White pill, 48px, 1px `#d6d6d6` border. Not clicked. |
| Text field | default, focus | Email on `/login`. 42px, 4px radius, 1px `#e7e7e7` border. Focus border becomes `#1a5ee5`. Nothing was typed. |
| Password field | default | Same metrics as the email field. |
| Inline link | default | Forgot your password. `#1a5ee5`. |
| Filter chip | default, open | Fitness on `/search`. 32px, 16px radius, blue text. Open fills `#f7f7f7`. The search screenshots are not in the package because they showed a street address. |
| Heading | default | Plans h1. 60px norms, weight 400. |
| Footer | observed | Home full-page shot. Dark band, light links. |

## Not present on the public pages

Text area as a product control (partner contact has fields that were not opened into a measurement), select, checkbox, radio, switch, tabs, tooltip, toast, table, avatar, badge. A language menu is present. A cookie dialog is present and was not accepted.

## Gaps

- Hover and pressed on the blue pill were not captured. The header "Get 14 days free" locator matched the banner link (transparent, 20px) instead of the pill.
- Disabled, loading and error states were not on the public pages. No form was submitted, so no validation error was raised.
- Dark theme: not present.
- Focus ring width: the email field recolours its border on focus. `outlineWidth` stayed 0.
- Icon set: not extracted. The logo is the wordmark in the header.
