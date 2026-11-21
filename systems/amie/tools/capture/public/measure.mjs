// Measures amie.so's public components in every state reachable without
// signing in, downloading or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing download contact mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// amie.so is a Tailwind + Radix build in one light theme; components are
// found by role, aria-label or stable text. Nothing is sent, downloaded or
// signed into: the only presses are local UI toggles — the Features flyout,
// the billing toggle, a pricing FAQ and the mobile menu. "Get started",
// "Login" and the plan buttons are measured in all states except followed or
// pressed for real.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing', download: '/download', contact: '/contact' };
let page, cdp, current, context, run;
const touched = new Set();
const listed = new Map();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000 } = {}) {
  current = key;
  const b = context.browser();
  const ctx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '');
  await open(page, BASE + URLS[key], { wait });
  if (await blocked()) { log('  BLOCKED', key); await page.close(); await ctx.close(); return false; }
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
  Object.assign(c, { page: current, run, url: URLS[current] && BASE + URLS[current] }, meta);
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
        if (opts.noToggle) via = 'flyout held open by opts.open';
        else { await toggle(loc); await page.waitForTimeout(900); via = 'own toggle'; }
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

// Clicks a UI toggle (flyout, billing, accordion, menu). Refuses a submit
// button and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|sign up|save|apply|accept|reject|start|get started|claim|share|export|select)$/i;
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

