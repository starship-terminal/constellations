# How this package was captured

2026-11-22. Public pages only.

Headless Chromium (Playwright at `~/.design-systems/pw`) opened https://www.atlassian.com/software/opsgenie. That URL 301s to https://www.atlassian.com/software/opsgenie/migration. Viewport 1440 by 900 and 390 by 844, device pixel ratio 2. Screenshots were quantised to 256 colours.

Sign in and the product login were opened and left empty. Continue and Next were not clicked. The Get it free control on the shared bar did not navigate. The pricing Get it free link points at https://www.atlassian.com/try, which redirects to the product index. An opsgenie signup bundle URL redirected to an empty Service Collection signup wall. That wall was photographed and not submitted. No identity provider was clicked. No form was submitted. Search was not typed.

The cookie banner was hidden with CSS and not accepted. Impressum was not opened because the same Atlassian page prints a street address and a phone number.

`catalog.json` and `webapps-manifest.json` were left alone, so `make design-md` and `make brief` were not run for this package. `systems/atlassian` was not touched.
