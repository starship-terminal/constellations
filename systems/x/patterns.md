# Patterns

Public signed-out surfaces only. Nothing was typed, submitted, or posted.

| Pattern | What was on the page | Evidence |
|---|---|---|
| Login chrome | Dark page, "Happening now." headline, light pills, Google button, "or" divider, email field, empty Continue, footer, QR card | [raw/readings.json](raw/readings.json). No screenshot: preview frames failed, headless Chromium returned 403 |
| Logged-out shell | Missing route paints a 600px column, a white Search pill, and a sign-up card. "Page not found" and the grey empty line are in the DOM | readings.json loggedOutShell. No screenshot, same 403 |
| Legal page | White page, black X, huge headline, date band, Download PDF pill | [screenshots/tos-light-1440.png](screenshots/tos-light-1440.png), [screenshots/privacy-light-1440.png](screenshots/privacy-light-1440.png) |
| About marketing | Black page, xVF display headline, translucent header that is hidden at 1169px | readings.json about. No screenshot: headless Chromium hit Cloudflare |

## Not on these pages

Form validation, empty-app state, loading, error toast, destructive confirmation, search results, lists, tables and onboarding sit behind sign-in or behind a query. Search was not submitted. The theme control on about.x.com was not pressed.
