"use client";

// The refero index surface: hero + search, facet filters and the card grid,
// ported from docs/gallery/app.js's refero section. Facet words in the query
// score double; a hover held 200ms mounts the card's preview video; every
// image tries the local mirror first and falls back to the remote CDN.
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import { reducedMotion, scrollBehavior } from "@/components/motion";
import { useUrlMirror } from "@/components/url-state";
import { useSlashFocus } from "@/components/keys";
import { scoreRow, terms, type Facet } from "@/lib/search";
import { cardFav, cardImg, cardVideo, type MediaPair as Media } from "@/lib/refero-media";
import { useEffect, useMemo, useRef, useState } from "react";
import type { ReferoCard, ReferoIndex as ReferoIndexData } from "@/lib/refero";

const PAGE = 48;
const HOVER_MS = 200;
const PROMPTS = [
  "Dark mode SaaS",
  "Warm paper",
  "Brutalist portfolio",
  "Editorial agency",
  "Neon crypto",
  "Minimal devtools",
  "Cinematic media",
  "Swiss fintech",
];
type FacetKey = "theme" | "type" | "style" | "industry";

const hayOf = (s: ReferoCard) =>
  [s.name, s.slug, s.tagline, s.industry, s.src, s.type, s.style, ...s.tags].join(" ").toLowerCase();

