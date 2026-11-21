# Patagonia

Patagonia is a public outdoor clothing store. This package is a signed-out capture of [https://www.patagonia.com/home/](https://www.patagonia.com/home/) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, one public product, and the empty login and signup walls were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px crop of the wordmark on white |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured homepage tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Black utility bar, black add-to-bag, type, and radii |
| [style-guide.html](style-guide.html) | Swatches and the search control |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Header, product, login wall, signup wall |
| [components/](components/) | Empty crops folder. No element crops were taken |
| [icons/](icons/) | Wordmark path copied from the live header symbol, plus INDEX.tsv |
| [screenshots/](screenshots/) | Homepage, one product, login wall, signup wall |
| [raw/](raw/) | Computed styles read on the homepage, the product, and the walls |
| [site-tree.md](site-tree.md) | Header, footer, and the pages those controls open |
| [login-review.json](login-review.json) | What the login and signup walls ask for |
| [tools/](tools/) | A check that the header and add-to-bag tokens match the readings |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

An incognito preview opened https://www.patagonia.com/home/ at 1440 by 900, `devicePixelRatio` 2. `getComputedStyle` was read on the body, the utility bar, a department link, the search button, the homepage h1, the product h1, the Add to Bag button, and the login email field and Log in button. Add to Bag was not clicked. Search was not submitted. Log in and Create Account were not clicked.

## What to distrust

This is the signed-out US store. Do not treat the live hero or a product price as stable chrome.

The wordmark in [icons/mark.svg](icons/mark.svg) is the path data from the live `#icon--logo` symbol. It is not a separate brand file.

Header black and the add-to-bag black are exact computed values. The page fill is sampled: the body style was transparent, the header was white, and the photographed pages are white outside the hero.

Phone width was not captured. Hover and focus were not measured. Menus were read from the homepage DOM and were not each opened.

A service worker on this browser first painted a maintenance page for product URLs. The product shot is the live page after that cache was cleared. Color swatches on that page were still loading when the shot was taken.

## Fonts

Ridgeway Sans is the UI face, with system-ui, Segoe UI, Roboto, Helvetica Neue, and Arial. These files are not in this package. The style guide falls back to Arial.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Colour, header | Captured | Utility bar `#000000`, header `#ffffff` |
| Colour, accent | Captured | Add to Bag `#000000` |
| Colour, muted | Captured | Search label `#4a4a4a` |
| Colour, status | Not captured | Not shown as a named status role |
| Type, body | Captured | Department link 16px Ridgeway Sans |
| Type, display | Captured | Homepage h1 64px Ridgeway Sans |
| Spacing scale | Not captured | No named scale was read |
| Radius | Captured | Search 40px, pills 30px |
| Elevation | Not captured | Not measured |
| Motion | Not captured | No duration was read |
| Button | Captured | Add to Bag, hero chips, login Log in, signup Create Account |
| Button hover, focus, pressed | Not captured | Not measured |
| Link | Captured | Department links, on the homepage shot |
| Text field | Captured, empty | Search, footer email, login, and signup |
| Menu | Captured, in the DOM | Department, Activism, and Stories menus |
| Card | Captured | Product page and homepage tiles |
| Login wall | Captured, empty | [screenshots/login-light-1440.png](screenshots/login-light-1440.png) |
| Signup wall | Captured, empty | [screenshots/signup-light-1440.png](screenshots/signup-light-1440.png) |
| Checkout | Not captured | The cart was not opened |
| Subscribe | Not captured | Footer email Sign Me Up was not submitted |
| Phone width | Not captured | Desktop only |

## Do and don't

- **Keep the utility bar black and the wordmark on white.** The bar is `#000000` with 12px white type. The wordmark sits on the white header. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Leave the walls empty.** Login asks for email and password. Signup asks for name, email, and password, and shows a reCAPTCHA. Neither form was submitted. [screenshots/login-light-1440.png](screenshots/login-light-1440.png)
- **Use black pills for the primary action.** Add to Bag, Log in, and Create Account are black, white type, 30px radius. Search is a gray pill. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)

## Rebuild

```bash
python3 systems/patagonia/tools/build_tokens.py
```
