// Shared helpers for the 1Password captures (adapted from the Allbirds ones).
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
export const BASE = 'https://1password.com';

export const HERE = path.dirname(new URL(import.meta.url).pathname);
export const REF = path.resolve(HERE, '..', '..', '..'); // systems/<slug>, from tools/capture/public
export const CROPS = path.join(REF, 'components', 'crops');
export const RAW = path.join(REF, 'raw');

// 1password.com is a Tailwind marketing site: utility classes with its own
// BEM-ish names (header-navigation, cta-btn, group/nav-item). M('btn')
// selects by class name; use literal selectors for anything else.
export const M = (name) => `.${name}`;

export async function launch({ width = 1440, height = 900, mobile = false } = {}) {
  const browser = await chromium.launch();
  const context = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width, height }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US', reducedMotion: 'no-preference' });
  return { browser, context };
}

// Dismiss whatever modal the page raised. 1password.com mounts no dialog on
// first load in the probe; the sweep covers a cookie/consent banner
// (OneTrust/Cookiebot/generic "Accept"/"×" bars) if one shows. The promo
// strip above the header is page chrome, not a modal — never removed.
// Consent: hide the banner, never choose. This used to write OneTrust's
// consent cookies with every group opted in (performance, functional,
// targeting), which is a consent choice made on the owner's behalf. It now
// aborts the OneTrust SDK at request level, so the banner never mounts and no
// consent record is written or sent (the acnestudios pattern).
export async function seedConsent(page) {
  await page.context().route(/cookielaw\.org|onetrust\.com|cookiepro\.com/, (r) => r.abort()).catch(() => {});
}

export async function closePromo(page) {
  // NB: do NOT click [class*=consent]/[id*=cookie] elements — on this site
  // those are footer "cookie settings" triggers that OPEN the OneTrust UI.
  const DLG = '#onetrust-banner-sdk, #onetrust-consent-sdk, [id*="onetrust" i], [class*="ot-sdk" i], [role="dialog"], dialog';
  for (let i = 0; i < 4; i++) {
    const dlg = page.locator(DLG).filter({ visible: true }).first();
    if (await dlg.count()) {
      // A consent banner is removed, never answered: no Accept, Reject or
      // Agree click. Any other dialog is closed by its own close control.
      if (await dlg.evaluate((n) => /onetrust|ot-sdk/i.test(n.id + ' ' + n.className) || /we use cookies|non-essential cookies/i.test(n.innerText || '')).catch(() => false)) {
        await dlg.evaluate((n) => n.remove()).catch(() => {});
        await page.waitForTimeout(300);
        continue;
      }
      const pick = dlg.locator('button:has-text("Close"), button:has-text("×"), button[aria-label*="lose" i], [class*="close"]').first();
      if (await pick.count()) await pick.click({ timeout: 5000 }).catch(() => {});
      else await page.keyboard.press('Escape');
      await page.waitForTimeout(1000);
      if (!(await dlg.isVisible().catch(() => false))) return true;
      continue;
    }
    // Remove-only sweep, main document and every child frame: the OneTrust
    // card on this site renders inside an about:blank iframe. Find the card
    // by its copy, delete the node, and hide the host iframe if it is a
    // fixed overlay. No clicks — clicking risks re-opening the settings UI.
    let hit = await page.evaluate(() => {
      let found = false;
      const box = [...document.querySelectorAll('div,section,aside,[role="dialog"]')].find((n) => {
        const t = n.innerText || '';
        const r = n.getBoundingClientRect();
        return /we use cookies|non-essential cookies/i.test(t) && t.length < 1400 && r.width > 250 && r.width < 1100 && r.height > 80;
      });
      if (box) { box.remove(); found = true; }
      for (const n of document.querySelectorAll('iframe')) {
        const cs = getComputedStyle(n); const r = n.getBoundingClientRect();
        if (/vimeo|youtube|player/i.test(n.src || '')) continue;
        if ((cs.position === 'fixed' || cs.position === 'absolute') && r.width > 200 && r.height > 100 && r.bottom > 0) { n.style.display = 'none'; found = true; }
      }
      return found;
    }).catch(() => false);
    for (const f of page.frames()) {
      if (f === page.mainFrame()) continue;
      const fh = await f.evaluate(() => {
        const box = [...document.querySelectorAll('body *')].find((n) => {
          const t = n.innerText || '';
          const r = n.getBoundingClientRect();
          return /we use cookies|non-essential cookies/i.test(t) && t.length < 1400 && r.width > 250;
        });
        if (!box) return false;
        box.remove(); // remove-only: never press Reject or Accept all
        return true;
      }).catch(() => false);
      hit = hit || fh;
    }
    // Closed-shadow sweep: the consent card lives in a shadow root that
    // DOM queries cannot see (no innerText, no frame, no host.shadowRoot).
    // elementFromPoint still resolves its HOST element, so scan a grid over
    // the viewport and hide any textless fixed/absolute overlay that is not
    // known page chrome.
    await page.evaluate(() => {
      const CHROME = /^(HTML|BODY|HEADER|NAV|MAIN|FOOTER|H[1-6]|A|BUTTON|P|SECTION|ARTICLE|UL|OL|LI|PICTURE|IMG|VIDEO|CANVAS|SVG|FORM|INPUT|LABEL|SPAN|SELECT|OPTION|IFRAME[src])$/i;
      const seen = new Set();
      for (let gy = 0.25; gy <= 0.92; gy += 0.12) {
        for (let gx = 0.15; gx <= 0.85; gx += 0.1) {
          const n = document.elementFromPoint(innerWidth * gx, innerHeight * gy);
          if (!n || seen.has(n)) continue;
          seen.add(n);
          if (CHROME.test(n.tagName)) continue;
          const cs = getComputedStyle(n);
          const z = parseInt(cs.zIndex, 10) || 0;
          const txt = (n.innerText || '').replace(/\s+/g, '');
          if ((cs.position === 'fixed' || cs.position === 'absolute' || z >= 1000) && txt.length === 0) n.style.display = 'none';
        }
      }
    }).catch(() => {});
    if (!hit) return false;
    await page.waitForTimeout(800);
  }
  await page.waitForTimeout(800);
  return true;
}

