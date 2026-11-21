# Uniqlo

Uniqlo is a public clothing store. This package is a signed-out capture of [https://www.uniqlo.com/sg/en/](https://www.uniqlo.com/sg/en/) on 2026-11-22. `https://www.uniqlo.com` redirected there. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, one public product, and the empty login and signup walls were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px crop of the header wordmark from the homepage shot |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Red, ink, page, text, search, and the login pill |
| [style-guide.html](style-guide.html) | Swatches and the search control |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Header, product, login wall, signup wall |
| [components/](components/) | Empty crops folder. No element crops were taken |
| [icons/](icons/) | Header wordmark paths copied from the live SVG, plus INDEX.tsv |
| [screenshots/](screenshots/) | Homepage, one product, login wall, signup wall |
| [raw/](raw/) | Computed styles read on the homepage, the product, and the walls |
| [site-tree.md](site-tree.md) | Header, footer, and the pages those controls open |
| [login-review.json](login-review.json) | What the login and signup walls ask for |
| [tools/](tools/) | A check that the red and ink tokens match the readings |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

An incognito preview opened https://www.uniqlo.com/ at 1440 by 900, `devicePixelRatio` 2. The store served Singapore English. `getComputedStyle` was read on the body, the header, the search button, the department tab, the promo strip, the sale price, the login fields, and the LOG IN and REGISTER ACCOUNT buttons. Search was not submitted. LOG IN and REGISTER ACCOUNT were not clicked.

## What to distrust

This is the signed-out Singapore store. Prices are in SGD. Do not treat the festival hero or a product price as stable chrome.

The product page computed text as black, and the sale label as `rgb(238, 0, 0)`. The preview canvas behind that page painted black until a white page background was set for the shot. The white page token comes from the create-account document, which reported `rgb(255, 255, 255)` on `html` and `body`.

The wordmark in [icons/mark.svg](icons/mark.svg) is the path data from the live header SVG. It is not a separate brand file.

Phone width was not captured. MEN, KIDS, and BABY were not opened. Hover and focus were not measured.

## Fonts

The body face is Segoe UI, Helvetica Neue, Helvetica, Arial, with Twemoji Country Flags first. These files are not in this package. The style guide falls back to Helvetica Neue.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Colour, brand red | Captured | Wordmark fill `red`, promo and sale `#ee0000` |
| Colour, ink button | Captured | LOG IN `#000000` |
| Colour, status | Not captured | Sale red is the only status colour that was read |
| Type, body | Captured | Body 16px |
| Type, display | Not captured | Homepage hero is an image, not a text style that was measured |
| Spacing scale | Not captured | No named scale was read |
| Radius | Captured | Search and LOG IN 999px, fields 0px |
| Elevation | Not captured | Not measured |
| Motion | Declared | `--animate-duration-standard` 300ms. Not timed |
| Button | Captured | LOG IN, REGISTER ACCOUNT, NOTIFY ME |
| Button hover, focus, pressed | Not captured | Not measured |
| Link | Captured | Department tabs and footer, on the homepage shot |
| Text field | Captured, empty | Search, and the login and signup walls |
| Radio | Observed | Gender on the signup wall. Not toggled |
| Checkbox | Observed | Newsletter and personalisation. Not toggled |
| Menu | Captured, open | Product categories. Listed in [site-tree.md](site-tree.md) |
| Card | Captured | Homepage category tiles and the product gallery |
| Login wall | Captured, empty | [screenshots/login-light-1440.png](screenshots/login-light-1440.png) |
| Signup wall | Captured, empty | [screenshots/signup-light-1440.png](screenshots/signup-light-1440.png) |
| Checkout | Not captured | Cart was not opened |
| Subscribe | Not captured | E-newsletter was not opened. The signup newsletter box was not ticked |
| Phone width | Not captured | Desktop only |

## Do and don't

- **Keep the wordmark red on white.** The header squares are `red`, and the promo strip is `#ee0000`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Make the buy and login actions a black pill.** LOG IN and REGISTER ACCOUNT are `#000000` at 52px with a 999px radius. [screenshots/login-light-1440.png](screenshots/login-light-1440.png)
- **Leave the walls empty.** Login asks for email and password. Signup asks for email, password, birthday, and gender. Nothing was typed. [screenshots/signup-light-1440.png](screenshots/signup-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the red, ink, and field tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
