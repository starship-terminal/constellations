// Measures helloivy.co's signed-out components on its public pages, in
// every state that can be reached without signing in or submitting
// anything — plus the matching chrome on app.helloivy.co's public surfaces:
// /login (the auth boundary card, at rest only) and the publicly shared
// "Media kit" document page the marketing footer links to.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs [page ...]
//
// Pages: home pricing features blog doc-post share login mobile.
// Writes raw/components-computed.json (merged, so a subset of pages can be
// re-run) and one crop per component and state into components/crops/.
// raw/measurements.md is then built from the JSON by
// build-measurements.mjs.
//
// States:
//   hover          real mouse hover, 500ms settle for transitions
//   focus-visible  keyboard: focus, Shift+Tab, Tab, so the browser sees a keyboard focus
//   pressed        CDP CSS.forcePseudoState [active, hover]; no mouse button is pressed,
//                  so no link or button can fire
//   dark           the same element after the footer "Change theme" toggle
//                  repaints html[toggle-theme=dark], verified by the painted
//                  surface — setTheme in lib.mjs
//   opened         a resting state reached by the component's own toggle:
//                  the nav menu overlay, a pricing FAQ row, the share page's
//                  own Settings menu
//   focused        the login field clicked into — nothing is typed
// Nothing is typed, sent, bought or signed into. The login card's fields
// are measured at rest (and focused, nothing entered); "Continue" and
// "Login with Google" are never pressed. The only presses are local UI
// toggles the page's own chrome provides.
import fs from 'node:fs';
import path from 'node:path';
import { chromium, BASE, APP, SHARE, M, open, closePromo, setTheme, paintedTheme, styleOf, crop, centre, domFind, patch, UA, UA_MOBILE, RAW } from './lib.mjs';
import { safeUrl } from '../safe-url.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= {};
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

const URLS = {
  home: BASE + '/',
  pricing: BASE + '/pricing',
  features: BASE + '/features',
  blog: BASE + '/blog',
  'doc-post': BASE + '/docs',
  login: APP + '/login',
  share: SHARE,
};
const isApp = (key) => ['login', 'share'].includes(key);

let page, cdp, context, current, currentUrl;

// ---------- state drivers ----------

async function reset() {
  await page.keyboard.press('Escape').catch(() => {});
  // The Framer menu overlay ignores Escape: when a state left it open the
  // clean recovery is a reload — every later element read and crop would
  // otherwise be the overlay, not the component.
  const overlayOpen = await page.evaluate(() => [...document.querySelectorAll('*')].some((e) => e !== document.documentElement && e !== document.body && /01\s*HOME/i.test(e.innerText || '') && /FEATURES/i.test(e.innerText || '') && (e.innerText || '').length < 4000 && e.getBoundingClientRect().height > 300)).catch(() => false);
  if (overlayOpen && currentUrl) { await open(page, currentUrl, { wait: 8000 }); await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {}); }
  // open() leaves the tab on about:blank when a reload was blocked; every
  // state after that fails here, so the saved readings are kept
  if (page.url() === 'about:blank') throw new Error('the page was lost to a blocked reload; saved readings kept');
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  const vw = page.viewportSize()?.width ?? 1440;
  await page.mouse.move(vw - 2, 2);
  await page.waitForTimeout(300);
}

async function hover(loc) {
  await centre(loc);
  const b = await loc.boundingBox();
  if (b) { await page.mouse.move(b.x + b.width / 2, b.y + b.height / 2); await page.waitForTimeout(600); }
}

async function kbFocus(loc) {
  await loc.evaluate((el) => el.focus());
  await page.keyboard.press('Shift+Tab');
  await page.keyboard.press('Tab');
  await page.waitForTimeout(400);
  // The attempt is only evidence when focus really came back to the element
  // and paints the :focus-visible ring — anything else is a resting reading,
  // recorded under the "focus failed" via rather than claimed as a state.
  return await loc.evaluate((el) => {
    const ae = document.activeElement;
    const held = ae === el || el.contains(ae);
    let ring = false;
    try { ring = Boolean((ae && ae.matches(':focus-visible')) || el.matches(':focus-visible')); } catch { /* unpierceable */ }
    return { held, ring };
  }).catch(() => ({ held: false, ring: false }));
}

// Pick one element out of a selector's matches inside the page — marks the
// winner with data-m-mark="<tag>" and returns a locator for it. score(el, r,
// cs) returns a number, lowest wins; return Infinity to skip a match.
async function pick(p, sel, score, tag = 'pk') {
  const ok = await p.evaluate(([s, t, src]) => {
    document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
    const fn = new Function('el', 'r', 'cs', `return (${src})(el, r, cs)`);
    let best = null, bestV = Infinity;
    for (const el of document.querySelectorAll(s)) {
      const r = el.getBoundingClientRect();
      if (!r.width || !r.height) continue;
      const cs = getComputedStyle(el);
      if (cs.visibility === 'hidden' || cs.opacity === '0') continue;
      const v = fn(el, r, cs);
      if (v < bestV) { bestV = v; best = el; }
    }
    if (!best) return false;
    best.setAttribute('data-m-mark', t);
    return true;
  }, [sel, tag, score.toString()]);
  return ok ? p.locator(`[data-m-mark="${tag}"]`) : p.locator('[data-m-mark="__none__"]');
}

