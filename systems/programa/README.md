# Programa design reference

A token set and component reference for Programa's public marketing site. Captured from [programa.design](https://programa.design/) on 2026-11-21, signed out, in headless Chromium. Desktop captures are 1440x900 at 1x. Phone captures are 390x844 at 2x. One light theme. The signed-in product at `https://app.programa.design/login` asks for email and password, or Google, Trimble, or Xero. Password was not submitted. Email was not typed. That branch stops at the wall.

Programa is interior-design project management software. The public site is a light editorial marketing surface: Rhymes Display headlines, Inter UI, a warm neutral ramp, a mint header button, and a yellow trial button.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site icon, 128 px PNG, from `/images/favicon.png` |
| [site-tree.md](site-tree.md) | Control map written before screenshots: which control opens which page, menu, or wall |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds the declared colour, spacing, type and radius scales. `light` holds the semantic roles. No dark set. Every token carries `$extensions.source` |
| [DESIGN.md](DESIGN.md) | Hand-written export of the light tokens, because this capture does not edit catalog.json and `make design-md` needs a catalog entry |
| [style-guide.html](style-guide.html) | Renders the light tokens and the three button recipes |
| [components.md](components.md) | Component inventory, crops, and gaps |
| [patterns.md](patterns.md) | How the shell, pricing, FAQ, search and contact combine |
| [components/crops/](components/crops) | 7 element crops |
| [screenshots/](screenshots) | 101 page captures, 256-colour PNGs. Desktop and phone |
| [raw/](raw) | [css-vars.json](raw/css-vars.json) and [components-computed.json](raw/components-computed.json) |
| [tools/](tools) | Capture scripts and the token and style-guide builders |

## Brief

<!-- brief:start -->
This section is not generated. The capture task forbids editing catalog.json, and `make brief` reads the catalog. Read [tokens.json](tokens.json) directly.

