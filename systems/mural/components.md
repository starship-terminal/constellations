# Mural components

Measured on the public site and the signed-out login, 1440 CSS px, light, on 2026-11-19. Colours are computed styles. A token name after a hex is the palette token with that value.

Screenshots of the controls sit in [components/crops/](components/crops/). Whole pages sit in [screenshots/](screenshots/).

## Buttons

| State | Size | Fill | Text | Radius | Border | Crop |
|---|---|---|---|---|---|---|
| Sign up free, rest | 154.5 x 40 | #00c27a `jade` | ABC Social 16/24 500, #000000 | 8px | none | [button-primary-default.png](components/crops/button-primary-default.png) |
| Sign up free, hover | 154.5 x 40 | #00c27a `jade` | same | 8px | none | [button-primary-hover.png](components/crops/button-primary-hover.png) |
| Book a demo, rest | 128.5 x 40 | transparent | ABC Social 16/24 500, #000000 | 8px | 2px solid #dce1e5 `grey100` | [button-outline-default.png](components/crops/button-outline-default.png) |
| Book a demo, hover | 128.5 x 40 | transparent | same | 8px | 2px solid #b8c1cc `grey200` | [button-outline-hover.png](components/crops/button-outline-hover.png) |
| Log in, rest | 416 x 40 | #e02935 `authRed` | ABC Social 14/20 700, #ffffff | 8px | none | [login-button-default.png](components/crops/login-button-default.png) |
| Log in, hover | 416 x 40 | #b3212a `authRedHover` | same | 8px | none | [login-button-hover.png](components/crops/login-button-hover.png) |

The navbar Sign up free control is a link, not a submit. Its label is weight 500. The link's own computed color is black because the label is a child. Hover did not change the green fill in the 450ms reading.

The Log in button was not clicked. Hover was a real pointer hover.

## Links

| Control | Size | Fill | Text | Radius | Crop |
|---|---|---|---|---|---|
| Pricing nav link, rest | 78.8 x 32 | transparent | ABC Social 16/24 300, #000000 | 8px, padding 8px 16px | [nav-link-default.png](components/crops/nav-link-default.png) |
| Pricing nav link, hover | 78.8 x 32 | #f0f0f0 `lightGrey` | same | 8px | [nav-link-hover.png](components/crops/nav-link-hover.png) |
| Sign up for free, auth | 128 x 45 | #ffffff | ABC Social 14/20 700, #48525b | 8px, inset 2px #dce1e5 | [auth-link-default.png](components/crops/auth-link-default.png) |

The auth link was not followed.

## Fields

| State | Size | Fill | Border | Text | Placeholder | Crop |
|---|---|---|---|---|---|---|
| Work email, rest | 416 x 40 | #ffffff | 2px solid #282e34 | ABC Social 14/20 400, #1b1f22 | #63707e | [text-field-default.png](components/crops/text-field-default.png) |
| Work email, clicked | 416 x 40 | #ffffff | 2px solid #282e34 | same | same | [text-field-focused.png](components/crops/text-field-focused.png) |
| Work email, keyboard focus | 416 x 40 | #ffffff | 2px solid #282e34, outline 2px solid #306ae3 | same | same | [text-field-focus-visible.png](components/crops/text-field-focus-visible.png) |
| Work email, filled then cleared | 416 x 40 | #ffffff | 2px solid #282e34 | same | same | [text-field-filled.png](components/crops/text-field-filled.png) |
| Hero email | 290 x 40 | #000000 | 2px solid #4f5457 | ABC Social 16/23 300, #ffffff | Enter your email | [hero-email-default.png](components/crops/hero-email-default.png) |
| Remember me | 20 x 20 | transparent | none on the input | | | [checkbox-default.png](components/crops/checkbox-default.png) |

The filled value was `design@example.com`. It was deleted. Nothing was submitted. The checkbox was not toggled. A click into the field did not paint the blue outline. Keyboard focus did: `outline: rgb(48, 106, 227) solid 2px`.

## Type

| Role | Face | Size | Weight | Line | Tracking | Color | Crop |
|---|---|---|---|---|---|---|---|
| Hero display | STK Bureau | 80px | 300 | 88px | -4px | #8c8c8c, with "Stand out." in #ffffff | [display-default.png](components/crops/display-default.png) |
| Hero lede | ABC Social | 18px | 300 | 27px | 0 | #ffffff | [lede-default.png](components/crops/lede-default.png) |
| Eyebrow | ABC Social | 14px | 300 | 15.4px | 3.5px, uppercase | #000000 | [eyebrow-default.png](components/crops/eyebrow-default.png) |
| Pricing title | STK Bureau | 64px | 300 | 70.4px | -3.2px | #000000 | [pricing-light-default.png](screenshots/pricing-light-default.png) |

## Cards and chrome

| Part | Size | Fill | Radius | Other | Crop |
|---|---|---|---|---|---|
| Navbar pill | 1360 x 64 | #ffffff | 16px | shadow from `--elevated-shadow` | [navbar-default.png](components/crops/navbar-default.png) |
| Pricing card content | 328 x 786 | #ffffff | 20px | padding 32px 24px, 3px white border | [plan-free-default.png](components/crops/plan-free-default.png) |
| Business price | | #00843f `muralGreen` | | STK Bureau figure | [price-figure.png](components/crops/price-figure.png) |

The Business card is marked MOST POPULAR. The badge text is ABC Social 10.4px, weight 400, tracking 0.32px. Its pill fill was not isolated from the card chrome, so the badge color is not tokenised.

## Gaps

- Dark theme: not present on the public pages or the signed-out login. Not captured.
- Signed-in workspace, mural canvas, templates inside the app, share dialog, comments: behind login. Not captured. Login and signup were not submitted.
- Select, radio, switch, tabs, toast, table, avatar, tooltip: not present on the pages that were opened. Not captured.
- Text area: not present on the login or the marketing hero. Not captured.
- Menu: the Product disclosure did not open a measurable list from the headless click. The open menu was not captured.
- Pricing call to action: the card actions did not match the text filter used in the pass. The cards themselves were measured. The action inside a plan card was not captured as its own crop.
- Checkbox selected, disabled, error, loading: the checkbox was left unchecked, and no error was provoked, because that would mean submitting the form. Not captured.
- Pressed: not forced. Hover was read with a real pointer where a control was on screen.
- Phone login and signup screenshots were saved, but the PNG is 780 x 1688 rather than the requested 390 x 844. The desktop login is the evidence for those controls.
- Motion: a dedicated reduced-motion probe was not run. Declared shadows and the hover border change were read. Whether the site honours `prefers-reduced-motion` is not captured.
- Proprietary fonts ABC Social and STK Bureau are not in the package. The tokens name Times New Roman and Arial as the fallbacks the stylesheets already declare.
