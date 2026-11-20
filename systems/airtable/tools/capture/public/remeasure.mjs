// Gap-fill pass over raw/components-computed.json: re-measures only the
// components the first measure.mjs run missed or read wrongly, merging into
// the same file (no stale-drop: entries this script does not touch are kept).
// Companion to measure.mjs — same states, same helpers, same crop pipeline.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node remeasure.mjs [run ...]
//
// Runs: home platform platform-ai pricing contact-sales templates whatsnew
//       marketplace mobile. What each run adds:
//   home          hero-title (rect re-read in view), resource-card, carousel-control
//   platform      platform-title (rect re-read in view), nav-dropdown, nav-dropdown-link, platform-card, footer, stories-prev
//   platform-ai   platform-ai-card, faq-item, faq-item-open (the opened item, not the trigger)
//   pricing       plan-card, compare-table, compare-table-row, pricing-faq-item, pricing-faq-item-open
//   contact-sales select-field, select-field-open (the raised menu), submit-button, field-label
//   templates     template-card, filter-section, filter-section-open
//   whatsnew      whatsnew-title, whatsnew-item, whatsnew-filter
//   marketplace   market-card (the first pass read the whole extensions grid)
//   mobile        m-nav-sheet (a positioned drawer only; the footer nav is not the sheet)
// Deliberately still missing (probes find nothing on the live site):
//   filter-checkbox (the templates rail is a plain link list, no checkboxes),
//   checkbox (the contact-sales form has none), a home FAQ (the page has none).
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, open, closePromo, styleOf, crop, centre, markFixed, RAW } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => { fs.mkdirSync(RAW, { recursive: true }); fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n'); };

const URLS = {
  home: BASE + '/', platform: BASE + '/platform', 'platform-ai': BASE + '/platform/ai',
  pricing: BASE + '/pricing', 'contact-sales': BASE + '/contact-sales',
  templates: BASE + '/templates', whatsnew: BASE + '/whatsnew', marketplace: BASE + '/marketplace',
  mobile: BASE + '/',
};

let page, cdp, current, context, run;

async function newPage(key, { mobile = false, wait = 8000 } = {}) {
  current = key;
  page = await context.newPage();
  page.setDefaultTimeout(8000);
  cdp = await context.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  log('open', key, mobile ? '(mobile)' : '', URLS[key]);
  await open(page, URLS[key], { wait });
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

const NEVER = /^(send|submit|sign up|sign up for free|log in|try it now|book demo|book a demo|contact sales|get started|get started for free|create|generate|upload|start|start free trial|upgrade|subscribe|apply|accept all|reject all|manage cookies|privacy choices|cookie settings|request demo|get a demo|join|share|buy|purchase|claim|view all.*|see all.*|sync this data)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

function comp(key, meta) {
  const c = (out.components[key] ??= { states: {} });
  Object.assign(c, { page: current, run, url: URLS[current] }, meta);
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
    log('  ', key, state, s.rect.w + 'x' + s.rect.h);
  } catch (e) {
    c.states[state] = { error: String(e.message || e).slice(0, 200) };
    log('  !', key, state, String(e.message).slice(0, 120));
  }
}

async function S(key, target, list, meta = {}, opts = {}) {
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  delete out.components[key].missing;
  if (opts.open) {
    await reset();
    await opts.open();
    if (opts.openTarget) {
      // The open state is the expanded container or the popup, not the trigger:
      // an accordion answer lies outside the trigger's own box.
      const ok = await tag('open-' + key, opts.openTarget);
      if (!ok) {
        log('  ! did not open', key);
        for (const st of list) out.components[key].states[st] = { error: 'the toggle did not open the target' };
        return;
      }
      target = q(`[data-m="open-${key}"]`);
    }
  }
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
        // a state that did not receive keyboard focus is not a captured focus
        if (via === 'focus failed') throw new Error('keyboard focus did not land on the element');
      } else if (st === 'pressed') {
        undo = await forcePseudo((opts.pressLoc || loc).filter({ visible: true }).first(), ['active', 'hover']);
        via = 'CDP forcePseudoState :active:hover';
      } else via = via || opts.via || 'at rest';
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

// openTarget probes for S({open, openTarget}) — same as measure.mjs: the
// element that shows the opened state (the capture guide wants the whole
// popup, not the trigger), or null when the toggle did not open. tag()
// serializes the probe's source, so the trigger's data-m name is inlined.
const openItem = (tagName) => new Function(`
  const t = document.querySelector('[data-m="${tagName}"]');
  if (!t) return null;
  let opened = t.getAttribute('aria-expanded') === 'true' || !!t.closest('[aria-expanded="true"], details[open], [data-state="open"]');
  for (let n = t; !opened && n && n !== document.body; n = n.parentElement) opened = /(^|[^a-z])(is|has|show)(open|expanded)([^a-z]|$)/i.test(String(n.className));
  if (!opened) return null;
  let n = t;
  for (let i = 0; n.parentElement && i < 6; i++) {
    n = n.parentElement;
    const r = n.getBoundingClientRect();
    if (r.height > t.getBoundingClientRect().height + 20 && (n.innerText || '').replace(t.innerText || '', '').trim().length > 4) return n;
  }
  return null;
`);
const openMenu = (tagName) => new Function(`
  const t = document.querySelector('[data-m="${tagName}"]');
  if (!t) return null;
  const menus = [...document.querySelectorAll('[role=listbox], [class*="-menu" i], [class*="menuList" i], [class*="dropdown-menu" i], [id*="listbox" i]')].filter((e) => {
    const r = e.getBoundingClientRect();
    return r.width > 100 && r.height > 40 && (e.innerText || '').trim().length > 2;
  });
  const menu = menus.sort((a, b) => a.getBoundingClientRect().height - b.getBoundingClientRect().height)[0];
  if (!menu) return null;
  return menu; // the popup itself: a mounted menu overflows the field box, so cropping the field would clip it
`);

async function tag(name, probe) {
  return page.evaluate(([n, src]) => {
    const el = (new Function('return (' + src + ')')())();
    if (!el) return false;
    document.querySelectorAll(`[data-m="${n}"]`).forEach((o) => o.removeAttribute('data-m'));
    el.setAttribute('data-m', n);
    return true;
  }, [name, probe.toString()]).catch(() => false);
}

const G = {
  shell: 'Shell and navigation', home: 'Home', cards: 'Cards and indexes',
  platform: 'Platform pages', pricing: 'Pricing', contact: 'Contact sales form',
  overlay: 'Overlays', mobile: 'Mobile (390 wide)',
};
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

// ---------- home ----------
async function home() {
  await newPage('home');
  const g = G.home;
  // The first pass recorded the h1 with the page scrolled past it (y=-6646);
  // re-read it centred so the rect records where it actually sits.
  const h1 = await tag('h1', () => document.querySelector('h1'));
  if (h1) await S('hero-title', q('[data-m="h1"]'), ['default'], { group: g, title: 'Hero title', desc: 'The home h1 ("All your teams, all their workflows — connected in one workspace").', sel: 'h1' });
  // "Resources to inspire" linked cards near the bottom of the page.
  const res = await tag('rescard', () => {
    const cands = [...document.querySelectorAll('a')].filter((e) => {
      const r = e.getBoundingClientRect();
      const top = r.top + scrollY;
      return r.width > 240 && r.height > 60 && top > 1500 && e.querySelector('img, h2, h3, [class*="title" i]') && /breakthrough|guide|in action|watch|read/i.test(e.innerText || '');
    });
    return cands.sort((a, b) => a.getBoundingClientRect().top + scrollY - (b.getBoundingClientRect().top + scrollY))[0] || null;
  });
  if (res) await S('resource-card', q('[data-m="rescard"]'), ['default', 'hover'], { group: g, title: 'Resource card', desc: 'A card in the "Resources to inspire" row (Builders & Breakthroughs).', sel: 'a resource card' });
  // The feature carousel's round pause/next controls.
  const dot = await tag('cdot', () => {
    const cands = [...document.querySelectorAll('[role=tab], button')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width >= 6 && r.width <= 60 && r.height >= 6 && r.height <= 60 && r.left >= 0 && /pause|next|previous|slide|autoplay|animation/i.test((e.getAttribute('aria-label') || '') + ' ' + (e.innerText || ''));
    });
    return cands[0] || null;
  });
  if (dot) await S('carousel-control', q('[data-m="cdot"]'), B4, { group: g, title: 'Carousel control', desc: 'A round control of the home feature carousel (the pause or next button).', sel: 'a carousel control button' });
  await page.close();
}

