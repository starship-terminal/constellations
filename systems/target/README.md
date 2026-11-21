# Target

Target is the retail site at [target.com](https://www.target.com/). This package is a public capture on 2026-11-22, signed out. The page is white with a red brand button (`#cc0000`). Desktop width measured 1440 by 900. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px site icon, resized from the published favicon |
| [DESIGN.md](DESIGN.md) | Copy of the measured tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Colour, type, radius, and spacing tokens |
| [style-guide.html](style-guide.html) | Specimens rendered from the tokens |
| [components.md](components.md) | Component inventory and gaps |
| [patterns.md](patterns.md) | Page patterns |
| [screenshots/](screenshots/) | Homepage, one product page, and the empty login wall |
| [raw/](raw/) | Computed styles and published custom properties |
| [site-tree.md](site-tree.md) | Which control opens which page |
| [login-review.json](login-review.json) | What the login wall asks for |
| [tools/](tools/) | Token check and the style-guide writer |
| [icons/](icons/) | Icon redraws |

## How the values were read

The shared preview browser opened the public site at 1440 by 900, `devicePixelRatio` 2. Computed styles were read on the body, the h1, the search wrap, and the footer Sign up button. Published custom properties (`--color-*`, `--typography-*`, `--radius-*`, `--motion-*`) were read from the stylesheets on the homepage.

A headless Chrome pass hit a Target verification wall and was discarded. A later preview navigation hit the same wall. Those pages were not photographed. The wall was not solved.

## What to distrust

This is the signed-out marketing homepage, one product page, and the empty login wall. It is not the signed-in account, cart, or checkout.

Accent hover (`#aa0000`) is the published token. It was not held under a pointer.

Success, warning, and info colours are published tokens. No live state of those colours was on the pages that were opened.

The homepage h1 text is "Homepage" and is visually hidden. The hero type is painted in an image.

Phone width was not photographed. The verification wall appeared before that shot.

## Fonts

Helvetica for Target is the UI face, with Targetica and Helvetica Neue in the stack. It is a commercial face. The file is not in this package.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-light-default.png](screenshots/home-light-default.png) |
| Colour, accent | Captured | Sign up fill `#cc0000` |
| Colour, status | Published only | Tokens exist. No live error, warning, or success state was shown |
| Type, display and UI | Captured | Body 16px, h1 29px / 700 |
| Type, code | Not present | No code sample on the public pages |
| Spacing scale | Captured | Published 4px step, `--_ref-measurement-space-*` |
| Radius | Captured | 999px pill on search and Sign up |
| Elevation | Not captured | No shadow was read on the measured controls |
| Motion | Published only | Durations and easings are in the stylesheets. They were not timed |
| Button | Captured | Footer Sign up, and Continue on the login wall |
| Button hover | Not captured | Published hover token only |
| Button focus | Not captured | Published focus token only |
| Link | Captured | Header and footer links on the home shot |
| Text field | Captured, empty | [screenshots/login-light-default.png](screenshots/login-light-default.png) |
| Text area | Not present | Not on the pages that were opened |
| Select | Not present | Not on the pages that were opened |
| Checkbox | Observed | Keep me signed in on the login wall. Not changed |
| Radio, switch | Not present | Not on the pages that were opened |
| Tabs | Not present | Not on the pages that were opened |
| Menu | Observed | Categories is a link to the shop-all page. The menu was not opened after the verification wall |
| Dialog | Observed | Sign-in tooltip on first paint. Closed before the saved home shot |
| Card | Captured | Product tiles on the homepage and the product page |
| Avatar, badge | Observed | Bestseller badge on the product page |
| Search | Captured, empty | Header combobox. Not submitted |
| App shell | Captured | Header and footer on the home shot |
| Empty login | Captured | [screenshots/login-light-default.png](screenshots/login-light-default.png) |
| Phone width | Not captured | Verification wall appeared before the 390 shot |
| Dark theme | Not present | The public site that loaded is light |

## Do and don't

- The brand button is a red pill. Secondary actions on the product page are an outline button.
- Search sits in a gray pill, not a bordered box.
- Login and signup are one screen. The first field is email or mobile phone. Continue was not clicked.
