# Frame.io patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

## Marketing chrome (dark)

The header is a zero-height sentinel whose visible bar is a fixed `nav.mainNavigation` — 80px tall (`component.topbar-height`), preceded by a 36px cobalt announcement band (`component.announcement-height`, `theme.banner.bg` → `color.brand.cobalt` #5b53ff) when one is up. The bar carries the 30 x 34 Frame.io waveform mark, the Features/Enterprise/Resources mega-menu triggers (`nav-trigger`, 83.92 x 80, `radius.navLink`-class chrome), the Pricing and Contact Us links, Sign In (a 45px text link to the accounts stack), and the 157.25 x 39.75 "Start Free Trial" pill (`component.cta-height`, `radius.cta` 100px, `theme.btn.primary.bg` — the near-white `color.accent` #f5f5f8 fill with near-black ink: the inverse of the page field). Clicking a trigger opens a 1440 x 604.5 full-width mega-panel (`component.nav-panel-width`) — hover does nothing — whose 360 x 49.19 destination rows (`nav-menu-item`, Workflow Management, File Management, Share & Present, Review & Approvals, Camera to Cloud, Integrations, Mounted Storage, Frame.io Drive) were measured, never followed.

## Home (dark)

The home page paints the dark roles on the near-black `theme.bg` field (`color.grey.00`). An 80px FrameGothic display headline ("The creative review platform…" — `hero-h1`, 504 x 249.56 measured) sits above two 39.75px pills side by side: the white `hero-cta` ("Start Free Trial") and the ghost `hero-tour` ("Take the tour", `theme.btn.secondary.border` → `color.grey.100` 1px hairline, transparent fill). Section headings drop to the 48px step (`section-h2`, 896 x 97.91), and content paces itself on the 12-column `--grid-*` frame inside `--global-max-width` 1080px (`layout.maxWidth`, `layout.grid.*`). The only surface-level variation is the card tint — `theme.surface.card` rgba(16,16,23,0.5) — and the cobalt/iris tints that paint feature bands.

## Pricing

/pricing leads with the same 80px display headline (`price-h1`, 804 x 166.38), then the Monthly/Annually billing switch — a pair of round radio controls, not a segmented pill (`price-toggle` Monthly 91.98 x 24, `price-toggle-alt` Annually 174.86 x 24; each a 24px circle ringed `color.grey.60` #81859f, the selected side filling a 10px `color.turquoise-triumph` dot, "SAVE 13%" on the annual side) — measured at rest, never switched, because switching re-prices the grid. Plan cards are 252px columns (`component.plan-card-width`, ~797px tall, `theme.surface.card` fill, `radius.card` 10px) each with a 202 x 39.75 CTA (`plan-signup` "Sign Up Now", `plan-trial` "Start Free Trial", `plan-meeting` "Book a Meeting"). The "View all Features" control expands the feature-comparison table — 1080px category accordions (`ptable-acc`, Users / Storage / Projects & workspaces / … mounting expanded, measured again closed) — and an FAQ accordion (`faq-acc`, "How do monthly and annual pricing differ?", measured closed then opened).

## Contact

/contact pairs the 80px "Hello, how can we help you?" masthead (`contact-h1`, 712 x 166.38) with route cards: the 186.53 x 39.75 "Schedule a Meeting" pill (`schedule-btn` — it mounts a Calendly widget and was never pressed) and the 132 x 32 "Talk with Sales" link (`sales-link`, underlined text not a pill). /contact/form is the form: 431px-wide, 48px-tall text and e-mail fields (`component.field-height`, `theme.form.field.*` — `color.grey.90` ink on `color.grey.20` hairline) plus an 886px message field (`form-message`), all typed into then cleared, and the 97.84 x 39.75 "Submit" pill (`component.submit-width`, `theme.form.submit.*` — an outlined ghost, not the white CTA) measured in every state, never pressed.

## The sign-in surface

accounts.frame.io/welcome is a different stack — a light styled-components page sharing none of the marketing `--*` layer. Its measured values live under `component.productShell.*`: a 346 x 346 centred card (`productShell.login-panel-width`, "Welcome / Enter your email to get started."), a 346 x 40 e-mail field (`productShell.login-field-height`, white fill, 4px radius) and a 346 x 40 "Let's go" submit (`productShell.login-submit-fill` — the accounts stack's own cobalt #5b53ff, white ink, 6px radius). The field was typed into then cleared; the submit was measured in every state, never pressed.

## Mobile (390px)

The phone chrome is a 120px bar (`component.mobile-topbar-height` — announcement plus bar) carrying the mark, Sign In and the 25 x 20 "Toggle mobile navigation" button; the closed top bar carries no CTA. The button opens the nav overlay (`m-menu-btn` measured 20 x 25 when open), whose nav list measured 342 x 210 (`m-drawer`) with the 165 x 37.75 white "Start Free Trial" pill at its foot (`m-cta`) — all local UI toggles, never followed. The hero drops to a 44px masthead (`m-hero-h1`, 342 x 145.17) and a full-width 37.75px pill (`m-hero-cta`, 342 wide).

## Motion and focus

Controls transition on the declared steps — `--duration-300ms` 0.3s (`motion.duration.*`) over the `--ease-*` curves (`motion.easing.*`, default cubic-bezier(0.25,0.1,0.25,1)) — with the measured control signature on the header CTA (`motion.control`: colour 0.3s over cubic-bezier(0,0.44,0.6,1)). Focus is a hairline outline: keyboard focus draws a 1px dotted `theme.border.focus` (→ `color.grey.100`) ring offset 1px on pills and links, measured as `focus-visible` states; pressed is a `::after` inset tint, DevTools-forced. Under `prefers-reduced-motion` the site removes 96 of 1,465 moving elements but keeps the rest — the probe's `partial` verdict is recorded in `core.motion.$extensions.reducedMotion`, not tidied.

## Indexes

The resource surfaces share the card grammar: `/integrations` tiles are 252 x 82 logo cells (`int-card`, `color.grey.05`-near fill, 5px radius) inside category groups; `/whats-new` editorial cards are 528 x 466 (`wn-card`) with image, glow and shadow layers; `/customers` rows are 1080 x 220 story rows (`cust-card`) — all measured, never followed. Index depth is bounded at eight chunks in the `-full` shots.
