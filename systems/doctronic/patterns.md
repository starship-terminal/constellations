# Doctronic patterns

How the measured components combine on doctronic.ai's public signed-out
surface, read from the screenshots and the component entries in
[components.md](components.md). Two rendering regimes share the site: the
app surfaces (home, `/chat/`, the symptom checker, the sign-in dialog)
are CSS-module components driven by the declared `--color-*` token layer,
and the content pages (blog, telehealth, authors, Wall of Love,
resource center) are Tailwind utility markup — though both paint the same
warm canvas, near-black ink and blue accent, and both set headings in
Fraunces.

## The warm paper field

Every page sits on `#fdfdf7` (`color.surface.canvas` → `neutral.50`), a
warm near-white, with `#1b1b18` ink (`color.fg.default` → `neutral.900`).
Borders are never a flat grey: the shared hairline is a 1px stroke at
8% ink (`color.border.default`), the 20% ink ring on secondary controls
is `color.border.strong`, and the menu drawer's dividers are drawn
*dashed* at that same 8% ink — a paper-and-ink signature that repeats
under the hero headline (its name is underlined with a dashed rule) and
in the drawer's section separators.

## The two top bars

The site ships two different headers.

The **app bar** (home, `/chat/`, symptom checker) is a 72px bar
([header](components/crops/header-default.png), `component.header.height`
72px): the doctronic wordmark
([logo](components/crops/logo-default.png)), then `Log in` — a quiet
secondary control whose `span.content` child paints a 32px-radius pill
with the 20%-ink ring — and `Sign up`, the same 32px pill filled
`#0b0b0a` near-black with `#fdfdf7` text (the *solid* role), then the
40 × 40 menu button. Every button on the site is built the same way: an
unpainted shell carrying `span.content` (the real fill) plus a
`span.shimmer` overlay that lights up on hover.

The **content bar** (blog, telehealth, authors, Wall of Love…) is a
shorter 56px sticky header
([mkt-header](components/crops/mkt-header-default.png)) painted in the
sage wash `#e2f0e4`: the wordmark, a row of full-round pill links
(About, FAQ, Blog, Online Treatment, Wall of Love, LegitScript —
[mkt-nav-pill](components/crops/mkt-nav-pill-default.png)) and the
near-black `Try Doctronic For Free →` pill
([try-button](components/crops/try-button-default.png), 215 × 40, Geist
14/500). No auth pair — the content pages' only entry into the product
is that single CTA.

## The site-menu drawer

The app bar's `open sidebar` button opens a 320 × 852 left drawer
([menu-drawer](components/crops/menu-drawer-default.png)) over a dimmed
page — see [home-light-menu](screenshots/home-light-menu.png). It is
organised as muted `label12` group captions (Dashboard, Explore,
Company) over 320 × 38 rows
([menu-item](components/crops/menu-item-default.png), 8px radius, Geist
16/22.4 at 500) with chevron rows for the expandable groups
(About Chat, Health Information —
[menu-item-expand](components/crops/menu-item-expand-default.png)),
separated by the dashed-ink dividers. Pinned at the bottom: the
`Sign up for free` near-black pill and `Log in` ringed secondary (both
224 wide), the HIPAA / Private & Secure badges and a `v1.x` build stamp.
Escape dismissed it; none of its rows was followed.

## The hero + chat-field pattern

The home page is built around one repeated component: the chat input
card. In the hero
([hero](components/crops/hero-default.png)) the Fraunces headline
([hero-title](components/crops/hero-title-default.png), Fraunces 48/56
regular, dashed underline) and lede sit above a lime prompt tab —
`What brings you in?`
([brings-pill](components/crops/brings-pill-default.png)) — that overlaps
the card's top edge like a folder label. The card itself
([hero-input-card](components/crops/hero-input-card-default.png), 548 ×
147) is the `surface.raised` recipe: white, 16px radius, 1px 8%-ink
border and `0 2px 24px rgba(0,0,0,.06)`, holding the textarea
([hero-textarea](components/crops/hero-textarea-default.png)), the
blue-text `Anonymous` session badge
([anon-label](components/crops/anon-label-default.png)) and the
`Start chat` button
([start-chat-button](components/crops/start-chat-button-default.png)):
the 52px-pill accent — `span.content` filled `#2463eb` (`accent.bg` →
`blue.600`) with the brand-glow shadow `rgba(36,99,235,.39) 0 4px 7px`
and white `heading14` text. Under it: `Free. Anonymous. Built by
doctors.` and the HIPAA & Private line
([hipaa-badge](components/crops/hipaa-badge-default.png)). The same card
repeats condensed near the footer
([condensed-form](components/crops/condensed-form-default.png)) with the
48 × 48 round accent submit
([condensed-button](components/crops/condensed-button-default.png)), and
on `/chat/` at 652 × 126
([input-card](components/crops/input-card-default.png)) with the 32 × 32
round Send
([send-button](components/crops/send-button-default.png)) — every accent
control on the site shares the 52px-pill shape and the blue glow. On the
symptom checker the card is a 24px-radius variant
([symptom-input-card](components/crops/symptom-input-card-default.png))
paired with a `Check My Symptoms` accent pill
([check-button](components/crops/check-button-default.png), 209 × 45,
same fill and glow). None of these submit controls was ever pressed.

## The chat surface

