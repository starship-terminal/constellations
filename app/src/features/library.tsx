"use client";
import { useEffect, useState } from "react";
import {
  ArrowLeft,
  ArrowRight,
  Check,
  Filter,
  Search,
  SlidersHorizontal,
  X,
} from "lucide-react";
import { useRouter } from "next/navigation";
import type { LibraryItem } from "@/contracts/library";
import { api, Empty, ErrorState, Spinner } from "@/components/shared";
import {
  Comparison,
  ReferenceCard,
  ReferenceInspector,
} from "@/components/reference";
import { StandaloneHeader } from "@/components/shell";
export function LibraryPage({ standalone = false }: { standalone?: boolean }) {
  const [q, setQ] = useState(""),
    [query, setQuery] = useState(""),
    [source, setSource] = useState(""),
    [platform, setPlatform] = useState(""),
    [theme, setTheme] = useState(""),
    [items, setItems] = useState<LibraryItem[]>([]),
    [total, setTotal] = useState(0),
    [loading, setLoading] = useState(true),
    [error, setError] = useState(""),
    [selected, setSelected] = useState<LibraryItem[]>([]),
    [compare, setCompare] = useState(false),
    [inspecting, setInspecting] = useState<LibraryItem | null>(null),
    [offset, setOffset] = useState(0),
    [stats, setStats] = useState<any>(null);
  useEffect(() => {
    const timer = setTimeout(() => {
      setQuery(q);
      setOffset(0);
    }, 250);
    return () => clearTimeout(timer);
  }, [q]);
  useEffect(() => {
    let alive = true;
    setLoading(true);
    setError("");
    const p = new URLSearchParams({
      q: query,
      limit: "24",
      offset: String(offset),
    });
    if (source) p.set("source", source);
    if (platform) p.set("platform", platform);
    if (theme) p.set("theme", theme);
    api(`/api/library?${p}`)
      .then((d) => {
        if (alive) {
          setItems((prev) => (offset ? [...prev, ...d.items] : d.items));
          setTotal(d.total);
          setStats(d.stats);
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
  }, [query, source, platform, theme, offset]);
  function filter(set: (s: string) => void, value: string) {
    set(value);
    setOffset(0);
  }
  function toggle(item: LibraryItem) {
    setSelected((prev) =>
      prev.some((x) => x.id === item.id)
        ? prev.filter((x) => x.id !== item.id)
        : prev.length < 3
          ? [...prev, item]
          : prev,
    );
  }
  return (
    <>
      {standalone && <StandaloneHeader />}
      <div
        id={standalone ? "main-content" : undefined}
        className={standalone ? "styles-page" : "page library-page"}
      >
        <header className={standalone ? "styles-hero" : "page-heading"}>
          <div className="eyebrow">
            {standalone
              ? "A library for your next idea"
              : "Your reference library"}
          </div>
          <h1>
            {standalone ? (
              <>
                Good design leaves a trail.
                <br />
                Find your next direction.
              </>
            ) : (
              "A little looking goes a long way."
            )}
          </h1>
          <p className="muted">
            {standalone
              ? "Explore visual styles, inspect their details, and bring a considered direction to your work."
              : "Screens, styles, and the details that make them work. Save what catches your eye."}
          </p>
        </header>
        <div className="library-controls">
          <div className="search-field">
            <Search size={19} />
            <input
              aria-label="Search references"
              placeholder="Search by product, mood, or design detail…"
              value={q}
              onChange={(e) => setQ(e.target.value)}
            />
            {q && (
              <button
                aria-label="Clear search"
                className="icon-button"
                onClick={() => setQ("")}
              >
                <X size={17} />
              </button>
            )}
          </div>
          <div className="filter-bar">
            <div className="filter-chips" aria-label="Reference source">
              {[
                ["", "All references"],
                ["systems", "Measured packages"],
                ["refero", "Refero styles"],
              ].map(([value, label]) => (
                <button
                  key={value}
                  className={`pill ${source === value ? "active" : ""}`}
                  onClick={() => filter(setSource, value)}
                >
                  {source === value && <Check size={13} />} {label}
                </button>
              ))}
            </div>
            <div className="filter-selects">
              <label>
                <span className="sr-only">Platform</span>
                <select
                  value={platform}
                  onChange={(e) => filter(setPlatform, e.target.value)}
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
                  onChange={(e) => filter(setTheme, e.target.value)}
                >
                  <option value="">All themes</option>
                  <option value="light">Light</option>
                  <option value="dark">Dark</option>
                </select>
              </label>
            </div>
          </div>
        </div>
        <div className="results-heading">
          <span>
            {loading && !items.length
              ? "Finding references…"
              : `${total.toLocaleString()} reference${total === 1 ? "" : "s"}`}
          </span>
          <span className="muted">Select up to 3 to compare</span>
        </div>
        {error ? (
          <ErrorState message={error} retry={() => setQuery(query + " ")} />
        ) : loading && !items.length ? (
          <div className="reference-grid">
            {[0, 1, 2, 3, 4, 5].map((x) => (
              <div className="card-skeleton" key={x}>
                <div />
                <span />
              </div>
            ))}
          </div>
        ) : items.length ? (
          <div className={`reference-grid ${standalone ? "styles-grid" : ""}`}>
            {items.map((item) => (
              <ReferenceCard
                key={item.id}
                item={item}
                onOpen={standalone ? undefined : setInspecting}
                style={standalone}
                onSelect={toggle}
                selected={selected.some((x) => x.id === item.id)}
              />
            ))}
          </div>
        ) : (
          <Empty title="No references in this direction yet.">
            <p>Try a broader search, or clear a filter.</p>
            <button
              className="pill"
              onClick={() => {
                setQ("");
                setQuery("");
                setSource("");
                setPlatform("");
                setTheme("");
              }}
            >
              Clear filters
            </button>
          </Empty>
        )}
        {items.length < total && !error && (
          <div className="load-more">
            <button
              className="pill"
              disabled={loading}
              onClick={() => setOffset(items.length)}
            >
              {loading ? "Loading…" : "Show more references"}
              <ArrowRight size={16} />
            </button>
          </div>
        )}
        {selected.length > 0 && (
          <div className="compare-bar">
            <div className="compare-thumbs">
              {selected.map((i) => (
                <button
                  onClick={() => toggle(i)}
                  title={`Remove ${i.name}`}
                  key={i.id}
                >
                  {i.icon ? <img src={i.icon} alt={i.name} /> : i.name[0]}
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
