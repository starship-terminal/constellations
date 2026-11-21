# Rivian components

Measured on the public homepage at https://rivian.com/ on 2026-11-21, desktop 1440×900, after Reject All. Crops are in [components/crops/](components/crops). Values are token names from [tokens.json](tokens.json).

## Button

The header Demo drive link is the primary button: fill `{light.component.button.background}` (`#ffaa00`), text black, height 32px, padding 8px 16px, radius 9999px, Adventure 14px weight 600.

| State | What changed |
|---|---|
| default | `#ffaa00` fill. Crop: `button-primary-default.png` |
| hover | `#ffbd2e`. Crop: `button-primary-hover.png` |
| pressed | Forced `:active`. Fill `rgba(255, 189, 46, 0.85)`. Crop: `button-primary-pressed.png` |
| focus-visible | Keyboard focus after Shift. Same amber, no painted ring (`outline: none`). Crop: `button-primary-focus-visible.png` |
| disabled | Not captured. No disabled primary was on the public header. |
| loading | Not present on the public header. |

The hero Design yours link is the inverse button: white fill, black text, radius 40px, height from the hero (taller than the header pill). Crop: `button-inverse-default.png`.

The hero Book a drive link is an outline button on the photograph: transparent fill, white text, 40px radius. Crop: `button-secondary-default.png`. Hover did not change the computed fill.

## Nav item

Header Vehicles button. Transparent at rest, `rgba(0, 0, 0, 0.1)` on hover and while the menu is open. Pill radius. Crops: `nav-item-default.png`, `nav-item-hover.png`, `nav-item-selected.png`.

## Menu

Vehicles mega-menu, opened from the header. The panel node itself computed transparent; the cards inside are painted by their own surfaces. Crop: `menu-default.png`. Charging, Technology, Discover and Gear Shop are the same chrome, captured as page screenshots.

## Link

Explore, inside the Vehicles menu. Black text, no fill, underline from the product's link style. Crop: `link-default.png`, `link-hover.png`. Hover did not change the computed colour in this reading.

## Icon button

Have a question? launcher.  Circular, yellow. Crop: `icon-button-default.png`. The mobile Open control is 32×32, pill radius. Crop: `icon-button-menu-default.png`.

## Dialog

Have a question? opens the Rivian Assistant panel (an iframe titled Newsletter form). The message field was not filled. Crop: `dialog-default.png`. Cookie preferences was captured once as a page screenshot before Reject All, then the banner was dismissed and not reopened.

## Not present on the captured public pages

Text area, select, checkbox, radio, switch, tabs (the homepage Technology / Performance / Design band is a button group, not a tab widget with a measured selected token), tooltip, toast, table, avatar, badge. A form with a validation error was not produced: no form was submitted.

## Gaps

- Focus ring: the primary button paints no outline on keyboard focus. Recorded as absent, not invented.
- Disabled, loading and error states of the button were not on the public header.
- The assistant panel is an iframe. Its inner field styles were not read.
- Dark theme: not present. `color-scheme` on the document was `normal`.
