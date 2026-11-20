// Measures intercom.com's public components in every state reachable
// without signing in, starting a trial, buying or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing contact-sales help changes blog mobile. Writes
// raw/components-computed.json (merged) and one crop per component and state
// into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// intercom.com is a Next.js + Tailwind v4 marketing site (body.theme-light,
// one theme) plus two older surfaces: the help center (/help/en/) and the
// changelog (/changes/en, body.header__lite). Headless Chromium loads it
// clean. Selectors ride the semantic hooks (header.shared-header, .input,
// .select, .label, .checkbox-label, .text-heading-*, .text-label-*) and text
// roles. The only presses are local UI toggles (the billing switch, a FAQ
// accordion, a select's own listbox, the mobile menu button); Start free
// trial, Log in, Next and every submit path are measured but never pressed.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, patch, open, closePromo, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/', pricing: '/pricing', 'contact-sales': '/contact-sales',
  help: '/help/en/', changes: '/changes/en', blog: '/blog', helpdesk: '/helpdesk',
};
let page, cdp, current, view, context, run, ctx0;
const touched = new Set();
const listed = new Map();
// Page+viewport visits that actually loaded this run (not blocked): readings
// may only be pruned for components of one of these.
const opened = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied/i.test(t) || /just a moment/i.test(document.title) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000, dsf } = {}) {
  current = key;
  view = mobile ? 'mobile' : 'desktop';
  const b = context.browser();
  // Close the previous context before opening another page. Overwriting
  // `page` alone left earlier pages' scripts and animations running.
  if (context && context !== ctx0) await context.close().catch(() => {});
  const ctx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: dsf ?? 2, userAgent: UA, locale: 'en-US' });
  context = ctx;
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  const loaded = await open(page, BASE + URLS[key], { wait });
  if (!loaded || await blocked()) { log('  BLOCKED', key); await page.close(); await ctx.close(); if (context === ctx) context = ctx0; return false; }
  opened.add(key + '|' + view);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  await closePromo(page);
  return true;
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
  Object.assign(c, { page: current, view, run, url: URLS[current] && BASE + URLS[current] }, meta);
  touched.add(key);
  c.states ??= {};
  return c;
}

// The header (and most components) mount a 0x0 hidden variant before the
// painted one — a mobile or pre-hydration copy — so "first visible" is not
// enough: firstWide picks the first candidate that actually has a box.
async function firstWide(target, { minW = 4 } = {}) {
  const cands = target.filter({ visible: true });
  const n = Math.min(await cands.count(), 12);
  for (let i = 0; i < n; i++) {
    const l = cands.nth(i);
    const box = await l.boundingBox().catch(() => null);
    if (box && box.width >= minW && box.height >= minW) return l;
  }
  return cands.first();
}

