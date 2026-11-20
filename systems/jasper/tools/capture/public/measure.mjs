// Measures jasper.ai's public components in every state reachable without
// signing in, booking a demo, or submitting a form.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home platform pricing brand demo signin mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// www.jasper.ai is a Webflow marketing site. Tokens are --swatch--* and
// --_theme---*, rebound by .u-theme-light and .u-theme-dark. app.jasper.ai
// is the login boundary. Nothing is sent or signed into: the only presses
// are local UI toggles (nav dropdown, FAQ, mobile menu). The demo form and
// the login card are measured at rest. Consent overlays are hidden, never
// answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, APP, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', platform: '/platform', pricing: '/pricing', brand: '/brand', demo: '/demo', signin: APP + '/auth/login', mobile: '/' };
const abs = (key) => (URLS[key] && URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key]);
let page, cdp, current, context, run, liveCtx;
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
  const loaded = await open(page, url || abs(key), { wait, promo });
  if (!loaded || await blocked()) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
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
  Object.assign(c, { page: current, run, url: abs(current) }, meta);
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
      } else if (st === 'selected') {
        if (opts.noToggle) via = 'held selected by an earlier toggle';
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

// Clicks a UI toggle (menu trigger, accordion, chip, locale dot). Refuses a
// submit button and any control whose text names an action this kit must
// never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start free|get started|claim|share|export|continue|continue with email|continue with google|get a demo|start free trial|free trial|book a demo|sign up)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const navTrigger = () => q('header button[data-slot="navigation-menu-trigger"], header button').filter({ hasText: /^\s*Products\s*$/ }).first();
// Click the Products trigger only when the menu is closed: a second click
// would collapse it again, and the measurements below need it open.
const openNav = async () => {
  const t = navTrigger();
  if (!(await t.count())) return;
  const state = () => page.evaluate(() => ({ n: document.querySelectorAll('[data-slot="navigation-menu-content"]').length, open: [...document.querySelectorAll('[data-slot="navigation-menu-content"]')].some((e) => { const r = e.getBoundingClientRect(); return r.width > 100 && r.height > 50; }) }));
  if ((await state()).open) return;
  const ok = await t.click({ timeout: 5000 }).then(() => true).catch(async () => { await t.evaluate((el) => el.click()); return 'js'; });
  await page.waitForTimeout(1100);
  const after = await state();
  log('  · openNav click=' + ok, 'content=' + after.n, 'open=' + after.open);
  // A click on a hover-armed trigger can toggle the menu closed again; click
  // once more when the first press left it shut.
  if (!after.open && ok === true) {
    await t.click({ timeout: 5000 }).catch(() => {});
    await page.waitForTimeout(1100);
    const again = await state();
    log('  · openNav retry', 'content=' + again.n, 'open=' + again.open);
  }
};
// Cartesia mounts its Astro islands on intersection (client:visible), so a
// component below the fold may not exist in the DOM until it has been
// scrolled to. The sweep walks the page once, mounts every island, and comes
// back to the top.
async function lazySweep() {
  await page.evaluate(async () => {
    const h = document.documentElement.scrollHeight;
    for (let y = 0; y < h; y += 700) { scrollTo(0, y); await new Promise((r) => setTimeout(r, 110)); }
    scrollTo(0, 0);
  });
  await page.waitForTimeout(1400);
}
// The biggest visible element matching sel gets data-m-mark="<tag>"; returns
// a locator for it (an empty one when nothing matched).
async function markBiggest(sel, tag, { minW = 100, minH = 40 } = {}) {
  const ok = await page.evaluate(([s, t, w, h]) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const cands = [...document.querySelectorAll(s)].filter((n) => {
      const r = n.getBoundingClientRect();
      return r.width >= w && r.height >= h && getComputedStyle(n).visibility !== 'hidden';
    }).sort((a, b) => b.getBoundingClientRect().width * b.getBoundingClientRect().height - a.getBoundingClientRect().width * a.getBoundingClientRect().height);
    if (!cands[0]) return false;
    cands[0].setAttribute('data-m-mark', t);
    return true;
  }, [sel, tag, minW, minH]);
  return ok ? page.locator(`[data-m-mark="${tag}"]`) : page.locator('[data-m-mark="__none__"]');
}

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
    await p.goto(abs(key), { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
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

// Marks the nearest ancestor of the element matching sel that paints a fill
// or a background image (the hero island paints a gradient), or falls back to
// marking a painted descendant: the hero card is a sibling layer, not an
// ancestor, so for it we mark the painted element inside its section instead.
async function markPainted(sel, tag, { maxUp = 8, minW = 100, minH = 60, descend = false } = {}) {
  const ok = await page.evaluate(([s, t, up, w, h, desc]) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const el = [...document.querySelectorAll(s)].find((n) => { const r = n.getBoundingClientRect(); return r.width > 0 && r.height > 0; });
    if (!el) return false;
    const paints = (cs) => cs.backgroundColor !== 'rgba(0, 0, 0, 0)' || cs.backgroundImage !== 'none';
    if (!desc) for (let n = el, i = 0; n && i < up; n = n.parentElement, i++) {
      const cs = getComputedStyle(n);
      const r = n.getBoundingClientRect();
      if (r.width >= w && r.height >= h && paints(cs)) { n.setAttribute('data-m-mark', t); return true; }
    }
    if (desc) {
      // The painted layer sits beside the content, not above it: find the
      // biggest painted element under the element's own section.
      const sec = el.closest('section') || el.parentElement;
      const cands = [...(sec || el).querySelectorAll('*')].filter((n) => {
        const r = n.getBoundingClientRect(); const cs = getComputedStyle(n);
        return r.width >= w && r.height >= h && paints(cs);
      }).sort((a, b) => b.getBoundingClientRect().width * b.getBoundingClientRect().height - a.getBoundingClientRect().width * a.getBoundingClientRect().height);
      if (cands[0]) { cands[0].setAttribute('data-m-mark', t); return true; }
    }
    return false;
  }, [sel, tag, maxUp, minW, minH, descend]);
  return ok ? page.locator(`[data-m-mark="${tag}"]`) : page.locator('[data-m-mark="__none__"]');
}


const G = {
  shell: 'Shell and navigation', hero: 'Home hero', home: 'Home',
  pricing: 'Pricing', brand: 'Brand page', demo: 'Demo form boundary',
  auth: 'App login boundary', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('header', q('.nav_contain').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The sticky marketing nav: wordmark, Platform, Solutions, Resources, Company, Pricing, Log in, Free Trial and Get a Demo.', sel: '.nav_contain' }, { noScroll: true });
  await S('logo', q('.nav_contain a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Jasper wordmark link.', sel: '.nav_contain a[href="/"]' }, { noScroll: true });
  await S('nav-item', q('.nav_menu_link').filter({ hasText: /Platform/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav item', desc: 'A header menu item (Platform). Hover opens its dropdown. Measured, never followed.', sel: '.nav_menu_link "Platform"' }, { noScroll: true });
  await S('nav-link', q('a').filter({ hasText: /^\s*Pricing\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'The Pricing header link.', sel: 'a "Pricing"' }, { noScroll: true });
  await S('nav-login', q('a').filter({ hasText: /^\s*Log In\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Log in link', desc: 'The Log In header action. Measured, never followed. It opens app.jasper.ai.', sel: 'a "Log In"' }, { noScroll: true });
  await S('nav-cta', q('a, .btn_main_wrap').filter({ hasText: /Free Trial/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav CTA', desc: 'The Free Trial header button. Measured, never followed.', sel: 'Free Trial' }, { noScroll: true });
  await S('nav-secondary', q('a').filter({ hasText: /Get a Demo/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav secondary', desc: 'The Get a Demo header link. Measured, never followed.', sel: 'a "Get a Demo"' }, { noScroll: true });
  const item = q('.nav_menu_item').filter({ hasText: /Platform/ }).filter({ visible: true }).first();
  if (await item.count()) { await item.hover(); await page.waitForTimeout(1200); }
  await S('nav-dropdown', q('.nav_dropdown').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav dropdown', desc: 'The Platform mega-menu panel, opened by hovering its item. The full-viewport .nav_dropdown_wrap is the scrim, not the panel.', sel: '.nav_dropdown' }, { noScroll: true, noReset: true });
  await S('menu-link', q('.nav_dropdown a').filter({ hasText: /Canvas|Brand IQ|Agents/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Menu link', desc: 'A link inside the opened Platform dropdown.', sel: '.nav_dropdown a' }, { noScroll: true, noReset: true });
  await page.mouse.move(8, 500);
  await page.waitForTimeout(400);
  const h = G.hero;
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The display headline, set in Feature.', sel: 'h1' });
  await S('hero-cta', q('a').filter({ hasText: /Start Free Trial|Get a Demo/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'A hero action. Measured, never followed.', sel: 'hero CTA' });
  await S('hero-secondary', q('a').filter({ hasText: /Explore the Platform/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero secondary', desc: 'The Explore the Platform link. Measured, never followed.', sel: 'a "Explore the Platform"' });
  const s = G.home;
  await S('section-title', q('h2').filter({ visible: true }).first(), ['default'], { group: s, title: 'Section heading', desc: 'A Feature display heading in a home section.', sel: 'h2' });
  await S('card', q('.g_card, [class*="card"]').filter({ visible: true }).first(), ['default'], { group: s, title: 'Card', desc: 'A content card on the home page.', sel: '.g_card' });
  await S('text-link', q('a').filter({ hasText: /Learn more|Read more/i }).filter({ visible: true }).first(), B4, { group: s, title: 'Text link', desc: 'An in-page text link. Measured, never followed.', sel: 'a "Learn more"' });
  save();
}

async function platform() {
  if (!(await newPage('platform', { wait: 8000 }))) return;
  await sheetsFor('platform');
  await S('platform-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: G.home, title: 'Platform headline', desc: 'The /platform display headline.', sel: 'h1 on /platform' });
  await S('platform-cta', q('a').filter({ hasText: /Start Free Trial|Get a Demo|Free Trial/i }).filter({ visible: true }).first(), B4, { group: G.home, title: 'Platform CTA', desc: 'A platform-page action. Measured, never followed.', sel: 'platform CTA' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing', { wait: 9000 }))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('pricing-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', desc: 'The pricing page headline.', sel: 'h1 on /pricing' });
  await lazySweep();
  await S('price-card', q('.price_chart_category_col').filter({ visible: true }).first(), ['default'], { group: g, title: 'Price card', desc: 'A pricing tier card.', sel: 'pricing card' });
  await S('price-cta', q('a, button').filter({ hasText: /Start Free Trial|Get a Demo|Contact|Talk to/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Price CTA', desc: 'A pricing action. Measured, never followed.', sel: 'pricing CTA' });
  await S('faq-item', q('.faq_accordion, .faq_item, details, [class*="faq"]').filter({ visible: true }).first(), B4.concat(['selected']), { group: g, title: 'FAQ item', desc: 'An FAQ row. Toggled for its open state. Nothing is submitted.', sel: 'faq item' });
  save();
}

async function brand() {
  if (!(await newPage('brand', { wait: 7000 }))) return;
  await S('brand-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: G.brand, title: 'Brand title', desc: 'The /brand page headline.', sel: 'h1 on /brand' });
  await S('brand-download', q('a').filter({ hasText: /Download PNG|All Logos/i }).filter({ visible: true }).first(), B4, { group: G.brand, title: 'Brand download', desc: 'A logo download link on /brand. Measured, never followed.', sel: 'a "Download PNG"' });
  save();
}

async function demo() {
  if (!(await newPage('demo', { wait: 8000 }))) return;
  await sheetsFor('demo');
  const g = G.demo;
  await S('demo-card', q('form.hs-form, form, .hs-form').filter({ visible: true }).first(), ['default'], { group: g, title: 'Demo form', desc: 'The Get a Demo HubSpot form, measured at rest. Nothing was typed or submitted.', sel: 'form on /demo' });
  await S('demo-field', q('input.hs-input[name="email"], input[name="email"], input[type="email"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Demo email field', desc: 'The work-email field. Focused only. Nothing typed, nothing submitted.', sel: 'input[name=email]' });
  await S('demo-submit', q('form input[type="submit"], form button, .hs-button').filter({ visible: true }).first(), B4, { group: g, title: 'Demo submit', desc: 'The form submit. Measured, never pressed.', sel: 'form submit' });
  save();
}

async function signin() {
  if (!(await newPage('signin', { wait: 8000 }))) return;
  await sheetsFor('signin');
  await chrome('signin');
  const g = G.auth;
  const card = await markBiggest('main, form, [class*="card"]', 'm-login', { minW: 240, minH: 160 });
  await S('login-card', card, ['default'], { group: g, title: 'Login card', desc: 'The app.jasper.ai login column. The boundary before the product. Never filled, never submitted, no OAuth followed.', sel: 'login column' }, { noScroll: true });
  await S('login-field', q('input').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Login email field', desc: 'The email field on the login card. Focused only. Nothing typed.', sel: 'login input' });
  await S('login-submit', q('button').filter({ hasText: /Continue with email/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Continue with email', desc: 'The email submit. Measured, never pressed.', sel: 'button "Continue with email"' });
  await S('login-google', q('button').filter({ hasText: /Continue with Google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Continue with Google', desc: 'The Google OAuth button. Measured, never followed.', sel: 'button "Continue with Google"' });
  await S('login-signup', q('button, a').filter({ hasText: /^\s*Sign up\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign up link', desc: 'The Sign up action on the login card. Measured, never followed.', sel: 'Sign up' });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 5000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1200);
  await S('footer', q('.footer_wrap').filter({ visible: true }).first(), ['default'], { group: g, title: 'Footer', desc: 'The site footer: link columns and legal.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('footer a, .footer_wrap a, [class*="footer"] a').filter({ hasText: /\S/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', sel: 'footer a' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('.nav_contain, .nav_wrap').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: '.nav_contain at 390' }, { noScroll: true });
  // At 390 the desktop .nav_menu is display:none and no hamburger mounts.
  // Record the miss honestly; do not click a neighbouring control.
  const menu = q('.nav_menu_button, .w-nav-button, .nav_hamburger, [class*="hamburger"], button[aria-label*="menu" i]').filter({ visible: true }).first();
  const btn = menu;
  await S('m-menu-button', btn, ['default'], { group: g, title: 'Menu button', desc: 'The mobile menu toggle.', sel: 'mobile menu button' }, { noScroll: true });
  try {
    if (await btn.count()) { await btn.click({ timeout: 5000 }).catch(() => btn.evaluate((el) => el.click())); await page.waitForTimeout(1400); }
  } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  await S('m-menu-open', q('.nav_overlay, .w-nav-menu, .nav_menu, .nav_dropdown').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The mobile nav panel opened by its own toggle.', sel: 'mobile menu open' }, { noScroll: true });
  await S('m-nav-item', q('.nav_menu a, .w-nav-menu a, a').filter({ hasText: /Platform|Pricing|Log In/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile nav item', desc: 'An item inside the opened mobile menu.', sel: 'mobile nav item' }, { noScroll: true });
  await page.keyboard.press('Escape').catch(() => {});
  await page.waitForTimeout(400);
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', sel: 'h1 at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844). Marketing pages paint light, with .u-theme-dark islands. The login card is app.jasper.ai at rest.';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, platform, pricing, brand, demo, signin, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  if (!pages.length || pages.includes('home')) await reducedMotion('home', '.nav_contain');
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    if (!touched.has(key) && !pages.length && !failedPages.has(c.page)) { delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close();
}
console.log('components-computed.json:', Object.keys(out.components).length, 'components');
