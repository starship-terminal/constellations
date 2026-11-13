# Deel patterns

How the components in [components.md](components.md) combine into the public marketing pages. Every value is in [tokens.json](tokens.json); the crops are in [components/crops/](components/crops) and the page captures in [screenshots/](screenshots).

## The chrome band

Every page carries the same two rows: a 64px `#1b1b1b` promo strip (`component.promo-banner-height`) — a `#b1d8fc` 2px-radius SPECIAL OFFER chip, 12px Inter copy, a 32px white 200px-radius Claim-offer pill and a close control — then an 80px white nav (`component.nav-height`): the 78px wordmark, 15px/500 BagossStandardVF dropdown items (Solutions, Use cases, Who we serve, Resources), plain Pricing, the EN locale switch, Log in, and the 40px-tall `#1b1b1b` Book-a-demo pill at 200px radius. The header is sticky; at 390px it collapses to a 64px bar with a 40px hamburger circle that opens a drawer.

## The purple hero

The home opens on a 732px `#201547` panel (`light.background.hero-panel`, `component.hero-panel-height`): a 60px/500 white BagossCondensed headline over five glass action tiles — 181x80, 4%-white fill (`light.background.tile-glass`), 10%-white hairline (`light.border.tile-glass`), 12px radius (`core.radius.card`) — that switch a preview panel like tabs, plus a 375x51 rounded-full white Book-a-demo pill (`core.radius.full`, computed as a huge px value by Tailwind's `!rounded-full`). On /hr/ the same shape returns as a 430x51 white CTA; mobile drops the headline to 38px.

## Cards, tiers and accordions

Below the hero the page returns to white: the global-people-platform grid holds 419x438 product cards (hover lifts), the AI-readiness band, and a 1206px video-carousel band whose review video sits on a `#141414` card (`light.background.video-card`). /pricing/ runs a 56px BagossCondensed dark hero into 459x928 white tier cards on the elevation-2dp shadow (`core.shadow.card`) — a 16px `#b1d8fc` top strip on the featured tier, a full-width 51px `#1b1b1b` pill CTA — then the FAQ: 952x80 MUI accordion summaries split by a 1px latte-at-16% hairline (`light.border.hairline`), opened by their own click toggle.

## The footer

A ~1015px footer (`component.footer-height`) on `#1b1b1b` (`light.text.ink`/`color.surface.dark`): `#faf4ee` cream column headings (`light.text.cream`, 16px BagossCondensed 500) over link lists painted as 14px/23.8px Inter 560 in `#faf4ee` (the link's text child, not the wrap's inherited ink), with 32px social icon buttons.

## Mobile

At 390px the promo strip drops, the nav shrinks to 64px with a circular hamburger, the hero heading drops to 38px, and the drawer carries the menu; the pricing page keeps its tier cards stacked.
