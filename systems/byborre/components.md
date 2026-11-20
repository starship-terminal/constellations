# BYBORRE components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from byborre.com on 2026-11-11, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; the login form was never filled; the order, cart and contact actions were never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (50 components, 123 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (122 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every captured surface paints `light`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [cart](screenshots/home-light-cart.png), [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| Textile Room | `/collection` | [default](screenshots/collection-light-default.png), [filtered](screenshots/collection-light-filtered.png), [full](screenshots/collection-light-full.png) |
| Textile detail | `/collection/blink` | [default](screenshots/textile-light-default.png), [full](screenshots/textile-light-full.png), [render](screenshots/textile-light-render.png) |
| Creative Control | `/creative-control` | [default](screenshots/creative-control-light-default.png), [full](screenshots/creative-control-light-full.png) |
| Knit Innovation | `/knit-innovation` | [default](screenshots/knit-innovation-light-default.png), [full](screenshots/knit-innovation-light-full.png) |
| Projects | `/projects` | [default](screenshots/projects-light-default.png), [full](screenshots/projects-light-full.png) |
| Brands | `/brands` | [default](screenshots/brands-light-default.png), [full](screenshots/brands-light-full.png) |
| Designers | `/designers` | [default](screenshots/designers-light-default.png), [full](screenshots/designers-light-full.png) |
| Founders' Story | `/founders-story` | [default](screenshots/founders-story-light-default.png), [full](screenshots/founders-story-light-full.png) |
| Responsibility | `/responsibility` | [default](screenshots/responsibility-light-default.png), [full](screenshots/responsibility-light-full.png) |
| Ways of Working | `/ways-of-working` | [default](screenshots/ways-of-working-light-default.png), [full](screenshots/ways-of-working-light-full.png) |
| Team | `/team` | [default](screenshots/team-light-default.png), [full](screenshots/team-light-full.png) |
| FAQ | `/faq` | [default](screenshots/faq-light-default.png), [full](screenshots/faq-light-full.png), [open](screenshots/faq-light-open.png) |
| Contact | `/contact` | [default](screenshots/contact-light-default.png), [full](screenshots/contact-light-full.png) |
| Pop-up Store | `/popup-store` | [default](screenshots/popup-store-light-default.png), [full](screenshots/popup-store-light-full.png) |
| Log in | `/login` | [default](screenshots/login-light-default.png) |
| Terms and Conditions | `/terms-and-conditions` | [default](screenshots/terms-light-default.png) |
| Privacy Policy | `/privacy-policy` | [default](screenshots/privacy-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Textile Room, phone | `/collection` | [default](screenshots/mobile-collection-light-default.png), [full](screenshots/mobile-collection-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu overlay | home, phone width | the header menu button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open), [m-nav-item](#mobile-nav-item) |
| About nav flyout | every desktop page | the About trigger's own hover | [home-light-menu](screenshots/home-light-menu.png), [nav-dropdown](#nav-flyout), [menu-link](#flyout-link) |
| Cookie consent bar | every page | hidden, never answered (the Reject/Accept buttons were never clicked) | hidden before every shot and reading |
| Newsletter / promo overlays | any page | hidden, never answered | hidden before every shot and reading |
| Cart flyout | home | the header cart button's own toggle | [home-light-cart](screenshots/home-light-cart.png) |
| Colour filter | /collection | a colour chip's own toggle (BLUE selected) | [collection-light-filtered](screenshots/collection-light-filtered.png), [colour-chip](#colour-filter-chip) |
| Textile viewer | /collection/blink | the PHOTO/RENDER toggle's own button | [textile-light-render](screenshots/textile-light-render.png) |
| FAQ accordion | /faq | a question row's own toggle | [faq-light-open](screenshots/faq-light-open.png), [faq-question](#faq-question) |
| Design Studio product | byborre.com design studio | signed-in; the login panel was measured, never filled | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 21 components were given a real keyboard focus. 7 draw an outline ring: `cart-button` (1px auto #005fcc `measured.focus-fallback`, offset 0px), `colour-chip` (on a child: 1px auto rgb(0, 95, 204) offset 2px), `textile-card` (1px auto #00e606 `color.brand.primary-500`, offset 1px), `view-tab` (1px auto #005fcc `measured.focus-fallback`, offset 0px), `signup-link` (1px auto #005fcc `measured.focus-fallback`, offset 0px), `forgot-link` (1px auto #005fcc `measured.focus-fallback`, offset 0px), `faq-question` (1px auto #005fcc `measured.focus-fallback`, offset 0px). 14 draw a focus ring as a shadow instead: `nav-link`, `nav-trigger`, `account-button`, `menu-link`, `hero-cta`, `order-cta`, `swatch`, `login-button`, `submit-button`, `footer-link`, `social-icon`, `m-nav-item`, `m-login-button`, `pattern-dropdown`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | -webkit-backdrop-filter, all, backdrop-filter, background-color, border-color, box-shadow, color, fill, filter, opacity, stroke, text-decoration-color, transform | account-button, footer-link, forgot-link, hero-cta, login-button, m-login-button, m-menu-button, m-nav-item and more |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Textile card](#textile-card) | 321.5 x 357.5 | - | - | transparent | none | 0 |
| [Flyout card](#flyout-card) | 280 x 160 | - | - | transparent | none | 0 |
| [Contact person](#contact-person) | 286.5 x 152 | - | - | transparent | none | 0 |
| [Mobile nav item](#mobile-nav-item) | 358 x 48 | - | 8px | transparent | none | 4px 16px |

## Components

### Shell and navigation

The cream header: wordmark, the Textile Room / Design Studio / Collaborations / About links and flyouts, Contact, and the cart and account icon buttons.

#### Marquee bar
The top ticker (ORDER FREE SAMPLES — WORLDWIDE SHIPPING) that scrolls continuously; measured as the outer bar, whose inner strip translates. Read as `marquee` on the home page.

**Values (default).** size 2834.22 x 12; background transparent; text Helvetica Neue 11/12 500, #ffffff `color.neutral.field`.

![Marquee bar default](components/crops/marquee-default.png)

#### Header
The sticky cream header: wordmark, Textile Room/Design Studio links, the Collaborations and About flyout triggers, Contact, Cart and account icons, the Go-to-the-platform pill. Read as `header` on the home page.

**Values (default).** size 1440 x 57; padding 0px 16px; border B: 1px solid #1b1b1b `color.neutral.ink`; background #f5f5f0 `color.neutral.cream`; text Helvetica Neue 16/20 400, #1b1b1b `color.neutral.ink`.

![Header default](components/crops/header-default.png)

#### Logo
The BYBORRE wordmark anchor (an img inside the home link). Read as `logo` on the home page.

**Values (default).** size 98.66 x 15.98; background transparent; text Helvetica Neue 13/19.5 400, #1b1b1b `color.neutral.ink`.

![Logo default](components/crops/logo-default.png)

#### Nav link
The Textile Room header link (with the New badge inside it). Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 152.67 x 28; padding 4px 8px; radius 8px; background transparent; text Helvetica Neue 16/20 400, #1b1b1b `color.neutral.ink`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers div.absolute.left-0 92.5x1.0 rgb(27, 27, 27); div.flex.h-[18px] 40.2x18.0 rgb(250, 226, 16) 8px |
| focus-visible | shadow #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset; outline 2px solid transparent, offset 2px; layers a.relative.group 152.7x28.0 rgb(255, 255, 255) 0px 0px 0px 0px inset, rgb(27, 27, 27) 0px 0px 0px 2px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 2px solid rgba(0, 0, 0, 0) offset 2px 8px; div.absolute.left-0 92.5x1.0 rgb(27, 27, 27); div.flex.h-[18px] 40.2x18.0 rgb(250, 226, 16) 8px |

Child layers that carry the look: div 92.5x1 background #1b1b1b `color.neutral.ink`; div 40.2x18 background #fae210 `color.brand.accent` radius 8px.

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Nav badge
The yellow "New" chip inside the Textile Room link. Read as `nav-badge` on the home page.

**Values (default).** size 24.22 x 12; background transparent; text Helvetica Neue 12/12 400, #1b1b1b `color.neutral.ink`.

![Nav badge default](components/crops/nav-badge-default.png)

#### Nav trigger
The About button that opens the header flyout; toggled, never followed. Read as `nav-trigger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 84.98 x 28; padding 4px 8px; radius 8px; background transparent; text Helvetica Neue 16/20 400, #1b1b1b `color.neutral.ink`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers div.absolute.left-0 69.0x1.0 rgb(27, 27, 27); span.iconify.i-mdi:plus 18.0x18.0 rgb(27, 27, 27) |
| focus-visible | shadow #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset; outline 2px solid transparent, offset 2px; layers button.relative.group 85.0x28.0 rgb(255, 255, 255) 0px 0px 0px 0px inset, rgb(27, 27, 27) 0px 0px 0px 2px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 2px solid rgba(0, 0, 0, 0) offset 2px 8px; div.absolute.left-0 69.0x1.0 rgb(27, 27, 27); span.iconify.i-mdi:plus 18.0x18.0 rgb(27, 27, 27) |

Child layers that carry the look: div 69x1 background #1b1b1b `color.neutral.ink`; span 18x18 background #1b1b1b `color.neutral.ink`.

![Nav trigger default](components/crops/nav-trigger-default.png) ![Nav trigger hover](components/crops/nav-trigger-hover.png) ![Nav trigger focus-visible](components/crops/nav-trigger-focus-visible.png) ![Nav trigger pressed](components/crops/nav-trigger-pressed.png)

#### Cart button
The icon-only cart action; opens the cart drawer (a local toggle). Read as `cart-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; padding 4px; border 1px solid #ccccc4 `color.neutral.line`; radius 9999px; background transparent; text Helvetica Neue 13/19.5 400, #1b1b1b `color.neutral.ink` |
| hover | background #ccccc4 `color.neutral.line` |
| focus-visible | outline 1px auto #005fcc `measured.focus-fallback`, offset 0px |
| pressed | background rgba(0, 0, 0, 0.1) `measured.dropdown-hover` |

![Cart button default](components/crops/cart-button-default.png) ![Cart button hover](components/crops/cart-button-hover.png) ![Cart button focus-visible](components/crops/cart-button-focus-visible.png) ![Cart button pressed](components/crops/cart-button-pressed.png)

#### Account button
The icon-only account action that opens the login dialog; measured, never followed. Read as `account-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; border 1px solid #ccccc4 `color.neutral.line`; radius 9999px; background transparent; text Helvetica Neue 12/16 500, #1b1b1b `color.neutral.ink`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background rgba(0, 0, 0, 0.1) `measured.dropdown-hover` |
| focus-visible | shadow #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset; outline 2px solid transparent, offset 2px |
| pressed | size 31.36 x 31.36; background rgba(0, 0, 0, 0.1) `measured.dropdown-hover`; transform scale(0.98) |

![Account button default](components/crops/account-button-default.png) ![Account button hover](components/crops/account-button-hover.png) ![Account button focus-visible](components/crops/account-button-focus-visible.png) ![Account button pressed](components/crops/account-button-pressed.png)

#### Nav flyout
The About flyout panel (link column plus the two image cards), opened by hovering its own trigger. Read as `nav-dropdown` on the home page.

**Values (default).** size 1408 x 210; padding 24px; border 1px solid #888888; background #f5f5f0 `color.neutral.cream`; text Helvetica Neue 16/20 400, #1b1b1b `color.neutral.ink`.

![Nav flyout default](components/crops/nav-dropdown-default.png)

#### Flyout link
A link inside the opened About flyout. Read as `menu-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 123 x 28; padding 4px 8px; radius 8px; background transparent; text Helvetica Neue 16/20 400, #1b1b1b `color.neutral.ink`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers div.absolute.left-0 107.0x1.0 rgb(27, 27, 27) |
| focus-visible, pressed | shadow #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset; outline 2px solid transparent, offset 2px; layers a.relative.group 123.0x28.0 rgb(255, 255, 255) 0px 0px 0px 0px inset, rgb(27, 27, 27) 0px 0px 0px 2px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 2px solid rgba(0, 0, 0, 0) offset 2px 8px; div.absolute.left-0 107.0x1.0 rgb(27, 27, 27) |

Child layers that carry the look: div 107x1 background #1b1b1b `color.neutral.ink`.

![Flyout link default](components/crops/menu-link-default.png) ![Flyout link hover](components/crops/menu-link-hover.png) ![Flyout link focus-visible](components/crops/menu-link-focus-visible.png) ![Flyout link pressed](components/crops/menu-link-pressed.png)

#### Flyout card
An image card inside the About flyout (the card whose caption is "Go to Textile Room"); measured, never followed. Read as `flyout-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 280 x 160; background transparent; text Helvetica Neue 16/24 400, #e5e5e1 `color.neutral.hairline`; layers a.relative.group 154.4x32.0 rgb(245, 245, 240) T:1px solid rgb(245, 245, 240) / R:1px solid rgb(245, 245, 240) / B:1px solid rgb(245, 245, 240) / L:1px solid rgb(245, 245, 240) 10px; span.iconify.i-mdi:arrow-right 18.0x18.0 rgb(27, 27, 27) |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: a 154.4x32 background #f5f5f0 `color.neutral.cream` border 1px solid #f5f5f0 `color.neutral.cream` radius 10px; span 18x18 background #1b1b1b `color.neutral.ink`.

![Flyout card default](components/crops/flyout-card-default.png) ![Flyout card hover](components/crops/flyout-card-hover.png) ![Flyout card pressed](components/crops/flyout-card-pressed.png)

### Home

The dark-media hero with the 80px display, the cream Explore-samples pill, and the manifesto sections.

#### Hero headline
The "Your brand's DNA in every stitch" display headline over the dark hero media. Read as `hero-title` on the home page.

**Values (default).** size 679 x 168; background transparent; text Helvetica Neue 80/84 500, #ffffff `color.neutral.field`.

![Hero headline default](components/crops/hero-title-default.png)

#### Hero copy
The lede under the hero headline (white on the dark hero media). Read as `hero-sub` on the home page.

**Values (default).** size 679 x 64; background transparent; text Helvetica Neue 24/32 400, #ffffff `color.neutral.field`.

![Hero copy default](components/crops/hero-sub-default.png)

#### Hero CTA
The "Explore samples →" action on the dark hero; measured, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 182.44 x 48; padding 0px 16px; border 1px solid #f5f5f0 `color.neutral.cream`; radius 10px; background #f5f5f0 `color.neutral.cream`; text Helvetica Neue 16/24 500, #1b1b1b `color.neutral.ink`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid #fae210 `color.brand.accent`; background #fae210 `color.brand.accent` |
| focus-visible | shadow #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset; outline 2px solid transparent, offset 2px |
| pressed | size 178.79 x 47.04; border 1px solid #fae210 `color.brand.accent`; background #fae210 `color.brand.accent`; transform scale(0.98) |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Section heading
A section display heading ("We reprogram tradition" / "BYBORRE is a textile innovation…"). Read as `section-h2` on the home page.

**Values (default).** size 412.66 x 106; background transparent; text Helvetica Neue 48/53 400, #1b1b1b `color.neutral.ink`.

![Section heading default](components/crops/section-h2-default.png)

### Textile Room

The /collection catalogue: sticky filter bar (colour chips, Pattern dropdown), the "35 textile families" grid and the textile cards.

#### Page title
The "Textile Room" display title. Read as `page-title` on the Textile Room page.

**Values (default).** size 592 x 84; background transparent; text Helvetica Neue 80/84 500, #1b1b1b `color.neutral.ink`.

![Page title default](components/crops/page-title-default.png)

#### Filter bar
The sticky colour-filter bar (Select colors, max 3) under the header. Read as `filter-bar` on the Textile Room page.

**Values (default).** size 1440 x 124; background #f5f5f0 `color.neutral.cream`; text Helvetica Neue 12/16 500, #1b1b1b `color.neutral.ink`.

![Filter bar default](components/crops/filter-bar-default.png)

#### Colour filter chip
A colour-filter circle (the label wrapping a colour-select checkbox); a BLUE selection was toggled for the filtered screenshot state, never submitted. Read as `colour-chip` on the Textile Room page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; padding 3px; radius 9999px; background transparent; text Helvetica Neue 13/19.5 400, #1b1b1b `color.neutral.ink`; layers ::before rgba(0, 0, 0, 0) 1px none 1; label::before.relative.mb-2 32pxx32px T:1px solid rgb(204, 204, 196) / R:1px solid rgb(204, 204, 196) / B:1px solid rgb(204, 204, 196) / L:1px solid rgb(204, 204, 196) 9999px; span.relative.inline-block 26.0x26.0 rgb(14, 76, 146) 9999px |
| hover | layers ::before rgba(0, 0, 0, 0) 1px none 1; label::before.relative.mb-2 32pxx32px T:1px solid rgb(153, 153, 147) / R:1px solid rgb(153, 153, 147) / B:1px solid rgb(153, 153, 147) / L:1px solid rgb(153, 153, 147) 9999px; span.relative.inline-block 26.0x26.0 rgb(14, 76, 146) 9999px |
| focus-visible | layers ::before rgba(0, 0, 0, 0) 1px none 1; label::before.relative.mb-2 32pxx32px T:1px solid rgb(204, 204, 196) / R:1px solid rgb(204, 204, 196) / B:1px solid rgb(204, 204, 196) / L:1px solid rgb(204, 204, 196) 9999px; input.sr-only 1.0x1.0 1px auto rgb(0, 95, 204) offset 2px; span.relative.inline-block 26.0x26.0 rgb(14, 76, 146) 9999px |
| pressed | layers ::before rgba(0, 0, 0, 0) 1px none 1; label::before.relative.mb-2 32pxx32px T:1px solid rgb(153, 153, 147) / R:1px solid rgb(153, 153, 147) / B:1px solid rgb(153, 153, 147) / L:1px solid rgb(153, 153, 147) 9999px; span.relative.inline-block 26.0x26.0 rgb(14, 76, 146) 9999px |

Child layers that carry the look: label::before 32pxx32px border 1px solid #ccccc4 `color.neutral.line` radius 9999px; span 26x26 background #0e4c92 `measured.chip-blue` radius 9999px.

![Colour filter chip default](components/crops/colour-chip-default.png) ![Colour filter chip hover](components/crops/colour-chip-hover.png) ![Colour filter chip focus-visible](components/crops/colour-chip-focus-visible.png) ![Colour filter chip pressed](components/crops/colour-chip-pressed.png)

#### Filter toggle
The "Show all filters" expander on the filter bar; present in the DOM but rendered 0x0 at desktop width, so it records missing rather than a phantom measurement. Read as `filter-toggle` on the Textile Room page.

Not on the page when it was captured.

#### Textile card
A textile card in the Textile Room grid (name, price, Configure textile / Order actions); measured, never followed. Read as `textile-card` on the Textile Room page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 321.5 x 357.5; background transparent; text Helvetica Neue 12/16 400, #f5f5f0 `color.neutral.cream`; layers div.relative.mb-3 321.5x321.5 rgb(209, 209, 209) 10px; div.inline-flex.items-center 87.8x24.0 rgba(0, 0, 0, 0.2) 1px solid rgb(153, 153, 147) offset -1px 9999px; div.absolute.inset-0 321.5x321.5 rgba(0, 0, 0, 0.3); button.relative.group 32.0x32.0 rgb(245, 245, 240) T:1px solid rgb(245, 245, 240) / R:1px solid rgb(245, 245, 240) / B:1px solid rgb(245, 245, 240) / L:1px solid rgb(245, 245, 240) 9999 |
| focus-visible | outline 1px auto #00e606 `color.brand.primary-500`, offset 1px; layers a 321.5x357.5 1px auto rgb(0, 230, 6) offset 1px; div.relative.mb-3 321.5x321.5 rgb(209, 209, 209) 10px; div.inline-flex.items-center 87.8x24.0 rgba(0, 0, 0, 0.2) 1px solid rgb(153, 153, 147) offset -1px 9999px; div.absolute.inset-0 321.5x321.5 rgba(0, 0, 0, 0.3); button.relative.group 32.0x32.0 rgb(245, 245, 240) T:1px solid rgb(245, 245, 240) / R:1px solid rgb(245, 245, 240) / B:1px solid rgb(24 |

Child layers that carry the look: div 321.5x321.5 background #d1d1d1 radius 10px; div 87.8x24 background rgba(0, 0, 0, 0.2) radius 9999px; div 321.5x321.5 background rgba(0, 0, 0, 0.3) `measured.card-scrim`.

![Textile card default](components/crops/textile-card-default.png) ![Textile card hover](components/crops/textile-card-hover.png) ![Textile card focus-visible](components/crops/textile-card-focus-visible.png) ![Textile card pressed](components/crops/textile-card-pressed.png)

#### Pattern dropdown
The Pattern filter trigger on the collection filter bar; measured closed, never opened. Read as `pattern-dropdown` on the Textile Room page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 160 x 32; padding 0px 12px; border 1px solid #ccccc4 `color.neutral.line`; radius 10px; background #ffffff `color.neutral.field`; text Helvetica Neue 12/16 500, #1b1b1b `color.neutral.ink`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background rgba(0, 0, 0, 0.1) `measured.dropdown-hover` |
| focus-visible | shadow #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset; outline 2px solid transparent, offset 2px |
| pressed | size 156.8 x 31.36; background rgba(0, 0, 0, 0.1) `measured.dropdown-hover`; transform scale(0.98) |

![Pattern dropdown default](components/crops/pattern-dropdown-default.png) ![Pattern dropdown hover](components/crops/pattern-dropdown-hover.png) ![Pattern dropdown focus-visible](components/crops/pattern-dropdown-focus-visible.png) ![Pattern dropdown pressed](components/crops/pattern-dropdown-pressed.png)

### Textile detail

A textile page (/collection/blink): the PHOTO/RENDER viewer, Configure-textile colour and tone pickers, spec accordions and the Order-sample action.

#### Textile name
The textile product title. Read as `textile-title` on the textile detail page.

**Values (default).** size 639 x 48; background transparent; text Helvetica Neue 48/48 400, #1b1b1b `color.neutral.ink`.

![Textile name default](components/crops/textile-title-default.png)

#### View tab
A product-view tab (Sample / Textile repeat / Sofa / Couch / Room divider); the Room-divider state is toggled for the screenshot. Read as `view-tab` on the textile detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 224 x 36; padding 8px 12px; border 1px solid #ccccc4 `color.neutral.line`; radius 10px; background #f5f5f0 `color.neutral.cream`; text Helvetica Neue 13/13 400, #1b1b1b `color.neutral.ink` |
| focus-visible | outline 1px auto #005fcc `measured.focus-fallback`, offset 0px |

![View tab default](components/crops/view-tab-default.png) ![View tab hover](components/crops/view-tab-hover.png) ![View tab focus-visible](components/crops/view-tab-focus-visible.png) ![View tab pressed](components/crops/view-tab-pressed.png)

#### Order CTA
The "Order free sample" action; measured, never pressed — it would mutate the cart. Read as `order-cta` on the textile detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 425 x 48; padding 0px 16px; border 1px solid #1b1b1b `color.neutral.ink`; radius 10px; background #1b1b1b `color.neutral.ink`; text Helvetica Neue 16/24 500, #f5f5f0 `color.neutral.cream`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid #c8b50d `color.brand.accent-border`; background #fae210 `color.brand.accent`; text Helvetica Neue 16/24 500, #1b1b1b `color.neutral.ink` |
| focus-visible | shadow #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset; outline 2px solid transparent, offset 2px |
| pressed | size 416.5 x 47.04; border 1px solid #c8b50d `color.brand.accent-border`; background #fae210 `color.brand.accent`; text Helvetica Neue 16/24 500, #1b1b1b `color.neutral.ink`; transform scale(0.98) |

![Order CTA default](components/crops/order-cta-default.png) ![Order CTA hover](components/crops/order-cta-hover.png) ![Order CTA focus-visible](components/crops/order-cta-focus-visible.png) ![Order CTA pressed](components/crops/order-cta-pressed.png)

#### Colourway swatch
A colourway selector (sr-only inputs behind swatch labels) on the detail page. Read as `swatch` on the textile detail page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 145.7 x 28; padding 4px 8px; radius 8px; background transparent; text Helvetica Neue 16/20 400, #1b1b1b `color.neutral.ink`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), transform 0.15s cubic-bezier(0.4, 0, 0.2, 1), filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), -webkit-backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1), backdrop-filter 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers div.absolute.left-0 129.7x1.0 rgb(27, 27, 27); span.iconify.i-mdi:plus 18.0x18.0 rgb(27, 27, 27) |
| focus-visible | shadow #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset; outline 2px solid transparent, offset 2px; layers button.relative.group 145.7x28.0 rgb(255, 255, 255) 0px 0px 0px 0px inset, rgb(27, 27, 27) 0px 0px 0px 2px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 2px solid rgba(0, 0, 0, 0) offset 2px 8px; div.absolute.left-0 129.7x1.0 rgb(27, 27, 27); span.iconify.i-mdi:plus 18.0x18.0 rgb(27, 27, 27) |

Child layers that carry the look: div 129.7x1 background #1b1b1b `color.neutral.ink`; span 18x18 background #1b1b1b `color.neutral.ink`.

![Colourway swatch default](components/crops/swatch-default.png) ![Colourway swatch hover](components/crops/swatch-hover.png) ![Colourway swatch focus-visible](components/crops/swatch-focus-visible.png) ![Colourway swatch pressed](components/crops/swatch-pressed.png)

#### Spec row
A row in the Textile-details block (composition, weight, width). Read as `spec-row` on the textile detail page.

**Values (default).** size 84 x 200; background transparent; text Helvetica Neue 13/19.5 400, #1b1b1b `color.neutral.ink`.

![Spec row default](components/crops/spec-row-default.png)

### Login dialog

The signed-out "Log in to continue" panel that gates the Design Studio; measured open, never filled or submitted.

#### Login dialog
The "Log in to continue" dialog that gates the Design Studio; captured open, never filled or submitted. Read as `login-dialog` on the login page.

**Values (default).** size 420 x 648; padding 32px; background transparent; text Helvetica Neue 40/42 400, #1b1b1b `color.neutral.ink`; layers input.h-12.w-full 356.0x48.0 rgb(255, 255, 255) T:1px solid rgb(204, 204, 196) / R:1px solid rgb(204, 204, 196) / B:1px solid rgb(204, 204, 196) / L:1px solid rgb(204, 204, 196) 10px; input.h-12.w-full 356.0x48.0 rgb(255, 255, 255) T:1px solid rgb(204, 204, 196) / R:1px solid rgb(204, 204, 196) / B:1px solid rgb(204, 204, 196) / L:1px solid rgb(204, 204, 196) 10px; button.relative.group 356.0x48.0.

Child layers that carry the look: input 356x48 background #ffffff `color.neutral.field` border 1px solid #ccccc4 `color.neutral.line` radius 10px; input 356x48 background #ffffff `color.neutral.field` border 1px solid #ccccc4 `color.neutral.line` radius 10px; button 356x48 background #1b1b1b `color.neutral.ink` border 1px solid #1b1b1b `color.neutral.ink` radius 10px.

![Login dialog default](components/crops/login-dialog-default.png)

#### Email field
The login email input; focused and given sample text that was deleted again — nothing sent. Read as `login-email` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 356 x 48; padding 0px 12px; border 1px solid #ccccc4 `color.neutral.line`; radius 10px; background #ffffff `color.neutral.field`; text Helvetica Neue 16/45.71 400, #1b1b1b `color.neutral.ink`; placeholder #646e69 `color.neutral.muted` |
| focused, filled | border 1px solid #888888; shadow #ffffff 0px 0px 0px 0px, rgba(136, 136, 136, 0.5) 0px 0px 0px 2px; outline 2px solid transparent, offset 2px |

![Email field default](components/crops/login-email-default.png) ![Email field focused](components/crops/login-email-focused.png) ![Email field filled](components/crops/login-email-filled.png)

#### Password field
The login password input; focused only, never typed into. Read as `login-password` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 356 x 48; padding 0px 12px; border 1px solid #ccccc4 `color.neutral.line`; radius 10px; background #ffffff `color.neutral.field`; text Helvetica Neue 16/45.71 400, #1b1b1b `color.neutral.ink`; placeholder #646e69 `color.neutral.muted` |
| focused | border 1px solid #888888; shadow #ffffff 0px 0px 0px 0px, rgba(136, 136, 136, 0.5) 0px 0px 0px 2px; outline 2px solid transparent, offset 2px |

![Password field default](components/crops/login-password-default.png) ![Password field focused](components/crops/login-password-focused.png)

#### Login button
The dialog's Login action; measured, never pressed. Read as `login-button` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 356 x 48; padding 0px 16px; border 1px solid #1b1b1b `color.neutral.ink`; radius 10px; background #1b1b1b `color.neutral.ink`; text Helvetica Neue 16/24 500, #f5f5f0 `color.neutral.cream`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid #c8b50d `color.brand.accent-border`; background #fae210 `color.brand.accent`; text Helvetica Neue 16/24 500, #1b1b1b `color.neutral.ink` |
| focus-visible | shadow #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset; outline 2px solid transparent, offset 2px |
| pressed | size 348.88 x 47.04; border 1px solid #c8b50d `color.brand.accent-border`; background #fae210 `color.brand.accent`; text Helvetica Neue 16/24 500, #1b1b1b `color.neutral.ink`; transform scale(0.98) |

![Login button default](components/crops/login-button-default.png) ![Login button hover](components/crops/login-button-hover.png) ![Login button focus-visible](components/crops/login-button-focus-visible.png) ![Login button pressed](components/crops/login-button-pressed.png)

#### Sign-up link
The "Don't have an account? Sign up" link; measured, never followed. Read as `signup-link` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 54.84 x 24; background transparent; text Helvetica Neue 16/24 400, #1b1b1b `color.neutral.ink`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text Helvetica Neue 16/24 400, #646e69 `color.neutral.muted` |
| focus-visible | outline 1px auto #005fcc `measured.focus-fallback`, offset 0px; layers button.bg-transparent.underline 54.8x24.0 1px auto rgb(0, 95, 204) offset 0px |
| pressed | text Helvetica Neue 16/24 400, #646e69 `color.neutral.muted` |

![Sign-up link default](components/crops/signup-link-default.png) ![Sign-up link hover](components/crops/signup-link-hover.png) ![Sign-up link focus-visible](components/crops/signup-link-focus-visible.png) ![Sign-up link pressed](components/crops/signup-link-pressed.png)

#### Forgot-password link
The forgot-password link inside the dialog; measured, never followed. Read as `forgot-link` on the login page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 129.92 x 24; background transparent; text Helvetica Neue 16/24 400, #646e69 `color.neutral.muted`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text Helvetica Neue 16/24 400, #000000 |
| focus-visible | outline 1px auto #005fcc `measured.focus-fallback`, offset 0px; layers button.mt-4.bg-transparent 129.9x24.0 1px auto rgb(0, 95, 204) offset 0px |
| pressed | text Helvetica Neue 16/24 400, #000000 |

![Forgot-password link default](components/crops/forgot-link-default.png) ![Forgot-password link hover](components/crops/forgot-link-hover.png) ![Forgot-password link focus-visible](components/crops/forgot-link-focus-visible.png) ![Forgot-password link pressed](components/crops/forgot-link-pressed.png)

### FAQ

The /faq accordion: question rows, toggled open for the screenshot state.

#### FAQ title
The FAQ page title and a section heading (Textile information). Read as `faq-title` on the FAQ page.

**Values (default).** size 592 x 84; background transparent; text Helvetica Neue 80/84 500, #1b1b1b `color.neutral.ink`.

![FAQ title default](components/crops/faq-title-default.png)

#### FAQ question
An accordion question row; toggled open for the opened state and the screenshot. Read as `faq-question` on the FAQ page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 719 x 56; padding 16px 24px; background transparent; text Helvetica Neue 16/24 400, #1b1b1b `color.neutral.ink`; layers span.iconify.i-mdi:plus 24.0x24.0 rgb(153, 153, 147) |
| focus-visible | outline 1px auto #005fcc `measured.focus-fallback`, offset 0px; layers button.w-full.px-4 719.0x56.0 1px auto rgb(0, 95, 204) offset 0px; span.iconify.i-mdi:plus 24.0x24.0 rgb(153, 153, 147) |

Child layers that carry the look: span 24x24 background #999993 `color.neutral.icon-muted`.

![FAQ question default](components/crops/faq-question-default.png) ![FAQ question hover](components/crops/faq-question-hover.png) ![FAQ question focus-visible](components/crops/faq-question-focus-visible.png) ![FAQ question pressed](components/crops/faq-question-pressed.png)

### Contact form

The /contact form: text, email, select and textarea fields plus the Send action; focused only, never submitted.

#### Contact title
The "Contact us" heading. Read as `contact-title` on the contact page.

**Values (default).** size 647 x 168; background transparent; text Helvetica Neue 80/84 500, #1b1b1b `color.neutral.ink`.

![Contact title default](components/crops/contact-title-default.png)

#### Text field
The First-name input; focused and given sample text that was deleted again — nothing sent. Read as `text-field` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 623 x 48; padding 0px 12px; border 1px solid #ccccc4 `color.neutral.line`; radius 10px; background #ffffff `color.neutral.field`; text Helvetica Neue 16/45.71 400, #1b1b1b `color.neutral.ink`; placeholder #646e69 `color.neutral.muted` |
| focused, filled | border 1px solid #888888; shadow #ffffff 0px 0px 0px 0px, rgba(136, 136, 136, 0.5) 0px 0px 0px 2px; outline 2px solid transparent, offset 2px |

![Text field default](components/crops/text-field-default.png) ![Text field focused](components/crops/text-field-focused.png) ![Text field filled](components/crops/text-field-filled.png)

#### Email field
The Email input on the contact form; focused only. Read as `email-field` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 623 x 48; padding 0px 12px; border 1px solid #ccccc4 `color.neutral.line`; radius 10px; background #ffffff `color.neutral.field`; text Helvetica Neue 16/45.71 400, #1b1b1b `color.neutral.ink`; placeholder #646e69 `color.neutral.muted` |
| focused | border 1px solid #888888; shadow #ffffff 0px 0px 0px 0px, rgba(136, 136, 136, 0.5) 0px 0px 0px 2px; outline 2px solid transparent, offset 2px |

![Email field default](components/crops/email-field-default.png) ![Email field focused](components/crops/email-field-focused.png)

#### Select
The inquiry-type select; focused only, never changed. Read as `select-field` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 623 x 48; padding 0px 12px; border 1px solid #ccccc4 `color.neutral.line`; radius 10px; background #ffffff `color.neutral.field`; text Helvetica Neue 16/45.71 400, #646e69 `color.neutral.muted` |
| focused | border 1px solid #888888; shadow #ffffff 0px 0px 0px 0px, rgba(136, 136, 136, 0.5) 0px 0px 0px 2px; outline 2px solid transparent, offset 2px |

![Select default](components/crops/select-field-default.png) ![Select focused](components/crops/select-field-focused.png)

#### Text area
The project-description textarea; focused only, never typed into. Read as `text-area` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 623 x 104; padding 6px 12px 0px 12px; border 1px solid #ccccc4 `color.neutral.line`; radius 10px; background #ffffff `color.neutral.field`; text Helvetica Neue 16/32 400, #1b1b1b `color.neutral.ink`; placeholder #646e69 `color.neutral.muted` |
| focused | border 1px solid #888888; shadow #ffffff 0px 0px 0px 0px, rgba(136, 136, 136, 0.5) 0px 0px 0px 2px; outline 2px solid transparent, offset 2px |

![Text area default](components/crops/text-area-default.png) ![Text area focused](components/crops/text-area-focused.png)

#### Submit button
The form's Send action; measured, never pressed. Read as `submit-button` on the contact page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 86.44 x 48; padding 0px 16px; border 1px solid #1b1b1b `color.neutral.ink`; radius 10px; background #1b1b1b `color.neutral.ink`; text Helvetica Neue 16/24 500, #f5f5f0 `color.neutral.cream`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid #c8b50d `color.brand.accent-border`; background #fae210 `color.brand.accent`; text Helvetica Neue 16/24 500, #1b1b1b `color.neutral.ink` |
| focus-visible | shadow #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset; outline 2px solid transparent, offset 2px |
| pressed | size 84.71 x 47.04; border 1px solid #c8b50d `color.brand.accent-border`; background #fae210 `color.brand.accent`; text Helvetica Neue 16/24 500, #1b1b1b `color.neutral.ink`; transform scale(0.98) |

![Submit button default](components/crops/submit-button-default.png) ![Submit button hover](components/crops/submit-button-hover.png) ![Submit button focus-visible](components/crops/submit-button-focus-visible.png) ![Submit button pressed](components/crops/submit-button-pressed.png)

#### Contact person
A named contact block (name, role) on the contact page. Read as `person-card` on the contact page.

**Values (default).** size 286.5 x 152; background transparent; text Helvetica Neue 40/44 400, #1b1b1b `color.neutral.ink`.

![Contact person default](components/crops/person-card-default.png)

### Footer

The ink footer panel: link columns and the social row.

#### Footer
The page footer: link columns, social links, legal and newsletter copy. Read as `footer` on the home page.

**Values (default).** size 1440 x 537.14; radius 24px 24px 0px 0px; background #1b1b1b `color.neutral.ink`; text Helvetica Neue 10/15 400, #ffffff `color.neutral.field`.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 107.06 x 20.5; padding 4px 0px; radius 8px; background transparent; text Helvetica Neue 10/12.5 400, #ffffff `color.neutral.field`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers div.absolute.left-0 107.1x1.0 rgb(27, 27, 27) |
| focus-visible | shadow #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset; outline 2px solid transparent, offset 2px; layers a.relative.group 107.1x20.5 rgb(255, 255, 255) 0px 0px 0px 0px inset, rgb(27, 27, 27) 0px 0px 0px 2px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 2px solid rgba(0, 0, 0, 0) offset 2px 8px; div.absolute.left-0 107.1x1.0 rgb(27, 27, 27) |

Child layers that carry the look: div 107.1x1 background #1b1b1b `color.neutral.ink`.

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social link
A social link in the footer. Read as `social-icon` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 150 x 24; radius 8px; background transparent; text Helvetica Neue 16/24 400, #ffffff `color.neutral.field`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers div.absolute.left-0 0.0x0.0 rgb(27, 27, 27) |
| focus-visible | shadow #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset; outline 2px solid transparent, offset 2px; layers a.relative.group 150.0x24.0 rgb(255, 255, 255) 0px 0px 0px 0px inset, rgb(27, 27, 27) 0px 0px 0px 2px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 2px solid rgba(0, 0, 0, 0) offset 2px 8px; div.absolute.left-0 0.0x0.0 rgb(27, 27, 27) |

Child layers that carry the look: div 0x0 background #1b1b1b `color.neutral.ink`.

![Social link default](components/crops/social-icon-default.png) ![Social link hover](components/crops/social-icon-hover.png) ![Social link focus-visible](components/crops/social-icon-focus-visible.png) ![Social link pressed](components/crops/social-icon-pressed.png)

### Mobile (390 wide)

The same surface at phone width: slimmer header, the full-screen menu panel, smaller display type.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 64; padding 0px 16px; background #f5f5f0 `color.neutral.cream`; text Helvetica Neue 13/19.5 400, #1b1b1b `color.neutral.ink`.

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
The burger toggle that opens the mobile menu. Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 32 x 32; border 1px solid #ccccc4 `color.neutral.line`; radius 9999px; background transparent; text Helvetica Neue 12/16 500, #1b1b1b `color.neutral.ink`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1).

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The opened mobile menu panel (the aside that slides over the page). Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 844; padding 64px 0px 0px 0px; background #f5f5f0 `color.neutral.cream`; text Helvetica Neue 16/24 500, #1b1b1b `color.neutral.ink`.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Mobile nav item
A link inside the opened mobile menu. Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 358 x 48; padding 4px 16px; radius 8px; background transparent; text Helvetica Neue 16/24 500, #1b1b1b `color.neutral.ink`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers div.absolute.left-0 0.0x0.0 rgb(27, 27, 27); div.flex.h-[18px] 40.7x18.0 rgb(250, 226, 16) 8px |
| focus-visible | shadow #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset; outline 2px solid transparent, offset 2px; layers a.relative.group 358.0x48.0 rgb(255, 255, 255) 0px 0px 0px 0px inset, rgb(27, 27, 27) 0px 0px 0px 2px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 2px solid rgba(0, 0, 0, 0) offset 2px 8px; div.absolute.left-0 0.0x0.0 rgb(27, 27, 27); div.flex.h-[18px] 40.7x18.0 rgb(250, 226, 16) 8px |

Child layers that carry the look: div 0x0 background #1b1b1b `color.neutral.ink`; div 40.7x18 background #fae210 `color.brand.accent` radius 8px.

![Mobile nav item default](components/crops/m-nav-item-default.png) ![Mobile nav item hover](components/crops/m-nav-item-hover.png) ![Mobile nav item focus-visible](components/crops/m-nav-item-focus-visible.png) ![Mobile nav item pressed](components/crops/m-nav-item-pressed.png)

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 358 x 144; background transparent; text Helvetica Neue 48/48 400, #ffffff `color.neutral.field`.

![Mobile headline default](components/crops/m-hero-default.png)

#### Mobile login button
The Login/Sign-up row inside the mobile menu; opens the login dialog, measured never followed. Read as `m-login-button` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 358 x 50; padding 12px 16px; border 1px solid #ccccc4 `color.neutral.line`; radius 8px; background transparent; text Helvetica Neue 16/24 500, #1b1b1b `color.neutral.ink`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | shadow #ffffff 0px 0px 0px 0px inset, #1b1b1b 0px 0px 0px 2px inset; outline 2px solid transparent, offset 2px |

![Mobile login button default](components/crops/m-login-button-default.png) ![Mobile login button hover](components/crops/m-login-button-hover.png) ![Mobile login button focus-visible](components/crops/m-login-button-focus-visible.png) ![Mobile login button pressed](components/crops/m-login-button-pressed.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the BYBORRE wordmark, the iconify Material-Design glyphs for account/cart/menu/arrows, the social glyphs and the textile photography) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

The Design Studio — BYBORRE's configure-and-order product — sits behind the login panel that gates /dashboard. The studio canvas, saved designs, the dashboard, ordering, checkout and account were never reached; /dashboard returns only a signed-out shell. The login panel itself was captured open and every field was measured, but nothing was ever typed, filled or submitted.

### Pages

- **The studio.** Everything post-login was never reached; the "Log in to continue" panel was measured as a form, never used.
- **Order, cart and checkout.** Order-sample, Order-free-sample, the header cart and every "Get in touch" action were measured or screenshotted, never followed through to a purchase or a sent message.
- **External surfaces** (help-center.byborre.com, news.byborre.com, the pcon-solutions catalogue, the Homerun jobs board, Instagram/LinkedIn) are linked from the site but were never opened.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.
- **filter-toggle** is recorded missing: the "Show all filters" button exists in the /collection DOM but renders 0x0 at 1440 wide — it is a smaller-viewport affordance.
- **Colour-filter state** captured once (BLUE selected) for collection-light-filtered; the Pattern dropdown was measured closed, never opened.
- **The cart flyout** was toggled open for home-light-cart; its contents were screenshotted, never read as checkout behaviour.

### Themes

One theme is painted: the cream canvas with ink panels (footer, marquee, hero media). The stylesheet declares a `.dark` flip of --color-primary-DEFAULT (500 -> 400) but nothing on the public surface toggles it; tokens.json keeps the ink-surface roles in the dark set.

### Fonts

- **Helvetica Neue** (400/500/700) is the single served family, loaded from byborre.com's own fonts; the style guide falls back to system sans.

### Screenshots

- Textile photography, the hero media, the flyout cards' imagery and the BYBORRE wordmark in the screenshots are the product's published content.
- The /collection full-page shot is tall (31,333px) and capped at the shooter's eight chunks; the grid beyond the cap is a documented truncation, not a missed surface.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Textile copy, project stories, the founders' story and FAQ answers are the product's content; only frames and components were measured.
