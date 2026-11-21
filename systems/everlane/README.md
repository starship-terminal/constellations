# Everlane

Everlane is a public clothing store. This package is a signed-out capture of [https://www.everlane.com/](https://www.everlane.com/) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, one public product, and the empty login wall were photographed. Signup is the same wall. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px crop of the wordmark on white |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured homepage tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Page, ink, sale red, button black, type, and square radius |
| [style-guide.html](style-guide.html) | Swatches, the sale label, and the empty email field |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Header, product, login wall |
| [components/](components/) | Empty crops folder. No element crops were taken |
| [icons/](icons/) | Wordmark path copied from the live header symbol, plus INDEX.tsv |
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

An incognito preview opened https://www.everlane.com/ at 1440 by 900, `devicePixelRatio` 2. `getComputedStyle` was read on the body, the announcement section, a department link, the SALE link, the homepage hero paragraph, the product title, the style pills, Sold Out, and the login email field. Sold Out was not clicked. Search was not submitted. Account opened the wall and then stopped. Continue with Shop was not clicked.

## What to distrust

This is the signed-out store. Do not treat the live hero, a product price, or the announcement slide as stable chrome. The homepage PNG shows the cashmere slide on `#12344b`. The product PNG shows the shipping slide on `#c8c0b8`. Both were read. The token uses the computed section color.

The wordmark in [icons/mark.svg](icons/mark.svg) is the path data from the live header symbol. It is not a separate brand file.

Shopify theme variables name Assistant as the body face. The visible chrome computed to Maison Neue Book. Trust the computed face.

Phone width was not captured. Hover and focus were not measured. Menus were read from the homepage DOM and were not each opened. The product was sold out, so Add to Bag was not on the page.

The login URL carries OAuth state. That query is not copied into this package. The screenshot is the painted wall, with an empty email field and no account name.

## Fonts

Maison Neue Book is the UI face. Maison Neue is the hero face. The login heading computed to a hashed family name, Howu5pMg. These files are not in this package. The style guide falls back to Arial.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Colour, header | Captured | Header `#ffffff`, announcement `#c8c0b8` and photographed slide `#12344b` |
| Colour, accent | Captured | Sale `#d0021b`, button `#262626` |
| Colour, muted | Captured | Breadcrumb `#737373` |
| Colour, status | Not captured | Not shown as a named status role |
| Type, body | Captured | Department link 12px Maison Neue Book, body 16px |
| Type, display | Captured | Hero eyebrow 20px Maison Neue |
| Spacing scale | Not captured | No named scale was read |
| Radius | Captured | Controls 0px |
| Elevation | Not captured | Not measured |
| Motion | Not captured | No duration was read |
| Button | Captured | Sold Out, style pills, Continue with Shop (not clicked) |
| Button hover, focus, pressed | Not captured | Not measured |
| Link | Captured | Department links, on the homepage shot |
| Text field | Captured, empty | Login email and footer subscribe field |
| Menu | Captured, in the DOM | Department menus |
| Card | Captured | Product page and homepage tiles |
| Login wall | Captured, empty | [screenshots/login-light-1440.png](screenshots/login-light-1440.png) |
| Signup wall | Captured, same wall | [screenshots/signup-light-1440.png](screenshots/signup-light-1440.png) |
| Checkout | Not captured | The bag drawer was not opened |
| Subscribe | Not captured | Footer email Subscribe was not submitted |
| Phone width | Not captured | Desktop only |

## Do and don't

- **Keep the wordmark black on a white header.** The department row is 12px, tracked 0.24px. Sale is the red label. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Leave the wall empty.** Login and signup share one email field. Continue with Shop is on the wall and was not clicked. [screenshots/login-light-1440.png](screenshots/login-light-1440.png)
- **Use a square black bar for the primary product action.** Sold Out is `#262626`, white type, 0 radius. The selected style pill matches. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)

## Rebuild

```bash
python3 systems/everlane/tools/build_tokens.py
```
