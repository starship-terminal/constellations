# Headspace patterns

How the measured components combine into the signed-out surfaces. Every value cited lives in [tokens.json](tokens.json); every pattern links the screenshot or crop that shows it. Captured signed out at 1440 x 900 (mobile notes at 390 x 844) from www.headspace.com, organizations.headspace.com, checkout.headspace.com and auth.headspace.com.

## The chrome

Every marketing page stacks the same three layers: a promo strip on top (the rotating offer, currently "Get 50% off"), the header (wordmark left, category links centre, Log in / Help / the offer CTA right), then the footer at the bottom (link columns, the language selector, app-store badges, legal). The header is the only sticky element; it stays light over every section.

Desktop navigation is a **hover mega-menu**: hovering a category (For You, For Business, For Providers, Our Plans, Resources, About) opens one shared panel under the bar that lists that category's sub-pages. The captured [home-light-menu](screenshots/home-light-menu.png) state was reached by a real hover, with no click and no navigation.

On a phone the categories collapse into a hamburger that opens a nav sheet ([mobile-home-light-drawer](screenshots/mobile-home-light-drawer.png)); the same six categories plus Log in, Help and the offer CTA.

## The marketing page

A topic page (meditation, mindfulness, sleep, anxiety, therapy, coaching, Ebb) is the same composition each time: a hero block (H1 in Headspace Apercu, a lede, a blue pill CTA, art or a device mock beside it), then alternating content sections — feature cards, a testimonial or stat band, a FAQ accordion — on the warm page ground, with a closing CTA section above the footer. The topic pages tint their sections in pastels (sleep cool, meditation warm); the tints are per-page readings, not a shared ramp.

The content surface works differently: [/content](screenshots/content-light-default.png) is a free-preview library — preview tiles on a tinted ground, topic links, a Subscribe CTA — and [/articles](screenshots/articles-light-default.png) is an editorial hub of card rows.

## The plans block

[/subscriptions](screenshots/subscriptions-light-default.png) puts the plan cards in a row with a billing switch (monthly/annual — the switch states were measured as components, not toggled for a shot) and a seat-count slider for family/business plans. Cards are rounded rectangles with a title, price line, feature list and a pill CTA; the recommended plan carries an accent edge.

## Forms

Signed-out forms share one shape: a rounded field (or an underlined one) with a pill submit beside or below it. The newsletter field sits in the footer; the [/code](screenshots/redeem-light-default.png) redeem page is a centred field with a Redeem button. Every field was clicked into for the `focused` reading and never filled or submitted — there are no success, error or post-submit states in this package.

## The auth surface

/login and /signup redirect to Auth0's universal pages on auth.headspace.com: a centred card on a tinted ground with the Headspace mark, an email field, a Continue button and the SSO / social options. It was measured as painted, empty — the identifier step only. Every state past Continue is a recorded gap.

## The checkout surface

checkout.headspace.com serves the self-serve plan checkout: a plan summary beside a payment form. It was viewed and measured in its arrival state only — no voucher, no card, no submit.

## The B2B surface

organizations.headspace.com is business marketing on the same stack and family — its own hero, benefit sections and a demo CTA — captured on the home and /employers pages. Its readings sit in their own component group; nothing there styles the consumer member app.

## Motion and focus

Transitions measured on the live components cluster on colour/background and transform at short durations (the motion tokens carry the readings); `prefers-reduced-motion` was probed and the result is in [raw/motion.json](raw/motion.json). Focus visibility varies: several controls draw a ring on real keyboard focus and some draw none — each entry's `focus-visible` row in [components.md](components.md) says which.

## What a page does not do

Nothing behind sign-in exists in this package: no member home, no meditation player, no streaks, no settings. No trial was started, no plan bought, no code redeemed, no form submitted anywhere. `/pricing` answers 404. These are recorded gaps, not design sources.