// Image with the local-first/remote-fallback dance; removes itself when both
// sources fail so tiles degrade to the letter placeholder or panel colour.
export function RfImg({ media, alt = "", className, onLoad }: {
  media: Media;
  alt?: string;
  className?: string;
  onLoad?: (e: React.SyntheticEvent<HTMLImageElement>) => void;
}) {
  const [failed, setFailed] = useState(false);
  const img = useRef<HTMLImageElement | null>(null);
  const src = media.local || media.remote;
  // Move to the remote copy once, then give up so the tile shows its letter
  // or panel colour instead of a broken-image icon.
  const fail = (el: HTMLImageElement) => {
    if (media.remote && el.src !== media.remote) el.src = media.remote;
    else setFailed(true);
  };
  // A server-rendered image can fail before React attaches onError, and the
  // event is gone by then: look at its state once on mount.
  useEffect(() => {
    const el = img.current;
    if (el && el.complete && el.naturalWidth === 0) fail(el);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);
  if (!src || failed) return null;
  return (
    // eslint-disable-next-line @next/next/no-img-element
    <img
      ref={img}
      className={className}
      src={src}
      alt={alt}
      loading="lazy"
      decoding="async"
      onLoad={onLoad}
      onError={(e) => fail(e.currentTarget)}
    />
  );
}

export function RfFav({ media, name, big }: { media: Media; name: string | null; big?: boolean }) {
  return (
    <span className={`rf-fav${big ? " big" : ""}`}>
      <i>{(name || "?")[0].toUpperCase()}</i>
      <RfImg media={media} />
    </span>
  );
}

function Card({ index, s }: { index: ReferoIndexData; s: ReferoCard }) {
  const [wantVideo, setWantVideo] = useState(false);
  const [auraOn, setAuraOn] = useState(false);
  const timer = useRef<ReturnType<typeof setTimeout> | null>(null);
  const vid = useRef<HTMLVideoElement | null>(null);
  const video = useMemo(() => cardVideo(index, s), [index, s]);

  const enter = () => {
    if (!s.video || reducedMotion()) return;
    if (wantVideo) {
      vid.current?.play().catch(() => {});
      return;
    }
    if (!timer.current) timer.current = setTimeout(() => !reducedMotion() && setWantVideo(true), HOVER_MS);
  };
  const leave = () => {
    if (timer.current) {
      clearTimeout(timer.current);
      timer.current = null;
    }
    const v = vid.current;
    if (v) {
      v.pause();
      v.classList.remove("on");
    }
  };

  return (
    <Link className="rf-card" href={`/refero/${encodeURIComponent(s.slug)}`} onMouseEnter={enter} onMouseLeave={leave}>
      <div className="rf-tile">
        <RfImg media={cardImg(index, s)} className={`rf-aura${auraOn ? " on" : ""}`} onLoad={() => setAuraOn(true)} />
        <div className="rf-shot">
          <RfImg media={cardImg(index, s)} alt={`${s.name || s.slug} screenshot`} />
          {wantVideo && (
            <video
              ref={(v) => {
                vid.current = v;
                if (!reducedMotion()) v?.play().catch(() => {});
              }}
              src={video.local || video.remote || undefined}
              muted
              loop
              playsInline
              preload="none"
              onCanPlay={(e) => {
                // Checked at every start, so a preference turned on after
                // the hover began still stops a late load from playing.
                if (!reducedMotion()) e.currentTarget.play().catch(() => {});
              }}
              onPlaying={(e) => e.currentTarget.classList.add("on")}
              onError={(e) => {
                const v = e.currentTarget;
                if (video.remote && v.src !== video.remote) v.src = video.remote;
              }}
            />
          )}
        </div>
      </div>
      <div className="rf-card-foot">
        <RfFav media={cardFav(index, s)} name={s.name} />
        <div className="rf-card-txt">
          <h3>{s.name || s.slug}</h3>
          <p>{s.tagline || ""}</p>
          <span className="rf-card-chips">
            {[...new Set([s.theme, s.industry, s.type].filter(Boolean))].map((c) => (
              <span key={c}>{c}</span>
            ))}
          </span>
        </div>
      </div>
    </Link>
  );
}

export function ReferoIndex({ index }: { index: ReferoIndexData }) {
  const params = useSearchParams();
  const [q, setQ] = useState(params.get("q") || "");
  const [theme, setTheme] = useState(params.get("theme") || "all");
  const [type, setType] = useState(params.get("type") || "all");
  const [style, setStyle] = useState(params.get("style") || "all");
  const [industry, setIndustry] = useState(params.get("industry") || "all");
  const [videoOnly, setVideoOnly] = useState(params.get("video") === "1");
  const [tagSet, setTagSet] = useState<Set<string>>(
    () => new Set((params.get("tag") || "").split(",").filter(Boolean)),
  );
  const [shown, setShown] = useState(PAGE);
  const [filtersReady, setFiltersReady] = useState(false);
  const qRef = useRef<HTMLInputElement>(null);
  const sentRef = useRef<HTMLDivElement>(null);
  const gridTop = useRef<HTMLDivElement>(null);

  // Saved filters survive navigation, matching the gallery index's habit.
  useEffect(() => {
    try {
      const s = JSON.parse(localStorage.getItem("ds-refero") || "{}");
      if (!params.get("theme") && s.theme) setTheme(s.theme);
      if (!params.get("type") && s.type) setType(s.type);
      if (!params.get("style") && s.style) setStyle(s.style);
      if (!params.get("industry") && s.industry) setIndustry(s.industry);
      if (!params.get("video") && s.video) setVideoOnly(true);
      if (!params.get("tag") && Array.isArray(s.tags)) setTagSet(new Set(s.tags));
    } catch {}
    // Rendered together with the restored filters, so the saved-view check
    // below compares against them and not the URL-only first render.
    setFiltersReady(true);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useSlashFocus(qRef);
  useUrlMirror({
    q: q.trim() || null,
    theme: theme === "all" ? null : theme,
    type: type === "all" ? null : type,
    style: style === "all" ? null : style,
    industry: industry === "all" ? null : industry,
    video: videoOnly ? "1" : null,
    tag: [...tagSet].join(",") || null,
  });

  const save = (patch: object) => {
    try {
      const s = JSON.parse(localStorage.getItem("ds-refero") || "{}");
      localStorage.setItem("ds-refero", JSON.stringify({ ...s, ...patch }));
    } catch {}
  };

  const counts = useMemo(() => {
    const out: Record<FacetKey | "tag", Map<string, number>> = {
      theme: new Map(),
      type: new Map(),
      style: new Map(),
      industry: new Map(),
      tag: new Map(),
    };
    for (const s of index.styles) {
      for (const k of ["theme", "type", "style", "industry"] as const) {
        const v = s[k];
        if (v) out[k].set(v, (out[k].get(v) || 0) + 1);
      }
      for (const t of s.tags) out.tag.set(t, (out.tag.get(t) || 0) + 1);
    }
    return out;
  }, [index]);

  const sorted = (m: Map<string, number>) =>
    [...m.entries()].sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]));

  const toks = useMemo(() => terms(q), [q]);
  const facets = useMemo<Facet<ReferoCard>[]>(
    () => [
      [new Set(counts.style.keys()), (s, t) => s.style === t],
      [new Set(counts.type.keys()), (s, t) => s.type === t],
      [new Set(counts.industry.keys()), (s, t) => s.industry === t],
      [new Set(["dark", "light", "mixed"]), (s, t) => s.theme === t],
    ],
    [counts],
  );
  const hay = useMemo(() => new Map(index.styles.map((s) => [s.slug, hayOf(s)])), [index]);

  const list = useMemo(() => {
    const scored = index.styles
      .filter(
        (s) =>
          (theme === "all" || s.theme === theme) &&
          (type === "all" || s.type === type) &&
          (style === "all" || s.style === style) &&
          (industry === "all" || s.industry === industry) &&
          (!videoOnly || s.video) &&
          (tagSet.size === 0 || [...tagSet].every((t) => s.tags.includes(t))),
      )
      .map((s) => [scoreRow(s, hay.get(s.slug) || "", toks, facets), s] as const)
      .filter(([sc]) => sc > 0);
    if (toks.length) scored.sort((a, b) => b[0] - a[0]);
    return scored.map(([, s]) => s);
  }, [index, theme, type, style, industry, videoOnly, tagSet, toks, facets, hay]);

  // How far the grid was scrolled in, kept for this tab so Back from a style
  // returns to the same cards rather than the first page at the top.
  const viewKey = JSON.stringify([q.trim(), theme, type, style, industry, videoOnly, [...tagSet].sort()]);
  const restore = useRef<{ shown: number; y: number } | null>(null);
  const firstView = useRef(true);
  useEffect(() => {
    if (!filtersReady) return;
    if (firstView.current) {
      firstView.current = false;
      try {
        const v = JSON.parse(sessionStorage.getItem("ds-refero-view") || "null");
        if (v && v.key === viewKey && v.shown > PAGE) {
          setShown(v.shown);
          if (typeof v.y === "number") restore.current = { shown: v.shown, y: v.y };
          return;
        }
      } catch {}
    }
    setShown(PAGE);
  }, [viewKey, filtersReady]);
  useEffect(() => {
    // Scroll once the saved number of cards has rendered; earlier, the page
    // is too short and the browser would clamp the position.
    const r = restore.current;
    if (!r || shown < r.shown) return;
    restore.current = null;
    window.scrollTo(0, r.y);
  }, [shown]);
  useEffect(() => {
    // Nothing is saved until the saved view has been read and restored.
    if (!filtersReady || restore.current) return;
    const keep = () => {
      try {
        sessionStorage.setItem("ds-refero-view", JSON.stringify({ key: viewKey, shown, y: window.scrollY }));
      } catch {}
    };
    let timer = 0;
    const onScroll = () => {
      window.clearTimeout(timer);
      timer = window.setTimeout(keep, 120);
    };
    keep();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => {
      window.clearTimeout(timer);
      window.removeEventListener("scroll", onScroll);
    };
  }, [viewKey, shown, filtersReady]);

  const hasMore = shown < list.length;
  useEffect(() => {
    const el = sentRef.current;
    if (!el || !hasMore) return;
    const io = new IntersectionObserver(
      (es) => {
        if (es[0].isIntersecting) setShown((n) => n + PAGE);
      },
      { rootMargin: "900px" },
    );
    io.observe(el);
    return () => io.disconnect();
  }, [hasMore, list.length]);

  const prompt = (label: string) => {
    setTheme("all");
    setType("all");
    setStyle("all");
    setIndustry("all");
    setVideoOnly(false);
    setTagSet(new Set());
    setQ(label);
    save({ theme: "", type: "", style: "", industry: "", video: false, tags: [] });
    gridTop.current?.scrollIntoView({ behavior: scrollBehavior(), block: "start" });
  };

  const sel = (key: FacetKey, first: string, value: string, set: (v: string) => void) => (
    <select
      className="rf-sel"
      aria-label={first}
      value={value}
      onChange={(e) => {
        set(e.target.value);
        save({ [key]: e.target.value });
      }}
    >
      <option value="all">{first}</option>
      {sorted(counts[key]).map(([v, n]) => (
        <option key={v} value={v}>
          {v} ({n})
        </option>
      ))}
    </select>
  );

  return (
    <div className="page">
      <div className="rf-hero">
        <div className="rf-beta">
          <a className="pill" href="https://styles.refero.design" target="_blank" rel="noopener">
            Refero
          </a>
          <p>
            <span className="dot" aria-hidden="true" />
            {index.styles.length.toLocaleString("en")} styles · interpreted, not measured
          </p>
        </div>
        <h1>
          <em>Every site,</em> in DESIGN.md
        </h1>
        <p className="rf-sub">
          A third-party snapshot of {index.styles.length.toLocaleString("en")} styles interpreted by{" "}
          <a href="https://styles.refero.design" target="_blank" rel="noopener">
            styles.refero.design
          </a>
          . Lower confidence than the measured library — here for breadth; the{" "}
          <Link href="/gallery">systems gallery</Link> is the source of truth.
        </p>
        <div className="rf-search">
          <label className="field">
            <svg width="14" height="14" viewBox="0 0 16 16" aria-hidden="true">
              <circle cx="7" cy="7" r="5" fill="none" stroke="currentColor" strokeWidth="1.6" />
              <path d="M11 11l3.5 3.5" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" />
            </svg>
            <input
              ref={qRef}
              type="search"
              placeholder="Search DESIGN.md examples"
              autoComplete="off"
              aria-label="Search refero styles"
              value={q}
              onChange={(e) => setQ(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter") gridTop.current?.scrollIntoView({ behavior: scrollBehavior() });
                if (e.key === "Escape") {
                  setQ("");
                  e.currentTarget.blur();
                }
              }}
            />
            <kbd>/</kbd>
          </label>
          <button className="go" type="button" aria-label="Search" onClick={() => qRef.current?.focus()}>
            <svg
              viewBox="0 0 16 16"
              width="15"
              height="15"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <path d="M8 13V3M3.5 7.5 8 3l4.5 4.5" />
            </svg>
          </button>
        </div>
        <div className="rf-chips">
          {PROMPTS.map((label) => (
            <button key={label} type="button" onClick={() => prompt(label)}>
              <i>↳</i>
              {label}
            </button>
          ))}
        </div>
      </div>

      <div className="rf-bar-row" ref={gridTop}>
        <div className="rf-tabs-list">
          <button
            type="button"
            aria-pressed={theme === "all"}
            onClick={() => {
              setTheme("all");
              save({ theme: "all" });
            }}
          >
            All themes
          </button>
          {sorted(counts.theme).map(([v, n]) => (
            <button
              key={v}
              type="button"
              aria-pressed={theme === v}
              onClick={() => {
                setTheme(v);
                save({ theme: v });
              }}
            >
              {v[0].toUpperCase() + v.slice(1)}
              <span className="n">{n}</span>
            </button>
          ))}
          <button
            type="button"
            aria-pressed={videoOnly}
            onClick={() => {
              setVideoOnly(!videoOnly);
              save({ video: !videoOnly });
            }}
          >
            Has video
          </button>
        </div>
        {sel("type", "All types", type, setType)}
        {sel("style", "All styles", style, setStyle)}
        {sel("industry", "All industries", industry, setIndustry)}
        <span className="count">
          {list.length.toLocaleString("en")} style{list.length === 1 ? "" : "s"}
        </span>
      </div>

      <div className="subfilters">
        {sorted(counts.tag).map(([t, n]) => (
          <button
            key={t}
            className="chip"
            aria-pressed={tagSet.has(t)}
            onClick={() => {
              const next = new Set(tagSet);
              if (next.has(t)) next.delete(t);
              else next.add(t);
              setTagSet(next);
              save({ tags: [...next] });
            }}
          >
            {t}
            <span className="n">{n}</span>
          </button>
        ))}
      </div>

      <div className="rf-wrap">
        {!list.length ? (
          <p className="empty">No style matches. Clear the search or filters.</p>
        ) : (
          <>
            <div className="rf-grid">
              {list.slice(0, shown).map((s) => (
                <Card key={s.slug} index={index} s={s} />
              ))}
            </div>
            {hasMore && (
              <div className="more" ref={sentRef}>
                <button className="btn" type="button" onClick={() => setShown((n) => n + PAGE)}>
                  Load more
                </button>
              </div>
            )}
          </>
        )}
      </div>
    </div>
  );
}
