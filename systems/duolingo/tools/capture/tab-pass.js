// tab-pass.js: keyboard focus pass, second round (raw/2026-10/live-measurements-2.json).
//
// Paste once into the signed-in page, then for each control:
//   1. __restAll()          record the resting style of every focusable element and three ancestors
//   2. press Tab (a real key press through the pane, so :focus-visible is set)
//   3. __tab('<page>')      diff the focused element and its ancestors against rest, push to __flog
//      (__tab('<page>', 'ArrowDown') after an arrow key; build_focus_md.py reads these records as saved)
// Call __restAll() again after a menu or dialog opens, so its rows have a resting read.
// Get the log out with JSON.stringify({focus: __flog}). Reads after a script focus() are not key
// presses and were left out of the saved file.
(() => {
  const P = 'background-color color border-top-width border-bottom-width border-top-color border-right-color border-bottom-color border-left-color border-top-left-radius box-shadow opacity filter transform outline-style outline-width outline-color outline-offset text-decoration-line font-weight'.split(' ');
  const keep = (c) => { const o = {}; for (const p of P) o[p] = c.getPropertyValue(p); return o; };
  const one = (el) => {
    const r = el.getBoundingClientRect();
    const n = { tag: el.tagName.toLowerCase(), cls: (el.getAttribute('class') || '').slice(0, 80), rect: [r.x, r.y, r.width, r.height].map(Math.round), s: keep(getComputedStyle(el)) };
    for (const ps of ['::before', '::after']) { const pc = getComputedStyle(el, ps); if (pc.content && pc.content !== 'none' && pc.content !== 'normal') n[ps] = keep(pc); }
    for (const a of ['role', 'aria-label', 'aria-selected', 'aria-checked', 'data-test', 'type']) if (el.hasAttribute(a)) n[a] = (el.getAttribute(a) || '').slice(0, 60);
    return n;
  };
  const chain = (e) => { const out = []; for (let n = e, i = 0; n && i < 4 && n !== document.body; n = n.parentElement, i++) out.push(n); return out; };
  const dif = (a, b) => {
    const d = {};
    for (const k of Object.keys(b.s)) if (a.s[k] !== b.s[k]) d[k] = [a.s[k], b.s[k]];
    for (const ps of ['::before', '::after']) { const x = a[ps] || {}, y = b[ps] || {}; for (const k of Object.keys(y)) if (x[k] !== y[k]) d[ps + ' ' + k] = [x[k], y[k]]; }
    return d;
  };
  window.__rest = new WeakMap(); window.__flog = window.__flog || [];
  window.__restAll = () => {
    let n = 0;
    document.querySelectorAll('a,button,input,textarea,select,[tabindex],[role]').forEach(e => { for (const c of chain(e)) if (!__rest.has(c)) { __rest.set(c, one(c)); n++; } });
    return n;
  };
  window.__tab = (page, key = 'Tab') => {
    const e = document.activeElement;
    if (!e || e === document.body) { __flog.push({ page, el: 'body' }); return 'body'; }
    const levels = chain(e).map((c, i) => { const r = __rest.get(c); return { level: i, cls: (c.getAttribute('class') || '').slice(0, 50), diff: r ? dif(r, one(c)) : null }; });
    const me = one(e);
    const rec = { page, key, tag: me.tag, cls: me.cls, role: me.role, dt: me['data-test'], aria: me['aria-label'], sel: me['aria-selected'] || me['aria-checked'], type: me.type, rect: me.rect, fv: e.matches(':focus-visible'), levels };
    __flog.push(rec);
    const vis = levels.filter(l => l.diff && Object.keys(l.diff).filter(k => !/outline-offset/.test(k)).length).map(l => l.level + ':' + Object.keys(l.diff).join(','));
    return [me.tag, me.role || '', me['data-test'] || '', me.cls.slice(0, 30), 'fv=' + rec.fv, vis.join(' | ') || 'no visible change'].join(' ; ');
  };
})();
