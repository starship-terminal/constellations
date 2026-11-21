# Coyuchi

Coyuchi is a public organic bedding and bath shop. This package is a signed-out capture of [https://www.coyuchi.com](https://www.coyuchi.com) on 2026-11-22. Prices on the product page read USD. The country selector showed United States (USD $). Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, one public product, and Our Story were photographed. The empty sign-in wall was reached and then left, because its URL carried OAuth state. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, product, and Our Story |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [raw/](raw/) | The readings the tokens check against |
| [icons/](icons/) | Header wordmark SVG |
| [components.md](components.md) | Controls seen on the public pages |
| [patterns.md](patterns.md) | How those controls sit on the page |
| [style-guide.html](style-guide.html) | The same values, drawn |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [tools/](tools/) | Checks tokens against the readings |
| [icon.png](icon.png) | 128px site icon |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | White page, ink `#333333` |
| Brand | Captured | Wordmark SVG, fill `#333333` |
| Type | Captured, files absent | Tiempos Text on the body, Tiempos Headline on the product title, TT Norms Pro on departments |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Button | Captured, default | Add to Cart is 58px, ink, square. Not clicked |
| Link | Captured | Header departments and footer columns |
| Text field | Measured, empty | Sign-in email, 49px, `12px` radius. Screenshot discarded |
| Password field | Not present | The empty wall asks for email only. Continue was not clicked |
| Login wall | Reached, not kept | URL carried OAuth state. Screenshot discarded |
| Signup wall | Same wall | Copy says "Sign in or create an account". No separate form before email |
| Newsletter | Stopped | Footer email field was not submitted |
| Checkout | Not captured | Cart and Add to Cart were not opened |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light |

## Do and don't

- **Keep the page white and the chrome ink.** The page is white. Department type, the wordmark, and Add to Cart are `#333333`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use a square for the primary button.** Shop 25% Off is 60px, white, square. Add to Cart is 58px, ink, square. Size chips are 36px with a stone border. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Stop at the empty email wall.** Sign in asks for email and offers Continue. The URL carried OAuth state, so the shot was discarded. Continue was not clicked.

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the ink, sage, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
