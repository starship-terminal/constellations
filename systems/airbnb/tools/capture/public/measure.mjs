// Measures Airbnb's components on its public pages, in every state that can be
// reached without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home search room help host mobile.
// Writes raw/components-computed.json (merged, so a subset of pages can be re-run)
// and one crop per component and state into components/crops/. raw/measurements.md
// is then built from the JSON by build-measurements.mjs.
//
// States:
//   hover          real mouse hover, 450ms settle for transitions
//   focus-visible  keyboard: focus, Shift+Tab, Tab, so the browser sees a keyboard focus
//   pressed        CDP CSS.forcePseudoState [active, hover]; no mouse button is pressed,
//                  so no link or submit button can fire
//   open           a UI toggle opened without submitting anything (the Where
//                  segment of the search bar); never a search, booking or sign-in
//   anything else  a resting state reached by the page itself
import fs from 'node:fs';
import path from 'node:path';
import { BASE, UA, UA_MOBILE, launch, open, sweepOverlays, firstRoomHref, styleOf, crop, centre, markFixed, RAW, REF, assertProductPage } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => { out._meta.read = new Date().toISOString().slice(0, 10); fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n'); };

const URLS = {
  home: '/', search: '/s/Tokyo--Japan/homes', room: 'ROOM',
  help: '/help', host: '/host/homes', mobile: '/',
};
let roomHref = null;
const urlFor = (key) => {
  const u = URLS[key];
  if (u === 'ROOM') return roomHref ? BASE + roomHref : BASE + '/';
  return BASE + u;
};

let page, cdp, current, context, run;
const touched = new Set();

// ---------- helpers ----------

async function newPage(key, { mobile = false, sweep = 'sweep', wait = 9000 } = {}) {
  current = key;
  page = await context.newPage();
  page.setDefaultTimeout(8000);
  cdp = await context.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  log('open', key, mobile ? '(mobile)' : '', urlFor(key));
  await open(page, urlFor(key), { wait, sweep });
  await assertProductPage(page);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' });
  await markFixed(page);
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
  Object.assign(c, { page: current, run, url: URLS[current] && urlFor(current), read: new Date().toISOString().slice(0, 10) }, meta);
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
        const shot = await crop(page, (opts.cropLoc || loc).filter({ visible: true }).first(), `${key}-${state}`, opts.pad ?? 8);
        file = shot.file;
        s.cropScale = shot.scale; // 2x normally, 1x when the crop was too large to keep at full scale
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
      } else via = via || opts.via || 'at rest';
      if (st === 'focus-visible' && via === 'focus failed') {
        // kbFocus could not land keyboard focus on the element: record the
        // failure instead of measuring the untouched control as a captured
        // focus, and drop any crop a previous run saved for this state
        const prev = out.components[key].states[st];
        if (prev && prev.crop) fs.rmSync(path.join(REF, prev.crop), { force: true });
        out.components[key].states[st] = { error: 'keyboard focus did not reach the element', via };
        log('  !', key, st, 'focus failed');
      } else {
        await measure(key, st, loc, { ...opts, via });
      }
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
// preferring an interactive tag or a cursor:pointer box. airbnb.com renders
// its tabs, chips and map price pills as styled divs, so role selectors alone
// miss them.
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
    // climb to the clickable parent when the match is a bare label inside it
    // (the header tabs are icon+label, the smallest text match is the label)
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

// Tags the listing-card CONTAINER around a stretched /rooms/ link: the anchor
// airbnb draws has no children, so the card is the smallest ancestor holding
// an <img> and a price line.
async function tagCard(name) {
  return page.evaluate((n) => {
    const a = [...document.querySelectorAll('a[href*="/rooms/"]')].find((x) => { const r = x.getBoundingClientRect(); return r.width > 150 && r.width < 600 && r.top > 100; });
    if (!a) return false;
    let el = a;
    for (let i = 0; i < 8 && el.parentElement; i++) {
      el = el.parentElement;
      const t = (el.innerText || '');
      if (el.querySelector('img') && /SGD|\$\d/.test(t) && t.length < 600) break;
    }
    el.setAttribute('data-m', n);
    return true;
  }, name).catch(() => false);
}

// ---------- groups ----------
const G = {
  shell: 'Header and navigation', searchbar: 'Search bar', home: 'Home galleries',
  search: 'Search results', room: 'Room page', help: 'Help Centre', host: 'Host landing',
  mobile: 'Mobile (390 wide)',
};

// ---------- home ----------

async function home() {
  await newPage('home', { sweep: 'keep' });
  await sweepOverlays(page);
  // signed-out home sometimes lands with the search sheet already expanded
  // (its "Where" coachmark), which unmounts the category tab rail. Esc
  // collapses it back to the pill + tabs — a local toggle, not a submission.
  await page.keyboard.press('Escape').catch(() => {});
  await page.waitForTimeout(1200);
  await markFixed(page);
  const g = G.shell;

  // The header: fixed top bar with the logo, category tabs and the user controls.
  const hdr = await tag('header', () => {
    const cands = [...document.querySelectorAll('header, [role=banner], body > div')].filter((e) => {
      const cs = getComputedStyle(e), r = e.getBoundingClientRect();
      return r.top <= 4 && r.width > innerWidth * 0.8 && r.height > 40 && r.height < 300 && /Become a host/.test(e.innerText || '');
    });
    return cands.sort((a, b) => a.getBoundingClientRect().height - b.getBoundingClientRect().height)[0] || null;
  });
  if (hdr) {
    await S('header', q('[data-m="header"]'), ['default'], { group: g, title: 'Header', desc: 'The fixed top bar: the Bélo logo, the category tabs (All, Homes, Experiences, Services) with their icons, "Become a host", the language globe and the profile menu. The search pill sits under it.', sel: 'the fixed top bar holding the logo, tabs and user controls' }, { noScroll: true, pad: 4 });
    if (await tagEl('hostlink', '^Become a host$', '[data-m="header"]'))
      await S('header-host-link', q('[data-m="hostlink"]'), B4, { group: g, title: 'Become a host link', desc: 'The host entry point in the header. Measured and focused, never followed.', sel: 'header "Become a host"' }, { noScroll: true });
    // The globe language button. Only a control that names language/region
    // counts: a generic "first small icon-only button" guess once picked the
    // Search submit, so a miss here means the component is missing this run.
    const globe = await tag('globe', () => {
      const h = document.querySelector('[data-m="header"]') || document;
      return [...h.querySelectorAll('button, a, [role=button], [tabindex], [aria-label], [title]')].find((e) => {
        const al = `${e.getAttribute('aria-label') || ''} ${e.getAttribute('title') || ''}`;
        return /language|region|locale|translate|langue|sprache|idioma| lingua/i.test(al) && e.getBoundingClientRect().width < 80;
      }) || null;
    });
    if (globe) await S('header-globe', q('[data-m="globe"]'), B3, { group: g, title: 'Language button', desc: 'The globe icon button that opens the language/region sheet. Hovered and focused only.', sel: 'the icon-only globe button in the header' }, { noScroll: true });
    const menu = await tag('menu', () => document.querySelector('button[aria-label*="navigation menu" i], button[aria-label*="Log in or sign up" i]'));
    if (menu) await S('header-menu', q('[data-m="menu"]'), B4, { group: g, title: 'Profile menu button', desc: 'The account buttons rightmost in the header (navigation menu and Log in or sign up). Pressed state is forced, not clicked: the menu leads to sign-up.', sel: 'the menu button rightmost in the header' }, { noScroll: true });
    // The active category tab and one resting tab (icon + label, the whole
    // clickable cell — the label alone is a nested span).
    const tabTag = (name, text) => tag(name, (text) => {
      const h = document.querySelector('[data-m="header"]') || document;
      // the label is a bare span; the cell is the smallest ancestor that also
      // holds the tab's icon (an svg) and still reads only the tab name
      const same = (t) => { t = (t || '').trim().replace(/\s+/g, ' '); return t === text || t === text + ' ' + text; };
      const band = (e) => { const r = e.getBoundingClientRect(); return r.width > 20 && r.top >= 0 && r.top < 300; };
      // the tabs are anchors with role=tab and doubled text (visible + sr-only)
      const cell = [...document.querySelectorAll('[role=tab]')].find((e) => same(e.innerText) && band(e));
      if (cell) return cell;
      // fallback: find the label span, then climb to the smallest ancestor that
      // still reads only the tab name and holds the tab's icon (an svg)
      const label = [...document.querySelectorAll('span,div,label,a')].filter((e) => same(e.innerText) && band(e)).sort((a, b) => (a.innerText || '').length - (b.innerText || '').length)[0];
      if (!label) return null;
      let n = label;
      for (let i = 0; i < 6 && n.parentElement; i++) {
        const p = n.parentElement;
        if (!same(p.innerText)) break;
        n = p;
        if (n.querySelector('svg')) break;
      }
      return n;
    }, text);
    if (await tabTag('tab0', 'Homes'))
      await S('tab-active', q('[data-m="tab0"]'), B4, { group: g, title: 'Category tab (active)', desc: 'A category tab in the header (Homes / Experiences / Services), the current one underlined.', sel: 'header tab "Homes"' }, { noScroll: true });
    if (await tabTag('tab1', 'Experiences'))
      await S('tab', q('[data-m="tab1"]'), B4, { group: g, title: 'Category tab', desc: 'A resting category tab. Pressed is forced: a real click would navigate.', sel: 'header tab "Experiences"' }, { noScroll: true });
  }

  const s = G.searchbar;
  // The search bar: the big white pill under the header with Where / When / Who
  // segments and the pink submit button.
  const bar = await tag('searchbar', () => {
    const w = [...document.querySelectorAll('body *')].find((e) => (e.innerText || '').trim() === 'Where' && getComputedStyle(e).cursor === 'pointer' && e.getBoundingClientRect().width > 100);
    if (!w) return null;
    let n = w;
    for (let i = 0; i < 8 && n.parentElement; i++) { n = n.parentElement; const r = n.getBoundingClientRect(); if (/Add guests/.test(n.innerText || '') && r.width > 500 && r.width < innerWidth - 100 && r.height < 120) return n; }
    return w.parentElement;
  });
  if (bar) {
    await S('search-bar', q('[data-m="searchbar"]'), ['default', 'hover'], { group: s, title: 'Search bar', desc: 'The big white pill: Where, When and Who segments with hairline dividers and the pink gradient submit button. Hovering a segment greys it.', sel: 'the pill holding the Where/When/Who segments' }, { noScroll: true });
    if (await tagEl('seg', '^Where$', '[data-m="searchbar"]'))
      await S('search-segment', q('[data-m="seg"]'), B4, { group: s, title: 'Search segment', desc: 'One labelled segment of the search pill (Where / When / Who): a label line over a placeholder line. Pressed is forced, never submitted.', sel: 'the "Where" segment' }, { noScroll: true });
    // The pink submit button: the magnifier/"Search" pill at the bar's right end.
    const sub = await tag('submit', () => document.querySelector('button[aria-label="Search"], button[type=submit]'));
    if (sub)
      await S('search-submit', q('[data-m="submit"]'), B4, { group: s, title: 'Search submit button', desc: 'The pink gradient round button with the magnifier (icon only at rest, icon + "Search" when the bar is expanded). Pressed is forced: a real press runs the search.', sel: 'the pink button inside the search bar' }, { noScroll: true });
    // The expanded panel the Where segment opens (local toggle, no submit).
    const whereEl = await tag('where', () => [...document.querySelectorAll('body *')].find((e) => (e.innerText || '').trim() === 'Where' && getComputedStyle(e).cursor === 'pointer' && e.getBoundingClientRect().width > 100));
    if (whereEl) {
      await q('[data-m="where"]').first().evaluate((el) => el.click()).catch(() => {});
      await page.waitForTimeout(1500);
      const panel = await tag('searchpanel', () => {
        // smallest element that names the suggestion list, climbed to the white
        // rounded panel that holds it (shadow may come from a ::before, so the
        // check is radius + size, not boxShadow)
        const m = [...document.querySelectorAll('body *')].filter((e) => {
          const t = (e.innerText || '').trim();
          return /Suggested destinations|Search by region/.test(t) && t.length < 3000 && e.getBoundingClientRect().width > 200;
        }).sort((a, b) => (a.innerText || '').length - (b.innerText || '').length)[0];
        if (!m) return null;
        let n = m;
        for (let i = 0; i < 8 && n.parentElement; i++) { n = n.parentElement; const r = n.getBoundingClientRect(); if (r.width > 350 && r.height > 250) return n; }
        return m;
      });
      if (panel) await S('search-panel-open', q('[data-m="searchpanel"]'), ['open'], { group: s, title: 'Search panel (open)', desc: 'The suggestion panel the Where segment opens ("Suggested destinations": Nearby and city rows with pictograms). Opened by clicking the segment, a local UI toggle; nothing was searched.', sel: 'the panel under the expanded search bar' }, { noScroll: true, via: 'clicked the Where segment' });
      await page.keyboard.press('Escape').catch(() => {});
      await page.mouse.click(700, 820).catch(() => {});
      await page.waitForTimeout(600);
    }
  }

  const h = G.home;
  // A carousel section: title row with a chevron, then the card rail.
  if (await tagEl('sectitle', '^Places to stay in|^Available in', null))
    await S('section-title', q('[data-m="sectitle"]'), ['default', 'hover'], { group: h, title: 'Section title', desc: 'A gallery section head ("Places to stay in Busan") with a chevron that follows to the search page.', sel: 'a gallery section title row' });
  // The first listing card in a rail (the anchor is a stretched link; tag the container).
  const card = await tagCard('card');
  if (card) {
    await S('listing-card', q('[data-m="card"]'), ['default', 'hover'], { group: h, title: 'Listing card', desc: 'A home card in a rail: a 12px-radius photo with the Guest favourite badge and wishlist heart over it, then the title, price and star rating rows.', sel: 'the first listing-card container in the rail' });
    // The badge: the white "Guest favourite" pill over the photo (the first
    // card may not carry one, so the tag is taken wherever a badge shows).
    const badge = await tag('badge', () => {
      const m = [...document.querySelectorAll('body *')].filter((e) => /Guest favourite|Superhost/.test((e.innerText || '').trim()) && (e.innerText || '').trim().length < 40 && e.getBoundingClientRect().width > 10).sort((a, b) => (a.innerText || '').length - (b.innerText || '').length)[0];
      if (!m) return null;
      let n = m;
      for (let i = 0; i < 5 && n.parentElement; i++) { const p = n.parentElement, r = p.getBoundingClientRect(); if (r.width > 200 || r.height > 60 || !/Guest favourite|Superhost/.test(p.innerText || '')) break; n = p; }
      return n;
    });
    if (badge) await S('card-badge', q('[data-m="badge"]'), ['default'], { group: h, title: 'Guest favourite badge', desc: 'The white pill over the card photo (Guest favourite / Superhost).', sel: 'the badge pill over a card photo' });
    // The heart: the svg toggle top-right of the photo (aria-label names wishlist).
    const heart = await tag('heart', () => {
      const c = document.querySelector('[data-m="card"]');
      return c && [...c.querySelectorAll('button, [role=button], [aria-label]')].find((e) => { const r = e.getBoundingClientRect(); return r.width < 70 && r.height < 70 && r.top < c.getBoundingClientRect().top + 80 && e.querySelector('svg'); }) || null;
    });
    if (heart) await S('card-heart', q('[data-m="heart"]'), B4, { group: h, title: 'Wishlist heart', desc: 'The heart toggle over the card photo. Pressed is forced: a real tap opens the sign-up sheet signed out.', sel: 'the heart button inside the card' });
    // The rating row: star svg + number.
    if (await tagEl('rating', '\\d\\.\\d', '[data-m="card"]'))
      await S('card-rating', q('[data-m="rating"]'), ['default'], { group: h, title: 'Rating row', desc: 'The star and average under the card title.', sel: 'the rating text inside the card' }, { crop: false });
  }
  // The rail next arrow: a small round white button at a rail's right edge.
  const arrow = await tag('arrow', () => {
    return [...document.querySelectorAll('button, [role=button]')].find((e) => { const r = e.getBoundingClientRect(); return r.width > 24 && r.width < 50 && r.height > 24 && r.height < 50 && r.left > innerWidth - 160 && e.querySelector('svg') && r.top > 150; }) || null;
  });
  if (arrow) await S('rail-arrow', q('[data-m="arrow"]'), B4, { group: h, title: 'Carousel arrow', desc: 'The small white round button that pages a card rail. Hovered and focused only; pressing pages the rail.', sel: 'the next arrow on a card rail' });
}

// ---------- search results ----------

async function search() {
  await newPage('search', { sweep: 'keep' });
  await sweepOverlays(page);
  await markFixed(page);
  const g = G.search;

  // The compact search pill: "Homes in Tokyo · Any week · Add guests" + the pink icon button.
  const pill = await tag('minibar', () => {
    const cands = [...document.querySelectorAll('body *')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.top < 120 && r.width > 250 && r.width < 700 && r.height > 30 && r.height < 80 && /Homes in Tokyo|Any week|Add guests/.test(e.innerText || '');
    });
    return cands.sort((a, b) => (a.innerText || '').length - (b.innerText || '').length)[0] || null;
  });
  if (pill) await S('mini-search', q('[data-m="minibar"]'), ['default', 'hover'], { group: G.searchbar, title: 'Mini search pill', desc: 'The collapsed search pill the results page shows: three segments and the small pink submit. Measured, never opened.', sel: 'the compact search bar in the header' }, { noScroll: true });
  // The filters row: the Filters button then the pill chips.
  if (await tagEl('filters', '^Filters$', null))
    await S('filters-button', q('[data-m="filters"]'), B4, { group: g, title: 'Filters button', desc: 'The sliders-icon button that opens the filters sheet. Pressed is forced; opening the sheet is a toggle but the row also navigates.', sel: 'the "Filters" button left of the chip row' }, { noScroll: true });
  if (await tagEl('chip', '^(Type of place|Price|Kitchen|Wifi|Heating)$', null))
    await S('filter-chip', q('[data-m="chip"]'), B4, { group: g, title: 'Filter chip', desc: 'One pill in the quick-filter row (Type of place, Price, Kitchen …). Pressed is forced.', sel: 'a filter pill in the row under the header' }, { noScroll: true });
  // A results card (the anchor is a stretched link; tag the container).
  const card = await tagCard('card');
  if (card) {
    await S('result-card', q('[data-m="card"]'), ['default', 'hover'], { group: g, title: 'Result card', desc: 'A listing card in the results grid: photo with badge and heart, then title, distance line, bed rows, dates, price and Free cancellation.', sel: 'the first listing card in the results grid' });
    if (await tagEl('badge', 'Guest favourite|Superhost', '[data-m="card"]'))
      await S('result-badge', q('[data-m="badge"]'), ['default'], { group: g, title: 'Listing badge', desc: 'The white pill over the photo (Guest favourite / Superhost).', sel: 'the badge pill inside the result card' });
    const heart = await tag('heart', () => {
      const c = document.querySelector('[data-m="card"]');
      return c && [...c.querySelectorAll('button, [role=button], [aria-label]')].find((e) => { const r = e.getBoundingClientRect(); return r.width < 70 && r.height < 70 && r.top < c.getBoundingClientRect().top + 80 && e.querySelector('svg'); }) || null;
    });
    if (heart) await S('result-heart', q('[data-m="heart"]'), B4, { group: g, title: 'Wishlist heart', desc: 'The heart over the photo. Pressed is forced: signed out it opens the sign-up sheet.', sel: 'the heart button on the result card' });
  }
  // The "Prices include all fees" tag with the pink price-tag icon.
  if (await tagEl('feestag', '^Prices include all fees$', null))
    await S('fees-tag', q('[data-m="feestag"]'), ['default', 'hover'], { group: g, title: 'All-fees tag', desc: 'The inline tag over the results grid explaining the total price display.', sel: 'the "Prices include all fees" row' });
  // Map price pills: the dark/white price bubbles pinned on the Google map.
  const mappill = await tag('mappill', () => {
    const b = [...document.querySelectorAll('body *')].filter((e) => {
      const t = (e.innerText || '').trim(); const r = e.getBoundingClientRect();
      return /^[\$S0-9,\. ]+SGD$|^\$[\d,]+$/.test(t) && t.length < 20 && r.width > 40 && r.width < 160 && r.height > 20 && r.height < 60 && r.left > innerWidth * 0.45;
    });
    return b.sort((a, b) => (a.innerText || '').length - (b.innerText || '').length)[0] || null;
  });
  if (mappill) await S('map-price-pill', q('[data-m="mappill"]'), ['default', 'hover'], { group: g, title: 'Map price pill', desc: 'A price bubble pinned on the map; hover paints it rausch pink. The map itself is a Google embed and not part of the system.', sel: 'a price marker on the results map' }, { noScroll: true });
}

