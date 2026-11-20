# Vevo design reference

A token set and component reference for Vevo's public marketing site, for building a music-network marketing page in the same proportions. It was read from **hq.vevo.com** on **2026-11-21**, signed out, in headless Chromium. `https://www.vevo.com/` redirects there. Desktop viewport measured 1440x900 at 1x. Phone viewport measured 390x844 at 2x. One light theme. No account.

The site is a Wix marketing site: a black-and-white shell, a full-bleed artist photo, a crimson stats band, and section pages that change ground (slate form, pink artist support, lilac feedback, black policy). The consumer video app is not on this host. `https://www.vevo.com/login` returned 503 with an empty document. Password walls at `/home-old` and `/label-partners` were not crossed.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site icon, 128 px PNG, resized from the 192 px Wix favicon |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds the measured colours, type, radii and sizes. `light` holds the roles. One theme. Every token has `$extensions.source` |
| [DESIGN.md](DESIGN.md) | Written by `tools/catalog.py`'s generator against a throwaway entry, because this capture does not edit catalog.json. One theme, no provenance |
| [style-guide.html](style-guide.html) | Renders the tokens. Open it from disk |
| [components.md](components.md) | Component inventory, crops, and gaps |
| [patterns.md](patterns.md) | How the pages combine the components |
| [site-tree.md](site-tree.md) | Which control opens which page, menu, or wall |
| [components/crops/](components/crops) | Element crops from the live pages |
| [icons/](icons) | Index only. The wordmark is not extracted |
| [screenshots/](screenshots) | 41 page captures, 256-colour PNGs. Privacy and terms pages were not kept: the terms page paints an office address |
| [raw/](raw) | `components-computed.json`, `component-tokens.json`, `css-vars.json` |
| [tools/](tools) | Builders and the adapted capture kit |

## Brief

<!-- brief:start -->
<!-- brief:end -->

## Health

<!-- health:start -->
<!-- health:end -->

## How the values were read

Headless Chromium through Playwright, 2026-11-21. `tools/capture/public/public.mjs` took the page shots. `tools/capture/public/measure.mjs` read computed styles and wrote crops. A second probe read painted backgrounds (the crimson band, the slate form page, the header height, the stats figure). Wix custom properties were listed and not tokenised: they are layout internals. `tools/build_tokens.py` writes `tokens.json` from `raw/component-tokens.json`.

The cookie banner was hidden with CSS. Decline and Accept were not clicked. No form was submitted. No password was typed.

## What to distrust

- **The font.** Computed `fontFamily` is a Wix hash (`wfont_08392a_…`). The public name was not readable. Tokens use Helvetica as the fallback and mark the real face Not captured.
- **Section grounds are page-specific.** Crimson is the stats band and the invalid field border. Slate is the advertiser form. Pink and lilac appear on artist pages and were not read as computed colours, so they are not tokens.
- **Hero type size moves.** The homepage headline computed at about 166px. That is a fluid Wix size, not a fixed step, so it is not a token.
- **Nav link colour on the element is the browser default blue.** The painted text is white. Tokens use the text node's colour, not the anchor's.
- **Hover on the submit button inverts it.** That is one control, not a second brand colour.
- **Screenshots are 256-colour PNGs.** Read colours from tokens.json.
- **No dark theme.** Do not invent one.
- **The password wall's blue Go button** is Wix's guest-area chrome, not the marketing accent. It was not tokenised.

## Fonts

| Family | Used for |
|---|---|
| Wix-hosted cut (public name Not captured) | Headlines, nav, buttons, fields |
| Helvetica, Arial, sans-serif | Fallback in the tokens and the style guide |

Weights measured were 400. A bold cut was not read.

## Coverage

| Checklist item | Status | Where |
|---|---|---|
| Colour roles | Captured, light only | tokens.json `light.color` |
| Dark theme | Not present | No theme switch |
| Type roles | Partly | Nav, control, button, field, figure. Display size not tokenised (fluid). Family Not captured |
| Spacing | Partly | Field padding only |
| Radii | Captured | 0, 24px pill, 999px submit |
| Borders | Captured | 1px field |
| Elevation | Not present | No shadows on the measured controls |
| Motion | Not captured | Measured transitions were 0s |
| Sizing | Captured | Header 77, button 46, field 41, area 104, checkbox 13 |
| Layout | Captured | 1440 and 390, measured |
| Button | Captured, default and hover | components.md |
| Icon button | Captured | menu and share crops |
| Link | Captured, default and hover | nav-link crops |
| Text field | Captured, default, focus, empty-invalid | form crops |
| Text area | Captured, default and focus | |
| Select | Captured, closed only | open menu not captured |
| Checkbox | Captured, unchecked | checked not captured |
| Radio | Captured, unselected | selected not captured |
| Switch | Not present | |
| Tabs | Not present | accordion instead |
| Menu | Captured | phone drawer |
| Tooltip | Not present | |
| Dialog | Partly | video lightbox screenshot. Cookie banner not clicked |
| Toast | Not present | no submit |
| Card | Captured | news card |
| List row | Not present | |
| Table | Not present | |
| Avatar | Not present | |
| Badge | Not present | |
| App shell | Captured | patterns.md |
| Form with validation | Partly | empty field border only. Form not submitted |
| Empty, loading, error | Partly | 404 page captured. No empty or loading state |
| Destructive confirmation | Not present | |
| Search and filtering | Not present | |
| Onboarding | Not present | |
| Signed-in app | Not captured | login 503, password walls not crossed |

## Do and don't

- **Do keep the shell black and white.** The header links and the wordmark sit on the photo. The footer is a black band. [home-light-default.png](screenshots/home-light-default.png)
- **Do spend crimson on the stats band.** It is the one brand colour on the homepage. [home-light-default.png](screenshots/home-light-default.png)
- **Do invert the pill on hover.** White pill becomes near-black, and the black submit becomes off-white. [text-link-hover.png](components/crops/text-link-hover.png)
- **Don't round the fields.** Buttons are pills. Fields are square. [text-field-default.png](components/crops/text-field-default.png)
- **Don't invent a dark theme.** The site paints one light scheme and swaps section grounds. [advertisers-light-default.png](screenshots/advertisers-light-default.png)
- **Don't treat the guest-area blue as the brand.** That blue is the password wall. [password-wall-light-default.png](screenshots/password-wall-light-default.png)

## Rebuild

```bash
cd systems/vevo && python3 tools/build_tokens.py && python3 tools/build_style_guide.py
```

Page shots:

```bash
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  node systems/vevo/tools/capture/public/public.mjs
python3 systems/vevo/tools/capture/quantize.py ~/.design-systems/vevo/raw-shots
```
