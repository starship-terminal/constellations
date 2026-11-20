# Components

Measured on www.sunsama.com on 2026-11-21, signed out, light theme only. Desktop components at 1440x900. Mobile components at 390x844. Values are computed styles from [raw/components-computed.json](raw/components-computed.json). Crops are in [components/crops](components/crops).

Evidence: a number in this file is Measured. A state with no crop is Not captured. A colour that did not change is reported as unchanged, not given a new value.

## Shared values

| Role | Value | Evidence |
|---|---|---|
| Marketing ink | `rgb(32, 34, 40)` / `#202228` | Measured on `.navbar`, `.headlinemain` |
| Marketing ground | `#fafafa` (`light.page`) | Measured CSS `--bg-light-grey-new` |
| Primary fill | `rgb(255, 137, 28)` / `#ff891c` | Measured on `a.buttonprimary` |
| Primary hover fill | `rgb(219, 116, 20)` / `#db7414` | Measured on `nav-cta` hover and pressed |
| Marketing type | DM Sans | Measured on nav, hero, buttons |
| App demo type | Avenir | Measured on price card, signup field, compare tab |
| Browser focus ring | 1px auto `rgb(0, 95, 204)`, offset 1px | Measured on nav-link, nav-cta, footer-link |
| Phone menu focus ring | 1px auto `rgb(229, 151, 0)` | Measured on `m-nav-item` focus-visible |
| Custom focus ring | 2px solid | Measured on `ai-pill` (`rgb(32, 34, 40)`) and `category-button` (`rgb(45, 168, 255)`) |

Radius on marketing buttons is computed `30px` (nav CTA) and `6px` (demo button). Those numbers are not the `--ss-radius-*` tokens (2, 4, 10, 100). Use the computed value for the marketing control and the token for the app demo.

## Shell and navigation

### header

The Webflow nav. 1440x84. Padding 20px top, about 95px inline. Background is transparent (`rgba(221, 221, 221, 0)`). Type is DM Sans 16/24 weight 400. No hover menu.

Crop: [header-default](components/crops/header-default.png).

### logo

Home link, 153x25. Colour `rgb(51, 51, 51)`. The wordmark image sits inside the link. Only default was measured.

Crop: [logo-default](components/crops/logo-default.png).

### nav-link

Pricing link, 71x30.5, padding 4px 12px. Ink `rgb(32, 34, 40)`. Hover and pressed did not change colour, background, or shadow. Focus-visible paints 1px auto `rgb(0, 95, 204)`.

Crops: [default](components/crops/nav-link-default.png), [hover](components/crops/nav-link-hover.png), [focus-visible](components/crops/nav-link-focus-visible.png), [pressed](components/crops/nav-link-pressed.png).

### nav-login

`a.navlinkitem.login`, 61x30.5. Same type and focus ring as nav-link. Hover and pressed did not change computed colour. Following the link opens the login wall. That branch was not followed during measurement.

Crops: [default](components/crops/nav-login-default.png), [hover](components/crops/nav-login-hover.png), [focus-visible](components/crops/nav-login-focus-visible.png), [pressed](components/crops/nav-login-pressed.png).

### nav-cta

`a[href="/start/signup"]`, 144x44, padding 10px 22px, radius 30px. Fill `rgb(255, 137, 28)`, ink `rgb(32, 34, 40)`. Hover and pressed fill `rgb(219, 116, 20)`. Focus-visible keeps the orange fill and adds 1px auto `rgb(0, 95, 204)`.

Crops: [default](components/crops/nav-cta-default.png), [hover](components/crops/nav-cta-hover.png), [focus-visible](components/crops/nav-cta-focus-visible.png), [pressed](components/crops/nav-cta-pressed.png).

## Home

### hero-title

`.headlinemain`, a div, not an h1. 478x178. DM Sans 51.2px, weight 600, line-height 59.392px, ink `rgb(32, 34, 40)`. Only default was measured.

Crop: [hero-title-default](components/crops/hero-title-default.png).

### cta-primary

Body Start for Free, 127x44, same orange fill and 30px radius as nav-cta. Pressed fill `rgb(219, 116, 20)`. Hover did not change the computed background in this pass. Focus-visible did not paint an outline (outline-width stayed 0). That differs from nav-cta.

