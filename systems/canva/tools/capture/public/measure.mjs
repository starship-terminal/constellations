// Measures canva.com's public components in every state reachable without
// signing in, checking out or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing templates login mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// canva.com is a StyleX app — every class is a build hash (x1ghz6dp, _0r5XCUQ)
// and themes ride on .theme light/dark/adaptive section classes — so every
// spec selects by role, aria-label, text or structure, never a class. The
// editor itself sits behind /signup and /login; the auth cards are public
// surfaces and are measured as such — "Continue with email" is pressed once
// to reveal the email form (a local step, still signed out), never submitted.
// Nothing is sent, bought or signed into: the only presses are local UI
// toggles — the Design nav flyout, the tools-showcase tabs, the pricing
// billing switch, the plan tabs, the mobile menu and the search/email
// fields' own focus. The "But first, cookies" consent banner is hidden,
// never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing/', templates: '/templates/', login: '/login/' };
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
  await open(page, url || BASE + URLS[key], { wait, promo });
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
  // Canva's SPA re-mounts subtrees when async data resolves (the pricing
  // plans grid re-renders once localised prices arrive): give a briefly
  // unmounted element up to 6s to come back before declaring a miss.
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
        else {
          await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle';
          // Close what the toggle opened once it is read: an open menu keeps focus and stole every later
          // component's keyboard focus (they recorded "focus failed").
          undo = async () => {
            await page.keyboard.press('Escape'); await page.waitForTimeout(400);
            const open = await loc.first().getAttribute('aria-expanded').catch(() => null);
            if (open === 'true') { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(400); }
          };
        }
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
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again|order( free)?( sample)?|add to cart|go to the platform)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

// Scrolls the page down in steps and back to the top: pricing's plan cards
// and comparison rows hydrate lazily, so a cold page only has the heading
// region in the DOM when the run reaches it.
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

// The header's Design button opens the mega-menu flyout (a click toggles it).
async function openFlyout() {
  const t = q('header button').filter({ hasText: /^\s*Design\s*$/ }).filter({ visible: true }).first();
  if (!(await t.count())) return false;
  await t.click({ timeout: 5000 }).catch(() => t.evaluate((el) => el.click()));
  await page.waitForTimeout(1200);
  return true;
}

// Marks the smallest visible ancestor of a "Continue with Google" button that
// holds the whole auth card (all four Continue actions + the terms text).
async function markAuthCard() {
  await page.evaluate(() => {
    const g = [...document.querySelectorAll('button')].find((b) => /Continue with Google/i.test(b.innerText || '') && b.getBoundingClientRect().width > 0);
    if (!g) return;
    let n = g;
    for (let i = 0; i < 12 && n.parentElement; i++) {
      n = n.parentElement;
      const t = n.innerText || '';
      const r = n.getBoundingClientRect();
      if (/Continue with Google/i.test(t) && /Continue with Facebook/i.test(t) && /Continue with email/i.test(t)
        && /Log in or sign up|Continue another way/i.test(t) && t.length < 3000 && r.height > 300 && r.width < 800) {
        n.setAttribute('data-m-mark', 'authcard');
        return;
      }
    }
  });
}

// Marks the smallest visible ancestor of a plan CTA that holds a plan name
// and a price — one pricing card, not the comparison grid around it.
async function markPlanCard() {
  await page.evaluate(() => {
    const cta = [...document.querySelectorAll('button, a')].find((b) => /Try for free|Start a free trial|Get started/i.test(b.innerText || '') && b.getBoundingClientRect().width > 0);
    if (!cta) return;
    let n = cta;
    for (let i = 0; i < 12 && n.parentElement; i++) {
      n = n.parentElement;
      const t = n.innerText || '';
      const r = n.getBoundingClientRect();
      if (/Free|Pro|Business|Enterprise/i.test(t) && /\$\d|\d+\s*\/\s*(month|year)|per (month|year)/i.test(t) && t.length < 2200 && r.width < 600) {
        n.setAttribute('data-m-mark', 'plancard');
        return;
      }
    }
  });
}

// Marks a dark feature card on the home page (a .theme.dark block that holds
// an "Explore …" link).
async function markFeatureCard() {
  await page.evaluate(() => {
    const link = [...document.querySelectorAll('.theme.dark a, .theme.dark [role="link"]')].find((a) => /Explore (Magic|Brand|animations|the collection)/i.test(a.innerText || a.getAttribute('aria-label') || '') && a.getBoundingClientRect().width > 0);
    if (!link) return;
    let n = link;
    for (let i = 0; i < 8 && n.parentElement; i++) {
      n = n.parentElement;
      const r = n.getBoundingClientRect();
      if (r.height > 90 && r.height < 400 && r.width > 200 && r.width < 700) { n.setAttribute('data-m-mark', 'featcard'); return; }
    }
    link.closest('div').setAttribute('data-m-mark', 'featcard');
  });
}

