"use client";
import Link from "next/link";
import { Suspense, useEffect, useMemo, useState } from "react";
import {
  ArrowRight,
  ArrowUp,
  Binoculars,
  Bitcoin,
  Blocks,
  Bot,
  BrainCircuit,
  CalendarDays,
  Check,
  Clapperboard,
  CodeXml,
  Cpu,
  GraduationCap,
  Grid2X2,
  Handshake,
  HeartPulse,
  Laptop,
  Layers,
  LayoutGrid,
  ListTodo,
  MessagesSquare,
  Palette,
  PanelTop,
  Plus,
  RefreshCw,
  Search,
  ShoppingBag,
  Smartphone,
  Telescope,
  UsersRound,
  UtensilsCrossed,
  Wallet,
  X,
  type LucideIcon,
} from "lucide-react";
import { useRouter, useSearchParams } from "next/navigation";
import type { LibraryItem } from "@/contracts/library";
import { categoryGroup } from "@/contracts/categories";
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
import {
  loadLibraryPages,
  mergeLibraryItems,
  type LibraryResponse,
} from "./library-data";

const categoryInfo: Record<string, { label: string; icon: LucideIcon }> = {
  ai: { label: "AI tools", icon: BrainCircuit },
  "ai-media": { label: "AI media", icon: Clapperboard },
  "ai-chat": { label: "AI chat", icon: MessagesSquare },
  "ai-agent": { label: "AI agents", icon: Bot },
  "ai-research": { label: "AI research", icon: Telescope },
  agency: { label: "Agencies", icon: Handshake },
  saas: { label: "Software", icon: Layers },
  commerce: { label: "Commerce", icon: ShoppingBag },
  design: { label: "Design & media editing", icon: Palette },
  "design-resource": { label: "Design resources", icon: Blocks },
  "design-tool": { label: "Design tools", icon: Palette },
  "food-drink": { label: "Food & drink", icon: UtensilsCrossed },
  hardware: { label: "Hardware", icon: Cpu },
  social: { label: "Social networking", icon: UsersRound },
  devtools: { label: "Development tools", icon: CodeXml },
  finance: { label: "Finance", icon: Wallet },
  crypto: { label: "Web3 & crypto", icon: Bitcoin },
  education: { label: "Education", icon: GraduationCap },
  productivity: { label: "Productivity", icon: ListTodo },
  fitness: { label: "Fitness", icon: HeartPulse },
  "component-library": { label: "Component libraries", icon: Blocks },
  messaging: { label: "Communication tools", icon: MessagesSquare },
  media: { label: "Entertainment & media", icon: Clapperboard },
  "super-app": { label: "Super apps", icon: LayoutGrid },
  browser: { label: "Browsers", icon: PanelTop },
  events: { label: "Events", icon: CalendarDays },
  other: { label: "Other references", icon: Grid2X2 },
};
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
    category = categoryGroup(params.get("category") || "");
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
  const categories = useMemo(
    () =>
      [
        ...new Set(
          scoped.map((item) => categoryGroup(item.category)).filter(Boolean),
        ),
      ].sort((a, b) =>
        (categoryInfo[a]?.label || a).localeCompare(
          categoryInfo[b]?.label || b,
        ),
      ),
    [scoped],
  );
  const filtered = useMemo(() => {
    const words = query.trim().toLowerCase().split(/\s+/).filter(Boolean);
    return scoped
      .filter(
        (item) =>
          (!category || categoryGroup(item.category) === category) &&
          words.every((word) =>
            `${item.name} ${item.slug} ${item.description} ${item.tags.join(" ")} ${item.themes.join(" ")} ${(item.fonts || []).join(" ")} ${item.category}`
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
  const modeUrl = (mode: string) => {
    const next = new URLSearchParams();
    if (query) next.set("q", query);
    if (mode) next.set("platform", mode);
    if (screenView) next.set("view", "screens");
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
              {searchField}
              <nav className={styles.modes} aria-label="Search mode">
                <Link href="/">
                  <Binoculars size={16} />
                  Research mode
                </Link>
                <Link
                  className={platform === "web" ? styles.modeActive : ""}
                  href={modeUrl("web")}
                >
                  <Laptop size={16} />
                  Web apps
                </Link>
                <Link
                  className={platform === "mobile" ? styles.modeActive : ""}
                  href={modeUrl("mobile")}
                >
                  <Smartphone size={15} />
                  iOS apps
                </Link>
              </nav>
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
              <nav
                className={styles.categories}
                aria-label={
                  complete
                    ? "Reference category"
                    : "Reference category (loaded references)"
                }
              >
                <button
                  className={!category ? styles.categoryActive : ""}
                  aria-pressed={!category}
                  onClick={() => updateFilters({ category: "" })}
                >
                  <RefreshCw size={21} />
                  Latest
                </button>
                {categories.map((value) => {
                  const Icon = categoryInfo[value]?.icon || Grid2X2;
                  return (
                    <button
                      key={value}
                      className={
                        category === value ? styles.categoryActive : ""
                      }
                      aria-pressed={category === value}
                      onClick={() =>
                        updateFilters({
                          category: category === value ? "" : value,
                        })
                      }
                    >
                      <Icon size={21} />
                      {categoryInfo[value]?.label || titleCase(value)}
                    </button>
                  );
                })}
              </nav>
            )}
          </>
        )}
        {!standalone && (
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
                    : `${filtered.length.toLocaleString()} matches · ${allItems.length.toLocaleString()}${catalogTotal === null ? "" : ` of ${catalogTotal.toLocaleString()}`} references loaded. Categories reflect loaded references.`}
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
                          `/library?view=screens&referenceId=${encodeURIComponent(item.id)}${platform ? `&platform=${platform}` : ""}`,
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