Crops: [default](components/crops/cta-primary-default.png), [hover](components/crops/cta-primary-hover.png), [focus-visible](components/crops/cta-primary-focus-visible.png), [pressed](components/crops/cta-primary-pressed.png).

### ai-pill

`button.ss-pill`, 306x30. White fill, 1px border `rgb(230, 228, 221)`, DM Sans 13px weight 500, colour `rgb(76, 79, 86)`, letter-spacing -0.13px. Hover and pressed darken the ink to `rgb(32, 34, 40)` and the border to `rgb(201, 198, 188)`. Focus-visible is 2px solid `rgb(32, 34, 40)`.

Crops: [default](components/crops/ai-pill-default.png), [hover](components/crops/ai-pill-hover.png), [focus-visible](components/crops/ai-pill-focus-visible.png), [pressed](components/crops/ai-pill-pressed.png).

### ai-panel

Opened dialog, 560x492. White fill. Shadow `rgba(29, 31, 39, 0.18) 0px 24px 48px 0px`. DM Sans 16/24. Close control was not measured as its own component.

Crop: [ai-panel-opened](components/crops/ai-panel-opened.png). Screenshot: [home-light-ai-panel](screenshots/home-light-ai-panel.png).

### ai-tab

Assistant tab inside the panel, 94x78. White fill, 1px border `rgb(230, 228, 221)`, DM Sans 13/500. Hover and pressed darken the border to `rgb(201, 198, 188)`. Selected fill `rgb(250, 249, 246)`, ink `rgb(32, 34, 40)`, inset shadow `rgb(32, 34, 40) 0px 0px 0px 1px`. Clicking a different tab timed out. That interaction is Not captured.

Crops: [default](components/crops/ai-tab-default.png), [hover](components/crops/ai-tab-hover.png), [pressed](components/crops/ai-tab-pressed.png), [selected](components/crops/ai-tab-selected.png).

### slider-next

Testimonial arrow, 42x30. Fill `rgb(246, 245, 241)`, 1px border `rgb(229, 228, 224)`. Hover, focus-visible, and pressed did not change computed colour or background. Focus outline-width stayed 0.

Crops: [default](components/crops/slider-next-default.png), [hover](components/crops/slider-next-hover.png), [focus-visible](components/crops/slider-next-focus-visible.png), [pressed](components/crops/slider-next-pressed.png).

## Pricing, compare, demo

### price-card

440x391. Fill `rgba(255, 255, 255, 0.5)`. Padding 32px. Shadow `rgba(29, 31, 39, 0.1) 0px 16px 30px 0px`. Type Avenir 16/24. Only default was measured. Prices on the page are static copy. There is no billing toggle.

Crop: [price-card-default](components/crops/price-card-default.png).

### faq-title

`.about-philosophy_title`, 563x24. DM Sans 20px weight 600, colour `rgb(44, 48, 52)`. The title is already expanded text, not a disclosure. Only default was measured.

Crop: [faq-title-default](components/crops/faq-title-default.png).

### compare-tab

64x64 logo tab. Rest opacity 0.7, transparent background. Selected opacity 1, background `rgb(255, 255, 255)`. Hover and pressed did not change computed style. Type on the box is Avenir 16/400, colour `rgb(34, 34, 34)`.

Crops: [default](components/crops/compare-tab-default.png), [hover](components/crops/compare-tab-hover.png), [pressed](components/crops/compare-tab-pressed.png), [selected](components/crops/compare-tab-selected.png).

### demo-button

`button.apm-button.apm-button--green`, 367x40.5. Fill `rgb(48, 199, 138)`, white text, Avenir 15px weight 600, radius 6px, padding 9px 16px. Hover, focus-visible, and pressed did not change computed colour or background. Focus outline-width stayed 0. This green is a page control. It is not `light.app.success` (`#4dcd7d`).

Crops: [default](components/crops/demo-button-default.png), [hover](components/crops/demo-button-hover.png), [focus-visible](components/crops/demo-button-focus-visible.png), [pressed](components/crops/demo-button-pressed.png).

### demo-panel

Opened in-page panel, 862x290. Background transparent. Type Outfit 16/24. The button click stays on `/features/daily-planning`. It is not a form submit.

Crop: [demo-panel-opened](components/crops/demo-panel-opened.png). Screenshot: [feature-planning-light-demo](screenshots/feature-planning-light-demo.png).

## Signup wall

Stopped at the wall. No email typed. No submit.

### signup-title

