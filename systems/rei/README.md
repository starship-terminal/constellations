# REI

REI is a public outdoor co-op shop. This package is a signed-out capture of [https://www.rei.com/](https://www.rei.com/) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage was photographed. A category page, a product page, and the about page were requested and stopped at a Press and Hold wall. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px PNG from the site apple-touch icon at `/icon-192x192.png` |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured homepage tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Charcoal utility bar, cream header, promo orange, type, and radius |
| [style-guide.html](style-guide.html) | Swatches, the search field, and the promo button |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Header, homepage tiles, and the walls that stopped the walk |
| [components/](components/) | Empty crops folder. No element crops were taken |
| [icons/](icons/) | Wordmark path copied from the live header SVG, plus INDEX.tsv |
| [screenshots/](screenshots/) | Homepage only. Later walls were discarded |
| [raw/](raw/) | Computed styles, and the header and footer link dumps |
| [site-tree.md](site-tree.md) | Header, footer, and the pages those controls open |
| [tools/](tools/) | A check that the promo, cream, and charcoal tokens match the readings |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

A preview opened https://www.rei.com/ at 1440 by 900, `devicePixelRatio` 2. `getComputedStyle` was read on the body, the utility bar (`.unav`), the cream bar (`.gnav`), a utility link, the Shop word, the search field, a category button, the promo bar, the Shop the sale link, a product title, a price, and the footer signup button. Search was not submitted. Sign in, Cart, and Sign me up were not clicked. Add to cart was not present on the homepage shot.

## What to distrust

This is the signed-out US shop on 2026-11-22. The holiday hero and the product prices on the homepage are campaign content.

The wordmark in [icons/mark.svg](icons/mark.svg) is the path data from the live `svg.logo__img`. It is not a separate brand file. [icon.png](icon.png) is the site's own `/icon-192x192.png`, resized to 128 px.

Header charcoal, cream, promo orange, and the search ring are exact computed values. The stylesheet also declares `--cdr-color-background-primary` as `#f4f2ed`, which matches the cream bar. A membership token, `#13352c`, is the fallback for `--cdr-color-text-primary` in a stylesheet rule. The homepage body text computed to black, so the tokens use the computed black.

Phone width was not captured. Hover and focus were not measured. Department menus were read from the homepage DOM and were not each opened.

A PerimeterX Press and Hold wall blocked every URL opened after the homepage, including a same-tab click and `location.assign`. Those pages are not in this package. A later scroll also raised that wall over the homepage. That frame was discarded.

## Fonts

Graphik is the UI face, with Helvetica Neue. Stuart is the display face, with Georgia. Both loaded in the page as variable fonts. These files are not in this package. The style guide falls back to Helvetica Neue and Georgia.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Colour, header | Captured | Utility bar `#292929`, main bar `#f4f2ed` |
| Colour, accent | Captured | Promo and Shop the sale `#c7370f` |
| Colour, muted | Captured | Category and price `#4b4a48` |
| Colour, link | Captured | Product title `#406eb5` |
| Colour, status | Not captured | Not shown as a named status role |
| Type, body | Captured | 16px Graphik |
| Type, display | Captured | Shop word 24px Stuart; section titles 32px Stuart |
| Spacing scale | Not captured | The page uses fluid `--cdr-space-scale-*` clamps. No fixed scale was copied |
| Radius | Captured | Search and buttons 4px |
| Elevation | Not captured | Search uses a 1px inset ring, not a shadow |
| Motion | Not captured | No duration was read |
| Button | Captured | Shop the sale, footer Sign me up (not clicked) |
| Button hover, focus, pressed | Not captured | Not measured |
| Link | Captured | Utility links, product title |
| Text field | Captured, empty | Search and footer email |
| Menu | Captured, in the DOM | Department menus in [site-tree.md](site-tree.md) |
| Card | Captured | Homepage product tile, title and price only |
| Product page | Not captured | Press and Hold wall, not solved |
| About page | Not captured | Press and Hold wall, not solved |
| Category page | Not captured | Press and Hold wall, not solved |
| Login wall | Not captured | Sign in was not followed |
| Checkout | Not captured | Cart was not opened |
| Subscribe | Not captured | Email signup was not submitted |
| Membership join | Not captured | Join was not started |
| Phone width | Not captured | Desktop only |

## Do and don't

- **Keep the utility bar charcoal and the wordmark on cream.** The bar is `#292929` with 14px near-white type. The mark and the word Shop sit on `#f4f2ed`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use the promo orange for the sale action.** Shop the sale and the promo strip are `#c7370f` with white type and a 4px radius. Search stays a light field with a sand ring.
- **Leave the walls empty.** Do not type into search, the footer email, or a subscribe dialog. Do not press through a Press and Hold wall. This capture stopped there.

## Rebuild

```bash
python3 systems/rei/tools/build_tokens.py
```
