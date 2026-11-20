// Measures delphi.co's public components in every state reachable without
// signing in, asking a question or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home discover search expert chat mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// delphi.co is a single light theme signed out: the marketing/search home,
// /discover/<topic> galleries, public /search/<question> results, public
// expert profiles (/<expert>) and public chat surfaces (/<expert>/chat). The
// css-* classes are hashed Tailwind utilities, so specs select by role,
// aria-label, structure or text. Nothing is sent or signed into: the only
// presses are local UI toggles — the Sign-In dialog and a perspective card's
// Read/Back flip; the search fields are typed into and cleared, never
// submitted; Sign In, Create Your Delphi, Continue with Google/Email, the
// suggested-question chips and every send/ask control are measured, never
// followed. No consent overlay was seen.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', discover: '/discover/productivity', search: '/search/i-want-to-bring-my-different-groups-of-friends-together-and-buil', expert: '/karpathy', chat: '/karpathy/chat', mobile: '/' };
// chat opens without a ?handoff= query: a handoff can post the handed-off
// question into a live AI chat on load, signed out. The composer is filled and
// cleared locally, never submitted.
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes PerimeterX gates this run: components last measured on them keep their
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

// A failed re-read must not erase an earlier successful one: keep the saved
// style and record the failed attempt beside it. comp() has already stamped
// this run's date on the component, so the kept state is pinned to the run
// that actually read it (its own run stamp, else the component's earlier run)
// and an old reading is never republished as a new one.
function keepEarlier(c, state, e, earlierRun) {
  const err = String(e.message || e).slice(0, 200);
  const prev = c.states[state];
  if (prev && prev.style) {
    prev.rerunError = err;
    prev.read ??= prev.run || earlierRun; // a second failed re-read keeps the first date
    prev.rerunOn = run;
  } else c.states[state] = { error: err };
}

