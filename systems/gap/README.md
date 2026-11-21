# Gap

Gap is a public clothing store. This package is a signed-out capture of [https://www.gap.com/](https://www.gap.com/) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, one public product, and the empty login wall were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px crop of the dark wordmark on white |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured homepage tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Black bars, navy add-to-bag, type, and radii |
| [style-guide.html](style-guide.html) | Swatches and the search control |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Header, product, login wall |
| [components/](components/) | Empty crops folder. No element crops were taken |
| [icons/](icons/) | Wordmark path copied from the live dark SVG, plus INDEX.tsv |
| [screenshots/](screenshots/) | Homepage, one product, login wall |
| [raw/](raw/) | Computed styles read on the homepage, the product, and the wall |
| [site-tree.md](site-tree.md) | Header, footer, and the pages those controls open |
| [login-review.json](login-review.json) | What the login wall asks for |
| [tools/](tools/) | A check that the header and add-to-bag tokens match the readings |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

An incognito preview opened https://www.gap.com/ at 1440 by 900, `devicePixelRatio` 2. `getComputedStyle` was read on the body, the universal bar, a department link, the search field, the homepage h2, the product h1, the Add to Bag button, and the login email field and Continue button. Add to Bag was not clicked. Search was not submitted. Continue was not clicked.

## What to distrust

This is the signed-out US store, not a signed-in account and not Gap Factory, Old Navy, Banana Republic, or Athleta. Do not treat the live hero or a product price as stable chrome.

The wordmark in [icons/mark.svg](icons/mark.svg) is the path data from the live dark SVG. It is not a separate brand file.

Header black and the add-to-bag navy are exact computed values. The page fill is sampled: the body style was transparent and the photographed pages are white.

Phone width was not captured. Hover and focus were not measured. Menus other than Women were read from the homepage DOM and were not each opened.

## Fonts

Gap Sans is the UI face, with Helvetica, Arial, and Roboto. The login wall uses Lato. These files are not in this package. The style guide falls back to Arial.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Colour, header | Captured | Universal bar `#000000` |
| Colour, accent | Captured | Add to Bag `#031ba1` |
| Colour, muted | Captured | Struck price `#757575` |
| Colour, status | Not captured | Not shown as a named status role |
| Type, body | Captured | Department link 16px Gap Sans v1 |
| Type, display | Captured | Homepage h2 32px Gap Sans |
| Spacing scale | Not captured | No named scale was read |
| Radius | Captured | Store controls 0px, login field 4px |
| Elevation | Not captured | Not measured |
| Motion | Not captured | No duration was read |
| Button | Captured | Add to Bag, hero chips, login Continue |
| Button hover, focus, pressed | Not captured | Not measured |
| Link | Captured | Department links, on the homepage shot |
| Text field | Captured, empty | Search, footer email, and the login wall |
| Menu | Captured, in the DOM | Department menus. Women was hovered open |
| Card | Captured | Product page and homepage arrival tiles |
| Login wall | Captured, empty | [screenshots/login-light-1440.png](screenshots/login-light-1440.png) |
| Signup wall | Not present as its own page | Join uses the same email wall. Continue was not clicked |
| Checkout | Not captured | The bag was not opened |
| Subscribe | Not captured | Footer email Sign up was not submitted |
| Phone width | Not captured | Desktop only |

## Do and don't

- **Keep the bars black and the wordmark on the photo.** The universal bar is `#000000` with white type. The wordmark sits on the hero. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Leave the email wall empty.** Sign in and join share one email field. Continue was not clicked. [screenshots/login-light-1440.png](screenshots/login-light-1440.png)
- **Stop before the bag.** Add to Bag is navy `#031ba1` and was not clicked. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the header and add-to-bag tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
