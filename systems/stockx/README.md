# StockX

StockX is a public marketplace for sneakers, streetwear, trading cards, handbags, and watches. This package is a signed-out capture of [https://stockx.com](https://stockx.com) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The shop painted dark (`data-theme="dark"`). The homepage, Sneakers, one product, and How It Works were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px mark from the public 192 px favicon |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Page, brand, type, radius, and the Buy Now bar |
| [style-guide.html](style-guide.html) | Swatches, the header row, and a buy bar |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Header, category, product, How It Works |
| [components/crops/](components/crops/) | Empty. No element crops were taken |
| [icons/](icons/) | The X path from the live header SVG, and INDEX.tsv |
| [screenshots/](screenshots/) | Homepage, Sneakers, one product, How It Works |
| [raw/](raw/) | Computed styles and the custom properties that were kept |
| [site-tree.md](site-tree.md) | Header, footer, and the pages those controls open |
| [tools/](tools/) | A check that the written tokens match the readings |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

An incognito preview opened https://stockx.com. `getComputedStyle` was read on the body, the header, the search box, Sign Up | Login, Deals, a section heading, a card price, the footer, the product title, Size, Buy Now, and Sell Now. Custom properties were read from `document.documentElement` while `data-theme` was `dark`. Buy Now was not clicked. Size was not opened. Search was not submitted. Sign Up | Login was not opened. The theme button was not clicked.

The homepage, Sneakers, the product, and How It Works were photographed in that same preview at 1440 by 900 CSS pixels, `devicePixelRatio` 2. PNG files are 2880 by 1800.

## What to distrust

This is the signed-out shop. Do not treat a live price, a last sale, or the hero banner as stable chrome. Prices on these pages were shown in USD. The locale button was not clicked.

The shop tokens are the dark theme. How It Works uses a light marketing shell: white page, black hero, logo fill `#242424`, and a dark Sign Up pill. Those about values are recorded separately. The dark theme button was not switched, so a light shop theme was not measured.

Buy Now paints `#95C0A4` with `#0F0F0F` text. That green is `--colors-brand-primary`. The wordmark on the dark shop uses the same green. On How It Works the wordmark paints `#242424`.

Suisse Intl is the computed UI face. Gestura Reg is the computed How It Works display face. No font file is in this package. The style guide uses Suisse Intl, then Helvetica, and a serif stack for the display line.

The mark in [icons/mark.svg](icons/mark.svg) is the X path from the live header SVG, fill `#95C0A4`. The wordmark letter paths were truncated in the DOM read, so they are not in the file. [icon.png](icon.png) is the public 192 px favicon, resized to 128 px, not a screenshot crop of the header.

Phone width was not captured. Hover and focus were not measured. Footer columns other than About were read from the homepage DOM. The footer was not photographed. Company was opened and discarded because it shows leadership portraits.

## Fonts

Suisse Intl is the computed UI face (400, 500, 600, 700). Gestura Reg is the computed How It Works display face (400). The files are not in this package.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-dark-1440.png](screenshots/home-dark-1440.png) |
| Colour, header | Captured | `#121212`, logo `#95C0A4` |
| Colour, footer | Captured | `#393939`, computed. Not photographed. |
| Colour, brand | Captured | `#95C0A4` on Buy Now |
| Colour, deals | Captured | `#EF6958` |
| Colour, status | Partial | Success and warning are custom properties. No error state was shown. |
| Type, body | Captured | 16px Suisse Intl 400 |
| Type, title | Captured | Product h1 24px Suisse Intl 500 |
| Type, display | Captured | How It Works 60px Gestura Reg 400 |
| Spacing scale | Captured | `--spacing-1` through `--spacing-8` |
| Radius | Captured | Search 8px, pills 100px |
| Elevation | Partial | `--shadows-sm` is a custom property. Header shadow is none. |
| Motion | Captured | `--durations-fast` 150ms, moderate 200ms, slow 300ms. Not observed in a transition. |
| Button | Captured | Sign Up \| Login, Buy Now (not clicked) |
| Button hover, focus, pressed | Not captured | Not measured |
| Link | Captured | Category bar and footer links, in the DOM |
| Text field | Present, empty | Search. Not submitted. |
| Menu | Captured | Category bar. All was not opened. |
| Card | Captured | Homepage rail and Sneakers grid |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Login wall | Not captured | Sign Up \| Login was not opened |
| Signup wall | Not captured | Sign Up was not opened |
| Sell and ask | Not captured | Sell and Sell Now were not opened |
| Buy and bid | Not captured | Buy Now and Size were not opened |
| Phone width | Not captured | Only 1440 was photographed |
| Light shop theme | Not captured | The theme button was not clicked |

## Do and don't

- One green on the dark shop. Buy Now and the wordmark use `#95C0A4`. Other actions stay white pills or quiet text. See [screenshots/product-dark-1440.png](screenshots/product-dark-1440.png).
- Product photos sit in a white well on the dark page. Do not tint the well green. See [screenshots/home-dark-1440.png](screenshots/home-dark-1440.png).
- Deals is the only red label in the category bar. See [screenshots/category-dark-1440.png](screenshots/category-dark-1440.png).
- Primary buttons are pills. Search and Size are 8px fields. Do not square the pills.
- How It Works is a light marketing page with a black hero and a serif title. Do not restyle it as the dark shop. See [screenshots/about-light-1440.png](screenshots/about-light-1440.png).

## Rebuild

```bash
python3 systems/stockx/tools/build_tokens.py
```