// ---------- platform ----------
async function platform() {
  await newPage('platform');
  const g = G.shell;
  // Same offscreen-rect repair as the home h1.
  const h1 = await tag('h1', () => document.querySelector('h1'));
  if (h1) await S('platform-title', q('[data-m="h1"]'), ['default'], { group: G.platform, title: 'Platform page title', desc: 'The h1 on https://www.airtable.com/platform.', sel: 'h1' });
  // The nav drawer, opened by clicking the Platform trigger (a local disclosure).
  const trig = page.locator('header button, nav button').filter({ hasText: /^platform$/i }).filter({ visible: true }).first();
  if (await trig.count()) {
    await trig.click().catch(() => {});
    await page.waitForTimeout(2200);
    const menu = await tag('submenu', () => {
      // The whole open drawer: the nav element marked drawerIsActive; its
      // nested promo panes share the same class without the active flag.
      const active = [...document.querySelectorAll('nav[class*="drawerIsActive" i], [class*="navDrawerMenu" i][class*="drawerIsActive" i]')].filter((e) => {
        const r = e.getBoundingClientRect();
        return r.left >= -10 && r.width > 150 && r.height > 80 && e.querySelector('a');
      });
      if (active.length) return active.sort((a, b) => a.querySelectorAll('*').length - b.querySelectorAll('*').length)[0];
      const cands = [...document.querySelectorAll('[class*="navDrawer" i], [role=menu], [class*="drawer" i]')].filter((e) => {
        const r = e.getBoundingClientRect();
        return r.left >= -10 && r.width > 150 && r.height > 80 && e.querySelector('a') && (e.innerText || '').trim().length > 10;
      });
      return cands.sort((a, b) => a.getBoundingClientRect().width * a.getBoundingClientRect().height - b.getBoundingClientRect().width * b.getBoundingClientRect().height)[0] || null;
    });
    if (menu) await S('nav-dropdown', q('[data-m="submenu"]'), ['default'], { group: g, title: 'Nav drawer', desc: 'The full-height drawer the Platform trigger opens (product areas and a promo card). Shown click-open; a local disclosure.', sel: 'the open navDrawerMenu' }, { noScroll: true, via: 'clicked the Platform trigger' });
    // an item inside the drawer
    const item = await tag('sublink', () => [...document.querySelectorAll('[data-m="submenu"] a')].find((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 100 && r.height > 20 && (e.innerText || '').trim().length > 3;
    }) || null);
    if (item) await S('nav-dropdown-link', q('[data-m="sublink"]'), ['default', 'hover'], { group: g, title: 'Drawer link', desc: 'An item in the open nav drawer (Airtable Platform).', sel: 'a link inside navDrawerMenu' }, { noScroll: true });
    await page.keyboard.press('Escape').catch(() => {});
    await page.waitForTimeout(700);
  }
  // A real linked card ("Ways to start building with agents").
  const card = await tag('pcard', () => {
    const cands = [...document.querySelectorAll('a[class*="card" i], [class*="cardLink" i], a, article')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 300 && r.height > 100 && r.left >= 0 && (e.querySelector('h2, h3, img, video')) && !e.closest('[class*="carousel" i], [class*="slick" i], [class*="slider" i], [role=listbox]');
    });
    return cands.sort((a, b) => a.getBoundingClientRect().top - b.getBoundingClientRect().top)[0] || null;
  });
  if (card) await S('platform-card', q('[data-m="pcard"]'), ['default', 'hover'], { group: G.platform, title: 'Platform feature card', desc: 'A linked card on /platform (a "Ways to start building with agents" tile).', sel: 'a cardLink' });
  // The customer-stories carousel: the arrows carry the *_arrowButton class
  // ("Previous story" / "Next story"). Scroll the carousel in first; the prev
  // arrow only shows once the carousel leaves its first slide.
  const next = await tag('snext', () => [...document.querySelectorAll('button[class*="arrowButton" i], button')].find((e) => /next/i.test((e.getAttribute('aria-label') || '') + ' ' + (e.innerText || ''))) || null);
  if (next) {
    await centre(q('[data-m="snext"]').filter({ visible: true }).first());
    const pv = await tag('sprev', () => [...document.querySelectorAll('button[class*="arrowButton" i]')].find((e) => /previous|prev/i.test((e.getAttribute('aria-label') || '') + ' ' + (e.innerText || ''))) || null);
    if (pv && !(await q('[data-m="sprev"]').filter({ visible: true }).first().count())) {
      await q('[data-m="snext"]').filter({ visible: true }).first().click({ timeout: 4000 }).catch(() => {});
      await page.waitForTimeout(1400);
    }
  }
  const prev = await tag('sprev', () => [...document.querySelectorAll('button[class*="arrowButton" i]')].find((e) => /previous|prev/i.test((e.getAttribute('aria-label') || '') + ' ' + (e.innerText || ''))) || null);
  if (prev) await S('stories-prev', q('[data-m="sprev"]'), B4, { group: G.platform, title: 'Stories previous button', desc: 'The previous-arrow of the customer-stories carousel, shown after the carousel leaves its first slide.', sel: 'the prev arrowButton' });
  // The real site footer: link columns + legal row (the first pass read a
  // carousel's control bar, which also carries a footer class name).
  const foot = await tag('foot', () => {
    const cands = [...document.querySelectorAll('footer, [class*="footer" i], [class*="siteFooter" i]')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 500 && r.height > 80 && /privacy|terms|careers|security|accessibility/i.test(e.innerText || '') && e.querySelectorAll('a').length >= 5;
    });
    return cands.sort((a, b) => a.innerText.length - b.innerText.length)[0] || null;
  });
  if (foot) await S('footer', q('[data-m="foot"]'), ['default'], { group: g, title: 'Footer', desc: 'The site footer: link columns (Platform, Solutions, Resources, Learn, Company), social icons, legal row.', sel: 'footer' });
  await page.close();
}

