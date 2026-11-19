# Components

Measured on the signed-out Urban Outfitters site on 2026-11-19. Values are computed styles or authored rules that reference the site's custom properties. Crops were not taken: the preview browser did not produce screenshot frames.

## Button

The cart button (`.o-pwa-button-cart`) on the product page is 520 by 45, fill `#222222`, text `#ffffff`, Helvetica 16px, weight 700, letter-spacing 0.5px, padding 10px 20px, border 1px solid `#222222`, radius 0. The label read "Get It Before It's Gone". It was not clicked.

Authored states, from the stylesheet, using tokens that resolved on the page:

| State | Background | Text |
|---|---|---|
| Default | `--button-cart-background` `#222222` | `--button-cart-text` `#ffffff` |
| Hover and focus | `--button-cart-background-hover` `#707070` | `#ffffff` |
| Disabled | `--button-cart-background-disabled` `#aaaaaa` | `#ffffff` |
| Confirmation | `--button-cart-background-confirmation` `#3a8700` | `#ffffff` |

The sign-in Next button (`.o-pwa-button-primary`) measured the same fill, type, padding, and radius at 395 by 45. It was not submitted.

## Icon button

Banner previous and next controls are 44 by 44, radius 0, transparent background. The sign-in close control is 44 by 44 with radius 50%. Search submit is 46 by 43. No standalone SVG set was extracted.

## Link

Promo links are 12px Helvetica, white, underlined, letter-spacing 0.5px. Nav links are 12px, `#222222`, letter-spacing 0.5px, padding 10px 12px, 60px tall, radius 0. The authored hover colour is `--link-navigation-text-hover` (`#707070`) with an underline and a 1px bottom border of `--link-navigation-border-hover` (`#aaaaaa`). Utility links, including Sign In / Sign Up, are 12px `#222222` with letter-spacing 0.5px. Size Guide is 12px `#707070` and underlined.

## Text field

Header search is 12px Helvetica, `#222222`, letter-spacing 0.5px, padding-left 15px, height 43, radius 0, transparent background. The sign-in phone field is 16px, white background, border 1px solid `#222222`, radius 0, padding 10px 10px 10px 44px, 296 by 45. It was left empty. Placeholder colour token `--input-text-placeholder` is `#707070`. Focus border token `--input-border-focus` is `#222222`.

## Text area

Not present on the pages that were measured.

## Select

The sign-in country select is 94 by 45, 16px Helvetica, white background, border 1px solid `#707070`, radius 5px. It was not changed. No product size select was present; sizes are chips.

## Checkbox

The sign-in form shows a "Keep Me Signed In" checkbox, already checked. The input computed at 13 by 16 with `appearance: auto`. No custom box colour was measured. It was not toggled.

## Radio

Colour choices are radio inputs with circular labels. A selected swatch label computed at 36 by 36, radius 50%, border 1px solid `#222222`. The inner swatch image is 30 by 30, radius 50%, border 1px solid `#dddddd`.

## Switch

OneTrust cookie switches exist in the preference center. That dialog was closed (0 by 0) and was not answered. No product switch was measured.

## Tabs

The sign-in dialog has Mobile Number and Email tabs. The selected tab is 12px `#222222` with a 2px bottom border of `#222222`. The resting tab is `#707070` with a 1px bottom border of `#dddddd`. The email tab was not opened for entry.

## Menu

Primary nav is a horizontal list under the logo. Mega-menu panels were not opened. Mobile navigation was not measured: the viewport stayed at 1440.

## Tooltip

A tooltip trigger sits beside the phone field (15 by 15). The tooltip itself was not opened. `--tooltip-background` is `#222222` and `--tooltip-text` is `#ffffff`.

## Dialog

Sign In is a white dialog, 475 by 620, inner padding 80px 40px, radius 0, no shadow. The heading is 18px `#222222`. Subcopy is 12px `#707070`. It was closed without a submission. The OneTrust preference center was present in the DOM and not visible.

## Toast

Not present on the pages that were measured. `--notification-background` is `#f5f5f5` and `--notification-border` is `#dddddd`.

## Card

Product tiles have no border, radius, or shadow. Home tray tiles measured 248 by 398. The women's grid tile measured 427 by 688. Title and regular price are 12px `#222222`, letter-spacing 0.2px.

## List row

Accordion rows (Highlights, Details, Size + Fit, Shipping + Returns) are 520 by 60, 14px Helvetica, `#222222`, letter-spacing 0.2px, padding 20px 0, radius 0. They were not expanded.

## Table

Not present on the pages that were measured. `--table-border` is `#dddddd` and `--table-head-background` is `#f5f5f5`.

## Avatar

Not present on the signed-out pages that were measured.

## Badge

No product badge was visible in the measured tiles. `--badge-background` is `#f5f5f5` and `--badge-text` is `#222222`. A heart count overlay sat on the product image. Its count is shopper data and is not recorded as a token.

## Gaps

- Hover, pressed, disabled, and error states were read from authored rules, not from a live repaint, except search focus, which did not change the computed border.
- No screenshot crops.
- Checkout, bag, and payment were not opened.
- The phone field and email tab were not filled.
