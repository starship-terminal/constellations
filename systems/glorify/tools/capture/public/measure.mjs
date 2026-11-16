// Measures glorify.com's public components in every state reachable without
// signing in or submitting anything.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing feature templates marketplace learn submit login
//        register designer mobile.
// Writes raw/components-computed.json (merged) and one crop per component and
// state into components/crops/; raw/measurements.md is built by
// build-measurements.mjs.
//
// glorify.com is a Framer marketing site (data-framer-name components: "Top
// nav", "Get Started Now", "Button/Button Primary"), light-only — no theme
// toggle, no dark media query. app.glorify.com is the product SPA (Tailwind
// plus named layers: button button-primary, field-container__input,
// dropdown-toolbar, panel--inspector): /welcome redirects to the dark
// /dashboard/login card, /dashboard/register paints the sign-up card, and
// /designer/use-template/0 anonymously opens the real editor — the upload
// onboarding, the Craft dialog behind "Try with Placeholder Image", and the
// tool rail / header / inspector of the canvas itself.
//
// Nothing is sent, bought or signed into: the only activations are local UI
// toggles — the nav "Features" dropdown (hover), the pricing billing
// switcher, the mobile burger, the editor's inspector tabs and the Craft
// dialog's style pick. The auth fields are typed into and cleared, never
// submitted; Login, Signup, Share, Download and "Add to canvas" are measured,
// never activated. No consent overlay was observed; any that appears is
// hidden, never answered.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, APP, LOGIN_URL, SIGNUP_URL, DESIGNER_URL, M, launch, patch, open, closePromo, domFind, styleOf, crop, centre, RAW, UA, UA_MOBILE } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
const URLS = {
  home: '/', pricing: '/pricing', feature: '/features/background-remover',
  templates: '/templates', marketplace: '/template-marketplace', learn: '/learn',
  submit: '/submit-template',
  login: LOGIN_URL, register: SIGNUP_URL, designer: DESIGNER_URL, mobile: '/',
};
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
  await open(page, url || (URLS[key].startsWith('http') ? URLS[key] : BASE + URLS[key]), { wait, promo });
  if (await blocked()) { log('  BLOCKED', key); failedPages.add(key); await page.close(); await ctx.close(); return false; }
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

async function S(key, target, list, meta = {}, opts = {}) {
  const prev = out.components[key];
  const keep = prev && Object.keys(prev.states || {}).length ? { page: prev.page, run: prev.run, url: prev.url } : null;
  comp(key, { title: meta.title, group: meta.group, desc: meta.desc, selector: meta.sel });
  if (!listed.has(key)) listed.set(key, new Set());
  for (const st of list) listed.get(key).add(st);
  delete out.components[key].missing;
  if (opts.open) { await reset(); try { await opts.open(); } catch (e) { log('  ! open failed', key, String(e.message).slice(0, 80)); } }
  let loc = target.filter({ visible: true }).first();
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
  // A broad selector re-resolves against the live DOM on every use, so an
  // overlay that mounts mid-run can swap the node a state reads. opts.pin
  // marks the resolved element once and every state below measures that same
  // node.
  if (opts.pin) {
    await loc.evaluate((el) => el.setAttribute('data-m-pin', '1')).catch(() => {});
    loc = page.locator('[data-m-pin="1"]').first();
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
        // A before.opened callback already toggled the control open — a second
        // generic click would close it again before the reading.
        if (opts.noToggle) via = 'held open by an earlier toggle';
        else if (!via) { await toggle(loc, { allowLink: opts.allowLink }); await page.waitForTimeout(900); via = 'own toggle'; }
        const exp = await loc.evaluate((el) => el.getAttribute('aria-expanded')).catch(() => null);
        if (exp !== null) via = (via || 'opened') + (exp === 'true' ? ' (aria-expanded=true at save)' : ' (aria-expanded=false at save — the open did not hold)');
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
  if (opts.pin) await page.evaluate(() => document.querySelectorAll('[data-m-pin]').forEach((n) => n.removeAttribute('data-m-pin'))).catch(() => {});
  await reset();
}

// Clicks a UI toggle (dropdown, menu, sheet trigger). Refuses a submit button
// and any control whose text names an action this kit must never take.
const NEVER = /^(send|send message|submit|sign in|log ?in|login|sign ?up|signup|create|add|download|buy|purchase|pay|checkout|join|subscribe|save|apply|accept|reject|start|get started|claim|share|export|select|continue|continue with.*|claim this offer|try again|start for free|try for free|book a demo|start planning|restore|send reset|reset password|start a free trial|start .* trial|add to canvas|play for free|get started now|shuffle designs)$/i;
async function toggle(loc, { allowLink = false } = {}) {
  const l = loc.filter({ visible: true }).first();
  const t = await l.evaluate((el) => ({ tag: el.tagName, type: el.getAttribute('type'), text: (el.innerText || el.getAttribute('aria-label') || '').trim() }));
  if (t.type === 'submit' || NEVER.test(t.text) || (t.tag === 'A' && !allowLink)) throw new Error(`toggle refused: ${t.tag} "${t.text}"`);
  await l.click({ timeout: 4000 }).catch(() => l.evaluate((el) => el.click()));
}

const q = (sel) => page.locator(sel);
const B4 = ['default', 'hover', 'focus-visible', 'pressed'];
const FIELD = ['default', 'focused', 'filled'];

// Tags and returns the first `<a>` whose box is at least `min`px in both
// directions and that wraps an image — the shape of a gallery card on
// /templates, /template-marketplace and the Learn article grid. Playwright's
// hasText cannot express "has an img child", and a bare a[href*=template]
// resolves to the header's "All templates" link instead of a card.
const imgCard = async (min = 150, tag = 'm-card') => {
  const ok = await page.evaluate(([m, t]) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const a = [...document.querySelectorAll('a')].find((n) => {
      const r = n.getBoundingClientRect();
      return r.width >= m && r.height >= m && n.querySelector('img, [style*="background-image"]');
    });
    if (!a) return false;
    a.setAttribute('data-m-mark', t);
    return true;
  }, [min, tag]);
  return ok ? page.locator(`[data-m-mark="${tag}"]`) : page.locator('[data-m-mark="__none__"]');
};

