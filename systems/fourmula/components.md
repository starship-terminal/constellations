# Fourmula components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from fourmula.ai and app.fourmula.ai on 2026-11-15, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; the sign-in fields were typed into then cleared, never sent; every link, CTA and submit was measured, never followed or pressed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (78 components, 176 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 15/22.5 600, #23252b`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (173 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-{state}.png` where the theme is the painted surface: `light` is the marketing site's first-visit paint (`.body.dark`, isDarkMode=true — the class name is inverted in the site's own code) and `dark` is either the site's own dark paint (plain `.body`) or the dark-only app. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x (bounded to 8 viewport chunks where a page runs long, with the boundary noted in the sidecars); mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-dark-default.png), [full](screenshots/home-dark-full.png), [menu](screenshots/home-dark-menu.png), [cookie](screenshots/home-light-cookie.png), [default](screenshots/home-light-default.png), [faq-opened](screenshots/home-light-faq-opened.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| Privacy policy | `/privacy-policy` | [default](screenshots/privacy-light-default.png), [full](screenshots/privacy-light-full.png) |
| Terms of service | `/terms-of-service` | [default](screenshots/terms-dark-default.png), [default](screenshots/terms-light-default.png), [full](screenshots/terms-light-full.png) |
| App start | `app.fourmula.ai/start` | [default](screenshots/start-dark-default.png), [menu](screenshots/start-dark-menu.png) |
| App sign-in | `app.fourmula.ai/auth` | [default](screenshots/auth-dark-default.png), [forgot](screenshots/auth-dark-forgot.png), [signup](screenshots/auth-dark-signup.png) |
| Create-PDP generator | `app.fourmula.ai/project/create-pdp` | [default](screenshots/create-pdp-dark-default.png), [menu](screenshots/create-pdp-dark-menu.png), [pdp-dialog](screenshots/create-pdp-dark-pdp-dialog.png), [recommendations](screenshots/create-pdp-dark-recommendations.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-dark-default.png), [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| App start, phone | `app.fourmula.ai/start` | [default](screenshots/mobile-start-dark-default.png) |
| App sign-in, phone | `app.fourmula.ai/auth` | [default](screenshots/mobile-auth-dark-default.png) |
| Create-PDP, phone | `app.fourmula.ai/project/create-pdp` | [default](screenshots/mobile-create-pdp-dark-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Cookie consent | every marketing page | the @finsweet layer (.cookies) mounts on every first load; it was shot once as seen, the Settings toggle was clicked to reach the preference manager, then the layer was hidden — Accept all / Save changes were never pressed | [home-light-cookie](screenshots/home-light-cookie.png), [cookie-modal](#cookie-consent-modal) |
| Nav overlay | every marketing page header | the header Menu pill's own toggle | [home-light-menu](screenshots/home-light-menu.png), [home-dark-menu](screenshots/home-dark-menu.png), [nav-overlay](#nav-overlay) |
| FAQ accordion | home page | a FAQ row's own toggle | [home-light-faq-opened](screenshots/home-light-faq-opened.png), [faq-item](#faq-row) |
| Theme toggle | the header pill | not pressed during measurement (it repaints the whole page); both painted themes were instead reached through the site's own isDarkMode storage key — the same key the toggle writes | [home-dark-default](screenshots/home-dark-default.png), [mkt-header-dark](#site-header-dark-paint) |
| Sign-in card switcher | app.fourmula.ai/auth | the card's own Sign up switcher (a local UI toggle); "Forgot password?" is a validating submit, so the reset view is uncaptured | [auth-dark-signup](screenshots/auth-dark-signup.png), [auth-signup-card](#create-account-view), [auth-forgot-card](#forgot-password-view-uncaptured) |
| Create-PDP dialogs | app.fourmula.ai/project/create-pdp | the What's-a-PDP and Recommendations triggers (local UI toggles), dismissed with Escape | [create-pdp-dark-pdp-dialog](screenshots/create-pdp-dark-pdp-dialog.png), [pdp-what-dialog](#pdp-explainer-dialog), [pdp-reco-dialog](#recommendations-dialog) |
| Sign-in fields | app.fourmula.ai/auth | typed into then cleared — nothing sent | [auth-field-email](#email-field), [auth-field-pass](#password-field) |
| Signed-in product | a Fourmula account | the dashboard, generation results and every post-login surface need an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 19 components were given a real keyboard focus. 0 draw an outline ring: . The other 19 show no measured change: `account-link`, `header-cta`, `ai-btn`, `how-cta`, `step-cta`, `footer-link`, `app-menu-btn`, `app-create-btn`, `app-signin-btn`, `start-cta`, `auth-back`, `auth-google`, `auth-submit`, `app-menu-btn-pdp`, `pdp-cancel`, `pdp-dash-link`, `pdp-upload`, `pdp-add-product`, `pdp-shopify-cta`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, -webkit-backdrop-filter, -webkit-text-decoration-color, backdrop-filter, background-color, border-color, box-shadow, color, content-visibility, display, fill, filter, opacity, outline-color, overlay, pointer-events, rotate, scale, stroke, text-decoration-color, transform, translate | pdp-format-static, pdp-format-video |
| 0.2s | `cubic-bezier(0, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, -webkit-backdrop-filter, -webkit-text-decoration-color, backdrop-filter, background-color, border-color, box-shadow, color, content-visibility, display, fill, filter, opacity, outline-color, overlay, pointer-events, rotate, scale, stroke, text-decoration-color, transform, translate | pdp-reco, pdp-reco-dialog, pdp-what-dialog |
| 0.2s | `cubic-bezier(0.25, 0.46, 0.45, 0.94)` | all | cookie-check |
| 0.2s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, -webkit-text-decoration-color, background-color, border-color, color, fill, opacity, outline-color, stroke, text-decoration-color | app-create-btn, app-menu-btn, app-menu-btn-pdp, app-signin-btn, auth-back, auth-eye, auth-forgot, auth-google and more |
| 0.2s | `ease` | all, opacity | account-link, ai-btn, cookie-accept, cookie-save, cookie-settings, footer-link, header-cta, header-cta-dark and more |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Cookie consent modal](#cookie-consent-modal) | 1440 x 900 | - | - | transparent | none | 13.3084px |
| [Nav overlay](#nav-overlay) | 1440 x 528.98 | - | - | transparent | none | 9.98131px 0px 0px 0px |
| [Sign-in card](#sign-in-card) | 384 x 468.8 | 1px solid #1a1a1a `core.appColor.base-700` | 28px | #111111 `core.appColor.base-800` | none | 24px 32px |
| [Create-account view](#create-account-view) | 384 x 435.8 | 1px solid #1a1a1a `core.appColor.base-700` | 28px | #111111 `core.appColor.base-800` | none | 24px 32px |
| [Recommendations dialog](#recommendations-dialog) | 480 x 655.86 | - | 28px | #1e1e1e `core.appColor.base-750` | none | 32px 48px |
| [PDP explainer dialog](#pdp-explainer-dialog) | 880 x 448.38 | - | 28px | #1e1e1e `core.appColor.base-750` | none | 24px |
| [Format radiogroup](#format-radiogroup) | 564 x 60 | - | - | transparent | none | 0 |
| [Mobile nav overlay](#mobile-nav-overlay) | 390 x 499.7 | - | - | transparent | none | 12.0928px 10.4804px 0px 0px |
| [App header](#app-header) | 1392 x 56 | - | 3.35544e+07px | #020108 `core.appColor.base-900` | none | 0px 16px |

## Components

### Cookie consent

The @finsweet cookie-consent layer (.cookies) that mounts on every first load of the marketing site: the bottom-right banner, the Settings outline button that opens the in-page preference manager, its category checkboxes and the Accept all / Save changes pair — measured, then hidden, never answered.

#### Cookie consent modal
The @finsweet consent modal shown on first load ("By clicking Accept all…"): the banner plus the cookie-preference manager. Measured, then hidden — never answered. Read as `cookie-modal` on the home page.

**Values (default).** size 1440 x 900; padding 13.3084px; background transparent; text Sf Pro Display 19.96/29.94 500, #020108 `light.background.menu`; transform translate(0px, 10px); opacity 0; icon 19.95 x 19.95, rgba(2, 1, 8, 0.3) `light.text.faint`; layers div.cookies__modal__main 359.3x186.7 rgb(217, 217, 217) 39.9252px; a.cookies__modal__close.w-inline-block 33.3x33.3 rgb(247, 247, 247) 39.9252px; div.fs-cc_modal-buttons 359.3x66.5 rgb(217, 217, 217) 39.9252px; a.btn-primary.u-btn 150.4x39.9 rgb(2, 1, 8) 1317.53px; a.btn-outline.u-btn 152.4x39.9 rgb(217, 217, 217) T:1px solid rgba(2, 1, 8, 0.2) / R:1px solid rgba(2, 1, 8, 0.2) / B:1px solid rgba(2.

Child layers that carry the look: div 359.3x186.7 background #d9d9d9 `light.background.dots` radius 39.9252px; a 33.3x33.3 background #f7f7f7 `light.background.surface` radius 39.9252px; div 359.3x66.5 background #d9d9d9 `light.background.dots` radius 39.9252px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Accept all button
The filled "Accept all" in the consent modal; measured, never pressed. Read as `cookie-accept` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 150.39 x 39.92; padding 11.6449px 19.9626px; radius 1317.53px; background #020108 `light.background.menu`; text Sf Pro Display 14.14/16.96 400, #ffffff `light.background.page`; transition all 0.2s ease |
| hover | background #146ef5 |

![Accept all button default](components/crops/cookie-accept-default.png) ![Accept all button hover](components/crops/cookie-accept-hover.png)

#### Save changes button
The outline "Save changes" inside the opened preference manager; measured, never pressed. Read as `cookie-save` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 198.98 x 39.92; padding 11.6449px 19.9626px; border 1px solid rgba(2, 1, 8, 0.2) `light.text.hairlineInk`; radius 1317.53px; background #d9d9d9 `light.background.dots`; text Sf Pro Display 14.14/16.96 400, #020108 `light.background.menu`; transition all 0.2s ease |
| hover | border 1px solid #146ef5; text Sf Pro Display 14.14/16.96 400, #146ef5 |

![Save changes button default](components/crops/cookie-save-default.png) ![Save changes button hover](components/crops/cookie-save-hover.png)

#### Settings button
The outline "Settings" that opens the cookie-preference manager in place — a local UI toggle accepting nothing; the opened state was measured after clicking it, and the manager was left open to measure its controls. Read as `cookie-settings` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 152.39 x 39.92; padding 11.6449px 19.9626px; border 1px solid rgba(2, 1, 8, 0.2) `light.text.hairlineInk`; radius 1317.53px; background #d9d9d9 `light.background.dots`; text Sf Pro Display 14.14/16.96 400, #020108 `light.background.menu`; transition all 0.2s ease |
| hover | border 1px solid #146ef5; text Sf Pro Display 14.14/16.96 400, #146ef5 |
| opened | size 0 x 0 |

![Settings button default](components/crops/cookie-settings-default.png) ![Settings button hover](components/crops/cookie-settings-hover.png)

#### Consent checkbox row
A category checkbox row in the opened preference manager (Strictly necessary is forced active); measured, never toggled. Read as `cookie-check` on the home page.

**Values (default).** size 399.27 x 73.19; padding 13.3084px 19.9626px 19.9626px 46.5794px; border 1px solid #f7f7f7 `light.background.surface`; radius 19.9626px; background #d9d9d9 `light.background.dots`; text Sf Pro Display 13.30/19.96 500, #020108 `light.background.menu`; transition all 0.2s cubic-bezier(0.25, 0.46, 0.45, 0.94); layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1.

![Consent checkbox row default](components/crops/cookie-check-default.png)

### Site chrome

The 91px header on every marketing page: the fourmula.ai logo-and-wordmark, the centre pill holding the Menu toggle, the sun/moon theme switch (data-theme-toggle — writes isDarkMode, .body.dark paints LIGHT) and the scroll-percentage counter, the icon-only Fourmula-app account link and the Get started pill. A second set of entries re-reads the same chrome under the site's own dark paint (plain .body, isDarkMode=false).

#### Site header
The 91px header: the logo-and-wordmark, the centre Menu pill with the theme toggle and scroll-percentage counter, the Fourmula-app account icon-link and the Get started pill. Read as `mkt-header` on the home page.

**Values (default).** size 1440 x 92.48; padding 19.9626px 26.6168px; background transparent; text Sf Pro Display 14.14/16.96 400, #ffffff `light.background.page`; transition all 0.2s ease; icon 48.56 x 46.58, #020108 `light.background.menu`; layers div.header__main 206.2x39.9 rgb(2, 1, 8) 1317.53px; div.header__menu-line.is-top 22.0x0.8 rgb(255, 255, 255); div.header__menu-line.is-bottom 22.0x0.8 rgb(255, 255, 255); div.header__theme 26.6x26.6 T:1px solid rgba(255, 255, 255, 0.2) / R:1px solid rgba(255, 255, 255, 0.2) / B:1px solid rgba(255, 255, 255, 0.2) / L:1px solid rgba(255, 255, 255, 0.2) 1317.53px; div.header__prc 47.9x26.6 rgba(255, .

Child layers that carry the look: div 206.2x39.9 background #020108 `light.background.menu` radius 1317.53px; div 22x0.8 background #ffffff `light.background.page`; div 22x0.8 background #ffffff `light.background.page`.

![Site header default](components/crops/mkt-header-default.png)

#### Logo
The header's fourmula.ai logo-and-wordmark. Read as `mkt-logo` on the home page.

**Values (default).** size 143.06 x 52.58; background transparent; text Arial 14.4/20 400, #333333; icon 48.56 x 46.58, #020108 `light.background.menu`.

![Logo default](components/crops/mkt-logo-default.png)

#### Menu pill
The header's centre "Menu" pill (lines icon + label) — a local UI toggle that opens the fixed .menu overlay; the opened state was measured after clicking it, then closed. Read as `menu-pill` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 78.48 x 35.23; padding 6.65421px 0px 6.65421px 6.65421px; background transparent; text Sf Pro Display 14.14/16.96 400, #ffffff `light.background.page`; transition opacity 0.2s ease; layers div.header__menu-line.is-top 22.0x0.8 rgb(255, 255, 255); div.header__menu-line.is-bottom 22.0x0.8 rgb(255, 255, 255) |
| hover, pressed | opacity 0.64 |
| opened | opacity 0.64; layers div.header__menu-line.is-top 16.1x16.1 rgb(255, 255, 255); div.header__menu-line.is-bottom 16.1x16.1 rgb(255, 255, 255) |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: div 22x0.8 background #ffffff `light.background.page`; div 22x0.8 background #ffffff `light.background.page`.

![Menu pill default](components/crops/menu-pill-default.png) ![Menu pill hover](components/crops/menu-pill-hover.png) ![Menu pill pressed](components/crops/menu-pill-pressed.png) ![Menu pill opened](components/crops/menu-pill-opened.png)

#### Theme toggle
The sun/moon half of the header pill — writes localStorage isDarkMode and flips body.dark (note .body.dark paints the LIGHT surface). Never pressed here; both paints are captured as separate pages instead. Read as `theme-toggle` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 26.61 x 26.61; border 1px solid rgba(255, 255, 255, 0.2) `light.background.counter`; radius 1317.53px; background transparent; text Arial 14.4/20 400, #333333; transition all 0.2s ease; icon 13.3 x 13.3, #ffffff `light.background.page` |
| hover | border 1px solid rgba(255, 255, 255, 0.65) |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Theme toggle default](components/crops/theme-toggle-default.png) ![Theme toggle hover](components/crops/theme-toggle-hover.png)

#### Scroll-percentage counter
The "0%" readout inside the header pill that counts down scroll progress through the page. Read as `prc-counter` on the home page.

**Values (default).** size 47.89 x 26.61; padding 0px 7.31963px; radius 1317.53px; background rgba(255, 255, 255, 0.2) `light.background.counter`; text Sf Pro Display 14.14/16.96 400, #ffffff `light.background.page`.

![Scroll-percentage counter default](components/crops/prc-counter-default.png)

#### App account link
The icon-only "Fourmula app account" link to app.fourmula.ai/auth; measured, never followed. Read as `account-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 26.61 x 26.61; border 1px solid rgba(2, 1, 8, 0.2) `light.text.hairlineInk`; radius 26.6168px; background transparent; text Arial 14.4/20 400, #020108 `light.background.menu`; transition all 0.2s ease; icon 13.3 x 13.3, #020108 `light.background.menu` |
| hover, pressed | border 1px solid rgba(2, 1, 8, 0.64) `light.text.muted` |

![App account link default](components/crops/account-link-default.png) ![App account link hover](components/crops/account-link-hover.png) ![App account link focus-visible](components/crops/account-link-focus-visible.png) ![App account link pressed](components/crops/account-link-pressed.png)

#### Get started button
The primary "Get started" pill in the header linking to app.fourmula.ai/start; measured, never followed. Read as `header-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 101.81 x 39.92; padding 11.6449px 19.9626px; radius 1317.53px; background #020108 `light.background.menu`; text Sf Pro Display 14.14/16.96 400, #ffffff `light.background.page`; transition all 0.2s ease |
| hover, pressed | background #ff6b02 |

![Get started button default](components/crops/header-cta-default.png) ![Get started button hover](components/crops/header-cta-hover.png) ![Get started button focus-visible](components/crops/header-cta-focus-visible.png) ![Get started button pressed](components/crops/header-cta-pressed.png)

#### Site header (dark paint)
The 91px header under the site's dark paint (plain .body, isDarkMode=false): the Menu pill, the theme toggle, the scroll-percentage counter, the account icon-link and the Get started pill. Read as `mkt-header-dark` on the home (dark paint) page.

**Values (default).** size 1440 x 92.48; padding 19.9626px 26.6168px; background transparent; text Sf Pro Display 14.14/16.96 400, #ffffff `dark.text.ink`; transition all 0.2s ease; icon 48.56 x 46.58, #ffffff `dark.text.ink`; layers div.header__main 206.2x39.9 rgb(39, 39, 39) 1317.53px; div.header__menu-line.is-top 22.0x0.8 rgb(255, 255, 255); div.header__menu-line.is-bottom 22.0x0.8 rgb(255, 255, 255); div.header__theme 26.6x26.6 T:1px solid rgba(255, 255, 255, 0.2) / R:1px solid rgba(255, 255, 255, 0.2) / B:1px solid rgba(255, 255, 255, 0.2) / L:1px solid rgba(255, 255, 255, 0.2) 1317.53px; div.header__prc 47.9x26.6 rgba(25.

Child layers that carry the look: div 206.2x39.9 background #272727 `dark.background.menu` radius 1317.53px; div 22x0.8 background #ffffff `dark.text.ink`; div 22x0.8 background #ffffff `dark.text.ink`.

![Site header (dark paint) default](components/crops/mkt-header-dark-default.png)

#### Menu pill (dark paint)
The header's centre "Menu" pill under the dark paint. Read as `menu-pill-dark` on the home (dark paint) page.

**Values (default).** size 78.48 x 35.23; padding 6.65421px 0px 6.65421px 6.65421px; background transparent; text Sf Pro Display 14.14/16.96 400, #ffffff `dark.text.ink`; transition opacity 0.2s ease; layers div.header__menu-line.is-top 22.0x0.8 rgb(255, 255, 255); div.header__menu-line.is-bottom 22.0x0.8 rgb(255, 255, 255).

Child layers that carry the look: div 22x0.8 background #ffffff `dark.text.ink`; div 22x0.8 background #ffffff `dark.text.ink`.

![Menu pill (dark paint) default](components/crops/menu-pill-dark-default.png)

#### Get started button (dark paint)
The header's primary "Get started" pill under the dark paint; measured, never followed. Read as `header-cta-dark` on the home (dark paint) page.

**Values (default).** size 101.81 x 39.92; padding 11.6449px 19.9626px; radius 1317.53px; background #ffffff `dark.text.ink`; text Sf Pro Display 14.14/16.96 400, #020108 `dark.background.page`; transition all 0.2s ease.

![Get started button (dark paint) default](components/crops/header-cta-dark-default.png)

### Nav overlay

The fixed .menu overlay the Menu pill opens: PDP's / Products / Videos / Our features anchors, Privacy Policy / Terms of Service / Cookie Policy, Instagram / Linkedin / Youtube and the app account link — never followed.

#### Nav overlay
The fixed .menu overlay opened by the Menu pill: PDP's / Products / Videos / Our features anchors, Privacy/Terms/Cookie links, Instagram and the app account link. Its links were never followed. Read as `nav-overlay` on the home page.

**Values (opened).** size 1440 x 528.98; padding 9.98131px 0px 0px 0px; background transparent; text Sf Pro Display 9.98/14.97 400, rgba(2, 1, 8, 0.5) `light.text.dim`; transition all 0.2s ease; icon 13.3 x 13.3, #020108 `light.background.menu`; layers div.menu__wrap 239.5x519.0 rgb(217, 217, 217) 26.6168px; div.menu__item.is-lined 206.3x102.2 T:1px solid rgba(2, 1, 8, 0.2); a.btn-primary.u-btn 0.0x0.0 rgb(2, 1, 8) 1317.53px; a.header_signin.w-inline-block 26.6x26.6 T:1px solid rgba(255, 255, 255, 0.2) / R:1px solid rgba(255, 255, 255, 0.2) / B:1px solid rgba(255, 255, 255, 0.2) / L:1px solid rgba(255, 255, 255, 0.2) 26.6168px.

Child layers that carry the look: div 239.5x519 background #d9d9d9 `light.background.dots` radius 26.6168px; div 206.3x102.2 border 1px solid rgba(2, 1, 8, 0.2) `light.text.hairlineInk`; a 0x0 background #020108 `light.background.menu` radius 1317.53px.

![Nav overlay opened](components/crops/nav-overlay-opened.png)

#### Nav overlay link
An anchor link inside the opened .menu overlay ("PDP's"); measured, never followed. Read as `nav-overlay-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 206.3 x 29.95; background transparent; text Sf Pro Display 19.96/29.94 500, #020108 `light.background.menu`; transition opacity 0.2s ease |

![Nav overlay link default](components/crops/nav-overlay-link-default.png) ![Nav overlay link hover](components/crops/nav-overlay-link-hover.png)

### Home

The fourmula.ai hero — 'Your catalog, instantly re-shot.' with the second line in --fonts-50, the rotating keyword chips at the right edge (PDPs / UGC / Lifestyle shots / Ads / Stories / Street style), the SCROLL DOWN cue — and the sections below: On-brand visuals, the AI features with their round app links, How It Works, the four steps with their Get started buttons.

#### Hero headline
"Your catalog, instantly re-shot." — the display h1; the second line paints --fonts-50 (u-fonts-50). Read as `hero-h1` on the home page.

**Values (default).** size 485.36 x 137.59; background transparent; text Sf Pro Display 73.19/68.80 400, #020108 `light.background.menu`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero keyword chip
A chip in the hero's right-edge rotating word column (PDPs / UGC / Lifestyle shots / Ads / Stories / Street style). Read as `hero-word` on the home page.

**Values (default).** size 58.91 x 31.94; padding 4.65794px 13.3084px 5.32336px 13.3084px; border 1px solid rgba(2, 1, 8, 0.2) `light.text.hairlineInk`; radius 6.65421px; background #ffffff `light.background.page`; text Sf Pro Display 13.30/19.96 500, #020108 `light.background.menu`.

![Hero keyword chip default](components/crops/hero-word-default.png)

#### Scroll-down cue
The "SCROLL DOWN" micro-label at the hero's bottom right, an in-page anchor to #what-is-fourmula; measured, never followed. Read as `hero-scroll` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 56.2 x 8.31; background transparent; text Sf Pro Display 8.31/8.31 500, #020108 `light.background.menu` |

![Scroll-down cue default](components/crops/hero-scroll-default.png) ![Scroll-down cue hover](components/crops/hero-scroll-hover.png)

#### Section heading
"On-brand visuals. Made by AI." — the u-h2 section heading style. Read as `section-h2` on the home page.

**Values (default).** size 686.11 x 199.63; background transparent; text Sf Pro Display 99.81/99.81 400, #020108 `light.background.menu`.

![Section heading default](components/crops/section-h2-default.png)

#### Round app link
The 53px round icon-link ("fourmula.ai") into app.fourmula.ai/start, repeated beside the AI feature copy; measured, never followed. Read as `ai-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 53.22 x 53.22; radius 1317.53px; background #ffffff `light.background.page`; text Arial 14.4/20 400, #000000; transition all 0.2s ease; icon 26.61 x 26.61, #000000 |
| hover, pressed | size 47.9 x 47.9; background #ff6b02; transform scale(0.9); icon 23.95 x 23.95, #000000 |

![Round app link default](components/crops/ai-btn-default.png) ![Round app link hover](components/crops/ai-btn-hover.png) ![Round app link focus-visible](components/crops/ai-btn-focus-visible.png) ![Round app link pressed](components/crops/ai-btn-pressed.png)

#### How-it-works CTA
The "Get started" pill in the How It Works section; measured, never followed. Read as `how-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 101.81 x 39.92; padding 11.6449px 19.9626px; radius 1317.53px; background #020108 `light.background.menu`; text Sf Pro Display 14.14/16.96 400, #ffffff `light.background.page`; transition all 0.2s ease |
| hover | background #ec6302 |
| pressed | background #ff6b02 |

![How-it-works CTA default](components/crops/how-cta-default.png) ![How-it-works CTA hover](components/crops/how-cta-hover.png) ![How-it-works CTA focus-visible](components/crops/how-cta-focus-visible.png) ![How-it-works CTA pressed](components/crops/how-cta-pressed.png)

#### Step heading
A u-h2-5 step heading in the "From idea to assets in four steps" section. Read as `step-h3` on the home page.

**Values (default).** size 693.39 x 106.47; background transparent; text Sf Pro Display 53.23/53.23 400, #ffffff `light.background.page`.

![Step heading default](components/crops/step-h3-default.png)

#### Step CTA
The "Get started" button repeated beside each of the four steps, linking to app.fourmula.ai/start; measured, never followed. Read as `step-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 101.81 x 39.92; padding 11.6449px 19.9626px; radius 1317.53px; background #ffffff `light.background.page`; text Sf Pro Display 14.14/16.96 400, #020108 `light.background.menu`; transition all 0.2s ease |
| hover | background #06050c; text Sf Pro Display 14.14/16.96 400, #fbfbfb |
| pressed | background #020108 `light.background.menu`; text Sf Pro Display 14.14/16.96 400, #ffffff `light.background.page` |

![Step CTA default](components/crops/step-cta-default.png) ![Step CTA hover](components/crops/step-cta-hover.png) ![Step CTA focus-visible](components/crops/step-cta-focus-visible.png) ![Step CTA pressed](components/crops/step-cta-pressed.png)

#### Hero headline (dark paint)
"Your catalog, instantly re-shot." under the dark paint — the second line picks up --fonts-50. Read as `hero-h1-dark` on the home (dark paint) page.

**Values (default).** size 485.36 x 137.59; background transparent; text Sf Pro Display 73.19/68.80 400, #ffffff `dark.text.ink`.

![Hero headline (dark paint) default](components/crops/hero-h1-dark-default.png)

#### Step CTA (dark paint)
A "Get started" button in the four-steps section under the dark paint; measured, never followed. Read as `step-cta-dark` on the home (dark paint) page.

**Values (default).** size 101.81 x 39.92; padding 11.6449px 19.9626px; radius 1317.53px; background #ffffff `dark.text.ink`; text Sf Pro Display 14.14/16.96 400, #020108 `dark.background.page`; transition all 0.2s ease.

![Step CTA (dark paint) default](components/crops/step-cta-dark-default.png)

### FAQ accordion

The FAQ rows at the foot of the home page — a local UI toggle whose + flips and whose answer expands on click.

#### FAQ row
A FAQ accordion row ("What can AI FOURMULA create for my brand?") — a local UI toggle whose + icon flips and the answer expands; the opened state was measured after clicking, then re-closed by toggling again. Read as `faq-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1060.72 x 75.02; padding 26.6168px; border B: 1px solid #d7d7d6 `light.border.rule`; background transparent; text Sf Pro Display 16.63/20.79 500, #020108 `light.background.menu`; layers div.faq__item 1060.7x75.0 B:1px solid rgb(215, 215, 214) |
| opened | size 1060.72 x 118.02; layers div.faq__item.active 1060.7x118.0 B:1px solid rgb(215, 215, 214) |

Child layers that carry the look: div 1060.7x75 border 1px solid #d7d7d6 `light.border.rule`.

![FAQ row default](components/crops/faq-item-default.png) ![FAQ row hover](components/crops/faq-item-hover.png) ![FAQ row opened](components/crops/faq-item-opened.png)

#### FAQ row (dark paint)
A closed FAQ accordion row under the dark paint. Read as `faq-item-dark` on the home (dark paint) page.

**Values (default).** size 1060.72 x 75.02; padding 26.6168px; border B: 1px solid #2a2a30 `dark.border.rule`; background transparent; text Sf Pro Display 16.63/20.79 500, #ffffff `dark.text.ink`; layers div.faq__item 1060.7x75.0 B:1px solid rgb(42, 42, 48).

Child layers that carry the look: div 1060.7x75 border 1px solid #2a2a30 `dark.border.rule`.

![FAQ row (dark paint) default](components/crops/faq-item-dark-default.png)

### Legal pages

The /privacy-policy template (shared by /terms-of-service): the .tech section with its big title, last-updated line and long unclassed prose.

#### Legal page title
"PRIVACY & COOKIES POLICY" — the legal page heading. Read as `legal-title` on the privacy-policy page.

**Values (default).** size 1386.78 x 153.72; background transparent; text Sf Pro Display 73.19/76.85 500, #020108 `light.background.menu`.

![Legal page title default](components/crops/legal-title-default.png)

#### Legal body copy
A body paragraph in the privacy policy — the legal prose text style. Read as `legal-body` on the privacy-policy page.

**Values (default).** size 1386.78 x 67.36; background transparent; text Arial 14.97/22.45 400, #020108 `light.background.menu`.

![Legal body copy default](components/crops/legal-body-default.png)

#### Legal inline link
A link inside the privacy-policy prose; measured, never followed. Read as `legal-link` on the privacy-policy page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 78.23 x 17; background transparent; text Arial 14.97/17.96 400, #020108 `light.background.menu` |

![Legal inline link default](components/crops/legal-link-default.png) ![Legal inline link hover](components/crops/legal-link-hover.png)

#### Legal section
The .tech section the legal pages paint their prose in. Read as `legal-section` on the privacy-policy page.

**Values (default).** size 1440 x 6033.16; padding 106.467px 26.6168px 0px 26.6168px; background transparent; text Sf Pro Display 73.19/76.85 500, #020108 `light.background.menu`; layers th.tech__rich-cell.is-head 159.5x36.5 rgba(0, 0, 0, 0.04) B:2px solid rgba(0, 0, 0, 0.25); th.tech__rich-cell.is-head 455.8x36.5 rgba(0, 0, 0, 0.04) B:2px solid rgba(0, 0, 0, 0.25); th.tech__rich-cell.is-head 411.2x36.5 rgba(0, 0, 0, 0.04) B:2px solid rgba(0, 0, 0, 0.25); th.tech__rich-cell.is-head 360.3x36.5 rgba(0, 0, 0, 0.04) B:2px solid rgba(0, 0, 0, 0.25); td.tech__rich-cell 159.5x68.2 B:1px .

Child layers that carry the look: th 159.5x36.5 background rgba(0, 0, 0, 0.04) border 2px solid rgba(0, 0, 0, 0.25); th 455.8x36.5 background rgba(0, 0, 0, 0.04) border 2px solid rgba(0, 0, 0, 0.25); th 411.2x36.5 background rgba(0, 0, 0, 0.04) border 2px solid rgba(0, 0, 0, 0.25).

![Legal section default](components/crops/legal-section-default.png)

### App chrome

The floating rounded-full header every app.fourmula.ai page paints (1392x56, fixed at 24,24): the 32px Open-main-menu icon button, the header Create asset submit and the Sign in button — all measured, never pressed.

#### App menu button
The 32px icon button (aria "Open main menu") in the app header — a local UI toggle that opens the nav drawer; the opened state was measured after clicking it, then the drawer was closed with Escape. Read as `app-menu-btn` on the app auth page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 32 x 32; background transparent; text sfProFont 16/24 400, #ffffff `core.appColor.base-100`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 32 x 32, #ffffff `core.appColor.base-100` |
| hover, pressed, opened | text sfProFont 16/24 400, #f94a00 `core.appColor.accent-600`; icon 32 x 32, #f94a00 `core.appColor.accent-600` |

![App menu button default](components/crops/app-menu-btn-default.png) ![App menu button hover](components/crops/app-menu-btn-hover.png) ![App menu button focus-visible](components/crops/app-menu-btn-focus-visible.png) ![App menu button pressed](components/crops/app-menu-btn-pressed.png) ![App menu button opened](components/crops/app-menu-btn-opened.png)

#### Create asset button
The header's "Create asset" submit — its states were measured but it was never pressed (it would start an authenticated action). Read as `app-create-btn` on the app auth page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 123 x 32; padding 0px 12px 0px 8px; radius 3.35544e+07px; background #ff6b02 `core.appColor.accent-500`; text sfProFont 14/20 400, #020108 `core.appColor.base-900`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #020108 `core.appColor.base-900` |
| hover, pressed | background #f94a00 `core.appColor.accent-600` |

![Create asset button default](components/crops/app-create-btn-default.png) ![Create asset button hover](components/crops/app-create-btn-hover.png) ![Create asset button focus-visible](components/crops/app-create-btn-focus-visible.png) ![Create asset button pressed](components/crops/app-create-btn-pressed.png)

#### Sign in button
The header's "Sign in" button (aria "Sign in to your account"); measured, never pressed. Read as `app-signin-btn` on the app auth page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 66 x 32; padding 0px 12px; radius 3.35544e+07px; background oklab(0.702262 0.141683 0.141613 / 0.2); text sfProFont 14/20 400, #ff6b02 `core.appColor.accent-500`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | background oklab(0.702262 0.141683 0.141613 / 0.35) |

![Sign in button default](components/crops/app-signin-btn-default.png) ![Sign in button hover](components/crops/app-signin-btn-hover.png) ![Sign in button focus-visible](components/crops/app-signin-btn-focus-visible.png) ![Sign in button pressed](components/crops/app-signin-btn-pressed.png)

#### App menu button
The 32px icon button (aria "Open main menu") in the app header — a local UI toggle that opens the nav drawer; the opened state was measured after clicking it, then the drawer was closed with Escape. Read as `app-menu-btn-pdp` on the app create-pdp page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 32 x 32; background transparent; text sfProFont 16/24 400, #ffffff `core.appColor.base-100`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 32 x 32, #ffffff `core.appColor.base-100` |
| hover, pressed, opened | text sfProFont 16/24 400, #f94a00 `core.appColor.accent-600`; icon 32 x 32, #f94a00 `core.appColor.accent-600` |

![App menu button default](components/crops/app-menu-btn-pdp-default.png) ![App menu button hover](components/crops/app-menu-btn-pdp-hover.png) ![App menu button focus-visible](components/crops/app-menu-btn-pdp-focus-visible.png) ![App menu button pressed](components/crops/app-menu-btn-pdp-pressed.png) ![App menu button opened](components/crops/app-menu-btn-pdp-opened.png)

#### App header
The app's floating header — a fixed rounded-full bar (1392x56 at 24,24) holding the menu button, the Create asset submit and the Sign in button. Read as `app-header` on the app auth page.

**Values (default).** size 1392 x 56; padding 0px 16px; radius 3.35544e+07px; background #020108 `core.appColor.base-900`; text sfProFont 14/20 400, #020108 `core.appColor.base-900`; icon 32 x 32, #ffffff `core.appColor.base-100`.

![App header default](components/crops/app-header-default.png)

### App start

app.fourmula.ai/start — the signed-out start page ('Create studio-quality product photos', page title 'Formula AI | Start') with its large Create asset call-to-action, measured and never pressed.

#### Start headline
"Create studio-quality product photos" — the signed-out start-page masthead (the page titles itself "Formula AI | Start"). Read as `start-h1` on the app start page.

**Values (default).** size 432.33 x 104; background transparent; text sfProFont 52/52 500, #ffffff `core.appColor.base-100`.

![Start headline default](components/crops/start-h1-default.png)

#### Start CTA
The large "Create asset" button in the start-page body; its states were measured but it was never pressed. Read as `start-cta` on the app start page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 139 x 40; padding 0px 24px 0px 12px; radius 3.35544e+07px; background #ff6b02 `core.appColor.accent-500`; text sfProFont 14/20 400, #020108 `core.appColor.base-900`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #020108 `core.appColor.base-900` |
| hover, pressed | background #f94a00 `core.appColor.accent-600` |

![Start CTA default](components/crops/start-cta-default.png) ![Start CTA hover](components/crops/start-cta-hover.png) ![Start CTA focus-visible](components/crops/start-cta-focus-visible.png) ![Start CTA pressed](components/crops/start-cta-pressed.png)

### App sign-in

app.fourmula.ai/auth — the sign-in card over the dark field: Back, Continue with Google, Email + Password fields with a visibility eye, the Sign in submit, the Forgot password? submit (validating, not switching — its reset view is uncaptured) and the Sign up switcher that flips the card to its create-account view. The fields were typed into then cleared; nothing was submitted.

#### Sign-in card
The sign-in card over the dark field: "Sign in" heading, Continue with Google, Email + Password fields, Sign in submit, the Forgot password? and Sign up switchers. Read as `auth-card` on the app auth page.

**Values (default).** size 384 x 468.8; padding 24px 32px; border 1px solid #1a1a1a `core.appColor.base-700`; radius 28px; background #111111 `core.appColor.base-800`; text sfProFont 32/44.8 500, #ffffff `core.appColor.base-100`; icon 16 x 16, #ff6b02 `core.appColor.accent-500`.

![Sign-in card default](components/crops/auth-card-default.png)

#### Back button
The "Back" button over the auth card; measured, never pressed (it navigates to the start page). Read as `auth-back` on the app auth page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 70 x 32; padding 0px 12px 0px 8px; radius 3.35544e+07px; background oklab(0.999994 0.0000455678 0.0000200868 / 0.05); text sfProFont 14/20 500, #b0b4ba `core.appColor.base-500`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #b0b4ba `core.appColor.base-500` |
| hover, pressed | background oklab(0.999994 0.0000455678 0.0000200868 / 0.15) |

![Back button default](components/crops/auth-back-default.png) ![Back button hover](components/crops/auth-back-hover.png) ![Back button focus-visible](components/crops/auth-back-focus-visible.png) ![Back button pressed](components/crops/auth-back-pressed.png)

#### Google sign-in
The "Continue with Google" button; measured, never pressed — it would start the OAuth flow. Read as `auth-google` on the app auth page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 318 x 40; padding 0px 12px; radius 3.35544e+07px; background oklab(0.702262 0.141683 0.141613 / 0.2); text sfProFont 14/20 500, #ff6b02 `core.appColor.accent-500`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #ff6b02 `core.appColor.accent-500` |
| hover, pressed | background oklab(0.702262 0.141683 0.141613 / 0.35) |

![Google sign-in default](components/crops/auth-google-default.png) ![Google sign-in hover](components/crops/auth-google-hover.png) ![Google sign-in focus-visible](components/crops/auth-google-focus-visible.png) ![Google sign-in pressed](components/crops/auth-google-pressed.png)

#### Email field
The "Email address" field on the sign-in card; focused and typed into then cleared — never submitted. Read as `auth-field-email` on the app auth page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 286 x 48; background transparent; text sfProFont 14/20 400, #ffffff `core.appColor.base-100`; placeholder #686a6e `core.appColor.base-600` |

![Email field default](components/crops/auth-field-email-default.png) ![Email field focused](components/crops/auth-field-email-focused.png) ![Email field filled](components/crops/auth-field-email-filled.png)

#### Password field
The "Password" field on the sign-in card; focused and typed into then cleared — never submitted. Read as `auth-field-pass` on the app auth page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 262 x 48; background transparent; text sfProFont 14/20 400, #ffffff `core.appColor.base-100`; placeholder #686a6e `core.appColor.base-600` |

![Password field default](components/crops/auth-field-pass-default.png) ![Password field focused](components/crops/auth-field-pass-focused.png) ![Password field filled](components/crops/auth-field-pass-filled.png)

#### Password visibility eye
The eye button inside the password field — a local UI toggle; measured at rest, never needed to reveal anything. Read as `auth-eye` on the app auth page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 16 x 16; background transparent; text sfProFont 14/20 400, #686a6e `core.appColor.base-600`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #686a6e `core.appColor.base-600` |
| hover | text sfProFont 14/20 400, #ffffff `core.appColor.base-100`; icon 16 x 16, #ffffff `core.appColor.base-100` |

![Password visibility eye default](components/crops/auth-eye-default.png) ![Password visibility eye hover](components/crops/auth-eye-hover.png)

#### Sign-in submit
The card's "Sign in" submit; its states were measured but the button was never pressed — nothing was submitted. Read as `auth-submit` on the app auth page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 318 x 40; padding 0px 12px; radius 3.35544e+07px; background #ff6b02 `core.appColor.accent-500`; text sfProFont 14/20 400, #020108 `core.appColor.base-900`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | background #f94a00 `core.appColor.accent-600` |

![Sign-in submit default](components/crops/auth-submit-default.png) ![Sign-in submit hover](components/crops/auth-submit-hover.png) ![Sign-in submit focus-visible](components/crops/auth-submit-focus-visible.png) ![Sign-in submit pressed](components/crops/auth-submit-pressed.png)

#### Forgot password submit
The "Forgot password?" button on the sign-in card — a form action, not a view switch: pressing it validates the email field in place (the card shows "Please enter a valid email address" and stays on sign-in), and completing it submits. Measured at rest, never pressed. Read as `auth-forgot` on the app auth page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 98 x 17; border B: 1px solid #686a6e `core.appColor.base-600`; background transparent; text sfProFont 12/16 400, #686a6e `core.appColor.base-600`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1); layers button.cursor-pointer.transition-colors 98.0x17.0 B:1px solid rgb(104, 106, 110) |
| hover | border B: 1px solid #f94a00 `core.appColor.accent-600`; text sfProFont 12/16 400, #f94a00 `core.appColor.accent-600`; layers button.cursor-pointer.transition-colors 98.0x17.0 B:1px solid rgb(249, 74, 0) |

Child layers that carry the look: button 98x17 border 1px solid #686a6e `core.appColor.base-600`.

![Forgot password submit default](components/crops/auth-forgot-default.png) ![Forgot password submit hover](components/crops/auth-forgot-hover.png)

#### Sign-up switcher
The "Sign up" text button at the card's foot that switches it to the create-account view — a local UI switch; measured at rest. Read as `auth-switch` on the app auth page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 41 x 17; border B: 1px solid #ff6b02 `core.appColor.accent-500`; background transparent; text sfProFont 12/16 400, #ff6b02 `core.appColor.accent-500`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1); layers button.cursor-pointer.transition-colors 41.0x17.0 B:1px solid rgb(255, 107, 2) |
| hover | border B: 1px solid #f94a00 `core.appColor.accent-600`; text sfProFont 12/16 400, #f94a00 `core.appColor.accent-600`; layers button.cursor-pointer.transition-colors 41.0x17.0 B:1px solid rgb(249, 74, 0) |

Child layers that carry the look: button 41x17 border 1px solid #ff6b02 `core.appColor.accent-500`.

![Sign-up switcher default](components/crops/auth-switch-default.png) ![Sign-up switcher hover](components/crops/auth-switch-hover.png)

#### Forgot-password view (uncaptured)
The auth card's reset view. "Forgot password?" is a form action, not a local UI switch: pressing it validates the email field in place and the card stays on sign-in, while a valid email would submit — so the reset view is uncaptured. Read as `auth-forgot-card` on the app auth page.

Uncaptured: the forgot-password control validates and submits rather than switching views; the reset view needs a submission this kit never runs.


#### Create-account view
The auth card switched to its create-account view by pressing the "Sign up" switcher; fields were measured, the create submit was never pressed. Returned to the sign-in view afterwards. Read as `auth-signup-card` on the app auth page.

**Values (opened).** size 384 x 435.8; padding 24px 32px; border 1px solid #1a1a1a `core.appColor.base-700`; radius 28px; background #111111 `core.appColor.base-800`; text sfProFont 32/44.8 500, #ffffff `core.appColor.base-100`; icon 16 x 16, #ff6b02 `core.appColor.accent-500`.

![Create-account view opened](components/crops/auth-signup-card-opened.png)

### Create-PDP generator

app.fourmula.ai/project/create-pdp — the signed-out PDP generator: Cancel and close / Start generation in the header, the Dashboard link, the Your visuals rail with Recommendations and the upload buttons, the Connect-your-Shopify-store banner with the accent Check-connection pill, the Adjust-look section with its What's-a-PDP explainer and the Static/Video format radios, the Signed-in chips and the full-width Start generation submit — measured, never pressed or submitted.

#### Cancel button
The header's "Cancel and close" (aria "Cancel and close PDP creation"); measured, never pressed — it would leave the generator. Read as `pdp-cancel` on the app create-pdp page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 131 x 32; padding 0px 12px; radius 3.35544e+07px; background oklab(0.702262 0.141683 0.141613 / 0.2); text sfProFont 14/20 400, #ff6b02 `core.appColor.accent-500`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | background oklab(0.702262 0.141683 0.141613 / 0.35) |

![Cancel button default](components/crops/pdp-cancel-default.png) ![Cancel button hover](components/crops/pdp-cancel-hover.png) ![Cancel button focus-visible](components/crops/pdp-cancel-focus-visible.png) ![Cancel button pressed](components/crops/pdp-cancel-pressed.png)

#### Start generation (header)
The header's compact "Start generation" submit; measured, never pressed — it would queue a generation. Read as `pdp-start-header` on the app create-pdp page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 123 x 32; padding 0px 12px; radius 3.35544e+07px; background oklab(0.702262 0.141683 0.141613 / 0.15); text sfProFont 14/20 400, oklab(0.702262 0.141683 0.141613 / 0.15); transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Start generation (header) default](components/crops/pdp-start-header-default.png) ![Start generation (header) hover](components/crops/pdp-start-header-hover.png) ![Start generation (header) pressed](components/crops/pdp-start-header-pressed.png)

#### Dashboard link
The faded "Dashboard" nav link beside the menu button; measured, never followed (the dashboard needs an account). Read as `pdp-dash-link` on the app create-pdp page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 61 x 24; background transparent; text sfProFont 12/16 400, #ffffff `core.appColor.base-100`; transition opacity 0.2s cubic-bezier(0.4, 0, 0.2, 1); opacity 0.3 |
| pressed | opacity none |

![Dashboard link default](components/crops/pdp-dash-link-default.png) ![Dashboard link hover](components/crops/pdp-dash-link-hover.png) ![Dashboard link focus-visible](components/crops/pdp-dash-link-focus-visible.png) ![Dashboard link pressed](components/crops/pdp-dash-link-pressed.png)

#### Your visuals heading
The left rail's "Your visuals" section heading. Read as `pdp-visuals-h` on the app create-pdp page.

**Values (default).** size 432 x 70; padding 0px 24px; border B: 1px solid #020108 `core.appColor.base-900`; background transparent; text sfProFont 22/34.22 500, #ffffff `core.appColor.base-100`; layers h2.text-m.md:text-lg 432.0x70.0 B:1px solid rgb(2, 1, 8).

Child layers that carry the look: h2 432x70 border 1px solid #020108 `core.appColor.base-900`.

![Your visuals heading default](components/crops/pdp-visuals-h-default.png)

#### Recommendations button
The small "Recommendations" trigger under Your visuals — a local UI toggle that opens the recommendations dialog; the opened state was measured after clicking it, then the dialog was closed with Escape. Read as `pdp-reco` on the app create-pdp page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: opened) | size 134 x 20; background transparent; text sfProFont 14/20 400, #686a6e `core.appColor.base-600`; transition color 0.2s cubic-bezier(0, 0, 0.2, 1), background-color 0.2s cubic-bezier(0, 0, 0.2, 1), border-color 0.2s cubic-bezier(0, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0, 0, 0.2, 1), -webkit-text-decoration-color 0.2s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0, 0, 0.2, 1), fill 0.2s cubic-bezier(0, 0, 0.2, 1), stroke 0.2s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0, 0, 0.2, 1); icon 14 x 14, #686a6e `core.appColor.base-600` |
| hover | text sfProFont 14/20 400, #ffffff `core.appColor.base-100`; icon 14 x 14, #ffffff `core.appColor.base-100` |

![Recommendations button default](components/crops/pdp-reco-default.png) ![Recommendations button hover](components/crops/pdp-reco-hover.png) ![Recommendations button opened](components/crops/pdp-reco-opened.png)

#### Recommendations dialog
The "What can I upload?" dialog opened by the Recommendations trigger — a rounded-4xl bg-base-750 panel over a blurred backdrop; measured, never submitted. Read as `pdp-reco-dialog` on the app create-pdp page.

**Values (default).** size 480 x 655.86; padding 32px 48px; radius 28px; background #1e1e1e `core.appColor.base-750`; text sfProFont 32/44.8 400, #ffffff `core.appColor.base-100`; transition color 0.2s cubic-bezier(0, 0, 0.2, 1), background-color 0.2s cubic-bezier(0, 0, 0.2, 1), border-color 0.2s cubic-bezier(0, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0, 0, 0.2, 1), -webkit-text-decoration-color 0.2s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0, 0, 0.2, 1), fill 0.2s cubic-bezier(0, 0, 0.2, 1), stroke 0.2s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0, 0, 0.2, 1), opacity 0.2s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.2s cubic-bezier(0, 0, 0.2, 1), transform 0.2s cubic-bezier(0, 0, 0.2, 1), translate 0.2s cubic-bezier(0, 0, 0.2, 1), scale 0.2s cubic-bezier(0, 0, 0.2, 1), rotate 0.2s cubic-bezier(0, 0, 0.2, 1), filter 0.2s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.2s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.2s cubic-bezier(0, 0, 0.2, 1), display 0.2s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.2s cubic-bezier(0, 0, 0.2, 1), overlay 0.2s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.2s cubic-bezier(0, 0, 0.2, 1); icon 18 x 18, #ffffff `core.appColor.base-100`.

![Recommendations dialog default](components/crops/pdp-reco-dialog-default.png)

#### Upload button
The "Upload Main Image" button in the Your visuals rail; measured, never pressed (it would open the file picker). Read as `pdp-upload` on the app create-pdp page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 180 x 40; padding 0px 24px 0px 12px; radius 3.35544e+07px; background #ff6b02 `core.appColor.accent-500`; text sfProFont 14/20 400, #020108 `core.appColor.base-900`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #020108 `core.appColor.base-900` |
| hover, pressed | background #f94a00 `core.appColor.accent-600` |

![Upload button default](components/crops/pdp-upload-default.png) ![Upload button hover](components/crops/pdp-upload-hover.png) ![Upload button focus-visible](components/crops/pdp-upload-focus-visible.png) ![Upload button pressed](components/crops/pdp-upload-pressed.png)

#### Add product button
The "Add your product" button under the upload slot; measured, never pressed. Read as `pdp-add-product` on the app create-pdp page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 165 x 40; padding 0px 24px 0px 12px; radius 3.35544e+07px; background oklab(0.702262 0.141683 0.141613 / 0.2); text sfProFont 14/20 400, #ff6b02 `core.appColor.accent-500`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #ff6b02 `core.appColor.accent-500` |
| pressed | background oklab(0.702262 0.141683 0.141613 / 0.35) |

![Add product button default](components/crops/pdp-add-product-default.png) ![Add product button hover](components/crops/pdp-add-product-hover.png) ![Add product button focus-visible](components/crops/pdp-add-product-focus-visible.png) ![Add product button pressed](components/crops/pdp-add-product-pressed.png)

#### Shopify banner heading
The "Connect your Shopify store" banner heading. Read as `pdp-shopify-h` on the app create-pdp page.

**Values (default).** size 591 x 22.84; padding 0px 112px 0px 0px; background transparent; text sfProFont 16/22.85 500, #ffffff `core.appColor.base-100`.

![Shopify banner heading default](components/crops/pdp-shopify-h-default.png)

#### Check connection pill
The accent "Check connection" pill linking to /shopify-integration — the only painted accent surface on the signed-out page; measured, never followed. Read as `pdp-shopify-cta` on the app create-pdp page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 152 x 40; padding 0px 20px; radius 3.35544e+07px; background oklab(0.702262 0.141683 0.141613 / 0.2); text sfProFont 14/20 400, #ff6b02 `core.appColor.accent-500`; transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) |
| hover, pressed | background oklab(0.702262 0.141683 0.141613 / 0.35) |

![Check connection pill default](components/crops/pdp-shopify-cta-default.png) ![Check connection pill hover](components/crops/pdp-shopify-cta-hover.png) ![Check connection pill focus-visible](components/crops/pdp-shopify-cta-focus-visible.png) ![Check connection pill pressed](components/crops/pdp-shopify-cta-pressed.png)

#### Adjust-look heading
The "Adjust look" section heading that carries the "What's a PDP" trigger. Read as `pdp-adjust-h` on the app create-pdp page.

**Values (default).** size 639 x 70; padding 0px 24px; border B: 1px solid #020108 `core.appColor.base-900`; background transparent; text sfProFont 22/34.22 500, #ffffff `core.appColor.base-100`; icon 16 x 16, #ffffff `core.appColor.base-100`; layers h2.text-m.md:text-lg 639.0x70.0 B:1px solid rgb(2, 1, 8); button.cursor-pointer.transition-colors 132.0x32.0 rgb(26, 26, 26) 3.35544e+07px.

Child layers that carry the look: h2 639x70 border 1px solid #020108 `core.appColor.base-900`; button 132x32 background #1a1a1a `core.appColor.base-700` radius 3.35544e+07px.

![Adjust-look heading default](components/crops/pdp-adjust-h-default.png)

#### What's-a-PDP button
The pill-shaped "What's a PDP" explainer trigger — a local UI toggle that opens the PDP explainer dialog; the opened state was measured after clicking it, then the dialog was closed with Escape. Read as `pdp-what` on the app create-pdp page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: opened) | size 132 x 32; padding 0px 12px; radius 3.35544e+07px; background #1a1a1a `core.appColor.base-700`; text sfProFont 14/20 500, oklab(0.999994 0.0000455678 0.0000200868 / 0.65); transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #ffffff `core.appColor.base-100` |
| hover | background oklab(0.999994 0.0000455678 0.0000200868 / 0.15) |

![What's-a-PDP button default](components/crops/pdp-what-default.png) ![What's-a-PDP button hover](components/crops/pdp-what-hover.png) ![What's-a-PDP button opened](components/crops/pdp-what-opened.png)

#### PDP explainer dialog
The dialog opened by the "What's a PDP" trigger; measured, never submitted. Read as `pdp-what-dialog` on the app create-pdp page.

**Values (default).** size 880 x 448.38; padding 24px; radius 28px; background #1e1e1e `core.appColor.base-750`; text sfProFont 14/14 500, #ff6b02 `core.appColor.accent-500`; transition color 0.2s cubic-bezier(0, 0, 0.2, 1), background-color 0.2s cubic-bezier(0, 0, 0.2, 1), border-color 0.2s cubic-bezier(0, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0, 0, 0.2, 1), -webkit-text-decoration-color 0.2s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0, 0, 0.2, 1), fill 0.2s cubic-bezier(0, 0, 0.2, 1), stroke 0.2s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0, 0, 0.2, 1), opacity 0.2s cubic-bezier(0, 0, 0.2, 1), box-shadow 0.2s cubic-bezier(0, 0, 0.2, 1), transform 0.2s cubic-bezier(0, 0, 0.2, 1), translate 0.2s cubic-bezier(0, 0, 0.2, 1), scale 0.2s cubic-bezier(0, 0, 0.2, 1), rotate 0.2s cubic-bezier(0, 0, 0.2, 1), filter 0.2s cubic-bezier(0, 0, 0.2, 1), -webkit-backdrop-filter 0.2s cubic-bezier(0, 0, 0.2, 1), backdrop-filter 0.2s cubic-bezier(0, 0, 0.2, 1), display 0.2s cubic-bezier(0, 0, 0.2, 1), content-visibility 0.2s cubic-bezier(0, 0, 0.2, 1), overlay 0.2s cubic-bezier(0, 0, 0.2, 1), pointer-events 0.2s cubic-bezier(0, 0, 0.2, 1); icon 18 x 18, #ffffff `core.appColor.base-100`.

![PDP explainer dialog default](components/crops/pdp-what-dialog-default.png)

#### Requirement chip
A small "Signed in" status chip in the requirements area; measured, never pressed. Read as `pdp-signedin-chip` on the app create-pdp page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 62 x 25; border B: 1px solid oklab(0.654752 0.176441 0.131884 / 0.65); background transparent; text sfProFont 16/24 400, oklab(0.654752 0.176441 0.131884 / 0.65); transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1); layers button.cursor-pointer.transition-colors 62.0x25.0 B:1px solid oklab(0.654752 0.176441 0.131884 / 0.65) |
| hover | border B: 1px solid #f94a00 `core.appColor.accent-600`; text sfProFont 16/24 400, #f94a00 `core.appColor.accent-600`; layers button.cursor-pointer.transition-colors 62.0x25.0 B:1px solid rgb(249, 74, 0) |

Child layers that carry the look: button 62x25 border 1px solid oklab(0.654752 0.176441 0.131884 / 0.65).

![Requirement chip default](components/crops/pdp-signedin-chip-default.png) ![Requirement chip hover](components/crops/pdp-signedin-chip-hover.png)

#### Start generation (footer)
The full-width "Start generation" submit at the foot of the form; measured, never pressed — it would queue a generation. Read as `pdp-start-bottom` on the app create-pdp page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 591 x 40; padding 0px 12px; radius 12px; background oklab(0.702262 0.141683 0.141613 / 0.15); text sfProFont 14/20 400, oklab(0.702262 0.141683 0.141613 / 0.15); transition color 0.2s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), fill 0.2s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.2s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.2s cubic-bezier(0.4, 0, 0.2, 1) |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Start generation (footer) default](components/crops/pdp-start-bottom-default.png) ![Start generation (footer) hover](components/crops/pdp-start-bottom-hover.png) ![Start generation (footer) pressed](components/crops/pdp-start-bottom-pressed.png)

