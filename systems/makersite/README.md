# Makersite

Public marketing site for Makersite, product lifecycle intelligence software, captured 2026-11-21 from https://makersite.io/. https://makersite.com returns HTTP 302 to that host. Signed out. One painted light theme. Desktop 1440 and phone 390. No login, signup, or identity-provider control on the homepage. Book a Demo, Watch a demo, and Contact were opened and not submitted. No email, password, or code was typed.

This is a new package. `origin/main` had no `systems/makersite/` folder. The task named a refresh. The folder was absent, so the capture started from the public site.

| Path | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [site-tree.md](site-tree.md) | Which homepage control opens which page, menu, or dialog |
| [login-review.json](login-review.json) | Offered nav, settings, and create, plus screens and gaps |
| [tokens.json](tokens.json) | Measured colour, type, and radius tokens |
| [DESIGN.md](DESIGN.md) | Not generated. Generating it needs a catalog entry, and this capture does not edit `catalog.json` |
| [style-guide.html](style-guide.html) | Renders the light tokens |
| [components.md](components.md) | Components seen on the public site |
| [patterns.md](patterns.md) | Homepage, menu, cookie, and demo-wall patterns |
| [screenshots/](screenshots/) | Public-state PNGs, 256-colour |
| [icon.png](icon.png) | 128 px raster of the site SVG icon |
| [raw/](raw/) | Computed style readings |
| [tools/](tools/) | Builders. `python3 tools/build_tokens.py` rebuilds `tokens.json` |
| [icons/](icons/) | Icon redraws |

## Brief

Not generated. `make brief` reads the catalog entry, and this capture does not edit `catalog.json`.

## Health

Not generated. `make grade` reads the catalog entry.

## How the values were read

Computed styles were read on https://makersite.io/ into [raw/readings.json](raw/readings.json). Hero and footer surface is `rgb(0, 60, 79)`. Body text is `rgb(64, 64, 64)`. The announcement bar is `rgb(222, 255, 0)`. Button label, padding, border, and focus outline were read with `getComputedStyle` on `header a.btn`. Font faces declared on the page are ArboriaMedium, ArboriaBook, and ArboriaBold. The favicon is an SVG whose rect fill is `#003C4F`.

The Borlabs cookie dialog was photographed in the first headed frame. Accept all, Accept only essential cookies, and Individual Privacy Preferences were not clicked. Later headless runs left the dialog box at height 0, so those shots hide it in a stylesheet. That hide is not a consent answer.

## What to distrust

The marketing site paints light only. There is no dark token set.

Button fill is a `linear-gradient` (`rgb(240, 243, 244)` to white), not a flat `background-color`. The token `button-fill` is the left stop. Hover did not change that computed gradient in this session.

`--wp--preset--color--primary-green` is `#70EE9C`. It is a WordPress preset, not the painted hero. It is not a token.

The Book a Demo page showed a white panel titled "Book a demo" and no fields. Do not treat that empty panel as the form.

Screenshots are 256-colour PNGs. Read colours from `tokens.json`.

## Fonts

ArboriaMedium, ArboriaBook, and ArboriaBold are declared `@font-face` families. The webfont files were not copied. Tokens name the families the site paints.

## Coverage

| Item | Status |
|---|---|
| Colour roles, light | Captured. [tokens.json](tokens.json) `light` |
| Colour roles, dark | Not captured. No public theme toggle |
| Type scale | Captured from computed h1, h2, body, and button |
| Spacing | Captured as button padding only. No named scale |
| Radii | Captured. Buttons are 0px. Content blocker is 4px |
| Elevation | Not present as a shadow scale. Button shadow is none |
| Motion | Not captured. No named duration scale was read |
| Button | Captured. Default, hover, focus. [screenshots/home-light-default.png](screenshots/home-light-default.png) |
| Link, nav | Captured. Header links and click menus |
| Menu | Captured. Five desktop menus and the phone drawer |
| Dialog | Captured. Cookie dialog. Not submitted |
| Text field | Not captured. Demo form fields did not paint |
| Cookie banner | Present, not clicked. [screenshots/site-tree/desktop-cookie-dialog.png](screenshots/site-tree/desktop-cookie-dialog.png) |
| Demo wall | Photographed, not submitted. [screenshots/demo-light-default.png](screenshots/demo-light-default.png) |
| Signed-in app, settings, create | Not present on the public site |
| Checkbox, radio, switch, select, toast, table, avatar, badge | Not present on the pages photographed, except the cookie checkboxes |
| Phone 390 | Captured. Home, pricing, and the drawer |

## Do and don't

- **Teal hero, square white button.** The page surface is `#003c4f`. Primary actions are square, not pills, with a `#003c4f` label. See [screenshots/home-light-default.png](screenshots/home-light-default.png).
- **Menus open on click and carry a lime panel.** Hover leaves the submenu `display: none`. The open panel uses `#deff00`. See [screenshots/site-tree/desktop-menu-what-is.png](screenshots/site-tree/desktop-menu-what-is.png).
- **One type family, three cuts.** Display and body are ArboriaMedium. Buttons are ArboriaBold. See [screenshots/home-light-default.png](screenshots/home-light-default.png).
- **Stop at Book a Demo.** That page is a demo wall. Do not submit it. See [screenshots/demo-light-default.png](screenshots/demo-light-default.png).
- **Answer the cookie dialog yourself.** Accept all and Accept only essential cookies were not pressed. See [screenshots/site-tree/desktop-cookie-dialog.png](screenshots/site-tree/desktop-cookie-dialog.png).

## Rebuild

```bash
cd systems/makersite && python3 tools/build_tokens.py && python3 tools/build_style_guide.py
```

`DESIGN.md` is not rebuilt here. `make design-md` writes it from the catalog, and this capture does not edit `catalog.json`.
