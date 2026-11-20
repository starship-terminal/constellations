// Measures krea.ai's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing enterprise blog plugins login image mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// krea.ai paints a dark app shell (html.dark, Suisse Intl) signed out.
// Sign in, Sign up, Log in, Continue with Google/Apple/SSO/Email, Book a call
// and every generate/checkout control are measured, never followed. The Tools
// menu, sidebar toggle, pricing interval and FAQ summaries are local toggles.
// No form is submitted. /assets redirects to /login and is recorded as a gate.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, styleOfSelector, crop, cropSelector, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => { fs.mkdirSync(RAW, { recursive: true }); fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n'); };
const URLS = {
  home: '/', pricing: '/pricing', enterprise: '/enterprise', blog: '/blog',
  plugins: '/plugins', login: '/login', image: '/image',
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
    ok = (await open(page, url || (/^https?:/.test(URLS[key]) ? URLS[key] : BASE + URLS[key]), { wait, promo })) && !(await blocked());
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
  // fillText is an option for the filled state; several specs pass it with the record fields.
  if (meta.fillText && !opts.fillText) opts = { ...opts, fillText: meta.fillText };
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
const NEVER = /^(send|submit|sign in|sign up|sign up for free|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|continue with google|continue with apple|continue with email|single sign-on \(sso\)|book a call|contact sales|generate|create account)$/i;
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
  shell: 'App shell', home: 'Home feed', pricing: 'Pricing',
  enterprise: 'Enterprise', blog: 'Blog', plugins: 'Plugins',
  login: 'Login boundary', image: 'Image tool (signed out)',
  mobile: 'Mobile (390 wide)',
};

const FIELD = ['default', 'focused', 'filled'];