`/chat/` lays the product shell out: a 74px collapsed rail
([chat-sidebar](components/crops/chat-sidebar-default.png)) that its own
toggle ([sidebar-toggle](components/crops/sidebar-toggle-default.png))
expands to 256px
([chat-sidebar-open](components/crops/chat-sidebar-open-default.png)) —
the two widths are in the token file as
`component.sidebar-collapsed.width` / `component.sidebar.width`. In the
expanded rail the current row `New chat` paints the blue-50 wash
`#f0f6ff` with `blue.600` text
([nav-link-current](components/crops/nav-link-current-default.png));
sibling rows ([nav-link](components/crops/nav-link-default.png), 224 ×
36, 8px radius) stay ink on transparent. The rail's foot is the same
solid/secondary button pair as the drawer plus the support mailto and
the legal block. The centre column is the `Chat for free` empty state:
Fraunces 40px greeting
([chat-greeting](components/crops/chat-greeting-default.png)), the input
card, then four starter chips
([starter](components/crops/starter-default.png), 164 × 37, 8px radius,
`#f5f5f0` fill, `label14`) — measured, never pressed — and the
one-line medical disclaimer
([disclaimer](components/crops/disclaimer-default.png)). Typing into the
composer is the filled state
([chat-textarea](components/crops/chat-textarea-filled.png)); the text
was deleted again and Send never pressed.

## The sign-in dialog

`/?modal=signin` renders the auth card publicly
([chat-signin-light-signin](screenshots/chat-signin-light-signin.png)):
a 393 × 583 raised dialog
([signin-dialog](components/crops/signin-dialog-default.png)) on a dimmed
page (the overlay layer readings are in
[raw/measurements.md](raw/measurements.md) → Dialog backdrop). Fraunces
`display32` title, the green-cross artwork, then the 52px-pill `Log in
with email` accent
([email-login-button](components/crops/email-login-button-default.png),
329 wide) over three 40px-radius ringed OAuth buttons
([oauth-button](components/crops/oauth-button-default.png)), the
`Create an account` link
([create-account-link](components/crops/create-account-link-default.png))
and a 32 × 32 close button
([dialog-close](components/crops/dialog-close-default.png)). Everything
inside was measured, nothing pressed.

## Content-page idioms

- **Blog.** The Fraunces title + lede, a 730px search field
  ([blog-search](components/crops/blog-search-default.png)), then a cloud
  of tinted `rounded-full` category chips
  ([category-chip](components/crops/category-chip-default.png), ~77 × 28,
  lavender `#e6dbe6`) and a grid of 371 × 480 article cards
  ([article-card](components/crops/article-card-default.png)): 14px
  radius, `#e5e7eb` border, a 150px pastel gradient thumbnail with a
  centred glyph, and lime `Healthcare Costs`-style tag pills at
  `rgba(223,255,149,.8)` — the same lime as the hero prompt tab.
- **Authors.** A grid of 380 × 281 reviewer rows
  ([author-card](components/crops/author-card-default.png)) separated by
  `#e7e4de` hairlines: circular portrait, Fraunces 20px name + MD
  credential, bio, `View profile →`.
- **Wall of Love.** A `columns-3` masonry of
  [love-card](components/crops/love-card-default.png) tiles (405 wide,
  24px radius, `#fdfdf8` face over a `#f0ede9` inner block, 8%-ink
  border): avatar, first name, quote, and a `Love Reply Send message`
  footer row that mirrors a chat thread's chrome.
- **Resource center.** One long prose sheet
  ([resource-sheet](components/crops/resource-sheet-default.png), 690px
  wide, 16px radius, shadow-xl) — the only `prose` surface captured.

## Footer

Both header regimes share one deep footer
([footer](components/crops/footer-default.png), ~1415px tall): link
columns, the social icon row
([footer-social-icon](components/crops/footer-social-icon-default.png),
16 × 16), the legal row
([footer-legal-link](components/crops/footer-legal-link-default.png)) and
a gradient wash. A round `Pause animations` control
([pause-control](components/crops/pause-control-default.png), 40 × 40,
`#f5f5f0`) is pinned bottom-right and expands to 159px with its label on
hover.

## The dark theme

`data-theme="dark"` is a real user-selectable theme
(`localStorage.theme`); the token layer redeclares every semantic role
under it. The canvas goes `#0d0e0b`, the input card's face goes
`#1b1b18` with an 8% white border
([d-input-card](components/crops/d-input-card-default.png)), the accent
fill lifts to `blue.400` `#61a6fa` with `blue.950` text
([d-start-button](components/crops/d-start-button-default.png)), and the
solid pair inverts — `Sign up` becomes a white pill with ink text
([d-signup-button](components/crops/d-signup-button-default.png)).
Focus rings swap `blue.500` for `blue.400`. The app surfaces repaint
fully; the Tailwind content pages keep literal utility colours, so the
dark capture set is scoped to the token-driven surfaces — recorded as
such in the Gaps.

## Mobile

At 390px the app bar drops `Log in` and keeps `Sign up` + the menu
button ([m-header](components/crops/m-header-default.png)); the hero
collapses to a 342px column
([m-hero](components/crops/m-hero-default.png)) with the same card and
chips; `/chat/` trades the rail for a 67px mobile header
([m-chat-header](components/crops/m-chat-header-default.png)) and a
full-width input card
([m-input-card-chat](components/crops/m-input-card-chat-default.png)).
The drawer, footer and card recipes are unchanged — same radii, same
ink, same hairlines.

## The state signature

Hover states are quiet: fills deepen one step, the `span.shimmer` layer
lights the button sheen, links take the muted wash. Keyboard focus is a
`blue.500` 2px outline on most controls (`blue.400` on dark) — or a
`shadow.focus-ring` ring on the button family, whose 52px pill already
carries a glow. Pressed is a slight deepen on `accent.bg-pressed` /
`solid.bg-pressed`, all declared in the token layer.
