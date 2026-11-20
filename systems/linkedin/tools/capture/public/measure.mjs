// Measures linkedin.com's public guest components without signing in or
// submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home jobs company profile legal signin mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// The guest site paints one light theme. Sign in, Join now, Apply, Follow,
// Message and Easy Apply are measured, never followed. No form is submitted.
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
  home: '/',
  jobs: '/jobs/search/?keywords=designer&location=United%20States&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
  company: '/company/linkedin',
  profile: '/in/reidhoffman',
  legal: '/legal/user-agreement',
  signin: '/login',
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

// Playwright string hasText is a substring. The guest home paints "New to
// LinkedIn? Join now" and "Sign in with email", so the element's own text
// must match the label and nothing else.
function exact(sel, label) {
  const re = new RegExp(`^\\s*${label.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}\\s*$`);
  return q(sel).filter({ hasText: re }).filter({ visible: true });
}

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
  shell: 'Shell and navigation', home: 'Guest home', jobs: 'Jobs search',
  company: 'Company page', profile: 'Public profile', legal: 'Legal',
  signin: 'Sign-in wall', mobile: 'Mobile (390 wide)',
};

const FIELD = ['default', 'focused', 'filled'];

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('header-nav', q('header, nav').filter({ has: exact('a', 'Join now') }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Guest nav', desc: 'The guest header: logo, Top Content, People, Learning, Jobs, Games, Sign in, Join now.', sel: 'header' }, { noScroll: true });
  await S('nav-logo', exact('a', 'LinkedIn'), ['default'], { group: g, title: 'Logo', desc: 'The LinkedIn wordmark in the guest nav. Measured, never followed.', sel: 'a' }, { noScroll: true });
  await S('nav-link', exact('a', 'Jobs'), B4, { group: g, title: 'Nav link', desc: '"Jobs" in the guest nav. A destination link, measured, never followed.', sel: 'a' }, { noScroll: true });
  await S('nav-signin', exact('a', 'Sign in'), B4, { group: g, title: 'Sign in', desc: '"Sign in" secondary-emphasis pill. A sign-in destination, measured, never followed.', sel: 'a' }, { noScroll: true });
  await S('nav-join', exact('a', 'Join now'), B4, { group: g, title: 'Join now', desc: '"Join now" primary pill. A sign-in destination, measured, never followed.', sel: 'a' }, { noScroll: true });
  const h = G.home;
  await S('hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero heading', desc: '"Welcome to your professional community" at text-display-lg (48px).', sel: 'h1' }, { noScroll: true });
  await S('hero-email', exact('a, button', 'Sign in with email'), B4, { group: h, title: 'Sign in with email', desc: '"Sign in with email" outline pill under the hero. A sign-in destination, measured, never followed.', sel: 'a' }, { noScroll: true });
  await S('topic-chip', exact('a, button', 'Career'), B4, { group: h, title: 'Topic chip', desc: 'A topic pill ("Career") in Explore top LinkedIn content. Measured, never followed.', sel: 'a' });
  await S('job-chip', exact('a, button', 'Engineering'), ['default', 'hover', 'focus-visible'], { group: h, title: 'Job category chip', desc: 'A suggested job-search chip. Measured, never followed.', sel: 'a' });
  await S('section-heading', exact('h2', 'Explore top LinkedIn content'), ['default'], { group: h, title: 'Section heading', desc: '"Explore top LinkedIn content", the first section heading on the guest home.', sel: 'h2' });
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The guest footer: legal links and the LinkedIn Corporation line.', sel: 'footer' });
  await S('footer-link', q('footer a').filter({ hasText: /user agreement|privacy policy|about/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', desc: 'A footer legal link. Measured, never followed.', sel: 'footer a' });
}

// The jobs search paints controls inside a virtualized list. Playwright's
// visibility filter misses them; a main-world mark on a painted box does not.
// The predicate is a real function spliced into the evaluated source, so the
// page never calls eval (a CSP without 'unsafe-eval' would reject that).
function markInPage(tag, pred) {
  document.querySelectorAll(`[data-m-mark="${tag}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
  const els = [...document.querySelectorAll('a,button,input,h1,li,div')].filter((el) => {
    const r = el.getBoundingClientRect();
    if (r.width < 8 || r.height < 8 || r.bottom < 0 || r.top > innerHeight) return false;
    const cs = getComputedStyle(el);
    if (cs.visibility === 'hidden' || cs.display === 'none' || Number(cs.opacity) === 0) return false;
    return pred(el, (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').replace(/\s+/g, ' ').trim());
  });
  const el = els.find((n) => !els.some((o) => o !== n && n.contains(o))) || els[0];
  if (!el) return false;
  el.setAttribute('data-m-mark', tag);
  return true;
}

async function mark(tag, pred) {
  const ok = await page.evaluate(`(${markInPage})(${JSON.stringify(tag)}, ${pred})`).catch(() => false);
  return ok ? q(`[data-m-mark="${tag}"]`) : q('[data-m-mark="__none__"]');
}

async function jobs() {
  if (!(await newPage('jobs'))) return;
  await sheetsFor('jobs');
  await chrome('jobs');
  const g = G.jobs;
  await page.evaluate(() => {
    window.scrollTo(0, 0);
    document.querySelectorAll('*').forEach((e) => { if (e.scrollTop) e.scrollTop = 0; });
  });
  await page.waitForTimeout(800);
  await S('jobs-h1', await mark('jobs-h1', (el, t) => el.tagName === "H1" && /Designer Jobs/.test(t)), ['default'], { group: g, title: 'Results heading', desc: 'The jobs-search results heading, as the page painted it for this capture IP.', sel: 'h1' }, { noScroll: true });
  await S('filter-chip', await mark('filter-chip', (el, t) => el.tagName === "BUTTON" && t === "Date posted"), [...B4, 'opened'], { group: g, title: 'Filter chip', desc: '"Date posted" filter chip. Opened as a local dropdown, never submitted.', sel: 'button' }, { noScroll: true });
  await S('job-row', await mark('job-row', (el, t) => el.tagName === "LI" && /Designer/.test(t) && el.getBoundingClientRect().height < 220), ['default', 'hover', 'focus-visible'], { group: g, title: 'Job card', desc: 'A job result card on the public search. Measured, never followed. Apply was not clicked.', sel: 'li' });
  await S('apply-cta', await mark('apply-cta', (el, t) => /^(A|BUTTON)$/.test(el.tagName) && t === "Apply"), B4, { group: g, title: 'Apply', desc: '"Apply" on the job detail pane. A sign-in destination, measured, never followed.', sel: 'button' });
  await S('search-keyword', await mark('search-keyword', (el, t) => el.tagName === "INPUT" && /title|keyword|Search job/i.test((el.getAttribute("aria-label") || "") + " " + (el.getAttribute("placeholder") || "") + " " + t)), ['default'], { group: g, title: 'Keyword field', desc: 'The jobs keyword field, when it is painted. Nothing was typed or submitted on this pass.', sel: 'input' }, { noScroll: true });
}

async function company() {
  if (!(await newPage('company'))) return;
  await sheetsFor('company');
  await chrome('company');
  const g = G.company;
  await S('company-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Company name', desc: 'The public company page title.', sel: 'h1' }, { noScroll: true });
  await S('company-follow', exact('button, a', 'Follow'), B4, { group: g, title: 'Follow', desc: '"Follow" on the company top card. A sign-in destination, measured, never followed.', sel: 'button' }, { noScroll: true });
  await S('company-jobs', exact('a, button', 'See jobs'), B4, { group: g, title: 'See jobs', desc: '"See jobs" primary pill. Measured, never followed.', sel: 'a' }, { noScroll: true });
  await S('company-tab', await mark('company-tab', (el, t) => /^(A|BUTTON)$/.test(el.tagName) && t === "About us" && el.getBoundingClientRect().height >= 32 && el.getBoundingClientRect().height <= 64), ['default', 'hover', 'focus-visible'], { group: g, title: 'Company tab', desc: 'The About us tab on the company page. Measured, never followed.', sel: 'a' });
}

async function profile() {
  if (!(await newPage('profile'))) return;
  await sheetsFor('profile');
  await chrome('profile');
  const g = G.profile;
  await S('profile-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Profile name', desc: 'The public profile name. A published profile, captured signed out.', sel: 'h1' }, { noScroll: true });
  await S('profile-headline', q('.top-card-layout__headline, h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Headline', desc: 'The public profile headline under the name.', sel: '.top-card-layout__headline' }, { noScroll: true });
  await S('profile-join', q('a.btn-primary, a').filter({ hasText: /join to view profile|join now/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Join to view profile', desc: '"Join to view profile". A sign-in destination, measured, never followed.', sel: 'a.btn-primary' });
  await S('profile-message', exact('a, button', 'Message'), B4, { group: g, title: 'Message', desc: '"Message". A sign-in destination into messaging, measured, never followed.', sel: 'a, button' });
  await S('avatar', q('img.top-card-layout__entity-image, img[class*="entity-image"], .top-card__profile-image img').filter({ visible: true }).first(), ['default'], { group: g, title: 'Avatar', desc: 'The public profile photo as the page paints it.', sel: 'img' }, { noScroll: true });
}

async function legal() {
  if (!(await newPage('legal'))) return;
  await sheetsFor('legal');
  await chrome('legal');
  const g = G.legal;
  await S('legal-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Legal heading', desc: 'The User Agreement banner heading (t-64).', sel: 'h1' }, { noScroll: true });
  await S('legal-link', q('a').filter({ hasText: /privacy policy/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Legal nav link', desc: 'A legal-section link. Measured, never followed.', sel: 'a' }, { noScroll: true });
}

async function signin() {
  if (!(await newPage('signin'))) return;
  await sheetsFor('signin');
  const g = G.signin;
  await S('signin-heading', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-in heading', desc: 'The sign-in wall heading, captured at rest. Nothing was typed or submitted.', sel: 'h1' }, { noScroll: true });
  await S('signin-email', q('input[type="email"], input[name="session_key"], input[autocomplete="username"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Email field', desc: 'The sign-in email field at rest and focused. No text was typed. The form was not submitted.', sel: 'input' }, { noScroll: true });
  await S('signin-submit', q('button[type="submit"], button').filter({ hasText: /^Sign in$/ }).filter({ visible: true }).first(), ['default', 'hover', 'focus-visible'], { group: g, title: 'Sign in submit', desc: 'The sign-in submit control. Hover and focus only. It was not pressed, so no sign-in was attempted.', sel: 'button' }, { noScroll: true });
}

async function mobile() {
  if (!(await newPage('home', { mobile: true }))) return;
  const g = G.mobile;
  await S('m-nav', q('header, nav').filter({ has: exact('a', 'Join now') }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile nav', desc: 'The guest nav at 390px.', sel: 'header' }, { noScroll: true });
  await S('m-join', exact('a', 'Join now'), ['default', 'pressed'], { group: g, title: 'Mobile Join now', desc: 'The Join now pill at 390px. A sign-in destination, measured, never followed.', sel: 'a' }, { noScroll: true });
  await S('m-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero heading', desc: 'The guest-home heading at 390px.', sel: 'h1' });
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); linkedin.com guest surfaces paint a single light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, jobs, company, profile, legal, signin, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that transitions (a nav link's hover),
  // so the delta is meaningful.
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
