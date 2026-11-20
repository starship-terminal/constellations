// Paste into the console of a signed-in app.researchrabbit.ai page (or run it through a
// browser tool's JavaScript action), then call window.__snap('<label>', REDACT), where REDACT
// is the contents of the redaction file (see redact.example.json): { "replace": [[pattern,
// flags, replacement], ...] }. It returns one string, SNAPSTART<meta>SNAPMETA<html>SNAPEND: a
// static copy of the page with every stylesheet inlined from the CSSOM (styled-components
// inserts its rules with insertRule, so the <style> tags alone are empty), scripts removed,
// iframes replaced by same-size boxes, signed URLs cut back to their path, every REDACT
// pattern replaced, and each <canvas> swapped for an <img> of its own bitmap. The graph is
// one canvas, so the copy keeps the graph exactly as it was drawn at that moment, at the
// device pixel ratio. unsnap.py writes it to disk and refuses it if a redacted string or a
// signing parameter survived; render.mjs screenshots it headless at 2x.
//
// The engine draws only when its state changes, and a browser tool's hover may reach the page
// only with its next action, so take a screenshot (any size) after the action and before the
// snapshot, or the canvas shows the state before.
window.__snap = function (label, REDACT) {
  if (!REDACT || !Array.isArray(REDACT.replace)) throw new Error('pass the redaction file as the second argument');
  // A presigned URL (S3, CloudFront) carries a credential that works until it expires, so
  // any URL with a signing parameter loses its whole query string.
  // The credential-carrying URL parameters: a copy of signed-params.json beside unsnap.py (a console
  // paste cannot read files), matched after ?, &, &amp;, # or their %-encodings. Same regex as unsnap.py.
  const SIGNED_PARAMS = {"prefixes": ["X-Amz-", "X-Goog-"], "params": ["Signature", "Key-Pair-Id", "Policy", "Expires", "sig", "token", "access_token", "id_token", "refresh_token", "code", "auth", "key", "api_key", "apikey", "api-key", "access_key", "client_secret", "jwt", "session", "session_id", "sessionid", "hmac", "hdnts", "__token__", "auth_token", "oauth_token", "csrf_token", "xsrf_token", "session_token", "api_token", "sas_token"]};
  const SIGNED = new RegExp('(?:[?&#]|%3F|%26|%23)(?:amp;)?(' + [
    ...SIGNED_PARAMS.prefixes.map((p) => p.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '[A-Za-z0-9-]*'),
    ...SIGNED_PARAMS.params.map((p) => p.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')),
  ].join('|') + ')(?:=|%3D)', 'i');
  const abs = (u) => { let h; try { h = new URL(u, location.href).href; } catch { return u; } return SIGNED.test(h) ? h.split(/[?#]/)[0] : h; };
  const parts = [];
  for (const ss of document.styleSheets) {
    try {
      let t = '';
      for (const r of ss.cssRules) t += r.cssText + '\n';
      parts.push({ css: t, media: ss.media && ss.media.mediaText });
    } catch { if (ss.href) parts.push({ href: ss.href }); }
  }
  const clone = document.documentElement.cloneNode(true);
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
    d.className = f.className;
    d.style.cssText = f.style.cssText + ';width:' + r.width + 'px;height:' + r.height + 'px;display:' + (r.width ? 'block' : 'none');
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
    else if (el.tagName !== 'SELECT') c.setAttribute('value', el.value);
  });
  clone.querySelectorAll('script,noscript,link[rel="stylesheet"],link[rel="preload"],link[rel="modulepreload"],link[rel="prefetch"],style,base').forEach((n) => n.remove());
  clone.querySelectorAll('[src]').forEach((n) => { const v = n.getAttribute('src'); if (!v.startsWith('data:')) n.setAttribute('src', abs(v)); });
  clone.querySelectorAll('[href]').forEach((n) => n.setAttribute('href', abs(n.getAttribute('href'))));
  clone.querySelectorAll('[srcset]').forEach((n) => n.setAttribute('srcset', n.getAttribute('srcset').split(',').map((p) => {
    const a = p.trim().split(/\s+/); a[0] = abs(a[0]); return a.join(' ');
  }).join(', ')));
  clone.querySelector('head').insertAdjacentHTML('beforeend', parts.map((p) => (p.href
    ? '<link rel="stylesheet" href="' + p.href + '">'
    : '<style' + (p.media ? ' media="' + p.media + '"' : '') + '>' + p.css.replace(/<\/style/gi, '<\\/style') + '</style>')).join('\n'));
  // As the kit's snapshot.js does: every query or fragment carrying a signing parameter is cut out
  // wherever the URL sits (any attribute, an inline style's url(), text), then each REDACT pattern
  // (always global) runs over every text node and attribute value, where entities are decoded (a
  // &nbsp; is a character \s matches), and again over the serialised copy.
  // A query runs to whitespace, a quote, an angle bracket, a CSS { or }, or a ; that starts a CSS
  // declaration (`;name:`), so a match that starts at a colour's # stops before a later declaration's
  // url(); any other ; (an &amp; entity, a ;-separated query) stays inside, as do commas and
  // parentheses, except a ")" that closes an unquoted url( ... ) before ; , } or the end.
  const cutSigned = (s) => s.replace(/[?#](?:[^\s"'<>);{}]|;(?![\w-]+\s*:)|\)(?![\s;,"'}]|$))*/g, (q) => (SIGNED.test(q) ? '' : q));
  const cutSignedUrl = (s) => s.replace(/[?#](?:[^\s"'<>);{}]|;|\)(?![\s"'}]|$))*/g, (q) => (SIGNED.test(q) ? '' : q));
  clone.querySelectorAll('*').forEach((n) => { for (const a of [...n.attributes]) { const v = (a.name === 'style' ? cutSigned : cutSignedUrl)(a.value); if (v !== a.value) n.setAttribute(a.name, v); } });
  const rx = REDACT.replace.map(([pattern, flags, rep]) => [new RegExp(pattern, flags.includes('g') ? flags : flags + 'g'), rep]);
  const scrub = (v) => rx.reduce((t, [r, rep]) => t.replace(r, rep), v);
  const tw = document.createTreeWalker(clone, NodeFilter.SHOW_TEXT | NodeFilter.SHOW_COMMENT);
  while (tw.nextNode()) { const v = scrub(tw.currentNode.nodeValue); if (v !== tw.currentNode.nodeValue) tw.currentNode.nodeValue = v; }
  clone.querySelectorAll('*').forEach((n) => { for (const a of [...n.attributes]) { const v = scrub(a.value); if (v !== a.value) n.setAttribute(a.name, v); } });
  let html = cutSigned('<!doctype html>\n' + clone.outerHTML);
  for (const [r, rep] of rx) html = html.replace(r, rep);
  const meta = { label, url: cutSigned(location.href), title: document.title, scrollY, w: innerWidth, h: innerHeight, docH: document.documentElement.scrollHeight };
  return 'SNAPSTART' + JSON.stringify(meta) + 'SNAPMETA' + html + 'SNAPEND';
};
