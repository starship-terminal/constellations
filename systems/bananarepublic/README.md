# Banana Republic

Banana Republic is a public clothing shop. This package is a signed-out capture of [https://bananarepublic.gap.com](https://bananarepublic.gap.com) on 2026-11-22. Prices read USD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the women's sweaters category, one public product, and the Our Values page were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, menus, footer, and the pages this pass opened |
| [tokens.json](tokens.json) | Colours and type measured from the live page |
| [DESIGN.md](DESIGN.md) | How the public chrome is built |
| [components.md](components.md) | Controls that were on screen |
| [patterns.md](patterns.md) | Page patterns |
| [style-guide.html](style-guide.html) | The measured tokens painted locally |
| [icon.png](icon.png) | Wordmark on the cream universal-bar colour |
| [icons/](icons/) | Wordmark SVG copied from the live logo, plus INDEX.tsv |
| [screenshots/](screenshots/) | Homepage, category, product, Our Values |
| [raw/](raw/) | Computed styles the tokens were checked against |
| [tools/](tools/) | A check that the tokens match the readings |

`catalog.json` and `webapps-manifest.json` were left alone. `login-extracted` stays `not-started`.

## Don't

- Keep the wordmark rust and the sale bar black. The page is white, the Gap Inc. strip is `#e9e8e3`, and the ticker is `#000000`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- Leave the corners square. Add to Bag, the hero chips, the search rule, and the size chips are 0px radius. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- Stop at the bag and the sign-in wall. Add to Bag was not clicked. Apply now and the account control point at `/my-account/sign-in`. Those pages were not opened.

## Coverage

| Item | Status |
|---|---|
| Colour | Captured. [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Type | Captured. Lynstone body, Banana department, BananaSerif and Linotype Didot BR display. Font files are not in this package |
| Spacing, radius, size | Captured for the three header bars, search, hero chips, Add to Bag, filter chips, size chips, swatches |
| Button | Default only. Add to Bag not clicked |
| Link, wordmark, card, price, swatch, size chip, badge | Default. [screenshots/category-light-1440.png](screenshots/category-light-1440.png), [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Text field | Search was on screen and empty. It was not submitted. Email and phone fields were not opened |
| Hover, focus, pressed, disabled, loading, error | Not captured |
| Select, checkbox, radio, switch, tabs, menu panel, tooltip, dialog, toast, table, avatar | Menu links were read from the DOM. The open panel was not photographed. Size is a chip row, not a native select. Other controls were not on the public pages opened |
| App shell | Captured. [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category and product | Captured |
| Our Values | Captured. [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Empty, loading, error, form error, destructive confirm | Not present on the public pages opened |
| Search, bag, checkout, subscribe, login, credit apply | Stopped. Not submitted |
| Dark theme | Not present on the public shop |
| Phone width | Not captured. This pass is 1440 |
| Motion | Not captured. No motion probe was run |

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the universal bar, promo bar, wordmark, footer, and Add to Bag tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
