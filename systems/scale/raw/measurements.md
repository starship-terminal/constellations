# Measurements

Read on 2026-11-21 from live public pages in headless Chromium.

| Reading | Where | Viewport |
|---|---|---|
| Body background #ffffff, text #000000, 16px/24px Aeonik 400 | scale.com/ computed body | innerWidth 1440, innerHeight 900, devicePixelRatio 1 |
| Header height 88px | scale.com/ header box | 1440×900 |
| Get Started 40×105px, radius 8px, fill #000000, text #ffffff | header `a[href="/demo"]` | 1440×900 |
| Log In text #929292, radius 8px, transparent fill | header login link | 1440×900 |
| Demo h1 40px/50px, weight 400, letter-spacing -0.4px, colour #212121 | scale.com/demo | 1440×900 |
| Text field fill #ffffff, text #171717, 14px, radius 8px | demo first-name input | 1440×900 |
| Docs dark page #090b10, text #ffffff, html class `dark` | scale.com/docs after choosing Dark | 1440×900 |
| Phone shots | 390×844 CSS, devicePixelRatio 2, PNG 780×1688 | mobile-* files |

`--spacing` resolves to `.25rem`. Spacing tokens of 4, 8, 12, 16, 24, and 32px are derived from that step at the measured 16px root.

The declared dark semantic colours are HSL triplets on `[data-theme="dark"] body` in raw/css-vars.json. Marketing pages did not change when `prefers-color-scheme: dark` was emulated.

Theme colour meta on the homepage: `#000000`.
