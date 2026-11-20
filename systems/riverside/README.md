# Riverside design reference

A token set and component reference for Riverside's public marketing site (https://riverside.com/), a Webflow build for HD podcast and video software. Use it to build a marketing page in this style: a white 64px bar, a dark photographic hero with white Sharp Grotesk 60px headlines over Instrument Sans, a black pill for the header Start for Free, and a purple `#9671ff` pill on the hero and the login button. Pricing sits on a smoke field. It was captured signed out, in headless Chromium at 1440×900 and 390×844, on 2026-11-21.

The product itself (the studio, editor and account) sits behind https://riverside.com/login. That page shows email and password, or Google, Apple and Spotify SSO. Password was not submitted. SSO was not clicked. https://riverside.com/start redirects to register and was not filled. The control map is [site-tree.md](site-tree.md).

This package contains no Riverside code, and none of its artwork has been redrawn. The screenshots belong to Riverside ([docs/RIGHTS.md](../../docs/RIGHTS.md)).

| File | What it is |
|---|---|
| [site-tree.md](site-tree.md) | The public control map: which header, footer and body control opens which page, menu or wall. Written before screenshots. |
| [icon.png](icon.png) | The site icon, 128 px PNG, when the fetch succeeds |
| [tokens.json](tokens.json) | W3C DTCG tokens: `core` (the Webflow `:root` palette, Sharp Grotesk and Instrument Sans, measured type, pill and field radii, header height) and `light` (page, surface, text, muted, accent, border, login panel roles). Every token has `$extensions.source`. One theme. |
| [DESIGN.md](DESIGN.md) | Written from tokens.json for readers of Google's DESIGN.md format. Not produced by `make design-md`, because that command registers the package in catalog.json. Take values from tokens.json. |
| [style-guide.html](style-guide.html) | Every token rendered, plus a chrome mock drawn from the tokens |
| [components.md](components.md) | Measured components with crops, then Gaps |
| [patterns.md](patterns.md) | How the bar, hero, pricing, login wall, blog and footer compose |
| [components/crops/](components/crops) | Element crops from the live page, `{component}-{state}.png` |
| [screenshots/](screenshots) | `{page}-light-{state}.png` at 1440×900 and `mobile-*` at 390×844 (2x), quantised to 256 colours |
| [raw/](raw) | `css-vars.json`, `components-computed.json`, `component-tokens.json`, `measurements.md` |
| [tools/](tools) | The capture scripts and the builders |

## Brief

<!-- brief:start -->
<!-- brief:end -->

## Health

<!-- health:start -->
<!-- health:end -->

## How the values were read

Every value came off the signed-out site in headless Chromium (Playwright), not from memory and not from screenshots.

- **Tokens.** [tools/capture/vars.mjs](tools/capture/vars.mjs) captured stylesheet bodies on the homepage and wrote every custom property to [raw/css-vars.json](raw/css-vars.json). The `:root` block declares the named palette (`--peacock`, `--primary-purple`, `--brand-black`, the smoke and wash names). A `.dark` probe was run and nothing binds it, so no dark set is emitted. [tools/build_component_tokens.py](tools/build_component_tokens.py) writes the spec. [tools/build_tokens.py](tools/build_tokens.py) writes [tokens.json](tokens.json).
- **Components.** [tools/capture/public/measure.mjs](tools/capture/public/measure.mjs) read `getComputedStyle` on the live pages for default, hover, focus-visible and a CDP-forced pressed state. Login fields were focused and not filled. Results are in [raw/components-computed.json](raw/components-computed.json) and [raw/measurements.md](raw/measurements.md).
- **Screenshots.** [tools/capture/public/public.mjs](tools/capture/public/public.mjs) took viewport and full-page shots. The cookie dialog was hidden, never answered. [tools/capture/quantize.py](tools/capture/quantize.py) posterised the copies to 256 colours.

Nothing was signed into, bought or submitted.

## What to distrust

- **This is the public site, not the studio.** The recording room, editor, hosting dashboard and account settings were not reached. Do not invent them from the marketing stills.
- **One token theme.** The home hero is a dark photograph with white type. Pricing and the header sit on white and smoke. The login wall is a dark panel. None of those is a second token theme. `tokens.json` has no dark set. Login colours are `light.login-surface` and `light.login-text`, measured on that panel.
- **The hero CTA colour is not the nav pill.** The header Start for Free pill is black `#1d1d1d`. The hero Start for Free button is purple. Both are called Start for Free.
- **Quantised screenshots.** Read colours from tokens or `raw/`, not from the PNGs.
- **Unread values are Not captured.** Spacing scale, elevation levels, motion easings, status colours, and several component states were not present as tokens or could not be held. They are listed in Coverage, not filled in.
- **A Google One Tap sheet** can appear on the phone homepage. It was not clicked. It is not part of the design system.

