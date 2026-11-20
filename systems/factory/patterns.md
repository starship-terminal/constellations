# Factory patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

## Marketing chrome (light)

A fixed ~72px bar (`component.topbar-height`) floats over the page behind a backdrop-blur mask: the Factory asterisk-and-wordmark (`component.logo-width`, 128x19), the Product/Enterprise/Company mega-menu triggers (`aria-expanded` buttons that open on hover, 61x60), the Pricing/News/Docs nav links (12px labels), a locale globe, a mono SIGN IN link, and the paired pills — bordered CONTACT SALES (`border.cta2Border`, 114x25) and dark-filled DOWNLOAD (`action.ctaFill` #101010, `component.cta-height`, 80x25). The Product mega-menu opens a viewport-wide container (`component.mega-menu-width`/`height`, 1440x363) holding a white rounded card with three labelled columns — SURFACES, AUTOMATIONS, PLATFORM — of small link rows. Under it the page gutters at `layout.contentGutter` (36px at 1440) inside the `layout.contentColumn` 1440px column.

## Home (light)

The home page ships `data-theme="light"` on the `#f9f9f9` field (`light.color.background`). The hero centers the asterisk mark (87.5x84.88) over a ~60px/500 uppercase Geist masthead (`component.hero-masthead-width` — "AI CODING AGENTS FOR THE ENTERPRISE"), a Geist Mono tagline ("Model agnostic. Deployed anywhere.", `text.subInk` #8a8380), the paired DOWNLOAD / BOOK DEMO pills (110x31 dark fill / 123x31 bordered) and the install-command copy box (`component.install-cmd-width` 420px, `font.family.geistMono` on the #ebebeb `color.surface.sunken` chip, with the 32x32 "Copy code" icon-button). A dark video panel follows, then the customer-logo strip and the first feature sections. Down the page: eight product cards with dark thumbnails (Analytics, Droid Computers, Agent Readiness, Mission Control; Automations, Model Routing, Code Review, AutoWiki), the connector-logo grid ("Plugs into the stack"), customer testimonial tiles, the dark "Built for industries" `.invert-color-scheme`/`[data-container-variant="inverted"]` section, the SOC/ISO compliance badge row, a numbered use-case list and the news card rail — all scroll-revealed sections ending in the dark CTA card and the dark footer.

## The scoped dark sections

factory.com never paints a whole dark marketing page. Dark lives inside `.invert-color-scheme` panels, `[data-container-variant="inverted"]` sections (the "Built for large enterprises" panel on /enterprise, the industries section on home) and the footer — `[data-dark-hero]` marks the dark hero tops that the blurred header adapts over. The fields are #1f1d1c `dark.background.panel` and the #101010 footer with `dark.color.foreground` #eeeeee ink, `dark.color.base-*` muted copy and the orange `color.accent.200` #ee6018 kept for eyebrow labels and accents. The dark set in tokens.json is the `:root` default these sections paint — not a user-selectable mode on the marketing site.

## Pricing

/pricing is light: the "Pricing Plans" masthead, a plan-tier switcher (PRO/PLUS/MAX as `role=radio` buttons — the selected tab paints a #101010 fill, `component`-measured 116x22 — a local UI toggle), plan cards (`component.plan-card-width` 416px) and a FAQ accordion of bordered question rows. Plan CTAs were measured, never followed.

## Contact form

/contact pairs the "Bring Autonomy to your Engineering Organization" masthead (44px) with a lazily-mounted HubSpot form: text fields (`component.field-height` 36px), a "Select one..." topic select, the message textarea (`component.textarea-height` 72px), a reCAPTCHA badge and the mono SUBMIT button (`component.send-width` ~100px, Geist Mono 14px). Fields were focused and typed into then cleared; SUBMIT was never pressed. The form's skin is the HubSpot `--hsf-*` variable layer, recorded in raw/css-vars.json's vendor bin.

## Docs (docs.factory.com)

docs.factory.com shares the marketing token layer plus a real three-way theme selector (icon-only `Switch to Light/Dark/System theme` buttons — local UI toggles). The layout: a top bar with the wordmark, Documentation/API Reference/Changelog tabs, search, GitHub and Discord icons, SIGN IN and DOWNLOAD; a left sidebar of collapsible nav groups (`component.docs-sidebar-width`); the article body with Geist prose and shiki-themed code blocks. The docs pages were captured light, then the selector switched the whole page to `data-theme="dark"` for the `*-dark-*` shots and re-measurements (`docs-h1-dk`, `docs-sidebar-dk`, `docs-code-dk`) — the dark set's roles resolve there exactly as the scoped marketing sections resolve them.

## Sign-in (app.factory.ai → auth.factory.ai)

app.factory.ai boots a splash then redirects to auth.factory.ai: a different app that does not share the marketing token layer. A dark page centers the sign-in card (`component.signin.panel-*`, 380x248.52): "Sign in", the e-mail field (`component.signin.field-*`, 378x34), "Continue with email" (a near-white fill `component.signin.submit-fill` #fdfcfb with `component.signin.submit-ink` #17120f, 380x36), an OR divider, "Continue with Google" (bordered, `component.signin.google-*`) and the Sign up link. The field was typed into then cleared; nothing was submitted and no OAuth link was followed. Every post-login surface — the Droid console, missions, settings — is the documented boundary.

## Mobile (390px)

The phone surface keeps the same system: the top bar shrinks to the mark, a locale globe and a 32x32 "Open menu" button (`component.mobile-topbar-height`, still 72px) — there is no header CTA pill at 390 wide. The menu button toggles a full-viewport `header nav` overlay (`m-drawer`, 390x844): accordion rows (Product/Enterprise/Company), inline links (Pricing/News/Docs), and SIGN IN / CONTACT SALES / DOWNLOAD rows (358x31, DOWNLOAD on the #101010 dark fill). The hero masthead drops to 32px/500 and the hero CTA becomes GET STARTED (115x31).

## Motion and focus

Controls transition color/background/border/shadow/transform over 150ms cubic-bezier(.4,0,.2,1) (`duration.default`, `easing.default`). Sections reveal on scroll — opacity/translate reveals driven by scroll progress, which is why `-full` captures stitch scrolled viewport tiles rather than one fullPage frame. Focus is an outline ring on header controls and links (`border.focusRing`); the measured rings are listed in components.md's Shared values.
