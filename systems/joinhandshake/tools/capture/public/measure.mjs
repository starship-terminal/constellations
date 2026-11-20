// Measures joinhandshake.com's components on its public pages, in every state
// that can be reached without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [group ...]
//
// Groups: chrome home employers pricing forms students blog careers legal
// access mobile. Writes raw/components-computed.json (merged, so a subset of
// groups can be re-run) and one crop per component and state into
// components/crops/. raw/measurements.md is then built from the JSON by
// build-measurements.mjs.
//
// States:
//   hover          real mouse hover, 600ms settle for transitions
//   focus-visible  keyboard: focus, Shift+Tab, Tab, so the browser sees a keyboard focus
//   pressed        CDP CSS.forcePseudoState [active, hover]; no mouse button is pressed,
//                  so no link can fire and no form can submit
//   opened         a resting state reached by the component's own toggle: the
//                  nav's hover-opened mega menu, a FAQ or department accordion,
//                  the segment switcher, the phone's "Open menu" sheet
//   focused        a text field clicked into — nothing is typed
// Nothing is typed, sent, bought or signed into. The hero job-search form and
// the Marketo demo/contact forms are measured at rest only — never submitted.
// The site paints light only: there is no theme control.
import fs from 'node:fs';
import path from 'node:path';
import { chromium, BASE, APP_URL, M, open, closePromo, paintedTheme, styleOf, crop, centre, domFind, patch, UA, UA_MOBILE, RAW } from './lib.mjs';
import { safeUrl } from '../safe-url.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

const URLS = {
  home: '/',
  employers: '/employers/',
  pricing: '/employers/pricing/',
  'request-more-info': '/employers/request-more-info/',
  'cc-contact': '/career-centers/contact/',
  students: '/students/',
  blog: '/blog/',
  careers: '/careers/',
  legal: '/legal/tos/',
  access: APP_URL,
};

let page, cdp, context, current;

// ---------- state drivers ----------

async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  const vw = page.viewportSize()?.width ?? 1440;
  await page.mouse.move(vw - 2, 2);
  await page.waitForTimeout(300);
}

async function hover(loc) {
  await centre(loc);
  const b = await loc.boundingBox();
  if (b) { await page.mouse.move(b.x + b.width / 2, b.y + b.height / 2); await page.waitForTimeout(600); }
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  await page.waitForTimeout(400);
}

// CSS.forcePseudoState through CDP: the press never happens, so no link can
// navigate, no button can fire and no form can submit.
async function pressOn(loc) {
  // Force :active:hover on the component element itself, never the topmost
  // node at its centre (a text span or an svg), so the component's own
  // :active rule applies (2026-11 audit, finding 12-6; not run since).
  await cdp.send('DOM.getDocument').catch(() => {});
  await loc.evaluate((el) => el.setAttribute('data-press-target', '1'));
  try {
    const { result } = await cdp.send('Runtime.evaluate', { expression: `document.querySelector('[data-press-target]')`, returnByValue: false });
    // an unresolved target throws, so the state records an error instead of
    // a resting reading labelled pressed
    if (!result || !result.objectId) throw new Error('press target not resolvable');
    const { nodeId } = await cdp.send('DOM.requestNode', { objectId: result.objectId });
    if (!nodeId) throw new Error('press target has no DOM node');
    await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: ['active', 'hover'] });
    await page.waitForTimeout(400);
    return nodeId;
  } finally {
    await loc.evaluate((el) => el.removeAttribute('data-press-target')).catch(() => {});
  }
}
const pressOff = (id) => id == null ? null : cdp.send('CSS.forcePseudoState', { nodeId: id, forcedPseudoClasses: [] }).catch(() => {});

// ---------- the component specs ----------
// find: page -> Locator. states: name -> 'hover' | 'focus-visible' |
// 'pressed' | 'opened:label' | (loc, page) => Promise<void>.
const via = { 'hover': 'mouse hover over the element', 'focus-visible': 'keyboard focus (Shift+Tab, Tab)', 'pressed': 'CDP CSS.forcePseudoState(:active:hover) — no real press' };

