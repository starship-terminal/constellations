// Paste into the console of a signed-in notebook.google.com page, then call
// window.__snap('<label>', REDACT), where REDACT holds only the redaction file's `scrub`, `keep`,
// `keepPattern` and `badges` (selectors and UI words) with `replace: []`. The account's own
// literals are applied afterwards by unsnap.py, so they never pass through the browser tool.
// It returns one string, SNAPSTART<meta>SNAPMETA<html>SNAPEND: a static copy of the page with
// every same-origin stylesheet inlined from the CSSOM (each url() made absolute against its sheet),
// cross-origin sheets (Google Fonts, the Google bar) kept as <link> tags, scripts removed, iframes
// replaced by same-size boxes, canvases kept as images, signed URLs cut back to their path, the
// account photo replaced by a disc, and every text node inside a `scrub` selector replaced.
// Adapted from systems/linear/tools/capture/signed-in/snapshot.js (itself from the Manus kit);
// the sprite and thumbnail helpers are dropped because NotebookLM draws icons with a font.
// The page URL is kept as origin and path with ids masked: a copy of ../safe-url.mjs (a console
// paste cannot import), which tools/test_package_snapshots.py keeps identical.
const RESOURCE = /^(?:c|g|p|u|chat|chats|project|projects|artifact|artifacts|cowork|share|shared|doc|docs|document|documents|page|pages|file|files|folder|folders|thread|threads|conversation|conversations|task|tasks|issue|issues|notebook|notebooks|workspace|workspaces|space|spaces|team|teams|org|orgs|organization|user|users|profile|people|member|members|channel|channels|board|boards|session|sessions|course|courses|lesson|lessons|story|stories|collection|collections|dashboard|dashboards|database|databases|calendar|calendars|event|events|deck|decks|app|apps|repo|repos)$/i;

function safeUrl(u) {
  let x;
  try { x = new URL(u); } catch { return '<url>'; }
  if (x.protocol === 'file:') return 'file:///<local file>';   // a local path names the owner's home folder
  const base = x.origin !== 'null' ? x.origin : `${x.protocol}//${x.host}`;
  const parts = x.pathname.split('/');
  return base + parts.map((s, i) => (!s || (/^[a-z]+(?:[-_][a-z]+)?$/.test(s) && s.length <= 20
    && !RESOURCE.test(parts[i - 1] || '')) ? s : '<id>')).join('/');
}

