// Measures cakeequity.com's public components in every state reachable without
// signing in, buying or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing feature blog demo login mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// cakeequity.com is a Webflow marketing build (cakester.shared.*.min.css, stable
// semantic classes); the only dark surface is the Cake-MCP section band inside
// the light page. The login page is Kinde's hosted auth widget on
// authentication.cakeequity.com (app.cakeequity.com/login redirects there):
// measured as a surface, never filled or submitted. Nothing is sent, bought or
// signed into: the only presses are local UI toggles — the Product mega-nav
// hover, the FAQ accordion and the mobile menu. The Chatbase assistant widget
// is hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing', feature: '/features/cap-table', blog: '/blog', demo: '/demo-request' };
let page, cdp, current, currentUrl, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes the edge gates this run: components last measured on them keep their
// earlier readings instead of being pruned below (a blocked pass must never
// erase evidence).
const failedPages = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied|unusual activity from your computer network|not a robot|you have been blocked|unable to access/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000, promo = 'close', url = null } = {}) {
  current = key;
  currentUrl = url || BASE + URLS[key];  // login and mobile pass their own url; no URLS entry
  // Close the previous page's context before opening the next: leaving them
  // alive keeps every captured page (and its animations) running in the
  // background for the rest of the run.
  if (liveCtx) { await liveCtx.close().catch(() => {}); liveCtx = null; }
  const b = context.browser();
  const ctx = liveCtx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  await open(page, currentUrl, { wait, promo });
  if (await blocked()) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  return true;
}

// Fixed/sticky chrome with paint order: the z-index map of the page's bars and
// overlays. Recorded per page into _meta.chrome.
async function chrome(key) {
  const z = await page.evaluate(() => {
    const els = [...document.querySelectorAll('body *')];
    const seen = [];
    for (const el of els) {
      const cs = getComputedStyle(el);
      if (cs.position !== 'fixed' && cs.position !== 'sticky') continue;
      const r = el.getBoundingClientRect();
      if (r.width < 40 || r.height < 10) continue;
      seen.push({ node: el.tagName.toLowerCase() + '.' + String(el.className).split(' ')[0].slice(0, 60), z: cs.zIndex, pos: cs.position, rect: `${r.width | 0}x${r.height | 0}@${r.x | 0},${r.y | 0}`, text: (el.innerText || '').slice(0, 40).replace(/\n/g, '|') });
    }
    return seen.sort((a, b) => (parseInt(b.z) || 0) - (parseInt(a.z) || 0)).slice(0, 20);
  }).catch(() => []);
  out._meta.chrome ??= {};
  out._meta.chrome[key] = z;
}

async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  const vw = page.viewportSize()?.width ?? 1440;
  await page.mouse.move(vw - 2, 2);
  await page.waitForTimeout(250);
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  let ok = await loc.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
  let how = 'Shift+Tab, Tab';
  if (!ok) {
    await page.keyboard.press('Shift');
    await loc.evaluate((el) => el.focus());
    ok = await loc.evaluate((el) => document.activeElement === el);
    how = 'keydown then focus()';
  }
  await page.waitForTimeout(350);
  return ok ? how : 'focus failed';
}

async function forcePseudo(loc, classes) {
  await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
  await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
  const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
  const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: classes });
  await page.waitForTimeout(400);
  return async () => { await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {}); };
}

function comp(key, meta) {
  const c = (out.components[key] ??= { states: {} });
  Object.assign(c, { page: current, run, url: currentUrl }, meta);
  touched.add(key);
  c.states ??= {};
  return c;
}

async function measure(key, state, target, opts = {}) {
  const loc = target.filter({ visible: true }).first();
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    let file;
    if (opts.crop !== false) {
      try {
        file = await crop(page, (opts.cropLoc || loc).filter({ visible: true }).first(), `${key}-${state}`, opts.pad ?? 8);
      } catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    c.states[state] = { ...s, crop: file, via: opts.via };
    if (opts.extra) c.states[state].extra = await opts.extra(loc);
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    c.states[state] = { error: String(e.message || e).slice(0, 200) };
    log('  !', key, state, String(e.message).slice(0, 120));
  }
}

