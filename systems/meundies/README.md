# MeUndies

MeUndies is a public underwear, loungewear, and pajamas shop. This package is a signed-out capture of [https://www.meundies.com](https://www.meundies.com) on 2026-11-22. Prices on the product page read USD. Locale en-US. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, one category, one product, About, Membership, the footer, and the empty login modal were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, category, product, about, footer, membership, and the empty login modal |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [raw/](raw/) | Readings the tokens were checked against |
| [icons/](icons/) | Wordmark SVG |
| [icon.png](icon.png) | Site favicon, scaled to 128 px |
| [login-review.json](login-review.json) | Empty wall, and where the walk stopped |
| [components.md](components.md) | Controls seen on the public pages |
| [patterns.md](patterns.md) | How the public pages are built |
| [style-guide.html](style-guide.html) | A page that renders the measured tokens |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [tools/](tools/) | The check that tokens still match the readings |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | Cream `#fffbf1`. Logo row is the same |
| Brand | Captured | Wordmark SVG, fill black. Favicon is a black mark on clear |
| Type | Captured, files absent | headingNow on the shop chrome |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured | [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Membership | Captured, public | [screenshots/membership-light-1440.png](screenshots/membership-light-1440.png) |
| Button | Captured, default | LOGIN is 44px, ink `#1e1e1d`, pill radius. Not clicked |
| Link | Captured | Header departments and footer columns |
| Text field | Captured, empty | Footer email, and the login email |
| Password field | Captured, empty | Login password. Nothing typed |
| Login wall | Captured, empty | [screenshots/login-light-1440.png](screenshots/login-light-1440.png) |
| Signup wall | Stopped | Register was not opened. Footer SIGN UP was not clicked |
| Newsletter | Stopped | Footer email was not submitted |
| Checkout | Not captured | Cart and SELECT A SIZE were not opened |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light |

## Do and don't

- **Keep the page cream and the type black.** Main is `#fffbf1`. Nav, titles, and footer type are `#000000`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use lime for the promo and the sale badge.** The promo bar and the 60% Off badge are `#d9ff6e`. [screenshots/membership-light-1440.png](screenshots/membership-light-1440.png)
- **Use ink for the one loud control.** LOGIN, SELECT A SIZE, and SIGN UP are `#1e1e1d` with white type and a pill radius. [screenshots/login-light-1440.png](screenshots/login-light-1440.png)
- **Stop at the empty login modal.** Email and password were empty. GOOGLE and FACEBOOK were not clicked. [screenshots/login-light-1440.png](screenshots/login-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the cream, lime, ink, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
