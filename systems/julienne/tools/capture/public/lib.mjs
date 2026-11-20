// Shared helpers for the withjulienne.com public captures.
// Adapted from the shared kit (hitchd's copy was the immediate ancestor).
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs).
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

const PYTHON = process.env.PYTHON || 'python3';

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://withjulienne.com';

// Documented boundaries the capture must not cross:
//   Log in / Sign in / Create account /signup
//                                   auth dialogs and the signup page are
//                                   captured at rest only. Nothing is typed,
//                                   submitted, or sent through Google, Apple
//                                   or the Turnstile widget.
//   Save / Cook / Buy               saving a recipe, starting cook mode and
//                                   buying a cookbook (Amazon/affiliate) are
//                                   account or purchase paths. Never pressed.
//   Search submit                   the search field is focused and read;
//                                   a query is never typed or submitted.
//                                   /search?ingredients=apple is a published
//                                   browse link, not a typed query.
export const RECIPE = '/days/11_17_2026/recipes/chef_muse_20261117_soup_season_e92685c034_10';
export const COLLECTION = '/collections/carousel/weeknights?title=November+Weeknight+dinners&period=2026-11';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// withjulienne.com is a Vite + Tailwind SPA. html starts as class "js light"
// and the header's own "Toggle theme" button flips it to "js dark". Display
// type is EB Garamond (.font-garamond); UI labels are Inter (.font-inter).
// Controls are glass pills (.glass.glass-interactive) at radius 9999px, and
// the auth buttons are 56px / 20px-radius solids. Brand ink is #3C1518 and
// the warm accent is #DE784F / #FF9D75.
export const M = (name) => `[class*="${name}"]`;

export async function patch(context) {
  await context.addInitScript(() => {
    // no navigator.webdriver mask: removed in the 2026-11 audit (D7), not run since
    try { window.__captureDPR = window.devicePixelRatio; } catch { /* read-only */ }
  });
}

export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch();
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US', reducedMotion: 'no-preference' });
  await patch(context);
  return { browser, context };
}

export async function clearChallenge(page, { tries = 8, step = 1500 } = {}) {
  for (let i = 0; i < tries; i++) {
    const s = await page.evaluate(() => ({
      title: document.title,
      body: (document.body && document.body.innerText || '').slice(0, 400),
    })).catch(() => ({ title: '', body: '' }));
    const challenging = /just a moment|attention required/i.test(s.title)
      || /performing security verification|verify you are human|verifying you are human|checking your browser|unusual activity/i.test(s.body);
    if (!challenging && s.body.length > 40) return true;
    await page.waitForTimeout(step);
  }
  return false;
}

// Hide (never click) any fixed consent overlay. REMOVE-ONLY.
export async function closePromo(page) {
  for (let i = 0; i < 4; i++) {
    const hit = await page.evaluate(() => {
      let n = 0;
      document.querySelectorAll('[id*="onetrust" i], [class*="onetrust" i], [id*="termly" i], [aria-label*="cookie consent" i], [class*="cookie-banner" i], [id*="transcend" i]').forEach((x) => { x.style.setProperty('display', 'none', 'important'); n++; });
      const box = [...document.querySelectorAll('div,section,aside,[role="dialog"]')].find((x) => {
        const t = (x.innerText || '').replace(/\s+/g, ' ');
        const r = x.getBoundingClientRect();
        const cs = getComputedStyle(x);
        return /this website uses cookies|we use cookies|cookie settings|accept all cookies/i.test(t)
          && t.length < 400 && r.height > 20 && r.height < 120 && r.width > 80;
      });
      if (box) { box.style.setProperty('display', 'none', 'important'); n++; }
      return n;
    }).catch(() => 0);
    if (!hit) break;
    await page.waitForTimeout(300);
  }
  return true;
}

