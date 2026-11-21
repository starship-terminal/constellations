# aaply patterns

The recurring shapes the marketing pages are built from. Everything below was
measured on the live site; the component entries and crops are in
[components.md](components.md).

## Floating pill nav

A 1200px white bar rounded at `radius.card-lg` (40px), floating over the
`page-gray` field with a hairline shadow: wordmark left, Inter 18px links
centre, then the auth pair — **Log in** as a 300-weight ghost (1px `border`
grey, text fades to `hover-gray` on hover) and **Sign up** as a 44px black
pill that inverts to `lime` with black text on hover
([nav-signup hover](components/crops/nav-signup-hover.png)). On mobile it
collapses to logo + burger.

## Display headline with inline atoms

Every page opens on the same Poppins 700 57/60 heading at −1px tracking —
the signature move is dropping small image atoms (emoji, squiggles, avatars)
inside the sentence flow at 24px ([hero-title](components/crops/hero-title-default.png),
[hero-emoji](components/crops/hero-emoji-default.png)). Mobile halves it to
27/28.

## CTA pair

A lime `button-primary` pill next to a black `button-dark` pill, both 60px
tall at `radius.pill` (30px), Inter 18px: "Sign up fo free →" and "Try demo
project" ([cta-signup-free](components/crops/cta-signup-free-default.png)).
Neither hero pill changes on hover or pressed — the nav
Sign up pill's lime invert is the only dark-pill swap on the site; the lime
pill holds flat. At the foot of /features the same pattern scales up to the 520x96 mega
button at `radius.mega`.

## Chat-annotation bubbles

Fake messenger bubbles pinned over the marketing sections — white rounded
bubbles with avatar stamps ("Have you seen this?" / "Looks nice!" / "I wanna
try too"), Inter 500 ~31px white or dark depending on the surface
([chat-bubble](components/crops/chat-bubble-default.png)). They annotate
product screenshots the way collaborators would inside the app.

## Numbered workflow steps

/features walks a sequence: a circled Poppins 700 numeral (27px, −2px
tracking), a 47px step heading, a chat bubble, and a 1131px
browser-chrome-framed product panel ([step-number](components/crops/step-number-default.png),
[step-card](components/crops/step-card-default.png)). The same cards end
the figma-plugin page as export steps.

## Billing rail + plan cards

A `page-gray` rail holds two 152x60 `radius.pill` segments — the held one
paints lime on a sibling shape behind the transparent text atom — beside a
`red` "Save 30%" badge ([billing-toggle](components/crops/billing-toggle-default.png),
[save-badge](components/crops/save-badge-default.png)). The cards are
561x618 at `radius.card` (36px): Free white, Plus lime, each with a Poppins
700 name, a 35px/500 price split across `$` + numeral atoms, a feature list
and a 3D character render ([plan-card-free](components/crops/plan-card-free-default.png),
[plan-card-plus](components/crops/plan-card-plus-default.png)).

## Review wall

A wide featured slide (1157x418, `lime-slide` fill, `radius.card-lg`) with
avatar, name/role and a Poppins 35px quote, carousel dots below
([review-slide](components/crops/review-slide-default.png)); under it a
grid of 370x580 white testimonial cards
([review-card](components/crops/review-card-default.png)).

## Black footer band

The one dark surface: a full-bleed 1440x1088 black band carrying the white
"Join the early birds" heading (52px), a lime mail link (the published address is not stored)
(fades to `silver` on hover), coral social icons and the second nav list
([footer](components/crops/footer-default.png),
[early-birds](components/crops/early-birds-default.png)). The same band
closes every page.
