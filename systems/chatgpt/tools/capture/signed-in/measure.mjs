// Measures ChatGPT's signed-in components from the static page copies (see render.mjs, unsnap.py),
// in both themes and in every state CSS can reach once scripts are gone.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs SNAPS=<dir of page copies> [READ_DATE=YYYY-MM-DD] node tools/capture/signed-in/measure.mjs [label ...] [--jobs N]
//
// With labels, only the components (and states) that live on those copies are re-measured and
// merged into the existing JSON. Writes raw/components-computed.json and one crop per component
// and state into components/crops/<component>-<state>.png (2x, 256 colours, halved when wider than
// 1600px). raw/measurements.md is then built from the JSON by build-measurements.mjs.
//
// Themes: since the 2026-10 redesign ChatGPT paints its palettes from `data-theme` on <html>
// (`.chatgpt-theme[data-theme="dark"|"light"]`), so each copy (captured in dark) is measured once as
// captured and once with every data-theme="dark" set to light, which is what render.mjs does for
// the light screenshots. Dark states keep their plain names
// (`default`, `hover`, ...); light states are `light`, `light-hover`, `light-focus-visible`, ...
// and every state records `theme`.
//
// States:
//   default        at rest, as captured
//   hover          real mouse hover (page.mouse.move), 450ms settle; Tailwind's hover: variants
//                  are plain CSS, so they apply on the static copy
//   focus-visible  real keyboard focus: focus(), Shift+Tab, Tab (or a Shift keydown then focus()),
//                  on the element or its first focusable descendant; ChatGPT draws most focus
//                  rings from `keyboard-focused:` variants that its script switches on, so many
//                  record the plain :focus-visible look only
//   pressed        the mouse button held down on the element for 300ms (:active), then released
//   anything else  another element, or another copy, captured in that state: `active` (the
//                  current page or chat), `selected`, `checked`, `open`, `typed`, ...
// No click is dispatched anywhere; the copies have no scripts and every request off the asset
// hosts is refused (lib.mjs).
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { chromium, REF, RAW, CROPS, SNAPS, SCROLL, metaOf, newContext, openSnap, toLight } from './lib.mjs';
import { safeUrl } from '../safe-url.mjs';
// An activated .venv without Pillow resolves python3 to itself: set PYTHON to a python3 that has it.
const PYTHON = process.env.PYTHON || 'python3';

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
//   D()               the last visible [role=dialog];  M() main#main;  S() the sidebar
//   PW(el, w)         el's first painted ancestor at least `w` px wide (a popover or dialog panel)
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
    M: () => document.querySelector('main'),
    // The expanded sidebar (the phone drawer on the 390 copies) and the tiny rail behind it.
    S: () => [...document.querySelectorAll('aside[class*="LeftPanel"]')].find((e) => e.getBoundingClientRect().width > 1) || null,
    // el's first ancestor at least `w` wide that paints a fill, border or shadow (a popover panel).
    PW: (el, w) => { for (let n = el; n && n !== document.documentElement; n = n.parentElement) if (n.getBoundingClientRect().width >= w - 0.5 && paints(n)) return n; return null; },
    // The visible button, link or [role=button] whose text (innerText, aria-label or textContent)
    // is exactly `text`; QA(sel, i) the i-th match of a selector, visible or not (hover-only controls).
    B: (text, root = document) => [...root.querySelectorAll('button, a, [role=button], [role=tab], [role=menuitem]')].find((e) => vis(e) && [e.innerText, e.getAttribute('aria-label'), e.textContent].some((t) => (t || '').trim() === text)) || null,
    QA: (sel, i = 0, root = document) => root.querySelectorAll(sel)[i] || null,
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
      // A scroll-driven animation (the signed-out page's panels) follows the scroll position, not
      // time; finishing it would jump it to the fully scrolled state and move the layout.
      if (!(a.timeline instanceof DocumentTimeline)) continue;
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
  // A url() in a computed value can be a signed URL: recorded as url(…), only data: and #fragment
  // references kept (the kit's noUrl).
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
  for (const a of ['role', 'aria-label', 'data-state', 'data-active', 'aria-checked', 'aria-selected', 'aria-expanded', 'aria-disabled', 'disabled', 'data-color', 'data-variant', 'data-size', 'data-context-menu']) if (el.hasAttribute(a)) (out.attrs ||= {})[a] = el.getAttribute(a);
  for (const pe of ['::before', '::after']) {
    const p = getComputedStyle(el, pe);
    if (p.content && p.content !== 'none' && p.content !== 'normal') {
      out[pe] = { content: noUrl(p.content).slice(0, 40), width: p.width, height: p.height, position: p.position, backgroundColor: p.backgroundColor, backgroundImage: noUrl(p.backgroundImage).slice(0, 200), boxShadow: p.boxShadow, borderTopWidth: p.borderTopWidth, borderTopStyle: p.borderTopStyle, borderTopColor: p.borderTopColor, borderRadius: p.borderRadius, inset: `${p.top} ${p.right} ${p.bottom} ${p.left}`, opacity: p.opacity, transform: p.transform, transition: p.transition };
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
  // The stacking: the element's own z-index, else the nearest positioned ancestors that set one.
  const za = [];
  for (let n = el; n && n !== document.documentElement && za.length < 3; n = n.parentElement) {
    const c = getComputedStyle(n);
    if (c.zIndex !== 'auto' && c.position !== 'static') za.push({ node: short(n), z: +c.zIndex, position: c.position });
  }
  if (za.length) out.zAncestors = za;
  const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, { acceptNode: (t) => (t.textContent.trim() && t.parentElement && t.parentElement.getBoundingClientRect().width > 1 && getComputedStyle(t.parentElement).visibility === 'visible' ? 1 : 3) });
  const tn = walker.nextNode();
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
  // ChatGPT names its tokens three ways in a class: `bg-token-text-primary` (Tailwind theme keys
  // that read `--text-primary`), `bg-(--sidebar-surface-primary)` and `[var(--x)]`; the inline
  // `--menu-item-*` variables a row sets are read too.
  for (const n of [el, ...el.querySelectorAll('*')].slice(0, 60)) {
    const c = cls(n);
    for (const m of c.matchAll(/var\((--[\w-]+)/g)) names.add(m[1]);
    for (const m of c.matchAll(/\((--[\w-]+)\)/g)) names.add(m[1]);
    for (const m of c.matchAll(/(?:^|[\s:!])[a-z-]*?-?token-([a-z0-9-]+?)(?:\/\d+)?(?=\s|$|!)/g)) names.add('--' + m[1]);
    const st = n.getAttribute && n.getAttribute('style');
    if (st) for (const m of st.matchAll(/(--[\w-]+)\s*:/g)) names.add(m[1]);
  }
  if (names.size) {
    out.vars = {};
    const root = getComputedStyle(el);
    for (const n of [...names].sort()) { const v = root.getPropertyValue(n).trim(); if (v) out.vars[n] = noUrl(v); }
    if (!Object.keys(out.vars).length) delete out.vars;
  }
  return out;
}

// ---------------------------------------------------------------- specs
//
// Each spec: key, group, title, desc, snap (the snapshot), find (a finder function), states, and
// optional `extra` states: { name: { snap?, find } } for another element or snapshot captured in
// that state (they are measured at rest, then with their own `states` if given). `pad` is the crop
// padding (8 by default); `crop: false` skips the crop.
const ALL = ['default', 'hover', 'focus-visible'];
const ALLP = ['default', 'hover', 'focus-visible', 'pressed'];
const HV = ['default', 'hover'];
const R = ['default'];

// Captured 2026-10-17 from the redesigned shell: components are CSS-module classes (`Button-*`,
// `itemBase-*`, `Table-*`, `Badge-*`) with data-color / data-variant / data-size attributes, the
// sidebar is `aside[class*=LeftPanel]` and the page header `[data-testid=app-shell-head]`.
const SPECS = [
  // ---------------- Sidebar
  { key: 'sidebar', group: 'Sidebar', title: 'Sidebar (expanded)', snap: 'home-dark', find: () => S(), states: R, pad: 0, desc: '`aside.LeftPanel`, 340 wide at 1440 (`--spacing-token-sidebar`, clamp(240px, 340px, ...)); header row, nav rows, then the Pinned, Projects and Recents sections and the account row.' },
  { key: 'sidebar-icon-button', group: 'Sidebar', title: 'Icon button (sidebar Search)', snap: 'home-dark', find: () => Q('button[aria-label="Search"]', 0, S()), states: ALLP, desc: '`Button` with data-color=secondary, data-variant=ghost, data-size=xl: 36x36.' },
  {
    key: 'nav-row', group: 'Sidebar', title: 'Nav row (Images)', snap: 'home-dark', find: () => Q('button[data-sidebar-destination="builtin:images"]', 0, S()), states: ALLP,
    desc: 'A 36 tall row with a 20px icon and 14px label. The current destination is filled (`active`).',
    extra: { active: { find: () => C(T('New chat', S()), 'button') }, 'active-library': { snap: 'library-dark', find: () => Q('button[data-sidebar-destination="builtin:library"]', 0, S()) } },
  },
  { key: 'section-toggle', group: 'Sidebar', title: 'Section header (Pinned)', snap: 'home-dark', find: () => Q('button[data-app-action-sidebar-section-toggle]', 0, S()), states: ALL, desc: 'Collapsible section label in tertiary text.' },
  {
    key: 'chat-row', group: 'Sidebar', title: 'List row (sidebar chat)', snap: 'home-dark', find: () => H(Q('a[data-interactive-row-link]', 2, S()), 30), hoverOn: () => Q('a[data-interactive-row-link]', 2, S()), states: ['default', 'hover'],
    desc: 'A chat in Recents: 36 tall, full radius (`--radius-token-row`), the title truncated; hover fills it and shows Chat actions and Pin. The open chat is filled (`active`).',
    extra: { active: { snap: 'thread-dark-code', find: () => P(QA('a[aria-current=page]', 0, S())) } },
  },
  { key: 'chat-row-link', group: 'Sidebar', title: 'Chat row link (keyboard focus)', snap: 'home-dark', find: () => Q('a[data-interactive-row-link]', 2, S()), states: ['focus-visible'], desc: 'The row\'s own link, focused from the keyboard.' },
  { key: 'chat-row-actions', group: 'Sidebar', title: 'Chat actions button', snap: 'home-dark', find: () => QA('button[aria-label="Chat actions"]', 2, S()), hoverOn: () => Q('a[data-interactive-row-link]', 2, S()), states: ['hover'], desc: 'A 20x20 `Button` (size 3xs, transparent, pill), shown when its row is hovered; measured while the row is hovered.' },
  { key: 'project-row', group: 'Sidebar', title: 'Project row', snap: 'home-dark', find: () => Q('[data-app-action-sidebar-project-row]', 0, S()), states: ALL, desc: 'Each project with its own icon; hover reveals project actions and a new-chat button.' },
  { key: 'account-row', group: 'Sidebar', title: 'Account row', snap: 'home-dark', find: () => Q('button[aria-label="Open profile menu"]', 0, S()), states: ALLP, desc: '`Button` primary ghost size 4xl: the 24px avatar, the name over the plan.', extra: { open: { snap: 'home-dark-user-menu', find: () => Q('button[aria-label="Open profile menu"]', 0, S()) } } },
  { key: 'avatar', group: 'Sidebar', title: 'Avatar', snap: 'home-dark', find: () => Q('button[aria-label="Open profile menu"] .rounded-full', 0, S()), states: R, desc: 'Redacted to a grey disc with an L; the real one is the account photo at 24px.' },
  { key: 'sidebar-upgrade', group: 'Sidebar', title: 'Outline pill button (account Upgrade)', snap: 'home-dark', find: () => C(T('Upgrade', S()), 'button'), states: ALLP },
  { key: 'sidebar-rail', group: 'Sidebar', title: 'Sidebar collapsed to the rail', snap: 'home-dark-sidebar-collapsed', find: () => S(), states: R, pad: 0, desc: '52 wide: show sidebar, new chat, search, pinned, recents, library, then the avatar.' },
  { key: 'rail-button', group: 'Sidebar', title: 'Rail button (New chat)', snap: 'home-dark-sidebar-collapsed', find: () => C(T('New chat', S()), 'button') || Q('button[data-sidebar-cycle-item]', 0, S()), states: ALL },

  // ---------------- Top bar
  { key: 'page-header', group: 'Top bar', title: 'Page header', snap: 'home-dark', find: () => QA('[data-testid=app-shell-header-context-menu-surface]') || W(B('Temporary chat'), 1000), states: R, pad: 0, desc: '52 tall: the Chat / Work toggle centred, Upgrade and temporary chat at the end.' },
  { key: 'mode-toggle', group: 'Top bar', title: 'Chat / Work segmented toggle', snap: 'home-dark', find: () => P(C(T('Chat', M()), 'button').parentElement), states: R, desc: 'A pill track with two 112x36 segments; the selected one carries a filled thumb.' },
  { key: 'mode-segment', group: 'Top bar', title: 'Mode segment (Work, not selected)', snap: 'home-dark', find: () => C(TS('Work', M()), 'button'), states: ALLP, extra: { selected: { find: () => C(T('Chat', M()), 'button'), states: ['hover'] } } },
  { key: 'header-upgrade', group: 'Top bar', title: 'Link-style button (header Upgrade)', snap: 'home-dark', find: () => B('Upgrade', QA('header') || document), states: ALLP, desc: 'Transparent pill, accent sparkle and label in `--color-text-header-upgrade`.' },
  { key: 'header-icon-button', group: 'Top bar', title: 'Icon button (Temporary chat)', snap: 'home-dark', find: () => Q('button[aria-label="Temporary chat"]'), states: ALLP },
  { key: 'share-button', group: 'Top bar', title: 'Secondary button (Share)', snap: 'thread-dark-code', find: () => B('Share'), states: ALLP },
  { key: 'more-button', group: 'Top bar', title: 'Icon button (More, thread)', snap: 'thread-dark-code', find: () => Q('button[aria-label="More"]'), states: ALLP },

  // ---------------- Home
  { key: 'home-heading', group: 'Home', title: 'Home heading', snap: 'home-dark', find: () => T('Ready when you are.'), states: R },
  { key: 'suggestion-row', group: 'Home', title: 'Suggestion row', snap: 'home-dark', find: () => C(T('Write or edit'), 'button'), states: ALLP, desc: '768x52, icon and 16px tertiary text; hover fills with `--color-background-home-suggestion-hover`.' },
  { key: 'promo-card', group: 'Home', title: 'Card (Plus nudge)', snap: 'home-dark', find: () => Q('aside[class*="surface-"]'), states: R, desc: '768x74 card pinned under the suggestions: icon, title and line, a filled Get Plus button and a dismiss button.' },
  { key: 'promo-button', group: 'Home', title: 'Primary button (Get Plus)', snap: 'home-dark', find: () => B('Get Plus'), states: ALLP },
  { key: 'promo-dismiss', group: 'Home', title: 'Dismiss button', snap: 'home-dark', find: () => Q('button[class*="dismissButton"]'), states: ALL },

  // ---------------- Composer
  {
    key: 'composer', group: 'Composer', title: 'Text area (composer)', snap: 'home-dark', find: () => P(Q('.ProseMirror').parentElement), focusOn: () => Q('.ProseMirror'), states: ['default', 'focus-visible'],
    desc: 'A pill on the home page, 768 wide: + button, the ProseMirror field, Think, dictate, voice.',
    extra: { typed: { snap: 'home-dark-composer-typed', find: () => P(Q('.ProseMirror').parentElement) }, thread: { snap: 'thread-dark-code', find: () => P(Q('.ProseMirror').parentElement) } },
  },
  { key: 'composer-placeholder', group: 'Composer', title: 'Composer placeholder', snap: 'home-dark', find: () => Q('.ProseMirror p'), states: R },
  { key: 'composer-plus', group: 'Composer', title: 'Icon button (composer +)', snap: 'home-dark', find: () => Q('button[aria-label="Add files and more"]'), states: ALLP },
  { key: 'think-chip', group: 'Composer', title: 'Think chip', snap: 'home-dark', find: () => C(T('Think'), 'button'), states: ALLP },
  { key: 'dictate-button', group: 'Composer', title: 'Icon button (Dictate)', snap: 'home-dark', find: () => Q('button[aria-label="Dictate"]'), states: ALLP },
  { key: 'voice-button', group: 'Composer', title: 'Accent icon button (Start Voice)', snap: 'home-dark', find: () => Q('button[aria-label="Start Voice"]'), states: ALLP, desc: 'A 36px circle in `--color-background-composer-primary`, the accent.' },
  { key: 'send-button', group: 'Composer', title: 'Accent icon button (Send, typed)', snap: 'home-dark-composer-typed', find: () => Q('button[aria-label="Send"]'), states: ALLP },
  { key: 'tooltip', group: 'Composer', title: 'Tooltip (Dictate)', snap: 'home-dark-tooltip', find: () => Q('[role=tooltip]'), states: R, desc: 'Opened by keyboard focus on the Dictate button: `--color-background-tooltip` fill, rounded, 14px text.' },

  // ---------------- Thread
  { key: 'user-bubble', group: 'Thread', title: 'User message bubble', snap: 'thread-dark-user-turn', find: () => Q('[data-user-message-bubble]'), states: R, desc: '`--color-background-user-message` / `--color-text-user-message`; right-aligned, rounded.' },
  { key: 'markdown', group: 'Thread', title: 'Assistant markdown body', snap: 'thread-dark-table', find: () => Q('[class*="MarkdownRoot"]'), states: R, pad: 0 },
  { key: 'md-paragraph', group: 'Thread', title: 'Markdown paragraph', snap: 'thread-dark-table', find: () => Q('[class*="MarkdownRoot"] p'), states: R },
  { key: 'md-heading', group: 'Thread', title: 'Markdown heading', snap: 'thread-dark-table', find: () => Q('[class*="MarkdownRoot"] h1, [class*="MarkdownRoot"] h2, [class*="MarkdownRoot"] h3'), states: R },
  { key: 'md-strong', group: 'Thread', title: 'Markdown strong', snap: 'thread-dark-table', find: () => Q('[class*="MarkdownRoot"] strong'), states: R },
  { key: 'md-inline-code', group: 'Thread', title: 'Inline code', snap: 'thread-dark-code', find: () => [...document.querySelectorAll('[class*="MarkdownRoot"] code')].find((c) => !c.closest('pre') && c.getBoundingClientRect().width > 1 && c.getBoundingClientRect().top > 0), states: R },
  { key: 'md-link', group: 'Thread', title: 'Link (citation in an answer)', snap: 'thread-dark-table', find: () => Q('[class*="MarkdownRoot"] a[href]'), states: ALL },
  { key: 'code-block', group: 'Thread', title: 'Code block', snap: 'thread-dark-code', find: () => Q('[class*="CodeSurface"]'), states: R },
  { key: 'code-text', group: 'Thread', title: 'Code text (inside a code block)', snap: 'thread-dark-code', find: () => Q('[class*="CodeSurface"] pre code'), states: R, desc: 'The `code` element itself, not the language label in the block header; `typography.code` is read from it.' },
  { key: 'code-block-button', group: 'Thread', title: 'Code block icon button', snap: 'thread-dark-code', find: () => Q('[class*="CodeSurface"] button'), states: ALLP },
  { key: 'md-table', group: 'Thread', title: 'Table', snap: 'thread-dark-table', find: () => Q('table'), states: R },
  { key: 'md-th', group: 'Thread', title: 'Table header cell', snap: 'thread-dark-table', find: () => Q('table th'), states: R },
  { key: 'md-td', group: 'Thread', title: 'Table cell', snap: 'thread-dark-table', find: () => Q('table td'), states: R },
  { key: 'turn-action', group: 'Thread', title: 'Turn action button (Copy)', snap: 'thread-dark-code', find: () => { const mds = [...document.querySelectorAll('[class*="MarkdownRoot"]')]; const md = mds[mds.length - 1]; let n = md; for (let i = 0; i < 10 && n; i++) { n = n.parentElement; const bs = [...n.querySelectorAll('button')].filter((b) => !md.contains(b) && Math.round(b.getBoundingClientRect().width) === 32 && !/Scroll/.test(b.getAttribute('aria-label') || '')); if (bs.length >= 3) return bs[0]; } return null; }, states: ALLP },
  { key: 'scroll-button', group: 'Thread', title: 'Scroll to bottom button', snap: 'thread-dark-user-turn', find: () => Q('button[aria-label="Scroll to bottom"]'), states: ALLP },
  { key: 'thread-disclaimer', group: 'Thread', title: 'Thread disclaimer', snap: 'thread-dark-code', find: () => TS('ChatGPT can make mistakes'), states: R },

  // ---------------- Feedback (a temporary chat: one prompt sent, then Copy on its code block)
  { key: 'streaming-dot', group: 'Feedback', title: 'Loading indicator (streaming dot)', snap: 'thread-dark-streaming', find: () => Q('.pulsing-dot'), states: R, desc: 'Where the answer will appear while it is being generated: a 12px dot in the composer colour that pulses (the copy shows one frame).' },
  { key: 'stop-button', group: 'Feedback', title: 'Icon button (Stop, while streaming)', snap: 'thread-dark-streaming', find: () => Q('[data-testid="stop-button"], button[aria-label*="Stop"]'), states: ALLP, desc: 'The composer\'s send button becomes Stop for as long as the answer streams.' },
  { key: 'toast', group: 'Feedback', title: 'Toast (error: Couldn\u2019t copy to clipboard)', snap: 'thread-dark-copied', find: () => C(T('Couldn\u2019t copy to clipboard'), '.alert-root'), states: R, desc: 'Copy on a code block failed (the capture browser refuses clipboard writes), and ChatGPT said so in a toast at the top centre: an icon, a bold line, a second line, and a close button.' },
  { key: 'toast-close', group: 'Feedback', title: 'Icon button (close toast)', snap: 'thread-dark-copied', find: () => C(T('Couldn\u2019t copy to clipboard'), '.alert-root').querySelector('button'), states: ALLP },
  { key: 'save-chat', group: 'Feedback', title: 'Popover (Save chat, temporary chat)', snap: 'thread-dark-copied', find: () => PW(T('Save chat'), 300), states: R, desc: 'After the first answer in a temporary chat, a popover under the header offers to save the chat to the history.' },
  { key: 'temp-bubble', group: 'Feedback', title: 'User bubble (temporary chat)', snap: 'thread-dark-copied', find: () => Q('[class*="bg-user-message"]'), states: R, desc: 'In a temporary chat the user bubble keeps the accent fill and gains a dashed outline.' },

  // ---------------- Menus
  { key: 'chat-menu', group: 'Menus', title: 'Menu (chat row)', snap: 'home-dark-chat-menu', find: () => Q('[role=menu]'), states: R, desc: 'Rename, Pin, Share, Archive, Delete (danger), Move to project; hairline separators between groups.' },
  { key: 'menu-item', group: 'Menus', title: 'Menu item', snap: 'home-dark-chat-menu', find: () => Q('[role=menu] [role=menuitem]', 0), states: ['default', 'hover', 'pressed'] },
  { key: 'menu-item-danger', group: 'Menus', title: 'Menu item (Delete, danger)', snap: 'home-dark-chat-menu', find: () => C(T('Delete', Q('[role=menu]')), '[role=menuitem]'), states: HV },
  { key: 'plus-menu', group: 'Menus', title: 'Menu (composer +)', snap: 'home-dark-plus-menu', find: () => PW(TS('Add photos'), 500), states: R, desc: 'Not a role=menu: a popover of buttons at the composer\'s width, each with a title and a grey hint.' },
  { key: 'plus-menu-item', group: 'Menus', title: 'Menu item with hint (composer +)', snap: 'home-dark-plus-menu', find: () => C(TS('Add from library'), 'button'), states: HV, extra: { highlighted: { find: () => C(TS('Add photos'), 'button') } } },
  { key: 'user-menu', group: 'Menus', title: 'Menu (account)', snap: 'home-dark-user-menu', find: () => Q('[role=menu]'), states: R },
  { key: 'checkbox-menu-item', group: 'Menus', title: 'Checkbox menu item (checked)', snap: 'settings-dark-notifications-menu', find: () => Q('[role=menuitemcheckbox]'), states: HV, desc: '`menuitemcheckbox`, aria-checked=true, a trailing check.' },
  { key: 'accent-menu', group: 'Menus', title: 'Select listbox (accent colour)', snap: 'settings-dark-accent-menu', find: () => Q('[role=menu]'), states: R, desc: 'Default, Blue (checked), Green, Yellow, Pink, Orange, Purple, White, Custom; each with a colour dot.' },
  { key: 'accent-item', group: 'Menus', title: 'Select option (accent)', snap: 'settings-dark-accent-menu', find: () => Q('[role=menu] [role=menuitem], [role=menu] [role=menuitemradio]', 2), states: HV, extra: { checked: { find: () => Q('[role=menu] [aria-checked=true]') || C(T('Blue', Q('[role=menu]')), '[role^=menuitem]') } } },

  // ---------------- Dialogs and search
  { key: 'confirm-dialog', group: 'Dialogs', title: 'Dialog (delete confirmation)', snap: 'home-dark-delete-confirm', find: () => Q('[role=dialog]'), states: R, desc: '420 wide: title, body naming the chat, Cancel and a danger Delete chat, close in the corner.' },
  { key: 'dialog-backdrop', group: 'Dialogs', title: 'Dialog backdrop', snap: 'home-dark-delete-confirm', find: () => [...document.querySelectorAll('body *')].find((e) => { const c = getComputedStyle(e); const r = e.getBoundingClientRect(); return (c.position === 'fixed' || c.position === 'absolute') && r.width >= innerWidth - 1 && r.height >= innerHeight - 1 && (c.backgroundColor !== 'rgba(0, 0, 0, 0)' || c.backdropFilter !== 'none'); }), states: R, crop: false },
  { key: 'button-danger', group: 'Dialogs', title: 'Danger button (Delete chat)', snap: 'home-dark-delete-confirm', find: () => B('Delete chat'), states: ALLP },
  { key: 'button-secondary', group: 'Dialogs', title: 'Secondary button (Cancel)', snap: 'home-dark-delete-confirm', find: () => B('Cancel'), states: ALLP },
  { key: 'dialog-close', group: 'Dialogs', title: 'Dialog close button', snap: 'home-dark-delete-confirm', find: () => B('Close dialog', D() || document), states: ALLP },
  { key: 'search-dialog', group: 'Dialogs', title: 'Dialog (global search)', snap: 'home-dark-search', find: () => Q('[role=dialog]'), states: R },
  { key: 'search-field', group: 'Dialogs', title: 'Text field (search)', snap: 'home-dark-search', find: () => Q('[role=dialog] input'), states: ['default', 'focus-visible'], extra: { typed: { snap: 'home-dark-search-empty', find: () => Q('[role=dialog] input') } } },
  { key: 'search-result', group: 'Dialogs', title: 'List row (search result)', snap: 'home-dark-search', find: () => { const t = TS('Sample title', D()); return t && (C(t, 'button,a,[role=option],li') || W(t, 600)); }, states: ALL },
  { key: 'search-tab', group: 'Dialogs', title: 'Tab (search filter)', snap: 'home-dark-search-empty', find: () => Q('[role=dialog] [role=tab][aria-selected=false]'), states: ALLP, extra: { selected: { find: () => Q('[role=dialog] [role=tab][aria-selected=true]') } } },
  { key: 'search-empty', group: 'Dialogs', title: 'Empty state (no results)', snap: 'home-dark-search-empty', find: () => W(T('No results', D()), 200), states: R },

  // ---------------- Library
  { key: 'library-title', group: 'Library', title: 'Page title (Library)', snap: 'library-dark', find: () => Q('main h1'), states: R },
  { key: 'library-icon-button', group: 'Library', title: 'Icon button (List view)', snap: 'library-dark', find: () => Q('button[aria-label="List view"]'), states: ALLP, extra: { selected: { find: () => Q('button[aria-label="Grid view"]') } } },
  { key: 'library-search', group: 'Library', title: 'Text field (Search library)', snap: 'library-dark', find: () => P(Q('input[id^="library-search"]').parentElement), focusOn: () => Q('input[id^="library-search"]'), states: ['default', 'hover', 'focus-visible'] },
  { key: 'library-new', group: 'Library', title: 'Inverted button (New)', snap: 'library-dark', find: () => C(T('New', M()), 'button'), states: ALLP },
  { key: 'library-tab', group: 'Library', title: 'Tab (Library)', snap: 'library-dark', find: () => Q('main [role=tab][aria-selected=false]'), states: ALLP, extra: { selected: { find: () => Q('main [role=tab][aria-selected=true]') } } },
  { key: 'library-card', group: 'Library', title: 'Card (Library file)', snap: 'library-dark', find: () => P(Q('[data-library-item] button')), hoverOn: () => Q('[data-library-item] button'), states: ['default', 'hover'], desc: 'Masonry grid cards (5 columns at 1440): a thumbnail (blanked in the copies) over the file name.' },
  { key: 'checkbox', group: 'Library', title: 'Checkbox (select a file)', snap: 'library-dark', find: () => QA('[data-library-item] [role=checkbox]'), hoverOn: () => QA('[data-library-item] button'), states: ['hover', 'focus-visible'], desc: 'A 20x20 `role=checkbox` button on each card, shown on hover.' },
  { key: 'library-error', group: 'Library', title: 'Error state (Failed to load files)', snap: 'library-dark-error', find: () => B('Try again') && B('Try again').parentElement, states: R, desc: 'Shown when the file list request fails (the capture guard refused it); a centred line and a Try again button.' },
  { key: 'retry-button', group: 'Library', title: 'Small button (Try again)', snap: 'library-dark-error', find: () => B('Try again'), states: ALLP },
  { key: 'inline-error', group: 'Library', title: 'Inline error (partial search results)', snap: 'library-dark-search-error', find: () => W(TS('Some search results'), 300), states: R },
  { key: 'library-loading', group: 'Library', title: 'Loading placeholder (file card shimmer)', snap: 'library-dark-loading', find: () => Q('[class*="LoadingResultsShimmer"]').parentElement, states: R, desc: 'While the file list loads, the grid holds shimmer cards of the file card\'s size (the capture guard held the request open). The shimmer is animated in the product; the copy has no scripts, so it shows one frame.' },

  // ---------------- Images and Plugins
  { key: 'images-tab', group: 'Images', title: 'Tab (Images)', snap: 'images-dark', find: () => Q('main [role=tab][aria-selected=false]'), states: ALLP, extra: { selected: { find: () => Q('main [role=tab][aria-selected=true]') } } },
  { key: 'image-card', group: 'Images', title: 'Card (image template)', snap: 'images-dark', find: () => P(Q('main img').parentElement) || W(Q('main img'), 100), states: HV },
  { key: 'plugins-search', group: 'Plugins', title: 'Text field (Search plugins)', snap: 'plugins-dark', find: () => P(Q('#plugins-store-page-search').parentElement), focusOn: () => Q('#plugins-store-page-search'), states: ['default', 'hover', 'focus-visible'] },
  { key: 'plugins-tab', group: 'Plugins', title: 'Tab (Plugins / Skills)', snap: 'plugins-dark', find: () => Q('[role=tab][aria-selected=false]'), states: ALL, extra: { selected: { find: () => Q('[role=tab][aria-selected=true]') } } },
  // The card is a bordered box with an absolutely placed link over it (inset-0, rounded-[inherit]);
  // the card paints the border, padding and hover fill, the link paints the focus ring.
  { key: 'plugin-row', group: 'Plugins', title: 'List row (plugin card)', snap: 'plugins-dark', find: () => CK(T('Gmail'), 'rounded-2xl border p-2'), states: ['default', 'hover', 'pressed'], desc: 'A bordered card with a link laid over the whole of it; hover fills the card, keyboard focus rings the link (see the next row).' },
  { key: 'plugin-row-link', group: 'Plugins', title: 'List row link (plugin card, focus ring)', snap: 'plugins-dark', find: () => { const c = CK(T('Gmail'), 'rounded-2xl border p-2'); return c && c.querySelector('a'); }, states: ['focus-visible'] },

  // ---------------- Settings
  { key: 'settings-nav-item', group: 'Settings', title: 'Settings nav item', snap: 'settings-dark-appearance', find: () => C(T('General'), 'a,button'), states: ALLP, extra: { selected: { find: () => C(T('Appearance', Q('nav') || document), 'a,button') } } },
  { key: 'settings-row', group: 'Settings', title: 'Settings row', snap: 'settings-dark-data-controls', find: () => H(T('Archive all chats'), 56), states: R },
  { key: 'switch-on', group: 'Settings', title: 'Switch (on)', snap: 'settings-dark-data-controls', find: () => Q('[role=switch][aria-checked=true]'), states: ALLP },
  { key: 'switch-off', group: 'Settings', title: 'Switch (off)', snap: 'settings-dark-data-controls', find: () => Q('[role=switch][aria-checked=false]'), states: ALLP },
  { key: 'button-outline', group: 'Settings', title: 'Outline button (Archive all)', snap: 'settings-dark-data-controls', find: () => B('Archive all'), states: ALLP },
  { key: 'button-danger-outline', group: 'Settings', title: 'Danger outline button (Delete all)', snap: 'settings-dark-data-controls', find: () => B('Delete all'), states: ALLP },
  { key: 'button-disabled', group: 'Settings', title: 'Button (disabled, Restore defaults)', snap: 'settings-dark-keyboard', find: () => B('Restore defaults'), states: ['default', 'hover'] },
  { key: 'keyboard-switch', group: 'Settings', title: 'Switch (keyboard shortcut on)', snap: 'settings-dark-keyboard', find: () => Q('[role=switch]'), states: R },
  { key: 'select', group: 'Settings', title: 'Select (notification channel)', snap: 'settings-dark-notifications-menu', find: () => Q('main button[aria-haspopup=menu]', 1), states: ALLP, extra: { open: { find: () => Q('main button[aria-expanded=true]') } } },
  { key: 'code-theme-select', group: 'Settings', title: 'Select (code theme)', snap: 'settings-dark-appearance', find: () => Q('button[aria-label="Dark code theme"]'), states: ALLP },
  { key: 'color-field', group: 'Settings', title: 'Text field (colour hex)', snap: 'settings-dark-appearance', find: () => Q('input[aria-label="Dark background color"]'), states: ['default', 'hover', 'focus-visible'] },
  { key: 'archived-search', group: 'Settings', title: 'Text field (Search archived chats)', snap: 'settings-dark-archived', find: () => P(Q('#archived-tasks-search').parentElement), focusOn: () => Q('#archived-tasks-search'), states: ['default', 'hover', 'focus-visible'] },
  { key: 'archived-row', group: 'Settings', title: 'List row (archived chat)', snap: 'settings-dark-archived', find: () => C(Q('button[data-archived-chat-unarchive]'), '[class*="settings-row"]') || H(Q('button[data-archived-chat-unarchive]'), 56), states: HV },
  { key: 'archived-link', group: 'Settings', title: 'Link (archived chat title)', snap: 'settings-dark-archived', find: () => Q('main a[href*="/c/"]'), states: ALLP },
  { key: 'unarchive-button', group: 'Settings', title: 'Outline button (Unarchive)', snap: 'settings-dark-archived', find: () => Q('button[data-archived-chat-unarchive]'), states: ALLP },
  { key: 'text-link', group: 'Settings', title: 'Link (Manage tasks)', snap: 'settings-dark-notifications-menu', find: () => C(T('Manage tasks'), 'a'), states: ALLP },

  // ---------------- Pricing
  { key: 'pricing-dialog', group: 'Pricing', title: 'Full-screen dialog (pricing)', snap: 'pricing-dark', find: () => Q('[role=dialog]'), states: R, pad: 0, crop: false },
  { key: 'segmented-radio', group: 'Pricing', title: 'Radio segment (Business, not checked)', snap: 'pricing-dark', find: () => Q('[role=dialog] [role=radio][aria-checked=false]'), states: ALLP, extra: { checked: { find: () => Q('[role=dialog] [role=radio][aria-checked=true]') } } },
  { key: 'pricing-card', group: 'Pricing', title: 'Card (Free plan)', snap: 'pricing-dark', find: () => P(Q('[data-pricing-plan-type=free]')) || Q('[data-pricing-plan-type=free]'), states: R },
  { key: 'pricing-card-plus', group: 'Pricing', title: 'Card (Plus plan, recommended)', snap: 'pricing-dark', find: () => { const b = T('RECOMMENDED') || TS('Recommended'); let n = b; while (n && n.getBoundingClientRect().width < 300) n = n.parentElement; return P(n) || n; }, states: R },
  { key: 'badge', group: 'Pricing', title: 'Badge (RECOMMENDED)', snap: 'pricing-dark', find: () => T('RECOMMENDED') || TS('Recommended'), states: R },
  { key: 'button-disabled-plan', group: 'Pricing', title: 'Button (disabled, Your current plan)', snap: 'pricing-dark', find: () => B('Your current plan'), states: R },
  { key: 'pricing-primary', group: 'Pricing', title: 'Accent button (Rejoin Plus)', snap: 'pricing-dark', find: () => B('Rejoin Plus'), states: ALLP },
  { key: 'pricing-close', group: 'Pricing', title: 'Icon button (Close pricing)', snap: 'pricing-dark', find: () => Q('button[aria-label="Close pricing"]'), states: ALLP },

  // ---------------- Signed out (the public page, read in a clean browser with no account)
  { key: 'onb-nudge', group: 'Signed out', title: 'Card (sign-in nudge)', snap: 'onboarding-dark', find: () => C(T('Get responses tailored to you'), 'section'), states: R, desc: 'The sidebar card a signed-out visitor sees: a heading, one line on what signing in adds, and a full-width Log in button.' },
  { key: 'onb-login-header', group: 'Signed out', title: 'Inverted button (Log in, header)', snap: 'onboarding-dark', find: () => [...document.querySelectorAll('button')].find((b) => b.textContent.trim() === 'Log in' && b.getBoundingClientRect().y < 60), states: ALLP },
  { key: 'onb-signup-header', group: 'Signed out', title: 'Secondary button (Sign up for free)', snap: 'onboarding-dark', find: () => B('Sign up for free'), states: ALLP },
  { key: 'onb-login-card', group: 'Signed out', title: 'Secondary button (Log in, card)', snap: 'onboarding-dark', find: () => C(T('Get responses tailored to you'), 'section').querySelector('button'), states: ALLP },
  { key: 'onb-dialog', group: 'Signed out', title: 'Dialog (Log in or sign up)', snap: 'onboarding-dark-signup', find: () => [...document.querySelectorAll('dialog[open], [role=dialog]')].filter((d) => d.getBoundingClientRect().width > 300).pop(), states: R, desc: 'Opened by Sign up for free: three provider buttons, an OR rule, an email field and Continue.' },
  { key: 'onb-provider', group: 'Signed out', title: 'Outline button (Continue with Google)', snap: 'onboarding-dark-signup', find: () => C(T('Continue with Google'), 'a,button'), states: ALLP },
  { key: 'onb-email', group: 'Signed out', title: 'Text field (email)', snap: 'onboarding-dark-signup', find: () => Q('input[type=email]'), states: ['default', 'hover', 'focus-visible'],
    extra: { error: { snap: 'onboarding-dark-email-error', find: () => Q('input[type=email]') } } },
  { key: 'onb-email-error', group: 'Signed out', title: 'Field error text (Email is not valid.)', snap: 'onboarding-dark-email-error', find: () => C(T('Email is not valid.'), 'p') || T('Email is not valid.'), states: R, desc: 'Shown under the field after Continue with an incomplete address; the field gets a red border and aria-invalid.' },
  { key: 'onb-continue', group: 'Signed out', title: 'Primary button (Continue)', snap: 'onboarding-dark-signup', find: () => B('Continue'), states: ALLP, extra: { 'after-error': { snap: 'onboarding-dark-email-error', find: () => B('Continue') } } },

  // ---------------- Phone (390)
  { key: 'm-header', group: 'Phone', title: 'Phone header', snap: 'mobile-home-dark', find: () => QA('header'), states: R, pad: 0 },
  { key: 'm-composer', group: 'Phone', title: 'Phone composer', snap: 'mobile-home-dark', find: () => P(Q('.ProseMirror').parentElement), states: R },
  { key: 'm-drawer', group: 'Phone', title: 'Phone drawer', snap: 'mobile-home-dark-drawer', find: () => S() || D(), states: R, pad: 0 },
  { key: 'm-drawer-row', group: 'Phone', title: 'Phone drawer row', snap: 'mobile-home-dark-drawer', find: () => Q('button[data-sidebar-destination="builtin:images"]'), states: R },
  { key: 'm-user-bubble', group: 'Phone', title: 'Phone user bubble', snap: 'mobile-thread-dark', find: () => Q('[data-user-message-bubble]'), states: R },
  { key: 'm-code-block', group: 'Phone', title: 'Phone code block', snap: 'mobile-thread-dark-bottom', find: () => Q('[class*="CodeSurface"]'), states: R },
];

// ---------------------------------------------------------------- jobs

function jobsFor(spec) {
  const out = [];
  for (const st of spec.states) out.push({ state: st, base: st, snap: spec.snap, find: spec.find, hoverOn: spec.hoverOn, focusOn: spec.focusOn, prep: spec.prep });
  for (const [name, v] of Object.entries(spec.extra || {})) {
    out.push({ state: name, base: 'default', snap: v.snap || spec.snap, find: v.find, variant: true });
    for (const st of v.states || []) out.push({ state: `${name}-${st}`, base: st, snap: v.snap || spec.snap, find: v.find, variant: true });
  }
  return out;
}

const MOBILE = (label) => label.startsWith('mobile-');

// The context is closed however measuring ends, so a copy that throws does not keep its pages open
// while the other workers go on. Returns whether the copy opened.
async function measureSnap(browser, label, specs, out) {
  const meta = metaOf(label);
  const ctx = await newContext(browser, meta);
  try {
    return await measureIn(ctx, meta, label, specs, out);
  } finally {
    await ctx.close().catch(() => {});
  }
}

async function measureIn(ctx, meta, label, specs, out) {
  await ctx.addInitScript(HELPERS);
  let page;
  try {
    page = await openSnap(ctx, label);
  } catch (e) {
    log('  ! open failed', label, e.message.split('\n')[0]);
    return false;
  }
  const rest = { x: meta.w - 2, y: Math.round(meta.h / 2) };
  // A <dialog open closedby="any"> (the signed-out sign-up sheet) closes itself on a light
  // dismiss even with scripts gone, so every dialog open in the copy is opened again before each
  // reading.
  await page.evaluate(() => { window.__saveScroll(); window.__openDialogs = [...document.querySelectorAll('dialog[open]')]; });
  const resetPage = async () => {
    await page.evaluate(() => { if (document.activeElement && document.activeElement.blur) document.activeElement.blur(); for (const d of window.__openDialogs || []) if (!d.open) d.setAttribute('open', ''); });
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
    execFileSync(PYTHON, ['-c', 'import sys\nfrom PIL import Image\nf=sys.argv[1]\nim=Image.open(f).convert("RGB")\nif im.width>1600: im=im.resize((im.width//2, im.height//2), Image.LANCZOS)\nim.quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(f, optimize=True)', file]);
    return path.relative(REF, file);
  };

  for (const theme of ['dark', 'light']) {
    if (theme === 'light') {
      // The signed-in app switches on data-theme; the signed-out page on prefers-color-scheme.
      // render.mjs renders light with both, so the readings do too.
      await page.emulateMedia({ colorScheme: 'light' });
      await toLight(page);
      await page.waitForTimeout(600);
    }
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
        await ensureVisible(loc);
        let via = job.variant && job.base === 'default' ? `at rest, captured ${job.state}` : 'at rest';
        let focus;
        let pressed = false;
        if (job.base === 'pressed') {
          const p = await pointOf(loc);
          await page.mouse.move(p.x, p.y, { steps: 4 });
          await page.waitForTimeout(250);
          await page.mouse.down();
          await page.waitForTimeout(300);
          pressed = true;
          via = 'mouse button held down on it (:hover:active)';
        } else if (job.base === 'hover') {
          const hl = (job.hoverOn && (await tag(job.hoverOn, 'hv'))) || loc;
          const p = await pointOf(hl);
          await page.mouse.move(p.x, p.y, { steps: 4 });
          // A second, sub-pixel move: an element revealed by group-hover only takes :hover itself
          // once the pointer moves again.
          await page.waitForTimeout(80);
          await page.mouse.move(p.x + 0.5, p.y);
          await page.waitForTimeout(450);
          via = job.hoverOn ? 'mouse hover on its row' : 'mouse hover';
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
        c.states[state] = { theme, snapshot: label, ...s, via };
        if (job.find !== spec.find) (c.selectors ||= {})[state] = job.find.toString();
        log('  ', name, `${s.rect.w}x${s.rect.h}`, via.slice(0, 50));
      } catch (e) {
        c.states[state] = { theme, snapshot: label, error: String(e.message || e).slice(0, 200) };
        log('  !', name, String(e.message || e).slice(0, 120));
      } finally {
        // off the element before the button comes up: a down and up on the same element is a click
        await page.mouse.move(rest.x, rest.y).catch(() => {});
        await page.mouse.up().catch(() => {});
        await untag().catch(() => {});
      }
    }
  }
  return true;
}

