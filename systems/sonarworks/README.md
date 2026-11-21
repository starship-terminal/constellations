# Sonarworks design reference

A token set and component reference for the public Sonarworks site, for building marketing pages in that style. Read from **www.sonarworks.com** on **2026-11-21**, signed out, in headless Chromium at 1440×900 and 390×844. One theme: light. The header is black on a white page. Inter is the only computed family.

The control map is [site-tree.md](site-tree.md). Pricing in the nav redirects to `/black-friday`. Login at `/account/login` is an auth wall (email, password, Facebook, Google, Apple) and was not filled. The signed-in account, checkout, and the support center were not reached.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site icon, 128 px PNG, resized from the favicon at www.sonarworks.com/favicon.ico |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds the declared Tailwind base and highlight scales, Inter, the measured type ramp, and radii. `light` holds role aliases. No dark set. Every token has `$extensions.source`. |
| [DESIGN.md](DESIGN.md) | Generated from tokens.json and this README. One theme, no provenance. |
| [style-guide.html](style-guide.html) | Renders the tokens and a few components. Light only. |
| [components.md](components.md) | Component inventory, crops, and gaps |
| [patterns.md](patterns.md) | Shell, hero, pricing, forms, lists |
| [site-tree.md](site-tree.md) | Which control opens which page, menu, or wall |
| [components/crops/](components/crops) | Element screenshots, `{component}-{state}.png` |
| [screenshots/](screenshots) | Page captures, `{page}-light-{state}.png`. Desktop 1440×900 at 1x. Phone shots are `mobile-*` at 390×844 and 2x. |
| [raw/](raw) | [css-vars.json](raw/css-vars.json) (declared utilities) and [components-computed.json](raw/components-computed.json) |
| [tools/](tools) | Builders and the adapted capture kit |

## Brief

<!-- brief:start -->
<!-- brief:end -->

## Health

<!-- health:start -->
<!-- health:end -->

## How the values were read

The page inlines a Tailwind style block. It does not declare a `:root` token layer. [tools/build_tokens.py](tools/build_tokens.py) reads the colour utilities from [raw/css-vars.json](raw/css-vars.json), which was parsed from that style block on 2026-11-21. `bg-base-00` through `bg-base-100` and `bg-highlight-*` are the palette. `--tw-*` names are Tailwind internals and were not tokenised.

Type, nav heights, and control colours were read with `getComputedStyle` on the live page (body, h1, h2, `#top-navigation`, `#primary-navigation`) and, where the selector matched, written by [tools/capture/public/measure.mjs](tools/capture/public/measure.mjs) to [raw/components-computed.json](raw/components-computed.json).

Screenshots came from [tools/capture/public/public.mjs](tools/capture/public/public.mjs) via Playwright. CookieScript and GetSiteControl were aborted and removed. No consent button was clicked. No form was submitted. No email was typed.

## What to distrust

- **This is the public site, not the account app.** Licenses, devices, trials, and checkout are behind login or a Buy now click. Those branches stopped.
- **Pricing is a campaign page.** `/soundid-reference/pricing` redirected to `/black-friday` on the capture day. That redirect can change.
- **Highlight colours are declared, not all painted as chrome.** Blue, green, lime, orange, pink, purple, red, sale yellow, and yellow exist as utilities. The home chrome is black, white, and grey. Do not treat every highlight as a status role.
- **The contact field computes a black fill.** That reading is the contact page, not the login field, which is white.
- **Quantised screenshots.** `screenshots/` are 256-colour PNGs. Read colours from tokens.json.
- **Focus ring.** `--tw-ring-color` is declared. A painted `:focus-visible` ring was not confirmed on every control. Primary-tab focus matched its hover fill.
- **Company menu item crop.** The panel is in the screenshot. The first link reported height 0, so there is no item crop.
- **No dark theme.** Do not invent one from the black header.

## Fonts

**Inter** (Google Fonts, weights 400, 500, 600, 700, 900) is the computed family on body, headings, and nav. The page also declares an Inter Fallback face that points at local Arial for metric matching. Inter is not committed. The style guide loads Inter from Google Fonts and falls back to sans-serif.

## Coverage

