# Polaris archive styling guide

This is a local reference library for Shopify's archived Polaris React system. It is not the current Polaris web components system, a native Shopify/Figma library, or a claim to reproduce every Shopify application screen.

## Version and evidence

Repository: https://github.com/Shopify/polaris-react-archive
Pinned commit: `3f7954ae42fabf26d63cee68c23ceebfd7ef0972`.
Captured 2026-09-25. Archive React package declares **13.10.1**. That version was unavailable from the configured npm registry; live specimens use **13.9.5**. Tokens **9.4.2**, icons **9.3.1**. All four published token sets were compared against the pinned archive's evaluated token values with **zero value differences**; see `evidence/token-parity.json`.

The website's navigation, green introduction panel, sample commerce data and specimen containers are editorial presentation, not Shopify product screenshots. Screenshots show the local reference gallery. Actual component rendering is supplied by the published React package. SVG components are deliberately labelled token-based redraws: they preserve editable geometry/text, but do not fully reproduce layered bevels, gradients, pseudo-elements or responsive behavior.

## Open and rebuild

From the repository root, run `make serve` and open Polaris from the catalog. Or, from this directory, run `python3 -m http.server 8768 --bind 127.0.0.1` and open http://127.0.0.1:8768/style-guide.html. The page fetches its data, so opening it straight from disk does not work. `-m` runs Python's HTTP server module; `8768` is the port; `--bind 127.0.0.1` restricts access to this computer.

For changes, from `tools/`: `npm ci --ignore-scripts --no-audit --no-fund`, then `npm run build`. The flags disable package lifecycle scripts, security audit network requests, and funding notices respectively. The committed lockfile pins the dependencies. Existing bundled assets work without installing Node dependencies. `python3 tools/build_vectors.py` regenerates SVG references; it needs Pillow, fontTools and Brotli. The font conversion produces a convenience desktop TTF from the included variable WOFF2 under the same OFL license.

## Color

Use semantic tokens rather than choosing raw RGB values by appearance. Surface tokens are large containers, fill tokens are controls and compact status areas, text/icon tokens pair with their intended backgrounds, and border tokens separate regions.

The light canvas is `color-bg` (`#F1F1F1`), primary surface is `color-bg-surface` (`#FFFFFF`), primary text is `color-text` (`#303030`). The catalog retains original RGBA strings and transparent colors. Critical, warning, caution, info, success and magic have separate families. Badge attention uses caution tokens.

Every color is searchable on the Colors page. `tokens/polaris-themes.raw.json` preserves all values grouped by theme and type; `tokens/polaris-metadata.json` preserves source metadata. `tokens/light.css` provides `--p-*` custom properties. At a 16px root, all displayed rem-to-pixel conversions are arithmetic conversions, not a recommendation to hard-code pixels.

## Typography

The UI sans stack is **Inter**, -apple-system, BlinkMacSystemFont, San Francisco, Segoe UI, Roboto, Helvetica Neue, sans-serif. Code uses **ui-monospace**, SFMono-Regular, SF Mono, Consolas, Liberation Mono, Menlo, monospace. These are two role-based stacks, not a claim that all fallback fonts render simultaneously.

The four weight tokens are regular **450**, medium **550**, semibold **650**, bold **700**. Use variable Inter to preserve intermediate weights. The local preview font comes from Fontsource Variable Inter 5.2.8; the archived documentation sources Inter via inter-ui, so glyph versions can differ. Install the included Inter TTF for editable text imports or substitute your matching Inter version.

Font sizes span 11, 12, 13, 14, 16, 18, 20, 22, 24, 30, 32, 36 and 40px at a 16px root. Font line-height tokens span 12 through 48px. Tracking tokens are -0.54px, -0.3px, -0.2px and 0. Text-role tokens combine size, leading, weight and tracking, and can change with mobile themes. The Typography page lists every font and text token and renders actual Text variants.

## Radius, border and layout

Radius scale: **0, 2, 4, 6, 8, 12, 16, 20, 30px**, plus a full radius token of 9999px. Medium buttons, badges, tags and inputs commonly use 8px. Card uses 12px from the small breakpoint upward; below it, the Card radius is zero. Desktop modal uses 16px. Keep component-specific rules rather than applying one radius everywhere.

Border widths include **0, 0.66, 1, 2, 4px**. Thin controls can use subpixel borders. Focus outlines typically use 2px with a 1px offset. Spacing tokens and width/height tokens are separate namespaces even when their values match. The Geometry page exposes the entire scale, shadows, motion, breakpoints and layering tokens.

Breakpoints: xs 0, sm 490, md 768, lg 1040, xl 1440px. Use these for responsive layout; component rules may use breakpoint-down mixins as well as min-width changes. Narrow-screen input type is larger than desktop type. Do not shrink touch controls to match desktop screenshots.

## Buttons

Secondary is the default variant; primary, tertiary, plain and monochromePlain express other hierarchy. Success and critical are tone overrides. Loading preserves the button label's width while hiding its normal content and announcing progress. Disabled suppresses activation, not merely a color change.

Micro, slim, medium and large have responsive minimum heights. At desktop the primary size minima are 24/28/32px; slim and medium share their authored minimum and padding. Text-only medium examples have 12px inline padding on each side. Icon-bearing buttons intentionally adjust the icon edge independently. Use content sizing, not a fixed width inferred from a specimen frame.

Primary and secondary buttons use compound inset/drop shadows and state-dependent fills. The live gallery and bundled CSS are the fidelity reference for these effects. Editable SVG controls flatten these details to their semantic fill/border. Use Tab on the live controls to inspect keyboard focus. See `evidence/component-findings.md` for exact selectors, tokens, source lines and all state rules.

