# Editor X / Wix Studio components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from editorx.com on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. editorx.com is now a redirect shell: every path 301s to wix.com/studio except /pricing, which still serves a Wix page on the domain itself — it answered with the 'Couldn't load Premium plans' error pane at capture time, so the plan components come from wix.com/studio/plans. Nothing was signed into, created, submitted or paid for; the Log In / Start Creating actions were measured, never followed, and no editor surface was reached.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (49 components, 115 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (113 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every captured surface paints `light`. Desktop shots are 1440 x 900 at 1x; desktop `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide — mobile viewport and `-full` shots alike are 390 CSS px at 2x. Each shot's `.capture.json` sidecar in screenshots/ records its real scale.

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/ (editorx.com → wix.com/studio)` | [default](screenshots/home-light-default.png), [end](screenshots/home-light-end.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png), [mid](screenshots/home-light-mid.png) |
| Features | `/features → wix.com/studio/features` | [default](screenshots/features-light-default.png), [full](screenshots/features-light-full.png) |
| Design | `wix.com/studio/design` | [default](screenshots/design-light-default.png), [full](screenshots/design-light-full.png) |
| Plans | `wix.com/studio/plans` | [default](screenshots/plans-light-default.png), [full](screenshots/plans-light-full.png) |
| Pricing (error pane at capture) | `/pricing on editorx.com` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Inspiration | `/inspiration → wix.com/studio/inspiration` | [default](screenshots/inspiration-light-default.png), [full](screenshots/inspiration-light-full.png) |
| Templates | `wix.com/studio/templates` | [default](screenshots/templates-light-default.png), [full](screenshots/templates-light-full.png) |
| Academy | `/academy → wix.com/studio/academy` | [default](screenshots/academy-light-default.png), [full](screenshots/academy-light-full.png) |
| Enterprise | `/enterprise → wix.com/studio/enterprise` | [default](screenshots/enterprise-light-default.png), [full](screenshots/enterprise-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Plans, phone | `wix.com/studio/plans` | [default](screenshots/mobile-plans-light-default.png), [full](screenshots/mobile-plans-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu overlay | home, phone width | the header menu button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open), [m-nav-item](#mobile-nav-item) |
| Product mega-menu | every desktop page | the Product trigger's own click | [home-light-menu](screenshots/home-light-menu.png), [nav-dropdown](#nav-dropdown), [menu-link](#menu-link) |
| FAQ expander | home | an FAQ question's own toggle | [faq-question](#faq-question) opened state |
| Cookie consent banner | every page | hidden, never answered (consent buttons were never clicked) | hidden before every shot and reading |
| The Studio editor and every signed-in surface | studio editor, dashboards, checkout | behind Log In / Start Creating; measured, never followed | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 20 components were given a real keyboard focus. 3 draw an outline ring: `academy-card` (on a child: 2px solid rgb(17, 109, 255) offset 1px), `pricing-refresh` (3px solid #116dff `color.brand.link`, offset 1px), `pricing-support` (1px auto #005fcc `measured.focus-ring-auto`, offset 1px). 15 draw a focus ring as a shadow instead: `nav-trigger`, `nav-link`, `nav-lang`, `nav-login`, `menu-link`, `hero-cta`, `section-link`, `faq-question`, `feat-link`, `inspo-card`, `inspo-filter`, `ent-cta`, `footer-link`, `social-icon`, `m-nav-item`. The other 2 show no measured change: `nav-cta`, `design-cta`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `linear` | background-color, border-color, color | pricing-refresh |
| 0.2s | `ease` | all | ent-cta, feat-link, inspo-filter, section-link |
| 0.3s | `linear` | transform | m-header |
| 0.4s | `ease` | background-color, border-color, color | design-cta, hero-cta, nav-cta, nav-lang |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card](#plan-card) | 202.02 x 574 | T: 3px solid #0e106a `color.neutral.navy`; R: 1px solid #dfe5eb `color.neutral.card-line`; B: 1px solid #dfe5eb `color.neutral.card-line`; L: 1px solid #dfe5eb `color.neutral.card-line` | - | #ffffff `color.neutral.white` | none | 0 |
| [Template card](#template-card) | 297.75 x 394.8 | - | 2px | #ffffff `color.neutral.white` | none | 12px 12px 26px 12px |
| [Feature card](#feature-card) | 312 x 116.75 | - | - | transparent | none | 0 |
| [Inspiration card](#inspiration-card) | 633.77 x 432.34 | - | - | rgba(255, 255, 255, 0) | none | 0 |
| [Academy card](#academy-card) | 673.13 x 631.38 | - | - | transparent | none | 0 |

## Components

### Shell and navigation

The fixed header shared by every page: the Wix Studio wordmark, the Product / Resources / Enterprise dropdown triggers, the Pricing link, the language globe, Log In and the purple Start Creating. Product opens a full-width mega-menu.

#### Nav bar
The fixed top bar (57px): the Wix Studio wordmark, the Product / Resources / Enterprise dropdown triggers, Pricing, the language selector, Log In and the black Start Creating button. Read as `nav-bar` on the home page.

**Values (default).** size 989.06 x 56; background transparent; text Madefor-Display 16/normal 400, #000000 `color.neutral.ink`; icon 20 x 20, #000000 `color.neutral.ink`; layers span.ErVudj 62.5x56.0 B:4px solid rgba(0, 0, 0, 0); div.aD6GhG 1440.0x0.0 rgb(255, 255, 255); div.U79u0Z.zEDyqc 1440.0x588.0; ul.D_XV1R 1267.2x357.0 T:1px solid rgb(216, 226, 236); div.CGPrIB 0.0x0.0; div.omadZW.xYoOe1 0.0x0.0 50%.

Child layers that carry the look: span 62.5x56 border 4px solid transparent; div 1440x0 background #ffffff `color.neutral.white`; div 1440x588 image linear-gradient(rgba(245, 245, 245, 0.74), #e2efff).

![Nav bar default](components/crops/nav-bar-default.png)

#### Logo
The Wix Studio wordmark anchor. Read as `logo` on the home page.

**Wrong element.** The `nav a` fallback in the selector matched first, so these are the "Pricing" nav link's values, not the Wix Studio wordmark's. The selector is fixed in tools/capture/public/measure.mjs; the entry needs a recapture.

**Values (default).** size 83.95 x 56; padding 0px 15px; background transparent; text Madefor-Display 16/normal 400, #000000 `color.neutral.ink`; layers ::after rgba(0, 0, 0, 0) 0px none 1.

![Logo default](components/crops/logo-default.png)

#### Nav trigger
The Product button that opens the nav dropdown; toggled, never followed. Read as `nav-trigger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 117.53 x 56; padding 0px 15px; background transparent; text Madefor-Display 16/normal 400, #000000 `color.neutral.ink`; icon 20 x 20, #000000 `color.neutral.ink`; layers span.ErVudj 62.5x56.0 B:4px solid rgba(0, 0, 0, 0) |
| hover | text Madefor-Display-Bold 16/normal 700, #000000 `color.neutral.ink`; layers span.ErVudj 62.5x56.0 B:4px solid rgb(0, 0, 0) |
| focus-visible | shadow #000000 0px 0px 0px 1px, #000000 0px 0px 0px 3px; layers button.Q3cjxA 117.5x56.0 rgb(0, 0, 0) 0px 0px 0px 1px, rgb(0, 0, 0) 0px 0px 0px 3px; span.ErVudj 62.5x56.0 B:4px solid rgba(0, 0, 0, 0) |
| pressed | text Madefor-Display-Bold 16/normal 700, #000000 `color.neutral.ink` |

