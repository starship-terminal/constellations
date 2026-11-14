# Descript patterns

How the components in [components.md](components.md) combine into the public marketing pages. Every value is in [tokens.json](tokens.json); the crops are in [components/crops/](components/crops) and the page captures in [screenshots/](screenshots).

## The chrome band

Every page carries the same floating nav: a 102px `#fff7fa` bar (`component.header-height`, `light.background.page`) holding the 98px wordmark (`component.logo-width`), 16px/600 Booton items — Features (a hover mega-panel), Pricing, Contact sales, Sign in — and the 108x54 `#772a4d` Sign up button at 12px radius (`component.signup-size`, `light.action.primary`, `core.radius.cta`). Nav links rest transparent in `#26171d` ink (`light.text.ink`) and take a `#f1eaed` warm-grey wash on hover (`light.action.hover-wash`); the maroon button deepens to `#5b142e` (`light.action.primary-hover`). The bar is fixed with a 12px radius where it meets the page edge. At 390px it collapses to an 84px bar (`component.m-header-height`).

## The maroon hero band

The home opens on a deep-maroon band: an 18px Brett uppercase eyebrow in `#f73b3b` (`light.text.accent`, `core.font.size.eyebrow`), then the 88px Gamuth display headline painted `#fff8f4` (`light.text.on-dark`, `core.font.size.hero`, `component.hero-display-size`). Below it sits the 610px workflow tab strip (`component.flow-tabs-width`): five 44px tabs (`component.flow-tab-height`) whose unselected state is muted `#c4b5bb` text (`light.text.muted-on-dark`) that picks up a `#26171d` ink wash on hover, and whose selected state fills `#5b142e` (`light.surface.tab-selected`) with `#fff7fd` text — a real local toggle, measured in its opened state. Product pages (/video-editing, /underlord) run the same shape at 72px (`core.font.size.page`) with a 222x56 `#f73b3b` red CTA (`light.action.red`, `core.radius.cta`) that deepens `#b81b1e` → `#8f0c10` across hover and pressed.

## Pricing

/pricing runs the 56px Gamuth "A plan for whatever you create" (`core.font.size.section`) into the billing toggle: a 228x50 track on `#f1eaed` (`component.toggle-size`, `light.background.toggle-track`, `core.radius.toggle`) holding two 106x34 options (`component.toggle-option`) — a local switch measured in its Annual-opened state. The 284x708 plan cards (`component.plan-card-size`) carry full-width 284x56 `#390a1a` CTAs (`component.plan-cta-size`, `light.action.deep`). Below, the plan-comparison table and a 56px FAQ section close the page. At 390px the toggle shrinks to 98x32 options and the CTAs go full-width at 52.5px (`component.m-toggle-option`, `component.m-plan-cta`).

## The auth card

web.descript.com/authenticate is the sign-in boundary: a centered card of 308x40 controls (`component.auth-control`) at 8px radius (`core.radius.control`) — "Continue with Google" and "Use single sign-on" as `#fdfcfc` outline buttons (`light.action.auth-outline`), the email field in the same fill, "Continue with email" as the `#3f2a32` primary (`light.action.auth-primary`, Booton VF 15.75px/500) that fades to a 90%-alpha shade on hover, and "Use a password instead" as a ghost. Terms/Privacy links sit under the card. Every control was measured and the field typed into and cleared; nothing was submitted.

## Cards and gallery

/templates runs a 72px Gamuth heading into a grid of 336x381 template cards (`component.template-card`): image-topped tiles whose overlay link carries a 2px inset ring on focus-visible rather than the shared 1px outline. The customer story (/customers/saastr) is long-form: a multi-line headline, 16px/600 Booton prose (`core.font.size.body`), and a "Request a demo" CTA.

## The footer

A ~1146px footer (`component.footer-height`) on `#110a0d` (`light.background.footer`) — the darkest surface in the package — with link columns under the wordmark.

## Focus language

Almost every control takes the browser's 1px auto outline in `#101010` (`light.border.focus`, `component.focus-ring`); template-card overlays paint a 2px inset ring instead. No custom focus-ring colour is declared on the public surface.

## Mobile

At 390px the nav becomes an 84px bar, the display drops to 48px (`core.font.size.mobile-display`), the billing toggle shrinks, plan CTAs go full-width, and the footer stretches to ~1859px (`component.m-header-height`, `component.m-plan-cta`).
