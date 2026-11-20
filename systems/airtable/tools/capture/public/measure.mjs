// Measures Airtable's components on its public pages, in every state that can be
// reached without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home platform platform-ai solutions enterprise pricing contact-sales
//        customer-stories templates marketplace whatsnew about mobile.
// Writes raw/components-computed.json (merged, so a subset of pages can be re-run),
// raw/layout.json (the frame of each page) and one crop per component and state
// into components/crops/. raw/measurements.md is then built from the JSON by
// build-measurements.mjs.
//
// One surface: www.airtable.com, a Next.js marketing site on CSS modules with hashed
// prefixes (`X_module__hash` and `hash_name` shapes; readable suffixes like _tab,
// _cardLink, _arrowButton are stable) plus shared utility classes (pill, link,
// colors-hyperlink-primary). The site declares a real token system: --color-* palette
// and semantics, --theme_* per-component state vars (scoped to .light/.darkBlue/...
// section themes), --type-*, --spacing-*, --radius-*, --border-width-*, --shadow-*.
// airtable.com/<workspace> (the app), /signup, /login and Book Demo are the signed or
// sign-up surface and are never touched; the /contact-sales Marketo form is measured,
// never submitted.
//
// States:
//   hover          real mouse hover, 450ms settle for transitions
//   focus-visible  keyboard: focus, Shift+Tab, Tab, so the browser sees a keyboard focus
//   pressed        CDP CSS.forcePseudoState [active, hover]; no mouse button is pressed,
//                  so no link or submit button can fire
//   focused        the field clicked into (a text field only)
//   filled         sample text typed into a field, measured, then deleted; Enter is never pressed
//   open           a resting state reached by a UI toggle (a nav dropdown, a tab, an
//                  accordion); nothing that submits, calls or signs in is ever pressed
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, open, closePromo, styleOf, crop, centre, markFixed, RAW } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const LAYOUT_OUT = path.join(RAW, 'layout.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
const layout = fs.existsSync(LAYOUT_OUT) ? JSON.parse(fs.readFileSync(LAYOUT_OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => { fs.mkdirSync(RAW, { recursive: true }); fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n'); };
const saveLayout = () => { fs.mkdirSync(RAW, { recursive: true }); fs.writeFileSync(LAYOUT_OUT, JSON.stringify(layout, null, 1) + '\n'); };

const URLS = {
  home: BASE + '/', platform: BASE + '/platform', 'platform-ai': BASE + '/platform/ai',
  solutions: BASE + '/solutions', enterprise: BASE + '/solutions/enterprise',
  pricing: BASE + '/pricing', 'contact-sales': BASE + '/contact-sales',
  'customer-stories': BASE + '/customer-stories', templates: BASE + '/templates',
  marketplace: BASE + '/marketplace', whatsnew: BASE + '/whatsnew', about: BASE + '/about',
};

let page, cdp, current, context, run;
const touched = new Set();

// ---------- helpers ----------

async function newPage(key, { mobile = false, promo = 'close', wait = 7000 } = {}) {
  current = key;
  page = await context.newPage();
  page.setDefaultTimeout(8000);
  cdp = await context.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  log('open', key, mobile ? '(mobile)' : '', URLS[key]);
  await open(page, URLS[key], { wait, promo });
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

// Clicks a UI toggle (a nav trigger, a tab, an accordion, a menu button). Refuses a
// submit button and any control whose text names an action this kit must never take.
const NEVER = /^(send|submit|sign up|sign up for free|log in|try it now|book demo|book a demo|contact sales|get started|get started for free|create|generate|upload|start|start free trial|upgrade|subscribe|apply|accept all|reject all|manage cookies|privacy choices|cookie settings|request demo|get a demo|join|share|buy|purchase|claim|view all.*|see all.*)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

function comp(key, meta) {
  const c = (out.components[key] ??= { states: {} });
  Object.assign(c, { page: current, run, url: URLS[current] }, meta);
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

const FILL = 'a workflow tracker for a studio';

// Records the listed states of one component. meta: title, group, desc, sel.
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
      } else if (st === 'focused') {
        await (opts.fieldLoc || loc).filter({ visible: true }).first().click({ timeout: 4000 });
        await page.waitForTimeout(400);
        via = 'clicked into the field';
      } else if (st === 'filled') {
        const f = (opts.fieldLoc || loc).filter({ visible: true }).first();
        await f.click({ timeout: 4000 });
        await page.keyboard.type(opts.fillText || FILL, { delay: 10 });
        await page.waitForTimeout(500);
        undo = async () => { await f.focus(); await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace'); await page.waitForTimeout(300); };
        via = `typed "${opts.fillText || FILL}", then deleted; nothing sent`;
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

// openTarget probes for S({open, openTarget}): each returns the element that
// shows the opened state (the capture guide wants the whole popup, not the
// trigger), or null when the toggle did not open, so the state is recorded as
// an error rather than a measurement of the still-closed trigger. tag()
// serializes the probe's source, so the factories build a free-variable-free
// function with the trigger's data-m name inlined.
// The smallest ancestor of the trigger that holds both the question and the
// opened answer; gated on an opened marker so a closed accordion's parents
// (which hold the hidden answers) do not count.
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
// The popup the combobox raised: the field wrapper when the menu mounts inside
// it, otherwise the portaled menu itself; null when nothing opened.
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

// Tags the first element matching an in-page probe so a locator can find it:
// await tag('nav', () => {...return element or null...}) then q('[data-m="nav"]').
async function tag(name, probe) {
  return page.evaluate(([n, src]) => {
    const el = (new Function('return (' + src + ')')())();
    if (!el) return false;
    document.querySelectorAll(`[data-m="${n}"]`).forEach((o) => o.removeAttribute('data-m'));
    el.setAttribute('data-m', n);
    return true;
  }, [name, probe.toString()]).catch(() => false);
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
    const el = cands.find((e) => e.matches('a,button,[role=button],[role=tab],li,[tabindex]') || getComputedStyle(e).cursor === 'pointer') || cands[0];
    if (!el) return false;
    document.querySelectorAll(`[data-m="${n}"]`).forEach((o) => o.removeAttribute('data-m'));
    el.setAttribute('data-m', n);
    return true;
  }, [name, reSrc, scopeSel || null]).catch(() => false);
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
        if (t || a) transitions.push({ selector: (r.selectorText || '').replace(/__[A-Za-z0-9_-]{5,6}/g, '').slice(0, 160), transition: t, animation: a });
      }
    };
    for (const ss of document.styleSheets) { try { walk(ss.cssRules); } catch { /* cross-origin, read by vars.mjs */ } }
    return transitions;
  });
  out._meta.sheets ??= {};
  out._meta.sheets[key] = res;
}

// The page's frame: nav height and position, the widest content column, the
// card grids' column counts and gaps, and every fixed overlay still painted.
async function layoutFor(key) {
  layout[key] = await page.evaluate(() => {
    const vw = innerWidth, vh = innerHeight;
    const vis = (e) => { const r = e.getBoundingClientRect(); return r.width > 4 && r.height > 4 && getComputedStyle(e).visibility !== 'hidden'; };
    const fixed = [...document.querySelectorAll('body *')].filter((e) => { const cs = getComputedStyle(e); return (cs.position === 'fixed' || cs.position === 'sticky') && vis(e) && e.getBoundingClientRect().top < vh && e.getBoundingClientRect().bottom > 0; })
      .map((e) => ({ el: e.tagName.toLowerCase() + (e.classList[0] ? '.' + String(e.classList[0]).split('__').pop() : ''), pos: getComputedStyle(e).position, top: +e.getBoundingClientRect().top.toFixed(0), w: +e.getBoundingClientRect().width.toFixed(0), h: +e.getBoundingClientRect().height.toFixed(0), text: (e.innerText || '').trim().slice(0, 60), backdrop: getComputedStyle(e).backdropFilter !== 'none' ? getComputedStyle(e).backdropFilter : undefined })).slice(0, 12);
    const maxWidths = [...document.querySelectorAll('main *, body > * > *')].filter(vis).map((e) => ({ w: +e.getBoundingClientRect().width.toFixed(0), max: getComputedStyle(e).maxWidth }))
      .filter((m) => m.max !== 'none' && parseFloat(m.max) > 200).slice(0, 8);
    const grids = [...document.querySelectorAll('body *')].filter((e) => getComputedStyle(e).display === 'grid' && vis(e)).map((e) => {
      const cs = getComputedStyle(e);
      return { el: e.tagName.toLowerCase() + (e.classList[0] ? '.' + String(e.classList[0]).split('__').pop() : ''), cols: cs.gridTemplateColumns.slice(0, 90), colGap: cs.columnGap, rowGap: cs.rowGap, w: +e.getBoundingClientRect().width.toFixed(0) };
    }).filter((g) => g.cols.split(' ').length > 1).slice(0, 8);
    return { vw, vh, docH: document.documentElement.scrollHeight, fixed, maxWidths, grids };
  }).catch((e) => ({ error: String(e).slice(0, 200) }));
  saveLayout();
}

// ---------- groups ----------
const G = {
  shell: 'Shell and navigation', home: 'Home', cards: 'Cards and indexes',
  platform: 'Platform pages', pricing: 'Pricing', contact: 'Contact sales form',
  overlay: 'Overlays', mobile: 'Mobile (390 wide)',
};
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

// The marketing chrome: a promo bar ("Bring your Airtable data into Claude.
// Try it now" + a close button), then the main header — wordmark, Platform /
// Solutions / Resources dropdown triggers, Enterprise / Pricing / What's new
// links, and Book Demo / Sign up for free / Log in on the right.
async function shell(pageKey) {
  const g = G.shell;
  const promo = await tag('promo', () => {
    const cands = [...document.querySelectorAll('[class*="whatsNewNav" i], [class*="promoBar" i], [class*="promo-bar" i], body > * > *')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.top <= 4 && r.width > 600 && r.height > 20 && r.height < 60 && /try it now|claude|bring your/i.test(e.innerText || '');
    });
    return cands.sort((a, b) => a.getBoundingClientRect().height - b.getBoundingClientRect().height)[0] || null;
  });
  if (promo) {
    await S('promo-bar', q('[data-m="promo"]'), ['default'], { group: g, title: 'Promo bar', desc: 'The dismissible strip above the nav ("Bring your Airtable data into Claude. Try it now").', sel: 'the top promo strip' }, { noScroll: true });
    if (await tagEl('promolink', 'try it now', '[data-m="promo"]'))
      await S('promo-link', q('[data-m="promolink"]'), B4, { group: g, title: 'Promo link', desc: 'The "Try it now" link in the promo bar. Measured and focused, never followed.', sel: 'the promo link' }, { noScroll: true });
    const x = await tag('promox', () => document.querySelector('button[aria-label*="close" i], button[aria-label*="dismiss" i]') || null);
    if (x) await S('promo-close', q('[data-m="promox"]'), ['default', 'hover', 'focus-visible'], { group: g, title: 'Promo close button', desc: 'The × that dismisses the promo bar; a local dismissal, measured and focused, never pressed.', sel: 'aria-label "Close promo banner"' }, { noScroll: true });
  }
  const nav = await tag('nav', () => {
    const cands = [...document.querySelectorAll('header, [class*="header" i], nav')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.top <= 100 && r.width > 500 && r.height > 30 && r.height < 140 && /platform|pricing|solutions|log in/i.test(e.innerText || '');
    });
    return cands.sort((a, b) => a.getBoundingClientRect().height * a.getBoundingClientRect().width - b.getBoundingClientRect().height * b.getBoundingClientRect().width)[0] || null;
  });
  if (nav) {
    await S('nav-bar', q('[data-m="nav"]'), ['default'], { group: g, title: 'Top navigation bar', desc: 'The header on every marketing page: the Airtable wordmark, Platform/Solutions/Resources triggers, Enterprise, Pricing, What\'s new, and Book Demo / Sign up for free / Log in.', sel: 'header' }, { noScroll: true });
    await tagEl('navtrig', '^platform$|^solutions$|^resources$', '[data-m="nav"]');
    if (await q('[data-m="navtrig"]').count())
      await S('nav-trigger', q('[data-m="navtrig"]'), B4, { group: g, title: 'Nav dropdown trigger', desc: 'A section trigger in the header (Platform); opens the section drawer on click. Measured, never followed.', sel: 'the Platform trigger' }, { noScroll: true });
    if (await tagEl('navlink', '^enterprise$|^pricing$|^what.s new$', '[data-m="nav"]'))
      await S('nav-link', q('[data-m="navlink"]'), B4, { group: g, title: 'Nav link', desc: 'A direct link in the header (Enterprise, Pricing, What\'s new). Measured, never followed.', sel: 'a header link' }, { noScroll: true });
    if (await tagEl('navdemo', '^book demo$', '[data-m="nav"]'))
      await S('nav-demo', q('[data-m="navdemo"]'), B4, { group: g, title: 'Book Demo button', desc: 'The outline "Book Demo" button in the header. Measured and focused, never followed (it leaves for the demo form).', sel: 'the Book Demo button' }, { noScroll: true });
    if (await tagEl('navsignup', '^sign up for free$|^sign up$', '[data-m="nav"]'))
      await S('nav-signup', q('[data-m="navsignup"]'), B4, { group: g, title: 'Sign up button', desc: 'The dark "Sign up for free" pill in the header. Measured and focused, never followed.', sel: 'the Sign up button' }, { noScroll: true });
    if (await tagEl('navlogin', '^log in$', '[data-m="nav"]'))
      await S('nav-login', q('[data-m="navlogin"]'), B4, { group: g, title: 'Log in link', desc: 'The "Log in" text link in the header. Measured and focused, never followed.', sel: 'the Log in link' }, { noScroll: true });
    const trig = q('[data-m="navtrig"]');
    if (await trig.count()) {
      // The drawers open on click; the trigger is a <button> (a local disclosure).
      const openDrawer = async () => {
        const open = await page.evaluate(() => {
          const cands = [...document.querySelectorAll('[class*="navDrawer" i], [class*="drawerMenu" i]')].filter((e) => {
            const r = e.getBoundingClientRect();
            return r.left >= -10 && r.width > 150 && r.height > 200 && e.querySelector('a');
          });
          return cands.length > 0;
        });
        if (!open) { await trig.click({ timeout: 4000 }).catch(() => {}); await page.waitForTimeout(1800); }
      };
      await openDrawer();
      const menu = await tag('submenu', () => {
        // The open drawer is the navDrawerMenu element marked drawerIsActive
        // (closed drawers stay mounted offscreen at negative x).
        const cands = [...document.querySelectorAll('[class*="navDrawerMenu" i][class*="drawerIsActive" i], [class*="navDrawer" i], [class*="drawerMenu" i], [class*="drawerInner" i], [role=menu], [class*="drawer" i]')].filter((e) => {
          const r = e.getBoundingClientRect();
          return r.left >= -10 && r.top >= -5 && r.width > 150 && r.height > 80 && e.querySelector('a') && (e.innerText || '').trim().length > 10;
        });
        return cands.sort((a, b) => a.getBoundingClientRect().width * a.getBoundingClientRect().height - b.getBoundingClientRect().width * b.getBoundingClientRect().height)[0] || null;
      });
      if (menu) await S('nav-dropdown', q('[data-m="submenu"]'), ['default'], { group: g, title: 'Nav drawer', desc: 'The drawer a header section trigger opens (Platform: the product areas and a promo card). Shown click-open; a local disclosure.', sel: 'the open drawer panel' }, { noScroll: true, via: 'clicked the trigger' });
      if (await tagEl('sublink', 'app building|ai agents|platform|portal|automations|connected data', '[data-m="submenu"]'))
        await S('nav-dropdown-link', q('[data-m="sublink"]'), ['default', 'hover'], { group: g, title: 'Drawer link', desc: 'An item in the open nav drawer.', sel: 'an item in the drawer' }, { noScroll: true, open: openDrawer });
      await page.keyboard.press('Escape').catch(() => {});
      await reset();
    }
  }
  // Footer: link columns, social icons, legal row. A bare `footer`-class match
  // can catch a carousel's control bar, so the candidate must hold real footer
  // links (legal or section links), not just media controls.
  const foot = await tag('foot', () => {
    const cands = [...document.querySelectorAll('footer, [class*="footer" i], [class*="siteFooter" i]')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 500 && r.height > 80 && /privacy|terms|careers|security|accessibility/i.test(e.innerText || '') && e.querySelectorAll('a').length >= 5;
    });
    return cands.sort((a, b) => a.innerText.length - b.innerText.length)[0] || null;
  });
  if (foot) {
    await S('footer', q('[data-m="foot"]'), ['default'], { group: g, title: 'Footer', desc: 'The site footer: link columns (AI App Building, Use Cases, Resources, Company), social icons, legal row.', sel: 'footer' });
    if (await tagEl('flink', '^templates$|^careers$|^privacy|^security|^blog$|^status$', '[data-m="foot"]'))
      await S('footer-link', q('[data-m="flink"]'), B4, { group: g, title: 'Footer link', desc: 'A link in the footer columns. Measured, never followed.', sel: 'a footer link' });
  }
}

