# Super components

Measured on https://super.so/ and the login wall at https://app.super.so/login on 2026-11-21, signed out, in headless Chromium. Desktop 1440 x 900 at 1x. Phone drawer at 390 x 844 at 2x. Colours below are computed styles. Crops are in [components/crops/](components/crops). A row marked wrong node was a selector miss: the crop exists and must not be used as that component.

## Navbar

The marketing shell. Class `.super-navbar`. 1440 x 80. Background `rgba(255, 255, 255, 0.85)`, which is [light.navbar](tokens.json). Text `rgb(55, 53, 47)` (`core.color.default`). Font 16px.

| Piece | Crop | Size | Fill | Text | Radius | States |
|---|---|---|---|---|---|---|
| Bar | [navbar-default](components/crops/navbar-default.png) | 1440 x 80 | light.navbar | core.color.default | 0 | default |
| Logo | [logo-default](components/crops/logo-default.png) | 162 x 80 | transparent | core.color.default | 0 | default. Links to `/`. |
| Link | [nav-link-default](components/crops/nav-link-default.png) | 99.77 x 80 | transparent | light.text | 8px | hover, focus-visible and pressed painted no change |
| Menu control | [nav-menu-default](components/crops/nav-menu-default.png) | 99.97 x 80 | transparent | core.color.default | 8px | opened paints the same control. The panel is the screenshot, not this crop |
| Sign in | [nav-signin-default](components/crops/nav-signin-default.png) | 84.81 x 44 | #ffffff | rgb(77, 84, 92) | 8px | hover and pressed: fill rgb(249, 249, 248), text light.text. Focus-visible: no change. Opens the login wall. Not followed past the wall |
| Get started free | [nav-cta-default](components/crops/nav-cta-default.png) | 152.22 x 41 | light.accent | #111111 | radius.md | hover, focus-visible and pressed painted no change. Padding 10px 16px. Weight 500. Opens the signup wall |

Phone hamburger is [m-menu-button-default](components/crops/m-menu-button-default.png), 32 x 80, a `div.super-navbar__menu-open`. The drawer is below.

## Menus

Use cases and Features open panels. The panel selector `.super-navbar .notion-dropdown__menu` clipped outside the image, so there is no panel crop. The open panel is [home-light-use-cases-menu.png](screenshots/home-light-use-cases-menu.png) and [home-light-features-menu.png](screenshots/home-light-features-menu.png).

| Piece | Crop | Size | Notes |
|---|---|---|---|
| Use cases item | [nav-dropdown-item-default](components/crops/nav-dropdown-item-default.png) | 298 x 48 | `a[href="/use-cases/website"]`. Text core.color.default, 16px, radius 8px. Hover fill rgb(242, 244, 245). The JSON marks the panel missing. The item crop is the link, not the panel |

## Hero

| Piece | Crop | Size | Type | Fill |
|---|---|---|---|---|
| Title | [hero-title-default](components/crops/hero-title-default.png) | 1088 x 131.44 | core.typography.display, 56px / 600 / 62.72px, light.text | transparent |
| Get started for free | [hero-cta-default](components/crops/hero-cta-default.png) | 177.36 x 52.59 | 16px / 500 / 25.6px, #111111 | light.accent. Hover and pressed: light.accentHover. Focus-visible: no change. Radius 8px. Shadow `rgba(18, 18, 32, 0.05) 0 12px 40px -3px` |
| Load more | [load-more-default](components/crops/load-more-default.png) | 117.98 x 31 | 14px, rgb(120, 118, 115) | transparent. Hover and pressed fill rgb(239, 239, 239). Radius 9999px |

The yellow announcement pill is visible on [home-light-default.png](screenshots/home-light-default.png). The measurement selector matched the page, 1440 x 20019, so [announcement-default.png](components/crops/announcement-default.png) is not the pill. Pill colour, radius and type are Not captured.

## Footer

[footer-default](components/crops/footer-default.png) is 1440 x 451, fill light.footer, text light.footerText. [footer-link](components/crops/footer-link-default.png) is 140 x 48, white, and hover and focus-visible painted no colour change.

## Templates

The page is [templates-light-default.png](screenshots/templates-light-default.png). The big title is a Notion heading and was not the node measured as page-title.

| Piece | Crop | What it actually is |
|---|---|---|
| page-title | [page-title-default](components/crops/page-title-default.png) | Wrong node. 115.81 x 48, 24px, rgb(179, 186, 194). That is the grey "Templates" eyebrow, not the painted title |
| filter-button | [filter-button-default](components/crops/filter-button-default.png) | 104.42 x 36, 22px, light.text. Hover, focus-visible and pressed painted no change |
| filter-menu | [filter-menu-default](components/crops/filter-menu-default.png) | 164.66 x 27.59, 14px, radius 6px. The "any site" sentence control |
| search-field | [search-field-default](components/crops/search-field-default.png) | 226 x 39.59, white, 14px, light.text, radius 10px. Focused and filled with the word portfolio, then cleared. No colour change. Not submitted |
| template-card | [template-card-default](components/crops/template-card-default.png) | Wrong node. 160.22 x 41. That is a Free badge, not a template card |
| category-row | [category-row-default](components/crops/category-row-default.png) | 0 x 0. The data-tab row was not visible to the crop. Hover missing |