// ---------- room detail ----------

async function room() {
  await newPage('room', { sweep: 'keep' });
  await sweepOverlays(page);
  await markFixed(page);
  const g = G.room;

  await S('room-title', q('h1').first(), ['default'], { group: g, title: 'Room title', desc: 'The listing headline under the header.', sel: 'main h1' }, { noScroll: true });
  if (await tagEl('sharebtn', '^Share$', null))
    await S('room-share', q('[data-m="sharebtn"]'), B4, { group: g, title: 'Share button', desc: 'The underlined Share action beside Save. Pressed is forced.', sel: 'the "Share" button by the title' }, { noScroll: true });
  if (await tagEl('savebtn', '^Save$', null))
    await S('room-save', q('[data-m="savebtn"]'), B4, { group: g, title: 'Save button', desc: 'The heart+Save action. Pressed is forced: signed out, a real press opens the sign-up sheet.', sel: 'the "Save" button by the title' }, { noScroll: true });
  // The photo collage.
  const grid = await tag('photogrid', () => {
    const cands = [...document.querySelectorAll('body *')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 700 && r.height > 300 && r.top < 400 && e.querySelectorAll('img').length >= 4;
    });
    return cands.sort((a, b) => a.getBoundingClientRect().height - b.getBoundingClientRect().height)[0] || null;
  });
  if (grid) await S('photo-grid', q('[data-m="photogrid"]'), ['default'], { group: g, title: 'Photo collage', desc: 'The 5-photo mosaic: one large tile left, a 2x2 grid right, 12px radius.', sel: 'the photo mosaic under the title' }, { noScroll: true });
  if (await tagEl('allphotos', '^Show all photos$', null))
    await S('show-photos', q('[data-m="allphotos"]'), B4, { group: g, title: 'Show all photos button', desc: 'The white pill bottom-right of the collage. Pressed is forced: it opens the photo viewer.', sel: 'the "Show all photos" pill' }, { noScroll: true });
  // The subtitle row: "Entire home in Shinjuku, Japan / 8 guests · ...".
  if (await tagEl('subtitle', '^(Entire|Private room|Room|Rental unit)', null))
    await S('room-subtitle', q('[data-m="subtitle"]'), ['default'], { group: g, title: 'Listing subtitle', desc: 'The "Entire rental unit in …" line and the guests/bedrooms/beds row.', sel: 'the subtitle under the collage' });
  // The guest favourite plaque: laurels + "One of the most loved homes" + rating + reviews.
  const plaque = await tag('plaque', () => {
    const cands = [...document.querySelectorAll('body *')].filter((e) => /most loved homes|Guest favourite/.test(e.innerText || '') && (e.innerText || '').length < 300);
    const m = cands.sort((a, b) => (a.innerText || '').length - (b.innerText || '').length)[0];
    if (!m) return null;
    // m can be the bare "Guest favourite" label; the plaque is the smallest
    // ancestor that holds the whole strip — the loved-homes line and the
    // rating digits beside it
    let n = m;
    for (let i = 0; i < 8 && n.parentElement; i++) {
      const p = n.parentElement, t = p.innerText || '';
      if (t.length > 500 || !/most loved homes|Guest favourite/i.test(t)) break;
      n = p;
      if (/most loved homes/i.test(t) && /\d/.test(t)) break;
    }
    return n;
  });
  if (plaque) await S('guest-plaque', q('[data-m="plaque"]'), ['default'], { group: g, title: 'Guest favourite plaque', desc: 'The laurel-bordered strip: "Guest favourite / One of the most loved homes on Airbnb" with the rating and review count.', sel: 'the laurel plaque under the subtitle' });
  // The reservation card.
  const res = await tag('rescard', () => {
    const cands = [...document.querySelectorAll('body *')].filter((e) => {
      const r = e.getBoundingClientRect();
      return /Add dates for prices|CHECK-IN|CHECKOUT|GUESTS/.test(e.innerText || '') && r.width > 300 && r.width < 600 && r.height > 200;
    });
    return cands.sort((a, b) => (a.innerText || '').length - (b.innerText || '').length)[0] || null;
  });
  if (res) {
    await S('reserve-card', q('[data-m="rescard"]'), ['default'], { group: g, title: 'Reservation card', desc: 'The booking card pinned right: "Add dates for prices", the CHECK-IN/CHECK-OUT/GUESTS field grid. Nothing was booked.', sel: 'the card with the date and guest fields' });
    // The CHECK-IN field cell. The label alone is a 12px line, so the probe
    // climbs to the smallest ancestor that also holds the value line without
    // swallowing the CHECKOUT / GUESTS siblings.
    const gfield = await tag('gfield', () => {
      const card = document.querySelector('[data-m="rescard"]');
      if (!card) return null;
      const lab = [...card.querySelectorAll('*')].filter((e) => {
        const t = (e.innerText || '').trim();
        return /^(CHECK-IN|Add date)$/i.test(t) && t.length < 20;
      }).sort((a, b) => (a.innerText || '').length - (b.innerText || '').length)[0];
      if (!lab) return null;
      let n = lab;
      for (let i = 0; i < 8 && n.parentElement; i++) {
        const p = n.parentElement, t = (p.innerText || '').trim(), r = p.getBoundingClientRect();
        if (/CHECKOUT|CHECK-OUT|GUESTS|TRAVELLERS/i.test(t)) break;
        n = p;
        if (r.height > 30 && t.length > (lab.innerText || '').trim().length) break;
      }
      return n;
    });
    if (gfield)
      await S('reserve-field', q('[data-m="gfield"]'), ['default', 'hover'], { group: g, title: 'Date field', desc: 'A labelled field cell in the booking grid (CHECK-IN / CHECKOUT / GUESTS).', sel: 'the CHECK-IN field cell' });
  }
  // The promo strip ("Get $25 SGD off your getaway" + Claim) — measured, never pressed.
  if (await tagEl('claim', '^Claim$|^Terms apply', null)) {
    const promo = await tag('promo', () => {
      const c = document.querySelector('[data-m="claim"]');
      let n = c;
      for (let i = 0; i < 6 && n && n.parentElement; i++) { n = n.parentElement; if (/getaway|off your/.test(n.innerText || '') && n.getBoundingClientRect().width > 300) return n; }
      return c;
    });
    if (promo) await S('promo-strip', q('[data-m="promo"]'), ['default'], { group: g, title: 'Promo strip', desc: 'The discount banner ("Get $25 SGD off your getaway") with the outlined Claim button. Measured, never pressed.', sel: 'the promo banner near the top of the listing' });
    if (await tagEl('claimbtn', '^Claim$', '[data-m="promo"]'))
      await S('promo-claim', q('[data-m="claimbtn"]'), B4, { group: g, title: 'Claim button', desc: 'The outlined Claim action on the promo strip. Pressed is forced: claiming needs an account.', sel: 'the Claim button on the promo strip' });
  }
  // The host row: "Hosted by" + avatar.
  if (await tagEl('hostrow', '^Hosted by', null))
    await S('host-row', q('[data-m="hostrow"]'), ['default'], { group: g, title: 'Host row', desc: 'The "Hosted by" row with the circular avatar.', sel: 'the Hosted-by row under the plaque' });
}

