# Gaps

Measured 2026-11-19. Public marketing pages were read in the T3 preview browser and again in headless Playwright at 1440 and 390. The signed-out app at `https://app.superlist.com/` was opened in the preview browser only.

- Dark theme. The marketing site and the signed-out app were light. No theme switch was on the pages.
- Primary button gradient stops. Computed style is `linear-gradient(0deg, color(display-p3 0.772358 0.137098 0.050813), color(display-p3 0.97561 0.379986 0.256739))`. The preview canvas clipped those `color()` values. Painted pixels from the 2x crop are the record: top of the fill about `rgb(255, 80, 47)`, bottom about `rgb(220, 0, 0)`. Those sampled pixels are stored as tokens. The display-p3 numbers are in `components-computed.json`.
- Hover and pressed colour. Hover scaled the pill to about 1.05 and did not change the gradient. Pressed was not forced.
- Focus ring. The first Tab stop was the logo link, outline `rgb(0, 95, 204) auto 1px`. A focused field outline was not on the marketing pages.
- Disabled, loading, error, checkbox, radio, switch, select, textarea, tooltip, toast, dialog, menu open, avatar, badge. Not on the measured marketing pages.
- Signed-out email form colours. `app.superlist.com` is a Flutter canvas. The accessibility tree showed "Continue with Apple", "Continue with email", then an email field labelled "Type your email" and a "Send link" button. The field's DOM node is the browser's default input (`Arial`, inset border), not the painted control. Painted fill, radius, and type of that form were not readable as CSS. The link was not sent.
- Apple sign-in. The button was visible and not followed.
- Payment. Pricing links to `https://app.superlist.com/settings/subscriptions`. That page was not opened. No card was entered.
- Screenshots from the T3 preview browser. `preview_snapshot` returned "The browser is not producing screenshot frames". The committed PNGs are from headless Playwright on public marketing URLs that returned 200 with no Cloudflare challenge. The Flutter login was not screenshotted.
- `prefers-reduced-motion`. No such media rule was found in the marketing stylesheets. A reduced-motion pass was not run.
- App product version. The marketing footer has a "version" label. The number was not read as a stable product version.