## Pricing

Painted title [pricing-title-default](components/crops/pricing-title-default.png) is 777.48 x 69.34, core.typography.title, 57.6px / 600 / 63.36px, light.text.

[pricing-cta-default](components/crops/pricing-cta-default.png) is the wrong node: 160.22 x 41, transparent, the same size as the Free badge. The plan buttons ("Start for free") are on [pricing-light-default.png](screenshots/pricing-light-default.png) and were not measured. Their fill, radius and type are Not captured.

## Use case

| Piece | Crop | Size | Notes |
|---|---|---|---|
| Title | [usecase-title-default](components/crops/usecase-title-default.png) | 520 x 182.25 | 54.4px / 600, light.text. A painted heading, not tokenised as its own style |
| Start with this website | [usecase-cta-default](components/crops/usecase-cta-default.png) | 198.66 x 45.59 | Fill rgb(255, 190, 61), text #111111, 16px, radius 8px. Hover, focus-visible and pressed painted no change. Opens the signup wall |
| Mono chip | [demo-chip-default](components/crops/demo-chip-default.png) | 54.34 x 27 | White, #111111, 12px, radius 999px. Hover painted no change. Recolours the demo in place |

## Feature and blog

[feature-title-default](components/crops/feature-title-default.png) is 708 x 132.69, core.typography.title. [body-text-default](components/crops/body-text-default.png) is 708 x 33.52, 18px, rgb(102, 112, 122).

[blog-title-default](components/crops/blog-title-default.png) is the grey eyebrow, 53 x 48, 24px, rgb(179, 186, 194), not the article title. [blog-card-default](components/crops/blog-card-default.png) is a 341.34 x 311.2 transparent wrapper. Hover painted no change.

## Login wall

Observed only. Nothing typed. Google, Apple and passkey were not clicked. The wall is [login-light-wall.png](screenshots/login-light-wall.png).

| Piece | Crop | Size | Notes |
|---|---|---|---|
| Email | [login-email-default](components/crops/login-email-default.png) | 286 x 20 | The text node, not the field chrome. 14px, rgb(27, 27, 24). Focused, empty |
| Password | [login-password-default](components/crops/login-password-default.png) | 286 x 20 | Same. Focused, empty. No password submitted |
| Log in | [login-submit-default](components/crops/login-submit-default.png) | 320 x 44 | Fill rgb(255, 190, 61), text rgb(27, 27, 24), 14px, radius 8px. Hover fill rgb(255, 174, 0). Not clicked as a submit |
| Google | [login-google-default](components/crops/login-google-default.png) | 320 x 44 | Fill rgb(253, 253, 252), text rgb(27, 27, 24), radius 8px. Not clicked |
| Apple | [login-apple-default](components/crops/login-apple-default.png) | 320 x 44 | Same fill. Not clicked |
| Passkey | [login-passkey-default](components/crops/login-passkey-default.png) | 320 x 44 | Same fill. Not clicked |

## Phone drawer

[m-drawer-opened](components/crops/m-drawer-opened.png) is 390 x 765, white, text core.color.default. [m-drawer-item-default](components/crops/m-drawer-item-default.png) is 358 x 37, 16px, radius 6px. The open drawer screenshot is [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png).

## Shared values

- Yellow marketing CTA: light.accent `#ffbe3c`, text `#111111`, radius 8px, 16px weight 500. Hero hover is light.accentHover `#fbb43c`. The navbar CTA did not change on hover.
- Login submit is a close yellow, `rgb(255, 190, 61)`, and its hover is `rgb(255, 174, 0)`. That hover is not tokenised.
- Sign-in ghost: white, `rgb(77, 84, 92)`, radius 8px. Hover fill `rgb(249, 249, 248)`.
- Page ground is light.page. Footer is light.footer with light.footerText.
- Focus-visible painted no ring on the controls that were focused.

## Gaps

- Navbar dropdown panel: selector missed. Screenshot only.
- Announcement pill: selector matched the page. Not captured as a component.
- Template card, pricing plan button, category row, templates and blog eyebrows: wrong or empty nodes. Do not read those crops as the named component.
- Login field chrome (the white rounded input) was not the measured node. The 286 x 20 crop is the inner text.
- No dialog, toast, checkbox, radio, switch, tabs, tooltip, table, avatar, or badge component was measured. The Free pill on template cards is visible and was the wrong template-card node.
- Dark theme: `html.theme-dark` is declared and was not switched. Not captured.
- Signed-in app, editor, billing, validation errors, empty states, loading states: behind the login wall. Not captured.
