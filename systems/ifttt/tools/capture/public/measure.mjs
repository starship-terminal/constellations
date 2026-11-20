// Measures IFTTT's signed-out components on its public pages, in every
// state that can be reached without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [group ...]
//
// Groups: shell home explore plans service applet connect solutions misc
// mobile. Writes raw/components-computed.json (merged, so a subset of
// groups can be re-run) and one crop per component and state into
// components/crops/. raw/measurements.md is then built from the JSON by
// build-measurements.mjs.
//
// States:
//   hover          real mouse hover, 600ms settle for transitions
//   focus-visible  keyboard: focus, Shift+Tab, Tab, so the browser sees a keyboard focus
//   pressed        CDP CSS.forcePseudoState [active, hover]; no mouse button is pressed,
//                  so no link or button can fire
//   opened         a resting state reached by the component's own toggle:
//                  the Share button's modal, the plans billing switch, the
//                  featured tabs, the mobile menu
//   focused        a field clicked into — nothing is typed
// Nothing is typed, sent, searched, shared, bought or signed into. Log in,
// Get started, Connect, the plan CTAs and the Copy button inside the share
// modal are measured, never pressed: they lead to sign-in, checkout,
// account or a clipboard side effect. The Applet "Connect" control is
// measured at rest only.
import fs from 'node:fs';
import path from 'node:path';
import { chromium, BASE, HOME, M, open, closePromo, styleOf, crop, centre, domFind, patch, UA, UA_MOBILE, RAW } from './lib.mjs';
import { safeUrl } from '../safe-url.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

const URLS = {
  home: HOME + '/',
  explore: BASE + '/explore',
  plans: BASE + '/plans',
  service: BASE + '/twitter',
  'service-light': BASE + '/todoist',
  applet: BASE + '/applets/A38TqjpD-start-irobot-cleaning-when-you-leave-home',
  connect: BASE + '/connect/discord/instagram',
  'solutions-productivity': BASE + '/solutions/productivity',
  mcp: BASE + '/mcp',
  about: BASE + '/about',
  careers: BASE + '/careers',
  terms: BASE + '/terms',
  mobile: HOME + '/',
};

let page, cdp, context, current;

// ---------- state drivers ----------

