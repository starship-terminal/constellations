# Cal.com patterns

How the measured components combine on cal.com's public surface, read from
the screenshots and the component entries in [components.md](components.md).
The capture spans three hosts: the light marketing pages on cal.com (home,
pricing, features, teams, enterprise, customers, blog, faq), the public
booking page on i.cal.com (cal.com/peer — light, plus its supported
`?theme=dark&embed=true` dark mode) and the light auth cards on
app.cal.com. Values are from the light set unless marked `dark` or `booker`.

## The floating glass bar

Every marketing page carries the same chrome
([header](components/crops/header-default.png), 64px high, 18px radius): a
72%-white `#f4f4f4` glass bar inset from the viewport edges holding the
wordmark ([logo](components/crops/logo-default.png)), the `Products`,
`Use cases`, `Features` and `Resources` mega-menu triggers
([nav-trigger](components/crops/nav-trigger-default.png), calSans 14/21 at
weight 500 on a 10px radius), the plain `Enterprise` and `Pricing` links
([nav-link](components/crops/nav-link-default.png)), a `Talk to sales` row
with an avatar cluster, `Sign in`, and the `#242424` `Get started` pill
([nav-cta](components/crops/nav-cta-default.png), 36px high on a 12px
radius with a white inset top line). Clicking a trigger opens a 955 x 519
mega-panel ([nav-dropdown](components/crops/nav-dropdown-default.png),
[home-light-menu](screenshots/home-light-menu.png)): product cards on the
right — 200 x 220 tiles each holding a thumbnail, the name and a one-line
blurb ([menu-link](components/crops/menu-link-default.png), 4%-ink hover
wash) — beside a booking-app preview card and a NEW release link. Keyboard
focus draws a 1px white gap then a 3px `#9ca3af` ring on every control
(`core.measured.focus-ring`).

## The home hero

The home page opens on white ([home-light-default](screenshots/home-light-default.png)):
the `NEW · Cal.com launches` release pill
([changelog](components/crops/changelog-default.png), 8px radius, 11px
label), the 80px/86.4 `Where people find the time to meet` display
([hero-title](components/crops/hero-title-default.png), weight 700, -0.8px
tracking, photo/clock/badge chips embedded inside the headline itself), a
20/28 lede in `#6a6e78` ([hero-sub](components/crops/hero-sub-default.png))
and two 64px sign-up buttons on 14px radii — dark `#242424` for Google
([hero-google](components/crops/hero-google-default.png)) and white with an
`#e5e7eb` ring for Microsoft
([hero-microsoft](components/crops/hero-microsoft-default.png)) — over the
quiet `Sign up with email.` link
([hero-email](components/crops/hero-email-default.png)). Below the fold a
mock OS window shows a booking page
([hero-mock](components/crops/hero-mock-default.png),
[home-light-full](screenshots/home-light-full.png)).

## Pricing

`/pricing` centres `Pricing that scales` at 64px
([pricing-h1](components/crops/pricing-h1-default.png)) over a muted
sub-line ([pricing-sub](components/crops/pricing-sub-default.png)) and the
plan tabs — `Individuals`/`Teams`/`Enterprise` at 22px weight 700
([plan-tab](components/crops/plan-tab-default.png)) — plus the MONTHLY /
YEARLY capsule switch
([billing-toggle](components/crops/billing-toggle-default.png)).
[pricing-light-teams](screenshots/pricing-light-teams.png) and
[pricing-light-monthly](screenshots/pricing-light-monthly.png) show the
toggled states. White 312 x 598 plan cards follow on the page field
([plan-card](components/crops/plan-card-default.png)): 14px radius on a
`#dee1e6` hairline, a 19px plan name, the feature list and the dark 36px
`Use for free`/`Get started` action
([plan-cta](components/crops/plan-cta-default.png)); Enterprise cards swap
it for a `Talk to sales` link
([sales-cta](components/crops/sales-cta-default.png)). A feature accordion
of 22px questions runs below
([feature-accordion](components/crops/feature-accordion-default.png)) —
measured closed, never expanded. Prices were never followed to checkout.

## The public booking page

