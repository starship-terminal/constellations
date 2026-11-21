# Floyd

Floyd is a public modular furniture shop at [https://floydhome.com](https://floydhome.com). This package is a signed-out capture on 2026-11-22. Prices on the product page read USD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, one public product, and Design Principles were photographed. Nothing was typed, submitted, or signed in.

floyd.com was not opened. That is a different company.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, product, and Design Principles |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [raw/](raw/) | The readings those tokens check against |
| [icons/](icons/) | Header wordmark SVG |
| [components.md](components.md) | Controls seen on the public pages |
| [patterns.md](patterns.md) | How those controls sit on the page |
| [style-guide.html](style-guide.html) | The measured colours and sizes, rendered |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [icon.png](icon.png) | Site favicon, resized to 128 px |
| [tools/](tools/) | The check that tokens still match the readings |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | `#f8f6ed`, ink `#231e1e` |
| Brand | Captured | Wordmark SVG, fill `#231E1E` |
| Type | Captured, files absent | Floyd Gothic on the shop, GT America Mono on Add To Cart |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Button | Captured, default | Add To Cart is 51px, ink, `5px` radius. Not clicked |
| Link | Captured | Header nav and footer columns |
| Text field | Captured, empty | Footer email, 52px, muted border. Not submitted |
| Password field | Not present | The empty wall asks for email only. Submit was not clicked |
| Login wall | Stopped | Account opened a Shopify URL with OAuth parameters. Screenshot discarded |
| Signup wall | Same wall | Copy says "Sign in or create an account". Not submitted |
| Newsletter | Stopped | Footer email field was not submitted |
| Checkout | Not captured | Cart and Add To Cart were not opened |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light |

## Do and don't

- **Keep the page cream and the type ink.** The page is `#f8f6ed`. Body type, the wordmark, and Add To Cart are `#231e1e`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use a sky bar for the sale line.** The announcement bar is `#65c3e9`, 65px, ink type. The header under it is cream, 71px. Same shot.
- **Stop before the account host.** Account leaves floydhome.com for a Shopify sign-in URL. The screenshot was discarded. Add To Cart and Subscribe were not clicked. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, ink, announcement, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
