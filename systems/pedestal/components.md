# Components

Public Pedestal storefront, measured on 2026-11-19 from `www.pedestal.com` in the light theme. Values are token names. Computed sizes are from a 1440 CSS-pixel viewport unless a row says otherwise. Crops were not saved: the preview browser returned "The browser is not producing screenshot frames".

## Button

Primary action. Product page Add to cart.

| | |
|---|---|
| Background | `light.background.action` |
| Text | `light.text.on-action`, `core.typography.cta` |
| Radius | `core.radius.md` |
| Height | `core.spacing.field` (74px at 1440) |
| Hover | `light.background.action-hover`, declared on `.betterhover:hover:bg-blue-dark` |
| Motion | `core.motion.duration.300` with `core.motion.easing.standard` |

Ink action. Contact Send, and Notify me.

| | |
|---|---|
| Background | `light.background.inverse` |
| Text | `light.text.on-inverse` |
| Radius | `core.radius.md` |
| Height | `core.spacing.field` |
| Padding | `core.spacing.1` |
| Hover | `light.background.inverse-hover` |

Grey menu row. Home mega-menu item, 48px tall, `core.radius.sm`, `light.background.muted`, hover `light` grey-medium `#e2e3de` (not a semantic token; see Gaps).

Nav chip. Header item, `core.typography.body`, padding 5px 10px 4px, `core.radius.sm`, transparent until hover (`black` at 5%). Configure sits on `light.background.sunken` at rest.

Disabled, loading, and pressed were not shown on a control at rest.

## Icon button

Search, cart, and close are inline SVGs at 28px or 32px, `currentColor`, on a transparent 2px-radius hit area. The cart label is text ("Cart 00"), not a badge. Artwork is not stored here.

## Link

Product and cart links are Suisse Intl 13px, `light.text.primary`, underline 1.5px in `light.text.secondary`, offset 4px. Header links over the hero are `light.text.on-hero` with no underline.

## Text field

Contact form, not submitted.

| | |
|---|---|
| Wrapper | `light.background.sunken`, `core.radius.md`, `core.spacing.field` |
| Input | transparent, `core.typography.label`, padding 0 12px, border 0 |
| Textarea | same wrapper, computed height 154px, padding 32px 12px 0 |
| Gap | `core.spacing.2` between the paired fields |
| Focus | browser outline `light.focus.outline` auto 1px on the input. The wrapper does not change. |

Search overlay field is a different control: page background, 56px type, 80px tall, 16px padding, capitalized. It was open on the home page and closed before the other readings.

## Text area

The contact Message field, above. No error state was triggered.

## Select

The country picker is a native `select` in the language banner (International - EUR and others). Its open list was dismissed and not measured as a menu. Footer language select uses `core.typography.small`.

## Checkbox

Cart terms. The input is screen-reader only. The box is a 16px SVG. The mark is a 6px square, black at 30% until checked, then `light.text.primary`. Radius 0. Not a switch.

## Radio

Not present. Colour choice is a row of round chips, below.

## Switch

Not present.

## Tabs

Not present on the captured pages.

## Menu

Header buttons (TV Stands, Power, Accessories, Pro) open a mega-menu. Featured labels use `core.typography.eyebrow` in `light.text.secondary`. A row inside it is the grey button above. The menu's minimum height custom property is 31.0625rem. It was closed before the resting readings.

## Tooltip

Not observed.

## Dialog

Country/language banner on first load, then a cookie dialog ("Pedestal uses cookies") with an Accept all control. Both were dismissed. Their resting styles were not measured after dismiss. Search opens as a fixed panel, class `invisible` once closed, 80px field.

## Toast

Not observed.

## Card

Collection product card on All TV Stands: 206 by 363 CSS pixels, radius 0, padding 0. Title and price nodes inside the card had no layout box in this viewport, so their type was not read off the card.

## List row

Cart recommendations render as named rows (Hook Mount, Moon) inside the empty-cart drawer. Row metrics were not separated from the drawer chrome.

## Table

Not present.

## Avatar

Not present.

## Badge

Collection title carries a 13px weight-600 count ("14") in Suisse Intl. Filter and Sort are 120px tiles, radius `core.radius.md`. Sort fill is `#efefef`. Filters fill is `light.background.inverse`.

Colour chip. 24px circle, `core.radius.chip`. The selected chip widens to 52px (`lg:w-[3.25rem]`).

## Gaps

- No component crops. The preview browser did not produce screenshot frames.
- Hover colours are declared stylesheet values, not a computed style with the pointer on the control.
- Pressed, disabled, loading, and field error were not on screen.
- The cookie dialog and country banner were dismissed before their controls were measured.
- Shopify Customer Account (orders, profile) uses Helvetica Neue on `#f6f6f6` and is not this inventory.
- Checkout, payment, and phone fields were not entered.
