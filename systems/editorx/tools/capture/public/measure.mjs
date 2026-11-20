// Measures the editorx.com surface's public components in every state
// reachable without signing in, checking out or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home features design plans pricing inspiration templates academy
// enterprise mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// editorx.com is a redirect shell for Wix Studio: paths on BASE are requested
// on www.editorx.com and 301 to wix.com/studio; /pricing still serves a Wix
// plans page on the domain itself. Pages with no editorx path left (design,
// plans, templates) are fetched from wix.com/studio. The site is a thunderbolt
// build — every class is a hash (BrYaz7, dsyWYg) and components are comp-* id
// boxes — so every spec selects by role, aria-label, text or structure, never
// a class. Nothing is sent, bought or signed into: the only presses are local
// UI toggles — the Product nav dropdown, an FAQ question, a billing toggle,
// the mobile menu and the plan tabs. Log In / Start Creating / plan CTAs are
// measured, never followed. Consent overlays are hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, STUDIO, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
// Paths on BASE run through the editorx.com redirect; full URLs are used for
// the studio pages that have no editorx path left.
const URLS = {
  home: '/', features: '/features', academy: '/academy', inspiration: '/inspiration',
  enterprise: '/enterprise', pricing: '/pricing',
  plans: STUDIO + '/plans', design: STUDIO + '/design', templates: STUDIO + '/templates',
};
const urlFor = (key) => (/^https?:/.test(URLS[key]) ? URLS[key] : BASE + URLS[key]);
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
  const cleared = await open(page, url || urlFor(key), { wait, promo });  // false: the bot check did not clear (lib.mjs)
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
  Object.assign(c, { page: current, run, url: URLS[current] && urlFor(current) }, meta);
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
  // Thunderbolt pages re-mount subtrees when async data resolves (the
  // plans grid re-renders once its data arrives): give a briefly
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

// Clicks a UI toggle (dropdown, menu, FAQ question, billing toggle). Refuses
// a submit button and any control whose text names an action this kit must
// never take — "Start Creating", "Log In", plan CTAs and checkout all land
// here.
const NEVER = /^(send|submit|sign in|log ?in|login|sign up|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start( creating)?|start for free|get started|claim|share|export|select|continue|claim this offer|try again|order( free)?( sample)?|add to cart|go to the platform|contact sales|learn more|upgrade|try now)$/i;
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

// The nav's Product/Resources/Enterprise buttons open a full-width mega-menu
// on hover (a click does nothing).
async function openDropdown(name = 'Product') {
  const t = q('nav button').filter({ hasText: new RegExp('^\\s*' + name + '\\s*$') }).filter({ visible: true }).first();
  if (!(await t.count())) return false;
  await t.hover({ timeout: 5000 }).catch(() => t.evaluate((el) => el.dispatchEvent(new MouseEvent('mouseover', { bubbles: true }))));
  await page.waitForTimeout(1500);
  return true;
}

// Marks the opened nav mega-menu: the smallest painted absolutely-positioned
// panel under the nav bar holding several links.
async function markDropdown() {
  await page.evaluate(() => {
    const cand = [...document.querySelectorAll('body *')].filter((el) => {
      const r = el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      const t = el.innerText || '';
      return r.top >= 40 && r.top < 120 && r.width > 320 && r.height > 160 && r.height < innerHeight
        && cs.visibility !== 'hidden' && +cs.opacity > 0
        && el.querySelectorAll('a').length >= 2 && t.length < 8000;
    }).sort((a, b) => a.getBoundingClientRect().width * a.getBoundingClientRect().height - b.getBoundingClientRect().width * b.getBoundingClientRect().height);
    if (cand[0]) cand[0].setAttribute('data-m-mark', 'dropdown');
  });
}

