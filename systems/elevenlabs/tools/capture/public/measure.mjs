// Measures elevenlabs.io's public components in every state reachable without
// signing in, checking out or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing tts api docs signin signup mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// elevenlabs.io is a Next.js + Tailwind 4 app — tw-* atomic classes plus a
// few hashed CSS-module names — so every spec selects by role, aria-label,
// text or structure, never a class. The public surface paints light only.
// /app redirects to /app/sign-in: the auth cards are public surfaces and are
// measured as such — fields are focused and given sample text that is deleted
// again, never submitted. The home playground's textarea is the public demo's
// own affordance; its Play is measured but never pressed here (the pressed
// state is CDP-forced, not a click). Nothing is sent, bought or signed into:
// the only presses are local UI toggles — the Products nav flyout, the hero
// product tabs, the billing dropdown, the mobile menu and the fields' own
// focus. The Cookiebot consent layer is hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', pricing: '/pricing', tts: '/text-to-speech', api: '/api', docs: '/docs/overview/intro', signin: '/app/sign-in', signup: '/app/sign-up' };
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
  const cleared = await open(page, url || BASE + URLS[key], { wait, promo });  // false: the bot check did not clear (lib.mjs)
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
          // Close it again after the reading: a menu left open holds focus, so every later
          // focus-visible on the page records 'focus failed'. Escape closes a menu; an
          // accordion still reporting aria-expanded=true is toggled back.
          undo = async () => {
            await page.keyboard.press('Escape'); await page.waitForTimeout(300);
            const l = loc.filter({ visible: true }).first();
            if ((await l.getAttribute('aria-expanded').catch(() => null)) === 'true') { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(600); }
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

// The nav's Products/Solutions/Resources buttons open the flyout (a click
// toggles it).
async function openFlyout() {
  const t = q('nav button, nav [role="button"]').filter({ hasText: /^\s*Products\s*$/ }).filter({ visible: true }).first();
  if (!(await t.count())) return false;
  await t.click({ timeout: 5000 }).catch(() => t.evaluate((el) => el.click()));
  await page.waitForTimeout(1200);
  return true;
}

// Marks the opened Products flyout: the smallest visible ancestor of an
// "Overview" label that also holds the ElevenCreative column links.
async function markFlyout() {
  await page.evaluate(() => {
    const h = [...document.querySelectorAll('*')].find((e) => /^\s*Overview\s*$/.test(e.innerText || '') && e.children.length === 0 && e.getBoundingClientRect().height > 0);
    if (!h) return;
    let n = h;
    for (let i = 0; i < 12 && n.parentElement; i++) {
      n = n.parentElement;
      const t = n.innerText || '';
      const r = n.getBoundingClientRect();
      if (/ElevenCreative/i.test(t) && /ElevenAgents/i.test(t) && /ElevenAPI/i.test(t) && r.width > 500 && r.height > 300 && r.height < 800) {
        n.setAttribute('data-m-mark', 'flyout');
        return;
      }
    }
  });
}

// Marks the smallest visible ancestor of a "Sign in with Google" button that
// holds the whole auth card (the OAuth actions, the email/password fields and
// the submit).
async function markAuthCard() {
  await page.evaluate(() => {
    const g = [...document.querySelectorAll('button, a')].find((b) => /Sign in with Google|Sign up with Google/i.test(b.innerText || '') && b.getBoundingClientRect().width > 0);
    if (!g) return;
    let n = g;
    for (let i = 0; i < 12 && n.parentElement; i++) {
      n = n.parentElement;
      const t = n.innerText || '';
      const r = n.getBoundingClientRect();
      if (/Email/i.test(t) && /Password/i.test(t) && /Sign in|Sign up/i.test(t) && t.length < 2200 && r.height > 280 && r.width < 700) {
        n.setAttribute('data-m-mark', 'authcard');
        return;
      }
    }
  });
}

// Marks the smallest visible ancestor of a plan CTA that holds a plan name
// and a price — one pricing card, not the grid around it.
async function markPlanCard() {
  await page.evaluate(() => {
    const cta = [...document.querySelectorAll('button, a')].find((b) => /Choose Creator|Build for free|Choose Starter/i.test(b.innerText || '') && b.getBoundingClientRect().width > 0);
    if (!cta) return;
    let n = cta;
    for (let i = 0; i < 12 && n.parentElement; i++) {
      n = n.parentElement;
      const t = n.innerText || '';
      const r = n.getBoundingClientRect();
      if (/\$\d|first month|\/\s*mo/i.test(t) && /Free|Starter|Creator|Pro|Scale|Business|Enterprise/i.test(t) && t.length < 2200 && r.width < 600) {
        n.setAttribute('data-m-mark', 'plancard');
        return;
      }
    }
  });
}

// Marks the home playground card: the smallest ancestor of the textarea that
// also holds the language and voice controls and the Play button.
async function markTtsCard() {
  await page.evaluate(() => {
    const ta = document.querySelector('textarea');
    if (!ta) return;
    let n = ta;
    for (let i = 0; i < 10 && n.parentElement; i++) {
      n = n.parentElement;
      const t = n.innerText || '';
      const r = n.getBoundingClientRect();
      if (/English/i.test(t) && /Play/i.test(t) && r.width > 400 && r.width < 900 && r.height > 180 && r.height < 700) {
        n.setAttribute('data-m-mark', 'ttscard');
        return;
      }
    }
  });
}

// Marks the promo strip: the smallest ancestor of the "Meet Eleven v4" /
// "$1 credits" copy wide enough to be the strip itself.
async function markPromo() {
  await page.evaluate(() => {
    const h = [...document.querySelectorAll('p, span, div, a')].find((e) => /Meet Eleven v4|credits for only \$1/i.test(e.innerText || '') && e.getBoundingClientRect().height > 0 && e.getBoundingClientRect().top < 80);
    if (!h) return;
    let n = h;
    for (let i = 0; i < 8 && n.parentElement; i++) {
      n = n.parentElement;
      const r = n.getBoundingClientRect();
      if (r.width > 900 && r.height < 200) { n.setAttribute('data-m-mark', 'promo'); return; }
    }
    h.setAttribute('data-m-mark', 'promo');
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
        && /Sign up|Log in/i.test(t) && /Products|Solutions|Resources|Pricing/i.test(t) && t.length < 9000;
    }).sort((a, b) => (a.innerText || '').length - (b.innerText || '').length);
    if (cand[0]) cand[0].setAttribute('data-m-mark', 'mmenu');
  });
}

