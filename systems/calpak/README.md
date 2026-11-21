# CALPAK

CALPAK is a public luggage and bag shop. This package is a signed-out capture of [https://www.calpaktravel.com](https://www.calpaktravel.com) on 2026-11-22. Global-e had set the storefront to Singapore and SGD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the Bags menu, the bags collection, one product, and About were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px mark from the public favicon |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Ink, page, yellow, promo, type, and the pill radius |
| [style-guide.html](style-guide.html) | Swatches, the header row, and a yellow pill |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Homepage, menu, collection, product, about |
| [components/](components/) | Empty crops folder. No element crops were taken |
| [icons/](icons/) | Wordmark paths from the live header SVG, and INDEX.tsv |
| [screenshots/](screenshots/) | Homepage, Bags menu, bags collection, one product, About |
| [raw/](raw/) | Computed styles and custom properties read on the homepage |
| [site-tree.md](site-tree.md) | Header, footer, and the pages those controls open |
| [tools/](tools/) | A check that the written tokens match the readings |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

An incognito preview opened https://www.calpaktravel.com. `getComputedStyle` was read on the body, the promo bar, the header sheet, a nav link, the hero heading, the hero pill, the collection title, the product title, and Add to Bag. Custom properties were read resolved from `:root`. Add to Bag was not clicked. Search was not submitted. Account was not opened. Subscribe was not submitted. The Klaviyo email dialog was closed. The cookie banner was rejected.

## What to distrust

This is the signed-out Singapore store. Prices are SGD. Do not treat the live hero, a product price, or the promo line as stable chrome.

The promo bar paints `rgb(248, 240, 95)`. `--color-yellow` is `#F8F15F`, and Add to Bag paints `rgb(248, 241, 95)`. The tokens keep both.

The promo bar's computed font is Roboto. The rest of the UI is Futura PT. Futura PT is not in this package. The style guide falls back to Futura, then Trebuchet MS.

The wordmark in [icons/mark.svg](icons/mark.svg) is the path from the live header SVG, fill `#030303`. [icon.png](icon.png) is the favicon, resized from 32 px to 128 px, not a screenshot crop of the header.

Phone width was not captured. Hover and focus were not measured. Menus other than Bags were read from the homepage DOM. The footer was not photographed, because it holds the newsletter embed.

The homepage shot has the Klaviyo "Get Free Shipping" teaser painted out of the lower left with the page cream. The live page shows that teaser after the email dialog is closed. It is a subscribe wall, not chrome.

## Fonts

Futura PT is the computed UI face (500, and 600 was also loaded). Kyoto is the serif (`--font-serif`, 500 loaded). Neither file is in this package. The style guide uses Futura, then Trebuchet MS.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Colour, header | Captured | Page `#FFFDF3`, 53px sheet, 5px radius |
| Colour, promo | Captured | Painted `#F8F05F` bar |
| Colour, accent | Captured | Add to Bag and hero pill `#F8F15F` on `#030303` |
| Colour, sale | Captured | `--color-red` `#D21A28` |
| Colour, muted | Captured | `--color-gray` `#E5E7DF` |
| Colour, status | Not captured | No error state was shown |
| Type, body | Captured | 18px Futura PT 500 |
| Type, title | Captured | Product heading 28px, collection heading 48px |
| Spacing scale | Partial | Promo 38, nav 53, button 47, section 60. No named scale. |
| Radius | Captured | Pills are 9999px. Header sheet is 5px |
| Elevation | Not captured | Header shadow is none |
| Motion | Partial | `--transition-duration` is 0.3s, ease-in-out. Not filmed |
| Button | Captured | Hero pill and Add to Bag (not clicked) |
| Button hover, focus, pressed | Not captured | Not measured |
| Link | Captured | Department links, on the homepage shot |
| Text field | Present, empty | Header search and newsletter email. Not submitted |
| Menu | Captured | Bags panel. Other menus read from the DOM |
| Card | Captured | Bags grid |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Login wall | Not captured | Account was not opened |
| Signup wall | Not captured | Account was not opened |
| Checkout | Not captured | Bag was not opened. Add to Bag was not clicked |
| Subscribe | Not captured | Popup and footer Subscribe were not submitted |
| Phone width | Not captured | Desktop only |

## Do and don't

1. **Do keep the page cream and the ink near-black.** Body is `#FFFDF3` and `#030303`. See [home-light-1440.png](screenshots/home-light-1440.png).
2. **Do set department labels in Futura PT 16px, weight 500.** They sit in a cream sheet with a 5px radius. See the same shot.
3. **Do make Add to Bag a yellow pill.** The face is `#F8F15F`, the label is ink, the height is 47px. See [product-light-1440.png](screenshots/product-light-1440.png).
4. **Do set the collection title at 48px and the product title at 28px.** Both are Futura PT 500. See [category-light-1440.png](screenshots/category-light-1440.png).
5. **Don't photograph the footer with the newsletter field filled.** Subscribe was not submitted. The footer links are listed in [site-tree.md](site-tree.md).
6. **Don't open account, bag, or store locations for this package.** Those stops are in [site-tree.md](site-tree.md).

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks ink, page, and promo in [tokens.json](tokens.json) against [raw/readings.json](raw/readings.json). It does not check type sizes or the other colours, and it does not rewrite either file. `make design-md` was not run, because this pass does not edit catalog.json.
