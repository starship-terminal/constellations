# Craft patterns — page layouts

Captured signed out on 2026-11-12. Heights are the painted `scrollHeight` of each route at 1440 wide; mobile is 390 wide at DPR 2.

## Shell

- **Floating nav pill (920x52, 26px radius).** A white rounded-full bar: CRAFT wordmark (800-weight display cut), then Product / Imagine / Community / Pricing / Learn / Download text links (16px 400 ink), Log in (links out to docs.craft.do) and a black 36px Try Craft Free pill that lifts to 75% ink on hover. On mobile it compresses to wordmark + Try pill + a 24px menu glyph.

## Home (`/`, H=11057)

- **Hero.** 66px/66px 400 Untitled Serif ("Your space for notes, tasks, and big ideas") on a sky-blue torn-paper collage; a white 48px Try Craft Free pill under it; a product screenshot collage closes the fold.
- **Sections.** Long marketing page — feature bands, the imagine/templates gallery links and the footer.

## Pricing (`/pricing`, H=8015; mobile H=10153)

- **Billing toggle.** A muted rounded-full pill holding two 112x40 segments (Yearly / Monthly); the selected segment paints white with a soft shadow.
- **Plan cards.** PLUS at 273x463 (name, serif price, /month, feature list, CTA); TEAM in the 24px-radius `.shadow-block` card (491x578 measured on the grid cell); a students card. Prices render SGD (the served region): the serif figures are 54px.
- **FAQ.** 1000px accordion rows (14px 500) with a 3px 6% ink ring on keyboard focus.

## Download (`/download`, H=2654)

- 54px serif "Get Craft for Free" and platform download buttons (226x48 pills); never used.

## Imagine (`/imagine`, H=8853) · Learn (`/learn`, H=3945) · Write (`/write`, H=6011)

- 54-70px serif headings; /imagine carries template cards (~712x399 — Blog Publisher, Reading Tracker) linking to guided flows; /learn and /write are editorial feature pages.

## Blog (`/blog`, H=8102)

- The blog index in the same shell.

## Footer

- A 24px-radius black panel (1409x563 on home): white 14px link columns, social links and the legal row — the only painted dark surface on the site.

## Mobile (390 wide, DPR 2)

- The pill header holds wordmark + Try pill + 24px menu glyph. The menu opens as a floating overlay: accordion rows (Product expands to Plan/Write/Organize/Customize/What's New/Imagine/Help and Support/Blog with coloured dots), chevron rows for Imagine/Pricing/Learn/Download, a Community accordion, and a black "Download for iOS" pill at the foot. The hero drops to 48px.

## Theme behaviour

Single light theme — no dark var set exists. The black footer and pill fills are painted surfaces, not a mode.
