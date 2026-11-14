# Designmodo patterns

How the components in [components.md](components.md) combine into the public surfaces. Designmodo runs two systems on one domain — the InterVariable marketing surface and the Fira Sans Postcards app — and both are read signed out. Every value is in [tokens.json](tokens.json); the crops are in [components/crops/](components/crops) and the page captures in [screenshots/](screenshots).

## The marketing chrome

Every marketing page carries a 70px top bar (`component.topbar-height`) over the dark hero band: the designmodo wordmark, product dropdowns (Products, Bundles, Articles), a Log in link, and the 94x38.5 `#f49a40` orange Sign Up Free pill (`light.action.orange`, `core.radius.pill`) that deepens to `#f18110` on hover (`light.action.orange-hover`). Nav text paints white on the dark band (`light.text.on-dark`). At 390px the bar stays 70px (`component.mobile-topbar-height`) and the links collapse behind a burger.

## The dark hero band

The home hero is a dark `#071c26`-family band carrying a 498px-wide, 56px InterVariable display (`core.font.size.measured.display`) in white (`light.text.on-dark`), a muted `#c3cecb` sub-line (`light.text.muted-mkt`), and the 164x53 `#27ae60` green Open App pill (`light.action.accent`, `core.radius.pill`, `component.cta-height`) that deepens to `#1e8449` on hover and pressed (`light.action.accent-hover`). Product pages (/postcards) run the same band with a 91.5px display (`core.font.size.measured.mega`) and the near-black `#0d1d24` 20px CTA (`light.action.dark`, `core.radius.product`, `core.font.size.measured.product-cta`) that flips to `#fb754b` coral on hover (`light.action.dark-hover`).

## The welcome-modal gate

/postcards/app/folder/templates is the signed-out app route: the gallery renders fully in the DOM and a 423px "Welcome back!" modal (`component.modal-width`, `light.background.modal`) sits over it on a dimmer, casting the one measured shadow (`core.shadow.modal`). The modal is a Fira Sans card on the app stack: the full-width 343px Continue-with-Google button (`component.modal-btn-width`), an email field, the 8px-radius `#27ae60` Login (`light.action.accent`, `core.radius.modal-btn`) and the `#e8ecf0` secondary Create Account (`light.action.secondary`). Escape dismisses the modal locally — the gallery behind it is real UI, measured through it; no action was submitted.

## The app shell

Behind the modal the Postcards app is a rectilinear Fira Sans surface on a `#f4f4f4` canvas (`light.background.paper`): the 60px `#071c26` navy header (`component.appbar-height`, `light.background.navy`) holding the blue `#2198ed` 94x40 Login pill (`light.action.blue`, `core.radius.app`) whose hover swaps to `#485f6b` slate (`light.action.dark-hover`), the `#485f6b` Sign Up, and a search field. Below sits the 241px workspace sidebar (`component.sidebar-width`) — Drafts, Templates (selected in `#2198ed`, `light.text.link`), Workspace Settings — next to the gallery: a green `#27ae60` + Create split button, 15px `#585d63` filter labels (`core.font.size.measured.filter`, `light.text.muted`), and a grid of 266x592 template cards (`component.tpl-card-width`, `component.tpl-card-height`) carrying 9px badges — `#2198ed` FREE and `#27ae60` NEW (`core.font.size.measured.badge`, `component.badge-height`, `component.free-badge`).

## Pricing

/postcards/pricing runs the 91.5px InterVariable display (`component` 1180x102 heading) over a tinted field: 313px near-white plan cards (`component.plan-card-width`, `light.background.card`, `rgba(247,249,252,.9)` over the tint) listing plan features in `#101d24` ink (`light.text.ink`), each closing on the 233px plan action (`component.plan-cta-width`). The same near-black `#0d1d24` CTA treatment as the product pages applies.

## The sign-in form

/my-account/sign-in/ is the auth boundary: a centered 380x562 card on white holding 380x50 fields (`component.field-width`, `light.background.field`) at 5px radius (`core.radius.form`), a 24px heading (`core.font.size.measured.section`), the `#2f80ed` Login button paired with a sign-up link (two 186px actions, `component.auth-submit-width`) that deepens to `#1366d6` on hover (`light.action.auth-blue-hover`), and the terms links. Every control was measured; the fields were typed into and cleared and Login was never pressed.

## Email-template gallery

/email-templates is the public marketing gallery: the 63px page display (`core.font.size.measured.tpl-display`), then rows of the same template-card shape as the app gallery with the 9px FREE/NEW badge pair.

## The footer

The marketing footer paints white over the page field with `#313942` body ink (`light.text.ink-body`, `core.font.size.measured.body`) — sitemap columns under the wordmark. On the phone it stretches to ~1387px.

## Focus language

Controls take the browser's default outline on focus-visible; no custom focus-ring colour is painted on the public surface. The app Login pill's focus-visible reading keeps its `#2198ed` fill while hover/pressed go slate — the focus look is the default look.

## Mobile

At 390px the marketing bar holds at 70px, the display drops to 44px (`core.font.size.measured.mobile-display`), and the Open App pill repeats as `m-cta`. The app route keeps its structure — navy header, sidebar, gallery — inside a nested scroller 14521px tall; the capture capped it at 8 viewport tiles (6752px), a recorded boundary.
