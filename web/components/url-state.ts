"use client";

// Mirror a listing's search and filters into the address bar, so a reload,
// a shared link or Back lands on the same results. replaceState keeps typing
// out of the history stack; Next's router picks the change up as well.
import { useEffect } from "react";

/** Write `entries` into the current URL's query: null, "" or the facet's
    "all" default removes the key. Debounced so typing does not hit the
    browsers' replaceState rate limits. */
export function useUrlMirror(entries: Record<string, string | null>, delay = 250) {
  const key = JSON.stringify(entries);
  useEffect(() => {
    const t = window.setTimeout(() => {
      const url = new URL(window.location.href);
      for (const [k, v] of Object.entries(JSON.parse(key) as Record<string, string | null>)) {
        if (v && v !== "all") url.searchParams.set(k, v);
        else url.searchParams.delete(k);
      }
      if (url.href === window.location.href) return;
      try {
        window.history.replaceState(window.history.state, "", url);
      } catch {}
    }, delay);
    return () => window.clearTimeout(t);
  }, [key, delay]);
}
