// Shared helpers for the lovable.dev public captures (adapted from the kit's
// Gauth copy via the Base44 package). Run with PLAYWRIGHT pointing at a
// Playwright install (index.mjs) when this directory has no node_modules.
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
export const BASE = 'https://lovable.dev';
export const DOCS = 'https://docs.lovable.dev';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..');
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// lovable.dev is a Tailwind site with a named token layer (--bg-*, --fg-*,
// --border-*, --shadow-*, --text-*-lmk, --radius-*-lmk) and an html.light /
// html.dark class. Public marketing paints light. The enterprise demo form
// paints dark. docs.lovable.dev is a separate Mintlify-style host (Inter,
// --primary). Selectors key off roles, landmarks and visible text.
export const M = (name) => name;

export async function patch(context) {
  await context.addInitScript(() => {
    // Automation is not hidden: no navigator.webdriver mask (bot check: recorded as a boundary, not bypassed).
    try { window.__captureDPR = window.devicePixelRatio; } catch { /* read-only */ }
  });
}

export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch();
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US', reducedMotion: 'no-preference' });
  await patch(context);
  return { browser, context };
}

export async function clearChallenge(page, { tries = 8, step = 1500 } = {}) {
  for (let i = 0; i < tries; i++) {
    const s = await page.evaluate(() => ({
      title: document.title,
      body: (document.body && document.body.innerText || '').slice(0, 400),
    })).catch(() => ({ title: '', body: '' }));
    const challenging = /just a moment/i.test(s.title)
      || /performing security verification|verify you are human|verifying you are human|checking your browser/i.test(s.body);
    if (!challenging && s.body.length > 40) return true;
    await page.waitForTimeout(step);
  }
  return false;
}