export async function setTheme(page, theme) {
  const current = await page.evaluate(() => document.documentElement.classList.contains('dark') ? 'dark' : 'light');
  if (current === theme) return current;
  const btn = page.getByRole('button', { name: 'Toggle theme' }).first();
  if (await btn.count()) {
    await btn.click();
    await page.waitForTimeout(500);
  } else {
    await page.evaluate((t) => {
      document.documentElement.classList.toggle('dark', t === 'dark');
      document.documentElement.classList.toggle('light', t === 'light');
    }, theme);
  }
  return page.evaluate(() => document.documentElement.classList.contains('dark') ? 'dark' : 'light');
}

export async function open(page, url, { wait = 2200, promo = 'close', theme = 'light' } = {}) {
  // A failed load or a challenge page that never clears is a boundary,
  // never measured as the product: open() logs BLOCKED, leaves the tab on
  // about:blank and returns false (true once the page loaded), without
  // stopping the rest of the run. Every caller checks the result and skips
  // the page or group, or fails the reading, so a blank tab is never saved
  // as the product (2026-11 audit, finding 20-4; not run since).
  const loaded = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).then(() => true, (e) => { console.log(`BLOCKED ${url}: ${String(e.message).split('\n')[0]}`); return false; });
  if (!loaded || !(await clearChallenge(page))) {
    if (loaded) console.log(`BLOCKED ${url}: the challenge page never cleared`);
    await page.goto('about:blank').catch(() => {});
    return false;
  }
  await page.waitForTimeout(wait);
  if (promo === 'close') await closePromo(page);
  if (theme) await setTheme(page, theme);
  return true;
}

export async function domFind(page, reText, { sel = 'button, a', tag = 'm', up = null, nth = 0, leaf = true, minW = 0, minH = 0 } = {}) {
  const ok = await page.evaluate(
    ([src, flags, s, t, upSel, i, leafOnly, w, h]) => {
      const re = new RegExp(src, flags);
      document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
      const els = [...document.querySelectorAll(s)].filter((n) => {
        const r = n.getBoundingClientRect();
        const cs = getComputedStyle(n);
        return r.width >= w && r.height >= h && r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.opacity !== '0' && re.test((n.innerText || n.getAttribute('aria-label') || '').trim());
      });
      const pool = leafOnly ? els.filter((n) => !els.some((o) => o !== n && n.contains(o))) : els;
      const el = pool[i] || els[i];
      if (!el) return false;
      (upSel ? el.closest(upSel) || el : el).setAttribute('data-m-mark', t);
      return true;
    },
    [reText.source, reText.flags, sel, tag, up, nth, leaf, minW, minH],
  );
  return ok ? page.locator(`[data-m-mark="${tag}"]`) : page.locator('[data-m-mark="__none__"]');
}

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height', 'minWidth', 'maxWidth', 'minHeight',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'marginTop', 'marginRight', 'marginBottom', 'marginLeft',
  'gap', 'rowGap', 'columnGap', 'flexDirection', 'alignItems', 'justifyContent',
  'gridTemplateColumns',
  'borderTopWidth', 'borderTopStyle', 'borderTopColor',
  'borderRightWidth', 'borderRightStyle', 'borderRightColor',
  'borderBottomWidth', 'borderBottomStyle', 'borderBottomColor',
  'borderLeftWidth', 'borderLeftStyle', 'borderLeftColor',
  'borderTopLeftRadius', 'borderTopRightRadius', 'borderBottomRightRadius', 'borderBottomLeftRadius',
  'backgroundColor', 'backgroundImage', 'boxShadow', 'backdropFilter',
  'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'textTransform',
  'color', 'textDecorationLine', 'textDecorationColor', 'textDecorationThickness', 'textUnderlineOffset',
  'transitionProperty', 'transitionDuration', 'transitionTimingFunction', 'transitionDelay',
  'cursor', 'opacity', 'transform', 'overflow', 'zIndex', 'top',
];

