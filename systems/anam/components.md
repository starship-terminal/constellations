# Anam components

The discovery list of every page and view captured, then one entry per component with crops of the real product and the Gaps. Captured from anam.ai on 2026-11-10, signed out, in headless Chromium at 1440 x 900 (the Mobile group at 390 x 844), with computed styles read from the running pages. Nothing was signed into, created, sent or uploaded; the avatar call button was never pressed and no consent choice was made.

anam.ai is three public surfaces with one accent: the **marketing pages** (Framer: white ground, black ink and pills, orange #ff6200, frosted-glass chips on the avatar videos), the **app pages** /pricing, /get-demo and /tools (Next.js: a small `:root` token set — `--bg`, `--surface`, `--text`, `--border`, `--brand`), and the **docs** (Mintlify: a warm-stone gray ramp on `:root`, Inter and Paper Mono, the same orange as `--primary`). Only the docs ship a dark theme.

The full per-state readings are in [raw/measurements.md](raw/measurements.md), with the machine-readable copy in [raw/components-computed.json](raw/components-computed.json) (79 components, 146 states). The page layouts are described in [raw/layout.json](raw/layout.json).

How to read an entry:

- A colour is its value followed by the palette token in [tokens.json](tokens.json) with the same value, when there is one. Text is written family size/line-height weight, then its colour, for example `Inter 15/18 500, #000`, and is read from the first text node inside the component.
- The state table has one row per state that differs. The first row lists every value; later rows list only what changes. A state with the same values as the first is named in its label, for example "default (same: focus-visible)". When the root paints nothing, "Child layers" names the first nodes inside it that do.
- Crops are images of the component read from the live page, in [components/crops/](components/crops) (133 files, named `{component}-{state}.png`, at 2x). Screenshots are in [screenshots/](screenshots).

## Discovery list

Screenshots are named `{page}-light-{state}.png` (the dark docs pass is `docs-dark-dark-{state}.png`). Desktop shots are 1440 x 900 at 1x; `-full` shots are whole pages at 1x; mobile shots are `mobile-{page}-light-{state}.png`, 780 wide (390 at 2x).

| Surface | URL | Screenshots |
|---|---|---|
| anam.ai home. Hero and badge, the persona video carousel, the demo card, feature sections, logo cloud, sticky CTA and the dark footer panel. | `https://anam.ai/` | [consent](screenshots/home-light-consent.png), [default](screenshots/home-light-default.png), [full](screenshots/home-light-full.png), [nav-submenu](screenshots/home-light-nav-submenu.png), [persona-tab](screenshots/home-light-persona-tab.png) |
| anam.ai/api. The API marketing page: hero, code and feature sections. | `https://anam.ai/api` | [default](screenshots/api-light-default.png), [full](screenshots/api-light-full.png) |
| anam.ai/interactive-avatars. The avatar gallery page. | `https://anam.ai/interactive-avatars` | [default](screenshots/interactive-avatars-light-default.png), [full](screenshots/interactive-avatars-light-full.png) |
| anam.ai/pricing. Title, billing toggle, plan cards, FAQ. | `https://anam.ai/pricing` | [billing-toggle](screenshots/pricing-light-billing-toggle.png), [default](screenshots/pricing-light-default.png), [full](screenshots/pricing-light-full.png) |
| anam.ai/get-demo. The demo request form; the email field shown focused. | `https://anam.ai/get-demo` | [default](screenshots/get-demo-light-default.png), [field-focused](screenshots/get-demo-light-field-focused.png), [full](screenshots/get-demo-light-full.png) |
| anam.ai/tools. The tools index (latency benchmark and friends). | `https://anam.ai/tools` | [default](screenshots/tools-light-default.png), [full](screenshots/tools-light-full.png) |
| anam.ai/about. Team and company page. | `https://anam.ai/about` | [default](screenshots/about-light-default.png), [full](screenshots/about-light-full.png) |
| anam.ai/research. Papers and model entries. | `https://anam.ai/research` | [default](screenshots/research-light-default.png), [full](screenshots/research-light-full.png) |
| anam.ai/case-studies. Customer story cards. | `https://anam.ai/case-studies` | [default](screenshots/case-studies-light-default.png), [full](screenshots/case-studies-light-full.png) |
| anam.ai/blog. Post cards. | `https://anam.ai/blog` | [default](screenshots/blog-light-default.png), [full](screenshots/blog-light-full.png) |
| anam.ai/changelog. Release entries. | `https://anam.ai/changelog` | [default](screenshots/changelog-light-default.png), [full](screenshots/changelog-light-full.png) |
| anam.ai docs overview. Sidebar, TOC, prose, cards; also the ⌘K dialog and the ⌘I assistant sheet. | `https://anam.ai/docs/introduction/overview` | [assistant-panel](screenshots/docs-overview-light-assistant-panel.png), [default](screenshots/docs-overview-light-default.png), [full](screenshots/docs-overview-light-full.png), [search-dialog](screenshots/docs-overview-light-search-dialog.png) |
| anam.ai docs API reference. Sidebar with method badges, code blocks. | `https://anam.ai/docs/api-reference/overview` | [default](screenshots/docs-api-light-default.png), [full](screenshots/docs-api-light-full.png) |
| anam.ai docs in its dark theme (.dark on html). | `https://anam.ai/docs/introduction/overview` | [default](screenshots/docs-dark-dark-default.png), [full](screenshots/docs-dark-dark-full.png) |
| anam.ai home at 390: menu button, hero, persona carousel, CTA; the consent card shown, then hidden. | `https://anam.ai/` | [consent](screenshots/mobile-home-light-consent.png), [default](screenshots/mobile-home-light-default.png), [full](screenshots/mobile-home-light-full.png), [nav-open](screenshots/mobile-home-light-nav-open.png) |
| anam.ai/pricing at 390. | `https://anam.ai/pricing` | [default](screenshots/mobile-pricing-light-default.png), [full](screenshots/mobile-pricing-light-full.png) |
| anam.ai docs overview at 390: the sidebar is behind the menu button. | `https://anam.ai/docs/introduction/overview` | [default](screenshots/mobile-docs-overview-light-default.png), [full](screenshots/mobile-docs-overview-light-full.png) |

### Overlays and transient states

| State | Where | How it was reached | Captured |
|---|---|---|---|
| Cookie consent card | the marketing pages and mobile home, on load on a fresh profile | photographed and measured in place, then hidden without a click — a consent choice is a submission | [home-light-consent](screenshots/home-light-consent.png), [mobile-home-light-consent](screenshots/mobile-home-light-consent.png), [consent-card](#cookie-consent-card) |
| Nav submenu | the pill nav, on hover over Developers or Company | a real hover opened the dropdown; captured open, never clicked through | [home-light-nav-submenu](screenshots/home-light-nav-submenu.png), [nav-submenu](#nav-submenu) |
| Persona carousel | anam.ai home, on load | the carousel keeps every persona's card parked in a strip; a second card was clicked into the centre for the selected state | [home-light-persona-tab](screenshots/home-light-persona-tab.png), [persona-chip](#persona-chip) |
| Docs ⌘K search dialog | anam.ai/docs | opened with ControlOrMeta+K; measured open, nothing typed | [docs-overview-light-search-dialog](screenshots/docs-overview-light-search-dialog.png), [docs-search-dialog](#search-dialog) |
| Docs ⌘I assistant sheet | anam.ai/docs | the sheet is open by default; measured in place, nothing sent | [docs-overview-light-assistant-panel](screenshots/docs-overview-light-assistant-panel.png), [docs-assistant-panel](#assistant-panel) |
| Talk-with call controls | anam.ai home, inside the demo card | measured and hovered, never pressed: a press opens a live session on Anam's servers and asks for the microphone | [demo-cta](#demo-call-button) |

## Checklist coverage

The 19 components of the library's checklist ([docs/DESIGN-SYSTEM.md](../../docs/DESIGN-SYSTEM.md)), each with the entries below that show it and the states captured across them. 13 of 19 are captured; the rest do not exist on the public pages.

| Component | Entries | States captured |
|---|---|---|
| Button | [Hero CTA button](#hero-cta-button), [Demo call button](#demo-call-button), [Plan CTA button](#plan-cta-button), [Submit button](#submit-button), [Accept all button](#accept-all-button), [Search button](#search-button), [Ask Assistant button](#ask-assistant-button), [Assistant send button](#assistant-send-button), [Theme menu button](#theme-menu-button) | default, hover, focus-visible, pressed |
| Icon button | [Theme menu button](#theme-menu-button), [Assistant send button](#assistant-send-button) | default, hover, focus-visible |
| Link | [Nav link](#nav-link), [Sign in link](#sign-in-link), [Submenu link](#submenu-link), [Footer link](#footer-link), [Sidebar link](#sidebar-link), [TOC link](#toc-link), [Top nav tab](#top-nav-tab) | default, hover, focus-visible, pressed |
| Text field | [Text field](#text-field), [Search field](#search-field) | default, focused, filled |
| Text area | [Text area](#text-area) | default, focused |
| Select | not captured: no public page offers one | - |
| Checkbox | not captured: no public form has one | - |
| Radio | not captured: no radio control on the public pages; the billing toggle is a pair of buttons | - |
| Switch | [Billing period toggle](#billing-period-toggle) | default, hover, focus-visible |
| Tabs | [Feature tab](#feature-tab), [Top nav tab](#top-nav-tab) | default, hover, focus-visible |
| Menu | [Nav submenu](#nav-submenu) | default |
| Tooltip | not captured: none appeared on hover or focus | - |
| Dialog | [Search dialog](#search-dialog), [Assistant panel](#assistant-panel) | default |
| Toast | not captured: no toast appeared after any action the capture took signed out | - |
| Card | [Persona chip](#persona-chip), [Persona chip, selected](#persona-chip-selected), [Avatar demo card](#avatar-demo-card), [Plan card](#plan-card), [Docs link card](#docs-link-card), [Cookie consent card](#cookie-consent-card), [Feature card](#feature-card) | default, hover, focus-visible, pressed |
| List row | [FAQ item](#faq-item) | default |
| Table | not captured: pricing lays plans out as cards, not a table | - |
| Avatar | [Persona chip](#persona-chip), [Avatar demo card](#avatar-demo-card) | default, hover, focus-visible, pressed |
| Badge | [Method badge](#method-badge), [Hero subline](#hero-subline) | default |

## Shared values

Values that apply across entries, from the measurement files.

**Focus.** 26 components were given a real keyboard focus. 19 show a change: `consent-manage` (2px solid #000000 `black`, offset 2px), `consent-accept` (2px solid #000000 `black`, offset 2px), `nav-link` (1px solid rgba(0, 0, 0, 0.18), offset 2px), `nav-signin` (1px auto #005fcc, offset 1px), `footer-link` (1px auto #005fcc, offset 1px), `hero-cta` (1px auto #005fcc, offset 1px), `persona-chip` (1px auto #005fcc, offset 0px), `nav-sub-link` (2px solid #ff6200 `brand.500`, offset 3px), `billing-toggle` (2px solid #ff6200 `brand.500`, offset 3px), `plan-cta` (2px solid #ff6200 `brand.500`, offset 3px), `form-submit` (1px auto #005fcc, offset 0px), `docs-topnav-link` (1px auto #ff6200 `brand.500`, offset 1px), `docs-search-btn` (1px auto #ff6200 `brand.500`, offset 0px), `docs-assistant-btn` (1px auto #ff6200 `brand.500`, offset 0px), `docs-theme-btn` (1px auto #ff6200 `brand.500`, offset 0px), `docs-card` (1px auto #ff6200 `brand.500`, offset 0px), `demo-cta` (1px auto #005fcc, offset 0px), `tool-card` (2px solid #ff6200 `brand.500`, offset 4px), `docs-prev-next` (2px solid #ff6200 `brand.500`, offset 2px). The other 7 draw nothing new — anam.ai largely lets the browser's own outline stand (Framer links take the default `auto` outline; the docs buttons keep their resting style): `tab-item`, `avatar-card`, `about-card`, `research-card`, `case-card`, `post-card`, `changelog-entry`. Keyboard focus could not be moved to `docs-nav-link`, `docs-toc-link`, `docs-assistant-send`, so those have no focus reading.

**Pressed.** Pressed was forced with DevTools, so it is the :active styles only: the plan CTA measurably shrinks a couple of pixels under :active (137.81x44 to 133.68x42.68 — a scale press), while the marketing pills and docs buttons keep their resting paint; the call controls were never really pressed because a press opens a live session.

**Motion.** Transitions measured on the components, by duration. The signature motion is the persona carousel's `transform .3s cubic-bezier(.12,.23,.5,1)` spring and the consent card's 240ms rise-in (`anam-cc-rise`); the scroll-driven TabSection animates on scroll, not on a transition.

| Duration | Easing | Property | Where |
|---|---|---|---|
| 0.04s | `ease` | transform | form-submit |
| 0.15s | `ease` | background, box-shadow, color, opacity | footer-link, form-input, form-submit, form-textarea |
| 0.16s | `cubic-bezier(0.16, 1, 0.3, 1)` | background-color | consent-accept, consent-manage |
| 0.16s | `ease` | border-color, transform | consent-accept, consent-manage, plan-cta |
| 0.2s | `cubic-bezier(0.44, 0, 0.56, 1)` | color | nav-link |
| 0.2s | `ease` | background-color, box-shadow, color | billing-toggle, plan-cta |
| 0.25s | `cubic-bezier(0.22, 1, 0.36, 1)` | opacity, scale, transform | docs-search-dialog |
| 0.3s | `cubic-bezier(0.12, 0.23, 0.5, 1)` | transform | m-persona-chip, persona-chip, persona-chip-selected |
| 0.4s | `cubic-bezier(0.44, 0, 0.56, 1)` | background, background-color, transform | nav-signin, tool-card |

**Layout.** Read on each page ([raw/layout.json](raw/layout.json)).

| Page | Frame | Content column | Grids | Fixed |
|---|---|---|---|---|
| home | - | full width | 4 grids (3 col gap 8px; 4 col gap 20px) | Developers (fixed) |
| api | - | full width | 1 grids (5 col gap 30px) | Developers (fixed), div (fixed) |
| pricing | - | max-width 820px | 8 grids (6 col gap 8px; 2 col gap 8px) | Skip to content (sticky) |
| get-demo | - | max-width 600px | 2 grids (2 col gap normal; 3 col gap 24px) | - |
| interactive-avatars | - | full width | 4 grids (2 col gap 16px; 4 col gap 20px) | Developers (fixed), div (fixed) |
| about | - | full width | 5 grids (8 col gap 21px; 5 col gap 20px) | Developers (fixed), div (fixed) |
| research | - | full width | 2 grids (4 col gap 20px; 5 col gap 30px) | Developers (fixed), div (fixed) |
| case-studies | - | full width | 2 grids (2 col gap 0px; 5 col gap 30px) | Developers (fixed), div (fixed) |
| blog | - | full width | 3 grids (2 col gap 20px; 3 col gap 20px) | Developers (fixed), div (fixed) |
| tools | - | max-width 620px | 8 grids (2 col gap 56px; 2 col gap 48px) | Developers (fixed) |
| docs-overview | - | max-width 1535.2px | 1 grids (3 col gap 16px) | Anam home page (sticky), Introduction (sticky), div (sticky) |
| docs-api | - | max-width 1535.2px | - | Anam home page (sticky), Use the API (sticky), div (sticky) |
| mobile-home | - | full width | 3 grids (2 col gap 12px; 2 col gap 12px) | Sign in (fixed) |
| mobile-docs | - | full width | - | Anam home page (fixed), span (fixed), div (sticky) |
| changelog | - | full width | 1 grids (5 col gap 30px) | Developers (fixed), Nov 3, 2026 (sticky), div (fixed) |

**Card shapes.** Default-state values; the entries hold the states. The marketing site's signature card is the 32px-radius persona tile over a long soft shadow with frosted-glass chips; the docs' is a 16px-radius white card with a warm hairline border.

| Card | Size | Border | Radius | Background | Shadow | Padding |
|---|---|---|---|---|---|---|
| [Persona chip](#persona-chip) | 340 x 451 | - | 50px | rgba(255, 255, 255, 0.5) `glass.fill` | none | 0 |
| [Avatar demo card](#avatar-demo-card) | 408 x 483.6 | - | 50px | rgba(255, 255, 255, 0.5) `glass.fill` | none | 0 |
| [Plan card](#plan-card) | 520 x 1133.19 | - | 50px | #000000 `black` | none | 0 |
| [Docs link card](#docs-link-card) | 218.94 x 230 | 1px solid rgba(17, 13, 10, 0.1) | 16px | #ffffff `white` | none | 0 |
| [Cookie consent card](#cookie-consent-card) | 420 x 180 | 1px solid rgba(0, 0, 0, 0.08) | 16px | #ffffff `white` | rgba(0, 0, 0, 0.18) 0px 12px 32px -8px, rgba(0, 0, 0, 0.06) 0px 1px 2px 0px | 20px |
| [Feature card](#feature-card) | 600 x 144 | - | - | transparent | none | 0 |
| [Search dialog](#search-dialog) | 640 x 62 | - | 20px | #ffffff `white` | rgba(17, 13, 10, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.01) 0px 57px 34px 0px, rgba(0, 0, 0, 0.02) 0px 25px 25px 0px, rgba(0, 0, 0, 0.02) 0px 6px 14px 0px | 0 |
| [Assistant panel](#assistant-panel) | 368 x 900 | 1px solid #e6e1de `neutral.200` | 16px | #ffffff `white` | none | 0 |

## Components

### Shell and navigation

The chrome shared by the marketing pages: a floating pill nav (Anam mark; Developers / Pricing / Resources with hover submenus; Sign in; a black Get started pill) and the footer, whose link columns sit on a 32px-radius black panel. On a phone the nav collapses to a menu button.

#### Top navigation bar
The floating pill nav on every marketing page: the Anam logo, the section links (Developers, Pricing, Resources, Company), Sign in and the Get started button. Read as `nav-bar` on the anam.ai tools page.

**Values (default).** size 1440 x 100; background transparent; text Inter 14/16.8 500, #000000 `black`; icon 60 x 22, #000000 `black`.

Child layers that carry the look: header::after 1440pxx523px background rgba(244, 244, 244, 0.55); div 1440x100 background #ffffff `white`; a 96.6x34 background #f5f5f5 `gray.100` radius 50px.

![Top navigation bar default](components/crops/nav-bar-default.png)

#### Nav link
A section link in the pill nav. Measured, never followed. Read as `nav-link` on the anam.ai tools page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 78.73 x 32.8; padding 8px 16px; background transparent; text Inter 14/16.8 500, #000000 `black`; transition color 0.2s cubic-bezier(0.44, 0, 0.56, 1) |
| hover | text Inter 14/16.8 500, rgba(0, 0, 0, 0.5) |
| focus-visible | radius 6px; outline 1px solid rgba(0, 0, 0, 0.18), offset 2px; text Inter 14/16.8 500, rgba(0, 0, 0, 0.5) |
| pressed | text Inter 14/16.8 500, rgba(0, 0, 0, 0.5) |

![Nav link default](components/crops/nav-link-default.png) ![Nav link hover](components/crops/nav-link-hover.png) ![Nav link focus-visible](components/crops/nav-link-focus-visible.png) ![Nav link pressed](components/crops/nav-link-pressed.png)

#### Sign in link
The quiet "Sign in" action (lab.anam.ai/login). Measured, never followed. Read as `nav-signin` on the anam.ai tools page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 96.58 x 34; padding 16px 24px; radius 50px; background #f5f5f5 `gray.100`; text Inter 15/15 500, #000000 `black`; transition background 0.4s cubic-bezier(0.44, 0, 0.56, 1), transform 0.4s cubic-bezier(0.44, 0, 0.56, 1) |
| hover | background #e8e6e6 |
| focus-visible | outline 1px auto #005fcc, offset 1px |

![Sign in link default](components/crops/nav-signin-default.png) ![Sign in link hover](components/crops/nav-signin-hover.png) ![Sign in link focus-visible](components/crops/nav-signin-focus-visible.png)

#### Nav submenu
The dropdown that opens under a nav section on hover (Developers: Documentation, Tools, Changelog; Company: Team, Research, Security). Shown in its hover-open state. Read as `nav-submenu` on the anam.ai tools page.

**Values (default).** size 222 x 128.91; background transparent; text Inter 13/16.9 500, rgba(0, 0, 0, 0.5).

![Nav submenu default](components/crops/nav-submenu-default.png)

#### Footer
The page footer: product/company/legal link columns, socials and the status line. Read as `footer` on the anam.ai tools page.

**Values (default).** size 1400 x 1154.59; padding 64px 0px 40px 0px; radius 32px; background #000000 `black`; text Inter 15/18 400, rgba(255, 255, 255, 0.5) `glass.fill`.

![Footer default](components/crops/footer-default.png)

#### Footer link
A quiet link in the footer columns. Measured, never followed. Read as `footer-link` on the anam.ai tools page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 112.44 x 18; background transparent; text Inter 15/18 400, rgba(255, 255, 255, 0.8); transition color 0.15s ease |
| hover | text Inter 15/18 400, #ffffff `white` |
| focus-visible | outline 1px auto #005fcc, offset 1px; text Inter 15/18 400, #ffffff `white` |

![Footer link default](components/crops/footer-link-default.png) ![Footer link hover](components/crops/footer-link-hover.png) ![Footer link focus-visible](components/crops/footer-link-focus-visible.png)

#### Submenu link
A row inside the open nav dropdown. Measured, never followed. Read as `nav-sub-link` on the anam.ai pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 102.02 x 19; background transparent; text Inter 15/22.5 400, #000000 `black` |
| focus-visible | outline 2px solid #ff6200 `brand.500`, offset 3px |

![Submenu link default](components/crops/nav-sub-link-default.png) ![Submenu link hover](components/crops/nav-sub-link-hover.png) ![Submenu link focus-visible](components/crops/nav-sub-link-focus-visible.png)

### Home

anam.ai's home: the Inter hero with the orange 'Meet our most expressive model' badge, the persona card carousel (each card a live avatar video with frosted-glass chips), the 'Talk with …' demo card with its call controls, and the sticky CTA band.

#### Hero title
"Create interactive avatars for…" — the display line the home page opens with (the last word rotates through personas). Read as `hero-title` on the anam.ai home page.

**Values (default).** size 1240 x 44; background transparent; text Inter 40/44 500, #000000 `black`.

![Hero title default](components/crops/hero-title-default.png)

#### Hero subline
Read as `hero-sub` on the anam.ai home page.

**Values (default).** size 353.47 x 27.59; background transparent; text Inter 13/15.6 500, #ff6200 `brand.500`.

Child layers that carry the look: a 353.5x27.6 background rgba(255, 98, 0, 0.05) `brand.tint` radius 40px; div 3x3 background #ff6200 `brand.500` radius 6px; div 3x3 background #ff6200 `brand.500` radius 6px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Hero CTA button
The primary button under the hero copy. Links to lab.anam.ai/register; measured, never followed. Read as `hero-cta` on the anam.ai home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: pressed) | size 128.02 x 34; padding 16px 24px; radius 50px; background #000000 `black`; text Inter 15/18 500, #ffffff `white` |
| hover | background rgba(0, 0, 0, 0.85); text Inter 15/18 500, rgba(255, 255, 255, 0.85) |
| focus-visible | outline 1px auto #005fcc, offset 1px |

![Hero CTA button default](components/crops/hero-cta-default.png) ![Hero CTA button hover](components/crops/hero-cta-hover.png) ![Hero CTA button focus-visible](components/crops/hero-cta-focus-visible.png) ![Hero CTA button pressed](components/crops/hero-cta-pressed.png)

#### Persona chip
One of the persona selector cards under the hero demo (Mia medical services, Anne skills training, Richard customer support, Liv sales, Gabriel language tutor). Pressed is forced; a real press only swaps the persona the demo card names. Read as `persona-chip` on the anam.ai home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 340 x 451; background transparent; text Inter 2/2.4 400, #000000 `black`; transition transform 0.3s cubic-bezier(0.12, 0.23, 0.5, 1); transform translate(160px, -225.5px) |
| hover | transform translate(1616px, -225.5px) |
| focus-visible | outline 1px auto #005fcc, offset 0px; transform translate(1616px, -225.5px) |
| pressed | transform translate(1616px, -225.5px) |

Child layers that carry the look: div 340x403 radius 32px shadow rgba(0, 0, 0, 0.01) 0px 124px 50px 0px, rgba(0, 0, 0, 0.05) 0px 70px 42px 0px, rgba(0, 0, 0, 0.09) 0px 31px 31px 0px, rgba(0, 0, 0, 0.1) 0px 8px 17px 0px; div 48x48 background rgba(255, 255, 255, 0.5) `glass.fill` radius 50px; div::after 48pxx48px border 2px solid rgba(255, 255, 255, 0.12) `glass.border` radius 50px.

![Persona chip default](components/crops/persona-chip-default.png) ![Persona chip hover](components/crops/persona-chip-hover.png) ![Persona chip focus-visible](components/crops/persona-chip-focus-visible.png) ![Persona chip pressed](components/crops/persona-chip-pressed.png)

#### Persona chip, selected
The same chip after a press, in its selected state (the demo card now names that persona). Read as `persona-chip-selected` on the anam.ai home page.

**Values (default).** size 340 x 451; background transparent; text Inter 2/2.4 400, #000000 `black`; transition transform 0.3s cubic-bezier(0.12, 0.23, 0.5, 1); transform translate(2742px, -225.5px).

Child layers that carry the look: div 408x483.6 radius 32px shadow rgba(0, 0, 0, 0.01) 0px 124px 50px 0px, rgba(0, 0, 0, 0.05) 0px 70px 42px 0px, rgba(0, 0, 0, 0.09) 0px 31px 31px 0px, rgba(0, 0, 0, 0.1) 0px 8px 17px 0px; div 57.6x57.6 background rgba(255, 255, 255, 0.5) `glass.fill` radius 50px; div::after 48pxx48px border 2px solid rgba(255, 255, 255, 0.12) `glass.border` radius 50px.

![Persona chip, selected default](components/crops/persona-chip-selected-default.png)

#### Avatar demo card
The "Talk with …" card under the hero: the avatar preview, the persona name and the call controls. The call button starts a live avatar session with microphone access, so it is measured inside the card and never pressed. Read as `demo-card` on the anam.ai home page.

**Values (default).** size 408 x 483.6; background transparent; text Inter 15/18 500, rgba(0, 0, 0, 0.7) `glass.dark-icon`.

Child layers that carry the look: div 408x483.6 radius 32px shadow rgba(0, 0, 0, 0.01) 0px 124px 50px 0px, rgba(0, 0, 0, 0.05) 0px 70px 42px 0px, rgba(0, 0, 0, 0.09) 0px 31px 31px 0px, rgba(0, 0, 0, 0.1) 0px 8px 17px 0px; div 57.6x57.6 background rgba(255, 255, 255, 0.5) `glass.fill` radius 50px; div::after 48pxx48px border 2px solid rgba(255, 255, 255, 0.12) `glass.border` radius 50px.

![Avatar demo card default](components/crops/demo-card-default.png)

#### Feature tab section
The scroll-driven tab showcase (TabSection): a tab per feature with a video or metric card beside it. Read as `tab-section` on the anam.ai home page.

**Values (default).** size 1280 x 765; padding 0px 20px 100px 20px; background transparent; text Inter 32/38.4 500, #000000 `black`.

Child layers that carry the look: a 143.8x34 background #000000 `black` radius 50px; div 2x95.8 background rgba(0, 0, 0, 0.12) radius 30px; div 2x6.2 background #ff6200 `brand.500` radius 99px.

![Feature tab section default](components/crops/tab-section-default.png)

#### Sticky CTA band
The "Build the future of customer experience. Today." band pinned at the foot of the page, with a Get started button. Read as `cta-band` on the anam.ai home page.

**Values (default).** size 700 x 163.59; background transparent; text Inter 48/52.8 500, #000000 `black`.

Child layers that carry the look: a 128x34 background #000000 `black` radius 50px.

![Sticky CTA band default](components/crops/cta-band-default.png)

#### Feature tab
A tab label inside the showcase. Measured, never pressed: the section advances on scroll. Read as `tab-item` on the anam.ai home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 372 x 28.8; background transparent; text Inter 24/28.8 500, #000000 `black` |

![Feature tab default](components/crops/tab-item-default.png) ![Feature tab hover](components/crops/tab-item-hover.png) ![Feature tab focus-visible](components/crops/tab-item-focus-visible.png)

#### Demo call button
The "Talk with <persona>" call control beside the demo card. Hovered and focused, never pressed: a press opens a session on Anam’s servers and asks for the microphone. Read as `demo-cta` on the anam.ai home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 184.58 x 48; padding 1px 18px; border 2px solid rgba(255, 255, 255, 0.12) `glass.border`; radius 50px; background rgba(255, 255, 255, 0.5) `glass.fill`; text Inter 15/normal 500, rgba(0, 0, 0, 0.7) `glass.dark-icon`; icon 24 x 24, rgba(0, 0, 0, 0.7) `glass.dark-icon` |
| hover | background rgba(255, 255, 255, 0.6) |
| focus-visible | outline 1px auto #005fcc, offset 0px |

![Demo call button default](components/crops/demo-cta-default.png) ![Demo call button hover](components/crops/demo-cta-hover.png) ![Demo call button focus-visible](components/crops/demo-cta-focus-visible.png)

### Feature sections

The scroll-driven sections further down the home page: the TabSection feature tabs (Human realism, Expression control, …), the benchmark feature card in IBM Plex Mono, and the logo cloud.

#### Feature card
A metrics/feature block from the latency or platform sections (a claim, its value and a diagram or video). Read as `feature-card` on the anam.ai home page.

**Values (default).** size 600 x 144; background transparent; text IBM Plex Mono 13/15.6 400, #000000 `black`.

![Feature card default](components/crops/feature-card-default.png)

#### Customer logo cloud
The customer logo strip that scrolls on a loop. Read as `logo-cloud` on the anam.ai home page.

**Values (default).** size 1280 x 82; padding 0px 20px; background transparent; text Inter 15/21 400, rgba(0, 0, 0, 0.5).

![Customer logo cloud default](components/crops/logo-cloud-default.png)

#### API page title
Read as `api-title` on the anam.ai API page.

**Values (default).** size 427 x 115.22; background transparent; text Inter 32/38.4 500, #ffffff `white`.

![API page title default](components/crops/api-title-default.png)

### Pricing

anam.ai/pricing, a Next.js page: the title, monthly/annual billing toggle, the plan cards (Free / Pro / Enterprise) and the FAQ list.

#### Pricing title
Read as `pricing-title` on the anam.ai pricing page.

**Values (default).** size 820 x 88; background transparent; text Inter 40/44 500, #000000 `black`.

![Pricing title default](components/crops/pricing-title-default.png)

#### Billing period toggle
The monthly/annual period switch above the plan cards. A local toggle; the capture presses it once on the screenshot pass. Read as `billing-toggle` on the anam.ai pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 92.33 x 40; padding 0px 18px; radius 50px; background transparent; text Inter 15/22.5 500, rgba(0, 0, 0, 0.68); transition background-color 0.2s ease, color 0.2s ease, box-shadow 0.2s ease |
| hover | text Inter 15/22.5 500, #000000 `black` |
| focus-visible | outline 2px solid #ff6200 `brand.500`, offset 3px |

![Billing period toggle default](components/crops/billing-toggle-default.png) ![Billing period toggle hover](components/crops/billing-toggle-hover.png) ![Billing period toggle focus-visible](components/crops/billing-toggle-focus-visible.png)

#### Plan card
A pricing plan card: name, price, included usage and a call-to-action button. Read as `plan-card` on the anam.ai pricing page.

**Values (default).** size 520 x 1133.19; background transparent; text Inter 32/38.4 500, #000000 `black`.

Child layers that carry the look: a 94.1x44 background #000000 `black` radius 50px; a 137.8x44 background #f5f5f5 `gray.100` radius 50px.

![Plan card default](components/crops/plan-card-default.png)

#### Plan CTA button
The call-to-action inside a plan card. Pressed is forced; a real press leads to checkout on lab.anam.ai. Read as `plan-cta` on the anam.ai pricing page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 137.81 x 44; padding 12px 20px; radius 50px; background #f5f5f5 `gray.100`; text Inter 15/18 500, #000000 `black`; transition background-color 0.2s ease, color 0.2s ease, transform 0.16s ease |
| hover | background #e8e6e6 |
| focus-visible | outline 2px solid #ff6200 `brand.500`, offset 3px |
| pressed | size 133.68 x 42.68; background #e8e6e6; transform scale(0.97) |

![Plan CTA button default](components/crops/plan-cta-default.png) ![Plan CTA button hover](components/crops/plan-cta-hover.png) ![Plan CTA button focus-visible](components/crops/plan-cta-focus-visible.png) ![Plan CTA button pressed](components/crops/plan-cta-pressed.png)

#### FAQ item
A question-and-answer row in the pricing FAQ. Read as `faq-item` on the anam.ai pricing page.

**Values (default).** size 728 x 57; border B: 1px solid rgba(0, 0, 0, 0.08); background transparent; text Inter 15/22.5 500, #000000 `black`.

Child layers that carry the look: details 728x57 border 1px solid rgba(0, 0, 0, 0.08); summary::before 12pxx1.5px background #ff6200 `brand.500`; summary::after 12pxx1.5px background #ff6200 `brand.500`.

![FAQ item default](components/crops/faq-item-default.png)

### Demo request form

anam.ai/get-demo, a Next.js page: the 420px sales form — work email, company, use case — measured in default, focused and filled states. Nothing was submitted.

#### Demo page title
Read as `demo-title` on the anam.ai Get a demo page.

**Values (default).** size 420 x 41.8; background transparent; text Inter 38/41.8 500, #0a0a0a `ink.DEFAULT`.

![Demo page title default](components/crops/demo-title-default.png)

#### Demo request form
The get-demo lead form: name, work email and a message box plus a submit. Every field was measured; nothing was filled or sent. Read as `demo-form` on the anam.ai Get a demo page.

**Values (default).** size 420 x 426; background transparent; text Inter 13.5/20.25 500, #0a0a0a `ink.DEFAULT`.

Child layers that carry the look: input 420x46.5 background #f5f5f5 `gray.100` radius 11px; input 420x46.5 background #f5f5f5 `gray.100` radius 11px; button 420x46.5 background #f5f5f5 `gray.100` image url(data:…) radius 11px.

![Demo request form default](components/crops/demo-form-default.png)

#### Field label
Read as `form-label` on the anam.ai Get a demo page.

**Values (default).** size 420 x 20.25; background transparent; text Inter 13.5/20.25 500, #0a0a0a `ink.DEFAULT`.

![Field label default](components/crops/form-label-default.png)

#### Text field
A text input in the demo form. Sample text was typed and deleted; nothing was submitted. Read as `form-input` on the anam.ai Get a demo page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 420 x 46.5; padding 12px 14px; radius 11px; background #f5f5f5 `gray.100`; text Inter 15/22.5 400, #0a0a0a `ink.DEFAULT`; transition background 0.15s ease, box-shadow 0.15s ease; placeholder #0a0a0a `ink.DEFAULT` |
| focused, filled | background #efefef; shadow rgba(255, 98, 0, 0.4) 0px 0px 0px 2px |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Text field box
Read as `form-input-box` on the anam.ai Get a demo page.

**Values (default).** size 420 x 72.75; background transparent; text Inter 13.5/20.25 500, #0a0a0a `ink.DEFAULT`.

Child layers that carry the look: input 420x46.5 background #f5f5f5 `gray.100` radius 11px.

![Text field box default](components/crops/form-input-box-default.png)

#### Text area
The message box. Clicked into, never filled. Read as `form-textarea` on the anam.ai Get a demo page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 420 x 69; padding 12px 14px; radius 11px; background #f5f5f5 `gray.100`; text Inter 15/22.5 400, #0a0a0a `ink.DEFAULT`; transition background 0.15s ease, box-shadow 0.15s ease; placeholder #0a0a0a `ink.DEFAULT` |
| focused | background #efefef; shadow rgba(255, 98, 0, 0.4) 0px 0px 0px 2px |

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Submit button
The form’s submit. Measured and hovered, never pressed: a press sends the lead form. Read as `form-submit` on the anam.ai Get a demo page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 420 x 52.5; padding 15px 24px; radius 50px; background #ff6200 `brand.500`; text Inter 15/22.5 500, #ffffff `white`; transition transform 0.04s ease, opacity 0.15s ease, background 0.15s ease |
| hover | background #ff8133 `brand.600` |
| focus-visible | outline 1px auto #005fcc, offset 0px |

![Submit button default](components/crops/form-submit-default.png) ![Submit button hover](components/crops/form-submit-hover.png) ![Submit button focus-visible](components/crops/form-submit-focus-visible.png)

### Docs (Mintlify)

anam.ai/docs, a Mintlify site: the top tabs, search pill, Ask Assistant button, warm-stone sidebar and TOC rails, link cards, code and method badges. The ⌘K dialog and ⌘I panel were opened by keyboard, never submitted; the dark theme was toggled once.

#### Docs sidebar
The left navigation tree on the Mintlify docs (section groups, page links, POST/GET method badges on the API reference). Read as `docs-sidebar` on the anam.ai docs (API reference) page.

**Values (default).** size 288 x 788; background transparent; text Inter 14/24 600, #1e1916 `neutral.900`.

Child layers that carry the look: div 256x32 image linear-gradient(in oklab, #ffffff `white` 0%, transparent 100%); a 256x36 background rgba(255, 98, 0, 0.1) `brand.tint-strong` radius 12px; span 32.1x15 background rgba(96, 165, 250, 0.2) radius 6px.

![Docs sidebar default](components/crops/docs-sidebar-default.png)

#### Sidebar link
A page link inside a sidebar group. Measured, never followed. Read as `docs-nav-link` on the anam.ai docs (API reference) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 256 x 24; padding 0px 0px 0px 16px; background transparent; text Inter 14/24 600, #1e1916 `neutral.900` |

![Sidebar link default](components/crops/docs-nav-link-default.png) ![Sidebar link hover](components/crops/docs-nav-link-hover.png)

#### Sidebar link, current page
The link for the open page, in its selected style. Read as `docs-nav-active` on the anam.ai docs (API reference) page.

**Values (default).** size 256 x 36; background transparent; text Inter 14/24 400, #ff6200 `brand.500`.

Child layers that carry the look: a 256x36 background rgba(255, 98, 0, 0.1) `brand.tint-strong` radius 12px.

![Sidebar link, current page default](components/crops/docs-nav-active-default.png)

#### Top nav tab
A section tab in the docs top bar (Documentation / API Reference). Read as `docs-topnav-link` on the anam.ai docs (API reference) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 63.53 x 48; background transparent; text Inter 14/20 500, #57524f `neutral.600` |
| hover | text Inter 14/20 500, #2d2825 `neutral.800` |
| focus-visible | outline 1px auto #ff6200 `brand.500`, offset 1px |

![Top nav tab default](components/crops/docs-topnav-link-default.png) ![Top nav tab hover](components/crops/docs-topnav-link-hover.png) ![Top nav tab focus-visible](components/crops/docs-topnav-link-focus-visible.png)

#### Search button
The "Search… ⌘K" pill in the docs bar. Pressed is forced; a real press opens the search dialog. Read as `docs-search-btn` on the anam.ai docs (API reference) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 269.56 x 36; padding 0px 12px 0px 14px; radius 12px; background #ffffff `white`; shadow rgba(166, 161, 158, 0.3) 0px 0px 0px 1px; text Inter 14/24 400, #77726f `neutral.500`; icon 16 x 16, #46413e `neutral.700` |
| hover | shadow rgba(87, 82, 79, 0.3) 0px 0px 0px 1px; icon 16 x 16, #2d2825 `neutral.800` |
| focus-visible | outline 1px auto #ff6200 `brand.500`, offset 0px |
| pressed | shadow rgba(87, 82, 79, 0.3) 0px 0px 0px 1px; icon 16 x 16, #2d2825 `neutral.800` |

![Search button default](components/crops/docs-search-btn-default.png) ![Search button hover](components/crops/docs-search-btn-hover.png) ![Search button focus-visible](components/crops/docs-search-btn-focus-visible.png) ![Search button pressed](components/crops/docs-search-btn-pressed.png)

#### Ask Assistant button
Opens the AI assistant panel (⌘I). Pressed is forced; the panel was opened by keyboard for its own entry. Read as `docs-assistant-btn` on the anam.ai docs (API reference) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 157.77 x 36; padding 0px 14px 0px 12px; radius 12px; background #ffffff `white`; shadow rgba(166, 161, 158, 0.3) 0px 0px 0px 1px; text Inter 14/20 400, #77726f `neutral.500`; icon 16 x 16, #46413e `neutral.700` |
| hover | shadow rgba(87, 82, 79, 0.3) 0px 0px 0px 1px; icon 16 x 16, #2d2825 `neutral.800` |
| focus-visible | outline 1px auto #ff6200 `brand.500`, offset 0px |
| pressed | shadow rgba(87, 82, 79, 0.3) 0px 0px 0px 1px; icon 16 x 16, #2d2825 `neutral.800` |

![Ask Assistant button default](components/crops/docs-assistant-btn-default.png) ![Ask Assistant button hover](components/crops/docs-assistant-btn-hover.png) ![Ask Assistant button focus-visible](components/crops/docs-assistant-btn-focus-visible.png) ![Ask Assistant button pressed](components/crops/docs-assistant-btn-pressed.png)

#### Theme menu button
The "Change theme preference" menu trigger. A local toggle; the dark run pressed it once. Read as `docs-theme-btn` on the anam.ai docs (API reference) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 32 x 32; padding 8px; radius 8px; background transparent; text Inter 14/20 400, rgba(17, 13, 10, 0.5) |
| focus-visible | outline 1px auto #ff6200 `brand.500`, offset 0px |

![Theme menu button default](components/crops/docs-theme-btn-default.png) ![Theme menu button hover](components/crops/docs-theme-btn-hover.png) ![Theme menu button focus-visible](components/crops/docs-theme-btn-focus-visible.png)

#### On-this-page rail
The sticky right-hand table of contents. Read as `docs-toc` on the anam.ai docs (API reference) page.

**Values (default).** size 304 x 748; background transparent; text Inter 14/24 500, #46413e `neutral.700`; icon 12 x 12, #46413e `neutral.700`.

![On-this-page rail default](components/crops/docs-toc-default.png)

#### TOC link
Read as `docs-toc-link` on the anam.ai docs (API reference) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 264 x 32; background transparent; text Inter 14/24 400, #ff6200 `brand.500` |

![TOC link default](components/crops/docs-toc-link-default.png) ![TOC link hover](components/crops/docs-toc-link-hover.png)

#### Docs page title
"Anam Documentation" in the docs display type. Read as `docs-h1` on the anam.ai docs (overview) page.

**Values (default).** size 360.47 x 40; background transparent; text Inter 36/40 600, #1e1916 `neutral.900`.

![Docs page title default](components/crops/docs-h1-default.png)

#### Body text
Read as `docs-body` on the anam.ai docs (overview) page.

**Values (default).** size 688.81 x 56; background transparent; text Inter 18/28 400, #46413e `neutral.700`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Docs link card
A card linking to another docs page (the "Learn" cards). Measured, never followed. Read as `docs-card` on the anam.ai docs (overview) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 218.94 x 230; border 1px solid rgba(17, 13, 10, 0.1); radius 16px; background #ffffff `white`; text Inter 16/24 600, #2d2825 `neutral.800` |
| hover | border 1px solid #ff6200 `brand.500` |
| focus-visible | outline 1px auto #ff6200 `brand.500`, offset 0px |
| pressed | border 1px solid #ff6200 `brand.500` |

![Docs link card default](components/crops/docs-card-default.png) ![Docs link card hover](components/crops/docs-card-hover.png) ![Docs link card focus-visible](components/crops/docs-card-focus-visible.png) ![Docs link card pressed](components/crops/docs-card-pressed.png)

#### Breadcrumb
The section/page breadcrumb over the title. Read as `docs-breadcrumb` on the anam.ai docs (overview) page.

Not on the page when it was captured.

#### API reference title
"Anam REST API". Read as `docs-api-title` on the anam.ai docs (API reference) page.

**Values (default).** size 259.33 x 40; background transparent; text Inter 36/40 600, #1e1916 `neutral.900`.

![API reference title default](components/crops/docs-api-title-default.png)

#### Code block
A fenced code sample (the base URL block, a curl example), mono-set over a tinted panel. Read as `docs-code-block` on the anam.ai docs (API reference) page.

**Values (default).** size 654.81 x 24; background transparent; shadow rgba(59, 130, 246, 0.5) 0px 0px 0px 0px; text Paper Mono 14/24 400, #1f2328.

![Code block default](components/crops/docs-code-block-default.png)

#### Inline code
Read as `docs-inline-code` on the anam.ai docs (API reference) page.

**Values (default).** size 126.3 x 20; padding 2px 8px; radius 6px; background rgba(245, 241, 238, 0.5); text Paper Mono 14/21 500, oklch(0.21 0.034 264.665).

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Method badge
The POST/GET verb chip beside an API endpoint in the sidebar. Read as `docs-method-badge` on the anam.ai docs (API reference) page.

**Values (default).** size 32 x 24; background transparent; text Inter 8.8/11 700, #1d4ed8 `method-blue`.

Child layers that carry the look: span 32.1x15 background rgba(96, 165, 250, 0.2) radius 6px.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Docs page, dark
The content column in the dark theme. Read as `docs-dark-main` on the anam.ai docs, dark theme page.

**Values (default).** size 1088 x 1936.55; background transparent; text Inter 14/24 500, #d5d1ce `neutral.300`; icon 12 x 12, #d5d1ce `neutral.300`.

Child layers that carry the look: button 140x34 background #000000 `black` border 1px solid rgba(255, 255, 255, 0.07) radius 12px 0px 0px 12px; button 34x34 background #000000 `black` border 1px solid rgba(255, 255, 255, 0.07) radius 0px 12px 12px 0px; button 0x0 background #000000 `black` border 1px solid rgba(255, 255, 255, 0.07) radius 12px 0px 0px 12px.

![Docs page, dark default](components/crops/docs-dark-main-default.png)

#### Sidebar, dark
Read as `docs-dark-sidebar` on the anam.ai docs, dark theme page.

**Values (default).** size 288 x 788; background transparent; text Inter 14/24 600, #e6e1de `neutral.200`; icon 16 x 16, #ff6200 `brand.500`.

Child layers that carry the look: div 256x32 image linear-gradient(in oklab, #000000 `black` 0%, transparent 100%); a 256x36 background rgba(255, 98, 0, 0.1) `brand.tint-strong` radius 12px; svg 16x16 background #ff6200 `brand.500`.

![Sidebar, dark default](components/crops/docs-dark-sidebar-default.png)

#### Docs title, dark
Read as `docs-dark-h1` on the anam.ai docs, dark theme page.

**Values (default).** size 360.47 x 40; background transparent; text Inter 36/40 600, #e6e1de `neutral.200`.

![Docs title, dark default](components/crops/docs-dark-h1-default.png)

#### Prev/next link
The page-footer pagination link. Measured, never followed. Read as `docs-prev-next` on the anam.ai docs (API reference) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 154.95 x 20; radius 2px; background transparent; text Inter 14/20 600, #46413e `neutral.700`; icon 3 x 6, #46413e `neutral.700` |
| hover | text Inter 14/20 600, #1e1916 `neutral.900` |
| focus-visible | outline 2px solid #ff6200 `brand.500`, offset 2px |

![Prev/next link default](components/crops/docs-prev-next-default.png) ![Prev/next link hover](components/crops/docs-prev-next-hover.png) ![Prev/next link focus-visible](components/crops/docs-prev-next-focus-visible.png)

#### Docs card, dark
Read as `docs-dark-card` on the anam.ai docs, dark theme page.

**Values (default).** size 218.94 x 230; border 1px solid rgba(255, 255, 255, 0.1); radius 16px; background #000000 `black`; text Inter 16/24 600, #ffffff `white`.

![Docs card, dark default](components/crops/docs-dark-card-default.png)

### Cards and lists

The card grids on the secondary pages: avatar cards on /interactive-avatars, team cards on /about, paper entries on /research, customer stories on /case-studies, post cards on /blog, release entries on /changelog and tool cards on /tools.

#### Avatar card title
Read as `avatar-card-title` on the anam.ai interactive avatars page.

**Values (default).** size 640 x 88; background transparent; text Inter 40/44 500, #000000 `black`.

![Avatar card title default](components/crops/avatar-card-title-default.png)

#### About card title
Read as `about-card-title` on the anam.ai about page.

**Values (default).** size 451.88 x 88; background transparent; text Inter 40/44 500, #000000 `black`.

![About card title default](components/crops/about-card-title-default.png)

#### Research entry title
Read as `research-card-title` on the anam.ai research page.

**Values (default).** size 390 x 88; background transparent; text Inter 40/44 500, #000000 `black`.

![Research entry title default](components/crops/research-card-title-default.png)

#### Case study card title
Read as `case-card-title` on the anam.ai case studies page.

**Values (default).** size 380 x 88; background transparent; text Inter 40/44 500, #000000 `black`.

![Case study card title default](components/crops/case-card-title-default.png)

#### Blog post card title
Read as `post-card-title` on the anam.ai blog page.

**Values (default).** size 208.53 x 38.41; background transparent; text Inter 32/38.4 500, #000000 `black`.

![Blog post card title default](components/crops/post-card-title-default.png)

#### Changelog entry title
Read as `changelog-entry-title` on the anam.ai changelog page.

**Values (default).** size 535 x 44; background transparent; text Inter 40/44 500, #000000 `black`.

![Changelog entry title default](components/crops/changelog-entry-title-default.png)

#### Tool card title
Read as `tool-card-title` on the anam.ai tools page.

**Values (default).** size 417.59 x 44; background transparent; text Inter 40/44 500, #000000 `black`.

![Tool card title default](components/crops/tool-card-title-default.png)

#### Avatar card
A card in the avatar gallery: a face, its style tag and name. Read as `avatar-card` on the anam.ai interactive avatars page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 222 x 128.91; background transparent; text Inter 13/16.9 500, rgba(0, 0, 0, 0.5) |

![Avatar card default](components/crops/avatar-card-default.png) ![Avatar card hover](components/crops/avatar-card-hover.png) ![Avatar card focus-visible](components/crops/avatar-card-focus-visible.png)

#### About card
A card on the team/company page. Read as `about-card` on the anam.ai about page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 222 x 128.91; background transparent; text Inter 13/16.9 500, rgba(0, 0, 0, 0.5) |

![About card default](components/crops/about-card-default.png) ![About card hover](components/crops/about-card-hover.png) ![About card focus-visible](components/crops/about-card-focus-visible.png)

#### Research entry
A paper or model entry on the research page. Read as `research-card` on the anam.ai research page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 222 x 128.91; background transparent; text Inter 13/16.9 500, rgba(0, 0, 0, 0.5) |

![Research entry default](components/crops/research-card-default.png) ![Research entry hover](components/crops/research-card-hover.png) ![Research entry focus-visible](components/crops/research-card-focus-visible.png)

#### Case study card
A customer story card. Read as `case-card` on the anam.ai case studies page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 222 x 128.91; background transparent; text Inter 13/16.9 500, rgba(0, 0, 0, 0.5) |

![Case study card default](components/crops/case-card-default.png) ![Case study card hover](components/crops/case-card-hover.png) ![Case study card focus-visible](components/crops/case-card-focus-visible.png)

#### Blog post card
A post card in the blog index. Read as `post-card` on the anam.ai blog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 222 x 128.91; background transparent; text Inter 13/16.9 500, rgba(0, 0, 0, 0.5) |

![Blog post card default](components/crops/post-card-default.png) ![Blog post card hover](components/crops/post-card-hover.png) ![Blog post card focus-visible](components/crops/post-card-focus-visible.png)

#### Changelog entry
A release entry on the changelog page. Read as `changelog-entry` on the anam.ai changelog page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover, focus-visible) | size 222 x 128.91; background transparent; text Inter 13/16.9 500, rgba(0, 0, 0, 0.5) |

![Changelog entry default](components/crops/changelog-entry-default.png) ![Changelog entry hover](components/crops/changelog-entry-hover.png) ![Changelog entry focus-visible](components/crops/changelog-entry-focus-visible.png)

#### Tool card
A card in the tools index. Read as `tool-card` on the anam.ai tools page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 598 x 506.5; padding 30px; radius 32px; background #fafafa; text Inter 10/10 600, #000000 `black`; transition background-color 0.4s cubic-bezier(0.44, 0, 0.56, 1), transform 0.4s cubic-bezier(0.44, 0, 0.56, 1) |
| hover | background #f5f5f5 `gray.100`; transform translate(0px, -2px) |
| focus-visible | outline 2px solid #ff6200 `brand.500`, offset 4px |

![Tool card default](components/crops/tool-card-default.png) ![Tool card hover](components/crops/tool-card-hover.png) ![Tool card focus-visible](components/crops/tool-card-focus-visible.png)

### Panels and dialogs

The overlays a fresh profile meets: the cookie consent card (photographed and measured, then hidden without a click — a consent choice is a submission), the docs ⌘K search dialog and the ⌘I assistant sheet.

#### Cookie consent card
The .anam-cc-card consent card pinned bottom-right on a fresh profile (Manage cookies / Reject all / Accept all). Photographed and measured in place, then hidden without a click: a consent choice is a submission. Read as `consent-card` on the anam.ai home page.

**Values (default).** size 420 x 180; padding 20px; border 1px solid rgba(0, 0, 0, 0.08); radius 16px; background #ffffff `white`; shadow rgba(0, 0, 0, 0.18) 0px 12px 32px -8px, rgba(0, 0, 0, 0.06) 0px 1px 2px 0px; text Inter 15/21 400, rgba(0, 0, 0, 0.62).

![Cookie consent card default](components/crops/consent-card-default.png)

#### Manage cookies button
The text button in the consent card. Measured and focused, never pressed. Read as `consent-manage` on the anam.ai home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 119.69 x 38; border 1px solid transparent; radius 999px; background transparent; text Inter 15/15 500, #000000 `black`; transition background-color 0.16s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.16s ease |
| focus-visible | outline 2px solid #000000 `black`, offset 2px |

![Manage cookies button default](components/crops/consent-manage-default.png) ![Manage cookies button hover](components/crops/consent-manage-hover.png) ![Manage cookies button focus-visible](components/crops/consent-manage-focus-visible.png)

#### Accept all button
The filled choice button in the consent card. Measured and focused, never pressed: accepting is a submission. Read as `consent-accept` on the anam.ai home page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default | size 109.11 x 38; padding 0px 18px; border 1px solid transparent; radius 999px; background #f5f5f5 `gray.100`; text Inter 15/15 500, #000000 `black`; transition background-color 0.16s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.16s ease |
| hover | background #ebebeb |
| focus-visible | outline 2px solid #000000 `black`, offset 2px |

![Accept all button default](components/crops/consent-accept-default.png) ![Accept all button hover](components/crops/consent-accept-hover.png) ![Accept all button focus-visible](components/crops/consent-accept-focus-visible.png)

#### Search dialog
The ⌘K search overlay: a field, result list and keyboard hints. Opened by keyboard; nothing was typed. Read as `docs-search-dialog` on the anam.ai docs (overview) page.

**Values (default).** size 640 x 62; radius 20px; background #ffffff `white`; shadow rgba(17, 13, 10, 0.06) 0px 0px 0px 1px, rgba(0, 0, 0, 0.01) 0px 57px 34px 0px, rgba(0, 0, 0, 0.02) 0px 25px 25px 0px, rgba(0, 0, 0, 0.02) 0px 6px 14px 0px; text Inter 14/20 500, #77726f `neutral.500`; transition transform 0.25s cubic-bezier(0.22, 1, 0.36, 1), scale 0.25s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.25s cubic-bezier(0.22, 1, 0.36, 1); icon 16 x 16, #77726f `neutral.500`.

![Search dialog default](components/crops/docs-search-dialog-default.png)

#### Search field
Read as `docs-search-input` on the anam.ai docs (overview) page.

**Values (default).** size 460.34 x 36; padding 0px 0px 0px 30px; background transparent; text Inter 16/24 500, #110d0a `neutral.950`; placeholder #a6a19e `neutral.400`.

No crop was saved for this entry (a whole page or a hidden element); the values are from the computed styles.

#### Assistant panel
The "Ask Assistant" sheet with a question box and send button. Opened by keyboard; nothing was typed or sent. Read as `docs-assistant-panel` on the anam.ai docs (overview) page.

**Values (default).** size 368 x 900; background #ffffff `white`; text Inter 16/24 500, #1e1916 `neutral.900`; icon 20 x 20, #ff6200 `brand.500`.

![Assistant panel default](components/crops/docs-assistant-panel-default.png)

#### Assistant send button
The send control in the assistant sheet. Measured, never pressed. Read as `docs-assistant-send` on the anam.ai docs (overview) page.

| State | Values (later rows list only what changes from the first row) |
|---|---|
| default (same: hover) | size 24 x 24; padding 4px; radius 9999px; background rgba(255, 98, 0, 0.3); text Inter 16/24 400, #77726f `neutral.500`; icon 10 x 10, #ffffff `white` |

![Assistant send button default](components/crops/docs-assistant-send-default.png) ![Assistant send button hover](components/crops/docs-assistant-send-hover.png)

### Mobile (390 wide)

The same pages as a phone draws them, at 390 x 844 with an iPhone user agent: the nav collapses to a menu button and the persona carousel scrolls horizontally.

#### Mobile nav bar
The top bar at 390 wide: logo, Sign in and the menu button. Read as `m-nav-bar` on the anam.ai home page at 390 wide.

**Values (default).** size 390 x 75; background transparent; text Inter 15/18 500, #000000 `black`.

Child layers that carry the look: div 390x75 background rgba(255, 255, 255, 0); div 60x22 background #000000 `black`; a 96.6x34 background #f5f5f5 `gray.100` radius 50px.

![Mobile nav bar default](components/crops/m-nav-bar-default.png)

#### Hero title (mobile)
Read as `m-hero-title` on the anam.ai home page at 390 wide.

**Values (default).** size 350 x 88; background transparent; text Inter 40/44 500, #000000 `black`.

![Hero title (mobile) default](components/crops/m-hero-title-default.png)

#### Persona chip (mobile)
Read as `m-persona-chip` on the anam.ai home page at 390 wide.

**Values (default).** size 340 x 451; background transparent; text Inter 2/2.4 400, #000000 `black`; transition transform 0.3s cubic-bezier(0.12, 0.23, 0.5, 1); transform translate(-170px, -225.5px).

Child layers that carry the look: div 340x403 radius 32px shadow rgba(0, 0, 0, 0.01) 0px 124px 50px 0px, rgba(0, 0, 0, 0.05) 0px 70px 42px 0px, rgba(0, 0, 0, 0.09) 0px 31px 31px 0px, rgba(0, 0, 0, 0.1) 0px 8px 17px 0px.

![Persona chip (mobile) default](components/crops/m-persona-chip-default.png)

#### Docs top bar (mobile)
Read as `m-docs-topbar` on the anam.ai docs (overview) page at 390 wide.

**Values (default).** size 390 x 120; background transparent; text Inter 14/24 400, #77726f `neutral.500`.

Child layers that carry the look: div 390x120 background #ffffff `white` border 1px solid rgba(119, 114, 111, 0.05); div 358x64 border 1px solid rgba(119, 114, 111, 0.05); button 0x0 background #ffffff `white` radius 12px shadow transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, transparent 0px 0px 0px 0px, rgba(166, 161, 158, 0.3) 0px 0px 0px 1px, transparent 0px 0px 0px 0px.

![Docs top bar (mobile) default](components/crops/m-docs-topbar-default.png)

## Gaps

### Pages

- **The product app.** lab.anam.ai (/build, /login, /register) is the signed surface: nothing behind Sign in or Get started was captured, and the persona builder, API keys and session UI are all missing. The kit never signs in or registers.
- **A live avatar session.** The 'Talk with …' button opens a WebRTC session on Anam's servers and asks for the microphone; the control was measured and hovered, never pressed, so the in-call UI is missing.
- **Checkout and account.** The plan CTAs lead to checkout/registration; no purchase was made and no card field was filled.
- **Article-depth pages.** The index pages were captured; the blog's posts, the case studies' stories and the guides were not opened.

### States

- **Pressed** was forced with DevTools on the safe controls, so a state a script adds on mousedown (if any) is missing; call, consent, search-send and submit controls were never pressed at all.
- **The hero title's last word rotates** through personas and the carousel re-renders its cards as it autoplays; a capture pins whichever pass was running.
- **The persona cards are live videos** (and the demo card can hold a running avatar), so a crop shows one frame of a moving face.
- **Disabled, loading and error** were not seen on any public control.

### Themes

Only the docs ship a dark theme: `.dark` on html via the theme menu (measured in the docs-dark pass). The marketing pages and the /pricing, /get-demo, /tools apps declare no dark values and did not change under prefers-color-scheme (`themeChecks` in [raw/css-vars.json](raw/css-vars.json)), so the token file's `dark` set is the docs' theme only.

### Fonts

- **Inter** is the UI face everywhere (self-hosted on the marketing pages, `--font-inter` on docs). **IBM Plex Mono** (400/500) covers code and metrics on the marketing pages; the docs code is **Paper Mono** (Mintlify's face).
- **MD Thermochrome 0.4 Trial** — a licensed trial face — is loaded on the home page for display accents. It is not redistributable; substitute a close free face when reproducing the style.

### Screenshots

- Avatar faces, customer logos, blog artwork and the cookie banner are Anam's content and appear only inside screenshots and crops.
- Screenshots are stored as 256-colour PNGs; read exact colours from the tokens or the raw files.

### Content left out

- The docs' prose was not transcribed into the package; the components around it were measured.
- No personal data was captured: the pages were read signed out.

