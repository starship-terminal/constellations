# Warby Parker

Warby Parker is a public eyewear shop. This package is a signed-out capture of [https://www.warbyparker.com](https://www.warbyparker.com) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage and one public product were photographed. The empty login and signup walls were reached and then discarded, because each URL carried an Auth0 `state` parameter. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage and one public product |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [login-review.json](login-review.json) | Empty walls, and where the walk stopped |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | Ivory `#faf8f5` on the product. Auth page chalk `#f6f7f5` |
| Brand | Captured | Wordmark white on the hero, ink `#121212` on type |
| Type | Captured, files absent | ABC Social on UI, Ivory LL on titles |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| Button | Captured, default | Pill, blueprint `#1050d0`, 48px on the product, 36px on the hero |
| Link | Captured | Header departments and footer columns |
| Text field | Captured, empty | Newsletter field, 60px, radius `12px`. Auth fields the same, not photographed |
| Password field | Not present | The empty walls ask for email, not a password |
| Login wall | Reached, not filed | Auth0 `state` in the URL. Screenshot discarded |
| Signup wall | Reached, not filed | Same reason. Fields were empty |
| Newsletter | Stopped | Footer email field, not submitted |
| Checkout | Not captured | Cart and Select lenses and buy were not opened |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light |

## Do and don't

- **Keep the shop ivory and the action blueprint.** Product surface is `#faf8f5`. Select lenses and buy is `#1050d0` on white. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)
- **Use a pill for the one action.** Primary buttons use a `100px` radius. The Sign in control is a pill too, white on the hero and outlined on ivory. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Stop at the empty email wall.** Sign in asks for email only. Continue, Google, and Apple were not clicked. The screenshot was discarded because the URL carried session state. [login-review.json](login-review.json)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the ink, blueprint, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
