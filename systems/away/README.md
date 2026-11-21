# Away

Away is a public luggage shop. This package is a signed-out capture of [https://www.awaytravel.com](https://www.awaytravel.com) on 2026-11-22. The store selector read United States. Prices on the product page read USD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, one public product, and the empty sign-in wall were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, product, login wall, signup wall |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [login-review.json](login-review.json) | Empty walls, and where the walk stopped |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | Header `#ffffff`, ink `#111111` |
| Brand | Captured | Wordmark SVG, black on white. Icon from the public brand mark |
| Type | Captured, files absent | Graphik on the shop, Lyon Display on the kicker and Gifts, a hashed face on the account wall |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Button | Captured, default | Shop Now is a 50px white pill. Add To Cart is a 52px black pill |
| Link | Captured | Header departments and footer columns |
| Text field | Captured, empty | Sign-in email, 56px, 2px radius. Footer email is an 80px pill |
| Password field | Not present | The public wall asks for email only. Continue was not clicked |
| Login wall | Captured, empty | [screenshots/login-light-1440.png](screenshots/login-light-1440.png) |
| Signup wall | Captured, same wall | Create an account is the same empty email page. [screenshots/signup-light-1440.png](screenshots/signup-light-1440.png) |
| Newsletter | Stopped | Footer email field was not submitted |
| Checkout | Not captured | Cart and Add To Cart were not opened |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light. The footer is a black band |

## Do and don't

- **Keep the header white and the sale word red.** The bar is `#ffffff`. SALE, the 25% OFF badge, and Save $87 today are `#d31b3b`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use a pill for Shop Now and Add To Cart.** Both use an 80px radius. Shop Now is white on the hero. Add To Cart is `#111111` with white type. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Stop at the empty email wall.** Sign in and create account share one page. Continue with shop and Continue were not clicked. [screenshots/login-light-1440.png](screenshots/login-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, sale, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
