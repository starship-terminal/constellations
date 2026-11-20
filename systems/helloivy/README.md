# Hello Ivy design reference

A token set and component reference for Hello Ivy's public marketing site. It was read from **www.helloivy.co** on **2026-11-21**, signed out, in headless Chromium at 1440 x 900 and 390 x 844. The product host is **app.helloivy.co**. Login and signup were photographed and measured at rest, then the branch stopped. No password was typed. No form was submitted. Google was not clicked.

Hello Ivy's public site is a Framer marketing page on a cream field, with black type, black pill actions, and two served faces: Unbounded for display and Inter for UI text. Several "Get Started" controls leave the site for complex.so. That host is not Hello Ivy and is not in this package.

**Boundary:** the signed-in app was never reached. Dark theme is not present on the public pages. `catalog.json` was not edited, so this package is not registered and `make design-md` cannot generate [DESIGN.md](DESIGN.md).

| File | What it is |
|---|---|
| [icon.png](icon.png) | The site favicon declared on www.helloivy.co, 32 px PNG. `tools/fetch_icon.py` did not accept the URL, so the file was downloaded from the declared icon link and saved as PNG. |
| [tokens.json](tokens.json) | W3C DTCG tokens: `core` and `light` only. Every leaf cites a computed style in [raw/readings.json](raw/readings.json) or [raw/extra-styles.json](raw/extra-styles.json). |
| [DESIGN.md](DESIGN.md) | Hand-written stand-in. The generator needs a catalog entry, which this capture was told not to add. |
| [style-guide.html](style-guide.html) | One light page that renders the tokens, a pill, and a field from [tokens.json](tokens.json). |
| [components.md](components.md) | Public components that were seen, with measured values where a node was read. |
| [patterns.md](patterns.md) | How the marketing shell, menu overlay, docs index, pricing page, and login wall fit together. |
| [site-tree.md](site-tree.md) | Which control opens which public page, menu, or auth wall. Mapped before the screenshots. |
| [screenshots/](screenshots) | 39 quantized PNGs. Desktop 1440 x 900 at 1x. Phone 390 x 844 at 2x. `-full` pages are stitched. |
| [raw/](raw) | [readings.json](raw/readings.json) and [extra-styles.json](raw/extra-styles.json). |
| [tools/](tools) | The adapted capture kit and [build_tokens.py](tools/build_tokens.py). |

## Brief

<!-- brief:start. Not generated. catalog.json has no helloivy entry, so tools/brief.py cannot write this section. -->

Read this before designing in this style. Take every value from [tokens.json](tokens.json). The screenshots are 256-colour PNGs.

### Principles

1. Do paint black pills on cream.
2. Do set display type in Unbounded.
3. Do keep the menu as a full overlay.
4. Don't treat complex.so as Hello Ivy.
5. Don't invent a dark theme.
6. Don't style the signed-in app from this package.

