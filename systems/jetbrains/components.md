# JetBrains components

Public components measured on jetbrains.com and account.jetbrains.com on 2026-11-21, signed out. The login wall was measured at rest. Values are computed styles. Colours that match a declared `--rs-*` token name that token.

Crops live in [components/crops/](components/crops).

## Button

The home hero's Explore Air pill is near-black `#19191c` (`core.color.black`) with white text, 40px tall, 20px radius. The store Buy pill is brand purple `#6b57ff` (`light.accent`).

| State | Crop | Fill | Text | Radius |
|---|---|---|---|---|
| default | [button-primary-default](components/crops/button-primary-default.png) | `#19191c` | `#ffffff` | 20px |
| hover | [button-primary-hover](components/crops/button-primary-hover.png) | `#19191c` | `#ffffff` | 20px |
| focus | [button-primary-focus](components/crops/button-primary-focus.png) | `#19191c` | `#ffffff` | 20px |
| buy | [button-buy-default](components/crops/button-buy-default.png) | `#6b57ff` | `#ffffff` | 20px |
| buy hover | [button-buy-hover](components/crops/button-buy-hover.png) | `#6b57ff` | `#ffffff` | 20px |

## Icon button

Header icon buttons are 32 by 32. Search, account, cart and language sit in the dark header.

| State | Crop |
|---|---|
| default | [icon-button-default](components/crops/icon-button-default.png) |
| hover | [icon-button-hover](components/crops/icon-button-hover.png) |
| focus | [icon-button-focus](components/crops/icon-button-focus.png) |
| menu (phone) | [icon-button-menu-default](components/crops/icon-button-menu-default.png) |

## Link

The hero's "Read the story" is white text with an arrow. The login card's "Create an account" is brand blue on white.

| State | Crop |
|---|---|
| default | [link-default](components/crops/link-default.png) |
| hover | [link-hover](components/crops/link-hover.png) |
| signup | [link-signup-default](components/crops/link-signup-default.png) |

## Text field

Search opens as a dark field labelled "⌘K for advanced search". Nothing was typed. Continue with email on the login wall was not clicked, so no email field was opened.

| State | Crop |
|---|---|
| search open | [search-field-opened](components/crops/search-field-opened.png) |

## Tabs

The store audience switcher is a pill group. "For Individual Use" is the selected pill, black stroke on white.

| State | Crop |
|---|---|
| selected | [tabs-selected](components/crops/tabs-selected.png) |

## Menu

Products opens a white mega menu under the dark header: IDE columns, a JetBrains Air banner, and a "Find your tool" pill.

| State | Crop |
|---|---|
| opened | [menu-opened](components/crops/menu-opened.png) |

## Card

Home audience cards are 8px radius on the dark field. Store price cards are white with a hairline border. The login card is a white column on the gradient.

| State | Crop |
|---|---|
| audience | [card-default](components/crops/card-default.png) |
| audience hover | [card-hover](components/crops/card-hover.png) |
| price | [price-card-default](components/crops/price-card-default.png) |
| login | [login-card-default](components/crops/login-card-default.png) |

## Badge

"Best offer" is a small red label on the All Products Pack card.

| State | Crop |
|---|---|
| default | [badge-default](components/crops/badge-default.png) |

## OAuth button

Login rows are outline pills, 312 by 40, grey stroke, JetBrains Sans 16.

| State | Crop |
|---|---|
| default | [oauth-button-default](components/crops/oauth-button-default.png) |
| hover | [oauth-button-hover](components/crops/oauth-button-hover.png) |
| focus | [oauth-button-focus](components/crops/oauth-button-focus.png) |
| email | [oauth-button-email-default](components/crops/oauth-button-email-default.png) |
| icon row | [oauth-icon-row-default](components/crops/oauth-icon-row-default.png) |

GitLab, WeChat and Bitbucket are three 96 by 40 icon buttons on one row. Their accessible names are Continue with Gitlab, Continue with WeChat and Continue with Bitbucket. They were not clicked.

## Navigation

The site header is a 72px dark bar, wordmark left, Products through Pricing in the centre, icon buttons on the right.

| State | Crop |
|---|---|
| bar | [nav-default](components/crops/nav-default.png) |
| item | [nav-link-default](components/crops/nav-link-default.png) |
| item hover | [nav-link-hover](components/crops/nav-link-hover.png) |

## Banner

A purple announcement strip sits under the header on home: "Introducing Air in IDEs".

| State | Crop |
|---|---|
| default | [banner-default](components/crops/banner-default.png) |

## Gaps

These checklist components are not on the public signed-out surface, so they were not captured:

- Text area, select, checkbox, radio, switch: no public form mounts them. The store billing control is a tab pill, recorded above.
- Tooltip, dialog, toast: none opened on the public pages. The cookie dialog was hidden and never answered.
- Table: the store is cards, not a data table.
- Avatar: the header account control is an icon button, not a user avatar.
- List row: the mega menu is link columns, recorded as menu.
- Disabled, loading and error states: none appear signed out.
- Email field, validation, checkout and the signed-in account: Continue with email was not clicked, and no identity provider was followed. See [login-review.json](login-review.json).