const G = {
  shell: 'Shell and navigation', hero: 'Home', pricing: 'Pricing',
  download: 'Download', contact: 'Contact', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  const g = G.shell;
  await S('header', q('header, nav').first(), ['default'], { group: g, title: 'Header', desc: 'The floating bar: logo, Features flyout, Pricing, Login, Get started.', sel: 'header/nav' }, { noScroll: true });
  await S('logo', q('header a, nav a').first(), ['default'], { group: g, title: 'Logo', sel: 'header a' }, { noScroll: true });
  const features = q('button').filter({ hasText: /^Features$/ }).first();
  await S('nav-flyout-button', features, B4, { group: g, title: 'Nav flyout button', desc: 'A Radix dropdown trigger; opens the Features panel.', sel: 'button:has-text("Features")' }, { noScroll: true });
  // The opened Radix panel mounts under the header's navigation-menu viewport;
  // crop that container so the crop actually holds the panel, not just the button.
  // The opened Radix panel mounts a navigation-menu viewport (it is not a
  // descendant of <header>, so no header qualifier on the selector).
  const flyoutPanel = q('[class*="navigation-menu-viewport" i], [data-radix-navigation-menu-viewport]').filter({ visible: true }).first();
  await S('nav-flyout-open', features, ['opened'], { group: g, title: 'Features flyout, open', desc: 'The Features button after its own toggle; the crop is the opened panel.', sel: 'button:has-text("Features")' }, { noScroll: true, cropLoc: flyoutPanel });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('nav-link', q('header a, nav a').filter({ hasText: /^Pricing$/ }), B4, { group: g, title: 'Nav link', sel: 'a:has-text("Pricing")' }, { noScroll: true });
  await S('nav-login', q('header a, nav a').filter({ hasText: /^Login$/ }), B4, { group: g, title: 'Login link', desc: 'The secondary nav link. Measured, never followed.', sel: 'a:has-text("Login")' }, { noScroll: true });
  await S('nav-cta', q('header a, nav a').filter({ hasText: /^Get started$/ }), B4, { group: g, title: 'Nav CTA', desc: 'The small blue Get started. Measured, never followed.', sel: 'a:has-text("Get started")' }, { noScroll: true });

  const h = G.hero;
  await S('hero-title', q('h1').first(), ['default'], { group: h, title: 'Hero title', sel: 'h1' }, { noScroll: true });
  await S('changelog-pill', q('a').filter({ hasText: /new|cpu|recorder|better/i }).filter({ hasText: /:/ }).first(), B4, { group: h, title: 'Changelog pill', desc: 'The "what\'s new" link under the hero.', sel: 'a:has-text(":")' }, { noScroll: true });
  await S('cta-primary', q('a,button').filter({ hasText: /^Get started$/ }).last(), B4, { group: h, title: 'Primary CTA', desc: 'The hero blue Get started. Measured, never followed.', sel: 'a:has-text("Get started")' });
  await S('cta-secondary', q('button,a').filter({ hasText: /^Download$/ }).first(), B4, { group: h, title: 'Secondary CTA', desc: 'The ghost Download beside it. Measured, never pressed.', sel: ':has-text("Download")' });
  const feat = q('h2, h3').filter({ hasText: /\w{4,}/ }).filter({ visible: true }).nth(1);
  await S('section-title', feat, ['default'], { group: h, title: 'Section title', sel: 'h2/h3 below the hero' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  const g = G.pricing;
  await S('pricing-title', q('h1').first(), ['default'], { group: g, title: 'Pricing title', sel: 'h1' }, { noScroll: true });
  await S('plan-cta', q('button, a').filter({ hasText: /trial/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Trial button', desc: '"Start 7 day free trial": the black plan CTA. Measured, never pressed.', sel: 'button:has-text("trial")' });
  const card = q('button, a').filter({ hasText: /trial/i }).filter({ visible: true }).first().locator('xpath=ancestor::*[contains(@class,"rounded") or contains(@class,"card") or contains(@class,"border")][1]');
  await S('plan-card', card, ['default'], { group: g, title: 'Plan card', sel: 'card ancestor of trial button' });
  await S('plan-select', q('button').filter({ hasText: /^Select$/ }).first(), B4, { group: g, title: 'Select button', desc: 'The white plan row action. Measured, never pressed.', sel: 'button:has-text("Select")' });
  const monthly = q('button').filter({ hasText: /^Bill monthly$/ }).first();
  const yearly = q('button').filter({ hasText: /^Bill yearly$/ }).first();
  await S('billing-monthly', monthly, B4, { group: g, title: 'Billing toggle, monthly', sel: 'button:has-text("Bill monthly")' });
  await S('billing-yearly', yearly, B4, { group: g, title: 'Billing toggle, yearly', sel: 'button:has-text("Bill yearly")' });
  await S('billing-yearly-on', yearly, ['opened'], { group: g, title: 'Billing toggle, yearly on', desc: 'The yearly side after its own toggle; plan prices flip and the trial button is re-rendered.', sel: 'button:has-text("Bill yearly")' });
  const faq = q('main button, section button').filter({ hasText: /\?/ }).filter({ visible: true }).first();
  await S('faq-question', faq, B4, { group: g, title: 'FAQ accordion button', sel: 'button[aria-expanded]' });
  await S('faq-open', faq, ['opened'], { group: g, title: 'FAQ accordion, open', desc: 'The same item after its own toggle.', sel: 'button[aria-expanded]' });
  await page.keyboard.press('Escape'); await page.waitForTimeout(400);
  save();
}

async function download() {
  if (!(await newPage('download'))) return;
  const g = G.download;
  await S('download-title', q('h1, h2').first(), ['default'], { group: g, title: 'Download title', sel: 'h1' }, { noScroll: true });
  const dl = q('a,button').filter({ hasText: /download|mac|ios|iphone/i }).filter({ visible: true }).first();
  await S('download-button', dl, B4, { group: g, title: 'Download button', desc: 'The app download action. Measured, never pressed.', sel: 'a/button:has-text("Download")' });
  save();
}

async function contact() {
  if (!(await newPage('contact'))) return;
  const g = G.contact;
  await S('contact-title', q('h1, h2').first(), ['default'], { group: g, title: 'Contact title', sel: 'h1' }, { noScroll: true });
  const mail = q('a[href^="mailto:"], a').filter({ hasText: /@|email|contact/i }).filter({ visible: true }).first();
  await S('contact-link', mail, B4, { group: g, title: 'Contact link', sel: 'mailto link' });
  const input = q('input[type="email"], input[type="text"], textarea').filter({ visible: true }).first();
  await S('contact-field', input, ['default', 'focused'], { group: g, title: 'Contact field', desc: 'Focused only; nothing was typed.', sel: 'input' });
  save();
}

async function footer() {
  // The footer is measured on the home page, so home must be the document that
  // is actually open — assigning `current` alone would keep the contact page
  // and mislabel a contact-footer reading as home's.
  if (!(await newPage('home'))) return;
  const g = G.footer;
  const fl = q('footer a').filter({ hasText: /\w{3,}/ }).first();
  if (await fl.count()) {
    await S('footer', q('footer'), ['default'], { group: g, title: 'Footer', sel: 'footer' });
    await S('footer-link', fl, B4, { group: g, title: 'Footer link', sel: 'footer a' });
    await S('footer-social', q('footer a[href*="linkedin" i], footer a[href*="instagram" i], footer a[aria-label]').first(), B4, { group: g, title: 'Footer social icon', sel: 'footer social a' });
    await S('footer-legal', q('footer a').filter({ hasText: /privacy|terms|imprint/i }).first(), B4, { group: g, title: 'Legal link', sel: 'footer a:has-text("Privacy")' });
  }
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  await S('m-header', q('header, nav').first(), ['default'], { group: g, title: 'Mobile header', sel: 'header/nav' }, { noScroll: true });
  const menuBtn = q('button[aria-label*="menu" i], [class*="hamburger" i], header button:has(svg), nav button:has(svg)').filter({ visible: true }).first();
  await S('m-menu-button', menuBtn, B4, { group: g, title: 'Mobile menu button', sel: 'header button' }, { noScroll: true });
  await S('m-menu-open', menuBtn, ['opened'], { group: g, title: 'Mobile menu, open', desc: 'The button after its own toggle; the open panel shows in the crop.', sel: 'header button' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  const mLink = q('a').filter({ hasText: /^Pricing$/ }).first();
  await S('m-nav-link', mLink, ['default'], { group: g, title: 'Mobile nav link', sel: 'a:has-text("Pricing")' }, { noScroll: true });
  await S('m-cta', q('a,button').filter({ hasText: /^Get started$/ }).first(), B4, { group: g, title: 'Mobile CTA', sel: 'a:has-text("Get started")' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, download, contact, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    if (!touched.has(key) && !pages.length) { delete out.components[key]; continue; }
    if (!touched.has(key)) continue;
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st) && pages.length) delete c.states[st];
  }
  save();
  await browser.close().catch(() => {});
}
console.log('done ->', OUT);
