# Oysho

Oysho is a public sports and leisure shop. This package is a signed-out capture of [https://www.oysho.com](https://www.oysho.com) on 2026-11-22. The browser landed on a market picker that defaulted to Singapore (English). The storefront photographed is Spain, English, [https://www.oysho.com/es/en/](https://www.oysho.com/es/en/). Desktop width measured 1440 by 900, `devicePixelRatio` 2. The market gate, the homepage, the menu, leggings, one product, Company, Help, and the footer were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Gate, homepage, menu, leggings, product, company, help, footer |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [style-guide.html](style-guide.html) | The measured colours and controls, with Roboto standing in for Oysho-font |
| [components.md](components.md) | Controls seen on the public pages |
| [patterns.md](patterns.md) | How those controls sit on the photographed pages |
| [icons/](icons/) | A wordmark stand-in, filled `#000000` |
| [icon.png](icon.png) | 128 px site icon, from the public apple touch icon |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py`, which checks the tokens against the readings |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | `#fefefe`, ink `#000000` |
| Brand | Captured | Wordmark in the header, icon font `oysho-icon-font` |
| Type | Captured, files absent | Oysho-font, then Roboto |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured | [screenshots/leggings-light-1440.png](screenshots/leggings-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| About | Captured | [screenshots/company-light-1440.png](screenshots/company-light-1440.png) |
| Help | Captured | [screenshots/help-light-1440.png](screenshots/help-light-1440.png) |
| Menu | Captured | [screenshots/menu-light-1440.png](screenshots/menu-light-1440.png) |
| Button | Captured, default | Add to basket, 56px, radius 0px, black `#000000` |
| Link | Captured | Menu columns and footer rows |
| Text field | Stopped | Search and the newsletter field were not typed |
| Password field | Not captured | Sign in was not opened |
| Login wall | Not captured | Sign in was not opened |
| Newsletter | Stopped | Join was not submitted |
| Checkout | Not captured | Add to basket and the basket were not clicked |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light |

## Do and don't

- **Keep the page at `#fefefe` and the ink at `#000000`.** Titles and prices sit on that white. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Use a square black bar for the one action.** Add to basket is 56px, radius 0px, `#f5f4f1` type on `#000000`. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Put the promo in a black bar.** The photographed bar is black with white type. The pink promo token is not that bar. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Set the wordmark in the icon font.** The header letters are `oysho-icon-font`, large, on the left of the white bar. [screenshots/menu-light-1440.png](screenshots/menu-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, ink, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
