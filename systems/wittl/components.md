# Wittl components

Public marketing homepage only. Measured on a local render of the 2025-11-08 Wayback HTML, viewport 1440 x 900, unless a row says otherwise. Crops are 256-colour.

## Button

Primary "Get started" is an anchor with class `kcyxOU`. Height 46px, padding 0 24px, radius 4px, background `#263921`, transition `all 0.2s ease-in-out`. The span is authored `#fff` at 18px. Hover did not change the background. Focus left `outline: none` and `box-shadow: none`.

Secondary "Login" uses class `eBOQwx`: the same size, background `#F3F3F1`, span colour `#141616`.

| State | Crop |
|---|---|
| Primary default | [components/crops/button-primary-default.png](components/crops/button-primary-default.png) |
| Primary hover | [components/crops/button-primary-hover.png](components/crops/button-primary-hover.png) |
| Secondary default | [components/crops/button-secondary-default.png](components/crops/button-secondary-default.png) |

Pressed, disabled, loading and error were not on the page.

## Link

Nav links are inline anchors. At rest they inherit `#141616`. Hover paints background `#F3F3F1`, padding 8px 16px, radius 4px. Footer links computed `#ffffff` while the footer opacity was 0. Their underline is a `::before` scaleX animation, 0.52s `cubic-bezier(0.32, 0.94, 0.6, 1)`, not captured open.

Crop: [components/crops/link-nav-hover.png](components/crops/link-nav-hover.png).

## Navigation

The header bar is white. The nav is 1024px wide, 102px tall, padding 28px 0. Crop: [components/crops/nav-default.png](components/crops/nav-default.png).

The features dropdown and the phone drawer are in the HTML at opacity 0. They were not opened. The phone menu button (class `iCIQPr`) is `display: none` above 768px and 46px square below that. No crop.

## Card

Feature cards (class `kSjCHD`) are `#F3F3F1`, radius 4px, padding 40px. The companion frame is the same stone colour with 10px padding. The image wash behind one feature is `#E7FDBC`.

Crop: [components/crops/card-feature.png](components/crops/card-feature.png).

## Badge

The update pill (class `etidoa`) is `#C1FA6B`, radius 99px, font-size 12px, line-height 12px, padding 8px.

Crop: [components/crops/badge-default.png](components/crops/badge-default.png).

## Check mark

A 24px square, `#C1FA6B`, radius 4px, with a 12px Lucide check. It is decoration on a marketing list, not a checkbox.

Crop: [components/crops/check-mark.png](components/crops/check-mark.png).

## Accordion

"What is Wittl?" is a button, padding 20px, label authored at 20px, plus icon 16px. The following panel stayed at height 0 after a click. Closed crop: [components/crops/accordion-default.png](components/crops/accordion-default.png).

## Display type

The `h1` computed to 48.421px FF More Pro, line-height 48.421px, letter-spacing -0.968px, colour `#141616`. The webfont did not load, so the crop shows the Georgia fallback.

Crop: [components/crops/type-display.png](components/crops/type-display.png).

## Gaps

- Text field, text area, select, checkbox, radio, switch, tabs, dialog, toast, table and list row were not on the archived homepage.
- Icon button, open menu, open accordion, tooltip and avatar were not captured. The menu and accordion need the page script.
- Pricing, guides, features, legal pages and `app.wittl.co` were not rendered. The live domain did not resolve, so those pages were not fetched in a browser.
- No dark theme was declared.
- No focus ring was painted.
- Hover motion on the primary button was declared (`0.2s ease-in-out`) and did not change the computed background.
