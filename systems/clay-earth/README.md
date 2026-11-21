# Clay design reference

Clay's public site is Mesh. `https://clay.earth/` returns 301 to `https://me.sh/`. This package was read signed out on **2026-11-21** in headless Chromium at 1440 x 900 and 390 x 844.

The marketing CSS modules declare no custom properties. Tokens are computed styles from the live pages. Home paints dark. Pricing, integrations, and the sign-in wall paint light. No dark switch was found on the light pages.

Signed-in app screens were not captured. `https://app.me.sh/login` and `https://app.me.sh/login?signin` are the same sign-in form (Apple, Google, email, SSO). Nothing was typed, submitted, or sent to an identity provider.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site icon, 128 px, from `https://me.sh/apple-touch-icon.png` |
| [tokens.json](tokens.json) | Measured colour and font tokens. `dark` is the home page. `light` is pricing and the sign-in wall |
| [DESIGN.md](DESIGN.md) | Generated from the tokens and this README. Placeholder until `make design-md` can see a catalog entry |
| [style-guide.html](style-guide.html) | Renders the tokens |
| [components.md](components.md) | Controls that were measured, and the states that were not |
| [patterns.md](patterns.md) | How the public pages are put together |
| [site-tree.md](site-tree.md) | Public tree: header, footer, menus, and what each control opens |
| [login-review.json](login-review.json) | What the login URLs actually showed |
| [components/crops/](components/crops) | Element crops |
| [screenshots/](screenshots) | Page captures. Names use `-light-` because the kit labels one run that way. Home is painted dark |
| [raw/](raw) | Readings, the token spec, and capture sidecars |
| [tools/](tools) | Capture reader and the token and style-guide builders |

## Brief

<!-- brief:start -->

Read [tokens.json](tokens.json) before designing in this style. The catalog entry is not in this PR, so this Brief is hand-written and `make brief` has not rewritten it.

Home is black with ivory display type (Verlag Condensed, 64px, weight 700) and a bronze accent (`#f2b98b`) on the wordmark and the header CTA. Light pages use paper `#f9f8f6`, ink `#1f1f1f`, and orange `#fb7232` on the popular plan and the email button.

<!-- brief:end -->

## Health

<!-- health:start -->

Not graded. This PR does not edit `catalog.json`, so `make grade` cannot attach a scorecard row. Coverage gaps are in the table below.

<!-- health:end -->

## How the values were read

`tools/capture/public/read.mjs` opened me.sh and `app.me.sh/login?signin` in headless Chromium and called `getComputedStyle`. A follow-up probe recorded the home `h1`, the pricing plan card, the POPULAR badge, and the sign-in buttons. Those readings are the `source` strings in [raw/component-tokens.json](raw/component-tokens.json). `tools/build_tokens.py` writes [tokens.json](tokens.json).

Stylesheet custom properties: none. [raw/css-vars.json](raw/css-vars.json) records `varCount: 0` and the five Next.js sheets that did load.

`<meta name="theme-color">` on the home page is `#000000`. `site.webmanifest` says `theme_color` `#ffffff` and `background_color` `#ffffff`. The mask-icon colour was not set.

## What to distrust

- Screenshot filenames say `light` for every page. Home is painted dark. The filename is the kit label, not the theme.
- The nav pill's own `backgroundColor` read transparent. Its fill is not a token.
- `GET MESH FREE` was not measured as its own node. The header Get started control was.
- Sign-in orange (`#ff6821`) and pricing orange (`#fb7232`) are two measured values. They are not one token.
- Quantised screenshots are 256-colour PNGs. Read colours from tokens.json.
- The product demo on the home page shows sample names. Those are the site's own marketing copy.

## Fonts

Verlag and Verlag Condensed on the marketing pages. SF Pro Text on the sign-in wall. The files are not in this package. The guide falls back to the system sans.

## Coverage

| Item | Status |
|---|---|
| Colour roles, dark home | Captured. [tokens.json](tokens.json) `dark` |
| Colour roles, light pages | Captured. `light` |
| Type | Captured as font families and the home h1 size. No type scale token |
| Spacing, radii, elevation, motion | Not captured as scales. A few radii are in [components.md](components.md) |
| Button, link, text field, menu, card, badge | Captured on the public pages |
| Checkbox, radio, switch, tabs, tooltip, toast, table, select, textarea | Not present on the public pages |
| Dialog, focus-visible, pressed, disabled, loading, error | Not captured |
| App shell behind sign-in | Not captured. Wall at `https://app.me.sh/login` |
| Dark theme of the light pages | Not present |
| Desktop 1440 and phone 390 | Captured. [screenshots/](screenshots) |

## Do and don't

- **Do** treat home and pricing as two painted themes. Home is black. Pricing is paper. [home-light-default.png](screenshots/home-light-default.png), [pricing-light-default.png](screenshots/pricing-light-default.png).
- **Do** keep one orange on a light page. The popular plan and the email button carry it. Other plan buttons are outlines. [pricing-light-default.png](screenshots/pricing-light-default.png).
- **Do** set the hero in a condensed face at a large size. The home h1 is 64px Verlag Condensed, weight 700, colour `#fefef7`.
- **Don't** invent a signed-in app from the marketing demo. The demo is a picture on the home page. The real app is behind the wall. [login-light-signin.png](screenshots/login-light-signin.png).
- **Don't** follow Sign in, Get started, or Connect if the task is the public site. Each opens `https://app.me.sh/login`. [site-tree.md](site-tree.md).

## Rebuild

```bash
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

The capture reader needs Playwright:

```bash
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/public/read.mjs
```

`catalog.json` is not updated in this PR. `make design-md` and `make brief` will not rewrite this package until an entry exists.
