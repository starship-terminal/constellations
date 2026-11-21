# Urban Outfitters

Urban Outfitters is a public clothing, home, and beauty shop. This package is a signed-out capture of [https://www.urbanoutfitters.com](https://www.urbanoutfitters.com) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the Women's mega-menu, the women's clothing grid, one product, and the UO Community page were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, mega-menu, category, product, and community |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [raw/](raw/) | Readings the tokens were checked against |
| [icons/](icons/) | Empty. The site mark is [icon.png](icon.png) |
| [icon.png](icon.png) | Site icon, 128 px, from the apple-touch icon |
| [components/](components/) | `crops/` is empty. Page shots are in [screenshots/](screenshots/) |
| [login-review.json](login-review.json) | Where the walk stopped |
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
| Brand | Captured | Wordmark in the header. [icon.png](icon.png) |
| Type | Captured, files absent | Helvetica on nav, promo, and the community heading |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Mega-menu | Captured | [screenshots/home-mega-light-1440.png](screenshots/home-mega-light-1440.png) |
| Category | Captured | [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Button | Captured, default | Get It Before It's Gone is `#222222` with white type, radius 0. Not clicked |
| Link | Captured | Header departments and footer columns |
| Text field | Captured, empty | Search. Not submitted |
| Password field | Not captured | Sign In / Sign Up was not opened |
| Login wall | Stopped | The button was not clicked |
| Signup wall | Stopped | The same button was not clicked |
| Newsletter | Stopped | SMS and email anchors were not submitted |
| Checkout | Not captured | Bag was not opened. Get It Before It's Gone was not clicked |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light |

## Do and don't

- **Keep the shop white and the ink `#222222`.** The header is `#ffffff`. Nav labels are `#222222` at 12px Helvetica. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use red only for the sale label.** Extra 40% Off Sale is `#d83604`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use green only for the offer line.** The product offer is `#3a8700`. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Use black for the buy button and keep it square.** Get It Before It's Gone is `#222222` with white type and radius 0. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Stop before sign-in, the bag, and checkout.** Sign In / Sign Up was not opened. Get It Before It's Gone was not clicked. [login-review.json](login-review.json)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, ink, sale, promo, and buy tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
