# Fernand

Public marketing capture of Fernand, the customer support platform at [https://getfernand.com/](https://getfernand.com/). Read on 2026-11-21, signed out, in headless Chromium. Desktop requested 1440x900. Phone requested 390x844. One painted theme: light.

The signed-in app was not captured. Log in opens [https://app.getfernand.com/auth/login](https://app.getfernand.com/auth/login) and asks for a work email and a password. No code was sent. The walk stopped there. [https://getfernand.com/login](https://getfernand.com/login) is a 404.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site icon, 128 px, from the apple-touch-icon |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds the site's `--*` palette. `light` holds the roles measured on the homepage. |
| [DESIGN.md](DESIGN.md) | Hand-written DESIGN.md-spec export. `make design-md` did not run, because catalog.json was not edited. |
| [style-guide.html](style-guide.html) | Renders the tokens and the two button recipes |
| [components.md](components.md) | Public controls that were measured |
| [patterns.md](patterns.md) | Header, footer, demo modal, auth wall |
| [site-tree.md](site-tree.md) | Which control opens which page, menu, or dialog |
| [login-review.json](login-review.json) | The auth wall that was reached. `signed_in` is false. |
| [screenshots/](screenshots/) | Quantized captures of the public shell, opened menus, and the auth wall |
| [components/crops/](components/crops/) | Element crops of the header controls |
| [raw/](raw/) | CSS variables and computed styles the tokens were built from |
| [tools/](tools/) | Capture and build scripts |

## Brief

<!-- brief:start -->
Public light marketing site. Accent is `#00a0ff`. Page is white. Text is `#1a2035`. The signed-in app is not in this package.
<!-- brief:end -->

## Health

<!-- health:start -->
Not graded in this capture. catalog.json was not edited, so `make grade` cannot write this section.
<!-- health:end -->

## How the values were read

Custom properties came from the live homepage CSSOM (`tools/capture/vars.mjs`) into [raw/css-vars.json](raw/css-vars.json). Brand names are `--blue`, `--black`, `--grey*`, `--border`, `--green`, `--orange`, `--red`. WordPress `--wp--preset--*` names are in that file and are not product tokens.

Component metrics came from `getComputedStyle` on the homepage (`tools/capture/measure.mjs`) into [raw/components-computed.json](raw/components-computed.json). `tools/build_tokens.py` writes [tokens.json](tokens.json) from [raw/component-tokens.json](raw/component-tokens.json).

Screenshots were taken with Playwright. They are quantized to 256 colours. Read colours from the tokens, not the PNGs.

## What to distrust

- One theme. The marketing page stays light. The widget preview has Light and Dark buttons. Those restyle the illustration, not the page.
- WordPress preset colours are not Fernand's palette.
- Focus colour `#3b84d8` is Chromium's outline on the primary link, not a designed ring.
- Hover on "Start for free" did not change the computed background.
- The signed-in inbox, settings, and onboarding were not opened. Those token values are Not captured.
- Screenshots are 256-colour PNGs.

## Fonts

Inter, then system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial. Read from `getComputedStyle(body)`. The webfont file is not in the package.

## Coverage

| Item | Status |
|---|---|
| Colour roles, light | Captured. [tokens.json](tokens.json) `light.*` |
| Colour roles, dark | Not present on the marketing page |
| Type | Captured as measured sizes. No type scale token on the site. |
| Spacing, radii | Control padding and 6px radius captured. No spacing scale token. |
| Button | Captured. [screenshots/desk-home-default.png](screenshots/desk-home-default.png) |
| Link, nav | Captured |
| Menu | Install with AI menu captured |
| Dialog | Watch-demo dialog and Cal.com book-demo modal captured |
| Text field, select, checkbox, radio, switch | Not on the public site. Present on the signup wall. Not filled. |
| Tabs, tooltip, toast, table, avatar, badge | Not present on the public pages walked |
| Search | Not present |
| App shell | Not captured. Auth wall. |
| Onboarding | Not captured. Not filled. |
| Themes | Light only |
| Widths | Desktop viewport shots measure 1440x900. Phone viewport shots measure 390x844 at device pixel ratio 2, so the PNG is 780x1688. |

## Do and don't

1. **Use one blue accent.** Start for free is `#00a0ff` on white. See [screenshots/desk-home-default.png](screenshots/desk-home-default.png).
2. **Keep secondary actions quiet.** Book a demo is a white control with a hairline shadow, not a second blue. See [screenshots/desk-home-default.png](screenshots/desk-home-default.png).
3. **Stay on one light page.** Do not invent a dark marketing theme from the widget preview's Dark button. See [screenshots/desk-home-default.png](screenshots/desk-home-default.png).

## Rebuild

```bash
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/measure.mjs
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

catalog.json is not part of this capture. A later registration step has to add the entry before `make check` can pass for this folder.
