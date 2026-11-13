# ElevenLabs patterns

How the measured components combine on elevenlabs.io's public signed-out
surface, read from the screenshots and the component entries in
[components.md](components.md). Every surface paints light — the `#FDFCFC`
eggshell field with white cards — and the site ships no dark theme or dark
island; the gradient voice orbs are painted media, not CSS.

## The chrome: promo strip over a quiet nav

Every desktop page opens on a 48px promo strip
([announcement](components/crops/announcement-default.png)): a `#f5f3f1`
band under a 0.5px `rgba(0,0,0,0.1)` hairline, with Inter 14/18 ink copy
and a small white 9999px pill link (the "Meet Eleven v4" bar on home, a
$1-credits countdown on the product pages — live timers, point-in-time).

Below it sits the light nav ([nav](components/crops/nav-default.png),
36px tall): the ElevenLabs wordmark
([logo](components/crops/logo-default.png), a 117 x 15 icon inside a
141 x 36 pill-padded anchor), the flyout triggers Products / Solutions /
Customers / Resources
([nav-trigger](components/crops/nav-trigger-default.png), Inter 14/20 at
36px, taking a `rgba(41,37,36,0.05)` wash on an 18px-radius inner chip on
hover and a `1px solid #2b7fff` ring at 2px offset on focus), the plain
Enterprise / Pricing links
([nav-link](components/crops/nav-link-default.png), same wash language),
then the auth pair — `Log in` as a ghost
([login-link](components/crops/login-link-default.png)) and `Sign up` as
the black pill ([signup-cta](components/crops/signup-cta-default.png),
78 x 36, `#000000` fill taking `#44403b` on hover and pressed, white
14/21 label).

The `Products` trigger opens a 940 x 565.5 mega-menu
([nav-dropdown](components/crops/nav-dropdown-default.png)) — see
[home-light-menu](screenshots/home-light-menu.png): a white panel holding
the Overview / ElevenCreative / ElevenAgents / ElevenAPI columns with
warm-grey link rows ([menu-link](components/crops/menu-link-default.png),
Inter, `rgb(119,113,105)` `#777169` muted text). The menu auto-closes a
few seconds after opening — every flyout reading re-opened it first.

A fixed voice-chat launcher
([voice-chat](components/crops/voice-chat-default.png), ~157 x 56) sits
bottom-right on home and the product pages — measured, never opened: the
agent session may count as a service interaction.

## The home hero: product tabs over the orb field

The hero centres `Bringing technology to life` in Waldenburg 48/52
([hero-title](components/crops/hero-title-default.png), ink on eggshell)
with a 16/24 lede ([hero-sub](components/crops/hero-sub-default.png)) and
the black-pill `Sign up` CTA
([hero-cta](components/crops/hero-cta-default.png), ~86 x 40, 9999px,
`#000` fill → `#44403b` hover/pressed).

Under it, two tab registers switch the showcase:

- the wide **product tabs** `ElevenAgents` /
  `Text to Speech` etc.
  ([product-tab](components/crops/product-tab-default.png), 389 x 44 at a
  12px radius, `rgb(68,64,59)` labels) — the ElevenAgents state is
  [home-light-agents-tab](screenshots/home-light-agents-tab.png);
- the pill **tool tabs**
  ([tool-tab](components/crops/tool-tab-default.png), 142 x 40 at 9999px)
  whose selected/hover state paints a `#ebe8e4` warm-grey fill on an
  absolutely-positioned layer behind the label.

## The TTS playground on the front door

The home page embeds a working demo — the signature ElevenLabs pattern, a
product you can touch before the account. A ~530 x 208 card
([tts-card](components/crops/tts-card-default.png)) holds a 530 x 136
textarea ([tts-textarea](components/crops/tts-textarea-default.png), Inter
16/24, typed into during the capture), the language and voice selects
([tts-language](components/crops/tts-language-default.png),
[tts-voice](components/crops/tts-voice-default.png), pill controls taking
a 2px `#2b7fff` focus ring), and the black-pill Play
([tts-play](components/crops/tts-play-default.png), ~58 x 36). Play was
pressed once in the shot pass — it generated without an account, a public
affordance; see
[home-light-playground](screenshots/home-light-playground.png) and
[home-light-playground-play](screenshots/home-light-playground-play.png).