// ---------- home ----------
async function home() {
  await newPage('home');
  await shell('home');
  const g = G.home;
  const h1 = await tag('h1', () => document.querySelector('h1'));
  if (h1) await S('hero-title', q('[data-m="h1"]'), ['default'], { group: g, title: 'Hero title', desc: 'The home h1 ("All your teams, all their workflows — connected in one workspace").', sel: 'h1' }, { noScroll: true });
  if (await tagEl('herocta', '^get started for free$|^get started$|^sign up', 'main'))
    await S('hero-cta-primary', q('[data-m="herocta"]'), B4, { group: g, title: 'Hero primary CTA', desc: 'The dark "Get started for free" pill under the hero title.', sel: 'the first primary button' });
  if (await tagEl('herocta2', '^book demo$', 'main'))
    await S('hero-cta-secondary', q('[data-m="herocta2"]'), B4, { group: g, title: 'Hero secondary CTA', desc: 'The outline "Book demo" pill beside the primary CTA.', sel: 'the secondary button' });
  // The big red feature card and its carousel dots.
  const card = await tag('fcard', () => {
    const cands = [...document.querySelectorAll('a, [class*="card" i], [class*="slide" i], section > div')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 700 && r.height > 200 && r.top > 300 && /workflow|speed|minutes/i.test(e.innerText || '');
    });
    return cands.sort((a, b) => a.getBoundingClientRect().height - b.getBoundingClientRect().height)[0] || null;
  });
  if (card) await S('feature-card', q('[data-m="fcard"]'), ['default', 'hover'], { group: g, title: 'Feature card', desc: 'The large red "Sophisticated workflows" feature card.', sel: 'the big feature card' });
  const dot = await tag('cdot', () => {
    const cands = [...document.querySelectorAll('[role=tab], [class*="dot" i], [class*="pagination" i] button, button')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width >= 6 && r.width <= 60 && r.height >= 6 && r.height <= 60 && /slide|previous|next|pause|autoplay|animation|\d/.test((e.getAttribute('aria-label') || '') + ' ' + (e.innerText || ''));
    });
    return cands[0] || null;
  });
  if (dot) await S('carousel-control', q('[data-m="cdot"]'), B4, { group: g, title: 'Carousel control', desc: 'A carousel control on the home page (a pause button or a numbered tab of the feature carousel).', sel: 'a carousel control' });
  // The light-blue Omni card ("Say hello to Omni").
  const ai = await tag('aicard', () => {
    const cands = [...document.querySelectorAll('[class*="textMediaCard" i], [class*="MediaCard" i], [class*="card" i]')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 300 && r.width < 1100 && r.height > 100 && r.height < 800 && /omni|deploy it/i.test(e.innerText || '');
    });
    return cands.sort((a, b) => a.getBoundingClientRect().width * a.getBoundingClientRect().height - b.getBoundingClientRect().width * b.getBoundingClientRect().height)[0] || null;
  });
  if (ai) await S('ai-card', q('[data-m="aicard"]'), ['default', 'hover'], { group: g, title: 'AI feature card', desc: 'The light-blue "Say hello to Omni" card.', sel: 'the Omni media card' });
  const faq = await tag('faqitem', () => {
    const cands = [...document.querySelectorAll('button, [role=button], summary, details, [aria-expanded], [class*="faq" i] > *')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 300 && r.height > 15 && /\?/.test(e.innerText || '');
    });
    return cands[0] || null;
  });
  if (faq) {
    await S('faq-item', q('[data-m="faqitem"]'), ['default', 'hover'], { group: g, title: 'FAQ item', desc: 'An accordion question on the home page.', sel: 'an accordion question' });
    // open state: a local expand; measure the opened item, not the trigger
    await S('faq-item-open', q('[data-m="faqitem"]'), ['default'], { group: g, title: 'FAQ item, open', desc: 'The same accordion item clicked open; a local expand.', sel: 'the open accordion item' }, { open: async () => { const l = q('[data-m="faqitem"]').filter({ visible: true }).first(); const exp = await l.evaluate((el) => el.getAttribute('aria-expanded')).catch(() => null); if (exp !== 'true') { await toggle(q('[data-m="faqitem"]')).catch(() => {}); await page.waitForTimeout(1200); } }, openTarget: openItem('faqitem'), via: 'clicked the question open' });
  }
  // The "path to 10x" coloured tiles.
  const tile = await tag('tile', () => {
    const cands = [...document.querySelectorAll('a, [class*="card" i], [class*="tile" i]')].filter((e) => {
      const r = e.getBoundingClientRect(), cs = getComputedStyle(e);
      return r.width > 200 && r.width < 800 && r.height > 150 && r.top > 800 && cs.backgroundColor !== 'rgba(0, 0, 0, 0)' && cs.backgroundColor !== 'rgb(255, 255, 255)';
    });
    return cands[0] || null;
  });
  if (tile) await S('tile-card', q('[data-m="tile"]'), ['default', 'hover'], { group: g, title: 'Coloured tile card', desc: 'A coloured tile in the "path to 10x" grid (orange, blue, green surfaces).', sel: 'a coloured tile' });
  const res = await tag('rescard', () => {
    // doc-space top: the capture has scrolled the page by now, so a
    // viewport-rect test finds nothing
    const cands = [...document.querySelectorAll('a')].filter((e) => {
      const r = e.getBoundingClientRect();
      const top = r.top + scrollY;
      return r.width > 240 && r.height > 60 && top > 1500 && (e.querySelector('img, h2, h3, [class*="title" i]')) && /breakthrough|guide|in action|resource|watch|read/i.test(e.innerText || '');
    });
    return cands.sort((a, b) => a.getBoundingClientRect().top + 0 - (b.getBoundingClientRect().top + 0))[0] || cands[0] || null;
  });
  if (res) await S('resource-card', q('[data-m="rescard"]'), ['default', 'hover'], { group: g, title: 'Resource card', desc: 'A card in the "Resources to inspire" row.', sel: 'a resource card' });
  await sheetsFor('home');
  await layoutFor('home');
  await page.close();
}

