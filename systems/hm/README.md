# H&M

H&M is a public fashion shop. This package is a signed-out capture of [https://www2.hm.com](https://www2.hm.com) on 2026-11-22. The first load geo-routed to Singapore. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, one public product, the empty Singapore login wall, and the empty US signup wall were photographed. Nothing was typed, submitted, or signed in.

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
| Page colour | Captured | Black `#000000`, text `#f2f2f2` |
| Brand | Captured | Wordmark path `#e50010` |
| Type | Captured, files absent | HM Slussen, weight 100 on UI |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Button | Captured, default | Add to bag, Continue, Sign up, all `#f2f2f2` on black, 56px, square |
| Link | Captured | Header departments and footer columns |
| Text field | Captured, empty | Login and signup walls |
| Password field | Captured, empty | Signup wall only. Not typed |
| Login wall | Captured, empty | [screenshots/login-light-1440.png](screenshots/login-light-1440.png) |
| Signup wall | Captured, empty | [screenshots/signup-light-1440.png](screenshots/signup-light-1440.png) |
| Newsletter | Stopped | Subscribe form, not photographed |
| Checkout | Not captured | Bag was not opened |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is already black |

## Do and don't

- **Keep the page black and the wordmark red.** The only brand fill is `#e50010`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use a square light button for the one action.** Add to bag, Continue, and Sign up share 56px, 0 radius, `#f2f2f2` fill. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Stop at the empty email wall.** Singapore sign in asks for email and does not show an identity provider. [screenshots/login-light-1440.png](screenshots/login-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the brand and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