#### Format radiogroup
The "Static content / Video content" radio pair under Adjust look — a local UI toggle; Video paints disabled signed out. Read as `pdp-format-group` on the app create-pdp page.

**Values (default).** size 564 x 60; background transparent; text sfProFont 14/17.5 400, #ff6b02 `core.appColor.accent-500`; icon 16 x 16, #ff6b02 `core.appColor.accent-500`; layers span.group.relative 280.0x60.0 rgb(26, 26, 26) T:2px solid rgb(26, 26, 26) / R:2px solid rgb(26, 26, 26) / B:2px solid rgb(26, 26, 26) / L:2px solid rgb(26, 26, 26) 16px; div.flex.w-full 260.0x56.0 T:2px solid rgba(0, 0, 0, 0) / R:2px solid rgba(0, 0, 0, 0) / B:2px solid rgba(0, 0, 0, 0) / L:2px solid rgba(0, 0, 0, 0); div.h-full.aspect-square 52.0x52.0 oklab(0.0834194 0.00993755 -0.0279362 / 0.3).

Child layers that carry the look: span 280x60 background #1a1a1a `core.appColor.base-700` border 2px solid #1a1a1a `core.appColor.base-700` radius 16px; div 260x56 border 2px solid transparent; div 52x52 background oklab(0.0834194 0.00993755 -0.0279362 / 0.3) radius 12px.

