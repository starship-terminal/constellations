# Free People

Free People is a public clothing shop. This package is a signed-out capture of [https://www.freepeople.com](https://www.freepeople.com) on 2026-11-22. The country chip read SG ($). Product prices on the opened pages were USD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the Clothes menu, the clothes landing, one product, and Our Story were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px mark from the public apple touch icon |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Page, promo, ink, pink, type, and the bar heights |
| [style-guide.html](style-guide.html) | Swatches, the nav row, and the pink Add to Bag bar |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Homepage, menu, collection, product, about |
| [components/](components/) | Empty crops folder. No element crops were taken |
| [icons/](icons/) | Wordmark paths from the live header SVG, and INDEX.tsv |
| [screenshots/](screenshots/) | Homepage, Clothes menu, clothes landing, one product, Our Story |
| [raw/](raw/) | Computed styles and custom properties read on the live pages |
| [site-tree.md](site-tree.md) | Header, footer, and the pages those controls open |
| [tools/](tools/) | A check that the written tokens match the readings |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

An incognito preview opened https://www.freepeople.com at 1440 by 900, `devicePixelRatio` 2. `getComputedStyle` was read on the body, the promo bar, a nav link, GIFTS, SALE, the search field, the product title, the product price, and Add to Bag. Custom properties were read from the stylesheets on `:root`. Add to Bag was not clicked. Search was not submitted. Account was not opened. Subscribe was not submitted. The promo banner was paused for the homepage photograph.

## What to distrust

The country chip says SG ($). The product page still showed $58.00. Do not treat the live hero, a product price, or the promo line as stable chrome. The promo bar rotates between shipping copy and a text-signup line.

Karla is the computed face. The file is not in this package. The style guide falls back to Helvetica, then Arial.

The wordmark in [icons/wordmark.svg](icons/wordmark.svg) is the public header SVG, fill `#2D2D2D`. [icon.png](icon.png) is the 512 px apple touch icon, resized to 128 px, not a screenshot crop of the header.

Phone width was not captured. Hover and focus were not measured as states. Menus other than Clothes were read from the homepage DOM after a mouseenter. The footer was not photographed, because it holds the email signup.

## Fonts

Karla is the computed UI face (400, and 700 on the promo). `--font-heading` is Karla, then Georgia. The file is not in this package.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Colour, header | Captured | Page `#FEFBFA`, 60px nav row |
| Colour, promo | Captured | Painted `#EDE6E0` bar, 44px |
| Colour, accent | Captured | Add to Bag and GIFTS and SALE `#D52975` on white |
| Colour, sale | Captured | SALE label uses the same pink |
| Colour, muted | Captured | `--stone` `#998F8A` |
| Colour, status | Not captured | `--error` is declared. No error state was shown |
| Type, body | Captured | 12px Karla on the nav |
| Type, title | Captured | Product and category headings 18px Karla |
| Spacing scale | Partial | Promo 44, nav 60, button 45, content gutter 60. No named scale. |
| Radius | Captured | Add to Bag, nav, and search are 0 |
| Elevation | Partial | Header shadow is none. `--popover-shadow` is declared |
| Motion | Not captured | Promo rotates. It was paused, not filmed |
| Button | Captured | Add to Bag (not clicked) |
| Button hover, focus, pressed | Not captured | Not measured |
| Link | Captured | Department links, on the homepage shot |
| Text field | Present, empty | Header search and footer email. Not submitted |
| Menu | Captured | Clothes panel. Other menus read from the DOM |
| Card | Captured | Clothes grid |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Login wall | Not captured | Account was not opened |
| Signup wall | Not captured | Account was not opened |
| Checkout | Not captured | Cart was not opened. Add to Bag was not clicked |
| Subscribe | Not captured | Footer email and text signup were not submitted |
