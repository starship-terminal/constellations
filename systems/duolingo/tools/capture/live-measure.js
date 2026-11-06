// Pasted into the signed-in page in the built-in browser pane (2026-10 refresh). It defines:
//   __measure(specs)  specs is {name: selector} or {name: [selector, index]}; returns the computed
//                     style of each element (and its ::before / ::after) as it is right now, so a
//                     state held live (hover through the pointer, focus through a real Tab key
//                     press, an open menu) is measured, not inferred.
//   __active()        the same for document.activeElement and its two ancestors, plus whether it
//                     matches :focus-visible. Run it after pressing Tab in the pane.
//   __rules(re)       every CSS rule whose selector or condition matches re, with its stylesheet
//                     file name (for @media (prefers-reduced-motion), :focus-visible, :active).
// Only properties that differ from a bare <div> are kept. No text content is returned beyond a
// length, so no learner's name leaves the page; aria-label and data-test are kept because they
// name controls, not people.
(() => {
  const P = 'display position top left right bottom width height padding-top padding-right padding-bottom padding-left margin-top margin-bottom gap row-gap column-gap grid-template-columns grid-template-rows background-color background-image color border-top-width border-right-width border-bottom-width border-left-width border-top-color border-right-color border-bottom-color border-left-color border-top-style border-bottom-style border-top-left-radius border-top-right-radius border-bottom-right-radius border-bottom-left-radius box-shadow opacity filter backdrop-filter font-family font-size font-weight line-height letter-spacing text-transform text-decoration-line transition-property transition-duration transition-timing-function animation-name animation-duration transform z-index cursor max-width min-width min-height outline-style outline-width outline-color outline-offset fill stroke'.split(' ');
  const base = {};
  { const x = document.createElement('div'); document.body.appendChild(x); const c = getComputedStyle(x); for (const p of P) base[p] = c.getPropertyValue(p); x.remove(); }
  // A url() in a computed value (a background photo, a cursor) can be a signed or per-account URL:
  // recorded as url(…), only data: and #fragment references kept (the kit's noUrl).
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\(\s*(?!['"]?(?:data:|#))(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|[^)]*)\s*\)/g, 'url(…)') : v);
  const keep = (c) => { const o = {}; for (const p of P) { const v = c.getPropertyValue(p); if (v !== base[p] && v !== '') o[p] = noUrl(v).slice(0, 300); } return o; };
  const one = (el) => {
    if (!el) return null;
    const r = el.getBoundingClientRect();
    const n = { tag: el.tagName.toLowerCase(), cls: (el.getAttribute('class') || '').slice(0, 120), rect: [r.x, r.y, r.width, r.height].map(Math.round), s: keep(getComputedStyle(el)) };
    for (const a of ['role', 'aria-label', 'aria-disabled', 'aria-pressed', 'aria-checked', 'aria-selected', 'aria-expanded', 'data-test', 'disabled', 'type']) if (el.hasAttribute(a)) n[a] = (el.getAttribute(a) || '').slice(0, 80);
    n.textLen = (el.textContent || '').trim().length;
    for (const ps of ['::before', '::after']) { const pc = getComputedStyle(el, ps); if (pc.content && pc.content !== 'none' && pc.content !== 'normal') n[ps] = keep(pc); }
    try { n.focusVisible = el.matches(':focus-visible'); n.hover = el.matches(':hover'); } catch { /* old engine */ }
    return n;
  };
  window.__measure = (specs) => {
    const out = {};
    for (const [name, spec] of Object.entries(specs)) {
      const [sel, i] = Array.isArray(spec) ? spec : [spec, 0];
      const all = document.querySelectorAll(sel);
      out[name] = all.length ? { count: all.length, ...one(all[i]) } : { count: 0 };
    }
    return out;
  };
  window.__active = () => { const a = document.activeElement; return { self: one(a), parent: one(a && a.parentElement), grand: one(a && a.parentElement && a.parentElement.parentElement) }; };
  window.__rules = (re) => {
    const out = [];
    const walk = (rules, file, cond) => { for (const r of rules) {
      if (r.cssRules && !r.selectorText) walk(r.cssRules, file, (cond ? cond + ' ' : '') + (r.conditionText || r.media && r.media.mediaText || ''));
      else if (re.test((cond || '') + ' ' + (r.selectorText || ''))) out.push({ file, cond: cond || '', css: r.cssText.slice(0, 600) });
    } };
    for (const ss of document.styleSheets) { try { walk(ss.cssRules, (ss.href || 'inline').split('/').pop(), ''); } catch { /* cross-origin */ } }
    return out;
  };
  return 'live-measure ready';
})();
