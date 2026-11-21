# Athleta

Athleta is a public women's athletic clothing shop on the Gap Inc. storefront. This package is a signed-out capture of [https://athleta.gap.com](https://athleta.gap.com) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the New menu, New Arrivals, one public product, and Certified B Corp were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, New menu, New Arrivals, product, Certified B Corp |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [style-guide.html](style-guide.html) | The measured colours and controls, with Arial standing in for the licensed faces |
| [components.md](components.md) | Controls seen on the public pages |
| [patterns.md](patterns.md) | How those controls sit on the photographed pages |
| [icons/wordmark.svg](icons/wordmark.svg) | A wordmark stand-in. The live mark is a remote SVG and is not copied |
| [icon.png](icon.png) | 128 px site icon, from the favicon |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py`, which checks the tokens against the readings |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | White page. Universal bar `#000000` |
| Brand | Captured | Wordmark on the white header. Current brand link is white on the black bar |
| Type | Captured, files absent | Phantom Sans 0.9 on body. Sohne Schmal on the B Corp heading |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured | [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Button | Captured, default | Shop Now pill, 52px. Add to Bag 44px, `#0c0c0c` |
| Link | Captured | Header departments and footer columns |
| Text field | Captured, empty | Header search, underlined `#0c0c0c` |
| Password field | Not captured | Account was not opened |
| Login wall | Not captured | Account was not opened |
| Newsletter | Stopped | Footer Sign Up was not typed and not submitted |
| Checkout | Not captured | Add to Bag and the bag were not clicked |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light. The universal bar and promo bar are dark on every photographed page |

## Do and don't

- **Keep the page white and the brand bar black.** The page is white. The universal bar is `#000000`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use a white pill on the photograph.** Shop Now is 52px, radius 999px, black text on white. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Paint the promo bar navy.** The "50% Off Daily Spotlights" bar is `#2c3c68`, 40px, white type. [screenshots/category-light-1440.png](screenshots/category-light-1440.png)
- **Fill Add to Bag ink-soft, not pure black.** Add to Bag is `#0c0c0c`, 44px, pill on the right. It was not clicked. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the ink, promo, lime, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
