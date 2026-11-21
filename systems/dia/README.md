# Dia public surface

A token set and page captures for Dia's public marketing site at **https://www.diabrowser.com/**. First capture of this product into `systems/dia/` on **2026-11-22**, signed out. Desktop is **1440 by 900** at devicePixelRatio 1. Phone is **390 by 844** at devicePixelRatio 2 (PNG width 780). The site tree is [site-tree.md](site-tree.md).

origin/main did not have `systems/dia/`. This is a new package. `catalog.json` was left alone, so `login-extracted` stays `not-started` and this README's Brief and Health are hand-written.

The marketing site paints **one theme**. There is no theme control. The homepage hero is a yellow photograph. Inner pages sit on cream `#FBFAF6`. The stylesheet declares **56 custom properties** that are not Tailwind resets.

**Boundary.** No public login or signup wall exists. `/login` and `/signup` are the 404. `auth.diabrowser.com` returned an empty document. Nothing was typed. Nothing was submitted. No identity provider was clicked. The help chat was opened and discarded. The download binary was not kept.

| File | What it is |
|---|---|
| [README.md](README.md) | This file. |
| [site-tree.md](site-tree.md) | Which header, drawer, footer and download controls open which pages, and where this pass stopped. |
| [login-review.json](login-review.json) | The login and signup probe. No wall. login-extracted is not-started. |
| [icon.png](icon.png) | The apple-touch icon from www.diabrowser.com, composited on cream, scaled to 128px. |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds declared swatches, radii, and type. `light` holds the painted roles. |
| [DESIGN.md](DESIGN.md) | Hand-written from the measured tokens. Not regenerated, because that would rewrite the catalog. |
| [style-guide.html](style-guide.html) | A page that renders the swatches, the hero band, and the download pill. |
| [components.md](components.md) | Component inventory and gaps. |
| [patterns.md](patterns.md) | How the public pages combine the components. |
| [components/](components/) | Crops of the nav pill, the download pill, the apps heading, and the 404 button. |
| [icons/](icons/) | `INDEX.tsv` only. UI SVGs were not exported. |
| [screenshots/](screenshots/) | Quantised page shots, desktop and phone. 17 PNGs. |
| [raw/](raw/) | The stylesheet readings and the login, signup, and auth probes. |
| [tools/](tools/) | `build_tokens.py`, `build_style_guide.py`, and the capture script under `tools/capture/`. |

## How the values were read

Computed style and the custom properties were read in headless Chromium on the live homepage, then written to [raw/css-vars.json](raw/css-vars.json). Colour tokens are the declared hex, or a computed colour. The hero `#DCB017` was sampled from the full-colour PNG before quantize. Radius and type tokens are the computed pixel sizes at 1440.

The phone drawer was opened in headless Chromium at 390 by 844, devicePixelRatio 2. Page shots are the same browser at devicePixelRatio 1.

## What to distrust

- **Screenshots are 256-colour.** Flat UI colours survive. The yellow hero bands. Read colours from the tokens and from [raw/css-vars.json](raw/css-vars.json), not from a PNG pixel.
- **The hero yellow is sampled.** `#DCB017` is a flat pixel in the photograph, not a declared token. `--yellow` is `#FFB005`, a different colour.
- **Hover, pressed, disabled, and loading were not read.** `--get-dia-button-hover` is declared and was not hovered. Do not invent the rest.
- **The home h1 size is the 1440 reading.** It is fluid. Do not treat 39px as the phone size.
- **There is no public account chrome.** Do not design a signed-in shell from these pages.
- **The product illustrations are marketing art.** Names on the homepage demo are the site's illustration, not an account.
- **Exposure, ABC Oracle, and ABC Favorit Mono are not shipped.** The tokens name the families.

## Fonts

- **Exposure VAR** for the homepage headline. The site serves it from `/fonts/205TF-Exposure-[0].woff2`. It is licensed and not included. Fallback in the token is serif.
- **ABC Oracle** for UI and body. Served as `/fonts/ABCOracle-Regular.woff2`. Fallback is Helvetica, sans-serif.
- **ABC Favorit Mono** for footer column labels. Fallback is monospace.

## Coverage

| Item | Status |
|---|---|
| Colour roles | Captured from declared swatches and computed body, hero, and button colours. One theme. |
| Type roles | Captured. Desktop computed size for the home h1, nav, button, and footer label. |
| Spacing | Button horizontal padding measured at 24px. The rest of the scale was not tokenised. |
| Radii | Home pill 9999px. Menu button 20px. |
| Borders | `--stroke-light` and `--stroke-medium` declared. Not isolated on a control. |
| Elevation | Nav pill sits on the hero. Shadow values were not tokenised. |
| Motion | Not measured. Reduced motion was requested in the capture browser and not compared. |
| Button | Download pill and 404 button measured at rest. Hover, focus, pressed, disabled, and loading not measured. |
| Link | Nav and footer links observed. Security sidebar link is blue. Hover not measured. |
| Text field | Not present on the kept pages. The help chat field was empty and the shot was discarded. Nothing typed. |
| Text area, checkbox, radio, switch, select | Not present on the measured pages. |
| Tabs | Not present. |
| Menu | Phone drawer captured. Desktop has no menu, only the pill. |
| Dialog | Not present. |
| Card | Featured app cards captured. |
| Badge, avatar, list row, table, toast, tooltip | Not present. |
| 404 | Captured. |
| Themes | Light only. No dark theme on the public site. |
| Widths | Captured. Desktop 1440 and phone 390. Home and apps at both widths. Home menu at 390. |
| Login and signup walls | Not present. `/login` and `/signup` are the 404. Auth host was empty. `login-extracted` is not-started. |
| Signed-in app | Not captured. |
| Download | Public. `/download` and `/download/thanks`. Binary not kept. |

## Do and don't

1. **Do paint inner pages in cream.** The declared page colour is `#FBFAF6` (`light.color.bg.page`).
2. **Do set the home headline in Exposure, white, on the yellow hero.** The home h1 is 39px at 1440, weight 500, tracking -1.55px.
3. **Do use a black pill for download.** "Download Dia for free" is `#000000` with `#F8F8F8` text and a 9999px radius.
4. **Do keep the nav in a white pill.** Logo, What's New, Apps, Security. No login link.
5. **Don't treat `--yellow` as the hero.** The hero sample is `#DCB017`. `--yellow` is `#FFB005`.
6. **Don't invent a dark theme.** None was on the public site.
7. **Don't invent a login form.** The public host has no one.
8. **Don't ship Exposure, ABC Oracle, or the wordmark.** The tokens name the families. The font files and the logo stay on the site.

## Health

<!-- health:start -->

Not graded. This PR does not edit `catalog.json`, so `make grade` cannot attach a scorecard row. Coverage gaps are in the table above.

Layout: `icons/` holds an index only. No SVG set was lifted. The wordmark stays in the screenshots.

<!-- health:end -->

## Brief

<!-- brief:start -->

Read [tokens.json](tokens.json) before designing in this style. There is no catalog entry yet, so this Brief is hand-written and `make brief` has not rewritten it.

Home is a yellow band with a white Exposure headline and a black download pill. The nav is a white pill with three links. Inner pages are cream with black Exposure headlines. There is no public login.

<!-- brief:end -->

## Rebuild

```bash
cd systems/dia
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

`build_tokens.py` checks the named swatches against [raw/css-vars.json](raw/css-vars.json). It does not rewrite tokens.json.