// The fixed nav rides over every marketing page. The "Employers" item opens
// the mega menu on hover; the right rail carries "Sign up" and "Log in".
const CHROME = [
  { key: 'hs-nav', group: 'Site chrome', title: 'Fixed nav bar',
    desc: 'The pill-shaped bar fixed under --desktop-nav-top-offset over every marketing page: wordmark, section items, "Sign up" and "Log in".',
    sel: 'nav.fixed', find: (p) => p.locator('nav').first(), states: ['default'] },
  { key: 'hs-nav-link', group: 'Site chrome', title: 'Nav section item',
    desc: 'A top-level nav item ("Employers") — opens the mega menu on hover.',
    sel: 'nav a (text Employers)', find: async (p) => await domFind(p, /^Employers$/, { sel: 'nav a, nav button', tag: 'nl', minW: 40, minH: 16 }), states: ['default', 'hover', 'focus-visible'] },
  { key: 'hs-signup-button', group: 'Site chrome', title: '"Sign up" button',
    desc: 'The solid sign-up control in the nav\'s right rail.',
    sel: 'nav a,nav button (text Sign up)', find: async (p) => await domFind(p, /^sign up$/i, { sel: 'nav a, nav button', tag: 'su', minW: 40, minH: 16 }), states: ['default', 'hover', 'focus-visible', 'pressed'] },
  { key: 'hs-login-link', group: 'Site chrome', title: '"Log in" link',
    desc: 'The outlined log-in control in the nav\'s right rail.',
    sel: 'nav a (text Log in)', find: async (p) => await domFind(p, /^log in$/i, { sel: 'nav a, nav button', tag: 'li', minW: 30, minH: 16 }), states: ['default', 'hover', 'focus-visible'] },
  { key: 'hs-nav-menu', group: 'Site chrome', title: 'Nav mega menu (open)',
    desc: 'The hover-opened panel under a nav section item. "opened" is the item\'s own hover: the pointer rests on it until aria-expanded flips.',
    sel: 'div.absolute.top-full.rounded-2xl', find: async (p) => {
      // The panel only exists in the DOM once the item is hovered: open it
      // here, before the runner's own visibility check. The nav item itself
      // also carries data-state=open, so match the panel's own classes only.
      const item = p.locator('nav').first().locator('a,button').filter({ hasText: /^Employers$/ }).first();
      const b = await item.boundingBox();
      if (b) { await p.mouse.move(b.x + b.width / 2, b.y + b.height / 2); await p.waitForTimeout(1400); }
      return p.locator('div.absolute.top-full.rounded-2xl:visible').first();
    }, states: [
      { name: 'opened', via: 'the nav item\'s own hover — the panel is measured in the nav region it overlays',
        fn: async (loc) => {
          const item = page.locator('nav').first().locator('a,button').filter({ hasText: /^Employers$/ }).first();
          const b = await item.boundingBox();
          if (b) { await page.mouse.move(b.x + b.width / 2, b.y + b.height / 2); await page.waitForTimeout(1400); }
        } }] },
  { key: 'hs-footer', group: 'Site chrome', title: 'Footer',
    desc: 'The rounded-top footer (rounded-t-3xl) with link columns.',
    sel: 'footer', find: (p) => p.locator('footer').first(), states: ['default'] },
  { key: 'hs-footer-link', group: 'Site chrome', title: 'Footer link',
    desc: 'A single link inside the footer columns.',
    sel: 'footer a', find: (p) => p.locator('footer a:visible').first(), states: ['default', 'hover', 'focus-visible'] },
];

