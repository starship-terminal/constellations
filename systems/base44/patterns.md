# Base44 patterns

How the components combine into the product's public screens. Captured from
base44.com on 2026-11-11, signed out, at 1440 x 900 (mobile 390 x 844).

## The fixed shell

`header` is a fixed transparent bar (86px tall over the hero, shrinking to a
56px bar + 20px margin — `--header-bar-h`, `--header-margin`, `--header-offset`)
that gains the paper ground on scroll. Inside it: the wordmark (orange dot +
"Base44" in the display face), four menu buttons (Product, Use Cases,
Solutions, Resources) that open a full-width mega panel, text links (Pricing,
Enterprise), the blue dotted Superagents link, a language globe and the dark
38px Start building pill. At 390px the bar collapses to logo + a hamburger
whose press opens a full sheet of stacked nav groups.

See [home-light-default](screenshots/home-light-default.png),
[home-light-product-menu](screenshots/home-light-product-menu.png) and
[mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png).

## The CTA vocabulary

Three buttons carry the whole site. The **dark pill** — `#312f2f`
(`color.cta.black`), 38px, 8px radius, white Geist 14px — is Start building in
the nav and the plan-card CTAs (10px radius at 50px height there). The **orange
action** — `#ff773c` (`color.cta.orange`), dark `#181818` text — is the
composer's send and the selected billing segment. The **ghost** — white card
with a `--border` hairline — is the OAuth buttons on the sign-in page. Hover
deepens every fill one step (`#433f3f`, `#ff8e5d`); keyboard focus is a 2px
`#1e1e24` outline offset 4px (2px `#3b51e5` on OAuth buttons).

## The hero composer

The home hero is a funnel: Dazzed ~94px headline, a Geist sub, then the prompt
box — a white 8px-radius card (`--radius-sm`, `--elevation-md`) holding a bare
textarea over a button row (`+` attach, "Build" mode trigger, mic, orange
40px send) — then five 120x66 build-type tiles (icon + label). The composer is
reused on builder landing pages. Everything below it is proof: a strip of
generated-app screenshots, feature sections with `br-display` titles, a plan
teaser, the FAQ accordion and the sendoff CTA.

See [home-light-full](screenshots/home-light-full.png) and
[prompt-box](components.md#prompt-box).

## Pricing

A centred Dazzed title, a 56px translucent Yearly/Monthly toggle (the selected
segment is an orange sliding indicator, not a button fill), then a row of
white square-cornered `.pricing-card`s — plan name, Geist blurb, Dazzed price
("/mo" muted), a hairline credits line, a full-width 50px dark CTA, plan
highlights. The Builder card wears a blue `Popular` chip (4px radius, white
14px). FAQ accordion under it, same pattern as home.

See [pricing-light-default](screenshots/pricing-light-default.png) and
[pricing-light-monthly](screenshots/pricing-light-monthly.png).

## The FAQ accordion

Right column under a two-line "Frequently asked questions" title: full-width
question rows (`button`, Geist medium, a `+` that becomes `−`), separated by
hairlines. A row's own press expands its answer — a local toggle, never a
navigation. See [faq-item](components.md#faq-item) and faq-open.

## Sign in

app.base44.com/login is a two-column card page: left a form column ("Welcome to
Base44" display-3, three 36px ghost OAuth buttons with provider glyphs, an "OR"
divider, a 36px bordered email field, a 36px submit captured disabled for the
empty field, a "Sign up" link); right a warm-cream artwork panel with product
collage and the asterisk mark. Terms/Privacy links in the footer line.

See [signin-light-default](screenshots/signin-light-default.png).

## Footer

Four link columns on the paper ground (`.br-footer-link`, Geist), social icon
links (X, Discord, LinkedIn, Reddit) and a legal row. See
[footer](components.md#footer).