// CSS.forcePseudoState through CDP: the press never happens, so no link can
// navigate and no button can fire.
async function pressOn(loc) {
  // Force :active:hover on the component element itself, never the topmost
  // node at its centre (a text span or an svg), so the component's own
  // :active rule applies (2026-11 audit, finding 12-6; not run since).
  await cdp.send('DOM.getDocument').catch(() => {});
  await loc.evaluate((el) => el.setAttribute('data-press-target', '1'));
  try {
    const { result } = await cdp.send('Runtime.evaluate', { expression: `document.querySelector('[data-press-target]')`, returnByValue: false });
    // an unresolved target throws, so the state records an error instead of
    // a resting reading labelled pressed
    if (!result || !result.objectId) throw new Error('press target not resolvable');
    const { nodeId } = await cdp.send('DOM.requestNode', { objectId: result.objectId });
    if (!nodeId) throw new Error('press target has no DOM node');
    await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: ['active', 'hover'] });
    await page.waitForTimeout(400);
    return nodeId;
  } finally {
    await loc.evaluate((el) => el.removeAttribute('data-press-target')).catch(() => {});
  }
}
const pressOff = (id) => id == null ? null : cdp.send('CSS.forcePseudoState', { nodeId: id, forcedPseudoClasses: [] }).catch(() => {});

// The nav bar on the marketing pages: the top strip Framer mounts as
// data-framer-name "Desktop" (1392x116 at 1440px) or "Mobile" at 390px —
// the element holding the logo + nav links + "Get Started" + menu box.
const NAV = () => page.evaluate(() => {
  const el = [...document.querySelectorAll('[data-framer-name]')]
    .filter((e) => {
      const r = e.getBoundingClientRect();
      if (r.top > 60 || r.width < 300 || r.height > 200 || r.height === 0) return false;
      if (!/desktop|mobile|nav|header|top|bar/i.test(e.getAttribute('data-framer-name') || '')) return false;
      let anc = e;
      while (anc && anc !== document.documentElement) { const cs = getComputedStyle(anc); if (cs.display === 'none' || cs.visibility === 'hidden') return false; anc = anc.parentElement; }
      return true;
    })[0];
  if (el) el.setAttribute('data-m-mark', 'nav');
  return Boolean(el);
});

// ---------- the component specs ----------
// find: page -> Locator. states: name -> 'hover' | 'focus-visible' |
// 'pressed' | 'dark' | 'opened:label' | (loc, page) => Promise<void>.
const via = { 'hover': 'mouse hover over the element', 'focus-visible': 'keyboard focus (Shift+Tab, Tab)', 'pressed': 'CDP CSS.forcePseudoState(:active:hover) — no real press', 'dark': 'same element after the footer "Change theme" toggle repaints html[toggle-theme=dark]' };

