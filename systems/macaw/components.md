# Macaw components

Measured on macawhq.com, signed out, 2026-11-18. Colours are computed styles. Token names are in [tokens.json](tokens.json).

| Component | States | Crop |
|---|---|---|
| Top bar (`navbar`) | default | [navbar-default.png](components/crops/navbar-default.png) |
| Nav link (`nav-link`) | default, hover, focus-visible, pressed | [nav-link-default.png](components/crops/nav-link-default.png) |
| Primary button (`button-primary`) | default, hover, focus-visible, pressed | [button-primary-default.png](components/crops/button-primary-default.png) |
| Secondary button (`button-secondary`) | default, hover, focus-visible, pressed | [button-secondary-default.png](components/crops/button-secondary-default.png) |
| Google sign-in link (`button-google`) | default, hover | [button-google-default.png](components/crops/button-google-default.png) |
| Display heading (`display`) | default | [display-default.png](components/crops/display-default.png) |
| Page (`body-copy`) | default | - |
| Resources menu toggle (`resources-toggle`) | missing | - |
| Resources menu (`resources-menu`) | missing | - |
| Pricing heading (`pricing-heading`) | default | [pricing-heading-default.png](components/crops/pricing-heading-default.png) |
| Starter plan card (`plan-starter`) | default | [plan-starter-default.png](components/crops/plan-starter-default.png) |
| Pro plan card (`plan-pro`) | default | [plan-pro-default.png](components/crops/plan-pro-default.png) |
| Scale plan card (`plan-scale`) | default | [plan-scale-default.png](components/crops/plan-scale-default.png) |
| Yearly billing toggle (`billing-yearly`) | default, hover | [billing-yearly-default.png](components/crops/billing-yearly-default.png) |
| Monthly billing toggle (`billing-monthly`) | default, selected | [billing-monthly-default.png](components/crops/billing-monthly-default.png) |
| Plan call to action (`plan-cta`) | missing | - |
| FAQ question (`faq-question`) | default, hover, expanded | [faq-question-default.png](components/crops/faq-question-default.png) |
| FAQ answer (`faq-answer`) | default | [faq-answer-default.png](components/crops/faq-answer-default.png) |
| Sales link (`sales-link`) | default | [sales-link-default.png](components/crops/sales-link-default.png) |
| Field label (`field-label`) | default | [field-label-default.png](components/crops/field-label-default.png) |
| Text field (`text-field`) | default, hover, focus-visible, focused, filled | [text-field-default.png](components/crops/text-field-default.png) |
| Text area (`text-area`) | default, hover, focus-visible, focused | [text-area-default.png](components/crops/text-area-default.png) |
| Send button (`send-button`) | default, hover, focus-visible | [send-button-default.png](components/crops/send-button-default.png) |
| Tool heading (`tool-heading`) | default | [tool-heading-default.png](components/crops/tool-heading-default.png) |
| Tool call to action (`tool-cta`) | default, hover | [tool-cta-default.png](components/crops/tool-cta-default.png) |
| Legal heading (`legal-heading`) | default | [legal-heading-default.png](components/crops/legal-heading-default.png) |
| Privacy heading (`privacy-heading`) | default | [privacy-heading-default.png](components/crops/privacy-heading-default.png) |
| Mobile top bar (`m-navbar`) | default | [m-navbar-default.png](components/crops/m-navbar-default.png) |
| Mobile menu button (`m-menu-button`) | default | [m-menu-button-default.png](components/crops/m-menu-button-default.png) |
| Primary button (mobile) (`m-button-primary`) | default | [m-button-primary-default.png](components/crops/m-button-primary-default.png) |
| Plan card (mobile) (`m-plan`) | default | [m-plan-default.png](components/crops/m-plan-default.png) |
| Footer link (`footer-link`) | default, hover, focus-visible | [footer-link-default.png](components/crops/footer-link-default.png) |

## Notes

The Resources toggle is `display: none` at 1440, so that row is missing. Get started on pricing did not match a visible link during the run. Log in was cropped by its on-screen box: Playwright treats the Webflow nav link as hidden.

Pressed on the coral button is a forced `:active` and paints the same `--primary700` as hover. The contact form was not submitted.
