# ClassPass design reference

A token set and page record for the public ClassPass site (classpass.com), the fitness and wellness booking product. Captured on 2026-11-21, signed out, in headless Chromium at 1440 x 900 and 390 x 844. Light only. The site has no public dark theme.

Nothing was submitted. Cookie OK and Cookie Preferences were not clicked. Login, signup, reset-password and every Apple, Google, Facebook and SSO control were photographed or recorded and then left alone. No email or password was typed.

The site placed the headless browser in a city. Search and studio shots that showed a street address were deleted and are not in this package. Plan prices that named a country are in the plans screenshot because that page is public marketing. No client IP was written down.

| File | What it is |
|---|---|
| [site-tree.md](site-tree.md) | Which control on the home page opens which page, menu, drawer or auth wall |
| [icon.png](icon.png) | Site favicon, resized to 128 px |
| [tokens.json](tokens.json) | DTCG tokens. `core` holds the measured type, radius and size steps. `light` holds the semantic colours and component values. No dark set. Every token has `$extensions.source` |
| [DESIGN.md](DESIGN.md) | Generated from tokens.json and this README when `make design-md` is run. This capture PR does not register the package in catalog.json, so DESIGN.md may be absent until that registration |
| [style-guide.html](style-guide.html) | Renders the measured tokens. TT Norms is not bundled, so the page uses the system sans |
| [components.md](components.md) | Component inventory and gaps |
| [patterns.md](patterns.md) | How the public pages are put together |
| [components/crops/](components/crops) | 18 element crops |
| [screenshots/](screenshots) | 85 page shots, `{page}-light-{state}.png`. Desktop 1440 x 900. Phone shots are named `mobile-*` at 390 x 844 |
| [raw/](raw) | `css-vars.json`, `components-computed.json`, `measurements.md` |
| [tools/](tools) | Capture scripts and `build_tokens.py`, `build_style_guide.py` |

## Brief

<!-- brief:start -->
Read [tokens.json](tokens.json) before designing in this style. The public site is white, black text, and one blue (`#0055ff`) used for the trial pill, links and the login button. Type is TT Norms. Buttons that submit are pills. Fields are 4px rounded. There is no dark theme in this package.
<!-- brief:end -->

## Health

<!-- health:start -->
Not graded in this capture. catalog.json was not edited, so `make grade` was not run for this package.
<!-- health:end -->

## How the values were read

- Custom properties: `tools/capture/vars.mjs` walked the live CSSOM on the home page. The public site declares about ten `--*` names (hero colours, ticker height, carousel dots). Most colour is not a custom property.
- Computed styles: `tools/capture/public/measure.mjs` opened home, plans, login, search and gifts, and read `getComputedStyle` on the header, nav link, login button, SSO button, email field, plans heading and filter chip.
- Stylesheets also live on `cdn9.classpass.com`. Cross-origin sheets were readable enough to list font-family (`norms`, `circuit`, `hiragino`) and a handful of hex colours. Those hexes are not tokens unless a live element also computed them.
- Screenshots: `tools/capture/public/public.mjs`, one fresh browser per page. ClassPass returns 403 if one browser visits many routes. Cookie dialogs were hidden, not accepted.

## What to distrust

- The header "Get 14 days free" measurement hit the yellow banner link, not the blue pill. The pill's colour and radius come from the login submit button, which is the same blue pill.
- Plan prices and the legal page slug follow the city the site assigned. Do not treat that city as a design token.
- Screenshots are 256-colour PNGs. Read colours from tokens.json.
- Hover of the blue pill, pressed, disabled, error and dark were not captured.
- `core.radius.button` is `9999px` (the computed pill radius), not a named radius step in the product's CSS.

## Fonts

TT Norms, served as the family name `norms`, with `sans-serif` as the fallback. The public stylesheet also names `circuit` and `hiragino` (the latter for Japanese). None of these files are in the package. The style guide falls back to the system sans.

## Coverage

| Item | Status |
|---|---|
| Colour roles, light | Captured for page, surface, raised, text primary, on-accent, link, border default, border focus, accent default. [tokens.json](tokens.json) |
| Dark theme | Not present |
| Type | Captured: norms, 14 / 16 / 18 / 60. Display, body, nav, field. Code face not used on the captured pages |
| Spacing scale | Not captured as a scale. Nav padding is 16px |
| Radius | Captured: 4px field, 16px chip, 9999px pill |
| Elevation | Captured: header shadow |
| Motion | Not captured |
| Button | Captured default (login pill, SSO pill). Hover and pressed not captured |
| Link | Captured |
| Text field | Captured default and focus. Filled not captured (nothing was typed) |
| Text area, select, checkbox, radio, switch | Not present on the pages that were measured |
| Menu | Captured: How it works, language, phone drawer |
| Dialog | Cookie dialog observed and hidden. Not accepted |
| Card | Plan cards observed on [plans-light-full](screenshots/plans-light-full.png) |
| Search and filter | Filters were opened. Screenshots withheld because the results showed a street address |
| Auth | Login and signup walls photographed. Not submitted |
| Desktop 1440 and phone 390 | Captured. Sidecars in the scratch folder recorded innerWidth |

## Do and don't

1. **Use one blue.** The trial pill, the login button and text links are `#0055ff`. A second accent is not on these pages. See [login-light-default](screenshots/login-light-default.png).
2. **Make the submit control a pill.** The login button is 48px tall with a 9999px radius. Fields stay at 4px. See [button-submit-default](components/crops/button-submit-default.png).
3. **Keep the header white and short.** 64px, white, a soft shadow, black 14px links. See [home-light-default](screenshots/home-light-default.png).
4. **Put the trial offer in a yellow bar.** The banner is a full-width strip under the header, with its own close control. See [home-light-banner](screenshots/home-light-banner.png).
5. **Don't invent a dark theme.** The public site did not offer one.

## Rebuild

```sh
cd systems/classpass
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/public/public.mjs
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/public/measure.mjs
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
python3 tools/capture/quantize.py ~/.design-systems/classpass/raw-shots
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

`catalog.json` is not part of this package. Registering it is a separate change.

## Site tree

The map of controls to pages is [site-tree.md](site-tree.md).