![Format radiogroup default](components/crops/pdp-format-group-default.png)

#### Format radio (Static)
The "Static content" radio — the checked default; measured, never changed. Read as `pdp-format-static` on the app create-pdp page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 280 x 60; padding 0px 16px 0px 0px; border 2px solid #1a1a1a `core.appColor.base-700`; radius 16px; background #1a1a1a `core.appColor.base-700`; text sfProFont 14/17.5 400, #ff6b02 `core.appColor.accent-500`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #ff6b02 `core.appColor.accent-500` |

![Format radio (Static) default](components/crops/pdp-format-static-default.png) ![Format radio (Static) hover](components/crops/pdp-format-static-hover.png)

#### Format radio (Video, disabled)
The "Video content" radio — painted disabled (data-disabled, 0.5 opacity) for signed-out visitors; measured, never pressed. Read as `pdp-format-video` on the app create-pdp page.

**Values (default).** size 280 x 60; padding 0px 16px 0px 0px; border 2px solid #1a1a1a `core.appColor.base-700`; radius 16px; background #1a1a1a `core.appColor.base-700`; text sfProFont 14/17.5 400, #b0b4ba `core.appColor.base-500`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), translate 0.15s cubic-bezier(0.4, 0, 0.2, 1), scale 0.15s cubic-bezier(0.4, 0, 0.2, 1), rotate 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), display 0.15s cubic-bezier(0.4, 0, 0.2, 1), content-visibility 0.15s cubic-bezier(0.4, 0, 0.2, 1), overlay 0.15s cubic-bezier(0.4, 0, 0.2, 1), pointer-events 0.15s cubic-bezier(0.4, 0, 0.2, 1); opacity 0.5; icon 16 x 16, #b0b4ba `core.appColor.base-500`.

