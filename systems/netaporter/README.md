# NET-A-PORTER

NET-A-PORTER is a public luxury fashion shop. This package is a signed-out capture of [https://www.net-a-porter.com/en-us/](https://www.net-a-porter.com/en-us/) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, Clothing, one product, and About Us were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px ribbon from the public favicon, on white |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Ink, page, muted, type, and the 2px button |
| [style-guide.html](style-guide.html) | Swatches, the white Shop now, and Add to Bag |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Header, listing, product, about |
| [components/](components/) | Empty crops folder. No element crops were taken |
| [icons/](icons/) | Wordmark SVG from the public header, and INDEX.tsv |
| [screenshots/](screenshots/) | Homepage, Clothing, one product, About Us |
| [raw/](raw/) | Computed styles read on the homepage, the listing, and the product |
| [site-tree.md](site-tree.md) | Header, footer, and the pages those controls open |
| [tools/](tools/) | A check that the written tokens match the readings |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

An incognito preview opened https://www.net-a-porter.com/en-us/ at 1440 by 900, `devicePixelRatio` 2. `getComputedStyle` was read on the service ribbon, the header, a department link, Shop now, the hero title, the New In heading, the Clothing heading, a listing designer and price, the product brand, Add to Bag, a size chip, and the footer heading. Add to Bag was not clicked. Search was not submitted. Account was not opened. Sign Up was not submitted.

A first-order promo was closed with its Close control on the clothing page. A shipping-location prompt was closed with its Close control. Change Location was not clicked. A chat button was hidden in the page so it would not cover the shots.

## What to distrust

This is the signed-out US store. Do not treat the live hero, a product price, or the ribbon line as stable chrome.

AkkuratPro is the UI face and was loaded. Chronicle Display and ChronicleText were loaded and are used on headings and product names. None of the files are in this package. The style guide falls back to Arial and Georgia.

The wordmark in [icons/wordmark.svg](icons/wordmark.svg) is the public header SVG, fill white. [icon.png](icon.png) is the favicon ribbon, resized to 128 px on white, not a screenshot crop of the header.

Phone width was not captured. Hover and focus were not measured. Department menus were read from the homepage DOM and were not hovered open. The footer was not photographed, because it contains a Sign Up form.

Size chips computed as black type on a transparent face with a `#e5e5e5` border. On the black product panel those labels did not paint in the first frame. The saved product shot forces the chip type to white so the labels can be read. That override is not a token.

About body copy computed as `#111111`. In the photograph the lower half of the page reads as dark type on a dark ground. Trust the computed color for the token, and the screenshot for the layout.

## Fonts

AkkuratPro is the UI face (400, and 700 on designer names and prices). Chronicle Display is the display face (400 and 500). ChronicleText is the serif face (400 and 500). These files are not in this package. The style guide falls back to Arial for AkkuratPro and Georgia for Chronicle Display.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Colour, header | Captured | Header `#111111`, ribbon `#cbcbcb`, nav `#ffffff` |
| Colour, accent | Captured | Add to Bag `#111111` on `#ffffff` |
| Colour, muted | Captured | Product name `#656565` |
| Colour, status | Not captured | No error state was shown. Low stock is 12px muted type, not a status colour. |
| Type, body | Captured | 16px ChronicleText on the hero, 14px AkkuratPro on nav |
| Type, display | Captured | New In 48px Chronicle Display 500 |
| Spacing scale | Partial | Ribbon 32, header 106, button 40. No named scale. |
| Radius | Captured | Buttons, chips, and the email field are 2px |
| Elevation | Not captured | No shadow was measured on a control |
| Motion | Not captured | No duration was read |
| Button | Captured | Shop now, Add to Bag (not clicked) |
| Button hover, focus, pressed | Not captured | Not measured |
| Link | Captured | Department links, on the homepage shot |
| Text field | Not captured | Header search is a button. The footer email field was not photographed. |
| Menu | Captured, in the DOM | New In through Editorial. Not hovered open. |
| Card | Captured | Clothing grid |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Login wall | Not captured | Account was not opened |
| Signup wall | Not captured | Sign Up was not submitted |
| Checkout | Not captured | Checkout was not opened. Add to Bag was not clicked. |
| Subscribe | Not captured | Footer Sign Up was not submitted |
| Phone width | Not captured | Desktop only |

## Do and don't

- **Keep the header ink and the ribbon grey.** Header `#111111`, wordmark white, ribbon `#cbcbcb` with `#111111` type. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use a 2px radius on the primary action.** Shop now is white on the hero. Add to Bag is `#111111` with white type, 40px. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Leave account, checkout, and Sign Up closed.** Those controls are in the tree and were not opened. [site-tree.md](site-tree.md)

## Rebuild

```bash
python3 systems/netaporter/tools/build_tokens.py
```