Child layers that carry the look: span 62.5x56 border 4px solid transparent.

![Nav trigger default](components/crops/nav-trigger-default.png) ![Nav trigger hover](components/crops/nav-trigger-hover.png) ![Nav trigger focus-visible](components/crops/nav-trigger-focus-visible.png) ![Nav trigger pressed](components/crops/nav-trigger-pressed.png)

#### Nav link
The plain Pricing nav link; measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 83.95 x 56; padding 0px 15px; background transparent; text Madefor-Display 16/normal 400, #000000 `color.neutral.ink`; layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | text Madefor-Display-Bold 16/normal 700, #000000 `color.neutral.ink` |
| focus-visible | shadow #000000 0px 0px 0px 1px, #000000 0px 0px 0px 3px; layers ::after rgba(0, 0, 0, 0) 0px none 1; a.twLEiD 84.0x56.0 rgb(0, 0, 0) 0px 0px 0px 1px, rgb(0, 0, 0) 0px 0px 0px 3px |
| pressed | text Madefor-Display-Bold 16/normal 700, #000000 `color.neutral.ink` |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Language selector
The globe language control ("language selector, english selected"); never opened. Read as `nav-lang` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 24 x 24; background transparent; text Madefor-Display 16/normal 400, #000000 `color.neutral.ink`; transition color 0.4s ease; icon 24 x 24, #000000 `color.neutral.ink` |
| hover | text Madefor-Display-Bold 16/normal 700, #000000 `color.neutral.ink` |
| focus-visible | shadow #000000 0px 0px 0px 1px, #000000 0px 0px 0px 3px; layers button.pGUFRX 24.0x24.0 rgb(0, 0, 0) 0px 0px 0px 1px, rgb(0, 0, 0) 0px 0px 0px 3px |
| pressed | text Madefor-Display-Bold 16/normal 700, #000000 `color.neutral.ink` |

![Language selector default](components/crops/nav-lang-default.png) ![Language selector hover](components/crops/nav-lang-hover.png) ![Language selector focus-visible](components/crops/nav-lang-focus-visible.png) ![Language selector pressed](components/crops/nav-lang-pressed.png)

#### Log-in link
The Log In header action; measured, never followed (it leaves for users.wix.com). Read as `nav-login` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 46.66 x 20; background transparent; text Madefor-Display 16/normal 400, #000000 `color.neutral.ink`; layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | text Madefor-Display-Bold 16/normal 700, #000000 `color.neutral.ink` |
| focus-visible | shadow #000000 0px 0px 0px 1px, #000000 0px 0px 0px 3px; layers ::after rgba(0, 0, 0, 0) 0px none 1; a.oQY31L 46.7x20.0 rgb(0, 0, 0) 0px 0px 0px 1px, rgb(0, 0, 0) 0px 0px 0px 3px |
| pressed | text Madefor-Display-Bold 16/normal 700, #000000 `color.neutral.ink` |

