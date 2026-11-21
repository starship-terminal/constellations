# Etsy

Etsy is a public marketplace. This package is a signed-out capture of [https://www.etsy.com/](https://www.etsy.com/) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, one public listing, and the empty login and signup walls were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px nearest-neighbor scale of the published apple-touch icon |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured homepage tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Page, text, accent, type, and the search radius |
| [style-guide.html](style-guide.html) | Swatches and the search control |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Header, listing, login wall, signup wall |
| [components/](components/) | Empty crops folder. No element crops were taken |
| [icons/](icons/) | A color wordmark drawn in Georgia, plus INDEX.tsv |
| [screenshots/](screenshots/) | Homepage, one listing, login wall, signup wall |
| [raw/](raw/) | Computed styles read on the homepage and the walls |
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

An incognito preview opened https://www.etsy.com/ at 1440 by 900, `devicePixelRatio` 2. The first response was the Singapore locale. United States was opened from the locale list so the shots use US English and USD. `getComputedStyle` was read on the body, the homepage h1, the search field, the search button's orange `::after`, the Sign in control, and the empty login and signup fields. The Search button was not clicked.

## What to distrust

This is the signed-out marketplace, not a signed-in account. Do not treat the live hero or a listing price as stable chrome.

The wordmark in [icons/mark.svg](icons/mark.svg) is a reconstruction in Georgia. It is not the ABCDiatype logo file. The published apple-touch file was 57 px, not 180 px.

The search button's own background is transparent. The orange circle is the `::after` fill `#f1641e`.

Phone width was not captured. The Categories menu was not opened. Hover and focus were not measured.

## Fonts

ABCDiatype is the UI face. ABCOtto is the display face. These files are not in this package. The style guide falls back to Arial and Georgia.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Colour, accent | Captured | Search circle `#f1641e` |
| Colour, status | Not captured | Not shown as a named status role |
| Type, body | Captured | Body 14px ABCDiatype |
| Type, display | Captured | Homepage h1 40px ABCOtto |
| Spacing scale | Not captured | No named scale was read |
| Radius | Captured | Search and Sign in 24px, field 8px |
| Elevation | Not captured | Search button box-shadow none |
| Motion | Not captured | No duration was read |
| Button | Captured | Search, on the homepage shot |
| Button hover, focus, pressed | Not captured | Not measured |
| Link | Captured | Promo strip, on the homepage shot |
| Text field | Captured, empty | Login and signup walls |
| Checkbox | Captured, checked | Stay signed in, not toggled |
| Select | Observed, closed | Listing options and quantity |
| Menu | Not captured | Categories was not opened |
| Card | Captured | Listing and homepage hero |
| Login wall | Captured, empty | [screenshots/login-light-1440.png](screenshots/login-light-1440.png) |
| Signup wall | Captured, empty | [screenshots/signup-light-1440.png](screenshots/signup-light-1440.png) |
| Checkout | Not captured | Cart was not opened |
| Phone width | Not captured | Desktop only |

## Do and don't

- **Keep the search circle orange.** The header's only filled accent is the search control. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Leave identity providers alone.** Google, Facebook, and Apple sit under the form and were not used. [screenshots/login-light-1440.png](screenshots/login-light-1440.png)
- **Stop at the empty walls.** Login asks for email first and keeps Sign in disabled while empty. Signup asks for email, first name, and password. [screenshots/signup-light-1440.png](screenshots/signup-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the accent token against [raw/readings.json](raw/readings.json). It does not recapture the site.
