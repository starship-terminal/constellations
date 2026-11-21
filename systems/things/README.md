# Things public surface

A token set and page captures for Things' public marketing site at **https://culturedcode.com/things/**. First capture of this product into `systems/things/` on **2026-11-22**, signed out. Desktop is **1440 by 900** at devicePixelRatio 1. Phone is **390 by 844** at devicePixelRatio 1. The site tree is [site-tree.md](site-tree.md).

origin/main did not have `systems/things/`. This is a new package. `systems/things-ios/` was left alone. `catalog.json` was left alone, so `login-extracted` stays `not-started` and this README's Brief and Health are hand-written.

The marketing site paints **one light scheme**. The homepage body is `#f2f5f7`. Inner pages such as Support and Cloud use white. The strong button is `#4f91fb` with white type. There is no theme switch.

**Boundary.** The site has no sign-in page. `/things/login/` is a 404, photographed empty. Newsletter and support search fields were left empty. Nothing was typed. Nothing was submitted. App Store badges were not clicked. `/things/download/` starts a file, which was not kept. The signed-in apps are not this site.

| File | What it is |
|---|---|
| [README.md](README.md) | This file. |
| [site-tree.md](site-tree.md) | Which header, footer, and page controls open which pages, and where this pass stopped. |
| [login-review.json](login-review.json) | No sign-in wall. The 404 and the empty newsletter field. login-extracted is not-started. |
| [icon.png](icon.png) | 128px raster of `apple-touch-icon.png`. |
| [tokens.json](tokens.json) | W3C tokens. `core` holds type, radius, and the button blue. `light` holds the painted roles. |
| [DESIGN.md](DESIGN.md) | Hand-written from the measured tokens. Not regenerated, because that would rewrite the catalog. |
| [style-guide.html](style-guide.html) | Swatches and the Back Home button. |
| [components.md](components.md) | What was on the signed-out pages. |
| [patterns.md](patterns.md) | How the homepage, support index, newsletter, and 404 are put together. |
| [components/](components/) | Empty of crops. Element shots are the full pages in `screenshots/`. |
| [icons/](icons/) | `INDEX.tsv` only. UI SVGs were not exported. |
| [screenshots/](screenshots/) | Quantised page shots. 16 PNGs. |
| [raw/](raw/) | The computed readings and the homepage link map. |
| [tools/](tools/) | `build_tokens.py` checks the token file against the readings. |

## How the values were read

Computed style was read in headless Chromium on the live homepage and the 404 at 1440, then written to [raw/measure.json](raw/measure.json). The page colour `#f2f5f7` was confirmed by pixel (10, 10) on the full-colour homepage PNG before quantize. The description colour `#44474b` and the watch-link colour `#5c9cf5` were confirmed the same way. `:root` declared no custom properties.

## What to distrust

- **Screenshots are 256-colour.** Flat UI colours survive. Photos and the app demos band. Read colours from the tokens and from [raw/measure.json](raw/measure.json), not from a PNG pixel.
- **The wordmark "Things" is an image.** `.hero-image` is 250 by 301. Do not treat the 24px computed size on the hidden `h1.hero-title` as the wordmark.
- **The button blue and the link blue are not the same.** Back Home and Subscribe are `#4f91fb`. Watch Introduction Video is `#5c9cf5`.
- **Hover, pressed, disabled, and loading were not read.** Do not invent them.
- **The hero description size is the 1440 reading.** Do not treat 24px as the phone size.
- **The app pictures are public demos.** They are not a signed-in account.
- **The family is the system stack.** ui-sans-serif, -apple-system, system-ui, Roboto. It is not shipped.

## Fonts

- **System sans** for body, nav, and buttons. Body 18px / 25.2px, weight 400. Nav 15px, weight 600. Back Home 16.56px, weight 700. Not included.
- **ui-monospace** for the 404 badge only. 13.5px, weight 700. Not included.

## Coverage

| Item | Status |
|---|---|
| Colour roles | Captured for page, text, text-soft, accent, and on-accent. One light scheme. |
| Type roles | Captured for body, the hero description, nav, the section heading, the button, and the support search field. |
| Spacing | Button padding measured: 6.9552px 16.56px. Search padding measured. No full scale. |
| Radii | Button 7.452px. Nav 6px. Field 6.4px. Search 9.5625px. Card 12px. Badge 5.4px. |
| Borders | Newsletter field uses a 1px border, rgb(223, 227, 232). Support cards use a 1px border, rgba(0, 28, 70, 0.06). |
| Elevation | Not measured. |
| Motion | Reduced motion was requested in the capture browser and not compared. |
| Button | Back Home and Subscribe measured at rest. Hover, focus, pressed, disabled, and loading not measured. |
| Link | Nav and the watch link observed. Hover not measured. |
| Text field | Newsletter email and the support search were on screen and left empty. Not typed. |
| Text area, select, checkbox, radio, switch | Not on the public pages that were opened. |
| Tabs | Not present. |
| Menu | No dropdown. The header is four links. |
| Dialog | Not opened. Watch Introduction Video was not played. |
| Card | Support article cards and the pricing platform cards captured. |
| Badge | 404 badge measured. App Store Awards badge photographed. |
| Avatar, list row, table, toast, tooltip | Not isolated. |
| 404 | Captured. "Oops! Page Not Found." |
| Themes | One light scheme. No switch. |
| Widths | Desktop 1440 and phone 390. Home at both. 404 at both. |
| Login and signup walls | No sign-in page. 404 captured. `login-extracted` is not-started. |
| Signed-in app | Not captured. |
| Download | `/things/download/` starts a file. The file was not kept. |

## Do and don't

1. **Do paint the homepage near `#f2f5f7`.** The body computed colour is `rgb(242, 245, 247)`.
2. **Do set the hero description in the system sans at 24px, weight 400.** The line height is 30px at 1440. The wordmark is an image.
3. **Do fill Back Home and Subscribe with `#4f91fb` and white type.** Weight 700. Radius is 7.452px.
4. **Do keep the watch link as its own blue.** That label is `#5c9cf5`, weight 600, not the button fill.
5. **Do paint support cards as a quiet blue wash.** The fill is `rgba(0, 52, 126, 0.04)` with a 12px radius.
6. **Do not invent a signed-in Things Cloud account from the marketing page.** The cloud page is public. Accounts are created in the apps.

## Brief

Hand-written. `make brief` was not run, because that rewrites the catalog.

Read [tokens.json](tokens.json) before designing in this style. The homepage is `#f2f5f7`. Text is `#303336`. The accent used on Back Home is `#4f91fb`. Body type is the system sans at 18/25.2. Controls are the same family at 16.56px, weight 700, radius 7.452px.

## Health

Hand-written. `make grade` was not run, because that rewrites the catalog.

Not graded. `login-extracted` is not-started. The signed-in apps were not entered.

## Rebuild

```bash
cd systems/things && python3 tools/build_tokens.py
```

`build_tokens.py` checks `tokens.json` against `raw/measure.json`. It does not fetch the site. `make design-md` was not run on this pass, because it rewrites the catalog.