// ---------------------------------------------------------------- main

const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
const ALL_LABELS = [...new Set(SPECS.flatMap((s) => jobsFor(s).map((j) => j.snap)))];
// A mistyped label used to measure nothing and stamp the run's date as NaN-NaN-NaN.
const unknown = ONLY.filter((l) => !ALL_LABELS.includes(l));
if (unknown.length) { console.error(`no spec reads ${unknown.join(', ')}; labels are listed in shots.tsv`); process.exit(2); }
const labels = ALL_LABELS.filter((l) => !ONLY.length || ONLY.includes(l));
out._meta = {
  // The day the copies were taken (the oldest copy's local date), not the day this script ran. A
  // re-render from re-redacted copies is not a new reading: READ_DATE=YYYY-MM-DD keeps the original day.
  // A run over some of the copies keeps the date of the last full reading.
  read: process.env.READ_DATE || (labels.length < ALL_LABELS.length && out._meta && out._meta.read) || (() => { const t = new Date(Math.min(...labels.map((l) => fs.statSync(path.join(SNAPS, `${l}.html`)).mtimeMs))); return `${t.getFullYear()}-${String(t.getMonth() + 1).padStart(2, '0')}-${String(t.getDate()).padStart(2, '0')}`; })(),
  source: 'Static, redacted page copies of the signed-in chatgpt.com app (tools/capture/signed-in/snapshot.js), loaded from file:// in headless Chromium; the stylesheets and icon sprites are inlined in each copy, fonts and a few images come from OpenAI\'s asset hosts through a local cache. Nothing was requested from chatgpt.com itself.',
  viewport: '1440x900 (the mobile-* snapshots 390x844), deviceScaleFactor 2',
  themes: 'Each copy was captured in the dark theme with the blue accent. Dark states have plain names; light states (`light`, `light-<state>`) were read from the same DOM with every data-theme="dark" set to light. Every state records `theme` and `snapshot`.',
  states: {
    default: 'at rest, as captured',
    hover: 'real mouse hover (page.mouse.move), 450ms settle; not measured on the 390 snapshots',
    pressed: 'the mouse button held down on the element (page.mouse.down) for 300ms, so :active applies; released after the reading',
    'focus-visible': 'real keyboard focus (focus, Shift+Tab, Tab) on the element or its first focusable descendant; recorded as skipped where the element cannot take focus',
    other: 'active / selected / checked / open / typed / enabled / ... are other elements or snapshots captured in that state',
  },
  tokens: '`vars` lists every var(--x) named in the classes of the element and its first descendants, resolved in that state\'s theme.',
  // Entries kept from an earlier run go through safeUrl again, so a partial rerun never writes an
  // unmasked URL it carried over; new ones keep only origin and route words (no query, no fragment, no id).
  snapshots: { ...Object.fromEntries(Object.entries((out._meta && out._meta.snapshots) || {}).map(([l, v]) => [l, { ...v, url: v.url && safeUrl(v.url) }])), ...Object.fromEntries(labels.map((l) => { const m = metaOf(l); return [l, { url: safeUrl(m.url), ...(m.title ? { title: m.title.replace(/^.* - ChatGPT$/, '<chat title> - ChatGPT') } : {}), w: m.w, h: m.h, ...(SCROLL[l] ? { scroll: SCROLL[l] } : {}) }]; })) },
};
out.components ??= {};
fs.mkdirSync(CROPS, { recursive: true });

