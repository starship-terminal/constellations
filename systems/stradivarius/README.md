# Stradivarius

Stradivarius is a public Inditex clothing shop. This package is a signed-out capture of [https://www.stradivarius.com](https://www.stradivarius.com) on 2026-11-22. The worldwide URL is a location picker, not a geo-redirect and not a parked page. United States English was chosen. The photographed storefront is [https://www.stradivarius.com/us/](https://www.stradivarius.com/us/). Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the menu, Dresses, one product, Help and contact, and the company profile were read. Nothing was typed or submitted.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, menu, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Location picker, homepage, menu, Dresses, product, company profile |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [style-guide.html](style-guide.html) | The measured colours and controls, with Avenir Next standing in for STRADIVARIUS WEB 2025 |
| [components.md](components.md) | Controls seen on the public pages |
| [patterns.md](patterns.md) | How those controls sit on the photographed pages |
| [icon.png](icon.png) | 128 px site icon, from the shop apple-touch icon |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py`, which checks the tokens against the readings |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## Brief

Not generated. `make brief` rewrites catalog.json, which this capture was told to leave alone.

## Health

Not graded. `make grade` rewrites catalog.json, which this capture was told to leave alone.

## How the values were read

The T3 preview browser opened https://www.stradivarius.com, then https://www.stradivarius.com/us/. Named colours were read from the storefront stylesheets (`--colors-black`, `--colors-white`, `--colors-grey-*`, `--colors-red-dark`, and the rest in [raw/readings.json](raw/readings.json)). Cross-origin sheets on static.e-stradivarius.net were blocked. Type sizes are `getComputedStyle` on the category title, the product title, the menu label, the Filters button, and the prices. `window.innerWidth` was 1440 and `devicePixelRatio` was 2. The preview resize report said 1280 by 800. The screenshots are 2880 by 1800.

## What to distrust

The 256-colour screenshots band the photographs. Read colours from [tokens.json](tokens.json). The contact page tree listed the help topics, but the raster of that page painted a black band, so it was not committed. Product ink `#1d1d1d` is the computed title colour. Named `--colors-grey-dark` is `#151515`. They are not the same token. The company profile uses a different host and a system font stack. Its type is not the shop face.

## Fonts

The shop face is STRADIVARIUS WEB 2025, loaded as an OTF named STRADIVARIUSWEB2025-Bold. The files are not in this package. The style guide uses Avenir Next, then Helvetica. Also declared on the shop, and not used as the body face: StrLogoSans, StrLogoSerif, Oswald.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Region | United States, English | Location picker. Not a geo-redirect |
| Page colour | Captured | White sections, black type |
| Brand | Captured | Wordmark in the header |
| Type | Captured, files absent | STRADIVARIUS WEB 2025 |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Menu | Captured | [screenshots/menu-light-1440.png](screenshots/menu-light-1440.png) |
| Category | Captured | [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Location picker | Captured | [screenshots/gate-light-1440.png](screenshots/gate-light-1440.png) |
| Help | Read, raster discarded | [site-tree.md](site-tree.md) |
| Button | Captured, default | Filters, black, radius 2px. Not applied |
| Link | Captured | Menu rows and footer columns |
| Text field | Captured, empty | Search pill. Not submitted |
| Password field | Not captured | Login redirected to OAuth and was left |
| Login wall | Stopped | /us/login.html redirected to account.stradivarius.com. Nothing typed |
| Newsletter | Stopped | Not submitted |
| Checkout | Not captured | Cart not opened. Add to bag not clicked |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | `color-scheme: normal` |

## Do and don't

- **Keep the shop black on white.** Body type is `#000000` on white sections. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Set menu labels in 16px semibold uppercase.** NEW IN computed 16px, weight 600. [screenshots/menu-light-1440.png](screenshots/menu-light-1440.png)
- **Paint Filters black with a 2px radius.** White 16px type. It was not applied. [screenshots/category-light-1440.png](screenshots/category-light-1440.png)
- **Use `#d0024c` for special prices.** Named `--colors-red-dark`. [screenshots/menu-light-1440.png](screenshots/menu-light-1440.png)
- **Do not invent a dark theme.** No theme control was on the public pages. [raw/readings.json](raw/readings.json)
- **Do not ship STRADIVARIUS WEB 2025.** Name it and fall back to a sans. [tokens.json](tokens.json)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the ink, page, sale, and type sizes against [raw/readings.json](raw/readings.json). It does not recapture the site. `python3 tools/catalog.py design-md stradivarius` from the repo root rewrites catalog.json, so it was not run.

## Where the walk stopped

Login at `/us/login.html` redirected to an OAuth authorize URL on account.stradivarius.com. Nothing was typed and that screenshot was discarded. Guest return login was not entered. Wishlist and checkout were not opened. No size was selected, so Add to bag never appeared. Newsletter and unsubscribe were not submitted. Identity providers were not clicked.
