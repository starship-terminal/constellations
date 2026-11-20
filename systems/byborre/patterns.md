# BYBORRE patterns

How the measured components combine on byborre.com's public surface, read
from the screenshots and the component entries in
[components.md](components.md). Everything paints one theme: a cream
`#f5f5f0` canvas with `#1b1b1b` ink panels. Values are from the light set;
the "dark" set in tokens.json is the ink-panel surface, not a user toggle.

## The chrome: marquee plus cream header

Every page opens with the ticker bar
([marquee](components/crops/marquee-default.png)) — white 11px medium text
(`ORDER FREE SAMPLES — WORLDWIDE SHIPPING`) scrolling a 10s linear loop over
an ink `#1b1b1b` band — then the 57px cream header
([header](components/crops/header-default.png)): the BYBORRE wordmark
([logo](components/crops/logo-default.png), ~99 x 16), top-level links
`Textile Room New` / `Design Studio` / `Collaborations +` / `About +` /
`Contact` ([nav-link](components/crops/nav-link-default.png), Helvetica Neue
16/20 on an 8px radius), and two 32px icon buttons — cart and account
([cart-button](components/crops/cart-button-default.png),
[account-button](components/crops/account-button-default.png)). The `About`
trigger ([nav-trigger](components/crops/nav-trigger-default.png)) opens a
full-width flyout ([nav-dropdown](components/crops/nav-dropdown-default.png),
210px): a link column on the left ([menu-link](components/crops/menu-link-default.png))
and two image cards on the right
([flyout-card](components/crops/flyout-card-default.png), 280 x 160 with a
cream pill caption). Keyboard focus draws the same ring everywhere: a 2px
transparent outline offset 2px plus an inset shadow — white 0 0 0 0 then ink
0 0 0 2px — so the ring reads as a 2px ink line inside the control's edge.

## The home hero and manifesto

The home page opens on dark textile photography
([home-light-default](screenshots/home-light-default.png)): `Your brand's
DNA in every stitch.` in Helvetica Neue 80/84 medium
([hero-title](components/crops/hero-title-default.png), white over the
media), a 24/32 lede
([hero-sub](components/crops/hero-sub-default.png)) and the `Explore
samples →` pill ([hero-cta](components/crops/hero-cta-default.png), 48px
high, cream `#f5f5f0` fill with a 1px same-colour border at a 10px radius
and ink text). Scrolling lands on cream manifesto sections with 48/53
headings ([section-h2](components/crops/section-h2-default.png)) and ends in
the ink footer.

## The Textile Room