![Log-in link default](components/crops/nav-login-default.png) ![Log-in link hover](components/crops/nav-login-hover.png) ![Log-in link focus-visible](components/crops/nav-login-focus-visible.png) ![Log-in link pressed](components/crops/nav-login-pressed.png)

#### Nav CTA
The black Start Creating action in the header; measured, never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 175.28 x 57; padding 0px 35px; background #3910ed `color.brand.studio-purple`; text Madefor-Text 16/57 400, #ffffff `color.neutral.white`; transition color 0.4s ease, background-color 0.4s ease |

![Nav CTA default](components/crops/nav-cta-default.png) ![Nav CTA hover](components/crops/nav-cta-hover.png) ![Nav CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Nav CTA pressed](components/crops/nav-cta-pressed.png)

#### Nav dropdown
The Product dropdown panel, opened by its own trigger. Read as `nav-dropdown` on the home page.

**Values (default).** size 1440 x 510; padding 47px 72px 66px 100.797px; background transparent; text Madefor-Display 16/normal 400, #000000 `color.neutral.ink`; layers ul.D_XV1R 1267.2x357.0 T:1px solid rgb(216, 226, 236).

Child layers that carry the look: ul 1267.2x357 border 1px solid #d8e2ec `color.neutral.hairline`.

![Nav dropdown default](components/crops/nav-dropdown-default.png)

#### Menu link
A link inside the opened Product mega-menu. Read as `menu-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 81.03 x 23; background transparent; text Madefor-Display-Bold 18/normal 700, #000000 `color.neutral.ink` |
| hover | text Madefor-Display-Bold 18/normal 700, #3910ed `color.brand.studio-purple` |
| focus-visible, pressed | shadow #000000 0px 0px 0px 1px, #000000 0px 0px 0px 3px; text Madefor-Display-Bold 18/normal 700, #3910ed `color.brand.studio-purple`; layers a.eXGFEo 81.0x23.0 rgb(0, 0, 0) 0px 0px 0px 1px, rgb(0, 0, 0) 0px 0px 0px 3px |

![Menu link default](components/crops/menu-link-default.png) ![Menu link hover](components/crops/menu-link-hover.png) ![Menu link focus-visible](components/crops/menu-link-focus-visible.png) ![Menu link pressed](components/crops/menu-link-pressed.png)

### Home

The home hero ('Design with impact / Deliver at scale' in the 80px display face) with the purple 'Start creating' stadium pill, the editor screenshot, the scroll-jacked 'Site of the week' showcase, the FAQ repeater and the lime closing band.

#### Hero headline
The "Design with impact / Deliver at scale" display headline, madefor-display. Read as `hero-title` on the home page.

**Values (default).** size 869.25 x 176.53; background transparent; text wix-madefor-display-v2 80.24/88.27 400, #000000 `color.neutral.ink`.

![Hero headline default](components/crops/hero-title-default.png)

#### Hero copy
The lede under the display headline. Read as `hero-sub` on the home page.

**Values (default).** size 586.13 x 23; background transparent; text wix-madefor-text-v2 18/28.8 400, #000000 `color.neutral.ink`.

![Hero copy default](components/crops/hero-sub-default.png)

#### Hero CTA
The purple "Start creating" pill under the hero copy (the header CTA shares the label, so the header is excluded); measured, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 221.25 x 56.23; radius 1123.88px; background rgba(255, 255, 255, 0); text wix-madefor-text-v2 23.25/32.54 400, #ffffff `color.neutral.white`; transition border-color 0.4s ease, background-color 0.4s ease; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | background rgba(57, 16, 237, 0) |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #116dff 0px 0px 0px 4px |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Section heading
A feature-section heading below the hero. Read as `section-h2` on the home page.

**Values (default).** size 751.11 x 108; background transparent; text wix-madefor-display-v2 54/54 400, #000000 `color.neutral.ink`.

![Section heading default](components/crops/section-h2-default.png)

#### Section link
An inline "learn more" link inside a feature section; measured, never followed. Read as `section-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 218.47 x 32; padding 0px 22px 0px 0px; radius 50px; background transparent; text madefor-text-mediumbold 16/normal 400, #000000 `color.neutral.ink`; transition all 0.2s ease |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #116dff 0px 0px 0px 4px; layers a.StylableButton2545352419__root.StylableButton2545352419__forcedColorsBackground 218.5x32.0 rgb(255, 255, 255) 0px 0px 0px 2px, rgb(17, 109, 255) 0px 0px 0px 4px 50px |

![Section link default](components/crops/section-link-default.png) ![Section link hover](components/crops/section-link-hover.png) ![Section link focus-visible](components/crops/section-link-focus-visible.png) ![Section link pressed](components/crops/section-link-pressed.png)

#### Showcase section
The "Site of the week" scroll-jacked showcase (a pinned media scene); measured mid-scroll state may sit between animation frames. Read as `showcase-card` on the home page.

**Values (default).** size 1440 x 900; background transparent; text wix-madefor-display-v2 18/normal 400, #000000 `color.neutral.ink`; icon 17 x 17, #000000 `color.neutral.ink`; layers div.jdJeEr.NYfD3h 1440.0x900.0 rgba(69, 84, 102, 0); div.jdJeEr.NYfD3h 648.3x314.7 rgba(238, 238, 238, 0); div.jdJeEr.NYfD3h 341.3x52.0 rgba(255, 255, 255, 0); div.jdJeEr.NYfD3h 181.0x52.0 rgba(255, 255, 255, 0); a.StylableButton2545352419__root.StylableButton2545352419__forcedColorsBackground 181.0x52.0 rgb(0, 0, 0) 50px; div.jdJeEr.NYfD3h 137.8x30.0 rgba(255, 255, 255, 0).