// The homepage hero: the job-search form (measured, never submitted) and its
// type pills, plus the h1.
const HOME = [
  { key: 'hs-hero-h1', group: 'Homepage hero', title: 'Hero headline (h1)',
    desc: '"LET\'S FIND YOUR NEXT JOB" — the hero title in the brand face. The page ships two hero copies (one per breakpoint); the visible one is picked, never the zero-rect twin.',
    sel: 'main h1, h1', find: (p) => p.locator('h1:visible').first(), states: ['default'] },
  { key: 'hs-search-form', group: 'Homepage hero', title: 'Job search form',
    desc: 'The hero job-search field row — measured at rest; typing and submitting were never done (the form navigates to the app).',
    sel: 'form', find: (p) => p.locator('form:visible').first(), states: ['default'] },
  { key: 'hs-search-input', group: 'Homepage hero', title: 'Job search input',
    desc: 'The rounded text field inside the hero form.',
    sel: 'form input[type="text"], form input', find: (p) => p.locator('form input:visible').first(), states: ['default', 'focused'] },
  { key: 'hs-search-button', group: 'Homepage hero', title: '"Search jobs" button',
    desc: 'The submit-styled button inside the hero form — pressed states are CDP-forced, so it never submits.',
    sel: 'form button[aria-label*="search" i] (icon-only "Search jobs" submit)', find: (p) => p.locator('form button[aria-label*="search" i]:visible, form button[type="submit"]:visible').first(), states: ['default', 'hover', 'focus-visible', 'pressed'] },
  { key: 'hs-filter-pill', group: 'Homepage hero', title: 'Job-type pill',
    desc: 'A selectable type pill under the search field ("Full-time").',
    sel: 'button (text Full-time)', find: async (p) => await domFind(p, /^full-time$/i, { sel: 'button', tag: 'fp', minW: 50, minH: 20 }), states: ['default', 'hover', 'focus-visible'] },
];

// The employers page: the notification banner, the segment switcher, the CTA
// link-buttons, the testimonial dots and the FAQ accordion.
const EMPLOYERS = [
  { key: 'hs-banner', group: 'Employers page', title: 'Notification banner',
    desc: 'The top banner (its height is --notification-banner-height); while it shows, the nav\'s top offset switches to --desktop-nav-top-offset-with-banner.',
    sel: 'div[class*="notification-banner-height"]:visible',
    find: (p) => p.locator('div[class*="notification-banner-height"]:visible').first(), states: ['default'] },
  { key: 'hs-banner-dismiss', group: 'Employers page', title: 'Banner dismiss button',
    desc: 'The icon-only "Dismiss notification" control — measured, never pressed.',
    sel: 'button[aria-label="Dismiss notification"]', find: (p) => p.locator('button[aria-label*="dismiss" i]:visible').first(), states: ['default', 'hover', 'focus-visible'] },
  { key: 'hs-segment-tab', group: 'Employers page', title: 'Segment switcher tab',
    desc: 'One of Source / Automate / Brand / Measure — opacity carries the selection. "selected" is the tab\'s own press: it swaps the feature panel.',
    sel: 'button (text Source|Automate)', find: async (p) => await domFind(p, /^(source|automate)$/i, { sel: 'button', tag: 'st', minW: 50, minH: 16 }), states: ['default', 'hover',
      { name: 'selected', via: 'the tab\'s own press — a local UI toggle that swaps the published panel',
        fn: async (loc) => { await loc.click({ timeout: 4000 }).catch(() => {}); await page.waitForTimeout(900); } }] },
  { key: 'hs-cta', group: 'Employers page', title: 'CTA link-button',
    desc: 'A solid call-to-action ("Post a job today" / "Get started" / "Contact sales") — the group.inline-flex pill.',
    sel: 'a.group.inline-flex (text Get started|Contact sales|Post a job)', find: async (p) => await domFind(p, /get started|contact sales|post a job today/i, { sel: 'a', tag: 'cta', minW: 60, minH: 24 }), states: ['default', 'hover', 'focus-visible', 'pressed'] },
  { key: 'hs-carousel-dot', group: 'Employers page', title: 'Testimonial dot',
    desc: 'A carousel page dot ("Go to testimonial N").',
    sel: 'button[aria-label*="testimonial" i]', find: (p) => p.locator('button[aria-label*="testimonial" i]:visible').first(), states: ['default', 'hover'] },
  { key: 'hs-faq', group: 'Employers page', title: 'FAQ accordion question',
    desc: 'A question row in the FAQ. "opened" is the question button\'s own press: it unfolds the answer.',
    sel: 'button (question)', find: async (p) => await domFind(p, /free plan|post a job directly|compare|value/i, { sel: 'button', tag: 'fq', minW: 200, minH: 18, leaf: false }), states: ['default', 'hover', 'focus-visible',
      { name: 'opened', via: 'the question button\'s own press — a local UI toggle',
        fn: async (loc) => { await loc.click({ timeout: 4000 }).catch(() => {}); await page.waitForTimeout(900); } }] },
];

