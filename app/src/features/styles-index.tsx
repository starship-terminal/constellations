"use client";
import Link from "next/link";
import { Suspense, useEffect, useMemo, useRef, useState } from "react";
import { useSearchParams } from "next/navigation";
import { ArrowRight, ArrowUp, Search, X } from "lucide-react";
import type { LibraryItem } from "@/contracts/library";
import {
  api,
  Empty,
  ErrorState,
  SkeletonGrid,
  Spinner,
} from "@/components/shared";
import {
  loadLibraryPages,
  mergeLibraryItems,
  type LibraryResponse,
} from "./library-data";
import {
  filterStyles,
  orderStyles,
  styleCounts,
  type StyleFacet,
  type StyleFilters,
} from "./styles-data";
import styles from "./styles.module.css";

// Representative prompts observed on the live source. Queries use captured facets
// where the source's semantic search uses words absent from this local snapshot.
const PROMPTS = [
  ["Cinematic dark", "dark cinematic"],
  ["Non-boring enterprise", "corporate"],
  ["Cobalt blue billboard", "blue"],
  ["Chalk & charcoal", "monochrome"],
  ["Terminal & monospace", "technical devtools"],
  ["Huge serif headlines", "editorial"],
  ["Retro web nostalgia", "retro"],
  ["White with one accent", "light minimal"],
];
const HEADLINES = [
  "Your favorite sites, in DESIGN.md",
  "Start with a design you love",
  "A DESIGN.md your AI can follow",
  "Bring that style into your project",
];
function RotatingHeadline() {
  const [current, setCurrent] = useState(0),
    [transitioning, setTransitioning] = useState(false);
  useEffect(() => {
    const preference = matchMedia("(prefers-reduced-motion: reduce)");
    let cycle: ReturnType<typeof setInterval> | undefined;
    let settle: ReturnType<typeof setTimeout> | undefined;
    function configure() {
      clearInterval(cycle);
      clearTimeout(settle);
      setTransitioning(false);
      if (preference.matches) {
        setCurrent(0);
        return;
      }
      cycle = setInterval(() => {
        setTransitioning(true);
        settle = setTimeout(() => {
          setCurrent((index) => (index + 1) % HEADLINES.length);
          setTransitioning(false);
        }, 3000);
      }, 6000);
    }
    configure();
    preference.addEventListener("change", configure);
    return () => {
      clearInterval(cycle);
      clearTimeout(settle);
      preference.removeEventListener("change", configure);
    };
  }, []);
  return (
    <h1>
      <span className="sr-only">{HEADLINES[0]}</span>
      <span className={styles.headline} aria-hidden="true">
        {HEADLINES.map((phrase) => (
          <span
            key={phrase}
            className={`${styles.headlinePhrase} ${styles.headlineMeasure}`}
          >
            {phrase}
          </span>
        ))}
        <span className={styles.headlinePhrase}>
          <span
            className={`${styles.headlineText} ${transitioning ? styles.headlineOutgoing : ""}`}
          >
            {HEADLINES[current]}
          </span>
        </span>
        {transitioning && (
          <span className={styles.headlinePhrase}>
            <span
              className={`${styles.headlineText} ${styles.headlineIncoming}`}
            >
              {HEADLINES[(current + 1) % HEADLINES.length]}
            </span>
          </span>
        )}
      </span>
    </h1>
  );
}

