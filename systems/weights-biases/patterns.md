# Patterns

No page screenshots. The preview browser did not produce frames. These notes are from the live DOM.

## Marketing home

[wandb.ai/site](https://wandb.ai/site) is a dark page. Body background is `dark.color.bg.page`. The header sits under a 60px gap, 96px tall, with the wordmark at the left and Docs, Pricing, CONTACT, LOG IN, SIGN UP at the right. The h1 is Source Serif 4 at 72px: "AI is easy to productionize". A Weave call to action uses the teal gradient. A code sample sits in a `dark.color.bg.code` panel. Section fills step through several near-black greys listed in [raw/computed.json](raw/computed.json).

`https://wandb.ai/` did not stay on this page. It redirected to `https://id.coreweave.com/login?next=%2Fwandb`.

## Pricing

[wandb.ai/site/pricing-privately-hosted/](https://wandb.ai/site/pricing-privately-hosted/) is the page the Pricing link reaches. The h1 is "Privately-Hosted Pricing" at 54px. Personal shows `$0/mo` and a GET STARTED link to `https://id.coreweave.com/signup`. Advanced Enterprise uses CONTACT US, which points at `/site/contact/`. A line on the page says cloud-hosted pricing has moved to CoreWeave Forge. That link was not followed into a purchase.

## Signed-out login and signup

Login and signup are CoreWeave Forge, light, Source Sans 3. A gold banner says Weights & Biases is now CoreWeave Forge. The form is an email field plus a cobalt primary button, with social buttons above an "or". Signup also offers Google, GitHub, and Microsoft, so the email field was not submitted.

## Phone

At 390 by 844 the marketing CSS viewport matched the request. Header links collapsed to empty boxes. The menu was not opened, so the phone navigation pattern is a gap.

## Not entered

No email was typed. No social login was pressed. No card, phone number, or company SSO was entered. No plan was started. No API key was created. Contact, careers, customers, and the 404 route were not opened.
