# Sunsama design reference

A token set and component reference for Sunsama's public marketing site, for building a calm daily-planning marketing page in that style. It was read from www.sunsama.com on 2026-11-21, signed out, in headless Chromium at 1440x900 and 390x844. The public site paints one light theme: warm grey page `#fafafa`, ink `#202228` in DM Sans, and one orange action colour `#ff891c` on the Start for Free buttons. The signed-in app was not entered.

Login at https://app.sunsama.com/login and signup at https://www.sunsama.com/start/signup are stop branches. No email was typed, no form was submitted, and Google, Outlook, and SSO were not clicked. Termly consent was hidden, never accepted. Dark app colours exist in the public CSS under `.sslab[data-theme="dark"]` and are tokenised. The marketing pages do not paint that attribute, so those values are declared CSS, not a live captured theme.

| File | What it is |
|---|---|
| [icon.png](icon.png) | The site apple-touch icon, resized to 128 px PNG. `tools/fetch_icon.py` needs a catalog entry, and this capture does not edit catalog.json, so the icon was fetched from the page's apple-touch URL and resized with `sips`. |
| [tokens.json](tokens.json) | W3C DTCG tokens in Tokens Studio's multi-set layout: `core` (33: marketing colour literals, the Avenir app stack and leading, radius and text sizes, column and calendar sizes, three shadows), `light` (32) and `dark` (32). Marketing roles are the same in both sets. App roles differ. Every token carries `$extensions.source`. |
| [DESIGN.md](DESIGN.md) | A hand export in Google's DESIGN.md format, written because `make design-md` reads catalog.json and this capture must not edit that file. It holds the light theme and no provenance. Take values from tokens.json. |
| [style-guide.html](style-guide.html) | One self-contained page that renders the marketing swatches, the app roles, and a theme toggle for the declared dark app tokens. |
| [components.md](components.md) | 26 measured components, crops of the real product, shared values, and the Gaps. |
| [patterns.md](patterns.md) | How the components combine: the flat nav, the home hero, pricing, compare, the signup wall, and the phone fold. |
| [components/](components) | `crops/`: 69 element screenshots, `{component}-{state}.png`. |
| [screenshots/](screenshots) | 60 `{page}-light-{state}.png` captures. Desktop shots are 1440 wide. Phone shots are 390 wide at 2x. |
| [raw/](raw) | Unprocessed readings: `css-vars.json`, `components-computed.json`, and `full/` (unquantised captures plus `.capture.json` sidecars). |
| [site-tree.md](site-tree.md) | Which control opens which page, menu, dialog, or stop branch. Mapped before the screenshot pass. |
| [tools/](tools) | The builders and the Playwright capture kit. See Rebuild. |

## Brief

<!-- brief:start -->

Not generated. `make brief` reads catalog.json, and this capture does not edit that file. Read How the values were read, Coverage, and Do and don't before using a value.

<!-- brief:end -->

## Health

<!-- health:start -->

Not generated. `make grade` reads catalog.json, and this capture does not edit that file. `make check` will fail until a later change registers the package.

<!-- health:end -->

## How the values were read

www.sunsama.com is a Webflow marketing site. Desktop nav is a flat bar (`.navbar`). There is no hover flyout. Phone width hides that bar and shows `.menu-button-2`, which opens `.w-nav-overlay`.

[vars.mjs](tools/capture/vars.mjs) harvested declared custom properties from the live home page. Marketing colours sit on `:root` (`--bg-light-grey-new`, `--black`, `--ss-orange`, `--blue`, and the border names). App demo colours sit on `.sslab` as `--ss-*`, and again on `.sslab[data-theme="dark"]`. The probe shell includes `#probe-sslab` so those names resolve. A name that resolved empty was omitted. Termly's variable is stored under vendor in `raw/css-vars.json` and is not a design token.

[build_tokens.py](tools/build_tokens.py) copies those resolved values into `tokens.json`. It does not invent a missing step. `--ss-text-5` is not declared, so the size scale jumps from `text-4` (16px) to `text-6` (20px). The stylesheet spells `--ss-dark-organge`. That spelling is kept in the source note. The token name is `core.color.orange-deep`.

Component values are computed styles from [measure.mjs](tools/capture/public/measure.mjs). Hover used the pointer. Focus-visible used keyboard Tab. Pressed was forced. The signup email field was focused and not typed. Login, Google, Outlook, and SSO were not clicked. Newsletter and search fields were not filled. Termly was hidden in [lib.mjs](tools/capture/public/lib.mjs) by a class match. Accept and Preferences were not clicked.

Screenshots came from [public.mjs](tools/capture/public/public.mjs) at 1440x900 (device scale 1) and 390x844 (device scale 2), then `python3 tools/capture/quantize.py` wrote 256-colour PNGs into `screenshots/`.

## What to distrust

