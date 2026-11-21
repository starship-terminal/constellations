# Doppler design reference

A token set and site map for Doppler's public web surfaces. Read signed out on 2026-11-21 from [www.doppler.com](https://www.doppler.com/) and [docs.doppler.com](https://docs.doppler.com/docs/start), in headless Chromium at 1440 and 390. The marketing site paints one dark theme. Docs paint a light page. The dashboard at `dashboard.doppler.com` is a login wall (email and password, or Google or GitHub). That branch stops. No form was filled.

The site map, including which control opens which page, is [site-tree.md](site-tree.md).

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site icon, 128 px PNG, rasterised from the SVG the home page declares |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds the brand palette and measured type, radius, and spacing. `dark` is the marketing site. `light` is the docs chrome. Every token carries `$extensions.source` |
| [DESIGN.md](DESIGN.md) | Generated export of the tokens. One theme, no provenance. Take values from tokens.json |
| [style-guide.html](style-guide.html) | Renders the measured palette, the two button recipes, and the docs chrome |
| [components.md](components.md) | Which checklist components the public site shows, and which sit behind the login wall |
| [patterns.md](patterns.md) | Marketing shell, docs shell, filters, and the demo form that was not submitted |
| [site-tree.md](site-tree.md) | Control-to-page map of the public site, desktop and phone |
| [screenshots/](screenshots) | Viewport captures at 1440 (1x) and 390 (2x), plus opened menus, search, one FAQ, and one filter |
| [raw/](raw) | Live CSS custom properties, computed component styles, theme checks |
| [tools/](tools) | Builders and the capture kit copy |

## Brief

<!-- brief:start -->
Brief is not generated. This package is not in catalog.json, by request: a capture PR that edits catalog.json is rejected. Run `make brief` only after a catalog entry exists.
<!-- brief:end -->

## Health

<!-- health:start -->
Health is not generated. Grades need a catalog entry. The coverage table below is the record of what was read.
<!-- health:end -->

## How the values were read

Playwright loaded the public pages. Computed styles were read on the home header, the Start for Free control (default, hover, focus), the h1, and the docs h1. Custom properties on the marketing sheets are mostly Tailwind internals (`--tw-*`) plus `--global-ease` and `--global-transition`. Those two stay in [raw/css-vars-merged.json](raw/css-vars-merged.json) and are not promoted to tokens. Brand hex labels on `/brand` match the computed page and accent colours. The font family is the computed Next.js local name `__DopplerRepro_a18e76`. The real family name and its licence were not captured.

## What to distrust

Screenshots are 256-colour PNGs. Read colours from tokens.json. The Sign In colour was read from a zero-width duplicate in the desktop DOM. Display type at 390 uses a derived line-height. Docs focus colour was not read. Purple, carmine, lilac, and yellow are brand-page labels, not roles painted on the home page. There is no light theme of the marketing site.

## Fonts

Marketing: `__DopplerRepro_a18e76` with a fallback of the same name, then sans-serif. Licence not captured. Docs: system-ui stack, read from the docs h1. The style guide uses system-ui so it does not fetch a font.

## Coverage

| Item | Status |
|---|---|
| Colour roles, marketing dark | captured: page, text, accent, accent hover, on-accent, border strong, focus. Raised, overlay, scrim, disabled, link: not captured |
| Colour roles, docs light | captured: page and text. Other roles not captured |
| Type | captured: display 48/450, body 16/400, button 16/400, docs heading 31/600. Scale of 6 to 8 sizes: not present in the readings |
| Spacing, radius, border width, header height | captured |
| Elevation | header shadow is none. No elevation scale |
| Motion | two globals in raw, not a component scale. Not captured as tokens |
| Button | default, hover, focus-visible. Pressed, disabled, loading: not captured |
| Menu | captured (three header menus, phone menu) |
| Search | docs panel opened, empty |
| Accordion | pricing FAQ opened |
| Filter | customers AI filter captured |
| Text field, select, checkbox, radio, switch, tooltip, dialog, toast, table, avatar, badge | not present on the pages used, or behind the login wall |
| Signed-in app | not captured: login wall |
| Dark theme of marketing | the only marketing theme |
| Light theme of marketing | not present |
| Docs theme toggle | not present |
| Desktop 1440 and phone 390 | captured |

## Do and don't

**Do** use one green for the primary action. Start for Free is fluorescent green on warm black. Screenshot: [home-dark-default.png](screenshots/home-dark-default.png).

**Do** keep secondary actions as an outline. Get Demo is a warm-white stroke, not a second fill. Screenshot: [home-dark-default.png](screenshots/home-dark-default.png).

**Do** keep docs on a light page. The docs host does not share the marketing ground. Screenshot: [docs-start-light-default.png](screenshots/docs-start-light-default.png).

**Don't** invent a light marketing theme. Emulating a dark colour scheme did not change the page, and no toggle exists.

**Don't** treat the dashboard as captured. Sign In opens a login wall. Screenshot of the wall was taken and left out of the package so a form is not stored.

## Rebuild

```bash
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

Run from `systems/doppler`. Inputs are the JSON files in `raw/`.

## Catalog

This folder is not registered in catalog.json. The capture request forbids that edit. `make check` will report `systems/doppler has no catalog.json entry` until a later change adds one.
