# Ableton patterns

How Ableton's components combine to do the recurring jobs on its public marketing pages, written from the captures of 2026-11-08 (signed out, 1440 and 390 wide). Each pattern says when the site uses it, the components it is built from (entries in [components.md](components.md), values in [tokens.json](tokens.json)), the layout, and the screens that show it. These are observations of what the site does, not Ableton's own guidance.

| Pattern | Captured | Example screen |
|---|---|---|
| [Shell and navigation](#shell-and-navigation) | yes | [home-light-default](screenshots/home-light-default.png) |
| [Teaser-cell marketing page](#teaser-cell-marketing-page) | yes | [home-light-full](screenshots/home-light-full.png) |
| [Product page](#product-page) | yes | [live-light-full](screenshots/live-light-full.png) |
| [Catalogue grids](#catalogue-grids) | yes | [packs-light-default](screenshots/packs-light-default.png) |
| [Forms and account entry](#forms-and-account-entry) | yes, at rest and focus only | [login-light-default](screenshots/login-light-default.png) |
| [Consent](#consent) | yes, never answered | [home-light-cookie-banner](screenshots/home-light-cookie-banner.png) |
| [Mobile fold](#mobile-fold) | yes | [mobile-home-light-default](screenshots/mobile-home-light-default.png) |

## Shell and navigation

**When.** Every public page: marketing, shop, blog, help, jobs and the account forms all sit inside the same shell.

**Components.** [Top navigation bar](components.md#top-navigation-bar), [Logo](components.md#logo), [Nav link](components.md#nav-link), [More disclosure](components.md#more-button) and [More panel](components.md#more-menu-panel), [Try Live CTA](components.md#trial-cta-link), [Log in or register](components.md#log-in-link), and the footer set: [Footer](components.md#footer), [Footer heading](components.md#footer-column-heading), [Footer link](components.md#footer-link), [Newsletter field](components.md#newsletter-email-field), [Newsletter submit](components.md#newsletter-sign-up-button), [Social button](components.md#social-icon-link), [Locale picker](components.md#language-selector).

**Layout.** A 69px white top bar (`layout.nav-height`) over a single `<main>` column. The bar holds the 60px grid-mark logo, the product links in 20/30 bold black (`typography.button`), the signature-blue Try-Live CTA, a 16px "Log in or register" and the More disclosure, which opens a secondary panel of links (`nav-more-panel`, captured in `home-light-more-menu`). The footer is a fat white band: newsletter form on the left, heading-led link columns, then locale picker and the six social icons (24px `currentColor` glyphs, see [icons/INDEX.tsv](icons/INDEX.tsv)). The shell draws no hairlines and no shadows; sections are separated by white space and the occasional full-bleed band.

**Screens.** [home-light-default](screenshots/home-light-default.png), [home-light-more-menu](screenshots/home-light-more-menu.png), [blog-light-default](screenshots/blog-light-default.png), [jobs-light-default](screenshots/jobs-light-default.png).

## Teaser-cell marketing page

**When.** The home page, and the pattern the whole site borrows from: a page is a stack of full-bleed cells, each a photo or video with a white Futura title pinned low, linking deeper.

**Components.** [Hero teaser](components.md#hero-teaser), [Hero title](components.md#hero-headline), [Hero CTA](components.md#hero-link), [Home cell](components.md#grid-cell), [Promo card](components.md#promo-card), [Scroll-down chevron](components.md#scroll-down-button), [Panel title](components.md#section-headline), [Blog teaser](components.md#blog-teaser-card) with [Blog teaser tag](components.md#blog-teaser-category) and [Panel category link](components.md#category-link).

**Layout.** At 1440 the cells tile edge to edge (720px squares in pairs); the promo card breaks the grid as a bordered cell with a lime-and-pale striped background and a 1px black rule (`home-promo-card`, 480 x 320). Below the grid, a 40px `panel-title` ("The latest from Ableton") sits over a row of three grey `blog-teaser` cards (360 wide, `#eeeeee` fill) each tagged with a salmon `blog-teaser-tag`, and a category link closes the panel. Text on cells is always white; text on the ground is always black; the only accent is the blue CTA.

**Screens.** [home-light-default](screenshots/home-light-default.png), [home-light-full](screenshots/home-light-full.png), [blog-light-default](screenshots/blog-light-default.png).

## Product page

**When.** The five product pages: Live (21k px), Push, Move, Note and Link, plus the trial and shop pages that echo its button set.

**Components.** [Live title](components.md#page-title), [Live section title](components.md#section-title), [Try button](components.md#try-for-free-button), [Buy button](components.md#buy-now-button), [Video play button](components.md#video-play-button), [Audio play button](components.md#audio-play-button), [Anchor link](components.md#anchor-link), [Feature collapse](components.md#discover-more-collapse) and its [open state](components.md#discover-more-collapse-open), [Link CTA](components.md#link-primary-cta).

**Layout.** Product pages alternate full-bleed dark photo bands with white sections. The title is 60/78 Futura bold in white (`typography.display`); calls to action come in two weights: `btn-try`, a boxed outline button that swaps its text from blue to black on hover, and `btn-buy`, a deep-blue `#0032e6` fill that darkens to `#042b9f`. Feature lists hide behind `collapse-toggle` rows: a 2px blue-bordered white strip at 24/36 bold that opens into the copy. Anchor links are deep blue at 18/27 with an underline and arrow; the media buttons (`btn-video`, `btn-audio`) are measured at rest, their players never started.

**Screens.** [live-light-default](screenshots/live-light-default.png), [live-light-full](screenshots/live-light-full.png), [push-light-default](screenshots/push-light-default.png), [link-light-default](screenshots/link-light-default.png), [trial-light-default](screenshots/trial-light-default.png).

## Catalogue grids

**When.** The shop index and the Packs catalogue: long grids of product or pack cards.

**Components.** [Shop title](components.md#shop-page-title), [Product card](components.md#product-teaser-card), [Product price](components.md#price), [Add to cart](components.md#add-to-cart-button), [Packs title](components.md#packs-page-title), [Pack card](components.md#pack-card), [Pack download](components.md#pack-download-button), [Blog row](components.md#article-teaser) and [Blog category badge](components.md#entry-category-badge) on the editorial index.

**Layout.** The shop index leads with 720px-square product teasers on tinted fills (`product-card` measures `#ffc3a5`); Packs runs a 40k px grid of artwork cards with a black `#000000` banner pack header (`pack-card`). Prices and actions sit inside the cards: `pack-download` is the standard blue button, `add-to-cart` a text control on the product's own fill. Nothing in either grid was clicked: no cart was opened and no download started.

**Screens.** [shop-light-default](screenshots/shop-light-default.png), [shop-light-full](screenshots/shop-light-full.png), [packs-light-default](screenshots/packs-light-default.png), [blog-light-default](screenshots/blog-light-default.png).

## Forms and account entry

**When.** The newsletter form in every footer, and the log in / register page — the only forms on the public site.

**Components.** [Newsletter field](components.md#newsletter-email-field), [Newsletter submit](components.md#newsletter-sign-up-button), [Log in form](components.md#log-in-form), [Login field](components.md#username-field), [Login submit](components.md#log-in-button), [Register form](components.md#register-form), [Register field](components.md#register-email-field), [Register select](components.md#country-select), [Register checkbox](components.md#newsletter-checkbox).

**Layout and validation.** Fields are flat `#eeeeee` rectangles (`component.field-bg`), 8px 15px padding, 20px text, no border and no radius; the login page puts a compact 246px-tall login card beside a taller 769px register card on white. Submits are the standard blue button. Focus is the only state captured: a focused field keeps its grey fill (no ring beyond the browser's caret) — measured in `newsletter-field-focused` and `login-field-focused`. Validation rules, error states and the post-submit flow all live behind a submit that was never pressed; neither form was filled or sent. The register card's password-strength meter (`ul`, `#ffc2ca` track) is measured as a child layer.

**Screens.** [login-light-default](screenshots/login-light-default.png), [login-light-full](screenshots/login-light-full.png); crops [login-field-focused](components/crops/login-field-focused.png), [newsletter-field-focused](components/crops/newsletter-field-focused.png).

## Consent

**When.** The cookie consent (`#biscuits-overlay`) sits pinned at the bottom of every page until answered.

**Components.** [Cookie consent card](components.md#cookie-consent-card), [Accept](components.md#accept-button), [Close](components.md#close-button), [More info](components.md#more-info-link).

**Layout.** A black card about 453 x 415 with 20px padding, white 16px copy and three controls: Accept in signature blue, then Close and More info as 2px-white-outline buttons (`component.button-outline-border`). It was captured exactly as found in `home-light-cookie-banner`; the clean shots hide it by CSS, which is a hide and not an answer. What the site does after a click is deliberately uncaptured.

**Screens.** [home-light-cookie-banner](screenshots/home-light-cookie-banner.png); crop [cookie-bar-default](components/crops/cookie-bar-open.png).

## Mobile fold

**When.** Every page at 390: the same shell folds to a compact bar.

**Components.** [Mobile nav bar](components.md#mobile-top-bar), [Mobile menu trigger](components.md#mobile-menu-trigger), [Mobile hero title](components.md#mobile-hero-headline), [Mobile trial CTA](components.md#mobile-trial-cta).

**Layout.** The top bar collapses to the logo and a hamburger trigger (`m-menu-trigger`, whose 0.35s colour transition is the site's longest); product links move into the "More" pattern. Hero titles drop from 60px to 20px (`m-hero-title`), teaser cells stack single-column, and the blue CTA shrinks with them. The fold keeps every rule: zero radius, one blue, white-on-photo type.

**Screens.** [mobile-home-light-default](screenshots/mobile-home-light-default.png), [mobile-home-light-full](screenshots/mobile-home-light-full.png), [mobile-live-light-default](screenshots/mobile-live-light-default.png), [mobile-shop-light-default](screenshots/mobile-shop-light-default.png).