// Alias kept for callers that clear a one-shot modal before each step;
// 1password has no region gate, so this is just the consent sweep.
export async function killGeo(page) {
  await closePromo(page);
}

// Finds a visible element in-page whose trimmed innerText matches reText,
// tags it with data-m-mark="<tag>" and returns a locator for it. up optionally
// retargets an ancestor (closest()). Use where getByRole/hasText miss nodes
// whose text lives in nested spans.
export async function domFind(page, reText, { sel = 'button, a', tag = 'm', up = null, nth = 0, leaf = true, minW = 0, minH = 0 } = {}) {
  const ok = await page.evaluate(
    ([src, flags, s, t, upSel, i, leafOnly, w, h]) => {
      const re = new RegExp(src, flags);
      document.querySelectorAll(`[data-m-mark="${t}"]`).forEach((n) => n.removeAttribute('data-m-mark'));
      const els = [...document.querySelectorAll(s)].filter((n) => {
        const r = n.getBoundingClientRect();
        const cs = getComputedStyle(n);
        return r.width >= w && r.height >= h && r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && re.test((n.innerText || '').trim());
      });
      // leaf: a container holding another match is a wrapper, not the target
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

// Finds a visible element by text and clicks it in-page: no Playwright
// actionability and no node detachment race (the buy box re-renders on geo
// resolution, so a locator resolved moments ago can be stale).
export async function domClick(page, reText, sel = 'button, a') {
  return page.evaluate(
    ([src, flags, s]) => {
      const re = new RegExp(src, flags);
      const els = [...document.querySelectorAll(s)].filter((n) => {
        const r = n.getBoundingClientRect();
        const cs = getComputedStyle(n);
        return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && !n.disabled;
      });
      const el = els.find((n) => re.test((n.innerText || '').trim()));
      if (!el) return false;
      el.click();
      return true;
    },
    [reText.source, reText.flags, sel],
  );
}

export async function open(page, url, { wait = 6000, promo = 'close' } = {}) {
  if (url.startsWith(BASE)) await seedConsent(page);
  await page.goto(url, { waitUntil: 'load', timeout: 90000 });
  await page.waitForTimeout(wait);
  if (promo === 'close') await closePromo(page);
}

// 1password.com has no product grid; pricing links go straight to plan pages.
// Kept for parity with the kit's page scripts.
export async function openFirstProduct(p) {
  const link = p.locator('a[href^="/pricing"], a[href^="/product/"]').first();
  await link.scrollIntoViewIfNeeded();
  await link.click();
  await p.waitForTimeout(4000);
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
const STICKY = ['.header-navigation', 'header', '[class*="sticky" i]', '[class*="fixed" i]'].join(', ');
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
