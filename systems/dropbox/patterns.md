# Dropbox patterns

How the measured components combine on dropbox.com's public surface, read
from the screenshots and the component entries in
[components.md](components.md). The whole surface paints one scope —
`dig-Theme-vis2023--bright` on `dig-Mode--bright` — with `dwg-theme--*`
classes rebinding the section palettes: coconut fields, graphite dark bands,
navy accents. Values are from the light set; section-scoped roles are the
`light.dwg.*` groups. The auth cards run an older "susi" sheet and are
noted where they diverge.

## The header and mega-menu

Every marketing page carries the same sticky 72px `dwg-nav`
([header](components/crops/header-default.png), white `dwg-bg-color--standard`
on the coconut theme): the box mark ([logo](components/crops/logo-default.png),
154 x 40), the `Products` and `Solutions` flyout triggers
([nav-trigger](components/crops/nav-trigger-default.png), 105 x 72), the
plain `Business` / `Pricing` links
([nav-link](components/crops/nav-link-default.png)) and `Contact sales`
([nav-contact](components/crops/nav-contact-default.png)) — then `Get app`,
`Sign up` ([nav-signup](components/crops/nav-signup-default.png)), `Log in`
([nav-login](components/crops/nav-login-default.png)) and the `Get started`
pill ([nav-cta](components/crops/nav-cta-default.png), 117 x 40, `#0061fe`
fill → `#0057e5` hover, `#f7f5f2` text, 12px radius). **Hovering** the
Products trigger opens the 480 x 400 two-column mega-menu
([nav-dropdown](components/crops/nav-dropdown-default.png),
[home-light-menu](screenshots/home-light-menu.png)) — a click closes it
again; the menu is pointer-driven and closes on keyboard focus. Rows are
92px product links ([menu-link](components/crops/menu-link-default.png))
that take a `rgba(167,146,114,0.14)` coconut wash with `#0061fe` text on
hover. Keyboard focus draws the 3px `#428bff` shadow ring
([nav-cta](components/crops/nav-cta-focus-visible.png)).

## The hero and the home page

The home hero paints inside a `dwg-theme--graphite` band
([home-light-default](screenshots/home-light-default.png)): a Sharp Grotesk
display headline ([hero-title](components/crops/hero-title-default.png),
~66px/71.5, weight 500, -1px tracking, `#f7f5f2` on graphite — the copy
rotates A/B variants), an Atlas Grotesk 20/30 lede
([hero-sub](components/crops/hero-sub-default.png),
`rgba(82,74,62,0.82)`-family muted ink), and the hero action
([hero-cta](components/crops/hero-cta-default.png), 230 x 71, 16px radius).
Below the hero the page alternates `dwg-theme--*` sections: coconut-200/300/
500/600 fields ([coconut-band](components/crops/coconut-band-default.png)),
graphite-600 bands ([graphite-band](components/crops/graphite-band-default.png)),
an icon-button carousel ([icon-button](components/crops/icon-button-default.png),
32px), transparent secondary actions
([transparent-btn](components/crops/transparent-btn-default.png)) and
inline `dwg-text-link` links ([text-link](components/crops/text-link-default.png))
— all on the 8px grid with 12-24px radii.

## Plans and pricing

/plans ([plans-light-default](screenshots/plans-light-default.png)) opens
on white with the title ([plans-title](components/crops/plans-title-default.png))
and a **Billed monthly / Billed yearly** radio pair
([billing-radio](components/crops/billing-radio-default.png), real
`dwg-input-radio` inputs — the page defaults to **yearly**;
[plans-light-monthly](screenshots/plans-light-monthly.png) is the toggled
state). The plan cards ([plan-card](components/crops/plan-card-default.png),
416 x 1079, `#faf9f7` field, 12px radius) stack a 14/20 plan name
([plan-name](components/crops/plan-name-default.png)), a 20/24 price figure
([plan-price](components/crops/plan-price-default.png), US$), a 320 x 55
blue primary action ([plan-cta](components/crops/plan-cta-default.png),
`#0061fe` → `#0057e5` → `#0050d0`, 16px radius) and a transparent
"or buy now" ([plan-cta-alt](components/crops/plan-cta-alt-default.png)).
Outline actions ([plan-outline](components/crops/plan-outline-default.png),
39px) carry the free/contact tiers. The comparison table adds a
Show-only-differences toggle ([diff-toggle](components/crops/diff-toggle-default.png))
and the "? Help me choose" trigger
([help-choose](components/crops/help-choose-default.png)).