const NAV_SPECS = [
  { key: 'nav-bar', group: 'Site chrome', title: 'Top navigation bar',
    desc: 'The fixed top strip: the Hello Ivy wordmark, Features / Pricing / About / Docs / Blog links, the "Get Started" CTA and the bordered menu box.',
    sel: 'header/nav (top strip)', find: async (p) => { await NAV(); return p.locator('[data-m-mark="nav"]'); }, states: ['default', 'dark'] },
  { key: 'nav-link', group: 'Site chrome', title: 'Nav link',
    desc: 'A nav item in the top strip ("Pricing").',
    sel: 'nav link', find: async (p) => await domFind(p, /^Pricing$/i, { sel: 'a, div, p', tag: 'nl', minW: 30 }), states: ['default', 'hover', 'focus-visible'] },
  { key: 'nav-cta', group: 'Site chrome', title: '"Get Started" nav button',
    desc: 'The solid call-to-action at the right of the nav — links to app.helloivy.co; measured, never followed.',
    sel: 'a/button (text Get Started)', find: async (p) => await domFind(p, /get started/i, { sel: 'a, button, div', tag: 'nc', minW: 60, minH: 20 }), states: ['default', 'hover', 'focus-visible', 'pressed', 'dark'] },
  { key: 'nav-menu-box', group: 'Site chrome', title: 'Menu box',
    desc: 'The bordered hamburger box at the nav\'s right edge — opens the 01 HOME / 02 FEATURES … overlay. "opened" is its own press, closed with Escape.',
    sel: '[data-framer-name="Menu"]', find: async (p) => {
      const ok = await p.evaluate(() => {
        const el = [...document.querySelectorAll('[data-framer-name="Menu"], [data-framer-name="menu"]')].filter((e) => {
          const r = e.getBoundingClientRect();
          if (r.width === 0 || r.top > 200) return false;
          let anc = e;
          while (anc && anc !== document.documentElement) { const cs = getComputedStyle(anc); if (cs.display === 'none' || cs.visibility === 'hidden') return false; anc = anc.parentElement; }
          return true;
        })[0];
        if (el) el.setAttribute('data-m-mark', 'mb');
        return Boolean(el);
      });
      return p.locator(ok ? '[data-m-mark="mb"]' : '[data-m-mark="__none__"]');
    }, states: ['default', 'hover',
      { name: 'opened', via: 'the menu box\'s own press (overlay open; reloaded afterwards)', fn: async (loc) => {
        await loc.click({ timeout: 4000 }).catch(() => {});   // a locator press scrolls into view first
        await page.waitForTimeout(2500);
        // The overlay box, not the page: html/body match the text test when
        // the overlay never opened, so they are excluded and the smallest
        // painted subtree holding the link list wins. No overlay = a failed
        // state, never a reading of the document.
        const ov = await page.evaluate(() => {
          const els = [...document.querySelectorAll('*')].filter((e) => {
            if (e === document.documentElement || e === document.body) return false;
            const t = e.innerText || '';
            if (!/0?1\s*HOME/i.test(t) || !/FEATURES/i.test(t) || t.length >= 4000) return false;
            return e.getBoundingClientRect().height > 300;
          }).sort((a, b) => a.querySelectorAll('*').length - b.querySelectorAll('*').length);
          const el = els[0];
          if (el) el.setAttribute('data-m-mark', 'mov');
          return Boolean(el);
        });
        if (!ov) throw new Error('the menu overlay never painted open');
        return page.locator('[data-m-mark="mov"]');
      } },
    ] },
];

const HERO_SPECS = [
  { key: 'hero-heading', group: 'Marketing', title: 'Hero heading (h1)',
    desc: 'The page\'s headline — the largest display type on the site.',
    sel: 'h1', find: (p) => p.locator('h1').filter({ visible: true }).first(), states: ['default', 'dark'] },
  { key: 'hero-copy', group: 'Marketing', title: 'Hero paragraph',
    desc: 'The supporting paragraph under the headline.',
    sel: 'p (sentence)', find: async (p) => await pick(p, 'p, div, span', (el, r) => {
      const t = (el.innerText || '').trim();
      if (t.length < 40 || t.length > 400) return Infinity;
      if (!/\S+(\s+\S+){7,}/.test(t)) return Infinity;
      return el.querySelectorAll('*').length;
    }, 'hc'), states: ['default'] },
  { key: 'hero-cta', group: 'Marketing', title: 'Hero call-to-action',
    desc: 'The trial CTA — the floating "Try it for free" pill painted bottom-right on the marketing pages — links to the app, measured never followed.',
    sel: 'a/button (trial CTA, outside the nav)', find: async (p) => {
      // Never the nav\'s "Get Started": anything inside the marked top
      // strip is excluded, and the trial pill sits below it.
      const ok = await p.evaluate(() => {
        const nav = document.querySelector('[data-m-mark="nav"]');
        const els = [...document.querySelectorAll('a, button, div')].filter((e) => {
          if (nav && nav.contains(e)) return false;
          const t = (e.innerText || '').trim();
          if (!/try it for free|free trial|start for free/i.test(t) || t.length > 40) return false;
          const r = e.getBoundingClientRect();
          if (r.width < 60 || r.height < 20 || r.top < 140) return false;
          let anc = e;
          while (anc) { const cs = getComputedStyle(anc); if (cs.display === 'none' || cs.visibility === 'hidden') return false; anc = anc.parentElement; }
          return true;
        });
        const el = els.filter((e) => !els.some((o) => o !== e && e.contains(o)))[0] || els[0];
        if (el) el.setAttribute('data-m-mark', 'ht');
        return Boolean(el);
      });
      return p.locator(ok ? '[data-m-mark="ht"]' : '[data-m-mark="__none__"]');
    }, states: ['default', 'hover', 'focus-visible', 'pressed', 'dark'] },
  { key: 'section-heading', group: 'Marketing', title: 'Section heading (h3)',
    desc: 'A mid-page section heading — the page\'s display type below the h1.',
    sel: 'h3', find: (p) => p.locator('h3').filter({ visible: true }).first(), states: ['default', 'dark'] },
  { key: 'footer', group: 'Site chrome', title: 'Footer',
    desc: 'The page footer: product/resource columns, the social icons, the "Change theme" control and the "Try it for free" CTA.',
    sel: 'footer (the whole block)', find: async (p) => await pick(p, 'footer, [data-framer-name*="footer" i], div, section', (el, r, cs) => {
      if (r.width < 600 || r.height < 120) return Infinity;
      const t = el.innerText || '';
      // The footer block, not the copyright line: its link columns and the
      // "Change theme" control must all live inside the measured box.
      if (!/© 20\d\d Hello Ivy|Hello Ivy Inc/i.test(t)) return Infinity;
      if (!/change theme/i.test(t)) return Infinity;
      if (!/features/i.test(t) || !/blog|about|pricing/i.test(t)) return Infinity;
      return el.querySelectorAll('*').length;
    }, 'ft'), states: ['default', 'dark'] },
  { key: 'theme-control', group: 'Site chrome', title: '"Change theme" control',
    desc: 'The footer\'s own theme toggle — the control that repaints html[toggle-theme] and writes localStorage.currentToggleState. Measured at rest; the painted dark pass lives on the `dark` states of other components.',
    sel: 'footer leaf (text Change theme)', find: async (p) => await domFind(p, /^Change theme$/i, { sel: 'div,span,p,a,button', tag: 'tc', minW: 40 }), states: ['default', 'hover'] },
  { key: 'footer-link', group: 'Site chrome', title: 'Footer link',
    desc: 'A footer column link (a product page) — an anchor inside the measured footer block.',
    sel: 'a inside the footer block', find: async (p) => {
      // Scoped to the footer found above: a bare page search lands on the
      // nav\'s "Pricing" first.
      const ok = await p.evaluate(() => {
        const f = document.querySelector('[data-m-mark="ft"]');
        if (!f) return false;
        const a = [...f.querySelectorAll('a')].filter((e) => {
          const r = e.getBoundingClientRect();
          const cs = getComputedStyle(e);
          return r.width > 20 && r.height > 8 && cs.visibility !== 'hidden' && cs.display !== 'none'
            && /features|pricing|blog|docs|about|terms/i.test((e.innerText || '').trim());
        })[0];
        if (a) a.setAttribute('data-m-mark', 'fl');
        return Boolean(a);
      });
      return p.locator(ok ? '[data-m-mark="fl"]' : '[data-m-mark="__none__"]');
    }, states: ['default', 'hover'] },
];

