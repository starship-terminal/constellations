# Editor X / Wix Studio patterns

How the measured components combine on the surface editorx.com now serves
(the editorx.com → wix.com/studio redirect shell), read from the screenshots
and the component entries in [components.md](components.md). The surface
paints one light theme; the only dark paint is the `#0e0e0e` chrome (the
footer) — a section treatment, not a user toggle. Every display
size is spx-scaled to the viewport, so the px values below are the 1440px
readings unless marked mobile (390px).

## The chrome: white header, purple square CTA

Every desktop page opens on a fixed white 56px header
([nav-bar](components/crops/nav-bar-default.png)): the Wix Studio wordmark
([logo](components/crops/logo-default.png), ~84 x 56 hitbox, Madefor
Display), the `Product` / `Resources` / `Enterprise` dropdown triggers
([nav-trigger](components/crops/nav-trigger-default.png), 16px regular —
the label takes the 700 face on hover rather than changing colour), the
plain `Pricing` [nav-link](components/crops/nav-link-default.png), the
language globe ([nav-lang](components/crops/nav-lang-default.png), 24 px),
`Log In` ([nav-login](components/crops/nav-login-default.png)) and the
`Start Creating` action ([nav-cta](components/crops/nav-cta-default.png),
175 x 57, `#3910ed` fill, sharp 0px corners, white 16px Madefor Text, 35px
side padding, a 0.4s ease colour transition). Keyboard focus inside the
header draws the ink double ring: 1px + 3px `#000` box-shadows
([nav-link focus-visible](components/crops/nav-link-focus-visible.png)).

The `Product` trigger opens a full-width mega-menu
([nav-dropdown](components/crops/nav-dropdown-default.png), ~1440 x 510 —
see [home-light-menu](screenshots/home-light-menu.png)): a transparent
panel over the page with a 1px `#d8e2ec` top hairline and 47-100px
padding, its links
([menu-link](components/crops/menu-link-default.png), 18px Madefor
Display Bold) going `#3910ed` on hover and pressed.

## The home hero and the scroll-jacked showcase

The hero is set in wix-madefor-display-v2 at 80.25/88.27 with -2.4px
tracking — `Design with impact / Deliver at scale`
([hero-title](components/crops/hero-title-default.png)) — over the 18/28.8
lede ([hero-sub](components/crops/hero-sub-default.png)) and the `Start
creating →` stadium pill
([hero-cta](components/crops/hero-cta-default.png), 221 x 56, the purple
fill painted on a child layer with a ~1124px computed radius cap, the
label wix-madefor-text-v2 23.25/32.55 white). Focus-visible on the pill
draws the content ring — 2px white + 4px `#116dff` — that every content
control shares
([hero-cta focus-visible](components/crops/hero-cta-focus-visible.png)).
Below it a framed editor screenshot, then the `Site of the week`
scroll-jacked showcase
([showcase-card](components/crops/showcase-card-default.png), a 1440 x
2320 pinned section — [home-light-mid](screenshots/home-light-mid.png)
catches it mid-pin), 54/54 section headings
([section-h2](components/crops/section-h2-default.png)), 50px-pill
`Explore`-style links
([section-link](components/crops/section-link-default.png)) and the FAQ
repeater — rows of 24/31.2 medium-weight questions over hairlines
([faq-question](components/crops/faq-question-default.png), opening to
~442px on toggle). The page closes on the lime band
([cta-band](components/crops/cta-band-default.png), 1269 x 171 `#deff00`
with a 1px `#c7c7c7` top edge).

## The inner pages: one giant display each

Every sub-page leads with the same quiet device — one enormous
regular-weight display at 1.0 line-height: 157.5px on
/studio/design ([design-h1](components/crops/design-h1-default.png)),
75px academy, 72.6px inspiration, 60.9px features, 60px enterprise
([ent-h1](components/crops/ent-h1-default.png)), then 48-54px section
headings under it. Actions split by intent: the purple square
[design-cta](components/crops/design-cta-default.png) repeats the header
treatment, while the enterprise page swaps to a black 50px stadium
([ent-cta](components/crops/ent-cta-default.png), 144 x 52, 0.2s
transition) — the secondary-action grammar is black pills, not purple
outlines.

## Plans: bordered cards, navy accent edge, mint badge

