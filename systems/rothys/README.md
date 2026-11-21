# Rothy's

Rothy's is a public shoe and bag store. This package is a signed-out capture of [https://rothys.com/](https://rothys.com/) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the women's shoe collection, one product, and the founder story were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px site mark, nearest-neighbor from the public 32 px favicon |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Midnight, page, roth, sale, line, sandstone, and the type roles |
| [style-guide.html](style-guide.html) | Swatches, the wordmark color, a struck price, and Select a size |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Header, collection, product, about |
| [components/](components/) | Empty crops folder. No element crops were taken |
| [icons/](icons/) | Wordmark paths from the live header SVG, and INDEX.tsv |
| [screenshots/](screenshots/) | Homepage, women's shoes, one product, about |
| [raw/](raw/) | Computed styles and the declared DNA custom properties |
| [site-tree.md](site-tree.md) | Header, footer, and the pages those controls open |
| [tools/](tools/) | A check that the written tokens match the readings |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

An incognito preview opened https://rothys.com/ at 1440 by 900, `devicePixelRatio` 2. `getComputedStyle` was read on the body, the announcement bar, the header, the department label, the collection heading, the product title, the sale price, and the compare price. CSS custom properties were read from `:root`. Select a size was not clicked. Add to bag was not clicked. Search was not submitted. Log in was not opened. Subscribe was not submitted.

The OneTrust banner was hidden with `display: none`. Accept cookies was not clicked.

## What to distrust

This is the signed-out store. Do not treat the live hero, a product price, or the announcement slide as stable chrome.

The hero sale line is painted into the photograph. It is not HTML text, so it has no computed style of its own. The announcement bar is the measured roth surface.

Maison Neue Book, Maison Neue Medium, and Grifo S Light were loaded. Canela was loaded and is named in the banner stylesheet. None of those files are in this package. The style guide falls back to Arial and Georgia.

The wordmark in [icons/wordmark.svg](icons/wordmark.svg) is the letter paths from the live header SVG, fill `#9A1B2C`. [icon.png](icon.png) is the public favicon, scaled from 32 to 128 with nearest neighbor, not a crop of the header.

Phone width was not captured. Hover and focus were not measured. Bags, Men, and Kids were read from the homepage DOM and were not opened. The footer was not photographed, because it contains the subscribe field.

`--dna-h1-font` declares 56px. The photographed titles are 40px. The token uses the measured 40px.

`--dna-border-radius-s` is 4px. The painted header, nav, and size control in this pass are 0. Both are recorded. The style guide uses 0.

The collection screenshot is scrolled so the product photos are in frame. A style-chip row sits under the header. The heading is above that frame.

## Fonts

Maison Neue Book is the UI face. Maison Neue Medium is the nav face. Grifo S Light is the title face. These files are not in this package. The style guide falls back to Arial and Georgia.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Colour, header | Captured | Page `#ffffff`, announcement `#9a1b2c`, rule `#dcdbdd` |
| Colour, accent | Captured | Wordmark and announcement `#9a1b2c` |
| Colour, sale | Captured | Sale price `#da3522` |
| Colour, status | Not captured | No error state was shown |
| Type, body | Captured | 14px Maison Neue Book |
| Type, display | Captured | Product and collection titles, 40px Grifo S Light |
| Spacing scale | Partial | Announcement 37, header 71, logo inset 40. The DNA space steps are declared and were not measured on a component. |
| Radius | Captured | Painted controls in this pass are 0. Declared small radius is 4px. |
| Elevation | Not captured | Not measured |
| Motion | Not captured | No duration was read |
| Button | Captured | Select a size, not clicked |
| Button hover, focus, pressed | Not captured | Not measured |
| Link | Captured | Department labels and the red underline row, on the homepage shot |
| Text field | Not submitted | Header search and footer email were not typed in |
| Menu | Captured, in the DOM | Women, Bags, Men, Kids |
| Card | Captured | Collection grid |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Login wall | Not captured | Log in was not opened |
| Signup wall | Not captured | Subscribe was not submitted |
| Checkout | Not captured | Cart was not opened. Select a size and Add to bag were not clicked. |
| Subscribe | Not captured | Footer Subscribe was not submitted |
| Phone width | Not captured | Desktop only |

## Do and don't

1. **Do keep midnight as the ink.** Body type, nav, and the size outline are `#03143b`, not pure black. See [home-light-1440.png](screenshots/home-light-1440.png).
2. **Do use roth for the mark and the bar.** The wordmark and the announcement bar are `#9a1b2c`. See [home-light-1440.png](screenshots/home-light-1440.png).
3. **Do strike the compare price and paint the sale price.** `$160` is midnight with a line-through. `$119` is `#da3522`. See [product-light-1440.png](screenshots/product-light-1440.png).
4. **Do set titles in Grifo, light.** Product and collection titles are 40px, weight 300. Nav stays 12px uppercase Maison Neue Medium. See [product-light-1440.png](screenshots/product-light-1440.png).
5. **Don't open login, cart, or subscribe from this package.** Those controls are in [site-tree.md](site-tree.md) and were not opened. See [site-tree.md](site-tree.md).

## Rebuild

```sh
python3 tools/build_tokens.py
```

`make design-md` is not run for this package. It needs a catalog.json entry, and this pass does not edit catalog.json.