Principles are the six rules under [Do and don't](#do-and-dont).

Colour roles, light only: page `#ffffff`, surface `#fcfbf9`, text `#1a1916`, muted `#aaa59c`, accent `#fdffa2`, border `#eeece6`.

Type: Rhymes Display for headlines, Inter for UI. Radius on controls is 6px. Spacing steps run 4, 8, 12, 16, 24, 32, 40, 60, 68, 80.
<!-- brief:end -->

## Health

<!-- health:start -->
Not graded. `make grade` writes this section from the catalog, and this capture does not edit catalog.json. Re-grade after the package is registered.
<!-- health:end -->

## How the values were read

Every value came off the running signed-out site in headless Chromium on 2026-11-21.

- **Tokens.** Stylesheets were readable through the CSSOM. Declared custom properties are in [raw/css-vars.json](raw/css-vars.json). The brand scale is `--color-neutral-*`, `--color-yellow-*`, `--color-green-*` and the other hue ramps, plus `--spacing-spacing-*`, `--text-font-size-*` and `--radius-*`. Bootstrap `--bs-*` names are also declared. Only the ones Programa overrides (`--bs-primary` `#fdffa2`, `--bs-danger` `#ff427b`) are kept as roles.
- **Components.** Computed styles of the header button, the hero buttons, the nav link, the headline, the New badge, the FAQ button, and the blog search field are in [raw/components-computed.json](raw/components-computed.json). Hover used a real pointer. Pressed used CDP `forcePseudoState` so no link fired. Focus used `focus()`. No form was submitted.
- **Screenshots.** [tools/capture/public/public.mjs](tools/capture/public/public.mjs) shot each planned public page at 1440x900 and 390x844. [tools/capture/quantize.py](tools/capture/quantize.py) reduced them to 256 colours.
- **Fonts.** `@font-face` families: Rhymes Display, Rhymes Text, Rhymes Dynamic, Inter. The webfont files are not committed.

Nothing was sent, downloaded, or signed into. The only presses were local UI toggles: nav hover, the phone menu, the pricing switch, one FAQ question, and focus on the blog search and contact email. Get in touch opened a dialog that stayed on a spinner in headless Chromium. It was not submitted.

## What to distrust

- **One painted theme.** No dark theme exists on the public site. Do not invent one.
- **Two yellows.** `--color-yellow-light` (`#fdffa2`) is the declared accent and the pricing trial button. The header Start free button is a measured mint (`rgb(217, 237, 242)`), not that accent.
- **Bootstrap leftovers.** `--bs-success`, `--bs-warning` and `--bs-info` are framework defaults. They were not seen as designed status chips on the captured pages.
- **Text field chrome.** The measured search and email boxes are the inner inputs. The painted field is Not captured.
- **Plan card metrics.** The first selector matched the page. The card is visible in the pricing screenshot. Its numbers are Not captured as tokens.
- **Contact dialog.** [contact-light-email-focus.png](screenshots/contact-light-email-focus.png) shows the dialog still loading. The form inside the iframe did not paint. Do not read colours from that image.
- **Quantised screenshots.** Read colours from [tokens.json](tokens.json), not from the PNGs.
- **Changelog and blog full pages** were truncated at 8 tiles. The log records the boundary.
- **Hero line-height.** The h1 computed line-height is 64px while the declared display leading is 84px. The token keeps the computed 64px on `core.typography.display` and the declared 84px on `core.lineHeight.xxxxl`.

## Fonts

Rhymes Display (headlines), Rhymes Text, Rhymes Dynamic, and Inter (UI). Inter is the SIL Open Font License face. Rhymes is a commercial face. Neither webfont is committed. The style guide falls back to Georgia for display and the system sans for UI.

## Coverage

| Checklist item | Status |
|---|---|
| Colour roles, light | Captured. [tokens.json](tokens.json) `light` |
| Colour roles, dark | Not present |
| Type roles | Captured. Display, body, label, caption |
| Spacing | Captured. `--spacing-spacing-*` |
| Radii | Captured. `--radius-2`, `--radius-12`, and measured 6px control radius |
| Borders | Captured. `--color-borders-base` |
| Elevation | Not captured as a scale. Button shadows are in the raw computed styles |
| Motion | Captured as the declared 150ms ease. Reduced motion was not tested |
| Sizing | Captured. Header 72px, button heights 28px and 36px |
| Layout | Captured at 1440 and 390. Content widths in `core.content` |
| Button | Captured. [components.md](components.md) |
| Icon button | Captured as the phone Open menu in [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png). Metrics Not captured |
| Link | Captured |
| Text field | Partly. Focused, not filled, chrome Not captured |
| Text area | Not present on the captured public pages |
| Select | Not present |
| Checkbox | Not present |
| Radio | Not present |
| Switch | Captured as the pricing Monthly / Annual toggle. Thumb metrics Not captured |
| Tabs | Not present |
| Menu | Captured. Desktop hover menus and the phone menu |
| Tooltip | Not present |
| Dialog | Not captured. Get in touch opens a dialog that stayed on a spinner |
| Toast | Not present |
| Card | Observed on pricing. Metrics Not captured |
| List row | Observed in feature menus. Metrics Not captured |
| Table | Not present on the public site. The hero shows a product demo, not a live table |
| Avatar | Observed as published staff photos on contact. No component states |
| Badge | Captured. New chip |
| App shell | Captured |
| Form with validation error | Not captured. No form was submitted |
| Empty, loading, error | Loading observed only as the contact dialog spinner |
| Destructive confirmation | Not present on the public site |
| Feedback after an action | Not captured. No form was submitted |
| Search | Captured as a focused field. Not submitted |
| List or table | Feature menus and blog index. No data table |
| Onboarding | Not captured. Behind register |
| Signed-in app | Not captured. `https://app.programa.design/login` asks for email and password, or Google, Trimble, or Xero. Password was not submitted |

## Do and don't

- **Do set headlines in Rhymes Display.** The home H1 is 80px, weight 300. See [home-light-default.png](screenshots/home-light-default.png).
- **Do keep the page warm white.** Page is `#ffffff`, raised hover is `#f8f6f3`, border is `#eeece6`. See [home-light-default.png](screenshots/home-light-default.png).
- **Do use the yellow button for the trial.** Pricing's Start 7 day trial is `#fdffa2`. See [pricing-light-default.png](screenshots/pricing-light-default.png).
- **Don't treat the header mint as the accent.** Start free is a measured mint, not `--color-yellow-light`. See [button-primary-default.png](components/crops/button-primary-default.png).
- **Don't invent a dark theme.** Every captured route paints light.
- **Don't follow Log in or Start free into the app.** Those open the login and register walls. See [site-tree.md](site-tree.md).

## Rebuild

```bash
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  node systems/programa/tools/capture/public/public.mjs
python3 systems/programa/tools/capture/quantize.py ~/.design-systems/programa/raw-shots
python3 systems/programa/tools/build_tokens.py
python3 systems/programa/tools/build_style_guide.py
```

`make design-md` and `make brief` need a catalog.json entry. This capture does not add one.

## Surfaces

The marketing host is `programa.design`. The product host is `app.programa.design`. Locale mirrors (`/au`, `/uk`, `/eu`, `/mx`, `/latam`) repeat the English pages and were not captured as a separate system. The sitemap listed 441 paths, mostly blog and editorial articles. Indexes and one article template were captured. Individual articles beyond that were not.
