# Dona patterns

How the measured components combine on dona.ai's public surface, read from
the screenshots and the component entries in [components.md](components.md).
The site paints one light theme over a white field; the light/dark/black UI
themes the copy advertises live inside the app. All values are from the light
set unless noted.

## The header bar

Every page opens under an unpinned 68px bar
([home-light-default](screenshots/home-light-default.png)): inside the 1140px
container ([header](components/crops/header-default.png), 32px drop from the
top), a borderless ghost button marked **About** sits at the left edge — it
paints nothing until hover picks up a `#f2f4f8` wash
([nav-about](components/crops/nav-about-hover.png)) — the dona
ring-and-wordmark logo centres itself with a translate
([logo](components/crops/logo-default.png), 95x28; its anchor is display:block
at 0 width, so the mark is the SVG), and a grey `#eceff2` **Login** pill
anchors the right ([nav-login](components/crops/nav-login-default.png)).
Every button is a 32px-radius pill at 36px tall here, and the login action
opens app.dona.ai — never followed.

## The hero

The home hero centres an 84px/92.4 Inter Bold headline — "A more humane to-do
list" ([hero-h1](components/crops/hero-h1-default.png)) — over a 24px/34.8
Inter Medium lede ([hero-lede](components/crops/hero-lede-default.png)), then
two 52px pills side by side: **Watch video** in the `#eceff2` secondary grey
([watch-video](components/crops/watch-video-default.png)) and **Try for
free** in the Dona blue `#008ffd` with white text and the deeper action
shadow ([try-cta](components/crops/try-cta-default.png)). Both hover one step
darker (#e9ecef, #0087fd) on a 150ms ease.

## The app frame and the feature grid

Below the hero, a 1100x688 `#eff2f5` 20px-radius tile
([hero-video](components/crops/hero-video-default.png)) carries the product
video still inside a deep ambient shadow plus a `#e6e9ed` inset hairline
ring. Further down, feature sections pair a narrow 360px text column — 32px
SemiBold section head, 26px feature head, 18px `#616870` paragraph
([section-h2](components/crops/section-h2-default.png),
[section-para](components/crops/section-para-default.png)) — with a 2-column
grid of 534x534 `#f4f4f5` tiles at 32px gap
([feature-tile](components/crops/feature-tile-default.png); the square ratio
is a 100% padding-bottom box). Each tile and the hero frame sit over a blue
`#008ffd` ::before ellipse — a 75%-radius swoosh that is the site's signature
decoration. Scroll-in elements rise on a 1s cubic-bezier(0.17, 0.17, 0, 1)
reveal.

## The newsletter band

The bottom of home is a 1100px form
([newsletter](components/crops/newsletter-default.png)): "Join our
newsletter" copy, then a 60px email field whose text is display-sized —
Inter 40px/60, placeholder `#bfc3c8`
([email-input](components/crops/email-input-default.png), filled sample in
[email-input-filled](components/crops/email-input-filled.png)) — stretched
over its own blue swoosh at 50% opacity. The submit is an ink `#19191b` pill
with white text ([join-btn](components/crops/join-btn-default.png)) wrapped
in a `#6fabff` 140px glow ::before, and the social row under it holds the
same pill shape in blue (`#008ffd` follow) and Discord's `#7289da`. The
hidden "Thank you! You're in." success copy sits in the DOM but only shows
after a real submit — never submitted.

## The cookie banner

The consent notice floats bottom-left as a 496x76 white card at 40px radius
on three stacked `#0c1442` shadow layers
([cookie-banner](components/crops/cookie-banner-default.png),
[home-light-cookies](screenshots/home-light-cookies.png)): a 40px cookie
glyph, "This website uses cookies." with a **Learn more** link whose
underline is a 1px ink ::before bar
([cookie-learn](components/crops/cookie-learn-default.png)), and the grey
**Accept** pill ([cookie-accept](components/crops/cookie-accept-default.png))
— never clicked. On the 390 pass the consent node never painted:
[mobile-home-light-cookies](screenshots/mobile-home-light-cookies.png) shows
no banner, and the marked node read as a fixed 555x64 bar at `top:1138px` —
offscreen and wider than the 390 viewport — so the
[m-cookie-banner](components/crops/m-cookie-banner-default.png) crop caught
body text, not the banner. Its computed shadow layers run upward
(−8/−16px), the shape of a top-anchored variant, but the real phone
placement is unverified until a re-measure.

## The video modal

**Watch video** opens the site's own overlay
([home-light-video](screenshots/home-light-video.png)): a translucent
`rgba(191,195,200,.8)` scrim fills the viewport
([video-modal](components/crops/video-modal-default.png), 300ms opacity
fade) with the YouTube embed centred, and a 56px round `#b0b5ba` close
button top-right that steps to `#a8adb3` on hover
([modal-close](components/crops/modal-close-default.png)).

## About and the legal pages

`/about` reuses the same display scale — an 84px headline, a 600-weight 24px
mission block ([mission-text](components/crops/mission-text-default.png)) —
then a "Team" grid of plain 286x330 cards: a 125px 12px-radius avatar,
name, role and a row of 40px `#e0e3e7` social chips at 14px radius
([team-card](components/crops/team-card-default.png),
[social-link](components/crops/social-link-default.png)). The privacy policy
and terms pages paint one layout: the same 84px display head over a 960px
measure of 16px/23.2 body with 18px SemiBold subheads
([legal-h4](components/crops/legal-h4-default.png)) and ink text links
([legal-link](components/crops/legal-link-default.png)).

## The footer

Every page ends in a 64px-padded row ([footer](components/crops/footer-default.png)):
the wordmark, Privacy/Terms links at 14px/20.3
([footer-link](components/crops/footer-link-default.png)), and a 40px
`#eceff2` social chip to twitter.com/getdona
([footer-twitter](components/crops/footer-twitter-default.png)). Links are
ink, unstyled — the chips darken one grey step per state.

## Mobile

At 390 the same surface stacks to one column: the header keeps its About and
Login pills — there is no hamburger — the display drops from 84px to
40px/46 ([m-hero](components/crops/m-hero-default.png)), the CTAs keep their
52px height ([m-try](components/crops/m-try-default.png)), the email field
shrinks to 28px/36
([m-email-input](components/crops/m-email-input-default.png)), and the
cookie banner never appeared — its DOM node read offscreen as described
above
([mobile-home-light-default](screenshots/mobile-home-light-default.png)).
