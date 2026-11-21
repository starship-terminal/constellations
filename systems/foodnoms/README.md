# FoodNoms design reference

A token set for the public FoodNoms marketing site (foodnoms.com), captured 2026-11-21, signed out, in headless Chromium. Desktop shots are 1440 x 900. Phone shots are 390 x 844 at 2x. Light and dark both exist: the site follows `prefers-color-scheme`. There is no web app. [https://foodnoms.com/login](https://foodnoms.com/login) is a 404. Get the App opens the Apple App Store. The iOS app was not captured, and no signed-in package was invented.

FoodNoms is worth a capture because the marketing site is a small, consistent system: one orange (`#f8622e`, derived from display-p3) on white or black, Aquawax Pro for every role, pill buttons, and a 25px card radius. The product UI in the hero is a picture of the iOS app, not a web screen.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site apple-touch icon, resized to 128 px |
| [tokens.json](tokens.json) | DTCG tokens: `core`, `light`, `dark`. Every token has `$extensions.source` |
| [DESIGN.md](DESIGN.md) | Generated from tokens.json and this README |
| [style-guide.html](style-guide.html) | Renders the tokens |
| [components.md](components.md) | Controls that exist on the public site, and the ones that do not |
| [patterns.md](patterns.md) | Header, hero, help, news, phone menu |
| [site-tree.md](site-tree.md) | Every public control and what it opens |
| [login-review.json](login-review.json) | Probe result: no web form. `login_extracted` is `not-started` |
| [screenshots/](screenshots) | 42 quantised captures, light and dark |
| [raw/](raw) | Computed-style readings the tokens were built from |
| [tools/](tools) | Builders and the adapted capture kit |

## Brief

<!-- brief:start -->
<!-- brief:end -->

## Health

<!-- health:start -->
<!-- health:end -->

## How the values were read

Headless Chromium opened foodnoms.com with `prefers-color-scheme` light and dark. Painted text and surfaces were read with `getComputedStyle` ([raw/type.json](raw/type.json), [raw/spans.json](raw/spans.json), [raw/measure.json](raw/measure.json)). Framer paints in `color(display-p3 ...)`. Tokens store those channels as hex (`channel * 255`). A canvas sRGB conversion clips the orange to `#ff5407`, so that conversion was not used. Radii, sizes, and font stacks are the computed values.

Nothing was signed into. The newsletter field was focused and left empty. The help search field received the word `widgets` so the result list could be photographed. No form was submitted. App Store document navigations were aborted.

## What to distrust

- The orange hex is a P3-channel conversion, not a declared CSS variable. Framer's own tokens are hashed `--token-<uuid>` names with no role labels.
- Get the App's `<a>` reports `color: rgb(0, 0, 238)` and `font: sans-serif`. The painted label is the inner `<p>`. Read the label from `core.font.family.label`.
- Dark search scrim was not sampled separately. `dark.scrim` repeats the light reading.
- Screenshots are 256-colour PNGs. Read colours from tokens.json.
- Phone mockups on the home page are marketing images of the iOS app. They are not measurements of the app.
- Press social buttons use one-off fills (blue, purple, pink). They are not brand tokens.

## Fonts

**Aquawax Pro** (Bold, DemiBold, Medium, Heavy) is the site face, served as woff2 from framerusercontent.com. **Fragment Mono** is loaded from fonts.gstatic.com and was not seen on the captured text roles. **Inter** is declared and was not the painted face on the roles that were measured. None of these files are in the package. The style guide falls back to the system sans.

## Coverage

| Checklist item | Status |
|---|---|
| Colour roles, light and dark | Captured. [tokens.json](tokens.json), [screenshots/home-light-default.png](screenshots/home-light-default.png), [screenshots/home-dark-default.png](screenshots/home-dark-default.png) |
| Type roles | Captured for display, nav, lede, wordmark, section. Code role not present. |
| Spacing | Partly. CTA padding only. No declared spacing scale. |
| Radii | Captured: 20px pill, 25px card, 40px field. |
| Border widths | Focus outline 1px. No design-system border scale. |
| Elevation | Not present. No box-shadow on the measured controls. |
| Motion | Captured: 0.4s link colour, cubic-bezier(0.44, 0, 0.56, 1). Reduced motion not observed as a separate theme. |
| Sizing | Captured: 40px button, 42px field. Icon sizes not tokenised. |
| Layout | Captured at 1440 and 390. Content width of the footer band measured at 1376px on a 1440 viewport. |
| Button | Captured default, hover, focus. Pressed fill Not captured as its own value. |
| Icon button | Captured: phone menu toggle. [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png) |
| Link | Captured. |
| Text field | Captured empty and focused. Not submitted. |
| Text area, select, checkbox, radio, switch | Not present. |
| Tabs | Not present. |
| Menu | Captured, phone only. |
| Tooltip, toast | Not present. Press "Copied!" is a label change. |
| Dialog | Captured: help search. |
| Card, list row | Captured. |
| Table, avatar, badge | Not present. |
| App shell | Not present on the web. Marketing header and footer only. |
| Form validation | Not captured: form was not submitted. |
| Empty, loading, error | 404 page captured ([screenshots/login-404-light-default.png](screenshots/login-404-light-default.png)). No loading state. |
| Destructive confirmation | Not present. |
| Search | Captured. [screenshots/help-light-search-results.png](screenshots/help-light-search-results.png) |
| Onboarding | Not present on the web. |
| Signed-in app | Not captured. No web sign-in. iOS app not opened. |

## Do and don't

- **Do use one orange.** The wordmark, Get the App, help links, and the footer band are the same orange. Screenshot: [screenshots/home-light-default.png](screenshots/home-light-default.png).
- **Do pill the primary button.** Get the App is 40px tall with a 20px radius. Screenshot: [screenshots/home-light-default.png](screenshots/home-light-default.png).
- **Do follow the system theme.** Light is white, dark is black, and the orange does not change. Screenshot: [screenshots/home-dark-default.png](screenshots/home-dark-default.png).
- **Don't treat the hero phones as the web app.** They are pictures. The web site has no food log.
- **Don't invent a sign-in screen.** `/login` is a 404. Screenshot: [screenshots/login-404-light-default.png](screenshots/login-404-light-default.png).
- **Don't submit the newsletter to see its error state.** It was left empty on purpose.

## Rebuild

```bash
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

Screenshots are regenerated with `PLAYWRIGHT` set and `node tools/capture/public/public.mjs`, then `python3 tools/capture/quantize.py`.
