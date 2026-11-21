# How this package was captured

2026-11-22. Public pages only. WordPress.com, not wordpress.org.

Headless Chromium (Playwright at `~/.design-systems/pw`) opened https://wordpress.com/ and the header and footer destinations that stay on wordpress.com. Viewport 1440 by 900 and 390 by 844, device pixel ratio 2. Screenshots were quantised to 256 colours.

`/log-in/` in headless Chromium returned a captcha interstitial. That shot was discarded. The empty login wall was photographed in a signed-out preview tab and copied in. Nothing was typed. Identity providers were not clicked. Continue was not clicked. No form was submitted.

`catalog.json` was left alone, so `make design-md` and `make brief` were not run for this package.
