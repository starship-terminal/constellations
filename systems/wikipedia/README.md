# Wikipedia public surface

A token set and page captures for the public English Wikipedia at **https://en.wikipedia.org**. First capture of this product into `systems/wikipedia/` on **2026-11-22**, signed out. Desktop is **1440 by 900** at devicePixelRatio 2 (PNG 2880 by 1800). Phone is **390 by 844** at devicePixelRatio 2 (PNG 780 by 1688). The site tree is [site-tree.md](site-tree.md).

origin/main did not have `systems/wikipedia/`. This is a new package. The slug is `wikipedia`. `catalog.json` and `webapps-manifest.json` were left alone, so `login-extracted` stays `not-started`.

The public default is **Light** (Vector 2022, `skin-theme-clientpref-day`). Text is Standard. Width is Standard. Appearance is pinned on the right. A separate headless context selected Color Dark only to read night tokens and shoot one home frame. The preview session stayed on Light.

**Boundary.** Login and signup were photographed empty on auth.wikimedia.org. Nothing was typed. Nothing was submitted. No identity provider was clicked. No captcha was solved. No page was edited. Donate, sister projects, and the language list were not followed.

| File | What it is |
|---|---|
| [README.md](README.md) | This file. |
| [site-tree.md](site-tree.md) | Which header, menu, drawer, and footer controls open which pages, and where this pass stopped. |
| [login-review.json](login-review.json) | Empty login and signup walls. login-extracted is not-started. |
| [icon.png](icon.png) | 128px favicon, resized from wikipedia.ico. |
| [tokens.json](tokens.json) | W3C tokens. `core` holds type and the search control. `light` and `dark` hold Codex colour roles. |
| [DESIGN.md](DESIGN.md) | Hand-written from the measured tokens. Not regenerated, because that would rewrite the catalog. |
| [style-guide.html](style-guide.html) | Swatches, the article title, a progressive link, and the search control. |
| [components.md](components.md) | Component inventory and gaps. No crops. |
| [patterns.md](patterns.md) | Main page, article, search, appearance, and the auth walls. |
| [raw/measured-home.json](raw/measured-home.json) | Computed styles and Codex custom properties on the main page, Light. |
| [raw/measured-article.json](raw/measured-article.json) | Same readings on Talking to Yourself. |
| [raw/measured-dark.json](raw/measured-dark.json) | Same readings after Color Dark, headless only. |
| [raw/article-toc.json](raw/article-toc.json) | Contents labels on the article. |
| [screenshots/](screenshots/) | 256-colour PNGs. Git LFS. |

## Brief

Hand-written. `make brief` was not run, because that reads `catalog.json` and this package is not registered.

1. Paint the canvas `#f8f9fa` and the content column white.
2. Set body text in the system sans at 16px, ink `#202122`, content line-height 26px.
3. Set the article title in Linux Libertine (Georgia fallback) at 28.8px / 39.6px, weight 400, colour `#101418`.
4. Paint links `#36c` with a 2px radius. Visited is `#6a60b0`.
5. Keep the search field 32px tall, 14px type, 1px `#72777d` border, radius 2px on the left.
6. Do not invent a signed-in editor from this package.

## Health

Not graded. `catalog.json` was left alone, so `make grade` was not run. Layout gaps: no component crops, no icon index.

## How the values were read

Computed style was read in a headless Chromium at 1440×900, devicePixelRatio 2, on `https://en.wikipedia.org/wiki/Main_Page` and on `https://en.wikipedia.org/wiki/Talking_to_Yourself`. Dark values were read in a second context after clicking the public Color Dark radio. The readings are in [raw/](raw/). Colour tokens are the Codex custom properties on the document, not samples from the quantised PNGs.

## What to distrust

- **Screenshots are 256-colour.** Flat UI colours survive. Photographs (the featured-article portrait, the news images) band. Read colours from [tokens.json](tokens.json), not from a PNG pixel.
- **The home-page content link computed at 25.92px.** That is the featured-article lead link, not body links. Article body links computed at 16px. Use the article reading for body links.
- **The main-page h1 computed at height 0.** The welcome heading is painted, and the article h1 computed at 28.8px / 39.6px. Use the article reading for the title role.
- **Codex did not expose border, font, radius, or spacing custom properties** in the dumped set (115 colour, background, shadow, and image-size variables). Radius and type come from computed style on the search field, the title, and body. Do not invent the rest of a spacing scale.
- **Hover, pressed, disabled, and loading were not read.** Codex publishes hover and active colour variables. Those are listed in `tokens.json` as declared variables, not as states this pass clicked.
- **Dark is a client preference, not the public default.** Light is checked on a fresh visit.
- **Linux Libertine and Source Serif 4 are not shipped.** The tokens name the computed stack.
- **There is no signed-in shell in this package.** The auth walls are empty.
- **The hCaptcha sentence on Create account is a notice.** No challenge widget was painted.

## Fonts

- **System sans** for body, chrome, search, and menus. Computed `font-family` is `sans-serif`. Not included.
- **Linux Libertine**, then Georgia, Times, Source Serif 4, serif, for the page title. Not included. The wordmark is an image, not this face.

## Coverage

| Item | Status |
|---|---|
| Page colour, ink, progressive, visited, canvas | Captured. [tokens.json](tokens.json), [screenshots/home-light-desktop.png](screenshots/home-light-desktop.png) |
| Night colour roles | Captured from Codex after Color Dark. [screenshots/home-dark-desktop.png](screenshots/home-dark-desktop.png) |
| Type roles | Captured for title, body, content, search, personal links. Other sizes not measured. |
| Search field and Search button | Captured default. |
| Main menu, Tools menu, language panel | Captured open. |
| Phone main page, phone article, phone menu | Captured. |
| Empty search and no-results search | Captured by URL. The header field was not typed in. |
| Login and signup walls | Captured empty. Stopped. |
| Light theme | Captured. It is the default. |
| Edit, history, talk, donate, sister projects | Not opened. |
| Hover, focus, pressed, disabled, loading | Not captured. |