async function S(key, target, list, meta = {}, opts = {}) {
  const prev = out.components[key];
  const keep = prev && Object.keys(prev.states || {}).length ? { page: prev.page, run: prev.run, url: prev.url } : null;
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  if (!listed.has(key)) listed.set(key, new Set());
  for (const st of list) listed.get(key).add(st);
  delete out.components[key].missing;
  if (opts.open) { await reset(); try { await opts.open(); } catch (e) { log('  ! open failed', key, String(e.message).slice(0, 80)); } }
  const loc = target.filter({ visible: true }).first();
  if (!(await loc.count())) {
    const has = Object.keys(out.components[key].states || {}).length > 0;
    log('  ! missing', key, has ? '(earlier states kept)' : '');
    // Keep earlier evidence under its own provenance: the states stay but the
    // entry keeps its original page/run/url and records the miss, so a re-run
    // never republishes old readings under a new date.
    if (!has) out.components[key].missing = true;
    else { Object.assign(out.components[key], keep); out.components[key].recaptureMissed = run; }
    return;
  }
  for (const st of list) {
    let undo, via;
    try {
      if (!opts.noReset) await reset();
      if (!opts.noScroll) await centre(loc);
      if (opts.before?.[st]) via = await opts.before[st](loc);
      if (st === 'hover') {
        await (opts.hoverLoc || loc).filter({ visible: true }).first().hover({ timeout: 5000 }).catch(() => (opts.hoverLoc || loc).filter({ visible: true }).first().hover({ timeout: 5000, force: true }));
        await page.waitForTimeout(450);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus((opts.focusLoc || loc).filter({ visible: true }).first());
      } else if (st === 'pressed') {
        undo = await forcePseudo((opts.pressLoc || loc).filter({ visible: true }).first(), ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        const fld = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await fld.click({ timeout: 4000 }).catch(() => fld.evaluate((el) => el.focus()));
        await page.waitForTimeout(400);
        via = 'clicked into the field';
      } else if (st === 'filled') {
        const f = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await f.click({ timeout: 4000 });
        await page.keyboard.type(opts.fillText || 'name@example.com', { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || 'name@example.com'}", then deleted; nothing sent`;
      } else if (st === 'opened') {
        if (opts.noToggle) via = 'held open by an earlier toggle';
        else { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle'; }
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      out.components[key].states[st] = { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  await reset();
}

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again|start free|book a demo)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

async function sheetsFor(key) {
  const res = await page.evaluate(() => {
    const transitions = [];
    const walk = (rules) => {
      for (const r of rules) {
        if (r.cssRules && !r.selectorText) { walk(r.cssRules); continue; }
        if (!r.style) continue;
        const t = r.style.getPropertyValue('transition');
        const a = r.style.getPropertyValue('animation');
        if (t || a) transitions.push({ selector: (r.selectorText || '').slice(0, 160), transition: t, animation: a });
      }
    };
    for (const ss of document.styleSheets) { try { walk(ss.cssRules); } catch { /* cross-origin */ } }
    return transitions;
  });
  out._meta.sheets ??= {};
  out._meta.sheets[key] = res;
}

// Whether the page paints a different transition under prefers-reduced-motion:
// the same component re-read in a context with reduce on.
async function reducedMotion(key, sel) {
  out._meta.reducedMotion ??= {};
  try {
    const b = context.browser();
    const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', reducedMotion: 'reduce' });
    await patch(ctx);
    const p = await ctx.newPage();
    await p.goto(BASE + URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(7000);
    await closePromo(p);
    const v = await p.evaluate((s) => {
      const el = document.querySelector(s);
      if (!el) return null;
      const cs = getComputedStyle(el);
      return { transition: cs.transition, animation: cs.animation, scrollBehavior: getComputedStyle(document.documentElement).scrollBehavior };
    }, sel).catch(() => null);
    out._meta.reducedMotion[key] = { selector: sel, reduce: v };
    await ctx.close();
  } catch (e) { out._meta.reducedMotion[key] = { selector: sel, error: String(e).slice(0, 120) }; }
}

const G = {
  shell: 'Shell and navigation', home: 'Home', pricing: 'Pricing',
  blog: 'Blog and demo', login: 'Login (Kinde hosted auth)', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('header', q('.navbar').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The fixed marketing navbar: wordmark, Product/Solutions/Resources/Customers mega-nav, Pricing link, Login, Book-a-demo and Get-started-free.', sel: 'div.navbar' }, { noScroll: true });
  await S('logo', q('.navbar-logo').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The cake. wordmark anchor.', sel: 'a.navbar-logo' }, { noScroll: true });
  await S('nav-trigger', q('.nav-menu-dropdown .w-dropdown-toggle').filter({ hasText: /^\s*Product\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav trigger', desc: 'The Product mega-nav toggle; opens its panel on hover (Webflow w-dropdown), never followed.', sel: '.nav-menu-dropdown .w-dropdown-toggle' }, { noScroll: true });
  await S('nav-link', q('.navbar-menu a, .navbar a').filter({ hasText: /^\s*Pricing\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'The plain Pricing header link.', sel: 'header Pricing link' }, { noScroll: true });
  await S('nav-login', q('.navbar a, .navbar .primary-nav-button').filter({ hasText: /^\s*Login\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Login link', desc: 'The Login header action (links to app.cakeequity.com); measured never followed.', sel: '.primary-nav-button' }, { noScroll: true });
  await S('nav-demo', q('.navbar a').filter({ hasText: /^\s*Book a demo\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Book-a-demo button', desc: 'The secondary header action (primary-button-nav light-grey).', sel: 'a.primary-button-nav.light-grey' }, { noScroll: true });
  await S('nav-cta', q('.navbar a').filter({ hasText: /^\s*Get started free\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav CTA', desc: 'The Get-started-free header action; links to the app signup, measured never followed.', sel: 'a.primary-button-nav' }, { noScroll: true });
  // The mega-nav opens on hover of its own trigger; keep the mouse put
  // (noReset) so the panel is still painted when it is read and cropped.
  try {
    const t = q('.nav-menu-dropdown .w-dropdown-toggle').filter({ hasText: /^\s*Product\s*$/ }).filter({ visible: true }).first();
    if (await t.count()) { await t.hover({ timeout: 5000 }); await page.waitForTimeout(1400); }
  } catch (e) { log('  ! mega-nav hover failed', String(e.message).split('\n')[0]); }
  await S('nav-dropdown', q('.nav-dropdown.w-dropdown-list.w--open').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mega-nav panel', desc: 'The Product mega-menu panel, opened by hovering its own trigger.', sel: '.nav-dropdown.w-dropdown-list.w--open' }, { noScroll: true, noReset: true });
  await S('menu-link', q('.nav-dropdown.w--open a').filter({ hasText: /\S/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Menu link', desc: 'A feature link inside the opened mega-nav.', sel: 'mega-nav link' }, { noScroll: true, noReset: true, open: async () => {
    const t = q('.nav-menu-dropdown .w-dropdown-toggle').filter({ hasText: /^\s*Product\s*$/ }).filter({ visible: true }).first();
    if (await t.count()) { await t.hover({ timeout: 5000 }); await page.waitForTimeout(1400); }
  } });
  const h = G.home;
  await S('announce-pill', q('a.pm-mig-chip-2, a').filter({ hasText: /managed migration works/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Announcement pill', desc: 'The Pulley announcement chip above the hero (links to the managed-migration section anchor).', sel: 'a.pm-mig-chip-2' }, { noScroll: true });
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The "The equity platform for growing startups" display headline in Exposure.', sel: 'h1' }, { noScroll: true });
  await S('hero-sub', await domFind(page, /cap table accuracy|compliance readiness/i, { sel: 'div.body-medium, .hp-new-hero div, p', tag: 'hero-sub' }), ['default'], { group: h, title: 'Hero copy', desc: 'The lede under the headline (body-medium).', sel: 'hero lede' });
  await S('hero-cta', q('a, button').filter({ hasText: /^\s*Get started\s*$/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The hero Get-started action (primary-button-v2); links to the app signup, measured never followed.', sel: 'a.primary-button-v2' });
  await S('hero-demo', q('a.transparent-button-v2').filter({ hasText: /Book a demo/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero secondary', desc: 'The hero Book-a-demo ghost button (transparent-button-v2).', sel: 'a.transparent-button-v2' });
  await S('eyebrow', q('.eyebrow-2.plum, .eyebrow').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section eyebrow', desc: 'A small-caps section label (eyebrow-2 plum).', sel: '.eyebrow-2.plum' });
  await S('section-h2', q('h2').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A 44px section heading.', sel: 'h2' });
  await S('dark-section', q('.hp26-aidark-2, section[class*="aidark" i]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Dark band', desc: 'The Cake-MCP section: the one dark surface on the page (hp26-aidark-2).', sel: 'section.hp26-aidark-2' });
  await S('story-card', q('.story-card').filter({ visible: true }).first(), B4, { group: h, title: 'Story card', desc: 'A customer-quote card in the stories section.', sel: '.story-card' });
  await S('faq-item', q('.faq-item-card').filter({ visible: true }).first(), ['default', 'opened'], { group: h, title: 'FAQ item', desc: 'A Frequently-Asked accordion card; toggled open by clicking its question wrap (a local UI toggle revealing the answer).', sel: '.faq-item-card' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing', { wait: 12000 }))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('pricing-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', desc: 'The "Growth-friendly pricing, no complexity" display heading.', sel: 'h1 on /pricing' }, { noScroll: true });
  await S('country-select', q('#countrySelect, select').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Country select', desc: 'The region <select> (United States/Canada/Australia/UK/Singapore/New Zealand) that re-prices the plans; geo-defaulted to Singapore in this capture. Tapped into focus, never changed.', sel: '#countrySelect' }, { noScroll: true });
  await S('billing-toggle', q('label.w-checkbox').filter({ hasText: /Yearly|Quarterly/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Billing toggle', desc: 'The Yearly/Quarterly save switch (label.w-checkbox over #cycleCheckbox); a local UI toggle measured at rest — clicking it re-prices client-side, captured in screenshots only.', sel: 'label.w-checkbox.ms-switch-wrap' });
  await S('calc-field', q('.pp-hidden-fields input, input[name="field"], input[type="number"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Calculator field', desc: 'The estimate inputs of the pricing form — they all sit in .pp-hidden-fields (display:none) behind the country select, so nothing paints; recorded missing.', sel: 'calculator input' });
  await S('plan-card', q('.pricing-cards.pop').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan card', desc: 'The Growth plan card (.pricing-cards.pop, the featured tier).', sel: '.pricing-cards.pop' });
  await S('plan-price', q('.pricing-cards.pop .price-card-rate, .price-card-rate').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan price', desc: 'A plan card\'s price figure (S$1,128 annually for the detected region).', sel: '.price-card-rate' });
  await S('plan-badge', q('.most-popular-pill').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan badge', desc: 'The "Most popular" pill on the featured plan card.', sel: '.most-popular-pill' });
  await S('plan-cta', q('.pricing-cards.pop a.w-button, a.paid-button').filter({ hasText: /Start free/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'A plan Start-free action; links to the app signup, measured never followed.', sel: 'a.primary-button-v2.paid-button' });
  save();
}

async function feature() {
  if (!(await newPage('feature'))) return;
  const g = G.blog;
  await S('feature-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Feature headline', desc: 'The /features/cap-table display heading; one of ~25 sibling feature pages on the same template.', sel: 'h1 on /features/cap-table' }, { noScroll: true });
  save();
}

async function blog() {
  if (!(await newPage('blog'))) return;
  const g = G.blog;
  await S('blog-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Blog title', desc: 'The "Cake blog" heading.', sel: 'h1 on /blog' }, { noScroll: true });
  await S('collection-card', q('.collection-card').filter({ visible: true }).first(), B4, { group: g, title: 'Article card', desc: 'A blog collection card (the featured post).', sel: '.collection-card' });
  save();
}

async function demo() {
  if (!(await newPage('demo', { wait: 10000 }))) return;
  const g = G.blog;
  await S('demo-h1', q('h1, .discovery-why').filter({ visible: true }).first(), ['default'], { group: g, title: 'Demo title', desc: 'The /demo-request heading.', sel: 'h1 on /demo-request' }, { noScroll: true });
  await S('demo-form', q('.form-grid-embed, .hs-form-frame').filter({ visible: true }).first(), ['default'], { group: g, title: 'Demo form embed', desc: 'The HubSpot form region (a cross-origin hsforms.net iframe; its inner fields are third-party paint, documented as a boundary).', sel: '.form-grid-embed' });
  save();
}

async function login() {
  // The auth surface lives on another origin: app.cakeequity.com/login 302s to
  // Kinde's hosted UI on authentication.cakeequity.com. Surface only.
  if (!(await newPage('login', { url: 'https://app.cakeequity.com/login/', wait: 11000 }))) return;
  const g = G.login;
  await S('login-card', q('article.kinde-layout-page-card, .kinde-layout-widget').filter({ visible: true }).first(), ['default'], { group: g, title: 'Login card', desc: 'The Kinde hosted-auth card (Welcome back): email field, Continue, Google and LinkedIn OAuth.', sel: 'article.kinde-layout-page-card' });
  await S('login-title', q('h1.kinde-heading, .kinde-heading').filter({ visible: true }).first(), ['default'], { group: g, title: 'Login title', desc: 'The "Welcome back" auth heading.', sel: 'h1.kinde-heading' });
  await S('login-field', q('input[type="email"], .kinde-control-select-text').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Email field', desc: 'The auth email input; tapped into focus, never typed into or submitted.', sel: 'input.kinde-control-select-text' });
  await S('login-cta', q('button.kinde-button-variant-primary').filter({ visible: true }).first(), B4, { group: g, title: 'Continue button', desc: 'The primary Continue action (a submit button — measured, never pressed for real).', sel: 'button.kinde-button-variant-primary' });
  await S('login-oauth', q('button.kinde-button-variant-secondary').filter({ visible: true }).first(), B4, { group: g, title: 'OAuth button', desc: 'A secondary Continue-with provider button (Google/LinkedIn).', sel: 'button.kinde-button-variant-secondary' });
  await S('login-link', q('a.kinde-text-link').filter({ visible: true }).first(), B4, { group: g, title: 'Create-one link', desc: 'The "Create one" signup link under the OAuth buttons.', sel: 'a.kinde-text-link' });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 6000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1500);
  await S('footer', q('.footer-section, footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The footer-section: office address, link columns, socials, legal.', sel: '.footer-section' }, { noScroll: true });
  await S('footer-link', q('.footer-section a, footer a').filter({ hasText: /\S/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', sel: 'footer a' }, { noScroll: true });
  await S('social-icon', q('.footer-section a[href*="linkedin"], .footer-section a[href*="instagram"], .footer-section a[href*="twitter"], footer a[href*="linkedin"], footer a[href*="x.com"]').filter({ visible: true }).first(), B4, { group: g, title: 'Social link', desc: 'A social link in the footer.', sel: 'footer social a' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('.navbar').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', desc: 'The navbar at 390 — the page forces a ~745px layout viewport (a .comparison-grid min-width:700px plus navbar chrome), so the hamburger sits outside the 390 visual viewport: the shots record what a phone actually paints.', sel: '.navbar at 390' }, { noScroll: true });
  await S('m-menu-button', q('.w-nav-button').filter({ visible: true }).first(), ['default'], { group: g, title: 'Menu button', desc: 'The hamburger (menu-button w-nav-button); painted at x~660 of the forced 745 layout, off the 390 visual viewport.', sel: '.w-nav-button' }, { noScroll: true });
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', sel: 'h1 at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844 requested; the page forces a ~745px layout viewport — see m-header); every surface paints light';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, feature, blog, demo, login, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that actually transitions (a button),
  // so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', '.primary-button-v2');
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // An untouched entry is pruned only when its page was not blocked this
    // run: an edge-blocked route keeps its earlier readings under their
    // original provenance instead of being erased and republished.
    if (!touched.has(key) && !pages.length && !failedPages.has(c.page)) { delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close();
}
console.log('components-computed.json:', Object.keys(out.components).length, 'components');
