# Linear styling reference

Captured 23 September 2026. Independent visual study, not an official Linear library.

## What this package contains

A local HTML guide, full-page public-site screenshots, accessibility snapshots of the signed-in desktop app, computed-style evidence, design tokens, editable SVG sheets, individual component SVGs, and public-demo reference icons. Open `style-guide.html` to browse everything. The signed-in app screenshots were captured from a real workspace and have been removed from the package (2026-10-11); the app is documented by its anonymised accessibility snapshots and the colours sampled from it. The reconstructed components use fictional content.

The study separates three systems: the authenticated desktop app, public marketing/product pages, and brand assets. The current app is more neutral and dense than the blue-gray public product examples. Using one palette for all three would lose that distinction.

## Evidence and limits

| Label | Meaning |
| --- | --- |
| Measured CSS | Computed styles read from visible DOM elements on public pages. Exact for the captured page and viewport. |
| Sampled pixels | Dominant flat colors sampled from signed-in app screenshots taken before they were removed. A displayed sRGB pixel, not proof of the underlying CSS token. |
| Observed | A component or state is visible in a saved public screenshot or recorded in an app accessibility snapshot. |
| Reconstruction | A practical redraw or suggested token. Dimensions and interaction behavior may differ from Linear's implementation. |
| Not inspected | Not accessible, not enabled, not reached, or deliberately outside the capture. |

This is broad page-type coverage, not a claim that every Linear route, workspace record, historical article, responsive breakpoint, permission state, or experiment has been captured. Native app captures showed the viewport, not every scroll position. Public screenshots are full-page but video, lazy-loading and scroll-triggered animation can leave inactive regions. See `coverage.json` for exact captured URLs and exclusions. App theme was System preference with Dark selected for the dark system appearance; font size was Default. No theme, workflow, issue, project or account setting was changed.

## Colors

### Authenticated app: sampled dark surfaces

| Role | Value | Evidence |
| --- | --- | --- |
| Outer canvas / navigation | #09090B | Flat pixels across issue list and detail |
| Main content | #121214 | Flat pixels across issue list and detail |
| Raised card / dialog | #1A1A1C | Properties and issue composer |
| Popover surface | #212123 | Status menu |
| Menu selection | #323234 | Status menu |
| Main text | #FFFFFF | Reconstruction value informed by text pixels |
| Secondary text | #969699 | Approximate reconstruction |
| Subtle border | #2B2B2E | Approximate reconstruction |
| Action accent | #5E6AD2 | Measured public accent, reused in reconstructed app controls |

These values describe the captured dark appearance. A complete light-theme token set is not included because the account theme was not changed. The public Switch guide provides a light editorial reference, not a verified light app theme.

### Public website: measured computed CSS

| Role | Hex | Where it appears |
| --- | --- | --- |
| Page background | #08090A | Homepage |
| Low surface | #0F1011 | Product examples / cards |
| Raised surface | #161718 | Product examples |
| Border | #24282C | New-issue control in product demo |
| Main text | #F7F8F8 | Headings and general copy |
| Secondary text | #D0D6E0 | Product-demo navigation / issue title |
| Muted text | #8A8F98 | Navigation and supporting copy |
| Subtle text / icons | #62666D | Demo controls and section labels |
| Light primary button | #E5E5E6 | Sign-up action |
| Accent | #5E6AD2 | Accent control styles |

Also observed: white overlays at 2%, 5%, 7% and 8%; green and red translucent code-diff fills. Use alpha over the correct surface instead of flattening all overlays to one gray. Not every color in raw evidence is a Linear token: customer logos, code syntax, illustrations and third-party integration mockups also contribute colors.

### Official brand colors

Mercury White is #F4F5F8. Nordic Gray is displayed as #222326. The brand page's RGB prose for Nordic Gray says 35, 35, 38, which does not exactly match that hex; this package preserves the displayed hex and records the inconsistency instead of silently correcting it. Brand colors are not substitutes for UI text and surface tokens. Source: https://linear.app/brand.

Status and label colors depend on workflow and configuration. The semantic tokens supplied here are reconstruction choices, not universal Linear assignments. Pair status color with icon shape and a text label.

## Fonts and typography

| Family | Verified use | Evidence |
| --- | --- | --- |
| Inter Variable | Public UI, navigation, product examples, marketing copy and headings; login/signup CSS stack | `01-home-styles.json`, `login-styles.json` |
| Berkeley Mono | Code, technical examples, small numbered annotations | `01-home-styles.json`, `agents-styles.json`, `method-styles.json` |
| Tiempos Headline | Editorial display heading on Linear Method | `method-styles.json`: 128px / 128px, weight 400 |
| Linear Thai | Fallback name present in authentication font stack | Presence in stack only; actual Thai glyph rendering not tested |

The authenticated app visually resembles Inter, but its exact computed text and code font families were not inspected. Preferences explicitly showed code Font: 12px, Regular, Default. Do not treat the public Berkeley Mono declaration as proof of the account's configured code font.

