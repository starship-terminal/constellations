# Column design reference

A token set and component reference for Column's public marketing site. Read from **column.com** on **2026-11-21**, signed out, in headless Chromium at 1440 x 900 and 390 x 844. Column N.A. is a nationally chartered developer infrastructure bank. The public surface is the marketing site, the public docs at docs.column.com, and the signed-out login wall at dashboard.column.com/login.

The marketing site paints one light theme. Navy `#111a4a` is the primary button. Page ground is white. Type is Suisse Intl, with Suisse Intl Mono and Inter also declared. Docs have their own dark theme, toggled on the docs page and not mixed into these marketing tokens.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Column's site icon (128 px PNG), from column.com/favicon.ico |
| [tokens.json](tokens.json) | W3C DTCG tokens: `core` (colour ramps, type sizes, spacing) and `light` (page, text, accent, button roles). Every token carries `$extensions.source`. |
| [DESIGN.md](DESIGN.md) | One-theme export of the measured roles and type scale. Written for this package because `make design-md` requires a catalog.json entry, and this capture was told not to edit catalog.json. |
| [style-guide.html](style-guide.html) | Renders the light roles, button recipe, type sizes, and ramps |
| [components.md](components.md) | Measured public controls with crops |
| [patterns.md](patterns.md) | Shell, menus, hero, product page, contact form, docs, login wall |
| [components/](components/) | Element crops under `crops/` |
| [screenshots/](screenshots/) | Quantised page captures, desktop 1440 x 900 and phone 390 x 844 |
| [raw/](raw/) | CSS readings and component measurements |
| [tools/](tools/) | Capture scripts and builders |
| [site-tree.md](site-tree.md) | Public page tree and which control opens which page, menu, or wall |
| [login-review.json](login-review.json) | Signed-out login and signup walls, and confirmation that nothing was typed or submitted |

## Brief

<!-- brief:start -->
Read [tokens.json](tokens.json) before designing in this style. The marketing site is light only. Navy `#111a4a` is the primary action. Text is `#12161e` on white. Body copy is `#575a64`. The focus ring is `#d4e3f7`.

This section is hand-written. `make brief` rewrites Brief from catalog.json, and this capture was told not to edit catalog.json.
<!-- brief:end -->

## Health

<!-- health:start -->
Not graded in this capture. `make grade` writes Health from the scorecard and catalog.json. This capture was told not to edit catalog.json, so the package is not in the scorecard yet.
<!-- health:end -->

## How the values were read

Every marketing value came off the signed-out site in headless Chromium on 2026-11-21.

- **Tokens.** [tools/capture/vars.mjs](tools/capture/vars.mjs) read the inline stylesheets through the CSSOM, re-parsed them, and resolved each custom property in a probe document. [tools/build_tokens.py](tools/build_tokens.py) keeps colours, the type scale, the spacing scale, and the light roles. Unresolved `var()` leftovers and animation values stay out.
- **Components.** [tools/capture/public/measure.mjs](tools/capture/public/measure.mjs) reads computed style for nav links, the primary action, the hero title, and empty contact fields. Hover is a real mouse hover. Pressed is CDP `forcePseudoState`, so no link or submit button fires. Contact fields were focused empty. Nothing was typed.
- **Screenshots.** [tools/capture/public/public.mjs](tools/capture/public/public.mjs) takes viewport and full-page shots. The cookie banner was hidden in the page, not accepted or rejected. [tools/capture/quantize.py](tools/capture/quantize.py) writes 256-colour PNGs into `screenshots/`.

Nothing was sent, signed into, or submitted. Sign in and Sign up were not clicked during screenshot capture. The login URL was opened once to record the wall and then stopped.

## What to distrust