// Hide (never click) any fixed consent or promo overlay. REMOVE-ONLY.
export async function closePromo(page) {
  for (let i = 0; i < 4; i++) {
    const hit = await page.evaluate(() => {
      let n = 0;
      const nodes = [...document.querySelectorAll('div,section,aside,[role="dialog"],[role="alertdialog"]')];
      for (const x of nodes) {
        const t = x.innerText || '';
        const r = x.getBoundingClientRect();
        const cs = getComputedStyle(x);
        const consent = /cookie|consent|manage preferences|we value your privacy|privacy preference/i.test(t);
        const fixed = cs.position === 'fixed' || cs.position === 'sticky';
        if (consent && fixed && t.length < 2400 && r.width > 160 && r.height > 40) {
          x.style.setProperty('display', 'none', 'important');
          n++;
        }
      }
      document.body && document.body.style.removeProperty('overflow');
      document.documentElement && document.documentElement.style.removeProperty('overflow');
      return n;
    }).catch(() => 0);
    if (!hit) { await page.waitForTimeout(400); continue; }
    await page.waitForTimeout(400);
  }
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
        return r.width >= w && r.height >= h && r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && +cs.opacity > 0 && re.test((n.innerText || n.getAttribute('aria-label') || '').trim());
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

// Returns false when a bot check never cleared; a navigation error is thrown, not swallowed.
export async function open(page, url, { wait = 4000, promo = 'close' } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  if (!(await clearChallenge(page))) return false;
  await page.waitForTimeout(wait);
  if (promo === 'close') await closePromo(page);
  return true;
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
  return locator.evaluate((el, props) => {
    const cls = (n) => [...n.classList].map((c) => String(c)).filter((c) => c && !/^x[0-9a-z]{5,8}$/.test(c));
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
    };
    for (const pe of ['::before', '::after']) {
      const p = getComputedStyle(el, pe);
      if (p.content && p.content !== 'none' && p.content !== 'normal') {
        out[pe] = {
          content: noUrl(p.content).slice(0, 40), width: p.width, height: p.height, position: p.position,
          backgroundColor: p.backgroundColor, backgroundImage: noUrl(p.backgroundImage).slice(0, 200), boxShadow: p.boxShadow,
          borderTopWidth: p.borderTopWidth, borderTopStyle: p.borderTopStyle, borderTopColor: p.borderTopColor,
          borderRadius: p.borderRadius, inset: `${p.top} ${p.right} ${p.bottom} ${p.left}`, opacity: p.opacity, transition: p.transition,
        };
      }
    }
    const paint = [];
    const nodes = [el, ...el.querySelectorAll('*')].slice(0, 400);
    for (const n of nodes) {
      if (paint.length >= 14) break;
      if (n.closest('svg') && n.tagName.toLowerCase() !== 'svg') continue;
      for (const pe of [null, '::before', '::after']) {
        const c = getComputedStyle(n, pe);
        if (pe && (c.content === 'none' || c.content === 'normal')) continue;
        const bw = ['Top', 'Right', 'Bottom', 'Left'].map((sd) => parseFloat(c[`border${sd}Width`]) > 0 && c[`border${sd}Style`] !== 'none' ? `${sd[0]}:${c[`border${sd}Width`]} ${c[`border${sd}Style`]} ${c[`border${sd}Color`]}` : '').filter(Boolean);
        const bg = c.backgroundColor !== 'rgba(0, 0, 0, 0)' ? c.backgroundColor : '';
        const bgi = c.backgroundImage !== 'none' && !/^url\("?https?:/.test(c.backgroundImage) ? noUrl(c.backgroundImage).replace(/url\("data:[^)]{60,}\)/g, 'url(data:…)').slice(0, 200) : '';
        const sh = c.boxShadow !== 'none' ? c.boxShadow : '';
        const ol = c.outlineStyle !== 'none' && parseFloat(c.outlineWidth) > 0 ? `${c.outlineWidth} ${c.outlineStyle} ${c.outlineColor} offset ${c.outlineOffset}` : '';
        if (!(bw.length || bg || bgi || sh || ol)) continue;
        if (n.tagName === 'IMG' && !bw.length && !sh) continue;
        const rr = n.getBoundingClientRect();
        paint.push({
          node: n.tagName.toLowerCase() + (pe || '') + cls(n).slice(0, 2).map((x) => '.' + x).join(''),
          size: pe ? `${c.width}x${c.height}` : `${rr.width.toFixed(1)}x${rr.height.toFixed(1)}`,
          border: bw.join(' | ') || undefined, bg: bg || undefined, bgImage: bgi || undefined, shadow: sh || undefined, outline: ol || undefined,
          radius: c.borderRadius !== '0px' ? c.borderRadius : undefined,
        });
      }
    }
    if (paint.length) out.paint = paint;
    const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, { acceptNode: (t) => (t.textContent.trim() && t.parentElement && t.parentElement.getBoundingClientRect().width > 1 && getComputedStyle(t.parentElement).visibility !== 'hidden' ? 1 : 3) });
    const tn = walker.nextNode();
    if (tn && tn.parentElement !== el) {
      const t = tn.parentElement;
      const tc = getComputedStyle(t);
      out.textStyle = { node: t.tagName.toLowerCase() + cls(t).slice(0, 2).map((x) => '.' + x).join(''), text: tn.textContent.trim().slice(0, 40), fontFamily: tc.fontFamily, fontSize: tc.fontSize, lineHeight: tc.lineHeight, fontWeight: tc.fontWeight, letterSpacing: tc.letterSpacing, color: tc.color, textDecorationLine: tc.textDecorationLine, textTransform: tc.textTransform };
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

export async function crop(page, locator, name, pad = 8) {
  fs.mkdirSync(CROPS, { recursive: true });
  const box = await locator.boundingBox();
  if (!box || box.width < 1 || box.height < 1) throw new Error('no box');
  const vp = page.viewportSize();
  const x = Math.max(0, box.x - pad);
  const y = Math.max(0, box.y - pad);
  const w = Math.min(vp.width - x, box.width + pad * 2);
  const h = Math.min(vp.height - y, box.height + pad * 2);
  const file = path.join(CROPS, `${name}.png`);
  await page.screenshot({ path: file, clip: { x, y, width: Math.max(1, w), height: Math.max(1, h) } });
  return `components/crops/${name}.png`;
}

export async function centre(locator) {
  await locator.evaluate((el) => el.scrollIntoView({ block: 'center', inline: 'nearest' })).catch(() => {});
  await locator.page().waitForTimeout(250);
}

export function quantizeNote() {
  return PYTHON;
}
