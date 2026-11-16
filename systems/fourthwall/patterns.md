# Fourthwall patterns

How the measured components combine into the real pages. Values are the measured ones in [components.md](components.md) and [raw/measurements.md](raw/measurements.md); tokens in [tokens.json](tokens.json). The screenshots under [screenshots/](screenshots) show each pattern in place. Fourthwall is five surfaces, not one: the Webflow marketing site, the styled-components product catalogue, the Keycloak auth shell, the Mintlify docs and the Docusaurus help center — each carries its own variable vocabulary, kept as separate token sets.

## Site chrome

Every marketing page carries a fixed `.nav-bar` (71px, `z-index` top, white over a hairline): the Fourthwall wordmark, the Features trigger that opens the `.mega-clip` mega-menu (a 1440×431 panel of `.mega-link` columns plus four 316×326 `.mega-card` tiles for Get inspired / Designers / Help / Blog — the tiles start `visibility:hidden` behind a Webflow reveal; earlier headless passes read mid-reveal, the settle wait in the capture tooling now lets it fire and the measured values are the painted ones), Product catalog / Pricing links, Log in and the `a.btn-primary` "Start now" pill (116×43, 12px radius, `#0a0a0a` ink on white — the pill inverts on the `.is-warm`/on-ink bars). At 390 wide the chrome is wordmark + `nav-burger` (44×44) only; the mobile Start-now variant sits in the DOM but paints nothing (`visibility:hidden`), so there is no mobile CTA at rest.

## The hero and the section grammar

The home masthead is a left-aligned `h1` at 1008px ("One platform for premium products and branded shops.", with the greyed "Easy to start. Ready to grow." second line) over a `.hero-cta-row` holding one `a.btn-primary` (132×55) — a single action, no secondary. Below it the page alternates white sections and `.on-ink` dark bands: `.ws--trusted` logo wall, `.design-preview` storefront carousel, `.leg-section.gs1000` feature band, `.made-with` showcase wall, `.wordmark-section`, then `.closer-section` — a 1440×513 dark closer whose entire headline is the action: `a.closer-link` "Make something worth buying" at 413×135 that grows ~4% on hover. Product tiles (`.ph-tile`, 337×428) carry a `.ph-tile-rating` chip. The footer is `.site-footer.is-warm` on the ink surface.

## Pricing

`/pricing` pairs a `h1` with the `.billing-toggle` (290×48 — "Pay yearly / Pay monthly"; clicking monthly repaints the plan prices locally), `.plan-card` columns at 1120×614, feature rows at 800×69 and `.ph-faq-summary` disclosures (800×69, `aria-expanded` flips on click). Buttons stay the shared 12px-radius pill grammar.

## The product catalogue

`products.fourthwall.com` is a different stack — styled-components over the Fourthwall DS (`--bg-*`, `--text-*`, `--border-*`, `--input-*`, `--radius-*`, `--motion-*`), every colour a declared `light-dark()` pair with no user toggle. The nav (551×50 measured) holds category tabs (Discover / All Products / Apparel / Accessories / Home & Living, 28px tall), a search field that expands 218→638px on focus, and Log in (75×40, `#f2f2f2`) / Sign up (87×40, `#161712` ink fill) buttons — hydration swaps the nav copy about a minute after load, so their focus/pressed states were left uncaptured. Below: the "What are you looking for?" quiz card (1344×907) with 639×137 answer options, product cards (243×323) with "Best seller"/"Staff pick" badges (77×22), and no footer. The PDP (Comfort Colors 1717 DTG) shows the title, the same badge, a row of classless 28×28 colour swatches, a static "S–4XL" range label beside a "Size guide" text button that mounts a full-screen `[role=dialog]` size table (1440×804, 32px radius), "From $15.45", and the 400×48 "Sign in to design" CTA — which starts an auth flow and was never pressed. This PDP exposes no per-size selector, decoration picker or accordion; sizes are chosen inside the designer.

## The signed-out auth shell

`/get-started` 302s to `auth.fourthwall.com` — a Keycloak page on the catalogue DS: a 440px column of provider rows ("Sign up with Google / Apple / email", 440×48, 8px radius, `#f2f2f2` fill) plus a small Log-in link. It was measured at rest; no provider was ever pressed and nothing was typed into a field.

## Docs

`docs.fourthwall.com` is Mintlify: a 112px navbar with a fake-input search trigger (`button[aria-label="Open search"]`, 437×36) that mounts a cmdk dialog (640×62 input row), a "Change theme preference" menu that genuinely sets `html.dark`, a 288px sidebar, a 689px article column (Inter text, Paper Mono code blocks) and `.card` tiles (336×134 in dark). Dark values come from the real menu choice, not a reconstruction.

## Help center

`help.fourthwall.com` is Docusaurus with `--ifm-*` variables plus `--fw-*`/`--eli-*`/`--ask-ai-*` brand vars: a 56px navbar holding an 852×48 local-search field (typing opens an 852×652 `.dropdownMenu_*` results list), a colour-mode toggle that cycles system → light → dark painting `data-theme="dark"`, category link rows and prose articles. `#161712` serves as both ink and "primary" brand colour — the help site shares the catalogue's ink.

## Mobile

The 390px passes show the marketing site reflowing rather than redesigning: the 71px nav becomes 64px wordmark+burger, the hero h1 drops to 350px wide, grids collapse to single columns. The catalogue and help mobile shots keep their own chrome.

## Motion and focus

Marketing animation is heavy — 966 moving elements on the home page (marquee bands, tile hovers, the growing closer link); the motion probe found the marketing and catalogue pages only *partially* honour reduced-motion, while docs/help honour it more (`raw/motion.json`). Focus paints as real rings on the marketing pills and the catalogue/auth buttons; several measured components show no change on focus (see the Shared values table in components.md).