Child layers that carry the look: div 1440x900 background rgba(69, 84, 102, 0); div 648.3x314.7 background rgba(238, 238, 238, 0); div 341.3x52 background rgba(255, 255, 255, 0).

![Showcase section default](components/crops/showcase-card-default.png)

#### FAQ question
A Wix Studio FAQ repeater item (question row); toggled open once for the opened state (local UI). Read as `faq-question` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 1327.66 x 131.19; background transparent; text wix-madefor-text-v2 24/31.20 500, #000000 `color.neutral.ink`; icon 20 x 20, #000000 `color.neutral.ink`; layers div.jdJeEr.NYfD3h 1327.7x131.2 rgba(220, 232, 255, 0); div.jdJeEr.NYfD3h 1327.7x1.0 rgb(0, 0, 0); div.jdJeEr.NYfD3h 0.0x0.0 rgba(238, 238, 238, 0) |
| focus-visible | layers div.jdJeEr.NYfD3h 1327.7x131.2 rgba(220, 232, 255, 0); button.StylableButton2545352419__root.StylableButton2545352419__forcedColorsBackground 1327.6x131.2 rgb(255, 255, 255) 0px 0px 0px 2px, rgb(17, 109, 255) 0px 0px 0px 4px 3px; div.jdJeEr.NYfD3h 1327.7x1.0 rgb(0, 0, 0); div.jdJeEr.NYfD3h 0.0x0.0 rgba(238, 238, 238, 0) |
| opened | size 1327.66 x 442.33; layers div.jdJeEr.NYfD3h 1327.7x442.3 rgba(220, 232, 255, 0); button.StylableButton2545352419__root.StylableButton2545352419__forcedColorsBackground 1327.6x131.2 rgb(255, 255, 255) 0px 0px 0px 2px, rgb(17, 109, 255) 0px 0px 0px 4px 3px; div.jdJeEr.NYfD3h 1327.7x1.0 rgb(0, 0, 0); div.jdJeEr.NYfD3h 1327.7x311.1 rgba(238, 238, 238, 0) |

Child layers that carry the look: div 1327.7x131.2 background rgba(220, 232, 255, 0); div 1327.7x1 background #000000 `color.neutral.ink`; div 0x0 background rgba(238, 238, 238, 0).

![FAQ question default](components/crops/faq-question-default.png) ![FAQ question hover](components/crops/faq-question-hover.png) ![FAQ question focus-visible](components/crops/faq-question-focus-visible.png) ![FAQ question pressed](components/crops/faq-question-pressed.png) ![FAQ question opened](components/crops/faq-question-opened.png)

#### CTA band
The closing "Unleash your creations. Rein in the chaos. / Start creating" band. Read as `cta-band` on the home page.

**Values (default).** size 1269 x 171; background #deff00 `color.brand.lime`; text Arial 10/normal 400, #000000 `color.neutral.ink`.

![CTA band default](components/crops/cta-band-default.png)

### Features and design

/studio/features and /studio/design: the 61px and 157px displays, the feature cards and inline links.

#### Features title
The features page display heading. Read as `feat-h1` on the features page.

**Values (default).** size 722.83 x 152; background transparent; text madefor-display 60.9/normal 400, #000000 `color.neutral.ink`.

![Features title default](components/crops/feat-h1-default.png)

#### Feature card
A feature card on the features index (a title over its blurb). Read as `feat-card` on the features page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 312 x 116.75; background transparent; text madefor-text-bold 18/25.2 400, #000000 `color.neutral.ink`; layers div.jdJeEr.NYfD3h 312.0x116.8 rgba(238, 238, 238, 0) |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: div 312x116.8 background rgba(238, 238, 238, 0).

![Feature card default](components/crops/feat-card-default.png) ![Feature card hover](components/crops/feat-card-hover.png) ![Feature card pressed](components/crops/feat-card-pressed.png)

#### Feature link
A "learn more" link on the features page; measured, never followed. Read as `feat-link` on the features page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 84.78 x 36; radius 50px; background transparent; text madefor-text 16/normal 400, #000000 `color.neutral.ink`; transition all 0.2s ease |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #116dff 0px 0px 0px 4px; layers a.StylableButton2545352419__root.style-lw3lh0ls1__root 84.8x36.0 rgb(255, 255, 255) 0px 0px 0px 2px, rgb(17, 109, 255) 0px 0px 0px 4px 50px |

![Feature link default](components/crops/feat-link-default.png) ![Feature link hover](components/crops/feat-link-hover.png) ![Feature link focus-visible](components/crops/feat-link-focus-visible.png) ![Feature link pressed](components/crops/feat-link-pressed.png)

#### Design title
The design-features page display heading — the page closest to Editor X's old positioning. Read as `design-h1` on the design page.

**Values (default).** size 1319.53 x 315; background transparent; text madefor-display 157.5/157.5 400, #000000 `color.neutral.ink`.

![Design title default](components/crops/design-h1-default.png)

