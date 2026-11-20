# Endless patterns

How the measured components combine on endless.app's public surface, read
from the screenshots and the component entries in
[components.md](components.md). endless.app is one Next.js + Tailwind v4
surface — marketing pages, ~70 free tools, the model catalog, social radar,
/docs and /brand — over a single shadcn-style token layer that re-binds
under `.dark` (next-themes). Values are from the light set unless marked;
`d-*` crops are the dark-scope repeats.

## The marketing header

Every page carries the same chrome
([header](components/crops/header-default.png), 1440 x 56, sticky, on a
~90% `#fcfcfc` veil with a hairline bottom border that paints on scroll):
the mark ([logo](components/crops/logo-default.png)), flat nav links —
Product, Models, Industries, Pricing, Blog
([nav-link](components/crops/nav-link-default.png),
[nav-industries](components/crops/nav-industries-default.png), TikTok Sans
14px/20px 500) — then a bordered `Sign in`
([nav-signin](components/crops/nav-signin-default.png), 1px `--border`
outline, 8px radius, 32px high) and the near-black `Sign up for free` pill
([nav-cta](components/crops/nav-cta-default.png), `#171717` on `#fafafa`,
8px radius). There is no mega-menu or dropdown on desktop — the Industries
link navigates flat. In dark the same header re-binds to a black veil with
a `#e5e5e5` primary fill
([d-header](components/crops/d-header-default.png),
[d-nav-cta](components/crops/d-nav-cta-default.png)). Hover lifts links to
the foreground colour; keyboard focus draws the 3px 30% accent ring.

## The home hero and composer

The home page centres its pitch
([home-light-default](screenshots/home-light-default.png)): the display
headline `What do you want to make?`
([hero-title](components/crops/hero-title-default.png), TikTok Sans
59.2px/63.9px 500 at -1.9px tracking), the lede
([hero-lede](components/crops/hero-lede-default.png), muted 18px), then the
Ask-Endless prompt composer
([composer](components/crops/composer-default.png), 660 x 122): a
20px-radius card on a floating multi-layer shadow holding the text input
([composer-input](components/crops/composer-input-default.png), 660 x 72 —
[captured focused](screenshots/home-light-composer.png) and filled with
deleted sample text), a model pill
([mode-pill](components/crops/mode-pill-default.png), 36px, bordered,
with the model name and a chevron), a row of prompt chips
([prompt-chip](components/crops/prompt-chip-default.png), 36px pills on
`--card` with a 1px border) and the 36px send well
([composer-send](components/crops/composer-send-default.png), 12px radius
on `--secondary`, arrow glyph). Nothing was ever sent — Generate and send
actions were measured, not pressed. The dark hero repeats the composition
on the black field
([d-composer-input](components/crops/d-composer-input-default.png),
[home-dark-composer](screenshots/home-dark-composer.png)).

## Pricing

/pricing ([pricing-light-default](screenshots/pricing-light-default.png))
centres the title ([pricing-h1](components/crops/pricing-h1-default.png))
above a Monthly/Annual segment
([billing-toggle](components/crops/billing-toggle-default.png), 96 x 32
full-pill; the toggled page is
[pricing-light-annual](screenshots/pricing-light-annual.png)) and a credits
slider ([credits-slider](components/crops/credits-slider-default.png)).
Plan cards ([plan-card](components/crops/plan-card-default.png), 273 x 612
at a 16px radius on `--card` with a 1px border) carry the plan name
([plan-name](components/crops/plan-name-default.png)), price
([plan-price](components/crops/plan-price-default.png)) and a full-width
CTA ([plan-cta](components/crops/plan-cta-default.png)) — the dark set is
[pricing-dark-default](screenshots/pricing-dark-default.png). FAQ rows
([faq-item](components/crops/faq-item-default.png)) close the page.

## A free tool page

/tools indexes ~70 free tools ([tools-light-full](screenshots/tools-light-full.png)).
A tool page, here the AI image generator
([toolgen-light-default](screenshots/toolgen-light-default.png)), runs the
title ([tool-title](components/crops/tool-title-default.png)) over a
controls panel ([tool-panel](components/crops/tool-panel-default.png),
504 x 114) with the prompt field
([tool-prompt](components/crops/tool-prompt-default.png), 504 x 64 —
[focused](screenshots/toolgen-light-prompt.png)) and the Generate button
([tool-generate](components/crops/tool-generate-default.png), 52px, the
big-radius primary). Steps are explained by
[tool-step](components/crops/tool-step-default.png) rows. Generate was
never pressed; the result gallery is a recorded gap.

