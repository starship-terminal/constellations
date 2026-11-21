# Reformation

Reformation is a public clothing shop at [https://www.thereformation.com](https://www.thereformation.com). This package is a signed-out capture on 2026-11-22. Prices on the product page read Singapore dollars. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, one public product, the about page, and the empty sign-in wall were photographed. Nothing was typed or submitted.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, product, about, and the empty sign-in wall |
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
| Page colour | Captured | `#ffffff`, ink `#000000` |
| Brand | Captured | Wordmark SVG, fill currentColor |
| Type | Captured, files absent | Newtime R on the shop, TimesNow on the hero |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Button | Captured, default | Add to bag is 44px, ink, square corners. Not clicked |
| Link | Captured | Header nav and footer groups |
| Text field | Captured, empty | Login email and password, 44px, ink underline. Not submitted |
| Password field | Captured, empty | Same wall. Sign in was not clicked |
| Login wall | Captured, empty | [screenshots/login-light-1440.png](screenshots/login-light-1440.png) |
| Signup wall | Same page | "create an account" was not clicked |
| Newsletter | Stopped | Footer email field was not submitted |
| Checkout | Not captured | Bag and add to bag were not opened |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light |

## Do and don't

- **Keep the page white and the type black.** The page is `#ffffff`. Body type, the wordmark on white, and add to bag are `#000000`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use a black bar for the promo line.** The announcement bar is `#000000`, 32px, white type. The nav under it is white. Same shot.
- **Stop before sign in.** The empty wall shows email and password, and a second column for order lookup. Sign in, check status, and sign up were not clicked. [screenshots/login-light-1440.png](screenshots/login-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, ink, announcement, footer, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
