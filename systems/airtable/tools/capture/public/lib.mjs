// Shared helpers for the Airtable captures (adapted from the Anthropic package's kit).
// Run with PLAYWRIGHT pointing at a Playwright install (index.mjs) when this
// directory has no node_modules of its own.
//
// airtable.com is a Next.js marketing site on CSS modules: classes read
// `X-module_name__hash`, so `[class*="__name"]` selects the readable suffix.
// The site declares ~3000 custom properties site-wide, including per-state
// variants (--mainNavButton*Hover/Active/Focus). airtable.com app and the
// sign-up/log-in flows are the signed surface and are never touched.
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { pngDimensions } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

// Interpreter for the inline Pillow calls below: an activated .venv resolves
// `python3` to itself, so set PYTHON when Pillow lives elsewhere.
const PYTHON = process.env.PYTHON || 'python3';

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://www.airtable.com';

export const HERE = path.dirname(fileURLToPath(import.meta.url));
export const REF = path.resolve(HERE, '..', '..', '..'); // systems/<slug>, from tools/capture/public
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// CSS-module classes carry the readable name after the last `__`
// (`NavBar-...__header` -> `[class*="__header"]`); the hash in the middle
// changes on rebuild, so specs use these suffixes plus role, text and shared
// utility classes. M() is a pass-through kept so the kit keeps its shape.
export const M = (sel) => sel;
// Readable CSS-module suffix selector: __name matches `X-module-...__name`.
export const cm = (name) => `[class*="__${name}"]`;

export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch();
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US', reducedMotion: 'no-preference' });
  // navigator.webdriver is not masked: a bot check is recorded as a boundary.
  await context.addInitScript(() => {
    // bot check: recorded as a boundary, not bypassed (navigator.webdriver is left as Chromium sets it)
  });
  // The Google One Tap sign-in prompt (accounts.google.com/gsi) is a sign-in
  // surface: it is aborted at the network, never rendered or answered.
  await context.route(/accounts\.google\.com|apis\.google\.com\/js/, (r) => r.abort()).catch(() => {});
  return { browser, context };
}

// airtable.com shows no cookie banner to this profile, but it mounts two
// third-party widgets that are not part of the design system: the Qualified
// "Riley" chat assistant (an expanded white panel or a dark round launcher,
// variously qualified.com iframes, #q-messenger-frame, qlfd-* classes and
// unclassed fixed hosts that only carry the widget's own text) and, on some
// pages, a Google One Tap sign-in prompt (blocked at the network in launch(),
// swept here if a node still mounts). Riley mounts after the first sweep on
// some loads, so this is called again before each shot and measure pass.
// The sweep hides them — a hide, not a consent or a dismissal of the
// product's own UI — and reports the count. It also hides any positioned
// consent overlay.
export async function closePromo(page) {
  return page.evaluate(() => {
    let hid = 0;
    const vis = (e) => { const r = e.getBoundingClientRect(); return r.width > 8 && r.height > 8 && e.isConnected; };
    const kill = (e) => { if (e && e.style && e.style.display !== 'none') { e.setAttribute('data-m-swept', '1'); e.style.setProperty('display', 'none', 'important'); e.style.setProperty('pointer-events', 'none', 'important'); hid++; } };
    for (const e of document.querySelectorAll('iframe[src*="qualified.com"], iframe[src*="accounts.google.com"], iframe[src*="transcend"], #q-messenger-frame, [id*="q-messenger" i], [id*="qualified" i], [id*="transcend" i], [class*="qlfd"], [class*="qualified" i], [class*="q-messenger" i], [class*="transcend" i], #credential_picker_container, [id^="g_id_"], [class*="g_id_signin" i], [data-testid*="qualified" i]')) {
      kill(e);
      const host = e.closest('div:not(body):not(main)') || e;
      if (host !== e) kill(host);
    }
    // A positioned element that only carries the chat widget's or the sign-in
    // prompt's text (these hosts mount late and may carry no qualified/google
    // marker at all): hide the outermost fixed ancestor holding it.
    for (const e of document.querySelectorAll('body *')) {
      const cs = getComputedStyle(e);
      if (cs.position !== 'fixed' && cs.position !== 'sticky' && cs.position !== 'absolute') continue;
      const t = (e.innerText || '') + ' ' + (e.getAttribute('aria-label') || '') + ' ' + (e.getAttribute('title') || '');
      if (/ask riley|riley from airtable|speak now|sign in with google|signin with google/i.test(t) || (/^riley\b/i.test(t.trim()) && /assistant|contact sales|customer support/i.test(t))) {
        let n = e;
        while (n.parentElement && n.parentElement !== document.body && getComputedStyle(n.parentElement).position === 'fixed') n = n.parentElement;
        kill(n);
      }
    }
    // Transcend's consent UI lives in an open shadow root. The host itself
    // reports 0 height, so a visibility check misses it, and clicking Agree
    // or Reject would POST. Hide the host by id. Never click those buttons.
    const transcend = document.getElementById('transcend-shadow-root');
    if (transcend) kill(transcend);
    for (const e of document.querySelectorAll('[id*="transcend" i], [class*="transcend" i]')) kill(e);
    return hid;
  }).catch(() => 0);
}

