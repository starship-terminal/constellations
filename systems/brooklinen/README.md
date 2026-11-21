# Brooklinen

Brooklinen is a public bedding and bath shop. This package is a signed-out capture of [https://www.brooklinen.com](https://www.brooklinen.com) on 2026-11-22. Prices on the product page read USD. The account host opened as locale en-SG. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, one public product, and the empty sign-in wall were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, product, and the empty sign-in wall |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [login-review.json](login-review.json) | Empty wall, and where the walk stopped |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [components.md](components.md) | Public components named from the capture |
| [icon.png](icon.png) | Product icon, 128 px |
| [icons/](icons/) | Icon redraws |
| [patterns.md](patterns.md) | Public patterns named from the capture |
| [raw/](raw/) | Readings the tokens were measured from |
| [style-guide.html](style-guide.html) | Renders the tokens |
| [tools/](tools/) | Builders for this package |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | `#fdfaf8`, navy `#283455` |
| Brand | Captured | Wordmark SVG, fill `#253455` |
| Type | Captured, files absent | Brandon Text on the shop, Toledo on the hero, a hashed face on the account wall |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Button | Captured, default | Add to Cart is 56px, navy, `20px` radius. Not clicked |
| Link | Captured | Header departments and footer columns |
| Text field | Captured, empty | Sign-in email, 53px, `20px` radius, navy border |
| Password field | Not present | The empty wall asks for email only. Continue was not clicked |
| Login wall | Captured, empty | [screenshots/login-light-1440.png](screenshots/login-light-1440.png) |
| Signup wall | Same wall | Create Account opens the same Sign in page. Copy says "Sign in or create an account" |
| Newsletter | Stopped | Footer email field was not submitted |
| Checkout | Not captured | Cart and Add to Cart were not opened |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light |

## Do and don't

- **Keep the page cream and the chrome navy.** The page is `#fdfaf8`. The promo bar, department type, and Add to Cart are `#283455`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use a 20px pill for the primary button.** Add to Cart and Shop the Sale are 56px, radius `20px`, navy fill, white type. Size chips are 40px with a `16px` radius. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Stop at the empty email wall.** Sign in and Create Account share one page. It asks for email and offers Continue with Shop. Neither was clicked. [screenshots/login-light-1440.png](screenshots/login-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, navy, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
