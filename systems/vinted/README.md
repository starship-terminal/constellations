# Vinted

Vinted is a public second-hand shop. This package is a signed-out capture of [https://www.vinted.com](https://www.vinted.com) on 2026-11-22. The address stayed on `www.vinted.com`. `html` lang was `en-US`. Prices were in dollars. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, Women, About, How it works, and Trust and Safety were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px public icon, resized from the live 192 px apple-touch icon |
| [DESIGN.md](DESIGN.md) | Hand copy of the measured tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Ink, page, teal, chips, type, header, and Sell now |
| [style-guide.html](style-guide.html) | Swatches, the header row, the hero card, and chips |
| [components.md](components.md) | What was visible, and the gaps |
| [patterns.md](patterns.md) | Header, homepage, category, About, How it works, Trust and Safety |
| [components/](components/) | Empty crops folder. No element crops were taken |
| [screenshots/](screenshots/) | Homepage, Women, About, How it works, Trust and Safety |
| [raw/](raw/) | Computed styles read on the homepage, Women, About, and How it works |
| [site-tree.md](site-tree.md) | Header, footer, and the pages those controls open |
| [tools/](tools/) | A check that the written tokens match the readings |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

A headless browser opened https://www.vinted.com. It stayed on that host. `getComputedStyle` was read on the body, the header, the search bar, Sign up | Log in, Sell now, the hero title, the hero card, Learn how it works, a price, a footer label, a footer link, a Women menu link, the Women title, a breadcrumb, the Category chip, an applied chip, a subcategory link, the About title, the About paragraph, and the How it works band. Sell now was not clicked. Sign up and Log in were not clicked. Search was not submitted.

A "Where do you live?" dialog opened on its own. Close was clicked. No country link was followed. A cookie bar was dismissed with Choose essential. Neither action typed or submitted a form.

The homepage, Women, About, How it works, and Trust and Safety were photographed at 1440 by 900 CSS pixels, `devicePixelRatio` 2. PNG files are 2880 by 1800. They were quantized to 256-color sRGB.

## What to distrust

This is the signed-out United States shop on `www.vinted.com`. Do not treat a price as stable chrome. The country dialog listed other domains. Those were not opened, and this package does not claim their colors.

Item cards name a brand. An item page was not opened, because it can print a seller username. The brand names on the photographed grids are the shop's own labels.

V-Inter and V_INTER are the computed faces. No font file is in this package. The style guide uses Helvetica.

[icon.png](icon.png) is the public apple-touch icon, resized from 192 px to 128 px. It is not a crop of the header wordmark.

Phone width was not captured. Hover and focus were not measured. Men, Designer, Kids, Home, Electronics, and the other category pages were not opened. Their menus were read, except Kids, which did not stay open on the last read.

Weight 375 and 580 are the computed values. They are not renamed to 400 or 600.

## Fonts

V_INTER is the body face. V-Inter is the control and title face. The files are not in this package. Fallback stack on the page: "V_INTER Fallback", Helvetica Neue, Arial, sans-serif.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Colour, teal | Captured | `#007782` Sell now, links, wordmark |
| Colour, chip | Captured | `#e6fafa` selected Category chip |
| Colour, mint | Captured | `#edffe9` How it works band |
| Colour, hairline | Captured | Sampled `#ededed` |
| Type, body | Captured | 13px V_INTER 400 |
| Type, title | Captured | 24px weight 500 on the homepage and About |
| Spacing scale | Partial | Header 98, search 36, sell 32, hero sell 44, chip 36. No named scale |
| Radius | Captured | Control 6px, card 12px, chip pill |
| Elevation | Not captured | No shadow was read on the hero card |
| Motion | Not captured | No duration was read |
| Button | Captured | Sell now and Sign up. Neither clicked |
| Button hover, focus, pressed | Not captured | Not measured |
| Link | Captured | Nav, menu, footer, subcategory |
| Text field | Present, not used | Search. Not typed |
| Menu | Captured | Women menu opened and read |
| Card | Captured | Hero card and item grid |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| How it works | Captured | [screenshots/how-light-1440.png](screenshots/how-light-1440.png) |
| Trust and Safety | Captured | [screenshots/safety-light-1440.png](screenshots/safety-light-1440.png) |
| Login wall | Not captured | Sign up \| Log in was not opened |
| Sell wall | Not captured | Sell now was not opened |
| Checkout | Not captured | No checkout control was clicked |
| Item page | Not opened | A seller username can print there |
| Dark theme | Not present | The shop did not offer one |
| Phone width | Not captured | Desktop only |

## Do and don't

- **Use the teal for the one filled action.** Sell now is `#007782` with white type. See [screenshots/home-light-1440.png](screenshots/home-light-1440.png).
- **Keep the page mint-grey, not white.** Body background is `#edf2f2`. The header and the hero card are white.
- **Leave Sign up, Sell now, and search unsubmitted.** Those controls stop the public walk.
- **Do not open an item page for a crop.** The grid already shows the card. The item page can print a seller username.

## Rebuild

```bash
python3 tools/build_tokens.py
```

The script checks [tokens.json](tokens.json) against [raw/readings.json](raw/readings.json). It does not rewrite either file.
