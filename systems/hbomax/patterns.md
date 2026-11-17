# HBO Max patterns

How the measured components combine on www.hbomax.com's signed-out surface,
read from the screenshots and the component entries in
[components.md](components.md). `hbomax.com` redirects to `www.hbomax.com`
and resolves the visitor's locale — this capture is the Singapore
`/sg/en` site. One dark theme is painted (`html data-theme="max"`), so all
marketing-surface values are from the dark set; the privacy page is a
separate light legal surface, called out below.

## The shell

A fixed translucent navbar sits over the hero on every marketing page
([home-dark-default](screenshots/home-dark-default.png)): a
`rgba(0, 0, 0, 0.7)` bar, 60px tall ([header-bar](components/crops/header-bar-default.png),
1425 x 60), carrying the HBO Max wordmark, the section links (Series,
Movies, HBO, Sports, Kids & Family) and the **Sign In** control
([header-signin](components/crops/header-signin-default.png), 136 x 44) —
a link to auth.hbomax.com, measured and never followed. At 390px the same
recipe collapses to a 56px bar ([m-header](components/crops/m-header-default.png),
390 x 56) over the mobile hero ([mobile-home-dark-default](screenshots/mobile-home-dark-default.png)).

## The hero carousel

The home page opens on a full-bleed autoplay carousel
([hero-carousel](components/crops/hero-carousel-default.png), 1425 x 694):
backdrop art per slide, the title treatment, a meta line and the
white-on-black **Start Subscription** pill ([hero-cta](components/crops/hero-cta-default.png),
140 x 44 — the action.primary recipe, white fill, black 18px text). A tall
Next control covers the right edge ([hero-next](components/crops/hero-next-default.png),
77 x 489) and slide indicators sit in the slide's text block; pressing Next
advances one slide ([home-dark-carousel-next](screenshots/home-dark-carousel-next.png)).

## Plans

Below the hero the subscription section runs the full 1425px width
([plan-section], 591 tall): a monthly/yearly billing toggle, then the tier
cards, each ending in a wide white **Choose** button
([plan-choose](components/crops/plan-choose-default.png), 293 x 52, 18px/600
black on white). The yearly state repaints the card prices
([home-dark-plan-yearly](screenshots/home-dark-plan-yearly.png)). The
buttons point at plan checkout — hovered and focused only, never pressed.

## FAQ

Near the foot of the home page, a "Questions" accordion
([faq-section](components/crops/faq-section-default.png), 391 tall) of
920px rows ([faq-item](components/crops/faq-item-default.png), 920 x 55);
a chevron press expands the answer
([faq-item-opened](components/crops/faq-item-opened.png),
[home-dark-faq-open](screenshots/home-dark-faq-open.png)).

## Content rails

Home and the browse pages (/movies, /shows, /channel, collections) carry
horizontal rails of poster cards — each card a link into a title detail
page. On the browse pages the rail block spans the full width
(`browse-rail-section`, 1425 x 768 — measured, no crop saved),
card controls ([browse-rail-card](components/crops/browse-rail-card-default.png))
inside; the home rail section was absent at this capture (a first-visit
lazy-load; rail-card itself was measured). See
[movies-dark-default](screenshots/movies-dark-default.png) and
[collection-dark-default](screenshots/collection-dark-default.png).

## Title detail

A detail page (/show/…, /movie/…) opens on a full-bleed backdrop hero
([detail-hero](components/crops/detail-hero-default.png), 1425 x 842) with
the title treatment ([detail-title](components/crops/detail-title-default.png))
and the same white subscribe pill as the home hero
([detail-cta](components/crops/detail-cta-default.png), 140 x 44 — the
action.primary recipe again):
[show-dark-default](screenshots/show-dark-default.png),
[movie-dark-default](screenshots/movie-dark-default.png).

## Footer

Every page ends in the link columns and legal row
([footer-legal-link](components/crops/footer-legal-link-default.png),
136 x 44 items), closing on the language selector — a translucent gray
`rgba(62, 62, 62, 0.75)` pill ([lang-selector](components/crops/lang-selector-default.png),
224 x 52) whose press opens the locale list without changing anything.

## Cookie consent

A fresh visit opens a "Cookie Preferences" modal over the home page
([home-dark-promo](screenshots/home-dark-promo.png),
[mobile-home-dark-promo](screenshots/mobile-home-dark-promo.png)):
a 692 x 148 dialog ([consent-dialog](components/crops/consent-dialog-default.png))
with **Accept** ([consent-accept](components/crops/consent-accept-default.png),
152 x 52) and **Manage** ([consent-manage](components/crops/consent-manage-default.png),
212 x 52) — styled, never pressed; the modal was hidden for the rest of
the pass.

## The light legal surface

`/privacy` is a different surface from the marketing chrome: a white
document column on `#f1f1f1`, plain `sans`/Arial prose — dark gray
headings (`rgb(32, 33, 36)`; `legal-h1` was absent at this capture)
and body text (`rgb(95, 99, 104)`, [legal-p](components/crops/legal-p-default.png))
— with none of the Max token sheet's `--color_*` roles painted. It is the
same signed-out host but its own stylesheets, so its values live in the
component entries rather than the dark token set:
[privacy-dark-default](screenshots/privacy-dark-default.png). The
`-dark-` in the filename is the capture naming convention (the theme the
suite paints), not the page's surface.

## Boundaries

auth.hbomax.com (sign-in, plan selection, checkout), play.hbomax.com (the
app) and help.hbomax.com (the help centre) were observed as link targets
only and never opened; every CTA pointing at them was measured, never
followed. Headless Chromium is refused by Akamai (403 "Access Denied") —
all captures ran headed under Xvfb.
