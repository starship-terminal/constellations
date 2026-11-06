# Refero patterns

How Refero's components combine to do the recurring jobs on its public pages, written from the captures of 2026-11-02 (signed out, 1440 and 390 wide, headless Chromium). Each pattern says when Refero uses it, the components it is built from (entries in [components.md](components.md), values in [tokens.json](tokens.json)), the layout, and the screens that show it. These are observations of what the product does, not Refero's own guidance.

Two hosts share the token system but compose it differently, and this file keeps them apart: **refero.design** patterns come first (the rail, the research box, the galleries, the promos), then **styles.refero.design** (the top bar, the video-tile index, the style page).

| Pattern | Captured | Example screen |
|---|---|---|
| [Research shell and navigation](#research-shell-and-navigation) | yes | [home-light-default](screenshots/home-light-default.png) |
| [Asking for research](#asking-for-research) | yes | [home-light-research-focused](screenshots/home-light-research-focused.png) |
| [Search, filtering and galleries](#search-filtering-and-galleries) | yes, results gated behind sign-up | [search-light-default](screenshots/search-light-default.png) |
| [Promos and guidance](#promos-and-guidance) | yes | [home-light-promo](screenshots/home-light-promo.png) |
| [Upsell and paywall](#upsell-and-paywall) | yes, checkout excluded | [pricing-light-default](screenshots/pricing-light-default.png) |
| [Styles gallery shell](#styles-gallery-shell) | yes | [styles-light-default](screenshots/styles-light-default.png) |
| [Video-preview cards](#video-preview-cards) | yes | [styles-light-card-hover](screenshots/styles-light-card-hover.png) |
| [A style's page](#a-styles-page) | yes | [styles-entity-light-default](screenshots/styles-entity-light-default.png) |
| [Feedback after an action](#feedback-after-an-action) | yes | [styles-light-card-hover](screenshots/styles-light-card-hover.png) |
| [Empty, loading and error states](#empty-loading-and-error-states) | loading only | [styles-light-card-hover](screenshots/styles-light-card-hover.png) |

## Research shell and navigation

**When.** Every refero.design page a visitor moves between: the home, Web apps and iOS apps search, pricing, MCP.

**Components.** The 270px left rail itself, [Refero MCP promo card](components.md#refero-mcp-promo-card), and the content column holding [Research box](components.md#research-box), [Hero title](components.md#hero-title), [Section title](components.md#section-title) and [Result card](components.md#result-card).

**Layout.** A fixed rail, `layout.sidebar-width` 270px, at the page's left edge on `background.page` with no border against the content: the refero wordmark on top, a "New research" bordered row with its `⌘K` hint, three destination links (Web apps, iOS apps, Styles with a Beta tag), and a foot of quiet secondary links (Pricing, Connect MCP, Figma Plugin, Log In / Sign Up). The content right of it is a column `layout.content-width` 1170px wide inside the `layout.page-width` 1600px wrap, padded 48px a side: serif title, the research box centred under it, then h2 sections (`fontSize.h2` 32/40) of cards.

The rail's identity is that it is flat — no fill change against the page, no separators; hierarchy comes only from the current item's `background.subtle` fill and weight. The [MCP promo card](components.md#refero-mcp-promo-card) floats separately, fixed at the lower left over the rail's ground with the only real drop shadow in the product (`shadow.card-pop`).

At 390 wide the rail collapses to a top bar and the content goes full-bleed; the research box shrinks to `m-research-box` 358 wide ([mobile-home-light-default](screenshots/mobile-home-light-default.png)).

**Screens.** [home-light-default](screenshots/home-light-default.png), [home-light-promo](screenshots/home-light-promo.png), [search-light-default](screenshots/search-light-default.png), [mcp-light-default](screenshots/mcp-light-default.png), [mobile-home-light-default](screenshots/mobile-home-light-default.png).

## Asking for research

**When.** The one act the app exists for, so the input is the page's centrepiece rather than a field in a form.

**Components.** [Research box](components.md#research-box), [Research prompt field](components.md#research-prompt-field), [Mode chip](components.md#mode-chip), [Research-mode coach box](components.md#research-mode-coach-box), [Coach close X](components.md#coach-close-x).

**Layout.** A 752 x 102 card at `radius.2xl` 24px on `component.research-box-bg` (`gray.solid.100`), drawn not by a border but by `shadow.inset-ring`, a soft 1px inset hairline. Inside: the placeholder line in `text.secondary`, a hairline under it, then a row of controls — a "Search by Image" white pill, the three scope chips, and the 36px near-black submit arrow pushed to the right edge.

**How the chips read.** The scope chips (Research mode / Web apps / iOS apps) are white pills at `component.research-chip-bg` with a 1px `component.research-chip-border` keyline and `shadow.chip`, labels in `component.research-chip-label` (`gray.alpha.600`) that go to ink on hover and press; the focused chip adds a 2px ring shadow. They act as a single-select corpus switch, not filters applied over results.

**The coach.** On first load a second box sits under the research card, [Research-mode coach box](components.md#research-mode-coach-box): same 752 width, top-rounded only (it docks onto the box above), white with a fainter hairline (`component.coach-box-*`), a bold lead, a grey continuation, and a bare svg X. It slides in over 400ms (`duration.coach`) and dismisses for good.

**Validation.** None is shown: an empty submit just does nothing. There is no error, helper or required state anywhere on the public pages.

**Screens.** [home-light-default](screenshots/home-light-default.png), [home-light-promo](screenshots/home-light-promo.png), [home-light-research-focused](screenshots/home-light-research-focused.png), [m-research-box crop](components/crops/m-research-box-default.png).

## Search, filtering and galleries

**When.** The Web apps and iOS apps pages and the home Page Types sections — grids of real product screenshots a visitor browses by corpus.

**Components.** [Search box (results page)](components.md#search-box-results-page), [Search result tile](components.md#search-result-tile), [iOS app tile](components.md#ios-app-tile), [Result card](components.md#result-card), [Result card label](components.md#result-card-label), [Section title](components.md#section-title), the Screens/Flows toggle on the search pages.

**Layout.** Search pages put the corpus switch first — the same chip pattern as the research box (Web apps / iOS apps), then a Screens / Flows pair of text toggles — then an auto-fill grid of tiles at `layout.min-col-width` 420px minimum columns, 16px gaps. A tile is a padded `gray.solid.200` shot (radius `radius.sm` 8px on the home Page Types cards, ~19%/9.2% responsive radii on the phone-shaped iOS tiles) with a favicon-and-name label row. Cards show no hover lift and no shadow; the pointer is the affordance.

**Two things the grid does that a gallery usually doesn't:** the home sections rotate their card sets on a timer (the same section re-renders new products while you watch — captured as changing DOM under the measurement run), and every grid ends in a **paywall tile**, a "Sign up to see more" panel that is the product's only wall ([search-light-full](screenshots/search-light-full.png)).

The result sets themselves sit behind sign-up, so what a tile links to was not captured.

**Screens.** [search-light-default](screenshots/search-light-default.png), [search-light-full](screenshots/search-light-full.png), [apps-light-default](screenshots/apps-light-default.png), [mobile-search-light-default](screenshots/mobile-search-light-default.png).

## Promos and guidance

**When.** First load of the refero.design home: two stacked pieces of guidance on top of the research column.

**Components.** [Refero MCP promo card](components.md#refero-mcp-promo-card), [MCP title](components.md#mcp-title), [Explore MCP button](components.md#explore-mcp-button), [Promo card Close button](components.md#promo-card-close-button), [Research-mode coach box](components.md#research-mode-coach-box), [Coach close X](components.md#coach-close-x).

**Two shapes, two jobs.** The coach box explains research mode inline under the input (quiet, white, dismissed by a bare svg X). The MCP card sells the agent integration as a floating white card, radius `radius.lg` 16, at the viewport's lower left: bold title, grey paragraph, a plain-text "Explore MCP" link beside a bordered ghost "Close" (`component.mcp-close-border`, filling `gray.solid.300`-ish on hover and press).

**Controls without semantics.** The lesson the code should not copy: the promo Close is a styled `div`, the coach X is a `cursor:pointer` `svg`, and several rail items are anchors only by behaviour. The look is consistent (36px pill, 14/20 medium) even where the element isn't a button.

**Screens.** [home-light-promo](screenshots/home-light-promo.png), [mobile-home-light-promo](screenshots/mobile-home-light-promo.png).

## Upsell and paywall

**When.** The pricing page, the end of every search grid, and the MCP card's Explore link.

**Components.** [Pricing title](components.md#pricing-title), [Plan card](components.md#plan-card), [Plan CTA button](components.md#plan-cta-button), [Student discount card](components.md#student-discount-card), the paywall tile at each grid's end.

**Layout.** A serif pricing title over plan cards: black 349px cards at `radius.lg` 16 with 30px padding, grey feature lists, and the `plan-cta` — a 56px pill at `radius.3xl` 28 in `action.primary` (near-black; white in dark) with `text.on-button` text. The student discount card repeats the shape at smaller size with a "Save $60 · Best Value" badge. The enterprise band sits underneath. Upsell elsewhere is quieter: the paywall tile is a text panel at the grid's tail, and the MCP card's only flourish is its shadow.

**Screens.** [pricing-light-default](screenshots/pricing-light-default.png), [pricing-light-full](screenshots/pricing-light-full.png), [search-light-full](screenshots/search-light-full.png).

## Styles gallery shell

**When.** Every styles.refero.design page: the index, the prompt-list pages and each style's documentation page.

**Components.** [Styles header](components.md#styles-header), [Gallery hero](components.md#gallery-hero), [Gallery headline](components.md#gallery-headline), [Search field](components.md#search-field), [Filter chip](components.md#filter-chip).

**Layout.** Instead of a rail, a sticky 81px top bar (`component.styles-header-border` hairline under it) over a near-white page, blurring 24px over `background.header-glass` (lab(1,0,0) at 90%). Inside it: the styles wordmark left, prompt pages, GitHub and X links, and a dark "Connect to your AI" pill right. Below, the centred hero column `layout.hero-width` 1100px holds the kalice headline (`fontSize.hero-styles` 64/69), then a 671 x 46 fully-round search pill, then filter chips.

The content sits in a wider wrap (`layout.content-width` 1800px): the filter chips sit in a four-column chip area, then the card grid. Everything here leans on fills: the page is `gray.solid.0`, the chips' hover is `background.subtle`, the tiles `gray.solid.100`.

At 390 wide the header compacts, the hero drops to a left-aligned stack, and the grid goes single-column ([m-styles-card](components/crops/m-styles-card-default.png), [mobile-styles-light-default](screenshots/mobile-styles-light-default.png)).

**Screens.** [styles-light-default](screenshots/styles-light-default.png), [styles-light-full](screenshots/styles-light-full.png), [mobile-styles-light-default](screenshots/mobile-styles-light-default.png).

## Video-preview cards

**When.** The styles index's card grid — the product's signature interaction.

**Components.** [Style card](components.md#style-card), [Style card, video playing](components.md#style-card-video-playing), [Card footer favicon](components.md#card-footer-favicon), [Similar style card](components.md#similar-style-card).

**How it works.** A card is a 394 x 339 padded tile at `radius.4xl` 32px on `background.subtle`: an inner shot area (the site's captured screenshot, 8px radius, inside a bordered well), then a footer row with a 40px rounded-square favicon, the site name and a tagline. At rest the poster image is all a visitor sees. On a real pointer hover the card's scroll-preview mp4 — a recording of someone scrolling the actual site — loads from the media CDN and fades in over the poster, `duration.fade` 0.5s opacity, playing inside the same frame; the poster stays put underneath so leaving hover returns to it. There is no badge, play icon or hint that video exists: the motion is the discovery.

The mobile card keeps the shape at 342 x 294 ([m-styles-card](components/crops/m-styles-card-default.png)); the similar-style card on an entity page repeats it smaller, 308 x 260 at `radius.lg` 16.

**Screens.** [styles-light-card-hover](screenshots/styles-light-card-hover.png), [styles-card-video crop](components/crops/styles-card-video-video.png), [styles-light-default](screenshots/styles-light-default.png).

## A style's page

**When.** Clicking a style card — the entity's documentation page.

**Components.** [Styles header](components.md#styles-header), [Media frame](components.md#media-frame), [Style favicon](components.md#style-favicon), [Style name](components.md#style-name), [Doc tab](components.md#doc-tab), [Doc tab, current](components.md#doc-tab-current), [Copy button](components.md#copy-button), [Similar style card](components.md#similar-style-card).

**Layout.** Two columns under the same 81px bar: left, the `entity-media` frame 630 x 394 at `radius.lg` 16 on `background.subtle`, where the scroll video loads over the poster on its own (no hover needed here); right, a narrow documentation column 768px max — 64px circular favicon, the kalice `entity-title` 48/48, the site's domain, then the doc tabs over a hairline.

**The tabs** are the four artefacts Refero ships per style: DESIGN.md, Tailwind v4, CSS Variables, Design Tokens — small caps-ish 13/24 labels (`typography.chip-styles`) tracked wide, the current tab marked by a 2px ink underline rather than a fill. The doc pane below renders the artefact in JetBrains Mono with a syntax palette from the code ramp, and the [Copy button](components.md#copy-button) — a 66 x 28 bordered pill — copies it.

**Screens.** [styles-entity-light-default](screenshots/styles-entity-light-default.png), [styles-entity-light-full](screenshots/styles-entity-light-full.png).

## Feedback after an action

**When.** After a visitor hovers, presses, focuses or dismisses.

- **Hover is quiet.** Nothing lifts and nothing slides: chips and ghost buttons swap to a subtle fill or darker label in `duration.fast` 150-200ms; links go from secondary to primary ink; the one exception is the card's video, which is the product's whole idea (see [Video-preview cards](#video-preview-cards)).
- **Pressed mirrors hover.** The chips and doc tabs go to ink on press exactly as on hover (measured with forced :active; a real press switches the corpus or the document instead).
- **Focus is two systems.** refero.design leans on the browser's `auto` outline (1px #005fcc) on CTAs and links plus the research chips' own 2px ring shadow; styles.refero.design draws a 2-3px ring shadow in `rgba(111, 113, 121, 0.4-0.5)` — the `--ring` colour at half alpha — on its chips, tabs and Copy button. The research input and the result cards draw nothing at all on focus (documented under Shared values in [components.md](components.md)).
- **Dismissals are immediate.** The coach box and the MCP card close without confirmation or toast; nothing confirms the click beyond the element disappearing.

## Empty, loading and error states

**Loading.** The only loading a visitor sees is the video's: a card or entity frame shows its poster while the mp4 buffers, and the video fades in when ready — the poster is the skeleton. Pages themselves render server-side; no skeleton screens appeared in the capture.

**Empty.** No empty grid or empty state exists publicly: the index always has cards, and the search grids always end at the paywall tile rather than an empty message.

**Error.** No reachable error: forms don't validate visibly, and no failed page or 404 state appeared during capture. Where the product fails (a missing local video in a mirror), the honest fallback — the CDN URL — is the only error state the design needs.

**Destructive confirmation.** Nothing destructive exists signed out: no deletes, no leaving flows, and both dismissable promos close without asking.
