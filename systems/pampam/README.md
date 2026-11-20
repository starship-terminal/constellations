# PamPam design reference

A token set and component reference for PamPam, the AI map maker at https://www.pampam.city/. Captured signed out on 2026-11-21 in headless Chromium. Desktop viewport measured 1440x900 at devicePixelRatio 1. Phone viewport measured 390x844 at devicePixelRatio 2. One light theme. The public surface is the marketing site, template gallery, a published community map, a print-guide wizard, and the Google sign-in wall. The map editor is behind that wall and was not entered. Google was not clicked. No form was submitted.

The public look is a warm ink (#1b1917) and a lavender mute (#9894a8) on white, a parchment tile (#faf2ec), and one blue action (#4b72f3). Headlines are the proprietary face Nineties. UI text is Inter at weight 550. Controls are 12px and 16px rounds, not pills, except the search field.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site icon, 128 px, from the apple-touch-icon |
| [tokens.json](tokens.json) | DTCG tokens. `core` holds measured brand colours, type, Panda spacing and radii, sizes and shadows. `light` is the only theme. Every token has `$extensions.source` |
| [DESIGN.md](DESIGN.md) | Not generated. `catalog.json` was not edited, and `make design-md` writes this file from a catalog entry |
| [style-guide.html](style-guide.html) | Renders the measured roles and the main controls |
| [components.md](components.md) | Component inventory, crops, and gaps |
| [patterns.md](patterns.md) | How the pages combine |
| [site-tree.md](site-tree.md) | Which control opens which page, menu, or dialog |
| [components/crops/](components/crops) | 12 element screenshots at 2x |
| [screenshots/](screenshots) | 31 viewport captures, 256-colour |
| [raw/](raw) | `css-vars.json` (Panda preset scales) and `component-tokens.json` (measured roles) |
| [tools/](tools) | Builders and the capture kit, adapted for this site |

## Brief

Not generated. `make brief` reads `catalog.json`, and this capture was told not to edit that file. Read [tokens.json](tokens.json) and the Do and don't list below.

## Health

Not generated. `make grade` requires a catalog entry. The coverage table below is the stand-in.

## How the values were read

Playwright loaded https://www.pampam.city/ and the public routes in [site-tree.md](site-tree.md). The stylesheet `https://www.pampam.city/_next/static/css/1aaf2a345b78a73b.css` declares a Panda preset (`--spacing-*`, `--radii-*`, `--durations-*`, `--breakpoints-*`, a default colour ramp). Brand colours are utility classes (`bg_#4B72F3`, `c_#1B1917`, `c_#9894A8`), confirmed by computed style on the heading, the nav link, the plan card and the Get Explorer control. Type sizes come from computed style and from `.nineties_*` and `.font-md_*` rules. There is no `data-theme` and no `prefers-color-scheme` rule. Screenshots were taken with Playwright, then quantized to 256 colours. Read colours from the tokens, not from the PNGs.

## What to distrust

- Nineties is a proprietary face. The style guide falls back when it is not installed. The family name is measured. The outlines are not in the repo.
- Panda's default ramps (`--colors-rose-50` and the rest) are framework presets. They are in `raw/css-vars.json`'s source sheet and are not the brand palette. They are not tokens here.
- The Pricing link hover did not change colour. A hover colour is not claimed.
- Focus outline `rgb(0, 95, 204)` is the browser default, recorded as such.
- The plan-card crop is the full Free column, not a tight card.
- Phone screenshots are 780x1688 because devicePixelRatio was 2. The CSS viewport was 390x844.
- Refero's pampam-city style is an interpretation. It is not a source for these values.
- The login dialog shows a Google button. That button was not clicked. The screenshot is the wall, not a signed-in state.

## Fonts

- Nineties, weight 400, display headlines. Proprietary. Fallback in the tokens is "nineties Fallback", which the site maps to local Arial.
- Inter, variable 100–900, used at 550 for UI. The site ships a woff2 and an Arial fallback named "inter Fallback".

## Coverage

| Checklist item | Status | Where |
|---|---|---|
| Page, surface, text, muted, accent, border | captured | `light.background.*`, `light.text.*`, `light.accent.default`, `light.border.*` |
| Raised, overlay, scrim | partly | Dialog is white on a dimmed photo. Scrim colour was not read |
| Success, warning, danger, info | not present | No status colours on the public pages |
| Disabled text | captured | `light.text.disabled` on the quiet button |
| Accent hover and pressed | not captured | Hover crop exists. Computed hover colour was not read. Pressed was not held |
| Type roles | captured | `core.typography` |
| Spacing scale | captured | `core.space`, the Panda preset |
| Radii | captured | Panda preset plus measured 6, 12, 16px controls |
| Border widths | captured | 1px hairline, 1px blue border, 2px plan border |
| Elevation | captured | `core.shadow.menu`, `core.shadow.button`, `core.shadow.quiet` |
| Motion | partly | Panda durations and easing are declared. A transition was not timed on an element |
| Control heights, icon sizes, focus ring | partly | Button 64px, nav 40px, search 36px. Focus ring is the browser default. Icons not extracted |
| Breakpoints and content width | captured | Panda breakpoints, content max 976px, viewports 1440 and 390 |
| Button | captured | primary, quiet, make-map |
| Icon button | observed | zoom, close, prompt star. Not cropped |
| Link | captured | nav link |
| Text field | captured | Explore search, filled, not submitted |
| Text area, select, checkbox, radio | not present | not on the public pages |
| Switch | observed | Pay yearly pill on pricing. Not cropped |
| Tabs | not present | Hero mode tiles are buttons, not a tab widget |
| Menu | captured | Solutions and Products |
| Tooltip, toast | not present | |
| Dialog | captured | Login dialog and `/login` |
| Card | captured | Plan card |
| List row | observed | Place cards on the published map. Crop missed and was deleted |
| Table, avatar, badge | not present | |
| App shell | captured | desktop and phone |
| Form validation | not captured | No form submitted |
| Empty, loading, error | not captured | Not reached without submitting or signing in |
| Destructive confirmation | not present | |
| Search | captured | Explore field filled, not submitted. Filter not opened |
| Onboarding | not captured | Behind Google sign-in |
| Dark theme | not present | |
| 1440 and 390 | captured | [screenshots/](screenshots) |
| Signed-in editor | not captured | `/login` is Sign in with Google only |

## Do and don't

- **Do set headlines in Nineties and UI in Inter 550.** The 80px hero and the 16px nav are the pair. [home-light-default.png](screenshots/home-light-default.png)
- **Do keep one blue for the paid action.** Get Explorer is `#4b72f3`. Quiet actions stay near-white. [button-primary-default.png](components/crops/button-primary-default.png)
- **Do mute navigation in lavender.** Pricing, Solutions and the footer use `#9894a8`, not the ink. [link-nav-default.png](components/crops/link-nav-default.png)
- **Do round controls at 12px and cards at 16px.** The menu is 6px. Search is the pill. [menu-solutions-default.png](components/crops/menu-solutions-default.png)
- **Don't invent a dark theme.** The public site has one light theme.
- **Don't treat the Google button as a captured signed-in flow.** It is the wall. [login-light-default.png](screenshots/login-light-default.png)

## Rebuild

```sh
cd systems/pampam
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
python3 tools/capture/quantize.py ~/.design-systems/pampam/raw-full
```

`make design-md` and `make grade` need a catalog entry. This capture does not add one.
