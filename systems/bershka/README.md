# Bershka

Bershka is a public clothing shop. This package is a signed-out capture of [https://www.bershka.com](https://www.bershka.com) on 2026-11-22. The storefront that loaded is Spain, Spanish. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The market gate, the women's homepage, the Mujer menu, dresses, a dress, Sobre Bershka, and the footer were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Gate, homepage, Mujer menu, dresses, product, about, footer |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [style-guide.html](style-guide.html) | The measured colours and controls, with Avenir Next standing in for Whyte |
| [components.md](components.md) | Controls seen on the public pages |
| [patterns.md](patterns.md) | How those controls sit on the photographed pages |
| [icons/](icons/) | The header wordmark path, filled `#000000` |
| [icon.png](icon.png) | 128 px site icon, from the public apple touch icon |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py`, which checks the tokens against the readings |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | `#ffffff`, ink `#000000` |
| Brand | Captured | Wordmark SVG, displayed 133 by 20 |
| Type | Captured, files absent | Whyte, weights 300, 400, 500, 700 |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured | [screenshots/dresses-light-1440.png](screenshots/dresses-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Menu | Captured | [screenshots/menu-mujer-light-1440.png](screenshots/menu-mujer-light-1440.png) |
| Button | Captured, default | Add to bag, 40px, radius 0px, black `#000000` |
| Link | Captured | Header departments and footer columns |
| Text field | Stopped | Search was not typed |
| Password field | Not captured | Sign in was not opened |
| Login wall | Not captured | Iniciar sesión was not opened |
| Newsletter | Stopped | Suscríbete was not submitted |
| Checkout | Not captured | Add to bag and the cart were not clicked |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light |

## Do and don't

- **Keep the page white and the ink at `#000000`.** Titles, prices, and nav sit on `#ffffff`. [screenshots/dresses-light-1440.png](screenshots/dresses-light-1440.png)
- **Use a square black bar for the one action.** Add to bag is 40px, radius 0px, white type on `#000000`. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Mark Promociones in red.** That menu word is `#d72b2b`. The other departments stay ink. [screenshots/menu-mujer-light-1440.png](screenshots/menu-mujer-light-1440.png)
- **Underline the selected department.** Mujer carries a black underline on the 40px header. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, ink, promo, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
