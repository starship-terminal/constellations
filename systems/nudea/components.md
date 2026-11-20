# Nudea components

Public signed-out Shopify theme, measured 2026-11-19. Crops are in [components/crops](components/crops). Values are token names from [tokens.json](tokens.json).

## Button

Primary action on the product page. Fill `color.raven`, label `color.cotton`, radius `radius.pill`, height `size.button-primary` (50px), type `typography.button` (Neue Haas Grotesk Display 12px, weight 400, tracking 0.96px, uppercase). Border is 1px raven.

| State | Crop | What was read |
|---|---|---|
| Default | [button-primary-default.png](components/crops/button-primary-default.png) | Computed on `.product-form__submit` |
| Hover | [button-primary-hover.png](components/crops/button-primary-hover.png) | Stylesheet sets `.button--primary:hover` colour to `var(--raven)`. The fill swap was not computed, because hover could not be held in the preview browser. |
| Focus | [button-primary-focus.png](components/crops/button-primary-focus.png) | `.button:focus-visible` box-shadow is `0 0 0 0.3rem` background, `0 0 0 0.5rem` foreground at 0.5, and a 0.5rem glow. Programmatic `focus()` did not paint that ring. |
| Pressed | not captured | Not held. |
| Disabled | not captured | No disabled control on the pages opened. |

The hero "Shop now" is `.button.button--cotton`: transparent fill, 1px `color.cotton` border, cotton label, 40px tall, same pill radius. The outline `.button` on cotton is the inverse: transparent fill, raven border and label, 40px.

## Link

Footer links and the collection eyebrow are `typography.eyebrow`: Neue Haas Grotesk Display 12px, tracking 0.96px, uppercase, no underline. Body links inside product copy were not given a separate colour. The unvisited browser blue (`rgb(0, 0, 238)`) appeared on some anchors before the theme font loaded and is not a Nudea token.

## Text field

Search field `.search__input`: Abril Text 20px / 30px, tracking 0.4px, padding 27px 98px 27px 41px, height 83px, bottom border 1px `color.grid`, radius 0. Newsletter email fields in drawers are 13px Neue Haas Grotesk, placeholder "Email address". They were measured inside closed drawers (height 0 on some) and were not submitted.

## Select, checkbox, radio, switch

Not present on the public pages opened. Size is a radio group drawn as a segmented control, recorded under Size below.

## Size

A row of labels, 55px tall, 1px `color.grid` border. Selected XS fills `color.raven` with `color.cotton` text and a 10px radius on the outer left. The last pill (XL) has a 10px radius on the outer right. Middles are square. Type is 13px Neue Haas Grotesk, weight 400, tracking 0.26px.

## Colour swatch

37px circle, `border-radius: 100%` (token `radius.swatch` is the derived 18.5px). Active swatch border colour computed to transparent. The swatch image is the product photo, not a flat token.

## Badge

`.product-tag--sale`: fill `color.red`, label `color.cotton`, radius 5px, padding 0 7px, height 20px, 10px Neue Haas Grotesk, tracking 0.2px. Crop: [badge-sale.png](components/crops/badge-sale.png). Text read: "Save 29%" and "Save 40%" on the collection.

## Card

Collection grid column is 360px at 1440 and 195px at 390. Image radius 10px. Title is Abril Text 14px / 20px, weight 300. Price is the price style, with the compare-at price struck through in the same raven. Crop: [card-product.png](components/crops/card-product.png).

## Accordion

Product details title is uppercase Neue Haas Grotesk 12px, tracking 0.96px, prefixed with "+". Open state was not expanded.

## Dialog and drawer

Cart, login, search and notification drawers exist in the DOM. Login fields (email, password) and "Submit" / "Cancel" buttons were measured while closed or off-screen. They were not opened and not submitted. Account creation was not entered.

## Menu

Desktop nav is Abril Text 16px / 34px, tracking 0.32px, weight 300. "Black Friday" uses `color.red` (`.nav-item--promo`). The mega menu is in the DOM and was not opened as a settled state.

## Icon button

Header icons (search, account, bag) are unfilled buttons. Bag label computes next to the wordmark. No separate icon-button token beyond the 44px close control measured in a drawer.

## Gaps

| Component | Status |
|---|---|
| Button pressed, disabled, loading | Not captured. Not held, or not on the page. |
| Text area | Not present on the pages opened. |
| Select | Not present. |
| Checkbox, radio, switch | Not present, except the size radios drawn as the segmented control. |
| Tabs | Not present. |
| Tooltip | Not present. |
| Toast | Not present. |
| Table | Not present. |
| Avatar | Not present. |
| Dark theme | Not present. The store does not switch theme. |
| Checkout, payment, Klarna | Not entered. The Klarna mark is visible on the product screenshot and its fill was not read from CSS. |
