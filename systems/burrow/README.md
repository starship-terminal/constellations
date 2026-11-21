# Burrow

Burrow is a public modular furniture shop. This package is a signed-out capture of [https://burrow.com](https://burrow.com) on 2026-11-22. Prices on the seating page read USD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the seating category, and the public story page were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, seating category, and the story page |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [icons/](icons/) | Header wordmark SVG |
| [icon.png](icon.png) | 128 px mark on the favicon cream tile |
| [raw/](raw/) | Readings the tokens were checked against |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [components.md](components.md) | Controls seen on the public pages |
| [patterns.md](patterns.md) | How those controls sit on the pages |
| [style-guide.html](style-guide.html) | The measured colours and controls, rendered |
| [tools/](tools/) | The token check |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | White `#ffffff`, ink `#262626` |
| Brand | Captured | Wordmark SVG, fill `#383633` |
| Type | Captured, files absent | Suisse Intl on the shop, DM Mono on the eyebrow |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured | [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Button | Captured, default | Shop Sale is 44px, white, `3px` radius. Not clicked |
| Link | Captured | Header departments and footer columns |
| Sale price | Captured | Coral `#e46950` on the seating card |
| Login wall | Stopped | Sign in was not opened |
| Signup wall | Stopped | Homepage modal closed without typing. Footer Subscribe was not submitted |
| Checkout | Not captured | Cart and Add to cart were not opened |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light |

## Do and don't

- **Keep the page white and the sale link rust.** The header is `#ffffff`. Department type is `#262626`. Warehouse Sale is `#883d2a`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use a 3px radius on the light primary button.** Shop Sale is 44px, white fill, black type, letter-spacing `1px`. Add to cart is 45px, ink fill, `2px` radius. It was not clicked. [screenshots/category-light-1440.png](screenshots/category-light-1440.png)
- **Stop at the empty subscribe wall.** The homepage modal and the footer form ask for email and phone. Neither was filled. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, promo, sale, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
