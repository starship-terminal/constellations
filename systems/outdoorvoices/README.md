# Outdoor Voices

Outdoor Voices is a public activewear store. This package is a signed-out capture of [https://www.outdoorvoices.com/](https://www.outdoorvoices.com/) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, one public product, and the empty login wall were photographed. Signup is the same wall. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px crop of the wordmark on white |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured homepage tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Page, ink, promo blue, pill button, sale badge, type, and radii |
| [style-guide.html](style-guide.html) | Swatches, the pill button, and the empty email field |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Header, product, login wall |
| [components/](components/) | Empty crops folder. No element crops were taken |
| [icons/](icons/) | A partial wordmark path from the live header symbol, plus INDEX.tsv |
| [screenshots/](screenshots/) | Homepage, one product, login wall, and the same frame as the signup wall |
| [raw/](raw/) | Computed styles read on the homepage, the product, and the wall |
| [site-tree.md](site-tree.md) | Header, footer, and the pages those controls open |
| [login-review.json](login-review.json) | What the login wall asks for |
| [tools/](tools/) | A check that the written tokens match the readings |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

An incognito preview opened https://www.outdoorvoices.com/ at 1440 by 900, `devicePixelRatio` 2. `getComputedStyle` was read on the promo bar, the department link, the Shop button, the homepage heading, the product title, the sale badge, Add to Bag, the footer email, and the login wall. Add to Bag was not clicked. Search was not submitted. Account opened the wall and then stopped. Continue with Shop was not clicked.

## What to distrust

This is the signed-out store. Do not treat the live hero, a product price, or the promo slide as stable chrome. The photographed promo is the shipping slide on `#2b54ab`. The other slide is "Enjoy 30% off sitewide." and uses the same bar.

The product column is black in the PNG. Computed styles on the title ancestors came back transparent, so the panel color is sampled, not a custom property. The title ink computed to `#202020` and sits on that black panel, so the painted title is lighter than the computed value. Trust the PNG for the panel and the computed style for the token name.

The wordmark path in [icons/mark.svg](icons/mark.svg) is a fragment of the live header symbol, not a separate brand file. The visible wordmark is the screenshot crop in [icon.png](icon.png).

`--color-blue` computed to `#2B54AB`. The homepage PNG top row sampled `#3553a5`. The token uses the computed value.

Phone width was not captured. Hover and focus were not measured. Menus were read from the homepage DOM and were not each opened.

The login URL carries OAuth state. That query is not copied into this package. The screenshot is the painted wall, with an empty email field and no account name.

## Fonts

TTCommonsPro is the UI face. NordiquePro is the display face. The login wall uses GTStandard-M on Continue with Shop and a system stack on the heading. These files are not in this package. The style guide falls back to Arial.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Colour, header | Captured | Header `#ffffff`, promo `#2b54ab` |
| Colour, accent | Captured | Pill button `#202020`, sale badge `#6c2932` |
| Colour, muted | Captured | `--color-dark-grey` `#737373` |
| Colour, status | Not captured | `--color-error` was read and not shown as a painted state |
| Type, body | Captured | Nav and promo 16px TTCommonsPro |
| Type, display | Captured | Homepage heading 60px NordiquePro |
| Spacing scale | Not captured | No named scale was read |
| Radius | Captured | Pill 100px, footer field 4px, login field 12px |
| Elevation | Not captured | Not measured |
| Motion | Not captured | No duration was read |
| Button | Captured | Shop — Women, Add to Bag (not clicked), Sign Up Now (not clicked) |
| Button hover, focus, pressed | Not captured | Not measured |
| Link | Captured | Department links, on the homepage shot |
| Text field | Captured, empty | Login email and footer subscribe field |
| Menu | Captured, in the DOM | Women and Men menus |
| Card | Captured | Product page and homepage tiles |
| Login wall | Captured, empty | [screenshots/login-light-1440.png](screenshots/login-light-1440.png) |
| Signup wall | Captured, same wall | [screenshots/signup-light-1440.png](screenshots/signup-light-1440.png) |
| Checkout | Not captured | The cart button was not opened |
| Subscribe | Not captured | Footer Sign Up Now was not submitted |
| Phone width | Not captured | Desktop only |

## Do and don't

- **Keep the wordmark black on a white header.** The promo bar is the only blue chrome. Department links are 16px TTCommonsPro. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Leave the wall empty.** Login and signup share one email field. Continue with Shop is on the wall and was not clicked. [screenshots/login-light-1440.png](screenshots/login-light-1440.png)
- **Use a black pill for the primary action.** Shop — Women, Add to Bag, and Sign Up Now are `#202020`, white type, 100px radius, 47px tall. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)

## Rebuild

```bash
python3 systems/outdoorvoices/tools/build_tokens.py
```
