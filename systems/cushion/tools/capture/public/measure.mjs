// Measures cushion.so's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs PYTHON=<venv python3> node measure.mjs [page ...]
//
// Pages: home pricing updates blog slackalt terms mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// cushion.so is a Tailwind marketing site for an async-messaging app; the
// page paints one light theme. Specs select by Tailwind utility class
// fragments, role, aria-label or text. "Log in", "Sign up", "Get started",
// "Talk to a human" and every outbound link are measured, never followed;
// the FAQ accordion is a local toggle.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, styleOfSelector, crop, cropSelector, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => { fs.mkdirSync(RAW, { recursive: true }); fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n'); };
const URLS = { home: '/', pricing: '/pricing', updates: '/updates', blog: '/blog', slackalt: '/slack-alternative', terms: '/terms' };
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
    await open(page, url || (/^https?:/.test(URLS[key]) ? URLS[key] : BASE + URLS[key]), { wait, promo });
    ok = !(await blocked());
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
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again|order( free)?( sample)?|add to cart|buy now|buy font|go to the platform|get a demo|get demo|contact sales|send message)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
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
  shell: 'Shell and navigation', home: 'Home', pricing: 'Pricing',
  updates: 'Updates', blog: 'Blog', terms: 'Legal', mobile: 'Mobile (390 wide)',
};