// ---------- platform-ai ----------
async function platformAi() {
  await newPage('platform-ai');
  const g = G.platform;
  // A card of the "Add AI to your workflows" grid (li *_cardCell cells; not
  // <a> elements — the first pass's a-only probe found nothing but an
  // offscreen carousel slide).
  const card = await tag('pcard', () => {
    const cands = [...document.querySelectorAll('li[class*="cardCell" i], [class*="cardCell" i], a[class*="card" i], [class*="cardLink" i]')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 250 && r.width < 700 && r.height > 100 && r.left >= 0 && (e.innerText || '').trim().length > 10;
    });
    return cands.sort((a, b) => a.getBoundingClientRect().top + scrollY - (b.getBoundingClientRect().top + scrollY))[0] || null;
  });
  if (card) await S('platform-ai-card', q('[data-m="pcard"]'), ['default', 'hover'], { group: g, title: 'Platform AI card', desc: 'A card of the "Add AI to your workflows" grid on /platform/ai ("Generate high-impact campaign concepts").', sel: 'a cardCell' });
  // The "You have questions? We have answers." FAQ accordion near the bottom.
  const faq = await tag('faqitem', () => {
    const cands = [...document.querySelectorAll('button, [role=button], summary, details, [aria-expanded]')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 300 && r.height > 15 && /\?/.test(e.innerText || '') && /omni|airtable|cost|edit|apps/i.test(e.innerText || '');
    });
    return cands[0] || null;
  });
  if (faq) {
    await S('faq-item', q('[data-m="faqitem"]'), ['default', 'hover'], { group: g, title: 'FAQ item', desc: 'An accordion question in the "You have questions? We have answers." section.', sel: 'an accordion question' });
    await S('faq-item-open', q('[data-m="faqitem"]'), ['default'], { group: g, title: 'FAQ item, open', desc: 'The same accordion item clicked open; a local expand.', sel: 'the open accordion item' }, { open: async () => { const l = q('[data-m="faqitem"]').filter({ visible: true }).first(); const exp = await l.evaluate((el) => el.getAttribute('aria-expanded')).catch(() => null); if (exp !== 'true') { await toggle(q('[data-m="faqitem"]')).catch(() => {}); await page.waitForTimeout(1200); } }, openTarget: openItem('faqitem'), via: 'clicked the question open' });
  }
  await page.close();
}

