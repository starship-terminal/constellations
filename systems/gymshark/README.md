# Gymshark

Gymshark is a public athletic shop. This package is a signed-out capture of [https://www.gymshark.com](https://www.gymshark.com) on 2026-11-22. The region prompt offered ROW and US. US was the current shop, with prices in USD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the Women menu, the Women shop page, one public product, and About were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, Women menu, Women shop, product, About |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [style-guide.html](style-guide.html) | The measured colours and controls, with Arial standing in for the licensed faces |
| [components.md](components.md) | Controls seen on the public pages |
| [patterns.md](patterns.md) | How those controls sit on the photographed pages |
| [icons/](icons/) | A wordmark stand-in. The live mark is a raster file and is not copied |
| [icon.png](icon.png) | 128 px site icon, from the apple-touch icon |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py`, which checks the tokens against the readings |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | `#ffffff`, ink `#0d1012` |
| Brand | Captured | Raster wordmark, 100 by 18. Light-page ink `#0d1012` |
| Type | Captured, files absent | SN Skandia on body, Plaak Gymshark on display |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured | [screenshots/shop-women-light-1440.png](screenshots/shop-women-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Button | Captured, default | Square, 52px hero and 54px Add to bag, ink `#0d1012` |
| Link | Captured | Header departments and footer columns |
| Text field | Captured, empty | Search on product and About, `#f4f5f6`, 44px |
| Password field | Not captured | Login was not opened |
| Login wall | Not captured | Account, Login, and Register were not opened |
| Newsletter | Stopped | Promo-bar signup link and footer Email Sign Up were not opened |
| Checkout | Not captured | Add to bag and the cart were not clicked |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light. The homepage header is white type over a photograph |

## Do and don't

- **Keep the page white and the ink near-black.** The page is `#ffffff` and titles are `#0d1012`. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Use a square for the one action.** Add to bag is 54px, radius `0px`, ink on white. Hero shop buttons are white squares. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Put the promo in the ocean bar.** The bar is `#004aa2`, 48px, with a white underlined line. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Strike the old price in sale red.** `$54` is `#dc0428` with a line-through. The sale price stays ink. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, ink, ocean, sale, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
