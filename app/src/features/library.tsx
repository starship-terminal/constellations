"use client";
import Link from "next/link";
import { Suspense, useEffect, useMemo, useState } from "react";
import {
  ArrowRight,
  ArrowUp,
  Binoculars,
  Check,
  Grid2X2,
  Monitor,
  Files,
  Scissors,
  PanelTop,
  Plus,
  RefreshCw,
  Search,
  Smartphone,
  X,
} from "lucide-react";
import { useRouter, useSearchParams } from "next/navigation";
import type { LibraryItem } from "@/contracts/library";
import { matchesCategory } from "@/contracts/categories";
import type { TaxonomyGroup } from "@/contracts/taxonomy";
import { CategoryIcon } from "./category-icon";
import {
  api,
  Empty,
  ErrorState,
  MediaPreview,
  Spinner,
} from "@/components/shared";
import {
  Comparison,
  ReferenceCard,
  ReferenceInspector,
} from "@/components/reference";
import { StandaloneHeader } from "@/components/shell";
import styles from "./library.module.css";
import { ScreenBrowser } from "./screen-browser";
import { CatalogSearch } from "./catalog-search";
import {
  platformSearch,
  inferredProductPlatform,
  canSwitchPlatform,
} from "./catalog-search-state";
import {
  loadLibraryPages,
  mergeLibraryItems,
  type LibraryResponse,
} from "./library-data";

const titleCase = (value: string) =>
  value.replace(/[-_]/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());

