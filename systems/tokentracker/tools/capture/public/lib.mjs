// Shared helpers for the TokenTracker captures (adapted from the gauth kit).
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs) when this
// directory has no node_modules of its own.
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
// The dashboard the TokenTracker CLI serves on this machine (`tokentracker serve`).
// It needs no sign-in; it reads the owner's local usage, so every shot is masked.
export const BASE = process.env.TT_BASE || 'http://127.0.0.1:7680';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..'); // systems/<slug>, from tools/capture/public
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// TokenTracker uses Tailwind utilities with no hashing; M() selects by a class.
export const M = (name) => `.${name}`;

// The owner's private text, replaced in the page before any shot or reading:
// home-directory paths, session and project titles, installed skill names and
// descriptions. Literals come from the redaction file, never from this script.
// A missing, unreadable or empty redaction file stops the capture: without it, home paths and
// names elsewhere on the page would reach the PNGs and readings.
const REDACT = (() => {
  const file = process.env.SNAP_REDACT || `${process.env.HOME}/.design-systems/tokentracker-redact.json`;
  let rules;
  try { rules = JSON.parse(fs.readFileSync(file, 'utf8')).replace; } catch (e) {
    throw new Error(`redaction file ${file} could not be read (${e.message}); refusing to capture`);
  }
  if (!Array.isArray(rules) || !rules.length) throw new Error(`redaction file ${file} has no "replace" rules; refusing to capture`);
  for (const r of rules) {
    if (!Array.isArray(r) || r.length !== 3 || r.some((x) => typeof x !== 'string')) throw new Error(`redaction rule ${JSON.stringify(r)} is not [pattern, flags, replacement]`);
    new RegExp(r[0], r[1]); // throws on a bad pattern
  }
  return rules;
})();
export async function mask(page) {
  await page.evaluate((rules) => {
    const res = rules.map(([src, flags, to]) => [new RegExp(src, flags.includes('g') ? flags : flags + 'g'), to]);
    const swap = (t) => { let v = t; for (const [re, to] of res) v = v.replace(re, to); return v; };
    const walk = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    for (let n; (n = walk.nextNode());) { const v = swap(n.textContent); if (v !== n.textContent) n.textContent = v; }
    const model = /^(claude|gpt|gemini|o\d|codex|swe|kimi|glm|grok|deepseek|qwen|sonnet|opus|haiku|composer)/i;
    let i = 0;
    document.querySelectorAll('.sessions-row').forEach((row) => {
      i++;
      const t = row.querySelector('.sessions-row-title'); if (t && t.textContent !== `project-${i}`) t.textContent = `project-${i}`;
      const id = row.querySelector('.sessions-row-identity');
      if (!id) return;
      const w = document.createTreeWalker(id, NodeFilter.SHOW_TEXT);
      for (let n; (n = w.nextNode());) {
        const v = n.textContent.trim();
        if (!v || n.parentElement === t || model.test(v) || /^[·\s]+$/.test(v) || /\d/.test(v) && !/[a-z]{4,}-[a-z]/i.test(v)) continue;
        if (/^[\w.-]+$/.test(v) || v.includes('/')) n.textContent = n.textContent.replace(v, `project-${i}`);
      }
    });
    let k = 0;
    document.querySelectorAll('[data-skill-row]').forEach((row) => {
      k++;
      const h = row.querySelector('h2'); if (h) h.textContent = `skill-${k}`;
      row.querySelectorAll('p').forEach((p) => { p.textContent = 'What this skill does and when an agent should use it, in one or two lines.'; });
      const sw = document.createTreeWalker(row, NodeFilter.SHOW_TEXT);
      for (let n; (n = sw.nextNode());) if (/\S\/\S/.test(n.textContent)) n.textContent = 'marketplace/plugin';
    });
  }, REDACT);
}

// The dashboard follows prefers-color-scheme until a theme is chosen, so the
// emulated colour scheme picks the theme (ThemeProvider adds .dark to <html>).
export async function launch({ width = 1440, height = 900, mobile = false, theme = 'dark', reducedMotion = 'no-preference' } = {}) {
  const browser = await chromium.launch();
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US', colorScheme: theme, timezoneId: 'Asia/Singapore' }
    : { viewport: { width, height }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US', reducedMotion, colorScheme: theme, timezoneId: 'Asia/Singapore' });
  await guard(context);
  return { browser, context };
}

// Look, don't act: every request that is not a read (GET, HEAD, OPTIONS) is aborted before it
// leaves the browser, so no click in a capture can save, sync, remove or send anything.
export const blocked = [];
export async function guard(context) {
  await context.route('**/*', (route) => {
    const req = route.request();
    if (['GET', 'HEAD', 'OPTIONS'].includes(req.method())) return route.continue();
    blocked.push(`${req.method()} ${req.url().replace(/\?.*/, '')}`);
    return route.abort();
  });
}

export async function closePromo() { return false; }

// Pages fetch from the local API after load; a fixed wait lets the numbers land.
export async function open(page, url, { wait = 3500 } = {}) {
  await page.goto(url, { waitUntil: 'load', timeout: 60000 });
  await page.waitForTimeout(wait);
  await mask(page);
}

export async function openStory() { throw new Error('not used for TokenTracker'); }

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
    const pick = (cs) => {
      const o = {};
      for (const p of props) o[p] = cs[p];
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
          content: p.content.slice(0, 40), width: p.width, height: p.height, position: p.position,
          backgroundColor: p.backgroundColor, backgroundImage: p.backgroundImage.slice(0, 200), boxShadow: p.boxShadow,
          borderTopWidth: p.borderTopWidth, borderTopStyle: p.borderTopStyle, borderTopColor: p.borderTopColor,
          borderRadius: p.borderRadius, inset: `${p.top} ${p.right} ${p.bottom} ${p.left}`, opacity: p.opacity, transition: p.transition,
        };
      }
    }
    // A url() in a computed value can be a signed URL: recorded as url(…), only data: and #fragment
    // references kept (the kit's noUrl).
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\(\s*(?!['"]?(?:data:|#))(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^)]*)\s*\)/g, 'url(…)') : v);
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

// Element screenshot into components/crops/<name>.png, padded so a focus ring
// or shadow is not clipped, then quantized to 256 colours. Sticky bars that do
// not hold the element are hidden for the shot.
const STICKY = '[data-tt-sticky-none]';
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
  execFileSync('python3', [
    '-c',
    'import sys\nfrom PIL import Image\nf=sys.argv[1]\nim=Image.open(f).convert("RGB")\nif im.width*im.height>1200000: im=im.resize((im.width//2, im.height//2), Image.LANCZOS)\nim.quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(f, optimize=True)',
    file,
  ]);
}

export function slug(s) {
  return s.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
}
