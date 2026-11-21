// Queries cut out of URLs that sit in recorded text (custom property values, selectors), where no url()
// wraps them so noUrl cannot see them. A query, or a fragment that carries parameters, can hold a signed
// credential or an account id. Plain JavaScript; tested in test_no_query.mjs.
//
// The rule fails closed: it does not try to recognise what a URL looks like (every shape it missed
// leaked). The text is split into delimited spans, and a span loses everything from the point where a
// query could start to its end:
//   - a URL-valued field (the quoted or unquoted body of url( ), or a quoted value of a src, href,
//     srcset, poster, action, data or xlink:href attribute selector) holds a URL, so everything from its
//     first ? goes (a field needs no = after it), and from its # when the fragment carries = or &.
//   - any other quoted text, and the text outside quotes and url( ) (the whole value), is free text: it
//     is cut from the first ? that has an = after it before the span ends, or from a # whose name runs
//     into = or &, whatever comes before it.
// "?", "=", "#" and "&" are matched in every spelling the formats allow (CSS escapes, HTML character
// references, percent-encoding), so "/avatar\3f token=…" or "&#63;" is a query like "?"; see spell().
// A data: URL (bare, quoted or in url( )) is left alone, = padding and all; quoted, it ends at a list's
// ", " (srcset="data:… 1x, /b.png?sig=… 2x" still cuts the second URL), and only where data: opens
// a value: at its start or after a space, a quote, a bracket, a comma or = ("/x/data:a.png" is a path).
// A bare one runs through any quoted text inside it and ends at the first unquoted space.
//
// What it over-cuts, knowingly: a quoted data: URL whose own payload holds ", " and a later ?…= loses
// that tail; prose with a ? followed later by an = loses its tail ("What? a=b" keeps
// "What"); a bare image-set() or srcset in free text loses everything after its first query, closing
// bracket included; a quoted srcset keeps only its first URL; an unquoted attribute selector
// (img[src=/a?sig=1]) loses its closing ]; a percent-encoded %3f, a literal in a URL path, is cut as a
// query; a literal backslash followed by 3f (CSS "\\3f") is cut too; and "&amp;#63;…=" loses its tail
// to the fragment rule (its literal # runs into an =).

