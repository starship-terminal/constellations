# ThirdLove

ThirdLove is a public bra and underwear shop. This package is a signed-out capture of [https://www.thirdlove.com](https://www.thirdlove.com) on 2026-11-22. Prices on the product page read USD. Locale `en`. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the Bras category, one product, Our Story, the footer, and the empty sign-in wall were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, category, product, about, footer, and the empty sign-in wall |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [raw/](raw/) | Readings the tokens were checked against |
| [icons/](icons/) | Wordmark note |
| [icon.png](icon.png) | Site favicon, scaled to 128 px |
| [login-review.json](login-review.json) | Empty wall, and where the walk stopped |
| [components.md](components.md) | Controls seen on the public pages |
| [patterns.md](patterns.md) | How the public pages are built |
| [style-guide.html](style-guide.html) | A page that renders the measured tokens |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [tools/](tools/) | The check that tokens still match the readings |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | White `#ffffff`. Footer is the same |
| Brand | Captured | Wordmark PNG, white over the hero, ink on a white header. Favicon is a serif T |
| Type | Captured, files absent | Rules on the shop. Founders Grotesk Text on the promo bar |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured | [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Button | Captured, default | Select Size is 48px, black, pill radius. Not clicked |
| Link | Captured | Header departments and footer columns |
| Text field | Captured, empty | Footer email, and the sign-in email and password |
| Password field | Captured, empty | On the sign-in wall. Sign In was not clicked |
| Login wall | Captured, empty | [screenshots/login-light-1440.png](screenshots/login-light-1440.png) |
| Signup wall | Same wall | Join Now sits beside Sign In. It was not clicked |
| Newsletter | Stopped | Footer email was not submitted |
| Checkout | Not captured | Cart, Select Size, and Add to Bag were not opened |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light |

## Do and don't

- **Keep the page white and the type ink.** Body type is `#2c272d`. The homepage header is transparent over the photograph, so the wordmark and nav are white there. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use burgundy for the promo bar only.** The 40px bar is `#85002c` with white 15px type. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use a black pill for the buy control and gold for rewards.** Select Size is `#000000`, radius `100px`. Join Now is `#f1dd99`. Neither was clicked. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Stop at the empty sign-in wall.** Email and password were empty. Google was not clicked. [screenshots/login-light-1440.png](screenshots/login-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the ink, burgundy, gold, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
