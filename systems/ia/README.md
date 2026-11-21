# iA Writer

Public marketing site for iA Writer, the focused Markdown writing app, at [https://ia.net/writer](https://ia.net/writer). Captured signed out on 2026-11-21 from the public pages only. One painted light theme. Desktop 1440 and phone 390. There is no signed-in web app on these pages: the product is a download.

This folder is not in `catalog.json`. `DESIGN.md` is not generated, because that generator needs a catalog entry. Night colours in `tokens.json` are declared in the stylesheet and were not applied on the captured pages.

## Files

| Path | Holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px site icon |
| [tokens.json](tokens.json) | Measured light tokens and declared night tokens |
| [style-guide.html](style-guide.html) | Token page rendered from tokens.json |
| [components.md](components.md) | Header, links, and the download pill |
| [patterns.md](patterns.md) | How the public pages are built |
| [site-tree.md](site-tree.md) | Which control opens which page |
| [login-review.json](login-review.json) | What was offered and what was not submitted |
| [components/](components/) | Crops of the measured controls |
| [screenshots/](screenshots/) | Public page captures, 19 PNGs |
| [raw/](raw/) | Stylesheet variables and computed styles |
| [tools/](tools/) | Rebuild scripts |

## Brief

<!-- brief:start -->
Not generated. `make brief` reads a catalog entry, and this package is not registered.
<!-- brief:end -->

## Health

<!-- health:start -->
Not graded. `make grade` reads a catalog entry.
<!-- health:end -->

## How the values were read

Custom properties come from `https://ia.net/assets/css/main.css`, resolved on `:root` of `https://ia.net/writer` by `tools/capture/vars.mjs`. Component styles come from `tools/capture/public/measure.mjs` on the same page. Screenshots come from headless Playwright, then `tools/capture/quantize.py`. Colours were not sampled from the quantised PNGs.

The T3 preview tab could not produce screenshot frames ("The browser is not producing screenshot frames"). Photographs were taken with headless Playwright.

## What to distrust

The `dark` set is the stylesheet's `--night-*` declarations. No captured page applied them. There is no theme switch. Treat that set as declared, not as a photographed theme.

The header background computed to transparent. Page colour is `--page` (`#f9f9f9`), which matches `theme-color` and the body background.

`--space-line` and `--page-margin` are `clamp()` expressions. The token keeps the declaration.

The Notebook shipping dialog's region labels were stripped from `raw/components-computed.json`. Its screenshot is not in the package.

Screenshots are 256-colour PNGs. Gradients and photographs band. Read colours from `raw/`.

## Fonts

The painted text uses iASansDay. The blue download pill uses iASansNight. Headlines can use iASerifDay. These faces are iA's and are not committed. The tokens name them and fall back to system-ui. The style guide uses the system sans only.

## Coverage

| Item | Status |
|---|---|
| Page, surface, text, muted, accent, border | Captured. [tokens.json](tokens.json) light set, from custom properties |
| Success, warning, error | Declared in the stylesheet. Not shown as a validation state on the captured pages |
| Night palette | Declared. Not applied. Not photographed |
| Type families | Captured as computed stacks. Font files not committed |
| Radius, shadow, page width | Captured from custom properties |
| Download pill height | Captured. 52.0156 px on `/writer` at 1440 |
| Header, nav, menu | Captured. [components.md](components.md), [home-light-menu.png](screenshots/home-light-menu.png) |
| Download, pricing, support, extras, Writer topics | Captured as public pages |
| Phone header and menu | Captured. [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png) |
| Phone home full page | Not captured. The tile dimension check failed |
| Quote expand | Captured. [home-light-quote.png](screenshots/home-light-quote.png) |
| Search field | Photographed on support. Not typed into |
| Newsletter form | Present on pricing. Not submitted |
| Login, signup, settings | Not present on the public Writer pages |
| Signed-in editor | Not captured. It is the downloaded app |
| Checkout | Not captured. Store links were not followed |
| Other iA products | Linked in the menu. Not captured as this package |
| Icons as SVG | Not captured. They stay in the screenshots |
| Cookie banner | Not present |
| Theme switch | Not present |

## Do and don't

- **One blue pill.** The download action is the only blue fill. Other header links stay black until they are the current page. See [home-light-default.png](screenshots/home-light-default.png).
- **Current page is blue text, not a pill.** Buy and Download turn blue when their page is open. See [pricing-light-default.png](screenshots/pricing-light-default.png).
- **The menu is a card, not a new page.** The summary opens a drawer on the same URL. See [home-light-menu.png](screenshots/home-light-menu.png).
- **Phone drops the text links.** At 390 the bar is the wordmark and Menu. See [mobile-home-light-default.png](screenshots/mobile-home-light-default.png).
- **Do not press Download in a capture.** The pill starts a file download. It was measured and photographed, not activated.
- **Do not follow checkout.** Pricing stays on ia.net. The Notebook shipping dialog leaves for a store. That dialog's screenshot is omitted.

## Rebuild

From the repo root, with the Playwright package the kit expects:

```bash
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node systems/ia/tools/capture/vars.mjs
PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs node systems/ia/tools/capture/public/measure.mjs home
python3 systems/ia/tools/build_tokens.py
python3 systems/ia/tools/build_style_guide.py
```

`build_components_md.py` is still the kit example and is not the writer for [components.md](components.md). That file is written by hand from `raw/components-computed.json`.

Do not regenerate `DESIGN.md` until the package has a catalog entry. This capture does not add one.
