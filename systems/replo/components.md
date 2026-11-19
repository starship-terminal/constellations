# Components

Controls that were on the public pages or the signed-out login form on 19 November 2026. Crops are from the Playwright screenshots. Login has no screenshot: the preview tab could not produce frames, and Playwright was not pointed at the login page.

| Component | State captured | Crop | Values |
|---|---|---|---|
| Button | Default, cream | [button-primary.png](components/crops/button-primary.png) | `dark.component.button.background`, height 36px, radius pill |
| Button | Secondary, black | [button-secondary.png](components/crops/button-secondary.png) | `dark.component.button-secondary` |
| Button | Hero, 44px | [button-hero.png](components/crops/button-hero.png) | Same cream face, `core.size.button-lg` |
| Link | Nav | [link-nav.png](components/crops/link-nav.png) | `core.typography.nav`, cream on black |
| Icon button | Phone menu | [button-icon-menu.png](components/crops/button-icon-menu.png) | Three cream bars. Size not tokenised beyond the crop |
| Text field | Empty, contact | [field-text.png](components/crops/field-text.png) | Height 50px, radius 10px |
| Tabs | Annual selected | [tabs-billing.png](components/crops/tabs-billing.png) | Track 44px, option 34px |
| Tabs | Monthly selected | [tabs-billing-monthly.png](components/crops/tabs-billing-monthly.png) | Same track, selected fill moves |
| Badge | Most popular | [badge-popular.png](components/crops/badge-popular.png) | editorialNew 14px, border `rgba(124, 127, 186, 0.4)` |
| Card | Plan | [card-plan.png](components/crops/card-plan.png) | `#0b0b0b`, radius 16px, border 8% white |
| Menu | Product open | [menu-product.png](components/crops/menu-product.png) | `#111111`, radius 14px, shadow 0 18px 50px |
| Empty | 404 | [empty-404.png](components/crops/empty-404.png) | Display type, cream pill |
| Logo | Wordmark | [logo.png](components/crops/logo.png) | Cream mark on black |

## Shared values

Buttons on the marketing site are pills. The cream face is the primary action. The black face with a cream hairline is the secondary action. Plan cards share one body: `#0b0b0b`, 16px radius, 8% white border. The login form is a different system: Inter, 8px radius, 40px controls, on `oklch(0.16 0.0046 72)`.

## Gaps

- Hover, focus-visible, pressed, disabled, loading and error were not forced. The button class names a `focus-visible:outline` and a disabled opacity. Those states were not on screen.
- Checkbox, radio, switch, tooltip, dialog, toast, table, avatar and list row were not on the captured pages as product controls. The contact page shows decorative avatar photos. They are not an avatar component reading.
- The login email and password fields were measured and not cropped, because the preview tab produced no screenshot frames and Playwright was not used on the login page.
- The case-study filter chips and search field are in [case-studies-light-default.png](screenshots/case-studies-light-default.png). Their computed styles were not read.
- FAQ rows were measured closed. None was expanded.
- Select on the contact form was not opened.
