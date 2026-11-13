# Doppler patterns

How the measured components combine on doppler.com's public surface, read
from the screenshots and the component entries in [components.md](components.md).
Every captured route paints the same dark theme (warm-black `#1c1624`); all
values are from the dark set.

## The shell

A floating marketing header over the warm-black field
([home-dark-default](screenshots/home-dark-default.png)): a 72px `#1c1624`
bar inset 14px from the viewport edge with a 1px `#55505b` glow stroke on
three sides and 16px bottom corners
([header](components/crops/header-default.png)). Inside: the asterisk
wordmark ([logo](components/crops/logo-default.png), 156 x 31), the
Platform/Solutions/Resources mega-menu triggers, plain silver links that go
warm-white on hover ([nav-link](components/crops/nav-link-default.png),
15/15 bold), the bordered Get-Demo and Sign-In actions, and the
fluorescent-green **Start for Free** pill
([nav-cta](components/crops/nav-cta-default.png), 156 x 36, 12px radius).
The Platform trigger opens a 720 x 372 warm-black panel with a `#55505b`
hairline ([nav-dropdown](components/crops/nav-dropdown-default.png)) of
314 x 73 menu tiles ([menu-link](components/crops/menu-link-default.png)).

The footer is a second warm-black sheet — 1400 x 718 with 20px top corners
([footer](components/crops/footer-default.png)) — carrying link columns, a
bordered "Doppler" tile ([footer-link](components/crops/footer-link-default.png),
201 x 40 at 12px small text with a 2px alpha ring) and the
Cookie Preferences text button
([cookie-button](components/crops/cookie-button-default.png)).

## CTA vocabulary

Two recipes cover every action on the surface:

- **Green pill** — `#00f575` fill, warm-black `#1c1624` text, 12px
  radius: the header's 36px Start for Free, the hero's 45px variant, the
  demo form's 43px Choose a Time submit
  ([demo-submit](components/crops/demo-submit-default.png)) and the Team
  plan's CTA, all at 15/15 bold — plus two 44px variants at 16/24 regular:
  the integrations page's Request an Integration
  ([request-integration](components/crops/request-integration-default.png),
  208 x 44) and the agents page's Pick Your Tool button
  ([agents-cta](components/crops/agents-cta-default.png), 161 x 44, an
  in-page scroll link painted as a button). Hover drops the fill to
  `#00bf5b`; text stays black.
- **Bordered ghost** — transparent fill, 1px `#f1f0ec` border, same 12px
  radius and 15/15 bold text: the hero Get Demo
  ([hero-cta](components/crops/hero-cta-default.png), 136 x 45), Sign In and
  the Developer/Enterprise plan CTAs
  ([plan-cta](components/crops/plan-cta-default.png), 332 x 45).
  Hover adds an 8% warm-white veil.

Plain silver links round out the vocabulary — nav items and Read More
anchors ([read-more](components/crops/read-more-default.png)) — with hover
to warm-white.

## Hero and section type

Every page opens with the same type composition: a Doppler Repro 450
headline at `h3`-size (48px on home — 56px elsewhere, up to the 96px `h1`
step) with a lilac `#855aff`-to-carmine `#ff5632` gradient painted on one
line ([hero-title](components/crops/hero-title-default.png),
[platform-h1](components/crops/platform-h1-default.png)), over a silver
`d0c9c4` lede in `p2` 18/1.4
([hero-sub](components/crops/hero-sub-default.png)). Section headings
down-page switch to light-purple `#b997ff`
([h2-section](components/crops/h2-section-default.png)) — the one place the
secondary accent leads. The blog and integrations titles run the full
96px step ([blog-h1](components/crops/blog-h1-default.png)).

## The interactive-card

