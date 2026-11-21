# IFTTT design reference

A token set and component reference for IFTTT's public site, for building marketing, explore, plans, and docs pages in the style of the real thing. Captured from [ifttt.ai](https://ifttt.ai/) on 2026-11-21, signed out, in headless Chromium. `https://ifttt.com/` redirects there. Desktop is 1440x900 at 1x. Phone is 390x844 at 2x. One light theme. `prefers-color-scheme: dark` does not switch the page.

The public site is ink on white. `#111111` is the text, the primary button, and the strong border. White is the page. Buttons are pills. The wordmark orange, a blue yearly switch, and two testimonial card colours (clover and fuchsia) are the only hues that are not ink. Museo Sans Rounded sets the UI. Menlo sets code.

Signed-in applet builder, billing, settings, and create all redirect to login or signup. Those URLs are recorded in [site-tree.md](site-tree.md). Nothing was typed into a password, email, profile, or survey field. Google, Apple, and Facebook were not clicked.

| File | What it is |
|---|---|
| [icon.png](icon.png) | IFTTT.ai apple-touch icon, resized to 128 px |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds the measured palette, type, radii, space, and sizes. `light` holds the role aliases. No dark set. Every token carries `$extensions.source`. |
| [DESIGN.md](DESIGN.md) | Not generated. This capture was not added to catalog.json, and `make design-md` writes DESIGN.md from a catalog entry. |
| [style-guide.html](style-guide.html) | Renders the tokens. One theme, so the dark toggle has nothing to switch to. |
| [components.md](components.md) | The public controls and the states that were read |
| [patterns.md](patterns.md) | How the pages combine those controls |
| [site-tree.md](site-tree.md) | Which control opens which page, menu, dialog, or wall. Written before the screenshots. |
| [screenshots/](screenshots) | 62 `{page}-light-{state}.png` captures, 256-colour. Desktop 1440x900, `mobile-*` at 390x844 and 2x. |
| [raw/](raw) | `css-vars.json`, `components-computed.json`, `login-fields.json`, `walls.json` |
| [tools/](tools) | The capture runner and the token builder |

## Brief

Not generated. `make brief` reads catalog.json, and this package is not in the catalog. The task forbade editing catalog.json.

## Health

Not generated. `make grade` reads catalog.json. The scorecard review was not run for the same reason.

## How the values were read

The customer stylesheet is `https://web-assets.ifttt.com/builds/assets/customer-BcV-_DZh.css` (154,331 bytes on 2026-11-21). It declares three custom properties: `--primary-text` (`#111` on `:root`), `--hero-unit` (a calc that scales the home animation), and `--card-color` (per testimonial card). Everything else is a literal in that sheet or a computed style.

[tools/capture/harvest.mjs](tools/capture/harvest.mjs) read the declarations and the computed body, h1, and primary button. [tools/capture/measure.mjs](tools/capture/measure.mjs) read header links, the hero button, featured tabs, the plans switch, service Share and Copy, and the phone menu. Login fields were read by a follow-up script into [raw/login-fields.json](raw/login-fields.json) without typing. [tools/build_tokens.py](tools/build_tokens.py) maps those readings into tokens.json.

Screenshots came from [tools/capture/public.mjs](tools/capture/public.mjs) through Playwright, then [tools/capture/quantize.py](tools/capture/quantize.py). Full-colour originals stay in `~/.design-systems/ifttt/raw-shots`.

## What to distrust

- Hover on the primary button is `opacity: 0.8` in the stylesheet. `light.accent.hover` is that opacity applied to `#111`, not a colour the sheet names.
- The warning token is the wordmark orange. The product has no warning role on the public pages.
- The code type role's line height is derived from the body ratio. The family is measured.
- Several computed focus outlines came back `none`. The 2px ink ring is from a logo-link rule, not from every control.
- The phone explore page grew past the 8-chunk cap (about 53,000 CSS pixels). That stitch was not kept. The viewport shot was.
- The first phone home full-page shot was taken with search open and locked to one screen. It was recaptured. The kept file is the stitch.
- The share dialog's short link was replaced with the public page URL before the screenshot was kept. The dialog chrome is the product's. The URL text in that one shot was rewritten.
- Screenshots are 256-colour. Read colours from tokens.json.
- No crop set was cut. Layout evidence is the full screenshots.

## Fonts

Museo Sans Rounded, with a fallback stack of Museo Sans Rounded Fallback, Avenir Next, Helvetica, Arial, sans-serif. Proprietary. The guide falls back to Avenir Next, Helvetica, Arial. Code uses Menlo, SFMono-Regular, Consolas, Liberation Mono, monospace.

## Coverage

| Checklist item | Status | Where |
|---|---|---|
| Page, surface, text, border, accent | captured | `light.background`, `light.text`, `light.border`, `light.accent` |
| Status colours | partly | success, info, and danger are measured hues. Warning is the wordmark orange, not a status role. |
| Dark theme | not present | `prefers-color-scheme: dark` left the page white |
| Type | captured | display, title, body, button, nav, label. Code family measured, line height derived. |
| Radius, space, size | captured | `core.radius`, `core.space`, `core.size` |
| Motion | partly | logo marquee is 30s linear. Control hovers are opacity, no duration token. Reduced motion not recorded. |
| Button, link, field, switch, tabs, menu, tooltip, dialog, card, badge | captured | [components.md](components.md) and the screenshots |
| Text area | partly | Home prompt is visible. Its own computed style was not stored. |
| Select, checkbox, toast, table | not present | |
| Radio | not captured | A stylesheet rule exists. No public radio was on the captured pages. |
| Hover, focus, pressed, disabled | partly | Hover and active are stylesheet rules. Disabled is a stylesheet rule, not a live control. |
| Form validation error | not captured | No form was submitted. |
| Empty, loading | not captured | No public empty or loading state was reached. |
| Destructive confirmation, onboarding | not present | Onboarding is behind signup. |
| Search | captured | [home-light-search.png](screenshots/home-light-search.png) |
| Login and signup walls | captured as walls | [login-light-default.png](screenshots/login-light-default.png), [join-light-default.png](screenshots/join-light-default.png). Branch stopped. |
| Signed-in app, billing, settings, create | not captured | Redirect to `/join` or `/login`. See [site-tree.md](site-tree.md). |
| Desktop 1440 and phone 390 | captured | Viewport sidecars in the scratch folder. Phone shots are 780 px wide at 2x. |

## Do and don't

- **Do set type and buttons in ink on white.** The hero, the header, and the plans page all do this. [home-light-default.png](screenshots/home-light-default.png)
- **Do make the one action a black pill.** Start building, Log in, and Get started share the 64px radius. [plans-light-default.png](screenshots/plans-light-default.png)
- **Do keep the orange in the wordmark.** It is not a button colour. [home-light-default.png](screenshots/home-light-default.png)
- **Do use the blue only for the yearly switch, and clover for the save badge.** [plans-light-default.png](screenshots/plans-light-default.png)
- **Don't invent a dark theme.** The public site does not ship one.
- **Don't treat a login wall as a signed-in screen.** Create, billing, and settings redirect to signup. [login-light-default.png](screenshots/login-light-default.png)

## Rebuild

```bash
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  node systems/ifttt/tools/capture/harvest.mjs
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
  node systems/ifttt/tools/capture/public.mjs
python3 systems/ifttt/tools/capture/quantize.py ~/.design-systems/ifttt/raw-shots
python3 systems/ifttt/tools/build_tokens.py
python3 systems/ifttt/tools/build_style_guide.py
```

`make design-md` and `make brief` need a catalog.json entry. This capture does not add one.