const FIELD = /(?:\[\s*(?:src|href|srcset|poster|action|data|xlink:href)\s*[~|^$*]?=\s*)$/i;
const DATA = /^\s*data:/i;
const DATA_OPENS = (before) => !before || /[\s"'(,=]/.test(before);   // data: here starts a data: URL

// Splits a value into outer text, quoted strings, url( ) bodies and bare data: tokens.
function scan(s) {
  const out = [];
  let outer = '';
  const flush = () => { if (outer) out.push({ kind: 'outer', text: outer }); outer = ''; };
  const quoteEnd = (i) => {   // index of the quote closing the one at i, or s.length
    for (let j = i + 1; j < s.length; j++) {
      if (s[j] === '\\') j++;
      else if (s[j] === s[i]) return j;
    }
    return s.length;
  };
  for (let i = 0; i < s.length;) {
    const before = i ? s[i - 1] : '';
    if (/^url\(/i.test(s.slice(i, i + 4)) && !/[\w-]/.test(before)) {
      let j = i + 4, depth = 1;
      for (; j < s.length; j++) {
        if (s[j] === '"' || s[j] === "'") j = quoteEnd(j);
        else if (s[j] === '(') depth++;
        else if (s[j] === ')' && --depth === 0) break;
      }
      flush();
      out.push({ kind: 'url', open: s.slice(i, i + 4), body: s.slice(i + 4, j), close: j < s.length ? ')' : '' });
      i = j + 1;
    } else if (s[i] === '"' || s[i] === "'") {
      const j = quoteEnd(i);
      const field = FIELD.test(outer);
      flush();
      out.push({ kind: 'quoted', quote: s[i], text: s.slice(i + 1, j), close: j < s.length ? s[i] : '', field });
      i = j + 1;
    } else if (/^data:/i.test(s.slice(i, i + 5)) && DATA_OPENS(before)) {
      const m = s.slice(i).match(/^data:(?:"[^"]*"|'[^']*'|[^\s"'])*/i);
      flush();
      out.push({ kind: 'data', text: m[0] });
      i += m[0].length;
    } else outer += s[i++];
  }
  flush();
  return out;
}

// Every spelling of "?", "=" and "#" the recorded formats allow, since a query written with escapes is
// still a query once the CSS or the HTML is read: the plain character, a CSS escape (\? or \3f with 1 to
// 6 hex digits, any case, and its optional single trailing space), an HTML character reference (&#63;,
// &#x3f; with any leading zeros, or the named one) and percent-encoding (%3f, strictly a literal in a
// path, cut anyway: fail closed). Doubly encoded forms are not these characters in any one layer and
// stay as they are: "%253f" is "%3f" after one decode, and "&amp;#63;" is "&#63;".
const SP = '(?:\\r\\n|[ \\t\\n\\r\\f])?';   // a hex escape's optional trailing whitespace
const spell = (ch, hex, dec, named) => {
  const lit = '\\' + ch;   // the character itself, escaped for the pattern
  return new RegExp([lit, `\\\\0{0,4}${hex}${SP}`, `\\\\${lit}`, `&#0*${dec};`, `&#x0*${hex};`, `&${named};`, `%${hex}`].join('|'), 'i');
};
const Q = spell('?', '3f', 63, 'quest');
const E = spell('=', '3d', 61, 'equals');
const H = spell('#', '23', 35, 'num');
const AMP = /&(?!#|[a-z]+;)|&amp;|&#0*38;|&#x0*26;|\\0{0,4}26(?:\r\n|[ \t\n\r\f])?|\\&|%26/i;
const at = (re, text, i) => { const m = re.exec(text.slice(i)); return m && m.index === 0 ? m[0].length : 0; };
const firstAt = (re, text) => { const m = re.exec(text); return m ? m.index : -1; };

// A fragment carries a parameter when it holds an "=" or an "&" in any spelling: anywhere in a URL field
// (the whole field is the URL, spaces and all), and in free text before the next space or quote.
const fragmentParams = (frag, whole = false) => {
  const word = whole ? frag : frag.match(/^[^\s"']*/)[0];
  return E.test(word) || AMP.test(word);
};

// A URL-valued field: everything from its first "?" in any spelling goes (a field holds a URL, so that is
// its query), and its fragment when the fragment carries a parameter.
function cutField(v) {
  if (DATA.test(v)) return v;
  const q = firstAt(Q, v);
  let h = -1;
  for (let i = 0; i < v.length && (q < 0 || i < q); i++) {
    const n = at(H, v, i);
    if (n && fragmentParams(v.slice(i + n), true)) { h = i; break; }
  }
  const cut = h >= 0 ? h : q;
  return cut < 0 ? v : v.slice(0, cut);
}

// The first point in free text a query could start: a "?" (any spelling) with an "=" (any spelling)
// after it in `rest` (the text from there to the end of the span), or a "#" whose name runs into "=" or
// "&". data: tokens are skipped.
function freeCut(text, restAfter = '') {
  const skip = [...text.matchAll(/(?<=^|[\s"'(,=])data:\S*/gi)].map((m) => [m.index, m.index + m[0].length]);
  const inData = (i) => skip.some(([a, b]) => i >= a && i < b);
  for (let i = 0; i < text.length; i++) {
    if (inData(i)) continue;
    const q = at(Q, text, i);
    if (q && E.test(text.slice(i + q) + restAfter)) return i;
    const h = at(H, text, i);
    if (h && fragmentParams(text.slice(i + h))) return i;
  }
  return -1;
}

const cutFree = (v) => { const at = freeCut(v); return at < 0 ? v : v.slice(0, at); };

function cutUrlBody(body) {
  const m = body.match(/^(\s*)(["'])([\s\S]*?)(\2?)(\s*)$/);
  if (m) return DATA.test(m[3]) ? body : m[1] + m[2] + cutField(m[3]) + m[4] + m[5];
  if (DATA.test(body)) return body;
  const lead = body.match(/^\s*/)[0], trail = body.match(/\s*$/)[0];
  return lead + cutField(body.trim()) + trail;
}

const render = (p) => (p.kind === 'url' ? p.open + p.body + p.close : p.kind === 'quoted' ? p.quote + p.text + p.close : p.text);

export const noQuery = (v) => {
  if (typeof v !== 'string') return v;
  const parts = scan(v).map((p) => {
    if (p.kind === 'url') return { ...p, body: cutUrlBody(p.body) };
    if (p.kind === 'quoted') {
      const cut = p.field ? cutField : cutFree;
      if (!DATA.test(p.text)) return { ...p, text: cut(p.text) };
      // A data: URL first in a quoted list (a srcset, an image-set) ends at the list's ", ": what follows
      // is cut like any other value, so a data: URL in front does not shield a signed URL behind it.
      const end = p.text.search(/,\s/);
      return end < 0 ? p : { ...p, text: p.text.slice(0, end) + cut(p.text.slice(end)) };
    }
    return p;
  });
  // Outer text is one span, the whole value: from a query start in it, the rest of the value goes.
  let out = '';
  for (let k = 0; k < parts.length; k++) {
    const p = parts[k];
    if (p.kind === 'outer') {
      const at = freeCut(p.text, parts.slice(k + 1).map(render).join(''));
      if (at >= 0) return out + p.text.slice(0, at);
    }
    out += render(p);
  }
  return out;
};

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

// Every line a capture script prints goes through noQuery, and so does an error that ends the run: a
// package commits its capture logs (raw/*.log), and a Playwright error quotes the locator it failed on
// and, on navigation, the page URL, query and all. Call it once, before the script launches a browser.
export function scrubConsole() {
  const clean = (x) => (typeof x === 'string' ? noQuery(x) : x instanceof Error ? noQuery(x.stack || String(x)) : x);
  for (const k of ['log', 'info', 'warn', 'error']) {
    const write = console[k].bind(console);
    console[k] = (...args) => write(...args.map(clean));
  }
  const die = (e) => { console.error(e instanceof Error ? e : String(e)); process.exit(1); };
  process.on('uncaughtException', die);
  process.on('unhandledRejection', die);
}
