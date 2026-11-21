# Mercari

Mercari is a public marketplace for used and secondhand goods. This package is a signed-out capture of [https://www.mercari.com](https://www.mercari.com) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, Electronics, About, and All brands were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px site icon, resized from the public apple-touch icon |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Navy, primary, field, type, and the header sizes |
| [style-guide.html](style-guide.html) | Swatches, the header row, and Sell |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Header, homepage, category, About, brands |
| [components/](components/) | Empty crops folder. No element crops were taken |
| [icons/](icons/) | Empty. The wordmark is an inline SVG and was not saved as a file |
| [screenshots/](screenshots/) | Homepage, Electronics, About, All brands |
| [raw/](raw/) | Computed styles read on the live pages |
| [site-tree.md](site-tree.md) | Header, footer, and the pages those controls open |
| [tools/](tools/) | A check that the written tokens match the readings |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

An incognito preview opened https://www.mercari.com. `getComputedStyle` was read on the body, the header, the logo, the search field, Log in, Sell, a category label, a section title, a price, the footer, a footer label, a footer link, and a legal link. The same preview then opened Electronics, About, and All brands, and the login URL. Sell was not clicked. Search was not submitted. Sign up was not clicked. Log in was not clicked from the header. The login URL was opened only to see the wall.

A privacy bar was dismissed with Got it. That click did not type or submit a form.

The homepage, Electronics, About, and All brands were photographed in that same preview at 1440 by 900 CSS pixels, `devicePixelRatio` 2. Homepage, About, and Brands PNGs are 2880 by 1800. The Electronics PNG is cropped to 2880 by 1500 so the seller-username row is not in the file.

## What to distrust

This is the signed-out shop. Do not treat a price, a sold count, or the notification badge as stable chrome. The homepage badge read 3. Electronics said about 147K new listings each week.

The homepage paints the header `#252b60`. Electronics, About, and Brands paint the same header `#ffffff` and the wordmark `#5356ee`. Both are recorded. CSS variable `--color-primary` is `#5356ee`. The homepage header height measured 77px. `--main-header-height` read 76px on the homepage and 111px on the first paint. The token uses the measured 77px.

Averta is the computed face. No font file is in this package. The style guide uses Avenir Next, then Helvetica Neue, then Arial.

The public apple-touch icon is a blue square, sampled `rgb(104, 119, 245)`. [icon.png](icon.png) is that file resized to 128 px. It is not a crop of the header wordmark.

Phone width was not captured. Hover, focus, and pressed were not measured. Dark theme was not offered on these pages.

The Electronics shot is cropped above the seller row. Listing titles in that shot are product names, not seller usernames.

## Fonts

Averta, computed on the body, the header, and the titles. The file is not in this package. The fallback in the style guide is Avenir Next, Helvetica Neue, Arial, sans-serif.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Colour, page | Captured | `#ffffff` body |
| Colour, navy header and footer | Captured | `#252b60` |
| Colour, primary | Captured | `#5356ee`, also `--color-primary` |
| Colour, field | Captured | `#f5f5f6` search and legal bar |
| Type, body | Captured | 16px Averta 400 |
| Type, nav | Captured | 16px weight 600 |
| Type, category label | Captured | 14px weight 400 |
| Type, page title | Captured | 26px weight 600 |
| Type, hero | Captured | 65px weight 600 on About |
| Spacing | Partial | Header 77, category row 92, search 44, Sell 32. No named scale. |
| Radius | Captured | Search 44px, Sell 4px |
| Elevation | Not captured | No shadow was read on the header |
| Motion | Not captured | No duration was read |
| Button | Captured | Sell and List an item, measured, not clicked |
| Button hover, focus, pressed | Not captured | Not measured |
| Link | Captured | Category, footer, and brand links |
| Text field | Present, empty | Search. Not submitted. |
| Menu | Not captured | Brands has a chevron. The menu was not opened. |
| Card | Captured | Homepage promo tiles and the Electronics sale row |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Brands | Captured | [screenshots/brands-light-1440.png](screenshots/brands-light-1440.png) |
| Login wall | Seen, not photographed | `/login/` shows email, Continue, and identity providers. Nothing typed. |
| Signup wall | Not captured | Sign up and Create an account were not opened |
| Sell wall | Seen as a redirect | `/sell/` redirected to the login wall |
| Checkout | Not captured | Cart was not opened |
| Subscribe | Not present | No newsletter field on the mapped footer |
| Phone width | Not captured | Desktop only |

## Do and don't

1. **Do paint the homepage header navy, with a white wordmark and a white Sell button.** Nav labels are 16px, weight 600. See [home-light-1440.png](screenshots/home-light-1440.png).
2. **Do paint interior headers white, and List an item in primary.** The wordmark turns primary on those pages. See [about-light-1440.png](screenshots/about-light-1440.png).
3. **Do keep category labels at 14px in primary.** The icon row sits under the homepage header. See [home-light-1440.png](screenshots/home-light-1440.png).
4. **Do set page titles at 26px, weight 600.** About is the exception: 65px on a primary hero. See [category-light-1440.png](screenshots/category-light-1440.png).
5. **Don't type in Search, and don't click Sell or Log in for this package.** Those stops are in [site-tree.md](site-tree.md).
6. **Don't include the legal bar in a screenshot.** It prints a mailing address. The Electronics seller row was cropped for the same reason: it prints usernames.

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks [tokens.json](tokens.json) against [raw/readings.json](raw/readings.json). It does not rewrite either file. `make design-md` was not run, because this pass does not edit catalog.json.
