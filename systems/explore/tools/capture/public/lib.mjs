// Shared helpers for the explore.family public captures (adapted from the
// enode copy of the kit).
//
// explore.family closed on 2023-04-19 and the domain later lapsed (NXDOMAIN,
// RDAP 404 at capture time), so no request can reach the real host. Every page
// is replayed from a local Internet Archive mirror instead: wireMirror()
// routes explore.family and back.explore.family to files on disk, so the
// February 2023 build of the app runs and measures as if live. Two archived
// builds exist in the mirror:
//   feb  2023-02-23 — the working product (SPA + archived API JSON + uploads)
//   jun  2023-06-08 — the closure announcement page only
// Profile pages were additionally server-rendered by the app; their archived
// SSR HTML lives in mirror/routes/<slug>.html and is replayed with JavaScript
// disabled (the SPA would otherwise mount over it and erase the content,
// because its API endpoints were never archived).
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import { execFileSync } from 'node:child_process';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

const PYTHON = process.env.PYTHON || 'python3';

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
export const BASE = 'https://explore.family';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..'); // systems/explore, from tools/capture/public
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// The archived site on disk. Populated by the capture notes in README:
// index-feb.html / index.html (the two <html> snapshots), css/, js/, fonts/,
// images/, videos/, saved-appreciated-lottie.json, api/ (endpoint JSON keyed
// as path_query with ?=&/ flattened to _), uploads/ (media) and routes/
// (server-rendered page HTML).
export const MIRROR = process.env.MIRROR || path.join(os.homedir(), '.design-systems', 'explore', 'mirror');
const MIME = {
  '.html': 'text/html', '.css': 'text/css', '.js': 'application/javascript', '.json': 'application/json',
  '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp',
  '.gif': 'image/gif', '.svg': 'image/svg+xml', '.mp4': 'video/mp4', '.woff2': 'font/woff2', '.ico': 'image/x-icon',
};
const exists = (p) => (p && fs.existsSync(p) && fs.statSync(p).isFile()) ? p : null;

// Resolve a decoded request path under root, or null when it escapes: an
// encoded ../ in restored markup must not read files outside the mirror.
const under = (root, p) => {
  const f = path.resolve(root, '.' + p);
  return f.startsWith(root + path.sep) ? f : null;
};

// Which archived <html> the SPA routes replay: 'feb' (default, the product)
// or 'jun' (the announcement). SSR profile pages set ssr: their archived
// routes/<slug>.html is served verbatim instead.
export function indexHtml(era = 'feb') {
  return era === 'jun' ? path.join(MIRROR, 'index.html') : path.join(MIRROR, 'index-feb.html');
}

// Records every URL the mirror could not serve (evidence of what the archive
// itself lacks — imported by public.mjs/measure.mjs runs).
export const mirrorMisses = [];

function serveFront(route, url, era) {
  const u = new URL(url);
  let p = decodeURIComponent(u.pathname);
  let f = exists(under(MIRROR, p));
  if (!f && !path.extname(p)) f = exists(indexHtml(era));
  if (f) return route.fulfill({ status: 200, contentType: MIME[path.extname(f)] || 'application/octet-stream', body: fs.readFileSync(f) });
  mirrorMisses.push(url);
  return route.fulfill({ status: 404, contentType: 'text/plain', body: 'mirror miss' });
}

function serveBack(route, url) {
  const u = new URL(url);
  const p = decodeURIComponent(u.pathname), q = u.search;
  const key = (p + q).replace(/^\/|\/$/g, '').replace(/[?=&/]/g, '_');
  const f = exists(path.join(MIRROR, 'api', key + '.json'));
  if (f) return route.fulfill({ status: 200, contentType: 'application/json', body: fs.readFileSync(f) });
  const up = exists(under(path.join(MIRROR, 'uploads'), p.replace(/^\/uploads/, '')));
  if (up) return route.fulfill({ status: 200, contentType: MIME[path.extname(up)] || 'application/octet-stream', body: fs.readFileSync(up) });
  if (p.startsWith('/uploads/')) { mirrorMisses.push(url); return route.fulfill({ status: 404, contentType: 'text/plain', body: 'upload not archived' }); }
  // Boot endpoints the app expects: the real shapes so the signed-out flow
  // proceeds exactly as the unauthenticated visitor's did (user calls get a
  // 401, which is what signed out meant on the live site too).
  if (p === '/country') return route.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify({ success: true, data: { country: 'US' } }) });
  if (p.startsWith('/user/') || p === '/get') return route.fulfill({ status: 401, contentType: 'application/json', body: JSON.stringify({ success: false, message: 'Unauthenticated.' }) });
  mirrorMisses.push(url);
  return route.fulfill({ status: 404, contentType: 'application/json', body: JSON.stringify({ success: false, message: 'endpoint not archived' }) });
}

