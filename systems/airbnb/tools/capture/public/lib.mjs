// Shared helpers for the Airbnb captures (adapted from the Refero kit).
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs) when this
// directory has no node_modules of its own.
//
// One surface is measured: https://www.airbnb.com, which geo-redirects to the
// regional mirror (www.airbnb.com.sg from this network; the design system is
// the same build). The public, signed-out pages are the home page (the app
// shell: logo, category tabs, the Where/When/Who search pill, listing
// carousels), /experiences and /services, the /s/<place>/homes results page
// (filters, listing grid, Google map), one /rooms/<id> detail page, and the
// two normally-scrolling pages /help and /host/homes.
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

// Interpreter for the inline Pillow calls below: an activated .venv resolves
// `python3` to itself, so set PYTHON when Pillow lives elsewhere.
const PYTHON = process.env.PYTHON || 'python3';

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://www.airbnb.com';

export const HERE = path.dirname(fileURLToPath(import.meta.url));
export const REF = path.resolve(HERE, '..', '..', '..'); // systems/<slug>, from tools/capture/public
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// airbnb.com is styled with atomic `atm_*` classes (a CSS-in-JS build) that a
// rebuild can rename, so there is no stable class vocabulary to match on.
// Specs therefore use role, text and structural selectors, and M() is a
// pass-through kept so the kit's other scripts keep their `M('sel')` shape.
export const M = (sel) => sel;

export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch();
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US', reducedMotion: 'no-preference' });
  // bot check: recorded as a boundary, not bypassed. Headless Chromium sets
  // navigator.webdriver and airbnb.com bot-walls some routes on it; the capture
  // no longer masks the flag, so a walled route is a boundary, not a reading.
  return { browser, context };
}

// Two kinds of overlay sit over airbnb.com signed out: coachmark modals (the
// "all fees included" card on search pages, "Translation on" on room pages)
// rendered in a fixed z-index 2000+ portal holding a [role=dialog], and small
// promo pills. sweepOverlays HIDES them — sets display:none on the fixed
// container that holds each dialog — and reports how many it hid. Nothing is
// clicked: there is no consent banner in the locales it serves, and clicking a
// "Got it" would still be a press the kit avoids. airbnb.com draws its body
// position:fixed at rest (the document scrolls on <html>), so no scroll lock
// needs undoing.
export async function sweepOverlays(page) {
  let hidden = 0;
  for (let i = 0; i < 4; i++) {
    const n = await page.evaluate(() => {
      let count = 0;
      const vis = (e) => { const r = e.getBoundingClientRect(); return r.width > 8 && r.height > 8 && getComputedStyle(e).visibility !== 'hidden' && +getComputedStyle(e).opacity > 0.05 && e.isConnected; };
      const hide = (el) => { el.setAttribute('data-m-overlay', '1'); el.style.setProperty('display', 'none', 'important'); count++; };
      for (const d of document.querySelectorAll('[role=dialog], [role=alertdialog], [aria-modal="true"]')) {
        if (!vis(d)) continue;
        let n = d;
        while (n.parentElement && n.parentElement !== document.body && getComputedStyle(n.parentElement).position !== 'fixed') n = n.parentElement;
        hide((n.parentElement && n.parentElement !== document.body) ? n.parentElement : n);
      }
      // The dimmer the dialog leaves behind is a fixed element covering the
      // viewport and painting a translucent fill. Hide it too (the site
      // header is fixed but paints an opaque white and covers only the top).
      for (const e of document.querySelectorAll('body *')) {
        if (e.hasAttribute('data-m-overlay') || !vis(e)) continue;
        const c = getComputedStyle(e);
        if (c.position !== 'fixed' && c.position !== 'sticky') continue;
        const r = e.getBoundingClientRect();
        if (r.width < innerWidth * 0.95 || r.height < innerHeight * 0.95) continue;
        const m = c.backgroundColor.match(/rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?\)/);
        const a = m ? (m[4] === undefined ? 1 : +m[4]) : 0;
        const dark = m && (+m[1] + +m[2] + +m[3]) < 400;
        // a dim is a dark fill the page shows through: translucent bg, or an
        // opaque fill on an element faded with opacity (airbnb's z-2000 dimmer)
        if (a > 0.05 && dark && (a < 0.95 || +c.opacity < 0.98)) hide(e);
      }
      return count;
    }).catch(() => 0);
    if (!n) break;
    hidden += n;
    await page.waitForTimeout(700);
  }
  return hidden;
}

// The first /rooms/<id> href the results page lists, used by the room run.
export async function firstRoomHref(page) {
  const href = await page.evaluate(() => {
    const a = [...document.querySelectorAll('a[href*="/rooms/"]')].find((x) => x.getBoundingClientRect().width > 100);
    return a && a.getAttribute('href');
  }).catch(() => null);
  return href ? href.split('?')[0] : null;
}

