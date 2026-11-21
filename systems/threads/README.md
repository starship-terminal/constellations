# Threads design reference

A token set and component reference for the public, signed-out Threads site at https://www.threads.com/. Captured on 2026-11-21 in headless Chromium, desktop 1440×900 and phone 390×844, light and dark. Dark is the browser colour scheme, which Threads paints as `__fb-dark-mode`. Nothing was signed into. No username, email, password, or code was typed. Instagram, Google, Apple, and Facebook were not clicked. A control that opened a login or sign-up wall was recorded and that branch stopped. The map is [site-tree.md](site-tree.md).

This package is not in [catalog.json](../../catalog.json). A capture pull request that edits the catalog is rejected, so registration is a later step.

| File | What it is |
|---|---|
| [icon.png](icon.png) | 128 px PNG from the site's 256 px apple-touch icon |
| [tokens.json](tokens.json) | DTCG tokens. `core` holds a few always-colours, type, radius, and spacing. `light` and `dark` hold the semantic colour roles. Every colour names the custom property it was read from. |
| [DESIGN.md](DESIGN.md) | Not generated. `make design-md` writes it from a catalog entry, and this package is not registered. |
| [style-guide.html](style-guide.html) | Renders the colour roles and three controls, with a light/dark toggle. |
| [components.md](components.md) | Checklist components, captured, observed, or not present. |
| [patterns.md](patterns.md) | Shell, feed, login wall, search, profile, menu. |
| [site-tree.md](site-tree.md) | Which control opens which page, menu, dialog, or login wall. Written before the screenshots. |
| [screenshots/](screenshots/) | 33 captures, 256-colour PNGs. Desktop 1440×900 at 1x. Phone 780×1688 (390×844 at 2x). |
| [raw/](raw/) | `css-vars.json` (declared custom properties), `components-computed.json`, `pages.json`. |
| [tools/](tools/) | `build_tokens.py`, `build_style_guide.py`, and the capture scripts under `tools/capture/`. |

## Brief

<!-- brief:start -->
Not generated. `make brief` reads the catalog entry, and this package is not in catalog.json.
<!-- brief:end -->

## Health

<!-- health:start -->
Not graded. `make grade` reads the catalog entry.
<!-- health:end -->

## How the values were read

Headless Chromium opened https://www.threads.com/ and https://www.threads.com/login. `tools/capture/public/measure-live.mjs` walked the CSSOM. The semantic colours are the custom properties on `:root, .__fb-light-mode:root, .__fb-light-mode` and on `.__fb-dark-mode:root, .__fb-dark-mode`. Computed styles of the left-rail labels, the Log in button, and the login fields are in `raw/components-computed.json`. `tools/build_tokens.py` copies those declarations into tokens.json. Screenshots were taken by `tools/capture/public/capture.mjs` and quantised to 256 colours. Read colours from tokens.json, not from the PNGs.

## What to distrust

- The join dialog, the right-hand login card, and the phone "Thread on Threads" dialog are the signed-out chrome. They are not the signed-in app.
- Profile tab clicks (Replies, Media, Reposts) did not change the visible list in this pass. Those screenshots match the Threads tab.
- The phone light feed is not in the package. The app dialog stayed painted over it after a hide attempt. The phone dark feed is the clean phone capture. The phone light app dialog is `mobile-home-light-app-dialog.png`.
- Login field focus painted no outline. The declared focus ring is still in the stylesheet (`--focus-ring-blue`).
- Dialog radius, post-card radius, and icon sizes are Not captured.
- `--primary-button-background` is Facebook blue (`#1B74E4`). The Threads Log in pill is `--barcelona-primary-button` (`rgb(0, 0, 0)` in light). The token `accent` uses the Threads button, not the Facebook blue.
- Screenshots are 256-colour PNGs. Photos in the feed band.

## Fonts

Body and the left rail compute to `system-ui, -apple-system, "system-ui", Roboto, Helvetica, Arial, sans-serif`. The login fields compute to `Helvetica, Arial, sans-serif`. The stylesheet also declares Instagram faces (`IG Logo Font`, `Optimistic AI VF`). Those files are not in this package.

## Coverage

| Checklist item | Status | Where |
|---|---|---|
| Colour roles, light and dark | Captured | tokens.json `light` and `dark` |
| Type | Captured | Nav 15px/400, button 15px/600, field 15px/400. Display and caption sizes Not captured. |
| Spacing, radii, borders | Partly | Button radius 10px, field radius 18px, nav item 32px, button 34px, field 55px. Dialog radius Not captured. |
| Elevation | Partly | Scrim `--barcelona-dark-backdrop-background`. No shadow token. |
| Motion | Not captured | Durations are declared as `.25s`, which is not a DTCG duration (ms). Easings stay in raw/css-vars.json. |
| Button | Captured | [home-light-default.png](screenshots/home-light-default.png) |
| Icon button | Observed | Post more, back, cookie close |
| Link | Captured | Topic chips, footer links |
| Text field | Captured | Search and login fields. Not typed. |
| Text area | Not present | Composer is a login wall |
| Select | Not present | |
| Checkbox, radio | Not present | |
| Switch | Observed | Sounds panel, not toggled |
| Tabs | Observed | Profile tabs, URL unchanged |
| Menu | Captured | [home-light-more-menu.png](screenshots/home-light-more-menu.png) |
| Tooltip | Not present | |
| Dialog | Captured | Join, sign up to post, sign up to follow |
| Toast | Not present | |
| Card, list row, avatar | Observed | Feed |
| Table | Not present | |
| Badge | Not captured | Token exists, no badge on the signed-out chrome |
| App shell | Captured | Desktop rail and phone tab bar |
| Form validation | Not captured | Login form was not submitted |
| Empty, loading, error | Not captured | Search is empty of results because no query was typed. A video error ("Sorry, we're having trouble playing this video") appears inside a post, not as an app error state. |
| Destructive confirmation | Not present | |
| Search | Captured | [search-light-default.png](screenshots/search-light-default.png). No query typed. |
| Onboarding | Not captured | Sign-up is the Instagram wall |
| Themes | Captured | Light and dark |
| Widths | Captured | 1440 and 390. Phone light feed is missing; see What to distrust. |

## Do and don't

- **Do use black for the primary pill in light, and white in dark.** The Log in button is `light.accent` / `dark.accent`, not the Facebook blue in `--primary-button-background`. [home-light-default.png](screenshots/home-light-default.png), [home-dark-default.png](screenshots/home-dark-default.png).
- **Do keep the feed in a narrow centre column** with a rail on the left and a quiet login card on the right. [home-light-default.png](screenshots/home-light-default.png).
- **Do treat Continue with Instagram as a wall, not as a button to press in a capture.** [home-light-join-dialog.png](screenshots/home-light-join-dialog.png).
- **Don't invent a pressed or focus style.** Hover did not change the Log in fill, and the login field painted no outline. The declared focus ring is in the stylesheet and was not seen on a control.
- **Don't sample colours from the screenshots.** They are 256-colour PNGs. Read tokens.json.

## Rebuild

```bash
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  node systems/threads/tools/capture/public/measure-live.mjs
python3 systems/threads/tools/build_tokens.py
python3 systems/threads/tools/build_style_guide.py
python3 systems/threads/tools/capture/quantize.py ~/.design-systems/threads/raw-shots
```

Screenshots are recaptured with `node systems/threads/tools/capture/public/capture.mjs`.
