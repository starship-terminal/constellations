# & Other Stories

& Other Stories is a public clothing shop. This package is a signed-out capture of [https://www.stories.com](https://www.stories.com) on 2026-11-22. That URL geo-redirected to [https://www.stories.com/en-ww/](https://www.stories.com/en-ww/), Guernsey / English. Prices read USD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. A phone pass measured 390 by 844. The homepage, the shop drawer, the dresses category, one public product, and the about page were opened. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, shop drawer, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Wordmark rasterized from the live sprite symbol |
| [icons/](icons/) | Wordmark SVG copied from the live sprite, plus INDEX.tsv |
| [screenshots/](screenshots/) | Homepage, phone homepage, shop drawer, dresses, product, about footer |
| [raw/](raw/) | Computed styles the tokens were checked against |
| [tools/](tools/) | A check that the tokens match the readings |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## How the values were read

Computed styles were read in the incognito preview on the live page, after the cookie wall was dismissed with Only required cookies. The stylesheet is one Next chunk. Cross-origin rules were not fully readable. Five CSS variables were present: the three brand families, `--font-serif`, and an Adyen outline. Screenshots are Git LFS. Headless Playwright received an access-denied page, so the walk used the preview tab.

## What to distrust

The about heading computed as black on a black editorial band, so [screenshots/about-light-1440.png](screenshots/about-light-1440.png) shows the footer, not the founding paragraph. The shop drawer shot includes a location dialog that was closed and not confirmed. The homepage account icon has a white hover remnant. Category product names sit below the photographed frame. SerifStories is named and was not loaded.

## Fonts

Quadrant, QuadrantMono, and SansStories at weight 400. They are the site's faces. Font files are not in this package. The style guide uses Helvetica and Courier as stand-ins.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. Quadrant body, QuadrantMono display, SansStories controls. Font files are not in this package |
| Spacing, radius, size | Captured for the promo strip, header, wordmark, Shop now, size chips, and Choose size |
| Button | Shop now default. Choose size disabled. Neither starts checkout |
| Link, wordmark, card, price, size chip | Default. [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Text field | Search was not opened far enough to type. Newsletter email and phone were on screen and were not typed |
| Hover, focus, pressed, loading, error | Focus outline observed once. Other states not captured |
| App shell | Captured, including 390. [screenshots/home-light-390.png](screenshots/home-light-390.png) |
| Category and product | Captured |
| About | Opened. Footer photographed. Heading text is in [site-tree.md](site-tree.md) |
| Search, bag, checkout, subscribe, login | Stopped. Not submitted |
| Dark theme | Not offered on the public shop |

## Do and don't

Keep the wordmark black on the white header, and white when it sits on a photograph. [screenshots/home-light-390.png](screenshots/home-light-390.png).

Keep Shop now white with a 2px radius and 0.96px tracking. [screenshots/home-light-1440.png](screenshots/home-light-1440.png).

Keep Last chance at `#cf0b00`. [screenshots/shop-menu-light-1440.png](screenshots/shop-menu-light-1440.png).

Stop at the bag, account, and newsletter form. Choose size was not clicked. Sign up was not clicked.

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the promo strip, header, last-chance link, footer heading, Choose size, hero size, and control radius against [raw/readings.json](raw/readings.json). It does not recapture the site.
