"use client";

// The media lightbox: stage with prev/next, a side rail with the owning
// package, tag chips that navigate back to a filtered listing, the palette,
// and download/copy/save actions. Saved paths persist in localStorage.
import Link from "next/link";
import { createContext, useCallback, useContext, useEffect, useRef, useState } from "react";
import { useToast } from "@/components/Toast";
import { copyWithToast } from "@/components/CopyButton";
import { readSavedPaths, writeSavedPaths } from "@/components/storage";

export interface LbItem {
  path: string; // resolved URL (/media/... or absolute)
  name: string;
  tags?: string[];
}
export interface LbSys {
  slug: string;
  name: string;
  icon?: string;
  category: string;
  categoryLabel: string;
  tags: string[];
  swatches: { role: string; value: string | null }[];
}
export interface LbOpts {
  sys?: LbSys | null;
  onTag?: (tag: string) => void;
  onSave?: () => void;
}
interface OpenArgs {
  items: LbItem[];
  index: number;
  opts?: LbOpts;
}
const Ctx = createContext<{ open: (a: OpenArgs) => void }>({ open: () => {} });

export const savedSet = (): Set<string> => new Set(readSavedPaths());

// Focusable controls that are actually rendered: a control inside a
// display:none rail has no layout boxes and must not take focus.
const visibleStops = () =>
  Array.from(document.querySelectorAll<HTMLElement>(".lightbox button:not([hidden]), .lightbox a[href]")).filter(
    (el) => el.getClientRects().length > 0,
  );