async function home() {
  if (!(await newPage('home', { wait: 5000 }))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('sidebar', q('[data-m-mark="sidebar"]'), ['default'], { group: g, title: 'Sidebar', desc: 'The signed-out app sidebar: Home, Agent, Train, Nodes, Assets, tool links, Pricing, Enterprise, Sign in. About 256px, near-black.', sel: 'sidebar' }, { noScroll: true, open: async () => {
    await page.evaluate(() => {
      const home = document.querySelector('a[aria-label="Home"]');
      if (!home) return;
      let el = home.parentElement;
      for (let i = 0; i < 8 && el; i++, el = el.parentElement) {
        const r = el.getBoundingClientRect();
        if (r.x < 8 && r.width > 200 && r.width < 360 && r.height > 600) {
          el.setAttribute('data-m-mark', 'sidebar');
          return;
        }
      }
    });
  } });
  await S('sidebar-toggle', page.getByRole('button', { name: 'Toggle Sidebar' }).first(), B4, { group: g, title: 'Sidebar toggle', desc: 'The "Toggle Sidebar" icon button. A local fold control.', sel: 'button[aria-label="Toggle Sidebar"]' }, { noScroll: true });
  await S('nav-home', page.getByRole('link', { name: 'Home', exact: true }).first(), B4, { group: g, title: 'Sidebar home link', desc: 'The Home item in the sidebar. Selected at rest (data-active).', sel: 'a[aria-label="Home"]' }, { noScroll: true });
  await S('nav-pricing', q('a[href="/pricing"]').filter({ visible: true }).first(), B4, { group: g, title: 'Pricing link', desc: 'The sidebar Pricing link, including the yearly-discount badge. Measured, never followed from this spec.', sel: 'a[href="/pricing"]' }, { noScroll: true });
  await S('nav-signin', page.getByRole('button', { name: 'Sign in', exact: true }).first(), B4, { group: g, title: 'Sign in', desc: 'The white sidebar Sign in button. Measured, never followed. It opens /login.', sel: 'button Sign in' }, { noScroll: true });
  await S('tools-button', page.getByRole('button', { name: 'Tools', exact: true }).first(), [...B4, 'opened'], { group: g, title: 'Tools menu button', desc: 'The Tools button that opens the tool list. A local menu toggle.', sel: 'button Tools' }, { noScroll: true });
  await S('search-button', page.getByRole('button', { name: 'Search', exact: true }).first(), B4, { group: g, title: 'Search button', desc: 'The sidebar Search control. Measured at rest. Opening the command palette and submitting a query are not done here.', sel: 'button Search' }, { noScroll: true });
  const h = G.home;
  await S('promo-banner', q('[class*="banner"], a[href="/pricing"]').filter({ hasText: /Claim offer|Unlimited/ }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Offer banner', desc: 'The top offer strip ("Unlimited Nano Banana for 7 days"). A campaign surface, hidden from other shots by closePromo when it is a dismiss overlay. Measured, never claimed.', sel: 'offer banner' }, { noScroll: true });
  await S('feed-card', q('a[href^="/feed/"]').filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'Feed card', desc: 'A published generation card on the signed-out home feed. A public demo, not a signed-in asset.', sel: 'a[href^="/feed/"]' });
  await S('announce-card', q('button, a').filter({ hasText: /Try Krea 3|Read more/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'Announcement card', desc: 'A model-announcement card on the home feed.', sel: 'announcement' });
  await S('composer', q('textarea, [contenteditable="true"]').filter({ visible: true }).first(), FIELD, { group: h, title: 'Home composer', desc: 'The signed-out prompt ("Describe an idea or upload an image to edit it"). Sample text is typed and deleted. The generate control is never pressed.', sel: 'textarea', fillText: 'a red square' });
  await S('composer-send', page.getByRole('button', { name: 'Generate', exact: true }).first(), ['default', 'hover'], { group: h, title: 'Composer generate', desc: 'The circular Generate control on the home composer (aria-label Generate). Measured, never clicked. Sending a prompt is a gated generation.', sel: 'button[aria-label="Generate"]' });
}

async function pricing() {
  if (!(await newPage('pricing', { wait: 5000 }))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('mkt-nav', q('header, nav').filter({ hasText: /Pricing/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Marketing nav', desc: 'The pricing-page top nav: App, Features, Plugins, Image, Video, API, MCP, Pricing, Enterprise, Sign up, Log in.', sel: 'header' }, { noScroll: true });
  await S('mkt-login', q('button, a').filter({ hasText: /^Log in$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Log in', desc: 'The marketing Log in control. Measured, never followed. Destination is /login.', sel: 'Log in' }, { noScroll: true });
  await S('mkt-signup', q('button, a').filter({ hasText: /Sign up for free/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign up for free', desc: 'The marketing Sign up control. Measured, never followed.', sel: 'Sign up for free' }, { noScroll: true });
  await S('price-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing heading', desc: '"Pick your plan".', sel: 'h1' }, { noScroll: true });
  await S('price-card', q('[data-m-mark="price-card"]'), ['default'], { group: g, title: 'Free plan card', desc: 'The Free plan column on /pricing: $0/month, Get Free.', sel: 'plan card' }, { open: async () => {
    await page.evaluate(() => {
      const btn = [...document.querySelectorAll('button, a')].find((b) => /^Get Free$/.test((b.innerText || '').trim()));
      if (!btn) return;
      let el = btn;
      for (let i = 0; i < 8 && el.parentElement; i++) {
        el = el.parentElement;
        const r = el.getBoundingClientRect();
        if (r.width > 180 && r.width < 420 && r.height > 180 && r.height < 520) {
          el.setAttribute('data-m-mark', 'price-card');
          return;
        }
      }
    });
  } });
  await S('price-pro', q('h2, h3').filter({ hasText: /^Pro$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Pro plan heading', desc: 'The Pro plan name.', sel: 'h2 Pro' });
  await S('price-interval', q('button').filter({ hasText: /year|month/i }).filter({ visible: true }).first(), ['default', 'hover', 'pressed'], { group: g, title: 'Billing interval', desc: 'The monthly/yearly toggle on pricing. A local UI toggle, never a checkout.', sel: 'interval button' });
  await S('price-cta', page.getByRole('button', { name: 'Get Pro', exact: true }).first(), B4, { group: g, title: 'Get Pro', desc: 'The Pro plan button. Measured, never followed. Checkout and account creation sit behind this control.', sel: 'button Get Pro' });
  await S('price-badge', page.getByText('40% off', { exact: true }).first(), ['default'], { group: g, title: 'Yearly discount badge', desc: 'The blue "40% off" chip on the Yearly interval.', sel: '40% off' }, { noScroll: true });
  await S('price-popular', q('span, div').filter({ hasText: /^Most popular$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Most popular badge', desc: 'The badge on the Pro card.', sel: 'Most popular' });
  await S('faq-item', q('button, summary, [role="button"]').filter({ hasText: /\?$/ }).filter({ visible: true }).first(), ['default', 'opened', 'focus-visible'], { group: g, title: 'FAQ row', desc: 'A pricing FAQ summary. Opened with its own toggle.', sel: 'faq button' });
}

async function enterprise() {
  if (!(await newPage('enterprise', { wait: 5000 }))) return;
  const g = G.enterprise;
  await S('ent-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Enterprise heading', desc: 'The enterprise hero heading.', sel: 'h1' }, { noScroll: true });
  await S('ent-cta', q('a, button').filter({ hasText: /Book a call/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Book a call', desc: 'The sales CTA. Measured, never followed. The booking form is a gated surface.', sel: 'Book a call' }, { noScroll: true });
}

async function blog() {
  if (!(await newPage('blog', { wait: 4000 }))) return;
  const g = G.blog;
  await S('blog-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Blog heading', desc: 'The blog index heading.', sel: 'h1' }, { noScroll: true });
  await S('blog-card', q('a').filter({ hasText: /Read/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Blog card', desc: 'A published blog card. Measured, not opened in this pass.', sel: 'blog a' });
}

async function plugins() {
  if (!(await newPage('plugins', { wait: 4000 }))) return;
  const g = G.plugins;
  await S('plug-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plugins heading', desc: 'The plugins marketing heading.', sel: 'h1' }, { noScroll: true });
  await S('plug-link', q('a[href*="/plugins/"]').filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Plugin link', desc: 'A plugin product link. Measured, never followed into an install flow.', sel: 'a[href*="/plugins/"]' });
}

async function login() {
  if (!(await newPage('login', { wait: 3000 }))) return;
  const g = G.login;
  await S('login-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Login heading', desc: '"Welcome to Krea" / "Log in or sign up". The auth boundary. Nothing is submitted.', sel: 'h1' }, { noScroll: true });
  await S('login-google', q('button').filter({ hasText: /Continue with Google/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Continue with Google', desc: 'OAuth button. Measured, never clicked through. Following it is an OAuth flow.', sel: 'Continue with Google' }, { noScroll: true });
  await S('login-apple', q('button').filter({ hasText: /Continue with Apple/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Continue with Apple', desc: 'OAuth button. Measured, never followed.', sel: 'Continue with Apple' }, { noScroll: true });
  await S('login-sso', q('button').filter({ hasText: /Single Sign-On/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'SSO', desc: 'SSO button. Measured, never followed.', sel: 'SSO' }, { noScroll: true });
  await S('login-email', q('input[type="email"], input[name="email"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field', desc: 'The email field on the login boundary. Sample text is typed and deleted. Enter is never pressed, and Continue with Email is never clicked.', sel: 'input[type=email]', fillText: 'name@example.com' }, { noScroll: true });
  await S('login-email-btn', q('button').filter({ hasText: /Continue with Email/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Continue with Email', desc: 'The email submit control. Measured at rest and hover only. Never clicked, so no account is created and no code is sent.', sel: 'Continue with Email' }, { noScroll: true });
  await S('login-terms', q('a[href="/terms"]').filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Terms link', desc: 'The Terms of Service link on the login page.', sel: 'a[href="/terms"]' }, { noScroll: true });
}

async function image() {
  if (!(await newPage('image', { wait: 4500 }))) return;
  const g = G.image;
  await S('image-shell', q('main, [role="main"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Image tool shell', desc: 'The signed-out /image tool. Generation is gated: the prompt is measured if present, never submitted.', sel: 'main' }, { noScroll: true });
  await S('image-prompt', q('textarea, input[placeholder]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Prompt field', desc: 'The image prompt, if the signed-out page paints one. Sample text is typed and deleted. Generate is never pressed.', sel: 'textarea', fillText: 'a red square' }, { noScroll: true });
  await S('image-generate', page.getByRole('button', { name: 'Generate', exact: true }).first(), ['default', 'hover'], { group: g, title: 'Generate', desc: 'The generate control on /image (aria-label Generate). Measured, never clicked. Submitting a generation is a gated action.', sel: 'button[aria-label="Generate"]' }, { noScroll: true });
}

async function mobile() {
  if (!(await newPage('home', { mobile: true, wait: 5000 }))) return;
  const g = G.mobile;
  await S('m-sidebar', q('nav, aside').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile shell', desc: 'The app shell at 390px.', sel: 'nav at 390' }, { noScroll: true });
  await S('m-menu', q('button').filter({ hasText: /Toggle Sidebar|menu/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile menu button', desc: 'The sidebar toggle at 390px. A local control.', sel: 'Toggle Sidebar' }, { noScroll: true });
  await S('m-signin', q('button, a').filter({ hasText: /^Sign in$/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: g, title: 'Mobile Sign in', desc: 'Sign in at 390px. Measured, never followed.', sel: 'Sign in' }, { noScroll: true });
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); krea.ai paints html.dark on the public app';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, enterprise, blog, plugins, login, image, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that transitions (a nav link's hover),
  // so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'a[href="/pricing"]');
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
