# Depop

Depop is a public marketplace for secondhand fashion. This package is a signed-out capture of [https://www.depop.com](https://www.depop.com) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The shop painted light. The homepage, Women's category, and About were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px mark from the public 180 px apple-touch icon |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Page, brand, type, radius, and spacing from the live shop |
| [style-guide.html](style-guide.html) | Swatches, the header row, and a shop button |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Homepage, category, About |
| [components/crops/](components/crops/) | Empty. No element crops were taken |
| [icons/](icons/) | The wordmark path from the live header SVG, and INDEX.tsv |
| [screenshots/](screenshots/) | Homepage, Women's category, About |
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

An incognito preview opened https://www.depop.com. `getComputedStyle` was read on the body, the header, the search field, the Women nav item, Shop now, the homepage heading, and a footer link. Custom properties were read from `document.documentElement`. There were 273 custom properties. Cross-origin stylesheets could not be parsed, so the values are the computed custom properties, not the stylesheet source.

The homepage, Women's category, and About were photographed in that same preview at 1440 CSS pixels wide, `devicePixelRatio` 2. Homepage and About PNGs are 2880 by 1800. The category PNG is 2880 by 1240, cropped above the listing grid.

Search was not submitted. Sell now, Sign up, and Log in were not opened. The app-install bubble was dismissed so the homepage photograph shows the shop.

## What to distrust

This is the signed-out shop. Do not treat a live price, a search suggestion, or the hero photo as stable chrome. The rotating search suggestion changed between reads ("black josie top", then "white linen trousers").

The shop tokens are the light theme. No dark theme switch was on the page. The About page uses a different shell: GT America Extended, black segmented tabs, and the same red `#e20020` for the current nav item. Those faces are named in [raw/readings.json](raw/readings.json). They are not in the shop token set.

Aktiv Grotesk Ex Basic is the computed shop face. The files are not in this package. The style guide uses that name, then Helvetica.

The wordmark in [icons/mark.svg](icons/mark.svg) is the header SVG path, fill `#E20020`. [icon.png](icon.png) is the public 180 px apple-touch icon, resized to 128 px, not a crop of the header wordmark.

Phone width was not captured. Hover and focus were not measured. The category listing grid was cropped out because product URLs carry a seller username.

## Fonts

Aktiv Grotesk Ex Basic is the computed shop face (400 and 700). GT America Extended is the computed newsroom face. The files are not in this package.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Colour, brand | Captured | `#e20020` wordmark and hero |
| Type, display and body | Captured | 48px heading, 16px nav |
| Search | Captured, not submitted | header search |
| Button, shop now | Captured | white pill on the hero |
| Category page | Captured, grid cropped | [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Dark theme | Not present on the shop | no theme switch |
| Phone width | Not captured | desktop only |
| Login, signup, sell | Stopped | walls |
| Seller listing | Not captured | username in the URL |

## Do and don't

**Use the red wordmark on white.** The header mark is `#e20020` on a white bar. See [screenshots/home-light-1440.png](screenshots/home-light-1440.png).

**Use black pills for Sell now and Sign up.** Those two are filled black. Log in stays a text link.

**Keep Shop now as a white pill on the red hero.** Label is `#e20020`, radius fully rounded.

**Do not invent a dark shop theme.** None was on the page.

**Do not photograph a seller card.** Product URLs include a username. The category file stops above the grid.

## Rebuild

```bash
cd systems/depop && python3 tools/build_tokens.py
```

That checks [tokens.json](tokens.json) against [raw/readings.json](raw/readings.json). It does not rewrite the tokens. `make design-md` was not run, because this pass does not edit catalog.json.
