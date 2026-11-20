// Measures fable.co's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home clubs book club signin support mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// fable.co paints two skins on one light product. The marketing pages
// (/, /signin, /support) are emotion-styled (hashed css-* classes): the cream
// forest-green hero under a transparent fixed header, Heldane Display
// mastheads, Inter body. The catalog pages (/clubs, /books, /book/*, /club/*)
// are CSS-module styled with readable names — Header-module, HeaderNav-module,
// HeaderLogo-module, Button-module, IconButton-module, Text-module,
// Modal-module, SearchModal-module, ClubsIndexGenrePills-module,
// ClubCard-module, BookCarouselItem-module, FaqAccordion-module — so specs
// there select by the readable module name; marketing specs select by role,
// aria-label and text. /discover is a whole-page dark cover wall. Nothing is
// sent, bought, joined or signed into: the only presses are local UI toggles —
// the /clubs "Search thousands of book and TV clubs" aria-haspopup="dialog"
// trigger, the book page's "May contain spoilers!" disclosure, a "Read more"
// ExpandableText toggle and one FAQ accordion question. The sign-in fields are
// typed into and cleared, never submitted; "Want to read", "Download the app
// to join", "Login with email", "Continue with Google/Apple", every nav and
// store link and "Your Privacy Choices" are measured, never followed. The
// Osano consent banner is hidden, never answered. The phone's off-canvas nav
// drawer is opened through its div[aria-label="Open menu"] hamburger — a
// local UI toggle — and measured in its opened state.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, BOOK_URL, CLUB_URL, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = { home: '/', clubs: '/clubs', book: BOOK_URL, club: CLUB_URL, signin: '/signin', support: '/support', discover: '/discover', mobile: '/' };
let page, cdp, current, context, run, liveCtx;
const touched = new Set();
const listed = new Map();
// Routes an edge block gates this run: components last measured on them keep
// their earlier readings instead of being pruned below (a blocked pass must
// never erase evidence).
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
  const loaded = await open(page, url || (URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key]), { wait, promo });
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
        await f.click({ timeout: 4000 }).catch(() => f.evaluate((el) => el.focus()));
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
      const prev = out.components[key].states[st];
      if (prev && prev.style) prev.rerunError = String(e.message || e).slice(0, 200);
      else out.components[key].states[st] = { error: String(e.message).slice(0, 200) };
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

