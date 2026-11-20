# Cartesia components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from cartesia.ai on 2026-11-12, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. cartesia.ai is three surfaces signed out: the marketing site (Astro + Tailwind v4, ABC Diatype body with PP Kyoto display, a --cartesia-* palette under a shadcn-style semantic layer), the Playground auth boundary (Clerk sign-in/sign-up cards on play.cartesia.ai, sharing the token layer) and the docs site (a separate Mintlify app in Inter, measured for reference but kept out of the token export). Nothing was signed into, generated, called or submitted; the sign-in and sign-up forms were never filled; the Talk to Skylar / Talk to Cartesia live-agent calls were never started; the only presses were local UI toggles — the nav and mobile menus, the voice picker, a voice row's play control and the FAQ disclosures.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (63 components, 177 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (176 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every captured surface paints `light` (the marketing .dark islands appear inside light shots). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| Sonic (TTS product) | `/sonic` | [default](screenshots/sonic-light-default.png), [full](screenshots/sonic-light-full.png), [voice-menu](screenshots/sonic-light-voice-menu.png) |
| Ink (STT product) | `/ink` | [default](screenshots/ink-light-default.png), [full](screenshots/ink-light-full.png) |
| Agents | `/agents` | [default](screenshots/agents-light-default.png), [full](screenshots/agents-light-full.png) |
| Voice cloning | `/product/voice-cloning` | [default](screenshots/voice-cloning-light-default.png), [full](screenshots/voice-cloning-light-full.png) |
| Voice library | `/voices` | [default](screenshots/voices-light-default.png), [full](screenshots/voices-light-full.png) |
| Pricing | `/pricing` | [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Tools | `/tools` | [default](screenshots/tools-light-default.png), [full](screenshots/tools-light-full.png) |
| MCP | `/mcp` | [default](screenshots/mcp-light-default.png), [full](screenshots/mcp-light-full.png) |
| Research | `/research` | [default](screenshots/research-light-default.png), [full](screenshots/research-light-full.png) |
| Blog | `/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| Contact | `/contact` | [default](screenshots/contact-light-default.png), [full](screenshots/contact-light-full.png) |
| Customers | `/customers` | [default](screenshots/customers-light-default.png), [full](screenshots/customers-light-full.png) |
| Sign in | `play.cartesia.ai/sign-in` | [default](screenshots/signin-light-default.png) |
| Sign up | `play.cartesia.ai/sign-in/create` | [default](screenshots/signup-light-default.png) |
| Docs | `docs.cartesia.ai` | [default](screenshots/docs-light-default.png), [full](screenshots/docs-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Sonic, phone | `/sonic` | [default](screenshots/mobile-sonic-light-default.png), [full](screenshots/mobile-sonic-light-full.png) |
| Sign in, phone | `play.cartesia.ai/sign-in` | [default](screenshots/mobile-signin-light-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu overlay | home, phone width | the hamburger button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open) |
| Products mega-menu | every marketing page | the nav trigger's own click | [home-light-menu](screenshots/home-light-menu.png), [nav-dropdown](#nav-dropdown), [menu-link](#menu-link) |
| Voice picker popover | /sonic demo | the voice-select button's own click — a local listbox, no audio generated | [sonic-light-voice-menu](screenshots/sonic-light-voice-menu.png) |
| Consent island | every page | hidden, never answered (no consent button was ever clicked, no consent POST sent) | hidden before every shot and reading |
| Voice playback | /sonic and /voices demos | a voice row's own play button — the public demo the page offers signed out | [play-btn](#play-button), [voice-row](#voice-row), [word-play](#sample-play-button) |
| FAQ disclosures | /pricing | the details/summary items' own toggles | [faq-trigger](#faq-item) |
| Signed-in playground | play.cartesia.ai app | the voice playground lives behind sign-in | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 35 components were given a real keyboard focus. 18 draw an outline ring: `banner` (1px auto oklab(0.707999 -0.00000712276 0.0000166297 / 0.5), offset 1px), `hero-orb` (2px solid #309d4b `color.brand.verdant`, offset 4px), `voice-nav` (2px solid #309d4b `color.brand.verdant`, offset 2px), `media-frame` (2px solid lab(66.128 -0.0000298023 0.0000119209), offset -2px), `product-card` (1px auto oklab(0.707999 -0.00000712276 0.0000166297 / 0.5), offset 1px), `usecase-chip` (1px auto oklab(0.707999 -0.00000712276 0.0000166297 / 0.5), offset 0px), `voice-chip` (1px auto oklab(0.707999 -0.00000712276 0.0000166297 / 0.5), offset 0px), `word-play` (2px solid #309d4b `color.brand.verdant`, offset 2px), `voice-row` (2px solid #309d4b `color.brand.verdant`, offset 2px), `globe-dot` (2px solid lab(66.128 -0.0000298023 0.0000119209), offset 2px), `globe-play` (2px solid lab(66.128 -0.0000298023 0.0000119209), offset 2px), `globe-arrow` (2px solid lab(66.128 -0.0000298023 0.0000119209), offset 2px), `globe-voice` (2px solid lab(66.128 -0.0000298023 0.0000119209), offset 2px), `faq-trigger` (2px solid lab(66.128 -0.0000298023 0.0000119209), offset -2px), `docs-search` (1px auto #309d4b `color.brand.verdant`, offset 0px), `docs-nav-item` (1px auto #309d4b `color.brand.verdant`, offset -2px), `m-nav-item` (1px auto oklab(0.707999 -0.00000712276 0.0000166297 / 0.5), offset 0px), `product-row` (1px auto oklab(0.707999 -0.00000712276 0.0000166297 / 0.5), offset 1px). 1 draw a focus ring as a shadow instead: `menu-link`. 16 change only their border: `nav-trigger`, `nav-link`, `nav-signin`, `nav-sales`, `nav-cta`, `cta-link`, `accordion-trigger`, `pd-cta`, `pd-secondary`, `play-btn`, `plan-cta`, `plan-cta-alt`, `continue-btn`, `sso-btn`, `passkey-btn`, `footer-link`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `cubic-bezier(0.23, 1, 0.32, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | accordion-trigger |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, all, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | continue-btn, cta-link, email-field, footer-link, menu-link, nav-cta, nav-link, nav-sales and more |
| 0.2s | `cubic-bezier(0, 0, 0.2, 1)` | opacity, translate, visibility | m-menu-open |
| 0.35s | `cubic-bezier(0.22, 1, 0.36, 1)` | opacity, transform, translate | nav-dropdown |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Product card](#product-card) | 571 x 377.59 | - | - | transparent | none | 0 |
| [Customer story tile](#customer-story-tile) | 559 x 559 | 1px solid #e4e3db `color.brand.canvas` | 8px | lab(95.4982 -0.0449121 1.52447) | none | 0 |
| [Media frame](#media-frame) | 559 x 559 | 1px solid #e4e3db `color.brand.canvas` | 8px | lab(95.4982 -0.0449121 1.52447) | none | 0 |
| [Plan card](#plan-card) | 254.8 x 543.25 | - | - | #fefefe `color.neutral.scale-50` | #e4e3db 0px 0px 0px 1px | 40px 24px |
| [Sign-in card](#sign-in-card) | 640 x 727.5 | - | - | transparent | none | 144px 0px 40px 0px |
| [Signup card](#signup-card) | 640 x 727.5 | - | - | transparent | none | 144px 0px 40px 0px |

## Components

### Shell and navigation

The marketing chrome on the #fefefe field: wordmark, the Products mega-menu trigger, plain links, Sign In, Talk to Sales and the verdant Try Cartesia pill.

#### Header
The sticky marketing header: wordmark, the Products/Solutions/Resources menu triggers, Customers, Pricing, Sign in, Contact Sales and the Try-Cartesia pill. Read as `header` on the home page.

**Values (default).** size 1440 x 64; border B: 1px solid #e4e3db `color.brand.canvas`; background #fefefe `color.neutral.scale-50`; text ABC Diatype-75f05108b2d5df75 14/20 500, #1e1c1a `color.neutral.100`.

![Header default](components/crops/header-default.png)

#### Logo
The Cartesia wordmark anchor (verdant mark over the neutral wordmark paths). Read as `logo` on the home page.

**Values (default).** size 139.52 x 20; background transparent; text ABC Diatype-75f05108b2d5df75 16/24 400, #1e1c1a `color.neutral.100`.

![Logo default](components/crops/logo-default.png)

#### Announcement banner
The full-width announcement strip above the header; measured never followed. Read as `banner` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 1440 x 36.8; padding 10px 16px; background transparent; text ABC Diatype-75f05108b2d5df75 14/16.8 500, #1e1c1a `color.neutral.100`; icon 20 x 16, #309d4b `color.brand.verdant`; ancestor paint `div.col-[full].border-border`: background #f4faef `color.green.50` |
| focus-visible | outline 1px auto oklab(0.707999 -0.00000712276 0.0000166297 / 0.5), offset 1px; layers a.group.flex 1440.0x36.8 1px auto oklab(0.707999 -0.00000712276 0.0000166297 / 0.5) offset 1px |

![Announcement banner default](components/crops/banner-default.png) ![Announcement banner hover](components/crops/banner-hover.png) ![Announcement banner focus-visible](components/crops/banner-focus-visible.png) ![Announcement banner pressed](components/crops/banner-pressed.png)

#### Nav trigger
The Products button that opens the header mega-menu; toggled, never followed. Read as `nav-trigger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 90.95 x 36; padding 6px 8px; border 1px solid transparent; radius 4px; background transparent; text ABC Diatype-75f05108b2d5df75 14/20 500, #1e1c1a `color.neutral.100`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 12 x 12, #1e1c1a `color.neutral.100` |
| hover | background #f3f2ef `color.neutral.scale-200` |
| focus-visible | border 1px solid lab(66.128 -0.0000298023 0.0000119209); background #f3f2ef `color.neutral.scale-200` |
| pressed | background #f3f2ef `color.neutral.scale-200` |

![Nav trigger default](components/crops/nav-trigger-default.png) ![Nav trigger hover](components/crops/nav-trigger-hover.png) ![Nav trigger focus-visible](components/crops/nav-trigger-focus-visible.png) ![Nav trigger pressed](components/crops/nav-trigger-pressed.png)

#### Nav link
The plain Pricing header link. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 62.19 x 36; padding 6px 8px; border 1px solid transparent; radius 4px; background transparent; text ABC Diatype-75f05108b2d5df75 14/20 500, #1e1c1a `color.neutral.100`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f3f2ef `color.neutral.scale-200` |
| focus-visible | border 1px solid lab(66.128 -0.0000298023 0.0000119209); background #f3f2ef `color.neutral.scale-200` |
| pressed | background #f3f2ef `color.neutral.scale-200` |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Sign-in link
The Sign-in header action (ghost pill); measured never followed. Read as `nav-signin` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 44.67 x 36; border 1px solid transparent; radius 8px; background transparent; text ABC Diatype-75f05108b2d5df75 14/20 500, #1e1c1a `color.neutral.100`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | border 1px solid lab(66.128 -0.0000298023 0.0000119209) |

![Sign-in link default](components/crops/nav-signin-default.png) ![Sign-in link hover](components/crops/nav-signin-hover.png) ![Sign-in link focus-visible](components/crops/nav-signin-focus-visible.png) ![Sign-in link pressed](components/crops/nav-signin-pressed.png)

#### Sales link
The Contact-Sales header action (outlined pill); measured never followed. Read as `nav-sales` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 122.08 x 36; padding 0px 16px; border 1px solid #e4e3db `color.brand.canvas`; radius 8px; background #fefefe `color.neutral.scale-50`; text ABC Diatype-75f05108b2d5df75 14/20 500, #1e1c1a `color.neutral.100`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f3f2ef `color.neutral.scale-200` |
| focus-visible | border 1px solid lab(66.128 -0.0000298023 0.0000119209) |
| pressed | background #f3f2ef `color.neutral.scale-200` |

![Sales link default](components/crops/nav-sales-default.png) ![Sales link hover](components/crops/nav-sales-hover.png) ![Sales link focus-visible](components/crops/nav-sales-focus-visible.png) ![Sales link pressed](components/crops/nav-sales-pressed.png)

#### Nav CTA
The Try-Cartesia solid pill; measured never followed. Read as `nav-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 120 x 36; padding 0px 16px; border 1px solid transparent; radius 8px; background #309d4b `color.brand.verdant`; text ABC Diatype-75f05108b2d5df75 14/20 500, #f9f9f8 `color.neutral.scale-100`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background oklab(0.615694 -0.130896 0.0819391 / 0.9) |
| focus-visible | border 1px solid lab(66.128 -0.0000298023 0.0000119209) |
| pressed | background oklab(0.615694 -0.130896 0.0819391 / 0.9) |

![Nav CTA default](components/crops/nav-cta-default.png) ![Nav CTA hover](components/crops/nav-cta-hover.png) ![Nav CTA focus-visible](components/crops/nav-cta-focus-visible.png) ![Nav CTA pressed](components/crops/nav-cta-pressed.png)

#### Nav dropdown
The Products mega-menu panel (navigation-menu-content), opened by its own trigger. Read as `nav-dropdown` on the home page.

**Values (default).** size 624 x 161.75; padding 12px; background transparent; text PP Kyoto-b14c6ebb315b725b 18/24.75 500, #1e1c1a `color.neutral.100`; transition opacity 0.35s cubic-bezier(0.22, 1, 0.36, 1), transform 0.35s cubic-bezier(0.22, 1, 0.36, 1), translate 0.35s cubic-bezier(0.22, 1, 0.36, 1); icon 16 x 16, #525150 `color.neutral.60`; layers a.border.border-transparent 197.3x64.8 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 6px; a.border.border-transparent 197.3x64.8 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 6px; a.border.border-transparent 197.3x64.8 T:1px solid rgba(0, 0, 0, 0) ; ancestor paint `nav.data-[ending-style]:easing-[ease].xs:w-(--popup-width)`: background #fefefe `color.neutral.scale-50`; radius 8px; shadow oklab(0.227917 0.00188442 0.00454755 / 0.1) 0px 0px 0px 1px, rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px -1px.

Child layers that carry the look: a 197.3x64.8 border 1px solid transparent radius 6px; a 197.3x64.8 border 1px solid transparent radius 6px; a 197.3x64.8 border 1px solid transparent radius 6px.

![Nav dropdown default](components/crops/nav-dropdown-default.png)

#### Menu link
A product link inside the opened mega-menu. Read as `menu-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 197.33 x 64.75; padding 8px 12px; border 1px solid transparent; radius 6px; background transparent; text PP Kyoto-b14c6ebb315b725b 18/24.75 500, #1e1c1a `color.neutral.100`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background oklab(0.961004 -0.0000606179 0.00415242 / 0.5) |
| focus-visible, pressed | border 1px solid lab(66.128 -0.0000298023 0.0000119209); background oklab(0.961004 -0.0000606179 0.00415242 / 0.5); shadow #1e1c1a 0px 0px 0px 0px |

![Menu link default](components/crops/menu-link-default.png) ![Menu link hover](components/crops/menu-link-hover.png) ![Menu link focus-visible](components/crops/menu-link-focus-visible.png) ![Menu link pressed](components/crops/menu-link-pressed.png)

### Home hero

The 40px PP Kyoto hero, the Talk-to-Skylar voice orb ringed by voice-chooser buttons, and the customer-story media frame.

#### Hero headline
The display headline (PP Kyoto / font-display) under the header. Read as `hero-title` on the home page.

**Values (default).** size 864.95 x 92; background transparent; text PP Kyoto-b14c6ebb315b725b 40/46 500, oklab(0.227917 0.00188442 0.00454755 / 0.7).

![Hero headline default](components/crops/hero-title-default.png)

#### Hero copy
The lede under the headline, ABC Diatype / font-sans. Read as `hero-lede` on the home page.

**Values (default).** size 520 x 48; background transparent; text ABC Diatype-75f05108b2d5df75 16/24 400, #525150 `color.neutral.60`.

![Hero copy default](components/crops/hero-lede-default.png)

#### Talk-to-Skylar orb
The large round voice-agent button in the hero (icon-only, aria-labelled); measured, never pressed (a press starts a call). Read as `hero-orb` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 244.8 x 244.8; radius 3.35544e+07px; background transparent; text ABC Diatype-75f05108b2d5df75 16/24 400, #1e1c1a `color.neutral.100`; icon 21.59 x 21.59, #004e23 `color.brand.forest`; layers span.flex.items-center 48.0x48.0 oklab(0.997012 0.0000453889 0.0000200272 / 0.85) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.16) 0px 1px 8px 0px 3.35544e+07px |
| focus-visible | outline 2px solid #309d4b `color.brand.verdant`, offset 4px; layers button.cursor-pointer.rounded-full 244.8x244.8 2px solid rgb(48, 157, 75) offset 4px 3.35544e+07px; span.flex.items-center 48.0x48.0 oklab(0.997012 0.0000453889 0.0000200272 / 0.85) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.16) 0px 1px 8px 0px 3.35544e+07px |

Child layers that carry the look: span 48x48 background oklab(0.997012 0.0000453889 0.0000200272 / 0.85) radius 3.35544e+07px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.16) 0px 1px 8px 0px.

![Talk-to-Skylar orb default](components/crops/hero-orb-default.png) ![Talk-to-Skylar orb hover](components/crops/hero-orb-hover.png) ![Talk-to-Skylar orb focus-visible](components/crops/hero-orb-focus-visible.png) ![Talk-to-Skylar orb pressed](components/crops/hero-orb-pressed.png)

#### Voice chooser
A round "Choose <voice>, <role>" button around the orb (icon-only, aria-labelled). Read as `voice-choose` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 58.75 x 58.75; radius 3.35544e+07px; background transparent; text ABC Diatype-75f05108b2d5df75 16/24 400, #1e1c1a `color.neutral.100`; transform matrix(0.24, 0, 0, 0.24, -526.32, 0); opacity 0 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Voice chooser default](components/crops/voice-choose-default.png) ![Voice chooser hover](components/crops/voice-choose-hover.png) ![Voice chooser pressed](components/crops/voice-choose-pressed.png)

#### Voice carousel arrow
A previous/next-voice arrow button in the hero voice carousel. Read as `voice-nav` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 40; radius 3.35544e+07px; background oklab(0.997012 0.0000453889 0.0000200272 / 0.8); text ABC Diatype-75f05108b2d5df75 16/24 400, oklab(0.227917 0.00188442 0.00454755 / 0.7); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, oklab(0.227917 0.00188442 0.00454755 / 0.7); layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| hover | background lab(95.4982 -0.0449121 1.52447); text ABC Diatype-75f05108b2d5df75 16/24 400, #1e1c1a `color.neutral.100`; icon 20 x 20, #1e1c1a `color.neutral.100` |
| focus-visible | outline 2px solid #309d4b `color.brand.verdant`, offset 2px |
| pressed | background lab(95.4982 -0.0449121 1.52447); text ABC Diatype-75f05108b2d5df75 16/24 400, #1e1c1a `color.neutral.100`; icon 20 x 20, #1e1c1a `color.neutral.100` |

![Voice carousel arrow default](components/crops/voice-nav-default.png) ![Voice carousel arrow hover](components/crops/voice-nav-hover.png) ![Voice carousel arrow focus-visible](components/crops/voice-nav-focus-visible.png) ![Voice carousel arrow pressed](components/crops/voice-nav-pressed.png)

#### Media frame
A customer-story media tile with a play affordance; measured, never pressed. Read as `media-frame` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 559 x 559; border 1px solid #e4e3db `color.brand.canvas`; radius 8px; background lab(95.4982 -0.0449121 1.52447); text ABC Diatype-75f05108b2d5df75 14/19.6 500, #1e1c1a `color.neutral.100`; icon 16 x 16, #1e1c1a `color.neutral.100` |
| focus-visible | outline 2px solid lab(66.128 -0.0000298023 0.0000119209), offset -2px |

![Media frame default](components/crops/media-frame-default.png) ![Media frame hover](components/crops/media-frame-hover.png) ![Media frame focus-visible](components/crops/media-frame-focus-visible.png) ![Media frame pressed](components/crops/media-frame-pressed.png)

#### Customer story tile
The customer-story media tile behind the play affordance. Read as `story-card` on the home page.

**Values (default).** size 559 x 559; border 1px solid #e4e3db `color.brand.canvas`; radius 8px; background lab(95.4982 -0.0449121 1.52447); text ABC Diatype-75f05108b2d5df75 14/19.6 500, #1e1c1a `color.neutral.100`; icon 16 x 16, #1e1c1a `color.neutral.100`.

![Customer story tile default](components/crops/story-card-default.png)

### Home

Sections of the home page: the 26px display section headings, product cards and rows, the deployment accordion and the text CTAs.

#### Section heading (display)
A PP-Kyoto display section heading in the light sections. Read as `h2-display` on the home page.

**Values (default).** size 559 x 67.59; background transparent; text PP Kyoto-b14c6ebb315b725b 26/33.8 500, #1e1c1a `color.neutral.100`.

![Section heading (display) default](components/crops/h2-display-default.png)

#### Product card
A product card link (Ink/Sonic) in the full-stack section; measured never followed. Read as `product-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 571 x 377.59; background transparent; text ABC Diatype-75f05108b2d5df75 16/16 500, #1e1c1a `color.neutral.100`; icon 16 x 16, #525150 `color.neutral.60`; layers video.h-75.w-full 571.0x300.0 rgb(243, 242, 239) |
| focus-visible | outline 1px auto oklab(0.707999 -0.00000712276 0.0000166297 / 0.5), offset 1px; layers a.group.flex 571.0x377.6 1px auto oklab(0.707999 -0.00000712276 0.0000166297 / 0.5) offset 1px; video.h-75.w-full 571.0x300.0 rgb(243, 242, 239) |

Child layers that carry the look: video 571x300 background #f3f2ef `color.neutral.scale-200`.

![Product card default](components/crops/product-card-default.png) ![Product card hover](components/crops/product-card-hover.png) ![Product card focus-visible](components/crops/product-card-focus-visible.png) ![Product card pressed](components/crops/product-card-pressed.png)

#### Text CTA
The "Our research" pill link in the research section; measured never followed. Read as `cta-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 120 x 36; padding 0px 16px; border 1px solid #e4e3db `color.brand.canvas`; radius 8px; background #fefefe `color.neutral.scale-50`; text ABC Diatype-75f05108b2d5df75 14/20 500, #1e1c1a `color.neutral.100`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f3f2ef `color.neutral.scale-200` |
| focus-visible | border 1px solid lab(66.128 -0.0000298023 0.0000119209) |
| pressed | background #f3f2ef `color.neutral.scale-200` |

![Text CTA default](components/crops/cta-link-default.png) ![Text CTA hover](components/crops/cta-link-hover.png) ![Text CTA focus-visible](components/crops/cta-link-focus-visible.png) ![Text CTA pressed](components/crops/cta-link-pressed.png)

#### Accordion trigger
A Cloud/On-premise deployment accordion header; toggled for its collapsed/expanded state. Read as `accordion-trigger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 514 x 74; padding 24px 0px; border 1px solid transparent; radius 8px; background transparent; text ABC Diatype-75f05108b2d5df75 16/24 500, #1e1c1a `color.neutral.100`; transition color 0.1s cubic-bezier(0.23, 1, 0.32, 1), background-color 0.1s cubic-bezier(0.23, 1, 0.32, 1), border-color 0.1s cubic-bezier(0.23, 1, 0.32, 1), outline-color 0.1s cubic-bezier(0.23, 1, 0.32, 1), text-decoration-color 0.1s cubic-bezier(0.23, 1, 0.32, 1), fill 0.1s cubic-bezier(0.23, 1, 0.32, 1), stroke 0.1s cubic-bezier(0.23, 1, 0.32, 1), --tw-gradient-from 0.1s cubic-bezier(0.23, 1, 0.32, 1), --tw-gradient-via 0.1s cubic-bezier(0.23, 1, 0.32, 1), --tw-gradient-to 0.1s cubic-bezier(0.23, 1, 0.32, 1); icon 24 x 24, #1e1c1a `color.neutral.100` |
| focus-visible | border 1px solid lab(66.128 -0.0000298023 0.0000119209); layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| selected | text ABC Diatype-75f05108b2d5df75 16/24 500, #525150 `color.neutral.60`; icon 24 x 24, #525150 `color.neutral.60` |

![Accordion trigger default](components/crops/accordion-trigger-default.png) ![Accordion trigger hover](components/crops/accordion-trigger-hover.png) ![Accordion trigger focus-visible](components/crops/accordion-trigger-focus-visible.png) ![Accordion trigger pressed](components/crops/accordion-trigger-pressed.png) ![Accordion trigger selected](components/crops/accordion-trigger-selected.png)

#### Accordion content
The expanded accordion region beside the deployment triggers. Read as `accordion-content` on the home page.

**Values (default).** size 514 x 224; background transparent; text ABC Diatype-75f05108b2d5df75 16/24 500, #525150 `color.neutral.60`; icon 24 x 24, #525150 `color.neutral.60`; layers div.border-border.not-last:border-b 514.0x75.0 B:1px solid rgb(228, 227, 219); button.focus-visible:border-focus.focus-visible:after:border-focus 514.0x74.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 8px; div.border-border.not-last:border-b 514.0x75.0 B:1px solid rgb(228, 227, 219); button.focus-visible:border-focus.foc.

Child layers that carry the look: div 514x75 border 1px solid #e4e3db `color.brand.canvas`; button 514x74 border 1px solid transparent radius 8px; div 514x75 border 1px solid #e4e3db `color.brand.canvas`.

![Accordion content default](components/crops/accordion-content-default.png)

#### Product row
The wide Managed-Agents product row link; measured never followed. Read as `product-row` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 1182 x 53.59; background transparent; text ABC Diatype-75f05108b2d5df75 16/16 500, #1e1c1a `color.neutral.100`; icon 16 x 16, #525150 `color.neutral.60` |
| focus-visible | outline 1px auto oklab(0.707999 -0.00000712276 0.0000166297 / 0.5), offset 1px; layers a.group.flex 1182.0x53.6 1px auto oklab(0.707999 -0.00000712276 0.0000166297 / 0.5) offset 1px |

![Product row default](components/crops/product-row-default.png) ![Product row hover](components/crops/product-row-hover.png) ![Product row focus-visible](components/crops/product-row-focus-visible.png) ![Product row pressed](components/crops/product-row-pressed.png)

### Product pages

The /sonic and /voices surfaces: product headlines and CTAs, use-case and voice chips, play buttons, the voices globe with its locale dots and voice rows.

#### Product headline
The Sonic product-page display headline. Read as `pd-h1` on the sonic page.

**Values (default).** size 745.33 x 92; background transparent; text PP Kyoto-b14c6ebb315b725b 40/46 500, oklab(0.227917 0.00188442 0.00454755 / 0.7).

![Product headline default](components/crops/pd-h1-default.png)

#### Product CTA
The "Try Sonic-3.6" hero action; measured never followed. Read as `pd-cta` on the sonic page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 124.38 x 40; padding 0px 20px; border 1px solid transparent; radius 8px; background #309d4b `color.brand.verdant`; text ABC Diatype-75f05108b2d5df75 14/20 500, #f9f9f8 `color.neutral.scale-100`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background oklab(0.615694 -0.130896 0.0819391 / 0.9) |
| focus-visible | border 1px solid lab(66.128 -0.0000298023 0.0000119209) |
| pressed | background oklab(0.615694 -0.130896 0.0819391 / 0.9) |

![Product CTA default](components/crops/pd-cta-default.png) ![Product CTA hover](components/crops/pd-cta-hover.png) ![Product CTA focus-visible](components/crops/pd-cta-focus-visible.png) ![Product CTA pressed](components/crops/pd-cta-pressed.png)

#### Secondary CTA
The Contact-Sales hero action; measured never followed. Read as `pd-secondary` on the sonic page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 130.08 x 40; padding 0px 20px; border 1px solid #e4e3db `color.brand.canvas`; radius 8px; background #fefefe `color.neutral.scale-50`; text ABC Diatype-75f05108b2d5df75 14/20 500, #1e1c1a `color.neutral.100`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f3f2ef `color.neutral.scale-200` |
| focus-visible | border 1px solid lab(66.128 -0.0000298023 0.0000119209) |
| pressed | background #f3f2ef `color.neutral.scale-200` |

![Secondary CTA default](components/crops/pd-secondary-default.png) ![Secondary CTA hover](components/crops/pd-secondary-hover.png) ![Secondary CTA focus-visible](components/crops/pd-secondary-focus-visible.png) ![Secondary CTA pressed](components/crops/pd-secondary-pressed.png)

#### Use-case chip
A demo use-case chip in the voice demo; toggled for its selected state (switches the demo script, nothing sent). Read as `usecase-chip` on the sonic page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 144.13 x 30; padding 6px 12px; border 1px solid #e4e3db `color.brand.canvas`; radius 3.35544e+07px; background #fefefe `color.neutral.scale-50`; text ABC Diatype-75f05108b2d5df75 12/16 400, #525150 `color.neutral.60`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 14 x 14, #525150 `color.neutral.60` |
| hover | text ABC Diatype-75f05108b2d5df75 12/16 400, #1e1c1a `color.neutral.100`; icon 14 x 14, #1e1c1a `color.neutral.100` |
| focus-visible | outline 1px auto oklab(0.707999 -0.00000712276 0.0000166297 / 0.5), offset 0px |
| pressed, selected | text ABC Diatype-75f05108b2d5df75 12/16 400, #1e1c1a `color.neutral.100`; icon 14 x 14, #1e1c1a `color.neutral.100` |

![Use-case chip default](components/crops/usecase-chip-default.png) ![Use-case chip hover](components/crops/usecase-chip-hover.png) ![Use-case chip focus-visible](components/crops/usecase-chip-focus-visible.png) ![Use-case chip pressed](components/crops/usecase-chip-pressed.png) ![Use-case chip selected](components/crops/usecase-chip-selected.png)

#### Voice/locale chip
A rounded-full locale or voice picker chip in the demo bar. Read as `voice-chip` on the sonic page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 118.19 x 34; padding 6px 12px; border 1px solid #e4e3db `color.brand.canvas`; radius 3.35544e+07px; background oklab(0.981786 -0.000328958 0.0012871 / 0.5); text ABC Diatype-75f05108b2d5df75 14/20 500, #1e1c1a `color.neutral.100`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #1e1c1a `color.neutral.100` |
| hover | background lab(95.4982 -0.0449121 1.52447) |
| focus-visible | outline 1px auto oklab(0.707999 -0.00000712276 0.0000166297 / 0.5), offset 0px |
| pressed | background lab(95.4982 -0.0449121 1.52447) |

![Voice/locale chip default](components/crops/voice-chip-default.png) ![Voice/locale chip hover](components/crops/voice-chip-hover.png) ![Voice/locale chip focus-visible](components/crops/voice-chip-focus-visible.png) ![Voice/locale chip pressed](components/crops/voice-chip-pressed.png)

#### Play button
The demo Play action; measured, never pressed. Read as `play-btn` on the sonic page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 59.91 x 36; padding 0px 16px; border 1px solid transparent; radius 8px; background #309d4b `color.brand.verdant`; text ABC Diatype-75f05108b2d5df75 14/20 400, #f9f9f8 `color.neutral.scale-100`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background oklab(0.615694 -0.130896 0.0819391 / 0.9) |
| focus-visible | border 1px solid lab(66.128 -0.0000298023 0.0000119209) |
| pressed | background oklab(0.615694 -0.130896 0.0819391 / 0.9) |

![Play button default](components/crops/play-btn-default.png) ![Play button hover](components/crops/play-btn-hover.png) ![Play button focus-visible](components/crops/play-btn-focus-visible.png) ![Play button pressed](components/crops/play-btn-pressed.png)

#### Sample play button
A 32px square play button on a pronunciation/clone sample (icon-only, aria-labelled); measured, never pressed. Read as `word-play` on the sonic page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; border 1px solid #f3f2ef `color.neutral.scale-200`; radius 3.35544e+07px; background #fefefe `color.neutral.scale-50`; text ABC Diatype-75f05108b2d5df75 16/24 400, #1e1c1a `color.neutral.100`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 14 x 14, #1e1c1a `color.neutral.100` |
| hover | background #f3f2ef `color.neutral.scale-200` |
| focus-visible | outline 2px solid #309d4b `color.brand.verdant`, offset 2px |
| pressed | background #f3f2ef `color.neutral.scale-200` |

![Sample play button default](components/crops/word-play-default.png) ![Sample play button hover](components/crops/word-play-hover.png) ![Sample play button focus-visible](components/crops/word-play-focus-visible.png) ![Sample play button pressed](components/crops/word-play-pressed.png)

#### Voice row
A "voice — locale" row in the voice list (group flex row with a play affordance). Read as `voice-row` on the sonic page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 329.33 x 48; padding 12px 8px; background transparent; text ABC Diatype-75f05108b2d5df75 16/22 400, #1e1c1a `color.neutral.100`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 12 x 12, #1e1c1a `color.neutral.100`; layers span.flex.shrink-0 24.0x24.0 rgb(254, 254, 254) T:1px solid rgb(243, 242, 239) / R:1px solid rgb(243, 242, 239) / B:1px solid rgb(243, 242, 239) / L:1px solid rgb(243, 242, 239) 3.35544e+07px |
| hover | background #f3f2ef `color.neutral.scale-200`; layers none |
| focus-visible | outline 2px solid #309d4b `color.brand.verdant`, offset 2px; layers button.group.flex 329.3x48.0 2px solid rgb(48, 157, 75) offset 2px; span.flex.shrink-0 24.0x24.0 rgb(254, 254, 254) T:1px solid rgb(243, 242, 239) / R:1px solid rgb(243, 242, 239) / B:1px solid rgb(243, 242, 239) / L:1px solid rgb(243, 242, 239) 3.35544e+07px |
| pressed | background #f3f2ef `color.neutral.scale-200`; layers none |

Child layers that carry the look: span 24x24 background #fefefe `color.neutral.scale-50` border 1px solid #f3f2ef `color.neutral.scale-200` radius 3.35544e+07px.

![Voice row default](components/crops/voice-row-default.png) ![Voice row hover](components/crops/voice-row-hover.png) ![Voice row focus-visible](components/crops/voice-row-focus-visible.png) ![Voice row pressed](components/crops/voice-row-pressed.png)

#### Voices headline
The "Find your voice." display headline. Read as `voices-h1` on the voices page.

**Values (default).** size 315.7 x 28; background transparent; text PP Kyoto-b14c6ebb315b725b 40/46 500, #1e1c1a `color.neutral.100`.

![Voices headline default](components/crops/voices-h1-default.png)

#### Globe locale dot
A locale dot on the voices globe; toggled, never dragged. Read as `globe-dot` on the voices page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 19.08 x 19.08; border 1px solid rgba(197, 194, 188, 0.9); radius 50%; background rgba(30, 28, 26, 0.7); text ABC Diatype-75f05108b2d5df75 16/24 400, #1e1c1a `color.neutral.100`; layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| focus-visible | outline 2px solid lab(66.128 -0.0000298023 0.0000119209), offset 2px |

![Globe locale dot default](components/crops/globe-dot-default.png) ![Globe locale dot hover](components/crops/globe-dot-hover.png) ![Globe locale dot focus-visible](components/crops/globe-dot-focus-visible.png) ![Globe locale dot pressed](components/crops/globe-dot-pressed.png)

#### Globe play
The round play button inside the voices globe; measured, never pressed. Read as `globe-play` on the voices page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 81 x 81; background transparent; text ABC Diatype-75f05108b2d5df75 16/24 400, #1e1c1a `color.neutral.100`; icon 24 x 24, #1e1c1a `color.neutral.100`; layers span.voices-globe-play-ring 81.0x81.0 T:1px solid rgb(254, 254, 254) / R:1px solid rgb(254, 254, 254) / B:1px solid rgb(254, 254, 254) / L:1px solid rgb(254, 254, 254) 50%; span.voices-globe-play-disc 64.2x64.2 rgb(254, 254, 254) 50% |
| focus-visible | outline 2px solid lab(66.128 -0.0000298023 0.0000119209), offset 2px; layers button.voices-globe-play 81.0x81.0 2px solid lab(66.128 -0.0000298023 0.0000119209) offset 2px; span.voices-globe-play-ring 81.0x81.0 T:1px solid rgb(254, 254, 254) / R:1px solid rgb(254, 254, 254) / B:1px solid rgb(254, 254, 254) / L:1px solid rgb(254, 254, 254) 50%; span.voices-globe-play-disc 64.2x64.2 rgb(254, 254, 254) 50% |

Child layers that carry the look: span 81x81 border 1px solid #fefefe `color.neutral.scale-50` radius 50%; span 64.2x64.2 background #fefefe `color.neutral.scale-50` radius 50%.

![Globe play default](components/crops/globe-play-default.png) ![Globe play hover](components/crops/globe-play-hover.png) ![Globe play focus-visible](components/crops/globe-play-focus-visible.png) ![Globe play pressed](components/crops/globe-play-pressed.png)

#### Locale arrow
A previous/next-locale arrow in the globe panel. Read as `globe-arrow` on the voices page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; background transparent; text ABC Diatype-75f05108b2d5df75 16/24 400, #1e1c1a `color.neutral.100`; icon 16 x 16, #1e1c1a `color.neutral.100`; layers ::before rgb(254, 254, 254) 0px none 1; button::before.voices-globe-arrow 32pxx32px rgb(254, 254, 254) 50% |
| hover | layers ::before rgb(243, 242, 239) 0px none 1; button::before.voices-globe-arrow 32pxx32px rgb(243, 242, 239) 50% |
| focus-visible | outline 2px solid lab(66.128 -0.0000298023 0.0000119209), offset 2px; layers ::before rgb(254, 254, 254) 0px none 1; button.voices-globe-arrow 32.0x32.0 2px solid lab(66.128 -0.0000298023 0.0000119209) offset 2px; button::before.voices-globe-arrow 32pxx32px rgb(254, 254, 254) 50% |
| pressed | layers ::before rgb(243, 242, 239) 0px none 1; button::before.voices-globe-arrow 32pxx32px rgb(243, 242, 239) 50% |

Child layers that carry the look: button::before 32pxx32px background #fefefe `color.neutral.scale-50` radius 50%.

![Locale arrow default](components/crops/globe-arrow-default.png) ![Locale arrow hover](components/crops/globe-arrow-hover.png) ![Locale arrow focus-visible](components/crops/globe-arrow-focus-visible.png) ![Locale arrow pressed](components/crops/globe-arrow-pressed.png)

#### Globe voice row
A "voice + persona" row in the globe voice list. Read as `globe-voice` on the voices page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 244.09 x 38; padding 6px 10px; radius 4px; background transparent; text ABC Diatype-75f05108b2d5df75 14/19.6 400, #525150 `color.neutral.60`; icon 12 x 12, #1e1c1a `color.neutral.100`; layers span.flex.rounded-full 26.0x26.0 rgb(254, 254, 254) T:1px solid rgb(243, 242, 239) / R:1px solid rgb(243, 242, 239) / B:1px solid rgb(243, 242, 239) / L:1px solid rgb(243, 242, 239) 3.35544e+07px; ancestor paint `div.hidden.flex-col`: background #fefefe `color.neutral.scale-50`; radius 8px; shadow rgba(0, 0, 0, 0.1) 0px 2px 8px 0px |
| hover | background #f3f2ef `color.neutral.scale-200`; text ABC Diatype-75f05108b2d5df75 14/19.6 400, #1e1c1a `color.neutral.100`; layers none |
| focus-visible | outline 2px solid lab(66.128 -0.0000298023 0.0000119209), offset 2px; layers button.voices-globe-voice.flex 244.1x38.0 2px solid lab(66.128 -0.0000298023 0.0000119209) offset 2px 4px; span.flex.rounded-full 26.0x26.0 rgb(254, 254, 254) T:1px solid rgb(243, 242, 239) / R:1px solid rgb(243, 242, 239) / B:1px solid rgb(243, 242, 239) / L:1px solid rgb(243, 242, 239) 3.35544e+07px |
| pressed | background #f3f2ef `color.neutral.scale-200`; text ABC Diatype-75f05108b2d5df75 14/19.6 400, #1e1c1a `color.neutral.100`; layers none |

Child layers that carry the look: span 26x26 background #fefefe `color.neutral.scale-50` border 1px solid #f3f2ef `color.neutral.scale-200` radius 3.35544e+07px.

![Globe voice row default](components/crops/globe-voice-default.png) ![Globe voice row hover](components/crops/globe-voice-hover.png) ![Globe voice row focus-visible](components/crops/globe-voice-focus-visible.png) ![Globe voice row pressed](components/crops/globe-voice-pressed.png)

### Pricing

The pricing surface: the four plan cards with their CTAs, the usage-slider calculator and the details/summary FAQ items.

#### Pricing title
The pricing page display heading. Read as `pricing-h1` on the pricing page.

**Values (default).** size 745.33 x 46; background transparent; text PP Kyoto-b14c6ebb315b725b 40/46 500, oklab(0.227917 0.00188442 0.00454755 / 0.7).

![Pricing title default](components/crops/pricing-h1-default.png)

#### Plan group name
A plan group heading (Text to Speech / Speech to Text / Voice Agents). Read as `plan-name` on the pricing page.

**Values (default).** size 132.16 x 26; background transparent; text ABC Diatype-75f05108b2d5df75 20/26 465, #1e1c1a `color.neutral.100`.

![Plan group name default](components/crops/plan-name-default.png)

#### Plan CTA
A plan card's "Start free" action; measured never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 206.8 x 36; padding 6px 12px; border 1px solid #e4e3db `color.brand.canvas`; radius 8px; background #fefefe `color.neutral.scale-50`; text ABC Diatype-75f05108b2d5df75 14/19.25 500, #1e1c1a `color.neutral.100`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f3f2ef `color.neutral.scale-200` |
| focus-visible | border 1px solid lab(66.128 -0.0000298023 0.0000119209) |
| pressed | background #f3f2ef `color.neutral.scale-200` |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Plan CTA alt
A secondary plan action ("Select Startup"/"Contact us"); measured never followed. Read as `plan-cta-alt` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 206.8 x 36; padding 6px 12px; border 1px solid #e4e3db `color.brand.canvas`; radius 8px; background #fefefe `color.neutral.scale-50`; text ABC Diatype-75f05108b2d5df75 14/19.25 500, #1e1c1a `color.neutral.100`; transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #f3f2ef `color.neutral.scale-200` |
| focus-visible | border 1px solid lab(66.128 -0.0000298023 0.0000119209) |
| pressed | background #f3f2ef `color.neutral.scale-200` |

![Plan CTA alt default](components/crops/plan-cta-alt-default.png) ![Plan CTA alt hover](components/crops/plan-cta-alt-hover.png) ![Plan CTA alt focus-visible](components/crops/plan-cta-alt-focus-visible.png) ![Plan CTA alt pressed](components/crops/plan-cta-alt-pressed.png)

#### Plan card
A pricing plan card (the painted cell holding the plan CTA, ring-1 bg-background). Read as `plan-card` on the pricing page.

**Values (default).** size 254.8 x 543.25; padding 40px 24px; background #fefefe `color.neutral.scale-50`; shadow #e4e3db 0px 0px 0px 1px; text IBM Plex Mono-1f31a4fbe8ce28fa 12/16.5 500, #a7a6a2 `color.neutral.scale-600`; icon 14 x 14, #309d4b `color.brand.verdant`.

![Plan card default](components/crops/plan-card-default.png)

#### FAQ item
An FAQs details/summary row (the summary toggles its own answer). Read as `faq-trigger` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed, selected) | size 852.02 x 102.75; padding 56px 48px 24px 48px; background transparent; text ABC Diatype-75f05108b2d5df75 14/22.75 500, #1e1c1a `color.neutral.100`; icon 16 x 16, #525150 `color.neutral.60` |
| focus-visible | outline 2px solid lab(66.128 -0.0000298023 0.0000119209), offset -2px; layers summary.faq-summary.flex 852.0x102.8 2px solid lab(66.128 -0.0000298023 0.0000119209) offset -2px |

![FAQ item default](components/crops/faq-trigger-default.png) ![FAQ item hover](components/crops/faq-trigger-hover.png) ![FAQ item focus-visible](components/crops/faq-trigger-focus-visible.png) ![FAQ item pressed](components/crops/faq-trigger-pressed.png) ![FAQ item selected](components/crops/faq-trigger-selected.png)

#### Plan tab
A plan tab in the compare strip (Free/Pro/Startup/Scale/Enterprise); toggled for its selected state, never checked out. Read as `plan-tab` on the pricing page.

Not on the page when it was captured.

#### Usage slider
The "Minutes of generated audio per month" range input in the cost calculator; focused only, never dragged. Read as `plan-slider` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 556.5 x 46; background transparent; text ABC Diatype-75f05108b2d5df75 16/24 400, #1e1c1a `color.neutral.100`; opacity 0; placeholder #1e1c1a `color.neutral.100`; ancestor paint `div.relative.h-12`: background #f3f2ef `color.neutral.scale-200`; radius 4px |

![Usage slider default](components/crops/plan-slider-default.png) ![Usage slider focused](components/crops/plan-slider-focused.png)

### Playground sign-in boundary

The auth boundary on play.cartesia.ai, measured but never filled or submitted: the 640px sign-in and sign-up columns, fields and SSO/passkey buttons — a Clerk app sharing the same token layer.

#### Sign-in card
The centred sign-in column on play.cartesia.ai (the boundary before the gated playground); never filled or submitted. Read as `login-card` on the sign-in page.

**Values (default).** size 640 x 727.5; padding 144px 0px 40px 0px; background transparent; text sans 30/36 500, lab(22.1595 1.49098 3.94592); icon 20 x 20, lab(22.1595 1.49098 3.94592); layers button.focus-visible:border-focus.aria-invalid:ring-destructive/20 206.0x44.0 lab(97.9206 -0.0992119 0.364304) T:1px solid lab(87.8444 0.427336 3.02215) / R:1px solid lab(87.8444 0.427336 3.02215) / B:1px solid lab(87.8444 0.427336 3.02215) / L:1px solid lab(87.8444 0.427336 3.02215) 12px; button.focus-visible:border-focus.aria-invalid:ring-destructive/20 206.0x44.0 lab(97.9206 -0.0992119 0.364304.

Child layers that carry the look: button 206x44 background lab(97.9206 -0.0992119 0.364304) border 1px solid lab(87.8444 0.427336 3.02215) radius 12px; button 206x44 background lab(97.9206 -0.0992119 0.364304) border 1px solid lab(87.8444 0.427336 3.02215) radius 12px; span 192.5x1 background lab(87.8444 0.427336 3.02215).

![Sign-in card default](components/crops/login-card-default.png)

#### Email field
The email-address input; sample text was typed and deleted, nothing sent. Read as `email-field` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 420 x 44; padding 4px 14px; border 1px solid lab(87.8444 0.427336 3.02215); radius 8px; background lab(100 0 0); text sans 14/21 400, lab(22.1595 1.49098 3.94592); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder oklab(0.495999 0.000279129 0.00299793 / 0.55) |
| focused, filled | border 1px solid lab(66.128 -0.0000298023 0.0000119209) |

![Email field default](components/crops/email-field-default.png) ![Email field focused](components/crops/email-field-focused.png) ![Email field filled](components/crops/email-field-filled.png)

#### Continue button
The Continue submit; measured, never pressed (a press would submit the form). Read as `continue-btn` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 420 x 44; padding 0px 24px; border 1px solid transparent; radius 12px; background lab(28.2787 -30.6481 19.0677); text sans 15/20 400, lab(99.652 0 0); transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background oklab(0.370998 -0.0869163 0.0473948 / 0.9) |
| focus-visible | border 1px solid lab(66.128 -0.0000298023 0.0000119209) |
| pressed | background oklab(0.370998 -0.0869163 0.0473948 / 0.9) |

![Continue button default](components/crops/continue-btn-default.png) ![Continue button hover](components/crops/continue-btn-hover.png) ![Continue button focus-visible](components/crops/continue-btn-focus-visible.png) ![Continue button pressed](components/crops/continue-btn-pressed.png)

#### SSO button
An OAuth button beside the form (labelled "Continue with Google"/"Continue with GitHub" when the labels render); measured, never followed. Read as `sso-btn` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 206 x 44; padding 0px 24px; border 1px solid lab(87.8444 0.427336 3.02215); radius 12px; background lab(97.9206 -0.0992119 0.364304); text sans 15/20 500, lab(22.1595 1.49098 3.94592); transition all 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, lab(22.1595 1.49098 3.94592) |
| hover | background lab(94.8115 -0.162512 1.89852) |
| focus-visible | border 1px solid lab(66.128 -0.0000298023 0.0000119209) |
| pressed | background lab(94.8115 -0.162512 1.89852) |

![SSO button default](components/crops/sso-btn-default.png) ![SSO button hover](components/crops/sso-btn-hover.png) ![SSO button focus-visible](components/crops/sso-btn-focus-visible.png) ![SSO button pressed](components/crops/sso-btn-pressed.png)

#### Passkey button
The "Sign in with a passkey" text action; measured, never pressed. Read as `passkey-btn` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 137.3 x 22; border 1px solid transparent; radius 4px; background transparent; text sans 14/20 400, lab(41.5479 0.0899583 1.14084) |
| hover | text sans 14/20 400, lab(22.1595 1.49098 3.94592) |
| focus-visible | border 1px solid lab(66.128 -0.0000298023 0.0000119209) |
| pressed | text sans 14/20 400, lab(22.1595 1.49098 3.94592) |

![Passkey button default](components/crops/passkey-btn-default.png) ![Passkey button hover](components/crops/passkey-btn-hover.png) ![Passkey button focus-visible](components/crops/passkey-btn-focus-visible.png) ![Passkey button pressed](components/crops/passkey-btn-pressed.png)

#### Signup card
The centred create-account column (/sign-in/create); never filled or submitted. Read as `signup-card` on the sign-up page.

**Values (default).** size 640 x 727.5; padding 144px 0px 40px 0px; background transparent; text sans 30/36 500, lab(22.1595 1.49098 3.94592); icon 20 x 20, lab(22.1595 1.49098 3.94592); layers button.focus-visible:border-focus.aria-invalid:ring-destructive/20 206.0x44.0 lab(97.9206 -0.0992119 0.364304) T:1px solid lab(87.8444 0.427336 3.02215) / R:1px solid lab(87.8444 0.427336 3.02215) / B:1px solid lab(87.8444 0.427336 3.02215) / L:1px solid lab(87.8444 0.427336 3.02215) 12px; button.focus-visible:border-focus.aria-invalid:ring-destructive/20 206.0x44.0 lab(97.9206 -0.0992119 0.364304.

Child layers that carry the look: button 206x44 background lab(97.9206 -0.0992119 0.364304) border 1px solid lab(87.8444 0.427336 3.02215) radius 12px; button 206x44 background lab(97.9206 -0.0992119 0.364304) border 1px solid lab(87.8444 0.427336 3.02215) radius 12px; span 192.5x1 background lab(87.8444 0.427336 3.02215).

![Signup card default](components/crops/signup-card-default.png)

#### Signup email field
The signup email input; focused only, never filled or submitted. Read as `signup-field` on the sign-up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 420 x 44; padding 4px 14px; border 1px solid lab(87.8444 0.427336 3.02215); radius 8px; background lab(100 0 0); text sans 14/21 400, lab(22.1595 1.49098 3.94592); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); placeholder oklab(0.495999 0.000279129 0.00299793 / 0.55) |
| focused | border 1px solid lab(66.128 -0.0000298023 0.0000119209) |

![Signup email field default](components/crops/signup-field-default.png) ![Signup email field focused](components/crops/signup-field-focused.png)

### Docs (Mintlify surface)

The public docs landing on docs.cartesia.ai: a separate Mintlify application in Inter, measured for reference; its tokens are kept out of the export.

#### Docs header
The Mintlify docs top bar (wordmark, Search ⌘K, Log In / Playground links). Read as `docs-header` on the docs page.

**Values (default).** size 1440 x 96; background transparent; text Inter 14/20 500, #181b19; icon 12 x 12, #9fa3a0; layers div.z-10.absolute 1440.0x96.0 B:1px solid rgb(239, 242, 240); div.z-0.absolute 1440.0x96.0 rgb(249, 249, 248); button.group/search.flex 277.6x36.0 oklab(0.159497 -0.00587773 0.0025713 / 0.03) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0.711296 -0.00557929 0.00278378 / 0.3) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 9999px; but.

Child layers that carry the look: div 1440x96 border 1px solid #eff2f0; div 1440x96 background #f9f9f8 `color.neutral.scale-100`; button 277.6x36 background oklab(0.159497 -0.00587773 0.0025713 / 0.03) radius 9999px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, oklab(0.711296 -0.00557929 0.00278378 / 0.3) 0px 0px 0px 0px, transparent 0px 0px 0px 0px.

![Docs header default](components/crops/docs-header-default.png)

#### Search button
The "Search… ⌘K" docs search input; measured, never opened. Read as `docs-search` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 277.56 x 36; padding 0px 12px 0px 14px; radius 9999px; background oklab(0.159497 -0.00587773 0.0025713 / 0.03); shadow oklab(0.711296 -0.00557929 0.00278378 / 0.3) 0px 0px 0px 0px; text Inter 14/24 400, #717472; icon 16 x 16, #404340 |
| hover | background oklab(0.159497 -0.00587773 0.0025713 / 0.1); shadow oklab(0.442478 -0.00459664 0.0019649 / 0.3) 0px 0px 0px 0px; icon 16 x 16, #262a27 |
| focus-visible | outline 1px auto #309d4b `color.brand.verdant`, offset 0px |
| pressed | background oklab(0.159497 -0.00587773 0.0025713 / 0.1); shadow oklab(0.442478 -0.00459664 0.0019649 / 0.3) 0px 0px 0px 0px; icon 16 x 16, #262a27 |

![Search button default](components/crops/docs-search-default.png) ![Search button hover](components/crops/docs-search-hover.png) ![Search button focus-visible](components/crops/docs-search-focus-visible.png) ![Search button pressed](components/crops/docs-search-pressed.png)

#### Docs nav item
A sidebar navigation link in the docs app. Read as `docs-nav-item` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 268 x 32; padding 6px 12px 6px 16px; radius 12px; background transparent; text Inter 14/20 400, #404340; icon 16 x 16, #404340; layers svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 16.0x16.0 rgb(159, 163, 160) |
| hover | background oklab(0.442478 -0.00459664 0.0019649 / 0.05); text Inter 14/20 400, #181b19; icon 16 x 16, #181b19; layers none |
| focus-visible | outline 1px auto #309d4b `color.brand.verdant`, offset -2px; layers a.group.flex 268.0x32.0 1px auto rgb(48, 157, 75) offset -2px 12px; svg.forced-colors:forced-color-adjust-none.forced-colors:bg-[color:CanvasText]! 16.0x16.0 rgb(159, 163, 160) |
| pressed | background oklab(0.442478 -0.00459664 0.0019649 / 0.05); text Inter 14/20 400, #181b19; icon 16 x 16, #181b19; layers none |

Child layers that carry the look: svg 16x16 background #9fa3a0.

![Docs nav item default](components/crops/docs-nav-item-default.png) ![Docs nav item hover](components/crops/docs-nav-item-hover.png) ![Docs nav item focus-visible](components/crops/docs-nav-item-focus-visible.png) ![Docs nav item pressed](components/crops/docs-nav-item-pressed.png)

#### Docs title
The docs page title (Inter, docs-platform type — a separate surface from the marketing fonts). Read as `docs-h1` on the docs page.

**Values (default).** size 343.19 x 40; background transparent; text Inter 36/40 600, #181b19.

![Docs title default](components/crops/docs-h1-default.png)

### Footer

The marketing footer: link columns on the light field.

#### Footer
The footer: link columns (Products/Company/Capabilities/Use cases/Industries/Resources), legal and social. Read as `footer` on the home page.

**Values (default).** size 1278 x 767; background transparent; text ABC Diatype-75f05108b2d5df75 15/24 400, #525150 `color.neutral.60`; layers div.flex.flex-col 304.3x684.0 R:1px solid rgb(228, 227, 219); a.rounded-sm.border 146.0x22.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 4px; a.flex.size-6 24.0x24.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 4px; a.flex.size-6 24.0x24.0 T:1px.

Child layers that carry the look: div 304.3x684 border 1px solid #e4e3db `color.brand.canvas`; a 146x22 border 1px solid transparent radius 4px; a 24x24 border 1px solid transparent radius 4px.

![Footer default](components/crops/footer-default.png)

#### Footer link
Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 39.88 x 30; padding 4px 0px; border 1px solid transparent; radius 4px; background transparent; text ABC Diatype-75f05108b2d5df75 15/20 400, #525150 `color.neutral.60`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | text ABC Diatype-75f05108b2d5df75 15/20 400, #1e1c1a `color.neutral.100` |
| focus-visible | border 1px solid lab(66.128 -0.0000298023 0.0000119209) |
| pressed | text ABC Diatype-75f05108b2d5df75 15/20 400, #1e1c1a `color.neutral.100` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Footer column head
A footer column heading (17px font-sans medium). Read as `footer-col-head` on the home page.

**Values (default).** size 146.67 x 24; background transparent; text ABC Diatype-75f05108b2d5df75 17/24 465, #1e1c1a `color.neutral.100`; ancestor paint `div.relative.bg-background`: background #fefefe `color.neutral.scale-50`; shadow #e4e3db 0px 0px 0px 1px.

![Footer column head default](components/crops/footer-col-head-default.png)

### Mobile (390 wide)

The marketing surface at phone width: the compact header, the full-height menu overlay and the stacked 32px hero.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 64; border B: 1px solid #e4e3db `color.brand.canvas`; background #fefefe `color.neutral.scale-50`; text ABC Diatype-75f05108b2d5df75 14/20 500, #f9f9f8 `color.neutral.scale-100`.

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
The header "Open menu" toggle. Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 36 x 36; radius 8px; background transparent; text ABC Diatype-75f05108b2d5df75 16/24 400, #1e1c1a `color.neutral.100`; icon 16 x 16, #1e1c1a `color.neutral.100`.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The header menu panel opened by its own toggle. Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 844; padding 64px 0px 0px 0px; background #fefefe `color.neutral.scale-50`; text ABC Diatype-75f05108b2d5df75 18/28 500, #1e1c1a `color.neutral.100`; transition opacity 0.2s cubic-bezier(0, 0, 0.2, 1), translate 0.2s cubic-bezier(0, 0, 0.2, 1), visibility 0.2s cubic-bezier(0, 0, 0.2, 1); icon 16 x 16, #525150 `color.neutral.60`.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Mobile nav item
An item inside the opened header menu. Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 356 x 56; padding 14px 16px; background transparent; text ABC Diatype-75f05108b2d5df75 18/28 500, #1e1c1a `color.neutral.100`; icon 16 x 16, #525150 `color.neutral.60` |
| focus-visible | outline 1px auto oklab(0.707999 -0.00000712276 0.0000166297 / 0.5), offset 0px; layers button.px-4.md:px-8 356.0x56.0 1px auto oklab(0.707999 -0.00000712276 0.0000166297 / 0.5) offset 0px |

![Mobile nav item default](components/crops/m-nav-item-default.png) ![Mobile nav item hover](components/crops/m-nav-item-hover.png) ![Mobile nav item focus-visible](components/crops/m-nav-item-focus-visible.png) ![Mobile nav item pressed](components/crops/m-nav-item-pressed.png)

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 308 x 183.98; background transparent; text PP Kyoto-b14c6ebb315b725b 32/36.8 500, oklab(0.227917 0.00188442 0.00454755 / 0.7).

![Mobile headline default](components/crops/m-hero-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Cartesia wordmark, the SSO glyphs, product illustrations and the docs app's glyphs) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Cartesia's product — the voice playground, text-to-speech console, voice cloning and management, agents, API keys, usage and billing — lives behind the sign-in on play.cartesia.ai and was never reached; only the public Clerk sign-in and sign-up cards were measured (never filled or submitted). The signed-out voice demos on /sonic and /voices were captured as far as their own play controls go; no audio was generated, and the Talk to Skylar / Talk to Cartesia live-agent calls were never started.

### Pages

- **The playground.** Every post-login surface (the Sonic playground, voice library management, agents, files, API keys, billing) needs an account and was never reached; /sign-in and /sign-in/create were captured as forms and never filled or submitted.
- **The docs app.** docs.cartesia.ai is public and was captured (landing, search, nav, title), but it is a separate Mintlify application — its Inter face and its own token layer are kept in raw/css-vars-docs.json, not merged into the export.
- **Checkout and onboarding.** Every Try Cartesia, Talk to Sales and plan CTA was measured, never followed past its public landing.
- **Discovered but unshot routes.** The footer and nav link out to /company, /integrations, /startups and the /product/* SEO pages (ai-dubbing, ai-voice-enhancer, ai-voiceover, python-text-to-speech-api-tts, realistic-text-to-speech, speech-synthesis, text-to-speech-mp3, voice-conversion, voice-reader), plus /speech-to-text-api and /voice-changer; none was captured as a screenshot.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **plan-tab** is recorded missing: the pricing plan tabs rendered zero-size/lazy-mounted at capture time — an honest miss, not a measured absence.
- **Disabled, error and loading states** were not seen on the public surface.
- **Focus-visible** on the marketing controls draws a 2px solid #a1a1a1 (--ring) outline; voice-list rows ring in verdant #309d4b.
- **Live audio states** (playing, paused, waveform progress) were never captured — play controls were pressed only to read their default/hover/focus styling.

### Themes

cartesia.ai is three surfaces, not a theme toggle: the marketing site paints light and declares a `.dark` scope that re-binds the same semantic roles (verdant primary becomes growth, borders become white alphas — captured in the dark set); the sign-in card paints light; and the docs app is a Mintlify surface kept out of the export.

### Fonts

- **ABC Diatype** (body text, nav, buttons and UI), **PP Kyoto** (display headlines), **IBM Plex Mono** (code and figures) and **Homemade Apple** (handwriting accents) are the marketing site's declared faces; the docs app uses Inter. The style guide falls back to system sans.

### Screenshots

- Product illustrations, demo art, the Cartesia wordmark and customer logos in the screenshots are the product's published content.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Marketing copy, customer stories and the demo voices' names and text are the product's content; only frames and components were measured.
