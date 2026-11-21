# Jace AI components

Public signed-out surfaces measured on 2026-11-18. Marketing pages are light. `app.jace.ai/signin` and `/signup` are the dark product boundary: Google, Outlook and SSO were measured, never pressed. Signup Continue and Continue to signup were clicked to open the OAuth card. There is no email field. The sales form was focused and a sample address was typed then deleted. Nothing was submitted.

Crops live in [components/crops/](components/crops/). Full pages live in [screenshots/](screenshots/).

## Inventory

| Component | Group | States | Crop |
|---|---|---|---|
| Header | Shell and navigation | default | [`header-default`](components/crops/header-default.png) |
| Wordmark | Shell and navigation | default, hover | [`logo-default`](components/crops/logo-default.png) |
| Log In | Shell and navigation | default, hover, focus-visible, pressed | [`nav-login-default`](components/crops/nav-login-default.png) |
| Header CTA | Shell and navigation | default, hover, focus-visible, pressed | [`nav-cta-default`](components/crops/nav-cta-default.png) |
| Hero title | Home | default | [`hero-title-default`](components/crops/hero-title-default.png) |
| Hero CTA | Home | default, hover, focus-visible, pressed | [`hero-cta-default`](components/crops/hero-cta-default.png) |
| Demo chip | Home | default, hover, focus-visible, pressed | [`chip-default`](components/crops/chip-default.png) |
| Integration pill | Home | default, hover, focus-visible, pressed | [`integration-pill-default`](components/crops/integration-pill-default.png) |
| Feature card | Home | default, hover | [`feature-card-default`](components/crops/feature-card-default.png) |
| Section title | Home | default | [`section-title-default`](components/crops/section-title-default.png) |
| Page ground | Home | default |  |
| Pager button | Home | default, hover, focus-visible, pressed | [`pager-default`](components/crops/pager-default.png) |
| Pricing title | Pricing | default | [`pricing-title-default`](components/crops/pricing-title-default.png) |
| Yearly toggle | Pricing | default, hover, focus-visible, pressed | [`billing-yearly-default`](components/crops/billing-yearly-default.png) |
| Monthly toggle | Pricing | default, hover, pressed | [`billing-monthly-default`](components/crops/billing-monthly-default.png) |
| Plus plan card | Pricing | default | [`price-card-default`](components/crops/price-card-default.png) |
| Plan CTA | Pricing | default, hover, focus-visible, pressed | [`price-cta-default`](components/crops/price-cta-default.png) |
| Secondary CTA | Pricing | default, hover, focus-visible, pressed | [`price-secondary-default`](components/crops/price-secondary-default.png) |
| FAQ row | Pricing | default, hover, focus-visible | [`faq-default`](components/crops/faq-default.png) |
| FAQ row, open | Pricing | default | [`faq-open-default`](components/crops/faq-open-default.png) |
| Inline link | Pricing | default, hover | [`link-default`](components/crops/link-default.png) |
| Blog title | Blog | default | [`blog-title-default`](components/crops/blog-title-default.png) |
| Docs nav link | Blog | default, hover, focus-visible, pressed | [`blog-nav-default`](components/crops/blog-nav-default.png) |
| Blog card | Blog | default, hover | [`blog-card-default`](components/crops/blog-card-default.png) |
| Docs title | Docs | default | [`docs-title-default`](components/crops/docs-title-default.png) |
| Docs sidebar link | Docs | default, hover | [`docs-nav-default`](components/crops/docs-nav-default.png) |
| Form title | Sales contact (boundary) | default | [`form-title-default`](components/crops/form-title-default.png) |
| Text field | Sales contact (boundary) | default, hover, focus-visible, focused | [`text-field-default`](components/crops/text-field-default.png) |
| Text area | Sales contact (boundary) | missing |  |
| Submit button | Sales contact (boundary) | default, hover, focus-visible, pressed | [`form-submit-default`](components/crops/form-submit-default.png) |
| Required field | Sales contact (boundary) | default | [`text-field-invalid-default`](components/crops/text-field-invalid-default.png) |
| Sign-in title | App sign-in (boundary) | default | [`signin-title-default`](components/crops/signin-title-default.png) |
| Google button | App sign-in (boundary) | default, hover, focus-visible, pressed | [`signin-oauth-default`](components/crops/signin-oauth-default.png) |
| Outlook button | App sign-in (boundary) | default, hover | [`signin-outlook-default`](components/crops/signin-outlook-default.png) |
| SSO link | App sign-in (boundary) | default, hover | [`signin-sso-default`](components/crops/signin-sso-default.png) |
| Sign up link | App sign-in (boundary) | default, hover, focus-visible, pressed | [`signin-signup-default`](components/crops/signin-signup-default.png) |
| Quote card | App sign-in (boundary) | missing |  |
| Mobile header | Mobile (390 wide) | default | [`m-header-default`](components/crops/m-header-default.png) |
| Menu button | Mobile (390 wide) | missing |  |
| Mobile headline | Mobile (390 wide) | default | [`m-hero-default`](components/crops/m-hero-default.png) |
| Signup title | App signup (boundary) | default | [`signup-title-default`](components/crops/signup-title-default.png) |
| Signup Continue | App signup (boundary) | default, hover, focus-visible, pressed | [`signup-continue-default`](components/crops/signup-continue-default.png) |

## Shared values

Marketing body text is `rgb(45, 45, 45)` (`#2d2d2d`) in Geist Sans. Display type is Gelica. Pills on the marketing site use a 9999px radius. Product controls on the sign-in page use the `--button-*` and `--radius-*` tokens (6px to 8px on those buttons).

## Gaps

- The signed-in inbox, drafts, labels, Flows, settings and billing sit behind Google or Outlook OAuth. Signup was opened through the privacy notice to the OAuth card. There is no email or password field. Google, Outlook and SSO were not pressed.
- The sales form at `/contact/sales` was not submitted, so a posted validation error was not captured. The empty required field was read at rest.
- No textarea is on the sales form. The message control is a text field, not a separate text area. The page ships with sample placeholders, cleared in the committed screenshot.
- The mobile home header has no separate hamburger. Log In and Get started sit in the bar, so the menu-open state is not present.
- Checkbox, radio, switch, select, toast, dialog, tooltip and table are not on the public pages. The pricing FAQ is an accordion, recorded as the FAQ row.
- The inbox table in the home hero is a public demo image, not the signed-in app.

