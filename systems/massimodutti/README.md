# Massimo Dutti

Massimo Dutti is a public clothing shop. This package is a signed-out capture of [https://www.massimodutti.com](https://www.massimodutti.com) on 2026-11-22. The market picker geo-selected Singapore and English. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the Woman menu, New In, one public product, and About were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, Woman menu, New In, product, About |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [style-guide.html](style-guide.html) | The measured colours and controls, with Georgia standing in for Suisse |
| [components.md](components.md) | Controls seen on the public pages |
| [patterns.md](patterns.md) | How those controls sit on the photographed pages |
| [icons/wordmark.svg](icons/wordmark.svg) | A wordmark stand-in. The live mark is an inline SVG and is not copied |
| [icon.png](icon.png) | 128 px site icon, from the favicon |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py`, which checks the tokens against the readings |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Region | Singapore | Market picker landed on Singapore, English, Women. Continue opened `/sg/` |
| Page colour | Captured | White page. Menu panel `rgb(255, 255, 255)` |
| Brand | Captured | Black wordmark on the white header |
| Type | Captured, files absent | Suisse Light on nav and product. Suisse Regular on the body |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured | [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Button | Captured, default | Add to Basket, 32px, white, 1px black border |
| Link | Captured | Header departments and footer columns |
| Text field | Not captured | Search was not opened |
| Password field | Not captured | Log in was not opened |
| Login wall | Not captured | Log in was not opened |
| Newsletter | Stopped | Footer Newsletter was not opened and not submitted |
| Checkout | Not captured | Add to Basket and the bag were not clicked |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light. About opens on a black story panel |

## Do and don't

- **Keep the page white and the type black.** The header, menu, and product column are white. Type is `#000000`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Set department labels in small caps.** Nav is Suisse Light 12px, letter-spacing 1.92px, uppercase. [screenshots/nav-woman-light-1440.png](screenshots/nav-woman-light-1440.png)
- **Outline Add to Basket.** It is 32px, white, with a 1px black border and no radius. It was not clicked. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Paint the market Continue black.** On the picker, Continue is 32px, `#000000` fill, white type. The photographed fill looked grey. [raw/readings.json](raw/readings.json)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the ink, page, muted, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
