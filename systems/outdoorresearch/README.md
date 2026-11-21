# Outdoor Research

Outdoor Research is a public outdoor clothing and gear shop. This package is a signed-out capture of [https://www.outdoorresearch.com](https://www.outdoorresearch.com) on 2026-11-22. The shop was already the United States store, with a US flag in the header and prices in USD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the Women menu, the Women shop page, one public product, and Our Story were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, Women menu, Women shop, product, Our Story |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [style-guide.html](style-guide.html) | The measured colours and controls, with Arial standing in for the licensed faces |
| [components.md](components.md) | Controls seen on the public pages |
| [patterns.md](patterns.md) | How those controls sit on the photographed pages |
| [icons/](icons/) | A wordmark stand-in. The live mark is a raster file and is not copied |
| [icon.png](icon.png) | 128 px site icon, from the 32 px favicon |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py`, which checks the tokens against the readings |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | `#ffffff`, ink `#333132` |
| Brand | Captured | Raster wordmark on the ink header. Gifts label `#fee32f` |
| Type | Captured, files absent | ff-good-web-pro on body, Gilroy on display |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured | [screenshots/shop-women-light-1440.png](screenshots/shop-women-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Button | Captured, default | Pill hero button, 50px. Add To Cart 60px, ink `#333132` |
| Link | Captured | Header departments and footer columns |
| Text field | Captured, empty | Header search, `#e4e4e4`, 44px |
| Password field | Not captured | Login was not opened |
| Login wall | Not captured | Log in was not opened |
| Newsletter | Stopped | Footer signup was not opened and not submitted |
| Checkout | Not captured | Add To Cart and the cart were not clicked |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light. The header and footer are ink on every photographed page |

## Do and don't

- **Keep the page white and the chrome ink.** The page is `#ffffff`. The header, footer, and Add To Cart are `#333132`. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Use a white pill on the photograph.** Shop Gifts For Him is 50px, radius 31px, white on the hero. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Mark Gifts in yellow and sale in red.** Gifts is `#fee32f`. Women's Sale is `#cc4428`. [screenshots/nav-women-light-1440.png](screenshots/nav-women-light-1440.png)
- **Leave the search square and grey.** The header field is `#e4e4e4`, 44px, radius 0. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, ink, quiet, sale, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