// Build the per-snapshot job lists, and the states each copy re-measures (moved aside while it runs).
const bySnap = new Map();
const RESET = new Map();
for (const spec of SPECS) {
  const c = (out.components[spec.key] ??= { states: {} });
  Object.assign(c, { group: spec.group, title: spec.title, desc: spec.desc, page: spec.snap, selector: spec.find.toString() });
  const jobs = jobsFor(spec);
  c.pages = [...new Set(jobs.map((j) => j.snap))];
  for (const job of jobs) {
    if (!labels.includes(job.snap)) continue;
    if (!RESET.has(job.snap)) RESET.set(job.snap, []);
    RESET.get(job.snap).push([c, job.state], [c, job.state === 'default' ? 'light' : `light-${job.state}`]);
    if (!bySnap.has(job.snap)) bySnap.set(job.snap, []);
    bySnap.get(job.snap).push({ spec, job });
  }
}

const browser = await chromium.launch();
const queue = [...bySnap.keys()].sort();
// Earlier readings of the states a copy in flight is re-measuring, by component. save() writes them
// wherever no new reading exists yet, so while workers run, the file on disk never loses one.
const earlier = new Map();
const save = () => {
  // Stable order: components in SPECS order, states in the order the spec lists them, dark then light.
  const comps = {};
  for (const spec of SPECS) {
    const c = out.components[spec.key];
    const names = jobsFor(spec).map((j) => j.state);
    const ordered = {};
    const prev = earlier.get(c) || {};
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
    // was measured, put back if it never opened or the run threw, so neither a failed open nor
    // another worker's save can erase what an earlier run measured.
    const kept = [];
    for (const [c, n] of RESET.get(label) || []) {
      if (!(n in c.states)) continue;
      if (!earlier.has(c)) earlier.set(c, {});
      earlier.get(c)[n] = c.states[n];
      kept.push([c, n]);
      delete c.states[n];
    }
    let opened = false;
    try {
      opened = await measureSnap(browser, label, bySnap.get(label), out);
    } catch (e) {
      log('  ! measuring failed', label, String(e.message || e).split('\n')[0]);
    }
    for (const [c, n] of kept) {
      if (!opened) c.states[n] ??= earlier.get(c)[n];
      delete earlier.get(c)[n];
    }
    save();
  }
}));
await browser.close();
save();
const all = SPECS.map((sp) => out.components[sp.key]);
const states = all.flatMap((c) => Object.values(c.states));
log(`${all.length} components, ${states.length} states (${states.filter((s) => s.error).length} errors, ${states.filter((s) => s.skipped).length} skipped)`);
