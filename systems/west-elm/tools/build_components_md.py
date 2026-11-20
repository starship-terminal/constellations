#!/usr/bin/env python3
"""Write components.md from the readings. No crops: screenshots were unavailable."""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
TEXT = """# West Elm components

Public signed-out surfaces, measured on westelm.com on 2026-11-19 from computed styles. No element crops: the preview browser returned "The browser is not producing screenshot frames", and a headless Playwright pass was refused with "403 - Restricted Access". This inventory names the element and the token. It does not pretend a crop exists.

## Button

Filled square. Login and the email overlay use `button.btn-primary`: background `light.action.primary` (#212121), text `light.text.inverse`, height `core.size.button` (42px), padding 8px, letter-spacing `core.letterSpacing.button` (1.4px), uppercase, radius `core.radius.none`.

Add to cart is a different control, `button.btn-conversion`: background `light.action.conversion` (#af1a31), height `core.size.addToCart` (52px), same tracking. The stylesheet sets hover to #7a0000 and disabled to #d48c8c. Those two states were not hovered live.

The homepage hero CTA (`SHOP NEW ARRIVALS`) is the inverse: white fill, ink text, 1px white border, padding 12px 24px, weight 375.

`button.btn-quaternary` (`NO THANKS`) is transparent, ink text, 42px tall, same tracking.

## Icon button

The header search submit is a 36px square, fill #4d4d4d, 1px #c8c8c8 border. The quantity decrease control is 44px, white, 1px #c8c8c8 border, 2px radius on the left corners only, glyph #a6a6a6 when it cannot decrease. The favorite toggle is a 24px hit target. No separate icon-button token beyond those sizes.

## Link

Category nav links are 10px, weight 300, tracking 0.4px, line-height 40px, uppercase, ink, no underline. Utility links (ACCOUNT) are 9px, weight 375, tracking 0.72px, uppercase. Secondary links (Room Inspiration) and footer links are 12px, #646464, tracking 0.36px, no underline. Sister-brand links are 10px, #646464.

## Text field

Search: 36px tall, 300px wide, 1px #c8c8c8 border, padding 6px 35px 6px 16px, 14px type, radius 0.

Email overlay field: 56px, 1px #212121 border, padding 0 16px, placeholder #363636.

Account email: 59px, 1px #212121 border, padding 28px 16px 8px, 16px type. The floating label is #666666.

## Text area

Not present on the captured public pages.

## Select

The product page Fabric select is a native `select`: 40px, white, 1px #767676 border, 14px type, radius 0. The open menu was not captured.

## Checkbox

Not measured. The email overlay has a hidden consent input. Its painted checkbox was not isolated.

## Radio

Not present as a painted control. Fabric options are thumbnail tiles, not radios.

## Switch

Not present on the captured public pages.

## Tabs

Not present. Category navigation is a single row of links, not tabs.

## Menu

Category nav is a horizontal list. Account, store and cart open drawer dialogs (`role="dialog"`, class `drawer-component-container`). Those drawers were in the DOM. Their open visual state was not measured after the email overlay was dismissed. The mega-menu flyout was not opened.

## Tooltip

Not present on the captured public pages.

## Dialog

The homepage email overlay is `dialog.modal_component`: white, 726px wide, shadow `0 0 11px rgba(0, 0, 0, 0.16)`, radius 0, padding 60px 83px. The scrim is `div.shader` at rgba(0, 0, 0, 0.4). Title is Sanomat 36/45, tracking 0.72px. It was dismissed with NO THANKS and was not submitted. It asks for a mobile number, which was not entered.

## Toast

Not present on the captured public pages.

## Card

A collection grid item (`.grid-item`) is 370px with 5px padding. The image is 360×359, radius 0. The name is 16px / 20.8px, tracking 0.48px. The price is 14px. A NEW flag is 12px, weight 400, tracking 1.2px. No card radius and no card shadow.

## List row

Not present as a data list. Footer link columns are the closest list: 12px, #646464, on the #f4f4f4 footer.

## Table

Not present on the captured public pages.

## Avatar

Not present on the captured public pages.

## Badge

The NEW flag (`.flag-text.flag-newcore`) is text only, ink, 12px, tracking 1.2px. No filled badge was measured.

## Shared

Focus: the global stylesheet declares `:focus-visible` outlines, including `solid 2px #2563eb` and `dotted 1px currentColor`. A live focus ring was not forced.

Motion: stylesheet transitions are `background-color .5s cubic-bezier(0.4, 0.8, 0.4, 0.8)` and `all .5s`. `prefers-reduced-motion` does not appear in the global stylesheet (0 matches). That is a finding, not a missed reading of a rule that is there.

Pressed and loading states were not forced.

## Gaps

- No screenshots or crops. The preview browser did not produce screenshot frames. Headless Playwright was answered with 403 Restricted Access, so those images were discarded.
- Dark theme: not shown. No theme switch on the public pages.
- Phone width (390): not measured. The pane was 1169×731.
- Hover, focus-visible and pressed were not forced live. Hover and disabled colours for Add to cart and the primary button come from stylesheet rules.
- Mega-menu, cart drawer, filter sheet and store drawer were not opened.
- Add to cart was not clicked. Checkout, payment, Apple sign-in and the email overlay's phone field were not entered.
- Text area, checkbox, radio, switch, tabs, tooltip, toast, table and avatar were not on the captured pages.
- Reduced motion: no authored `prefers-reduced-motion` rule in the global stylesheet.
"""

(HERE / "components.md").write_text(TEXT)
print("wrote components.md")