// The pricing page: the plan comparison tables and its own FAQ.
const PRICING = [
  { key: 'pricing-table', group: 'Pricing page', title: 'Plan comparison table',
    desc: 'One of the plan/feature tables on /employers/pricing/ (the page mounts four).',
    sel: 'table', find: (p) => p.locator('table:visible').first(), states: ['default'] },
  { key: 'pricing-th', group: 'Pricing page', title: 'Table header cell',
    desc: 'A th in the comparison table.', sel: 'th', find: (p) => p.locator('th:visible').first(), states: ['default'] },
  { key: 'pricing-td', group: 'Pricing page', title: 'Table cell',
    desc: 'A td in the comparison table.', sel: 'td', find: (p) => p.locator('td:visible').first(), states: ['default'] },
  { key: 'pricing-plan-card', group: 'Pricing page', title: 'Plan card',
    desc: 'A plan column/card on the pricing page.',
    sel: '[class*="plan" i], [class*="tier" i], main section', find: async (p) => await domFind(p, /^(basic|pro|enterprise|promoted jobs?)$/i, { sel: 'main h2, main h3, main h4, main [class*="card" i] h2, main [class*="card" i] h3', tag: 'pc', up: 'div', minW: 60, minH: 16 }), states: ['default'] },
  { key: 'pricing-feature-tab', group: 'Pricing page', title: 'Feature group tab',
    desc: 'A "Target & Connect" / "Centralize" / "Brand" / "Measure" group button that switches the comparison section.',
    sel: 'button (text Target & Connect|Centralize)', find: async (p) => await domFind(p, /^(target & connect|centralize|brand|measure)$/i, { sel: 'button', tag: 'ft', minW: 60, minH: 16 }), states: ['default', 'hover',
      { name: 'selected', via: 'the tab\'s own press — a local UI toggle', fn: async (loc) => { await loc.click({ timeout: 4000 }).catch(() => {}); await page.waitForTimeout(900); } }] },
];

// The Marketo lead forms (request-more-info, cc-contact): vendor-rendered
// fields measured at rest. Nothing is typed and the form is never submitted.
const FORMS = [
  { key: 'mkto-form', page: 'request-more-info', group: 'Marketo forms', title: 'Demo form shell',
    desc: 'The "Request a demo" Marketo form — its fields mount from go.joinhandshake.com vendor script.',
    sel: 'form[class*="marketo" i], form', find: (p) => p.locator('form:visible').first(), states: ['default'] },
  { key: 'mkto-input', page: 'request-more-info', group: 'Marketo forms', title: 'Form text field',
    desc: 'A text input inside the Marketo form.', sel: 'form input[type="text"], form input',
    find: (p) => p.locator('form input:visible').first(), states: ['default', 'focused'] },
  { key: 'mkto-select', page: 'request-more-info', group: 'Marketo forms', title: 'Form select',
    desc: 'A select inside the Marketo form.', sel: 'form select',
    find: (p) => p.locator('form select:visible').first(), states: ['default'] },
  { key: 'mkto-submit', page: 'request-more-info', group: 'Marketo forms', title: 'Form submit button',
    desc: 'The form\'s submit control — measured, never pressed (pressed states are CDP-forced).',
    sel: 'form button[type="submit"], form button', find: (p) => p.locator('form button[type="submit"]:visible, form button:visible').first(), states: ['default', 'hover', 'focus-visible', 'pressed'] },
  { key: 'cc-form', page: 'cc-contact', group: 'Marketo forms', title: 'Career-center contact form',
    desc: 'The EDU contact form on /career-centers/contact/ — same Marketo stack.',
    sel: 'form', find: (p) => p.locator('form:visible').first(), states: ['default'] },
];