Content grids are built from one tile recipe, `.interactive-card`: a 4%
warm-white veil `rgba(242,241,237,0.04)` at 20px radius, a diagonal white
sheen in `::before`, and a 500ms hover that lifts the sheen. It is the
feature card on home ([feature-card](components/crops/feature-card-default.png),
396 x 288), the plan card on pricing
([plan-card](components/crops/plan-card-default.png), 396 x 939), the post
card on the blog ([post-card](components/crops/post-card-default.png),
396 x 570), the integration tile
([integration-card](components/crops/integration-card-default.png),
289 x 181), the agents cards
([agents-card](components/crops/agents-card-default.png)) and the platform
feature cards ([platform-card](components/crops/platform-card-default.png),
610 x 516). The demo form panel uses the same recipe with a 20/32px padding
([demo-card](components/crops/demo-card-default.png)). The one exception is
the customers page's case-study card, which paints solid `#2d2734` inside a
1px `rgba(255,255,255,0.08)` ring at the same 20px radius
([case-card](components/crops/case-card-default.png), 1224 x 590).

## Chips, badges and code

Filters and badges are 22px-tall pill chips — the fill painted on an inner
span, the text a 10px `labelSm` uppercase micro-label at +1px tracking.
Resting chips are `#2d2734` with warm-white text
([filter-chip](components/crops/filter-chip-default.png),
[cat-chip](components/crops/cat-chip-default.png)); the selected chip flips
to light-purple `#b997ff` with warm-black text
([cat-chip-active](components/crops/cat-chip-active-default.png)). The
pricing "MOST POPULAR" badge is the same chip on `#302c37`
([plan-badge](components/crops/plan-badge-default.png)). The customers
page's industry chips paint taller at 37px with an `#2d2734` plate and
green `#00f575` 18px labels
([industry-chip](components/crops/industry-chip-default.png)). Inline code
is the only mono on the surface: Doppler Repro Mono at `code` 16/1.6 in
brand-orange `#f55c15` on the 4% veil at 6px radius
([code-chip](components/crops/code-chip-default.png)).

## Pricing

/pricing is the surface's most instrumented page: the big headline, a
1252px seats slider (10px track, 35px radius) with its 52px `$100,000`
spend field ([seat-slider](components/crops/seat-slider-default.png),
[seat-field](components/crops/seat-field-default.png)), three plan columns
of interactive-cards carrying plan name, price and the two CTA recipes
([plan-name](components/crops/plan-name-default.png),
[plan-price](components/crops/plan-price-default.png)), and the FAQ
accordion — bordered rows of 18px questions with a `+`/`x` toggle, the
answer in silver Inter below ([faq-item](components/crops/faq-item-default.png),
[faq-open](components/crops/faq-open-default.png), 892 x 182 open).

## Forms

The demo request page carries the surface's one real form
([demo-dark-default](screenshots/demo-dark-default.png)): 43px fields with
16px corners and `#8b877d` aluminum borders
([demo-field](components/crops/demo-field-default.png),
[demo-email](components/crops/demo-email-default.png),
[demo-select](components/crops/demo-select-default.png)), placeholder text
in muted warm tones, a `#b997ff` light-purple border on focus, and the
green Choose a Time submit — never pressed. The integrations search field
is the same control at 46px
([search-field](components/crops/search-field-default.png)). Beside the
form, a checklist paints green `#00f575` ticks in Inter
([check-item](components/crops/check-item-default.png)).

## Pagination and miscellany

The blog's pagination is a row of 30px circles — a plain numbered circle at
rest ([page-number](components/crops/page-number-default.png)), the current
page solid. Read More links anchor each post card.

## The mobile surface

At 390px the header holds the wordmark and a 24px hamburger
([m-menu-button](components/crops/m-menu-button-default.png)); its toggle
opens a fixed 390 x 789 warm-black sheet
([m-menu-open](components/crops/m-menu-open-default.png),
[mobile-home-dark-menu](screenshots/mobile-home-dark-menu.png)) of 50px
nav rows ([m-nav-item](components/crops/m-nav-item-default.png)) — the
menu's own toggle was used for the open state, never a script. The hero
stacks at the `h3Mobile` step — 36px at weight 450 on a 36px line
([m-hero](components/crops/m-hero-default.png)) — with the
same 36px green pill ([m-cta](components/crops/m-cta-default.png)).
