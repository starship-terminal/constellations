# Superhuman public surface

A token set and page captures for Superhuman's public marketing site at **https://superhuman.com/**. First capture of this web site into `systems/superhuman/` on **2026-11-22**, signed out. Desktop is **1440 by 900** at devicePixelRatio 1. Phone is **390 by 844** CSS. The site tree is [site-tree.md](site-tree.md).

origin/main did not have `systems/superhuman/`. [systems/superhuman-ios](../superhuman-ios) and [systems/superhuman-mac](../superhuman-mac) were not edited. `catalog.json` was left alone, so `login-extracted` stays `not-started` and this README's Brief and Health are hand-written.

The marketing site paints **one light theme**. There is no theme control. The homepage stylesheet declared **no custom properties** on `:root`. The login and signup walls are a separate app at id.superhuman.com (SuperSans, violet Continue with email, empty email field, Google, Microsoft, and Apple). Mail admin stays on superhuman.com and offers Google and Microsoft only.

**Boundary.** Login and signup were photographed empty and the branch stopped. Nothing was typed. Nothing was submitted. Google, Microsoft, and Apple were not clicked. The contact form was photographed empty and not submitted. Pricing checkout was not entered. The Go, Mail, and Docs pricing pages were not opened.

| File | What it is |
|---|---|
| [README.md](README.md) | This file. |
| [site-tree.md](site-tree.md) | Which header, menu, drawer, footer and wall controls open which pages, and where this pass stopped. |
| [login-review.json](login-review.json) | Empty login and signup walls. Probe stopped there. login-extracted is not-started. |
| [icon.png](icon.png) | The apple-touch icon from superhuman.com, scaled to 128px. |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds measured swatches, radii, and type. `light` holds the painted roles. |
| [DESIGN.md](DESIGN.md) | Hand-written from the measured tokens. Not regenerated, because that would rewrite the catalog. |
| [style-guide.html](style-guide.html) | A page that renders the swatches and the two button fills. |
| [components.md](components.md) | Component inventory and gaps. |
| [patterns.md](patterns.md) | How the public pages combine the components. |
| [icons/](icons/) | `INDEX.tsv` only. UI SVGs were not exported. |
| [screenshots/](screenshots/) | Quantised page shots, desktop and phone. |
| [raw/](raw/) | The computed-style readings and the login and signup probes. |
| [tools/](tools/) | `build_tokens.py` checks `tokens.json` against the readings. The capture script is under `tools/capture/`. |

## How the values were read

Computed style was read in headless Chromium on the live homepage, the pricing page, and the identity wall, then written to [raw/](raw/). Colour tokens are those `rgb()` values converted to hex. The Mail promo bar lilac was sampled from the full-colour PNG before quantise, and the token says so. Radius and type tokens are the computed pixel sizes.

Menus, the phone drawer, and the page shots are headless Chromium. The T3 preview confirmed the live nav and the cookie sheet before the script ran. The preview pane was 1169 CSS pixels wide, so the committed desktop shots are the headless 1440 captures.

The cookie sheet is Transcend's `#transcend-consent-manager`. It paints from a closed shadow. The script hid that node. Accept and Reject were not clicked.

## What to distrust

- **Screenshots are 256-colour.** Flat UI colours survive. The homepage hero video bands. Read colours from the tokens and from [raw/](raw/), not from a PNG pixel.
- **The homepage Get Superhuman control has a transparent fill.** The dark pill is the hero video. The measured action fill is the violet on pricing and on the identity wall.
- **The homepage declared no custom properties.** Do not invent a token scale from memory of the product.
- **The banner lilac is sampled, not computed.** It is marked that way in tokens.json.
- **Hover, pressed, disabled, and loading were not read.** Do not invent them.
- **Suite is the painted pricing page.** Go + Agents, Mail, and Docs pricing pages were not opened. Get Superhuman Free, Pro, and Business were not clicked.
- **Login is a different host.** SuperSans, not Super Sans VF. The violet button is the auth submit.
- **The homepage inbox is demo art.** The names in that illustration are the site's artwork, not an account.
- **Super Sans VF is not shipped.** The tokens name the family.
- **Phone devicePixelRatio is 1.** The script requested 2. The sidecar records 1. The 390 shot is 390 CSS pixels wide.

## Fonts

- **Super Sans VF** for marketing UI, headings, and body. The site serves it. It is licensed and not included. Fallback in the token is system-ui, sans-serif.
- **SuperSans** is the painted auth-wall family.

## Coverage

| Item | Status |
|---|---|
| Colour roles | Captured from computed style. One theme. Banner lilac is sampled. |
| Type roles | Captured. Desktop computed size for the home h1, the pricing h1, prices, and body. |
| Spacing | Pricing button padding measured. The page scale was not tokenised step by step. |
| Radii | Painted 12px on pricing, identity, and the hero control. |
| Borders | Identity field is 1px at #dedbd5. Hero control is 1px at white 12%. |
| Elevation | Not measured. Menus sit over the page. |
| Motion | Not measured. Reduced motion was not emulated. |
| Button | Default primary measured at rest on pricing and the identity wall. Hover, focus, pressed, disabled, and loading not measured. |
| Link | Nav and footer links observed. Hover not measured. |
| Text field | Signup and login email fields measured empty. Contact and store search photographed empty. Nothing typed. |
| Text area | Not present, except a hidden reCAPTCHA textarea left empty. |
| Select | Store and contact selects photographed closed. Not opened. |
| Checkbox, radio, switch | Not present on the measured pages. |
| Tabs | Not present on the measured pages. What's new filters photographed closed. |
| Menu | Products, Solutions, AI, Resources, Pricing, Sign in, and the phone drawer captured. |
| Dialog | Not opened. Cookie Settings not opened. |
| Card | Pricing cards captured. |
| Badge | Best value observed. |
| Avatar, list row, table, toast, tooltip | Not present, except demo art on the homepage. |
| 404 | Captured. |
| Themes | Light only. No dark theme on the public site. |
| Widths | Captured. Desktop 1440 and phone 390 for the homepage. Other pages at 1440 only. |
| Login and signup walls | Captured empty. Stopped there. `login-extracted` is not-started. |
| Signed-in app | Not captured. |

## Do and don't

- Use one violet pill for the primary action. The secondary action is a quiet outline.
- Keep marketing pages on #f2f0eb with #292827 ink. The footer is #421d24 with white type.
- Treat the homepage inbox as illustration. Do not read it as a signed-in product screen.
- Do not style the auth wall from the hero button. The wall is SuperSans on #fcfaf7, with identity-provider rows above an empty email field.
- Do not invent a dark theme. The public site did not paint one.

## Brief

Hand-written because `catalog.json` was left alone. Superhuman's public site is a warm paper page, ink type in Super Sans VF, and a violet pill for the action. The homepage hero is a video. Sign in is a menu of Go, Mail, and Docs, and each one stops at an empty wall.

## Health

Not graded. `catalog.json` was left alone, so `make grade` was not run for this package.