// The students page: the email capture forms and the sign-up CTA.
const STUDENTS = [
  { key: 'stu-email-input', group: 'Students page', title: 'Email capture field',
    desc: 'The "Type school or personal email here" field in the hero — measured at rest, nothing typed.',
    sel: 'input[type="email"]', find: (p) => p.locator('input[type="email"]:visible').first(), states: ['default', 'focused'] },
  { key: 'stu-signup-button', group: 'Students page', title: '"Sign up" CTA',
    desc: 'The students sign-up button (group.inline-flex).',
    sel: 'button.group.inline-flex (text Sign up)', find: async (p) => await domFind(p, /^sign up$/i, { sel: 'button, a', tag: 'ss', minW: 60, minH: 24 }), states: ['default', 'hover', 'focus-visible', 'pressed'] },
  { key: 'stu-text-link', group: 'Students page', title: 'Arrow text link',
    desc: '"Find jobs and internships →" — an arrow-suffixed text link in the brand face.',
    sel: 'a (text Find jobs and internships)', find: async (p) => await domFind(p, /find jobs and internships/i, { sel: 'a', tag: 'tl', minW: 60, minH: 10 }), states: ['default', 'hover', 'focus-visible'] },
  { key: 'stu-carousel-btn', group: 'Students page', title: 'Card carousel arrow',
    desc: 'A "Slide to the next/previous card" arrow button.',
    sel: 'button[aria-label*="card" i]', find: (p) => p.locator('button[aria-label*="slide" i]:visible, button[aria-label*="card" i]:visible').first(), states: ['default', 'hover'] },
];

// The blog index: the search field, category links and article cards.
const BLOG = [
  { key: 'blog-search-input', group: 'Blog', title: 'Blog search field',
    desc: 'The search input on the blog index — measured at rest, nothing typed.',
    sel: 'input[type="search"]', find: (p) => p.locator('input[type="search"]:visible, form input:visible').first(), states: ['default', 'focused'] },
  { key: 'blog-search-button', group: 'Blog', title: 'Search button',
    desc: 'The Search button beside the field — CDP-forced states only.',
    sel: 'button (text Search)', find: async (p) => await domFind(p, /^search$/i, { sel: 'button', tag: 'bb', minW: 50, minH: 20 }), states: ['default', 'hover', 'focus-visible', 'pressed'] },
  { key: 'blog-category-link', group: 'Blog', title: 'Category link',
    desc: 'An uppercase category link ("AI SKILLS STUDIO").',
    sel: 'a.uppercase', find: (p) => p.locator('a.uppercase:visible').first(), states: ['default', 'hover', 'focus-visible'] },
  { key: 'blog-card', group: 'Blog', title: 'Article card',
    desc: 'An article card link on the blog index.',
    sel: 'main a[href*="/blog/"] (the card-sized anchor, not a category link)', find: async (p) => await domFind(p, /./, { sel: 'main a[href*="/blog/"]', tag: 'bc', minW: 200, minH: 100, leaf: false }), states: ['default', 'hover'] },
  { key: 'blog-readmore', group: 'Blog', title: '"Read More" link',
    desc: 'The Read More affordance on an article card.',
    sel: 'a (text Read More)', find: async (p) => await domFind(p, /read more/i, { sel: 'a', tag: 'rm', minW: 40, minH: 10 }), states: ['default', 'hover'] },
];

// The careers page: the benefits tabs, the search field, department
// accordion and pagination.
const CAREERS = [
  { key: 'car-benefit-tab', group: 'Careers page', title: 'Benefits tab',
    desc: 'A benefits category button ("Health & wellness") — the tab\'s own press swaps the panel.',
    sel: 'button (text Health & wellness)', find: async (p) => await domFind(p, /health & wellness|financial support|growth|time off/i, { sel: 'button', tag: 'bt', minW: 60, minH: 16 }), states: ['default', 'hover',
      { name: 'selected', via: 'the tab\'s own press — a local UI toggle', fn: async (loc) => { await loc.click({ timeout: 4000 }).catch(() => {}); await page.waitForTimeout(900); } }] },
  { key: 'car-search-input', group: 'Careers page', title: 'Roles search field',
    desc: 'The open-roles search input — measured at rest, nothing typed.',
    sel: 'input[placeholder*="earch" i], input', find: (p) => p.locator('input:visible').first(), states: ['default', 'focused'] },
  { key: 'car-dept-button', group: 'Careers page', title: 'Department filter button',
    desc: 'The "All departments" filter dropdown in the roles list — "opened" is its own press.',
    sel: 'button.group.flex', find: (p) => p.locator('button.group.flex:visible').first(), states: ['default', 'hover',
      { name: 'opened', via: 'the header\'s own press — a local UI toggle', fn: async (loc) => { await loc.click({ timeout: 4000 }).catch(() => {}); await page.waitForTimeout(900); } }] },
  { key: 'car-job-link', group: 'Careers page', title: 'Job row link',
    desc: 'An open-role link in the list.',
    sel: 'a (job title)', find: async (p) => await domFind(p, /engineer|manager|director|designer|representative|lead/i, { sel: 'main a, [class*="role" i] a, a', tag: 'jl', minW: 120, minH: 20 }), states: ['default', 'hover'] },
  { key: 'car-page-button', group: 'Careers page', title: 'Pagination button',
    desc: 'A page number in the roles pagination.',
    sel: 'button.group.inline-flex (text 1|2|3)', find: async (p) => await domFind(p, /^[0-9]+$/, { sel: 'button', tag: 'pg', minW: 16, minH: 16 }), states: ['default', 'hover', 'focus-visible'] },
];

