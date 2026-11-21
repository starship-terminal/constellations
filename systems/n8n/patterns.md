# Patterns

The 2026-11-19 readings below were taken without screenshot frames. Public pages were photographed on 2026-11-22. See [site-tree.md](site-tree.md). Those shots do not replace the measurements.

## App shell and navigation

[https://n8n.io/](https://n8n.io/) has a fixed header, 94px tall, transparent, with a 0.3s transform transition. An announcement line sits above the wordmark: `Meet Nod, an open-source personal agent from n8n Labs.` plus a pink `Learn more` link. At 1169px the named nav links are not displayed. A 32px hamburger is the visible control. Clicking it did not open a labelled menu.

The signed-out console at [https://app.n8n.cloud/login](https://app.n8n.cloud/login) and [https://app.n8n.cloud/register](https://app.n8n.cloud/register) is a dark page, oklch(0.2046 0 89.88), with a CLOUD wordmark and a narrow form (334px on login, 374px on register). It is not the marketing shell.

## Form with a validation error

Register asks for `Company email` and a `Continue` button. The copy says a free 14-day trial needs no credit card. Empty submit uses the browser's own `Please fill out this field.` Typing `not-an-email` and clicking Continue paints an alert, `Value needs to be an email address`, and a red inset ring. The form was not submitted. A real email was not entered.

Login asks for an instance name and appends `.app.n8n.cloud`. No name was submitted, so no login error was measured.

## Empty, loading and error

No empty state, loading state, or product error page was on the signed-out surfaces. The only error is the register email alert above.

## Destructive confirmation

Not present. No delete or cancel flow was opened.

## Feedback after an action

Declining the CookieScript banner removed it. That banner is a third-party overlay, not an n8n toast. No n8n success message was shown, because no form was submitted.

## Search and filtering

Not present on the homepage, pricing, login, or register pages.

## List or table

Pricing is a row of plan cards, not a table. Starter, Pro and Business each have a price, an execution dropdown, a `START FREE TRIAL` button, a hosting line, and a feature list. Enterprise uses `CONTACT SALES`. No trial or sales form was submitted. Prices read on the annual toggle: Starter 20€, Pro 50€. Business was truncated in the text read.

## Onboarding

Not entered. Register stops at the email field until a real address is submitted. The workflow editor was not opened.
