# Fourthwall design reference

A token set and public-site map for Fourthwall, the creator-commerce platform. Captured from [https://fourthwall.com/](https://fourthwall.com/) on 2026-11-21, signed out, in headless Chromium at 1440x900 and 390x844. The marketing site is Webflow. Log in and Start now stop at a Keycloak wall on `auth.fourthwall.com`. `signed_in` is false. The signed-in app was not captured.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Fourthwall's site icon, 128 px PNG, resized from the 48 px favicon at fourthwall.com. Fetched without editing catalog.json. |
| [tokens.json](tokens.json) | W3C DTCG tokens in Tokens Studio's multi-set layout: `core` (124: ink and paper, grey/blue/green/red/yellow ramps, Suisse and heading faces, radii, space, layout) and `light` (22 semantic roles). One theme. Every token carries `$extensions.source`. |
| [DESIGN.md](DESIGN.md) | Written by hand for this package. `make design-md` was not run, because that generator needs a catalog.json entry and this capture does not edit catalog.json. |
| [style-guide.html](style-guide.html) | One page rendering the measured colour and type tokens. Component drawings lower on the page are kit leftovers, not Fourthwall specimens. |
| [components.md](components.md) | Measured controls (button, links, fields, nav, footer, menus) with crops and gaps. |
| [patterns.md](patterns.md) | How the header, menus, search page, pricing, footer and auth wall combine. |
| [components/](components/) | 26 element crops in [components/crops/](components/crops), `{component}-{state}.png` at 2x. |
| [screenshots/](screenshots/) | 211 quantized page shots: 104 desktop, 107 phone. Full-colour originals stay outside the repo. |
| [raw/](raw/) | `css-vars.json`, `computed-home.json`, `components-computed.json`. |
| [tools/](tools/) | The walkers and builders. See Rebuild. |
| [site-tree.md](site-tree.md) | Header, footer and in-page controls, and which page, menu or wall each one opens. |
| [login-review.json](login-review.json) | The empty auth walls. `signed_in` is false. Nothing was typed or submitted. |

## Brief

<!-- brief:start -->

Generated Brief was not written. `make brief` reads catalog.json, and this capture does not edit catalog.json. Read [tokens.json](tokens.json) and the Do and don't list below. Signed-in app was not captured. Unread token values are Not captured.

<!-- brief:end -->

## Health

<!-- health:start -->

Generated Health was not written. `make grade` writes the root catalog table as well as this section, and this capture does not edit catalog.json. The package has not been graded. Optional C5, V1 and V2 are not published here.

Gaps that are known without a grade: no dark theme, no declared focus-ring token, no declared success/warning/danger/info roles used as product status, no icon set (brand artwork is not kept), no signed-in app, pressed state of links not captured, hover of the measured controls did not change computed paint.

<!-- health:end -->

## How the values were read

Pages were captured signed out in headless Chromium. Desktop is 1440x900 at deviceScaleFactor 1. Phone is 390x844 at deviceScaleFactor 2. Sidecars in the scratch walk record `innerWidth` 1440 and 390. Cookie banners were hidden with CSS and the consent SDK was aborted at the request layer. No consent button was pressed.

`tools/capture/public/read-css.mjs` dumped 195 custom properties from the live home page into [raw/css-vars.json](raw/css-vars.json). `tools/build_tokens.py` tokenised the declared px colours, faces, radii and space steps. Fluid clamps, letter-spacing ems, a 50% circle, and Cookiebot `--cc-*` names are listed under `core.$extensions.notTokenised`, not as tokens.

`tools/capture/public/measure-states.mjs` measured visible controls on the live DOM: default, real hover, and keyboard focus-visible. Press on links was disabled because mouse-down navigates and destroys the page. Crops are in [components/crops/](components/crops). Values were not sampled from the quantized PNGs.

## What to distrust

- The hero and header Start now button computes to white fill and ink text (`rgb(255, 255, 255)` on `rgb(10, 10, 10)`). The declared action fill `--_surface---bg--action` is ink `#0a0a0a` with white text. That ink button is the Log in control on the auth wall, which is a different host. Do not treat the hero pill as the action token.
- Hover on the measured controls did not change computed colour. A CSS hover that the script missed is Not captured, not proof that hover is a no-op everywhere.
- Focus on links painted a 1px outline `rgb(0, 95, 204)` at 1px offset. That colour is the browser default, not a declared Fourthwall token. Status: Not captured as a token.
- `light.accent.hover`, `light.accent.pressed`, `light.text.disabled` and `light.status.*` are Derived or Not captured. The status ramps exist as older `--g*`, `--y*`, `--r*` and `--b*` variables. The public site does not assign them to success, warning, danger or info roles.
- The button crop text reads "Start now" once. The computed text was "Start now Start now" because a visually hidden duplicate sits in the same control. The crop is the visible label.
- `textField` measured a 52x23 control with 64px radius, not the search field. The search field on `/search` is 940x38, 14px, `rgb(51, 51, 51)` on white, radius 0. The accordion measurement returned a 0x0 box (the desktop burger is hidden). Do not use those two readings as the control spec.
- `button-pressed.png` exists from an earlier attempt. The finished measurement file has no pressed state. Pressed is Not captured.
- Screenshots are 256-colour. Do not sample tokens from them.
- Display type sizes are `clamp()` and were not tokenised as one length. The hero heading measured 57.6px / weight 420 on the home page at 1440.
- `/apps/beehiiv`, `/apps/packiyo` and `/apps/zapier` returned "Page not found" even though the sitemap lists 28 `/apps/*` URLs.
- Desktop screenshots timed out for `/features/direct-messages`, `/features/apps-and-integrations/stream-alerts`, `/features/apps-and-integrations/twitch-gifting`, `/make-your-own/kickboxing-class-t-shirts` and `/make-your-own/zine-publisher-t-shirts`. Those pages loaded. Phone shots of the same paths landed. The missing desktop files were not invented.
- The style guide's lower component drawings are kit leftovers. They are not Fourthwall.

## Fonts

- Suisse Intl is the body and control face, with Arial and sans-serif as fallbacks. Proprietary. The guide renders Arial.
- PP Telegraf (`--font-heading`) is the heading face. Proprietary. Not loaded here.
- Saans is the display primitive. Proprietary. Not loaded here.
- Weights in the token file: 300, 400, 420, 435, 450, 465, 480, 500, 600, 700. Nav and the hero button measured 450. Footer links measured 400. The hero heading measured 420.

## Coverage

| Expectation | Status | Where |
|---|---|---|
| Page, surface, text, muted, border roles | captured | `light.background.*`, `light.text.*`, `light.border.*` |
| Action fill | captured as a token, split in the UI | `light.accent.default` is ink. The hero button is a white pill. The auth Log in button is ink. |
| Accent hover and pressed | Not captured | no declared action-hover or action-pressed token |
| Status colours | Not captured as roles | ramps exist; no product role assigns them |
| Theme parity | not present | one light theme (`color-scheme: normal`) |
| Type families and static sizes | captured | `core.font` |
| Fluid display sizes | not tokenised | recorded under `notTokenised.fluidType` |
| Shape | captured | `core.radius` 6 to 18px plus a 999px pill |
| Spacing | captured | declared px steps in `core.space` |
| Layout | partly | column 768, page max 1880, section pad, measured nav 1440x71, footer 1440x362 |
| Buttons, links, nav, footer, menus, search page | captured | [components.md](components.md), [site-tree.md](site-tree.md) |
| Switch, radio, checkbox, select, toast, tooltip, table, avatar, dialog | not present | not measured on the public marketing pages |
| Disabled | Not captured | no disabled control was on the pages measured |
| Pressed | Not captured | link press navigates; not forced |
| Signed-in app, onboarding, checkout, newsletter, plan, survey | not captured | stopped at the auth wall |
| 1440 and 390 | captured | [screenshots/](screenshots) |
| Icons | not kept | brand artwork, docs/RIGHTS.md. `icon.png` is the site favicon only |
| Cookie banner | hidden, never accepted | no consent shot is in the package |

## Do and don't

- **Do set marketing type in ink or paper, not a brand hue.** Body text is `#0a0a0a`. The home hero inverts to paper type on an ink ground ([home](screenshots/home-default.png), [heading crop](components/crops/heading-default.png)).
- **Do use the 12px radius on the hero pill.** Start now measured 117x43, radius 12px, padding 12px 20px, Suisse Intl 17px weight 450 ([button](components/crops/button-default.png)).
- **Do treat the declared action fill as ink with paper text.** `--_surface---bg--action` is `#0a0a0a`. The auth wall Log in button shows that pair ([auth login](screenshots/auth-login-desktop.png)).
- **Do keep nav labels sentence case in Suisse Intl 450.** Features, Product catalog, Pricing, Learn, Log in ([nav](components/crops/nav-default.png)).
- **Do open Features and Learn as menus, not as new pages.** Desktop hover: [features menu](screenshots/home-menu-features.png), [learn menu](screenshots/home-menu-learn.png). Phone burger: [menu](screenshots/mobile-home-menu.png).
- **Don't sample colours from the screenshots.** They are 256-colour. Read [tokens.json](tokens.json).
- **Don't invent a dark theme.** `color-scheme` is `normal`. No `data-theme` was set.
- **Don't treat the browser focus outline as a Fourthwall token.** Links focused with a 1px `rgb(0, 95, 204)` outline ([nav link focus](components/crops/nav-link-focus-visible.png)). That value is Not captured as a token.
- **Don't follow Log in or Start now past the empty wall.** Both stop at Keycloak. Nothing was typed. See [login-review.json](login-review.json).

## Rebuild

```sh
cd systems/fourthwall
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  node tools/capture/public/read-css.mjs
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  node tools/capture/public/measure-states.mjs
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

The site walk is `tools/capture/public/walk.mjs`. It writes full-colour shots under `~/.design-systems/fourthwall/walk`. Quantize with `python3 tools/capture/quantize.py ~/.design-systems/fourthwall/walk`. Do not run `python3 tools/fetch_icon.py fourthwall` until catalog.json has an entry. This package's icon was resized from the favicon by hand so catalog.json stayed untouched.

`make design-md`, `make brief` and `make grade` need a catalog.json entry. They were not run. `make check` will report `systems/fourthwall has no catalog.json entry` until an entry is added in a separate change.
