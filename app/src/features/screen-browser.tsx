"use client";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import { useEffect, useRef, useState } from "react";
import { ArrowRight } from "lucide-react";
import type { ScreenItem, ScreenResponse } from "@/contracts/screens";
import { api, Empty, ErrorState, Spinner } from "@/components/shared";
import { MediaBookmarkButton } from "@/components/media-bookmark";
import { PackageLightbox } from "./package-detail";
import styles from "./screen-browser.module.css";
import {
  captureViewerOrigin,
  type CaptureViewerOrigin,
} from "./capture-viewer-motion";

export function ScreenBrowser() {
  const viewerOrigin = useRef<CaptureViewerOrigin | undefined>(undefined);
  const grid = useRef<HTMLDivElement | null>(null);
  const params = useSearchParams();
  const query = params.get("q") || "",
    platform =
      params.get("platform") || (params.has("referenceId") ? "" : "web"),
    theme = params.get("theme") || "",
    category = params.get("category") || "",
    tag = params.get("tag") || "",
    group = params.get("group") || "",
    referenceIdsKey = JSON.stringify(params.getAll("referenceId")),
    termIdsKey = JSON.stringify(params.getAll("term")),
    mode = params.get("mode") === "flows" ? "flows" : "screens",
    kind = params.get("kind") === "crop" ? "crop" : "screenshot",
    order = params.get("order") || "recent",
    scope = params.get("scope") || "all";
  const [data, setData] = useState<ScreenResponse | null>(null),
    [dataKey, setDataKey] = useState(""),
    [restored, setRestored] = useState<ScreenItem | null>(null),
    [selectionError, setSelectionError] = useState(""),
    [selectionRetry, setSelectionRetry] = useState(0),
    [loading, setLoading] = useState(true),
    [error, setError] = useState(""),
    [limit, setLimit] = useState(60),
    [retry, setRetry] = useState(0);
  const searchParams = new URLSearchParams({
    q: query,
    scope,
    platform,
    theme,
    category,
    tag,
    group,
    mode,
    kind,
    order,
    limit: "60",
    offset: String(limit - 60),
  });
  for (const id of JSON.parse(referenceIdsKey) as string[])
    searchParams.append("referenceId", id);
  for (const id of JSON.parse(termIdsKey) as string[])
    searchParams.append("term", id);
  const search = searchParams.toString();
  const filterKey = JSON.stringify([
    query,
    platform,
    theme,
    category,
    tag,
    group,
    referenceIdsKey,
    termIdsKey,
    mode,
    kind,
    order,
    scope,
  ]);
  useEffect(() => {
    setLimit(60);
    setData(null);
  }, [
    query,
    platform,
    theme,
    category,
    tag,
    group,
    referenceIdsKey,
    termIdsKey,
    mode,
    kind,
    order,
    scope,
  ]);
  useEffect(() => {
    let alive = true;
    setLoading(true);
    setError("");
    api<ScreenResponse>(`/api/library/screens?${search}`)
      .then((value) => {
        if (alive) {
          setDataKey(filterKey);
          setData((previous) =>
            limit > 60 && previous
              ? {
                  ...value,
                  items: [
                    ...new Map(
                      [...previous.items, ...value.items].map((item) => [
                        item.id,
                        item,
                      ]),
                    ).values(),
                  ],
                }
              : value,
          );
        }
      })
      .catch((e) => {
        if (alive) setError(e.message);
      })
      .finally(() => {
        if (alive) setLoading(false);
      });
    return () => {
      alive = false;
    };
  }, [search, retry]);
  function update(patch: Record<string, string>) {
    const next = new URLSearchParams(window.location.search);
    for (const [key, value] of Object.entries(patch))
      value ? next.set(key, value) : next.delete(key);
    window.history.replaceState(
      null,
      "",
      `${window.location.pathname}?${next}`,
    );
  }
  const visibleData = dataKey === filterKey ? data : null;
  const items = visibleData?.items || [];
  useEffect(() => {
    if (
      !visibleData ||
      !grid.current ||
      window.matchMedia("(prefers-reduced-motion: reduce)").matches
    )
      return;
    const animation = grid.current.animate(
      [
        { opacity: 0, transform: "translateY(6px)" },
        { opacity: 1, transform: "translateY(0)" },
      ],
      { duration: 150, easing: "ease-out" },
    );
    return () => animation.cancel();
  }, [dataKey]);
  const selectedScreen = params.get("screen");
  const loadedCurrent = items.find((item) => item.id === selectedScreen);
  const current =
    loadedCurrent || (restored?.id === selectedScreen ? restored : undefined);
  useEffect(() => {
    if (!selectedScreen || loadedCurrent || loading) return;
    let alive = true;
    setSelectionError("");
    api<ScreenResponse>(
      `/api/library/screens?screenId=${encodeURIComponent(selectedScreen)}`,
    )
      .then((value) => {
        if (alive) {
          if (value.items[0]) setRestored(value.items[0]);
          else setSelectionError("This captured screen is unavailable.");
        }
      })
      .catch((e) => {
        if (alive) setSelectionError(e.message);
      });
    return () => {
      alive = false;
    };
  }, [selectedScreen, loadedCurrent, loading, selectionRetry]);
  const viewerItems = loadedCurrent ? items : current ? [current] : [];
  function open(item: ScreenItem) {
    update({ screen: item.id });
  }
  return (
    <section className={styles.browser} aria-label="Captured screens">
      <span className="sr-only" role="status">
        {loading
          ? "Finding screens…"
          : `${visibleData?.total || 0} ${mode === "flows" ? "flows" : "screens"}`}
      </span>
      {selectedScreen && !current && selectionError && (
        <div role="alert">
          <ErrorState
            message={selectionError}
            retry={() => setSelectionRetry((value) => value + 1)}
          />
          <button className="pill" onClick={() => update({ screen: "" })}>
            Dismiss selection
          </button>
        </div>
      )}
      {error && (
        <ErrorState
          message={error}
          retry={() => setRetry((value) => value + 1)}
        />
      )}
      {loading && !visibleData ? (
        <Spinner label="Opening captured screens…" />
      ) : !items.length && !loading ? (
        <Empty
          title={
            mode === "flows"
              ? "No recorded flows yet"
              : "No screens match these filters"
          }
        >
          <p>
            {mode === "flows"
              ? "This library has individual captures, but no verified step-by-step flows yet."
              : "Try another filter or remove a search chip."}
          </p>
          <button
            className="pill"
            onClick={() =>
              update({
                q: "",
                tag: "",
                group: "",
                category: "",
                theme: "",
                platform: "",
                referenceId: "",
                term: "",
                screen: "",
              })
            }
          >
            Clear filters
          </button>
        </Empty>
      ) : (
        <div
          ref={grid}
          className={`${styles.grid} ${platform === "mobile" ? styles.phoneGrid : ""}`}
          aria-busy={loading}
        >
          {items.map((item) => (
            <article className={styles.card} key={item.id}>
              <button
                className={styles.open}
                onClick={(event) => {
                  viewerOrigin.current = captureViewerOrigin(
                    event.currentTarget,
                    item.id,
                  );
                  open(item);
                }}
                aria-label={`Open ${item.reference.name}: ${item.media.name}`}
              >
                <div className={styles.picture} data-viewer-source={item.id}>
                  <img
                    src={item.media.thumbnail || item.media.url}
                    alt={`${item.reference.name}: ${item.media.name}`}
                    loading="lazy"
                    decoding="async"
                  />
                </div>
              </button>
              <div className={styles.caption}>
                <Link
                  href={`/library?view=screens&platform=${item.reference.platform}&referenceId=${encodeURIComponent(item.reference.id)}`}
                >
                  {item.reference.icon && (
                    <img src={item.reference.icon} alt="" loading="lazy" />
                  )}
                  {item.reference.name}
                </Link>
                <MediaBookmarkButton
                  referenceId={item.reference.id}
                  mediaId={item.media.id}
                  compact
                />
              </div>
            </article>
          ))}
        </div>
      )}
      {visibleData && items.length < visibleData.total && (
        <div className={styles.more}>
          <button
            className="pill"
            disabled={loading || !!error}
            onClick={() => setLimit((value) => value + 60)}
          >
            Show more screens <ArrowRight size={16} />
          </button>
        </div>
      )}
      {current && (
        <PackageLightbox
          detail={current.reference}
          current={current.media}
          items={viewerItems.map((item) => item.media)}
          origin={viewerOrigin.current}
          onClose={() => update({ screen: "" })}
          onChange={(media) => {
            const next = viewerItems.find((item) => item.media === media);
            if (next) open(next);
          }}
        />
      )}
    </section>
  );
}
