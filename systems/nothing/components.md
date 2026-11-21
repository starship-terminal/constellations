# Nothing components

Public storefront controls measured on 2026-11-21 at 1440 x 900. Values are computed styles from [raw/components-computed.json](raw/components-computed.json). Crops are in [components/crops/](components/crops). Hover and focus readings that moved off-screen (y below 0) are not treated as a second visual state.

## promo-bar

Yellow announcement strip. The link's own background is transparent; the yellow is the bar behind it (`--accent-yellow` `#ffc700`).

| State | Crop | Type | Fill | Radius | Size |
|---|---|---|---|---|---|
| default | [promo-bar-default.png](components/crops/promo-bar-default.png) | 16px/400 NType82-Regular, colour `#040404` | transparent on the yellow bar | 0 | 708 x 30, padding 8px 16px |

## hero-cta

The "Shop now" control on the homepage hero.

| State | Crop | Type | Fill | Radius | Size |
|---|---|---|---|---|---|
| default | [hero-cta-default.png](components/crops/hero-cta-default.png) | 16px/400 NType82-Regular, colour `#040404` | `#ffffff` | 4px | height 40, padding 12px 16px |

## text-field

Contact support search field. Not filled.

| State | Crop | Type | Fill | Radius | Size |
|---|---|---|---|---|---|
| default | [text-field-default.png](components/crops/text-field-default.png) | 18px/300 NType82, colour `#000000` | `#e9ecef` | 800px (pill) | height 44 |

## cart-button

Header cart icon. Opens the empty-cart dialog. The measured box sat at y=-43 because the region suggestion shifted the header during the first measure. Size 32 x 32 is the reading. Re-measure after Stay is a gap.

| State | Crop | Type | Size |
|---|---|---|---|
| default | [cart-button-default.png](components/crops/cart-button-default.png) | 16px/400 NType82-Regular | 32 x 32 |

## nav-link

Header label. The first measure placed it at y=-37, so the crop may clip the label. Type matches the promo bar: 16px/400 NType82-Regular, colour `#040404`, transparent fill.

## Shared values

- Body type on chrome is NType82-Regular at 16px / 400.
- Control radius on the hero button is 4px. The contact field is a pill (800px).
- Ink is `#040404` (`--greyscale-black`). Page wash is `#f4f4f4` (`--greyscale-100`).
- Promo yellow is `#ffc700`. Accent red `#c8102e` and accent blue `#002f6c` are declared and not assigned to a measured control in this pass.

## Gaps

- Add to bag on the product page was not measured. The dark product page shows a black button labelled ADD TO BAG. Its computed style is Not captured.
- Menu-link and footer-link locators missed. Not captured.
- Focus rings did not paint in the first measure (outline width 0). Not captured as a distinct focus style.
- Pressed states were not measured.
- Icons were not extracted as SVG. The site icon is [icon.png](icon.png).
