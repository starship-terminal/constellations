// Measures fresha.com's components on its signed-out public pages, in every
// state that can be reached without signing in, booking or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home userflow auth partner venue booking pricing business lp help mobile.
// Writes raw/components-computed.json (merged, so a subset of pages can be re-run)
// and one crop per component and state into components/crops/. raw/measurements.md
// is then built from the JSON by build-measurements.mjs.
//
// States:
//   hover          real mouse hover, 450ms settle for transitions
//   focus-visible  keyboard: focus, Shift+Tab, Tab, so the browser sees a keyboard focus
//   pressed        CDP CSS.forcePseudoState [active, hover]; no mouse button is pressed,
//                  so no link, Book button or submit control can fire
//   focused        the field clicked into (a text field only)
//   filled         sample text typed into a field, measured, then deleted; Enter is never pressed
//   anything else  a resting state reached by the page itself or by a local UI toggle
//                  (a menu, a tab, an accordion, a filter checkbox, the booking wizard's
//                  own service checkboxes); nothing that books, pays, signs in, submits
//                  a form or starts an OAuth flow is ever pressed
import fs from 'node:fs';
import path from 'node:path';
import { BASE, AUTH, USERFLOW, PARTNER_SIGNIN, VENUE, VENUE_BOOKING, LP_BROWSE, M, launch, open, closePromo, domFind, styleOf, crop, centre, patch, UA_MOBILE, RAW } from './lib.mjs';
import { safeUrl } from '../safe-url.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

const URLS = {
  home: BASE + '/',
  userflow: USERFLOW,
  auth: AUTH,
  partner: PARTNER_SIGNIN,
  venue: VENUE,
  booking: VENUE_BOOKING,
  pricing: BASE + '/pricing',
  business: BASE + '/for-business',
  lp: LP_BROWSE,
  help: BASE + '/help-center',
};

let page, cdp, current, context, run, mobileContext, desktopContext;
const touched = new Set();
const listed = new Map(); // component -> the states this run's specs list for it

// ---------- helpers ----------

async function newPage(key, { mobile = false, promo = 'close', wait = 7000, url = null } = {}) {
  current = key;
  // A mobile pass needs its own context (390 x 844, touch UA, dpr 2) — the
  // shared `context` is the desktop one.
  if (mobile) {
    if (!mobileContext) {
      mobileContext = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' });
      await patch(mobileContext);
    }
    context = mobileContext;
  } else if (desktopContext) {
    context = desktopContext;
  }
  page = await context.newPage();
  page.setDefaultTimeout(9000);
  cdp = await context.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  log('open', key, mobile ? '(mobile)' : '');
  if (!(await open(page, url || URLS[key], { wait, promo }))) throw new Error(`BLOCKED ${key}: the page never loaded, nothing measured`);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
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
    await loc.evaluate((el) => el.focus());
    ok = await loc.evaluate((el) => document.activeElement === el);
    how = 'element.focus()';
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

// Clicks a local UI toggle (tab, menu, accordion, map overlay). Refuses a submit
// button, any anchor unless allowLink, and any control whose text names an
// action this capture must never take.
const NEVER = /send|submit|sign ?in|log ?in|sign ?up|create|book now|book\b|confirm|pay|checkout|purchase|continue|proceed|get started|try for free|start free|upgrade|subscribe|buy|order|add to|apply|join|verify|next|reschedule|cancel appointment/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim().slice(0, 60) }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

function comp(key, meta) {
  const c = (out.components[key] ??= { states: {} });
  Object.assign(c, { page: current, run, url: safeUrl(URLS[current] || '') }, meta);
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

const FILL = 'haircut';

// Records the listed states of one component. meta: title, group, desc, sel.
async function S(key, target, list, meta = {}, opts = {}) {
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  if (!listed.has(key)) listed.set(key, new Set());
  for (const st of list) listed.get(key).add(st);
  delete out.components[key].missing;
  if (opts.open) { await reset(); await opts.open(); }
  const loc = target.filter({ visible: true }).first();
  if (!(await loc.count())) { log('  ! missing', key); out.components[key].missing = true; return; }
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
        const f = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await f.click({ timeout: 4000 }).catch(() => f.evaluate((el) => el.click()));
        await page.waitForTimeout(400);
        via = 'clicked into the field';
      } else if (st === 'filled') {
        const f = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await f.click({ timeout: 4000 }).catch(() => f.evaluate((el) => el.click()));
        await page.keyboard.type(opts.fillText || FILL, { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus().catch(() => {}); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || FILL}", then deleted; nothing sent`;
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

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const F3 = ['default', 'focused', 'filled'];

// Fresha bars are divs, not <header>: walks up from a known header control
// ("Log in", "Menu") until the element spans ~the viewport width, and marks it.
async function chromeOf(anchorRe = /Log in|Menu|fresha/i) {
  const ok = await page.evaluate((src) => {
    const re = new RegExp(src, 'i');
    const a = [...document.querySelectorAll('a,button')].find((n) => {
      const r = n.getBoundingClientRect();
      return re.test((n.innerText || n.getAttribute('aria-label') || '').trim()) && r.top < 100 && r.width > 10;
    });
    if (!a) return false;
    let n = a, best = a;
    for (let i = 0; i < 7 && n; i++) {
      const r = n.getBoundingClientRect();
      best = n;
      if (r.width >= window.innerWidth * 0.85) break;
      n = n.parentElement;
    }
    best.setAttribute('data-m-mark', 'topchrome');
    return true;
  }, anchorRe.source).catch(() => false);
  return ok ? q('[data-m-mark="topchrome"]') : q('header');
}

// Transitions and animations declared in every readable sheet, by selector.
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
    for (const ss of document.styleSheets) { try { walk(ss.cssRules); } catch { /* cross-origin, read by vars.mjs */ } }
    return transitions;
  });
  out._meta.sheets ??= {};
  out._meta.sheets[key] = res;
}

