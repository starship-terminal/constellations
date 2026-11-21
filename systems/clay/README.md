# Clay public surface

A token set and page captures for Clay's public marketing site at **https://www.clay.com/**. First capture of this product into `systems/clay/` on **2026-11-22**, signed out. Desktop is **1440 by 900** at devicePixelRatio 1. Phone is **390 by 844** at devicePixelRatio 2 (PNG width 780). The site tree is [site-tree.md](site-tree.md).

origin/main already had `systems/clay/`. That folder was the personal CRM at clay.earth, which 301s to me.sh. This pass replaces those files with the GTM product at clay.com. [systems/clay-earth](../clay-earth) still holds the me.sh capture and was not edited. `catalog.json` was left alone, so `login-extracted` stays `not-started` and this README's Brief and Health are hand-written.

The marketing site is Webflow and paints **one theme**. There is no theme control. The stylesheet declares **712 custom properties**. The login and signup walls are a separate app at app.clay.com (blueberry Continue button, split layout, demo art).

**Boundary.** Login and signup were photographed empty and the branch stopped. Nothing was typed. Nothing was submitted. Google was not clicked. The demo form was not opened. Contact's select was not opened. Checkout was not entered.

| File | What it is |
|---|---|
| [README.md](README.md) | This file. |
| [site-tree.md](site-tree.md) | Which header, menu, drawer, footer and wall controls open which pages, and where this pass stopped. |
| [login-review.json](login-review.json) | Empty login and signup walls. Probe stopped there. login-extracted is not-started. |
| [icon.png](icon.png) | The apple-touch icon from www.clay.com, scaled to 128px. |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds declared swatches, radii, and type. `light` holds the painted roles. |
| [DESIGN.md](DESIGN.md) | Hand-written from the measured tokens. Not regenerated, because that would rewrite the catalog. |
| [style-guide.html](style-guide.html) | A page that renders the swatches, the hero band, and the three button fills. |
| [components.md](components.md) | Component inventory and gaps. |
| [patterns.md](patterns.md) | How the public pages combine the components. |
| [components/](components/) | Element crops of the nav buttons, hero buttons, nav, heading, product menu, pricing card, and the empty auth fields. |
| [icons/](icons/) | `INDEX.tsv` only. UI SVGs were not exported. |
| [screenshots/](screenshots/) | Quantised page shots, desktop and phone. |
| [raw/](raw/) | The stylesheet readings and the login and signup probes. |
| [tools/](tools/) | `build_tokens.py`, `build_style_guide.py`, and the capture script under `tools/capture/`. |

## How the values were read

Computed style and the custom properties were read in headless Chromium on the live homepage, then written to [raw/css-vars.json](raw/css-vars.json). The Webflow sheet is `fs-clay.shared.6a0496afe097048308f6d1bf.0d84fff8d.min.css`. Colour tokens are the declared hex, or a computed `rgb()` converted to hex. The hero band `#005c44` and the auth Continue button `#0382f7` were sampled from the full-colour PNG before quantize, because the band is a painted illustration and the auth button lives on another origin. Radius and type tokens are the declared rem values, or the computed pixel size when that is what the page paints (the home h1 is 88px at 1440).

Menus, the search dialog, and the phone drawer were opened in the T3 preview browser and scaled from a 2x frame. Page shots are headless Chromium at devicePixelRatio 1.

## What to distrust

- **Screenshots are 256-colour.** Flat UI colours survive. The claymation hero bands. Read colours from the tokens and from [raw/css-vars.json](raw/css-vars.json), not from a PNG pixel.
- **The hero band is sampled.** `#005c44` is a flat pixel in the green band, not a declared token. The illustration around it is artwork.
- **Hover, pressed, disabled, and loading were not read.** Do not invent them.
- **Annual pricing is the painted state.** Monthly was not switched.
- **Login is a different system.** The Continue button is blueberry `#0382f7`. It is not the marketing black pill.
- **The login panel's table is demo art.** The names on that card are the site's illustration, not an account.
- **Roobertvf is not shipped.** The tokens name the family.
- **Blog and changelog full sheets were not kept.** Those pages are longer than 40,000 CSS px. The package keeps the first viewport.

