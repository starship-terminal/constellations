# Studio's visual foundation

[tokens.css](tokens.css) owns the app's semantic dark theme, system font stacks,
shape values, and motion timings. It takes the page, subtle, elevated and muted
background roles, radius values, and micro-interaction/video durations from
`systems/refero-design/tokens.json`. Secondary text and border contrast are Studio
adjustments. Dialog and insertion timings are app choices, labelled in the file.

The theme choice is System, Dark or Light, stored in `localStorage` under
`studio-theme`. With no stored choice the app is on System: it follows
`prefers-color-scheme`, and an inline script in the layout sets `data-theme`
before first paint. A stored Dark or Light wins over the system setting.

The app uses Georgia and a system sans-serif stack from the system instead of captured proprietary
fonts. Studio's mark is original, and interface icons come from Lucide. Captured
product icons and screenshots identify references inside the private library.

[reference-values.module.css](reference-values.module.css) owns the token inspector
component. Its grid adapts to the containing panel, so the standalone detail view
and the wider modal share the same readable token presentation. Page-specific research, catalog and detail styles use CSS modules. Shared navigation
and base controls remain in `src/app/globals.css`.

Keep component-specific styles in CSS modules as components change. Use semantic
variables from the token file rather than redefining theme roles in a component.

## Visual acceptance

The approved local Refero mockup and signed-in Refero pages are the layout baseline.
Research uses a single-line regular serif title, a 760px composer with a coach panel,
and a tabbed two-column prompt list. Catalog navigation uses a 270px rail (240px on
smaller desktops), 40px controls, a broad search field, category links and generous
screenshot cards. Styles opens separately with an 80px header and equal-width
preview/documentation columns. Preserve these proportions when adding features;
do not introduce editorial eyebrows, oversized bold headings or decorative cards.

The library supplies its own categories, counts and references. Reference-site
marketing claims and unavailable features do not become mock controls in Studio.
Check home, catalog, inspector and Styles in the browser after visual changes,
including scrolling, keyboard dismissal, separate-tab navigation and mobile layout.

The 2026-11-04 interaction audit additionally measured the signed-in research
result grid (1280px viewport: two 399px columns, 36px gap). The app uses an adaptive
minimum 320px column to reproduce laptop and wider desktop layouts. Styles' cycling
headline uses the live measured text sweep colors, documented beside its CSS;
reduced motion freezes both its phrase timer and sweep. These additions are app
adaptations, not edits to the canonical captured package.
