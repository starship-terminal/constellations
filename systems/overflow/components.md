# Overflow components

Measured on https://overflow.io/ on 2026-11-21, signed out, desktop 1440x900 and phone 390x844. Crops are 256-colour PNGs. Read colours from [tokens.json](tokens.json).

## hero-title

Display heading. Homepage and pricing h1, class intro-section__title.

| State | Crop | What changed |
|---|---|---|
| default | [default](components/crops/hero-title-default.png) | rgb(255, 255, 255) on rgba(0, 0, 0, 0), 56px, 800 |

## hero-cta

Button. Black primary button, Download - free trial.

| State | Crop | What changed |
|---|---|---|
| default | [default](components/crops/hero-cta-default.png) | rgb(255, 255, 255) on rgb(0, 0, 0), 16px, 550 |
| hover | [hover](components/crops/hero-cta-hover.png) | transform matrix(1, 0, 0, 1, 0, -1.94684) |
| focus-visible | [focus-visible](components/crops/hero-cta-focus-visible.png) | transform matrix(1, 0, 0, 1, 0, -0.0078372); Tab |
| pressed | [pressed](components/crops/hero-cta-pressed.png) | transform matrix(1, 0, 0, 1, 0, -0.408152); CDP forcePseudoState active |

## nav-cta

Button. Header Download for free, shorter than the hero button.

| State | Crop | What changed |
|---|---|---|
| default | [default](components/crops/nav-cta-default.png) | rgb(255, 255, 255) on rgb(0, 0, 0), 15px, 550 |
| hover | [hover](components/crops/nav-cta-hover.png) | transform matrix(1, 0, 0, 1, 0, -1.98188) |
| focus-visible | [focus-visible](components/crops/nav-cta-focus-visible.png) | transform matrix(1, 0, 0, 1, 0, -0.00778137); Tab |
| pressed | [pressed](components/crops/nav-cta-pressed.png) | transform matrix(1, 0, 0, 1, 0, -0.496637); CDP forcePseudoState active |

## nav-signin

Button. Quiet Sign In control. Fill appears only while pressed.

| State | Crop | What changed |
|---|---|---|
| default | [default](components/crops/nav-signin-default.png) | rgb(0, 0, 0) on rgba(0, 0, 0, 0), 15px, 400 |
| hover | [hover](components/crops/nav-signin-hover.png) | transform matrix(1, 0, 0, 1, 0, -1.98197) |
| focus-visible | [focus-visible](components/crops/nav-signin-focus-visible.png) | transform matrix(1, 0, 0, 1, 0, -0.00782178); Tab |
| pressed | [pressed](components/crops/nav-signin-pressed.png) | backgroundColor rgba(240, 240, 242, 0.498); transform matrix(1, 0, 0, 1, 0, -0.496717); CDP forcePseudoState active |

## nav-link

Link. Header text link. Hover and pressed shift to the blue accent.

| State | Crop | What changed |
|---|---|---|
| default | [default](components/crops/nav-link-default.png) | rgb(0, 0, 0) on rgba(0, 0, 0, 0), 15px, 400 |
| hover | [hover](components/crops/nav-link-hover.png) | color rgb(37, 154, 239) |
| focus-visible | [focus-visible](components/crops/nav-link-focus-visible.png) | Tab |
| pressed | [pressed](components/crops/nav-link-pressed.png) | color rgb(18, 75, 116); CDP forcePseudoState active |

## product-trigger

Link. Product control that opens the mega menu.

| State | Crop | What changed |
|---|---|---|
| default | [default](components/crops/product-trigger-default.png) | rgb(0, 0, 0) on rgba(0, 0, 0, 0), 15px, 400 |
| hover | [hover](components/crops/product-trigger-hover.png) | color rgb(37, 154, 239) |
| focus-visible | [focus-visible](components/crops/product-trigger-focus-visible.png) | color rgb(34, 141, 219); Tab |
| pressed | [pressed](components/crops/product-trigger-pressed.png) | color rgb(37, 154, 239); CDP forcePseudoState active |

## product-menu

Menu. White mega menu, 1440 by 393, hairline #dadce0.

| State | Crop | What changed |
|---|---|---|
| default | [default](components/crops/product-menu-default.png) | rgb(0, 0, 0) on rgb(255, 255, 255), 16px, 400 |

## menu-link

Link. Mega menu item. Hover fills #f5f5f6.

| State | Crop | What changed |
|---|---|---|
| default | [default](components/crops/menu-link-default.png) | rgb(22, 22, 55) on rgb(255, 255, 255), 14px, 400 |
| hover | [hover](components/crops/menu-link-hover.png) | backgroundColor rgb(245, 245, 246) |
| focus-visible | [focus-visible](components/crops/menu-link-focus-visible.png) | Tab |
| pressed | [pressed](components/crops/menu-link-pressed.png) | backgroundColor rgb(249, 249, 250); CDP forcePseudoState active |

## logo

Link. Wordmark link. Computed color is the brand blue.

| State | Crop | What changed |
|---|---|---|
| default | [default](components/crops/logo-default.png) | rgb(0, 133, 228) on rgba(0, 0, 0, 0), 16px, 500 |

## demo-link

Link. Watch product demo. Opens the video dialog.

