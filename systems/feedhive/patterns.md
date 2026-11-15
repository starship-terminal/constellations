# FeedHive patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

## Marketing chrome (light)

A fixed 38px promo bar (`component.promo-height`, `light.background.subtle` #f4f3f2, a 5%-black bottom hairline, 14px/600 Inter copy in #2d2f35) sits over an 80px transparent header (`component.header-height`, 20px/32px padding): the 118px FeedHive mark-and-wordmark, the Product / Agents & Automation / Socials / Learn dropdown triggers (14px/500 in `light.text.linkInk` #4f5562, anchors with `href="#"` and `aria-haspopup`), Pricing, the 40px neutral Login pill (`component.nav-pill-height`, `light.background.pillNeutral` #f4f2f0, `radius.navPill` 11px) and the 88px indigo Sign Up pill (`component.signup-pill-width`, `light.action.fill` #4457ff, `light.action.ink` white). A trigger opens a full-width 1440 x 316 white dropdown panel (`component.nav-panel-height`, `light.border.panel` #efefed hairlines) whose rows pair 48px icon tiles (`light.border.iconTile` #e8e7e4, 14px radius) with a 15px/600 label and a muted description, tracked caps group labels in #8b9098.

## Home (light)

The hero opens on the white page field (`light.background.page`): the "Introducing FeedHive v2.0" badge — a white 218 x 35 pill with a `light.border.input` #dfdfe4 hairline inside FeedHive's animated `.cta-gradient-ring` (`core.ctaRing.*`: the conic border rotates 0deg→1turn) — then the 55px/600 Plus Jakarta Sans masthead "Social media using Automation & AI Agents." (`font.size.measured.hero`, `font.tracking.display` -1.925px) with the second line in `light.action.fill`. The muted lede runs 16px in `light.text.muted` #666c77 (`font.tracking.lede`), then the 196 x 50 "Get started for free" CTA (`component.hero-cta-*`, `light.action.fill`, `radius.cta` 15px) and three checked feature rows. Beside it the product screenshot plays inside a 688 x 592 clip (`component.hero-mock-*`, `radius.card` 16px, overflow hidden). Below, the feature showcase switches a demo panel through dashed-border tab pills (`light.border.tab` #d8dbe2 at rest) that select into the indigo tint (`light.background.selectedTint` #eef2ff, `light.action.selectedBorder` #84a1ff, `light.action.selectedInk` #5a84ff, plus a bouncing check badge) — a local UI toggle, never a navigation. The agent/plugin cards are 585 x 416 #f6f6f8 tiles (`component.agent-card-*`, `light.background.card`, 15px radius, a white@70% inset top highlight) with Sometype Mono 700 kickers in brand indigo; headings drop to the 58px `font.size.measured.h2Section` step.

## Pricing (light)

/pricing keeps the same shell: a 64px masthead (`font.size.measured.h1Pricing`), then the gradient-ring "7-day free trial" badge beside the Monthly/Yearly pill (112 x 41 halves, `component.billing-toggle-*` — the unselected half reads `light.text.gray` #757b86, selection fills `light.action.selectedBg` #3347fb, the darker indigo step). The four plan cards are 297 x 652.5 articles (`component.plan-card-*`, `radius.card` 16px, 20/24px padding): Creator/Agency/Brand stay white on a #e8e4dd hairline while Business inverts to a full `light.action.fill` #4457ff card with white Plus Jakarta Sans 31px names (`font.size.measured.planName`). Each card closes with a 255 x 50 "Get started" CTA.

## Feature pages (light)

/features/scheduling (and /features/ai, same template) opens with the Sometype Mono tracked caps eyebrow ("SCHEDULING", 14px/700, `font.tracking.caps` +1.96px) over a 62px masthead (`font.size.measured.h1Feature`) and the 50px Get started CTA. The grid below paints 247 x 225 white feature cards (`component.feature-card-height`) on a 0.3s cubic-bezier(0.22,1,0.36,1) lift — hover grows the card ~2%.

## Blog (light)

/blog runs a 68px masthead (`font.size.measured.h1Blog`) over the featured card (1248 x 420, `component.blog-featured-height`) — a 652 x 367 media clip on `radius.card` 16px, an 11px/600 tracked caps "FEATURED POST" label in #516fe2, the #f6f6f8 meta tile — then the archive rows: 383 x 598 #f6f6f8 articles (`light.background.card`, `light.border.rule` #e7e8ec dividers) with 13px #6c7280 meta (`light.text.meta`).

## Tools (light)

/tools/bio-generator is the public form pattern: a 60px masthead (`font.size.measured.h1Tool`), then option chips — platform buttons (116 x 40, `radius.option` 9px, white on a #dfdfe4 ring shadow) and tone pills (36px, `radius.pill`, `light.border.input` hairlines, 13px #4c525e) — a 362 x 110 textarea (`component.bio-field-width`, `radius.field` 12px) and the 364 x 50 "Generate bios" submit (`component.bio-submit-height`), which rests in the desaturated `light.action.disabledFill` #b9c0f5 until the form has content. Fields were typed into and cleared; nothing was generated.

## The app sign-in/up (a different system)

app.feedhive.com/signin and /signup are a separate Chakra-UI app that shares no token layer with the marketing site — every value here is a `component.login.*` literal. The pale page frames a 512 x 610 white card (`component.login.panel-*`: 20px radius, a two-layer rgba(0,0,0,.1/.04) lift shadow, 44px padding, #1a202c ink). Inside: the FeedHive wordmark, "Let's get you signed in" at 18.4px/700, the 424 x 61 "Sign in with Google" outline pill (9999px radius, `component.login.field-border` #edf2f7, `component.login.control-shadow` rgba(27,25,121,.05) 0 2px 8px), an OR divider, 61px pill fields that trade the hairline for `component.login.field-focus` #3b82f6 on focus, then the 59px Sign in submit in `component.login.submit-fill` #3b82f6 behind a violet `component.login.submit-glow` (rgba(89,106,255,.28) 0 0 35px 10px). Links read `component.login.link` #5d60ec; controls transition at 0.2s ease rather than the marketing 150ms cubic-bezier. The fields were typed into and cleared; nothing was submitted.

## Mobile (390px)

The phone shell keeps the same system: a 76px header (`component.mobile-header-height`) with the mark and a 44px icon-only menu button (`component.mobile-menu-size`, aria-label "Open menu" → "Close menu") that swaps the viewport for a 390 x 844 `light.background.drawer` #fbfaf7 overlay — the same nav stack and pill pair, with #e8e4dd section rules. The masthead measures 46px (`font.size.measured.h1Mobile`, `font.tracking.display` -1.61px) and the hero CTA keeps its 196 x 50 profile.

## Motion and focus

Controls transition over the declared 150ms cubic-bezier(.4,0,.2,1) (`core.motion.control`, matching `duration.default` and `easing.default`); cards lift slower (0.3s) and the CTA gradient ring spins its `--cta-border-angle` 0deg→1turn. Keyboard focus is a thin outline, not a fill swap: marketing controls draw a 1px auto #101010 ring (offset 1px), the billing pill and mobile chrome draw it in #e59700, and the Chakra controls keep a 2px transparent outline at rest that resolves on focus — plus the declared `focus:ring-primary/20` wash (`light.focus.ring` rgba(68,87,255,.2)).