// ---------- help centre ----------

async function help() {
  await newPage('help');
  const g = G.help;
  await S('help-title', q('h1').first(), ['default'], { group: g, title: 'Help title', desc: '"Hi, how can we help?" — the Help Centre headline.', sel: 'h1' }, { noScroll: true });
  const inp = await tag('helpsearch', () => document.querySelector('input[type=text], input[type=search], input[placeholder]'));
  if (inp) await S('help-search', q('[data-m="helpsearch"]'), ['default', 'focus-visible'], { group: g, title: 'Help search field', desc: 'The search field under the headline (the icon + placeholder). Focused only; nothing was searched.', sel: 'the search input on the help home' });
  // A help tile/card in the topic grid: a link into /help/ content. The size
  // window alone once picked the "Log in or sign up" button, so the probe
  // requires a help href and rejects account and nav text.
  const tile = await tag('helptile', () => {
    const cands = [...document.querySelectorAll('a[href]')].filter((e) => {
      const r = e.getBoundingClientRect(); const t = (e.innerText || '').trim();
      const href = e.getAttribute('href') || '';
      return r.width > 200 && r.width < 700 && r.height > 40 && r.height < 300 && r.top > 300 && t.length > 10 && t.length < 120
        && /\/help\//i.test(href) && !/log in|sign up|menu|search/i.test(t);
    });
    return cands.sort((a, b) => a.getBoundingClientRect().top - b.getBoundingClientRect().top)[0] || null;
  });
  if (tile) await S('help-tile', q('[data-m="helptile"]'), B4, { group: g, title: 'Help tile', desc: 'A topic card in the help grid. Pressed is forced: a real click navigates.', sel: 'a topic card in the help grid' });
  // A footer quick link — the help page scrolls normally, so the footer is a
  // stable target here (the home page's lazy rails made it crash the run).
  if (await tagEl('footlink', '^(kyoto|milan|amsterdam|dallas|whistler|hosting|support|company)', null))
    await S('footer-link', q('[data-m="footlink"]'), B4, { group: g, title: 'Footer link', desc: 'A quick link in the footer grid. Pressed is forced: a real click navigates.', sel: 'a link in the footer' });
}

