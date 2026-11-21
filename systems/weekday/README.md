# Weekday

Weekday is a public women's and men's clothing shop. This package is a signed-out capture of [https://www.weekday.com](https://www.weekday.com) on 2026-11-22. The live storefront is the worldwide English shop at `/en-ww/`, with shipping set to Singapore. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the women mega-menu, women's clothing, one product, and About us were photographed. Nothing was typed, submitted, or signed in.

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` was not flipped. DESIGN.md in this folder is a hand copy, because `make design-md` needs a catalog entry.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px crop of the public apple-touch icon, a white W on `#1d1d1b` |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured tokens |
| [tokens.json](tokens.json) | Ink, page, promo, sale, type, header, and buttons |
| [style-guide.html](style-guide.html) | Swatches, the header row, and a button row |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Header, homepage, category, product, About |
| [components/](components/) | Empty crops folder. No element crops were taken |
| [screenshots/](screenshots/) | Homepage, women mega-menu, women's clothing, one product, About us |
| [raw/](raw/) | Computed styles read on the live shop |
| [site-tree.md](site-tree.md) | Header, footer, and the pages those controls open |
| [tools/](tools/) | A check that the written tokens match the readings |
| [login-review.json](login-review.json) | Empty walls, and where the walk stopped |

## How the values were read

An incognito preview opened https://www.weekday.com. The first hit was an Akamai Access Denied page. A reload landed on the live shop at `/en-ww/`. `getComputedStyle` was read on the body, the promo bar, the header, WOMEN, LOGIN, search, the homepage title, the hero titles, the sale link, JOIN NOW, the shipping confirm button, Add to cart, the product title, the About title, and the footer. Add to cart was not clicked. JOIN NOW was not submitted. LOGIN was not opened. Search was not submitted.

Only required cookies was clicked. YES, DELIVER TO SINGAPORE was clicked, confirming the region this pass landed on. A newsletter popup was closed with Escape. None of those clicks typed or submitted a form.

The homepage, the women mega-menu, women's clothing, one product, and About us were photographed in that same preview at 1440 by 900 CSS pixels, `devicePixelRatio` 2. PNG files are 2880 by 1800.

## What to distrust

This is the signed-out worldwide shop with shipping set to Singapore. Do not treat the live item count, a product price, the promo copy, or the countdown as stable chrome. Women's clothing read 1900 items. The photographed product was 74.99 USD.

The promo bar computed as `rgb(255, 255, 3)`. The 2x screenshot of the same bar samples near `#ffff55`. The token keeps the computed value.

The About h1 is 74px black type over a black hero band, so ABOUT US does not show in the screenshot. The readable proof is the subnav and the THIS IS WEEKDAY block under the band.

weekdayRegularFont, weekdaySemiBoldFont, and weekdayMonoFont are the computed faces. No font file is in this package. The style guide uses Arial Narrow, then Arial.

Phone width was not captured. Hover and focus were not measured. The men mega-menu was read from the DOM and not photographed. Store locator and Find in store were not opened.

## Fonts

weekdayRegularFont is the body face. weekdaySemiBoldFont is the homepage title, the hero titles, and the About title. weekdayMonoFont is the promo bar. The files are preloaded from `/_next/static/media/` and are not in this package. Computed weight on the measured styles is 400.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json) |
| Colour, promo | Captured | Computed `#ffff03`. Screenshot samples `#ffff55` |
| Colour, sale | Captured | `#d1443b` on UP TO 50% OFF |
| Colour, header | Captured | White, 56px, no hairline |
| Colour, button | Captured | `#1d1d1b` fill, white label. Add to cart not clicked |
| Colour, status | Not captured | No error state was shown |
| Type, body | Captured | 18px weekdayRegularFont 400 |
| Type, nav | Captured | 16px, height 56 |
| Type, home | Captured | 34px weekdaySemiBoldFont |
| Spacing scale | Partial | Promo 58, header 56, button 40. No named scale. |
| Radius | Captured | 0px on measured controls |
| Elevation | Not captured | Header has no shadow |
| Motion | Not captured | No duration was read |
| Button | Captured | Primary fill and JOIN NOW outline. Neither submitted a form |
| Button hover, focus, pressed | Not captured | Not measured |
| Link | Captured | Nav, mega-menu, footer |
| Text field | Present, empty | Search and the newsletter fields. Not submitted. |
| Menu | Captured | Women mega-menu opened |
| Card | Captured | Homepage hero and women's clothing grid |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Login wall | Not opened | LOGIN was not clicked |
| Signup wall | Not opened | Create account sits inside login |
| Checkout | Not captured | Add to cart, cart, and size select were not clicked |

## Do and don't

Do use the measured colours, the 0px radius, and the three Weekday faces. Don't treat the Singapore shipping choice, the USD prices, or the winter promo as the brand's only storefront. Don't follow login, cart, checkout, or newsletter submit from this package.

## Rebuild

```sh
python3 systems/weekday/tools/build_tokens.py
```
