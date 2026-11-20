// Measures thenavia.com's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home blog contact legal mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// thenavia.com is a Webflow marketing site in one light theme. Nothing is
// sent or signed into. Feature items and the mobile menu are local toggles.
// Get started, Sign up, the contact form and the newsletter popup are
// measured, never followed or filled.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/',
  blog: '/blog',
  contact: '/contact-us',
  legal: '/privacy-policy',
};
let page, cdp, current, context, run;
const touched = new Set();
const listed = new Map();
const reached = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000, promo = 'close' } = {}) {
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
  if (!(await open(page, BASE + URLS[key], { wait, promo }))) { log('  BLOCKED', key); await page.close(); await ctx.close(); return false; }
  if (await blocked()) { log('  BLOCKED', key); await page.close(); await ctx.close(); return false; }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  reached.add(mobile ? '@' + key : key);
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
  // Found again: a retry's fresh readings replace the earlier miss record, so
  // the token builder stops rejecting them.
  delete out.components[key].recaptureMissed;
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
        await page.keyboard.type(opts.fillText || 'sample text', { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || 'sample text'}", then deleted; nothing sent`;
      } else if (st === 'opened') {
        if (opts.noToggle) via = 'flyout held open by opts.open';
        else { await toggle(loc); await page.waitForTimeout(900); via = 'own toggle'; }
      } else if (st === 'selected') {
        await toggle(loc, { allowLink: true });
        await page.waitForTimeout(500);
        via = 'own toggle, pressed once; a local UI state, never submitted';
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

// Clicks a UI toggle (drawer, accordion, menu). Refuses a submit button and
// any control whose text names a purchase, consent or location answer this
// kit must never take.
const NEVER = /^(accept all|only required cookies|continue to|stay in|send|submit|sign in|log ?in|login|create|add to bag|add to cart|buy|purchase|pay|checkout|join|subscribe|sign up|save|apply|accept|reject|place order|shop now|read more|join the community|get started|get started for free)$/i;
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
  shell: 'Shell and navigation', home: 'Home', blog: 'Blog', contact: 'Contact',
  legal: 'Legal', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function hidePopups() {
  await page.evaluate(() => {
    document.querySelectorAll('[data-ff-el="root"], #cky-consent, .cky-consent-container, .cky-modal').forEach((el) => {
      el.style.setProperty('display', 'none', 'important');
    });
    const re = /@/;
    for (const el of document.querySelectorAll('a, p, div, span')) {
      const t = (el.innerText || '').trim();
      if (t.length > 80 || !re.test(t) || !t.includes('.')) continue;
      if (el.querySelector('a, p, div') && el.tagName !== 'A') continue;
      el.style.setProperty('visibility', 'hidden', 'important');
    }
  }).catch(() => {});
}

async function home() {
  if (!(await newPage('home', { wait: 4000 }))) return;
  await hidePopups();
  await sheetsFor('home');
  const g = G.shell;
  await S('header', q('.navbar, .w-nav, header, nav').first(), ['default'], { group: g, title: 'Header', desc: 'The top nav: wordmark, Platform, Pricing, Resources, Get started.', sel: '.w-nav' }, { noScroll: true });
  await S('logo', q('a.w-nav-brand').first(), ['default'], { group: g, title: 'Logo', desc: 'The wordmark. Measured, never followed.', sel: 'a.w-nav-brand' }, { noScroll: true });
  await S('nav-link', q('.w-nav-menu a, nav a').filter({ hasText: /^Platform$/ }).first(), B4, { group: g, title: 'Nav link', desc: 'A nav item. Measured, never followed.', sel: 'nav a Platform' }, { noScroll: true });
  await S('nav-cta', q('.w-nav-menu a, nav a').filter({ hasText: /^Get started$/ }).first(), B4, { group: g, title: 'Nav Get started', desc: 'The nav action. It opens the app sign-in wall. Measured, never followed.', sel: 'nav a Get started' }, { noScroll: true });

  const h = G.home;
  await S('hero-title', q('h1').first(), ['default'], { group: h, title: 'Hero title', sel: 'h1' });
  await S('hero-cta', q('a').filter({ hasText: /Get started for free/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'Primary action. Opens the app wall. Measured, never followed.', sel: 'a Get started for free' });
  await S('hero-secondary', q('a').filter({ hasText: /Book a demo/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Book a demo', desc: 'Secondary action. Opens an external calendar. Measured, never followed.', sel: 'a Book a demo' });
  const feature = q('.feature_item').first();
  await S('feature-item', feature, ['default', 'hover', 'focus-visible', 'pressed'], { group: h, title: 'Feature item', desc: 'One of four in-page feature selectors.', sel: '.feature_item' });
  await S('feature-item-selected', q('.feature_item').nth(1), ['selected'], { group: h, title: 'Feature item, selected', desc: 'A feature item after its own toggle. The selection moves locally.', sel: '.feature_item' });
  await S('section-title', q('h2').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', sel: 'h2' });
  await S('plan-card', q('#pricing').locator('a').filter({ hasText: /Sign up/ }).first().locator('xpath=ancestor::*[contains(@class,"w-layout") or self::div][1]'), ['default'], { group: h, title: 'Plan card', desc: 'A pricing plan. The Sign up link is not followed.', sel: '#pricing' });
  await S('plan-cta', q('#pricing a').filter({ hasText: /Sign up/ }).first(), B4, { group: h, title: 'Plan Sign up', desc: 'A plan action. Opens the app wall. Measured, never followed.', sel: '#pricing a' });
  await S('testimonial', q('blockquote, [class*="testimonial"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Testimonial', sel: 'blockquote' });
  save();
}

async function blog() {
  if (!(await newPage('blog', { wait: 3000 }))) return;
  await hidePopups();
  const g = G.blog;
  await S('blog-title', q('h1').first(), ['default'], { group: g, title: 'Blog title', sel: 'h1' }, { noScroll: true });
  const card = q('a[href*="/blog/"]').filter({ visible: true }).first();
  await S('article-card', card, ['default', 'hover', 'focus-visible', 'pressed'], { group: g, title: 'Article card', desc: 'A blog index card. Measured, never followed.', sel: 'a[href*="/blog/"]' });
  const next = q('a').filter({ hasText: /^Next$/ }).filter({ visible: true }).first();
  if (await next.count()) await S('pager-next', next, B4, { group: g, title: 'Blog Next', desc: 'The index pager. Measured, never followed in this pass.', sel: 'a Next' });
  save();
}

async function contact() {
  if (!(await newPage('contact', { wait: 3000 }))) return;
  await hidePopups();
  const g = G.contact;
  await S('contact-title', q('h1').first(), ['default'], { group: g, title: 'Contact title', sel: 'h1' }, { noScroll: true });
  const field = q('input[type="text"]').filter({ visible: true }).first();
  if (await field.count()) await S('text-field', field, ['default', 'hover', 'focus-visible', 'focused'], { group: g, title: 'Text field', desc: 'A contact field. Focused only. Nothing typed or sent.', sel: 'input[type=text]' });
  const email = q('input[type="email"]').filter({ visible: true }).first();
  if (await email.count()) await S('email-field', email, ['default', 'focused'], { group: g, title: 'Email field', desc: 'Focused only. Nothing typed or sent.', sel: 'input[type=email]' });
  const area = q('textarea').filter({ visible: true }).first();
  if (await area.count()) await S('text-area', area, ['default', 'focused'], { group: g, title: 'Message field', desc: 'Focused only. Nothing typed or sent.', sel: 'textarea' });
  const sel = q('select').filter({ visible: true }).first();
  if (await sel.count()) await S('select', sel, ['default', 'hover', 'focus-visible', 'focused'], { group: g, title: 'Topic select', desc: 'Focused only. No option chosen and nothing sent.', sel: 'select' });
  const submit = q('input[type="submit"], button[type="submit"]').filter({ visible: true }).first();
  if (await submit.count()) await S('submit', submit, ['default', 'hover', 'focus-visible'], { group: g, title: 'Submit', desc: 'The contact submit. Measured, never pressed.', sel: 'submit' });
  save();
}

async function legal() {
  if (!(await newPage('legal', { wait: 2500 }))) return;
  await hidePopups();
  const g = G.legal;
  await S('legal-title', q('h1').first(), ['default'], { group: g, title: 'Legal title', sel: 'h1' }, { noScroll: true });
  await S('legal-body', q('main, .w-richtext, article, .legal, section').filter({ visible: true }).first(), ['default'], { group: g, title: 'Legal body', sel: 'main' });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 9000 }))) return;
  const g = G.footer;
  const foot = q('.footer, footer').first();
  await foot.scrollIntoViewIfNeeded().catch(() => {});
  await S('footer', foot, ['default'], { group: g, title: 'Footer', sel: 'footer' });
  const fl = q('.footer a, footer a').filter({ hasText: /\w{3,}/ }).first();
  if (await fl.count()) await S('footer-link', fl, B4, { group: g, title: 'Footer link', sel: 'footer a' });
  const soc = q('.footer a[href*="twitter"], footer a[href*="instagram"], footer a[href*="dribbble"], footer a[aria-label]').filter({ visible: true }).first();
  if (await soc.count()) await S('footer-social', soc, B4, { group: g, title: 'Footer social icon', sel: 'footer social a' });
  save();
}

async function mobile() {
  if (!(await newPage('home', { mobile: true, wait: 3500 }))) return;
  await hidePopups();
  const g = G.mobile;
  await S('m-header', q('.navbar, .w-nav, header, nav').first(), ['default'], { group: g, title: 'Mobile header', sel: '.w-nav' }, { noScroll: true });
  const menuBtn = q('.w-nav-button, button[aria-label="menu"]').filter({ visible: true }).first();
  await S('m-menu-button', menuBtn, B4, { group: g, title: 'Mobile menu button', sel: '.w-nav-button' }, { noScroll: true });
  await S('m-menu-open', menuBtn, ['opened'], { group: g, title: 'Mobile menu, open', desc: 'The bar after its own toggle. The crop is the opened nav panel.', sel: '.w-nav-button' }, { cropLoc: q('.w-nav-overlay, .w-nav-menu').filter({ visible: true }).last(), pad: 0 });
  const mLink = q('.w-nav-menu a, .w-nav-overlay a').filter({ hasText: /^Platform$/ }).filter({ visible: true }).first();
  await S('m-nav-link', mLink, ['default', 'hover'], { group: g, title: 'Mobile nav link', desc: 'Read inside the open menu. Measured, never followed.', sel: 'overlay a' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(400);
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844), light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, blog, contact, legal, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // Prune entries this run never touched only when their page was actually
    // reached: a blocked page must not erase the readings saved under it.
    const src = c.group === G.mobile ? '@' + c.page : c.page;
    if (!touched.has(key) && !pages.length && reached.has(src)) { delete out.components[key]; continue; }
    if (!Object.keys(c.states || {}).length && !c.missing && touched.has(key)) delete out.components[key];
  }
  save();
  await context.close().catch(() => {});
  await browser.close().catch(() => {});
}