const PRICING_SPECS = [
  { key: 'plan-card', group: 'Pricing', title: 'Plan card',
    desc: 'A pricing card ("Grow" / "Business" / "Enterprise"): name, price, allowance rows and its CTA.',
    sel: 'box (priced plan with its own CTA)', find: async (p) => await pick(p, 'div, section, article', (el, r) => {
      if (r.width < 240 || r.width > 800 || r.height < 200) return Infinity;
      const t = el.innerText || '';
      if (!/\$\s*\d/.test(t) || !/per user/i.test(t)) return Infinity;
      // A plan card carries its own call-to-action; the "one monthly fee"
      // aside that also quotes a price does not.
      if (![...el.querySelectorAll('a, button')].some((b) => /try|start|talk|choose|sign up/i.test((b.innerText || '').trim()))) return Infinity;
      return el.querySelectorAll('*').length;
    }, 'pc'), states: ['default', 'dark'] },
  { key: 'plan-cta', group: 'Pricing', title: 'Plan CTA button',
    desc: 'A plan\'s call-to-action inside the measured plan card — links to the app; measured, never followed.',
    sel: 'a/button inside the plan card', find: async (p) => {
      // Scoped to the plan card found above: a bare page search lands on
      // the nav\'s "Get Started" first.
      const ok = await p.evaluate(() => {
        const card = document.querySelector('[data-m-mark="pc"]');
        if (!card) return false;
        const b = [...card.querySelectorAll('a, button')].filter((e) => {
          const r = e.getBoundingClientRect();
          const cs = getComputedStyle(e);
          return r.width > 40 && r.height > 16 && cs.visibility !== 'hidden' && cs.display !== 'none'
            && /try|start|talk|choose|sign/i.test((e.innerText || '').trim());
        })[0];
        if (b) b.setAttribute('data-m-mark', 'pct');
        return Boolean(b);
      });
      return p.locator(ok ? '[data-m-mark="pct"]' : '[data-m-mark="__none__"]');
    }, states: ['default', 'hover', 'focus-visible', 'pressed'] },
  { key: 'faq-question', group: 'Pricing', title: 'FAQ accordion question',
    desc: 'A question row in the pricing FAQ. "opened" is its own press revealing the answer, pressed again to close.',
    sel: 'row (text Is Hello Ivy only useful for design teams?)', find: async (p) => await domFind(p, /is hello ivy only useful for design teams/i, { sel: 'div,p,h1,h2,h3,button,a', tag: 'fq', minW: 100 }), states: ['default', 'hover',
      { name: 'opened', via: 'the question row\'s own press (answer visible; pressed again to close)', fn: async (loc) => {
        const before = await page.evaluate(() => document.documentElement.scrollHeight);
        await loc.click({ timeout: 4000 }).catch(() => {});   // a locator press scrolls into view first
        await page.waitForTimeout(1200);
        // Opened means the page grew (the answer pushed content down) or a
        // row reported expanded — a silent miss records a failed state,
        // never a second reading of the closed row.
        const grew = await page.evaluate((h) => document.documentElement.scrollHeight > h + 20, before);
        const expanded = await page.evaluate(() => Boolean(document.querySelector('[aria-expanded="true"]')));
        if (!grew && !expanded) throw new Error('the FAQ row press opened no answer');
      } },
    ] },
];