// ---------- platform pages ----------
async function platformPage(key) {
  await newPage(key);
  if (key === 'platform') await shell(key);
  const g = G.platform;
  const h1 = await tag('h1', () => document.querySelector('h1'));
  if (h1) await S(key + '-title', q('[data-m="h1"]'), ['default'], { group: g, title: 'Platform page title', desc: 'The h1 on ' + URLS[key] + '.', sel: 'h1' }, { noScroll: true });
  if (await tagEl('pcta', '^get started|^sign up|^book demo|^learn more|^contact sales', 'main'))
    await S(key + '-cta', q('[data-m="pcta"]'), B4, { group: g, title: 'Platform CTA', desc: 'A primary button on the platform page. Measured and focused, never followed.', sel: 'the first CTA' });
  // The linked cards ("Ways to start building with agents", "Resources and
  // insights to inspire"). Carousel slides sit offscreen at negative x, so a
  // candidate must be on-screen now; the locator picks a real card over a
  // slide by requiring a positive left edge.
  const card = await tag('pcard', () => {
    const cands = [...document.querySelectorAll('a[class*="card" i], [class*="cardLink" i], a, article')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 300 && r.height > 100 && r.left >= 0 && (e.querySelector('h2, h3, img, video')) && !e.closest('[class*="carousel" i], [class*="slick" i], [class*="slider" i], [role=listbox]');
    });
    return cands.sort((a, b) => a.getBoundingClientRect().top - b.getBoundingClientRect().top)[0] || null;
  });
  const cardKey = key === 'platform-ai' ? 'platform-ai-card' : 'platform-card';
  if (card) await S(cardKey, q('[data-m="pcard"]'), ['default', 'hover'], { group: g, title: 'Platform feature card', desc: key === 'platform-ai' ? 'A linked card on /platform/ai (a "Resources and insights" tile).' : 'A linked card on /platform (a "Ways to start building" tile).', sel: 'a cardLink' });
  // The feature tab strip on /platform (Shared data / Durable workflows / ...).
  const tablist = await tag('tablist', () => document.querySelector('[role=tablist], [class*="tablist" i]') || null);
  if (tablist) {
    await S('feature-tablist', q('[data-m="tablist"]'), ['default'], { group: g, title: 'Feature tab list', desc: 'The vertical tab strip ("Data that fits your business": Shared data, Durable workflows, Open surfaces, Governance).', sel: 'the tablist' });
    const tab = await tag('ftab', () => [...document.querySelectorAll('button[role=tab], [class*="_tab"]:not([class*="tablist" i]):not([class*="tabActive" i]):not([class*="expandInner" i])')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 100 && r.height > 20 && r.height < 120 && /data|workflow|surface|governance/i.test(e.innerText || '');
    })[0] || null);
    if (tab) await S('feature-tab', q('[data-m="ftab"]'), B4, { group: g, title: 'Feature tab', desc: 'One segment of the feature tab strip.', sel: 'a _tab button' });
    const act = await tag('ftabact', () => document.querySelector('button[role=tab][aria-selected="true"], [class*="tabActive" i]') || null);
    if (act) await S('feature-tab-active', q('[data-m="ftabact"]'), ['default'], { group: g, title: 'Feature tab, selected', desc: 'The selected segment of the tab strip.', sel: 'the _tabActive' });
  }
  // Customer-stories carousel controls: scroll the section in first, the arrows lazy-mount.
  const carEl = await page.evaluate(() => {
    const b = [...document.querySelectorAll('button')].find((e) => /previous|next|pause|autoplay/i.test((e.getAttribute('aria-label') || '') + ' ' + (e.innerText || '')));
    if (b) { b.scrollIntoView({ block: 'center' }); return true; }
    return false;
  });
  if (carEl) await page.waitForTimeout(1200);
  const next = await tag('snext', () => [...document.querySelectorAll('button')].find((e) => /next/i.test(e.getAttribute('aria-label') || e.innerText || '')) || null);
  if (next) await S('stories-next', q('[data-m="snext"]'), B4, { group: g, title: 'Stories next button', desc: 'The next-arrow of the customer-stories carousel.', sel: 'the next arrow button' });
  // The previous arrow stays hidden until the carousel leaves its first slide:
  // click Next once (a local UI toggle, changes no data), then measure it.
  let prev = await tag('sprev', () => [...document.querySelectorAll('button')].find((e) => /previous|prev/i.test(e.getAttribute('aria-label') || e.innerText || '')) || null);
  if (next && (!prev || !(await q('[data-m="sprev"]').filter({ visible: true }).first().count()))) {
    await toggle(q('[data-m="snext"]')).catch(() => {});
    await page.waitForTimeout(1200);
    if (!prev) prev = await tag('sprev', () => [...document.querySelectorAll('button')].find((e) => /previous|prev/i.test(e.getAttribute('aria-label') || e.innerText || '')) || null);
  }
  if (prev) await S('stories-prev', q('[data-m="sprev"]'), B4, { group: g, title: 'Stories previous button', desc: 'The previous-arrow of the customer-stories carousel, shown after the carousel leaves its first slide.', sel: 'the prev arrow button' });
  const pause = await tag('spause', () => [...document.querySelectorAll('button')].find((e) => /pause|play/i.test(e.getAttribute('aria-label') || e.innerText || '')) || null);
  if (pause) await S('stories-pause', q('[data-m="spause"]'), ['default', 'hover', 'focus-visible'], { group: g, title: 'Stories pause button', desc: 'The pause-autoplay button of the customer-stories carousel; measured and focused, never pressed.', sel: 'the pause button' });
  await layoutFor(key);
  await page.close();
}

