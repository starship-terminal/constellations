# SKIMS

SKIMS is a public underwear, clothing, and shapewear shop. This package is a signed-out capture of [https://skims.com](https://skims.com) on 2026-11-22. The shop redirected to `/en-sg`. Prices on the product page read SGD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the clothing collection, one public product, and the about page were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, clothing, product, and about, four files |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [raw/](raw/) | The readings those tokens check against |
| [login-review.json](login-review.json) | Empty wall, and where the walk stopped |
| [components.md](components.md) | Controls seen on the public pages |
| [patterns.md](patterns.md) | How those controls sit on a page |
| [style-guide.html](style-guide.html) | The same tokens, rendered |
| [icon.png](icon.png) | Public wordmark SVG, rasterized to 128 px |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [tools/](tools/) | The checker that matches tokens to readings |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## How the values were read

Computed style on the live page, in an incognito preview, after the Singapore welcome and the cookie notice were closed. Custom properties `--color-primary`, `--color-accent`, `--font-tstar`, and `--font-inter` were read from the document element. The wordmark fill was read from the header SVG. Font files were not downloaded.

## What to distrust

Department type is white over the homepage hero. On a white page the same links are ink. The product buy panel is black, so the product title reads light there. The sale price `#b6263d` is the only red measured. Accent `#986b58` is a token on the page and was not a fill in the shots. The login wall URL carried OAuth state, so it has no screenshot. Quantized screenshots are not a source of colour. `icon.png` is the public Shopify wordmark SVG, not the 16 px favicon.

## Fonts

Inter is the body, nav, and footer-link face. T-Star is the display face, weight 900, on the hero, collection title, product title, and footer headings. Files are not in this package. The style guide falls back to Arial.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | `#ffffff`, ink `#2d2a26` |
| Brand | Captured | Wordmark SVG, fill `#c4d0d9` |
| Type | Captured, files absent | Inter on the shop, T-Star on the hero and headings |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured | [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Button | Captured, disabled | Select a size is 52px, white, `2px` radius. Not clicked |
| Link | Captured | Header departments and footer columns |
| Text field | Captured, empty | Search and the footer email. Neither was submitted |
| Password field | Not present | The empty wall asks for email only. Continue was not clicked |
| Login wall | Seen, not photographed | URL carried OAuth state. See [login-review.json](login-review.json) |
| Signup wall | Same wall | The heading is Sign in. Continue was not clicked |
| Newsletter | Stopped | Footer email field was not submitted |
| Checkout | Not captured | Cart and Add to cart were not opened |
| Phone width | Not captured | Desktop only |
| Dark theme | Partial | The product buy panel and the about page are black. There is no theme toggle |

## Do and don't

- **Keep the page white and the type ink.** The page is `#ffffff`. Promo type, footer links, and the clothing title are `#2d2a26`. [screenshots/category-light-1440.png](screenshots/category-light-1440.png)
- **Set display type in T-Star at weight 900.** The homepage hero is 48px, tracking `1.2px`, `#f6f6f6`. The clothing title is 30px. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use a 2px radius on the buy button and the email field.** Both are 52px. Search is a 40px pill with a `24px` radius. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Stop at the empty email wall.** Sign in asks for email and offers Continue. Neither was filled or clicked. The wall was not photographed, because the URL carried OAuth state.

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, ink, hero, sale, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