const FEATURE_SPECS = [
  { key: 'feature-card', group: 'Features', title: 'Feature card',
    desc: 'A feature tile on /features — an illustration, name and description.',
    sel: 'box (feature tile)', find: async (p) => await pick(p, 'div, section, article', (el, r) => {
      if (r.width < 150 || r.width > 700) return Infinity;
      const t = el.innerText || '';
      if (!/tasks|feed|chat|docs|files|roadmap|calendar|annotate|client portal|version control/i.test(t)) return Infinity;
      return el.querySelectorAll('*').length;
    }, 'fc'), states: ['default', 'hover'] },
];

const BLOG_SPECS = [
  { key: 'post-card', group: 'Blog', title: 'Post card',
    desc: 'A post row/card on the blog index — cover, title, excerpt, date.',
    sel: 'box (post card)', find: async (p) => await pick(p, 'a, article, div, li', (el, r) => {
      if (r.width < 150 || r.width > 900) return Infinity;
      const t = el.innerText || '';
      if (t.length < 30 || t.length > 600) return Infinity;
      const href = el.getAttribute('href') || el.querySelector('a[href*="/blog/"]')?.getAttribute('href') || '';
      if (!href.includes('/blog/')) return Infinity;
      return el.querySelectorAll('*').length;
    }, 'bc'), states: ['default', 'hover'] },
];

const DOCS_SPECS = [
  { key: 'docs-nav', group: 'Docs', title: 'Docs sidebar',
    desc: 'The docs index navigation — the section list (Getting Started, Main tools, …) beside the content.',
    sel: 'aside/nav (docs sections)', find: async (p) => await pick(p, 'aside, nav, div', (el, r) => {
      if (r.width < 120 || r.width > 600) return Infinity;
      const t = el.innerText || '';
      if (!/getting started/i.test(t) || !/project tools|main tools|team collaboration/i.test(t)) return Infinity;
      return el.querySelectorAll('*').length;
    }, 'dn'), states: ['default', 'dark'] },
  { key: 'docs-link', group: 'Docs', title: 'Docs nav link',
    desc: 'A docs section/article link.',
    sel: 'docs a', find: async (p) => await domFind(p, /create a project|getting started/i, { sel: 'a, div, p', tag: 'dl', minW: 40 }), states: ['default', 'hover'] },
];

// ---- app.helloivy.co: the public login card, at rest only ----
const LOGIN_SPECS = [
  { key: 'login-card', group: 'App login', title: 'Login card',
    desc: 'The centred card on app.helloivy.co/login ("Welcome back", email/password fields, Continue, Google). The auth boundary: nothing is entered or submitted.',
    sel: 'form/card (login)', find: async (p) => await pick(p, 'form, [class*="card"], [class*="login"], div, section', (el, r) => {
      if (r.width < 200 || r.width > 700 || r.height < 150) return Infinity;
      const t = el.innerText || '';
      if (!/welcome back|log in using your account/i.test(t)) return Infinity;
      // The card, not the heading div: it carries the fields and a submit
      // control.
      if (!el.querySelector('input')) return Infinity;
      if (![...el.querySelectorAll('button, [role="button"], a')].some((b) => /continue|google|log in|sign in/i.test((b.innerText || '').trim()))) return Infinity;
      return el.querySelectorAll('*').length;
    }, 'lc'), states: ['default'] },
  { key: 'login-input-email', group: 'App login', title: 'Email input',
    desc: 'The "Your email" field — measured at rest; nothing is entered.',
    sel: 'input[type="email"], input[name*="email" i]', find: (p) => p.locator('input[type="email"], input[name*="email" i], input').filter({ visible: true }).first(), states: ['default', 'focused'] },
  { key: 'login-input-password', group: 'App login', title: 'Password input',
    desc: 'The "Your password" field — measured at rest; nothing is entered.',
    sel: 'input[type="password"]', find: (p) => p.locator('input[type="password"]').filter({ visible: true }).first(), states: ['default'] },
  { key: 'login-continue', group: 'App login', title: '"Continue" button',
    desc: 'The form\'s submit — measured, never pressed (it would submit).',
    sel: 'button (text Continue)', find: async (p) => await domFind(p, /^continue$/i, { sel: 'button, a, input', tag: 'lc2', minW: 50 }), states: ['default', 'hover', 'focus-visible'] },
  { key: 'login-google', group: 'App login', title: '"Login with Google" button',
    desc: 'The OAuth button — measured, never pressed.',
    sel: 'button (text Login with Google)', find: async (p) => await domFind(p, /login with google|sign in with google/i, { sel: 'button, a, div', tag: 'lg', minW: 80 }), states: ['default', 'hover'] },
  { key: 'login-signup', group: 'App login', title: '"Sign up" link',
    desc: 'The "Don\'t have an account yet? Sign up" link — measured, never followed.',
    sel: 'a (text Sign up)', find: async (p) => await domFind(p, /^sign up$/i, { sel: 'a', tag: 'ls', minW: 30 }), states: ['default', 'hover'] },
  { key: 'login-forgot', group: 'App login', title: '"Forgot password?" link',
    desc: 'The reset link — measured, never followed.',
    sel: 'a (text Forgot password?)', find: async (p) => await domFind(p, /forgot password/i, { sel: 'a', tag: 'lf', minW: 30 }), states: ['default', 'hover'] },
];