Each rule links a screenshot under [Do and don't](#do-and-dont).

### Using tokens

| Role | light |
|---|---|
| page | #faf6f0 `core.color.paper` |
| surface | #faf6f0 `core.color.paper` |
| text | #000000 `core.color.ink` |
| muted | #707b8b `core.color.muted` |
| accent | #000000 `core.color.ink` |
| border | #c4c4c4 `core.color.field-border` |

Fonts: `core.font.family.display` is Unbounded. `core.font.family.text` is Inter. Type composites live under `core.typography` (display, body, nav, button). Radius steps are pill, control, and none. Spacing steps are under `core.space`.

### Using components

Read [components.md](components.md) and [patterns.md](patterns.md). There is no `components/crops/` folder. [style-guide.html](style-guide.html) renders the measured tokens.

### Accessibility

| Theme | text on page | muted on page |
|---|---|---|
| light | #000 on #faf6f0 | #707b8b on #faf6f0 |

Focus tokens: none measured. A keyboard focus ring was not captured.

<!-- brief:end -->

## Health

<!-- health:start. Not generated. This package is not in catalog.json and has no scorecard grades. -->

Scorecard: not reviewed. The capture was told not to edit catalog.json, so `make grade` has no row to write.

Layout ([docs/PACKAGE.md](../../docs/PACKAGE.md)): no `components/` crops, no `icons/`. Icons were not extracted. The wordmark is an SVG in the screenshots. DESIGN.md is a hand-written stand-in, not `make design-md` output.

<!-- health:end -->

## How the values were read

Every value came off the running public site in headless Chromium, Playwright at `~/.design-systems/pw/node_modules/playwright/index.mjs`.

- **Pages.** [tools/capture/public/public.mjs](tools/capture/public/public.mjs) opened the marketing routes and the login wall. It hid consent overlays. It did not click consent, Google, Apple, mailto, or a submit button.
- **Styles.** [tools/capture/public/read.mjs](tools/capture/public/read.mjs) wrote [raw/readings.json](raw/readings.json) from `getComputedStyle` on painted nodes. Button labels were read on the inner text node, not the wrapping anchor.
- **Tokens.** [tools/build_tokens.py](tools/build_tokens.py) writes [tokens.json](tokens.json) from those readings. A role the pages do not paint is omitted.
- **Screenshots.** Raw shots stayed outside the repo. [tools/capture/quantize.py](tools/capture/quantize.py) wrote 256-colour PNGs into [screenshots/](screenshots).

The menu overlay was measured in a separate probe while it was open. Those readings are in the coverage notes. They are not all folded into tokens.json. The wordmark is an SVG. Its computed font is the browser default, so the wordmark face is Not captured.

## What to distrust

- **This is the marketing site plus the login wall.** The signed-in product was not opened.
- **complex.so is a different product.** Several CTAs leave helloivy.co for it. Do not copy that UI into a Hello Ivy screen.
- **One theme.** `html` stayed `toggle-theme="light"`. A "Change theme" control on the phone overlay did not switch the attribute. There is no dark set.
- **Framer hashed custom properties** are ink, cream, and white. Named roles in tokens.json are the measured computed styles, not a published token spec.
- **UA blue is not a brand colour.** Unstyled anchors computed `rgb(0, 0, 238)`. Painted labels were measured instead.
- **Pricing plan CTAs** computed `border-radius: 0` on the anchor that was read. Header pills computed `9999px`. Both readings are kept. Do not average them.
- **Muted** is the Google button label on the login wall, not a marketing secondary colour. Marketing secondary text was not isolated.
- **Quantized screenshots.** Read colours from tokens.json.
- **Menu screenshots** hide the overlay's street line and email line. Those strings are not in the package text.
- **Login placeholders** in the screenshots are the product's own field hints. Nothing was typed into them.

## Fonts

**Unbounded** (400, 500, 700) is the display face: home headline, pricing headline, price figures. **Inter** (400, 500, 600) is the text face: nav, intro, pills, login fields. The site also requests Instrument Sans. The nodes that were read used Unbounded or Inter. The wordmark is an SVG, so its face is Not captured. Neither family is vendored here. The style guide loads them from Google Fonts.

## Coverage

| Expectation | Status | Where |
|---|---|---|
| Colour roles | captured | `core.color.*`, `light.*`. Light only. |
| Type | captured | Unbounded display, Inter text, measured sizes in `core.font.size` |
| Spacing, radii, borders | captured | `core.space`, `core.radius`, `core.border` |
| Elevation | not captured | No shadow was read on the probed nodes |
| Motion | not captured | Durations and easings were not read |
| Sizing, layout | captured | CTA 56px, login field 48.5px, content width 1344px |
| Button | captured | Header pill and login Continue. Hover, focus, pressed, disabled not captured |
| Link | captured | Header Features link |
| Text field | captured | Login email and password at rest. Not typed. Not submitted |
| Menu | captured | [home-light-menu](screenshots/home-light-menu.png), [mobile-home-light-menu](screenshots/mobile-home-light-menu.png) |
| Card | captured | Docs and feature cards in screenshots. Card chrome was not separately measured |
| Badge | not present | No badge component was isolated |
| Text area, select, checkbox, radio, switch, tabs, tooltip, toast, dialog, table, avatar | not present | None on the public pages that were opened |
| Docs search | not captured | Visible on the docs index. Not opened. Not measured |
| States: hover, focus, pressed, disabled, loading, error | not captured | Forms were not submitted. Focus was not held |
| Form with a validation error | not captured | No form was submitted |
| Signed-in app, signup, reset password | not captured | Auth wall. URLs are in [site-tree.md](site-tree.md) |
| Dark theme | not present | `toggle-theme` stayed light |
| Widths: 1440, 390 | captured | Desktop and phone shots |
| Blog and release-note families | partly | One index and one article each. The sitemap lists 84 posts and 35 notes. They share templates |
| Feature pages | partly | Index plus tasks. The other feature URLs share that template. Listed in [site-tree.md](site-tree.md) |

## Do and don't

1. **Do paint black pills on cream.** Page background is `#faf6f0`. Primary actions are black pills with white Inter labels. See [home-light-default](screenshots/home-light-default.png).
2. **Do set display type in Unbounded.** Headlines are Unbounded 500, 82px on home and 90px on pricing. Body intro is Inter 27px. See [pricing-light-default](screenshots/pricing-light-default.png).
3. **Do keep the menu as a full overlay.** The menu icon opens a cream sheet with numbered links, a close control, and a trial pill. See [home-light-menu](screenshots/home-light-menu.png).
4. **Don't treat complex.so as Hello Ivy.** Get Started and several footer controls leave the site. Record the hop. Do not restyle Hello Ivy from that host.
5. **Don't invent a dark theme.** The public pages stayed light. See [docs-light-default](screenshots/docs-light-default.png).
6. **Don't style the signed-in app from this package.** Login is a wall, measured at rest. See [login-light-default](screenshots/login-light-default.png).

## Rebuild

From `systems/helloivy/`:

```sh
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
python3 tools/capture/quantize.py ~/.design-systems/helloivy/raw-shots
```

`make design-md` and `make brief` need a catalog entry. This capture does not add one.

Live recapture, when the site loads:

```sh
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  node tools/capture/public/public.mjs
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  node tools/capture/public/read.mjs
```

## Registration gap

This folder is a real public capture. It is not in [catalog.json](../../catalog.json). A capture PR that includes catalog.json was forbidden. `make check` will fail until a later change registers the package. [webapps-manifest.json](../../webapps-manifest.json) was not edited.
