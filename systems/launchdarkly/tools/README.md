# How this package was captured

2026-11-22. Public pages only.

Headless Chromium (Playwright at `~/.design-systems/pw`) opened https://launchdarkly.com/ and the header and footer destinations. Viewport 1440 by 900 and 390 by 844, device pixel ratio 2. Screenshots were quantised to 256 colours.

Sign in redirects to `https://app.launchdarkly.com/login?redirect=%2F`. That URL carries session state, so the screenshot was discarded. Continue was not clicked. Google and GitHub were not clicked. Signup was opened empty and kept. No form was submitted. No account was created. No captcha was solved. The cookie banner was hidden with CSS and not accepted.

`catalog.json` was left alone, so `make design-md` and `make brief` were not run for this package.