// Clicks a UI toggle (dropdown, disclosure, accordion, dialog trigger).
// Refuses a submit button and any control whose text names an action this kit
// must never take.
const NEVER = /^(send|send message|submit|sign in|log ?in|login|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|continue with.*|want to read|reset it|sign up|get the app|shop|shop .*ebooks)$/i;
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
async function reducedMotion(key, sel) {
  out._meta.reducedMotion ??= {};
  try {
    const b = context.browser();
    const ctx = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', reducedMotion: 'reduce' });
    await patch(ctx);
    const p = await ctx.newPage();
    await p.goto(URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key], { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(12000);
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
  shell: 'Site chrome', home: 'Home', clubs: 'Clubs index', book: 'Book detail',
  club: 'Club detail', signin: 'Sign-in', support: 'Support', mobile: 'Mobile (390 wide)',
  footer: 'Footer', modal: 'Club search modal', promo: 'App-install prompt',
  discover: 'Discover (dark)',
};

// Opens the /clubs search dialog: its trigger is an aria-haspopup="dialog"
// button — a local UI toggle, never a submit. Click, then keyboard Enter as a
// fallback; Escape closes afterwards.
async function openSearchDialog() {
  const btn = page.locator('button[aria-haspopup="dialog"]').filter({ hasText: /Search thousands/i }).first();
  if (!(await btn.count())) return 'no search trigger';
  // Osano mounts its own role="dialog" nodes, so count only a visible,
  // non-consent dialog.
  const open = () => page.evaluate(() => !![...document.querySelectorAll('[role="dialog"]')].find((x) => !/osano/i.test(x.className) && x.getBoundingClientRect().width > 100));
  if (await open()) return 'the search dialog was already open';
  for (let i = 0; i < 3; i++) {
    if (i === 0) await btn.click({ timeout: 4000 }).catch(() => btn.evaluate((el) => el.click()));
    else { await btn.focus(); await page.keyboard.press('Enter'); }
    await page.waitForTimeout(900);
    if (await open()) return 'clicked the "Search thousands of book and TV clubs" button to open the modal';
  }
  return 'activated the search trigger; the dialog did not report open';
}

// The catalog pages' header pieces, shared by /clubs, /book/* and /club/*.
async function catalogShell(g) {
  await S('cat-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Catalog header', desc: 'The fixed 60px catalog top bar: the heldane "Fable" wordmark, nav links (Clubs / Books / Library / Blog) and the sign-in icon.', sel: 'header.Header-module' }, { noScroll: true });
  await S('cat-logo', q(`a${M('HeaderLogo-module')}`).filter({ visible: true }).first(), ['default'], { group: g, title: 'Fable wordmark (catalog)', desc: 'The catalog header wordmark link — heldane bold type, "Fable home".', sel: 'a.HeaderLogo-module' }, { noScroll: true });
  await S('cat-nav-link', q(`a${M('HeaderNav-module')}`).filter({ hasText: /^Clubs$/ }).first(), B4, { group: g, title: 'Catalog nav link', desc: 'A catalog header nav link (Clubs) — a 60px-tall cell; measured, never followed.', sel: 'a.HeaderNav-module__link Clubs' }, { noScroll: true });
  await S('cat-signin', q(`a${M('HeaderUserMenu-module')}`).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-in icon (catalog)', desc: 'The 36x36 "Sign up or log in" avatar icon linking to /signin; measured, never followed.', sel: 'a.HeaderUserMenu-module__signInIcon' }, { noScroll: true });
}

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('mkt-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Marketing header', desc: 'The fixed transparent top bar over the green hero: Fable wordmark, Clubs/Books/Library/Blog links, the "Sign up or log in" and cart icons.', sel: 'header[data-header]' }, { noScroll: true });
  await S('mkt-logo', q('header a[aria-label="Home"], header a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Fable logo (marketing)', desc: 'The Fable mark-and-wordmark svg in the marketing header — a dark-green rounded square of rainbow book spines with cream letterforms.', sel: 'header a[aria-label=Home]' }, { noScroll: true });
  await S('mkt-nav-link', q('header a').filter({ hasText: /^Clubs$/ }).first(), B4, { group: g, title: 'Nav link (marketing)', desc: 'A marketing header nav link; measured, never followed.', sel: 'header a Clubs' }, { noScroll: true });
  await S('mkt-signin', q('button[aria-label="Sign up or log in"]').filter({ visible: true }).first(), B4, { group: g, title: 'Sign-in icon (marketing)', desc: 'The 24px "Sign up or log in" icon button; its states were measured but it was never clicked — the sign-in flow is a gap, not a state.', sel: 'button[aria-label="Sign up or log in"]' }, { noScroll: true });
  await S('mkt-cart', q('button[aria-label="Shopping cart"]').filter({ visible: true }).first(), B4, { group: g, title: 'Cart icon', desc: 'The 32px "Shopping cart" icon button; measured, never clicked.', sel: 'button[aria-label="Shopping cart"]' }, { noScroll: true });
  const h = G.home;
  await S('hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: '"The modern app for every reader" — the Heldane Display 72px cream masthead on the forest-green cover-wall hero.', sel: 'h1' }, { noScroll: true });
  // Cover-wall tiles past ~x1300 sit outside the 1440 viewport, so pick one
  // comfortably inside.
  await S('hero-cover', q('a[href*="/discover"]').filter({ visible: true }).nth(6), ['default', 'hover'], { group: h, title: 'Hero book cover', desc: 'One book-cover tile in the hero cover wall, linking into the dark /discover app; measured, never followed.', sel: 'a[href*="/discover"]' });
  await S('getapp-hero', q('button').filter({ hasText: /^Get the app$/ }).filter({ visible: true }).first(), B4, { group: h, title: 'Get the app (hero)', desc: 'The white "Get the app" pill on the green hero (radius 60, white-on-green); measured, never clicked.', sel: 'hero Get the app' }, { noScroll: true });
  await S('getapp-dark', q('button').filter({ hasText: /^Get the app$/ }).filter({ visible: true }).nth(1), B4, { group: h, title: 'Get the app (on light)', desc: 'The dark-ink "Get the app" pill used on the light feature sections; measured, never clicked.', sel: 'feature Get the app' });
  await S('section-h2', q('h2').filter({ hasText: /Track your books|Visualize your reading/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Section headline', desc: 'A Heldane Display 80px marketing section heading ("Track your books in one place").', sel: 'h2 section' });
  await S('feature-h', q('h2').filter({ hasText: /Build a habit with streaks|Import your goodreads/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Feature card heading', desc: 'A 24px Inter semibold feature-card heading inside a marketing section.', sel: 'feature card h2' });
  await S('fortune-quote', await domFind(page, /more thoughtful|less toxic/i, { sel: 'blockquote, q, figure, p, div, span', tag: 'fq' }), ['default'], { group: h, title: 'Press quote', desc: 'The Fortune pull-quote — "A more thoughtful—and less toxic—social media app".', sel: 'press quote block' });
  await S('club-card', q('[data-testid="club-card"], [data-testid="club-card"] a').filter({ visible: true }).first(), ['default', 'hover'], { group: h, title: 'Club card', desc: 'A "Popular clubs" card — hero image, club cover thumb, moderator line, member count.', sel: '[data-testid=club-card]' });
  await S('getapp-cta', q('button').filter({ hasText: /^Get the app$/ }).filter({ visible: true }).last(), B4, { group: h, title: 'Get the app (closing CTA)', desc: 'The "Get the app" pill in the closing call-to-action band; measured, never clicked.', sel: 'closing Get the app' });
  const f = G.footer;
  await S('footer', q('footer').filter({ visible: true }).first(), ['default'], { group: f, title: 'Footer', desc: 'The near-black footer: sitemap columns, social icons, legal links, "Your Privacy Choices".', sel: 'footer' }, { noScroll: true });
  await S('footer-link', q('footer a').filter({ hasText: /^Join a club$/ }).first(), B4, { group: f, title: 'Footer link', desc: 'A footer sitemap link; measured, never followed.', sel: 'footer a' }, { noScroll: true });
  await S('privacy-btn', q('footer button').filter({ hasText: /Your Privacy Choices/ }).filter({ visible: true }).first(), ['default', 'hover'], { group: f, title: 'Your Privacy Choices', desc: 'The footer\'s Osano "Your Privacy Choices" control; measured at rest — clicking it would open the consent manager, so it was never pressed.', sel: 'footer button Your Privacy Choices' }, { noScroll: true });
  save();
}

async function clubs() {
  if (!(await newPage('clubs'))) return;
  await sheetsFor('clubs');
  await chrome('clubs');
  const g = G.shell;
  await catalogShell(g);
  const c = G.clubs;
  await S('clubs-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: c, title: 'Clubs headline', desc: 'The /clubs masthead heading.', sel: 'clubs h1' }, { noScroll: true });
  await S('search-trigger', q('button[aria-haspopup="dialog"]').filter({ hasText: /Search thousands/i }).first(), [...B4, 'opened'], { group: c, title: 'Club search trigger', desc: 'The 440x52 search field-styled button opening the "Find a club" modal — an aria-haspopup="dialog" local toggle; the opened state was measured after clicking it.', sel: 'button[aria-haspopup=dialog] Search thousands' }, { noScroll: true });
  // Osano mounts its own hidden role="dialog" nodes earlier in document
  // order, so every dialog selector is scoped to the Modal-module classes.
  await S('search-modal', q(`[role="dialog"]${M('Modal-module')}`).filter({ visible: true }).first(), ['default'], { group: G.modal, title: 'Find a club modal', desc: 'The centered Modal-module sheet opened by the search trigger: drag handle, "Find a club" title, close button, search input and an empty results prompt.', sel: '[role=dialog].Modal-module__surface' }, { open: openSearchDialog, noScroll: true, noReset: true });
  await S('search-input', q(`[role="dialog"]${M('Modal-module')} input[type="search"]`).filter({ visible: true }).first(), ['default', 'focused'], { group: G.modal, title: 'Search input', desc: 'The search field inside the Find a club modal; focused, never submitted.', sel: '[role=dialog].Modal-module input[type=search]' }, { open: openSearchDialog, noScroll: true, noReset: true });
  await S('search-close', q(`[role="dialog"]${M('Modal-module')} button[aria-label*="Close" i]`).filter({ visible: true }).first(), B4, { group: G.modal, title: 'Modal close button', desc: 'The icon-only close button in the modal header.', sel: '[role=dialog].Modal-module button[aria-label^=Close]' }, { open: openSearchDialog, noScroll: true, noReset: true });
  await page.keyboard.press('Escape').catch(() => {});
  await page.waitForTimeout(600);
  await S('genre-pill', q(`a${M('ClubsIndexGenrePills-module')}`).filter({ visible: true }).first(), B4, { group: c, title: 'Genre pill', desc: 'A 46px genre pill link (Fantasy) in the scrollable genre strip; measured, never followed.', sel: 'a.ClubsIndexGenrePills-module__pill' });
  await S('genre-scroll', q('button[aria-label*="genres" i]').filter({ visible: true }).first(), B4, { group: c, title: 'Genre scroll arrow', desc: 'The dark 40px arrow that scrolls the genre strip forward; measured, never clicked.', sel: 'button[aria-label="Scroll genres forward"]' });
  await S('search-icon-btn', q('button[aria-label="Search clubs"], button[aria-label*="Search clubs" i]').filter({ visible: true }).first(), B4, { group: c, title: 'Search icon button', desc: 'The cream 44px circular search affordance at the head of the genre strip; measured, never clicked.', sel: 'button[aria-label="Search clubs"]' });
  await S('icon-btn', q(`button${M('IconButton-module')}`).filter({ visible: true }).first(), B4, { group: c, title: 'Carousel arrow', desc: 'A 40px round bordered IconButton (Previous <shelf>) stepping a club/book carousel; measured, never clicked.', sel: 'button.IconButton-module Previous' });
  await S('club-card-cat', q(`a${M('ClubCard-module')}, [data-testid="club-card"]`).filter({ visible: true }).first(), ['default', 'hover'], { group: c, title: 'Club card (catalog)', desc: 'A club card in a clubs-index shelf — image, moderator line, club name, member count; measured, never followed.', sel: 'a.ClubCard-module__card' });
  // The off-canvas MobileMenu carries hidden h2s, so the shelf heading is
  // scoped to main.
  await S('clubs-section-h', q('main h2').filter({ hasText: /starting soon|Engaging|Inspiring|Popular/i }).filter({ visible: true }).first(), ['default'], { group: c, title: 'Shelf heading', desc: 'A clubs-index shelf heading (heldane) above a horizontal card rail.', sel: 'main h2 shelf' });
  save();
}

async function book() {
  if (!(await newPage('book', { wait: 9000 }))) return;
  await sheetsFor('book');
  await chrome('book');
  const g = G.shell;
  await catalogShell(g);
  const p = G.promo;
  await S('app-banner', q(`div${M('AppDownloadBanner-module')}`).filter({ has: page.locator('a[href*="apps.apple.com"]') }).filter({ visible: true }).first(), ['default'], { group: p, title: 'App download banner', desc: 'The app-install strip under the header with App Store and Play badges; the badge links are measured, never followed.', sel: 'div.AppDownloadBanner-module' }, { noScroll: true });
  await S('store-badge', q('a[href*="apps.apple.com"]').filter({ visible: true }).first(), ['default', 'hover'], { group: p, title: 'Store badge', desc: 'The App Store badge inside the download banner; measured, never followed.', sel: 'a[href*=apps.apple.com]' }, { noScroll: true });
  const b = G.book;
  await S('book-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: b, title: 'Book title', desc: 'The book detail masthead title.', sel: 'book h1' }, { noScroll: true });
  await S('author-link', q(`a${M('BookDetailHero-module')}`).filter({ visible: true }).first(), B4, { group: b, title: 'Author link', desc: 'The author byline link in the book hero; measured, never followed.', sel: 'a.BookDetailHero-module__authorLink' }, { noScroll: true });
  await S('ratings-line', q(`a${M('BookDetailReviewLine-module')}`).filter({ visible: true }).first(), B4, { group: b, title: 'Ratings line', desc: 'The "66,098 Ratings" anchor linking to the reviews block; measured, never followed.', sel: 'a.BookDetailReviewLine-module__ratings' }, { noScroll: true });
  await S('btn-primary', q(`button${M('Button-module')}`).filter({ hasText: /Want to read/i }).first(), B4, { group: b, title: 'Primary button', desc: 'The dark 52px "Want to read" pill (Button-module primary, radius 9999); its states were measured but it was never clicked — saving to a shelf is signed-in functionality.', sel: 'button.Button-module Want to read' });
  await S('btn-secondary', q(`button${M('Button-module')}`).filter({ hasText: /Read or listen/i }).first(), B4, { group: b, title: 'Secondary button', desc: 'The outlined "Read or listen free today" pill below the primary; measured, never clicked.', sel: 'button.Button-module Read or listen' });
  // Clicking the spoiler pill unmounts it (the review text expands), so its
  // disclosure is measured as a resting state, not an opened one.
  await S('spoiler-pill', q('button').filter({ hasText: /May contain spoilers/i }).first(), B4, { group: b, title: 'Spoiler disclosure', desc: 'The olive "May contain spoilers!" pill toggling the pre-published review text — a local disclosure; pressing it reveals the text, so it was measured at rest.', sel: 'button May contain spoilers' });
  await S('read-more', q(`button${M('ExpandableText-module')}`).filter({ visible: true }).first(), [...B4, 'opened'], { group: b, title: 'Read more toggle', desc: 'The inline "Read more" disclosure expanding the book description — a local toggle; the opened state was measured after clicking it.', sel: 'button.ExpandableText-module Read more' });
  await S('author-profile-btn', q(`a${M('Button-module')}`).filter({ hasText: /View author profile/i }).first(), B4, { group: b, title: 'Author profile button', desc: 'The outlined "View author profile" pill link; measured, never followed.', sel: 'a.Button-module View author profile' });
  await S('book-card', q(`a${M('BookCarouselItem-module')}`).filter({ visible: true }).first(), ['default', 'hover'], { group: b, title: 'Book card', desc: 'A book carousel item — cover image, title, author — linking to another book page; measured, never followed.', sel: 'a.BookCarouselItem-module__item' });
  await S('club-card-book', q(`a${M('ClubCard-module')}`).filter({ visible: true }).first(), ['default', 'hover'], { group: b, title: 'Club card (book page)', desc: 'A club card in the "clubs reading this" rail; measured, never followed.', sel: 'a.ClubCard-module__card' });
  await S('icon-btn-book', q(`button${M('IconButton-module')}`).filter({ visible: true }).first(), B4, { group: b, title: 'Carousel arrow (book)', desc: 'A 40px round bordered IconButton stepping the "Other books by" carousel; measured, never clicked.', sel: 'button.IconButton-module' });
  save();
}

async function club() {
  if (!(await newPage('club', { wait: 9000 }))) return;
  await sheetsFor('club');
  await chrome('club');
  const g = G.shell;
  await catalogShell(g);
  const c = G.club;
  await S('club-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: c, title: 'Club name', desc: 'The club masthead — heldane 46px bold "The Cozy Chaos Book Club".', sel: 'club h1 Text-module v-header' }, { noScroll: true });
  await S('club-sub', q('h3').filter({ visible: true }).first(), ['default'], { group: c, title: 'Moderator line', desc: 'The 14px Inter semibold moderator byline under the club name.', sel: 'club h3 Text-module v-subheader' }, { noScroll: true });
  await S('join-cta', q(`a${M('Button-module')}`).filter({ hasText: /Download the app to join/i }).first(), B4, { group: c, title: 'Join CTA', desc: 'The dark "Download the app to join" pill — joining is app-only; measured, never followed.', sel: 'a.Button-module Download the app to join' });
  await S('share-btn', q(`button${M('ShareButton-module')}`).filter({ visible: true }).first(), B4, { group: c, title: 'Share button', desc: 'The round share icon button ("Share The Cozy Chaos Book Club"); measured, never clicked.', sel: 'button.ShareButton-module' });
  await S('club-h2', q('h2').filter({ hasText: /About this club|Club picks/i }).filter({ visible: true }).first(), ['default'], { group: c, title: 'Club section heading', desc: 'A heldane 36px club-page section heading ("About this club").', sel: 'club h2 Text-module' });
  await S('faq-q', q(`button${M('FaqAccordion-module')}`).filter({ visible: true }).first(), [...B4, 'opened'], { group: c, title: 'FAQ question', desc: 'A FAQ accordion question ("Are Fable book clubs free to join?") — a local toggle; the opened state was measured after clicking it.', sel: 'button.FaqAccordion-module__faqQuestion' });
  // The first carousel items sit left of the viewport; nth(2) is on-screen
  // for a resting read (its hover keeps landing outside the viewport, so it
  // is honestly not captured).
  await S('book-card-club', q(`a${M('BookCarouselItem-module')}`).filter({ visible: true }).nth(2), ['default'], { group: c, title: 'Club pick card', desc: 'A "Club picks" book card (CURRENTLY READING badge, cover, title); measured, never followed.', sel: 'a.BookCarouselItem-module__item' });
  save();
}

async function signin() {
  if (!(await newPage('signin', { wait: 9000 }))) return;
  await sheetsFor('signin');
  await chrome('signin');
  const g = G.signin;
  await S('signin-h1', q('h1, h2').filter({ hasText: /log in|sign up|welcome/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-in headline', desc: '"Please log in" — the Heldane Display 26px heading over the sign-in card.', sel: 'signin h1' }, { noScroll: true });
  await S('signin-panel', q('form').filter({ visible: true }).first(), ['default'], { group: g, title: 'Sign-in form', desc: 'The sign-in form: email and password fields, show-password, the email submit and SSO buttons. Shot and measured at rest — never submitted.', sel: 'signin form' }, { noScroll: true });
  await S('field-email', q('input[type="email"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Email field', desc: 'The Email Address text input; focused and typed into then cleared — never submitted.', sel: 'input[type=email]' }, { noScroll: true, fillText: 'name@example.com' });
  await S('field-password', q('input[type="password"]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Password field', desc: 'The Password input with the inline Show button; focused and typed into then cleared — never submitted.', sel: 'input[type=password]' }, { noScroll: true, fillText: 'example-password-123' });
  await S('show-btn', q('button[aria-label*="Show" i], button').filter({ hasText: /^Show$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Show password', desc: 'The inline "Show" reveal button in the password field; measured, never clicked.', sel: 'button Show password' }, { noScroll: true });
  await S('submit-btn', q('button[type="submit"]').filter({ visible: true }).first(), B4, { group: g, title: 'Login with email', desc: 'The dark "Login with email" submit; its states were measured but the button was never clicked — nothing was submitted.', sel: 'button[type=submit] Login with email' }, { noScroll: true });
  // The SSO buttons carry stable data-testids (their innerText is
  // "Continue with\nGoogle" — a hidden "Login with" in textContent breaks
  // every hasText regex). They mount late, after the identity SDKs land.
  try { await q('button[data-testid="auth-provider-google-button"]').waitFor({ timeout: 15000 }); } catch { /* may never render */ }
  await S('sso-google', q('button[data-testid="auth-provider-google-button"]'), B4, { group: g, title: 'Continue with Google', desc: 'The white Google SSO button; measured, never clicked.', sel: 'button[data-testid=auth-provider-google-button]' }, { noScroll: true });
  await S('sso-apple', q('button[data-testid="auth-provider-apple-button"]'), B4, { group: g, title: 'Continue with Apple', desc: 'The white Apple SSO button; measured, never clicked.', sel: 'button[data-testid=auth-provider-apple-button]' }, { noScroll: true });
  await S('reset-link', q('button, a').filter({ hasText: /^Reset it$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Reset link', desc: 'The "Reset it" password-reset link styled as a bold inline button; measured, never clicked.', sel: 'button Reset it' }, { noScroll: true });
  await S('signup-link', q('button, a').filter({ hasText: /^Sign up$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign up link', desc: 'The "Sign up" link button under the SSO buttons; measured, never clicked.', sel: 'button Sign up' }, { noScroll: true });
  save();
}

async function support() {
  if (!(await newPage('support', { wait: 8000 }))) return;
  await sheetsFor('support');
  await chrome('support');
  const g = G.support;
  await S('support-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Support headline', desc: 'The /support masthead heading on the forest-green band.', sel: 'support h1' }, { noScroll: true });
  await S('support-masthead', await domFind(page, /\S/, { sel: 'h1', tag: 'sm', up: 'section' }), ['default'], { group: g, title: 'Support masthead band', desc: 'The forest-green support masthead band (rgb(6, 76, 55)) carrying the heading and intro.', sel: 'support h1 closest section' }, { noScroll: true });
  await S('help-card', q('a').filter({ hasText: /^FAQs|frequently asked/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Help card', desc: 'The "FAQs" help-card linking to help.fable.co; measured, never followed.', sel: 'support FAQs card' });
  await S('email-card', q('a[href^="mailto"]').filter({ visible: true }).first(), B4, { group: g, title: 'Email card', desc: 'The "Email" help-card (mailto:support@fable.co); measured, never followed.', sel: 'support Email card' });
  save();
}

async function discover() {
  if (!(await newPage('discover', { wait: 12000 }))) return;
  // The wall is a live "Gathering ten thousand covers" animation: image
  // decodes saturate the main thread while it settles, so reads need a
  // longer timeout and a settle wait before the first measurement.
  page.setDefaultTimeout(25000);
  await page.waitForFunction(() => !/Gathering/i.test(document.body.innerText || ''), { timeout: 30000 }).catch(() => {});
  await page.waitForTimeout(8000);
  await sheetsFor('discover');
  await chrome('discover');
  // Once the wall is settled, freeze the render loop: the live animation
  // re-mounts the masthead every frame, which starves locator resolution
  // (disc-h1 timed out at 25s twice). RAF is stopped only after the full
  // wall has rendered; computed styles are unaffected.
  await page.evaluate(() => { window.requestAnimationFrame = () => 0; }).catch(() => {});
  await page.waitForTimeout(1500);
  const g = G.discover;
  // The wall paints a radial-gradient scrim over the cover grid, not a flat
  // fill: the painted layer carries the dark field.
  await S('disc-wall', q('main').filter({ visible: true }).first().locator('> div').first(), ['default'], { group: g, title: 'Cover wall', desc: 'The /discover cover wall under its dark-green radial scrim (rgba(12, 92, 66, 0.85)); a whole-page dark surface, not a .dark-scope paint.', sel: 'main.app-content > div' }, { noScroll: true });
  await S('disc-h1', await domFind(page, /Find new books/i, { sel: 'h1, h2, [class*="title" i]', tag: 'dh' }), ['default'], { group: g, title: 'Discover headline', desc: '"Find new books by browsing similar covers" — the Heldane Display 64px pearl masthead on the dark wall.', sel: 'discover h1' }, { noScroll: true });
  await S('disc-field', q('input[placeholder*="book you love" i]').filter({ visible: true }).first(), ['default', 'focused', 'filled'], { group: g, title: 'Book search field', desc: 'The white 420x60 search pill ("Search for a book you love..."); focused and typed into then cleared — never submitted.', sel: 'input[placeholder*="book you love"]' }, { noScroll: true, fillText: 'project hail mary' });
  await S('disc-random', q('button').filter({ hasText: /^\s*Random\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Random button', desc: 'The forest-400 "Random" pill shuffling the cover wall; measured, never clicked.', sel: 'button Random' }, { noScroll: true });
  await S('disc-whatis', q('button').filter({ hasText: /What is this/i }).filter({ visible: true }).first(), B4, { group: g, title: 'What is this button', desc: 'The matching "What is this?" pill; measured, never clicked.', sel: 'button What is this' }, { noScroll: true });
  await S('disc-wordmark', q('a[href="/"], a[aria-label*="able" i], header a').filter({ visible: true }).first(), ['default'], { group: g, title: 'Fable wordmark (discover)', desc: 'The fable wordmark link at the top of the dark wall; measured, never followed.', sel: 'discover wordmark' }, { noScroll: true });
  save();
}

// The phone's hamburger is div[aria-label="Open menu"]; the nav sheet it
// opens is the Clubs button's outermost on-screen ancestor inside the
// header. Tags that sheet with data-m-nav so it can be located while open.
async function openMobileNav() {
  const probe = () => page.evaluate(() => {
    const b = [...document.querySelectorAll('header button')].find((x) => x.innerText.trim() === 'Clubs');
    if (!b) return false;
    let sheet = null;
    for (let n = b; n && n.tagName !== 'HEADER'; n = n.parentElement) {
      const r = n.getBoundingClientRect();
      if (r.width > 250 && r.left > -10) sheet = n;
    }
    if (!sheet) return false;
    sheet.setAttribute('data-m-nav', '1');
    return true;
  });
  if (await probe()) return 'nav sheet already open';
  const btn = q('[aria-label="Open menu"]').first();
  try { await btn.waitFor({ timeout: 15000 }); } catch { return 'menu trigger never mounted'; }
  await btn.click().catch(() => btn.evaluate((el) => el.click()));
  await page.waitForTimeout(1200);
  return (await probe()) ? 'clicked the "Open menu" hamburger; the nav sheet slid in from x=-390' : 'clicked Open menu; the sheet did not report open';
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-header', q('header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile header', desc: 'The phone top bar: Fable mark, "Sign up or log in" and cart icons. The off-canvas nav sheet is measured below in its opened state.', sel: 'mobile header' }, { noScroll: true });
  await S('m-logo', q('header a[aria-label="Home"], header a[href="/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile logo', desc: 'The Fable mark-and-wordmark svg at 390 wide.', sel: 'mobile header logo' }, { noScroll: true });
  await S('m-hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero headline', desc: 'The masthead at 390 wide.', sel: 'mobile h1' });
  await S('m-getapp', q('button').filter({ hasText: /^Get the app$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile Get the app', desc: 'The hero "Get the app" pill at 390 wide; measured, never clicked.', sel: 'mobile Get the app' });
  await S('m-club-card', q('[data-testid="club-card"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile club card', desc: 'A Popular-clubs card at 390 wide.', sel: 'mobile club-card' });
  await S('m-footer', q('footer').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile footer', desc: 'The near-black footer stacked at 390 wide.', sel: 'mobile footer' }, { noScroll: true });
  // The off-canvas nav sheet, honestly opened through its div hamburger.
  await S('m-menu-btn', q('[aria-label="Open menu"]').filter({ visible: true }).first(), B4, { group: g, title: 'Mobile menu button', desc: 'The hamburger div opening the off-canvas nav sheet; its rest states were measured and the sheet was opened once for the rows below.', sel: '[aria-label="Open menu"]' }, { noScroll: true });
  await S('m-nav', q('[data-m-nav]'), ['default'], { group: g, title: 'Mobile nav sheet', desc: 'The full-screen cream nav sheet slid in from x=-390: pill links (Clubs / Books / Library / Blog / Log in), footer links and the copyright line. Opened by clicking the hamburger — a local UI toggle.', sel: 'header off-canvas nav sheet' }, { open: openMobileNav, noScroll: true, noReset: true });
  await S('m-nav-link', q('header button').filter({ hasText: /^Clubs$/ }).first(), B4, { group: g, title: 'Nav sheet link', desc: 'A pill link inside the opened nav sheet; measured while the sheet was open, never followed.', sel: 'nav sheet button Clubs' }, { open: openMobileNav, noScroll: true, noReset: true });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); marketing pages (/ /signin /support) paint emotion-styled light surfaces on a forest-green hero, catalog pages (/clubs /books /book/* /club/*) paint the CSS-module white skin; /discover paints dark';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, clubs, book, club, signin, support, discover, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (the primary button's
  // hover), so the delta is meaningful.
  if (!pages.length || pages.includes('book')) await reducedMotion('book', `button${M('Button-module')}`);
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
