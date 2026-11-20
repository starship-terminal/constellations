// Measures NotebookLM's signed-in components from the static page copies (see render.mjs,
// unsnap.py), in both themes and in every state CSS can reach once scripts are gone. Adapted from
// systems/linear/tools/capture/signed-in/measure.mjs (itself from the kit).
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs SNAPS=<dir of page copies> node tools/capture/signed-in/measure.mjs [label ...] [--jobs N]
//
// With labels, only the components (and states) that live on those copies are re-measured and
// merged into the existing JSON. Writes raw/components-computed.json and one crop per component
// and state into components/crops/<component>-<state>.png (2x, 256 colours, halved when wider than
// 1600px). raw/measurements.md is then built from the JSON by build-measurements.mjs.
//
// Themes: every copy was taken in dark. Each spec names its dark copy (`notebook-dark`); the same
// copy is opened again with the body's dark-theme class swapped for light-theme (lib.mjs setLight)
// and measured in light. Dark states keep their plain names (`default`, `hover`, ...); light
// states are `light`, `light-hover`, ... and every state records `theme`.
//
// States:
//   default        at rest, as captured
//   hover          real mouse hover (page.mouse.move), 450ms settle; Tailwind's hover: variants
//                  (inside @media (hover: hover)) are plain CSS, so they apply on the static copy
//   focus-visible  real keyboard focus: focus(), Shift+Tab, Tab (or a Shift keydown then focus()),
//                  on the element or its first focusable descendant
//   pressed        mouse hover, then the button held down (page.mouse.down) for 250ms, so :active
//                  applies; released after the reading
//   anything else  another element, or another copy, captured in that state: `active`, `selected`,
//                  `checked`, `open`, `typed`, `on`, ...
// The pressed state releases the mouse over the element, so a click event fires, but the copies have
// no scripts, clicks are cancelled, and every navigation away from the file is aborted.
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { safeUrl } from '../safe-url.mjs';
import { chromium, REF, RAW, CROPS, SNAPS, SCROLL, metaOf, newContext, openSnap, setLight } from './lib.mjs';

if (!SNAPS) { console.error('SNAPS=<snapshot dir> is required'); process.exit(2); }
const OUT = path.join(RAW, 'components-computed.json');
const args = process.argv.slice(2);
const jobsArg = args.indexOf('--jobs');
const CONC = jobsArg >= 0 ? +args[jobsArg + 1] : 4;
const ONLY = args.filter((a, i) => !a.startsWith('--') && (jobsArg < 0 || i !== jobsArg + 1));
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

