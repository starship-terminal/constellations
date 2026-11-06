// The form a page URL is recorded in under raw/: origin and path only (a query or fragment can
// carry a signed credential, a search, an email), and every path segment that is not a plain
// route word masked as <id>, since ids and title slugs name the owner's own conversations,
// documents and projects. So https://app.example/chat/1f2e-77?q=x#m becomes
// https://app.example/chat/<id>. Favours masking: a route word is lowercase letters with at most
// one - or _ inside, 20 characters at most. Plain JavaScript, so a page.evaluate can carry it too.
export function safeUrl(u) {
  let x;
  try { x = new URL(u); } catch { return '<url>'; }
  if (x.protocol === 'file:') return 'file:///<local file>';   // a local path names the owner's home folder
  const base = x.origin !== 'null' ? x.origin : `${x.protocol}//${x.host}`;
  const seg = (s) => (!s || (/^[a-z]+(?:[-_][a-z]+)?$/.test(s) && s.length <= 20) ? s : '<id>');
  return base + x.pathname.split('/').map(seg).join('/');
}
