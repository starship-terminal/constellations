# Weights & Biases

Weights & Biases is an MLOps platform. This package is a public Playwright capture of [wandb.ai/site](https://wandb.ai/site) on 2026-11-21, signed out. The app host [wandb.ai](https://wandb.ai/) redirects to a CoreWeave Forge login wall. Marketing pages are dark. The Forge login and signup screens are light. Desktop width measured 1440 by 900. Phone width measured 390 by 844 on the home and pricing pages. Nothing was typed, submitted, or signed in.

An earlier package at `systems/weights-biases` measured the same surfaces on 2026-11-19 without screenshot frames. This package is the public refresh with frames.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px site icon, rasterised from the SVG favicon |
| [DESIGN.md](DESIGN.md) | DESIGN.md-shaped copy of the measured tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Colour, type, radius, and component tokens |
| [style-guide.html](style-guide.html) | Specimens rendered from the tokens |
| [components.md](components.md) | Component inventory and gaps |
| [patterns.md](patterns.md) | Page patterns |
| [components/](components/) | Crops of the Weave button, docs link, LOG IN, and SIGN UP |
| [icons/](icons/) | Site mark SVG and INDEX.tsv |
| [screenshots/](screenshots/) | Public pages, open menus, and the login and signup walls |
| [raw/](raw/) | Computed styles and custom properties that were read |
| [site-tree.md](site-tree.md) | Which control opens which page |
| [login-review.json](login-review.json) | What the login and signup walls ask for |
| [tools/](tools/) | Capture scripts and the token check |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

Headless Playwright opened the public site. Custom properties `--e-global-color-*` and `--e-global-typography-*` were read from the stylesheets. Component styles were `getComputedStyle` on the live controls. Hover was a real pointer move. Focus on SIGN UP was `element.focus()`. The announcement dialog was closed with its close control, then removed from the DOM so menus could be photographed. Cookie banners were hidden, not answered.

Desktop viewport was 1440 by 900, `devicePixelRatio` 1, `visualViewport` 1440 by 900 at scale 1. Phone shots were requested at 390 by 844 with `deviceScaleFactor` 2. Sidecars with those fields stayed in the capture scratch directory.

## What to distrust

Marketing and Forge are two products. `dark` is the marketing site. `light` is the Forge signed-out screen. Do not paint a marketing page with Forge cobalt.

The Weave button fill is a gradient. `dark.color.action.primary` is only the end stop.

`core.typography.label` line height is the Elementor accent line height, 18px, not a computed line height on the button.

The code sample's font was not read. There is no code type token.

Spacing is not a published scale. Control heights live on the component tokens.

The menu panel's own background colour was not stored. Do not invent one from the screenshot.

WordPress preset colours are in the stylesheets and are not product roles. They were left out.

The contact screenshots have the published support address painted over with the page ink. The docs link beside it is still the live page.

## Fonts

Source Sans 3 is the UI face on both surfaces. Source Serif 4 is the marketing display face. These are commercial faces. The tokens name them. The files are not in this package.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-dark-default.png](screenshots/home-dark-default.png) |
| Colour, accent and gold | Captured | [raw/readings.json](raw/readings.json) |
| Colour, status | Not captured | No success, warning, danger, or info role on the public pages |
| Type, display and UI | Captured | Home h1 and Elementor typography variables |
| Type, code | Not captured | Code sample visible, computed font not stored |
| Spacing scale | Not present | No published spacing scale. Control sizes are on component tokens |
| Radius | Captured | 3px field, 4px Forge control, 8px marketing button |
| Elevation | Not present | Weave button computed box-shadow none. No raised shadow was read |
| Motion | Not captured | Menu open was observed. Duration was not read from CSS |
| Button | Captured | [components/crops/button-weave-default.png](components/crops/button-weave-default.png) |
| Button hover | Captured | [components/crops/button-weave-hover.png](components/crops/button-weave-hover.png). Computed gradient did not change |
| Button focus | Captured on SIGN UP | [screenshots/home-dark-signup-focus.png](screenshots/home-dark-signup-focus.png) |
| Link | Captured | [components/crops/nav-docs-default.png](components/crops/nav-docs-default.png) |
| Text field | Captured, empty | [screenshots/contact-dark-default.png](screenshots/contact-dark-default.png) |
| Text area | Captured, empty | Same contact page |
| Select | Observed, not opened | Contact country and interest menus |
| Checkbox, radio, switch | Not present | Not on the public pages that were opened |
| Tabs | Observed | Brand guide tab row. Not activated |
| Menu | Captured | [screenshots/home-dark-menu-weave.png](screenshots/home-dark-menu-weave.png) |
| Dialog | Captured, then dismissed | Announcement on first paint. Not kept as its own frame after dismiss |
| Tooltip, toast | Not present | Not shown on the public pages |
| Card | Captured | [screenshots/pricing-dark-default.png](screenshots/pricing-dark-default.png) |
| Table, list row, avatar | Not captured | Not measured as components |
| Icon button | Not captured | Announcement close was used and not cropped |
| App shell | Captured | [screenshots/home-dark-default.png](screenshots/home-dark-default.png) |
| Form validation | Not captured | Contact form was not submitted |
| Empty, loading, error | Not captured | Signed-in app was not entered |
| Destructive confirmation | Not present | Not on the public site |
| Search | Not present | No public search field on the home page |
| Onboarding | Not captured | Would require an account |
| Dark theme | Captured | Marketing site |
| Light theme | Captured | Forge login and signup only |
| Desktop 1440 | Captured | Sidecar innerWidth 1440 |
| Phone 390 | Captured | Home and pricing. Phone nav not opened |
| Signed-in app | Not captured | Login wall. Session absent |

## Do and don't

- **Use the teal gradient for the marketing call to action.** The Weave button is `linear-gradient(270deg, #10bfcc, #0097ab)` with ink text, 8px radius, and uppercase Source Sans 3. See [screenshots/home-dark-default.png](screenshots/home-dark-default.png).
- **Use cobalt for the Forge primary button.** Log in is `#0541e9` on white, 4px radius, 32px tall. See [screenshots/login-light-default.png](screenshots/login-light-default.png).
- **Keep the marketing page on ink.** Body background is `#1a1c1f`. Display type is Source Serif 4. Nav links are `#00afc2`. See [screenshots/home-dark-default.png](screenshots/home-dark-default.png).
- **Do not submit the signup form from this capture.** Signup offers Google, GitHub, and Microsoft as well as email. No account was created. See [screenshots/signup-light-default.png](screenshots/signup-light-default.png).
- **Do not follow LOG IN and keep capturing.** That URL is a login wall. Record it and stop. See [login-review.json](login-review.json).

## Rebuild

```bash
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

Run those from this folder. `tools/build_tokens.py` checks sources. It does not regenerate tokens.json. The tokens were written from the readings at capture time. `make design-md` cannot write this package's DESIGN.md until catalog.json has a `wandb` entry. This pass does not edit catalog.json.