// ---------------------------------------------------------------- page helpers (run in the page)
//
// Finders are plain functions of these globals, so a spec reads as what it looks for:
//   T(text, root)     the visible element whose innerText is exactly `text`, in the viewport first,
//                     then the smallest; TS(prefix, root) the same by prefix
//   Q(sel, i, root)   the i-th visible match of a CSS selector, in-viewport matches first
//   K(tokens, i, root) the i-th visible element carrying every class token (no CSS escaping needed
//                     for Tailwind names such as `group/nav-tab` or `p-[1px]`)
//   C(el, sel)        el.closest(sel);  CK(el, tokens) the closest element carrying the tokens
//   W(el, w)          el or the first ancestor at least `w` px wide (H(el, h) the same by height)
//   unhidden(list)    the first element of a list whose centre nothing covers;  at(x, y) the element there
//   P(el)             el or the first ancestor that paints a fill, border or shadow
//   D()               the last visible [role=dialog];  MN() the last visible [role=menu]
//   M()               the main content column (main.dframe-content);  S() the sidebar (aside.dframe-sidebar)
const HELPERS = () => {
  const vis = (e) => {
    if (!e || !e.getBoundingClientRect) return false;
    const r = e.getBoundingClientRect();
    if (r.width < 1 || r.height < 1) return false;
    const cs = getComputedStyle(e);
    if (cs.visibility !== 'visible' || cs.display === 'none') return false;
    // Opacity is not inherited in the computed style, so a popover held at opacity 0 (the thread's
    // hover outline, a hover-only toolbar) is found by walking up.
    for (let n = e; n && n !== document.documentElement; n = n.parentElement) if (+getComputedStyle(n).opacity === 0) return false;
    return true;
  };
  const inVp = (e) => { const r = e.getBoundingClientRect(); return r.bottom > 0 && r.right > 0 && r.top < innerHeight && r.left < innerWidth ? 1 : 0; };
  const order = (list) => list.filter(vis).map((e, i) => [e, i]).sort((a, b) => inVp(b[0]) - inVp(a[0]) || a[1] - b[1]).map((x) => x[0]);
  const area = (e) => { const r = e.getBoundingClientRect(); return r.width * r.height; };
  const byText = (pred, needle, root) => {
    root = root || document.body;
    // An sr-only label (a 1x1 clipped box) never counts as the visible text.
    const c = [...root.querySelectorAll('*')].filter((e) => e.textContent.includes(needle) && pred((e.innerText || '').trim()) && vis(e) && area(e) > 4);
    c.sort((a, b) => inVp(b) - inVp(a) || area(a) - area(b));
    return c[0] || null;
  };
  const hasTokens = (e, tokens) => e.classList && tokens.split(/\s+/).filter(Boolean).every((t) => e.classList.contains(t));
  const paints = (e) => {
    const cs = getComputedStyle(e);
    return cs.backgroundColor !== 'rgba(0, 0, 0, 0)' || cs.backgroundImage !== 'none' || cs.boxShadow !== 'none' || ['Top', 'Right', 'Bottom', 'Left'].some((s) => parseFloat(cs[`border${s}Width`]) > 0 && cs[`border${s}Style`] !== 'none');
  };
  Object.assign(window, {
    T: (text, root) => byText((t) => t === text, text, root),
    TS: (prefix, root) => byText((t) => t.startsWith(prefix), prefix, root),
    Q: (sel, i = 0, root = document) => order([...root.querySelectorAll(sel)])[i] || null,
    K: (tokens, i = 0, root = document) => order([...root.querySelectorAll('*')].filter((e) => hasTokens(e, tokens)))[i] || null,
    C: (el, sel) => (el ? el.closest(sel) : null),
    CK: (el, tokens) => { for (let n = el; n && n !== document.documentElement; n = n.parentElement) if (hasTokens(n, tokens)) return n; return null; },
    H: (el, h) => { for (let n = el; n && n !== document.documentElement; n = n.parentElement) if (n.getBoundingClientRect().height >= h - 0.5) return n; return null; },
    // The first visible element of a list whose centre is not covered by anything else.
    unhidden: (list) => [...list].find((e) => { if (!vis(e)) return false; const r = e.getBoundingClientRect(); const h = document.elementFromPoint(r.x + r.width / 2, r.y + r.height / 2); return h && (e.contains(h) || h.contains(e)); }) || null,
    W: (el, w) => { for (let n = el; n && n !== document.documentElement; n = n.parentElement) if (n.getBoundingClientRect().width >= w - 0.5) return n; return null; },
    at: (x, y) => document.elementFromPoint(x, y),
    P: (el) => { for (let n = el; n && n !== document.documentElement; n = n.parentElement) if (paints(n)) return n; return null; },
    D: () => { const d = [...document.querySelectorAll('[role=dialog]')].filter(vis); return d[d.length - 1] || null; },
    // PRODUCT (adapt): NotebookLM's chat column and the sources panel.
    M: () => document.querySelector('section.chat-panel') || document.querySelector('main') || document.body,
    S: () => document.querySelector('section.source-panel'),
    // NotebookLM (adapt): the share dialog's select panel was copied where the live overlay had
    // placed it, off the 1440 viewport; this moves its overlay pane under the trigger.
    MOVESEL: () => { const p = document.querySelector('.mat-mdc-select-panel'); const pane = p && p.closest('.cdk-overlay-pane'); const t = document.querySelector('mat-select.general-access-select-dropdown'); if (!pane || !t) return; const r = t.getBoundingClientRect(); const box = pane.parentElement; if (box && box.classList.contains('cdk-overlay-connected-position-bounding-box')) Object.assign(box.style, { top: '0px', left: '0px', width: innerWidth + 'px', height: innerHeight + 'px', right: 'auto', bottom: 'auto' }); Object.assign(pane.style, { position: 'absolute', top: (r.bottom + 4) + 'px', left: (r.left - 16) + 'px', right: 'auto', bottom: 'auto', transform: 'none' }); },
    // An element by exact text, then the closest button, link or row around it.
    TB: (text, root) => { const t = byText((x) => x === text, text, root); return t ? (t.closest('button, a, [role=button], [role=option], [role=tab]') || t) : null; },
    // The first ancestor of el (or el) that casts a box-shadow: a menu's or popover's surface.
    SHD: (el) => { for (let n = el; n && n !== document.documentElement; n = n.parentElement) if (getComputedStyle(n).boxShadow !== 'none') return n; return null; },
    // A highlight box slid under the active option of a listbox (a separate absolutely positioned
    // div, moved by script); kept from the Linear adaptation, unused here.
    HL: () => { const lb = Q('[role=listbox]'); return lb ? [...lb.parentElement.querySelectorAll('div')].find((d) => { const c = getComputedStyle(d); const r = d.getBoundingClientRect(); return c.position === 'absolute' && r.height >= 26 && r.height <= 40 && c.backgroundColor !== 'rgba(0, 0, 0, 0)'; }) || null : null; },
    // The innermost painted box of at least w x h that contains el.
    BOX: (el, w, h) => { for (let n = el; n && n !== document.documentElement; n = n.parentElement) { const r = n.getBoundingClientRect(); if (r.width >= w && r.height >= h && paints(n)) return n; } return null; },
    MN: () => { const d = [...document.querySelectorAll('[role=menu]')].filter(vis); return d[d.length - 1] || null; },
    painted: (list) => [...list].find((e) => vis(e) && paints(e)) || null,
    unpainted: (list) => [...list].find((e) => vis(e) && !paints(e)) || null,
  });
  window.__isFocusable = (e) => e && (e.tabIndex >= 0 || e.isContentEditable || /^(A|BUTTON|INPUT|SELECT|TEXTAREA)$/.test(e.tagName)) && !e.disabled;
  window.__focusTarget = (e) => {
    if (window.__isFocusable(e)) return e;
    return [...e.querySelectorAll('a[href], button, input, select, textarea, [tabindex], [contenteditable=true]')].find((x) => window.__isFocusable(x) && vis(x)) || null;
  };
  // Every scroller's position as the snapshot was opened (after the scroll rule), put back before
  // each measurement, so an earlier component scrolled into view does not move a later one.
  window.__saveScroll = () => { window.__scrolls = [...document.querySelectorAll('*')].filter((e) => e.scrollTop || e.scrollLeft).map((e) => [e, e.scrollTop, e.scrollLeft]); window.__scrollY = scrollY; };
  window.__restoreScroll = () => { for (const [e, t, l] of window.__scrolls || []) { e.scrollTop = t; e.scrollLeft = l; } document.querySelectorAll('*').forEach((e) => { if ((e.scrollTop || e.scrollLeft) && !(window.__scrolls || []).some((x) => x[0] === e)) { e.scrollTop = 0; e.scrollLeft = 0; } }); scrollTo(0, window.__scrollY || 0); };
  // CSS animations are pinned so two runs crop the same pixels: a finite one (an entrance fade) is
  // finished, an infinite one (the promo progress, marquees, skeleton pulses) held at its first
  // frame. Transitions are left alone: hover and focus need them to finish.
  window.__freeze = () => {
    for (const a of document.getAnimations()) {
      if (typeof CSSAnimation === 'undefined' || !(a instanceof CSSAnimation)) continue;
      const t = a.effect && a.effect.getComputedTiming();
      if (t && t.iterations === Infinity) { a.pause(); a.currentTime = 0; } else { try { a.finish(); } catch { a.pause(); } }
    }
  };
  document.addEventListener('click', (e) => e.preventDefault(), true);
  document.addEventListener('submit', (e) => e.preventDefault(), true);
};

// Computed properties recorded for every component and state (the gauth set).
const PROPS = [
  'display', 'position', 'boxSizing', 'width', 'height', 'minWidth', 'maxWidth', 'minHeight',
  'paddingTop', 'paddingRight', 'paddingBottom', 'paddingLeft',
  'marginTop', 'marginRight', 'marginBottom', 'marginLeft',
  'gap', 'rowGap', 'columnGap', 'flexDirection', 'alignItems', 'justifyContent', 'gridTemplateColumns',
  'borderTopWidth', 'borderTopStyle', 'borderTopColor', 'borderRightWidth', 'borderRightStyle', 'borderRightColor',
  'borderBottomWidth', 'borderBottomStyle', 'borderBottomColor', 'borderLeftWidth', 'borderLeftStyle', 'borderLeftColor',
  'borderTopLeftRadius', 'borderTopRightRadius', 'borderBottomRightRadius', 'borderBottomLeftRadius',
  'backgroundColor', 'backgroundImage', 'boxShadow', 'backdropFilter', 'filter',
  'outlineWidth', 'outlineStyle', 'outlineColor', 'outlineOffset',
  'fontFamily', 'fontSize', 'fontWeight', 'lineHeight', 'letterSpacing', 'textTransform', 'textAlign',
  'color', 'textDecorationLine', 'textDecorationColor', 'textDecorationThickness', 'textUnderlineOffset',
  'transitionProperty', 'transitionDuration', 'transitionTimingFunction', 'transitionDelay',
  'cursor', 'opacity', 'transform', 'overflow', 'zIndex', 'top',
];

