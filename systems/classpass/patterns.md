# ClassPass patterns

How the measured components combine on classpass.com's public surfaces,
read from the screenshots and the component entries in
[components.md](components.md). The site paints one light theme — a white
`#fff` ground the `html` element itself carries (`body` is transparent) —
with the black footer as its only dark island; all values are from the
light set unless noted.

## The header and the Products flyout

Every marketing page opens under a 64px white bar
([home-light-default](screenshots/home-light-default.png)) separated from
the page by a 1px `#e7e7e7`-style hairline: the wordmark anchor
([logo](components/crops/logo-default.png)) left, text nav items at 14px
norms that pick up a `#f7f7f7` wash on hover, focus and press
([nav-item](components/crops/nav-item-hover.png)), and two actions right —
the **Log in** link
([nav-login](components/crops/nav-login-default.png)) and the 149x53 blue
`#0055ff` pill **Get 14 days free**
([nav-cta](components/crops/nav-cta-default.png), radius 9999px). The
**Products** item is a dropdown trigger whose own press opens a small
200px panel of menu cards
([menu-panel](components/crops/menu-panel-default.png),
[menu-card](components/crops/menu-card-default.png), the open state in
[home-light-menu](screenshots/home-light-menu.png)). Keyboard focus draws
a 1px auto `#101010` outline on text controls and a designed 2px solid
`#0055ff` ring on the blue and dark buttons; the header's own Log-in link
and CTA pill could not be given a real keyboard focus on this pass
(recorded as unmeasured, not absent).

## The rotating-word hero

The home hero is a full-width headline set in 36-40px Circuit — "One app
for" followed by a rotating activity word (fitness, wellness, beauty,
gyms, Pilates…) that repaints through a scripted 0.5s fade
([hero-title](components/crops/hero-title-default.png),
[home-light-default](screenshots/home-light-default.png)) — over the 20px
norms subtitle "Join ClassPass today to access thousands of top-rated
studios, gyms, salons, and spas"
([hero-sub](components/crops/hero-sub-default.png)). Scattered through the
hero are translucent photo cards — `rgba(0, 0, 0, 0.08)` scrim frames with
25px corners
([hero-card](components/crops/hero-card-default.png)) — and a
multi-carousel of logo/brand tiles. The whole band sits on the white page;
nothing inverts.

## The search surface

`/search` is the densest public screen
([search-light-default](screenshots/search-light-default.png),
[search-light-full](screenshots/search-light-full.png)): a 549x64 white
search box with 20px corners holding two comboboxes — an activity field
and a location field
([search-box](components/crops/search-box-default.png),
[search-field](components/crops/search-field-default.png),
[search-loc](components/crops/search-loc-default.png)) with `#757575`
placeholders and `#e7e7e7` hairlines — then a row of 128x38 filter pills
with 16px corners, `#d6d6d6` borders and **blue** `#0055ff` labels
([filter-pill](components/crops/filter-pill-default.png),
[filter-multi](components/crops/filter-multi-default.png)). A pill's own
press opens a 380px dropdown panel — the activity picker with Clear/Done
actions
([filter-panel](components/crops/filter-panel-default.png), open state in
[search-light-filter-open](screenshots/search-light-filter-open.png)).
Results render as 790px venue rows: a photo, the studio name, a `#0055ff`
star rating and a `#999` muted line, separated by 10%-black hairlines with
5px corners
([venue-card](components/crops/venue-card-default.png),
[venue-rating](components/crops/venue-rating-default.png)). The controls
were opened and measured; no search was ever run.

## The plan carousel and FAQ

`/plans` opens with the 60px Circuit heading "Pick a plan that works for
you"
([plans-h1](components/crops/plans-h1-default.png),
[plans-light-default](screenshots/plans-light-default.png)) over a
carousel of 267x148 plan cards: white on the outside with 18px corners and
the brand-tinted `0 5px 16px rgba(1,85,254,0.1)` shadow, a light-blue
`#c0e0ff` tinted band inside with 14px corners, a small pill tag, the
credits line and a 36px/700 norms price
([plan-slide](components/crops/plan-slide-default.png),
[plan-pill](components/crops/plan-pill-default.png),
[plan-price](components/crops/plan-price-default.png)). Real copy is
geo-localized — this capture shows "45 credits SGD 99 /mo". Below the
carousel a CMS section pairs the 24px section heading "Fitness and
wellness aren't one-size-fits-all…"
([section-title](components/crops/section-title-default.png)) with a dark
`#111` pill CTA "See all plans"
([cms-cta](components/crops/cms-cta-default.png)) and an accordion of
18px FAQ questions
([faq-question](components/crops/faq-question-default.png)) whose chevrons
rotate on a 0.3s transform.

## The sign-in card (boundary)

`/login` is a centred card on the white page: the "Welcome back" title,
two 400x42 white fields with 4px corners and `#e7e7e7` hairlines that
repaint their borders `#1a5ee5` on focus
([signin-email](components/crops/signin-email-focused.png),
[signin-pass](components/crops/signin-pass-focused.png)), the `#1a5ee5`
"Forgot password?" link
([signin-forgot](components/crops/signin-forgot-default.png)), the 400x48
blue `Log in` submit that runs the full #0055ff/#004de6/#0044cc ramp
([signin-submit](components/crops/signin-submit-pressed.png)), and the
OAuth buttons — white 400x48 pills with `#d6d6d6` borders that pick up the
same blue focus ring
([signin-apple](components/crops/signin-apple-default.png),
[signin-google](components/crops/signin-google-default.png),
[signin-light-default](screenshots/signin-light-default.png)). The fields
were focused and filled with placeholder text only; the form was never
submitted.

## The walkthrough carousel (boundary)

`/walkthrough` is the trial onboarding carousel: a 596x676 slide card with
20px/500 norms step copy
([walk-slide](components/crops/walk-slide-default.png)), a row of carousel
dots riding the app's own `--carousel-dot-*` variables
([walk-dots](components/crops/walk-dots-default.png)), and the 208x48
`#111` black pill **Next** that deepens to `#040404` on hover and `#000`
pressed
([walk-cta](components/crops/walk-cta-default.png),
[walk-light-default](screenshots/walk-light-default.png)). The first step
was measured; the carousel was never advanced.

## The footer — the dark island

Every page ends in the same 1440x581 black `#000` block
([footer](components/crops/footer-default.png),
[home-light-full](screenshots/home-light-full.png)): white 16px link
columns that keep the 0.3s colour transition
([footer-link](components/crops/footer-link-default.png)), the social row
([footer-social](components/crops/footer-social-default.png)) and the
app-store badges — inline anchors whose badge art overflows their small
boxes ([app-badge](components/crops/app-badge-default.png)). Text over it
is `text.onDark` white; focus still draws the browser's `#101010` auto
ring, invisible on black — recorded as measured, not "wrong".

## The mobile surface

At 390 wide the bar keeps the wordmark but swaps the actions for a yellow
`#fce172` promo banner
([m-banner](components/crops/m-banner-default.png)) and a hamburger that
opens a full-height white menu overlay of 20px links
([m-menu-button](components/crops/m-menu-button-default.png),
[m-menu-open](components/crops/m-menu-open-default.png),
[m-menu-link](components/crops/m-menu-link-default.png), open state in
[mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png)).
The hero reflows to the phone width
([m-hero](components/crops/m-hero-default.png)) and the plan/search
surfaces stack vertically
([mobile-home-light-full](screenshots/mobile-home-light-full.png),
[mobile-search-light-full](screenshots/mobile-search-light-full.png),
[mobile-plans-light-full](screenshots/mobile-plans-light-full.png)).