// ---- app.helloivy.co/.../share: the public Media-kit document ----
const SHARE_SPECS = [
  { key: 'share-header', group: 'Share document', title: 'Share page header',
    desc: 'The document page\'s top strip — the "hello ivy" name and the Settings button.',
    sel: 'header/toolbar (share)', find: async (p) => await pick(p, 'header, nav, [class*="header"], [class*="toolbar"], div', (el, r) => {
      if (r.top > 120 || r.width < 300 || r.height > 160 || r.height === 0) return Infinity;
      const t = el.innerText || '';
      if (!/settings|hello ivy|media kit/i.test(t)) return Infinity;
      return el.querySelectorAll('*').length;
    }, 'sh'), states: ['default'] },
  { key: 'share-settings', group: 'Share document', title: '"Settings" button',
    desc: 'The document\'s own settings control — a local UI toggle opening the document menu (Send to mail / Print / word count). "opened" is its own press, closed with Escape.',
    sel: 'button (text Settings)', find: async (p) => await domFind(p, /^settings$/i, { sel: 'button, a, div', tag: 'ss', minW: 40 }), states: ['default', 'hover',
      { name: 'opened', via: 'the "Settings" button\'s own press (menu open; Escape restores)', fn: async (loc) => {
        await loc.click({ timeout: 4000 }).catch(() => {});
        await page.waitForTimeout(1500);
        const m = await page.evaluate(() => {
          const el = [...document.querySelectorAll('div,ul,nav,section')].filter((e) => {
            const t = e.innerText || '';
            const r = e.getBoundingClientRect();
            return /send to mail/i.test(t) && /print|word count/i.test(t) && t.length < 2000 && r.width > 60;
          }).sort((a, b) => a.querySelectorAll('*').length - b.querySelectorAll('*').length)[0];
          if (el) el.setAttribute('data-m-mark', 'sm');
          return Boolean(el);
        });
        return m ? page.locator('[data-m-mark="sm"]') : null;
      } },
    ] },
  { key: 'share-doc', group: 'Share document', title: 'Media-kit document',
    desc: 'The document canvas — the public marketing disclaimer, the Hello Ivy logo and product screenshots the file carries.',
    sel: 'article/main (doc)', find: async (p) => await pick(p, 'article, main, [class*="content"], [class*="document"], div, section', (el, r) => {
      if (r.width < 300 || r.height < 200) return Infinity;
      const t = el.innerText || '';
      if (!/media kit|logo|marketing|hello ivy/i.test(t)) return Infinity;
      return el.querySelectorAll('*').length;
    }, 'sd'), states: ['default'] },
];

