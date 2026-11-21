# Tuft & Needle

Tuft & Needle is a public mattress and bedding shop. This package is a signed-out capture of [https://www.tuftandneedle.com](https://www.tuftandneedle.com) on 2026-11-22. Prices on the product page read USD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the Mattresses menu, one public product, and Our Story were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, Mattresses menu, product, and Our Story. Four PNGs |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [raw/](raw/) | The readings the tokens were checked against |
| [icons/](icons/) | A text stand-in for the wordmark, plus an index |
| [components.md](components.md) | Controls seen on the public pages |
| [patterns.md](patterns.md) | How those controls sit on the page |
| [style-guide.html](style-guide.html) | The same tokens, rendered |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [tools/](tools/) | `build_tokens.py`, which checks tokens against the readings |
| [icon.png](icon.png) | Site favicon, resized to 128 px |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | `#ffffff`, deep green `#062d31` |
| Brand | Captured | Wordmark PNG on the header. [icon.png](icon.png) is the site favicon |
| Type | Captured, files absent | Inter on the shop, fields on the hero and product title |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Navigation | Captured | [screenshots/nav-mattresses-light-1440.png](screenshots/nav-mattresses-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Button | Captured, default | Start Saving is sand, 49px, `42px` radius. Add to Cart is mint. Not clicked |
| Link | Captured | Header departments and footer columns |
| Text field | Seen, not used | Subscribe dialog asked for email. Not typed, not submitted |
| Login wall | Not captured | Sign In was not opened |
| Newsletter | Stopped | Subscribe dialog closed with Escape |
| Checkout | Not captured | Cart and Add to Cart were not opened |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light. Deep green is a band, not a theme |

## Do and don't

- **Keep the page white and the chrome deep green.** The page is `#ffffff`. The toolbar, announcement, deals band, and footer are `#062d31`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use mint for the buy button and the hero type.** Add to Cart is `#60edb3` with `#2b2823` type. The homepage headline is the same mint. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Mark Sale in red, and stop before the cart.** The nav Sale link is `#d20000`. The sale price is `#ab2210`. Add to Cart was not clicked. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, deep green, mint, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
