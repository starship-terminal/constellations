# Lululemon

Lululemon is a public athletic shop. This package is a signed-out capture of [https://shop.lululemon.com](https://shop.lululemon.com) on 2026-11-22. The region control read US (USD). Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, one public product, and the empty login wall were photographed. Signup uses that same wall. Nothing was typed, submitted, or signed in.

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
| Page colour | Captured | `#fafafa`, ink `#140f0f` |
| Brand | Captured | Wordmark `currentColor`, measured `#140f0f` |
| Type | Captured, files absent | Calibre on body, Saans on nav and headings |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Button | Captured, default | Pill, 44px, `1000px` radius. Quiet `#f4f3f2` or ink `#140f0f` |
| Link | Captured | Header departments and footer columns |
| Text field | Captured, empty | Login wall, 44px, radius `4.8px` |
| Password field | Not present | The wall asks for email only |
| Login wall | Captured, empty | [screenshots/login-light-1440.png](screenshots/login-light-1440.png) |
| Signup wall | Captured, empty | Same wall. [screenshots/signup-light-1440.png](screenshots/signup-light-1440.png) |
| Newsletter | Stopped | Homepage email modal closed, not submitted |
| Checkout | Not captured | Bag was not opened |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light |

## Do and don't

- **Keep the page warm grey and the wordmark ink.** The page is `#fafafa` and the mark is `#140f0f`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use a pill for the one action.** Add to bag and Continue are 44px, radius `1000px`, ink on white. Quiet shop buttons invert that. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Stop at the empty email wall.** Sign in and register share one email field. Continue was not clicked. [screenshots/login-light-1440.png](screenshots/login-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, ink, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
