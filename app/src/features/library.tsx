"use client";
import Link from "next/link";
import { Suspense, useEffect, useMemo, useState } from "react";
import {
  ArrowRight,
  Binoculars,
  Check,
  Grid2X2,
  Laptop,
  Monitor,
  Files,
  Scissors,
  PanelTop,
  Plus,
  RefreshCw,
  CircleDashed,
  Smartphone,
  X,
} from "lucide-react";
import { useRouter, useSearchParams } from "next/navigation";
import type { LibraryItem } from "@/contracts/library";
import { matchesCategory, UNCATEGORISED } from "@/contracts/categories";
import type { TaxonomyGroup } from "@/contracts/taxonomy";
import { CategoryIcon } from "./category-icon";
import {
  api,
  Empty,
  ErrorState,
  MediaPreview,
  Select,
  SkeletonGrid,
  Spinner,
} from "@/components/shared";
import { Comparison } from "@/components/reference";
import styles from "./library.module.css";
import { ScreenBrowser } from "./screen-browser";
import {
  MobileCatalogPreview,
  originalMobilePreview,
} from "./mobile-catalog-preview";
import { CatalogSearch } from "./catalog-search";
import {
  platformSearch,
  inferredProductPlatform,
  canSwitchPlatform,
} from "./catalog-search-state";
import { loadCatalog, type LibraryResponse } from "./library-data";
import { replaceSearch } from "./url-state";

