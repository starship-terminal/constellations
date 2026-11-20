// Shared helpers for the forhers.com public-web capture (adapted from the
// farfetch.com Wayback copy of the kit; the kit lineage is noted in
// tools/kit/README.md).
//
// www.forhers.com sits behind a Cloudflare managed challenge
// (cf-mitigated: challenge, "Performing security verification") that never
// resolves for this capture host — headless Chromium and headed Google
// Chrome under xvfb alike, on every route including robots.txt and the
// favicon (HTTP 403 challenge page). The egress IP is in Singapore and
// forhers.com is US telehealth, so the block may be geo- or
// reputation-based; it is not bypassed. The DOM evidence is therefore
// recent Wayback Machine snapshots of the public SSR pages (PAGES below),
// served from the local static server these scripts spin up; the site's
// own assets (the /css/fonts/* faces, the /forhims/image/upload/* media and
// the cloudinary.forhims.com uploads) are mirrored through web.archive.org
// under ~/.design-systems/forhers/assets. The SSR markup carries the full
// styled-components stylesheet inline (one ~340 KB <style> block per page,
// semantic `*-style__ComponentName-sc-*` classes), so the pages paint
// styled with every script stripped. Nothing is sent, bought, signed into
// or submitted: the only presses are local UI toggles, and hydration-owned
// states are recorded as gaps, never faked.
import fs from 'node:fs';
import http from 'node:http';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
export const { chromium } = pw.default ?? pw;

const PYTHON = process.env.PYTHON || 'python3';

export const UA =
  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
export const UA_MOBILE =
  'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..'); // systems/forhers
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');
export const SCRATCH = process.env.SCRATCH || `${process.env.HOME}/.design-systems/forhers`;

// The archived pages and their snapshot timestamps (each stamp also anchors
// how that page's assets resolve on web.archive.org). Chosen as the newest
// clean 200 capture of each route in the same weeks as the home snapshot.
export const PAGES = {
  home: { url: 'https://www.forhers.com/', ts: '20261109094857' },
  'weight-loss': { url: 'https://www.forhers.com/weight-loss', ts: '20261108030323' },
  'hair-loss': { url: 'https://www.forhers.com/hair-loss', ts: '20261020231923' },
  'skin-care': { url: 'https://www.forhers.com/skin-care', ts: '20261107033608' },
  'mental-health': { url: 'https://www.forhers.com/mental-health', ts: '20260910142746' },
  'birth-control': { url: 'https://www.forhers.com/birth-control', ts: '20261024162428' },
  product: { url: 'https://www.forhers.com/hair-loss/minoxidil-biotin-chew', ts: '20261020231926' },
  'anti-aging': { url: 'https://www.forhers.com/skin-care/anti-aging', ts: '20251223070028' },
  'wegovy-pill': { url: 'https://www.forhers.com/weight-loss/wegovy-pill', ts: '20260927044024' },
  labs: { url: 'https://www.forhers.com/labs', ts: '20261107033636' },
  benefits: { url: 'https://www.forhers.com/benefits', ts: '20260713111036' },
  // The onboarding quiz (forhers.com/g/i/wm, /lp/* start pages) is a
  // client-rendered app: its SSR shell carries no markup, so it is a
  // hydration boundary recorded in the README, not a page here.
  quality: { url: 'https://www.forhers.com/quality-and-safety', ts: '20260111225942' },
  blog: { url: 'https://www.forhers.com/blog', ts: '20260930012919' },
  'blog-post': { url: 'https://www.forhers.com/blog/zoloft-weight-loss', ts: '20261020231409' },
  'bmi-calculator': { url: 'https://www.forhers.com/tools/bmi-calculator', ts: '20261111052225' },
  'drugs-info': { url: 'https://www.forhers.com/drugs/info', ts: '20261023151745' },
};

// Assets that paint the pages: same-origin paths under these prefixes are
// mirrored from the archived www.forhers.com record; absolute URLs to the
// hosts in ASSET_HOSTS are rewritten to /asset/<host>/ by prepare-pages.mjs
// and mirrored from that host's archived record.
export const SITE_PREFIXES = ['/css/', '/forhims/', '/image/', '/fonts/', '/shop/', '/_next/'];
export const ASSET_HOSTS = ['cloudinary.forhims.com', 'static.legitscript.com'];
const ASSET_TS = '20261109'; // archive resolves each asset to its nearest record

