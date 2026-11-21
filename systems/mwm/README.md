# MWM design reference

A token set and component reference for MWM's public marketing site, for building a dark product-marketing page or an app-directory index in that style. It was read from https://mwm.ai/ on 2026-11-21, signed out, in headless Chromium. Desktop captures are 1440 by 900 at device pixel ratio 1. Phone captures are 390 by 844 at device pixel ratio 2. The only public theme is dark (`html.dark-mode`). No account was created, no form was submitted, and the Console and Create App login walls were not entered.

The captured surface is the marketing site and its public directories: home, product pages, pricing, studio, company, articles, guides, glossary, apps, tags, rankings, authors, methodology, the ASO tool, and the legal pages. Signed-in Console and app creation are a different product and are not in this package.

| File | What it is |
|---|---|
| [icon.png](icon.png) | The site icon, 128 px, resized from https://mwm.ai/apple-touch-icon.png (180 px). |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds the declared `--mwm-*` colours, the measured type styles, radius, a few paddings, and the composer focus ring. `dark` is the only semantic set. Every token carries `$extensions.source`. |
| [DESIGN.md](DESIGN.md) | Generated from [tokens.json](tokens.json) and this README by `tools/catalog.py`. It holds one theme and no provenance. Take values from tokens.json. |
| [style-guide.html](style-guide.html) | One page that renders the measured colours, type, and the main controls. Dark only. |
| [components.md](components.md) | The component inventory, with values as token names, and the Gaps section. |
| [patterns.md](patterns.md) | How the header, composer, product page, directory, and legal page fit together. |
| [site-tree.md](site-tree.md) | Which control opens which page, menu, or stopped branch. Mapped before the screenshots. |
| [components/crops/](components/crops) | Element crops cut from the 256-colour screenshots. They show layout, not exact colour. |
| [icons/](icons) | The header mark, saved from the apple touch icon. [icons/INDEX.tsv](icons/INDEX.tsv) names it. MWM's property, kept for reference only. |
| [screenshots/](screenshots) | 91 `{page}-dark-{state}.png` captures, 256-colour. Desktop 1440 by 900. Phone shots are named `mobile-*` and are 780 by 1688 pixels (390 by 844 at 2x). |
| [raw/](raw) | `css-probe.json` (declared custom properties, resolved on `html`), `components-computed.json` (computed styles of the measured controls), and `captures/` (viewport sidecars). Full-colour originals stay outside git. |
| [tools/](tools) | `build_tokens.py`, `build_style_guide.py`, `build_components_md.py`, and the adapted capture kit under `capture/`. |

## Brief

<!-- brief:start -->

Brief is not generated. This capture does not add a catalog.json entry, and `tools/brief.py` reads that entry. Take values from [tokens.json](tokens.json).

<!-- brief:end -->

## Health

<!-- health:start -->

Health is not generated. `tools/health.py` reads the catalog and the scorecard, and this capture does not edit either. The coverage table below is the record of what was and was not captured.

<!-- health:end -->

## How the values were read

Custom properties were read from the live CSSOM on https://mwm.ai/ on 2026-11-21 and stored in [raw/css-probe.json](raw/css-probe.json). `html` had class `dark-mode`. The theme colour meta is `#0D0D0D`. Resolved `--mwm-*` values on `html` are the colour tokens. Tailwind `--tw-*` properties are in the dump and are not brand tokens.

Computed styles of the header buttons, the home heading, the composer, the pricing CTA, the empty IP dispute form, and a glossary category card were read at 1440 by 900, device pixel ratio 1, `en-US`, reduced motion. They are in [raw/components-computed.json](raw/components-computed.json). No value was typed into a field. No form was submitted.

`CSS.forcePseudoState` failed on every targeted node (`Could not find node with given id`). Hover and pressed colours of the header and pricing buttons are therefore not in the tokens. The three public stylesheets (`index.DKqvgvwu.css`, `primeicons.CBEcAFVq.css`, `pricing.CIa7aOJp.css`) declare a composer menu hover (`#373737`), a send-button hover shadow, and a composer focus ring (`0 0 0 2px #ffffff2e`). Those are labelled as declared, not as measured on an element.

Screenshots were taken with Playwright from [tools/capture/public/public.mjs](tools/capture/public/public.mjs), then quantised to 256 colours by [tools/capture/quantize.py](tools/capture/quantize.py). `navigator.webdriver` was masked. No cookie banner appeared, so none was clicked.

## What to distrust

- Screenshots are 256-colour PNGs. Read colours from [tokens.json](tokens.json) or [raw/](raw).
- `--mwm-btn-secondary-bg` is `#2a2a2a`. The live header control "Open MWM Console" measured `rgba(255, 255, 255, 0.1)`. The token records the measured control.
- An older `.mwm-topbar-primary` rule declares `border-radius: 999px` and `color: #050505`. The live "Build your app" control measured `8px` and `rgb(12, 12, 12)`.
- The pricing CTA "Get MWM AI Pro" measured label `rgb(0, 0, 0)`, not `#0c0c0c`.
- `--mwm-font-display` names Modern Gothic. `document.fonts` did not list it as loaded, and the home `h1` computed to Inter.
- Home-scoped `--mwm-lilac`, `--mwm-gold`, and `--mwm-green` resolved empty on `html`. They are not tokens.
- The legal screenshots show the company's published headquarters in the page text. That string is not copied into this package's text files.
- Capture sidecars report `theme.classes` as empty even though `html` had `dark-mode` during the CSS probe. Trust the CSS probe for the theme class.

