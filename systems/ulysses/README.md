# Ulysses

Public marketing site for Ulysses, the writing app for Mac, iPad, and iPhone. Captured signed out on 2026-11-22 from [https://ulysses.app/en/](https://ulysses.app/en/).

This is a first capture. `catalog.json` was left alone.

**What was captured.** The homepage, pricing, the footer pages on `ulysses.app`, a 404, the phone homepage with the nav drawer open and closed, and the empty volume-licensing login and signup walls.

**Where.** Marketing pages are `ulysses.app`. Pricing is public: $39.99 per year or $5.99 per month in the U.S., sold through the App Store and Setapp. The writing app has no web login. Volume licensing lives at `license.ulysses.app`.

**Boundary.** Login and signup were photographed empty and the branch stopped. Nothing was typed. Nothing was submitted. Continue to Checkout was not clicked. The country select was not opened. The contact and newsletter forms were photographed empty and not submitted. `login-extracted` is `not-started`.

| File | What it is |
|---|---|
| [README.md](README.md) | This file. |
| [site-tree.md](site-tree.md) | Which header, drawer, footer and wall controls open which pages, and where this pass stopped. |
| [login-review.json](login-review.json) | Empty login and signup walls. Probe stopped there. login-extracted is not-started. |
| [icon.png](icon.png) | The apple-touch icon from ulysses.app, scaled to 128px. |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds measured swatches, radius, and type. `light` holds the painted roles. |
| [DESIGN.md](DESIGN.md) | Hand-written from the measured tokens. Not regenerated, because that would rewrite the catalog. |
| [style-guide.html](style-guide.html) | A page that renders the swatches and the yellow outline button. |
| [components.md](components.md) | Component inventory and gaps. |
| [patterns.md](patterns.md) | How the public pages combine the components. |
| [icons/](icons/) | `INDEX.tsv` only. UI SVGs were not exported. |
| [screenshots/](screenshots/) | Quantised page shots, desktop and phone. |
| [raw/](raw/) | The computed-style readings and the login and signup probes. |
| [tools/](tools/) | `build_tokens.py` checks `tokens.json` against the readings. The capture script is under `tools/capture/`. |

## How the values were read

Computed style was read in headless Chromium on the live homepage, the pricing page, and the volume-licensing login wall, then written to [raw/](raw/). Colour tokens are those `rgb()` values converted to hex. Radius and type tokens are the computed pixel sizes.

Page shots are headless Chromium at 1440×900, and the homepage also at 390×844 with deviceScaleFactor 2. The T3 preview confirmed the live nav, pricing, and the empty login wall before the script ran. The preview pane was 1169 CSS pixels wide, so the committed desktop shots are the headless 1440 captures.

## What to distrust

- **Screenshots are 256-colour.** Flat UI colours survive. Product photographs on the homepage band. Read colours from the tokens and from [raw/](raw/), not from a PNG pixel.
- **The homepage hero is a product photograph.** The names and the draft text in that illustration are the site's artwork, not an account.
- **The action is an outline.** Get Ulysses on the dark section, Back to Homepage, and Log In all paint a 2px yellow border on a transparent fill. Do not invent a filled yellow pill.
- **`:root` declares a Bootstrap palette.** `--primary` is `#fc0`. The painted accent used here is the measured `#ffcc00` on the login submit. The two are the same yellow at 8-bit. The rest of that palette (blue, indigo, purple) was declared and not painted on the pages opened.
- **Hover, pressed, disabled, and loading were not read.** Do not invent them.
- **The signup page is a purchase form.** Country was preselected by the site (Singapore in the preview). Nothing was typed. Checkout was not entered. Do not treat that page as a completed account.
- **Interstate is not shipped.** The tokens name the family. Adobe Typekit serves it.
- **Phone devicePixelRatio is 2.** The 390 shot is 780 PNG pixels wide.

## Fonts

- **Interstate** for marketing UI, headings, and body. The site serves it from Typekit. It is licensed and not included. Fallback in the token is system-ui, sans-serif.

## Coverage

| Item | Status |
|---|---|
| Colour roles | Captured from computed style. One theme. Page, ink, footer, accent, field, focus. |
| Type roles | Captured. Desktop computed size for the home h2, the home h1, the login title, nav, and body. |
| Spacing | Login field padding measured (6px 9.75px). The page scale was not tokenised step by step. |
| Radii | Painted 3px on the login field and the Log In submit. |
| Borders | Login submit is 2px `#ffcc00`. Focused email field is 2px `#ffe680`. |
| Elevation | Not measured. The phone drawer sits over a dimmed page. |
| Motion | Not measured. Reduced motion was not emulated. |
| Button | Default outline measured at rest on the login wall. Hover, focus, pressed, disabled, and loading not measured. |
| Link | Nav and footer links observed. Hover not measured. |
| Text field | Login email and password, and the signup email field, measured empty. Contact and newsletter photographed empty. Nothing typed. |
| Text area | Present on the contact page below the fold of the first viewport. Not measured. Nothing typed. |
| Select | Country select on the signup wall photographed closed. Not opened. |
| Radio | Contact subject radios photographed. General is selected by the page. Not changed. |
| Checkbox | Terms checkbox on the signup wall. Not checked. |
| Switch | Not present on the pages opened. |
| Tabs | Not present on the pages opened. |
| Menu | Phone drawer captured open and closed. Desktop nav has no dropdown. |
| Dialog | Not opened. |
| Card | Pricing feature list captured. |
| Badge | Apple Design Award Winner observed on the homepage. |
| Avatar, list row, table, toast, tooltip | Not present, except demo art on the homepage. |
| 404 | Captured. |
| Themes | Light only. No dark theme on the public site. |
| Widths | Captured. Desktop 1440 and phone 390 for the homepage. Other pages at 1440 only. |
| Login and signup walls | Captured empty. Stopped there. `login-extracted` is not-started. |
| Signed-in app | Not captured. The writing app is native. |

## Do and don't

- Use a yellow outline for the primary action. The fill stays transparent. The border is `#ffcc00`.
- Keep marketing pages on white with `#27272b` ink. The footer is `#262626` with yellow links and white column labels.
- Treat the homepage device screens as illustration. Do not read them as a signed-in product screen.
- Do not style a consumer web app from this package. The only account wall is volume licensing, and it stops at an empty email and password.
- Do not invent a dark theme. The public site did not paint one.

## Brief

Hand-written because `catalog.json` was left alone. Ulysses's public site is a white page, ink type in Interstate, and a yellow outline for the action. The homepage hero is a photograph of the Mac, iPad, and iPhone app. Pricing is public. Sign-in is a volume-licensing wall, and this pass stopped there.

## Health

Not graded. `catalog.json` was left alone, so `make grade` was not run for this package.
