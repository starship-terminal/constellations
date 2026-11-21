# How this package was captured

2026-11-22. Public pages only.

Headless Chromium (Playwright at `~/.design-systems/pw`) opened https://posthog.com/ and the header destinations. Viewport 1440 by 900 and 390 by 844, device pixel ratio 2. Screenshots were quantised to 256 colours.

Get started paints https://us.posthog.com/signup with no query string. Login paints https://us.posthog.com/login with no query string. Both were kept. Continue was not clicked. Google, GitHub, GitLab, and Passkey were not clicked. Talk to a human was photographed empty. Send was not clicked. No form was submitted. No org was created. No captcha was solved. The cookie banner was left on screen.

`catalog.json` was left alone, so `make design-md` and `make brief` were not run for this package.

`test_site_tree.py` checks the date, the stop note, and that the homepage, pricing, and empty walls exist.
