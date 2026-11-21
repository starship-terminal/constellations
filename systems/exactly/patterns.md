# Exactly.ai patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

## Marketing chrome (over image)

The home header floats over the photo hero with everything inverted: white wordmark, white Industries/Showcase/Case studies/Pricing links (`light.on-image.ink`), a ghost Log in and a white Start-for-free pill (`light.pill.light` on `light.pill.light-ink`). On interior pages the same shell repaints to `light.ink` links and a `#fb411f` (`light.accent`) Start-for-free. The hero's own actions pair the white pill with a translucent Book-a-demo pill: `light.on-image.glass` 10% white fill behind a `light.on-image.line` 20% white edge — the recurring on-image recipe.

## Photo hero + content sections (light)

A full-bleed brand photograph carries the 47px/60px wght-300 Inter display (`light.on-image.ink`, letter-spacing −1.88px) over a two-line white sub at 60% (`light.on-image.muted`) and the two pills. Sections below are white (`light.canvas`) with `light.ink` headings in the same wght-300 voice, `light.muted` body copies, and `#f7f7f7` (`light.surface.card`) fields at 40px radius for cards and strips. The trusted-by wall is a row of white-on-transparent partner marks — content, not components.

## Pricing

A centered headline, then three `#f7f7f7` plan cards at 40px radius (`light.surface.card`, `radius.card`): each opens with a monochrome glyph (the plan icons in [icons/](icons)), the plan name, price line and feature rows, and ends in a dark `#1e1e1e` pill (`light.pill.dark`/`light.pill.dark-ink`) — Start for free, Book a demo, Contact us. A sticky compare bar (white, 1000px pill outline) offers Solo/Team/Enterprise jumps, and a closing strip answers pricing FAQs. Small plus markers (`icons/plus.svg`) punctuate section corners.

## Showcase and case studies

/showcase is a cover grid: large image cards whose captions sit on the image (the on-image whites again). A brand page (/showcase/revolut) stacks the brand headline, a category line and a gallery of generated-image panels. /case-studies lists 767×240 rows with a Read-study pill; the article page itself is a 47px display headline, a meta strip, then Inter body prose with pull-quotes and h2 sub-heads — the only longform surface captured.

## Industries

/industries tiles wide image cards (industry-card, 708×892) linking to per-industry pages; the industry page is hero + 27px/36px sub-head + section bodies plus the same pill CTAs and plus markers.

## Help center

A doc layout on white: a left rail of article links grouped under small caps labels (Getting started, AI style transfer, Library…), each a `help-nav-link`; the Search… trigger opens Framer's own search modal with a `Search...` input (measured default/focused/filled, never submitted). Article-collection cards are 640×296 at 40px radius on the 8% warm-grey wash (`light.surface.chip`). FAQ "answers" are ordinary anchor-linked `<h3>` headings on a single FAQ article — there is no accordion.

## Book a demo

Headline plus the embedded scheduler at rest inside its iframe: a bordered panel with a calendar grid and a times column. No day, time or contact field was ever touched — the scheduler's interactive states are a documented gap. Its cookie line was hidden, never answered.

## Mobile (390 wide)

A 56px top bar carries the wordmark, a white Join pill and the hamburger (`light.focus.ring-mobile` #e59700 focus ring — the colour Chrome's phone emulation uses for its own `auto` ring, as #101010 is on the desktop pass; the site sets no focus colour). The hamburger toggles a nav overlay of drawer links; the hero display drops to 27px/36px over the same photograph recipe.

## Onboarding shell (signed in, 2026-11-21)

The only signed-in screen this pass could open. A `#f0f0f0` page (`--color-background-tertiary`) holds a white 360 x 480 card at 32px radius, centered at 1440. A 4px accent bar (`#fb411f`, aria value 14) runs across the top. Log out is a white 36px pill at the top left. The title is Exactly Display at 22.5px / 28px. Four choices sit on `#7c7c7c` at 6% opacity, 20px radius, 80px tall. At 390 the card docks to the bottom, radius `32px 32px 0 0`, and the last choice is clipped. The help and chat circles are desktop only. No option was selected. See [onboarding-light-default.png](screenshots/onboarding-light-default.png).

## Footer

Every page ends in the near-black footer (`light.footer.bg` #000): white column heads and `light.footer.muted` 60% links, with the watermark wordmark set beneath — the only near-dark surface the public site paints.
