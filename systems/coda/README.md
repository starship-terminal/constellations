# Coda

Coda is a collaborative doc and team workspace. The public site now brands it Superhuman Docs and still answers on https://coda.io/. This package covers the public marketing site and the signed-out login and signup walls, measured on 2026-11-22. No account was created. No doc was created. Theme seen: light. Widths photographed: 1440 and 390 CSS px.

A 2026-11-22 pass mapped the public website into [site-tree.md](site-tree.md) and photographed the marketing pages plus the empty login and signup walls. Google, Microsoft, Apple, and SSO were not clicked. The email field was not typed. `login-extracted` stays not-started. catalog.json was left alone.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px site icon, resized from the marketing favicon |
| [DESIGN.md](DESIGN.md) | Colour, type, and control sizes from the readings |
| [tokens.json](tokens.json) | Measured colours, type, and radii |
| [style-guide.html](style-guide.html) | Light marketing and login swatches |
| [components.md](components.md) | Controls seen on the public pages and the walls |
| [patterns.md](patterns.md) | Marketing shell, pricing, login, signup stop |
| [site-tree.md](site-tree.md) | Which header and footer controls open which public page or wall |
| [login-review.json](login-review.json) | Empty login and signup walls. `login-extracted` is not-started |
| [raw/](raw/) | Computed-style readings and the shoot log |
| [screenshots/](screenshots/) | Marketing pages and the empty walls |
| [tools/](tools/) | The site-tree check |

## Brief

<!-- brief:start -->

Not generated. catalog.json was left alone, so `make brief` was not run for this package.

<!-- brief:end -->

## Health

<!-- health:start -->

Not graded. This pass maps the public site and does not register the package.

<!-- health:end -->

## How the values were read

An incognito preview tab opened https://coda.io/ at 1440 CSS px and read `getComputedStyle` on the body, the h1, the header, the footer, the rebrand banner, and the Get started and Contact sales controls. The same tab opened https://coda.io/signin and https://coda.io/signup and read the empty work-email field and the Continue button. Headless Chrome photographed the public pages at 1440 by 900, and the homepage, pricing, login, and signup at 390 by 844.

## What to distrust

Hover and pressed fills were not held. The header Get started link itself computed as transparent. The visible black pill is the inner label, #141413. Chart custom properties (`--kr-blue-chart` and the rest) were declared and were not used on a captured control, so they are not tokens. The Startups nav link returns a page-not-found. Hire a Services Partner redirected to a Forbidden page, and that shot was discarded. Help center stopped on a security check, and that shot was discarded.

## Fonts

Marketing body is Super Sans VF. Display headings are Calibre-R. Button labels and the rebrand banner use Inter. Those faces are licensed to the product. The style guide falls back to system-ui.

## Coverage

| Item | Status |
|---|---|
| Colour roles, light | Captured in [tokens.json](tokens.json) from the marketing site and the login wall |
| Colour roles, dark | Not present on the public pages |
| Type roles | Captured. Calibre-R display, Super Sans VF body, Inter on buttons |
| Spacing | Captured as control padding and the 36px banner |
| Radii | Captured. 4px field, 8px header button, 12px hero button |
| Borders | Login Continue is 1px #714cb6. Marketing buttons have no border |
| Elevation | Not captured |
| Motion | Not captured |
| Sizing | Captured. Header button 40px, hero button 62px, login field 36px |
| Layout | Captured as screenshots at 1440 and 390 |
| Button | Captured, default. Hover and pressed not held |
| Link | Captured |
| Text field | Captured, empty, on the login and signup walls |
| Text area, select, checkbox, radio, switch | Not inventoried on the photographed marketing pages |
| Menu | Product, Solutions, and Resources open as pages |
| Card | Pricing plans photographed on the redirected pricing page |
| App shell | Marketing shell captured. Signed-in shell not captured |
| Form validation | Not captured. No form was submitted |
| Empty login | Captured |
| Empty signup | Captured |
| Help center | Stopped at a captcha wall |
| Desktop 1440 and phone 390 | Homepage, pricing, login, and signup at both widths. Other pages at 1440 |

## Do and don't

**The primary action is near-black.** Get started is #141413 with white text and an 8px radius. Do not paint it in the orange banner colour.

**Orange is the rebrand banner, not the button.** The banner is #ee5a29. The page body is white. The header is #fcfaf7. The footer is #fff6ec.

**Login Continue is purple.** The empty-wall Continue button is #714cb6. It is not the marketing primary.

**Stop at the empty wall.** Get started and Sign up open an email field and identity buttons. Do not treat a filled field or a created doc as part of this capture.

## Rebuild

Readings are in [raw/readings.json](raw/readings.json). [tokens.json](tokens.json) was written from those readings. There is no builder to regenerate them. catalog.json was left alone, so `make brief` and `make grade` were not run.