The public Inter stack is `"Inter Variable", "SF Pro Display", -apple-system, system-ui, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif`. The mono stack is `"Berkeley Mono", ui-monospace, "SF Mono", Menlo, monospace`. Tiempos falls back to a system serif/Georgia family.

The public UI uses `font-feature-settings: "cv01", "ss03"` in many elements. Preserve these when matching letterforms. Common measured weights are 400, 510 and 590, rather than assuming all labels are conventional 500/600. Family names are CSS declarations; this inspection did not prove every glyph's final fallback face.

| Role | Size / line-height | Weight | Letter spacing | Source |
| --- | --- | --- | --- | --- |
| Homepage hero | 64 / 64px | 510 | Read individual sample | Homepage H1 |
| Section heading | 48 / 48px | 510 | -1.056px | Changelog heading |
| Large closing statement | 72 / 72px | 510 | -1.584px | Homepage closing heading |
| Product-demo issue title | 20 / 26.6px | 590 | -0.24px | Embedded issue detail |
| Public body | 16 / 24px | 400 | Context dependent | Homepage |
| Navigation | 13 / 19.5px | 400 | normal | Product / Resources |
| Product sidebar | 13px, normal line-height | 510 | Context dependent | Embedded sidebar |
| Section label | 12 / 14px | 510 | Context dependent | Embedded Workspace label |
| Editorial display | 128 / 128px | 400 | normal | Linear Method |

The component redraws use 12–14px UI text and 20–24px detail titles as reconstruction choices. SVG font fallback affects appearance. Install the exact faces before judging fidelity; the package does not include font binaries. Obtain Inter from https://rsms.me/inter/, Berkeley Mono from https://usgraphics.com/products/berkeley-mono, and Tiempos Headline from https://klim.co.nz/fonts/tiempos-headline/. Inter is open-source; obtain appropriate licensing for the commercial faces. Georgia and Menlo are only preview fallbacks.

## Geometry, spacing and layout

| Element | Observed or reconstructed geometry |
| --- | --- |
| Public navigation / sign-up | 32px tall, 12px horizontal padding, pill radius |
| Demo icon buttons | 28 × 28px, circular/pill |
| Demo sidebar rows | 28px tall, 8px radius, 7px horizontal padding |
| Demo workspace label | 24px tall, 12px text, 8px radius |
| Public logo link | 6px radius |
| Cards / panels | 9, 12, 16 and 22px radii occur in public DOM; context matters |
| App tabs | Observed pills; redraw uses 28px height and half-height radius |
| App main pane | Large rounded container inset from outer canvas |
| App properties | Stacked rounded panels with thin borders and close vertical spacing |
| Menus | Rounded surface, search at top, compact rows, selected fill, shortcuts on right |
| Issue rows | One-line, aligned metadata columns, subtle horizontal dividers |

The 4, 8, 12, 16, 24, 32, 48, 64px spacing scale in the tokens is a reconstruction convenience, not an extracted official spacing system. Desktop app screenshots were captured at 3024 × 1898 device pixels on this machine; approximate logical dimensions use a 2× assumption. Browser zoom/device scaling was not independently measured. Public CSS measurements use the actual capture viewport in each JSON file.

Avoid indiscriminate rounded rectangles: pill actions, modestly rounded sidebar items, squared list rows, and more rounded floating surfaces serve different roles. Public marketing pages also use large whitespace, narrow text measures and oversized editorial titles that do not belong in a dense issue table.

## Buttons, fields and interaction states

Public primary actions are pale filled pills with dark text, 32px high and 13px text at weight 510. Public navigation is transparent with muted labels. The embedded demo has subtle icon buttons using 2% white fill and an inset 1px line at 5% white. Read raw border style as well as border color: computed border color alone does not imply a visible border.

The authenticated issue composer shows an accent primary action, compact metadata chips, a quiet close affordance, and a footer separated by a hairline. Tabs use filled pills. Property controls often look like text-and-icon rows until opened.

The library includes default, hover, focus, disabled and destructive button variants; default/focus/error fields; checkbox and switch pairs; and tooltip/toast examples. The hover, focus, validation error, switch, tooltip and toast redraws are proposals for a usable library, not claims that those precise Linear states were captured. Actual menus, the date picker, composer, filters and display settings were observed. Checkboxes are visible in settings. No destructive confirmation or error was deliberately triggered.

## Icons

The reference atlas contains 39 SVG extracts from visible buttons in Linear's public homepage demos, including navigation, search, issue creation, priority-related controls, copy actions, attachments and communication actions. A button can contain more than one SVG; the named extract is the first encountered, so names describe source controls rather than guaranteed canonical icon names. Some examples depict third-party integration UI.

Use the supplied source SVG paths for visual study. Preserve viewBox and aspect ratio; `currentColor` lets monochrome icons inherit foreground color. Many UI icons sit on a 16px design scale within 28px controls, but individual source viewBoxes differ. Do not replace mixed filled/outlined glyphs with a uniform arbitrary stroke. Do not assume Linear uses Lucide, Heroicons or SF Symbols: no upstream icon library was established.

