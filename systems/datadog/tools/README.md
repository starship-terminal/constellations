# How this package was captured

2026-11-22. Public pages only.

Headless Chromium (Playwright at `~/.design-systems/pw`) opened https://www.datadoghq.com/. Viewport 1440 by 900 and 390 by 844, device pixel ratio 2. Screenshots are the first viewport, then quantised to 256 colours.

Login was opened at https://app.datadoghq.com/account/login and left empty. Get started free opened the signup modal. The form paints in an iframe from https://app.datadoghq.com/signup_corp. Nothing was typed. Sign up was not clicked. Google and Single Sign-On were not clicked.

The cookie banner was hidden with CSS and not accepted. Contact was not kept because the page prints a phone number. Search was not typed.

catalog.json and webapps-manifest.json were left alone, so `make design-md` and `make brief` were not run for this package.