// Tags and returns the first on-screen Framer tile holding an image —
// /templates is a draggable marquee canvas of template thumbnails ("Row 2 -
// 1", "Beauty 2 - 1"…), not a link grid, so a card is a data-framer-name tile
// whose box sits inside the viewport.
const framerTile = async (tag = 'm-tile') => {
  const ok = await page.evaluate((t) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const el = [...document.querySelectorAll('[data-framer-name]')].find((n) => {
      const r = n.getBoundingClientRect();
      return r.width >= 100 && r.width <= 600 && r.height >= 100 && r.height <= 700
        && r.x >= 0 && r.x + r.width <= innerWidth && r.y >= 0 && r.y < innerHeight
        && n.querySelector('img, video, [style*="background-image"]');
    });
    if (!el) return false;
    el.setAttribute('data-m-mark', t);
    return true;
  }, tag);
  return ok ? page.locator(`[data-m-mark="${tag}"]`) : page.locator('[data-m-mark="__none__"]');
};

// Tags and returns the card around the first meaningful `h3` — Learn article
// titles are h3s that sit beside category-label h3s ("Company News"), so the
// heading has to be filtered to a real title before its ancestor is the card.
const titleCard = async (tag = 'm-tcard') => {
  const ok = await page.evaluate((t) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const h = [...document.querySelectorAll('h2, h3')].find((n) => {
      const r = n.getBoundingClientRect();
      const txt = (n.innerText || '').trim();
      return r.width > 50 && txt.length > 15 && !/^(company news|marketing|design|e-?commerce|latest|all|design formats|side hustles|podcast|tutorials?)$/i.test(txt);
    });
    if (!h) return false;
    const card = h.closest('a') || h.closest('[data-framer-name*="Card" i], [class*="card" i]') || h.parentElement;
    card.setAttribute('data-m-mark', t);
    return true;
  }, tag);
  return ok ? page.locator(`[data-m-mark="${tag}"]`) : page.locator('[data-m-mark="__none__"]');
};

// Tags and returns the first ancestor of `sel` that paints a card-sized box —
// the auth "card" on app.glorify.com is a nested .flex column (352x384), not
// a form or a [class*=card] element.
const cardAncestor = async (sel, { minW = 300, minH = 200, maxH = 800, tag = 'm-anc' } = {}) => {
  const ok = await page.evaluate(([s, w, h, mxh, t]) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    let el = document.querySelector(s);
    while (el && el !== document.body) {
      const r = el.getBoundingClientRect();
      if (r.width >= w && r.height >= h && r.height <= mxh) { el.setAttribute('data-m-mark', t); return true; }
      el = el.parentElement;
    }
    return false;
  }, [sel, minW, minH, maxH, tag]);
  return ok ? page.locator(`[data-m-mark="${tag}"]`) : page.locator('[data-m-mark="__none__"]');
};

// Tags and returns the card-sized ancestor of the first leaf whose text
// matches `re` — for the onboarding dropzone, whose own copy ("Drag and
// drop…") is the only reliable hook (the file inputs on the page belong to
// the tool rail's upload tool, not the onboarding zone).
const textCard = async (re, { minW = 150, minH = 80, maxH = 600, tag = 'm-tx' } = {}) => {
  const ok = await page.evaluate(([src, flags, w, h, mxh, t]) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const rx = new RegExp(src, flags);
    const leaf = [...document.querySelectorAll('p,span,div,label')].find((n) => {
      const txt = (n.innerText || '').trim();
      return txt.length < 120 && rx.test(txt) && ![...n.children].some((c) => (c.innerText || '').trim() === txt) && n.getBoundingClientRect().width > 0;
    });
    if (!leaf) return false;
    let el = leaf;
    while (el && el !== document.body) {
      const r = el.getBoundingClientRect();
      if (r.width >= w && r.height >= h && r.height <= mxh) { el.setAttribute('data-m-mark', t); return true; }
      el = el.parentElement;
    }
    return false;
  }, [re.source, re.flags, minW, minH, maxH, tag]);
  return ok ? page.locator(`[data-m-mark="${tag}"]`) : page.locator('[data-m-mark="__none__"]');
};

// The Craft dialog's painted box: one of several .modal__content siblings —
// every other app modal sits in the DOM at 0x0, so only the wrap whose text
// mentions the dialog's own copy ("Add to canvas" / the product description)
// is the open one.
const craftBox = () => q('[class*="modal__content"]').filter({ hasText: /add to canvas|product description|brand name/i }).filter({ visible: true }).last();

// The first element matching `sel` whose trimmed text is at least `min` chars
// (hasText cannot express a trimmed length — /\S{20,}/ means twenty
// *consecutive* non-space characters, which no normal paragraph matches).
const p20 = async (sel, min = 20) => {
  const all = q(sel).filter({ visible: true });
  const n = Math.min(await all.count(), 15);
  for (let i = 0; i < n; i++) {
    const t = ((await all.nth(i).innerText().catch(() => '')) || '').trim();
    if (t.length >= min) return all.nth(i);
  }
  return all.first();
};

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
  shell: 'Site chrome', home: 'Home', pricing: 'Pricing', feature: 'Feature page',
  templates: 'Templates', marketplace: 'Template marketplace', learn: 'Learn',
  submit: 'Submit a template', login: 'App sign-in', register: 'App sign-up',
  designer: 'Anonymous editor', footer: 'Footer', mobile: 'Mobile (390 wide)',
};

