# Navia design reference

A token set and component reference for Navia's public marketing site (https://www.thenavia.com/), a Webflow + Relume site for a marketing product. Use it to build a marketing surface that borrows its look: a cream page `#faf4e6`, ink `#36312a`, a chartreuse accent `#e8ff39` on 64px pills, an orange contact submit `#f88450` that inverts to ink on hover, Lora headings, and Public Sans on controls. It was captured signed out, in headless Chromium at 1440 x 900 and 390 x 844, on 2026-11-21.

The product app at https://app.thenavia.com/ paints a welcome wall and was not passed. Sign-in at https://accounts.thenavia.com/sign-in stopped at a Cloudflare check. No form was submitted.

This package contains no Navia code, and none of its artwork has been redrawn. The screenshots and the mark they show belong to Navia ([docs/RIGHTS.md](../../docs/RIGHTS.md)). Borrow structure and proportions, not the logo or brand assets.

| File | What it is |
|---|---|
| [icon.png](icon.png) | The site webclip, resized to 128 px |
| [tokens.json](tokens.json) | W3C DTCG tokens: `core` (scheme-1 slots, primitives, declared font stacks and radius steps, measured type styles) and `light` (page, text, accent, orange, component sizes). No dark set. Every token has `$extensions.source` |
| [DESIGN.md](DESIGN.md) | Not generated. `make design-md` needs a catalog.json entry, and this capture was told not to edit that file |
| [style-guide.html](style-guide.html) | Tokens rendered as a cream page, chartreuse pill, and orange submit. Open it from disk. Fonts fall back to Georgia and system-ui |
| [components.md](components.md) | 29 components with measured states and crops, then a Gaps section |
| [patterns.md](patterns.md) | How the header, hero, plans, blog, contact form, and phone menu compose |
| [site-tree.md](site-tree.md) | Which control opens which page, menu, dialog, or wall. Mapped before screenshots |
| [components/crops/](components/crops) | 61 element crops, `{component}-{state}.png` |
| [screenshots/](screenshots) | 30 captures, `{page}-light-{state}.png` at 1440 x 900 and `mobile-*` at 780 wide, quantised to 256 colours |
| [raw/](raw) | `css-vars.json`, `components-computed.json`, `component-tokens.json` |
| [tools/](tools) | Capture scripts and the builders that rewrite `tokens.json`, `components.md`, and `style-guide.html` |

## Brief

<!-- brief:start -->

Not generated. `tools/brief.py` reads catalog.json, and this capture was told not to edit that file. Read [tokens.json](tokens.json) and the Do and don't list below.

<!-- brief:end -->

## Health

<!-- health:start -->

Not graded. `tools/grade.py --write` updates catalog.json, which this capture must not touch.

<!-- health:end -->

## How the values were read

- [tools/capture/vars.mjs](tools/capture/vars.mjs) read the live Webflow stylesheets into [raw/css-vars.json](raw/css-vars.json). Colour roles resolved on a probe element. Font stacks and radius steps are declared on `:root` and did not resolve on that probe, so the tokens quote the declaration.
- [tools/capture/public/measure.mjs](tools/capture/public/measure.mjs) read computed styles and 2x crops. Cookie banners were rejected. The newsletter popup was closed. The published contact mailbox was hidden before contact shots. No field was filled.
- [tools/capture/public/public.mjs](tools/capture/public/public.mjs) took the page shots. [tools/capture/quantize.py](tools/capture/quantize.py) stitched full pages and wrote 256-colour PNGs.
- Font file URLs in the stylesheet dump were replaced with `url(…)` so signed query strings are not in the package.

## What to distrust

- **The app is absent.** Get started, Sign up, and the app host stop at a wall. Nothing here describes the signed-in product.
- **Button fill is not on the anchor.** Get started anchors are transparent. The chartreuse fill is on an inner `.button-base`, 48px tall, 64px radius. The contact submit is the orange control.
- **Feature selection does not paint the row.** Clicking a feature adds `is-active`. The measured row stays transparent. The selected look lives on a child the crop did not isolate.
- **Focus is Not captured.** Keyboard focus did not paint a site-authored ring. Do not treat a browser outline as a Navia token.
- **Scheme 2 through 10 are slot swaps, not a dark theme.** `prefers-color-scheme: dark` still paints cream and ink.
- **Screenshots are 256-colour PNGs.** Read colours from tokens.json.
- **The published mailbox is hidden** on the contact screenshots. Do not reconstruct it. The contact shots still show the site's empty-field sample placeholders. Those strings were removed from the raw JSON.

## Fonts

- **Lora Variablefont Wght** — headings. Declared as `--_typography---font-styles--heading`, with Times New Roman then sans-serif. Computed on the hero, sections, blog title, and contact title. Licence of the file on the site was not read. The style guide uses Georgia.
- **Publicsans Variablefont Wght** — nav, fields, submit. Declared as `--_typography---font-styles--body`, with Arial then sans-serif. The style guide uses system-ui.
- **Notemakersmark** — declared as `--_typography---font-styles--handwriting`. No captured control computed it.

## Coverage

| Surface | Desktop 1440 | Phone 390 | Notes |
|---|---|---|---|
| Home | cookies, preferences, default, feature, full | cookies, default, menu, full | Reject All used. Accept All not used |
| Blog index | default, full, page 2 | default, full | Pages 3 and 4 mapped, not shot |
| One post | default, full | default | Other posts not shot |
| Contact | default, select focused, full | default, full | Form not submitted. Mailbox hidden |
| Privacy | default, full | default | |
| Terms | default, full | not shot | Same chrome as privacy |
| Do not sell | default, full | not shot | Same chrome |
| App wall | default | default | Stopped. Sign In not passed |
| Accounts sign-in | not captured | not captured | Cloudflare check |

## Do and don't

1. **Do keep the page cream and the type ink.** The field is `#faf4e6` and the type is `#36312a`. [home-light-default](screenshots/home-light-default.png).
2. **Do use chartreuse for the primary pill.** `#e8ff39` on a 64px radius, ink label, 48px tall. [home-light-default](screenshots/home-light-default.png).
3. **Do use orange for the contact submit.** `#f88450`, same pill, inverting to ink with white type on hover. [submit-hover](components/crops/submit-hover.png).
4. **Do set headings in a serif and controls in a sans.** Lora on the hero, Public Sans on the nav and fields. [hero-title-default](components/crops/hero-title-default.png).
5. **Don't ship this as the product app.** The app is a sign-in wall. [app-wall-light-default](screenshots/app-wall-light-default.png).
6. **Don't invent a dark theme or a focus ring.** Neither was captured.

## Rebuild

```bash
cd systems/navia
python3 tools/build_component_tokens.py
python3 tools/build_tokens.py
python3 tools/build_components_md.py
python3 tools/build_style_guide.py
```

Capture again with `node tools/capture/vars.mjs`, `node tools/capture/public/measure.mjs`, and `node tools/capture/public/public.mjs`, then `python3 tools/capture/quantize.py ~/.design-systems/navia/raw-shots`. Those need the local Playwright install named in the capture scripts. `make design-md` and `make grade` need a catalog entry this package does not add.
