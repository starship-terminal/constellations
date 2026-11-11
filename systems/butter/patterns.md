# Butter patterns

How the measured components combine on butter.video's public surface, read
from the screenshots and the component entries in
[components.md](components.md). The site paints two surfaces: the light
marketing pages (home, product, pricing, blog, mcp, contact, terms, login)
and a dark-only app shell on /explore, /blocks and /templates that is public
signed-out. Values are from the light set unless marked `dark` (the shell).

## The floating header island

Every marketing page carries the same chrome
([header](components/crops/header-default.png), 88px high): a light-grey
`#ededed` island inset from the viewport edges at a 16px radius holding the
wordmark ([logo](components/crops/logo-default.png), a 107 x 23 SVG),
the `Co-Create` and `Product` dropdown triggers
([nav-trigger](components/crops/nav-trigger-default.png)), the plain
`Blocks`/`Templates`/`Pricing`/`Blog` links
([nav-link](components/crops/nav-link-default.png), DieGrotesk 16/20 with
0.7px letterspacing), then `Login` and the dark `#1e1e1e` `Try for free`
pill ([nav-cta](components/crops/nav-cta-default.png), 39px high on a 10px
painted radius). The triggers open a grey `#ededed` dropdown panel listing
feature rows ([nav-dropdown](components/crops/nav-dropdown-default.png),
[menu-link](components/crops/menu-link-default.png),
[home-light-menu](screenshots/home-light-menu.png)). Keyboard focus draws a
1px `#3c3c3c` zero-offset shadow ring on links and a 3px `#4dc5e5` outline
offset 3px on the buttons' inner layer — the same cyan the buttons keep
inside.

## The home hero

The home page opens on the keyring artwork over white
([home-light-default](screenshots/home-light-default.png)): a centred
`Engineered for Creativity` display headline in DieGrotesk at 107.57px /
106.7px ([hero-title](components/crops/hero-title-default.png)), a 24px lede
([hero-sub](components/crops/hero-sub-default.png)) and the dark pill
`Get Started` ([hero-cta](components/crops/hero-cta-default.png), 50px high:
the anchor computes transparent — its painted child draws the `#1e1e1e`
fill at a 16px radius over a `#4dc5e5` accent layer). Playful
collaborator-cursor chips — black `#0f0f0f` pills on a 12px radius with
light text — float over the artwork
([cursor-badge](components/crops/cursor-badge-default.png)). Below the fold
a 60.4px `Butter is the first video editor where...` section head
([section-h2](components/crops/section-h2-default.png)) leads feature bands
and editor screenshots ([home-light-full](screenshots/home-light-full.png)).

## Pricing

`/pricing` centres `Unlimit your creativity.` at the same 107px
([pricing-h1](components/crops/pricing-h1-default.png)) over a sub-line and
the billing toggle ([billing-toggle](components/crops/billing-toggle-default.png)):
a pill rail of `Monthly`/`Annually` buttons — the selected one paints dark
`#1e1e1e` with a `#fafafa` label — plus a `Save 28%` grey tag. Four
308 x 1133 plan cards follow on the `#ededed` field at a 32px radius
([plan-card](components/crops/plan-card-default.png)): a `#fafafa` 16px name
chip (`Free`, `Basic`, `Pro` with a `Most popular` flag, `Business`), a
60.4px price figure ([plan-price](components/crops/plan-price-default.png) —
$18 annually / $25 monthly), the feature list and the 70px-high
`Choose …` dark pill ([plan-cta](components/crops/plan-cta-default.png)).
The comparison table is an accordion of 1px-`rgba(15,15,15,0.15)`-topped
rows ([feature-row](components/crops/feature-row-default.png)), and the
`Frequently Asked` block pairs a text column with `AccordionTrigger`
questions ([faq-item](components/crops/faq-item-default.png)) — measured
closed, never expanded.
[pricing-light-monthly](screenshots/pricing-light-monthly.png) shows the
toggled Monthly state; the prices were never followed to checkout.

## The dark app shell

`/explore`, `/blocks` and `/templates` hand off to a dark MUI surface that
is public signed-out ([explore-dark-full](screenshots/explore-dark-full.png),
[blocks-dark-full](screenshots/blocks-dark-full.png),
[templates-dark-full](screenshots/templates-dark-full.png)). A 283px
sidebar on the `#0a0909` canvas
([d-sidebar](components/crops/d-sidebar-default.png)) holds the wordmark,
`Home`/`Explore`/`Templates`/`Blocks` nav items — the active one a
`#252525` pill on a 12px radius
([d-nav-link](components/crops/d-nav-link-default.png), dieGroteskA 14/20)
— `More`/`Blog` links, then `#1d1d1d` `Log in` and inverted `#f5f5f5`
`Sign up` buttons at 10px radii
([d-login](components/crops/d-login-default.png),
[d-signup](components/crops/d-signup-default.png)). The content column runs
24px section heads ([d-section](components/crops/d-section-default.png) —
`What's New?`) over two card kinds: 637 x 437 feature cards in `#151515` on
a 1px `#212121` hairline at 32px
([d-card](components/crops/d-card-default.png)) and 359 x 181 block tiles at
42px ([d-block-card](components/crops/d-block-card-default.png)); both shrink
~2% on hover. The shell's controls transition at 0.16s — faster than the
marketing's 0.5s fades.

## The footer

Marketing pages end on a `#ededed` footer field
([footer](components/crops/footer-default.png), 1127px tall): link columns
in DieGrotesk 20.7px ([footer-link](components/crops/footer-link-default.png)),
social rows ([social-icon](components/crops/social-icon-default.png)) and
ABCDiatype 13.5px small print at 50% black.

## Mobile

At 390 the header island slims to 76px keeping wordmark and menu button
([m-header](components/crops/m-header-default.png),
[m-menu-button](components/crops/m-menu-button-default.png)); the opened
menu stacks 73px rows for Product/Blocks/Templates/Pricing plus MCP, the
socials and Blog ([m-menu-open](components/crops/m-menu-open-default.png),
[m-nav-item](components/crops/m-nav-item-default.png),
[mobile-home-light-menu](screenshots/mobile-home-light-menu.png)). The
display type compresses to 56.7px
([m-hero](components/crops/m-hero-default.png)) and the dark shell keeps its
sidebar as a drawer
([mobile-explore-dark-full](screenshots/mobile-explore-dark-full.png)).

## Boundaries

The editor — workspace, projects, exports, billing, the API-key flows the
/mcp page advertises — sits behind /login and was never reached. /login was
captured as a surface, never filled or submitted; every Try-for-free,
Get-Started and Choose-plan action was measured, never followed. See the
Gaps section in [components.md](components.md).