#### Design CTA
A call-to-action on the design page; measured, never followed. Read as `design-cta` on the design page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 175.28 x 57; padding 0px 35px; background #3910ed `color.brand.studio-purple`; text Madefor-Text 16/57 400, #ffffff `color.neutral.white`; transition color 0.4s ease, background-color 0.4s ease |

![Design CTA default](components/crops/design-cta-default.png) ![Design CTA hover](components/crops/design-cta-hover.png) ![Design CTA focus-visible](components/crops/design-cta-focus-visible.png) ![Design CTA pressed](components/crops/design-cta-pressed.png)

#### Design section heading
A section heading on the design page. Read as `design-h2` on the design page.

**Values (default).** size 369 x 96; background transparent; text madefor-display 48/48 400, #000000 `color.neutral.ink`.

![Design section heading default](components/crops/design-h2-default.png)

### Plans and pricing

/studio/plans (wix.com) holds the plan cards with the navy-topped recommended card and mint RECOMMENDED badge; /pricing on editorx.com itself answered with the 'Couldn't load Premium plans' error pane at capture time — measured as such.

#### Plans title
The "Choose the right Studio plan for each project" heading. Read as `plans-h1` on the plans page.

**Values (default).** size 687.61 x 36; background transparent; text Madefor 32/36 700, #000624 `color.neutral.ink-plans`.

![Plans title default](components/crops/plans-h1-default.png)

#### Plan card
A studio plan card (name, price, action). Read as `plan-card` on the plans page.

**Values (default).** size 202.02 x 574; border T: 3px solid #0e106a `color.neutral.navy`; R: 1px solid #dfe5eb `color.neutral.card-line`; B: 1px solid #dfe5eb `color.neutral.card-line`; L: 1px solid #dfe5eb `color.neutral.card-line`; background #ffffff `color.neutral.white`; text Madefor 18/24 700, #000624 `color.neutral.ink-plans`.

![Plan card default](components/crops/plan-card-default.png)

#### Plan price
A plan card's price figure (US$ in the region the capture was served). Read as `plan-price` on the plans page.

**Values (default).** size 146.3 x 48; background transparent; text Madefor 14/18 500, #000624 `color.neutral.ink-plans`.

![Plan price default](components/crops/plan-price-default.png)

#### Plan CTA
A plan card's action; measured, never followed. Read as `plan-cta` on the plans page.

Not on the page when it was captured.

#### Pricing title (editorx.com)
The heading editorx.com/pricing serves — on this run, the "Couldn't load Premium plans due to a technical issue" error title. Read as `pricing-h1` on the pricing page.

**Values (default).** size 540 x 258; background transparent; text Madefor 18/24 700, #000624 `color.neutral.ink-plans`.

![Pricing title (editorx.com) default](components/crops/pricing-h1-default.png)

#### Recommended badge
The lime RECOMMENDED badge on the highlighted plan column. Read as `plan-badge` on the plans page.

**Values (default).** size 200 x 30; background transparent; text Madefor 10/24 700, #000624 `color.neutral.ink-plans`; layers div.wds_1_315_0_Box__root.wds_1_315_0_Box---direction-10-horizontal 200.0x30.0 rgb(166, 255, 216).

Child layers that carry the look: div 200x30 background #a6ffd8 `color.neutral.badge-mint`.

![Recommended badge default](components/crops/plan-badge-default.png)

#### Error pane (editorx.com)
The pane the premium-plans widget paints when it fails headless; honest evidence of what the domain serves. Read as `pricing-pane` on the pricing page.

**Values (default).** size 540 x 54; background transparent; text Madefor 14/18 400, #868aa5.

![Error pane (editorx.com) default](components/crops/pricing-pane-default.png)

#### Refresh link (editorx.com)
The Refresh action inside the error pane; measured, never followed. Read as `pricing-refresh` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 57.25 x 24; radius 2px; background transparent; text Madefor 16/24 400, #116dff `color.brand.link`; transition background-color 0.1s linear, color 0.1s linear, border-color 0.1s linear |
| hover | text Madefor 16/24 400, #0f62e6 `color.brand.link-hover` |
| focus-visible | outline 3px solid #116dff `color.brand.link`, offset 1px; layers ::before rgba(0, 0, 0, 0) 0px none 1; button.wds-button-core.wds_1_348_0-button-core 57.3x24.0 3px solid rgb(17, 109, 255) offset 1px 2px; button::before.wds-button-core.wds_1_348_0-button-core 57.25pxx24px 1px solid rgb(255, 255, 255) offset 0px 2px |
| pressed | text Madefor 16/24 400, #084ebd |

![Refresh link (editorx.com) default](components/crops/pricing-refresh-default.png) ![Refresh link (editorx.com) hover](components/crops/pricing-refresh-hover.png) ![Refresh link (editorx.com) focus-visible](components/crops/pricing-refresh-focus-visible.png) ![Refresh link (editorx.com) pressed](components/crops/pricing-refresh-pressed.png)

#### Support link (editorx.com)
The 'contact Customer Care.' support link inside the error pane's copy; measured, never followed. Read as `pricing-support` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 154.31 x 18; background transparent; text Madefor 14/18 400, #116dff `color.brand.link` |
| hover | text Madefor 14/18 400, #0f62e6 `color.brand.link-hover` |
| focus-visible | outline 1px auto #005fcc `measured.focus-ring-auto`, offset 1px; layers a 154.3x18.0 1px auto rgb(0, 95, 204) offset 1px |
| pressed | text Madefor 14/18 400, #0f62e6 `color.brand.link-hover` |

