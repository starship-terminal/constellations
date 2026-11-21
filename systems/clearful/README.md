# Clearful design reference

A token set and component reference for Clearful's public site. Clearful is a journaling app. This package was read from [clearful.com](https://clearful.com/) and [support.clearful.com](https://support.clearful.com/) on 2026-11-21, signed out, in headless Chromium at 1440 x 900 and 390 x 844. The app at [app.clearful.com/#/sign-in](https://app.clearful.com/#/sign-in) stops at email, Apple, or Google. That wall was photographed and not passed.

The marketing site is a Webflow page with a Relume `:root` token layer: a white page, `#222` ink, Manrope for UI, Literatatt for display, and one blue (`#1953ff`) used for the pill CTA. There is no dark theme.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Clearful's site icon, 128 px, from the site's apple-touch-icon |
| [tokens.json](tokens.json) | W3C DTCG tokens: `core` (neutral and blue ramps, two font families, radii, four type styles) and `light` (page, surface, text, accent, border, plus measured component metrics). Every token has `$extensions.source` |
| [DESIGN.md](DESIGN.md) | Generated from [tokens.json](tokens.json) and this README. Written by the package because this capture does not edit [catalog.json](../../catalog.json) |
| [style-guide.html](style-guide.html) | One page that renders the tokens and the main controls |
| [components.md](components.md) | The public components, with measured values as token names, and the gaps |
| [patterns.md](patterns.md) | Shell, get-app overlay, editorial page, help center, sign-in wall |
| [site-tree.md](site-tree.md) | Which control opens which page, menu, or overlay |
| [screenshots/](screenshots) | 46 captures, `{page}-light` naming omitted: files are `{page}-{state}.png` and `mobile-*`. Desktop 1440 x 900 at 1x. Phone 390 x 844 at 2x, except the sign-in wall, which the app host paints at 1x |
| [raw/](raw) | [css-vars.json](raw/css-vars.json) (resolved `:root` properties) and [component-tokens.json](raw/component-tokens.json) (the spec the builder reads) |
| [icons/](icons) | [INDEX.tsv](icons/INDEX.tsv). Icons were not extracted as SVG |
| [tools/](tools) | Builders and the capture scripts |

## Brief

<!-- brief:start -->

Read [tokens.json](tokens.json) before designing in this style. The catalog has no Clearful entry yet, so this Brief is not the generated one.

The page is white. The action is one blue pill. Display type is Literatatt. UI type is Manrope. Do not invent a dark theme. Do not treat the sign-in wall as the product.

<!-- brief:end -->

## Health

<!-- health:start -->

Not graded. This capture does not edit [catalog.json](../../catalog.json), so `make grade` cannot write this section. Review it after the package is registered.

<!-- health:end -->

## How the values were read

The Webflow stylesheet is cross-origin, so the page CSSOM cannot list its custom properties. [tools/capture/vars.mjs](tools/capture/vars.mjs) is the kit's signed-in reader. For this capture the stylesheet was fetched from `cdn.prod.website-files.com` (`clearful.webflow.08821de8c.min.css`) and each `:root` name was resolved in a probe document. The resolved set is [raw/css-vars.json](raw/css-vars.json). Three deleted Webflow variable names remain in the file. They are listed under `deleted` and are not tokens. One of them, the deleted blue-600, is what the live CTA paints on hover (`#1b1bbc`). That hover is a measured colour, [light.accent-hover](tokens.json).

Component metrics were read with `getComputedStyle` on the live page at 1440 x 900 (`innerWidth` 1440, `innerHeight` 900, `devicePixelRatio` 1). Screenshots were taken with Playwright through [tools/capture/public/shoot.mjs](tools/capture/public/shoot.mjs) and quantised to 256 colours. Nothing was submitted. No email, password, or identity button was used.

## What to distrust

