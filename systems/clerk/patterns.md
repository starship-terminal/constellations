# Clerk patterns

Observed on 2026-10-30 in a Hobby development instance. These are descriptions of captured layouts, not an official behavior specification.

Dark evidence covers the main dashboard and settings. The owner approved a
temporary switch to light for five states at 884 CSS pixels: email and
password settings, the password requirements dialog, Users and workspace
settings. The original dark theme was restored and verified afterward.

| Pattern | Composition | Evidence |
|---|---|---|
| Workspace navigation | Workspace selector above Applications, Team and Settings tabs | [Applications](screenshots/apps-dark-desktop.png) |
| Application shell | Workspace/application/environment selectors, top-level tabs, then configuration sidebar | [Authentication settings](screenshots/authentication-email-dark-1440.png) |
| Settings form | Section heading, explanation, aligned toggle or radio options, dependent choices | [Access mode](screenshots/access-mode-dark-desktop.png) |
| Data table | Search/columns/filter toolbar, quiet headers, avatar/title/secondary text in rows | [Users](screenshots/users-dark-desktop.png) |
| Empty table | Headers remain visible, centered explanation and next action | [Features](screenshots/features-dark-desktop.png) |
| Feature onboarding | Bounded introduction with explanation and activation action | [Organizations](screenshots/organizations-onboarding-dark-desktop.png) |
| Configuration dialog | Heading, helper text, inputs/options and footer actions | [Password requirements](screenshots/password-requirements-dialog-dark-desktop.png) |
| Light settings and dialog | The same grouped settings and footer-action arrangement, with light surfaces | [Email](screenshots/authentication-email-light-desktop.png), [password](screenshots/authentication-password-light-desktop.png), [dialog](screenshots/password-requirements-dialog-light-desktop.png) |
| Light table and workspace settings | Table toolbar and rows; grouped workspace form fields | [Users](screenshots/users-light-desktop.png), [workspace settings](screenshots/workspace-settings-light-desktop.png) |
| Destructive confirmation | Consequence text and a distinct primary destructive action beside Cancel | [Disable native applications](screenshots/disable-native-confirmation-dark-desktop.png) |
| Search/filter menu | Input and selectable suggestions attached to a toolbar control | [Log filter](screenshots/logs-event-filter-dark-desktop.png) |
| Public product landing | Centered display heading, feature sections, animated demos and a light page field | [Home](screenshots/public-home-desktop.png) |
| Public pricing | Dark field, four plan cards, purple primary on Hobby | [Pricing](screenshots/public-pricing-desktop.png) |
| Public docs | White field, left rail, empty search dialog | [Docs](screenshots/public-docs-desktop.png), [search](screenshots/public-docs-search-desktop.png) |
| Empty auth wall | Centered card, provider buttons, empty email, purple Continue. Not submitted | [Sign in](screenshots/login-wall-desktop.png), [Sign up](screenshots/signup-wall-desktop.png) |

## Gaps

Submission validation, successful-save feedback, server errors, reliable loading-state pairs, exhaustive mobile layouts, light mobile, matching light interaction states and destructive-action results were not captured. No activation, invitation, create-user request, deletion or application-setting change was submitted. The approved appearance switch was restored to dark.
