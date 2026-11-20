# Pattern Brands components

Public site only, captured 2026-11-21. Values are computed styles unless the row says Sampled. Crops are in [components/crops/](components/crops).

## Button

The home Contact Us control is `a.btn`. The fill is `.btn__bg` at `#084935`, radius 24px, height 44px, padding 12px 20px. Label is P22 Mackinac Pro 16/20.8, white.

| State | What changed | Crop |
|---|---|---|
| default | Green fill, white label | [button-default.png](components/crops/button-default.png) |
| hover | `.btn__circle` (`#1d9671`) scales from 0 to cover the fill over 700ms, easing `cubic-bezier(0.625, 0.05, 0, 1)` | [button-hover.png](components/crops/button-hover.png) |
| focus-visible | Tab paints a 1px `#005fcc` outline, offset 1px. The stylesheet's `*[tabindex]:focus-visible` rule names `#4d65ff`; the browser painted the UA outline instead | [button-focus-visible.png](components/crops/button-focus-visible.png) |
| pressed | Mouse-down did not change colour. Not a separate token | |
| disabled, loading | Not present | |

The 404 Go Home control is a different button: `a.button.w-button`, fill `#084935`, white label, radius 1600px, padding 8px 24px, 320×37 at 1440. Hover did not change its colour. Crops: [error-button-default.png](components/crops/error-button-default.png), [error-button-hover.png](components/crops/error-button-hover.png).

## Link

Visit links (`.product_link`) are `#084935`, 16px, underlined, with an 18×8 arrow that shifts 4px right on card hover. Footer links (`a.footer_link`) are Cadiz 14/18.2, white, no underline. Crop: [link-default.png](components/crops/link-default.png), [footer-link-default.png](components/crops/footer-link-default.png).

## Card

`a.product_item` is 240×339 at 1440 and 350×398 at 390. Square corners, no shadow. The photo (`.product_image`) scales to 1.1 on hover. Copy is 16/20.8 ink. Crop: [card-default.png](components/crops/card-default.png), [card-hover.png](components/crops/card-hover.png).

## Heading and body

Home heading is `h2.heading-style-h4`, P22 Mackinac Pro 28.8/31.68 at 1440, 24/26.4 at 390, weight 400, colour `#1e1e1e`. The rotating word is painted green. Computed colour stayed `#1e1e1e`. The flat green in the raw screenshot is `#13af7f` (Sampled). Legal `h1` is 48/52.8 at 1440 and 40/44 at 390. Body is 16/20.8. Crop: [heading-default.png](components/crops/heading-default.png), [body-default.png](components/crops/body-default.png).

## Footer

`footer.footer_component` is `#084935` with white Cadiz 14px links. At 1440 it is a 175px band under the cards. At 390 the columns stack. Crop: [footer-default.png](components/crops/footer-default.png).

## Logo

Inline SVG wordmark, 301×91 at 1440 and 160px wide at 390. Kept only as it appears in screenshots. Crop: [logo-default.png](components/crops/logo-default.png).

## Gaps

Text field, text area, select, checkbox, radio, switch, tabs, menu, tooltip, dialog, toast, list row, table, avatar and badge are not on the public site. No disabled, loading, or field-error state was reachable. No destructive confirmation. The only error surface is the Webflow 404.
