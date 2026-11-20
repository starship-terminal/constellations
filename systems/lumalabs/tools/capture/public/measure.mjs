// Measures lumalabs.ai's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing about api ray news enterprise mobile.
// Writes raw/components-computed.json and one crop per component and state.
//
// Sign In, Try for free, Start Now, Use the API, Subscribe and the enterprise
// form Submit are measured, never followed. The home prompt is filled and
// cleared, never submitted. Pricing interval, news filters, FAQ and the
// mobile nav are local toggles. Consent overlays are hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, patch, open, closePromo, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => { fs.mkdirSync(RAW, { recursive: true }); fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n'); };
const URLS = {
  home: '/', pricing: '/pricing', about: '/about', api: '/api', ray: '/ray',
  news: '/news', enterprise: '/enterprise',
};
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes blocked this run: components last measured on them keep their
// earlier readings instead of being pruned below (a blocked pass must never
// erase evidence).
const failedPages = new Set();

async function blocked() {
  return page.evaluate(() => {
    const t = (document.body && document.body.innerText) || '';
    return /client challenge|performing security verification|verifying you are human|just a moment|access denied|unusual activity from your computer network|not a robot|you have been blocked|unable to access|a required part of this site/i.test(t + ' ' + document.title) || t.trim().length < 40;
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
  // Cloudflare Turnstile can greet a route: wait it out, then one retry on a
  // fresh context before recording the route as blocked this run.
  let ok = false;
  for (let tries = 0; tries < 2 && !ok; tries++) {
    const opened = await open(page, url || (/^https?:/.test(URLS[key]) ? URLS[key] : BASE + URLS[key]), { wait, promo })
      .catch((e) => { log('  open failed', key, String(e.message || e).slice(0, 120)); return false; });
    ok = opened && !(await blocked());
    if (!ok && tries === 0) { log('  challenge, one reload', key); }
  }
  if (!ok) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); liveCtx = null; return false; }
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
  Object.assign(c, { page: current, run, url: /^https?:/.test(URLS[current] || '') ? URLS[current] : BASE + (URLS[current] || '') }, meta);
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
  await loc.waitFor({ state: 'visible', timeout: 6000 }).catch(() => {});
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
const NEVER = /^(send|submit|sign in|sign up|try for free|try free|try now for free|start now|use the api|get started|subscribe|buy|purchase|pay|checkout|join|apply|accept|reject|continue|contact sales|generate|create account)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

// Variant of S() for routes whose Playwright locators never resolve.
// curater.org/taste client-side redirected to /taste/soon and the navigation
// never settles: locators count matches, but every resolve dies with the
// execution context. Measuring the default state through the main world
// (same styleOf reader + clip crop) instead of locators.
async function SJ(key, sel, meta = {}, opts = {}) {
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: sel });
  delete out.components[key].missing;
  const found = await page.evaluate((pick) => !!eval(pick), sel.startsWith('js:') ? sel.slice(3) : `document.querySelector(${JSON.stringify(sel)})`);
  if (!found) { out.components[key].missing = true; log('  ! missing', key); return; }
  try {
    const s = await styleOfSelector(page, sel);
    if (!s) throw new Error('element not found');
    let file;
    if (opts.crop !== false) {
      try { file = await cropSelector(page, sel, `${key}-default`, opts.pad ?? 8); }
      catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    out.components[key].states.default = { ...s, crop: file, via: 'main-world query (locators never settle on this route)' };
    log('  ', key, 'default', s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    out.components[key].states.default = { error: String(e.message || e).slice(0, 200) };
    log('  !', key, 'default', String(e.message).slice(0, 120));
  }
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

// Scrolls the page down in steps and back to the top: lazy-mounted sections
// only enter the DOM once scrolled into view.
async function lazyLoad() {
  await page.evaluate(async () => {
    const h = document.documentElement.scrollHeight;
    for (let y = 0; y <= h; y += 800) { scrollTo(0, y); await new Promise((r) => setTimeout(r, 120)); }
    scrollTo(0, 0);
  });
  await page.waitForTimeout(1600);
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
    await p.goto(URLS[key] ? (/^https?:/.test(URLS[key]) ? URLS[key] : BASE + URLS[key]) : BASE, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
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
  shell: 'Marketing shell', home: 'Home', pricing: 'Pricing',
  about: 'About', api: 'API', ray: 'Ray', news: 'News',
  enterprise: 'Enterprise', mobile: 'Phone (390 wide)',
};

const FIELD = ['default', 'focused', 'filled'];

async function home() {
  if (!(await newPage('home', { wait: 4000 }))) return;
  await sheetsFor('home');
  const g = G.shell;
  await S('nav-product', q('a[href="/app"]').first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Nav link', desc: 'The PRODUCT nav link. It points at /app, a marketing route, not the signed-in app. Uppercase Graphik label.', sel: 'a[href="/app"]' }, { noScroll: true });
  await S('nav-signin', q('a[href*="app.lumalabs.ai"]').filter({ hasText: /Sign In/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign In', desc: 'The header Sign In pill. It links to app.lumalabs.ai, which redirects to the sign-up host. Measured, never followed.', sel: 'a Sign In' }, { noScroll: true });
  await S('hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: G.home, title: 'Hero heading', desc: 'The home hero heading.', sel: 'h1' }, { noScroll: true });
  await S('hero-cta', q('a').filter({ hasText: /Try for free/ }).filter({ visible: true }).first(), B4, { group: G.home, title: 'Try for free', desc: 'The hero pill. Links to the app host. Measured, never followed. Following it is a sign-in.', sel: 'Try for free' });
  await S('prompt', q('textarea, [contenteditable="true"]').filter({ visible: true }).first(), FIELD, { group: G.home, title: 'Prompt field', desc: 'The home prompt. Sample text is typed and deleted. Submit is never pressed.', sel: 'textarea' }, { fillText: 'a ceramic cup on a table' });
  await S('prompt-submit', q('button[aria-label="Submit prompt"]').first(), ['default', 'hover'], { group: G.home, title: 'Submit prompt', desc: 'The prompt submit control. Measured at rest and hover only. Never clicked, so no generation is started.', sel: 'button[aria-label=Submit prompt]' });
  await S('idea-chip', q('button').filter({ hasText: /Product Hero Shots/ }).filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: G.home, title: 'Idea chip', desc: 'A suggested-prompt chip. A local control. It was not used to submit a prompt.', sel: 'Product Hero Shots' });
  await S('footer-link', q('footer a').filter({ hasText: /Pricing/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Footer link', desc: 'A footer text link.', sel: 'footer a Pricing' });
}

async function pricing() {
  if (!(await newPage('pricing', { wait: 3500 }))) return;
  const g = G.pricing;
  await S('price-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing heading', desc: 'Plans and Pricing heading.', sel: 'h1' }, { noScroll: true });
  await S('price-monthly', q('button').filter({ hasText: /^Monthly$/ }).filter({ visible: true }).first(), ['default', 'hover', 'pressed'], { group: g, title: 'Monthly', desc: 'The billing-interval button. A local toggle. Checkout is never opened.', sel: 'Monthly' }, { noScroll: true });
  await S('price-yearly', q('button').filter({ hasText: /^Yearly$/ }).filter({ visible: true }).first(), ['default', 'hover', 'pressed'], { group: g, title: 'Yearly', desc: 'The yearly interval button. A local toggle.', sel: 'Yearly' }, { noScroll: true });
  await S('price-cta', q('a, button').filter({ hasText: /Start Now/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Start Now', desc: 'A plan CTA. Measured, never followed. Following it is a sign-in and a checkout.', sel: 'Start Now' });
  await S('price-card', q('body'), ['default'], { group: g, title: 'Plan card', desc: 'The Plus plan card. Cropped from the node whose text starts with Plus and whose box is card-sized.', sel: 'Plus card' }, {
    crop: false,
    extra: async () => {
      const handle = await page.evaluateHandle(() => {
        const nodes = [...document.querySelectorAll('div')].filter((el) => {
          const t = (el.innerText || '').trim();
          if (!t.startsWith('Plus')) return false;
          const r = el.getBoundingClientRect();
          return r.width > 180 && r.width < 520 && r.height > 180 && r.height < 900;
        });
        nodes.sort((a, b) => a.getBoundingClientRect().width * a.getBoundingClientRect().height - b.getBoundingClientRect().width * b.getBoundingClientRect().height);
        return nodes[0] || null;
      });
      const el = handle.asElement();
      if (!el) return { missing: true };
      const file = await crop(page, el, 'price-card-default', 8);
      const box = await el.boundingBox();
      // The S() target is body, so the state's own style is the page's. The card's computed style
      // goes in extra.card, which build_components_md.py reads in place of the body reading.
      return { crop: file, box, card: await styleOf(el) };
    },
  });
  await S('faq', q('button, [role="button"]').filter({ hasText: /What is Luma/ }).filter({ visible: true }).first(), ['default', 'hover', 'opened'], { group: g, title: 'FAQ row', desc: 'A pricing FAQ button. A local toggle. Nothing is submitted.', sel: 'FAQ' });
}

async function about() {
  if (!(await newPage('about', { wait: 3000 }))) return;
  const g = G.about;
  await S('about-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'About heading', desc: 'The about page heading.', sel: 'h1' }, { noScroll: true });
  await S('about-faq', q('button').filter({ hasText: /What is Luma\?/ }).filter({ visible: true }).first(), ['default', 'hover', 'opened'], { group: g, title: 'About FAQ', desc: 'An about FAQ button. A local toggle.', sel: 'What is Luma?' });
}

async function api() {
  if (!(await newPage('api', { wait: 3000 }))) return;
  const g = G.api;
  await S('api-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'API heading', desc: 'Build with Luma APIs.', sel: 'h1' }, { noScroll: true });
  await S('api-cta', q('a, button').filter({ hasText: /Use the API/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Use the API', desc: 'The API CTA. Measured, never followed. Keys and billing sit behind sign-in.', sel: 'Use the API' });
  await S('api-tab', q('button').filter({ hasText: /^Uni-1\.1$/ }).filter({ visible: true }).first(), ['default', 'hover', 'pressed'], { group: g, title: 'Model tab', desc: 'A model switch on the API page. A local toggle.', sel: 'Uni-1.1' });
  await S('api-docs', q('a').filter({ hasText: /Explore docs/ }).filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Explore docs', desc: 'The docs link. Measured, never followed from this page. Docs were captured as their own route.', sel: 'Explore docs' });
}

async function ray() {
  if (!(await newPage('ray', { wait: 3500 }))) return;
  const g = G.ray;
  await S('ray-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Ray heading', desc: 'The Ray3.2 page heading on the dark field.', sel: 'h1' }, { noScroll: true });
  await S('ray-faq', q('button').filter({ hasText: /What Is Ray3\.2\?/ }).filter({ visible: true }).first(), ['default', 'hover', 'opened'], { group: g, title: 'Ray FAQ', desc: 'A Ray FAQ button. A local toggle.', sel: 'What Is Ray3.2?' });
}

async function news() {
  if (!(await newPage('news', { wait: 3000 }))) return;
  const g = G.news;
  await S('news-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'News heading', desc: 'The news index heading.', sel: 'h1' }, { noScroll: true });
  await S('news-filter', q('button').filter({ hasText: /^Product$/ }).filter({ visible: true }).first(), ['default', 'hover', 'pressed'], { group: g, title: 'News filter', desc: 'A news category filter. A local toggle. Subscribe was not clicked.', sel: 'Product' });
  await S('news-card', q('a[href*="/news/"], a[href*="/blog/"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'News card', desc: 'A published news card. A public article link.', sel: 'news card' });
}

async function enterprise() {
  if (!(await newPage('enterprise', { wait: 3000 }))) return;
  const g = G.enterprise;
  await S('ent-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Enterprise heading', desc: 'The enterprise page heading.', sel: 'h1' }, { noScroll: true });
  await S('ent-field', q('input[type="email"], input[type="text"], input:not([type])').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Enterprise field', desc: 'A field on the enterprise form. Focused only. Nothing is typed that would be submitted, and Submit is never clicked.', sel: 'input' });
  await S('ent-submit', q('button').filter({ hasText: /^Submit$/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Enterprise submit', desc: 'The enterprise form submit. Measured at rest and hover. Never clicked, so no sales form is sent.', sel: 'Submit' });
}

async function mobile() {
  if (!(await newPage('home', { mobile: true, wait: 4000 }))) return;
  const g = G.mobile;
  await S('m-menu', q('header button, button[aria-label*="menu" i]').filter({ visible: true }).last(), ['default', 'hover', 'pressed', 'opened'], { group: g, title: 'Phone menu', desc: 'The mobile navigation toggle at 390px. A local control. Sign In inside it is not followed.', sel: 'header menu button' }, { noScroll: true });
  await S('m-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Phone heading', desc: 'The home heading at 390px.', sel: 'h1' }, { noScroll: true });
  await S('m-signin', q('a').filter({ hasText: /Sign In/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Phone Sign In', desc: 'Sign In at 390px. Measured, never followed.', sel: 'Sign In' }, { noScroll: true });
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (phone group 390 x 844); inner pages paint light, the home hero and /ray paint dark';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, about, api, ray, news, enterprise, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'a[href="/pricing"]');
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    if (!touched.has(key) && !pages.length && !failedPages.has(c.page)) { delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close();
}