export function StyleCard({ item }: { item: LibraryItem }) {
  const [playing, setPlaying] = useState(false);
  const [mounted, setMounted] = useState(false);
  const [imageSource, setImageSource] = useState(item.image);
  const [videoSource, setVideoSource] = useState(item.video);
  const [iconSource, setIconSource] = useState(item.icon);
  const video = useRef<HTMLVideoElement | null>(null);
  const timer = useRef<ReturnType<typeof setTimeout> | null>(null);
  const active = useRef(false);
  const start = () => {
    active.current = true;
    if (!item.video || matchMedia("(prefers-reduced-motion: reduce)").matches)
      return;
    if (mounted) video.current?.play().catch(() => {});
    else timer.current = setTimeout(() => setMounted(true), 200);
  };
  const stop = () => {
    active.current = false;
    if (timer.current) clearTimeout(timer.current);
    video.current?.pause();
    setPlaying(false);
  };
  useEffect(
    () => () => {
      if (timer.current) clearTimeout(timer.current);
    },
    [],
  );
  return (
    <Link
      className={styles.card}
      href={`/styles/refero/${item.slug}`}
      onMouseEnter={start}
      onMouseLeave={stop}
      onFocus={start}
      onBlur={stop}
    >
      <div className={styles.cardPicture}>
        <div className={styles.cardScreen}>
          {imageSource ? (
            <img
              src={imageSource}
              alt={`${item.name} style preview`}
              loading="lazy"
              decoding="async"
              onError={() =>
                setImageSource(
                  item.imageFallback && imageSource !== item.imageFallback
                    ? item.imageFallback
                    : null,
                )
              }
            />
          ) : (
            <span className={styles.missing}>{item.name[0]}</span>
          )}
          {mounted && videoSource && (
            <video
              ref={(node) => {
                video.current = node;
                if (active.current) node?.play().catch(() => {});
              }}
              src={videoSource}
              muted
              loop
              playsInline
              preload="none"
              className={playing ? styles.playing : ""}
              onError={() => {
                setPlaying(false);
                setVideoSource(
                  item.videoFallback && videoSource !== item.videoFallback
                    ? item.videoFallback
                    : null,
                );
              }}
              onPlaying={() => {
                if (active.current) setPlaying(true);
                else video.current?.pause();
              }}
            />
          )}
        </div>
        {item.video && <span className={styles.videoBadge}>Video</span>}
      </div>
      <div className={styles.cardMeta}>
        {iconSource ? (
          <img
            src={iconSource}
            alt=""
            loading="lazy"
            decoding="async"
            onError={() =>
              setIconSource(
                item.iconFallback && iconSource !== item.iconFallback
                  ? item.iconFallback
                  : null,
              )
            }
          />
        ) : (
          <span className={styles.letter}>{item.name[0]}</span>
        )}
        <div>
          <h2>{item.name}</h2>
          <p>{item.description}</p>
          <div className={styles.cardChips}>
            {[item.themes[0], item.industry, item.productType]
              .filter(Boolean)
              .filter((value, i, all) => all.indexOf(value) === i)
              .map((value) => (
                <span key={value}>{value}</span>
              ))}
          </div>
        </div>
      </div>
    </Link>
  );
}

