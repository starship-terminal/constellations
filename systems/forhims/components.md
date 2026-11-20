# Components

Public Hims UK controls, measured on 2026-11-21 at 1440×900 unless a crop says otherwise. Crops are 2x. Values are computed styles. A state that was not reached is listed under Gaps.

## Button

LOGIN is a quiet pill: 12px Care Sans, colour `rgba(0, 0, 0, 0.88)`, background `rgba(0, 0, 0, 0.06)`, radius 48px.

| State | Crop |
|---|---|
| default | [login-button-default.png](components/crops/login-button-default.png) |
| hover | [login-button-hover.png](components/crops/login-button-hover.png) |
| focus-visible | [login-button-focus-visible.png](components/crops/login-button-focus-visible.png) |
| pressed | [login-button-pressed.png](components/crops/login-button-pressed.png) |

Hover, focus-visible and pressed did not change the computed colour. The product may paint no ring.

Explore treatments is a black pill in [screenshots/home-light-default.png](screenshots/home-light-default.png). Computed `backgroundColor` on the button node was transparent. The fill is visible and not isolated. Disabled and loading were not present.

## Link

Nav links are 14px, `rgba(0, 0, 0, 0.89)`, no underline. Hover did not change the computed colour. The Sex item shows an underline when its menu is open: [screenshots/home-light-sex-menu.png](screenshots/home-light-sex-menu.png).

Safety links on the PDP compute to 12.83px and `rgba(0, 0, 0, 0.54)`.

## Menu

Sex opens a white floating menu, radius 8px, with Erectile Dysfunction and Premature Ejaculation. Learn opens the same pattern for Blog and Condition Guides.

The hamburger opens an account drawer: Get started, Log in, Forgot password, then Weight, Hair, ED, Early Climax. Closing it is the X. Log in and Forgot password were not followed.

| State | Where |
|---|---|
| Sex menu | [screenshots/home-light-sex-menu.png](screenshots/home-light-sex-menu.png) |
| Learn menu | [screenshots/home-light-learn-menu.png](screenshots/home-light-learn-menu.png) |
| Account drawer | [screenshots/home-light-account-menu.png](screenshots/home-light-account-menu.png) |
| Phone drawer | [screenshots/mobile-home-light-account-menu.png](screenshots/mobile-home-light-account-menu.png) |

## Accordion

Weight FAQ buttons expand in place. PDP "Meet The Generic ED Pill" expands a bullet list. Both are local. Nothing is submitted.

## Select

`/hair-loss` has Rating and Sort `<select>` elements. Sort computes to 18.5px. The control was not changed, so no selected-option state was captured.

## Card

Home treatment cards are 16px radius. The cream fill is `--colors-canvas-grayPink` (`#f4f1ee`). The locator's computed background was transparent, so the fill is the declared canvas token, confirmed by the screenshot.

The chooser at `/c` is three rows: [screenshots/chooser-light-default.png](screenshots/chooser-light-default.png). Each row goes to an assessment wall. Those walls were not entered.

## Gaps

- Text field, text area, checkbox, radio, switch: not on the public marketing pages. The login form was not entered.
- Toast, tooltip, table, avatar, badge, tabs: not present on the captured pages.
- Button disabled, loading, and a form error: not reached. No form was submitted.
- Primary button fill: visible, not isolated in CSS.
- Dark theme: not present.
