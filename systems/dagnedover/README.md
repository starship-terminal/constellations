# Dagne Dover

Dagne Dover is a public bag shop. This package is a signed-out capture of [https://www.dagnedover.com](https://www.dagnedover.com) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, Shop All, the Landon Carryall page, and Our Story were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, Shop All, Landon Carryall, Our Story |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [style-guide.html](style-guide.html) | The measured colours and controls, with Trebuchet MS standing in for the licensed faces |
| [components.md](components.md) | Controls seen on the public pages |
| [patterns.md](patterns.md) | How those controls sit on the photographed pages |
| [icons/](icons/) | The header wordmark path, filled `#333333` |
| [icon.png](icon.png) | 128 px wordmark, rasterized from that path |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py`, which checks the tokens against the readings |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | `#ffffff`, body text `#666666`, titles `#333333` |
| Brand | Captured | Wordmark SVG, 192 by 20. White on the homepage hero, ink on light pages |
| Type | Captured, files absent | nimbus-sans on body, nimbus-sans-condensed on display and nav |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured | [screenshots/shop-all-light-1440.png](screenshots/shop-all-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Button | Captured, default | Pill, 46px Add to bag, ink `#333333` |
| Link | Captured | Header departments and footer columns |
| Text field | Stopped | Email signup and search were not typed |
| Password field | Not captured | Account was not opened |
| Login wall | Not captured | The account icon was not opened |
| Newsletter | Stopped | The 30% off dialog was closed. The footer email field was not submitted |
| Checkout | Not captured | Add to bag, Waitlist, Pre-order, and the cart were not clicked |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light. The homepage header is white type over a photograph |

## Do and don't

- **Keep the page white and the ink at `#333333`.** Titles, prices, and the Add to bag fill are that ink. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Use a pill for the one action.** Add to bag is 46px, radius `9999px`, white type on ink. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Put the promo in the orange bar on the homepage.** The bar is `#ff3600`, 38px, with a white underlined line. On the product page the same bar is ink. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Mark a new or favorite card with an orange flag.** The badge is `#ff3600`, white type, radius `0px 5px 5px 0px`. [screenshots/shop-all-light-1440.png](screenshots/shop-all-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, ink, orange, lime, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