// Opens the nav "Features" dropdown — a hover-driven Framer nav item whose
// panel lists the feature pages. A local UI toggle; its links are measured,
// never followed.
async function openFeatures() {
  const btn = q('[data-framer-name="Features"], [data-framer-name*="Feature"], a, div').filter({ hasText: /^Features$/ }).filter({ visible: true }).first();
  if (!(await btn.count())) return 'no Features nav trigger';
  const open = async () => page.evaluate(() => {
    const els = [...document.querySelectorAll('a[href*="features/"], a[href*="mockup"], a[href*="background-remover"]')];
    return els.some((a) => { const r = a.getBoundingClientRect(); return r.y > 40 && r.y < 420 && r.width > 80 && r.height > 10; });
  }).catch(() => false);
  if (await open()) return 'the Features dropdown was already open';
  for (let i = 0; i < 3; i++) {
    await btn.hover({ timeout: 4000 }).catch(() => btn.evaluate((el) => el.dispatchEvent(new MouseEvent('mouseover', { bubbles: true }))));
    await page.waitForTimeout(900);
    if (await open()) return 'hovered the "Features" nav trigger to open its dropdown';
  }
  return 'hovered the "Features" nav trigger; the dropdown did not report open';
}

// Clicks the pricing billing switcher (Monthly/Yearly) — a Framer variant
// toggle that only swaps the displayed prices. A local UI toggle.
async function billingSwitch(re) {
  const hit = await page.evaluate((src) => {
    const rx = new RegExp(src, 'i');
    const els = [...document.querySelectorAll('div, a, button, span, p')].filter((el) => {
      const r = el.getBoundingClientRect();
      const own = (el.innerText || '').trim();
      return r.width > 30 && r.height > 10 && r.y > 0 && r.y < innerHeight && own.length < 30 && rx.test(own) && ![...el.children].some((c) => (c.innerText || '').trim() === own);
    });
    if (!els.length) return false;
    els[0].setAttribute('data-m-billing', '1');
    return true;
  }, re.source);
  if (!hit) return null;
  const el = page.locator('[data-m-billing="1"]').first();
  await clickEl(el, 4000);
  await page.waitForTimeout(1100);
  return el;
}

async function clickEl(loc, ms = 8000) { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); }

// The Craft dialog behind "Try with Placeholder Image", reached on the
// anonymous editor surface.
async function openCraft() {
  const ph = await domFind(page, /Placeholder Image/i, { sel: 'a,button,div,span,p', tag: 'm-ph' });
  if (!(await ph.count())) return 'no Placeholder Image card';
  const hasDialog = async () => (await q('button').filter({ hasText: /Add to canvas/i }).count()) > 0;
  if (await hasDialog()) return 'the Craft dialog was already open';
  await ph.click({ timeout: 6000 }).catch(() => ph.evaluate((el) => el.click()));
  for (let i = 0; i < 20 && !(await hasDialog()); i++) await page.waitForTimeout(1000);
  return (await hasDialog()) ? 'clicked "Try with Placeholder Image" to open the Craft dialog' : 'clicked "Try with Placeholder Image"; the Craft dialog did not report open';
}

// Picks the "Modern" style card in the Craft dialog — the local UI toggle
// that enables "Add to canvas". Never presses the button itself.
async function pickStyle() {
  const st = craftBox().locator('div,button').filter({ hasText: /^Modern$/ }).filter({ visible: true }).last();
  if (!(await st.count())) return 'no Modern style card';
  await clickEl(st, 4000);
  await page.waitForTimeout(1500);
  return 'clicked the "Modern" style card to enable "Add to canvas" — the button itself was never pressed';
}

// Selects the LAYERS inspector tab — a local UI toggle.
async function layersTab() {
  const t = q('div,button,span,a').filter({ hasText: /^LAYERS$/ }).filter({ visible: true }).first();
  if (!(await t.count())) return 'no LAYERS tab';
  await clickEl(t, 4000);
  await page.waitForTimeout(900);
  return 'clicked the LAYERS inspector tab';
}

