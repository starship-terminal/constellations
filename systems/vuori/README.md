# Vuori

Vuori is a public athletic shop. This package is a signed-out capture of [https://vuoriclothing.com](https://vuoriclothing.com) on 2026-11-22. The country control read US. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the women's collection, one public product, Our Story, and the empty login wall were photographed. Signup uses that same wall. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, collection, product, Our Story, login wall, signup wall |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [login-review.json](login-review.json) | Empty wall, and where the walk stopped |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [components/](components/) | Component crops |
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
| Page colour | Captured | `#ffffff`, ink `#333333` |
| Brand | Captured | Wordmark 112 by 18, letters `#333333`, mark gradient from `#A4DEF9` to `#F8EB30` |
| Type | Captured, files absent | aktiv-grotesk on body, nav, and headings. Ask AI reports Arial |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Collection | Captured | [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Button | Captured, default | Hero shop links are square, 60px, white. Select Size is 44px, `#333333`, radius `2px` |
| Link | Captured | Header departments and footer columns |
| Text field | Captured, empty | Login email, 40px, radius `2px` |
| Password field | Not present | The wall asks for email only |
| Login wall | Captured, empty | [screenshots/login-light-1440.png](screenshots/login-light-1440.png) |
| Signup wall | Captured, empty | Same wall. [screenshots/signup-light-1440.png](screenshots/signup-light-1440.png) |
| Newsletter | Stopped | Promo Sign Up and footer email were not submitted |
| Checkout | Not captured | Bag was not opened. Select Size was not clicked |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light |

## Do and don't

- **Keep the page white and the wordmark ink.** The page is `#ffffff` and the letters are `#333333`. The mark is the only gradient. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use a square shop link and a near-square ink button.** Shop Men's is 60px, radius `0px`, white. Select Size is 44px, radius `2px`, ink on white. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Leave Gifting as the only coloured department.** It is `#811b28`. The other departments are ink. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Stop at the empty email wall.** Sign in and create account share one email field. Continue, Shop, and Google were not clicked. [screenshots/login-light-1440.png](screenshots/login-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, ink, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
