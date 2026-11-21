# Nomad Goods design reference

A token set and component reference for Nomad Goods, the accessory brand (iPhone cases, watch bands, chargers, wallets). Captured from the public storefront at nomadgoods.com on 2026-11-21, signed out, in headless Chromium. The root redirects to `/sg/` (Singapore storefront). Desktop shots are 1440x900 at 1x. Phone shots are 390x844 at 2x. Nothing was signed into, bought, or submitted.

The storefront is a light theme only. Page ground is `#f3f3f3`, the nav bar is white with a 25px radius, headlines and buttons are Gotham-Bold, body and nav are Aleo. Buttons are pills.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site favicon, resized to 128 px |
| [tokens.json](tokens.json) | W3C DTCG tokens: `core` and `light`. Every token has `$extensions.source` |
| DESIGN.md | Not in this commit. `make design-md` writes it from catalog.json, and this capture was told not to edit catalog.json |
| [style-guide.html](style-guide.html) | Renders the measured roles, type and the two button faces |
| [components.md](components.md) | Component inventory and gaps |
| [patterns.md](patterns.md) | How the storefront combines those pieces |
| [site-tree.md](site-tree.md) | Which control opens which page, menu, dialog, or wall |
| [screenshots/](screenshots) | 33 captures, `{page}-light-{state}.png`, phone names prefixed `mobile-` |
| [raw/](raw) | CSSOM dump, computed roles, PDP measurements, the token spec |
| [tools/](tools) | Builders and the Playwright capture kit |

## Brief

<!-- brief:start -->
Brief is written by `make brief` from catalog.json. This capture does not edit catalog.json, so the generated Brief is not in this package yet.
<!-- brief:end -->

## Health

<!-- health:start -->
Health is written by `make grade` after a catalog entry and a scorecard review. Neither was added: the capture brief forbids editing catalog.json.
<!-- health:end -->

## How the values were read

Pages were opened signed out in headless Chromium. `tools/capture/vars.mjs` read the live CSSOM. The design sheets (`buttons-*.css`, `css-bundle-*.css`, `type-*.css`) are cross-origin, so the CSSOM skipped them. Those sheets were fetched and parsed. Computed styles of body, the nav bar, the homepage h1 and h2, Shop Now, and the PDP primary button were read on the live page at 1440x900 (`raw/computed-roles.json`, `raw/measured-chrome.json`, `raw/pdp-measured.json`).

The cookie banner was hidden with CSS. Accept, Decline and Preferences were not clicked. The Klaviyo signup dialog was closed with its X. No email was typed. No form was submitted. Account links to `account.nomadgoods.com` were recorded and not opened.

## What to distrust

- Sale's orange label computed as `rgb(0, 0, 0)` on the link. The orange is in the screenshot only. It is not a token.
- `#6b6b6b`, `#dedede`, `#d02d2d` and `#2c4a8c` are hexes counted in the stylesheet bundle, not colours read off a named text or status node.
- Button faces use a gradient plus an inset shadow. `backgroundColor` on the live button computed as transparent. The face colour comes from `buttons-FS3QHQ7I.css`.
- The capture is the `/sg/` storefront. Other regions were not opened. The locale control was clicked. Its list did not paint in the shot.
- `/sg/login` and `/account/login` are public 404s, not a login form.
- Screenshots are 256-colour PNGs. Read colours from tokens.json.

## Fonts

Gotham-Bold sets headlines and buttons. Aleo sets body and nav, with Helvetica Neue as the next family in the computed stack. Both Gotham and Aleo are proprietary and are not in this package. The style guide falls back to Helvetica Neue.

## Coverage

| Expectation | Status | Where |
|---|---|---|
| Page, surface, text, border | captured | `light.background.*`, `light.text.primary`, `light.border.default` |
| Muted text | partly | `#6b6b6b` from stylesheet frequency, not a named node |
| Accent hover and pressed | not captured | `:active` rule read in the button sheet, not photographed |
| Dark theme | not present | no theme switch on the public storefront |
| Type | captured | `core.typography` display, heading, button, body, label |
| Radius and control size | captured | pill 100px, bar 25px, button 48px, nav 70px |
| Motion | partly | button transition 150ms from the stylesheet |
| Elevation | partly | nav bar and button shadows measured; no elevation scale |
| Button, link, field, menu, dialog, card, badge | captured | [components.md](components.md) |
| Text area, radio, switch, tooltip, toast, table, avatar | not present | not on the public pages opened |
| Checkbox, select | not captured | cookie preferences not opened; locale list did not paint |
| Hover, focus-visible, disabled, error, loading | not captured | no form submitted, no separate state crops |
| App shell, search, cart, phone menu | captured | [patterns.md](patterns.md) |
| Account, checkout, waitlist, newsletter | not captured | walls and unsubmitted forms. See [site-tree.md](site-tree.md) |
| 1440 and 390 | captured | [screenshots/](screenshots) |
| Icons as assets | not present | brand artwork is not extracted ([docs/RIGHTS.md](../../docs/RIGHTS.md)) |

## Do and don't

- **Do set headlines in Gotham-Bold on the photograph.** The hero is white type, tight tracking, on a dark photo ([home](screenshots/home-light-default.png)).
- **Do pill the actions.** Shop Now and the PDP button are 48px pills, radius 100px ([home](screenshots/home-light-default.png), [pdp](screenshots/pdp-light-default.png)).
- **Do float a white nav bar.** 70px tall, radius 25px, hairline shadow, over the page ([home](screenshots/home-light-default.png)).
- **Do keep the page ground off-white.** Body and footer are `#f3f3f3`, not pure white ([home full](screenshots/home-light-full.png)).
- **Don't invent a dark theme.** The public storefront has one light scheme.
- **Don't treat the Sale orange as a token.** It is in the screenshot. The computed link colour was black.

## Rebuild

```sh
cd systems/nomadgoods
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  RAW=~/.design-systems/nomadgoods/raw-shots \
  node tools/capture/public/public.mjs
python3 tools/capture/quantize.py ~/.design-systems/nomadgoods/raw-shots
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  node tools/capture/vars.mjs
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

`make design-md` and `make brief` need a catalog.json entry. This capture does not add one.
