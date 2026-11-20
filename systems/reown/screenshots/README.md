# Screenshots

Headless Playwright, 2026-11-19, of public pages that returned 200 and no Cloudflare challenge. Viewport requested 1440x900, or 390x844 for the phone shot, deviceScaleFactor 1. The T3 preview tab (1169x731, devicePixelRatio 2) is where the computed styles were read. `preview_snapshot` returned "The browser is not producing screenshot frames", so these files are a second pass, not frames from that tab.

| File | Page |
|---|---|
| home-light-default.png | https://reown.com/ |
| home-light-phone.png | https://reown.com/ at 390 |
| pricing-dark-default.png | https://reown.com/pricing |
| faq-light-default.png | https://reown.com/faq |
| blog-light-default.png | blog post |
| docs-dark-default.png | https://docs.reown.com/ |
| docs-light-default.png | same docs page after Switch to light theme, then restored to dark |
| contact-light-default.png | https://reown.com/contact |

The sign-in wall was not screenshotted. Headless Playwright was not launched against it.
