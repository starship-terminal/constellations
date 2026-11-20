# Peerlist components

Public site only, signed out, 2026-11-21. Crops are in [components/crops/](components/crops/). Values are token names from [tokens.json](tokens.json).

## Button

Two fills show up on every page.

| State | Where | Tokens |
|---|---|---|
| Accent default | Post, Create Profile | `light.color.accent.default` fill, white text, radius `core.radius.md` (12px), height `core.size.control-md` (32px), label `core.typography.label` |
| Quiet default | Log in | page fill, `light.color.border.default` 1px, same height and radius, shadow `light.shadow.5` |
| Ink default | Login, Book | `core.color.gray.900` fill, white text, radius 12px on Book and 16px on the login page Login |
| Soft | Launch | `light.color.accent.soft` fill, green-400 text, green-100 border |
| Hover | Post hover was captured; computed background stayed `rgb(0, 170, 69)`. The stylesheet names `hover:shadow-focus-border` on the username Submit. A distinct hover colour was not read. | Not captured as a separate colour |
| Pressed | Not held. The accent border is `light.color.accent.pressed` (`#1e874b`) on Post. | Border only |
| Disabled | `disabled:shadow-none` is in the button class. No disabled control was on a public page. | Not captured |
| Focus-visible | Login email focus ring was not isolated. `--shadow-focus` is `0 0 0 4px #e1e4e880` in light. | Declared, not seen on a focused control |
| Loading | Not present on public pages. | Not present |

Crops: [button-accent-default.png](components/crops/button-accent-default.png), [button-secondary-default.png](components/crops/button-secondary-default.png).

## Icon button

Theme control is 24px, radius 8px, page fill, border default. Aria label "Change System theme". Crop is inside [nav-light.png](components/crops/nav-light.png).

## Link

Rail links (Scroll, Jobs, Launchpad, Search, Blog) are 16px Geist, 44px row, 187px wide. The current item uses a green left border (`light.color.accent.default`). Inline links such as Read More use `light.color.text.link` (`#2f80ed`).

## Text field

Login email and password: 32px, radius 8px, padding-left 8px, page fill, border `core.color.gray.300` on email and `gray.200` on password. Homepage username field is a 20px transparent input inside a pill, not the same control. Search people input is 14px, transparent, 20px tall, placeholder "Search people". Focus on that search input did not change outline or shadow in the computed style.

Nothing was typed. No error or filled state.

## Text area

The Scroll composer ("What are you working on?") is visible. It was not measured as its own element. Posting opens the login dialog.

## Select

Not present as a native select. Search filters (Skills and Tools, Location, Roles, Company) are custom. Location was not opened. Not captured.

## Checkbox, radio, switch

A checkbox exists in the search DOM ("Match with all the tags"). It was not cropped as its own state. No radio or switch was used on a public page. Not captured as states.

## Tabs

Scroll: NEWEST and TRENDING, pill pair, green outline on the selected one. Search: People, Projects, Jobs, Posts. People selected is `core.color.gray.900` fill with white text. Projects, Jobs and Posts open the login dialog for a signed-out visitor.

## Menu

Phone home: hamburger opens an overlay with Scroll, Jobs, Launchpad, each with a trailing arrow. [nav-mobile-menu.png](components/crops/nav-mobile-menu.png). Desktop theme control did not mount a Light / Dark / System menu; it toggles `html` class.

## Tooltip

Not seen on the public pages that were opened. Not captured.

## Dialog

Login dialog from Post on `/scroll`: white card, scrim over the feed, Continue with Google, email, password, Login, close. [dialog-login.png](components/crops/dialog-login.png) and [screenshots/scroll-light-login-dialog.png](screenshots/scroll-light-login-dialog.png). Play on the homepage opens a video dialog. The login page is the same form full page: [form-login.png](components/crops/form-login.png).

## Toast

`--toastify-*` variables are in the stylesheet. No toast was triggered. Not captured.

## Card

Launch of the day and job rows are cards. Job row is transparent, 72px, padding 16px 24px, 16px text. [list-row-default.png](components/crops/list-row-default.png).

## List row

Jobs list. Hover shot [list-row-hover.png](components/crops/list-row-hover.png) did not show a computed background change on the anchor.

## Table

Not present on the public pages opened. Not present.

## Avatar

Circular profile images in the home marquee and on Scroll posts. Sizes were not isolated as a token. Observed in [screenshots/home-light-default.png](screenshots/home-light-default.png).

## Badge

LAUNCH chip on featured projects, green. TRENDING tab. Not measured as a separate component token.

## Gaps

- Pressed, disabled, loading, error and focus-visible were not held on a public control.
- Checkbox, radio, switch, select, tooltip, toast and table are not captured.
- Signed-in composer, settings, messages and notifications sit behind `/login`.
- Dark accent button was not measured; dark tokens come from `.dark` custom properties.
- Hover colour for the green button did not change in computed style.