// ---------- groups ----------
const G = {
  shell: 'Shell and navigation', home: 'Consumer home', search: 'Search', venue: 'Venue page',
  card: 'Cards', auth: 'Sign-in shell', booking: 'Booking wizard', pricing: 'Pricing',
  business: 'For-business marketing', lp: 'Marketplace browse (/lp)', help: 'Help centre',
  overlay: 'Dialogs, menus and overlays', form: 'Form controls', mobile: 'Mobile (390 wide)',
};

// ---------- consumer home ----------
async function home() {
  await newPage('home');
  await sheetsFor('home');
  await S('shell-header', await chromeOf(/Log in/), ['default'], { group: G.shell, title: 'Top bar', desc: 'The consumer app bar: logo left, Log in / For businesses / Menu / Get the app right, over the hero.', sel: 'header chrome' }, { noScroll: true });
  await S('shell-login-link', await domFind(page, /^Log in$/, { sel: 'a,button', tag: 'login' }), B4, { group: G.shell, title: 'Log in link', desc: 'Header link to the /user-flow chooser. Measured, never followed.', sel: 'a:has-text("Log in")' }, { noScroll: true });
  await S('shell-business-link', await domFind(page, /^For businesses$/, { sel: 'a,button', tag: 'biz' }), B4, { group: G.shell, title: 'For businesses link', desc: 'Header link to the B2B marketing app. Measured, never followed.', sel: 'a:has-text("For businesses")' }, { noScroll: true });
  const menuBtn = await domFind(page, /^Menu$/, { sel: 'button, [role=button]', tag: 'menu' });
  await S('shell-menu-button', menuBtn, B4, { group: G.shell, title: 'Menu button', desc: 'Header button that opens the consumer drawer (aria-haspopup).', sel: 'button:has-text("Menu")' }, { noScroll: true });
  const getApp = await domFind(page, /^Get the app$/, { sel: 'button, a', tag: 'getapp' });
  await S('shell-getapp-button', getApp, B4, { group: G.shell, title: 'Get the app button', desc: 'Header button. Opens the app-download dialog on click — captured open where the dialog mounts.', sel: 'button:has-text("Get the app")' }, { noScroll: true });

  // Menu overlay: the button opens it; items are measured inside.
  if (await menuBtn.count()) {
    await reset();
    await menuBtn.first().click({ timeout: 5000 }).catch(() => {});
    await page.waitForTimeout(1200);
    const drawerEl = await page.evaluate(() => {
      const cand = [...document.querySelectorAll('[role="dialog"],[role="menu"],[role="listbox"],div,nav,aside,ul')].filter((n) => {
        const r = n.getBoundingClientRect(); const cs = getComputedStyle(n);
        return r.width > 100 && r.width < 620 && r.height > 120 && r.height < 640
          && /Log in or sign up/i.test(n.innerText || '') && (n.innerText || '').length < 900
          && (cs.position === 'fixed' || cs.position === 'absolute' || r.top < 240);
      });
      cand.sort((a, b) => a.querySelectorAll('*').length - b.querySelectorAll('*').length);
      const el = cand[0];
      if (el) el.setAttribute('data-m-mark', 'drawer');
      return !!el;
    }).catch(() => false);
    if (drawerEl) {
      const d = q('[data-m-mark="drawer"]');
      await S('menu-drawer', d, ['default'], { group: G.overlay, title: 'Menu drawer', desc: 'The consumer menu popover opened by the Menu button: "Log in or sign up", "Download the app", "Help and support", "English (US)", "For businesses". Opened by its own button, closed after measuring.', sel: '[data-m-mark="drawer"]' }, { noScroll: true });
      const signup = await domFind(page, /Log in or sign up/i, { sel: 'a,button,li,[role="menuitem"],[role="link"],span,div', tag: 'drawer-signup' });
      await S('menu-item', signup, ['default', 'hover'], { group: G.overlay, title: 'Menu drawer item', desc: 'A row in the menu popover. Measured, never followed.', sel: 'menu item' }, { noScroll: true });
      await page.keyboard.press('Escape').catch(() => {});
      await page.waitForTimeout(800);
      // Fall back to clicking the button again when Escape is not wired.
      if (await page.evaluate(() => { const n = document.querySelector('[data-m-mark="drawer"]'); return n && n.getBoundingClientRect().width > 10 && getComputedStyle(n).visibility !== 'hidden'; }).catch(() => false)) {
        await menuBtn.first().click({ timeout: 4000 }).catch(() => {});
        await page.waitForTimeout(800);
      }
    }
  }

  // Get-the-app dialog (a QR-code modal), if the button opens one.
  if (await getApp.count()) {
    await reset();
    await getApp.first().click({ timeout: 5000 }).catch(() => {});
    await page.waitForTimeout(1200);
    const hasDialog = await page.evaluate(() => {
      const d = [...document.querySelectorAll('[role="dialog"]')].find((n) => {
        const r = n.getBoundingClientRect(); return r.width > 200 && /app|scan|download/i.test(n.innerText || '');
      });
      if (d) d.setAttribute('data-m-mark', 'appdlg');
      return !!d;
    }).catch(() => false);
    if (hasDialog) {
      await S('app-dialog', q('[data-m-mark="appdlg"]'), ['default'], { group: G.overlay, title: 'Get the app dialog', desc: 'The download dialog opened by "Get the app" — a QR code for the mobile app plus copy. Opened by its own button, closed after measuring.', sel: '[role="dialog"]' }, { noScroll: true });
      await page.keyboard.press('Escape').catch(() => {});
      await page.waitForTimeout(700);
    }
  }

  // Hero + search trio.
  const hero = await domFind(page, /Book local selfcare services|Book selfcare/i, { sel: 'h1,h2,[class*="hero" i]', tag: 'hero', leaf: true });
  await S('home-hero-title', hero, ['default'], { group: G.home, title: 'Hero title', desc: '"Book local selfcare services" — the Roobert display size over the home hero.', sel: 'h1' });
  const treat = await domFind(page, /All treatments/i, { sel: 'input,button,[role="combobox"]', tag: 'treat' });
  const treatField = q('input[placeholder*="treatment" i], input[aria-label*="treatment" i], [role="combobox"]').first();
  const tf = (await treatField.count()) ? treatField : treat;
  await S('search-treatment-field', tf, ['default', 'focused'], { group: G.search, title: 'Treatment field', desc: 'The "All treatments" combobox of the hero search bar. Focused opens a suggestion list; nothing is submitted.', sel: 'input/[role=combobox] treatments' });
  const locField = q('input[placeholder*="location" i], input[placeholder*="Current location" i]').first();
  await S('search-location-field', (await locField.count()) ? locField : await domFind(page, /Current location/i, { sel: 'input,button', tag: 'loc' }), ['default', 'focused'], { group: G.search, title: 'Location field', desc: 'The "Current location" input of the hero search bar. Focused only — no query is sent.', sel: 'input location' });
  // The "Any time" control sits in the same hero search bar as the treatment
  // and location fields — mark that bar (the smallest ancestor holding both
  // fields) and find the control inside it, so a "any time" phrase in a
  // review or a promotion cannot be mistaken for it.
  await page.evaluate(() => {
    document.querySelectorAll('[data-m-mark="searchbar"]').forEach((x) => x.removeAttribute('data-m-mark'));
    const f = document.querySelector('input[placeholder*="treatment" i], input[aria-label*="treatment" i], [role="combobox"]');
    if (!f) return;
    let n = f;
    for (let i = 0; i < 8 && n; i++) {
      if (n.querySelector && n.querySelector('input[placeholder*="location" i], input[placeholder*="Current location" i]')) break;
      n = n.parentElement;
    }
    if (n && n !== f) n.setAttribute('data-m-mark', 'searchbar');
  }).catch(() => {});
  let when = await domFind(page, /Any time/i, { sel: 'button,input,[role="combobox"],[role="button"]', tag: 'when', root: '[data-m-mark="searchbar"]' });
  if (!(await when.count())) when = await domFind(page, /^\s*Any time\s*$/i, { sel: 'button,input,[role="combobox"],[role="button"],div,li,span', tag: 'when', leaf: true, root: '[data-m-mark="searchbar"]' });
  if (!(await when.count())) when = await domFind(page, /^\s*Any time\s*$/i, { sel: 'button,input,[role="combobox"],[role="button"],div,li,span', tag: 'when', leaf: true });
  await S('search-when-control', when, ['default', 'focused'], { group: G.search, title: 'When control', desc: 'The "Any time" control of the hero search bar: opens the date/time popover. Focused state only in the field view; the open popover is measured where it mounts.', sel: '"Any time" control' });
  const searchBtn = await domFind(page, /^Search$/, { sel: 'button,[role="button"]', tag: 'searchbtn' });
  await S('search-button', (await searchBtn.count()) ? searchBtn : q('button[type="submit"]').first(), B4, { group: G.search, title: 'Search button', desc: 'The hero search submit. Measured, never pressed — a press runs a search query.', sel: 'button "Search"' });
  // The suggestion listbox after a field focus (a local dropdown, no submit).
  if (await tf.count()) {
    await reset();
    await tf.first().click({ timeout: 4000 }).catch(() => {});
    await page.waitForTimeout(1200);
    const lb = q('[role="listbox"], ul[class*="suggest" i], [class*="dropdown" i] li').first();
    if (await lb.count()) {
      await S('search-suggestions', q('[role="listbox"]').first(), ['default'], { group: G.overlay, title: 'Search suggestions', desc: 'The dropdown the treatment field opens on focus: suggestion rows for services and venues. Opened by focusing the field; Escape closes it; nothing is chosen.', sel: '[role="listbox"]' }, { noScroll: true });
    }
    await page.keyboard.press('Escape').catch(() => {});
    await page.waitForTimeout(600);
  }

  // Recommended venues: a carousel of venue cards.
  const card = await domFind(page, /Best in Class|Highly Recommended|Featured|^New$/, { sel: 'a,article,li,div', tag: 'vcard', up: 'a,article,li', minW: 200, minH: 100 });
  const cardLoc = (await card.count()) ? card : q('a[href*="/a/"]').first();
  await S('venue-card', cardLoc, ['default', 'hover'], { group: G.card, title: 'Venue card', desc: 'A recommended-venue card in the home carousel: photo, name, rating badge and score, address line and a tag ("Best in Class", "Featured"). The whole card is one link; measured, never followed.', sel: 'a[href*="/a/"]' });
  const rating = await domFind(page, /^\d\.\d\s*\(?\d|\d\.\d$/, { sel: 'span,div,p', tag: 'rating', minW: 16, minH: 10 });
  await S('rating-badge', rating, ['default'], { group: G.card, title: 'Rating badge', desc: 'The score chip on a venue card ("4.9" with a star): badge fill plus the count beside it. The screen-reader "4.9 rating" copy is excluded.', sel: 'rating chip' });
  // The arrows are plain buttons whose text IS "Previous"/"Next" (no
  // aria-label); the favourite hearts (aria-label "Sign in to add to
  // favorites") must never match.
  let prevBtn = await domFind(page, /^(Previous|Next)$/i, { sel: 'button,[role="button"]', tag: 'prev', leaf: true });
  if (!(await prevBtn.count())) prevBtn = await domFind(page, /prev|next|arrow|scroll/i, { sel: 'button[aria-label], [role="button"][aria-label]', tag: 'prev' });
  const carouselPrev = (await prevBtn.count()) ? prevBtn : q('button[aria-label*="prev" i], button[aria-label*="next" i]').first();
  await S('carousel-button', carouselPrev, B4, { group: G.home, title: 'Carousel arrow', desc: 'The circular Prev/Next buttons on the recommended carousel.', sel: 'button[aria-label] arrow' });
  await S('footer', q('footer').first(), ['default'], { group: G.shell, title: 'Footer', desc: 'The site footer: link columns, app badges, region and legal links.', sel: 'footer' });
  await page.close();
}

// ---------- /user-flow chooser ----------
async function userflow() {
  await newPage('userflow');
  const back = await domFind(page, /Go back|Back/, { sel: 'button,a', tag: 'back' });
  await S('back-button', back, B4, { group: G.auth, title: 'Back button', desc: 'The round "Go back" control every auth-shell page carries.', sel: 'button "Go back"' }, { noScroll: true });
  const custCard = await domFind(page, /Fresha for customers/i, { sel: 'a,button,[role="link"],div', tag: 'cust', up: 'a,button,[role="link"]', minW: 200 });
  await S('chooser-card', custCard, ['default', 'hover', 'focus-visible'], { group: G.auth, title: 'Customer/professional card', desc: 'One of the two chooser cards on /user-flow ("Fresha for customers", "Fresha for professionals"): title, description and chevron. A link to the auth shell; measured, never followed.', sel: 'a:has-text("Fresha for customers")' }, { noScroll: true });
  const lang = await domFind(page, /English/i, { sel: 'button,a', tag: 'lang' });
  await S('language-button', lang, B4, { group: G.auth, title: 'Language button', desc: 'The "English (US)" locale picker on the chooser. Measured; not opened (opening it may navigate).', sel: 'button:has-text("English")' }, { noScroll: true });
  await page.close();
}

// ---------- /auth sign-in shell ----------
async function auth() {
  await newPage('auth');
  await sheetsFor('auth');
  const back = await domFind(page, /Go back|Back/, { sel: 'button,a', tag: 'back' });
  if (await back.count()) await S('auth-back', back, B4, { group: G.auth, title: 'Auth back button', sel: 'button back' }, { noScroll: true });
  const email = q('input[type="email"], input[name*="email" i], input[autocomplete*="email" i], form input:visible').last();
  await S('auth-email-field', email, F3, { group: G.form, title: 'Email field', desc: 'The auth shell\'s single text input: "We\'ll send you a verification code". Typed into then cleared; Continue is never pressed — no code is ever requested.', sel: 'input email' }, { noScroll: true, fillText: 'hello@example.com' });
  const cont = await domFind(page, /^Continue$/, { sel: 'button', tag: 'cont' });
  await S('auth-continue', cont, B4, { group: G.auth, title: 'Continue button', desc: 'The email submit — a press requests a verification code, so it is only measured.', sel: 'button "Continue"' }, { noScroll: true });
  const google = await domFind(page, /Continue with Google/, { sel: 'button,a', tag: 'sso1' });
  await S('sso-button', google, B4, { group: G.auth, title: 'SSO button', desc: '"Continue with Google" (the Apple and passkey rows share the style): a full-width outlined button with the provider mark. Never pressed — a press starts an OAuth flow.', sel: 'button:has-text("Continue with Google")' }, { noScroll: true });
  const passkey = await domFind(page, /Continue with passkey/, { sel: 'button,a', tag: 'sso3' });
  await S('passkey-button', passkey, ['default', 'hover'], { group: G.auth, title: 'Passkey button', sel: 'button:has-text("passkey")' }, { noScroll: true });
  const bizLink = await domFind(page, /Go to Fresha for professionals/i, { sel: 'a,button', tag: 'bizlink' });
  await S('auth-cross-link', bizLink, ['default', 'hover'], { group: G.auth, title: 'Cross-over link', desc: '"Have a business account? Go to Fresha for professionals" — the link out to the partner sign-in. Measured, never followed.', sel: 'a:has-text("professionals")' }, { noScroll: true });
  await page.close();
}

// ---------- partners.fresha.com sign-in ----------
async function partner() {
  await newPage('partner', { wait: 9000 });
  await sheetsFor('partner');
  const email = q('input[type="email"], input[name*="email" i]').first();
  await S('partner-email-field', email, F3, { group: G.form, title: 'Partner email field', desc: 'The professional sign-in\'s email input. Typed into then cleared; nothing is submitted.', sel: 'input[type="email"]' }, { noScroll: true });
  // A hidden input[type=password] sits off-viewport (x≈-1278): an
  // autocomplete/decoy field, recorded for honesty — the sign-in itself is a
  // verification-code flow with no visible password field.
  const pw = q('input[type="password"]').first();
  await S('partner-decoy-password', pw, ['default'], { group: G.form, title: 'Hidden password input', desc: 'An off-viewport input[type=password] (x≈-1278) in the partner sign-in form — a browser-autocomplete decoy, not a painted control. The real flow is email + verification code.', sel: 'input[type="password"]' }, { noScroll: true, crop: false });
  const cont = await domFind(page, /^Continue$|^Log in$|^Sign in$/i, { sel: 'button', tag: 'pcont' });
  await S('partner-continue', cont, B4, { group: G.auth, title: 'Partner continue button', desc: 'The professional sign-in submit. Measured, never pressed.', sel: 'button submit' }, { noScroll: true });
  const sso = await domFind(page, /Continue with Google|Google/, { sel: 'button,a', tag: 'psso' });
  await S('partner-sso', sso, B4, { group: G.auth, title: 'Partner SSO button', sel: 'button Google' }, { noScroll: true });
  const custLink = await domFind(page, /customer|book(ing)?s?\b|fresha for customers/i, { sel: 'a', tag: 'plink' });
  await S('partner-cross-link', custLink, ['default', 'hover'], { group: G.auth, title: 'Partner cross link', desc: 'The link sending customers back to the consumer sign-in. Measured, never followed.', sel: 'a customer' }, { noScroll: true });
  await page.close();
}

// ---------- venue page ----------
async function venue() {
  await newPage('venue', { wait: 8000 });
  await sheetsFor('venue');
  const crumb = await domFind(page, /Hair salons|Beauty/i, { sel: 'nav a, ol a, [aria-label*="breadcrumb" i] a', tag: 'crumb' });
  const crumbs = q('[aria-label*="breadcrumb" i], nav ol').first();
  await S('breadcrumb', (await crumbs.count()) ? crumbs : crumb, ['default'], { group: G.venue, title: 'Breadcrumb', desc: 'The category/location breadcrumb over the venue title.', sel: 'nav[aria-label*=breadcrumb]' }, { noScroll: true });
  const tabs = q('[role="tablist"], nav:has(a[href^="#"])').first();
  const tab = await domFind(page, /^Services$|^About$|^Reviews$|^Team$|^Photos$/i, { sel: 'a,button,[role="tab"]', tag: 'vtab' });
  await S('venue-tab', tab, ['default', 'hover', 'focus-visible'], { group: G.venue, title: 'Venue section tab', desc: 'The sticky section nav (Services / Team / Reviews / About / Photos) — anchor links that scroll the page. Measured, never followed.', sel: 'nav a' });
  const bookNow = await domFind(page, /^Book now$/i, { sel: 'button,a', tag: 'booknow' });
  await S('book-now', bookNow, B4, { group: G.venue, title: 'Book now button', desc: 'The venue page\'s primary CTA — the primary button style. Never pressed: a press starts the booking wizard.', sel: 'button "Book now"' });
  const seeImgs = await domFind(page, /See all images|See all|photos/i, { sel: 'button,a', tag: 'gallery' });
  await S('gallery-button', seeImgs, B4, { group: G.venue, title: 'Gallery button', desc: '"See all images" over the photo grid. Measured only — opening it navigates to the gallery.', sel: 'button "See all images"' });
  const vtitle = await domFind(page, /HA-LU|Hair Design/i, { sel: 'h1,h2', tag: 'vtitle' });
  await S('venue-title', q('h1').first(), ['default'], { group: G.venue, title: 'Venue title', desc: 'The venue name heading.', sel: 'h1' });
  const svcRow = await domFind(page, /\d+\s*(min|h)|mins/i, { sel: 'li,div[class*="row" i],div', tag: 'svc', up: 'li,[class*="row" i]', minW: 280, minH: 40 });
  const svc = (await svcRow.count()) ? svcRow : q('h3 ~ div, section li').first();
  await S('service-row', svc, ['default', 'hover'], { group: G.venue, title: 'Service row', desc: 'A bookable service line: name, duration, price and a Select/Book control. Measured, never booked.', sel: 'li service row' });
  const svcBook = await domFind(page, /^Select$|^Book$/i, { sel: 'button,a', tag: 'svcbook' });
  await S('service-book-button', svcBook, B4, { group: G.venue, title: 'Service select button', desc: 'The per-service select control. Never pressed.', sel: 'button "Select"' });
  const hoursH = await domFind(page, /Opening times|Opening hours/i, { sel: 'h2,h3,h4,div,section', tag: 'hours-h', leaf: true });
  const hoursWrap = (await hoursH.count()) ? hoursH.locator('xpath=..').first() : q('table').first();
  await S('hours-table', hoursWrap, ['default'], { group: G.venue, title: 'Opening times', desc: 'The "Opening times" week schedule in the About section — green dot per open day, grey for closed.', sel: 'opening-times block' });
  const staff = await domFind(page, /Top stylist|stylist/i, { sel: 'div,a,li', tag: 'staff', leaf: true, minW: 60 });
  const staffWrap = (await staff.count()) ? staff.locator('xpath=..').first() : staff;
  await S('staff-avatar', staffWrap, ['default', 'hover'], { group: G.venue, title: 'Staff avatar', desc: 'A Team circle: photo, name, "Top stylist" label and rating badge.', sel: 'staff card' });
  const score = await domFind(page, /^5\.0$|Best in Class/i, { sel: 'div,span,p', tag: 'score', leaf: true, minW: 40 });
  await S('review-score', score, ['default'], { group: G.venue, title: 'Review score', desc: 'The big "5.0 Best in Class" review block: display-size score with trophy badges.', sel: 'review score' });
  const review = await domFind(page, /ago|staff|verified/i, { sel: 'article,li,div', tag: 'rev', up: 'article,li', minW: 280, minH: 60 });
  await S('review-card', review, ['default'], { group: G.venue, title: 'Review card', desc: 'A venue review: star row, comment text, service and staff line, date.', sel: 'article review' });
  await page.close();
}

// ---------- booking wizard (step 1 only, plus a ticked checkbox) ----------
async function booking() {
  await newPage('booking', { wait: 9000 });
  await sheetsFor('booking');
  await page.evaluate(() => {
    const steps = [...document.querySelectorAll('ol li, nav li, [class*="step" i], a, span, div')].filter((n) => /^(Services|Professional|Time|Confirm)$/.test((n.innerText || '').trim()));
    steps.forEach((n) => n.setAttribute('data-m-step', '1'));
    return steps.length;
  });
  await S('booking-header', await chromeOf(/Confirm|Services|Back/i), ['default'], { group: G.booking, title: 'Booking header', desc: 'The wizard chrome: back arrow, the "Services › Professional › Time › Confirm" step trail and a close control.', sel: 'wizard chrome' }, { noScroll: true });
  const step = q('[data-m-step]').first();
  await S('booking-step', step, ['default'], { group: G.booking, title: 'Wizard step', desc: 'A step label in the "Services / Professional / Time / Confirm" trail — the current step emphasised.', sel: 'step label' }, { noScroll: true });
  const row = await domFind(page, /\d+\s*min|\d+h/i, { sel: 'li,div', tag: 'brow', up: 'li', minW: 280, minH: 40 });
  const brow = (await row.count()) ? row : q('ul li').nth(2);
  await S('booking-service-row', brow, ['default', 'hover'], { group: G.booking, title: 'Booking service row', desc: 'A selectable service card: name, duration, notes and price, with a round "+" add control. Adding only marks the service in the local cart; nothing is booked.', sel: 'li booking service' });
  // The "+" add control on a service card: hover, keyboard focus and a
  // CDP-forced :active only, never a real press.
  let add = await domFind(page, /^\s*\+\s*$|^Add$/i, { sel: 'button, [role="button"]', tag: 'badd', leaf: true });
  if (!(await add.count())) add = (await brow.count()) ? brow.locator('button, [role="button"]').last() : add;
  await S('booking-add-button', add, B4, { group: G.booking, title: 'Add-service button', desc: 'The round "+" that selects a service for the cart. Measured, never pressed: its pressed state is CDP-forced.', sel: 'button "+"' });
  const catPill = await domFind(page, /^Featured$|^Promotion$|^Set menu$/i, { sel: 'button,a,[role="tab"]', tag: 'cat' });
  await S('booking-category-pill', catPill, ['default', 'hover'], { group: G.booking, title: 'Category pill', desc: 'The service-category chips under "Select services" (Featured, Promotion, Set menu, CUT & TRIM …) — the active one is solid.', sel: 'category pill' });
  const cart = await domFind(page, /No services selected|Total/i, { sel: 'aside,section,div', tag: 'cart', leaf: true, minW: 240, minH: 200 });
  await S('booking-cart', cart, ['default'], { group: G.booking, title: 'Cart summary', desc: 'The right-hand booking summary: venue card (photo, rating, address), the selected-services list, Total and the step button.', sel: 'aside cart' });
  // No service is added: the "+" puts a service in a real venue's booking
  // cart, a state change on a third-party site, so the cart is measured at
  // rest only. The committed 'service-added' reading predates this edit
  // (2026-11 audit; not run since).
  const cont = await domFind(page, /^Continue$/, { sel: 'button', tag: 'bcont' });
  await S('booking-continue', cont, B4, { group: G.booking, title: 'Continue button', desc: 'The wizard\'s step button — grey while the cart is empty, dark once a service is selected. Measured, never pressed: a press advances to "Professional". The wizard never goes past step 1 in this capture.', sel: 'button "Continue"' });
  await page.close();
}

// ---------- /pricing (b2b marketing app) ----------
async function pricing() {
  await newPage('pricing', { wait: 8000 });
  await sheetsFor('pricing');
  await S('b2b-header', q('header, nav').first(), ['default'], { group: G.business, title: 'B2B top bar', desc: 'The marketing app bar shared by /for-business, /pricing, /blog and /careers: product logo, Business types / Features flyouts, Marketplace, Pricing, Help, Blog, "Try for free".', sel: 'header' }, { noScroll: true });
  const planCard = await domFind(page, /Independent|^Team$|Enterprise/i, { sel: 'article,li,div[class*="card" i],div', tag: 'plan', up: 'article,li', minW: 200, minH: 200 });
  await S('plan-card', planCard, ['default', 'hover'], { group: G.pricing, title: 'Plan card', desc: 'A pricing plan column (Independent / Team / Enterprise): plan name, monthly price, "7 day trial" badge, feature list and its CTA.', sel: 'article plan' });
  // The price, the feature rows and the info badges all live inside the
  // marked plan card — scoping keeps a "20 free messages" feature line or the
  // header's Menu button from being saved as them.
  const price = await domFind(page, /SGD|\$\s*\d|USD|EUR|GBP|€\s*\d|£\s*\d|per month|per year/i, { sel: 'span,p,div,h2,h3', tag: 'price', leaf: true, minW: 20, root: '[data-m-mark="plan"]' });
  await S('plan-price', price, ['default'], { group: G.pricing, title: 'Plan price', desc: 'The price display inside a plan card (amount + period + commission line).', sel: 'price' });
  const cta = await domFind(page, /Try for free|Get started|Contact sales|Get a demo/i, { sel: 'button,a', tag: 'cta' });
  await S('plan-cta', cta, B4, { group: G.pricing, title: 'Plan CTA', desc: 'The plan card\'s call to action. Measured, never pressed: a press starts sign-up.', sel: 'button CTA' });
  const feat = await domFind(page, /calendar|messages|client|booking|payment|notification|website|report|card processing|Marketplace/i, { sel: 'li,tr,p,div', tag: 'feat', leaf: true, minW: 100, root: '[data-m-mark="plan"]' });
  await S('feature-row', feat, ['default'], { group: G.pricing, title: 'Feature row', desc: 'A line in a plan\'s feature list (label plus checkmark or info icon).', sel: 'li feature' });
  // The "i" badges live in the comparison rows below the plan cards, as 16x16
  // buttons whose only text is the aria-label ("Description of the price of …",
  // "Definition of a team member") — domFind reads aria-labels now.
  const info = q('button[aria-label*="Description" i], button[aria-label*="Definition" i], button[aria-label*="info" i], [role="button"][aria-label*="Description" i]').first();
  const infoBtn = await domFind(page, /Description of|Definition of|more info|^\s*(i|info|ⓘ)\s*$/i, { sel: 'button,[role="button"],span,a', tag: 'info', leaf: true });
  const ib = (await infoBtn.count()) ? infoBtn : info;
  if (await ib.count()) {
    await S('info-icon', ib, ['default', 'hover', 'focus-visible'], { group: G.pricing, title: 'Info icon', desc: 'The "i" badge beside a feature — hovering opens a tooltip.', sel: 'button info' });
    await reset();
    await ib.first().hover({ timeout: 4000 }).catch(() => {});
    await page.waitForTimeout(700);
    const tip = q('[role="tooltip"]').first();
    if (await tip.count()) await S('tooltip', tip, ['default'], { group: G.overlay, title: 'Tooltip', desc: 'The tooltip an info icon opens on hover: dark fill, small body copy. Opened by hovering its trigger, dismissed by moving off.', sel: '[role=tooltip]' }, { noScroll: true });
    await page.mouse.move(8, 8).catch(() => {});
  }
  // FAQ accordion.
  const faq = await domFind(page, /How do|What is|Can I|payments\?/i, { sel: 'button,[role="button"],summary', tag: 'faq', leaf: true, minW: 200 });
  await S('faq-item', faq, ['default', 'hover'], { group: G.pricing, title: 'FAQ item', desc: 'A pricing FAQ disclosure: question row with a chevron. The open state is captured by its own toggle.', sel: 'button faq' });
  if (await faq.count()) {
    await reset();
    await centre(faq.first());
    await toggle(faq).catch((e) => log('  ! faq', String(e).slice(0, 80)));
    await page.waitForTimeout(700);
    await measure('faq-item', 'open', faq, { via: 'opened by its own toggle; the answer panel below measured with it' });
  }
  await page.close();
}

// ---------- /for-business ----------
async function business() {
  await newPage('business', { wait: 8000 });
  const flyBtn = await domFind(page, /^Business types$|^Features$/, { sel: 'button,a', tag: 'fly' });
  await S('nav-flyout-button', flyBtn, ['default', 'hover', 'focus-visible'], { group: G.business, title: 'Nav flyout button', desc: '"Business types" and "Features" in the marketing nav — each opens a mega-menu flyout on click/hover.', sel: 'button nav' }, { noScroll: true });
  if (await flyBtn.count()) {
    await reset();
    await toggle(flyBtn).catch(() => flyBtn.first().hover({ timeout: 4000 }).catch(() => {}));
    await page.waitForTimeout(900);
    const fly = await page.evaluate(() => {
      const c = [...document.querySelectorAll('[role="menu"], [data-state="open"] > div, div, nav')].filter((n) => {
        const r = n.getBoundingClientRect();
        return r.width > 300 && r.height > 150 && r.width < 1200 && /Hair|Nail|Spa|Barber|Massage/.test(n.innerText || '') && (n.innerText || '').length < 1500;
      });
      const el = c[c.length - 1];
      if (el) el.setAttribute('data-m-mark', 'flyout');
      return !!el;
    }).catch(() => false);
    if (fly) {
      // The flyout is hover-driven: moving the mouse off closes it, so the
      // item rows are measured as part of the flyout crop, not individually.
      await S('nav-flyout', q('[data-m-mark="flyout"]'), ['default'], { group: G.overlay, title: 'Nav flyout', desc: 'The mega-menu under "Business types": a column of vertical links (Salon, Barber, Nails, Spa & sauna, Medspa, Massage …). Opened by its own button.', sel: '[role=menu] flyout' }, { noScroll: true, noReset: true });
      await page.keyboard.press('Escape').catch(() => {});
      await page.waitForTimeout(700);
    }
  }
  const btitle = q('h1').first();
  await S('b2b-hero-title', btitle, ['default'], { group: G.business, title: 'Marketing hero title', desc: 'The /for-business display heading.', sel: 'h1' });
  const demo = await domFind(page, /Get a demo|Try for free|Get started/i, { sel: 'button,a', tag: 'demo' });
  await S('b2b-cta', demo, B4, { group: G.business, title: 'Marketing CTA', desc: 'The primary marketing button. Measured, never pressed.', sel: 'button CTA' });
  const watch = await domFind(page, /Watch an overview|Watch/i, { sel: 'button,a', tag: 'watch' });
  await S('watch-button', watch, B4, { group: G.business, title: 'Watch button', desc: '"Watch an overview" — the secondary media button.', sel: 'button Watch' });
  const typeCard = await domFind(page, /Hairdressers|Beauty|Nails|Barbers|Massage|Spas/i, { sel: 'a,article,div,li', tag: 'tcard', up: 'a,article,li', minW: 140, minH: 60 });
  await S('business-type-card', typeCard, ['default', 'hover'], { group: G.card, title: 'Business-type card', desc: 'A vertical-market card ("More info on …"): name plus icon. A link; measured, never followed.', sel: 'a business type' });
  const stat = await domFind(page, /\d+\s*(million|M\+?|billion)|#\d|Top rated/i, { sel: 'div,p,span,li', tag: 'stat', leaf: true, minW: 60 });
  await S('stat', stat, ['default'], { group: G.business, title: 'Stat', desc: 'A proof-point figure in the marketing stats row.', sel: 'stat' });
  await page.close();
}

// ---------- /lp browse microsite ----------
async function lp() {
  await newPage('lp', { wait: 9000 });
  await sheetsFor('lp');
  await S('lp-header', await chromeOf(/Menu|Hair Salon|Search/i), ['default'], { group: G.lp, title: 'LP top bar', desc: 'The /lp microsite chrome: its own stylesheet, no Panda vars — every value here is measured.', sel: 'lp chrome' }, { noScroll: true });
  // No painted filter rail exists on this page: the only controls are the top
  // search bar, the Sort select, the "See map" link and the category chips at
  // the foot. Hidden radios/checkboxes in the DOM belong to an unpainted block.
  const chip = await domFind(page, /Beauty Salons|Barbers|Nail Salons|Medspas/i, { sel: 'a,button,li', tag: 'chip', leaf: true, minW: 40 });
  await S('lp-category-chip', chip, ['default', 'hover'], { group: G.lp, title: 'Category chip', desc: 'A category pill in the footer browse row (Beauty Salons, Barbers, Nail Salons …). A link; measured, never followed.', sel: 'category chip' });
  // The card is measured first so its mark can scope the price and the
  // see-all link — unscoped, a page-wide "from $"/services query lands on the
  // header blurb or the whole services list instead of the card's own nodes.
  const card = await domFind(page, /reviews?|stars?|\d\.\d/i, { sel: 'a,article,li,div', tag: 'lpcard', up: 'article,li', minW: 240, minH: 100 });
  const lpc = (await card.count()) ? card : q('article, ol li').nth(1);
  await S('lp-venue-card', lpc, ['default', 'hover'], { group: G.lp, title: 'Browse venue card', desc: 'A venue result in the /lp list: photo, name, address, rating and review count, next-availability line.', sel: 'article venue' });
  const svcLine = await domFind(page, /S\$\s*\d+|from\s+S?GD|from\s+\$|\$\s*\d+/i, { sel: 'div,li,span,p', tag: 'svcl', leaf: true, minW: 10, minH: 8, root: '[data-m-mark="lpcard"]' });
  await S('lp-price', svcLine, ['default'], { group: G.lp, title: 'Card price', desc: 'A service price inside a venue card ("$98", "from $0").', sel: 'price span' });
  const seeAll = await domFind(page, /See all \d+ services/i, { sel: 'a,button,span,div,p', tag: 'seeall', leaf: true, root: '[data-m-mark="lpcard"]' });
  await S('lp-see-all', seeAll, ['default', 'hover'], { group: G.lp, title: 'See all services link', desc: 'The "See all N services" link inside a venue card. Measured, never followed.', sel: 'see-all link' });
  // The page's only other <select> is the header's language picker — never a
  // fallback: if no select offers sort criteria, the component stays missing
  // rather than measuring the wrong control.
  const sortMarked = await page.evaluate(() => {
    const s = [...document.querySelectorAll('select')].find((x) => /recommend|price|rating|distance|review|sort|nearest|popular/i.test(x.innerText || ''));
    if (s) s.setAttribute('data-m-mark', 'sortsel');
    return !!s;
  }).catch(() => false);
  const sel = sortMarked ? q('[data-m-mark="sortsel"]') : page.locator('[data-m-mark="__none__"]');
  await S('lp-sort-select', sel, ['default', 'focus-visible'], { group: G.form, title: 'Sort select', desc: 'The "Sort by" native select over the results list.', sel: 'select' });
  const mapBtn = await domFind(page, /See map|Map/i, { sel: 'button,a', tag: 'map' });
  await S('lp-map-button', mapBtn, B4, { group: G.lp, title: 'See map button', desc: 'Opens the map panel over the results. Measured at rest and opened by its own control where the overlay mounts.', sel: 'button "See map"' });
  if (await mapBtn.count()) {
    await reset();
    await toggle(mapBtn).catch(() => {});
    await page.waitForTimeout(1500);
    const overlay = await page.evaluate(() => {
      const c = [...document.querySelectorAll('[role="dialog"], div, aside, section')].filter((n) => {
        const r = n.getBoundingClientRect();
        return r.width > 500 && r.height > 400 && /map|km|mi\b/i.test(n.className + ' ' + (n.innerText || '').slice(0, 300));
      });
      const el = c[c.length - 1];
      if (el) el.setAttribute('data-m-mark', 'mapovl');
      return !!el;
    }).catch(() => false);
    if (overlay) await S('lp-map-overlay', q('[data-m-mark="mapovl"]'), ['default'], { group: G.overlay, title: 'Map overlay', desc: 'The map panel "See map" opens over the result list. Closed after measuring.', sel: 'map overlay' }, { noScroll: true });
    await page.keyboard.press('Escape').catch(() => {});
    const closeMap = await domFind(page, /close|back|list/i, { sel: 'button', tag: 'mapclose' });
    if (await closeMap.count()) await toggle(closeMap).catch(() => {});
    await page.waitForTimeout(700);
  }
  const pager = await domFind(page, /^2$|^Next$|next/i, { sel: 'a,button,[aria-label]', tag: 'pager' });
  await S('lp-pagination', pager, ['default', 'hover'], { group: G.lp, title: 'Pagination', desc: 'The result-list pager. Measured, never followed.', sel: 'pagination' });
  await page.close();
}

// ---------- /help-center ----------
async function help() {
  await newPage('help', { wait: 7000 });
  // Several hidden inputs share the placeholder; pick the one that paints.
  const hs = await page.evaluate(() => {
    const i = [...document.querySelectorAll('input')].find((n) => /help|search/i.test(n.placeholder || '') && n.getBoundingClientRect().width > 100);
    if (i) i.setAttribute('data-m-mark', 'hs');
    return !!i;
  }).catch(() => false);
  const search = hs ? q('[data-m-mark="hs"]') : q('input').filter({ visible: true }).first();
  await S('help-search', search, ['default', 'focused'], { group: G.help, title: 'Help search field', desc: 'The help-centre search input (a 654x60 pill). Focused only — no query is sent.', sel: 'input "Search our help center"' }, { noScroll: true });
  const topic = await domFind(page, /Booking|Account|Payments|Getting started|cancellation/i, { sel: 'a[href],article,li', tag: 'topic', up: 'a,article,li', minW: 140, minH: 40, leaf: true });
  await S('topic-card', topic, ['default', 'hover'], { group: G.help, title: 'Help topic card', desc: 'A help topic tile linking to an article group. Measured, never followed.', sel: 'a topic' });
  const article = await domFind(page, /How do I|What is|Can I|book|cancel/i, { sel: 'main a[href*="help"], ul a, ol a, a', tag: 'art', leaf: true });
  await S('article-link', article, ['default', 'hover'], { group: G.help, title: 'Article link', desc: 'A help article row. Measured, never followed.', sel: 'a article' });
  await page.close();
}

// ---------- mobile pass ----------
async function mobile() {
  await newPage('home', { mobile: true, wait: 7000 });
  // The mobile chrome is a 390x72 sticky div/nav with the wordmark and a
  // 32x32 icon-only burger (aria-label="Menu") — the desktop "Menu" pill is
  // not rendered.
  const mnav = q('nav[class*="grid"], div[class*="pos_sticky"]').first();
  await S('m-header', mnav, ['default'], { group: G.mobile, title: 'Mobile top bar', desc: 'The 390x72 sticky mobile bar: wordmark left, icon burger right.', sel: 'nav sticky' }, { noScroll: true });
  const menuBtn = q('button[aria-label="Menu"], button[aria-label*="menu" i]').first();
  await S('m-menu-button', menuBtn, B4, { group: G.mobile, title: 'Mobile menu button', desc: 'The 32x32 icon-only burger (aria-label "Menu") in the mobile bar.', sel: 'button[aria-label=Menu]' }, { noScroll: true });
  const tf = q('input[placeholder*="treatment" i], [role="combobox"], input').first();
  await S('m-search-field', tf, ['default', 'focused'], { group: G.mobile, title: 'Mobile search field', sel: 'input' });
  const card = q('a[href*="/a/"]').first();
  await S('m-venue-card', card, ['default'], { group: G.mobile, title: 'Mobile venue card', sel: 'a[href*="/a/"]' });
  await page.close();
}

const PAGES = { home, userflow, auth, partner, venue, booking, pricing, business, lp, help, mobile };
const wanted = process.argv.slice(2).filter((a) => !a.startsWith('-'));
const order = wanted.length ? wanted : Object.keys(PAGES);

const { browser, context: ctx } = await launch();
context = ctx;
desktopContext = ctx;
run = new Date().toISOString();
out._meta.lastRun = run;
out._meta.base = BASE;
out._meta.boundary = 'signed-out public pages; nothing submitted, booked or signed in';

for (const name of order) {
  try {
    await PAGES[name]();
  } catch (e) {
    log('page failed', name, String(e).slice(0, 200));
    out._meta.errors ??= {};
    out._meta.errors[name] = String(e).slice(0, 300);
  }
  save();
}

// Mark components whose spec found nothing in this run (keep stale states but flag).
for (const [key, st] of listed) {
  const c = out.components[key];
  if (c && c.missing) c.note = 'not found on this run';
}

await browser.close();
save();
log('done —', Object.keys(out.components).length, 'components');
