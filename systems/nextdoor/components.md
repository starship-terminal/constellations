# Nextdoor components

Public surface only, measured on 2026-11-21. The product app (feed, posts, maps, profiles) sits behind login and was not opened. Values below are token names from [tokens.json](tokens.json). Crops are in [components/crops/](components/crops). Several homepage crops read the transparent button wrapper, so the painted face is described from the computed style of the inner `BaseButton` div (`rgb(27, 135, 81)`, radius pill). That reading is in the How the values were read section of the README.

## Button

| State | Where | Fill | Text | Radius | Height |
|---|---|---|---|---|---|
| default | Homepage Sign up face | `light.color.accent` #1b8751 | white, 16px, weight 620 | `core.radius.pill` | 48px |
| hover | Same face | same fill, `filter: opacity(0.88)` | white | pill | 48px |
| focus-visible | Not captured as a distinct ring on the pill | | | | |
| pressed | CDP forced `:active` on the wrapper. Face colour did not change. | | | | |
| default | About Log in | `light.color.emphasis` #232f46 | white | pill | 40px |
| hover | About Log in | emphasis at 0.88 alpha | white | pill | 40px |
| default | Small-business Create Your Business Page | `light.color.accent` | white | pill | 40px |
| hover | Same | accent at 0.88 alpha | white | pill | 40px |
| default | Advertise Now | `light.color.surface` #f0f2f5 | `light.color.text` | pill | 38px |
| hover | Advertise Now | #d8d9dc (Not captured as its own token) | text | pill | 38px |
| default | Claim your free Business Page | `light.color.emphasis` | white | pill | 52px |

Disabled, loading and error buttons were not present on the public pages.

## Icon button

The phone header has a 40px menu button. Its crop is [icon-button-menu-default.png](components/crops/icon-button-menu-default.png). The control was not opened.

## Link

Directory category links use `light.color.link` #1197de. The signup card's Privacy Policy link is underlined body text. Invite-code and Get started links open walls and were not followed.

## Text field

The homepage email field is 352 x 56, radius 12px (`core.radius.md`), with an inset 1px ring in `light.color.border` (#cad3e5). Focus replaces that ring with a 2px inset in `light.color.borderStrong` (#232f46). The field was not typed into. Help-center search is a 40px white field. Not submitted.

## Text area, select, checkbox, radio, switch

Not present on the public pages that were opened.

## Tabs

Not present.

## Menu

Partners opens a white menu with Publishers and Public agencies. The menu is in [home-light-menu-partners.png](screenshots/home-light-menu-partners.png). Businesses opens a second menu. Neither item was followed during measurement.

## Tooltip, toast, dialog

The homepage signup card is a raised white panel (400 x 566, radius 12px) over a photo. It is the page, not a dialog that can be dismissed. No tooltip or toast appeared.

## Card

Marketing pages use a split hero: ink type on a pale surface beside a photograph. The small-business page is the clearest example: [smallbiz-light-default.png](screenshots/smallbiz-light-default.png).

## List row, table

The directory is a four-column link list, not a table. [directories-light-default.png](screenshots/directories-light-default.png).

## Avatar, badge

Not present on the signed-out pages. Neighbor avatars live behind login.

## Gaps

- Signed-in feed, composer, map, notifications, and settings: behind https://nextdoor.com/login/.
- Hover on the homepage green pill is a CSS filter, not a second fill token.
- Focus ring on pills: Not captured as a distinct outline.
- Disabled, loading, error, and empty states of the product: Not captured.
- Dark theme: declared, not applied.
- Pressed state: forced through CDP. A real press on Continue, Sign up, or Log in would submit or open a wall.
