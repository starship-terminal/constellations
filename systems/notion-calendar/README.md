# Notion Calendar public surface

A token set and page captures for Notion Calendar's public marketing site. First capture of this web site into `systems/notion-calendar/` on **2026-11-22**, signed out. The requested URL `https://notion.com/product/calendar` redirected to **https://www.notion.com/product/calendar**. Desktop is **1440 by 900** at devicePixelRatio 1. Phone is **390 by 844** CSS. The site tree is [site-tree.md](site-tree.md).

origin/main did not have `systems/notion-calendar/`. [systems/notion](../notion) is the workspace marketing site and was not edited. [systems/notion-calendar-desktop](../notion-calendar-desktop) is the macOS app and was not edited. `catalog.json` was left alone, so `login-extracted` stays `not-started` and this README's Brief and Health are hand-written.

The marketing page paints **one light theme**. There is no theme switch. The homepage stylesheet declares hundreds of `--tatami-*` custom properties. The login and signup walls are a separate app at app.notion.com (empty email field, blue Continue, identity-provider rows).

**Boundary.** Login and signup were photographed empty and the branch stopped. Nothing was typed. Nothing was submitted. Google, Apple, Microsoft, Passkey, and SSO were not clicked. The sales form was photographed empty and not submitted. The macOS download link is a file and was not saved. Pricing checkout was not entered. Pay monthly was not switched.

| File | What it is |
|---|---|
| [README.md](README.md) | This file. |
| [site-tree.md](site-tree.md) | Which header, menu, drawer, footer and wall controls open which pages, and where this pass stopped. |
| [login-review.json](login-review.json) | Empty login and signup walls. Probe stopped there. login-extracted is not-started. |
| [icon.png](icon.png) | 128px PNG from the 512px apple-touch icon at `/front-static/logo-ios.png`. |
| [tokens.json](tokens.json) | W3C DTCG tokens. `core` holds measured swatches, radius, and type. `light` holds the painted roles. |
| [DESIGN.md](DESIGN.md) | Hand-written from the measured tokens. Not regenerated, because that would rewrite the catalog. |
| [style-guide.html](style-guide.html) | A page that renders the swatches and the primary button fill. |
| [components.md](components.md) | Component inventory and gaps. |
| [patterns.md](patterns.md) | How the public pages combine the components. |
| [screenshots/](screenshots/) | Quantised page shots, desktop and phone. |
| [raw/](raw/) | The stylesheet readings and the login and signup probes. |
| [tools/](tools/) | `build_tokens.py` checks `tokens.json` against `raw/css-vars.json`. The capture script is under `tools/capture/`. |

## How the values were read

Computed style and the custom properties were read in headless Chromium on the live calendar page, then written to [raw/css-vars.json](raw/css-vars.json). Colour tokens are declared hex values, or the computed button fill. The home h1 is 64px at 1440. The nav primary is 36px tall with an 8px radius.

Menus, the phone drawer, and the page shots are headless Chromium. The T3 preview confirmed the live nav before the script ran. In that pane, Product, How to, and Enterprise are links. Headless Chromium painted Product as a dropdown. The site tree follows the preview.

## What to distrust

- **Screenshots are 256-colour.** Flat UI colours survive. The hero illustration bands. Read colours from the tokens and from [raw/css-vars.json](raw/css-vars.json), not from a PNG pixel.
- **Hover, pressed, disabled, and loading were not read.** Do not invent them.
- **Pay yearly is the painted pricing state.** Pay monthly was not switched. Sign up and Get started were not clicked.
- **Login is a different system.** The blue Continue button is the auth submit, not the marketing black pill.
- **The homepage calendar is demo art.** The names in that illustration are the site's artwork, not an account.
- **NotionInter is not shipped.** The tokens name the family. Fallback is Inter.
- **Shared Notion pages were not recaptured.** Product, How to, Enterprise, blog, and customers live in [systems/notion](../notion).
- **Phone devicePixelRatio is 1.** The 390 shot is 390 CSS pixels wide. It is not a 2x retina PNG.
- **The var dump is capped at 400 names.** Later custom properties are not in the raw file.

## Fonts

- **NotionInter** for marketing UI, headings, and body. The site serves it. It is licensed and not included. Fallback in the token is Inter, then system-ui.

## Coverage

| Item | Status |
|---|---|
| Colour roles | Captured from declared Tatami swatches and computed button and body colours. One theme. |
| Type roles | Captured. Desktop computed size for the home h1 and body. |
| Spacing | Primary button padding measured (4px 14px). The rest of the scale was not tokenised. |
| Radii | Declared Tatami scale plus the painted 8px primary button. |
| Borders | Declared 1px solid. Not measured per control. |
| Elevation | Not measured. |
| Motion | Not measured. Reduced motion was requested in the capture context. |
| Button | Default primary measured at rest. Hover, focus, pressed, disabled, and loading not measured. |
| Link | Nav and footer links observed. Hover not measured. |
| Text field | Signup, login, and sales email fields measured empty. Nothing typed. |
| Text area | Not present on the photographed pages. |
| Select | macOS Universal on the download page. Not switched. |
| Checkbox, radio, switch | Not present on the measured pages. |
| Tabs | Pricing Pay monthly and Pay yearly. Yearly painted. Monthly not switched. |
| Menu | Resources panel and the phone drawer captured. |
| Dialog | Not opened. Cookie settings not opened. |
| Card | Pricing cards and help topic cards captured. |
| Badge | Recommended on Business pricing. |
| Avatar, list row, table, toast, tooltip | Not present, except demo art on the homepage. |
| Themes | Light only. No dark theme on the public calendar page. |
| Widths | Captured. Desktop 1440 and phone 390 for the homepage. Other pages at 1440 only. |
| Login and signup walls | Captured empty. Stopped there. `login-extracted` is not-started. |
| Signed-in calendar | Not captured. `calendar.notion.so` was not entered. |
| Download | Public download page captured. The installer file was not saved. |

## Do and don't

- Use one black pill for the calendar primary action. The secondary action is a quiet outline button.
- Keep the page on white with near-black ink. Blue is the auth Continue and the pricing Get started, not the calendar hero button.
- Treat the homepage calendar as illustration. Do not read it as a signed-in product screen.
- Do not style the auth wall from the marketing pill. The wall is a blue Continue under an empty email field, with identity-provider rows below.
- Do not invent a dark theme. The public calendar page did not paint one.
