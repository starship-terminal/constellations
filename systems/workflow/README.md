# Workflow design reference

A token set and component reference for Workflow, the design-feedback product at [workflow.design](https://www.workflow.design/). Captured from the public marketing site on 2026-11-21, signed out, in headless Chromium. Desktop 1440×900 at 1x. Phone 390×844 at 2x. One light theme. The app at `app.workflow.design` is a login wall and was not entered.

The public site sets type in Inter and Crimson Pro, paints a warm page (`#f6f4f0`) and an ink (`#1a1a1a`) that is not pure black, and uses 8px corners on the header button.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site apple-touch icon, resized to 128 px from the published 256 px logo |
| [tokens.json](tokens.json) | W3C DTCG tokens: `core` and `light`. Every token carries `$extensions.source` |
| [DESIGN.md](DESIGN.md) | Not generated. `make design-md` needs a catalog entry, which this capture did not add |
| [style-guide.html](style-guide.html) | Renders the colour, type and space tokens |
| [components.md](components.md) | Public controls and their crops |
| [patterns.md](patterns.md) | How the public pages are put together |
| [site-tree.md](site-tree.md) | Which control opens which page, menu, or wall |
| [components/crops/](components/crops) | Element screenshots of the public button, link and tab |
| [screenshots/](screenshots) | 175 captures, `{page}-light-{state}.png`, phone files prefixed `mobile-` |
| [raw/](raw) | CSS custom properties, computed styles, and a few viewport sidecars |
| [icons/](icons) | No extracted icons. INDEX.tsv records that brand artwork stays in screenshots |
| [tools/](tools) | Capture scripts and the builders |

## Brief

<!-- brief:start -->
Read this before designing in this style. Take every value from [tokens.json](tokens.json).

### Principles

1. Do set body type in Inter and display type in Crimson Pro.
2. Do paint the page in the warm ground and the ink, not pure black.
3. Do keep the header button quiet: a light fill, 8px corners, 40px tall.
4. Don't invent a second accent hue. The marketing accent is the ink.
5. Don't assume a dark theme. The public site does not ship one.
6. Don't treat the home demo as the signed-in app.

Each rule links a screenshot under [Do and don't](#do-and-dont).

### Using tokens

Light page `#f6f4f0`, surface white, text `#1a1a1a`, muted `#1a1a1aa6`, accent `#1a1a1a`, border `#1a1a1a1f`.

### Using components

Read [components.md](components.md) and [patterns.md](patterns.md). Crops are in [components/crops/](components/crops). [style-guide.html](style-guide.html) renders the tokens.

### Accessibility

Text on page is ink on `#f6f4f0`. The header button's focus outline width measured 0px, so no ring paints by default. See `light.focus.ring`.

<!-- brief:end -->

## Health

<!-- health:start -->
Not graded in this capture. `catalog.json` was left unchanged, so this package is not in the scorecard snapshot.
<!-- health:end -->

## How the values were read

Custom properties were read from the live CSSOM on https://www.workflow.design/ and written to [raw/css-vars.json](raw/css-vars.json). Resolved values are `getComputedStyle(document.documentElement)` on the home page. Component sizes and the button hover fill were read from computed styles in [raw/components-computed.json](raw/components-computed.json). Screenshots were taken with Playwright and quantised to 256 colours. Read colours from the tokens, not the PNGs.

## What to distrust

- The home page demo shows a sample review of a published Squarespace page, with names the product itself publishes. It is not the signed-in app.
- Help pages load a second stylesheet (`_ferndesk`) with its own canvas tokens. Those are the help center's chrome, not the marketing `:root` set used in `tokens.json`.
- `legacy.*` colours are still declared. The current roles are the `--color--*` names.
- Button pressed state did not paint a distinct fill under CDP `:active`. It is not a token.
- Warning and info colours are not declared. They are Not captured.
- Contact screenshots have the published street address and mailbox addresses painted out. The rest of that page is the live layout.
- Phone full-page shots of `/features` and `/policies` are tall. The shooter caps a page at 8 chunks.

## Fonts

Inter and Crimson Pro, named by `--type--body` and `--type--display`. Both are loaded by the site from a font host. The tokens name the families. The font files are not in this package.

## Coverage

| Item | Status |
|---|---|
| Colour roles (page, surface, text, border, accent, overlay, success, error) | Captured. [tokens.json](tokens.json) |
| Warning, info | Not captured. Not declared |
| Type (display, body, label) | Captured from h1, body and the header button |
| Caption, code | Not captured. No public role was measured |
| Spacing, radii | Captured from `--space--*` and `--radius--*` |
| Elevation | Not captured as a scale. Comment shadow colours are in `light.shadow` |
| Motion | Captured. 200ms, cubic-bezier(0.455, 0.03, 0.515, 0.955) on the header button |
| Button, link, tabs, menu, dialog | Captured. See [components.md](components.md) |
| Text field | Not present. `/contact` has no inputs |
| Icon button, select, checkbox, radio, switch, tooltip, toast, table, avatar, badge | Not present on the public site |
| App shell, inbox, comment composer, destructive confirm, onboarding | Not captured. Login wall at `https://app.workflow.design/users/sign-in` |
| Dark theme | Not present |
| Desktop 1440 and phone 390 | Captured. See [screenshots/](screenshots) |
| Sitemap feature articles (65) | 15 representative articles captured, plus the features index. The rest are the same template. Listed in [site-tree.md](site-tree.md) |
| Help articles | Index plus `/help/what-reviewers-see-3ferr`. Other confirmed slugs are in [site-tree.md](site-tree.md) and were not all screenshotted |

## Do and don't

1. **Do set body type in Inter and display type in Crimson Pro.** The home heading is Crimson Pro 32/32 weight 300. Body is Inter 14/21. See [home-light-full](screenshots/home-light-full.png).
2. **Do paint the page in the warm ground and the ink, not pure black.** Page is `#f6f4f0`, text is `#1a1a1a`. See [pricing-light-default](screenshots/pricing-light-default.png).
3. **Do keep the header button quiet.** Light fill, 8px radius, 40px tall. See [components/crops/button-default.png](components/crops/button-default.png).
4. **Don't invent a second accent hue.** Links and the wordmark use the same ink. See [home-light-default](screenshots/home-light-default.png).
5. **Don't assume a dark theme.** No toggle exists on the public pages.
6. **Don't treat the home demo as the signed-in app.** The review frame is a marketing recording. See [home-light-tab-videos](screenshots/home-light-tab-videos.png).

## Rebuild

```bash
cd systems/workflow
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

Screenshots:

```bash
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  node tools/capture/public/public.mjs
python3 tools/capture/quantize.py ~/.design-systems/workflow/raw-shots
```
