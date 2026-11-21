# MonoDesk design reference

A token set and component reference for MonoDesk's public site. Read from **www.monodesk.com** on **2026-11-21**, signed out, in headless Chromium at 1440×900 and 390×844.

MonoDesk is a workspace for freelance creatives (clients, projects, proposals, invoices, a client portal, an AI Co-Worker). The public site paints one dark page (`#212121`) with a blue grid hero (`#1c64f5`), a highlighter pill CTA (`#d1ff6e` on `#026232`), and a floating blurred header. The product app at `app.monodesk.com` asks for email and password, or Google. That login was not entered. `https://www.monodesk.com/signin` is 404.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Site icon, 128 px PNG |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds the `:root` brand, spacing and radius scales. `dark` holds the painted page roles and measured component metrics. Every token has `$extensions.source` |
| [style-guide.html](style-guide.html) | Renders the tokens and the main public components |
| [components.md](components.md) | Component inventory and gaps |
| [patterns.md](patterns.md) | How the header, hero, pricing, help and playground combine |
| [site-tree.md](site-tree.md) | Which control opens which page, menu, or dialog, mapped before screenshots |
| [components/crops/](components/crops) | Element screenshots |
| [screenshots/](screenshots) | `{page}-dark-{state}.png`. Desktop 1440×900 at 1×, `mobile-*` 390×844 at 2× |
| [raw/](raw) | [css-vars.json](raw/css-vars.json), [component-tokens.json](raw/component-tokens.json), [components-computed.json](raw/components-computed.json) |
| [tools/](tools) | Builders and the adapted capture kit |

## Brief

<!-- brief:start -->
<!-- brief:end -->

## Health

<!-- health:start -->
<!-- health:end -->

## How the values were read

Custom properties were read from the live CSSOM on `https://www.monodesk.com/` (`tools/capture/vars.mjs`). The brand, type, spacing and radius scales are declared on `:root` in `/_astro/HeroHeader4.*.css` and again in the Geist Mono sheet. Component colours and sizes were read with `getComputedStyle` on the painted elements (`raw/component-tokens.json`). Screenshots were taken with Playwright at the measured viewports in the sidecar JSON. Nothing was submitted. Login, signup, Google, and the phone "email me the link" field were not filled.

## What to distrust

- The body paints `#212121`. The token `--background` is `#dadee1`. That token is kept under `core.color.token-background` and is not the page role.
- `--surface-white` resolves to `#343434`. The name does not match the painted value.
- The header "Get started free" control's anchor has a transparent background. The highlighter fill is on `a.hero-cta-button` in the hero, which is the accent token.
- The hero product frame is a marketing render. It is not the signed-in app.
- Screenshots in `screenshots/` are 256-colour PNGs. Read colours from `tokens.json`.
- Focus, disabled, loading and error styles were not shown. Those tokens are Not captured.
- `DESIGN.md` is absent. `make design-md` writes it only for a slug already in `catalog.json`, and this capture must not edit that file.
- Help's body background computed to brand blue because the hero fills the first viewport. The page ground below the hero is the light band in the screenshot.

## Fonts

Geist for UI and display, declared as `Geist, system-ui, sans-serif` on `body`. Geist Mono is loaded from `/_astro/geist-mono-latin-wght-normal.*.css`. The font files are not committed. The guide falls back to system sans and monospace.

## Coverage

| Item | Status |
|---|---|
| Colour roles (page, surface, text, muted, accent, border) | Captured. [tokens.json](tokens.json) `dark.*`. Success, warning, danger, info: not present on the public surface |
| Type | Captured for display (72/400), body (16/400) and nav label (14/500). Other roles Not captured |
| Spacing and radius scales | Captured from `--spacing-*` and `--radius-*` |
| Elevation | Header blur measured on `.menu` (`backdrop-filter: blur(20px)`). No named elevation scale. Not captured as a token |
| Motion | Not captured. Durations were not read into a token |
| Button, link, text field, menu, dialog, card, badge, accordion, table, icon button | Captured as listed in [components.md](components.md) |
| Text area, select, checkbox, radio, switch, tabs, tooltip, toast, avatar, list row | Not present on the opened public pages |
| Themes | One painted dark page. No theme switch. Light set not present |
| Widths | 1440×900 and 390×844, confirmed in screenshot sidecars |
| Signed-in app | Not captured. `https://app.monodesk.com/login` asks for email and password, or Google. Stopped |
| `www.monodesk.com/signin` | 404 |

## Do and don't

- **Use the highlighter pill for the one primary action.** Fill `#d1ff6e`, text `#026232`, radius 100px. See [home-dark-default.png](screenshots/home-dark-default.png).
- **Keep the header a blurred pill, not a solid bar.** 16px radius, 1px white border at 8% opacity. See the same screenshot.
- **Set the page on `#212121` and the hero on brand blue.** The grid is the hero, not the whole site. See [features-dark-default.png](screenshots/features-dark-default.png).
- **Don't invent a light theme.** The public site does not switch. `--background: #dadee1` is a token, not a second theme.
- **Don't treat the hero frame as the app.** It is a demo render. The app is behind login.
- **Don't fill the phone email prompt.** It is a lead form. See [mobile-home-dark-prompt.png](screenshots/mobile-home-dark-prompt.png).

## Rebuild

```bash
cd systems/monodesk
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

Screenshots are recaptured with `PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node tools/capture/public/public.mjs`, then `python3 tools/capture/quantize.py`.
