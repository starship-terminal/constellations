# Enode patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

## Marketing chrome (light)

A fixed 58px glass bar (`component.topbar-height`, `light.color.background.glass.thin` over `light.color.line.primary`'s 1px bottom line) carries the 82px Enode wordmark (`component.logo-width`), the Platform and Resources mega-menu triggers (`aria-haspopup="dialog"` buttons), the Enterprise/Updates/Company nav pills (34px tall, `radius.navPill` 4px, a 60%-opacity green `::before` wash on hover) and, on the right, Sign in plus the 32px full-pill "Talk to our team" (`radius.cta`, dark fill `light.color.foreground.primary`, white ink `light.color.button.ink`). The mega-menus open a 1120 x 290 dark-glass panel (`component.mega-menu-width`/`height`) — a scoped `[data-mode="dark"]` surface inside the light page, its columns holding product-area rows with mono labels.

## Home (light)

The home page paints `data-mode="light"` on a pale-green field (`core.color.brand.75` #f0fde8 as `--color-page-background`). A 68px/475 Enode Sans masthead (`font.size.masthead`, `font.weight.masthead`, -0.02em tracking) — "Orchestrating energy for the next grid" — sits left over the paired CTAs: the dark "Talk to our team" pill and the hairline-bordered "Explore our platform" ghost pill (`light.color.border.primary.default`). Below, a 1360 x 765 dark showcase panel (`component.showcase-height`, `dark-showcase`, #151413) plays the live energy diagram — green "BALANCING 9.24 MW" type in `core.color.enodeGreen` — inside the light page. Stat cards further down are 396 x 184 translucent tiles (`component.stat-card-*`, `radius.statCard` 6px, `light.color.card.background.default` with the 1px inset hairline `light.shadow.visual.well.hairline`). Section headings drop to `font.size.h2` steps.

## The dark platform pages

/platform/overview and /platform/flexibility paint `data-mode="dark"` on `<html>` itself — whole dark pages, not scoped sections: a `dark.color.background.primary` #151413 canvas, a white masthead in `dark.color.foreground.primary`, translucent tiles (`dark.color.card.background.default` white@4%), and the same 58px chrome whose glass and pills now resolve the dark roles (the CTA inverts: white pill, `dark.color.button.ink` #252322 ink). The content column holds a sticky product-area nav (188px pills, `feature-row`) beside `.visual-frame` tiles — 304 x 171 product mocks on `dark` raised #32302f (`component.visual-frame-width`, `radius.sm` 4px) — and Enode Mono code frames. /platform/homes and /platform/assets use the same templates on the light theme.

## Contact form

/contact is a light two-column page: the "Get in touch" masthead left, a stacked form right — 294px text fields 48px tall (`component.field-height`, white `light.color.background.secondary`, `radius.field` 6px), an inquiry-type radio row, a 604 x 100 textarea (`component.textarea-height`) and the 130px dark "Send message" pill (`component.send-width`, same fill as the hero CTA). Focused and filled states were measured by typing into the fields and clearing them; the submit was never pressed.

## Platform login (a separate app)

platform.enode.com/login is a different product that does not share this token layer: a 600px-wide light panel (`component.login.panel-width`, 64/72px padding) sits over a dimmed dark product screenshot. Inside it: the Enode mark, a 455 x 41 white e-mail field, a 455 x 32 dark "Log in" submit, a "Continue with SAML SSO" link-button and "Contact us". The field, submit and links were measured (including forced pressed states); nothing was submitted and SSO was never followed.

## Mobile (390px)

The phone surface keeps the same system: a 60px top bar (`component.mobile-topbar-height`), the wordmark and a 36px round menu button (`component.mobile-menu-size`) that toggles a full-viewport nav overlay (`m-drawer`, 390 x 844). The hero masthead is fluid, not stepped: `font.size.masthead` declares `clamp(2.125rem, 1.211rem + 3.9vw, 4.25rem)` (kept on `$extensions.responsive`), which resolves to the measured 34.586px at 390px, and the CTAs keep the full-pill profile.

## Motion and focus

Controls transition color/background/border/outline/fill/stroke/transform over 150ms cubic-bezier(.4,0,.2,1) (`core.motion.control`, matching `duration.default` 150ms and `easing.default`). Focus is an outline ring, not a border swap: nav pills, Sign in, footer links and the login submit draw `2px solid #b0f87c` (`core.color.brand.225`, offset 2px) — the signature green is spent on focus and live metrics, not fills.
