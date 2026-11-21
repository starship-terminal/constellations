# fal components

Public surfaces only, signed out, 2026-11-21. Values are measured. A state that was not held is marked not captured.

## Marketing site

| Component | States | Where |
|---|---|---|
| Nav link | default, hover `#e5ece7`, pressed same as hover. Focus ring not painted (`outline: none`). | [nav-link-default.png](components/crops/nav-link-default.png), [home-light-default.png](screenshots/home-light-default.png) |
| Nav dropdown (Products, Resources) | hover opens a menu. Products items: Model APIs, Serverless, Compute. | [home-light-products-menu.png](screenshots/home-light-products-menu.png) |
| Header button, Get Started | default black, hover `#e5ece7`, 35px tall. Opens the login wall. | [button-start-default.png](components/crops/button-start-default.png) |
| Header button, Contact Sales | default `#e5ece7`, hover `#d9d9d9`. | [button-sales-default.png](components/crops/button-sales-default.png) |
| Hero Get Started | face `#adff00`, 44px tall. Opens the login wall. | [hero-cta-default.png](components/crops/hero-cta-default.png) |
| Display heading | Focal Web, 96px, weight 500, black on the pricing page. Home display is cyan on bronze. | [hero-h1-default.png](components/crops/hero-h1-default.png) |
| Tab (Model APIs / Serverless / Compute) | selected face `#403700`. In-page pane. | [tab-default.png](components/crops/tab-default.png) |
| Footer link | text link in the footer columns. | [home-light-default.png](screenshots/home-light-default.png) |

## App shell (login, explore, docs)

| Component | States | Where |
|---|---|---|
| OAuth button | 40px, radius 4px, label `rgb(32, 32, 34)`, hover `rgb(18, 18, 22, 0.05)`, focus outline colour `rgb(0, 95, 204)`. Not clicked. | [oauth-github-default.png](components/crops/oauth-github-default.png), [login-light-default.png](screenshots/login-light-default.png) |
| SSO button | 32px text button, "Use SSO". Not clicked. | [sso-default.png](components/crops/sso-default.png) |
| Login title | 30px, line-height 0.97, "Welcome to fal". | [login-h1-default.png](components/crops/login-h1-default.png) |
| App nav link | 28px, hover yellow `rgb(255, 255, 0)` on the login header Blog link. | [login-nav-default.png](components/crops/login-nav-default.png) |
| Explore card action | "Try it now", face `rgb(250, 250, 250)`, hover `rgb(228, 228, 231)`, 36px, radius 4px. | [explore-light-default.png](screenshots/explore-light-default.png) |
| Docs search | "Search..." in the sidebar and "Search or ask a question" in the page. Opened, not submitted. | [docs-dark-search.png](screenshots/docs-dark-search.png) |
| Theme switch | System, light, dark on the docs shell. Dark photographed. | [docs-dark-default.png](screenshots/docs-dark-default.png) |

## Not present on the captured public surface

Text field on the marketing site, text area, select, checkbox, radio, switch, tooltip, toast, table, avatar, badge as a product component. The login wall has no email field.

## Not captured

| Item | Reason |
|---|---|
| Signed-in dashboard controls | Login wall. Branch stopped. |
| SSO email step | Use SSO was not clicked. |
| Disabled, loading, error on buttons | Not shown on the public pages that were measured. |
| Marketing focus ring | Computed outline is `none`. |
