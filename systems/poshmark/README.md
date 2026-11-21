# Poshmark

Poshmark is a public resale marketplace. This package is a signed-out capture of [https://poshmark.com](https://poshmark.com) on 2026-11-22. The footer country chip read United States. Prices on the opened pages were USD. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the Women menu, the Women category, and How it works were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px mark from the public apple touch icon |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Page, ink, burgundy, live, type, and the bar heights |
| [style-guide.html](style-guide.html) | Swatches, the search pill, and the FREE SHIPPING line |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Homepage, menu, category, how it works |
| [components/](components/) | Empty crops folder. No element crops were taken |
| [icons/](icons/) | Wordmark paths from the live header SVG, and INDEX.tsv |
| [screenshots/](screenshots/) | Homepage, Women menu, Women category, How it works |
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

An incognito preview opened https://poshmark.com at 1440 by 900, `devicePixelRatio` 2. `getComputedStyle` was read on the body, the header, a department link, the search field, Log in / Sign up, the homepage hero, a price, the category title, the footer, and Start Selling. The wordmark fill was read from the public SVG. No `:root` custom properties were readable. Search was not submitted. Log in was not opened. Sell was not opened. The cookie notice Ok was clicked so the homepage photograph was not covered.

## What to distrust

The homepage hero rotates. The photograph holds the FREE SHIPPING slide. Do not treat that line, a listing price, or the editorial tiles as stable chrome.

Graphik and NantesWeb are the computed faces. The files are not in this package. The style guide falls back to Helvetica Neue, then Georgia.

The wordmark in [icons/wordmark.svg](icons/wordmark.svg) is the public header SVG, fill `#610722`. [icon.png](icon.png) is the 180 px apple touch icon, resized to 128 px. Its field is `#7F0353`, which is not the wordmark fill.

The category title band `#F6F6F6` was read from the photograph, not from `getComputedStyle`. Phone width was not captured. Hover and focus were not measured as states. Menus other than Women were read from the homepage DOM. Listing pages were not opened, because they show a seller username. `/about` was opened and discarded: the first slide paired a person's name with a portrait.

## Fonts

Graphik is the computed UI face (400, 500, 600, 700). NantesWeb is the display face (600). The files are not in this package.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Colour, header | Captured | White, 116px |
| Colour, wordmark | Captured | `#610722` |
| Colour, accent | Captured | Posh Live `#BA4E41` |
| Colour, footer | Captured | `#121212` |
| Colour, muted | Captured | Sidebar `#717171`, footer links `#999999` |
| Colour, status | Not captured | No error state was shown |
| Type, body | Captured | 14px Graphik |
| Type, title | Captured | Category 26px NantesWeb, hero 52px |
| Spacing scale | Partial | Header 116, utility 73, department 44, menu 415, footer 608. No named scale. |
| Radius | Captured | Search 60, login 4, Sign Up 3, Start Selling 14 |
| Elevation | Captured | Header shadow is none |
| Motion | Not captured | Homepage hero and About carousel move. Not filmed |
| Button | Captured | Log in, Sign Up, Start Selling (none clicked) |
| Button hover, focus, pressed | Not captured | Not measured |
| Link | Captured | Department links, on the homepage shot |
| Text field | Present, empty | Header search. Not submitted |
| Menu | Captured | Women panel. Other menus read from the DOM |
| Card | Captured | Women grid. No seller username in the frame |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) is How it works. `/about` was discarded |
| Login wall | Not captured | Log in was not opened |
| Signup wall | Not captured | Sign Up was not opened |
| Sell wall | Not captured | Sell Now and Start Selling were not opened |
| Checkout | Not captured | No bag control was opened. Hearts were not clicked |
| Subscribe | Not present | No email signup sat in the footer |

## Do and don't

**Keep the wordmark burgundy and the login button ink.** The wordmark is `#610722`. Log in / Sign up is an ink pill with white type. [screenshots/home-light-1440.png](screenshots/home-light-1440.png).

**Keep the search pill round.** The field is a 60px radius pill with a 1px ink border, and Listings sits inside it. [screenshots/home-light-1440.png](screenshots/home-light-1440.png).

**Paint Posh Live in the rust red.** The department row is ink except that one link. [screenshots/home-light-1440.png](screenshots/home-light-1440.png).

**Do not invent a seller name on a card.** The category grid shows title, price, and size. [screenshots/category-light-1440.png](screenshots/category-light-1440.png).

## Rebuild

```bash
cd systems/poshmark && python3 tools/build_tokens.py
```

The check confirms the written tokens still match [raw/readings.json](raw/readings.json). It does not recapture the site.
