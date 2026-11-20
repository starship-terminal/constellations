# Luma patterns

How the measured components combine on luma.com's public surface, read from
the screenshots and the component entries in [components.md](components.md).
Marketing pages paint `theme-root.light` on a white field. The public event
page paints `theme-root.dark` on its own. Values are from the light set
unless marked.

## The landing header

The home header is not a wordmark
([header](components/crops/header-default.png)). It is a 20px spark
([spark](components/crops/spark-default.png)) and a light Sign In pill
([nav-signin](components/crops/nav-signin-default.png), about 67 x 30,
15px radius). Inner pages add the luma wordmark
([wordmark](components/crops/wordmark-default.png), about 44 x 28, linking
home) and Discover Events
([nav-discover](components/crops/nav-discover-default.png)). At 390px the
home header stays spark plus Sign In
([m-header](components/crops/m-header-default.png)). There is no hamburger.

## The home hero

Home opens on white
([home-light-default](screenshots/home-light-default.png)) with a stacked
80px weight-500 title
([hero-title](components/crops/hero-title-default.png)): "Delightful events
start here". The visible line is one of four `h1.landing-title` atoms. The
lede sits under it
([hero-lede](components/crops/hero-lede-default.png)). Two actions follow:
Create Your First Event
([cta-create](components/crops/cta-create-default.png), ink pill, 100px
radius, linking `/create`) and Discover Events
([cta-discover](components/crops/cta-discover-default.png), a text link).
Create was measured and never followed. `/create` opens a sign-in dialog.

## Pricing

Pricing ([pricing-light-default](screenshots/pricing-light-default.png))
centres a 60px title
([pricing-title](components/crops/pricing-title-default.png)) over Monthly
and Annual segments
([billing-monthly](components/crops/billing-monthly-default.png),
[billing-annual](components/crops/billing-annual-default.png)). Annual is
selected at rest. The Monthly shot is
[pricing-light-monthly](screenshots/pricing-light-monthly.png). Plan cards
([plan-card](components/crops/plan-card-default.png),
[plan-card-plus](components/crops/plan-card-plus-default.png)) use a 24px
radius. Get Started is a dark 16px-radius pill linking `/signin`
([plan-cta](components/crops/plan-cta-default.png)). Get Luma Plus is the
pink brand pill
([plan-cta-brand](components/crops/plan-cta-brand-default.png)) and links
to `/calendar/manage/plus`, which is checkout and was never opened.

## Discover

Discover ([discover-light-default](screenshots/discover-light-default.png))
is a public directory: a title
([discover-title](components/crops/discover-title-default.png)), category
cards ([category-card](components/crops/category-card-default.png)) and
event rows with a Follow pill
([follow-button](components/crops/follow-button-default.png)). Follow was
measured and never pressed. Event titles on this page follow the capture
egress.

## The public event page

`/july4-brooklyn` paints dark on its own
([event-dark-default](screenshots/event-dark-default.png)). The header is
the wordmark, Discover Events and a Sign In button
([event-signin](components/crops/event-signin-default.png)). The title
([event-title](components/crops/event-title-default.png)) uses Google Sans
Flex near 38px at weight 575. A host card
([host-card](components/crops/host-card-default.png)) carries a Follow
control ([host-follow](components/crops/host-follow-default.png)) that was
never pressed. The location row
([event-meta](components/crops/event-meta-default.png)) names Brooklyn
Bridge Park, a public venue, and links to a map. The page has no public
tickets. Access-code entry was not submitted.

## Sign in

Sign-in ([signin-light-default](screenshots/signin-light-default.png)) is
a light card: "Welcome to Luma"
([signin-title](components/crops/signin-title-default.png)), an email
field ([email-field](components/crops/email-field-default.png), 320 x 38,
typed then cleared), a Use Phone Number toggle
([phone-toggle](components/crops/phone-toggle-default.png), never pressed),
Continue with Email
([continue-btn](components/crops/continue-btn-default.png)), Sign in with
Google ([google-btn](components/crops/google-btn-default.png)) and Sign in
with Passkey ([passkey-btn](components/crops/passkey-btn-default.png)).
Nothing was submitted.

## Footer

The marketing footer ([footer](components/crops/footer-default.png)) is a
link row. One link was measured
([footer-link](components/crops/footer-link-default.png)) and never followed.

## Mobile

At 390px the home hero stacks
([m-hero](components/crops/m-hero-default.png)) under the spark and Sign In
pill ([m-signin](components/crops/m-signin-default.png)). The event page
and the sign-in card were captured at the same width
([mobile-event-dark-default](screenshots/mobile-event-dark-default.png),
[mobile-signin-light-default](screenshots/mobile-signin-light-default.png)).