// navigator.webdriver is left as Chromium sets it, so a bot wall can answer
// instead of the product. A wall still loads as a normal document, so check for
// it before any screenshot or component record: throw, and let the page loop
// record the route as failed with its earlier evidence left in place.
const WALL = /captcha|verify (that )?you are (a )?human|are you a robot|unusual traffic|access denied|request (was )?blocked|press (&|and) hold|pardon our interruption|attention required/i;
export async function assertProductPage(page) {
  const probe = await page.evaluate(() => ({ title: document.title || '', text: (document.body?.innerText || '').slice(0, 4000) })).catch(() => ({ title: '', text: '' }));
  if (WALL.test(probe.title) || WALL.test(probe.text)) throw new Error('bot check: ' + (probe.title || probe.text.slice(0, 80)).trim());
  if (probe.text.trim().length < 200) throw new Error('bot check or empty page: ' + probe.text.trim().length + ' characters of text');
}

export async function open(page, url, { wait = 6000, sweep = 'sweep' } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  await page.waitForTimeout(wait);
  if (sweep === 'sweep') await sweepOverlays(page);
  await page.waitForTimeout(400);
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
// Atomic hash classes (`atm_*`, and any single capitalised run such as `yQTE0`)
// are dropped from the report.
export async function styleOf(locator) {
  return locator.evaluate((el, props) => {
    const strip = (c) => String(c).replace(/__[A-Za-z0-9_-]{5,6}$/, '');
    const cls = (n) => [...n.classList].map(strip).filter((c) => !/^atm_[a-z0-9]+_[a-z0-9]+$/i.test(c) && !/^[A-Za-z][0-9A-Za-z]{4}$/.test(c) && !/^x[0-9a-z]{5,8}$/.test(c) && !/[[\]:()]/.test(c));
    // A url() in a computed value can be a signed URL: recorded as url(…), only data: and #fragment
    // references kept (the kit's noUrl).
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
    const svg = el.tagName === 'svg' ? el : el.querySelector('svg');
    if (svg) {
      const sr = svg.getBoundingClientRect();
      const scs = getComputedStyle(svg);
      out.icon = { w: +sr.width.toFixed(2), h: +sr.height.toFixed(2), fill: scs.fill, stroke: scs.stroke, color: scs.color };
    }
    return out;
  }, PROPS);
}

// Element screenshot into components/crops/<name>.png, padded so a focus ring
// or shadow is not clipped, then quantized to 256 colours. Fixed-position
// chrome (airbnb's header, the results map, any promo card still open) is
// tagged data-m-sticky by markFixed() and hidden for the shot unless it holds
// the element.
const STICKY = '[data-m-sticky]';
export async function markFixed(page) {
  await page.evaluate(() => {
    for (const e of document.querySelectorAll('[data-m-sticky]')) e.removeAttribute('data-m-sticky');
    for (const e of document.querySelectorAll('body *')) {
      const cs = getComputedStyle(e);
      if (cs.position !== 'fixed' && cs.position !== 'sticky') continue;
      const r = e.getBoundingClientRect();
      if (r.width < 40 || r.height < 24) continue;
      e.setAttribute('data-m-sticky', '1');
    }
  }).catch(() => {});
}

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
  const shrink = quantize(file);
  // the scale the crop was actually saved at: the page's devicePixelRatio,
  // halved when quantize had to shrink it past the 1.2 megapixel cap
  const dpr = await page.evaluate(() => devicePixelRatio).catch(() => 1);
  return { file: path.relative(REF, file), scale: +(dpr * shrink).toFixed(2) };
}

export async function centre(locator) {
  await locator.evaluate((el) => el.scrollIntoView({ block: 'center', inline: 'nearest', behavior: 'instant' })).catch(() => {});
  await locator.page().waitForTimeout(350);
}

// 256 colours, and a crop larger than about 1.2 megapixels (a whole sidebar or
// section at 2x) is halved, so the folder stays small. Returns the shrink
// factor applied: 1 normally, 0.5 when the crop was halved.
export function quantize(file) {
  const out = execFileSync(PYTHON, [
    '-c',
    'import sys\nfrom PIL import Image\nf=sys.argv[1]\nim=Image.open(f).convert("RGB")\nhalved=im.width*im.height>1200000\nif halved: im=im.resize((im.width//2, im.height//2), Image.LANCZOS)\nim.quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(f, optimize=True)\nprint(0.5 if halved else 1)',
    file,
  ]);
  return parseFloat(String(out).trim()) || 1;
}

export function slug(s) {
  return s.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
}