| State | Crop | What changed |
|---|---|---|
| default | [default](components/crops/demo-link-default.png) | rgb(0, 0, 0) on rgba(0, 0, 0, 0), 14px, 400 |
| hover | [hover](components/crops/demo-link-hover.png) | color rgba(0, 0, 0, 0.6) |
| focus-visible | no crop | focus failed |
| pressed | [pressed](components/crops/demo-link-pressed.png) | CDP forcePseudoState active |

## plan-card

Card. Pricing card, 24px radius, soft shadow.

| State | Crop | What changed |
|---|---|---|
| default | [default](components/crops/plan-card-default.png) | rgb(0, 0, 0) on rgb(255, 255, 255), 16px, 400 |

## plan-cta

Button. Start free trial inside the plan card.

| State | Crop | What changed |
|---|---|---|
| default | [default](components/crops/plan-cta-default.png) | rgb(255, 255, 255) on rgb(0, 0, 0), 16px, 550 |
| hover | [hover](components/crops/plan-cta-hover.png) | transform matrix(1, 0, 0, 1, 0, -1.94674) |
| focus-visible | [focus-visible](components/crops/plan-cta-focus-visible.png) | transform matrix(1, 0, 0, 1, 0, -0.00782418); Tab |
| pressed | [pressed](components/crops/plan-cta-pressed.png) | transform matrix(1, 0, 0, 1, 0, -0.408489); CDP forcePseudoState active |

## pricing-h1

Display heading. Pricing page title, same ramp as the homepage h1, ink on white.

| State | Crop | What changed |
|---|---|---|
| default | [default](components/crops/pricing-h1-default.png) | rgb(0, 0, 0) on rgba(0, 0, 0, 0), 56px, 800 |

## faq-item

Accordion. Closed FAQ opener. Hover does not change the computed fill.

| State | Crop | What changed |
|---|---|---|
| default | [default](components/crops/faq-item-default.png) | rgb(0, 0, 0) on rgb(255, 255, 255), 16px, 400 |
| hover | [hover](components/crops/faq-item-hover.png) | same as default |
| focus-visible | no crop | focus failed |
| pressed | no crop | CDP forcePseudoState active |

## faq-open

Accordion. Same item after click, body opened.

| State | Crop | What changed |
|---|---|---|
| default | [default](components/crops/faq-open-default.png) | rgb(0, 0, 0) on rgba(0, 0, 0, 0), 16px, 400 |

## download-mac

Button. Download for Mac. Class btn-gradient, painted black.

| State | Crop | What changed |
|---|---|---|
| default | [default](components/crops/download-mac-default.png) | rgb(255, 255, 255) on rgb(0, 0, 0), 16px, 550 |
| hover | [hover](components/crops/download-mac-hover.png) | transform matrix(1, 0, 0, 1, 0, -1.94678) |
| focus-visible | [focus-visible](components/crops/download-mac-focus-visible.png) | transform matrix(1, 0, 0, 1, 0, -0.0180869); Tab |
| pressed | [pressed](components/crops/download-mac-pressed.png) | transform matrix(1, 0, 0, 1, 0, -0.408682); CDP forcePseudoState active |

## download-h1

Display heading. Download page title.

| State | Crop | What changed |
|---|---|---|
| default | [default](components/crops/download-h1-default.png) | rgb(0, 0, 0) on rgba(0, 0, 0, 0), 56px, 800 |

## section-h2

Heading. Features section title, 48px extra-bold.

| State | Crop | What changed |
|---|---|---|
| default | [default](components/crops/section-h2-default.png) | rgb(0, 0, 0) on rgba(0, 0, 0, 0), 48px, 800 |

## blog-card

Badge. Blog filter pill. The card selector missed the article grid.

| State | Crop | What changed |
|---|---|---|
| default | [default](components/crops/blog-card-default.png) | rgba(0, 0, 0, 0.6) on rgb(255, 255, 255), 15px, 500 |
| hover | [hover](components/crops/blog-card-hover.png) | color rgb(0, 0, 0) |

## m-menu-button

Icon button. Phone navbar toggler, 22px wide.

| State | Crop | What changed |
|---|---|---|
| default | [default](components/crops/m-menu-button-default.png) | rgb(0, 0, 0) on rgba(0, 0, 0, 0), 16px, 500 |
| hover | [hover](components/crops/m-menu-button-hover.png) | same as default |
| focus-visible | [focus-visible](components/crops/m-menu-button-focus-visible.png) | Tab |
| pressed | [pressed](components/crops/m-menu-button-pressed.png) | CDP forcePseudoState active |

## m-nav-item

Link. Phone menu row, 24px bold.

| State | Crop | What changed |
|---|---|---|
| default | [default](components/crops/m-nav-item-default.png) | rgb(0, 0, 0) on rgba(0, 0, 0, 0), 24px, 700 |

## Gaps

- Text field, text area, select, checkbox, radio, and switch are not on the public marketing pages. The footer newsletter field was not filled.
- Tooltip, toast, table, and avatar were not found as product controls. The homepage shows decorative avatars inside the product demo artwork.
- Disabled, loading, and error states were not present on the captured controls.
- Focus-visible on demo-link and faq-item failed: those nodes are not keyboard-focusable.
- feature-card and integration-card selectors matched the page body. Those crops are not component evidence.
- Success, warning, danger, and info roles were not painted as status colours.
- Dark theme: not present. The site has no theme toggle.
- Signed-in app, editor, and account screens: not captured. https://overflow.io/n/signin and https://overflow.io/n/signup?buy are walls.
