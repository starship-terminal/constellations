# Google public surface

A token set and page captures for Google Search at **https://www.google.com/**. First capture of this product into `systems/google/` on **2026-11-22**, signed out. Desktop is **1440 by 900** at devicePixelRatio 1. Phone is **390 by 844** at devicePixelRatio 2 (PNG width 780). The site tree is [site-tree.md](site-tree.md).

origin/main did not have `systems/google/`. This is a new package. `catalog.json` was left alone, so `login-extracted` stays `not-started` and this README's Brief and Health are hand-written.

The homepage paints **one light theme**. `color-scheme` was `normal`. A dark `prefers-color-scheme` still painted white. Dark theme is a Settings row and was not switched.

**Boundary.** Sign in and create account were photographed empty. Nothing was typed. Next was not clicked. No identity provider was clicked. No search was submitted. Gmail, Maps, YouTube and Drive were not opened.

| File | What it is |
|---|---|
| [README.md](README.md) | This file. |
| [site-tree.md](site-tree.md) | Which header, menu, footer and phone controls open which pages, and where this pass stopped. |
| [login-review.json](login-review.json) | The empty login and signup probe. login-extracted is not-started. |
| [icon.png](icon.png) | The 128px Google "G" from `googleg_standard_color_128dp.png`. |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds measured colours, radii and type. `light` holds the painted roles. |
| [DESIGN.md](DESIGN.md) | Hand-written from the measured tokens. Not regenerated, because that would rewrite the catalog. |
| [style-guide.html](style-guide.html) | A page that renders the swatches, the search field, the quiet buttons and the Sign in pill. |
| [components.md](components.md) | Component inventory and gaps. |
| [patterns.md](patterns.md) | How the public pages combine the components. |
| [components/](components/) | Crops of the sign-in pill, the search field, the quiet buttons, the footer, the apps card, the settings menu and the login card. |
| [icons/](icons/) | `INDEX.tsv` only. UI SVGs were not exported. |
| [screenshots/](screenshots/) | Quantised page shots, desktop and phone. 18 PNGs. |
| [raw/](raw/) | The stylesheet readings and the login-wall measurements. |
| [tools/](tools/) | `build_tokens.py` and `build_style_guide.py`. |

## Brief

Hand-written. `make brief` was not run, because that reads catalog.json and this capture does not edit it.

Read [tokens.json](tokens.json) before designing in this style. The homepage is white, the search field is a 26px pill, quiet actions are `#f8f9fa`, and the only filled action is the Sign in pill at `#0b57d0`.

## Health

Hand-written. `make grade` was not run, because that writes a scorecard snapshot and the root catalog table.

No scorecard review was written. `login-extracted` is not-started. The signed-in app was not captured.

## How the values were read

Computed style and the named custom properties were read in headless Chromium on the live homepage, then written to [raw/css-vars.json](raw/css-vars.json). Colour tokens are those computed colours, or a declared hex. The footer `#ececed` was sampled from the full-colour PNG before quantize. Radius and type tokens are the computed pixel sizes at 1440.

The phone menu and the phone sign-in wall were opened in headless Chromium at 390 by 844, devicePixelRatio 2.

## What to distrust

- **Screenshots are 256-colour.** Flat UI colours survive. The logo and the About photograph band. Read colours from the tokens and from [raw/css-vars.json](raw/css-vars.json), not from a PNG pixel.
- **The footer colour is sampled.** `#ececed` is a flat pixel on the country row, not a named custom property.
- **Hover, pressed, disabled and loading were not held.** The Search button shadow was read while the pointer was over it.
- **Sign in and accounts Next are different blues.** `#0b57d0` is the homepage pill. `#1a73e8` is the accounts Next button.
- **There is no signed-in chrome.** Do not design an inbox, Drive, Maps or YouTube from these pages.
- **Google Sans Text is not shipped.** The token names the family the Sign in link computed.
- **Trending searches are public suggestions.** Names in that panel are the site's suggestions, not an account.

## Fonts

- **Arial** for body, the search field and the quiet buttons. A system font.
- **Google Sans Text** for the Sign in label, with Roboto, Helvetica and Arial as fallbacks. Licensed and not included.

## Coverage

| Item | Status |
|---|---|
| Colour roles | Captured from computed body, Sign in, search field, quiet button, promo link and the footer sample. One theme. |
| Type roles | Captured. Desktop computed size for body, field, button, Sign in and the sign-in heading. |
| Spacing | Button padding 16px. Sign in padding 10px 12px. The rest of the scale was not tokenised. |
| Radii | Field 26px. Quiet button 8px. Sign in pill. Accounts Next 4px. |
| Borders | Search field `#dadce0`. Declared hairline `#d2d2d2`. |
| Elevation | Field shadow and focused field shadow measured. |
| Motion | Not measured. Reduced motion was requested in the capture browser and not compared. |
| Button | Sign in and Google Search measured. Hover, pressed, disabled and loading not measured. |
| Link | Header, promo and footer links observed. Promo colour measured. |
| Text field | Homepage field measured empty and focused. Sign-in identifier photographed empty. Nothing typed. |
| Text area, checkbox, radio, switch | Not isolated. Advanced search has empty fields and native selects. Not submitted. |
| Tabs | Phone homepage shows ALL and IMAGES. Not measured as a component. |
| Menu | Settings menu, apps panel and phone menu captured. |
| Dialog | Voice dialog captured, then closed. |
| Card | Apps panel and sign-in card captured. |
| Badge, avatar, table, toast, tooltip | Not present on the kept pages. |
| Themes | Light only on the public homepage. Dark theme row was not switched. |
| Widths | Captured. Desktop 1440 and phone 390. Home, phone menu and phone sign-in wall. |
| Login and signup walls | Captured empty. `login-extracted` is not-started. |
| Signed-in app | Not captured. |
| Gmail, Maps, YouTube, Drive | Not this package. Links were not followed. |

## Do and don't

1. **Do paint the page white and put the only filled action in the Sign in pill.** The fill is `#0b57d0` (`light.color.action.fill`).
2. **Do keep Google Search and I'm Feeling Lucky quiet.** Face `#f8f9fa`, radius 8px, label `#202124`.
3. **Do draw the search field as a 26px pill with a 1px `#dadce0` border.** Focus opens suggestions. Do not invent a submitted results page from this package.
4. **Don't follow Sign in, Gmail, Maps, YouTube or Drive and call it this capture.** Those walls and products were the stop.