// ---------- index pages (solutions, enterprise, customer-stories, whatsnew) ----------
async function indexPage(key, g, title, cardKey, cardDesc, cardSel) {
  await newPage(key);
  const h1 = await tag('h1', () => document.querySelector('h1, [role=heading], h2'));
  if (h1) await S(cardKey + '-title', q('[data-m="h1"]'), ['default'], { group: g, title, sel: 'h1' }, { noScroll: true });
  const card = await tag('icard', () => {
    const cands = [...document.querySelectorAll('a, [role=link], [class*="card" i], [class*="Card" i], article, li')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 240 && r.width < 1000 && r.height > 60 && r.height < 700 && r.left >= 0 && r.top > 200 && (e.innerText || '').trim().length > 5;
    });
    return cands.sort((a, b) => a.getBoundingClientRect().top - b.getBoundingClientRect().top)[0] || null;
  });
  if (card) await S(cardKey, q('[data-m="icard"]'), ['default', 'hover'], { group: g, title: cardDesc.split(':')[0], desc: cardDesc, sel: cardSel || 'a linked card in the index' });
  await layoutFor(key);
  await page.close();
}

// ---------- pricing ----------
async function pricing() {
  await newPage('pricing');
  const g = G.pricing;
  const h1 = await tag('h1', () => document.querySelector('h1'));
  if (h1) await S('pricing-title', q('[data-m="h1"]'), ['default'], { group: g, title: 'Pricing title', desc: 'The "A plan for every organization\'s needs" h1.', sel: 'h1' }, { noScroll: true });
  const card = await tag('pcard', () => {
    // /pricing's plan grid sits in a landmark other than <main> on some builds,
    // so scope to the whole document body
    const scope = document.querySelector('main') || document.body;
    const cands = [...scope.querySelectorAll('*')].filter((e) => {
      const r = e.getBoundingClientRect();
      if (!(r.width > 200 && r.width < 500 && r.height > 250)) return false;
      if (!/per month|\/mo|billed|free forever|contact sales|custom pricing/i.test(e.innerText || '')) return false;
      if (!e.querySelector('a, button, [role=button]')) return false;
      // the smallest ancestor chain still holding one whole plan
      return ![...e.children].some((c) => /per month|\/mo|billed|free forever|custom pricing/i.test(c.innerText || '') && c.getBoundingClientRect().width > 200);
    });
    return cands.sort((a, b) => a.innerText.length - b.innerText.length)[0] || null;
  });
  if (card) await S('plan-card', q('[data-m="pcard"]'), ['default'], { group: g, title: 'Plan card', desc: 'A plan column on the pricing grid (Free, Team $20, Business $45, Enterprise Scale).', sel: 'a plan column' });
  if (await tagEl('planc', '^contact sales$|^get started|^sign up|^try for free|^add$', 'main'))
    await S('plan-cta', q('[data-m="planc"]'), B4, { group: g, title: 'Plan CTA', desc: 'A button inside a plan card ("Contact Sales" pill). Measured and focused, never followed.', sel: 'a plan card button' });
  if (await tagEl('seemore', '^see more$|^see less$|^see all features', 'main'))
    await S('plan-see-more', q('[data-m="seemore"]'), B4, { group: g, title: 'See more link', desc: 'The "See more" / "See all features and compare plans" expander. Measured, never followed.', sel: 'a See more link' });
  // The "Compare our plans" feature table: a real table or a grid of role=row
  // rows under a "Compare our plans" heading.
  const table = await tag('ctable', () => {
    const cands = [...document.querySelectorAll('table, [role=table], [role=grid], [class*="table" i], [class*="compare" i], [class*="comparison" i]')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 500 && r.height > 400 && /compare our plans|feature|usage|records|automation/i.test(e.innerText || '');
    });
    if (cands.length) return cands.sort((a, b) => a.getBoundingClientRect().height - b.getBoundingClientRect().height)[0];
    // Fallback: the smallest element holding a "Compare our plans" heading plus many rows
    const all = [...document.querySelectorAll('body *')].filter((e) => {
      const r = e.getBoundingClientRect();
      if (!(r.width > 500 && r.height > 400)) return false;
      const rows = e.querySelectorAll('tr, [role=row]');
      return rows.length >= 5 && /compare our plans/i.test(e.innerText || '');
    });
    return all.sort((a, b) => a.getBoundingClientRect().height - b.getBoundingClientRect().height)[0] || null;
  });
  if (table) {
    await S('compare-table', q('[data-m="ctable"]'), ['default'], { group: g, title: 'Plan comparison table', desc: 'The "Compare our plans" feature table: plan columns against feature rows with checks.', sel: 'the comparison table' });
    const trow = await tag('trow', () => {
      const cands = [...document.querySelectorAll('[data-m="ctable"] tr, [data-m="ctable"] [class*="row" i], [data-m="ctable"] li')].filter((e) => {
        const r = e.getBoundingClientRect();
        return r.width > 500 && r.height > 15 && r.height < 90;
      });
      return cands[0] || null;
    });
    if (trow) await S('compare-table-row', q('[data-m="trow"]'), ['default'], { group: g, title: 'Comparison row', desc: 'A feature row in the comparison table.', sel: 'a table row' });
  }
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
  await layoutFor('pricing');
  await page.close();
}