// Marks the smallest visible ancestor of a plan CTA that holds a plan name
// and a price — one pricing card, not the grid around it.
async function markPlanCard(priceRe = /\$\s*\d|\d+\s*\/\s*mo\b|per month|\/month/i) {
  await page.evaluate((re) => {
    const rx = new RegExp(re);
    document.querySelectorAll('[data-m-mark="plancard"]').forEach((n) => n.removeAttribute('data-m-mark'));
    // Anchor on the price text: the hero also carries CTAs, so walk up from
    // each price figure to the smallest box that holds a price and a call to
    // action — one plan card, not the grid around it.
    const CTARE = /get started|start creat|try|select|choose|upgrade|contact sales|learn more|start now/i;
    const prices = [...document.querySelectorAll('span, div, p, h2, h3')].filter((e) => rx.test(e.innerText || '') && (e.innerText || '').length < 120 && e.getBoundingClientRect().width > 0);
    for (const p of prices) {
      let n = p;
      for (let i = 0; i < 14 && n.parentElement; i++) {
        n = n.parentElement;
        const r = n.getBoundingClientRect();
        const t = n.innerText || '';
        if (r.width > 160 && r.width < 660 && r.height > 140 && r.height < 1200 && t.length < 2800
          && [...n.querySelectorAll('button, a')].some((b) => CTARE.test(b.innerText || '') && b.getBoundingClientRect().width > 0)) {
          n.setAttribute('data-m-mark', 'plancard');
          return;
        }
      }
    }
    // no CTA inside the card (some grids put actions in a row below): mark
    // the smallest box around the price instead.
    const p = prices[0];
    if (!p) return;
    let n = p;
    for (let i = 0; i < 14 && n.parentElement; i++) {
      n = n.parentElement;
      const r = n.getBoundingClientRect();
      const t = n.innerText || '';
      if (r.width > 160 && r.width < 660 && r.height > 140 && r.height < 1200 && t.length < 2800) {
        n.setAttribute('data-m-mark', 'plancard');
        return;
      }
    }
  }, priceRe.source);
}

// Marks the painted band near the bottom of the studio home page — the
// closing call-to-action section paints a saturated fill (rgb(222,255,0)
// lime) with its copy in a sibling layer.
async function markCtaBand() {
  await page.evaluate(() => {
    const H = document.documentElement.scrollHeight;
    const cand = [...document.querySelectorAll('section, div, footer')].filter((el) => {
      const r = el.getBoundingClientRect() && el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      const top = r.top + scrollY;
      return top > H - 6000 && top < H - 900 && r.width > 900 && r.height > 80 && r.height < 1600
        && !el.closest('footer, #WIX_STUDIO_FOOTER')
        && (cs.backgroundColor !== 'rgba(0, 0, 0, 0)' || cs.backgroundImage !== 'none');
    }).sort((a, b) => {
      const ar = a.getBoundingClientRect(), br = b.getBoundingClientRect();
      return br.top - ar.top || (ar.width * ar.height) - (br.width * br.height);
    });
    if (cand[0]) cand[0].setAttribute('data-m-mark', 'ctaband');
  });
}

// Marks a showcase/gallery card: a link or figure that holds an image tile
// and a short caption (inspiration, templates, academy cards all match).
async function markGalleryCard(tag, linkRe = /./) {
  await page.evaluate(([t, re]) => {
    const rx = new RegExp(re);
    const cand = [...document.querySelectorAll('a, article, li, figure, div')].filter((el) => {
      const r = el.getBoundingClientRect();
      const t = el.innerText || '';
      return r.width > 160 && r.width < 700 && r.height > 140 && r.height < 700 && t.length < 500
        && el.querySelector('img, video, canvas') && rx.test(t || el.getAttribute('aria-label') || '');
    }).sort((a, b) => a.getBoundingClientRect().top - b.getBoundingClientRect().top);
    if (cand[0]) cand[0].setAttribute('data-m-mark', t);
  }, [tag, linkRe.source]);
}

// Marks the opened mobile navigation panel: a fixed overlay holding the nav
// links and the auth actions.
async function markMobileMenu() {
  await page.evaluate(() => {
    const cand = [...document.querySelectorAll('div,nav,aside,section')].filter((el) => {
      const r = el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      const t = el.innerText || '';
      return (cs.position === 'fixed' || cs.position === 'absolute') && r.height > innerHeight * 0.5 && r.width > innerWidth * 0.6
        && /Log In|Start Creating/i.test(t) && /Product|Resources|Enterprise|Pricing/i.test(t) && t.length < 9000;
    }).sort((a, b) => (a.innerText || '').length - (b.innerText || '').length);
    if (cand[0]) cand[0].setAttribute('data-m-mark', 'mmenu');
  });
}

