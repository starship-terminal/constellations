# Lemonade

The public marketing site at [https://www.lemonade.com/](https://www.lemonade.com/). On 2026-11-21 that URL was a live insurance storefront. The title was "Lemonade: An Insurance Company Built for the 21st Century". Account: none. Theme: one light site. `color-scheme` was `normal`. There is no theme toggle. Widths photographed: 1440 by 900 and 390 by 844.

This is a first capture. `origin/main` had no `systems/lemonade/`. Lemon Squeezy stays `systems/lemonsqueezy/` and is a different product.

The map of controls is [site-tree.md](site-tree.md). The walk record is [login-review.json](login-review.json). `login_extracted` is `not-started`.

| Path | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [site-tree.md](site-tree.md) | Which homepage control opens which page, menu, or dialog |
| [login-review.json](login-review.json) | Public nav that was opened, and the walls that stopped the walk. `login_extracted` is `not-started` |
| [screenshots/](screenshots/) | 16 public pages at desktop and phone width, 256-colour PNGs |
| [DESIGN.md](DESIGN.md) | Hand-written export from the measured tokens. Catalog was not edited, so this file was not generated |
| [tokens.json](tokens.json) | Measured colour roles, type, radius, and button padding |
| [raw/](raw/) | Computed styles from the homepage, the login field, the phone drawer, and the CTA hover |
| [icon.png](icon.png) | 128 px PNG from the site favicon |
| [tools/](tools/) | Capture kit copy. Not adapted to browse the site |
| [style-guide.html](style-guide.html) | Measured colours, type, and buttons |

## How the values were read

Headless Playwright got a Cloudflare "Just a moment..." page (HTTP 403). A real Chrome window that had already passed the check was driven over its debugging port. Screenshots are 256-colour PNGs from `tools/capture/quantize.py`.

Colours and type below are `getComputedStyle` on `https://www.lemonade.com/` at 1440 by 900 on 2026-11-21, plus the login field and the phone drawer. The homepage stylesheets declare 164 custom properties on `:root`. The ones used here were also read as computed colours on real elements.

| Role | Reading | Where |
|---|---|---|
| Page | `rgb(255, 255, 255)` | `body` background. `theme-color` is `#ffffff` |
| Text | `rgb(74, 74, 74)` | `h1` and the Renters nav link. `--night-color` |
| Accent | `rgb(255, 0, 131)` | Check our prices background. `--pink-color` |
| Accent hover | `rgb(220, 0, 115)` | Same control on hover. `--dark-pink-color` |
| On accent | `rgb(255, 255, 255)` | Check our prices text |
| Border | `rgb(217, 217, 217)` | Login email field |
| Disabled | `rgb(231, 231, 231)` | Log in button while the email field is empty |
| Drawer | `rgb(49, 49, 49)` | Phone menu panel, 280 px wide |
| Display | Merriweather, Georgia, serif | Hero `h1`, 55 px, weight 400, line-height 71.5 px |
| UI | Lato, Helvetica Neue, Arial, sans-serif | Nav 16 px, CTA 18 px weight 700 |

The primary button is a short rectangle: `border-radius: 5px`, padding `18px 44px`, height 61 px. Its shadow is `rgba(255, 0, 131, 0.5) 0px 10px 40px -10px`.

## What to distrust

- [DESIGN.md](DESIGN.md) was written by hand from [tokens.json](tokens.json). `catalog.json` was left alone, so `make design-md` was not run and would rewrite the catalog if it were.
- Body computed `font-family` as Times at 10 px. That is the unstyled body, not the painted UI. Headings and controls use Merriweather and Lato. Loaded fonts were Merriweather 400, Lato 400, and Lato 700.
- The quote-start shot was taken while the chat was still typing. It is the first frame of the flow, not a finished empty state.
- Full-page sheets are capped near 6400 CSS px. FAQ is taller than the saved sheet.
- The phone shots are the viewport, not the whole page.
- The language menu was opened. Its screenshot was discarded. The footer behind it shows a public phone number and a street address.
- Cookie banners were hidden with CSS. Accept was not clicked.

## Fonts

Merriweather (display) and Lato (UI) loaded in the page. Fallbacks in the computed stacks are Georgia for display, and Helvetica Neue, Arial, sans-serif for UI. The font files were not copied.

## Coverage

| Item | Status |
|---|---|
| Colour roles, light | Partial. Page, text, accent, hover, border, disabled, drawer. [raw/home-readings.json](raw/home-readings.json) |
| Colour roles, dark theme | Not present. No toggle |
| Type roles | Partial. Display, body, nav label, button |
| Spacing, radii | Partial. Button padding and 5 px radius |
| Button default | Captured. [screenshots/home-light-default.png](screenshots/home-light-default.png) |
| Button hover | Captured. [screenshots/home-light-cta-hover.png](screenshots/home-light-cta-hover.png) |
| Button disabled | Captured. Empty login button. [screenshots/login-light-empty.png](screenshots/login-light-empty.png) |
| Button focus | Partial. Tab landed on the skip link. Outline `rgb(0, 95, 204)` |
| Text field | Captured empty. Login email field. Nothing typed |
| Menu | Captured. Phone drawer. Desktop nav is a link row, not a flyout |
| Dialog | Not present as a marketing dialog. Language menu was opened and its shot was discarded |
| Link | Captured. Header product links |
| Card | Captured. Price cards. [screenshots/home-light-prices.png](screenshots/home-light-prices.png) |
| App shell | Captured. Header, footer columns, phone drawer |
| FAQ | Captured. [screenshots/faq-light-default.png](screenshots/faq-light-default.png) |
| Login | Stopped. Empty email wall |
| Signup | Not present at `/signup` or `/register` (404) |
| Quote start | Stopped. Chat opened, not answered |
| Desktop 1440 and phone 390 | Captured. Homepage and renters at phone width |

## Do and don't

- Use one pink for the primary action. Check our prices is `#ff0083`, and it darkens to `#dc0073` on hover.
- Keep the page white and the type `#4a4a4a`. Headings are Merriweather. Controls are Lato.
- Keep control corners at 5 px. The primary button is a short rectangle, not a pill.
- Leave the login field empty in any replay of this capture. The wall is the evidence. The button stays grey until an address is entered.
- Do not treat the quote chat as a finished screen. The shot is the opening frame, and the flow was not answered.

## Rebuild

```bash
python3 systems/lemonade/tools/capture/quantize.py systems/lemonade/screenshots
```

The kit's public runner was not adapted. Headless Chromium is blocked by Cloudflare on this host. Do not run `build_tokens.py` to invent tokens. The readings in `raw/` are the source.