// ---------- pricing ----------
async function pricing() {
  await newPage('pricing');
  const g = G.pricing;
  const card = await tag('pcard', () => {
    const scope = document.querySelector('main') || document.body;
    const cands = [...scope.querySelectorAll('*')].filter((e) => {
      const r = e.getBoundingClientRect();
      if (!(r.width > 200 && r.width < 500 && r.height > 250)) return false;
      const t = e.innerText || '';
      // a plan column carries a $ price or "Custom pricing" plus a CTA; a footer
      // link column carries the words too, so require the price text and few links
      if (!/\$\d+|custom pricing/i.test(t)) return false;
      if (e.querySelectorAll('a').length > 4) return false;
      if (!e.querySelector('a, button, [role=button]')) return false;
      // the smallest ancestor chain that still holds a whole plan: reject only
      // when a child also carries BOTH the price text and a button
      return ![...e.children].some((c) => /\$\d+|custom pricing/i.test(c.innerText || '') && c.querySelector('a, button, [role=button]') && c.getBoundingClientRect().width > 200);
    });
    return cands.sort((a, b) => a.innerText.length - b.innerText.length)[0] || null;
  });
  if (card) await S('plan-card', q('[data-m="pcard"]'), ['default'], { group: g, title: 'Plan card', desc: 'A plan column on the pricing grid (Free, Team $20, Business $45, Enterprise Scale).', sel: 'a plan column' });
  const table = await tag('ctable', () => {
    // The comparison is a div grid: hover-container rows under a sticky plan
    // header, inside the smallest box holding "Compare our plans" + >= 5 rows.
    const all = [...document.querySelectorAll('body *')].filter((e) => {
      const r = e.getBoundingClientRect();
      if (!(r.width > 500 && r.height > 400)) return false;
      return /compare our plans/i.test(e.innerText || '') && e.querySelectorAll('[class*="hover-container" i]').length >= 5;
    });
    return all.sort((a, b) => a.getBoundingClientRect().height - b.getBoundingClientRect().height)[0] || null;
  });
  if (table) {
    await S('compare-table', q('[data-m="ctable"]'), ['default'], { group: g, title: 'Plan comparison table', desc: 'The "Compare our plans" feature table: a div grid of plan columns against feature rows with checks (measured whole; no <table> element).', sel: 'the comparison grid' });
    const trow = await tag('trow', () => {
      const cands = [...document.querySelectorAll('[data-m="ctable"] [class*="hover-container" i], [data-m="ctable"] tr, [data-m="ctable"] [class*="row" i]')].filter((e) => {
        const r = e.getBoundingClientRect();
        return r.width > 500 && r.height > 15 && r.height < 90 && (e.innerText || '').trim().length > 3;
      });
      return cands[0] || null;
    });
    if (trow) await S('compare-table-row', q('[data-m="trow"]'), ['default'], { group: g, title: 'Comparison row', desc: 'A feature row in the comparison table (a hover-container flex row).', sel: 'a table row' });
  }
  // The pricing FAQ accordion; the first pass measured the closed trigger for
  // the open state, so re-read both, measuring the opened item itself.
  const faq = await tag('faqitem', () => {
    const cands = [...document.querySelectorAll('button, [role=button], summary, details, [aria-expanded], [class*="pointer" i]')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 300 && r.height > 15 && /\?/.test(e.innerText || '') && /pricing|airtable|cost|pay|plan|free|seats|billing/i.test(e.innerText || '');
    });
    return cands[0] || null;
  });
  if (faq) {
    await S('pricing-faq-item', q('[data-m="faqitem"]'), ['default', 'hover'], { group: g, title: 'Pricing FAQ item', desc: 'An accordion question in the pricing FAQ ("How does Airtable\'s pricing work?").', sel: 'an accordion row' });
    await S('pricing-faq-item-open', q('[data-m="faqitem"]'), ['default'], { group: g, title: 'Pricing FAQ item, open', desc: 'The same accordion item clicked open; a local expand.', sel: 'the open accordion row' }, { open: async () => { const l = q('[data-m="faqitem"]').filter({ visible: true }).first(); const exp = await l.evaluate((el) => el.getAttribute('aria-expanded')).catch(() => null); if (exp !== 'true') { await toggle(q('[data-m="faqitem"]')).catch(() => {}); await page.waitForTimeout(1200); } }, openTarget: openItem('faqitem'), via: 'clicked the question open' });
  }
  await page.close();
}

