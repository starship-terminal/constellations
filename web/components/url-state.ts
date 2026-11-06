"use client";

// Mirror a listing's search and filters into the address bar, so a reload,
// a shared link or Back lands on the same results. replaceState keeps typing
// out of the history stack; Next's router picks the change up as well.
import { useEffect, useRef } from "react";

/** Write `entries` into the current URL's query; a null or "" value removes
    the key (callers pass null for a filter's default). Debounced so typing
    does not hit the browsers' replaceState rate limits, and flushed before
    any click (opening a result) or page hide, so a quick click still leaves
    the latest search on the history entry Back returns to. */
export function useUrlMirror(entries: Record<string, string | null>, delay = 250) {
  const key = JSON.stringify(entries);
  const pending = useRef<(() => void) | null>(null);

  useEffect(() => {
    const write = () => {
      pending.current = null;
      const url = new URL(window.location.href);
      for (const [k, v] of Object.entries(JSON.parse(key) as Record<string, string | null>)) {
        if (v) url.searchParams.set(k, v);
        else url.searchParams.delete(k);
      }
      if (url.href === window.location.href) return;
      try {
        window.history.replaceState(window.history.state, "", url);
      } catch {}
    };
    pending.current = write;
    const t = window.setTimeout(write, delay);
    return () => {
      window.clearTimeout(t);
      if (pending.current === write) pending.current = null;
    };
  }, [key, delay]);

  useEffect(() => {
    // Capture on document runs before React's own click handlers, so this
    // lands before a Link or router.push adds the next history entry.
    const flush = () => pending.current?.();
    document.addEventListener("click", flush, true);
    window.addEventListener("pagehide", flush);
    return () => {
      document.removeEventListener("click", flush, true);
      window.removeEventListener("pagehide", flush);
    };
  }, []);
}
