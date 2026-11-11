# Busuu patterns

How the measured components combine on busuu.com's public surface, read from
the screenshots and the component entries in [components.md](components.md).
The site paints one light theme over a white field; the footer is a pale-blue
`#f2f7fd` section, not a second theme, and the hero/upsell are gradient
sections. All values are from the light set unless noted.

## Two shells

The public surface splits into two frames. Marketing pages (home, about,
choose-your-language) carry the simplified header
([header](components/crops/header-default.png)) — the wordmark
([logo](components/crops/logo-default.png)) over a purple-to-blue gradient, a
white `Learn for free` pill ([cta-signup](components/crops/cta-signup-default.png),
#11ee92 at 2px, radius 45.04px, a 0/2/4 rgba(0,0,0,.3) drop shadow) and the
kebab that opens the Log in / For Educators / For Businesses dropdown
([home-light-menu](screenshots/home-light-menu.png),
[nav-dropdown](components/crops/nav-dropdown-default.png)). App-shell pages
(course, register, login, premium) carry a denser product header — white bar,
blue `Sign in` / `Learn for free` buttons and an `EN` locale selector — and a
deeper link-column footer ([course-light-full](screenshots/course-light-full.png)).

## The home hero

The home page opens on the purple `#6e00f8` → `#563ce9` → `#116eee` diagonal
gradient ([home-light-default](screenshots/home-light-default.png)): a 40px
Nista 800 white headline ([hero-title](components/crops/hero-title-default.png)),
a translucent-white lede ([hero-sub](components/crops/hero-sub-default.png)),
the green `#11ee92` `Learn for free` pill
([hero-cta](components/crops/hero-cta-default.png) — the same pill as the
header CTA: 48px high, ink label, hover lifts to `#41f1a8`), a Trustpilot row
and the learner illustration. Below the fold, an `I want to learn` flag
carousel ([flag-card](components/crops/flag-card-default.png)) and
alternating text/screenshot feature rows lead to a second gradient band
(`Join over 120 million learners`), a B2B logo strip and the footer
([home-light-full](screenshots/home-light-full.png)).

## The language picker

`/en/choose-your-language` and `/en/register` step 1 paint the same surface
([languages-light-full](screenshots/languages-light-full.png),
[register-light-default](screenshots/register-light-default.png)): a centred
40px `What would you like to learn?` over a 4-column grid of white 16px
cards — circular flag artwork, the language name, a muted learner count
([language-item](components/crops/language-item-default.png)). Hover adds a
1px `#116eee` border and a `#f3f8fe` label fill; the same card pattern drives
the home flag carousel. Choosing a language creates the session — measured,
never chosen.

## The Premium upsell

`/en/premium` is a full-page indigo `#221658` paywall surface
([premium-light-full](screenshots/premium-light-full.png)): a `RECOMMENDED
FOR YOU` kicker, a white 32px title
([premium-title](components/crops/premium-title-default.png)), a pill-rail
billing toggle ([period-toggle](components/crops/period-toggle-default.png) —
12 months selected, [premium-light-monthly](screenshots/premium-light-monthly.png)
shows 1 month) and two translucent plan cards on an 8px radius
([plan-card](components/crops/plan-card-default.png)). Each card holds a
strikethrough list price beside a yellow `SAVE 51%` and the sale price
([plan-price](components/crops/plan-price-default.png)), a white pill CTA
with a `#5438dc` label ([plan-cta](components/crops/plan-cta-default.png),
radius 26px) and a check-list of features. The X close button sits top-right;
where it lands was never followed.

## The course landing page

`/en/course/learn-spanish-online` is the app-shell long page
([course-light-full](screenshots/course-light-full.png)): a blue hero with
phone screenshots (`Learn Spanish online for free`, a green
`Get started for free` CTA — [course-cta](components/crops/course-cta-default.png):
the anchor computes transparent, its child button paints a green `#11ee92`
fill on a 100px radius over the blue hero band), a
language chip row, `Courses for the basics and beyond` carousel cards, a stat
band (510+ lessons · 120m+ learners · 5million reviews), a `Discover
effective Spanish learning` feature band, numbered `How Busuu works` cards,
testimonial cards, a `Download the Busuu app` band and `Spanish learning
resources` article cards before the app-shell footer.

## Login

`/en/login` centres a narrow form on white
([login-light-default](screenshots/login-light-default.png)): a `Log in`
title, `Continue with Google/Apple/Facebook` outline pills, an `OR` hairline
divider, labelled Email and Password fields underlined in the action blue, a
solid blue `Log in` pill and an SSO link. Never filled, never submitted.

## The footers

Marketing pages end on the pale-blue `#f2f7fd` `.main-footer`
([footer](components/crops/footer-default.png)): a `Display Language` select
with a `#d6dee6` hairline border, four link columns in ink
([footer-link](components/crops/footer-link-default.png)), a row of circular
`#a7b0b7` social icons ([social-icon](components/crops/social-icon-default.png))
and the copyright line. The app-shell footer swaps in a denser column layout
with app-store badges (visible in
[course-light-full](screenshots/course-light-full.png)).

## Mobile

At 390 the simplified header keeps the wordmark, the `Learn for free` pill
and the kebab ([m-header](components/crops/m-header-default.png)); the
kebab's own toggle opens the same three-link dropdown panel over the hero
([mobile-home-light-menu](screenshots/mobile-home-light-menu.png),
[m-nav-item](components/crops/m-nav-item-default.png)). The hero compresses
to a centred 30px headline ([m-hero](components/crops/m-hero-default.png)),
the gradient and illustration stack vertically
([mobile-home-light-full](screenshots/mobile-home-light-full.png)) and the
course page scales the same way
([mobile-course-light-full](screenshots/mobile-course-light-full.png)).

## Boundaries

app.busuu.com — lessons, review, streaks, the profile and every signed-in
surface — was never reached. Register stops at step 1 (choosing a language
starts the account), checkout was never followed, and the premium close
button's destination is unrecorded. See the Gaps section in
[components.md](components.md).
