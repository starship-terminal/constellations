// Measures exactly.ai's public components in every state reachable without
// signing in, buying or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing showcase showcase-brand case-studies case-study
// industries industry help-center help-faq book-a-demo mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// exactly.ai is a Framer-published marketing site in one light theme: the
// photo-hero home page, /pricing, the /showcase brand gallery, /case-studies
// articles, /industries pages, the doc-style /help-center and /book-a-demo's
// embedded scheduler. Classes are framer-XXXXX hashes plus stable
// framer-text/framer-styles-preset-* presets, so specs select by role,
// aria-label, structure or text. Nothing is sent, bought or signed into:
// the only presses are local UI toggles — the FAQ accordion items and the
// mobile "Mobile menu toggle" hamburger; the help-center search is typed
// into and cleared, never submitted; Log in, Start for free, Book a demo
// and every threads.exactly.ai link are measured, never followed. The
// Gleap support bubble and the scheduler's cookie line are hidden, never
// answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, REF, CROPS, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/', pricing: '/pricing', showcase: '/showcase', 'showcase-brand': '/showcase/revolut',
  'case-studies': '/case-studies', 'case-study': '/case-studies/how-indrive-scales-global-brand-assets-at-the-speed-of-mobility-with-exactly-ai',
  industries: '/industries', industry: '/industries/saas-n-mobile-apps',
  'help-center': '/help-center', 'help-faq': '/help-center/frequently-asked-questions',
  'book-a-demo': '/book-a-demo', mobile: '/',
};
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes the edge or a failure gated this run: components last measured on
// them keep their earlier readings instead of being pruned below (a blocked
// pass must never erase evidence).
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
  const cleared = await open(page, url || (URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key]), { wait, promo });  // false: the bot check did not clear (lib.mjs)
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
  Object.assign(c, { page: current, run, url: URLS[current] && (URLS[current].startsWith('http') ? URLS[current] : BASE + URLS[current]) }, meta);
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
      if (st === 'focus-visible' && via === 'focus failed') {
        // Keyboard focus never reached the element, so a reading now would be the element at rest
        // saved as its focus. Record the miss instead (the builders list it as "focus could not be
        // captured"); an earlier run's real focus reading is kept, with the failed retry noted beside it.
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
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again|book|start for free|book a demo)$/i;
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

