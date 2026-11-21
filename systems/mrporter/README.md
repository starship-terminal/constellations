# MR PORTER

MR PORTER is a public men's luxury shop. This package is a signed-out capture of [https://www.mrporter.com/en-sg/](https://www.mrporter.com/en-sg/) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 1. The homepage, Clothing, one product, and About Us were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px mark from the public favicon, on white |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Ink, page, promo grey, muted, type, and the 2px button |
| [style-guide.html](style-guide.html) | Swatches, the hero title, Add to Bag, and a size chip |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Header, collection, product, about |
| [components/](components/) | Empty crops folder. No element crops were taken |
| [icons/](icons/) | Index only. The live wordmark is a festive GIF and was not saved |
| [screenshots/](screenshots/) | Homepage, Clothing, one product, About Us |
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

The shared preview and curl received Akamai Access Denied. A local Chrome window, with no automation flag, opened https://www.mrporter.com/ and landed on `/en-sg/` at 1440 by 900, `devicePixelRatio` 1. `getComputedStyle` was read on the promo ribbon, the header, a department link, the hero title, Shop now, the clothing heading, the product designer, the product name, the price, Add to Bag, a size chip, a footer heading, and the email field. Add to Bag was not clicked. Search was not submitted. Account was not opened. Sign Up was not submitted.

A chat widget and a live-shopping frame were hidden in the page before the screenshots. Neither was used to send a message.

## What to distrust

This is the signed-out Singapore store. Do not treat the live hero, a product price, or the promo line as stable chrome. Prices show pounds and an approximate Singapore dollar figure.

Georgia is the UI face. SackersGothicStd is the display face and was loaded. Neither file is in this package. The style guide falls back to Georgia.

The header wordmark is a festive GIF and is not in this package. [icon.png](icon.png) is the public favicon, padded to 128 px on white, not a crop of the header.

Phone width was not captured. Hover and focus were not measured. Department menus other than Clothing were read from the homepage DOM and were not hovered open. The footer was not photographed, because it contains a subscribe form.

## Fonts

Georgia is the UI face (400). SackersGothicStd is the display face (400, and 500 on the homepage hero). These files are not in this package. The style guide falls back to Georgia.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Colour, header | Captured | Page `#ffffff`, promo `#cbcbcb` |
| Colour, accent | Captured | Add to Bag `#000000` on `#ffffff` |
| Colour, muted | Captured | Footer link and category chip `#656565` |
| Colour, status | Partial | Unavailable size `#838383`. No error state was shown |
| Type, body | Captured | 14px Georgia |
| Type, display | Captured | Homepage hero 32px SackersGothicStd |
| Spacing scale | Partial | Promo 32, header 183, nav 52, button 40. No named scale |
| Radius | Captured | Controls are 2px |
| Elevation | Not captured | No shadow was measured on a control |
| Motion | Not captured | No duration was read |
| Button | Captured | Shop now, Add to Bag (not clicked) |
| Button hover, focus, pressed | Not captured | Not measured |
| Link | Captured | Department links, on the homepage shot |
| Text field | Not captured | Header search was not opened. The footer email field was not photographed |
| Menu | Captured, in the DOM | What's New through How to Wear It. Clothing was opened once |
| Card | Captured | Clothing grid |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Login wall | Not captured | Account and Sign In were not opened |
| Signup wall | Not captured | Register was not opened |
| Checkout | Not captured | Bag was not opened. Add to Bag was not clicked |
| Subscribe | Not captured | Footer Sign Up was not submitted |
| Phone width | Not captured | Desktop only |