![Support link (editorx.com) default](components/crops/pricing-support-default.png) ![Support link (editorx.com) hover](components/crops/pricing-support-hover.png) ![Support link (editorx.com) focus-visible](components/crops/pricing-support-focus-visible.png) ![Support link (editorx.com) pressed](components/crops/pricing-support-pressed.png)

### Galleries

/studio/inspiration and /studio/templates: the site-of-the-week gallery cards, the filter chips and the white 2px-radius template cards.

#### Inspiration title
The inspiration gallery heading. Read as `inspo-h1` on the inspiration page.

**Values (default).** size 683.39 x 145.13; background transparent; text wfont_1f4e5a_a4dab464d39a4954a3f7d14cdb48d3ed 72.56/72.56 400, #000000 `color.neutral.ink`.

![Inspiration title default](components/crops/inspo-h1-default.png)

#### Inspiration card
A showcase-site card in the inspiration gallery; measured, never followed. Read as `inspo-card` on the inspiration page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 633.77 x 432.34; background rgba(255, 255, 255, 0); text madefor-text 12/19.2 400, #000000 `color.neutral.ink`; icon 9 x 9, #000000 `color.neutral.ink` |

![Inspiration card default](components/crops/inspo-card-default.png) ![Inspiration card hover](components/crops/inspo-card-hover.png) ![Inspiration card focus-visible](components/crops/inspo-card-focus-visible.png) ![Inspiration card pressed](components/crops/inspo-card-pressed.png)

#### Gallery filter
A category filter on the inspiration page; measured unselected. Read as `inspo-filter` on the inspiration page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 219.77 x 32; padding 0px 22px 0px 0px; background transparent; text wix-madefor-text-v2 20/normal 400, #ffffff `color.neutral.white`; transition all 0.2s ease |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #116dff 0px 0px 0px 4px; layers button.StylableButton2545352419__root.StylableButton2545352419__forcedColorsBackground 219.8x32.0 rgb(255, 255, 255) 0px 0px 0px 2px, rgb(17, 109, 255) 0px 0px 0px 4px |

![Gallery filter default](components/crops/inspo-filter-default.png) ![Gallery filter hover](components/crops/inspo-filter-hover.png) ![Gallery filter focus-visible](components/crops/inspo-filter-focus-visible.png) ![Gallery filter pressed](components/crops/inspo-filter-pressed.png)

#### Templates title
The studio templates page heading. Read as `templates-h1` on the templates page.

**Values (default).** size 215.48 x 17; background transparent; text Madefor 18/17 500, #000000 `color.neutral.ink`.

![Templates title default](components/crops/templates-h1-default.png)

#### Template card
A template card in the gallery; measured, never followed. Read as `template-card` on the templates page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 297.75 x 394.8; padding 12px 12px 26px 12px; radius 2px; background #ffffff `color.neutral.white`; text Madefor 16/24 530, #000000 `color.neutral.ink` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Template card default](components/crops/template-card-default.png) ![Template card hover](components/crops/template-card-hover.png) ![Template card pressed](components/crops/template-card-pressed.png)

### Academy and enterprise

/studio/academy and /studio/enterprise: the 75px and 60px displays, the academy cards and the black 50px-pill CTA.

#### Academy title
The studio academy heading. Read as `academy-h1` on the academy page.

**Values (default).** size 1222.5 x 75; background transparent; text madefor-display 75/75 400, #000000 `color.neutral.ink`.

![Academy title default](components/crops/academy-h1-default.png)

