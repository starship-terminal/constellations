# Amazon

Amazon is a retail storefront. This package is a public Playwright capture of [amazon.com](https://www.amazon.com/) on 2026-11-22, signed out. The header is orange (`#ff6200`) on a white page. Desktop width measured 1440 by 900. Phone width measured 390 by 844 on the home page. Nothing was typed, submitted, added to a cart, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px site icon, resized from the published favicon |
| [DESIGN.md](DESIGN.md) | Light-theme copy of the measured tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Colour, type, radius, and size tokens |
| [style-guide.html](style-guide.html) | Specimens rendered from the tokens |
| [components.md](components.md) | Component inventory and gaps |
| [patterns.md](patterns.md) | Page patterns |
| [components/](components/) | Crops of Add to cart, Buy Now, and Sign in |
| [icons/](icons/) | INDEX.tsv. The wordmark is a CSS sprite and was not extracted |
| [screenshots/](screenshots/) | Public pages, open menus, and the login and signup walls |
| [raw/](raw/) | Computed styles and custom properties that were read |
| [site-tree.md](site-tree.md) | Which control opens which page |
| [login-review.json](login-review.json) | What the login and signup walls ask for |
| [tools/](tools/) | Token check and the style-guide writer |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

Headless Playwright opened the public site at 1440 by 900, `devicePixelRatio` 1. Computed styles were read on the body, `#nav-belt`, the search field, the sign-in heading, Continue, Add to cart, and Buy Now. Header colours were also read from `--nav-*` custom properties. Hover on Continue was a real pointer move. Focus on the search field and the email field used `element.focus()`. No text was typed.

Phone home was requested at 390 by 844 with `deviceScaleFactor` 2. It measured `innerWidth` 390.

## What to distrust

This is the public storefront, not a signed-in account. Orders, lists, and recommendations were not entered.

The delivery location on the photographed pages is Singapore. Prices on the product page are in SGD. No street address was entered. A product URL that redirected to amazon.sg was discarded.

The homepage body computed to Arial before Amazon Ember loaded. The sign-in wall and the product title computed to Amazon Ember. Treat Arial as the fallback, not as a second brand face.

Muted `#565959` is the published `--secondary-text-color` fallback. It was not read off a live secondary label in this pass.

Continue hover is `#ffce12`. The default fill is `#ffd814`. The style guide button uses the default fill.

The hamburger wordmark is a sprite. It is not in `icons/`.

## Fonts

Amazon Ember is the product face, named in computed styles on the sign-in wall. Arial is the fallback the homepage body computed to. The font files are not in this package.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | `#ffffff` body |
| Text colour | Captured | `#0f1111` |
| Accent | Captured | Add to cart and Continue `#ffd814` |
| Brand | Captured | Header `#ff6200` |
| Link | Captured | `#2162a1` |
| Type | Captured | Amazon Ember and Arial fallback |
| Radius | Captured | 100px pills, 8px fields |
| Button | Captured | [components/crops/button-add-to-cart-default.png](components/crops/button-add-to-cart-default.png) |
| Link | Captured | [components/crops/link-signin-default.png](components/crops/link-signin-default.png) |
| Text field | Captured | Search and empty sign-in field |
| Select | Observed | Department select. Not changed. |
| Menu | Captured | [screenshots/home-light-menu.png](screenshots/home-light-menu.png) |
| Card | Captured | Homepage cards |
| Badge | Captured | Deal badge on the product page |
| App shell | Captured | [screenshots/home-light-default.png](screenshots/home-light-default.png) |
| Empty | Captured | [screenshots/cart-light-default.png](screenshots/cart-light-default.png) |
| Search | Captured, empty | Search focused. Not submitted. |
| Form validation | Not captured | Sign-in form was not submitted |
| Loading and error | Not captured | No form was submitted |
| Destructive confirmation | Not present | Not on the public pages opened |
| Onboarding | Not captured | Would require an account |
| Dark theme | Not present | Public storefront is light |
| Light theme | Captured | Storefront, login, and signup |
| Desktop 1440 | Captured | Playwright innerWidth 1440 |
| Phone 390 | Captured | Home |
| Signed-in app | Not captured | Login wall. Session absent |
| Checkout | Not captured | Add to cart and Buy Now were not clicked |

## Do and don't

- **Use yellow for the primary action.** Add to cart and Continue are `#ffd814` on `#0f1111`, 100px radius, 32px tall. Hover is `#ffce12`. See [screenshots/product-light-default.png](screenshots/product-light-default.png).
- **Use orange for the header, not for the primary button.** The header is `#ff6200`. Buy Now is a separate orange, `#ffa41c`. See [screenshots/home-light-default.png](screenshots/home-light-default.png).
- **Keep the page white.** Body background is `#ffffff`. Department cards are white. Text is `#0f1111`. See [screenshots/home-light-default.png](screenshots/home-light-default.png).
- **Do not submit the sign-in form from this capture.** The first wall asks for a mobile number or email and stops at Continue. No password field was on that screen. Nothing was typed. See [screenshots/login-light-default.png](screenshots/login-light-default.png).
- **Do not follow Orders, lists, or Subscribe & Save and keep capturing.** Those URLs are account or subscribe walls. Record them and stop. See [login-review.json](login-review.json).

## Rebuild

```bash
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

Run those from this folder. `tools/build_tokens.py` checks sources. It does not regenerate tokens.json. The tokens were written from the readings at capture time. `make design-md` cannot write this package's DESIGN.md until catalog.json has an `amazon` entry. This pass does not edit catalog.json.
