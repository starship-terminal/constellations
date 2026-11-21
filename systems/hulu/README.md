# Hulu

Hulu is the US streaming service from Hulu, LLC. This package is a public capture on 2026-11-22, signed out, from Singapore. `https://www.hulu.com/` returned 302 to Disney+ (`x-aka-user-geo: SG`). The pages that stayed on a Hulu host are the plan chooser, the empty login wall, the Help Center, and the press site. Desktop width was 1440 by 900. Phone width was 390 by 844. Nothing was typed, submitted, or signed in.

| File | What it holds |
|---|---|
| [README.md](README.md) | This file |
| [icon.png](icon.png) | 128 px site icon, resized from the published favicon |
| [DESIGN.md](DESIGN.md) | Copy of the measured tokens. Not written by `make design-md`, because that command needs a catalog.json entry and this pass does not edit catalog.json |
| [tokens.json](tokens.json) | Colour, type, and radius tokens |
| [style-guide.html](style-guide.html) | Specimens rendered from the tokens |
| [components.md](components.md) | Component inventory and gaps |
| [patterns.md](patterns.md) | Page patterns |
| [components/](components/) | Crops of SELECT, LOG IN, and the empty help search |
| [icons/](icons/) | Favicon source note |
| [screenshots/](screenshots/) | Public pages and the login, subscribe, and press walls |
| [raw/](raw/) | Computed styles that were read |
| [site-tree.md](site-tree.md) | Which control opens which page |
| [login-review.json](login-review.json) | What the login and subscribe walls ask for |
| [tools/](tools/) | Token check and the style-guide writer |

<!-- brief:start -->
## Brief

<!-- brief:end -->

<!-- health:start -->
## Health

<!-- health:end -->

## How the values were read

Headless Playwright opened the plan chooser at 1440 by 900, `deviceScaleFactor` 1. Computed styles were read on the body, the h1, LOG IN, and SELECT. Hover on SELECT was a real pointer move. Focus on LOG IN was `element.focus()`. The login email wall and the Help Center search were read the same way. The email field value length was 0.

The wordmark green is a pixel sample of the published favicon and the login wordmark image, `rgb(28, 231, 131)`. It is not a computed style. The token marks it Derived.

Phone shots were requested at 390 by 844 with `deviceScaleFactor` 2.

## What to distrust

This is not the signed-in player. `www.hulu.com` marketing paths redirected to Disney+ from Singapore. The plan chooser still served US prices.

SELECT hover was read as `rgba(4, 4, 5, 0.8)`. The resting fill was `rgb(4, 4, 5)`.

The plan page body is `#f7f7f9`. The login wall is a dark gradient behind a white card. The Help Center hero is dark. They are different surfaces.

The Help Center search border is `#15bc74`. The wordmark sample is `#1ce783`. They are not the same green.

No error, warning, or success colour was on the pages that were opened. Those roles are not in the tokens.

Spacing is not a named scale. Control height is on the measured buttons.

## Fonts

Graphik Web is the UI face on the plan chooser. The login heading uses Inspire. The email field and Continue computed as Arial. These are commercial faces. The files are not in this package.

## Coverage

| Item | Status | File |
|---|---|---|
| Colour, page and text | Captured | [tokens.json](tokens.json), [screenshots/home-light-default.png](screenshots/home-light-default.png) |
| Colour, accent | Captured | Help search border `#15bc74` |
| Colour, status | Not captured | No live error, warning, or success state was shown |
| Type, display and UI | Captured | Plan h1 and body |
| Type, code | Not present | No code sample on the public pages |
| Spacing scale | Not captured | No named spacing tokens were published |
| Radius | Captured | 1000px pill on SELECT, 4px on the email field |
| Elevation | Not captured | Computed box-shadow none on the measured controls |
| Motion | Not captured | Durations were not read |
| Button | Captured | [components/crops/button-select-default.png](components/crops/button-select-default.png) |
| Button hover | Captured | [screenshots/home-light-select-hover.png](screenshots/home-light-select-hover.png) |
| Button focus | Not captured | LOG IN focus computed as outline none |
| Link | Captured | LOG IN and Terms apply |
| Text field | Captured, empty | [screenshots/login-light-default.png](screenshots/login-light-default.png), [components/crops/field-search-empty.png](components/crops/field-search-empty.png) |
| Text area | Not present | Not on the public pages that were opened |
| Select | Not present | The plan tabs are labels, not a native select |
| Checkbox, radio, switch | Observed | Bundle/Save and Base Plans are checkboxes styled as tabs. Not a form control set |
| Tabs | Captured | Bundle/Save and Base Plans |
| Menu | Captured, press | Press header dropdowns. Not opened past the listed pages |
| Tooltip, toast, dialog | Not present | Not shown on the public pages |
| Card | Captured | Plan cards |
| Table | Captured | Press schedule |
| List row | Captured | Help articles |
| Avatar | Not present | Not on the signed-out pages |
| App shell | Captured, marketing | Plan header is wordmark plus LOG IN |
| Empty, loading, error | Not captured | Pages loaded. No empty catalog state was opened |
| Login wall | Captured, stopped | [login-review.json](login-review.json) |
| Subscribe wall | Captured, stopped | Same file |

## Do and don't

- Keep the plan page on `#f7f7f9`. SELECT is a black pill. The green is the wordmark and the help search border.
- Use a pill for SELECT. LOG IN on the plan header is text, not a filled button.
- Stop at the email wall and at SELECT. Do not treat the plan chooser as a completed signup.

## Rebuild

```bash
python3 systems/hulu/tools/build_tokens.py
python3 systems/hulu/tools/build_style_guide.py
python3 systems/hulu/tools/test_build_tokens.py
```
