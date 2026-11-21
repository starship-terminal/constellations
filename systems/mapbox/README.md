# Mapbox design reference

Public marketing site of Mapbox, captured signed out on 2026-11-21 from https://www.mapbox.com/. Headless Chromium, desktop 1440×900 and phone 390×844. One light theme. The account console was not entered: Log in opens https://account.mapbox.com/auth/signin/ and that branch stopped.

Mapbox's public UI is a Webflow marketing site on Cera Pro, white page, ink `#0e1012`, and a pill accent `#007afc`. Product, solution, and company pages share one header. Docs, status, and the account host are other sites.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site icon, 128 px, from the apple-touch-icon on mapbox.com |
| [tokens.json](tokens.json) | DTCG tokens: `core` ramps, type, space, radius; `light` roles. No dark set. Every token has `$extensions.source`. |
| [DESIGN.md](DESIGN.md) | Generated. Not hand-edited. |
| [style-guide.html](style-guide.html) | Renders the light tokens and the pill button, stroke button, and field |
| [components.md](components.md) | Component inventory and gaps |
| [patterns.md](patterns.md) | Header, hero, pricing, contact, menus |
| [site-tree.md](site-tree.md) | Which control opens which page, menu, or wall, mapped before screenshots |
| [components/crops/](components/crops) | Element crops cut from the raw shots |
| [screenshots/](screenshots) | Public page captures, 256-colour |
| [raw/](raw) | CSS variable harvest and computed component readings |
| [tools/](tools) | Capture scripts and builders |

## Brief

<!-- brief:start -->
Brief is written by `make brief` after a catalog entry exists. This capture was asked not to edit catalog.json, so the generated Brief is not in this commit.
<!-- brief:end -->

## Health

<!-- health:start -->
Health is written by `make grade` from the scorecard. This capture was asked not to edit catalog.json, so grades were not merged.
<!-- health:end -->

## How the values were read

[tools/capture/vars.mjs](tools/capture/vars.mjs) loaded https://www.mapbox.com/, saved stylesheet bodies, and resolved every custom property on `:root`. [tools/build_tokens.py](tools/build_tokens.py) maps the blue, gray, green, orange, purple, red, and yellow ramps, the spacer and radius scales, and the heading sizes.

Painted controls were read with `getComputedStyle` in [tools/capture/public/measure.mjs](tools/capture/public/measure.mjs). The hero CTA's colour sits on `.button_inner`, not the anchor. Hover was a real pointer hover. The contact field was focused and not filled.

The OneTrust banner was hidden with CSS. Accept, Reject, and Customize were not clicked. No form was submitted.

## What to distrust

- One theme. No dark set. `--nav--dark-*` names exist for the mega menu's dark panel and are not a second page theme.
- Screenshots are 256-colour PNGs. Read colours from tokens.json.
- Cera Pro is not in the style guide. The site's own fallback is Trebuchet MS.
- Button pressed, disabled, loading, and error were not on the public pages.
- Motion durations were not declared as custom properties. Not captured.
- `--_color-mode---box-shadow--box-shadow` is a colour, not a shadow. Elevation is not captured.
- Deleted Webflow variable names (the `<deleted|variable-…>` suffixes) were skipped. Live names were used.
- The contact combobox was not opened. Its closed field was measured.

## Fonts

**Cera Pro** is the licensed UI face (`@font-face` weights 300, 400, 500, 700, normal and italic). It is not distributed. The computed stack is `"Cera pro", "Trebuchet MS", sans-serif`. Open Sans is declared in an inline sheet and was not the body face.

## Coverage

| Expectation | Status | Where |
|---|---|---|
| Colour roles | captured | `light.*` over `core.color.*` |
| Type | captured | `core.font.*` and computed body/h1 |
| Spacing | captured | `core.space.*` from `--_dimensions---spacers--*` |
| Radii | captured | `core.radius.*` plus button `100px` |
| Borders | captured | `light.border.*` |
| Elevation | not captured | no shadow layer token |
| Motion | not captured | no duration or easing custom properties |
| Sizing | captured | button 52px, field 44px, nav 63px, icon sizes |
| Layout | captured | `core.layout.*` max-widths; 1440 and 390 shots |
| Button | captured | pill and stroke |
| Icon button | partly | mobile menu control in phone shots; no isolated crop |
| Link | captured | header Log in |
| Text field | captured | contact field, default and focus |
| Text area | not present | no textarea on the contact page |
| Select | not present | combobox input, native select count 0 |
| Checkbox, radio, switch | not present | only hidden OneTrust switches, not opened |
| Tabs | not present | hero slide buttons, no tab role |
| Menu | captured | Products mega menu and language menu |
| Tooltip, toast | not present | none on the public pages |
| Dialog | not present | cookie banner hidden, not a product dialog |
| Card | partly | pricing page screenshot; card box not isolated |
| List row | partly | footer and showcase index |
| Table | not present | |
| Avatar | not present | |
| Badge | partly | NEW and HIRING labels in menus, not cropped |
| Hover, focus | captured | button hover, field focus |
| Pressed, disabled, loading, error | not captured | not shown on public pages |
| App shell | captured | marketing header, [site-tree.md](site-tree.md) |
| Form with validation error | not captured | form not submitted |
| Empty, loading | not present | marketing pages |
| Destructive confirmation | not present | |
| Search and filtering | not captured | docs search is on docs.mapbox.com |
| Onboarding | not captured | signup wall |
| Signed-in console | not captured | https://account.mapbox.com/auth/signin/ |
| Dark theme | not present | |
| Widths 1440 and 390 | captured | screenshots |

## Do and don't

1. **Do use one blue pill for the primary action.** `#007afc`, white label, `100px` radius. See the home hero in [screenshots/home-light-default.png](screenshots/home-light-default.png).
2. **Do keep the page white and the ink near-black.** Page `#ffffff`, text `#0e1012`, secondary `#333943`.
3. **Do use the stroke pill for the quiet action.** Transparent face, `#bbc2ce` border, `#1c1f24` label.
4. **Don't invent a dark theme.** The site paints light. Dark nav tokens are menu chrome.
5. **Don't enter the account host.** Log in and Sign up leave the marketing site. Stop there.
6. **Don't submit the contact or newsletter forms.** They are public, and this capture left them empty.

## Rebuild

```sh
cd systems/mapbox
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/public/measure.mjs
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
python3 tools/build_components_md.py
python3 tools/capture/quantize.py ~/.design-systems/mapbox/raw-shots screenshots
```

`make design-md` needs a catalog.json entry. This capture was asked not to edit that file.
