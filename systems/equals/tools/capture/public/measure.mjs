// Measures Equals' public components in every state reachable without
// signing in, submitting a form or starting a trial.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing usecase signin docs docsdark mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// Equals' public surface is three sites: the equals.com marketing pages
// (light only, BEM classes), the go.equals.com sign-in card (light, the only
// signed-out view of the Rails app) and the docs.equals.com Mintlify docs in
// its real light and dark themes. Nothing is sent, bought or signed into:
// the only presses are local UI toggles — the "Use cases" mega-menu trigger,
// a pricing FAQ label (a checkbox accordion), the guide's "Start reading"
// splash and the mobile hamburger. The "Get a demo" email captures and the
// sign-in form are focused and typed into then cleared — never submitted.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, APP_BASE, DOCS_BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, REF, CROPS, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: BASE + '/', pricing: BASE + '/pricing/', usecase: BASE + '/use-cases/arr-dashboard/',
  signin: APP_BASE + '/', docs: DOCS_BASE + '/docs/getting-started', docsdark: DOCS_BASE + '/docs/getting-started',
  mobile: BASE + '/',
};
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes a block or error gates this run: components last measured on them
// keep their earlier readings instead of being pruned below (a blocked pass
// must never erase evidence).
const failedPages = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /performing security verification|verifying you are human|just a moment|access denied|unusual activity from your computer network|not a robot|you have been blocked|unable to access/i.test(t) || t.trim().length < 40;
  }).catch(() => true);
}

async function newPage(key, { mobile = false, wait = 8000, promo = 'close', url = null, scheme = 'light' } = {}) {
  current = key;
  // Close the previous page's context before opening the next: leaving them
  // alive keeps every captured page (and its animations) running in the
  // background for the rest of the run.
  if (liveCtx) { await liveCtx.close().catch(() => {}); liveCtx = null; }
  const b = context.browser();
  const ctx = liveCtx = await b.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US', colorScheme: scheme }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US', colorScheme: scheme });
  await patch(ctx);
  page = await ctx.newPage();
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  page.setDefaultTimeout(8000);
  log('open', key, mobile ? '(mobile)' : '', scheme === 'dark' ? '(dark)' : '');
  const cleared = await open(page, url || URLS[key], { wait, promo });  // false: the bot check did not clear (lib.mjs)
  if (!cleared || (await blocked())) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
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
  Object.assign(c, { page: current, run, url: URLS[current] }, meta);
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
    c.states[state] = { ...s, crop: file, via: opts.via, run };
    if (opts.extra) c.states[state].extra = await opts.extra(loc);
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    // A failed re-read must not erase an earlier successful one: keep the
    // saved style and record the failed attempt beside it.
    const prev = c.states[state];
    if (prev && prev.style) prev.rerunError = String(e.message || e).slice(0, 200);
    else c.states[state] = { error: String(e.message || e).slice(0, 200) };
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
        via = 'filled state not captured: this pass does not type into fields';
        log('  !', key, st, via);
        continue;
      } else if (st === 'opened') {
        if (opts.noToggle) via = via || 'held open by an earlier toggle';
        else { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle'; }
      } else via = via || 'at rest';
      if (st === 'focus-visible' && via === 'focus failed') {
        // Keyboard focus never reached the element, so a reading now would be the element at rest
        // saved as its focus. Record the miss instead (the builders list it as "focus could not be
        // captured"), and drop the crop an earlier run saved for this state.
        // An earlier run's real focus reading is kept, with the failed retry noted beside it.
        const prevSt = out.components[key].states[st];
        if (prevSt?.style && prevSt.via !== 'focus failed') {
          prevSt.rerunError = 'focus failed: keyboard focus did not reach the element';
          log('  !', key, st, 'focus failed; earlier reading kept');
        } else {
          const old = prevSt?.crop && path.resolve(REF, prevSt.crop);
          if (old && old.startsWith(CROPS + path.sep)) fs.rmSync(old, { force: true });
          out.components[key].states[st] = { skipped: 'focus failed: keyboard focus did not reach the element', via, run };
          log('  -', key, st, 'skipped: focus failed');
        }
      } else await measure(key, st, loc, { ...opts, via });
    } catch (e) {
      const prev = out.components[key].states[st];
      if (prev && prev.style) prev.rerunError = String(e.message || e).slice(0, 200);
      else out.components[key].states[st] = { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  // A listed state that failed its re-read kept the earlier evidence under
  // rerunError (and its own earlier `run`); the entry then republishes under
  // the earlier run's page/run/url and records the miss, so retained readings
  // never carry the new run's date.
  if (keep && list.some((st) => out.components[key].states[st]?.rerunError)) {
    Object.assign(out.components[key], keep);
    out.components[key].recaptureMissed = run;
  }
  await reset();
}

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again|get a demo|request a demo|start reading)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const FIELD = ['default', 'focused', 'filled'];

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
  const slot = `${key} ${sel}`; // one entry per element, so a second call cannot overwrite the first
  out._meta.reducedMotion ??= {};
  try {
    const b = context.browser();
    const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', reducedMotion: 'reduce' });
    await patch(ctx);
    const p = await ctx.newPage();
    await p.goto(URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(7000);
    await closePromo(p);
    const v = await p.evaluate((s) => {
      const el = document.querySelector(s);
      if (!el) return null;
      const cs = getComputedStyle(el);
      return { transition: cs.transition, animation: cs.animation, scrollBehavior: getComputedStyle(document.documentElement).scrollBehavior };
    }, sel).catch(() => null);
    out._meta.reducedMotion[slot] = { page: key, selector: sel, reduce: v };
    await ctx.close();
  } catch (e) { out._meta.reducedMotion[slot] = { page: key, selector: sel, error: String(e).slice(0, 120) }; }
}