// ---------- contact-sales form ----------
async function contactSales() {
  await newPage('contact-sales');
  const g = G.contact;
  const h1 = await tag('h1', () => document.querySelector('h1, h2'));
  if (h1) await S('contact-title', q('[data-m="h1"]'), ['default'], { group: g, title: 'Contact page title', desc: 'The "Get in touch with us!" heading over the form.', sel: 'h1' }, { noScroll: true });
  const form = await tag('form', () => {
    // The Marketo <form> renders hidden (mktoHasWidth 0x0); the visible form is the
    // React fields grid. Tag the smallest visible box holding the field rows.
    const cands = [...document.querySelectorAll('main div, main section, main form')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 300 && r.height > 300 && e.querySelectorAll('input').length >= 4;
    });
    return cands.sort((a, b) => a.querySelectorAll('div,section,form').length - b.querySelectorAll('div,section,form').length || a.getBoundingClientRect().width - b.getBoundingClientRect().width)[0] || null;
  });
  if (form) {
    await S('contact-form', q('[data-m="form"]'), ['default'], { group: g, title: 'Contact form', desc: 'The Marketo contact-sales form (a hidden mkto <form> with a visible React fields grid): First/Last name, Work Email, Phone with a country selector, Company Name, Job Title, Country, a message area and Submit. Photographed and focused, never submitted.', sel: 'the fields grid' });
    const lab = await tag('flabel', () => [...document.querySelectorAll('label[class*="_label" i], label')].find((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 40 && r.height > 8 && (e.innerText || '').trim().length > 2;
    }) || null);
    if (lab) await S('field-label', q('[data-m="flabel"]'), ['default'], { group: g, title: 'Field label', desc: 'A floating label inside a field of the form ("* First Name").', sel: 'a label element' });
    const input = q('form input:not([type=checkbox]):not([type=radio]):not([type=hidden]):not([type=submit]):not([type=tel]), main input[type=text], form input[name=FirstName]').filter({ visible: true }).first();
    if (await input.count()) {
      await S('text-field', input, ['default', 'focused', 'filled'], { group: g, title: 'Text field', desc: 'A text input in the form (First name). Focused and filled with sample text that was deleted; nothing was sent.', sel: 'the first text input' });
      await S('text-field-box', input, ['default'], { group: g, title: 'Text field box', desc: 'The same field measured at rest (default only).', sel: 'the first text input' }, { crop: false });
    }
    const phone = q('form input[type=tel], form input[name=Phone]').filter({ visible: true }).first();
    if (await phone.count()) await S('phone-field', phone, ['default', 'focused'], { group: g, title: 'Phone field', desc: 'The phone input beside the country selector.', sel: 'input[type=tel]' });
    const ctry = q('button[class*="country-selector" i], form button[role=combobox]').filter({ visible: true }).first();
    if (await ctry.count()) await S('country-selector', ctry, ['default', 'hover', 'focus-visible'], { group: g, title: 'Country selector', desc: 'The phone country combobox button. Measured and focused, never opened (a choice posts a value).', sel: 'the country selector button' });
    const email = q('form input[type=email], form input[name=Email]').filter({ visible: true }).first();
    if (await email.count()) await S('email-field', email, ['default', 'focused'], { group: g, title: 'Email field', desc: 'The work-email input.', sel: 'input[type=email]' });
    const ta = q('form textarea').filter({ visible: true }).first();
    if (await ta.count()) await S('text-area', ta, ['default', 'focused'], { group: g, title: 'Text area', desc: 'The "How can we help?" message textarea.', sel: 'textarea' });
    // The mkto <select> mirrors stay hidden at 0x0; the visible "Country"
    // dropdown is a custom combobox-styled div with a chevron.
    const csel = await tag('csel', () => {
      const cands = [...document.querySelectorAll('main div, main button, main [role=combobox], form div, body div')].filter((e) => {
        const r = e.getBoundingClientRect();
        return r.width > 200 && r.width < 600 && r.height > 30 && r.height < 110 && /country|how can our team help/i.test((e.innerText || '').trim().slice(0, 60)) && (e.querySelector('svg') || /combobox|select/i.test(String(e.className)));
      });
      return cands.sort((a, b) => a.getBoundingClientRect().width * a.getBoundingClientRect().height - b.getBoundingClientRect().width * b.getBoundingClientRect().height)[0] || null;
    });
    if (csel) {
      await S('select-field', q('[data-m="csel"]'), ['default', 'hover'], { group: g, title: 'Select field', desc: 'The "Country" dropdown in the form (a custom combobox, not a native select). Measured at rest; never submitted.', sel: 'the Country field' });
      await S('select-field-open', q('[data-m="csel"]'), ['default'], { group: g, title: 'Select field, open', desc: 'The Country dropdown clicked open; a local disclosure, nothing chosen.', sel: 'the open dropdown' }, { open: async () => { const inner = q('[data-m="csel"] [class*="-control" i], [data-m="csel"] [role=combobox], [data-m="csel"] button').filter({ visible: true }).first(); await toggle((await inner.count()) ? inner : q('[data-m="csel"]')).catch(() => {}); await page.waitForTimeout(1500); }, openTarget: openMenu('csel'), noReset: true, via: 'clicked the field open; nothing chosen' });
      await page.keyboard.press('Escape').catch(() => {});
    }
    const cb = q('form input[type=checkbox]').filter({ visible: true }).first();
    if (await cb.count()) await S('checkbox', cb, ['default'], { group: g, title: 'Checkbox', desc: 'A checkbox in the form.', sel: 'input[type=checkbox]' });
    const sub = await tag('submit', () => [...document.querySelectorAll('button, [role=button], input[type=submit]')].find((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 100 && r.height > 20 && /^(submit|contact sales)$/i.test((e.innerText || e.value || '').trim());
    }) || null);
    if (sub) await S('submit-button', q('[data-m="submit"]'), ['default', 'hover', 'focus-visible'], { group: g, title: 'Submit button', desc: 'The dark "Submit" of the sales form. Measured and focused, never pressed.', sel: 'the submit button' });
  }
  await layoutFor('contact-sales');
  await page.close();
}

