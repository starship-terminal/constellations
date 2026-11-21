# Rhone

Rhone is a public apparel store. This package is a signed-out capture of [https://www.rhone.com/](https://www.rhone.com/) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the men's collection, one product, and the about page were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px stitch mark from the public favicon, on the page color |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Ink, page, courtesy, line, olive, type, and the two buttons |
| [style-guide.html](style-guide.html) | Swatches, the square buttons, and a size chip |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Header, collection, product, about |
| [components/](components/) | Empty crops folder. No element crops were taken |
| [icons/](icons/) | Wordmark paths from the live header SVG, the favicon stitch, and INDEX.tsv |
| [screenshots/](screenshots/) | Homepage, men's collection, one product, about |
| [raw/](raw/) | Computed styles read on the homepage, the product, and about |
| [site-tree.md](site-tree.md) | Header, footer, and the pages those controls open |
| [tools/](tools/) | A check that the written tokens match the readings |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

An incognito preview opened https://www.rhone.com/ at 1440 by 900, `devicePixelRatio` 2. `getComputedStyle` was read on the body, the shipping bar, the courtesy bar, the header, the hero heading, Shop men's, a product title, Add to bag, a size chip, and the about heading. Add to bag was not clicked. Search was not submitted. Account was not opened. Subscribe was not submitted.

The first homepage paint was the Singapore storefront. Opening the product switched the same host to the United States storefront. Both are public pages of rhone.com. Prices on the two shots are in different currencies for that reason.

## What to distrust

This is the signed-out store. Do not treat the live hero, a product price, or the shipping slide as stable chrome. The homepage shipping line is the Singapore copy. The product and about shots show the United States copy on the same bar.

Denim is the UI face and was loaded. Reckless was loaded and is used on quotes. Neither file is in this package. The style guide falls back to Arial and Georgia.

The wordmark in [icons/wordmark.svg](icons/wordmark.svg) is the five paths from the live header SVG, fill `#1c1519`. [icon.png](icon.png) is the favicon stitch, rasterized and padded, not a screenshot crop of the header.

Phone width was not captured. Hover and focus were not measured. Menus were read from the homepage DOM. New and Women were not opened. The footer was not photographed, because it contains a phone link.

The product page names a model's height further down the page. The screenshot is the top viewport, which does not include that line.

## Fonts

Denim is the UI face (400 and 500). Reckless is the quote face (400). These files are not in this package. The style guide falls back to Arial for Denim and Georgia for Reckless.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Colour, header | Captured | Page `#fbf9f9`, courtesy `#efedea`, shipping `#1c1519` |
| Colour, accent | Captured | Add to bag `#1c1519` on `#fbf9f9` |
| Colour, muted | Captured | Olive `#617259` on "Bundle & save" |
| Colour, status | Not captured | No error state was shown |
| Type, body | Captured | 16px Denim |
| Type, display | Captured | Homepage heading 56px Denim |
| Spacing scale | Partial | Shipping 30, courtesy 32, nav row 68. No named scale. |
| Radius | Captured | Buttons, chips, and search are 0 |
| Elevation | Not captured | Not measured |
| Motion | Not captured | No duration was read |
| Button | Captured | Shop men's, Add to bag (not clicked) |
| Button hover, focus, pressed | Not captured | Not measured |
| Link | Captured | Department links, on the homepage shot |
| Text field | Captured, empty | Header search. Not submitted. |
| Menu | Captured, in the DOM | New, Men, Women |
| Card | Captured | Collection grid and homepage tiles |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Login wall | Not captured | Account was not opened |
| Signup wall | Not captured | Take 15% off and Subscribe were not opened |
| Checkout | Not captured | Cart was not opened. Add to bag was not clicked. |
| Subscribe | Not captured | Footer Subscribe was not submitted |
| Phone width | Not captured | Desktop only |

## Do and don't

- **Keep the header square and quiet.** Page `#fbf9f9`, courtesy `#efedea`, ink `#1c1519`, no radius on buttons. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use ink for the primary action and the page color for the hero action.** Add to bag is `#1c1519` with `#fbf9f9` type. Shop men's is the reverse, 57px, 0 radius. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Leave account, cart, and subscribe closed.** Those controls are in the tree and were not opened. [site-tree.md](site-tree.md)

## Rebuild

```bash
python3 systems/rhone/tools/build_tokens.py
```
