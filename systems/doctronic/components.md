# Doctronic components

The discovery list of every page and view captured, then one entry per component with crops of the real product, and the Gaps. Captured from www.doctronic.ai on 2026-11-13, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844, the Dark group on the site's real data-theme="dark" theme), with computed styles read from the running page. Nothing was signed into, created, submitted or sent: the chat composer was given sample text that was deleted again, Send/Start chat and every sign-in action were never pressed.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (100 components, 197 states). The page layouts are described in [patterns.md](patterns.md).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `SF Pro 14/21 500, #21252e`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (191 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-{theme}-state.png`: the app surfaces (home, /chat/, the symptom checker, the resource center, the blog, telehealth and our-philosophy) were captured in both `light` and `dark`; the rest paint `light` only. Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-{theme}-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| Home | `/` | [composer-focused](screenshots/home-dark-composer-focused.png), [default](screenshots/home-dark-default.png), [full](screenshots/home-dark-full.png), [menu](screenshots/home-dark-menu.png), [composer-focused](screenshots/home-light-composer-focused.png), [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [menu](screenshots/home-light-menu.png) |
| Chat (signed out) | `/chat/` | [default](screenshots/chat-dark-default.png), [filled](screenshots/chat-dark-filled.png), [sidebar](screenshots/chat-dark-sidebar.png), [default](screenshots/chat-light-default.png), [filled](screenshots/chat-light-filled.png), [sidebar](screenshots/chat-light-sidebar.png) |
| Sign-in dialog | `/?modal=signin` | [signin](screenshots/chat-signin-light-signin.png) |
| Symptom checker | `/symptom-checker/` | [default](screenshots/symptom-checker-dark-default.png), [full](screenshots/symptom-checker-dark-full.png), [default](screenshots/symptom-checker-light-default.png), [full](screenshots/symptom-checker-light-full.png) |
| Resource center | `/resource-center/` | [default](screenshots/resource-center-dark-default.png), [full](screenshots/resource-center-dark-full.png), [default](screenshots/resource-center-light-default.png), [full](screenshots/resource-center-light-full.png) |
| Blog | `/blog/` | [default](screenshots/blog-dark-default.png), [full](screenshots/blog-dark-full.png), [search](screenshots/blog-dark-search.png), [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png), [search](screenshots/blog-light-search.png) |
| Telehealth | `/telehealth/` | [default](screenshots/telehealth-dark-default.png), [full](screenshots/telehealth-dark-full.png), [default](screenshots/telehealth-light-default.png), [full](screenshots/telehealth-light-full.png) |
| Urology (condition page) | `/urology/` | [default](screenshots/urology-light-default.png), [full](screenshots/urology-light-full.png) |
| Our philosophy | `/our-philosophy/` | [default](screenshots/our-philosophy-dark-default.png), [full](screenshots/our-philosophy-dark-full.png), [default](screenshots/our-philosophy-light-default.png), [full](screenshots/our-philosophy-light-full.png) |
| Authors | `/authors/` | [default](screenshots/authors-light-default.png), [full](screenshots/authors-light-full.png) |
| Careers | `/careers/` | [default](screenshots/careers-light-default.png), [full](screenshots/careers-light-full.png) |
| Online treatment | `/online-treatment/` | [default](screenshots/online-treatment-light-default.png), [full](screenshots/online-treatment-light-full.png) |
| GLP-1 prescriptions | `/prescription-glp-1/` | [default](screenshots/prescription-glp-1-light-default.png), [full](screenshots/prescription-glp-1-light-full.png) |
| Wall of Love | `/wall-of-love/` | [default](screenshots/wall-of-love-light-default.png), [full](screenshots/wall-of-love-light-full.png) |
| About | `/about/` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| Privacy policy | `/privacy-policy/` | [default](screenshots/privacy-policy-light-default.png) |
| Partnerships article | `/strategic-partnerships-driving-healthcare-innovation/` | [default](screenshots/partnerships-light-default.png), [full](screenshots/partnerships-light-full.png) |
| Home, phone | `/` | [default](screenshots/mobile-home-dark-default.png), [full](screenshots/mobile-home-dark-full.png), [menu](screenshots/mobile-home-dark-menu.png), [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [menu](screenshots/mobile-home-light-menu.png) |
| Chat, phone | `/chat/` | [default](screenshots/mobile-chat-dark-default.png), [default](screenshots/mobile-chat-light-default.png) |
| Symptom checker, phone | `/symptom-checker/` | [default](screenshots/mobile-symptom-checker-light-default.png), [full](screenshots/mobile-symptom-checker-light-full.png) |
| Blog, phone | `/blog/` | [default](screenshots/mobile-blog-light-default.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Site-menu drawer | home, the menu button | the header menu button's own toggle, closed with Escape | [home-light-menu](screenshots/home-light-menu.png) |
| Chat sidebar, expanded | /chat/ | the rail's own Expand sidebar button | [chat-light-sidebar](screenshots/chat-light-sidebar.png), [chat-sidebar-open](#chat-sidebar-expanded) |
| Filled composer | /chat/ | sample text typed into the textarea and deleted again; Send never pressed | [chat-light-filled](screenshots/chat-light-filled.png), [chat-textarea](#chat-textarea) |
| Sign-in dialog | the ?modal=signin URL | the public modal URL alone; nothing inside it was pressed | [chat-signin-light-signin](screenshots/chat-signin-light-signin.png), [signin-dialog](#sign-in-dialog) |
| Blog search | /blog/ | sample text typed into the search field; search never submitted | [blog-light-search](screenshots/blog-light-search.png) |
| Cookie/consent and reCAPTCHA chrome | every page | hidden, never answered — the reCAPTCHA badge is Google's chrome, not the product's | hidden before every shot and reading |
| Everything behind Log in / Sign up | the chat product, health record, prescriptions, appointments | behind sign-in; the sign-in card was measured, never used | boundary; see Gaps |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 27 components were given a real keyboard focus. 21 draw an outline ring: `signup-button` (2px solid #3c83f6 `color.blue.500`, offset 0px), `login-button` (2px solid #3c83f6 `color.blue.500`, offset 0px), `menu-item` (2px solid #1d4fd7 `color.blue.700`, offset 2px), `nav-link` (2px solid #3c83f6 `color.blue.500`, offset 2px), `signup-free` (2px solid #3c83f6 `color.blue.500`, offset 0px), `sidebar-login` (2px solid #3c83f6 `color.blue.500`, offset 0px), `support-link` (1px auto #2463eb `color.blue.600`, offset 1px), `starter` (2px solid #1b1b18 `color.neutral.900`, offset 2px), `oauth-button` (2px solid #3c83f6 `color.blue.500`, offset 0px), `create-account-link` (1px auto #005fcc, offset 1px), `check-button` (1px auto #005fcc, offset 0px), `mkt-nav-pill` (1px auto #005fcc, offset 1px), `try-button` (1px auto #005fcc, offset 1px), `mkt-footer-link` (1px auto #005fcc, offset 1px), `article-card` (on a child: 1px auto rgb(0, 95, 204) offset 1px), `telehealth-cta` (1px auto #005fcc, offset 1px), `d-signup-button` (2px solid #61a6fa `color.blue.400`, offset 0px), `pause-control` (2px solid #3c83f6 `color.blue.500`, offset 2px), `category-chip` (1px auto #005fcc, offset 1px), `footer-social-icon` (1px auto #005fcc, offset 1px), `footer-legal-link` (1px auto #005fcc, offset 1px). 6 draw a focus ring as a shadow instead: `menu-button`, `start-chat-button`, `sidebar-toggle`, `send-button`, `email-login-button`, `dialog-close`. Focus could not be captured on 2 more (keyboard focus never landed on them, so their readings are left out): `testimonial-arrow`, `condensed-button`.

**Pressed.** Forced with DevTools (`CSS.forcePseudoState` :active:hover). Nothing a real press would submit was ever pressed.

**Motion.** Transitions measured on the components, by duration.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.15s | `cubic-bezier(0.4, 0, 0.2, 1)` | --tw-gradient-from, --tw-gradient-to, --tw-gradient-via, background-color, border-color, color, fill, opacity, outline-color, stroke, text-decoration-color | category-chip, check-button, mkt-footer-link, mkt-nav-pill, telehealth-cta, try-button |
| 0.15s | `ease` | background-color, color | footer-legal-link, footer-social-icon, pause-control |
| 0.15s | `ease-in` | background-color | m-starter, starter |
| 0.2s | `ease-in-out` | color | support-link |
| 0.2s | `ease-out` | border-radius | condensed-form |
| 0.25s | `ease` | transform | d-header, header, m-header |
| 0.3s | `ease` | background-color | mkt-header |

**Card shapes.** Default-state values; the entries hold the states.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Chat input card](#chat-input-card) | 652 x 148 | - | - | transparent | none | 0 |
| [Hero chat field](#hero-chat-field) | 548 x 147.38 | 1px solid rgba(27, 27, 24, 0.08) | 16px | #ffffff `color.white` | rgba(0, 0, 0, 0.06) 0px 2px 24px 0px | 16px |
| [Feature card](#feature-card) | 1233 x 274 | 1px solid rgba(27, 27, 24, 0.08) | 32px | transparent | none | 24px 48px |
| [Pricing card](#pricing-card) | 640 x 384.34 | - | - | transparent | none | 0 |
| [Sign-in dialog](#sign-in-dialog) | 393 x 583.45 | - | - | transparent | none | 0 |
| [Article card](#article-card) | 370.66 x 480.28 | 1px solid #e5e7eb | 14px | #ffffff `color.white` | none | 0 |
| [Author card](#author-card) | 380 x 280.5 | T: 1px solid #e7e4de | - | transparent | none | 0 |

## Components

### Shell and navigation

The 72px marketing top bar over the home page: the wordmark, Log in, the solid Sign up pill and the button that opens the site-menu drawer, plus the drawer itself. (The content pages carry a different, shorter sage bar with pill links and the dark Try Doctronic For Free CTA — see the Marketing and content pages group.)

#### Marketing top bar
The bar over the home page: wordmark, Log in, Sign up and the menu button that opens the site-menu drawer. Read as `header` on the home page.

**Values (default).** size 1440 x 72; background transparent; text geist 12/16.8 600, #1b1b18 `color.neutral.900`; transition transform 0.25s ease; icon 115.89 x 22, #1b1b18 `color.neutral.900`; layers div.content.contentShrink 1440.0x72.0 rgb(253, 253, 247); span.content 59.1x34.8 T:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / R:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / B:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / L:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) 32px; span.shimmer 57.1x32.8 32px; span.content 65.6x32.8 rgb(11, 11, 10) 32px; s.

Child layers that carry the look: div 1440x72 background #fdfdf7 `color.neutral.50`; span 59.1x34.8 border 1px solid rgba(27, 27, 24, 0.2) radius 32px; span 57.1x32.8 image linear-gradient(105deg, transparent 20%, rgba(253, 253, 247, 0.18) 50%, transparent 80%) radius 32px.

![Marketing top bar default](components/crops/header-default.png)

#### Sign up button
The dark pill at the right of the top bar. Measured, never pressed. Read as `signup-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 65.64 x 34.8; radius 32px; background transparent; text geist 12/16.8 600, #fdfdf7 `color.neutral.50`; layers ::before rgba(0, 0, 0, 0) 0px none 1; span.content 65.6x32.8 rgb(11, 11, 10) 32px; span.shimmer 65.6x32.8 32px |
| hover | layers ::before rgba(0, 0, 0, 0) 0px none 1; span.content 65.6x32.8 rgb(39, 39, 37) 32px; span.shimmer 65.6x32.8 32px |
| focus-visible | outline 2px solid #3c83f6 `color.blue.500`, offset 0px; layers ::before rgba(0, 0, 0, 0) 0px none 1; button.button.primary 65.6x34.8 2px solid rgb(60, 131, 246) offset 0px 32px; span.content 65.6x32.8 rgb(11, 11, 10) 32px; span.shimmer 65.6x32.8 32px |
| pressed | layers ::before rgba(0, 0, 0, 0) 0px none 1; span.content 64.3x32.1 rgb(27, 27, 24) 32px; span.shimmer 64.3x32.1 32px |

Child layers that carry the look: span 65.6x32.8 background #0b0b0a `color.neutral.950` radius 32px; span 65.6x32.8 image linear-gradient(105deg, transparent 20%, rgba(253, 253, 247, 0.18) 50%, transparent 80%) radius 32px.

![Sign up button default](components/crops/signup-button-default.png) ![Sign up button hover](components/crops/signup-button-hover.png) ![Sign up button focus-visible](components/crops/signup-button-focus-visible.png) ![Sign up button pressed](components/crops/signup-button-pressed.png)

#### Log in button
The quiet secondary button beside Sign up. Measured, never pressed. Read as `login-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 59.11 x 34.8; radius 32px; background transparent; text geist 12/16.8 600, #1b1b18 `color.neutral.900`; layers ::before rgba(0, 0, 0, 0) 0px none 1; span.content 59.1x34.8 T:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / R:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / B:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / L:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) 32px; span.shimmer 57.1x32.8 32px |
| hover | text geist 12/16.8 600, #fdfdf7 `color.neutral.50`; layers ::before rgba(0, 0, 0, 0) 0px none 1; span.content 59.1x34.8 rgb(11, 11, 10) T:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / R:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / B:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / L:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) 32px; span.shimmer 57.1x32.8 32px |
| focus-visible | outline 2px solid #3c83f6 `color.blue.500`, offset 0px; layers ::before rgba(0, 0, 0, 0) 0px none 1; button.button.secondary 59.1x34.8 2px solid rgb(60, 131, 246) offset 0px 32px; span.content 59.1x34.8 T:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / R:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / B:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / L:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) 32px; span.shimmer 57. |
| pressed | text geist 12/16.8 600, #fdfdf7 `color.neutral.50`; layers ::before rgba(0, 0, 0, 0) 0px none 1; span.content 57.9x34.1 rgb(27, 27, 24) T:1px solid rgb(27, 27, 24) / R:1px solid rgb(27, 27, 24) / B:1px solid rgb(27, 27, 24) / L:1px solid rgb(27, 27, 24) 32px; span.shimmer 56.0x32.1 32px |

Child layers that carry the look: span 59.1x34.8 border 1px solid rgba(27, 27, 24, 0.2) radius 32px; span 57.1x32.8 image linear-gradient(105deg, transparent 20%, rgba(253, 253, 247, 0.18) 50%, transparent 80%) radius 32px.

![Log in button default](components/crops/login-button-default.png) ![Log in button hover](components/crops/login-button-hover.png) ![Log in button focus-visible](components/crops/login-button-focus-visible.png) ![Log in button pressed](components/crops/login-button-pressed.png)

#### Site-menu button
aria-label "open sidebar": opens the site-menu drawer. The drawer was opened and measured below, then dismissed with Escape. Read as `menu-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 40 x 40; radius 100px; background transparent; text -apple-system 16/normal 400, #1b1b18 `color.neutral.900`; icon 24 x 24, #1b1b18 `color.neutral.900`; layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | layers ::after rgba(0, 0, 0, 0) 0px none 1; span.surface 40.0x40.0 rgb(245, 245, 240) 100px |
| focus-visible | shadow #2463eb 0px 0px 0px 2px; layers ::after rgba(0, 0, 0, 0) 0px none 1; button.buttonBase.expandHitArea 40.0x40.0 rgb(36, 99, 235) 0px 0px 0px 2px 100px |

![Site-menu button default](components/crops/menu-button-default.png) ![Site-menu button hover](components/crops/menu-button-hover.png) ![Site-menu button focus-visible](components/crops/menu-button-focus-visible.png) ![Site-menu button pressed](components/crops/menu-button-pressed.png)

#### Wordmark
Read as `logo` on the home page.

**Known wrong; recapture needed.** The reading is the 620 x 25 logo wrapper `div`, not the wordmark link.

**Values (default).** size 620 x 25; background transparent; text -apple-system 16/normal 400, #1b1b18 `color.neutral.900`; icon 115.89 x 22, #1b1b18 `color.neutral.900`.

![Wordmark default](components/crops/logo-default.png)

#### Site-menu drawer
The left drawer the menu button opens: Dashboard links (New chat, Explore, Health record, Health information), then a Company group (About us, Careers, Partnerships, …). Read as `menu-drawer` on the home page.

**Values (default).** size 320 x 852; background transparent; text geist 12/16.8 500, rgba(27, 27, 24, 0.6); icon 115.89 x 22, #1b1b18 `color.neutral.900`; layers div.divider 320.0x1.0 B:1px dashed color(srgb 0.105882 0.105882 0.0941176 / 0.08); div.container 320.0x51.8 T:1px dashed color(srgb 0.105882 0.105882 0.0941176 / 0.08); span.content 154.0x32.8 rgb(11, 11, 10) 32px; span.shimmer 154.0x32.8 32px; span.content 154.0x34.8 T:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / R:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / B:1px solid.

Child layers that carry the look: div 320x1 border 1px dashed rgba(27, 27, 24, 0.08); div 320x51.8 border 1px dashed rgba(27, 27, 24, 0.08); span 154x32.8 background #0b0b0a `color.neutral.950` radius 32px.

![Site-menu drawer default](components/crops/menu-drawer-default.png)

#### Menu drawer item
A row in the site-menu drawer. Measured while the drawer was open; links were never followed. Read as `menu-item` on the home page.

**Known wrong; recapture needed.** The reading is the "About Chat" expandable row, the same node as `menu-item-expand`, not a link row.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 320 x 38.39; padding 8px; radius 8px; background transparent; text geist 16/22.4 500, #1b1b18 `color.neutral.900`; icon 16 x 16, #1b1b18 `color.neutral.900` |
| hover | background #f5f5f0 `color.neutral.100` |
| focus-visible | radius 4px; outline 2px solid #1d4fd7 `color.blue.700`, offset 2px; layers button.menuItem.menuItemButton 320.0x38.4 2px solid rgb(29, 79, 215) offset 2px 4px |
| pressed | radius 4px; background #f5f5f0 `color.neutral.100`; outline 2px solid #1d4fd7 `color.blue.700`, offset 2px |

![Menu drawer item default](components/crops/menu-item-default.png) ![Menu drawer item hover](components/crops/menu-item-hover.png) ![Menu drawer item focus-visible](components/crops/menu-item-focus-visible.png) ![Menu drawer item pressed](components/crops/menu-item-pressed.png)

#### Menu drawer expandable
A submenu row (About Chat / Health information) with a chevron. Measured, never expanded. Read as `menu-item-expand` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 320 x 38.39; padding 8px; radius 4px; background transparent; outline 2px solid #1d4fd7 `color.blue.700`, offset 2px; text geist 16/22.4 500, #1b1b18 `color.neutral.900`; icon 16 x 16, #1b1b18 `color.neutral.900`; layers button.menuItem.menuItemButton 320.0x38.4 2px solid rgb(29, 79, 215) offset 2px 4px |
| hover | background #f5f5f0 `color.neutral.100`; layers none |

Child layers that carry the look: button 320x38.4 radius 4px.

![Menu drawer expandable default](components/crops/menu-item-expand-default.png) ![Menu drawer expandable hover](components/crops/menu-item-expand-hover.png)

### Home: hero and marketing

The home hero with the Fraunces display greeting, the raised chat input card with its animated accent border and the accent Start chat button, the suggestion chips, then the marketing sections — feature cards, pricing, testimonials, the Hippocratic oath band and the footer.

#### Home hero
The first band: the Fraunces display headline, the "What brings you in?" prompt and the chat input card. Read as `hero` on the home page.

**Values (default).** size 548 x 421.5; background transparent; text fraunces 48/56.16 400, #1b1b18 `color.neutral.900`; icon 20 x 20, #000000; layers div.content 150.5x36.6 color(srgb 0.85098 1 0.501961 / 0.5) 16px 18px 18px 2px; div::before.material 148.453pxx34.5938px 16px 18px 18px 2px; div::after.material 150.453pxx36.5938px rgba(128, 128, 128, 0) 16px 18px 18px 2px; div.edgeReflection 186.5x72.6 T:18px solid rgba(0, 0, 0, 0) / R:18px solid rgba(0, 0, 0, 0) / B:18px solid rgba(0, 0, 0, 0) / L:18px solid rgba(0, 0, 0, 0) 34px 36px 36px 20px;.

Child layers that carry the look: div 150.5x36.6 background rgba(217, 255, 128, 0.5) radius 16px 18px 18px 2px; div::before 148.453pxx34.5938px image linear-gradient(155deg, rgba(255, 255, 255, 0.06) 0%, rgba(0, 0, 0, 0.06) 50%, rgba(255, 2 radius 16px 18px 18px 2px; div::after 150.453pxx36.5938px background rgba(128, 128, 128, 0) radius 16px 18px 18px 2px.

![Home hero default](components/crops/hero-default.png)

#### Hero headline
"Hi, I'm Doctronic" in the Fraunces display face with the dashed underline. Read as `hero-title` on the home page.

**Values (default).** size 378.56 x 56.16; background transparent; text fraunces 48/56.16 400, #1b1b18 `color.neutral.900`.

![Hero headline default](components/crops/hero-title-default.png)

#### Anonymous label
The "Anonymous" session badge inside the chat field. Read as `anon-label` on the home page.

**Values (default).** size 105.56 x 32; padding 3px 8px; border 1px dashed rgba(27, 27, 24, 0.08); radius 34px; background transparent; text geist 12/16.8 500, #2463eb `color.blue.600`; icon 20 x 20, #000000.

![Anonymous label default](components/crops/anon-label-default.png)

#### Hero chat field
The input card the page is built around: raised white surface, soft border, the textarea and the Start chat button. Measured, never submitted. Read as `hero-input-card` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 548 x 147.38; padding 16px; border 1px solid rgba(27, 27, 24, 0.08); radius 16px; background #ffffff `color.white`; shadow rgba(0, 0, 0, 0.06) 0px 2px 24px 0px; text geist 12/16.8 500, #2463eb `color.blue.600`; icon 20 x 20, #000000 |

![Hero chat field default](components/crops/hero-input-card-default.png) ![Hero chat field hover](components/crops/hero-input-card-hover.png)

#### Hero textarea
"Describe symptom or ask any health questions…" — text was typed and deleted; nothing was sent. Read as `hero-textarea` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 514 x 58.78; background transparent; text geist 14/19.6 400, #1b1b18 `color.neutral.900`; placeholder rgba(27, 27, 24, 0.73) |

![Hero textarea default](components/crops/hero-textarea-default.png) ![Hero textarea focused](components/crops/hero-textarea-focused.png) ![Hero textarea filled](components/crops/hero-textarea-filled.png)

#### Start chat button
The accent-blue submit control. Measured, never pressed — pressing would start a chat. Read as `start-chat-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 136.36 x 43.59; radius 52px; background transparent; text geist 14/19.6 600, #ffffff `color.white`; icon 16 x 16, #ffffff `color.white`; layers ::before rgba(0, 0, 0, 0) 0px none 1; span.content.submitButtonContent 136.4x43.6 rgb(36, 99, 235) color(srgb 0.141176 0.388235 0.921569 / 0.39) 0px 4px 7px 0px 52px; span.shimmer 136.4x43.6 52px |
| hover | layers ::before rgba(0, 0, 0, 0) 0px none 1; span.content.submitButtonContent 136.4x43.6 rgb(29, 79, 215) color(srgb 0.141176 0.388235 0.921569 / 0.5) 0px 6px 10px 0px 52px; span.shimmer 136.4x43.6 52px |
| focus-visible | shadow rgba(36, 99, 235, 0.39) 0px 4px 7px 0px, #0b0b0a 0px 0px 0px 2px; layers ::before rgba(0, 0, 0, 0) 0px none 1; button.button.hero 136.4x43.6 color(srgb 0.141176 0.388235 0.921569 / 0.39) 0px 4px 7px 0px, rgb(11, 11, 10) 0px 0px 0px 2px 52px; span.content.submitButtonContent 136.4x43.6 rgb(36, 99, 235) 52px; span.shimmer 136.4x43.6 52px |
| pressed | icon 15.68 x 15.68, #ffffff `color.white`; layers ::before rgba(0, 0, 0, 0) 0px none 1; span.content.submitButtonContent 133.6x42.7 rgb(30, 63, 174) 52px; span.shimmer 133.6x42.7 52px |

Child layers that carry the look: span 136.4x43.6 background #2463eb `color.blue.600` radius 52px shadow rgba(36, 99, 235, 0.39) 0px 4px 7px 0px; span 136.4x43.6 image linear-gradient(105deg, transparent 20%, rgba(253, 253, 247, 0.18) 50%, transparent 80%) radius 52px.

![Start chat button default](components/crops/start-chat-button-default.png) ![Start chat button hover](components/crops/start-chat-button-hover.png) ![Start chat button focus-visible](components/crops/start-chat-button-focus-visible.png) ![Start chat button pressed](components/crops/start-chat-button-pressed.png)

#### "What brings you in?" pill
Read as `brings-pill` on the home page.

**Values (default).** size 126.45 x 18; background transparent; text geist 14/19.6 600, #1b1b18 `color.neutral.900`.

!["What brings you in?" pill default](components/crops/brings-pill-default.png)

#### HIPAA badge
Read as `hipaa-badge` on the home page.

**Values (default).** size 90.39 x 16; background transparent; text geist 10/14 500, rgba(27, 27, 24, 0.6); icon 16 x 16, rgba(27, 27, 24, 0.6).

![HIPAA badge default](components/crops/hipaa-badge-default.png)

#### Feature card
Read as `feature-card` on the home page.

**Known wrong; recapture needed.** The reading is the testimonial `article` (the same card as `quote-card`), not a feature card.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 1233 x 274; padding 24px 48px; border 1px solid rgba(27, 27, 24, 0.08); radius 32px; background transparent; text fraunces 24/28.08 400, #1b1b18 `color.neutral.900`; icon 24 x 24, #797972 `color.neutral.500` |

![Feature card default](components/crops/feature-card-default.png) ![Feature card hover](components/crops/feature-card-hover.png)

#### Pricing card
The plan card with the $ price and the highlighted callout. Read as `pricing-card` on the home page.

**Values (default).** size 640 x 384.34; background transparent; text geistMono 16/22.4 600, #3c3c39 `color.neutral.700`; icon 115.89 x 22, #1b1b18 `color.neutral.900`; layers div.root.card 640.0x384.3 rgb(253, 253, 247) rgba(0, 0, 0, 0.15) 0px 15px 30px -10px, rgba(255, 255, 255, 0.8) 0px 1px 1px 0px inset, rgba(0, 0, 0, 0.05) 0px -1px 1px 0px inset, rgba(255, 255, 255, 0.8) 1px 0px 1px 0px inset, rgba(0, 0, 0, 0.05) -1px 0px 1px 0px inset, rgba(255, 255, 255, 0.4) 0px 0px 20px 0px inset 24px; div::before.root.card 640pxx384.344px 24px; div.holoLayer 640.0x384.3 24px; .

Child layers that carry the look: div 640x384.3 background #fdfdf7 `color.neutral.50` radius 24px shadow rgba(0, 0, 0, 0.15) 0px 15px 30px -10px, rgba(255, 255, 255, 0.8) 0px 1px 1px 0px inset, rgba(0, 0, 0, 0.05) 0px -1px 1px 0px inset, rgba(255, 255, 255, 0.8) 1px 0px 1px 0px inset, rgba(0, 0, 0, 0.05) -1px 0px 1px 0px inset, rgba(255, 255, 255, 0.4) 0px 0px 20px 0px inset; div::before 640pxx384.344px image linear-gradient(115deg, rgba(255, 255, 255, 0) 0%, rgba(255, 255, 255, 0) 25%, rgba(255, 1 radius 24px; div 640x384.3 image linear-gradient(115deg, rgba(255, 255, 255, 0) 0%, rgba(255, 255, 255, 0) 25%, rgba(255, 1 radius 24px.

![Pricing card default](components/crops/pricing-card-default.png)

#### Price figure
Read as `price` on the home page.

**Values (default).** size 63.39 x 21; background transparent; text geist 16/22.4 400, #2463eb `color.blue.600`.

![Price figure default](components/crops/price-default.png)

#### Testimonial arrow
Read as `testimonial-arrow` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 32 x 32; radius 100px; background transparent; text -apple-system 16/normal 400, rgba(27, 27, 24, 0.3); icon 24 x 24, #797972 `color.neutral.500`; layers ::after rgba(0, 0, 0, 0) 0px none 1 |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

![Testimonial arrow default](components/crops/testimonial-arrow-default.png) ![Testimonial arrow hover](components/crops/testimonial-arrow-hover.png) ![Testimonial arrow pressed](components/crops/testimonial-arrow-pressed.png)

#### Watch testimonial button
Measured, never pressed. Read as `watch-button` on the home page.

Not on the page when it was captured.

#### Hippocratic oath band
Read as `oath-band` on the home page.

**Values (default).** size 1440 x 490.94; padding 0px 0px 32px 0px; background transparent; text geist 28/39.2 600, #1b1b18 `color.neutral.900`.

![Hippocratic oath band default](components/crops/oath-band-default.png)

#### Testimonial card
Read as `quote-card` on the home page.

**Values (default).** size 608 x 112.31; background transparent; text fraunces 24/28.08 400, #1b1b18 `color.neutral.900`.

![Testimonial card default](components/crops/quote-card-default.png)

#### Trustpilot rating block
Read as `rating-group` on the home page.

**Values (default).** size 153.19 x 14; background transparent; text geist 10/14 500, rgba(27, 27, 24, 0.6).

![Trustpilot rating block default](components/crops/rating-group-default.png)

#### Condensed chat form
The slim repeat of the chat field near the footer: one textarea and a Get started button. Read as `condensed-form` on the home page.

**Values (default).** size 480 x 72; padding 12px 12px 12px 24px; radius 48px; background #fdfdf7 `color.neutral.50`; shadow rgba(0, 0, 0, 0.1) 0px 5px 32px 0px; text -apple-system 16/normal 400, #1b1b18 `color.neutral.900`; transition border-radius 0.2s ease-out; icon 24 x 24, #ffffff `color.white`.

![Condensed chat form default](components/crops/condensed-form-default.png)

#### Get started button
Measured, never pressed. Read as `condensed-button` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 48 x 48; radius 52px; background transparent; text -apple-system 16/normal 400, #1b1b18 `color.neutral.900`; icon 24 x 24, #ffffff `color.white`; layers ::before rgba(0, 0, 0, 0) 0px none 1; span.content 48.0x48.0 rgb(36, 99, 235) color(srgb 0.141176 0.388235 0.921569 / 0.39) 0px 4px 7px 0px 52px; span.shimmer 48.0x48.0 52px |
| pressed | icon 22.8 x 22.8, #ffffff `color.white`; layers ::before rgba(0, 0, 0, 0) 0px none 1; span.content 45.6x45.6 rgb(30, 63, 174) 52px; span.shimmer 45.6x45.6 52px |

**Focus not capturable.** A real keyboard focus could not be held on this element (`focus-visible` recorded `via: focus failed`), so its focus look is uncaptured — not measured as absent.

Child layers that carry the look: span 48x48 background #2463eb `color.blue.600` radius 52px shadow rgba(36, 99, 235, 0.39) 0px 4px 7px 0px; span 48x48 image linear-gradient(105deg, transparent 20%, rgba(253, 253, 247, 0.18) 50%, transparent 80%) radius 52px.

![Get started button default](components/crops/condensed-button-default.png) ![Get started button pressed](components/crops/condensed-button-pressed.png)

#### Footer
The deep page footer: link columns, legal row and the "Made in" note. Read as `footer` on the home page.

**Values (default).** size 1440 x 1414.5; background transparent; text geist 18/25.2 600, #1b1b18 `color.neutral.900`; layers div.gradient 1440.0x1414.5; span.content 59.1x34.8 T:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / R:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / B:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / L:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) 32px; span.shimmer 57.1x32.8 32px; span.content 65.6x32.8 rgb(11, 11, 10) 32px; span.shimmer 65.6x32.8 32px; di.

Child layers that carry the look: div 1440x1414.5 image linear-gradient(#fdfdf7 `color.neutral.50` 0%, #e1efe3 `color.sage.100` 100%); span 59.1x34.8 border 1px solid rgba(27, 27, 24, 0.2) radius 32px; span 57.1x32.8 image linear-gradient(105deg, transparent 20%, rgba(253, 253, 247, 0.18) 50%, transparent 80%) radius 32px.

![Footer default](components/crops/footer-default.png)

#### Legal line
Read as `footer-legal` on the home page.

**Values (default).** size 296.28 x 33.59; background transparent; text geist 12/16.8 400, #a7a7a0 `color.neutral.400`.

![Legal line default](components/crops/footer-legal-default.png)

#### Animation pause control
The round control pinned bottom-right that pauses the page's motion. Measured, never pressed. Read as `pause-control` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 40 x 40; padding 8px 32px 8px 8px; radius 32px; background #f5f5f0 `color.neutral.100`; text -apple-system 16/normal 400, #797972 `color.neutral.500`; transition background-color 0.15s ease, color 0.15s ease; icon 24 x 24, #797972 `color.neutral.500` |
| hover | size 159 x 40; text geist 14/19.6 500, #1b1b18 `color.neutral.900`; icon 24 x 24, #1b1b18 `color.neutral.900` |
| focus-visible | outline 2px solid #3c83f6 `color.blue.500`, offset 2px; text -apple-system 16/normal 400, #1b1b18 `color.neutral.900`; icon 24 x 24, #1b1b18 `color.neutral.900` |
| pressed | size 159 x 40; text geist 14/19.6 500, #1b1b18 `color.neutral.900`; icon 24 x 24, #1b1b18 `color.neutral.900` |

![Animation pause control default](components/crops/pause-control-default.png) ![Animation pause control hover](components/crops/pause-control-hover.png) ![Animation pause control focus-visible](components/crops/pause-control-focus-visible.png) ![Animation pause control pressed](components/crops/pause-control-pressed.png)

#### Footer social icon link
An aria-labelled icon link in the footer's social row (e.g. "Doctronic on Instagram"). Measured, never followed. Read as `footer-social-icon` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 16 x 16; background transparent; text -apple-system 16/normal 400, #1b1b18 `color.neutral.900`; transition color 0.15s ease; icon 16 x 16, #1b1b18 `color.neutral.900`; layers ::before rgba(0, 0, 0, 0) 0px none 1 |
| hover | text -apple-system 16/normal 400, #2463eb `color.blue.600`; icon 16 x 16, #2463eb `color.blue.600` |
| focus-visible | outline 1px auto #005fcc, offset 1px; text -apple-system 16/normal 400, #2463eb `color.blue.600`; icon 16 x 16, #2463eb `color.blue.600`; layers ::before rgba(0, 0, 0, 0) 0px none 1; a.link 16.0x16.0 1px auto rgb(0, 95, 204) offset 1px |
| pressed | text -apple-system 16/normal 400, #2463eb `color.blue.600`; icon 16 x 16, #2463eb `color.blue.600` |

![Footer social icon link default](components/crops/footer-social-icon-default.png) ![Footer social icon link hover](components/crops/footer-social-icon-hover.png) ![Footer social icon link focus-visible](components/crops/footer-social-icon-focus-visible.png) ![Footer social icon link pressed](components/crops/footer-social-icon-pressed.png)

#### Footer legal link
Privacy Policy / Terms of Service in the legal row. Measured, never followed. Read as `footer-legal-link` on the home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 72.63 x 24; background transparent; text geist 12/16.8 400, #1b1b18 `color.neutral.900`; transition color 0.15s ease |
| hover | text geist 12/16.8 400, #2463eb `color.blue.600` |
| focus-visible | outline 1px auto #005fcc, offset 1px; text geist 12/16.8 400, #2463eb `color.blue.600`; layers a.link 72.6x24.0 1px auto rgb(0, 95, 204) offset 1px |
| pressed | text geist 12/16.8 400, #2463eb `color.blue.600` |

![Footer legal link default](components/crops/footer-legal-link-default.png) ![Footer legal link hover](components/crops/footer-legal-link-hover.png) ![Footer legal link focus-visible](components/crops/footer-legal-link-focus-visible.png) ![Footer legal link pressed](components/crops/footer-legal-link-pressed.png)

### Chat surface

The signed-out /chat/ surface: the collapsible left rail (New chat highlighted, Sign up for free and Log in pinned at the bottom), the centered empty-state greeting, the large input card with the Send control and the starter chips. Nothing was sent.

#### Chat sidebar (collapsed)
The left rail as a signed-out visitor first sees it: collapsed to the logo and toggle. Read as `chat-sidebar` on the /chat/ page.

**Values (default).** size 74 x 900; background transparent; text geist 12/16.8 600, #fdfdf7 `color.neutral.50`; icon 115.89 x 22, #1b1b18 `color.neutral.900`; layers aside.sidebar.collapsed 74.0x900.0 rgb(253, 253, 247) color(srgb 0.105882 0.105882 0.0941176 / 0.08) -1px 0px 0px 0px inset; a.wrapper.collapsed 40.0x40.0 rgb(240, 246, 255) 50%; span.content 58.0x32.8 rgb(11, 11, 10) 32px; span.shimmer 58.0x32.8 32px; span.content 58.0x34.8 T:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / R:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / B:1p.

Child layers that carry the look: aside 74x900 background #fdfdf7 `color.neutral.50` shadow rgba(27, 27, 24, 0.08) -1px 0px 0px 0px inset; a 40x40 background #f0f6ff `color.blue.50` radius 50%; span 58x32.8 background #0b0b0a `color.neutral.950` radius 32px.

![Chat sidebar (collapsed) default](components/crops/chat-sidebar-default.png)

#### Sidebar expand button
Read as `sidebar-toggle` on the /chat/ page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 36 x 36; radius 100px; background transparent; text -apple-system 16/normal 400, rgba(27, 27, 24, 0.2); icon 20 x 20, rgba(27, 27, 24, 0.2); layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | layers ::after rgba(0, 0, 0, 0) 0px none 1; span.surface 36.0x36.0 rgb(245, 245, 240) 100px |
| focus-visible | shadow #2463eb 0px 0px 0px 2px; layers ::after rgba(0, 0, 0, 0) 0px none 1; button.buttonBase.expandHitArea 36.0x36.0 rgb(36, 99, 235) 0px 0px 0px 2px 100px |

![Sidebar expand button default](components/crops/sidebar-toggle-default.png) ![Sidebar expand button hover](components/crops/sidebar-toggle-hover.png) ![Sidebar expand button focus-visible](components/crops/sidebar-toggle-focus-visible.png) ![Sidebar expand button pressed](components/crops/sidebar-toggle-pressed.png)

#### Chat sidebar (expanded)
Opened with the sidebar's own Expand button: New chat highlighted at the top, Health record / Appointments / Prescriptions below, then Sign up and Log in pinned at the bottom. Read as `chat-sidebar-open` on the /chat/ page.

**Values (default).** size 256 x 900; background transparent; text geist 14/19.6 500, #2463eb `color.blue.600`; icon 115.89 x 22, #1b1b18 `color.neutral.900`; layers aside.sidebar 256.0x900.0 rgb(253, 253, 247) color(srgb 0.105882 0.105882 0.0941176 / 0.08) -1px 0px 0px 0px inset; a.wrapper.highlighted 224.0x36.0 rgb(240, 246, 255) 8px; span.content 224.0x32.8 rgb(11, 11, 10) 32px; span.shimmer 224.0x32.8 32px; span.content 224.0x34.8 T:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / R:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / B:1px s.

Child layers that carry the look: aside 256x900 background #fdfdf7 `color.neutral.50` shadow rgba(27, 27, 24, 0.08) -1px 0px 0px 0px inset; a 224x36 background #f0f6ff `color.blue.50` radius 8px; span 224x32.8 background #0b0b0a `color.neutral.950` radius 32px.

![Chat sidebar (expanded) default](components/crops/chat-sidebar-open-default.png)

#### Sidebar link, current
New chat: the highlighted row in the expanded rail. Read as `nav-link-current` on the /chat/ page.

**Values (default).** size 224 x 36; padding 8px; radius 8px; background #f0f6ff `color.blue.50`; text geist 14/19.6 500, #2463eb `color.blue.600`; icon 20 x 20, #2463eb `color.blue.600`.

![Sidebar link, current default](components/crops/nav-link-current-default.png)

#### Sidebar link
Read as `nav-link` on the /chat/ page.

**Known wrong; recapture needed.** The reading is the highlighted "New chat" row, the same node as `nav-link-current`, not a resting sidebar link.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, pressed) | size 224 x 36; padding 8px; radius 8px; background #f0f6ff `color.blue.50`; text geist 14/19.6 500, #2463eb `color.blue.600`; icon 20 x 20, #2463eb `color.blue.600` |
| focus-visible | outline 2px solid #3c83f6 `color.blue.500`, offset 2px |

![Sidebar link default](components/crops/nav-link-default.png) ![Sidebar link hover](components/crops/nav-link-hover.png) ![Sidebar link focus-visible](components/crops/nav-link-focus-visible.png) ![Sidebar link pressed](components/crops/nav-link-pressed.png)

#### Sign up for free button
The blue primary button pinned at the bottom of the expanded rail. Measured, never pressed. Read as `signup-free` on the /chat/ page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 224 x 32.8; radius 32px; background transparent; text geist 12/16.8 600, #fdfdf7 `color.neutral.50`; layers ::before rgba(0, 0, 0, 0) 0px none 1; span.content 224.0x32.8 rgb(11, 11, 10) 32px; span.shimmer 224.0x32.8 32px |
| hover | layers ::before rgba(0, 0, 0, 0) 0px none 1; span.content 224.0x32.8 rgb(39, 39, 37) 32px; span.shimmer 224.0x32.8 32px |
| focus-visible | outline 2px solid #3c83f6 `color.blue.500`, offset 0px; layers ::before rgba(0, 0, 0, 0) 0px none 1; button.button.primary 224.0x32.8 2px solid rgb(60, 131, 246) offset 0px 32px; span.content 224.0x32.8 rgb(11, 11, 10) 32px; span.shimmer 224.0x32.8 32px |
| pressed | layers ::before rgba(0, 0, 0, 0) 0px none 1; span.content 219.5x32.1 rgb(27, 27, 24) 32px; span.shimmer 219.5x32.1 32px |

Child layers that carry the look: span 224x32.8 background #0b0b0a `color.neutral.950` radius 32px; span 224x32.8 image linear-gradient(105deg, transparent 20%, rgba(253, 253, 247, 0.18) 50%, transparent 80%) radius 32px.

![Sign up for free button default](components/crops/signup-free-default.png) ![Sign up for free button hover](components/crops/signup-free-hover.png) ![Sign up for free button focus-visible](components/crops/signup-free-focus-visible.png) ![Sign up for free button pressed](components/crops/signup-free-pressed.png)

#### Sidebar log in button
The secondary button beside Sign up for free. Measured, never pressed. Read as `sidebar-login` on the /chat/ page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 224 x 34.8; radius 32px; background transparent; text geist 12/16.8 600, #1b1b18 `color.neutral.900`; layers ::before rgba(0, 0, 0, 0) 0px none 1; span.content 224.0x34.8 T:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / R:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / B:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / L:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) 32px; span.shimmer 222.0x32.8 32px |
| hover | text geist 12/16.8 600, #fdfdf7 `color.neutral.50`; layers ::before rgba(0, 0, 0, 0) 0px none 1; span.content 224.0x34.8 rgb(11, 11, 10) T:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / R:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / B:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / L:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) 32px; span.shimmer 222.0x32.8 32px |
| focus-visible | outline 2px solid #3c83f6 `color.blue.500`, offset 0px; layers ::before rgba(0, 0, 0, 0) 0px none 1; button.button.secondary 224.0x34.8 2px solid rgb(60, 131, 246) offset 0px 32px; span.content 224.0x34.8 T:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / R:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / B:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / L:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) 32px; span.shimmer 2 |
| pressed | text geist 12/16.8 600, #fdfdf7 `color.neutral.50`; layers ::before rgba(0, 0, 0, 0) 0px none 1; span.content 219.5x34.1 rgb(27, 27, 24) T:1px solid rgb(27, 27, 24) / R:1px solid rgb(27, 27, 24) / B:1px solid rgb(27, 27, 24) / L:1px solid rgb(27, 27, 24) 32px; span.shimmer 217.6x32.1 32px |

Child layers that carry the look: span 224x34.8 border 1px solid rgba(27, 27, 24, 0.2) radius 32px; span 222x32.8 image linear-gradient(105deg, transparent 20%, rgba(253, 253, 247, 0.18) 50%, transparent 80%) radius 32px.

![Sidebar log in button default](components/crops/sidebar-login-default.png) ![Sidebar log in button hover](components/crops/sidebar-login-hover.png) ![Sidebar log in button focus-visible](components/crops/sidebar-login-focus-visible.png) ![Sidebar log in button pressed](components/crops/sidebar-login-pressed.png)

#### Anonymous badge
The "Anonymous" session chip. Pressing it is a sign-in path, so it was hovered and measured only. Read as `anon-badge` on the /chat/ page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 105.56 x 32; padding 3px 8px; border 1px dashed rgba(27, 27, 24, 0.08); radius 34px; background transparent; text geist 12/16.8 500, #2463eb `color.blue.600`; icon 20 x 20, #000000 |
| hover | background #f5f5f0 `color.neutral.100` |

![Anonymous badge default](components/crops/anon-badge-default.png) ![Anonymous badge hover](components/crops/anon-badge-hover.png)

#### Support mail link
Read as `support-link` on the /chat/ page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 93.52 x 13; background transparent; text geist 10/14 400, #2463eb `color.blue.600`; transition color 0.2s ease-in-out |
| hover | text geist 10/14 400, #1d4fd7 `color.blue.700` |
| focus-visible | outline 1px auto #2463eb `color.blue.600`, offset 1px; layers a.link 93.5x13.0 1px auto rgb(36, 99, 235) offset 1px |

![Support mail link default](components/crops/support-link-default.png) ![Support mail link hover](components/crops/support-link-hover.png) ![Support mail link focus-visible](components/crops/support-link-focus-visible.png)

#### Legal link
The Terms of Service / Privacy Policy link in the chat footer. The first-capture selector read the footer's first anchor — the support@doctronic.ai mailto, already measured as support-link — so those states were dropped and the fixed selector's re-measure is queued. Read as `legal-link` on the /chat/ page.

Not on the page when it was captured.

#### View recent chats
Link to the (signed-in) chat list; measured only. Read as `recent-chats` on the /chat/ page.

Not on the page when it was captured.

#### Chat hero
The centered empty-state: the Fraunces greeting and the large input card. Read as `chat-hero` on the /chat/ page.

**Known wrong; recapture needed.** The reading is the whole 1440 x 900 `main`, not the centred empty state.

**Values (default).** size 1440 x 900; background #fdfdf7 `color.neutral.50`; text geist 14/19.6 500, #2463eb `color.blue.600`; icon 115.89 x 22, #1b1b18 `color.neutral.900`.

![Chat hero default](components/crops/chat-hero-default.png)

#### Chat greeting
Read as `chat-greeting` on the /chat/ page.

**Values (default).** size 232 x 46.8; background transparent; text fraunces 40/46.8 400, #1b1b18 `color.neutral.900`.

![Chat greeting default](components/crops/chat-greeting-default.png)

#### Chat input card
The large raised card holding the textarea and the round Send button; expands when focused. Read as `input-card` on the /chat/ page.

**Known wrong; recapture needed.** The reading is the transparent 652 x 148 `.wrapper.chatInput`, not the painted `form` card.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 652 x 148; background transparent; text geist 12/16.8 500, #2463eb `color.blue.600`; icon 20 x 20, #000000; layers form.inputCard.inputCardExpanded 652.0x126.0 rgb(255, 255, 255) T:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.08) / R:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.08) / B:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.08) / L:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.08) rgba(0, 0, 0, 0.06) 0px 2px 24px 0px 16px; button.badgeButton 105.6x32.0 T:1px dashed color(sr |

Child layers that carry the look: form 652x126 background #ffffff `color.white` border 1px solid rgba(27, 27, 24, 0.08) radius 16px shadow rgba(0, 0, 0, 0.06) 0px 2px 24px 0px; button 105.6x32 border 1px dashed rgba(27, 27, 24, 0.08) radius 34px; span 32x32 background #2463eb `color.blue.600` radius 52px shadow rgba(36, 99, 235, 0.39) 0px 4px 7px 0px.

![Chat input card default](components/crops/input-card-default.png) ![Chat input card hover](components/crops/input-card-hover.png)

#### Chat textarea
"Ask a question about your health…" — text was typed and deleted, Enter never pressed. Read as `chat-textarea` on the /chat/ page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused, filled) | size 618 x 52; background transparent; text geist 16/22.4 400, #1b1b18 `color.neutral.900`; placeholder rgba(27, 27, 24, 0.6) |

![Chat textarea default](components/crops/chat-textarea-default.png) ![Chat textarea focused](components/crops/chat-textarea-focused.png) ![Chat textarea filled](components/crops/chat-textarea-filled.png)

#### Send message button
The condensed dark submit control inside the card. Measured, never pressed — pressing would send a message. Read as `send-button` on the /chat/ page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 32 x 32; radius 52px; background transparent; text -apple-system 16/normal 400, #1b1b18 `color.neutral.900`; icon 20 x 20, #ffffff `color.white`; layers ::before rgba(0, 0, 0, 0) 0px none 1; span.content 32.0x32.0 rgb(36, 99, 235) color(srgb 0.141176 0.388235 0.921569 / 0.39) 0px 4px 7px 0px 52px; span.shimmer 32.0x32.0 52px |
| hover | layers ::before rgba(0, 0, 0, 0) 0px none 1; span.content 32.0x32.0 rgb(29, 79, 215) color(srgb 0.141176 0.388235 0.921569 / 0.5) 0px 6px 10px 0px 52px; span.shimmer 32.0x32.0 52px |
| focus-visible | shadow rgba(36, 99, 235, 0.39) 0px 4px 7px 0px, #0b0b0a 0px 0px 0px 2px; layers ::before rgba(0, 0, 0, 0) 0px none 1; button.button.hero 32.0x32.0 color(srgb 0.141176 0.388235 0.921569 / 0.39) 0px 4px 7px 0px, rgb(11, 11, 10) 0px 0px 0px 2px 52px; span.content 32.0x32.0 rgb(36, 99, 235) 52px; span.shimmer 32.0x32.0 52px |
| pressed | icon 19 x 19, #ffffff `color.white`; layers ::before rgba(0, 0, 0, 0) 0px none 1; span.content 30.4x30.4 rgb(30, 63, 174) 52px; span.shimmer 30.4x30.4 52px |

Child layers that carry the look: span 32x32 background #2463eb `color.blue.600` radius 52px shadow rgba(36, 99, 235, 0.39) 0px 4px 7px 0px; span 32x32 image linear-gradient(105deg, transparent 20%, rgba(253, 253, 247, 0.18) 50%, transparent 80%) radius 52px.

![Send message button default](components/crops/send-button-default.png) ![Send message button hover](components/crops/send-button-hover.png) ![Send message button focus-visible](components/crops/send-button-focus-visible.png) ![Send message button pressed](components/crops/send-button-pressed.png)

#### Starter chip
"Check my symptoms" — a conversation starter under the card. Measured, never pressed. Read as `starter` on the /chat/ page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 164.11 x 36.59; padding 8px 16px; radius 8px; background #f5f5f0 `color.neutral.100`; text geist 14/19.6 500, #1b1b18 `color.neutral.900`; transition background-color 0.15s ease-in |
| hover | background #e4e4dc `color.neutral.200` |
| focus-visible | outline 2px solid #1b1b18 `color.neutral.900`, offset 2px |
| pressed | background #e4e4dc `color.neutral.200` |

![Starter chip default](components/crops/starter-default.png) ![Starter chip hover](components/crops/starter-hover.png) ![Starter chip focus-visible](components/crops/starter-focus-visible.png) ![Starter chip pressed](components/crops/starter-pressed.png)

#### Medical disclaimer
Read as `disclaimer` on the /chat/ page.

**Values (default).** size 652 x 14; background transparent; text geist 10/14 400, rgba(27, 27, 24, 0.6).

![Medical disclaimer default](components/crops/disclaimer-default.png)

### Symptom checker

The /symptom-checker/ entry point: the Fraunces headline, the symptoms textarea card and the Check My Symptoms action. Measured, never submitted.

#### Symptom-checker headline
"…your private and personal AI symptom checker" in the Fraunces display face. Read as `symptom-title` on the symptom checker page.

**Values (default).** size 640 x 211.17; background transparent; text Fraunces 64/70.4 400, #000000.

![Symptom-checker headline default](components/crops/symptom-title-default.png)

#### Symptom input card
The raised card holding the symptoms textarea and the Check button. Read as `symptom-input-card` on the symptom checker page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 638 x 171; padding 16px; border 1px solid #e3e1d6; radius 24px; background #ffffff `color.white`; shadow rgba(27, 27, 24, 0.06) 0px 10px 30px 0px; text Geist 15/22.5 600, #1b1b18 `color.neutral.900`; icon 16 x 16, #fdfdf8 |

![Symptom input card default](components/crops/symptom-input-card-default.png) ![Symptom input card hover](components/crops/symptom-input-card-hover.png)

#### Symptoms textarea
"Describe your symptoms…" — text was typed and deleted, never submitted. Read as `symptom-textarea` on the symptom checker page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 604 x 80; padding 4px; background transparent; text Geist 16/24 400, #1a1a18; placeholder rgba(26, 26, 24, 0.6) |
| focused, filled | shadow #1a1a18 0px 0px 0px 0px; layers textarea.order-1.w-full 604.0x80.0 rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgb(26, 26, 24) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px |

![Symptoms textarea default](components/crops/symptom-textarea-default.png) ![Symptoms textarea focused](components/crops/symptom-textarea-focused.png) ![Symptoms textarea filled](components/crops/symptom-textarea-filled.png)

#### Check My Symptoms button
Measured, never pressed — pressing would submit symptoms. Read as `check-button` on the symptom checker page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 208.95 x 45; padding 12px 24px; radius 52px; background #2563eb; shadow rgba(9, 97, 228, 0.39) 0px 4px 7px 0px; text Geist 14/21 600, #fdfdf8; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 16 x 16, #fdfdf8 |
| hover | background oklch(0.488 0.243 264.376) |
| focus-visible | outline 1px auto #005fcc, offset 0px |
| pressed | background oklch(0.488 0.243 264.376) |

![Check My Symptoms button default](components/crops/check-button-default.png) ![Check My Symptoms button hover](components/crops/check-button-hover.png) ![Check My Symptoms button focus-visible](components/crops/check-button-focus-visible.png) ![Check My Symptoms button pressed](components/crops/check-button-pressed.png)

### Marketing and content pages

The Tailwind-utility content surface — the same pill-link top bar and dark CTA on /blog/, /telehealth/, /authors/, /resource-center/ and /wall-of-love/ — with its own literal hex values alongside the token layer.

#### Marketing top bar
The pill-link bar shared by the content pages: wordmark, About/FAQ/Blog/Online Treatment/Wall of Love, "Try Doctronic For Free" and Sign up. Read as `mkt-header` on the blog page.

**Values (default).** size 1440 x 56; background #e2f0e4; text Geist 14/21 600, #1a1a18; transition background-color 0.3s ease; icon 18 x 18, #ffffff `color.white`.

![Marketing top bar default](components/crops/mkt-header-default.png)

#### Marketing pill link
Read as `mkt-nav-pill` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 46.39 x 29; padding 4px 10px; radius 3.35544e+07px; background transparent; text Geist 14/21 600, #1a1a18; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | background oklab(0 0 0 / 0.05) |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers a.rounded-full.px-[10px] 46.4x29.0 1px auto rgb(0, 95, 204) offset 1px 3.35544e+07px |
| pressed | background oklab(0 0 0 / 0.05) |

![Marketing pill link default](components/crops/mkt-nav-pill-default.png) ![Marketing pill link hover](components/crops/mkt-nav-pill-hover.png) ![Marketing pill link focus-visible](components/crops/mkt-nav-pill-focus-visible.png) ![Marketing pill link pressed](components/crops/mkt-nav-pill-pressed.png)

#### Try Doctronic button
The dark rounded-full CTA link in the top bar. Measured, never followed. Read as `try-button` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 214.77 x 40; padding 10px 22px; radius 3.35544e+07px; background #0c0e12; text Geist 14/20 500, #ffffff `color.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 18 x 18, #ffffff `color.white` |
| hover | background oklch(0.269 0 0) |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background oklch(0.269 0 0) |

![Try Doctronic button default](components/crops/try-button-default.png) ![Try Doctronic button hover](components/crops/try-button-hover.png) ![Try Doctronic button focus-visible](components/crops/try-button-focus-visible.png) ![Try Doctronic button pressed](components/crops/try-button-pressed.png)

#### Marketing sign up
Measured, never pressed. Read as `mkt-signup` on the blog page.

Not on the page when it was captured.

#### Marketing footer
The link-column footer shared by the content pages. Read as `mkt-footer` on the blog page.

**Values (default).** size 1440 x 1414.5; background transparent; text Geist 18/25.2 600, #1b1b18 `color.neutral.900`; layers div 1440.0x96.0; div.absolute.inset-0 1440.0x1414.5; a.flex.items-center 59.1x34.8 T:1px solid rgba(27, 27, 24, 0.2) / R:1px solid rgba(27, 27, 24, 0.2) / B:1px solid rgba(27, 27, 24, 0.2) / L:1px solid rgba(27, 27, 24, 0.2) 32px; a.flex.items-center 65.6x32.8 rgb(27, 27, 24) 32px; div.w-full.border-t-2 1240.0x2.0 T:2px dashed rgba(26, 26, 24, 0.08).

Child layers that carry the look: div 1440x96 image linear-gradient(#ffffff `color.white`, transparent); div 1440x1414.5 image linear-gradient(#fdfdf8 0%, #e2f0e4 100%); a 59.1x34.8 border 1px solid rgba(27, 27, 24, 0.2) radius 32px.

![Marketing footer default](components/crops/mkt-footer-default.png)

#### Marketing footer link
Read as `mkt-footer-link` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 16 x 16; background transparent; text Geist 16/24 400, #1b1b18 `color.neutral.900`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | text Geist 16/24 400, #0f64e9 |
| focus-visible | outline 1px auto #005fcc, offset 1px; layers ::after rgba(0, 0, 0, 0) 0px none 1; a.relative.inline-flex 16.0x16.0 1px auto rgb(0, 95, 204) offset 1px |
| pressed | text Geist 16/24 400, #0f64e9 |

![Marketing footer link default](components/crops/mkt-footer-link-default.png) ![Marketing footer link hover](components/crops/mkt-footer-link-hover.png) ![Marketing footer link focus-visible](components/crops/mkt-footer-link-focus-visible.png) ![Marketing footer link pressed](components/crops/mkt-footer-link-pressed.png)

#### Blog title
Read as `blog-title` on the blog page.

**Values (default).** size 319.86 x 56.16; background transparent; text Fraunces 48/56.16 400, #242424.

![Blog title default](components/crops/blog-title-default.png)

#### Blog search field
Text was typed and deleted; search was never submitted. Read as `blog-search` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: focused) | size 730 x 39; background transparent; text Geist 14/21 400, #242424; placeholder #666666 |
| filled | size 706 x 39 |

![Blog search field default](components/crops/blog-search-default.png) ![Blog search field focused](components/crops/blog-search-focused.png) ![Blog search field filled](components/crops/blog-search-filled.png)

#### Article card
A post card: gradient thumbnail with a centred glyph, category/date line and title; the whole card is one link. Read as `article-card` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 370.66 x 480.28; border 1px solid #e5e7eb; radius 14px; background #ffffff `color.white`; text Geist 12/18 600, #000000; icon 64 x 64, rgba(15, 23, 42, 0.6) |

![Article card default](components/crops/article-card-default.png) ![Article card hover](components/crops/article-card-hover.png) ![Article card focus-visible](components/crops/article-card-focus-visible.png)

#### Article card title
Read as `article-card-title` on the blog page.

**Values (default).** size 324.66 x 105; background transparent; text Geist 25/26.25 500, #1a1a18.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Content h2
Read as `body-h2` on the blog page.

**Values (default).** size 386.77 x 28; background transparent; text Geist 20/28 700, #242424.

![Content h2 default](components/crops/body-h2-default.png)

#### Telehealth headline
Read as `telehealth-title` on the telehealth page.

**Values (default).** size 640 x 281.56; background transparent; text Fraunces 64/70.4 400, #000000.

![Telehealth headline default](components/crops/telehealth-title-default.png)

#### Telehealth lede
Read as `telehealth-lede` on the telehealth page.

**Values (default).** size 640 x 57; background transparent; text Geist 15/28.5 400, #5a5a54.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Telehealth CTA
The page's primary call to action — the dark "Try Doctronic For Free" pill shared with the top bar. Measured, never pressed. Read as `telehealth-cta` on the telehealth page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 214.77 x 40; padding 10px 22px; radius 3.35544e+07px; background #0c0e12; text Geist 14/20 500, #ffffff `color.white`; transition color 0.15s cubic-bezier(0.4, 0, 0.2, 1), background-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), outline-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), text-decoration-color 0.15s cubic-bezier(0.4, 0, 0.2, 1), fill 0.15s cubic-bezier(0.4, 0, 0.2, 1), stroke 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-from 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-via 0.15s cubic-bezier(0.4, 0, 0.2, 1), --tw-gradient-to 0.15s cubic-bezier(0.4, 0, 0.2, 1); icon 18 x 18, #ffffff `color.white` |
| hover | background oklch(0.269 0 0) |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | background oklch(0.269 0 0) |

![Telehealth CTA default](components/crops/telehealth-cta-default.png) ![Telehealth CTA hover](components/crops/telehealth-cta-hover.png) ![Telehealth CTA focus-visible](components/crops/telehealth-cta-focus-visible.png) ![Telehealth CTA pressed](components/crops/telehealth-cta-pressed.png)

#### Telehealth section heading
Read as `step-block` on the telehealth page.

**Values (default).** size 689.52 x 28.08; background transparent; text Fraunces 24/28.08 500, #1b1b18 `color.neutral.900`.

![Telehealth section heading default](components/crops/step-block-default.png)

#### Authors headline
Read as `authors-title` on the authors page.

**Values (default).** size 760 x 114.38; background transparent; text Fraunces 52/57.2 400, #0c0e12.

![Authors headline default](components/crops/authors-title-default.png)

#### Author card
A reviewer card: portrait, name and medical credential line, with a "View profile" link. Read as `author-card` on the authors page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 380 x 280.5; border T: 1px solid #e7e4de; background transparent; text Fraunces 20/24 400, #0c0e12; icon 16 x 16, #0961e4 |
| hover | text Fraunces 20/24 400, #0961e4; icon 16 x 16, oklch(0.424 0.199 265.638) |

![Author card default](components/crops/author-card-default.png) ![Author card hover](components/crops/author-card-hover.png)

#### Resource center headline
Read as `resource-title` on the resource center page.

**Values (default).** size 625.52 x 39.98; background transparent; text Fraunces 36/40 800, oklch(0.208 0.042 265.755).

![Resource center headline default](components/crops/resource-title-default.png)

#### Body copy
Read as `body-copy` on the resource center page.

**Values (default).** size 625.52 x 168; background transparent; text Geist 16/28 400, oklch(0.372 0.044 257.287).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Wall of Love headline
Read as `wall-title` on the Wall of Love page.

**Values (default).** size 664.11 x 86.41; background transparent; text Fraunces 72/86.4 400, #0c0e12.

![Wall of Love headline default](components/crops/wall-title-default.png)

#### Testimonial card
A review card on the Wall of Love: avatar, first name, quote and the Love/Reply footer row. Read as `love-card` on the Wall of Love page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 405.33 x 109.38; background transparent; text Geist 16/24 400, #0c0e12; layers div.group.relative 405.3x109.4 rgb(253, 253, 248) T:1px solid rgba(26, 26, 24, 0.08) / R:1px solid rgba(26, 26, 24, 0.08) / B:1px solid rgba(26, 26, 24, 0.08) / L:1px solid rgba(26, 26, 24, 0.08) 24px; div.pointer-events-none.absolute 0.0x0.0 rgb(240, 237, 233) 18px |
| hover | layers div.group.relative 405.3x109.4 rgb(253, 253, 248) T:1px solid rgba(26, 26, 24, 0.08) / R:1px solid rgba(26, 26, 24, 0.08) / B:1px solid rgba(26, 26, 24, 0.08) / L:1px solid rgba(26, 26, 24, 0.08) rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.08) 0px 8px 24px 0px 24px; div.pointer-events-none.a |

Child layers that carry the look: div 405.3x109.4 background #fdfdf8 border 1px solid rgba(26, 26, 24, 0.08) radius 24px; div 0x0 background #f0ede9 radius 18px.

![Testimonial card default](components/crops/love-card-default.png) ![Testimonial card hover](components/crops/love-card-hover.png)

#### Category chip
A tinted pill filtering the article grid ("Allergies", "Mental Health", …). Measured, never followed. Read as `category-chip` on the blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 77.08 x 28; padding 6px 10px; radius 3.35544e+07px; background #e6dbe6; text Geist 14/16 500, #242424; transition opacity 0.15s cubic-bezier(0.4, 0, 0.2, 1) |
| hover | opacity 0.7 |
| focus-visible | outline 1px auto #005fcc, offset 1px |
| pressed | opacity 0.7 |

![Category chip default](components/crops/category-chip-default.png) ![Category chip hover](components/crops/category-chip-hover.png) ![Category chip focus-visible](components/crops/category-chip-focus-visible.png) ![Category chip pressed](components/crops/category-chip-pressed.png)

#### Resource article sheet
The long-form white card the Resource Center is typeset into. Read as `resource-sheet` on the resource center page.

**Values (default).** size 689.52 x 10568.97; padding 32px; radius 16px; background #ffffff `color.white`; shadow rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.1) 0px 8px 10px -6px; text Fraunces 36/40 800, oklch(0.208 0.042 265.755).

![Resource article sheet default](components/crops/resource-sheet-default.png)

### Dialogs and overlays

The sign-in card reached by the public ?modal=signin URL: a centered raised dialog over a dimmed page with email and OAuth actions. Everything inside was measured, never pressed.

#### Sign-in dialog
Reached by the public ?modal=signin URL: a centered raised card over a dimmed page. Nothing inside it was pressed. Read as `signin-dialog` on the home (the ?modal=signin URL) page.

**Known wrong; recapture needed.** The reading is the transparent inner `section`, not the painted `div.modal` card.

**Values (default).** size 393 x 583.45; background transparent; text fraunces 32/37.44 400, #1b1b18 `color.neutral.900`; icon 16 x 16, #1b1b18 `color.neutral.900`; layers img.doctorImage 78.0x78.0 rgba(0, 0, 0, 0.1) 0px 5px 32px 0px 50%; img.patientImage 45.0x45.0 rgba(0, 0, 0, 0.1) 0px 5px 32px 0px 50%; span.content 329.0x43.6 rgb(36, 99, 235) color(srgb 0.141176 0.388235 0.921569 / 0.39) 0px 4px 7px 0px 52px; span.shimmer 329.0x43.6 52px; span.content 329.0x44.0 T:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / R:1px solid color(srgb 0.105882 0.105882 0.

Child layers that carry the look: img 78x78 radius 50% shadow rgba(0, 0, 0, 0.1) 0px 5px 32px 0px; img 45x45 radius 50% shadow rgba(0, 0, 0, 0.1) 0px 5px 32px 0px; span 329x43.6 background #2463eb `color.blue.600` radius 52px shadow rgba(36, 99, 235, 0.39) 0px 4px 7px 0px.

![Sign-in dialog default](components/crops/signin-dialog-default.png)

#### Sign-in title
Read as `signin-title` on the home (the ?modal=signin URL) page.

**Values (default).** size 256.61 x 74.88; background transparent; text fraunces 32/37.44 400, #1b1b18 `color.neutral.900`.

![Sign-in title default](components/crops/signin-title-default.png)

#### Log in with email button
The primary action inside the dialog. Measured, never pressed. Read as `email-login-button` on the home (the ?modal=signin URL) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 329 x 43.59; radius 52px; background transparent; text geist 14/19.6 600, #ffffff `color.white`; icon 16 x 16, #ffffff `color.white`; layers ::before rgba(0, 0, 0, 0) 0px none 1; span.content 329.0x43.6 rgb(36, 99, 235) color(srgb 0.141176 0.388235 0.921569 / 0.39) 0px 4px 7px 0px 52px; span.shimmer 329.0x43.6 52px |
| hover | layers ::before rgba(0, 0, 0, 0) 0px none 1; span.content 329.0x43.6 rgb(29, 79, 215) color(srgb 0.141176 0.388235 0.921569 / 0.5) 0px 6px 10px 0px 52px; span.shimmer 329.0x43.6 52px |
| focus-visible | shadow rgba(36, 99, 235, 0.39) 0px 4px 7px 0px, #0b0b0a 0px 0px 0px 2px; layers ::before rgba(0, 0, 0, 0) 0px none 1; button.button.hero 329.0x43.6 color(srgb 0.141176 0.388235 0.921569 / 0.39) 0px 4px 7px 0px, rgb(11, 11, 10) 0px 0px 0px 2px 52px; span.content 329.0x43.6 rgb(36, 99, 235) 52px; span.shimmer 329.0x43.6 52px |
| pressed | shadow rgba(36, 99, 235, 0.39) 0px 4px 7px 0px, #0b0b0a 0px 0px 0px 2px; icon 15.68 x 15.68, #ffffff `color.white`; layers ::before rgba(0, 0, 0, 0) 0px none 1; button.button.hero 329.0x43.6 color(srgb 0.141176 0.388235 0.921569 / 0.39) 0px 4px 7px 0px, rgb(11, 11, 10) 0px 0px 0px 2px 52px; span.content 322.4x42.7 rgb(30, 63, 174) 52px; span.shimmer 322.4x42.7 52px |

Child layers that carry the look: span 329x43.6 background #2463eb `color.blue.600` radius 52px shadow rgba(36, 99, 235, 0.39) 0px 4px 7px 0px; span 329x43.6 image linear-gradient(105deg, transparent 20%, rgba(253, 253, 247, 0.18) 50%, transparent 80%) radius 52px.

![Log in with email button default](components/crops/email-login-button-default.png) ![Log in with email button hover](components/crops/email-login-button-hover.png) ![Log in with email button focus-visible](components/crops/email-login-button-focus-visible.png) ![Log in with email button pressed](components/crops/email-login-button-pressed.png)

#### OAuth button
A Continue-with provider button. Measured, never pressed. Read as `oauth-button` on the home (the ?modal=signin URL) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 329 x 44; radius 40px; background transparent; text geist 14/19.6 600, #1b1b18 `color.neutral.900`; icon 16 x 16, #1b1b18 `color.neutral.900`; layers ::before rgba(0, 0, 0, 0) 0px none 1; span.content 329.0x44.0 T:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / R:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / B:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / L:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) 40px; span.shimmer 327.0x42.0 40px |
| hover | text geist 14/19.6 600, #fdfdf7 `color.neutral.50`; icon 16 x 16, #fdfdf7 `color.neutral.50`; layers ::before rgba(0, 0, 0, 0) 0px none 1; span.content 329.0x44.0 rgb(11, 11, 10) T:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / R:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / B:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / L:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) 40px; span.shimmer 327.0x42.0 40px |
| focus-visible | outline 2px solid #3c83f6 `color.blue.500`, offset 0px; layers ::before rgba(0, 0, 0, 0) 0px none 1; button.button.secondary 329.0x44.0 2px solid rgb(60, 131, 246) offset 0px 40px; span.content 329.0x44.0 T:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / R:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / B:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / L:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) 40px; span.shimmer 3 |
| pressed | outline 2px solid #3c83f6 `color.blue.500`, offset 0px; text geist 14/19.6 600, #fdfdf7 `color.neutral.50`; icon 15.68 x 15.68, #fdfdf7 `color.neutral.50`; layers ::before rgba(0, 0, 0, 0) 0px none 1; button.button.secondary 329.0x44.0 2px solid rgb(60, 131, 246) offset 0px 40px; span.content 322.4x43.1 rgb(27, 27, 24) T:1px solid rgb(27, 27, 24) / R:1px solid rgb(27, 27, 24) / B:1px solid rgb(27, 27, 24) / L:1px solid rgb(27, 27, 24) 40px; span.shimmer 320.5x41.2 40px |

Child layers that carry the look: span 329x44 border 1px solid rgba(27, 27, 24, 0.2) radius 40px; span 327x42 image linear-gradient(105deg, transparent 20%, rgba(253, 253, 247, 0.18) 50%, transparent 80%) radius 40px.

![OAuth button default](components/crops/oauth-button-default.png) ![OAuth button hover](components/crops/oauth-button-hover.png) ![OAuth button focus-visible](components/crops/oauth-button-focus-visible.png) ![OAuth button pressed](components/crops/oauth-button-pressed.png)

#### Create an account link
Measured, never followed. Read as `create-account-link` on the home (the ?modal=signin URL) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 128.22 x 21; background transparent; text geist 16/22.4 400, #2463eb `color.blue.600` |
| focus-visible, pressed | outline 1px auto #005fcc, offset 1px; layers a.signupLink 128.2x21.0 1px auto rgb(0, 95, 204) offset 1px |

![Create an account link default](components/crops/create-account-link-default.png) ![Create an account link hover](components/crops/create-account-link-hover.png) ![Create an account link focus-visible](components/crops/create-account-link-focus-visible.png) ![Create an account link pressed](components/crops/create-account-link-pressed.png)

#### Dialog close button
Read as `dialog-close` on the home (the ?modal=signin URL) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 32 x 32; radius 100px; background transparent; text -apple-system 16/normal 400, #1b1b18 `color.neutral.900`; icon 16 x 16, #1b1b18 `color.neutral.900`; layers ::after rgba(0, 0, 0, 0) 0px none 1 |
| hover | layers ::after rgba(0, 0, 0, 0) 0px none 1; span.surface 32.0x32.0 rgb(245, 245, 240) 100px |
| focus-visible | shadow #2463eb 0px 0px 0px 2px; layers ::after rgba(0, 0, 0, 0) 0px none 1; button.buttonBase.expandHitArea 32.0x32.0 rgb(36, 99, 235) 0px 0px 0px 2px 100px |

![Dialog close button default](components/crops/dialog-close-default.png) ![Dialog close button hover](components/crops/dialog-close-hover.png) ![Dialog close button focus-visible](components/crops/dialog-close-focus-visible.png) ![Dialog close button pressed](components/crops/dialog-close-pressed.png)

### Dark theme (data-theme="dark")

The home surface re-measured under the site's real dark theme — localStorage.theme=dark sets data-theme on <html>, which redeclares the semantic colour roles and the focus ring.

#### Top bar, dark
The same bar under data-theme="dark": sunken dark ground, light text. Read as `d-header` on the home in dark theme page.

**Values (default).** size 1440 x 72; background transparent; text geist 12/16.8 600, #fdfdf7 `color.neutral.50`; transition transform 0.25s ease; layers div.content.contentShrink 1440.0x72.0 rgb(13, 14, 11); span.content 59.1x34.8 T:1px solid color(srgb 0.992157 0.992157 0.968627 / 0.2) / R:1px solid color(srgb 0.992157 0.992157 0.968627 / 0.2) / B:1px solid color(srgb 0.992157 0.992157 0.968627 / 0.2) / L:1px solid color(srgb 0.992157 0.992157 0.968627 / 0.2) 32px; span.shimmer 57.1x32.8 32px; span.content 65.6x32.8 rgb(253, 253, 247) 32px; span..

Child layers that carry the look: div 1440x72 background #0d0e0b; span 59.1x34.8 border 1px solid rgba(253, 253, 247, 0.2) radius 32px; span 57.1x32.8 image linear-gradient(105deg, transparent 20%, rgba(11, 11, 10, 0.18) 50%, transparent 80%) radius 32px.

![Top bar, dark default](components/crops/d-header-default.png)

#### Sign up button, dark
Read as `d-signup-button` on the home in dark theme page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 65.64 x 34.8; radius 32px; background transparent; text geist 12/16.8 600, #0b0b0a `color.neutral.950`; layers ::before rgba(0, 0, 0, 0) 0px none 1; span.content 65.6x32.8 rgb(253, 253, 247) 32px; span.shimmer 65.6x32.8 32px |
| hover | layers ::before rgba(0, 0, 0, 0) 0px none 1; span.content 65.6x32.8 rgb(228, 228, 220) 32px; span.shimmer 65.6x32.8 32px |
| focus-visible | outline 2px solid #61a6fa `color.blue.400`, offset 0px; layers ::before rgba(0, 0, 0, 0) 0px none 1; button.button.primary 65.6x34.8 2px solid rgb(97, 166, 250) offset 0px 32px; span.content 65.6x32.8 rgb(253, 253, 247) 32px; span.shimmer 65.6x32.8 32px |
| pressed | layers ::before rgba(0, 0, 0, 0) 0px none 1; span.content 64.3x32.1 rgb(245, 245, 240) 32px; span.shimmer 64.3x32.1 32px |

Child layers that carry the look: span 65.6x32.8 background #fdfdf7 `color.neutral.50` radius 32px; span 65.6x32.8 image linear-gradient(105deg, transparent 20%, rgba(11, 11, 10, 0.18) 50%, transparent 80%) radius 32px.

![Sign up button, dark default](components/crops/d-signup-button-default.png) ![Sign up button, dark hover](components/crops/d-signup-button-hover.png) ![Sign up button, dark focus-visible](components/crops/d-signup-button-focus-visible.png) ![Sign up button, dark pressed](components/crops/d-signup-button-pressed.png)

#### Hero, dark
Read as `d-hero` on the home in dark theme page.

**Values (default).** size 548 x 421.5; background transparent; text fraunces 48/56.16 400, #fdfdf7 `color.neutral.50`; icon 20 x 20, #000000; layers div.content 150.5x36.6 color(srgb 0.85098 1 0.501961 / 0.5) 16px 18px 18px 2px; div::before.material 148.453pxx34.5938px 16px 18px 18px 2px; div::after.material 150.453pxx36.5938px rgba(128, 128, 128, 0) 16px 18px 18px 2px; div.edgeReflection 186.5x72.6 T:18px solid rgba(0, 0, 0, 0) / R:18px solid rgba(0, 0, 0, 0) / B:18px solid rgba(0, 0, 0, 0) / L:18px solid rgba(0, 0, 0, 0) 34px 36px 36px 20px;.

Child layers that carry the look: div 150.5x36.6 background rgba(217, 255, 128, 0.5) radius 16px 18px 18px 2px; div::before 148.453pxx34.5938px image linear-gradient(155deg, rgba(255, 255, 255, 0.06) 0%, rgba(0, 0, 0, 0.06) 50%, rgba(255, 2 radius 16px 18px 18px 2px; div::after 150.453pxx36.5938px background rgba(128, 128, 128, 0) radius 16px 18px 18px 2px.

![Hero, dark default](components/crops/d-hero-default.png)

#### Hero headline, dark
Read as `d-hero-title` on the home in dark theme page.

**Values (default).** size 378.56 x 56.16; background transparent; text fraunces 48/56.16 400, #fdfdf7 `color.neutral.50`.

![Hero headline, dark default](components/crops/d-hero-title-default.png)

#### Chat field, dark
Read as `d-input-card` on the home in dark theme page.

**Values (default).** size 548 x 147.38; padding 16px; border 1px solid rgba(253, 253, 247, 0.08); radius 16px; background #1b1b18 `color.neutral.900`; shadow rgba(0, 0, 0, 0.06) 0px 2px 24px 0px; text geist 12/16.8 500, #61a6fa `color.blue.400`; icon 20 x 20, #000000.

![Chat field, dark default](components/crops/d-input-card-default.png)

#### Start chat button, dark
Read as `d-start-button` on the home in dark theme page.

**Values (default).** size 136.36 x 43.59; radius 52px; background transparent; text geist 14/19.6 600, #172554 `color.blue.950`; icon 16 x 16, #172554 `color.blue.950`; layers ::before rgba(0, 0, 0, 0) 0px none 1; span.content.submitButtonContent 136.4x43.6 rgb(97, 166, 250) color(srgb 0.380392 0.65098 0.980392 / 0.39) 0px 4px 7px 0px 52px; span.shimmer 136.4x43.6 52px.

Child layers that carry the look: span 136.4x43.6 background #61a6fa `color.blue.400` radius 52px shadow rgba(97, 166, 250, 0.39) 0px 4px 7px 0px; span 136.4x43.6 image linear-gradient(105deg, transparent 20%, rgba(11, 11, 10, 0.18) 50%, transparent 80%) radius 52px.

![Start chat button, dark default](components/crops/d-start-button-default.png)

#### Prompt pill, dark
Read as `d-pill` on the home in dark theme page.

**Values (default).** size 126.45 x 18; background transparent; text geist 14/19.6 600, #fdfdf7 `color.neutral.50`.

![Prompt pill, dark default](components/crops/d-pill-default.png)

#### Footer, dark
Read as `d-footer` on the home in dark theme page.

**Values (default).** size 1440 x 1414.5; background transparent; text geist 18/25.2 600, #fdfdf7 `color.neutral.50`; layers div.gradient 1440.0x1414.5; span.content 59.1x34.8 T:1px solid color(srgb 0.992157 0.992157 0.968627 / 0.2) / R:1px solid color(srgb 0.992157 0.992157 0.968627 / 0.2) / B:1px solid color(srgb 0.992157 0.992157 0.968627 / 0.2) / L:1px solid color(srgb 0.992157 0.992157 0.968627 / 0.2) 32px; span.shimmer 57.1x32.8 32px; span.content 65.6x32.8 rgb(253, 253, 247) 32px; span.shimmer 65.6x32.8 32px; div.

Child layers that carry the look: div 1440x1414.5 image linear-gradient(#fdfdf7 `color.neutral.50` 0%, #e1efe3 `color.sage.100` 100%); span 59.1x34.8 border 1px solid rgba(253, 253, 247, 0.2) radius 32px; span 57.1x32.8 image linear-gradient(105deg, transparent 20%, rgba(11, 11, 10, 0.18) 50%, transparent 80%) radius 32px.

![Footer, dark default](components/crops/d-footer-default.png)

### Mobile (390 wide)

The same surface at phone width: the top bar shrinks to wordmark + actions + menu, and the chat rail collapses into a mobile header.

#### Top bar (mobile)
The 390px header: wordmark, Sign up and the menu button (Log in is dropped at this width). Read as `m-header` on the home page at 390 wide.

**Values (default).** size 390 x 72; background transparent; text geist 12/16.8 600, #fdfdf7 `color.neutral.50`; transition transform 0.25s ease; icon 115.89 x 22, #1b1b18 `color.neutral.900`; layers div.content.contentShrink 390.0x72.0 rgb(253, 253, 247); span.content 0.0x0.0 T:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / R:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / B:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / L:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) 32px; span.shimmer 0.0x0.0 32px; span.content 65.6x32.8 rgb(11, 11, 10) 32px; span.s.

Child layers that carry the look: div 390x72 background #fdfdf7 `color.neutral.50`; span 0x0 border 1px solid rgba(27, 27, 24, 0.2) radius 32px; span 0x0 image linear-gradient(105deg, transparent 20%, rgba(253, 253, 247, 0.18) 50%, transparent 80%) radius 32px.

![Top bar (mobile) default](components/crops/m-header-default.png)

#### Mobile menu button
Read as `m-menu-button` on the home page at 390 wide.

**Values (default).** size 40 x 40; radius 100px; background transparent; text -apple-system 16/normal 400, #1b1b18 `color.neutral.900`; icon 24 x 24, #1b1b18 `color.neutral.900`; layers ::after rgba(0, 0, 0, 0) 0px none 1.

![Mobile menu button default](components/crops/m-menu-button-default.png)

#### Hero (mobile)
Read as `m-hero` on the home page at 390 wide.

**Values (default).** size 342 x 535.94; background transparent; text fraunces 32/37.44 400, #1b1b18 `color.neutral.900`; icon 20 x 20, #000000; layers div.content 150.5x36.6 color(srgb 0.85098 1 0.501961 / 0.5) 16px 18px 18px 2px; div::before.material 148.453pxx34.5938px 16px 18px 18px 2px; div::after.material 150.453pxx36.5938px rgba(128, 128, 128, 0) 16px 18px 18px 2px; div.edgeReflection 186.5x72.6 T:18px solid rgba(0, 0, 0, 0) / R:18px solid rgba(0, 0, 0, 0) / B:18px solid rgba(0, 0, 0, 0) / L:18px solid rgba(0, 0, 0, 0) 34px 36px 36px 20px;.

Child layers that carry the look: div 150.5x36.6 background rgba(217, 255, 128, 0.5) radius 16px 18px 18px 2px; div::before 148.453pxx34.5938px image linear-gradient(155deg, rgba(255, 255, 255, 0.06) 0%, rgba(0, 0, 0, 0.06) 50%, rgba(255, 2 radius 16px 18px 18px 2px; div::after 150.453pxx36.5938px background rgba(128, 128, 128, 0) radius 16px 18px 18px 2px.

![Hero (mobile) default](components/crops/m-hero-default.png)

#### Hero headline (mobile)
Read as `m-hero-title` on the home page at 390 wide.

**Values (default).** size 252.39 x 37.44; background transparent; text fraunces 32/37.44 400, #1b1b18 `color.neutral.900`.

![Hero headline (mobile) default](components/crops/m-hero-title-default.png)

#### Chat field (mobile)
Read as `m-input-card` on the home page at 390 wide.

**Values (default).** size 342 x 155.77; padding 16px; border 1px solid rgba(27, 27, 24, 0.08); radius 16px; background #ffffff `color.white`; shadow rgba(0, 0, 0, 0.06) 0px 2px 24px 0px; text geist 12/16.8 500, #2463eb `color.blue.600`; icon 20 x 20, #000000.

![Chat field (mobile) default](components/crops/m-input-card-default.png)

#### Start chat button (mobile)
Read as `m-start-button` on the home page at 390 wide.

**Values (default).** size 136.36 x 43.59; radius 52px; background transparent; text geist 14/19.6 600, #ffffff `color.white`; icon 16 x 16, #ffffff `color.white`; layers ::before rgba(0, 0, 0, 0) 0px none 1; span.content.submitButtonContent 136.4x43.6 rgb(36, 99, 235) color(srgb 0.141176 0.388235 0.921569 / 0.39) 0px 4px 7px 0px 52px; span.shimmer 136.4x43.6 52px.

Child layers that carry the look: span 136.4x43.6 background #2463eb `color.blue.600` radius 52px shadow rgba(36, 99, 235, 0.39) 0px 4px 7px 0px; span 136.4x43.6 image linear-gradient(105deg, transparent 20%, rgba(253, 253, 247, 0.18) 50%, transparent 80%) radius 52px.

![Start chat button (mobile) default](components/crops/m-start-button-default.png)

#### Footer (mobile)
Read as `m-footer` on the home page at 390 wide.

**Values (default).** size 390 x 1643.25; background transparent; text geist 18/25.2 600, #1b1b18 `color.neutral.900`; layers div.gradient 390.0x1643.3; span.content 59.1x34.8 T:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / R:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / B:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / L:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) 32px; span.shimmer 57.1x32.8 32px; span.content 65.6x32.8 rgb(11, 11, 10) 32px; span.shimmer 65.6x32.8 32px; div.

Child layers that carry the look: div 390x1643.3 image linear-gradient(#fdfdf7 `color.neutral.50` 0%, #e1efe3 `color.sage.100` 100%); span 59.1x34.8 border 1px solid rgba(27, 27, 24, 0.2) radius 32px; span 57.1x32.8 image linear-gradient(105deg, transparent 20%, rgba(253, 253, 247, 0.18) 50%, transparent 80%) radius 32px.

![Footer (mobile) default](components/crops/m-footer-default.png)

#### Chat top bar (mobile)
Read as `m-chat-header` on the /chat/ page at 390 wide.

**Values (default).** size 390 x 66.8; padding 16px; background transparent; text geist 12/16.8 600, #1b1b18 `color.neutral.900`; icon 24 x 24, #1b1b18 `color.neutral.900`; layers span.content 59.1x34.8 T:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / R:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / B:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) / L:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.2) 32px; span.shimmer 57.1x32.8 32px.

Child layers that carry the look: span 59.1x34.8 border 1px solid rgba(27, 27, 24, 0.2) radius 32px; span 57.1x32.8 image linear-gradient(105deg, transparent 20%, rgba(253, 253, 247, 0.18) 50%, transparent 80%) radius 32px.

![Chat top bar (mobile) default](components/crops/m-chat-header-default.png)

#### Chat input card (mobile)
Read as `m-input-card-chat` on the /chat/ page at 390 wide.

**Values (default).** size 342 x 148; background transparent; text geist 12/16.8 500, #2463eb `color.blue.600`; icon 20 x 20, #000000; layers form.inputCard.inputCardExpanded 342.0x126.0 rgb(255, 255, 255) T:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.08) / R:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.08) / B:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.08) / L:1px solid color(srgb 0.105882 0.105882 0.0941176 / 0.08) rgba(0, 0, 0, 0.06) 0px 2px 24px 0px 16px; button.badgeButton 105.6x32.0 T:1px dashed color(sr.

Child layers that carry the look: form 342x126 background #ffffff `color.white` border 1px solid rgba(27, 27, 24, 0.08) radius 16px shadow rgba(0, 0, 0, 0.06) 0px 2px 24px 0px; button 105.6x32 border 1px dashed rgba(27, 27, 24, 0.08) radius 34px; span 32x32 background #2463eb `color.blue.600` radius 52px shadow rgba(36, 99, 235, 0.39) 0px 4px 7px 0px.

![Chat input card (mobile) default](components/crops/m-input-card-chat-default.png)

#### Starter chip (mobile)
Read as `m-starter` on the /chat/ page at 390 wide.

**Values (default).** size 164.11 x 36.59; padding 8px 16px; radius 8px; background #f5f5f0 `color.neutral.100`; text geist 14/19.6 500, #1b1b18 `color.neutral.900`; transition background-color 0.15s ease-in.

![Starter chip (mobile) default](components/crops/m-starter-default.png)

## Icons

No standalone SVG icon set was lifted on this pass; the icons in the crops and screenshots (the Doctronic wordmark, the arrow/spark glyphs in buttons and chips, the Trustpilot stars and the testimonial artwork) are the product's artwork. Declared under layoutGaps in the catalog entry.

| Icon | Rendered sizes | View box | Style | Seen on | Next to |
|---|---|---|---|---|---|

## Gaps

### The signed-in product

Everything behind Log in and Sign up — the chat product's real threads, the health record, prescriptions, appointments, account and billing — was never reached. The sign-in card was rendered from the public ?modal=signin URL and measured, and nothing inside it (email login, the OAuth buttons, Create an account) was pressed. What the authenticated app looks like or how it behaves is not documented here; the marketing pages' claims about it were never verified.

### Pages

- **Chat actions.** Start chat, Send message, Check My Symptoms, the suggestion chips, View recent chats and the Anonymous badge were measured, never pressed — each would start a session or submit text.
- **Auth and sign-up actions.** Sign up, Sign up for free, Try Doctronic For Free, Log in, Log in with email, the OAuth buttons and Create an account were measured, never followed; no account was created.
- **Medical record / prescription links** in the site-menu drawer and footers were left unfollowed where they lead to account surfaces.
- **The mobile app's Open/App Store banner**, where it appears, was left untouched.

### States

- **Pressed** was forced with DevTools on every control, so a state a script adds on mousedown (if any) is missing.
- **Disabled, error and loading states** were only seen where the page paints them at rest (the declared *-disabled tokens are in the token file); no form was submitted to provoke an error.
- **The chat rail's signed-in content** (recent chats, history) only fills for a signed-in visitor; the rail was measured expanded in its signed-out state.

### Themes

doctronic.ai ships a real user-selectable dark theme: `localStorage.theme` is `light`, `dark` or `system`, an init script sets `data-theme` on `<html>` and the stylesheets redeclare the semantic `--color-*` roles and the focus ring under `[data-theme="dark"]` (harvested in [raw/css-vars.json](raw/css-vars.json)). The app surfaces (home, /chat/, the symptom checker, resource center, blog, telehealth, our-philosophy) were captured in both themes; the darker content pages keep their light Tailwind paint under `data-theme="dark"` — the utility classes carry literal hex, not theme vars — which the token file records honestly as a dark set scoped to the token-driven surfaces.

### Fonts

- **fraunces** (400/600, plus italics), **geist** (400/500/600) and **geistMono** (400/600) are self-hosted woff2 files declared in @font-face blocks in the Next.js chunks (the src list is in [raw/css-vars.json](raw/css-vars.json)). The style guide does not load them — they are the product's licensed faces — so its samples fall back to Georgia and the system sans.
- **The plain body font** (`--font-body`) is the Apple system stack (SF Pro Text → Segoe UI → Roboto…), not a webfont.

### Screenshots

- The hero illustration, the testimonial photos, the condition-page imagery and the Doctronic wordmark in the screenshots are the product's published content; only frames and components were measured.
- The invisible-reCAPTCHA badge is Google's chrome mounted over the page; it was hidden, never answered.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- Article copy, condition guidance, testimonials, the Hippocratic-oath text and the privacy/terms text are the product's content; only frames and components were measured.
