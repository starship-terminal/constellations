# Acne Studios patterns

How the measured components combine on each surface, in the order a page composes them. All values resolve through [tokens.json](tokens.json); component detail is in [components.md](components.md).

## The shell

Every page hangs from the same two rails.

- **Header** — a 60px white rail (`size.header.height`, 45px under `breakpoint.mediumDown`), boxed top and bottom by 1px `#f2f2f2` hairlines drawn as inset shadows. Left: section triggers WOMAN MAN BAGS SCARVES GIFTS as full-height caps labels (`typography.microCaps` on a 60px hit row, hover → `text.muted`). Centre: the wordmark, a plain ~15px "Acne Studios" line, not a logo asset. Right: SEARCH HELP ACCOUNT plus the bag count "00" in muted grey, divided from the left zone by a hairline. Under 991px the left zone collapses to a single Menu button.
- **Footer** — a 572px block under a 1px hairline: NEWSLETTER with its 430x60 grey email rail, contact methods, four link columns of `typography.link` blue lines on 24px leading, the two-letter social links, and the shipping-region selector in caps blue. The place name is painted out of the screenshots.

## The hero

A full-bleed campaign band under the header — black ground, a seasonal photo, the giant white wordmark set over it (~1440x810). A GIFT GUIDE eyebrow sits top-left in white caps; two `navRow` link bars (WOMEN'S GIFT GUIDE / MEN'S GIFT GUIDE) tile the foot, each a 30px row whose tile overlays shift on hover. Below it, more campaign tiles (product and category cells with 1px black inner frames drawn as inset shadows) flow in the page grid.

## The category page (PLP)

- Under the header, a 30px subnav: NEW ARRIVALS / GIFTS FOR HER / WINTER DRESSING in `text.secondary` grey caps, hover underlines.
- The toolbar row holds the caps title ("WOMEN'S NEW ARRIVALS" + item count) and the FILTER button — a header-style label.
- The grid is 4-span product tiles (360 wide cells at 1440): a full-bleed photo, the caps name and the price in Helvetica Now Text (note: PLP prices are *not* monospaced — that face is reserved for the PDP). Hover swaps the photo.
- A centred black `action.primary` LOAD MORE bar (320x60) under the grid; appended rows flow in place.
- **Filter rail**: FILTER opens a 360x901 right drawer on opaque white — a 45px head (FILTER & SORTING + X CLOSE in deep blue), then bordered 44px radio rows for SORT BY and TYPE OF PRODUCT, each with a 10px `border-radius:100%` dot (the site's only curve), the picked row's dot filling black. A black SHOW N ITEMS bar (165x44) applies at the foot.

## The product page (PDP)

- Sticky breadcrumbs (31px, hairline bottom) over a two-column canvas: gallery left, purchase column right (~460 wide).
- Purchase column: caps title (12/20), the colourway in `text.muted`, the monospace `S$4,500`, then the Fit Predictor line ("Item runs True to size") and the SIZE GUIDE link in blue.
- **Size grid**: 77x45 cells of `typography.price` numerals on `border.subtle` hairlines. Hover turns the numeral blue; the picked cell fills `action.selected` (#e8f0fe), keys its border and text `color.blue.default`, and draws a 1px white inset keyline — a two-ring effect.
- **ADD TO BAG** — a 400x60 `action.accent` blue bar beside a 60x60 white wishlist square keyed `color.blue.default` with a heart. Hover the bag bar with no size picked and the site's own handler retitles it to PLEASE SELECT SIZE; pressed it deepens to `action.accentHover`.
- **Info rows**: FREE DELIVERY & EASY RETURNS / COMPLIMENTARY GIFTWRAPPING / PICK UP IN STORE — 460x50 rows boxed in hairlines with a blue caps label and a chevron; they expand an accordion (`motion.duration.slider`, 200ms on the slider easing).
- The spec list sits under them in sentence case with en-dash bullets at a 20px indent, behind a blue caps + SHOW MORE expander.

## The drawers

One pattern for every right-side overlay (search, filter, bag): a `size.drawer.width` 360 column on `background.overlay`, a 45px head keyed by a 1px black border, caps title left and a deep-blue CLOSE right. The search drawer adds its `search-field` variant — a 30px grey rail keyed black — SUGGESTIONS in blue caps on alternating `background.inset` rows, and SUGGESTED PRODUCTS thumbnails. Scroll edges fade under white 45px gradients.

## The mega-menu

Pressing a section trigger drops a 391px panel under the header, framed top and bottom by a 1px black keyline. Columns of `navRow` links in blue (`text.link`) on rows that alternate white / `background.inset` #f7f7f7 — the same striping the mobile Menu drawer uses.

## The sign-in gate

A centred ~520px column: "Sign in or register" in `typography.title` (18/20, the rare larger line), a change-location link in blue, a member-benefit list (en-dash bullets at `space.indent`), the grey 60px EMAIL rail (`typography.field`), the black CONTINUE bar and the white-bordered GOOGLE row. Both bars are 60px. Never submitted. The place name is painted out.

## Mobile (390)

The shell compresses: header to 45px with Menu + wordmark + bag only; the Menu button opens a flat drawer of 45px rows (CONTACT US, HELP, CLIENT SERVICES, COMPANY, the social links), each separated by a 1px `#f2f2f2` hairline painted as a background gradient. The grid drops to single/double columns; product tiles and the hero reflow; drawers keep their 360 pattern against the narrower frame.

## Motion and focus, globally

- State changes are instant (`motion.duration.instant`): no easing on any hover, focus or pressed flip. The only motion on chrome is the drawers' 150ms safe-area pad, the accordions' 200ms max-height reveal and a 500ms campaign fade.
- Focus draws a 1px keyline 3px inside controls (`focusRing`) — white on dark fills, deep blue or black on light ones. Text links get no ring: focus is a colour shift only.
