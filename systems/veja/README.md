# Veja

Veja is a public sneaker shop. This package is a signed-out capture of the United States storefront at [https://www.veja-store.com/en_us/](https://www.veja-store.com/en_us/) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the men's collection, one product, and the FAQ page were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px mark from the public apple-touch-icon |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Ink, page, promo, gift green, type, and the Add to cart button |
| [style-guide.html](style-guide.html) | Swatches, the header row, and a buy box |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Header, collection, product, FAQ |
| [components/](components/) | Empty crops folder. No element crops were taken |
| [icons/](icons/) | Logo paths from the live header SVG, and INDEX.tsv |
| [screenshots/](screenshots/) | Homepage, men's collection, one product, FAQ |
| [raw/](raw/) | Computed styles read on the homepage and the product |
| [site-tree.md](site-tree.md) | Header, footer, and the pages those controls open |
| [tools/](tools/) | A check that the written tokens match the readings |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

An incognito preview opened https://www.veja-store.com. The first paint was `/fr_fr/`. The shipping picker lists the United States. Opening https://www.veja-store.com/en_us/ switched the same host to the United States storefront (site id VEJA-USA). `getComputedStyle` was read on the body, the promo bar, the header, a nav link, the product title, the price, Add to cart, a size chip, and Filters. Add to cart was not clicked. Search was not submitted. Account was not opened. Subscribe was not submitted. The cookie banner was closed without accepting.

## What to distrust

This is the signed-out United States store. Do not treat the live hero, a product price, or the promo line as stable chrome.

The promo paragraph node reports `rgb(33, 37, 41)`. The painted label is white on `#4d4d4d`. The token uses the painted colour.

Helvetica is the computed UI face. No font file is in this package. The style guide uses Helvetica.

The mark in [icons/mark.svg](icons/mark.svg) is the path from the live header symbol, fill `#000000`. [icon.png](icon.png) is the apple-touch-icon, resized to 128 px, not a screenshot crop of the header.

Phone width was not captured. Hover and focus were not measured. Menus other than Men were read from the homepage DOM. The footer was not photographed, because it holds the newsletter field.

A repair mailto exists in the FAQ DOM. It is not in the photographed viewport and is not copied here.

## Fonts

Helvetica is the computed UI face (400 and 700). The file is not in this package. The style guide uses Helvetica, then the system sans.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Colour, header | Captured | Page `#ffffff`, 1px black border |
| Colour, promo | Captured | `#4d4d4d` bar, white label |
| Colour, accent | Captured | Add to cart `#000000` on `#ffffff` |
| Colour, gift | Captured | Gift card link `#065a21` |
| Colour, muted | Captured | Subscribe `#888888` |
| Colour, status | Not captured | No error state was shown |
| Type, body | Captured | 16px Helvetica |
| Type, title | Captured | Product heading 30px Helvetica 700 |
| Spacing scale | Partial | Promo 38, header 134, nav row 26, logo 65. No named scale. |
| Radius | Captured | Buttons and size chips are 5px |
| Elevation | Not captured | Header shadow is none. Not measured elsewhere. |
| Motion | Not captured | No duration was read |
| Button | Captured | Add to cart (not clicked), Filters |
| Button hover, focus, pressed | Not captured | Not measured |
| Link | Captured | Department links, on the homepage shot |
| Text field | Present, empty | Header search and newsletter email. Not submitted. |
| Menu | Captured, in the DOM | Women, Men, Kids, Running, Accessories, Vegan, Outlet |
| Card | Captured | Men's grid and homepage tiles |
| FAQ | Captured | [screenshots/faq-light-1440.png](screenshots/faq-light-1440.png) |
| Login wall | Not captured | Account was not opened |
| Signup wall | Not captured | Account was not opened |
| Checkout | Not captured | Cart was not opened. Add to cart was not clicked. |
| Subscribe | Not captured | Footer Subscribe was not submitted |
| Phone width | Not captured | Desktop only |

## Do and don't

1. **Do keep the header white with a 1px black rule.** The logo, departments, and icons sit on `#ffffff`. See [home-light-1440.png](screenshots/home-light-1440.png).
2. **Do set department labels in uppercase Helvetica 14px.** Gift card is the same size in `#065a21`. A second green is wrong. See the same shot.
3. **Do make Add to cart a black bar with a 5px radius.** Size chips use the same radius and a 1px black border. See [product-light-1440.png](screenshots/product-light-1440.png).
4. **Do set product titles in uppercase 30px Helvetica 700.** Prices sit under the title at 25px. See the product shot.
5. **Don't photograph the footer with the newsletter field filled.** Subscribe was not submitted. The footer links are listed in [site-tree.md](site-tree.md).
6. **Don't open account, cart, or the store locator for this package.** Those stops are in [site-tree.md](site-tree.md).

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks [tokens.json](tokens.json) against [raw/readings.json](raw/readings.json). It does not rewrite either file. `make design-md` was not run, because this pass does not edit catalog.json.
