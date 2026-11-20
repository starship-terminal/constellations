# West Elm design reference

A token and component reference for West Elm (westelm.com), the Williams-Sonoma furniture store. Captured 2026-11-21, signed out, in headed Chrome through Playwright. Headless Chromium received HTTP 403 on every URL. Desktop shots are 1440x900 at 1x. Phone shots are 390x844 at 2x, except the privacy page, whose measured inner width drifted to 405 on the first pass.

The pages that loaded are the home page, the store locator, customer service, track order, the privacy policy, the registry marketing page, and the login page. `/shop/`, `/pages/`, `/products/`, `/favorites/` and `/shoppingcart/` returned HTTP 403, including clicks that started on the loaded homepage. The login page asks for an email. No email was typed and no form was submitted.

One light theme. No dark-theme control was found.

| File | What it is |
|---|---|
| [site-tree.md](site-tree.md) | Which control opens which page, menu or dialog, and which branches stopped |
| [icon.png](icon.png) | Site favicon, resized to 128 px from the `.ico` the homepage declares |
| [tokens.json](tokens.json) | DTCG tokens: `core` and `light`. Every token has `$extensions.source` |
| [DESIGN.md](DESIGN.md) | Not generated. `make design-md` needs a catalog.json entry, and this capture was told not to edit catalog.json |
| [style-guide.html](style-guide.html) | Renders the measured tokens. Fallback fonts, because GT Eesti Text and Sanomat are proprietary |
| [components.md](components.md) | Controls that were on the loaded pages, and the gaps |
| [patterns.md](patterns.md) | How those pages are assembled |
| [screenshots/](screenshots) | 35 quantised PNGs, `{page}-light-{state}.png` |
| [raw/](raw) | `component-tokens.json`, the readings the builder consumed. Full-colour PNGs stay in `~/.design-systems/westelm/raw-shots/` |
| [tools/](tools) | Kit copy plus the adapted token builder |

## Brief

<!-- brief:start -->

Not generated. `make brief` reads catalog.json, and this capture was told not to edit catalog.json.

<!-- brief:end -->

## Health

<!-- health:start -->

Not generated. `make grade` reads catalog.json, and this capture was told not to edit catalog.json.

<!-- health:end -->

## How the values were read

Headed Chrome (`channel: chrome`) loaded westelm.com. Computed styles were read on the live DOM for body, the homepage h1, primary and secondary nav, the utility row, the footer, the SHOP NOW control, the search input, and the focused login email field. The promo band colour `#5b081a` and the SALE label `#bf4759` were sampled from the full-colour home screenshot before quantize, because the band's computed background sat on a transparent wrapper. Custom properties in the CSSOM are Tailwind internals (`--tw-*`) and were not tokenised. Stylesheet URLs 403'd to curl, so they were not parsed from disk.

## What to distrust

- The promo and SALE colours are sampled pixels, not declared tokens. Label them Sampled.
- Font weight 375 is the computed value the browser reported. It is not a guess, and it is also not a weight most font files ship.
- Registry h1 measured 64px in a later pass. The display token is the homepage h1 at 48px.
- Screenshots are 256-colour PNGs. Read colours from tokens.json.
- The phone privacy shot's first capture measured innerWidth 405. The recapture of the default viewport was requested at 390. Check the sidecar before treating that file as a 390 capture.
- Shop, product, cart and favorites were not seen. Do not invent their components from the home tiles.

## Fonts

GT Eesti Text (body, nav, buttons) and Sanomat (display headings) are proprietary. The style guide falls back to Helvetica and Georgia. Font files were not committed.

## Coverage

| Expectation | Status | Where |
|---|---|---|
| Page, surface, text, muted, border | captured | `light.background.page`, `light.background.surface`, `light.text.primary`, `light.text.muted`, `light.border.default` |
| Accent | captured, sampled | `light.text.sale` and `light.background.promo` are sampled pixels |
| Dark theme | not present | no theme switch on the loaded pages |
| Type roles | captured | `core.typography` for display, nav, utility, body, button, secondary, field |
| Radius | captured | `core.radius.none` is 0px on the measured controls |
| Spacing and sizing | captured | `core.space`, `core.size` |
| Motion | not captured | durations were not read |
| Elevation | not present | measured controls had `box-shadow: none` |
| Button | captured, resting only | [login-light-default](screenshots/login-light-default.png) |
| Link | captured | [home-light-default](screenshots/home-light-default.png) |
| Text field | captured, default and focus | [login-light-email-focus](screenshots/login-light-email-focus.png) |
| Menu | captured | [home-light-nav-furniture](screenshots/home-light-nav-furniture.png), [mobile-home-light-menu](screenshots/mobile-home-light-menu.png) |
| Dialog | captured, then dismissed without submit | [home-light-signup](screenshots/home-light-signup.png) |
| Text area, radio, switch, tabs, tooltip, toast, table, avatar | not present | not on the loaded pages |
| Select, checkbox | not captured | present on the store locator and track-order form, states not measured |
| Product list, product page, cart, search results | not captured | HTTP 403 |
| Signed-in account, checkout | not captured | login asks for an email; branch stopped |
| 1440 and 390 | captured | [screenshots/](screenshots) |
| Icons | not captured | brand artwork not extracted ([docs/RIGHTS.md](../../docs/RIGHTS.md)) |

## Do and don't

- **Do set type in GT Eesti Text on white, and headlines in Sanomat.** Body is 12px weight 300, ink on white. [home-light-default](screenshots/home-light-default.png)
- **Do keep corners square.** Measured buttons, fields and nav report 0 radius. [login-light-default](screenshots/login-light-default.png)
- **Do use one ink fill for the primary action.** CONTINUE WITH EMAIL and SHOP NOW are `rgb(33, 33, 33)` with a white uppercase label. [login-light-default](screenshots/login-light-default.png)
- **Do put the sale voice in the burgundy band.** The home promo sits under the nav. The band colour is a sampled pixel, `#5b081a`. [home-light-default](screenshots/home-light-default.png)
- **Don't follow a shop, cart or account link and expect a capture.** Those URLs 403'd or asked for an email. [site-tree.md](site-tree.md)
- **Don't fill the email field.** The login page and the signup dialog both ask for one. Neither was submitted. [login-light-default](screenshots/login-light-default.png)

## Rebuild

```sh
cd systems/westelm
python3 tools/build_tokens.py
```

Screenshots were taken by a headed Playwright script that is not checked in as a page runner. Raw PNGs live in `~/.design-systems/westelm/raw-shots/`. Quantize with:

```sh
python3 tools/capture/quantize.py ~/.design-systems/westelm/raw-shots
```

`make design-md`, `make brief` and `make grade` need a catalog.json entry. This capture was told not to add one.
