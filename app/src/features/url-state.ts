/** pathname + optional ?query + hash, so a filter change never drops the #anchor the reader is on. */
export function searchHref(
  pathname: string,
  params: URLSearchParams,
  hash = "",
): string {
  const search = params.toString();
  return `${pathname}${search ? `?${search}` : ""}${hash}`;
}
/**
 * Replace the current URL's query in place. Native history keeps
 * useSearchParams in sync without a server navigation that could restore an
 * older search over newer typing.
 */
export function replaceSearch(
  params: URLSearchParams,
  pathname = window.location.pathname,
): void {
  window.history.replaceState(
    null,
    "",
    searchHref(pathname, params, window.location.hash),
  );
}
