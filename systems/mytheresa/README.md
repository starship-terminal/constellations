# Mytheresa

Mytheresa is a public luxury shop. This package is a signed-out capture of [https://www.mytheresa.com/sg/en/women](https://www.mytheresa.com/sg/en/women) on 2026-11-22. The start URL was [https://www.mytheresa.com](https://www.mytheresa.com). Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the Clothing menu, Clothing, one product, and About us were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px mark from the public 32 px favicon, on the mark's yellow |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Ink, page, sale red, muted, type, and the square Add to bag |
| [style-guide.html](style-guide.html) | Swatches, the hero title, Add to bag, and a nav link |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Header, collection, product, about |
| [icons/](icons/) | Index only. The live wordmark SVG was not saved |
| [screenshots/](screenshots/) | Homepage, Clothing menu, Clothing, one product, About us |
| [raw/](raw/) | Computed styles read on the homepage, the product, and About us |
| [site-tree.md](site-tree.md) | Header, footer, and the pages those controls open |
| [tools/](tools/) | A check that the written tokens match the readings |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

A preview tab opened https://www.mytheresa.com/ and landed on `/sg/en/women` at 1440 by 900, `devicePixelRatio` 2. `getComputedStyle` was read on the promo ribbon, a department link, a category link, the hero title, a product card designer, the Clothing heading, the product designer, the product name, the price, Add to bag, an unavailable size, a footer link, the email field, and the About us title. Add to bag was not clicked. Search was not submitted. Account was not opened. Subscribe was not submitted.

The public stylesheets were readable. They declare four font faces and no brand colour custom properties. Values in [tokens.json](tokens.json) are computed colours and sizes, not aliases of a site token layer.

## What to distrust

This is the signed-out Singapore store. Do not treat the live hero, a product price, or the promo line as stable chrome. The promo bar is red on the women homepage and black on About us. Its line rotates.

AvenirNextLTPro-Medium is the UI face. OptimaLTPro-Roman is the display face. Both were loaded. Neither file is in this package. The style guide falls back to Palatino and Avenir.

The header wordmark is an SVG and is not in this package. [icon.png](icon.png) is the public favicon, scaled and padded to 128 px on the mark's yellow, not a crop of the header.

Phone width was not captured. Hover and focus were not measured as separate states. Department menus other than Clothing were not opened. The footer was not photographed, because it contains a subscribe form. The privacy-policy links inside the newsletter consent text are `#f2f2f2` on a dark panel. That panel was not in the viewport shot.

## Fonts

AvenirNextLTPro-Medium is the UI face (400 as computed, though the file name says Medium). OptimaLTPro-Roman is the display face (400). DINNextLTArabic-Regular is also loaded and was not used on the measured Latin text. These files are not in this package. The style guide falls back to Palatino for display and Avenir for UI.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Colour, header | Captured | Page `#ffffff`, sale promo `#ed0000` |
| Colour, accent | Captured | Add to bag `#000000` on `#ffffff` |
| Colour, muted | Captured | Unavailable size `#757575` |
| Colour, status | Partial | Unavailable size only. No error state was shown |
| Type, body | Captured | 12px AvenirNextLTPro-Medium |
| Type, display | Captured | 48px OptimaLTPro-Roman on the hero |
| Spacing and radius | Captured | Header 158px, Add to bag 44px, radius 0 |
| Button | Captured | Add to bag measured, not clicked |
| Link | Captured | Nav and footer links |
| Text field | Partial | Search and newsletter measured. Neither was filled or submitted |
| Menu | Captured | Clothing flyout |
| Card | Captured | Product grid on Clothing |
| Tabs | Captured | About us section tabs |
| Text area, checkbox, radio, switch, tooltip, dialog, toast, table, avatar, badge | Partial | A "new" label sits on cards. The other controls were not on the public pages that were opened |
| Dark theme | Not present | The public store paints one light theme |
| Phone width | Not captured | Desktop 1440 only |
| Signed-in account | Not captured | Stopped at `/sg/en/account/login` |

## Do and don't

- **Do keep the store black and white.** The control face is ink. The red bar is a sale promo, shown in [screenshots/home-light-1440.png](screenshots/home-light-1440.png).
- **Do pair the two faces.** OptimaLTPro-Roman carries titles and the product price. AvenirNextLTPro-Medium carries nav, names, and buttons.
- **Do keep corners square.** Add to bag, the size control, and the nav use a 0 radius.
- **Don't style the signed-in product from this package.** Account, wishlist, bag, and checkout were not opened.
- **Don't submit the newsletter from a recreation of this footer.** The field was measured and left empty.

## Rebuild

```bash
python3 tools/check_tokens.py
```

The check compares [tokens.json](tokens.json) with [raw/readings.json](raw/readings.json). `make design-md` was not run. This pass does not edit catalog.json.
