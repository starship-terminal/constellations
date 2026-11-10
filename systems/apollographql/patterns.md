# apollographql patterns

The recurring shapes the marketing pages are built from. Everything below was
measured on the live site; the component entries and crops are in
[components.md](components.md).

## Space-dark shell

Every marketing page opens on a near-black field — `lightfall` #02060a on the
home hero, `navy-deep` #091b23 on the product pages — under a sticky
transparent nav bar (65px): Apollo wordmark, disclosure links at white 72%
that brighten to full white over a 15%-white pill at hover, a 20px search
icon and the 40px `brand-accent` Start-for-free pill
([nav-bar](components/crops/nav-bar-default.png),
[nav-cta hover](components/crops/nav-cta-hover.png)). A `1a1a1a` eyebrow
strip (promo headline + white pill CTA) can sit above it
([eyebrow](components/crops/eyebrow-default.png)). Sections then alternate
freely between the dark grounds and the light `offwhite`/`satellite`/`faq`
fills — the same tokens, re-bound per section by `[data-theme="dark"]`.

## Display hero

An Aeonik 60/63 headline at −1.5px tracking (36/37.8 at 390) over a 20px
medium lede, then the CTA pair ([hero-title](components/crops/hero-title-default.png),
[hero-sub](components/crops/hero-sub-default.png)). The primary is the
site's signature: a 60px pill whose border is a rotating conic gradient —
teal `component.cta-ring` around a space-dark fill — beside a 1px
white-35 outline pill ([cta-primary](components/crops/cta-primary-default.png),
[cta-secondary](components/crops/cta-secondary-default.png)). Inner pages
drop to Inter 50/55 titles with plain orange CTAs.

## Orange CTAs

Every action pill is fully round (`radius.pill` 999px): filled ones paint
`brand-accent` #e75e15 and darken to #d84f08 on hover and pressed
([nav-cta](components/crops/nav-cta-default.png),
[plan-cta hover](components/crops/plan-cta-hover.png)); outline ones keep
the orange 1px border and fill at 10% on hover
([cta-orange-outline](components/crops/cta-orange-outline-hover.png)). Text
links inside light copy run `horizon-dark` #c74100, brightening to
`brand-accent` on hover ([text-link](components/crops/text-link-hover.png)).
Focus draws a 2px `focus-orange` ring on dark controls, `focus-cyan` on the
hero pair, `focus-blue` on quiet links and segments.

## Pills and segments

The pricing page stacks three pill shapes: 43px filter and billing segments
(1px offwhite border, `radius.segment` 20px, `all 0.2s`), 39px request-volume
pills (`radius.sm` 8px; the held one fills `brand` #fc5200 with nebula text),
and per-plan 49px orange CTAs ([tier-segment](components/crops/tier-segment-default.png),
[volume-pill-on](components/crops/volume-pill-on-default.png),
[plan-cta](components/crops/plan-cta-default.png)).

## Cards on both grounds

Cards split by theme: dark surfaces get `card-dark-bg` #15252d at
`radius.card-lg` 32px with `stats-border` #9fb2bc inner tiles
([stats-card](components/crops/stats-card-default.png)); light surfaces get
white `card-light-bg` or `card-satellite-bg` #cfd7d6, and the FAQ card flips
to `faq-gray` #e3e3e3 ([article-card](components/crops/article-card-default.png),
[faq-card](components/crops/faq-card-default.png)). The OneTrust consent
card is the only element with a real drop shadow — white, 16px radius,
double `shadow.cookie-card` ([cookie-card](components/crops/cookie-card-default.png)).

## Navy form band

On contact-sales the light intro gives way to a `field-bg` nebula band:
54px fields at `radius.field` 16px, offwhite borders that switch to `brand`
#fc5200 on focus, Inter 18/25.2, then the pill submit
([field focused](components/crops/field-focused.png),
[submit](components/crops/submit-default.png)). Nothing was submitted; the
form is documented as a boundary in components.md > Gaps.

## Footer

A space-dark band: a 42px Aeonik tagline, five link columns of 14px quiet
links, a small orange Start-for-free pill and 28px social circles
([footer](components/crops/footer-default.png),
[social-link](components/crops/social-link-default.png)).

## Mobile fold

At 390 the nav collapses to wordmark + burger (the drawer is not captured),
the hero drops to 36/37.8 and both CTAs go full width
([m-nav-bar](components/crops/m-nav-bar-default.png),
[m-hero-title](components/crops/m-hero-title-default.png),
[m-cta-primary](components/crops/m-cta-primary-default.png)).
