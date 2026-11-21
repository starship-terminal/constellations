# Glossier

Glossier is a public beauty shop. This package is a signed-out capture of [https://www.glossier.com](https://www.glossier.com) on 2026-11-22. That URL resolved to the Singapore English storefront at [https://www.glossier.com/en-sg](https://www.glossier.com/en-sg). Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, one public product, the empty login wall, and the empty signup wall were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, product, login wall, signup wall |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [login-review.json](login-review.json) | Empty walls, and where the walk stopped |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [components.md](components.md) | Controls seen on the photographed pages |
| [patterns.md](patterns.md) | How those controls sit on the page |
| [icon.png](icon.png) | Site icon, 32px source scaled to 128px |
| [icons/](icons/) | Index for that icon |
| [raw/](raw/) | Computed-style readings |
| [tools/](tools/) | Token check |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | White `#ffffff`, ink `#000000` |
| Nav | Captured | White, 40px, 12px labels |
| Brand | Captured | Italic "Glossier." in Apercu, 32px |
| Type | Captured, files absent | Apercu, then Gill Sans |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Button | Captured, default | Shop now and Add to bag `#e8e8e8`, 40px, square. Not clicked |
| Link | Captured | Header departments and footer columns |
| Text field | Captured, empty | Login and signup walls, 50px |
| Password field | Captured, empty | Both walls. Visibility was not toggled |
| Login wall | Captured, empty | [screenshots/login-light-1440.png](screenshots/login-light-1440.png) |
| Signup wall | Captured, empty | [screenshots/signup-light-1440.png](screenshots/signup-light-1440.png) |
| Newsletter | Stopped | Footer email field was left empty. Submit was not pressed |
| Checkout | Not captured | Bag was not opened |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | No theme control on the public shop |

## Do and don't

- **Keep the page white and the type black.** The wordmark is italic Apercu. Nav labels are 12px. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use the blue only on the campaign and the sale badge.** The hero photograph samples to `#0500f5`. The promo badge is `#0600ff`. Buttons stay grey. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Stop at the empty account form.** Email and password stay empty. Sign in and Create an account were not pressed. [screenshots/login-light-1440.png](screenshots/login-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the colour and size tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