// ---------- host landing ----------

async function host() {
  await newPage('host', { sweep: 'keep' });
  await sweepOverlays(page);
  await markFixed(page);
  const g = G.host;
  await S('host-hero', q('h1').first(), ['default'], { group: g, title: 'Host headline', desc: '"Your home could make money on Airbnb".', sel: 'h1' }, { noScroll: true });
  if (await tagEl('getstart', '^Get started$', null))
    await S('host-cta', q('[data-m="getstart"]'), B4, { group: g, title: 'Get started button', desc: 'The rausch CTA in the nav and on the page. Pressed is forced: it starts the host sign-up flow.', sel: 'a "Get started" button' }, { noScroll: true });
  // The earnings estimate card (map region input + slider) — measured at rest.
  const est = await tag('estimator', () => {
    const cands = [...document.querySelectorAll('body *')].filter((e) => {
      const r = e.getBoundingClientRect();
      return /per night|per month|earnings|night/i.test(e.innerText || '') && r.width > 300 && r.width < 800 && r.height > 150 && (e.innerText || '').length < 800;
    });
    return cands.sort((a, b) => (a.innerText || '').length - (b.innerText || '').length)[0] || null;
  });
  if (est) await S('estimator-card', q('[data-m="estimator"]'), ['default'], { group: g, title: 'Earnings estimator', desc: 'The interactive earnings card (location field, guest slider, monthly total). Measured at rest; nothing was submitted.', sel: 'the earnings estimate card on the host page' });
}

