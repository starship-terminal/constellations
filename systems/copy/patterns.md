# Copy.ai patterns

How the measured components combine on copy.ai's public signed-out
surface, read from the screenshots and the component entries in
[components.md](components.md). The surface paints a single light theme
with ink-dark bands inside it — the 48px promo banner and the deep-purple
feature cards — not a user toggle.

## The chrome: ink banner over a white mega-nav

Every desktop page opens on a 48px ink strip
([top-banner](components/crops/top-banner-default.png), `#171717`,
white text) over the 88px sticky white nav
([header](components/crops/header-default.png)): the copy.ai wordmark
([logo](components/crops/logo-default.png)), the triggers `Platform` /
`Use cases` / `Resources` / `Pricing` / `GTM AI`
([nav-dd-toggle](components/crops/nav-dd-toggle-default.png), 14/22 #222222
at 500), then a text `Login` link
([login-link](components/crops/login-link-default.png)) and the purple
`Get a Demo` pill ([btn-nav](components/crops/btn-nav-default.png),
#693ee0 fill, white 14/22 700 label, 4px radius, 47px tall, a 0.3s
fill transition that deepens on hover).

The `Platform` trigger opens a 389px full-width mega-menu
([nav-dd-panel](components/crops/nav-dd-panel-default.png)) — see
[home-light-menu](screenshots/home-light-menu.png): a white panel with a
`#e0e0e0` top hairline and a faint `rgba(0,0,0,0.03) 0 40px 34px` drop,
holding four columns of links
([dd-link](components/crops/dd-link-default.png), 16/24 #171717 at 500,
a #4d65ff 2px focus ring). The triggers' own hover is the system's
quietest signature: an `rgb(23,23,23) 0 -1px 0 0 inset` underline that
arrives over 0.4s ([nav-dd-toggle](components/crops/nav-dd-toggle-hover.png)).
The menu auto-closes after a few seconds — readings re-open it first.

## The hero and the email capture

Home centres the 88px ABC Normal display
([hero-title](components/crops/hero-title-default.png), 88/88 at 600,
#171717) over a 14/22 slate lede
([hero-sub](components/crops/hero-sub-default.png), #566b76), with the
purple circuit artwork behind them — published content, not a CSS value.
The capture pairs a 42px field
([hero-email](components/crops/hero-email-default.png), #f6fafb fill on a
#e4edf1 border, a 0.2s border/box-shadow transition that takes a real
outline on focus) with a 40px black submit
([hero-submit](components/crops/hero-submit-default.png)) that lifts to
#693ee0 on hover. Below, playbook chips
([playbook-card](components/crops/playbook-card-default.png)) carry the
#ccd9e0 border and an `rgba(204,217,224,0.2) 0 -3px 0 inset` bottom
wash, and section headings repeat at 56/66
([section-h2](components/crops/section-h2-default.png)). The deep-purple
platform band ([platform-card](components/crops/platform-card-default.png),
#29007a) is the page's biggest painted dark surface — white 28/38 titles
inside it.

## Pricing

[/prices](screenshots/pricing-light-full.png) opens on the 64/74 page
display ([pricing-h1](components/crops/pricing-h1-default.png)) and a
56px segmented pill ([plan-toggle](components/crops/plan-toggle-default.png),
Self-Serve | Enterprise, 48px radius, a `rgba(0,0,0,0.06) 0 28px 64px`
float — the surface's only drop shadow of any size). The Chat plan card
([plan-card](components/crops/plan-card-default.png), 360 x ~595, white
on a #e0e0e0 hairline) stacks a checklist, a Monthly|Annually inline
control, the `SAVING 20%` badge
([saving-badge](components/crops/saving-badge-default.png), #693ee0 on a
40px pill), the purple price
([plan-price](components/crops/plan-price-default.png)) and a full-width
47px black `Get started`
([plan-cta](components/crops/plan-cta-default.png)) — which lifts to
#683ee4 on hover like every dark button. The FAQ rows below
([faq-item](components/crops/faq-item-default.png), 82px, toggled open
in [pricing-light-faq](screenshots/pricing-light-faq.png)) answer in
#3a4554.

## Contact and the auth card

[/contact-us](screenshots/contact-light-full.png) leads with the 72/82
display ([contact-h1](components/crops/contact-h1-default.png), the
surface's only 700 heading) beside a three-field form: 48px #f6fafb
fields on #e4edf1 borders at a 5px radius
([name-input](components/crops/name-input-default.png),
[email-input](components/crops/email-input-default.png), the 80px
[message-field](components/crops/message-field-default.png)) and a 63px
black `Send message`
([send-button](components/crops/send-button-default.png)) — focused and
filled then cleared in
[contact-light-form-focus](screenshots/contact-light-form-focus.png),
never submitted. An FAQ column ([contact-faq](components/crops/contact-faq-default.png))
sits alongside.

The login link lands on login.copy.ai's own card
([auth-card](components/crops/auth-card-default.png), 344 x ~284, white
on a #e5e7eb border — see [login-light-default](screenshots/login-light-default.png)):
a 38px email field ([auth-email](components/crops/auth-email-default.png),
3.5px radius), the #693ee0 `Continue with email`
([auth-continue](components/crops/auth-continue-default.png), 4.5px
radius, walking #693ee0 → #5b36c3 hover → #4e22b1 pressed), the
Google/Microsoft OAuth anchors
([auth-oauth](components/crops/auth-oauth-default.png)) whose only edge
is a 1px inset ring — rgba(0,0,0,0.192) that darkens to 0.267 on hover
and takes a 6% black wash pressed — and the #5753c6 `Sign up` link
([auth-signup](components/crops/auth-signup-default.png)). The auth host
paints its own stack (`interFont`) and links; it's a second system, kept
separate in the tokens. Measured, never used.

## The footer

The light footer ([footer](components/crops/footer-default.png)) runs
link columns ([footer-link](components/crops/footer-link-default.png))
and social icons ([social-icon](components/crops/social-icon-default.png))
on white, closed by the legal line — ink headings, muted links, the same
#4d65ff/#005fcc focus rings as the rest of the surface.

## Mobile

At 390 the header compresses to 80px
([m-header](components/crops/m-header-default.png)) with a 46px circled
burger ([m-menu-button](components/crops/m-menu-button-default.png)).
The burger opens a full-height overlay
([m-menu-open](components/crops/m-menu-open-default.png) — see
[mobile-home-light-menu](screenshots/mobile-home-light-menu.png)):
89px accordion rows ([m-nav-item](components/crops/m-nav-item-default.png),
#e0e0e0 hairlines) over `Login`
([m-login](components/crops/m-login-default.png), 8px radius, 50px) and
`Contact Sales` ([m-sales](components/crops/m-sales-default.png), 4px).
The display drops to ~43px
([m-hero](components/crops/m-hero-default.png), 42.9/53.625). Both
mobile full pages stitched from two chunks.

## The state signature

Two moves carry the surface's interactivity. Every **black button lifts
to purple on hover** — #171717 → #693ee0/#683ee4 on hero-submit,
plan-cta, send-button, invert-cta, the 0.3s fill transition — while
**nav triggers take an ink inset underline** (0 -1px) over 0.4s. Fields
transition border/box-shadow in 0.2s; playbook chips take a 0.1s shadow
move. Focus paints a real outline: #005fcc 1px auto on buttons and
links, #4d65ff 2px solid on dropdown and accordion rows, #a396ff on the
auth host. Pressed is CDP-forced on every control.

## Boundaries

Everything behind the login.copy.ai card — the workflows builder, GTM
dashboards, chat, tables, teams, billing — was never reached. Get a
Demo, Try for free, Get started, Sign up, Contact Sales and both OAuth
providers were measured or screenshotted, never followed; the hero
email capture and the contact form were focused and filled then cleared,
never submitted; the Enterprise half of the plan toggle was never
switched; help.copy.ai, the academy and social profiles were never
opened. The HubSpot cookie banner and chat widget were hidden, never
answered.