![Format radio (Video, disabled) default](components/crops/pdp-format-video-default.png)

### Mobile (390 wide)

The marketing site at 390 wide: the header, the Menu pill and its nav overlay, the hero and the FAQ rows.

#### Mobile header
The phone header at 390 wide: logo, the Menu pill with the theme toggle and the Get started pill. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 104.11; padding 19.3484px 16.1237px; background transparent; text Sf Pro Display 17.13/20.55 400, #ffffff `light.background.page`; transition all 0.2s ease; icon 58.84 x 56.42, #020108 `light.background.menu`; layers div.header__main 249.8x48.4 rgb(2, 1, 8) 1596.25px; div.header__menu-line.is-top 26.6x1.0 rgb(255, 255, 255); div.header__menu-line.is-bottom 26.6x1.0 rgb(255, 255, 255); div.header__theme 32.2x32.2 T:1px solid rgba(255, 255, 255, 0.2) / R:1px solid rgba(255, 255, 255, 0.2) / B:1px solid rgba(255, 255, 255, 0.2) / L:1px solid rgba(255, 255, 255, 0.2) 1596.25px; div.header__prc 58.0x32.2 rgba(255, .

Child layers that carry the look: div 249.8x48.4 background #020108 `light.background.menu` radius 1596.25px; div 26.6x1 background #ffffff `light.background.page`; div 26.6x1 background #ffffff `light.background.page`.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile menu pill
The "Menu" pill at 390 wide — a local UI toggle that opens the nav overlay; the opened state was measured after clicking it, then closed. Read as `m-menu-pill` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 95.08 x 42.69; padding 8.06185px 0px 8.06185px 8.06185px; background transparent; text Sf Pro Display 17.13/20.55 400, #ffffff `light.background.page`; transition opacity 0.2s ease; layers div.header__menu-line.is-top 26.6x1.0 rgb(255, 255, 255); div.header__menu-line.is-bottom 26.6x1.0 rgb(255, 255, 255) |
| hover, pressed | opacity 0.64 |
| opened | opacity 0.64; layers div.header__menu-line.is-top 19.5x19.5 rgb(255, 255, 255); div.header__menu-line.is-bottom 19.5x19.5 rgb(255, 255, 255) |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: div 26.6x1 background #ffffff `light.background.page`; div 26.6x1 background #ffffff `light.background.page`.

