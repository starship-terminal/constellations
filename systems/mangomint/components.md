# Mangomint components

Public marketing site at www.mangomint.com, measured 2026-11-21 in headless Chromium. Desktop 1440x900 at 1x. Phone 390x844 at 2x. One light theme. The app login wall at https://app.mangomint.com/login was opened and not filled.

Crops are in [components/crops](components/crops). Values are the computed style of the named element, written as a hex that matches a token in [tokens.json](tokens.json) when one matches. A state row lists only what changed from default.

## Shared values

| Role | Value | Token |
|---|---|---|
| Page | #fcfafa | `core.palette.cream` |
| Ink | #191e49 | `core.palette.ink` |
| Muted | #474f7b | `core.palette.inkSoft` |
| Accent | #bc269b | `core.palette.magenta` |
| Accent hover | #921185 | `core.palette.magentaPressed` |
| Text on accent | #fcfafa | `core.palette.creamText` |
| Pill radius | 48px | `core.radius.pill` |
| Button height | 48px | `core.size.buttonHeight` |
| Body type | tt-commons-pro 16 / 22.4 / 400 | `core.typography.body` |
| Display | tt-commons-pro 54 / 60 / 620 | `core.typography.display` |

## Button

The filled action is a link, not a `<button>`. Try it now (`a[href="/trial/"]`).

| State | What changed |
|---|---|
| default | fill #bc269b, label #fcfafa, 16px weight 540, padding 16px 30px, radius 48px, height 48. [button-primary-default.png](components/crops/button-primary-default.png) |
| hover | fill #921185. [button-primary-hover.png](components/crops/button-primary-hover.png) |
| focus-visible | same fill as hover. No outline ring. [button-primary-focus-visible.png](components/crops/button-primary-focus-visible.png) |
| pressed | CSS `forcePseudoState` hover+active. Same fill as hover. [button-primary-pressed.png](components/crops/button-primary-pressed.png) |

The pricing page's Start a free trial link is the same fill at 17px, height 56, radius 56. [trial-cta-default.png](components/crops/trial-cta-default.png)

The demo wall's Continue button is the same fill, and it is disabled-looking only by sitting under an unanswered question. It was not pressed. [continue-default.png](components/crops/continue-default.png)

## Secondary button

Book a demo in the header. Transparent fill, 2px inset shadow in #bc269b, label #bc269b, radius 48px, height 48.

| State | What changed |
|---|---|
| default | [button-secondary-default.png](components/crops/button-secondary-default.png) |
| hover | label shifts to #fcfafa. The inset shadow stays. [button-secondary-hover.png](components/crops/button-secondary-hover.png) |
| focus-visible | same as hover. [button-secondary-focus-visible.png](components/crops/button-secondary-focus-visible.png) |
| pressed | same as hover. [button-secondary-pressed.png](components/crops/button-secondary-pressed.png) |

## Nav trigger

Features button in the desktop bar. 17px, weight 540, no radius, height 40.

| State | What changed |
|---|---|
| default | label #191e49. [nav-trigger-default.png](components/crops/nav-trigger-default.png) |
| hover | label #bc269b. [nav-trigger-hover.png](components/crops/nav-trigger-hover.png) |
| focus-visible | label #bc269b. [nav-trigger-focus-visible.png](components/crops/nav-trigger-focus-visible.png) |
| pressed | label #bc269b. [nav-trigger-pressed.png](components/crops/nav-trigger-pressed.png) |

Log in is the same treatment. [nav-login-default.png](components/crops/nav-login-default.png)

## Menu

The Features menu is a wide panel under the bar. The crop of the panel is the open state. [nav-menu-open.png](components/crops/nav-menu-open.png)

A row is 16px, radius 10px. Hover paints a white wash at 25% opacity. [nav-menu-link-default.png](components/crops/nav-menu-link-default.png) [nav-menu-link-hover.png](components/crops/nav-menu-link-hover.png)

## Link

The video-tour control is a button whose label is #bc269b at 14px, weight 400. Hover and pressed shift the label to #921185. [video-tour-default.png](components/crops/video-tour-default.png) [video-tour-hover.png](components/crops/video-tour-hover.png)

