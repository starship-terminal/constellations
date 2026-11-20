# Designmodo components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from designmodo.com on 2026-11-14, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. The site runs two distinct systems: the InterVariable marketing surface and the Fira Sans Postcards app shell. Nothing was signed into, bought or submitted; no form was ever sent; the Login, Sign Up Free, Create Account, + Create, Download and Purchase actions were measured, never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (48 components, 132 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (126 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: every public surface paints `light` (no meaningful dark variant is declared or shown signed out). Desktop shots are 1440 x 900 at 1x; `-full` pages that scroll inside a nested container are captured as viewport-tall `partN` tiles capped at 8 tiles (the mobile app gallery is 14521px tall; the cap kept the first 6752px - a boundary recorded in the capture log); mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png) |
| Postcards app | `/postcards/app/folder/templates` | [default](screenshots/app-light-default.png), [full](screenshots/app-light-full.png) |
| Pricing | `/postcards/pricing/` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Email templates | `/email-templates/` | [default](screenshots/templates-light-default.png), [full](screenshots/templates-light-full.png) |
| Slides | `/slides/` | [default](screenshots/slides-light-default.png), [full](screenshots/slides-light-full.png) |
| Sign in | `/my-account/sign-in/` | [default](screenshots/login-light-default.png), [full](screenshots/login-light-full.png) |
| Postcards product | `/postcards/` | [default](screenshots/postcards-light-default.png), [full](screenshots/postcards-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| App, phone | `/postcards/app/folder/templates` | [default](screenshots/mobile-app-light-default.png), [full](screenshots/mobile-app-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Welcome-back modal | /postcards/app/folder/templates | the signed-out app route mounts the modal over the dimmed gallery; Escape dismisses it and reveals the gallery, which is real DOM, not a paywall stub | [app-light-default](screenshots/app-light-default.png), [welcome-modal](#welcome-back), [modal-google](#continue-with-google), [modal-login](#log-in) |
| Mobile app scroller | phone /postcards/app | the gallery scrolls inside a nested container 14521px tall; the capture kept the first 8 viewport tiles (6752px) and stops there on purpose | [mobile-app-light-full](screenshots/mobile-app-light-full.png) |
| Auth form | /my-account/sign-in/ | the public sign-in card; the fields were typed into and cleared and Login was never pressed | [login-light-default](screenshots/login-light-default.png), [login-submit](#log-in) |
| Signed-in product | a Designmodo account | the builder canvas, saving and every post-login surface needs an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 20 components were given a real keyboard focus. 14 draw an outline ring: `nav-apps` (2px solid #ffffff `background.page`, offset 2px), `nav-login` (2px solid #ffffff `background.page`, offset 2px), `nav-signup` (2px solid #ffffff `background.page`, offset 2px), `openapp-cta` (2px solid #ffffff `background.page`, offset 2px), `seemore-link` (2px solid #c3cecb `text.muted-mkt`, offset 2px), `article-card` (2px solid #ffffff `background.page`, offset 2px), `plan-cta` (2px solid #101d24 `text.ink`, offset 2px), `tpl-filter` (on a child: 1px auto rgb(16, 16, 16) offset 2px), `tpl-card-m` (on a child: 1px auto rgb(16, 16, 16) offset 1px), `login-google` (2px solid #313942 `text.ink-body`, offset 2px), `login-submit` (2px solid #ffffff `background.page`, offset 2px), `login-create` (2px solid #ffffff `background.page`, offset 2px), `pc-cta` (2px solid #101d24 `text.ink`, offset 2px), `m-cta` (2px solid #ffffff `background.page`, offset 2px). The other 6 show no measured change: `modal-google`, `modal-sso`, `modal-login`, `modal-create`, `app-login`, `app-signup`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `ease` | all | modal-email |
| 0.15s | `ease` | all, color | create-split, login-email, login-pass, tpl-card-m |
| 0.15s | `ease-in-out` | all | app-login, app-signup |
| 0.2s | `ease` | all | create-blank, genai-card, seemore-link |
| 0.2s | `ease-in-out` | all | modal-create, modal-login |
| 0.28s | `cubic-bezier(0.22, 1, 0.36, 1)` | box-shadow, transform | tpl-card-m |
| 0.3s | `ease` | all | article-card, login-create, login-google, login-submit, m-cta, nav-signup, openapp-cta, pc-cta and more |
| 0.3s | `ease-in-out` | all | modal-google, modal-sso |
| 0.35s | `cubic-bezier(0.5, 0, 0.35, 1)` | opacity, transform | m-header, mkt-header |
| 0.35s | `ease` | all, background, box-shadow | m-header, mkt-header, nav-apps, nav-login |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card](#plan-card) | 313.33 x 299.89 | - | 16px | rgba(247, 249, 252, 0.9) `background.card` | rgba(58, 76, 102, 0.07) 0px 4px 57px 0px, rgba(191, 197, 202, 0.65) 0px -1.5px 4.5px 0px inset | 40px 40px 30px 40px |
| [Template card](#template-card) | 266 x 592 | - | - | transparent | none | 0 |
| [Generate AI card](#generate-ai-card) | 266 x 592 | - | - | transparent | none | 0 |
| [Article card](#article-card) | 340 x 24 | - | - | transparent | none | 0 |
| [Create Blank card](#create-blank-card) | 266 x 592 | - | - | transparent | none | 0 |
| [Sign-in form](#sign-in-form) | 380 x 562.5 | - | - | transparent | none | 0 |
| [Welcome modal](#welcome-modal) | 423 x 621.2 | - | 10px | #ffffff `background.page` | rgba(169, 179, 187, 0.5) 0px 0px 2px 0px, rgba(169, 179, 187, 0.25) 0px 10px 12px 0px | 0 |
| [Mobile CTA](#mobile-cta) | 134 x 50 | - | 999px | #27ae60 `action.accent` | rgba(39, 174, 96, 0.15) 0px 4px 9px 0px | 13px 28px |

## Components

### Header and navigation

The marketing top bar: the Designmodo wordmark, product dropdowns, Log in and the #f49a40 Sign Up Free pill over the dark hero field.

#### Site header
The top bar: Designmodo wordmark, Apps/Articles menus, Log In and Sign Up. Read as `mkt-header` on the home page.

**Values (default).** size 1440 x 70; padding 0px 24px; background transparent; text InterVariable 15/70 500, #ffffff `background.page`; transition box-shadow 0.35s ease, transform 0.35s cubic-bezier(0.5, 0, 0.35, 1), opacity 0.35s cubic-bezier(0.5, 0, 0.35, 1), background 0.35s ease; icon 30 x 30, #ffffff `background.page`; layers a.button.round 94.0x38.5 #f49a40 `action.orange` 999px; span::before.menu-icon.sidebarTrigger 24pxx2px T:1px solid rgb(255, 255, 255) / R:1px solid rgb(255, 255, 255) / B:1px solid rgb(255, 255, 255) / L:1px solid rgb(255, 255, 255); span::after.menu-icon.sidebarTrigger 24pxx2px T:1px solid rgb(255, 255, 255) / R:1px solid rgb(255, 255, 255) / B:1px solid rgb(255, 255, 255) / L:1px solid rgb(255, .

Child layers that carry the look: a 94x38.5 background #f49a40 `action.orange` radius 999px; span::before 24pxx2px border 1px solid #ffffff `background.page`; span::after 24pxx2px border 1px solid #ffffff `background.page`.

![Site header default](components/crops/mkt-header-default.png)

#### Apps menu
The "Apps" product menu in the header; measured, never opened beyond hover. Read as `nav-apps` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 84 x 70; padding 0px 15px; background transparent; text InterVariable 15/70 500, #ffffff `background.page`; transition all 0.35s ease; icon 11 x 10, #ffffff `background.page` |
| hover | text InterVariable 15/70 500, #2f80ed `action.auth-blue`; transition all 0.15s ease; icon 11 x 10, #2f80ed `action.auth-blue` |
| focus-visible | outline 2px solid #ffffff `background.page`, offset 2px; transition all 0.15s ease; layers a.menu-link.dropdownTrigger 84.0x70.0 2px solid rgb(255, 255, 255) offset 2px |
| pressed | text InterVariable 15/70 500, #2f80ed `action.auth-blue`; transition all 0.15s ease; icon 11 x 10, #2f80ed `action.auth-blue` |

![Apps menu default](components/crops/nav-apps-default.png) ![Apps menu hover](components/crops/nav-apps-hover.png) ![Apps menu focus-visible](components/crops/nav-apps-focus-visible.png) ![Apps menu pressed](components/crops/nav-apps-pressed.png)

#### Log In
The header Log-In action; measured, never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 69 x 70; padding 0px 10px 0px 15px; background transparent; text InterVariable 15/70 500, #ffffff `background.page`; transition all 0.35s ease |
| hover | text InterVariable 15/70 500, #2f80ed `action.auth-blue`; transition all 0.15s ease |
| focus-visible | outline 2px solid #ffffff `background.page`, offset 2px; transition all 0.15s ease; layers a.menu-link.middle 69.0x70.0 2px solid rgb(255, 255, 255) offset 2px |
| pressed | text InterVariable 15/70 500, #2f80ed `action.auth-blue`; transition all 0.15s ease |

![Log In default](components/crops/nav-login-default.png) ![Log In hover](components/crops/nav-login-hover.png) ![Log In focus-visible](components/crops/nav-login-focus-visible.png) ![Log In pressed](components/crops/nav-login-pressed.png)

#### Sign Up
The header Sign-Up action; measured, never followed. Read as `nav-signup` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 94 x 38.5; padding 8px 18px; radius 999px; background #f49a40 `action.orange`; text InterVariable 15/22.5 600, #ffffff `background.page`; transition all 0.3s ease |
| hover | background #f18110 `action.orange-hover`; transition all 0.15s ease |
| focus-visible | background #f18110 `action.orange-hover`; outline 2px solid #ffffff `background.page`, offset 2px; transition all 0.15s ease |
| pressed | background #f18110 `action.orange-hover`; transition all 0.35s ease; transform translate(0px, 2px) |

![Sign Up default](components/crops/nav-signup-default.png) ![Sign Up hover](components/crops/nav-signup-hover.png) ![Sign Up focus-visible](components/crops/nav-signup-focus-visible.png) ![Sign Up pressed](components/crops/nav-signup-pressed.png)

### Home marketing

The designmodo.com marketing page: a 56px InterVariable display heading over the dark hero, the green Open App pill, product strips and the See more link.

#### Hero headline
"Level up email & web designs faster" — the 56px display heading over the dark hero. Read as `hero-h1` on the home page.

**Values (default).** size 498.33 x 123.19; background transparent; text InterVariable 56/61.6 600, #defaca.

![Hero headline default](components/crops/hero-h1-default.png)

#### Open App CTA
The green "Open App →" product CTA (164x53, #27ae60); measured, never followed. Read as `openapp-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 164 x 53; padding 13px 28px; radius 999px; background #27ae60 `action.accent`; shadow rgba(39, 174, 96, 0.15) 0px 4px 9px 0px; text InterVariable 18/27 500, #ffffff `background.page`; transition all 0.3s ease |
| hover | background #1e8449 `action.accent-hover`; shadow rgba(39, 174, 96, 0.2) 0px 6px 12px 0px; transition all 0.15s ease |
| focus-visible | background #1e8449 `action.accent-hover`; outline 2px solid #ffffff `background.page`, offset 2px; transition all 0.15s ease |
| pressed | background #1e8449 `action.accent-hover`; shadow rgba(39, 174, 96, 0.2) 0px 6px 12px 0px; transition all 0.35s ease; transform translate(0px, 2px) |

![Open App CTA default](components/crops/openapp-cta-default.png) ![Open App CTA hover](components/crops/openapp-cta-hover.png) ![Open App CTA focus-visible](components/crops/openapp-cta-focus-visible.png) ![Open App CTA pressed](components/crops/openapp-cta-pressed.png)

#### See more link
A "See more →" link on a product strip. Read as `seemore-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 102.48 x 27; background transparent; text InterVariable 18/27 600, #c3cecb `text.muted-mkt`; transition all 0.2s ease |
| hover | text InterVariable 18/27 600, #ffffff `background.page` |
| focus-visible | outline 2px solid #c3cecb `text.muted-mkt`, offset 2px; layers a.p.weight-6 102.5x27.0 2px solid rgb(195, 206, 203) offset 2px |
| pressed | text InterVariable 18/27 600, #ffffff `background.page` |

![See more link default](components/crops/seemore-link-default.png) ![See more link hover](components/crops/seemore-link-hover.png) ![See more link focus-visible](components/crops/seemore-link-focus-visible.png) ![See more link pressed](components/crops/seemore-link-pressed.png)

#### Article card
A "Read more →" article card in the home articles strip. Read as `article-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 340 x 24; background transparent; text InterVariable 16/24 600, #ffffff `background.page`; transition all 0.3s ease |
| hover | text InterVariable 16/24 600, #27ae60 `action.accent` |
| focus-visible | outline 2px solid #ffffff `background.page`, offset 2px; layers a.margin-top-2.read_more 340.0x24.0 2px solid rgb(255, 255, 255) offset 2px |
| pressed | text InterVariable 16/24 600, #27ae60 `action.accent` |

![Article card default](components/crops/article-card-default.png) ![Article card hover](components/crops/article-card-hover.png) ![Article card focus-visible](components/crops/article-card-focus-visible.png) ![Article card pressed](components/crops/article-card-pressed.png)

#### Product headline
The Postcards product page heading. Read as `pc-h1` on the postcards page.

**Values (default).** size 880 x 204.97; background transparent; text InterVariable 91.5/102.48 900, #101d24 `text.ink`; layers ::before rgba(0, 0, 0, 0) 0px none 1; span.word-animation.nobr 387.8x111.0 #101d24 `text.ink`; span.type-caret 7.3x75.2 #fb754b `action.dark-hover` rgba(251, 117, 75, 0.35) 0px 0px 6px 0px 1px.

Child layers that carry the look: span 387.8x111 background #101d24 `text.ink` image url(data:…); span 7.3x75.2 background #fb754b `action.dark-hover` radius 1px shadow rgba(251, 117, 75, 0.35) 0px 0px 6px 0px.

![Product headline default](components/crops/pc-h1-default.png)

#### Product CTA
The product page primary CTA; measured, never followed. Read as `pc-cta` on the postcards page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 227.69 x 62; padding 16px 26px; radius 12px; background #0d1d24 `action.dark`; text InterVariable 20/30 750, #ffffff `background.page`; transition all 0.3s ease |
| hover | background #fb754b `action.dark-hover`; transition all 0.35s ease |
| focus-visible | outline 2px solid #101d24 `text.ink`, offset 2px |
| pressed | background #fb754b `action.dark-hover`; transition all 0.35s ease; transform translate(0px, 2px) |

![Product CTA default](components/crops/pc-cta-default.png) ![Product CTA hover](components/crops/pc-cta-hover.png) ![Product CTA focus-visible](components/crops/pc-cta-focus-visible.png) ![Product CTA pressed](components/crops/pc-cta-pressed.png)

### Welcome-back auth modal

The signed-out app gate: the 423px Welcome back! modal over the dimmed gallery - Continue with Google, the email passwordless field, Login and Create Account (measured, never submitted).

#### Welcome modal
The "Welcome back!" auth modal over the app shell (418x615, white card on a dimmed gallery). Read as `welcome-modal` on the app page.

**Values (default).** size 423 x 621.2; radius 10px; background #ffffff `background.page`; shadow rgba(169, 179, 187, 0.5) 0px 0px 2px 0px, rgba(169, 179, 187, 0.25) 0px 10px 12px 0px; text Fira Sans 36/43.2 800, #071c26 `background.navy`; icon 16 x 16, #2d3a41 `text.app-ink`.

![Welcome modal default](components/crops/welcome-modal-default.png)

#### Google button
"Continue with Google" in the welcome modal; measured, never pressed. Read as `modal-google` on the app page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 343 x 48; padding 12px 35px 12px 14px; border 1px solid #e8ecf0 `action.secondary`; radius 8px; background #ffffff `background.page`; text Fira Sans 15/22.05 500, #2d3a41 `text.app-ink`; transition all 0.3s ease-in-out; icon 20 x 20, #2d3a41 `text.app-ink` |
| hover, focus-visible, pressed | background rgba(232, 236, 240, 0.5) |

![Google button default](components/crops/modal-google-default.png) ![Google button hover](components/crops/modal-google-hover.png) ![Google button focus-visible](components/crops/modal-google-focus-visible.png) ![Google button pressed](components/crops/modal-google-pressed.png)

#### SSO button
The dark "Sign-in with SSO" button; measured, never pressed. Read as `modal-sso` on the app page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 343 x 48; padding 12px 35px 12px 14px; border 1px solid #e8ecf0 `action.secondary`; radius 8px; background #071c26 `background.navy`; text Fira Sans 15/22.05 500, #ffffff `background.page`; transition all 0.3s ease-in-out; icon 20 x 20, #ffffff `background.page` |
| hover, focus-visible, pressed | background #2a3539 |

![SSO button default](components/crops/modal-sso-default.png) ![SSO button hover](components/crops/modal-sso-hover.png) ![SSO button focus-visible](components/crops/modal-sso-focus-visible.png) ![SSO button pressed](components/crops/modal-sso-pressed.png)

#### Email field
The your@email.com field in the welcome modal; focused and typed then cleared, never submitted. Read as `modal-email` on the app page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 343 x 50; padding 10px 15px 10px 45px; border 1px solid #e8ecf0 `action.secondary`; radius 8px; background #ffffff `background.page`; outline 2px solid transparent, offset 0px; text Fira Sans 15/18 400, #071c26 `background.navy`; transition all 0.1s ease; placeholder #2d3a41 `text.app-ink` |
| focused, filled | border 1px solid transparent; outline 2px solid #2198ed `action.blue`, offset 0px |

![Email field default](components/crops/modal-email-default.png) ![Email field focused](components/crops/modal-email-focused.png) ![Email field filled](components/crops/modal-email-filled.png)

#### Modal Login
The green modal Login button; measured, never pressed. Read as `modal-login` on the app page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 166.5 x 52; padding 1px 6px; radius 8px; background #27ae60 `action.accent`; text Fira Sans 15/normal 500, #ffffff `background.page`; transition all 0.2s ease-in-out |
| hover, focus-visible, pressed | background #239b58 |

![Modal Login default](components/crops/modal-login-default.png) ![Modal Login hover](components/crops/modal-login-hover.png) ![Modal Login focus-visible](components/crops/modal-login-focus-visible.png) ![Modal Login pressed](components/crops/modal-login-pressed.png)

#### Create Account
The secondary "Create Account" button; measured, never pressed. Read as `modal-create` on the app page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 166.5 x 52; padding 1px 6px; radius 8px; background #e8ecf0 `action.secondary`; text Fira Sans 15/normal 500, #2d3a41 `text.app-ink`; transition all 0.2s ease-in-out |
| hover, focus-visible, pressed | background #d9dfe6 |

![Create Account default](components/crops/modal-create-default.png) ![Create Account hover](components/crops/modal-create-hover.png) ![Create Account focus-visible](components/crops/modal-create-focus-visible.png) ![Create Account pressed](components/crops/modal-create-pressed.png)

### Postcards app (signed out)

The Postcards email-builder shell behind the welcome modal: the #071c26 navy app header, the 241px workspace sidebar, + Create, the filter labels and 266x592 template cards with FREE/NEW badges.

#### App header
The dark navy app header: postcards mark, Login/Signup, the "+ Create" split button. Read as `app-header` on the app page.

**Values (default).** size 1440 x 60; background #071c26 `background.navy`; text Fira Sans 15/22.05 500, #ffffff `background.page`; icon 17 x 18, #0000ee.

![App header default](components/crops/app-header-default.png)

#### App Login
The blue Login pill in the app header; measured, never pressed. Read as `app-login` on the app page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 94 x 40.05; padding 9px 15px; radius 6px; background #2198ed `action.blue`; text Fira Sans 15/22.05 500, #ffffff `background.page`; transition all 0.15s ease-in-out; icon 16 x 16, #ffffff `background.page` |
| hover, pressed | background #344a56 `action.blue-hover` |

![App Login default](components/crops/app-login-default.png) ![App Login hover](components/crops/app-login-hover.png) ![App Login focus-visible](components/crops/app-login-focus-visible.png) ![App Login pressed](components/crops/app-login-pressed.png)

#### App Signup
The dark Signup pill in the app header; measured, never pressed. Read as `app-signup` on the app page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 78 x 40.05; padding 9px 15px; radius 6px; background #485f6b `action.slate`; text Fira Sans 15/22.05 500, #ffffff `background.page`; transition all 0.15s ease-in-out |
| hover, pressed | background #344a56 `action.blue-hover` |

![App Signup default](components/crops/app-signup-default.png) ![App Signup hover](components/crops/app-signup-hover.png) ![App Signup focus-visible](components/crops/app-signup-focus-visible.png) ![App Signup pressed](components/crops/app-signup-pressed.png)

#### Create split button
The green "+ Create" split button top-right of the gallery; measured, never pressed. Read as `create-split` on the app page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 122 x 40; padding 0px 13px; radius 6px; background #27ae60 `action.accent`; text Fira Sans 14/normal 500, #ffffff `background.page`; transition all 0.15s ease; icon 16 x 16, #ffffff `background.page` |
| hover, pressed | background #239b58 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Create split button default](components/crops/create-split-default.png) ![Create split button hover](components/crops/create-split-hover.png) ![Create split button pressed](components/crops/create-split-pressed.png)

#### App sidebar
The 240px workspace sidebar: Drafts, Templates (+233 NEW), Workspace Settings, Chat with Us. Read as `sidebar` on the app page.

**Values (default).** size 241 x 840; border R: 1px solid #e8ecf0 `action.secondary`; background transparent; text Fira Sans 13/19.5 500, #2d3a41 `text.app-ink`; icon 20 x 20, #aab2bb; layers div.sc-iUVXli.gXFlZm 241.0x840.0 R:1px solid rgb(232, 236, 240); div.sc-eDknUU.gzbzF 240.0x60.0 B:1px solid rgb(232, 236, 240); div.sc-tDzRk.dTSGyz 220.0x40.0 2px solid rgba(33, 152, 237, 0) offset 0px 10px; div.sc-EtVYz.QEotB 240.0x1.0 T:1px solid rgb(232, 236, 240); div.sc-tDzRk.dsBttE 220.0x40.0 #d9efff 2px solid rgba(33, 152, 237, 0) offset 0px 10px; span.sc-jmLfgi.hfvJKt 54.0x14.0 #27ae60 `ac.

Child layers that carry the look: div 241x840 border 1px solid #e8ecf0 `action.secondary`; div 240x60 border 1px solid #e8ecf0 `action.secondary`; div 220x40 radius 10px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Templates nav
The "Templates" sidebar item with the +233 NEW badge. Read as `side-templates` on the app page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 69 x 21; background transparent; text Fira Sans 14/21 500, #2198ed `action.blue` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Templates nav default](components/crops/side-templates-default.png) ![Templates nav hover](components/crops/side-templates-hover.png) ![Templates nav pressed](components/crops/side-templates-pressed.png)

#### NEW badge
The green "+233 NEW" counter badge on the Templates item. Read as `new-badge` on the app page.

**Values (default).** size 54 x 14; padding 0px 4px; radius 3px; background #27ae60 `action.accent`; shadow rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset; text Fira Sans 9/9 600, #ffffff `background.page`.

![NEW badge default](components/crops/new-badge-default.png)

#### Industry filter
The "Industry" gallery filter dropdown; measured, never opened. Read as `filter-industry` on the app page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 61.97 x 15; background transparent; text Fira Sans 13/normal 400, #585d63 `text.muted`; icon 8 x 5, #585d63 `text.muted` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Industry filter default](components/crops/filter-industry-default.png) ![Industry filter hover](components/crops/filter-industry-hover.png) ![Industry filter pressed](components/crops/filter-industry-pressed.png)

#### Create Blank card
The dashed "Create Blank Template" gallery card (266x532); measured, never pressed. Read as `create-blank` on the app page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 266 x 592; background transparent; text Fira Sans 13/19.5 500, #788994; transition all 0.2s ease; icon 24 x 24, #788994; layers div.sc-hBxvHn.emdIll 266.0x532.0 #f4f6f7 `background.card-face` T:1px solid rgba(27, 27, 27, 0.1) / R:1px solid rgba(27, 27, 27, 0.1) / B:1px solid rgba(27, 27, 27, 0.1) / L:1px solid rgba(27, 27, 27, 0.1) 2px solid rgba(0, 0, 0, 0) offset 0px 10px |
| hover | layers div.sc-hBxvHn.emdIll 266.0x532.0 #f4f6f7 `background.card-face` T:1px solid rgba(27, 27, 27, 0.1) / R:1px solid rgba(27, 27, 27, 0.1) / B:1px solid rgba(27, 27, 27, 0.1) / L:1px solid rgba(27, 27, 27, 0.1) 2px solid rgb(33, 152, 237) offset 0px 10px |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: div 266x532 background #f4f6f7 `background.card-face` border 1px solid rgba(27, 27, 27, 0.1) radius 10px.

![Create Blank card hover](components/crops/create-blank-hover.png) ![Create Blank card pressed](components/crops/create-blank-pressed.png)

#### Generate AI card
The lavender "Generate with AI" gallery card; measured, never pressed. Read as `genai-card` on the app page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 266 x 592; background transparent; text Fira Sans 13/19.5 500, #405eff; transition all 0.2s ease; icon 20 x 20, #405eff; layers div.sc-kjGiqv.kEmqZX 266.0x532.0 T:1px solid rgba(27, 27, 27, 0.1) / R:1px solid rgba(27, 27, 27, 0.1) / B:1px solid rgba(27, 27, 27, 0.1) / L:1px solid rgba(27, 27, 27, 0.1) 2px solid rgba(0, 0, 0, 0) offset 0px 10px |
| hover | layers div.sc-kjGiqv.kEmqZX 266.0x532.0 T:1px solid rgba(27, 27, 27, 0.1) / R:1px solid rgba(27, 27, 27, 0.1) / B:1px solid rgba(27, 27, 27, 0.1) / L:1px solid rgba(27, 27, 27, 0.1) 2px solid rgb(64, 94, 255) offset 0px 10px |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: div 266x532 image linear-gradient(135deg, #f0f4ff 0%, #e6ebff 100%) border 1px solid rgba(27, 27, 27, 0.1) radius 10px.

![Generate AI card default](components/crops/genai-card-default.png) ![Generate AI card hover](components/crops/genai-card-hover.png) ![Generate AI card pressed](components/crops/genai-card-pressed.png)

#### Template card
A named template card (Kindred, Nortflow...) with the FREE badge and category tags. Read as `tpl-card` on the app page.

**Values (default).** size 266 x 592; background transparent; text Fira Sans 9/9 600, #ffffff `background.page`; icon 10 x 10, #ffffff `background.page`; layers div.sc-dvTebe.hIbSre 266.0x532.0 #215c43 rgba(0, 0, 0, 0) 0px 0px 0px 2px 1px solid rgba(27, 27, 27, 0.1) offset 0px 10px; span.sc-fMjwjh.sc-kbXUY 43.0x16.0 #2198ed `action.blue` rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset 4px; span.sc-bkSjNy.bqBVzQ 28.5x14.0 #27ae60 `action.accent` rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset 3px.

Child layers that carry the look: div 266x532 background #215c43 radius 10px shadow transparent 0px 0px 0px 2px; span 43x16 background #2198ed `action.blue` radius 4px shadow rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset; span 28.5x14 background #27ae60 `action.accent` radius 3px shadow rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset.

![Template card default](components/crops/tpl-card-default.png)

#### FREE badge
The blue FREE corner badge on template cards. Read as `free-badge` on the app page.

**Values (default).** size 43 x 16; padding 2.5px 4px 3.5px 4px; radius 4px; background #2198ed `action.blue`; shadow rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset; text Fira Sans 9/9 600, #ffffff `background.page`; icon 10 x 10, #ffffff `background.page`.

![FREE badge default](components/crops/free-badge-default.png)

### Pricing

The /pricing marketing page: the 91.5px display heading, plan cards on the tinted field and the plan CTAs.

#### Pricing headline
The 91.5px "Pricing" display heading. Read as `pricing-h1` on the pricing page.

**Values (default).** size 1180 x 102.48; background transparent; text InterVariable 91.5/102.48 900, #101d24 `text.ink`; layers ::before rgba(0, 0, 0, 0) 0px none 1.

![Pricing headline default](components/crops/pricing-h1-default.png)

#### Billing toggle
The Yearly/Monthly billing switch; measured, never toggled. Read as `billing-toggle` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 193 x 30; background transparent; text InterVariable 16/30 500, #101d24 `text.ink`; layers span::before.qmark.description 260pxx93px #111111 8px; span::after.qmark.description 26pxx7px; span.element 30.0x16.0 #101d24 `text.ink` 10px; span::after.element 10pxx10px #ffffff `background.page` 50% |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: span::before 260pxx93px background #111111 radius 8px; span::after 26pxx7px image url(data:…)'%3E%3Cpath d='M0 0L-8.74228e-08 1C2.97731 1 5.81883 2.27754 7.8 4.5C10.4659 7.; span 30x16 background #101d24 `text.ink` radius 10px.

![Billing toggle default](components/crops/billing-toggle-default.png) ![Billing toggle hover](components/crops/billing-toggle-hover.png) ![Billing toggle pressed](components/crops/billing-toggle-pressed.png)

#### Plan card
A pricing plan card (Start FREE FOREVER / Plus / Pro) — white-box 313px wide. Read as `plan-card` on the pricing page.

**Values (default).** size 313.33 x 299.89; padding 40px 40px 30px 40px; radius 16px; background rgba(247, 249, 252, 0.9) `background.card`; shadow rgba(58, 76, 102, 0.07) 0px 4px 57px 0px, rgba(191, 197, 202, 0.65) 0px -1.5px 4.5px 0px inset; text InterVariable 22/26.4 700, #101d24 `text.ink`.

![Plan card default](components/crops/plan-card-default.png)

#### Plan CTA
A plan action (Get Started / $19/month) — it adds to the cart; measured, never pressed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 233.33 x 52; padding 14px 22px; radius 10px; background #101d24 `text.ink`; text InterVariable 16/24 800, #ffffff `background.page`; transition all 0.3s ease |
| hover | transition all 0.35s ease |
| focus-visible | outline 2px solid #101d24 `text.ink`, offset 2px |
| pressed | transition all 0.35s ease; transform translate(0px, 2px) |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Plan feature
A plan feature row ("10 template projects") with the ? hint icon. Read as `plan-feature` on the pricing page.

**Values (default).** size 293.33 x 308; background transparent; text InterVariable 16/28 700, #101d24 `text.ink`; layers span.qmark.description 14.0x14.0 #747491 25px; span::before.qmark.description 260pxx72px #111111 8px; span::after.qmark.description 26pxx7px; span.qmark.description 14.0x14.0 #747491 25px; span::before.qmark.description 260pxx72px #111111 8px; span::after.qmark.description 26pxx7px.

Child layers that carry the look: span 14x14 background #747491 radius 25px; span::before 260pxx72px background #111111 radius 8px; span::after 26pxx7px image url(data:…)'%3E%3Cpath d='M0 0L-8.74228e-08 1C2.97731 1 5.81883 2.27754 7.8 4.5C10.4659 7..

![Plan feature default](components/crops/plan-feature-default.png)

### Email-template gallery

The public /email-templates/ gallery: the 63px page display, the NEW/FREE badges and template cards.

#### Gallery headline
The email-templates gallery heading. Read as `tpl-h1` on the templates page.

**Values (default).** size 780 x 151.19; background transparent; text InterVariable 63/75.6 900, #101d24 `text.ink`.

![Gallery headline default](components/crops/tpl-h1-default.png)

#### Gallery filter
The Industry / Usage / Season / Brand / Free-only filter bar over the email-template grid (714x43); measured, never activated. Read as `tpl-filter` on the templates page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 714 x 43.19; background transparent; text InterVariable 16/38.4 400, #ffffff `background.page`; icon 11 x 11, #ffffff `background.page`; layers span.white.text-deepPurple 0.0x20.0 #ffffff `background.page`; span.white.text-deepPurple 0.0x20.0 #ffffff `background.page`; span.white.text-deepPurple 0.0x20.0 #ffffff `background.page`; span.white.text-deepPurple 0.0x20.0 #ffffff `background.page`; span.free-filter-box 14.0x14.0 T:1px solid rgba(255, 255, 255, 0.55) / R:1px solid rgba(255, 255, 255, 0.55) / B:1px solid rgba(255, 255, 255, 0.55) |
| focus-visible | layers span.white.text-deepPurple 0.0x20.0 #ffffff `background.page`; span.white.text-deepPurple 0.0x20.0 #ffffff `background.page`; span.white.text-deepPurple 0.0x20.0 #ffffff `background.page`; span.white.text-deepPurple 0.0x20.0 #ffffff `background.page`; input.free-filter-checkbox 1.0x1.0 1px auto rgb(16, 16, 16) offset 2px; span.free-filter-box 14.0x14.0 T:1px solid rgba(255, 255, 255, 0.55) / R:1px |

Child layers that carry the look: span 0x20 background #ffffff `background.page`; span 0x20 background #ffffff `background.page`; span 0x20 background #ffffff `background.page`.

![Gallery filter default](components/crops/tpl-filter-default.png) ![Gallery filter hover](components/crops/tpl-filter-hover.png) ![Gallery filter focus-visible](components/crops/tpl-filter-focus-visible.png) ![Gallery filter pressed](components/crops/tpl-filter-pressed.png)

#### Template tile
An email-template tile in the marketing gallery grid (210x420, thumbnail + name + tags); measured, never followed. Read as `tpl-card-m` on the templates page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 210 x 420; radius 8px; background transparent; shadow rgba(10, 33, 65, 0.05) 0px 10px 20px 0px, rgba(0, 0, 0, 0.13) 0px 0px 2px 0px; text InterVariable 9/9 600, #ffffff `background.page`; transition transform 0.28s cubic-bezier(0.22, 1, 0.36, 1), box-shadow 0.28s cubic-bezier(0.22, 1, 0.36, 1), color 0.15s ease; icon 10 x 10, #ffffff `background.page`; layers div.template-box.margin-bottom-2 210.0x420.0 rgba(10, 33, 65, 0.05) 0px 10px 20px 0px, rgba(0, 0, 0, 0.13) 0px 0px 2px 0px 8px; span.template-license-label.is-free 46.0x16.0 #2198ed `action.blue` rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset 4px; div.template-hover-overlay 210.0x420.0 rgba(255, 255, 255, 0.96); a.button.crop 178.0x42.5 #101d24 `text.ink` 8px; a.button.crop 178.0x42.5 #fb754b `action. |
| hover | shadow rgba(10, 33, 65, 0.05) 0px 18.296px 36.592px 0px, rgba(0, 0, 0, 0.13) 0px 0px 2px 0px; transform translate(0px, -3.31841px); layers div.template-box.margin-bottom-2 210.0x420.0 rgba(10, 33, 65, 0.05) 0px 18.296px 36.592px 0px, rgba(0, 0, 0, 0.13) 0px 0px 2px 0px 8px; span.template-license-label.is-free 46.0x16.0 #2198ed `action.blue` rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset 4px; div.template-hover-overlay 210.0x420.0 rgba(255, 255, 255, 0.96); a.button.crop 178.0x42.5 #101d24 `text.ink` 8px; a.button.crop 178.0x42.5 #fb754b  |
| focus-visible | layers div.template-box.margin-bottom-2 210.0x420.0 rgba(10, 33, 65, 0.05) 0px 10px 20px 0px, rgba(0, 0, 0, 0.13) 0px 0px 2px 0px 8px; span.template-license-label.is-free 46.0x16.0 #2198ed `action.blue` rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset 4px; div.template-hover-overlay 210.0x420.0 rgba(255, 255, 255, 0.96); a 148.5x125.8 1px auto rgb(16, 16, 16) offset 1px; a.button.crop 178.0x42.5 #101d24 `text. |
| pressed | shadow rgba(10, 33, 65, 0.05) 0px 16.2721px 32.5442px 0px, rgba(0, 0, 0, 0.13) 0px 0px 2px 0px; transform translate(0px, -2.50884px); layers div.template-box.margin-bottom-2 210.0x420.0 rgba(10, 33, 65, 0.05) 0px 16.2721px 32.5442px 0px, rgba(0, 0, 0, 0.13) 0px 0px 2px 0px 8px; span.template-license-label.is-free 46.0x16.0 #2198ed `action.blue` rgba(0, 0, 0, 0.06) 0px -1px 0px 0px inset 4px; div.template-hover-overlay 210.0x420.0 rgba(255, 255, 255, 0.96); a.button.crop 178.0x42.5 #101d24 `text.ink` 8px; a.button.crop 178.0x42.5 #fb754 |

![Template tile hover](components/crops/tpl-card-m-hover.png) ![Template tile focus-visible](components/crops/tpl-card-m-focus-visible.png) ![Template tile pressed](components/crops/tpl-card-m-pressed.png)

### Sign-in form

The /my-account/sign-in/ public auth form: the 380x562 card with email/password fields, the Login button and sign-up link (measured, never submitted).

#### Sign-in form
The my-account sign-in card (380px, Google/SSO buttons over email+password). Read as `login-form` on the login page.

**Values (default).** size 380 x 562.5; background transparent; text InterVariable 16/24 500, #313942 `text.ink-body`; icon 20 x 20, #313942 `text.ink-body`; layers a.button.white 380.0x50.0 #ffffff `background.page` rgb(224, 229, 235) 0px 0px 0px 1px inset 5px; a.button.flat 380.0x50.0 #313942 `text.ink-body` 5px; div::before.hr.p 170pxx1px #e0e5eb `border.hairline`; div::after.hr.p 170pxx1px #e0e5eb `border.hairline`; input.woocommerce-Input.woocommerce-Input--text 380.0x50.0 #ffffff `background.page` T:1px solid rgb(224, 229, 235) / R:1px solid rgb(224, 22.

Child layers that carry the look: a 380x50 background #ffffff `background.page` radius 5px shadow #e0e5eb `border.hairline` 0px 0px 0px 1px inset; a 380x50 background #313942 `text.ink-body` radius 5px; div::before 170pxx1px background #e0e5eb `border.hairline`.

![Sign-in form default](components/crops/login-form-default.png)

#### Sign-in heading
"Login to Designmodo" — the 24px form heading. Read as `login-h1` on the login page.

**Values (default).** size 440 x 32.39; background transparent; text InterVariable 24/32.4 700, #313942 `text.ink-body`.

![Sign-in heading default](components/crops/login-h1-default.png)

#### Google login
"Login with Google" — measured, never pressed. Read as `login-google` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 380 x 50; padding 13px 20px; radius 5px; background #ffffff `background.page`; shadow #e0e5eb 0px 0px 0px 1px inset; text InterVariable 16/24 500, #313942 `text.ink-body`; transition all 0.3s ease; icon 20 x 20, #313942 `text.ink-body` |
| hover | background #e6e6e6; transition all 0.15s ease |
| focus-visible | background #e6e6e6; outline 2px solid #313942 `text.ink-body`, offset 2px; transition all 0.15s ease |
| pressed | background #e6e6e6; transition all 0.35s ease; transform translate(0px, 2px) |

![Google login default](components/crops/login-google-default.png) ![Google login hover](components/crops/login-google-hover.png) ![Google login focus-visible](components/crops/login-google-focus-visible.png) ![Google login pressed](components/crops/login-google-pressed.png)

#### Email field
The 380x50 email input; focused and typed then cleared, never submitted. Read as `login-email` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 380 x 50; padding 14px 18px; border 1px solid #e0e5eb `border.hairline`; radius 5px; background #ffffff `background.page`; text InterVariable 17/normal 400, #242424; transition all 0.15s ease; placeholder #242424 |
| focused, filled | border 1px solid rgba(47, 128, 237, 0.8); shadow rgba(99, 142, 216, 0.3) 0px 0px 10px 0px; outline 2px solid #242424, offset 2px |

![Email field default](components/crops/login-email-default.png) ![Email field focused](components/crops/login-email-focused.png) ![Email field filled](components/crops/login-email-filled.png)

#### Password field
The password input; focused and typed then cleared, never submitted. Read as `login-pass` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 380 x 50; padding 14px 18px; border 1px solid #e0e5eb `border.hairline`; radius 5px; background #ffffff `background.page`; text InterVariable 17/normal 400, #242424; transition all 0.15s ease; placeholder #242424 |
| focused, filled | border 1px solid rgba(47, 128, 237, 0.8); shadow rgba(99, 142, 216, 0.3) 0px 0px 10px 0px; outline 2px solid #242424, offset 2px |

![Password field default](components/crops/login-pass-default.png) ![Password field focused](components/crops/login-pass-focused.png) ![Password field filled](components/crops/login-pass-filled.png)

#### Login button
The blue Login submit (186x38.5, #2f80ed); measured, never pressed. Read as `login-submit` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 186 x 38.5; padding 8px 17px; radius 5px; background #2f80ed `action.auth-blue`; shadow rgba(47, 128, 237, 0.15) 0px 4px 9px 0px; text InterVariable 15/22.5 500, #ffffff `background.page`; transition all 0.3s ease |
| hover | background #1366d6 `action.auth-blue-hover`; shadow rgba(47, 128, 237, 0.2) 0px 6px 12px 0px |
| focus-visible | background #1366d6 `action.auth-blue-hover`; outline 2px solid #ffffff `background.page`, offset 2px |
| pressed | background #1366d6 `action.auth-blue-hover`; shadow rgba(47, 128, 237, 0.2) 0px 6px 12px 0px; transition all 0.35s ease; transform translate(0px, 2px) |

![Login button default](components/crops/login-submit-default.png) ![Login button hover](components/crops/login-submit-hover.png) ![Login button focus-visible](components/crops/login-submit-focus-visible.png) ![Login button pressed](components/crops/login-submit-pressed.png)

#### Create Account
The green "Create Account" pair button; measured, never followed. Read as `login-create` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 186 x 38.5; padding 8px 17px; radius 5px; background #27ae60 `action.accent`; shadow rgba(39, 174, 96, 0.15) 0px 4px 9px 0px; text InterVariable 15/22.5 500, #ffffff `background.page`; transition all 0.3s ease |
| hover | background #1e8449 `action.accent-hover`; shadow rgba(39, 174, 96, 0.2) 0px 6px 12px 0px; transition all 0.15s ease |
| focus-visible | background #1e8449 `action.accent-hover`; outline 2px solid #ffffff `background.page`, offset 2px; transition all 0.15s ease |
| pressed | background #1e8449 `action.accent-hover`; shadow rgba(39, 174, 96, 0.2) 0px 6px 12px 0px; transition all 0.35s ease; transform translate(0px, 2px) |

![Create Account default](components/crops/login-create-default.png) ![Create Account hover](components/crops/login-create-hover.png) ![Create Account focus-visible](components/crops/login-create-focus-visible.png) ![Create Account pressed](components/crops/login-create-pressed.png)

### Mobile (390 wide)

The phone surface at 390 wide: the mobile top bar, the 44px hero, the m-cta pill and the app surface at phone width.

#### Mobile header
The phone top bar with the wordmark and menu. Read as `m-header` on the mobile page at 390 wide.

**Values (default).** size 390 x 70; padding 0px 24px; background transparent; text InterVariable 15/22.5 400, #ffffff `background.page`; transition box-shadow 0.35s ease, transform 0.35s cubic-bezier(0.5, 0, 0.35, 1), opacity 0.35s cubic-bezier(0.5, 0, 0.35, 1), background 0.35s ease; layers a.button.round 0.0x0.0 #f49a40 `action.orange` 999px; span::before.menu-icon.sidebarTrigger 24pxx2px T:1px solid rgb(255, 255, 255) / R:1px solid rgb(255, 255, 255) / B:1px solid rgb(255, 255, 255) / L:1px solid rgb(255, 255, 255); span::after.menu-icon.sidebarTrigger 24pxx2px T:1px solid rgb(255, 255, 255) / R:1px solid rgb(255, 255, 255) / B:1px solid rgb(255, 255, 255) / L:1px solid rgb(255, 25.

Child layers that carry the look: a 0x0 background #f49a40 `action.orange` radius 999px; span::before 24pxx2px border 1px solid #ffffff `background.page`; span::after 24pxx2px border 1px solid #ffffff `background.page`.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile headline
The phone hero heading. Read as `m-h1` on the mobile page at 390 wide.

**Values (default).** size 343.22 x 158.39; background transparent; text InterVariable 44/52.8 600, #defaca.

![Mobile headline default](components/crops/m-h1-default.png)

#### Mobile CTA
The green Open App CTA on the phone; measured, never followed. Read as `m-cta` on the mobile page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 134 x 50; padding 13px 28px; radius 999px; background #27ae60 `action.accent`; shadow rgba(39, 174, 96, 0.15) 0px 4px 9px 0px; text InterVariable 16/24 500, #ffffff `background.page`; transition all 0.3s ease |
| hover | background #1e8449 `action.accent-hover`; shadow rgba(39, 174, 96, 0.2) 0px 6px 12px 0px; transition all 0.15s ease |
| focus-visible | background #1e8449 `action.accent-hover`; outline 2px solid #ffffff `background.page`, offset 2px; transition all 0.15s ease |
| pressed | background #1e8449 `action.accent-hover`; shadow rgba(39, 174, 96, 0.2) 0px 6px 12px 0px; transition all 0.35s ease; transform translate(0px, 2px) |

![Mobile CTA default](components/crops/m-cta-default.png) ![Mobile CTA hover](components/crops/m-cta-hover.png) ![Mobile CTA focus-visible](components/crops/m-cta-focus-visible.png) ![Mobile CTA pressed](components/crops/m-cta-pressed.png)

#### Mobile footer
The phone footer. Read as `m-footer` on the mobile page at 390 wide.

**Values (default).** size 390 x 1386.78; background #ffffff `background.page`; text InterVariable 14/23.8 400, #313942 `text.ink-body`; icon 36 x 36, #313942 `text.ink-body`.

![Mobile footer default](components/crops/m-footer-default.png)

### Footer

The sitemap footer on the long-scroll marketing surfaces.

#### Site footer
The sitemap footer (products, resources, legal links). Read as `site-footer` on the home page.

**Values (default).** size 1440 x 844.8; background #ffffff `background.page`; text InterVariable 14/23.8 400, #313942 `text.ink-body`; icon 36 x 36, #313942 `text.ink-body`.

![Site footer default](components/crops/site-footer-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Designmodo mark, product glyphs, the Font Awesome face set) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

The Postcards builder canvas, saving work and every post-login surface need an account and were never reached. What is genuinely public signed out: the marketing pages, /postcards/pricing, /email-templates, /postcards, /slides, the sign-in form and the Postcards app shell behind the Welcome-back modal - which is real product UI (header, sidebar, filters, gallery cards), not a stub; Escape dismissed the modal and the whole gallery was measured through it. No account was created and no form was ever submitted.

### Pages

- **Two systems.** The marketing surface and the Postcards app are different stacks: InterVariable marketing over dark heroes with #f49a40/#27ae60 actions, and a Fira Sans app shell with the #071c26 navy header, #2198ed/#485f6b actions and styled-components classes. Both are captured and documented separately.
- **Slides and Static.app.** /slides was captured as a product page; the off-viewport 'Add to cart' plan links sit in a slide panel that never mounts visibly signed out and were left out rather than fabricated.
- **Welcome-back modal.** /postcards/app/folder/templates mounts the auth modal over the gallery for signed-out visitors; every modal action was measured and none pressed.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.
- **The plan-link slide panel** on the home product strip renders off-viewport and was unreachable; the pricing page covers the plan actions honestly.

### Themes

Every public surface paints a single light theme signed out; the stylesheet carries no meaningful dark variant (the only declared custom properties are Font Awesome widget internals), so tokens.json keeps a real light set and an empty dark set rather than inventing one.

### Fonts

- **InterVariable** (marketing: nav, hero, pricing, forms) and **Fira Sans** (the Postcards app: sidebar, modal, gallery, badges) are the served faces. Source Serif 4 is loaded for article content. They are served from Google Fonts and the site CDN; the style guide falls back to system fonts.

### Screenshots

- The app gallery scrolls inside a nested container, not the document: desktop fulls are viewport-tall `partN` tiles, and the mobile app scroller is 14521px tall but capped at 8 tiles (6752px) - the cap is a recorded boundary, not a missing save.
- A transient edge challenge appeared once during capture (the app route) and cleared on retry; no route stayed blocked.
- Screenshots are 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Template names, thumbnails and marketing copy are the product's content; only frames and components were measured.
