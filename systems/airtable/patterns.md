# Airtable patterns

How the components combine on www.airtable.com's public marketing pages. Every name links to its entry in [components.md](components.md); every screen links into [screenshots/](screenshots). Take values from tokens.json, never from the images.

## Shell and navigation

**When.** Every marketing page: home, platform, solutions, pricing, contact-sales, templates, marketplace, whatsnew and about sit inside the same chrome.

**Components.** [Promo bar](components.md#promo-bar) with [Promo link](components.md#promo-link) and [Promo close button](components.md#promo-close-button), [Top navigation bar](components.md#top-navigation-bar), [Nav dropdown trigger](components.md#nav-dropdown-trigger), [Nav link](components.md#nav-link), [Book Demo button](components.md#book-demo-button), [Sign up button](components.md#sign-up-button), [Log in link](components.md#log-in-link), the open [Nav drawer](components.md#nav-drawer) with [Drawer link](components.md#drawer-link), and the footer set: [Footer](components.md#footer) and [Footer link](components.md#footer-link).

**Layout.** A 121px chrome stack: a 42px `#f0f6ff` promo strip over the white nav row. The row holds the wordmark, three drawer triggers (Platform, Solutions, Resources) in ATSeasonSans 16/20.8 w650, Enterprise, Pricing, What's new, a 12px-radius outline Book Demo, the ink Sign up pill, and Log in. A trigger opens `nav-dropdown`, a 710px white drawer pinned under the bar, with link rows on the left and a promo card on the right. The footer is a white link-column grid (Platform / Solutions / Resources / Learn / Company) over a legal row. Fixed elements on several pages are the promo bar (`sticky`) plus a cookie consent bar on first visit, which the captures dismiss by sweep, not by answering.

**Screens.** [home-light-default](screenshots/home-light-default.png), [home-light-nav-dropdown](screenshots/home-light-nav-dropdown.png), [home-light-promo-closed](screenshots/home-light-promo-closed.png), [platform-light-default](screenshots/platform-light-default.png).

## Carousel marketing page

**When.** The home page, and the platform pages that repeat its parts: a stack of white sections alternating hero, feature carousel, dark proof band and coloured tiles.

**Components.** [Hero title](components.md#hero-title), [Hero primary CTA](components.md#hero-primary-cta), [Hero secondary CTA](components.md#hero-secondary-cta), [Feature tab list](components.md#feature-tab-list) with [Feature tab](components.md#feature-tab) and [Feature tab, selected](components.md#feature-tab-selected), [Feature card](components.md#feature-card), [Carousel control](components.md#carousel-control), [Story row](components.md#story-row) / [Story card](components.md#story-card) on the dark band with [Stories pause](components.md#stories-pause-button), [Stories previous](components.md#stories-previous-button) and [Stories next](components.md#stories-next-button), [Coloured tile card](components.md#coloured-tile-card), [Resource card](components.md#resource-card), [See more link](components.md#see-more-link).

**Layout.** Sections centre on a ~1344px column. The hero is a centred Haas title over two CTAs — the ink pill and a 1px outline twin. The feature carousel shows a white tab list over a media card; the stories carousel sits on a dark ink band with 40px ghost-ring arrows (`rgba(255,255,255,.23)` ring, `.5` on hover) and a pause button; prev renders only off the first slide. The tile rows are the signature shape: 32px-radius pastel cells (`#c7e5f2`, `#fcab79`) with dark tinted text. Resource cards below reuse the same tile logic with an image plus copy.

**Screens.** [home-light-default](screenshots/home-light-default.png), [home-light-full](screenshots/home-light-full.png), [platform-light-full](screenshots/platform-light-full.png), [platform-ai-light-full](screenshots/platform-ai-light-full.png).

## Index galleries

**When.** /templates, /marketplace, /whatsnew and /customer-stories: a display title over a filter or tab rail and a card grid.

**Components.** [Templates title](components.md#templates-title) / [Marketplace title](components.md#marketplace-title) / [What's new title](components.md#whatsnew-title) / [Customer stories title](components.md#customer-stories-title), [Template search field](components.md#template-search-field) and [Marketplace search field](components.md#marketplace-search-field), [Filter section](components.md#filter-section) and [Filter section, open](components.md#filter-section-open), [What's new filter](components.md#whatsnew-filter), [Template card](components.md#template-card), [Marketplace category card](components.md#marketplace-category-card), [What's new card](components.md#whatsnew-card), [Marketplace CTA](components.md#marketplace-cta).

**Layout.** Templates pairs a pill search field (fully rounded) with a left filter rail of collapsible sections over a card gallery. Marketplace shows three big saturated category tiles (For marketing teams / Page designer / Scripting — background-image divs, text is baked in), then a tab rail and extension rows. What's new embeds Airtable's own published interface in an iframe; its release cards are 6px-radius white panels with a low shadow and plan/month chips, filtered by "Available on" / "Release month" dropdowns measured inside the frame.

**Screens.** [templates-light-default](screenshots/templates-light-default.png), [marketplace-light-default](screenshots/marketplace-light-default.png), [whatsnew-light-default](screenshots/whatsnew-light-default.png), [customer-stories-light-default](screenshots/customer-stories-light-default.png).

## Pricing grid

**When.** /pricing, the one page typeset entirely in Inter Display rather than Haas.

**Components.** [Pricing title](components.md#pricing-title), [Plan card](components.md#plan-card), [Plan CTA](components.md#plan-cta), [Plan comparison table](components.md#plan-comparison-table) with [Comparison row](components.md#comparison-row), [Pricing FAQ item](components.md#pricing-faq-item) and [Pricing FAQ item, open](components.md#pricing-faq-item-open).

**Layout.** Four plan columns (Free, Team $20, Business $45, Enterprise Scale) each with a 2px-bordered CTA; the recommended column lifts on a 50%-alpha `#f0f6ff` wash. Below, "Compare our plans" is a div grid of `hover-container` rows — feature name left, per-plan check/marks right, under a sticky plan header. A FAQ accordion closes the page. The plan CTAs lead to signup/checkout and were never pressed.

**Screens.** [pricing-light-default](screenshots/pricing-light-default.png), [pricing-light-full](screenshots/pricing-light-full.png).

## Sales form

**When.** /contact-sales: a centred 430px lead form under the Haas title.

**Components.** [Contact page title](components.md#contact-page-title), [Contact form](components.md#contact-form), [Field label](components.md#field-label), [Text field](components.md#text-field) and [Text field box](components.md#text-field-box), [Email field](components.md#email-field), [Phone field](components.md#phone-field) with [Country selector](components.md#country-selector), [Text area](components.md#text-area), [Select field](components.md#select-field) and [Select field, open](components.md#select-field-open), [Submit button](components.md#submit-button).

**Layout.** Fields are 56px boxes with a floating `* Label` inside (12/18, w500) and a 1px keyline border painted by the field container; focus draws a 1px `#005fcc` outline. "Country" and "How can our team help?" are custom combobox divs (the hidden Marketo mirror `<select>`s stay 0x0), opened locally and measured open without choosing. Submit is the ink pill, measured and focused but never pressed; the Marketo submit is a real submission.

**Screens.** [contact-sales-light-default](screenshots/contact-sales-light-default.png), [contact-sales-light-full](screenshots/contact-sales-light-full.png).

## Mobile fold

**When.** Every page at 390 wide: the chrome collapses and sections stack.

**Components.** [Top navigation bar (mobile)](components.md#top-navigation-bar-mobile), [Nav menu button (mobile)](components.md#nav-menu-button-mobile), [Mobile nav sheet](components.md#mobile-nav-sheet), [Hero title (mobile)](components.md#hero-title-mobile).

**Layout.** At 390 the bar drops the links to an "Open side menu" button that slides in a 342px drawer from the left. Sections reflow to a single column; the tile cards keep their 32px radius, CTAs go full width. The promo strip persists.

**Screens.** [mobile-home-light-default](screenshots/mobile-home-light-default.png), [mobile-home-light-nav-open](screenshots/mobile-home-light-nav-open.png), [mobile-pricing-light-default](screenshots/mobile-pricing-light-default.png), [mobile-platform-light-default](screenshots/mobile-platform-light-default.png).
