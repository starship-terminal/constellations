# PayPal readings

Read on 2026-11-19 from a T3 preview tab (`tab_2g_b476fa69-d865-4d9c-9974-6281ced1c8e8`), signed out. `getComputedStyle` on the live page. Cross-origin stylesheets on `paypalobjects.com` threw SecurityError in the CSSOM, so declared names were fetched with curl and used only where a computed value confirmed them.

Viewport for every page: `innerWidth` 1169, `innerHeight` 731, `devicePixelRatio` 2, `visualViewport` 1169 by 731 at scale 1. That is the preview pane's fill size. It is not a 1440 or 390 capture.

`preview_snapshot` failed twice: "The browser is not producing screenshot frames." No screenshot was invented. Headless Playwright was not launched.

## Pages

| Page | URL | What was read |
|---|---|---|
| SG home | `https://www.paypal.com/` redirected to `/sg/home` | PayPal Open marketing, Business/Personal tabs, Sign Up and Contact Sales |
| US home | `https://www.paypal.com/us/home` | Personal marketing, Learn More, Browse Offers, plate colours |
| Login | `https://www.paypal.com/signin` | Signed-out email step. Nothing typed. Nothing submitted. |
| Account selection | `https://www.paypal.com/us/webapps/mpp/account-selection` | Signup wall. Get Started points at `/welcome/signup` and was not followed. |

## Colours (computed)

| Role | Value | Where |
|---|---|---|
| Canvas | `rgb(241, 239, 234)` | `.document-body-root` |
| Page | `rgb(255, 255, 255)` | `section.primary-plate`, login `html` |
| Ink | `rgb(0, 0, 0)` | marketing body and headings |
| Navy plate | `rgb(0, 41, 145)` | `section.accent-3-plate` |
| Text on navy | `rgb(255, 255, 255)` | heading inside that plate |
| Cyan plate | `rgb(96, 205, 255)` | `section.accent-1-plate` on US home |
| Tertiary plate | `rgb(245, 247, 250)` | `section.tertiary-1-plate` |
| Link on light | `rgb(0, 102, 245)` | `.html-text-renderer-link` |
| Link on navy | `rgb(96, 205, 255)` | links inside accent-3 |
| Muted icon | `rgb(104, 106, 109)` | cookie close button |
| Cookie banner | `rgb(240, 242, 249)` | `.CookieBanner_container_wrapper` |
| Secondary button fill | `rgba(5, 55, 130, 0.08)` | `a.button-type-secondary` |
| Login ink | `rgb(0, 20, 53)` | signin body |
| Login action | `rgb(5, 81, 181)` | `#btnNext` |
| Login link | `rgb(0, 112, 224)` | Forgot email |
| Login label | `rgb(108, 115, 120)` | `label.fieldLabel` |
| Login meta | `rgb(84, 93, 104)` | language links |
| Login card border | `rgb(234, 236, 237)` | `#content` |
| Field focus border | `rgb(207, 211, 216)` | focused `#email` |
| Marketing focus | `rgb(0, 102, 245)` | focused primary button outline, 2px, offset 2px |
| Login focus | `rgb(9, 127, 245)` | focused `#email` outline, 2px |

## Type (computed, innerWidth 1169)

Marketing body: PayPal Pro Text VF, 16px / 18.4px / 400. Headlines: PayPal Pro, weight 900. Fluid sizes at this width: headline-2 60.328px, headline-3 51.077px, headline-4 43.392px, title 22.699px, paragraph 16.647px. A display span on the cyan plate measured 118.757px.

Login: pp-open-regular for body and the 24px / 32px heading. Next uses pp-open-medium at weight 500, 16px / 21px.

## Controls

Marketing primary: black fill, white text, 12px 20px padding, 48px tall, radius 1000px, weight 700, letter-spacing -0.24px. Secondary: the 8% navy wash, same padding and radius, a 1px inset shadow that computes transparent. Login Next: `#0551B5`, 2px solid same colour, radius 100px, 12px 32px, 366px wide. Passkey and Sign Up: 2px black border, transparent fill, radius 100px. Email field: white, radius 6px, padding 20px 12px 8px, 64px tall, 364px wide.

Account card: padding 32px, radius 24px, transparent over the tertiary plate.

## Motion

Primary button transition: padding, margin, width, height, 0.3s, `cubic-bezier(0.4, 1.2, 0.2, 1)`. `prefers-reduced-motion: reduce` was false in this browser, so a reduce pass was not run. No dark theme was painted.
