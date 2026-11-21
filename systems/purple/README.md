# Purple

Purple is a public mattress and bedding shop. This package is a signed-out capture of [https://purple.com](https://purple.com) on 2026-11-22. The live host returned Cloudflare error 1009 for this region (SG), so the public tree was read from the 18 November 2026 archive and the photographs come from styled archive pages of the same shop. Desktop width measured 1440 by 900. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, mattresses category, and Why Purple, 3 files |
| [tokens.json](tokens.json) | Measured colours, type, and radii |
| [icon.png](icon.png) | 128 px wordmark tile |
| [icons/](icons/) | Wordmark SVG and [icons/INDEX.tsv](icons/INDEX.tsv) |
| [components.md](components.md) | Header, button, badge, and field |
| [patterns.md](patterns.md) | Homepage, category, and Why Purple |
| [style-guide.html](style-guide.html) | Token swatches and the pill button |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [raw/](raw/) | [raw/readings.json](raw/readings.json) and the favicon bytes |
| [tools/](tools/) | [tools/build_tokens.py](tools/build_tokens.py) |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | `#f8f5ef`, ink `#181831` |
| Brand | Captured | Wordmark SVG, fill `#1f1a5e` |
| Type | Captured, files absent | Graphik on body, nav, and buttons |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured | [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Button | Captured, default | Pill, 46px, ink fill, `48px` radius. Not used to start checkout |
| Link | Captured | Header departments and footer columns |
| Text field | Captured, empty | Footer email, 56px wrap, `16px` radius. Not submitted |
| Login wall | Not captured | Account and Sign in were not opened |
| Signup wall | Not captured | Same account wall, not opened |
| Newsletter | Stopped | Footer email field was not submitted |
| Checkout | Not captured | Cart was not opened |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light |
| Live page | Blocked | Cloudflare 1009 from SG |

## Do and don't

- **Keep the page cream and the type ink.** The page and footer are `#f8f5ef`. Body and nav type are `#181831`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use a 48px pill for the primary button.** Learn about our mattresses is 46px tall, ink fill, white type, radius `48px`. [screenshots/category-light-1440.png](screenshots/category-light-1440.png)
- **Mark a sale in promo red.** Black Friday Sale and the On sale badge are `#ca2b16`. [screenshots/category-light-1440.png](screenshots/category-light-1440.png)
- **Stop before account, cart, and the email field.** Those controls were listed and not opened or submitted. [site-tree.md](site-tree.md)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the ink, promo, page, wordmark, and pill tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