180x59. Outfit 56px weight 500, line-height 59.36px, ink `rgb(32, 34, 40)`.

Crop: [signup-title-default](components/crops/signup-title-default.png).

### signup-field

Email input, 440x54, padding 18px. White fill, 1px border `rgba(0, 0, 0, 0.2)`, Avenir 14/20, colour `rgb(51, 51, 51)`. Focus-visible border becomes `rgb(56, 152, 236)`. Outline-width stayed 0. Filled, error, and disabled are Not captured.

Crops: [default](components/crops/signup-field-default.png), [focus-visible](components/crops/signup-field-focus-visible.png).

## Integrations and pro tips

### lightbox-link

`a.w-lightbox` on `/integrations/asana`, 914x570. Transparent. Avenir 16/24. Default only. Hover, focus, pressed, and the opened lightbox chrome are Not captured.

Crop: [lightbox-link-default](components/crops/lightbox-link-default.png). The page screenshot with the lightbox open is [integration-light-lightbox](screenshots/integration-light-lightbox.png).

### category-button

`.pt-select__button`, 64x25. DM Sans 14px weight 500. Hover and opened turn the ink `rgb(45, 168, 255)`. Focus-visible is 2px solid `rgb(45, 168, 255)`, offset 1px, radius 3px. Search text was not typed.

Crops: [default](components/crops/category-button-default.png), [hover](components/crops/category-button-hover.png), [focus-visible](components/crops/category-button-focus-visible.png), [opened](components/crops/category-button-opened.png).

## Footer

### footer

1440x842. Transparent background. Horizontal padding about 120px. DM Sans 16/24. The newsletter field is inside this region and was not filled.

Crop: [footer-default](components/crops/footer-default.png).

### footer-link

First footer anchor, 47x17. A social icon, not a text link. Hover and pressed did not change computed colour. Focus-visible is 1px auto `rgb(0, 95, 204)`.

Crops: [default](components/crops/footer-link-default.png), [hover](components/crops/footer-link-hover.png), [focus-visible](components/crops/footer-link-focus-visible.png), [pressed](components/crops/footer-link-pressed.png).

## Mobile (390)

### m-header

`.navbar` at 390, 390x76, padding 20px. Desktop links are hidden.

Crop: [m-header-default](components/crops/m-header-default.png).

### m-menu-button

`.menu-button-2`, 36x36, padding 6px, DM Sans 24/36. Hover, focus-visible, and pressed did not change computed colour. Focus outline-width stayed 0.

Crops: [default](components/crops/m-menu-button-default.png), [hover](components/crops/m-menu-button-hover.png), [focus-visible](components/crops/m-menu-button-focus-visible.png), [pressed](components/crops/m-menu-button-pressed.png).

### m-menu-open

`.w-nav-overlay` after the menu button click. Measured box 390x15787, transparent. The crop is that tall box. The visible menu is the screenshot.

Crop: [m-menu-open-default](components/crops/m-menu-open-default.png). Screenshot: [mobile-home-light-menu](screenshots/mobile-home-light-menu.png).

### m-nav-item

A link in the overlay, 362x51, padding 4px 12px. DM Sans 20/30. Hover and pressed did not change computed colour. Focus-visible is 1px auto `rgb(229, 151, 0)`, not the desktop blue ring.

Crops: [default](components/crops/m-nav-item-default.png), [hover](components/crops/m-nav-item-hover.png), [focus-visible](components/crops/m-nav-item-focus-visible.png), [pressed](components/crops/m-nav-item-pressed.png).

## Gaps

| Item | Status |
|---|---|
| Login email, password, Google, Outlook, SSO | Not captured. Stop branch. |
| Signup filled, error, Turnstile solve, submit | Not captured. Field was focused only. |
| Newsletter and blog subscribe | Not captured. Not filled. |
| Pro-tips search query | Not captured. Not typed. |
| AI tab switch to ChatGPT, Cursor, Claude Code, Other | Not captured. Click timed out. The ChatGPT panel screenshot exists: [home-light-ai-chatgpt](screenshots/home-light-ai-chatgpt.png). |
| Lightbox hover, focus, pressed | Not captured. |
| Dark theme as a painted page | Not captured. Tokens are declared CSS. |
| Disabled, loading, error, toast, table, checkbox, switch | Not captured. Not on the public pages that were measured. |
| SVG icon set | Not captured. |
