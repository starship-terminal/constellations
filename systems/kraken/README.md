# Kraken design reference

A token set and public-site map for Kraken, the cryptocurrency exchange at [https://www.kraken.com/](https://www.kraken.com/). Captured on 2026-11-21 from the public marketing site, signed out. The live theme is magic light. Desktop captures are 1440 by 900. One phone capture is 390 wide.

`signed_in` is false. The sign-in and sign-up walls were photographed and not filled in. Google, Apple, and passkey were not clicked. No trade, deposit, or verification flow was started.

This package contains no Kraken code and no extracted logo or icon artwork. Screenshots belong to Payward, Inc. ([docs/RIGHTS.md](../../docs/RIGHTS.md)). Borrow structure and proportions.

| File | What it is |
|---|---|
| [tokens.json](tokens.json) | DTCG tokens. `core` holds type, radius, and spacing. `light` is the live magic-light semantic set. `dark` is the same roles declared on `.default-dark-theme, .magic-dark-theme`, not applied on the public site |
| [DESIGN.md](DESIGN.md) | Generated from tokens.json and this README. One theme, no provenance |
| [style-guide.html](style-guide.html) | Light specimens drawn from the measured tokens. Proprietary Kraken fonts are not loaded |
| [components.md](components.md) | Public controls and the states that were not reached |
| [patterns.md](patterns.md) | Header, menus, search, price table, auth card |
| [site-tree.md](site-tree.md) | What each visible public control opens |
| [login-review.json](login-review.json) | What the sign-in and sign-up walls ask for. `signed_in` is false |
| [screenshots/](screenshots) | 14 public captures, quantised to 256 colours |
| [raw/](raw) | `css-vars.json`, the CSSOM reading the tokens come from |
| [tools/](tools) | `build_tokens.py` and the Playwright capture scripts |

## Brief

<!-- brief:start -->
Read [tokens.json](tokens.json) before designing in this style. The public page is `#f6f5f9`, text is `#101114`, and the primary action is `#7132f5`.

### Principles

1. Do use one purple for the primary action.
2. Do keep the page cool grey and the cards white.
3. Do set the hero in the brand face and controls in the product face.
4. Don't treat the declared dark tokens as a live public theme.

Each rule links a screenshot under [Do and don't](#do-and-dont).
<!-- brief:end -->

## Health

<!-- health:start -->
Not graded in this capture. The catalog entry was not added, by request. Run `make grade` after a catalog entry exists.
<!-- health:end -->

## How the values were read

`tools/capture/read-tokens.mjs` opened [https://www.kraken.com/](https://www.kraken.com/) in Playwright and read custom properties from the CSSOM. `tools/build_tokens.py` maps the magic-light semantic names and the marketing type scale into [tokens.json](tokens.json).

The homepage body background computed to `rgb(246, 245, 249)`, which matches `--colors-ds-semantic-surface-page` (`#f6f5f9`). The header Sign up link computed to `rgb(113, 50, 245)`, which matches `--colors-ds-semantic-content-brand` (`#7132f5`).

Dark values were read from the same stylesheets on `.default-dark-theme, .magic-dark-theme`. The public page's body class stayed `magic-light-theme` even with `prefers-color-scheme: dark`. Those tokens are labelled Declared.

## What to distrust

- **Dark theme.** Declared, not seen on the public site. A Pro sign-in link asks for `preferTheme=dark`. That URL was not opened past the wall.
- **Fonts.** Computed stacks name Kraken-Brand and Kraken-Product, with IBM Plex Sans as the next family. The proprietary files are not in this package. Weights in the type tokens are the declared custom properties, not a measured glyph.
- **Disabled text.** `--colors-ds-semantic-content-disabled` is `#fff6` on the light theme selector. That is a white at 40% alpha. It was not seen on a light control, so do not use it as light-theme disabled text.
- **Screenshots.** Quantised to 256 colours. Read colours from tokens.json.
- **Prices in screenshots.** Live quotes from the capture session, not tokens.

## Fonts

| Family | Where | Licence |
|---|---|---|
| Kraken-Brand | Hero headings, computed on `h1` | Proprietary. Not committed. Fallback in the computed stack: IBM Plex Sans, Helvetica, Arial, sans-serif |
| Kraken-Product | Body and buttons, computed on the Sign up link | Proprietary. Not committed. Same fallback stack |

## Coverage

| Item | Status |
|---|---|
| Colour, light | Captured. [tokens.json](tokens.json) `light`, from `raw/css-vars.json` |
| Colour, dark | Declared in CSS, not applied on the public site. `dark` set |
| Type roles | Captured as declared `--fontSize-ds-*` on `:root, .marketing-text-theme`. Hero size also computed (48px / 56px) |
| Spacing | Partial. Button padding measured (8px 12px). Scale steps 4, 16, 32 from radius tokens |
| Radii | Captured. `--border-radius-ds-0` through `round` |
| Border widths | Not captured as a scale. Button border width computed 0 |
| Elevation | Not captured. No shadow token was mapped |
| Motion | Not captured |
| Control height | Captured for the header Sign up link, 36px |
| Breakpoints | Desktop 1440 and phone 390 screenshots. The CSS breakpoint list was not read |
| Button | Default captured. Hover declared. Pressed, disabled, loading not captured |
| Link, menu, search, dialog | Captured as public interactions. [site-tree.md](site-tree.md) |
| Text field | Seen, not filled. Focus and error not captured |
| Text area, checkbox, radio, switch, tooltip, toast, avatar | Not present on the pages opened, or only declared in CSS |
| Tabs, table, card, badge | Seen on the homepage and `/prices` |
| Auth wall | Photographed. [login-review.json](login-review.json). Branch stopped |
| Signed-in app | Not captured. Sign-in required |
| Onboarding | Not captured. Not filled |

## Do and don't

- **Do use one purple for the primary action.** Sign up is `#7132f5` on white text. [screenshots/home-light-default.png](screenshots/home-light-default.png)
- **Do keep the page cool grey and the cards white.** Page `#f6f5f9`, raised surface `#ffffff`. [screenshots/sign-in-light-wall.png](screenshots/sign-in-light-wall.png)
- **Do set the hero in the brand face and controls in the product face.** The `h1` computed to Kraken-Brand. The Sign up link computed to Kraken-Product.
- **Don't treat the declared dark tokens as a live public theme.** The public body class stayed `magic-light-theme`.

## Rebuild

```bash
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node systems/kraken/tools/capture/read-tokens.mjs
python3 systems/kraken/tools/build_tokens.py
```

The screenshot crawl is `systems/kraken/tools/capture/public/capture.mjs`. It hides the cookie banner and does not submit forms.
