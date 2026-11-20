# Components

Measured on theorg.com, signed out, on 2026-11-19. Colours are computed styles. Crops are from the same public pages.

| Component | States captured | Crop |
|---|---|---|
| Button, primary | default, hover | [button-primary-default.png](components/crops/button-primary-default.png), [button-primary-hover.png](components/crops/button-primary-hover.png) |
| Button, dark | default, compact | [button-dark-default.png](components/crops/button-dark-default.png), [button-dark-compact.png](components/crops/button-dark-compact.png) |
| Button, secondary | default | [button-secondary-default.png](components/crops/button-secondary-default.png) |
| Button, submit | default | [button-submit-default.png](components/crops/button-submit-default.png) |
| Button, follow | default | [button-follow-default.png](components/crops/button-follow-default.png) |
| Link, login | default | [link-login-default.png](components/crops/link-login-default.png) |
| Text field | default, focus | [text-field-default.png](components/crops/text-field-default.png), [text-field-focus.png](components/crops/text-field-focus.png) |
| Menu | open | [menu-platform-open.png](components/crops/menu-platform-open.png) |
| Chart card | default | [chart-card-default.png](components/crops/chart-card-default.png) |
| Billing toggle | yearly selected | [toggle-yearly-selected.png](components/crops/toggle-yearly-selected.png) |

## Button, primary

Header Sign up. Height 32px, padding 16px, radius 40px, DMSans 14px weight 500, white text.

| State | Background |
|---|---|
| default | rgb(23, 84, 207) |
| hover | rgb(15, 73, 189) |

The declared token `--primary-100` is `#0F4BE5` and `--primary-100-hover` is `#0515d4`. The painted button is neither.

Focus-visible on the marketing button classes is a 2px solid outline, rgb(0, 48, 136). Keyboard focus landed on a menu link before that outline was read on Sign up, so the focus crop is not here.

## Button, dark

Start for free and Get started. Background rgb(39, 39, 37), text rgb(253, 253, 252), radius 24px. The hero button is 48px tall with 24px horizontal padding. Get started on pricing is 32px tall with 12px horizontal padding.

## Button, secondary

Learn more and Follow. White fill, 1px solid rgb(230, 230, 230), text rgb(13, 13, 13), radius 24px on Learn more and 10px on Follow.

## Text field

Login and signup inputs. Height 48px, radius 10px, border 1px solid rgb(218, 217, 214), padding 9px 12px 9px 34px, Inter 14px / 20px. Focus paints a black border. Placeholder is "Enter work email" on login and "Work email" on signup. Nothing was typed or submitted.

## Menu

Platform opens a `[role=dialog]`, 351 by 199 px, white, radius 12px, padding 20px, border 1px solid rgba(0, 0, 0, 0.08), shadow `rgba(0, 0, 0, 0.15) 0px 4px 20px 0px`. Titles are 14px weight 500. Descriptions are 13px, rgb(102, 102, 102).

## Chart card

`PositionCard_container` is 216 by 92 px, white, radius 12px, shadow `rgba(0, 0, 0, 0.05) 0px 1px 2px 0px` plus a 1px rgb(234, 234, 235) ring. The name is 14px weight 500, rgb(10, 10, 11). Initials avatars are 46px circles on rgb(228, 228, 231).

## Billing toggle

The wrap is white, 1px solid rgb(230, 230, 230), radius 32px, padding 4px. Yearly is a dark pill, rgb(32, 30, 29), radius 80px, white 14px weight 500, with a blue "33% off" badge, rgb(23, 84, 207), radius 16px, 12px weight 600. Monthly stays grey, rgb(102, 102, 102). The switch was not clicked.

## Gaps

- No checkbox, radio, switch, select, text area, toast, tooltip, table, or badge as a product component beyond the pricing "33% off" chip.
- Disabled, loading, pressed, and error states were not on the public pages. `--error` is `#f6354d` as a declaration only.
- Icon buttons in the header (search, more) were not cropped.
- No dark theme was on screen.