// ---------- contact-sales ----------
async function contactSales() {
  await newPage('contact-sales');
  const g = G.contact;
  // A real <label> element (the floating "* First Name" label inside a field).
  const lab = await tag('flabel', () => [...document.querySelectorAll('label[class*="_label" i], label')].find((e) => {
    const r = e.getBoundingClientRect();
    return r.width > 40 && r.height > 8 && (e.innerText || '').trim().length > 2;
  }) || null);
  if (lab) await S('field-label', q('[data-m="flabel"]'), ['default'], { group: g, title: 'Field label', desc: 'A floating label inside a field of the form ("* First Name").', sel: 'a label element' });
  // The "Country" dropdown: a custom combobox-style field box (the mkto
  // <select> mirrors stay hidden at 0x0; the visible control is a div with a
  // chevron). Measured at rest and clicked open; no option was chosen.
  const sel = await tag('csel', () => {
    const cands = [...document.querySelectorAll('main div, main button, main [role=combobox], form div, body div')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 200 && r.width < 600 && r.height > 30 && r.height < 110 && /country|how can our team help/i.test((e.innerText || '').trim().slice(0, 60)) && (e.querySelector('svg') || /combobox|select/i.test(String(e.className)));
    });
    return cands.sort((a, b) => a.getBoundingClientRect().width * a.getBoundingClientRect().height - b.getBoundingClientRect().width * b.getBoundingClientRect().height)[0] || null;
  });
  if (sel) {
    await S('select-field', q('[data-m="csel"]'), ['default', 'hover'], { group: g, title: 'Select field', desc: 'The "Country" dropdown in the form (a custom combobox, not a native select). Measured at rest; never submitted.', sel: 'the Country field' });
    await S('select-field-open', q('[data-m="csel"]'), ['default'], { group: g, title: 'Select field, open', desc: 'The Country dropdown clicked open; a local disclosure, nothing chosen.', sel: 'the open dropdown' }, { open: async () => { const inner = q('[data-m="csel"] [class*="-control" i], [data-m="csel"] [role=combobox], [data-m="csel"] button').filter({ visible: true }).first(); await toggle((await inner.count()) ? inner : q('[data-m="csel"]')).catch(() => {}); await page.waitForTimeout(1500); }, openTarget: openMenu('csel'), noReset: true, via: 'clicked the field open; nothing chosen' });
    await page.keyboard.press('Escape').catch(() => {});
  }
  const sub = await tag('submit', () => [...document.querySelectorAll('button, [role=button], input[type=submit]')].find((e) => {
    const r = e.getBoundingClientRect();
    return r.width > 100 && r.height > 20 && /^(submit|contact sales)$/i.test((e.innerText || e.value || '').trim());
  }) || null);
  if (sub) await S('submit-button', q('[data-m="submit"]'), ['default', 'hover', 'focus-visible'], { group: g, title: 'Submit button', desc: 'The dark "Submit" of the sales form. Measured and focused, never pressed.', sel: 'the submit button' });
  await page.close();
}

