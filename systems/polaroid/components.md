# Components

Public signed-out storefront, www.polaroid.com/en_sg, 2026-11-19. Crops are element screenshots of the live controls. Values are token names.

## Button

Shop Bundles is a white square, 42px tall, Commit Mono 12px uppercase, no border, no radius. Get Inspired, beside it on the hero, is a 1px white outline with a transparent fill and white label.

| State | Crop | Tokens |
|---|---|---|
| Shop Bundles, default | [button-shop-default](components/crops/button-shop-default.png) | `light.page` on the photo, `light.text`, `core.typography.button`, `core.control.shop-height`, `core.radius.none` |
| Get Inspired, default | [button-inspired-default](components/crops/button-inspired-default.png) | transparent fill, 1px `light.on-accent` border, `light.on-accent` label |
| Continue, default | [button-continue-default](components/crops/button-continue-default.png) | `light.accent` fill, `light.on-accent` label, `core.control.continue-height` |
| Add to Bag, default | [button-add-default](components/crops/button-add-default.png) | same as Continue. 290px wide on the MoMA Now product page. Not clicked. |
| Hover | not cropped | Declared rule `.tDSUJq_link:not([disabled]):hover` swaps to `rgb(21, 21, 21)` fill and `rgb(255, 255, 255)` label. A synthetic mouseover did not apply it. Playwright hover was intercepted by the nav. |

## Link

Header nav is Real Head Regular 13px, letter-spacing -0.2106px. The current section (Holidays, on the cameras page) is `light.nav-active` (`#d60026`). Other items are `light.text`. Mega-menu links are Real Head Demibold 26px.

## Text field

The login email field is a 1px `light.border` box, 45px tall, square corners. The input itself has no border. The label is 13px Real Head Regular. Focus computed `outline: none` and `box-shadow: none`. The field was focused and not submitted.

| State | Crop |
|---|---|
| Default | [field-email-default](components/crops/field-email-default.png) |

## Badge

Bundle Savings is a black square tag, white 13px Real Head Regular, padding 4px 4.96px. See [badge-bundle-default](components/crops/badge-bundle-default.png). A red "New" tag is visible on the cameras listing. Its computed style landed on a parent with a transparent background, so the red is not tokenised.

## Icon button

Search is a 20px button in the header. Account and cart sit beside it. States were not cropped.

## Product finder

Product Finder is the one pill: 32px, radius 100px, 1px `light.border`, white fill, Commit Mono 12px uppercase. Compare beside it is the same type at radius 0.

## Card

Listing cards use `--color-grey-200` (`light.surface`) and a 1px `light.border`. Radius 0. The declared hover mixes that grey 85% with black. That hover was not measured live.

## Not on these pages

Text area, select (the region picker is a native control inside a closed dialog), checkbox, radio, switch, tabs, menu (the mega-menu was not opened), tooltip, dialog (the cookie dialog was dismissed before measuring), toast, list row, table, avatar.

## Gaps

- Hover and pressed states were not captured as crops. The outline button's hover rule is declared, not computed under a real pointer.
- Focus on the email field removed the outline. No focus ring token.
- Disabled, loading, and error states of the buy button were not shown. Add to Bag was not clicked.
- The "New" badge red was not isolated from its parent.
- Dark mode is declared on `html.dark-mode` and was not on the page.
