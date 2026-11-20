# Monarch Money design reference

Public marketing site for Monarch Money, captured from www.monarch.com on 2026-11-21. `https://www.monarchmoney.com/` redirects there. Signed out. One light theme. Desktop 1440 x 900 at 1x and phone 390 x 844 at 2x. The product app at `https://app.monarch.com/login` asks for a password and was not entered.

The site paints parchment (`#fdf8ed`) with charcoal text (`#22201d`) and a monarch orange button (`#f35b16`). Display type is ABC Otto. Body and UI type is ABC Oracle. A 12-step Radix-style ramp exists for gray, orange, blue, green, red, yellow, indigo, pink, and purple, plus named brand stops (evergreen, goldenrod, wheat, walnut, and others).

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Which control opens which page, menu, dialog, or wall, mapped before screenshots |
| [icon.png](icon.png) | Site icon, 128 px, from the apple touch icon |
| [tokens.json](tokens.json) | DTCG tokens: `core` ramps, type, fonts; `light` roles. `dark` is empty |
| [DESIGN.md](DESIGN.md) | Generated from tokens.json and this README |
| [style-guide.html](style-guide.html) | Renders the light roles, ramps, and type |
| [components.md](components.md) | Public controls and the states that were reached |
| [patterns.md](patterns.md) | Header, hero, pricing, FAQ, blog, calculators |
| [screenshots/](screenshots) | 100 quantised PNGs, `{page}-light-{state}.png`. Viewport shots plus stitched full pages. `mobile-about-light-full` was dropped: the stitch grew without bound |
| [raw/](raw) | [css-vars.json](raw/css-vars.json), [components-computed.json](raw/components-computed.json), [sitemap-paths.txt](raw/sitemap-paths.txt), [capture/](raw/capture) viewport sidecars |
| [tools/](tools) | Capture scripts and the token and style-guide builders |

## Brief

<!-- brief:start -->
Read [tokens.json](tokens.json). The public site has one light theme.

Page `#fdf8ed` (`light.page`). Text `#22201d` (`light.text`). Accent token `#ff692d` (`light.accent`). Painted button `#f35b16` (`light.button`). Border `#dcd9d6` (`light.border`). Muted text `#777573` (`light.muted`).

Fonts: ABC Oracle, ABC Otto, Copernicus, Beltram Mono. The files are not in this package.
<!-- brief:end -->

## Health

<!-- health:start -->
Not graded in this capture. catalog.json was not edited, so `make grade` was not run for this package.
<!-- health:end -->

## How the values were read

[tools/capture/vars.mjs](tools/capture/vars.mjs) read every stylesheet on the homepage through the CSSOM and wrote [raw/css-vars.json](raw/css-vars.json). 457 names resolved. 309 are product tokens, 146 are Osano consent variables (left out of tokens.json), 72 are Tailwind internals. [tools/build_tokens.py](tools/build_tokens.py) maps the resolved colours and the `--type-*` roles into tokens.json.

Button fill, hover, focus ring, and control heights were read with `getComputedStyle` on the live header and written to [raw/components-computed.json](raw/components-computed.json). Screenshots came from [tools/capture/public/shoot.mjs](tools/capture/public/shoot.mjs) and were quantised by [tools/capture/quantize.py](tools/capture/quantize.py).

The cookie banner was hidden with CSS. Accept All, Reject Non-Essential, and Save were not clicked. No form was submitted. No password, code, or profile field was typed.

## What to distrust

- `--primary` resolves to `#ff692d`. The painted Sign up button is `#f35b16` (`--monarch-orange`). Use `light.button` for the control and `light.accent` for the declared primary.
- The homepage hero video fails in headless Chromium and shows a Media Error overlay. That is a capture limit, not the designed hero.
- Screenshots are 256-colour PNGs. Read colours from tokens.json.
- ABC Oracle, ABC Otto, Copernicus, and Beltram Mono are not loaded in the style guide. Specimens fall back to system fonts.
- Radii, spacing, and elevation were not declared as custom properties. The pill radius `9999px` and the 36px / 48px heights are measurements, not a scale. They are not tokens.
- Letter-spacing on the type roles is in raw/css-vars.json as a raw string and is Not captured as a token.
- `--link`, several `--theme-*-link` names, and `--duration` did not resolve. Not captured.
- No dark theme was painted. `color-scheme` was `normal`.

## Fonts

Declared in raw/css-vars.json: ABC Oracle (300, 350, 500, 700, with italics), ABC Otto (400, 500), Copernicus (400, 500), Copernicus Book (500), Beltram Mono (400). Proprietary. Not committed. Fallbacks in the tokens are the stacks the CSS variables name (`sans-serif`, `serif`, `ui-monospace`).

## Coverage

| Item | Status |
|---|---|
| Colour roles, light | Captured. [tokens.json](tokens.json) `light` |
| Colour ramps | Captured. `core.color` |
| Dark theme | Not present on the public site |
| Type roles | Captured. `core.typography` from `--type-*` |
| Spacing scale | Not captured. No spacing custom properties |
| Radii | Not captured as a scale. Pill radius measured at 9999px on the header buttons |
| Elevation | Not captured as tokens. Header shadow measured in components-computed.json |
| Motion | Not captured. `--duration` did not resolve |
| Button, link, menu, tabs, card, FAQ | Captured. See [components.md](components.md) |
| Text field, select, checkbox | Observed, not filled |
| Text area, radio, switch, tooltip, toast, table | Not present on the captured public pages |
| Dialog | Cookie banner recorded and hidden. Fee dialog Not captured |
| Pressed, disabled, loading, error | Not captured |
| Signed-in app, onboarding, signup | Not captured. Walls listed in [site-tree.md](site-tree.md) |
| Desktop 1440 and phone 390 | Captured. Sidecars record innerWidth 1440 and 390 |

## Do and don't

- **Do paint the page parchment and the primary button monarch orange.** The body is `#fdf8ed` and the Sign up control is `#f35b16`. [screenshots/home-light-default.png](screenshots/home-light-default.png)
- **Do keep the header a white pill on the parchment page.** [screenshots/home-light-default.png](screenshots/home-light-default.png)
- **Do set display headlines in a serif (ABC Otto) and UI labels in ABC Oracle.** [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png)
- **Don't treat `#ff692d` as the button fill.** That is `--primary`. The painted button is `#f35b16`. [raw/components-computed.json](raw/components-computed.json)
- **Don't invent a dark theme.** The public site does not ship one.
- **Don't follow Sign in or Sign up into the app.** Those URLs are login and signup walls.

## Rebuild

```bash
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/public/shoot.mjs
python3 tools/capture/quantize.py ~/.design-systems/monarchmoney/raw-shots
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

Run the node commands from `systems/monarchmoney` only after `PLAYWRIGHT` is set. The shoot script writes full-colour PNGs under `~/.design-systems/monarchmoney/raw-shots`.