const G = {
  shell: 'Marketing chrome', home: 'Home hero and sections', workbook: 'Workbook mockup',
  pricing: 'Pricing', guide: 'Guide', signin: 'Sign in (go.equals.com)',
  docs: 'Docs (docs.equals.com)', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

// The "Use cases" mega-menu: button.header__menu-trigger toggles
// .header__menu--use-cases. A local UI toggle; its links are never followed.
async function openUseCasesMenu() {
  const openNow = (ms) => page.waitForFunction(
    () => [...document.querySelectorAll('.header__menu')].some((el) => el.getBoundingClientRect().height > 40 && getComputedStyle(el).visibility !== 'hidden' && +getComputedStyle(el).opacity > 0),
    undefined, { timeout: ms }).then(() => true).catch(() => false);
  if (await openNow(400)) return 'the use-cases menu was already open';
  const trig = page.locator('button.header__menu-trigger').filter({ visible: true }).first();
  if (!(await trig.count())) return 'no Use-cases trigger';
  for (let i = 0; i < 3; i++) {
    await trig.click({ timeout: 4000 }).catch(() => trig.evaluate((el) => el.click()));
    if (await openNow(3000)) return 'clicked "Use cases" to open the mega-menu';
    await page.waitForTimeout(500);
  }
  return 'clicked "Use cases"; the menu did not report open';
}

// A pricing FAQ item: label.faq__question toggles the hidden .faq__checkbox —
// a local accordion, never a form post.
async function openFaq() {
  const openNow = () => page.evaluate(() => [...document.querySelectorAll('.faq__checkbox')].some((c) => c.checked));
  if (await openNow()) return 'a FAQ item was already open';
  const q0 = page.locator('label.faq__question').filter({ visible: true }).first();
  if (!(await q0.count())) return 'no FAQ label';
  await q0.click({ timeout: 4000 }).catch(() => q0.evaluate((el) => el.click()));
  await page.waitForTimeout(900);
  return (await openNow()) ? 'clicked the first FAQ question to expand its answer' : 'clicked the FAQ label; the accordion did not report open';
}

// The mobile nav: label.header__mobile-nav-toggle toggles
// input.header__mobile-nav-checkbox — a local drawer, never followed.
async function openMobileNav() {
  const openNow = (ms) => page.waitForFunction(
    () => { const c = document.querySelector('.header__mobile-nav-checkbox'); return c && c.checked; },
    undefined, { timeout: ms }).then(() => true).catch(() => false);
  if (await openNow(400)) return 'the mobile nav was already open';
  const ham = page.locator('label.header__mobile-nav-toggle').filter({ visible: true }).first();
  if (!(await ham.count())) return 'no hamburger';
  for (let i = 0; i < 3; i++) {
    await ham.click({ timeout: 4000 }).catch(() => ham.evaluate((el) => el.click()));
    if (await openNow(2500)) return 'clicked the hamburger to open the mobile nav';
    await page.waitForTimeout(500);
  }
  return 'clicked the hamburger; the nav did not report open';
}

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('mkt-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Marketing header', desc: 'The top bar: wordmark, Home / Use cases / Pricing / About, "Get a demo" capture and the "Sign in" link.', sel: 'header' }, { noScroll: true });
  await S('mkt-logo', q('header a.header__nav-home, header .svg-embed').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Equals wordmark at the left of the header.', sel: 'header logo' }, { noScroll: true });
  // "Home" and the mobile-only "Use cases" anchors are real nodes but 0x0
  // (Playwright's visible = checkVisibility, which passes a zero-size node);
  // the hasText below keeps only the painted Pricing/About links.
  await S('mkt-nav-link', q('header a.header__nav-link').filter({ hasText: /^\s*(Pricing|About)\s*$/ }).first(), B4, { group: g, title: 'Nav link', desc: 'A marketing header link (Pricing/About); measured, never followed.', sel: 'header .header__nav-link' }, { noScroll: true });
  await S('mkt-menu-trigger', q('button.header__menu-trigger').filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Use-cases menu trigger', desc: 'The header "Use cases" button; opened to reveal the mega-menu of use-case links (a local toggle, its links never followed).', sel: 'button.header__menu-trigger' }, { noScroll: true });
  await S('mkt-menu', q('.header__menu--use-cases, .header__menu').filter({ visible: true }).first(), ['default'], { group: g, title: 'Use-cases mega-menu', desc: 'The dropdown the "Use cases" trigger opens: category labels and use-case links.', sel: '.header__menu--use-cases' }, { open: openUseCasesMenu, noScroll: true, noReset: true });
  await S('mkt-menu-item', q('.header__menu a.header__use-case-link, .header__use-case-link').filter({ visible: true }).first(), B4, { group: g, title: 'Mega-menu link', desc: 'One use-case link inside the open mega-menu; measured, never followed.', sel: '.header__use-case-link' }, { open: openUseCasesMenu, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('mkt-signin', q('header a, .header__nav a').filter({ hasText: /^\s*Sign in\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-in link', desc: 'The header "Sign in" link to go.equals.com; measured, never followed.', sel: 'header Sign in' }, { noScroll: true });
  const h = G.home;
  await S('hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: '"What’s after Excel?" — the Serrif Condensed display on the hero.', sel: 'h1.home__hero-h1' }, { noScroll: true });
  await S('hero-sub', q('p, [class*="sub" i]').filter({ hasText: /first new spreadsheet/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero sub', desc: 'The lede under the headline.', sel: 'hero sub' }, { noScroll: true });
  // The first input/button in the page is a 0x0 mobile-only header clone;
  // the hero capture is the one inside .home__hero-cta.
  await S('hero-email', q('.home__hero-cta input.email-capture-group__input').first(), FIELD, { group: h, title: 'Demo email field', desc: 'The "Enter your work email" capture under the hero copy; focused and typed into then cleared — never submitted.', sel: '.home__hero-cta .email-capture-group__input' }, { fill: false });
  await S('hero-cta', q('.home__hero-cta button.email-capture-group__button').first(), B4, { group: h, title: 'Get-a-demo button', desc: 'The black "Get a demo" pill on the email capture; measured never pressed (it submits the capture).', sel: '.home__hero-cta .email-capture-group__button' });
  await S('section-label', q('p.section__label').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section label', desc: 'The numbered eyebrow label over a marketing section ("1. TRUST"), coloured by the page’s label-- theme.', sel: 'p.section__label' });
  await S('section-h2', q('h2.section__h2').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A marketing section heading ("A single source of truth…").', sel: 'h2.section__h2' });
  const w = G.workbook;
  await S('wb-mockup', q('[class*="mockup-workbook" i]').filter({ visible: true }).first(), ['default'], { group: w, title: 'Workbook mockup', desc: 'The in-page spreadsheet demo: toolbar, formula bar, sheet tabs and cells — a public demo, not the app.', sel: '.mockup-workbook' });
  await S('wb-toolbar-button', q('.mockup-workbook__toolbar-button').filter({ visible: true }).first(), B4, { group: w, title: 'Mock toolbar button', desc: 'A toolbar icon button inside the workbook mockup; measured, never pressed.', sel: '.mockup-workbook__toolbar-button' });
  await S('wb-sheet-tab', q('.mockup-workbook__sheet-tab--active, .mockup-workbook__sheet-tab').filter({ visible: true }).first(), B4, { group: w, title: 'Sheet tab', desc: 'A workbook sheet tab inside the mockup; measured, never pressed.', sel: '.mockup-workbook__sheet-tab' });
  // The mockup's demo cycles slides and its cells periodically collapse to
  // 0x0; domFind with a min size picks whichever label cell is painted now.
  await S('wb-cell', await domFind(page, /.*/, { sel: '.mockup-workbook__cell--label', tag: 'wbcell', minW: 5, minH: 5 }), ['default'], { group: w, title: 'Workbook cell', desc: 'A label cell in the workbook mockup ("Build Summary"); the mockup cycles demo slides, so the reading is whichever cell is painted — its value cells animate as the demo types.', sel: '.mockup-workbook__cell--label' });
  await S('build-tab', q('.build-tab--active, .build-tab').filter({ visible: true }).first(), B4, { group: h, title: 'Persona tab', desc: 'A "Build …" persona tab in the AI-demo section (the active one carries build-tab--active); measured, never pressed.', sel: '.build-tab' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('plan-card', q('.pricing__plan').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan card', desc: 'An Essential pricing card: plan name, price, "Get a demo" CTA and feature list on the cream page.', sel: '.pricing__plan' });
  await S('plan-name', q('.pricing__plan .plan-name').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan name', desc: 'The "Essential" plan label.', sel: '.plan-name' });
  await S('plan-price', q('.pricing__plan .plan-price').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan price', desc: 'The "$24k /year" price line — the suffix is a smaller muted span.', sel: '.plan-price' });
  await S('plan-cta', q('.pricing__plan .plan-cta').filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'The card’s "Get a demo" action on its accent--amber background; measured never pressed.', sel: '.plan-cta' });
  await S('plan-cta-orchid', q('.pricing__plan .plan-cta.accent--orchid, .pricing__plan.accent--orchid .plan-cta, .pricing__plan .plan-cta').nth(1), B4, { group: g, title: 'Plan CTA (orchid)', desc: 'The Business card’s CTA on the accent--orchid background; each plan carries its own accent colour.', sel: '.plan-cta.accent--orchid' });
  await S('plan-feature', q('.pricing__plan .plan-features li').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan feature row', desc: 'A feature line inside the plan card ("Unlimited seats").', sel: '.plan-features li' });
  await S('faq', q('.faq').filter({ visible: true }).first(), ['default', 'opened'], { group: g, title: 'FAQ item', desc: 'A pricing FAQ row (a checkbox accordion); opened by clicking its label — a local toggle, never a form post.', sel: '.faq' }, { before: { opened: openFaq }, noToggle: true });
  // ^ `open` is a prerequisite run before every state, so on 2026-11-13 `default` was read already
  //   expanded; the toggle now runs only for `opened`.
  await S('faq-question', q('label.faq__question').filter({ visible: true }).first(), ['default'], { group: g, title: 'FAQ question', desc: 'The question label of the first FAQ item.', sel: 'label.faq__question' }, { open: openFaq });
  save();
}

async function usecase() {
  if (!(await newPage('usecase'))) return;
  await sheetsFor('usecase');
  await chrome('usecase');
  const g = G.home;
  await S('uc-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Use-case headline', desc: '"ARR Dashboard" — the use-case page’s display heading.', sel: 'use-case h1' }, { noScroll: true });
  await S('uc-lede', q('main p, article p, .use-case p').filter({ visible: true }).first(), ['default'], { group: g, title: 'Use-case lede', desc: 'The first paragraph under the use-case hero.', sel: 'use-case first paragraph' });
  // Scoped to main: the header also carries a 0x0 mobile-only clone of the
  // capture that checkVisibility counts as visible.
  await S('uc-email', q('main input.email-capture-group__input').first(), FIELD, { group: g, title: 'Demo email field (use-case)', desc: 'The same email capture on a use-case page; focused and typed into then cleared — never submitted.', sel: 'main .email-capture-group__input' }, { fill: false });
  save();
}

async function signin() {
  if (!(await newPage('signin', { wait: 8000 }))) return;
  await sheetsFor('signin');
  await chrome('signin');
  const g = G.signin;
  await S('signin-card', q('.SignIn').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-in card', desc: 'The whole "Sign in to Equals" card — heading, subheading, the email form and the footer line.', sel: '.SignIn' }, { noScroll: true });
  await S('signin-heading', q('.SignIn__Heading, .SignIn h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-in heading', desc: '"Sign in to Equals".', sel: '.SignIn__Heading' }, { noScroll: true });
  await S('signin-sub', q('.SignIn__Subheading').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-in subheading', desc: '"Enter your email below to login to your account".', sel: '.SignIn__Subheading' }, { noScroll: true });
  await S('signin-email', q('input.SignIn__Input, .SignIn input[type="email"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Sign-in email field', desc: 'The empty email input on the sign-in wall. Nothing is typed.', sel: '.SignIn__Input' }, { noScroll: true, fill: false });
  await S('signin-continue', q('input.SignIn__Button, .SignIn input[type="submit"]').filter({ visible: true }).first(), B4, { group: g, title: 'Continue button', desc: 'The form’s "Continue" submit; its states were measured but it was never clicked — nothing was submitted.', sel: '.SignIn__Button' }, { noScroll: true });
  await S('signin-footer', q('.SignIn__Footer, .SignIn__Footer a').filter({ visible: true }).first(), B4, { group: g, title: 'Sign-in footer link', desc: '"Don’t have an account? Request a demo" — the footer copy and link; measured, never followed.', sel: '.SignIn__Footer' }, { noScroll: true });
  save();
}

async function docsPage(scheme = 'light') {
  const key = scheme === 'dark' ? 'docsdark' : 'docs';
  if (!(await newPage(key, { wait: 9000, scheme }))) return;
  await sheetsFor(key);
  await chrome(key);
  const g = G.docs + (scheme === 'dark' ? ' (dark)' : ' (light)');
  const p = scheme === 'dark' ? 'd-' : '';
  await S(p + 'docs-sidebar', q('#sidebar, aside, [class*="sidebar" i], nav[class*="nav" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Docs sidebar', desc: 'The docs left rail: logo, search, theme menu and the nav tree.', sel: 'docs sidebar' }, { noScroll: true });
  await S(p + 'docs-logo', q('#logo, header a, [class*="logo" i]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Docs logo', desc: 'The Equals wordmark at the top of the docs rail.', sel: 'docs logo' }, { noScroll: true });
  await S(p + 'docs-search', q('#search-bar-entry, button[id*="search" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Search button', desc: 'The "Search…" field-styled button in the docs rail; measured, never opened.', sel: '#search-bar-entry' }, { noScroll: true });
  await S(p + 'docs-theme-btn', q('#theme-preference-menu-trigger, button[id*="theme" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Theme menu button', desc: 'The docs theme menu button; measured, never opened (the dark capture used a prefers-color-scheme context instead).', sel: '#theme-preference-menu-trigger' }, { noScroll: true });
  await S(p + 'docs-nav-item', q('#sidebar a, aside a, [class*="sidebar" i] a').filter({ hasText: /^\s*(Overview|Getting started)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav item', desc: 'A docs sidebar link; measured, never followed.', sel: 'sidebar nav link' }, { noScroll: true });
  await S(p + 'docs-assistant', q('#assistant-entry, button[id*="assistant" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Assistant button', desc: 'The "Ask AI" assistant entry in the docs chrome; measured at rest, never opened — nothing was sent.', sel: '#assistant-entry' }, { noScroll: true });
  await S(p + 'docs-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Page heading', desc: 'The doc page’s h1.', sel: 'docs h1' }, { noScroll: true });
  await S(p + 'docs-para', q('main p, article p').filter({ visible: true }).first(), ['default'], { group: g, title: 'Body paragraph', desc: 'A body paragraph in the doc.', sel: 'main p' });
  await S(p + 'docs-link', q('main a, article a').filter({ hasText: /\S{3,}/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Body link', desc: 'A link inside the doc body; measured, never followed.', sel: 'main a' });
  await S(p + 'docs-code', q('main pre, article pre, main code, article code').filter({ visible: true }).first(), ['default'], { group: g, title: 'Code block', desc: 'A code block or inline code span in the doc.', sel: 'main pre/code' });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', desc: 'The top bar at 390: wordmark, hamburger and "Get a demo".', sel: 'header' }, { noScroll: true });
  await S('m-hamburger', q('label.header__mobile-nav-toggle').filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Hamburger', desc: 'The mobile nav toggle (a label over a hidden checkbox); opened to reveal the drawer — a local toggle, its links never followed.', sel: 'label.header__mobile-nav-toggle' }, { noScroll: true });
  // The drawer is the tall panel the hamburger reveals: `.header__nav, .header__mobile-nav, nav`
  // .first() caught the 52px header nav on 2026-11-13.
  await openMobileNav();
  await S('m-drawer', await domFind(page, /Use cases[\s\S]*Pricing/, { sel: 'nav, div, ul', tag: 'mdrawer', minH: 200 }), ['default'], { group: g, title: 'Mobile nav drawer', desc: 'The nav the hamburger opens.', sel: 'mobile nav' }, { open: openMobileNav, noScroll: true, noReset: true });
  await S('m-hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Hero headline (mobile)', desc: '"What’s after Excel?" at 390 wide.', sel: 'h1' }, { noScroll: true });
  await S('m-email', q('input.email-capture-group__input').filter({ visible: true }).first(), FIELD, { group: g, title: 'Demo email field (mobile)', desc: 'The email capture at 390; focused and typed into then cleared — never submitted.', sel: '.email-capture-group__input' }, { fill: false });
  save();
}

const PAGES = { home, pricing, usecase, signin, docs: () => docsPage('light'), docsdark: () => docsPage('dark'), mobile };
const want = process.argv.slice(2).filter((a) => !a.startsWith('-'));
const launched = await launch();
const browser = launched.browser;
context = launched.context;
run = new Date().toISOString();
out._meta.read = run.slice(0, 10);
const finishedPages = new Set();
try {
  for (const k of Object.keys(PAGES)) {
    if (want.length && !want.includes(k)) continue;
    await PAGES[k]();
    finishedPages.add(k);
  }
  await reducedMotion('home', '.build-tab');
  await reducedMotion('home', 'button.email-capture-group__button');
} finally {
  for (const k of failedPages) log('blocked:', k);
  // An untouched entry is pruned only when its page finished this run (a page the run never
  // reached, or an edge-blocked one, keeps its earlier readings under their own provenance), and
  // a touched entry keeps only the states this run's spec lists. comp() stamps every touched
  // entry with this run, so the old `c.run === run` guard could never prune anything.
  for (const [k, c] of Object.entries(out.components)) {
    if (!touched.has(k) && finishedPages.has(c.page) && !failedPages.has(c.page)) { delete out.components[k]; continue; }
    const wantSt = listed.get(k);
    if (wantSt) for (const st of Object.keys(c.states || {})) if (!wantSt.has(st)) delete c.states[st];
  }
  save();
  if (liveCtx) await liveCtx.close().catch(() => {});
  await context.close().catch(() => {});
  await browser.close();
}