# Grammarly patterns

How the measured components combine on the signed-out pages. Everything here was captured public, in headless Chromium at 1440 x 900 (mobile 390 x 844); the page-level geometry is in [raw/layout.json](raw/layout.json) and the components in [components.md](components.md).

## The frame every page shares

A sticky 65px white bar (the same height at 390) tops every page — the Grammarly lockup left, the Product/Work/Education/Resources menu buttons and the Pricing link in the middle, and Request a demo, Log in and the Sign Up pill at the right ([header](components/crops/header-default.png)). The menu buttons open a 667 x 463 flyout panel ([nav-panel](components/crops/nav-panel-default.png)) of linked item rows; the flyout is hover/click driven and closes on Escape or pointer-leave. At 390 the bar collapses to lockup + a 38px menu button that opens a full-height 390-wide sheet ([m-menu](components/crops/m-menu-default.png)). Content runs full-bleed in page sections (`page-section_*` modules) on the white ground; the footer is a tall link-column block ([footer](components/crops/footer-default.png)) repeated on every route.

## Marketing heroes and cards

Home leads with a Matter display headline (~46px at 1440), a lede and the two hero CTAs — a 360x60 green primary ("Sign up It's free", `button.primary`) beside a same-size bordered Google secondary ([btn-hero](components/crops/btn-hero-default.png), [btn-google](components/crops/btn-google-default.png)). A carousel of 417px capability cards follows ([feature-card](components/crops/feature-card-default.png)) with round 48px Previous/Next arrow buttons; the cards grow ~3% on hover. A dark enterprise strip ([section-dark](components/crops/section-dark-default.png)) carries the linked stat cards ([stat-card](components/crops/stat-card-default.png)) — dark-on-light content, not a theme switch. A thin dark promo banner ([banner](components/crops/banner-default.png)) sits aside with a pale CTA.

## Plans: three static columns

/plans paints a 1160px three-column grid ([plan-grid](components/crops/plan-grid-default.png)) of 387px cards — Free, Pro, Enterprise — with no billing-period switch on the captured page. The Pro column is featured: a "Most popular" strip on the brand green over the card, the $12 USD/month price with a 60px "Try for free" tag ([sticker-tag](components/crops/sticker-tag-default.png)), and the green "Try for $0.00" CTA ([plan-cta-primary](components/crops/plan-cta-primary-default.png)); Free and Enterprise take bordered secondary CTAs ([plan-cta-secondary](components/crops/plan-cta-secondary-default.png)). A Compare Plans table follows with round 32px "More information" icon buttons ([info-icon-button](components/crops/info-icon-button-default.png)) beside each row, then a 700px FAQ of chevron-marked question rows ([faq-item](components/crops/faq-item-default.png)) — lazy-mounted, never opened.

## The free checker: editor + rail

The free tools share a sticky 46px secondary nav strip under the header ([tools-nav](components/crops/tools-nav-default.png)) — icon + label links, the current tool marked. /grammar-check lays out a 1280px two-column panel: a 670px contenteditable writing area left ([checker-editor](components/crops/checker-editor-default.png)) and a 267px Suggestions rail right. For a signed-out visitor the rail paints the Suggestions header (with a count badge once text has issues) and a "Let's get started" card of three numbered steps ([suggestions-panel](components/crops/suggestions-panel-default.png), [getting-started](components/crops/getting-started-default.png)), over the green "Get Grammarly It's free" CTA. A sample sentence typed in was underlined live by the checker's overlay and deleted after ([grammar-check-light-filled](screenshots/grammar-check-light-filled.png)); the issue underlines and suggestion cards themselves render outside the page's DOM and were not measurable.

## Forms and sign-in

/contact/sales puts a 653px lead form beside the pitch ([form](components/crops/form-default.png)): 573px fields at 42px tall with hairline borders and 6px radius ([form-input](components/crops/form-input-default.png)), matching selects ([form-select](components/crops/form-select-default.png)) and a compact 93x60 green Submit ([form-submit](components/crops/form-submit-default.png)) — clicked and typed in, never sent. /signin centres a 396px card ([signin-dialog](components/crops/signin-dialog-default.png)): a 46px email field, the green Continue button, bordered provider rows (Google, Facebook, Apple, SSO) and the "Can't sign in?" / "I don't have an account" links — measured and filled with a placeholder email, deleted after, never submitted ([signin-light-email-filled](screenshots/signin-light-email-filled.png)).

## Focus and motion, consistently

Almost every interactive element takes the same keyboard affordance: a 2px solid `green.60` (#027e6f) ring offset 1-3px — nav links, hero buttons, carousel arrows, plan CTAs, tools-nav items, the mobile menu button. The quiet exceptions (tabs, the rail CTA, form submit) draw nothing. Motion is modest: 100-200ms ease on button fills and card transforms (the carousel cards and feature cards lift ~3% on hover), 300ms on the tools strip and mobile sheet, 400ms on tab colour; `prefers-reduced-motion` is honoured partially ([raw/motion.json](raw/motion.json)).
