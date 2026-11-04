# Studio's visual foundation

[tokens.css](tokens.css) owns the app's semantic dark theme, system font stacks,
shape values, and motion timings. It takes the page, subtle, elevated and muted
background roles, radius values, and micro-interaction/video durations from
`systems/refero-design/tokens.json`. Secondary text and border contrast are Studio
adjustments. Dialog and insertion timings are app choices, labelled in the file.

The app uses Georgia and Arial from the system instead of captured proprietary
fonts. Studio's mark is original, and interface icons come from Lucide. Captured
product icons and screenshots identify references inside the private library.

[reference-values.module.css](reference-values.module.css) owns the token inspector
component. Its grid adapts to the containing panel, so the standalone detail view
and the wider modal share the same readable token presentation. Other app styles
currently remain in `src/app/globals.css`; they have not been migrated to modules.

Keep component-specific styles in CSS modules as components change. Use semantic
variables from the token file rather than redefining theme roles in a component.
