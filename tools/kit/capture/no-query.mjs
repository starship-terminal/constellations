// Queries cut out of URLs that sit in recorded text (custom property values, selectors), where no url()
// wraps them so noUrl cannot see them. A query, or a fragment that carries parameters, can hold a signed
// credential or an account id. Plain JavaScript; tested in test_no_query.mjs.
//
// Where a URL ends is decided by its context, never by guessing which characters a query may hold:
//   - inside quotes, it ends at its own closing quote: a quoted value that starts with a URL is that
//     URL, so a space inside the quotes does not end it (a srcset-style list loses what follows its
//     first query, never keeps a query);
//   - inside an unquoted url( ), it ends at the ) that closes the url( (CSS allows no ) in it);
//   - bare, it ends at the next space or quote, and a closing ) or ] at the very end is given back
//     only when the part of the token that is kept opened it.
// Within that span everything from the first ? is cut; for an absolute or scheme-relative URL from the
// first #, for a relative one from a # whose fragment holds a parameter (= or &), so icons.svg#close
// stays. A data: URL is left alone, quotes and spaces inside it included, and so is text whose part
// before ? does not look like a URL.

const SPAN = /(?<![\w.-])data:(?:"[^"]*"|'[^']*'|[^\s"'])*|(["'])((?:\\.|(?!\1)[^\\])*)\1|(url\(\s*)([^\s"')][^)\s]*)(\s*\))|[^\s"']+/gi;
const ABSOLUTE = /^(?:[a-z][a-z0-9+.-]*:)?\/\//i;
const URLISH = /^(?:[a-z][a-z0-9+.-]*:\/\/|\/\/|[\w.~%@+()[\]=,-]*[/.])/i;

// The index a URL-shaped text is cut at, or -1 to keep it whole.
function cutAt(u) {
  if (/^data:/i.test(u)) return -1;
  const q = u.indexOf('?');
  let h = u.indexOf('#');
  if (h >= 0 && !ABSOLUTE.test(u) && !/[=&]/.test(u.slice(h + 1))) h = -1;   // a plain fragment of a relative path
  const at = q < 0 ? h : h < 0 ? q : Math.min(q, h);
  if (at <= 0) return -1;
  return URLISH.test(u.slice(0, at)) ? at : -1;
}

// One whitespace-free piece whose end is fixed by its wrapper (a quote or url( )): cut, nothing given back.
const cutWhole = (u) => { const at = cutAt(u); return at < 0 ? u : u.slice(0, at); };

// A bare token: cut, then give back the closing brackets at its end that close what the kept part opened.
function cutBare(t) {
  // the URL starts at the token start or after a bracket, comma or = (image-set(/a.png?x, [src=/a?x])
  const starts = [0, ...[...t.matchAll(/[([,=]/g)].map((m) => m.index + 1)];
  for (const s of starts) {
    if (/^data:/i.test(t.slice(s))) return t;
    const at = cutAt(t.slice(s));
    if (at < 0) continue;
    const kept = t.slice(0, s + at);
    let open = 0;
    for (const ch of kept) open += ch === '(' || ch === '[' ? 1 : ch === ')' || ch === ']' ? -1 : 0;
    let back = '';
    for (let i = t.length - 1; open > 0 && i >= s + at && (t[i] === ')' || t[i] === ']'); i--, open--) back = t[i] + back;
    return kept + back;
  }
  return t;
}

export const noQuery = (v) => (typeof v === 'string'
  ? v.replace(SPAN, (m, quote, inner, urlOpen, urlBody, urlClose) => {
    if (/^data:/i.test(m)) return m;
    if (quote) return quote + cutWhole(inner) + quote;
    if (urlOpen) return urlOpen + cutWhole(urlBody) + urlClose;
    return cutBare(m);
  })
  : v);

// Two keys that clean to the same key are merged, never one dropped: counts add up (vars.mjs's
// counts.bySelector), objects merge the same way, lists join, and otherwise the first value stays.
const put = (o, k, value) => Object.defineProperty(o, k, { value, enumerable: true, writable: true, configurable: true });   // a __proto__ key stays a key
function merge(a, b) {
  if (typeof a === 'number' && typeof b === 'number') return a + b;
  if (Array.isArray(a) && Array.isArray(b)) return [...a, ...b];
  if (a && b && typeof a === 'object' && typeof b === 'object' && !Array.isArray(a) && !Array.isArray(b)) {
    const out = {};
    for (const [k, v] of Object.entries(a)) put(out, k, v);
    for (const [k, v] of Object.entries(b)) put(out, k, Object.prototype.hasOwnProperty.call(out, k) ? merge(out[k], v) : v);
    return out;
  }
  return a;
}

// Every string in a recorded object, keys included, through noQuery.
export function scrubQueries(x) {
  if (typeof x === 'string') return noQuery(x);
  if (Array.isArray(x)) return x.map(scrubQueries);
  if (x && typeof x === 'object') {
    const out = {};
    for (const [k, v] of Object.entries(x)) {
      const key = noQuery(k), val = scrubQueries(v);
      put(out, key, Object.prototype.hasOwnProperty.call(out, key) ? merge(out[key], val) : val);
    }
    return out;
  }
  return x;
}