| Expectation | Status | Where |
|---|---|---|
| Colour roles | captured | `light.surface`, `light.text`, `light.border`, `light.accent` over `core.color.base` and `core.color.highlight` |
| Type | captured | `core.typography` display, heading, body, label. Inter only. |
| Spacing | not captured | Tailwind spacing utilities exist in the stylesheet. A spacing scale was not measured onto elements, so none is tokenised. |
| Radii | captured | `core.radius` from `.rounded-*` (2px through 9999px) |
| Borders | captured | `light.border.default` is base-25. `light.border.hairline` is the computed `#dfe0e1`. |
| Elevation | not present | Computed box-shadow on the measured controls is none. No elevation scale. |
| Motion | not captured | The product bar uses a 300ms opacity transition in its class list. Durations were not read into tokens. |
| Sizing | captured | `core.sizing.top-nav` 56px, `core.sizing.primary-nav` 104px |
| Layout breakpoints | captured as observation | `lg` shows the desktop bars. Below that, Menu opens `#mobile-navigation`. Numeric breakpoints were not tokenised. |
| Button | captured | Learn more pills in [home-light-default](screenshots/home-light-default.png) and [components/crops/learn-more-default.png](components/crops/learn-more-default.png) |
| Link | captured | [components/crops/top-link-default.png](components/crops/top-link-default.png), [components/crops/footer-link-default.png](components/crops/footer-link-default.png) |
| Menu | captured | [home-light-company-menu](screenshots/home-light-company-menu.png), [home-light-product-menu](screenshots/home-light-product-menu.png), [mobile-home-light-menu](screenshots/mobile-home-light-menu.png) |
| Text field | captured | Contact field and empty login email field. Not typed. |
| Card | captured as a page pattern | Product cards in [home-light-default](screenshots/home-light-default.png). No separate card crop (selector missed). |
| FAQ / disclosure | captured | `<details>` on `/soundid-reference`. Crop failed. Reading is in raw/components-computed.json. |
| Text area, select, checkbox, radio, switch | not captured | Checkboxes exist on the Black Friday page and were not measured. |
| Tabs, tooltip, toast, dialog, table, avatar | not present | No product instances on the captured pages. Cookie dialog was hidden, not captured. |
| States: default | captured | Crops and screenshots |
| States: hover, focus | captured | Primary tab only. Hover and focus both `#1e1f20`. |
| States: pressed, disabled, loading, error | not captured | Not held or not present on the measured controls. |
| Form with a validation error | not captured | No form was submitted. |
| Login and signup | not captured past the wall | [login-light-wall](screenshots/login-light-wall.png). `/account/signup` not opened. Facebook, Google, Apple not clicked. |
| Support center | not captured | support.sonarworks.com returned HTTP 403 (Cloudflare challenge). |
| Checkout | not captured | Buy now was not clicked. Cart page is empty. |
| Dark theme | not present | No control. |
| Widths 1440 and 390 | captured | Desktop and `mobile-*` screenshots |
| Sitemap articles, partner pages, EU funding pages | not captured | Listed in site-tree.md. The nav and footer tree was captured, not all 209 sitemap URLs. |

## Do and don't

1. **Do keep the page white and the header black.** The shell is `#ffffff` under a `#000000` bar, with `#96999c` links. See [home-light-default](screenshots/home-light-default.png).
2. **Do set display type in Inter at 44px with tight tracking.** The home headline is 44/52, weight 400, letter-spacing -1.5px. See [home-light-default](screenshots/home-light-default.png).
3. **Do open product navigation as a bar, and Company as a dark menu.** Hover reveals them. They are not pages. See [home-light-company-menu](screenshots/home-light-company-menu.png) and [home-light-product-menu](screenshots/home-light-product-menu.png).
4. **Do use a pill for the primary action.** Learn More is a 9999px radius pill, white on dark photos and black on the light card. See [components/crops/learn-more-default.png](components/crops/learn-more-default.png).
5. **Don't style the account app from this package.** Login stops at the wall. Licenses, devices, and checkout were not captured.
6. **Don't treat the highlight scale as status colours.** Those utilities are campaign accents. The chrome does not use them as success, warning, or danger.

## Rebuild

From `systems/sonarworks/`:

```sh
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
python3 tools/capture/quantize.py ~/.design-systems/sonarworks/raw-shots screenshots
```

Live recapture (Playwright at `PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs`):

```sh
node tools/capture/public/public.mjs
node tools/capture/public/measure.mjs
```

`make design-md` from the repo root regenerates DESIGN.md once the package is in the catalog. This capture does not edit catalog.json.