const G = {
  shell: 'Shell and navigation', home: 'Home', pricing: 'Pricing',
  tts: 'Text to Speech', api: 'API', docs: 'Docs', auth: 'Sign in and sign up',
  footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await markPromo();
  await S('announcement', q('[data-m-mark="promo"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Announcement bar', desc: 'The promo strip above the nav (the V4 "Meet Eleven v4" bar on home, the $1-credits countdown on product pages).', sel: 'promo strip' }, { noScroll: true });
  await S('nav', q('nav').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav bar', desc: 'The top nav: the ElevenLabs wordmark, the Products/Solutions/Customers/Resources flyout triggers, Enterprise and Pricing links, and the Log in / Sign up actions.', sel: 'nav' }, { noScroll: true });
  await S('logo', q('nav a[aria-label="ElevenLabs"], nav a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The ElevenLabs wordmark anchor (aria-label "ElevenLabs").', sel: 'a[aria-label=ElevenLabs]' }, { noScroll: true });
  await S('nav-trigger', q('nav button, nav [role="button"]').filter({ hasText: /^\s*Products\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav trigger', desc: 'The Products button that opens the nav flyout; toggled, never followed.', sel: 'nav button Products' }, { noScroll: true });
  await S('nav-link', q('nav a').filter({ hasText: /^\s*Pricing\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A plain nav link (Pricing); measured, never followed.', sel: 'nav a Pricing' }, { noScroll: true });
  await S('signup-cta', q('a').filter({ hasText: /^\s*Sign up\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-up action', desc: 'The header Sign up action (the black pill); measured, never followed.', sel: 'header Sign up' }, { noScroll: true });
  await S('login-link', q('a').filter({ hasText: /^\s*Log in\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Log-in action', desc: 'The header Log in action; measured, never followed.', sel: 'header Log in' }, { noScroll: true });
  try { await openFlyout(); } catch (e) { log('  ! flyout open failed', String(e.message).split('\n')[0]); }
  await markFlyout();
  await S('nav-dropdown', q('[data-m-mark="flyout"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav flyout', desc: 'The Products mega-menu panel (Overview / ElevenCreative / ElevenAgents / ElevenAPI columns), opened by its own trigger.', sel: 'opened Products flyout' }, { noScroll: true, noReset: true });
  const ensureFlyout = async () => {
    if (!(await q('[data-m-mark="flyout"]').filter({ visible: true }).count())) {
      await openFlyout(); await markFlyout(); await page.waitForTimeout(400);
    }
  };
  await S('menu-link', q('a[href="/text-to-speech"], a[href="/studio"]').filter({ visible: true }).first(), B4, { group: g, title: 'Flyout link', desc: 'A link inside the opened Products flyout (Text to Speech).', sel: 'flyout a[href=/text-to-speech]' }, { noScroll: true, noReset: true, before: { default: ensureFlyout, hover: ensureFlyout, 'focus-visible': ensureFlyout, pressed: ensureFlyout } });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  const h = G.home;
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The "Bringing technology to life" display headline.', sel: 'h1' });
  await S('hero-sub', await domFind(page, /Powering the best enterprises/, { sel: 'p, span, div, h2', tag: 'herosub' }), ['default'], { group: h, title: 'Hero copy', desc: 'The lede under the hero headline.', sel: 'hero lede' });
  await S('hero-cta', q('button, a').filter({ hasText: /^\s*Sign up\s*$/ }).filter({ visible: true }).last(), B4, { group: h, title: 'Hero CTA', desc: 'The hero "Sign up" black pill; measured, never followed.', sel: 'hero Sign up' });
  await S('contact-sales', q('button, a').filter({ hasText: /^\s*Contact sales\s*$/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Secondary CTA', desc: 'The hero "Contact sales" ghost pill; measured, never followed.', sel: 'hero Contact sales' });
  await S('product-tab', q('[role="tab"]').filter({ hasText: 'ElevenAgents' }).filter({ visible: true }).first(), B4, { group: h, title: 'Product tab', desc: 'A hero product tab (ElevenCreative / ElevenAgents / ElevenAPI); measured unselected — the selected state is the screenshot toggle.', sel: 'hero role=tab' });
  await S('tool-tab', q('[role="tab"]').filter({ hasText: 'Text to Speech' }).filter({ visible: true }).first(), B4, { group: h, title: 'Tool tab', desc: 'A product-showcase tab (AI Voice Generator / Text to Speech / Music / Speech to Text / Voice Cloning / Dubbing).', sel: 'tools role=tab' });
  await S('voice-play', q('button[aria-label*="preview"]').filter({ visible: true }).first(), B4, { group: h, title: 'Voice preview', desc: 'A "Play <voice> preview" button on the voice-orb carousel; measured, the audio itself was never played here.', sel: 'button[aria-label*=preview]' });
  await S('voice-prev', q('button[aria-label="Previous voice"]').first(), B4, { group: h, title: 'Carousel previous', desc: 'The "Previous voice" carousel icon button.', sel: 'button[aria-label=Previous voice]' });
  await S('section-h2', q('h2').filter({ hasText: /Create, edit, and localize|Built for|Trusted by/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A section heading below the hero (the "Create, edit, and localize in one AI platform" block).', sel: 'section h2' });
  await markTtsCard();
  await S('tts-card', q('[data-m-mark="ttscard"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Playground card', desc: 'The "Ultra-realistic speech" playground card — the signed-out TTS demo widget (textarea, language and voice selects, Play).', sel: 'playground card' });
  await S('tts-textarea', q('textarea').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: h, title: 'Playground textarea', desc: "The playground's text field; focused and given sample text that was deleted again — nothing generated in this pass.", sel: 'textarea' });
  await S('tts-language', q('button').filter({ hasText: /^\s*English\s*$/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Language select', desc: 'The playground language combobox (the flag + "English" button).', sel: 'language button' });
  await S('tts-voice', q('button').filter({ hasText: /Spuds Oxley|James|Hope/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Voice select', desc: 'The playground voice combobox (the orb + voice-name button).', sel: 'voice button' });
  await S('tts-play', q('button').filter({ hasText: /^\s*Play\s*$/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Play button', desc: 'The playground Play action; states forced — the public shot pass pressed it once and it generated without an account (see README).', sel: 'Play button' });
  await S('learn-more', q('button, a').filter({ hasText: /^\s*Learn more\s*$/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Learn more', desc: 'The "Learn more" black pill in the product section.', sel: 'Learn more' });
  await S('feature-card', q('[data-m-mark="ttscard"]').filter({ visible: true }).first().locator('xpath=..'), ['default'], { group: h, title: 'Feature panel', desc: 'A feature panel under the product grid (the Ultra-realistic speech showcase, the playground card\'s parent).', sel: 'feature panel' });
  await S('voice-chat', q('button, [role="button"], a').filter({ hasText: /Voice chat/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Voice-chat launcher', desc: 'The fixed "Voice chat" launcher bottom-right (the ElevenAgents widget); measured, never opened.', sel: 'Voice chat launcher' }, { noScroll: true });
  save();
}

async function pricing() {
  if (!(await newPage('pricing', { wait: 10000 }))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  await lazyLoad();
  const g = G.pricing;
  await S('pricing-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing title', desc: 'The "Flexible pricing for your needs" display heading.', sel: 'h1 on /pricing' }, { noScroll: true });
  await S('product-pill', q('a').filter({ hasText: 'ElevenAgents' }).filter({ visible: true }).first(), B4, { group: g, title: 'Product pill', desc: 'An ElevenCreative/ElevenAgents/ElevenAPI product pill (a link, not a tab — it navigates); measured, never followed.', sel: 'product pill' }, { noScroll: true });
  await S('billing-select', q('button').filter({ hasText: /billing/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Billing dropdown', desc: 'The "Monthly billing" dropdown; opened for the billing screenshot, never changed.', sel: 'billing dropdown' }, { noScroll: true });
  await markPlanCard();
  await S('plan-card', q('[data-m-mark="plancard"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan card', desc: 'A pricing plan card (Free / Starter / Creator / Pro — name, price and action).', sel: 'plan card' });
  await S('plan-price', await domFind(page, /\$\d+/, { sel: 'span, div', tag: 'price' }), ['default'], { group: g, title: 'Plan price', desc: "A plan card's price figure.", sel: 'plan $ figure' });
  await S('plan-cta', q('[data-m-mark="plancard"] button, [data-m-mark="plancard"] a').filter({ hasText: /Build for free|Choose \w+|Contact sales/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: "A plan card's action (Build for free / Choose X); measured, never followed.", sel: 'plan card CTA' });
  await S('plan-badge', await domFind(page, /^\s*(Popular|Until Nov \d+)\s*$/, { sel: 'span, div, button', tag: 'badge' }), ['default'], { group: g, title: 'Plan badge', desc: 'A badge on a plan card ("Popular" on Creator, "Until Nov 16" on Starter).', sel: 'plan badge' });
  await S('feature-row', q('[data-m-mark="plancard"] div, [data-m-mark="plancard"] span, [data-m-mark="plancard"] p, [data-m-mark="plancard"] li').filter({ hasText: /Everything in/ }).filter({ visible: true }).last(), B4, { group: g, title: 'Feature row', desc: 'An "Everything in X, plus" feature-group row inside a plan card.', sel: 'plan card feature row' });
  await S('faq-item', q('button').filter({ hasText: /How much does each plan cost|How do text characters and credits work/ }).filter({ visible: true }).first(), B4, { group: g, title: 'FAQ accordion', desc: 'A FAQ accordion row under Compare plans; measured closed, never expanded.', sel: 'FAQ button' });
  save();
}

async function tts() {
  if (!(await newPage('tts', { wait: 10000 }))) return;
  await sheetsFor('tts');
  await chrome('tts');
  const g = G.tts;
  await S('tts-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Page title', desc: 'The h1 on /text-to-speech (the small "Text to Speech" eyebrow above the big display).', sel: 'h1 on /text-to-speech' }, { noScroll: true });
  await S('tts-display', await domFind(page, /high quality, human-like AI voices/, { sel: 'h1, h2, p, span, div', tag: 'ttsdisplay' }), ['default'], { group: g, title: 'Display heading', desc: 'The "Text to Speech with high quality, human-like AI voices" display heading.', sel: 'tts display' }, { noScroll: true });
  await S('google-login', q('button, a').filter({ hasText: /Log in with Google/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Google login CTA', desc: 'The "Log in with Google" action on the product hero; measured, never pressed — it would leave for the OAuth flow.', sel: 'Log in with Google' }, { noScroll: true });
  await S('convert-cta', q('button, a').filter({ hasText: /Convert Text to Speech/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Convert CTA', desc: 'The "Convert Text to Speech" action; measured, never followed.', sel: 'Convert Text to Speech' }, { noScroll: true });
  await S('voice-card', q('a, div, section, article').filter({ hasText: /Conversational|Social Media|Podcast/ }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Voice sample card', desc: 'A voice-sample card (the photo card with a corner play button and the voice name).', sel: 'voice card' });
  await S('card-play', q('button[aria-label^="Play - "], button[aria-label^="Play – "]').filter({ visible: true }).first(), B4, { group: g, title: 'Sample play button', desc: 'The corner play button on a voice-sample card; measured, audio never played here.', sel: 'button[aria-label^=Play]' });
  await S('try-voice', q('button, a').filter({ hasText: /Try this voice/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Try voice CTA', desc: 'The "Try this voice" action under the voice cards; measured, never followed.', sel: 'Try this voice' });
  save();
}

async function api() {
  if (!(await newPage('api', { wait: 10000 }))) return;
  await sheetsFor('api');
  await chrome('api');
  const g = G.api;
  await S('api-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Page title', desc: 'The "Build production-ready audio AI in minutes" display heading.', sel: 'h1 on /api' }, { noScroll: true });
  await S('apikey-cta', q('button, a').filter({ hasText: /Get API key/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Get API key CTA', desc: 'The "Get API key" black pill; measured, never followed (it leads to sign-up).', sel: 'Get API key' }, { noScroll: true });
  await S('explore-docs', q('button, a').filter({ hasText: /Explore docs/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Explore docs', desc: 'The "Explore docs" ghost pill; measured, never followed.', sel: 'Explore docs' }, { noScroll: true });
  await S('demo-tab', q('button, [role="tab"]').filter({ hasText: /^\s*(Demo|Code)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Demo/Code tab', desc: 'The Demo/Code toggle on the Text to Speech API card.', sel: 'Demo Code toggle' });
  save();
}

async function docs() {
  if (!(await newPage('docs', { wait: 10000 }))) return;
  await sheetsFor('docs');
  await chrome('docs');
  const g = G.docs;
  await S('docs-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Docs title', desc: 'The "ElevenLabs Documentation" heading.', sel: 'h1 on /docs' }, { noScroll: true });
  await S('docs-search', q('button, input, [role="combobox"], [role="searchbox"]').filter({ hasText: /Search/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Docs search', desc: 'The docs search trigger in the top bar.', sel: 'docs Search' }, { noScroll: true });
  await S('docs-nav-item', q('aside a, nav a').filter({ hasText: /^\s*Text to Speech\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Docs nav item', desc: 'A sidebar capability link (Text to Speech).', sel: 'docs sidebar link' });
  await S('docs-copy-page', q('button, a').filter({ hasText: /Copy page/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Copy page', desc: 'The "Copy page" dropdown on the doc header.', sel: 'Copy page' });
  save();
}

async function signin() {
  if (!(await newPage('signin', { wait: 10000 }))) return;
  await sheetsFor('signin');
  const g = G.auth;
  await markAuthCard();
  await S('signin-card', q('[data-m-mark="authcard"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-in card', desc: 'The sign-in card (Sign in with Google / Apple / SSO, email + password, the disabled submit); captured, never used.', sel: 'sign-in card' }, { noScroll: true });
  await S('oauth-google', q('button, a').filter({ hasText: /Sign in with Google/ }).filter({ visible: true }).first(), B4, { group: g, title: 'OAuth button', desc: 'The "Sign in with Google" action; measured, never pressed — it would leave for the OAuth flow.', sel: 'Sign in with Google' }, { noScroll: true });
  await S('oauth-sso', q('button, a').filter({ hasText: /Sign in with SSO/ }).filter({ visible: true }).first(), B4, { group: g, title: 'SSO button', desc: 'The "Sign in with SSO" action; measured, never pressed.', sel: 'Sign in with SSO' }, { noScroll: true });
  await S('email-field', q('input[type="email"], input[name="email"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Email field', desc: 'The email input; focused and given sample text that was deleted again — nothing sent.', sel: 'input[type=email]' }, { noScroll: true });
  await S('password-field', q('input[type="password"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Password field', desc: 'The password input (with the visibility toggle); focused only — nothing typed, nothing sent.', sel: 'input[type=password]' }, { noScroll: true });
  await S('signin-submit', q('button[type="submit"], button').filter({ hasText: /^\s*Sign in\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-in submit', desc: 'The Sign in submit — disabled until the fields validate; measured, never pressed. The card carries no forgot-password or sign-up link — the sign-up page links back instead.', sel: 'Sign in submit' }, { noScroll: true });
  save();
}

async function signup() {
  if (!(await newPage('signup', { wait: 10000 }))) return;
  await sheetsFor('signup');
  const g = G.auth;
  await markAuthCard();
  await S('signup-card', q('[data-m-mark="authcard"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-up card', desc: 'The create-account card (SSO / Google, email + password, the ToS checkbox, the disabled submit); captured, never used.', sel: 'sign-up card' }, { noScroll: true });
  await S('tos-checkbox', q('input[type="checkbox"], [role="checkbox"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'ToS checkbox', desc: 'The "I agree to the Terms of Service" checkbox; measured unchecked, never toggled.', sel: 'checkbox' }, { noScroll: true });
  await S('signup-submit', q('button[type="submit"], button').filter({ hasText: /^\s*Sign up\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-up submit', desc: 'The Sign up submit — disabled until the form validates; measured, never pressed.', sel: 'Sign up submit' }, { noScroll: true });
  await S('signin-link', q('a[href="/app/sign-in"]').filter({ visible: true }).first(), B4, { group: g, title: 'Sign-in link', desc: 'The "Already registered? Sign in" link under the sign-up card; measured, never followed.', sel: 'a[href=/app/sign-in]' }, { noScroll: true });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 6000 }))) return;
  const g = G.footer;
  // The footer mounts lazily near the bottom of the long page: scroll in
  // steps so the streamed sections land before reading it.
  for (let i = 0; i < 10; i++) {
    await page.evaluate(() => scrollBy(0, innerHeight));
    await page.waitForTimeout(700);
  }
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(2000);
  // The <footer> element itself reports 0x0 (a display:contents-ish shell);
  // mark the smallest real ancestor of the Privacy link that spans the page.
  await page.evaluate(() => {
    const a = [...document.querySelectorAll('a')].find((e) => /^\s*Privacy\s*$/.test(e.innerText || '') && e.getBoundingClientRect().width > 0);
    if (!a) return;
    let n = a;
    for (let i = 0; i < 10 && n.parentElement; i++) {
      n = n.parentElement;
      const r = n.getBoundingClientRect();
      if (r.width > 900 && r.height > 150) { n.setAttribute('data-m-mark', 'footerwrap'); return; }
    }
  });
  await S('footer', q('[data-m-mark="footerwrap"], footer').filter({ visible: true }).first(), ['default'], { group: g, title: 'Footer', desc: 'The footer (a 0x0 <footer> shell whose children paint the product/company/resources columns, social icons, language selector and legal).', sel: 'footer contents' }, { noScroll: true });
  await S('footer-link', q('footer a').filter({ hasText: /Pricing|Careers|Blog|Safety|API/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', sel: 'footer a' }, { noScroll: true });
  await S('social-icon', q('footer a[href*="x.com"], footer a[href*="twitter"], footer a[href*="linkedin"], footer a[href*="instagram"], footer a[href*="youtube"], footer a[aria-label*="LinkedIn" i], footer a[aria-label*="X " i]').filter({ visible: true }).first(), B4, { group: g, title: 'Social link', desc: 'A social link in the footer.', sel: 'footer social a' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('nav, header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', sel: 'header at 390' }, { noScroll: true });
  const menu = q('button[aria-label*="navigation" i], button[aria-label*="menu" i], header button, nav button').filter({ visible: true }).first();
  await S('m-menu-button', menu, ['default'], { group: g, title: 'Menu button', desc: 'The burger toggle that opens the mobile navigation sheet.', sel: 'menu button' }, { noScroll: true });
  try {
    if (await menu.count()) { await menu.click({ timeout: 5000 }).catch(() => menu.evaluate((el) => el.click())); await page.waitForTimeout(1600); }
  } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  await markMobileMenu();
  await S('m-menu-open', q('[data-m-mark="mmenu"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The opened mobile navigation sheet (the overlay holding the menu links and the auth actions).', sel: 'opened mobile menu' }, { noScroll: true });
  await S('m-nav-item', q('[data-m-mark="mmenu"] a, [data-m-mark="mmenu"] button, [data-m-mark="mmenu"] [role="link"], [data-m-mark="mmenu"] [role="button"]').filter({ hasText: /^\s*(Products|Solutions|Customers|Resources|Enterprise|Pricing)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile nav item', desc: 'A row inside the opened mobile menu.', sel: 'mobile menu row' }, { noScroll: true });
  await S('m-signup', q('[data-m-mark="mmenu"] a, [data-m-mark="mmenu"] button').filter({ hasText: /^\s*Sign up\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile sign-up', desc: 'The Sign up action inside the mobile menu; measured, never followed.', sel: 'mobile menu Sign up' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', sel: 'h1 at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); the public surface paints light only (the #FDFCFC eggshell field) — elevenlabs.io has no dark theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, tts, api, docs, signin, signup, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that actually transitions (a nav
  // flyout trigger), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'nav button');
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
