// Measures Expedia's components on its public pages, in every state that can be
// reached without signing in, searching or booking anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home home-i search mobile.
//   home    the archived home page, scripts blocked: the SSR markup paints the
//           header nav and menus that hydration strips
//   home-i  the same page hydrated with the site's own JS, so the search
//           form's panels (calendar, room picker, destination) open on click
//   search  the archived Hotel-Search results, scripts blocked
//   mobile  home at 390 x 844, scripts blocked
// Writes raw/components-computed.json (merged, so a subset of pages can be re-run)
// and one crop per component and state into components/crops/. raw/measurements.md
// is then built from the JSON by build-measurements.mjs.
//
// States:
//   hover          real mouse hover, 450ms settle for transitions
//   focus-visible  keyboard: focus, Shift+Tab, Tab, so the browser sees a keyboard focus
//   pressed        CDP CSS.forcePseudoState [active, hover]; no mouse button is pressed,
//                  so no link or submit button can fire
//   open           a resting state reached through the page's own no-JS menu
//                  mechanism or a field trigger click; nothing is searched,
//                  signed into or booked
//   focused        the field clicked into (a text field only)
//   filled         sample text typed into a field, measured, then deleted; Enter
//                  is never pressed
import crypto from 'node:crypto';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { servePages, open, launch, styleOf, crop, centre, RAW, REF, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => { out._meta.read = new Date().toISOString().slice(0, 10); fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n'); };

const PAGESDIR = process.env.PAGES || path.join(os.homedir(), '.design-systems', 'expedia', 'pages');
const { srv, port } = await servePages(PAGESDIR);
const LOCAL = `http://127.0.0.1:${port}`;
// Which archived copy each page was read from: the inputs live outside the repo, so the file name
// and its hash are the only way a later rebuild can tell whether it saw the same snapshot.
const pageFile = (key) => (URLS[key] ? new URL(URLS[key]).pathname.replace(/^\/+/, '').replace(/^pages\//, '') : null);
const URLS = {
  home: `${LOCAL}/pages/home.html`,
  'home-i': `${LOCAL}/pages/home.html`,
  search: `${LOCAL}/pages/search.html`,
  mobile: `${LOCAL}/pages/home.html`,
};

let page, cdp, current, context, mobileContext, run;
const touched = new Set();

// ---------- helpers ----------

async function newPage(key, { mobile = false } = {}) {
  current = key;
  const ctx = mobile
    ? (mobileContext ??= await context.browser().newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }))
    : context;
  page = await ctx.newPage();
  page.setDefaultTimeout(8000);
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  const hydrate = key === 'home-i';
  log('open', key, mobile ? '(mobile)' : '', hydrate ? '(hydrated)' : '(ssr)', URLS[key]);
  await open(page, URLS[key], { wait: hydrate ? 12000 : 7000, hydrate });
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
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
  // each component stamps its own read date: a page that fails later in the
  // run keeps its older readings visibly dated instead of looking fresh
  Object.assign(c, { page: current, run, url: current === 'search' ? 'wayback:expedia.com/Hotel-Search' : 'wayback:expedia.com/', read: new Date().toISOString().slice(0, 10) }, meta);
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
    // A failed re-read must not erase an earlier successful one: keep the
    // saved style and record the failed attempt beside it.
    const prev = c.states[state];
    if (prev && prev.style) prev.rerunError = String(e.message || e).slice(0, 200);
    else c.states[state] = { error: String(e.message || e).slice(0, 200) };
    log('  !', key, state, String(e.message).slice(0, 120));
  }
}

// Records the listed states of one component. meta: title, group, desc, sel.
async function S(key, target, list, meta = {}, opts = {}) {
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
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
        await (opts.fieldLoc || loc).filter({ visible: true }).first().click({ timeout: 4000, force: true });
        await page.waitForTimeout(400);
        via = 'clicked into the field';
      } else if (st === 'filled') {
        const f = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await f.click({ timeout: 4000, force: true });
        await page.keyboard.type(opts.fillText || 'Las Vegas', { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || 'Las Vegas'}", then deleted; nothing sent`;
      } else via = via || opts.via || 'at rest';
      if (st === 'focus-visible' && via === 'focus failed') {
        const prev = out.components[key].states[st];
        if (prev && prev.style) prev.rerunError = 'keyboard focus did not reach the element';
        else {
          if (prev && prev.crop) fs.rmSync(path.join(REF, prev.crop), { force: true });
          out.components[key].states[st] = { error: 'keyboard focus did not reach the element', via };
        }
        log('  !', key, st, 'focus failed');
      } else {
        await measure(key, st, loc, { ...opts, via });
      }
    } catch (e) {
      const prev = out.components[key].states[st];
      if (prev && prev.style) prev.rerunError = String(e.message || e).slice(0, 200);
      else out.components[key].states[st] = { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
    if (undo) await undo().catch(() => {});
    if (opts.after?.[st]) await opts.after[st](loc).catch(() => {});
  }
  await reset();
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const B3 = ['default', 'hover', 'focus-visible'];

// Tags the first element matching an in-page probe so a locator can find it:
// await tag('x', () => {...return element or null...}) then q('[data-m="x"]').
async function tag(name, probe, arg) {
  return page.evaluate(([n, src, a]) => {
    const el = (new Function('return (' + src + ')')())(a);
    if (!el) return false;
    el.setAttribute('data-m', n);
    return true;
  }, [name, probe.toString(), arg === undefined ? null : arg]).catch(() => false);
}

// Tags the smallest element whose trimmed text matches reSrc inside scopeSel,
// preferring an interactive tag or a cursor:pointer box.
async function tagEl(name, reSrc, scopeSel) {
  return page.evaluate(([n, src, scope]) => {
    const re = new RegExp(src, 'i');
    const sc = (scope && document.querySelector(scope)) || document;
    const cands = [...sc.querySelectorAll('a,button,[role=button],[role=tab],li,div,span')].filter((e) => {
      const t = (e.innerText || e.getAttribute('aria-label') || '').trim(); const r = e.getBoundingClientRect();
      return re.test(t) && t.length < 80 && r.width > 10 && r.height > 8;
    }).sort((a, b) => (a.innerText || '').length - (b.innerText || '').length);
    let el = cands.find((e) => e.matches('a,button,[role=button],[role=tab],li,[tabindex]') || getComputedStyle(e).cursor === 'pointer') || cands[0];
    if (!el) return false;
    for (let i = 0; i < 4 && el.parentElement; i++) {
      const p = el.parentElement;
      const pt = (p.innerText || '').trim();
      if (!(p.matches('a,button,[role=button],[role=tab]') || getComputedStyle(p).cursor === 'pointer')) break;
      if (!re.test(pt) || pt.length > 80) break;
      el = p;
    }
    el.setAttribute('data-m', n);
    return true;
  }, [name, reSrc, scopeSel || null]).catch(() => false);
}

// Opens the SSR uitk-menu whose checkbox the server marked aria-checked=want
// ('true' for the Sign in card, 'false' for "Shop travel"): its no-JS path.
async function openUitkMenu(want) {
  await page.evaluate((w) => {
    for (const m of document.querySelectorAll('.uitk-menu')) {
      const cb = m.querySelector('input.uitk-menu-checkbox');
      if (!cb || cb.getAttribute('aria-checked') !== w) continue;
      cb.checked = true;
      const c = m.querySelector('.uitk-menu-container');
      if (c) c.style.display = 'block';
      return true;
    }
    return false;
  }, want);
  await page.waitForTimeout(600);
}
async function closeUitkMenus() {
  await page.evaluate(() => {
    for (const m of document.querySelectorAll('.uitk-menu')) {
      const cb = m.querySelector('input.uitk-menu-checkbox');
      if (cb) cb.checked = false;
      const c = m.querySelector('.uitk-menu-container');
      if (c) c.style.removeProperty('display');
    }
  }).catch(() => {});
}

// ---------- groups ----------
const G = {
  shell: 'Header and navigation', searchbar: 'Search form', panels: 'Menus and dialogs',
  home: 'Home content', search: 'Hotel results', mobile: 'Mobile (390 wide)',
};

// ---------- home (SSR) ----------

async function home() {
  await newPage('home');
  const g = G.shell;

  await S('header', q('header'), ['default'], { group: g, title: 'Header', desc: 'The top bar over the whole page: the Expedia logo, the "Shop travel" menu, the USD currency control, "List your property", "Support", "Trips", the notifications bell and "Sign in".', sel: 'header' }, { noScroll: true });
  await S('header-logo', q('header a').first(), ['default'], { group: g, title: 'Logo link', sel: 'the first link in the header (the Expedia logo)' }, { noScroll: true });
  await S('header-shop-travel', q('button[data-testid="header-menu-button"]').first(), B4, { group: g, title: 'Shop travel menu button', desc: 'The nav menu trigger next to the logo: a tertiary uitk-button with a chevron. Pressed is forced; the menu is shot separately on the public page.', sel: 'button[data-testid="header-menu-button"] (first)' }, { noScroll: true });
  await S('header-signin', q('button[data-testid="header-menu-button"]:has-text("Sign in")'), B4, { group: g, title: 'Sign in button', desc: 'The account menu trigger rightmost in the header. Pressed is forced: a real click only opens the guest card, measured separately.', sel: 'header "Sign in" button' }, { noScroll: true });
  if (await tagEl('curr', '^(USD|US\\$|\\$)', 'header'))
    await S('header-currency', q('[data-m="curr"]'), B3, { group: g, title: 'Currency button', desc: 'The locale/currency control in the header ("USD" + flag). Hovered and focused only.', sel: 'header control reading USD' }, { noScroll: true });
  await S('header-link', q('a[data-stid="support-cs-link"]'), B3, { group: g, title: 'Header link', desc: 'A plain header link ("Support"; "Trips" and "List your property" share the style): tertiary as-link buttons.', sel: 'a[data-stid="support-cs-link"]' }, { noScroll: true });

  // The guest sign-in card, opened through the SSR no-JS menu mechanism.
  const openSignin = async () => { await openUitkMenu('true'); };
  const signinMenu = q('.uitk-menu-container');
  if (await tag('signinmenu', () => {
    for (const m of document.querySelectorAll('.uitk-menu')) {
      const cb = m.querySelector('input.uitk-menu-checkbox');
      if (cb && cb.getAttribute('aria-checked') === 'true') return m.querySelector('.uitk-menu-container');
    }
    return null;
  })) {
    await S('signin-card', q('[data-m="signinmenu"]'), ['open'], { group: g, title: 'Sign-in card', desc: 'The 375px guest menu the Sign in button opens: "Unlock instant savings with Member Prices", the primary Sign in button, "Learn more about One Key" and a Feedback link. Opened through the SSR checkbox mechanism; nothing was submitted.', sel: '.uitk-menu-container of the Sign in uitk-menu' }, { noScroll: true, before: { open: openSignin }, after: { open: closeUitkMenus } });
    if (await tag('signinbtn', () => document.querySelector('[data-m="signinmenu"] .uitk-button-primary, [data-m="signinmenu"] button'))) {
      await openSignin();
      await S('signin-card-button', q('[data-m="signinbtn"]'), ['open', 'hover'], { group: g, title: 'Sign-in card button', desc: 'The blue primary "Sign in" button inside the guest card. Hovered only, never pressed.', sel: 'primary button inside the sign-in card' }, { noScroll: true });
      await closeUitkMenus();
    }
    await closeUitkMenus();
  }

  const s = G.searchbar;
  await S('search-shell', q('[data-testid="multi-product-search-form"], [data-stid="search-form-sticky"]').first(), ['default'], { group: s, title: 'Search form shell', desc: 'The white rounded card under the hero holding the product tabs and the three search fields with the Search button.', sel: '[data-testid="multi-product-search-form"]' }, { noScroll: true });
  const tabs = q('[role=tab]');
  await S('search-tabs', q('[role=tablist]').first(), ['default'], { group: s, title: 'Product tabs', desc: 'The tab rail atop the form: Stays, Flights, Cars, Packages, Things to do, Cruises, each an icon over a label.', sel: '[role=tablist]' }, { noScroll: true });
  const activeTab = q('[role=tab][aria-selected="true"], [data-stid="uitk-tab-active"]').first();
  await S('tab-active', activeTab, B4, { group: s, title: 'Product tab (active)', desc: 'The current product tab (Stays): label and icon in the primary blue with a 2px underline.', sel: '[role=tab][aria-selected=true]' }, { noScroll: true });
  await S('tab', tabs.filter({ hasText: 'Flights' }).first(), B4, { group: s, title: 'Product tab', desc: 'A resting product tab (Flights). Pressed is forced: a real click switches the form, shot separately on the hydrated page.', sel: '[role=tab] "Flights"' }, { noScroll: true });
  // SSR fields are .uitk-field boxes (label + pointer-events-none input + icon);
  // hydration wraps them in the button.uitk-form-field-trigger the panels open on.
  await S('field-destination', q('[data-stid="search-location"] .uitk-field'), B4, { group: s, title: 'Destination field', desc: 'The "Where to?" field: a uitk-field box with floated label, pin icon and empty input; once hydrated its trigger button opens the destination panel. Pressed is forced.', sel: '[data-stid="search-location"] .uitk-field' }, { noScroll: true });
  await S('field-dates', q('.uitk-field').filter({ hasText: 'Dates' }).first(), B4, { group: s, title: 'Dates field', desc: 'The "Dates" field with the range value (Fri, Feb 13 - Tue, Feb 17) and a calendar icon. Pressed is forced: a click opens the calendar.', sel: '.uitk-field containing "Dates"' }, { noScroll: true });
  await S('field-travelers', q('.uitk-field').filter({ hasText: 'Travelers' }).first(), B4, { group: s, title: 'Travelers field', desc: 'The "Travelers" field ("2 travelers, 1 room") with a person icon. Pressed is forced: a click opens the room picker.', sel: '.uitk-field containing "Travelers"' }, { noScroll: true });
  if (await tagEl('searchbtn', '^Search$', '[data-testid="multi-product-search-form"], [data-stid="search-form-sticky"]'))
    await S('search-submit', q('[data-m="searchbtn"]'), B4, { group: s, title: 'Search button', desc: 'The primary Search button at the form\'s right end (uitk-button-primary-large). Pressed is forced: a real press would run a search.', sel: 'the Search button in the search form' }, { noScroll: true });
  if (await tagEl('bundlecb', 'Add a flight to Bundle'))
    await S('bundle-checkbox', q('[data-m="bundlecb"]'), ['default'], { group: s, title: 'Bundle & Save checkbox', desc: 'The "Add a flight to Bundle & Save*" checkbox under the fields: an uitk-checkbox box plus label.', sel: 'the Bundle & Save checkbox' }, { noScroll: true, cropLoc: q('[data-m="bundlecb"]') });
  await S('tertiary-button', q('.uitk-button:has-text("See all deals"), a.uitk-button:has-text("See all deals")').first(), B4, { group: s, title: 'Tertiary button', desc: 'The "See all deals" button by the deals heading: outlined tertiary uitk-button. Pressed is forced, never followed.', sel: '"See all deals" uitk-button' }, { noScroll: true });

  const h = G.home;
  await S('hero-title', q('[data-testid="hero-title-campaign"]'), ['default'], { group: h, title: 'Hero title', desc: '"The one place you go to go places" over the hero photo: the display type style in Reckless XPD, inverse colour.', sel: '[data-testid="hero-title-campaign"]' }, { noScroll: true });
  if (await tag('band', () => { const s = document.querySelector('section[data-theme-light="marketing-3"]'); return s ? [...s.querySelectorAll('div,section')].find((d) => d.getBoundingClientRect().height > 50) : null; }))
    await S('marketing-band', q('[data-m="band"]'), ['default'], { group: h, title: 'Marketing band', desc: 'The section re-themed data-theme-light="marketing-3": the pale-blue palette applied to the same components (the promo strip under the search form).', sel: 'section[data-theme-light="marketing-3"] (first child)' }, { noScroll: true });
  // the first .uitk-card IS the search shell; a deal card is a small carousel-item card holding a save button
  if (await tag('dealcard', () => [...document.querySelectorAll('[data-stid="carousel-item"] .uitk-card')].find((c) => { const r = c.getBoundingClientRect(); return r.width > 100 && r.width < 500 && c.querySelector('[data-stid="outlined-save-button"], img'); })))
    await S('deal-card', q('[data-m="dealcard"]'), ['default', 'hover'], { group: h, title: 'Deal card', desc: 'One card in the deals carousels: a uitk-card with rounded corners, the gallery photo, a heart save button, the property name and the price.', sel: 'a deals .uitk-card' });
  await S('card-heart', q('[data-stid="outlined-save-button"]').first(), B4, { group: h, title: 'Save (heart) button', desc: 'The heart save control over a card photo: a round white button, pressed state forced so nothing is saved.', sel: '[data-stid="outlined-save-button"]' });
  await S('footer-link', q('footer a').first(), ['default', 'hover'], { group: h, title: 'Footer link', desc: 'A link in the page footer.', sel: 'footer a (first)' });
}

// ---------- home-i (hydrated: the panels that need the site's own JS) ----------

async function homeI() {
  await newPage('home-i');
  const g = G.panels;
  const trig = q('button.uitk-form-field-trigger');

  if (await trig.nth(1).count()) {
    await trig.nth(1).click({ force: true }).catch(() => {});
    await page.waitForTimeout(3500);
    const dlg = q('[role=dialog]').filter({ hasText: 'Calendar' }).first();
    await S('calendar-dialog', dlg, ['open'], { group: g, title: 'Calendar dialog', desc: 'The date picker the Dates field opens: Calendar/Flexible dates tabs, the range line, two months, weekday headings, the selected range endpoints as filled blue days, the ±day flexibility chips and the Done button. Opened by clicking the field trigger; Escape closed it, nothing was searched.', sel: '[role=dialog] containing "Calendar"' }, { noScroll: true });
    if (await tag('daysel', () => [...document.querySelectorAll('[role=dialog] button, [role=dialog] [class*=day]')].find((b) => b.getAttribute('aria-pressed') === 'true' || /selected/i.test(b.getAttribute('aria-label') || ''))))
      await S('calendar-day-selected', q('[data-m="daysel"]'), ['open'], { group: g, title: 'Calendar day (selected)', desc: 'A range endpoint in the calendar: the filled primary circle.', sel: 'the selected day button in the calendar' }, { noScroll: true });
    if (await tagEl('calchip', '± 2 days|Exact dates', '[role=dialog]'))
      await S('calendar-chip', q('[data-m="calchip"]'), ['open'], { group: g, title: 'Flexibility chip', desc: 'The "Exact dates" / "± N days" chips under the calendar: outlined pills, the active one filled.', sel: 'a ±days chip in the calendar dialog' }, { noScroll: true });
    if (await tagEl('caldone', '^Done$', '[role=dialog]'))
      await S('dialog-done', q('[data-m="caldone"]'), ['open', 'hover'], { group: g, title: 'Dialog Done button', desc: 'The primary Done button at the foot of the calendar. Hovered only, never pressed.', sel: 'the Done button in the calendar dialog' }, { noScroll: true });
    await page.keyboard.press('Escape').catch(() => {});
    await page.waitForTimeout(800);
  }

  if (await trig.nth(2).count()) {
    await trig.nth(2).click({ force: true }).catch(() => {});
    await page.waitForTimeout(2500);
    if (await tag('trav', () => [...document.querySelectorAll('[role=dialog], .uitk-menu-container, [data-stid="rooms-traveler-selector-menu-container"]')].find((d) => /Room 1|Adults/.test(d.innerText || ''))))
      await S('travelers-menu', q('[data-m="trav"]'), ['open'], { group: g, title: 'Travelers menu', desc: 'The room picker the Travelers field opens: "Room 1", the Adults and Children steppers (−/+), "Add another room", the group-booking line and Done. Opened by clicking the field trigger; Escape closed it.', sel: 'the travelers panel ([role=dialog] or uitk-menu)' }, { noScroll: true });
    if (await tag('stepbtn', () => [...document.querySelectorAll('[role=dialog] button, .uitk-menu-container button, [data-stid="rooms-traveler-selector-menu-container"] button')].find((b) => /increment|increase|add adult|plus|\\+/i.test(b.getAttribute('aria-label') || '') || (b.innerText || '').trim() === '+')))
      await S('stepper-button', q('[data-m="stepbtn"]'), ['open', 'hover'], { group: g, title: 'Stepper button', desc: 'A + stepper in the room picker: a round outlined button. Hovered only; the count was never changed.', sel: 'a + button in the travelers panel' }, { noScroll: true });
    await page.keyboard.press('Escape').catch(() => {});
    await page.waitForTimeout(800);
  }

  if (await trig.nth(0).count()) {
    await trig.nth(0).click({ force: true }).catch(() => {});
    await page.waitForTimeout(2500);
    if (await tag('where', () => [...document.querySelectorAll('[role=dialog], .uitk-menu-container, [class*=sheet], [data-stid]')].filter((d) => /Search by destination/.test(d.innerText || '') && d.getBoundingClientRect().width > 200).sort((a, b) => (a.innerText || '').length - (b.innerText || '').length)[0]))
      await S('whereto-panel', q('[data-m="where"]'), ['open'], { group: g, title: 'Destination panel', desc: 'The panel the Where to? field opens: the prompt, the magnifier and the "Search by destination, accommodations, or landmark" input. Opened by clicking the field trigger.', sel: 'the destination panel' }, { noScroll: true });
    const inp = q('[role=dialog] input, .uitk-menu-container input').filter({ visible: true }).first();
    await S('whereto-input', inp, ['filled'], { group: g, title: 'Destination input', desc: 'The free-text destination field inside the panel; text was typed and deleted, nothing searched.', sel: 'the input inside the destination panel' }, { noScroll: true, fillText: 'Las Vegas' });
    await page.keyboard.press('Escape').catch(() => {});
    await page.waitForTimeout(800);
  }
}

// ---------- search (SSR results) ----------

async function search() {
  await newPage('search');
  const g = G.search;

  await S('search-form-sticky', q('form#lodging_search_form, form:has([data-stid="search-location"])').first(), ['default'], { group: g, title: 'Sticky search form', desc: 'The compact search bar pinned under the header on the results page: the same three fields plus the round search button.', sel: 'form#lodging_search_form' }, { noScroll: true });
  await S('header-signin-search', q('button[data-testid="header-menu-button"]:has-text("Sign in")'), B3, { group: g, title: 'Sign in button (results)', sel: 'header "Sign in" button' }, { noScroll: true });
  const seg = q('[role=tablist], [role=radiogroup]').filter({ hasText: 'All stays' }).first();
  await S('stay-type-tabs', seg, ['default'], { group: g, title: 'Stay type tabs', desc: 'The segmented "All stays / Hotels / Homes" control above the results.', sel: 'the All stays segmented control' }, { noScroll: true });
  await S('sort-control', q('#sort-filter-sort-pill-sort, button.uitk-pill:has-text("Sort by")').first(), B3, { group: g, title: 'Sort control', desc: 'The "Sort by recommended for you" uitk-pill over the results list. Hovered and focused only, never opened.', sel: '#sort-filter-sort-pill-sort' }, { noScroll: true });
  if (await tag('propsummary', () => [...document.querySelectorAll('body *')].find((e) => /^\d+\s+properties$/.test((e.innerText || '').trim()))))
    await S('results-summary', q('[data-m="propsummary"]'), ['default'], { group: g, title: 'Results count', desc: 'The "N properties" line over the results list.', sel: 'the "N properties" text' }, { noScroll: true });

  const card = q('[data-stid="lodging-card-responsive"]').first();
  await S('property-card', card, ['default', 'hover'], { group: g, title: 'Property card', desc: 'One result card (uitk-card): the 21:9 photo gallery with carousel arrows and the heart, VIP badge, name, amenity icons, refund line, rating pill, nightly and total prices, and the "Sign in for extra savings" pill.', sel: '[data-stid="lodging-card-responsive"]' });
  await S('card-gallery', card.locator('.uitk-gallery-carousel').first(), ['default'], { group: g, title: 'Card gallery', desc: 'The 21:9 image carousel in a result card with prev/next circle buttons.', sel: '.uitk-gallery-carousel in a property card' });
  if (await tag('priceblock', () => {
    const c = document.querySelector('[data-stid="lodging-card-responsive"]');
    if (!c) return null;
    const m = [...c.querySelectorAll('div,section')].filter((e) => /nightly/.test(e.innerText || '') && /total/.test(e.innerText || '') && (e.innerText || '').length < 200).sort((a, b) => (a.innerText || '').length - (b.innerText || '').length);
    return m[0] || null;
  }))
    await S('price-block', q('[data-m="priceblock"]'), ['default'], { group: g, title: 'Price block', desc: 'The right-aligned price area of a result card: the struck list price, the nightly rate in the headline size, and the total with taxes in muted text.', sel: 'the price area of a property card' });
  if (await tag('rating', () => {
    const c = document.querySelector('[data-stid="lodging-card-responsive"]');
    if (!c) return null;
    return [...c.querySelectorAll('div,span')].find((e) => /Exceptional|Wonderful|Very Good|Good/.test(e.innerText || '') && /reviews/.test(e.innerText || '') && (e.innerText || '').length < 60) || null;
  }))
    await S('rating-pill', q('[data-m="rating"]'), ['default'], { group: g, title: 'Rating pill', desc: 'The guest rating on a card: the score chip (9.4) in positive green beside the word and the review count.', sel: 'the rating area of a property card' });
  if (await tag('savecta', () => [...document.querySelectorAll('[data-stid="lodging-card-responsive"] button, [data-stid="lodging-card-responsive"] a')].find((b) => /Sign in for extra savings/.test(b.innerText || ''))))
    await S('savings-pill', q('[data-m="savecta"]'), B3, { group: g, title: '"Sign in for extra savings" pill', desc: 'The filled primary-blue pill button with white text on each card pointing signed-out guests at member prices (the fill paints on its ::after layer). Hovered and focused only, never followed.', sel: 'the "Sign in for extra savings" button' });
  if (await tag('vip', () => [...document.querySelectorAll('[data-stid="lodging-card-responsive"] *')].find((e) => (e.innerText || '').trim() === 'VIP Access')))
    await S('vip-badge', q('[data-m="vip"]'), ['default'], { group: g, title: 'VIP Access badge', desc: 'The dark "VIP Access" chip pinned over the card photo.', sel: 'the VIP Access badge on a property card' });
  await S('card-heart-search', q('[data-stid="lodging-card-responsive"] [data-stid="outlined-save-button"], [data-stid="outlined-save-button"]').first(), B4, { group: g, title: 'Save (heart) button', desc: 'The heart over the card photo. Pressed is forced; nothing was saved.', sel: '[data-stid="outlined-save-button"] on a property card' });
  if (await tag('carbtn', () => document.querySelector('[data-stid="lodging-card-responsive"] .uitk-button-paging')))
    await S('carousel-nav', q('[data-m="carbtn"]'), B3, { group: g, title: 'Carousel arrow', desc: 'A round prev/next button in the card gallery (uitk-button-paging). Hovered and focused only.', sel: 'an uitk-button-paging in a property card' });
  if (await tagEl('amen', 'Hot tub on site|Bar and lounge|Restaurant|Balcony', '[data-stid="lodging-card-responsive"]'))
    await S('amenity-item', q('[data-m="amen"]'), ['default'], { group: g, title: 'Amenity line', desc: 'One amenity row on a card: a small icon and a muted label.', sel: 'an amenity line in a property card' });

  // filters column
  await S('filters', q('form.uitk-form').filter({ hasText: 'Filter by' }).first(), ['default'], { group: g, title: 'Filter column', desc: 'The left filter rail: "Search by property name", "Filter by" groups (Property class checkboxes, Guest rating radios), See more links.', sel: 'the Filter by sidebar form' });
  if (await tagEl('namefld', 'Search by property name|e\\.g\\. Marriott'))
    await S('name-field', q('[data-m="namefld"]'), ['default', 'focused'], { group: g, title: 'Property name field', desc: 'The "e.g. Marriott" text input in the filter rail. Clicked into only.', sel: 'the Search by property name field' });
  if (await tag('fchk', () => document.querySelector('.uitk-checkbox')))
    await S('filter-checkbox', q('[data-m="fchk"]'), ['default', 'hover'], { group: g, title: 'Filter checkbox', desc: 'A "Property class" checkbox in the filter rail: an uitk-checkbox box with its count-bearing label. Hovered only, never toggled.', sel: 'an uitk-checkbox in the filter rail' });
  if (await tag('frad', () => document.querySelector('.uitk-radio')))
    await S('filter-radio', q('[data-m="frad"]'), ['default', 'hover'], { group: g, title: 'Filter radio', desc: 'A "Guest rating" radio in the filter rail. Hovered only, never toggled.', sel: 'an uitk-radio in the filter rail' });
  if (await tag('sw', () => document.querySelector('.uitk-switch, [role=switch]')))
    await S('compare-switch', q('[data-m="sw"]'), ['default', 'hover'], { group: g, title: 'Compare switch', desc: 'The "Compare properties" toggle over the filter rail. Hovered only, never switched.', sel: 'the compare uitk-switch' });
  if (await tagEl('urgent', 'We have \\d+ left'))
    await S('urgency-note', q('[data-m="urgent"]'), ['default'], { group: g, title: 'Urgency note', desc: '"We have 1 left at this price" under a price: the critical-coloured nudge line.', sel: 'the "We have N left" text on a card' });
  if (await tagEl('refund', 'Fully refundable', '[data-stid="lodging-card-responsive"]'))
    await S('refund-note', q('[data-m="refund"]'), ['default'], { group: g, title: 'Refund note', desc: '"Fully refundable" / "Reserve now, pay later" in positive green.', sel: 'the Fully refundable text on a card' });
  if (await tag('mapcard', () => { const b = document.querySelector('[data-stid="map-trigger-image"]'); return b ? b.closest('.uitk-card') : null; }))
    await S('map-card', q('[data-m="mapcard"]'), ['default'], { group: g, title: 'Map card', desc: 'The static map tile card at the top of the filter rail ("View in a map").', sel: 'the .uitk-card holding the static map' });
}

// ---------- mobile ----------

async function mobile() {
  await newPage('mobile', { mobile: true });
  const g = G.mobile;
  await S('m-header', q('header'), ['default'], { group: g, title: 'Header', desc: 'The mobile top bar.', sel: 'header' }, { noScroll: true });
  await S('m-hero-title', q('[data-testid="hero-title-campaign"]'), ['default'], { group: g, title: 'Hero title', sel: '[data-testid="hero-title-campaign"]' }, { noScroll: true });
  await S('m-search-shell', q('[data-testid="multi-product-search-form"], [data-stid="search-form-sticky"]').first(), ['default'], { group: g, title: 'Search form', sel: '[data-testid="multi-product-search-form"]' }, { noScroll: true });
  await S('m-field', q('[data-stid="search-location"] .uitk-field, .uitk-field').first(), B4, { group: g, title: 'Search field', desc: 'The first search field at 390 wide.', sel: '.uitk-field' }, { noScroll: true });
  if (await tagEl('msearchbtn', '^Search$', '[data-testid="multi-product-search-form"], [data-stid="search-form-sticky"]'))
    await S('m-search-button', q('[data-m="msearchbtn"]'), B4, { group: g, title: 'Search button', sel: 'the Search button' }, { noScroll: true });
  // the first .uitk-card is the search shell; a deal card is a small
  // carousel-item card holding a save button (same probe as the desktop page)
  if (await tag('mdealcard', () => [...document.querySelectorAll('[data-stid="carousel-item"] .uitk-card')].find((c) => { const r = c.getBoundingClientRect(); return r.width > 100 && r.width < 500 && c.querySelector('[data-stid="outlined-save-button"], img'); })))
    await S('m-card', q('[data-m="mdealcard"]'), ['default'], { group: g, title: 'Deal card', sel: 'a deals .uitk-card' });
  else delete out.components['m-card'];
}

// ---------- run ----------

// A component recorded for a page this run finished but never touched is stale evidence from an
// earlier capture (a probe that returned false, or a page that changed): flag it missing so it
// cannot read as a fresh measurement on a subset run (a full run drops it below). Ported from the
// airbnb base, which this fork dropped.
function sweepMissing(pageName) {
  for (const [k, c] of Object.entries(out.components)) {
    if (c.page === pageName && !touched.has(k) && !c.missing) {
      c.missing = true;
      log('  ! not found this run', k);
    }
  }
}

const RUNS = { home, 'home-i': homeI, search, mobile };
const { browser, context: ctx } = await launch();
context = ctx;
const only = process.argv.slice(2);
run = new Date().toISOString();
const finishedPages = new Set();
for (const key of Object.keys(RUNS)) {
  if (only.length && !only.includes(key)) continue;
  const file = pageFile(key);
  if (file && fs.existsSync(path.join(PAGESDIR, file))) {
    (out._meta.pages ??= {})[key] = { file, sha256: crypto.createHash('sha256').update(fs.readFileSync(path.join(PAGESDIR, file))).digest('hex') };
  }
  try {
    await RUNS[key]();
    finishedPages.add(key);
    sweepMissing(key);
    if (out._meta.failed) delete out._meta.failed[key];
    save();
  } catch (e) {
    const msg = e.message.split('\n')[0].slice(0, 160);
    log('PAGE FAILED', key, msg);
    // record the failure against the page instead of letting its old components read as fresh
    (out._meta.failed ??= {})[key] = msg;
    save();
  }
  if (page) await page.close().catch(() => {});
}
// Drop components no page touched this full run — but only ones from a page
// that finished: a page that failed mid-run keeps its earlier readings under
// their original provenance instead of losing them to the cleanup.
for (const k of Object.keys(out.components)) if (!touched.has(k) && !only.length && finishedPages.has(out.components[k].page)) delete out.components[k];
save();
await browser.close();
srv.close();
console.log('components:', Object.keys(out.components).length, '->', OUT);