## Fonts

- **Roobertvf** (variable, 300 to 900) for marketing UI, headings, and body. The site serves it. It is licensed and not included. Fallback in the token is Arial, sans-serif.
- **Roobert mono** is the declared secondary family. It was not the painted body.
- **Canela Web** is declared and was not the painted h1.
- **Phosphor** is the icon font, loaded from unpkg. The glyphs were not copied.

## Coverage

| Item | Status |
|---|---|
| Colour roles | Captured from declared swatches and computed button, hero, and body colours. One theme. |
| Type roles | Captured. Desktop computed size for the home h1 and body. |
| Spacing | Button padding measured. The fluid section scale is in raw/css-vars.json and was not tokenised step by step. |
| Radii | Declared scale plus painted 12px buttons. |
| Borders | Field borders were not isolated. Grey-200 is the declared quiet border. |
| Elevation | The nav pill and the search dialog sit above the page. Shadow values were not tokenised. |
| Motion | Not measured. Reduced motion was not emulated. |
| Button | Default primary, secondary, hero, and auth measured at rest. Hover, focus, pressed, disabled, and loading not measured. |
| Link | Nav and footer links observed. Hover not measured. |
| Text field | Signup and login fields and the search field measured empty. Nothing typed. |
| Text area, checkbox, radio, switch | Not present on the measured pages. |
| Select | Present on pricing and contact. Not opened. |
| Tabs | Pricing Monthly/Annual observed. Annual painted. Monthly not switched. Search/Ask AI observed. Ask AI not started. |
| Menu | Product, Solutions, Resources, Company, and the phone drawer captured. |
| Dialog | Command-K search captured empty. |
| Card | Pricing cards captured. |
| Badge | Recommended and Save 10% observed. |
| Avatar, list row, table, toast, tooltip | Not present, except demo art on the auth wall. |
| 404 | Captured. |
| Themes | Light only. No dark theme on the public site. |
| Widths | Captured. Desktop 1440 and phone 390. Home and pricing at both widths. |
| Login and signup walls | Captured empty. Stopped there. `login-extracted` is not-started. |
| Signed-in app | Not captured. |

## Do and don't

1. **Do paint the page in oat paper.** The declared page colour is `#fefdfb` (`light.color.bg.page`).
2. **Do set display type in Roobertvf.** The home h1 is 88px, weight 575, tracking -0.04em, ivory on the green band.
3. **Do use a black pill for the nav primary.** "Start free trial" is `#000000` with white text, 12px radius, 39px tall.
4. **Do use chartreuse for the hero secondary.** "Get a demo" on the green band is `#cbd810` with black text.
5. **Do keep the nav in a white pill.** Logo, four menus, Pricing, search, Log in, demo, trial.
6. **Don't style the app from the marketing buttons.** Login Continue is `#0382f7` on a split card.
7. **Don't invent a dark theme.** None was on the public site.
8. **Don't follow signup, demo, or checkout from this package.** Those flows were not entered.
9. **Don't ship Roobertvf or the wordmark.** The tokens name the family. The font file and the logo stay on the site.

## Health

<!-- health:start -->

Not graded. This PR does not edit `catalog.json`, so `make grade` cannot attach a scorecard row. Coverage gaps are in the table above.

Layout: `icons/` holds an index only. No SVG set was lifted. The wordmark and Phosphor glyphs stay in the screenshots.

<!-- health:end -->

## Brief

<!-- brief:start -->

Read [tokens.json](tokens.json) before designing in this style. The catalog entry still describes the old clay.earth capture, so this Brief is hand-written and `make brief` has not rewritten it.

Home is a green band with an 88px Roobertvf headline and a chartreuse secondary pill. The nav primary is a black 12px pill. Pricing cards use blueberry, matcha, dragonfruit, and ube headers on white. The auth wall is a separate blueberry button.

<!-- brief:end -->

## Rebuild

```bash
cd systems/clay
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```

`build_tokens.py` checks the named swatches against [raw/css-vars.json](raw/css-vars.json). It does not rewrite tokens.json.
