# Front patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

## Marketing chrome (light sections)

The 80px header (`component.marketing.header.height`, `mkt-header`) carries the Front wordmark (`mkt-logo`, 112x26), the Product/Solutions/Resources mega-menu triggers (`nav-menu-btn`, 90x40 buttons), the Pricing link (`nav-pricing`, 84x40), then Sign in (`nav-signin`, 82x40) and two actions: "Request a demo" (`nav-demo`, 153x40, the bordered `button-primary-white`) and "Try for free" (`nav-try`, 111x40, `button-secondary-violet-300` on the plum hero, repainting per section theme). The Product trigger opens a full-width mega panel (`nav-panel`, 1271x419 — the `rounded-20` bordered flyout with product entries like Platform Overview, Autopilot, Copilot, Omnichannel, `nav-menu-item`); its links were measured, never followed. The Solutions and Resources panels are screenshot-captured only. The Qualified "Quinn" launcher pins bottom-right — a vendor surface, measured at rest, never opened.

## Home — the three section themes alternate

The home page stacks sections under `[data-theme]` contexts that repaint the same role names. The hero sits on `violet.surface.l0` (#300c41, theme-dark-violet plum) with `violet.text.primary` (#f8f1fe) display type (`hero-h1`, 840x104 — the responsive `font-size-d3` utilities measured 43px/52px at the desktop break; the nearest declared ramp step is `core.font.size.display3` 42px over `core.font.lineHeight.display3` 52px) and `violet.text.secondary` subcopy; its single CTA is "Request demo" (`hero-cta`, 140x48 — `component.marketing.button.hero.height` 48px, a `rounded-[64px]` pill painted `violet.surface.highlight` #dee948 — the citron accent — with `violet.button.textDefault` ink). Down the page, theme-white sections paint `light.surface.l0` #fff behind `light.text.primary` #0d1d39 ink and theme-gray sections `gray.surface.l0` ~#f3f3f4 (`gray-section`, `dark-violet-section` measured 1440x952 / 1440x404 as surfaces). Customer-outcome stat rows and feature grids sit inside these alternating fields; the footer (`footer`, 1440x1481) closes on the plum theme with `footer-link` items.

## Pricing

/pricing leads with the "Billed Annually" / "Billed Monthly" switch (`billing-toggle`, 66x36 — a `label`-wrapped checkbox whose visual track paints the toggle; toggled and restored as a local UI change) that re-prices the plan grid. The plan cards are white `rounded-[24px]` columns (`plan-card`, 313x460, `component.marketing.planCard.bg`/`.radius`) each carrying a full-width "Try for Free" action (`plan-cta`, 265x40, `component.marketing.planCta.bg`); "Talk to sales" (`sales-link`, 121x26) is the enterprise contact. FAQ disclosures (`faq-item`, 872x100 buttons such as "What is a seat?", opened measured, `faq-answer` revealed below) close the page — all local UI toggles. The page carries no `h1`; `pricing-h1` records the first heading (`h2`).

## Forms

/request-demo is a two-field edge: the work-email input (`demo-email`, 576x48, `component.forms.demoEmail.height`/`.bg`), the company-size select (`demo-field`, 576x48) and the Continue submit (`demo-submit`, 576x48 — `component.forms.demoSubmit.height`, a `rounded-[64px]` pill painting its disabled gray until the fields validate). /signup is a single email field (`signup-field`, 480x48) plus its submit (`signup-submit`, 480x48 — `component.forms.signupSubmit.height`, the same `rounded-[64px]` pill pattern). The app shell's own /signup card submits with `signup-app-submit` (234x38, `component.forms.signupAppSubmit.height`) — a separate key from the marketing `signup-submit`, which it used to overwrite. Both were typed into then cleared — never submitted — so validation, error and success states are unmeasured.

## The auth shell, light and dark

app.frontapp.com paints the product's real `--color-*` token layer. The signin card (`app-panel`, 332x577 on `app.color.bg.surface.primary.default`) holds Email and Password fields (`app-email`), the submit (`app-continue`, 234x38 on `app.color.bg.fill.brand.default`, reads "Sign in"), the "Forgot password?" link (`app-forgot`, 234x16), an "or continue with" divider and three SSO buttons (`app-sso`, Google / Office 365 / SAML SSO at 234x38). `/signup` and `/forgot-password` routes paint the same card — `signup-*` and `forgot-*` components document that honestly. The dark pass (`appd-*` keys) is the same card under `html[data-theme="dark"]` via the shell's own `front-theme-preference` key — verified painted before measuring, never an emulated palette.

## Help centre (Front's Knowledge Base product)

help.front.com is a third stack: the KB product's own chrome (`help-header`, 1440x306 — mark, nav, and the hero search `help-search`, 408x40, typed into then cleared) over the `help` token set's `--primary-color`/`--gray-shade*`/`--article-*` `:root` block. The home lists category cards (`help-card`/`help-card-2`, 402x259 `kb-category-card` anchors — Getting started, Using Front, Rules, API & integrations, Community, Academy…), not article links; an article was reached by one reader's own click (`helpa-h1`, `helpa-body`, `helpa-crumb`). The pages embed the Companion/Froyo token sheet (`companion`/`companionDark` sets), Front's messenger design language in transit.

## Developer portal (ReadMe vendor)

dev.frontapp.com is a fourth stack — ReadMe — skinned to Front: the portal header (`dev-header`, 1430x94), the search trigger (`dev-search`, 150x32), the docs sidebar links (`dev-side-link`, 251x32) and code blocks (`devref-code`). Its `--color-*` overrides are vendor values kept in `raw/css-vars.json` under `vendor`, not promoted to tokens. The portal scrolls inside a container, so `dev-*-full-scroll` shots are the article column at content height.

## Mobile (390px)

The phone surface keeps the same system: a 96px top bar (`m-topbar`) with the wordmark, CTAs and the `m-menu-btn` burger (44x44, `button-mobile-menu-trigger`, aria-label "Open menu") toggling a full-viewport nav overlay (`m-drawer`, 390x844) — opened via its own click, Escape-closed. The hero shrinks (`m-hero-h1`, 358x184) and the "Request demo" CTA (`m-cta`, 167x40) follows.

## Motion and focus

Marketing controls transition over the declared `.duration-100..1000` and `.ease-appear` (cubic-bezier(0.16,1,0.3,1)) classes — the `core.motion.*` tokens. The reduced-motion probe found the marketing pages largely ignore `prefers-reduced-motion: reduce` (transitions kept; `raw/motion.json`) — an honest absence, not a variant. Focus is a visible outline on keyboard focus-visible across nav, plan CTAs, FAQ and auth controls, measured per component.

## The dark set is the app's, the companion sets are embedded

There is no marketing dark mode: `violet`/`light`/`gray` are section themes of one light marketing page. The `dark` token set is the auth shell's real `data-theme="dark"` repaint of the same `--color-*` names, and `companion`/`companionDark` are the Froyo messenger layer's own light/dark semantics — four honest layers, never merged.