// ---------- templates ----------
async function templates() {
  await newPage('templates');
  const g = G.cards;
  const h1 = await tag('h1', () => document.querySelector('h1'));
  if (h1) await S('templates-title', q('[data-m="h1"]'), ['default'], { group: g, title: 'Templates title', desc: 'The "Templates" h1.', sel: 'h1' }, { noScroll: true });
  const search = q('input[type=search], input[name=q], input[placeholder*="earch" i]').filter({ visible: true }).first();
  if (await search.count()) await S('templates-search', search, ['default', 'focused'], { group: g, title: 'Template search field', desc: 'The "Search templates" field in the filter rail. Focused, nothing typed.', sel: 'input[type=search]' });
  const filt = await tag('filt', () => [...document.querySelectorAll('button')].find((e) => /^by (use case|industry|feature)/i.test((e.innerText || '').trim())) || null);
  if (filt) {
    await S('filter-section', q('[data-m="filt"]'), ['default', 'hover', 'focus-visible'], { group: g, title: 'Filter section', desc: 'A collapsible filter group in the templates rail (By Use Case / By Industry / By Feature).', sel: 'a filter group button' });
    await S('filter-section-open', q('[data-m="filt"]'), ['default'], { group: g, title: 'Filter section, open', desc: 'The filter group clicked open; a local expand.', sel: 'the open filter group' }, { open: async () => { const l = q('[data-m="filt"]').filter({ visible: true }).first(); const exp = await l.evaluate((el) => el.getAttribute('aria-expanded')).catch(() => null); if (exp !== 'true') { await toggle(q('[data-m="filt"]')).catch(() => {}); await page.waitForTimeout(1200); } }, openTarget: openItem('filt'), via: 'clicked the filter group open' });
    const cb = q('[data-m="filt"] + * input[type=checkbox], [data-m="filt"] ~ * input[type=checkbox], form input[type=checkbox], [class*="filter" i] input[type=checkbox]').filter({ visible: true }).first();
    if (await cb.count()) await S('filter-checkbox', cb, ['default'], { group: g, title: 'Filter checkbox', desc: 'A checkbox inside the open filter group.', sel: 'a filter checkbox' });
  }
  const card = await tag('tcard', () => {
    const cands = [...document.querySelectorAll('main a.group, main a[class*="group" i], main a')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 200 && r.height > 80 && r.top > 300 && (e.querySelector('img, video, h2, h3') || /template/i.test(e.innerText || ''));
    });
    return cands.sort((a, b) => a.getBoundingClientRect().top - b.getBoundingClientRect().top)[0] || null;
  });
  if (card) await S('template-card', q('[data-m="tcard"]'), ['default', 'hover'], { group: g, title: 'Template card', desc: 'A linked template card in the gallery (the image-thumb tiles at the top, the text cards below).', sel: 'a template card' });
  await layoutFor('templates');
  await page.close();
}

