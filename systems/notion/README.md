# Notion

Public marketing site for Notion, captured 2026-11-21 from [https://www.notion.com/](https://www.notion.com/). Signed out. One painted light theme. Desktop 1440 and phone 390. Log in and signup redirect to app.notion.com and were photographed empty. No email, password, or code was typed. Google, Apple, Microsoft, ChatGPT, Passkey, and SSO were not clicked.

This is a new package. `origin/main` had no `systems/notion/` folder. The task named a refresh. The folder was absent, so the capture started from the public site. Notion Calendar is [systems/cron](../cron) and is not this package.

| Path | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [site-tree.md](site-tree.md) | Which homepage control opens which page, menu, or wall |
| [login-review.json](login-review.json) | Offered nav, settings, and create, plus screens and gaps |
| [tokens.json](tokens.json) | Measured colour, type, and radius tokens |
| [DESIGN.md](DESIGN.md) | Not generated. Generating it needs a catalog entry, and this capture does not edit `catalog.json` |
| [style-guide.html](style-guide.html) | Renders the light tokens |
| [components.md](components.md) | Components seen on the public site |
| [patterns.md](patterns.md) | Homepage, pricing, walls, and the phone drawer |
| [screenshots/](screenshots/) | Public-state PNGs, 256-colour |
| [icon.png](icon.png) | 128 px raster of the site apple-touch icon |
| [raw/](raw/) | Computed style readings |
| [tools/](tools/) | Builders. `python3 tools/build_tokens.py` rebuilds `tokens.json` |

## Brief

Not generated. `make brief` reads the catalog entry, and this capture does not edit `catalog.json`.

## Health

Not generated. `make grade` reads the catalog entry.

## How the values were read

Computed styles were read on https://www.notion.com/ into [raw/readings.json](raw/readings.json). Body background is `rgb(255, 255, 255)`. Body text is `rgba(0, 0, 0, 0.95)`. The header Get Notion free fill is `rgb(0, 117, 222)` with a white label, 8px radius, 16px weight 500, 36px tall. The homepage h1 is 96px, weight 600, line-height 100px, letter-spacing -4.6px, family NotionInter then Inter.

The login wall on app.notion.com uses a different blue for Continue: `rgb(35, 131, 226)`. That value is tokenised as `light.color.login-accent` and is not the marketing accent.

The site declares about 1194 custom properties. A short sample is in the readings file. Semantic roles above were read from computed styles on visible controls, not assigned from that sample.

The apple-touch icon is `https://www.notion.com/front-static/logo-ios.png`, resized to 128 px.

## What to distrust

The marketing site paints light only. `prefers-color-scheme: dark` left `color-scheme` at `normal` and the body at white. There is no dark token set.

The homepage headline rotates words inside a pill (Think, Ship). Two shots of the same URL can differ. The h1 size was read on "Where teams and agents Think together."

`/product/all-features` and `/a-new-shape-for-work` returned 404 on 2026-11-21. Do not treat those shots as product pages.

The homepage product mock is a marketing demo of a Ramp workspace. It is not a signed-in capture.

Login Continue is a different blue from the marketing button. Do not unify them.

Screenshots are 256-colour PNGs. Read colours from `tokens.json`.

## Fonts

NotionInter, then Inter, is the family painted on www.notion.com. The login wall paints Inter without NotionInter. The webfont files were not copied. Tokens name the families the site paints.

## Coverage

| Item | Status |
|---|---|
| Colour roles, light | Captured. [tokens.json](tokens.json) `light` |
| Colour roles, dark | Not captured. No public theme toggle. Dark preference still paints light |
| Type scale | Captured from computed h1, body, and button |
| Spacing | Captured as button padding only. No named scale |
| Radii | Captured. Buttons are 8px. Nav triggers are 4px |
| Elevation | Not present as a shadow scale on the measured controls |
| Motion | Not captured. No named duration scale was read |
| Button | Captured. Default, hover, focus. [screenshots/home-light-default.png](screenshots/home-light-default.png) |
| Link, nav | Captured. Header links and click menus |
| Menu | Captured. Product and Resources dropdowns, phone drawer |
| Dialog | Captured. Singapore report card. Not dismissed |
| Text field | Captured empty. Login and contact-sales. Not typed |
| Cookie banner | Not present on these loads. Cookie settings is a footer control and was not opened |
| Login wall | Photographed, not submitted. [screenshots/login-light-default.png](screenshots/login-light-default.png) |
| Signup wall | Photographed, not submitted. [screenshots/signup-light-default.png](screenshots/signup-light-default.png) |
| Demo request | Photographed, not submitted. [screenshots/contact-sales-light-default.png](screenshots/contact-sales-light-default.png) |
| Signed-in app, settings, create | Not present on the public site |
| Checkbox, radio, switch, select, toast, table, avatar | Not present on the pages photographed |
| Phone 390 | Captured. Home, drawer, and pricing |

## Do and don't

- **One blue for marketing actions.** Get Notion free is `#0075de` with an 8px corner. Secondary pricing actions are the pale `#e6f3fe` fill. See [screenshots/home-light-default.png](screenshots/home-light-default.png) and [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png).
- **Menus open on click.** Product and Resources are `button.HWB10a_dropdownTrigger`. Hover left them closed in this session. See [screenshots/site-tree/desktop-menu-product.png](screenshots/site-tree/desktop-menu-product.png).
- **Keep the login blue separate.** Continue on app.notion.com is `#2383e2`. See [screenshots/login-light-default.png](screenshots/login-light-default.png).
- **Stop at the email wall.** Do not type an address and do not click Google, Apple, Microsoft, ChatGPT, Passkey, or SSO. See [screenshots/signup-light-default.png](screenshots/signup-light-default.png).
- **The phone primary action is black.** Request a demo in the drawer is a black pill, not the desktop blue. See [screenshots/home-light-mobile-menu.png](screenshots/home-light-mobile-menu.png).

## Rebuild

```bash
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

`build_tokens.py` reads `raw/readings.json` and writes `tokens.json`. `build_style_guide.py` writes `style-guide.html` from `tokens.json`. Edit the readings or the builders, never the generated files.