async function reset() {
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

// Opens the page's own Share modal (button.modal-open) and returns the
// modal locator; the caller closes it with its own X after measuring.
async function openShareModal() {
  const btn = page.locator('button.modal-open').filter({ hasText: /share/i }).first();
  if (!(await btn.count())) return null;
  // Poll for the painted modal — a click landing mid close-animation is
  // swallowed by the catch and the 1.2s settle is not always enough.
  for (let i = 0; i < 3; i++) {
    await btn.click({ timeout: 5000 }).catch(() => {});
    const m = page.locator('div.share-modal:visible, div.modal:visible').first();
    try {
      await m.waitFor({ state: 'visible', timeout: 2500 });
      return m;
    } catch { /* retry the press */ }
  }
  return null;
}
async function closeShareModal() {
  // Only true close controls — a generic `.share-modal button` would press
  // the Copy pill (a clipboard side effect the capture must not do).
  const x = page.locator('.modal .modal-close:visible, .share-modal .modal-close:visible, .modal [class*="modal-close"]:visible').first();
  if (await x.count()) await x.click({ timeout: 4000 }).catch(() => {});
  else await page.keyboard.press('Escape');
  // Wait until the modal has actually left, not a fixed settle.
  await page.locator('div.share-modal:visible, div.modal:visible').first()
    .waitFor({ state: 'hidden', timeout: 4000 }).catch(() => {});
}

// ---------- the component specs ----------
// find: page -> Locator. states: 'hover' | 'focus-visible' | 'pressed' |
// 'focused' | { name, via, fn } — fn returns an alternate locator to
// measure (the opened surface), or null.
const via = { 'hover': 'mouse hover over the element', 'focus-visible': 'keyboard focus (Shift+Tab, Tab)', 'pressed': 'CDP CSS.forcePseudoState(:active:hover) — no real press', 'focused': 'the field clicked into' };

const B = 'a[class*="button"], button[class*="button"]';

const SHELL = [
  { key: 'site-header', group: 'Site chrome', title: 'Site header',
    desc: 'header.unified-header: the IFTTT.ai wordmark, the search field, Explore / Plans links, "Log in" (outlined) and "Get started" (filled) — .dark.on-color over the dark heroes.',
    sel: 'header.unified-header', find: (p) => p.locator('header.unified-header:visible').first(), states: ['default'] },
  { key: 'nav-logo', group: 'Site chrome', title: 'IFTTT.ai wordmark',
    desc: 'The logo link home: the IFTTT.ai mark as inline SVG.',
    sel: 'a.logo.logo-ifttt-ai', find: (p) => p.locator('a.logo:visible').first(), states: ['default'] },
  { key: 'nav-search', group: 'Site chrome', title: 'Header search field',
    desc: 'input.ifttt-search-input "Search for Applets, services, etc." — measured and focused, never queried.',
    sel: 'input.ifttt-search-input', find: (p) => p.locator('input.ifttt-search-input:visible').first(), states: ['default', 'focused'] },
  { key: 'nav-link', group: 'Site chrome', title: 'Nav link',
    desc: 'A primary nav link ("Explore") — a.nav-link.link-menu.',
    sel: 'a.nav-link', find: async (p) => await domFind(p, /^explore$/i, { sel: 'a.nav-link', tag: 'nl', minW: 30 }), states: ['default', 'hover', 'focus-visible'] },
  { key: 'nav-login', group: 'Site chrome', title: '"Log in" button',
    desc: 'a.sign-in.button-tertiary.button-outlined — the outlined pill; measured, never followed (it leads to sign-in).',
    sel: 'a.sign-in.button-tertiary', find: async (p) => await domFind(p, /^log in$/i, { sel: 'a, button', tag: 'li', minW: 60 }), states: ['default', 'hover', 'focus-visible', 'pressed'] },
  { key: 'nav-signup', group: 'Site chrome', title: '"Get started" button',
    desc: 'a.button-tertiary.sign-up — the filled near-black pill in the header; measured, never followed (it leads to /join).',
    sel: 'a.sign-up.button-tertiary', find: async (p) => await domFind(p, /^get started$/i, { sel: 'a, button', tag: 'su', minW: 80 }), states: ['default', 'hover', 'focus-visible', 'pressed'] },
  { key: 'site-footer', group: 'Site chrome', title: 'Site footer',
    desc: 'The page footer: link columns, the app-store badges and the social icons.',
    sel: 'footer', find: (p) => p.locator('footer:visible').last(), states: ['default'] },
  { key: 'footer-link', group: 'Site chrome', title: 'Footer link',
    desc: 'A link inside the footer columns.',
    sel: 'footer a', find: (p) => p.locator('footer a:visible').filter({ hasText: /\w{3}/ }).first(), states: ['default', 'hover'] },
];

const HOME_SPECS = [
  { key: 'hero-headline', group: 'Home', title: 'Hero headline',
    desc: 'The home hero h1 "The easiest way to automate anything" — Museo Sans Rounded 900.',
    sel: 'h1', find: (p) => p.locator('h1:visible').first(), states: ['default'] },
  { key: 'hero-prompt', group: 'Home', title: '"Describe what you\'d like to build" field',
    desc: 'textarea.prompt-hero-input — the AI prompt box the hero is built around. focused is the field clicked into; nothing is typed or submitted.',
    sel: 'textarea.prompt-hero-input', find: (p) => p.locator('textarea.prompt-hero-input:visible').first(), states: ['default', 'focused'] },
  { key: 'hero-submit', group: 'Home', title: '"Start building" button',
    desc: 'button.button-primary.prompt-hero-submit — the big black pill under the prompt. Measured, never pressed (it submits the prompt).',
    sel: 'button.prompt-hero-submit', find: (p) => p.locator('button.prompt-hero-submit:visible').first(), states: ['default', 'hover', 'focus-visible', 'pressed'] },
  { key: 'featured-tab', group: 'Home', title: 'Featured category tab',
    desc: 'A featured-Applets category tab (button.featured-tab). "selected" is its own activation — a local UI toggle, restored to Popular after.',
    sel: 'button.featured-tab', find: async (p) => await domFind(p, /^smart home$/i, { sel: 'button.featured-tab', tag: 'ft', minW: 60 }), states: ['default', 'hover',
      { name: 'selected', via: 'the tab\'s own activation', fn: async (loc) => {
        await loc.click({ timeout: 4000 }).catch(() => {});
        await page.waitForTimeout(1200);
        return loc;
      }, restore: async () => {
        // A later default reading of .featured-tab.active must be Popular, not the tab this spec just selected.
        const pop = page.locator('button.featured-tab').filter({ hasText: /^popular$/i }).first();
        if (await pop.count()) { await pop.click({ timeout: 4000 }).catch(() => {}); await page.waitForTimeout(800); }
      } },
    ] },
  { key: 'featured-tab-active', group: 'Home', title: 'Featured tab, active',
    desc: 'The resting "Popular" tab — the selected pill state. Measured only when its text is Popular, so a leftover selected tab is never stored as the resting default.',
    sel: 'button.featured-tab.active', find: async (p) => {
      const loc = p.locator('button.featured-tab.active:visible').first();
      const text = ((await loc.innerText().catch(() => '')) || '').trim();
      if (text && !/^popular$/i.test(text)) return p.locator('[data-m-mark="__none__"]');
      return loc;
    }, states: ['default'] },
  { key: 'service-chip', group: 'Home', title: 'Service icon chip',
    desc: 'One floating service icon in the hero automation canvas — the rounded-square brand tiles that drift across the hero.',
    sel: 'img, a, div', find: async (p) => await pick(p, '[class*="automation-apps"] img, [class*="app-icon"], [class*="service-icon"]', (el, r) => r.width > 20 && r.width < 130 ? r.y : Infinity, 'sc'), states: ['default'] },
  { key: 'secondary-cta', group: 'Home', title: 'Secondary CTA',
    desc: '"Join today" / "Explore all Applets" — a.button-secondary, the large outlined action. Measured, never followed (it leads to /join or /explore).',
    sel: 'a.button-secondary', find: (p) => p.locator('a.button-secondary:visible').first(), states: ['default', 'hover', 'focus-visible', 'pressed'] },
  { key: 'section-heading', group: 'Home', title: 'Section heading',
    desc: 'A home section heading (an h2 in the modules below the fold).',
    sel: 'h2', find: (p) => p.locator('h2:visible').first(), states: ['default'] },
];

const EXPLORE = [
  { key: 'explore-hero', group: 'Explore', title: 'Explore hero (dark)',
    desc: 'The dark "Automate X with Y" hero band on /explore: near-black ground, the prompt card and the cycling service names.',
    sel: 'section, div[class*="hero"]', find: async (p) => await pick(p, '[class*="hero"], section', (el, r) => r.width > 600 && r.height > 200 ? r.y : Infinity, 'eh'), states: ['default'] },
  { key: 'explore-prompt', group: 'Explore', title: 'Explore prompt field',
    desc: 'textarea.prompt-hero-input inside the dark hero card — "tell us what you\'d like to automate". focused only; never submitted.',
    sel: 'textarea.prompt-hero-input', find: (p) => p.locator('textarea.prompt-hero-input:visible').first(), states: ['default', 'focused'] },
  { key: 'explore-prompt-card', group: 'Explore', title: 'Prompt card',
    desc: 'The white card holding the prompt field and its "Start building" submit inside the dark hero. The dark hero section is explore-hero, not this card.',
    sel: '[class*="prompt-card"], form:has(textarea.prompt-hero-input)', find: async (p) => await pick(p, '[class*="prompt-card"], form:has(textarea.prompt-hero-input)', (el, r, cs) => {
      // The hero section also matches a bare [class*="prompt"] and holds the textarea as a descendant. Require the card itself: white, card-sized, and the textarea's nearest painted ancestor.
      if (!el.querySelector('textarea.prompt-hero-input')) return Infinity;
      if (r.width < 280 || r.width > 900 || r.height < 48 || r.height > 280) return Infinity;
      if (cs.backgroundColor === 'rgba(0, 0, 0, 0)') return Infinity;
      return r.y * 10000 + r.width;
    }, 'ep'), states: ['default'] },
  { key: 'explore-service-chip', group: 'Explore', title: 'Service chip in hero',
    desc: 'a.explore-hero-service — a service name chip ("Pinterest") in the "Automate X with Y" cycler.',
    sel: 'a.explore-hero-service', find: (p) => p.locator('a.explore-hero-service:visible').first(), states: ['default', 'hover'] },
  { key: 'example-prompt-card', group: 'Explore', title: '"Try these examples" card',
    desc: 'One translucent suggestion card under the prompt ("If there\'s a new Tweet with keyword, add to sheets.").',
    sel: 'a, div', find: async (p) => await pick(p, 'a, div[class*="example"], [class*="suggestion"]', (el, r) => /tweet|phone call|rss feed/i.test(el.innerText || '') && r.height > 40 && r.height < 200 ? r.x : Infinity, 'ex'), states: ['default'] },
  { key: 'explore-tab', group: 'Explore', title: 'Explore gallery tab',
    desc: 'The All / Applets / Services / Stories gallery tabs (a.text-h5). "active" is the current tab.',
    sel: 'a.text-h5', find: async (p) => await domFind(p, /^services$/i, { sel: 'a.text-h5', tag: 'et', minW: 40 }), states: ['default', 'hover'] },
  { key: 'explore-tab-active', group: 'Explore', title: 'Explore gallery tab, active',
    desc: 'The resting "All" tab — the active state (a.text-h5.active).',
    sel: 'a.text-h5.active', find: (p) => p.locator('a.text-h5.active:visible').first(), states: ['default'] },
  { key: 'applet-card', group: 'Explore', title: 'Applet card',
    desc: 'A gallery applet card (a.applet-card-body inside li.web-applet-card): the tile with service icons, title, author and use count.',
    sel: 'a.applet-card-body', find: (p) => p.locator('a.applet-card-body:visible').first(), states: ['default', 'hover'] },
  { key: 'service-card', group: 'Explore', title: 'Service card',
    desc: 'a.service-card — a service tile in the gallery grid: brand icon over name on white.',
    sel: 'a.service-card', find: (p) => p.locator('a.service-card:visible').first(), states: ['default', 'hover'] },
  { key: 'story-card', group: 'Explore', title: 'Story card',
    desc: 'a.story-box — a story tile ("Put AI to work for you") in the gallery.',
    sel: 'a.story-box', find: (p) => p.locator('a.story-box:visible').first(), states: ['default'] },
  { key: 'gallery-search', group: 'Explore', title: '"Search automations" field',
    desc: 'The gallery\'s own search input (input.ifttt-search-input "Search automations"). Focused only; never queried.',
    sel: 'input[placeholder*="automations" i]', find: (p) => p.locator('input[placeholder*="automations" i]:visible').first(), states: ['default', 'focused'] },
];

const PLANS = [
  { key: 'billing-toggle', group: 'Plans', title: 'Monthly / Yearly switch',
    desc: 'button.switch-field (role=switch) in the credits-plans-toggle — the billing-period control. "yearly"/"monthly" are its own presses, the repainted prices proof; restored to the default (Yearly).',
    sel: 'button.switch-field[role="switch"]', find: (p) => p.locator('button.switch-field[role="switch"]:visible').first(), states: ['default', 'hover',
      { name: 'toggled', via: 'the switch\'s own press (Yearly -> Monthly, then restored)', fn: async (loc) => {
        await loc.click({ timeout: 4000 }).catch(() => {});
        await page.waitForTimeout(1200);
        return loc;
      }, restore: async (loc) => {
        // Clicking the switch leaves Monthly on. Later default readings (the badge, the plan cards) must see Yearly again.
        const on = await loc.getAttribute('aria-checked').catch(() => null);
        const cls = (await loc.getAttribute('class').catch(() => '')) || '';
        if (on === 'false' || /switch-field-off/.test(cls) || !/switch-field-on/.test(cls)) {
          await loc.click({ timeout: 4000 }).catch(() => {});
          await page.waitForTimeout(800);
        }
      } },
    ] },
  { key: 'billing-toggle-wrap', group: 'Plans', title: 'Billing toggle with labels',
    desc: 'div.credits-plans-toggle — Monthly | switch | Yearly + the "SAVE 30%" badge.',
    sel: 'div.credits-plans-toggle', find: (p) => p.locator('div.credits-plans-toggle:visible').first(), states: ['default'] },
  { key: 'save-badge', group: 'Plans', title: '"SAVE 30%" badge',
    desc: 'The green discount badge beside the yearly label. The billing row that contains it is billing-toggle-wrap, not the badge.',
    sel: 'span.credits-plans-save, [class*="save"]', find: async (p) => await pick(p, 'span.credits-plans-save, [class*="credits-plans-save"], [class*="save-badge"]', (el, r) => {
      const text = (el.innerText || '').trim();
      if (!/^save\s*30%?$/i.test(text)) return Infinity;
      if (r.height >= 40 || r.width >= 160 || r.width < 20) return Infinity;
      return r.x;
    }, 'sb'), states: ['default'] },
  { key: 'plan-card', group: 'Plans', title: 'Plan card (Free)',
    desc: 'A pricing card: name, $ price, credits line, feature list with check icons and a "Get started" outline CTA.',
    sel: 'div, li', find: async (p) => await pick(p, '[class*="price-list"] > *, [class*="plan"] li, li, div[class*="card"]', (el, r) => /free|\$0/i.test(el.innerText || '') && r.height > 200 && r.width > 150 && r.width < 700 ? r.x : Infinity, 'pc'), states: ['default'] },
  { key: 'plan-card-recommended', group: 'Plans', title: 'Plan card, recommended (Pro)',
    desc: 'The highlighted Pro card — dark header, "RECOMMENDED" ribbon, filled "Get started" CTA.',
    sel: 'div, li', find: async (p) => await pick(p, '[class*="price-list"] > *, [class*="plan"] li, li, div[class*="card"]', (el, r) => /recommended/i.test(el.innerText || '') && r.height > 200 && r.width < 700 ? r.x : Infinity, 'pr'), states: ['default'] },
  { key: 'plan-price', group: 'Plans', title: 'Plan price figure',
    desc: 'The big "$0.00 / month" figure on a plan card — the display number style.',
    sel: 'span, div', find: async (p) => await pick(p, 'span, div, strong', (el, r) => /\$\d/.test(el.innerText || '') && (el.innerText || '').trim().length < 30 && r.height > 20 ? r.y : Infinity, 'pp'), states: ['default'] },
  { key: 'plan-feature', group: 'Plans', title: 'Plan feature row',
    desc: 'A feature line inside a plan card ("All features unlocked") with its check icon.',
    sel: 'li', find: async (p) => await pick(p, 'li', (el, r) => /unlocked|applets|credits/i.test(el.innerText || '') && r.height < 60 ? r.y : Infinity, 'pf'), states: ['default'] },
  { key: 'plan-cta', group: 'Plans', title: 'Plan "Get started" CTA',
    desc: 'The outlined button on a plan card — measured, never followed (it leads to checkout).',
    sel: 'a.button-tertiary', find: async (p) => await pick(p, 'a.button-tertiary', (el, r) => /get started/i.test(el.innerText || '') && r.y > 300 ? r.y : Infinity, 'cta'), states: ['default', 'hover', 'pressed'] },
  { key: 'plan-cta-filled', group: 'Plans', title: 'Plan CTA on the recommended card',
    desc: 'The filled "Get started" on the Pro card — measured, never followed. The header signup is nav-signup; this one sits inside the recommended plan card, below the fold.',
    sel: '[class*="price-list"] a.button-tertiary:not(.button-outlined), [class*="plan"] a.button-tertiary:not(.button-outlined)', find: async (p) => await pick(p, '[class*="price-list"] a, [class*="plan"] a, [class*="credits-plan"] a', (el, r) => {
      if (!/get started/i.test(el.innerText || '')) return Infinity;
      if (el.closest('header, .unified-header')) return Infinity;
      if (r.y < 200) return Infinity;
      if (el.classList.contains('button-outlined') || el.classList.contains('sign-up')) return Infinity;
      const card = el.closest('li, [class*="card"], [class*="plan"]');
      if (!card || !/recommended/i.test(card.innerText || '')) return Infinity;
      return r.y;
    }, 'cf'), states: ['default', 'hover', 'pressed'] },
];

const DETAIL = [
  { key: 'back-button', group: 'Detail pages', title: 'Back button',
    desc: 'The fixed "Back" pill on service/applet/connect pages — measured, never followed.',
    sel: 'a[class*="back-button"], a.button-with-icon', find: async (p) => {
      const l = await domFind(p, /^back$/i, { sel: 'a, button', tag: 'bk', minW: 60 });
      if (await l.count()) return l;
      // "Back" is an icon-only outlined pill (a.button-with-icon) pinned top-left.
      return await pick(p, 'a.button-with-icon, a.button-tertiary', (el, r) => r.y < 200 && r.x < 220 && r.width < 220 ? r.x : Infinity, 'bk2');
    }, states: ['default', 'hover', 'pressed'] },
  { key: 'share-button', group: 'Detail pages', title: 'Share button',
    desc: 'button.modal-open "Share" — opens the site\'s own share modal. "opened" is its own press painting .modal; the modal is closed with its X after.',
    sel: 'button.modal-open', find: async (p) => await domFind(p, /share/i, { sel: 'button.modal-open', tag: 'sh', minW: 60 }), states: ['default', 'hover',
      { name: 'opened', via: 'the Share button\'s own press (the share modal open; closed with its X after)', fn: async () => {
        return await openShareModal();
      } },
    ] },
  { key: 'share-modal-copy', group: 'Detail pages', title: 'Share modal "Copy" button',
    desc: 'The black Copy pill inside the share modal — measured inside the opened modal, never pressed (a clipboard side effect).',
    sel: '.share-modal button, .share-modal a, .modal button, .modal a', find: async (p) => {
      const vis = await p.locator('div.share-modal:visible, div.modal:visible').count();
      if (!vis) await openShareModal();
      const loc = p.locator('.share-modal:visible, .modal:visible').locator('button, a').filter({ hasText: /copy/i }).first();
      return loc;
    }, states: ['default'],
  },
  { key: 'share-url-field', group: 'Detail pages', title: 'Share URL field',
    desc: 'input.share-url-input — the read-only short-link field in the share modal.',
    sel: 'input.share-url-input', find: async (p) => {
      if (!(await p.locator('div.share-modal:visible, div.modal:visible').count())) await openShareModal();
      const loc = p.locator('input.share-url-input:visible').first();
      return loc;
    }, states: ['default'] },
  { key: 'service-hero', group: 'Detail pages', title: 'Service / applet hero',
    desc: 'The branded hero band on a detail page: service icons, the display headline and lede — dark on service and connect pages, the partner brand colour on applet pages.',
    sel: 'section, div', find: async (p) => await pick(p, 'section, [class*="hero"], [class*="banner"]', (el, r) => r.width > 700 && r.height > 250 ? r.y : Infinity, 'dh'), states: ['default'] },
  { key: 'service-icon', group: 'Detail pages', title: 'Service icon',
    desc: 'The service\'s rounded-square brand tile in a hero or card.',
    sel: 'img', find: async (p) => await pick(p, 'img', (el, r) => r.width > 30 && r.width < 160 && Math.abs(r.width - r.height) < 8 ? r.y : Infinity, 'si'), states: ['default'] },
  { key: 'get-started-today', group: 'Detail pages', title: '"Get started today" button',
    desc: 'The white pill on the dark heroes — measured, never followed (it leads to sign-up).',
    sel: 'a, button', find: async (p) => await domFind(p, /get started today/i, { sel: 'a, button', tag: 'gt', minW: 100 }), states: ['default', 'hover', 'pressed'] },
];

const APPLET = [
  { key: 'connect-toggle', group: 'Applet page', title: '"Connect" toggle',
    desc: 'The big black pill with the brand-coloured knob — the applet\'s install control, styled like a giant switch. Measured, never pressed (it leads to sign-in).',
    sel: 'a, button, div.connect-cta', find: async (p) => await domFind(p, /^connect$/i, { sel: 'a, button, div[role="button"], div.connect-cta, [class*="connect-button"]', tag: 'cn', minW: 150, minH: 40 }), states: ['default', 'hover', 'pressed'] },
  { key: 'applet-meta', group: 'Applet page', title: 'Applet meta line',
    desc: '.applet-meta-line — the "iRobot · 20.8k" byline under the headline.',
    sel: '.applet-meta-line', find: (p) => p.locator('.applet-meta-line:visible').first(), states: ['default'] },
  { key: 'author-link', group: 'Applet page', title: 'Author link',
    desc: 'a.author-link.link-on-color — the applet author on the brand-coloured hero.',
    sel: 'a.author-link', find: (p) => p.locator('a.author-link:visible').first(), states: ['default', 'hover'] },
  { key: 'trigger-row', group: 'Applet page', title: 'Trigger row',
    desc: 'A trigger line in the "About this Applet" detail ("You exit an area" — a.meta-type "Realtime trigger").',
    sel: 'a.meta-type', find: async (p) => await pick(p, 'a, div', (el, r) => /realtime trigger|trigger/i.test(el.innerText || '') && r.height < 60 && r.y > 100 ? r.y : Infinity, 'tr'), states: ['default'] },
  { key: 'service-item', group: 'Applet page', title: 'Service list row',
    desc: 'a.service-item — a service row in the page\'s service list ("Location", "iRobot").',
    sel: 'a.service-item', find: (p) => p.locator('a.service-item:visible').first(), states: ['default', 'hover'] },
];

const SOLUTIONS = [
  { key: 'solutions-hero', group: 'Solutions', title: 'Solutions hero',
    desc: 'The hero band on a solutions page ("Achieve more in less time").',
    sel: 'section, div', find: async (p) => await pick(p, 'section, [class*="hero"], [class*="banner"]', (el, r) => r.width > 700 && r.height > 200 ? r.y : Infinity, 'sh'), states: ['default'] },
  { key: 'solutions-card', group: 'Solutions', title: 'Solutions feature card',
    desc: 'A feature or use-case card on the solutions page.',
    sel: 'div, a', find: async (p) => await pick(p, '[class*="card"], [class*="feature"], article', (el, r) => r.height > 120 && r.width > 200 && r.width < 800 ? r.y : Infinity, 'sc'), states: ['default'] },
];

const MISC = [
  { key: 'marketing-h1', group: 'Marketing pages', title: 'Marketing h1',
    desc: 'The page headline on a marketing surface (mcp / about / careers).',
    sel: 'h1', find: (p) => p.locator('h1:visible').first(), states: ['default'] },
  { key: 'prose-p', group: 'Marketing pages', title: 'Body paragraph',
    desc: 'A body paragraph of marketing or legal prose.',
    sel: 'p', find: (p) => p.locator('p:visible, li:visible').filter({ hasText: /\S+(\s+\S+){9,}/ }).first(), states: ['default'] },
];

const LEGAL = [
  { key: 'prose-link', group: 'Marketing pages', title: 'Inline prose link',
    desc: 'A link inside body prose — the legal pages carry them (/mcp prose has no inline links).',
    sel: 'main p a, p a', find: (p) => p.locator('main :is(p,li) a:visible, p a:visible').filter({ hasText: /\w{2}/ }).first(), states: ['default', 'hover'] },
];

const MOBILE = [
  { key: 'm-header', group: 'Mobile (390)', title: 'Mobile header',
    desc: 'The 390px header: wordmark, search button and the hamburger.',
    sel: 'header.unified-header', find: (p) => p.locator('header.unified-header:visible').first(), states: ['default'] },
  { key: 'm-menu-button', group: 'Mobile (390)', title: 'Hamburger button',
    desc: 'The mobile menu button. "opened" is its own press painting the full-screen menu (logo, Explore/Plans links, Log in / Get started) — closed with its own X.',
    sel: 'button.closed', find: (p) => p.locator('button.closed:visible').first(), states: ['default',
      { name: 'opened', via: 'the hamburger\'s own press (the full-screen mobile menu open; closed with its X after)', fn: async (loc) => {
        await loc.click({ timeout: 4000 }).catch(() => {});
        await page.waitForTimeout(1400);
        const m = page.locator('section.right-group:visible, [class*="mobile-menu"]:visible, nav:visible').last();
        return (await m.count()) ? m : null;
      } },
    ] },
  { key: 'm-menu-link', group: 'Mobile (390)', title: 'Mobile menu link',
    desc: 'An "Explore" link inside the opened mobile menu — big text rows.',
    sel: 'a.nav-link', find: async (p) => {
      const b = p.locator('button.closed:visible').first();
      if (!(await p.locator('section.right-group').filter({ hasText: /plans/i }).count())) {
        if (await b.count()) { await b.click({ timeout: 4000 }).catch(() => {}); await p.waitForTimeout(1400); }
      }
      return p.locator('a.nav-link:visible').filter({ hasText: /^explore$/i }).first();
    }, states: ['default'] },
];

const GROUPS = {
  shell: { page: 'explore', specs: SHELL },
  home: { page: 'home', specs: HOME_SPECS },
  explore: { page: 'explore', specs: EXPLORE },
  plans: { page: 'plans', specs: PLANS },
  service: { page: 'service', specs: DETAIL },
  applet: { page: 'applet', specs: [...APPLET] },
  'applet-detail': { page: 'applet', specs: DETAIL },
  connect: { page: 'connect', specs: DETAIL },
  solutions: { page: 'solutions-productivity', specs: SOLUTIONS },
  misc: { page: 'mcp', specs: MISC },
  legal: { page: 'terms', specs: LEGAL },
  mobile: { page: 'mobile', mobile: true, specs: MOBILE },
};

// The group that owns each spec key's bare name: the last group listing it.
const KEY_OWNER = {};
for (const [gk, gg] of Object.entries(GROUPS)) for (const sp of gg.specs) KEY_OWNER[sp.key] = gk;

// ---------- runner ----------

const b = await chromium.launch();
context = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
await patch(context);
const mobCtx = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' });
await patch(mobCtx);

const wanted = process.argv.slice(2);
out._meta.read = new Date().toLocaleDateString('en-CA');
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); IFTTT paints one theme — dark heroes are painted sections, not a switched theme';
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
  const url = URLS[g.page];
  log('open', key, g.mobile ? '(mobile)' : '', url);
  if (!(await open(page, url, { wait: 7000 }))) { log('  group skipped: the page never loaded'); await page.close().catch(() => {}); continue; }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  // the readable sheets' transition declarations, for measurements.md
  out._meta.sheets[g.page] = await page.evaluate(() => {
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

  for (let spec of g.specs) {
    // One key per page, fixed by GROUPS order: a spec key listed by several
    // groups belongs to the LAST group that lists it (connect, which is what
    // the committed readings and the builder's bare keys are), and every other
    // group writes it under its own prefix (service-back-button). The names
    // never depend on what an earlier run saved. (2026-11 audit; not run.)
    if (KEY_OWNER[spec.key] !== key) spec = { ...spec, key: `${key}-${spec.key}` };
    const comp = out.components[spec.key] ??= {};
    comp.group = spec.group;
    comp.title = spec.title;
    comp.desc = spec.desc;
    comp.selector = spec.sel;
    comp.page = g.page;
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
        let readLoc = loc;
        if (st === 'hover') { await hover(readLoc); viaText = via.hover; }
        else if (st === 'focus-visible') { const f = await kbFocus(readLoc); viaText = f && (f.held || f.ring) ? via['focus-visible'] : 'focus failed'; }
        else if (st === 'focused') { await readLoc.click({ timeout: 3000 }).catch(() => readLoc.evaluate((el) => el.focus())); await page.waitForTimeout(400); viaText = via.focused; }
        else if (st === 'pressed') { pressed = await pressOn(readLoc); viaText = via.pressed; }
        else if (st && typeof st === 'object' && st.fn) { const alt = await st.fn(readLoc); if (alt && typeof alt.count === 'function' && await alt.count()) readLoc = alt; viaText = st.via || 'reached by the component\'s own UI toggle'; }
        else if (typeof st === 'function') { await st(readLoc); viaText = 'reached by the component\'s own UI toggle'; }
        await centre(readLoc).catch(() => {});
        const v = await styleOf(readLoc);
        v.via = viaText;
        v.crop = await crop(page, readLoc, `${spec.key}-${name}`).catch((e) => { log('  crop failed', spec.key, name, e.message.split('\n')[0]); return undefined; });
        v.run = new Date().toISOString();
        comp.states[name] = v;
        log(' ', spec.key, name, 'ok');
        // Put the control back only after this state's reading is stored, so a
        // restore cannot overwrite the changed state with the resting one.
        if (st && typeof st === 'object' && st.restore) await st.restore(loc);
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
        // If a spec opened the share modal or the mobile menu, close it so
        // the next spec reads the resting page.
        if (await page.locator('div.share-modal:visible, div.modal:visible').count()) await closeShareModal().catch(() => {});
        if (await page.locator('body.mobile-menu-opened').count()) {
          const x = page.locator('header button:visible, .mobile-menu button:visible, [class*="close"]:visible').first();
          if (await x.count()) await x.click({ timeout: 3000 }).catch(() => {});
          await page.waitForTimeout(600);
        }
      }
    }
    save();
  }
  await page.close();
}
await b.close();
log('done ->', OUT);
