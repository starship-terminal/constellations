# Microsoft design reference

A token set and component reference for the public Microsoft homepage. Read signed out on 2026-11-21 from https://www.microsoft.com, which redirected to https://www.microsoft.com/en-sg. Also read, still on www.microsoft.com: products, Microsoft 365, Windows, Surface, Sale, and the sitemap. Desktop captures are 1440 by 900 at 1x. The phone capture is 390 by 844 at 2x. One painted light theme. Sign in left for login.live.com and was not submitted. Azure, Copilot, XBOX, and Support leave this host and were not captured as this package.

The homepage paints actions in Fluent blue, `#0078d4`, on Segoe UI Variable Text. The stylesheet declares the same blue as `--ds-color-brilliant-blue-500` and `--ds-theme-border-accent-strong-normal`.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site icon, 128 px, from the homepage favicon |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds type, spacing, and radius. `light` holds painted roles and declared `--ds-*` roles. Every token carries `$extensions.source`. |
| [DESIGN.md](DESIGN.md) | Written from tokens.json and this README. Catalog registration was out of scope, so `make design-md` was not run. |
| [style-guide.html](style-guide.html) | Renders the tokens and the main controls. One theme, so no toggle. |
| [components.md](components.md) | Button, link, search field, and heading, with crops |
| [patterns.md](patterns.md) | Header, All Microsoft menu, search, hero, and footer |
| [site-tree.md](site-tree.md) | Which homepage control opens which page, menu, or dialog |
| [login-review.json](login-review.json) | Offered nav, settings, and create, plus the screens that exist |
| [components/crops/](components/crops) | 5 element screenshots |
| [screenshots/](screenshots) | `{page}-light-{state}.png`. Desktop 1440 by 900 at 1x. `mobile-home` at 390 wide, 2x. |
| [raw/](raw) | Computed styles, resolved `--ds-*` values, and viewport metadata |
| [tools/](tools) | [build_tokens.py](tools/build_tokens.py) and [capture_public.mjs](tools/capture_public.mjs) |
| [icons/](icons/) | Icon redraws |

## Brief

Not generated. `make brief` reads catalog.json, and this capture was told not to edit that file.

## Health

Not generated. `make grade` reads catalog.json, and this capture was told not to edit that file.

## How the values were read

Playwright opened the public URLs signed out, at 1440 by 900 (device pixel ratio 1) and 390 by 844 (device pixel ratio 2). No account was used. The script read `getComputedStyle` on the hero heading, the universal header, the Shop now link, and the Search Microsoft.com field. It also resolved `--ds-*` custom properties on `:root`. Hover and focus on Shop now were forced with Playwright hover and focus, then read again. The T3 preview tab loaded the same homepage and confirmed the locale, the heading, and the nav labels. Its screenshot API returned no frames (`The browser is not producing screenshot frames`), so the PNGs come from Playwright.

## What to distrust

`--ds-color-brilliant-blue-500` is `#0078d4` and matches the painted Shop now fill. The hover stop `#006dc1` matches the computed hover. Pressed `#004275` is the declared ramp stop. It was not held on a pointer.

Several `--ds-theme-foreground-*` values are gradients. They are not the heading colour. The heading computed to `#0e1726`.

`color-scheme` was `normal`. No dark theme was painted, and no theme toggle was found. A reconstruction that adds a dark theme would be a guess.

The All Microsoft menu lists Azure, Copilot, and XBOX. Those hosts are not this package. The login wall screenshot was deleted because its URL carried OAuth state.

Screenshots are full-colour PNGs from this capture, not the kit's 256-colour quantize pass. Read values from tokens.json anyway.

## Fonts

The hero and body compute to Segoe UI Variable Text, then Segoe UI, segoeui, Helvetica Neue, helvetica, arial, sans-serif. The universal header computes to Segoe UI, SegoeUI, Helvetica Neue, Helvetica, Arial, sans-serif. Those files are proprietary and are not in this package. The tokens name the computed families and the same fallbacks.

## Coverage

| Checklist | Status |
|---|---|
| Colour roles, one theme | Captured. Painted page, header, action, heading, and nav in tokens.json. Declared brilliant-blue and status ramps kept beside them. |
| Type | Captured. Hero 48/56, button 15/22, nav 13, search field 16. Declared body 14, 16, and 20. |
| Spacing | Captured from `--ds-spacing-*` (2 to 72). |
| Radius | Captured. 8px on Shop now. 0 on the search field. No other radius scale was declared under a `--ds-radius-*` name. |
| Border | Captured. Search field 1px `#0067b8`. Declared accent `#0078d4`. |
| Elevation | Not a painted shadow. Shop now computed a zero-spread shadow. Header computed none. |
| Motion | Not captured as a scale. No duration custom property resolved on `:root`. |
| Layout | 1440 and 390 captured. Header is 54px. |
| Button | Default, hover, focus. Pressed and disabled not captured. |
| Link | Header Windows link measured. Crop is the search and menu screenshots. |
| Text field | Search Microsoft.com captured, including focus. Nothing typed. |
| Heading | Home h1 captured at both widths. |
| Icon button | Search, cart, and the phone menu are in the screenshots. No separate crop. |
| Menu | All Microsoft menu captured at 1440. Phone nav captured at 390. |
| Badge | "New" is in the home screenshot. Its fill was not isolated from the parent. |
| Text area, select, checkbox, radio, switch, tabs, tooltip, dialog, toast, table, avatar, list row | Not present as product controls on the public homepage. The products page shows an Animation switch. It was not toggled. |
| App shell, form error, empty, loading, destructive confirm, onboarding | Not on the public homepage. Account settings need a Microsoft account. |
| Themes | Light only. |

## Do and don't

1. **Do paint homepage actions Fluent blue.** Shop now is `#0078d4`, hover `#006dc1`, label white, 8px radius, 48px tall. See [button-primary-default](components/crops/button-primary-default.png).
2. **Do set the homepage hero in Segoe UI Variable Text at 48px.** The home h1 is 48px / 56px, weight 500, tracking -1.2px, colour `#0e1726`. See [home-light-default](screenshots/home-light-default.png).
3. **Do keep the universal header at 54px on white.** Nav labels are 13px Segoe UI, `#262626`. All Microsoft opens a six-column menu. See [home-light-menu-all-microsoft](screenshots/home-light-menu-all-microsoft.png).
4. **Do open search in the header, not as a new page.** The field is 36px, square, 1px `#0067b8`, with a 2px outline in the same colour. See [text-field-focus](components/crops/text-field-focus.png).
5. **Don't follow Sign in into this package.** It leaves for login.live.com. Stop there.
6. **Don't treat Azure, Copilot, or XBOX as this package.** Those links leave www.microsoft.com.

## Rebuild

```bash
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture_public.mjs
python3 tools/build_tokens.py
```

## Colors

Page is white. Actions are `#0078d4`. Headings are `#0e1726`. Nav text is `#262626`.

## Typography

Segoe UI Variable Text for the hero and buttons. Segoe UI for the universal header.

## Layout

Header 54px. Content inset 72px on the desktop hero. Phone width 390.

## Components

Shop now, the search field, and the All Microsoft menu are the controls this capture measured.

## Do's and Don'ts

Take the blue from the computed Shop now fill. Leave login.live.com out of this package.
