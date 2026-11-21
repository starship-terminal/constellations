# Eight Sleep

Eight Sleep is a public shop for a cooling and heating sleep cover. This package is a signed-out capture of [https://www.eightsleep.com](https://www.eightsleep.com) on 2026-11-22. The browser landed on [https://www.eightsleep.com/sg/](https://www.eightsleep.com/sg/). Prices on the Pod 6 page read USD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage and the Pod 6 product page were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Wordmark on white, 128 px |
| [icons/](icons/) | Header wordmark SVG and an index |
| [screenshots/](screenshots/) | Homepage and Pod 6 product page |
| [raw/](raw/) | The readings the tokens were checked against |
| [tools/](tools/) | `build_tokens.py` |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Paint the promo bar gold. The bar is black, 42px. The type is gold `#e6be8c`, and the amount is white. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Paint Shop the sale white. Shop the sale is black, 41px, radius 8px, white type. Get up to $1,400 off is the white pill, 57px, black type, radius 8px. Same shot.
- Flatten the hero headline to Neue Montreal. The headline is Bethany Elingston, about 120px, with a white gradient clipped to the letters. Nav labels are Neue Montreal, 12px, weight 500, uppercase.
- Open Member Login, the cart, Checkout, Sleep Elixir Login, or help.eightsleep.com from this package. Those walls were not entered. The cookie bar and the sale quiz were hidden for the photographs and were not submitted.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. Neue Montreal for UI, Bethany Elingston for the hero, IBM Plex Mono for the eyebrow. Font files are not in this package |
| Spacing, radius, size | Captured for promo bar, header glass, Shop the sale, Get up to $1,400 off, and the sale badge |
| Button | Default only. Shop the sale was followed as a link. Checkout was not clicked |
| Link, wordmark, price | Default. [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Text field | The footer email field was on the homepage and was not filled. It is below the photographed viewport |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu, tooltip, dialog, toast, table, avatar | Region and cart buttons were not opened. Cookie buttons were not clicked |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product | Captured. Pod 6 page |
| About | No about page was in the header. Careers, Press, and Athletes were listed in the footer and not photographed |
| Empty, loading, error, form error, destructive confirm | Not present on the public pages opened |
| Search, cart, checkout, subscribe, login | Stopped. Member Login, cart, Checkout, and the email field were not used |
| Dark theme | The public shop is a light page with a dark hero. No theme toggle was on screen |
| Phone width | Not captured. This pass is 1440 |
| Motion | Not captured. No motion probe was run |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, ink, gold, hero, compare, and badge tokens, plus the button radius and promo height, against [raw/readings.json](raw/readings.json). It does not recapture the site.