// ---------- mobile ----------

async function mobile() {
  await newPage('mobile', { mobile: true, sweep: 'keep' });
  await sweepOverlays(page);
  await markFixed(page);
  const g = G.mobile;
  // The mobile search pill near the top.
  const pill = await tag('mpill', () => {
    const cands = [...document.querySelectorAll('body *')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.top < 160 && r.width > 200 && r.height > 30 && r.height < 80 && /Where|Any|Search|Add/.test(e.innerText || '') && (e.innerText || '').length < 100;
    });
    return cands.sort((a, b) => (a.innerText || '').length - (b.innerText || '').length)[0] || null;
  });
  if (pill) await S('m-search-pill', q('[data-m="mpill"]'), ['default'], { group: g, title: 'Mobile search pill', desc: 'The compact search bar at the top of the mobile home.', sel: 'the search pill under the header' }, { noScroll: true });
  // A mobile listing card (container around the stretched link).
  const card = await tagCard('mcard');
  if (card) await S('m-listing-card', q('[data-m="mcard"]'), ['default'], { group: g, title: 'Mobile listing card', desc: 'A home card in the mobile rail: full-bleed photo, badge, heart, title, price.', sel: 'the first listing card' });
  // The bottom nav bar (Explore / Wishlists / Log in) if present.
  const nav = await tag('mnav', () => {
    const cands = [...document.querySelectorAll('nav, footer, [role=navigation], body *')].filter((e) => {
      const cs = getComputedStyle(e), r = e.getBoundingClientRect();
      return (cs.position === 'fixed' || cs.position === 'sticky') && r.bottom >= innerHeight - 4 && r.height > 40 && r.height < 120 && r.width > 300;
    });
    return cands[0] || null;
  });
  if (nav) await S('m-bottom-bar', q('[data-m="mnav"]'), ['default'], { group: g, title: 'Bottom bar', desc: 'The bar pinned at the foot of the mobile page (Explore / Wishlists / Log in, or the map button).', sel: 'the fixed bottom bar' }, { noScroll: true });
}

