# Measurements

Read on 2026-11-21 from https://www.patternbrands.com/ in headless Chromium.

Desktop request: 1440×900, deviceScaleFactor 1. Measured `innerWidth` 1440, `innerHeight` 900, `devicePixelRatio` 1.

Phone request: 390×844, deviceScaleFactor 2. Measured `innerWidth` 390, `innerHeight` 844, `devicePixelRatio` 2. Home scroll height 2092.

Dark check: `matchMedia('(prefers-color-scheme: dark)').matches` was true. `body` background stayed `rgb(255, 255, 255)`, text stayed `rgb(30, 30, 30)`, footer stayed `rgb(8, 73, 53)`.

Computed values are in [components-computed.json](components-computed.json). Custom properties are in [css-vars.json](css-vars.json).

## Colour counts on the home page

Elements with a visible box, colour or background:

| Value | Count |
|---|---|
| transparent | 84 |
| rgb(30, 30, 30) | 39 |
| rgb(255, 255, 255) | 31 |
| rgb(8, 73, 53) | 17 |
| rgb(170, 173, 176) | 3 (Webflow badge) |

Font sizes: 16px on 67 elements, 14px on 10, 28.8px on 6. Radii: 0px on 84, 24px on 2 (button fill and circle wrap), 3px on the Webflow badge.

## States

Contact Us hover: `.btn__circle` background `#1d9671`, transform scaled to about 1, size 142×142. Resting circle background is the same green at scale 0.

Card hover: `.product_image` transform `matrix(1.1, 0, 0, 1.1, 0, 0)`. `.product_arrow` transform `matrix(1, 0, 0, 1, 4, 0)`.

Tab focus on Contact Us: outline `rgb(0, 95, 204) auto 1px`, offset 1px.

404 Go Home hover: background stayed `rgb(8, 73, 53)`.
