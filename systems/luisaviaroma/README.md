# LUISAVIAROMA

LUISAVIAROMA is a public luxury shop. This package is a signed-out capture of [https://www.luisaviaroma.com](https://www.luisaviaroma.com) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, Women, one public product, and Frequently Asked Questions were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, Women, product, FAQ |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [raw/readings.json](raw/readings.json) | The computed styles the tokens come from |
| [style-guide.html](style-guide.html) | Announcement, nav, and add-to-bag colours |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [components.md](components.md) | Header, nav, product card, and add to bag |
| [patterns.md](patterns.md) | Homepage, category, product, and FAQ |
| [icon.png](icon.png) | 128 px site icon, scaled from the 32 px favicon |
| [tools/build_tokens.py](tools/build_tokens.py) | Checks tokens against the readings |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## How the values were read

Computed styles were read on the live homepage and the product page with `getComputedStyle` and `getBoundingClientRect`. `:root` custom properties came from the theme stylesheets. Screenshots are the 1440 by 900 viewport at device pixel ratio 2, so each PNG is 2880 by 1800. The visual viewport width was 1430 because a scrollbar took 10px.

## What to distrust

The favicon is 32 px, scaled to 128 px with nearest neighbour, so the icon edges are the site's own pixels, repeated. Font files were not downloaded. Inter was the painted family. `--bs-body-font-family` is Arial and was not what the body used. `--bs-cta` is `#609e3e` and was not the photographed Add to bag button. Shipping country on this pass was Singapore, so prices are in S$.

## Fonts

Inter is the painted family, weights 300, 400, and 500. The page lists sans-serif after it. The files are the shop's, and they are not in this package. The style guide falls back to Helvetica.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | `#ffffff`, ink `#000000` |
| Brand | Captured | Wordmark image, 157 by 17 |
| Type | Captured, files absent | Inter on body and nav |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured | [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| FAQ | Captured | [screenshots/faq-light-1440.png](screenshots/faq-light-1440.png) |
| Button | Captured, default | Add to bag is 44px, `#303030`, radius `0px`, uppercase |
| Link | Captured | Header departments and footer columns |
| Text field | Not submitted | Search and newsletter were not opened or filled |
| Login wall | Not captured | Account points at `/en/account/dashboard`. Sign in is `/en/login`. The walk stopped there |
| Newsletter | Stopped | Subscribe was not clicked |
| Checkout | Not captured | Bag was not opened. Add to bag was not clicked |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light |

## Do and don't

- **Keep the page white and the announcement purple.** The page is `#ffffff`. The promo bar is `#3f1da0`, 24px, white type. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use a square charcoal add-to-bag button.** Add to bag is 44px, `#303030`, radius `0px`, uppercase, 12px. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Set department nav in Inter, 12px, uppercase.** Padding is `12px 10px`. The row is 40px. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Stop before account, bag, and checkout.** Those controls were mapped and not opened. [site-tree.md](site-tree.md)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, ink, announcement, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