// Wire a browser context to the mirror. era: 'feb' | 'jun'. ssr: serve the
// archived routes/<slug>.html verbatim and abort every <script> — the SSR
// document stays exactly what the server sent (the SPA would mount over it
// and erase the content, since its API endpoints were never archived) while
// the page's own JavaScript keeps working for measurement evaluates.
export async function wireMirror(context, { era = 'feb', ssr = null } = {}) {
  await context.route('**/back.explore.family/**', (route) => serveBack(route, route.request().url()));
  await context.route(/https:\/\/(www\.)?explore\.family\//, (route) => {
    const u = new URL(route.request().url());
    if (ssr && route.request().resourceType() === 'script') return route.abort();
    if (ssr && u.pathname === ssr && !path.extname(u.pathname)) {
      const f = exists(path.join(MIRROR, 'routes', ssr.replace(/^\//, '') + '.html'));
      // The archived SSR HTML carries inline <script> blocks as well as the
      // bundle tags: strip every one at the boundary so the measured page is
      // exactly the server-rendered document — script-resource requests are
      // aborted above, and inline code never reaches the page (the measure
      // context keeps JavaScript enabled for its own locators/evaluates, so
      // the no-script guarantee has to live in the served document).
      if (f) return route.fulfill({ status: 200, contentType: 'text/html', body: fs.readFileSync(f, 'utf8').replace(/<script\b[^>]*>[\s\S]*?<\/script>/gi, '') });
    }
    return serveFront(route, route.request().url(), era);
  });
  await context.route(/(google-analytics|googletagmanager|gtag|doubleclick|facebook\.net|hotjar|segment\.io)/i, (route) => route.abort());
}

export const M = (name) => `[class*="${name}"]`;

export async function patch(context) {
  await context.addInitScript(() => {
    // bot check: navigator.webdriver is left as the browser reports it; a challenge is recorded as a boundary, not bypassed (D7)
    try { window.__captureDPR = window.devicePixelRatio; } catch { /* read-only */ }
  });
}

export async function launch({ width = 1440, height = 900, mobile = false, era = 'feb', ssr = null } = {}) {
  const browser = await chromium.launch();
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US', javaScriptEnabled: !ssr }
    : { viewport: { width, height }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US', reducedMotion: 'no-preference', javaScriptEnabled: !ssr });
  await patch(context);
  await wireMirror(context, { era, ssr });
  return { browser, context };
}

// explore.family shows no consent or promo overlay signed out (checked on
// every replayed route); this only strips a stuck fixed layer if one appears
// and removes a scroll lock. REMOVE-ONLY: nothing is ever accepted.
export async function closePromo(page) {
  await page.evaluate(() => {
    document.querySelectorAll('div[id*="onetrust" i], div[class*="onetrust" i], div[id*="cookiebot" i], div[id*="cookiebanner" i]').forEach((x) => x.style.setProperty('display', 'none', 'important'));
    if (document.body) document.body.style.removeProperty('overflow');
    document.documentElement && document.documentElement.style.removeProperty('overflow');
  }).catch(() => {});
  return true;
}

// Finds a visible element in-page whose trimmed innerText matches reText,
// tags it with data-m-mark="<tag>" and returns a locator for it. up optionally
// retargets an ancestor (closest()).
export async function domFind(page, reText, { sel = 'button, a', tag = 'm', up = null, nth = 0, leaf = true, minW = 0, minH = 0 } = {}) {
  const ok = await page.evaluate(
    ([src, flags, s, t, upSel, i, leafOnly, w, h]) => {
      const re = new RegExp(src, flags);
      document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
      const els = [...document.querySelectorAll(s)].filter((n) => {
        const r = n.getBoundingClientRect();
        const cs = getComputedStyle(n);
        return r.width >= w && r.height >= h && r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.opacity !== '0' && re.test((n.innerText || '').trim());
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

export async function open(page, url, { wait = 6000, promo = 'close' } = {}) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
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
        const bw = ['Top', 'Right', 'Bottom', 'Left'].map((sd) => parseFloat(c[`border${sd}Width`]) > 0 && c[`border${sd}Style`] !== 'none' ? `${sd[0]}:${c[`border${sd}Width`]} ${c[`border${sd}Style`]}` : '').filter(Boolean);
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
// or shadow is not clipped, then quantized to 256 colours. The fixed .header
// bar is hidden for shots it does not overlap.
const STICKY = ['.header', 'nav[class*="sticky" i]', '[class*="sticky" i]'].join(', ');
export async function crop(page, locator, name, pad = 8) {
  fs.mkdirSync(CROPS, { recursive: true });
  const file = path.join(CROPS, `${name}.png`);
  const hidden = await locator.evaluate((el, { sel, pad }) => {
    let n = 0;
    const er = el.getBoundingClientRect();
    document.querySelectorAll(sel).forEach((s) => {
      if (s.contains(el) || el.contains(s)) return;
      const sr = s.getBoundingClientRect();
      const overlap = !(sr.right < er.left - pad || sr.left > er.right + pad || sr.bottom < er.top - pad || sr.top > er.bottom + pad);
      if (overlap) return;
      s.setAttribute('data-m-hidden', '1');
      s.style.setProperty('visibility', 'hidden', 'important');
      n++;
    });
    return n;
  }, { sel: STICKY, pad });
  try {
    const box = await locator.boundingBox();
    if (!box) throw new Error(`no box for ${name}`);
    const vp = page.viewportSize();
    const inView = box.y - pad >= 0 && box.y + box.height + pad <= vp.height && box.x >= 0 && box.x + box.width <= vp.width + 1;
    let lastErr;
    for (let i = 0; i < 2; i++) {
      try {
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
        lastErr = null;
        break;
      } catch (e) { lastErr = e; await page.waitForTimeout(900); }
    }
    if (lastErr) { try { fs.unlinkSync(file); } catch { /* none */ } throw lastErr; }
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

// 256 colours, and a crop larger than about 1.2 megapixels is halved.
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