## The model catalog

/models ([models-light-default](screenshots/models-light-default.png))
opens on the title
([models-title](components/crops/models-title-default.png)), a 256 x 32
search field
([models-search](components/crops/models-search-default.png), captured
[focused and filled](components/crops/models-search-filled.png)) and
modality links ([mode-tab](components/crops/mode-tab-default.png),
[mode-pill](components/crops/mode-pill-default.png)) — Chat, Image, Video,
Audio, 3D — then a grid of model cards
([model-card](components/crops/model-card-default.png), 354 x 200 anchors
at a 16px radius) linking out through
[model-link](components/crops/model-link-default.png). /model-index is a
static capability/price table
([model-index-light-full](screenshots/model-index-light-full.png)).

## The contact form

/contact ([contact-light-default](screenshots/contact-light-default.png))
is an unpainted 640px column
([contact-form](components/crops/contact-form-default.png)): 40px fields
([field-name](components/crops/field-name-default.png),
[field-email](components/crops/field-email-default.png),
[field-company](components/crops/field-company-default.png)) on a
translucent ~50% neutral fill at an 8px radius, a 64px message textarea
([field-message](components/crops/field-message-default.png)) and the
640 x 52 Send button
([send-btn](components/crops/send-btn-default.png), the `lg` 12px-radius
primary). Focus paints the accent ring
([field-email-focused](components/crops/field-email-focused.png),
[contact-light-field](screenshots/contact-light-field.png)); the fields
were filled with deleted sample text
([field-name-filled](components/crops/field-name-filled.png)) and never
submitted.

## Radar, docs, blog, brand

/radar lists social trend rows
([radar-row](components/crops/radar-row-default.png)) under the title
([radar-title](components/crops/radar-title-default.png)) with a copy
action ([radar-copy](components/crops/radar-copy-default.png)) and a
why-this link ([radar-why](components/crops/radar-why-default.png)) — there
is no search input on the public page. /docs is a sidebar shell
([docs-sidebar](components/crops/docs-sidebar-default.png)) of nav items
([docs-nav-item](components/crops/docs-nav-item-default.png)) plus a
search button
([docs-search](components/crops/docs-search-default.png)) and the page
heading ([docs-h1](components/crops/docs-h1-default.png)); /mcp shows a
Geist Mono code block
([mcp-code](components/crops/mcp-code-default.png)) with a copy button
([mcp-copy](components/crops/mcp-copy-default.png)). /blog is category
pills ([blog-pill](components/crops/blog-pill-default.png)) over post
cards ([blog-card](components/crops/blog-card-default.png)); /brand lists
logo blocks
([brand-logo-block](components/crops/brand-logo-block-default.png)),
colour swatches
([brand-swatch](components/crops/brand-swatch-default.png)) and download
buttons ([brand-btn](components/crops/brand-btn-default.png)).

## The footer

The footer ([footer](components/crops/footer-default.png)) runs muted
14px link columns ([footer-link](components/crops/footer-link-default.png)),
a Cookie settings button
([cookie-btn](components/crops/cookie-btn-default.png)) and the icon-only
Theme control
([theme-toggle](components/crops/theme-toggle-default.png), aria-label
`Theme: system. Switch to light`) — the user's own control for the same
`.dark` scope the `-dark` captures emulate.

## Mobile

At 390 x 844 the chrome collapses to
[m-header](components/crops/m-header-default.png): mark, a 36px menu
button ([m-menu-button](components/crops/m-menu-button-default.png)) and
the Sign-in link. The button opens a full overlay
([m-menu-open](components/crops/m-menu-open-default.png),
[mobile-home-light-menu](screenshots/mobile-home-light-menu.png)) of
stacked nav items
([m-nav-item](components/crops/m-nav-item-default.png)) — the site's only
menu overlay. The hero shrinks to
[m-hero](components/crops/m-hero-default.png) and the composer to a
346px-wide input row
([m-composer](components/crops/m-composer-default.png),
[mobile-home-light-full](screenshots/mobile-home-light-full.png) —
part-stitched; the pricing, tool and models pages also have
`mobile-*-full` stitched shots).
