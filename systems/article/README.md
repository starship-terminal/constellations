# Article

Signed-out capture of the public Article shop at [https://www.article.com/](https://www.article.com/) on 2026-11-22. Desktop 1440 by 900, `devicePixelRatio` 2. The page is white, body type is Proxima Nova, and the coral accent is `#ff6458`.

Photographed the homepage and the Timber 90" leather sofa. Header, footer, and the public links those controls open are in [site-tree.md](site-tree.md). Colours and type are in [tokens.json](tokens.json). `catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

Stopped at login, signup, the footer subscribe form, and the cart. Opening [https://www.article.com/login](https://www.article.com/login) painted a captcha wall titled "Let's confirm you are human". Begin was not clicked. Nothing was typed. No form was submitted. No identity provider was clicked. No captcha was solved. Add to cart was not clicked. Cart was not opened.


## Files

| File | What it holds |
|---|---|
| [DESIGN.md](DESIGN.md) | Generated export of the tokens |
| [components.md](components.md) | Public components named from the capture |
| [icon.png](icon.png) | Product icon, 128 px |
| [login-review.json](login-review.json) | Empty walls, and where the walk stopped |
| [patterns.md](patterns.md) | Public patterns named from the capture |
| [raw/](raw/) | Readings the tokens were measured from |
| [screenshots/](screenshots/) | Public page screenshots |
| [site-tree.md](site-tree.md) | Public pages and where the walk stopped |
| [style-guide.html](style-guide.html) | Renders the tokens |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [tools/](tools/) | Builders for this package |

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | `#ffffff`, text `#2e2e2e` |
| Brand | Captured | Grey ARTICLE. wordmark with a coral period. [icon.png](icon.png) is the public favicon mark |
| Type | Captured, files absent | Proxima Nova regular and bold |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Button | Captured, default | Shop the sale is a 44px coral pill. Add to cart is a 42px coral pill. Not clicked |
| Link | Captured | Header departments and footer columns |
| Text field | Captured, empty | Search, 40px, 4px radius, `#c2c2c2` border. Nothing typed |
| Password field | Not captured | Login wall was a captcha. No password field was reached |
| Login wall | Stopped | [https://www.article.com/login](https://www.article.com/login) painted a captcha. Begin was not clicked |
| Signup wall | Stopped | Login/Register is the same URL. No signup fields were reached |
| Newsletter | Stopped | Footer email field was empty. Subscribe was not clicked |
| Checkout | Not captured | Cart and Add to cart were not opened |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light |

## Do and don't

- **Keep the page white and the message bar near-black.** The page is `#ffffff` and the 42px site message is `#141414`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use coral pills for the sale and the cart.** Shop the sale, Add to cart, and Subscribe are `#ff6458` with a pill radius. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Stop before account, cart, and subscribe.** Login painted a captcha. Add to cart was visible and was not clicked. [site-tree.md](site-tree.md)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, ink, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
