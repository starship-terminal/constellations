# Quince

Quince is a public apparel, home, and beauty shop. This package is a signed-out capture of [https://www.quince.com](https://www.quince.com) on 2026-11-22. Prices on the product page read USD. Locale en-US. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, one category, one product, About Us, and the empty sign-in wall were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, category, product, about, footer, and the empty sign-in wall |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [raw/](raw/) | Readings the tokens were checked against |
| [icons/](icons/) | Wordmark SVG |
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
| Page colour | Captured | White `#ffffff`. Header is the same |
| Brand | Captured | Wordmark SVG, fill `#21201f`. Favicon is a Q on cantaloupe |
| Type | Captured, files absent | Grosa on the shop, ivy-headline on the hero |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured | [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Button | Captured, default | Add to Bag is 52px, cantaloupe `#ffa273`, pill radius. Not clicked |
| Link | Captured | Header departments and footer columns |
| Text field | Captured, empty | Search, and the sign-in email |
| Password field | Not present | The empty wall asks for email only. Continue was not clicked |
| Login wall | Captured, empty | [screenshots/login-light-1440.png](screenshots/login-light-1440.png) |
| Signup wall | Same wall | The heading is Sign in / Register. No separate form before email is submitted |
| Newsletter | Stopped | Footer email was not submitted |
| Checkout | Not captured | Cart and Add to Bag were not opened |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light |

## Do and don't

- **Keep the page white and the type ink.** The header is `#ffffff`. Nav, titles, and Add to Bag type are `#21201f`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use cantaloupe for the one loud control.** Search, Shop Now, and Add to Bag are `#ffa273`. Holiday Gifts is the only rust label, `#bc5a28`. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Use a pill for the primary action and a square chip for size.** Add to Bag is 52px with radius `9999px`. Size chips are 40 by 56px with radius `0`. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Stop at the empty email wall.** Sign in and Register share one page. It asks for email and offers Continue with Google. Neither was used. [screenshots/login-light-1440.png](screenshots/login-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the ink, cantaloupe, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
