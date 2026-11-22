# Grailed

Grailed is a public fashion marketplace. This package is a signed-out capture of [https://www.grailed.com](https://www.grailed.com) on 2026-11-22. The shop priced in US dollars. Desktop width measured 1440 by 900. Phone width measured 390 by 844. The homepage, the Men's Tops category, the designers index, About, and the empty Log in and Sign up dialogs were photographed. Nothing was typed. No identity provider was clicked.

The control map is [site-tree.md](site-tree.md). `catalog.json` was left alone.

| File | What it holds |
|---|---|
| [site-tree.md](site-tree.md) | Header, menus, footer, and the public links those controls open |
| [screenshots/](screenshots/) | Homepage at 1440 and 390, Men's Tops, designers, About, and the empty login and signup walls |
| [tokens.json](tokens.json) | Measured colours, type, and sizes |
| [raw/](raw/) | The readings those tokens were checked against |
| [icon.png](icon.png) | Site favicon, resized to 128 px |
| [style-guide.html](style-guide.html) | The measured colours and controls, in Helvetica |
| [components.md](components.md) | Controls seen on the public pages |
| [patterns.md](patterns.md) | How those controls sit on a page |
| [tools/](tools/) | The script that writes the style guide, and how the capture was run |

## Brief

<!-- brief:start -->
Not generated. `catalog.json` was left alone, so `make brief` has no entry to write from.
<!-- brief:end -->

## Health

<!-- health:start -->
Not generated. This package is not in the catalog yet.
<!-- health:end -->

## How the values were read

Computed styles were read in headed Chrome on the homepage, `/categories/tops`, `/about`, and the login dialog. Declared colours were read from custom properties in the site CSS (`--colors--primary-text`, `--colors--seafoam-green`, and the rest in [raw/readings.json](raw/readings.json)). The fee ticker and the shipping banner use a declared radial gradient from `rgb(255, 255, 255)` to `rgb(224, 241, 236)`. A `prefers-color-scheme: dark` probe left the header at `rgb(255, 255, 255)`. There is no dark set.

The T3 preview tab loaded the homepage, then failed twice to take a frame. The error was: "Preview automation snapshot failed: The browser is not producing screenshot frames." The shots in this package are from Chrome after that switch.

## What to distrust

Secondary, tertiary, warning, and alert colours are declared in CSS and were not computed on a sampled element. Their sources say so. The page surface is transparent over a white header, so the page role is the header white, not a sampled body fill. `--global-header-height` computed as 70px. The visible header block measured 118px. Video is Grailed's own face and is not in this package. The style guide uses Helvetica.

## Fonts

Video is served from `fonts.grailed.com` as OpenType (`medium.otf`, `semibold.otf`, `condensed-semibold.otf`, `condensed-bold.otf`). Nav labels, titles, and body copy compute as Helvetica, Arial, sans-serif. Buttons, prices, and Shop all compute as Video, monospace. The font files are not stored here.

## Coverage

| Item | Status | Evidence |
|---|---|---|
| Page colour | Captured | Header `#ffffff`, text `#000000` |
| Brand | Captured | Wordmark in the header. Favicon resized to [icon.png](icon.png) |
| Type | Captured, files absent | Helvetica on nav and titles, Video on buttons and prices |
| Homepage | Captured | [screenshots/home-light-1440.png](screenshots/home-light-1440.png) and [screenshots/home-light-390.png](screenshots/home-light-390.png) |
| Category | Captured | [screenshots/category-light-1440.png](screenshots/category-light-1440.png) |
| Designers | Captured | [screenshots/designers-light-1440.png](screenshots/designers-light-1440.png) |
| About | Captured | [screenshots/about-light-1440.png](screenshots/about-light-1440.png) |
| Product | Not captured | One listing showed "Listed by Grailed" next to a portrait badge. The screenshot was discarded |
| Button | Captured, default | Log in is 32px, black, square. Not submitted |
| Link | Captured | Shop all is `#0000ff` |
| Text field | Captured, empty | Search is 40px, 2px radius. Not typed |
| Login wall | Captured, empty | [screenshots/login-light-1440.png](screenshots/login-light-1440.png) |
| Signup wall | Captured, empty | [screenshots/signup-light-1440.png](screenshots/signup-light-1440.png) |
| Sell | Stopped | `/sell/new` was not opened |
| Checkout | Not captured | No bag or buy control was opened |
| Dark theme | Not present | Dark media probe kept the white header |

## Do and don't

- **Do keep the shop black and white.** The header, titles, and primary button are black on white. See [screenshots/home-light-1440.png](screenshots/home-light-1440.png).
- **Do use the mint ticker for the fee line.** The bar is a white-to-mint gradient and the label is `#208368`. See the same homepage shot.
- **Do keep header buttons square and dialog buttons pill-shaped.** Log in is 0px radius. Log in with email is 32px radius. See [screenshots/login-light-1440.png](screenshots/login-light-1440.png).
- **Don't ship a dark theme.** The dark media probe did not change the header.
- **Don't invent a listing portrait.** Public listing pages in this pass showed a seller badge, so none was kept.
- **Don't treat the declared warning and alert colours as measured.** They were not computed on an element.

## Rebuild

```bash
python3 tools/build_style_guide.py
```
