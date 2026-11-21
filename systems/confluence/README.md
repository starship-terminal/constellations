# Confluence

Confluence is Atlassian's knowledge and collaboration workspace. This package covers the public product site at https://www.atlassian.com/software/confluence and the signed-out login and signup walls, measured on 2026-11-22. No account was created. No site was created. Theme seen: light. Widths photographed: 1440 and 390 CSS px.

A 2026-11-22 pass mapped the public website into [site-tree.md](site-tree.md) and photographed the marketing pages plus the empty login and signup walls. Passkey, Google, Microsoft, Apple, and Slack were not clicked. The email field was not typed. `login-extracted` stays not-started. catalog.json was left alone. webapps-manifest.json was left alone.

The company homepage stays in `systems/atlassian`. This package does not edit that folder or `systems/jira`.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px site icon, resized from the Atlassian favicon |
| [DESIGN.md](DESIGN.md) | Colour, type, and control sizes from the readings |
| [tokens.json](tokens.json) | Measured colours, type, and radii |
| [style-guide.html](style-guide.html) | Light marketing and login swatches |
| [components.md](components.md) | Controls seen on the public pages and the walls |
| [patterns.md](patterns.md) | Marketing shell, pricing, login, signup stop |
| [site-tree.md](site-tree.md) | Which header and footer controls open which public page or wall |
| [login-review.json](login-review.json) | Empty login and signup walls. `login-extracted` is not-started |
| [raw/](raw/) | Computed-style readings and the shoot log |
| [screenshots/](screenshots/) | Marketing pages and the empty walls |
| [tools/](tools/) | How the shots were made |

## Brief

<!-- brief:start -->

Not generated. catalog.json was left alone, so `make brief` was not run for this package.

<!-- brief:end -->

## Health

<!-- health:start -->

Not graded. This pass maps the public site and does not register the package.

<!-- health:end -->

## How the values were read

Headless Chromium opened https://www.atlassian.com/software/confluence at 1440 CSS px and read `getComputedStyle` on the body, the h1, the header, the footer, Get it free, Sign in, the hero Sign up control, and the work-email field. The same browser opened https://id.atlassian.com/login and the Confluence signup wall and read the empty fields and the Continue and Sign up buttons. Photographs are 1440 by 900 and, for home, pricing, the phone menu, login, and signup, 390 by 844.

## What to distrust

Hover and pressed fills were not held. The header itself computed as transparent. The blue mark was sampled from the homepage screenshot at the left edge. The hero email field's own box is transparent. The visible grey pill is the wrapper, #f8f8f8, radius 25px. The login heading node that computed as 14px grey is the form block, not the visible "Log in to continue" title. Impressum was discarded because it prints a street address and a phone number.

## Fonts

Marketing body is Charlie Text. Display headings are Charlie Display. The login and signup walls use Atlassian Sans. Those faces are licensed to the product. The style guide falls back to system-ui.

## Coverage

| Item | Status |
|---|---|
| Colour roles, light | Captured in [tokens.json](tokens.json) from the marketing site and the login wall |
| Colour roles, dark | Not present on the public pages |
| Type roles | Captured. Charlie Display headings, Charlie Text body, Atlassian Sans on the walls |
| Spacing | Captured as control padding and the 68px header |
| Radii | Captured. Pill header button, 25px hero field, 3px login Continue, 6px signup button |
| Borders | Marketing buttons use a 2px transparent border. Login Continue has no border |
| Elevation | Not captured |
| Motion | Not captured |
| Sizing | Captured. Header button 40px, hero Sign up 48px, login Continue 40px, login field 36px |
| Layout | Captured as screenshots at 1440 and 390 |
| Button | Captured, default. Hover and pressed not held |
| Link | Captured |
| Text field | Captured, empty, on the homepage hero and both walls |
| Text area, select, checkbox, radio, switch | Remember me is a checkbox on the login wall. The rest were not inventoried |
| Menu | Features and Templates open as pages. Phone menu photographed |
| Card | Pricing plans photographed. Start free trial not clicked |
| App shell | Marketing shell captured. Signed-in shell not captured |
| Form validation | Not captured. No form was submitted |
| Empty login | Captured |
| Empty signup | Captured |
| Impressum | Discarded. Street address and phone number |
| Desktop 1440 and phone 390 | Homepage, pricing, login, and signup at both widths. Phone menu at 390. Other pages at 1440 |

## Do and don't

**The primary action is Atlassian blue.** Get it free, Sign up, and Continue are #1868db with white text. Do not paint them black.

**The header button is a pill.** Get it free uses a 10000px radius. Login Continue is a 3px radius. They are different controls.

**The hero field is a grey pill.** The work-email wrapper is #f8f8f8 with a 25px radius. The placeholder is `you@company.com`. Leave it empty.

**Stop at the empty wall.** Sign in and Get it free open an email field and identity buttons. Do not treat a filled field or a created site as part of this capture.

## Rebuild

Readings are in [raw/readings.json](raw/readings.json). [tokens.json](tokens.json) was written from those readings. There is no builder to regenerate them. catalog.json was left alone, so `make brief` and `make grade` were not run.