// ---------------------------------------------------------------------------
// Local render of the archived SSR pages. pages/ holds the rewritten copies;
// the server answers asset paths from the disk mirror first and falls back to
// a web.archive.org fetch which it then caches, so a re-run is entirely local.
export function servePages(pagesDir, assetsDir) {
  const types = {
    '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'application/javascript',
    '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp',
    '.svg': 'image/svg+xml', '.json': 'application/json', '.woff': 'font/woff', '.woff2': 'font/woff2',
    '.avif': 'image/avif', '.gif': 'image/gif', '.otf': 'font/otf', '.ttf': 'font/ttf',
    '.mp4': 'video/mp4', '.webm': 'video/webm', '.ico': 'image/x-icon',
  };
  const inflight = new Map();
  // Resolve against the cache root and refuse anything that leaves it, so an
  // encoded ../ in a request can neither read nor write outside assetsDir.
  const inside = (root, file) => {
    const rel = path.relative(path.resolve(root), path.resolve(file));
    return rel !== '' && !rel.startsWith('..') && !path.isAbsolute(rel);
  };
  const mirror = (host, rel) => {
    if (!ASSET_HOSTS.includes(host) && host !== 'www.forhers.com') return Promise.resolve(null);
    const safe = rel.replace(/[^\w\-.~/%+,;=:@()]/g, '');
    const dest = path.resolve(assetsDir, host, safe);
    // Always check against the fixed assets root, never a folder the host chose.
    if (!inside(assetsDir, dest)) return Promise.resolve(null);
    if (fs.existsSync(dest)) return Promise.resolve(dest);
    if (inflight.has(dest)) return inflight.get(dest);
    const wb = `https://web.archive.org/web/${ASSET_TS}id_/https://${host}/${safe}`;
    const job = fetch(wb, { redirect: 'follow' })
      .then(async (r) => {
        if (!r.ok) return null;
        const buf = Buffer.from(await r.arrayBuffer());
        if (!buf.length) return null;
        // web.archive.org may serve the record still gzipped.
        const body = buf[0] === 0x1f && buf[1] === 0x8b ? (await import('node:zlib')).gunzipSync(buf) : buf;
        fs.mkdirSync(path.dirname(dest), { recursive: true });
        fs.writeFileSync(dest, body);
        return dest;
      })
      .catch(() => null)
      .finally(() => inflight.delete(dest));
    inflight.set(dest, job);
    return job;
  };
  const srv = http.createServer((req, res) => {
    let u;
    try { u = decodeURIComponent(req.url.split('?')[0]); } catch { res.writeHead(400); res.end('bad'); return; }
    if (u.includes('\0')) { res.writeHead(400); res.end('bad'); return; }
    const send = (file) => {
      fs.readFile(file, (e, data) => {
        if (e) { res.writeHead(404); res.end('nope'); return; }
        // script-src 'none': nothing in an archived copy may run, whatever the
        // rewrite in prepare-pages.mjs missed (2026-11 audit; not run since)
        res.writeHead(200, { 'content-type': types[path.extname(file).toLowerCase()] || 'application/octet-stream', 'cache-control': 'no-store', 'content-security-policy': "script-src 'none'; object-src 'none'" });
        res.end(data);
      });
    };
    const ext = u.match(/^\/asset\/([^/]+)\/(.+)$/);
    if (ext) {
      // The host is part of the path. Only the mirrored hosts are allowed, and
      // the check is against the fixed assets root, so a host of ".." cannot
      // move dest or the checked folder to the parent of assetsDir.
      const host = ext[1];
      if (!ASSET_HOSTS.includes(host) || host.includes('..') || host.includes('/') || host.includes('\\')) {
        res.writeHead(404); res.end('nf'); return;
      }
      mirror(host, ext[2]).then((f) => {
        if (!f || !inside(assetsDir, f)) { res.writeHead(404); res.end('nf'); return; }
        send(f);
      });
      return;
    }
    if (SITE_PREFIXES.some((p) => u.startsWith(p))) {
      mirror('www.forhers.com', u.replace(/^\/+/, '')).then((f) => (f ? send(f) : (res.writeHead(404), res.end('nf'))));
      return;
    }
    const rel = u.replace(/^\/+/, '').replace(/^pages\//, '') || 'home.html';
    const file = path.resolve(pagesDir, rel);
    if (!inside(pagesDir, file)) { res.writeHead(404); res.end('nope'); return; }
    send(file);
  });
  return new Promise((resolve) => srv.listen(0, '127.0.0.1', () => resolve({ srv, port: srv.address().port })));
}

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

// Open a locally-served archived page. Scripts were stripped at rewrite time,
// so nothing executes; the SSR styled-components sheets paint statically.
export async function open(page, url, { wait = 6000 } = {}) {
  await page.goto(url, { waitUntil: 'load', timeout: 120000 }).catch(() => {});
  await page.waitForFunction(() => document.fonts && document.fonts.status === 'loaded', undefined, { timeout: 15000 }).catch(() => {});
  await page.waitForTimeout(wait);
}

// Hide (never click) any fixed consent/promo overlay the SSR markup mounts:
// forhers embeds a Transcend consent manager and a regional-redirect popup.
// REMOVE-ONLY: hiding never accepts or rejects anything.
export async function closePromo(page) {
  for (let i = 0; i < 3; i++) {
    const hit = await page.evaluate(() => {
      let n = 0;
      document.querySelectorAll('[id*="transcend" i], [class*="transcend" i], [id*="regional-redirect" i], [class*="regional-redirect" i], [id*="onetrust" i], [class*="onetrust" i], [data-testid*="consent" i]').forEach((x) => { x.style.setProperty('display', 'none', 'important'); n++; });
      const box = [...document.querySelectorAll('div,section,aside,[role="dialog"],[role="alertdialog"]')].find((x) => {
        const t = x.innerText || '';
        const r = x.getBoundingClientRect();
        const cs = getComputedStyle(x);
        return (cs.position === 'fixed' || cs.position === 'sticky')
          && /cookie|consent|we value privacy|personal data|looks like you('re| are) (visiting|browsing) from|region|country/i.test(t)
          && t.length < 1600 && r.width > 200 && r.width < 1400 && r.height > 60 && +cs.zIndex > 5;
      });
      if (box) { box.style.setProperty('display', 'none', 'important'); n++; }
      document.body && document.body.style.removeProperty('overflow');
      document.documentElement && document.documentElement.style.removeProperty('overflow');
      return n;
    }).catch(() => 0);
    if (!hit) { await page.waitForTimeout(500); continue; }
    await page.waitForTimeout(500);
  }
  return true;
}

// Finds a visible element in-page whose trimmed innerText matches reText,
// tags it with data-m-mark="<tag>" and returns a locator for it.
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

export const M = (name) => `[class*="${name}"]`;

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
// or shadow is not clipped, then quantized to 256 colours. Sticky bars that sit over the
// element (and do not hold it) are hidden for the shot, so the crop shows the component, not the chrome.
const STICKY = ['header', 'nav', '[class*="sticky" i]', '[data-testid*="sticky" i]'].join(', ');
export async function crop(page, locator, name, pad = 8) {
  fs.mkdirSync(CROPS, { recursive: true });
  const file = path.join(CROPS, `${name}.png`);
  const hidden = await locator.evaluate((el, { sel, pad }) => {
    let n = 0;
    const er = el.getBoundingClientRect();
    const scrolls = er.top - pad < 0 || er.bottom + pad > innerHeight || er.left < 0 || er.right > innerWidth + 1;
    document.querySelectorAll(sel).forEach((s) => {
      if (s.contains(el) || el.contains(s)) return;
      const sr = s.getBoundingClientRect();
      const overlap = !(sr.right < er.left - pad || sr.left > er.right + pad || sr.bottom < er.top - pad || sr.top > er.bottom + pad);
      // A bar clear of an in-view crop never shows. When the shot scrolls (the element is not fully
      // in view), sticky bars ride along over it, so every bar not holding the element goes.
      if (!overlap && !scrolls) return;
      s.setAttribute('data-m-hidden', '1');
      s.style.setProperty('visibility', 'hidden', 'important');
      s.style.setProperty('opacity', '0', 'important'); // children can re-declare visibility; opacity cannot be undone below
      n++;
    });
    return n;
  }, { sel: STICKY, pad });
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
    if (hidden) await page.evaluate(() => document.querySelectorAll('[data-m-hidden]').forEach((n) => { n.style.removeProperty('visibility'); n.style.removeProperty('opacity'); n.removeAttribute('data-m-hidden'); }));
  }
  quantize(file);
  return path.relative(REF, file);
}

export async function centre(locator) {
  await locator.evaluate((el) => el.scrollIntoView({ block: 'center', inline: 'nearest', behavior: 'instant' })).catch(() => {});
  await locator.page().waitForTimeout(350);
}

export function quantize(file) {
  execFileSync(PYTHON, [
    '-c',
    `import sys
from PIL import Image
p = sys.argv[1]
im = Image.open(p)
if im.mode not in ('RGB','P'):
    im = im.convert('RGB')
elif im.mode == 'P':
    im = im.convert('RGB')
im.quantize(colors=256, method=Image.FASTOCTREE).save(p, optimize=True)`,
    file,
  ]);
}
