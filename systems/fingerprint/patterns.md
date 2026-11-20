# Fingerprint patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

## Marketing chrome (light)

A 56px header (`component.topbar-height`) carries the Fingerprint wordmark, the Product/Use Cases/Resources dropdown triggers, the Docs, Demo and Pricing nav links (16px Inter, `text.navInk` → `color.gray.900` #484946) and, on the right, Login, the ghost Contact Sales button and the orange "Get Started" pill (`component.cta-height` 32px, `action.ctaFill` → `theme.action.primary` #f35820 with `action.ctaInk` white ink — hover lifts to `action.ctaHover` → `color.orange.800` #bd400f). The Product trigger opens a full-width dropdown panel (`component.dropdown-width` 1288px, 262px tall for the product grid) listing the product family — Identification, Smart Signals, AI agent detection, integrations — whose items were measured, never followed. A floating "Open the chat" launcher pins bottom-right, measured and never opened.

## Home (light)

The home page paints the light `:root` roles on the white `background.page` field (`color.base.white` #ffffff). A "New — We now detect Claude Duet" announcement pill sits above the display masthead (`component.hero-headline-width`, large-step Inter), paired with the "Prompt" install expander (a local toggle that reveals install copy) and the "Install Fingerprint with AI" button. Section headings step down the declared `--text-*` ramp and marketing sections stack on generous vertical padding, all on the white field. The live `IdentifySection` demo panels on home and /products/identification paint the capture machine's visitor ID, IP and geolocation — real product output, masked in the committed shots.

## Pricing

/pricing leads with the identification-volume range slider (`component.slider-width`, 20K to 1M+ ticks) that re-prices the plan grid — measured at rest, never dragged. Plan cards are 329px bordered columns (`component.plan-card-width`, `surface.planCardBg` → `color.gray.100` #f8f8f6, a solid `#e4e5e1` `theme.border.default` hairline at `radius.card` 16px, dashed separators between the columns) whose CTAs read "Start Free" (a ghost button on the Free card) and "Contact Sales" (Enterprise); a "Compare all features" control and the feature-group accordions (`feature-acc`) expand the comparison table, and FAQ rows (`faq-acc`) accordion the same way — all local UI toggles.

## Contact form

/contact-sales is a two-column page: the sales masthead left, the form right — text fields at `component.field-height` over the `form.fieldBg` white field with `form.placeholder` #a0a09d placeholder ink, and the "Submit" button (`component.submit-width`, `action.submitFill` #f35b22). The email field was typed into then cleared; Submit was measured in all states, never pressed.

## The demo surface

/demo embeds the product's own public demo: the 01/02/03 signal-group tabs (`demo-tab`, local toggles), "See <signal> in the signals below" reveal controls, the "Analyze my browser again" button and fake checkout/sign-in fields inside the demo pane (`demo-field`, `demo-order`, `demo-login`). The live panel paints real signals for the visiting machine — visitor ID, IP, rough geolocation — so committed shots mask those regions; the controls were measured, the order/login/analyze buttons never pressed.

## Docs chrome (Mintlify, light + dark)

docs.fingerprint.com is a different stack — Mintlify — with its own token layer and a real theme preference. Its chrome: the "Open search" trigger (`component.docs.search-btn-bg`), nav tabs, sidebar links (`component.docs.sidebar-link-ink`), code blocks (no fill token: the block itself paints transparent, so its ground is the page's) and the "Change theme preference" button. The preference was measured but never held; the docs' dark surface is captured as the `docs-*-light-theme-dark` screenshots — a genuinely painted dark theme, kept out of the marketing token sets.

## The auth shell

dashboard.fingerprint.com /login and /signup are the product shell — a different stack again that does not share the marketing `--fpds-*`/`--color-*` layer. Its measured values live under `component.productShell.*`: a centred elevated auth card (`productShell.login-panel-width` 384px, the MuiPaper card), the white "Continue with Google/GitHub" buttons (`productShell.google-btn-fill`/`google-btn-ink`), the "Continue with email" / "Sign up" submit (`productShell.email-btn-fill`) and a "Login" link back to the marketing site. The buttons were measured, never pressed; the e-mail form was never opened or submitted.

## Mobile (390px)

The phone surface keeps the same system: a top bar (`component.mobile-topbar-height`) with the Fingerprint mark, the Get Started pill and the "Mobile Menu" button. The button toggles a full-viewport overlay — measured 350 x 812 (`m-drawer`, the dropdown groups plus page links) — and the hero drops to a smaller masthead (`m-hero-h1`).

## Motion and focus

Marketing controls transition over the declared `--ease-*`/`--animate-*` tokens (`motion.easing.*`) — measured transitions run 0.1–0.25s `cubic-bezier(0.4,0,0.2,1)` on colour/background/shadow. Focus is an outline ring: primary controls draw the 2px `border.focusRing` (→ `theme.action.primary` orange, offset 2px) on keyboard focus, plain links draw a 1px auto ring in ink, and the auth shell draws a box-shadow ring instead — measured as `focus-visible` states.

## Declared-not-painted dark

The marketing stylesheets redeclare only the eleven `--fpds-color-syntax-*` code colours under `.dark` — the `dark` token set — and nothing public carried that class while captured; a `prefers-color-scheme: dark` probe resolved `:root` identically. The one genuinely painted dark surface is the Mintlify docs preference, captured as screenshots rather than token values.
