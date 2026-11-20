// Shared helpers for the kinhive.com public captures.
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs) when this
// directory has no node_modules.
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
export const BASE = 'https://kinhive.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..'); // systems/<slug>, from tools/capture/public
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// kinhive.com is a Next.js marketing site. The public surface paints light.
// A dark palette is declared under @media (prefers-color-scheme: dark) on
// html[data-app-theme=system], and the live document does not set that
// attribute, so the painted theme is light. Specs select by role, id, or
// visible text. Cookie settings is a footer link, not a blocking overlay;
// any consent dialog that mounts is hidden, never answered.
export const M = (name) => `[class*="${name}"]`;

export async function patch(context) {
  await context.addInitScript(() => {
    // navigator.webdriver is left as the browser reports it: automation is not hidden (2026-11 audit).
    try { window.__captureDPR = window.devicePixelRatio; } catch { /* read-only */ }
  });
}

export async function launch({ width = 1440, height = 900, mobile = false, colorScheme = 'light' } = {}) {
  const browser = await chromium.launch();
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US', colorScheme }
    : { viewport: { width, height }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US', reducedMotion: 'no-preference', colorScheme });
  await patch(context);
  return { browser, context };
}

export async function clearChallenge(page, { tries = 12, step = 1500 } = {}) {
  for (let i = 0; i < tries; i++) {
    const s = await page.evaluate(() => ({
      title: document.title,
      body: (document.body && document.body.innerText || '').slice(0, 400),
    })).catch(() => ({ title: '', body: '' }));
    const challenging = /just a moment|attention required/i.test(s.title)
      || /performing security verification|verify you are human|verifying you are human|checking your browser|unusual activity from your computer network|press ?& ?hold|not a robot|you have been blocked|unable to access/i.test(s.body);
    if (!challenging && s.body.length > 40) return true;
    await page.waitForTimeout(step);
  }
  return false;
}

// Hide (never click) a consent or promo overlay. Cookie settings in the
// footer is a link, not a dialog, and is left alone.
export async function closePromo(page) {
  for (let i = 0; i < 3; i++) {
    const hit = await page.evaluate(() => {
      let n = 0;
      document.querySelectorAll('#CybotCookiebotDialog, #CybotCookiebotDialogBodyUnderlay, [id*="onetrust" i], [class*="onetrust" i], [id*="termly-code-snippet-support" i]').forEach((x) => {
        x.style.setProperty('display', 'none', 'important'); n++;
      });
      const box = [...document.querySelectorAll('div,section,aside,[role="dialog"],[role="alertdialog"]')].find((x) => {
        const t = x.innerText || '';
        const r = x.getBoundingClientRect();
        const cs = getComputedStyle(x);
        return (cs.position === 'fixed' || cs.position === 'sticky')
          && /we use cookies|cookie settings|we value your privacy|accept all cookies|manage cookies/i.test(t)
          && t.length < 1600 && r.width > 200 && r.height > 60 && +cs.zIndex > 10
          && r.top < 200;
      });
      if (box) { box.style.setProperty('display', 'none', 'important'); n++; }
      return n;
    }).catch(() => 0);
    if (!hit) return true;
    await page.waitForTimeout(400);
  }
  return true;
}

export async function open(page, url, { wait = 2200 } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(wait);
  await clearChallenge(page, { tries: 4, step: 800 });
  await closePromo(page);
}

export async function domFind(page, reText, { sel = 'button, a', tag = 'm', up = null, nth = 0, leaf = true, minW = 0, minH = 0 } = {}) {
  const ok = await page.evaluate(
    ([src, flags, s, t, upSel, i, leafOnly, w, h]) => {
      const re = new RegExp(src, flags);
      document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
      const els = [...document.querySelectorAll(s)].filter((n) => {
        const r = n.getBoundingClientRect();
        const cs = getComputedStyle(n);
        if (r.width < w || r.height < h || cs.visibility === 'hidden' || +cs.opacity === 0 || cs.display === 'none') return false;
        const text = (n.innerText || n.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim();
        if (!re.test(text)) return false;
        if (leafOnly && [...n.querySelectorAll(s)].some((c) => re.test((c.innerText || '').replace(/\s+/g, ' ').trim()))) return false;
        return true;
      });
      const el = els[i];
      if (!el) return false;
      const target = upSel ? (el.closest(upSel) || el) : el;
      target.setAttribute('data-m-mark', t);
      return true;
    },
    [reText.source, reText.flags, sel, tag, up, nth, leaf, minW, minH],
  );
  return ok ? page.locator(`[data-m-mark="${tag}"]`).first() : null;
}

export const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height', 'minWidth', 'maxWidth', 'minHeight',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'marginTop', 'marginRight', 'marginBottom', 'marginLeft',
  'gap', 'rowGap', 'columnGap', 'flexDirection', 'alignItems', 'justifyContent',
  'gridTemplateColumns', 'borderTopLeftRadius', 'borderTopRightRadius', 'borderBottomRightRadius', 'borderBottomLeftRadius',
  'borderTopWidth', 'borderRightWidth', 'borderBottomWidth', 'borderLeftWidth',
  'borderTopColor', 'borderRightColor', 'borderBottomColor', 'borderLeftColor',
  'borderTopStyle', 'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset',
  'backgroundColor', 'backgroundImage', 'color', 'fontFamily', 'fontSize', 'fontWeight', 'fontStyle',
  'lineHeight', 'letterSpacing', 'textAlign', 'textTransform', 'textDecorationLine',
  'boxShadow', 'opacity', 'overflow', 'zIndex',
  'transitionProperty', 'transitionDuration', 'transitionTimingFunction',
];

export async function readBox(page, locator) {
  const handle = await locator.elementHandle();
  if (!handle) return null;
  const box = await handle.evaluate((el, props) => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const o = { x: r.x, y: r.y, w: r.width, h: r.height };
    for (const p of props) o[p] = noUrl(cs[p]);
    o.text = (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 180);
    return o;
  }, PROPS);
  await handle.dispose();
  return box;
}

export function crop(page, locator, file, pad = 8) {
  return locator.screenshot({ path: file, animations: 'disabled' }).catch(async () => {
    const box = await locator.boundingBox();
    if (!box) return false;
    await page.screenshot({
      path: file,
      clip: {
        x: Math.max(0, box.x - pad),
        y: Math.max(0, box.y - pad),
        width: box.width + pad * 2,
        height: box.height + pad * 2,
      },
    });
    return true;
  });
}

export function quantizePng(file) {
  try {
    execFileSync(PYTHON, ['-c', `
from PIL import Image
im = Image.open(${JSON.stringify(file)}).convert('RGBA')
q = im.convert('P', palette=Image.ADAPTIVE, colors=256)
q.save(${JSON.stringify(file)})
`], { stdio: 'ignore' });
  } catch { /* leave full colour if Pillow is missing */ }
}