export function StylesIndex() {
  return (
    <Suspense
      fallback={
        <div className={styles.index}>
          <SkeletonGrid
            shape="style"
            count={6}
            className={styles.grid}
            label="Opening styles…"
          />
        </div>
      }
    >
      <StylesContent />
    </Suspense>
  );
}
function StylesContent() {
  const params = useSearchParams();
  const filters: StyleFilters = {
    q: params.get("q") || "",
    theme: params.get("theme") || "",
    type: params.get("type") || "",
    style: params.get("style") || "",
    industry: params.get("industry") || "",
    tags: (params.get("tag") || "").split(",").filter(Boolean),
    video: params.get("video") === "1",
  };
  const [items, setItems] = useState<LibraryItem[]>([]),
    [total, setTotal] = useState<number | null>(null),
    [loading, setLoading] = useState(true),
    [error, setError] = useState(""),
    [retry, setRetry] = useState(0),
    [shown, setShown] = useState(48);
  const search = useRef<HTMLInputElement | null>(null),
    results = useRef<HTMLDivElement | null>(null),
    sentinel = useRef<HTMLDivElement | null>(null);
  const order = params.get("order") === "newest" ? "newest" : "name";
  const filterKey = JSON.stringify([filters, order]);
  function update(patch: Record<string, string>) {
    const next = new URLSearchParams(window.location.search);
    for (const [key, value] of Object.entries(patch))
      value ? next.set(key, value) : next.delete(key);
    // Styles owns its source. A legacy ?source=systems cannot mix the stores.
    next.delete("source");
    next.delete("platform");
    window.history.replaceState(
      null,
      "",
      `/styles${next.size ? `?${next}` : ""}`,
    );
    try {
      localStorage.setItem(
        "ds-style-filters",
        JSON.stringify(Object.fromEntries(next)),
      );
    } catch {}
  }
  useEffect(() => {
    if (window.location.search) return;
    try {
      const saved = JSON.parse(
        localStorage.getItem("ds-style-filters") || "{}",
      );
      const next = new URLSearchParams();
      for (const key of ["theme", "type", "style", "industry", "tag", "video"])
        if (typeof saved[key] === "string") next.set(key, saved[key]);
      if (next.size) window.history.replaceState(null, "", `/styles?${next}`);
    } catch {}
  }, []);
  useEffect(() => {
    let live = true;
    setLoading(true);
    setError("");
    loadLibraryPages(
      (offset) =>
        api<LibraryResponse>(
          `/api/library?source=refero&limit=200&offset=${offset}`,
        ),
      (page) => {
        if (live) {
          setItems((previous) =>
            mergeLibraryItems(
              previous,
              page.items.filter((item) => item.source === "refero"),
            ),
          );
          setTotal(page.total);
        }
      },
      () => {
        if (live)
          setError(
            "Some styles could not be loaded. Retry to complete the collection.",
          );
      },
    )
      .catch((e) => {
        if (live) setError(e.message);
      })
      .finally(() => {
        if (live) setLoading(false);
      });
    return () => {
      live = false;
    };
  }, [retry]);
  useEffect(() => {
    const key = (event: KeyboardEvent) => {
      if (
        event.key !== "/" ||
        event.metaKey ||
        event.ctrlKey ||
        (event.target instanceof Element &&
          event.target.closest(
            'input, textarea, select, [contenteditable="true"], [role="dialog"]',
          ))
      )
        return;
      event.preventDefault();
      search.current?.focus();
    };
    document.addEventListener("keydown", key);
    return () => document.removeEventListener("keydown", key);
  }, []);
  useEffect(() => setShown(48), [filterKey]);
  const filtered = useMemo(
    () =>
      filters.q
        ? filterStyles(items, filters)
        : orderStyles(filterStyles(items, filters), order),
    [items, filterKey],
  );
  const hasMore = shown < filtered.length;
  useEffect(() => {
    if (!sentinel.current || !hasMore) return;
    const observer = new IntersectionObserver(
      (entries) => {
        if (entries[0].isIntersecting) setShown((count) => count + 48);
      },
      { rootMargin: "600px" },
    );
    observer.observe(sentinel.current);
    return () => observer.disconnect();
  }, [hasMore, shown, filtered.length]);
  const complete = total !== null && items.length >= total;
  const active =
    filters.q ||
    filters.theme ||
    filters.type ||
    filters.style ||
    filters.industry ||
    filters.tags.length ||
    filters.video;
  const clear = {
    q: "",
    theme: "",
    type: "",
    style: "",
    industry: "",
    tag: "",
    video: "",
  };
  return (
    <>
      <div className={styles.index}>
        <header className={styles.hero}>
          <div className={styles.kicker}>
            <a
              href="https://styles.refero.design"
              target="_blank"
              rel="noreferrer"
            >
              Refero styles <ArrowRight size={12} />
            </a>
            <span>Third-party interpretation</span>
          </div>
          <RotatingHeadline />
          <p>
            A collection of {total?.toLocaleString() || "1,342"} interpreted
            website styles, with videos, documents, and design details.{" "}
            <Link href="/library">Measured app screenshots</Link> live in their
            own library.
          </p>
          <div className={styles.searchArea}>
            <form
              className={styles.search}
              onSubmit={(event) => {
                event.preventDefault();
                results.current?.scrollIntoView({
                  behavior: "smooth",
                  block: "start",
                });
              }}
            >
              <Search size={18} />
              <input
                ref={search}
                aria-label="Search Refero styles"
                placeholder="Search DESIGN.md examples"
                value={filters.q}
                onChange={(e) => update({ q: e.target.value })}
                onKeyDown={(event) => {
                  if (event.key === "Escape") {
                    update({ q: "" });
                    search.current?.blur();
                  }
                }}
              />
              {filters.q && (
                <button
                  type="button"
                  aria-label="Clear search"
                  onClick={() => update({ q: "" })}
                >
                  <X size={18} />
                </button>
              )}
              <kbd>/</kbd>
              <button
                className={styles.submit}
                aria-label="Search"
                disabled={!filters.q.trim()}
              >
                <ArrowUp size={20} />
              </button>
            </form>
            <div className={styles.prompts}>
              {PROMPTS.map(([prompt, query]) => (
                <button
                  key={prompt}
                  onClick={() => update({ ...clear, q: query })}
                >
                  <ArrowRight size={12} />
                  {prompt}
                </button>
              ))}
            </div>
          </div>
        </header>
        <div className={styles.filterArea} ref={results}>
          {!filters.q && (
            <div
              className={styles.orderTabs}
              role="tablist"
              aria-label="Style order"
              onKeyDown={(event) => {
                if (
                  !["ArrowLeft", "ArrowRight", "Home", "End"].includes(
                    event.key,
                  )
                )
                  return;
                event.preventDefault();
                const next =
                  event.key === "Home"
                    ? "name"
                    : event.key === "End"
                      ? "newest"
                      : order === "name"
                        ? "newest"
                        : "name";
                update({ order: next === "name" ? "" : next });
                event.currentTarget
                  .querySelectorAll<HTMLButtonElement>("button")
                  [next === "name" ? 0 : 1]?.focus();
              }}
            >
              <button
                role="tab"
                aria-selected={order === "name"}
                tabIndex={order === "name" ? 0 : -1}
                onClick={() => update({ order: "" })}
              >
                Name A–Z
              </button>
              <button
                role="tab"
                aria-selected={order === "newest"}
                tabIndex={order === "newest" ? 0 : -1}
                title="Newest source extraction in this snapshot"
                onClick={() => update({ order: "newest" })}
              >
                Newest capture
              </button>
            </div>
          )}
          <div className={styles.filters}>
            {(
              [
                ["theme", "All themes"],
                ["type", "All product types"],
                ["style", "All design styles"],
                ["industry", "All industries"],
              ] as [StyleFacet, string][]
            ).map(([key, label]) => (
              <label key={key}>
                <span className="sr-only">{label}</span>
                <select
                  value={filters[key]}
                  onChange={(event) => update({ [key]: event.target.value })}
                >
                  <option value="">{label}</option>
                  {styleCounts(items, key).map(([value, count]) => (
                    <option key={value} value={value}>
                      {value} ({count})
                    </option>
                  ))}
                </select>
              </label>
            ))}
            <button
              className={filters.video ? styles.activeChip : styles.chip}
              aria-pressed={filters.video}
              onClick={() => update({ video: filters.video ? "" : "1" })}
            >
              Has video
            </button>
            {!!active && (
              <button className={styles.reset} onClick={() => update(clear)}>
                Clear filters <X size={13} />
              </button>
            )}
          </div>
          <div className={styles.tags} aria-label="Secondary style tags">
            {styleCounts(items, "tag").map(([tag, count]) => (
              <button
                key={tag}
                className={
                  filters.tags.includes(tag) ? styles.activeChip : styles.chip
                }
                aria-pressed={filters.tags.includes(tag)}
                onClick={() =>
                  update({
                    tag: (filters.tags.includes(tag)
                      ? filters.tags.filter((t) => t !== tag)
                      : [...filters.tags, tag]
                    ).join(","),
                  })
                }
              >
                {tag}
                <span>{count}</span>
              </button>
            ))}
          </div>
          <p className={styles.count} role="status">
            {complete
              ? `${filtered.length.toLocaleString()} styles`
              : `${filtered.length.toLocaleString()} matches · ${items.length.toLocaleString()} of ${total?.toLocaleString() || "…"} styles loaded`}
            {loading && items.length > 0 ? " · Loading…" : ""}
          </p>
        </div>
        {error && (
          <ErrorState message={error} retry={() => setRetry((n) => n + 1)} />
        )}
        {!items.length && loading ? (
          <SkeletonGrid
            shape="style"
            count={6}
            className={styles.grid}
            label="Opening the style collection…"
          />
        ) : filtered.length ? (
          <div className={styles.grid}>
            {filtered.slice(0, shown).map((item) => (
              <StyleCard item={item} key={item.id} />
            ))}
          </div>
        ) : loading ? (
          <Spinner label="Searching remaining styles…" />
        ) : (
          <Empty
            title={
              complete
                ? "No styles match these filters."
                : "No matches in the loaded styles."
            }
          >
            <button className="pill" onClick={() => update(clear)}>
              Clear filters
            </button>
          </Empty>
        )}
        {hasMore && (
          <div className={styles.more} ref={sentinel}>
            <button
              className="pill"
              onClick={() => setShown((count) => count + 48)}
            >
              Load more styles <ArrowRight size={14} />
            </button>
          </div>
        )}
      </div>
    </>
  );
}
