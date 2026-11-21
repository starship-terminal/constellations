# Kith

Kith is a public clothing and lifestyle shop. This package is a signed-out capture of [https://kith.com](https://kith.com) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, Kith Winter 2026, one product, and About were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px mark from the public favicon |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Ink, page, footer, buy column, type, and Select a size |
| [style-guide.html](style-guide.html) | Swatches, the header row, and a buy box |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Header, collection, product, About |
| [components/](components/) | Empty crops folder. No element crops were taken |
| [icons/](icons/) | Logo path from the live header SVG, and INDEX.tsv |
| [screenshots/](screenshots/) | Homepage, Winter 2026, one product, About |
| [raw/](raw/) | Computed styles read on the homepage, the collection, the product, and About |
| [site-tree.md](site-tree.md) | Header, footer, and the pages those controls open |
| [tools/](tools/) | A check that the written tokens match the readings |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

An incognito preview opened https://kith.com. `getComputedStyle` was read on the body, the header, a nav button, the hero heading, Shop now, a price, the footer, the product title, a size chip, and Select a size. Select a size was not clicked. Search was not submitted. Account was not opened. Subscribe was not submitted. The welcome dialog was closed with Shop kith.com. A later newsletter popup was closed without typing.

The homepage, the collection, and About were also photographed in headless Chromium at the same 1440 by 900 CSS viewport, `devicePixelRatio` 2. Direct product URLs in that headless browser stopped on a connection check. The product photograph is from the incognito preview, which loaded the product page. PNG files are 2880 by 1800.

## What to distrust

This is the signed-out shop. Do not treat the live hero, a product price, or the currency as stable chrome. Prices on these pages were shown in SGD. The currency picker was not submitted.

The homepage header is transparent over the hero, so its computed color is white. Interior pages paint the same header `#ffffff` with `#333333` labels. The token uses the interior paint.

The product buy column paints `#000000`. `getComputedStyle` on `.product__information` still reports `#333333` and a transparent background. The title, price, and size labels in the photograph are light on that black. The token records the painted column, and the readings file records both.

Proxima Nova is the computed UI face. Georgia is the computed display face. No font file is in this package. The style guide uses Proxima Nova, then Helvetica, and Georgia for titles.

The mark in [icons/mark.svg](icons/mark.svg) is the path from the live header symbol, fill `#333333`. [icon.png](icon.png) is the public favicon, resized from 32 px to 128 px, not a screenshot crop of the header.

Phone width was not captured. Hover and focus were not measured. Menus other than Mens were read from the homepage DOM. The footer was not photographed, because it holds the newsletter field.

## Fonts

Proxima Nova is the computed UI face (300 and 500). Georgia is the computed display face (400). The files are not in this package.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Colour, header | Captured | Interior `#ffffff`, labels `#333333`. Homepage is white on the hero. |
| Colour, footer | Captured | `#f2f2f2`, computed. Not photographed. |
| Colour, buy column | Captured | Painted `#000000` on [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Colour, muted | Captured | Select a size `#828282` |
| Colour, status | Not captured | No error state was shown |
| Type, body | Captured | 12px Proxima Nova 300 |
| Type, title | Captured | Product and collection heading 18px Georgia 400 |
| Type, display | Captured | Hero and About 28px Georgia 400 |
| Spacing scale | Partial | Header 66, logo 54 by 23, button 41, size chip 79 by 41. No named scale. |
| Radius | Captured | Buttons and size chips are 0 |
| Elevation | Not captured | Header shadow is none. Not measured elsewhere. |
| Motion | Not captured | No duration was read |
| Button | Captured | Shop now, Select a size (not clicked) |
| Button hover, focus, pressed | Not captured | Not measured |
| Link | Captured | Department buttons and footer links, in the DOM |
| Text field | Present, empty | Search and newsletter email. Not submitted. |
| Menu | Captured | Mens drawer opened. Other departments read from the DOM. |
| Card | Captured | Homepage rail and Winter 2026 grid |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Login wall | Not captured | Account was not opened |
| Signup wall | Not captured | Loyalty Program was not opened |
| Checkout | Not captured | Cart was not opened. Select a size was not clicked. |
| Subscribe | Not captured | Footer Submit was not clicked |
| Phone width | Not captured | Desktop only |

## Do and don't

1. **Do keep interior headers white, 66px, with tracked uppercase nav.** Labels are 12px, weight 500, letter-spacing 3px, `#333333`. See [category-light-1440.png](screenshots/category-light-1440.png).
2. **Do let the homepage header sit on the hero.** There the same labels are white. See [home-light-1440.png](screenshots/home-light-1440.png).
3. **Do set display titles in Georgia.** The hero and About are 28px. Product and collection titles are 18px. See [about-light-1440.png](screenshots/about-light-1440.png).
4. **Do paint the buy column black, with square size chips and a gray Select a size.** Size chips are 79 by 41 with a `#d9d9d9` border. Select a size is `#828282`, 41px, radius 0. See [product-light-1440.png](screenshots/product-light-1440.png).
5. **Don't photograph the footer with the newsletter field filled.** Submit was not clicked. The footer links are listed in [site-tree.md](site-tree.md).
6. **Don't open account, cart, locations, or hospitality for this package.** Those stops are in [site-tree.md](site-tree.md).

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks [tokens.json](tokens.json) against [raw/readings.json](raw/readings.json). It does not rewrite either file. `make design-md` was not run, because this pass does not edit catalog.json.
