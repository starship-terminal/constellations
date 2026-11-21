# eBay

eBay is a public marketplace. This package is a signed-out capture of [https://www.ebay.com/](https://www.ebay.com/) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, one public listing, and the empty login and signup walls were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px site icon, nearest-neighbor scale of the published 60 px apple-touch icon |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured homepage tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Page, text, accent, type, and the search button radius |
| [style-guide.html](style-guide.html) | Swatches and the Search button |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Header, listing, login wall, signup wall |
| [components/](components/) | Empty crops folder. No element crops were taken |
| [icons/](icons/) | A color wordmark drawn in Arial, plus INDEX.tsv |
| [screenshots/](screenshots/) | Homepage, one listing, login wall, signup wall |
| [raw/](raw/) | Computed styles read on the homepage |
| [site-tree.md](site-tree.md) | Header, footer, and the pages those controls open |
| [login-review.json](login-review.json) | What the login and signup walls ask for |
| [tools/](tools/) | A check that the accent token matches the reading |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

An incognito preview opened https://www.ebay.com/ at 1440 by 900, `devicePixelRatio` 2. `getComputedStyle` was read on the body, the Search button, the Sign in link, and the search field. Custom properties were sampled from the stylesheets. The Search button was not clicked. Cookie banners were not present.

## What to distrust

This is the signed-out marketplace, not a signed-in account. Do not treat the live hero or a listing price as stable chrome.

The wordmark in [icons/mark.svg](icons/mark.svg) is a reconstruction in Arial. It is not the Market Sans logo file.

`--color-blue-500` matches the Search fill. The other sampled custom properties were not seen as live states.

Phone width was not captured. Menus were not opened. Hover and focus were not measured.

## Fonts

Market Sans is the UI face. The search field uses Helvetica Neue. These files are not in this package. The style guide falls back to Arial.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Colour, accent | Captured | Search fill `#0968f6` |
| Colour, status | Not captured | Not shown on the pages that were opened |
| Type, body | Captured | Body 14px Market Sans |
| Type, display | Not captured | Homepage h1 was visually hidden |
| Spacing scale | Not captured | No named scale was read |
| Radius | Captured | Search button 44px |
| Elevation | Not captured | Search button box-shadow none |
| Motion | Not captured | No duration was read |
| Button | Captured | Search, on the homepage shot |
| Button hover, focus, pressed | Not captured | Not measured |
| Link | Captured | Sign in, on the homepage shot |
| Text field | Captured, empty | Login and signup walls |
| Checkbox | Captured, checked | Stay signed in, not toggled |
| Select | Observed, closed | All Categories |
| Menu | Not captured | Expand buttons were not opened |
| Card | Captured | Listing and homepage hero |
| Login wall | Captured, empty | [screenshots/login-light-1440.png](screenshots/login-light-1440.png) |
| Signup wall | Captured, empty | [screenshots/signup-light-1440.png](screenshots/signup-light-1440.png) |
| Checkout | Not captured | Cart was not opened |
| Phone width | Not captured | Desktop only |

## Do and don't

- **Keep the search pill blue.** The Search control is the only filled accent on the header. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Leave identity providers alone.** Google, Apple, and Facebook sit under the form and were not used. [screenshots/login-light-1440.png](screenshots/login-light-1440.png)
- **Stop at the empty walls.** Login asks for email first. Signup asks for name, email, and password, and Create stays disabled while empty. [screenshots/signup-light-1440.png](screenshots/signup-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the accent token against [raw/readings.json](raw/readings.json). It does not recapture the site.
