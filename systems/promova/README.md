# Promova design reference

A token set and component reference for Promova's public marketing site. Captured from https://promova.com/ on 2026-11-21, signed out, in headless Chromium at 1440 x 900 and 390 x 844. The homepage, four nav menus, one language page, one course page, features, who we are, FAQ, blog, contact, a level-test landing, the 404, and the sign-up and onboarding walls.

Promova's marketing site is a black frame around white and lilac panels with 30px corners. Headlines are Nekst, heavy and black. Body is Manrope. Actions are square black buttons. A pink page fill marks FAQ. There is one light scheme.

Boundary: `/sign-up` rendered no email form. `/sign-in` rendered no login form. GET STARTED and TRY NOW open `/foxtrot/org-main`, a 15-step quiz, and that branch stopped on screen 1. No form was submitted. The signed-in product was not captured.

The control map is [site-tree.md](site-tree.md).

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site icon, 128 px PNG, from promova.com apple-touch-icon |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds measured colours, type, radii and sizes. `light` aliases them into roles. One theme. Every token has `$extensions.source` |
| [DESIGN.md](DESIGN.md) | Generated from tokens.json and this README. One theme, no provenance |
| [style-guide.html](style-guide.html) | Renders the tokens and a reconstruction of the bar, hero and cards |
| [components.md](components.md) | Component inventory and gaps |
| [patterns.md](patterns.md) | How the shell, hero, menus and walls fit together |
| [site-tree.md](site-tree.md) | Homepage controls and where each one goes |
| [screenshots/](screenshots) | `{page}-light-{state}.png` captures. Desktop 1440x900 at 1x. `mobile-*` at 390x844, 2x. Full pages are cropped to 1000px so the footer legal block stays out |
| [raw/](raw) | css-vars.json, components-computed.json, component-tokens.json, measurements.md |
| [tools/](tools) | Builders and the capture kit copy |

## Brief

<!-- brief:start -->
<!-- brief:end -->

## Health

<!-- health:start -->
<!-- health:end -->

## How the values were read

Values came from the signed-out site in headless Chromium on 2026-11-21.

- Custom properties: the live CSSOM on the homepage declared a vendor progress-bar set and `--safe-area-inset-bottom`. No design tokens. Recorded in [raw/css-vars.json](raw/css-vars.json).
- Components: `getComputedStyle` on the hero title, nav bar, buttons, language card, footer, FAQ body, FAQ search and FAQ card. Pointer hover on GET STARTED. Readings in [raw/components-computed.json](raw/components-computed.json).
- Screenshots: Playwright at 1440x900 (1x) and 390x844 (2x), with viewport sidecars in the scratch folder outside the repo. Consent overlays were hidden, never clicked. [tools/capture/quantize.py](tools/capture/quantize.py) wrote 256-colour PNGs.

Nothing was signed into, bought or submitted. Language chips, review arrows and nav menus are local UI. The onboarding quiz was not answered.

## What to distrust

- This is the public site, not the app. Lessons, plans and the account live behind the walls above.
- One theme. Lilac and pink are section fills.
- The site does not publish a token system. Every value is a computed style on one element. A class hash in the source string will change on their next deploy.
- `light.text.muted` aliases ink because no second text colour was measured. It is not a muted reading.
- Yellow `#fff584` and lavender `#d7d4e2` were counted in a colour pass. The elements were not isolated. Treat them as fills that appeared, not as named roles.
- Menu panel fill was not read. The wrapper computed transparent.
- Screenshots are 256-colour PNGs. Read colours from tokens.json.
- Privacy and sign-up shots are cropped so a published address and support address do not enter the package. The full legal page was not kept.
- Focus, pressed, disabled, loading and error were not captured.

## Fonts

Nekst sets the hero (70px, weight 700) and the buttons. Manrope sets body (16px, weight 400). Both are served by the site and are not in this package. The style guide falls back to Arial. Rubik appears in the computed fallback stack.

## Coverage

| Expectation | Status | Where |
|---|---|---|
| Colour roles | captured | `light.background.*`, `light.text.primary`, `light.accent.*`, `light.border.default`. Muted text, disabled, success, warning, danger and info were not measured |
| Type | captured | `core.font.*` Nekst and Manrope sizes and weights. No code or caption role |
| Spacing | not captured | no spacing scale was declared. Paddings are in measurements.md |
| Radii, borders | captured | `core.radius` 30 / 20 / 0. SIGN UP border 1px ink |
| Elevation | not present | measured shadows were `none` |
| Motion | partly | nav opacity 0.2s ease-out. No cubic-bezier token |
| Sizing, layout | captured | nav 100px, buttons 40 and 60, content width 1400 at 1440 |
| Button, link | captured | GET STARTED, SIGN UP, TRY NOW, nav triggers |
| Menu | captured | four desktop menus and the phone drawer |
| Card | captured | language card, FAQ topic card |
| Text field | partly | FAQ search is in [faq-light-default](screenshots/faq-light-default.png). Not filled. Contact form not measured |
| Icon button, text area, select, checkbox, radio, switch, tabs, tooltip, dialog, toast, table, avatar, badge | not present | not isolated on the captured public pages |
| States: default, hover | captured | hover on GET STARTED only |
| States: focus-visible, pressed, disabled, loading, error | not captured | not held or not present |
| Form with a validation error | not captured | no form was submitted |
| Signed-in app, sign-up form, onboarding past screen 1 | not captured | walls recorded in site-tree.md |
| Themes: light, dark | partly | light only |
| Widths: 1440, 390 | captured | desktop and phone shots |

## Do and don't

1. **Do set type in black on a white or lilac panel.** The frame around those panels is black. See [home-light-default](screenshots/home-light-default.png).
2. **Do round the panels and keep the buttons square.** Nav, hero and footer use 30px. Cards use 20px. GET STARTED, SIGN UP and TRY NOW use 0. See [home-light-default](screenshots/home-light-default.png).
3. **Do use one black fill for the action.** Hover shifts that fill to `#262626`. See [home-light-cta-hover](screenshots/home-light-cta-hover.png).
4. **Do spend lilac on the hero and pink on FAQ.** They are section fills, not a second theme. See [faq-light-default](screenshots/faq-light-default.png).
5. **Don't style the app from this package.** Sign-up rendered no form. Onboarding stopped at screen 1. See [signup-light-wall](screenshots/signup-light-wall.png).
6. **Don't invent a dark theme.** None was offered.

## Rebuild

From `systems/promova/`:

```sh
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

Then from the repo root, `make design-md` rewrites DESIGN.md. `make brief` and `make grade` need a catalog entry. This capture does not edit catalog.json.

Live recapture needs Playwright at `PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs`. The shot list for this run lived in scratch, not in the package. Full-colour PNGs stay in `~/.design-systems/promova/raw-shots/`.
