# Glassnode patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

## Marketing chrome (light)

A 72px header (`component.topbar-height`) carries the glassnode wordmark, the Products dropdown trigger (a hover opens it — measured `nav-dropdown-btn`, `nav-menu-item`), the Pricing, Data and About nav links (14px Inter, `measured.navInk`) and the dark "Launch Studio" pill (`component.cta-height` ~33px, `measured.ctaFill` #1a1a1a → `palette.grey.90`, white ink, `radius.cta` 2px). The footer is a dark #1a1a1a band: sitemap columns, the "Enter your email" subscribe field (`component.field-height` 40px, 1px #808080 border, `radius.field` 2px) beside the "Send me free research" button (`component.subscribe-btn-width`), and the "Privacy settings" consent control — a local UI toggle, never opened.

## Home (light)

The home page paints the light `--light_*` roles on the white `theme.bg.default` field. The masthead is "Pioneering digital asset market intelligence" in fraktion 51.2px/700 (#333333, `font.size.measured.hero`, `component.hero-headline-width`), paired with a product-chart mock and a "Partner Reports" promo link card (`partner-report-link`, 276 x 370) — measured, never followed. Section headings step down in fraktion (`font.size.measured.section`); in-page dark sections paint `theme.section.bgDark` #1a1a1a — sections, not a global theme.

## Vector pricing

/pricing/vector is the Bitcoin Vector page: a quarterly/monthly billing select (`vec-billing-select`), the plan card (`vec-plan-card`, 373 x 185 on the `theme.bg.tinted` #f7f8fa field, 1px black top hairline), the "Download sample" text button in ultramarine #4559dc (`palette.ultramarine.50`) and the FAQ accordion rows (`vec-faq`, 822 x 82 — local toggles, opened and measured). Nothing was purchased or downloaded.

## Contact

/contact is a category-picker page: "How can we connect" (`contact-h1`, an h2 masthead) above white category cards (`contact-category`, 384 x 193, 1px #dedfe1 border, `radius` 2px) and the subscribe band (`contact-subscribe-btn`). The category cards were measured, never followed.

## Studio shell (signed out, light)

studio.glassnode.com is the React product shell on the declared `--gds-*` layer: a 70px navbar (`component.studio-navbar-height`, `studio.background.default` white) with Home, Dashboards, Charts, Market Compass, Alpha Lab, Research, Tokenization links, the search trigger (32 x 32), a transparent "Log in" (#1a1a1a ink, `measured.studioLoginBg`) and the dark "Sign up" pill (`measured.studioSignupFill` #1a1a1a, `radius` 2px). /pricing lays out plan columns (`component.plan-card-width` ~400px, `st-plan-card`) with per-plan "Sign up" and "Configure" controls, "Show N more metrics" catalog expanders (`st-metrics-expander`, local toggles, opened and measured) and FAQ rows (`st-faq`). /charts and /dashboards render public read-only market views; Market Compass is an upgrade gate signed out.

## The Auth0 card

The navbar's real "Log in" hands to auth.glassnode.com/u/login (the volatile `?state=` is never recorded). The card is 320px wide (`component.auth-card-width`): the username field (52px, white, 1px #c9cace border), the password field, the black "Continue" submit (white ink, 2px radius), the white "Continue with Google" button (1px #c9cace border, dark ink), plus "Reset password" and "Sign up" links. The username field was typed into then cleared; the form was never submitted.

## Research (Ghost, light + dark)

research.glassnode.com is a Ghost publication on `--rf-*` roles with a real theme control (`.gh-theme-toggle`, 32 x 32 — measured at rest). The 65px header carries the tag nav; below, article cards run 1280 wide (`component.research-card-width`) over the light `--rf-bg` field, with the subscribe field (334 x 40, #f4f4f5 fill) and the dark footer. The dark surface is painted by the site's own toggle — the `research-home-light-theme-dark` screenshot and the `dark.research.*` roles, not a forced emulation.

## Docs (GitBook, light + dark)

docs.glassnode.com is a GitBook stack with the platform's own token layer (RGB-triplet ramps, kept out of the GDS token tree). Chrome: the 64px header with Website/Studio/Insights links, the "Switch to light/dark theme" buttons (33 x 33 — measured at rest; the dark surface is the `docs-home-light-theme-dark` screenshot), the search trigger, sidebar links (282 x 32, `component.docs.sidebar-link-ink`) and the metric-catalog page (`docs-metric`). Its measured values live under `component.docs.*`.

## Tokenization registry (dark by default)

tokenization.glassnode.com paints dark: a 220px left shell (`component.tok-nav-height`, `tok-shell` #141414) with asset/issuer/product/derivative nav items (#b8b8b5 ink), the search bar (560 x 32, #262626 fill, `radius.tokenization.md` 6px), the "Switch to light theme" button (28 x 28 — measured at rest; the light surface is the `tokenization-dark-theme-light` screenshot and the `light.tokenization.*` roles) and "Request access". Stat rows paint the `--c1`–`--c7` chart colours (`palette.chart.*`).

## Mobile (390px)

The phone surface keeps the same system: a 70px top bar (`component.mobile-topbar-height`) with the wordmark and hamburger (28 x 22). The hamburger toggles a dark 290 x 844 overlay drawer (`m-drawer`, #1a1a1a — the Products/Resources groups plus page links); the hero drops to a smaller masthead (`m-hero-h1`) and the newsletter field stacks full-width.

## Motion and focus

Marketing controls transition on the declared `--transition_*` shorthands (`motion.marketing.*`); measured control transitions run colour/background on the standard curve. Focus is a real keyboard focus: marketing nav links draw a 1px auto outline in ink (`measured.focusRing`), and the studio, docs and registry controls draw their own rings — all recorded as `focus-visible` states in [raw/measurements.md](raw/measurements.md). Pressed states are DevTools-forced (`CSS.forcePseudoState`), so nothing a press would submit was ever pressed.
