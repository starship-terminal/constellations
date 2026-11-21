# Hims UK design reference

A token set and component reference for the public Hims UK site, for building marketing and chooser surfaces in the style of the real thing. Captured from [www.forhims.co.uk](https://www.forhims.co.uk/) on 2026-11-21, signed out, in headless Chromium. Desktop shots are 1440×900 at 1x (`window.innerWidth` 1440, `innerHeight` 900, devicePixelRatio 1). Phone shots are 390×844 at 2x (`innerWidth` 390, `innerHeight` 844, devicePixelRatio 2). One light theme: `html` carries `brand-hims variant-care-sans`, and `color-scheme` is `normal`. No theme switch exists on the public surface.

The UK site paints black ink on white, a copper brand (`#cc835c`) on the wordmark and the accented headline words, cream treatment cards, and pill controls. Care Sans is the active family. The signed-in app and the intake quiz live on `app.forhims.co.uk`. Those branches stop at the wall. See [site-tree.md](site-tree.md).

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site icon, 128 px PNG, resized from `https://www.forhims.co.uk/apple-touch-icon.png` |
| [tokens.json](tokens.json) | W3C DTCG tokens: `core` (colour ramps, Care Sans, measured type roles, unit scale, radii) and `light` (page, surface, text, border, action, status). Every token carries `$extensions.source`. |
| [style-guide.html](style-guide.html) | Renders the measured tokens and the main controls. |
| [components.md](components.md) | Component inventory with crops and gaps. |
| [patterns.md](patterns.md) | How the chrome, hero, cards, menus and chooser combine. |
| [site-tree.md](site-tree.md) | Which control opens which page, menu, or wall. Mapped before screenshots. |
| [components/crops/](components/crops) | Element screenshots, `{component}-{state}.png` at 2x. |
| [screenshots/](screenshots) | `{page}-light-{state}.png` captures, quantised to 256 colours. Full-colour originals stay at `~/.design-systems/forhims/raw-shots/`. |
| [raw/](raw) | `css-vars.json` (903 resolved custom properties) and `components-computed.json`. |
| [tools/](tools) | The public capture scripts and `build_tokens.py`. |

## Brief

<!-- brief:start -->
<!-- brief:end -->

## Health

<!-- health:start -->
<!-- health:end -->

## How the values were read

Custom properties were read from the live CSSOM on `www.forhims.co.uk` at 1440×900 with [tools/capture/vars.mjs](tools/capture/vars.mjs). The Ketch consent CDN was aborted so the cookie dialog never mounted. No consent button was clicked. Stylesheets were same-origin, so none were skipped.

Component colours, sizes and radii were computed on the live elements with [tools/capture/public/measure.mjs](tools/capture/public/measure.mjs). Hover is a real pointer. Focus-visible and pressed on the LOGIN pill were forced through the Chrome DevTools protocol, so the button never navigated. No form was submitted. No password, code, profile, birthday, plan, survey or newsletter field was filled.

Colour ramps in `core.color` are the declared `--b-color-hims-*`, `--b-color-neutral-*`, `--b-color-sage-light-*` and `--b-color-utility-*` names, resolved by the browser. The Hers ramps in the same stylesheet are a sister brand and are not in this package.

## What to distrust

- The Explore treatments and Get started pills are black in the screenshots. Computed `backgroundColor` on the button node and its parents was transparent. `light.action.primary` aliases the declared `--colors-button-primary` (`#000000`). The painted fill was not isolated to a node.
- `--b-font-size-*` and `--b-unit-*` are fluid slopes. The stored px is the value computed at 1440×900, including sub-pixel rounding. Do not treat those px as the authored rem.
- `--b-line-height-*` resolved to about 18px for every role. The computed line-height on the measured controls is the one in `core.typography`.
- The chooser row computed to `rgb(0, 0, 238)`, the browser default link blue, because the locator hit the anchor rather than the painted card. The card in [screenshots/chooser-light-default.png](screenshots/chooser-light-default.png) is black text on white. That blue is not a brand colour.
- Focus-visible on the LOGIN pill did not change the computed colour. The product may paint no ring. That is recorded, not invented.
- Screenshots are 256-colour PNGs. Read colours from tokens.json.
- No email address, phone number or street address is written in the text. The complaints viewport and the condition-guide footer originally painted a support address, a press address and a pharmacy register. Those spans were painted over before commit. Full-page shots were cropped to the last painted row, so the black footer on the other pages is not in the PNGs.

## Fonts

Care Sans is the active family (`--b-font-family-sans` on `html.variant-care-sans`), with Helvetica and Arial as fallbacks. The files are served from `www.hims.com` and are proprietary. They are not in this package. The guide falls back to the system sans.

Sofia Pro (`SofiaProWeb`) and Ivar Soft are declared in `@font-face` rules. The captured UK pages use Care Sans. Ivar Soft was not observed on a heading in this capture.

## Coverage

| Expectation | Status | Where |
|---|---|---|
| Page, surface, text, border, accent | captured | `light.background`, `light.text`, `light.border`, `core.color.brand` |
| Accent hover and pressed | not captured | Declared `--colors-button-accentHover` exists. The public primary button's fill was not isolated, so its hover step was not read. |
| Success, warning, danger | declared, not seen | `light.status.*` aliases the utility ramps. No public form was submitted, so no error state was shown. |
| Dark theme | not present | One light theme on the public site. |
| Type | captured | `core.typography` from computed nav, LOGIN, button and menu. Display slopes are in `raw/css-vars.json` and were not the painted hero size. |
| Spacing | captured | `core.space` from `--b-unit-*` at 1440. |
| Radii | captured | Menu 8px, card 16px, pill 48px. |
| Motion | not captured | Named easings exist in the CSS (`--transitions-easing-*`). Durations were not read off a control. |
| Button | captured | LOGIN pill states. Primary pill observed in screenshots. Fill not isolated in CSS. |
| Link | captured | Nav link, safety link. |
| Text field, text area, checkbox, radio, switch | not present | Not on the public marketing pages. The login page has email and password fields and was not entered. |
| Select | captured | Review sort on `/hair-loss`. |
| Menu | captured | Sex and Learn floating menus. Account drawer. |
| Accordion | captured | Weight FAQ and PDP "Meet The Generic ED Pill". |
| Dialog | captured | Account menu drawer. Cookie dialog was not clicked. |
| Card | captured | Home treatment cards, chooser rows. |
| Toast, tooltip, table, avatar, badge, tabs | not present | Not on the captured public pages. Review stars are content, not a badge component. |
| Phone 390 | captured | Home, weight, PDP, blog, chooser, 404, account menu. |
| Signed-in app | not captured | LOGIN opens `https://app.forhims.co.uk/login`. Stopped. |
| Assessment | not captured | `/c/wl`, `/c/hl`, `/c/e`, `/c/p` redirect to `app.forhims.co.uk/flow/`. Stopped. |
| Profile, messaging, treatments | not captured | Redirect to `/customer/login`. Stopped. |

## Do and don't

- **Do paint the page white and the ink near-black.** The home canvas is white and the nav computes to `rgba(0, 0, 0, 0.89)`. See [screenshots/home-light-default.png](screenshots/home-light-default.png).
- **Do spend the copper on the wordmark and one headline word.** "for you" is the brand colour. The rest of the headline stays black. See the same shot.
- **Do put treatment choices in cream cards with a 16px radius.** See [screenshots/home-light-default.png](screenshots/home-light-default.png).
- **Do use a pill for LOGIN and the primary action.** LOGIN is a quiet grey pill. Explore treatments is a black pill. See the home shot.
- **Don't infer the signed-in app from the marketing site.** Login, profile, messaging and the intake quiz are walls. See [site-tree.md](site-tree.md).
- **Don't copy the press or support addresses into a design.** They are published contacts and are omitted from this package.

## Rebuild

```bash
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  node systems/forhims/tools/capture/vars.mjs
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  node systems/forhims/tools/capture/public/measure.mjs
python3 systems/forhims/tools/build_tokens.py
python3 systems/forhims/tools/capture/quantize.py \
  ~/.design-systems/forhims/raw-shots systems/forhims/screenshots
```

`make design-md` was not run. It needs a catalog.json entry, and this capture does not edit catalog.json. DESIGN.md, the generated Brief, and the generated Health section are absent for that reason. The markers in this file are empty on purpose.
