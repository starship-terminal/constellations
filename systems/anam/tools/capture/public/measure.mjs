// Measures Anam's components on its public pages, in every state that can be
// reached without signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home api pricing interactive-avatars about research case-studies blog
//        changelog tools get-demo docs-overview docs-api docs-dark mobile.
// Writes raw/components-computed.json (merged, so a subset of pages can be re-run),
// raw/layout.json (the frame of each page) and one crop per component and state
// into components/crops/. raw/measurements.md is then built from the JSON by
// build-measurements.mjs.
//
// anam.ai is a Framer site (hashed classes, data-framer-name on the parts the
// author named); anam.ai/docs is Mintlify (Tailwind classes, data-component-*
// hooks). The app at lab.anam.ai and the "Talk with Sophie" call are never
// touched; the /get-demo form is measured, never submitted.
//
// States:
//   hover          real mouse hover, 450ms settle for transitions
//   focus-visible  keyboard: focus, Shift+Tab, Tab, so the browser sees a keyboard focus
//   pressed        CDP CSS.forcePseudoState [active, hover]; no mouse button is pressed,
//                  so no link or submit button can fire
//   focused        the field clicked into (a text field only)
//   filled         sample text typed into a field, measured, then deleted; Enter is never pressed
//   open           a resting state reached by a UI toggle (a persona chip, a nav
//                  submenu, a docs panel); nothing that submits, calls or signs
//                  in is ever pressed
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, open, closePromo, styleOf, crop, centre, markFixed, RAW } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const LAYOUT_OUT = path.join(RAW, 'layout.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
// Older runs saved the camelCase page keys; map them to the URLS keys PAGES now uses, so the
// stale-entry cleanup (done.has(c.run)) still covers readings an older run wrote.
const OLD_RUN = { getDemo: 'get-demo', docsOverview: 'docs-overview', docsApi: 'docs-api', docsDark: 'docs-dark' };
for (const c of Object.values(out.components || {})) if (OLD_RUN[c.run]) c.run = OLD_RUN[c.run];
const layout = fs.existsSync(LAYOUT_OUT) ? JSON.parse(fs.readFileSync(LAYOUT_OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => { fs.mkdirSync(RAW, { recursive: true }); fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n'); };
const saveLayout = () => { fs.mkdirSync(RAW, { recursive: true }); fs.writeFileSync(LAYOUT_OUT, JSON.stringify(layout, null, 1) + '\n'); };

const URLS = {
  home: '/', api: '/api', pricing: '/pricing', 'interactive-avatars': '/interactive-avatars',
  about: '/about', research: '/research', 'case-studies': '/case-studies', blog: '/blog',
  changelog: '/changelog', tools: '/tools', 'get-demo': '/get-demo',
  'docs-overview': '/docs/introduction/overview', 'docs-api': '/docs/api-reference/overview',
  'docs-dark': '/docs/introduction/overview',
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
  log('open', key, mobile ? '(mobile)' : '', BASE + URLS[key]);
  await open(page, BASE + URLS[key], { wait, promo });
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

// Clicks a UI toggle (a persona chip, a tab, a menu button, a docs theme item).
// Refuses a submit button and any control whose text names an action this kit
// must never take.
const NEVER = /^(send|submit|sign in|log in|create|generate|upload|get started|start|start building|start free trial|upgrade|subscribe|talk with|unmute|call|accept all|reject all|manage cookies|cookie settings|request demo|get a demo|book|join|pick an avatar|or upload|choose from|explore interactive avatars|experience the platform|read docs|read our research|connect|open|share)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
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

const FILL = 'a voice agent for a clinic';

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
        // A failed focus is not a focus reading: record the failed attempt,
        // never the resting styles under a focus-visible label.
        if (via === 'focus failed') {
          out.components[key].states[st] = { error: 'keyboard focus could not be moved to the element', via };
          log('  !', key, st, 'focus failed');
          continue;
        }
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

// Tags the first element matching an in-page probe so a locator can find it:
// await tag('nav', () => {...return element or null...}) then q('[data-m="nav"]').
// Extra args are forwarded to the probe inside the page — a closure like a
// RegExp built in Node does NOT exist in the browser and throws ReferenceError.
async function tag(name, probe, ...args) {
  return page.evaluate(([n, src, a]) => {
    const el = (new Function('return (' + src + ')')())(...a);
    for (const old of document.querySelectorAll(`[data-m="${n}"]`)) old.removeAttribute('data-m');
    if (!el) return false;
    el.setAttribute('data-m', n);
    return true;
  }, [name, probe.toString(), args]).catch(() => false);
}

// Tags the smallest element whose trimmed text matches reSrc inside scopeSel,
// preferring an interactive tag or a cursor:pointer box. Framer renders its
// tabs and chips as styled divs, so role selectors alone miss them.
async function tagEl(name, reSrc, scopeSel) {
  return page.evaluate(([n, src, scope]) => {
    const re = new RegExp(src, 'i');
    const sc = scope ? document.querySelector(scope) : document;
    if (!sc) return false; // the scope (an open menu) is gone: never fall back to the whole page
    const cands = [...sc.querySelectorAll('a,button,[role=button],[role=tab],li,div,span')].filter((e) => {
      const t = (e.innerText || e.getAttribute('aria-label') || '').trim(); const r = e.getBoundingClientRect();
      return re.test(t) && t.length < 80 && r.width > 10 && r.height > 8;
    }).sort((a, b) => (a.innerText || '').length - (b.innerText || '').length);
    const el = cands.find((e) => e.matches('a,button,[role=button],[role=tab],li,[tabindex]') || getComputedStyle(e).cursor === 'pointer') || cands[0];
    for (const old of document.querySelectorAll(`[data-m="${n}"]`)) old.removeAttribute('data-m');
    if (!el) return false;
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
      .map((e) => ({ el: e.tagName.toLowerCase() + (e.getAttribute('data-framer-name') ? '.' + e.getAttribute('data-framer-name') : ''), pos: getComputedStyle(e).position, top: +e.getBoundingClientRect().top.toFixed(0), w: +e.getBoundingClientRect().width.toFixed(0), h: +e.getBoundingClientRect().height.toFixed(0), text: (e.innerText || '').trim().slice(0, 60), backdrop: getComputedStyle(e).backdropFilter !== 'none' ? getComputedStyle(e).backdropFilter : undefined })).slice(0, 12);
    const maxWidths = [...document.querySelectorAll('main *, body > * > *')].filter(vis).map((e) => ({ w: +e.getBoundingClientRect().width.toFixed(0), max: getComputedStyle(e).maxWidth }))
      .filter((m) => m.max !== 'none' && parseFloat(m.max) > 200).slice(0, 8);
    const grids = [...document.querySelectorAll('body *')].filter((e) => getComputedStyle(e).display === 'grid' && vis(e)).map((e) => {
      const cs = getComputedStyle(e);
      return { el: e.tagName.toLowerCase() + (e.getAttribute('data-framer-name') ? '.' + e.getAttribute('data-framer-name') : ''), cols: cs.gridTemplateColumns.slice(0, 90), colGap: cs.columnGap, rowGap: cs.rowGap, w: +e.getBoundingClientRect().width.toFixed(0) };
    }).filter((g) => g.cols.split(' ').length > 1).slice(0, 8);
    return { vw, vh, docH: document.documentElement.scrollHeight, fixed, maxWidths, grids };
  }).catch((e) => ({ error: String(e).slice(0, 200) }));
  saveLayout();
}

// ---------- groups ----------
const G = {
  shell: 'Shell and navigation', home: 'Home', features: 'Feature sections',
  pricing: 'Pricing', demo: 'Demo request form', cards: 'Cards and lists',
  docs: 'Docs (Mintlify)', overlay: 'Panels and dialogs', mobile: 'Mobile (390 wide)',
};
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];

// ---------- marketing (Framer) ----------

// The fixed pill nav every marketing page carries: logo, section links, Sign
// in, the Get started CTA.
async function shell() {
  const g = G.shell;
  const nav = await tag('nav', () => {
    const cands = [...document.querySelectorAll('body *')].filter((e) => {
      const cs = getComputedStyle(e), r = e.getBoundingClientRect();
      return (cs.position === 'fixed' || cs.position === 'sticky') && r.top <= 80 && r.width > 500 && r.height < 140 && /sign in|developers|pricing/i.test(e.innerText || '');
    });
    return cands.sort((a, b) => a.getBoundingClientRect().height * a.getBoundingClientRect().width - b.getBoundingClientRect().height * b.getBoundingClientRect().width)[0] || null;
  });
  if (nav) {
    await S('nav-bar', q('[data-m="nav"]'), ['default'], { group: g, title: 'Top navigation bar', desc: 'The floating pill nav on every marketing page: the Anam logo, the section links (Developers, Pricing, Resources, Company), Sign in and the Get started button.', sel: 'the fixed nav container' }, { noScroll: true });
    if (await tagEl('navlink', '^pricing$', '[data-m="nav"]'))
      await S('nav-link', q('[data-m="navlink"]'), B4, { group: g, title: 'Nav link', desc: 'A section link in the pill nav. Measured, never followed.', sel: '"Pricing" inside the nav' }, { noScroll: true });
    if (await tagEl('navcta', '^get started|^sign up', '[data-m="nav"]'))
      await S('nav-cta', q('[data-m="navcta"]'), B4, { group: g, title: 'Nav CTA button', desc: 'The "Get started" button, the nav\u2019s primary action (links to lab.anam.ai/register). Measured and focused, never followed.', sel: '"Get started" inside the nav' }, { noScroll: true });
    if (await tagEl('navsign', '^sign in$', '[data-m="nav"]'))
      await S('nav-signin', q('[data-m="navsign"]'), ['default', 'hover', 'focus-visible'], { group: g, title: 'Sign in link', desc: 'The quiet "Sign in" action (lab.anam.ai/login). Measured, never followed.', sel: '"Sign in" inside the nav' }, { noScroll: true });
    // The Developers/Resources/Company items open a ContentSubMenu on hover.
    const sub = await tagEl('navdev', '^developers|^resources|^company', '[data-m="nav"]');
    if (sub) {
      await q('[data-m="navdev"]').hover({ timeout: 4000 }).catch(() => {});
      await page.waitForTimeout(1400);
      const menu = await tag('submenu', () => {
        const cands = [...document.querySelectorAll('body *')].filter((e) => {
          const r = e.getBoundingClientRect();
          return r.top > 40 && r.top < 160 && r.width > 200 && r.height > 100 && /documentation|changelog|tools|blog|team|research|security/i.test(e.innerText || '') && e.querySelector('a');
        });
        return cands.sort((a, b) => a.innerText.length - b.innerText.length)[0] || null;
      });
      if (menu) await S('nav-submenu', q('[data-m="submenu"]'), ['default'], { group: g, title: 'Nav submenu', desc: 'The dropdown that opens under a nav section on hover (Developers: Documentation, Tools, Changelog; Company: Team, Research, Security). Shown in its hover-open state.', sel: 'the open ContentSubMenu' }, { noScroll: true, noReset: true, via: 'hover over the nav item' });
      // S() resets the pointer when it returns, which closes the hover menu: reopen it
      await q('[data-m="navdev"]').hover({ timeout: 4000 }).catch(() => {});
      await page.waitForTimeout(1000);
      if (await tagEl('sublink', 'documentation|changelog|^blog$', '[data-m="submenu"]'))
        await S('nav-sub-link', q('[data-m="sublink"]'), ['default', 'hover', 'focus-visible'], { group: g, title: 'Submenu link', desc: 'A row inside the open nav dropdown. Measured, never followed.', sel: 'a link inside the submenu' }, { noScroll: true, noReset: true });
      await page.mouse.move(720, 500);
      await page.waitForTimeout(600);
    }
  }
  const foot = await tag('foot', () => {
    const cands = [...document.querySelectorAll('footer, [data-framer-name="Footer"], body > div:last-of-type')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 500 && r.height > 200 && /privacy|terms|linkedin|github|x\.com|youtube|slack/i.test(e.innerText || '');
    });
    return cands.sort((a, b) => b.getBoundingClientRect().height - a.getBoundingClientRect().height)[0] || null;
  });
  if (foot) {
    await S('footer', q('[data-m="foot"]'), ['default'], { group: g, title: 'Footer', desc: 'The page footer: product/company/legal link columns, socials and the status line.', sel: 'the footer block' });
    if (await tagEl('footlink', 'privacy|terms|acceptable use', '[data-m="foot"]'))
      await S('footer-link', q('[data-m="footlink"]'), ['default', 'hover', 'focus-visible'], { group: g, title: 'Footer link', desc: 'A quiet link in the footer columns. Measured, never followed.', sel: 'a legal link inside the footer' });
  }
}

async function home() {
  await newPage('home', { promo: 'keep' });
  await sheetsFor('home');
  // the consent card first, in place, then swept for the rest of the page
  const cc = await tag('ccard', () => document.querySelector('.anam-cc-card'));
  if (cc) {
    await S('consent-card', q('[data-m="ccard"]'), ['default'], { group: G.overlay, title: 'Cookie consent card', desc: 'The .anam-cc-card consent card pinned bottom-right on a fresh profile (Manage cookies / Reject all / Accept all). Photographed and measured in place, then hidden without a click: a consent choice is a submission.', sel: '.anam-cc-card' }, { noScroll: true });
    if (await tagEl('ccmanage', 'manage cookies', '[data-m="ccard"]'))
      await S('consent-manage', q('[data-m="ccmanage"]'), ['default', 'hover', 'focus-visible'], { group: G.overlay, title: 'Manage cookies button', desc: 'The text button in the consent card. Measured and focused, never pressed.', sel: '"Manage cookies" in .anam-cc-card' }, { noScroll: true });
    if (await tagEl('ccaccept', 'accept all', '[data-m="ccard"]'))
      await S('consent-accept', q('[data-m="ccaccept"]'), ['default', 'hover', 'focus-visible'], { group: G.overlay, title: 'Accept all button', desc: 'The filled choice button in the consent card. Measured and focused, never pressed: accepting is a submission.', sel: '"Accept all" in .anam-cc-card' }, { noScroll: true });
  }
  await closePromo(page);
  await markFixed(page);
  await layoutFor('home');
  await shell();
  const g = G.home;

  await S('hero-title', q('h1').first(), ['default'], { group: g, title: 'Hero title', desc: '"Create interactive avatars for\u2026" \u2014 the display line the home page opens with (the last word rotates through personas).', sel: 'h1' }, { noScroll: true });
  await S('hero-sub', q('h1').first().locator('xpath=ancestor::*[.//p or .//a][1]').locator('xpath=.//*[self::p or self::div][string-length(normalize-space())>40][1]').first().or(q('h1').locator('..').locator('p').first()), ['default'], { group: g, title: 'Hero subline', sel: 'the paragraph under the h1' }, { crop: false, noScroll: true });
  if (await tagEl('herocta', '^get started|^start building', 'main, body'))
    await S('hero-cta', q('[data-m="herocta"]'), B4, { group: g, title: 'Hero CTA button', desc: 'The primary button under the hero copy. Links to lab.anam.ai/register; measured, never followed.', sel: '"Get started"/"Start building" near the hero' }, { noScroll: true });

  // The persona carousel under the hero: five div[role=button] cards that pick
  // which avatar the demo card would reach (Mia, Anne, Richard, Liv, Gabriel).
  // The carousel re-renders on its timer, so the tag is re-applied to a fresh
  // card before every state.
  const chipProbe = () => {
    const cands = [...document.querySelectorAll('[role=button]')].filter((e) => {
      const r = e.getBoundingClientRect();
      const onscreen = r.left > -40 && r.right < innerWidth + 40 && r.top > -40;
      return /^(sales|customer-support|skill-training|language-tutor|medical-services)/i.test((e.innerText || '').trim()) && r.width > 100 && r.height > 60;
    });
    // the carousel parks unshown cards off-screen; prefer a painted one
    return cands.find((e) => { const r = e.getBoundingClientRect(); return r.left > -40 && r.right < innerWidth + 40 && r.top > -40 && r.top < innerHeight + 400; }) || cands[0] || null;
  };
  const retagChip = async () => { await tag('pchip', chipProbe); return 're-tagged a fresh card'; };
  if (await tag('pchip', chipProbe)) {
    await S('persona-chip', q('[data-m="pchip"]'), B4, { group: g, title: 'Persona chip', desc: 'One of the persona selector cards under the hero demo (Mia medical services, Anne skills training, Richard customer support, Liv sales, Gabriel language tutor). Pressed is forced; a real press only swaps the persona the demo card names.', sel: 'a [role=button] persona card' }, { before: { hover: retagChip, 'focus-visible': retagChip, pressed: retagChip } });
    // select one and measure the selected style
    const sel2 = await tag('pchip2', () => {
      const cands = [...document.querySelectorAll('[role=button]')].filter((e) => { const r = e.getBoundingClientRect(); return /^(sales|customer-support|skill-training|language-tutor|medical-services)/i.test((e.innerText || '').trim()) && r.width > 100 && r.left > -40 && r.right < innerWidth + 40; });
      const el = cands[1] || cands[0];
      if (el) { el.scrollIntoView({ block: 'center' }); el.click(); el.setAttribute('data-m', 'pchip2'); }
      return el || null;
    });
    if (sel2) {
      await page.waitForTimeout(1200);
      await S('persona-chip-selected', q('[data-m="pchip2"]'), ['default'], { group: g, title: 'Persona chip, selected', desc: 'The same chip after a press, in its selected state (the demo card now names that persona).', sel: 'a pressed persona card' }, { via: 'a press on the chip (a local selection toggle)' });
    }
  }
  // The "Talk with …" demo card: the smallest ON-SCREEN element still holding
  // the text (the carousel keeps the other personas' cards parked off-screen).
  const demo = await tag('demo', () => {
    const cands = [...document.querySelectorAll('body *')].filter((e) => {
      const r = e.getBoundingClientRect();
      return /^talk with/i.test((e.innerText || '').trim()) && r.width > 250 && r.width < 700 && r.height > 140 && r.height < 600 && r.left > -20 && r.right < innerWidth + 20 && r.top > -20 && r.top < innerHeight;
    });
    return cands.sort((a, b) => a.getBoundingClientRect().width * a.getBoundingClientRect().height - b.getBoundingClientRect().width * b.getBoundingClientRect().height)[0] || null;
  });
  if (demo) {
    await S('demo-card', q('[data-m="demo"]'), ['default'], { group: g, title: 'Avatar demo card', desc: 'The "Talk with \u2026" card under the hero: the avatar preview, the persona name and the call controls. The call button starts a live avatar session with microphone access, so it is measured inside the card and never pressed.', sel: 'the visible Talk-with card' });
    const call = await tag('callbtn', () => {
      // The "Talk with <name>" call control sits beside the demo card, not inside it.
      const cands = [...document.querySelectorAll('button, [role=button]')].filter((b) => {
        const r = b.getBoundingClientRect();
        return /^talk with/i.test((b.innerText || '').trim()) && r.width > 80 && r.width < 300 && r.height > 24 && r.height < 80;
      });
      return cands[0] || document.querySelector('button[aria-label=call]') || null;
    });
    if (call) await S('demo-cta', q('[data-m="callbtn"]'), ['default', 'hover', 'focus-visible'], { group: g, title: 'Demo call button', desc: 'The "Talk with <persona>" call control beside the demo card. Hovered and focused, never pressed: a press opens a session on Anam\u2019s servers and asks for the microphone.', sel: 'the "Talk with …" call button under the demo card' });
  }
  // A tab strip (the TabSection carousel: "Human realism", "Expression control", …)
  const tabsec = await tag('tabsec', () => {
    const cands = [...document.querySelectorAll('[data-framer-name]')].filter((e) => /tabsection|^tabs$/i.test(e.getAttribute('data-framer-name')) && e.getBoundingClientRect().width > 300);
    return cands[0] || null;
  });
  if (tabsec) {
    await S('tab-section', q('[data-m="tabsec"]'), ['default'], { group: g, title: 'Feature tab section', desc: 'The scroll-driven tab showcase (TabSection): a tab per feature with a video or metric card beside it.', sel: '[data-framer-name=TabSection]' });
    if (await tagEl('tabitem', 'expression control|image-to-avatar|human realism', '[data-m="tabsec"]'))
      await S('tab-item', q('[data-m="tabitem"]'), ['default', 'hover', 'focus-visible'], { group: g, title: 'Feature tab', desc: 'A tab label inside the showcase. Measured, never pressed: the section advances on scroll.', sel: 'a tab inside TabSection' });
  }
  // A feature/metric card lower down the page.
  const feat = await tag('feat', () => {
    const named = [...document.querySelectorAll('[data-framer-name]')].filter((e) => /^feature$|^metrics$|^stats$/i.test(e.getAttribute('data-framer-name')) && e.getBoundingClientRect().width > 200);
    if (named.length) return named[0];
    const h = [...document.querySelectorAll('h2, h3')].find((x) => /latency|concurrency|uptime|fastest/i.test(x.innerText || ''));
    return h ? h.parentElement.parentElement : null;
  });
  if (feat) await S('feature-card', q('[data-m="feat"]'), ['default'], { group: G.features, title: 'Feature card', desc: 'A metrics/feature block from the latency or platform sections (a claim, its value and a diagram or video).', sel: 'a [data-framer-name=Feature|Metrics] block' });
  const logos = await tag('logos', () => [...document.querySelectorAll('[data-framer-name]')].find((e) => /logos carousel|customers/i.test(e.getAttribute('data-framer-name')) && e.getBoundingClientRect().width > 300) || null);
  if (logos) await S('logo-cloud', q('[data-m="logos"]'), ['default'], { group: G.features, title: 'Customer logo cloud', desc: 'The customer logo strip that scrolls on a loop.', sel: '[data-framer-name="Logos Carousel"|Customers]' });
  const ctaband = await tag('ctaband', () => {
    const cands = [...document.querySelectorAll('body *')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 500 && r.width <= 1440 && r.height > 60 && r.height < 500 && /build the future/i.test(e.innerText || '') && (e.querySelector('a, [role=button], button') || /get started|start building/i.test(e.innerText || ''));
    });
    return cands.sort((a, b) => a.getBoundingClientRect().width * a.getBoundingClientRect().height - b.getBoundingClientRect().width * b.getBoundingClientRect().height)[0] || null;
  });
  if (ctaband) await S('cta-band', q('[data-m="ctaband"]'), ['default'], { group: g, title: 'Sticky CTA band', desc: 'The "Build the future of customer experience. Today." band pinned at the foot of the page, with a Get started button.', sel: 'the bottom sticky CTA' }, { noScroll: true });
  await page.close();
}

async function api() {
  await newPage('api');
  await layoutFor('api');
  await shell();
  const g = G.features;
  await S('api-title', q('h1').first(), ['default'], { group: g, title: 'API page title', sel: 'h1' }, { noScroll: true });
  // The developer page shows code blocks with a Copy code button.
  const code = await tag('code', () => {
    const cands = [...document.querySelectorAll('pre, code, [class*=code], [data-framer-name]')].filter((e) => {
      const r = e.getBoundingClientRect(), t = e.innerText || '';
      return r.width > 200 && r.height > 40 && /npm|install|import|curl|token|const |npm i|pnpm/i.test(t) && t.length < 3000;
    });
    return cands.sort((a, b) => a.innerText.length - b.innerText.length)[0] || null;
  });
  if (code) {
    await S('code-block', q('[data-m="code"]'), ['default'], { group: g, title: 'Code block', desc: 'A developer code sample (install or API call) with syntax colouring and a Copy code button.', sel: 'a pre/code sample block' });
    if (await tagEl('copycode', 'copy code|^copy', 'main, body'))
      await S('copy-code', q('[data-m="copycode"]'), B4, { group: g, title: 'Copy code button', desc: 'Copies the sample. Measured, never pressed.', sel: '"Copy code" beside a sample' });
  }
  const card = await tag('apicard', () => {
    const cands = [...document.querySelectorAll('main *, body *')].filter((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 240 && r.width < 700 && r.height > 140 && r.height < 560 && e.querySelector('h3, h4') && e.querySelector('p');
    });
    return cands.sort((a, b) => a.getBoundingClientRect().width - b.getBoundingClientRect().width)[0] || null;
  });
  if (card) await S('api-feature-card', q('[data-m="apicard"]'), ['default'], { group: g, title: 'API feature card', desc: 'A capability card on the developers page (a heading, body copy and often a link or diagram).', sel: 'a feature card on /api' });
  await page.close();
}

async function pricing() {
  await newPage('pricing');
  await layoutFor('pricing');
  await shell();
  const g = G.pricing;
  await S('pricing-title', q('h1').first(), ['default'], { group: g, title: 'Pricing title', sel: 'h1' }, { noScroll: true });
  const tog = await tag('btog', () => {
    const cands = [...document.querySelectorAll('button, [role=switch], [role=tab], [role=button], div')].filter((e) => {
      const t = (e.innerText || '').trim(); const r = e.getBoundingClientRect();
      return /annual|yearly|monthly|month/i.test(t) && t.length < 80 && r.width > 60 && r.width < 420 && r.height < 80;
    });
    return cands.sort((a, b) => a.innerText.length - b.innerText.length)[0] || null;
  });
  if (tog) await S('billing-toggle', q('[data-m="btog"]'), ['default', 'hover', 'focus-visible'], { group: g, title: 'Billing period toggle', desc: 'The monthly/annual period switch above the plan cards. A local toggle; the capture presses it once on the screenshot pass.', sel: 'the billing period control' });
  const pc = await tag('pcard', () => {
    const cands = [...document.querySelectorAll('main *, body *')].filter((e) => {
      const r = e.getBoundingClientRect(), t = (e.innerText || '');
      return r.width > 220 && r.width < 560 && r.height > 200 && /\/mo|month|free|concurrency|credit|minute|usage/i.test(t) && (e.querySelector('a, button') || e.querySelector('[role=button]'));
    });
    return cands.sort((a, b) => a.getBoundingClientRect().width - b.getBoundingClientRect().width || (a.innerText || '').length - (b.innerText || '').length).filter((e) => !cands.some((o) => o !== e && e.contains(o)))[0] || null;
  });
  if (pc) {
    await S('plan-card', q('[data-m="pcard"]'), ['default'], { group: g, title: 'Plan card', desc: 'A pricing plan card: name, price, included usage and a call-to-action button.', sel: 'a pricing plan card' });
    const cta = await tag('pcta', () => {
      const card = document.querySelector('[data-m="pcard"]');
      return card && [...card.querySelectorAll('a, button, [role=button]')].filter((b) => ((b.innerText || '').trim().length > 1) && (b.innerText || '').trim().length < 40).pop() || null;
    });
    if (cta) await S('plan-cta', q('[data-m="pcta"]'), B4, { group: g, title: 'Plan CTA button', desc: 'The call-to-action inside a plan card. Pressed is forced; a real press leads to checkout on lab.anam.ai.', sel: 'a button inside a plan card' });
  }
  const faq = await tag('faq', () => {
    const cands = [...document.querySelectorAll('details, [role=button], [data-framer-name]')].filter((e) => {
      const t = (e.innerText || ''); const r = e.getBoundingClientRect();
      return t.length > 10 && t.length < 400 && r.width > 300 && /\?/.test(t) && e.getBoundingClientRect().top > 400;
    });
    return cands.sort((a, b) => a.innerText.length - b.innerText.length)[0] || null;
  });
  if (faq) await S('faq-item', q('[data-m="faq"]'), ['default'], { group: g, title: 'FAQ item', desc: 'A question-and-answer row in the pricing FAQ.', sel: 'an FAQ entry' });
  await page.close();
}

async function gallery(key, headingRe, cardRe, compKey, title, desc) {
  await newPage(key);
  await layoutFor(key);
  await shell();
  const g = G.cards;
  await S(`${compKey}-title`, q('h1').first(), ['default'], { group: g, title: `${title} title`, sel: 'h1' }, { noScroll: true });
  const card = await tag('gcard', (reSrc, reFlags) => {
    const cardRe = new RegExp(reSrc, reFlags);
    // Inside the page body only: the nav's Company/Developers submenu stays
    // mounted in the header and is not a card.
    const root = document.querySelector('main') || document.body;
    const cands = [...root.querySelectorAll('a, article, [data-framer-name]')].filter((e) => {
      const r = e.getBoundingClientRect();
      return !e.closest('header, nav, [role="navigation"], footer') && (e.querySelector('img, video') || cardRe.test(e.innerText || '')) && r.width > 200 && r.width < 900 && r.height > 100 && r.top > 60;
    });
    return cands.sort((a, b) => a.getBoundingClientRect().top - b.getBoundingClientRect().top || a.getBoundingClientRect().left - b.getBoundingClientRect().left)[0] || null;
  }, cardRe.source, cardRe.flags);
  // S() records the component as missing when nothing was tagged.
  await S(compKey, q('[data-m="gcard"]'), ['default', 'hover', 'focus-visible'], { group: g, title, desc, sel: card ? `the first card on ${URLS[key]}` : `no card found on ${URLS[key]}` });
  await page.close();
}

async function getDemo() {
  await newPage('get-demo');
  await layoutFor('get-demo');
  const g = G.demo;
  await S('demo-title', q('h1, h2').first(), ['default'], { group: g, title: 'Demo page title', sel: 'h1/h2' }, { noScroll: true });
  const form = await tag('form', () => document.querySelector('form'));
  if (form) {
    await S('demo-form', q('[data-m="form"]'), ['default'], { group: g, title: 'Demo request form', desc: 'The get-demo lead form: name, work email and a message box plus a submit. Every field was measured; nothing was filled or sent.', sel: 'form' });
    const lab = await tag('flabel', () => {
      const f = document.querySelector('[data-m="form"]') || document;
      return [...f.querySelectorAll('label, [data-framer-name]')].find((e) => (e.innerText || '').trim().length > 2 && (e.innerText || '').trim().length < 40) || null;
    });
    if (lab) await S('form-label', q('[data-m="flabel"]'), ['default'], { group: g, title: 'Field label', sel: 'a label inside the form' });
    const inputs = q('[data-m="form"]').locator('input[type=text], input:not([type]), input[type=email]');
    if (await inputs.count()) {
      await S('form-input', inputs.first(), ['default', 'focused', 'filled'], { group: g, title: 'Text field', desc: 'A text input in the demo form. Sample text was typed and deleted; nothing was submitted.', sel: 'the first text input in the form' }, { fieldLoc: inputs.first(), crop: false });
      await S('form-input-box', inputs.first().locator('xpath=ancestor::*[contains(@class,"field") or contains(@class,"input") or position()=2][1]'), ['default'], { group: g, title: 'Text field box', sel: 'the input or its padded wrapper' });
    }
    const ta = q('[data-m="form"]').locator('textarea');
    if (await ta.count()) await S('form-textarea', ta.first(), ['default', 'focused'], { group: g, title: 'Text area', desc: 'The message box. Clicked into, never filled.', sel: 'textarea' }, { fieldLoc: ta.first(), crop: false });
    const sub = await tag('fsub', () => {
      const f = document.querySelector('form');
      return f && [...f.querySelectorAll('button, input[type=submit], [role=button], a')].filter((b) => /submit|send|request|book|get|demo/i.test(b.innerText || b.value || b.getAttribute('aria-label') || '')).pop() || null;
    });
    if (sub) await S('form-submit', q('[data-m="fsub"]'), ['default', 'hover', 'focus-visible'], { group: g, title: 'Submit button', desc: 'The form\u2019s submit. Measured and hovered, never pressed: a press sends the lead form.', sel: 'the submit control in the form' });
  }
  await page.close();
}

// ---------- docs (Mintlify) ----------

async function docsChrome() {
  const g = G.docs;
  const side = await tag('dside', () => document.querySelector('#sidebar, [id*=sidebar]') || [...document.querySelectorAll('nav')].find((n) => n.getBoundingClientRect().width > 180 && n.getBoundingClientRect().height > 400) || null);
  if (side) {
    await S('docs-sidebar', q('[data-m="dside"]'), ['default'], { group: g, title: 'Docs sidebar', desc: 'The left navigation tree on the Mintlify docs (section groups, page links, POST/GET method badges on the API reference).', sel: '#sidebar' }, { noScroll: true });
    if (await tagEl('dsidelink', '^models$|^personas$|^voices$|^sessions$', '[data-m="dside"]'))
      await S('docs-nav-link', q('[data-m="dsidelink"]'), ['default', 'hover', 'focus-visible'], { group: g, title: 'Sidebar link', desc: 'A page link inside a sidebar group. Measured, never followed.', sel: 'a link inside the sidebar' }, { noScroll: true });
  }
  const active = await tag('dactive', () => document.querySelector('#sidebar [aria-current=page], #sidebar .active, #sidebar [data-active=true], nav [aria-current=page]') || null);
  if (active) await S('docs-nav-active', q('[data-m="dactive"]'), ['default'], { group: g, title: 'Sidebar link, current page', desc: 'The link for the open page, in its selected style.', sel: '[aria-current=page] in the sidebar' }, { noScroll: true });
  const top = await tag('dtoplink', () => [...document.querySelectorAll('header a, nav a')].find((a) => /api reference|documentation|overview/i.test(a.innerText || '') && a.getBoundingClientRect().top < 80) || null);
  if (top) await S('docs-topnav-link', q('[data-m="dtoplink"]'), ['default', 'hover', 'focus-visible'], { group: g, title: 'Top nav tab', desc: 'A section tab in the docs top bar (Documentation / API Reference).', sel: 'a top-nav link' }, { noScroll: true });
  const search = await tag('dsearch', () => [...document.querySelectorAll('button')].find((b) => /search/i.test(b.innerText || b.getAttribute('aria-label') || '') && b.getBoundingClientRect().top < 90) || null);
  if (search) await S('docs-search-btn', q('[data-m="dsearch"]'), B4, { group: g, title: 'Search button', desc: 'The "Search\u2026 \u2318K" pill in the docs bar. Pressed is forced; a real press opens the search dialog.', sel: 'the Search button' }, { noScroll: true });
  const assist = await tag('dassist', () => document.querySelector('#assistant-entry') || [...document.querySelectorAll('button')].find((b) => { const r = b.getBoundingClientRect(); return /ask assistant/i.test((b.innerText || '') + ' ' + (b.getAttribute('aria-label') || '')) && r.top < 90 && r.left >= 0 && r.left < innerWidth && r.width > 10; }) || null);
  if (assist) await S('docs-assistant-btn', q('[data-m="dassist"]'), B4, { group: g, title: 'Ask Assistant button', desc: 'Opens the AI assistant panel (\u2318I). Pressed is forced; the panel was opened by keyboard for its own entry.', sel: 'the Ask Assistant button' }, { noScroll: true });
  const theme = await tag('dtheme', () => document.querySelector('#theme-preference-menu-trigger, [data-component-name=theme-preference-menu] button') || null);
  if (theme) await S('docs-theme-btn', q('[data-m="dtheme"]'), ['default', 'hover', 'focus-visible'], { group: g, title: 'Theme menu button', desc: 'The "Change theme preference" menu trigger. A local toggle; the dark run pressed it once.', sel: '#theme-preference-menu-trigger' }, { noScroll: true });
  const toc = await tag('dtoc', () => document.querySelector('#content-side-layout') || [...document.querySelectorAll('aside, nav')].find((n) => /on this page/i.test(n.innerText || '')) || null);
  if (toc) {
    await S('docs-toc', q('[data-m="dtoc"]'), ['default'], { group: g, title: 'On-this-page rail', desc: 'The sticky right-hand table of contents.', sel: '#content-side-layout' }, { noScroll: true });
    if (await tagEl('dtoclink', '.', '[data-m="dtoc"]'))
      await S('docs-toc-link', q('[data-m="dtoclink"]'), ['default', 'hover', 'focus-visible'], { group: g, title: 'TOC link', sel: 'a link inside the TOC rail' }, { noScroll: true });
  }
}

async function docsOverview() {
  await newPage('docs-overview');
  await sheetsFor('docs-overview');
  await layoutFor('docs-overview');
  await docsChrome();
  const g = G.docs;
  await S('docs-h1', q('main h1, h1').first(), ['default'], { group: g, title: 'Docs page title', desc: '"Anam Documentation" in the docs display type.', sel: 'main h1' }, { noScroll: true });
  const para = await tag('dpara', () => [...document.querySelectorAll('main p, article p')].find((x) => (x.innerText || '').trim().length > 60) || null);
  if (para) await S('docs-body', q('[data-m="dpara"]'), ['default'], { group: g, title: 'Body text', sel: 'a main paragraph' }, { crop: false });
  // One painted card, not the three-column grid holding them: Mintlify cards
  // are div.card.block / a.card elements ~219x230 at radius 16.
  const card = await tag('dcard', () => [...document.querySelectorAll('main .card, article .card, main a.card')].find((e) => {
    const r = e.getBoundingClientRect();
    return r.width > 100 && r.width < 500 && r.height > 80;
  }) || [...document.querySelectorAll('main a')].find((e) => e.getBoundingClientRect().width > 200 && e.getBoundingClientRect().height > 60) || null);
  if (card) await S('docs-card', q('[data-m="dcard"]'), B4, { group: g, title: 'Docs link card', desc: 'A card linking to another docs page (the "Learn" cards). Measured, never followed.', sel: '.card in main' });
  const bc = await tag('dcrumb', () => [...document.querySelectorAll('nav, [class*=breadcrumb], header *')].find((e) => /introduction|documentation/i.test(e.innerText || '') && e.getBoundingClientRect().top < 160 && (e.innerText || '').length < 60) || null);
  if (bc) await S('docs-breadcrumb', q('[data-m="dcrumb"]'), ['default'], { group: g, title: 'Breadcrumb', desc: 'The section/page breadcrumb over the title.', sel: 'the breadcrumb row' }, { noScroll: true });
  // The ⌘K search dialog and the ⌘I assistant sheet, opened by keyboard.
  await page.keyboard.press('ControlOrMeta+k');
  await page.waitForTimeout(1500);
  const dlg = await tag('sdlg', () => [...document.querySelectorAll('[role=dialog], [data-component-name*=search], [aria-modal=true]')].find((e) => { const r = e.getBoundingClientRect(); return r.width > 200 && r.height > 20 && !/cookie/i.test(e.className || ''); }) || null);
  if (dlg) {
    await S('docs-search-dialog', q('[data-m="sdlg"]'), ['default'], { group: G.overlay, title: 'Search dialog', desc: 'The \u2318K search overlay: a field, result list and keyboard hints. Opened by keyboard; nothing was typed.', sel: 'the [role=dialog] search overlay' }, { noScroll: true, noReset: true, via: 'Meta+K' });
    const sinput = await tag('sinput', () => document.querySelector('[role=dialog] input, [role=dialog] textarea') || null);
    if (sinput) await S('docs-search-input', q('[data-m="sinput"]'), ['default'], { group: G.overlay, title: 'Search field', sel: 'the input inside the search dialog' }, { noScroll: true, crop: false });
  }
  await page.keyboard.press('Escape');
  await page.waitForTimeout(600);
  await page.keyboard.press('ControlOrMeta+i');
  await page.waitForTimeout(1500);
  const panel = await tag('apanel', () => [...document.querySelectorAll('[role=dialog], [data-component-name*=assistant], [id*=assistant], aside')].filter((e) => /ask a question|assistant/i.test(e.innerText || '') && e.getBoundingClientRect().width > 200)[0] || null);
  if (panel) {
    await S('docs-assistant-panel', q('[data-m="apanel"]'), ['default'], { group: G.overlay, title: 'Assistant panel', desc: 'The "Ask Assistant" sheet with a question box and send button. Opened by keyboard; nothing was typed or sent.', sel: 'the assistant sheet' }, { noScroll: true, noReset: true, via: 'Meta+I' });
    if (await tagEl('asend', 'send message|^send', '[data-m="apanel"]'))
      await S('docs-assistant-send', q('[data-m="asend"]'), ['default', 'hover', 'focus-visible'], { group: G.overlay, title: 'Assistant send button', desc: 'The send control in the assistant sheet. Measured, never pressed.', sel: '"Send message" in the assistant panel' }, { noScroll: true });
  }
  await page.keyboard.press('Escape');
  await page.waitForTimeout(400);
  await page.close();
}

async function docsApi() {
  await newPage('docs-api');
  await layoutFor('docs-api');
  await docsChrome();
  const g = G.docs;
  await S('docs-api-title', q('main h1, h1').first(), ['default'], { group: g, title: 'API reference title', desc: '"Anam REST API".', sel: 'main h1' }, { noScroll: true });
  const pre = await tag('dpre', () => [...document.querySelectorAll('main pre, article pre')].filter((e) => e.getBoundingClientRect().width > 200)[0] || document.querySelector('pre'));
  if (pre) {
    await S('docs-code-block', q('[data-m="dpre"]'), ['default'], { group: g, title: 'Code block', desc: 'A fenced code sample (the base URL block, a curl example), mono-set over a tinted panel.', sel: 'main pre' });
    const cp = await tag('dcopy', () => {
      const p = document.querySelector('[data-m="dpre"]');
      return p && ([...p.parentElement.querySelectorAll('button, [role=button]')].find((b) => /copy/i.test(b.innerText || b.getAttribute('aria-label') || '')) || [...p.querySelectorAll('button')][0]) || null;
    });
    if (cp) await S('docs-code-copy', q('[data-m="dcopy"]'), B4, { group: g, title: 'Copy button', desc: 'The copy control on a code block. Pressed is forced.', sel: 'the copy button on a pre block' });
  }
  const ic = await tag('dinline', () => [...document.querySelectorAll('main code, article code')].find((e) => !e.closest('pre') && (e.innerText || '').trim().length > 1) || null);
  if (ic) await S('docs-inline-code', q('[data-m="dinline"]'), ['default'], { group: g, title: 'Inline code', sel: 'a code span in body text' }, { crop: false });
  const badge = await tag('dbadge', () => [...document.querySelectorAll('#sidebar *')].find((e) => /^(post|get|put|delete|patch)$/i.test((e.innerText || '').trim()) && e.getBoundingClientRect().width < 80) || null);
  if (badge) await S('docs-method-badge', q('[data-m="dbadge"]'), ['default'], { group: g, title: 'Method badge', desc: 'The POST/GET verb chip beside an API endpoint in the sidebar.', sel: 'a method label in the sidebar' }, { crop: false, noScroll: true });
  const pn = await tag('dprev', () => [...document.querySelectorAll('main a, article a')].find((e) => /previous|next|create session/i.test(e.innerText || '') && e.getBoundingClientRect().top > document.documentElement.scrollHeight * 0.5) || [...document.querySelectorAll('[class*=pagination] a, main > a')].pop() || null);
  if (pn) await S('docs-prev-next', q('[data-m="dprev"]'), ['default', 'hover', 'focus-visible'], { group: g, title: 'Prev/next link', desc: 'The page-footer pagination link. Measured, never followed.', sel: 'a pagination link' });
  await page.close();
}

async function docsDark() {
  await newPage('docs-dark');
  // switch to dark through the local theme menu
  const t = await tag('dtheme', () => document.querySelector('#theme-preference-menu-trigger') || null);
  if (t) {
    await q('[data-m="dtheme"]').click().catch(() => {});
    await page.waitForTimeout(1000);
    const dark = await page.evaluate(() => {
      const items = [...document.querySelectorAll('[role=menuitem], [role=menu] *, [data-component-part*=item], [data-component-part*=option]')].filter((e) => /^dark$/i.test((e.innerText || '').trim()));
      const el = items[0];
      if (el) { el.click(); return true; }
      return false;
    });
    await page.waitForTimeout(1500);
    log('  dark switched:', dark, await page.evaluate(() => document.documentElement.className + '/' + document.documentElement.getAttribute('data-theme-preference')));
  }
  const g = G.docs;
  const darkNow = await page.evaluate(() => document.documentElement.className.includes('dark') || document.documentElement.getAttribute('data-theme-preference') === 'dark');
  if (!darkNow) { log('  ! dark theme not applied; skipping dark measures'); await page.close(); return; }
  await S('docs-dark-main', q('main').first(), ['default'], { group: g, title: 'Docs page, dark', desc: 'The content column in the dark theme.', sel: 'main' }, { noScroll: true, via: 'theme menu > Dark' });
  const side = await tag('dside', () => document.querySelector('#sidebar, [id*=sidebar]') || null);
  if (side) await S('docs-dark-sidebar', q('[data-m="dside"]'), ['default'], { group: g, title: 'Sidebar, dark', sel: '#sidebar in dark' }, { noScroll: true });
  await S('docs-dark-h1', q('main h1, h1').first(), ['default'], { group: g, title: 'Docs title, dark', sel: 'main h1 in dark' }, { noScroll: true });
  const card = await tag('dcard', () => [...document.querySelectorAll('main .card, article .card, main a')].find((e) => e.getBoundingClientRect().width > 200 && e.getBoundingClientRect().height > 60) || null);
  if (card) await S('docs-dark-card', q('[data-m="dcard"]'), ['default'], { group: g, title: 'Docs card, dark', sel: 'a card link in dark' });
  await page.close();
}

// ---------- mobile ----------
async function mobile() {
  const g = G.mobile;
  await newPage('home', { mobile: true, promo: 'keep' });
  await closePromo(page);
  await markFixed(page);
  await layoutFor('mobile-home');
  const nav = await tag('mnav', () => {
    const cands = [...document.querySelectorAll('body *')].filter((e) => {
      const cs = getComputedStyle(e), r = e.getBoundingClientRect();
      return (cs.position === 'fixed' || cs.position === 'sticky' || r.top <= 80) && r.width > 300 && r.height < 120 && /sign in|menu|developers/i.test(e.innerText || '');
    });
    return cands.sort((a, b) => (a.innerText || '').length - (b.innerText || '').length)[0] || null;
  });
  if (nav) await S('m-nav-bar', q('[data-m="mnav"]'), ['default'], { group: g, title: 'Mobile nav bar', desc: 'The top bar at 390 wide: logo, Sign in and the menu button.', sel: 'the mobile top bar' }, { noScroll: true });
  const menu = await page.evaluate(() => { const b = [...document.querySelectorAll('button, [role=button], [data-framer-name=NavTrigger]')].find((e) => { const r = e.getBoundingClientRect(); return r.top < 100 && r.width >= 20 && r.width <= 80; }); if (b) b.setAttribute('data-m', 'm-menu'); return !!b; });
  if (menu) {
    await S('m-menu-button', q('[data-m="m-menu"]'), ['default'], { group: g, title: 'Mobile menu button', sel: 'the menu control in the top bar' }, { noScroll: true });
    // open the drawer (a local toggle) and measure it
    await q('[data-m="m-menu"]').click({ timeout: 4000 }).catch(() => {});
    await page.waitForTimeout(1200);
    const drawer = await tag('mdrawer', () => {
      const cands = [...document.querySelectorAll('body *')].filter((e) => {
        const r = e.getBoundingClientRect();
        return r.width > 280 && r.height > 200 && /developers|pricing|resources|sign in/i.test(e.innerText || '') && e.getBoundingClientRect().top < 300;
      });
      return cands.sort((a, b) => (a.innerText || '').length - (b.innerText || '').length)[0] || null;
    });
    if (drawer) await S('m-nav-drawer', q('[data-m="mdrawer"]'), ['default'], { group: g, title: 'Mobile nav drawer', desc: 'The open menu at 390 wide (a local toggle: the menu button).', sel: 'the open nav drawer' }, { noScroll: true, noReset: true, via: 'a press on the menu button' });
    await page.keyboard.press('Escape').catch(() => {});
    await page.mouse.click(20, 780).catch(() => {});
    await page.waitForTimeout(500);
  }
  await S('m-hero-title', q('h1').first(), ['default'], { group: g, title: 'Hero title (mobile)', sel: 'h1 at 390 wide' }, { noScroll: true });
  const chip = await tag('mchip', () => {
    const cands = [...document.querySelectorAll('[role=button]')].filter((e) => /^(sales|customer-support|skill-training|language-tutor|medical-services)/i.test((e.innerText || '').trim()) && e.getBoundingClientRect().width > 60);
    return cands[0] || null;
  });
  if (chip) await S('m-persona-chip', q('[data-m="mchip"]'), ['default'], { group: g, title: 'Persona chip (mobile)', sel: 'a persona card at 390 wide' });
  await page.close();
  await newPage('docs-overview', { mobile: true });
  await layoutFor('mobile-docs');
  const dnav = await tag('mdside', () => document.querySelector('#sidebar, [id*=sidebar]') || null);
  if (dnav && await q('[data-m="mdside"]').isVisible()) await S('m-docs-sidebar', q('[data-m="mdside"]'), ['default'], { group: g, title: 'Docs sidebar (mobile)', sel: '#sidebar at 390 wide' }, { noScroll: true });
  const mtabs = await tag('mdtop', () => [...document.querySelectorAll('header, nav')].find((n) => n.getBoundingClientRect().top < 80 && n.getBoundingClientRect().width > 300) || null);
  if (mtabs) await S('m-docs-topbar', q('[data-m="mdtop"]'), ['default'], { group: g, title: 'Docs top bar (mobile)', sel: 'the docs top bar at 390' }, { noScroll: true });
  await page.close();
}

const PAGES = {
  home, api, pricing, 'get-demo': getDemo, 'docs-overview': docsOverview, 'docs-api': docsApi, 'docs-dark': docsDark, mobile,
  'interactive-avatars': () => gallery('interactive-avatars', /avatar|character/i, /.+/i, 'avatar-card', 'Avatar card', 'A card in the avatar gallery: a face, its style tag and name.'),
  about: () => gallery('about', /team|story|mission/i, /.+/i, 'about-card', 'About card', 'A card on the team/company page.'),
  research: () => gallery('research', /research|paper|model/i, /.+/i, 'research-card', 'Research entry', 'A paper or model entry on the research page.'),
  'case-studies': () => gallery('case-studies', /customer|story|case/i, /.+/i, 'case-card', 'Case study card', 'A customer story card.'),
  blog: () => gallery('blog', /blog|post|read/i, /.+/i, 'post-card', 'Blog post card', 'A post card in the blog index.'),
  changelog: () => gallery('changelog', /release|update|new|fix/i, /.+/i, 'changelog-entry', 'Changelog entry', 'A release entry on the changelog page.'),
  tools: () => gallery('tools', /tool|benchmark|demo/i, /.+/i, 'tool-card', 'Tool card', 'A card in the tools index.'),
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
