# Capture notes

Date: 2026-11-19.

## Browser

T3 preview tab `tab_4i_b476fa69-d865-4d9c-9974-6281ced1c8e8`, opened with `reuseExistingTab: false`.

| Page | URL | Viewport | DPR | visualViewport scale |
|---|---|---|---|---|
| Home, first read | https://savvycal.com/ | 1169 x 731, then 1440 x 900 | 2 | 1 |
| Login | https://savvycal.com/login | 1440 x 900 | 2 | 1 |

`html` class on the first home load was `dark`. Body background stayed `rgb(252, 247, 237)` (`bg-brand-oatmeal`). Removing `dark` resolved `--color-cal-*` to the light calendar tokens. Headless Chrome loaded the same marketing pages with `html` class empty and the same oatmeal page colour.

`preview_snapshot` then returned: "The browser is not producing screenshot frames." Measurements already read were kept. No screenshot was invented from that browser.

Headless Playwright (Chromium from `~/.design-systems/pw`) loaded the public pages after they had already loaded in the preview browser without a Cloudflare challenge. Login was included because it had already loaded in the preview browser without a challenge. Signup was not opened.

## Stylesheet

`https://d1j9qa1hxpa4m.cloudfront.net/assets/main-fcbd905e3a5e102869c096dfd6d70798.css?vsn=d`

Cross-origin in the preview tab, so custom properties were read with `getComputedStyle(document.documentElement)` and the file was fetched for declared rules. Inter is loaded from `https://rsms.me/inter/inter.css`. Computed body font is `InterVariable, sans-serif`.

## Not entered

- `/signup` (calendar OAuth plus email, not email-only)
- Google, Microsoft, and Fastmail buttons (not clicked)
- Sign In (not submitted)
- Send instructions on `/reset-password` (not submitted)
- Pricing CTAs (not followed into checkout)
- No card, phone, or company SSO