// Whether the page paints a different transition under prefers-reduced-motion:
// the same component re-read in a context with reduce on.
async function reducedMotion(key, sel, text = null) {
  // `text` narrows `sel` to the named, visible element the normal pass measured.
  const slot = `${key} ${sel}${text ? ` "${text.source}"` : ''}`; // one entry per element
  out._meta.reducedMotion ??= {};
  try {
    const b = context.browser();
    const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', reducedMotion: 'reduce' });
    await patch(ctx);
    const p = await ctx.newPage();
    await p.goto(URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(7000);
    await closePromo(p);
    const v = await p.evaluate(([s, src]) => {
      const re = src && new RegExp(src, 'i');
      const el = [...document.querySelectorAll(s)].find((n) => {
        const r = n.getBoundingClientRect();
        return r.width > 0 && r.height > 0 && (!re || re.test((n.innerText || '').trim()));
      });
      if (!el) return null;
      const cs = getComputedStyle(el);
      return { transition: cs.transition, animation: cs.animation, scrollBehavior: getComputedStyle(document.documentElement).scrollBehavior };
    }, [sel, text && text.source]).catch(() => null);
    out._meta.reducedMotion[slot] = { page: key, selector: sel, text: text && text.source, reduce: v };
    await ctx.close();
  } catch (e) { out._meta.reducedMotion[slot] = { page: key, selector: sel, error: String(e).slice(0, 120) }; }
}

const G = {
  shell: 'App shell and navigation', home: 'Home', pricing: 'Pricing', showcase: 'Showcase and case studies',
  industries: 'Industries', help: 'Help center', demo: 'Book a demo', mobile: 'Mobile (390 wide)', footer: 'Footer',
};

// Opens the mobile nav overlay: the div carrying the "Mobile menu toggle"
// label switches the hamburger into a full-viewport menu. A local UI toggle;
// its links are never followed.
async function openBurgerMenu() {
  const ok = () => page.waitForFunction(() => {
    const links = [...document.querySelectorAll('a')].filter((el) => {
      const r = el.getBoundingClientRect();
      return r.height > 20 && /^(Industries|Showcase|Case studies|Pricing|Log in)$/.test((el.innerText || '').trim()) && getComputedStyle(el).visibility !== 'hidden';
    });
    return links.length >= 3;
  }, undefined, { timeout: 4000 }).then(() => true).catch(() => false);
  if (await ok()) return 'the nav overlay was already open';
  const b = page.locator('div[aria-label="Mobile menu toggle"]').filter({ visible: true }).last();
  if (!(await b.count())) return 'no burger toggle';
  for (let i = 0; i < 3; i++) {
    await b.evaluate((el) => el.scrollIntoView({ block: 'nearest', behavior: 'instant' }));
    await b.click({ timeout: 4000 }).catch(() => b.evaluate((el) => el.click()));
    if (await ok()) return 'clicked "Mobile menu toggle" to open the nav overlay';
    await page.waitForTimeout(500);
  }
  return 'clicked "Mobile menu toggle"; the overlay did not report open';
}

// Opens the help-center search: "Search…" is a fake field that opens
// Framer's __framer-search-modal-container dialog with the real input. A
// local UI toggle; nothing typed into it is submitted.
async function openSearch() {
  const t = page.locator('p').filter({ hasText: /^\s*Search…\s*$/ }).filter({ visible: true }).last();
  if (!(await t.count())) return 'no search trigger';
  for (let i = 0; i < 3; i++) {
    await t.evaluate((el) => el.scrollIntoView({ block: 'center', behavior: 'instant' }));
    await page.waitForTimeout(400);
    // A transparent <button> covers the fake field: click its centre.
    const bb = await t.boundingBox();
    if (bb) await page.mouse.click(bb.x + bb.width / 2, bb.y + bb.height / 2);
    const ok = await page.locator('.__framer-search-modal-container input, input[placeholder="Search..."]').filter({ visible: true }).count();
    if (ok) return 'clicked "Search…" to open the Framer search modal';
    await page.waitForTimeout(700);
  }
  return 'clicked "Search…"; the modal did not report open';
}

const FIELD = ['default', 'focused', 'filled'];

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('nav-header', q('div[class*="container"], header, nav').filter({ hasText: /Industries/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Marketing header', desc: 'The fixed top bar: exactly.ai wordmark, Industries/Showcase/Case studies/Pricing, Log in and the orange Start-for-free pill.', sel: 'fixed header container' }, { noScroll: true });
  await S('nav-logo', q('a[href="./"], a[href="/"], a[href="https://exactly.ai/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The exactly.ai wordmark in the header; links home.', sel: 'header logo link' }, { noScroll: true });
  await S('nav-link', q('a').filter({ hasText: /^\s*Industries\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A header link (Industries/Showcase/Case studies/Pricing); measured, never followed.', sel: 'header nav a' }, { noScroll: true });
  await S('nav-login', q('a').filter({ hasText: /^\s*Log in\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Log in link', desc: 'The Log-in link to threads.exactly.ai/signin; measured never followed.', sel: 'header Log in' }, { noScroll: true });
  await S('nav-cta', q('a').filter({ hasText: /^\s*Start for free\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Start-for-free pill', desc: 'The #fb411f orange Start-for-free pill; links to threads.exactly.ai/signin?action=create, measured never followed.', sel: 'header Start for free' }, { noScroll: true });
  const h = G.home;
  await S('hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: '"AI automation for your brand\'s daily creative work." — the display headline over the photo hero.', sel: 'h1' }, { noScroll: true });
  await S('hero-sub', q('h1 span.framer-text').filter({ hasText: /Across design, illustration/ }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero sub', desc: '"Across design, illustration and photography." — the second span inside the hero h1.', sel: 'h1 span' }, { noScroll: true });
  await S('hero-cta', q('a').filter({ hasText: /^\s*Start for free\s*$/ }).filter({ visible: true }).nth(1), B4, { group: h, title: 'Hero CTA', desc: 'The white Start-for-free pill over the hero photo; measured never followed.', sel: 'hero Start for free' });
  await S('hero-demo', q('a').filter({ hasText: /^\s*Book a demo\s*$/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Book-a-demo pill', desc: 'The translucent Book-a-demo pill beside the hero CTA; links to /book-a-demo, measured never followed.', sel: 'hero Book a demo' });
  await S('trusted-strip', q('p, div').filter({ hasText: /trusted by the best creative teams/i }).filter({ visible: true }).last(), ['default'], { group: h, title: 'Trusted-by line', desc: 'The "Trusted by the best creative teams and companies, globally" line over the logo wall (UNIQLO, Pentagram, Sony, Glossier, Nike).', sel: 'trusted-by strip' });
  await S('section-h2', q('h2').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A marketing section heading further down the home page.', sel: 'h2' });
  const f = G.footer;
  const foot = q('div, footer').filter({ hasText: /Platform license agreement/i }).filter({ hasText: /Company/ }).filter({ visible: true }).last();
  await S('footer', foot, ['default'], { group: f, title: 'Footer', desc: 'The near-black footer: Follow/Company/Industries/Policies link columns, a watermark exactly.ai wordmark and the © line.', sel: 'footer (Policies ancestor)' });
  await S('footer-col', q('p, div').filter({ hasText: /^\s*Policies\s*$/ }).filter({ visible: true }).first(), ['default'], { group: f, title: 'Footer column label', desc: 'A column heading in the footer ("Policies").', sel: 'footer column label' });
  await S('footer-link', q('a').filter({ hasText: /^\s*(Privacy policy|Cookies policy|Copyright policy|Content rules|Platform license agreement)\s*$/i }).filter({ visible: true }).first(), B4, { group: f, title: 'Footer link', desc: 'A legal link in the footer; measured, never followed.', sel: 'footer legal a' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  const g = G.pricing;
  await S('pricing-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Pricing headline', desc: '"Bring AI into your creative work to automate routine tasks."', sel: 'h1 on /pricing' }, { noScroll: true });
  await S('plan-card', q('div').filter({ hasText: /£500\s*\/\s*mo/i }).filter({ has: page.locator('a').filter({ hasText: /Start for free/ }) }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Plan card', desc: 'A plan card (Pilot): name chip, price, feature list and its Start-for-free CTA.', sel: 'plan card (price ancestor)' });
  await S('plan-name', q('h4, h5, h6, div').filter({ hasText: /^\s*(Pilot|Solo|Team|Enterprise)\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan name', desc: 'The plan-name label on a card.', sel: 'plan name heading' });
  await S('plan-price', q('em, p, div, span').filter({ hasText: /^\s*£\d+\s*\/\s*mo/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan price', desc: '"£500 / mo," on the Pilot card.', sel: 'plan price line' });
  await S('plan-feature', q('p').filter({ hasText: /custom AI workflow|asset licenses|credits \/ mo/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan feature row', desc: 'A feature line inside a plan card.', sel: 'plan feature p' });
  await S('plan-cta', q('a').filter({ hasText: /^\s*Start for free\s*$/ }).filter({ visible: true }).nth(1), B4, { group: g, title: 'Plan CTA', desc: 'A plan card\'s Start-for-free action; measured never followed.', sel: 'plan Start for free' });
  await S('plan-demo-cta', q('a').filter({ hasText: /^\s*Book a demo\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan Book-a-demo', desc: 'The dark Book-a-demo action on the enterprise cards; measured never followed.', sel: 'plan Book a demo' });
  await S('compare-bar', q('div').filter({ hasText: /Solo[\s\S]{0,40}Team[\s\S]{0,40}Enterprise/ }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Plan comparison bar', desc: 'The sticky Solo/Team/Enterprise bar that pins over the comparison table on scroll.', sel: 'sticky compare bar' });
  await S('compare-h2', q('h2').filter({ hasText: /compare our plans/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Compare heading', desc: '"Compare our plans in detail and find the right fit for your team".', sel: 'compare h2' });
  await S('faq-strip', q('div, a').filter({ hasText: /still have questions/i }).filter({ visible: true }).last(), ['default'], { group: g, title: 'FAQ strip', desc: 'The "Still have questions? Take a look at our FAQ" closing block.', sel: 'faq strip' });
  save();
}

async function showcase() {
  if (!(await newPage('showcase'))) return;
  await sheetsFor('showcase');
  await chrome('showcase');
  const g = G.showcase;
  await S('showcase-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Showcase headline', desc: '"Any brand\'s visual style, mastered. We just get what works."', sel: 'h1 on /showcase' }, { noScroll: true });
  await S('showcase-chip', q('a, p').filter({ hasText: /^\s*Tech\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Category chip', desc: 'A category tag on a brand card ("Tech"); the card links to /showcase/opal, measured never followed.', sel: 'showcase category chip' }, { allowLink: true });
  await S('showcase-card', q('a').filter({ hasText: /Opal/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Brand card', desc: 'A showcase brand card (cover image, category chip, brand name, tagline, Read more); measured, never followed.', sel: 'a /showcase/<brand> card' }, { allowLink: true });
  await S('showcase-card-title', q('h4, h3').filter({ hasText: /^\s*Opal\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Brand name', desc: 'The brand name heading on a showcase card.', sel: 'card h4' });
  await S('read-more', q('a, p').filter({ hasText: /^\s*Read more\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Read-more link', desc: 'The "Read more" caption link on a brand card; measured, never followed.', sel: 'card Read more' }, { allowLink: true });
  save();
}

async function showcaseBrand() {
  if (!(await newPage('showcase-brand'))) return;
  await sheetsFor('showcase-brand');
  await chrome('showcase-brand');
  const g = G.showcase;
  await S('brand-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Brand headline', desc: 'The brand page headline ("Revolut — Change the way you money").', sel: 'h1 on /showcase/revolut' }, { noScroll: true });
  await S('brand-chip', q('p, h2, h3, h4, span').filter({ hasText: /^\s*Financial services\s*$/ }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Brand category', desc: 'The category label on the brand page.', sel: 'brand category' });
  await S('brand-body', q('p').filter({ hasText: /global financial super-app/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Brand intro', desc: 'The brand description paragraph.', sel: 'brand intro p' });
  save();
}

async function caseStudies() {
  if (!(await newPage('case-studies'))) return;
  await sheetsFor('case-studies');
  await chrome('case-studies');
  const g = G.showcase;
  await S('cases-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Case-studies headline', desc: 'The case-studies index headline.', sel: 'h1 on /case-studies' }, { noScroll: true });
  await S('case-card', q('div').filter({ hasText: /Aspora/ }).filter({ has: page.locator('a, [role="button"], div').filter({ hasText: /^\s*Read study\s*$/ }) }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Case-study row', desc: 'A case-study row on the index: brand name, tagline, description, Read-study pill and image.', sel: 'case row (brand + Read study ancestor)' });
  await S('case-read', q('a').filter({ hasText: /^\s*Read study\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Read-study pill', desc: 'The "Read study" pill on a case-study row — the outer anchor that paints the grey fill, not the text box inside it; measured, never followed.', sel: 'Read study pill (outer a)' }, { allowLink: true });
  save();
}

async function caseStudy() {
  if (!(await newPage('case-study'))) return;
  await sheetsFor('case-study');
  await chrome('case-study');
  const g = G.showcase;
  await S('article-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Article headline', desc: 'The case-study article headline.', sel: 'article h1' }, { noScroll: true });
  await S('article-body', q('p').filter({ hasText: /inDrive is one of the fastest/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Article body', desc: 'A body paragraph in the article prose.', sel: 'article p' });
  await S('article-h2', q('h2, h3').filter({ hasText: /.{10,}/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Article heading', desc: 'A section heading inside the article.', sel: 'article h2/h3' });
  save();
}

async function industries() {
  if (!(await newPage('industries'))) return;
  await sheetsFor('industries');
  await chrome('industries');
  const g = G.industries;
  await S('industries-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Industries headline', desc: 'The industries index headline.', sel: 'h1 on /industries' }, { noScroll: true });
  await S('industry-card', q('a').filter({ hasText: /grocery|meal|saas|tech/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Industry card', desc: 'An industry card on the index; measured, never followed.', sel: 'industry card a' }, { allowLink: true });
  save();
}

async function industry() {
  if (!(await newPage('industry'))) return;
  await sheetsFor('industry');
  const g = G.industries;
  await S('industry-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Industry headline', desc: 'The industry page headline.', sel: 'h1 on /industries/saas-n-mobile-apps' }, { noScroll: true });
  await S('industry-body', q('p').filter({ hasText: /.{60,}/ }).filter({ visible: true }).nth(1), ['default'], { group: g, title: 'Industry body', desc: 'A body paragraph on the industry page.', sel: 'industry p' });
  save();
}

async function helpCenter() {
  if (!(await newPage('help-center'))) return;
  await sheetsFor('help-center');
  await chrome('help-center');
  const g = G.help;
  await S('help-sidebar', q('div').filter({ hasText: /Getting started/ }).filter({ hasText: /AI style transfer/ }).filter({ hasText: /Editing & Controls/ }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Help sidebar', desc: 'The left doc rail: Getting started, AI style transfer, Library and more groups of article links.', sel: 'help sidebar rail' }, { noScroll: true, crop: false });
  await S('help-nav-group', q('p, div').filter({ hasText: /^\s*Getting started\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav group label', desc: 'A sidebar group label ("Getting started").', sel: 'sidebar group label' }, { noScroll: true });
  await S('help-nav-link', q('a').filter({ hasText: /^\s*Overview\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sidebar link', desc: 'A sidebar article link; measured, never followed.', sel: 'sidebar a' }, { noScroll: true });
  await S('help-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Help headline', desc: '"Help center".', sel: 'h1 on /help-center' }, { noScroll: true });
  await S('help-search', q('div[class*="-container"]').filter({ has: page.locator('p').filter({ hasText: /^\s*Search…\s*$/ }) }).filter({ visible: true }).last(), B4, { group: g, title: 'Search trigger', desc: 'The "Search…" affordance on the help landing: a rounded field that opens the Framer search modal when its overlay button is clicked (a local UI toggle).', sel: 'help "Search…" field container' });
  await S('help-search-input', q('.__framer-search-modal-container input, input[placeholder="Search..."]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Search field', desc: 'The real input inside the Framer search modal; focused and typed into then cleared — never submitted.', sel: 'search modal input' }, { open: openSearch, fillText: 'train a style' });
  await page.keyboard.press('Escape').catch(() => {});
  await S('help-card', q('a').filter({ hasText: /articles/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Article-collection card', desc: 'A collection card ("FAQ — Get quick answers — 12 articles"); measured, never followed.', sel: 'help collection card a' }, { allowLink: true });
  save();
}

async function helpFaq() {
  if (!(await newPage('help-faq'))) return;
  await sheetsFor('help-faq');
  const g = G.help;
  await S('faq-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'FAQ headline', desc: '"Frequently asked questions" — the FAQ article page.', sel: 'h1 on /help-center/frequently-asked-questions' }, { noScroll: true });
  await S('faq-question', q('h3').filter({ hasText: /What are credits and licenses\?/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'FAQ question', desc: 'An anchor-linked question heading inside the FAQ article (H3).', sel: 'faq h3' });
  await S('faq-answer', q('p').filter({ hasText: /credits are used to pay/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'FAQ answer', desc: 'The answer paragraph under a question heading.', sel: 'faq answer p' });
  await S('article-link', q('#help-center-rich-text a').filter({ hasText: /./ }).filter({ visible: true }).first(), B4, { group: g, title: 'Inline link', desc: 'The "Data protection & privacy" link inside the FAQ article prose (the #help-center-rich-text body); measured, never followed.', sel: '#help-center-rich-text a' });
  save();
}

async function bookADemo() {
  if (!(await newPage('book-a-demo', { wait: 12000 }))) return;
  await chrome('book-a-demo');
  const g = G.demo;
  await S('demo-h1', q('h1, h2, p').filter({ hasText: /See how exactly\.ai works/i }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Demo headline', desc: '"See how exactly.ai works. Let us help you scale your creative processes."', sel: 'demo headline' }, { noScroll: true });
  await S('demo-scheduler', q('iframe').first(), ['default'], { group: g, title: 'Scheduler embed', desc: 'The embedded scheduling widget (a Calendly-style day picker in a srcdoc iframe): measured as a region at rest — no day, time or contact detail was ever picked or typed.', sel: 'scheduler iframe' }, { noScroll: true, crop: false });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-topbar', q('div[class*="container"], header, nav').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile top bar', desc: 'The phone top bar: exactly.ai wordmark, Join pill, hamburger.', sel: 'mobile header' }, { noScroll: true });
  await S('m-join', q('a, [role="button"]').filter({ hasText: /^\s*Join\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Join pill', desc: 'The white Join pill in the phone top bar; measured never followed.', sel: 'mobile Join' }, { noScroll: true });
  const ham = q('div[aria-label="Mobile menu toggle"]').filter({ visible: true }).last();
  await S('m-hamburger', ham, [...B4, 'opened'], { group: g, title: 'Mobile hamburger', desc: 'The burger that opens the phone nav overlay — a local UI toggle; the opened state was measured after tapping it.', sel: 'Mobile menu toggle' }, { noScroll: true, allowLink: true });
  await S('m-drawer-link', q('a').filter({ hasText: /^\s*(Industries|Showcase|Pricing)\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Drawer link', desc: 'A nav link inside the opened overlay; measured, never followed.', sel: 'drawer a' }, { open: openBurgerMenu, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await S('m-hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero headline', desc: 'The hero display at 390 wide.', sel: 'mobile h1' });
  await S('m-hero-cta', q('a').filter({ hasText: /^\s*Start for free\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile hero CTA', desc: 'The white Start-for-free pill over the phone hero; measured never followed.', sel: 'mobile Start for free' });
  await S('m-hero-demo', q('a').filter({ hasText: /^\s*Book a demo\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile demo pill', desc: 'The translucent Book-a-demo pill on the phone hero; measured never followed.', sel: 'mobile Book a demo' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); every captured surface paints the single light theme';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, showcase, 'showcase-brand': showcaseBrand, 'case-studies': caseStudies, 'case-study': caseStudy, industries, industry, 'help-center': helpCenter, 'help-faq': helpFaq, 'book-a-demo': bookADemo, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions, so the delta is meaningful: the footer
  // links' 0.2s colour transition (the CTAs and the first `a` declare none).
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'a', /^(Privacy policy|Cookies policy|Copyright policy|Content rules|Platform license agreement)$/);
} finally {
  for (const [key, c] of Object.entries(out.components)) {
    // An untouched entry is pruned only when its page finished this run: a
    // page the run never reached, and an edge-blocked route, keeps its earlier
    // readings under their original provenance instead of being erased and
    // republished.
    if (!touched.has(key) && !pages.length && finishedPages.has(c.page) && !failedPages.has(c.page)) { delete out.components[key]; continue; }
    const want = listed.get(key);
    if (want) for (const st of Object.keys(c.states || {})) if (!want.has(st)) delete c.states[st];
  }
  save();
  await browser.close();
}
console.log('components-computed.json:', Object.keys(out.components).length, 'components');