`/collection` is the public catalogue
([collection-light-default](screenshots/collection-light-default.png)): an
80/84 `Textile Room` title
([page-title](components/crops/page-title-default.png)), then a sticky
cream filter bar ([filter-bar](components/crops/filter-bar-default.png),
124px) holding `Select colors (max 3)` and nine 32px colour chips — each a
9999px circle with a 1px `#ccccc4` ring that turns `#999993` on hover and
carries its textile colour on a 26px inner disc
([colour-chip](components/crops/colour-chip-default.png)) — and a `Pattern`
dropdown trigger ([pattern-dropdown](components/crops/pattern-dropdown-default.png),
160 x 32, white with the same `#ccccc4` border at 10px, taking a 10%-black
wash on hover). `Show all filters` exists in the DOM but renders 0x0 at
this width — recorded missing. The `35 textile families` grid runs
321.5 x 357.5 cards ([textile-card](components/crops/textile-card-default.png)):
a square 10px-radius image tile with a 9999px `Collaboration` badge (1px
`#999993` outline), a 30%-black scrim and a 32px cream circle action, over
a cream 12/16 label. Toggling the BLUE chip shoots
[collection-light-filtered](screenshots/collection-light-filtered.png) — a
local filter state, nothing submitted. The full page is very long
([collection-light-full](screenshots/collection-light-full.png), 31,333px,
stitched under the shooter's eight-chunk cap).

## The textile detail page

`/collection/blink` is the product surface
([textile-light-default](screenshots/textile-light-default.png)): a PHOTO /
RENDER viewer ([textile-light-render](screenshots/textile-light-render.png)
shows the RENDER state toggled by the site's own button), a `Collaboration`
badge and `Share` button, the 48/48 `Blink` title
([textile-title](components/crops/textile-title-default.png)) with story
copy and `SKU: BLI0014`, then the `Configure textile` panel — colour
circles (the same chip language as the filter bar) and Base/Balance/Bold
tone cards. The `Sample` tab
([view-tab](components/crops/view-tab-default.png), 224 x 36, cream on the
`#ccccc4` border at 10px) sits over the ink `Order sample` action
([order-cta](components/crops/order-cta-default.png), 425 x 48). Below,
the Material / Performance-specs / Suggested-use / Downloads accordion
rows ([spec-row](components/crops/spec-row-default.png)) and a `Download
textile passport` CTA — all measured, never followed.

## The login panel

Signing out lands on `/login` — the `Log in to continue` panel
([login-dialog](components/crops/login-dialog-default.png), 420 x 648 on
the cream page): the 48px `Email` and `Password` fields
([login-email](components/crops/login-email-default.png),
[login-password](components/crops/login-password-default.png)) in white
with the shared `#ccccc4` border at 10px and `#646e69` placeholders, a
`Forgot password?` link ([forgot-link](components/crops/forgot-link-default.png)),
the `Don't have an account? Sign up` line
([signup-link](components/crops/signup-link-default.png), hover turns it
`#646e69`), and the ink `Login →` button
([login-button](components/crops/login-button-default.png), 356 x 48). The
panel gates the Design Studio — every field was measured, nothing was
typed or submitted.

## The contact form and FAQ

`/contact` centres an 80/84 `Contact us` title
([contact-title](components/crops/contact-title-default.png)) over the
only real form on the public surface: 623px-wide First-name, Email and
Inquiry-select fields and a 104px textarea — all white with the `#ccccc4`
border at 10px ([text-field](components/crops/text-field-default.png),
[email-field](components/crops/email-field-default.png),
[select-field](components/crops/select-field-default.png),
[text-area](components/crops/text-area-default.png)) — plus a small ink
`Send` button ([submit-button](components/crops/submit-button-default.png),
86 x 48) and the named contact blocks
([person-card](components/crops/person-card-default.png)). `/faq` pairs an
80/84 title ([faq-title](components/crops/faq-title-default.png)) with
719 x 56 question rows
([faq-question](components/crops/faq-question-default.png)); a row's own
toggle opens the accordion for
[faq-light-open](screenshots/faq-light-open.png).

## The ink footer

Pages end on the ink `#1b1b1b` footer panel
([footer](components/crops/footer-default.png), 537px, 24px top radius —
a rounded cap on the cream page): white 10/12.5 link columns
([footer-link](components/crops/footer-link-default.png)), a social row
([social-icon](components/crops/social-icon-default.png)), and a `#454542`
divider — the same dark-on-dark line that separates the link groups from
the small print.

## Mobile

At 390 the header keeps wordmark plus a 32px menu button
([m-header](components/crops/m-header-default.png),
[m-menu-button](components/crops/m-menu-button-default.png)). The opened
menu is a full-screen cream `aside` panel
([m-menu-open](components/crops/m-menu-open-default.png), 390 x 844):
`Cart` and `Login/Sign-up` rows at the top
([m-login-button](components/crops/m-login-button-default.png), 358 x 50
with the `#ccccc4` border at 8px), then 48px nav rows
([m-nav-item](components/crops/m-nav-item-default.png)) — see
[mobile-home-light-menu](screenshots/mobile-home-light-menu.png). The
display type compresses to 48px
([m-hero](components/crops/m-hero-default.png)) and the Textile Room's
filter bar and grid reflow to one column
([mobile-collection-light-default](screenshots/mobile-collection-light-default.png)).

## The hover signature

The site's one motion language: controls transition colour, background,
border and filter at 0.15s `cubic-bezier(0.4,0,0.2,1)`. Every ink button —
hero CTA, Order sample, Login, Send — keeps its shape but flips to the
`#fae210` yellow on hover, keeping a slightly deeper `#c8b50d` edge, and
pressed state scales to 0.98. Text links answer hover with `#646e69` or
black instead. The marquee never stops, including under
prefers-reduced-motion.

## Boundaries

The Design Studio — BYBORRE's configure-and-order product — sits behind
the login panel and was never reached: no studio canvas, saved designs,
dashboard, ordering, checkout or account. `/dashboard` returns a
signed-out shell only. Order-sample, cart, Get-in-touch and every external
link (help-center, news, the pcon catalogue, careers, socials) were
measured or screenshotted, never followed. See the Gaps section in
[components.md](components.md).
