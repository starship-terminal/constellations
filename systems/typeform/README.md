# Typeform design reference

A token set and component reference for Typeform's public marketing site. Read from [https://www.typeform.com/](https://www.typeform.com/) on 2026-11-21, signed out, in headless Chromium at 1440x900 and 390x844. The site paints one light theme. The header and menus invert to a dark plum. The form builder, results, and account settings sit behind [https://admin.typeform.com/login](https://admin.typeform.com/login) and were not entered.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Typeform apple-touch icon, resized to 128 px PNG |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds the declared colour ramps, type roles, spacing and radii. `light` holds semantic aliases. No dark set. Every token carries `$extensions.source`. |
| [style-guide.html](style-guide.html) | Renders the light tokens and the main controls |
| [components.md](components.md) | Component inventory with 23 crops |
| [patterns.md](patterns.md) | How the shell, menus, pricing, preview dialog and login wall fit together |
| [site-tree.md](site-tree.md) | Which control opens which public page, menu, or auth wall |
| [components/](components) | `crops/`: 23 element screenshots of buttons, nav, billing toggle, hero and menu |
| [screenshots/](screenshots) | 80 captures. Desktop 1440x900 at 1x. Phone shots are 390x844 at 2x (780 px wide). |
| [raw/](raw) | Stylesheet harvest, computed component styles, and 82 screenshot sidecars |
| [tools/](tools) | Capture scripts and the builders |

## Brief

Not generated. `make brief` writes this section from a catalog entry, and this capture was told not to edit `catalog.json`.

## Health

Not generated. `make grade` writes this section from a catalog entry and a scorecard snapshot. Neither was produced for this capture.

## How the values were read

Custom properties were read from the public Webflow stylesheet `typeform-website.webflow.shared.*.min.css` on `cdn.prod.website-files.com`. The sheet is cross-origin, so [tools/capture/vars.mjs](tools/capture/vars.mjs) collected it from the network response, parsed it in a headless page, and resolved each name on a probe element. The harvest is [raw/css-vars.json](raw/css-vars.json).

Semantic colours (`--tokens--*`), primitive ramps (`--_colour-primitives---primitives--*`), type roles (`--_typography---*`) and spacing (`--_size-and-spacing---*`) are declared values. Control heights, the menu shadow and the hero's 80px size are computed styles from [raw/components-computed.json](raw/components-computed.json).

Screenshots were taken with Playwright at a measured `innerWidth` of 1440 and 390. Sidecars in [raw/](raw) record the viewport. The OneTrust banner was hidden with CSS. No consent button was clicked. No form was submitted. Google, Microsoft, Apple, Facebook and SSO were not clicked.

## What to distrust

- This is the marketing site, not the product. The builder is behind login.
- There is no dark theme to switch. The dark header is an inverted surface in the light theme, stored as `light.invert`.
- Font weight on buttons computed to 400 even when the family token is named "Twklausanne 500". Role weights are Derived from that name.
- Focus outline computed to none after keyboard focus landed. Do not invent a focus colour.
- Screenshots are 256-colour PNGs. Read colours from tokens.json.
- Deleted Webflow variable names (containing `<deleted|`) were ignored.
- The action-text-xs letter-spacing and line-height declarations in the sheet look swapped. They were not tokenised.
- On the pricing cards, Growth Flow's struck-through trial price sits on top of the current price for a moment after the Monthly / Yearly click. [pricing-light-yearly.png](screenshots/pricing-light-yearly.png) and [pricing-light-monthly.png](screenshots/pricing-light-monthly.png) show that overlap (`266 0` and `379 0`). The prices underneath are the page's own text. A second wait of 2.8 seconds still caught the overlay.
- Phone menu sections (Platform, Solutions, Resources) were photographed closed. Desktop menus were photographed open.

## Fonts

**Tobias** is the display face (declared `--_typography---heading-display-font`). **Twklausanne** is the UI face. **Apercu Mono** is in `@font-face` rules and was not seen on the captured controls. None of these faces is distributed with the package. The style guide falls back to Times New Roman and Arial.

## Coverage

| Item | Status |
|---|---|
| Colour roles | Captured in [tokens.json](tokens.json) `light` and the primitive ramps in `core.color`. Overlay and scrim are Not captured. Status colours are the declared green, yellow and red ramps, not painted as form validation. |
| Type | Captured. Display, headings, body, label, caption. Code face Not captured in use. |
| Spacing, radii | Captured from `--_size-and-spacing---*`. |
| Elevation | One menu shadow, measured. No 5-level scale was declared. |
| Motion | Not captured. No duration or easing custom properties in the harvest. |
| Sizing | Button height 40px and nav item height 88px measured. Icon sizes Not captured. |
| Layout | Content widths and section padding captured. Breakpoints Not captured as tokens. |
| Button | Captured. Default, hover, focus-visible. Pressed, disabled, loading Not captured. |
| Link | Captured (Log in). |
| Text field | Visible on the login wall. Not filled. Values Not captured. |
| Text area, select, checkbox, radio, switch | Not present on the captured public pages. |
| Tabs | Billing Monthly/Yearly captured in screenshots. |
| Menu | Captured. Desktop hover menus and the phone menu. |
| Tooltip | Pricing info buttons exist. Not captured as a measured component. |
| Dialog | Template preview captured. Cookie preference centre present and not opened. |
| Toast, table, avatar, badge | Not captured. NEW pills are visible in the Platform menu screenshot. |
| App shell | Public marketing shell captured. Product shell behind login. |
| Form validation, empty, loading, error, destructive confirm | Not captured. Behind login, or not shown on public pages. |
| Themes | Light only. No dark toggle. |
| Widths | 1440 and 390, measured in the sidecars. |
| Icons | Not captured as SVG. The mark is on [icon.png](icon.png) and in the screenshots. `icons/` is absent. |
| DESIGN.md | Not generated. `make design-md` needs a catalog entry, and this capture was told not to edit `catalog.json`. |
| Catalog | `catalog.json` and `webapps-manifest.json` were not edited. `make check` will fail on a missing catalog entry until a later change registers the package. |

## Do and don't

**Do invert the header.** The page is warm off-white and the header is plum `#2a222b` with light text. [home-light-default.png](screenshots/home-light-default.png)

**Do use plum for the main button, purple only as a highlight.** Sign up is white on the dark header. Eyebrows and NEW badges use `#9454ab`. [home-light-platform-menu.png](screenshots/home-light-platform-menu.png)

**Do set display type in Tobias, tight.** The hero is a large serif line, not the UI sans. [hero-heading-default.png](components/crops/hero-heading-default.png)

**Do open Platform, Solutions and Resources on hover.** They are full-width menus, not small popovers. [home-light-solutions-menu.png](screenshots/home-light-solutions-menu.png)

**Don't style the form builder from this package.** The builder is behind login. [login-light-default.png](screenshots/login-light-default.png)

**Don't invent a focus ring.** Keyboard focus landed and the outline computed to none.

## Rebuild

```bash
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/public/measure.mjs
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/public/public.mjs
python3 tools/capture/quantize.py ~/.design-systems/typeform/raw-shots
python3 tools/build_tokens.py && python3 tools/build_style_guide.py
```

Run the last two from `systems/typeform`.
