# Savage X Fenty

Savage X Fenty is a public lingerie and loungewear shop. This package is a signed-out capture of [https://www.savagex.com](https://www.savagex.com) on 2026-11-22. Prices on the product page read USD. Locale en-US. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the bras category, one product, About Us, How Membership Works, the footer, and the empty sign-in wall were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, category, product, about, footer, and the empty sign-in wall |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [raw/](raw/) | Readings the tokens were checked against |
| [icons/](icons/) | Wordmark crop from the homepage |
| [icon.png](icon.png) | Site mark, an X, 128 px |
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
| Page colour | Captured | White `#ffffff`. Header is the same |
| Brand | Captured | Wordmark SVG, 275 by 23. Icon is a lilac X on charcoal |
| Type | Captured, files absent | Plain on the shop, Arizona on the product title |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured | [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Button | Captured, default | TAKE OUR QUIZ is 32px, `#1b1f24`, radius 4px. MEMBER ADD TO BAG is lilac. Not clicked |
| Link | Captured | Header departments and footer columns |
| Text field | Captured, empty | Search, and the sign-in email |
| Password field | Not present | The empty wall asks for email only. SIGN IN was not clicked |
| Login wall | Captured, empty | [screenshots/login-light-1440.png](screenshots/login-light-1440.png) |
| Signup wall | Stopped | Get Started was not clicked |
| Newsletter | Not present | No email field in the photographed footer |
| Checkout | Not captured | MEMBER ADD TO BAG was not clicked |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light |

## Do and don't

- **Keep the page white and the type black.** The header is `#ffffff`. Department labels and the product title are `#000000`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use charcoal for the one loud utility.** TAKE OUR QUIZ and the sign-in submit are `#1b1f24` with white type and radius 4px. [screenshots/login-light-1440.png](screenshots/login-light-1440.png)
- **Use lilac for the member action.** MEMBER ADD TO BAG is `#c5b4e3`, 48px, radius 4px. The offer chip is chartreuse `#bfcc4a`. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Stop at the empty email wall.** Sign in asks for an email and offers Get Started. Neither was used. [screenshots/login-light-1440.png](screenshots/login-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, ink, quiz, member, and search tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
