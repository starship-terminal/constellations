# Pull&Bear

Pull&Bear is a public Inditex clothing shop. This package is a signed-out capture of the United Kingdom storefront at [https://www.pullandbear.com/gb/](https://www.pullandbear.com/gb/) on 2026-11-22. The start URL was [https://www.pullandbear.com](https://www.pullandbear.com). It geo-redirected to Singapore, a closure notice, so the walk continued on the United Kingdom shop the country picker offered. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the menu, New arrivals, one product, brand history, and the footer were photographed. Nothing was typed or submitted. Log in, the basket, and Add were not opened.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, menu, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, menu, New arrivals, product, brand history, footer |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [style-guide.html](style-guide.html) | The measured colours and controls, with Helvetica standing in for Neue Haas |
| [components.md](components.md) | Controls seen on the public pages |
| [patterns.md](patterns.md) | How those controls sit on the photographed pages |
| [icons/wordmark.svg](icons/wordmark.svg) | A wordmark stand-in. The live mark is an image and is not copied |
| [icon.png](icon.png) | 128 px site icon, from the apple-touch icon |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py`, which checks the tokens against the readings |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | White page, black text |
| Brand | Captured | Wordmark centred in the header |
| Type | Captured, files absent | Neue Haas. Display 46px weight 600. Body 12px muted |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Menu | Captured | [screenshots/menu-light-1440.png](screenshots/menu-light-1440.png) |
| Category | Captured | [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Footer | Captured | [screenshots/footer-light-1440.png](screenshots/footer-light-1440.png) |
| Button | Captured, default | Add is a black rectangle. It was not clicked |
| Link | Captured | Menu columns and footer labels |
| Text field | Captured, empty | Header search, underlined black |
| Password field | Not captured | Log in was not opened |
| Login wall | Not captured | Log in was not opened |
| Newsletter | Not present | No subscribe field on the photographed pages |
| Checkout | Not captured | Add and the basket were not clicked |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light. The Add button and the wordmark on photographs are black or white |

## Do and don't

- **Keep the page white and the type black.** The page is `#ffffff`. Text is `#000000`. Muted copy is `#5a5a5a`. [screenshots/about-light-1440.png](screenshots/about-light-1440.png)
- **Centre the wordmark.** Menu sits left. Search, account, and basket sit right. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Paint the promo bar sky blue.** The Mix & Match bar is `#71c5fa`, 36px, black type. [screenshots/category-light-1440.png](screenshots/category-light-1440.png)
- **Set display type at 46px, weight 600.** "AN EVER YOUNG COMMUNITY" is Neue Haas, 46px, line-height 70px, tracking 0.7px. [screenshots/about-light-1440.png](screenshots/about-light-1440.png)
- **Leave Add black and unclicked.** Add is a black rectangle beside Apple Pay. It was not clicked. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the ink, page, muted, promo, sale, and display tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
