# Casper

Signed-out capture of the public Casper shop at [https://casper.com](https://casper.com) on 2026-11-22. Desktop 1440 by 900, `devicePixelRatio` 2. The page is `#ffffff`, body type is Calibre, and the wordmark and footer are navy `#1e306e`.

Photographed the homepage, The One mattress, and the empty login and signup walls. Header, footer, and the public links those controls open are in [site-tree.md](site-tree.md). Colours and type are in [tokens.json](tokens.json). `catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

Stopped at the login wall, the signup wall, the footer subscribe form, and the cart. Nothing was typed. No form was submitted. No identity provider was clicked. No captcha was solved. Add to cart was not clicked. Cart was not opened.


## Files

| File | What it holds |
|---|---|
| [DESIGN.md](DESIGN.md) | Generated export of the tokens |
| [components.md](components.md) | Public components named from the capture |
| [icon.png](icon.png) | Product icon, 128 px |
| [login-review.json](login-review.json) | Empty walls, and where the walk stopped |
| [patterns.md](patterns.md) | Public patterns named from the capture |
| [raw/](raw/) | Readings the tokens were measured from |
| [screenshots/](screenshots/) | Public page screenshots |
| [site-tree.md](site-tree.md) | Public pages and where the walk stopped |
| [style-guide.html](style-guide.html) | Renders the tokens |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [tools/](tools/) | Builders for this package |

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | `#ffffff`, text `#1e306e` |
| Brand | Captured | Blue wordmark on the homepage. [icon.png](icon.png) is the public favicon mark |
| Type | Captured, files absent | Calibre on the shop, NewKansas-Medium on headings |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Button | Captured, default | Shop mattresses is a 50px white pill. Add to cart is a 63px navy pill. Not clicked |
| Link | Captured | Header departments and footer columns |
| Text field | Captured, empty | Login and signup walls, 60px, 8px radius, `#526699` border |
| Password field | Captured, empty | Present on both walls. Nothing typed |
| Login wall | Captured, empty | [screenshots/login-light-1440.png](screenshots/login-light-1440.png) |
| Signup wall | Captured, empty | [screenshots/signup-light-1440.png](screenshots/signup-light-1440.png) |
| Newsletter | Stopped | Footer email field was not submitted |
| Checkout | Not captured | Cart and Add to cart were not opened |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light |

## Do and don't

- **Keep the page white and the bar navy.** The page is `#ffffff` and the 53px announcement bar is `#1e306e`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use a 32px pill for the sale and the cart.** Shop sale is lime `#eaffac`. Add to cart is `#012169`. Both have a `32px` radius. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Stop at the empty account walls.** Login asks for email and password. Sign up asks for name, email, and password. Create account was not clicked. [screenshots/signup-light-1440.png](screenshots/signup-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, ink, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
