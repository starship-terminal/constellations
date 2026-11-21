# Bombas

Bombas is a public sock, underwear, and apparel shop. This package is a signed-out capture of [https://bombas.com](https://bombas.com) on 2026-11-22. The promo bar shows Singapore. Prices read SGD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the Women collection, one public product, About, and the empty Log In dialog were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, Women collection, product, About, and the empty Log In dialog |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [raw/](raw/) | The readings those tokens were checked against |
| [icons/](icons/) | A stand-in wordmark. The live mark is an icon font |
| [icon.png](icon.png) | Site favicon, resized to 128 px |
| [login-review.json](login-review.json) | Empty wall, and where the walk stopped |
| [components.md](components.md) | Controls seen on the public pages |
| [patterns.md](patterns.md) | How those controls sit on a page |
| [style-guide.html](style-guide.html) | The measured colours and controls, in Arial |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [tools/](tools/) | A check that tokens still match the readings |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | Header `#fdfcf6`, navy `#223859` |
| Brand | Captured | Icon-font wordmark, `#030302`. Favicon resized to [icon.png](icon.png) |
| Type | Captured, files absent | Conforto on the shop, Cabrio on the hero, Decoy on titles |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured | [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Button | Captured, default | Add to Bag is 56px, navy, `14px` radius. Not clicked |
| Link | Captured | Header departments and footer columns |
| Text field | Captured, empty | Login email and password, 44px, `12px` radius |
| Password field | Captured, empty | Same dialog. Not typed |
| Login wall | Captured, empty | [screenshots/login-light-1440.png](screenshots/login-light-1440.png) |
| Signup wall | Stopped | Sign Up sits on the login dialog and was not clicked |
| Newsletter | Stopped | Footer email field was not submitted |
| Checkout | Not captured | Cart and Add to Bag were not opened |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light |

## Do and don't

- **Keep the header cream and the chrome navy.** The header is `#fdfcf6`. The promo bar, Add to Bag, and the login button are `#223859`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use a 14px radius on Add to Bag and 12px on the pills.** Add to Bag is 56px, navy, white type. Shop Women is 40px with a `12px` radius. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Stop at the empty login dialog.** It asks for email and password and offers Facebook and Google. Neither was clicked. [screenshots/login-light-1440.png](screenshots/login-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, navy, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