async function home() {
  if (!(await newPage('home'))) return;
  await sheetsFor('home');
  await chrome('home');
  const g = G.shell;
  await S('page-bg', q('body'), ['default'], { group: g, title: 'Page field', desc: 'The marketing body element — the painted field every page sits on.', sel: 'body' }, { crop: false, noScroll: true });
  await S('mkt-header', q('[data-framer-name="Top nav"], header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Site header', desc: 'The marketing top bar: wordmark, the "Who is it for?"/Features/Resources/Templates dropdowns, Pricing, Login, "Play for free" and "Get Started Now".', sel: '[data-framer-name="Top nav"]' }, { noScroll: true });
  await S('mkt-logo', q('[data-framer-name="Logo + Icon"], [data-framer-name*="Logo"], header a').filter({ visible: true }).first(), ['default'], { group: g, title: 'Logo', desc: 'The Glorify wordmark in the header, linking home.', sel: 'logo framer component' }, { noScroll: true });
  await S('nav-link', q('[data-framer-name="Top nav"] a, header a').filter({ hasText: /^Pricing$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Nav link', desc: 'A marketing header nav link (Pricing); measured, never followed.', sel: 'nav Pricing link' }, { noScroll: true });
  await S('nav-features', q('[data-framer-name="Top nav"] *, [data-framer-name="Top nav"] a').filter({ hasText: /^Features$/ }).filter({ visible: true }).last(), [...B4, 'opened'], { group: g, title: 'Features nav trigger', desc: 'The "Features" nav item that opens the feature-page dropdown on hover.', sel: 'nav Features trigger' }, { noScroll: true, before: { opened: openFeatures } });
  await S('nav-login', q('[data-framer-name="Top nav"] a, header a').filter({ hasText: /^Login$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Login link', desc: 'The "Login" nav action to app.glorify.com/welcome; measured, never followed.', sel: 'nav Login link' }, { noScroll: true });
  await S('nav-play', q('[data-framer-name="Top nav"] a, header a').filter({ hasText: /play for free/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Play for free link', desc: 'The "Play for free" nav action to the anonymous editor on app.glorify.com; measured, never followed.', sel: 'nav Play for free' }, { noScroll: true });
  const h = G.home;
  await S('hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: h, title: 'Hero headline', desc: '"Easily create marketing visuals that turn browsers to buyers." — the display heading.', sel: 'home h1' }, { noScroll: true });
  await S('hero-sub', await p20('p, [data-framer-name] p', 30), ['default'], { group: h, title: 'Hero subline', desc: 'The paragraph under the hero heading ("Enjoy the ultimate Ecom design tool…").', sel: 'hero paragraph' }, { noScroll: true });
  await S('hero-cta', await domFind(page, /play for free/i, { sel: 'a, p, span', tag: 'm-hc', up: 'a, button', nth: 1 }), B4, { group: h, title: 'Hero CTA', desc: 'The hero "Play for free" button to the anonymous editor — an outlined ghost on the dark hero band, not the filled nav button (the leaf text is tagged in-page: the nav\'s identical label is the DOM-first match). Measured, never followed.', sel: 'hero Play for free' }, { noScroll: true });
  await S('home-h2', q('h2').filter({ visible: true }).first(), ['default'], { group: h, title: 'Section heading', desc: 'A section heading on the marketing home.', sel: 'home h2' });
  await S('home-card', await p20('[data-framer-name*="Card"], [class*="card"], [class*="tile"], a[href*="features/"]', 8), ['default', 'hover'], { group: h, title: 'Home card', desc: 'A feature/benefit card on the marketing home.', sel: 'home card' }, { pin: true });
  await S('home-learn-more', q('a').filter({ hasText: /learn more/i }).filter({ visible: true }).first(), B4, { group: h, title: 'Learn more link', desc: 'A "Learn more" link inside a home feature row; measured, never followed.', sel: 'home Learn more link' });
  await S('footer-col', q('[data-framer-name*="Footer"], footer, [class*="footer"]').filter({ visible: true }).last(), ['default'], { group: G.footer, title: 'Footer', desc: 'The marketing footer: sitemap columns, legal and social links.', sel: 'footer' });
  await S('footer-link', q('[data-framer-name*="Footer" i] a, footer a, [class*="footer"] a').filter({ hasText: /^Pricing$|knowledge base|webinars/i }).filter({ visible: true }).first(), B4, { group: G.footer, title: 'Footer link', desc: 'A link inside the marketing footer; measured, never followed.', sel: 'footer link' });
  save();
}

async function pricing() {
  if (!(await newPage('pricing'))) return;
  await sheetsFor('pricing');
  // The pricing header carries the "Get Started Now" button the home header
  // does not; measure it here under the site-chrome group.
  await S('nav-cta', q('[data-framer-name="Button Wrap"]').filter({ visible: true }).first(), B4, { group: G.shell, title: 'Get Started Now button', desc: 'The header "Get Started Now" CTA on /pricing ([data-framer-name="Button Wrap"]); measured, never followed.', sel: '[data-framer-name="Button Wrap"]' }, { noScroll: true });
  const g = G.pricing;
  // The billing switcher labels are leaf p.framer-text nodes; a hasText filter
  // resolves the page wrapper instead, so tag the leaf in-page first.
  const monthly = await domFind(page, /^Monthly$/i, { sel: 'p,div,span,a,button', tag: 'm-mo' });
  const yearly = await domFind(page, /^(yearly|annual|yearly\b.*)$/i, { sel: 'p,div,span,a,button', tag: 'm-yr' });
  await S('bill-monthly', monthly, [...B4, 'opened'], { group: g, title: 'Billing tab (monthly)', desc: 'The "Monthly" side of the pricing billing switcher; opened is the state after clicking it — a local UI toggle.', sel: 'billing Monthly' }, { noScroll: true, before: { opened: async () => ((await billingSwitch(/monthly/i)) ? 'clicked "Monthly" to show monthly prices' : 'no Monthly toggle found') } });
  await S('bill-yearly', yearly, [...B4, 'opened'], { group: g, title: 'Billing tab (yearly)', desc: 'The "Yearly" side of the billing switcher; opened is the state after clicking it — a local UI toggle.', sel: 'billing Yearly' }, { noScroll: true, before: { opened: async () => ((await billingSwitch(/yearly|annual/i)) ? 'clicked "Yearly" to show annual prices' : 'no Yearly toggle found') } });
  await S('plan-card', q('[data-framer-name*="Card Plans" i]').filter({ hasText: /pro|free|trial|\$/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan card', desc: 'A pricing plan card (name, price, feature list, trial CTA) — the Framer "Card/Card Plans Free" component (~230x154).', sel: 'pricing plan card' });
  await S('plan-price', q('h2, [class*="price"], [data-framer-name*="price"]').filter({ hasText: /^\$?\d+$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Plan price', desc: 'The price figure inside a plan card.', sel: 'pricing price' });
  await S('plan-cta', q('a').filter({ hasText: /start pro trial/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Plan CTA', desc: 'A plan card\'s "Start … Trial" action to /dashboard/register; its states were measured but it was never followed — no trial was started.', sel: 'pricing Start Pro Trial' });
  await S('plan-row', await p20('[data-framer-name] li, [data-framer-name] p, li', 8), ['default'], { group: g, title: 'Plan feature row', desc: 'A feature row inside a plan card or the compare table.', sel: 'pricing feature row' });
  await S('compare-h2', q('h2').filter({ hasText: /compare/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Compare heading', desc: 'The "Compare Plans" table heading.', sel: 'pricing Compare Plans' });
  save();
}

async function feature() {
  if (!(await newPage('feature'))) return;
  await sheetsFor('feature');
  const g = G.feature;
  await S('feat-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Feature headline', desc: 'The /features/background-remover page heading.', sel: 'feature h1' }, { noScroll: true });
  await S('feat-cta', await domFind(page, /get started/i, { sel: 'a, p, span', tag: 'm-fc', up: 'a, button', nth: 0 }), B4, { group: g, title: 'Feature CTA', desc: 'The feature hero\'s filled "Get Started Now" action — the nav\'s "Play for free" is the DOM-first match, so the leaf text is tagged in-page. Measured, never followed.', sel: 'feature CTA' });
  await S('feat-card', await p20('[data-framer-name*="Card"], [class*="card"], [data-framer-name*="Fast"], [data-framer-name*="Option"]', 8), ['default', 'hover'], { group: g, title: 'Feature card', desc: 'A benefit card on the feature page ("Fast", "Inexpensive", "Manual Option").', sel: 'feature card' }, { pin: true });
  await S('feat-prose', await p20('[data-framer-name] p, main p, section p, p', 40), ['default'], { group: g, title: 'Feature paragraph', desc: 'A body paragraph on the feature page.', sel: 'feature p' });
  save();
}

async function templates() {
  if (!(await newPage('templates'))) return;
  const g = G.templates;
  await S('tpl-h1', q('h1, h2, h3').filter({ visible: true }).first(), ['default'], { group: g, title: 'Templates headline', desc: 'The templates gallery heading.', sel: 'templates h1' }, { noScroll: true });
  await S('tpl-card', await framerTile(), ['default', 'hover'], { group: g, title: 'Template tile', desc: 'A template thumbnail tile on the /templates draggable canvas (a Framer "Row n - m"/"Beauty n - m" tile with artwork) — the gallery is a pan-canvas, not a link grid.', sel: 'templates tile (data-framer-name tile)' }, { pin: true });
  await S('tpl-cat', q('a').filter({ hasText: /e-?commerce|adverts|social media|videos/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Template category link', desc: 'A template-category link; measured, never followed.', sel: 'templates category link' });
  save();
}

async function marketplace() {
  if (!(await newPage('marketplace'))) return;
  const g = G.marketplace;
  await S('mk-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Marketplace headline', desc: 'The "New template marketplace" heading.', sel: 'marketplace h1' }, { noScroll: true });
  await S('mk-tag', q('a, div, button, span').filter({ hasText: /^All$|^Paid$|^Free$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Marketplace filter', desc: 'A use-case/style filter pill on the marketplace.', sel: 'marketplace filter' });
  await S('mk-card', await imgCard(150), ['default', 'hover'], { group: g, title: 'Marketplace card', desc: 'A template card in the marketplace grid (the first thumbnail link over 150px); measured, never followed.', sel: 'marketplace card (a>img)' }, { pin: true });
  save();
}

async function learn() {
  if (!(await newPage('learn'))) return;
  const g = G.learn;
  await S('learn-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Learn headline', desc: 'The "Learn about Glorify, Ecom, Design and more" heading.', sel: 'learn h1' }, { noScroll: true });
  await S('learn-cat', await domFind(page, /^All$/i, { sel: 'a,button,div,span,p', tag: 'm-lc' }), B4, { group: g, title: 'Learn filter', desc: 'The "All" category pill on the Learn hub; the leaf text node is tagged in-page because a hasText filter resolves the page wrapper.', sel: 'learn filter' });
  await S('learn-card', await titleCard(), ['default', 'hover'], { group: g, title: 'Article card', desc: 'A Learn article card (cover, category tag, title) — the card wrapping the first article-title heading; measured, never followed.', sel: 'learn article card' }, { pin: true });
  await S('learn-tag', q('h3, span, div, a').filter({ hasText: /^Company News$|^Marketing$|^Design$/ }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Article tag', desc: 'A category tag on an article card.', sel: 'learn article tag' });
  save();
}

async function submit() {
  if (!(await newPage('submit'))) return;
  const g = G.submit;
  await S('st-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Submit headline', desc: 'The "Submit your template" heading.', sel: 'submit h1' }, { noScroll: true });
  await S('st-quote', q('[data-framer-name*="Card"], [class*="card"], [data-framer-name*="Privileges"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Privileges card', desc: 'The "Creator Privileges" card on the submit-a-template page.', sel: 'submit card' });
  await S('st-prose', await p20('[data-framer-name] p, p', 40), ['default'], { group: g, title: 'Submit paragraph', desc: 'A guidelines paragraph on the submit page.', sel: 'submit p' });
  save();
}

async function login() {
  if (!(await newPage('login', { wait: 10000 }))) return;
  await sheetsFor('login');
  await chrome('login');
  const g = G.login;
  await S('app-bg', q('body'), ['default'], { group: g, title: 'App page field', desc: 'The app body element — the dark field the auth cards and editor chrome sit on.', sel: 'body' }, { crop: false, noScroll: true });
  await S('login-title', await domFind(page, /^Sign in to your account$/i, { sel: 'p,div,span,h1,h2,h3', tag: 'm-lt' }), ['default'], { group: g, title: 'Sign-in headline', desc: 'The "Sign in to your account" heading (a p leaf) on app.glorify.com/dashboard/login.', sel: 'signin heading' }, { noScroll: true });
  await S('login-card', await cardAncestor('input.field-container__input, input[type="email"], input[type="password"]'), ['default'], { group: g, title: 'Sign-in card', desc: 'The sign-in form card — the flex column (~352px) holding the e-mail and password fields, the primary submit and the Google OAuth button; tagged by walking up from the e-mail input to the first card-sized ancestor.', sel: 'signin card ancestor' }, { noScroll: true });
  await S('login-field', q('input[type="email"], input[name*="mail" i], input[placeholder*="mail" i]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field (sign-in)', desc: 'The sign-in e-mail input; focused and typed into then cleared — never submitted.', sel: 'signin email input' }, { noScroll: true, fillText: 'name@example.com' });
  await S('login-pass', q('input[type="password"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Password field (sign-in)', desc: 'The sign-in password input; focused and typed into then cleared — never submitted.', sel: 'signin password input' }, { noScroll: true, fillText: 'sample-pass-123' });
  await S('login-submit', q('button').filter({ hasText: /^sign ?in$/i }).filter({ visible: true }).first(), [...B4, 'enabled'], { group: g, title: 'Sign-in submit', desc: 'The primary "Sign in" submit; every state was measured but the button was never clicked — nothing was submitted. `enabled` is the fill it paints once sample text sits in both fields.', sel: 'signin submit button' }, { noScroll: true, before: { enabled: async () => {
    const em = q('input[type="email"], input[name*="mail" i]').filter({ visible: true }).first();
    const pw = q('input[type="password"]').filter({ visible: true }).first();
    await em.click({ timeout: 4000 }).catch(() => em.evaluate((el) => el.focus())); await page.keyboard.type('name@example.com', { delay: 8 });
    await pw.click({ timeout: 4000 }).catch(() => pw.evaluate((el) => el.focus())); await page.keyboard.type('sample-pass-123', { delay: 8 });
    await page.waitForTimeout(500);
    return 'typed sample text into both fields so the submit enabled — still never clicked';
  } }, after: { enabled: async () => {
    for (const sel of ['input[type="email"]', 'input[type="password"]']) {
      const f = q(sel).filter({ visible: true }).first();
      await f.click({ timeout: 2000 }).catch(() => f.evaluate((el) => el.focus()));
      await page.keyboard.press('ControlOrMeta+a'); await page.keyboard.press('Backspace');
    }
    await page.waitForTimeout(300);
  } } });
  await S('login-google', q('button, a').filter({ hasText: /google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Google OAuth button', desc: 'The "Sign in with Google" OAuth button; measured, never activated.', sel: 'signin Google button' }, { noScroll: true });
  await S('login-forgot', q('a, button, span, label').filter({ hasText: /forgot|restore|remember/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Forgot/remember control', desc: 'The "Forgot password?" link or "Remember me" checkbox label on the sign-in card; measured, never followed.', sel: 'signin forgot/remember' }, { noScroll: true });
  await S('login-signup', q('a, button, span').filter({ hasText: /sign ?up|create.*account|register/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-up link', desc: 'The "Sign up" link beside the sign-in form; measured, never followed.', sel: 'signin signup link' }, { noScroll: true });
  save();
}

async function register() {
  if (!(await newPage('register', { wait: 10000 }))) return;
  const g = G.register;
  await S('reg-title', await domFind(page, /^Create your account$/i, { sel: 'p,div,span,h1,h2,h3', tag: 'm-rt' }), ['default'], { group: g, title: 'Sign-up headline', desc: 'The "Create your account" heading (a p leaf) on app.glorify.com/dashboard/register.', sel: 'signup heading' }, { noScroll: true });
  await S('reg-name', q('input[placeholder*="name" i], input[name*="name" i], input[type="text"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Name field (sign-up)', desc: 'The sign-up "Full name" input; focused and typed into then cleared — never submitted.', sel: 'signup name input' }, { noScroll: true, fillText: 'Example User' });
  await S('reg-email', q('input[type="email"], input[name*="mail" i], input[placeholder*="mail" i]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Email field (sign-up)', desc: 'The sign-up e-mail input; focused and typed into then cleared — never submitted.', sel: 'signup email input' }, { noScroll: true, fillText: 'name@example.com' });
  await S('reg-pass', q('input[type="password"]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Password field (sign-up)', desc: 'The sign-up password input; focused and typed into then cleared — never submitted.', sel: 'signup password input' }, { noScroll: true, fillText: 'sample-pass-123' });
  await S('reg-submit', q('button').filter({ hasText: /^sign ?up$/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Sign-up submit', desc: 'The primary sign-up submit; its states were measured but the button was never clicked — no account was created.', sel: 'signup submit button' }, { noScroll: true });
  await S('reg-google', q('button, a').filter({ hasText: /google/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Google OAuth button (sign-up)', desc: 'The "Sign up with Google" button; measured, never activated.', sel: 'signup Google button' }, { noScroll: true });
  await S('reg-terms', q('a').filter({ hasText: /terms|privacy/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Terms link', desc: 'The terms/privacy link under the sign-up form; measured, never followed.', sel: 'signup terms link' }, { noScroll: true });
  save();
}

async function designer() {
  if (!(await newPage('designer', { wait: 16000 }))) return;
  await sheetsFor('designer');
  await chrome('designer');
  const g = G.designer;
  // The upload onboarding the anonymous /file/<id> route paints first.
  await S('ob-title', q('h1, h2, h3, [class*="title" i]').filter({ hasText: /generate designs|uploading|glorify/i }).filter({ visible: true }).first(), ['default'], { group: g, title: 'Onboarding headline', desc: 'The "Generate designs for your campaign" heading on the anonymous editor\'s upload screen.', sel: 'onboarding heading' }, { noScroll: true });
  await S('ob-drop', await textCard(/drag\s*(and|&|n'?)\s*drop|choose file|drop your/i, { tag: 'm-drop' }), ['default'], { group: g, title: 'Upload dropzone', desc: 'The onboarding upload dropzone — the card-sized ancestor of the "Drag and drop…" prompt; measured at rest — no file was ever chosen or uploaded.', sel: 'onboarding dropzone (text ancestor)' }, { noScroll: true });
  await S('ob-ph', q('a,button,div,span').filter({ hasText: /Placeholder Image/i }).filter({ visible: true }).last(), B4, { group: g, title: 'Placeholder Image card', desc: 'The "Try with Placeholder Image" card — the product\'s own demo path into the canvas; measured, and only ever activated through its own spec flow.', sel: 'onboarding placeholder card' }, { noScroll: true });
  await S('ob-own', q('a,button,div,span').filter({ hasText: /get started on my own/i }).filter({ visible: true }).last(), B4, { group: g, title: 'Own-start link', desc: 'The "I\'ll get started on my own" link (it bounces to /dashboard/register signed out); measured, never followed.', sel: 'onboarding own-start link' }, { noScroll: true });
  // The editor shell behind and around the Craft dialog.
  await S('ed-header', q('header.app-header, header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Editor header', desc: 'The editor top bar: file name dropdown, Login/Signup, zoom, Share, Download.', sel: 'header.app-header' }, { noScroll: true });
  await S('ed-login', q('button').filter({ hasText: /^Login$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Editor Login button', desc: 'The outlined "Login" button in the editor header; measured, never clicked.', sel: 'editor Login button' }, { noScroll: true });
  await S('ed-signup', q('button').filter({ hasText: /^Signup$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Editor Signup button', desc: 'The filled "Signup" button in the editor header; measured, never clicked.', sel: 'editor Signup button' }, { noScroll: true });
  await S('ed-share', q('button').filter({ hasText: /^Share$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Share button', desc: 'The "Share" button in the editor header; measured, never clicked.', sel: 'editor Share button' }, { noScroll: true });
  await S('ed-download', q('button').filter({ hasText: /^Download$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Download button', desc: 'The "Download" button in the editor header; measured, never clicked.', sel: 'editor Download button' }, { noScroll: true });
  await S('ed-zoom', q('button.dropdown__trigger, .dropdown__trigger').filter({ hasText: /%$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Zoom control', desc: 'The zoom-percentage dropdown trigger in the editor header; measured, never toggled.', sel: 'editor zoom trigger' }, { noScroll: true });
  await S('ed-tool', q('button.dropdown-toolbar, .dropdown-toolbar').filter({ hasText: /^(Text|Video|Elements|Graphics|Uploads|Photos)$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Tool rail button', desc: 'A labelled tool-rail button (Text/Video/Elements…) on the editor\'s left rail — 48x48 .dropdown-toolbar buttons over a 20px icon; its flyout was never opened.', sel: '.dropdown-toolbar tool' }, { noScroll: true });
  await S('ed-tool-active', q('.dropdown-toolbar.dropdown--icon-active').filter({ visible: true }).first(), ['default'], { group: g, title: 'Active tool button', desc: 'The selected tool on the left rail (Pointer, marked dropdown--icon-active).', sel: '.dropdown-toolbar.dropdown--icon-active' }, { noScroll: true });
  await S('ed-inspector', q('.panel--inspector').filter({ visible: true }).first(), ['default'], { group: g, title: 'Inspector panel', desc: 'The right-hand inspector (.panel--inspector, ~280px): EDIT/LAYERS/PAGES tabs over the Page Background and Color controls.', sel: '.panel--inspector' }, { noScroll: true });
  // The hex field sits on the EDIT pane, so it is measured before the LAYERS
  // toggle below swaps the panels.
  await S('ed-color', q('input[placeholder="000"], .panel--inspector input[type="text"]').filter({ visible: true }).first(), ['default', 'focused'], { group: g, title: 'Inspector colour field', desc: 'The page-background colour input in the inspector (the hex field, placeholder "000"); focused, never typed into.', sel: 'inspector colour input' }, { noScroll: true });
  await S('ed-tab', q('div,button,span,a').filter({ hasText: /^EDIT$/ }).filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Inspector tab', desc: 'The EDIT inspector tab; opened was measured after switching to LAYERS — a local UI toggle.', sel: 'inspector EDIT tab' }, { noScroll: true, before: { opened: layersTab } });
  await S('ed-tab-layers', q('div,button,span,a').filter({ hasText: /^LAYERS$/ }).filter({ visible: true }).first(), B4, { group: g, title: 'Layers tab', desc: 'The LAYERS inspector tab; measured at rest.', sel: 'inspector LAYERS tab' }, { noScroll: true });
  // The Craft dialog needs the placeholder path opened first. Every other app
  // modal sits hidden at 0x0 in the DOM, so the dialog specs below are scoped
  // to the .modal__content whose text mentions the dialog's own copy.
  await S('ed-craft', craftBox(), ['default'], { group: g, title: 'Craft dialog', desc: 'The "Craft Professional Assets" dialog (.modal__content): brand name, product description, the style grid, the image pane and "Add to canvas".', sel: 'craft dialog' }, { noScroll: true, open: openCraft });
  // Both Craft fields are <textarea>s — the 307x32 brand line and the 307x73
  // description box, distinguished by placeholder.
  await S('ed-craft-field', craftBox().locator('textarea[placeholder*="brand" i]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Brand-name field', desc: 'The "Enter your brand name" textarea in the Craft dialog; focused and typed into then cleared — never used.', sel: 'craft brand textarea' }, { noScroll: true, fillText: 'Example Brand' });
  await S('ed-craft-area', craftBox().locator('textarea[placeholder*="description" i], textarea[placeholder*="product" i]').filter({ visible: true }).first(), FIELD, { group: g, title: 'Description area', desc: 'The "Write a short description about your product" textarea; focused and typed into then cleared — never used.', sel: 'craft description textarea' }, { noScroll: true, fillText: 'A sample product description' });
  await S('ed-craft-style', craftBox().locator('div,button').filter({ hasText: /^Modern$/ }).filter({ visible: true }).last(), [...B4, 'opened'], { group: g, title: 'Style card', desc: 'A style card in the Craft dialog grid (Modern); opened is the selected state after clicking it — a local UI toggle that enables "Add to canvas".', sel: 'craft style card' }, { noScroll: true, before: { opened: pickStyle } });
  await S('ed-add', craftBox().locator('button').filter({ hasText: /add to canvas/i }).filter({ visible: true }).first(), [...B4, 'enabled'], { group: g, title: 'Add to canvas', desc: 'The Craft dialog\'s primary submit — disabled until a style is picked; `enabled` is the fill after the style click. The button itself was never pressed in this pass.', sel: 'craft Add to canvas' }, { noScroll: true, before: { enabled: pickStyle } });
  await S('ed-replace', craftBox().locator('button').filter({ hasText: /replace/i }).filter({ visible: true }).first(), B4, { group: g, title: 'Replace image button', desc: 'The "Replace" button on the Craft dialog\'s image pane; measured, never clicked.', sel: 'craft Replace button' }, { noScroll: true });
  await S('ed-close', craftBox().locator('.modal__close, button[class*="close" i], button[aria-label*="close" i]').filter({ visible: true }).first(), B4, { group: g, title: 'Dialog close', desc: 'The Craft dialog\'s own close button; measured, never clicked.', sel: '.modal__close inside craft dialog' }, { noScroll: true });
  save();
}

async function mobile() {
  if (!(await newPage('mobile', { mobile: true, url: BASE + '/' }))) return;
  await chrome('mobile');
  const g = G.mobile;
  await S('m-topbar', q('[data-framer-name="Top nav"], header').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile top bar', desc: 'The phone header at 390 wide: wordmark, the burger and the actions that survive the width.', sel: 'mobile top nav' }, { noScroll: true });
  await S('m-burger', q('[data-framer-name="Menu Icon"], button[aria-label*="menu" i]').filter({ visible: true }).first(), [...B4, 'opened'], { group: g, title: 'Mobile burger', desc: 'The nav burger at 390 wide (the 60x60 "Menu Icon" — the overlay it opens is the [data-framer-name="Menu"] panel); opened was measured after tapping it.', sel: '[data-framer-name="Menu Icon"]' }, { noScroll: true, before: { opened: async (loc) => { await loc.tap({ timeout: 4000 }).catch(() => loc.click({ timeout: 4000 }).catch(() => loc.evaluate((el) => el.click()))); await page.waitForTimeout(1200); return 'tapped the nav "Menu Icon" to open the mobile menu'; } } });
  await S('m-menu-link', q('[data-framer-name="Menu"] a, nav a, a[href*="features/"]').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile menu link', desc: 'A link inside the opened mobile nav menu.', sel: 'mobile menu link' }, { noScroll: true });
  await S('m-hero-h1', q('h1').filter({ visible: true }).first(), ['default'], { group: g, title: 'Mobile hero headline', desc: 'The hero display heading at 390 wide.', sel: 'mobile h1' });
  await S('m-hero-cta', await domFind(page, /play for free/i, { sel: 'a, p, span', tag: 'm-mhc', up: 'a, button', nth: 1 }), B4, { group: g, title: 'Mobile hero CTA', desc: 'The hero action at 390 wide — the same outlined ghost as desktop, centred under the hero copy (the DOM-first "Play for free" is the menu overlay\'s full-width filled button, so the leaf text is tagged in-page). Measured, never followed.', sel: 'mobile hero CTA' });
  save();
}

run = new Date().toISOString().slice(0, 10);
out._meta.read = run;
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); glorify.com paints light only — no theme toggle or dark media query on any signed-out route — while app.glorify.com paints its dark chrome on the auth cards and the anonymous editor';
out._meta.tool = 'tools/capture/public/measure.mjs';
const { browser, context: ctx0 } = await launch();
context = ctx0;
const pages = process.argv.slice(2);
const plan = { home, pricing, feature, templates, marketplace, learn, submit, login, register, designer, mobile };
const order = Object.keys(plan).filter((k) => !pages.length || pages.includes(k));
const finishedPages = new Set();
try {
  for (const k of order) { if (k !== 'mobile') { await plan[k](); finishedPages.add(k); } }
  if (!pages.length || pages.includes('mobile')) { await plan.mobile(); finishedPages.add('mobile'); }
  // Reduced-motion check on an element that transitions (the nav link's
  // hover), so the delta is meaningful.
  if (!pages.length || pages.includes('home')) await reducedMotion('home', '[data-framer-name="Top nav"] a, header a');
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