window.__snap = function (label, REDACT) {
  if (!REDACT || !Array.isArray(REDACT.replace)) throw new Error('pass the redaction selectors as the second argument');
  // The credential-carrying URL parameters: a copy of signed-params.json beside unsnap.py (a console
  // paste cannot read files), matched after ?, &, &amp;, # or their %-encodings. Same regex as unsnap.py.
  const SIGNED_PARAMS = {"prefixes": ["X-Amz-", "X-Goog-"], "params": ["Signature", "Key-Pair-Id", "Policy", "Expires", "sig", "token", "access_token", "id_token", "refresh_token", "code", "auth", "key", "api_key", "apikey", "api-key", "access_key", "client_secret", "jwt", "session", "session_id", "sessionid", "hmac", "hdnts", "__token__", "auth_token", "oauth_token", "csrf_token", "xsrf_token", "session_token", "api_token", "sas_token"]};
  const SIGNED = new RegExp('(?:[?&#]|%3F|%26|%23)(?:amp;)?(' + [
    ...SIGNED_PARAMS.prefixes.map((p) => p.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '[A-Za-z0-9-]*'),
    ...SIGNED_PARAMS.params.map((p) => p.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')),
  ].join('|') + ')(?:=|%3D)', 'i');
  // Every query or fragment in a string that carries a signing parameter is cut out, wherever the URL
  // sits: an attribute of any name, an inline style's url(), a stylesheet, text (the kit's cutSigned).
  // A query runs to whitespace, a quote, an angle bracket, a CSS { or }, or a ; that starts a CSS
  // declaration (`;name:`), so a match that starts at a colour's # stops before a later declaration's
  // url(); any other ; (an &amp; entity, a ;-separated query) stays inside, as do commas and
  // parentheses, except a ")" that closes an unquoted url( ... ) before ; , } or the end.
  const cutSigned = (s) => s.replace(/[?#](?:[^\s"'<>);{}]|;(?![\w-]+\s*:)|\)(?![\s;,"'}]|$))*/g, (q) => (SIGNED.test(q) ? '' : q));
  const cutSignedUrl = (s) => s.replace(/[?#](?:[^\s"'<>);{}]|;|\)(?![\s"'}]|$))*/g, (q) => (SIGNED.test(q) ? '' : q));
  const abs = (u) => { let h; try { h = new URL(u, location.href).href; } catch { return cutSigned(u); } return SIGNED.test(h) ? h.split(/[?#]/)[0] : h; };
  const parts = [];
  for (const ss of document.styleSheets) {
    try {
      let t = '';
      // NotebookLM (adapt): Chrome serialises a rule like `font: var(--x); letter-spacing: ...` as
      // empty longhands ("font-family: ;"), which drops every Material type class from the copy.
      // An inline <style> keeps its source text, so that is copied instead of the CSSOM.
      const own = ss.ownerNode && ss.ownerNode.tagName === 'STYLE' && ss.ownerNode.textContent;
      if (own && own.trim()) t = own;
      else for (const r of ss.cssRules) t += r.cssText + '\n';
      const base = ss.href || location.href;
      t = t.replace(/url\((['"]?)([^'")]+)\1\)/g, (m, q, u) => (u.startsWith('data:') || u.startsWith('#') ? m : 'url("' + abs(new URL(u, base).href) + '")'));
      parts.push({ css: t, media: ss.media && ss.media.mediaText });
    } catch { if (ss.href) parts.push({ href: ss.href }); }
  }
  for (const ss of document.adoptedStyleSheets || []) {
    let t = '';
    for (const r of ss.cssRules) t += r.cssText + '\n';
    parts.push({ css: t, adopted: true });
  }
  const clone = document.documentElement.cloneNode(true);
  const liveAll = document.documentElement.querySelectorAll('*'), cloneAll = clone.querySelectorAll('*');
  liveAll.forEach((e, i) => { if (e.scrollTop > 0 || e.scrollLeft > 0) cloneAll[i].setAttribute('data-snap-scroll', e.scrollTop + ',' + e.scrollLeft); });
  // NotebookLM (adapt): the focused control is marked so measure.mjs can find it again.
  liveAll.forEach((e, i) => { if (e === document.activeElement && e !== document.body) cloneAll[i].setAttribute('data-snap-focus', ''); });
  const srcC = document.querySelectorAll('canvas'), cC = clone.querySelectorAll('canvas');
  srcC.forEach((c, i) => {
    try {
      const img = document.createElement('img');
      img.src = c.toDataURL(); img.style.cssText = c.style.cssText;
      img.width = c.width; img.height = c.height; img.className = c.className;
      cC[i].replaceWith(img);
    } catch { /* tainted canvas: leave it blank */ }
  });
  const srcIf = document.querySelectorAll('iframe'), cIf = clone.querySelectorAll('iframe');
  srcIf.forEach((f, i) => {
    const r = f.getBoundingClientRect();
    const d = document.createElement('div');
    d.className = f.className; d.setAttribute('data-was-iframe', abs(f.src || '').split('?')[0]);
    d.style.cssText = f.style.cssText + ';width:' + r.width + 'px;height:' + r.height + 'px;background:transparent;display:' + (r.width ? 'block' : 'none');
    cIf[i].replaceWith(d);
  });
  // A field that holds a credential never reaches the copy: a hidden input (CSRF and session
  // tokens), a one-time code or card field loses its value; a password keeps only a fixed
  // eight-dot stand-in, so the field still renders filled.
  const SECRET_FIELD = (el) => el.type === 'hidden' || /one-time-code|cc-|current-password|new-password/.test(el.autocomplete || '')
    || /token|csrf|secret|otp|passcode|api[-_]?key/i.test((el.name || '') + ' ' + (el.id || ''));
  const srcIn = document.querySelectorAll('input,textarea,select'), cIn = clone.querySelectorAll('input,textarea,select');
  srcIn.forEach((el, i) => {
    const c = cIn[i];
    if (!c) return;
    if (el.type === 'password') { if (el.value) c.setAttribute('value', 'xxxxxxxx'); else c.removeAttribute('value'); return; }
    if (el.tagName === 'INPUT' && SECRET_FIELD(el)) { c.removeAttribute('value'); return; }
    if (el.type === 'checkbox' || el.type === 'radio') { if (el.checked) c.setAttribute('checked', ''); else c.removeAttribute('checked'); }
    else if (el.tagName === 'TEXTAREA') c.textContent = el.value;
    else if (el.tagName === 'SELECT') [...c.options].forEach((o, j) => { o.selected = el.options[j] && el.options[j].selected; });
    else c.setAttribute('value', el.value);
  });
  clone.querySelectorAll('script,noscript,link[rel="stylesheet"],link[rel="preload"],link[rel="modulepreload"],link[rel="prefetch"],style,base').forEach((n) => n.remove());
  clone.querySelectorAll('[src]').forEach((n) => n.setAttribute('src', abs(n.getAttribute('src'))));
  clone.querySelectorAll('[href]').forEach((n) => { const v = n.getAttribute('href'); if (!v.startsWith('#')) n.setAttribute('href', abs(v)); });
  clone.querySelectorAll('[srcset]').forEach((n) => n.setAttribute('srcset', n.getAttribute('srcset').split(',').map((p) => { const a = p.trim().split(/\s+/); a[0] = abs(a[0]); return a.join(' '); }).join(', ')));
  // The account photo (Google serves it from googleusercontent.com) becomes a grey disc.
  clone.querySelectorAll('img[src*="googleusercontent.com"], img[src*="gravatar.com"], img[src*="avatar"]').forEach((img) => {
    const d = document.createElement('div');
    d.className = img.className;
    d.setAttribute('style', 'display:inline-flex;align-items:center;justify-content:center;width:100%;height:100%;border-radius:9999px;background:#8a8a8a;color:#fff;font-weight:600;font-size:12px');
    d.textContent = 'L';
    img.replaceWith(d);
  });
  for (const [sel, rep] of REDACT.badges || []) {
    clone.querySelectorAll(sel).forEach((b) => {
      const w = document.createTreeWalker(b, NodeFilter.SHOW_TEXT);
      while (w.nextNode()) if (/^\s*[A-Za-z]{1,2}\s*$/.test(w.currentNode.nodeValue)) w.currentNode.nodeValue = rep;
      b.querySelectorAll('img').forEach((i) => i.remove());
    });
  }
  // NotebookLM (adapt): the page enforces Trusted Types, so the inlined sheets go in through a
  // pass-through policy.
  const TH = (x) => (window.trustedTypes ? (window.__tp ||= trustedTypes.createPolicy('snapcopy', { createHTML: (y) => y })).createHTML(x) : x);
  clone.querySelector('head').insertAdjacentHTML('beforeend', TH(parts.map((p) => (p.href
    ? '<link rel="stylesheet" href="' + p.href + '">'
    : '<style' + (p.adopted ? ' data-adopted=""' : '') + (p.media ? ' media="' + p.media + '"' : '') + '>' + p.css.replace(/<\/style/gi, '<\\/style') + '</style>')).join('\n')));
  // REDACT.scrub lists [selector, replacement] pairs: every text node inside a match that is not
  // in REDACT.keep becomes the replacement numbered in order ("Sample source 1", ...), so notebook,
  // source, note and output titles and chat text never reach the copy even when the redaction file
  // does not name them. Attributes that repeat a title are emptied inside matches. Icon ligatures
  // (mat-icon text) are left alone, since they are the icon's name.
  const keep = new Set(REDACT.keep || []);
  const keepRe = new RegExp(REDACT.keepPattern || '(?!)');
  for (const [sel, rep] of REDACT.scrub || []) {
    let n = 0;
    clone.querySelectorAll(sel).forEach((el) => {
      for (const a of ['aria-label', 'title', 'alt', 'mattooltip']) if (el.hasAttribute(a)) el.setAttribute(a, '');
      // An editable title is an <input> whose text lives in its value attribute.
      el.querySelectorAll('input,textarea').forEach((x) => { if (x.getAttribute('value')) x.setAttribute('value', rep + ' ' + (++n)); if (x.tagName === 'TEXTAREA' && x.textContent) x.textContent = rep + ' ' + (++n); });
      el.querySelectorAll('[aria-label],[title],[alt],[mattooltip]').forEach((x) => { for (const a of ['aria-label', 'title', 'alt', 'mattooltip']) if (x.hasAttribute(a) && !keep.has(x.getAttribute(a))) x.setAttribute(a, ''); });
      const w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
      const texts = [];
      while (w.nextNode()) texts.push(w.currentNode);
      for (const t of texts) {
        const v = t.nodeValue.trim();
        if (!v || keep.has(v) || keepRe.test(v) || /^[\d%.,:·\s/-]+$/.test(v)) continue;
        if (t.parentElement && t.parentElement.closest('mat-icon')) continue;
        t.nodeValue = rep + (/\s$/.test(rep) ? '' : ' ') + (++n);
      }
    });
  }
  // Cards, source rows and studio items repeat their title in aria-label.
  clone.querySelectorAll('[aria-label]').forEach((x) => { if (x.closest('project-button, .single-source-container, .artifact-item-button, .source-stretched-button')) x.setAttribute('aria-label', ''); });
  // Last, every attribute of every element (data-src, style="background:url(...)", anything) and then
  // the serialised copy, inlined stylesheets and text included, lose any signed query abs() missed.
  clone.querySelectorAll('*').forEach((n) => { for (const a of [...n.attributes]) { const v = (a.name === 'style' ? cutSigned : cutSignedUrl)(a.value); if (v !== a.value) n.setAttribute(a.name, v); } });
  const html = cutSigned('<!doctype html>\n' + clone.outerHTML);
  const pathOf = (el) => { const out = []; for (let n = el; n && n !== document.documentElement; n = n.parentElement) out.unshift([...n.parentElement.children].indexOf(n)); return out; };
  const scrolls = [...document.querySelectorAll('*')].filter((e) => e.scrollTop > 0).map((e) => ({ path: pathOf(e), top: e.scrollTop, left: e.scrollLeft, max: e.scrollHeight - e.clientHeight }));
  const meta = { label, url: safeUrl(location.href), title: '', scrollY, w: innerWidth, h: innerHeight, docH: document.documentElement.scrollHeight, scrolls };
  return 'SNAPSTART' + JSON.stringify(meta) + 'SNAPMETA' + html + 'SNAPEND';
};
'snapshot.js loaded';
