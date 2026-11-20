# Esquire components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from esquire.com on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running page. Nothing was signed into, submitted or bought; the More dropdown, the FAQ accordion and the side panel are local UI toggles, and hover/focus/pressed states were forced. Sign In, Subscribe, Join, story links and the shop.esquire.com outbound links were measured, never followed; the search and newsletter fields were typed into and cleared, never submitted. The OneTrust consent layer was hidden, never answered, and third-party ad/tracker requests were aborted so ad slots read as blank containers.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (90 components, 157 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (157 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: every page paints `light`. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at CSS scale (one CSS pixel per image pixel — mobile fulls are 390 wide); mobile viewport shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| Style section | `/style/` | [default](screenshots/style-light-default.png), [full](screenshots/style-light-full.png) |
| Entertainment section | `/entertainment/` | [default](screenshots/entertainment-light-default.png), [full](screenshots/entertainment-light-full.png) |
| News & Politics section | `/news-politics/` | [default](screenshots/politics-light-default.png), [full](screenshots/politics-light-full.png) |
| Food & Drinks section | `/food-drink/` | [default](screenshots/food-light-default.png), [full](screenshots/food-light-full.png) |
| Cover article | `/entertainment/movies/a71465908/dwayne-johnson-the-rock-interview-2026/` | [default](screenshots/article-light-default.png), [full](screenshots/article-light-full.png) |
| Essay | `/lifestyle/sex/a74076291/ai-chatbots-flirting-texts/` | [default](screenshots/essay-light-default.png), [full](screenshots/essay-light-full.png) |
| Membership offers | `/offers/premium-membership/` | [default](screenshots/offers-light-default.png), [full](screenshots/offers-light-full.png) |
| Premium hub | `/esq-premium-exclusive/` | [default](screenshots/premium-light-default.png), [full](screenshots/premium-light-full.png) |
| Search results | `/search/?q=suits` | [default](screenshots/search-light-default.png), [full](screenshots/search-light-full.png) |
| About | `/about/a26377/about-us/` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-light-default.png), [drawer](screenshots/mobile-home-light-drawer.png), [full](screenshots/mobile-home-light-full.png) |
| Article, phone | `/entertainment/movies/a71465908/dwayne-johnson-the-rock-interview-2026/` | [default](screenshots/mobile-article-light-default.png), [full](screenshots/mobile-article-light-full.png) |
| Style section, phone | `/style/` | [default](screenshots/mobile-style-light-default.png), [full](screenshots/mobile-style-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| More overflow panel | every page | the More toggle in .megaMenu, clicked locally | [more-btn](#more-toggle) opened state + [home-light-menu](screenshots/home-light-menu.png) |
| Side panel | every page (the hamburger) | the hamburger/Open-Sidepanel trigger, clicked locally | [m-drawer](#side-panel) + [mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png) |
| FAQ accordion | membership offers | the collapsible header button, clicked locally | [faq-header](#faq-accordion-header) opened state |
| Sign In / Subscribe / Join / shop links | the nav, plan cards and footer | measured at rest, never followed | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 20 components were given a real keyboard focus. 20 draw an outline ring: `nav-edition` (1px auto #101010, offset 0px), `nav-newsletter` (1px auto #101010, offset 1px), `nav-signin` (1px auto #101010, offset 1px), `nav-subscribe` (1px auto #101010, offset 1px), `nav-search-btn` (1px auto #101010, offset 0px), `nav-link` (1px auto #101010, offset 1px), `nav-subchevron` (1px auto #101010, offset 0px), `more-btn` (1px auto #101010, offset 0px), `newsletter-signup` (1px auto #101010, offset 0px), `footer-link` (1px auto #101010, offset 1px), `sec-see-more` (1px auto #101010, offset 0px), `plan-join` (2px dotted #000000 `core.palette.gray.0`, offset 4px), `faq-header` (1px auto #101010, offset 0px), `gift-cta` (2px dotted #000000 `core.palette.gray.0`, offset 4px), `search-btn` (2px dotted #000000 `core.palette.gray.0`, offset 4px), `search-sort` (on a child: 2px dotted rgb(0, 0, 0) offset 0px), `search-more` (1px auto #101010, offset 0px), `m-hamburger` (1px auto #e59700, offset 0px), `m-drawer-close` (1px auto #e59700, offset 0px), `m-search` (1px auto #e59700, offset 1px).

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.2s | `linear` | transform | m-drawer |
| 0.25s | `ease-in-out` | height | faq-answer |
| 0.3s | `cubic-bezier(0, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, outline-color, stroke, text-decoration-color | m-drawer-close, m-hamburger, more-btn, nav-edition, nav-newsletter, nav-search-btn, nav-signin, nav-subchevron and more |
| 0.3s | `ease-in-out` | all | art-byline, gift-cta, plan-join, search-btn |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Story list card](#story-list-card) | 302 x 132 | - | - | transparent | none | 0 |
| [Rail card](#rail-card) | 302 x 342.8 | - | - | transparent | none | 0 |
| [Section card](#section-card) | 1440 x 1311.58 | - | - | #f5f6f8 `light.background.panel` | none | 10px 40px 30px 40px |
| [Result card](#result-card) | 265 x 212.7 | - | - | transparent | none | 4px 5px 15px 5px |
| [Plan card](#plan-card) | 352 x 250.95 | 1px solid #3b3b3b `light.text.muted` | 10px | #f5f6f8 `light.background.panel` | none | 16px 16px 20px 16px |
| [Related card](#related-card) | 800 x 982 | - | - | transparent | none | 0 |
| [Premium story card](#premium-story-card) | 1200 x 72.8 | - | - | transparent | none | 20px 0px 0px 0px |

## Components

### Navigation and site chrome

The ~155px top chrome shared by every page: the 32px red utility strip (edition switcher, Newsletter), the main bar (211px search field, 296px Esquire wordmark, Sign In, red Subscribe pill) and the .megaMenu category strip with per-item submenu chevrons and the More overflow toggle.

#### Desktop navigation
The full top chrome: the dark utility strip (edition, Newsletter), the main bar (search field, Esquire wordmark, Sign In, Subscribe) and the .megaMenu category strip. Read as `nav` on the home page.

**Values (default).** size 1440 x 155.5; background #ffffff `light.background.page`; text Lausanne 13/18.2 400, #121212 `light.text.ink`; icon 16 x 16, #121212 `light.text.ink`.

![Desktop navigation default](components/crops/nav-default.png)

#### Utility strip
The 32px top utility bar holding the US edition switcher and the Newsletter link. Read as `nav-utility` on the home page.

**Values (default).** size 64.81 x 32; background transparent; text Lausanne 13/18.2 400, #121212 `light.text.ink`; icon 16 x 16, #121212 `light.text.ink`; layers button.hds-do-not-use.inline-flex 64.8x32.0 rgb(255, 58, 48) T:1px solid rgb(255, 58, 48) / R:1px solid rgb(255, 58, 48) / B:1px solid rgb(255, 58, 48) / L:1px solid rgb(255, 58, 48) 1024px; div.css-1gvhv7i.e1c0kr9d1 0.0x0.0 rgb(255, 255, 255) T:1px solid rgb(237, 237, 237) / R:1px solid rgb(237, 237, 237) / B:1px solid rgb(237, 237, 237) / L:1px solid rgb(237, 237, 237); a.hds-do-not-use.inline-f.

Child layers that carry the look: button 64.8x32 background #ff3a30 `light.brand.red` border 1px solid #ff3a30 `light.brand.red` radius 1024px; div 0x0 background #ffffff `light.background.page` border 1px solid #ededed `light.border.soft`; a 0x0 background rgba(255, 56, 46, 0) `light.button.primary-outlined.bg` border 1px solid rgba(255, 255, 255, 0.04).

![Utility strip default](components/crops/nav-utility-default.png)

#### Edition switcher
The "US" edition button in the utility strip; measured, never toggled open beyond a hover. Read as `nav-edition` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 64.81 x 32; padding 0px 12px; border 1px solid #ff3a30 `light.brand.red`; radius 1024px; background #ff3a30 `light.brand.red`; text Lausanne 13/18.2 400, #121212 `light.text.ink`; transition color 0.3s cubic-bezier(0, 0, 0.2, 1), background-color 0.3s cubic-bezier(0, 0, 0.2, 1), border-color 0.3s cubic-bezier(0, 0, 0.2, 1), outline-color 0.3s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0, 0, 0.2, 1), fill 0.3s cubic-bezier(0, 0, 0.2, 1), stroke 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.3s cubic-bezier(0, 0, 0.2, 1); icon 16 x 16, #121212 `light.text.ink` |
| hover | background #ffffff `light.background.page` |
| focus-visible | outline 1px auto #101010, offset 0px |
| pressed | background #fff0f0 `light.button.primary.bg_active` |

![Edition switcher default](components/crops/nav-edition-default.png) ![Edition switcher hover](components/crops/nav-edition-hover.png) ![Edition switcher focus-visible](components/crops/nav-edition-focus-visible.png) ![Edition switcher pressed](components/crops/nav-edition-pressed.png)

#### Newsletter link
The "Newsletter" utility link; measured, never followed. Read as `nav-newsletter` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 125 x 32; padding 0px 12px; border 1px solid #ff3a30 `light.brand.red`; radius 1024px; background #ff3a30 `light.brand.red`; text Lausanne 13/18.2 400, #121212 `light.text.ink`; transition color 0.3s cubic-bezier(0, 0, 0.2, 1), background-color 0.3s cubic-bezier(0, 0, 0.2, 1), border-color 0.3s cubic-bezier(0, 0, 0.2, 1), outline-color 0.3s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0, 0, 0.2, 1), fill 0.3s cubic-bezier(0, 0, 0.2, 1), stroke 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.3s cubic-bezier(0, 0, 0.2, 1); icon 16 x 16, #121212 `light.text.ink` |
| hover | background #ffffff `light.background.page` |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | background #fff0f0 `light.button.primary.bg_active` |

![Newsletter link default](components/crops/nav-newsletter-default.png) ![Newsletter link hover](components/crops/nav-newsletter-hover.png) ![Newsletter link focus-visible](components/crops/nav-newsletter-focus-visible.png) ![Newsletter link pressed](components/crops/nav-newsletter-pressed.png)

#### Wordmark
The Esquire wordmark lockup centred in the main bar (a link home holding the widest inline svg). Read as `nav-logo` on the home page.

**Values (default).** size 296 x 60; background transparent; text sans-serif 16/18.4 400, #121212 `light.text.ink`; transform translate(-148px, 0px).

![Wordmark default](components/crops/nav-logo-default.png)

#### Sign In link
The "Sign In" link to account.esquire.com; measured, never followed. Read as `nav-signin` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 77.41 x 38.3; padding 8px 12px; border 1px solid rgba(255, 255, 255, 0.04); radius 1024px; background rgba(255, 56, 46, 0) `light.button.primary-outlined.bg`; text Lausanne 16/20.3 400, #121212 `light.text.ink`; transition color 0.3s cubic-bezier(0, 0, 0.2, 1), background-color 0.3s cubic-bezier(0, 0, 0.2, 1), border-color 0.3s cubic-bezier(0, 0, 0.2, 1), outline-color 0.3s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0, 0, 0.2, 1), fill 0.3s cubic-bezier(0, 0, 0.2, 1), stroke 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.3s cubic-bezier(0, 0, 0.2, 1) |
| hover | border 1px solid rgba(255, 58, 48, 0.08); background rgba(255, 58, 48, 0.08) |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | border 1px solid rgba(255, 58, 48, 0.16); background rgba(255, 58, 48, 0.16) |

![Sign In link default](components/crops/nav-signin-default.png) ![Sign In link hover](components/crops/nav-signin-hover.png) ![Sign In link focus-visible](components/crops/nav-signin-focus-visible.png) ![Sign In link pressed](components/crops/nav-signin-pressed.png)

#### Subscribe button
The red "Subscribe" call-to-action in the main bar; measured, never followed. Read as `nav-subscribe` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 105.81 x 38.3; padding 8px 12px; border 1px solid #ff3a30 `light.brand.red`; radius 1024px; background #ff3a30 `light.brand.red`; text Lausanne 16/20.3 400, #121212 `light.text.ink`; transition color 0.3s cubic-bezier(0, 0, 0.2, 1), background-color 0.3s cubic-bezier(0, 0, 0.2, 1), border-color 0.3s cubic-bezier(0, 0, 0.2, 1), outline-color 0.3s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0, 0, 0.2, 1), fill 0.3s cubic-bezier(0, 0, 0.2, 1), stroke 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.3s cubic-bezier(0, 0, 0.2, 1) |
| hover | background #ffffff `light.background.page` |
| focus-visible | outline 1px auto #101010, offset 1px |
| pressed | background #fff0f0 `light.button.primary.bg_active` |

![Subscribe button default](components/crops/nav-subscribe-default.png) ![Subscribe button hover](components/crops/nav-subscribe-hover.png) ![Subscribe button focus-visible](components/crops/nav-subscribe-focus-visible.png) ![Subscribe button pressed](components/crops/nav-subscribe-pressed.png)

#### Search field
The header "Search..." input; focused and typed into then cleared — never submitted. Read as `nav-search` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 211.81 x 26.19; padding 4px 2px 4px 12px; background transparent; text Lausanne 14/18.2 400, #121212 `light.text.ink`; placeholder #757575 `light.text.disabled`; ancestors div.flex.items-center bg #ffffff `light.background.page` |

![Search field default](components/crops/nav-search-default.png) ![Search field focused](components/crops/nav-search-focused.png) ![Search field filled](components/crops/nav-search-filled.png)

#### Search icon button
The search-icon submit inside the header search box; measured, never pressed. Read as `nav-search-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 26.19 x 26.19; border 1px solid rgba(18, 18, 18, 0); radius 1024px; background rgba(18, 18, 18, 0); text Lausanne 13/18.2 400, #121212 `light.text.ink`; transition color 0.3s cubic-bezier(0, 0, 0.2, 1), background-color 0.3s cubic-bezier(0, 0, 0.2, 1), border-color 0.3s cubic-bezier(0, 0, 0.2, 1), outline-color 0.3s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0, 0, 0.2, 1), fill 0.3s cubic-bezier(0, 0, 0.2, 1), stroke 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.3s cubic-bezier(0, 0, 0.2, 1); icon 16 x 16, #121212 `light.text.ink` |
| hover | border 1px solid rgba(18, 18, 18, 0.04) `light.button.secondary.bg_hover`; background rgba(18, 18, 18, 0.04) `light.button.secondary.bg_hover` |
| focus-visible | outline 1px auto #101010, offset 0px |
| pressed | border 1px solid rgba(18, 18, 18, 0.08) `light.button.secondary.bg_active`; background rgba(18, 18, 18, 0.08) `light.button.secondary.bg_active` |

![Search icon button default](components/crops/nav-search-btn-default.png) ![Search icon button hover](components/crops/nav-search-btn-hover.png) ![Search icon button focus-visible](components/crops/nav-search-btn-focus-visible.png) ![Search icon button pressed](components/crops/nav-search-btn-pressed.png)

#### Category menu
The .megaMenu category strip under the main bar: Entertainment through Food and Drinks plus the "More" overflow toggle. Read as `megamenu` on the home page.

**Values (default).** size 1440 x 53.2; border B: 1px solid #757575 `light.text.disabled`; background transparent; text Lausanne 16/23.2 400, #121212 `light.text.ink`; icon 16 x 16, #121212 `light.text.ink`; layers div.megaMenu.css-1uwvko7 1440.0x53.2 B:1px solid rgb(117, 117, 117); button.hds-do-not-use.inline-flex 26.0x18.0 rgba(255, 56, 46, 0) T:1px solid rgba(255, 255, 255, 0.04) / R:1px solid rgba(255, 255, 255, 0.04) / B:1px solid rgba(255, 255, 255, 0.04) / L:1px solid rgba(255, 255, 255, 0.04) 1024px; button.hds-do-not-use.inline-flex 26.0x18.0 rgba(255, 56, 46, 0) T:1px solid rgba(255, 255, 255, 0.0; ancestors div.css-zbfy27.eju4swf3 bg #ffffff `light.background.page`.

Child layers that carry the look: div 1440x53.2 border 1px solid #757575 `light.text.disabled`; button 26x18 background rgba(255, 56, 46, 0) `light.button.primary-outlined.bg` border 1px solid rgba(255, 255, 255, 0.04) radius 1024px; button 26x18 background rgba(255, 56, 46, 0) `light.button.primary-outlined.bg` border 1px solid rgba(255, 255, 255, 0.04) radius 1024px.

![Category menu default](components/crops/megamenu-default.png)

#### Category link
A .megaMenu category link ("Entertainment"); measured, never followed. Read as `nav-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 112.61 x 23.2; background transparent; text Lausanne 16/23.2 400, #121212 `light.text.ink` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.hds-do-not-use.no-underline 112.6x23.2 1px auto rgb(16, 16, 16) offset 1px |

![Category link default](components/crops/nav-link-default.png) ![Category link hover](components/crops/nav-link-hover.png) ![Category link focus-visible](components/crops/nav-link-focus-visible.png) ![Category link pressed](components/crops/nav-link-pressed.png)

#### Submenu chevron
The per-category "Open X submenu" chevron button; measured, never toggled. Read as `nav-subchevron` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 26 x 18; padding 0px 4px; border 1px solid rgba(255, 255, 255, 0.04); radius 1024px; background rgba(255, 56, 46, 0) `light.button.primary-outlined.bg`; text Lausanne 13/18.2 400, #121212 `light.text.ink`; transition color 0.3s cubic-bezier(0, 0, 0.2, 1), background-color 0.3s cubic-bezier(0, 0, 0.2, 1), border-color 0.3s cubic-bezier(0, 0, 0.2, 1), outline-color 0.3s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0, 0, 0.2, 1), fill 0.3s cubic-bezier(0, 0, 0.2, 1), stroke 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.3s cubic-bezier(0, 0, 0.2, 1); icon 16 x 16, #121212 `light.text.ink` |
| focus-visible | outline 1px auto #101010, offset 0px |
| pressed | border 1px solid rgba(255, 58, 48, 0.16); background rgba(255, 58, 48, 0.16) |

![Submenu chevron default](components/crops/nav-subchevron-default.png) ![Submenu chevron hover](components/crops/nav-subchevron-hover.png) ![Submenu chevron focus-visible](components/crops/nav-subchevron-focus-visible.png) ![Submenu chevron pressed](components/crops/nav-subchevron-pressed.png)

#### More toggle
The "More" overflow toggle — a local UI toggle; the opened state was measured after clicking it, its links never followed. Read as `more-btn` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, opened) | size 87.61 x 28.2; padding 4px 12px; border 1px solid rgba(255, 255, 255, 0.04); radius 1024px; background rgba(255, 56, 46, 0) `light.button.primary-outlined.bg`; text Lausanne 16/18.2 400, #121212 `light.text.ink`; transition color 0.3s cubic-bezier(0, 0, 0.2, 1), background-color 0.3s cubic-bezier(0, 0, 0.2, 1), border-color 0.3s cubic-bezier(0, 0, 0.2, 1), outline-color 0.3s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0, 0, 0.2, 1), fill 0.3s cubic-bezier(0, 0, 0.2, 1), stroke 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.3s cubic-bezier(0, 0, 0.2, 1); icon 16 x 16, #121212 `light.text.ink` |
| focus-visible | outline 1px auto #101010, offset 0px |
| pressed | border 1px solid rgba(255, 58, 48, 0.16); background rgba(255, 58, 48, 0.16) |

![More toggle default](components/crops/more-btn-default.png) ![More toggle hover](components/crops/more-btn-hover.png) ![More toggle focus-visible](components/crops/more-btn-focus-visible.png) ![More toggle pressed](components/crops/more-btn-pressed.png) ![More toggle opened](components/crops/more-btn-opened.png)

#### More panel
The overflow panel opened by "More" — the hidden sections (Sports, Member Exclusives, For You) plus their submenu links. Read as `more-panel` on the home page.

**Values (default).** size 302 x 92.89; background transparent; text Lausanne 14/20.3 400, #121212 `light.text.ink`; ancestors div.css-96zydn.edouk7815 bg #ffffff `light.background.page`.

![More panel default](components/crops/more-panel-default.png)

### Home page

The landing: the Latest story list (thumbnail rows, 18px Lausanne headlines, BY-line + read-time), the 56px PlayFair cover hero, the MAN AT HIS BEST rail, section bands (Most Read, Entertainment, Watches…), the 846px newsletter band and the 1|2|3 pagination.

#### Ad disclaimer
The "Advertisement - Continue Reading Below" furniture label that sits above each blank ad slot; the slots themselves stay empty because ad requests are aborted. Read as `ad-disclaimer` on the home page.

**Values (default).** size 1280 x 14.84; background transparent; text Lausanne 11/14.85 400, #121212 `light.text.ink`; layers ::before rgb(237, 237, 237) 0px none 1; ::after rgb(237, 237, 237) 0px none 1; div::before.ad-disclaimer.no-print 507.906pxx1px rgb(237, 237, 237); div::after.ad-disclaimer.no-print 507.906pxx1px rgb(237, 237, 237).

Child layers that carry the look: div::before 507.906pxx1px background #ededed `light.border.soft`; div::after 507.906pxx1px background #ededed `light.border.soft`.

![Ad disclaimer default](components/crops/ad-disclaimer-default.png)

#### Section heading
A home-page section heading ("The Latest") — 32px Lausanne. Read as `section-h2` on the home page.

**Values (default).** size 302 x 41.59; background transparent; text Lausanne 32/41.6 400, #121212 `light.text.ink`.

![Section heading default](components/crops/section-h2-default.png)

#### Story list card
A story row in "The Latest": thumbnail, 18px Lausanne headline, byline and read-time. Read as `story-card` on the home page.

**Values (default).** size 302 x 132; background transparent; text Lausanne 12/16.8 400, #3b3b3b `light.text.muted`; icon 16 x 16, #3b3b3b `light.text.muted`.

![Story list card default](components/crops/story-card-default.png)

#### Story headline
An 18px Lausanne story headline in the Latest list. Read as `story-title` on the home page.

**Values (default).** size 214 x 69.61; background transparent; text Lausanne 18/23.2 400, #121212 `light.text.ink`.

![Story headline default](components/crops/story-title-default.png)

#### Story thumbnail
The thumbnail image inside a story list card. Read as `story-thumb` on the home page.

**Values (default).** size 80 x 80; background #ededed `light.border.soft`; text Lausanne 16/18.4 400, transparent.

![Story thumbnail default](components/crops/story-thumb-default.png)

#### Byline
A "BY <AUTHOR>" byline under a story headline. Read as `byline` on the home page.

**Values (default).** size 114.41 x 12; background transparent; text Lausanne 12/16.8 400, #3b3b3b `light.text.muted`.

![Byline default](components/crops/byline-default.png)

#### Read time
The "min read" duration label with its clock icon on a story card. Read as `readtime` on the home page.

**Values (default).** size 86 x 16.8; background transparent; text Lausanne 12/16.8 400, #3b3b3b `light.text.muted`; icon 16 x 16, #3b3b3b `light.text.muted`.

![Read time default](components/crops/readtime-default.png)

#### Eyebrow
The small uppercase red eyebrow ("NEWS" / "STYLE") over a headline. Read as `eyebrow` on the home page.

**Values (default).** size 40.61 x 13; background transparent; text Lausanne 13/18.2 400, #121212 `light.text.ink`.

![Eyebrow default](components/crops/eyebrow-default.png)

#### Hero story
The cover hero headline painted at display size (56px PlayFair). Read as `hero-story` on the home page.

**Values (default).** size 628 x 112; background transparent; text PlayFair 56/56 400, #121212 `light.text.ink`.

![Hero story default](components/crops/hero-story-default.png)

#### Hero dek
The standfirst paragraph under the hero headline. Read as `hero-dek` on the home page.

**Values (default).** size 628 x 52.19; background transparent; text Lausanne 20/26.1 400, #121212 `light.text.ink`.

![Hero dek default](components/crops/hero-dek-default.png)

#### Rail card
A right-rail "MAN AT HIS BEST" style card: thumbnail over a 20px headline with a dek. Read as `rail-card` on the home page.

**Values (default).** size 302 x 342.8; background transparent; text Lausanne 13/18.2 400, #121212 `light.text.ink`; icon 16 x 16, #3b3b3b `light.text.muted`; layers hr.css-1n2oy37.ehvmj2s4 302.0x1.0 rgb(18, 18, 18).

Child layers that carry the look: hr 302x1 background #121212 `light.text.ink`.

![Rail card default](components/crops/rail-card-default.png)

#### Newsletter block
The mid-page "Real journalism and real style" newsletter band: 28px Lausanne pitch, email field, Sign Up button and terms copy. Read as `newsletter-block` on the home page.

**Values (default).** size 942 x 235.31; padding 32px 48px 20px 48px; background #f5f6f8 `light.background.panel`; text Lausanne 13/18.2 400, #121212 `light.text.ink`; icon 24 x 24, #575757 `light.text.subtle`.

![Newsletter block default](components/crops/newsletter-block-default.png)

#### Newsletter field
The "Enter your email address" field; focused and typed into then cleared — never submitted. Read as `newsletter-input` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 368.59 x 36.3; padding 8px 0px; background transparent; text Lausanne 16/20.3 400, #121212 `light.text.ink`; placeholder #757575 `light.text.disabled`; ancestors div.flex.items-center bg #ffffff `light.background.page` |

![Newsletter field default](components/crops/newsletter-input-default.png) ![Newsletter field focused](components/crops/newsletter-input-focused.png) ![Newsletter field filled](components/crops/newsletter-input-filled.png)

#### Sign Up button
The red "Sign Up" submit inside the newsletter band; measured, never pressed. Read as `newsletter-signup` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 85.41 x 28.3; padding 0px 12px; border 1px solid #ff3a30 `light.brand.red`; radius 1024px; background #ff3a30 `light.brand.red`; text Lausanne 16/20.3 400, #121212 `light.text.ink`; transition color 0.3s cubic-bezier(0, 0, 0.2, 1), background-color 0.3s cubic-bezier(0, 0, 0.2, 1), border-color 0.3s cubic-bezier(0, 0, 0.2, 1), outline-color 0.3s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0, 0, 0.2, 1), fill 0.3s cubic-bezier(0, 0, 0.2, 1), stroke 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.3s cubic-bezier(0, 0, 0.2, 1) |
| hover | background #ffffff `light.background.page` |
| focus-visible | outline 1px auto #101010, offset 0px |
| pressed | background #fff0f0 `light.button.primary.bg_active` |

![Sign Up button default](components/crops/newsletter-signup-default.png) ![Sign Up button hover](components/crops/newsletter-signup-hover.png) ![Sign Up button focus-visible](components/crops/newsletter-signup-focus-visible.png) ![Sign Up button pressed](components/crops/newsletter-signup-pressed.png)

#### Pagination
The "1 | 2 | 3" pagination under the story feed; measured, never followed. Read as `pagination` on the home page.

**Values (default).** size 192 x 56.39; padding 12px 0px; background transparent; text Lausanne 14/20.3 400, #121212 `light.text.ink`; icon 24 x 24, #121212 `light.text.ink`; layers a.hds-do-not-use.inline-flex 32.0x32.0 rgba(255, 56, 46, 0) 1024px; a.hds-do-not-use.inline-flex 32.0x32.0 rgb(214, 214, 214) T:1px solid rgb(237, 237, 237) / R:1px solid rgb(237, 237, 237) / B:1px solid rgb(237, 237, 237) / L:1px solid rgb(237, 237, 237) 1024px; a.hds-do-not-use.inline-flex 32.0x32.0 rgb(255, 255, 255) T:1px solid rgba(18, 18, 18, 0) / R:1px solid rgba(18, 18, 18, 0) / B:1px soli; ancestors section.css-1imhwz1.ege0am41 bg #ffffff `light.background.page`.

Child layers that carry the look: a 32x32 background rgba(255, 56, 46, 0) `light.button.primary-outlined.bg` radius 1024px; a 32x32 background #d6d6d6 `light.border.field` border 1px solid #ededed `light.border.soft` radius 1024px; a 32x32 background #ffffff `light.background.page` border 1px solid rgba(18, 18, 18, 0) radius 1024px.

![Pagination default](components/crops/pagination-default.png)

### Section front

A section index (Style): the front title and description, the lead story card and the grid of standard cards, closed by the red-outline See More button.

#### Section title
The section-front title ("Style") — the display word at the top of the front. Read as `sec-h1` on the style section page.

**Values (default).** size 205 x 85; padding 25px 40px 13px 40px; radius 80px; background rgba(0, 0, 0, 0.7); text Lausanne 52/52 400, #ffffff `light.background.page`.

![Section title default](components/crops/sec-h1-default.png)

#### Section description
The standfirst describing the section under its title. Read as `sec-desc` on the style section page.

**Values (default).** size 1200 x 87.59; padding 0px 0px 30px 0px; background transparent; text Lora 18/28.8 700, #000000 `core.palette.gray.0`; layers a 118.0x24.0 B:1px solid rgb(0, 0, 0); a 102.0x24.0 B:1px solid rgb(0, 0, 0); a 57.0x24.0 B:1px solid rgb(0, 0, 0); a 875.5x52.8 B:1px solid rgb(0, 0, 0); a 78.0x24.0 B:1px solid rgb(0, 0, 0); a 138.0x24.0 B:1px solid rgb(0, 0, 0).

Child layers that carry the look: a 118x24 border 1px solid #000000 `core.palette.gray.0`; a 102x24 border 1px solid #000000 `core.palette.gray.0`; a 57x24 border 1px solid #000000 `core.palette.gray.0`.

![Section description default](components/crops/sec-desc-default.png)

#### Section lead card
The lead story card on the section front — the first image-carrying story link on the front. Read as `sec-hero` on the style section page.

**Values (default).** size 1200 x 813; background transparent; text Lausanne 40/48 400, #000000 `core.palette.gray.0`; layers div.css-wjntws.e11w5h812 1200.0x213.0 rgb(245, 246, 248).

Child layers that carry the look: div 1200x213 background #f5f6f8 `light.background.panel`.

![Section lead card default](components/crops/sec-hero-default.png)

#### Section eyebrow
The uppercase eyebrow over the lead story. Read as `sec-eyebrow` on the style section page.

**Values (default).** size 205 x 85; padding 25px 40px 13px 40px; radius 80px; background rgba(0, 0, 0, 0.7); text Lausanne 52/52 400, #ffffff `light.background.page`.

![Section eyebrow default](components/crops/sec-eyebrow-default.png)

#### Section card
A standard story card lower on the section front. Read as `sec-card` on the style section page.

**Values (default).** size 1440 x 1311.58; padding 10px 40px 30px 40px; background #f5f6f8 `light.background.panel`; text Lausanne 44/52.8 400, #000000 `core.palette.gray.0`.

![Section card default](components/crops/sec-card-default.png)

#### See More button
The "See More" pagination ghost button — dark #121212 outline, red text; measured, never pressed. Read as `sec-see-more` on the style section page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 101.61 x 38.3; padding 8px 12px; border 1px solid #121212 `light.text.ink`; radius 1024px; background #ffffff `light.background.page`; text Lausanne 16/20.3 400, #ff3a30 `light.brand.red`; transition color 0.3s cubic-bezier(0, 0, 0.2, 1), background-color 0.3s cubic-bezier(0, 0, 0.2, 1), border-color 0.3s cubic-bezier(0, 0, 0.2, 1), outline-color 0.3s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0, 0, 0.2, 1), fill 0.3s cubic-bezier(0, 0, 0.2, 1), stroke 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.3s cubic-bezier(0, 0, 0.2, 1) |
| hover | background rgba(18, 18, 18, 0.04) `light.button.secondary.bg_hover` |
| focus-visible | outline 1px auto #101010, offset 0px |
| pressed | background rgba(18, 18, 18, 0.08) `light.button.secondary.bg_active` |

![See More button default](components/crops/sec-see-more-default.png) ![See More button hover](components/crops/sec-see-more-hover.png) ![See More button focus-visible](components/crops/sec-see-more-focus-visible.png) ![See More button pressed](components/crops/sec-see-more-pressed.png)

#### About heading
The "About Us" page heading. Read as `about-h1` on the about page.

**Values (default).** size 1140 x 64; background transparent; text PlayFair 64/64 400, #000000 `core.palette.gray.0`.

![About heading default](components/crops/about-h1-default.png)

#### About paragraph
A paragraph on the About Us page. Read as `about-para` on the about page.

**Values (default).** size 644 x 259.17; background transparent; text Lora 18/28.8 400, #000000 `core.palette.gray.0`.

![About paragraph default](components/crops/about-para-default.png)

### Article page

A cover story: the RELATED pill strip, breadcrumb, PlayFair headline with standfirst and byline, hero photograph with caption/credit, the ~628px Lora text column, pull quotes, mid-story block headings and related cards — with the Advertisement furniture left in place over the blanked ad slots.

#### Related strip
The "RELATED" pill row pinned under the nav linking sibling stories; measured, never followed. Read as `related-strip` on the article page.

**Values (default).** size 1440 x 40; background transparent; text SF Pro 14/15.4 700, #000000 `core.palette.gray.0`; layers span.css-6o028r.e1gtgae89 8.0x8.0 rgb(0, 0, 0) 50%; a.e1gtgae84.css-1ylu0af 220.4x32.0 T:1px solid rgb(82, 82, 82) / R:1px solid rgb(82, 82, 82) / B:1px solid rgb(82, 82, 82) / L:1px solid rgb(82, 82, 82) 24px; a.e1gtgae84.css-1ylu0af 272.6x32.0 T:1px solid rgb(82, 82, 82) / R:1px solid rgb(82, 82, 82) / B:1px solid rgb(82, 82, 82) / L:1px solid rgb(82, 82, 82) 24px; a.e1gtgae84.css-1ylu0af 174.5x; ancestors div.css-p4n3k4.e1gtgae80 bg #ffffff `light.background.page`.

Child layers that carry the look: span 8x8 background #000000 `core.palette.gray.0` radius 50%; a 220.4x32 border 1px solid #525252 radius 24px; a 272.6x32 border 1px solid #525252 radius 24px.

![Related strip default](components/crops/related-strip-default.png)

#### Breadcrumb
The section breadcrumb over the headline ("Entertainment › Movies"). Read as `art-breadcrumb` on the article page.

**Values (default).** size 1140 x 34.56; background transparent; text Lausanne 11.20/14.56 400, #525252.

![Breadcrumb default](components/crops/art-breadcrumb-default.png)

#### Article headline
The cover-story headline — large PlayFair display. Read as `art-h1` on the article page.

**Values (default).** size 1140 x 64; background transparent; text PlayFair 64/64 400, #000000 `core.palette.gray.0`.

![Article headline default](components/crops/art-h1-default.png)

#### Standfirst
The intro standfirst under the headline — lighter, larger Lausanne copy. Read as `art-standfirst` on the article page.

**Values (default).** size 1140 x 82.89; background transparent; text Lausanne 21/27.3 400, #515150.

![Standfirst default](components/crops/art-standfirst-default.png)

#### Byline
The author byline link ("By <name>"); measured, never followed. Read as `art-byline` on the article page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 116 x 25.19; background transparent; text Lausanne 14/25.2 400, #161616; transition all 0.3s ease-in-out; layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| hover | text Lausanne 14/25.2 400, #525252 |

![Byline default](components/crops/art-byline-default.png) ![Byline hover](components/crops/art-byline-hover.png)

#### Hero image
The hero photograph under the article header. Read as `art-hero` on the article page.

**Values (default).** size 1440 x 17; background transparent; text sans-serif 16/18.4 400, #000000 `core.palette.gray.0`.

![Hero image default](components/crops/art-hero-default.png)

#### Caption
The photo caption / credit line under the hero. Read as `art-caption` on the article page.

**Values (default).** size 1430 x 16.59; background transparent; text Lausanne 12/15.6 400, #525252.

![Caption default](components/crops/art-caption-default.png)

#### Body paragraph
A body paragraph — Lora 18px on the measure. Read as `art-para` on the article page.

**Values (default).** size 644 x 86.39; background transparent; text Lora 18/28.8 400, #000000 `core.palette.gray.0`.

![Body paragraph default](components/crops/art-para-default.png)

#### Drop-cap paragraph
The lede paragraph whose first letter paints a drop cap. Read as `art-dropcap` on the article page.

**Values (default).** size 644 x 345.56; background transparent; text Lora 18/28.8 400, #000000 `core.palette.gray.0`.

![Drop-cap paragraph default](components/crops/art-dropcap-default.png)

#### Inline story link
An inline text link inside body copy; measured, never followed. Not every story carries one — this story had only the styled SUBSCRIBE CTA, so the link is a gap rather than a mislabelled button. Read as `art-link` on the article page.

Not on the page when it was captured.

#### Pull quote
A display pull quote inside the story. Read as `art-pullquote` on the article page.

**Values (default).** size 644 x 307.77; padding 15px 0px; background transparent; text Lausanne 38/45.6 400, #000000 `core.palette.gray.0`; layers span::before.css-5esr6z.e1ge6zcj1 35pxx35px T:5px solid rgb(255, 58, 48) / R:5px solid rgb(255, 58, 48) / B:5px solid rgb(255, 58, 48) / L:5px solid rgb(255, 58, 48) 100%.

Child layers that carry the look: span::before 35pxx35px border 5px solid #ff3a30 `light.brand.red` radius 100%.

![Pull quote default](components/crops/art-pullquote-default.png)

#### Block heading
A mid-story block heading ("readers also read…"). Read as `art-blockhead` on the article page.

**Values (default).** size 1200 x 52.8; background transparent; text Lausanne 44/52.8 400, #000000 `core.palette.gray.0`.

![Block heading default](components/crops/art-blockhead-default.png)

#### Ad furniture
The "Advertisement - Continue Reading Below" furniture inside the story; the slot below it stays blank because ad requests are aborted. Read as `art-ad` on the article page.

**Values (default).** size 1436.81 x 12.31; background transparent; text Lausanne 11.20/12.32 400, #000000 `core.palette.gray.0`; layers ::before rgb(229, 229, 229) 0px none 1; ::after rgb(229, 229, 229) 0px none 1; div::before.ad-disclaimer.no-print 588.906pxx1px rgb(229, 229, 229); div::after.ad-disclaimer.no-print 588.906pxx1px rgb(229, 229, 229).

Child layers that carry the look: div::before 588.906pxx1px background #e5e5e5; div::after 588.906pxx1px background #e5e5e5.

![Ad furniture default](components/crops/art-ad-default.png)

#### Related card
A related-story card in the tail of the article. Read as `art-related-card` on the article page.

**Values (default).** size 800 x 982; background transparent; text Lausanne 20/24 400, #161616; ancestors section.css-5l71pd.e17377vn1 bg #f5f6f8 `light.background.panel`.

![Related card default](components/crops/art-related-card-default.png)

#### Essay headline
A shorter essay headline — same display treatment as the cover story. Read as `essay-h1` on the essay page.

**Values (default).** size 660 x 171.56; background transparent; text Lausanne 52/57.2 400, #000000 `core.palette.gray.0`.

![Essay headline default](components/crops/essay-h1-default.png)

#### Essay paragraph
A body paragraph on the shorter essay. Read as `essay-para` on the essay page.

**Values (default).** size 612 x 230.38; background transparent; text Lora 18/28.8 400, #000000 `core.palette.gray.0`.

![Essay paragraph default](components/crops/essay-para-default.png)

### Membership offers

The /offers/premium-membership plan page: Choose a Plan over three plan cards (Premium $50/year Best Value, Print + Digital $30/year, Digital Only $25/year) with struck prices, perk lists and red Join buttons; the Compare table, Membership Perks icons, the FAQ accordion and the gift-subscription CTA.

#### Offers heading
"Choose a Plan" — the display heading over the plan grid. Read as `offers-h1` on the membership offers page.

**Values (default).** size 1088 x 36; background transparent; text sans-serif 32/36 700, #121212 `light.text.ink`.

![Offers heading default](components/crops/offers-h1-default.png)

#### Plan card
A membership plan card: plan name, price line, perk list and its Join action. Read as `plan-card` on the membership offers page.

**Values (default).** size 352 x 250.95; padding 16px 16px 20px 16px; border 1px solid #3b3b3b `light.text.muted`; radius 10px; background #f5f6f8 `light.background.panel`; text SF Pro 12/15.96 600, #ffffff `light.background.page`.

![Plan card default](components/crops/plan-card-default.png)

#### Plan name
The plan name ("Premium") heading on a plan card. Read as `plan-name` on the membership offers page.

**Values (default).** size 85.47 x 26.09; padding 4px 8px; border 1px solid #bdbdbd `light.border.divider`; radius 1024px; background #ffffff `light.background.page`; text SF Pro 14/16.1 600, #121212 `light.text.ink`.

![Plan name default](components/crops/plan-name-default.png)

#### Plan price
The "$xx/year" price line on a plan card. Read as `plan-price` on the membership offers page.

**Values (default).** size 35.05 x 24; background transparent; text SF Pro 20/24 400, #575757 `light.text.subtle`.

![Plan price default](components/crops/plan-price-default.png)

#### Plan perk
A perk bullet inside a plan card. Read as `plan-perk` on the membership offers page.

**Values (default).** size 298 x 16.09; background transparent; text SF Pro 14/16.1 400, #121212 `light.text.ink`.

![Plan perk default](components/crops/plan-perk-default.png)

#### Join button
The "Join Premium" primary button on a plan card — links to checkout; measured, never followed. Read as `plan-join` on the membership offers page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 318 x 32; padding 9.6px 18px 5px 18px; border 1px solid #ff3a30 `light.brand.red`; radius 1024px; background #ff3a30 `light.brand.red`; text Lausanne 16/32 400, #000000 `core.palette.gray.0`; transition all 0.3s ease-in-out |
| hover | background #ffffff `light.background.page` |
| focus-visible | outline 2px dotted #000000 `core.palette.gray.0`, offset 4px |
| pressed | background #ffffff `light.background.page` |

![Join button default](components/crops/plan-join-default.png) ![Join button hover](components/crops/plan-join-hover.png) ![Join button focus-visible](components/crops/plan-join-focus-visible.png) ![Join button pressed](components/crops/plan-join-pressed.png)

#### Best Value chip
The "Best Value" badge on the featured plan. Read as `best-value` on the membership offers page.

**Values (default).** size 99.7 x 23.95; background transparent; text SF Pro 12/15.96 600, #ffffff `light.background.page`; transform translate(-49.8516px, 0px); layers div.css-16hzl36.enfk5g712 99.7x24.0 rgb(0, 0, 0) 20px; ancestors div.css-15330ls.enfk5g70 bg #f5f6f8 `light.background.panel`.

Child layers that carry the look: div 99.7x24 background #000000 `core.palette.gray.0` radius 20px.

![Best Value chip default](components/crops/best-value-default.png)

#### Membership Perks heading
The "Membership Perks" section heading on the offers page. Read as `perks-h2` on the membership offers page.

**Values (default).** size 1216 x 56; background transparent; text SF Pro 32/56 700, #000000 `core.palette.gray.0`.

![Membership Perks heading default](components/crops/perks-h2-default.png)

#### FAQ heading
The "Frequently Asked Questions" section heading. Read as `faq-h2` on the membership offers page.

**Values (default).** size 1200 x 48; background transparent; text SF Pro 32/48 700, #000000 `core.palette.gray.0`.

![FAQ heading default](components/crops/faq-h2-default.png)

#### FAQ accordion header
An FAQ collapsible header ("When will my magazine be delivered?") — a local UI toggle; the opened state was measured after clicking it. Read as `faq-header` on the membership offers page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 1200 x 56; padding 20px 10px 0px 10px; background transparent; text SF Pro 20/24 700, #000000 `core.palette.gray.0` |
| hover | opacity 0.8 |
| focus-visible | outline 1px auto #101010, offset 0px; layers button.css-6kn1c7.eupr88z2 1200.0x56.0 1px auto rgb(16, 16, 16) offset 0px |
| pressed, opened | opacity 0.8 |

![FAQ accordion header default](components/crops/faq-header-default.png) ![FAQ accordion header hover](components/crops/faq-header-hover.png) ![FAQ accordion header focus-visible](components/crops/faq-header-focus-visible.png) ![FAQ accordion header pressed](components/crops/faq-header-pressed.png) ![FAQ accordion header opened](components/crops/faq-header-opened.png)

#### FAQ answer
The answer panel revealed by the FAQ header toggle — the region its aria-controls names, or the sibling of the header heading when the attribute is absent; captured only when visible with text. Read as `faq-answer` on the membership offers page.

**Values (default).** size 1200 x 284; padding 0px 0px 4px 0px; background transparent; text SF Pro 16/20 400, #000000 `core.palette.gray.0`; transition height 0.25s ease-in-out.

![FAQ answer default](components/crops/faq-answer-default.png)

#### Gift subscription CTA
The "GIVE A GIFT SUBSCRIPTION" ghost action — red text on white at rest, filling red on hover; measured, never followed. Read as `gift-cta` on the membership offers page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 322.28 x 40.59; padding 9.6px 18px 5px 18px; border 1px solid transparent; radius 1024px; background #ffffff `light.background.page`; text Lausanne 20/24 400, #ff3a30 `light.brand.red`; transition all 0.3s ease-in-out |
| hover | border 1px solid #ffffff `light.background.page`; background #ff3a30 `light.brand.red`; text Lausanne 20/24 400, #ffffff `light.background.page` |
| focus-visible | outline 2px dotted #000000 `core.palette.gray.0`, offset 4px |
| pressed | border 1px solid #ffffff `light.background.page`; background #ff3a30 `light.brand.red`; text Lausanne 20/24 400, #ffffff `light.background.page` |

![Gift subscription CTA default](components/crops/gift-cta-default.png) ![Gift subscription CTA hover](components/crops/gift-cta-hover.png) ![Gift subscription CTA focus-visible](components/crops/gift-cta-focus-visible.png) ![Gift subscription CTA pressed](components/crops/gift-cta-pressed.png)

#### Renewal fine print
The "Cancel anytime…" fine print under the plan grid. Read as `offers-fine` on the membership offers page.

**Values (default).** size 1088 x 16; background transparent; text SF Pro 12/16 700, #000000 `core.palette.gray.0`.

![Renewal fine print default](components/crops/offers-fine-default.png)

#### Premium hub heading
The heading on the /esq-premium-exclusive/ hub. Read as `prem-h1` on the premium hub page.

**Values (default).** size 481 x 90; padding 25px 40px 13px 40px; radius 80px; background transparent; text Lausanne 52/52 400, #000000 `core.palette.gray.0`.

![Premium hub heading default](components/crops/prem-h1-default.png)

#### Premium story card
A member-exclusive story card on the premium hub. Read as `prem-card` on the premium hub page.

**Values (default).** size 1200 x 72.8; padding 20px 0px 0px 0px; background transparent; text Lausanne 44/52.8 400, #000000 `core.palette.gray.0`; ancestors section.css-1l0vm3i.e17377vn1 bg #f5f6f8 `light.background.panel`.

![Premium story card default](components/crops/prem-card-default.png)

### Search

The results page: the 1115x48 search field with the round red submit, the result count, the Sort By popover trigger, 40px-Lausanne result cards and the See More ghost button.

#### Search results field
The big search field on the results page (1115x48); focused and typed into then cleared — never submitted. Read as `search-field` on the search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 1115 x 48; padding 12px; background transparent; text Lausanne 14/18.2 400, #121212 `light.text.ink`; placeholder #757575 `light.text.disabled`; ancestors div.css-1h43vkx.e1ow10r31 bg #ffffff `light.background.page` |

![Search results field default](components/crops/search-field-default.png) ![Search results field focused](components/crops/search-field-focused.png) ![Search results field filled](components/crops/search-field-filled.png)

#### Search submit
The round red search submit beside the field; measured, never pressed. Read as `search-btn` on the search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 46 x 45; padding 13px 12px 10px 12px; border 1px solid #ff3a30 `light.brand.red`; radius 32px; background #ff3a30 `light.brand.red`; text Lausanne 14/18.2 400, #000000 `core.palette.gray.0`; transition all 0.3s ease-in-out |
| hover | background #ffffff `light.background.page` |
| focus-visible | outline 2px dotted #000000 `core.palette.gray.0`, offset 4px |
| pressed | background #ffffff `light.background.page` |

![Search submit default](components/crops/search-btn-default.png) ![Search submit hover](components/crops/search-btn-hover.png) ![Search submit focus-visible](components/crops/search-btn-focus-visible.png) ![Search submit pressed](components/crops/search-btn-pressed.png)

#### Result count
The "N results for keyword <q>" line. Read as `search-count` on the search page.

**Values (default).** size 253 x 28.8; background transparent; text Lora 18/28.8 400, #000000 `core.palette.gray.0`.

![Result count default](components/crops/search-count-default.png)

#### Sort control
The "Sort By: Relevance" popover trigger; measured, never toggled. Read as `search-sort` on the search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible, pressed) | size 238 x 51.19; padding 12px; border 1px solid #d4d4d4; radius 3px; background #ffffff `light.background.page`; text Lausanne 14/25.2 400, #000000 `core.palette.gray.0`; layers ::before rgba(0, 0, 0, 0) 0px none 1 |

![Sort control default](components/crops/search-sort-default.png) ![Sort control hover](components/crops/search-sort-hover.png) ![Sort control focus-visible](components/crops/search-sort-focus-visible.png) ![Sort control pressed](components/crops/search-sort-pressed.png)

#### Result card
A search-result card: thumbnail, 40px Lausanne title, muted dek. Read as `search-card` on the search page.

**Values (default).** size 265 x 212.7; padding 4px 5px 15px 5px; background transparent; text Lausanne 20/24 400, #000000 `core.palette.gray.0`.

![Result card default](components/crops/search-card-default.png)

#### Result title
A 40px Lausanne result title. Read as `search-title` on the search page.

**Values (default).** size 255 x 52; background transparent; text Lausanne 20/24 400, #000000 `core.palette.gray.0`.

![Result title default](components/crops/search-title-default.png)

#### See More button
The red-outline "See More" button at the foot of the results; measured, never pressed. Read as `search-more` on the search page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 101.61 x 38.3; padding 8px 12px; border 1px solid #121212 `light.text.ink`; radius 1024px; background #ffffff `light.background.page`; text Lausanne 16/20.3 400, #ff3a30 `light.brand.red`; transition color 0.3s cubic-bezier(0, 0, 0.2, 1), background-color 0.3s cubic-bezier(0, 0, 0.2, 1), border-color 0.3s cubic-bezier(0, 0, 0.2, 1), outline-color 0.3s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0, 0, 0.2, 1), fill 0.3s cubic-bezier(0, 0, 0.2, 1), stroke 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.3s cubic-bezier(0, 0, 0.2, 1) |
| hover | background rgba(18, 18, 18, 0.04) `light.button.secondary.bg_hover` |
| focus-visible | outline 1px auto #101010, offset 0px |
| pressed | background rgba(18, 18, 18, 0.08) `light.button.secondary.bg_active` |

![See More button default](components/crops/search-more-default.png) ![See More button hover](components/crops/search-more-hover.png) ![See More button focus-visible](components/crops/search-more-focus-visible.png) ![See More button pressed](components/crops/search-more-pressed.png)

### Side panel and overlays

The slide-in side panel the hamburger opens (section links with accordion chevrons, Close button) and the More dropdown panel — both reached by local UI toggles, their links never followed.

#### Side panel
The slide-in side panel the hamburger opens — section links with accordion chevrons; its links were never followed. Read as `m-drawer` on the home page.

**Values (default).** size 390 x 844; background #f5f5f5 `core.palette.gray.96`; text Lausanne 13/18.2 400, #121212 `light.text.ink`; transition transform 0.2s linear; icon 16 x 16, #121212 `light.text.ink`.

![Side panel default](components/crops/m-drawer-default.png)

#### Drawer close
The "Close Sidepanel" icon button; measured, never pressed. Read as `m-drawer-close` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 42 x 42; padding 8px; border 1px solid rgba(18, 18, 18, 0); radius 1024px; background rgba(18, 18, 18, 0); text Lausanne 16/20.3 400, #121212 `light.text.ink`; transition color 0.3s cubic-bezier(0, 0, 0.2, 1), background-color 0.3s cubic-bezier(0, 0, 0.2, 1), border-color 0.3s cubic-bezier(0, 0, 0.2, 1), outline-color 0.3s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0, 0, 0.2, 1), fill 0.3s cubic-bezier(0, 0, 0.2, 1), stroke 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.3s cubic-bezier(0, 0, 0.2, 1); icon 24 x 24, #121212 `light.text.ink` |
| focus-visible | outline 1px auto #e59700, offset 0px |
| pressed | border 1px solid rgba(18, 18, 18, 0.08) `light.button.secondary.bg_active`; background rgba(18, 18, 18, 0.08) `light.button.secondary.bg_active`; outline 1px auto #e59700, offset 0px |

![Drawer close default](components/crops/m-drawer-close-default.png) ![Drawer close hover](components/crops/m-drawer-close-hover.png) ![Drawer close focus-visible](components/crops/m-drawer-close-focus-visible.png) ![Drawer close pressed](components/crops/m-drawer-close-pressed.png)

#### Drawer section link
A section link inside the side panel; measured, never followed. Read as `m-drawer-link` on the home page.

Not on the page when it was captured.

### Footer

The site footer: wordmark, social icon buttons, the link columns and the Hearst legal line.

#### Footer
The site footer: wordmark, social icons, the Newsletter/About Us link columns and the legal line. Read as `footer` on the home page.

**Values (default).** size 1280 x 634.2; background transparent; text Lausanne 14/20.3 400, #121212 `light.text.ink`; layers a.ot-sdk-show-settings.ebnr9ku0 144.8x54.0 T:1px solid rgb(0, 0, 0) / R:1px solid rgb(0, 0, 0) / B:1px solid rgb(0, 0, 0) / L:1px solid rgb(0, 0, 0).

Child layers that carry the look: a 144.8x54 border 1px solid #000000 `core.palette.gray.0`.

![Footer default](components/crops/footer-default.png)

#### Footer link
A footer nav link ("About Us"); measured, never followed. Read as `footer-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 67.2 x 20.3; background transparent; text Lausanne 14/20.3 400, #121212 `light.text.ink` |
| focus-visible | outline 1px auto #101010, offset 1px; layers a.hds-do-not-use.no-underline 67.2x20.3 1px auto rgb(16, 16, 16) offset 1px |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png) ![Footer link pressed](components/crops/footer-link-pressed.png)

#### Social icon link
A square social icon button in the footer (x, tiktok, youtube…); measured, never followed. Read as `footer-social` on the home page.

Not on the page when it was captured.

### Mobile (390 wide)

The home at phone width: the ~154px top chrome (red strip, hamburger, wordmark, search icon), the feed cards and the footer.

#### Mobile navigation
The phone top chrome: red utility strip, hamburger, Esquire wordmark and search icon. Read as `m-nav` on the home page at 390 wide.

**Values (default).** size 390 x 154.2; background #ffffff `light.background.page`; text Lausanne 13/18.2 400, #121212 `light.text.ink`; icon 16 x 16, #121212 `light.text.ink`.

![Mobile navigation default](components/crops/m-nav-default.png)

#### Hamburger
The hamburger button that toggles the side panel — a local UI toggle; the opened state was measured after clicking it. Read as `m-hamburger` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, opened) | size 42 x 42; padding 8px; border 1px solid rgba(18, 18, 18, 0); radius 1024px; background rgba(18, 18, 18, 0); text Lausanne 16/20.3 400, #121212 `light.text.ink`; transition color 0.3s cubic-bezier(0, 0, 0.2, 1), background-color 0.3s cubic-bezier(0, 0, 0.2, 1), border-color 0.3s cubic-bezier(0, 0, 0.2, 1), outline-color 0.3s cubic-bezier(0, 0, 0.2, 1), text-decoration-color 0.3s cubic-bezier(0, 0, 0.2, 1), fill 0.3s cubic-bezier(0, 0, 0.2, 1), stroke 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-from 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-via 0.3s cubic-bezier(0, 0, 0.2, 1), --tw-gradient-to 0.3s cubic-bezier(0, 0, 0.2, 1); icon 24 x 24, #121212 `light.text.ink` |
| focus-visible | outline 1px auto #e59700, offset 0px |
| pressed | border 1px solid rgba(18, 18, 18, 0.08) `light.button.secondary.bg_active`; background rgba(18, 18, 18, 0.08) `light.button.secondary.bg_active` |

![Hamburger default](components/crops/m-hamburger-default.png) ![Hamburger hover](components/crops/m-hamburger-hover.png) ![Hamburger focus-visible](components/crops/m-hamburger-focus-visible.png) ![Hamburger pressed](components/crops/m-hamburger-pressed.png) ![Hamburger opened](components/crops/m-hamburger-opened.png)

#### Mobile wordmark
The Esquire wordmark centred in the phone bar. Read as `m-logo` on the home page at 390 wide.

**Values (default).** size 192 x 48; background transparent; text sans-serif 16/18.4 400, #121212 `light.text.ink`; transform translate(-96px, 0px).

![Mobile wordmark default](components/crops/m-logo-default.png)

#### Mobile search link
The search icon link in the phone bar; measured, never followed. Read as `m-search` on the home page at 390 wide.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 24 x 32; background transparent; text sans-serif 16/18.4 400, #121212 `light.text.ink`; icon 24 x 24, #121212 `light.text.ink` |
| focus-visible | outline 1px auto #e59700, offset 1px; layers a.hds-do-not-use.no-underline 24.0x32.0 1px auto rgb(229, 151, 0) offset 1px |

![Mobile search link default](components/crops/m-search-default.png) ![Mobile search link hover](components/crops/m-search-hover.png) ![Mobile search link focus-visible](components/crops/m-search-focus-visible.png) ![Mobile search link pressed](components/crops/m-search-pressed.png)

#### Mobile story headline
A story headline in the phone feed. Read as `m-story` on the home page at 390 wide.

**Values (default).** size 358 x 36.41; background transparent; text Lausanne 28/36.4 400, #121212 `light.text.ink`.

![Mobile story headline default](components/crops/m-story-default.png)

#### Mobile eyebrow
The uppercase eyebrow over a phone headline. Read as `m-eyebrow` on the home page at 390 wide.

**Values (default).** size 40.61 x 13; background transparent; text Lausanne 13/18.2 400, #121212 `light.text.ink`.

![Mobile eyebrow default](components/crops/m-eyebrow-default.png)

#### Mobile byline
A "BY <AUTHOR>" byline on the phone feed. Read as `m-byline` on the home page at 390 wide.

**Values (default).** size 114.41 x 12; background transparent; text Lausanne 12/16.8 400, #3b3b3b `light.text.muted`.

![Mobile byline default](components/crops/m-byline-default.png)

#### Mobile newsletter
The newsletter band in the phone feed. Read as `m-newsletter` on the home page at 390 wide.

**Values (default).** size 326 x 217.61; background transparent; text Lausanne 16/20.3 400, #121212 `light.text.ink`; icon 24 x 24, #575757 `light.text.subtle`; layers div.flex.items-center 326.0x38.3 rgb(255, 255, 255) T:1px solid rgb(117, 117, 117) / R:1px solid rgb(117, 117, 117) / B:1px solid rgb(117, 117, 117) / L:1px solid rgb(117, 117, 117) 1024px; button.hds-do-not-use.inline-flex 326.0x38.3 rgb(255, 58, 48) T:1px solid rgb(255, 58, 48) / R:1px solid rgb(255, 58, 48) / B:1px solid rgb(255, 58, 48) / L:1px solid rgb(255, 58, 48) 1024px.

Child layers that carry the look: div 326x38.3 background #ffffff `light.background.page` border 1px solid #757575 `light.text.disabled` radius 1024px; button 326x38.3 background #ff3a30 `light.brand.red` border 1px solid #ff3a30 `light.brand.red` radius 1024px.

![Mobile newsletter default](components/crops/m-newsletter-default.png)

#### Mobile footer
The site footer on the phone. Read as `m-footer` on the home page at 390 wide.

**Values (default).** size 358 x 1272.7; background transparent; text Lausanne 14/20.3 400, #121212 `light.text.ink`; layers a.ot-sdk-show-settings.ebnr9ku0 140.8x54.0 T:1px solid rgb(0, 0, 0) / R:1px solid rgb(0, 0, 0) / B:1px solid rgb(0, 0, 0) / L:1px solid rgb(0, 0, 0).

Child layers that carry the look: a 140.8x54 border 1px solid #000000 `core.palette.gray.0`.

![Mobile footer default](components/crops/m-footer-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the glyphs in the crops and screenshots (the wordmark, the social icons, the FRE icons under /_assets/design-tokens/fre/static/icons/) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### Members and external destinations

Esquire has a signed-in product — bookmarks, comment counts, the premium archive — that lives behind Sign In on account.esquire.com and was never opened. The Join buttons lead to checkout on shop.esquire.com and were measured, never followed; premium stories marked with the lock icon render their public lede and are otherwise gated.

### Pages

- **Outbound links.** 'Sign In' (account.esquire.com), 'Subscribe'/'Join' (shop.esquire.com checkout) and every social icon were measured, never followed — they leave the captured domain or start a purchase.
- **Paywalled content.** Premium stories gate below the lede; what the signed-out page paints was captured and the gated remainder is a boundary, not an error.
- **Ad slots.** Third-party ad requests were aborted before they left the browser, so placements read as blank containers under the site's own 'Advertisement - Continue Reading Below' furniture.
- **Infinite surfaces.** The phone article ran to 56,109px and was capped at the kit's 8-chunk bound (recorded on the shot); the desktop article fit at 37,921px.
- **Author archives and topic indexes** exist but were not individually captured; they reuse the section-front card layouts.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **The More panel, FAQ accordion and side panel** were opened by their own triggers (local UI toggles); nothing was typed into or submitted anywhere.
- **The US edition switcher and Sort By popover** were measured at rest only — opening them was not needed for evidence.
- **Disabled, error and loading states** were not seen on the public surface.

### Themes

One painted theme, no toggle: white editorial surfaces with the #ff3a30 brand red — the utility strip, Subscribe pill and Join/Sign-Up buttons — over the FRE token layer (Lausanne UI, PlayFair display, Lora body). The dark overlay surfaces (scrim rgba(18,18,18,.72), the dark side panel) are recorded as surfaces inside the single theme; tokens.json emits light only.

### Fonts

- **Lausanne** (UI), **PlayFair** (display), **Lora** (article body), **Charter** and **Inter** are proprietary Hearst webfonts served from /_assets/design-tokens/; the font files are not shipped in this package. The offers page falls back to "SF Pro" on this Linux box.

### Screenshots

- Photography, cover art and author names shown in stories are the product's published content; only frames and components were measured.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Article text, headlines, captions and photography are the product's content; only frames and components were measured.