// ---------- templates ----------
async function templates() {
  await newPage('templates');
  const g = G.cards;
  const card = await tag('tcard', () => {
    const cands = [...document.querySelectorAll('a, [role=link], [class*="card" i]')].filter((e) => {
      const r = e.getBoundingClientRect();
      const top = r.top + scrollY;
      return r.width > 200 && r.height > 80 && top > 300 && r.left >= 0 && (e.querySelector('img, video, h2, h3, svg') || /template/i.test(e.innerText || '')) && (e.innerText || '').trim().length > 3;
    });
    return cands.sort((a, b) => a.getBoundingClientRect().top + scrollY - (b.getBoundingClientRect().top + scrollY))[0] || null;
  });
  if (card) await S('template-card', q('[data-m="tcard"]'), ['default', 'hover'], { group: g, title: 'Template card', desc: 'A template tile in the gallery (the "Project Management" use-case tiles and the featured cards below).', sel: 'a template card' });
  // The filter rail's collapsible group; the first pass recorded the closed
  // button for the open state, so re-read both, measuring the opened group.
  const filt = await tag('filt', () => [...document.querySelectorAll('button')].find((e) => /^by (use case|industry|feature)/i.test((e.innerText || '').trim())) || null);
  if (filt) {
    await S('filter-section', q('[data-m="filt"]'), ['default', 'hover', 'focus-visible'], { group: g, title: 'Filter section', desc: 'A collapsible filter group in the templates rail (By Use Case / By Industry / By Feature).', sel: 'a filter group button' });
    await S('filter-section-open', q('[data-m="filt"]'), ['default'], { group: g, title: 'Filter section, open', desc: 'The filter group clicked open; a local expand.', sel: 'the open filter group' }, { open: async () => { const l = q('[data-m="filt"]').filter({ visible: true }).first(); const exp = await l.evaluate((el) => el.getAttribute('aria-expanded')).catch(() => null); if (exp !== 'true') { await toggle(q('[data-m="filt"]')).catch(() => {}); await page.waitForTimeout(1200); } }, openTarget: openItem('filt'), via: 'clicked the filter group open' });
  }
  await page.close();
}

