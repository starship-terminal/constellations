# Flask patterns

How the measured components combine on each captured surface. Every value cited is in [tokens.json](tokens.json); the components are in [components.md](components.md) and the full-page evidence in [screenshots/](screenshots).

## Marketing chrome (dark)

The top chrome is a `div` (not a `<header>`) with `md:sticky md:top-0 z-50`, 1440 x 56 at the desktop run, painted over `dark.surface.0` `#0c0c0c` (the declared `--ds-surface-0` channel list `12 12 12`). It carries the 64 x 32 Flask mark on the left and, right-aligned, the Pricing (58 x 32) and Features (69 x 32) links plus a Sign Up link (82 x 32) whose href is `/home` — the authenticated workspace entry, measured and never followed. Nav links sit at the control radius `dark.radius.control` 9999px pill family; hover lifts ink along the `--ds-fg-*` ramp and hover/focus/pressed states were all measured.

## Home (dark)

The home page opens on the `dark.surface.0` field with a 1440x56 sticky chrome over a centred hero: "The world's fastest way to review video." (measured hero-h1 1200 x 138), a 128 x 40 primary `Open Flask` pill (`button-primary`, `dark.radius.control` pill) beside a 146 x 40 `Copy Prompt` secondary (`button-secondary` on the glass/control family). Below, the hero embeds a working mock of the Flask workspace itself — version chip (94 x 30), Context/Feedback tabs (the measured `demo-th` strip), Copy Link (104 x 30), share-scope control, folder rows and a close control — all measured as components, the Version chip opened for its `demo-asset-2` state. The folder-row region is a large bounded slice of that mock (1440 x 7560.78 measured), not a single list row.

## Pricing

/pricing keeps the same dark field and chrome: plan cards on `dark.surface.*` steps with `dark.line.*` hairline borders, a "Billed yearly" switch (measured at rest, toggled for the `pricing-dark-billed-monthly` shot then toggled back — it re-prices the cards, so the monthly grid exists only as a screenshot state), and a FAQ accordion whose items open locally (measured `faq-item` in default and open states).

## Documentation

/mcp is the public documentation page — same chrome, long-form prose on `dark.surface.0` with `dark.fg.*` ink steps and `dark.brand.*` accents on links and code accents. /security, /about and the comparison/legal pages reuse the same shell and were captured as full-page tiles.

## The auth boundary

/login paints the same dark system: "Sign in to Flask", a `Continue with Google` button, an `OR` divider and a `Continue with Email` form (measured `login-email-field`, `login-submit` in default/hover/focus/filled states — typed into then cleared, never submitted). Everything past this point (`/home`, the real workspace) is the authenticated boundary, never reached.

## Mobile (390px)

The 390px pass keeps the dark field and stacked marketing sections. Chrome is inconsistent across passes — see the README's distrust list: the measured run mounted only the logo link with no visible header or menu button, a later probe found an `Open menu` button with zero-sized bounds, and another capture rendered a mobile bottom-sheet menu. The package records what each pass painted rather than a universal drawer.

## Motion and focus

Controls transition over the declared `--ease-out`/`--ease-in-out` tokens (harvested in `raw/css-vars.json`). Focus is a ring on the `--ds-focus` role: nav links and CTAs draw it on keyboard focus, measured as `focus-visible` states rather than border swaps.
