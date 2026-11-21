# Birdies

Birdies is a public women's shoe store. This package is a signed-out capture of [https://birdies.com/](https://birdies.com/) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, New Arrivals, one product, and Our Story were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px stitch mark from the public favicon, on the page color |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Ink, page, warm, gold, type, and the square button |
| [style-guide.html](style-guide.html) | Swatches, the square button, Shop all, and a size chip |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Header, collection, product, about |
| [components/](components/) | Empty crops folder. No element crops were taken |
| [icons/](icons/) | Wordmark SVG from the public logo file, and INDEX.tsv |
| [screenshots/](screenshots/) | Homepage, New Arrivals, one product, Our Story |
| [raw/](raw/) | Computed styles read on the homepage, the collection, and the product |
| [site-tree.md](site-tree.md) | Header, footer, and the pages those controls open |
| [tools/](tools/) | A check that the written tokens match the readings |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

An incognito preview opened https://birdies.com/ at 1440 by 900, `devicePixelRatio` 2. `getComputedStyle` was read on the body, the announcement bar, the header, a department link, Shop all, the hero heading, Shop the crystal collection, the collection heading, the product title, the price, Add to bag, and a size chip. Add to bag was not clicked. Search was not submitted. Login was not opened. Subscribe was not submitted.

A signup popup was closed with its Close control before the homepage shot. A Join the Flock tab was hidden in the page so it would not cover that shot. Neither was used to enter an email.

## What to distrust

This is the signed-out store. Do not treat the live hero, a product price, or the announcement line as stable chrome.

Sofia Pro is the UI face and was loaded. Calluna was loaded and is used on headings. Nunito is the body face named in CSS. None of the files are in this package. The style guide falls back to Arial and Georgia.

The wordmark in [icons/wordmark.svg](icons/wordmark.svg) is the public header SVG, fill black. [icon.png](icon.png) is the favicon stitch, padded to 128 px on white, not a screenshot crop of the header.

Phone width was not captured. Hover and focus were not measured. Department menus were read from the homepage DOM and were not hovered open. The footer was not photographed, because it contains a subscribe form.

Add to bag's computed background was transparent while its label was white. The screenshot shows a filled black face. Use the screenshot for that fill.

## Fonts

Sofia Pro is the UI face (400 and 500, and 700 on the hero button). Calluna is the display face (400, and 500 on the collection heading). Nunito is the body face (400). These files are not in this package. The style guide falls back to Arial for Sofia Pro and Georgia for Calluna.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Colour, header | Captured | Page `#ffffff`, announcement `#000000`, Shop all `#f6f4f1` |
| Colour, accent | Captured | Hero button `#000000` on `#ffffff` |
| Colour, muted | Captured | Gold `#c9a66b` from `--home-gold` |
| Colour, status | Not captured | No error state was shown. Sale `#e32c2b` is a token only. |
| Type, body | Captured | 14px Nunito |
| Type, display | Captured | Homepage heading 50px calluna |
| Spacing scale | Partial | Announcement 44, header 88, hero button 50. No named scale. |
| Radius | Captured | Buttons, chips, and Shop all are 0. A material tab is a 50px pill. |
| Elevation | Not captured | Shadows exist as custom properties and were not measured on a control |
| Motion | Not captured | No duration was read |
| Button | Captured | Shop the crystal collection, Add to bag (not clicked) |
| Button hover, focus, pressed | Not captured | Not measured |
| Link | Captured | Department links, on the homepage shot |
| Text field | Not captured | Header search is a link. The footer email field was not photographed. |
| Menu | Captured, in the DOM | Boots, Loafers, Flats, Sneakers, Heels, Sandals |
| Card | Captured | Collection grid and homepage tiles |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Login wall | Not captured | Login was not opened |
| Signup wall | Not captured | Join the Flock and Subscribe were not submitted |
| Checkout | Not captured | Cart was not opened. Add to bag was not clicked. |
| Subscribe | Not captured | Footer Save 10% today was not submitted |
| Phone width | Not captured | Desktop only |

## Do and don't

- **Keep the header white and the announcement black.** Page `#ffffff`, ink `#000000`, announcement `#000000`, no radius on buttons. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use ink for the primary action.** Shop the crystal collection is `#000000` with `#ffffff` type, 50px, 0 radius. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Leave login, cart, and subscribe closed.** Those controls are in the tree and were not opened. [site-tree.md](site-tree.md)

## Rebuild

```bash
python3 systems/birdies/tools/build_tokens.py
```
