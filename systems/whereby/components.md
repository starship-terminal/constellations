# Components

Public controls on whereby.com, 2026-11-21. Crops are 1x cuts from the 1440 captures.

| Control | State | Evidence |
|---|---|---|
| Sign up | Default, indigo fill `#2B189B`, white Inter-Medium 16/500, 48px, radius 12 | [components/crops/button-signup.png](components/crops/button-signup.png) |
| Log in | Default, indigo label, 48px, radius 12. The named `blue-outline` node computed a transparent background and no border. | [components/crops/button-secondary.png](components/crops/button-secondary.png) |
| Get started | Default, same indigo fill as Sign up | [components/crops/button-primary.png](components/crops/button-primary.png) |
| Login submit | Default, indigo fill, white 16/500, 48px, radius 12, width 400 | [components/crops/button-login-submit.png](components/crops/button-login-submit.png) |
| Continue | Disabled on the empty signup wall. Fill `rgba(0, 0, 0, 0.12)`, label `rgba(0, 0, 0, 0.56)`, 48px, radius 12. Not clicked. | [screenshots/signup-light-default.png](screenshots/signup-light-default.png) |
| Google / Apple | Default outline buttons on the auth walls. Not clicked. | [screenshots/login-light-default.png](screenshots/login-light-default.png) |
| Work email | Empty, placeholder `name@email.com`. Field 58px, radius 12, 1px `rgba(0, 0, 0, 0.12)`. Not typed. | [components/crops/text-field-email.png](components/crops/text-field-email.png) |
| Full name | Empty on signup, placeholder `Full Name`. Not typed. | [screenshots/signup-light-default.png](screenshots/signup-light-default.png) |
| Monthly / Annual | Monthly selected. Track 240 by 48, radius 80, white, shadow `0 1px 4 rgba(0,0,0,0.08)`. | [components/crops/tabs-monthly.png](components/crops/tabs-monthly.png) |
| Save 17% | Badge, indigo fill, white 14px, radius 4. | [components/crops/badge-save.png](components/crops/badge-save.png) |
| Plan card | White, radius 12, shadow `0 1px 4 rgba(0,0,0,0.16), 0 8px 16 rgba(0,0,0,0.16)`. Price 56px display. | [components/crops/price.png](components/crops/price.png) |
| Signup link | Indigo, 18px, underlined. Not followed. | [screenshots/login-light-default.png](screenshots/login-light-default.png) |
| Checkbox | Present on signup (terms, offers) and as the captcha box. Not checked. | [screenshots/signup-light-default.png](screenshots/signup-light-default.png) |
| Cookie dialog | "This website uses cookies", Cookie settings, Accept all cookies. Accept was not clicked. | [screenshots/home-light-cookie.png](screenshots/home-light-cookie.png) |
| Nav dropdown | Products, Pricing, Developers, Resources. White panel. | [screenshots/home-light-products-menu.png](screenshots/home-light-products-menu.png) |
| Phone drawer | Full-screen menu. Login outline and Try for free fill. | [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png) |

Hover, pressed, and a keyboard focus ring were not isolated. Text area, select, radio, switch, tooltip, toast, avatar, and table were not present on the pages that were opened. The captcha is a third-party checkbox and was not solved.
