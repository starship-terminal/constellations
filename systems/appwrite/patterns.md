# Appwrite patterns

How the measured components combine on appwrite.io's public surface, read
from the screenshots and the component entries in [components.md](components.md).
Every page pins `html.dark`; all values are from the dark set unless noted.

## The shell

A dismissable announcement banner sits above the fixed 56px header
([home-dark-default](screenshots/home-dark-default.png)): wordmark left,
nav links and the Products/Solutions flyout buttons centre-left, GitHub stars,
ghost Sign in and filled Sign up right. At 390px the links collapse into the
hamburger, whose own toggle opens a left sheet of 40px nav rows
([mobile-home-dark-menu](screenshots/mobile-home-dark-menu.png),
[m-nav-link](components/crops/m-nav-link-default.png)).

## Hero and CTA pattern

Every landing page opens with a large Aeonik headline (48px+ on home, 36–40px
in sections), the first line often carrying the pink→orange gradient through
background-clip ([hero-title](components/crops/hero-title-default.png),
[measured.hero-gradient](tokens.json)). Actions come in three weights:
filled brand pink (`--brand-cta` #fd366e) for the one that ends a flow
("Start project", "Sign up"), a hairline-bordered ghost for the alternative
("View docs", "Contact us"), and a muted-foreground text link for the rest.

## Cards and pricing

Feature and plan surfaces are 14px-radius cards with a 1px hairline border and
a translucent muted tint (`measured.card-tint`) rather than shadows
([plan-card](components/crops/plan-card-default.png),
[product-card](components/crops/product-card-default.png)). Pricing is three
columns — Free / Pro / Enterprise — each a self-contained card with its own
CTA, followed by hairline-separated 60px FAQ accordions
([faq-question](components/crops/faq-question-default.png),
[pricing-dark-faq](screenshots/pricing-dark-faq.png)).

## Docs

The docs chrome swaps the marketing header for a search bar
("Search documentation ⌘K"). Opening it mounts a dialog; a query was typed and cleared, never submitted
([docs-dark-search](screenshots/docs-dark-search.png)). A 195px sidebar of 32px
nav rows with the current item muted-filled ([docs-nav-active](components/crops/docs-nav-active-default.png)),
and prose with `--code-*` syntax colours on a darker `--editor-bg` block
([code-block](components/crops/code-block-default.png),
[docs-react-dark-full](screenshots/docs-react-dark-full.png)).

## Blog and changelog

The blog index is a featured tile followed by 384px story cards: image,
two-line headline, author row ([post-card](components/crops/post-card-default.png)),
plus a "Search articles ⌘K" trigger and category links. Changelog entries
stack as dated rows on the same dark ground.

## The sign-in gate

The public `/sign-in` card ([signin-card](components/crops/signin-card-default.png),
[sign-in-dark-default](screenshots/sign-in-dark-default.png)) is the densest
form on the site: OAuth provider rows (wide GitHub + square GitLab/Bitbucket
icon buttons), Google and passkey buttons, then labelled 36px fields
(fields focused with `element.focus()`, never typed into) with an inline
show-password toggle, a forgot-password link and the full-width Login.
It is a real form. Nothing was typed, clicked through, or submitted.
