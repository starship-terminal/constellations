# Components

Measured on jitter.video on 2026-11-21, signed out, desktop 1440 and phone 390. Marketing fills paint on `span.button-inner`, not on the anchor. Crops are in [components/crops/](components/crops/).

## Shell

| Component | States | Notes |
|---|---|---|
| Header | default | Fixed bar, fill `#f2f1f3`, 1440 x 129. [header-default.png](components/crops/header-default.png) |
| Sign up | default, hover, focus-visible, pressed | Black pill `#19171c`, white label, 52px, radius 50px. [nav-signup-default.png](components/crops/nav-signup-default.png) |
| Log in | default, hover, focus-visible, pressed | Text link, not a pill. [nav-login-default.png](components/crops/nav-login-default.png) |
| Footer | default | Grey band. [footer-default.png](components/crops/footer-default.png) |
| Phone header | default | 390-wide bar with a round menu button. [m-header-default.png](components/crops/m-header-default.png) |
| Phone menu | opened | Drawer after Open menu. The crop is the header row of that drawer. [m-menu-opened.png](components/crops/m-menu-opened.png), [mobile-home-light-menu-open.png](screenshots/mobile-home-light-menu-open.png) |

## Buttons

| Component | Fill | States |
|---|---|---|
| Hero CTA | `#b593ff` violet | default, hover, focus-visible, pressed. [hero-cta-default.png](components/crops/hero-cta-default.png) |
| Stories link | `#f5ff63` yellow | default, hover, focus-visible, pressed. [stories-link-default.png](components/crops/stories-link-default.png) |
| Free plan CTA | `#50b8ff` blue | default, hover. Not clicked. [plan-free-default.png](components/crops/plan-free-default.png) |
| Pro plan CTA | `#f5ff63` | default, hover, focus-visible. [plan-pro-default.png](components/crops/plan-pro-default.png) |
| Product CTA | `#b593ff` | default, hover, focus-visible. [product-cta-default.png](components/crops/product-cta-default.png) |
| Send message | `#b593ff` | default, hover, focus-visible. Never clicked. [contact-send-default.png](components/crops/contact-send-default.png) |

Hover does not recolour the marketing pills. The auth card's Google button does: `#f2f1f3` to `#e5e4e7`.

## Fields

| Component | States | Notes |
|---|---|---|
| Newsletter | default, focused | Footer email, dark fill `#2d2933`. Not submitted. [newsletter-default.png](components/crops/newsletter-default.png) |
| Template search | default, focused | Search field. Not typed. [search-default.png](components/crops/search-default.png) |
| Login email | default, focused | Boundary field. Empty. [login-field-default.png](components/crops/login-field-default.png) |
| Contact name | default, focused | Boundary. Not filled. The published placeholder reads John Doe. [contact-name-default.png](components/crops/contact-name-default.png) |
| Contact message | default, focused | Textarea. Not submitted. [contact-body-default.png](components/crops/contact-body-default.png) |

## Other

| Component | States | Notes |
|---|---|---|
| Billing toggle | default | Monthly / annual. The page already shows Pay annually selected. [plan-toggle-default.png](components/crops/plan-toggle-default.png) |
| FAQ row | default, opened | Accordion. [faq-default.png](components/crops/faq-default.png), [faq-open-opened.png](components/crops/faq-open-opened.png) |
| Login Google | default, hover, focus-visible | OAuth button, never clicked. [login-google-default.png](components/crops/login-google-default.png) |
| Login email button | default, hover | Continue with email. Never clicked. [login-email-default.png](components/crops/login-email-default.png) |

## Gaps

- Select, checkbox, radio, switch, tooltip, dialog, toast, table and badge were not isolated.
- Continue with SSO was not on the login card on 2026-11-21. The old SSO crop was the email field, so it was removed.
- The product submenu was photographed as a page, not as an isolated crop. [home-light-product-menu.png](screenshots/home-light-product-menu.png)
- Disabled, error and loading states were not produced. Nothing was submitted.
- Files, account, editor, onboarding and trash were not re-entered on this public pass. Those crops and screenshots were removed.
