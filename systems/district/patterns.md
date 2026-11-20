# District patterns

How the measured components combine on district.in. Read with [components.md](components.md) for the per-component values and [tokens.json](tokens.json) for the numbers.

## The app shell

Every public page carries the same sticky top bar (`nv-bar`, 1440x75): the District wordmark left, the location line (the city and state District detected for the visitor; masked in raw/ as `[city]` `[state]`, and painted out of the screenshots and crops), a centered category tab row (For you, Dining, Movies, Events, Comedy, Stores, Activities, Play — 84x36 pills, 9999px radius), and a 28x28 search affordance plus avatar at right. A black@8% hairline (`--color-border-subtle`) separates the bar from the page. The active tab is a `#eae5ff` (`--color-purple-100`) fill with a `#231268` (`--color-text-accent-purple`) 14px semibold label; inactive tabs are transparent with `#545459` (`--color-text-secondary`) ink. Tabs are real links — navigation, not JS state.

The page field below is `#ffffff` (`--color-background-primary`) with `#131316` (`--color-text-primary`) ink, ending in a `#1e1e20` (`--color-grey-800`) sitemap footer with help/contact links.

## The feed (/)

The home feed is a stack of headed rails:

- **Section heading** — a bold display line ("Top Hindi movies near you", "Artists in your District") above each rail.
- **Movie rail** — 197x348 poster cards (`mc-card`): rounded artwork over a 16px semibold title (`mc-title`), then a certificate chip + language line ("U | Hindi", "UA13+ | Hindi").
- **Artist rail** — 190x222 circular headshot cards (`ar-card`) with the artist's name underneath, linking to `/events/<slug>/artist`.
- **Venue rail** — 236x325 venue/event cards (`ev-card`): image, name, distance and address lines (the distance is painted out of the images: it measures from the visitor's location).

Rails scroll horizontally (snap-x) with a carousel arrow at the rail edge.

## The listing pages

`/movies/`, `/events/`, `/events/comedy`, `/dining/`, `/stores/`, `/activities/`, `/play/` share one recipe:

- A display heading — the 40px/60px lh bold line (`mv-h1`, `ev-h1`, `cm-h1`).
- A filter rail — 56x32 white chips (`mv-chip`) with a black@24% border (`--color-border-intense`) and 6px radius for language/format choices; the comedy page adds a sort/filter column (`cm-filter`).
- A card grid — movie cards on /movies/, venue cards on /events/ and /events/comedy (with `₹… onwards` price lines at 16px bold, `ev-price`), store cards on /stores/ with "Flat ₹300 OFF" offer lines.

## The artist and ticket pages

- **Artist page** (`/events/<slug>/artist`): the artist display name (`at-h1` region), then upcoming-show cards (`at-show`, 296x544) holding date, venue and price, each with a booking affordance (`at-book`).
- **Ticket page** (`/events/<slug>-buy-tickets`): the event title and About section (`tk-h1`, 24px semibold), date pills (`tk-date`), the ₹ price line (`tk-price`) and the primary Book CTA (`tk-book`, 163x52, `#131316` fill — `--color-button-primary-background` — 12px radius, `#f7f7f7` label). Booking gates on the Zomato account: measured, never pressed.

## The dark theme

`html[data-theme=dark]` is the product's own theme switch and the package measures it as a forced pass: chrome repaints to `#131316` (`--color-background-primary` dark) with `#f7f7f7` ink (`--color-text-primary` dark) and white@8% hairlines (`--color-border-subtle` dark). Feed rails on / keep their baked gradient fills (`gradient-for-you`-style classes), so dark paint on this surface is partial — the nav, cards and text roles all repaint; the recorded `dk-*` measurements are the real evidence, not a full dark redesign.

## Mobile

At 390x844 the same chrome compresses: a 390x60 bar (`m-bar`) with mark + location, an 84x60 tab (`m-tab`, 8px radius), and 364x272 content cards (`m-card`) in a single column. Category tabs stay link-based.

## States and motion

Controls expose default/hover/focus-visible/pressed on tabs, chips, CTAs and links; the category tab transition is the measured 0.2s `cubic-bezier(0.4, 0, 0.2, 1)`. Disabled, error and loading states do not exist on the signed-out public surface and were not fabricated.