// ---------- run ----------

// Any component recorded for a page that this run never touched is stale
// evidence from an earlier capture (a probe that returned false, or a page
// that changed): flag it missing so it cannot read as a fresh measurement.
function sweepMissing(pageName) {
  for (const [k, c] of Object.entries(out.components)) {
    if (c.page === pageName && !touched.has(k) && !c.missing) {
      c.missing = true;
      log('  ! not found this run', k);
    }
  }
}

const ALL = { home, search, room, help, host, mobile };
const wanted = process.argv.slice(2);
const { browser } = await launch();
for (const name of process.argv.slice(2).length ? wanted : Object.keys(ALL)) {
  if (!ALL[name]) continue;
  run = name;
  // The room page needs its own fresh context after a detour to the results
  // page for the href.
  const mob = name === 'mobile';
  context = await browser.newContext({ viewport: { width: mob ? 390 : 1440, height: mob ? 844 : 900 }, deviceScaleFactor: mob ? 2 : 2, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US', reducedMotion: 'no-preference' });
  // bot check: recorded as a boundary, not bypassed (navigator.webdriver is left as Chromium sets it)
  if (name === 'room' && !roomHref) {
    const p = await context.newPage();
    await open(p, BASE + '/s/Tokyo--Japan/homes', { wait: 8000 });
    roomHref = await firstRoomHref(p);
    await p.close();
    log('room href', roomHref);
  }
  try {
    await ALL[name]();
    sweepMissing(name);
    if (out._meta.failed) delete out._meta.failed[name];
    save();
  } catch (e) {
    const msg = e.message.split('\n')[0].slice(0, 160);
    log('PAGE FAILED', name, msg);
    // record the failure against the page instead of silently refreshing the
    // shared date over its old components; untouched entries keep their own
    // per-component read dates
    (out._meta.failed ??= {})[name] = msg;
    save();
  }
  for (const p of context.pages()) await p.close().catch(() => {});
  await context.close();
}
await browser.close();
// missing report
const missing = Object.entries(out.components).filter(([, c]) => c.missing).map(([k]) => k);
const errors = Object.entries(out.components).flatMap(([k, c]) => Object.entries(c.states || {}).filter(([, s]) => s.error).map(([s]) => `${k}:${s}`));
const failedPages = Object.keys(out._meta.failed || {});
log('components:', touched.size, 'missing:', missing.length ? missing.join(', ') : 'none', 'errors:', errors.length ? errors.join(', ') : 'none', 'failed pages:', failedPages.length ? failedPages.join(', ') : 'none');
