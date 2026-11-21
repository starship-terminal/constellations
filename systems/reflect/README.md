# Reflect design reference

Tokens and component notes for Reflect's signed-out site. First capture on **2026-11-21** from https://reflect.app/, signed out, in headless Chromium at 1440×900 and 390×844 (devicePixelRatio 2). The T3 preview tab loaded the homepage and returned the link map, then failed screenshots with "The browser is not producing screenshot frames". Screenshots are from headless Chromium.

Captured: the marketing home, the pricing and company sections, the footer, the launch-film dialog, the blog and its Articles filter, the download page, privacy, terms, a public 404, the phone homepage, the phone nav drawer, and the phone blog. Login and signup are the same empty wall at `/auth`. Nothing was typed. Identity providers were not clicked. The control map is [site-tree.md](site-tree.md).

Reflect paints one marketing theme. Forcing `prefers-color-scheme: dark` left the page background at `rgb(3, 0, 20)`. Privacy and terms are a separate light document. The auth wall uses Inter, not AeonikPro.

| File | What it is |
|---|---|
| [README.md](README.md) | This file. |
| [icon.png](icon.png) | Site icon, 128 px. |
| [tokens.json](tokens.json) | DTCG tokens. `core` holds type, radius, space, motion. `light` holds the one painted marketing theme. |
| [DESIGN.md](DESIGN.md) | Hand-written from the measured tokens. catalog.json was not edited, so the generator was not run. |
| [style-guide.html](style-guide.html) | Specimens rendered from the tokens. AeonikPro and Inter V are not loaded. |
| [components.md](components.md) | Controls that were on the page, with measured values. |
| [patterns.md](patterns.md) | How the home, blog, and auth wall are put together. |
| [site-tree.md](site-tree.md) | Which homepage controls open which pages, menus, and dialogs. Mapped 2026-11-21. |
| [components/crops/](components/crops/) | Not cut. Declared under layoutGaps. |
| [icons/](icons/) | Not extracted. Declared under layoutGaps. The wordmark stays in the screenshots. |
| [screenshots/](screenshots/) | Viewport shots of the public pages, pricing, footer, video dialog, blog filter, empty login wall, a full home, and 390px home, menu, and blog. Quantised to 256 colours. |
| [raw/](raw/) | Computed-style dumps, button CSS rules, the dark-scheme probe, and the auth-wall reading. |
| [tools/](tools/) | Builders and the copied capture kit. |

## Brief

<!-- brief:start -->

Not generated. catalog.json was left alone, so `make brief` was not run for this package.

<!-- brief:end -->

## Health

<!-- health:start -->

Not graded. catalog.json was left alone, so this package is not in the scorecard.

<!-- health:end -->

## How the values were read

Computed styles on the live DOM at 1440×900: body, h1, h2, nav link, Download, Download for Mac, the hero subcopy, the Meet Reflect Open pill. Button fills come from the `.button-primary` and `.button-secondary` CSS rules, because the anchor's own `background-color` is transparent and the wash sits on `::before`. Blog trial, login, and the selected tag were computed on https://reflect.app/blog. The auth email field and Continue button were computed on https://reflect.app/auth. The mobile drawer background was computed on `.header-nav` after `.header-toggle` was clicked. Focus-visible on Download for Mac did not paint an outline (`outline: none 0px`). Hover swapped the button pseudo-element opacity. That swap is in the CSS rule, not a second computed background on the anchor.

## What to distrust

- Primary button colour is the `::before` wash, not a flat fill. A screenshot sample of the button will not match `#712fff1f`.
- The auth wall and the blog header are a second implementation (solid `#7c3aed` and `#a855f7`). They are not the marketing `.button-primary`.
- Privacy and terms use a light page. They are not a dark-theme toggle.
- Pressed, disabled, and loading were not captured.
- Screenshots are 256-colour. Read values from tokens.json.
- AeonikPro and Inter V are not shipped. The style guide falls back.
- The homepage product screenshot is marketing artwork. It is not the signed-in app.
- `login-extracted` was not started.

## Fonts

- **AeonikPro** for display headings, 500. Computed on the homepage h1. Not shipped.
- **Inter V** for marketing UI, 400 and 500. Computed on body, nav, and buttons. Not shipped.
- **Inter** (a hashed Next font, `__inter_5b82ff`) on the blog and the auth wall. Not shipped.

## Coverage

| Item | Status |
|---|---|
| Colour roles | Captured for page, text, muted, nav, button wash, trial, continue, tag, field, and the light legal page. |
| Type | Captured at 1440: display 72/80, heading 56/64, body 16/24, label 14/20. |
| Spacing, radius, borders | Captured from the controls that showed them. No published scale. |
| Elevation | Inset glows on `.button-primary` (12px). No drop shadow on the marketing page. Auth Continue has a 1px soft shadow. |
| Motion | Button pseudo-element opacity, 200ms, cubic-bezier(0.6, 0.6, 0, 1). |
| Button, link, field | Captured. |
| Icon button | The phone `.header-toggle` and the video close control. No separate crop. |
| Menu | Phone drawer. Desktop nav is a link pill, not a menu. |
| Dialog | Launch-film overlay. |
| Chip | Blog tag filter. |
| Card | Download rows and blog cards. |
| Select, checkbox, radio, switch, tabs, tooltip, toast, table, avatar, badge | Not present on the pages opened. |
| Login chrome | Captured empty. Not submitted. |
| Signup | No separate page. Start Free Trial lands on the same empty `/auth` wall. Not submitted. |
| Empty state | Public 404. |
| Dark theme | The marketing site is dark and does not switch. Confirmed 2026-11-21. |
| Desktop 1440 and phone 390 | Captured. Phone inner page is the blog. |
| Site tree | [site-tree.md](site-tree.md), 2026-11-21. |
| Signed-in app | Not captured. Stopped at the login wall. |

## Do and don't

1. **Do paint the page near-black and the type white.** Body computes to `#030014`. The hero is white AeonikPro ([home](screenshots/home-light-default.png)).
2. **Do keep marketing buttons glassy.** Primary is an 8px radius wash of violet, not a solid fill ([home](screenshots/home-light-default.png)).
3. **Do set the display line in AeonikPro at 500.** The home hero is 72px / 80px at 1440 ([home](screenshots/home-light-default.png)).
4. **Don't invent a light marketing theme.** Forcing dark colour-scheme did not restyle the page. The light pages are legal documents ([privacy](screenshots/privacy-light-default.png)).
5. **Don't ship AeonikPro, Inter V, or the wordmark.** Names are evidence. The files and the logo are Reflect's.
6. **Don't treat this as the signed-in product.** Login was photographed empty and not submitted ([login](screenshots/login-light-default.png)).

## Rebuild

```bash
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
python3 tools/build_components_md.py
```

`catalog.json` was left alone, so `python3 tools/catalog.py design-md reflect` was not run.
