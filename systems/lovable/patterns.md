# Lovable patterns

How the measured components combine on the public site. Values are the ones in [components.md](components.md) and [tokens.json](tokens.json).

## Marketing shell

A sticky 56px header sits over a `#f5f5f5` page (`light.page`). Nav items are pill buttons. Log in is a white pill. Get started is an inverse pill (`light.inverse`, near-black at 88% opacity, near-white text). The header itself paints no fill. See [home-light-default](screenshots/home-light-default.png).

On a phone the same header collapses to a menu trigger. Opening it is a local press. See [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png).

## Prompt composer

The home hero is a small kicker ("AI App Builder", 18px, weight 480) over a chat-shaped field. The field is labelled "Chat input". Beside it sit an Additional actions icon button (32px) and a Build chip. Focusing the field does not send it. Nothing was typed into a send path. See [prompt-field-default](components/crops/prompt-field-default.png).

## Pricing

A Monthly / Yearly segment sits above plan cards. Yearly is a local toggle, not a purchase. Each plan has a Get started link (36px high, pill) and a credit combobox ("100 monthly credits"). The Pro plan's CTA uses the special purple (`light.special` `#8e48ff`). The combobox list was not opened, so no checkout started. One FAQ row expands in place. See [pricing-light-default](screenshots/pricing-light-default.png) and [pricing-light-yearly](screenshots/pricing-light-yearly.png).

## Log in

`/login` renders signed out. Continue with Google, GitHub and Apple are 44px by 350px, weight 480. The email field is the same size, pill radius, with an inset shadow. Continue is the inverse fill (`oklch(0 0 0 / 0.88)`, text `oklch(0.9851 0 89.88)`). Sample text was typed into the email field and deleted. Continue and the OAuth buttons were never pressed. See [login-light-default](screenshots/login-light-default.png).

## Enterprise form

`/enterprise` redirects to `/enterprise-form`, which paints dark (`dark.page` `#1d1d1c`). The demo form (name, email, phone, Submit) was not submitted. See [enterprise-form-dark-default](screenshots/enterprise-form-dark-default.png).

## Docs

docs.lovable.dev is a separate host. It uses Inter and its own blue (`rgb(0, 149, 255)`), not the marketing token set. Search opens a dialog. The theme control was not changed. The "Start building for free" link was not followed. See [docs-light-default](screenshots/docs-light-default.png) and [docs-light-search-open](screenshots/docs-light-search-open.png).

## What is missing

Empty, loading and error states do not appear on the public surface. Destructive confirmation, search filtering inside the product, and onboarding sit behind sign-in. Checkout was not reached.
