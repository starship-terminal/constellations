# Epidemic Sound design reference

Public signed-out design system for Epidemic Sound, the music and sound-effects licensing site. Captured from [https://www.epidemicsound.com/](https://www.epidemicsound.com/) on 2026-11-21 in headless Chromium at 1440 and 390, signed out. One light marketing theme. Login, signup, checkout, and identity providers were not opened.

The page is off-white (`#f1f0eb`) with black text and black pill buttons. Display type is Sebenta. UI type is Inter. The product's own `--es-color-*` tokens describe a dark player palette. That palette is declared on the page and was not the painted marketing theme.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site icon, 128 px, from the public icon link |
| [tokens.json](tokens.json) | DTCG tokens: `core` scales and a `light` semantic set. Every token has `$extensions.source` |
| [DESIGN.md](DESIGN.md) | Generated export of the light theme. Take values from tokens.json |
| [style-guide.html](style-guide.html) | Renders the light tokens and the two button fills |
| [components.md](components.md) | Controls that were measured, with crops |
| [patterns.md](patterns.md) | Header, pricing, and catalog patterns |
| [site-tree.md](site-tree.md) | Public page tree and which control opens which page or panel |
| [components/crops/](components/crops/) | Element crops |
| [screenshots/](screenshots/) | Page captures at 1440 and 390 |
| [raw/](raw/) | CSS variable readings, computed styles, and [raw/site-tree.json](raw/site-tree.json) |
| [tools/](tools/) | Builders and the capture helper |

## Brief

<!-- brief:start -->
Read [tokens.json](tokens.json) before designing in this style. The catalog entry for this package is not in this pull request.

### Principles

1. Do set display type in Sebenta on off-white.
2. Do use black pills for the primary action.
3. Do keep secondary actions as a quiet grey fill.
4. Do open navigation as a white panel, not a new page.
5. Don't treat the dark `--es-color-*` set as the marketing theme.
6. Don't follow login, signup, or checkout.

Each rule is tied to a screenshot under [Do and don't](#do-and-dont).

### Using tokens

| Role | light |
|---|---|
| page | #f1f0eb `light.background.page` |
| surface | #ffffff `light.background.surface` |
| text | #000000 `light.text.primary` |
| muted | rgba(0, 0, 0, 0.6) `light.text.muted` |
| accent | #000000 `light.accent` |
| border | #000000 `light.border.default` |

Fonts: `core.font.display` is Sebenta; `core.font.sans` is Inter. Scales: 5 type styles, 4 radius steps, 4 spacing steps.

### Using components

[components.md](components.md), [patterns.md](patterns.md), crops in [components/crops/](components/crops/), and [style-guide.html](style-guide.html).

### Accessibility

Text on page is black on #f1f0eb. Muted footer links are black at 60% opacity. Focus on the primary button is a 2px white outline (`core.focus.outline-color`). The declared focus token `--es-color-misc-focused` is #20afff and was not what the public button painted.
<!-- brief:end -->

## Health

<!-- health:start -->
Not graded in this pull request. catalog.json was not edited, so `make grade` was not run for this package.
<!-- health:end -->

## How the values were read

Playwright loaded the public pages. `#es-cookie-banner` was hidden with CSS. Accept was not clicked. Custom properties were read from the live CSSOM. Control sizes, colours, and type were read with `getComputedStyle` at 1440. Screenshots are 256-colour PNGs. Read colours from [tokens.json](tokens.json), not from the PNGs.

## What to distrust

- The `--es-color-*` dark palette is declared and not the painted marketing theme. It is in [raw/css-vars.json](raw/css-vars.json) and not in the `light` set.
- `--es-radius-button` is 0 on `body`. Public buttons measure 10000px because `.radii-override` sets the token to a pill. The token file records the measured pill.
- Header "Log in" was in the DOM and not visible at 1440 in this capture, so its crop is missing. The mobile drawer shows it.
- Sebenta and Inter are proprietary. The style guide uses Georgia and a system sans.
- Full-page shots taller than 7200px are truncated. The boundary is in the capture log.
- Genre, artist, and track URLs repeat a few templates. Not every catalog URL was opened.

## Fonts

Sebenta (weight 500, roman and italic) is the display face. Inter (400 to 700) is the UI face. Both are served by the site and are not redistributed here. Fallbacks recorded on the page: Georgia, Times New Roman, Noto Serif for Sebenta; Arial and Helvetica Neue for Inter.

## Coverage

| Item | Status | Where |
|---|---|---|
| Page, surface, text, muted, border | captured | `light.background.*`, `light.text.*` |
| Accent | captured | black primary fill. Brand yellow is declared, not a painted marketing accent |
| Dark theme | not present | no public toggle. Product dark tokens are declared only |
| Type | captured | `core.typography` |
| Radius, size, space | captured | `core.radius`, `core.size`, `core.space` |
| Motion | partly | 150ms on buttons measured; `--animation-duration` 600ms declared |
| Button, link, menu, switch, search, card | captured | [components.md](components.md) |
| Text area, select, checkbox, radio, tabs, tooltip, toast, table, avatar | not present | not on the measured public pages |
| Dialog | not captured | cookie dialog was hidden, not accepted, and not photographed as a component |
| Login, signup, checkout | not captured | stopped. See [site-tree.md](site-tree.md) |
| 1440 and 390 | captured | [screenshots/](screenshots/) |

## Do and don't

- **Do set display type in Sebenta on off-white.** The hero is 80px Sebenta on #f1f0eb ([home](screenshots/home-light-default.png)).
- **Do use black pills for the primary action.** Create free account is a 44px black pill ([button](components/crops/button-primary-default.png)).
- **Do keep secondary actions as a quiet grey fill.** Contact sales is rgba(61, 77, 116, 0.12) ([secondary](components/crops/button-secondary-default.png)).
- **Do open navigation as a white panel.** Music opens `#top-nav-panel-music` ([menu](screenshots/home-light-nav-music.png)).
- **Don't treat the dark `--es-color-*` set as the marketing theme.** The painted page is light. The dark values are in the CSSOM only.
- **Don't follow login, signup, or checkout.** Those URLs are recorded in [site-tree.md](site-tree.md) and were not opened.

## Rebuild

```sh
cd systems/epidemicsound
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

Screenshots were captured with Playwright from `tools/capture/public/lib.mjs` (cookie banner hidden, no consent click) and quantised with `tools/capture/quantize.py`.
