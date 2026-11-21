# How this package was captured

2026-11-22. Public pages only.

Headless Chromium (Playwright at `~/.design-systems/pw`) opened https://newrelic.com/ and the header and footer destinations. Viewport 1440 by 900 and 390 by 844, device pixel ratio 2. Screenshots were quantised to 256 colours.

Log in opens `https://one.newrelic.com/` and paints on `login.newrelic.com` with a redirect query. That screenshot was discarded. Nothing was typed. No identity provider was clicked. Signup was opened empty and kept. Demo, contact, and pricing-request forms were not submitted, and those screenshots were not kept. No account was created. No captcha was solved. The cookie banner was hidden with CSS and not accepted.

`catalog.json` was left alone, so `make design-md` and `make brief` were not run for this package.