// Reads one element: computed style, rect, ::before/::after, the painted layers inside it (so a
// root that paints nothing still shows what does), the paint of up to three ancestors, the first
// text node's type, the first icon, a field's placeholder (the composer's is Tiptap's
// `p.is-editor-empty::before`), and every `var(--x)` its classes and painted children name, with
// the value that variable resolves to in the current theme.
function styleOf(el, props) {
  const cls = (n) => (typeof n.className === 'string' ? n.className : n.getAttribute('class') || '');
  const short = (n) => n.tagName.toLowerCase() + cls(n).split(/\s+/).filter((c) => c && !c.includes('[') && !c.includes(':')).slice(0, 3).map((c) => '.' + c).join('');
  // A url() in a computed value (a background photo, a cursor) can be a signed or per-account URL:
  // recorded as url(…), only data: and #fragment references kept (the kit's noUrl).
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\(\s*(?!['"]?(?:data:|#))(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^)]*)\s*\)/g, 'url(…)') : v);
  const pick = (cs) => { const o = {}; for (const p of props) o[p] = noUrl(cs[p]); return o; };
  const cs = getComputedStyle(el);
  const r = el.getBoundingClientRect();
  const out = {
    tag: el.tagName.toLowerCase(),
    classes: cls(el).slice(0, 700),
    text: (el.innerText || el.getAttribute('aria-label') || el.getAttribute('placeholder') || '').trim().replace(/\s+/g, ' ').slice(0, 80),
    rect: { x: +r.x.toFixed(1), y: +r.y.toFixed(1), w: +r.width.toFixed(2), h: +r.height.toFixed(2) },
    style: pick(cs),
  };
  for (const a of ['role', 'aria-label', 'data-cds', 'data-state', 'data-active', 'aria-checked', 'aria-selected', 'data-variant']) if (el.hasAttribute(a)) (out.attrs ||= {})[a] = el.getAttribute(a);
  for (const pe of ['::before', '::after']) {
    const p = getComputedStyle(el, pe);
    if (p.content && p.content !== 'none' && p.content !== 'normal') {
      out[pe] = { content: noUrl(p.content).slice(0, 40), width: p.width, height: p.height, position: p.position, backgroundColor: p.backgroundColor, backgroundImage: noUrl(p.backgroundImage).slice(0, 200), boxShadow: p.boxShadow, borderTopWidth: p.borderTopWidth, borderTopStyle: p.borderTopStyle, borderTopColor: p.borderTopColor, borderRadius: p.borderRadius, inset: `${p.top} ${p.right} ${p.bottom} ${p.left}`, opacity: p.opacity, transition: p.transition };
    }
  }
  const paint = [];
  const nodes = [el, ...el.querySelectorAll('*')].slice(0, 400);
  for (const n of nodes) {
    if (paint.length >= 14) break;
    if (n.closest('svg') && n.tagName.toLowerCase() !== 'svg') continue;
    const nr = n.getBoundingClientRect();
    if (nr.width < 1 || nr.height < 1) continue;
    for (const pe of [null, '::before', '::after']) {
      const c = getComputedStyle(n, pe);
      if (pe && (c.content === 'none' || c.content === 'normal')) continue;
      if (c.visibility !== 'visible') continue;
      const bw = ['Top', 'Right', 'Bottom', 'Left'].map((sd) => (parseFloat(c[`border${sd}Width`]) > 0 && c[`border${sd}Style`] !== 'none' ? `${sd[0]}:${c[`border${sd}Width`]} ${c[`border${sd}Style`]} ${c[`border${sd}Color`]}` : '')).filter(Boolean);
      const bg = c.backgroundColor !== 'rgba(0, 0, 0, 0)' ? c.backgroundColor : '';
      const bgi = c.backgroundImage !== 'none' && !/^url\("?https?:/.test(c.backgroundImage) ? noUrl(c.backgroundImage).replace(/url\("data:[^)]{60,}\)/g, 'url(data:…)').slice(0, 200) : '';
      const sh = c.boxShadow !== 'none' ? c.boxShadow : '';
      const ol = c.outlineStyle !== 'none' && parseFloat(c.outlineWidth) > 0 ? `${c.outlineWidth} ${c.outlineStyle} ${c.outlineColor} offset ${c.outlineOffset}` : '';
      if (!(bw.length || bg || bgi || sh || ol)) continue;
      if (n.tagName === 'IMG' && !bw.length && !sh) continue;
      paint.push({ node: short(n) + (pe || ''), size: pe ? `${c.width}x${c.height}` : `${nr.width.toFixed(1)}x${nr.height.toFixed(1)}`, border: bw.join(' | ') || undefined, bg: bg || undefined, bgImage: bgi || undefined, shadow: sh || undefined, outline: ol || undefined, radius: c.borderRadius !== '0px' ? c.borderRadius : undefined, opacity: c.opacity !== '1' ? c.opacity : undefined });
    }
  }
  if (paint.length) out.paint = paint;
  const anc = [];
  for (let n = el.parentElement, i = 0; n && i < 3; n = n.parentElement, i++) {
    const c = getComputedStyle(n);
    const fill = i < 1 && c.backgroundColor !== 'rgba(0, 0, 0, 0)';
    if (fill || c.boxShadow !== 'none' || (c.outlineStyle !== 'none' && parseFloat(c.outlineWidth) > 0 && c.outlineColor !== 'rgba(0, 0, 0, 0)')) anc.push({ up: i + 1, node: short(n), shadow: c.boxShadow !== 'none' ? c.boxShadow : undefined, outline: c.outlineStyle !== 'none' ? `${c.outlineWidth} ${c.outlineStyle} ${c.outlineColor}` : undefined, radius: c.borderRadius, bg: c.backgroundColor });
  }
  if (anc.length) out.ancestors = anc;
  const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, { acceptNode: (t) => (t.textContent.trim() && t.parentElement && t.parentElement.getBoundingClientRect().width > 1 && getComputedStyle(t.parentElement).visibility === 'visible' ? 1 : 3) });
  // Icon fonts render ligatures as text ("add", "description"); read the label first and fall
  // back to the icon glyph only when the element has no other text (icon buttons).
  const isIcon = (t) => !!t.parentElement.closest('mat-icon, .material-symbols-outlined, .material-symbols-rounded, .google-symbols, [class*="symbols"]') || /Symbols/.test(getComputedStyle(t.parentElement).fontFamily);
  let tn = null, iconTn = null;
  for (let t = walker.nextNode(); t; t = walker.nextNode()) {
    if (!isIcon(t)) { tn = t; break; }
    iconTn = iconTn || t;
  }
  if (iconTn) {
    const ic = getComputedStyle(iconTn.parentElement);
    out.iconStyle = { node: short(iconTn.parentElement), text: iconTn.textContent.trim().slice(0, 40), fontFamily: ic.fontFamily, fontSize: ic.fontSize, fontVariationSettings: ic.fontVariationSettings, color: ic.color };
  }
  tn = tn || iconTn;
  if (tn && tn.parentElement !== el) {
    const t = tn.parentElement;
    const tc = getComputedStyle(t);
    out.textStyle = { node: short(t), text: tn.textContent.trim().slice(0, 40), fontFamily: tc.fontFamily, fontSize: tc.fontSize, lineHeight: tc.lineHeight, fontWeight: tc.fontWeight, letterSpacing: tc.letterSpacing, color: tc.color, textDecorationLine: tc.textDecorationLine, textTransform: tc.textTransform };
  }
  if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA' || el.querySelector('input')) {
    const f = el.tagName === 'INPUT' || el.tagName === 'TEXTAREA' ? el : el.querySelector('input');
    const ph = getComputedStyle(f, '::placeholder');
    out.placeholder = { text: f.getAttribute('placeholder'), color: ph.color, opacity: ph.opacity, fontSize: ph.fontSize, lineHeight: ph.lineHeight };
  }
  const pp = el.querySelector('[contenteditable=true] p[data-placeholder], [contenteditable=true] p.is-editor-empty') || (el.matches('p[data-placeholder]') ? el : null);
  if (pp) {
    const b = getComputedStyle(pp, '::before');
    out.placeholder = { text: pp.getAttribute('data-placeholder') || noUrl(b.content).slice(0, 80), color: b.color, opacity: b.opacity, fontSize: b.fontSize, lineHeight: b.lineHeight, float: b.cssFloat, height: b.height };
  }
  const svg = el.tagName.toLowerCase() === 'svg' ? el : [...el.querySelectorAll('svg')].find((s) => s.getBoundingClientRect().width > 1);
  if (svg) {
    const sr = svg.getBoundingClientRect();
    const scs = getComputedStyle(svg);
    out.icon = { w: +sr.width.toFixed(2), h: +sr.height.toFixed(2), fill: scs.fill, stroke: scs.stroke, color: scs.color, strokeWidth: scs.strokeWidth, classes: (svg.getAttribute('class') || '').slice(0, 80) };
  }
  // Design tokens: every var(--x) named in the classes of the element and the first painted or
  // texted nodes inside it, resolved on the element in the current theme.
  const names = new Set();
  for (const n of [el, ...el.querySelectorAll('*')].slice(0, 60)) for (const m of cls(n).matchAll(/var\((--[\w-]+)/g)) names.add(m[1]);
  if (names.size) {
    out.vars = {};
    const root = getComputedStyle(el);
    for (const n of [...names].sort()) out.vars[n] = noUrl(root.getPropertyValue(n).trim());
  }
  return out;
}

