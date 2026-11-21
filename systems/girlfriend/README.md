# Girlfriend Collective

Girlfriend Collective is a public activewear shop. This package is a signed-out capture of [https://girlfriend.com](https://girlfriend.com) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, one public product, and Our Story were photographed. The account control redirects to an OAuth login and was not photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, product, Our Story |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [login-review.json](login-review.json) | Where the walk stopped |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [components.md](components.md) | Components, observed states, and gaps |
| [components/](components/) | Empty component folder |
| [patterns.md](patterns.md) | Page patterns and screenshot links |
| [style-guide.html](style-guide.html) | Colour and control samples |
| [raw/](raw/) | Saved measurements |
| [tools/](tools/) | Token checks |
| [icon.png](icon.png) | Site icon |
| [icons/](icons/) | Wordmark and icon index |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | `#ffffff`, ink `#000000` |
| Brand | Captured | Wordmark fill `#0d0d29` |
| Type | Captured, files absent | Neue Haas Grotesk Text Roman on body, Canela Thin on display, Space Mono on the promo |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Button | Captured, default | Pill, 41px, `30px` radius. Quiet white on the hero. Ink `#000000` on Add to Cart |
| Link | Captured | Header departments and footer columns |
| Text field | Captured, empty | Footer email, 54px, left radius `30px`. Not submitted |
| Password field | Not captured | The account wall is an OAuth URL and was not photographed |
| Login wall | Not captured | `/account` redirects to `account.girlfriend.com` with an OAuth query |
| Signup wall | Not captured | Create account uses that same host |
| Newsletter | Stopped | 15% dialog closed. Footer email left empty |
| Checkout | Not captured | Cart and Add to Cart were not opened |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light. `palette--light` is on the body |

## Do and don't

- **Keep the page white and the wordmark navy.** The page is `#ffffff` and the mark is `#0d0d29`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use a pill for the one action.** Add to Cart is 41px, radius `30px`, white on ink. Shop Compressive inverts that: ink on white. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Stop before the account host.** My Account leaves `girlfriend.com` for an OAuth login. Nothing was typed there. [login-review.json](login-review.json)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, ink, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
