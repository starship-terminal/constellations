# Puma

Puma is a public sportswear shop. This package is a signed-out capture of [https://us.puma.com/us/en](https://us.puma.com/us/en) on 2026-11-22. `https://us.puma.com` resolved to that US English storefront. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, one public product, the empty login wall, and the empty signup wall were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, product, login wall, signup wall |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [login-review.json](login-review.json) | Empty walls, and where the walk stopped |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [style-guide.html](style-guide.html) | Measured colours, type, and buttons |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | White `#ffffff`, ink `#191919` |
| Nav | Captured | Black `#191919`, white type, 80px |
| Brand | Captured | Leaping cat, `currentColor`, white on the nav |
| Type | Captured, files absent | FFDINforPuma, then Inter |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Button | Captured, default | Add to cart `#191919`, 56px, 2px radius. Not clicked |
| Disabled button | Captured | Empty Login and Create account `#bdc1c5` |
| Link | Captured | Header departments and footer columns |
| Text field | Captured, empty | Login and signup walls, 48px |
| Password field | Captured, empty | Both walls. Visibility was not toggled |
| Login wall | Captured, empty | [screenshots/login-light-1440.png](screenshots/login-light-1440.png) |
| Signup wall | Captured, empty | [screenshots/signup-light-1440.png](screenshots/signup-light-1440.png) |
| Newsletter | Stopped | Footer has no email field. Membership email drawer was closed without typing |
| Checkout | Not captured | Cart was not opened |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | No theme control on the public shop |

## Do and don't

- **Keep the nav black and the page white.** The leaping cat is white on `#191919`. Body type is `#191919` on white. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use red only for the sale price.** `$64.99` is `#ba2b20`. The crossed-out price stays ink. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Stop at the empty account form.** Login and Create account stay grey until the fields are filled. They were not filled. [screenshots/login-light-1440.png](screenshots/login-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the colour and size tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
