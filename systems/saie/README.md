# Saie

Public shop at [https://saiehello.com](https://saiehello.com), captured signed out on 22 November 2026. Desktop only, 1440 by 900 CSS pixels, `devicePixelRatio` 2. Light only. The shop did not offer a dark theme. No account was used.

## Files

| Path | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Homepage map, the Lip collection, and the Glossybounce product page |
| [tokens.json](tokens.json) | Measured color, type, radius, and spacing |
| [DESIGN.md](DESIGN.md) | Written from those tokens for readers that expect that format |
| [components.md](components.md) | Bar, header, buttons, title, shade chip, filter rail |
| [patterns.md](patterns.md) | Home, collection, and product layouts |
| [style-guide.html](style-guide.html) | One page of the measured values, Arial fallback |
| [icon.png](icon.png) | Site favicon, rasterized to 128 CSS pixels |
| [icons/](icons/) | Wordmark SVG and [icons/INDEX.tsv](icons/INDEX.tsv) |
| [screenshots/](screenshots/) | Homepage, Lip collection, Glossybounce. Git LFS |
| [raw/readings.json](raw/readings.json) | Computed styles and the link list from the walk |
| [tools/build_tokens.py](tools/build_tokens.py) | Checks that the measured keys are still in tokens.json |

## How the values were read

Headless Chromium, viewport 1440 by 900, device scale 2, on 22 November 2026. Custom properties were read from `:root` (`--color-black-main`, `--color-bg`, `--color-purple`, `--header-height`). Component values are `getComputedStyle` on the live homepage, [https://saiehello.com/collections/lip](https://saiehello.com/collections/lip), and [https://saiehello.com/products/glossybounce](https://saiehello.com/products/glossybounce). The filled button color was confirmed on the visible product control (`top` 632, 600 by 64). Nothing was neutralized. No cookie banner was present.

## What to distrust

Ordinary-Display is the live family. It is not in this package. The style guide uses Arial, which is the declared fallback. Victor Serif and unionbold were registered and not loaded on these pages, so they are not tokens. The announcement lilac is the bar text color, not a body muted color. Card buttons use a 1px black border. The homepage SHOP NOW uses a 2px black border. The product button uses a 2px ink border. Radius is 0 on the controls that were measured. Hover, focus, and pressed were not read. The favicon raster is the 32px GIF drawn up to 128, so the edges are soft.

## Fonts

Ordinary-Display, weights 400 and 500, loaded from the shop. Weights 300, 700, and 900 were declared and not loaded. Ordinary-Text was declared and not loaded. Fallback in the computed stack: Arial, sans-serif. The family is the shop's webfont. This package does not ship the files.

## Coverage

| Item | Status |
|---|---|
| Color roles, light | Captured. [tokens.json](tokens.json), [home-light-1440.png](screenshots/home-light-1440.png) |
| Dark theme | Not present on the public shop |
| Type roles | Body, nav, heading, button. [tokens.json](tokens.json) |
| Spacing and radius | Bar, header, button padding, radius 0. [tokens.json](tokens.json) |
| Homepage | [home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Lip. [category-light-1440.png](screenshots/category-light-1440.png) |
| Product | Glossybounce. [product-light-1440.png](screenshots/product-light-1440.png) |
| Phone width | Not captured. Desktop only |
| Button hover, focus, pressed, disabled | Not captured |
| Search, bag, login, signup, checkout, subscribe | Not captured. The walk stopped there |
| Footer | Listed in [site-tree.md](site-tree.md). Below the photographed viewport |

## Do and don't

- **Use the ink bar and the lilac announcement type together.** The bar is `#1b2121` and the copy is `#c0c0da`. [home-light-1440.png](screenshots/home-light-1440.png).
- **Keep buttons square.** Measured radius is 0 on SHOP NOW, the card button, and the product button. [product-light-1440.png](screenshots/product-light-1440.png).
- **Set nav and buttons in uppercase 13px weight 500.** [category-light-1440.png](screenshots/category-light-1440.png).
- **Fill the product add button with ink and white type.** Outline buttons stay for the hero and the collection cards. [product-light-1440.png](screenshots/product-light-1440.png).

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the measured keys. It does not rewrite tokens.json. Screenshots are Git LFS pointers in git and full PNGs on disk after `git lfs pull`.

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` was not flipped.
