# Fibery components

The discovery list of every page and view captured, then one entry per component with crops of the real product, the icon index and the Gaps. Captured from fibery.com and fibery.io on 2026-11-14, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; the sign-up and login forms were never sent, the OAuth POST forms never pressed; every link and CTA was measured, never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (45 components, 109 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Suisse Intl 15/22 500, #251d1a`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (103 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png` — Fibery's public surfaces paint one light theme, with no toggle and no dark scope. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu-platform](screenshots/home-light-menu-platform.png), [menu-solutions](screenshots/home-light-menu-solutions.png) |
| Features | `/features` | [default](screenshots/features-light-default.png), [full](screenshots/features-light-full.png) |
| Templates | `/templates` | [default](screenshots/templates-light-default.png), [full](screenshots/templates-light-full.png) |
| Template detail | `/templates/content-marketing` | [default](screenshots/template-detail-light-default.png), [full](screenshots/template-detail-light-full.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Customer stories | `/customer-stories` | [default](screenshots/customer-stories-light-default.png), [full](screenshots/customer-stories-light-full.png) |
| Blog | `/blog/` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Blog article | `/blog/product-updates/fibery-ai/` | [default](screenshots/blog-article-light-default.png), [full](screenshots/blog-article-light-full.png) |
| 101 Questions | `/101-questions-about-fibery` | [default](screenshots/questions-light-default.png), [full](screenshots/questions-light-full.png) |
| AI | `/ai` | [default](screenshots/ai-light-default.png), [full](screenshots/ai-light-full.png) |
| No-code | `/no-code` | [default](screenshots/no-code-light-default.png), [full](screenshots/no-code-light-full.png) |
| Product management | `/product-management` | [default](screenshots/product-management-light-default.png), [full](screenshots/product-management-light-full.png) |
| About us | `/about-us` | [default](screenshots/about-us-light-default.png), [full](screenshots/about-us-light-full.png) |
| Museum | `/museum` | [default](screenshots/museum-light-default.png), [full](screenshots/museum-light-full.png) |
| Download | `/download` | [default](screenshots/download-light-default.png), [full](screenshots/download-light-full.png) |
| Getting started | `/getting-started` | [default](screenshots/getting-started-light-default.png), [full](screenshots/getting-started-light-full.png) |
| Sign-up wizard | `fibery.io/sign-up` | [default](screenshots/sign-up-light-default.png), [full](screenshots/sign-up-light-full.png) |
| Login | `fibery.io/login/` | [default](screenshots/login-light-default.png), [full](screenshots/login-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [drawer](screenshots/mobile-home-light-drawer.png), [full](screenshots/mobile-home-light-full.png) |
| Features, phone | `/features` | [default](screenshots/mobile-features-light-default.png), [full](screenshots/mobile-features-light-full.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Sign-up, phone | `fibery.io/sign-up` | [default](screenshots/mobile-sign-up-light-default.png), [full](screenshots/mobile-sign-up-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Consent layer | every page | the kit hides any consent layer and the Intercom widget; neither is answered | hidden before every shot and reading |
| Solutions dropdown | every page header | hovered the 'Solutions' trigger (pointer hover opens the panel) | [home-light-menu-solutions](screenshots/home-light-menu-solutions.png), [nav-panel](#dropdown-panel), [nav-menu-item](#dropdown-item) |
| Platform dropdown | every page header | the same hover on 'Platform' | [home-light-menu-platform](screenshots/home-light-menu-platform.png) |
| Mobile nav drawer | home page, phone width | the sandwich button's own toggle | [mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png), [m-drawer](#mobile-nav) |
| Billing switch | /pricing | the Monthly/Yearly checkbox toggled — a local UI toggle; prices flip, nothing is sent | [price-switch](#billing-switch) |
| FAQ accordion | /pricing | a question row toggled open | [faq-item](#faq-item) |
| AI prompt field | fibery.io/sign-up | typed into then cleared — 'Create workspace' never pressed | [su-field](#prompt-field), [su-submit](#create-workspace-button) |
| E-mail sign-in step | fibery.io/login/ | 'Continue with Email' pressed — a local step change; the field typed into then cleared, never submitted | [login-email-field](#email-field-login) |
| Signed-in product | a Fibery workspace | every post-login surface (the app itself, workspaces, docs) needs an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 14 components were given a real keyboard focus. 13 draw an outline ring: `nav-item` (1px auto #101010, offset 1px), `nav-login` (1px auto #101010, offset 1px), `nav-signup` (1px auto #101010, offset 1px), `hero-cta` (1px auto #101010, offset 1px), `hero-cta2` (1px auto #101010, offset 0px), `footer-link` (1px auto #101010, offset 1px), `plan-cta` (1px auto #101010, offset 1px), `su-skip` (1px auto #101010, offset 0px), `login-google` (1px auto #101010, offset 0px), `login-ms` (1px auto #101010, offset 0px), `login-email` (1px auto #101010, offset 0px), `login-sso` (1px auto #101010, offset 0px), `m-hero-cta` (1px auto #e59700, offset 1px). The other 1 show no measured change: `su-premade`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.2s | `cubic-bezier(0.12, 0, 0.39, 0)` | box-shadow | tpl-card |
| 0.3s | `ease` | all, border-color, color | hero-cta, hero-cta2, login-email, login-sso, m-hero-cta, nav-item, nav-login, nav-signup and more |
| 0.3s | `ease-in-out` | all | login-email-field, su-field |
| 0.3s | `linear` | background-color | nav-menu-item |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Dropdown panel](#dropdown-panel) | 740 x 383 | - | 12px | #fff5e8 | rgba(20, 21, 26, 0.08) 0px 10px 16px -3px, rgba(20, 21, 26, 0.05) 0px 1px 2px 0px | 28px 24px 24px 24px |
| [Plan card](#plan-card) | 282 x 559.27 | 1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) | 12px | #fdf7ef `color.named.cream` | none | 40px 32px |
| [Paid plan card](#paid-plan-card) | 282 x 559.27 | 1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) | 12px | #fdf7ef `color.named.cream` | none | 40px 32px |
| [Template card](#template-card) | 270.66 x 435.58 | 1px solid #f0b89b `color.named.rustyPeach` | 16px | #fdf7ef `color.named.cream` | none | 30px 30px 0px 30px |
| [FAQ item](#faq-item) | 1200 x 73 | B: 1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) | - | transparent | none | 0 |
| [Sign-up panel](#sign-up-panel) | 560 x 448.58 | - | - | transparent | none | 0 |
| [Login panel](#login-panel) | 360 x 276.8 | - | - | transparent | none | 0 |
| [Hint card](#hint-card) | 560.8 x 850 | - | 20px | #d5d8ca `color.tertiary.green` | rgba(0, 0, 0, 0.05) 0px 0px 0px 1px inset | 40px |

## Components

### Site chrome

The header on every marketing page: the Fibery mark, the Solutions/Platform/Support dropdown triggers, Pricing, Log in and the dark 'Sign up for free' pill; the dropdown panel is the menu-bg cream surface.

#### Site header
The top bar: Fibery wordmark, Solutions/Platform/Support dropdowns, Pricing, Book a demo, Log in and the dark "Sign up for free" button. Read as `mkt-header` on the home page.

**Values (default).** size 1440 x 88; padding 12px; background transparent; text Suisse Intl 16/34 500, #251d1a `color.basic.black`; layers nav::before.HeaderMainMenu_menuList__q0OJp 619pxx60px rgb(255, 245, 232) 10px; div.HeaderMainMenu_headerDivider__6tgCG 1.0x18.0 rgba(0, 0, 0, 0.25); div.HeaderMenuItem_root__Lva5Q.HeaderMenuItem_mobileHidden__ssM4C 113.0x36.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 6px; span::after.HeaderMenuItem_menuLink__JgNSg 5pxx.

Child layers that carry the look: nav::before 619pxx60px background #fff5e8 radius 10px; div 1x18 background rgba(0, 0, 0, 0.25); div 113x36 border 1px solid transparent radius 6px.

![Site header default](components/crops/mkt-header-default.png)

#### Logo
The Fibery mark-and-wordmark in the header, linking home. Read as `mkt-logo` on the home page.

**Values (default).** size 127 x 36; background transparent; text Suisse Intl 16/0 400, #0000ee.

![Logo default](components/crops/mkt-logo-default.png)

#### Nav link
The Pricing header link; measured, never followed. Read as `nav-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 77 x 34; padding 0px 12px; background transparent; text Suisse Intl 16/34 500, #251d1a `color.basic.black`; transition color 0.3s ease |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.HeaderMenuItem_menuLink__JgNSg 77.0x34.0 1px auto rgb(16, 16, 16) offset 1px |

![Nav link default](components/crops/nav-item-default.png) ![Nav link hover](components/crops/nav-item-hover.png) ![Nav link focus-visible](components/crops/nav-item-focus-visible.png) ![Nav link pressed](components/crops/nav-item-pressed.png)

#### Dropdown trigger
The "Solutions" header item — opens the solutions dropdown panel on hover. The opened state was measured after hovering it. Read as `nav-menu-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 113 x 36; border 1px solid transparent; radius 6px; background transparent; text Suisse Intl 16/34 500, #251d1a `color.basic.black`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover, pressed, opened | border 1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1); background #fdf7ef `color.named.cream`; icon 32 x 32, #0000ee |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Dropdown trigger default](components/crops/nav-menu-btn-default.png) ![Dropdown trigger hover](components/crops/nav-menu-btn-hover.png) ![Dropdown trigger pressed](components/crops/nav-menu-btn-pressed.png) ![Dropdown trigger opened](components/crops/nav-menu-btn-opened.png)

#### Dropdown panel
The solutions dropdown panel opened by hovering its trigger (menu tiles plus template links); its links were never followed. Read as `nav-panel` on the home page.

**Values (default).** size 740 x 383; padding 28px 24px 24px 24px; radius 12px; background #fff5e8; shadow rgba(20, 21, 26, 0.08) 0px 10px 16px -3px, rgba(20, 21, 26, 0.05) 0px 1px 2px 0px; text Suisse Intl 14/14 500, #5f5f5f; icon 32 x 32, #0000ee.

![Dropdown panel default](components/crops/nav-panel-default.png)

#### Dropdown item
A tile inside the open dropdown panel; measured, never followed. Read as `nav-menu-item` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 326 x 64; padding 4px 24px 4px 4px; radius 10px; background transparent; text Suisse Intl 16/16 500, #251d1a `color.basic.black`; transition background-color 0.3s linear; icon 32 x 32, #0000ee; layers div.MenuItemTile_iconWrap__6DuKw 56.0x56.0 T:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) / R:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) / B:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) / L:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) 8px |
| hover | background #faebd6 `color.named.soup`; layers none |

Child layers that carry the look: div 56x56 border 1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) radius 8px.

![Dropdown item default](components/crops/nav-menu-item-default.png) ![Dropdown item hover](components/crops/nav-menu-item-hover.png)

#### Log in link
The "Log in" header link to fibery.io/login; measured, never followed. Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 79 x 40; padding 0px 16px; radius 6px; background #fdf7ef `color.named.cream`; text Suisse Intl 16/40 600, #251d1a `color.basic.black`; transition all 0.3s ease |
| hover | shadow oklab(0.239148 0.0103381 0.00917888 / 0.1) 0px 0px 0px 1px |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | shadow oklab(0.239148 0.0103381 0.00917888 / 0.0969406) 0px 0px 0px 0.969406px |

![Log in link default](components/crops/nav-login-default.png) ![Log in link hover](components/crops/nav-login-hover.png) ![Log in link focus-visible](components/crops/nav-login-focus-visible.png) ![Log in link pressed](components/crops/nav-login-pressed.png)

#### Sign up button
The dark "Sign up for free" header button — the FiberyButton solid variant; links to /sign-up, measured never followed. Read as `nav-signup` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 153 x 40; padding 0px 16px; radius 6px; background #251d1a `color.basic.black`; text Suisse Intl 16/40 600, #faebd6 `color.named.soup`; transition all 0.3s ease |
| hover | shadow #251d1a 0px 0px 0px 1px |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | shadow #251d1a 0px 0px 0px 1px |

![Sign up button default](components/crops/nav-signup-default.png) ![Sign up button hover](components/crops/nav-signup-hover.png) ![Sign up button focus-visible](components/crops/nav-signup-focus-visible.png) ![Sign up button pressed](components/crops/nav-signup-pressed.png)

### Home

The hero on fibery.com: the Fraunces display headline 'Operating system for orgs run by nerds', the announcement pill, the paired Sign up / Book a Demo pills and the looping product video frame.

#### Announcement pill
The announcement pill at the top of the hero ("Are we turning Fibery into yet another AI app builder?") — a link to the blog post; measured, never followed. Read as `announce-bar` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 874.38 x 32; padding 5px 20px; radius 16px; background #f6d3a0 `color.named.tea`; text Suisse Intl 16/19.2 600, #251d1a `color.basic.black`; icon 20 x 20, #0000ee |

![Announcement pill default](components/crops/announce-bar-default.png) ![Announcement pill hover](components/crops/announce-bar-hover.png)

#### Hero headline
"Operating system for orgs run by nerds" — the display headline. Read as `hero-h1` on the home page.

**Values (default).** size 440.23 x 256; background transparent; text Suisse Intl 64/64 800, #251d1a `color.basic.black`.

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero lede
The muted supporting paragraph under the hero headline. Read as `hero-lede` on the home page.

**Values (default).** size 352.19 x 70.17; background transparent; text Suisse Intl 18/23.4 400, #251d1a `color.basic.black`.

![Hero lede default](components/crops/hero-lede-default.png)

#### Hero CTA
The dark "Sign up" hero button (FiberyButton solid); measured never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 150 x 40; padding 0px 24px; radius 6px; background #251d1a `color.basic.black`; text Suisse Intl 16/40 600, #faebd6 `color.named.soup`; transition all 0.3s ease |
| hover | shadow #251d1a 0px 0px 0px 1px |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | shadow #251d1a 0px 0px 0px 1px |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Hero secondary CTA
The outlined "Book a Demo" hero button (FiberyButton outline); measured never followed. Read as `hero-cta2` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 136 x 40; padding 0px 16px; radius 6px; background oklab(0.946375 0.00760221 0.0313067 / 0.1); shadow #251d1a 0px 0px 0px 1px inset; text Suisse Intl 16/40 600, #251d1a `color.basic.black`; transition all 0.3s ease |
| hover | shadow #251d1a 0px 0px 0px 1px inset, #251d1a 0px 0px 0px 0.5px |
| focus-visible | outline 1px auto #101010, offset 0px |

![Hero secondary CTA default](components/crops/hero-cta2-default.png) ![Hero secondary CTA hover](components/crops/hero-cta2-hover.png) ![Hero secondary CTA focus-visible](components/crops/hero-cta2-focus-visible.png) ![Hero secondary CTA pressed](components/crops/hero-cta2-pressed.png)

#### Product video frame
The hero product video (the looping app screencast in a framed panel beside the copy, with its pause control); a public product mock, not the signed-in app. Read as `product-frame` on the home page.

**Values (default).** size 854.58 x 480.69; radius 20px; background transparent; shadow rgba(20, 21, 26, 0.08) 0px 10px 16px -3px, rgba(20, 21, 26, 0.05) 0px 1px 2px 0px; text Suisse Intl 16/0 400, #251d1a `color.basic.black`; icon 24 x 24, #fffdfa `color.named.milk`; layers div.MainHero_screenSide__vs7Jo 854.6x480.7 rgba(20, 21, 26, 0.08) 0px 10px 16px -3px, rgba(20, 21, 26, 0.05) 0px 1px 2px 0px 20px; button.VideoItem_control__lNTZU 40.0x40.0 rgba(0, 0, 0, 0.55) 50%.

![Product video frame default](components/crops/product-frame-default.png)

#### Section heading
A marketing section heading further down the home page. Read as `section-h2` on the home page.

**Values (default).** size 592 x 96; background transparent; text Suisse Intl 48/48 800, #faebd6 `color.named.soup`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Pricing

The /pricing page: the Monthly/Yearly switch, the tinted plan cards (the Free plan on quaternary-yellow), the plan CTAs, the FAQ accordion and the plan-comparison table.

#### Pricing headline
"One platform for the whole company" — the /pricing masthead. Read as `price-h1` on the pricing page.

**Values (default).** size 1200 x 52.8; background transparent; text Suisse Intl 48/52.8 800, #251d1a `color.basic.black`.

![Pricing headline default](components/crops/price-h1-default.png)

#### Billing switch
The Monthly/Yearly billing switch (a checkbox + label control); the toggled state flips the displayed prices — a local UI toggle, nothing sent. Read as `price-switch` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 213 x 36; padding 2px; radius 8px; background #fdf7ef `color.named.cream`; text Suisse Intl 14/20 500, #251d1a `color.basic.black` |
| toggled | text Suisse Intl 14/20 500, #fffdfa `color.named.milk` |

![Billing switch default](components/crops/price-switch-default.png) ![Billing switch toggled](components/crops/price-switch-toggled.png)

#### Plan card
A pricing plan tile (the Free plan: name, icon, price, feature list, CTA). Read as `plan-card` on the pricing page.

**Values (default).** size 282 x 559.27; padding 40px 32px; border 1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1); radius 12px; background #fdf7ef `color.named.cream`; text Suisse Intl 24/26.4 800, #251d1a `color.basic.black`; transition all 0.3s ease; icon 18 x 18, #251d1a `color.basic.black`; layers ::before rgb(251, 240, 225) 0px none 0.

![Plan card default](components/crops/plan-card-default.png)

#### Paid plan card
A paid plan tile beside the Free plan. Read as `plan-card-paid` on the pricing page.

**Values (default).** size 282 x 559.27; padding 40px 32px; border 1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1); radius 12px; background #fdf7ef `color.named.cream`; text Suisse Intl 10/12 700, #fffdfa `color.named.milk`; transition all 0.3s ease; icon 14.14 x 14.14, #fffdfa `color.named.milk`; layers ::before rgb(246, 234, 227) 0px none 0.

![Paid plan card default](components/crops/plan-card-paid-default.png)

#### Plan CTA
The call-to-action inside a plan tile; measured never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 216 x 40; padding 0px 16px; radius 6px; background oklab(0.946375 0.00760221 0.0313067 / 0.1); shadow #251d1a 0px 0px 0px 1px inset; text Suisse Intl 16/40 600, #251d1a `color.basic.black`; transition all 0.3s ease |
| hover | shadow #251d1a 0px 0px 0px 1px inset, #251d1a 0px 0px 0px 0.5px |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | shadow #251d1a 0px 0px 0px 1px inset, #251d1a 0px 0px 0px 0.5px |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### FAQ item
A pricing FAQ row ("Is there a trial period?"); the opened state expands the answer — a local UI toggle. Read as `faq-item` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1200 x 73; border B: 1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1); background transparent; text Suisse Intl 20/32 400, #132331; layers div.QandAItem_root__Pe7di 1200.0x73.0 B:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1); div::after.QandAItem_questionHead__85Qr_ 9pxx9px R:2px solid rgb(36, 41, 56) / B:2px solid rgb(36, 41, 56) |
| opened | size 1200 x 215.38; text Suisse Intl 20/32 800, #132331; layers div.QandAItem_root__Pe7di 1200.0x215.4 B:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1); div::after.QandAItem_questionHead__85Qr_.QandAItem_open__MKU7f 9pxx9px R:2px solid rgb(36, 41, 56) / B:2px solid rgb(36, 41, 56) |

Child layers that carry the look: div 1200x73 border 1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1); div::after 9pxx9px border 2px solid #242938.

![FAQ item default](components/crops/faq-item-default.png) ![FAQ item opened](components/crops/faq-item-opened.png)

#### Feature table
The plan-comparison feature table under the cards. Read as `extend-table` on the pricing page.

**Values (default).** size 1270 x 6593.17; padding 20px 35px; radius 16px; background #fdf7ef `color.named.cream`; shadow rgba(20, 21, 26, 0.08) 0px 10px 16px -3px, rgba(20, 21, 26, 0.05) 0px 1px 2px 0px; text Suisse Intl 14/20 500, #fffdfa `color.named.milk`; icon 24 x 24, #251d1a `color.basic.black`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Templates

The /templates index: headline and the coloured template tiles.

#### Templates headline
The /templates index headline. Read as `tpl-h1` on the templates page.

**Values (default).** size 1144 x 52.8; background transparent; text Suisse Intl 48/52.8 800, #251d1a `color.basic.black`.

![Templates headline default](components/crops/tpl-h1-default.png)

#### Template card
A template tile on the index (the square icon, name and description, tinted by --template-color); measured, never followed. Read as `tpl-card` on the templates page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 270.66 x 435.58; padding 30px 30px 0px 30px; border 1px solid #f0b89b `color.named.rustyPeach`; radius 16px; background #fdf7ef `color.named.cream`; text Suisse Intl 24/28.8 800, #251d1a `color.basic.black`; transition box-shadow 0.2s cubic-bezier(0.12, 0, 0.39, 0) |
| hover | shadow rgba(193, 123, 88, 0.25) 4px 4px 20px 0px |

![Template card default](components/crops/tpl-card-default.png) ![Template card hover](components/crops/tpl-card-hover.png)

#### Template icon
A coloured template glyph (the square icon tile, tinted by --template-color). Read as `tpl-icon` on the templates page.

**Values (default).** size 36 x 36; radius 35%; background #fdf7ef `color.named.cream`; text Suisse Intl 16/19.2 400, #251d1a `color.basic.black`; layers ::before rgb(156, 43, 175) 0px none 0.15.

![Template icon default](components/crops/tpl-icon-default.png)

### Sign-up wizard (fibery.io)

fibery.io/sign-up — the public workspace-creation wizard: the AI prompt field, premade-solution chips, the disabled-until-filled 'Create workspace' submit, 'Start without AI' and the step dots. Measured and typed into then cleared, never submitted.

#### Sign-up panel
The "Get a head start with AI" wizard step on fibery.io/sign-up: prompt field, premade solutions, the AI submit and "Start without AI". Read as `su-panel` on the sign-up wizard page.

**Values (default).** size 560 x 448.58; background transparent; text Suisse Intl 24/28.8 700, #251d1a `color.basic.black`; icon 20 x 20, rgba(0, 0, 0, 0.7); layers div.SpillTheTea_teaIconWrap__wOwL_ 32.0x32.0 rgb(246, 211, 160) 8px; div.SpillTheTea_teaContent__tNd8n 0.0x0.0 rgb(246, 211, 160) 8px 0px 8px 8px; textarea.AiPromptInput_textField__FYXHP 560.0x164.0 rgb(255, 255, 255) rgba(0, 0, 0, 0.1) 0px 0px 0px 1px, rgba(0, 0, 0, 0.05) 0px 2px 6px 0px 20px; div::before.AiPromptInput_controlsWrap__7AgKJ 540pxx52px rgb(255, 253, 250) 0px 0px 10px 10px; button.Fi.

Child layers that carry the look: div 32x32 background #f6d3a0 `color.named.tea` radius 8px; div 0x0 background #f6d3a0 `color.named.tea` radius 8px 0px 8px 8px; textarea 560x164 background #ffffff `color.form.white` radius 20px shadow rgba(0, 0, 0, 0.1) 0px 0px 0px 1px, rgba(0, 0, 0, 0.05) 0px 2px 6px 0px.

![Sign-up panel default](components/crops/su-panel-default.png)

#### Prompt field
The AI workspace prompt textarea; focused and typed into then cleared — never submitted. Read as `su-field` on the sign-up wizard page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 560 x 164; padding 16px 32px 50px 18px; radius 20px; background #ffffff `color.form.white`; shadow rgba(0, 0, 0, 0.1) 0px 0px 0px 1px, rgba(0, 0, 0, 0.05) 0px 2px 6px 0px; text Suisse Intl 16/24 400, #000000; transition all 0.3s ease-in-out; placeholder #251d1a `color.basic.black` |

![Prompt field default](components/crops/su-field-default.png) ![Prompt field focused](components/crops/su-field-focused.png) ![Prompt field filled](components/crops/su-field-filled.png)

#### Create workspace button
The AI wizard submit — disabled until the prompt holds text; the enabled state was measured after typing (the text was then cleared, never submitted). Read as `su-submit` on the sign-up wizard page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 162 x 32; padding 6px 12px; radius 16px; background #bd5f00; text Suisse Intl 14/20 500, #fffdfa `color.named.milk`; transition all 0.3s ease; opacity 0.5; icon 12 x 10, #fffdfa `color.named.milk` |
| enabled | opacity none |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Create workspace button default](components/crops/su-submit-default.png) ![Create workspace button hover](components/crops/su-submit-hover.png) ![Create workspace button pressed](components/crops/su-submit-pressed.png) ![Create workspace button enabled](components/crops/su-submit-enabled.png)

#### Premade solution
A premade-solution chip ("Product development"); measured, never pressed — it fills the prompt. Read as `su-premade` on the sign-up wizard page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 164 x 28; padding 0px 12px 0px 10px; radius 16px; background rgba(255, 255, 255, 0.5); shadow rgba(0, 0, 0, 0.05) 0px 0px 0px 1px; text Suisse Intl 12/28 400, rgba(0, 0, 0, 0.6); transition all 0.3s ease; icon 16 x 16, rgba(0, 0, 0, 0.6) |
| hover, pressed | background rgba(255, 255, 255, 0.9); shadow #f0d7c8 0px 0px 0px 1px |

![Premade solution default](components/crops/su-premade-default.png) ![Premade solution hover](components/crops/su-premade-hover.png) ![Premade solution focus-visible](components/crops/su-premade-focus-visible.png) ![Premade solution pressed](components/crops/su-premade-pressed.png)

#### Start without AI
The "Start without AI" skip action; measured, never followed — it advances the wizard. Read as `su-skip` on the sign-up wizard page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 163 x 34; padding 0px 8px 0px 12px; radius 6px; background #fffdfa `color.named.milk`; shadow #251d1a 0px 0px 0px 1px; text Suisse Intl 16/34 500, #251d1a `color.basic.black`; transition all 0.3s ease |
| hover | background #251d1a `color.basic.black`; text Suisse Intl 16/34 500, #fffdfa `color.named.milk` |
| focus-visible | outline 1px auto #101010, offset 0px |
| pressed | background #251d1a `color.basic.black`; text Suisse Intl 16/34 500, #fffdfa `color.named.milk` |

![Start without AI default](components/crops/su-skip-default.png) ![Start without AI hover](components/crops/su-skip-hover.png) ![Start without AI focus-visible](components/crops/su-skip-focus-visible.png) ![Start without AI pressed](components/crops/su-skip-pressed.png)

#### Step pagination
The wizard step dots at the bottom (step 1 of the workspace-creation flow). Read as `su-steps` on the sign-up wizard page.

**Values (default).** size 198 x 11; padding 0px 14px; background transparent; text Suisse Intl 16/19.2 400, #251d1a `color.basic.black`; layers button::before.SignupStepPagination_step__oPEqw.SignupStepPagination_active__EpG_s 50pxx3px rgb(193, 123, 88); button::before.SignupStepPagination_step__oPEqw.SignupStepPagination_disabled__KMDWj 50pxx3px rgb(222, 222, 222); button::before.SignupStepPagination_step__oPEqw.SignupStepPagination_disabled__KMDWj 50pxx3px rgb(222, 222, 222).

Child layers that carry the look: button::before 50pxx3px background #c17b58 `color.named.rusty`; button::before 50pxx3px background #dedede; button::before 50pxx3px background #dedede.

![Step pagination default](components/crops/su-steps-default.png)

### Login (fibery.io)

fibery.io/login/ — the public sign-in: the 'Login to Fibery' form column, the Google/Microsoft OAuth POST forms (measured, never pressed), 'Continue with Email' (its step reveal measured), 'Workspace SSO' and the 'Did you know?' hint card.

#### Login panel
The "Login to Fibery" form column on fibery.io/login: OAuth buttons, Continue with Email, Workspace SSO and the sign-up switch link. Read as `login-panel` on the login page.

**Values (default).** size 360 x 276.8; background transparent; text Suisse Intl 24/28.8 700, #251d1a `color.basic.black`; icon 16 x 16, #251d1a `color.basic.black`; layers div.OAuthButtonLogin_oAuthButton__00E7t 360.0x36.0 rgb(255, 253, 250) T:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) / R:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) / B:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) / L:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) rgba(214, 214, 214, 0.01) 0px 9px 2px 0px, rgba(214, 214, 214, 0.05) 0px 6px 2px 0px, rgba(214, 214, 214.

Child layers that carry the look: div 360x36 background #fffdfa `color.named.milk` border 1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) radius 6px shadow rgba(214, 214, 214, 0.01) 0px 9px 2px 0px, rgba(214, 214, 214, 0.05) 0px 6px 2px 0px, rgba(214, 214, 214, 0.18) 0px 3px 2px 0px, rgba(214, 214, 214, 0.3) 0px 1px 1px 0px, rgba(214, 214, 214, 0.35) 0px 0px 1px 0px, rgba(255, 255, 255, 0.2) 0px 1px 0px 0px inset; div 360x36 background #fffdfa `color.named.milk` border 1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) radius 6px shadow rgba(214, 214, 214, 0.01) 0px 9px 2px 0px, rgba(214, 214, 214, 0.05) 0px 6px 2px 0px, rgba(214, 214, 214, 0.18) 0px 3px 2px 0px, rgba(214, 214, 214, 0.3) 0px 1px 1px 0px, rgba(214, 214, 214, 0.35) 0px 0px 1px 0px, rgba(255, 255, 255, 0.2) 0px 1px 0px 0px inset; button 360x36 background #fffdfa `color.named.milk` border 1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) radius 6px shadow rgba(214, 214, 214, 0.01) 0px 9px 2px 0px, rgba(214, 214, 214, 0.05) 0px 6px 2px 0px, rgba(214, 214, 214, 0.18) 0px 3px 2px 0px, rgba(214, 214, 214, 0.3) 0px 1px 1px 0px, rgba(214, 214, 214, 0.35) 0px 0px 1px 0px, rgba(255, 255, 255, 0.2) 0px 1px 0px 0px inset.

![Login panel default](components/crops/login-panel-default.png)

#### Google OAuth
The "Continue with Google" OAuth submit — its form POSTs to /login/google/start; measured, never pressed. Read as `login-google` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 360 x 36; background transparent; text Suisse Intl 16/20 400, #251d1a `color.basic.black`; icon 16 x 16, #251d1a `color.basic.black`; layers div.OAuthButtonLogin_oAuthButton__00E7t 360.0x36.0 rgb(255, 253, 250) T:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) / R:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) / B:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) / L:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) rgba(214, 214, 214, 0.01) 0px 9px 2px 0px, rgba(214, 214, 214, 0.05) 0px 6px 2px 0px, rgba(214, 214, 214 |
| hover | layers div.OAuthButtonLogin_oAuthButton__00E7t 360.0x36.0 rgb(255, 253, 250) T:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.25) / R:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.25) / B:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.25) / L:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.25) rgba(214, 214, 214, 0.01) 0px 9px 2px 0px, rgba(214, 214, 214, 0.05) 0px 6px 2px 0px, rgba(214, 214, |
| focus-visible | outline 1px auto #101010, offset 0px; layers button.OAuthButtonLogin_formButton__BcoL2 360.0x36.0 1px auto rgb(16, 16, 16) offset 0px; div.OAuthButtonLogin_oAuthButton__00E7t 360.0x36.0 rgb(255, 253, 250) T:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) / R:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) / B:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) / L:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) rgba(214, 214, |

Child layers that carry the look: div 360x36 background #fffdfa `color.named.milk` border 1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) radius 6px shadow rgba(214, 214, 214, 0.01) 0px 9px 2px 0px, rgba(214, 214, 214, 0.05) 0px 6px 2px 0px, rgba(214, 214, 214, 0.18) 0px 3px 2px 0px, rgba(214, 214, 214, 0.3) 0px 1px 1px 0px, rgba(214, 214, 214, 0.35) 0px 0px 1px 0px, rgba(255, 255, 255, 0.2) 0px 1px 0px 0px inset.

![Google OAuth default](components/crops/login-google-default.png) ![Google OAuth hover](components/crops/login-google-hover.png) ![Google OAuth focus-visible](components/crops/login-google-focus-visible.png) ![Google OAuth pressed](components/crops/login-google-pressed.png)

#### Microsoft OAuth
The "Continue with Microsoft" OAuth submit; measured, never pressed. Read as `login-ms` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 360 x 36; background transparent; text Suisse Intl 16/20 400, #251d1a `color.basic.black`; icon 16 x 16, #251d1a `color.basic.black`; layers div.OAuthButtonLogin_oAuthButton__00E7t 360.0x36.0 rgb(255, 253, 250) T:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) / R:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) / B:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) / L:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) rgba(214, 214, 214, 0.01) 0px 9px 2px 0px, rgba(214, 214, 214, 0.05) 0px 6px 2px 0px, rgba(214, 214, 214 |
| hover | layers div.OAuthButtonLogin_oAuthButton__00E7t 360.0x36.0 rgb(255, 253, 250) T:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.25) / R:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.25) / B:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.25) / L:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.25) rgba(214, 214, 214, 0.01) 0px 9px 2px 0px, rgba(214, 214, 214, 0.05) 0px 6px 2px 0px, rgba(214, 214, |
| focus-visible | outline 1px auto #101010, offset 0px; layers button.OAuthButtonLogin_formButton__BcoL2 360.0x36.0 1px auto rgb(16, 16, 16) offset 0px; div.OAuthButtonLogin_oAuthButton__00E7t 360.0x36.0 rgb(255, 253, 250) T:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) / R:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) / B:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) / L:1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) rgba(214, 214, |

Child layers that carry the look: div 360x36 background #fffdfa `color.named.milk` border 1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1) radius 6px shadow rgba(214, 214, 214, 0.01) 0px 9px 2px 0px, rgba(214, 214, 214, 0.05) 0px 6px 2px 0px, rgba(214, 214, 214, 0.18) 0px 3px 2px 0px, rgba(214, 214, 214, 0.3) 0px 1px 1px 0px, rgba(214, 214, 214, 0.35) 0px 0px 1px 0px, rgba(255, 255, 255, 0.2) 0px 1px 0px 0px inset.

![Microsoft OAuth default](components/crops/login-ms-default.png) ![Microsoft OAuth hover](components/crops/login-ms-hover.png) ![Microsoft OAuth focus-visible](components/crops/login-ms-focus-visible.png) ![Microsoft OAuth pressed](components/crops/login-ms-pressed.png)

#### Email button
The "Continue with Email" button — reveals the e-mail step of the sign-in (a local step change, not a submission); the opened state was measured after pressing it. Read as `login-email` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: opened) | size 360 x 36; padding 8px 12px; border 1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1); radius 6px; background #fffdfa `color.named.milk`; shadow rgba(214, 214, 214, 0.01) 0px 9px 2px 0px, rgba(214, 214, 214, 0.05) 0px 6px 2px 0px, rgba(214, 214, 214, 0.18) 0px 3px 2px 0px, rgba(214, 214, 214, 0.3) 0px 1px 1px 0px, rgba(214, 214, 214, 0.35) 0px 0px 1px 0px, rgba(255, 255, 255, 0.2) 0px 1px 0px 0px inset; text Suisse Intl 16/20 500, #251d1a `color.basic.black`; transition border-color 0.3s ease; icon 20 x 16, #251d1a `color.basic.black` |
| hover | border 1px solid oklab(0.239148 0.0103381 0.00917888 / 0.25) |
| focus-visible | outline 1px auto #101010, offset 0px |
| pressed | border 1px solid oklab(0.239148 0.0103381 0.00917888 / 0.25) |

![Email button default](components/crops/login-email-default.png) ![Email button hover](components/crops/login-email-hover.png) ![Email button pressed](components/crops/login-email-pressed.png) ![Email button opened](components/crops/login-email-opened.png)

#### Email field (login)
The e-mail input revealed by the "Continue with Email" step; focused and typed into then cleared — never submitted. Read as `login-email-field` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 360 x 36; padding 4px 12px; border 1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1); radius 6px; background #ffffff `color.form.white`; text Suisse Intl 16/28 400, #000000; transition all 0.3s ease-in-out; placeholder #251d1a `color.basic.black` |
| focused, filled | border 1px solid oklab(0.239148 0.0103381 0.00917888 / 0.25) |

![Email field (login) default](components/crops/login-email-field-default.png) ![Email field (login) focused](components/crops/login-email-field-focused.png) ![Email field (login) filled](components/crops/login-email-field-filled.png)

#### Workspace SSO
The "Workspace SSO" button; measured, never followed. Read as `login-sso` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 360 x 36; padding 8px 12px; border 1px solid oklab(0.239148 0.0103381 0.00917888 / 0.1); radius 6px; background #fffdfa `color.named.milk`; shadow rgba(214, 214, 214, 0.01) 0px 9px 2px 0px, rgba(214, 214, 214, 0.05) 0px 6px 2px 0px, rgba(214, 214, 214, 0.18) 0px 3px 2px 0px, rgba(214, 214, 214, 0.3) 0px 1px 1px 0px, rgba(214, 214, 214, 0.35) 0px 0px 1px 0px, rgba(255, 255, 255, 0.2) 0px 1px 0px 0px inset; text Suisse Intl 16/20 500, #251d1a `color.basic.black`; transition border-color 0.3s ease; icon 20 x 18, #251d1a `color.basic.black` |
| hover | border 1px solid oklab(0.239148 0.0103381 0.00917888 / 0.25) |
| focus-visible | outline 1px auto #101010, offset 0px |
| pressed | border 1px solid oklab(0.239148 0.0103381 0.00917888 / 0.25) |

![Workspace SSO default](components/crops/login-sso-default.png) ![Workspace SSO hover](components/crops/login-sso-hover.png) ![Workspace SSO focus-visible](components/crops/login-sso-focus-visible.png) ![Workspace SSO pressed](components/crops/login-sso-pressed.png)

#### Hint card
The "Did you know?" tip card beside the sign-in (the dark/system theme tip). Read as `login-hint` on the login page.

**Values (default).** size 560.8 x 850; padding 40px; radius 20px; background #d5d8ca `color.tertiary.green`; image url(…); shadow rgba(0, 0, 0, 0.05) 0px 0px 0px 1px inset; text Suisse Intl 20/20 700, #251d1a `color.basic.black`; icon 18 x 18, #000000.

![Hint card default](components/crops/login-hint-default.png)

### Mobile (390 wide)

The phone surface at 390 wide: the top bar, the sandwich button and the nav drawer it opens, the hero and its CTA.

#### Mobile top bar
The phone header: Fibery mark, the sandwich button and the sign-up CTA. Read as `m-topbar` on the home page at 390 wide.

**Values (default).** size 390 x 77; padding 12px; background transparent; text Suisse Intl 16/19.2 400, #251d1a `color.basic.black`; layers div.HeaderMainMenu_root__idMKp 366.0x53.0 rgb(255, 245, 232) rgba(20, 21, 26, 0.08) 0px 10px 16px -3px, rgba(20, 21, 26, 0.05) 0px 1px 2px 0px 12px; nav::before.HeaderMainMenu_menuList__q0OJp 100%x100% rgb(255, 245, 232) 10px; div.HeaderMainMenu_headerDivider__6tgCG 0.0x0.0 rgba(0, 0, 0, 0.25); div.HeaderMenuItem_root__Lva5Q.HeaderMenuItem_mobileHidden__ssM4C 0.0x0.0 T:1px solid rgba(0, 0, 0, 0) /.

Child layers that carry the look: div 366x53 background #fff5e8 radius 12px shadow rgba(20, 21, 26, 0.08) 0px 10px 16px -3px, rgba(20, 21, 26, 0.05) 0px 1px 2px 0px; nav::before 100%x100% background #fff5e8 radius 10px; div 0x0 background rgba(0, 0, 0, 0.25).

![Mobile top bar default](components/crops/m-topbar-default.png)

#### Mobile menu button
The icon-only sandwich button that opens the phone nav — a local UI toggle; the opened state was measured after activating it. Read as `m-menu-btn` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, opened) | size 20 x 20; background transparent; text Suisse Intl 16/19.2 400, #251d1a `color.basic.black`; layers ::before rgb(37, 29, 26) 0px none 1; ::after rgb(37, 29, 26) 0px none 1; div::before.HeaderMainMenu_sandwichBtn__VTPQ2 20pxx2px rgb(37, 29, 26) 2px; div::after.HeaderMainMenu_sandwichBtn__VTPQ2 20pxx2px rgb(37, 29, 26) 2px |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: div::before 20pxx2px background #251d1a `color.basic.black` radius 2px; div::after 20pxx2px background #251d1a `color.basic.black` radius 2px.

![Mobile menu button default](components/crops/m-menu-btn-default.png) ![Mobile menu button hover](components/crops/m-menu-btn-hover.png) ![Mobile menu button pressed](components/crops/m-menu-btn-pressed.png) ![Mobile menu button opened](components/crops/m-menu-btn-opened.png)

#### Mobile nav
The nav drawer opened by the sandwich button — the menu list plus the Book a demo / Log in / Sign up buttons; its links were never followed. Read as `m-drawer` on the home page at 390 wide.

**Values (default).** size 366 x 749.97; padding 12px; radius 12px; background #fff5e8; shadow rgba(20, 21, 26, 0.08) 0px 10px 16px -3px, rgba(20, 21, 26, 0.05) 0px 1px 2px 0px; text Suisse Intl 16/34 500, #251d1a `color.basic.black`.

![Mobile nav default](components/crops/m-drawer-default.png)

#### Mobile hero headline
The display headline at 390 wide. Read as `m-hero-h1` on the home page at 390 wide.

**Values (default).** size 358.81 x 184; background transparent; text Suisse Intl 46/46 800, #251d1a `color.basic.black`.

![Mobile hero headline default](components/crops/m-hero-h1-default.png)

#### Mobile hero CTA
The "Sign up" hero button at 390 wide; measured never followed. Read as `m-hero-cta` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 358.81 x 40; padding 0px 24px; radius 6px; background #251d1a `color.basic.black`; text Suisse Intl 16/40 600, #faebd6 `color.named.soup`; transition all 0.3s ease |
| focus-visible | outline 1px auto #e59700, offset 1px |
| pressed | shadow #251d1a 0px 0px 0px 1px |

![Mobile hero CTA default](components/crops/m-hero-cta-default.png) ![Mobile hero CTA hover](components/crops/m-hero-cta-hover.png) ![Mobile hero CTA focus-visible](components/crops/m-hero-cta-focus-visible.png) ![Mobile hero CTA pressed](components/crops/m-hero-cta-pressed.png)

### Footer

The page footer: sitemap columns, social icons and the legal/security links.

#### Footer
The page footer: sitemap columns, social icons, security/legal links. Read as `footer` on the home page.

**Values (default).** size 1440 x 489.56; background transparent; text Suisse Intl 14/21 400, #251d1a `color.basic.black`; icon 86 x 36, #0000ee; layers div.FooterMain_mainPart__47yxl 1440.0x416.4 rgb(253, 247, 239); a.AskAiAboutFibery_urlItem__SKDx8.plausible-event-name=Ask+Chat+GPT+About+Fibery 25.0x25.0 rgb(255, 253, 250) T:1px solid rgb(238, 208, 191) / R:1px solid rgb(238, 208, 191) / B:1px solid rgb(238, 208, 191) / L:1px solid rgb(238, 208, 191) 6px; a.AskAiAboutFibery_urlItem__SKDx8.plausible-event-name=Ask+Claude+About+Fibery 25.0x25.0 rg.

Child layers that carry the look: div 1440x416.4 background #fdf7ef `color.named.cream`; a 25x25 background #fffdfa `color.named.milk` border 1px solid #eed0bf `color.named.peachSoup` radius 6px; a 25x25 background #fffdfa `color.named.milk` border 1px solid #eed0bf `color.named.peachSoup` radius 6px.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer sitemap link; measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 45 x 24; background transparent; text Suisse Intl 14/21 400, #251d1a `color.basic.black` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a 45.0x24.0 1px auto rgb(16, 16, 16) offset 1px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

## Icons

140 SVGs were lifted from the pages into [icons/](icons), named by role, with the source table in [icons/INDEX.tsv](icons/INDEX.tsv). Colour is `currentColor` wherever the icon took its colour from the text, so each recolours from CSS `color`. These are the interface icons; the illustrations, the Fibery dog artwork and the product imagery were left out. The SVGs are Fibery's property, kept for reference only.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|
| [sociallink](icons/sociallink-293fe484.svg) | 16x14 18x14 | 0 0 18 14 | fill | home; pricing; templates; features; stories; blog; about; download; menu; mobile drawer |  |
| [sociallink](icons/sociallink-3d12265a.svg) | 15x16 16x16 | 0 0 16 16 | fill | home; pricing; templates; features; stories; blog; about; download; menu; mobile drawer |  |
| [sociallink](icons/sociallink-4de6be5e.svg) | 16x14 18x14 | 0 0 18 14 | fill | home; pricing; templates; features; stories; blog; about; download; menu; mobile drawer |  |
| [sociallink](icons/sociallink-5b3c14eb.svg) | 15x14 16x14 | 0 0 16 14 | fill | home; pricing; templates; features; stories; blog; about; download; menu; mobile drawer |  |
| [sociallink](icons/sociallink-a05341da.svg) | 19x20 21x20 | 0 0 21 20 | fill | home; pricing; templates; features; stories; blog; about; download; menu; mobile drawer |  |
| [sociallink](icons/sociallink-c97d0aa1.svg) | 18x20 20x20 | 0 0 20 20 | fill | home; pricing; templates; features; stories; blog; about; download; menu; mobile drawer |  |
| [root](icons/root-b4a1a0cd.svg) | 10x10 12x12 | 0 0 20 20 | fill | home; pricing; templates; features; stories; about; download; menu; mobile drawer | Changelog: November 5, 2026 / Community A place to exchange  |
| [flagwrap](icons/flagwrap.svg) | 18x12 | 0 0 810 540 | fill | home; pricing; templates; features; stories; about; download; menu; mobile drawer |  |
| [root](icons/root-8496c203.svg) | 20x20 | 0 0 20 18 | fill | home; pricing; about; menu; mobile drawer |  |
| [root](icons/root-76bc33a7.svg) | 20x20 | 0 0 20 18 | fill | home; menu; mobile drawer; sign-up | Are we turning Fibery into yet another A / See what our cust |
| [board](icons/board.svg) | 16x16 | 0 0 16 16 | fill | home; menu; mobile drawer | Board |
| [root](icons/root-082be65e.svg) | 20x20 | 0 0 23 15 | fill | home; menu; mobile drawer | Are we turning Fibery into yet another A / See what our cust |
| [non-profit](icons/non-profit.svg) | 20x20 | 0 0 20 20 | fill | home; menu; mobile drawer | Non-profit |
| [enterprise](icons/enterprise.svg) | 20x20 | 0 0 20 20 | fill | home; menu; mobile drawer | Enterprise |
| [calendar](icons/calendar.svg) | 16x16 | 0 0 16 16 | fill | home; menu; mobile drawer | Calendar |
| [report](icons/report.svg) | 16x16 | 0 0 16 16 | fill | home; menu; mobile drawer | Report |
| [dashboard](icons/dashboard.svg) | 16x16 | 0 0 16 16 | fill | home; menu; mobile drawer | Dashboard |
| [gantt](icons/gantt.svg) | 16x16 | 0 0 16 16 | fill | home; menu; mobile drawer | Gantt |
| [feed](icons/feed.svg) | 16x16 | 0 0 16 16 | fill | home; menu; mobile drawer | Feed |
| [list](icons/list.svg) | 16x16 | 0 0 16 16 | fill | home; menu; mobile drawer | List |
| [root](icons/root-7d4b8928.svg) | 20x20 | 0 0 20 20 | fill | home; menu; mobile drawer |  |
| [map](icons/map.svg) | 16x16 | 0 0 16 16 | fill | home; menu; mobile drawer | Map |
| [startup](icons/startup-8404f020.svg) | 20x20 | 0 0 20 20 | fill | home; menu; mobile drawer | Startup |
| [table](icons/table.svg) | 16x16 | 0 0 16 16 | fill | home; menu; mobile drawer | Table |
| [timeline](icons/timeline.svg) | 16x16 | 0 0 16 16 | fill | home; menu; mobile drawer | Timeline |
| [agency](icons/agency.svg) | 20x20 | 0 0 20 20 | fill | home; menu; mobile drawer | Agency |
| [gallery](icons/gallery.svg) | 16x16 | 0 0 16 16 | fill | home; menu; mobile drawer | Gallery |
| [form](icons/form.svg) | 16x16 | 0 0 16 16 | fill | home; menu; mobile drawer | Form |
| [root](icons/root-dd53366e.svg) | 20x20 | 0 0 18 18 | fill | home; menu; mobile drawer |  |
| [pause](icons/pause.svg) | 24x24 | 0 0 24 24 | fill | home; menu; mobile drawer | Pause |
| [root](icons/root-fb88f3cd.svg) | 20x20 | 0 0 20 20 | fill | home; menu; mobile drawer |  |
| [features](icons/features.svg) | 17x17 | 0 0 16 15 | fill | home; menu; mobile drawer | Features / Integrations / See changelog |
| [root](icons/root-6f03c357.svg) | 60x60 | 0 0 60 60 | fill | home; menu |  |
| [templateitemsquareicon](icons/templateitemsquareicon-22547a06.svg) | 15x15 23x23 | 0 0 20 20 | fill | features; stories | How Lemonade's tech team connects strate / How to organize h |
| [templateitemsquareicon](icons/templateitemsquareicon-3b10c926.svg) | 15x15 23x23 | 0 0 20 20 | fill | features; stories | How Lemonade's tech team connects strate / How e-com startup |
| [templateitemsquareicon](icons/templateitemsquareicon-4ee6a710.svg) | 15x15 23x23 | 0 0 18 21 | fill | features; stories | How Lemonade's tech team connects strate / How B2B SaaS mana |
| [templateitemsquareicon](icons/templateitemsquareicon-56262e0a.svg) | 24x24 36x36 | 0 0 40 40 | fill | features; stories | How Lemonade's tech team connects strate |
| [templateitemsquareicon](icons/templateitemsquareicon-6cf2174b.svg) | 15x15 | 0 0 20 21 | fill | features; stories | How e-com startup tests assumptions and  / How B2B SaaS mana |
| [templateitemsquareicon](icons/templateitemsquareicon-7cf253ce.svg) | 15x15 | 0 0 20 20 | fill | features; stories | How to organize hardware & software deve / How PowerX tracks |
| [templateitemsquareicon](icons/templateitemsquareicon-8e04da00.svg) | 15x15 | 0 0 19 22 | fill | features; stories | How e-com startup tests assumptions and  / How HR startup tu |
| [root](icons/root-03bf0a65.svg) | 20x20 | 0 0 20 20 | fill | download |  |
| [root](icons/root-09fccd32.svg) | 18x18 | 0 0 18 18 | fill | pricing |  |
| [root](icons/root-0a5867f3.svg) | 48x48 | 0 0 32 32 | fill | stories | Product Create an uninterrupted flow fro |
| [root](icons/root-0cd72cdd.svg) | 30x30 | 0 0 20 20 | fill | features | Whiteboards Create interactive diagrams, |
| [workspace-sso](icons/workspace-sso.svg) | 20x18 | 0 0 20 18 | fill | login | Workspace SSO |
| [root](icons/root-0e5b86b8.svg) | 30x30 | 0 0 20 20 | fill | features | Collaborative Documents Mix docs with yo |
| [icon-13f8b839](icons/icon-13f8b839.svg) | 24x24 | 0 0 52 52 | fill | pricing |  |
| [root](icons/root-14144cab.svg) | 30x30 | 0 0 20 20 | fill | features | Full-text search Find tasks, documents,  |
| [templateitemsquareicon](icons/templateitemsquareicon-16fb453d.svg) | 24x24 | 0 0 40 40 | fill | stories | How Vandrouka uses Fibery for game devel |
| [templateitemsquareicon](icons/templateitemsquareicon-1fa5811f.svg) | 24x24 | 0 0 39 38 | fill | stories | How Thundra plans and tracks software de |
| [root](icons/root-2196f133.svg) | 48x48 | 0 0 32 32 | fill | stories | 6 months for free Startup Invent, build, |
| [root](icons/root-232d5482.svg) | 30x30 | 0 0 20 20 | fill | features | Templates Get started with User Research |
| [recruitment](icons/recruitment.svg) | 13x13 | 0 0 21 18 | fill | menu | Recruitment |
| [root](icons/root-28ad4c30.svg) | 32x32 | 0 0 32 32 | fill | menu | Startup Invent, build, and grow — withou |
| [root](icons/root-2bbfeaac.svg) | 32x32 | 0 0 32 32 | fill | menu | Integrations Get a single connected work |
| [root](icons/root-2cae7634.svg) | 32x32 | 0 0 32 32 | fill | menu | Templates Discover, install and fully cu |
| [connect-in](icons/connect-in.svg) | 17x17 | 0 0 24 24 | fill | download | Connect in |
| [root](icons/root-312ed351.svg) | 30x30 | 0 0 20 20 | fill | features | API Integrate Fibery with external syste |
| [icon-32de545f](icons/icon-32de545f.svg) | 24x24 | 0 0 52 52 | fill | pricing |  |
| [digital-agency-crm](icons/digital-agency-crm.svg) | 16x16 | 0 0 15 15 | fill | sign-up | Digital agency CRM |
| [root](icons/root-3545cf41.svg) | 40x40 | 0 0 141 141 | fill | mobile drawer |  |
| [templateitemsquareicon](icons/templateitemsquareicon-3a1641ab.svg) | 15x15 | 0 0 21 20 | fill | stories | How B2B SaaS manages roadmap and feedbac / How ScootAPI coll |
| [root](icons/root-3c5c1d9a.svg) | 30x30 | 0 0 20 20 | fill | features | Integrations Connect Fibery to dozens of |
| [templateitemsquareicon](icons/templateitemsquareicon-41779656.svg) | 15x15 | 0 0 20 20 | fill | stories | Improving leave management and staff vac |
| [root](icons/root-4e5d1fc1.svg) | 32x32 | 0 0 32 32 | fill | menu | No-code Design your perfect workspace fr |
| [root](icons/root-4e65cdcb.svg) | 32x32 | 0 0 32 32 | fill | menu | Expert help Choose your favorite format: |
| [root](icons/root-56e90cf1.svg) | 29x40 | 0 0 103 141 | fill | mobile drawer |  |
| [root](icons/root-5711fff1.svg) | 24x24 | 0 0 20 20 | fill | login |  |
| [templateitemsquareicon](icons/templateitemsquareicon-58f06ed1.svg) | 15x15 | 0 0 20 18 | fill | stories | How Soft Dev agency automated recruiting |
| [create-workspace](icons/create-workspace.svg) | 12x10 | 0 0 14 12 | fill | sign-up | Create workspace |
| [root](icons/root-59a7748c.svg) | 32x32 | 0 0 32 32 | fill | menu | Digital agency Collaborate with clients, |
| [icon-5a71633b](icons/icon-5a71633b.svg) | 24x24 | 0 0 52 52 | fill | pricing |  |
| [icon-5c0ba132](icons/icon-5c0ba132.svg) | 24x24 | 0 0 52 52 | fill | pricing |  |
| [templateitemsquareicon](icons/templateitemsquareicon-5dd2f67a.svg) | 15x15 | 0 0 18 21 | fill | stories | How Santa Uses Fibery to make Christmas  |
| [product-development](icons/product-development.svg) | 16x16 | 0 0 16 16 | fill | sign-up | Product development |
| [root](icons/root-6261c8cc.svg) | 18x18 | 0 0 18 18 | fill | pricing |  |
| [install-in](icons/install-in.svg) | 17x17 | 0 0 24 24 | fill | download | Install in |
| [templateitemsquareicon](icons/templateitemsquareicon-633e72d2.svg) | 15x15 | 0 0 15 22 | fill | stories | How Tokatab prioritises and plans featur |
| [templateitemsquareicon](icons/templateitemsquareicon-65bf8401.svg) | 15x15 | 0 0 20 20 | fill | stories | How product studio uses Fibery to build  / How KeyGuru track |
| [root](icons/root-6d13de33.svg) | 30x30 | 0 0 20 20 | fill | features | Custom formulas Use powerful formulas to |
| [templateitemsquareicon](icons/templateitemsquareicon-6f634a00.svg) | 15x15 | 0 0 21 20 | fill | stories | How Vandrouka uses Fibery for game devel / How Soft Dev agen |
| [root](icons/root-703a6ea0.svg) | 30x30 | 0 0 20 20 | fill | features | Smart Folders Show filtered and sorted l |
| [startup](icons/startup-71b7f44c.svg) | 16x16 | 0 0 14 16 | fill | sign-up | Startup |
| [root](icons/root-71b88e47.svg) | 30x30 | 0 0 20 20 | fill | features | Custom Action Buttons Replace the same s |
| [root](icons/root-726b6416.svg) | 30x30 | 0 0 18 18 | fill | features | Custom Appsnew Build exactly what you ne |
| [continue-with-google](icons/continue-with-google.svg) | 16x16 | 0 0 16 16 | fill | login | Continue with Google |
| [templateitemsquareicon](icons/templateitemsquareicon-75cf27b5.svg) | 15x15 | 0 0 21 21 | fill | stories | How Santa Uses Fibery to make Christmas  |
| [root](icons/root-764fa56a.svg) | 32x32 | 0 0 32 32 | fill | menu | Getting started Explore educational mate |
| [root](icons/root-77b74d30.svg) | 18x18 | 0 0 18 18 | fill | pricing |  |
| [root](icons/root-79cdb938.svg) | 30x30 | 0 0 20 20 | fill | features | Browser Extension Add Ideas, Insights, C |
| [templateitemsquareicon](icons/templateitemsquareicon-7a4fd05f.svg) | 15x15 | 0 0 22 18 | fill | stories | How tech startup unites tasks, docs, and / How B2B SaaS tool |
| [chrome-extension](icons/chrome-extension.svg) | 17x17 | 0 0 14 14 | fill | download | Chrome extension |
| [root](icons/root-7c7d8887.svg) | 18x18 | 0 0 20 20 | stroke | login |  |
| [root](icons/root-7f27e5b6.svg) | 18x18 | 0 0 18 18 | fill | pricing |  |
| [okr-tracking](icons/okr-tracking.svg) | 13x13 | 0 0 20 20 | fill | menu | OKR Tracking |
| [root](icons/root-8329f698.svg) | 40x40 | 0 0 141 141 | fill | mobile drawer |  |
| [root](icons/root-856f5a39.svg) | 20x20 | 0 0 20 20 | fill | download |  |
| [root](icons/root-89711ca7.svg) | 48x48 | 0 0 32 32 | fill | stories | Digital agency Collaborate with clients, |
| [root](icons/root-8b7467ca.svg) | 32x32 | 0 0 32 32 | fill | menu | Product Turn customer insights into real |
| [root](icons/root-8c342698.svg) | 30x30 | 0 0 20 20 | fill | features | Custom domain & connected processes Refl |
| [root](icons/root-8e12de07.svg) | 30x30 | 0 0 20 20 | fill | features | Automation Rules Automate repetitive act |
| [root](icons/root-8e3f726b.svg) | 32x32 | 0 0 32 32 | fill | menu | Community A place to exchange ideas, exp |
| [root](icons/root-92c4513e.svg) | 30x30 | 0 0 20 20 | fill | features | Forms Grab outside data from users, co-w |
| [root](icons/root-94064112.svg) | 30x30 | 0 0 20 20 | fill | features | Documents and entities sharing Share any |
| [templateitemsquareicon](icons/templateitemsquareicon-960f12e8.svg) | 15x15 | 0 0 21 18 | fill | stories | How Santa Uses Fibery to make Christmas  |
| [root](icons/root-9ac676fe.svg) | 32x32 | 0 0 32 32 | fill | menu | Fibery AI Brainstorm, automate tasks, fi |
| [sales-crm](icons/sales-crm.svg) | 13x13 | 0 0 19 22 | fill | menu | Sales CRM |
| [root](icons/root-9d8e60ee.svg) | 30x30 | 0 0 20 20 | fill | features | Dashboards Visualize information in a de |
| [continue-with-microsoft](icons/continue-with-microsoft.svg) | 16x16 | 0 0 16 16 | fill | login | Continue with Microsoft |
| [root](icons/root-a766d30e.svg) | 20x20 | 0 0 16 23 | fill | download |  |
| [root](icons/root-a96ddbba.svg) | 29x40 | 0 0 103 141 | fill | mobile drawer |  |
| [icon-a9e5b4eb](icons/icon-a9e5b4eb.svg) | 24x24 | 0 0 52 52 | fill | pricing |  |
| [root](icons/root-abfdae94.svg) | 30x30 | 0 0 20 20 | fill | features | Change history Track changes happening i |
| [imagewrap](icons/imagewrap.svg) | 40x40 | 0 0 120 120 | fill | download |  |
| [icon-b449e89f](icons/icon-b449e89f.svg) | 24x24 | 0 0 52 52 | fill | pricing |  |
| [root](icons/root-b73be7f2.svg) | 20x20 | 0 0 20 12 | fill | download |  |
| [root](icons/root-b815ec74.svg) | 30x30 | 0 0 20 20 | fill | features | Charts Transform data into information a |
| [templateitemsquareicon](icons/templateitemsquareicon-b8e08ca6.svg) | 15x15 | 0 0 20 20 | fill | stories | How marketing agency manages projects an |
| [icon-bd289a92](icons/icon-bd289a92.svg) | 24x24 | 0 0 52 52 | fill | pricing |  |
| [root](icons/root-c2ce62df.svg) | 40x40 | 0 0 141 141 | fill | mobile drawer |  |
| [root](icons/root-cacd745d.svg) | 48x48 | 0 0 32 32 | fill | stories | Software development Run sprints the way |
| [surprise-me](icons/surprise-me.svg) | 16x16 | 0 0 16 16 | fill | sign-up | Surprise me |
| [templateitemsquareicon](icons/templateitemsquareicon-ce676b9b.svg) | 15x15 | 0 0 26 26 | fill | stories | How marketing agency manages projects an |
| [root](icons/root-d4bfccfc.svg) | 32x32 | 0 0 32 32 | fill | menu | Features Explore our most powerful featu |
| [root](icons/root-d52f1c77.svg) | 30x30 | 0 0 20 20 | stroke | features | Dependency Management Create dependencie |
| [root](icons/root-d739f7b7.svg) | 32x32 | 0 0 32 32 | fill | menu | Webinars & tutorials Watch our previous  |
| [root](icons/root-db6374f4.svg) | 30x30 | 0 0 20 20 | fill | features | Bi-directional links Make knowledge disc |
| [icon-de3be581](icons/icon-de3be581.svg) | 24x24 | 0 0 52 52 | fill | pricing |  |
| [continue-with-email](icons/continue-with-email.svg) | 20x16 | 0 0 20 16 | fill | login | Continue with Email |
| [root](icons/root-e4a47006.svg) | 30x30 | 0 0 20 20 | fill | features | Customizable Views Visualize your data u |
| [icon-e6378a94](icons/icon-e6378a94.svg) | 24x24 | 0 0 52 52 | fill | pricing |  |
| [root](icons/root-e7013d53.svg) | 30x30 | 0 0 20 20 | fill | features | Data import and export Import data into  |
| [icon-e8f14d68](icons/icon-e8f14d68.svg) | 24x24 | 0 0 52 52 | fill | pricing |  |
| [root](icons/root-ed1c9377.svg) | 30x30 | 0 0 20 20 | fill | features | MCP Servernew Connect Claude, ChatGPT, o |
| [templateitemsquareicon](icons/templateitemsquareicon-ed265c98.svg) | 15x15 | 0 0 18 20 | fill | stories | How marketing agency manages projects an / Project planning  |
| [root](icons/root-ee091fcc.svg) | 30x30 | 0 0 20 20 | fill | features | Permissions & Sharing Set up granular pe |
| [root](icons/root-f0402652.svg) | 32x32 | 0 0 32 32 | fill | menu | Software development Run sprints your wa |
| [templateitemsquareicon](icons/templateitemsquareicon-f05449c6.svg) | 15x15 | 0 0 21 18 | fill | stories | How Soft Dev agency automated recruiting |
| [firefox-extension](icons/firefox-extension.svg) | 17x17 | 0 0 16 16 | fill | download | Firefox extension |
| [root](icons/root-f9cc3d72.svg) | 14x14 | 0 0 20 20 | fill | pricing |  |

## Gaps

### The signed-in product

Fibery's product is the workspace app: every post-login surface — the spaces, entity views, whiteboards, automations, AI and admin — needs an account and was never reached. fibery.io/sign-up and fibery.io/login/ are the only app surfaces a signed-out visitor sees, and they were measured as forms, never submitted. The hero product video and the product screenshots on the marketing pages are mocks, not the product.

### Pages

- **The account.** Every post-login surface was never reached; the OAuth forms on /login were measured and never pressed, 'Continue with Email' was pressed only far enough to reveal the field (typed into then cleared, never submitted), 'Workspace SSO' was never followed, and the wizard was never advanced past step one — 'Create workspace' and 'Start without AI' were never pressed, so steps 2+ of the sign-up are uncaptured.
- **The demo.** 'Book a demo' links to a scheduler that was never opened; what it asks is unverified.
- **Articles, stories and templates** are covered by one captured example each (one blog post, the stories index, one template detail); the other article, story and template routes are the same templates, unmeasured.
- **Tall pages.** /101-questions-about-fibery (37,790px) and the other long pages were captured whole by scroll-stitching (the kit's 8-tile full-page cap collapses the FAQ, so the runner scrolls a stable viewport and stitches — the merged sidecar records `capture.mode: stitchedParts`, built from 42 `scrollViewport` part captures; the blog, templates and two mobile fulls are `stitchedParts` from `clip` parts).

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error, loading and validation states** were not seen on the public surface — the forms were never submitted.
- **Mega-menu items' focus/hover** is partially covered: the panel closes on blur, so a real keyboard focus inside it could not always be held.

### Themes

Fibery's public surfaces paint one light theme: no toggle anywhere, no `prefers-color-scheme` variants in the stylesheets, the same warm palette on the marketing pages, the sign-up wizard and the sign-in. The signed-in app does offer a dark/system theme — the login page's 'Did you know?' hint advertises it — but it is behind sign-in and was not captured, so the token file ships core + light only and the style guide has no dark mode.

### Fonts

- **Suisse Intl** (100–900 static weights; every control, nav item and body line), **Fraunces Var** (the serif display on headlines and quotes), **Casuar** and **Inter Var** (special and embedded surfaces) are the served faces, self-hosted from /_next/static/media. The style guide falls back to system fonts.

### Screenshots

- The product mocks, photography and video frames in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Article copy, customer names, the template contents and the video frames are the product's content; only frames and components were measured.
- No personal data was captured: the pages were read signed out, no form was submitted, and the login page's CSRF fields were never sent.
