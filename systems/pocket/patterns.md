# Patterns

The only public surface left is the shutdown notice. Signed-in Pocket, the save flow, and the list are gone.

## Shutdown notice

[https://getpocket.com/](https://getpocket.com/) redirects to `/home` and renders one long page in `html.colormode-light`. A fixed white header, 64px inside a 65px bar, holds the wordmark and nothing else. The hero is a two-column grid at desktop (80px column gap, 48px vertical padding, 40px page padding, max width 1128px) and a single column at 390px. The headline is Doyle 38px bold. Sections below use the same grid, with 112px padding above each one. The page ends with a full-width secondary button, then a footer with a 1px `#d9d9d9` top border, a Mozilla line, three underlined links, and a language select.

![Shutdown page, 1440 CSS pixels, first fold](screenshots/home-light-fold.png)

![Shutdown page, full, 1440](screenshots/home-light-default.png)

![Shutdown page, full, 390](screenshots/home-light-phone.png)

There is no cookie banner, no sign-in form, and no colour-mode control. `prefers-color-scheme: dark` was true in the preview browser and the page stayed light, because the dark values sit on `.colormode-dark` and `.colormode-system`, and the root class was `colormode-light`.

## Error page

`/privacy` and `/tos` both return the same error. The title is Graphik Web 40px bold. The body is 20px `#666`. One primary button links to `https://help.getpocket.com/`. That support site was not opened. No screenshot of the error page is in `screenshots/`; the button crops in [components.md](components.md) are from it.

## Not present

| Pattern | Status |
|---|---|
| App shell and navigation | The header is a wordmark only. The old app nav is not rendered. |
| Form with a validation error | No form. |
| Empty, loading | Not shown. |
| Destructive confirmation | Not shown. |
| Feedback after an action | Not shown. |
| Search and filtering | Not shown. |
| List or table | Not shown. |
| Onboarding | Not shown. |
| Dark theme, painted | Declared, not painted. |