export async function styleOf(locator) {
  if (!(await locator.count())) return { missing: true };
  return locator.evaluate((el, props) => {
    const cls = (n) => [...n.classList].filter((c) => c && !/^x[0-9a-z]{5,8}$/.test(c));
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\(\s*(?!['"]?(?:data:|#))(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^)]*)\s*\)/g, 'url(…)') : v);
    const pick = (cs) => {
      const o = {};
      for (const p of props) o[p] = noUrl(cs[p]);
      return o;
    };
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const out = {
      tag: el.tagName.toLowerCase(),
      classes: cls(el).slice(0, 6).join(' '),
      text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').trim().replace(/\s+/g, ' ').slice(0, 80),
      rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(2), h: +r.height.toFixed(2) },
      style: pick(cs),
      htmlClass: document.documentElement.className,
    };
    for (const pe of ['::before', '::after']) {
      const p = getComputedStyle(el, pe);
      if (p.content && p.content !== 'none' && p.content !== 'normal') {
        out[pe] = {
          content: noUrl(p.content).slice(0, 40), width: p.width, height: p.height,
          backgroundColor: p.backgroundColor, boxShadow: p.boxShadow, borderRadius: p.borderRadius, opacity: p.opacity,
        };
      }
    }
    if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
      const ph = getComputedStyle(el, '::placeholder');
      out.placeholder = { color: ph.color, opacity: ph.opacity, fontSize: ph.fontSize };
    }
    const svg = el.tagName.toLowerCase() === 'svg' ? el : el.querySelector('svg');
    if (svg) {
      const sr = svg.getBoundingClientRect();
      const scs = getComputedStyle(svg);
      out.icon = { w: +sr.width.toFixed(2), h: +sr.height.toFixed(2), fill: scs.fill, stroke: scs.stroke, color: scs.color };
    }
    return out;
  }, PROPS);
}

const STICKY = 'header.site-header, .site-header';
export async function crop(page, locator, name, pad = 10) {
  fs.mkdirSync(CROPS, { recursive: true });
  const file = path.join(CROPS, `${name}.png`);
  if (!(await locator.count())) return null;
  await locator.scrollIntoViewIfNeeded().catch(() => {});
  await page.waitForTimeout(200);
  const box = await locator.boundingBox();
  if (!box || box.width < 2 || box.height < 2) return null;
  const vp = page.viewportSize();
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(vp.width - Math.max(0, box.x - pad), box.width + 2 * pad),
    height: Math.min(vp.height - Math.max(0, box.y - pad), box.height + 2 * pad),
  };
  if (clip.width < 4 || clip.height < 4) return null;
  await page.screenshot({ path: file, clip, animations: 'disabled' });
  quantize(file);
  return path.relative(REF, file);
}

export function quantize(file) {
  execFileSync(PYTHON, [
    '-c',
    'import sys\nfrom PIL import Image\nf=sys.argv[1]\nim=Image.open(f).convert("RGB")\nif im.width*im.height>1200000: im=im.resize((im.width//2, im.height//2), Image.LANCZOS)\nim.quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(f, optimize=True)',
    file,
  ]);
}

export async function forceState(page, locator, state) {
  const handle = await locator.elementHandle();
  if (!handle) return false;
  const session = await page.context().newCDPSession(page);
  const { nodeId } = await session.send('DOM.describeNode', { objectId: handle._objectId || (await handle.evaluateHandle(() => this))._objectId }).catch(() => ({}));
  // Playwright element handles expose the node through DOM.getNodeForLocation is unreliable.
  // Use CSS.forcePseudoState via the remote object.
  try {
    const { object } = await session.send('Runtime.evaluate', { expression: '1' });
    void object;
    const node = await session.send('DOM.requestNode', { objectId: handle._remoteObject?.objectId || (await page.evaluateHandle((el) => el, await locator.elementHandle()))._remoteObject?.objectId });
    void node;
  } catch { /* fall through */ }
  try {
    const obj = await locator.evaluateHandle((el) => el);
    const remote = obj._remoteObject || obj;
    const described = await session.send('DOM.describeNode', { objectId: remote.objectId });
    await session.send('CSS.enable');
    await session.send('CSS.forcePseudoState', { nodeId: described.node.nodeId, forcedPseudoClasses: [state] });
    await page.waitForTimeout(120);
    return true;
  } catch (e) {
    return false;
  }
}
