# Figma patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

## Marketing chrome (light)

A fixed 78.39px header (`component.topbar-height`) carries the 19 x 28 Figma mark, the Products/Solutions/Community/Resources `data-nav-dropdown-trigger` buttons, the Pricing and Log in nav links (39.19px tall, `radius.navLink` 0px, 16/23.2 figmaSans) and, on the right, Contact sales plus the 198 x 46.39 black "Get started for free" pill (`component.cta-height`, `radius.cta` 8px, `action.ctaFill` → `theme.fg.default` black with `action.ctaInk` white ink — hover lifts to `action.ctaHover` → `theme.btn.primary.bg.hover` rgba(0,0,0,0.85)). The Products trigger opens a 1440 x 523 full-width dropdown panel (`component.dropdown-width`, 1360px content nav inside) listing the product family — Figma Design, Make, Weave, Dev Mode, Motion, Specs, FigJam, Slides, Draw, Sites, Buzz — whose 328px items were measured, never followed.

## Home (light)

The home page paints the light `:root` roles on the white `background.page` field (`--fig-theme-bg` #ffffff). A 56px/56 figmaSans masthead ("The full-stack creative canvas", `font.size.display2`-class type at 328 x 168 measured) sits over the dark hero CTA (222.75 x 84 at this run's promo copy — the pill geometry is `radius.cta`). Section headings drop to the 30/36 step (`font.size.measured.body` → `font.size.title3`) and marketing sections stack on `layout.sectionBlockPadding` 80px, all on the white field — the only black-painted surface on the page is the footer's field, painted directly, not through a theme scope. The `--f-*` frame grid — 48 columns over a 1440px max (`layout.frame.*`, 30px column / 60px gutter at this viewport) — paces every marketing page.

## Pricing

/pricing leads with an 840px display headline, then the 180 x 29 Monthly/Annual segmented control (`component.toggle-width`, `radius.full`-class 80px pill on the 8%-black `theme.btn.transparent.bg.hover` wash), a "Full seat" combobox and the "All features / Key features" switch — all measured at rest, never toggled (toggling re-prices the grid). Plan cards are 330px columns (`component.plan-card-width`, 802.8px tall for the Professional card, `radius.card` 0px — the card paint lives on child layers) with a "Why choose Professional?" disclosure and dark plan CTAs; a comparison-row accordion (`feature-acc`) expands feature groups.

## Contact form

/contact is a light two-column page: the "Contact our sales team" masthead left, the multi-step form right — 600px text fields 58.19px tall (`component.field-height`, `form.fieldBg` → `theme.form.input.bg` 8%-black fill, `radius.field` 8px, generous 27px top padding over floating labels), an email/first-name/last-name row and the unnamed free-text step field (`component.topic-field-width`; its `name=topic` twin is a display:none honeypot). The 480px "Next step" button (`component.next-width`, dark fill, `radius.cta`) was measured in all states, never pressed — the form never advanced.

## The product app shell

/login, /signup and /community are a different stack — the app shell, which does not share the marketing `--fig-*` layer (it uses Inter and "Figma Sans" system stacks). Its measured values live under `component.productShell.*`: a 422px centred auth panel (`productShell.login-panel-width`, 32px side padding), the white "Continue with Google" button, a 358 x 48 dark "Log in" submit (`productShell.login-submit-fill` #2c2c2c, white ink, `radius.field`-class 8px) and an SSO link. /community paints a light index of 394.66 x 532.81 resource cards (`component.comm-card-width`) with a 284px search field, "Design resources" category pills, banner controls and like buttons — all measured, the grid itself bounded at eight chunks in the `-full` shot.

## Prompt surfaces

/make leads with the product's prompt box: a 672 x 97.19 white textarea (`prompt-textarea`, `radius.24`-class 24px corners, 36px top / 96px right padding clearing the submit affordance) with an icon-only submit button. The field was typed into then cleared; the submit measured in all states, never pressed.

## Mobile (390px)

The phone surface keeps the same system: a 72px top bar (`component.mobile-topbar-height`) with the Figma mark, the 198px "Get started for free" pill and the 40 x 40 "Open navigation menu" button. The button toggles a full-viewport overlay — its accordion nav measured 358 x 844 (`m-drawer`, Products/Solutions/Community/Resources accordions plus page links, 110px top padding) — and the hero drops to a 36/36 masthead (358 x 72).

## Motion and focus

Marketing controls transition over the declared `--fig-animation-180` (180ms) step (`duration.180`, with 250ms and 400ms companions in the ramp). Focus is an outline ring: the header CTA and nav links draw their `border.focusRing` (→ `theme.fg.default`, near-black) as an outline on keyboard focus — measured as `focus-visible` states — rather than swapping borders.

## Declared-not-painted dark

Every `--fig-theme-*` role is redeclared under `:root[data-theme="dark"]` — the `dark` token set resolves to an inverted palette (bg #000000, fg #ffffff, the same 4%/8%/16%/54% tints shifted onto white). No public page set the attribute while captured, so the set documents the declaration, not a photographed surface; the only black paint observed publicly was the footer's directly-painted field and the CTA pills.