export function LightboxProvider({ children }: { children: React.ReactNode }) {
  const [state, setState] = useState<({ items: LbItem[]; index: number } & LbOpts) | null>(null);
  const opener = useRef<Element | null>(null);
  const { toast } = useToast();

  const open = useCallback((a: OpenArgs) => {
    opener.current = document.activeElement;
    setState({ items: a.items, index: a.index, sys: a.opts?.sys ?? null, onTag: a.opts?.onTag, onSave: a.opts?.onSave });
  }, []);
  const close = useCallback(() => {
    setState(null);
    if (opener.current instanceof HTMLElement && document.contains(opener.current)) opener.current.focus();
    opener.current = null;
  }, []);
  const step = useCallback(
    (d: number) => setState((s) => (s ? { ...s, index: (s.index + d + s.items.length) % s.items.length } : s)),
    [],
  );

  useEffect(() => {
    if (!state) return;
    document.body.style.overflow = "hidden";
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") close();
      if (e.key === "ArrowLeft") step(-1);
      if (e.key === "ArrowRight") step(1);
      if (e.key === "Tab") {
        const stops = visibleStops();
        if (!stops.length) return;
        const at = stops.indexOf(document.activeElement as HTMLElement);
        e.preventDefault();
        stops[(at + (e.shiftKey ? -1 : 1) + stops.length) % stops.length].focus();
      }
    };
    document.addEventListener("keydown", onKey);
    // Start on a Close that is on screen: the side rail (and its Close) is
    // hidden on narrow screens, where the stage carries its own.
    const stops = visibleStops();
    (stops.find((el) => el.matches(".lb-close")) ?? stops[0])?.focus();
    return () => {
      document.body.style.overflow = "";
      document.removeEventListener("keydown", onKey);
    };
  }, [state === null, close, step]);

  if (!state)
    return <Ctx.Provider value={{ open }}>{children}</Ctx.Provider>;

  const it = state.items[state.index];
  const sys = state.sys;
  const saved = typeof window !== "undefined" && savedSet().has(it.path);

  return (
    <Ctx.Provider value={{ open }}>
      {children}
      <div className="lightbox" role="dialog" aria-modal="true" aria-label="Screenshot viewer" onClick={(e) => { if (e.target === e.currentTarget) close(); }}>
        <div className="lb-stage" onClick={(e) => { if (e.target === e.currentTarget) close(); }}>
          <button className="lb-close lb-stage-close icon-btn" type="button" aria-label="Close" onClick={close}>
            ✕
          </button>
          <span className="lb-pos">
            {state.index + 1} / {state.items.length.toLocaleString()}
          </span>
          <figure>
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img src={it.path} alt={it.name} />
            <figcaption>
              {it.name}{" "}
              <a href={it.path} target="_blank" rel="noopener">
                Open original ↗
              </a>
            </figcaption>
          </figure>
          {state.items.length > 1 && (
            <div className="lb-nav">
              <button className="lb-prev icon-btn" type="button" aria-label="Previous" onClick={() => step(-1)}>
                ‹
              </button>
              <button className="lb-next icon-btn" type="button" aria-label="Next" onClick={() => step(1)}>
                ›
              </button>
            </div>
          )}
        </div>
        <aside className="lb-side">
          <div className="lb-app">
            {sys && (
              <Link className="lb-card" href={`/gallery/${sys.slug}`}>
                <span className="lb-card-icon">
                  {sys.icon ? (
                    /* eslint-disable-next-line @next/next/no-img-element */
                    <img src={sys.icon} alt="" />
                  ) : (
                    <i>{sys.name[0].toUpperCase()}</i>
                  )}
                </span>
                <span className="lb-card-txt">
                  <b>{sys.name}</b>
                  <small>{it.name}</small>
                </span>
              </Link>
            )}
            <button className="lb-close icon-btn" type="button" aria-label="Close" onClick={close}>
              ✕
            </button>
          </div>
          {!!it.tags?.length && (
            <div className="lb-sec">
              <h4>Tags</h4>
              <div className="lb-chips">
                {it.tags.map((t) => (
                  <button key={t} className="chip" onClick={() => { state.onTag?.(t); if (state.onTag) close(); }}>
                    {t}
                  </button>
                ))}
              </div>
            </div>
          )}
          {sys && (
            <div className="lb-sec">
              <h4>Style</h4>
              <div className="lb-chips">
                <Link className="chip" href={`/gallery?cat=${encodeURIComponent(sys.category)}`} onClick={close}>
                  {sys.categoryLabel}
                </Link>
                {sys.tags.map((t) => (
                  <Link key={t} className="chip" href={`/gallery?q=${encodeURIComponent(t)}`} onClick={close}>
                    {t}
                  </Link>
                ))}
              </div>
            </div>
          )}
          {!!sys?.swatches.length && (
            <div className="lb-sec">
              <h4>Colors</h4>
              <div className="lb-chips">
                {sys.swatches.slice(0, 10).map((x, i) =>
                  x.value ? (
                    <button key={i} className="chip lb-color" title={x.role} onClick={() => copyWithToast(x.value!, toast, `${x.value} copied`)}>
                      <i style={{ background: x.value }} />
                      {x.role}
                    </button>
                  ) : null,
                )}
              </div>
            </div>
          )}
          <div className="lb-actions">
            <a className="lb-btn" href={it.path} download>
              <svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round"><path d="M8 2v9m0 0 3.5-3.5M8 11 4.5 7.5M2 14h12"/></svg>
              Download
            </a>
            <button
              className="lb-btn"
              type="button"
              title="Copy link"
              aria-label="Copy link"
              onClick={() => copyWithToast(new URL(it.path, location.href).href, toast, "Link copied")}
            >
              <svg width="15" height="15" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"><rect x="5.5" y="5.5" width="8" height="8" rx="1.6"/><path d="M10.5 5.5v-2A1.5 1.5 0 0 0 9 2H3.5A1.5 1.5 0 0 0 2 3.5V9a1.5 1.5 0 0 0 1.5 1.5h2"/></svg>
            </button>
            <button
              className="lb-btn"
              type="button"
              aria-pressed={saved}
              onClick={() => {
                const s = savedSet();
                if (s.has(it.path)) s.delete(it.path);
                else s.add(it.path);
                writeSavedPaths(s);
                state.onSave?.();
                setState((cur) => (cur ? { ...cur } : cur));
              }}
            >
              <svg width="14" height="14" viewBox="0 0 16 16" fill={saved ? "currentColor" : "none"} stroke="currentColor" strokeWidth="1.5" strokeLinejoin="round"><path d="M3.5 2.5h9a1 1 0 0 1 1 1v10l-5.5-3.4L2.5 13.5v-10a1 1 0 0 1 1-1z"/></svg>
              {saved ? "Saved" : "Save"}
            </button>
          </div>
        </aside>
      </div>
    </Ctx.Provider>
  );
}

export const useLightbox = () => useContext(Ctx);