- Screenshots are 256-colour PNGs. Read colours from tokens.json or `raw/components-computed.json`.
- The dark set is declared CSS on `.sslab[data-theme="dark"]`. No public control paints it. Marketing `page`, `text`, and `accent` are the same hex in `light` and `dark` because those names live on `:root`.
- `--ss-*` app colours are the embedded demo layer, not the painted marketing page. A marketing screen should use `light.page`, `light.text`, and `light.accent`.
- Nav link hover and pressed did not change computed colour. Do not invent a hover ink.
- `cta-primary` focus-visible did not paint an outline. `nav-cta` did (1px auto `#005fcc`). They are different controls.
- `m-menu-open` measured 390x15787. The crop is the overlay box, not a short sheet. The phone menu screenshot is [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png).
- `footer-link` is the first footer anchor (a social icon, 47x17). It is not a text link style.
- `lightbox-link` states other than default are Not captured. The trigger is an image, so a text filter missed it on the first pass.
- `ai-tab` click timed out. Default, hover, pressed, and selected were measured. Opening a different assistant tab was not.
- Footer mailto and community-invite URLs were not copied into this package.

## Fonts

| Family | Where it was read | Used for |
|---|---|---|
| DM Sans | Computed on `.navbar`, `.headlinemain`, buttons. Served from Google Fonts. | Marketing UI and headlines. Hero title is 51.2px / 600. |
| Avenir | `--ss-font`, and computed on the price card, compare tab, and signup field. Eight `@font-face` rules in sunsama.css. | App demo and some marketing cards. |
| Outfit | Computed on the signup title (56px / 500) and the opened demo panel. | Signup wall display. |
| Inter, Inconsolata | `@font-face` only. Not measured on the captured controls. | Not captured as a used face. |
| webflow-icons | Icon font in sunsama.css. | Webflow glyphs. Not extracted as SVG. |

DM Sans is a webfont. Avenir is served from the site's own `/fonts/` paths. No font file is committed. The style guide falls back to a system sans.

## Coverage

| Expectation | Status | Where |
|---|---|---|
| Marketing page, surface, text, accent, border | Measured | `light.page` `#fafafa`, `light.surface` `#f6f5f1`, `light.text` `#202228`, `light.accent` `#ff891c`, `light.border` `#e5e4e0` |
| App demo colours, both declared themes | Measured as CSS | `light.app.*` and `dark.app.*` from `.sslab` and `.sslab[data-theme=dark]` |
| Live dark marketing theme | Not captured | No public toggle. `color-scheme` is `normal`. |
| Type sizes | Measured | `core.size.text-1` through `text-4` and `text-6`. `text-5` is not declared. |
| Radius | Measured | 2, 4, 10, 100 px on `--ss-radius-*`. Marketing buttons paint 30px in computed style, which is not one of those tokens. |
| Elevation | Measured | `core.shadow.card`, `.button`, `.modal` |
| Spacing scale | Not captured | Padding is per component. No `core.spacing` tokens. |
| Motion durations | Observed | Sheet transitions in `raw/components-computed.json` `_meta.sheets`. Not tokenised. Reduced-motion behaviour is Not captured. |
| Desktop 1440 and phone 390 | Measured | [screenshots/](screenshots) |
| Nav, CTA, AI panel, price card, FAQ, compare tab, demo, signup field, footer, phone menu | Measured | [components.md](components.md) |
| Login form, Google, Outlook, SSO | Not captured | Stop branch. Recorded in [site-tree.md](site-tree.md). |
| Newsletter, search, blog subscribe | Not captured | Fields were not filled. Forms were not submitted. |
| Individual blog posts, pro-tip articles, affiliate `/a/` pages | Not captured | Sitemap lists them. Indexes were captured. Articles were not walked. |
| Signed-in app | Not captured | Behind the login wall. |
| Icons as SVG | Not captured | No `icons/` folder. |

## Do and don't

1. **Do use one orange for the primary action.** `#ff891c` fills Start for Free. Hover and pressed darken to `#db7414`. See [nav-cta-default](components/crops/nav-cta-default.png) and [nav-cta-hover](components/crops/nav-cta-hover.png).
2. **Do set marketing type in DM Sans.** The hero is 51.2px weight 600, line-height 59.4px, ink `#202228`, on `#fafafa`. See [hero-title-default](components/crops/hero-title-default.png) and [home-light-default](screenshots/home-light-default.png).
3. **Do keep the nav flat.** Links do not open a menu. Phone width replaces them with the overlay. See [header-default](components/crops/header-default.png) and [mobile-home-light-menu](screenshots/mobile-home-light-menu.png).
4. **Don't treat the dark tokens as a captured marketing theme.** They are `.sslab[data-theme=dark]` declarations. The public pages stay light.
5. **Don't invent a nav-link hover colour.** Computed colour stayed `rgb(32, 34, 40)` on hover and pressed.
6. **Don't fill the signup field or follow Login.** Both are stop branches. The field crop is focus only. See [signup-light-wall](screenshots/signup-light-wall.png).

## Rebuild

From `systems/sunsama`:

```bash
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

`build_tokens.py` reads `raw/css-vars.json` and writes `tokens.json`. `build_style_guide.py` writes `style-guide.html` from `tokens.json`. `tools/build_components_md.py` is still the shared kit and expects a different raw shape. Do not run it. `components.md` was written from `raw/components-computed.json`.

```bash
PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/public/public.mjs
python3 tools/capture/quantize.py raw/full
PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/vars.mjs
PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/public/measure.mjs
```

Run those from `systems/sunsama`. `public.mjs` writes `raw/full`. Quantize copies 256-colour PNGs to `screenshots/`.

## Catalog

This folder is not in catalog.json. A capture pull request that edits catalog.json is rejected. Register it in a later change, then run `make design-md`, `make brief`, and `make grade`.
