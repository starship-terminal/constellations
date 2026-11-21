# Rivian design reference

A token set and component reference for Rivian's public site, for building marketing and shopping surfaces in the style of the real thing. Captured from https://rivian.com/ on 2026-11-21, signed out, in headless Chromium at 1440×900 and 390×844. One light theme. Cookie banner was rejected (Reject All). No form was submitted. Sign-in at https://rivian.com/auth/login is a wall: email and password are shown, password was not submitted, and that branch stops.

Rivian paints a white page, black Adventure type, and one amber (`#ffaa00`) for the Demo drive pill and the chat launcher. Header menus are pale cards. Corners are pills on controls and 20px on cards. There is no dark theme switch on the public pages.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site icon, 128 px, from rivian.com/apple-touch-icon-180x180.png |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds the palette, Adventure, type roles, radius, space, shadow and motion. `light` holds semantic roles and measured controls. Every token has `$extensions.source`. |
| [DESIGN.md](DESIGN.md) | Generated export of the light theme. Take values from tokens.json. |
| [style-guide.html](style-guide.html) | Renders the main roles and controls with the measured values. Adventure is not bundled, so the page falls back to Helvetica. |
| [components.md](components.md) | Measured controls and the states that were reached |
| [patterns.md](patterns.md) | How the header, menus, hero and assistant combine |
| [site-tree.md](site-tree.md) | Which control opens which page, menu or dialog |
| [components/crops/](components/crops) | Element screenshots of the measured controls |
| [screenshots/](screenshots) | Page captures, `{page}-light-{state}.png`, desktop 1440×900 at 1x and `mobile-*` at 390×844 at 2x |
| [raw/](raw) | `css-vars.json`, `components-computed.json`. Full-colour shots stay in `~/.design-systems/rivian/raw-shots/` |
| [tools/](tools) | The capture scripts and `build_tokens.py` |

## Brief

<!-- brief:start -->

Read [tokens.json](tokens.json) before designing in this style. The catalog Brief is not generated for this package because catalog.json was left unchanged, as the capture task required.

Page `#ffffff`, surface `#f2f2f2`, text `#000000`, muted `#494949`, accent `#ffaa00`, border `#cbcbcb`. Type is Adventure. The primary control is a 32px amber pill.

<!-- brief:end -->

## Health

<!-- health:start -->

Not graded in this capture. catalog.json was not edited, so `make grade` was not run for this package. Re-grade when the package is registered.

<!-- health:end -->

## How the values were read

Custom properties were read from the live homepage stylesheets through the CSSOM, after Reject All, at 1440×900. Resolved colours and lengths are in [raw/css-vars.json](raw/css-vars.json). Names that the browser stores as space-separated HSL components (`40 100% 50%`) were converted to sRGB in `build_tokens.py` and labelled Derived. Control colours (the amber button, its hover and pressed fills, the inverse pill, the nav hover) were read from computed styles on the real elements and stored in [raw/components-computed.json](raw/components-computed.json).

## What to distrust

- HSL ramps (stone, yellow, green, and the rest) are Derived from component strings, not from a computed colour. The amber button fill `#ffaa00` is Measured and matches `--brand` after that conversion.
- Radius and spacing steps that come from `body[data-responsive="true"]` use the declaration's fallback (`4px`, `12px`, `20px`). That attribute was not set on the captured page, so those steps are Derived.
- Shadow tokens keep the first layer only. The full string is in css-vars.json.
- Screenshots are 256-colour PNGs. Do not sample colours from them.
- The assistant panel is an iframe. Its inner control styles were not read.
- Focus paints no ring on the primary button. That absence is measured, not a missing crop.

## Fonts

Adventure and Adventure Mono are declared in `@font-face` on the site. Both are proprietary. The tokens name Adventure, then Helvetica Neue, Helvetica, Arial, sans-serif. Canela and Liga appear in font faces and were not used as a measured text role on the captured controls. The style guide does not bundle the font files.

## Coverage

| Item | Status | Where |
|---|---|---|
| Page, surface, text, muted, accent, border | captured | `light.color.*`, `light.text.*`, `light.border.*` |
| Status colours | captured | `light.status.*` from `--semantic-*` |
| Dark theme | not present | `color-scheme: normal`, no theme switch |
| Type roles | captured | `core.typography` from `--text-display-*`, `--text-headline-*`, `--text-body-*`, `--text-label-*` |
| Radius and space | captured | `core.radius`, `core.space`. Responsive fallbacks are Derived |
| Shadow and motion | captured | `core.shadow`, `core.motion` |
| Button default, hover, pressed, focus | captured | `components/crops/button-primary-*` |
| Button disabled, loading | not captured | not on the public header |
| Icon button | captured | question launcher and mobile Open |
| Link | captured | Explore in the Vehicles menu |
| Menu | captured | Vehicles, Charging, Technology, Discover, Gear Shop |
| Dialog | captured | assistant panel; cookie preferences before reject |
| Text field, text area, select, checkbox, radio, switch | not captured | public forms were not filled or submitted |
| Tabs, tooltip, toast, table, avatar, badge | not present | not on the captured public pages |
| Form validation error | not captured | no form submitted |
| Login | not captured | https://rivian.com/auth/login is a wall. Password was not submitted. |
| Desktop 1440 and phone 390 | captured | `screenshots/` |
| Spaces index | captured | `spaces-light-default.png` |
| Locations list and a single space page | not captured | both show street addresses; omitted on purpose |
| Inventory past the postal-code dialog | not captured | the field was left empty and Continue was not clicked |
| Event signup fields | not captured | empty form on the event page; Sign up was not clicked |
| Full-page scrolls | not captured | viewport shots only; long pages and location tiles were not shipped |
| Accessibility contact line | redacted | the public contact address was painted out of the screenshot and is not written here |

## Do and don't

- **Do spend the amber on one action.** The header Demo drive pill is the only filled amber control in the bar. See [screenshots/home-light-default.png](screenshots/home-light-default.png).
- **Do keep the header a white 56px bar.** Menus open as pale cards under it. See [screenshots/home-light-vehicles-menu.png](screenshots/home-light-vehicles-menu.png).
- **Do set display type in Adventure, tight leading.** Headlines use the `--text-headline-*` sizes at weight 600.
- **Don't invent a dark theme.** The public site did not paint one.
- **Don't draw a focus ring the product does not paint.** Keyboard focus on Demo drive changed the fill and left `outline` at none.
- **Don't submit a public form to capture an error.** Booking, trade-in, updates and newsletter fields were left empty.

## Rebuild

```bash
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  node tools/capture/vars.mjs
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  node tools/capture/public/measure.mjs
python3 tools/build_tokens.py
python3 tools/capture/quantize.py ~/.design-systems/rivian/raw-shots
```

Full-colour shots are written to `~/.design-systems/rivian/raw-shots`. `quantize.py` writes the 256-colour copies into `screenshots/`.