// The legal pages' left rail: an active section link and an inactive one.
const LEGAL = [
  { key: 'legal-nav-active', group: 'Legal pages', title: 'Legal nav link (active)',
    desc: 'The current section link in the legal left rail (opacity-100).',
    sel: 'main a.font-medium', find: (p) => p.locator('main a.font-medium:visible, aside a.font-medium:visible').first(), states: ['default', 'hover'] },
  { key: 'legal-nav-link', group: 'Legal pages', title: 'Legal nav link',
    desc: 'An inactive section link in the legal left rail (opacity-60).',
    sel: 'a.opacity-60', find: (p) => p.locator('a.opacity-60:visible').first(), states: ['default', 'hover', 'focus-visible'] },
];

// The consumer app's "Log in or sign up" page — the Rosetta component layer:
// the locale select, the email field, the rosetta-button, the Google SSO
// widget, the skip link and the employer link.
const ACCESS = [
  { key: 'app-shell', group: 'App access', title: 'Login page shell',
    desc: 'The /access page body — the consumer app\'s signed-out entry.',
    sel: 'main, #maincontent, body', find: (p) => p.locator('main, #maincontent').first(), states: ['default'] },
  { key: 'app-locale-select', group: 'App access', title: 'Locale select',
    desc: 'The "English (US)" rosetta-select in the page chrome.',
    sel: 'select.rosetta-select__hidden, select', find: (p) => p.locator('select:visible').first().locator('..').locator('..'), states: ['default'] },
  { key: 'app-email-field', group: 'App access', title: 'Email field',
    desc: 'The "Enter your email" rosetta-field — measured at rest, nothing typed.',
    sel: 'input[name="email"], input[type="text"]', find: (p) => p.locator('input[name="email"]:visible, input:visible').first(), states: ['default', 'focused'] },
  { key: 'app-continue-button', group: 'App access', title: '"Continue with email" button',
    desc: 'The rosetta-button submit — pressed states are CDP-forced, so the form never submits.',
    sel: 'button.rosetta-button', find: (p) => p.locator('button').filter({ hasText: /continue with email/i }).first(), states: ['default', 'hover', 'focus-visible', 'pressed'] },
  { key: 'app-google-button', group: 'App access', title: 'Google SSO button',
    desc: 'The "Continue with Google" button — Google\'s own rendered widget (GSI), recorded as vendor.',
    sel: '[class*="LgbsSe"], [id*="gsi" i], iframe[title*="Google" i], iframe[src*="accounts.google.com"]',
    find: (p) => p.locator('[class*="LgbsSe"], [id*="gsi" i], iframe[src*="accounts.google.com"], iframe[title*="Google" i]').first(), states: ['default'] },
  { key: 'app-employer-link', group: 'App access', title: '"Sign up as an employer" link',
    desc: 'The employer sign-up link under the login card.',
    sel: 'a (text employer)', find: async (p) => await domFind(p, /sign up as an employer|employer/i, { sel: 'a', tag: 'el', minW: 40, minH: 10 }), states: ['default', 'hover'] },
  { key: 'app-tos-link', group: 'App access', title: 'Terms link',
    desc: 'The Terms of Service link in the fine print.',
    sel: 'a (text Terms of Service)', find: async (p) => await domFind(p, /terms of service/i, { sel: 'a', tag: 'ts', minW: 40, minH: 8 }), states: ['default', 'hover'] },
];

