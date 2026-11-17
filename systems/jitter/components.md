# Components

Measured on jitter.video on 2026-11-18, signed out, desktop 1440 and phone 390. Fills paint on `span.button-inner`, not on the anchor. Crops are in [components/crops/](components/crops/).

## Shell

| Component | States | Notes |
|---|---|---|
| Header | default | Fixed bar, fill `#f2f1f3`, 1440 x 129. [header-default.png](components/crops/header-default.png) |
| Sign up | default, hover, focus-visible, pressed | Black pill `#19171c`, white label, 52px, radius 50px. [nav-signup-default.png](components/crops/nav-signup-default.png) |
| Log in | default, hover, focus-visible, pressed | Text link, not a pill. [nav-login-default.png](components/crops/nav-login-default.png) |
| Footer | default | Grey band. [footer-default.png](components/crops/footer-default.png) |
| Phone header | default | 390-wide bar with a round menu button. [m-header-default.png](components/crops/m-header-default.png) |

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
| Contact name | default, focused | Boundary. Not filled. [contact-name-default.png](components/crops/contact-name-default.png) |
| Contact email | default | Boundary. The published placeholder was covered so the image check stays clean. See the page shot, not a crop. |
| Contact message | default, focused | Textarea. Not submitted. [contact-body-default.png](components/crops/contact-body-default.png) |

## Other

| Component | States | Notes |
|---|---|---|
| Billing toggle | default | Monthly / annual. [plan-toggle-default.png](components/crops/plan-toggle-default.png) |
| FAQ row | default, opened | Accordion. [faq-default.png](components/crops/faq-default.png), [faq-open-opened.png](components/crops/faq-open-opened.png) |
| Login Google | default, hover, focus-visible | OAuth button, never clicked. [login-google-default.png](components/crops/login-google-default.png) |
| Login SSO | default, hover | Never clicked. [login-sso-default.png](components/crops/login-sso-default.png) |
| Login email button | default, hover | Never clicked, so the password step was never reached. [login-email-default.png](components/crops/login-email-default.png) |

## Gaps

- Text area beyond the contact-sales boundary, select, checkbox, radio, switch, tabs, tooltip, dialog, toast, table, avatar and badge do not mount on the signed-out marketing pages.
- The product submenu and the phone menu button were not isolated as their own crops. The open phone drawer is [mobile-home-light-menu-open.png](screenshots/mobile-home-light-menu-open.png).
- Disabled, error and loading states do not appear signed out. Nothing was submitted, so no validation error was seen.
- The editor, files, account, billing, SSO and OAuth flows sit behind sign-in and were not entered.
