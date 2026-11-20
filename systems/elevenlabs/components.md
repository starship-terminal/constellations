# ElevenLabs components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from elevenlabs.io on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, created, submitted or paid for; the auth cards were measured and their fields focused, never completed; the Sign up, checkout and OAuth actions were never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (71 components, 172 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (170 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every captured surface paints `light`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [agents-tab](screenshots/home-light-agents-tab.png), [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png), [playground-play](screenshots/home-light-playground-play.png), [playground](screenshots/home-light-playground.png) |
| Pricing | `/pricing` | [billing](screenshots/pricing-light-billing.png), [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| Text to Speech | `/text-to-speech` | [default](screenshots/text-to-speech-light-default.png), [full](screenshots/text-to-speech-light-full.png) |
| Conversational AI | `/conversational-ai` | [default](screenshots/conversational-ai-light-default.png), [full](screenshots/conversational-ai-light-full.png) |
| Sound Effects | `/sound-effects` | [default](screenshots/sound-effects-light-default.png), [full](screenshots/sound-effects-light-full.png) |
| API for developers | `/api` | [default](screenshots/api-light-default.png), [full](screenshots/api-light-full.png) |
| Documentation | `/docs` | [default](screenshots/docs-light-default.png), [full](screenshots/docs-light-full.png) |
| About | `/about` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Enterprise | `/enterprise` | [default](screenshots/enterprise-light-default.png), [full](screenshots/enterprise-light-full.png) |
| Blog | `/blog` | [default](screenshots/blog-light-default.png) |
| Sign in card | `/app/sign-in` | [default](screenshots/sign-in-light-default.png) |
| Sign up card | `/app/sign-up` | [default](screenshots/sign-up-light-default.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Pricing, phone | `/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| Text to Speech, phone | `/text-to-speech` | [default](screenshots/mobile-text-to-speech-light-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Mobile menu overlay | home, phone width | the header menu button's own toggle | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png), [m-menu-open](#mobile-menu-open), [m-nav-item](#mobile-nav-item), [m-signup](#mobile-sign-up) |
| Products mega-menu | home | the Products trigger's own click | [home-light-menu](screenshots/home-light-menu.png), [nav-dropdown](#nav-flyout), [menu-link](#flyout-link) |
| Hero product tab | home | the ElevenAgents tab's own click | [home-light-agents-tab](screenshots/home-light-agents-tab.png), [product-tab](#product-tab), [tool-tab](#tool-tab) |
| TTS playground | home | the demo's own textarea and Play button — typed into; Play pressed once in the shot pass, generating without an account | [home-light-playground](screenshots/home-light-playground.png), [home-light-playground-play](screenshots/home-light-playground-play.png), [tts-card](#playground-card), [tts-textarea](#playground-textarea), [tts-play](#play-button) |
| Billing dropdown | /pricing | the Monthly billing dropdown's own toggle | [pricing-light-billing](screenshots/pricing-light-billing.png), [billing-select](#billing-dropdown) |
| Voice-chat launcher | home and product pages | the fixed launcher bottom-right — measured, never opened | [voice-chat](#voice-chat-launcher) |
| Cookie consent | every page | the Cookiebot layer was hidden, never answered (no consent button was clicked) | hidden before every shot and reading |
| Auth fields | /app/sign-in, /app/sign-up | the fields' own focus; sample text typed and deleted again — the submits stayed disabled and were never pressed | [email-field](#email-field), [password-field](#password-field), [tos-checkbox](#tos-checkbox) |
| The signed-in product | elevenlabs.io/app workspace | behind sign-in; /app redirects to /app/sign-in | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 32 components were given a real keyboard focus. 25 draw an outline ring: `nav-trigger` (on a child: 1px solid rgb(43, 127, 255) offset 2px), `nav-link` (on a child: 1px solid rgb(43, 127, 255) offset 2px), `signup-cta` (1px solid #2b7fff `color.brand.accent`, offset 2px), `login-link` (1px solid #2b7fff `color.brand.accent`, offset 2px), `hero-cta` (1px solid #2b7fff `color.brand.accent`, offset 2px), `contact-sales` (1px solid #2b7fff `color.brand.accent`, offset 2px), `product-tab` (1px solid #2b7fff `color.brand.accent`, offset 2px), `tool-tab` (1px solid #2b7fff `color.brand.accent`, offset 2px), `tts-language` (2px solid #2b7fff `color.brand.accent`, offset 2px), `tts-voice` (2px solid #2b7fff `color.brand.accent`, offset 2px), `learn-more` (1px solid #2b7fff `color.brand.accent`, offset 2px), `product-pill` (1px solid #2b7fff `color.brand.accent`, offset 2px), `billing-select` (1px solid #2b7fff `color.brand.accent`, offset 2px), `plan-cta` (1px solid #2b7fff `color.brand.accent`, offset 2px), `faq-item` (1px solid #2b7fff `color.brand.accent`, offset 2px), `google-login` (1px solid #2b7fff `color.brand.accent`, offset 2px), `convert-cta` (1px solid #2b7fff `color.brand.accent`, offset 2px), `card-play` (1px solid #2b7fff `color.brand.accent`, offset 2px), `try-voice` (1px solid #2b7fff `color.brand.accent`, offset 2px), `apikey-cta` (1px solid #2b7fff `color.brand.accent`, offset 2px), `explore-docs` (1px solid #2b7fff `color.brand.accent`, offset 2px), `demo-tab` (1px solid #2b7fff `color.brand.accent`, offset 2px), `docs-nav-item` (2px solid #404040, offset 2px), `m-nav-item` (1px solid #2b7fff `color.brand.accent`, offset 2px), `m-signup` (1px solid #2b7fff `color.brand.accent`, offset 2px). 3 draw a focus ring as a shadow instead: `docs-search`, `oauth-google`, `oauth-sso`. The other 4 show no measured change: `menu-link`, `voice-chat`, `feature-row`, `docs-copy-page`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.075s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | oauth-google, oauth-sso, signin-submit, signup-submit |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, box-shadow, color, fill, outline-color, stroke, text-decoration-color | apikey-cta, billing-select, contact-sales, convert-cta, docs-copy-page, docs-nav-item, docs-search, explore-docs and more |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Plan card](#plan-card) | 262 x 739 | - | - | transparent | none | 0 |
| [Playground card](#playground-card) | 530 x 208 | - | - | transparent | none | 0 |
| [Sign-in card](#sign-in-card) | 360 x 519 | - | - | #ffffff `color.neutral.white` | none | 0 |
| [Voice sample card](#voice-sample-card) | 724 x 54.5 | - | - | transparent | none | 0 |

## Components

### Shell and navigation

The promo strip (the V4 bar on home, the $1-credits countdown on product pages) and the light top nav: the ElevenLabs wordmark, the Products / Solutions / Customers / Resources flyout triggers, Enterprise and Pricing links, and the Log in / Sign up actions. Products opens a mega-menu with Overview / ElevenCreative / ElevenAgents / ElevenAPI columns.

#### Announcement bar
The promo strip above the nav (the V4 "Meet Eleven v4" bar on home, the $1-credits countdown on product pages). Read as `announcement` on the home page.

**Values (default).** size 1440 x 48; padding 8px 16px; background transparent; text Inter 14/18 400, #000000 `color.brand.ink`; icon 20 x 22, #f5f3f1; layers div.tw-absolute.tw-inset-0 1440.0x48.0 rgb(245, 243, 241); div.tw-absolute.tw-inset-x-0 1440.0x0.5 rgba(0, 0, 0, 0.1); a.tw-inline-flex.tw-items-center 77.9x32.0 rgb(255, 255, 255) rgb(255, 255, 255) 0px 0px 0px 0px, rgba(0, 0, 0, 0.125) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.04) 0px 1px 1px 0px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px 2px solid rgba(0, 0, 0, 0) offset 2px 9999px; a.tw-inline-flex.tw-item.

Child layers that carry the look: div 1440x48 background #f5f3f1; div 1440x0.5 background rgba(0, 0, 0, 0.1); a 77.9x32 background #ffffff `color.neutral.white` radius 9999px shadow #ffffff `color.neutral.white` 0px 0px 0px 0px, rgba(0, 0, 0, 0.125) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.04) 0px 1px 1px 0px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px.

![Announcement bar default](components/crops/announcement-default.png)

#### Nav bar
The top nav: the ElevenLabs wordmark, the Products/Solutions/Customers/Resources flyout triggers, Enterprise and Pricing links, and the Log in / Sign up actions. Read as `nav` on the home page.

**Values (default).** size 672.3 x 36; background transparent; text Inter 14/20 400, #000000 `color.brand.ink`; icon 117 x 15, #000000 `color.brand.ink`; layers a.tw-group.tw-outline-none 141.0x36.0 2px solid rgba(0, 0, 0, 0) offset 2px 9999px; button.tw-group.tw-flex 83.1x36.0 2px solid rgba(0, 0, 0, 0) offset 2px; button.tw-group.tw-flex 85.1x36.0 2px solid rgba(0, 0, 0, 0) offset 2px; a.tw-group.tw-flex 95.8x36.0 2px solid rgba(0, 0, 0, 0) offset 2px; button.tw-group.tw-flex 93.6x36.0 2px solid rgba(0, 0, 0, 0) offset 2px; a.tw-group.tw-flex 91.7x36.0 .

Child layers that carry the look: a 141x36 radius 9999px; button 83.1x36; button 85.1x36.

![Nav bar default](components/crops/nav-default.png)

#### Logo
The ElevenLabs wordmark anchor (aria-label "ElevenLabs"). Read as `logo` on the home page.

**Values (default).** size 141 x 36; padding 0px 12px; radius 9999px; background transparent; outline 2px solid transparent, offset 2px; text Inter 18/28.8 400, #000000 `color.brand.ink`; icon 117 x 15, #000000 `color.brand.ink`; layers a.tw-group.tw-outline-none 141.0x36.0 2px solid rgba(0, 0, 0, 0) offset 2px 9999px.

Child layers that carry the look: a 141x36 radius 9999px.

![Logo default](components/crops/logo-default.png)

#### Nav trigger
The Products button that opens the nav flyout; toggled, never followed. Read as `nav-trigger` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 83.06 x 36; background transparent; outline 2px solid transparent, offset 2px; text Inter 14/20 400, #000000 `color.brand.ink`; layers button.tw-group.tw-flex 83.1x36.0 2px solid rgba(0, 0, 0, 0) offset 2px |
| hover | layers button.tw-group.tw-flex 83.1x36.0 2px solid rgba(0, 0, 0, 0) offset 2px; div.tw-py-2.tw-px-3 83.1x36.0 rgba(41, 37, 36, 0.05) 18px |
| focus-visible | layers button.tw-group.tw-flex 83.1x36.0 2px solid rgba(0, 0, 0, 0) offset 2px; div.tw-py-2.tw-px-3 83.1x36.0 1px solid rgb(43, 127, 255) offset 2px 18px |
| pressed | layers button.tw-group.tw-flex 83.1x36.0 2px solid rgba(0, 0, 0, 0) offset 2px; div.tw-py-2.tw-px-3 83.1x36.0 rgba(41, 37, 36, 0.05) 18px |

Child layers that carry the look: button 83.1x36.

![Nav trigger default](components/crops/nav-trigger-default.png) ![Nav trigger hover](components/crops/nav-trigger-hover.png) ![Nav trigger focus-visible](components/crops/nav-trigger-focus-visible.png) ![Nav trigger pressed](components/crops/nav-trigger-pressed.png)

#### Nav link
A plain nav link (Pricing); measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 70 x 36; background transparent; outline 2px solid transparent, offset 2px; text Inter 14/20 400, #000000 `color.brand.ink`; layers a.tw-group.tw-flex 70.0x36.0 2px solid rgba(0, 0, 0, 0) offset 2px |
| hover | layers a.tw-group.tw-flex 70.0x36.0 2px solid rgba(0, 0, 0, 0) offset 2px; div.tw-px-3.tw-py-2 70.0x36.0 rgba(41, 37, 36, 0.05) 18px |
| focus-visible | layers a.tw-group.tw-flex 70.0x36.0 2px solid rgba(0, 0, 0, 0) offset 2px; div.tw-px-3.tw-py-2 70.0x36.0 1px solid rgb(43, 127, 255) offset 2px 18px |
| pressed | layers a.tw-group.tw-flex 70.0x36.0 2px solid rgba(0, 0, 0, 0) offset 2px; div.tw-px-3.tw-py-2 70.0x36.0 rgba(41, 37, 36, 0.05) 18px |

Child layers that carry the look: a 70x36.

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Sign-up action
The header Sign up action (the black pill); measured, never followed. Read as `signup-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 78.03 x 36; padding 0px 14px; radius 9999px; background #000000 `color.brand.ink`; outline 2px solid transparent, offset 2px; text Inter 14/21 400, #ffffff `color.neutral.white`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #44403b `color.brand.ink-hover` |
| focus-visible | outline 1px solid #2b7fff `color.brand.accent`, offset 2px |
| pressed | size 76.47 x 35.28; background #44403b `color.brand.ink-hover`; transform scale(0.98) |

![Sign-up action default](components/crops/signup-cta-default.png) ![Sign-up action hover](components/crops/signup-cta-hover.png) ![Sign-up action focus-visible](components/crops/signup-cta-focus-visible.png) ![Sign-up action pressed](components/crops/signup-cta-pressed.png)

#### Log-in action
The header Log in action; measured, never followed. Read as `login-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 68.5 x 36; padding 0px 14px; radius 9999px; background #ffffff `color.neutral.white`; shadow #ffffff 0px 0px 0px 0px, rgba(0, 0, 0, 0.125) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.04) 0px 1px 1px 0px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px; outline 2px solid transparent, offset 2px; text Inter 14/21 400, #000000 `color.brand.ink`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #fdfcfc `color.neutral.eggshell` |
| focus-visible | outline 1px solid #2b7fff `color.brand.accent`, offset 2px |
| pressed | size 67.13 x 35.28; background #fdfcfc `color.neutral.eggshell`; transform scale(0.98) |

![Log-in action default](components/crops/login-link-default.png) ![Log-in action hover](components/crops/login-link-hover.png) ![Log-in action focus-visible](components/crops/login-link-focus-visible.png) ![Log-in action pressed](components/crops/login-link-pressed.png)

#### Nav flyout
The Products mega-menu panel (Overview / ElevenCreative / ElevenAgents / ElevenAPI columns), opened by its own trigger. Read as `nav-dropdown` on the home page.

**Values (default).** size 940 x 565.5; background transparent; text Inter 13/18 500, #777169 `color.neutral.muted`; layers a.tw-block.tw-font-medium 226.0x12.5 2px solid rgba(0, 0, 0, 0) offset 2px; a.tw-block.tw-font-medium 226.0x12.5 2px solid rgba(0, 0, 0, 0) offset 2px; a.tw-block.tw-font-medium 226.0x12.5 2px solid rgba(0, 0, 0, 0) offset 2px; div.tw-h-px.tw-bg-gray-100 226.0x1.0 rgb(245, 243, 241); a.tw-block.tw-font-medium 226.0x11.0 2px solid rgba(0, 0, 0, 0) offset 2px; a.tw-block.tw-font-medium 226.0x11.0 2p.

Child layers that carry the look: a 226x12.5; a 226x12.5; a 226x12.5.

![Nav flyout default](components/crops/nav-dropdown-default.png)

#### Flyout link
A link inside the opened Products flyout (Text to Speech). Read as `menu-link` on the home page.

**Wrong element.** The default and pressed states caught a same-href link far down the page (y 3144); hover and focus-visible are the flyout's link. The entry needs a recapture.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 173.45 x 22; background transparent; outline 2px solid transparent, offset 2px; text Inter 15/22 400, #777169 `color.neutral.muted`; icon 12 x 12, #777169 `color.neutral.muted`; layers a.tw-outline-none.tw-inline-flex 173.5x22.0 2px solid rgba(0, 0, 0, 0) offset 2px |

Child layers that carry the look: a 173.5x22.

![Flyout link default](components/crops/menu-link-default.png) ![Flyout link hover](components/crops/menu-link-hover.png) ![Flyout link focus-visible](components/crops/menu-link-focus-visible.png) ![Flyout link pressed](components/crops/menu-link-pressed.png)

#### Voice-chat launcher
The fixed "Voice chat" launcher bottom-right (the ElevenAgents widget); measured, never opened. Read as `voice-chat` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 157.09 x 56; padding 10px 20px 10px 56px; background transparent; outline 2px solid transparent, offset 2px; text Inter 16/24 400, #000000 `color.brand.ink`; layers button.tw-py-1.5.sm:tw-py-2.5 157.1x56.0 2px solid rgba(0, 0, 0, 0) offset 2px |

Child layers that carry the look: button 157.1x56.

![Voice-chat launcher default](components/crops/voice-chat-default.png) ![Voice-chat launcher hover](components/crops/voice-chat-hover.png) ![Voice-chat launcher focus-visible](components/crops/voice-chat-focus-visible.png) ![Voice-chat launcher pressed](components/crops/voice-chat-pressed.png)

### Home

The light hero with the "Bringing technology to life" display and the Sign up / Contact sales pills, the product tabs (ElevenCreative / ElevenAgents / ElevenAPI) over a showcase with voice-orb carousel, and the signed-out Ultra-realistic speech TTS playground (textarea, language and voice selects, Play).

#### Hero headline
The "Bringing technology to life" display headline. Read as `hero-title` on the home page.

**Values (default).** size 563 x 86.5; background transparent; text Waldenburg 48/52 300, #000000 `color.brand.ink`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1.

![Hero headline default](components/crops/hero-title-default.png)

#### Hero copy
The lede under the hero headline. Read as `hero-sub` on the home page.

**Values (default).** size 563 x 59.5; background transparent; text Inter 16/24 400, #000000 `color.brand.ink`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1.

![Hero copy default](components/crops/hero-sub-default.png)

#### Hero CTA
The hero "Sign up" black pill; measured, never followed. Read as `hero-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 85.59 x 40; padding 0px 16px; radius 9999px; background #000000 `color.brand.ink`; outline 2px solid transparent, offset 2px; text Inter 15/22 400, #ffffff `color.neutral.white`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #44403b `color.brand.ink-hover` |
| focus-visible | outline 1px solid #2b7fff `color.brand.accent`, offset 2px |
| pressed | size 83.88 x 39.2; background #44403b `color.brand.ink-hover`; transform scale(0.98) |

![Hero CTA default](components/crops/hero-cta-default.png) ![Hero CTA hover](components/crops/hero-cta-hover.png) ![Hero CTA focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA pressed](components/crops/hero-cta-pressed.png)

#### Secondary CTA
The hero "Contact sales" ghost pill; measured, never followed. Read as `contact-sales` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 118.13 x 36; padding 0px 14px; radius 9999px; background #ffffff `color.neutral.white`; shadow #ffffff 0px 0px 0px 0px, rgba(0, 0, 0, 0.125) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.04) 0px 1px 1px 0px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px; outline 2px solid transparent, offset 2px; text Inter 14/21 400, #000000 `color.brand.ink`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #fdfcfc `color.neutral.eggshell` |
| focus-visible | outline 1px solid #2b7fff `color.brand.accent`, offset 2px |
| pressed | size 115.76 x 35.28; background #fdfcfc `color.neutral.eggshell`; transform scale(0.98) |

![Secondary CTA default](components/crops/contact-sales-default.png) ![Secondary CTA hover](components/crops/contact-sales-hover.png) ![Secondary CTA focus-visible](components/crops/contact-sales-focus-visible.png) ![Secondary CTA pressed](components/crops/contact-sales-pressed.png)

#### Product tab
A hero product tab (ElevenCreative / ElevenAgents / ElevenAPI); measured unselected — the selected state is the screenshot toggle. Read as `product-tab` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 389.33 x 44; padding 0px 21px; radius 12px; background transparent; outline 2px solid transparent, offset 2px; text Inter 16/24 400, #44403b `color.brand.ink-hover`; layers div.tw-group/tab.tw-isolate 389.3x44.0 2px solid rgba(0, 0, 0, 0) offset 2px 12px; div.tw-relative.tw-mr-0.5 12.0x12.0 rgb(245, 243, 241) 12px; div.tw-absolute.tw-mix-blend-overlay 12.0x12.0; div.tw-absolute.-tw-z-10 383.3x40.0 rgb(235, 232, 228) 12px; div.tw-absolute.-tw-z-10 383.3x40.0 rgb(255, 255, 255) rgba(0, 0, 0, 0.125) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.04) 0px 1px 1px 0px, rgba(0, 0, 0, 0 |
| hover | text Inter 16/24 400, #000000 `color.brand.ink` |
| focus-visible | outline 1px solid #2b7fff `color.brand.accent`, offset 2px; layers div.tw-group/tab.tw-isolate 389.3x44.0 1px solid rgb(43, 127, 255) offset 2px 12px; div.tw-relative.tw-mr-0.5 12.0x12.0 rgb(245, 243, 241) 12px; div.tw-absolute.tw-mix-blend-overlay 12.0x12.0; div.tw-absolute.-tw-z-10 383.3x40.0 rgb(235, 232, 228) 12px; div.tw-absolute.-tw-z-10 383.3x40.0 rgb(255, 255, 255) rgba(0, 0, 0, 0.125) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.04) 0px 1px 1px 0px, rgba(0, 0, 0,  |
| pressed | text Inter 16/24 400, #000000 `color.brand.ink` |

Child layers that carry the look: div 389.3x44 radius 12px; div 12x12 background #f5f3f1 radius 12px; div 12x12 image image-set(url(…) 1dppx type("image/avif"), url(…) 1dppx type("image/png")).

![Product tab default](components/crops/product-tab-default.png) ![Product tab hover](components/crops/product-tab-hover.png) ![Product tab focus-visible](components/crops/product-tab-focus-visible.png) ![Product tab pressed](components/crops/product-tab-pressed.png)

#### Tool tab
A product-showcase tab (AI Voice Generator / Text to Speech / Music / Speech to Text / Voice Cloning / Dubbing). Read as `tool-tab` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 142.34 x 40; padding 0px 17px; radius 9999px; background transparent; outline 2px solid transparent, offset 2px; text Inter 15/22 400, #44403b `color.brand.ink-hover`; layers div.tw-group/tab.tw-isolate 142.3x40.0 2px solid rgba(0, 0, 0, 0) offset 2px 9999px; div.tw-absolute.-tw-z-10 136.3x36.0 rgb(235, 232, 228) 9999px; div.tw-absolute.-tw-z-10 136.3x36.0 rgb(255, 255, 255) rgba(0, 0, 0, 0.125) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.04) 0px 1px 1px 0px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px 9999px |
| hover | text Inter 15/22 400, #000000 `color.brand.ink` |
| focus-visible | outline 1px solid #2b7fff `color.brand.accent`, offset 2px; layers div.tw-group/tab.tw-isolate 142.3x40.0 1px solid rgb(43, 127, 255) offset 2px 9999px; div.tw-absolute.-tw-z-10 136.3x36.0 rgb(235, 232, 228) 9999px; div.tw-absolute.-tw-z-10 136.3x36.0 rgb(255, 255, 255) rgba(0, 0, 0, 0.125) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.04) 0px 1px 1px 0px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px 9999px |
| pressed | text Inter 15/22 400, #000000 `color.brand.ink` |

Child layers that carry the look: div 142.3x40 radius 9999px; div 136.3x36 background #ebe8e4 radius 9999px; div 136.3x36 background #ffffff `color.neutral.white` radius 9999px shadow rgba(0, 0, 0, 0.125) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.04) 0px 1px 1px 0px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px.

![Tool tab default](components/crops/tool-tab-default.png) ![Tool tab hover](components/crops/tool-tab-hover.png) ![Tool tab focus-visible](components/crops/tool-tab-focus-visible.png) ![Tool tab pressed](components/crops/tool-tab-pressed.png)

#### Voice preview
A "Play <voice> preview" button on the voice-orb carousel; measured, the audio itself was never played here. Read as `voice-play` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 108.94 x 108.94; radius 9999px; background transparent; outline 2px solid transparent, offset 2px; text Inter 18/28.8 400, #000000 `color.brand.ink`; layers button.tw-absolute.tw-inset-0 108.9x108.9 2px solid rgba(0, 0, 0, 0) offset 2px 9999px |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: button 108.9x108.9 radius 9999px.

![Voice preview default](components/crops/voice-play-default.png) ![Voice preview hover](components/crops/voice-play-hover.png) ![Voice preview pressed](components/crops/voice-play-pressed.png)

#### Carousel previous
The "Previous voice" carousel icon button. Read as `voice-prev` on the home page.

Not on the page when it was captured.

#### Section heading
A section heading below the hero (the "Create, edit, and localize in one AI platform" block). Read as `section-h2` on the home page.

**Values (default).** size 563 x 11.5; background transparent; text Inter 16/24 400, #000000 `color.brand.ink`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1.

![Section heading default](components/crops/section-h2-default.png)

#### Playground card
The "Ultra-realistic speech" playground card — the signed-out TTS demo widget (textarea, language and voice selects, Play). Read as `tts-card` on the home page.

**Values (default).** size 530 x 208; background transparent; text Inter 16/24 400, #000000 `color.brand.ink`; icon 16 x 16, #a59f97; layers div.tw-px-5.tw-text-base/base 530.0x136.0 2px solid rgba(0, 0, 0, 0) offset 2px; textarea.tw-px-5.tw-text-base/base 530.0x136.0 2px solid rgba(0, 0, 0, 0) offset 2px; div.tw-flex-none.tw-sticky 529.0x24.0; button.tw-w-full.tw-font-medium 120.0x36.0 2px solid rgba(0, 0, 0, 0) offset 2px 12px; select 180.0x23.0 rgb(255, 255, 255); button.tw-w-full.tw-font-medium 158.1x36.0 2px solid rgba(0, 0, 0, 0).

Child layers that carry the look: div 530x136; textarea 530x136; div 529x24 image linear-gradient(to top, #ffffff `color.neutral.white`, rgba(255, 255, 255, 0)).

![Playground card default](components/crops/tts-card-default.png)

#### Playground textarea
The playground's text field; focused and given sample text that was deleted again — nothing generated in this pass. Read as `tts-textarea` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 530 x 136; padding 16px 20px 0px 20px; background transparent; outline 2px solid transparent, offset 2px; text Inter 16/24 400, transparent; placeholder transparent; layers textarea.tw-px-5.tw-text-base/base 530.0x136.0 2px solid rgba(0, 0, 0, 0) offset 2px |

Child layers that carry the look: textarea 530x136.

![Playground textarea default](components/crops/tts-textarea-default.png) ![Playground textarea focused](components/crops/tts-textarea-focused.png) ![Playground textarea filled](components/crops/tts-textarea-filled.png)

#### Language select
The playground language combobox (the flag + "English" button). Read as `tts-language` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 120.03 x 36; padding 0px 8px 0px 12px; radius 12px; background transparent; outline 2px solid transparent, offset 2px; text Inter 15/22 500, #000000 `color.brand.ink`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #a59f97; layers button.tw-w-full.tw-font-medium 120.0x36.0 2px solid rgba(0, 0, 0, 0) offset 2px 12px |
| hover | icon 16 x 16, #000000 `color.brand.ink` |
| focus-visible | outline 2px solid #2b7fff `color.brand.accent`, offset 2px; layers button.tw-w-full.tw-font-medium 120.0x36.0 2px solid rgb(43, 127, 255) offset 2px 12px |

Child layers that carry the look: button 120x36 radius 12px.

![Language select default](components/crops/tts-language-default.png) ![Language select hover](components/crops/tts-language-hover.png) ![Language select focus-visible](components/crops/tts-language-focus-visible.png) ![Language select pressed](components/crops/tts-language-pressed.png)

#### Voice select
The playground voice combobox (the orb + voice-name button). Read as `tts-voice` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 158.14 x 36; padding 0px 8px 0px 12px; radius 12px; background transparent; outline 2px solid transparent, offset 2px; text Inter 15/22 500, #000000 `color.brand.ink`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #a59f97; layers button.tw-w-full.tw-font-medium 158.1x36.0 2px solid rgba(0, 0, 0, 0) offset 2px 12px |
| hover | icon 16 x 16, #000000 `color.brand.ink` |
| focus-visible | outline 2px solid #2b7fff `color.brand.accent`, offset 2px; layers button.tw-w-full.tw-font-medium 158.1x36.0 2px solid rgb(43, 127, 255) offset 2px 12px |

Child layers that carry the look: button 158.1x36 radius 12px.

![Voice select default](components/crops/tts-voice-default.png) ![Voice select hover](components/crops/tts-voice-hover.png) ![Voice select focus-visible](components/crops/tts-voice-focus-visible.png) ![Voice select pressed](components/crops/tts-voice-pressed.png)

#### Play button
The playground Play action; states forced — the public shot pass pressed it once and it generated without an account (see README). Read as `tts-play` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 57.86 x 36; padding 0px 14px; radius 9999px; background #000000 `color.brand.ink`; outline 2px solid transparent, offset 2px; text Inter 15/15 400, #ffffff `color.neutral.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1) |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Play button default](components/crops/tts-play-default.png) ![Play button hover](components/crops/tts-play-hover.png) ![Play button pressed](components/crops/tts-play-pressed.png)

#### Learn more
The "Learn more" black pill in the product section. Read as `learn-more` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 126.44 x 44; padding 0px 20px; radius 9999px; background #000000 `color.brand.ink`; outline 2px solid transparent, offset 2px; text Inter 16/24 400, #ffffff `color.neutral.white`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #44403b `color.brand.ink-hover` |
| focus-visible | outline 1px solid #2b7fff `color.brand.accent`, offset 2px |
| pressed | size 123.91 x 43.12; background #44403b `color.brand.ink-hover`; transform scale(0.98) |

![Learn more default](components/crops/learn-more-default.png) ![Learn more hover](components/crops/learn-more-hover.png) ![Learn more focus-visible](components/crops/learn-more-focus-visible.png) ![Learn more pressed](components/crops/learn-more-pressed.png)

#### Feature panel
A feature panel under the product grid (the Ultra-realistic speech showcase, the playground card's parent). Read as `feature-card` on the home page.

**Values (default).** size 530 x 208; background transparent; text Inter 16/24 400, #000000 `color.brand.ink`; icon 16 x 16, #a59f97; layers div.tw-px-5.tw-text-base/base 530.0x40.0 2px solid rgba(0, 0, 0, 0) offset 2px; textarea.tw-px-5.tw-text-base/base 530.0x136.0 2px solid rgba(0, 0, 0, 0) offset 2px; div.tw-flex-none.tw-sticky 529.0x24.0; button.tw-w-full.tw-font-medium 120.0x36.0 2px solid rgba(0, 0, 0, 0) offset 2px 12px; select 180.0x23.0 rgb(255, 255, 255); button.tw-w-full.tw-font-medium 158.1x36.0 2px solid rgba(0, 0, 0, 0) .

Child layers that carry the look: div 530x40; textarea 530x136; div 529x24 image linear-gradient(to top, #ffffff `color.neutral.white`, rgba(255, 255, 255, 0)).

![Feature panel default](components/crops/feature-card-default.png)

### Pricing

The /pricing surface: the product pills (links), the Monthly billing dropdown, the Free / Starter / Creator / Pro / Scale / Business / Enterprise cards and the FAQ accordion under Compare plans.

#### Pricing title
The "Flexible pricing for your needs" display heading. Read as `pricing-h1` on the pricing page.

**Values (default).** size 757.33 x 34.5; background transparent; text Waldenburg 48/52 300, #000000 `color.brand.ink`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1.

![Pricing title default](components/crops/pricing-h1-default.png)

#### Product pill
An ElevenCreative/ElevenAgents/ElevenAPI product pill (a link, not a tab — it navigates); measured, never followed. Read as `product-pill` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 169.05 x 44; padding 0px 21px; radius 9999px; background transparent; outline 2px solid transparent, offset 2px; text Inter 16/24 400, #777169 `color.neutral.muted`; layers a.tw-group/tab.tw-isolate 169.0x44.0 2px solid rgba(0, 0, 0, 0) offset 2px 9999px; div.tw-relative.tw-mr-0.5 12.0x12.0 rgb(245, 243, 241) 9999px; div.tw-absolute.tw-mix-blend-overlay 12.0x12.0; div.tw-absolute.-tw-z-10 161.0x38.0 rgb(245, 243, 241) 9999px; div.tw-absolute.-tw-z-10 161.0x38.0 rgb(255, 255, 255) rgba(0, 0, 0, 0.125) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.04) 0px 1px 1px 0px, rgba(0, 0,  |
| hover | text Inter 16/24 400, #000000 `color.brand.ink` |
| focus-visible | outline 1px solid #2b7fff `color.brand.accent`, offset 2px; layers a.tw-group/tab.tw-isolate 169.0x44.0 1px solid rgb(43, 127, 255) offset 2px 9999px; div.tw-relative.tw-mr-0.5 12.0x12.0 rgb(245, 243, 241) 9999px; div.tw-absolute.tw-mix-blend-overlay 12.0x12.0; div.tw-absolute.-tw-z-10 161.0x38.0 rgb(245, 243, 241) 9999px; div.tw-absolute.-tw-z-10 161.0x38.0 rgb(255, 255, 255) rgba(0, 0, 0, 0.125) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.04) 0px 1px 1px 0px, rgba(0, 0, |
| pressed | text Inter 16/24 400, #000000 `color.brand.ink` |

Child layers that carry the look: a 169x44 radius 9999px; div 12x12 background #f5f3f1 radius 9999px; div 12x12 image image-set(url(…) 1dppx type("image/avif"), url(…) 1dppx type("image/png")).

![Product pill default](components/crops/product-pill-default.png) ![Product pill hover](components/crops/product-pill-hover.png) ![Product pill focus-visible](components/crops/product-pill-focus-visible.png) ![Product pill pressed](components/crops/product-pill-pressed.png)

#### Billing dropdown
The "Monthly billing" dropdown; opened for the billing screenshot, never changed. Read as `billing-select` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 168.2 x 44; padding 0px 20px; radius 9999px; background transparent; shadow #ffffff 0px 0px 0px 0px inset, #d7d2cc 0px 0px 0px 0.5px inset; outline 2px solid transparent, offset 2px; text Inter 16/24 400, #777169 `color.neutral.muted`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #777169 `color.neutral.muted`; layers button.tw-inline-flex.tw-items-center 168.2x44.0 rgb(255, 255, 255) 0px 0px 0px 0px inset, rgb(215, 210, 204) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 2px solid rgba(0, 0, 0, 0) offset 2px 9999px |
| hover | shadow #ffffff 0px 0px 0px 0px inset, #a59f97 0px 0px 0px 0.5px inset; text Inter 16/24 400, #000000 `color.brand.ink`; icon 20 x 20, #000000 `color.brand.ink`; layers button.tw-inline-flex.tw-items-center 168.2x44.0 rgb(255, 255, 255) 0px 0px 0px 0px inset, rgb(165, 159, 151) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 2px solid rgba(0, 0, 0, 0) offset 2px 9999px |
| focus-visible | outline 1px solid #2b7fff `color.brand.accent`, offset 2px; layers button.tw-inline-flex.tw-items-center 168.2x44.0 rgb(255, 255, 255) 0px 0px 0px 0px inset, rgb(215, 210, 204) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 1px solid rgb(43, 127, 255) offset 2px 9999px |
| pressed | size 164.84 x 43.12; shadow #ffffff 0px 0px 0px 0px inset, #a59f97 0px 0px 0px 0.5px inset; text Inter 16/24 400, #000000 `color.brand.ink`; transform scale(0.98); icon 19.6 x 19.6, #000000 `color.brand.ink`; layers button.tw-inline-flex.tw-items-center 164.8x43.1 rgb(255, 255, 255) 0px 0px 0px 0px inset, rgb(165, 159, 151) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 2px solid rgba(0, 0, 0, 0) offset 2px 9999px |

![Billing dropdown default](components/crops/billing-select-default.png) ![Billing dropdown hover](components/crops/billing-select-hover.png) ![Billing dropdown focus-visible](components/crops/billing-select-focus-visible.png) ![Billing dropdown pressed](components/crops/billing-select-pressed.png)

#### Plan card
A pricing plan card (Free / Starter / Creator / Pro — name, price and action). Read as `plan-card` on the pricing page.

**Values (default).** size 262 x 739; background transparent; text Inter 24/32 400, #000000 `color.brand.ink`; icon 20 x 20, #000000 `color.brand.ink`; layers div.tw-absolute.tw-inset-0 262.0x200.0 rgb(245, 243, 241); div.tw-absolute.tw-mix-blend-overlay 262.0x200.0 16px; div.tw-absolute.tw-pointer-events-none 262.0x200.0 rgb(255, 255, 255) 0px 0px 0px 0px inset, rgba(0, 0, 0, 0.075) 0px 0px 0px 0.5px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 16px; a.tw-inline-flex.tw-items-center 262.0x44.0 rgb(0, 0, 0) 2px solid rgba(0, 0, 0, 0) offset 2px 9999px; div 2.

Child layers that carry the look: div 262x200 background #f5f3f1; div 262x200 image image-set(url(…) 1dppx type("image/avif"), url(…) 1dppx type("image/png")) radius 16px; div 262x200 radius 16px shadow #ffffff `color.neutral.white` 0px 0px 0px 0px inset, rgba(0, 0, 0, 0.075) 0px 0px 0px 0.5px inset, transparent 0px 0px 0px 0px.

![Plan card default](components/crops/plan-card-default.png)

#### Plan price
A plan card's price figure. Read as `plan-price` on the pricing page.

**Values (default).** size 25.45 x 14.5; background transparent; text Inter 20/27 400, #000000 `color.brand.ink`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1.

![Plan price default](components/crops/plan-price-default.png)

#### Plan CTA
A plan card's action (Build for free / Choose X); measured, never followed. Read as `plan-cta` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 262 x 44; padding 0px 20px; radius 9999px; background #000000 `color.brand.ink`; outline 2px solid transparent, offset 2px; text Inter 16/24 400, #ffffff `color.neutral.white`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #44403b `color.brand.ink-hover` |
| focus-visible | outline 1px solid #2b7fff `color.brand.accent`, offset 2px |
| pressed | size 256.76 x 43.12; background #44403b `color.brand.ink-hover`; transform scale(0.98) |

![Plan CTA default](components/crops/plan-cta-default.png) ![Plan CTA hover](components/crops/plan-cta-hover.png) ![Plan CTA focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA pressed](components/crops/plan-cta-pressed.png)

#### Plan badge
A badge on a plan card ("Popular" on Creator, "Until Nov 16" on Starter). Read as `plan-badge` on the pricing page.

**Values (default).** size 89.22 x 21; padding 4px 8px; radius 9999px; background #000000 `color.brand.ink`; text Inter 13/13 400, #ffffff `color.neutral.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1.

![Plan badge default](components/crops/plan-badge-default.png)

#### Feature row
An "Everything in X, plus" feature-group row inside a plan card. Read as `feature-row` on the pricing page.

**Wrong element.** The plan-card mark caught the whole 1440 x 5508 page body, not a feature row; the 2026-11-13 re-run did not find it either (recaptureMissed), so these are the first run's readings. The entry needs a recapture.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 1440 x 5508.61; background transparent; text Inter 14/21 400, #ffffff `color.neutral.white`; icon 116 x 15, #000000 `color.brand.ink`; layers div.tw-fixed.tw-top-0 1440.0x64.0 rgb(255, 255, 255); div.tw-absolute.tw-inset-x-0 1440.0x1.0 rgb(235, 232, 228); a.tw-h-9.tw-flex 140.0x36.0 2px solid rgba(0, 0, 0, 0) offset 2px 9999px; a.tw-inline-flex.tw-items-center 78.0x36.0 rgb(0, 0, 0) 2px solid rgba(0, 0, 0, 0) offset 2px 9999px; div.tw-grid.tw-rounded-full 0.0x0.0 rgb(255, 255, 255) 0px 0px 0px 0px inset, rgb(215, 210, 204) 0px 0px 0px 0 |
| focus-visible | text Waldenburg 48/52 300, #000000 `color.brand.ink` |

Child layers that carry the look: div 1440x64 background #ffffff `color.neutral.white`; div 1440x1 background #ebe8e4; a 140x36 radius 9999px.

![Feature row default](components/crops/feature-row-default.png) ![Feature row hover](components/crops/feature-row-hover.png) ![Feature row focus-visible](components/crops/feature-row-focus-visible.png) ![Feature row pressed](components/crops/feature-row-pressed.png)

#### FAQ accordion
A FAQ accordion row under Compare plans; measured closed, never expanded. Read as `faq-item` on the pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 724 x 52.5; radius 4px; background transparent; outline 2px solid transparent, offset 2px; text Inter 17/25 400, #000000 `color.brand.ink`; icon 20 x 20, #a59f97; layers button.tw-group/trigger.tw-text-left 724.0x52.5 2px solid rgba(0, 0, 0, 0) offset 2px 4px |
| hover | icon 20 x 20, #000000 `color.brand.ink` |
| focus-visible | outline 1px solid #2b7fff `color.brand.accent`, offset 2px; layers button.tw-group/trigger.tw-text-left 724.0x52.5 1px solid rgb(43, 127, 255) offset 2px 4px |
| pressed | icon 20 x 20, #000000 `color.brand.ink` |

Child layers that carry the look: button 724x52.5 radius 4px.

![FAQ accordion default](components/crops/faq-item-default.png) ![FAQ accordion hover](components/crops/faq-item-hover.png) ![FAQ accordion focus-visible](components/crops/faq-item-focus-visible.png) ![FAQ accordion pressed](components/crops/faq-item-pressed.png)

### Text to Speech

The /text-to-speech product page: the display heading, the Log in with Google / Convert Text to Speech actions and the voice-sample card carousel with per-card play buttons.

#### Page title
The h1 on /text-to-speech (the small "Text to Speech" eyebrow above the big display). Read as `tts-h1` on the text-to-speech page.

**Values (default).** size 1178 x 11; background transparent; text Inter 15/22 500, #777169 `color.neutral.muted`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1.

![Page title default](components/crops/tts-h1-default.png)

#### Google login CTA
The "Log in with Google" action on the product hero; measured, never pressed — it would leave for the OAuth flow. Read as `google-login` on the text-to-speech page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 207.09 x 44; padding 0px 20px 0px 18px; radius 9999px; background #000000 `color.brand.ink`; outline 2px solid transparent, offset 2px; text Inter 16/24 400, #ffffff `color.neutral.white`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #44403b `color.brand.ink-hover` |
| focus-visible | outline 1px solid #2b7fff `color.brand.accent`, offset 2px |
| pressed | size 202.95 x 43.12; background #44403b `color.brand.ink-hover`; transform scale(0.98) |

![Google login CTA default](components/crops/google-login-default.png) ![Google login CTA hover](components/crops/google-login-hover.png) ![Google login CTA focus-visible](components/crops/google-login-focus-visible.png) ![Google login CTA pressed](components/crops/google-login-pressed.png)

#### Convert CTA
The "Convert Text to Speech" action; measured, never followed. Read as `convert-cta` on the text-to-speech page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 217.84 x 44; padding 0px 20px; radius 9999px; background #ffffff `color.neutral.white`; shadow #ffffff 0px 0px 0px 0px, rgba(0, 0, 0, 0.125) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.04) 0px 1px 1px 0px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px; outline 2px solid transparent, offset 2px; text Inter 16/24 400, #000000 `color.brand.ink`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #fdfcfc `color.neutral.eggshell` |
| focus-visible | outline 1px solid #2b7fff `color.brand.accent`, offset 2px |
| pressed | size 213.49 x 43.12; background #fdfcfc `color.neutral.eggshell`; transform scale(0.98) |

![Convert CTA default](components/crops/convert-cta-default.png) ![Convert CTA hover](components/crops/convert-cta-hover.png) ![Convert CTA focus-visible](components/crops/convert-cta-focus-visible.png) ![Convert CTA pressed](components/crops/convert-cta-pressed.png)

#### Voice sample card
A voice-sample card (the photo card with a corner play button and the voice name). Read as `voice-card` on the text-to-speech page.

**Wrong element.** The `.last()` over a broad union caught a 724 x 54 FAQ row, not a voice-sample card. The entry needs a recapture.

**Values (default).** size 724 x 54.5; background transparent; text Inter 17/25 400, #000000 `color.brand.ink`; icon 20 x 20, #a59f97; layers button.tw-group/trigger.tw-text-left 724.0x54.5 2px solid rgba(0, 0, 0, 0) offset 2px 4px; div 724.0x2.0.

Child layers that carry the look: button 724x54.5 radius 4px; div 724x2 image repeating-radial-gradient(circle, rgba(0, 0, 0, 0.15) 0px, rgba(0, 0, 0, 0.15) 1px, transp.

![Voice sample card default](components/crops/voice-card-default.png)

#### Sample play button
The corner play button on a voice-sample card; measured, audio never played here. Read as `card-play` on the text-to-speech page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 338.4 x 439.92; radius 16px; background transparent; outline 2px solid transparent, offset 2px; text Inter 18/28.8 400, #000000 `color.brand.ink`; icon 11.28 x 11.28, #000000 `color.brand.ink`; layers button.tw-group/preview-button.tw-absolute 338.4x439.9 2px solid rgba(0, 0, 0, 0) offset 2px 16px; div.tw-absolute.tw-inset-0 41.4x41.4 rgb(255, 255, 255) rgb(255, 255, 255) 0px 0px 0px 0px, rgba(0, 0, 0, 0.125) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.04) 0px 1px 1px 0px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px 9999px |
| focus-visible | outline 1px solid #2b7fff `color.brand.accent`, offset 2px; layers button.tw-group/preview-button.tw-absolute 338.4x439.9 1px solid rgb(43, 127, 255) offset 2px 16px; div.tw-absolute.tw-inset-0 38.3x38.3 rgb(255, 255, 255) rgb(255, 255, 255) 0px 0px 0px 0px, rgba(0, 0, 0, 0.125) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.04) 0px 1px 1px 0px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px 9999px |

Child layers that carry the look: button 338.4x439.9 radius 16px; div 41.4x41.4 background #ffffff `color.neutral.white` radius 9999px shadow #ffffff `color.neutral.white` 0px 0px 0px 0px, rgba(0, 0, 0, 0.125) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.04) 0px 1px 1px 0px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px.

![Sample play button default](components/crops/card-play-default.png) ![Sample play button hover](components/crops/card-play-hover.png) ![Sample play button focus-visible](components/crops/card-play-focus-visible.png) ![Sample play button pressed](components/crops/card-play-pressed.png)

#### Try voice CTA
The "Try this voice" action under the voice cards; measured, never followed. Read as `try-voice` on the text-to-speech page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 141.33 x 48; padding 0px 20px; radius 9999px; background #000000 `color.brand.ink`; outline 2px solid transparent, offset 2px; text Inter 16/24 400, #ffffff `color.neutral.white`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #44403b `color.brand.ink-hover` |
| focus-visible | outline 1px solid #2b7fff `color.brand.accent`, offset 2px |
| pressed | size 138.5 x 47.04; background #44403b `color.brand.ink-hover`; transform scale(0.98) |

![Try voice CTA default](components/crops/try-voice-default.png) ![Try voice CTA hover](components/crops/try-voice-hover.png) ![Try voice CTA focus-visible](components/crops/try-voice-focus-visible.png) ![Try voice CTA pressed](components/crops/try-voice-pressed.png)

#### Display heading
The "Text to Speech with high quality, human-like AI voices" display heading. Read as `tts-display` on the text-to-speech page.

**Values (default).** size 565 x 68; background transparent; text Waldenburg 36/42 300, #000000 `color.brand.ink`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1.

![Display heading default](components/crops/tts-display-default.png)

### API

The /api developer page: the "Build production-ready audio AI in minutes" heading, Get API key / Explore docs pills and the Text to Speech API card with its Demo / Code toggle.

#### Page title
The "Build production-ready audio AI in minutes" display heading. Read as `api-h1` on the api page.

**Values (default).** size 563 x 86.5; background transparent; text Waldenburg 48/52 300, #000000 `color.brand.ink`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1.

![Page title default](components/crops/api-h1-default.png)

#### Get API key CTA
The "Get API key" black pill; measured, never followed (it leads to sign-up). Read as `apikey-cta` on the api page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 127.48 x 44; padding 0px 20px; radius 9999px; background #000000 `color.brand.ink`; outline 2px solid transparent, offset 2px; text Inter 16/24 400, #ffffff `color.neutral.white`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #44403b `color.brand.ink-hover` |
| focus-visible | outline 1px solid #2b7fff `color.brand.accent`, offset 2px |
| pressed | size 124.93 x 43.12; background #44403b `color.brand.ink-hover`; transform scale(0.98) |

![Get API key CTA default](components/crops/apikey-cta-default.png) ![Get API key CTA hover](components/crops/apikey-cta-hover.png) ![Get API key CTA focus-visible](components/crops/apikey-cta-focus-visible.png) ![Get API key CTA pressed](components/crops/apikey-cta-pressed.png)

#### Explore docs
The "Explore docs" ghost pill; measured, never followed. Read as `explore-docs` on the api page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 138.19 x 44; padding 0px 20px; radius 9999px; background #ffffff `color.neutral.white`; shadow #ffffff 0px 0px 0px 0px, rgba(0, 0, 0, 0.125) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.04) 0px 1px 1px 0px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px; outline 2px solid transparent, offset 2px; text Inter 16/24 400, #000000 `color.brand.ink`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background #fdfcfc `color.neutral.eggshell` |
| focus-visible | outline 1px solid #2b7fff `color.brand.accent`, offset 2px |
| pressed | size 135.42 x 43.12; background #fdfcfc `color.neutral.eggshell`; transform scale(0.98) |

![Explore docs default](components/crops/explore-docs-default.png) ![Explore docs hover](components/crops/explore-docs-hover.png) ![Explore docs focus-visible](components/crops/explore-docs-focus-visible.png) ![Explore docs pressed](components/crops/explore-docs-pressed.png)

#### Demo/Code tab
The Demo/Code toggle on the Text to Speech API card. Read as `demo-tab` on the api page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 75.31 x 40; padding 0px 17px 0px 16px; radius 9999px; background transparent; outline 2px solid transparent, offset 2px; text Inter 15/22 400, #000000 `color.brand.ink`; layers div.tw-group/tab.tw-isolate 75.3x40.0 2px solid rgba(0, 0, 0, 0) offset 2px 9999px; div.tw-absolute.-tw-z-10 68.3x34.0 rgb(235, 232, 228) 9999px; div.tw-absolute.-tw-z-10 74.3x40.0 rgb(255, 255, 255) rgba(0, 0, 0, 0.125) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.04) 0px 1px 1px 0px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px 9999px |
| focus-visible | outline 1px solid #2b7fff `color.brand.accent`, offset 2px; layers div.tw-group/tab.tw-isolate 75.3x40.0 1px solid rgb(43, 127, 255) offset 2px 9999px; div.tw-absolute.-tw-z-10 68.3x34.0 rgb(235, 232, 228) 9999px; div.tw-absolute.-tw-z-10 74.3x40.0 rgb(255, 255, 255) rgba(0, 0, 0, 0.125) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.04) 0px 1px 1px 0px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px 9999px |

Child layers that carry the look: div 75.3x40 radius 9999px; div 68.3x34 background #ebe8e4 radius 9999px; div 74.3x40 background #ffffff `color.neutral.white` radius 9999px shadow rgba(0, 0, 0, 0.125) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.04) 0px 1px 1px 0px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px.

![Demo/Code tab default](components/crops/demo-tab-default.png) ![Demo/Code tab hover](components/crops/demo-tab-hover.png) ![Demo/Code tab focus-visible](components/crops/demo-tab-focus-visible.png) ![Demo/Code tab pressed](components/crops/demo-tab-pressed.png)

### Docs

The /docs landing (Mintlify-style): the ElevenLabs Documentation heading, the search trigger, the capability sidebar and the Copy page dropdown.

#### Docs title
The "ElevenLabs Documentation" heading. Read as `docs-h1` on the docs page.

**Values (default).** size 467.75 x 45; background transparent; text ui-sans-serif 36/45 800, #2a2a2a.

![Docs title default](components/crops/docs-h1-default.png)

#### Docs search
The docs search trigger in the top bar. Read as `docs-search` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 632.63 x 36; padding 8px; radius 8px; background transparent; shadow rgba(0, 0, 0, 0.12) 0px 0px 0px 1px inset; text ui-sans-serif 14/20 500, rgba(0, 0, 0, 0.608); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, rgba(0, 0, 0, 0.608); layers button.focus-visible:ring-(color:--accent).rounded-2 632.6x36.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.12) 0px 0px 0px 1px inset, rgba(0, 0, 0, 0) 0px 0px 0px 0px 8px; kbd.fern-kbd 21.2x22.0 rgba(255, 255, 255, 0.8) T:1px solid rgba(0, 0, 0, 0.15) / R:1px solid rgba(0, 0, 0, 0.15) / B:1px solid rgba(0, 0, 0, 0.15) / L:1 |
| hover | background rgba(0, 0, 0, 0.06); transition none 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers none |
| focus-visible | background rgba(0, 0, 0, 0.004); shadow #404040 0px 0px 0px 1px inset; layers none |
| pressed | background rgba(0, 0, 0, 0.06); transition none 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers none |

![Docs search default](components/crops/docs-search-default.png) ![Docs search hover](components/crops/docs-search-hover.png) ![Docs search focus-visible](components/crops/docs-search-focus-visible.png) ![Docs search pressed](components/crops/docs-search-pressed.png)

#### Docs nav item
A sidebar capability link (Text to Speech). Read as `docs-nav-item` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 195 x 36; padding 8px; radius 8px; background transparent; text ui-sans-serif 14/17.5 400, rgba(0, 0, 0, 0.875); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, rgba(0, 0, 0, 0.447) |
| hover | background rgba(0, 0, 0, 0.06); transition none 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 2px solid #404040, offset 2px; layers a.fern-sidebar-link.fern-sidebar-level-1 195.0x36.0 2px solid rgb(64, 64, 64) offset 2px 8px |
| pressed | background rgba(0, 0, 0, 0.06); transition none 0.15s cubic-bezier(0.4, 0, 0.2, 1) |

![Docs nav item default](components/crops/docs-nav-item-default.png) ![Docs nav item hover](components/crops/docs-nav-item-hover.png) ![Docs nav item focus-visible](components/crops/docs-nav-item-focus-visible.png) ![Docs nav item pressed](components/crops/docs-nav-item-pressed.png)

#### Copy page
The "Copy page" dropdown on the doc header. Read as `docs-copy-page` on the docs page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 110.56 x 32; padding 4px 8px; border R: 1px solid rgba(0, 0, 0, 0.12); radius 8px 0px 0px 8px; background transparent; text ui-sans-serif 14/20 400, rgba(0, 0, 0, 0.608); transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, rgba(0, 0, 0, 0.608); layers button.w-fit.px-2 110.6x32.0 R:1px solid rgba(0, 0, 0, 0.12) 8px 0px 0px 8px |
| hover | background rgba(0, 0, 0, 0.06); text ui-sans-serif 14/20 400, #2a2a2a; transition none 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #2a2a2a; layers none |
| focus-visible | radius 4px 0px 0px 4px; background rgba(0, 0, 0, 0.06); text ui-sans-serif 14/20 400, #2a2a2a; icon 16 x 16, #2a2a2a; layers none |
| pressed | background rgba(0, 0, 0, 0.06); text ui-sans-serif 14/20 400, #2a2a2a; transition none 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #2a2a2a; layers none |

Child layers that carry the look: button 110.6x32 border 1px solid rgba(0, 0, 0, 0.12) radius 8px 0px 0px 8px.

![Copy page default](components/crops/docs-copy-page-default.png) ![Copy page hover](components/crops/docs-copy-page-hover.png) ![Copy page focus-visible](components/crops/docs-copy-page-focus-visible.png) ![Copy page pressed](components/crops/docs-copy-page-pressed.png)

### Sign in and sign up

The /app/sign-in and /app/sign-up cards: Google / Apple / SSO actions, the email and password fields, the ToS checkbox on sign-up and the disabled submit. Fields were focused and given sample text that was deleted again — nothing was sent.

#### Sign-in card
The sign-in card (Sign in with Google / Apple / SSO, email + password, the disabled submit); captured, never used. Read as `signin-card` on the sign-in page.

**Values (default).** size 360 x 519; background #ffffff `color.neutral.white`; text WaldenburgHF 24/30 600, #0f0f10; icon 20 x 20, #2e2e2e.

![Sign-in card default](components/crops/signin-card-default.png)

#### OAuth button
The "Sign in with Google" action; measured, never pressed — it would leave for the OAuth flow. Read as `oauth-google` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 360 x 46; padding 0px 12px; border 1px solid rgba(0, 0, 0, 0.1); radius 12px; background #ffffff `color.neutral.white`; text Inter 14/20 500, #2e2e2e; transition color 0.075s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.075s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.075s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.075s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.075s cubic-bezier(0.4, 0, 0.2, 1), fill 0.075s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.075s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.075s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.075s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.075s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #2e2e2e |
| hover | border 1px solid rgba(0, 0, 0, 0.16); background rgba(0, 0, 0, 0.02) |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #0f0f10 0px 0px 0px 3.5px |
| pressed | border 1px solid rgba(0, 0, 0, 0.16); background rgba(0, 0, 0, 0.043) `color.neutral.wash-pressed` |

![OAuth button default](components/crops/oauth-google-default.png) ![OAuth button hover](components/crops/oauth-google-hover.png) ![OAuth button focus-visible](components/crops/oauth-google-focus-visible.png) ![OAuth button pressed](components/crops/oauth-google-pressed.png)

#### SSO button
The "Sign in with SSO" action; measured, never pressed. Read as `oauth-sso` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 360 x 46; padding 0px 12px; border 1px solid rgba(0, 0, 0, 0.1); radius 12px; background #ffffff `color.neutral.white`; text Inter 14/20 500, #2e2e2e; transition color 0.075s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.075s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.075s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.075s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.075s cubic-bezier(0.4, 0, 0.2, 1), fill 0.075s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.075s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.075s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.075s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.075s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | border 1px solid rgba(0, 0, 0, 0.16); background rgba(0, 0, 0, 0.02) |
| focus-visible | shadow #ffffff 0px 0px 0px 2px, #0f0f10 0px 0px 0px 3.5px |
| pressed | border 1px solid rgba(0, 0, 0, 0.16); background rgba(0, 0, 0, 0.043) `color.neutral.wash-pressed` |

![SSO button default](components/crops/oauth-sso-default.png) ![SSO button hover](components/crops/oauth-sso-hover.png) ![SSO button focus-visible](components/crops/oauth-sso-focus-visible.png) ![SSO button pressed](components/crops/oauth-sso-pressed.png)

#### Email field
The email input; focused and given sample text that was deleted again — nothing sent. Read as `email-field` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 360 x 46; padding 4px 16px; border 1px solid rgba(0, 0, 0, 0.1); radius 12px; background transparent; text Inter 14/20 400, #0f0f10; placeholder #0f0f10 |
| focused, filled | border 1px solid #0f0f10; shadow #ffffff 0px 0px 0px 0px, #0f0f10 0px 0px 0px 0.5px |

![Email field default](components/crops/email-field-default.png) ![Email field focused](components/crops/email-field-focused.png) ![Email field filled](components/crops/email-field-filled.png)

#### Password field
The password input (with the visibility toggle); focused only — nothing typed, nothing sent. Read as `password-field` on the sign-in page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 360 x 46; padding 4px 40px 4px 16px; border 1px solid rgba(0, 0, 0, 0.1); radius 12px; background transparent; text Inter 14/20 400, #0f0f10; placeholder #0f0f10 |
| focused | border 1px solid #0f0f10; shadow #ffffff 0px 0px 0px 0px, #0f0f10 0px 0px 0px 0.5px |

![Password field default](components/crops/password-field-default.png) ![Password field focused](components/crops/password-field-focused.png)

#### Sign-in submit
The Sign in submit — disabled until the fields validate; measured, never pressed. Read as `signin-submit` on the sign-in page.

**Values (default).** size 360 x 46; padding 0px 12px; radius 12px; background #a3a3a3; text Inter 14/20 500, #e3e3e3; transition color 0.075s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.075s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.075s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.075s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.075s cubic-bezier(0.4, 0, 0.2, 1), fill 0.075s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.075s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.075s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.075s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.075s cubic-bezier(0.4, 0, 0.2, 1).

![Sign-in submit default](components/crops/signin-submit-default.png)

#### Forgot link
The "Forgot your password?" link; measured, never followed. Read as `forgot-link` on the sign-in page.

Not on the page when it was captured.

#### Sign-up link
The "Sign up" link under the card; measured, never followed. Read as `signup-link` on the sign-in page.

Not on the page when it was captured.

#### Sign-up card
The create-account card (SSO / Google, email + password, the ToS checkbox, the disabled submit); captured, never used. Read as `signup-card` on the sign-up page.

**Values (default).** size 360 x 601; background transparent; text WaldenburgHF 24/30 600, #0f0f10; icon 20 x 20, #2e2e2e; layers a.whitespace-nowrap.font-medium 360.0x46.0 rgb(255, 255, 255) T:1px solid rgba(0, 0, 0, 0.1) / R:1px solid rgba(0, 0, 0, 0.1) / B:1px solid rgba(0, 0, 0, 0.1) / L:1px solid rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 12px; button.whitespace-nowrap.font-med.

Child layers that carry the look: a 360x46 background #ffffff `color.neutral.white` border 1px solid rgba(0, 0, 0, 0.1) radius 12px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px; button 360x46 background #ffffff `color.neutral.white` border 1px solid rgba(0, 0, 0, 0.1) radius 12px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px; a 325.6x31 shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(60, 131, 246, 0.5) 0px 0px 0px 0px, transparent 0px 0px 0px 0px.

![Sign-up card default](components/crops/signup-card-default.png)

#### ToS checkbox
The "I agree to the Terms of Service" checkbox; measured unchecked, never toggled. Read as `tos-checkbox` on the sign-up page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 16 x 16; border 1px solid #b8b8b8; radius 6px; background transparent; text Inter 12/16 500, rgba(0, 0, 0, 0.714) |
| focused | background rgba(0, 0, 0, 0.86); text Inter 12/16 500, #ffffff `color.neutral.white`; icon 16 x 12, #ffffff `color.neutral.white` |

![ToS checkbox default](components/crops/tos-checkbox-default.png) ![ToS checkbox focused](components/crops/tos-checkbox-focused.png)

#### Sign-up submit
The Sign up submit — disabled until the form validates; measured, never pressed. Read as `signup-submit` on the sign-up page.

**Values (default).** size 360 x 46; padding 0px 16px; radius 12px; background #a3a3a3; text Inter 14/20 500, #e3e3e3; transition color 0.075s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.075s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.075s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.075s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.075s cubic-bezier(0.4, 0, 0.2, 1), fill 0.075s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.075s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.075s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.075s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.075s cubic-bezier(0.4, 0, 0.2, 1).

![Sign-up submit default](components/crops/signup-submit-default.png)

#### Sign-in link
The "Already registered? Sign in" link under the sign-up card; measured, never followed. Read as `signin-link` on the sign-up page.

Not on the page when it was captured.

### Footer

The light footer: the product / company / resources columns, social icons, language selector and legal.

#### Footer
The footer (a 0x0 <footer> shell whose children paint the product/company/resources columns, social icons, language selector and legal). Read as `footer` on the home page.

Not on the page when it was captured.

#### Footer link
Read as `footer-link` on the home page.

Not on the page when it was captured.

#### Social link
A social link in the footer. Read as `social-icon` on the home page.

Not on the page when it was captured.

### Mobile (390 wide)

The same surface at phone width: the header shrinks to wordmark + Sign up + burger, the menu opens as a sheet with nav rows and the auth actions.

#### Mobile header
Read as `m-header` on the home page at 390 wide.

**Values (default).** size 117 x 36; background transparent; text Inter 17/23.8 400, #000000 `color.brand.ink`; icon 117 x 15, #000000 `color.brand.ink`; layers a.tw-group.tw-outline-none 141.0x36.0 2px solid rgba(0, 0, 0, 0) offset 2px 9999px; button.tw-group.tw-flex 0.0x0.0 2px solid rgba(0, 0, 0, 0) offset 2px; button.tw-group.tw-flex 0.0x0.0 2px solid rgba(0, 0, 0, 0) offset 2px; a.tw-group.tw-flex 0.0x0.0 2px solid rgba(0, 0, 0, 0) offset 2px; button.tw-group.tw-flex 0.0x0.0 2px solid rgba(0, 0, 0, 0) offset 2px; a.tw-group.tw-flex 0.0x0.0 2px solid .

Child layers that carry the look: a 141x36 radius 9999px; button 0x0; button 0x0.

![Mobile header default](components/crops/m-header-default.png)

#### Menu button
The burger toggle that opens the mobile navigation sheet. Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 36 x 36; padding 6px; radius 9999px; background transparent; outline 2px solid transparent, offset 2px; text Inter 17/23.8 400, #000000 `color.brand.ink`; icon 24 x 24, #000000 `color.brand.ink`; layers button.nav-topbar-item.tw-relative 36.0x36.0 2px solid rgba(0, 0, 0, 0) offset 2px 9999px.

Child layers that carry the look: button 36x36 radius 9999px.

![Menu button default](components/crops/m-menu-button-default.png)

#### Mobile menu, open
The opened mobile navigation sheet (the overlay holding the menu links and the auth actions). Read as `m-menu-open` on the home page at 390 wide.

**Values (default).** size 390 x 732; background transparent; text Inter 14/21 400, #ffffff `color.neutral.white`; transform translate(0px, 98px); icon 117 x 15, #000000 `color.brand.ink`; layers div.tw-relative.tw-w-full 390.0x732.0 2px solid rgba(0, 0, 0, 0) offset 2px; a.tw-group.tw-outline-none 141.0x36.0 2px solid rgba(0, 0, 0, 0) offset 2px 9999px; a.tw-items-center.tw-whitespace-nowrap 0.0x0.0 rgb(255, 255, 255) rgb(255, 255, 255) 0px 0px 0px 0px, rgba(0, 0, 0, 0.125) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.04) 0px 1px 1px 0px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px 2px solid rgba(0, 0, 0, .

Child layers that carry the look: div 390x732; a 141x36 radius 9999px; a 0x0 background #ffffff `color.neutral.white` radius 9999px shadow #ffffff `color.neutral.white` 0px 0px 0px 0px, rgba(0, 0, 0, 0.125) 0px 0px 0px 0.5px, rgba(0, 0, 0, 0.04) 0px 1px 1px 0px, rgba(0, 0, 0, 0.04) 0px 2px 4px 0px.

![Mobile menu, open default](components/crops/m-menu-open-default.png)

#### Mobile nav item
A row inside the opened mobile menu. Read as `m-nav-item` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 366 x 44; padding 12px 12px 12px 16px; radius 8px; background transparent; outline 2px solid transparent, offset 2px; text Inter 14/20 500, #000000 `color.brand.ink`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 20 x 20, #a59f97; layers button.tw-group.tw-flex 366.0x44.0 2px solid rgba(0, 0, 0, 0) offset 2px 8px |
| focus-visible | outline 1px solid #2b7fff `color.brand.accent`, offset 2px; layers button.tw-group.tw-flex 366.0x44.0 1px solid rgb(43, 127, 255) offset 2px 8px |

Child layers that carry the look: button 366x44 radius 8px.

![Mobile nav item default](components/crops/m-nav-item-default.png) ![Mobile nav item hover](components/crops/m-nav-item-hover.png) ![Mobile nav item focus-visible](components/crops/m-nav-item-focus-visible.png) ![Mobile nav item pressed](components/crops/m-nav-item-pressed.png)

#### Mobile sign-up
The Sign up action inside the mobile menu; measured, never followed. Read as `m-signup` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 78.03 x 36; padding 0px 14px; radius 9999px; background #000000 `color.brand.ink`; outline 2px solid transparent, offset 2px; text Inter 14/21 400, #ffffff `color.neutral.white`; transition background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), color 0.15s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 1px solid #2b7fff `color.brand.accent`, offset 2px |
| pressed | size 76.47 x 35.28; transform scale(0.98) |

![Mobile sign-up default](components/crops/m-signup-default.png) ![Mobile sign-up hover](components/crops/m-signup-hover.png) ![Mobile sign-up focus-visible](components/crops/m-signup-focus-visible.png) ![Mobile sign-up pressed](components/crops/m-signup-pressed.png)

#### Mobile headline
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 350 x 68; background transparent; text Waldenburg 36/42 300, #000000 `color.brand.ink`; layers ::before rgba(0, 0, 0, 0) 0px none 1; ::after rgba(0, 0, 0, 0) 0px none 1.

![Mobile headline default](components/crops/m-hero-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the ElevenLabs wordmark and its "II" mark, the gradient voice orbs, the Google/Apple/SSO provider glyphs, the social glyphs and the card artwork) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Everything behind the auth card — the ElevenLabs workspace (Studio, Agents Platform, the voice library, API keys, billing and account surfaces) — was never reached. /app redirects to /app/sign-in; the card's fields were measured and given sample text that was deleted again, and the submits were never pressed. What the workspace looks like or how it behaves is not documented here — the marketing pages' claims about it were never verified.

### Pages

- **Sign up, trial and checkout.** Sign up, Get API key, Subscribe, Contact Sales and the plan CTAs were measured or screenshotted, never followed; no account was created and no payment surface was reached.
- **OAuth providers.** Sign in with Google / Apple / SSO and Log in with Google were measured, never pressed — they leave for the providers' flows.
- **Voice playback.** The home playground's Play was pressed once in the shot pass and generated without an account (a public affordance); the voice-orb and sample-card play buttons were measured but not played. Whether repeated use hits an account wall is not documented.
- **Conversational agent.** The "Talk to an agent" / Voice chat launchers were never opened — the agent session may count as a service interaction.
- **External surfaces** (help center, the careers pages, social profiles) are linked from the site but were never opened.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface; the sign-in/sign-up submits were captured in their disabled resting state.
- **The mega-menu auto-closes** a few seconds after it opens; each flyout-child state re-opened it with the Products trigger before reading.

### Themes

The public surface paints light only — the #FDFCFC eggshell field with white cards — and the bundles declare no `.dark` scope or `prefers-color-scheme` rebind; no dark island was captured. The export holds core + light only.

### Fonts

- **Waldenburg / WaldenburgFH, Inter and Geist Mono** are served from eleven-public-cdn.elevenlabs.io; the @font-face blocks live in the cross-origin bundles (harvested src list in raw/css-vars.json). The style guide falls back to system faces — the webfonts are licensed, not shipped.

### Screenshots

- The gradient voice orbs, the card artwork, the blog imagery and the ElevenLabs wordmark in the screenshots are the product's published content — painted media layers, not CSS values; no flat-colour token claims to be them.
- The promo strips vary by page (V4 bar on home, a $1-credits countdown on product pages) and carry live countdown timers; the captured values are point-in-time.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Voice names and samples, plan feature lists, marketing copy and the terms text are the product's content; only frames and components were measured.