- **One marketing theme.** column.com declares no dark variant. docs.column.com has a Toggle theme control. Its dark screenshot is evidence that the docs theme exists. Those dark values are not in tokens.json.
- **Status colours are not roles.** Green, orange, red, and cyan ramps exist in `core.color`. The site does not declare success, warning, danger, or info roles. Do not treat a ramp step as a status token.
- **Button hover matches default.** `--btn-bg-primary-hover` resolves to the same `#111a4a` as the resting primary button.
- **Screenshots are quantised.** Read colours from tokens.json or raw/css-vars.json.
- **Login wall screenshots are absent.** Headless Chromium was shown a captcha instead of the sign-in form. The captcha was not solved and those images were not kept. The wall is recorded from an earlier DOM read in [login-review.json](login-review.json) and [site-tree.md](site-tree.md).
- **Docs contact line is masked.** The docs homepage prints published contact addresses. That line is painted over in the two docs screenshots. The rest of the page is unchanged.
- **Hero demo art.** The homepage shows sample names, sample balances, and a sample API payload. That is published marketing art, not a signed-in account.

## Fonts

Declared in `raw/css-vars.json`: **Suisse Intl** (300, 400, 500, 600), **Suisse Neue** (400, 500), **Suisse Intl Mono** (400), **Inter** (400, 500, 600), and a display face named **ryry**. The site preloads Suisse Intl and Suisse Neue woff2 files from `/fonts/`. Those files are not committed. The style guide uses the system sans.

## Coverage

| Expectation | Status | Where |
|---|---|---|
| Colour roles | captured | `light.*` and `core.color.color.*` ramps |
| Type | captured | Suisse Intl, sizes `--text-100` (12px) through `--text-1000` (72px), weights 300–700 |
| Spacing | captured | `--space-0` through `--space-96` in `core.spacing` |
| Radii | not captured | no shared radius custom property resolved on `:root` |
| Elevation | partly | `--shadow-product` is in raw/css-vars.json as an unresolved shadow string, not a token |
| Motion | not captured | durations and easings were not read as tokens |
| Button, link | captured | nav Sign in, Blog, Products, hero Sign up |
| Text field, text area | captured | empty contact fields, focused, nothing typed |
| Select, checkbox, radio, switch | not present | none measured on the public marketing surface |
| Menu | captured | Products, Developers, Get started, phone Open menu |
| Search | partly | docs search control exists; dialog open was not kept as a screenshot in this pass |
| Dialog, toast, tooltip | not present | on the marketing surface |
| Card | observed | product menu preview card and homepage product art |
| Table, avatar, badge | not present | as product components on the marketing surface |
| States: default, hover, focus-visible, pressed | captured | measured controls; pressed via CDP |
| Disabled, error, loading | not captured | would require submitting a form |
| App shell | captured | [home-light-default.png](screenshots/home-light-default.png) |
| Form with a validation error | not captured | contact form was not submitted |
| Empty, loading, error | not present | on the public marketing pages |
| Onboarding and the dashboard | not captured | login wall |
| Themes | partly | marketing light only; docs dark observed, values not tokenised |
| Widths 1440 and 390 | captured | desktop and `mobile-*` shots |
| Login wall | recorded, not screenshotted | captcha blocked the form; see [login-review.json](login-review.json) |

## Do and don't

1. **Do ground on white.** Page is `#ffffff`, ink is `#12161e`, muted body is `#575a64`. See [home-light-default.png](screenshots/home-light-default.png).
2. **Do use navy for the primary action.** `#111a4a` fill, white text. See [home-light-default.png](screenshots/home-light-default.png).
3. **Do keep Sign in quiet.** It is text, not a filled button. Get started is the filled control. See [home-light-products-menu.png](screenshots/home-light-products-menu.png).
4. **Do set display type in Suisse Intl.** The hero is large, tight, navy. See [home-light-default.png](screenshots/home-light-default.png).
5. **Don't invent status roles.** The ramps are palette, not success or danger tokens.
6. **Don't invent a marketing dark theme.** Docs can toggle dark. The marketing site does not.

## Rebuild

```sh
cd systems/column
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  node tools/capture/vars.mjs
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  RAW=~/.design-systems/column/raw-shots \
  node tools/capture/public/public.mjs
python3 tools/capture/quantize.py ~/.design-systems/column/raw-shots screenshots
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  node tools/capture/public/measure.mjs
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
python3 tools/build_components_md.py
```

`make design-md` and `make brief` need a catalog.json entry. This capture does not add one.
