# Monos

Monos is a public luggage shop. This package is a signed-out capture of the United States shop at [https://monos.com](https://monos.com) on 2026-11-22. The body class was `shop-us` and prices were in USD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the luggage collection, the Carry-On product, and Our Story were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px mark from the public favicon |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Ink, page, promo, footer, type, and the Add to cart button |
| [style-guide.html](style-guide.html) | Swatches, the header row, a buy box, and the hero button |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Header, homepage, collection, product, story |
| [components/](components/) | Empty crops folder. No element crops were taken |
| [icons/](icons/) | Wordmark paths from the live header SVG, and INDEX.tsv |
| [screenshots/](screenshots/) | Homepage, luggage collection, Carry-On, Our Story |
| [raw/](raw/) | Computed styles read on the homepage, the collection, the product, and Our Story |
| [site-tree.md](site-tree.md) | Header, footer, and the pages those controls open |
| [tools/](tools/) | A check that the written tokens match the readings |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

An incognito preview opened https://monos.com. The first paint was the United States shop (`shop-us`, USD). `getComputedStyle` was read on the body, the promo bar, the header, a nav link, the hero title, the outline button, the product title, the price, Add to cart, a colour swatch, the collection intro, the story title, the footer, and Sign up. Add to cart was not clicked. Search was not submitted. Account was not opened. Sign up was not submitted. Store locations were not opened. The country control was left on United States.

A later preview screenshot failed because the desktop tab stopped producing frames. The committed PNGs were taken in headless Chromium at the same 1440 by 900 CSS viewport and `devicePixelRatio` 2, then quantized to 256-colour sRGB. Colours in the tokens come from the computed styles, not from the quantized PNGs.

## What to distrust

This is the signed-out United States shop. Do not treat the live hero, a product price, or the promo line as stable chrome.

`header.site-header` reports a transparent background. The painted header on the luggage page is white. The token uses the painted colour.

On the homepage hero the logo and nav paint white. On interior pages they paint `#4d4d4d`. Both are measured. The wordmark file uses the interior fill.

Cabin, Vollkorn, and Vollkorn SC are the computed faces. No font file is in this package. The style guide names those families and falls back when they are not installed.

[icon.png](icon.png) is the public favicon, resized from 32 px to 128 px, not a screenshot crop of the header. [icons/mark.svg](icons/mark.svg) is the path from the live header symbol.

Phone width was not captured. Hover and focus were not measured. Menus other than Luggage were read from the homepage DOM. The footer was not photographed, because it holds the email field.

The product page prints a Shop financing line. That line is a payment offer. It is not a token.

## Fonts

Cabin is the computed UI face (500 and 700). Vollkorn is the body and intro face (400). Vollkorn SC is the eyebrow (600). The files are not in this package. The style guide uses those family names, then the system sans and serif.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| Colour, header | Captured | Painted white on interior pages. Transparent over the homepage hero. |
| Colour, promo | Captured | `#4d4d4d` bar, white label |
| Colour, accent | Captured | Add to cart `#4d4d4d` on white |
| Colour, muted | Captured | Footer `#b3b3b3` |
| Colour, status | Not captured | No error state was shown |
| Type, body | Captured | 14px Vollkorn |
| Type, title | Captured | Product heading 36px Cabin 700 |
| Type, hero | Captured | 63px Cabin, letter-spacing 15px |
| Spacing scale | Partial | Promo 30, header 70, logo 120 by 50, button 48. No named scale. |
| Radius | Captured | Buttons are square. Swatches are circles. The code chip is 2px. |
| Elevation | Not captured | Header shadow is none. Not measured elsewhere. |
| Motion | Not captured | No duration was read |
| Button | Captured | Add to cart (not clicked), outline Use code and Learn more |
| Button hover, focus, pressed | Not captured | Not measured |
| Link | Captured | Department links, on the homepage shot |
| Text field | Present, empty | Header search and newsletter email. Not submitted. |
| Menu | Captured, in the DOM | Luggage opened by hover. Bags, Wallets, Sunglasses, Accessories, About us read from the DOM. |
| Card | Captured | Luggage tiles and homepage product names |
| Story | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Login wall | Not captured | Account was not opened |
| Signup wall | Not captured | Account was not opened. Footer Sign up was not submitted. |
| Checkout | Not captured | Cart was not opened. Add to cart was not clicked. |
| Subscribe | Not captured | Footer Sign up was not submitted |
| Phone width | Not captured | Desktop only |

## Do and don't

1. **Do keep the promo bar gray and the interior header white.** The bar is 30px `#4d4d4d`. The header under it is white with `#4d4d4d` type. See [category-light-1440.png](screenshots/category-light-1440.png).
2. **Do set department labels in uppercase Cabin, 12.32px, weight 700.** Letter-spacing is 2.464px. See [home-light-1440.png](screenshots/home-light-1440.png).
3. **Do make Add to cart a square `#4d4d4d` bar.** White uppercase Cabin 14px, 48px tall. See [product-light-1440.png](screenshots/product-light-1440.png).
4. **Do set product titles in Cabin 36px, weight 700.** Prices sit beside the title at 24px. Colour choices are 24px circles. See the product shot.
5. **Don't photograph the footer with the email field filled.** Sign up was not submitted. The footer links are listed in [site-tree.md](site-tree.md).
6. **Don't open account, cart, gift cards, or the store locator for this package.** Those stops are in [site-tree.md](site-tree.md).

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks [tokens.json](tokens.json) against [raw/readings.json](raw/readings.json) for the recorded colours, the hero and title sizes, the nav size, and the Add to cart height. It does not rewrite either file. `make design-md` was not run, because this pass does not edit catalog.json.
