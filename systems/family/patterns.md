# Family patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

## Public chrome (light)

A 94px top bar (`core.component.topbar-height`, 96px wordmark `core.component.logo-width`) sits over a white page (`light.background.page` → `color.white`): Developers and Resources dropdown triggers (119px/113px pill labels), an X (Twitter) link, a beige **Log In** pill (`light.action.beige` `#f6f4ef`, ink text) and the near-black **Get Started** pill (`light.action.accent` → `color.overlay.background` `#171717`, white text `light.text.on-dark`, 32px radius `core.radius.button`). The dropdowns open small white cards (`nav-dropdown`, ~316 x 135, 8px radius, `0px 3px 16px rgba(0,0,0,.1)`) listing ConnectKit/Family under Developers and Blog/Changelog/Help & Support/FAQs under Resources — measured open, never followed.

## The hero

Home opens with the "Family" display face at 68px (`core.font.size.measured.display`, 44px at 390px `core.font.size.measured.mobile-display`) — "Your favorite crypto wallet." in `#343433` ink (`light.text.ink` → `color.heading`) — over a 15px Inter subline and two 48px pills: the black **Download on iOS** (a 209.7px pill, measured never followed — it goes to the App Store) and the beige **Watch the Video** pill beside it. Product videos (`/videos/*.mp4`: send, receive, swap, nft, watch, activity, onboarding, missioncontrol, dragdropdone, promo-collectibles) play inside the feature mockups further down.

## Feature sections and the demo overlay

Below the hero, a label/heading rhythm repeats: a coloured kicker (`light.text.kicker`, the 26px-high "Easy"/"Secure" labels), a 44px Family-face section heading (`core.font.size.measured.section`), Inter body copy at 15px in `light.text.muted` (`rgba(71,70,69,.7)`), and per-feature `h5` tags ("Send & Receive", "Wallet Activity"…). A **Watch the demo** button (314.69 x 68) mounts a full-viewport video overlay (`demo-overlay`, 1440 x 900) — a local overlay, measured open then closed.

## The testimonial marquee

"Friends of Family" runs a CSS-animated horizontal marquee of testimonial cards (`tweet-card`, 540 x 204 white panels, 10px radius, `light.background.card` → `color.white`, an inset `#f2f0ed` ring, 32px padding): avatar, author name and a social icon, each linking out to the tweet — measured, never followed.

## FAQ and footer

The FAQ is a stack of collapsible rows (`faq-item`, 512 x 56) on `#f2f0ed` hairlines (`light.border.hairline` → `color.gray.light`) with a 14px toggle (`core.component.faq-toggle`) that draws a focus-visible ring. The sitemap footer closes every page (`site-footer`, ~1024 x 316; `m-footer` 342 x 505 on mobile).

## Content surfaces

- **/blog**: a 44px "Blog" Family-face title, topic filter pills (`blog-filter`, 43 x 33 "All"/"News"/"Wallet" — the opened state is a local toggle), then 1024 x 280 post cards (`blog-card`, `core.component.post-card-width`) on bottom hairlines, each with a date/tags meta line (`blog-date`, `light.text.low` → `color.body.muted` `#848281`).
- **/blog/\<post\>**: 44px article title (`core.font.size.measured.article`), `h2` subheads, Inter body, a back link (`post-back`).
- **/changelog**: the same filter/card rhythm with dated release entries.
- **/support**: a search field (`sup-search`, `core.component.search-field-width` ~269px — typed and cleared, never submitted) over category buttons and article links.
- **/faqs, /legal, /docs, /docs/connectkit, /docs/family-account**: the same Family-face h1 + hairline list layout; the docs carry the ConnectKit and Family Accounts (Aave Account) developer content with CTA pills and side links.

## The Aave Account login

app.family.co/ paints the app layer on light: a 380px login card (`core.component.login-card-width`, 14px radius) on a white field — an "Aave Account" heading and subtitle in variable Inter (`core.font.family.app`), a 380px borderless transparent field (`light.background.field`; its fill is the declared `light.color.input.background.default` `#f6f7f9` on the wrapper) that was typed into and cleared, a **Learn More** pill — near-black `#121212` text on a warm `#f9f7f5` fill, 18px radius (the app's declared `--hyperlink-color` violet `#9896ff` → `color.app.primary` is the link default nothing here paints) — and a footer link. The app draws its own focus ring — a blue `rgba(0,122,255,.5)` (`--focus-color` → `color.focus.color`) vs the marketing `#848281` ring (`light.border.focus` → `color.focus.default`). Past this card is the authenticated product — a documented boundary.

## Mobile (390px)

The phone surface is the same light theme: a 70px compact header (`core.component.mobile-topbar-height`), a 32px hamburger (`m-menu`) that swaps the document for a full-screen drawer (measured `mobile-home-light-drawer`), the same pills and hairline FAQ. The display heading drops to 44px (`m-h1`).

## Motion and focus

Both surfaces ship real motion: the app declares `--duration-swift-out` 0.22s / `--duration-snappy-out` / `--duration-overshoot-out` with matching `--ease-*` cubic-bezier curves (`core.duration.*`, `core.easing.*`) and a 0.3s field opacity transition; marketing controls run 0.1s-0.2s ease transitions. Focus-visible is a 2px outline ring — `#848281` on marketing, `rgba(0,122,255,.5)` blue on the app. Pressed states are DevTools-forced `:active` and may not match real mousedown.
