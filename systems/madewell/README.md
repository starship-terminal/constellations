# Madewell

Madewell is a public clothing shop at [https://www.madewell.com](https://www.madewell.com). This package is a signed-out capture on 2026-11-22. Prices read USD after the country control was set to United States. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage, the women's jeans category, one public product, Our Story, and the footer were photographed. Nothing was typed, submitted, or signed in.

The first load redirected to `/SG/` and priced in SGD. United States was selected in the ship-to dialog, then Continue Shopping. No email or address was entered.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage, jeans category, product, Our Story, footer |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [raw/](raw/) | The readings those tokens check against |
| [icons/](icons/) | Header wordmark image |
| [components.md](components.md) | Controls seen on the public pages |
| [patterns.md](patterns.md) | How those controls sit on the page |
| [style-guide.html](style-guide.html) | The measured colours and sizes, rendered |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [icon.png](icon.png) | Site favicon, resized to 128 px |
| [tools/](tools/) | The check that tokens still match the readings |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | `#ffffff`, ink `#000000` |
| Brand | Captured | Announcement and hero red `#ac140a`. Wordmark image |
| Type | Captured, files absent | p22-underground on the shop. manop-variable and TAYBigBird on display lines |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured | [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| Product | Captured | [screenshots/product-light-1440.png](screenshots/product-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Footer | Captured | [screenshots/footer-light-1440.png](screenshots/footer-light-1440.png) |
| Button | Captured, default | Add To Bag is 44px, ink, square. Not clicked |
| Link | Captured | Header nav and footer columns |
| Text field | Captured, empty | Header search and footer email. Not submitted |
| Password field | Not present | The wall asks for email only. Continue was not clicked |
| Login wall | Stopped | Account opened a modal with Sign In, Sign Up, Facebook, and Apple. Screenshot discarded |
| Signup wall | Same modal | Sign Up tab was visible. Not submitted |
| Newsletter | Stopped | Footer email field was not submitted |
| Checkout | Not captured | Bag and Add To Bag were not opened |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop is light |

## Do and don't

- **Keep the page white and the type black.** The page is `#ffffff`. Body type and the nav are `#000000`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use the red bar for the sale line.** The announcement bar is `#ac140a`, 55px, white type. Gift Shop is a second red, `#b7132e`. The Black Friday Event label is the bar red. Same shot.
- **Stop before the account modal.** Account stays on madewell.com and asks for an email, then offers Facebook and Apple. Continue was not clicked. Add To Bag and the email form were not submitted. [screenshots/product-light-1440.png](screenshots/product-light-1440.png)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, ink, brand, and button tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
