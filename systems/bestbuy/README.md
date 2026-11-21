# Best Buy

Best Buy is a public electronics store. This package is a signed-out capture of [https://www.bestbuy.com/](https://www.bestbuy.com/) on 2026-11-22. The first page is a country picker. United States was opened. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, one public product, and the empty login and signup walls were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px crop of the wordmark from the login header, on the header blue |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured homepage tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Header blue, tag yellow, text, cart yellow, type, and radii |
| [style-guide.html](style-guide.html) | Swatches and the search control |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Header, product, login wall, signup wall |
| [components/](components/) | Empty crops folder. No element crops were taken |
| [icons/](icons/) | Header wordmark paths copied from the live SVG, plus INDEX.tsv |
| [screenshots/](screenshots/) | Homepage, one product, login wall, signup wall |
| [raw/](raw/) | Computed styles read on the homepage and the walls |
| [site-tree.md](site-tree.md) | Header, footer, and the pages those controls open |
| [login-review.json](login-review.json) | What the login and signup walls ask for |
| [tools/](tools/) | A check that the header token matches the reading |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

An incognito preview opened https://www.bestbuy.com/ at 1440 by 900, `devicePixelRatio` 2. United States was chosen on the country picker. `getComputedStyle` was read on the body, the homepage h2, the search field, the header bars, Ask Blue, the login Continue button, the login field, and the product Add to cart button. Add to cart was not clicked. Search was not submitted.

## What to distrust

This is the signed-out US store, not a signed-in account and not the Canada store. Do not treat the live hero or a product price as stable chrome.

The wordmark in [icons/mark.svg](icons/mark.svg) is the path data from the live header SVG. It is not a separate brand file. The homepage did not publish an apple-touch icon link.

Header blue and the tag yellow are exact computed values. The login page fill in the screenshot is a hair off the white body style, so that wall color is labeled sampled.

Phone width was not captured. Deals, Support & Services, and Discover did not open a new list in this session. Hover and focus were not measured.

## Fonts

Human BBY Digital is the UI face, with Human Fallback, then Arial. These files are not in this package. The style guide falls back to Arial.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Colour, header | Captured | Header bar `#0046be` |
| Colour, tag | Captured | Wordmark tag `#fff200` |
| Colour, cart | Captured | Add to cart `#ffe200` |
| Colour, status | Not captured | Not shown as a named status role |
| Type, body | Captured | Body 13px Human BBY Digital |
| Type, display | Captured | Homepage h2 68px, weight 700 |
| Spacing scale | Not captured | No named scale was read |
| Radius | Captured | Search 8px, Ask Blue pill, login field 4px |
| Elevation | Not captured | Not measured |
| Motion | Not captured | No duration was read |
| Button | Captured | Ask Blue, Shop now, Add to cart |
| Button hover, focus, pressed | Not captured | Not measured |
| Link | Captured | Utility links, on the homepage shot |
| Text field | Captured, empty | Search, and the login and signup walls |
| Checkbox | Observed | Use for Account Recovery, signup wall. Not toggled |
| Menu | Captured, open | Shop categories. Deals, Support, and Discover did not open |
| Card | Captured | Product page and homepage deal tiles |
| Login wall | Captured, empty | [screenshots/login-light-1440.png](screenshots/login-light-1440.png) |
| Signup wall | Captured, empty | [screenshots/signup-light-1440.png](screenshots/signup-light-1440.png) |
| Checkout | Not captured | Cart was not opened |
| Subscribe | Not captured | Footer email Sign Up was not submitted |
| Phone width | Not captured | Desktop only |

## Do and don't

- **Keep the header blue and the tag yellow.** The wordmark tag is `#fff200` on `#0046be`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Leave identity providers alone.** Passkey, Apple, and Google sit under the login form and were not used. [screenshots/login-light-1440.png](screenshots/login-light-1440.png)
- **Stop at the empty walls.** Login asks for a phone or email first. Signup asks for name, email, password, and a mobile number, all left empty. [screenshots/signup-light-1440.png](screenshots/signup-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the header and tag tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