// ---------------------------------------------------------------- specs
//
// Each spec: key, group, title, desc, snap (the copy), find (a finder function), states, and
// optional `extra` states: { name: { snap?, find } } for another element or copy captured in that
// state (they are measured at rest, then with their own `states` if given). `pad` is the crop
// padding (8 by default); `crop: false` skips the crop.
const ALL = ['default', 'hover', 'focus-visible'];
const ALLP = ['default', 'hover', 'focus-visible', 'pressed'];
const HV = ['default', 'hover'];
const HF = ['default', 'hover', 'focus-visible'];
const R = ['default'];

// NotebookLM (adapt): one entry per checklist component this capture reached. Finders use roles,
// aria-labels, Angular Material and nb-* classes, and the product's own UI words, never account
// text (the copies' titles were scrubbed to "Sample ..." anyway). `snap` is the dark copy; the same
// copy is measured again in light (the body class swap in lib.mjs setLight).
const SPECS = [
  // Buttons
  { key: 'button-accent', group: 'Buttons', title: 'Accent button (New notebook)', desc: 'nb-button type accent: the one filled page action.', snap: 'home-dark', find: () => Q('nb-button.nb-button-type-accent button'), states: ALLP },
  { key: 'button-tonal', group: 'Buttons', title: 'Tonal button (Add sources)', desc: 'mat-tonal-button, full panel width.', snap: 'notebook-dark', find: () => Q('nb-button.add-source-button button'), states: ALLP },
  { key: 'button-text', group: 'Buttons', title: 'Text button (Create notebook, header)', snap: 'notebook-dark', find: () => Q('nb-button.create-notebook-button button'), states: ALLP },
  { key: 'button-outlined', group: 'Buttons', title: 'Outlined button (Upload files)', snap: 'notebook-dark-add-sources', find: () => Q('[role=dialog] button.source-action-button.mdc-button--outlined'), states: ALLP },
  { key: 'button-dialog-primary', group: 'Buttons', title: 'Dialog confirm button (Save, Configure Chat)', desc: 'Disabled while the Custom prompt is empty.', snap: 'notebook-dark-configure-chat', find: () => Q('[role=dialog] button.submit-button'), states: ALLP, extra: { disabled: { snap: 'notebook-dark-configure-chat-custom', find: () => Q('[role=dialog] button.submit-button') } } },
  { key: 'button-disabled', group: 'Buttons', title: 'Disabled filled button (Insert)', desc: 'Stays disabled while the URL field is empty or invalid.', snap: 'notebook-dark-website-dialog', find: () => Q('[role=dialog] button.mdc-button--unelevated'), states: R },
  { key: 'button-confirm-delete', group: 'Buttons', title: 'Delete confirmation buttons (Delete)', desc: 'The destructive action is a tonal button; it was never clicked.', snap: 'home-dark-delete-confirm', find: () => Q('[role=dialog] nb-button.yes-button button'), states: ALLP, extra: { cancel: { find: () => Q('[role=dialog] nb-button.no-button button'), states: ['hover', 'focus-visible'] } } },
  { key: 'icon-button', group: 'Buttons', title: 'Icon button (Settings, 36px)', snap: 'home-dark', find: () => Q('button[aria-label="Settings"]'), states: ALLP },
  { key: 'icon-button-small', group: 'Buttons', title: 'Icon button, small (card actions, 28px)', snap: 'home-dark', find: () => Q('project-button .project-button-more button'), states: ALLP },
  { key: 'search-pill', group: 'Buttons', title: 'Search pill (outlined button that opens search)', snap: 'home-dark', find: () => Q('nb-button.search-pill-button button'), states: ALLP },
  // Links
  { key: 'link', group: 'Links', title: 'Link (Learn more, Notifications dialog)', snap: 'home-dark-notifications-dialog', find: () => Q('[role=dialog] a.learn-more-link'), states: ALL },
  { key: 'link-inline', group: 'Links', title: 'Inline link in help text (learn more)', snap: 'notebook-dark-website-dialog', find: () => Q('[role=dialog] a.learn-more'), states: ALL },
  // Inputs
  { key: 'text-field', group: 'Inputs', title: 'Text field (Add people and groups)', snap: 'notebook-dark-share-dialog', find: () => C(Q('[role=dialog] input.mat-mdc-input-element'), 'mat-form-field'), fieldFocus: true, states: ALL },
  { key: 'search-field', group: 'Inputs', title: 'Search field (expanded header search)', snap: 'search-dark-empty', find: () => C(Q('input[aria-label="Search notebooks"]'), 'mat-form-field') || P(Q('input[aria-label="Search notebooks"]')), fieldFocus: true, states: ALL, extra: { typed: { snap: 'home-dark-search-typed', find: () => P(Q('input[placeholder]')) } } },
  { key: 'text-area', group: 'Inputs', title: 'Text area (chat composer)', desc: 'A cdk-autosize <textarea> inside the rounded composer.', snap: 'notebook-dark', find: () => P(Q('textarea.query-box-input')), focusOn: () => Q('textarea.query-box-input'), states: ALL, extra: { typed: { snap: 'notebook-dark-composer-typed', find: () => P(Q('textarea.query-box-input')) } } },
  { key: 'text-area-outlined', group: 'Inputs', title: 'Text area, outlined (Website URLs)', snap: 'notebook-dark-website-dialog', find: () => C(Q('[role=dialog] textarea'), 'mat-form-field'), fieldFocus: true, states: ALL, extra: { typed: { snap: 'notebook-dark-website-dialog-typed', find: () => C(Q('[role=dialog] textarea'), 'mat-form-field') }, error: { snap: 'notebook-dark-website-dialog-error', find: () => C(Q('[role=dialog] textarea'), 'mat-form-field') } } },
  { key: 'error-text', group: 'Inputs', title: 'Field error message', snap: 'notebook-dark-website-dialog-error', find: () => Q('[role=dialog] mat-error'), states: R, pad: 4 },
  { key: 'text-area-custom', group: 'Inputs', title: 'Text area with counter (Custom chat prompt)', snap: 'notebook-dark-configure-chat-custom', find: () => C(Q('[role=dialog] textarea.custom-input-textarea'), 'mat-form-field'), fieldFocus: true, states: ALL },
  { key: 'select', group: 'Inputs', title: 'Select (Notebook access)', snap: 'notebook-dark-share-dialog', find: () => C(Q('[role=dialog] mat-select.general-access-select-dropdown'), 'mat-form-field') || Q('[role=dialog] mat-select.general-access-select-dropdown'), fieldFocus: true, states: ALL, extra: { open: { snap: 'notebook-dark-share-select-open', prep: () => MOVESEL(), find: () => Q('.mat-mdc-select-panel') }, option: { snap: 'notebook-dark-share-select-open', prep: () => MOVESEL(), find: () => Q('.mat-mdc-select-panel mat-option', 1), states: ['hover'] }, 'option-selected': { snap: 'notebook-dark-share-select-open', prep: () => MOVESEL(), find: () => Q('.mat-mdc-select-panel mat-option.mdc-list-item--selected') } } },
  { key: 'menu-trigger', group: 'Inputs', title: 'Menu trigger (Web source type)', snap: 'notebook-dark', find: () => Q('nb-button.corpus-menu-trigger button'), states: ALLP },
  { key: 'checkbox', group: 'Inputs', title: 'Checkbox (source row, checked)', snap: 'notebook-dark', find: () => Q('mat-checkbox.select-checkbox'), focusOn: () => document.querySelector('mat-checkbox.select-checkbox input'), states: ALL, extra: { 'notify-checked': { snap: 'notebook-dark-share-dialog', find: () => Q('[role=dialog] mat-checkbox') } } },
  { key: 'radio', group: 'Inputs', title: 'Radio group drawn as toggle chips (Configure Chat)', desc: 'mat-button-toggle-group with role radiogroup; each chip is a role=radio button. The checked chip gains a leading check.', snap: 'notebook-dark-configure-chat', find: () => Q('[role=dialog] mat-button-toggle:not(.mat-button-toggle-checked) button'), states: ALLP, extra: { selected: { find: () => Q('[role=dialog] mat-button-toggle.mat-button-toggle-checked button') }, group: { find: () => Q('[role=dialog] mat-button-toggle-group') } } },
  { key: 'switch', group: 'Inputs', title: 'Switch (Web notifications, off and disabled)', desc: 'Disabled because the browser blocks notifications; no enabled switch appeared.', snap: 'home-dark-notifications-dialog', find: () => Q('[role=dialog] button[role=switch]'), states: HV },
  { key: 'progress', group: 'Inputs', title: 'Progress bar (source limit)', snap: 'notebook-dark-add-sources', find: () => Q('[role=dialog] mat-progress-bar'), states: R },
  // Navigation
  { key: 'tab', group: 'Navigation', title: 'Header tab (All, My notebooks, Discover, Collections)', desc: 'nb-buttons: the selected one is tonal, the rest text.', snap: 'home-dark', find: () => Q('nb-button.nb-button-type-text-primary button'), states: ALLP, extra: { selected: { find: () => Q('nb-button.nb-button-type-tonal button') } } },
  { key: 'segmented', group: 'Navigation', title: 'Segmented control (Grid view, List view)', snap: 'home-dark', find: () => Q('button.nb-segmented-button-action[aria-label="List view"]'), states: ALLP, extra: { selected: { find: () => Q('button.nb-segmented-button-action[aria-label="Grid view"]') }, group: { find: () => Q('nb-segmented-button-row') } } },
  { key: 'mobile-tab', group: 'Navigation', title: 'Panel tab at 390 (Sources, Chat, Studio)', snap: 'mobile-notebook-dark-chat', find: () => Q('button.tab-button:not(.tab-button--active)'), states: ['default', 'focus-visible', 'pressed'], extra: { selected: { find: () => Q('button.tab-button--active') }, bar: { find: () => P(Q('button.tab-button')) } } },
  // Overlays
  { key: 'menu', group: 'Overlays', title: 'Menu (notebook card actions)', snap: 'home-dark-card-menu', find: () => Q('.mat-mdc-menu-panel'), states: R, extra: { item: { find: () => Q('.mat-mdc-menu-panel [role=menuitem]', 1), states: ['hover', 'focus-visible', 'pressed'] } } },
  { key: 'menu-settings', group: 'Overlays', title: 'Menu (Settings) and its Theme submenu', snap: 'home-dark-settings-menu', find: () => Q('.mat-mdc-menu-panel'), states: R, extra: { submenu: { snap: 'home-dark-theme-submenu', find: () => [...document.querySelectorAll('.mat-mdc-menu-panel')].pop() } } },
  { key: 'tooltip', group: 'Overlays', title: 'Tooltip', desc: 'Its text was scrubbed, since tooltips repeat titles; the live one read "Audio Overview - Generate an AI podcast based on your sources".', snap: 'notebook-dark-tooltip', find: () => Q('.mat-mdc-tooltip-surface'), states: R },
  { key: 'dialog', group: 'Overlays', title: 'Dialog (Delete this notebook?)', snap: 'home-dark-delete-confirm', find: () => Q('.mat-mdc-dialog-surface'), states: R },
  { key: 'dialog-large', group: 'Overlays', title: 'Dialog, large (Configure Chat)', snap: 'notebook-dark-configure-chat', find: () => Q('.mat-mdc-dialog-surface'), states: R, crop: false },
  { key: 'dialog-announcement', group: 'Overlays', title: 'Announcement dialog (what is new)', snap: 'notebook-dark-announcement', find: () => Q('.mat-mdc-dialog-surface'), states: R, crop: false },
  { key: 'scrim', group: 'Overlays', title: 'Dialog scrim', snap: 'home-dark-delete-confirm', find: () => Q('.cdk-overlay-dark-backdrop'), states: R, crop: false },
  { key: 'toast', group: 'Overlays', title: 'Toast (Failed to copy.)', desc: 'The clipboard is blocked in the capture browser, so the copy action reported a failure.', snap: 'notebook-dark-toast', find: () => Q('mat-snack-bar-container .mdc-snackbar__surface') || Q('mat-snack-bar-container'), states: R },
  // Lists and tables
  { key: 'card', group: 'Lists', title: 'Notebook card', snap: 'home-dark', find: () => Q('project-button mat-card'), focusOn: () => Q('project-button a.primary-action-button'), states: ALLP },
  { key: 'studio-tile', group: 'Lists', title: 'Studio tile (Audio Overview)', snap: 'notebook-dark', find: () => Q('[aria-label="Audio Overview"]'), states: ALLP },
  { key: 'list-row', group: 'Lists', title: 'List row (source)', snap: 'notebook-dark', find: () => C(Q('button.source-stretched-button'), '.single-source-container') || Q('button.source-stretched-button'), focusOn: () => Q('button.source-stretched-button'), states: ALLP },
  { key: 'list-row-output', group: 'Lists', title: 'List row (Studio output)', snap: 'notebook-dark', find: () => Q('.artifact-item-button'), states: ALLP },
  { key: 'table-row', group: 'Tables', title: 'Table row (notebook list view)', snap: 'home-dark-list', find: () => Q('tbody tr.mat-mdc-row'), states: HV },
  { key: 'table-header', group: 'Tables', title: 'Table header row', snap: 'home-dark-list', find: () => Q('thead tr'), states: R },
  { key: 'mobile-list-row', group: 'Tables', title: 'Notebook row at 390', snap: 'mobile-home-dark', find: () => Q('tbody tr.mat-mdc-row'), states: R },
  { key: 'chat-bubble', group: 'Lists', title: 'User chat bubble', snap: 'notebook-dark', find: () => P(Q('.from-user-message-inner-content')) || Q('.from-user-message-inner-content'), states: R },
  { key: 'citation', group: 'Lists', title: 'Citation marker', snap: 'notebook-dark', find: () => Q('button.citation-marker'), states: ALLP, pad: 4 },
  // Display
  { key: 'avatar', group: 'Display', title: 'Avatar (account, 32px)', desc: 'The photo was replaced by a grey disc with an L in the copy; size and shape are the product\'s, the fill is not.', snap: 'home-dark', find: () => Q('a[aria-label^="Google Account"]'), states: R, crop: false },
  { key: 'badge-pro', group: 'Display', title: 'Badge (PRO)', snap: 'home-dark', find: () => Q('.pro-badge'), states: R, pad: 4 },
  { key: 'badge-new', group: 'Display', title: 'Badge (New! on a Studio tile)', snap: 'notebook-dark', find: () => P(T('New!')), states: R, pad: 4 },
  { key: 'status-chip', group: 'Display', title: 'Status chip (Blocked by browser)', snap: 'home-dark-notifications-dialog', find: () => P(T('Blocked by browser')) || T('Blocked by browser'), states: R, pad: 4 },
  { key: 'banner', group: 'Display', title: 'Inline banner (Studio, Try it)', snap: 'notebook-dark', find: () => Q('.artifact-callout') || P(TS('New: You can now')), states: R },
  { key: 'skeleton', group: 'Display', title: 'Loading skeleton row', snap: 'search-dark-loading', find: () => Q('.skeleton-row'), states: R },
  { key: 'empty-state', group: 'Display', title: 'Empty state (No notebooks found)', snap: 'search-dark-empty', find: () => P(Q('h2.no-results-heading')) || Q('h2.no-results-heading'), states: R, extra: { action: { find: () => Q('button.no-results-clear-button'), states: ['hover', 'focus-visible'] } } },
  // Shell
  { key: 'header', group: 'Shell', title: 'Page header (home)', snap: 'home-dark', find: () => Q('page-header') || Q('header'), states: R, crop: false },
  { key: 'panel-sources', group: 'Shell', title: 'Sources panel', snap: 'notebook-dark', find: () => Q('section.source-panel'), states: R, crop: false },
  { key: 'panel-chat', group: 'Shell', title: 'Chat panel', snap: 'notebook-dark', find: () => Q('section.chat-panel'), states: R, crop: false },
  { key: 'panel-studio', group: 'Shell', title: 'Studio panel', snap: 'notebook-dark', find: () => Q('section.studio-panel'), states: R, crop: false },
  // Type
  { key: 'type-page-title', group: 'Type', title: 'Page title (My notebooks)', snap: 'home-dark', find: () => Q('h2.projects-header'), states: R, crop: false },
  { key: 'type-cover-title', group: 'Type', title: 'Notebook cover title', snap: 'notebook-dark', find: () => Q('h2.cover-title'), states: R, crop: false },
  { key: 'type-panel-header', group: 'Type', title: 'Panel header (Sources)', snap: 'notebook-dark', find: () => Q('.panel-header h2') || Q('h2.panel-header-content'), states: R, crop: false },
  { key: 'type-dialog-title', group: 'Type', title: 'Dialog title', snap: 'home-dark-delete-confirm', find: () => Q('[role=dialog] h2'), states: R, crop: false },
  { key: 'type-heading', group: 'Type', title: 'Answer heading', snap: 'notebook-dark', find: () => Q('.paragraph.heading3') || Q('.paragraph[class*=heading]'), states: R, crop: false },
  { key: 'type-body', group: 'Type', title: 'Answer body paragraph', snap: 'notebook-dark', find: () => Q('labs-tailwind-structural-element-view-v2 .paragraph.normal') || Q('labs-tailwind-structural-element-view-v2 .paragraph'), states: R, crop: false },
  { key: 'type-caption', group: 'Type', title: 'Card meta line (date, source count)', snap: 'home-dark', find: () => Q('.project-button-subtitle-part'), states: R, crop: false },
  { key: 'type-code', group: 'Type', title: 'Inline code', snap: 'notebook-dark', find: () => Q('code.code'), states: R, crop: false },
  { key: 'type-disclaimer', group: 'Type', title: 'Composer footnote', snap: 'notebook-dark', find: () => Q('.disclaimer'), states: R, crop: false },
];

