// Measures huddlekit.com's signed-out components on its public pages, in
// every state that can be reached without signing in or submitting
// anything — plus the app.huddlekit.com login, the only surface the app
// serves anonymously (the `app-*` specs).
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing support tool contact blog-post integrations compare-page
// app-login mobile. Writes raw/components-computed.json (merged, so a subset
// of pages can be re-run) and one crop per component and state into
// components/crops/. raw/measurements.md is then built from the JSON by
// build-measurements.mjs.
//
// States:
//   hover          real mouse hover, 500ms settle for transitions
//   focus-visible  keyboard: focus, Shift+Tab, Tab, so the browser sees a keyboard focus
//   pressed        CDP CSS.forcePseudoState [active, hover]; no mouse button is pressed,
//                  so no link or button can fire
//   dark           on app-login: prefers-color-scheme emulated + reload —
//                  the signal the app honours (setAppTheme in lib.mjs). The
//                  marketing site has no dark surface of its own; its dark
//                  evidence is the nested .dark panels, measured at rest.
//   opened         a resting state reached by the component's own toggle:
//                  the nav's hover-open Solutions menu, a FAQ accordion, a
//                  billing switch, the feature tabs, the phone's "Toggle
//                  menu" button, the login's "Continue with email" reveal
//   focused        the search/login field clicked into — nothing is typed
// Nothing is typed, sent, searched or signed into. The only presses are
// local UI toggles the page's own chrome provides, plus the consent banner's
// Decline dismissal.
import fs from 'node:fs';
import path from 'node:path';
import { chromium, BASE, APP, M, open, closePromo, setAppTheme, paintedTheme, styleOf, crop, centre, domFind, patch, UA, UA_MOBILE, RAW } from './lib.mjs';
import { toggleBefore, toggleOpen, toggleRestore } from './toggle.mjs';
import { safeUrl } from '../safe-url.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

const URLS = {
  home: '/',
  pricing: '/pricing',
  support: '/support',
  tool: '/tools/color-contrast-checker',
  contact: '/contact',
  'blog-post': '/blog/introducing-huddlekit',
  integrations: '/integrations',
  'compare-page': '/compare/pastel-alternative',
  'app-login': { app: '/login' },
};
const urlOf = (key) => typeof URLS[key] === 'string' ? BASE + URLS[key] : APP + URLS[key].app;
const pathOf = (key) => typeof URLS[key] === 'string' ? URLS[key] : URLS[key].app;

let page, cdp, context, current;

// ---------- state drivers ----------

async function reset() {
  // open() leaves the tab on about:blank when a reload was blocked; every
  // state after that fails here, so the saved readings are kept
  if (page.url() === 'about:blank') throw new Error('the page was lost to a blocked reload; saved readings kept');
  await page.keyboard.press('Escape').catch(() => {});
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
  // The attempt is only evidence when focus really came back to the element
  // and paints the :focus-visible ring — anything else is a resting reading,
  // recorded under the "focus failed" via rather than claimed as a state.
  return await loc.evaluate((el) => {
    const ae = document.activeElement;
    const held = ae === el || el.contains(ae);
    let ring = false;
    try { ring = Boolean((ae && ae.matches(':focus-visible')) || el.matches(':focus-visible')); } catch { /* unpierceable */ }
    return { held, ring };
  }).catch(() => ({ held: false, ring: false }));
}

// Pick one element out of a selector's matches inside the page — marks the
// winner with data-m-mark="<tag>" and returns a locator for it. score(el, r,
// cs) returns a number, lowest wins; return Infinity to skip a match.
async function pick(p, sel, score, tag = 'pk') {
  const ok = await p.evaluate(([s, t, src]) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const fn = new Function('el', 'r', 'cs', `return (${src})(el, r, cs)`);
    let best = null, bestV = Infinity;
    for (const el of document.querySelectorAll(s)) {
      const r = el.getBoundingClientRect();
      if (!r.width || !r.height) continue;
      const cs = getComputedStyle(el);
      if (cs.visibility === 'hidden' || cs.opacity === '0') continue;
      const v = fn(el, r, cs);
      if (v < bestV) { bestV = v; best = el; }
    }
    if (!best) return false;
    best.setAttribute('data-m-mark', t);
    return true;
  }, [sel, tag, score.toString()]);
  return ok ? p.locator(`[data-m-mark="${tag}"]`) : p.locator('[data-m-mark="__none__"]');
}

