# Cotopaxi

Cotopaxi is a public outdoor shop. This package is a signed-out capture of [https://www.cotopaxi.com](https://www.cotopaxi.com) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, All Packs, one public product, and About Us were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, All Packs, product, About Us |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [raw/readings.json](raw/readings.json) | The computed styles the tokens come from |
| [style-guide.html](style-guide.html) | Page, announcement, nav, and button colours |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [components.md](components.md) | Header, search, nav, and the shop button |
| [patterns.md](patterns.md) | Homepage, collection, product, and about |
| [icon.png](icon.png) | 128 px site icon, scaled from the 32 px favicon |
| [tools/build_tokens.py](tools/build_tokens.py) | Checks tokens against the readings |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## How the values were read

Computed styles were read on the live homepage with `getComputedStyle` and `getBoundingClientRect`. `:root` custom properties came from the theme stylesheet `styles.css`. Screenshots are the 1440 by 900 viewport at device pixel ratio 2, so each PNG is 2880 by 1800.

## What to distrust

The favicon is 32 px, scaled to 128 px with nearest neighbour, so the icon edges are the site's own pixels, repeated. Font files were not downloaded. Gotham and Mont were loaded in the page. The style guide falls back to Helvetica. Bootstrap radius tokens are `0px`. The search pill is the exception, at `99px`.

## Fonts

Gotham is the body family, weights 400 and 700. Mont is the nav family, weights 600 and 800. The page lists Helvetica Neue, Helvetica, and Arial after them. The files are the shop's, and they are not in this package.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | `#ffffff`, ink `#25282a` |
| Brand | Captured | Wordmark SVG, 114 by 37 |
| Type | Captured, files absent | Gotham on body, Mont on nav |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Collection | Captured | [screenshots/collection-light-1440.png](screenshots/collection-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Button | Captured, default | Shop Packs is 41px, white, radius `0px`, uppercase |
| Link | Captured | Header departments and footer columns |
| Text field | Captured, empty | Search pill, 300 by 30, `#f2f2f2` |
| Login wall | Not captured | Account points at `https://account.cotopaxi.com/`. The walk stopped there |
| Newsletter | Stopped | No subscribe form was submitted |
| Checkout | Not captured | Side cart was not opened. Add to Cart was not clicked |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light |

## Do and don't

- **Keep the page white and the announcement lilac.** The page is `#ffffff`. The promo bar is `#ebdbff`, 34px. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use a square white shop button.** Shop Packs is 41px, radius `0px`, uppercase, letter-spacing `1.5px`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Leave Black Friday and Gifts as the coloured departments.** Black Friday is `#8a0010`. Gifts is `#005f9e`. The others are ink. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Stop before account, cart, and checkout.** Those controls were mapped and not opened. [site-tree.md](site-tree.md)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, ink, and primary tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
