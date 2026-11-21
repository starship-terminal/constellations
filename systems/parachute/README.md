# Parachute Home

Parachute Home is a public bedding, bath, and decor shop. This package is a signed-out capture of [https://parachutehome.com](https://parachutehome.com) on 2026-11-22. Prices on the product page read USD. The account host opened as locale en-US. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, one public product, and the about page were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, product, and about, three files |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [raw/](raw/) | The readings those tokens check against |
| [login-review.json](login-review.json) | Empty wall, and where the walk stopped |
| [components.md](components.md) | Controls seen on the public pages |
| [patterns.md](patterns.md) | How those controls sit on a page |
| [style-guide.html](style-guide.html) | The same tokens, rendered |
| [icon.png](icon.png) | Site favicon, resized to 128 px |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [tools/](tools/) | The checker that matches tokens to readings |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## How the values were read

Computed style on the live page, in an incognito preview, after the signup overlay and the chat widget were hidden. Custom properties `--cv-color--*`, `--cv-font-*`, `--cv-space-*`, and `--cv-radius-*` were read from the document element. The wordmark fill was read from the SVG file the header image loads. Font files were not downloaded.

## What to distrust

The header on the homepage is transparent over a photograph, so the department type reads white there. On a white page the same links inherit ink. The login wall uses the system font, not Suisse Intl, and its URL carried OAuth state, so it has no screenshot. The accent `#5b2831` is a token on the page and was not a fill in the shots. Quantized screenshots are not a source of colour.

## Fonts

Suisse Intl is the body, nav, button, and footer face. Canela is the display face, with a Canela Fallback. Files are not in this package. The style guide falls back to Georgia and Arial.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | `#ffffff`, ink `#353331` |
| Brand | Captured | Wordmark SVG, fill `#080808` |
| Type | Captured, files absent | Suisse Intl on the shop, Canela on the hero and product title |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Button | Captured, default | Add to bag is 44px, ink, `4px` radius. Not clicked |
| Link | Captured | Header departments and footer columns |
| Text field | Captured, empty | Sign-in email, not submitted. Footer email, not submitted |
| Password field | Not present | The empty wall asks for email only. Continue was not clicked |
| Login wall | Seen, not photographed | URL carried OAuth state. See [login-review.json](login-review.json) |
| Signup wall | Same wall | Copy says "Sign in or create an account" |
| Newsletter | Stopped | Footer email field was not submitted. Alia overlay was hidden, not submitted |
| Checkout | Not captured | Cart and Add to bag were not opened |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light |

## Do and don't

- **Keep the page white and the type ink.** The page is `#ffffff`. Body type, Add to bag, and the product title are `#353331`. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Use a 4px radius for the primary button.** Add to bag is 44px, radius `4px`, ink fill, white type. Shop the Sale is cream `#f1eee9` with a `2px` radius. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Set display type in Canela.** The homepage hero is 112px, weight 300, white. The product title is 28px, weight 300, ink. [screenshots/about-light-1440.png](screenshots/about-light-1440.png)
- **Stop at the empty email wall.** Sign in and create account share one page. It asks for email and offers Continue. Neither was clicked. The wall was not photographed, because the URL carried OAuth state.

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, ink, cream, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