const G = {
  shell: 'Shell and navigation', home: 'Home', pricing: 'Pricing',
  templates: 'Templates', login: 'Login and signup', footer: 'Footer',
  mobile: 'Mobile (390 wide)',
};

// Marks the opened mega-menu panel: the first visible ancestor of the
// "Digital design" flyout heading wide enough to be the panel.
async function markFlyout() {
  await page.evaluate(() => {
    const h = [...document.querySelectorAll('h2,h3,h4')].find((e) => /Digital design/i.test(e.innerText || '') && e.getBoundingClientRect().height > 0);
    if (!h) return;
    let n = h;
    for (let i = 0; i < 9 && n.parentElement; i++) {
      n = n.parentElement;
      const r = n.getBoundingClientRect();
      if (r.width > 500 && r.height > 300) { n.setAttribute('data-m-mark', 'flyout'); return; }
    }
    h.setAttribute('data-m-mark', 'flyout');
  });
}

// Marks the opened mobile navigation panel: a fixed overlay holding the nav
// links and the auth actions.
async function markMobileMenu() {
  await page.evaluate(() => {
    const cand = [...document.querySelectorAll('div,nav,aside,section')].filter((el) => {
      const r = el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      const t = el.innerText || '';
      return (cs.position === 'fixed' || cs.position === 'absolute') && r.height > innerHeight * 0.55 && r.width > innerWidth * 0.6
        && /Sign up|Log in/i.test(t) && /Design|Product|Docs|Presentations/i.test(t) && t.length < 9000;
    }).sort((a, b) => (a.innerText || '').length - (b.innerText || '').length);
    if (cand[0]) cand[0].setAttribute('data-m-mark', 'mmenu');
  });
}

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  // The whole top band (header + hero) sits inside .theme.dark on canva.com.
  await S('header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Header', desc: 'The dark header bar (.theme.dark): the Canva logo, the Design/Product/Plans/Business/Education/Help flyout triggers and the Sign up / Log in actions.', sel: 'header' }, { noScroll: true });
  await S('logo', q('header a').filter({ hasText: /Canva home/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The "Canva home" wordmark anchor.', sel: 'header a Canva home' }, { noScroll: true });
  await S('nav-trigger', q('header button').filter({ hasText: /^\s*Design\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav trigger', desc: 'The Design button that opens the header mega-menu; toggled, never followed.', sel: 'header button Design' }, { noScroll: true });
  await S('signup-cta', q('header a, header button').filter({ hasText: /^\s*Sign up\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-up action', desc: 'The header Sign up action (the purple pill); measured, never followed.', sel: 'header Sign up' }, { noScroll: true });
  await S('login-link', q('header a, header button').filter({ hasText: /^\s*Log in\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Log-in action', desc: 'The header Log in action; measured, never followed.', sel: 'header Log in' }, { noScroll: true });
  try { await openFlyout(); } catch (e) { log('  ! flyout open failed', String(e.message).split('\n')[0]); }
  await markFlyout();
  await S('nav-dropdown', q('[data-m-mark="flyout"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav flyout', desc: 'The Design mega-menu panel (Digital design / Print design / Images / Videos columns), opened by its own trigger.', sel: 'opened Design flyout' }, { noScroll: true, noReset: true });
  // The flyout auto-closes a few seconds after it opens; re-open it before
  // every flyout-child state so hover/focus land on a live element.
  const ensureFlyout = async () => {
    if (!(await q('[data-m-mark="flyout"]').filter({ visible: true }).count())) {
      await openFlyout(); await markFlyout(); await page.waitForTimeout(400);
    }
  };
  await S('menu-link', q('[data-m-mark="flyout"] a, [data-m-mark="flyout"] [role="link"]').filter({ hasText: /Docs|Sheets|Whiteboards|Presentations/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Flyout link', desc: 'A link inside the opened Design flyout.', sel: 'flyout link' }, { noScroll: true, noReset: true, before: { default: ensureFlyout, hover: ensureFlyout, 'focus-visible': ensureFlyout, pressed: ensureFlyout } });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  const h = G.home;
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The "What will you design today?" headline, white on the gradient hero band.', sel: 'h1' });
  await S('hero-sub', await domFind(page, /Make AI-powered social posts/, { sel: 'p, span, div, h2', tag: 'herosub' }), ['default'], { group: h, title: 'Hero copy', desc: 'The lede under the headline on the gradient hero.', sel: 'hero lede' });
  await S('hero-cta', q('button, a').filter({ hasText: /^\s*Start designing\s*$/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The "Start designing" action on the dark hero; measured, never followed.', sel: 'hero CTA' });
  await S('tool-panel', q('[role="tabpanel"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Tool panel', desc: "The tools-showcase panel under the tabs (the selected tool's artwork and copy).", sel: 'role=tabpanel' });
  // After the panel: focus-visible on an ARIA tab activates it, so measured first it turned the panel into
  // the Presentations panel and its own focus/pressed readings into selected-state ones.
  await S('tool-tab', q('[role="tab"]').filter({ hasText: /^\s*Presentations\s*$/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Tool tab', desc: 'A tools-showcase tab (AI / Presentations / Social / Video / Print Shop); measured unselected — the selected state is the screenshot toggle.', sel: 'tools role=tab' });
  await markFeatureCard();
  await S('feature-card', q('[data-m-mark="featcard"]').filter({ visible: true }).first(), B4, { group: h, title: 'Feature card', desc: 'A dark feature card on the home page (the Magic-Layers card with an "Explore" link); the link was measured, never followed.', sel: '.theme.dark feature card' });
  await S('explore-link', q('.theme.dark a, .theme.dark [role="link"]').filter({ hasText: /Explore (Magic|Brand|animations|the collection)/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Explore link', desc: 'An "Explore X" link inside a dark feature card; measured, never followed.', sel: 'explore link' });
  await S('section-h2', q('h2').filter({ hasText: /All the tools|Templates for absolutely anything|Unlock Canva/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A section heading below the dark band (the light part of the page).', sel: 'section h2' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing', { wait: 10000 }))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  await lazyLoad();
  const g = G.pricing;
  await S('pricing-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', desc: 'The "Plans and pricing" display heading.', sel: 'h1 on /pricing' }, { noScroll: true });
  await S('billing-switch', q('button[role="switch"]').filter({ visible: true }).first(), B4, { group: g, title: 'Billing switch', desc: 'The Monthly/Yearly billing switch next to "Save from 16%"; toggled for the billing screenshot, never checked out.', sel: 'button[role=switch]' }, { noScroll: true });
  await markPlanCard();
  await S('plan-card', q('[data-m-mark="plancard"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan card', desc: 'A pricing plan card (plan name, price in S$ — the capture was served the Singapore region — and its action).', sel: 'plan card' });
  await S('plan-price', await domFind(page, /S\$\s*\d+/, { sel: 'span, div', tag: 'price' }), ['default'], { group: g, title: 'Plan price', desc: "A plan card's price figure (S$ in the Singapore region the capture was served).", sel: 'plan S$ figure' });
  await S('plan-cta', q('[data-m-mark="plancard"] button, [data-m-mark="plancard"] a').filter({ hasText: /Get started|Try for free|Start a free trial/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: "A plan card's action (Get started / Try for free / Start a free trial); measured, never followed.", sel: 'plan card CTA' });
  await S('feature-accordion', q('button').filter({ hasText: /Design and publishing|Templates for social media/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Feature row', desc: 'A feature-comparison row in the plan table; measured closed, never expanded.', sel: 'comparison row button' });
  // Plan tab last: keyboard focus AUTO-ACTIVATES it (ARIA automatic
  // activation — the URL switches to ?tab=education and every component
  // below re-renders), so measuring its focus state earlier would poison
  // every reading after it.
  await S('plan-tab', q('[role="tab"]').filter({ hasText: /Education/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan tab', desc: 'A plan-audience tab (Individuals and business / Education); keyboard focus auto-activates it, which swaps the pricing view — measured last so the tab switch cannot contaminate the other components.', sel: 'plans role=tab' }, { noScroll: true });
  save();
}

async function templates() {
  if (!(await newPage('templates', { wait: 10000 }))) return;
  await sheetsFor('templates');
  await chrome('templates');
  const g = G.templates;
  await S('templates-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Templates title', desc: 'The "Free templates" display heading.', sel: 'h1 on /templates' }, { noScroll: true });
  await S('search-field', q('input[type="search"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Search field', desc: 'The "Search templates" input; focused only — typing was never sent so no live query ran.', sel: 'input[type=search]' });
  await S('category-card', q('a[href$="/templates/"]').filter({ visible: true }).first(), B4, { group: g, title: 'Category card', desc: 'A template-category card (image tile + label linking /presentations/templates/ etc.); measured, never followed.', sel: 'a[href$="/templates/"]' });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 10000 }))) return;
  await sheetsFor('login');
  const g = G.login;
  await markAuthCard();
  await S('auth-card', q('[data-m-mark="authcard"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Auth card', desc: 'The sign-in card (Continue with Google / Facebook / email / another way + terms); captured, never used.', sel: 'auth card' }, { noScroll: true });
  await S('oauth-button', q('button').filter({ hasText: /Continue with Google/ }).filter({ visible: true }).first(), B4, { group: g, title: 'OAuth button', desc: 'The "Continue with Google" action; measured, never pressed — it would leave for the OAuth flow.', sel: 'Continue with Google' }, { noScroll: true });
  await S('email-continue', q('button').filter({ hasText: /Continue with email/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Email continue', desc: 'The "Continue with email" action that reveals the email form; pressed once below to open that form (a local step, still signed out).', sel: 'Continue with email' }, { noScroll: true });
  // Reveal the email form — a local UI step, not a submit. The username field
  // is focused, given sample text that is deleted again, and the Continue
  // action is measured but never pressed.
  try {
    const b = q('button').filter({ hasText: /Continue with email/ }).filter({ visible: true }).first();
    await b.click({ timeout: 5000 }).catch(() => b.evaluate((el) => el.click()));
    await page.waitForTimeout(1800);
  } catch (e) { log('  ! email-continue open failed', String(e.message).split('\n')[0]); }
  await S('username-input', q('input[name="username"], input[type="email"], input[type="text"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Email field', desc: 'The email/username input revealed by "Continue with email"; focused and given sample text that was deleted again — nothing sent.', sel: 'input[name=username]' }, { noScroll: true });
  await S('continue-button', q('button').filter({ hasText: /^\s*Continue\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Continue button', desc: "The email form's Continue action; measured, never pressed.", sel: 'form Continue' }, { noScroll: true });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 6000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1500);
  await S('footer', q('footer').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The footer: download links, the Product/Plans/About columns, social icons and legal.', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('footer a').filter({ hasText: /Pricing|Pro|Features|Windows|Mac/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', sel: 'footer a' }, { noScroll: true });
  await S('social-icon', q('footer a[href*="instagram"], footer a[href*="facebook"], footer a[href*="x.com"], footer a[href*="twitter"], footer a[href*="linkedin"], footer a[aria-label*="Instagram" i], footer a[aria-label*="Facebook" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Social link', desc: 'A social link in the footer.', sel: 'footer social a' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: 'header at 390' }, { noScroll: true });
  const menu = q('header button[aria-label*="navigation menu" i], header button[aria-label*="menu" i]').filter({ visible: true }).first();
  await S('m-menu-button', menu, ['default'], { group: g, title: 'Menu button', desc: 'The "Open navigation menu" burger toggle.', sel: 'button[aria-label*=navigation menu]' }, { noScroll: true });
  try {
    if (await menu.count()) { await menu.click({ timeout: 5000 }).catch(() => menu.evaluate((el) => el.click())); await page.waitForTimeout(1600); }
  } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  await markMobileMenu();
  await S('m-menu-open', q('[data-m-mark="mmenu"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The opened mobile navigation panel (the fixed overlay holding the menu links and the auth actions).', sel: 'opened mobile menu' }, { noScroll: true });
  await S('m-nav-item', q('[data-m-mark="mmenu"] a, [data-m-mark="mmenu"] button, [data-m-mark="mmenu"] [role="link"], [data-m-mark="mmenu"] [role="button"]').filter({ hasText: /^\s*(Design|Product|Plans|Business|Education|Help)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile nav item', desc: 'A row inside the opened mobile menu (Design / Product / Plans / Business / Education / Help).', sel: 'mobile menu row' }, { noScroll: true });
  await S('m-signup', q('[data-m-mark="mmenu"] a, [data-m-mark="mmenu"] button').filter({ hasText: /^\s*Sign up\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile sign-up', desc: 'The Sign up action inside the mobile menu; measured, never followed.', sel: 'mobile menu Sign up' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', sel: 'h1 at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); the public surface paints light with a dark .theme header/hero band on home and dark .theme sections elsewhere';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, templates, login, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that actually transitions (a header
  // flyout trigger), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'header button');
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
