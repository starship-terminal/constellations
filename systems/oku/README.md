# Oku design reference

A token set and component reference for Oku's public surface. Read from [oku.club](https://oku.club/) on 2026-11-21, signed out, in headless Chromium at 1440×900 (1x) and 390×844 (2x). Light is the default. Dark follows `prefers-color-scheme: dark`. There is no theme switch on the page.

Oku is a reading tracker. The public site is a marketing page, an explore grid, a blog, pricing, legal pages, and public book, profile, and review pages. The library editor, checkout, and account settings sit behind a signup wall and were not opened.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Oku's 128 px app icon, resized from the site's apple-touch icon |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds type, radius, space, size, and the button shadow. `light` and `dark` hold colour roles and a few component values. Every token has `$extensions.source`. |
| [DESIGN.md](DESIGN.md) | Not generated. This capture was told not to edit catalog.json, and `make design-md` only writes DESIGN.md for catalog entries. |
| [style-guide.html](style-guide.html) | Renders the measured roles and the main controls, with a light/dark toggle |
| [components.md](components.md) | Component inventory, crops, and gaps |
| [patterns.md](patterns.md) | How the public pages are put together |
| [site-tree.md](site-tree.md) | Which control opens which page, menu, dialog, or wall |
| [components/](components/) | 12 crops in [components/crops/](components/crops/) |
| [screenshots/](screenshots/) | 78 captures. Desktop and phone, light and dark. Tiles are the scrolled page. |
| [raw/](raw/) | [capture-readings.json](raw/capture-readings.json), [components-computed.json](raw/components-computed.json), [css-vars.json](raw/css-vars.json) |
| [tools/](tools/) | Builders and the Playwright capture script |

## Brief

Oku's public UI is black ink on white, or near-white ink on #131314. Display type is FabricSerifWeb. UI type is Inter. Controls are 8px radius. The only accent is the ink of the Join button. There is no separate brand hue on the chrome.

Take values from [tokens.json](tokens.json). The screenshots are 256-colour.

## Health

Not generated. `make grade` writes Health from the catalog, and this capture was told not to edit catalog.json. A reviewer still needs to grade the package before it can sit in the gallery.

## How the values were read

Headless Playwright, signed out. No password, code, email, or phone was typed. No form was submitted. Google, Facebook, and Apple were not clicked.

- Custom properties: the site's CSS was harvested from network responses. Oku declares none of its own. The 34 names are `--toastify-*` and `--swiper-*`. They are recorded as not tokenised in [raw/css-vars.json](raw/css-vars.json).
- Computed styles: [tools/capture/public/oku-public.mjs](tools/capture/public/oku-public.mjs) and a follow-up measure pass wrote [raw/capture-readings.json](raw/capture-readings.json) and [raw/components-computed.json](raw/components-computed.json). [tools/build_tokens.py](tools/build_tokens.py) turns those readings into tokens.
- Screenshots: the same script, at the measured viewports. Sidecars (`*.png.capture.json`) stayed in the scratch folder. [tools/capture/quantize.py](tools/capture/quantize.py) wrote the 256-colour copies.

The Join dialog and the book status buttons open a signup form. The form was photographed empty and closed. `/signin` was photographed as a wall and not filled.

## What to distrust

- This is the public site. The signed-in library is unknown.
- Dark is a browser preference, not a toggle the page offers.
- Hover and focus did not change the Join button's fill. Do not invent a hover colour.
- The header is transparent. A screenshot of the hero can make the header look white because the page behind it is white.
- Privacy and terms screenshots had a published contact address, a street, and a VAT number painted out before quantize. The raw shots outside the repo were masked the same way. Do not read those lines back from the images.
- Quantised PNGs are not a source of colour. Read tokens.
- Section heading size (36px h2) was seen below the fold in an earlier probe and is not in tokens.json. Not captured.
- Pressed, disabled, loading, and error states were not held.

## Fonts

Inter for UI, with the system sans stack as fallback. FabricSerifWeb for display, book titles, and prices, with Georgia as the computed fallback. Neither file is in this package.

## Coverage

| Expectation | Status | Where |
|---|---|---|
| Colour roles, light and dark | captured | `light.color.*`, `dark.color.*` |
| Type | captured | `core.font.*` for display, book, body, nav, button, field, price |
| Section heading size | not captured | h2 was below the first viewport; not in the sidecar readings |
| Spacing scale | not present | no spacing tokens in CSS. Measured paddings are `core.space.*` |
| Radii | captured | 8px controls, 20px dialog |
| Borders | captured | Sign in inset ring, field border |
| Elevation | captured | one button shadow. No card shadow. |
| Motion | not captured | no running transition was read |
| Button, link | captured | Join, Sign in, nav links |
| Text field | captured | empty, inside the signup dialog |
| Dialog | captured | Join dialog, both themes |
| Menu | captured | phone menu |
| Card, list row, tabs | observed | book grid, activity feed, book tabs. No separate fill token. |
| Text area, select, checkbox, radio, switch, tooltip, toast, table, avatar, badge | not present | none on the public surface |
| Hover, focus colour | not present | computed styles matched default. Focus ring width was 0. |
| Pressed, disabled, loading, error | not captured | not shown, or not held |
| Form validation | not captured | no form was submitted |
| Search | not present | explore has no field |
| Signed-in library, checkout | not captured | signup wall |
| Widths 1440 and 390 | captured | desktop 1x, phone 2x. Sidecars record innerWidth. |
| Themes | captured | light default, dark via prefers-color-scheme |

## Do and don't

1. **Do set type in a serif for the display line and a sans for the chrome.** The hero is FabricSerifWeb at 48px. Nav and buttons are Inter. See [home-light-default.png](screenshots/home-light-default.png).
2. **Do use ink as the only accent.** Join is black on white, or #e0e1e4 on #131314. There is no second brand colour on the controls. See [join-button-default.png](components/crops/join-button-default.png).
3. **Do keep the header transparent and the corners small.** 8px on buttons and fields, 20px on the dialog, no radius on the page. See [header-default.png](components/crops/header-default.png).
4. **Do open Join as a dialog, not a new page, when it is the header button.** The dialog is 480px over a 60% black scrim. See [home-light-join-dialog.png](screenshots/home-light-join-dialog.png).
5. **Don't style the signed-in library from this package.** Those screens were not opened.
6. **Don't add a hover fill.** The measured hover matched the default.

## Rebuild

From `systems/oku/`:

```sh
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

Live recapture needs Playwright at `PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs`:

```sh
node tools/capture/public/oku-public.mjs
python3 tools/capture/quantize.py ~/.design-systems/oku/raw-shots
```

`make design-md`, `make grade`, and `make check` need a catalog.json entry. This capture was told not to add one.