async function measure(key, state, target, opts = {}) {
  const loc = await firstWide(target, opts.firstWide);
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    const prev = c.states[state];
    let file;
    if (opts.crop !== false) {
      try {
        file = await crop(page, opts.cropLoc ? await firstWide(opts.cropLoc) : loc, `${key}-${state}`, opts.pad ?? 8);
      } catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    // A failed crop keeps the previous state's image link rather than
    // dropping it; the style reading is fresh, the crop is last good.
    c.states[state] = { ...s, crop: file ?? (prev && prev.crop), via: opts.via, run };
    if (opts.extra) c.states[state].extra = await opts.extra(loc);
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    // A failed state capture must not erase a previous reading: keep it under
    // its own provenance and record the error beside it.
    const prev = c.states[state];
    c.states[state] = prev && !prev.error
      ? { ...prev, recaptureError: String(e.message || e).slice(0, 200) }
      : { error: String(e.message || e).slice(0, 200) };
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
  delete out.components[key].recaptureMissed;
  if (opts.open) { await reset(); try { await opts.open(); } catch (e) { log('  ! open failed', key, String(e.message).slice(0, 80)); } }
  const loc = await firstWide(target, opts.firstWide);
  if (!(await loc.count()) || !((await loc.boundingBox().catch(() => null))?.width > 0)) {
    const has = Object.keys(out.components[key].states || {}).length > 0;
    log('  ! missing', key, has ? '(earlier states kept)' : '');
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
        // opts.open already opened the overlay. Clicking the measured node
        // again toggles it shut, so the reading lands on a hidden copy or a
        // different element that happens to match the locator.
        if (opts.open || opts.noToggle) via = 'menu held open by opts.open';
        else { await toggle(opts.toggleLoc || loc); await page.waitForTimeout(900); via = 'own toggle'; }
      } else via = via || 'at rest';
      if (opts.expect && !(await opts.expect(loc))) {
        throw new Error(`opened target is not the intended ${key}`);
      }
      await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      const prev = out.components[key].states[st];
      out.components[key].states[st] = prev && !prev.error
        ? { ...prev, recaptureError: String(e.message || e).slice(0, 200) }
        : { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  await reset();
}

// Clicks a UI toggle (billing switch, accordion, select listbox, mobile
// menu). Refuses a submit button and any control whose text names an action
// this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|sign ?up|save|apply|accept|reject|start|get started|claim|share|export|select|continue|book|request|next|contact|view demo|start free trial)$/i;
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

// Marks the first painted card-like element on the page: a bordered or
// filled container with a radius, inside main, that is not the nav or
// footer. `attr` marks it for the locator pass.
const markCard = async (attr, { hasText } = {}) => page.evaluate(([a, wantText]) => {
  const els = [...document.querySelectorAll('main div, main article, main section, body div[class*="rounded"]')];
  const cand = els.filter((e) => {
    const r = e.getBoundingClientRect();
    if (!(r.width > 220 && r.width < 900 && r.height > 90 && r.height < 700)) return false;
    const cs = getComputedStyle(e);
    const painted = cs.backgroundColor !== 'rgba(0, 0, 0, 0)' || parseFloat(cs.borderTopWidth) > 0 || cs.boxShadow !== 'none';
    const round = parseFloat(cs.borderTopLeftRadius) >= 4;
    return painted && round && (!wantText || (e.innerText || '').includes(wantText));
  });
  const leaf = cand.find((e) => !cand.some((o) => o !== e && e.contains(o))) || cand[0];
  if (!leaf) return false;
  leaf.setAttribute(a, '1');
  return true;
}, [attr, hasText || null]);

// Marks the first element matching a structural spec (run in the page) for
// the locator pass — for components whose shell is unpainted (the pricing
// plan columns) or reachable only by text. Serializable options only: the
// page's CSP can refuse new Function/eval.
const markEl = (attr, spec = {}) => page.evaluate(([a, s]) => {
  const leaf = [...document.querySelectorAll(s.sel || 'main div, main article, main section')].find((e) => {
    const r = e.getBoundingClientRect();
    if (!(r.width >= (s.minW ?? 0) && r.width <= (s.maxW ?? 1e5) && r.height >= (s.minH ?? 0) && r.height <= (s.maxH ?? 1e5))) return false;
    const t = (e.innerText || '').trim();
    if (s.startsWith && !t.startsWith(s.startsWith)) return false;
    if (s.hasText && !t.includes(s.hasText)) return false;
    return true;
  });
  if (!leaf) return false;
  leaf.setAttribute(a, '1');
  return true;
}, [attr, spec]);

const G = {
  shell: 'Shell and navigation', home: 'Home', pricing: 'Pricing', form: 'Contact sales form',
  help: 'Help center', changes: 'Changelog', blog: 'Blog', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  const g = G.shell;
  await S('promo-banner', q('header').locator('a[href*="fin.ai"], [class*="banner"]').filter({ hasText: /Fin/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Promo banner', desc: 'The announcement row at the very top of the shared header ("Introducing Fin 4 … Learn more"): real chrome, kept.', sel: 'header banner row' }, { noScroll: true });
  await S('header', q('header.shared-header'), ['default'], { group: g, title: 'Nav bar', desc: 'The shared site header (header.shared-header): Intercom logo, Product/Customers/Resources menu triggers, Pricing link, Log in, Contact sales, View demo and the black "Start free trial" button.', sel: 'header.shared-header' }, { noScroll: true });
  await S('logo', q('header a[href="/"]'), ['default'], { group: g, title: 'Logo', desc: 'The Intercom wordmark home anchor in the nav.', sel: 'header a[href="/"]' }, { noScroll: true });
  await S('nav-item', q('header button').filter({ hasText: /^Product$/ }), B4, { group: g, title: 'Nav menu trigger', desc: 'A mega-menu trigger in the nav ("Product"): 40px, radius 6, opens the nav panel.', sel: 'header button "Product"' }, { noScroll: true });
  await S('nav-link', q('header a').filter({ hasText: /^Pricing$/ }), B4, { group: g, title: 'Nav link', desc: 'A plain nav link ("Pricing"): 40px ghost row, radius 6.', sel: 'header a "Pricing"' }, { noScroll: true });
  await S('nav-login', q('header a[href*="sign_in"], header a[href*="/login"]'), B4, { group: g, title: 'Nav log in', desc: 'The "Log in" link to app.intercom.com; measured, never followed.', sel: 'header a[href*=sign_in]' }, { noScroll: true });
  await S('nav-cta', q('header a[href*="signup"]'), B4, { group: g, title: 'Nav CTA', desc: 'The black "Start free trial" button in the nav (--button-primary-* tokens, --button-radius 4px, height --button-height 40px); links to /signup, never followed.', sel: 'header a[href*=signup]' }, { noScroll: true });
  // The nav mega-menu, opened by its own Product trigger.
  // The first switch-card in the DOM is a hidden variant (opacity 0). Measure
  // the painted panel the Product trigger actually opens, and do not click it.
  await S('nav-menu', q('[class*="nav-panel"], [class*="switch-card"], header [class*="popover"]').filter({ visible: true }), ['opened'], { group: g, title: 'Nav mega-menu', desc: 'The panel the Product/Customers/Resources triggers open (shared-header-switch-card): a white card with the nav-panel border and a drop shadow.', sel: 'visible nav panel' }, { noScroll: true, noReset: true, open: async () => { const t = q('header button').filter({ hasText: /^Product$/ }); await t.hover().catch(() => {}); await page.waitForTimeout(700); if ((await t.getAttribute('aria-expanded').catch(() => null)) !== 'true') await t.click().catch(() => {}); await page.waitForTimeout(800); }, expect: async (loc) => loc.evaluate((el) => getComputedStyle(el).opacity !== '0' && el.getBoundingClientRect().width > 0 && /product|customers|resources|inbox|fin/i.test(el.innerText || '')) });
  const h = G.home;
  await S('hero-title', q('main h1, h1'), ['default'], { group: h, title: 'Hero title', desc: 'The home hero headline ("A complete system for AI and human customer service", text-heading-2: Saans, tight tracking).', sel: 'first visible h1' }, { noScroll: true });
  await S('eyebrow', q('main span.text-label-lg, main [class*="eyebrow"], main [class*="label"]'), ['default'], { group: h, title: 'Eyebrow label', desc: 'A small label over a section (text-label-lg: SaansMono-family uppercase micro type).', sel: 'span.text-label-lg' });
  await S('hero-cta', q('main a[href*="signup"]'), B4, { group: h, title: 'Hero CTA', desc: 'The black "Start free trial" button under the hero copy (--button-primary-*, --button-radius); links to /signup, never followed.', sel: 'main a[href*=signup]' });
  await S('hero-secondary', q('main a').filter({ hasText: /View demo|Take a tour|Learn more/i }), B4, { group: h, title: 'Hero secondary link', desc: 'The secondary action beside the hero CTA ("View demo" style link button).', sel: 'main a "View demo|Learn more"' });
  await S('section-title', q('main h2.text-heading-3, main h2'), ['default'], { group: h, title: 'Section title', desc: 'A display section heading in page flow (text-heading-3: Saans).', sel: 'h2.text-heading-3 first' });
  await S('feature-card', q('[data-m-card="1"]'), ['default', 'hover'], { group: h, title: 'Feature card', desc: 'A painted card on the home page (the first bordered/filled rounded container in main).', sel: 'first painted card in main' }, { open: async () => { await markCard('data-m-card'); } });
  await S('page-ground', q('body'), ['default'], { group: h, title: 'Page ground', desc: 'The body element: --body-bg = --color-cream under the current brand scope.', sel: 'document.body' }, { noScroll: true, crop: false });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  const g = G.pricing;
  await S('pricing-title', q('main h1, h1'), ['default'], { group: g, title: 'Pricing title', desc: '"Get Fin and Intercom for a single, fully integrated customer service stack" (text-heading-3).', sel: 'first visible h1' }, { noScroll: true });
  await S('billing-toggle', q('button').filter({ hasText: /^Billed annually$/ }), B4, { group: g, title: 'Billing toggle (selected)', desc: 'The selected half of the annual/monthly billing segmented control ("Billed annually": canvas fill, radius none). Local UI state, switched and switched back.', sel: 'button "Billed annually"' });
  await S('billing-toggle-off', q('button').filter({ hasText: /^Billed monthly$/ }), B4, { group: g, title: 'Billing toggle (unselected)', desc: 'The unselected half ("Billed monthly": transparent).', sel: 'button "Billed monthly"' });
  await S('promo-badge', q('button').filter({ hasText: /save 35%|save \d+%/i }), B4, { group: g, title: 'Promo badge button', desc: 'The helpdesk-blue tinted badge button on pricing ("New customers save 35%", bg-helpdesk/15, 2px radius).', sel: 'button "save 35%"' });
  await S('plan-card', q('[data-m-plan="1"]'), ['default'], { group: g, title: 'Plan card', desc: 'A pricing plan column (the Essential cell of the @container plan grid: unpainted itself, its plan name, "Includes Fin AI Agent" list and CTA inside).', sel: 'Essential @container cell' }, { open: async () => { await markEl('data-m-plan', { minW: 200, maxW: 500, minH: 300, startsWith: 'Essential' }); } });
  await S('faq-item', q('[class*="accordion"] button, button').filter({ hasText: /\?/ }).filter({ visible: true }).last(), ['default', 'opened'], { group: g, title: 'FAQ accordion item', desc: 'A question row in the pricing FAQ accordion; opened by its own press.', sel: 'last ? button' });
  save();
}

async function contact() {
  if (!(await newPage('contact-sales'))) return;
  const g = G.form;
  await S('form', q('form'), ['default'], { group: g, title: 'Contact sales form', desc: 'The first step of the contact-sales form (Business Email, company size select, opt-in checkbox, Next): measured at rest, never advanced or sent.', sel: 'form' }, { noScroll: true });
  await S('form-title', q('main h1, h1'), ['default'], { group: g, title: 'Form page title', desc: '"Discover the perfect fit with Intercom".', sel: 'first visible h1' }, { noScroll: true });
  await S('input-label', q('label.label'), ['default'], { group: g, title: 'Field label', desc: 'A field label (.label: "Business Email *").', sel: 'label.label' }, { noScroll: true });
  await S('input', q('input.input'), ['default', 'focused', 'filled'], { group: g, title: 'Text field', desc: 'The "Business email address" text input (.input: off-white fill, 2px radius, 40px). Sample text typed and deleted; nothing sent.', sel: 'input.input' });
  await S('select', q('button.select'), ['default', 'opened'], { group: g, title: 'Select (combobox)', desc: 'The "Your company size" select (button.select, same field styling as .input): its own listbox opened, nothing chosen.', sel: 'button.select' });
  await S('select-popup', q('.select-popup, [role="listbox"]').filter({ visible: true }), ['opened'], { group: g, title: 'Select popup', desc: 'The open listbox of the select (div.select-popup): options list, held open by the select entry.', sel: 'visible .select-popup' }, { noReset: true, open: async () => { const openBox = q('.select-popup, [role="listbox"]').filter({ visible: true }); if (!(await openBox.count())) { const s = await firstWide(q('button.select')); if (await s.count()) { await s.click().catch(() => {}); await page.waitForTimeout(800); } } }, expect: async (loc) => loc.evaluate((el) => { const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0 && /select-popup|listbox/i.test((el.className || '') + ' ' + (el.getAttribute('role') || '')); }) });
  await S('checkbox', q('label.checkbox-label'), ['default'], { group: g, title: 'Checkbox row', desc: 'The opt-in checkbox row (label.checkbox-label: "Get updates about upcoming events…"). Never ticked.', sel: 'label.checkbox-label' });
  await S('next-button', q('button').filter({ hasText: /^Next$/ }), B4, { group: g, title: 'Next button', desc: 'The form\'s black "Next" submit control (--button-primary-*, --button-radius, --button-height): measured with CDP-forced pseudo states only — never pressed, so the form was never advanced.', sel: 'button "Next"' });
  save();
}

async function help() {
  if (!(await newPage('help'))) return;
  const g = G.help;
  await S('help-header', q('header, [class*="header"]'), ['default'], { group: g, title: 'Help center header', desc: 'The help center\'s own header bar (a different surface from the marketing shell: white, no theme-light class).', sel: 'header' }, { noScroll: true });
  await S('help-search', q('input[type="search"], input[placeholder*="Search" i], button').filter({ hasText: /Search/i }), ['default', 'focused'], { group: g, title: 'Help search field', desc: 'The help center search ("Search for articles… ⌘K"): focused once, nothing typed.', sel: 'search input/button' }, { noScroll: true });
  await S('help-hero', q('main h1, h1'), ['default'], { group: g, title: 'Help center title', desc: '"Great service changes everything."', sel: 'first visible h1' }, { noScroll: true });
  await S('help-card', q('[data-m-helpcard="1"]'), ['default', 'hover'], { group: g, title: 'Help article card', desc: 'A category/article card on the help center home (first painted rounded container in main).', sel: 'marked card in main' }, { open: async () => { await markCard('data-m-helpcard'); } });
  await S('help-nav', q('nav, [class*="sidebar"], aside'), ['default'], { group: g, title: 'Docs nav', desc: 'The help center\'s expandable docs navigation tree (Overview, Getting Started, Operator, Fin AI Agent …).', sel: 'nav' });
  save();
}

async function changes() {
  if (!(await newPage('changes'))) return;
  const g = G.changes;
  await S('changes-title', q('main h1, h1'), ['default'], { group: g, title: 'Changelog title', desc: 'The changelog header (the older "header__lite" surface: #f3f5f7 ground, MediumLL-era type).', sel: 'first visible h1' }, { noScroll: true });
  await S('changes-entry', q('.newsfeed__newsitem, [data-m-change="1"]'), ['default'], { group: g, title: 'Changelog entry', desc: 'A release-note entry on /changes/en (div.paper.newsfeed__newsitem: white card, 4px radius on the #f3f5f7 header__lite ground).', sel: '.newsfeed__newsitem' }, { open: async () => { await markCard('data-m-change'); } });
  save();
}

async function blog() {
  if (!(await newPage('blog'))) return;
  const g = G.blog;
  await S('blog-title', q('main h1, h1'), ['default'], { group: g, title: 'Blog title', desc: '"Blog" (text-heading-*: Saans).', sel: 'first visible h1' }, { noScroll: true });
  await S('blog-card', q('main ul li, [data-m-blog="1"]'), ['default', 'hover'], { group: g, title: 'Blog article card', desc: 'An article row in the /blog index list (li.border-t over the white section).', sel: 'first article li in main' }, { open: async () => { await markCard('data-m-blog'); } });
  save();
}

async function footerGroup() {
  // its own page, so the footer readings name the page they come from (it
  // used to measure whatever page ran last; 2026-11 audit, not run since).
  // Opening home for the footer must not count as a home run: the prune at
  // the end deletes the readings of every page+view in `opened`.
  const homeRan = opened.has('home|desktop');
  if (!(await newPage('home'))) return;
  if (!homeRan) opened.delete('home|desktop');
  const g = G.footer;
  await S('footer', q('footer'), ['default'], { group: g, title: 'Footer', desc: 'The site footer: link columns, social icons, the locale selector and legal row on the page ground.', sel: 'footer' });
  await S('footer-link', q('footer a'), B4, { group: g, title: 'Footer link', desc: 'A footer link (Saans, muted); focus-visible carries the site outline.', sel: 'footer a first' });
  await S('locale-select', q('footer button, footer a').filter({ hasText: /English|Français|Deutsch/i }), B4, { group: g, title: 'Locale selector', desc: 'The footer language selector ("English").', sel: 'footer language control' });
  save();
}

async function mobileHome() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  await S('m-header', q('header.shared-header, header'), ['default'], { group: g, title: 'Mobile header', desc: 'The header at 390: logo + the menu button (the desktop nav unmounts).', sel: 'header' }, { noScroll: true });
  await S('m-menu-button', q('header button[aria-label*="navigation menu" i]'), B4, { group: g, title: 'Mobile menu button', desc: 'The hamburger toggle in the mobile header (aria-label "Open navigation menu"); opens the menu overlay.', sel: 'header menu button' }, { noScroll: true });
  await S('m-hero', q('main h1, h1'), ['default'], { group: g, title: 'Mobile hero', desc: 'The hero title at 390 (the responsive text-heading-*-mobile size).', sel: 'first visible h1' }, { noScroll: true });
  await S('m-menu-overlay', q('[role="dialog"].shared-header-portal, .shared-header-portal[role="dialog"]').filter({ visible: true }), ['opened'], { group: g, title: 'Mobile menu overlay', desc: 'The full-height navigation sheet the mobile menu button opens (div[role=dialog].shared-header-portal, off-white ground).', sel: '[role=dialog].shared-header-portal' }, { noScroll: true, noReset: true, open: async () => { const t = q('header button[aria-label*="navigation menu" i]'); if (await t.count() && (await t.getAttribute('aria-expanded').catch(() => null)) !== 'true') { await t.click().catch(() => {}); await page.waitForTimeout(1200); } }, expect: async (loc) => loc.evaluate((el) => el.classList.contains('shared-header-portal') && /product|customers|pricing|resources/i.test(el.innerText || '') && !/business email/i.test(el.innerText || '')) });
  save();
}

// ---------------------------------------------------------------- driver
const launched = await launch();
const browser = launched.browser;
ctx0 = launched.context;
context = ctx0;
run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.note = 'intercom.com signed-out public surface; headless Chromium at 1440x900 (mobile pass 390x844), computed styles from the live DOM. Nothing signed into, bought, trialled or submitted.';
const args = process.argv.slice(2);
const ALL = { home, pricing, 'contact-sales': contact, help, changes, blog, footer: footerGroup, mobile: mobileHome };
const list = args.length ? args : Object.keys(ALL);
for (const k of list) {
  if (!ALL[k]) { log('unknown page', k); continue; }
  await ALL[k]();
  save();
}
// Prune readings of components whose page+viewport ran this run but whose
// spec was dropped (a page that failed to open keeps its old evidence).
for (const [k, c] of Object.entries(out.components)) {
  if (touched.has(k)) continue;
  if (opened.has(c.page + '|' + (c.view || 'desktop'))) { log('prune', k); delete out.components[k]; }
}
save();
await browser.close();
log('done ->', OUT);
