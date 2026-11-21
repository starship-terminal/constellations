# Anthropologie

Anthropologie is a public clothing and home shop. This package is a signed-out capture of [https://www.anthropologie.com](https://www.anthropologie.com) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the Dresses menu, Dresses, a dress page, and Anthro Impact were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, Dresses menu, Dresses, product, Anthro Impact |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [style-guide.html](style-guide.html) | The measured colours and controls, with Avenir Next standing in for the licensed faces |
| [components.md](components.md) | Controls seen on the public pages |
| [patterns.md](patterns.md) | How those controls sit on the photographed pages |
| [icons/](icons/) | The header wordmark path, filled `#26262c` |
| [icon.png](icon.png) | 128 px site icon, from the public favicon |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py`, which checks the tokens against the readings |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | `#fdfdf9`, ink `#26262c`, text `#5c5c5f` |
| Brand | Captured | Wordmark SVG, displayed 170 by 10, teal underline |
| Type | Captured, files absent | Avenir Book and Avenir Medium. Spectral Extra Light is named and was not loaded |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured | [screenshots/dresses-light-1440.png](screenshots/dresses-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Menu | Captured | [screenshots/menu-dresses-light-1440.png](screenshots/menu-dresses-light-1440.png) |
| Button | Captured, default | Add to Basket, 45px, radius 0px, slate `#4b5666` |
| Link | Captured | Header departments and footer columns |
| Text field | Stopped | Search and the footer email field were not typed |
| Password field | Not captured | Sign In was not opened |
| Login wall | Not captured | Sign In / Sign Up was not opened |
| Newsletter | Stopped | The footer email field was not submitted |
| Checkout | Not captured | Add to Basket and the cart were not clicked |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light |

## Do and don't

- **Keep the page cream and the ink at `#26262c`.** Titles, prices, and nav sit on `#fdfdf9`. [screenshots/dresses-light-1440.png](screenshots/dresses-light-1440.png)
- **Use a square slate bar for the one action.** Add to Basket is 45px, radius 0px, white type on `#4b5666`. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Mark Holiday and Sale in red.** Those nav words are `#c33d3d`. The other departments stay ink. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Underline the selected wordmark in teal.** The Anthropologie tab carries `#167a92`. Utility links use the same teal. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, ink, teal, red, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
