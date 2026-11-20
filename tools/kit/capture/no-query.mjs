// Queries cut out of URLs that sit in recorded text (custom property values, selectors), where no url()
// wraps them so noUrl cannot see them. A query or fragment can carry a signed credential or an account
// id. Covered: absolute URLs (https://...), scheme-relative ones (//cdn.example/...), and relative paths
// (/a/b.png, avatar.png) with a query. A URL-shaped token starts a value or follows a space, a quote, a
// bracket, a comma or =. Plain JavaScript; tested in test_no_query.mjs.
const ABS = /(\bhttps?:\/\/|(?:^|(?<=[\s"'(,=]))\/\/)([^\s"'?#]*)[?#][^\s"']*/gi;
const REL = /(?:^|(?<=[\s"'(,=]))([\w.~%@+-]*[/.][^\s"'(),?#]*)\?[^\s"')]*/g;

export const noQuery = (v) => (typeof v === 'string' ? v.replace(ABS, '$1$2').replace(REL, '$1') : v);

// Every string in a recorded object, keys included, through noQuery.
export function scrubQueries(x) {
  if (typeof x === 'string') return noQuery(x);
  if (Array.isArray(x)) return x.map(scrubQueries);
  if (x && typeof x === 'object') return Object.fromEntries(Object.entries(x).map(([k, v]) => [noQuery(k), scrubQueries(v)]));
  return x;
}