![Mobile menu pill default](components/crops/m-menu-pill-default.png) ![Mobile menu pill hover](components/crops/m-menu-pill-hover.png) ![Mobile menu pill pressed](components/crops/m-menu-pill-pressed.png) ![Mobile menu pill opened](components/crops/m-menu-pill-opened.png)

#### Mobile nav overlay
The nav overlay opened by the menu pill at 390 wide; its links were never followed. Read as `m-nav-overlay` on the home page at 390 wide.

**Values (opened).** size 390 x 499.7; padding 12.0928px 10.4804px 0px 0px; background transparent; text Sf Pro Display 12.09/18.13 400, rgba(2, 1, 8, 0.5) `light.text.dim`; transition all 0.2s ease; icon 24.17 x 24.17, #020108 `light.background.menu`; layers div.menu__wrap 258.5x487.6 rgb(217, 217, 217) 32.2474px; div.menu__item.is-lined 234.0x117.3 T:1px solid rgba(2, 1, 8, 0.2); a.btn-primary.u-btn 181.6x48.4 rgb(2, 1, 8) 1596.25px; a.header_signin.w-inline-block 48.4x48.4 rgb(217, 217, 217) T:1px solid rgba(2, 1, 8, 0.2) / R:1px solid rgba(2, 1, 8, 0.2) / B:1px solid rgba(2, 1, 8, 0.2) / L:1px solid rgba(2, 1, 8, 0.2) 32.2474px.