The Meet Mira banner link is #fcfafa at 14px, weight 540, on the navy bar. [announcement-default.png](components/crops/announcement-default.png)

Footer blog link on the pricing page is #bec5ff at 14px, weight 500. Hover shifts it to #fcfafa. [footer-link-default.png](components/crops/footer-link-default.png) [footer-link-hover.png](components/crops/footer-link-hover.png)

## Carousel tab

Slide 2 on the homepage. 13px, weight 400, colour #474f7b, radius 40px. Hover, focus and pressed did not change the computed colour. [carousel-tab-default.png](components/crops/carousel-tab-default.png)

## Stepper

Increase Locations on the pricing calculator. 22px square, label #bc269b. Hover and pressed shift the label to #921185. Not submitted. [stepper-default.png](components/crops/stepper-default.png) [stepper-hover.png](components/crops/stepper-hover.png)

## Display

Homepage h1. 54px, weight 620, line-height 60px, letter-spacing -1.62px, colour #191e49. [hero-title-default.png](components/crops/hero-title-default.png)

Pricing h1 uses the same size and weight, letter-spacing -1.8px. [pricing-title-default.png](components/crops/pricing-title-default.png)

## Login wall

https://app.mangomint.com/login. Not filled. Not submitted.

| Part | Measured |
|---|---|
| Page | background #191e49, font Muli. |
| Email field | 330x50, radius 5px 5px 0 0, fill rgba(255, 255, 255, 0.1), placeholder #afb8ce. [login-email-default.png](components/crops/login-email-default.png) |
| Focused email | same computed colours. [login-email-focused.png](components/crops/login-email-focused.png) |
| Password field | 330x50, radius 0 0 5px 5px, same fill. [login-password-default.png](components/crops/login-password-default.png) |
| Log In | fill #b28eff, hover #c1a5ff, label #191e49, 17px weight 500, radius 5px, height 46. [login-submit-default.png](components/crops/login-submit-default.png) [login-submit-hover.png](components/crops/login-submit-hover.png) |
| Forgot password | label #ffffff, 16px. [login-forgot-default.png](components/crops/login-forgot-default.png) |

## Phone

Hamburger is a 50x60 icon button. Computed colour stayed black across states. [m-hamburger-default.png](components/crops/m-hamburger-default.png)

The Pricing control in the open drawer is a filled pill, #bc269b, label #fcfafa, radius 48px. [m-menu-link-default.png](components/crops/m-menu-link-default.png)

## Gaps

| Component | Status | Why |
|---|---|---|
| Text field (marketing) | not present | No public marketing form was filled. The demo and trial walls ask a question and were not answered. |
| Text area | not present | Not on the captured public pages. |
| Select | not present | The pricing calculator uses steppers, not a select. |
| Checkbox, radio, switch | not present | Not on the captured public pages. The demo wall uses choice cards, and those cards were not selected. |
| Tabs | captured as carousel tabs | The homepage product demo uses pill tabs. No other tab set was isolated. |
| Tooltip | not present | None opened. |
| Dialog | partly | Watch a video tour opens a business-type dialog ([screenshots/home-light-video-tour.png](screenshots/home-light-video-tour.png)). Its options were not clicked. Watch video was not pressed. |
| Toast | not present | No action was submitted, so no confirmation appeared. |
| Table | not present | Not on the captured public pages. |
| Avatar | observed | Staff avatars appear inside the homepage product demo. The demo is a marketing illustration, not the signed-in app. No crop was taken, so a person's face is not stored as a component. |
| Badge | not present | Not isolated. |
| Card | observed | Pricing cards and blog cards are on the pages. The blog-card crop landed on a link, not the card surface. [blog-card-default.png](components/crops/blog-card-default.png) |
| List row | captured | Feature-menu links. |
| Icon button | captured | Pricing stepper and the phone hamburger. |
| Disabled, loading, error | not present | Continue on the demo wall was not pressed, so its disabled or error state was not reached. |
| Dark theme | not present | Marketing site is light only. The login wall is a separate dark surface. |