// CSS.forcePseudoState through CDP: the press never happens, so no link can
// navigate and no button can fire.
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
// 'pressed' | 'dark' | 'focused' | (loc, page) => Promise<void|Locator>.
const via = { 'hover': 'mouse hover over the element', 'focus-visible': 'keyboard focus (Shift+Tab, Tab)', 'pressed': 'CDP CSS.forcePseudoState(:active:hover) — no real press', 'dark': 'same element after prefers-color-scheme repaints html.dark (the signal the app honours; the login has no theme control of its own)' };

// The marketing header: logo, Features / Solutions / Resources / Pricing /
// Sign in links, and the secondary "Get started" button.
const CHROME = [
  { key: 'announce-bar', group: 'Chrome', title: 'Announcement bar',
    desc: 'The top "New: hand feedback to your AI agent over MCP" announcement link — border-b over the header.',
    sel: 'a (announcement)', find: async (p) => await domFind(p, /hand feedback to your ai agent/i, { sel: 'a', tag: 'an', minW: 100 }), states: ['default', 'hover'] },
  { key: 'nav-header', group: 'Chrome', title: 'Site header',
    desc: 'The header holding the logo, the Features / Solutions / Resources / Pricing / Sign in nav and the "Get started" button.',
    sel: 'header', find: (p) => p.locator('header').first(), states: ['default'] },
  { key: 'nav-link', group: 'Chrome', title: 'Nav link',
    desc: 'A plain nav link ("Features"), text-foreground with hover:text-foreground/70.',
    sel: 'nav a, header a', find: (p) => p.locator('header a, nav a').filter({ hasText: /^features$/i }).filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible'] },
  { key: 'nav-menu-button', group: 'Chrome', title: 'Nav menu trigger',
    desc: 'The "Solutions" button that opens a nav-surface popover on hover. "opened" is after the real hover that opened it.',
    sel: 'button (text Solutions)', find: async (p) => await domFind(p, /^solutions$/i, { sel: 'button', tag: 'nv', minW: 40 }), states: ['default', 'hover',
      { name: 'opened', via: 'the trigger\'s own hover (the nav-surface popover open; the pointer is then moved away)', fn: async (loc) => {
        await hover(loc);
      } },
    ] },
  { key: 'nav-menu-surface', group: 'Chrome', title: 'Nav popover (open)',
    desc: 'The open nav-surface popover under the header — the Solutions menu the hover shows.',
    sel: '.nav-surface', find: async (p) => {
      const btn = await domFind(p, /^solutions$/i, { sel: 'button', tag: 'nvb', minW: 40 });
      if (await btn.count()) { await hover(btn); }
      return p.locator('.nav-surface, [role="menu"], [data-state="open"] ~ div').filter({ visible: true }).first();
    }, states: [{ name: 'opened', via: 'the Solutions trigger\'s own hover; the popover itself is read while open', fn: async () => {
      // reset() moved the pointer away and closed the popover — re-open it
      // on the repainted document before reading.
      const btn = await domFind(page, /^solutions$/i, { sel: 'button', tag: 'nvb2', minW: 40 });
      if (await btn.count()) await hover(btn);
      const s = page.locator('.nav-surface, [role="menu"], [data-state="open"] ~ div').filter({ visible: true }).first();
      if (await s.count() && await s.isVisible().catch(() => false)) return s;
    } }] },
  { key: 'nav-signin', group: 'Chrome', title: '"Sign in" link',
    desc: 'The header sign-in link — measured, never followed (it leads to app.huddlekit.com, which was captured separately).',
    sel: 'a (text Sign in)', find: async (p) => await domFind(p, /^sign in$/i, { sel: 'header a, nav a, a', tag: 'si', minW: 40 }), states: ['default', 'hover'] },
  { key: 'cta-primary', group: 'Chrome', title: 'Primary CTA button',
    desc: 'The solid "Get started for free" call-to-action (bg-primary text-primary-foreground, the inner-shadow stack) — links to the app, measured never followed.',
    sel: 'a (text Get started for free)', find: async (p) => await domFind(p, /get started for free/i, { sel: 'a', tag: 'ct', minW: 80 }), states: ['default', 'hover', 'focus-visible', 'pressed'] },
  { key: 'cta-secondary', group: 'Chrome', title: 'Secondary button',
    desc: 'The header\'s "Get started" button (bg-secondary with the same inner-shadow stack).',
    sel: 'a (text Get started)', find: async (p) => await pick(p, 'header a, nav a', (el) => {
      const t = (el.innerText || '').trim();
      return /^get started$/i.test(t) ? 0 : Infinity;
    }, 'cs'), states: ['default', 'hover', 'focus-visible', 'pressed'] },
  { key: 'cta-outline', group: 'Chrome', title: 'Outline button',
    desc: 'A bordered ghost action in the hero ("5-star reviews"): border + transparent fill, hover:bg-accent.',
    sel: 'a (text 5-star reviews)', find: async (p) => await domFind(p, /5-star reviews/i, { sel: 'a, button', tag: 'ob', minW: 60 }), states: ['default', 'hover', 'focus-visible'] },
];

const HOME = [
  { key: 'feature-tab', group: 'Home', title: 'Feature tab (vertical)',
    desc: 'One row of the vertical feature tabs ("Draw on the page"): role=tab, muted until selected. "selected" is the tab\'s own activation.',
    sel: '[role="tab"]', find: (p) => p.locator('[role="tab"]').filter({ hasText: /draw on the page/i }).filter({ visible: true }).first(), states: ['default', 'hover',
      { name: 'selected', via: 'the tab\'s own activation (aria-selected switches the demo panel)', fn: async (loc) => {
        await loc.click({ timeout: 4000 }).catch(() => {});
        await page.waitForTimeout(900);
      } },
    ] },
  { key: 'integration-card', group: 'Home', title: 'Integration card',
    desc: 'An integration card on the home grid ("Linear" — icon, name, one line): bg-background rounded-xl shadow-xs.',
    sel: 'a (text Linear)', find: async (p) => await domFind(p, /^linear\b/i, { sel: 'a', tag: 'ic', minW: 100, leaf: false }), states: ['default', 'hover'] },
  { key: 'mcp-card-dark', group: 'Home', title: 'Dark MCP panel',
    desc: 'The .dark "Let your AI agent fix comments over MCP" card — the marketing page\'s painted-dark surface evidence: bg-background/text-foreground inside .dark re-point to the dark palette.',
    sel: '.dark a, a.dark', find: (p) => p.locator('a.dark, .dark a').filter({ hasText: /ai agent/i }).first(), states: ['default', 'hover'] },
  { key: 'testimonial-card-dark', group: 'Home', title: 'Dark testimonial card',
    desc: 'A large .dark testimonial card (quote + attribution) in the testimonials grid.',
    sel: 'a.dark', find: (p) => p.locator('a.dark').filter({ hasText: /“|"/ }).first(), states: ['default', 'hover', 'focus-visible'] },
  { key: 'show-more', group: 'Home', title: '"Show more testimonials" button',
    desc: 'The ghost expander under the testimonial grid. "opened" is its own press (the grid grows).',
    sel: 'button (text Show more testimonials)', find: async (p) => await domFind(p, /show more testimonials/i, { sel: 'button', tag: 'sm', minW: 80 }), states: ['default', 'hover', 'focus-visible',
      { name: 'opened', via: 'the button\'s own press (testimonial grid expanded)', fn: async (loc) => {
        await loc.click({ timeout: 4000 }).catch(() => {});
        await page.waitForTimeout(900);
      } },
    ] },
  { key: 'faq-question', group: 'Home', title: 'FAQ accordion question',
    desc: 'A question row in the page FAQ accordion. "opened" is its own press revealing the answer.',
    sel: 'main button[aria-expanded] (question text)', find: (p) => p.locator('main button[aria-expanded]').filter({ hasText: /\?/ }).filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible',
      { name: 'opened', via: 'the question row\'s own press (answer visible; pressed again to close)', fn: async (loc) => {
        await loc.click({ timeout: 4000 }).catch(() => {});
        await page.waitForTimeout(700);
      } },
    ] },
  { key: 'footer', group: 'Chrome', title: 'Site footer (dark)',
    desc: 'The .dark footer (bg-background text-foreground inside .dark): Product / Solutions / Resources columns, "Cookie settings" button and the social links.',
    sel: 'footer.dark, footer', find: (p) => p.locator('footer.dark, footer').first(), states: ['default'] },
  { key: 'footer-link', group: 'Chrome', title: 'Footer link',
    desc: 'A muted footer link (text-muted-foreground) inside the dark footer.',
    sel: 'footer a', find: (p) => p.locator('footer a').filter({ visible: true }).first(), states: ['default', 'hover'] },
  { key: 'cookie-settings', group: 'Chrome', title: '"Cookie settings" button',
    desc: 'The footer control that re-shows the consent banner — a local UI toggle.',
    sel: 'button (text Cookie settings)', find: async (p) => await domFind(p, /cookie settings/i, { sel: 'button', tag: 'ck', minW: 60 }), states: ['default', 'hover',
      { name: 'opened', via: 'the button\'s own press (the consent banner returns; Decline dismisses it again)', fn: async (loc) => {
        await loc.click({ timeout: 4000 }).catch(() => {});
        await page.waitForTimeout(1200);
      } },
    ] },
];

// The consent banner is measured on its own page load with the banner still
// up — every other group opens with promo:'close' so the fixed panel never
// overlays another component's crop.
const CONSENT = [
  { key: 'consent-banner', group: 'Consent', title: 'Cookie consent banner',
    desc: 'The fixed bottom consent banner ("We\'d like to use cookies…"): bg-background rounded-2xl border shadow-lg with Decline / Accept.',
    sel: 'section.fixed', find: (p) => p.locator('section.fixed').filter({ hasText: /cookies/i }).first(), states: ['default'] },
  { key: 'consent-decline', group: 'Consent', title: 'Consent "Decline" button',
    desc: 'The decline control in the consent banner (secondary style).',
    sel: 'button (text Decline)', find: async (p) => await domFind(p, /^decline$/i, { sel: 'button', tag: 'dc', minW: 40 }), states: ['default', 'hover', 'focus-visible'] },
  { key: 'consent-accept', group: 'Consent', title: 'Consent "Accept" button',
    desc: 'The accept control in the consent banner (bg-primary).',
    sel: 'button (text Accept)', find: async (p) => await domFind(p, /^accept$/i, { sel: 'button', tag: 'ac', minW: 40 }), states: ['default', 'hover', 'focus-visible', 'pressed'] },
];

const PRICING = [
  { key: 'plan-card', group: 'Pricing', title: 'Plan card',
    desc: 'A pricing plan card on /pricing (name, price, feature list, CTA).',
    sel: 'main box (priced plan)', find: async (p) => await pick(p, 'main div, main section, main article', (el, r) => {
      if (r.width < 200 || r.width > 720 || r.height < 160) return Infinity;
      const t = el.innerText || '';
      if (!/\$\s*\d|€\s*\d|\d+\s*\/\s*(mo|month)|per month|monthly/i.test(t)) return Infinity;
      if (!/sign up|get started/i.test(t)) return Infinity;
      // The fewest descendants otherwise lands on the "Free forever" label.
      // A plan card holds a price, a feature list and a call to action.
      if ((t.match(/\n/g) || []).length < 4) return Infinity;
      return el.querySelectorAll('*').length;
    }, 'pc'), states: ['default'] },
  { key: 'billing-switch', group: 'Pricing', title: 'Billing switch',
    desc: 'A monthly/annual switch on the plan cards (role=switch, data-state=checked, bg-primary on). "off" is its own press — then pressed back.',
    sel: 'button[role="switch"]', find: (p) => p.locator('button[role="switch"]').filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible',
      { name: 'off', via: 'the switch\'s own press (aria-checked flips; pressed again to restore)',
        stateOf: async (loc) => await loc.getAttribute('aria-checked'),
        fn: async (loc) => {
          await loc.click({ timeout: 4000 });
          await page.waitForTimeout(700);
        }, restore: async (loc) => {
          await loc.click({ timeout: 4000 });
          await page.waitForTimeout(700);
        } },
    ] },
  { key: 'plan-cta', group: 'Pricing', title: '"Sign up free" button',
    desc: 'A plan call-to-action — links to the app sign-up, measured never followed.',
    sel: 'a (text Sign up free)', find: async (p) => await domFind(p, /sign up free/i, { sel: 'a', tag: 'su', minW: 70 }), states: ['default', 'hover', 'focus-visible', 'pressed'] },
  { key: 'compare-link-card', group: 'Pricing', title: 'Alternative-comparison card',
    desc: 'A "… alternative" card under the pricing grid, same card grammar as the integration cards.',
    sel: 'a (text alternative)', find: async (p) => await domFind(p, /alternative$/i, { sel: 'a', tag: 'al', minW: 100, leaf: false }), states: ['default', 'hover'] },
];

const SUPPORT = [
  { key: 'support-search', group: 'Support', title: 'Support search input',
    desc: 'The "Search…" field at the top of /support. "focused" is the field clicked into — nothing is typed.',
    sel: 'input', find: (p) => p.locator('input').filter({ visible: true }).first(), states: ['default', 'focused', 'focus-visible'] },
  { key: 'support-category', group: 'Support', title: 'Support category card',
    desc: 'A category card on the support index ("Getting started" — heading + one line).',
    sel: 'a (text Getting started)', find: async (p) => await domFind(p, /getting started/i, { sel: 'a', tag: 'sc', minW: 100, leaf: false }), states: ['default', 'hover'] },
];

const TOOL = [
  { key: 'tool-color-input', group: 'Tools', title: 'Colour input',
    desc: 'The native colour swatch input on the contrast checker (input[type=color]) — measured at rest.',
    sel: 'input[type="color"]', find: (p) => p.locator('input[type="color"]').filter({ visible: true }).first(), states: ['default', 'focus-visible'] },
  { key: 'tool-text-input', group: 'Tools', title: 'Hex text input',
    desc: 'The hex value text field beside the colour input (#000000) — measured at rest; nothing is typed.',
    sel: 'input (no type attr; .type reads text)', find: (p) => p.locator('input:not([type="color"]):not([type="submit"])').filter({ visible: true }).first(), states: ['default', 'focus-visible'] },
];

const CONTACT = [
  { key: 'contact-copy', group: 'Contact', title: '"Copy" icon button',
    desc: 'The copy button beside a published contact email — measured, never pressed (it writes to the clipboard).',
    sel: 'button (text Copy)', find: async (p) => await domFind(p, /^copy$/i, { sel: 'button', tag: 'cp', minW: 30 }), states: ['default', 'hover', 'focus-visible', 'pressed'] },
  { key: 'contact-row', group: 'Contact', title: 'Contact channel row',
    desc: 'A contact row on /contact ("Sales, inquiries & partnerships" + the published hello@huddlekit.com).',
    sel: 'main box (contact row)', find: async (p) => await pick(p, 'main div, main section', (el, r) => {
      if (r.width < 280 || r.width > 900 || r.height < 40) return Infinity;
      const t = el.innerText || '';
      // The email node alone also matches huddlekit.com. A row names the
      // channel and publishes the address.
      if (!/huddlekit\.com/i.test(t)) return Infinity;
      if (!/sales|inquir|partnership|support|press|hello@/i.test(t)) return Infinity;
      if (!/@/.test(t) || (t.match(/\n/g) || []).length < 1) return Infinity;
      return el.querySelectorAll('*').length;
    }, 'cr'), states: ['default'] },
];

const PROSE = [
  { key: 'prose-h1', group: 'Prose', title: 'Article title (h1)',
    desc: 'The post title on a blog article.', sel: 'main h1, h1', find: (p) => p.locator('main h1, h1').first(), states: ['default'] },
  { key: 'prose-meta', group: 'Prose', title: 'Article meta line',
    desc: 'The date / updated / read-time / author line under the title.', sel: 'main p, main time', find: async (p) => await pick(p, 'main p, main div', (el, r) => {
      const t = (el.innerText || '').trim();
      return /\d{4}-\d{2}-\d{2}|\d+ min read/i.test(t) && t.length < 200 ? r.width : Infinity;
    }, 'pm'), states: ['default'] },
  { key: 'prose-p', group: 'Prose', title: 'Body paragraph',
    desc: 'A paragraph of article prose.', sel: 'main p (sentence)', find: (p) => p.locator('main p').filter({ visible: true }).filter({ hasText: /\S+(\s+\S+){7,}/ }).first(), states: ['default'] },
  { key: 'prose-link', group: 'Prose', title: 'Prose link',
    desc: 'A body-text link inside the article.', sel: 'article :is(p, li) a', find: (p) => p.locator('article :is(p, li) a, main article :is(p, li) a').filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible'] },
  { key: 'breadcrumb', group: 'Prose', title: 'Breadcrumb',
    desc: 'The Home / Blog / … breadcrumb above the article.', sel: 'nav[aria-label*="breadcrumb" i], nav', find: (p) => p.locator('nav[aria-label*="breadcrumb" i], nav').filter({ hasText: /blog/i }).filter({ visible: true }).first(), states: ['default'] },
];

const INTEGRATIONS = [
  { key: 'integration-grid-card', group: 'Integrations', title: 'Integration page card',
    desc: 'A card on the /integrations index (Slack — icon, name, description).',
    sel: 'a (text Slack)', find: async (p) => await domFind(p, /^slack\b/i, { sel: 'a', tag: 'ig', minW: 100, leaf: false }), states: ['default', 'hover'] },
];

const COMPARE = [
  { key: 'compare-toc', group: 'Compare', title: '"Contents" rail',
    desc: 'The Contents navigation on a comparison page.', sel: 'nav, aside', find: async (p) => await domFind(p, /contents/i, { sel: 'nav, aside, h2, div', tag: 'ct', up: 'nav, aside', minW: 80 }), states: ['default'] },
  { key: 'compare-check-item', group: 'Compare', title: 'Feature-check list row',
    desc: 'A checklist row in the comparison (a lucide check / badge icon + capability line).',
    sel: 'main li:has(svg)', find: (p) => p.locator('main li').filter({ has: p.locator('svg') }).filter({ visible: true }).filter({ hasText: /\w{6,}/ }).first(), states: ['default'] },
];

const APP_LOGIN = [
  { key: 'app-login-card', group: 'App login', title: 'Sign-in panel',
    desc: 'The centred "Sign in to Huddlekit" panel: wordmark, heading, the Google and email buttons, and the privacy/terms line.',
    sel: 'main, main [class*="card"], div[class*="bg-"]', find: async (p) => await pick(p, 'main div, main section, div', (el, r) => {
      const t = el.innerText || '';
      if (!/sign in to huddlekit/i.test(t) || !/continue with/i.test(t)) return Infinity;
      return el.querySelectorAll('*').length;
    }, 'lc'), states: ['default', 'dark'] },
  { key: 'app-google-button', group: 'App login', title: '"Continue with Google" button',
    desc: 'The primary OAuth button (bg-primary). Never pressed — it would leave for Google sign-in.',
    sel: 'button (text Continue with Google)', find: async (p) => await domFind(p, /continue with google/i, { sel: 'button', tag: 'gb', minW: 100 }), states: ['default', 'hover', 'focus-visible', 'pressed', 'dark'] },
  { key: 'app-email-button', group: 'App login', title: '"Continue with email" button',
    desc: 'The secondary sign-in button (bg-secondary). "pressed" is the CDP-forced pseudo-state only; the real press is the email-reveal spec below.',
    sel: 'button (text Continue with email)', find: async (p) => await domFind(p, /continue with email/i, { sel: 'button', tag: 'eb', minW: 100 }), states: ['default', 'hover', 'focus-visible', 'pressed', 'dark'] },
  { key: 'app-email-input', group: 'App login', title: 'Email input',
    desc: 'The "Enter your email" field the Continue-with-email press reveals — a local state change; nothing is typed and Continue is never pressed.',
    sel: 'input[type="email"]', find: async (p) => {
      const btn = await domFind(p, /continue with email/i, { sel: 'button', tag: 'eb2', minW: 100 });
      if (await btn.count()) { await btn.click({ timeout: 4000 }).catch(() => {}); await p.waitForTimeout(1200); }
      return p.locator('input[type="email"]').filter({ visible: true }).first();
    }, states: ['default', 'focused', 'dark'] },
  { key: 'app-continue-button', group: 'App login', title: 'Email "Continue" submit',
    desc: 'The primary submit under the email field — measured, never pressed (it would send a sign-in code).',
    sel: 'button (text Continue with email)', find: async (p) => {
      const btn = await domFind(p, /continue with email/i, { sel: 'button', tag: 'eb3', minW: 100 });
      if (await btn.count()) { await btn.click({ timeout: 4000 }).catch(() => {}); await p.waitForTimeout(1200); }
      return await domFind(p, /^continue with email$/i, { sel: 'button', tag: 'cb', minW: 80 });
    }, states: ['default', 'hover', 'focus-visible'] },
  { key: 'app-back-button', group: 'App login', title: '"Back to login" button',
    desc: 'The ghost return control under the email form.',
    sel: 'button (text Back to login)', find: async (p) => {
      const btn = await domFind(p, /continue with email/i, { sel: 'button', tag: 'eb4', minW: 100 });
      if (await btn.count()) { await btn.click({ timeout: 4000 }).catch(() => {}); await p.waitForTimeout(1200); }
      return await domFind(p, /back to login/i, { sel: 'button', tag: 'bb', minW: 60 });
    }, states: ['default', 'hover'] },
];

const MOBILE = [
  { key: 'm-header', group: 'Chrome (mobile)', title: 'Mobile header',
    desc: 'The header at 390px: logo, the "Toggle menu" button and the "Get started" link.',
    sel: 'header', find: (p) => p.locator('header').first(), states: ['default'] },
  { key: 'm-menu-button', group: 'Chrome (mobile)', title: '"Toggle menu" button',
    desc: 'The hamburger that opens the phone nav.',
    sel: 'button (aria-label Toggle menu)', find: (p) => p.getByRole('button', { name: /toggle menu|menu/i }).filter({ visible: true }).first(), states: ['default', 'hover', 'focus-visible'] },
  { key: 'm-nav-drawer', group: 'Chrome (mobile)', title: 'Nav sheet (open)',
    desc: 'The opened navigation panel — the "Toggle menu" press drops an absolute rounded-md sheet under the sticky header; the press happens in find().',
    sel: 'header div[class*="absolute"]', find: async (p) => {
      const ham = p.getByRole('button', { name: /toggle menu|menu/i }).filter({ visible: true }).first();
      await ham.click({ timeout: 5000 }).catch(() => ham.evaluate((el) => el.click()).catch(() => {}));
      await p.waitForTimeout(1500);
      return await domFind(p, /^features$/i, { sel: 'a', tag: 'mn', up: 'div[class*="absolute"]', minW: 60, scope: 'header' });
    }, states: [{ name: 'opened', via: 'the "Toggle menu" button\'s own press; the open sheet is read', fn: async (loc) => {
      // reset() pressed Escape — re-open before reading.
      const ham = page.getByRole('button', { name: /toggle menu|menu/i }).filter({ visible: true }).first();
      if (await ham.count()) { await ham.click({ timeout: 5000 }).catch(() => {}); await page.waitForTimeout(1500); }
      return await domFind(page, /^features$/i, { sel: 'a', tag: 'mn2', up: 'div[class*="absolute"]', minW: 60, scope: 'header' });
    } }] },
];

const GROUPS = {
  consent: { page: 'home', consent: true, specs: CONSENT },
  home: { page: 'home', specs: [...CHROME, ...HOME] },
  pricing: { page: 'pricing', specs: PRICING },
  support: { page: 'support', specs: SUPPORT },
  tool: { page: 'tool', specs: TOOL },
  contact: { page: 'contact', specs: CONTACT },
  'blog-post': { page: 'blog-post', specs: PROSE },
  integrations: { page: 'integrations', specs: INTEGRATIONS },
  'compare-page': { page: 'compare-page', specs: COMPARE },
  'app-login': { page: 'app-login', specs: APP_LOGIN },
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
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); huddlekit.com paints light only — its .dark rules re-point the tokens inside nested dark panels, measured as their own components — while app.huddlekit.com paints html.dark + data-theme="dark" under prefers-color-scheme (emulated + reloaded), so `dark` states on app-login are measured on the painted dark surface';
out._meta.tool = 'tools/capture/public/measure.mjs';
out._meta.sheets ??= {};

for (const [key, g] of Object.entries(GROUPS)) {
  if (wanted.length && !wanted.includes(key)) continue;
  const ctx = g.mobile ? mobCtx : context;
  page = await ctx.newPage();
  page.setDefaultTimeout(8000);
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  const darkFn = setAppTheme;
  const url = urlOf(g.page);
  log('open', key, g.mobile ? '(mobile)' : '', url);
  // The consent group keeps the banner up to measure it; every other group
  // hides it so the fixed panel never overlays another component's crop.
  if (!(await open(page, url, { wait: 7000, promo: g.consent ? 'keep' : 'close' }))) { log('  group skipped: the page never loaded'); await page.close().catch(() => {}); continue; }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
  if (g.setup) await g.setup(page).catch((e) => log('  setup failed:', e.message));
  // the readable sheets' transition declarations, for measurements.md
  out._meta.sheets[pathOf(g.page)] = await page.evaluate(() => {
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
    comp.page = pathOf(g.page);
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
      // pressed/dark are cleared in finally so a failed read can never leak
      // the forced state into the next measurement.
      let pressed = null;
      let toggle = null;  // a toggled state's press and its state before, for the restore
      let darkOn = false;
      try {
        await reset();
        let viaText = 'resting state';
        let readLoc = loc;
        if (st === 'hover') { await hover(readLoc); viaText = via.hover; }
        else if (st === 'focus-visible') { const f = await kbFocus(readLoc); viaText = f && (f.held || f.ring) ? via['focus-visible'] : 'focus failed'; }
        else if (st === 'focused') { await readLoc.click({ timeout: 3000 }).catch(() => readLoc.evaluate((el) => el.focus())); await page.waitForTimeout(400); viaText = 'the field clicked into'; }
        else if (st === 'pressed') { pressed = await pressOn(readLoc); viaText = via.pressed; }
        else if (st === 'dark') {
          if (!(await darkFn(page, 'dark'))) { log(' ', spec.key, name, 'dark never painted — skipped'); continue; }
          darkOn = true; viaText = via.dark;
          // setAppTheme reloads the page for the boot script to apply the OS
          // signal, so every locator taken before it is stale — refind on the
          // repainted document (a find that reveals a form re-reveals it).
          const refound = await spec.find(page).catch(() => null);
          if (refound && await refound.count() && await refound.first().isVisible().catch(() => false)) {
            readLoc = refound.first();
            loc = refound.first();
          } else { log(' ', spec.key, name, 'not refound after the dark reload — skipped'); continue; }
        }
        else if (st && typeof st === 'object' && st.fn) { toggle = await toggleBefore(st, readLoc); const alt = await toggleOpen(st, toggle); if (alt && typeof alt.count === 'function' && await alt.count()) readLoc = alt; viaText = st.via || 'reached by the component\'s own UI toggle'; }
        else if (typeof st === 'function') { await st(readLoc); viaText = 'reached by the component\'s own UI toggle'; }
        await centre(readLoc).catch(() => {});
        const v = await styleOf(readLoc);
        v.via = viaText;
        v.crop = await crop(page, readLoc, `${spec.key}-${name}`).catch((e) => { log('  crop failed', spec.key, name, e.message.split('\n')[0]); return undefined; });
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
        // a toggled state presses its control back, so later components are
        // read in the resting layout (the ifttt pattern; 2026-11 audit, not run)
        // back to the state it had before its press (toggle.mjs): a press
        // that never landed leaves nothing to undo
        if (toggle && st.restore) {
          const refind = async () => { const a = await spec.find(page).catch(() => null); return a && await a.count() ? a.first() : null; };
          await toggleRestore(st, toggle, refind).catch((e) => log(' ', spec.key, name, 'restore failed', e.message.split('\n')[0]));
        }
        if (darkOn) {
          let back = await darkFn(page, 'light').catch(() => false);
          if (!back) back = await darkFn(page, 'light').catch(() => false);
          if (!back) {
            // A failed reset must never leak dark paint into the next
            // default reading: reload, which restores the light boot, and
            // re-find the element so later states measure the live page.
            log(' ', spec.key, 'light reset failed — reloading to the light boot');
            await open(page, url, { wait: 7000 }).catch(() => {});
            await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
            if (g.setup) await g.setup(page).catch(() => {});
            const refound = await spec.find(page).catch(() => null);
            if (refound && await refound.count()) loc = refound.first();
          }
        }
      }
    }
    save();
  }
  if (g.teardown) await g.teardown(page).catch(() => {});
  await page.close();
}
await b.close();
log('done ->', OUT);