// ---------- marketplace ----------
async function marketplace() {
  await newPage('marketplace');
  const g = G.cards;
  const h1 = await tag('h1', () => document.querySelector('h1'));
  if (h1) await S('marketplace-title', q('[data-m="h1"]'), ['default'], { group: g, title: 'Marketplace title', desc: 'The "Marketplace" h1.', sel: 'h1' }, { noScroll: true });
  const search = q('input[placeholder*="extension" i], input[type=search], input[type=text]').filter({ visible: true }).first();
  if (await search.count()) await S('marketplace-search', search, ['default', 'focused'], { group: g, title: 'Marketplace search field', desc: 'The "Find an extension" field. Focused, nothing typed.', sel: 'the search input' });
  // One category card ("For marketing teams" / "Page designer" / "Scripting");
  // bounding sizes keep the grid wrapper out (the first pass read it whole).
  const card = await tag('mcard', () => {
    const cands = [...document.querySelectorAll('a, [role=button], [role=link], [class*="card" i]')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 200 && r.width < 700 && r.height > 100 && r.height < 700 && r.left >= 0 && (e.querySelector('img, h2, h3, svg')) && (e.innerText || '').trim().length > 5;
    });
    return cands.sort((a, b) => a.getBoundingClientRect().top + scrollY - (b.getBoundingClientRect().top + scrollY))[0] || null;
  });
  if (card) await S('market-card', q('[data-m="mcard"]'), ['default', 'hover'], { group: g, title: 'Marketplace category card', desc: 'A category card on the marketplace ("Airtable for marketing teams", "Page designer", "Scripting").', sel: 'a category card' });
  if (await tagEl('mcta', '^view all extensions|^view all scripts', 'main'))
    await S('market-cta', q('[data-m="mcta"]'), B4, { group: g, title: 'Marketplace CTA', desc: 'A "View all …" button in the marketplace. Measured and focused, never followed.', sel: 'a View all button' });
  await layoutFor('marketplace');
  await page.close();
}

