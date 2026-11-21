# Vestiaire Collective

Vestiaire Collective is a public second-hand fashion shop. This package is a signed-out capture of [https://www.vestiairecollective.com](https://www.vestiairecollective.com) on 2026-11-22. The live host redirected to [https://us.vestiairecollective.com/](https://us.vestiairecollective.com/). Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, Women, and About us were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px public icon, resized from the live 192 px android-chrome icon |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Ink, page, promo, sale, type, header, and Sell an item |
| [style-guide.html](style-guide.html) | Swatches, the header row, and a size row |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Header, homepage, category, About |
| [components/](components/) | Empty crops folder. No element crops were taken |
| [screenshots/](screenshots/) | Homepage, Women, About us |
| [raw/](raw/) | Computed styles read on the homepage, Women, About, and one product |
| [site-tree.md](site-tree.md) | Header, footer, and the pages those controls open |
| [tools/](tools/) | A check that the written tokens match the readings |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

An incognito preview opened https://www.vestiairecollective.com. It redirected to https://us.vestiairecollective.com/. `getComputedStyle` was read on the body, the header, a nav link, Sale, Search, Sell an item, Sign in, the promo, the hero, a section title, a brand, a price, a menu heading, a menu link, the Women title, a filter chip, a sale price, a badge, the About title, the footer label, a footer link, and Add to Bag. Sell an item was not clicked. Sign in and Sign up were not clicked. The bag was not opened. Add to Bag and Make an Offer were not clicked. Search was not submitted.

A shopping-preference dialog opened on its own. Continue was not clicked. The dialog was hidden so the page could be photographed. A cookie bar was dismissed with Continue without accepting. Neither action typed or submitted a form.

The homepage, Women, and About were photographed in that same preview at 1440 by 900 CSS pixels, `devicePixelRatio` 2. PNG files are 2880 by 1800.

## What to distrust

This is the signed-out shop. Do not treat a product price, a sale price, or the currency as stable chrome. Prices on these pages were shown in SGD. The footer locale was not changed.

The product page prints a seller username in the first screen. It was measured and not photographed. The seller name and the product URL are not stored in this package.

HelveticaNowText and Albra-Regular are the computed faces. No font file is in this package. The style guide uses Georgia for titles and Helvetica for the shop.

[icon.png](icon.png) is the public android-chrome icon, resized from 192 px to 128 px. It is not a crop of the header wordmark.

Phone width was not captured. Hover and focus were not measured. Men, Designers, and the journal index were not opened.

## Fonts

HelveticaNowText is the shop face (400, 500, and 700). Albra-Regular is the title face (400). The files are not in this package.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Colour, promo | Captured | `#d31e1e` bar, white type |
| Colour, sale | Captured | `#db2124` Sale nav and sale price |
| Colour, header | Captured | White, ink `#1e1e1e` |
| Colour, hairline | Captured | Sampled `#ececec` |
| Colour, sell | Captured | `#000000` fill, white label. Not clicked |
| Colour, footer | Captured | Black block, grey links |
| Colour, status | Not captured | No error state was shown |
| Type, body | Captured | 16px HelveticaNowText 400 |
| Type, nav | Captured | 15px weight 400 |
| Type, title | Captured | Albra-Regular, 32 to 64px |
| Spacing scale | Partial | Header 132, search 45, sell 36, chip 44, Add to Bag 48. No named scale. |
| Radius | Captured | Search 33px, sell 2px, hero button 24px, chip 0 |
| Elevation | Not captured | No shadow was read |
| Motion | Not captured | No duration was read |
| Button | Captured | Sell an item and Press boilerplate. Neither clicked |
| Button hover, focus, pressed | Not captured | Not measured |
| Link | Captured | Nav, menu, footer, breadcrumb |
| Text field | Not present | Search is a button. Not opened |
| Menu | Captured | Women menu opened |
| Card | Captured | Homepage rail and Women grid |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Login wall | Not captured | Sign in was not opened |
| Signup wall | Not captured | Sign up was not opened |
| Sell wall | Not captured | Sell an item was not opened |
| Checkout | Not captured | The bag, Add to Bag, and Make an Offer were not clicked |
| Product page | Measured, not photographed | The first screen prints a seller username |
| Dark theme | Not present | The shop did not offer one |
| Phone width | Not captured | Desktop only |