- **One theme.** No dark class and no `prefers-color-scheme` rule. Do not invent a dark set.
- **Hover blue is not a declared token.** `#1b1bbc` comes from a deleted Webflow variable that the stylesheet still references. The declared `--base-color-brand--blue-600` is `#0039e6` and is not the hover.
- **Screenshots are 256-colour.** Read colours from [tokens.json](tokens.json).
- **The get-app scrim** was measured as `rgba(0, 0, 0, 0.25)` on `.modal_get-app_background-overlay`. The panel itself paints a blue wash. Use the screenshot for the panel, the token for the overlay.
- **Phone sign-in** is 390 x 844 at 1x. The app host ignored `deviceScaleFactor: 2` and the 2x shot failed the kit's dimension check. The marketing phone shots are 2x.
- **Tall full pages** (home, what's new, terms, new-home, and a few product pages over 6000px) stay in the scratch folder, not in [screenshots/](screenshots). Viewport shots of those pages are committed.
- **Literatatt** is a self-hosted display face. The style guide falls back to a system serif. The family name is measured. The font file is not in the repo.

## Fonts

`--primary-font-family` is `Manrope, sans-serif` (Google Fonts, weights 200 to 800). `--secondary-font-family` is `Literatatt, sans-serif` (self-hosted display, used at 72px/700 on the home hero). The page also loads Inter, Lora, Prata, Muli, Tenor Sans, Petit Formal Script, and Homemade Apple. Those faces were not measured on a primary role, so they are not tokens. Licences: Manrope is SIL OFL. Literatatt's licence was not read. Do not ship the file from this package.

## Coverage

| Checklist item | Status | Where |
|---|---|---|
| Page, surface, text, muted, accent, border | captured | `light.page`, `light.surface`, `light.text`, `light.muted`, `light.accent`, `light.border` |
| Raised, overlay, scrim | captured in part | scrim is `light.scrim`. Raised and overlay roles are not declared. The get-app panel is in [home-get-app](screenshots/home-get-app.png) |
| Success, warning, danger, info | not present | no status colours on the public pages |
| Disabled, on-accent | on-accent captured | `light.on-accent`. Disabled text was not shown |
| Focus | not captured | keyboard focus on the nav pill painted no distinct ring |
| Type roles | captured | `core.typography.display`, `.body`, `.nav`, `.button` |
| Spacing scale | not present | Webflow sets padding per component. Measured padding is on `light.component` |
| Radii | captured | `core.radius` small through xlarge, plus pill 999px |
| Border widths | captured | `light.component.button.border-width` 1px, field 1px, large button halo 6px |
| Elevation | not present | measured controls have `box-shadow: none` |
| Motion | not captured | durations were not read |
| Sizing | captured | nav 72px, button 50px, large button 82px, field 60px |
| Layout | captured | 1440 and 390 screenshots. No breakpoint tokens |
| Button | captured | [components.md](components.md), [home-default](screenshots/home-default.png) |
| Link | captured | nav links in [home-default](screenshots/home-default.png) |
| Text field, text area | captured | [contact-default](screenshots/contact-default.png). Not submitted |
| Tabs | captured | [home-timeline-monthly](screenshots/home-timeline-monthly.png), [whats-new-tab-features](screenshots/whats-new-tab-features.png) |
| Menu | captured | [mobile-home-menu-open](screenshots/mobile-home-menu-open.png) |
| Dialog | captured | [home-get-app](screenshots/home-get-app.png) |
| Card | captured | [library-default](screenshots/library-default.png) |
| Badge | observed | laurels on the home hero. No token |
| Search | observed | [support-default](screenshots/support-default.png). Nothing typed |
| Icon button, select, checkbox, radio, switch, tooltip, toast, list row, table, avatar | not present | not on the public pages |
| Hover | captured | CTA hover `#1b1bbc`, measured, `light.accent-hover` |
| Pressed, disabled, loading, error | not present | not shown signed out |
| App shell | captured | [patterns.md](patterns.md) |
| Form with validation | not captured | contact form was not submitted |
| Empty, loading, error, destructive, onboarding | not present | signed out |
| Sign-in wall | captured as a boundary | [sign-in-wall](screenshots/sign-in-wall.png). Branch stopped |
| Light theme, 1440 and 390 | captured | [screenshots/](screenshots) |
| Dark theme | not present | stylesheet has no dark variant |
| Icons | not captured | [icons/INDEX.tsv](icons/INDEX.tsv). Mark is in [icon.png](icon.png) |
| Site tree | captured | [site-tree.md](site-tree.md) |

## Do and don't

- **Do keep the page white and the ink `#222`.** The secondary surface is `#f7f7f7`. Do not grey the whole page. ([home-default](screenshots/home-default.png))
- **Do use one blue pill for the action.** `#1953ff`, 999px radius, white label. Secondary actions are text links, not a second filled colour. ([home-default](screenshots/home-default.png))
- **Do set the hero in Literatatt and the UI in Manrope.** 72px/700 for the home headline, 16px Manrope for nav and buttons. ([home-default](screenshots/home-default.png))
- **Do open "start a journal" as the get-app overlay.** It is not a signup form on the marketing host. ([home-get-app](screenshots/home-get-app.png))
- **Don't invent a dark theme.** The stylesheet does not declare one.
- **Don't treat the sign-in wall as the editor.** Email, Apple, and Google are the wall. The journal is behind it and was not captured. ([sign-in-wall](screenshots/sign-in-wall.png))
- **Don't use the declared blue-600 as the hover.** Hover is the deleted variable's `#1b1bbc`, not `#0039e6`.

## Rebuild

```sh
cd systems/clearful
PLAYWRIGHT=/path/to/playwright/index.mjs node tools/capture/public/shoot.mjs
python3 tools/capture/quantize.py ~/.design-systems/clearful/raw-shots
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

`make design-md` needs a catalog entry. This package ships its own [DESIGN.md](DESIGN.md) for that reason. Register the package, then regenerate DESIGN.md from the catalog tool.

The control map is [site-tree.md](site-tree.md).
