# Play components

Public marketing components measured on Internet Archive replays of createwithplay.com. The live host did not resolve on 19 November 2026. There is no signed-in app in this package.

| Component | State | Evidence | Values |
|---|---|---|---|
| Button, primary | Default | [button-primary-default.png](components/crops/button-primary-default.png) | 32px tall, 6px radius, padding 0 12px, fill `{action.primary}` `#17ffa6`, label `{text.ink}` `#212121`, Inter Tight 13px weight 600, letter-spacing 0.52px |
| Button, enterprise | Default | [button-enterprise-default.png](components/crops/button-enterprise-default.png) | 32px tall, 6px radius, padding 0 12px, transparent fill, white Inter Tight 13px weight 600 |
| Button, plan | Default | [pricing-dark-default.png](screenshots/pricing-dark-default.png) | 231 by 32px, 8px radius. Get Started and Choose Starter: `{surface.plan-button}` `#212121` with `{text.accent}` label. Choose Pro: `{action.pro}` `#aa6cf6` with black label. Contact Us: `{action.inverse}` white with black label |
| Button, phone store | Default | [home-dark-phone.png](screenshots/home-dark-phone.png) | 48px tall, 8px radius, padding 0 16px 0 12px. App Store fill `{action.primary}`. macOS fill white |
| Link, announcement | Default | [home-dark-default.png](screenshots/home-dark-default.png) | Learn More, Inter 12px weight 500, `{text.accent}` |
| Link, nav | Default | [home-dark-default.png](screenshots/home-dark-default.png) | Inter Tight 13px weight 500, white, 6px radius, padding 0 8px |
| Badge, plan | Default | [pricing-dark-default.png](screenshots/pricing-dark-default.png) | 6px radius, padding 0 6px. Neutral chips `{surface.chip}`. Pro chip fill `rgba(180, 118, 255, 0.07)`, text `{text.pro}` |
| Card, pricing | Default | [pricing-dark-default.png](screenshots/pricing-dark-default.png) | Pro card fill `{surface.pro}`, 8px radius. Other plan columns had a transparent computed background |
| Card, download | Default | [download-dark-default.png](screenshots/download-dark-default.png) | Fill `{surface.card}` `#262626`, 20px radius, padding 32px 24px |
| Switch, billing | Default, annual | [pricing-dark-default.png](screenshots/pricing-dark-default.png) | Track 99 by 35px, radius 72px, fill `{surface.raised}` `#171717`, padding 10px 12px. The thumb was not a separate measurable node |
| Icon button, carousel | Default | January homepage computed style | 40px square, radius 40px, fill `{surface.chip}` |
| Segment | Selected | January homepage computed style | Design tab 44px tall, radius 12px, padding 8px 16px, fill `{surface.chip}` |

## Gaps

- Button hover: the nav primary link's computed background stayed `#17ffa6` under pointer hover. Authored Framer hover rules target text links, not this button. No hover colour was measured.
- Button focus-visible: computed `outline` was `none` and `box-shadow` was `none` after `focus()`.
- Button pressed, disabled, loading: not shown on the public pages.
- Text field, text area, select, checkbox, radio, switch (settings), tabs (app), menu, tooltip, dialog, toast, list row, table, avatar: not present on the pages that loaded. The pricing toggle is the only switch.
- Signed-out login form: [createwithplay.com/create-account](https://web.archive.org/web/20260120211930/https://createwithplay.com/create-account) embeds `dashboard.createwithplay.com/login`. The iframe aborted. A June 2025 login capture rendered an empty body. No email field was measured. No account was created.
- Light theme: the marketing pages set `theme-color` to `#000000` and painted a black page. No theme toggle was on the page.
- Icons: the site favicon is an SVG on Framer's CDN. It was not copied. `icons/` is a catalog gap.
