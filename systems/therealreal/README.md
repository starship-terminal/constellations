# The RealReal

The RealReal is a public luxury consignment shop. This package is a signed-out capture of [https://www.therealreal.com](https://www.therealreal.com) on 2026-11-22. Desktop width measured 1440 by 900, `devicePixelRatio` 2. The homepage and Women were photographed. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage and Women, 2 files |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [raw/readings.json](raw/readings.json) | The computed styles the tokens come from |
| [style-guide.html](style-guide.html) | Promo bar, wordmark, SELL, and search colours |
| [DESIGN.md](DESIGN.md) | Handwritten, because generation needs a catalog entry |
| [components.md](components.md) | Header, nav, SELL, search, and footer |
| [patterns.md](patterns.md) | Homepage and Women |
| [icon.png](icon.png) | 128 px site icon, scaled from the 48 px favicon |
| [tools/build_tokens.py](tools/build_tokens.py) | Checks tokens against the readings |

`catalog.json` was left alone. `webapps-manifest.json` was left alone. `login-extracted` was not flipped.

## How the values were read

Computed styles were read on the live homepage with `getComputedStyle` and `getBoundingClientRect`. `:root` custom properties came from the same page. Screenshots are the 1440 by 900 viewport at device pixel ratio 2, so each PNG is 2880 by 1800. The visual viewport width was 1440.

## What to distrust

The favicon is 48 px, scaled to 128 px with nearest neighbour, so the icon edges are the site's own pixels, repeated. Font files were not downloaded. SuisseIntl was the painted family. `--chakra-fonts-heading` is TRRFont and was not what the body used. The wordmark is an image. The $25 Off banner is a photograph, so its sampled pink is one pixel, not a token the page named. SELL's PNG sample is `#e8f0ad` against a computed `#e6f0a5`. Use the computed value. A product page and About were not photographed: later requests hit a Press & Hold wall, and that hold was not performed.

## Fonts

SuisseIntl is the painted family, weights 400, 600, and 700. The page lists SuisseIntl Fallback after it. The files are the shop's, and they are not in this package. Heading token TRRFont and serif token SuisseWorks were declared and not painted on the photographed body. The style guide falls back to Georgia.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | `#ffffff`, ink `#333333` |
| Brand | Captured | Wordmark image, 172 by 28 |
| Type | Captured, files absent | SuisseIntl on body and nav |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) |
| Category | Captured | [screenshots/category-light-1440.png](screenshots/category-light-1440.png), Women landing |
| Product | Not captured | Hold wall before a product URL could be opened |
| About | Not captured | Footer links to `/about`. Hold wall. Not photographed |
| Button | Captured, default | SELL is 32px, `#e6f0a5`, radius `0px`, uppercase |
| Link | Captured | Header departments and footer columns |
| Text field | Not submitted | Search was not typed. Newsletter email was not typed |
| Login wall | Not captured | Sign In and Member Sign In. The walk stopped there |
| Signup wall | Stopped | Create Account dialog was on the homepage. SIGN UP was not clicked |
| Sell with us | Stopped | `/sell-trr` was mapped and not opened |
| Newsletter | Stopped | First Look is `/first-look/subscription`. Not opened |
| Checkout | Not captured | No cart control was opened. No add-to-cart was clicked |
| Phone width | Not captured | Desktop only |
| Dark theme | Not present | The shop paints a light header on a light page |

## Do and don't

- **Keep the page white and the promo bar black.** The page is `#ffffff`. The promo bar is `#000000`, 40px, white type. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Use the chartreuse SELL chip for sell, and leave it square.** SELL is 32px, `#e6f0a5`, radius `0px`, 11px, tracking `3.3px`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Set department nav in SuisseIntl, 16px, sentence case.** New Arrivals is 16px, weight 400, colour `#333333`. [screenshots/home-light-1440.png](screenshots/home-light-1440.png)
- **Stop before account, signup, sell-with-us, and checkout.** Those controls were mapped and not opened. [site-tree.md](site-tree.md)

## Rebuild

```bash
python3 tools/build_tokens.py
```

That checks the page, ink, announcement, and SELL tokens against [raw/readings.json](raw/readings.json). It does not recapture the site.
