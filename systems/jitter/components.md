# Components

Measured on jitter.video on 2026-11-18, signed out then signed in on a free email account, desktop 1440 and phone 390. Marketing fills paint on `span.button-inner`, not on the anchor. Crops are in [components/crops/](components/crops/).

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
| Login email button | default, hover | Continue with email. Later used for the magic-link sign-in. [login-email-default.png](components/crops/login-email-default.png) |

## Files

| Component | States | Notes |
|---|---|---|
| Create new file | default, hover | 60px, TWK Lausanne, white label. Fill is on the parent pill. [files-create-default.png](components/crops/files-create-default.png) |
| Import from Figma | default, hover | Blue companion CTA. [files-figma-default.png](components/crops/files-figma-default.png) |
| Files search | default, focused | Sidebar search. Not typed. [files-search-default.png](components/crops/files-search-default.png) |
| Upgrade your plan | default | Sidebar link. Never followed. [files-upgrade-default.png](components/crops/files-upgrade-default.png) |
| Account name | default | `/account/` name field, 296 x 60, white fill. [account-name-default.png](components/crops/account-name-default.png) |

## Editor

| Component | Fill | States |
|---|---|---|
| Share | `#29a9ff` | default. 32 x 68, Inter 13/500, not clicked. [editor-share-default.png](components/crops/editor-share-default.png) |
| Export | `#9262f0` | default. 48 x 137, radius 0. Not opened. [editor-export-default.png](components/crops/editor-export-default.png) |
| Design tab | selected | Inspector mode. [editor-design-default.png](components/crops/editor-design-default.png) |
| Animate tab | default | Inspector mode. [editor-animate-default.png](components/crops/editor-animate-default.png) |
| Upgrade now | `#7a40ed` | default. Toolbar chip. Not clicked. [editor-upgrade-default.png](components/crops/editor-upgrade-default.png) |

## Gaps

- Select, checkbox, radio, switch, tooltip, dialog, toast, table and badge were not isolated.
- The product submenu and the phone menu button were not isolated as their own crops. The open phone drawer is [mobile-home-light-menu-open.png](screenshots/mobile-home-light-menu-open.png).
- Disabled, error and loading states were not produced. Nothing was submitted after sign-in.
- Billing checkout, the export dialog, Invite members and Google/SSO were measured at rest and never followed.
