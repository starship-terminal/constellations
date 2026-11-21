# Conductor public site tree

Mapped 2026-11-22 from [https://www.conductor.build/](https://www.conductor.build/). The host redirects `conductor.build` to `www.conductor.build`. The page title is "Conductor - Run a team of coding agents in the cloud". Desktop shots are 1440×900 CSS pixels. Phone shots are 390×844 CSS pixels. Device pixel ratio was 2 on the dark desktop and phone captures. The light homepage and docs shots were taken at device pixel ratio 1, so those PNGs are 1440×900.

`html` carried `class="dark"` when `prefers-color-scheme` was dark, and `class="light"` when it was light. The homepage hero copy changes with width and theme: "in the cloud." at 1440 dark, "on your Mac." at 1440 light, "from your iPhone." at 390.

A control that opens a login, signup, or identity-provider wall stops that branch. Nothing was typed. No form was submitted. No identity provider was clicked. No download was started.

## Header

Present on the homepage. At 1440 the bar holds the mark, Changelog, Docs, Sign in, and Download. At 390 those links collapse into an Open menu button. Open menu expands the header. It is not a drawer and not a dialog.

| Control | Kind | Opens | Shot |
|---|---|---|---|
| Mark | Link, "Conductor home" | https://www.conductor.build/ | [desktop](screenshots/home-dark-desktop.png) |
| Conductor is joining Meta | Banner link | https://www.conductor.build/announcement | [desktop](screenshots/announcement-dark-desktop.png) |
| Changelog | Link | https://www.conductor.build/changelog | [desktop](screenshots/changelog-dark-desktop.png) |
| Docs | Link | https://www.conductor.build/docs | [desktop](screenshots/docs-dark-desktop.png) |
| Sign in | Link | https://app.conductor.build/ which redirects to the login wall. Stopped. | [desktop](screenshots/login-wall-dark-desktop.png), [phone](screenshots/login-wall-dark-phone.png) |
| Download | Button | Dialog "Download Conductor". The file links were not followed. | [desktop](screenshots/site-tree/desktop-download-dialog.png) |
| Open menu | Button, 390 only | Expands the header into navigation "Mobile". | [phone](screenshots/site-tree/phone-menu.png) |

## Mobile menu

Opened from Open menu at 390. The header grows and lists the same four controls. Close menu collapses it.

| Label | Kind | Opens |
|---|---|---|
| Changelog | Link | https://www.conductor.build/changelog |
| Docs | Link | https://www.conductor.build/docs |
| Sign in | Link | Login wall. Stopped. |
| Download | Button | Same download dialog as the desktop button. Not followed into a file. |
| Close menu | Button | Collapses the header. |

## Download dialog

Opened from the header Download button, from Download in the mobile menu, from the macOS button in "Conduct from anywhere.", and from Download now in the closing band. The dialog title is "Download Conductor". The body says "Choose the build for your Mac."

| Label | Kind | Opens |
|---|---|---|
| Download for Mac, Apple silicon | Button | A file download. Not clicked. |
| Join Windows/Linux waitlist | Link | A Google Form. Not followed. |
| Download for Intel-based Macs | Link | A CDN dmg URL. Not followed. |
| Close | Button | Closes the dialog. |

## Homepage sections

| Control | Kind | Opens |
|---|---|---|
| Get Conductor | Link | https://app.conductor.build/users/sign_up wall. Stopped. | [desktop](screenshots/signup-wall-dark-desktop.png) |
| Learn more about Cloud | Link | https://www.conductor.build/docs/cloud/faq | [desktop](screenshots/docs-cloud-dark-desktop.png) |
| macOS | Button | The download dialog. |
| iOS | Link | Apple App Store listing for Conductor. Not photographed. |
| API | Link | https://www.conductor.build/docs/api | [desktop](screenshots/docs-api-dark-desktop.png) |
| Changelog (section heading) | Link | https://www.conductor.build/changelog |
| View all | Link | https://www.conductor.build/changelog |
| 0.98.0 See where your usage goes | Link | https://www.conductor.build/changelog/0.98.0-see-where-your-usage-goes | [desktop](screenshots/changelog-entry-dark-desktop.png) |

## Footer

| Group | Label | Opens |
|---|---|---|
| Company | Blog | https://www.conductor.build/blog | [desktop](screenshots/blog-dark-desktop.png) |
| Resources | Docs | https://www.conductor.build/docs |
| Resources | Changelog | https://www.conductor.build/changelog |
| Resources | Brand kit | https://www.conductor.build/brandkit | [desktop](screenshots/brandkit-dark-desktop.png) |
| Legal | Privacy | https://www.conductor.build/privacy | [desktop](screenshots/privacy-dark-desktop.png) |
| Legal | Terms | https://www.conductor.build/terms | [desktop](screenshots/terms-dark-desktop.png) |
| Connect | X, YouTube, Reddit, Discord | Off-site. Not photographed. |
| SOC 2 Type II | Link | https://trust.conductor.build/. Not photographed. |

## Where the capture stopped

Sign in and Get Conductor land on identity-provider walls at `app.conductor.build`. The walls offer Continue with Google, Continue with GitHub, Continue with ChatGPT, and Other sign-in options. None of those was clicked. No email, password, code, or phone was typed. No form was submitted. The signed-in app was not entered. `login-extracted` stays not-started.

There is no public pricing page. Download is a dialog, not a page.