// Marks one feature card on the features index: the smallest box that holds a
// feature heading and its blurb. Picking "the biggest painted element under
// the section" once marked the empty full-bleed background layer instead
// (1440x942 of fallback type) — a card is anchored on its content.
async function markFeatureCard() {
  await page.evaluate(() => {
    document.querySelectorAll('[data-m-mark="featcard"]').forEach((n) => n.removeAttribute('data-m-mark'));
    // A card holds its heading plus a short blurb in a column's width: a
    // full-bleed band or an empty painted layer is not the component.
    const cardAround = (h) => {
      const ht = (h.innerText || '').trim().length;
      for (let n = h, i = 0; n.parentElement && i < 12; i++) {
        n = n.parentElement;
        const r = n.getBoundingClientRect();
        const t = (n.innerText || '').trim();
        if (r.width > 200 && r.width < 720 && r.height > 90 && r.height < 700
          && t.length > ht + 15 && t.length < 600) return n;
      }
      return null;
    };
    const heads = [...document.querySelectorAll('h2, h3, h4, h5')].filter((el) => {
      const r = el.getBoundingClientRect();
      const t = (el.innerText || '').trim();
      return r.width > 0 && t.length >= 4 && t.length <= 60;
    });
    for (const h of heads) { const n = cardAround(h); if (n) { n.setAttribute('data-m-mark', 'featcard'); return; } }
    // Fallback when the titles are not headings: leaf text that names a
    // feature (the card box around it is found the same way).
    const leaves = [...document.querySelectorAll('p, span, div, a')].filter((el) => {
      const r = el.getBoundingClientRect();
      const t = (el.innerText || '').trim();
      return r.width > 0 && !el.children.length && t.length >= 4 && t.length <= 60
        && /breakpoint|pixel|figma|wireframe|sitemap|responsive|grid|seo|cms/i.test(t);
    });
    for (const h of leaves) { const n = cardAround(h); if (n) { n.setAttribute('data-m-mark', 'featcard'); return; } }
  });
}

// Marks the pinned showcase scene: the sticky viewport box carrying the
// "Site of the week" copy. The section's full-height scroll track once
// passed for it — an empty painted layer 1440x2320 with fallback type.
async function markShowcase() {
  await page.evaluate(() => {
    document.querySelectorAll('[data-m-mark="showcase"]').forEach((n) => n.removeAttribute('data-m-mark'));
    const has = (el) => /site of the week/i.test(el.innerText || '');
    const stick = [...document.querySelectorAll('body *')].filter((el) => {
      const cs = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return cs.position === 'sticky' && r.width > 800 && r.height > 300 && r.height <= innerHeight + 80 && has(el);
    }).sort((a, b) => a.getBoundingClientRect().height - b.getBoundingClientRect().height);
    const el = stick[0] || [...document.querySelectorAll('section, div')].filter((n) => {
      const r = n.getBoundingClientRect();
      return r.width > 800 && r.height > 300 && r.height < 1200 && has(n) && n.querySelector('img, video, canvas');
    }).sort((a, b) => a.getBoundingClientRect().height - b.getBoundingClientRect().height)[0];
    if (el) el.setAttribute('data-m-mark', 'showcase');
  });
}

// Marks the real mobile header: the smallest fixed/sticky bar pinned to the
// top that holds the burger/menu button. The page's header is not a <nav> at
// phone width — the footer's <nav> matched a bare nav selector first and was
// recorded as the header (footer copy, dark fill, 390x861 at y 14287).
async function markMobileHeader() {
  await page.evaluate(() => {
    document.querySelectorAll('[data-m-mark="mheader"]').forEach((n) => n.removeAttribute('data-m-mark'));
    const btn = [...document.querySelectorAll('button, [role="button"], a')].find((el) => {
      const r = el.getBoundingClientRect();
      return r.width > 0 && r.top < 100 && /navigation|menu/i.test(el.getAttribute('aria-label') || '');
    });
    if (btn) for (let n = btn.parentElement; n; n = n.parentElement) {
      const cs = getComputedStyle(n);
      const r = n.getBoundingClientRect();
      if ((cs.position === 'fixed' || cs.position === 'sticky') && r.top <= 4 && r.height > 20 && r.height < 120 && r.width >= innerWidth * 0.8) {
        n.setAttribute('data-m-mark', 'mheader');
        return;
      }
    }
    // Fallback: any fixed top bar carrying the Start Creating action.
    const cand = [...document.querySelectorAll('body *')].filter((el) => {
      const cs = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return (cs.position === 'fixed' || cs.position === 'sticky') && r.top <= 4 && r.height > 20 && r.height < 120
        && r.width >= innerWidth * 0.8 && /Start Creating/i.test(el.innerText || '');
    }).sort((a, b) => a.getBoundingClientRect().height - b.getBoundingClientRect().height);
    if (cand[0]) cand[0].setAttribute('data-m-mark', 'mheader');
  });
}

