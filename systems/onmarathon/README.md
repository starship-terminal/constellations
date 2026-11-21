# On Marathon design reference

A token set and component reference for the public archive at [onmarathon.com](https://onmarathon.com/). Captured on 2026-11-21, signed out, in headless Chromium. Desktop is 1440 by 900 at 1x. Phone is 390 by 844 at 2x. The live site paints one light theme (`html.light`).

The site is an archive of Marathon, a former Figma comment tool. Sign In and Get Started redirect to the homepage and show no form. The control map is [site-tree.md](site-tree.md).

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site icon, 128 px PNG, fetched from onmarathon.com |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds colour, type, radius, space and motion. `light` holds the painted roles. Every token has `$extensions.source`. Dark class values sit on colour tokens as `darkProbe` and are not a theme set |
| [DESIGN.md](DESIGN.md) | Hand-written from the tokens and this README, because catalog.json was not edited and `make design-md` was not run. One theme, no provenance |
| [style-guide.html](style-guide.html) | Renders the tokens and a small shell mock |
| [components.md](components.md) | Measured controls, crops, shared values, and gaps |
| [patterns.md](patterns.md) | How the pages combine: shell, letter, pricing, demo, curated, 404 |
| [site-tree.md](site-tree.md) | Which control opens which page, menu, or stopped branch |
| [components/crops/](components/crops) | Element screenshots, `{component}-{state}.png` |
| [screenshots/](screenshots) | `{page}-light-{state}.png`. `mobile-` is 390. `-full` is the whole page. `-menu-open` is the phone nav. `-monthly` is the pricing toggle |
| [raw/](raw) | [css-vars.json](raw/css-vars.json) and [components-computed.json](raw/components-computed.json) |
| [tools/](tools) | Builders and the adapted capture kit. `vars.mjs`, `public/public.mjs`, `public/measure.mjs`, `build_tokens.py` and `build_style_guide.py` were run. The signed-in, electron and native kit copies were not run |

## Brief

<!-- brief:start -->
The package is not in catalog.json. This capture was told not to edit that file, so Brief cannot be generated. Read tokens.json.
<!-- brief:end -->

## Health

<!-- health:start -->
No scorecard row. The package is not in catalog.json, by instruction. Health cannot be generated until a later commit registers it.
<!-- health:end -->

## How the values were read

Headless Playwright, signed out, on 2026-11-21.

- **Tokens.** [tools/capture/vars.mjs](tools/capture/vars.mjs) read the same-origin Next stylesheets and resolved each custom property on a probe. `html.light` is the live theme. A second probe added class `dark` and removed `light`. That probe is labelled on each colour token and is not a theme set. One sheet, the Choc Chip cookie CSS on jsDelivr, is cross-origin and was fetched with curl. No cookie banner mounted, so those colours are not tokens.
- **Components.** [tools/capture/public/measure.mjs](tools/capture/public/measure.mjs) read `getComputedStyle` for default, hover, keyboard focus and a CDP `:active` state. The phone menu was opened with its own button. The pricing toggle was clicked only to change the local price. Nothing was submitted.
- **Screenshots.** [tools/capture/public/public.mjs](tools/capture/public/public.mjs) wrote full-colour shots under `~/.design-systems/onmarathon/raw-shots`, with `.capture.json` sidecars. [tools/capture/quantize.py](tools/capture/quantize.py) made the 256-colour copies in `screenshots/`.
- **Colour hex.** oklch custom properties were converted in a canvas `fillStyle` read, then checked against the builder. `--primary` is already `#d7fd51`.

No password, code, captcha, Google or Apple button, profile field, or form was touched.

## What to distrust

- **One painted theme.** Screenshots are light. `darkProbe` on a colour token is a forced class, not a page anyone can open from the nav.
- **oklch to hex.** The builder converts oklch the same way the canvas probe did. A later browser can round a chroma colour differently. `#d7fd51`, `#ffffff` and `#404040` were read as sRGB and do not depend on that conversion.
- **Focus ring.** Desktop keyboard focus is Chromium's `#005fcc` auto outline. The phone menu button drew `rgb(229, 151, 0)` in the same browser's mobile context. Neither is a site token.
- **`--destructive` is unused** on the captured pages. It is a declared variable, not a painted state.
- **The demo iframe** was still a spinner in the viewport shot. Do not treat that white card as the scheduler's design.
- **Quantised screenshots.** Read colours from tokens.json, not from `screenshots/`.
- **Wordmark states.** Only the resting wordmark was measured. The first locator matched the banner.

## Fonts

Inter, weights 100 to 900, from the Next font files, with an "Inter Fallback" that maps to Arial. graphik, weights 400 and 500, also from Next font files, used on the display heading. The webfonts are not committed. The guide falls back to system-ui.

## Coverage

| Checklist item | Status |
|---|---|
| Colour roles, light | Captured. [tokens.json](tokens.json) `light`. Banner, text, muted, button, border |
| Colour roles, dark | Not captured as a live theme. `.dark` exists in CSS and has no public switch. Values are `darkProbe` |
| Type | Captured. Display, body, label, caption in `core.typography`. [components/crops/heading-default.png](components/crops/heading-default.png) |
| Spacing | Captured as measured padding steps in `core.space`. No published spacing scale beyond those readings |
| Radii | Captured. `17.6px` cards, `9999px` controls |
| Borders | Partly. `--border` is declared. No captured control paints a 1px border in that colour |
| Elevation | Not present. Plan cards and the header have no box-shadow |
| Motion | Captured. 150ms, cubic-bezier(0.4, 0, 0.2, 1) on links and Get Started |
| Sizing | Captured. Button 40px, menu button 40px, banner 44px, header 56px observed |
| Layout | Captured at 1440 and 390. Content width is the page. No breakpoint tokens |
| Button | Captured. [components/crops/button-primary-default.png](components/crops/button-primary-default.png), hover, focus, pressed |
| Icon button | Captured. Phone menu button. [components/crops/menu-button-default.png](components/crops/menu-button-default.png) |
| Link | Captured. Nav, sign-in, footer |
| Text field, text area, select, checkbox, radio, switch | Not present on the public pages |
| Tabs | Not present. The billing control is two buttons, not tabs |
| Menu | Captured. Phone nav. [screenshots/mobile-home-light-menu-open.png](screenshots/mobile-home-light-menu-open.png). Desktop has no dropdown |
| Tooltip, dialog, toast | Not present. The demo iframe's empty dialog node was opacity 0 |
| Card | Captured. [components/crops/plan-card-default.png](components/crops/plan-card-default.png), [components/crops/plan-card-pro-default.png](components/crops/plan-card-pro-default.png) |
| List row, table, avatar | Not present |
| Badge | Captured. [components/crops/badge-default.png](components/crops/badge-default.png) |
| App shell | Captured. [screenshots/home-light-default.png](screenshots/home-light-default.png) |
| Form with validation | Not present. Sign-in and register redirect home. Demo embed not filled |
| Empty, loading, error | Error page captured. [screenshots/notfound-light-default.png](screenshots/notfound-light-default.png). No empty or loading app state. Demo spinner is a third-party embed |
| Destructive confirmation | Not present |
| Feedback after an action | Not present. The pricing toggle is the only in-page action, and it only changes a price |
| Search and filtering | Not present |
| List or table | Not present |
| Onboarding | Not present. Register redirects home |
| Desktop 1440 and phone 390 | Captured. Sidecars record innerWidth 1440 and 390 |

## Do and don't

- **Do keep the page quiet.** The homepage is a letter on a grey-white ground. One black pill is the action. [screenshots/home-light-default.png](screenshots/home-light-default.png)
- **Do use the lime once per band.** The banner and the Pro card share `#d7fd51`. Body sections stay white or grey. [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png)
- **Do set display type in graphik at a tight line height.** The h1 is 81.4px on 81.4px. [components/crops/heading-default.png](components/crops/heading-default.png)
- **Don't invent a theme switch.** The live pages are `html.light`. The `.dark` rule is not a screen. [screenshots/home-light-default.png](screenshots/home-light-default.png)
- **Don't follow Sign In or Get Started into a form.** Both URLs redirect to the archive homepage. [screenshots/home-light-default.png](screenshots/home-light-default.png)
- **Don't fill the demo embed.** It is a booking form. [screenshots/demo-light-default.png](screenshots/demo-light-default.png)

## Rebuild

```bash
cd systems/onmarathon
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/public/public.mjs
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/public/measure.mjs
python3 tools/capture/quantize.py ~/.design-systems/onmarathon/raw-shots
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

`make design-md` and `make brief` need a catalog.json entry. This capture was told not to add one.

## Registration gap

catalog.json and webapps-manifest.json were not edited. A capture pull request that includes catalog.json is rejected. The package will fail `make check` until a later commit registers it. That is expected.