// ---------- about ----------
async function about() {
  await newPage('about');
  const g = G.home;
  const h1 = await tag('h1', () => document.querySelector('h1'));
  if (h1) await S('about-title', q('[data-m="h1"]'), ['default'], { group: g, title: 'About page title', desc: 'The h1 on /about.', sel: 'h1' }, { noScroll: true });
  const card = await tag('acard', () => {
    const cands = [...document.querySelectorAll('a, [class*="card" i], article')].filter((e) => {
      const r = e.getBoundingClientRect();
      // a card, not a full-width list or grid (the 1342px stats ul matched before)
      return r.width > 240 && r.width < 900 && r.height > 100 && r.top > 400 && !e.matches('ul, ol') && (e.querySelector('img, h2, h3'));
    });
    return cands[0] || null;
  });
  if (card) await S('about-card', q('[data-m="acard"]'), ['default', 'hover'], { group: g, title: 'About page card', desc: 'A card on the about page (values, offices, news).', sel: 'a card' });
  await layoutFor('about');
  await page.close();
}

// ---------- mobile ----------
async function mobile() {
  await newPage('home', { mobile: true });
  const g = G.mobile;
  const promo = q('[data-m="promo"]');
  const nav = await tag('mnav', () => {
    const cands = [...document.querySelectorAll('header, [class*="header" i], nav')].filter((e) => {
      const cs = getComputedStyle(e), r = e.getBoundingClientRect();
      return r.top <= 120 && r.width > 200 && r.height < 160;
    });
    return cands.sort((a, b) => a.getBoundingClientRect().top - b.getBoundingClientRect().top)[0] || null;
  });
  if (nav) await S('m-nav-bar', q('[data-m="mnav"]'), ['default'], { group: g, title: 'Top navigation bar (mobile)', desc: 'The header at 390: wordmark and menu button.', sel: 'the mobile header' }, { noScroll: true });
  // The hamburger: visible, and not the drawer's own hidden back/close buttons.
  const menu = await tag('mmenu', () => [...document.querySelectorAll('button')].find((e) => {
    const r = e.getBoundingClientRect();
    return r.width > 8 && r.height > 8 && /menu|nav/i.test((e.innerText || e.getAttribute('aria-label') || '').trim()) && !/back|close|previous/i.test(e.getAttribute('aria-label') || '');
  }) || null);
  if (menu) {
    await S('m-nav-menu-btn', q('[data-m="mmenu"]'), ['default'], { group: g, title: 'Nav menu button (mobile)', desc: 'The "Open side menu" button in the mobile header. Opened for the screenshot; nothing is followed.', sel: 'the menu button' }, { noScroll: true });
    await toggle(q('[data-m="mmenu"]')).catch(() => {});
    await page.waitForTimeout(2200);
    const sheet = await tag('msheet', () => {
      // The opened drawer is a positioned overlay pinned to the viewport top;
      // an in-flow nav (the footer link columns at top>1000) is not the sheet.
      const cands = [...document.querySelectorAll('[role=dialog], [class*="navDrawer" i], [class*="drawer" i], [class*="sheet" i], [class*="menu" i], [class*="modal" i], nav, aside')].filter((e) => {
        const r = e.getBoundingClientRect(), cs = getComputedStyle(e);
        return r.top <= 200 && (cs.position === 'fixed' || cs.position === 'absolute') && r.height > 200 && r.width > 150 && r.left < 100 && (e.innerText || '').trim().length > 10 && e.querySelectorAll('a, button').length > 2;
      });
      return cands.sort((a, b) => a.getBoundingClientRect().width * a.getBoundingClientRect().height - b.getBoundingClientRect().width * b.getBoundingClientRect().height)[0] || null;
    });
    if (sheet) await S('m-nav-sheet', q('[data-m="msheet"]'), ['default'], { group: g, title: 'Mobile nav sheet', desc: 'The open side drawer at 390.', sel: 'the open menu' }, { noScroll: true, via: 'clicked the menu button' });
    await page.keyboard.press('Escape').catch(() => {});
    await page.waitForTimeout(600);
  }
  const h1 = await tag('mh1', () => document.querySelector('h1'));
  if (h1) await S('m-hero-title', q('[data-m="mh1"]'), ['default'], { group: g, title: 'Hero title (mobile)', desc: 'The h1 at 390.', sel: 'h1' });
  await layoutFor('mobile-home');
  await page.close();
}

const PAGES = {
  home,
  platform: () => platformPage('platform'),
  'platform-ai': () => platformPage('platform-ai'),
  solutions: () => indexPage('solutions', G.platform, 'Solutions page title', 'solutions-card', 'Solutions card: a team tile in the solutions grid (Marketing teams, Product teams, ...).', 'a cardIconCard tile'),
  enterprise: () => indexPage('enterprise', G.platform, 'Enterprise page title', 'enterprise-card', 'Enterprise card: a linked capability card on the enterprise page.', 'a cardLink'),
  pricing, 'contact-sales': contactSales,
  'customer-stories': () => indexPage('customer-stories', G.cards, 'Customer stories title', 'story-card', 'Story row: a linked customer story row on the index.', 'a story row'),
  templates, marketplace,
  whatsnew: () => indexPage('whatsnew', G.cards, 'What\'s new title', 'whatsnew-item', 'What\'s new entry: a linked release card with a badge chip.', 'a release card'),
  about, mobile,
};

const want = process.argv.slice(2).length ? process.argv.slice(2) : Object.keys(PAGES);
const done = new Set(); // pages whose capture ran to the end
for (const k of want) {
  const isMobile = k === 'mobile';
  const l = await launch({ mobile: isMobile });
  context = l.context;
  run = k;
  try { await PAGES[k](); done.add(k); } catch (e) { log('PAGE FAILED', k, String(e.message).split('\n')[0]); }
  out._meta.read = new Date().toLocaleDateString('en-CA'); // the local date of the capture
  save();
  await l.browser.close();
}
// a component a page no longer produces is dropped, so a re-run cannot leave stale entries; a page that
// failed partway keeps its earlier entries, since what it did not reach is not known to be gone
for (const [key, c] of Object.entries(out.components)) if (done.has(c.run) && !touched.has(key)) { delete out.components[key]; log('dropped stale', key); }
save();
log('done ->', OUT);