The same demo language repeats on `/text-to-speech` with a breadcrumb h1
([tts-h1](components/crops/tts-h1-default.png), 15px) over the 36px
display heading
([tts-display](components/crops/tts-display-default.png), "Text to Speech
with high quality, human-like AI voices"), the `Log in with Google`
black pill ([google-login](components/crops/google-login-default.png)),
the ink `Convert` CTA
([convert-cta](components/crops/convert-cta-default.png)), and voice
sample cards ([voice-card](components/crops/voice-card-default.png)) with
their own sample-play buttons
([card-play](components/crops/card-play-default.png)) and `Try this
voice` CTAs ([try-voice](components/crops/try-voice-default.png)) — the
play buttons measured, never pressed.

## Pricing: pills, a dropdown, white cards on hairlines

`/pricing` opens on a 48/52 display title
([pricing-h1](components/crops/pricing-h1-default.png), "Flexible pricing
for your needs"), the product pill selector
([product-pill](components/crops/product-pill-default.png), `#777169`
muted label) and the Monthly billing dropdown
([billing-select](components/crops/billing-select-default.png), 168 x 44
pill with a layered `rgb(215,210,204)` ring shadow — the open state is
[pricing-light-billing](screenshots/pricing-light-billing.png)).

The grid is a row of ~262 x 739 plan cards
([plan-card](components/crops/plan-card-default.png)) — white surfaces on
`#e5e5e5` hairlines at the declared `--rounded-card` 16px radius — each
stacking a `rgb(15,15,16)` title, a 20/27 price figure
([plan-price](components/crops/plan-price-default.png)), a `#a3a3a3`-meta
badge ([plan-badge](components/crops/plan-badge-default.png), 13px), the
full-width black-pill CTA
([plan-cta](components/crops/plan-cta-default.png), 262 x 44,
`#000 → #44403b → ~0.98` pressed scale) and the feature list
([feature-row](components/crops/feature-row-default.png), rows that take
a `#ebe8e4` wash on hover). FAQ accordions
([faq-item](components/crops/faq-item-default.png), 724 x 52.5 at a 4px
radius) close the page. Every CTA was measured, never followed — no
checkout surface was reached.

## The supporting pages

`/conversational-ai`, `/sound-effects`, `/api` and `/enterprise` replay
the same grammar: display title + lede + ink CTA + secondary ghost +
media artwork. The API page's `Get API key`
([apikey-cta](components/crops/apikey-cta-default.png)) and `Explore the
docs` ghost ([explore-docs](components/crops/explore-docs-default.png))
are the black-pill/white-ghost pair again; its demo/code switch
([demo-tab](components/crops/demo-tab-default.png)) is the pill tab. The
announcement strip here reads the $1-credits countdown instead of the V4
bar. `/about` and `/blog` keep the same chrome over the editorial media —
see [about-light-full](screenshots/about-light-full.png),
[blog-light-default](screenshots/blog-light-default.png).

## Docs: the Fern register

`/docs` is a different product surface — a docs shell with its own 36px
search field ([docs-search](components/crops/docs-search-default.png),
632 x 36 at an 8px radius, `rgba(0,0,0,0.608)` placeholder, a
`rgba(255,255,255,0.8)` kbd chip and a `rgba(0,0,0,0.06)` hover fill), a
left nav ([docs-nav-item](components/crops/docs-nav-item-default.png),
`rgba(0,0,0,0.875)` ink taking a `2px solid #404040` focus ring — the
docs' own ring colour, not the site's blue), the docs title
([docs-h1](components/crops/docs-h1-default.png)) and a `Copy page`
utility ([docs-copy-page](components/crops/docs-copy-page-default.png)).
Same families, smaller radii, a second focus colour — treat the docs
chrome as its own dialect. See
[docs-light-full](screenshots/docs-light-full.png).

## The auth cards: the second dialect

`/app` redirects to `/app/sign-in`, which renders a 360 x 519 white card
([signin-card](components/crops/signin-card-default.png)) — `rgb(15,15,16)`
ink, "Welcome back" heading, `Sign in with Google` / `Sign in with SSO`
buttons ([oauth-google](components/crops/oauth-google-default.png),
[oauth-sso](components/crops/oauth-sso-default.png), 360 x 46 at 12px,
`#2e2e2e` labels, `rgba(0,0,0,0.02) → 0.043` washes), then the email
([email-field](components/crops/email-field-default.png)) and password
([password-field](components/crops/password-field-default.png)) fields —
360 x 46, 12px radius, `1px rgba(0,0,0,0.1)` border — and the disabled
submit ([signin-submit](components/crops/signin-submit-default.png),
`#a3a3a3` resting state, faster 0.075s transition). `/app/sign-up` is the
same card taller (601px,
[signup-card](components/crops/signup-card-default.png)) with the ToS
checkbox ([tos-checkbox](components/crops/tos-checkbox-default.png), 16 x
16, `rgba(0,0,0,0.714)` label). Fields were focused and sample-filled,
then emptied — the submits stayed disabled and were never pressed; the
OAuth buttons leave for the providers and were never followed.

## The footer and the phone pass

The light footer (uncaptured as a component this pass — see Gaps) closes
every page with product / company / resources columns, social glyphs and
legal over the same eggshell field; it is visible in the `-full` shots,
for example [home-light-full](screenshots/home-light-full.png).

At 390 wide the chrome collapses to a 117px-wordmark header
([m-header](components/crops/m-header-default.png)) with a 36px menu
button ([m-menu-button](components/crops/m-menu-button-default.png)) that
opens a full-width menu ([m-menu-open](components/crops/m-menu-open-default.png),
390 x 732) of 366 x 44 rows
([m-nav-item](components/crops/m-nav-item-default.png), Inter 14/20) plus
the black `Sign up` pill
([m-signup](components/crops/m-signup-default.png)) — see
[mobile-home-light-menu](screenshots/mobile-home-light-menu.png). The
hero drops to Waldenburg 36/42
([m-hero](components/crops/m-hero-default.png), 350 x 68) and the
playground keeps its card. Mobile coverage: home (default, menu, full —
stitched from three chunks), pricing (default, full) and text-to-speech
(default).

## The state signature

Two mechanics carry every interactive surface: the **ink ramp** — black
pills step `#000000 → #44403b` on hover *and* pressed (the same warm-dark
step, with a ~0.98 press scale on the big CTAs) — and the **warm washes**
— `rgba(41,37,36,0.05)` on nav chips, `rgba(0,0,0,0.02) → 0.043` on the
auth ghosts, `#ebe8e4` behind selected tabs and feature rows. Focus is a
`1px solid #2b7fff` ring at 2px offset almost everywhere (2px on the
playground selects; the docs shell uses `2px #404040`; a few fields draw
a shadow ring instead), and controls transition on a shared 0.15s
`cubic-bezier(0.4,0,0.2,1)` clock (0.075s inside the auth card). Nothing
on the public surface is ever disabled except the auth submits, and no
error or loading state exists to capture — the boundary of a signed-out
read.
