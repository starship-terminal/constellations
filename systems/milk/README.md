# Milk Makeup

Public shop at [https://milkmakeup.com](https://milkmakeup.com), captured signed out on 22 November 2026. Desktop only, 1440 by 900 CSS pixels, `devicePixelRatio` 2. Light only. The shop did not offer a dark theme. No account was used.

## Files

| Path | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Homepage map, the Lip collection, and the Line + Fill product page |
| [tokens.json](tokens.json) | Measured color, type, radius, and spacing |
| [DESIGN.md](DESIGN.md) | Written from those tokens for readers that expect that format |
| [components.md](components.md) | Bar, header, buttons, titles, badge, shade row |
| [patterns.md](patterns.md) | Home, collection, and product layouts |
| [style-guide.html](style-guide.html) | One page of the measured values, Arial fallback |
| [icon.png](icon.png) | Site favicon, rasterized to 128 CSS pixels |
| [icons/](icons/) | Wordmark SVG and [icons/INDEX.tsv](icons/INDEX.tsv) |
| [screenshots/](screenshots/) | Homepage, Lip collection, Line + Fill. Git LFS |
| [raw/readings.json](raw/readings.json) | Computed styles from the walk |
| [tools/build_tokens.py](tools/build_tokens.py) | Checks that the measured keys are still in tokens.json |

## How the values were read

Headed Chrome, viewport 1440 by 900, device scale 2, on 22 November 2026. Component values are `getComputedStyle` on the live homepage, [https://milkmakeup.com/collections/lip](https://milkmakeup.com/collections/lip), and [https://milkmakeup.com/products/line-fill](https://milkmakeup.com/products/line-fill). The filled button color was confirmed on the visible product control (background `rgb(0, 0, 0)`, label `rgb(255, 255, 255)`, 50px tall). Nothing was neutralized. No cookie banner was present.

## What to distrust

Review is the live family. It is not in this package. The style guide uses Arial, which is in the declared fallback stack. GTStandard-M 450 was registered and was not used for the measured controls, so it is not a token. The pink is the Milk Sticks nav color. Other nav labels are white on the dark hero and black on white pages. Homepage SHOP NOW is square. Add to Bag and Buy It Now use a 4px radius. Hover, focus, and pressed were not read. The favicon raster is the 32px icon drawn up to 128, so the edges are hard.

## Fonts

Review, weights 400, 500, 600, and 700, loaded from the shop. Fallback in the computed stack includes Arial and system sans. The family is the shop's webfont. This package does not ship the files.

## Coverage

| Item | Status |
|---|---|
| Color roles, light | Captured. [tokens.json](tokens.json), [home-light-1440.png](screenshots/home-light-1440.png) |
| Dark theme | Not present on the public shop |
| Type roles | Body, nav, hero, collection title, product title, button. [tokens.json](tokens.json) |
| Spacing and radius | Bar, header, hero button, 0px and 4px radii. [tokens.json](tokens.json) |
| Homepage | [home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Lip. [category-light-1440.png](screenshots/category-light-1440.png) |
| Product | Line + Fill. [product-light-1440.png](screenshots/product-light-1440.png) |
| Phone width | Not captured. Desktop only |
| Button hover, focus, pressed, disabled | Not captured |
| Search, cart, login, signup, checkout, subscribe | Not captured. The walk stopped there |
| Footer | Below the photographed viewport. Listed in [site-tree.md](site-tree.md) |

## Do and don't

- **Keep the announcement bar black with white 12px type.** The bar is `#000000` and the copy is `#ffffff`. [home-light-1440.png](screenshots/home-light-1440.png).
- **Use pink only for the current promo nav item.** Milk Sticks is `#f44b8b`. The other nav labels follow the page. [category-light-1440.png](screenshots/category-light-1440.png).
- **Fill Add to Bag and leave Buy It Now as an outline.** The fill is `#000000` with white 17px weight 600 type and a 4px radius. [product-light-1440.png](screenshots/product-light-1440.png).
- **Keep the homepage hero button square and uppercase.** Measured radius is 0, letter-spacing 1.28px, 16px weight 400. [home-light-1440.png](screenshots/home-light-1440.png).

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the measured keys. It does not rewrite tokens.json. Screenshots are Git LFS pointers in git and full PNGs on disk after `git lfs pull`.

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` was not flipped.
