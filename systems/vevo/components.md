# Components

Public marketing chrome on `https://www.hq.vevo.com/`, signed out, 2026-11-19. Values are token names. Crops are in [components/crops](components/crops).

## Button

White pill, black label, 24px radius, 46px tall. The visible label is the inner span at 16px, not the anchor's 10px Arial. Hover fills `rgb(2, 2, 2)` and turns the label `rgb(253, 253, 253)` over 400ms ease.

| State | Crop | Tokens |
|---|---|---|
| Default | [button-default.png](components/crops/button-default.png) | `light.button.fill`, `light.button.label`, `core.radius.pill`, `core.typography.button` |
| Hover | [button-hover.png](components/crops/button-hover.png) | `light.button.fill-hover`, `light.button.label-hover`, `core.motion.duration.button` |
| Focus-visible | not captured on the pill | skip link uses `light.focus.skip` |
| Pressed, disabled, loading | not on the page | |

## Link

Desktop nav labels are 14px white with 10px horizontal padding. The anchor's own color is `rgb(0, 0, 238)`; the painted label is white. Phone menu items are 22px. The current item, Home, is `rgb(149, 7, 255)`.

| State | Crop |
|---|---|
| Desktop nav | [nav-default.png](components/crops/nav-default.png) |
| Phone menu open | [menu-open.png](components/crops/menu-open.png) |
| Hover, focus-visible | not captured on a nav link |

## Banner

Cookie bar, 68px, `light.background.action`. Decline is a blue button with a white 1px border and white label. Accept is a white button with blue label. Both are 32px tall, square corners, 16px horizontal padding, 14px cookie face.

| State | Crop |
|---|---|
| Default | [banner-default.png](components/crops/banner-default.png) |

## Icon button

Phone header menu control is 27 by 18 CSS px, transparent, three white bars. Close control in the open menu is 16px, fill `rgb(255, 255, 255)`. See [icons/menu.svg](icons/menu.svg).

## Wordmark

[icons/logo.svg](icons/logo.svg), 62 by 15 CSS px in the header, fill `#ffffff`.

## Card

Stat cards are white overlays on the crimson section: 20%, 40% and 60% white. Artist stills sit beside section copy. No separate card component with its own border or shadow.

## List row

Contact page rows are published department names and addresses on a blue stack. No interactive row, no hover state captured.

## Footer

Black band, 14px links (Contact, Brand, Careers), 15.1px legal line in white, social marks at 32px. [footer-default.png](components/crops/footer-default.png).

## Gaps

Not present on the signed-out marketing site: text field, text area, select, checkbox, radio, switch, tabs, tooltip, dialog, toast, table, avatar, badge, video player chrome.

Not captured: button pressed, button disabled, button loading, nav hover, nav focus-visible, menu item hover, dark theme. `prefers-color-scheme: dark` did not change the Wix colour tokens.