## Product and landing pages

`/features` ([features-light-default](screenshots/features-light-default.png))
and the product pages (`/dropbox`, `/replay`, `/sign`, `/docsend`) repeat
the same grammar: a Sharp Grotesk display heading
([feat-title](components/crops/feat-title-default.png),
[sign-title](components/crops/sign-title-default.png),
[biz-title](components/crops/biz-title-default.png)), a 40px blue primary
action ([biz-cta](components/crops/biz-cta-default.png),
[sign-cta](components/crops/sign-cta-default.png)), feature/nav cards
([feat-card](components/crops/feat-card-default.png), 413 x 517) and the
section palettes — navy on /business
([navy-band](components/crops/navy-band-default.png)), graphite on /replay
([replay-light-default](screenshots/replay-light-default.png) is mostly a
dark page on the bright scope).

## The auth cards

/login and /register ([login-light-default](screenshots/login-light-default.png),
[register-light-default](screenshots/register-light-default.png)) centre a
white 368px card ([auth-card](components/crops/auth-card-default.png),
[register-card](components/crops/register-card-default.png)) on the coconut
field: `Continue with Apple` and `Continue with Microsoft` outline buttons
([sso-button](components/crops/sso-button-default.png),
[sso-button-alt](components/crops/sso-button-alt-default.png), 368 x 40,
white, 4px radius, 8% ink wash on hover), the `name@company.com` email
field ([email-field](components/crops/email-field-default.png), 368 x 48 —
focused, it takes the 3px `#428bff` shadow ring;
[email-field-focused](components/crops/email-field-focused.png)) and the
blue 55px `Continue`
([continue-button](components/crops/continue-button-default.png),
[register-cta](components/crops/register-cta-default.png)). This "susi"
surface mixes sheets — the wrappers and the email field run an older
`lucida grande` system stack at 13-16px while the painted labels stay
Atlas Grotesk Web (SSO 14/16, Continue 16/19.2 500) — with small radii,
not the DIG marketing system's shapes. Captured and measured, never used.

## The footer

The footer ([footer](components/crops/footer-default.png), 619px) closes
every page with the dwg-text-link columns — Product / Plans / Support /
Community / Company — app links and social icons
([footer-link](components/crops/footer-link-default.png),
[social-icon](components/crops/social-icon-default.png)) on the black
field.

## Mobile

At 390 wide ([mobile-home-light-default](screenshots/mobile-home-light-default.png))
the nav collapses to mark + actions + a 48px hamburger
([m-header](components/crops/m-header-default.png),
[m-menu-button](components/crops/m-menu-button-default.png)). The hamburger
opens the `dwg-nav-mobile-dropdown` panel
([m-menu-open](components/crops/m-menu-open-default.png), 390 x 708,
[mobile-home-light-menu](screenshots/mobile-home-light-menu.png)) — 77px
nav rows ([m-nav-item](components/crops/m-nav-item-default.png)) for
Products / Solutions / Business / Pricing / Contact sales / Get app /
language, with `Sign up` / `Log in` staying in the top bar
([m-signup](components/crops/m-signup-default.png)) and a full-width blue
`Get started` at the bottom. The display heading scales to ~350px wide
([m-hero](components/crops/m-hero-default.png)).