wix.com/studio/plans rows white 202 x 574 plan cards
([plan-card](components/crops/plan-card-default.png)): sharp corners, 1px
`#dfe5eb` borders on three sides, the recommended card topping its
`#0e106a` 3px accent edge and floating on the page's only measured
elevation (an ink-plans wash: `rgba(0,6,36,0.05)` 6px + `rgba(0,6,36,0.1)`
18px). Inside, the `#000624` ink carries 700 18/24 headings
and the 10/24 700 `RECOMMENDED` label on its `#a6ffd8` mint badge
([plan-badge](components/crops/plan-badge-default.png)); prices set in
the plain-Madefor stack at 14/18 500
([plan-price](components/crops/plan-price-default.png)). At 390 the same
grid stacks vertically
([mobile-plans-light-full](screenshots/mobile-plans-light-full.png)).

editorx.com/pricing itself — the one path still served on the editorx
domain — answered with the Wix error pane at capture time: `Couldn't
load Premium plans due to a technical issue` in 18/24 700 over a 14/18
explanation and the `#116dff` Refresh link
([pricing-refresh](components/crops/pricing-refresh-default.png)),
documented in
[pricing-light-default](screenshots/pricing-light-default.png). The link
darks to `#0f62e6` on hover and takes a 1px auto `#005fcc` outline on
keyboard focus — the surface's only real outline-style ring.

## Galleries: filters, white 2px cards

/studio/inspiration runs a filter row of 32px chips
([inspo-filter](components/crops/inspo-filter-default.png)) over the
site-of-the-week grid ([inspo-card](components/crops/inspo-card-default.png),
~634 x 432 media blocks over `rgba(238,238,238,0)` placeholder paint).
/studio/templates tiles 298 x 395 white cards
([template-card](components/crops/template-card-default.png)) at the
surface's only nonzero card radius — 2px — with a white 21px-radius
action inside (`a.wds-button-core`, 102 x 42 at the 530 variable weight)
over a media block that reads `rgba(0,0,0,0.8)` dim while loading. No
shadows anywhere; borders do the separation.

## The dark footer

Every page ends on the #0e0e0e footer
([footer](components/crops/footer-default.png), 1440 x 793): Madefor
Text links at 16/34 in `#f6f6f6`
([footer-link](components/crops/footer-link-default.png)) that dim to
`#828282` on hover and pressed, an `#848280` hairline separating the
columns, and 36px social buttons as 50% circles on a 1px `#f6f6f6` ring
([social-icon](components/crops/social-icon-default.png)). Focus on dark
draws the `#828282` double ring.

## Mobile (390 wide)

The header collapses to a white 390 x 47 bar over a `#d8e2ec` hairline —
wordmark + `Start Creating` + the 50 x 46 burger
([m-header](components/crops/m-header-default.png),
[m-menu-button](components/crops/m-menu-button-default.png)); the purple
CTA keeps its fill at phone width. The menu opens as a white full panel
([m-menu-open](components/crops/m-menu-open-default.png), 390 x 797 —
see [mobile-home-light-menu](screenshots/mobile-home-light-menu.png)) of
50px rows at 15px/27px padding
([m-nav-item](components/crops/m-nav-item-default.png)) with the same
ink double focus ring. The hero display scales down with the viewport to
34.53/37.98 ([m-hero](components/crops/m-hero-default.png), -0.35px
tracking) — the spx scale in action.

## The state signature

- **Hover** never adds fills on this surface: links recolour (`#3910ed`
  on menu links, `#0f62e6` on link blue, `#828282` on the dark chrome),
  nav triggers swap to the 700 face, and that is it. No wash states, no
  lifts.
- **Focus-visible** is a double box-shadow ring everywhere, tinted per
  surface: white 2px + `#116dff` 4px on content controls, `#000` 1px +
  3px in the header, `#828282` 1px + 3px on the dark chrome, a bare 1px
  auto `#005fcc` outline on the inline link-blue control, and a 3px
  `#116dff` outline on the standalone Refresh link.
- **Pressed** is DevTools-forced `:active:hover`; the mega-menu links
  hold the `#3910ed` colour and the footer links hold `#828282` — no
  distinct pressed paint.
- **Motion** is short and plain: 0.4s ease colour transitions on the
  CTAs, 0.2s `all` on the wixui buttons, and view-transition slices
  (0.6s slide, 0.35s out-in fades) on page navigation.

## Boundaries

The Studio editor, workspaces, dashboards, signup and checkout sit behind
Log In / Start Creating — measured, never followed. The /pricing plans
data is a server-side error at capture time. Nothing here verifies the
product itself.