## Fonts

Inter is the face that loaded (weights 400 and 700) and the computed family of the measured heading, buttons, and fields. The declared UI stack is Inter, then `-apple-system`, `BlinkMacSystemFont`, `Segoe UI`, `sans-serif`. Instrument Sans 400 also loaded. It was not the computed family of the measured controls. Modern Gothic and Modern Gothic Mono are declared and were not confirmed loaded. PrimeIcons is referenced and was unloaded. These are MWM's font choices. This package does not ship the font files.

## Coverage

| Item | Status |
|---|---|
| Colour roles, dark | Captured. [tokens.json](tokens.json), [screenshots/home-dark-default.png](screenshots/home-dark-default.png). |
| Light theme | Not present. No theme switch. |
| Type roles | Captured for display, lede, nav, button, chip, and field. |
| Spacing scale | Not present as a published scale. Measured paddings are in `core.space`. |
| Radius | Captured: 8, 16, 24 px declared. 8 and 16 measured. |
| Borders | Captured: `--mwm-line`, `--mwm-line-strong`, field hairline `#1a1a1a`, focus border `#3a3a3a`. |
| Elevation | Partly. Composer focus ring and send shadow are declared. Header buttons measured `box-shadow: none`. |
| Motion | Partly. Send transition `.18s ease` is declared. Captures used reduced motion. |
| Button | Captured default: header primary, header secondary, pricing CTA, disabled submit. Hover and pressed: not captured. |
| Icon button | Observed on the composer (attachment, voice, send). Values for the default chip height are declared. Voice and attachment were not used. |
| Link | Observed in the header, footer, and legal body. Orange link colour on the privacy page is observed, not measured as its own token. |
| Text field | Captured empty and focused on the IP dispute form. No value typed. |
| Text area | Captured empty on the home composer and the IP form. Not submitted. |
| Select | Captured empty on the IP form. Not changed. |
| Checkbox | Captured unchecked. Not toggled. |
| Radio, switch | Not present on the captured public pages. |
| Tabs | Not present as a tab widget. Category filters are buttons. |
| Menu | Captured: Products, Resources, language, agent, platform, model, phone nav. Agent and model menus clip at the bottom of the 900 px viewport. |
| Tooltip, toast | Not present on the captured pages. |
| Dialog | Not present, other than the native file picker, which was not opened. |
| Card | Captured: glossary category card, default and selected. |
| List row, table | Directory indexes are card grids, observed in the screenshots. No data table was measured. |
| Avatar, badge | Observed on directory and studio pages. Not measured. |
| App shell | Captured at desktop and phone. [screenshots/mobile-home-dark-nav-open.png](screenshots/mobile-home-dark-nav-open.png). |
| Form validation error | Not captured. The empty IP form was not submitted. |
| Empty, loading, error | The sign-up URL is a 404: [screenshots/sign-up-404-dark-default.png](screenshots/sign-up-404-dark-default.png). Loading states were not held. |
| Search and filter | Captured: glossary ASO filter, duo Optimized filter, reports Europe filter, search fields focused on trends and tags. |
| Signed-in console | Not captured. Login wall at `https://console.mwm.ai/sign-in`. |
| Create app | Not captured. Login wall at `https://create.mwm.ai/sign-in`. |
| Locale mirrors | Not captured. The language menu was opened. English only. |
| Careers and external product sites | Not captured. They leave mwm.ai. |
| Catalog rows beyond one example | Not captured individually. Same template as the captured example. |

## Do and don't

- **Do** build on a near-black page (`#0c0c0c`) with white type and white primary buttons. [screenshots/home-dark-default.png](screenshots/home-dark-default.png).
- **Do** use 8 px radius on buttons, fields, and chips, 16 px on cards, and 24 px only where the panel token is declared.
- **Do** set display type at 72 px, weight 600, line-height 76 px, tracking `-2.88px`, in Inter.
- **Don't** invent a light theme. The public site has one theme.
- **Don't** invent hover colours for the header buttons. They were not measured.
- **Don't** treat orange as the primary button fill. Orange is the accent and the selected-card ring. Primary buttons are white.
- **Don't** read colours off the screenshots. They are 256-colour PNGs.
- **Don't** copy the logo, app icons, or photography into something that ships.

## Rebuild

```bash
cd systems/mwm
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
python3 tools/build_components_md.py
```

From the repository root, `python3 tools/catalog.py design-md` can regenerate [DESIGN.md](DESIGN.md) only after a catalog entry exists. This capture does not add that entry. The committed DESIGN.md was generated once with a temporary entry that was not written to catalog.json.

To recapture screenshots:

```bash
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  node tools/capture/public/public.mjs
python3 tools/capture/quantize.py ~/.design-systems/mwm/raw-shots
```

## Catalog

This package is not registered in catalog.json. A capture that edits catalog.json was out of scope. `make check` will report that `systems/mwm` has no catalog entry until a later change adds one.
