# Patterns

How the captured pages are built. Screenshots are 256-colour. Values are in [tokens.json](tokens.json).

## Marketing shell

Every public page on mwm.ai shares one header: logo, Products, Resources, Pricing, Open MWM Console, Build your app. The page background is `#0c0c0c`. Type is white. The two header actions are a translucent secondary button and a white primary button, both 32 px and 8 px radius.

At 390 px the same links move into a drawer opened by "Open navigation".

| State | Shot |
|---|---|
| Desktop home | [screenshots/home-dark-default.png](screenshots/home-dark-default.png) |
| Products menu | [screenshots/home-dark-products-menu.png](screenshots/home-dark-products-menu.png) |
| Resources menu | [screenshots/home-dark-resources-menu.png](screenshots/home-dark-resources-menu.png) |
| Language menu | [screenshots/home-dark-language-menu.png](screenshots/home-dark-language-menu.png) |
| Phone drawer | [screenshots/mobile-home-dark-nav-open.png](screenshots/mobile-home-dark-nav-open.png) |

The footer repeats Products, Resources, About, and Our apps as disclosure summaries. Our apps and Careers leave the site. Those destinations were not captured.

## Home composer

The home page is a display heading, one lede sentence, and a prompt panel. The heading is 72 px Inter at weight 600. The panel holds a textarea, an attachment control, Agent, platform, model, voice, and a disabled send control. Menus open in place. Sending a prompt, attaching a file, or using the microphone was not done.

Full page: [screenshots/home-dark-full.png](screenshots/home-dark-full.png).

## Product page

MWM AI, Console, Publishing, Intelligence, and Studio are long marketing pages under the same header. They use the same display scale, white type, and in-page FAQ buttons. Plan and console calls to action leave for a login wall. The wall URL is recorded in [site-tree.md](site-tree.md). The wall itself is not in the screenshots.

| Page | Shot |
|---|---|
| MWM AI | [screenshots/mwm-ai-dark-default.png](screenshots/mwm-ai-dark-default.png) |
| Agent details | [screenshots/mwm-ai-dark-agent-details.png](screenshots/mwm-ai-dark-agent-details.png) |
| Pricing | [screenshots/pricing-dark-default.png](screenshots/pricing-dark-default.png) |
| Pricing FAQ | [screenshots/pricing-dark-faq-open.png](screenshots/pricing-dark-faq-open.png) |
| Studio apps | [screenshots/studio-apps-dark-default.png](screenshots/studio-apps-dark-default.png) |
| One studio app | [screenshots/studio-app-dark-default.png](screenshots/studio-app-dark-default.png) |

## Directory

Apps, tags, rankings, articles, glossary, and guides share an index-plus-detail template. Each index was captured, plus one example row. The other rows are the same template.

| Index | Example |
|---|---|
| [screenshots/apps-dark-default.png](screenshots/apps-dark-default.png) | [screenshots/app-profile-dark-default.png](screenshots/app-profile-dark-default.png) |
| [screenshots/articles-dark-default.png](screenshots/articles-dark-default.png) | [screenshots/article-dark-default.png](screenshots/article-dark-default.png) |
| [screenshots/glossary-dark-default.png](screenshots/glossary-dark-default.png) | [screenshots/glossary-term-dark-default.png](screenshots/glossary-term-dark-default.png) |
| [screenshots/guides-dark-default.png](screenshots/guides-dark-default.png) | [screenshots/guide-dark-default.png](screenshots/guide-dark-default.png) |
| [screenshots/rankings-dark-default.png](screenshots/rankings-dark-default.png) | [screenshots/ranking-chart-dark-default.png](screenshots/ranking-chart-dark-default.png) |
| [screenshots/tags-dark-default.png](screenshots/tags-dark-default.png) | [screenshots/tag-dark-default.png](screenshots/tag-dark-default.png) |

Filters stay on the page: glossary categories, duo Optimized, reports Europe. Search fields were focused and not submitted.

## Legal and missing page

Privacy, terms, SDK privacy, and SDK terms are long text under the same header. Their contact details are not copied into this package. The IP dispute form is shown empty, and with the first field focused and empty. It was not submitted.

`/sign-up` is a 404, linked from the ASO tool. Shot: [screenshots/sign-up-404-dark-default.png](screenshots/sign-up-404-dark-default.png).

## Stopped

Open MWM Console and Build your app, and the pricing "Get MWM AI Pro" links, open login walls. Those branches stop at the URL. Google, Apple, and GitHub were not clicked. No password, code, or profile field was filled.