## Badges, tags and forms

Progress badges represent incomplete, partially complete or complete status. Tags represent removable choices and give their remove control a separate accessible name. Keep text content-sized and account for the remove target at the end.

TextField and Select have distinct default, hover, focus, invalid, read-only and disabled treatments. Labels remain visible; helper text supplies context; errors explain recovery. Text fields use prefix/suffix regions for units without turning them into value text. Native select, checkbox and radio semantics remain intact under custom visual layers. Indeterminate checkbox state is semantically mixed.

## Other components

Cards group related content using surface, padding and bevel. Banners use semantic status families and change presentation inside content containers. Critical/warning banners announce alerts; info/success announce status. Tabs show selected state and preserve tab roles. Popovers have bounded surfaces, action lists and dismissal. Modals use a focus-managed dialog with title and actions. Tooltips explain controls and must not be the sole home of essential instructions. Tables align numeric content separately from labels; empty states explain what belongs there and offer an action.

The live guide includes card, banner, tabs, pagination, popover, modal, tooltip, avatar, data table, progress bar, spinner, range slider and empty-state compositions in addition to core controls. Sample actions do not modify any store.

## Icons

All **534 original SVGs** and their YAML metadata are bundled in `icons/`. The searchable Icons page links directly to downloads. Preserve each source viewBox; most are 20 × 20. Use semantic icon colors and standard Icon components in code. Decorative icons are hidden from assistive technology; icon-only actions need accessible labels.

## Theme coverage

All four sets are retained: `light`, `light-mobile`, `light-high-contrast-experimental`, `dark-experimental`. The live gallery defaults to light; dark/high-contrast token exports are reference material, not validated complete production themes. Tokens alone do not establish accessible contrast across every composite state.

## Do and don't

1. **Do keep the interface neutral and spend color on status.** The canvas, surfaces, secondary buttons, selected tabs and pressed buttons are white and greys; the primary button and checked checkboxes, radios and the slider use the dark brand fill `#303030`. Hue goes to status (badges, banners, the critical and success buttons, the invalid field) and to links. See [05-buttons](screenshots/05-buttons.png), [07-forms](screenshots/07-forms.png), [08-feedback](screenshots/08-feedback.png) and [09-navigation](screenshots/09-navigation.png).
2. **Do give each decision one dark primary button.** The modal pairs a dark "Archive product" with a white, bordered "Cancel", and the empty state has a single dark "Add product". Other actions stay secondary (white with a border), tertiary (text only) or plain (blue link text). See [14-modal-open](screenshots/14-modal-open.png), [11-data](screenshots/11-data.png) and [05-buttons](screenshots/05-buttons.png).
3. **Do keep critical red for destructive actions.** "Delete product" is a filled red button and "Remove" a white button with red text. In the action menu only "Delete" is red; "Duplicate" and "Archive" stay neutral. See [05-buttons](screenshots/05-buttons.png) and [15-popover-open](screenshots/15-popover-open.png).
4. **Do pair every badge tone with words.** Badges communicate status and are not buttons: they are flat tinted chips with no border or shadow, unlike the bordered, bevelled buttons. Each tone carries a label ("Paid", "Overdue", "Unfulfilled"), and progress badges add an empty, partial or filled pip, so color is never the only signal. See [06-badges-tags](screenshots/06-badges-tags.png) and [01-overview](screenshots/01-overview.png).
5. **Don't fake states with opacity.** Hover, active, selected and disabled each have their own tokens. The disabled secondary button drops its border and bevel and turns pale grey with grey text, the disabled primary turns light grey with white text rather than a faded dark button, and pressed "Selected" and the selected "Day" segment take a darker grey fill. The disabled field loses its border and takes a grey fill. See [05-buttons](screenshots/05-buttons.png), [07-forms](screenshots/07-forms.png) and [02-colors](screenshots/02-colors.png).
6. **Do put icons inside full-size buttons.** A leading icon sits left of the label ("Add product", "Open") and the disclosure chevron sits right ("More actions"). The icon-only search button and the pagination arrows keep the same height as the text buttons, with their own border or fill around the icon, so icon size never stands in for the pointer or touch target. See [05-buttons](screenshots/05-buttons.png) and [09-navigation](screenshots/09-navigation.png).

## Import into Figma, Paper or similar

Unzip `polaris-design-library.zip`. Import a board from `boards/` or individual SVGs from `components/`; original icon vectors live in `icons/`. Importers vary in text, clipping and font handling. Install Inter before importing. SVGs contain ordinary paths/rectangles/text, with no HTML foreignObject dependency. They are editable references, not native auto-layout components, variants or linked instances. Native Paper/Figma import was not exercised in this environment.

For Tokens Studio, import `tokens/polaris.tokens-studio.json` as token sets and enable light. Dimension values stay in source rem units. Complex shadows, motion strings and other unsupported values retain the `other` type rather than a misleading conversion. Use raw JSON/CSS for lossless source values. To create a production design library, map semantic tokens to your tool's variables and turn the imported redraws into native components with constraints and variants.

## Licensing

Read `licenses/SHOPIFY-LICENSE.md` and `licenses/ICONS-LICENSE.md`. Shopify's license includes Shopify-interoperability and visual-use restrictions; this is not an unrestricted generic UI kit. Inter is redistributed under the included SIL Open Font License. Original notices are retained. No private Shopify store data or authenticated app screenshots are included.