export function LibraryPage({ standalone = false }: { standalone?: boolean }) {
  return (
    <Suspense fallback={<Spinner label="Opening references…" />}>
      <LibraryContent standalone={standalone} />
    </Suspense>
  );
}
function LibraryContent({ standalone }: { standalone: boolean }) {
  const router = useRouter();
  const params = useSearchParams();
  const query = params.get("q") || "",
    platform = params.get("platform") || "",
    source = "systems",
    theme = params.get("theme") || "",
    category = params.get("category") || "";
  const screenView = !standalone && params.get("view") === "screens";
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
    [inspecting, setInspecting] = useState<LibraryItem | null>(null),
    [visibleCount, setVisibleCount] = useState(24),
    [stats, setStats] = useState<LibraryResponse["stats"] | null>(null);
  const [taxonomy, setTaxonomy] = useState<TaxonomyGroup[]>([]),
    [taxonomyLoading, setTaxonomyLoading] = useState(true),
    [taxonomyError, setTaxonomyError] = useState(""),
    [taxonomyReload, setTaxonomyReload] = useState(0);
  useEffect(() => {
    if (standalone) return;
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
  }, [standalone, taxonomyReload]);
  function updateFilters(patch: Record<string, string>) {
    const next = new URLSearchParams(window.location.search);
    for (const [key, value] of Object.entries(patch))
      value ? next.set(key, value) : next.delete(key);
    const search = next.toString();
    // Native history integrates with useSearchParams without an asynchronous
    // server navigation that could restore an older search over newer typing.
    window.history.replaceState(
      null,
      "",
      `${window.location.pathname}${search ? `?${search}` : ""}${window.location.hash}`,
    );
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
    loadLibraryPages(
      (offset) =>
        api<LibraryResponse>(
          `/api/library?source=systems&limit=200&offset=${offset}`,
        ),
      (page) => {
        if (!alive) return;
        setAllItems((previous) => mergeLibraryItems(previous, page.items));
        setStats(page.stats);
        setCatalogTotal(page.total);
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
    if (standalone) return;
    const current = new URLSearchParams(window.location.search);
    if (current.has("platform") || current.get("view") !== "screens") return;
    const inferred = inferredProductPlatform(current, allItems);
    if (inferred) {
      current.set("platform", inferred);
      window.history.replaceState(
        null,
        "",
        `${window.location.pathname}?${current}${window.location.hash}`,
      );
    }
  }, [params, allItems, standalone]);
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
  const suggestions = useMemo(() => {
    const tags = new Set(allItems.flatMap((item) => item.tags));
    return [
      "editorial",
      "minimal",
      "monochrome",
      "playful",
      "cinematic",
      "luxury",
      "chat",
      "glass",
    ].filter((tag) => tags.has(tag));
  }, [allItems]);
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
  const searchField = (
    <form
      className={styles.search}
      role="search"
      onSubmit={(e) => {
        e.preventDefault();
        updateFilters({ q: query, view: standalone ? "" : "screens" });
      }}
    >
      <input
        aria-label={standalone ? "Search styles" : "Search references"}
        placeholder={
          standalone
            ? "Search DESIGN.md examples"
            : "Search products, screens, or design details"
        }
        value={query}
        onChange={(e) => updateFilters({ q: e.target.value })}
      />
      {query && (
        <button
          type="button"
          className={styles.clearSearch}
          aria-label="Clear search"
          onClick={() => {
            updateFilters({ q: "" });
          }}
        >
          <X size={17} />
        </button>
      )}
      <button
        type="submit"
        className={standalone ? styles.searchSubmit : styles.searchIcon}
        aria-label="Search"
      >
        {standalone ? <ArrowUp size={21} /> : <Search size={19} />}
      </button>
    </form>
  );
  return (
    <>
      {standalone && <StandaloneHeader />}
      <div
        id={standalone ? "main-content" : undefined}
        className={`${styles.library} ${standalone ? styles.standalone : styles.catalog}`}
      >
        {standalone ? (
          <header className={styles.styleHero}>
            <div className={styles.styleKicker}>
              Your design reference library
            </div>
            <h1>Your favorite sites, in DESIGN.md</h1>
            <p>
              {stats
                ? `Browse ${stats.systems} captured packages and ${stats.refero.toLocaleString()} interpreted styles.`
                : "Browse recorded design references from real products."}
              <br />
              Open a style for its colors, typography, spacing, and available
              exports.
            </p>
            <div className={styles.styleSearch}>
              {searchField}
              <div className={styles.suggestions}>
                {suggestions.map((tag) => (
                  <button
                    key={tag}
                    onClick={() => {
                      updateFilters({ q: tag });
                    }}
                  >
                    <ArrowRight size={13} />
                    {titleCase(tag)}
                  </button>
                ))}
              </div>
            </div>
          </header>
        ) : (
          <>
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
                      platformLinksReady
                        ? undefined
                        : "Loading selected filters…"
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
                      platformLinksReady
                        ? modeUrl("mobile")
                        : `/library?${params}`
                    }
                    aria-disabled={!platformLinksReady}
                    title={
                      platformLinksReady
                        ? undefined
                        : "Loading selected filters…"
                    }
                    onClick={(event) => {
                      if (!platformLinksReady) event.preventDefault();
                    }}
                  >
                    <Smartphone className={styles.iosModeIcon} size={18} />
                    iOS apps
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
                </nav>
              </>
            )}
          </>
        )}
        {!standalone && !screenView && (
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
              <label>
                <span className="sr-only">Gallery layout</span>
                <select
                  value={layout}
                  onChange={(e) => {
                    setLayout(e.target.value);
                    localStorage.setItem(
                      "studio-gallery-layout",
                      e.target.value,
                    );
                  }}
                >
                  <option value="grid">Grid view</option>
                  <option value="list">List view</option>
                </select>
              </label>
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
              <label>
                <span className="sr-only">Platform</span>
                <select
                  value={platform}
                  onChange={(e) =>
                    updateFilters({ platform: e.target.value, category: "" })
                  }
                >
                  <option value="">All platforms</option>
                  <option value="web">Web</option>
                  <option value="mobile">Mobile</option>
                  <option value="desktop">Desktop</option>
                </select>
              </label>
              <label>
                <span className="sr-only">Theme</span>
                <select
                  value={theme}
                  onChange={(e) => updateFilters({ theme: e.target.value })}
                >
                  <option value="">All themes</option>
                  <option value="light">Light</option>
                  <option value="dark">Dark</option>
                </select>
              </label>
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
              <Spinner label="Opening the library…" />
            ) : items.length ? (
              <div
                className={`${standalone ? styles.styleGrid : styles.appGrid} ${layout === "list" ? styles.listView : ""}`}
              >
                {items.map((item) =>
                  standalone ? (
                    <ReferenceCard
                      key={item.id}
                      item={item}
                      style
                      onSelect={toggle}
                      selected={selected.some((x) => x.id === item.id)}
                    />
                  ) : (
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
                  ),
                )}
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
                  key={item.id}
                >
                  {item.icon ? (
                    <img src={item.icon} alt={item.name} />
                  ) : (
                    item.name[0]
                  )}
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
      <ReferenceInspector
        items={items}
        current={inspecting}
        onClose={() => setInspecting(null)}
        onChange={setInspecting}
      />
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
          <MediaPreview
            image={frames[frame] || item.image}
            video={item.video}
            name={item.name}
          />
        </div>
        <div className={styles.appMeta}>
          {item.icon ? (
            <img src={item.icon} alt="" loading="lazy" />
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
