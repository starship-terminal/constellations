# Granola

Public marketing site for Granola, the AI notepad for back-to-back meetings, captured 2026-11-21 from https://www.granola.ai/. Signed out. One painted light theme. Desktop 1440 and phone 390. The notes host at https://notes.granola.ai/download returned HTTP 500 and then painted a "preparing download" page. https://notes.granola.ai/login returned HTTP 500 and painted a login wall (Google, Microsoft, SSO). Those buttons were not clicked. No email, password, or code was typed. No form was submitted.

This is a new package. `origin/main` had no `systems/granola/` folder. The iOS app is listed in `ios-manifest.json` and was not captured.

| Path | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [site-tree.md](site-tree.md) | Which homepage control opens which page, menu, or dialog |
| [login-review.json](login-review.json) | Offered nav, settings, and create, plus screens and gaps |
| [tokens.json](tokens.json) | Measured colour, type, radius, and motion tokens |
| [DESIGN.md](DESIGN.md) | Not generated. Generating it needs a catalog entry, and this capture does not edit `catalog.json` |
| [style-guide.html](style-guide.html) | Renders the light tokens |
| [components.md](components.md) | Components seen on the public site, with measured values |
| [patterns.md](patterns.md) | Homepage, pricing, dialog, and login-wall patterns |
| [screenshots/](screenshots/) | 17 public-state PNGs, 256-colour |
| [icon.png](icon.png) | 128 px site icon from the apple-touch icon |
| [raw/](raw/) | CSS custom properties and computed component styles |
| [tools/](tools/) | Builders. `python3 tools/build_tokens.py` rebuilds `tokens.json` |
| [icons/](icons/) | Icon redraws |

## Brief

Not generated. `make brief` reads the catalog entry, and this capture does not edit `catalog.json`.

## Health

Not generated. `make grade` reads the catalog entry.

## How the values were read

Custom properties were read from the stylesheets on https://www.granola.ai/ into [raw/css-vars.json](raw/css-vars.json). Semantic colour uses the `--oats-*` names declared on `:root`. Primitive ramps use `--color-oats-*` on `:host, :root`. Component sizes (hero button, nav link, dialog field, dialog submit) were read with `getComputedStyle` into [raw/components.json](raw/components.json). `<meta name="theme-color">` is `#ffffff`. No mask-icon colour was present.

The iubenda cookie banner was removed in the page for the measured shots. Reject all and Accept all were not clicked.

## What to distrust

The marketing site paints light only. A dark `--oats-*` block exists in CSS and is not a public theme, so there is no dark token set.

The hero `h1` computed at 86.4 px. That size is not a `--text-*` token. The type scale in `tokens.json` is the declared scale, not the hero size.

`rounded-full` computed as `3.35544e+07px`. The pill token records that sentinel. It is not a designed radius in pixels.

Focus on the header Download link used the browser default outline (`rgb(7, 86, 178)`), not `--oats-border-focus`. The token is the declared focus border. The computed outline is in `raw/components.json`.

Screenshots are 256-colour PNGs. Read colours from `tokens.json`.

The Features menu screenshot was taken after the open menu's inline style was held so the shot could land. The menu does open on pointer enter. The phone drawer screenshot was taken after the Open menu button's React `onClick` ran. A Playwright click on that button did not open it in this session.

https://www.granola.ai/download paints "Redirecting..." and points at the notes host. That host returned HTTP 500. The painted "preparing download" page is what the browser showed after the 500. It is not a reconstructed download page.

The login wall screenshot is the painted result of HTTP 500 on https://notes.granola.ai/login. Google, Microsoft, and SSO were not clicked.

## Fonts

`--font-sans` is "KMR Melange Grotesk" with a system fallback. The painted body family was `melange, "melange Fallback"`. `--font-display` and `--font-quadrant` are "Quadrant Notepad". `--font-mono` is JetBrains Mono. The webfont files were not copied. Tokens name the stacks the site declares.

## Coverage

| Item | Status |
|---|---|
| Colour roles, light | Captured. [tokens.json](tokens.json) `light` |
| Colour roles, dark | Not captured. No public theme toggle. Dark CSS was not applied |
| Type scale | Captured from `--text-*` and `--font-*` |
| Spacing | Captured as `--spacing` (0.25rem). A full named scale was not declared |
| Radii | Captured from `--radius-*` plus the pill sentinel |
| Elevation | Not captured as a scale. Dialog overlay scrim is measured |
| Motion | Captured easings `--ease-out`, `--ease-out-expo`, `--ease-in-out`. Durations were not a named scale |
| Button | Captured. Hero "Download for free", dialog "Send link". [screenshots/home-light-default.png](screenshots/home-light-default.png) |
| Link, nav | Captured. Header links |
| Text field | Captured, empty. Dialog email field. Not typed. [screenshots/home-light-mobile-dialog.png](screenshots/home-light-mobile-dialog.png) |
| Menu | Captured. Features hover menu. [screenshots/home-light-features-menu.png](screenshots/home-light-features-menu.png) |
| Dialog | Captured. Granola for mobile. Email not submitted |
| Tabs | Observed. iOS and Android labels in the mobile dialog. Not switched |
| Cookie banner | Present, not clicked. [screenshots/home-light-cookie.png](screenshots/home-light-cookie.png) matches the default shot after the banner was removed in later runs |
| Login wall | Photographed, not entered. [screenshots/notes-login-error.png](screenshots/notes-login-error.png) |
| Download host | HTTP 500, then a preparing-download paint. [screenshots/notes-download-error.png](screenshots/notes-download-error.png) |
| Signed-in app, settings, create | Not present on the public site |
| Checkbox, radio, switch, select, toast, table, avatar, badge | Not present on the pages photographed |
| Phone 390 | Captured. Home and pricing, plus the phone drawer |

## Do and don't

- **One olive accent on a warm off-white page.** Primary actions are pills filled with `#5b6f00`. Secondary actions are quiet pills. See [screenshots/home-light-default.png](screenshots/home-light-default.png) and [screenshots/pricing-light-default.png](screenshots/pricing-light-default.png).
- **Display type is Quadrant, UI type is Melange.** The hero is the display face. Nav, buttons, and body are the grotesque. See [screenshots/home-light-default.png](screenshots/home-light-default.png).
- **Features is a hover menu, not a page.** It lists Notepad, Chat, Mobile & Watch, MCP, and Voice typing. See [screenshots/home-light-features-menu.png](screenshots/home-light-features-menu.png).
- **Mobile download is a dialog, not a new page.** It asks for a work email and shows iOS and Android. Do not submit that field from a capture. See [screenshots/home-light-mobile-dialog.png](screenshots/home-light-mobile-dialog.png).
- **Stop at the notes host.** Download and login returned HTTP 500. Do not invent the app behind Google, Microsoft, or SSO. See [screenshots/notes-login-error.png](screenshots/notes-login-error.png).

## Rebuild

```bash
cd systems/granola && python3 tools/build_tokens.py && python3 tools/build_style_guide.py
```

`DESIGN.md` is not rebuilt here. `make design-md` writes it from the catalog, and this capture does not edit `catalog.json`.