// ---------------------------------------------------------------- jobs

function jobsFor(spec) {
  const out = [];
  for (const st of spec.states) out.push({ state: st, base: st, snap: spec.snap, find: spec.find, hoverOn: spec.hoverOn, focusOn: spec.focusOn, prep: spec.prep });
  for (const [name, v] of Object.entries(spec.extra || {})) {
    out.push({ state: name, base: 'default', snap: v.snap || spec.snap, find: v.find, variant: true, prep: v.prep });
    for (const st of v.states || []) out.push({ state: `${name}-${st}`, base: st, snap: v.snap || spec.snap, find: v.find, variant: true, prep: v.prep });
  }
  return out;
}

const MOBILE = (label) => label.startsWith('mobile-');

// NotebookLM (adapt): `<copy>#light` is the dark copy opened in light.
const LIGHT = (label) => label.endsWith('#light');
const fileOf = (label) => label.replace(/#light$/, '');

async function measureSnap(browser, label, specs, out) {
  const meta = metaOf(fileOf(label));
  const ctx = await newContext(browser, meta, LIGHT(label));
  await ctx.addInitScript(HELPERS);
  let page;
  try {
    page = await openSnap(ctx, fileOf(label), { light: LIGHT(label) });
  } catch (e) {
    log('  ! open failed', label, e.message.split('\n')[0]);
    await ctx.close();
    return false;
  }
  const rest = { x: meta.w - 2, y: Math.round(meta.h / 2) };
  await page.evaluate(() => window.__saveScroll());
  const resetPage = async () => {
    await page.evaluate(() => { if (document.activeElement && document.activeElement.blur) document.activeElement.blur(); });
    await page.mouse.move(rest.x, rest.y);
    await page.evaluate(() => { window.__restoreScroll(); window.__freeze(); });
    await page.waitForTimeout(200);
  };
  const tag = async (fn, name) => {
    if (!fn) return null;
    const h = await page.evaluateHandle(`(() => { try { return (${fn.toString()})(); } catch (e) { return null; } })()`);
    const el = h.asElement();
    if (!el) return null;
    await el.evaluate((e, n) => e.setAttribute(`data-mt-${n}`, ''), name);
    return page.locator(`[data-mt-${name}]`).first();
  };
  const untag = () => page.evaluate(() => document.querySelectorAll('*').forEach((n) => { for (const a of [...n.attributes]) if (a.name.startsWith('data-mt-')) n.removeAttribute(a.name); }));
  const ensureVisible = (loc) => loc.evaluate((el) => {
    const r = el.getBoundingClientRect();
    if (r.top < 0 || r.bottom > innerHeight || r.left < 0 || r.right > innerWidth) el.scrollIntoView({ block: r.height > innerHeight ? 'start' : 'center', inline: 'nearest', behavior: 'instant' });
  });
  const pointOf = (loc) => loc.evaluate((el) => {
    const r = [...el.getClientRects()].find((x) => x.width > 0 && x.height > 0) || el.getBoundingClientRect();
    return { x: r.x + Math.min(r.width / 2, 40), y: r.y + Math.min(r.height / 2, 20) };
  });
  const kbFocus = async (loc) => {
    const ok0 = await loc.evaluate((el) => window.__isFocusable(el));
    if (!ok0) return { ok: false, how: 'not focusable in the static copy (no tabindex)' };
    await loc.evaluate((el) => el.focus());
    await page.keyboard.press('Shift+Tab');
    await page.keyboard.press('Tab');
    let ok = await loc.evaluate((el) => document.activeElement === el);
    let how = 'keyboard: focus(), Shift+Tab, Tab';
    if (!ok) {
      await page.keyboard.press('Shift');
      await loc.evaluate((el) => el.focus());
      ok = await loc.evaluate((el) => document.activeElement === el);
      how = 'keyboard: Shift keydown, then focus()';
    }
    await page.waitForTimeout(350);
    return { ok, how, matches: await loc.evaluate((el) => el.matches(':focus-visible')) };
  };
  const crop = async (loc, name, pad) => {
    const vp = page.viewportSize();
    const box = await loc.boundingBox();
    if (!box) throw new Error('no box');
    const clip = { x: Math.max(0, box.x - pad), y: Math.max(0, box.y - pad) };
    clip.width = Math.min(vp.width, box.x + box.width + pad) - clip.x;
    clip.height = Math.min(vp.height, box.y + box.height + pad) - clip.y;
    if (clip.width < 1 || clip.height < 1) throw new Error('off screen');
    const file = path.join(CROPS, `${name}.png`);
    await page.screenshot({ path: file, clip, animations: 'allow' });
    execFileSync('python3', ['-c', 'import sys\nfrom PIL import Image\nf=sys.argv[1]\nim=Image.open(f).convert("RGB")\nif im.width>1600: im=im.resize((im.width//2, im.height//2), Image.LANCZOS)\nim.quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(f, optimize=True)', file]);
    return path.relative(REF, file);
  };

  const theme = LIGHT(label) ? 'light' : 'dark';
  {
    for (const { spec, job } of specs) {
      const state = theme === 'dark' ? job.state : job.state === 'default' ? 'light' : `light-${job.state}`;
      const c = out.components[spec.key];
      const name = `${spec.key}-${state}`;
      if (MOBILE(label) && job.base === 'hover') continue;
      try {
        await resetPage();
        if (job.prep) { await page.evaluate(`(${job.prep.toString()})()`); await page.waitForTimeout(250); }
        const loc = await tag(job.find, 'el');
        if (!loc) throw new Error('element not found');
        // NotebookLM (adapt): Material outlined fields show focus through classes Angular's focus
        // monitor sets (mat-focused, mdc-text-field--focused), which a static copy keeps from the
        // moment it was taken and no script clears or sets. For a field spec's own states, every
        // copied focus class is cleared at rest and on hover, and set on the measured field after
        // real keyboard focus, as the focus monitor would. Variant copies (typed, error) keep the
        // classes they were captured with.
        if (spec.fieldFocus && !job.variant) {
          await loc.evaluate((el, on) => {
            for (const f of document.querySelectorAll('mat-form-field')) {
              const mine = on && (f.contains(el) || el.contains(f) || f === el);
              f.classList.toggle('mat-focused', mine);
              f.querySelectorAll('.mdc-text-field').forEach((t) => t.classList.toggle('mdc-text-field--focused', mine));
            }
          }, job.base === 'focus-visible');
          // The label and outline animate between focused and resting colours; read after they settle.
          await page.waitForTimeout(400);
        }
        await ensureVisible(loc);
        let via = job.variant && job.base === 'default' ? `at rest, captured ${job.state}` : 'at rest';
        let focus;
        if (job.base === 'hover') {
          const hl = (job.hoverOn && (await tag(job.hoverOn, 'hv'))) || loc;
          const p = await pointOf(hl);
          await page.mouse.move(p.x, p.y, { steps: 4 });
          // A second, sub-pixel move: an element revealed by group-hover only takes :hover itself
          // once the pointer moves again.
          await page.waitForTimeout(80);
          await page.mouse.move(p.x + 0.5, p.y);
          await page.waitForTimeout(450);
          via = job.hoverOn ? 'mouse hover on its row' : 'mouse hover';
        } else if (job.base === 'pressed') {
          const p = await pointOf(loc);
          await page.mouse.move(p.x, p.y, { steps: 4 });
          await page.waitForTimeout(80);
          await page.mouse.move(p.x + 0.5, p.y);
          await page.mouse.down();
          await page.waitForTimeout(250);
          via = 'mouse hover, then held down';
        } else if (job.base === 'focus-visible') {
          let fl = job.focusOn ? await tag(job.focusOn, 'fo') : null;
          if (!fl) {
            const h = await loc.evaluateHandle((el) => window.__focusTarget(el));
            if (h.asElement()) { await h.asElement().evaluate((e) => e.setAttribute('data-mt-fo', '')); fl = page.locator('[data-mt-fo]').first(); }
          }
          focus = fl ? await kbFocus(fl) : { ok: false, how: 'not focusable in the static copy (no tabindex)' };
          if (!focus.ok) { c.states[state] = { theme, snapshot: label, skipped: focus.how }; log('  -', name, 'skipped:', focus.how); continue; }
          via = focus.how + (fl && !(await fl.evaluate((e) => e.hasAttribute('data-mt-el'))) ? ' (on the field inside)' : '');
        }
        const s = await loc.evaluate(styleOf, PROPS);
        if (focus) s.focus = focus;
        // Is something else painted over the element's centre? (Then its crop shows that instead.)
        const hit = await loc.evaluate((el) => {
          const r = el.getBoundingClientRect();
          const x = Math.min(Math.max(r.x + r.width / 2, 1), innerWidth - 1);
          const y = Math.min(Math.max(r.y + r.height / 2, 1), innerHeight - 1);
          const h = document.elementFromPoint(x, y);
          if (!h || el.contains(h) || h.contains(el)) return null;
          return h.tagName.toLowerCase() + '.' + String(h.className).split(/\s+/).slice(0, 3).join('.');
        });
        if (hit) { s.occludedBy = hit.slice(0, 120); log('  ?', name, 'centre covered by', hit.slice(0, 80)); }
        if (spec.crop !== false) {
          try { s.crop = await crop(loc, name, spec.pad ?? 8); } catch (e) { s.cropError = String(e.message || e).slice(0, 120); }
        }
        c.states[state] = { theme, snapshot: label, ...s, via, read: RUN };
        out._meta.read = RUN; // a reading succeeded in this run
        if (job.find !== spec.find) (c.selectors ||= {})[state] = job.find.toString();
        log('  ', name, `${s.rect.w}x${s.rect.h}`, via.slice(0, 50));
      } catch (e) {
        // A state that fails on a rerun keeps the reading an earlier run took and says it failed now,
        // instead of replacing a good reading with an error.
        const prev = (earlier.get(spec.key) || {})[state];
        const error = String(e.message || e).slice(0, 200);
        c.states[state] = prev && !prev.error ? { ...prev, recaptureError: error, recaptureRun: RUN } : { theme, snapshot: label, error, read: RUN };
        log('  !', name, String(e.message || e).slice(0, 120));
      } finally {
        await page.mouse.up().catch(() => {});
        await page.mouse.move(rest.x, rest.y).catch(() => {});
        await untag().catch(() => {});
      }
    }
  }
  await ctx.close();
  return true;
}

// ---------------------------------------------------------------- main

const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
// _meta.read keeps the earlier date until this run reads a state, so a rerun that
// fails throughout never redates old readings; _meta.lastAttempt is this run's
// date. Each state carries its own `read` date; states kept from before per-state
// dates existed take the earlier _meta.read.
const RUN = new Date().toLocaleDateString('en-CA');
const PRIOR_READ = out._meta && out._meta.read;
for (const c of Object.values(out.components || {})) {
  for (const st of Object.values((c && c.states) || {})) if (st && typeof st === 'object' && !st.read && PRIOR_READ) st.read = PRIOR_READ;
}
// NotebookLM (adapt): every dark copy is measured again in light, from the same file.
const hasCopy = (label) => fs.existsSync(path.join(SNAPS, `${label.replace(/#light$/, '')}.json`));
const copiesOf = (snap) => [snap, ...(/-dark(?=-|$)/.test(snap) ? [snap + '#light'] : [])];
const labels = [...new Set(SPECS.flatMap((s) => jobsFor(s).flatMap((j) => copiesOf(j.snap))))].filter((l) => hasCopy(l) && (!ONLY.length || ONLY.includes(l.replace(/#light$/, ''))));
out._meta = {
  read: PRIOR_READ || RUN,   // moves to this run's date once a state is read
  lastAttempt: RUN,
  source: 'Static, redacted copies of the signed-in notebook.google.com web app (tools/capture/signed-in/snapshot.js) with every same-origin stylesheet inlined, loaded from file:// in headless Chromium; Google Fonts and gstatic come through a local cache. Nothing was requested from notebook.google.com itself.',
  viewport: '1440x900 (the mobile-* copies 390x844), deviceScaleFactor 2',
  themes: 'Every copy was taken in dark. Light is the same copy with the body class dark-theme swapped for light-theme, which is what the in-app Light mode does. Dark states have plain names; light states are `light`, `light-<state>`. Every state records `theme` and `snapshot`.',
  states: {
    default: 'at rest, as captured',
    hover: 'real mouse hover (page.mouse.move), 450ms settle; not measured on the 390 copies',
    'focus-visible': 'real keyboard focus (focus, Shift+Tab, Tab) on the element or its first focusable descendant; recorded as skipped where the element cannot take focus',
    pressed: 'mouse hover, then the button held down for 250ms (:active)',
    other: 'selected / open / readonly / off / option-highlighted are other elements or copies captured in that state',
  },
  tokens: '`vars` lists every var(--x) named in the classes of the element and its first descendants (NotebookLM\'s classes name none, so this is usually empty; the theme variables are read by tools/capture/read-css.mjs).',
  // Entries kept from an earlier run go through safeUrl again, so a partial rerun never writes an
  // older copy's full URL back.
  snapshots: { ...Object.fromEntries(Object.entries((out._meta && out._meta.snapshots) || {}).map(([l, v]) => [l, { ...v, url: v.url && safeUrl(v.url) }])), ...Object.fromEntries(labels.filter((l) => !l.endsWith('#light')).map((l) => { const m = metaOf(l); return [l, { url: safeUrl(m.url), w: m.w, h: m.h }]; })) },
};
out.components ??= {};
fs.mkdirSync(CROPS, { recursive: true });

// Build the per-snapshot job lists. The states a copy re-measures are cleared only once that copy has
// opened (see the worker below), so a copy that fails to open keeps its earlier readings (finding
// 12-10; the kit's signed-in measure.mjs does the same).
const bySnap = new Map();
for (const spec of SPECS) {
  const c = (out.components[spec.key] ??= { states: {} });
  Object.assign(c, { group: spec.group, title: spec.title, desc: spec.desc, page: spec.snap, selector: spec.find.toString() });
  const jobs = jobsFor(spec);
  c.pages = [...new Set(jobs.map((j) => j.snap))];
  for (const job of jobs) {
    for (const copy of copiesOf(job.snap)) {
      if (!labels.includes(copy)) continue;
      if (!bySnap.has(copy)) bySnap.set(copy, []);
      bySnap.get(copy).push({ spec, job });
    }
  }
}

const browser = await chromium.launch();
const queue = [...bySnap.keys()].sort();
// Earlier readings of the states a copy in flight is re-measuring, by component. save() writes them
// wherever no new reading exists yet, so while workers run, the file on disk never loses one.
const earlier = new Map();
const stateOf = (copy, job) => (LIGHT(copy) ? (job.state === 'default' ? 'light' : `light-${job.state}`) : job.state);
const save = () => {
  // Stable order: components in SPECS order, states in the order the spec lists them, dark then light.
  const comps = {};
  for (const spec of SPECS) {
    const c = out.components[spec.key];
    const names = jobsFor(spec).map((j) => j.state);
    const ordered = {};
    const prev = earlier.get(spec.key) || {};
    const pick = (n) => c.states[n] || prev[n];
    for (const n of names) if (pick(n)) ordered[n] = pick(n);
    for (const n of names) { const l = n === 'default' ? 'light' : `light-${n}`; if (pick(l)) ordered[l] = pick(l); }
    comps[spec.key] = { ...c, states: ordered };
  }
  fs.writeFileSync(OUT, JSON.stringify({ _meta: out._meta, components: comps }, null, 1) + '\n');
};
await Promise.all(Array.from({ length: Math.min(CONC, queue.length) }, async () => {
  while (queue.length) {
    const label = queue.shift();
    log('open', label, `(${bySnap.get(label).length} jobs x 2 themes)`);
    // This copy's earlier readings move to `earlier` for the run: replaced once the copy opened and
    // was measured, put back if it never opened, the run threw, or the state was skipped (hover on a
    // 390 copy).
    const jobs = bySnap.get(label), kept = [];
    for (const { spec, job } of jobs) {
      const st = out.components[spec.key].states, n = stateOf(label, job);
      if (!(n in st)) continue;
      if (!earlier.has(spec.key)) earlier.set(spec.key, {});
      earlier.get(spec.key)[n] = st[n];
      kept.push([spec.key, n]);
      delete st[n];
    }
    let opened = false;
    try {
      opened = await measureSnap(browser, label, jobs, out);
    } catch (e) {
      log('  ! measuring failed', label, String(e.message || e).split('\n')[0]);
    }
    for (const [key, n] of kept) {
      out.components[key].states[n] ??= earlier.get(key)[n];
      delete earlier.get(key)[n];
    }
    save();
  }
}));
await browser.close();
save();
const all = SPECS.map((sp) => out.components[sp.key]);
const states = all.flatMap((c) => Object.values(c.states));
log(`${all.length} components, ${states.length} states (${states.filter((s) => s.error).length} errors, ${states.filter((s) => s.skipped).length} skipped, ${states.filter((s) => s.recaptureError).length} kept from an earlier run because this rerun failed)`);
