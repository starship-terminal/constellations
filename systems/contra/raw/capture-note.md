# Capture note

Date: 2026-11-19.

Surfaces: public signed-out pages on contra.com. No account was created. No email, phone, card, wallet, government ID, or company SSO was entered.

The T3 preview tab loaded https://contra.com/ (redirected to /?view=projects) without a Cloudflare challenge. preview_snapshot returned "The browser is not producing screenshot frames" twice. Computed styles were read from that live tab with preview_evaluate, then confirmed in headless Chrome on the same public marketing URLs.

Headless Chrome (Playwright, channel chrome) measured:

- https://contra.com/ at 1440x900 and 390x844, deviceScaleFactor 2
- https://contra.com/features/payments
- https://contra.com/partners
- https://contra.com/hackathons
- https://contra.com/log-in (email field measured, nothing typed)
- https://contra.com/sign-up (first name, last name, email, and a Cloudflare Turnstile widget were on the page; nothing typed, no screenshot kept)

prefers-color-scheme: dark left the home page white. --rollout-* computed values on that same page were the dark pair (#1e1d1b surface, #fff text). They are recorded in measurements.json and are not a second live theme.

Stylesheet: https://builds.contra.com/assets/assets/static/shared_core.CbqWNEWO.b-jlMthc.css (cross-origin; cssRules threw SecurityError in the preview tab; named custom properties were read from getComputedStyle(document.documentElement)).