Child layers that carry the look: div 258.5x487.6 background #d9d9d9 `light.background.dots` radius 32.2474px; div 234x117.3 border 1px solid rgba(2, 1, 8, 0.2) `light.text.hairlineInk`; a 181.6x48.4 background #020108 `light.background.menu` radius 1596.25px.

![Mobile nav overlay opened](components/crops/m-nav-overlay-opened.png)

#### Mobile hero headline
The masthead at 390 wide (u-h1 resolves to the mobile size). Read as `m-hero-h1` on the home page at 390 wide.

**Values (default).** size 286.22 x 75.78; background transparent; text Sf Pro Display 40.30/37.89 400, #020108 `light.background.menu`.

![Mobile hero headline default](components/crops/m-hero-h1-default.png)

#### Mobile step CTA
A "Get started" button in the steps section at 390 wide; measured, never followed. Read as `m-step-cta` on the home page at 390 wide.

**Values (default).** size 124.73 x 48.36; padding 14.1082px 24.1855px; radius 1596.25px; background #ffffff `light.background.page`; text Sf Pro Display 17.13/20.55 400, #020108 `light.background.menu`; transition all 0.2s ease.

![Mobile step CTA default](components/crops/m-step-cta-default.png)

#### Mobile FAQ row
A FAQ accordion row at 390 wide; the opened state was measured after clicking, then re-closed. Read as `m-faq-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 357.78 x 94.69; padding 20.1546px 0px 32.2474px 0px; border T: 1px solid #d7d7d6 `light.border.rule`; B: 1px solid #d7d7d6 `light.border.rule`; background transparent; text Sf Pro Display 16.12/20.15 500, #020108 `light.background.menu` |
| opened | size 357.78 x 125.53 |

![Mobile FAQ row default](components/crops/m-faq-item-default.png) ![Mobile FAQ row opened](components/crops/m-faq-item-opened.png)

### Footer

The 811px page footer: the fourmula.ai mark, the section anchors, the legal links and the social column.

#### Footer
The 811px page footer: the fourmula.ai mark, section anchors (PDP's / Videos / Products / Our features), legal links, Instagram. Read as `footer` on the home page.

**Values (default).** size 1440 x 811.78; padding 6.65421px; background transparent; text Sf Pro Display 13.30/19.96 500, #020108 `light.background.menu`; layers div.footer__wrap 1426.7x798.5 rgb(247, 247, 247) 39.9252px; div.dot 13.3x13.3 rgb(2, 1, 8) 50%; div.dot 13.3x13.3 rgb(2, 1, 8) 50%; div.dot 13.3x13.3 rgb(2, 1, 8) 50%; div.dot 13.3x13.3 rgb(2, 1, 8) 50%; div.dot 13.3x13.3 rgb(2, 1, 8) 50%.

Child layers that carry the look: div 1426.7x798.5 background #f7f7f7 `light.background.surface` radius 39.9252px; div 13.3x13.3 background #020108 `light.background.menu` radius 50%; div 13.3x13.3 background #020108 `light.background.menu` radius 50%.

![Footer default](components/crops/footer-default.png)

#### Footer link
The "Privacy Policy" footer link; measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 68.59 x 17.45; background transparent; text Sf Pro Display 11.64/17.46 500, #020108 `light.background.menu`; transition opacity 0.2s ease |
| hover, pressed | opacity 0.65 |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Footer (dark paint)
The page footer under the dark paint. Read as `footer-dark` on the home (dark paint) page.

**Values (default).** size 1440 x 811.78; padding 6.65421px; background transparent; text Sf Pro Display 13.30/19.96 500, #ffffff `dark.text.ink`; layers div.footer__wrap 1426.7x798.5 rgb(17, 17, 17) 39.9252px; div.dot 13.3x13.3 rgb(255, 255, 255) 50%; div.dot 13.3x13.3 rgb(255, 255, 255) 50%; div.dot 13.3x13.3 rgb(255, 255, 255) 50%; div.dot 13.3x13.3 rgb(255, 255, 255) 50%; div.dot 13.3x13.3 rgb(255, 255, 255) 50%.

Child layers that carry the look: div 1426.7x798.5 background #111111 `dark.background.surface` radius 39.9252px; div 13.3x13.3 background #ffffff `dark.text.ink` radius 50%; div 13.3x13.3 background #ffffff `dark.text.ink` radius 50%.

![Footer (dark paint) default](components/crops/footer-dark-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the fourmula.ai square mark, the header theme sun/moon, the account glyph, the + FAQ icons and the app's menu/eye glyphs) are the product's artwork — the fourmula.ai logo is an inline Webflow embed, not an icon font. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Fourmula's product is the app at app.fourmula.ai: the dashboard, project pages, generation results and every post-login surface need an account and were never reached. The signed-out edge — /start, /auth and the /project/create-pdp generator — was measured as far as a visitor can go without an account: fields were typed into then cleared, and Sign in, Continue with Google, Create asset, Upload Main Image, Check connection, Start generation and every other submit was never pressed. The generator's Start generation would queue a job; what it returns is unverified.

### Pages

- **The account.** The dashboard and every post-login surface were never reached; /auth was measured at rest — what a submitted sign-in or sign-up returns is unverified.
- **The PDP generator** is reachable signed out and its form was measured, but the upload, the Check-connection flow and generation itself need an account and a Shopify store and were never run.
- **Legal pages** — /privacy-policy was measured; /terms-of-service was screenshotted on the same .tech template, unmeasured.
- **No pricing page** was found in the nav, footer or menu links at capture time; the product's cost is unobserved on the public surface.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error, loading and validation states** were not seen on the public surface beyond the disabled Video-content radio — the sign-in fields were never submitted.
- **The theme toggle was never pressed during measurement** (a press repaints the whole page); both painted themes were instead reached through the site's own isDarkMode storage key — the same key the toggle writes — so the toggled paint is the site's own, not a reconstruction.

### Themes

The marketing site ships a real two-theme switcher with inverted naming: `data-theme-toggle` writes localStorage isDarkMode and flips the `dark` class on `<body>`, but `.body.dark` paints the LIGHT surface (white `--mainbg`) and plain `.body` paints the DARK one (`#020108` `--mainbg`). A first visit stores isDarkMode=true, so visitors open on the light paint; the `light` token set is that default surface and `dark` is the toggled one. app.fourmula.ai is a separate dark-only Tailwind v4 app with its own `--color-base-*`/`--color-accent-*` layer that shares nothing but the `#020108` near-black with the marketing tokens; its declared values sit under `core.appColor`, `core.font.size.app`, `core.radius.app`, `core.spacing.app` and the other app ramps, and the measured ones under `core.component.app.*` — there is no `component.login` group.

### Fonts

- **Sf Pro Display** is the marketing site's face (`--_font-family---font-family: "Sf Pro Display", Arial, sans-serif`), and the app loads its own **SF Pro** variable face (sfProFont, a Next.js local-font variable). The files are Apple's proprietary fonts the site serves itself; the style guide falls back to system fonts.

### Screenshots

- The product photos, model imagery and logo artwork in the captures are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- The legal prose, FAQ answers and marketing copy are the product's content; only frames and components were measured.