Reference SVGs remain proprietary/reference material and are not offered as a newly licensed icon pack. Brand assets should be taken from https://linear.app/brand and used according to its guidance. The component redraws are separate from extracted icons and do not bundle a Linear wordmark.

## Component inventory and evidence

| Family | Included | Primary screenshot evidence | Status |
| --- | --- | --- | --- |
| Navigation | Selected sidebar row, pills, circular action | App My issues / project overview; public demo | Observed, redrawn |
| Buttons | Primary, secondary, ghost, icon, web CTA | Issue composer; public homepage | Observed bases, proposed extra states |
| Forms | Text fields, checkbox, switch | Preferences; issue composer | Mixed, switches/error state reconstructed |
| Metadata | Labels, avatars, keyboard shortcut | Issue list, menus | Observed, redrawn |
| Lists | Issue row, board card | My issues; public board example | Observed, redrawn |
| Menus | Status selector | App status picker | Observed, redrawn |
| Calendar | Month grid and input | App date picker | Observed, simplified |
| Composition | Issue composer, properties, empty state | App composer / project / views | Observed, redrawn |
| Feedback | Tooltip and success toast | No dedicated live capture | Proposed reconstruction |
| Icons | 39 source SVGs | Public homepage buttons | Extracted reference |

Other documented components include breadcrumbs, search, grouped list headers, project progress graphs, property chips, dense settings tables, empty states, billing/feature upgrade notices, code blocks and diff colors, avatar lists, footer navigation, pricing comparison tables, editorial cards and mobile illustrations. They are visible in the screenshot collection; not every one has a standalone SVG redraw.

## Import into Figma, Paper or another vector editor

Import any `boards/*.svg` file for a full reference sheet, or `components/*.svg` for isolated pieces. In Figma, drag the SVG files onto the canvas. In Paper or another editor, use its SVG import/paste support if available; the exact Paper workflow has not been tested here. The SVGs use ordinary paths, rectangles, text and named groups, with no foreignObject, linked fonts or raster UI embedded.

These are vector assets, not a native `.fig` library. Import does not automatically create component variants, auto-layout, variable bindings or prototype interactions; text editability depends on the importer. Convert the imported groups to components and configure variants in the destination tool if needed. `components/manifest.json` gives intended names and bounds.

`tokens/linear.tokens.json` uses DTCG-style `$type`/`$value` objects, including sRGB color components. `tokens/tokens-studio.json` provides a separate hex-value Tokens Studio structure. Import with a token-aware plugin/tool that supports that format; neither file is claimed to be a native Figma variables import. `tokens/linear.css` supplies CSS custom properties. Preserve evidence descriptions when promoting tokens into a production design system.

The SVG syntax and browser rendering are checked locally. Import into Paper/Figma itself is unverified. Font installation and commercial font licenses are not included.

## Coverage and remaining gaps

Captured public page families: homepage; Brand; Pricing; Intake; Plan; AI; Build; Asks; Agents; Coding Sessions; Customer Requests; Insights; Mobile; Integrations; Changelog; About; Customers; Careers; Now; Method; Quality; Switch; Download; Docs; Developers; Enterprise; Startups; Security; Contact; Privacy; Terms; DPA; AUP; login and signup entry screens.

Captured app families (accessibility snapshots only; no screenshots remain) include agent, inbox, assigned issues, issue detail, selectors, projects, project overview/activity/issues, reviews, saved views, team home/issues/projects/views/documents/members, workspace menu, issue composer, date/filter/display menus, and settings pages listed in the evidence index. Repeated issues and project records were not individually captured because they reuse these page structures.

Not completed: all nested marketing articles/customer stories/docs pages; mobile authenticated UI; light authenticated theme; board/timeline layout after a preference change; enabled cycles/triage (disabled for this team); every settings subpage; security/API/credential pages; destructive dialogs; every interaction state and breakpoint; exact authenticated computed typography, radii and shadows. These remain explicit gaps rather than inferred verification.

## Source files and provenance

Each public `evidence/styles/*-styles.json` contains URL, title, viewport and visible-element computed properties. `evidence/pages/*-page.txt` preserves public page text/structure. The app accessibility snapshots in `screenshots/app/` are the only app evidence kept; early captures contain diffs, later ones contain full trees. Their workspace, team, project, people, issue titles and ids were replaced with neutral values (workspace Acme, teams Core and Research, Teammate A to D, Sample issue N) on 2026-10-11; the screenshots themselves were not changed. `evidence/coverage.json` is the final index, and `evidence/capture-manifest.json` is an earlier collection log that may include first-pass titles. `tools/build_library.py` rebuilds SVG assets and tokens; `tools/build_guide.py` rebuilds the gallery (`style-guide.html`) and validation report. Both need Pillow and Markdown (`pip install pillow markdown`) and run from any directory.

Primary sources: Linear's live pages and signed-in workspace, captured 2026-09-23; https://linear.app/brand; https://rsms.me/inter/; https://usgraphics.com/products/berkeley-mono; https://klim.co.nz/fonts/tiempos-headline/.
