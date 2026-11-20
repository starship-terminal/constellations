# Calendly patterns

How the measured components combine on calendly.com's public surface, read
from the screenshots and the component entries in
[components.md](components.md). calendly.com is two products signed out: the
Astro/Tailwind marketing site (Geist body, Calendly Sans headings, Wulkan
Text serif accents, on the `#fcfbf8` magnolia field with `.dark` islands)
and the invitee booking pages on `/calendly-demo` (a separate booking-kit
application in Proxima Nova on white). Values are from the light set unless
marked; booking values are the `light.booking.*` roles.

## The marketing header

Every marketing page carries the same chrome
([header](components/crops/header-default.png), 68px high on the
`#fcfbf8` field, sticky): the wordmark
([logo](components/crops/logo-default.png), 156 x 32), the
`Products` mega-menu trigger
([nav-trigger](components/crops/nav-trigger-default.png)), the plain
`Solutions`, `Enterprise`, `Resources`, `Pricing` links
([nav-link](components/crops/nav-link-default.png), Geist 16px), then
`Talk to sales` ([nav-sales](components/crops/nav-sales-default.png)),
a bordered `Log In` ([nav-login](components/crops/nav-login-default.png),
1px midnight border, 16px radius, 48px) and the midnight `Get started`
pill ([nav-cta](components/crops/nav-cta-default.png), `#071a31` on
`#fcfbf8` text, 16px radius). Hovering the trigger opens a 304 x 398
white mega-menu panel ([nav-dropdown](components/crops/nav-dropdown-default.png))
listing feature rows ([menu-link](components/crops/menu-link-default.png),
[home-light-menu](screenshots/home-light-menu.png)). Keyboard focus draws
a 2px solid `#6bb1ff` cornflower outline on the interactive items.

## The home hero

The home page opens on the `#fcfbf8` field ([home-light-default](screenshots/home-light-default.png)):
a 640px-wide `Easy scheduling ahead` headline in Calendly Sans at
72px / 79.2px with -2px tracking ([hero-title](components/crops/hero-title-default.png)),
a 560px lede in Geist 18px ([hero-lede](components/crops/hero-lede-default.png)),
then the two acquisition actions side by side —
`Sign up with Google` ([signup-google](components/crops/signup-google-default.png),
224 x 50, magnolia fill, midnight text, 20px pill) and
`Sign up free with email` ([signup-email](components/crops/signup-email-default.png)).
Below the fold a rounded gradient card
([hero-card](components/crops/hero-card-default.png), 920 x 409 at a 48px
painted radius) paints the first `.dark` island: midnight field, magnolia
text, inverted buttons. Further sections repeat the same grammar — a Wulkan
Text serif h2 at 48px / 52.8px -2px tracking
([h2-serif](components/crops/h2-serif-default.png)) and small neutral badge
chips ([badge](components/crops/badge-default.png), 5%-midnight fill on an
8px radius).

## The pricing surface

/pricing ([pricing-light-default](screenshots/pricing-light-default.png))
centres a Calendly Sans h1
([pricing-h1](components/crops/pricing-h1-default.png)) above a
Monthly/Yearly radio pair — a 20px white circle with a 12px midnight dot
when checked ([billing-radio](components/crops/billing-radio-default.png);
the toggled page is [pricing-light-yearly](screenshots/pricing-light-yearly.png)).
White plan cards ([plan-card](components/crops/plan-card-default.png),
266 x 301 at a 40px painted radius on the `shadow-ui-lg` elevation) hold a
plan name ([plan-name](components/crops/plan-name-default.png)), the price
figure ([plan-price](components/crops/plan-price-default.png)) and a
midnight pill action ([plan-cta](components/crops/plan-cta-default.png),
218 x 50). Feature rows carry 32px square icon buttons
([icon-button](components/crops/icon-button-default.png), 5%-midnight
fill, hover 10%, pressed 20%) and tooltip triggers
([feature-tip](components/crops/feature-tip-default.png)).

## The auth boundary cards

/login and /signup centre white cards on the magnolia field — never
submitted on this pass. The login card
([login-card](components/crops/login-card-default.png), 464 x 500 at 48px
radius on a Tailwind shadow-xl) holds the email field
([email-field](components/crops/email-field-default.png), 368 x 48 at 16px
radius), the midnight `Continue` button
([continue-btn](components/crops/continue-btn-default.png), 368 x 50) and
the SSO row ([sso-btn](components/crops/sso-btn-default.png)). Signup is
the same construction wider ([signup-card](components/crops/signup-card-default.png),
912 x 580, two columns) with its own email field
([signup-field](components/crops/signup-field-default.png)). Both lead to
the authenticated workspace — the boundary, not the product.

## The invitee booking flow

The booking pages are a different application — Proxima Nova 14/21 on the
`#0a2540` ink, no magnolia anywhere. The profile page
([booking-light-default](screenshots/booking-light-default.png)) shows the
`POWERED BY Calendly` mark ([bk-poweredby](components/crops/bk-poweredby-default.png),
105 x 105) and event-link cards ([bk-event](components/crops/bk-event-default.png),
360 x 200 on a `#d4e0ed` hairline). The event page
([booking-event-light-default](screenshots/booking-event-light-default.png))
splits the ~1058px panel ([bk-panel](components/crops/bk-panel-default.png)):
left, the 399px month grid ([bk-calendar](components/crops/bk-calendar-default.png))
with circular month-nav buttons ([bk-month-nav](components/crops/bk-month-nav-default.png),
40 x 40, `#a6bbd1` chevrons); enabled days are 44px circles on a `#f4f8ff`
wash with `#004eba` numbers ([bk-day](components/crops/bk-day-default.png)),
the picked day goes solid `#006bff` with white text
([bk-day-selected](components/crops/bk-day-selected-default.png),
[booking-event-light-day](screenshots/booking-event-light-day.png)) — and
locks disabled once picked. Right, the times column: 278 x 52 slot buttons,
1px `#006bff` border on an 8px radius with 16px/700 `#004eba` labels
([bk-timeslot](components/crops/bk-timeslot-default.png)), under the
timezone control ([bk-timezone](components/crops/bk-timezone-default.png)).
Nothing past the slot was ever reached.

## The footer

The marketing footer ([footer](components/crops/footer-default.png),
1440 x 1038) closes every page in the same magnolia/steel scheme: link
columns ([footer-link](components/crops/footer-link-default.png), Geist
13px steel) under a final `.dark` CTA island.

## Mobile (390 wide)

At phone width the header compresses to 64px
([m-header](components/crops/m-header-default.png)) with a 24px hamburger
([m-menu-button](components/crops/m-menu-button-default.png)) that opens a
full-height 390 x 780 overlay
([m-menu-open](components/crops/m-menu-open-default.png),
[mobile-home-light-menu](screenshots/mobile-home-light-menu.png)) of 57px
nav rows ([m-nav-item](components/crops/m-nav-item-default.png)). The hero
drops to a 320px measure at a smaller display size
([m-hero](components/crops/m-hero-default.png),
[mobile-home-light-default](screenshots/mobile-home-light-default.png)).
The booking event page stacks its two columns vertically
([mobile-booking-event-light-default](screenshots/mobile-booking-event-light-default.png)).