const MOBILE = [
  { key: 'm-hs-topbar', group: 'Site chrome (mobile)', title: 'Mobile header pill',
    desc: 'The floating pill at 390px: the mobile nav wrapper is a 0-height relative container; the painted bar is its fixed child (wordmark, links, the "Open menu" button).',
    sel: 'nav[class*="xl:hidden"] > div:first-child (fixed pill)',
    find: (p) => p.locator('nav[class*="xl:hidden"] > div:visible').first(), states: ['default'] },
  { key: 'm-hs-hamburger', group: 'Site chrome (mobile)', title: '"Open menu" button',
    desc: 'The icon-only button (aria-label "Open menu", no text content) that opens the mobile nav sheet.',
    sel: 'button[aria-label="Open menu"]', find: (p) => p.locator('button[aria-label*="menu" i]:visible').first(), states: ['default', 'hover'] },
  { key: 'm-hs-drawer', group: 'Site chrome (mobile)', title: 'Nav sheet (open)',
    desc: 'The opened mobile navigation sheet. The "Open menu" press happens in find(): the sheet is only reachable once open, so the state itself is a no-op.',
    sel: 'div[class*="mobile-nav-height"][class*="100dvh"] (the fixed sheet under the bar; Ketch\'s dialog is excluded)',
    find: async (p) => {
      const sheet = p.locator('div[class*="mobile-nav-height"][class*="100dvh"]:not([class*="ketch" i]):visible');
      const ham = p.locator('button[aria-label*="menu" i]:visible').first();
      await ham.click({ timeout: 5000 }).catch(() => {});
      await p.waitForTimeout(1300);
      if (!(await sheet.count())) {
        // A late-mounting Ketch overlay can sit over the button; hide it and press again.
        await p.evaluate(() => {
          for (const el of document.querySelectorAll('[id*="ketch" i], [class*="ketch" i], iframe[src*="ketch" i]'))
            el.style.setProperty('display', 'none', 'important');
        }).catch(() => {});
        await ham.click({ timeout: 5000, force: true }).catch(() => {});
        await p.waitForTimeout(1300);
      }
      return sheet.first();
    }, states: [{ name: 'opened', via: 'the "Open menu" button\'s own press', fn: async () => {} }] },
];

const GROUPS = {
  chrome: { page: 'home', specs: [...CHROME, ...HOME] },
  employers: { page: 'employers', specs: EMPLOYERS },
  pricing: { page: 'pricing', specs: PRICING },
  forms: { page: 'request-more-info', specs: FORMS.filter((f) => f.page === 'request-more-info'), scrollFirst: true },
  'cc-forms': { page: 'cc-contact', specs: FORMS.filter((f) => f.page === 'cc-contact'), scrollFirst: true },
  students: { page: 'students', specs: STUDENTS },
  blog: { page: 'blog', specs: BLOG },
  careers: { page: 'careers', specs: CAREERS },
  legal: { page: 'legal', specs: LEGAL },
  access: { page: 'access', app: true, specs: ACCESS },
  mobile: { page: 'home', mobile: true, specs: MOBILE },
};

// ---------- runner ----------

const b = await chromium.launch();
context = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
await patch(context);
const mobCtx = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' });
await patch(mobCtx);

const wanted = process.argv.slice(2);
out._meta.read = new Date().toLocaleDateString('en-CA');
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); joinhandshake.com paints light only — there is no theme control';
out._meta.tool = 'tools/capture/public/measure.mjs';
out._meta.sheets ??= {};

