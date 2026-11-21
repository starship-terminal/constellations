# New Balance

New Balance is a public athletic shop. This package is a signed-out capture of [https://www.newbalance.com](https://www.newbalance.com) on 2026-11-22. The utility bar said US. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, one public product, the empty login wall, and the empty signup wall were photographed. Nothing was typed, submitted, or signed in.

The UK store stays in [systems/new-balance](../new-balance/README.md). This package does not replace it.

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
| Page colour | Captured | White `#ffffff`, text `#000000` |
| Brand | Captured | Wordmark path `#cf0a2c` |
| Type | Captured, files absent | Proxima Nova W01 on UI, ITC Garamond W01 on the hero |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Button | Captured, default | Shop now, Add to bag, Log in, all `#151415`, 54px, 2px radius |
| Link | Captured | Header departments and footer columns |
| Text field | Captured, empty | Login and signup walls, 58px, 4px radius |
| Password field | Captured, empty | Both walls. Visibility was not toggled |
| Login wall | Captured, empty | [screenshots/login-light-1440.png](screenshots/login-light-1440.png) |
| Signup wall | Captured, empty | [screenshots/signup-light-1440.png](screenshots/signup-light-1440.png) |
| Newsletter | Stopped | Email popup closed. Footer Sign up not opened |
| Checkout | Not captured | Bag was not opened. Add to bag was not clicked |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | No theme control on the captured surfaces |

## Do and don't

- **Keep the page white and the wordmark red.** The only brand fill is `#cf0a2c`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use a near-black button for the one action.** Shop now, Add to bag, and Log in share 54px, 2px radius, `#151415` fill. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Stop at the empty login wall.** Log in asks for email or mobile number and a password, and does not show an identity provider. [screenshots/login-light-1440.png](screenshots/login-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the brand and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
