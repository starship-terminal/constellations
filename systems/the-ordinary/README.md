# The Ordinary

The Ordinary is a public clinical skincare shop. This package is a signed-out capture of [https://theordinary.com](https://theordinary.com) on 2026-11-22. The public entry redirected to the Singapore storefront at [https://theordinary.com/en-sg](https://theordinary.com/en-sg). Prices on the product page read USD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, one public product, and the empty login and signup walls were photographed. Nothing was typed, submitted, or signed in.

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
| Page colour | Captured | `#ffffff`, text `#212529` |
| Brand | Captured | Wordmark SVG, ink `#333333` on the product title |
| Type | Captured, files absent | Raleway on the shop, Geologica on the account walls |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Button | Captured, default | Add To Cart is a 48px square outline. Join Now is a 48px black fill |
| Link | Captured | Header departments and footer columns |
| Text field | Captured, empty | Login and signup walls, 40px, square, black underline |
| Password field | Captured, empty | Present on both walls. Nothing typed |
| Login wall | Captured, empty | [screenshots/login-light-1440.png](screenshots/login-light-1440.png) |
| Signup wall | Captured, empty | [screenshots/signup-light-1440.png](screenshots/signup-light-1440.png) |
| Newsletter | Stopped | Footer email field was not submitted |
| Checkout | Not captured | Cart and Add To Cart were not opened |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light |

## Do and don't

- **Keep the page white and the promo bar black.** The page is `#ffffff` and the 37px promo bar is `#000000`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use a square outline for Add To Cart.** It is 48px, radius `0`, a 1px black border, and `#333333` type. The selected size chip is the only pill. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Stop at the empty account walls.** Sign in asks for email and password. Create account asks for name, email, and password. Join Now and the identity providers were not clicked. [screenshots/login-light-1440.png](screenshots/login-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, ink, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