const MOBILE_SPECS = [
  { key: 'm-nav-bar', group: 'Site chrome (mobile)', title: 'Mobile nav bar',
    desc: 'The top strip at 390px — wordmark and the menu box (the menu element\'s painted ancestor bar).',
    sel: 'top strip (ancestor of Menu)', find: async (p) => {
      const ok = await p.evaluate(() => {
        const menu = [...document.querySelectorAll('[data-framer-name="Menu"], [data-framer-name="menu"]')].filter((e) => {
          const r = e.getBoundingClientRect();
          if (r.width === 0 || r.top > 200) return false;
          let anc = e;
          while (anc && anc !== document.documentElement) { const cs = getComputedStyle(anc); if (cs.display === 'none' || cs.visibility === 'hidden') return false; anc = anc.parentElement; }
          return true;
        })[0];
        if (!menu) return false;
        let el = menu.parentElement;
        while (el && el.getBoundingClientRect().width < 300) el = el.parentElement;
        if (el && el.getBoundingClientRect().top <= 200) { el.setAttribute('data-m-mark', 'mnav'); return true; }
        return false;
      });
      return p.locator(ok ? '[data-m-mark="mnav"]' : '[data-m-mark="__none__"]');
    }, states: ['default'] },
  { key: 'm-menu-box', group: 'Site chrome (mobile)', title: 'Menu box (drawer open)',
    desc: 'The nav menu box at 390px — a real tap opens the full-screen overlay (data-framer-name "Menu"). "opened" is its own tap, closed with Escape.',
    sel: '[data-framer-name="Menu"]', find: async (p) => {
      const ok = await p.evaluate(() => {
        const el = [...document.querySelectorAll('[data-framer-name="Menu"], [data-framer-name="menu"]')].filter((e) => {
          const r = e.getBoundingClientRect();
          if (r.width === 0 || r.top > 200) return false;
          let anc = e;
          while (anc && anc !== document.documentElement) { const cs = getComputedStyle(anc); if (cs.display === 'none' || cs.visibility === 'hidden') return false; anc = anc.parentElement; }
          return true;
        })[0];
        if (el) el.setAttribute('data-m-mark', 'mmb');
        return Boolean(el);
      });
      return p.locator(ok ? '[data-m-mark="mmb"]' : '[data-m-mark="__none__"]');
    }, states: [{ name: 'opened', via: 'the menu box\'s own tap (overlay open; reloaded afterwards)', fn: async (loc) => {
      await loc.tap({ timeout: 4000 }).catch(() => loc.click({ timeout: 3000 }).catch(() => {}));   // a locator press scrolls into view first
      await page.waitForTimeout(2500);
      // The overlay box, not the page: html/body match the text test when
      // the overlay never opened, so they are excluded and the smallest
      // painted subtree holding the link list wins.
      const ov = await page.evaluate(() => {
        const els = [...document.querySelectorAll('*')].filter((e) => {
          if (e === document.documentElement || e === document.body) return false;
          const t = e.innerText || '';
          if (!/0?1\s*HOME/i.test(t) || !/FEATURES/i.test(t) || t.length >= 4000) return false;
          return e.getBoundingClientRect().height > 300;
        }).sort((a, b) => a.querySelectorAll('*').length - b.querySelectorAll('*').length);
        const el = els[0];
        if (el) el.setAttribute('data-m-mark', 'mov2');
        return Boolean(el);
      });
      if (!ov) throw new Error('the menu overlay never painted open');
      return page.locator('[data-m-mark="mov2"]');
    } }] },
  { key: 'm-hero-heading', group: 'Marketing (mobile)', title: 'Hero heading at 390px',
    desc: 'The headline on the phone — the display type compressed to the small width (an h3 at this width).',
    sel: 'h1,h2,h3', find: (p) => p.locator('h1,h2,h3').filter({ visible: true }).first(), states: ['default'] },
];

const GROUPS = {
  home: { page: 'home', specs: [...NAV_SPECS, ...HERO_SPECS] },
  pricing: { page: 'pricing', specs: PRICING_SPECS },
  features: { page: 'features', specs: FEATURE_SPECS },
  blog: { page: 'blog', specs: BLOG_SPECS },
  'doc-post': { page: 'doc-post', specs: DOCS_SPECS },
  login: { page: 'login', specs: LOGIN_SPECS },
  share: { page: 'share', specs: SHARE_SPECS },
  mobile: { page: 'home', mobile: true, specs: MOBILE_SPECS },
};

// ---------- runner ----------

const b = await chromium.launch();
context = await b.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
await patch(context);
const mobCtx = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' });
await patch(mobCtx);

const wanted = process.argv.slice(2);
out._meta.read = new Date().toLocaleDateString('en-CA');
out._meta.viewport = '1440 x 900 (mobile group 390 x 844); www.helloivy.co paints html[toggle-theme=light] by default and repaints through the footer\'s own "Change theme" toggle (a real click on the painted control; html[toggle-theme=dark] + localStorage.currentToggleState, verified by the painted surface before any dark reading). app.helloivy.co has no theme control and paints light only; its semantic --*-color layer is the share page\'s inline section.main_section theme, not the login card\'s.';
out._meta.tool = 'tools/capture/public/measure.mjs';
out._meta.sheets ??= {};

