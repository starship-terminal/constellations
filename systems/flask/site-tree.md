# Flask site tree

Mapped on 2026-11-21 from the public homepage at https://flask.do/, signed out, before the screenshot pass. Desktop CSS viewport measured `innerWidth` 1440, `innerHeight` 900, `devicePixelRatio` 2, `visualViewport` 1440 by 900 at scale 1. `color-scheme` on `:root` is `dark`. There is no theme toggle and no cookie banner.

Flask.do is a video-review product (https://flask.do, "Flask - Video Review Workspace for Teams and Agents"). This is not the Python Flask framework. The marketing site is public. The workspace is not. Sign Up and Open Flask both go to `/home`. A signed-out visit to `/home` and to `/login` lands on the same wall: Continue with Google, an email field, Continue with Email. Nothing was typed. Google was not clicked. No form was submitted.

The homepage header has no dropdown. At 1440 it shows Pricing, Features, and Sign Up. Open menu (`aria-haspopup="menu"`) is in the DOM and has zero size until the phone width. The product chrome inside the hero (Copy Link, Context, Feedback, Version, share scope, folder rows) is a painted marketing demo. Those controls are `cursor-default` and do not open a page.

| Control | Page | Destination or state |
|---|---|---|
| Flask wordmark | https://flask.do/ | / |
| Pricing | https://flask.do/ | /pricing |
| Features | https://flask.do/ | /pricing#features |
| Sign Up | https://flask.do/ | /home, which redirects to the /login wall |
| Open menu | https://flask.do/ | phone nav only (`md:hidden`, zero size at 1440). Same two links as the desktop nav: Pricing, Features |
| Open Flask, hero | https://flask.do/ | /home (login wall). Button, no form |
| Copy Prompt, hero | https://flask.do/ | copies a prompt to the clipboard. No navigation, no submit |
| Quote attribution, @sferro21 | https://flask.do/ | https://www.instagram.com/sferro21/ (external, not followed) |
| Demo, Copy Link | https://flask.do/ | painted demo control. No page |
| Demo, v2 Context | https://flask.do/ | painted demo chip. No page |
| Demo, Feedback 0 | https://flask.do/ | painted demo chip. No page |
| Demo, Version 3 | https://flask.do/ | painted demo chip. The capture kit toggles the visible Version chip for `home-dark-demo-asset-2`. No page |
| Product Hunt badge | https://flask.do/ | https://www.producthunt.com/products/flask-6/awards (external, not followed) |
| Demo, Copy Link to Folder | https://flask.do/ | painted demo control. No page |
| Demo, Latest Activity / Last Opened / Creator / Type | https://flask.do/ | painted sort chips. No page |
| Demo, Collapse Group | https://flask.do/ | painted demo control (`aria-expanded` true). No page |
| Demo, Anyone with Link | https://flask.do/ | painted share-scope chip. No page |
| Demo, ACME Studios | https://flask.do/ | painted workspace chip. No page |
| Demo, Close | https://flask.do/ | painted demo control. No page |
| All Features | https://flask.do/ | /pricing#features |
| Book a Chat | https://flask.do/ | https://cal.com/enricotartarotti/flask-20 in a new tab. Booking form, not opened, not submitted |
| Testimonial, Eric Villa | https://flask.do/ | https://www.youtube.com/@mkbhd (external, not followed) |
| Testimonial, Pedro Duarte | https://flask.do/ | https://raycast.com (external, not followed) |
| Testimonial, Simone Ferretti | https://flask.do/ | https://www.instagram.com/sferro21/ (external, not followed) |
| Testimonial, Tommy Geoco | https://flask.do/ | https://www.youtube.com/@designertom (external, not followed) |
| Open Flask, closing band | https://flask.do/ | /home (login wall) |
| Book a Demo, closing band | https://flask.do/ | https://cal.com/enricotartarotti/flask-20 in a new tab. Not opened, not submitted |
| Footer, Pricing | https://flask.do/ | /pricing |
| Footer, MCP | https://flask.do/ | /mcp |
| Footer, Login | https://flask.do/ | /login (login wall) |
| Footer, Video Collaboration | https://flask.do/ | /video-collaboration |
| Footer, Video Feedback for Agents | https://flask.do/ | /ai-video-feedback |
| Footer, Frame.io Alternatives | https://flask.do/ | /frame-io-alternative |
| Footer, Video Review Software | https://flask.do/ | /best-video-review-software |
| Footer, Flask vs. Frame.io | https://flask.do/ | /flask-vs-frame-io |
| Footer, Frame.io vs. Dropbox Replay | https://flask.do/ | /frame-io-vs-dropbox-replay |
| Footer, Video review for AI agents | https://flask.do/ | /video-review-for-ai-agents |
| Footer, Remotion and HyperFrames | https://flask.do/ | /remotion-hyperframes-video-review |
| Footer, Timestamped feedback | https://flask.do/ | /timestamped-video-feedback |
| Footer, AI video feedback | https://flask.do/ | /ai-video-feedback |
| Footer, Best video review software | https://flask.do/ | /best-video-review-software |
| Footer, About | https://flask.do/ | /about |
| Footer, Trust Center | https://flask.do/ | /security |
| Flask Ltd. | https://flask.do/ | / |
| I have a bad feeling about this | https://flask.do/ | https://www.youtube.com/watch?v=c-wT7sijLIs (external, not followed) |
| Privacy | https://flask.do/ | /privacy-policy |
| Terms | https://flask.do/ | /terms-of-service |

Public routes the router also publishes, not linked from the homepage: `/start.md`. Signed-out app routes that stop at the login wall, not entered: `/home`, `/activity`, `/assets`, `/dash`, `/plan`, `/team-settings`, `/members`, `/tags`, `/ai-agents`, `/profile`, `/upgrade`, `/subscription`, `/newteam`. Token and invite routes (`/r/:code`, `/oauth/consent`, `/auth/callback`, `/invite/:inviteCode`, `/files/:versionId/:name`, `/f/:id`, `/a/:id`, `/flask/:id`) need an account or a link this pass does not have.
