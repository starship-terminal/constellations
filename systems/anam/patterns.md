# Anam patterns

How Anam's components combine to do the recurring jobs on its public pages, written from the captures of 2026-11-09 (signed out, 1440 and 390 wide, headless Chromium). Each pattern says when Anam uses it, the components it is built from (entries in [components.md](components.md), values in [tokens.json](tokens.json)), the layout, and the screens that show it. These are observations of what the product does, not Anam's own guidance.

anam.ai is three surfaces with one accent, and this file keeps them apart: **marketing** patterns come first (the pill nav, the avatar carousel, the demo call, the feature sections), then the **app pages** (pricing, the demo form, tools), then the **docs** (the Mintlify chrome, search, assistant, dark theme).

| Pattern | Captured | Example screen |
|---|---|---|
| [Marketing shell and navigation](#marketing-shell-and-navigation) | yes | [home-light-default](screenshots/home-light-default.png) |
| [The avatar carousel](#the-avatar-carousel) | yes | [home-light-persona-tab](screenshots/home-light-persona-tab.png) |
| [Talking to an avatar](#talking-to-an-avatar) | control only, never pressed | [home-light-default](screenshots/home-light-default.png) |
| [Scroll-driven feature sections](#scroll-driven-feature-sections) | yes | [home-light-full](screenshots/home-light-full.png) |
| [Pricing and plans](#pricing-and-plans) | yes, checkout excluded | [pricing-light-default](screenshots/pricing-light-default.png) |
| [Asking for a demo](#asking-for-a-demo) | yes, never submitted | [get-demo-light-field-focused](screenshots/get-demo-light-field-focused.png) |
| [Docs chrome, search and assistant](#docs-chrome-search-and-assistant) | yes | [docs-overview-light-default](screenshots/docs-overview-light-default.png) |
| [Docs dark theme](#docs-dark-theme) | yes | [docs-dark-dark-default](screenshots/docs-dark-dark-default.png) |
| [Consent](#consent) | yes, never answered | [home-light-consent](screenshots/home-light-consent.png) |
| [Empty, loading and error states](#empty-loading-and-error-states) | not seen | — |

## Marketing shell and navigation

**When.** Every Framer page: home, api, interactive-avatars, about, research, case-studies, blog, changelog.

**Components.** [Top navigation bar](components.md#top-navigation-bar), [Nav link](components.md#nav-link), [Sign in link](components.md#sign-in-link), [Nav submenu](components.md#nav-submenu) and [Submenu link](components.md#submenu-link), [Footer](components.md#footer) and [Footer link](components.md#footer-link).

**Layout.** A floating 100px band at the page top: the Anam mark (a black rounded square with the orange wedge), text links at Inter 14/16.8 500 (Developers, Pricing, Resources, Company), then a gray `radius.pill` 50px Sign in and a black Get started pill. Hover on a section opens a small dropdown (`nav-submenu` 222x129) of secondary links in dimmed 13/16.9 text. There is no border and no fill on the bar — it floats over the white page.

The footer inverts the palette: a `radius.2xl` 32px **black** panel spanning the content column (1400x1154 measured), link columns in `text.inverse-dim` 15/18 (white at .5-.8), the legal row inside it. It is the marketing site's one dark surface.

At 390 wide the nav collapses to the mark plus a menu button (`m-nav-bar` 390x75; [mobile-home-light-nav-open](screenshots/mobile-home-light-nav-open.png)).

**Screens.** [home-light-default](screenshots/home-light-default.png), [home-light-nav-submenu](screenshots/home-light-nav-submenu.png), [api-light-default](screenshots/api-light-default.png), [mobile-home-light-default](screenshots/mobile-home-light-default.png).

## The avatar carousel

**When.** The home hero's product demonstration — the first thing under the title.

**Components.** [Hero title](components.md#hero-title), [Hero subline](components.md#hero-subline) (the `accent-tint` badge "Meet our most expressive model"), [Hero CTA button](components.md#hero-cta-button), [Persona chip](components.md#persona-chip), [Persona chip, selected](components.md#persona-chip-selected).

**Layout.** The h1 (Inter 40/44 500, tracking `font.tracking.tight` -0.8px) rotates its last word through personas. Under it a strip of persona cards — measured `persona-chip` 340x451, the centred selected card 408x483.6 — each a **live avatar video** in a `radius.2xl` 32px frame with `shadow.persona-card`, the long four-layer soft shadow reaching 124px down. On the video sit the frosted chips: a `color.glass.fill` 48px circle with a 2px `color.glass.border` ring for the call chip and `color.glass.dark-icon` icon wells, then the persona name in 24px and a mono `tag` (sales, customer-support, medical-services…).

**Behaviour.** The carousel keeps parked copies of every card off-screen and re-renders on its own clock; the measurement re-resolves the live card per state for that reason. A click brings a parked card to the centre — the only click-state on the page.

**Screens.** [home-light-default](screenshots/home-light-default.png), [home-light-persona-tab](screenshots/home-light-persona-tab.png), [mobile-home-light-default](screenshots/mobile-home-light-default.png).

## Talking to an avatar

**When.** The page's central demo: a live call with a persona, one click away.

**Components.** [Avatar demo card](components.md#avatar-demo-card), [Demo call button](components.md#demo-call-button).

**Layout.** The selected persona's card carries the call row beside it: a `radius.pill` `color.glass.fill` 48px-tall "Talk with …" control (measured 184.58x48, `button.glass-bg` / `button.glass-text`) and a matching 48px unmute disc. Hovering and focusing were captured; **pressing was not** — a press opens a WebRTC session on Anam's servers and asks for the microphone.

**Screens.** [home-light-default](screenshots/home-light-default.png), [persona-tab](screenshots/home-light-persona-tab.png).

## Scroll-driven feature sections

**When.** The sections between hero and footer: feature tabs, benchmark, social proof.

**Components.** [Feature tab section](components.md#feature-tab-section), [Feature tab](components.md#feature-tab), [Feature card](components.md#feature-card), [Customer logo cloud](components.md#customer-logo-cloud), [Sticky CTA band](components.md#sticky-cta-band).

**Layout.** TabSection (1280x765) is a scroll-driven showcase: 24px tab labels (Human realism, Expression control, …) whose active item fills as you scroll, beside a video/metric card. The feature card pairs an Inter claim with `IBM Plex Mono` metrics (the latency benchmark numbers). The logo cloud is a quiet 1280x82 row of customer marks under a 15/21 `text-tertiary` line ("Trusted by over 8,000 builders"). The sticky CTA band ("Build the future of customer experience. Today.", Inter 48/52.8) parks at the foot of the page at 700 wide with the same black Get started pill.

**Screens.** [home-light-full](screenshots/home-light-full.png).

## Pricing and plans

**When.** anam.ai/pricing — a Next.js page, not Framer, with its own `:root` token set.

**Components.** [Pricing title](components.md#pricing-title), [Billing period toggle](components.md#billing-period-toggle), [Plan card](components.md#plan-card), [Plan CTA button](components.md#plan-cta-button), [FAQ item](components.md#faq-item).

**Layout.** A 72px sticky header (the same links, Next.js-flavoured) over an 820px title, the monthly/annual toggle (measured 92.33x40 — a pair of buttons, not a switch), then plan cards on the 1280 grid: Free, Pro, Enterprise. `plan-cta` is a black pill 137.81x44 that measurably shrinks under forced `:active` (133.68x42.68 — a ~3% scale press, the product's one pressed state with real paint). FAQ items are 728px rows. The page's declared set (`--bg #fff`, `--surface #fafafa`, `--text #0a0a0a`, `--border #0000001f`, `--brand #ff6200`) is the semantic layer this package's light set is built from.

**Screens.** [pricing-light-default](screenshots/pricing-light-default.png), [pricing-light-billing-toggle](screenshots/pricing-light-billing-toggle.png), [mobile-pricing-light-default](screenshots/mobile-pricing-light-default.png).

## Asking for a demo

**When.** anam.ai/get-demo — the lead form, a Next.js page.

**Components.** [Demo page title](components.md#demo-page-title), [Demo request form](components.md#demo-request-form), [Field label](components.md#field-label), [Text field](components.md#text-field), [Text field box](components.md#text-field-box), [Text area](components.md#text-area), [Submit button](components.md#submit-button).

**Layout.** A 420px column on `bg` white: 14/20 labels over 46.5px fields with `border` hairlines and 12px radii, a taller textarea, then a full-width 52.5px black submit. States were captured with sample text typed and deleted — **nothing was submitted**. The field-focused screenshot shows the browser's own outline doing the focus work.

**Screens.** [get-demo-light-default](screenshots/get-demo-light-default.png), [get-demo-light-field-focused](screenshots/get-demo-light-field-focused.png).

## Docs chrome, search and assistant

**When.** anam.ai/docs — the Mintlify documentation, light and (below) dark.

**Components.** [Docs sidebar](components.md#docs-sidebar), [Sidebar link](components.md#sidebar-link), [Sidebar link, current page](components.md#sidebar-link-current-page), [Top nav tab](components.md#top-nav-tab), [Search button](components.md#search-button), [Ask Assistant button](components.md#ask-assistant-button), [Theme menu button](components.md#theme-menu-button), [On-this-page rail](components.md#on-this-page-rail), [TOC link](components.md#toc-link), [Docs page title](components.md#docs-page-title), [Body text](components.md#body-text), [Docs link card](components.md#docs-link-card), [Code block](components.md#code-block), [Inline code](components.md#inline-code), [Method badge](components.md#method-badge), [Search dialog](components.md#search-dialog), [Search field](components.md#search-field), [Assistant panel](components.md#assistant-panel), [Assistant send button](components.md#assistant-send-button).

**Layout.** Three rails: a 288px warm-stone sidebar (section groups, 14/24 links in `neutral.500`, the current page on `accent-tint-strong` with `accent` text and icon), a ~700px content column (36/40 `neutral.900` h1, 16-18px `neutral.700` prose, `neutral.100`/`200` hairlines), and a 304px "On this page" TOC. The top bar holds tabs (the current one underlined in `accent`), the 270x36 Search ⌘K pill (white, `radius.md` 12, `border.warm`), the 158x36 "Ask Assistant ⌘I" button and the 32px theme button.

⌘K opens the 640px `radius.xl` 20 search dialog at the top of the page (nothing was typed); the assistant sheet is a 368px fixed right rail that is open by default (its send button a `radius.full` disc at 30% accent tint — nothing was sent). Code is Paper Mono: a warm near-black `neutral.950` block for fenced code and a light tinted `radius.sm` span inline; API methods are 8.8px bold badges in `method-blue`.

**Screens.** [docs-overview-light-default](screenshots/docs-overview-light-default.png), [docs-overview-light-search-dialog](screenshots/docs-overview-light-search-dialog.png), [docs-overview-light-assistant-panel](screenshots/docs-overview-light-assistant-panel.png), [docs-api-light-default](screenshots/docs-api-light-default.png), [mobile-docs-overview-light-default](screenshots/mobile-docs-overview-light-default.png).

## Docs dark theme

**When.** The docs' theme menu — the only dark theme on the site.

**Components.** [Docs page, dark](components.md#docs-page-dark), [Sidebar, dark](components.md#sidebar-dark), [Docs title, dark](components.md#docs-title-dark).

**Layout.** The ground goes pure `#000` (`--background-dark 0 0 0`), headings read `neutral.200` #e6e1de, body `neutral.300`/`400`, hairlines move to `neutral.800` (`--default-border-color` swaps gray-100 for gray-800), and the accent stays #ff6200. Sidebar and TOC keep their light-theme geometry with dark values — no relayout.

**Screens.** [docs-dark-dark-default](screenshots/docs-dark-dark-default.png), [docs-dark-dark-full](screenshots/docs-dark-dark-full.png).

## Consent

**When.** A fresh profile's first load on the marketing pages.

**Components.** [Cookie consent card](components.md#cookie-consent-card), [Manage cookies button](components.md#manage-cookies-button), [Accept all button](components.md#accept-all-button).

**Layout.** A 420x180 `radius.lg` white card pinned bottom-right on `shadow.card` with a 1px `border` hairline: the 15/21 dimmed body, then Manage cookies (text), Reject all and Accept all (gray `radius.full` pills). It rises in over 240ms (`anam-cc-rise`). It was photographed and measured in place and then **hidden without a click** — a consent choice is a submission.

**Screens.** [home-light-consent](screenshots/home-light-consent.png), [mobile-home-light-consent](screenshots/mobile-home-light-consent.png).

## Empty, loading and error states

None were reachable on the public pages: every list renders content, the only form was never submitted, and nothing errored. The signed product's empty and loading states are behind lab.anam.ai and were not captured.