// Marks the embedded app mock frame: the smallest ancestor of the "New post"
// button that paints a border, ring or shadow (the mock window chrome).
async function markMock() {
  await page.evaluate(() => {
    const btn = [...document.querySelectorAll('button, a')].find((b) => /^\s*New post\s*$/i.test(b.innerText || ''));
    let best = null;
    for (let el = btn; el; el = el.parentElement) {
      const r = el.getBoundingClientRect(); const cs = getComputedStyle(el);
      if (r.width > 500 && r.height > 400 && (cs.borderTopWidth !== '0px' || cs.boxShadow !== 'none' || cs.borderTopLeftRadius !== '0px')) { best = el; break; }
    }
    // No fallback to the button's parent or the body: a miss is recorded as missing, never a guessed frame.
    if (best) best.setAttribute('data-m-mark', 'mock');
  });
}

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('nav-bar', q('nav').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav bar', desc: 'The 72px sticky top nav (Pricing / Updates / Blog / Log in / Sign up).', sel: 'nav.sticky' }, { noScroll: true });
  await S('nav-logo', q('nav a').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav logo', desc: 'The Cushion wordmark link.', sel: 'nav a' }, { noScroll: true });
  await S('nav-link', q('nav a').filter({ hasText: /^\s*Pricing\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A 40px nav link (Pricing); measured, never followed.', sel: 'nav a' }, { noScroll: true });
  await S('nav-login', q('nav a').filter({ hasText: /^\s*Log in\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Login link', desc: '"Log in" — the header auth link; measured, never followed.', sel: 'nav a' }, { noScroll: true });
  await S('signup-btn', q('nav a, nav button').filter({ hasText: /^\s*Sign up\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-up button', desc: '"Sign up" — the 91x40 #00a6f4 nav CTA; measured, never followed.', sel: 'nav a.signup' }, { noScroll: true });
  const h = G.home;
  await S('hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero heading', desc: '"Work messaging that keeps your team organised" — the 60px Inter Tight hero.', sel: 'h1' }, { noScroll: true });
  await S('hero-sub', q('p').filter({ hasText: /async messaging app/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero subhead', desc: '"Cushion is the async messaging app for small, distributed teams."', sel: 'hero p' }, { noScroll: true });
  await S('cta-start', q('a, button').filter({ hasText: /^\s*Get started\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Get-started CTA', desc: '"Get started" — the 119x44 #00a6f4 primary CTA; measured, never followed.', sel: 'a.cta' }, { noScroll: true });
  await S('cta-human', q('a, button').filter({ hasText: /talk to a human/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Secondary CTA', desc: '"Talk to a human" — the 154x44 #fcfcfc secondary CTA; measured, never followed.', sel: 'a.cta-secondary' }, { noScroll: true });
  await S('problem-h2', q('h2[class*="max-w-prose"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Problem heading', desc: '"Workspace messaging is broken" — the animated problem statement.', sel: 'h2.max-w-prose' });
  await S('feature-h2', q('h2').filter({ hasText: /collaborate without the chaos/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Feature heading', desc: '"Collaborate without the chaos" — the feature section heading.', sel: 'h2' });
  // The embedded app mock ("Acme Inc" inbox) is a real rendered component.
  await markMock();
  await S('mock-frame', q('[data-m-mark="mock"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'App mock frame', desc: 'The embedded "Acme Inc" inbox product mock.', sel: 'app mock frame' });
  await S('mock-newpost', q('button').filter({ hasText: /^\s*New post\s*$/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Mock: New post', desc: 'The mock inbox "New post" button (209x32).', sel: 'mock button' });
  await S('mock-channel', q('button:has-text("Engineering")').filter({ visible: true }).first(), B4, { group: h, title: 'Mock: channel', desc: 'A mock sidebar channel button (209x32).', sel: 'mock channel button' });
  await S('mock-post', q('article[class*="group"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Mock: post card', desc: 'A mock post card in the inbox mock (606x108).', sel: 'article.group' });
  await S('mock-post-bar', q('footer').filter({ hasText: /Save|Post/ }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Mock: post footer', desc: 'The mock post action bar ("Save for later" / "Post").', sel: 'mock footer' });
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The 1240x184 link-columns footer band.', sel: 'footer' });
  await S('footer-link', q('footer a').filter({ hasText: /privacy/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', desc: 'A footer link (Privacy); measured, never followed.', sel: 'footer a' });
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('pricing-h2', q('h2').filter({ hasText: /everything you need/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing heading', desc: '"Everything you need for just $8/mo/user."', sel: 'pricing h2' }, { noScroll: true });
  await S('plan-panel', q('div[class*="bg-gray-1"][class*="rounded-2xl"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan panel', desc: 'The single-plan panel ($8/mo/user + 30-day trial copy).', sel: 'div.bg-gray-1' });
  await S('pricing-cta', q('a, button').filter({ hasText: /^\s*Get started\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Pricing CTA', desc: '"Get started" — the pricing-page CTA; measured, never followed.', sel: 'pricing cta' });
  await S('faq-item', q('button[aria-expanded]').filter({ visible: true }).first(), ['default', 'opened'], { group: g, title: 'FAQ item', desc: 'A FAQ accordion row ("How\'s this different from Slack?"); opened and closed locally.', sel: 'button[aria-expanded]' });
}

async function updates() {
  if (!(await newPage('updates'))) return;
  await sheetsFor('updates');
  await chrome('updates');
  const g = G.updates;
  await S('update-entry', q('article[class*="md:flex-row"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Update entry', desc: 'A changelog entry (date + items, ~1024x1719).', sel: 'article.md:flex-row' });
  await S('update-h2', q('article h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Update title', desc: 'A release title ("Post Redesign, Slack Sync Upgrades, and more").', sel: 'article h2' });
  await S('update-h3', q('article h3').filter({ visible: true }).first(), ['default'], { group: g, title: 'Update item', desc: 'A release item heading.', sel: 'article h3' });
}

async function blog() {
  if (!(await newPage('blog'))) return;
  await sheetsFor('blog');
  await chrome('blog');
  const g = G.blog;
  await S('blog-featured', q('article').filter({ visible: true }).first(), B4, { group: g, title: 'Featured post', desc: 'The featured blog row (1240x339); measured, never followed.', sel: 'article' });
  await S('blog-card', q('article[class*="rounded-xl"]').filter({ visible: true }).first(), B4, { group: g, title: 'Blog card', desc: 'A 397x403 post card; measured, never followed.', sel: 'article.rounded-xl' });
  await S('blog-card-title', q('article h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Card title', desc: 'A post card title (text-lg).', sel: 'article h2' });
}

async function slackalt() {
  if (!(await newPage('slackalt'))) return;
  await sheetsFor('slackalt');
  await chrome('slackalt');
  const g = G.home;
  await S('cmp-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Comparison heading', desc: '"The best Slack alternative for async teams".', sel: 'h1' }, { noScroll: true });
  await S('cmp-article', q('article').filter({ visible: true }).first(), ['default'], { group: g, title: 'Comparison section', desc: 'A comparison page section/article.', sel: 'article' });
}

async function terms() {
  if (!(await newPage('terms'))) return;
  const g = G.terms;
  await S('legal-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Legal heading', desc: '"Terms of Service" — the legal page heading.', sel: 'h1' }, { noScroll: true });
  await S('legal-body', q('article p, main p, p').filter({ visible: true }).first(), ['default'], { group: g, title: 'Legal paragraph', desc: 'A body paragraph of the terms text.', sel: 'legal p' });
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  await S('m-nav-bar', q('nav').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile nav', sel: 'nav at 390' }, { noScroll: true });
  await S('m-hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero', desc: 'The hero at 390px.', sel: 'h1 at 390' }, { noScroll: true });
  await S('m-cta-start', q('a, button').filter({ hasText: /^\s*Get started\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile CTA', desc: '"Get started" at 390px; measured, never followed.', sel: 'cta at 390' }, { noScroll: true });
}

run = new Date().toISOString().slice(0, 10);
run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); cushion.so paints a single light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, updates, blog, slackalt, terms, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that transitions (a nav button's
  // hover), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'nav a');
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