const G = {
  shell: 'Shell and navigation', home: 'Home', features: 'Features and design',
  plans: 'Plans and pricing', galleries: 'Galleries', academy: 'Academy and enterprise',
  footer: 'Footer', mobile: 'Mobile (390 wide)',
};

async function home() {
  if (!(await newPage('home', { wait: 12000 }))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('nav-bar', q('nav').filter({ hasText: /Product/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav bar', desc: 'The fixed top bar (57px): the Wix Studio wordmark, the Product / Resources / Enterprise dropdown triggers, Pricing, the language selector, Log In and the black Start Creating button.', sel: 'nav' }, { noScroll: true });
  await S('logo', q('nav a[href$="/studio"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Wix Studio wordmark anchor.', sel: 'nav a /studio' }, { noScroll: true });
  await S('nav-trigger', q('nav button').filter({ hasText: /^\s*Product\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav trigger', desc: 'The Product button that opens the nav dropdown; toggled, never followed.', sel: 'nav button "Product"' }, { noScroll: true });
  await S('nav-link', q('nav a').filter({ hasText: /^\s*Pricing\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'The plain Pricing nav link; measured, never followed.', sel: 'nav a "Pricing"' }, { noScroll: true });
  await S('nav-lang', q('button[aria-label*="language" i], button#menu-item-languages').filter({ visible: true }).first(), B4, { group: g, title: 'Language selector', desc: 'The globe language control ("language selector, english selected"); never opened.', sel: 'button[aria-label*=language]' }, { noScroll: true });
  await S('nav-login', q('#WIX_STUDIO_HEADER a, header a').filter({ hasText: /^\s*Log In\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Log-in link', desc: 'The Log In header action; measured, never followed (it leaves for users.wix.com).', sel: '#WIX_STUDIO_HEADER a "Log In"' }, { noScroll: true });
  await S('nav-cta', q('#WIX_STUDIO_HEADER a, header a').filter({ hasText: /^\s*Start Creating\s*$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav CTA', desc: 'The black Start Creating action in the header; measured, never followed.', sel: '#WIX_STUDIO_HEADER a "Start Creating"' }, { noScroll: true });
  try { await openDropdown('Product'); } catch (e) { log('  ! dropdown open failed', String(e.message).split('\n')[0]); }
  await markDropdown();
  await S('nav-dropdown', q('[data-m-mark="dropdown"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Nav dropdown', desc: 'The Product dropdown panel, opened by its own trigger.', sel: 'opened Product dropdown' }, { noScroll: true, noReset: true });
  const ensureDropdown = async () => {
    if (!(await q('[data-m-mark="dropdown"]').filter({ visible: true }).count())) {
      await openDropdown('Product'); await markDropdown(); await page.waitForTimeout(1200);
    }
  };
  await S('menu-link', q('[data-m-mark="dropdown"] a').filter({ hasText: /Design|Development|Enterprise|AI|Business solutions|CMS|SEO/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Menu link', desc: 'A link inside the opened Product mega-menu.', sel: 'mega-menu link' }, { noScroll: true, noReset: true, open: ensureDropdown, before: { hover: ensureDropdown, 'focus-visible': ensureDropdown, pressed: ensureDropdown } });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  const h = G.home;
  await S('hero-title', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: 'The "Design with impact / Deliver at scale" display headline, madefor-display.', sel: 'h1' }, { noScroll: true });
  await S('hero-sub', await domFind(page, /website building platform for designers/i, { sel: 'p, span, div, h2', tag: 'herosub' }), ['default'], { group: h, title: 'Hero copy', desc: 'The lede under the display headline.', sel: 'hero lede' });
  await S('hero-cta', q('button:not(#WIX_STUDIO_HEADER *), a:not(#WIX_STUDIO_HEADER *)').filter({ hasText: /^\s*Start creating\s*(→|->|›|➔)?\s*$/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Hero CTA', desc: 'The purple "Start creating" pill under the hero copy (the header CTA shares the label, so the header is excluded); measured, never followed.', sel: '"Start creating" pill' });
  await S('section-h2', q('h2, h3').filter({ hasText: /Focus on design|Set your vision in motion|Develop and sell|Code on your terms/i }).filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A feature-section heading below the hero.', sel: 'section h2' });
  await S('section-link', q('a').filter({ hasText: /Advanced design features|Explore all AI tools|Learn more|See all solutions/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Section link', desc: 'An inline "learn more" link inside a feature section; measured, never followed.', sel: 'section link' });
  // The "Site of the week" showcase card is a scroll-jacked sticky section.
  await markShowcase();
  await S('showcase-card', q('[data-m-mark="showcase"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'Showcase section', desc: 'The "Site of the week" scroll-jacked showcase (a pinned media scene); measured mid-scroll state may sit between animation frames.', sel: 'sticky showcase scene' });
  await S('faq-question', q('[role="listitem"], button, [role="button"], h2, h3, h4').filter({ hasText: /What is Wix Studio|difference between Wix and Wix Studio|How much does Wix Studio/i }).filter({ visible: true }).first(), [...B4, 'opened'], { group: h, title: 'FAQ question', desc: 'A Wix Studio FAQ repeater item (question row); toggled open once for the opened state (local UI).', sel: 'FAQ listitem' });
  await markCtaBand();
  await S('cta-band', q('[data-m-mark="ctaband"]').filter({ visible: true }).first(), ['default'], { group: h, title: 'CTA band', desc: 'The closing "Unleash your creations. Rein in the chaos. / Start creating" band.', sel: 'closing CTA band' }, { noScroll: true });
  save();
}

async function features() {
  if (!(await newPage('features', { wait: 11000 }))) return;
  await sheetsFor('features');
  await chrome('features');
  const g = G.features;
  await S('feat-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Features title', desc: 'The features page display heading.', sel: 'h1 on /studio/features' }, { noScroll: true });
  await markFeatureCard();
  await S('feat-card', q('[data-m-mark="featcard"]').filter({ visible: true }).first(), B4, { group: g, title: 'Feature card', desc: 'A feature card on the features index (a title over its blurb).', sel: 'feature card box' });
  await S('feat-link', q('a').filter({ hasText: /Learn more|Explore|See all/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Feature link', desc: 'A "learn more" link on the features page; measured, never followed.', sel: 'features link' });
  save();
}

async function design() {
  if (!(await newPage('design', { wait: 11000 }))) return;
  await sheetsFor('design');
  await chrome('design');
  const g = G.features;
  await S('design-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Design title', desc: 'The design-features page display heading — the page closest to Editor X\'s old positioning.', sel: 'h1 on /studio/design' }, { noScroll: true });
  await S('design-cta', q('button, a').filter({ hasText: /Start creating|Get started|Try now/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Design CTA', desc: 'A call-to-action on the design page; measured, never followed.', sel: 'design CTA' });
  await S('design-h2', q('h2').filter({ visible: true }).first(), ['default'], { group: g, title: 'Design section heading', desc: 'A section heading on the design page.', sel: 'h2 on /studio/design' });
  save();
}

async function plans() {
  if (!(await newPage('plans', { wait: 11000 }))) return;
  await sheetsFor('plans');
  await chrome('plans');
  await lazyLoad();
  const g = G.plans;
  await S('plans-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plans title', desc: 'The "Choose the right Studio plan for each project" heading.', sel: 'h1 on /studio/plans' }, { noScroll: true });
  await S('plan-badge', q('div, span, p').filter({ hasText: /^\s*RECOMMENDED\s*$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Recommended badge', desc: 'The lime RECOMMENDED badge on the highlighted plan column.', sel: '"RECOMMENDED" badge' });
  await markPlanCard();
  await S('plan-card', q('[data-m-mark="plancard"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan card', desc: 'A studio plan card (name, price, action).', sel: 'plan card' });
  await S('plan-price', await domFind(page, /\$\s*\d+|US\$\s*\d+/i, { sel: 'span, div, p', tag: 'price' }), ['default'], { group: g, title: 'Plan price', desc: "A plan card's price figure (US$ in the region the capture was served).", sel: 'plan US$ figure' });
  await S('plan-cta', q('[data-m-mark="plancard"] button, [data-m-mark="plancard"] a').filter({ hasText: /get started|start creat|try|select|choose|upgrade|contact sales|learn more|start now/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: "A plan card's action; measured, never followed.", sel: 'plan card CTA' });
  save();
}

async function pricing() {
  // editorx.com/pricing — the one page still served on the domain itself. In
  // headless runs its premium-plans widget fails to load and paints an error
  // pane ("Couldn't load Premium plans due to a technical issue" + a Refresh
  // link); the spec measures exactly what the domain serves.
  if (!(await newPage('pricing', { wait: 11000 }))) return;
  await sheetsFor('pricing');
  await chrome('pricing');
  await lazyLoad();
  const g = G.plans;
  const head = q('h1, h2, h3, h4, p, span').filter({ hasText: /Couldn't load Premium plans|technical issue/i }).filter({ visible: true }).first();
  await S('pricing-h1', head, ['default'], { group: g, title: 'Pricing title (editorx.com)', desc: 'The heading editorx.com/pricing serves — on this run, the "Couldn\'t load Premium plans due to a technical issue" error title.', sel: 'error title on editorx.com/pricing' }, { noScroll: true });
  await S('pricing-pane', q('div, section').filter({ hasText: /Couldn't load Premium plans|technical issue/i }).filter({ visible: true }).last(), ['default'], { group: g, title: 'Error pane (editorx.com)', desc: 'The pane the premium-plans widget paints when it fails headless; honest evidence of what the domain serves.', sel: 'pricing error pane' });
  // The pane carries two links — 'contact Customer Care.' inside the copy and
  // a standalone 'Refresh' action below it. An alternation matched whichever
  // came first in the DOM (Customer Care), so Refresh is matched exactly and
  // the support link is a separate entry when it exists.
  const refresh = q('a, button').filter({ hasText: /^\s*Refresh\s*$/i }).filter({ visible: true });
  const refreshLoc = (await refresh.count()) ? refresh.first()
    : q('[role="button"], [role="link"], span').filter({ hasText: /^\s*Refresh\s*$/i }).filter({ visible: true }).first();
  await S('pricing-refresh', refreshLoc, B4, { group: g, title: 'Refresh link (editorx.com)', desc: 'The Refresh action inside the error pane; measured, never followed.', sel: 'error Refresh' }, { noScroll: true });
  await S('pricing-support', q('a, button, [role="link"]').filter({ hasText: /Customer Care/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Support link (editorx.com)', desc: "The 'contact Customer Care.' support link inside the error pane's copy; measured, never followed.", sel: 'error pane support link' }, { noScroll: true });
  save();
}

async function inspiration() {
  if (!(await newPage('inspiration', { wait: 11000 }))) return;
  await sheetsFor('inspiration');
  await chrome('inspiration');
  await lazyLoad();
  const g = G.galleries;
  await S('inspo-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Inspiration title', desc: 'The inspiration gallery heading.', sel: 'h1 on /studio/inspiration' }, { noScroll: true });
  await markGalleryCard('inspo', /./);
  await S('inspo-card', q('[data-m-mark="inspo"]').filter({ visible: true }).first(), B4, { group: g, title: 'Inspiration card', desc: 'A showcase-site card in the inspiration gallery; measured, never followed.', sel: 'inspiration card' });
  await S('inspo-filter', q('button, [role="tab"], a').filter({ hasText: /All|Websites|Portfolios|Stores|Categories/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Gallery filter', desc: 'A category filter on the inspiration page; measured unselected.', sel: 'inspiration filter' });
  save();
}

async function templates() {
  if (!(await newPage('templates', { wait: 11000 }))) return;
  await sheetsFor('templates');
  await chrome('templates');
  await lazyLoad();
  const g = G.galleries;
  await S('templates-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Templates title', desc: 'The studio templates page heading.', sel: 'h1 on /studio/templates' }, { noScroll: true });
  await markGalleryCard('tmpl', /./);
  await S('template-card', q('[data-m-mark="tmpl"]').filter({ visible: true }).first(), B4, { group: g, title: 'Template card', desc: 'A template card in the gallery; measured, never followed.', sel: 'template card' });
  save();
}

async function academy() {
  if (!(await newPage('academy', { wait: 11000 }))) return;
  await sheetsFor('academy');
  await chrome('academy');
  await lazyLoad();
  const g = G.academy;
  await S('academy-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Academy title', desc: 'The studio academy heading.', sel: 'h1 on /studio/academy' }, { noScroll: true });
  await markGalleryCard('acad', /./);
  await S('academy-card', q('[data-m-mark="acad"]').filter({ visible: true }).first(), B4, { group: g, title: 'Academy card', desc: 'A course or tutorial card on the academy page; measured, never followed.', sel: 'academy card' });
  save();
}

async function enterprise() {
  if (!(await newPage('enterprise', { wait: 11000 }))) return;
  const g = G.academy;
  await S('ent-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Enterprise title', desc: 'The enterprise page display heading.', sel: 'h1 on /studio/enterprise' }, { noScroll: true });
  await S('ent-cta', q('button, a').filter({ hasText: /Contact sales|Talk to|Get started|Learn more/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Enterprise CTA', desc: 'A Contact-sales-style action on the enterprise page; measured, never followed.', sel: 'enterprise CTA' });
  save();
}

async function footer() {
  if (!(await newPage('home', { wait: 9000 }))) return;
  const g = G.footer;
  await page.evaluate(() => scrollTo(0, document.documentElement.scrollHeight));
  await page.waitForTimeout(1800);
  await S('footer', q('footer, #WIX_STUDIO_FOOTER').filter({ visible: true }).last(), ['default'], { group: g, title: 'Footer', desc: 'The Wix Studio footer: the blurb, link columns, social icons, language and legal.', sel: 'footer#WIX_STUDIO_FOOTER' }, { noScroll: true });
  await S('footer-link', q('footer a, #WIX_STUDIO_FOOTER a').filter({ hasText: /Design|Development|Enterprise|Academy|Blog/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Footer link', sel: 'footer a' }, { noScroll: true });
  await S('social-icon', q('footer a[href*="instagram"], footer a[href*="facebook"], footer a[href*="twitter"], footer a[href*="youtube"], #WIX_STUDIO_FOOTER a[aria-label*="Instagram" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Social link', desc: 'A social link in the footer.', sel: 'footer social a' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/', wait: 12000 }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await markMobileHeader();
  await S('m-header', q('[data-m-mark="mheader"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile nav', desc: 'The fixed mobile top bar (the wordmark, the square Start Creating and the burger menu button) — the page header is not a <nav> at phone width.', sel: 'fixed top bar at 390' }, { noScroll: true });
  const menu = q('button[aria-label*="navigation" i], button[aria-label*="menu" i]').filter({ visible: true }).first();
  await S('m-menu-button', menu, ['default'], { group: g, title: 'Menu button', desc: 'The burger/menu toggle in the mobile nav.', sel: 'nav menu button' }, { noScroll: true });
  try {
    if (await menu.count()) { await menu.click({ timeout: 5000 }).catch(() => menu.evaluate((el) => el.click())); await page.waitForTimeout(1600); }
  } catch (e) { log('  ! mobile menu toggle failed', String(e.message).split('\n')[0]); }
  await markMobileMenu();
  await S('m-menu-open', q('[data-m-mark="mmenu"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu, open', desc: 'The opened mobile navigation panel.', sel: 'opened mobile menu' }, { noScroll: true });
  await S('m-nav-item', q('[data-m-mark="mmenu"] a, [data-m-mark="mmenu"] button, [data-m-mark="mmenu"] [role="link"], [data-m-mark="mmenu"] [role="button"]').filter({ hasText: /^\s*(Product|Resources|Enterprise|Pricing)\s*$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Mobile nav item', desc: 'A row inside the opened mobile menu.', sel: 'mobile menu row' }, { noScroll: true });
  await page.keyboard.press('Escape'); await page.waitForTimeout(500);
  await S('m-hero', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile headline', sel: 'h1 at 390' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); the surface paints one light theme, reached through the editorx.com → wix.com/studio redirect (editorx.com/pricing is still served on-domain)';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, features, design, plans, pricing, inspiration, templates, academy, enterprise, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
try {
  for (const k of order) { if (k !== 'mobile') await plan[k](); }
  if (!pages.length || pages.includes('home')) await footer();
  if (!pages.length || pages.includes('mobile')) await plan.mobile();
  // Reduced-motion check on an element that actually transitions (a nav
  // trigger), so the delta is meaningful.
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