## Fonts

Marketing pages use **Sharp Grotesk** for display (hero 60px, pricing title 50px) and **Instrument Sans** for UI (14px nav, 16px body, 12px footer). The login wall uses **Inter** and **Sharp Grotesk Book**. The faces are served by Riverside and are not in this package. The style guide falls back to system sans. Other faces in the stylesheet harvest (Alfa Slab One, IBM Plex Sans, Poppins, Shrikhand) are loaded by Webflow and were not the measured text on the captured controls.

## Coverage

| Checklist item | Status |
|---|---|
| Colour roles | Captured for page, surface, text, muted, accent, border, on-accent, login panel. Raised, overlay, scrim, disabled text: Not captured. |
| Type | Captured: display, title, ui, body, caption, login. Code role: not present on the public pages. |
| Spacing | Not captured. Webflow sets padding per component. No spacing scale was declared. |
| Radii | Captured: pill 300px, newsletter field 5px, login field 8px. |
| Borders | Captured as `--secondary-c150`. Strong border: Not captured. |
| Elevation | Not captured. No shadow scale was declared on the measured controls. |
| Motion | Not captured as named tokens. |
| Sizing | Captured: header 64px, mobile header 60px, nav pill 40px, newsletter field 52px, login field 40px. Icon sizes: Not captured. |
| Layout | Captured at 1440 and 390. Breakpoints are not tokenised. |
| Button | Captured: nav CTA default, hover, focus-visible, pressed. Hero purple CTA: seen in [home-light-default](screenshots/home-light-default.png), crop Not captured (selector missed). |
| Icon button | Captured: mobile menu button. |
| Link | Captured: nav Pricing link, footer Privacy link. |
| Text field | Captured: newsletter email (focused, not filled), login email (focused, not filled). |
| Text area | Not present on the captured pages. Community form has one; that form was not opened for measurement. |
| Select | Not captured. |
| Checkbox | Seen as hero chips in the screenshot. Values Not captured. |
| Radio | Not captured. |
| Switch | Not present. |
| Tabs | Pricing Monthly / Yearly seen in screenshots. Measure selector missed. Values Not captured. |
| Menu | Phone menu captured open. Desktop Platform menu: in the site tree. Crop Not captured. |
| Tooltip | Not present on the captured pages. |
| Dialog | Cookie dialog seen and hidden, never answered. Values Not captured. |
| Toast | Not present. |
| Card | Pricing panel measured as one large region, not one card. Individual card crop: Not captured. |
| List row | Phone menu row captured. |
| Table | Not present on the captured marketing pages. |
| Avatar | Not present. |
| Badge | Best Value badge seen on the Grow card in the pricing screenshot. Values Not captured. |
| App shell | Captured. |
| Form with validation error | Not captured. No form was submitted, so no error state was shown. |
| Empty, loading, error | Not present on the marketing pages. |
| Destructive confirmation | Not present. |
| Feedback after an action | Not captured. No action was submitted. |
| Search | Help Center search exists at support.riverside.com. Not measured. |
| Onboarding | Behind the register wall. Not captured. |
| Dark theme | Not present. |
| Desktop 1440 and phone 390 | Captured. |

## Do and don't

- **Do set display type in Sharp Grotesk and UI in Instrument Sans.** The hero and the pricing title use Sharp Grotesk. Nav, body and footer use Instrument Sans. See [home-light-default](screenshots/home-light-default.png).
- **Do use the black pill for the header action and purple for the hero action.** They share a label and not a colour. See [home-light-default](screenshots/home-light-default.png).
- **Do keep the header and pricing on white and smoke.** The home hero is a dark photograph with white type, not a coloured band and not a dark theme. See [home-light-default](screenshots/home-light-default.png) and [pricing-light-default](screenshots/pricing-light-default.png).
- **Don't treat the login panel as a dark theme.** It is one screen, with Inter and a `#222` field. See [login-light-wall](screenshots/login-light-wall.png).
- **Don't style the studio from this package.** The editor stills on the marketing pages are public demos. The signed-in product was not captured.
- **Don't submit the cookie dialog or a form to "see the real site".** Hiding the dialog was the capture. Answering it was not.

## Rebuild

```bash
cd systems/riverside
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/vars.mjs
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/public/measure.mjs
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/public/public.mjs
python3 tools/capture/quantize.py ~/.design-systems/riverside/raw-shots
node tools/capture/public/build-measurements.mjs
python3 tools/build_component_tokens.py && python3 tools/build_tokens.py
python3 tools/build_style_guide.py && python3 tools/build_components_md.py
```

Full-colour shots stay in `~/.design-systems/riverside/raw-shots`. They are not committed.