// ---------- whatsnew ----------
async function whatsnew() {
  await newPage('whatsnew');
  const g = G.cards;
  const h = await tag('wntitle', () => document.querySelector('h1, [role=heading], h2') || [...document.querySelectorAll('main *')].find((e) => /where airtable is headed/i.test(e.innerText || '') && (e.innerText || '').length < 120) || null);
  if (h) await S('whatsnew-title', q('[data-m="wntitle"]'), ['default'], { group: g, title: "What's new title", desc: 'The "Where Airtable is headed." heading.', sel: 'the page heading' }, { noScroll: true });
  // The release gallery is Airtable's own published interface embedded as an
  // iframe (airtable.com/embed/appL2oaKxSWg9qz8y); measure inside the frame.
  const frame = page.frameLocator('iframe[src*="airtable.com/embed"], iframe[src*="/embed/"]').first();
  const cardLoc = frame.locator('[class*="galleryCard" i], [class*="card" i], a, li, article, [role=row]').filter({ visible: true })
    .filter({ has: page.locator('img') }).first();
  if (await cardLoc.count()) {
    await S('whatsnew-item', cardLoc, ['default', 'hover'], { group: g, title: "What's new card", desc: 'A release card in the embedded roadmap gallery (plan chips and a release-month chip), inside airtable.com/embed/appL2oaKxSWg9qz8y.', sel: 'a card in the embed' });
  } else {
    const any = frame.locator('[class*="card" i], a, li').filter({ hasText: /20\d\d|free|team|business/i }).filter({ visible: true }).first();
    if (await any.count()) await S('whatsnew-item', any, ['default', 'hover'], { group: g, title: "What's new card", desc: 'A release card in the embedded roadmap gallery.', sel: 'a card in the embed' });
    else { comp('whatsnew-item', { group: g, title: "What's new card", desc: 'A release card in the embedded roadmap gallery.', selector: 'a card in the embed' }); out.components['whatsnew-item'].missing = true; }
  }
  const filt = frame.locator('button, [role=combobox], [role=listbox]').filter({ hasText: /available on|release month/i }).filter({ visible: true }).first();
  if (await filt.count()) {
    await S('whatsnew-filter', filt, ['default', 'hover', 'focus-visible'], { group: g, title: "What's new filter", desc: 'An "Available on" / "Release month" filter dropdown in the embedded release gallery. Measured and focused, never opened.', sel: 'a filter button in the embed' });
  }
  await page.close();
}

