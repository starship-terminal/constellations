# GOAT

GOAT is a public sneaker, apparel, and accessories shop. This package is a signed-out capture of [https://www.goat.com](https://www.goat.com) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, Sneakers, one product, and About Us were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px wordmark drawn to match the homepage header. The public favicon is a solid black square |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Ink, page, homepage, hairline, type, header, and Sign Up |
| [style-guide.html](style-guide.html) | Swatches, the header row, and a size row |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Header, homepage, category, product, About |
| [components/](components/) | Empty crops folder. No element crops were taken |
| [screenshots/](screenshots/) | Homepage, Sneakers, one product, About Us |
| [raw/](raw/) | Computed styles read on the homepage, Sneakers, the product, and About |
| [site-tree.md](site-tree.md) | Header, footer, and the pages those controls open |
| [tools/](tools/) | A check that the written tokens match the readings |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

An incognito preview opened https://www.goat.com. `getComputedStyle` was read on the body, the header, a nav link, Search, Account, a menu heading, a menu link, the shop menu panel, a section title, the Sneakers title, the product title, a price, Buy New, the About title, the footer, a footer label, and Sign Up. Buy New was not clicked. Make Offer was not clicked. Search was not submitted. Account was not opened. Sign Up was not clicked.

A login dialog opened on its own. Close (X) was clicked. A cookie bar was dismissed with Reject All. Neither click typed or submitted a form.

The homepage, Sneakers, the product, and About were photographed in that same preview at 1440 by 900 CSS pixels, `devicePixelRatio` 2. PNG files are 2880 by 1800. A headless Chromium pass of the same URLs stopped on a Cloudflare check, so those frames were discarded.

## What to distrust

This is the signed-out shop. Do not treat the live shop count, a product price, or the currency as stable chrome. The header read 841,015 items. Prices on these pages were shown in SGD. Location Preferences was not submitted.

The homepage paints the header and the page `#000000` with white type. Interior pages paint the same header `#ffffff` with `#000000` labels. Both are recorded.

GOATProductVariableVF is the computed face. No font file is in this package. The style guide uses Helvetica Neue, then Helvetica, then Arial.

The public favicon and apple-touch icon fetched from the live page are solid black squares. [icon.png](icon.png) is a 128 px wordmark on black, drawn in Helvetica to stand in for the header wordmark. It is not a crop of a logo file, because the header has no logo image.

Phone width was not captured. Hover and focus were not measured. Editorial, Timeline, and the shop index were not opened.

## Fonts

GOATProductVariableVF is the computed face (300, 400, 600, and 700). The file is not in this package.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| Colour, homepage | Captured | `#000000` page, white type. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Colour, header | Captured | Homepage black. Interior white. |
| Colour, hairline | Captured | Sampled `#515151` interior, `#aeaeae` homepage |
| Colour, signup | Captured | `#000000` fill, white label. Not clicked |
| Colour, status | Not captured | No error state was shown |
| Type, body | Captured | 11.5px GOATProductVariableVF 400 |
| Type, nav | Captured | 11.5px weight 300 |
| Type, category | Captured | 11.5px weight 700, uppercase |
| Spacing scale | Partial | Header 50, nav 38, menu 564 by 311, Sign Up 32, field 49. No named scale. |
| Radius | Captured | Sign Up and the email wrapper are 1px |
| Elevation | Captured | Shop menu shadow is none |
| Motion | Not captured | No duration was read |
| Button | Captured | Sign Up (not clicked). Buy New measured, not clicked |
| Button hover, focus, pressed | Not captured | Not measured |
| Link | Captured | Nav, menu, footer, and underlined category links |
| Text field | Present, empty | Newsletter email. Not submitted. |
| Menu | Captured | Shop menu opened |
| Card | Captured | Homepage rail and Sneakers grid |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Login wall | Seen, not photographed | A login dialog opened and was closed. Account was not opened |
| Signup wall | Not captured | Create Account and Sign Up were not opened |
| Checkout | Not captured | Buy New, Make Offer, and size select were not clicked |
| Subscribe | Not captured | Sign Up was not clicked |
| Phone width | Not captured | Desktop only |

## Do and don't

1. **Do keep the header at 50px, with Search at the left and Account at the right.** Nav is 11.5px, weight 300. See [category-light-1440.png](screenshots/category-light-1440.png).
2. **Do paint the homepage black.** The same header labels are white there. See [home-light-1440.png](screenshots/home-light-1440.png).
3. **Do keep type near 11.5px.** Category titles are weight 700. Product titles are weight 300. See [about-light-1440.png](screenshots/about-light-1440.png).
4. **Do put the size row and Buy New under the shoe, on white.** Buy New is a text button, not a filled bar. See [product-light-1440.png](screenshots/product-light-1440.png).
5. **Don't click Sign Up or type in the email field.** The field is empty in [about-light-1440.png](screenshots/about-light-1440.png).
6. **Don't open Account, Buy New, or Make Offer for this package.** Those stops are in [site-tree.md](site-tree.md).

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks [tokens.json](tokens.json) against [raw/readings.json](raw/readings.json). It does not rewrite either file. `make design-md` was not run, because this pass does not edit catalog.json.