for (const [key, g] of Object.entries(GROUPS)) {
  if (wanted.length && !wanted.includes(key)) continue;
  const ctx = g.mobile ? mobCtx : context;
  const url = g.app ? APP_URL : BASE + URLS[g.page];
  // The app surface's challenge clears only on some loads: fresh pages in
  // the same context retry the navigation until the real document arrives.
  let opened = false;
  for (let attempt = 0; attempt < (g.app ? 6 : 1) && !opened; attempt++) {
    page = await ctx.newPage();
    page.setDefaultTimeout(8000);
    cdp = await ctx.newCDPSession(page);
    await cdp.send('DOM.enable');
    await cdp.send('CSS.enable');
    log('open', key, g.mobile ? '(mobile)' : '', g.app ? '(app)' : '', url, attempt ? `(try ${attempt + 1})` : '');
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    const { clearChallenge } = await import('./lib.mjs');
    if (await clearChallenge(page, { tries: g.app ? 8 : 6, step: 2000 })) { opened = true; }
    else { await page.close(); log('  challenge did not clear'); }
  }
  if (!opened) { log('  BOUNDARY', key, 'never loaded a real page'); continue; }
  await page.waitForTimeout(7000);
  await closePromo(page);
  if (g.scrollFirst) {
    // Marketo mounts its fields once the form scrolls into view.
    await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
    await page.waitForTimeout(2500);
    await page.evaluate(() => scrollTo(0, 0));
    await page.waitForTimeout(1500);
  }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  if (g.setup) await g.setup(page).catch((e) => log('  setup failed:', e.message));
  // the readable sheets' transition declarations, for measurements.md
  out._meta.sheets[URLS[g.page] || 'access'] = await page.evaluate(() => {
    const found = [];
    for (const ss of document.styleSheets) {
      try {
        for (const r of ss.cssRules) {
          if (r.style && r.style.transition && r.style.transition !== 'all 0s') found.push({ transition: r.style.transition.slice(0, 90) });
        }
      } catch { /* cross-origin sheet */ }
    }
    return found.slice(0, 30);
  }).catch(() => []);

  for (const spec of g.specs) {
    const comp = out.components[spec.key] ??= {};
    comp.group = spec.group;
    comp.title = spec.title;
    comp.desc = spec.desc;
    comp.selector = spec.sel;
    comp.page = URLS[g.page] || '/access';
    comp.url = safeUrl(url);
    comp.run = new Date().toISOString();
    comp.states ??= {};
    let loc;
    // A lookup miss must not erase states a previous run already measured —
    // only a component with no good readings at all counts as missing.
    const hasStates = () => Object.values(comp.states ?? {}).some((s) => s && s.style);
    try { loc = await spec.find(page); } catch (e) {
      log(' ', spec.key, 'find failed:', e.message.split('\n')[0]);
      if (hasStates()) comp.rerunMiss = e.message.split('\n')[0]; else comp.missing = true;
      continue;
    }
    if (!(await loc.count()) || !(await loc.first().isVisible().catch(() => false))) {
      log(' ', spec.key, 'absent');
      if (hasStates()) comp.rerunMiss = 'absent on this run'; else comp.missing = true;
      continue;
    }
    delete comp.missing;
    delete comp.rerunMiss;
    loc = loc.first();
    for (const st of spec.states) {
      const name = typeof st === 'string' ? st : (st.name || 'opened');
      // pressed is cleared in finally so a failed read can never leak the
      // forced state into the next measurement.
      let pressed = null;
      try {
        await reset();
        let viaText = 'resting state';
        if (st === 'hover') { await hover(loc); viaText = via.hover; }
        else if (st === 'focus-visible') { await kbFocus(loc); viaText = via['focus-visible']; }
        else if (st === 'focused') { await loc.click({ timeout: 3000 }).catch(() => loc.evaluate((el) => el.focus())); await page.waitForTimeout(400); viaText = 'the field clicked into'; }
        else if (st === 'pressed') { pressed = await pressOn(loc); viaText = via.pressed; }
        else if (st && typeof st === 'object' && st.fn) { await st.fn(loc); viaText = st.via || 'reached by the component\'s own UI toggle'; }
        else if (typeof st === 'function') { await st(loc); viaText = 'reached by the component\'s own UI toggle'; }
        await centre(loc).catch(() => {});
        const v = await styleOf(loc);
        v.via = viaText;
        v.crop = await crop(page, loc, `${spec.key}-${name}`).catch((e) => { log('  crop failed', spec.key, name, e.message.split('\n')[0]); return undefined; });
        v.run = new Date().toISOString();
        comp.states[name] = v;
        log(' ', spec.key, name, 'ok');
      } catch (e) {
        // A failed rerun records the error beside the last good reading, not
        // over it — a good saved state outlives a transient failure.
        const prev = comp.states[name];
        comp.states[name] = (prev && prev.style)
          ? { ...prev, rerunError: e.message.split('\n')[0] }
          : { error: e.message.split('\n')[0] };
        log(' ', spec.key, name, 'FAILED', e.message.split('\n')[0]);
      } finally {
        if (pressed != null) await pressOff(pressed).catch(() => {});
      }
    }
    save();
  }
  if (g.teardown) await g.teardown(page).catch(() => {});
  await page.close();
}
await b.close();
log('done ->', OUT);
