# Delphi components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from www.delphi.co (the catalog's delphi.ai redirects here) on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, bought or submitted; no question was ever asked and no form was ever sent; the Sign-In, Create Your Delphi, Continue, Share, Save and Expand actions were measured, never followed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (51 components, 115 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (114 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png`: every public surface paints `light` (the dark resolution is declared but never shown signed out). Desktop shots are 1440 x 900 at 1x; `-full` pages scroll inside a nested container rather than the document, so they are captured as viewport-tall `partN` tiles and capped at 8 tiles (an inner-scroller boundary recorded in the capture log); mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [signin](screenshots/home-light-signin.png) |
| Discover | `/discover/productivity` | [default](screenshots/discover-light-default.png), [full](screenshots/discover-light-full.png) |
| Search results | `/search/i-want-to-bring-my-different-groups-of-friends-together-and-buil` | [default](screenshots/search-light-default.png), [full](screenshots/search-light-full.png) |
| Expert profile | `/karpathy` | [default](screenshots/expert-light-default.png), [full](screenshots/expert-light-full.png) |
| Chat | `/karpathy/chat` | [default](screenshots/chat-light-default.png), [full](screenshots/chat-light-full.png) |
| Onboarding | `/onboarding` | [dialog](screenshots/onboarding-light-dialog.png), [full](screenshots/onboarding-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png) |
| Chat, phone | `/karpathy/chat` | [default](screenshots/mobile-chat-light-default.png), [full](screenshots/mobile-chat-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Sign-In dialog | / | the header Sign In link routes through /auth and returns with the dialog mounted | [home-light-signin](screenshots/home-light-signin.png), [signin-dialog](#sign-in-dialog), [dialog-google](#continue-with-google), [dialog-email](#continue-with-email) |
| Onboarding route | /onboarding | the public onboarding route mounts the same Sign-In dialog over the home page — creating a clone needs an account | [onboarding-light-dialog](screenshots/onboarding-light-dialog.png) |
| Perspective flip | / | a perspective card's own Read flip | [persp-flip](#perspective-card), [persp-quote](#perspective-quote) |
| Chat composer | /karpathy/chat | typed into then cleared; the submit button only renders once text is in the field and was never pressed | [chat-input](#message-field), [chat-send](#send-button) |
| Ask fields | /, phone / | typed into then cleared — typing does not navigate signed out | [hero-search](#ask-field), [m-search](#mobile-ask-field) |
| Signed-in product | a Delphi account | creating a clone, saving, personalising and every post-login surface needs an account | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 18 components were given a real keyboard focus. 8 draw an outline ring: `nav-topic` (1px auto rgba(253, 84, 0, 0.5), offset 1px), `topic-card` (2px solid #21201c `text.ink`, offset 4px), `persp-flip` (2px solid #fd5400 `border.focus`, offset -5px), `disc-cat` (1px auto rgba(253, 84, 0, 0.5), offset 1px), `disc-ask` (2px solid #21201c `text.ink`, offset 4px), `srch-personalize` (1px auto rgba(253, 84, 0, 0.5), offset 1px), `m-signin` (1px auto rgba(253, 84, 0, 0.5), offset 1px), `m-topic-card` (2px solid #21201c `text.ink`, offset 4px). 9 draw a focus ring as a shadow instead: `signin-btn`, `create-cta`, `mic-btn`, `dialog-google`, `dialog-email`, `share-btn`, `suggested-chip`, `srch-save`, `srch-expand`. The other 1 show no measured change: `chat-send`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.1s | `ease` | all | signin-dialog |
| 0.15s | `cubic-bezier(0.165, 0.84, 0.44, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, box-shadow, color, fill, opacity, outline-color, stroke, text-decoration-color, transform | create-cta, dialog-email, dialog-google, hero-search, m-search, persp-flip, share-btn, signin-btn and more |
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | m-signin, mkt-logo |
| 0.18s | `cubic-bezier(0.165, 0.84, 0.44, 1)` | background-color | disc-card |
| 0.2s | `cubic-bezier(0, 0, 0.2, 1)` | all | disc-cat, nav-topic |
| 0.2s | `cubic-bezier(0.165, 0.84, 0.44, 1)` | box-shadow | srch-expert-card |
| 0.26s | `cubic-bezier(0.165, 0.84, 0.44, 1)` | box-shadow, translate | disc-ask, m-topic-card, topic-card |
| 0.26s | `cubic-bezier(0.22, 1, 0.36, 1)` | box-shadow, transform | disc-card |
| 0.26s | `ease` | border-color | disc-card |
| 0.3s | `cubic-bezier(0, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | srch-personalize |
| 0.3s | `cubic-bezier(0.3, 0.9, 0.25, 1)` | opacity, translate, visibility | m-header, mkt-header |
| 0.4s | `cubic-bezier(0.16, 1, 0.3, 1)` | background-color, box-shadow, color, opacity, transform | chat-send, mic-btn |
| 0.4s | `cubic-bezier(0.7, 0, 0.84, 0)` | opacity, scale, translate | scroll-bottom |
| 1.8s | `cubic-bezier(0.3, 0, 0, 1)` | --quote-glow | srch-expert-card |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Topic card](#topic-card) | 346.66 x 280 | - | 24px | #f7f3f0 `background.warm` | none | 20px |
| [Perspective flip](#perspective-flip) | 272.23 x 360.3 | 1px solid transparent | 28px | transparent | none | 0 |
| [Expert tile](#expert-tile) | 528 x 192 | 1px solid rgba(33, 32, 28, 0.09) `border.hairline` | 24px | #ffffff `background.page` | none | 24px 24px 18px 24px |
| [Ask card](#ask-card) | 346.66 x 280 | - | 24px | #f7f3f0 `background.warm` | none | 20px |
| [Result expert card](#result-expert-card) | 672 x 318 | 1px solid rgba(141, 141, 134, 0.2) `border.card-border` | 26px | #ffffff `background.page` | none | 18px 0px 20px 0px |
| [Suggested question](#suggested-question) | 245.33 x 83.75 | 1px solid transparent | 18px | rgba(141, 141, 134, 0.1) `background.chip` | none | 12px 14px |
| [Sign-in dialog](#sign-in-dialog) | 448 x 360 | - | 26px | #ffffff `background.page` | rgba(33, 32, 28, 0.05) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.1) 0px 8px 10px -6px | 0 |
| [Mobile topic card](#mobile-topic-card) | 350 x 150 | - | 20px | #f7f3f0 `background.warm` | none | 16px 18px |

## Components

### Header and navigation

The public top bar on every surface: the Delphi wordmark, topic nav pills, Sign In and the orange Create Your Delphi CTA.

#### Site header
The fixed top bar: Delphi wordmark, Sign In and the Create Your Delphi pill. Read as `mkt-header` on the home page.

**Values (default).** size 1440 x 64; padding 0px 20px 0px 12px; background transparent; text Delphi Inter 14/20 500, #63635e `text.mid`; transition translate 0.3s cubic-bezier(0.3, 0.9, 0.25, 1), opacity 0.3s cubic-bezier(0.3, 0.9, 0.25, 1), visibility 0.3s cubic-bezier(0.3, 0.9, 0.25, 1); icon 84.5 x 26, #82827c `text.low`; layers ::before rgb(255, 255, 255) 0px none 1; header::before.fixed.inset-x-0 1440pxx0px #ffffff `background.page`; div.absolute.inset-x-0 1440.0x88.0; a.group/button.inline-flex 96.0x36.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 26px; a.group/button.inline-flex 180.0x36.0 #fd5400 `border.focus` T:1px solid rgba(0, 0, 0, 0) .

Child layers that carry the look: header::before 1440pxx0px background #ffffff `background.page`; div 1440x88 image linear-gradient(#ffffff `background.page` 0%, rgba(255, 255, 255, 0.9888) 6.25%, rgba(255,; a 96x36 border 1px solid transparent radius 26px.

![Site header default](components/crops/mkt-header-default.png)

#### Logo
The Delphi mark at the left of the header. Read as `mkt-logo` on the home page.

**Values (default).** size 91.5 x 40; padding 0px 0px 0px 7px; background transparent; text Delphi Inter 16/24 400, #82827c `text.low`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 84.5 x 26, #82827c `text.low`.

![Logo default](components/crops/mkt-logo-default.png)

#### Topic link
A topic link in the header/category strip ("Career & Work"); measured, never followed. Read as `nav-topic` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 79 x 40; padding 10px 16px; radius 3.35544e+07px; background rgba(141, 141, 134, 0.1) `background.chip`; text Delphi Inter 14/20 500, #63635e `text.mid`; transition all 0.2s cubic-bezier(0, 0, 0.2, 1) |
| hover | background rgba(141, 141, 134, 0.15); text Delphi Inter 14/20 500, #21201c `text.ink` |
| focus-visible | outline 1px auto rgba(253, 84, 0, 0.5), offset 1px |
| pressed | size 77.42 x 39.2; background rgba(141, 141, 134, 0.15); text Delphi Inter 14/20 500, #21201c `text.ink` |

![Topic link default](components/crops/nav-topic-default.png) ![Topic link hover](components/crops/nav-topic-hover.png) ![Topic link focus-visible](components/crops/nav-topic-focus-visible.png) ![Topic link pressed](components/crops/nav-topic-pressed.png)

#### Sign In
The header Sign-In action; it opens the auth dialog (measured below), never followed past it. Read as `signin-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 96 x 36; padding 0px 12px; border 1px solid transparent; radius 26px; background transparent; text Delphi Inter 14/20 500, #63635e `text.mid`; transition color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), background-color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), transform 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), opacity 0.15s cubic-bezier(0.165, 0.84, 0.44, 1); icon 13.6 x 13.6, #63635e `text.mid` |
| hover | background rgba(141, 141, 134, 0.1) `background.chip`; text Delphi Inter 14/20 500, #21201c `text.ink`; icon 13.6 x 13.6, #21201c `text.ink` |
| focus-visible | border 1px solid #fd5400 `border.focus`; shadow rgba(253, 84, 0, 0.3) 0px 0px 0px 3px |
| pressed | size 94.08 x 35.28; background rgba(141, 141, 134, 0.1) `background.chip`; text Delphi Inter 14/20 500, #21201c `text.ink`; icon 13.33 x 13.33, #21201c `text.ink` |

![Sign In default](components/crops/signin-btn-default.png) ![Sign In hover](components/crops/signin-btn-hover.png) ![Sign In focus-visible](components/crops/signin-btn-focus-visible.png) ![Sign In pressed](components/crops/signin-btn-pressed.png)

#### Create CTA
The "Create Your Delphi" primary pill in the header; measured, never followed (it starts onboarding). Read as `create-cta` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 180 x 36; padding 0px 12px; border 1px solid transparent; radius 26px; background #fd5400 `border.focus`; text Delphi Inter 14/20 500, #ffffff `background.page`; transition color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), background-color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), transform 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), opacity 0.15s cubic-bezier(0.165, 0.84, 0.44, 1); icon 13.6 x 13.6, #ffffff `background.page` |
| hover | background #df4000 |
| focus-visible | border 1px solid #fd5400 `border.focus`; shadow rgba(253, 84, 0, 0.3) 0px 0px 0px 3px |
| pressed | size 176.4 x 35.28; background #df4000; icon 13.33 x 13.33, #ffffff `background.page` |

![Create CTA default](components/crops/create-cta-default.png) ![Create CTA hover](components/crops/create-cta-hover.png) ![Create CTA focus-visible](components/crops/create-cta-focus-visible.png) ![Create CTA pressed](components/crops/create-cta-pressed.png)

### Home

The home hero: the 50px Pythia display, the ask-anything textarea, topic cards and the perspective flip cards that turn on press.

#### Hero headline
"Find people who’ve been there" — the Pythia serif display heading. Read as `hero-h1` on the home page.

**Values (default).** size 597.25 x 51; background transparent; text Delphi Pythia 50/51 500, #21201c `text.ink`; layers ::before rgba(0, 0, 0, 0) 0px none 1; h1::before.font-heading 821.25pxx115px 50%.

Child layers that carry the look: h1::before 821.25pxx115px image radial-gradient(#fcf8f3 30%, rgba(252, 248, 243, 0.92) 48%, transparent 74%) radius 50%.

![Hero headline default](components/crops/hero-h1-default.png)

#### Ask field
The "Describe your situation" hero textarea — the product’s front door; focused and typed into then cleared, never submitted. Read as `hero-search` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 624 x 52; background transparent; text Delphi Inter 18/26 400, #21201c `text.ink`; transition color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), background-color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.15s cubic-bezier(0.165, 0.84, 0.44, 1); placeholder #63635e `text.mid`; layers textarea.min-w-0.placeholder:text-fg-mid 624.0x52.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px |

![Ask field default](components/crops/hero-search-default.png) ![Ask field focused](components/crops/hero-search-focused.png) ![Ask field filled](components/crops/hero-search-filled.png)

#### Voice button
The "Say your situation" mic button beside the ask field; measured, never pressed (it would start recording). Read as `mic-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 32 x 32; radius 3.35544e+07px; background transparent; text Delphi Inter 14/20 500, #63635e `text.mid`; transition opacity 0.4s cubic-bezier(0.16, 1, 0.3, 1), transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), color 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s cubic-bezier(0.16, 1, 0.3, 1); icon 17 x 17, #63635e `text.mid` |
| focus-visible | shadow rgba(255, 255, 255, 0.992) 0px 0px 0px 1.98098px, rgba(253, 84, 0, 0.990492) 0px 0px 0px 3.96197px; layers button.inline-flex.shrink-0 32.0x32.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(255, 255, 255, 0.992) 0px 0px 0px 1.98098px, oklab(0.67 0.163492 0.147209 / 0.990492) 0px 0px 0px 3.96197px, rgba(0, 0, 0, 0) 0px 0px 0px 0px 3.35544e+07px |
| pressed | background #e9e8e6; text Delphi Inter 14/20 500, #21201c `text.ink`; icon 17 x 17, #21201c `text.ink` |

![Voice button default](components/crops/mic-btn-default.png) ![Voice button hover](components/crops/mic-btn-hover.png) ![Voice button focus-visible](components/crops/mic-btn-focus-visible.png) ![Voice button pressed](components/crops/mic-btn-pressed.png)

#### Topic card
A shuffled topic card ("Ask ex-Googlers about scaling under pressure"); measured, never pressed. Read as `topic-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 346.66 x 280; padding 20px; radius 24px; background #f7f3f0 `background.warm`; image radial-gradient(140% 85% at 50% 118%, rgba(245, 174, 123, 0.27), transparent 72%); text Delphi Pythia 22/25.3 600, #23211f; transition translate 0.26s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.26s cubic-bezier(0.165, 0.84, 0.44, 1); icon 18 x 18, #23211f |
| focus-visible | outline 2px solid #21201c `text.ink`, offset 4px |

![Topic card default](components/crops/topic-card-default.png) ![Topic card hover](components/crops/topic-card-hover.png) ![Topic card focus-visible](components/crops/topic-card-focus-visible.png) ![Topic card pressed](components/crops/topic-card-pressed.png)

#### Expert card
An expert portrait card on the home rail (name, claim, the Read-perspective flip). Read as `persp-card` on the home page.

**Values (default).** size 272 x 360; background transparent; text Delphi Pythia 24/25.2 500, #ffffff `background.page`; icon 20.02 x 20.02, #ffffff `background.page`; layers div.perspective-flip-front 272.2x360.3 #f7f3f0 `background.warm` oklch(0.67 0.22 42) 0px 0px 0px 2px, color(srgb 0.990616 0.33041 -0.139183 / 0.85) 0px 12px 28px -8px 28px; span.portrait-well.relative 272.2x360.3 #f7f3f0 `background.warm`; span.perspective-scrim 272.2x198.2; button.group/button.inline-flex 272.2x360.3 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0.

Child layers that carry the look: div 272.2x360.3 background #f7f3f0 `background.warm` radius 28px shadow #fd5400 `border.focus` 0px 0px 0px 2px, color(srgb 0.990616 0.33041 -0.139183 / 0.85) 0px 12px 28px -8px; span 272.2x360.3 background #f7f3f0 `background.warm`; span 272.2x198.2 image linear-gradient(transparent, rgba(0, 0, 0, 0.35) 50%, rgba(0, 0, 0, 0.8)).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Perspective flip
The "Read <name>’s perspective" card toggle — a local flip, never a navigation. Read as `persp-flip` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 272.23 x 360.3; border 1px solid transparent; radius 28px; background transparent; text Delphi Inter 14/20 500, #63635e `text.mid`; transition color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), background-color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), transform 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), opacity 0.15s cubic-bezier(0.165, 0.84, 0.44, 1) |
| hover | radius 133.769px 133.769px 28px 28px; text Delphi Inter 14/20 500, #21201c `text.ink` |
| focus-visible | border 1px solid #fd5400 `border.focus`; radius 127.551px 127.551px 28px 28px; shadow rgba(253, 84, 0, 0.3) 0px 0px 0px 3px; outline 2px solid #fd5400 `border.focus`, offset -5px |
| pressed | size 266.78 x 353.09; text Delphi Inter 14/20 500, #21201c `text.ink` |

![Perspective flip default](components/crops/persp-flip-default.png) ![Perspective flip hover](components/crops/persp-flip-hover.png) ![Perspective flip focus-visible](components/crops/persp-flip-focus-visible.png) ![Perspective flip pressed](components/crops/persp-flip-pressed.png)

#### Perspective quote
A quoted perspective on a card ("Nir on why we reach for our phones..."). Read as `persp-quote` on the home page.

**Values (default).** size 227.81 x 171.29; background transparent; text Delphi Inter 13/15.86 500, #f0eae4 `text.on-dark`.

![Perspective quote default](components/crops/persp-quote-default.png)

#### Section heading
A home section heading ("Ask people who’ve lived it"). Read as `section-h2` on the home page.

**Values (default).** size 228 x 28; background transparent; text Delphi Inter 20/28 500, #21201c `text.ink`.

![Section heading default](components/crops/section-h2-default.png)

### Auth and onboarding dialogs

The Sign-In dialog — reached via /auth on home and mounted again by /onboarding for signed-out visitors (Continue with Google / Continue with Email — measured, never pressed).

#### Sign-in dialog
The auth dialog opened by the header Sign In (Continue with Google / Continue with Email); its buttons were measured, never pressed. Read as `signin-dialog` on the home page.

**Values (default).** size 448 x 360; radius 26px; background #ffffff `background.page`; shadow rgba(33, 32, 28, 0.05) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.1) 0px 8px 10px -6px; text Delphi Inter 24/32 500, #21201c `text.ink`; transition all 0.1s ease; icon 13.6 x 13.6, #63635e `text.mid`.

![Sign-in dialog default](components/crops/signin-dialog-default.png)

#### Google SSO button
"Continue with Google" inside the auth dialog; measured, never pressed. Read as `dialog-google` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 400 x 40; padding 0px 16px 0px 12px; border 1px solid transparent; radius 26px; background #21201c `text.ink`; text Delphi Inter 14/20 500, #ffffff `background.page`; transition color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), background-color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), transform 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), opacity 0.15s cubic-bezier(0.165, 0.84, 0.44, 1); icon 13.6 x 13.6, #ffffff `background.page` |
| hover | background #63635e `text.mid` |
| focus-visible | border 1px solid #fd5400 `border.focus`; background #63635e `text.mid`; shadow rgba(253, 84, 0, 0.3) 0px 0px 0px 3px |
| pressed | size 392 x 39.2; border 1px solid #fd5400 `border.focus`; background #63635e `text.mid`; shadow rgba(253, 84, 0, 0.3) 0px 0px 0px 3px; icon 13.33 x 13.33, #ffffff `background.page` |

![Google SSO button default](components/crops/dialog-google-default.png) ![Google SSO button hover](components/crops/dialog-google-hover.png) ![Google SSO button focus-visible](components/crops/dialog-google-focus-visible.png) ![Google SSO button pressed](components/crops/dialog-google-pressed.png)

#### Email button
"Continue with Email" inside the auth dialog; measured, never pressed. Read as `dialog-email` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 400 x 40; padding 0px 16px 0px 12px; border 1px solid transparent; radius 26px; background rgba(141, 141, 134, 0.1) `background.chip`; text Delphi Inter 14/20 500, #21201c `text.ink`; transition color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), background-color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), transform 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), opacity 0.15s cubic-bezier(0.165, 0.84, 0.44, 1); icon 13.6 x 13.6, #21201c `text.ink` |
| hover | background rgba(141, 141, 134, 0.15) |
| focus-visible | border 1px solid #fd5400 `border.focus`; background rgba(141, 141, 134, 0.15); shadow rgba(253, 84, 0, 0.3) 0px 0px 0px 3px |
| pressed | size 392 x 39.2; border 1px solid #fd5400 `border.focus`; background rgba(141, 141, 134, 0.15); shadow rgba(253, 84, 0, 0.3) 0px 0px 0px 3px; icon 13.33 x 13.33, #21201c `text.ink` |

![Email button default](components/crops/dialog-email-default.png) ![Email button hover](components/crops/dialog-email-hover.png) ![Email button focus-visible](components/crops/dialog-email-focus-visible.png) ![Email button pressed](components/crops/dialog-email-pressed.png)

### Discover galleries

The /discover/<topic> gallery: the 50px Pythia page title, category pills, quoted perspective cards and the warm ask cards.

#### Gallery headline
"Productivity advice from people who’ve been there" — the topic gallery heading. Read as `disc-h1` on the discover page.

**Values (default).** size 700 x 102; background transparent; text Delphi Pythia 50/51 500, #21201c `text.ink`; layers ::before rgba(0, 0, 0, 0) 0px none 1; h1::before.font-heading 924pxx166px 50%.

Child layers that carry the look: h1::before 924pxx166px image radial-gradient(#fcf8f3 30%, rgba(252, 248, 243, 0.92) 48%, transparent 74%) radius 50%.

![Gallery headline default](components/crops/disc-h1-default.png)

#### Topic chip strip
The category chip strip under the gallery heading (Career & Work / Money & Business / ...). Read as `disc-cats` on the discover page.

**Values (default).** size 1072 x 320.59; background transparent; text Delphi Inter 13/13 400, #63635e `text.mid`; layers span.hl-ripples-paper 1440.0x788.6; span.hl-ripples-warmth 1440.0x544.6; span.breath-fallback.absolute 1440.0x570.6; span.hl-topic-pill 136.0x32.0 #f2eee9 999px; span.hl-topic-pill 158.0x32.0 #f2eee9 999px; span.hl-topic-pill 155.0x32.0 #f2eee9 999px.

Child layers that carry the look: span 1440x788.6 image linear-gradient(#fcf8f3 62%, #f9f9f8); span 1440x544.6 image radial-gradient(520px 300px at 50% 300px, color(srgb 0.990616 0.33041 -0.139183 / 0.04), t; span 1440x570.6 image radial-gradient(80% 52% at 46% 40%, rgba(255, 158, 102, 0.56) 0%, transparent 70%), radial.

![Topic chip strip default](components/crops/disc-cats-default.png)

#### Topic chip
A category chip in the gallery strip; measured, never followed. Read as `disc-cat` on the discover page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 79 x 40; padding 10px 16px; radius 3.35544e+07px; background rgba(141, 141, 134, 0.1) `background.chip`; text Delphi Inter 14/20 500, #63635e `text.mid`; transition all 0.2s cubic-bezier(0, 0, 0.2, 1) |
| hover | background rgba(141, 141, 134, 0.15); text Delphi Inter 14/20 500, #21201c `text.ink` |
| focus-visible | outline 1px auto rgba(253, 84, 0, 0.5), offset 1px |
| pressed | size 77.43 x 39.2; background rgba(141, 141, 134, 0.149813); text Delphi Inter 14/20 500, #21201c `text.ink` |

![Topic chip default](components/crops/disc-cat-default.png) ![Topic chip hover](components/crops/disc-cat-hover.png) ![Topic chip focus-visible](components/crops/disc-cat-focus-visible.png) ![Topic chip pressed](components/crops/disc-cat-pressed.png)

#### Gallery quote
A quoted expert perspective in the gallery. Read as `disc-quote` on the discover page.

**Values (default).** size 227.81 x 149.36; background transparent; text Delphi Inter 13/15.86 500, #f0eae4 `text.on-dark`.

![Gallery quote default](components/crops/disc-quote-default.png)

#### Expert tile
An expert portrait tile in the gallery grid. Read as `disc-card` on the discover page.

**Values (default).** size 528 x 192; padding 24px 24px 18px 24px; border 1px solid rgba(33, 32, 28, 0.09) `border.hairline`; radius 24px; background #ffffff `background.page`; text Delphi Inter 23/29.9 500, #63635e `text.mid`; transition box-shadow 0.26s cubic-bezier(0.22, 1, 0.36, 1), transform 0.26s cubic-bezier(0.22, 1, 0.36, 1), background-color 0.18s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.26s ease.

![Expert tile default](components/crops/disc-card-default.png)

#### Ask card
A gallery "Ask <group> about <topic>" card; measured, never pressed. Read as `disc-ask` on the discover page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 346.66 x 280; padding 20px; radius 24px; background #f7f3f0 `background.warm`; image radial-gradient(140% 85% at 50% 118%, rgba(245, 174, 123, 0.27), transparent 72%); text Delphi Pythia 22/25.3 600, #23211f; transition translate 0.26s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.26s cubic-bezier(0.165, 0.84, 0.44, 1); icon 18 x 18, #23211f |
| focus-visible | outline 2px solid #21201c `text.ink`, offset 4px |

![Ask card default](components/crops/disc-ask-default.png) ![Ask card hover](components/crops/disc-ask-hover.png) ![Ask card focus-visible](components/crops/disc-ask-focus-visible.png) ![Ask card pressed](components/crops/disc-ask-pressed.png)

### Search results

Public /search/<question> results: the pre-filled query field, Top perspectives, expert result cards with credential badges, quotes and Save/Expand actions.

#### Top perspectives
The "Top perspectives" results heading over the quoted answers. Read as `srch-top` on the search page.

**Values (default).** size 150 x 28; background transparent; text Delphi Inter 18/28 500, #63635e `text.mid`.

![Top perspectives default](components/crops/srch-top-default.png)

#### Personalize link
The "Personalize your results" action; measured, never followed. Read as `srch-personalize` on the search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 180 x 20; background transparent; text Delphi Inter 14/20 400, #63635e `text.mid`; transition color 0.3s cubic-bezier(0, 0, 0.2, 1), background-color 0.3s cubic-bezier(0, 0, 0.2, 1), border-color 0.3s cubic-bezier(0, 0, 0.2, 1), outline-color 0.3s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0, 0, 0.2, 1), fill 0.3s cubic-bezier(0, 0, 0.2, 1), stroke 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.3s cubic-bezier(0, 0, 0.2, 1); icon 13.6 x 13.6, #63635e `text.mid` |
| hover | text Delphi Inter 14/20 400, #f48734; icon 13.6 x 13.6, #f48734 |
| focus-visible | outline 1px auto rgba(253, 84, 0, 0.5), offset 1px; layers a.inline-flex.items-center 180.0x20.0 1px auto oklab(0.67 0.163492 0.147209 / 0.5) offset 1px |
| pressed | text Delphi Inter 14/20 400, #f48734; icon 13.6 x 13.6, #f48734 |

![Personalize link default](components/crops/srch-personalize-default.png) ![Personalize link hover](components/crops/srch-personalize-hover.png) ![Personalize link focus-visible](components/crops/srch-personalize-focus-visible.png) ![Personalize link pressed](components/crops/srch-personalize-pressed.png)

#### Result quote
A quoted expert answer in the results. Read as `srch-quote` on the search page.

**Values (default).** size 630 x 82; padding 14px 16px 20px 16px; background transparent; text Delphi Inter 16/24 400, #82827c `text.low`; icon 20 x 20, #63635e `text.mid`; layers ::before color(srgb 0.946353 0.946353 0.943059) 0px none 1; ::after color(srgb 0.946353 0.946353 0.943059) 0px none 1; blockquote::before.perspective-bubble.relative 630pxx82px #f1f1f0 14px; blockquote::after.perspective-bubble.relative 40pxx44px #f1f1f0.

Child layers that carry the look: blockquote::before 630pxx82px background #f1f1f0 image radial-gradient(42% 120% at 50% calc(160%), rgba(253, 84, 0, 0.16) 0%, transparent 100%) radius 14px; blockquote::after 40pxx44px background #f1f1f0.

![Result quote default](components/crops/srch-quote-default.png)

#### Result expert card
An expert result card (portrait, name, role, badges, quoted answer, Save/Expand). Read as `srch-expert-card` on the search page.

**Values (default).** size 672 x 318; padding 18px 0px 20px 0px; border 1px solid rgba(141, 141, 134, 0.2) `border.card-border`; radius 26px; background #ffffff `background.page`; text Delphi Pythia 24/28 600, #21201c `text.ink`; transition box-shadow 0.2s cubic-bezier(0.165, 0.84, 0.44, 1), --quote-glow 1.8s cubic-bezier(0.3, 0, 0, 1); icon 24 x 24, #21201c `text.ink`.

![Result expert card default](components/crops/srch-expert-card-default.png)

#### Credential badge
A credential badge on a result card ("VP OF GLOBAL COMMUNITY AT TORC"). Read as `srch-badge` on the search page.

**Values (default).** size 228 x 20; radius 6px; background rgba(33, 32, 28, 0.06) `background.badge`; text Delphi Pythia 10/20 600, #63635e `text.mid`.

![Credential badge default](components/crops/srch-badge-default.png)

#### Query field
The large query textarea at the top of results, pre-filled with the asked question; focused, never submitted. Read as `srch-field` on the search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 664 x 72; padding 16px 48px 8px 20px; background transparent; text Delphi Inter 16/24 400, #21201c `text.ink`; transition color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), background-color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.15s cubic-bezier(0.165, 0.84, 0.44, 1); placeholder #63635e `text.mid`; layers textarea.min-w-0.resize-none 664.0x72.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px |

![Query field default](components/crops/srch-field-default.png) ![Query field focused](components/crops/srch-field-focused.png)

#### Save button
The card’s "Save" action; measured, never pressed. Read as `srch-save` on the search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 81 x 36; padding 0px 12px 0px 10px; border 1px solid transparent; radius 26px; background transparent; text Delphi Inter 14/20 500, #63635e `text.mid`; transition color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), background-color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), transform 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), opacity 0.15s cubic-bezier(0.165, 0.84, 0.44, 1); icon 13.6 x 13.6, #63635e `text.mid` |
| hover | background rgba(141, 141, 134, 0.1) `background.chip`; text Delphi Inter 14/20 500, #21201c `text.ink`; icon 13.6 x 13.6, #21201c `text.ink` |
| focus-visible | border 1px solid #fd5400 `border.focus`; shadow rgba(253, 84, 0, 0.3) 0px 0px 0px 3px |
| pressed | size 79.38 x 35.28; background rgba(141, 141, 134, 0.1) `background.chip`; text Delphi Inter 14/20 500, #21201c `text.ink`; icon 13.33 x 13.33, #21201c `text.ink` |

![Save button default](components/crops/srch-save-default.png) ![Save button hover](components/crops/srch-save-hover.png) ![Save button focus-visible](components/crops/srch-save-focus-visible.png) ![Save button pressed](components/crops/srch-save-pressed.png)

#### Expand button
The orange "Expand" card action; measured, never followed. Read as `srch-expand` on the search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 97 x 36; padding 0px 10px 0px 12px; border 1px solid transparent; radius 26px; background #fd5400 `border.focus`; text Delphi Inter 14/20 500, #ffffff `background.page`; transition color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), background-color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), transform 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), opacity 0.15s cubic-bezier(0.165, 0.84, 0.44, 1); icon 13.6 x 13.6, #ffffff `background.page` |
| hover | background #df4000 |
| focus-visible | border 1px solid #fd5400 `border.focus`; shadow rgba(253, 84, 0, 0.3) 0px 0px 0px 3px |
| pressed | size 95.06 x 35.28; background #df4000; icon 13.33 x 13.33, #ffffff `background.page` |

![Expand button default](components/crops/srch-expand-default.png) ![Expand button hover](components/crops/srch-expand-hover.png) ![Expand button focus-visible](components/crops/srch-expand-focus-visible.png) ![Expand button pressed](components/crops/srch-expand-pressed.png)

### Expert profile

The public /<expert> profile: portrait, Pythia display name, Share pill, About copy, Experiences and experience items.

#### Expert name
The expert’s display name heading on their public profile. Read as `exp-name` on the expert page.

**Values (default).** size 418.19 x 41.47; padding 0px 23.8px 4.08px 0px; background transparent; text Delphi Pythia 34/37.4 600, #21201c `text.ink`; icon 17 x 17, #21201c `text.ink`.

![Expert name default](components/crops/exp-name-default.png)

#### Expert portrait
The expert’s portrait photo in the profile header. Read as `exp-portrait` on the expert page.

**Values (default).** size 110 x 110; background transparent; text Delphi Inter 16/24 400, transparent.

![Expert portrait default](components/crops/exp-portrait-default.png)

#### Share button
The "Share" profile action; measured, never pressed. Read as `share-btn` on the expert page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 77.81 x 40; padding 0px 16px; border 1px solid transparent; radius 26px; background rgba(33, 32, 28, 0.1) `action.share`; text Delphi Inter 16/24 450, #63635e `text.mid`; transition color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), background-color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), outline-color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), text-decoration-color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), fill 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), stroke 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), --tw-gradient-from 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), --tw-gradient-via 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), --tw-gradient-to 0.15s cubic-bezier(0.165, 0.84, 0.44, 1) |
| focus-visible | border 1px solid #fd5400 `border.focus`; shadow rgba(253, 84, 0, 0.3) 0px 0px 0px 3px |
| pressed | size 76.26 x 39.2; background rgba(33, 32, 28, 0.15); text Delphi Inter 16/24 450, #21201c `text.ink` |

![Share button default](components/crops/share-btn-default.png) ![Share button focus-visible](components/crops/share-btn-focus-visible.png) ![Share button pressed](components/crops/share-btn-pressed.png)

#### About text
The expert’s About copy on the profile. Read as `exp-about` on the expert page.

**Values (default).** size 650 x 48; background transparent; text Delphi Inter 16/24 400, #82827c `text.low`.

![About text default](components/crops/exp-about-default.png)

#### Profile section
A profile section heading ("Experiences"). Read as `exp-section` on the expert page.

**Values (default).** size 672 x 22.5; background transparent; text Delphi Inter 18/22.5 500, #161615 `text.strong`.

![Profile section default](components/crops/exp-section-default.png)

#### Experience item
A listed experience on the profile. Read as `exp-exp-item` on the expert page.

**Values (default).** size 655 x 77.5; padding 14px 12px 0px 6px; radius 20px; background transparent; text Delphi Inter 14/20 400, #6b6b67; layers div.mt-3.5.h-px 637.0x1.0 rgba(28, 24, 20, 0.06).

Child layers that carry the look: div 637x1 background rgba(28, 24, 20, 0.06).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

### Chat surface

The public /<expert>/chat surface: greeting, suggested-question chips, the composer (typed into and cleared, never sent), the 48px send button and the terms line.

#### Chat expert name
The expert’s name in the chat header. Read as `chat-name` on the chat page.

**Values (default).** size 163 x 80; background transparent; text Delphi Inter 14/20 500, #21201c `text.ink`; icon 13.6 x 13.6, #63635e `text.mid`; layers span.avatar-squircle.group/avatar 48.0x48.0 #ffffff `background.page` T:1px solid oklab(0.641239 -0.00290832 0.00981319 / 0.12) / R:1px solid oklab(0.641239 -0.00290832 0.00981319 / 0.12) / B:1px solid oklab(0.641239 -0.00290832 0.00981319 / 0.12) / L:1px solid oklab(0.641239 -0.00290832 0.00981319 / 0.12) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px.

Child layers that carry the look: span 48x48 background #ffffff `background.page` border 1px solid rgba(141, 141, 134, 0.12) radius 28% shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 32.25px 32.25px 0px, rgba(0, 0, 0, 0.1) 0px 17.2px 17.2px -8.6px, rgba(0, 0, 0, 0.03) 0px 8.6px 8.6px -4.3px, rgba(0, 0, 0, 0.05) 0px 4.3px 4.3px -2.15px, rgba(0, 0, 0, 0.05) 0px 1.075px 1.075px -0.538px, rgba(255, 255, 255, 0.5) 0px 2px 4px 0px inset, rgba(255, 255, 255, 0.4) 0px -2px 4px 0px inset; span 46x46 radius 28% shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(255, 255, 255, 0.5) 0px 2px 4px 0px inset, rgba(255, 255, 255, 0.4) 0px -2px 4px 0px inset; div 163x34 background #ffffff `background.page` border 1px solid rgba(141, 141, 134, 0.12) radius 3.35544e+07px shadow rgba(0, 0, 0, 0.1) 0px 2px 12px -2px, rgba(0, 0, 0, 0.08) 0px 4px 20px -4px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Greeting bubble
The clone’s opening message ("Hi there. What problem you trying to solve?"). Read as `chat-greeting` on the chat page.

**Values (default).** size 287 x 20; background transparent; text Delphi Inter 14/20 400, #63635e `text.mid`.

![Greeting bubble default](components/crops/chat-greeting-default.png)

#### Suggested label
The "Suggested" label over the starter questions. Read as `suggested-label` on the chat page.

**Values (default).** size 752 x 26; background transparent; text Delphi Inter 12/16 500, #82827c `text.low`; icon 8.5 x 8.5, #82827c `text.low`; layers button.group/button.inline-flex 88.0x26.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0); button.group/button.inline-flex 20.0x20.0 T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0).

Child layers that carry the look: button 88x26 border 1px solid transparent; button 20x20 border 1px solid transparent.

![Suggested label default](components/crops/suggested-label-default.png)

#### Suggested question
A suggested starter question chip; measured, never pressed — pressing it would send the question. Read as `suggested-chip` on the chat page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 245.33 x 83.75; padding 12px 14px; border 1px solid transparent; radius 18px; background rgba(141, 141, 134, 0.1) `background.chip`; text Delphi Inter 14/19.25 500, #21201c `text.ink`; transition color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), background-color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), transform 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), opacity 0.15s cubic-bezier(0.165, 0.84, 0.44, 1) |
| hover | background rgba(141, 141, 134, 0.15) |
| focus-visible | border 1px solid #fd5400 `border.focus`; shadow rgba(253, 84, 0, 0.3) 0px 0px 0px 3px |
| pressed | size 240.42 x 82.07; background rgba(141, 141, 134, 0.15) |

![Suggested question default](components/crops/suggested-chip-default.png) ![Suggested question hover](components/crops/suggested-chip-hover.png) ![Suggested question focus-visible](components/crops/suggested-chip-focus-visible.png) ![Suggested question pressed](components/crops/suggested-chip-pressed.png)

#### Message field
The "Send a message..." composer; focused and typed into then cleared, never submitted. Read as `chat-input` on the chat page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 592 x 52; padding 12px 4px 12px 12px; background transparent; shadow #21201c 0px 0px 0px 0px; text Delphi Inter 18/28 400, #21201c `text.ink`; placeholder #82827c `text.low`; layers textarea.text-fg-high.placeholder:text-fg-low 592.0x52.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(33, 32, 28) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px |

![Message field default](components/crops/chat-input-default.png) ![Message field focused](components/crops/chat-input-focused.png) ![Message field filled](components/crops/chat-input-filled.png)

#### Send button
The composer submit button — it only renders once text is in the field; its states were measured but it was never pressed, and the text was cleared. Read as `chat-send` on the chat page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 48 x 48; radius 3.35544e+07px; background #fd5400 `border.focus`; shadow rgba(0, 0, 0, 0.05) 0px 24.348px 24.348px 0px, rgba(239, 5, 240, 0) 0px 12.986px 12.986px -6.493px, rgba(0, 0, 0, 0.05) 0px 6.493px 6.493px -3.246px, rgba(0, 0, 0, 0.05) 0px 3.246px 3.246px -1.623px, rgba(239, 95, 0, 0.05) 0px 0.812px 0.812px -0.406px, rgba(0, 0, 0, 0.04) 0px 0px 0px 0.812px, rgba(255, 255, 255, 0.2) 0px -1.623px 1.623px 0px inset, rgba(255, 255, 255, 0.2) 0px 1.623px 1.623px 0px inset; text Delphi Inter 14/20 500, #ffffff `background.page`; transition opacity 0.4s cubic-bezier(0.16, 1, 0.3, 1), transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.4s cubic-bezier(0.16, 1, 0.3, 1), color 0.4s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s cubic-bezier(0.16, 1, 0.3, 1); icon 17 x 17, #ffffff `background.page` |
| pressed | size 45.6 x 45.6; icon 16.15 x 16.15, #ffffff `background.page` |

![Send button default](components/crops/chat-send-default.png) ![Send button hover](components/crops/chat-send-hover.png) ![Send button focus-visible](components/crops/chat-send-focus-visible.png) ![Send button pressed](components/crops/chat-send-pressed.png)

#### Scroll-to-bottom
The "Scroll to bottom" helper pill; measured, never pressed. Read as `scroll-bottom` on the chat page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 30.4 x 30.4; border 1px solid rgba(141, 141, 134, 0.12); radius 3.35544e+07px; background #ffffff `background.page`; shadow rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px -1px; text Delphi Inter 14/20 500, #63635e `text.mid`; transition translate 0.4s cubic-bezier(0.7, 0, 0.84, 0), scale 0.4s cubic-bezier(0.7, 0, 0.84, 0), opacity 0.4s cubic-bezier(0.7, 0, 0.84, 0); opacity 0; icon 12.92 x 12.92, #63635e `text.mid` |
| pressed | size 31.36 x 31.36; border 1px solid #8d8d86; text Delphi Inter 14/20 500, #21201c `text.ink`; icon 13.33 x 13.33, #21201c `text.ink` |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Scroll-to-bottom default](components/crops/scroll-bottom-default.png) ![Scroll-to-bottom hover](components/crops/scroll-bottom-hover.png) ![Scroll-to-bottom pressed](components/crops/scroll-bottom-pressed.png)

#### Terms line
The "By using this service, you..." terms line under the composer. Read as `chat-terms` on the chat page.

**Values (default).** size 429.25 x 16; padding 0px 0px 0px 8px; background transparent; text Delphi Inter 12/16 400, #63635e `text.mid`; layers a.border-b.border-sand-9/40 97.2x16.0 B:1px solid oklab(0.641239 -0.00290832 0.00981319 / 0.4); a.border-b.border-sand-9/40 77.8x16.0 B:1px solid oklab(0.641239 -0.00290832 0.00981319 / 0.4).

Child layers that carry the look: a 97.2x16 border 1px solid rgba(141, 141, 134, 0.4); a 77.8x16 border 1px solid rgba(141, 141, 134, 0.4).

![Terms line default](components/crops/chat-terms-default.png)

### Mobile (390 wide)

The phone surface at 390 wide: the mobile top bar, hero, ask field and topic cards.

#### Mobile header
The phone top bar: wordmark, Sign In, Create pill. Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 64; padding 0px 20px 0px 12px; background transparent; text Delphi Inter 14/20 500, #ffffff `background.page`; transition translate 0.3s cubic-bezier(0.3, 0.9, 0.25, 1), opacity 0.3s cubic-bezier(0.3, 0.9, 0.25, 1), visibility 0.3s cubic-bezier(0.3, 0.9, 0.25, 1); icon 84.5 x 26, #82827c `text.low`; layers ::before rgb(255, 255, 255) 0px none 1; header::before.fixed.inset-x-0 390pxx0px #ffffff `background.page`; div.absolute.inset-x-0 390.0x88.0; a.group/button.inline-flex 102.0x36.0 #fd5400 `border.focus` T:1px solid rgba(0, 0, 0, 0) / R:1px solid rgba(0, 0, 0, 0) / B:1px solid rgba(0, 0, 0, 0) / L:1px solid rgba(0, 0, 0, 0) 26px.

Child layers that carry the look: header::before 390pxx0px background #ffffff `background.page`; div 390x88 image linear-gradient(#ffffff `background.page` 0%, rgba(255, 255, 255, 0.9888) 6.25%, rgba(255,; a 102x36 background #fd5400 `border.focus` border 1px solid transparent radius 26px.

![Mobile header default](components/crops/m-header-default.png)

#### Mobile Sign In
The Sign-In action on the phone header; measured, never followed. Read as `m-signin` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 42 x 17.88; background transparent; text Delphi Inter 13/17.87 400, #82827c `text.low`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| focus-visible | outline 1px auto rgba(253, 84, 0, 0.5), offset 1px; layers a.text-fg-low.text-[13px] 42.0x17.9 1px auto oklab(0.67 0.163492 0.147209 / 0.5) offset 1px |

![Mobile Sign In default](components/crops/m-signin-default.png) ![Mobile Sign In hover](components/crops/m-signin-hover.png) ![Mobile Sign In focus-visible](components/crops/m-signin-focus-visible.png) ![Mobile Sign In pressed](components/crops/m-signin-pressed.png)

#### Mobile headline
The phone hero heading. Read as `m-h1` on the home page at 390 wide.

**Values (default).** size 350 x 65.25; background transparent; text Delphi Pythia 32/32.64 500, #21201c `text.ink`; layers ::before rgba(0, 0, 0, 0) 0px none 1; h1::before.font-heading 390pxx121.25px 50%.

Child layers that carry the look: h1::before 390pxx121.25px image radial-gradient(#fcf8f3 30%, rgba(252, 248, 243, 0.92) 48%, transparent 74%) radius 50%.

![Mobile headline default](components/crops/m-h1-default.png)

#### Mobile ask field
The ask textarea on the phone hero; focused and typed then cleared, never submitted. Read as `m-search` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 342 x 52; background transparent; text Delphi Inter 18/26 400, #21201c `text.ink`; transition color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), background-color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), border-color 0.15s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.15s cubic-bezier(0.165, 0.84, 0.44, 1); placeholder #63635e `text.mid`; layers textarea.min-w-0.placeholder:text-fg-mid 342.0x52.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px |

![Mobile ask field default](components/crops/m-search-default.png) ![Mobile ask field focused](components/crops/m-search-focused.png) ![Mobile ask field filled](components/crops/m-search-filled.png)

#### Mobile topic card
A topic card on the phone rail; measured, never pressed. Read as `m-topic-card` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 350 x 150; padding 16px 18px; radius 20px; background #f7f3f0 `background.warm`; image radial-gradient(140% 85% at 50% 118%, rgba(245, 174, 123, 0.27), transparent 72%); text Delphi Pythia 20/23 600, #23211f; transition translate 0.26s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.26s cubic-bezier(0.165, 0.84, 0.44, 1); icon 18 x 18, #23211f |
| focus-visible | outline 2px solid #21201c `text.ink`, offset 4px |

![Mobile topic card default](components/crops/m-topic-card-default.png) ![Mobile topic card hover](components/crops/m-topic-card-hover.png) ![Mobile topic card focus-visible](components/crops/m-topic-card-focus-visible.png) ![Mobile topic card pressed](components/crops/m-topic-card-pressed.png)

#### Mobile footer
The phone footer. Read as `m-footer` on the home page at 390 wide.

**Values (default).** size 390 x 372.75; padding 0px 20px 24px 20px; background transparent; text Delphi Inter 14/20 400, #63635e `text.mid`; icon 78 x 24, #21201c `text.ink`; layers div.shrink-0.data-horizontal:h-px 350.0x1.0 rgba(141, 141, 134, 0.12).

Child layers that carry the look: div 350x1 background rgba(141, 141, 134, 0.12).

![Mobile footer default](components/crops/m-footer-default.png)

### Footer

The sitemap footer on the long-scroll surfaces.

#### Site footer
The sitemap footer (Discover / About Delphi / Blog / Premium...). Read as `site-footer` on the home page.

**Values (default).** size 1152 x 242.88; padding 0px 40px 24px 40px; background transparent; text Delphi Inter 14/20 400, #63635e `text.mid`; icon 78 x 24, #21201c `text.ink`; layers div.shrink-0.data-horizontal:h-px 1072.0x1.0 rgba(141, 141, 134, 0.12).

Child layers that carry the look: div 1072x1 background rgba(141, 141, 134, 0.12).

![Site footer default](components/crops/site-footer-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Delphi mark, the mic glyph, the send arrow, expert portraits) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Creating a Delphi (a personal clone), saving perspectives, personalising results and every post-login surface need an account and were never reached. What is genuinely public signed out: the marketing home, /discover/<topic> galleries, /search/<question> result pages, /<expert> profiles and /<expert>/chat conversations. A chat message was never sent — the submit button's states were measured with text in the field, then the text was cleared, so what the clone would answer is unverified.

### Pages

- **Create and auth.** /auth mounts the Sign-In dialog on home and /onboarding mounts the same dialog for signed-out visitors — the create-a-clone flow itself is behind an account. Both were measured as dialogs and every Continue/Sign-In action was never pressed.
- **Send and follow actions.** Submit message, Save, Expand, Share, Personalize, the suggested-question chips and every mic/voice button were measured, never followed or pressed where pressing would act.
- **delphi.ai redirects to www.delphi.co**; the catalog keeps the product's listed domain and the package captures the redirect's destination.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were not seen on the public surface.
- **sr-only headings are real but invisible**: profile sections carry screen-reader `h2`s at 1x1 alongside the visible headings; selectors exclude `.sr-only`.

### Themes

Every public surface paints the light theme signed out. The stylesheet genuinely declares both themes (425 resolved variables each, 276 that differ — the dark surface is reachable in the app behind an account or preference), so tokens.json keeps real light and dark sets even though the dark values are declared, not painted.

### Fonts

- **Delphi Inter** (UI text), **Delphi Pythia** (display headings, quotes, badges) and **Delphi Geist Mono** (declared @font-face, not exercised on the public surface) are the served faces. They are served from Delphi's CDN; the style guide falls back to system fonts.

### Screenshots

- Long pages scroll inside a nested container, not the document, so full-page shots are viewport-tall `partN` tiles capped at 8 tiles — the inner-scroller cap is a real capture boundary (home is ~8.7k px tall on mobile).
- A transient edge challenge appeared twice during capture (mobile-home, onboarding) and cleared on retry; no route stayed blocked.
- Expert portraits, names and quoted answers are the product's published content; screenshots are 256-colour PNGs, read exact colours from the tokens or the raw files.

### Content left out

- Expert names, quotes, bios and portraits are the product's content; only frames and components were measured.