cal.com/peer serves Peer Richelsen's `15 Minute Meeting` from i.cal.com
([booking-light-default](screenshots/booking-light-default.png)): Inter
throughout, three zones on the white `--cal-bg` canvas. A left card carries
the `Own Your Time` cover, the host avatar, `Peer Richelsen`, the 20/28
event title ([bk-title](components/crops/bk-title-default.png), weight
600), the `With Peer Richelsen, Co-Founder` blurb
([bk-host](components/crops/bk-host-default.png)) and meta rows —
`Requires confirmation` ([bk-badge](components/crops/bk-badge-default.png)),
`15m`, `Cal Video` and the `Asia/Singapore` timezone dropdown
([bk-meta](components/crops/bk-meta-default.png)). The centre holds the
month grid ([bk-calendar](components/crops/bk-calendar-default.png),
MON–SUN header): 59px day cells on 8px radii, today painted `#292929` with
white text ([bk-day-today](components/crops/bk-day-today-default.png)),
bookable days `#e5e7eb` with `#070a0d` numbers
([bk-day](components/crops/bk-day-default.png)), past days faded. Picking a
day reveals the right column's slot list under a `12h`/`24h` toggle
([booking-light-slots](screenshots/booking-light-slots.png)): 239 x 36
white buttons on 10px radii with `#d1d5db` borders and a soft drop
([bk-slot](components/crops/bk-slot-default.png), `#f6f7f9` hover, pressed
flips its shadow to a top inset). A slot press opens the guest-details
form in place ([booking-light-form](screenshots/booking-light-form.png)):
371px wide, 32px `#d1d5db`-ringed fields
([bk-field](components/crops/bk-field-default.png)) and the `#292929`
Confirm action ([bk-confirm](components/crops/bk-confirm-default.png)) —
measured, never filled or confirmed.

## The dark booker

The booker is the only surface that paints dark signed out, under its
supported `?theme=dark&embed=true` mode
([booking-dark-dark-default](screenshots/booking-dark-dark-default.png)):
the same tree re-resolves — `#0f0f0f` canvas, `#262626` subtle fills,
`#4d4d4d` borders, `#d4d4d4` text
([bkd-canvas](components/crops/bkd-canvas-default.png),
[bkd-title](components/crops/bkd-title-default.png),
[bkd-calendar](components/crops/bkd-calendar-default.png),
[bkd-slot](components/crops/bkd-slot-default.png) — the dark slot is
`#0f0f0f` on `#4d4d4d`). `tokens.json` keeps these roles in the `dark` set.

## The auth cards

app.cal.com's signed-out cards mark the product boundary, light only,
fontSans body with fontHeading display
([login-light-default](screenshots/login-light-default.png),
[signup-light-default](screenshots/signup-light-default.png)). The 446px
login card ([auth-card](components/crops/auth-card-default.png)) stacks the
`Welcome back` heading
([auth-title](components/crops/auth-title-default.png)), a 36px `#262626`
`Sign in with Google` button
([sso-google](components/crops/sso-google-default.png)), 30px
`#d1d5db`-ringed email/password fields
([email-field](components/crops/email-field-default.png),
[pass-field](components/crops/pass-field-default.png)), the `#696969`
`Forgot?` link ([forgot-link](components/crops/forgot-link-default.png)),
the dark `Continue` action
([continue-btn](components/crops/continue-btn-default.png)) and a SAML
link ([saml-link](components/crops/saml-link-default.png)). Signup pairs
the same controls — 40px on 14px radii
([signup-google](components/crops/signup-google-default.png),
[signup-email](components/crops/signup-email-default.png)) — with a 56px
`Claim cal.com/you` fontHeading title
([signup-title](components/crops/signup-title-default.png),
[signup-card](components/crops/signup-card-default.png)) and a
Trustpilot/Product-Hunt rating row
([trust-row](components/crops/trust-row-default.png)). Every field and
action measured, never filled or followed.

## The footer

A near-black `#111111` field closes every marketing page
([footer](components/crops/footer-default.png), 1487px of link columns,
app-store badges and social links at 60%-white —
[footer-link](components/crops/footer-link-default.png)).

## At 390 wide

The marketing surface stacks: the same glass bar narrows to 374px
([m-header](components/crops/m-header-default.png)) with a 36px menu
button ([m-menu-button](components/crops/m-menu-button-default.png)) that
opens a full-screen white drawer
([m-menu-open](components/crops/m-menu-open-default.png),
[mobile-home-light-menu](screenshots/mobile-home-light-menu.png)) of 48px
link rows ([m-nav-item](components/crops/m-nav-item-default.png)). The
display drops to 42px ([m-hero](components/crops/m-hero-default.png),
[mobile-home-light-default](screenshots/mobile-home-light-default.png)),
and the booker keeps its column layout scrollable
([mobile-booking-light-default](screenshots/mobile-booking-light-default.png)).
