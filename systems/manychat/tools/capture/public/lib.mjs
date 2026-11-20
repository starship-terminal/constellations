// Shared helpers for the manychat.com public captures (adapted from the
// public-capture kit).
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs) when this
// directory has no node_modules of its own.
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

// Interpreter for the inline Pillow calls below: an activated .venv resolves
// `python3` to itself, so set PYTHON when Pillow lives elsewhere.
const PYTHON = process.env.PYTHON || 'python3';

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://manychat.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..'); // systems/<slug>, from tools/capture/public
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// manychat.com is a Next.js + Tailwind marketing site. Specs select by role,
// aria-label, href or visible text. M() is a class-fragment helper for the
// few stable fragments the site publishes (mc-html, mc-text-label).
export const M = (name) => `[class*="${name}"]`;

// The per-context patch every page gets: a record of the real devicePixelRatio
// before app code runs. Automation is not hidden (no webdriver mask, no
// AutomationControlled flag): a bot check is recorded as a boundary, not bypassed.
export async function patch(context) {
  await context.addInitScript(() => {
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

// Waits out a Cloudflare interstitial and reports whether the real document arrived.
export async function clearChallenge(page, { tries = 8, step = 1500 } = {}) {
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

// Hide (never click) the Usercentrics privacy layer and any other consent
// overlay. Hiding never accepts or rejects anything. The OK control is never clicked.
export async function closePromo(page) {
  for (let i = 0; i < 4; i++) {
    const hit = await page.evaluate(() => {
      let n = 0;
      const hide = (el) => { if (!el || el.dataset.mcHidden === '1') return; el.dataset.mcHidden = '1'; el.style.setProperty('display', 'none', 'important'); n++; };
      document.querySelectorAll('#usercentrics-root, [id*="usercentrics" i], [class*="usercentrics" i], #uc-center-container, [data-testid*="uc-" i], #onetrust-banner-sdk, [id*="onetrust" i], #CybotCookiebotDialog, [id*="CybotCookiebot" i], .cky-consent-container, [id*="iubenda" i]').forEach(hide);
      for (const el of document.querySelectorAll('*')) {
        if (!el.shadowRoot) continue;
        const t = el.shadowRoot.textContent || '';
        if (/privacy information|we and our partners are using technologies/i.test(t)) hide(el);
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

// Returns whether the real document arrived. A failed navigation or a challenge
// that never clears returns false, so the caller records the page as blocked
// instead of measuring the interstitial as the product.
export async function open(page, url, { wait = 6000, promo = 'close' } = {}) {
  let loaded = true;
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 })
    .catch((e) => { loaded = false; console.log('  goto failed', url, String(e.message).split('\n')[0]); });
  if (!loaded || !(await clearChallenge(page))) return false;
  await page.waitForTimeout(wait);
  if (promo === 'close') await closePromo(page);
  return true;
}

// Computed style properties recorded for every component and state.
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

// Reads the computed style of the element, its ::before/::after if they paint
// anything, the rect, the painted layers in its subtree, a focus ring or fill
// painted by an ancestor, the first text node's type, and the first svg icon.
// Class names are reported without their CSS-module hash.
export async function styleOf(locator) {
  return locator.evaluate((el, props) => {
    const strip = (c) => String(c).replace(/__[A-Za-z0-9_-]{5,6}$/, '');
    const cls = (n) => [...n.classList].map(strip).filter((c) => !/^x[0-9a-z]{5,8}$/.test(c));
    // A url() in a computed value (a background photo, a cursor) can be a signed URL: recorded as
    // url(…), only data: and #fragment references kept.
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
      classes: cls(el).slice(0, 4).join(' '),
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
    const anc = [];
    for (let n = el.parentElement, i = 0; n && i < 3; n = n.parentElement, i++) {
      const c = getComputedStyle(n);
      const fill = i < 1 && c.backgroundColor !== 'rgba(0, 0, 0, 0)';
      if (fill || c.boxShadow !== 'none' || (c.outlineStyle !== 'none' && parseFloat(c.outlineWidth) > 0 && c.outlineColor !== 'rgba(0, 0, 0, 0)')) {
        anc.push({ up: i + 1, node: n.tagName.toLowerCase() + cls(n).slice(0, 2).map((x) => '.' + x).join(''), shadow: c.boxShadow !== 'none' ? c.boxShadow : undefined, outline: c.outlineStyle !== 'none' ? `${c.outlineWidth} ${c.outlineStyle} ${c.outlineColor}` : undefined, radius: c.borderRadius, bg: c.backgroundColor });
      }
    }
    if (anc.length) out.ancestors = anc;
    const paints = (node) => {
      const cs = getComputedStyle(node);
      return cs.visibility !== 'hidden' && cs.display !== 'none' && cs.opacity !== '0' && cs.color !== 'rgba(0, 0, 0, 0)' && cs.color !== 'transparent';
    };
    const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, { acceptNode: (t) => (t.textContent.trim() && t.parentElement && t.parentElement.getBoundingClientRect().width > 1 && paints(t.parentElement) ? 1 : 3) });
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

// Element screenshot into components/crops/<name>.png, padded so a focus ring
// or shadow is not clipped, then quantized to 256 colours. Sticky bars that do
// not hold the element are hidden for the shot.
const STICKY = [M('pc-header_header'), M('catalog_stickyToolbar'), M('math-course-detail_backBar'), M('header_header')].join(', ');
export async function crop(page, locator, name, pad = 8) {
  fs.mkdirSync(CROPS, { recursive: true });
  const file = path.join(CROPS, `${name}.png`);
  const hidden = await locator.evaluate((el, sel) => {
    let n = 0;
    document.querySelectorAll(sel).forEach((s) => {
      if (s.contains(el) || el.contains(s)) return;
      s.setAttribute('data-m-hidden', '1');
      s.style.setProperty('visibility', 'hidden', 'important');
      n++;
    });
    return n;
  }, STICKY);
  try {
    const box = await locator.boundingBox();
    if (!box) throw new Error(`no box for ${name}`);
    const vp = page.viewportSize();
    const inView = box.y - pad >= 0 && box.y + box.height + pad <= vp.height && box.x >= 0 && box.x + box.width <= vp.width + 1;
    if (inView) {
      const clip = {
        x: Math.max(0, box.x - pad),
        y: Math.max(0, box.y - pad),
        width: Math.min(vp.width - Math.max(0, box.x - pad), box.width + 2 * pad),
        height: Math.min(vp.height - Math.max(0, box.y - pad), box.height + 2 * pad),
      };
      await page.screenshot({ path: file, clip, animations: 'allow' });
    } else {
      await locator.screenshot({ path: file, animations: 'allow' });
    }
  } finally {
    if (hidden) await page.evaluate(() => document.querySelectorAll('[data-m-hidden]').forEach((n) => { n.style.removeProperty('visibility'); n.removeAttribute('data-m-hidden'); }));
  }
  quantize(file);
  return path.relative(REF, file);
}

export async function centre(locator) {
  await locator.evaluate((el) => el.scrollIntoView({ block: 'center', inline: 'nearest', behavior: 'instant' })).catch(() => {});
  await locator.page().waitForTimeout(350);
}

// 256 colours, and a crop larger than about 1.2 megapixels (a whole sidebar or
// section at 2x) is halved, so the folder stays small.
export function quantize(file) {
  execFileSync(PYTHON, [
    '-c',
    'import sys\nfrom PIL import Image\nf=sys.argv[1]\nim=Image.open(f).convert("RGB")\nif im.width*im.height>1200000: im=im.resize((im.width//2, im.height//2), Image.LANCZOS)\nim.quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(f, optimize=True)',
    file,
  ]);
}

export function slug(s) {
  return s.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
}
