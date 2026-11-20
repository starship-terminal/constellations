# Family components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from family.co and app.family.co on 2026-11-14, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, downloaded or submitted; the Log In, Get Started, Download on iOS and every Watch action was measured, never followed, and the two fields were typed into and cleared, never sent.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (64 components, 138 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (135 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: every public surface paints the one light theme (the app declares a [data-theme="dark"] layer — 23 names — that never paints while signed out; it is token evidence only). Desktop shots are 1440 x 900 at 1x; `-full` pages are stitched full-page captures capped at 8 chunks; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [demo](screenshots/home-light-demo.png), [full](screenshots/home-light-full.png), [menu-developers](screenshots/home-light-menu-developers.png), [menu-resources](screenshots/home-light-menu-resources.png) |
| Blog | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Blog post | `/blog/why-family-accounts` | [default](screenshots/blog-post-light-default.png), [full](screenshots/blog-post-light-full.png) |
| Changelog | `/changelog` | [default](screenshots/changelog-light-default.png), [full](screenshots/changelog-light-full.png) |
| Help & Support | `/support` | [default](screenshots/support-light-default.png), [full](screenshots/support-light-full.png) |
| Support article | `/support/import-a-wallet-from-metamask` | [default](screenshots/support-article-light-default.png), [full](screenshots/support-article-light-full.png) |
| FAQs | `/faqs` | [default](screenshots/faqs-light-default.png), [full](screenshots/faqs-light-full.png) |
| Legal | `/legal` | [default](screenshots/legal-light-default.png), [full](screenshots/legal-light-full.png) |
| Docs | `/docs` | [default](screenshots/docs-light-default.png), [full](screenshots/docs-light-full.png) |
| ConnectKit docs | `/docs/connectkit` | [default](screenshots/docs-connectkit-light-default.png), [full](screenshots/docs-connectkit-light-full.png) |
| Family docs | `/docs/family-account` | [default](screenshots/docs-account-light-default.png), [full](screenshots/docs-account-light-full.png) |
| App login | `app.family.co/` | [default](screenshots/login-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [drawer](screenshots/mobile-home-light-drawer.png), [full](screenshots/mobile-home-light-full.png) |
| Support, phone | `/support` | [default](screenshots/mobile-support-light-default.png), [full](screenshots/mobile-support-light-full.png) |
| App login, phone | `app.family.co/` | [default](screenshots/mobile-login-light-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Developers dropdown | header, / | hovering the Developers trigger — a local UI toggle, never a navigation | [home-light-menu-developers](screenshots/home-light-menu-developers.png), [nav-dropdown](#nav-dropdown) |
| Resources dropdown | header, / | hovering the Resources trigger | [home-light-menu-resources](screenshots/home-light-menu-resources.png) |
| Watch-the-demo overlay | / | a Watch the demo button's own press — a local video overlay, never a download | [home-light-demo](screenshots/home-light-demo.png), [demo-overlay](#demo-overlay) |
| Mobile drawer | phone, / | the hamburger button's own press — a local toggle | [mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png), [m-menu](#mobile-menu-button) |
| App login field | app.family.co/ | typed into then cleared — the form was never submitted | [login-field](#emailphone-field) |
| Support search | /support | typed into then cleared — nothing was searched | [sup-search](#support-search) |
| Signed-in product | an Aave Account | logging in and every post-login surface needs an account | boundary; see Gaps |
| The iOS app | an Apple device | Family the wallet is an iOS app; the site links to the App Store | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 21 components were given a real keyboard focus. 10 draw an outline ring: `nav-developers` (2px solid color(display-p3 0.517647 0.509804 0.505882), offset 1px), `nav-resources` (2px solid color(display-p3 0.517647 0.509804 0.505882), offset 1px), `nav-twitter` (2px solid color(display-p3 0.517647 0.509804 0.505882), offset 1px), `faq-toggle` (2px solid color(display-p3 0.517647 0.509804 0.505882), offset 0px), `blog-card` (2px solid color(display-p3 0.517647 0.509804 0.505882), offset 1px), `blog-filter` (2px solid color(display-p3 0.517647 0.509804 0.505882), offset 0px), `post-back` (2px solid color(display-p3 0.517647 0.509804 0.505882), offset 1px), `cl-filter` (2px solid color(display-p3 0.517647 0.509804 0.505882), offset 0px), `login-learn` (2px solid rgba(0, 122, 255, 0.5) `color.focus.color`, offset 1px), `login-footer-link` (2px solid rgba(0, 122, 255, 0.5) `color.focus.color`, offset 1px). 1 draw a focus ring as a shadow instead: `demo-btn`. 2 change only their border: `sup-article-link`, `art-side-link`. The other 8 show no measured change: `login-btn`, `getstarted-btn`, `download-cta`, `sup-category`, `legal-section`, `ck-cta`, `m-menu`, `m-download`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.08s | `ease-out` | all | art-side-link, sup-article-link, sup-category |
| 0.1s | `ease` | background, background-color, box-shadow, color, opacity, transform | blog-card, demo-btn, download-cta, getstarted-btn, login-footer-link, m-download, nav-dropdown, tweet-card and more |
| 0.2s | `ease` | background, color, transform | blog-filter, cl-filter, login-learn, nav-developers, nav-resources, nav-twitter |
| 0.2s | `ease-out` | all | ck-cta, legal-section, login-btn, mkt-logo, post-back |
| 0.3s | `ease` | opacity | login-field |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Post card](#post-card) | 1024 x 280 | B: 1px solid color(display-p3 0.94902 0.941176 0.929412) | - | transparent | none | 96px 0px 72px 0px |
| [Tweet card](#tweet-card) | 540 x 204 | - | 10px | color(display-p3 1 1 1) | color(display-p3 0.94902 0.941176 0.929412) 0px 0px 0px 1px inset | 32px |
| [Nav dropdown](#nav-dropdown) | 316 x 135 | - | 8px | #ffffff `color.overlay.color` | rgba(0, 0, 0, 0.1) 0px 3px 16px 0px | 4px |
| [FAQ item](#faq-item) | 512 x 56 | B: 1px solid color(display-p3 0.94902 0.941176 0.929412) | - | transparent | none | 0px 0px 28px 0px |
| [Category button](#category-button) | 240 x 29.92 | - | 8px | transparent | none | 10px 0px |
| [Login card](#login-card) | 380 x 284 | - | - | transparent | none | 0 |
| [Mobile FAQ item](#mobile-faq-item) | 342 x 56 | B: 1px solid color(display-p3 0.94902 0.941176 0.929412) | - | transparent | none | 0px 0px 28px 0px |

## Components

### Header and navigation

The public top bar on every marketing surface: the Family wordmark, the Developers and Resources hover dropdowns, X (Twitter), the beige Log In pill and the near-black Get Started pill.

#### Site header
The fixed top bar: the Family wordmark, the Developers/Resources hover dropdowns, X (Twitter), Log In and the dark Get Started pill. Read as `mkt-header` on the home page.

**Values (default).** size 1024 x 94; background transparent; text Inter 15/10 500, #282624; transform matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1); icon 72 x 18, #262626; layers a 119.0x32.9 #ffffff `color.overlay.color` 6px; div.Nav__DropdownContainer-sc-141m4ur-3.jmGeWm 303.4x129.6 #ffffff `color.overlay.color` rgba(0, 0, 0, 0.1) 0px 3px 16px 0px 8px; div.Nav__IconContainer-sc-141m4ur-2.jhkKsN 34.6x34.6 #ffffff `color.overlay.color` rgba(0, 0, 0, 0.04) 0px 0px 0px 1px 9.6px; div.Nav__IconContainer-sc-141m4ur-2.jhkKsN 34.6x34.6 #ffffff `color.overlay.color` rgba(0, 0, 0,.

Child layers that carry the look: a 119x32.9 background #ffffff `color.overlay.color` radius 6px; div 303.4x129.6 background #ffffff `color.overlay.color` radius 8px shadow rgba(0, 0, 0, 0.1) 0px 3px 16px 0px; div 34.6x34.6 background #ffffff `color.overlay.color` radius 9.6px shadow rgba(0, 0, 0, 0.04) 0px 0px 0px 1px.

![Site header default](components/crops/mkt-header-default.png)

#### Logo
The Family wordmark at the left of the header. Read as `mkt-logo` on the home page.

**Values (default).** size 96 x 34; padding 8px 12px; radius 6px; background transparent; text Inter 16/normal 500, #474645; transition all 0.2s ease-out; icon 72 x 18, #262626.

![Logo default](components/crops/mkt-logo-default.png)

#### Developers menu
The Developers dropdown trigger; hover opens the ConnectKit/Family card menu — measured, never followed. Read as `nav-developers` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 119 x 32.91; padding 11px 10px; radius 6px; background #ffffff `color.overlay.color`; text Inter 15/10 500, #282624; transition background 0.2s ease, color 0.2s ease; icon 10 x 10, #282624 |
| hover | background color(display-p3 0.984314 0.980392 0.976471); text Inter 15/10 500, color(display-p3 0.203922 0.203922 0.2); icon 10 x 10, color(display-p3 0.203922 0.203922 0.2) |
| focus-visible | outline 2px solid color(display-p3 0.517647 0.509804 0.505882), offset 1px |

![Developers menu default](components/crops/nav-developers-default.png) ![Developers menu hover](components/crops/nav-developers-hover.png) ![Developers menu focus-visible](components/crops/nav-developers-focus-visible.png) ![Developers menu pressed](components/crops/nav-developers-pressed.png)

#### Nav dropdown
The Developers dropdown panel (ConnectKit and Family cards); opened by hovering the trigger. Read as `nav-dropdown` on the home page.

**Values (default).** size 316 x 135; padding 4px; radius 8px; background #ffffff `color.overlay.color`; shadow rgba(0, 0, 0, 0.1) 0px 3px 16px 0px; text Inter 15/22 500, #121212 `text.kicker`; transition opacity 0.1s ease, transform 0.1s ease; transform matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1); icon 23 x 28, color(display-p3 0.203922 0.203922 0.2); layers ::before rgba(0, 0, 0, 0) 0px none 1.

![Nav dropdown default](components/crops/nav-dropdown-default.png)

#### Resources menu
The Resources dropdown trigger (Blog / Changelog / Help & Support / FAQs); measured, never followed. Read as `nav-resources` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 113 x 32.91; padding 11px 10px; radius 6px; background #ffffff `color.overlay.color`; text Inter 15/10 500, #282624; transition background 0.2s ease, color 0.2s ease; icon 10 x 10, #282624 |
| hover | background color(display-p3 0.984314 0.980392 0.976471); text Inter 15/10 500, color(display-p3 0.203922 0.203922 0.2); icon 10 x 10, color(display-p3 0.203922 0.203922 0.2) |
| focus-visible | outline 2px solid color(display-p3 0.517647 0.509804 0.505882), offset 1px |

![Resources menu default](components/crops/nav-resources-default.png) ![Resources menu hover](components/crops/nav-resources-hover.png) ![Resources menu focus-visible](components/crops/nav-resources-focus-visible.png) ![Resources menu pressed](components/crops/nav-resources-pressed.png)

#### X (Twitter) link
The header social link; measured, never followed. Read as `nav-twitter` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 97 x 32; padding 11px 10px; radius 6px; background #ffffff `color.overlay.color`; text Inter 15/10 500, #282624; transition background 0.2s ease, color 0.2s ease |
| hover | background color(display-p3 0.984314 0.980392 0.976471); text Inter 15/10 500, color(display-p3 0.203922 0.203922 0.2) |
| focus-visible | outline 2px solid color(display-p3 0.517647 0.509804 0.505882), offset 1px |

![X (Twitter) link default](components/crops/nav-twitter-default.png) ![X (Twitter) link hover](components/crops/nav-twitter-hover.png) ![X (Twitter) link focus-visible](components/crops/nav-twitter-focus-visible.png) ![X (Twitter) link pressed](components/crops/nav-twitter-pressed.png)

#### Log In button
The beige Log In pill in the header, inside a link to app.family.co; measured, never followed. Read as `login-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 70.47 x 32; background transparent; text Inter 15/normal 500, #121212 `text.kicker`; transition all 0.2s ease-out; layers button.Button__Container-sc-1jjqbrw-0.hACioR 70.5x32.0 #f6f4ef `action.beige` 32px |
| hover | layers button.Button__Container-sc-1jjqbrw-0.hACioR 70.5x32.0 #eae6dd 32px |

Child layers that carry the look: button 70.5x32 background #f6f4ef `action.beige` radius 32px.

![Log In button default](components/crops/login-btn-default.png) ![Log In button hover](components/crops/login-btn-hover.png) ![Log In button focus-visible](components/crops/login-btn-focus-visible.png) ![Log In button pressed](components/crops/login-btn-pressed.png)

#### Get Started button
The near-black Get Started pill; measured, never pressed (it starts the download flow). Read as `getstarted-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 109.02 x 32; padding 0px 14px; radius 32px; background #171717 `border.field-border`; text Inter 15/normal 500, #ffffff `color.overlay.color`; transition background-color 0.1s ease |
| hover, pressed | background #121212 `text.kicker` |

![Get Started button default](components/crops/getstarted-btn-default.png) ![Get Started button hover](components/crops/getstarted-btn-hover.png) ![Get Started button focus-visible](components/crops/getstarted-btn-focus-visible.png) ![Get Started button pressed](components/crops/getstarted-btn-pressed.png)

### Home

The marketing home: the display hero, the Download on iOS pill, feature sections with coloured kickers, the Watch-the-demo video overlay, the FAQ accordion, testimonial cards and the latest-posts rail.

#### Hero headline
"Your favorite crypto wallet." — the Family display face hero. Read as `hero-h1` on the home page.

**Values (default).** size 1024 x 165.59; padding 0px 0px 16px 0px; background transparent; text Family 68/74.8 500, color(display-p3 0.203922 0.203922 0.2).

![Hero headline default](components/crops/hero-h1-default.png)

#### Hero subline
The "Explore Ethereum with the best wallet for iOS" subline under the hero. Read as `hero-sub` on the home page.

**Values (default).** size 408 x 52; background transparent; text Inter 17/26 500, #474645.

![Hero subline default](components/crops/hero-sub-default.png)

#### Download CTA
The "Download on iOS" pill; measured, never followed (it goes to the App Store). Read as `download-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 209.7 x 48; padding 0px 24px 0px 22px; radius 32px; background #171717 `border.field-border`; text Inter 17/17 500, #ffffff `color.overlay.color`; transition background-color 0.1s ease; icon 16 x 20, #ffffff `color.overlay.color` |
| hover, pressed | background #121212 `text.kicker` |

![Download CTA default](components/crops/download-cta-default.png) ![Download CTA hover](components/crops/download-cta-hover.png) ![Download CTA focus-visible](components/crops/download-cta-focus-visible.png) ![Download CTA pressed](components/crops/download-cta-pressed.png)

#### Watch the Video
The "Watch the Video" action beside the download pill; measured, never pressed. Read as `watch-video` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 199.7 x 48; padding 0px 20px 0px 19px; radius 32px; background #f6f4ef `action.beige`; text Inter 17/17 500, #121212 `text.kicker`; transition background-color 0.1s ease; icon 18 x 20, #121212 `text.kicker` |
| hover, pressed | background #eae6dd |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Watch the Video default](components/crops/watch-video-default.png) ![Watch the Video hover](components/crops/watch-video-hover.png) ![Watch the Video pressed](components/crops/watch-video-pressed.png)

#### Section heading
A marketing section heading ("Explore Ethereum in a whole new way."). Read as `feature-h2` on the home page.

**Values (default).** size 1024 x 48; background transparent; text Family 44/48 500, #121212 `text.kicker`.

![Section heading default](components/crops/feature-h2-default.png)

#### Feature label
A feature label in the intro grid (Easy / Secure / Fast / Powerful / Fun). Read as `feature-label` on the home page.

**Values (default).** size 38.13 x 26; background transparent; text Inter 17/26 600, #121212 `text.kicker`.

![Feature label default](components/crops/feature-label-default.png)

#### Feature body
Feature body copy ("Whether you’re a beginner or seasoned pro, Family makes it easy."). Read as `feature-body` on the home page.

**Values (default).** size 273.06 x 44; background transparent; text Inter 15/22 400, rgba(71, 70, 69, 0.7) `text.muted`.

![Feature body default](components/crops/feature-body-default.png)

#### Watch-the-demo button
A "Watch the demo" button under a feature; opens the video overlay — measured, the press opens a local overlay only. Read as `demo-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 314.69 x 68; padding 12px 32px 12px 12px; radius 12px; background transparent; shadow color(display-p3 0.94902 0.941176 0.929412) 0px 0px 0px 0px inset; text Inter 15/22 500, #121212 `text.kicker`; transition box-shadow 0.1s ease; icon 26 x 28, color(display-p3 0.286275 0.266667 0.25098); layers button.WatchDemo__Container-sc-1kj9jjo-0.dIaiHi 314.7x68.0 color(display-p3 0.94902 0.941176 0.929412) 0px 0px 0px 0px inset 12px; div.WatchDemo__ImageContainer-sc-1kj9jjo-1.dKfigb 78.0x44.0 color(display-p3 0.94902 0.941176 0.929412) 4px; div::before.sc-gsFSXq.kakWLo 78pxx43.875px #fbfaf9 `color.beige.default` 8px |
| hover | shadow color(display-p3 0.94902 0.941176 0.929412) 0px 0px 0px 1px inset; layers button.WatchDemo__Container-sc-1kj9jjo-0.dIaiHi 314.7x68.0 color(display-p3 0.94902 0.941176 0.929412) 0px 0px 0px 1px inset 12px; div.WatchDemo__ImageContainer-sc-1kj9jjo-1.dKfigb 78.0x44.0 color(display-p3 0.94902 0.941176 0.929412) 4px; div::before.sc-gsFSXq.kakWLo 78pxx43.875px #fbfaf9 `color.beige.default` 8px |
| focus-visible | shadow color(display-p3 0.517647 0.509804 0.505882) 0px 0px 0px 2px inset; layers button.WatchDemo__Container-sc-1kj9jjo-0.dIaiHi 314.7x68.0 color(display-p3 0.517647 0.509804 0.505882) 0px 0px 0px 2px inset 12px; div.WatchDemo__ImageContainer-sc-1kj9jjo-1.dKfigb 78.0x44.0 color(display-p3 0.94902 0.941176 0.929412) 4px; div::before.sc-gsFSXq.kakWLo 78pxx43.875px #fbfaf9 `color.beige.default` 8px |
| pressed | shadow color(display-p3 0.94902 0.941176 0.929412) 0px 0px 0px 1px inset; layers button.WatchDemo__Container-sc-1kj9jjo-0.dIaiHi 314.7x68.0 color(display-p3 0.94902 0.941176 0.929412) 0px 0px 0px 1px inset 12px; div.WatchDemo__ImageContainer-sc-1kj9jjo-1.dKfigb 78.0x44.0 color(display-p3 0.94902 0.941176 0.929412) 4px; div::before.sc-gsFSXq.kakWLo 78pxx43.875px #fbfaf9 `color.beige.default` 8px |

![Watch-the-demo button default](components/crops/demo-btn-default.png) ![Watch-the-demo button hover](components/crops/demo-btn-hover.png) ![Watch-the-demo button focus-visible](components/crops/demo-btn-focus-visible.png) ![Watch-the-demo button pressed](components/crops/demo-btn-pressed.png)

#### Demo overlay
The full-viewport video overlay "Watch the demo" mounts; measured open, then closed. Read as `demo-overlay` on the home page.

**Values (default).** size 1440 x 900; padding 16px; background transparent; text Inter 16/22 500, #ffffff `color.overlay.color`; icon 14 x 14, #000000; layers div.WatchDemo__OverlayBackground-sc-1kj9jjo-4.kCuicB 1440.0x900.0 rgba(249, 247, 245, 0.8); div.WatchDemo__VideoContainer-sc-1kj9jjo-5.cgVGwv 860.0x483.8 #cccccc 12px; div.WatchDemo__IconContainer-sc-1kj9jjo-8.fnJard 860.0x483.8 rgba(0, 0, 0, 0.1).

Child layers that carry the look: div 1440x900 background rgba(249, 247, 245, 0.8); div 860x483.8 background #cccccc radius 12px; div 860x483.8 background rgba(0, 0, 0, 0.1).

![Demo overlay default](components/crops/demo-overlay-default.png)

#### Feature tag
A feature tag ("Send & Receive", "WalletConnect Enabled") beside a section. Read as `feature-h3` on the home page.

**Values (default).** size 472 x 20; background transparent; text Inter 14/20 600, color(display-p3 0.215686 0.517647 0.956863).

![Feature tag default](components/crops/feature-h3-default.png)

#### Feature section heading
A feature section heading ("Send, receive, swap. All in one place."). Read as `section-h3` on the home page.

**Values (default).** size 1024 x 96; background transparent; text Family 44/48 500, #121212 `text.kicker`.

![Feature section heading default](components/crops/section-h3-default.png)

#### FAQ item
A collapsible question/answer item in the home FAQ ("Is Family safe?"). Read as `faq-item` on the home page.

**Values (default).** size 512 x 56; padding 0px 0px 28px 0px; border B: 1px solid color(display-p3 0.94902 0.941176 0.929412); background transparent; text Inter 19/27 500, #121212 `text.kicker`; layers div.Item__StyledCollapsableItem-sc-bjycf3-2.egfBPj 512.0x56.0 B:1px solid color(display-p3 0.94902 0.941176 0.929412); div 14.0x2.0 color(display-p3 1 0.32549 0.0627451) 2px; div 2.0x14.0 color(display-p3 1 0.32549 0.0627451) 2px; a::after 132.266pxx2px #1a88f8 2px.

Child layers that carry the look: div 512x56 border 1px solid color(display-p3 0.94902 0.941176 0.929412); div 14x2 background color(display-p3 1 0.32549 0.0627451) radius 2px; div 2x14 background color(display-p3 1 0.32549 0.0627451) radius 2px.

![FAQ item default](components/crops/faq-item-default.png)

#### FAQ toggle
The 14px collapse toggle on an FAQ item; measured, never pressed. Read as `faq-toggle` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 14 x 14; padding 4px 0px; background transparent; text Inter 13.33/normal 400, color(display-p3 1 0.32549 0.0627451); layers div 14.0x2.0 color(display-p3 1 0.32549 0.0627451) 2px; div 2.0x14.0 color(display-p3 1 0.32549 0.0627451) 2px |
| focus-visible | size 14 x 16; padding 8px 0px; radius 4px; outline 2px solid color(display-p3 0.517647 0.509804 0.505882), offset 0px; layers button.Item__Toggle-sc-bjycf3-4.iIeMnL 14.0x16.0 2px solid color(display-p3 0.517647 0.509804 0.505882) offset 0px 4px; div 14.0x2.0 color(display-p3 1 0.32549 0.0627451) 2px; div 2.0x14.0 color(display-p3 1 0.32549 0.0627451) 2px |

Child layers that carry the look: div 14x2 background color(display-p3 1 0.32549 0.0627451) radius 2px; div 2x14 background color(display-p3 1 0.32549 0.0627451) radius 2px.

![FAQ toggle default](components/crops/faq-toggle-default.png) ![FAQ toggle hover](components/crops/faq-toggle-hover.png) ![FAQ toggle focus-visible](components/crops/faq-toggle-focus-visible.png) ![FAQ toggle pressed](components/crops/faq-toggle-pressed.png)

#### Tweet card
A "Friends of Family" testimonial card linking to a tweet; measured, never followed. Read as `tweet-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 540 x 204; padding 32px; radius 10px; background color(display-p3 1 1 1); shadow color(display-p3 0.94902 0.941176 0.929412) 0px 0px 0px 1px inset; text Inter 15/22 600, #474645; transition box-shadow 0.1s ease, background 0.1s ease; icon 20 x 21.11, color(display-p3 0.203922 0.203922 0.2) |
| pressed | background color(display-p3 0.984314 0.980392 0.976471); shadow color(display-p3 0.984314 0.980392 0.976471) 0px 0px 0px 0px inset |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Tweet card default](components/crops/tweet-card-default.png) ![Tweet card hover](components/crops/tweet-card-hover.png) ![Tweet card pressed](components/crops/tweet-card-pressed.png)

### App login (app.family.co)

The public Aave Account login on app.family.co: the welcome heading, the Email or Phone Number field (typed into and cleared, never submitted) and the footer links.

#### Login card
The Aave Account login card on app.family.co — the container holding the welcome text and the field; at rest, never submitted. Read as `login-card` on the app login page.

**Values (default).** size 380 x 284; background transparent; text inter 18/19 600, #222222; icon 58 x 30, #222222; layers div.styles-module-scss-module__EkH3Mq__inputContainer 380.0x48.0 #f6f7f9 `background.field` rgba(0, 0, 0, 0) 0px 0px 0px 1px inset 14px.

Child layers that carry the look: div 380x48 background #f6f7f9 `background.field` radius 14px shadow transparent 0px 0px 0px 1px inset.

![Login card default](components/crops/login-card-default.png)

#### Login title
"Welcome to Aave Account" — the login heading (Family Accounts is now Aave Account). Read as `login-h1` on the app login page.

**Values (default).** size 380 x 19; background transparent; text inter 18/19 600, #222222.

![Login title default](components/crops/login-h1-default.png)

#### Login subline
"Log in or sign up to get started. We’ll create an account if you don’t have one yet." Read as `login-sub` on the app login page.

**Values (default).** size 380 x 19; background transparent; text inter 16/19 400, rgba(23, 23, 23, 0.5).

![Login subline default](components/crops/login-sub-default.png)

#### Email/phone field
The "Email or Phone Number" login field; typed into then cleared, never submitted. Read as `login-field` on the app login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 380 x 48; padding 15px 16.96px; background transparent; text inter 16/18 500, #171717 `border.field-border`; transition opacity 0.3s ease; placeholder rgba(23, 23, 23, 0.2) |

![Email/phone field default](components/crops/login-field-default.png) ![Email/phone field focused](components/crops/login-field-focused.png) ![Email/phone field filled](components/crops/login-field-filled.png)

#### Learn More link
The "Learn More" link under the rebrand note; measured, never followed. Read as `login-learn` on the app login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 135.44 x 32; padding 7px 16px 7px 16.736px; radius 18px; background color(display-p3 0.9765 0.9686 0.9608); text inter 14/normal 500, color(display-p3 0.0706 0.0706 0.0706); transition background 0.2s ease; icon 18 x 18, color(display-p3 0.0706 0.0706 0.0706) |
| hover | background #f5f2ef |
| focus-visible | outline 2px solid rgba(0, 122, 255, 0.5) `color.focus.color`, offset 1px |
| pressed | background #f5f2ef |

![Learn More link default](components/crops/login-learn-default.png) ![Learn More link hover](components/crops/login-learn-hover.png) ![Learn More link focus-visible](components/crops/login-learn-focus-visible.png) ![Learn More link pressed](components/crops/login-learn-pressed.png)

#### Login footer link
A footer link on the login page (Developers / Privacy / Terms); measured, never followed. Read as `login-footer-link` on the app login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 69.7 x 16; background transparent; text inter 13/normal 400, rgba(23, 23, 23, 0.5); transition color 0.1s ease |
| hover | text inter 13/normal 400, #111111 |
| focus-visible | outline 2px solid rgba(0, 122, 255, 0.5) `color.focus.color`, offset 1px; layers a 69.7x16.0 2px solid rgba(0, 122, 255, 0.5) offset 1px |
| pressed | text inter 13/normal 400, #111111 |

![Login footer link default](components/crops/login-footer-link-default.png) ![Login footer link hover](components/crops/login-footer-link-hover.png) ![Login footer link focus-visible](components/crops/login-footer-link-focus-visible.png) ![Login footer link pressed](components/crops/login-footer-link-pressed.png)

### Blog

The /blog index — topic filters and post cards — and one article page.

#### Post card
A post card on /blog; measured, never followed. Read as `blog-card` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1024 x 280; padding 96px 0px 72px 0px; border B: 1px solid color(display-p3 0.94902 0.941176 0.929412); background transparent; text Inter 15/22 400, color(display-p3 0.517647 0.509804 0.505882); transition opacity 0.1s ease; layers a 1024.0x280.0 B:1px solid color(display-p3 0.94902 0.941176 0.929412); span.dot 0.0x0.0 color(display-p3 0.517647 0.509804 0.505882) 50% |
| hover | opacity 0.75 |
| focus-visible | radius 8px; outline 2px solid color(display-p3 0.517647 0.509804 0.505882), offset 1px; transition none; layers a 1024.0x280.0 B:1px solid color(display-p3 0.94902 0.941176 0.929412) 2px solid color(display-p3 0.517647 0.509804 0.505882) offset 1px 8px; span.dot 0.0x0.0 color(display-p3 0.517647 0.509804 0.505882) 50% |
| pressed | opacity 0.75 |

Child layers that carry the look: a 1024x280 border 1px solid color(display-p3 0.94902 0.941176 0.929412); span 0x0 background color(display-p3 0.517647 0.509804 0.505882) radius 50%.

![Post card default](components/crops/blog-card-default.png) ![Post card hover](components/crops/blog-card-hover.png) ![Post card focus-visible](components/crops/blog-card-focus-visible.png) ![Post card pressed](components/crops/blog-card-pressed.png)

#### Blog title
The "Blog" page title. Read as `blog-h1` on the blog page.

**Values (default).** size 88.63 x 48; background transparent; text Family 44/48 500, #121212 `text.kicker`.

![Blog title default](components/crops/blog-h1-default.png)

#### Blog filter
A topic filter button (All / News / Wallet); "opened" is its selected state — a local filter toggle, never a submission. Read as `blog-filter` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, opened) | size 43 x 33.38; padding 7.2px 12px; radius 32px; background color(display-p3 0.917647 0.917647 0.917647); text Inter 15/normal 500, color(display-p3 0.203922 0.203922 0.2); transition transform 0.2s ease, color 0.2s ease, background 0.2s ease |
| focus-visible | outline 2px solid color(display-p3 0.517647 0.509804 0.505882), offset 0px; transition none |
| pressed | transition transform 0.1s ease, color 0.1s ease, background 0.1s ease |

![Blog filter default](components/crops/blog-filter-default.png) ![Blog filter hover](components/crops/blog-filter-hover.png) ![Blog filter focus-visible](components/crops/blog-filter-focus-visible.png) ![Blog filter pressed](components/crops/blog-filter-pressed.png) ![Blog filter opened](components/crops/blog-filter-opened.png)

#### Post date line
The post date/tag meta line on a post card ("13 May, 2025  News, Wallet"). Read as `blog-date` on the blog page.

**Values (default).** size 160 x 111; background transparent; text Inter 15/22 400, color(display-p3 0.517647 0.509804 0.505882); layers span.dot 0.0x0.0 color(display-p3 0.517647 0.509804 0.505882) 50%.

Child layers that carry the look: span 0x0 background color(display-p3 0.517647 0.509804 0.505882) radius 50%.

![Post date line default](components/crops/blog-date-default.png)

#### Article title
The blog article title ("The Crypto Wallet Problem – Why We Created Family Accounts"). Read as `post-h1` on the blog post page.

**Values (default).** size 732 x 96; background transparent; text Family 44/48 500, #121212 `text.kicker`.

![Article title default](components/crops/post-h1-default.png)

#### Article subheading
An H2 subheading inside the article. Read as `post-h2` on the blog post page.

**Values (default).** size 732 x 27; background transparent; text Inter 19/27 500, #121212 `text.kicker`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Article body
Article body copy. Read as `post-body` on the blog post page.

**Values (default).** size 732 x 162; padding 0px 0px 32px 0px; background transparent; text Inter 17/26 400, #474645.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Back link
The article’s back/index link if present; measured, never followed. Read as `post-back` on the blog post page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 149.76 x 38.4; padding 9px 12px; radius 6px; background transparent; text Inter 15/22 500, color(display-p3 0.203922 0.203922 0.2); transition all 0.2s ease-out |
| focus-visible | outline 2px solid color(display-p3 0.517647 0.509804 0.505882), offset 1px; layers a.active 149.8x38.4 2px solid color(display-p3 0.517647 0.509804 0.505882) offset 1px 6px |

![Back link hover](components/crops/post-back-hover.png) ![Back link focus-visible](components/crops/post-back-focus-visible.png)

### Changelog

The /changelog page: filter buttons and dated entry bodies.

#### Changelog title
The "Changelog" page title. Read as `cl-h1` on the changelog page.

**Values (default).** size 222.91 x 48; background transparent; text Family 44/48 500, #121212 `text.kicker`.

![Changelog title default](components/crops/cl-h1-default.png)

#### Changelog filter
A filter button on /changelog (All / ConnectKit); measured, never pressed. Read as `cl-filter` on the changelog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 43 x 33.38; padding 7.2px 12px; radius 32px; background color(display-p3 0.917647 0.917647 0.917647); text Inter 15/normal 500, color(display-p3 0.203922 0.203922 0.2); transition transform 0.2s ease, color 0.2s ease, background 0.2s ease |
| focus-visible | outline 2px solid color(display-p3 0.517647 0.509804 0.505882), offset 0px; transition none |
| pressed | transition transform 0.1s ease, color 0.1s ease, background 0.1s ease |

![Changelog filter default](components/crops/cl-filter-default.png) ![Changelog filter hover](components/crops/cl-filter-hover.png) ![Changelog filter focus-visible](components/crops/cl-filter-focus-visible.png) ![Changelog filter pressed](components/crops/cl-filter-pressed.png)

#### Entry heading
A changelog entry heading ("Updated"). Read as `cl-entry` on the changelog page.

**Values (default).** size 732 x 34; padding 0px 0px 8px 0px; background transparent; text Inter 17/26 600, #121212 `text.kicker`.

![Entry heading default](components/crops/cl-entry-default.png)

#### Entry body
Changelog entry copy. Read as `cl-entry-body` on the changelog page.

**Values (default).** size 732 x 84; padding 0px 0px 32px 0px; background transparent; text Inter 17/26 400, #474645.

![Entry body default](components/crops/cl-entry-body-default.png)

### Help and support

The /support index — the search field (typed into and cleared, never submitted), help categories and article links — plus one article and the /faqs accordion.

#### Support title
The "Help & Support" page title. Read as `sup-h1` on the support page.

**Values (default).** size 300.11 x 48; background transparent; text Family 44/48 500, #121212 `text.kicker`.

![Support title default](components/crops/sup-h1-default.png)

#### Support search
The "Search Help & Support" field; typed into then cleared, never submitted. Read as `sup-search` on the support page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 269 x 36; padding 10px 15px 9px 34px; background transparent; text Inter 14/normal 500, #373737; placeholder rgba(55, 55, 55, 0.3) |

![Support search default](components/crops/sup-search-default.png) ![Support search focused](components/crops/sup-search-focused.png) ![Support search filled](components/crops/sup-search-filled.png)

#### Category button
A help-category button ("Ethereum 101", "Getting Started with Family"); measured, never followed. Read as `sup-category` on the support page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 240 x 29.92; padding 10px 0px; radius 8px; background transparent; text Inter 14/22 400, #848281 `color.body.muted`; transition all 0.08s ease-out |
| hover, pressed | text Inter 14/22 500, #4e5360; transition all 0.18s ease-out |

![Category button default](components/crops/sup-category-default.png) ![Category button hover](components/crops/sup-category-hover.png) ![Category button focus-visible](components/crops/sup-category-focus-visible.png) ![Category button pressed](components/crops/sup-category-pressed.png)

#### Article link
A help-article link; measured, never followed. Read as `sup-article-link` on the support page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 224 x 29.92; padding 10px 0px; radius 8px; background transparent; text Inter 14/22 400, #848281 `color.body.muted`; transition all 0.08s ease-out |
| focus-visible | text Inter 14/22 500, #4e5360; transition all 0.18s ease-out |
| pressed | text Inter 14/22 500, #121212 `text.kicker` |

![Article link default](components/crops/sup-article-link-default.png) ![Article link hover](components/crops/sup-article-link-hover.png) ![Article link focus-visible](components/crops/sup-article-link-focus-visible.png) ![Article link pressed](components/crops/sup-article-link-pressed.png)

#### Article title
The help-article title ("Import a wallet from MetaMask"). Read as `art-h1` on the support article page.

**Values (default).** size 620.86 x 48; background transparent; text Family 44/48 500, #121212 `text.kicker`.

![Article title default](components/crops/art-h1-default.png)

#### Article heading
A "How to" section heading inside the help article. Read as `art-h2` on the support article page.

**Values (default).** size 704 x 27; background transparent; text Inter 19/27 500, #121212 `text.kicker`.

![Article heading default](components/crops/art-h2-default.png)

#### Article body
Help-article body copy. Read as `art-body` on the support article page.

**Values (default).** size 704 x 136; padding 0px 0px 32px 0px; background transparent; text Inter 17/26 400, #474645.

![Article body default](components/crops/art-body-default.png)

#### Side-nav link
A related-category/article link beside the article; measured, never followed. Read as `art-side-link` on the support article page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 224 x 29.92; padding 10px 0px; radius 8px; background transparent; text Inter 14/22 400, #848281 `color.body.muted`; transition all 0.08s ease-out |
| focus-visible | text Inter 14/22 500, #4e5360; transition all 0.18s ease-out |
| pressed | text Inter 14/22 500, #121212 `text.kicker` |

![Side-nav link default](components/crops/art-side-link-default.png) ![Side-nav link hover](components/crops/art-side-link-hover.png) ![Side-nav link focus-visible](components/crops/art-side-link-focus-visible.png) ![Side-nav link pressed](components/crops/art-side-link-pressed.png)

#### FAQs title
The "FAQs" page title. Read as `faq-h1` on the FAQs page.

**Values (default).** size 104.63 x 48; background transparent; text Family 44/48 500, #121212 `text.kicker`.

![FAQs title default](components/crops/faq-h1-default.png)

### Docs pages

The public docs: /docs, /docs/connectkit and /docs/family-account.

#### Legal title
The "Legal" page title. Read as `legal-h1` on the legal page.

**Values (default).** size 109.28 x 48; background transparent; text Family 44/48 500, #121212 `text.kicker`.

![Legal title default](components/crops/legal-h1-default.png)

#### Legal section
A legal section link (Family App / Sweepstakes / privacy / terms); measured, never followed. Read as `legal-section` on the legal page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 212 x 30.59; padding 4.8px 0px; background transparent; text Inter 14/20 400, #018dff; transition all 0.2s ease-out |
| hover, pressed | opacity 0.75 |

![Legal section default](components/crops/legal-section-default.png) ![Legal section hover](components/crops/legal-section-hover.png) ![Legal section focus-visible](components/crops/legal-section-focus-visible.png) ![Legal section pressed](components/crops/legal-section-pressed.png)

#### Docs title
The "Getting Started" docs title. Read as `docs-h1` on the docs page.

**Values (default).** size 710 x 22.67; background transparent; text Inter 32/28.64 600, #343433 `color.marketing.primary`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1.

![Docs title default](components/crops/docs-h1-default.png)

#### Docs body
Docs body copy. Read as `docs-body` on the docs page.

**Values (default).** size 212.19 x 19.2; background transparent; text Inter 14/20 400, #848281 `color.body.muted`.

![Docs body default](components/crops/docs-body-default.png)

#### ConnectKit title
The "ConnectKit 1.9.1" docs title. Read as `ck-h1` on the ConnectKit docs page.

**Values (default).** size 710 x 24.5; background transparent; text Inter 32/40 600, #343433 `color.marketing.primary`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1; span.Tag__Container-sc-1f7fvlr-0.jUrfYZ 41.8x24.0 #fafafa 6px.

Child layers that carry the look: span 41.8x24 background #fafafa radius 6px.

![ConnectKit title default](components/crops/ck-h1-default.png)

#### Docs heading
A section heading on the ConnectKit doc page. Read as `ck-h2` on the ConnectKit docs page.

**Values (default).** size 710 x 14.17; background transparent; text Inter 20/22.67 500, #343433 `color.marketing.primary`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1.

![Docs heading default](components/crops/ck-h2-default.png)

#### Docs CTA
A docs action button ("Stay Updated" / "Contact Us"); measured, never pressed. Read as `ck-cta` on the ConnectKit docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible, pressed) | size 116 x 32; background transparent; text Inter 14/22 500, #ffffff `color.overlay.color`; transition all 0.2s ease-out; layers button.sc-dAlyuH.DTESE 116.0x32.0 #343433 `color.marketing.primary` rgba(0, 0, 0, 0) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 6px |
| hover | layers button.sc-dAlyuH.DTESE 116.0x32.0 #171717 `border.field-border` rgba(0, 0, 0, 0) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 6px |

Child layers that carry the look: button 116x32 background #343433 `color.marketing.primary` radius 6px shadow transparent 0px 0px 0px 1px inset, transparent 0px 0px 0px 0px.

![Docs CTA default](components/crops/ck-cta-default.png) ![Docs CTA hover](components/crops/ck-cta-hover.png) ![Docs CTA focus-visible](components/crops/ck-cta-focus-visible.png) ![Docs CTA pressed](components/crops/ck-cta-pressed.png)

#### Family doc title
The "Family" docs title (the Family account doc). Read as `acct-h1` on the Family docs page.

**Values (default).** size 710 x 24.5; background transparent; text Inter 32/40 600, #343433 `color.marketing.primary`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1.

![Family doc title default](components/crops/acct-h1-default.png)

### Mobile (390 wide)

The phone surface at 390 wide: the mobile header with the drawer button, the hero and the FAQ.

#### Mobile header
The phone top bar: wordmark, menu button and the Get Started pill. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 342 x 70; background transparent; text Inter 15/normal 500, #ffffff `color.overlay.color`; transform matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1); icon 72 x 18, #262626; layers a 0.0x0.0 #ffffff `color.overlay.color` 6px; div.Nav__DropdownContainer-sc-141m4ur-3.jmGeWm 0.0x0.0 #ffffff `color.overlay.color` rgba(0, 0, 0, 0.1) 0px 3px 16px 0px 8px; div.Nav__IconContainer-sc-141m4ur-2.jhkKsN 0.0x0.0 #ffffff `color.overlay.color` rgba(0, 0, 0, 0.04) 0px 0px 0px 1px 9.6px; div.Nav__IconContainer-sc-141m4ur-2.jhkKsN 0.0x0.0 #ffffff `color.overlay.color` rgba(0, 0, 0, 0.04) 0px .

Child layers that carry the look: a 0x0 background #ffffff `color.overlay.color` radius 6px; div 0x0 background #ffffff `color.overlay.color` radius 8px shadow rgba(0, 0, 0, 0.1) 0px 3px 16px 0px; div 0x0 background #ffffff `color.overlay.color` radius 9.6px shadow rgba(0, 0, 0, 0.04) 0px 0px 0px 1px.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile menu button
The hamburger that opens the mobile nav drawer; measured, its press is a local toggle. Read as `m-menu` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 32 x 32; radius 8px; background #ffffff `color.overlay.color`; text Inter 13.33/normal 400, #000000 |

![Mobile menu button default](components/crops/m-menu-default.png) ![Mobile menu button hover](components/crops/m-menu-hover.png) ![Mobile menu button focus-visible](components/crops/m-menu-focus-visible.png) ![Mobile menu button pressed](components/crops/m-menu-pressed.png)

#### Mobile headline
The phone hero heading. Read as `m-h1` on the home page at 390 wide.

**Values (default).** size 342 x 112; padding 0px 0px 16px 0px; background transparent; text Family 44/48 500, color(display-p3 0.203922 0.203922 0.2).

![Mobile headline default](components/crops/m-h1-default.png)

#### Mobile download CTA
The "Download on iOS" pill on the phone hero; measured, never followed. Read as `m-download` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focus-visible) | size 209.7 x 48; padding 0px 24px 0px 22px; radius 32px; background #171717 `border.field-border`; text Inter 17/17 500, #ffffff `color.overlay.color`; transition background-color 0.1s ease; icon 16 x 20, #ffffff `color.overlay.color` |
| hover, pressed | background #121212 `text.kicker` |

![Mobile download CTA default](components/crops/m-download-default.png) ![Mobile download CTA hover](components/crops/m-download-hover.png) ![Mobile download CTA focus-visible](components/crops/m-download-focus-visible.png) ![Mobile download CTA pressed](components/crops/m-download-pressed.png)

#### Mobile FAQ item
A collapsible FAQ item at 390 wide. Read as `m-faq-item` on the home page at 390 wide.

**Values (default).** size 342 x 56; padding 0px 0px 28px 0px; border B: 1px solid color(display-p3 0.94902 0.941176 0.929412); background transparent; text Inter 19/27 500, #121212 `text.kicker`; layers div.Item__StyledCollapsableItem-sc-bjycf3-2.egfBPj 342.0x56.0 B:1px solid color(display-p3 0.94902 0.941176 0.929412); div 14.0x2.0 color(display-p3 1 0.32549 0.0627451) 2px; div 2.0x14.0 color(display-p3 1 0.32549 0.0627451) 2px; a::after 132.266pxx2px #1a88f8 2px.

Child layers that carry the look: div 342x56 border 1px solid color(display-p3 0.94902 0.941176 0.929412); div 14x2 background color(display-p3 1 0.32549 0.0627451) radius 2px; div 2x14 background color(display-p3 1 0.32549 0.0627451) radius 2px.

![Mobile FAQ item default](components/crops/m-faq-item-default.png)

#### Mobile footer
The phone footer. Read as `m-footer` on the home page at 390 wide.

**Values (default).** size 342 x 504.88; padding 24px 0px 48px 0px; background transparent; text Inter 13/18 500, #121212 `text.kicker`; icon 16 x 16, #e4e4e4.

![Mobile footer default](components/crops/m-footer-default.png)

### Footer

The sitemap footer on the long-scroll surfaces.

#### Site footer
The sitemap footer (Developers / Resources / Company, © 2026). Read as `site-footer` on the home page.

**Values (default).** size 1024 x 316; padding 68px 0px 96px 0px; background transparent; text Inter 13/18 500, #121212 `text.kicker`; icon 60 x 62, color(display-p3 0.517647 0.509804 0.505882).

![Site footer default](components/crops/site-footer-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Family wordmark, the dropdown chevrons, feature illustrations, phone mockups) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product and the iOS app

Family is a crypto wallet: the marketing site presents the iOS app (send, receive, swap, NFTs, watched wallets, mission control), and app.family.co hosts Aave Account — the login surface says Family Accounts is now Aave Account. Logging in, the authenticated account surfaces and the iOS app itself were never reached. What is genuinely public signed out: the marketing home and its local states, /blog + articles, /changelog, /support + articles, /faqs, /legal, the three docs pages and the login card. The login and support-search fields were typed into and cleared, never submitted — what either would do next is unverified.

### Pages

- **Log In, Get Started and Download on iOS** route to the app, the App Store and the download flow — all measured, never followed.
- **Watch links** (Watch the Video, Watch, Watch the demo) open local video overlays; the demo overlay was opened, measured and closed. The video files themselves were never downloaded into the package.
- **Legal pages** (Privacy Policy, Terms of Service, the sweepstakes rules) are linked from /legal; the index was captured, each document is a long page of the same prose type.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.
- **The loading bar** — the `_app__LoadingBar` indeterminate bar — flashes on navigation and was never captured still.

### Themes

Every public surface paints the light theme signed out — the marketing sheet declares no theme switch, but the app's CSS chunks declare a real `[data-theme="dark"]` theme (38 switching variables) that the login never paints publicly, so tokens.json keeps light and dark sets: the dark values are declared evidence, not a painted surface.

### Fonts

- The **marketing stack** (system sans via `--font`) carries the public site; **Inter** carries the app login (`--font-primary`). The declared stacks **SF Pro Rounded / Nunito** (`--font-secondary`) and **SF Mono** (`--font-code`) are recorded from the app's declarations; the style guide falls back to system fonts.

### Screenshots

- Full-page shots are stitched from chunks capped at 8 chunks each.
- Marketing copy, feature names and the published blog/support text are the product's content; screenshots are 256-colour PNGs, read exact colours from the tokens or the raw files.

### Content left out

- Feature illustrations, phone mockups and video content are the product's artwork; only frames and components were measured.