export async function open(page, url, { wait = 5000, promo = 'close' } = {}) {
  await page.goto(url, { waitUntil: 'load', timeout: 90000 });
  await page.waitForTimeout(wait);
  if (promo === 'close') await closePromo(page);
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
// CSS-module hashes are trimmed to the readable suffix; shared utilities like
// text-body-2 pass through.
export async function styleOf(locator) {
  return locator.evaluate((el, props) => {
    const cls = (n) => [...n.classList].map((c) => c.includes('__') ? c.split('__').pop() : c).filter((c) => c && !/[[\]:()]/.test(c)).slice(0, 4);
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
      classes: cls(el).join(' '),
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
// or shadow is not clipped, then quantized to 256 colours. Fixed-position
// chrome (the nav bar, sticky docs rails) is tagged data-m-sticky by
// markFixed() and hidden for the shot unless it holds the element.
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
  // Riley and other fixed chrome can mount after the page-open sweep and the
  // first markFixed pass, so sweep again at the crop boundary, the way
  // Shooter.view does for page screenshots.
  await closePromo(page);
  await markFixed(page);
  // A .capture.json sidecar per crop, the same fields screenshotWithMetadata
  // records for page shots (docs/CAPTURE.md: the browser's real inner size and
  // pixel ratio plus the PNG's pixel dimensions), plus the final PNG
  // dimensions after quantize() may have halved the file.
  const meta = {
    schemaVersion: 1,
    capturedAt: new Date().toISOString(),
    screenshot: `${name}.png`,
    sanitizedSourceUrl: null,
    requested: { viewport: page.viewportSize(), deviceScaleFactor: null },
    configuredViewport: page.viewportSize(),
    actual: null,
    capture: { mode: null, scale: 'device', clip: null },
    png: null,
    pngFinal: null,
    resize: null,
    dimensionCheck: { status: 'pending', expected: null, basis: 'crop' },
    visualReview: { status: 'pending', note: 'Inspect the final image for complete, settled contents; dimensions alone cannot accept it.' },
    cropCoordinates: { status: 'unverified', note: 'Do not derive crop or masking boxes from requested size or assume DOM rectangles align with this PNG.' },
  };
  const writeMeta = () => fs.writeFileSync(`${file}.capture.json`, JSON.stringify(meta, null, 2) + '\n');
  writeMeta(); // invalidate a previous same-name pass before any browser call can fail
  try {
    meta.actual = await page.evaluate(() => {
      const visual = window.visualViewport;
      return { innerWidth, innerHeight, devicePixelRatio,
        visualViewport: visual ? { width: visual.width, height: visual.height, scale: visual.scale } : null };
    });
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
    meta.capture.box = box;
    const vp = page.viewportSize();
    const inView = box.y - pad >= 0 && box.y + box.height + pad <= vp.height && box.x >= 0 && box.x + box.width <= vp.width + 1;
    if (inView) {
      const clip = {
        x: Math.max(0, box.x - pad),
        y: Math.max(0, box.y - pad),
        width: Math.min(vp.width - Math.max(0, box.x - pad), box.width + 2 * pad),
        height: Math.min(vp.height - Math.max(0, box.y - pad), box.height + 2 * pad),
      };
      meta.capture.mode = 'clip';
      meta.capture.clip = clip;
      await page.screenshot({ path: file, clip, animations: 'allow' });
    } else {
      meta.capture.mode = 'element';
      await locator.screenshot({ path: file, animations: 'allow' });
    }
  } finally {
    if (hidden) await page.evaluate(() => document.querySelectorAll('[data-m-hidden]').forEach((n) => { n.style.removeProperty('visibility'); n.removeAttribute('data-m-hidden'); }));
  }
  meta.png = pngDimensions(fs.readFileSync(file));
  const dpr = meta.actual?.devicePixelRatio || 1;
  const region = meta.capture.clip || meta.capture.box;
  meta.dimensionCheck.expected = { width: Math.round(region.width * dpr), height: Math.round(region.height * dpr) };
  meta.dimensionCheck.basis = meta.capture.mode;
  meta.dimensionCheck.status = Math.abs(meta.png.width - meta.dimensionCheck.expected.width) <= 2
    && Math.abs(meta.png.height - meta.dimensionCheck.expected.height) <= 2 ? 'pass' : 'fail';
  quantize(file);
  meta.pngFinal = pngDimensions(fs.readFileSync(file));
  if (meta.pngFinal.width !== meta.png.width || meta.pngFinal.height !== meta.png.height) {
    meta.resize = { factor: +(meta.pngFinal.width / meta.png.width).toFixed(4), note: 'halved by crop() so the folder stays small' };
    meta.dimensionCheck.note = `png holds the captured pixels; pngFinal is the committed file after halving`;
  }
  writeMeta();
  return path.relative(REF, file);
  } catch (e) {
    meta.dimensionCheck.status = 'fail';
    meta.dimensionCheck.error = String(e.message || e);
    writeMeta();
    throw e;
  }
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
