# Old Navy

Old Navy is a public clothing store. This package is a signed-out capture of [https://oldnavy.gap.com/](https://oldnavy.gap.com/) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the Women category, one public product, Our Values, and the empty login wall were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px navy wordmark on white |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured homepage tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Navy bars, promo blue, type, and radii |
| [style-guide.html](style-guide.html) | Swatches and the search control |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Header, category, product, login wall |
| [components/](components/) | Empty crops folder. No element crops were taken |
| [icons/](icons/) | Wordmark redraw, plus INDEX.tsv |
| [screenshots/](screenshots/) | Homepage, Women category, one product, Our Values, login wall |
| [raw/](raw/) | Computed styles read on the homepage, the product, and the wall |
| [site-tree.md](site-tree.md) | Header, footer, and the pages those controls open |
| [login-review.json](login-review.json) | What the login wall asks for |
| [tools/](tools/) | A check that the navy and promo tokens match the readings |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

An incognito preview opened https://oldnavy.gap.com/ at 1440 by 900, `devicePixelRatio` 2. `getComputedStyle` was read on the body, the universal bar, a department link, the search field, Ask Navy, the product price, the Add to Bag button, the footer Sign Up button, and the login email field and Continue button. Add to Bag was not clicked. Search was not submitted. Sign Up was not clicked. Continue was not clicked.

## What to distrust

This is the signed-out US store, not a signed-in account and not Gap, Banana Republic, or Athleta. Do not treat the live hero or a product price as stable chrome.

The wordmark in [icons/mark.svg](icons/mark.svg) is a redraw of the live navy logo. It is not a separate brand file.

Navy `#05274c` and promo `#0b6ab3` are exact computed values. The page fill is sampled: the body style was transparent and the photographed pages are white.

Phone width was not captured. Hover and focus were not measured. Department menus other than Women were read from the homepage DOM and were not each opened.

## Fonts

ON Sans Text is the UI face. ON Sans Display is the body face. The login wall uses Lato. These files are not in this package. The style guide falls back to Arial.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Colour, header | Captured | Universal bar `#05274c` |
| Colour, promo | Captured | Promo strip `#0b6ab3` |
| Colour, accent | Captured | Add to Bag `#05274c` |
| Colour, deals | Captured | Today's Deals `#ff0000` |
| Colour, status | Not captured | Not shown as a named status role |
| Type, body | Captured | Body 16px ON Sans Display v1 |
| Type, nav | Captured | Department link 14.4px ON Sans Text v1 |
| Type, price | Captured | Product price 32px |
| Spacing scale | Not captured | No named scale was read |
| Radius | Captured | Search 24px, Sign Up 999px, login field 4px |
| Elevation | Not captured | Not measured |
| Motion | Not captured | No duration was read |
| Button | Captured | Add to Bag, Ask Navy, footer Sign Up, login Continue |
| Button hover, focus, pressed | Not captured | Not measured |
| Link | Captured | Department links, on the homepage shot |
| Text field | Captured, empty | Search, footer email, and the login wall |
| Menu | Captured, in the DOM | Department menus. Women was opened as a page |
| Card | Captured | Product page and the Women grid |
| Login wall | Captured, empty | [screenshots/login-light-1440.png](screenshots/login-light-1440.png) |
| Signup wall | Not present as its own page | Join uses the same email wall. Continue was not clicked |
| Checkout | Not captured | The bag was not opened. Add to Bag was not clicked |
| Subscribe | Not captured | Footer email Sign Up and Let's Text were not submitted |
| Phone width | Not captured | Desktop only |

## Do and don't

- **Keep the bars navy and the wordmark on white.** The universal bar is `#05274c`. The wordmark is the same navy. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Leave the email wall empty.** Sign in and join share one email field. Continue was not clicked. [screenshots/login-light-1440.png](screenshots/login-light-1440.png)
- **Stop before the bag.** Add to Bag is navy `#05274c` and was not clicked. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the navy and promo tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