#### Academy card
A course or tutorial card on the academy page; measured, never followed. Read as `academy-card` on the academy page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 673.13 x 631.38; background transparent; text madefor-display 26.6/29.26 400, #000000 `color.neutral.ink`; icon 54.61 x 54.61, #000000 `color.neutral.ink`; layers div.jdJeEr.NYfD3h 673.1x631.4 rgb(190, 214, 255) 34px; div.jdJeEr.NYfD3h 399.6x58.5 rgba(255, 255, 255, 0); div.jdJeEr.NYfD3h 590.6x449.1 rgba(255, 255, 255, 0); div.jdJeEr.NYfD3h 133.4x34.4 rgba(255, 255, 255, 0); div.jdJeEr.NYfD3h 107.4x2.0 rgb(0, 0, 0) |
| hover | layers div.jdJeEr.NYfD3h 673.1x631.4 rgb(190, 214, 255) 34px; div.jdJeEr.NYfD3h 399.6x58.5 rgba(255, 255, 255, 0); div.jdJeEr.NYfD3h 590.6x449.1 rgba(255, 255, 255, 0); a.PoVCDy.wixui-button 590.6x449.1 rgba(57, 16, 237, 0); div.jdJeEr.NYfD3h 133.4x34.4 rgba(255, 255, 255, 0); div.jdJeEr.NYfD3h 107.4x2.0 rgb(0, 0, 0) |
| focus-visible | layers div.jdJeEr.NYfD3h 673.1x631.4 rgb(190, 214, 255) 34px; div.jdJeEr.NYfD3h 399.6x58.5 rgba(255, 255, 255, 0); div.UeoHYs 590.6x449.1 rgb(255, 255, 255) 0px 0px 0px 2px, rgb(17, 109, 255) 0px 0px 0px 4px 8px; div.UCYv5s 0.0x11.0 rgb(255, 255, 255) 0px 0px 1px 2px 2px solid rgb(17, 109, 255) offset 1px; div.jdJeEr.NYfD3h 590.6x449.1 rgba(255, 255, 255, 0); div.jdJeEr.NYfD3h 133.4x34.4 rgba(255, 255, 2 |

Child layers that carry the look: div 673.1x631.4 background #bed6ff radius 34px; div 399.6x58.5 background rgba(255, 255, 255, 0); div 590.6x449.1 background rgba(255, 255, 255, 0).

![Academy card default](components/crops/academy-card-default.png) ![Academy card hover](components/crops/academy-card-hover.png) ![Academy card focus-visible](components/crops/academy-card-focus-visible.png) ![Academy card pressed](components/crops/academy-card-pressed.png)

#### Enterprise title
The enterprise page display heading. Read as `ent-h1` on the enterprise page.

**Values (default).** size 1222.52 x 120; background transparent; text wix-madefor-display-v2 60/60 400, #000000 `color.neutral.ink`.

![Enterprise title default](components/crops/ent-h1-default.png)

#### Enterprise CTA
A Contact-sales-style action on the enterprise page; measured, never followed. Read as `ent-cta` on the enterprise page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 144.47 x 52; padding 0px 4px 0px 30px; radius 50px; background #000000 `color.neutral.ink`; text madefor-text-mediumbold 16/normal 400, #ffffff `color.neutral.white`; transition all 0.2s ease; icon 17 x 17, #000000 `color.neutral.ink` |
| hover | padding 0px 16px 0px 20px; icon 15 x 15, #000000 `color.neutral.ink` |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #116dff 0px 0px 0px 4px |
| pressed | padding 0px 16px 0px 20px; icon 15 x 15, #000000 `color.neutral.ink` |

![Enterprise CTA default](components/crops/ent-cta-default.png) ![Enterprise CTA hover](components/crops/ent-cta-hover.png) ![Enterprise CTA focus-visible](components/crops/ent-cta-focus-visible.png) ![Enterprise CTA pressed](components/crops/ent-cta-pressed.png)

### Footer

The #0e0e0e footer on every page: #f6f6f6 links dimming to #828282, the circled social buttons and the legal line.

#### Footer
The Wix Studio footer: the blurb, link columns, social icons, language and legal. Read as `footer` on the home page.

**Values (default).** size 1440 x 793; background transparent; text Madefor-Text 14/20 400, #f6f6f6 `color.neutral.footer-ink`; layers nav.tuyyeT 1440.0x793.0 rgb(14, 14, 14); div.VK8FJF 0.0x0.0 rgb(132, 130, 128); div.fbTMfh 1296.0x56.0 rgb(132, 130, 128) 0px -1px 0px 0px; button.ZXBKx_ 36.0x36.0 T:1px solid rgb(246, 246, 246) / R:1px solid rgb(246, 246, 246) / B:1px solid rgb(246, 246, 246) / L:1px solid rgb(246, 246, 246) 50%.

Child layers that carry the look: nav 1440x793 background #0e0e0e `color.neutral.surface-dark`; div 0x0 background #848280 `color.neutral.footer-divider`; div 1296x56 shadow #848280 `color.neutral.footer-divider` 0px -1px 0px 0px.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 52.22 x 34; background transparent; text Madefor-Text 16/34 400, #f6f6f6 `color.neutral.footer-ink` |
| hover | text Madefor-Text 16/34 400, #828282 `color.neutral.footer-muted` |
| focus-visible | shadow #828282 0px 0px 0px 1px, #828282 0px 0px 0px 3px; text Madefor-Text 16/34 400, #828282 `color.neutral.footer-muted`; layers a.Pllco1 52.2x34.0 rgb(130, 130, 130) 0px 0px 0px 1px, rgb(130, 130, 130) 0px 0px 0px 3px |
| pressed | text Madefor-Text 16/34 400, #828282 `color.neutral.footer-muted` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social link
A social link in the footer. Read as `social-icon` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 24 x 24; background transparent; text Arial 10/normal 400, #f6f6f6 `color.neutral.footer-ink`; icon 24 x 24, #f6f6f6 `color.neutral.footer-ink` |
| hover | text Arial 10/normal 400, #828282 `color.neutral.footer-muted`; icon 24 x 24, #828282 `color.neutral.footer-muted` |
| focus-visible | shadow #828282 0px 0px 0px 1px, #828282 0px 0px 0px 3px; text Arial 10/normal 400, #828282 `color.neutral.footer-muted`; icon 24 x 24, #828282 `color.neutral.footer-muted`; layers a.Rv9f2H 24.0x24.0 rgb(130, 130, 130) 0px 0px 0px 1px, rgb(130, 130, 130) 0px 0px 0px 3px |
| pressed | text Arial 10/normal 400, #828282 `color.neutral.footer-muted`; icon 24 x 24, #828282 `color.neutral.footer-muted` |

![Social link default](components/crops/social-icon-default.png) ![Social link hover](components/crops/social-icon-hover.png) ![Social link focus-visible](components/crops/social-icon-focus-visible.png) ![Social link pressed](components/crops/social-icon-pressed.png)

### Mobile (390 wide)

The same surface at phone width: the header shrinks to wordmark + Start Creating + burger, and the menu opens as a white full panel with 50px rows.

#### Mobile nav
The fixed mobile top bar (the wordmark, the square Start Creating and the burger menu button) — the page header is not a <nav> at phone width. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 47; padding 0px 0px 0px 20px; border B: 1px solid #d8e2ec `color.neutral.hairline`; background #ffffff `color.neutral.white`; text Madefor-Display 14/normal 400, #ffffff `color.neutral.white`; transition transform 0.3s linear.

![Mobile nav default](components/crops/m-header-default.png)

#### Menu button
The burger/menu toggle in the mobile nav. Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 50 x 46; background transparent; text Arial 13.33/normal 400, #000000 `color.neutral.ink`; icon 50 x 46, #000000 `color.neutral.ink`.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The opened mobile navigation panel. Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 797; background #ffffff `color.neutral.white`; text Madefor-Display 16/normal 400, #000000 `color.neutral.ink`; icon 20 x 20, #000000 `color.neutral.ink`.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Mobile nav item
A row inside the opened mobile menu. Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 390 x 50; padding 15px 27.2969px; background transparent; text Madefor-Display 16/normal 400, #000000 `color.neutral.ink`; icon 20 x 20, #000000 `color.neutral.ink` |
| focus-visible | shadow #000000 0px 0px 0px 1px, #000000 0px 0px 0px 3px; layers button.Q3cjxA 390.0x50.0 rgb(0, 0, 0) 0px 0px 0px 1px, rgb(0, 0, 0) 0px 0px 0px 3px |

![Mobile nav item default](components/crops/m-nav-item-default.png) ![Mobile nav item hover](components/crops/m-nav-item-hover.png) ![Mobile nav item focus-visible](components/crops/m-nav-item-focus-visible.png) ![Mobile nav item pressed](components/crops/m-nav-item-pressed.png)

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 332.45 x 75.97; background transparent; text wix-madefor-display-v2 34.53/37.98 400, #000000 `color.neutral.ink`.

![Mobile headline default](components/crops/m-hero-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Wix Studio wordmark and its square mark, the language globe, the social glyphs and the template/showcase artwork) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Everything behind Log In / Start Creating — the Studio editor, workspaces, dashboards, site management and checkout — was never reached. Those actions were measured and screenshotted, never followed; no account was created, no form was submitted and no plan was bought. What the editor itself looks like or how it behaves is not documented here — the marketing pages' claims about it were never verified.

### Pages

- **editorx.com is a redirect shell.** Every path on www.editorx.com 301s to wix.com/studio (deep paths keep their tail) except /pricing, which still serves a Wix page on the editorx.com domain. Paths on the redirect host were requested on editorx.com so the redirect is the evidence; pages with no editorx path left (design, plans, templates) were fetched from wix.com directly. Editor X's own product surface no longer exists here — this package documents the Wix Studio surface it now serves.
- **/pricing answered with its error pane** ('Couldn't load Premium plans due to a technical issue') at capture time and on retry — a Wix server-side state, not a capture failure. The pane and its Refresh link were measured as the error state they are; the plan-card components come from wix.com/studio/plans instead.
- **Start Creating / Log In / plan CTAs** were measured or screenshotted, never followed; the checkout and signup flows were never reached.
- **External surfaces** (academy courses, social profiles, wix.com subpages beyond the nine captured) are linked from the site but were never opened.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled and loading states** were not seen on the public surface; the error state was seen on /pricing.
- **The hero pill's fill lives on a child layer** (the wixui-button label span): the anchor's own computed background is transparent and its hover reading shows the fill mid-transition at alpha 0 — the real painted hover colour was not separable from the transition.
- **The hero pill's anchor colour reads rgb(0, 0, 238)** (the browser's unstyled-link default) and its pressed reading rgb(255, 0, 0) — link-state quirks of the unstyled anchor, not painted text colours; the label itself paints white.

### Themes

The surface paints one light theme; there is no user-facing dark mode or theme toggle. The export's "dark" set is the near-black #0e0e0e chrome (the footer) with its #f6f6f6 text and #828282 muted — a painted surface on the light page, not a selectable theme. The --wst-* layer declares no dark redeclarations.

### Fonts

- **Madefor** (Display and Text, 400-700 plus a 530 variable weight) is served from static.parastorage.com under five face names: Madefor-Display/-Text on the marketing chrome, wix-madefor-display-v2/-text-v2 on the thunderbolt content, plain Madefor on the plans page. The @font-face blocks are harvested in raw/css-vars.json (243 faces); the style guide falls back to system sans — the webfonts are licensed, not shipped.

### Screenshots

- The editor screenshots, template and showcase imagery and the Wix Studio wordmark in the shots are the product's published content. Display sizes are spx-scaled (font-size tracks viewport width via --theme-spx-ratio): the measured px values are the 1440px-desktop and 390px-mobile readings, not fixed sizes.
- home and mobile-home full pages overflowed one GPU texture and were stitched from chunks; design's too. Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Template artwork, plan feature lists, showcase sites, marketing copy and the FAQ answers are the product's content; only frames and components were measured.
