// Installs window.__cap in Conductor's page: readers for custom properties and computed styles,
// and helpers that reveal states (click, type, keys, forced pseudo-classes). Run once per page load.
const C = window.__cap = {};
C.PROPS = ['color', 'background-color', 'background-image', 'border-top-color', 'border-top-width', 'border-top-style',
  'border-bottom-color', 'border-bottom-width', 'border-top-left-radius', 'border-bottom-right-radius', 'box-shadow', 'outline-color', 'outline-width', 'outline-style', 'outline-offset',
  'font-family', 'font-size', 'font-weight', 'line-height', 'letter-spacing', 'text-transform', 'text-decoration-line',
  'padding-top', 'padding-right', 'padding-bottom', 'padding-left', 'gap', 'width', 'height', 'opacity',
  'backdrop-filter', 'transition-duration', 'transition-timing-function', 'transition-property', 'cursor', 'z-index'];
C.sleep = ms => new Promise(r => setTimeout(r, ms));
C.vis = e => { if (!e) return false; const r = e.getBoundingClientRect(); return r.width > 1 && r.height > 1 && getComputedStyle(e).visibility !== 'hidden'; };
C.$ = (sel, root = document) => [...root.querySelectorAll(sel)].filter(C.vis);
// Elements whose own text (trimmed) equals t, innermost first.
C.byText = (t, sel = '*', root = document) => [...root.querySelectorAll(sel)].filter(e => C.vis(e) && (e.innerText || e.textContent || '').trim() === t).reverse();
C.btn = (t) => C.byText(t, 'button, [role=button], [role=menuitem], [role=tab], [role=option], a, [role=radio], [role=switch]')[0];
C.click = (e) => {
  if (typeof e === 'string') e = C.btn(e) || document.querySelector(e);
  if (!e) throw new Error('nothing to click');
  const r = e.getBoundingClientRect(), o = { bubbles: true, cancelable: true, composed: true, clientX: r.x + r.width / 2, clientY: r.y + r.height / 2, button: 0, pointerId: 1, pointerType: 'mouse', isPrimary: true };
  e.dispatchEvent(new PointerEvent('pointerdown', o)); e.dispatchEvent(new MouseEvent('mousedown', o));
  e.dispatchEvent(new PointerEvent('pointerup', o)); e.dispatchEvent(new MouseEvent('mouseup', o));
  e.dispatchEvent(new MouseEvent('click', o));
  return true;
};
C.key = (key, target = document.activeElement || document.body, mods = {}) => {
  const o = { key, code: key.length === 1 ? 'Key' + key.toUpperCase() : key, bubbles: true, cancelable: true, composed: true, ...mods };
  target.dispatchEvent(new KeyboardEvent('keydown', o)); target.dispatchEvent(new KeyboardEvent('keyup', o));
};
C.esc = async (n = 1) => { for (let i = 0; i < n; i++) { C.key('Escape'); await C.sleep(250); } };
// Type into an input or textarea the way React sees it, or into a contenteditable.
C.type = (e, text) => {
  if (typeof e === 'string') e = document.querySelector(e);
  e.focus();
  if (e.isContentEditable) { document.execCommand('selectAll'); document.execCommand('insertText', false, text); return; }
  const proto = e.tagName === 'TEXTAREA' ? HTMLTextAreaElement.prototype : HTMLInputElement.prototype;
  Object.getOwnPropertyDescriptor(proto, 'value').set.call(e, text);
  e.dispatchEvent(new Event('input', { bubbles: true }));
};
C.box = e => { const r = e.getBoundingClientRect(), d = devicePixelRatio; return [r.x, r.y, r.width, r.height].map(v => Math.round(v * d)); };
C.style = (e, props = C.PROPS) => {
  // A url() in a computed value (a background photo, a cursor) can be a signed or per-account URL:
  // recorded as url(…), only data: and #fragment references kept (the kit's noUrl).
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\(\s*(?!['"]?(?:data:|#))(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^)]*)\s*\)/g, 'url(…)') : v);
  const cs = getComputedStyle(e), r = e.getBoundingClientRect(), out = {};
  for (const p of props) out[p] = noUrl(cs.getPropertyValue(p));
  out._box = [r.x, r.y, r.width, r.height].map(v => Math.round(v * 10) / 10);
  out._tag = e.tagName.toLowerCase(); out._role = e.getAttribute('role');
  out._slot = e.getAttribute('data-slot'); out._cls = (e.getAttribute('class') || '').slice(0, 400);
  return out;
};
C.viewport = () => ({ dpr: devicePixelRatio, css: [innerWidth, innerHeight], device: [Math.round(innerWidth * devicePixelRatio), Math.round(innerHeight * devicePixelRatio)],
  title: document.title, htmlClass: document.documentElement.className, bodyClass: document.body.className });
// parts: { name: Element | selector | () => Element }
C.measure = (parts) => {
  const out = {};
  for (const [k, s] of Object.entries(parts)) {
    let e = typeof s === 'function' ? s() : typeof s === 'string' ? C.$(s)[0] : s;
    if (!e || !C.vis(e)) continue;
    out[k] = { box: C.box(e), style: C.style(e) };
  }
  return out;
};
// Every named thing on screen, for choosing parts.
C.inventory = (sel = '[data-slot], [role], [aria-label], button, input, textarea, [contenteditable=true]') => {
  const m = [];
  for (const e of document.querySelectorAll(sel)) {
    if (!C.vis(e)) continue;
    const r = e.getBoundingClientRect();
    m.push({ tag: e.tagName.toLowerCase(), slot: e.getAttribute('data-slot'), role: e.getAttribute('role'), aria: e.getAttribute('aria-label'),
      text: (e.innerText || '').trim().slice(0, 40), box: [r.x, r.y, r.width, r.height].map(Math.round), cls: (e.getAttribute('class') || '').slice(0, 160) });
  }
  return m;
};
// Forced pseudo-classes: copy every rule whose selector uses :hover / :focus-visible / :active / :focus
// into a capture stylesheet with the pseudo-class swapped for [data-cap-<state>], then mark the element.
// The values painted are the product's own declarations; only the trigger is replaced.
C.forceSheet = () => {
  let st = document.getElementById('cap-force');
  if (st) return st;
  const pseudo = { hover: /:hover/g, 'focus-visible': /:focus-visible/g, active: /:active/g, focus: /:focus(?![-\w])/g, 'focus-within': /:focus-within/g };
  const lines = [];
  const walk = (rules, wrap) => {
    for (const r of rules) {
      if (r.cssRules && !r.style) {
        const c = r.media ? `@media ${r.media.mediaText}` : r.conditionText !== undefined && r.constructor.name.includes('Supports') ? `@supports ${r.conditionText}` : null;
        walk(r.cssRules, c && !/hover/.test(c) ? [...wrap, c] : wrap); continue;
      }
      if (!r.selectorText || !/:(hover|focus|active)/.test(r.selectorText)) { if (r.cssRules && r.cssRules.length) walk(r.cssRules, wrap); continue; }
      let sel = r.selectorText;
      for (const [k, re] of Object.entries(pseudo)) sel = sel.replace(re, `[data-cap-${k}]`);
      // nested rules (&:hover) are already resolved in selectorText by WebKit
      let body = `${sel}{${r.style.cssText}}`;
      for (const w of [...wrap].reverse()) body = `${w}{${body}}`;
      lines.push(body);
    }
  };
  for (const s of document.styleSheets) { try { walk(s.cssRules, []); } catch {} }
  st = document.createElement('style'); st.id = 'cap-force'; st.textContent = lines.join('\n');
  document.head.appendChild(st);
  return st;
};
C.force = (e, states) => {
  C.forceSheet();
  if (typeof e === 'string') e = C.$(e)[0];
  for (const s of states) e.setAttribute(`data-cap-${s}`, '');
  if (states.includes('focus-visible') || states.includes('focus')) { let p = e.parentElement; while (p) { p.setAttribute('data-cap-focus-within', ''); p = p.parentElement; } }
  return e;
};
C.unforce = () => { for (const s of ['hover', 'focus-visible', 'active', 'focus', 'focus-within']) document.querySelectorAll(`[data-cap-${s}]`).forEach(e => e.removeAttribute(`data-cap-${s}`)); };
C.tag = (e, n) => { e.setAttribute('data-cap', n); return `[data-cap="${n}"]`; };
C.untag = () => document.querySelectorAll('[data-cap]').forEach(e => e.removeAttribute('data-cap'));
C.vars = (scopes = [], keep = '^--') => {
  const KEEP = new RegExp(keep);
  const sheets = [], decls = [], names = new Set(), conditions = {};
  [...document.styleSheets].forEach((s, i) => {
    const owner = s.ownerNode;
    const id = s.href ? s.href.split('/').slice(-1)[0] : (owner && (owner.id || owner.getAttribute('data-vite-dev-id') || owner.className)) || `inline-${i}`;
    if (id === 'cap-force') return;
    let rules; try { rules = s.cssRules; } catch { sheets.push({ id, unreadable: true }); return; }
    sheets.push({ id, rules: rules.length });
    const walk = (rs, cond) => {
      for (const r of rs) {
        if (r.cssRules && !r.style) {
          const c = r.conditionText || (r.media && r.media.mediaText) || (r.name !== undefined ? `@layer ${r.name}` : '') || r.constructor.name;
          walk(r.cssRules, cond ? `${cond} && ${c}` : c); continue;
        }
        if (!r.style) continue;
        if (cond && /reduced-motion|width|hover|pointer|contrast|color-scheme/.test(cond)) {
          const k = cond.slice(0, 160), e = conditions[k] ||= { rules: 0, properties: {}, selectors: [] };
          e.rules++; for (const p of r.style) e.properties[p] = (e.properties[p] || 0) + 1;
          if (e.selectors.length < 6) e.selectors.push((r.selectorText || '').slice(0, 120));
        }
        for (const p of r.style) if (p.startsWith('--') && KEEP.test(p)) {
          names.add(p);
          decls.push({ name: p, value: r.style.getPropertyValue(p).trim(), selector: (r.selectorText || r.constructor.name).slice(0, 200), condition: cond || '', sheet: id });
        }
        if (r.cssRules && r.cssRules.length) walk(r.cssRules, cond);
      }
    };
    walk(rules, '');
  });
  const computed = {};
  const els = { html: document.documentElement, body: document.body };
  for (const s of scopes) { const e = document.querySelector(s); if (e) els[s] = e; }
  for (const e of Object.values(els)) for (const p of e.style) if (p.startsWith('--') && KEEP.test(p)) names.add(p);
  for (const [k, e] of Object.entries(els)) {
    const cs = getComputedStyle(e), v = {};
    for (const n of [...names].sort()) { const x = cs.getPropertyValue(n).trim(); if (x) v[n] = x; }
    computed[k] = v;
  }
  const scopeKey = scopes[0] && document.querySelector(scopes[0]) ? scopes[0] : 'body';
  const scopeEl = els[scopeKey];
  const host = document.createElement('div'), probe = document.createElement('div');
  host.style.cssText = 'position:fixed;left:-99px;top:-99px;color:rgb(1, 2, 3)';
  host.appendChild(probe); scopeEl.appendChild(host);
  const colors = {}, shadows = {};
  for (const n of Object.keys(computed[scopeKey])) {
    probe.style.color = ''; probe.style.color = `var(${n})`;
    const c = getComputedStyle(probe).color;
    if (c !== 'rgb(1, 2, 3)' || computed[scopeKey][n] === 'rgb(1, 2, 3)') colors[n] = c;
    if (/shadow/.test(n)) { probe.style.boxShadow = `var(${n})`; shadows[n] = getComputedStyle(probe).boxShadow; probe.style.boxShadow = ''; }
  }
  host.remove();
  const faces = [];
  for (const f of document.fonts) faces.push({ family: f.family, weight: f.weight, style: f.style, status: f.status });
  const sc = getComputedStyle(scopeEl);
  const inline = {}; for (const p of document.documentElement.style) inline[p] = document.documentElement.style.getPropertyValue(p).trim();
  return { meta: { ...C.viewport(), read: new Date().toISOString().slice(0, 10) }, scope: scopeKey, sheets, decls, computed, colors, shadows, conditions, htmlInline: inline,
    fonts: { faces, body: getComputedStyle(document.body).fontFamily, scope: { family: sc.fontFamily, size: sc.fontSize, weight: sc.fontWeight, lineHeight: sc.lineHeight } } };
};
// Interactive and text-bearing descendants of root, for choosing parts.
C.tree = (root, max = 80) => {
  if (typeof root === 'string') root = C.$(root)[0];
  const out = [];
  for (const e of root.querySelectorAll('*')) {
    if (!C.vis(e) || /^(path|svg|g|circle|rect|line|polyline)$/i.test(e.tagName)) continue;
    const own = [...e.childNodes].filter(n => n.nodeType === 3).map(n => n.textContent.trim()).join(' ').trim();
    const inter = /^(BUTTON|INPUT|TEXTAREA|SELECT|A|LABEL|H\d)$/.test(e.tagName) || e.getAttribute('role');
    if (!own && !inter) continue;
    const r = e.getBoundingClientRect();
    out.push([e.tagName.toLowerCase(), e.getAttribute('role'), own.slice(0, 30), [r.x, r.y, r.width, r.height].map(Math.round).join(','), (e.getAttribute('class') || '').slice(0, 90)]);
    if (out.length >= max) break;
  }
  return out;
};
