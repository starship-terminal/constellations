# Rare Beauty

Rare Beauty is a public makeup shop. This package is a signed-out capture of [https://www.rarebeauty.com](https://www.rarebeauty.com) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the Bestsellers collection, and the Brow Harmony product page were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, shop menu, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, Bestsellers, Brow Harmony |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [components.md](components.md) | Controls seen on the photographed pages |
| [patterns.md](patterns.md) | How those controls sit on the page |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Site icon, 32px source scaled to 128px |
| [icons/](icons/) | Index for that icon |
| [raw/](raw/) | Computed-style readings |
| [tools/](tools/) | Token check |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` was not flipped.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | Cream `#fdfbf8`, ink `#000914` |
| Promo bar | Captured | `#fdf6f0`, 47px, burgundy hairline |
| Nav | Captured | 12px uppercase, `#6f0936` |
| Brand | Captured | Sprite wordmark, 175 by 32px, burgundy |
| Type | Captured, files absent | Ogg Regular for headings, Neue Hass Unica Regular for UI |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured | [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Button | Captured, default | Product Add to bag `#6f0936`, 36px, square. Not clicked |
| Link | Captured | Header departments and footer columns |
| Login wall | Not opened | Account was not followed |
| Newsletter | Stopped | Footer email field was left empty. Submit was not pressed |
| Cart and checkout | Not captured | Cart was not opened |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | No theme control on the public shop |

## Do and don't

- **Keep the page cream and the type ink.** Headings are Ogg Regular. Nav labels are 12px uppercase burgundy. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use burgundy for the wordmark, the hairline, and the filled Add to bag.** Card Add to bag stays an outline. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Stop before account, cart, and the newsletter.** Those controls were listed and not entered.

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the colour and size tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