export function LibraryPage() {
  return (
    <Suspense
      fallback={
        <div className={`${styles.library} ${styles.catalog}`}>
          <SkeletonGrid
            shape="web"
            count={6}
            className={styles.appGrid}
            label="Opening references…"
          />
        </div>
      }
    >
      <LibraryContent />
    </Suspense>
  );
}
function LibraryContent() {
  const router = useRouter();
  const params = useSearchParams();
  const query = params.get("q") || "",
    platform = params.get("platform") || "",
    source = "systems",
    theme = params.get("theme") || "",
    category = params.get("category") || "";
  const screenView = params.get("view") === "screens";
  const [layout, setLayout] = useState("grid");
  const [scrub, setScrub] = useState(true);
  useEffect(() => {
    setLayout(localStorage.getItem("studio-gallery-layout") || "grid");
    setScrub(localStorage.getItem("studio-gallery-scrub") !== "false");
  }, []);
  const [allItems, setAllItems] = useState<LibraryItem[]>([]),
    [loading, setLoading] = useState(true),
    [catalogTotal, setCatalogTotal] = useState<number | null>(null),
    [error, setError] = useState(""),
    [reload, setReload] = useState(0),
    [selected, setSelected] = useState<LibraryItem[]>([]),
    [compare, setCompare] = useState(false),
    [visibleCount, setVisibleCount] = useState(24);
  const [taxonomy, setTaxonomy] = useState<TaxonomyGroup[]>([]),
    [taxonomyLoading, setTaxonomyLoading] = useState(true),
    [taxonomyError, setTaxonomyError] = useState(""),
    [taxonomyReload, setTaxonomyReload] = useState(0);
  useEffect(() => {
    let alive = true;
    setTaxonomyLoading(true);
    setTaxonomyError("");
    api<{ groups: TaxonomyGroup[] }>("/api/taxonomy")
      .then(({ groups }) => {
        if (
          !Array.isArray(groups) ||
          !["web-categories", "ios-categories"].every((id) =>
            groups.some((group) => group.id === id && group.terms.length),
          )
        )
          throw new Error("The reference categories are unavailable.");
        if (alive) setTaxonomy(groups);
      })
      .catch((error) => {
        if (alive) setTaxonomyError(error.message);
      })
      .finally(() => {
        if (alive) setTaxonomyLoading(false);
      });
    return () => {
      alive = false;
    };
  }, [taxonomyReload]);
  function updateFilters(patch: Record<string, string>) {
    const next = new URLSearchParams(window.location.search);
    for (const [key, value] of Object.entries(patch))
      value ? next.set(key, value) : next.delete(key);
    replaceSearch(next);
  }
  useEffect(() => {
    setVisibleCount(24);
  }, [query, source, platform, theme, category]);
  useEffect(() => {
    let alive = true;
    setLoading(true);
    setError("");
    // Publish available cards immediately; later pages enrich exact filters/categories.
    // Retain already loaded items on retry, including when a later page failed.
    loadCatalog(
      "systems",
      (offset) =>
        api<LibraryResponse>(
          `/api/library?source=systems&limit=200&offset=${offset}`,
        ),
      (catalog) => {
        if (!alive) return;
        setAllItems(catalog.items);
        setCatalogTotal(catalog.total);
      },
      () => {
        if (alive)
          setError(
            "Some references could not be loaded. Available references are still shown. Retry to load the remaining pages.",
          );
      },
    )
      .catch((e) => {
        if (alive) setError(e.message);
      })
      .finally(() => {
        if (alive) setLoading(false);
      });
    return () => {
      alive = false;
    };
  }, [reload]);
  useEffect(() => {
    const current = new URLSearchParams(window.location.search);
    if (current.has("platform") || current.get("view") !== "screens") return;
    const inferred = inferredProductPlatform(current, allItems);
    if (inferred) {
      current.set("platform", inferred);
      replaceSearch(current);
    }
  }, [params, allItems]);
  const scoped = useMemo(
    () =>
      allItems.filter(
        (item) =>
          (!source || item.source === source) &&
          (!platform || item.platform === platform) &&
          (!theme ||
            item.themes.some(
              (value) => value === theme || value.startsWith(`${theme}-`),
            )),
      ),
    [allItems, source, platform, theme],
  );
  const categories = useMemo(() => {
    const groupIds =
      platform === "mobile"
        ? ["ios-categories"]
        : platform
          ? ["web-categories"]
          : ["web-categories", "ios-categories"];
    const options = new Map<
      string,
      { id: string; label: string; ids: string[] }
    >();
    // Preserve Refero's term order. In Gallery, shared labels represent both
    // platform groups while the URL keeps the first recorded canonical ID.
    for (const groupId of groupIds) {
      for (const term of taxonomy.find((group) => group.id === groupId)
        ?.terms || []) {
        const existing = options.get(term.label);
        if (existing) existing.ids.push(term.id);
        else
          options.set(term.label, {
            id: term.id,
            label: term.label,
            ids: [term.id],
          });
      }
    }
    return [...options.values()];
  }, [taxonomy, platform]);
  const filtered = useMemo(() => {
    const words = query.trim().toLowerCase().split(/\s+/).filter(Boolean);
    return scoped
      .filter(
        (item) =>
          matchesCategory(item, category) &&
          words.every((word) =>
            `${item.name} ${item.slug} ${item.description} ${item.tags.join(" ")} ${item.themes.join(" ")} ${(item.fonts || []).join(" ")} ${item.category} ${(item.categories || []).map((value) => value.label).join(" ")}`
              .toLowerCase()
              .includes(word),
          ),
      )
      .sort(
        (a, b) =>
          (b.captured || "").localeCompare(a.captured || "") ||
          a.name.localeCompare(b.name),
      );
  }, [scoped, category, query]);
  const items = filtered.slice(0, visibleCount);
  const complete = catalogTotal !== null && allItems.length >= catalogTotal;
  function toggle(item: LibraryItem) {
    setSelected((prev) =>
      prev.some((x) => x.id === item.id)
        ? prev.filter((x) => x.id !== item.id)
        : prev.length < 3
          ? [...prev, item]
          : prev,
    );
  }
  const platformLinksReady = canSwitchPlatform(
    params,
    !taxonomyLoading && !taxonomyError,
    allItems,
    loading,
  );
  const modeUrl = (mode: string) => {
    const next = platformSearch(
      new URLSearchParams(params.toString()),
      mode,
      taxonomy,
      allItems,
      !loading && !error,
    );
    return `/library${next.size ? `?${next}` : ""}`;
  };
  return (
    <>
      <div className={`${styles.library} ${styles.catalog}`}>
        <div className={styles.searchTop}>
          <CatalogSearch
            taxonomy={taxonomy}
            items={allItems}
            taxonomyLoading={taxonomyLoading}
            taxonomyError={taxonomyError}
            retryTaxonomy={() => setTaxonomyReload((value) => value + 1)}
          />
          <div className={styles.modeBar}>
            <nav className={styles.modes} aria-label="Search mode">
              <Link href="/">
                <Binoculars size={16} />
                Research mode
              </Link>
              <Link
                className={
                  platform === "web" || (screenView && !platform)
                    ? styles.modeActive
                    : ""
                }
                href={
                  platformLinksReady ? modeUrl("web") : `/library?${params}`
                }
                aria-disabled={!platformLinksReady}
                title={
                  platformLinksReady ? undefined : "Loading selected filters…"
                }
                onClick={(event) => {
                  if (!platformLinksReady) event.preventDefault();
                }}
              >
                <Monitor className={styles.webModeIcon} size={18} />
                Web apps
              </Link>
              <Link
                className={platform === "mobile" ? styles.modeActive : ""}
                href={
                  platformLinksReady ? modeUrl("mobile") : `/library?${params}`
                }
                aria-disabled={!platformLinksReady}
                title={
                  platformLinksReady ? undefined : "Loading selected filters…"
                }
                onClick={(event) => {
                  if (!platformLinksReady) event.preventDefault();
                }}
              >
                <Smartphone className={styles.iosModeIcon} size={18} />
                iOS apps
              </Link>
              <Link
                className={platform === "desktop" ? styles.modeActive : ""}
                href={
                  platformLinksReady ? modeUrl("desktop") : `/library?${params}`
                }
                aria-disabled={!platformLinksReady}
                title={
                  platformLinksReady ? undefined : "Loading selected filters…"
                }
                onClick={(event) => {
                  if (!platformLinksReady) event.preventDefault();
                }}
              >
                <Laptop size={18} />
                Desktop apps
              </Link>
            </nav>
            {screenView && (
              <nav className={styles.resultModes} aria-label="Result type">
                <button
                  aria-pressed={params.get("mode") !== "flows"}
                  onClick={() => updateFilters({ mode: "" })}
                >
                  <Files className={styles.screensModeIcon} size={18} />
                  Screens
                </button>
                <button
                  aria-pressed={params.get("mode") === "flows"}
                  onClick={() => updateFilters({ mode: "flows" })}
                >
                  <Scissors size={18} />
                  Flows
                </button>
              </nav>
            )}
          </div>
        </div>
        {!screenView && (
          <h1 className={styles.catalogTitle}>
            {platform === "web"
              ? "Web apps"
              : platform === "mobile"
                ? "iOS apps"
                : platform === "desktop"
                  ? "Desktop apps"
                  : "Gallery"}
          </h1>
        )}
        {!screenView && (
          <>
            {taxonomyLoading && (
              <Spinner label="Loading reference categories…" />
            )}
            {taxonomyError && (
              <ErrorState
                message={taxonomyError}
                retry={() => setTaxonomyReload((value) => value + 1)}
              />
            )}
            <nav
              className={styles.categories}
              aria-label="Reference category"
              aria-busy={taxonomyLoading}
            >
              <button
                className={!category ? styles.categoryActive : ""}
                aria-pressed={!category}
                onClick={() => updateFilters({ category: "" })}
              >
                <RefreshCw size={18} aria-hidden="true" />
                Latest
              </button>
              {categories.map((option) => {
                const active =
                  !!category &&
                  matchesCategory(
                    { category: "", categoryIds: option.ids },
                    category,
                  );
                return (
                  <button
                    key={option.id}
                    className={active ? styles.categoryActive : ""}
                    aria-pressed={active}
                    onClick={() =>
                      updateFilters({
                        category: active ? "" : option.id,
                      })
                    }
                  >
                    <CategoryIcon label={option.label} />
                    {option.label}
                  </button>
                );
              })}
              {/* Packages the category seed has not curated yet stay findable. */}
              {scoped.some((item) => !item.categoryIds?.length) && (
                <button
                  className={
                    category === UNCATEGORISED ? styles.categoryActive : ""
                  }
                  aria-pressed={category === UNCATEGORISED}
                  onClick={() =>
                    updateFilters({
                      category: category === UNCATEGORISED ? "" : UNCATEGORISED,
                    })
                  }
                >
                  <CircleDashed size={18} aria-hidden="true" />
                  Uncategorised
                </button>
              )}
            </nav>
          </>
        )}
        {!screenView && (
          <nav className={styles.browseModes} aria-label="Browse references">
            <button
              aria-pressed={!screenView}
              onClick={() =>
                updateFilters({
                  view: "",
                  referenceId: "",
                  tag: "",
                  group: "",
                  kind: "",
                })
              }
            >
              <Grid2X2 size={16} />
              Apps
            </button>
            <button
              aria-pressed={screenView}
              onClick={() => updateFilters({ view: "screens" })}
            >
              <PanelTop size={16} />
              Screens
            </button>
          </nav>
        )}
        {screenView ? (
          <ScreenBrowser />
        ) : (
          <>
            <div className={styles.filters}>
              <Select
                compact
                label="Gallery layout"
                value={layout}
                onChange={(value) => {
                  setLayout(value);
                  localStorage.setItem("studio-gallery-layout", value);
                }}
                options={[
                  { value: "grid", label: "Grid view" },
                  { value: "list", label: "List view" },
                ]}
              />
              <label>
                <input
                  type="checkbox"
                  checked={scrub}
                  onChange={(e) => {
                    setScrub(e.target.checked);
                    localStorage.setItem(
                      "studio-gallery-scrub",
                      String(e.target.checked),
                    );
                  }}
                />{" "}
                Preview on hover
              </label>
              <Select
                compact
                label="Platform"
                value={platform}
                onChange={(value) =>
                  updateFilters({ platform: value, category: "" })
                }
                options={[
                  { value: "", label: "All platforms" },
                  { value: "web", label: "Web" },
                  { value: "mobile", label: "Mobile" },
                  { value: "desktop", label: "Desktop" },
                ]}
              />
              <Select
                compact
                label="Theme"
                value={theme}
                onChange={(value) => updateFilters({ theme: value })}
                options={[
                  { value: "", label: "All themes" },
                  { value: "light", label: "Light" },
                  { value: "dark", label: "Dark" },
                ]}
              />
            </div>
            <div className={styles.results}>
              <span>
                {!allItems.length && loading
                  ? "Finding references…"
                  : complete
                    ? `${filtered.length.toLocaleString()} references`
                    : `${filtered.length.toLocaleString()} matches · ${allItems.length.toLocaleString()}${catalogTotal === null ? "" : ` of ${catalogTotal.toLocaleString()}`} references loaded.`}
              </span>
              <span>
                {loading && allItems.length > 0
                  ? "Loading more references…"
                  : "Select up to 3 to compare"}
              </span>
            </div>
            {error && (
              <ErrorState
                message={error}
                retry={() => setReload((value) => value + 1)}
              />
            )}
            {!allItems.length && loading ? (
              <SkeletonGrid
                shape={
                  layout === "list"
                    ? "list"
                    : platform === "mobile"
                      ? "ios"
                      : "web"
                }
                count={6}
                className={`${styles.appGrid} ${platform === "mobile" ? styles.mobileGrid : ""} ${layout === "list" ? styles.listView : ""}`}
                label="Opening the library…"
              />
            ) : items.length ? (
              <div
                className={`${styles.appGrid} ${platform === "mobile" ? styles.mobileGrid : ""} ${layout === "list" ? styles.listView : ""}`}
              >
                {items.map((item) => (
                  <CatalogCard
                    key={item.id}
                    item={item}
                    scrub={scrub}
                    onOpen={(item) =>
                      router.push(
                        `/library?view=screens&referenceId=${encodeURIComponent(item.id)}&platform=${encodeURIComponent(item.platform)}`,
                      )
                    }
                    onSelect={toggle}
                    selected={selected.some((x) => x.id === item.id)}
                  />
                ))}
              </div>
            ) : loading ? (
              <Spinner label="Checking the remaining references…" />
            ) : !complete ? (
              <Empty title="No matches in the loaded references.">
                <p>Load the remaining references to complete this search.</p>
              </Empty>
            ) : (
              <Empty title="No references match this search.">
                <p>Try another description or clear a filter.</p>
                <button
                  className="pill"
                  onClick={() => {
                    updateFilters({
                      q: "",
                      source: "",
                      platform: "",
                      theme: "",
                      category: "",
                    });
                  }}
                >
                  Clear filters
                </button>
              </Empty>
            )}
            {visibleCount < filtered.length && (
              <div className={styles.loadMore}>
                <button
                  className="pill"
                  onClick={() => setVisibleCount((value) => value + 24)}
                >
                  Show more references
                  <ArrowRight size={16} />
                </button>
              </div>
            )}
          </>
        )}
        {!!selected.length && (
          <div className="compare-bar">
            <div className="compare-thumbs">
              {selected.map((item) => (
                <button
                  onClick={() => toggle(item)}
                  title={`Remove ${item.name}`}
                  aria-label={`Remove ${item.name} from comparison`}
                  key={item.id}
                >
                  {item.icon ? <img src={item.icon} alt="" /> : item.name[0]}
                  <X size={10} />
                </button>
              ))}
            </div>
            <span>{selected.length} selected</span>
            <button
              className="primary small"
              disabled={selected.length < 2}
              onClick={() => setCompare(true)}
            >
              Compare references
              <ArrowRight size={14} />
            </button>
            <button
              className="icon-button"
              aria-label="Clear comparison"
              onClick={() => setSelected([])}
            >
              <X size={17} />
            </button>
          </div>
        )}
      </div>
      {compare && (
        <Comparison items={selected} onClose={() => setCompare(false)} />
      )}
    </>
  );
}
function CatalogCard({
  item,
  scrub,
  onOpen,
  onSelect,
  selected,
}: {
  item: LibraryItem;
  scrub: boolean;
  onOpen: (item: LibraryItem) => void;
  onSelect: (item: LibraryItem) => void;
  selected: boolean;
}) {
  const [frame, setFrame] = useState(0);
  const frames = scrub ? item.previewFrames || [] : [];
  return (
    <article
      className={`${styles.appCard} ${item.platform === "mobile" ? styles.mobileCard : ""} ${selected ? styles.appSelected : ""}`}
    >
      <button
        className={styles.openCard}
        onClick={() => onOpen(item)}
        aria-label={`Browse ${item.name} screens`}
      >
        <div
          className={styles.appShot}
          onPointerMove={(e) => {
            if (frames.length) {
              const bounds = e.currentTarget.getBoundingClientRect();
              setFrame(
                Math.min(
                  frames.length - 1,
                  Math.max(
                    0,
                    Math.floor(
                      ((e.clientX - bounds.left) / bounds.width) *
                        frames.length,
                    ),
                  ),
                ),
              );
            }
          }}
          onPointerLeave={() => setFrame(0)}
        >
          {item.platform === "mobile" &&
          (frames[frame] || item.imageFallback || item.image) ? (
            <MobileCatalogPreview
              image={
                frames[frame]
                  ? originalMobilePreview(frames[frame])
                  : item.imageFallback || item.image!
              }
              fallback={frames[frame] || item.image || ""}
              name={item.name}
            />
          ) : (
            <MediaPreview
              image={frames[frame] || item.image}
              video={item.video}
              name={item.name}
            />
          )}
        </div>
        <div className={styles.appMeta}>
          {item.icon ? (
            <img src={item.icon} alt="" loading="lazy" decoding="async" />
          ) : (
            <span className={styles.appLetter}>{item.name[0]}</span>
          )}
          <div>
            <h2>{item.name}</h2>
            <p>{item.description || `${item.platform} design reference`}</p>
          </div>
        </div>
      </button>
      <Link className={styles.packageLink} href={`/library/${item.slug}`}>
        Package details <ArrowRight size={13} />
      </Link>
      <button
        className={styles.compareSelect}
        onClick={() => onSelect(item)}
        aria-label={`${selected ? "Remove" : "Add"} ${item.name} ${selected ? "from" : "to"} comparison`}
        aria-pressed={selected}
      >
        {selected ? <Check size={17} /> : <Plus size={17} />}
      </button>
    </article>
  );
}
