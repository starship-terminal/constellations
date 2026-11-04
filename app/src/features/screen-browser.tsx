"use client";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import { useEffect, useState } from "react";
import { ArrowRight, SlidersHorizontal, X } from "lucide-react";
import type { ScreenItem, ScreenResponse } from "@/contracts/screens";
import { api, Empty, ErrorState, Spinner } from "@/components/shared";
import { MediaBookmarkButton } from "@/components/media-bookmark";
import { PackageLightbox } from "./package-detail";
import styles from "./screen-browser.module.css";

export function ScreenBrowser() {
  const params = useSearchParams();
  const query = params.get("q") || "",
    platform = params.get("platform") || "",
    theme = params.get("theme") || "",
    category = params.get("category") || "",
    tag = params.get("tag") || "",
    group = params.get("group") || "",
    referenceId = params.get("referenceId") || "",
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
    [retry, setRetry] = useState(0),
    [filtersOpen, setFiltersOpen] = useState(false);
  const search = new URLSearchParams({
    q: query,
    scope,
    platform,
    theme,
    category,
    tag,
    group,
    referenceId,
    kind,
    order,
    limit: "60",
    offset: String(limit - 60),
  }).toString();
  const filterKey = JSON.stringify([
    query,
    platform,
    theme,
    category,
    tag,
    group,
    referenceId,
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
    referenceId,
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
  const reference = referenceId
    ? items.find((item) => item.reference.id === referenceId)?.reference
    : undefined;
  const activeFilters = [
    ["q", query],
    ["scope", scope === "media" ? "Capture text only" : ""],
    ["platform", platform],
    ["theme", theme],
    [
      "category",
      data?.items
        .flatMap((item) => item.reference.categories || [])
        .find((term) => term.id === category)?.label ||
        category.split(":").at(-1)?.replace(/-/g, " ") ||
        category,
    ],
    ["tag", tag],
    ["group", group],
    ["referenceId", reference?.name || referenceId],
  ].filter(([, value]) => value);
  function open(item: ScreenItem) {
    update({ screen: item.id });
  }
  return (
    <section className={styles.browser} aria-label="Captured screens">
      {!!activeFilters.length && (
        <div className={styles.chips} aria-label="Active screen filters">
          {activeFilters.map(([key, value]) => (
            <button
              key={key}
              onClick={() => update({ [key]: "", screen: "" })}
              aria-label={`Remove ${value} filter`}
            >
              {key === "referenceId"
                ? "App"
                : key === "q"
                  ? "Search"
                  : key === "scope"
                    ? "Search in"
                    : key}{" "}
              <strong>{value}</strong>
              <X size={14} />
            </button>
          ))}
          <button
            onClick={() =>
              update({
                q: "",
                scope: "",
                platform: "",
                theme: "",
                category: "",
                tag: "",
                group: "",
                referenceId: "",
                screen: "",
              })
            }
          >
            Clear all
          </button>
        </div>
      )}
      <div className={styles.toolbar}>
        <div className={styles.kinds} aria-label="Capture type">
          <button
            aria-pressed={kind === "screenshot"}
            onClick={() => update({ kind: "screenshot", screen: "" })}
          >
            Screens
          </button>
          <button
            aria-pressed={kind === "crop"}
            onClick={() => update({ kind: "crop", screen: "" })}
          >
            UI elements
          </button>
        </div>
        <span className={styles.count} role="status">
          {loading
            ? "Finding screens…"
            : `${(visibleData?.total || 0).toLocaleString()} ${kind === "crop" ? "UI elements" : "screens"}`}
        </span>
        <button
          className={styles.filterToggle}
          aria-expanded={filtersOpen}
          onClick={() => setFiltersOpen((value) => !value)}
        >
          <SlidersHorizontal size={16} />
          Filters
        </button>
        <label>
          <span className="sr-only">Screen order</span>
          <select
            value={order}
            onChange={(e) => update({ order: e.target.value, screen: "" })}
          >
            <option value="recent">Latest captures</option>
            <option value="name">Name A–Z</option>
          </select>
        </label>
      </div>
      {filtersOpen && (
        <div className={styles.filterPanel}>
          <label>
            Platform
            <select
              value={platform}
              onChange={(e) => update({ platform: e.target.value, screen: "" })}
            >
              <option value="">All platforms</option>
              {visibleData?.facets.platforms.map((f) => (
                <option key={f.value} value={f.value}>
                  {f.value} ({f.count})
                </option>
              ))}
            </select>
          </label>
          <label>
            Theme
            <select
              value={theme}
              onChange={(e) => update({ theme: e.target.value, screen: "" })}
            >
              <option value="">All themes</option>
              <option>light</option>
              <option>dark</option>
            </select>
          </label>
          <label>
            Capture tag
            <select
              value={tag}
              onChange={(e) => update({ tag: e.target.value, screen: "" })}
            >
              <option value="">All tags</option>
              {visibleData?.facets.tags.map((f) => (
                <option key={f.value} value={f.value}>
                  {f.value} ({f.count})
                </option>
              ))}
            </select>
          </label>
          <label>
            Capture group
            <select
              value={group}
              onChange={(e) => update({ group: e.target.value, screen: "" })}
            >
              <option value="">All groups</option>
              {visibleData?.facets.groups.map((f) => (
                <option key={f.value} value={f.value}>
                  {f.value} ({f.count})
                </option>
              ))}
            </select>
          </label>
        </div>
      )}
      {reference && (
        <div className={styles.product}>
          <h1>{reference.name}</h1>
          <Link href={`/library/${reference.slug}`}>
            Package details <ArrowRight size={14} />
          </Link>
        </div>
      )}
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
        <Empty title="No captures match these filters">
          <p>Try another screen description or clear a filter.</p>
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
              })
            }
          >
            Clear filters
          </button>
        </Empty>
      ) : (
        <div
          className={`${styles.grid} ${platform === "mobile" ? styles.phoneGrid : ""}`}
          aria-busy={loading}
        >
          {items.map((item) => (
            <article className={styles.card} key={item.id}>
              <button
                className={styles.open}
                onClick={() => open(item)}
                aria-label={`Open ${item.reference.name}: ${item.media.name}`}
              >
                <div className={styles.picture}>
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
                  href={`/library?view=screens&referenceId=${encodeURIComponent(item.reference.id)}`}
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
              <p title={item.media.name}>{item.media.name}</p>
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