// ---------- marketplace ----------
async function marketplace() {
  await newPage('marketplace');
  const g = G.cards;
  // One category card ("For marketing teams" / "Page designer" / "Scripting"):
  // big colour-saturated tiles; not the grid wrapper the first pass read, and
  // their text does not reach innerText reliably, so find them by paint.
  const card = await tag('mcard', () => {
    // The tiles' text is screen-reader-only, so innerText misses it: match on
    // textContent instead, else fall back to a big saturated box in the top band.
    let cands = [...document.querySelectorAll('body *')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 250 && r.width < 700 && r.height > 150 && r.height < 600 && r.left >= 0 && /for marketing teams|page designer|scripting/i.test(e.textContent || '');
    });
    if (!cands.length) {
      cands = [...document.querySelectorAll('body *')].filter((e) => {
        const r = e.getBoundingClientRect();
        if (!(r.width > 250 && r.width < 700 && r.height > 150 && r.height < 600 && r.left >= 0)) return false;
        const top = r.top + scrollY;
        if (top < 250 || top > 2500) return false;
        const m = getComputedStyle(e).backgroundColor.match(/rgba?\((\d+),\s*(\d+),\s*(\d+)/);
        if (!m) return false;
        const [rr, gg, bb] = [+m[1], +m[2], +m[3]];
        return Math.max(rr, gg, bb) - Math.min(rr, gg, bb) > 60 && Math.max(rr, gg, bb) > 120;
      });
    }
    // the tiles are background-image divs (flex-auto background-cover rounded-huge)
    if (!cands.length) {
      cands = [...document.querySelectorAll('div[class*="background-cover" i][class*="rounded" i], div.col-4 div[class*="flex" i]')].filter((e) => {
        const r = e.getBoundingClientRect();
        return r.width > 250 && r.width < 700 && r.height > 150 && r.height < 600 && r.left >= 0;
      });
    }
    // walk down: keep the candidate that still holds the whole tile
    return cands.sort((a, b) => a.querySelectorAll('*').length - b.querySelectorAll('*').length)[0] || cands[0] || null;
  });
  if (card) await S('market-card', q('[data-m="mcard"]'), ['default', 'hover'], { group: g, title: 'Marketplace category card', desc: 'A category card on the marketplace ("For marketing teams", "Page designer", "Scripting").', sel: 'a coloured category tile' });
  await page.close();
}

// ---------- mobile ----------
async function mobile() {
  await newPage('mobile', { mobile: true });
  const g = G.mobile;
  const btn = page.locator('button[aria-label*="side menu" i], button[aria-label*="menu" i]:not([aria-label*="back" i]):not([aria-label*="close" i])').filter({ visible: true }).first();
  if (await btn.count()) {
    await btn.click({ timeout: 4000 }).catch(() => {});
    await page.waitForTimeout(2500);
    const sheet = await tag('msheet', () => {
      // The opened drawer is a positioned overlay pinned to the viewport top;
      // an in-flow nav (the footer link columns at top>1000) is not the sheet.
      const cands = [...document.querySelectorAll('[role=dialog], [class*="navDrawer" i], [class*="drawer" i], [class*="sheet" i], [class*="menu" i], [class*="modal" i], nav, aside')].filter((e) => {
        const r = e.getBoundingClientRect(), cs = getComputedStyle(e);
        return r.top <= 200 && (cs.position === 'fixed' || cs.position === 'absolute') && r.height > 200 && r.width > 150 && r.left < 100 && (e.innerText || '').trim().length > 10 && e.querySelectorAll('a, button').length > 2;
      });
      return cands.sort((a, b) => a.getBoundingClientRect().width * a.getBoundingClientRect().height - b.getBoundingClientRect().width * b.getBoundingClientRect().height)[0] || null;
    });
    if (sheet) await S('m-nav-sheet', q('[data-m="msheet"]'), ['default'], { group: g, title: 'Mobile nav sheet', desc: 'The side drawer the "Open side menu" button opens at 390.', sel: 'the open menu' }, { noScroll: true, via: 'clicked the menu button' });
    else { const c = comp('m-nav-sheet', { group: g, title: 'Mobile nav sheet', desc: 'The side drawer the "Open side menu" button opens at 390.', selector: 'the open menu' }); c.missing = true; c.states = {}; /* the earlier reading was the footer nav, not the sheet */ }
    await page.keyboard.press('Escape').catch(() => {});
  }
  await page.close();
}

const RUNS = { home, platform, 'platform-ai': platformAi, pricing, 'contact-sales': contactSales, templates, whatsnew, marketplace, mobile };
const want = process.argv.slice(2).length ? process.argv.slice(2) : Object.keys(RUNS);
for (const k of want) {
  const l = await launch({ mobile: k === 'mobile' });
  context = l.context;
  run = k === 'mobile' ? 'mobile' : k;
  try { await RUNS[k](); } catch (e) { log('RUN FAILED', k, String(e.message).split('\n')[0]); }
  out._meta.read = new Date().toLocaleDateString('en-CA');
  save();
  await l.browser.close();
}
log('done ->', OUT);