for (const [key, g] of Object.entries(GROUPS)) {
  if (wanted.length && !wanted.includes(key)) continue;
  const ctx = g.mobile ? mobCtx : context;
  page = await ctx.newPage();
  page.setDefaultTimeout(8000);
  cdp = await ctx.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  const url = URLS[g.page];
  currentUrl = url;
  log('open', key, g.mobile ? '(mobile)' : '', url);
  if (!(await open(page, url, { wait: 8000 }))) { log('  group skipped: the page never loaded'); await page.close().catch(() => {}); continue; }
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
  if (g.setup) await g.setup(page).catch((e) => log('  setup failed:', e.message));
  // the readable sheets' transition declarations, for measurements.md
  out._meta.sheets[g.page] = await page.evaluate(() => {
    const found = [];
    for (const ss of document.styleSheets) {
      try {
        for (const r of ss.cssRules) {
          if (r.style && r.style.transition && r.style.transition !== 'all 0s') found.push({ transition: r.style.transition.slice(0, 90) });
        }
      } catch { /* cross-origin sheet */ }
    }
    return found.slice(0, 30);
  }).catch(() => []);

  for (const spec of g.specs) {
    const comp = out.components[spec.key] ??= {};
    comp.group = spec.group;
    comp.title = spec.title;
    comp.desc = spec.desc;
    comp.selector = spec.sel;
    comp.page = g.page;
    comp.url = safeUrl(url);
    comp.run = new Date().toISOString();
    comp.states ??= {};
    let loc;
    // A lookup miss must not erase states a previous run already measured —
    // only a component with no good readings at all counts as missing.
    const hasStates = () => Object.values(comp.states ?? {}).some((s) => s && s.style);
    try { loc = await spec.find(page); } catch (e) {
      log(' ', spec.key, 'find failed:', e.message.split('\n')[0]);
      if (hasStates()) comp.rerunMiss = e.message.split('\n')[0]; else comp.missing = true;
      continue;
    }
    if (!(await loc.count()) || !(await loc.first().isVisible().catch(() => false))) {
      log(' ', spec.key, 'absent');
      if (hasStates()) comp.rerunMiss = 'absent on this run'; else comp.missing = true;
      continue;
    }
    delete comp.missing;
    delete comp.rerunMiss;
    loc = loc.first();
    for (const st of spec.states) {
      const name = typeof st === 'string' ? st : (st.name || 'opened');
      // pressed/dark are cleared in finally so a failed read can never leak
      // the forced state into the next measurement.
      let pressed = null;
      let darkOn = false;
      try {
        await reset();
        let viaText = 'resting state';
        let readLoc = loc;
        if (st === 'hover') { await hover(readLoc); viaText = via.hover; }
        else if (st === 'focus-visible') { const f = await kbFocus(readLoc); viaText = f && (f.held || f.ring) ? via['focus-visible'] : 'focus failed'; }
        else if (st === 'focused') { await readLoc.click({ timeout: 3000 }).catch(() => readLoc.evaluate((el) => el.focus())); await page.waitForTimeout(400); viaText = 'the field clicked into'; }
        else if (st === 'pressed') { pressed = await pressOn(readLoc); viaText = via.pressed; }
        else if (st === 'dark') { if (!(await setTheme(page, 'dark'))) { log(' ', spec.key, name, 'dark never painted — skipped'); continue; } darkOn = true; viaText = via.dark; }
        else if (st && typeof st === 'object' && st.fn) { const alt = await st.fn(readLoc); if (alt && typeof alt.count === 'function' && await alt.count()) readLoc = alt; viaText = st.via || 'reached by the component\'s own UI toggle'; }
        else if (typeof st === 'function') { await st(readLoc); viaText = 'reached by the component\'s own UI toggle'; }
        await centre(readLoc).catch(() => {});
        const v = await styleOf(readLoc);
        v.via = viaText;
        v.crop = await crop(page, readLoc, `${spec.key}-${name}`).catch((e) => { log('  crop failed', spec.key, name, e.message.split('\n')[0]); return undefined; });
        v.run = new Date().toISOString();
        comp.states[name] = v;
        log(' ', spec.key, name, 'ok');
      } catch (e) {
        // A failed rerun records the error beside the last good reading, not
        // over it — a good saved state outlives a transient failure.
        const prev = comp.states[name];
        comp.states[name] = (prev && prev.style)
          ? { ...prev, rerunError: e.message.split('\n')[0] }
          : { error: e.message.split('\n')[0] };
        log(' ', spec.key, name, 'FAILED', e.message.split('\n')[0]);
      } finally {
        if (pressed != null) await pressOff(pressed).catch(() => {});
        if (darkOn) {
          let back = await setTheme(page, 'light').catch(() => false);
          if (!back) back = await setTheme(page, 'light').catch(() => false);
          if (!back) {
            // A failed reset must never leak dark paint into the next
            // default reading: reload, which restores the html[toggle-theme]
            // boot, and re-find the element so later states measure the live
            // page.
            log(' ', spec.key, 'light reset failed — reloading to the light boot');
            await open(page, url, { wait: 8000 }).catch(() => {});
            await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
            if (g.setup) await g.setup(page).catch(() => {});
            const refound = await spec.find(page).catch(() => null);
            if (refound && await refound.count()) loc = refound.first();
          }
        }
      }
    }
    save();
  }
  if (g.teardown) await g.teardown(page).catch(() => {});
  await setTheme(page, 'light').catch(() => {});
  await page.close();
}
await b.close();
log('done ->', OUT);
