# ThredUp

ThredUp is a public online consignment and thrift shop. This package is a signed-out capture of [https://www.thredup.com](https://www.thredup.com) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, Women, one product, and About were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px site icon, resized from the public 192 px favicon |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Ink, page, promo, sand, burgundy, cream, type, header, and controls |
| [style-guide.html](style-guide.html) | Swatches, the header row, the sale hero, and a price row |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Homepage, category, product, About |
| [components/](components/) | Empty crops folder. No element crops were taken |
| [screenshots/](screenshots/) | Homepage, Women, one product, About |
| [raw/](raw/) | Computed styles read on the homepage, Women, the product, and About |
| [site-tree.md](site-tree.md) | Header, footer, and the pages those controls open |
| [tools/](tools/) | A check that the written tokens match the readings |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

An incognito preview opened https://www.thredup.com. `getComputedStyle` was read on the body, the header, the promo bar, the code chip, the Shop/Sell pill, a nav link, Holiday Shop, search, the sale hero, the Women title, the product brand, the price, the badge, Add to Cart, the footer, and the email field. Add to Cart was not clicked. Search was not submitted. Account was not opened. Sign up was not clicked. Sell was not opened.

A signup dialog opened on its own. Close was clicked. A privacy settings bar was dismissed with its close control. Neither click typed or submitted a form.

The homepage, Women, the product, and About were photographed in that same preview at 1440 by 900 CSS pixels, `devicePixelRatio` 2. PNG files are 2880 by 1800.

## What to distrust

This is the signed-out shop. Do not treat a product price, the promo code, or the promo line as stable chrome. The promo bar rotated between a Black Friday sale line and a Clean Out sell line. Prices on these pages were shown in USD.

The hero panel computed as `rgb(131, 33, 30)`. Holiday Shop, the sale price, and the badge computed as `rgb(131, 33, 29)`. The token records the second. The style guide paints the panel one step lighter.

Season Sans and Season Serif are the computed faces. No font file is in this package. The style guide uses Helvetica Neue and Georgia.

The public favicon is a 192 px PNG. [icon.png](icon.png) is that file resized to 128 px. The header wordmark is a separate SVG and is not the icon.

Phone width was not captured. Hover and focus were not measured. The footer phone line was not photographed.

## Fonts

Season Sans is the computed UI face (400 and 500). Season Serif is the computed display face (400). The files are not in this package.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| Colour, promo | Captured | `#daefc6` bar, white chip |
| Colour, header chrome | Captured | Sand pill, white selected half |
| Colour, sale | Captured | Burgundy price and badge, cream hero type |
| Colour, status | Not captured | No error state was shown |
| Type, body | Captured | 14px Season Sans 400 |
| Type, nav | Captured | 14px, current weight 500 with a 2px underline |
| Type, hero | Captured | 36px Season Serif |
| Type, price | Captured | 20px weight 500 |
| Header | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured | [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Dark theme | Not present | The photographed shop is light |
| Phone width | Not captured | Desktop only |
| Hover and focus | Not captured | Not measured |
| Login, sell, cart, newsletter | Not captured | Walk stopped. Nothing was typed |

## Do and don't

**Keep the promo bar green and the sale price burgundy.** The bar is `#daefc6`. The price and the badge are `#83211d`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) and [screenshots/product-light-1440.png](screenshots/product-light-1440.png).

**Keep Shop selected as a white pill on sand.** The track is `#f3f2ee`, radius 999px. [screenshots/home-light-1440.png](screenshots/home-light-1440.png).

**Do not treat the promo code or a price as chrome.** Both change. This pass read 50WELCOME and $33.49.

**Do not open sell, cart, or account from this package.** Those walks stopped.

## Rebuild

```bash
python3 tools/build_tokens.py
```

The script checks `tokens.json` against `raw/readings.json`. It does not rewrite tokens.
