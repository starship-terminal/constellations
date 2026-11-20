# Components

Public marketing controls on overflow.io, plus the signed-out app shell at
`/n/signin` and `/n/signup`. Values are computed styles from 2026-11-19.
Crops are in [components/crops/](components/crops/).

## Button

Primary marketing button. Black fill, white text, 8px radius, 1px black border.

| State | Where | Values |
|---|---|---|
| default | header `a.btn-primary`, [button-primary-default.png](components/crops/button-primary-default.png) | background `{background.action}`, text `{text.on-action}`, radius `{radius.button}`, height 48px, padding 15px 12.8px, weight 550, 15px, tracking 0.2px |
| hero | `.intro-section a.btn-primary` | height `{size.button-hero}` (56px), padding 19px 24px, 16px |
| hover | declared `.btn-primary:hover` | background stays `#000`, `transform: translateY(-2px)` over 0.4s. Computed hover of the header button did not change colour |
| focus | declared `.btn-primary:focus` | same fill as default |
| focus-visible | forced on the header button | outline 1px `{focus.outline}` (`#005fcc`), offset `{focus.offset}`: `outline-style: auto`, Chromium's default ring. Overflow sets no focus colour, so this is the browser's, not a brand value |
| pressed | not captured | no `:active` rule in the marketing sheet; a press was not held |

Secondary cookie button `button.btn-secondary.btn-xs`: fill `{background.action-secondary}` (`#f0f0f2`), text black, radius 8px, padding 8px 12px, 15px weight 550. Declared hover fills `#e8e8ea` and lifts 2px.

Ghost `a.navbar__btn-simple` ("Sign In"): transparent, black, 15px weight 400, padding 8px 16px, radius 0.

## App button

Signed-out shell. Crop: [button-download-hover.png](components/crops/button-download-hover.png), [button-signin-disabled.png](components/crops/button-signin-disabled.png), [button-google-hover.png](components/crops/button-google-hover.png).

| State | Values |
|---|---|
| primary `.download-button` | fill `{background.app-action}` `#0071db`, text white, radius 6px, height 32px, padding 0 12px, weight 600, 12px, tracking 0.1px, shadow `{shadow.app-button}` |
| primary hover | fill `{background.app-action-hover}` `#0065c5`, shadow `{shadow.app-button-hover}` |
| disabled `button.disabled` | fill `{background.app-disabled}` `#f0f1f3`, text `{text.auth-disabled}` `#b7bdc5`, height 40px, radius 6px. The empty Sign in button is disabled until the fields validate |
| secondary `.google-btn` | white fill, text `#36383b`, height 40px, radius 6px, same resting shadow. Hover deepens the shadow and does not change the fill |
| text button | `{text.auth-link}` `#0071db`, 14px or 12px, radius 3px |

## Link

In-content link (cookie statement, active nav "Pricing"): `{text.link}` `#0085e4`, weight 500 on the cookie link, weight 400 on `.nav-link.active`. Declared `a:hover` is `#259aef`. Footer link: `{text.secondary}` at 60% black, 14px / 24.5px.

App text links ("Sign in with SSO", "Forgot password?") use the text-button styles above. Forgot password is the muted grey, not the blue.

## Text field

Marketing footer `input.form-control`: fill `{color.field}` (4% black), radius 8px, height 48px, padding 16px, 14px, border 0 with a computed border-colour of `#e8e8ea`. Declared focus turns the background white and paints a 2px `#149bfe` ring.

App field, [textfield-focus.png](components/crops/textfield-focus.png): white fill, 1px `{border.app-input}` `#cfd2d7`, radius 6px, height 40px, padding 7px 11px, 14px / 24px, tracking 0.2px, placeholder colour not separately read. Focus darkens the border to `{border.app-input-focus}` `#a3a6aa` and adds no ring. Password focus crop: [textfield-password-focus.png](components/crops/textfield-password-focus.png).

## Text area

Not present on the captured public pages.

## Select

The sign-in page shows an "Overflow for Mac" platform menu beside Download. Its computed style was not isolated (the measurement pass found no `select`). Recorded as a gap.

## Checkbox

`/n/signup` renders two checkboxes (Terms of Service, product updates). Both computed to 0x0: the visible box is not the input element. The painted box was not measured. Recorded as a gap.

## Radio

Not present.

## Switch

Not present on the captured pages. The pricing page has no billing toggle.

## Tabs

Home "Canvas view / Prototype view / Story presentation" is a presentation switcher. Its resting and selected computed styles were not isolated. Recorded as a gap. See [screenshots/home-light-default.png](screenshots/home-light-default.png).

## Menu

Product mega-menu, opened by hover: [screenshots/home-light-nav-open.png](screenshots/home-light-nav-open.png). The panel is `.navbar-nav__megamenu`, white, 1440px wide, 393px tall, no shadow, radius 0. Column titles are the eyebrow style (14px, weight 700, `#acacbc`, tracking 1px). Item titles are 16px weight 700 `#161637`, tracking -0.4px.

Phone drawer: [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png). White sheet, black  type, Sign in on the grey secondary fill, Download for free on black.

## Tooltip

Not present on the captured pages. The app declares `--color-tooltip` and `--shadow-*` but no tooltip was opened.

## Dialog

Cookie notice `.alert.alert--cookies.alert-white`: white surface, 14px text, two buttons (Required only, Allow all). It sits over the hero. No other dialog was opened. Forgot-password is not a dialog: `/n/forgot` returns the app 404.

## Toast

Not present.

## Card

Plan card `.card` on `/pricing/`: white, radius `{radius.card}` 24px, shadow `0 4px 16px -8px rgba(0,0,0,.08)`, 392px wide. Header `.price-box__header` radius 7px 7px 0 0, padding 40px. Title "Pro" is the link blue.

The sign-in trial card ("Don't have an account?") was not isolated as its own computed box. It is visible in [screenshots/signin-light-default.png](screenshots/signin-light-default.png).

## List row

Mega-menu rows and pricing feature rows (check icon plus label). Feature-row metrics were not isolated. Recorded as a gap beyond the menu type above.

## Table

Not present.

## Avatar

Not present. Testimonials use names and roles, not avatar images, on the captured fold.

## Badge

Not present as a component. The app declares `--color-latest-version-badge`.

## Heading

Marketing display, [screenshots/home-light-default.png](screenshots/home-light-default.png): 56px, weight 800, line-height 63.84px, tracking -1.2px, white on the hero, black on interior pages. Section titles 48px / 55.68px / -0.8px weight 800. Mobile home h1 is 40px. App h1, [heading-signin.png](components/crops/heading-signin.png): 32px weight 600, line-height 40px, tracking -0.6px, colour `#2a2d32`.

## Gaps

- No dark theme. `prefers-color-scheme: dark` left marketing and `/n/signin` painted light.
- Pressed states were not held. Marketing `:active` is absent from the sheet.
- Select, checkbox paint, tabs, tooltip, toast, table, avatar, badge, list-row metrics: not isolated.
- `/n/forgot` is a 404, so the forgot-password field was not measured.
- Signup was looked at and not submitted. Validation, error, and loading states are uncaptured.
- Google and SSO were not clicked.
- Help center `support.overflow.io` returned 403 and was not captured.
- The hero wash is a rendered gradient (no CSS `background-image` on the section or its ancestors). Its stops were not read from CSS.