async function measure(key, state, target, opts = {}) {
  const loc = target.and(page.locator(':visible')).first();
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    let file;
    if (opts.crop !== false) {
      try {
        file = await crop(page, (opts.cropLoc || loc).and(page.locator(':visible')).first(), `${key}-${state}`, opts.pad ?? 8);
      } catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
    }
    c.states[state] = { ...s, crop: file, via: opts.via };
    if (opts.extra) c.states[state].extra = await opts.extra(loc);
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    keepEarlier(c, state, e, opts.earlierRun);
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
  const loc = target.and(page.locator(':visible')).first();
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
        await (opts.hoverLoc || loc).and(page.locator(':visible')).first().hover({ timeout: 5000 }).catch(() => (opts.hoverLoc || loc).and(page.locator(':visible')).first().hover({ timeout: 5000, force: true }));
        await page.waitForTimeout(450);
        via = 'mouse hover';
      } else if (st === 'focus-visible') {
        via = await kbFocus((opts.focusLoc || loc).and(page.locator(':visible')).first());
      } else if (st === 'pressed') {
        undo = await forcePseudo((opts.pressLoc || loc).and(page.locator(':visible')).first(), ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else if (st === 'focused') {
        const fld = (opts.fieldLoc || loc).and(page.locator(':visible')).first();
        await fld.click({ timeout: 4000 }).catch(() => fld.evaluate((el) => el.focus()));
        await page.waitForTimeout(400);
        via = 'clicked into the field';
      } else if (st === 'filled') {
        const f = (opts.fieldLoc || loc).and(page.locator(':visible')).first();
        await f.click({ timeout: 4000 }).catch(() => f.evaluate((el) => el.focus()));
        await page.keyboard.type(opts.fillText || 'name@example.com', { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || 'name@example.com'}", then deleted; nothing sent`;
      } else if (st === 'opened') {
        if (opts.noToggle) via = 'held open by an earlier toggle';
        else { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle'; }
      } else via = via || 'at rest';
      await measure(key, st, loc, { ...opts, via, earlierRun: keep?.run });
    } catch (e) {
      keepEarlier(out.components[key], st, e, keep?.run);
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  await reset();
}

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|claim this offer|try again)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.and(page.locator(':visible')).first();
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
async function reducedMotion(key, sel) {
  out._meta.reducedMotion ??= {};
  try {
    const b = context.browser();
    const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', reducedMotion: 'reduce' });
    await patch(ctx);
    const p = await ctx.newPage();
    await p.goto(URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
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
  shell: 'Header and navigation', home: 'Home', dialog: 'Auth and onboarding dialogs',
  discover: 'Discover galleries', search: 'Search results', expert: 'Expert profile',
  chat: 'Chat surface', mobile: 'Mobile (390 wide)', footer: 'Footer',
};

// Opens the Sign-In dialog: the header "Sign In" link routes through /auth
// and lands back on home with the auth dialog mounted. The dialog's buttons
// (Continue with Google / Continue with Email) are measured, never pressed.
async function openSignin() {
  const shown = () => page.waitForFunction(() => {
    const d = document.querySelector('[role="dialog"]');
    return d && d.getBoundingClientRect().height > 100 && /google|email/i.test(d.innerText || '');
  }, undefined, { timeout: 8000 }).then(() => true).catch(() => false);
  if (await shown()) return 'the sign-in dialog was already open';
  const t = page.locator('a,button').filter({ hasText: /^\s*Sign In\s*$/ }).and(page.locator(':visible')).first();
  if (!(await t.count())) return 'no Sign In control';
  for (let i = 0; i < 3; i++) {
    await t.click({ timeout: 4000 }).catch(() => t.evaluate((el) => el.click()));
    await page.waitForTimeout(1500);
    if (await shown()) return 'clicked "Sign In" to open the auth dialog';
  }
  return 'clicked "Sign In"; the dialog did not report open';
}

// Flips a portrait card: "Read <name>'s perspective" is a local UI toggle on
// the home rail; the flip's back side is measured as its opened state.
async function openPerspective() {
  const flipped = (ms) => page.waitForFunction(() =>
    [...document.querySelectorAll('[class*="perspective-flip" i]')].some((el) => /back/i.test(el.className) || getComputedStyle(el).transform !== 'none'),
    undefined, { timeout: ms }).then(() => true).catch(() => false);
  if (await flipped(400)) return 'a perspective card was already flipped';
  const b = page.locator('button[aria-label*="perspective" i]').and(page.locator(':visible')).first();
  if (!(await b.count())) return 'no perspective trigger';
  for (let i = 0; i < 3; i++) {
    await b.click({ timeout: 4000 }).catch(() => b.evaluate((el) => el.click()));
    await page.waitForTimeout(1200);
    if (await flipped(800)) return 'clicked "Read perspective" to flip the card';
  }
  return 'clicked "Read perspective"; the flip did not report';
}

const FIELD = ['default', 'focused', 'filled'];

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('mkt-header', q('header.fixed, header').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Site header', desc: 'The fixed top bar: Delphi wordmark, Sign In and the Create Your Delphi pill.', sel: 'header.fixed' }, { noScroll: true });
  await S('mkt-logo', q('header a, header svg').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Logo', desc: 'The Delphi mark at the left of the header.', sel: 'header logo' }, { noScroll: true });
  await S('nav-topic', q('header a, nav a, a.shrink-0').filter({ hasText: /^\s*(Career|Money|Love|Growth)/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Topic link', desc: 'A topic link in the header/category strip ("Career & Work"); measured, never followed.', sel: 'topic link' }, { noScroll: true });
  await S('signin-btn', q('header a, header button, a').filter({ hasText: /^\s*Sign In\s*$/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Sign In', desc: 'The header Sign-In action; it opens the auth dialog (measured below), never followed past it.', sel: 'header Sign In' }, { noScroll: true });
  await S('create-cta', q('header a, a').filter({ hasText: /Create Your Delphi/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Create CTA', desc: 'The "Create Your Delphi" primary pill in the header; measured, never followed (it starts onboarding).', sel: 'header Create Your Delphi' }, { noScroll: true });
  const h = G.home;
  await S('hero-h1', q('h1.font-heading, h1').and(page.locator(':visible')).first(), ['default'], { group: h, title: 'Hero headline', desc: '"Find people who\u2019ve been there" — the Pythia serif display heading.', sel: 'h1.font-heading' }, { noScroll: true });
  await S('hero-search', q('textarea[aria-label="Search Delphi"], textarea').and(page.locator(':visible')).first(), FIELD, { group: h, title: 'Ask field', desc: 'The "Describe your situation" hero textarea — the product\u2019s front door; focused and typed into then cleared, never submitted.', sel: 'textarea[aria-label=Search Delphi]' }, { noScroll: true, fillText: 'how do i find a co-founder' });
  await S('mic-btn', q('button[aria-label*="Say" i], button[aria-label*="record" i]').and(page.locator(':visible')).first(), B4, { group: h, title: 'Voice button', desc: 'The "Say your situation" mic button beside the ask field; measured, never pressed (it would start recording).', sel: 'Say your situation' }, { noScroll: true });
  await S('topic-card', q('button.deck-card.topic-card, .topic-card, button[class*="deck-card" i]').and(page.locator(':visible')).first(), B4, { group: h, title: 'Topic card', desc: 'A shuffled topic card ("Ask ex-Googlers about scaling under pressure"); measured, never pressed.', sel: 'button.deck-card.topic-card' });
  await S('persp-card', q('div.perspective-flip-front, [class*="perspective-flip" i]').and(page.locator(':visible')).first(), ['default'], { group: h, title: 'Expert card', desc: 'An expert portrait card on the home rail (name, claim, the Read-perspective flip).', sel: 'div.perspective-flip-front' });
  await S('persp-flip', q('button[aria-label*="perspective" i]').and(page.locator(':visible')).first(), B4, { group: h, title: 'Perspective flip', desc: 'The "Read <name>\u2019s perspective" card toggle — a local flip, never a navigation.', sel: 'button[aria-label*=perspective]' });
  await S('persp-quote', q('blockquote.font-heading, blockquote').and(page.locator(':visible')).first(), ['default'], { group: h, title: 'Perspective quote', desc: 'A quoted perspective on a card ("Nir on why we reach for our phones...").', sel: 'blockquote.font-heading' });
  await S('section-h2', q('h2').filter({ hasText: /Ask people who|Ask the experts/ }).and(page.locator(':visible')).first(), ['default'], { group: h, title: 'Section heading', desc: 'A home section heading ("Ask people who\u2019ve lived it").', sel: 'h2' });
  const f = G.footer;
  await S('site-footer', q('footer').and(page.locator(':visible')).last(), ['default'], { group: f, title: 'Site footer', desc: 'The sitemap footer (Discover / About Delphi / Blog / Premium...).', sel: 'footer' });
  // The Sign-In dialog is opened last: it mounts over the page and its
  // buttons are measured, never pressed. Escape closes it.
  const d = G.dialog;
  await S('signin-dialog', q('[role="dialog"]').filter({ hasText: /google|email/i }).and(page.locator(':visible')).last(), ['default'], { group: d, title: 'Sign-in dialog', desc: 'The auth dialog opened by the header Sign In (Continue with Google / Continue with Email); its buttons were measured, never pressed.', sel: '[role=dialog]' }, { open: openSignin, noScroll: true, noReset: true });
  await S('dialog-google', q('[role="dialog"] button, [role="dialog"] a').filter({ hasText: /Continue with Google/i }).and(page.locator(':visible')).first(), B4, { group: d, title: 'Google SSO button', desc: '"Continue with Google" inside the auth dialog; measured, never pressed.', sel: 'Continue with Google' }, { noScroll: true, noReset: true });
  await S('dialog-email', q('[role="dialog"] button, [role="dialog"] a').filter({ hasText: /Continue with Email/i }).and(page.locator(':visible')).first(), B4, { group: d, title: 'Email button', desc: '"Continue with Email" inside the auth dialog; measured, never pressed.', sel: 'Continue with Email' }, { noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  save();
}

async function discover() {
  if (!(await newPage('discover'))) return;
  await sheetsFor('discover');
  await chrome('discover');
  const g = G.discover;
  await S('disc-h1', q('h1.font-heading, h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Gallery headline', desc: '"Productivity advice from people who\u2019ve been there" — the topic gallery heading.', sel: 'h1.font-heading' }, { noScroll: true });
  await S('disc-cats', q('.hl-topic-ripples, [class*="hl-ripples" i], [class*="topic" i]').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Topic chip strip', desc: 'The category chip strip under the gallery heading (Career & Work / Money & Business / ...).', sel: '.hl-topic-ripples' }, { noScroll: true });
  await S('disc-cat', q('a.shrink-0, a').filter({ hasText: /^\s*(Career|Money|Love|Growth)/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Topic chip', desc: 'A category chip in the gallery strip; measured, never followed.', sel: 'topic chip' }, { noScroll: true });
  await S('disc-quote', q('blockquote.font-heading, blockquote').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Gallery quote', desc: 'A quoted expert perspective in the gallery.', sel: 'blockquote' });
  await S('disc-card', q('img.portrait-img, img').and(page.locator(':visible')).first().locator('xpath=ancestor::*[self::a or self::article or contains(@class,"card")][1]'), ['default'], { group: g, title: 'Expert tile', desc: 'An expert portrait tile in the gallery grid.', sel: 'portrait card' });
  await S('disc-ask', q('button.deck-card.topic-card, button[class*="deck-card" i]').and(page.locator(':visible')).first(), B4, { group: g, title: 'Ask card', desc: 'A gallery "Ask <group> about <topic>" card; measured, never pressed.', sel: 'button.deck-card.topic-card' });
  save();
}

async function search() {
  if (!(await newPage('search', { wait: 10000 }))) return;
  await sheetsFor('search');
  await chrome('search');
  const g = G.search;
  await S('srch-field', q('textarea').and(page.locator(':visible')).first(), ['default', 'focused'], { group: g, title: 'Query field', desc: 'The large query textarea at the top of results, pre-filled with the asked question; focused, never submitted.', sel: 'results textarea' }, { noScroll: true });
  await S('srch-top', q('h3:not(.sr-only), span').filter({ hasText: /^\s*Top perspectives\s*$/ }).and(page.locator(':visible')).last(), ['default'], { group: g, title: 'Top perspectives', desc: 'The "Top perspectives" results heading over the quoted answers.', sel: 'Top perspectives' }, { noScroll: true });
  await S('srch-personalize', q('a, button').filter({ hasText: /Personalize your results/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Personalize link', desc: 'The "Personalize your results" action; measured, never followed.', sel: 'Personalize your results' }, { noScroll: true });
  await S('srch-quote', q('blockquote.perspective-bubble, blockquote').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Result quote', desc: 'A quoted expert answer in the results.', sel: 'blockquote' });
  await S('srch-expert-card', q('blockquote.perspective-bubble').and(page.locator(':visible')).first().locator('xpath=ancestor::*[contains(@class,"bg-surface-primary")][1]'), ['default'], { group: g, title: 'Result expert card', desc: 'An expert result card (portrait, name, role, badges, quoted answer, Save/Expand).', sel: 'result card' });
  await S('srch-badge', q('span.brand-tag').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Credential badge', desc: 'A credential badge on a result card ("VP OF GLOBAL COMMUNITY AT TORC").', sel: 'span.brand-tag' });
  await S('srch-save', q('a, button').filter({ hasText: /^\s*Save\s*$/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Save button', desc: 'The card\u2019s "Save" action; measured, never pressed.', sel: 'Save' });
  await S('srch-expand', q('a, button').filter({ hasText: /^\s*Expand/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Expand button', desc: 'The orange "Expand" card action; measured, never followed.', sel: 'Expand' });
  save();
}

async function expert() {
  if (!(await newPage('expert'))) return;
  await sheetsFor('expert');
  await chrome('expert');
  const g = G.expert;
  await S('exp-name', q('h1').filter({ hasText: /Andrej Karpathy/ }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Expert name', desc: 'The expert\u2019s display name heading on their public profile.', sel: 'expert h1' }, { noScroll: true });
  await S('exp-portrait', q('img.object-cover, img.portrait-img, img').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Expert portrait', desc: 'The expert\u2019s portrait photo in the profile header.', sel: 'profile img' }, { noScroll: true });
  await S('share-btn', q('main button').filter({ hasText: /^\s*Share\s*$/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Share button', desc: 'The "Share" profile action; measured, never pressed.', sel: 'Share' });
  await S('exp-about', q('p, div, span').filter({ hasText: /I\u2019m founder of Eureka Labs|founder of Eureka Labs/i }).and(page.locator(':visible')).last(), ['default'], { group: g, title: 'About text', desc: 'The expert\u2019s About copy on the profile.', sel: 'about text' });
  await S('exp-section', q('h2:not(.sr-only)').filter({ hasText: /^\s*Experiences\s*$/ }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Profile section', desc: 'A profile section heading ("Experiences").', sel: 'profile h2' });
  await S('exp-exp-item', q('div, li').filter({ hasText: /Eureka Labs|Director of AI at Tesla/i }).and(page.locator(':visible')).last(), ['default'], { group: g, title: 'Experience item', desc: 'A listed experience on the profile.', sel: 'experience item' });
  save();
}

async function chat() {
  if (!(await newPage('chat', { wait: 10000 }))) return;
  await sheetsFor('chat');
  await chrome('chat');
  const g = G.chat;
  await S('chat-name', q('header *, h1, h2, a, span, div').filter({ hasText: /^\s*Andrej Karpathy\s*$/ }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Chat expert name', desc: 'The expert\u2019s name in the chat header.', sel: 'chat header name' }, { noScroll: true });
  await S('chat-greeting', q('div, p').filter({ hasText: /What problem|Start a conversation/i }).and(page.locator(':visible')).last(), ['default'], { group: g, title: 'Greeting bubble', desc: 'The clone\u2019s opening message ("Hi there. What problem you trying to solve?").', sel: 'greeting bubble' });
  await S('suggested-label', q('div, span, p, h2').filter({ hasText: /^\s*Suggested\s*$/ }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Suggested label', desc: 'The "Suggested" label over the starter questions.', sel: 'Suggested' });
  await S('suggested-chip', q('button').filter({ hasText: /What are you building|Rubik|hardest problems/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Suggested question', desc: 'A suggested starter question chip; measured, never pressed — pressing it would send the question.', sel: 'suggested chip' });
  await S('chat-input', q('textarea[placeholder*="Send a message" i], textarea[aria-label*="Send a message" i], textarea').and(page.locator(':visible')).last(), FIELD, { group: g, title: 'Message field', desc: 'The "Send a message..." composer; focused and typed into then cleared, never submitted.', sel: 'chat textarea' }, { fillText: 'what should i learn next' });
  const sendField = q('textarea').and(page.locator(':visible')).last();
  await sendField.fill('what should i learn next').catch(() => {});
  await page.waitForTimeout(600);
  await S('chat-send', q('button[type="submit"], button[aria-label*="Submit message" i]').and(page.locator(':visible')).last(), B4, { group: g, title: 'Send button', desc: 'The composer submit button — it only renders once text is in the field; its states were measured but it was never pressed, and the text was cleared.', sel: 'send button' });
  await sendField.fill('').catch(() => {});
  await page.waitForTimeout(400);
  await S('scroll-bottom', q('button').filter({ hasText: /Scroll to bottom/i }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Scroll-to-bottom', desc: 'The "Scroll to bottom" helper pill; measured, never pressed.', sel: 'Scroll to bottom' });
  await S('chat-terms', q('p').filter({ hasText: /By using this service/i }).and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Terms line', desc: 'The "By using this service, you..." terms line under the composer.', sel: 'chat terms' });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('header.fixed, header').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Mobile header', desc: 'The phone top bar: wordmark, Sign In, Create pill.', sel: 'mobile header' }, { noScroll: true });
  await S('m-signin', q('header a, header button, a').filter({ hasText: /^\s*Sign In\s*$/ }).and(page.locator(':visible')).first(), B4, { group: g, title: 'Mobile Sign In', desc: 'The Sign-In action on the phone header; measured, never followed.', sel: 'mobile Sign In' }, { noScroll: true });
  await S('m-h1', q('h1.font-heading, h1').and(page.locator(':visible')).first(), ['default'], { group: g, title: 'Mobile headline', desc: 'The phone hero heading.', sel: 'mobile h1' });
  await S('m-search', q('textarea[aria-label="Search Delphi"], textarea').and(page.locator(':visible')).first(), FIELD, { group: g, title: 'Mobile ask field', desc: 'The ask textarea on the phone hero; focused and typed then cleared, never submitted.', sel: 'mobile textarea' }, { fillText: 'how do i sleep better' });
  await S('m-topic-card', q('button.deck-card.topic-card, button[class*="deck-card" i]').and(page.locator(':visible')).first(), B4, { group: g, title: 'Mobile topic card', desc: 'A topic card on the phone rail; measured, never pressed.', sel: 'mobile topic card' });
  await S('m-footer', q('footer').and(page.locator(':visible')).last(), ['default'], { group: g, title: 'Mobile footer', desc: 'The phone footer.', sel: 'mobile footer' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); delphi.co paints a single light theme signed out';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, discover, search, expert, chat, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (the Create CTA's
  // hover), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', 'header a, a');
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
