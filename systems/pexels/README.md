# Pexels design reference

A token set and component reference for the public Pexels site (www.pexels.com), for building a photo-and-video library in that style. Captured signed out on 2026-11-21 in headless system Chrome through Playwright, at 1440x900 and 390x844. The homepage, search, videos, discover, license, challenges, leaderboard, a published photo, a published video, content pages, the styled 404, and the login wall were loaded. No form was submitted. No email was typed. Google, Apple, and Facebook were not clicked.

Pexels paints one live theme: near-black ink (#191919) on white, a 12-step greyscale, and five named hues (alien green, jellyfish, papaya, strawberry, sunshine). Canva Sans sets the UI. Controls are 48px tall. The primary button is a 12px-radius ink pill. Selected nav items are black capsules. Search chips are full pills.

| File | What it is |
|---|---|
| [site-tree.md](site-tree.md) | Which control opens which page, menu, or dialog, mapped before screenshots |
| [icon.png](icon.png) | Site icon, 128 px PNG, from static.pexels.com |
| [tokens.json](tokens.json) | DTCG tokens: `core`, `light` (live), `dark` (declared on `[data-mode=dark]`, not applied on the public pages). Every token has `$extensions.source` |
| [DESIGN.md](DESIGN.md) | Written from the same generator `make design-md` uses, against an in-memory entry. `catalog.json` was not edited |
| [style-guide.html](style-guide.html) | Renders the tokens and the main controls. The toggle shows the declared dark set |
| [components.md](components.md) | Component inventory and gaps |
| [patterns.md](patterns.md) | How the pages combine |
| [screenshots/](screenshots) | 54 `{page}-light-{state}.png` captures, 256-colour. Desktop 1440x900 at 1x, `mobile-*` at 390x844 at 2x |
| [raw/](raw) | `css-vars.json` and `components-sample.json`. Full-colour shots stay in `~/.design-systems/pexels/raw-shots` |
| [tools/](tools) | Builders and the capture script `capture/public/pexels.mjs` |
| [components/](components) | Not created. No element crops in this pass. See components.md |

## Brief

<!-- brief:start -->
<!-- brief:end -->

## Health

<!-- health:start -->
<!-- health:end -->

## How the values were read

Custom properties were parsed from the live Next.js stylesheets on the homepage (system Chrome, Playwright). The greyscale and the five hues are declared on `[data-mode="light"], body` and again on `[data-mode="dark"]`. Computed styles of the Join button, its hover, the Home pill, the h1, the search container, a trending chip, and the License link were read on the homepage at 1440x900 and stored in [raw/components-sample.json](raw/components-sample.json). `python3 tools/build_tokens.py` turns those readings into [tokens.json](tokens.json).

`prefers-color-scheme: dark` did not change the body colours. No public page set `data-mode="dark"`.

## What to distrust

- The dark set is a stylesheet declaration. It was not on screen. Do not treat dark screenshots as evidence. There are none.
- `light.action.download` aliases `--color-alien-dark` (#32ac64). The Free download button looks that green, and its computed colour was not read.
- `light.text.muted` and `light.background.sunken` are declared greyscale steps, not measured on a specific element.
- Screenshots are 256-colour. Read colours from tokens.json.
- The cookie banner did not paint in the capture sessions. The first mapper saw its copy.
- The photo download chevron did not open a size menu. [photo-light-download-menu.png](screenshots/photo-light-download-menu.png) shows the search type menu instead.
- Discover's full-page shot is truncated at the kit's height cap (page was 23225px).
- Login wall text includes the product's own email placeholder. That is the field hint, not an account.

## Fonts

Canva Sans (Medium and Bold) and Canva Sans Display (Regular, Medium, Bold) are served from static.pexels.com as woff2. Proprietary. The style guide falls back to Helvetica Neue. Jersey 10 is also declared and was not used on the measured controls.

## Coverage

| Item | Status | Where |
|---|---|---|
| Colour roles, light | captured | `light.background`, `light.text`, `light.border`, `light.action` |
| Colour ramps | captured | greyscale 100–900 plus black, shadow, white. Five hues with four steps each |
| Dark theme | not captured live | Declared on `[data-mode=dark]`. Public pages did not apply it |
| Type | captured | display 48/700, body 14/400, label 17/400. No code face measured |
| Spacing | partly | 4, 8, 12, 16, 20 from measured paddings. Not a published scale |
| Radii | captured | 12, 25, 30, 180 |
| Elevation | not present | Measured controls have `box-shadow: none`. Dialogs dim the page. Scrim colour not sampled |
| Motion | partly | Join hover 100ms, border-color 250ms. Easing `ease` |
| Button, link, text field, tabs, menu, dialog, card, list row, avatar, badge | captured | [components.md](components.md) |
| Text area, select, switch, tooltip, toast, table | not present | Not on the public pages that loaded |
| Checkbox, radio | partly | Filter chips and the Cloudflare checkbox on the login wall. Not toggled |
| Hover | captured | Join button only |
| Focus-visible | partly | Search focus painted no ring |
| Pressed, disabled, loading, error | not captured | Nothing submitted. No disabled control held |
| App shell | captured | Home desktop and phone |
| Search and filtering | captured | Suggestions, ocean results, filter rail |
| Empty / error | captured | Styled 404 |
| Login wall | captured, then stopped | [login-light-wall.png](screenshots/login-light-wall.png) |
| Signed-in app, upload, onboarding, newsletter | not captured | `/upload/` redirects to `/login/`. `/join-contributor/` is a signup wall. Forms not filled |
| Cookie banner | not captured | Hid in the DOM. Never clicked |
| Download size menu | not captured | Click opened the search type menu |
| Phone hamburger | not captured | The more-icon click did not open a drawer |

## Do and don't

1. **Do set type in Canva Sans on white.** The homepage headline is 48px bold, tracking -2px, on a white page. [home-light-default.png](screenshots/home-light-default.png)
2. **Do make the one filled action ink, 48px, 12px radius.** Join is #191919 with white label. The selected nav pill is a black capsule. [home-light-default.png](screenshots/home-light-default.png)
3. **Do use the green only for download.** Free download is the alien green. Everything else in the chrome is ink or grey. [photo-light-default.png](screenshots/photo-light-default.png)
4. **Do keep search as a grey well, not an outlined field.** The home search is #f7f7f7, 12px radius, 72px tall. [home-light-default.png](screenshots/home-light-default.png)
5. **Don't invent a dark theme from the public site.** The dark custom properties exist and the captured pages never applied them.
6. **Don't submit the login form to see the app.** The wall stops at email, password, Google, Apple, and Facebook. [login-light-wall.png](screenshots/login-light-wall.png)

## Rebuild

```bash
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  node systems/pexels/tools/capture/public/pexels.mjs
python3 systems/pexels/tools/capture/quantize.py ~/.design-systems/pexels/raw-shots
python3 systems/pexels/tools/build_tokens.py
python3 systems/pexels/tools/build_style_guide.py
```

Capture needs the system Chrome channel. Bundled headless Chromium is stopped by Cloudflare after the homepage.
